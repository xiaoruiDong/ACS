"""
This module contains scripts which are shared across multiple ACS modules.
"""

default_job_info_dict_after_initial_sp_screening = \
{
'project': None,  # project name, str
'is_initial_sp_screening': False,  # used to identify type of info file when read from disk
'valid_conformer_num_ids': None,  # tuples of conformer (identified by its number in the conformers dictionary) that are considered valid
'valid_conformer_hash_ids': None,  # tuples of conformer (identified by its hash id) that are considered valid, used to select from all conformers
'project_folder_path': None,  # absolute path where the project info is saved, str
'calc_solvation_sp_correction': None,  # bool

'level_of_theory': {
                    'initial_screening_sp': None,  # initial sp energy used to screen conformers, hartree, float
                    'end_of_opt': None,  # energy after geometry optimization, hatree, float
                    'sp_after_opt': None,  # high level gas phase sp energy computed using optimized geometry, hatree, float
                    'solv_sp_gas': None,  # gas phase sp energy computed using optimized geometry for solvation correction, hatree, float
                    'solv_sp_liq': None,  # liquid phase sp energy (e.g., SMD, PCM) computed using optimized geometry for solvation correction, hatree, float
                    'solv_correction': None,  # either (1) solv_sp_liq - solv_sp_gas for PCM, SMD corrections or (2) direct delta G solv correction such as COSMO-RS, hatree, float
                    },

'species': {
            'name': None,  # species name, str
            'smiles': None,
            'is_ts': None,  # bool
            'multiplicity': None,  # int
            'charge': None,  # int
            'rotatable_1d_dihedrals': None,  # tuple of atom indices of all 1d rotatable dihedrals in the species
                                             # ((1, 2, 3, 4), (7, 8, 9, 10)) indicates two rotatable dihedrals

            'coord':    {
                        'file': None,  # files with coord info, can be xyz, gjf, log, out etc
                        'xyz': None,   # standard xyz format
                        'zmat': None,  # standard zmat format
                        'arc_zmat': None,
                        'gaussian_std_zmat': None,
                        'connectivity_dict': None,  # connectivity info deduced by ACS
                        },
            },

'conformers':   {
                1: {
                    'rotor_dimension': None,  #  number of dihedrals modified
                    'dihedral': None,  #  ((atom indices for dihedral X), float of dihedral angle X)
                                       #  ( ((1, 2, 3, 4), 45.0), ((7, 8, 9, 10), 120.0) ) for 2d dihedral changes
                    'hash_id': None,  # globally unique 128-bit id
                    'is_colliding': None, # bool
                    'is_crashing': None, # bool
                    'is_isomorphic': None, # bool
                    'is_valid_ts': None,  # bool
                    'frequencies': None,  # tuple
                    'negative_frequencies': None,  # tuple


                    'energy':   {
                                'initial_screening_sp': None,
                                'end_of_opt': None,
                                'sp_after_opt': None,
                                'solv_sp_gas': None,
                                'solv_sp_liq': None,
                                'solv_correction': None,
                                'sp_include_solv_correction': None,
                                },

                    'file_path': {
                                    'input': {
                                                'initial_screening_sp': None,
                                                'end_of_opt': None,
                                                'sp_after_opt': None,
                                                'solv_sp_gas': None,
                                                'solv_sp_liq': None,
                                                'solv_correction': None,
                                                'sp_include_solv_correction': None,
                                            },

                                    'output':   {
                                                'initial_screening_sp': None,
                                                'end_of_opt': None,
                                                'sp_after_opt': None,
                                                'solv_sp_gas': None,
                                                'solv_sp_liq': None,
                                                'solv_correction': None,
                                                'sp_include_solv_correction': None,
                                                },

                                },
                    },
                },
}


default_job_info_dict_for_initial_sp_screening = \
{
'project': None,  # project name, str
'is_initial_sp_screening': True,  # used to identify type of info file when read from disk
'valid_conformer_num_ids': None,  # tuples of conformer (identified by its number in the conformers dictionary) that are considered valid
'valid_conformer_hash_ids': None,  # tuples of conformer (identified by its hash id) that are considered valid, used to select from all conformers
'project_folder_path': None,  # absolute path where the project info is saved, str
'calc_solvation_sp_correction': None,  # bool
'initial_screening_sp_level_of_theory': None,

'species': {
            'name': None,  # species name, str
            'smiles': None,
            'is_ts': None,  # bool
            'multiplicity': None,  # int
            'charge': None,  # int
            'rotatable_1d_dihedrals': None,  # tuple of atom indices of all 1d rotatable dihedrals in the species
                                             # ((1, 2, 3, 4), (7, 8, 9, 10)) indicates two rotatable dihedrals

            'coord':    {
                        'file': None,  # files with coord info, can be xyz, gjf, log, out etc
                        'xyz': None,   # standard xyz format
                        'zmat': None,  # standard zmat format
                        'arc_zmat': None,
                        'gaussian_std_zmat': None,
                        'connectivity_dict': None,  # connectivity info deduced by ACS
                        },
            },

'conformers':   {
                1: {
                    'rotor_dimension': None,  #  number of dihedrals modified
                    'dihedral': None,  #  ((atom indices for dihedral X), float of dihedral angle X)
                                       #  ( ((1, 2, 3, 4), 45.0), ((7, 8, 9, 10), 120.0) ) for 2d dihedral changes
                    'hash_id': None,  # globally unique 128-bit id
                    'is_colliding': None, # bool
                    'is_crashing': None, # bool
                    'is_isomorphic': None, # bool
                    'is_valid_ts': None,  # bool
                    'initial_screening_sp_energy': None,
                    },
                },
}