<div dir="rtl" align="right">

<style>
.tg-channel-box {
  max-width: 800px;
  margin: 0 auto;
  padding: 16px;
  font-family: system-ui, -apple-system, 'Segoe UI', 'Vazirmatn', Tahoma, sans-serif;
  background: #fafafa;
  border-radius: 20px;
  line-height: 1.7;
}

/* حالت دارک برای کسانی که تم دارک دارن */
@media (prefers-color-scheme: dark) {
  .tg-channel-box {
    background: #1a1a2e;
    color: #eee;
  }
  .tg-post {
    background: #16213e;
    border-color: #0f3460;
  }
  .tg-post-header {
    background: #0f3460;
  }
  .tg-footer {
    color: #aaa;
  }
  .tg-text a {
    color: #7eb6ff;
  }
}

/* کارت پست */
.tg-post {
  background: white;
  border-radius: 20px;
  padding: 18px 22px;
  margin: 20px 0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  border: 1px solid #e5e7eb;
  transition: box-shadow 0.2s;
}
.tg-post:hover {
  box-shadow: 0 8px 20px rgba(0,0,0,0.1);
}
.tg-post-header {
  background: #f3f4f6;
  margin: -18px -22px 16px -22px;
  padding: 10px 22px;
  border-radius: 20px 20px 0 0;
  font-size: 13px;
  color: #4b5563;
  border-bottom: 1px solid #e5e7eb;
}

/* نقل قول / فوروارد */
.tg-forward {
  background: #eef2ff;
  border-right: 4px solid #3b82f6;
  padding: 8px 14px;
  border-radius: 12px;
  margin: 12px 0;
  font-size: 13px;
  color: #1e40af;
}

/* متن */
.tg-text {
  font-size: 16px;
  margin: 14px 0;
}
.tg-text a {
  color: #2563eb;
  text-decoration: none;
}
.tg-text a:hover {
  text-decoration: underline;
}

/* تصاویر */
.tg-photo {
  margin: 12px 0;
  text-align: center;
}
.tg-photo img {
  max-width: 100%;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

/* آلبوم */
.tg-album {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 8px;
  margin: 12px 0;
}
.tg-album-item {
  overflow: hidden;
  border-radius: 12px;
}
.tg-album-item img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  transition: transform 0.2s;
}
.tg-album-item img:hover {
  transform: scale(1.02);
}

/* ویدیو */
.tg-video {
  margin: 12px 0;
}
.tg-video video {
  width: 100%;
  border-radius: 16px;
  background: black;
}
.tg-dl-btn {
  display: inline-block;
  background: #3b82f6;
  color: white;
  padding: 6px 14px;
  border-radius: 24px;
  font-size: 13px;
  text-decoration: none;
  margin-top: 6px;
}
.tg-dl-btn:hover {
  background: #2563eb;
}

/* فایل */
.tg-doc {
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  padding: 12px 16px;
  margin: 12px 0;
  display: flex;
  align-items: center;
  gap: 12px;
}
.tg-doc-icon {
  font-size: 32px;
}
.tg-doc-info {
  flex: 1;
}
.tg-doc-title {
  font-weight: 600;
}
.tg-doc-extra {
  font-size: 12px;
  color: #6b7280;
}
.tg-doc-link {
  background: #3b82f6;
  color: white;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 12px;
  text-decoration: none;
}

/* نظرسنجی */
.tg-poll {
  background: #fef9e3;
  border: 1px solid #fde047;
  border-radius: 20px;
  padding: 12px 18px;
  margin: 12px 0;
}
.tg-poll h4 {
  margin: 0 0 10px 0;
  color: #854d0e;
}
.tg-poll ul {
  margin: 0;
  padding-right: 20px;
}
.tg-poll li {
  margin: 6px 0;
  color: #a16207;
}

/* فوتر پست (تاریخ و بازدید) */
.tg-footer {
  font-size: 12px;
  color: #9ca3af;
  margin-top: 12px;
  padding-top: 8px;
  border-top: 1px solid #e5e7eb;
  display: flex;
  gap: 12px;
  justify-content: flex-end;
}
.tg-footer a {
  color: #6b7280;
  text-decoration: none;
}
.tg-footer a:hover {
  color: #3b82f6;
}

/* هدر کانال */
.tg-channel-header {
  text-align: center;
  padding: 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 28px;
  color: white;
  margin-bottom: 24px;
}
.tg-avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  border: 4px solid white;
  margin-bottom: 12px;
}
.tg-channel-header h1 {
  margin: 8px 0 4px;
  font-size: 24px;
}
.tg-channel-header p {
  margin: 4px 0;
  opacity: 0.9;
}
.tg-channel-desc {
  background: #f3f4f6;
  padding: 14px 20px;
  border-radius: 20px;
  margin: 16px 0;
  font-size: 14px;
  color: #374151;
}
.tg-last-update {
  text-align: center;
  font-size: 12px;
  color: #9ca3af;
  margin: 16px 0;
}
.tg-telegram-btn {
  display: inline-block;
  background: #1e88e5;
  color: white;
  padding: 8px 18px;
  border-radius: 30px;
  text-decoration: none;
  margin: 12px 0;
  font-weight: 500;
}
.tg-telegram-btn:hover {
  background: #0b5e8a;
}
@media (prefers-color-scheme: dark) {
  .tg-channel-desc {
    background: #1f2937;
    color: #d1d5db;
  }
  .tg-post {
    background: #1e1e2f;
    border-color: #2d2d44;
  }
  .tg-post-header {
    background: #2a2a3b;
    color: #bbb;
    border-color: #3a3a52;
  }
  .tg-doc {
    background: #252535;
    border-color: #3a3a52;
  }
  .tg-forward {
    background: #1f2a3a;
    color: #90cdf4;
  }
}
</style>

<div class="tg-channel-box">

<div class="tg-channel-header">
<img src="https://cdn4.telesco.pe/file/L5tMIbqpAf5dILxJnuZbLcyH7kLhyr1ZyyUiwPPDo8TVS8jOP9Fd7QqIhpDd7cgpI5GE0W9IFolxedC2etQYpLP4hBSgiUwJMZeBBmnz9kh02n_xFXtH-XpiRG9cND4ZBGkqYYwx3VOrEJ7h48RwJ-dqkC9T3Yf-vWnjaY2OVk3SwuPXMnte0bAcCL0zgiOucJFA5L2WUI-lV6rc2ikgshCnhAcseRUO0WxY3I-U2HjwUg0CqvI6d2oeQ68s3Wla5l-b0hy-oeNy3qEyBHt_-cpvbSIoYir9yNe66wlM5BfD5i84gEOv2XHcWMUba8FErYV_2N2iW3BCOTnOLS-meA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.8M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-02 02:28:59</div>
<hr>

<div class="tg-post" id="msg-444168">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oux9xJtxxworpRKOqkO0IGH7h8aTCSkp0-V_wXtagI4O1wig8Zji00C10CG3M7NoCL-xPD51MVxnaviboM0iMb0AdhW9ievGM695fneAJwm0h48_IDDW6Q1QJ9SKhYiTvN0iQv_CYYUMHelTB9ldX5z5Cy-ktOg3-d4oevJNo4YzZnPX07Gd_LjyT3XcxwRJ_iarZYKtQXT93IxciPc5izRj3LZQ1ebZ6SB51-i2zaq3hzu0ZXRKClD12ZBbPbiTsSCLyIlGzaBC_MVrcndkOm2XOgJbeHNZvu_PCog-qGu-t4ybbTL38XpZH1X-m2B3Gbw93ag1UGRMBl0QznxQBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XnbL1_HvO8isuVuVs76Q7uljkArUMAhD6X204X_4ifNlhqU0a3hTjUAGc2LLPMrnOJBShYlEnrxo3o-IsRFowixd65Ro0VwPzADHMldW_2HN8xnNpRuK3MnZNM1UoLz8QNCRLEiKLRxi0uMDy6X3qa97cb-8bJToTV-y1cmX5TwdLVWnJ1cmtDsGNuz4b0XCdMPEPntp8q2u2UNvUxTvNYYTMVVpHqDK1jVqobEtHH-tCrljxAKM22D5aasHjDAu4bAK-8h6L3NOnw44kpU2KkfiTc0oP6PU_nJs4omr4u7q2W8-FI7XM-w6eKnHo_uNrvj1WkqKQw439PGHgim53Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y-xLgYPvBBqUtj3vZBYURpW7v9U1M7_W9v0VF2NX5AVCO2TupAGCavHu0ZHMbwqZzNLGcXKfYq9IH6phquSR_wbDafJHFPNHSYdN8tYM6GGwM9tfcFJXzzuzgUf7i6s-4R2Aou0fRootBjk5bvBODA-MLQ3GG5iRlM0F1pM1ubfS_QB4sZvMOYGTu3BdCyi1m_fLQ5Vn7le34U43xR0o_EBLoq4gl_ICCxqmBSxgvVpVebG0lWdSu5heOuKAjLwu1MELO8UDzLd1zgvTGV_Rmf6L_HIx3x8LXx3HosIWHyi8cFqgaO1yBu8RNaRkaZdIIb-KiLjoDq9CmRpqb-jONg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K4sj2lJFLjDLDALIqjH8lHaPsLlZ_fSrC7uMI4jyIABDXT6tNejJEe_ETCCCRWHiUF4tizIKUE9tk7w7zCPv8lB5mEdFZUkVSLbtltEY4toB8K_9673vCxu84MlrqgzUlDDcP_MzGEI6B_JmRL0Tpu1HGVQPx7lqjXy57aZTnQefrz8IXUz-bbwtx8ut0j3gCen1nS6pHVF_tEZfOX99BhbnTGR5ZaiUVErHMCOfuRFSRJd01sOODLrahOSksOFSMNFPofE9pugIU3XiYU7aEtYCD6sKpbZJByI2kEGqPnhvnrzCt5H7UEyQdn-hv7RSp3BkSAW_zBcja38oPYAZ-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nVPJ2PqQHfuCVyzTv5xWlea6EwSqKmCZJ_74v6fInNICbiHd3qDhNwUh7RumEDw8LBR6apa1HNp-Hh3XbZ3StVCHF7CjVnV7X2zfnMzntyzWbvHZgV3JO3srw3AJQwY_fnTQaVxVyf4GONizASyROgTSposSaQZCaSWCbbgWjcld6wFG3HQOZ1pAyu8tJXLLC4Q8bboLu1S8WrZPwuc-72ZC9VzTd7i_dKmiNXf-GI_FFoWmVcdrBIWQpXSjly92Pzya82bJjafn_kakW0lerGZYFiaxgfJNKzD4KF-2u_XmIOW_5FpadMDpc12Efla15w8fKe7pggN6Zh-0q4s3Yg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | سه‌شنبه ۲ تیر ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 411 · <a href="https://t.me/farsna/444168" target="_blank">📅 02:21 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444158">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fr7C-3ooeudx2Zg9WSAwNTF6_r0nS4Sp8_nDv_rp347l8vJPs94A-lC43Sf731UsrOLwOQjluB0w4pac1GC_3AiWqRxsSKyBo5zaZ8Z_bNN349HtGzOX-wx4KJ8umhcGLKcN-2VL9usEyzSdte6YpxWmNdVatrLqOEnebESJ3w2KkqDTirZx1SGvltfCLz9EW9-SyYdZgl5ccpBjQ23S5PqrZ-p0co3bc8j45b6FQ_dhinWfCBPBAGi87fLrQnSmHOs9epuhSeZxRDKt48-RdsLXRj-aMrwkIE-pcSo3SQAinJw1hOh0bQ0tDT-SLBNmPsIhKJsKJu2bWaFdW-bYEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MlZhb-j7dKQLoZOmcU9lLl9ldvH-Fv_j_g_aJh2jJJymzPutmpG0LdWmaZBBqK2y3Q7yKE4EfHEU8CIjBdjoW3gxn4j1l34g7r67Yvskr_b5NdHHzT-8jH-mpz-BLaKnyA45QaoV-8_JphFODaGVGFAr3_2x7azBh1xXTvzU_TFFqYe1dPCOTiOPMaC1aE5HGMdMfDkaqSMQLUJf01kJFuZTDrcD7-tXsy4Y1jnomVcyL-TpqxJ8LbqbatSt3biX8Xy6fuFIMgplMWf5u8b1F1wEa9EtRfjw3bAsXq-M275-8Zh-oOiWkda2oSKEcdOVDp4oiKyitpjuh19JB6J0wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ohuy3xOLWPL_f2dDO1trCKJ6NIZAWUl0wc0ZL4mEEooqoZ2Da2wIjmjEqKXuDMBW7EEgJbH6xMJLLTmIq34Dv4GXVuUSIe7ptu8pFTuJLDzJn9KS6jhky94fignT8QOvxKgbS8DuArnFA-BKk-MZFC191Cxy6VKNW0poYOWVSFRU9IHaNHu0dFZmsdnAZvhqtKJAlTKotm_FFv94yqOjn9wrfDC0w4cHTRtmf5wP9piuFNbbI68-zUt4vPylIuSMl45tJZpeX27fQhapbdiAR9mWloZh7IvqzSQIjcovKUw-f8G2-igc2PYr94RajJSoQv4GBk4hc76JUSML_Sz9zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/knuZKTED0OtG4NiJzDJNBUzcK-pGuopude2Vx2GAIo9U129cs39RfUDi4cZBtKJi05RbDaoIQZfjCXyUlQPpI4R3Nj6Pb7LOe1aMLLdplzzSVTZsDHY0GyXBLMjPx3cCPDR1wNn5ZkKShVlghsvgYokBSrNw_j3DQhLKrDzM3aFZWZaFwXIwwIIl413fCH9YHmbc6_r3BWOQNRiuu5JtaxZp00bPTS5-Z5p4NcVx7DkVWp_Bj9F4_KanwCDFJ0urn2x2NDNdC3GMI2i_7D7Y6Ldzn8pFsPkx7JC9Hvkv3ZpJxgSgb32kSKae2x7k7e5pTIftBkJRd_S1vI_Zma_NPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T8dAbTlCcBaggRqNA86hZ2bySbOHpz4m9Nk8lQYnhMvRTaPWCx1b7DHhvgPW-BlpjlI387a2jSL-Z2aXTm1Dx__081Saaqktkqqlw2b0m4Fmi4HUypVmA_gIAQvrhwigh-6GbD6bvJ70JRFrMu9nbNZYKv7i6D4GxP_IbGyprj8Y-MJzHysLBBxl5ssRdsxOZlxENtZfG-Ppw2eyErT0nzrsFpSqb8ONBRwqb8L64Xe02I7cJy3BpmCVqxPwMnHkWYw_592P7ASyoURhNs_rNEp_-8DaxZ2s63pEEamvTsjrCiefLR7TsiuTVpn85d1S-0bS1FOpZZHOvxkVRRulbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n8uKcGXSryejsvgQ62yS_-nZodbSj1NMVqGxLjz4v5BZ9VbmAki5nCfWYybOMmJvRlB0QjGXHWsqcRlkPbhdJU3xdgpFwn8RZEwhkiOq_7TzfnIvbGO9xQPaOFVizvGtDYbxmIfInMz3hZrZ72-oxdG_A1ghz48ney7YCbTx8wkXMK1GmgbWoMI63x5A2W0sScPZBO75QuyA7CeWdY8cF7a8NU5l3_5MVEGNgl1gX_JE6nUJ2-RVJsBE4JowZ_eHhfpg6VMW2P2_df4ok8u8FC4fzFOoDa3nNSvxgG49ftI_OKv-B7FYZa2bsoEyeXc5MdwlLnFCYdE6dJRPugIoPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cw_P9adgdbIuYFcS4PNiwUaAk2Z-u85gGY7PmlSDwg5wWXKjC-9t1ZzxVVoN7fs7Kx5C2Emcu51h0JaNSmHpnJo_THYcVDHOZE439HivO6_HtRiwEJA1wqWEhs9mYWhrqqOLYYQ4DVp9xfAG0pSAXfOssh_HrgrXs3cX5k8GBG4L-rW9odAS6PddwxdN9z7RaiaJ9vmycNdjCJgjFOnStiEvpBz7Ee-7uCAsNQLEh6sc5DVZzXQcTRy0xvGAdPLvSh0_ZJV-LgHe7kti5IHctLL-lUZXpcsICH8fjeLTSrovo9oVXUX93mAizab3SCNLs9hIbxWOPaYPhrunXxeUAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SdOTemeDyr0vaeJkKVlrK9IvtL5PEfcKIDiKzBNSrONOy5TBwMkmD8IKT5pezuie4WgkfbSPfG1jFtPtGT36OJ88mLe2YhASWHFlg_AnHK5mOv4bEUamac1-s9Ww2Pyn5Qu5mLIXC0jK2foXsGB0GETbBMuJooyAasyi6mWldPNwZPE6y1RjFVV6O4LKjlqUS8HWcHcNoqZWN80p_GgEYqzm_vOhLriOr6TL2NxI-8uRRwHaoDlZQkZ5lvfEGDWQgmDiMwNn8b8jXngr_0obDI1STgt9rkUL-EBMg8Lap2l7CVT1yN_PByW4L63xAx3Ccd-61fwMlO2nEtwHofF1Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iMrXkmADi33FQMsf_VE67rA3c5vOURRU3hJXD8her_TFohuskHNZsxQ7my6XE43pyXancjbNs9-zmktDQnVAz-78DiYZ_AZYH-4UK9TKh3MJ8CdwhIo4Ut4k6W9JQ58FU1r2n_AMncfLJhHj6CYXpaEaFRfkvpr_-No1rn7CZyOYiaDtlf2RWoCODRmRxV0hWe8Su-FU_3COhGVExhrDLMGxrxdrtku9zJfcO9IGVpHw7rQrMAxqvrrnJguQvLzmjl1MX2xWnt8i4HStwsbi8T6VPxa-7euxYWPU4Q0KYSZoV1oCHUKzQ7SGYoPBIXJ3sfazbhVXMruGBrI4pSw81g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qDlUS8QNjA6LFuXfTBGOJurFFIcdu-vWlIuoP_jVugTD-B_xHcTOcZnzWnlSgyCin3soFtrfjaV1IYI-1ybSRe_tImKzrjVo7y28qX1EyHKPfaWPFylinSbrCS1StRwycoUMp20xP436-mJLWFwAN7-qgWA7pSm4NMVJiuADKHwSmgAxs_xmObYzSszsY1VvouTkzhyP2yKEVyO93nLkAyx7zqbxmeLLj-lrl3iygThr9QjQilcVWrcJYerCzbLWwbM93Esc2PmgJoUGayD3U3icepAqccRgE-66HFyU78PMFJ9TXiDqqhMDFzTQqjQLI3lyXF5qjOX6hlWNAsNdUQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 412 · <a href="https://t.me/farsna/444158" target="_blank">📅 02:21 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444157">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔴
وزارت خارجه از توافق دربارۀ ترتیبات مذاکرات آتی با آمریکا خبر داد
🔹
غریب‌آبادی، معاون وزارت خارجه و رئیس هیئت مذاکرات فنی ایران: قرار شد تفاهمات امضا شده درخصوص آزادی وجوه مسدود شده به مبلغ ۱۲ میلیارد دلار (دو مبلغ ۶ میلیارد دلاری)، بلافاصله وارد مرحلۀ اجرایی…</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/farsna/444157" target="_blank">📅 02:08 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444156">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dZCZbMQLnDEK11XlJOr7_HhUDZobqC6mWfw6qh0joG9JZVzHTQjdgPA6YzoKhoNliyEXoLEGEP5t1894RrCK5KBSygyVUPRgdJO-Qw2je4K7hoi4f126ERCWX33I2k1ksVt4q5oE0PjsmRcHmnV31zKsvxmy0aO5rgyEyR1AaKzFd9GjM-y_2BKzq2KJUPtPVMXSystrmQYjFK8v84ZWTulE4Y-K743zqQEOrC04FBR7hebC3lb4dlN2Q750COlVIheqcNuKLpfIlOf18mHCDrm-TWgsE9QNgv1ZdlnGR84TnKfUMTPrmh1MtDxWHLLocp9LSoZ1f0b6wUCNai7Z_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
وزارت خارجه از توافق دربارۀ ترتیبات مذاکرات آتی با آمریکا خبر داد
🔹
غریب‌آبادی، معاون وزارت خارجه و رئیس هیئت مذاکرات فنی ایران: قرار شد تفاهمات امضا شده درخصوص آزادی وجوه مسدود شده به مبلغ ۱۲ میلیارد دلار (دو مبلغ ۶ میلیارد دلاری)، بلافاصله وارد مرحلۀ اجرایی شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/farsna/444156" target="_blank">📅 02:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444151">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RvGNsYqBeqyLvfQvUH5yv7S_twESpvE5kadQCAERZXn3HR0wa_ZbFxlYbTRKyCsDhBdgH-naIw1b1ZOirxTh6J85BR-3AiYu6MNba4eZRgVJXPFd35QnPs3FXvMZ47uCO22P7r0iOnsGYHhNYVy55K9PfK7qLmbBz0ECQ7Ply8EaWRIsdyHfu-ZAk9MZ5COCD9wK17CsRo9CUPUzI-SsADLb0_12lI7D5QdwWDNpHZLPrhSXEg98KMx7w74PnXe2hQfWaPkwr3UtG-g4QQveA8qfd84_zSJXOHURhp8PRWyv5UGlo89eW72zP7YMIZaK0cbDdNk179lmcKnUfsYapw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uylvHx8ouL1sDOm6gHtMRTQeFNjTdK7p9emLoypf3tV0XH-lfGUMax-6AiavbDzEdg81nuoMh69MVNqKadjZoFHyoiDvlPMeJ46GUFJ0E5cwVrHJQCbjjF3J1zK2kEJa9KoDwy1WtQJwBz7tlbMH0aMYQKM4pDGKueaAfj3kg3VHwHwlx7WAAsmN38Pgjig2mSj4Lf8SUn6sQVPVR9f3BoEgPWxN9gueNCvnU-h2u8K0ZUEZx__STo_D5v7xuQYNurO7i6VoDkj2ooLQ7s2BxoKbtJCdNUv93dWpPu_EzPPpUaizwugT3QOh9xCwH-kwYDbMOiOvp9QkXADhlz4VtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d5bvTRbmjAPWgSOIkeEx8fcILcFibCNTF1gXbdiToGI4qop8NunAjwsxMl1IBfvrOmB5Sefi3cLMHxfRC4wm4eZkzlbjFADPq_3wUbS6HJ0nyD62RxzCNGkTt4i6fH_H4cvI9Lfo2-bQAwVw7ZvRsEZ9HQ4_psOXvH73NDd-4vZ_-exnLmSylFNOZ69OEr68dKOHWdklvBlqTS_5v8RdDsNEdMAEjTM4X80oyLegetEeE-eCLc4ukNG_KTBy8MCPC4NEz8PKMld4T21ugqkamaHK01AV_aiX7dMiHicaQOipJYxUhqA7yRvS1PT7WZ_-yPwhwLtvplTO7CD7UTcVIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LHDe7LTjTJmgWfwxeu4bMz94B8-89LbLrtDTR26u9MIhByUUWoPrPFgNTAX4_MjHt9uqf8IwzB9me91ZlJSRG0PN3l7D5C8-JJvx9TIL3BMxN4-Nxt8x0GI3558A_2c2TgcmzmMEelzaTZN01oinBGmUgVn4OarBUwuFmm9IXCqfvhiWKk2HZFBmJcHylbmy0U8A5guzZWAriT9rJt9IdN0jkUAzaQSdugTpACQ67_nTIUbMBWbU3FssiVlOhGLShMMKW1AkbmvyX9UpAJHlCsq-q5eAjI1dsNtISd2aC232E4gOBbaZLJyrbQumoFshO04FZFu7nHkq9PZXf5GXtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZlV7hV3rEvxSJH_KBo5kWDHYX1l1k_Rb2BeHV7SpJ54vOUWrLROwnMVR22N-9SIrYF5Kt1xOLntsYx7ch5sw6egGwlxhx2jLwmwyk_2H1f8CLng0srA7slRd2MbQX0hTzP2j3B4mo84P7EirY5yZli2WscTdu8549bcFSZ_wbQOQMK3qlCQeab-k5yxi26-RtTcCx3mCiF9muVWS_7zmsi6iah0nAS832rD20XHGBaxRMKhNVlDVrR7-9-4imY05YfooBmc-61TbecV6RRLQkXhT1S124muhFR4xMUVMDTXd81Abot8dfsz3HOSymJYBGO0EvFsWtZbu1p85Sgb6hA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
استقبال وزیر خارجهٔ عمان از قالیباف در بدو ورود به مسقط  @Farsna - Link</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/farsna/444151" target="_blank">📅 01:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444150">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4b8757089.mp4?token=iPJg397P15_aaLZuJBeZTLXjRf3aTg0mM3j96ZmYcRcwLuZLV1v5QGT7oLFaEOfizePHcYmap6-u6ZYdTJ9YvrmBKSPRZpNHGL_De5qmteavSjJyM_kxkOGvGwNNnosBZgd2bW_uF2p6_69XAUqedyENoJsccKlfxDk_DWsIIK8tRaL_TdkXSRN7h3D3p-gmYm9DTJNOknVc4S1cbXLYJsiJnaQyGcA0hLb4v5iv2CHup5OxdlsxCQm_1BR54BglyJ3IFqZVfl-6_Aza4es3LqwazKrOPygvt_lCNmXxe-0M_BAGCiiMo87BLXxMC0QSdcKtMVn6g5cx5swUrxjuiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4b8757089.mp4?token=iPJg397P15_aaLZuJBeZTLXjRf3aTg0mM3j96ZmYcRcwLuZLV1v5QGT7oLFaEOfizePHcYmap6-u6ZYdTJ9YvrmBKSPRZpNHGL_De5qmteavSjJyM_kxkOGvGwNNnosBZgd2bW_uF2p6_69XAUqedyENoJsccKlfxDk_DWsIIK8tRaL_TdkXSRN7h3D3p-gmYm9DTJNOknVc4S1cbXLYJsiJnaQyGcA0hLb4v5iv2CHup5OxdlsxCQm_1BR54BglyJ3IFqZVfl-6_Aza4es3LqwazKrOPygvt_lCNmXxe-0M_BAGCiiMo87BLXxMC0QSdcKtMVn6g5cx5swUrxjuiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
شرایط بد جوی و خطر رعدوبرق، شروع نیمۀ دوم دیدار فرانسه و عراق را حداقل ۱۵ دقیقه به تعویق انداخت.
🔹
از هواداران خواسته شده ورزشگاه را فعلا ترک کنند. @Farsna</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/farsna/444150" target="_blank">📅 01:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444149">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">کتاب آه</div>
  <div class="tg-doc-extra">قسمت ۸</div>
</div>
<a href="https://t.me/farsna/444149" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">قسمت ۷ – کتاب آه</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/farsna/444149" target="_blank">📅 01:46 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444148">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PJDazWypxhsNQ1VFgNU7WYWOywd_wTCgpV8oW23KP9iTtXKl5XDB6_ovu908j1P7Riq4KygDTyqt-E_DD6vWz08hqh9yAJXDDP71xvyF0-RUwBws3pm-d3UuJtb-Qg1bjq0KPwBiqJ4oPF-4un8YWFMGwxfd9MvbATaCI109-loQVN4AfI8XkQONX-kv3w_Gbb11VWM5C5hdAKr0nAUdeyIVL9Ju0u727hzoYwaXh0jPgUH7yMY4dtmt85nkaL1ds3WoTUPh6sIV4_O4pbGGxXmm7GOM_1hhugu-duJB6ydAsPp-B7A9ZvV0He1h7uo2BJEFRF7PBatSB7pgvSbqOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
شرایط بد جوی و خطر رعدوبرق، شروع نیمۀ دوم دیدار فرانسه و عراق را حداقل ۱۵ دقیقه به تعویق انداخت
.
🔹
از هواداران خواسته شده ورزشگاه را فعلا ترک کنند.
@Farsna</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/farsna/444148" target="_blank">📅 01:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444147">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b8d941003.mp4?token=JJ9hP2nzJC4HKgnlMZEj6kxGUNkIf-GiZcPZNb1tFJrbXJ5dh4HRTn4aqlEIqyf6Wt28aSOs2kPNtYup99DRIXcfRpLpFNATpwWruT_0Ddhwm5TCUSjQgnaGelXWgR2B5wRqgC5JhBi7KzoAyfT3x9WZtKSFVZ_7IIbKnchp0xpUM48bnuhWRq3WJUkX7inCH9d6MaGDP4MudZr-d0o75F-nocid2EdXSZpcagzg4Ngjxb8okdCCOMjUEmKCAIY1gVE7N5NcZ4Ajr7N1m9fSK9Zn30naRnffuT4E3XwwfT40EXmjnTecYbFuyHIeKjzmHURLh3s2FTNXjym3FvLzjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b8d941003.mp4?token=JJ9hP2nzJC4HKgnlMZEj6kxGUNkIf-GiZcPZNb1tFJrbXJ5dh4HRTn4aqlEIqyf6Wt28aSOs2kPNtYup99DRIXcfRpLpFNATpwWruT_0Ddhwm5TCUSjQgnaGelXWgR2B5wRqgC5JhBi7KzoAyfT3x9WZtKSFVZ_7IIbKnchp0xpUM48bnuhWRq3WJUkX7inCH9d6MaGDP4MudZr-d0o75F-nocid2EdXSZpcagzg4Ngjxb8okdCCOMjUEmKCAIY1gVE7N5NcZ4Ajr7N1m9fSK9Zn30naRnffuT4E3XwwfT40EXmjnTecYbFuyHIeKjzmHURLh3s2FTNXjym3FvLzjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پاسخ مبهم ترامپ به سوالی در مورد اشغالگری اسرائیل
🔸
خبرنگار: نتانیاهو امروز اعلام کرد که نیروهایش لبنان را ترک نخواهند کرد. این موضوع یکی از گره‌های اصلی و نقاط بن‌بست در مذاکرات است.
🔹
ترامپ: این حرف را به چه کسی گفت؟ به شما؟
🔸
خبرنگار: او این مسئله را به‌طور عمومی در اسرائیل مطرح کرد.
🔹
ترامپ: خب، ما قرار است نگاهی به این قضیه بیندازیم.
🔸
خبرنگار: خب، چه اقدامی انجام می‌کنید تا مطمئن شوید نتانیاهو اوضاع را بدتر نمی‌کند؟
🔹
ترامپ: قرار نیست به شما بگویم اما این موضوع حل می‌شود. من آدم حل‌کردن مشکلاتم؛ مسائل را خیلی سریع حل‌وفصل می‌کنم، از جمله مسائل مربوط به نتانیاهو را.
@Farsna</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/farsna/444147" target="_blank">📅 01:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444146">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">بدر البوسعیدی: با قالیباف و عراقچی درباره تنگه هرمز صحبت کردم
🔹
وزیر خارجه عمان بامداد سه‌شنبه گفت که در دیدار با رئیس مجلس و وزیر خارجه جمهوری اسلامی ایران، بر تعهد به قوانین بین‌المللی و عبور بدون عوارض از تنگه هرمز تأکید کرده است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/farsna/444146" target="_blank">📅 01:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444145">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3761e2cf7a.mp4?token=tVaTw1DaDji9XU-9nD8dSACpCWK0CWJJN9tJAmOul54eERs48qISszu9fCHVFVNaeFcIAVbMvQzqIjarWWktyr0lBfj3IrSsR7Lae2u_1TFdh4xMzRsMVG49anJkWYWGSQn0SIgmj32-sacZfBtTrdzNtVZZFndZTzjIAxs9q4mgt49Ad4-vfKU5nXpaUGe4U3-WUhF-1P4Pk6VEQbzfKcFZyiqFTyofP1ylpAbaTgSsiEgUryjLeDC59QL5n6RNEaGeBhP-DH7-EnC1W3pRlsIjLacq-vRl99tL8auX-m79vEAj9sppXi5m1qUjXeLLPAbPvOZ4kh37j8Kf1qpITYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3761e2cf7a.mp4?token=tVaTw1DaDji9XU-9nD8dSACpCWK0CWJJN9tJAmOul54eERs48qISszu9fCHVFVNaeFcIAVbMvQzqIjarWWktyr0lBfj3IrSsR7Lae2u_1TFdh4xMzRsMVG49anJkWYWGSQn0SIgmj32-sacZfBtTrdzNtVZZFndZTzjIAxs9q4mgt49Ad4-vfKU5nXpaUGe4U3-WUhF-1P4Pk6VEQbzfKcFZyiqFTyofP1ylpAbaTgSsiEgUryjLeDC59QL5n6RNEaGeBhP-DH7-EnC1W3pRlsIjLacq-vRl99tL8auX-m79vEAj9sppXi5m1qUjXeLLPAbPvOZ4kh37j8Kf1qpITYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: بیش از ۱۰ میلیون رأی قضایی در معرض عموم قرار گرفت
🔹
اذعان می‌کنیم که هنوز به شفافیت مطلوب و مدنظر خود در قوۀقضاییه دست پیدا نکرده‌ایم، اما اقدامات قابل توجهی را در این زمینه انجام داده‌ایم.   @Farsna</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/farsna/444145" target="_blank">📅 01:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444144">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🎥
اژه‌ای: دیوان عدالت اداری حدود ۲۵ مصوبۀ دولت و شوراهای عالی که خلاف قانون تشخیص داده شده بود را ابطال کرد.
🔹
همچنین بیش از ۱۲۰ مورد از مصوبات شوراهای شهر و روستا که خلاف قانون بودند نیز باطل شدند.  @Farsna</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/farsna/444144" target="_blank">📅 01:18 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444143">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce9296f446.mp4?token=WAx02Fn3r2Sda6LtYr9rsmI4ZUo354MSx8Fkte6ghvZFEifu0YmbIV_CAHL4OAoPeVmotfH_klr-1a-jOgXVQtDqV9he6vhpgwfTRBAt2N_M1D2nC0yHuQwlHS22Pj_dWMMPXANWNcN4d587hAUMkOL2l2bbnNBez178tNsD4fodls2GKHVX5yjh7TT4OO3YWFeje6zcu38fe7tArIIelmZ_cof6Savhd_Uk51fCMhUgd_5HJTrpr-57alFD_rxXrgcfVjZP65AzUXT6rdFqKCgLQlBgZuSPqO7HTB8jlOc9UBG4a2Bh-r9_6tggMExae34HngjvkARBmPIw_qlafWRMeveHAEvd88cOoqXFXf8FWqlZbKBKCI3MpjICbhdHj32vsHMSZHYT6A6ZTBzJe3XIg9CJcSiffcl_rc5ZMz0peIOCxUcyZr5nW_VZINj-1ApWOBlbVtgRxxdO68K2KzCssU8HbSPZvCPIhsvzpfFzHI_sHrDtzJ07TpX3cyh6Lzp0R08P2hWflyHOW4uwLUDkOQKi8T5R1CTvJ1vAHhGWbiuJROL8KTcR7PdJ7IyG1_hQQE8SVXk73BmyI395kmD3a4Sy73ZwV1jb23O5dq2b30VLrljLXS8HpWKuXcO2YXvsbNg2Gz3y3OkBHjlGN_riFRVQaGaE6wSk2yemb9o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce9296f446.mp4?token=WAx02Fn3r2Sda6LtYr9rsmI4ZUo354MSx8Fkte6ghvZFEifu0YmbIV_CAHL4OAoPeVmotfH_klr-1a-jOgXVQtDqV9he6vhpgwfTRBAt2N_M1D2nC0yHuQwlHS22Pj_dWMMPXANWNcN4d587hAUMkOL2l2bbnNBez178tNsD4fodls2GKHVX5yjh7TT4OO3YWFeje6zcu38fe7tArIIelmZ_cof6Savhd_Uk51fCMhUgd_5HJTrpr-57alFD_rxXrgcfVjZP65AzUXT6rdFqKCgLQlBgZuSPqO7HTB8jlOc9UBG4a2Bh-r9_6tggMExae34HngjvkARBmPIw_qlafWRMeveHAEvd88cOoqXFXf8FWqlZbKBKCI3MpjICbhdHj32vsHMSZHYT6A6ZTBzJe3XIg9CJcSiffcl_rc5ZMz0peIOCxUcyZr5nW_VZINj-1ApWOBlbVtgRxxdO68K2KzCssU8HbSPZvCPIhsvzpfFzHI_sHrDtzJ07TpX3cyh6Lzp0R08P2hWflyHOW4uwLUDkOQKi8T5R1CTvJ1vAHhGWbiuJROL8KTcR7PdJ7IyG1_hQQE8SVXk73BmyI395kmD3a4Sy73ZwV1jb23O5dq2b30VLrljLXS8HpWKuXcO2YXvsbNg2Gz3y3OkBHjlGN_riFRVQaGaE6wSk2yemb9o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: معضلات ۴۰ تا ۱۰۰ ساله حوزه اسناد و اراضی حل شد.  @Farsna</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/farsna/444143" target="_blank">📅 01:13 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444141">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3198d874de.mp4?token=Nb3unjZaCf8oqWumAksXhX2UVHd0sf5GXIKLn4ghmyojqHHZOwKf7u7gf16ZL9wBPZEgCrWm6I8ySZvdhH5RfKn7JuEdTXdCvjbvLdDPM6n3n3fjzlAjt2oZqiUZxl28lixkWnth90QAewe2ZS7cO5pVAOr5MjXXQabORKiiYPQL8x3y4KJNR47m3kbmumPif65JrxjC8bAXWTiUPJ0XnYaBd5SqVktSKqnPosAnP3iQgJoUFex-YWDiycNZbYjIIBhnSVWEeIBRgy-UHW-3VcuaFo05Z0RDXvmMCNwnmZpGibFNmc4g5IdY3KOXXrpS_jj0a0BeSvp_eqiOMjHz9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3198d874de.mp4?token=Nb3unjZaCf8oqWumAksXhX2UVHd0sf5GXIKLn4ghmyojqHHZOwKf7u7gf16ZL9wBPZEgCrWm6I8ySZvdhH5RfKn7JuEdTXdCvjbvLdDPM6n3n3fjzlAjt2oZqiUZxl28lixkWnth90QAewe2ZS7cO5pVAOr5MjXXQabORKiiYPQL8x3y4KJNR47m3kbmumPif65JrxjC8bAXWTiUPJ0XnYaBd5SqVktSKqnPosAnP3iQgJoUFex-YWDiycNZbYjIIBhnSVWEeIBRgy-UHW-3VcuaFo05Z0RDXvmMCNwnmZpGibFNmc4g5IdY3KOXXrpS_jj0a0BeSvp_eqiOMjHz9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: برخورد با محتکران متناسب با شرایط جنگی تشدید شده است.  @Farsna</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/farsna/444141" target="_blank">📅 01:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444140">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🎥
اژه‌ای: دشمن با جنگ ترکیبی به‌دنبال ضربه به ایران است.
@Farsna</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/farsna/444140" target="_blank">📅 01:08 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444139">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a7a3f7b60.mp4?token=oF8TYim_jQr3SgJ_6an5tmsF4VbhwclsWDdOtAv8-xbG_6nQl3qGmA9cwYW5GmNT80mBNMNHWrZs6XXmloNmoz0IUy5SCvPZmsc7yR8cj4M6QIUVbxGbUSHlLPkWebEl2jwSLQxRYvk-sf7L8NNuoxMi7aqTuguje8njxpeyu_9almp5FOJYBL7FQHUBrhaE8EhJlUojTv2eOFAfGBi6qYJeQc2ikY3F4HQ-nMzrYmH0tSgS9oRhSui9sY9vDMMHLdOr5um2JqImD7DiC1ZHaPZeZEoMQbFM6oNIoZKA4POj2wKTh0SydevlKoMPq67_fK4lwL4-IIbL74CcyXMNUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a7a3f7b60.mp4?token=oF8TYim_jQr3SgJ_6an5tmsF4VbhwclsWDdOtAv8-xbG_6nQl3qGmA9cwYW5GmNT80mBNMNHWrZs6XXmloNmoz0IUy5SCvPZmsc7yR8cj4M6QIUVbxGbUSHlLPkWebEl2jwSLQxRYvk-sf7L8NNuoxMi7aqTuguje8njxpeyu_9almp5FOJYBL7FQHUBrhaE8EhJlUojTv2eOFAfGBi6qYJeQc2ikY3F4HQ-nMzrYmH0tSgS9oRhSui9sY9vDMMHLdOr5um2JqImD7DiC1ZHaPZeZEoMQbFM6oNIoZKA4POj2wKTh0SydevlKoMPq67_fK4lwL4-IIbL74CcyXMNUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: با ورود قوه‌قضاییه به موضوع ارزهای صادراتی و تراستی‌ها  ۶.۵ میلیارد دلار سرمایه ملی به کشور بازگشت.  @Farsna</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/farsna/444139" target="_blank">📅 01:06 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444138">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdf51c89ef.mp4?token=vJ5fj85tALjjNuhsgh5b_Rg3vo8R3Kdp--6ymDq4ItkV2_HetmtBKjkA9tmx4JJp72ylP44WImQfQPVo1RQK2py4gTarAY3AjviWkvlMo0XySEWHtFdlEhG_zmLnrJMFdjnWtbBHhd239Gf7hwrIjhkJEcHfVho_QMQhg8qJe-8SXwhvld1aCpFag9P8PTEraq0Wx6RVYq_moh9OtWTEOHzdliEJXI8ZnY1-au9y7gETw3H_21MROVybriy3ik-50HZluIw3Ba84ktAjhwRM2ASqRB4LPZmifl8ZJiR3WdMz0KbRFQCa8S5OhGn3i9wlgjQrUbi_lBOh9YHQ_CEZKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdf51c89ef.mp4?token=vJ5fj85tALjjNuhsgh5b_Rg3vo8R3Kdp--6ymDq4ItkV2_HetmtBKjkA9tmx4JJp72ylP44WImQfQPVo1RQK2py4gTarAY3AjviWkvlMo0XySEWHtFdlEhG_zmLnrJMFdjnWtbBHhd239Gf7hwrIjhkJEcHfVho_QMQhg8qJe-8SXwhvld1aCpFag9P8PTEraq0Wx6RVYq_moh9OtWTEOHzdliEJXI8ZnY1-au9y7gETw3H_21MROVybriy3ik-50HZluIw3Ba84ktAjhwRM2ASqRB4LPZmifl8ZJiR3WdMz0KbRFQCa8S5OhGn3i9wlgjQrUbi_lBOh9YHQ_CEZKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت رئیس قوه‌قضائیه از تخریب بنای متعلق به دستگاه قضا برای آزادسازی حریم رودخانه  @Farsna</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/farsna/444138" target="_blank">📅 01:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444137">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vv5E4JXGnyvIqie01dGQN3qpQxdvMQNWbMaxUumNMvcdaRhOKgURRfI0l4TOInpr9g9S6vVlHbShEdmRc6QSANfMWzUrCLRxYR7OB4Djh7GG2YgqKJXT357TY-4ssjHhW4weXy18-dhZoTgTCziERdOEPLYKu1aPDbK6Kns6_YW1BaMKlZIkJ4QOpGd45fR50NZxbdrFutm3WwE6QhL6iQY8fBerkbfldky9cLVgutdomNBL1lbAB-HZ6z3E4-GpwUid6rg1XRq0aT35UtTO2v8SC1KDkTLjlPeX4-rqKvrqUCoFI-cdYzNCY5EC1S3Vd2bx2tdTRRwtPmsTSkmvFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب‌الله: با هرگونه نقض آتش‌بس اسرائیل مقابله‌به‌مثل می‌کنیم
🔹
محمود قماطی، نائب‌رئیس شورای سیاسی حزب‌الله: مقاومت در برابر هرگونه نقض آتش‌بس از سوی رژیم صهیونیستی، متقابلاً پاسخ خواهد داد و به شرایط پیش از جنگ جاری بازنخواهد گشت.
🔹
چشم مقاومت باز است و انگشت آن روی ماشه قرار دارد تا در برابر هرگونه نقض از سوی رژیم صهیونیستی مقابله کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/farsna/444137" target="_blank">📅 01:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444136">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb884a97d5.mp4?token=pmpdlspKxq6CnNIrv9wD-LhfzF6UY8fGbhaV0Dtfx2JWFbWYAZ_P_wO04NeqEGxrro5mPNwnh1SBfU5jfEqNwMWwfW3Iv4BpNp8XTizznbX4sZIxP5XoMVkuppFwc9onUvfo3tuP5Ym-1ayef4VJO6u04Yry5QCzK4EdsQs4MLFxVLNHOqGMvV-U-AhTBEy7tW_6nBTMexKg1-UcdLGvaB9a-yMuMTJldAynJXIHYNFASyvq0Ypsnkgp5R5024mZH5Z5fI1gFw_EusA9AC61QwKhVdbdhz0g-XD782KskFahtapq81AOOfZiwhDbAAVS7iGn-XTZQFm_jTNzun82qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb884a97d5.mp4?token=pmpdlspKxq6CnNIrv9wD-LhfzF6UY8fGbhaV0Dtfx2JWFbWYAZ_P_wO04NeqEGxrro5mPNwnh1SBfU5jfEqNwMWwfW3Iv4BpNp8XTizznbX4sZIxP5XoMVkuppFwc9onUvfo3tuP5Ym-1ayef4VJO6u04Yry5QCzK4EdsQs4MLFxVLNHOqGMvV-U-AhTBEy7tW_6nBTMexKg1-UcdLGvaB9a-yMuMTJldAynJXIHYNFASyvq0Ypsnkgp5R5024mZH5Z5fI1gFw_EusA9AC61QwKhVdbdhz0g-XD782KskFahtapq81AOOfZiwhDbAAVS7iGn-XTZQFm_jTNzun82qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: بیش از ۸۰ هزار پرونده مربوط به اغتشاشات ۱۴۰۱ مختومه شد.
@Farsna</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/farsna/444136" target="_blank">📅 01:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444135">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1834a9bbae.mp4?token=tRIQqV66y0hUmQnW6hrvO7cBRxJMHGdLKE6W6GGX9loSmj0kj4kJMM2LYJfYwLpWvQILapHIeKbzOrzJuJO7L6Xsrh5RyTrB7AZCGjgQgX6e2mjsQdae6mp40nafXjPEvUsRn_fx5_jvJLMQR0gNkjdawEuS2DQFTi5DlEdeXREuEZEvW8bpqybKABl9DDYH90aKGoHWozN4a-zdT4Z_EW8CJ1WegLVZRkpzP5bUuL4-51jJ-QcOTimzIW7jdbi-zPm3D0lL8O_Ncyk09ppKHKu9A3a_Q2eMjBGy0PL5_lVF2Jd9kZ_nllt4920lSQ7mlS5K4H8h7iF2RNjwiMSuDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1834a9bbae.mp4?token=tRIQqV66y0hUmQnW6hrvO7cBRxJMHGdLKE6W6GGX9loSmj0kj4kJMM2LYJfYwLpWvQILapHIeKbzOrzJuJO7L6Xsrh5RyTrB7AZCGjgQgX6e2mjsQdae6mp40nafXjPEvUsRn_fx5_jvJLMQR0gNkjdawEuS2DQFTi5DlEdeXREuEZEvW8bpqybKABl9DDYH90aKGoHWozN4a-zdT4Z_EW8CJ1WegLVZRkpzP5bUuL4-51jJ-QcOTimzIW7jdbi-zPm3D0lL8O_Ncyk09ppKHKu9A3a_Q2eMjBGy0PL5_lVF2Jd9kZ_nllt4920lSQ7mlS5K4H8h7iF2RNjwiMSuDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
سوپرگل دیدنی
⚽️
امباپه دقیقه ۱۴
فرانسه ۱ - ۰ عراق
@Sportfars</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/farsna/444135" target="_blank">📅 00:57 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444134">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/171b81be2e.mp4?token=B4Wjrjq5huRsQbeugPejCD5rC5C8JTLVNek-0DGPkhwixq3kiupasex3jUt4teeKnDRV6iTV0wc7lXXUXViHvf2boeiaMRMXbskJHshrtnLCy-hENtCw8fFMBzVCWTnnGfivgr8lcnX2GaMfCqgK-CxTlZzldawAgxDVpQ-a-MhNF8gtRJcbriwTsgccOk6JTBDVbrb3AlBA-F-7UymY_R_aF_sxSfQ5vNnDt5LzVOLLghgLkCGkfSZm8_QsmcZ2DhZJ-BACzrW-j3EoSJekv9rBp0_e2Tw5gyvDC1sFP6VmBFaPsFgoiJiKk56feDZuGITahqxck9HXJsT2pss7Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/171b81be2e.mp4?token=B4Wjrjq5huRsQbeugPejCD5rC5C8JTLVNek-0DGPkhwixq3kiupasex3jUt4teeKnDRV6iTV0wc7lXXUXViHvf2boeiaMRMXbskJHshrtnLCy-hENtCw8fFMBzVCWTnnGfivgr8lcnX2GaMfCqgK-CxTlZzldawAgxDVpQ-a-MhNF8gtRJcbriwTsgccOk6JTBDVbrb3AlBA-F-7UymY_R_aF_sxSfQ5vNnDt5LzVOLLghgLkCGkfSZm8_QsmcZ2DhZJ-BACzrW-j3EoSJekv9rBp0_e2Tw5gyvDC1sFP6VmBFaPsFgoiJiKk56feDZuGITahqxck9HXJsT2pss7Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: ۵۸ هزار میلیارد تومان تنها در یک فقره مبارزه با فساد به بیت‌المال بازگشت داده شد.  @Farsna</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/farsna/444134" target="_blank">📅 00:55 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444132">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09f208a55a.mp4?token=cE0BHblVAIikEB4fM_EeG6NF3pKCDY9_k0W3DRkphYZfiQeRTS_B-irjzJKmXchhgdu-VGhCBOXKRW7n1iki0y5Eg3REyfGqQJN8-dOZIStHrUM9jwNGonCKrXg4wemMZYVOB22CTOLevmLlcLBsP6QuEhXAAtQ1f3SCvAxhZ08d7FuAKMuGKy_-vxa31uJiifUHftq6fMBXELQhprtamTnePAcMA42NkOyeFc-IWeVJym220T9uc1yZcULGzTWdXuGb1XH5GSMUfMDDVaeEf7bUiSU11llhT6KQaPFJ7ZtdDeu_MKmyNAk72hEhk8u5-ZykuPEpprqO717JkJdzFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09f208a55a.mp4?token=cE0BHblVAIikEB4fM_EeG6NF3pKCDY9_k0W3DRkphYZfiQeRTS_B-irjzJKmXchhgdu-VGhCBOXKRW7n1iki0y5Eg3REyfGqQJN8-dOZIStHrUM9jwNGonCKrXg4wemMZYVOB22CTOLevmLlcLBsP6QuEhXAAtQ1f3SCvAxhZ08d7FuAKMuGKy_-vxa31uJiifUHftq6fMBXELQhprtamTnePAcMA42NkOyeFc-IWeVJym220T9uc1yZcULGzTWdXuGb1XH5GSMUfMDDVaeEf7bUiSU11llhT6KQaPFJ7ZtdDeu_MKmyNAk72hEhk8u5-ZykuPEpprqO717JkJdzFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: قوه‌قضاییه زیر بمباران حتی یک روز هم کار مردم را زمین نگذاشت.  @Farsna</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/farsna/444132" target="_blank">📅 00:53 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444131">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/946b7c5e0a.mp4?token=M5KPDgQrM_RJLlHwX1uk2NifrKNj__mVILA6U1TgxLsSPkhVtiEs4YA-I8AjvpQFTHPnbQ2jqkaoBNJ57ZU2P_RHuO7Y0npIwsyGqJzLp9q4d-VXVSr8H7iKtmlUjw27rxcN9kPfx3I1AvzyEuwY48n0h0q3f6fcheBzAtmH1q4kIVHnBDZAPUAVknspCMkQs6y3XqgO0RN-h3xtC4ohlMXMtVwQCZV1N0thsyOE0D3CVF781c2XmbXCswc2UtuKu-HZq-r81KKN3rBQZAJuLmb4wUOeaxauDX1V67fx9oHqOQy8n5Z24KIPO9L4ODSoAlhhn6mYqNx4Zqx5BdX7Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/946b7c5e0a.mp4?token=M5KPDgQrM_RJLlHwX1uk2NifrKNj__mVILA6U1TgxLsSPkhVtiEs4YA-I8AjvpQFTHPnbQ2jqkaoBNJ57ZU2P_RHuO7Y0npIwsyGqJzLp9q4d-VXVSr8H7iKtmlUjw27rxcN9kPfx3I1AvzyEuwY48n0h0q3f6fcheBzAtmH1q4kIVHnBDZAPUAVknspCMkQs6y3XqgO0RN-h3xtC4ohlMXMtVwQCZV1N0thsyOE0D3CVF781c2XmbXCswc2UtuKu-HZq-r81KKN3rBQZAJuLmb4wUOeaxauDX1V67fx9oHqOQy8n5Z24KIPO9L4ODSoAlhhn6mYqNx4Zqx5BdX7Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: قوه‌قضاییه زیر بمباران حتی یک روز هم کار مردم را زمین نگذاشت.
@Farsna</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/farsna/444131" target="_blank">📅 00:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444130">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EylUmwucBwZlpjft4G2w-Sce-QHxZXQze6i655tfp95K1eyFGnqUMgrY5DUiPz0krw_XKfXYzyggSnVWdaNItkKEbor4c7PIDB2qDAhbVeflepg3HHgBZ9er2Q388HDkfx0-GGQoB4IH6jLe8iVPlB82TY71TUcHeforaBIMA3JK8dvphgzfw0Obk57kKqjDP-3LUYQlFhz3nVMU72G629ftVd81Ej0Kgrv7V8w0qTm1R6XGqDh2F7r_4oepk_y2pAufX04sW_58bUdzOLJHkl25CoGwVmy4avd6_e2NR41W4kP_Xp_KwqHoCtQqcaAcIsTrAQygUHhd4jrBOi2obQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنده است یا آزاد؟
🔹
روزی بِشر حافی که مردی لاابالی و غرق در خوش‌گذرانی بود در خانه‌اش مجلسی پر از عیش و نوش و صدای ساز و آواز برپا کرده بود. در همین حین، امام موسی کاظم(ع) از مقابل خانهٔ او عبور می‌کردند.
🔹
دَرِ خانه باز شد و کنیزی برای ریختن خاکروبه به بیرون آمد. امام از کنیز پرسیدند: «صاحب این خانه بنده است یا آزاد؟»
🔹
کنیز با تعجب پاسخ داد: «معلوم است که آزاد است؛ او مردی شریف و ثروتمند است.»
🔹
امام فرمودند: «راست گفتی؛ اگر بنده [و فرمان‌بردار خدا] بود، از صاحب‌اختیار خود شرم می‌کرد و این بساط گناه را پهن نمی‌کرد.»
🔹
کنیز با سطل خالی به خانه برگشت. بشر که منتظر او بود، پرسید: «چرا این‌قدر طول کشید؟» کنیز ماجرای گفت‌وگوی خود با مرد ناشناس و جمله‌ای که او گفته بود را تعریف کرد.
🔹
سخنان امام مانند جرقه بر روح بشر نشست. او سراسیمه، پابرهنه و بدون کفش به دنبال امام دوید تا به ایشان رسید. بشر در مقابل امام توبه کرد، بساط گناه را برچید و از آن پس به یکی از زاهدان و مردان پاک روزگار تبدیل شد.
🔸
و چون آن روز پابرهنه دویده بود، تا پایان عمر به «بِشر حافی» یعنی بشرِ پابرهنه معروف شد.
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/farsna/444130" target="_blank">📅 00:36 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444129">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16c61cd58c.mp4?token=v8KztQSgbSCk6WQX0PgYgRwfIimp_A1_G5CKR7A3Z3_LZx7GY4b7y3svXliWl8zODhDmJroZ6-ZmDZDZyDGbEunO4RkWE5EqTbDDD-IkxnIRZF1MBeWkPeaR5W1O2N3C64vjtgNv0a2l7gJv0hDYvKjaznvyFdJ-eyOBDJcTe3z4Xz-w5I8COU7P30KZzfweDmKm3GCDs1GCjmHsSxUoyUt-z1onDpmcce2XDsw9TvchUkHtUq1oV2HabKph-xX8sn8_YV6fkKamaJ6qL47mPMeotbpJDYIez68bZ67Eoof2krXm5Vl87HE1NEeHGmqHlwxTCTwJT3U9mkGNGhHEOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16c61cd58c.mp4?token=v8KztQSgbSCk6WQX0PgYgRwfIimp_A1_G5CKR7A3Z3_LZx7GY4b7y3svXliWl8zODhDmJroZ6-ZmDZDZyDGbEunO4RkWE5EqTbDDD-IkxnIRZF1MBeWkPeaR5W1O2N3C64vjtgNv0a2l7gJv0hDYvKjaznvyFdJ-eyOBDJcTe3z4Xz-w5I8COU7P30KZzfweDmKm3GCDs1GCjmHsSxUoyUt-z1onDpmcce2XDsw9TvchUkHtUq1oV2HabKph-xX8sn8_YV6fkKamaJ6qL47mPMeotbpJDYIez68bZ67Eoof2krXm5Vl87HE1NEeHGmqHlwxTCTwJT3U9mkGNGhHEOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظاتی از شعرخوانی سیدمجید بنی‌فاطمه در دومین شب مراسم عزاداری حضرت اباعبدالله الحسین(ع) در جوار حسینیهٔ امام خمینی(ره)  @Farsna</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/farsna/444129" target="_blank">📅 00:31 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444128">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2866ec25ae.mp4?token=lhj3aZxNQymsabBpj2zzSySxp0Q47p9QC9NzMYEZo-Ch6EEzHVKumip6DU2esupWj_xuSQ3bq8OOHQa80uGqWQrchzGj5ZNdtfaHZ4zGp1zjTSUVXrtqPKDzsr6bLA8qOJg6akHoA3Y6LhTO2Hqcd6qvl8WuRsvKzVF378y8mb2dGyS5QZLKnzXTr9rXkGhIYr99505lNLz8zH-DTQPFnV_Tf2NMOpCg8p1Q4gjKCxQxqSq-QUEoQXe-bwrCYYHeg5aMr2JVwMeRnLYiLdUt4VMjwJ5RVW8T-AttP2nc8oWGbWfgq9hvPn0knlONVP2BYBNLgBfAuRD0kvRLi8V34w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2866ec25ae.mp4?token=lhj3aZxNQymsabBpj2zzSySxp0Q47p9QC9NzMYEZo-Ch6EEzHVKumip6DU2esupWj_xuSQ3bq8OOHQa80uGqWQrchzGj5ZNdtfaHZ4zGp1zjTSUVXrtqPKDzsr6bLA8qOJg6akHoA3Y6LhTO2Hqcd6qvl8WuRsvKzVF378y8mb2dGyS5QZLKnzXTr9rXkGhIYr99505lNLz8zH-DTQPFnV_Tf2NMOpCg8p1Q4gjKCxQxqSq-QUEoQXe-bwrCYYHeg5aMr2JVwMeRnLYiLdUt4VMjwJ5RVW8T-AttP2nc8oWGbWfgq9hvPn0knlONVP2BYBNLgBfAuRD0kvRLi8V34w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بیرانوند با واکنشی تماشایی بلژیک را در حسرت گل گذاشت  @Farsna</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/farsna/444128" target="_blank">📅 00:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444127">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ccbc7c95b.mp4?token=WLlXeNqWVtzV5kWCSlan3CDdSB6cFNm1YmnphbPwVGl-UWtSRz7iVEeinwnjlPvrKSoXVRoWpDS2VvVw_VSvhqk46fHqKeZYENZfXgpRPtDOQG90Tv1DdXSWeJnITGrRMESzY4IcbxmNYiKpwOkRU7HR3D7qgWK2lYM2wV8hPTB9UM7XHducLPqZyfQyMhG4JrWund9NOtfEwY3FZFM63X4JTyJb5uHn9D4yEWqU2IeMpK40Jal1fBHlC5fSWiqH1pppBxLluoqXyFDXgStkBY0w7QCURXHixH84xT607AnFdduam0VgqauFCWvmTixEKY3sUiVRi3Pn1LmYoPAN_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ccbc7c95b.mp4?token=WLlXeNqWVtzV5kWCSlan3CDdSB6cFNm1YmnphbPwVGl-UWtSRz7iVEeinwnjlPvrKSoXVRoWpDS2VvVw_VSvhqk46fHqKeZYENZfXgpRPtDOQG90Tv1DdXSWeJnITGrRMESzY4IcbxmNYiKpwOkRU7HR3D7qgWK2lYM2wV8hPTB9UM7XHducLPqZyfQyMhG4JrWund9NOtfEwY3FZFM63X4JTyJb5uHn9D4yEWqU2IeMpK40Jal1fBHlC5fSWiqH1pppBxLluoqXyFDXgStkBY0w7QCURXHixH84xT607AnFdduam0VgqauFCWvmTixEKY3sUiVRi3Pn1LmYoPAN_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: در انتهای دور اول مذاکرات وقتی متوجه شدم ترامپ هیئت مذاکره‌کننده و رئیس‌جمهور ما را تهدید کرده و از حمله به ایران گفته، به ونس گفتم بند اول مذاکرات این است که تهدید و زور نباشد و همان لحظه مذاکره را تمام کردیم و از جلسه بیرون آمدیم و دیگر برنگشتیم…</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/farsna/444127" target="_blank">📅 00:14 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444126">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0bd5d167b.mp4?token=g0tnHyb-r8Fm2aU-gyswXPW6ApMk87D7sNC1bOiIm8Aur3QKwU9jk4e-GSiy4EdDWIvF4F6zNSt6bcrsfVSyKgDRTapyXVmLtFkWFPlh-28cowmrqZNaf42xSnR3DoOwpJu5-5d7AQdb3np04P90_alB2MyF7XYi1YXSJWDcgdJAwXVvwUL69kXm8zJt4aew0tmYMMdiqtcEqOZSzT29QTMAwaIJ2d01UXJ32PnYcBssLd0ggnO3ZntyndZfOUSpNBEHTgV5DHB0HNvUFy_IoPJrrHbcuMDk-_osK1GVxZiB4QBzyJMLSEmpZ4ubb8Uq0v9pewQxR1CF_2gcOHan6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0bd5d167b.mp4?token=g0tnHyb-r8Fm2aU-gyswXPW6ApMk87D7sNC1bOiIm8Aur3QKwU9jk4e-GSiy4EdDWIvF4F6zNSt6bcrsfVSyKgDRTapyXVmLtFkWFPlh-28cowmrqZNaf42xSnR3DoOwpJu5-5d7AQdb3np04P90_alB2MyF7XYi1YXSJWDcgdJAwXVvwUL69kXm8zJt4aew0tmYMMdiqtcEqOZSzT29QTMAwaIJ2d01UXJ32PnYcBssLd0ggnO3ZntyndZfOUSpNBEHTgV5DHB0HNvUFy_IoPJrrHbcuMDk-_osK1GVxZiB4QBzyJMLSEmpZ4ubb8Uq0v9pewQxR1CF_2gcOHan6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: ما هرگز نمی‌خواهیم با آمریکایی‌ها در یک قاب باشیم
🔹
میانجی‌ها خیلی اصرار داشتند و ماهم گفتیم در آن قاب حاضر نمی‌شویم و ما فقط برای مذاکره می‌آییم. @Farsna</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/farsna/444126" target="_blank">📅 00:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444125">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/524582de93.mp4?token=dv5fkQbi_r5WfmzGOG8tsid3IJCZbC5IekIzsMXZu3BFMECR8rokxTSLpTWHiJaW81S-CGXMmUXQc_rKAUCeoGysyqq2zslrnZZS0z0b4kknITU-Dl_K231biIJgRtbDCGQ1FFBNL9iXSEFv5G8MB9I--oDBSa5JAgPaT3BudMcBptCvx3BucoXVcUARij1QxfGCmHj7dWzRS9zIjNfPQ-E0lZ2h3fZvPue_vAyZJ60Dri8K9Q1i0UkwgsGXQSEmMaoXSPzMBWrmb73xMxLTpeT0wSvSdttvmWIIlXvvX2HabaZjWr0wxqTzit_Q6tQhIBKEDXPgx8_Sk6yZ20hIqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/524582de93.mp4?token=dv5fkQbi_r5WfmzGOG8tsid3IJCZbC5IekIzsMXZu3BFMECR8rokxTSLpTWHiJaW81S-CGXMmUXQc_rKAUCeoGysyqq2zslrnZZS0z0b4kknITU-Dl_K231biIJgRtbDCGQ1FFBNL9iXSEFv5G8MB9I--oDBSa5JAgPaT3BudMcBptCvx3BucoXVcUARij1QxfGCmHj7dWzRS9zIjNfPQ-E0lZ2h3fZvPue_vAyZJ60Dri8K9Q1i0UkwgsGXQSEmMaoXSPzMBWrmb73xMxLTpeT0wSvSdttvmWIIlXvvX2HabaZjWr0wxqTzit_Q6tQhIBKEDXPgx8_Sk6yZ20hIqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: با رعایت قوانین بین‌المللی تنگهٔ هرمز با ترتیبات ایرانی اداره خواهد شد
🔹
هماهنگی کردیم که خط تلفنی وجود داشته باشد که در دورهٔ تفاهم، کشتی‌ها با امنیت بیشتر پیش بروند. آن‌هایی که احساس نگرانی دارند با این خط تماس بگیرند ما به‌عنوان مدیر تنگه مشکل…</div>
<div class="tg-footer">👁️ 7.45K · <a href="https://t.me/farsna/444125" target="_blank">📅 00:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444123">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d56dae973.mp4?token=bG-NDrqMit8kS5AAXtD54iX1yOV4GggJmVEAxOmTlq4i8Sxsf9DlqQE2sDlrP-CfqEPt8Ss0Q4G2uCfvv1tshg6u6_3C9xj5Ovbn2bM8opSiRvj3LzFEy_DBu50KKC4FQ-gXLJv1iQfwIR1z5edeUJD7fIgEFbh6-eIUIR_K4c3p-NUpj3CDt2iCVTfNxOdaoJRMbCPy0o5gkAye8FA7LDFIxs5mnoS5C0XdvjAMrYfjMk66oyr0npWwRptUfQSSWOK-nJiI7yGAWRFQ9C5biC_cspk23V3xC34LCZiH3Rb7d2gN-CZxVmFIohHGhsJh2rB0vBb3opN74537f_TRHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d56dae973.mp4?token=bG-NDrqMit8kS5AAXtD54iX1yOV4GggJmVEAxOmTlq4i8Sxsf9DlqQE2sDlrP-CfqEPt8Ss0Q4G2uCfvv1tshg6u6_3C9xj5Ovbn2bM8opSiRvj3LzFEy_DBu50KKC4FQ-gXLJv1iQfwIR1z5edeUJD7fIgEFbh6-eIUIR_K4c3p-NUpj3CDt2iCVTfNxOdaoJRMbCPy0o5gkAye8FA7LDFIxs5mnoS5C0XdvjAMrYfjMk66oyr0npWwRptUfQSSWOK-nJiI7yGAWRFQ9C5biC_cspk23V3xC34LCZiH3Rb7d2gN-CZxVmFIohHGhsJh2rB0vBb3opN74537f_TRHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: با سفر به عمان مدیریت ایرانی تنگهٔ هرمز را مستحکم می‌کنیم.  @Farsna</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/farsna/444123" target="_blank">📅 00:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444122">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12bdb04e6b.mp4?token=JA29Lu4gea2xwyt0rPKswfd6ihl4WP8xpBhjjSvUGLRcmCzpUfnn5PcJ3S12xvto9q6ysKgc6D9IaQ0Ot0v1CMGPULToQq16ekeSwfL0jfz6cA8YolppNcUTjdIUmTB8xAdTCQhcTrsYgObB7BnPlfS40LU9xYxvq6FCbiGkySLBYMpxrUHRw3RrFfjB-A6BamU5H9AM8Gye99drSehZnGHr7SJF5TVAThVFd8ub1vxFBZkxtJnArjTBSvoBfsWG8nZBy3uWPJF00BmeJpQfrVFCIkKQuXcDVioeS8vLWGSD9XRDQyjCqz6R-hM0PmNaDNQ_DfGTXF2kwMCCrYrfXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12bdb04e6b.mp4?token=JA29Lu4gea2xwyt0rPKswfd6ihl4WP8xpBhjjSvUGLRcmCzpUfnn5PcJ3S12xvto9q6ysKgc6D9IaQ0Ot0v1CMGPULToQq16ekeSwfL0jfz6cA8YolppNcUTjdIUmTB8xAdTCQhcTrsYgObB7BnPlfS40LU9xYxvq6FCbiGkySLBYMpxrUHRw3RrFfjB-A6BamU5H9AM8Gye99drSehZnGHr7SJF5TVAThVFd8ub1vxFBZkxtJnArjTBSvoBfsWG8nZBy3uWPJF00BmeJpQfrVFCIkKQuXcDVioeS8vLWGSD9XRDQyjCqz6R-hM0PmNaDNQ_DfGTXF2kwMCCrYrfXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: ما اگر به سوئیس نمی‌رفتیم هر لحظه خون بیشتری از شیعیان ریخته می‌شد.  @Farsna</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/farsna/444122" target="_blank">📅 23:55 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444121">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/477b8b8251.mp4?token=jQ3mVyLztDRZyhPtydBRge2KW82oh99uROJfk3bJ-5xt_PKRuWRfzQPtRxU-0odsqXr7DAywbzyUajXRNqHD_g1pZOyUR7ys2yfDI1vC-BtqAnzk4vJcfmMQ8oCeEWPOMowh4BMZVt73WKpssFj30JN0r_odqTIWxFEizzYrv3FrIxrigCD-aEDvY_wCXsyjSmGAvKTfb0o_hx6_bOgXWDIMUuDovo39ZwNm2UwXInE72_EwLb4BjeS8BHrFRXIWAfeGHBegm76wTAneOrGIsRP224FsIc6wz3-11zJB1Bdj4VA4ulIjGZP-FPUNEHc1uN0dwTR2k-TO6WL-rrw1sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/477b8b8251.mp4?token=jQ3mVyLztDRZyhPtydBRge2KW82oh99uROJfk3bJ-5xt_PKRuWRfzQPtRxU-0odsqXr7DAywbzyUajXRNqHD_g1pZOyUR7ys2yfDI1vC-BtqAnzk4vJcfmMQ8oCeEWPOMowh4BMZVt73WKpssFj30JN0r_odqTIWxFEizzYrv3FrIxrigCD-aEDvY_wCXsyjSmGAvKTfb0o_hx6_bOgXWDIMUuDovo39ZwNm2UwXInE72_EwLb4BjeS8BHrFRXIWAfeGHBegm76wTAneOrGIsRP224FsIc6wz3-11zJB1Bdj4VA4ulIjGZP-FPUNEHc1uN0dwTR2k-TO6WL-rrw1sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: در مذاکرات سازوکاری درست کردیم که ایران و آمریکا هردو باید تمامیت ارضی و حاکمیت ملی لبنان را ضمانت کنند
🔹
توافق کردیم مرکزی باشد در حد هماهنگی‌ها که [از درگیری] پیشگیری شود. @Farsna</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/farsna/444121" target="_blank">📅 23:55 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444120">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83a821d59d.mp4?token=F1_bYL0hDIy555mEg8Fm2il87P_1GJpmfx-LrwUnfEegU3GGKZIs0enEYH7Fn69ZG4DAyAJmcjMrvyQmX-Eiso59I3sO-69nE-BxFWM7e1Ma1pD3zyTRFd1Q71BUfL-jverpBoNn5OOvPIYPMg45bNGLhNYmNmIAKAfhq0Alp82ThOVADLv1IFWZgeYtqi0xz3ZMjv151ufR3FUUEQGNvvRWawIhOhDca4-AdfQ4ShMtkGZMZHTli6jSzP_moGgQVwWHT8p_9isYnozEI9uEgEGVaVKD0UAOLgjuXGiFSk5KC2URUoiIZ9G86k4tH_Grn_el18hTFb97aqEtPfYoXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83a821d59d.mp4?token=F1_bYL0hDIy555mEg8Fm2il87P_1GJpmfx-LrwUnfEegU3GGKZIs0enEYH7Fn69ZG4DAyAJmcjMrvyQmX-Eiso59I3sO-69nE-BxFWM7e1Ma1pD3zyTRFd1Q71BUfL-jverpBoNn5OOvPIYPMg45bNGLhNYmNmIAKAfhq0Alp82ThOVADLv1IFWZgeYtqi0xz3ZMjv151ufR3FUUEQGNvvRWawIhOhDca4-AdfQ4ShMtkGZMZHTli6jSzP_moGgQVwWHT8p_9isYnozEI9uEgEGVaVKD0UAOLgjuXGiFSk5KC2URUoiIZ9G86k4tH_Grn_el18hTFb97aqEtPfYoXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: ما به آمریکایی‌ها بی‌اعتماد بودیم و بی‌اعتماد هستیم
🔹
اگر می‌خواستیم از طریق نظامی محاصره را برداریم متحمل خسارات سنگین مالی می‌شدیم اما با مذاکره محاصره را یک‌شبه برداشتیم.
🔹
تا توافق نهایی نشود تحریم‌ها هنوز هستند؛ پس ما باید معافیت تحریمی فروش…</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/farsna/444120" target="_blank">📅 23:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444119">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ed9726683.mp4?token=rr_DvuWch2AnTCu0xzeAxYcwFqW8NyWJuw8n6Q1yBJxGjiTiQHJ_uhMKwBYVvsZRtZRv0IuNl8DHmi6SxxRRWR9dYM2MXh6e0aulfOGiZBS2kZpuV-uQo8_RCFEl5nmRc_UThYMFpcdo4ZdeOKZx3wV4aL7jITmoQAX8bMNVXs61Vw5CNn6AwX380h7ofxcr2rJDIAEBWbsCPrXp9n67dL1iQKRz1WtB2mk7Gecs-1M50-Ii8I1qfFO80RqAOOWKFyV6TDTwOpvJCqdpOlbJ4t379mvRdxw-DX0BsqCxU2WCAd7Wo_rXYuvnjZbvt0ZXlrBHgQFYX7r1-4BZPXlqQJIJgiI_zjWSjkA3SKIjfFAtUIN7t3My3bbr0lyAD0UiLjIG6kgw7WjemMH6hZCD73YAE4FtuUATtsSwh7ZUbPsaPvA_yXIuWSdvQxRNEELQK2d6H0TIbyPIhf6HV5IB9RheHdW2bFyH2o-9CUSBtHXnC-R0wNGBSvPA4bLRyqI9yyXUH9TjVPVZNxqEqKuupKNVTuosb9NaZ_d8REVS-knFfCCVpv1EaRwgGV06WpYOiekggcOx7wJQ58tG348ljuA2mKdQglrtcmTB6yau5GcKpTrvpfnKszXsUKAA-g9nF6oy1eduPf-IawXRWymQP8YmY8UBtdtBGgtHJUwxebM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ed9726683.mp4?token=rr_DvuWch2AnTCu0xzeAxYcwFqW8NyWJuw8n6Q1yBJxGjiTiQHJ_uhMKwBYVvsZRtZRv0IuNl8DHmi6SxxRRWR9dYM2MXh6e0aulfOGiZBS2kZpuV-uQo8_RCFEl5nmRc_UThYMFpcdo4ZdeOKZx3wV4aL7jITmoQAX8bMNVXs61Vw5CNn6AwX380h7ofxcr2rJDIAEBWbsCPrXp9n67dL1iQKRz1WtB2mk7Gecs-1M50-Ii8I1qfFO80RqAOOWKFyV6TDTwOpvJCqdpOlbJ4t379mvRdxw-DX0BsqCxU2WCAd7Wo_rXYuvnjZbvt0ZXlrBHgQFYX7r1-4BZPXlqQJIJgiI_zjWSjkA3SKIjfFAtUIN7t3My3bbr0lyAD0UiLjIG6kgw7WjemMH6hZCD73YAE4FtuUATtsSwh7ZUbPsaPvA_yXIuWSdvQxRNEELQK2d6H0TIbyPIhf6HV5IB9RheHdW2bFyH2o-9CUSBtHXnC-R0wNGBSvPA4bLRyqI9yyXUH9TjVPVZNxqEqKuupKNVTuosb9NaZ_d8REVS-knFfCCVpv1EaRwgGV06WpYOiekggcOx7wJQ58tG348ljuA2mKdQglrtcmTB6yau5GcKpTrvpfnKszXsUKAA-g9nF6oy1eduPf-IawXRWymQP8YmY8UBtdtBGgtHJUwxebM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: وقتی پیاده‌سازی آتش‌بس و پایان جنگ مشکل پیداکند ما می‌توانیم این را هم با موشک حل کنیم هم با مذاکره.  مذاکره و‌ میدان مکمل یکدیگرند. @Farsna</div>
<div class="tg-footer">👁️ 7.3K · <a href="https://t.me/farsna/444119" target="_blank">📅 23:46 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444118">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e88fe3f217.mp4?token=Oih1DsRyv4po73w1KpkKU7r2TM-HNPD4vyr6XM954nzCzbViru0x8k35e6ZQu9urvDACCK62YJb7TGkJASj7E0orFDdJM6wZr3mSxsh5-PdrEemjToDuHCp-DXbh7l6B8O3lI_PIpfhcWyJRnPBkHzryS1MPyGv7OsB3JZBzL8fqjMah8p6CnXnwV5xBajwBZeI9OdTLrDzDvIzVDCSR62pl_Nu-Avrtn7VvfTq3gNRddThC47EZj7iPyoIehvm1FDQKlRBxrdlLg6PNOmFEVpKRGHY-Ea6NNTjw024F0VH239wqCdlRmAZuRLHBV-9cX7_VjtL8RknY0lIxTaV52Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e88fe3f217.mp4?token=Oih1DsRyv4po73w1KpkKU7r2TM-HNPD4vyr6XM954nzCzbViru0x8k35e6ZQu9urvDACCK62YJb7TGkJASj7E0orFDdJM6wZr3mSxsh5-PdrEemjToDuHCp-DXbh7l6B8O3lI_PIpfhcWyJRnPBkHzryS1MPyGv7OsB3JZBzL8fqjMah8p6CnXnwV5xBajwBZeI9OdTLrDzDvIzVDCSR62pl_Nu-Avrtn7VvfTq3gNRddThC47EZj7iPyoIehvm1FDQKlRBxrdlLg6PNOmFEVpKRGHY-Ea6NNTjw024F0VH239wqCdlRmAZuRLHBV-9cX7_VjtL8RknY0lIxTaV52Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: در گفت‌وگوها موضوع [حفظ] تمامیت ارضی لبنان را تا به نتیجه‌رساندن رها نخواهیم کرد.  @Farsna</div>
<div class="tg-footer">👁️ 7.67K · <a href="https://t.me/farsna/444118" target="_blank">📅 23:35 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444117">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38e8285d04.mp4?token=JhSTdgQrlsL-rxPjeOX95DpN4BxY9AT9K7zZScspl9iNtbYJxsQhOvVilSASQufPW_7tbCH_NImKPqzaG10sFPIeErQXAV7Nfncj89V2xZDsK80DivMu4NLiaGpTb9IwnscuqVv1VIsIuEe_ZvGk5gbQdqVD083OwFG7fJUCMgDokDitff5IfIFSY2oYyjyeHMYuLd8gou9DxOewWWFaZynZpyfe-ArgwOKDFCxxAtzYTonBue4SUIh3Z9bw0HJPQlJ-MarWO3pkBQjR2up_r7IvXBVUkqythi0onVc3KqS6F9aYCK2L2i7JeupWNx87a6-lIN_P0sSoXbO86GeWzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38e8285d04.mp4?token=JhSTdgQrlsL-rxPjeOX95DpN4BxY9AT9K7zZScspl9iNtbYJxsQhOvVilSASQufPW_7tbCH_NImKPqzaG10sFPIeErQXAV7Nfncj89V2xZDsK80DivMu4NLiaGpTb9IwnscuqVv1VIsIuEe_ZvGk5gbQdqVD083OwFG7fJUCMgDokDitff5IfIFSY2oYyjyeHMYuLd8gou9DxOewWWFaZynZpyfe-ArgwOKDFCxxAtzYTonBue4SUIh3Z9bw0HJPQlJ-MarWO3pkBQjR2up_r7IvXBVUkqythi0onVc3KqS6F9aYCK2L2i7JeupWNx87a6-lIN_P0sSoXbO86GeWzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بیرانوند: مردم ما ۴ ماه سخت را سپری کردند و ما همه تلاش خود را کردیم تا دل آن‌ها را شاد کنیم و شرمنده آن‌ها نشویم.  @Farsna</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/farsna/444117" target="_blank">📅 23:25 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444116">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45811675c3.mp4?token=W14kZGRn85hroQRGiDoHKIooc3ADWg6LtGHvaHNqvB9ZPz6UG9L4zNuNWfSX2Bty_L7-Y-i-pZB1Jjt1WFVBDI_QmeDwAPWBBzoQdJUJ--5gHXaoFP3rMOde4TnM_-hI_yzc84wv44_f8j2aLIt4F7dcQO1fq19fJ7bgGx8pmBi7dVV2vP0eICepZcJR4-eIH7F69-eqTOx2XABqn18q_JYl7SuC8PQf-LYPx8TiRAJ0tfb1zES-FzjTOr0RqKpuUIpCY8fa7YFI_fXbBb2aW9xvCdywAGtG2q5AHH3_zehATdcSKrWCgPMvVQNMTekhS62lSn9SSBLEqJu8RjuJAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45811675c3.mp4?token=W14kZGRn85hroQRGiDoHKIooc3ADWg6LtGHvaHNqvB9ZPz6UG9L4zNuNWfSX2Bty_L7-Y-i-pZB1Jjt1WFVBDI_QmeDwAPWBBzoQdJUJ--5gHXaoFP3rMOde4TnM_-hI_yzc84wv44_f8j2aLIt4F7dcQO1fq19fJ7bgGx8pmBi7dVV2vP0eICepZcJR4-eIH7F69-eqTOx2XABqn18q_JYl7SuC8PQf-LYPx8TiRAJ0tfb1zES-FzjTOr0RqKpuUIpCY8fa7YFI_fXbBb2aW9xvCdywAGtG2q5AHH3_zehATdcSKrWCgPMvVQNMTekhS62lSn9SSBLEqJu8RjuJAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بیرانوند: مهدی طارمی قبل از بازی یک سخنرانی حماسی کرد و به بازیکنان گفت اگر سر خود را در مقابل بازیکنان بلژیک پایین بندازید، بلژیکی‌ها ما را له می‌کنند و آبروی ما را می‌برند و باید در تمام لحظات سر خود را بالا بگیرید.  @Farsna</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/farsna/444116" target="_blank">📅 23:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444115">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/001a8c75c3.mp4?token=WFrRx_GO_owJ0R8Yc2VTa1pScBuye3xk1lWR1XPRWAAHBzxJT3ok4zc7CRutU4uvwUuSuACuWu038123aAuZhhsW_uerrDgtBNvJn_NOITP-vX7gg_Qel5ZLGX7jUJeSFuJK1oOVheZ1xPK7rNlXq3w12OvBNm29ySLYVcBOdeMP3-KTqMqoxGdk6sLX9eWfES599PcSwZPLVcFNrKOfWccyuBJCgh-3RIscZ3hfduQUczUd89R6MTLaifZMq5HQZqyW1Ttv7Ckn0XmT88vfJDiymd-LDX9-Fp21V42KzColqtLbWZ-MggVuZORYBeFTIV0VFRR6VVsrZkPD23A3uakLnE8T6JD2uTTK87UQwSPiSEStrOOmKbymzOtMHq4fPvU9tdo3mGDCNfc6aLaGUgzH6lCv8StY6B_s_-IQzw-it9WDiLeD8KC5J_3dRfS65awqGswhogEMTVudtwJW7peFO7lTlCpW-VIPSKiXTu9duILW_GgTjG4hQ6XSZilq0eZBw4iN5Jvt8LwIhEW5U2TW3ZEl4W4puKgaOO24EAtZx7TrJwCY1xtZUj-bWxEBouiaiwfcGH4m-1g2H6iTIt171Y8WCOfvycRBdexT3ZJBlAzCaEVCfXK9wnhD7IbB3sLTvEyUR-JcZYyvonDv3dmmwEVM5ySAgcr1HuBroJ0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/001a8c75c3.mp4?token=WFrRx_GO_owJ0R8Yc2VTa1pScBuye3xk1lWR1XPRWAAHBzxJT3ok4zc7CRutU4uvwUuSuACuWu038123aAuZhhsW_uerrDgtBNvJn_NOITP-vX7gg_Qel5ZLGX7jUJeSFuJK1oOVheZ1xPK7rNlXq3w12OvBNm29ySLYVcBOdeMP3-KTqMqoxGdk6sLX9eWfES599PcSwZPLVcFNrKOfWccyuBJCgh-3RIscZ3hfduQUczUd89R6MTLaifZMq5HQZqyW1Ttv7Ckn0XmT88vfJDiymd-LDX9-Fp21V42KzColqtLbWZ-MggVuZORYBeFTIV0VFRR6VVsrZkPD23A3uakLnE8T6JD2uTTK87UQwSPiSEStrOOmKbymzOtMHq4fPvU9tdo3mGDCNfc6aLaGUgzH6lCv8StY6B_s_-IQzw-it9WDiLeD8KC5J_3dRfS65awqGswhogEMTVudtwJW7peFO7lTlCpW-VIPSKiXTu9duILW_GgTjG4hQ6XSZilq0eZBw4iN5Jvt8LwIhEW5U2TW3ZEl4W4puKgaOO24EAtZx7TrJwCY1xtZUj-bWxEBouiaiwfcGH4m-1g2H6iTIt171Y8WCOfvycRBdexT3ZJBlAzCaEVCfXK9wnhD7IbB3sLTvEyUR-JcZYyvonDv3dmmwEVM5ySAgcr1HuBroJ0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیوند ۱۱۴ شب دلتنگی با شور ۸ محرم در یاسوج
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/farsna/444115" target="_blank">📅 23:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444114">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39f08f7b5c.mp4?token=LktU5bXPV2qYzRj8UlT5y610Kj6IG8JZIaFQ5JvWZdEqxCFWjRNyFjQAMA2kdFla-UrBOHY9KBGxguO7mJbUPuJmZTjfH1Li4TU1nCJcbFUUcwx1bsdv4VehBa-iQSS4EU04NhKhxDV0RT6qpq-ZwoJuBqfZU7lt2MTIk6hNADcdHCO4P4FmSoTMtNU0Uhe2HrnQAiUb_g_u1HZeXGMLz5MLNDytIoD7g_S_Qp8urhiNhPd-K7uXm6GVDmBjsaXHOOL4yFXpIBZOg-Ix99agffymrL2zSCnpHIqhRF3lh-q3mqqgb0glhsGghKYvABLeOs4hsSiNtwrqBEBLXeHQqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39f08f7b5c.mp4?token=LktU5bXPV2qYzRj8UlT5y610Kj6IG8JZIaFQ5JvWZdEqxCFWjRNyFjQAMA2kdFla-UrBOHY9KBGxguO7mJbUPuJmZTjfH1Li4TU1nCJcbFUUcwx1bsdv4VehBa-iQSS4EU04NhKhxDV0RT6qpq-ZwoJuBqfZU7lt2MTIk6hNADcdHCO4P4FmSoTMtNU0Uhe2HrnQAiUb_g_u1HZeXGMLz5MLNDytIoD7g_S_Qp8urhiNhPd-K7uXm6GVDmBjsaXHOOL4yFXpIBZOg-Ix99agffymrL2zSCnpHIqhRF3lh-q3mqqgb0glhsGghKYvABLeOs4hsSiNtwrqBEBLXeHQqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
علیرضا بیرانوند: بعد از برخورد با لوکاکو، تمام زمان مسابقه را با درد خیلی زیادی بازی کردم.  @Farsna</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/farsna/444114" target="_blank">📅 23:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444113">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef10148d95.mp4?token=iR2V5wxQoC01n6JH7nDO8QEdLdWMChCogmbucxtMSJanT7BBmG_m0zDMlQfgGmpOqghI_12eh8K0Cu4ns-t1i60fUq56DLVBvdstXNvad03sZktJhDOiS6mogYfeELC2gubYqnGT-XZ2L7D6sK6CPWGcI-1hm9Ff3PULY0wFcJSy2uc8XaDvJZlIoEj1Do8WL-yvg0nkLBON7Izwy4TFYkSCwcNa4txCszEtJzNnpV1X-OEfVk48PItAG6ERrHDNMsmPkNI44a0C3QINFq9VOhq0mfbPxNH0F3GvmPSReR4j9X96q7VtbDPi3vw96qGo_JqtareiAxSNh2Ev7cysyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef10148d95.mp4?token=iR2V5wxQoC01n6JH7nDO8QEdLdWMChCogmbucxtMSJanT7BBmG_m0zDMlQfgGmpOqghI_12eh8K0Cu4ns-t1i60fUq56DLVBvdstXNvad03sZktJhDOiS6mogYfeELC2gubYqnGT-XZ2L7D6sK6CPWGcI-1hm9Ff3PULY0wFcJSy2uc8XaDvJZlIoEj1Do8WL-yvg0nkLBON7Izwy4TFYkSCwcNa4txCszEtJzNnpV1X-OEfVk48PItAG6ERrHDNMsmPkNI44a0C3QINFq9VOhq0mfbPxNH0F3GvmPSReR4j9X96q7VtbDPi3vw96qGo_JqtareiAxSNh2Ev7cysyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لوکاکو به‌خاطر خطا روی بیرانوند کارت زرد گرفت   @Farsna</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/farsna/444113" target="_blank">📅 23:12 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444112">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5540a0a5eb.mp4?token=fiiRUFBFLSnXq45cjP-o2KTR-453P6G5VI-4b5r16OwFhV6tvc9-eJ2LcP15aq9ASJzxpAxWNv7STRJ3mypKBcVQ2yGQsN8Zwyn7R4hMbCyBttxrlO0m3-5EKhlJ1HKk9soS2G1pGiAyocjkoqrHmHehZZKHiz51gJOTlfxxfX0nOwhSdHUrKnw-N3eYCut_TPfpe1e6-78Fe9GIzOUkDuFgIoaEpvM6FpwKcpJ4GswaQ729is4IsfhkXXIDb-jxk0OSBWz72vt5iDLQPJzR54_QisQIZ9xQh1PxwGXlwHCiihxTF363F0dGoLKFZpZAXf_o7w5d43H941_yl38Vhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5540a0a5eb.mp4?token=fiiRUFBFLSnXq45cjP-o2KTR-453P6G5VI-4b5r16OwFhV6tvc9-eJ2LcP15aq9ASJzxpAxWNv7STRJ3mypKBcVQ2yGQsN8Zwyn7R4hMbCyBttxrlO0m3-5EKhlJ1HKk9soS2G1pGiAyocjkoqrHmHehZZKHiz51gJOTlfxxfX0nOwhSdHUrKnw-N3eYCut_TPfpe1e6-78Fe9GIzOUkDuFgIoaEpvM6FpwKcpJ4GswaQ729is4IsfhkXXIDb-jxk0OSBWz72vt5iDLQPJzR54_QisQIZ9xQh1PxwGXlwHCiihxTF363F0dGoLKFZpZAXf_o7w5d43H941_yl38Vhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
استقبال وزیر خارجهٔ عمان از قالیباف در بدو ورود به مسقط
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/farsna/444112" target="_blank">📅 23:09 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444111">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">‌
🔴
یک ‌منبع آگاه نزدیک به هیئت مذاکره‌کننده ایران در گفت‌وگو با خبرنگار فارس: ادعای معاون رئیس‌جمهور آمریکا دربارۀ بازگشت بازرسان آژانس به ایران کذب است
🔹
این منبع آگاه ادامه داد: در مذاکرات سوئیس هیچ صحبتی درباره حضور بازرسان در کشور نشده است. @Farsna</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/farsna/444111" target="_blank">📅 22:59 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444110">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qNNMHQA7e3Bf_mKja5jNZkPueHYEKjqKpaWZNGM9z5o4EAeNejGOvqidPrHSmq_Cb7i6I-TPR8BTxbzIFupIZfKWY_uibn8vpCRT3CkJ78mFeeV8tehJemBDIJ6gUAPOHy264lqCPZS4J0-PT3YXSSfBxbWoJSIvqXXE2jhxoqs2s_Pid5lQvvJ_3cIN9QT0pIIxmXoXugzGzF82orOA9g83IEM7pFgTCrlXOHeO749x1-EopP5U1SnArIYsvJ1eDZLUqyN5Rylr_Y7OYX9xBY3OEP4-OCW_C5q6shPB0ncga9M9hiakruBjILOaifYw4jGqWQPJB-VDf8xOcfnVMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از کلوزه عبور کرد
👑
لیونل مسی با گلزنی مقابل اتریش، با ۱۷ گل به بهترین گلزن تاریخ جام جهانی تبدیل شد.
@Sportfars</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/farsna/444110" target="_blank">📅 22:44 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444109">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bCH4q5bxjVmuDnNPZdXtWmHiO6n6NKoIHiM8s3JTyB4FZXIOj3D8NkJjpjqGegMLu3yZ-heN2kkRjDKXt9Fy2dqQc2gJt1vYiftN-BVcBI_A09MSaMS22g3FoCoKvZFcbOC0AGgxiFHwD3ET2NgpQoaqHhoCsGNczYlHyt8FFavi7M82tNa1K5m7BdtV24C8ShQJMCo98P_viTzixxXeATwb7UsL9XFWhMnk2pJ4h2UhL97ZYTBgxmOQ09KyW8Tkwf3XPE9Mrk13DKNrxFEb5QIrH-WdCAUwPjxNQnB8x56uVKNfxWpwTemrHjL29ULbHuSQdmDEZ84Mojx5G8uVng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرژانتین با ۲ گل مسی از سد اتریش گذشت
⚽️
آرژانتین ۲ - ۰ اتریش
@Farsna</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/farsna/444109" target="_blank">📅 22:34 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444108">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc13f57280.mp4?token=NjzduOByfdg2mOIoTef9je9_8ExpmtST_fySiW5VRlOfqTViYsLTW1aajS9eS5z1rIlUwC5HfbwJy6vzp4rUhALft2PqONnfcPJT39VoJOtMdZ-9eK_nwLp9xElT9k8HmX68ALrvOkrCc9zDFw7xP7NARPnepgDjyE3jSRRxA2XJt4UWayR8tLFUZc6t6xnVeXoFJftZIfxIUhD4gH1QBZIpBqnG8E0_I9lWem2dbSdkYTizBvRKTcEBnmT1Q9iYQIT1fIEU1C_tI_pIPDYWYrqxjGk2dpSyF9FxFnNr_q8KAjWDRrbUneeZJwJN0JWqZMMscPQmRz2cTHxEuf_UMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc13f57280.mp4?token=NjzduOByfdg2mOIoTef9je9_8ExpmtST_fySiW5VRlOfqTViYsLTW1aajS9eS5z1rIlUwC5HfbwJy6vzp4rUhALft2PqONnfcPJT39VoJOtMdZ-9eK_nwLp9xElT9k8HmX68ALrvOkrCc9zDFw7xP7NARPnepgDjyE3jSRRxA2XJt4UWayR8tLFUZc6t6xnVeXoFJftZIfxIUhD4gH1QBZIpBqnG8E0_I9lWem2dbSdkYTizBvRKTcEBnmT1Q9iYQIT1fIEU1C_tI_pIPDYWYrqxjGk2dpSyF9FxFnNr_q8KAjWDRrbUneeZJwJN0JWqZMMscPQmRz2cTHxEuf_UMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خبرنگار خطاب به معاون ترامپ: بی‌توجهی و سلام‌ندادن وزیرخارجهٔ ایران به شما، توهین‌آمیز بود؟ این کار عمدی بود؟
🔹
ونس: باور کنید در این چند ماه گذشته زمان زیادی رو صرف سروکله‌زدن با ایرانی‌ها کردم. بعضی وقت‌ها به‌عنوان مذاکره‌کننده واقعاً رفتار پیچیده و گیج‌کننده‌ای دارند.
@Farsna</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/farsna/444108" target="_blank">📅 22:28 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444107">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62a722f491.mp4?token=MkeeymbQNvM0VkhwC8Hca17IT717oKWnge26SZp8hov6YDor4rxs0SCQOB_-bREzimQJowXAphTCajj1AyvsE3TX-PHg4FhEL72vL1hx6G5J8vKARCjlZgD6MprWx710IuOuSCVBwA8-N3sTmi3wyu0Y8gst3cn-yIqlgPLTqAbzooOfeHV53z5SwBb-7x11Jfoo5pD91iPr2J7oJnk3Pwxlb63wi4eIEtya1pxwBF72kVqF_o7YQEV07rdUMeZu9nUkwtnJI6yDmHL5hk79AhvA-uQ35zAOhQgN79lgJQKxaX_h1qRfp17fusZQB2BTzt6hpydtMWjqd7dCYpjCCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62a722f491.mp4?token=MkeeymbQNvM0VkhwC8Hca17IT717oKWnge26SZp8hov6YDor4rxs0SCQOB_-bREzimQJowXAphTCajj1AyvsE3TX-PHg4FhEL72vL1hx6G5J8vKARCjlZgD6MprWx710IuOuSCVBwA8-N3sTmi3wyu0Y8gst3cn-yIqlgPLTqAbzooOfeHV53z5SwBb-7x11Jfoo5pD91iPr2J7oJnk3Pwxlb63wi4eIEtya1pxwBF72kVqF_o7YQEV07rdUMeZu9nUkwtnJI6yDmHL5hk79AhvA-uQ35zAOhQgN79lgJQKxaX_h1qRfp17fusZQB2BTzt6hpydtMWjqd7dCYpjCCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موشک‌های ایران  دست‌نخورده ماندند!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/farsna/444107" target="_blank">📅 22:20 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444106">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🎥
دهلران ایلام در محاصره پرچم‌ها و نوحه‌ها
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/farsna/444106" target="_blank">📅 22:14 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444105">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TRj3kHSZDezmzhs7ulsSEfrV7ZBip-LdBBd3Y2eS6ZV4fioacC0N2kCTmVMkZFglK75zI3vxNh99dzJGudi14PWOPPHEMFVw4Ii0e-3HpGoLk-3B5VDFUNKkk0PS1AWZc7BL4JiNxHC_D3airfxvKkZI72QA1txJ5-o2B1-nYEWTndA6WtZxIEqeE7qecu6jBJPf2AVpp9g2dVzCu23bIP-KBDxIdOjGfwuVfdd4O5JoB_KXChiU7OB64TC6Vj70OadnePwzQn7tNd4FLLPoiIx6x7uWB35tr4EHXpccnkk71rzPwh3nC5OKqkKy0G3Jh7LI7pBIkPyLad93HVkN4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استانداری محور مدیریت حریم تهران شد
🔹
شورای‌عالی شهرسازی محوریت مدیریت حریم تهران را برعهده استانداری تهران قرار داد.
🔹
براساس مصوبه این شورا باتوجه به افزایش ساخت‌وسازهای غیرقانونی مقرر شد شهرداری ظرف مدت ۳ ماه حریم مشخص و قانونی برای تهران را معین کند و پس از آن صدور مجوزها در حریم شهر را استانداری انجام دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/farsna/444105" target="_blank">📅 22:09 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444104">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">پیام‌هایی که شما برای فارس فرستادید
🔸
خواهش می‌کنم دستور رئیس‌جمهور رو مبنی بر حذف پیمانکاران در استان هرمزگان را پیگیری کنید. چرا این دستور در استان هرمزگان اجرا نمی‌شه؟
🔹
حالا که دارن بعضی جاها برق رو قطع می‌کنند کاش مثل پارسال اطلاع‌رسانی کنند که بتوانیم برنامه‌ریزی کنیم.
🔸
الان یک هفته است خونه فروختم و پولم تو بانک ملی گیر افتاده. چرا کسی فکری برای این مشکل این بانک نمی‌کنه؟
🔹
با وجود مصوب کردن مجلس دوره قبل مبنی بر اختصاص کد استخدامی به معلمان پیمانی مهرآفرین، چرا وزارت آموزش‌وپرورش این کدهای استخدامی را در احکام معلمان پیمانی مهرآفرین اعمال نمی‌کند و هیچ‌کس هم پاسخگو نیست؟
🔸
وزیر آموزش‌وپرورش گفتن مدارس شهریه نباید بگیرند پس چرا در شهرستان میناب هر مدرسه‌ای سرخود یه رقم وحشتناک می‌گیره؟
🔹
میشه به گوش وزیر اقتصاد برسونید مددجوی کمیته امداد چی داره که دهکش شده ۸؟
🔸
امکان داره پاداش‌ها و حقوق‌های بی‌حساب‌وکتاب و امکانات عجیب‌و‌غریبی رو که به شرکت‌های نفتی‌ می‌دن رو پیگیری کنید. مثلا بهشون پاداش می‌دن که بتونن جنگ رو تحمل کنن یا حتی حق مقاومت می‌گیرن!
🔹
تو رو خدا شما که رسانه دارین لطفاً به مسئولان بگین مردم واقعا از فشار و تحقیری که از طرف خودروسازها با قیمت و شرایط و نحوه تحویل خودروها بهشون تحمیل می‌شه خسته شدن.
🔸
ای کاش یه نظارتی هم روی اجاره‌ها می‌شد یا طوری بود که صاحب‌خونه نتونه هرچی دلش خواست به اجاره اضافه کنه. آخه مستاجر چه گناهی کرده که هرچی درمیاره باید تقدیم مالک کنه؟
🔹
۳۰۰۰ نفر از هیئت علمی‌های پذیرفته‌شده فراخوان‌های  ۹۹ تا ۱۴۰۳ که همگی پروسه جذب هیئت علمی را با موفقیت گذرانده‌اند، بیشتر از ۳ سال هست که درگیر مسئله صدور کد و حکم برای واریز حقوق هستند و به‌صورت تقریبا رایگان درحال تدریس در دانشگاه‌های کشور هستند.
🙍‍♂️
شناسۀ ارتباطی ما:
@Fars_ma
@Farsna</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/farsna/444104" target="_blank">📅 22:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444102">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbea764f62.mp4?token=SLJQs4WwPqVaIaWPJU-Wuwd9ve0c0froBVacOU3831z0b1JUFQTuwhMzH6t59o8ZLzWa98SI5_7Bp-3j8e4mD65zrAEiimAC9VmX0V163EO4-29mnjbudhVpRVARuIucgKoMoSm0BTGCt8q7MC3E1ouaIjq4rFXHTKVmWboqWr1K6eqsjsnKOyYbcW-jmVJUN7bwxXmcNn3g14k8EATG_s6zuYxm6UKanyI2un8rgKjk9jKRfeY8A3Lq9mOSMbkF_94hnYLZcr0ugKXiaKjyH_J9HgrnEGaMlWnpKAVn43ewuLwJxAPowdp1j8WdTh0MgaNXJEVbDMxfQmBb2Xxr3oVZE9xBqYFSu5uwUQ1B5XBcvr8fbCo88nJooCbia-Fzb51zQc38lFbmCh-IlcSIHXWFnCt_6FidGDAJ1p_IRtsKf1E9eNyypnC77HhT0SXLbV01YGmwA9e790SmLOdarsee34L6AT2sP6-9HVTh8waeGI0x8gP_HJ1yxD-ejsMUZfIsgj19_8d6MXsVUQT-QSd62aSghY9rHEk1eDoS21o3NGnp4GeX2n-t2_SwaBK7Msm4Jh9O69qFBzZJAnK4VMqbcLeYn6RJs7-_43Lq4pAjMq7tKcZIlz-UkShP_qIjo1-hV1ukP6h0KJxiqUzztwKhPVxBBlSiMx3iEThZjpY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbea764f62.mp4?token=SLJQs4WwPqVaIaWPJU-Wuwd9ve0c0froBVacOU3831z0b1JUFQTuwhMzH6t59o8ZLzWa98SI5_7Bp-3j8e4mD65zrAEiimAC9VmX0V163EO4-29mnjbudhVpRVARuIucgKoMoSm0BTGCt8q7MC3E1ouaIjq4rFXHTKVmWboqWr1K6eqsjsnKOyYbcW-jmVJUN7bwxXmcNn3g14k8EATG_s6zuYxm6UKanyI2un8rgKjk9jKRfeY8A3Lq9mOSMbkF_94hnYLZcr0ugKXiaKjyH_J9HgrnEGaMlWnpKAVn43ewuLwJxAPowdp1j8WdTh0MgaNXJEVbDMxfQmBb2Xxr3oVZE9xBqYFSu5uwUQ1B5XBcvr8fbCo88nJooCbia-Fzb51zQc38lFbmCh-IlcSIHXWFnCt_6FidGDAJ1p_IRtsKf1E9eNyypnC77HhT0SXLbV01YGmwA9e790SmLOdarsee34L6AT2sP6-9HVTh8waeGI0x8gP_HJ1yxD-ejsMUZfIsgj19_8d6MXsVUQT-QSd62aSghY9rHEk1eDoS21o3NGnp4GeX2n-t2_SwaBK7Msm4Jh9O69qFBzZJAnK4VMqbcLeYn6RJs7-_43Lq4pAjMq7tKcZIlz-UkShP_qIjo1-hV1ukP6h0KJxiqUzztwKhPVxBBlSiMx3iEThZjpY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حمایتِ گنابادی‌ها از انقلاب در شب حضرت علی اکبر(ع)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.6K · <a href="https://t.me/farsna/444102" target="_blank">📅 21:56 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444101">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">‌
🔴
یک ‌منبع آگاه نزدیک به هیئت مذاکره‌کننده ایران در گفت‌وگو با خبرنگار فارس: ادعای معاون رئیس‌جمهور آمریکا دربارۀ بازگشت بازرسان آژانس به ایران کذب است
🔹
این منبع آگاه ادامه داد: در مذاکرات سوئیس هیچ صحبتی درباره حضور بازرسان در کشور نشده است. @Farsna</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/farsna/444101" target="_blank">📅 21:52 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444100">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(N@vid)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y89kJrr8g3C3ZMbu7sL0Yv4LzCBnTtvLqSi_2be9HwuIeAnVbyj_I_f2rFxbH6muku3uUA4sGNrEqWNTUPx2-K27BESf8wX7zu2QwXvzxx6hHVHtvdh49vqJPf_S70w9CYj_Ro6a8IixBbGEm8K8BXO7CeY1YeWKgNGQ_6y83CQUyj1L4_crZujhhytQUcvg5PhMntKOJwi9A9elxW4_CcR897Mug-mYGF2l6I8kB2k2g28GCbDULdMAqgurTq_hRXFXwfL3VDjYyjijzYbppQYWMQ0NgXi13AxswXdeAgaw4ylaeBJlBBjBL1cXhdCttPVy8s6bj-jor_hDqcBSKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
گام مشترک بانک شهر و ساتبا برای جهش سرمایه‌گذاری در انرژی‌های تجدیدپذیر
🟢
به منظور توسعه سرمایه‌گذاری و تسهیل تامین مالی پروژه‌های انرژی‌های تجدیدپذیر، تفاهم‌نامه همکاری مشترک میان سازمان انرژی‌های تجدیدپذیر و بهره‌وری انرژی برق (ساتبا) و بانک شهر به امضا رسید.
🟢
به گزارش روابط عمومی بانک شهر، بر اساس این تفاهم‌نامه، دو طرف در زمینه‌های مورد توافق همکاری خواهند کرد که اولویت اصلی آن مشارکت در تامین مالی طرح‌های احداث نیروگاه‌های تجدیدپذیر شامل نیروگاه‌های خورشیدی و بادی است. این همکاری در راستای حمایت از توسعه ظرفیت تولید برق تجدیدپذیر کشور، جذب سرمایه‌گذاری و تسریع در اجرای پروژه‌های نیروگاهی انجام شده است.
مشروح خبر را
اینجا
بخوانید</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/farsna/444100" target="_blank">📅 21:52 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444099">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromگروه مالی فیروزه | Firouzeh</strong></div>
<div class="tg-text">💎
«
مسگون
»
سه‌شنبه ۲ تیر
در تمام کارگزاری‎‌ها
«مسگون» صندوق بخشی در صنعت «فلزات اساسی» با تمرکز بر مس و نماد
#مسگون
در روز سه‌شنبه ۲ تیرماه ۱۴۰۵ پذیره‌نویسی خواهد شد.
تحولات قیمتی صنعت «فلزات اساسی»
در کنار آینده ممتاز «مس» این صندوق بخشی جدید گروه فیروزه را به یکی از گزینه‌های جذاب بازار سرمایه تبدیل کرده است.
💎
تخفیف ویژه معاملات و خدمات اعتباری اختصاصی در کارگزاری فیروزه آسیا:
https://in.firouzeh.com/kargozari
https://in.firouzeh.com/kargozari
🔙
👨‍💻
واحد پذیرش و پشتیبانی کارگزاری فیروزه آسیا: ‍
🔜
+982152461000
💎
@firouzeh</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/farsna/444099" target="_blank">📅 21:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444098">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/farsna/444098" target="_blank">📅 21:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444097">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09908d161b.mp4?token=JOGo0ZvQxODkpfMIYbisRJl557Jj6dS8GmBEiCOKaum3wdARu0mGa4kFvHtAA6AfBhVnkXYS87O7CYprIx5wxUSMjLKPlO_yHLZzX7sTBPud1ZIsAL5Ugm14aqv5L1KHQ-P8H4uPTgO72hIgRNGdoyVkAUXw9aTyivPPPZKWEwdJGC5DVPfTZ_LMmbP5-ezNLbiJTANSjKlNWq9afPAgfJVSniPTRf2WU0J9sVYIt0G-4-jb2h8veF_bZ-5SonaxBtMwvczHePeZZj5HsZ2gA8Sgqr_74LrjcaLqyCnUbhJ3PHQseAaX34YslTdH6pinO2y9Ttl-WGVhbWmq1jcQcinfUDSNWz7_qrCTTIwT0qiIy66UrJ_m_4ImzKgjBFBZcyGdzSab147HLzq77QNcrcl83M9fCw07y7WaVCNoxEpCprBfFMrJ9ELYi4GTvm8jAxYjb5NiA15_1Cfx4Ze9yfBcb7pZqeBIfHF8BUn9T3nE73SALeV97w9j1z1rvOgIhgoiDemYhmYdS8EmWZoS2X1s1TLDELwy0Bf4H9lHqJAwfHj35zkiXZA3P5lcxPqjveWEfIVJt-_ER3t9_Q6QfvkQQ1tlsnomxk6Fv4s27SkHMRvIBnfx3_xarSY8htFEWIObpnBCP99grl--Iuhw46W76CGOPJwNkFf02vTNTEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09908d161b.mp4?token=JOGo0ZvQxODkpfMIYbisRJl557Jj6dS8GmBEiCOKaum3wdARu0mGa4kFvHtAA6AfBhVnkXYS87O7CYprIx5wxUSMjLKPlO_yHLZzX7sTBPud1ZIsAL5Ugm14aqv5L1KHQ-P8H4uPTgO72hIgRNGdoyVkAUXw9aTyivPPPZKWEwdJGC5DVPfTZ_LMmbP5-ezNLbiJTANSjKlNWq9afPAgfJVSniPTRf2WU0J9sVYIt0G-4-jb2h8veF_bZ-5SonaxBtMwvczHePeZZj5HsZ2gA8Sgqr_74LrjcaLqyCnUbhJ3PHQseAaX34YslTdH6pinO2y9Ttl-WGVhbWmq1jcQcinfUDSNWz7_qrCTTIwT0qiIy66UrJ_m_4ImzKgjBFBZcyGdzSab147HLzq77QNcrcl83M9fCw07y7WaVCNoxEpCprBfFMrJ9ELYi4GTvm8jAxYjb5NiA15_1Cfx4Ze9yfBcb7pZqeBIfHF8BUn9T3nE73SALeV97w9j1z1rvOgIhgoiDemYhmYdS8EmWZoS2X1s1TLDELwy0Bf4H9lHqJAwfHj35zkiXZA3P5lcxPqjveWEfIVJt-_ER3t9_Q6QfvkQQ1tlsnomxk6Fv4s27SkHMRvIBnfx3_xarSY8htFEWIObpnBCP99grl--Iuhw46W76CGOPJwNkFf02vTNTEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظاتی از شعرخوانی سیدمجید بنی‌فاطمه در دومین شب مراسم عزاداری حضرت اباعبدالله الحسین(ع) در جوار حسینیهٔ امام خمینی(ره)
@Farsna</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/farsna/444097" target="_blank">📅 21:37 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444092">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سخنرانی</div>
  <div class="tg-doc-extra">حجت‌الاسلام کاشانی</div>
</div>
<a href="https://t.me/farsna/444092" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
#حسینیه_فارس
|
شب هشتم محرم
🔗
سایر مداحی‌های امشب را
اینجا
گوش کنید
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/444092" target="_blank">📅 21:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444091">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-footer">👁️ 7.67K · <a href="https://t.me/farsna/444091" target="_blank">📅 21:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444090">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">هدف آمریکا از «رفع تحریم نفتی» چیست؟ ونس پاسخ می‌دهد
🔸
وزارت خزانه‌داری آمریکا امروز با صدور یک اطلاعیه مدعی شد که یک مجوز عمومی برای معاف کردن صادرات نفت ایران از تحریم‌ها برای یک بازه زمانی ۶۰ روزه کرده است.
🔹
پیش از این جی دی ونس، معاون دونالد ترامپ، رئیس‌جمهور آمریکا درباره انگیزه‌های واشنگتن از صدور چنین معافیتی برای خبرنگاران توضیح داده بود.
🔹
او چند روز پیش در جمع خبرنگاران تصریح کرد که تحریم‌های ایالات متحده علیه ایران در سال‌های گذشته بی‌اثر شده بود و واشنگتن به دنبال راهی برای رصد شبکه فروش نفت ایران بوده است.
🔹
وی روز پنجشنبه گفت: «صراحتاً بگویم، ما این اقدام را امتیاز بزرگی به ایرانی‌ها نمی‌دانستیم؛ ایران هم... آن را امتیازی برای خود تلقی نمی‌کرد، چرا که عامل بازدارنده آن‌ها از فروش نفت، تحریم‌ها نبود.»
🔹
ونس اضافه کرد: «آن‌ها بدون هیچ تخفیفی، نفت زیادی می‌فروختند، زیرا تحریم‌ها اساساً ناکارآمد بودند. در آن مقطع، کاری که تحریم‌ها انجام دادند این بود که سیستم مالی ایران را به سمت چیزی شبیه به سیستم بانکداری سایه سوق دادند.»
🔹
معاون رئیس‌جمهور آمریکا اضافه کرد: با لغو محاصره ما در واقع قادر خواهیم بود تا حدی ببینیم که سیستم مالی آن‌ها پول را به کجا می‌فرستد و از کجا دریافت می‌کند. این یک منفعت واقعی است.»
@FarsNewsInt</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/farsna/444090" target="_blank">📅 21:24 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444089">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🎥
دیشب سربازان ایران در ۳ جبهه جنگیدند
@Farsna</div>
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/farsna/444089" target="_blank">📅 21:23 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444088">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8ed475c50.mp4?token=djyw5Z-Db7K-TojtK4E-K5uUBvUWQsMNiDupaENSP8JnWL1IiF8ySirGWwfdFuexumhqxpYsLLIpk6wYUd4bA820JXJ5Oged3csII_hYhdIU78cCd2sziVSctUz3yKv_7OmlomeWSL-fvjysh6-_f03x2OF-w9gPQfzY1pKCieOHWbWIkM0Yoyc4DZGsFEulUaIY4t0Q8Zlq98S1DRgEaafM2QXf9bT9hd1nVcZTGcn75OC2Vi1mgG1LOdHyhz-sweO8SyIGhkyx3TtiXEsDJ_lnlIyuyRR2ivLlwOpsMxlO1SuuWAxpr7wq7SwKhS1oew5Vd73084DoSxaGnL849w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8ed475c50.mp4?token=djyw5Z-Db7K-TojtK4E-K5uUBvUWQsMNiDupaENSP8JnWL1IiF8ySirGWwfdFuexumhqxpYsLLIpk6wYUd4bA820JXJ5Oged3csII_hYhdIU78cCd2sziVSctUz3yKv_7OmlomeWSL-fvjysh6-_f03x2OF-w9gPQfzY1pKCieOHWbWIkM0Yoyc4DZGsFEulUaIY4t0Q8Zlq98S1DRgEaafM2QXf9bT9hd1nVcZTGcn75OC2Vi1mgG1LOdHyhz-sweO8SyIGhkyx3TtiXEsDJ_lnlIyuyRR2ivLlwOpsMxlO1SuuWAxpr7wq7SwKhS1oew5Vd73084DoSxaGnL849w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: اجازه نخواهیم داد [دشمنان] حقوق کشور ما را نادیده بگیرند و سرخم نخواهیم کرد.
@Farsna</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/farsna/444088" target="_blank">📅 21:09 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444087">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62dec6eb76.mp4?token=r9ttaQHuRG4PbHPlHStDGIGHR8P8P36PoOTpUBEKIQDG1tNWSGt0IQO-YohioT5W7VRlIQBjcn7jOXJm5744ZC8Lc8ZWW--_yxQ9vEXx0W81AKfOmC-Nzw1sioaJXAhCg5h9cUwpR1idWi2OYcFm1vNlwtT7CakU6hzR0pMObEb9Q7SIl41gsqpeDrb8wQbjIop8e7tXys1u9rFe4dVipI4h2azxt5LiUC8W8wBa3LbaPu1pG175DW_0_ERexPFyqrIWLeB3_IB2YVyTQghUn9ngrY7AcCT2UKWpqpbfi9xzEM3228MfHzuEKdhToP2MoSZZJ0DTBgxff4vmY0iClg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62dec6eb76.mp4?token=r9ttaQHuRG4PbHPlHStDGIGHR8P8P36PoOTpUBEKIQDG1tNWSGt0IQO-YohioT5W7VRlIQBjcn7jOXJm5744ZC8Lc8ZWW--_yxQ9vEXx0W81AKfOmC-Nzw1sioaJXAhCg5h9cUwpR1idWi2OYcFm1vNlwtT7CakU6hzR0pMObEb9Q7SIl41gsqpeDrb8wQbjIop8e7tXys1u9rFe4dVipI4h2azxt5LiUC8W8wBa3LbaPu1pG175DW_0_ERexPFyqrIWLeB3_IB2YVyTQghUn9ngrY7AcCT2UKWpqpbfi9xzEM3228MfHzuEKdhToP2MoSZZJ0DTBgxff4vmY0iClg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: بدون دیپلماسی زحمت عرصهٔ میدان به ثمر نخواهد نشست
🔹
مذاکره یک‌ روش مبارزه است و دوگانگی در مذاکره و میدان وجود ندارد. @Farsna</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/farsna/444087" target="_blank">📅 21:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444086">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f870b96bdf.mp4?token=CPBrS9EJfdlwuGYlBK2UD83BShpi16H2CpHIzNNLusp60BzNIW0X1mpM5osPKgu4esvvw7xNPjPDfua2f8mh8E_zrCqWHoeW1xgGG9pzsjCmW7u87UmFqKQu_YmEfF9t5uCrt2Iauwbb7dS3KlU-8gcozWLc7fyFZJ83TTlVWGbMyhfo6btYRozlY4TPgs8Iuk9WdHf7p38rpGbUC97hoRKBhLzm_z0mGIABRPDyJcXr5UkKgUcsFVOiM7LsYy58uW7xAMK50JPxT8aH8Q7PPWL5TlWVEyP9ezDFg19RPXClHeVRZubfP3ka3e0J6FzhhjPQaJjP9uwKmtJd0XvQ7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f870b96bdf.mp4?token=CPBrS9EJfdlwuGYlBK2UD83BShpi16H2CpHIzNNLusp60BzNIW0X1mpM5osPKgu4esvvw7xNPjPDfua2f8mh8E_zrCqWHoeW1xgGG9pzsjCmW7u87UmFqKQu_YmEfF9t5uCrt2Iauwbb7dS3KlU-8gcozWLc7fyFZJ83TTlVWGbMyhfo6btYRozlY4TPgs8Iuk9WdHf7p38rpGbUC97hoRKBhLzm_z0mGIABRPDyJcXr5UkKgUcsFVOiM7LsYy58uW7xAMK50JPxT8aH8Q7PPWL5TlWVEyP9ezDFg19RPXClHeVRZubfP3ka3e0J6FzhhjPQaJjP9uwKmtJd0XvQ7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: بدون دیپلماسی زحمت عرصهٔ میدان به ثمر نخواهد نشست
🔹
مذاکره یک‌ روش مبارزه است و دوگانگی در مذاکره و میدان وجود ندارد.
@Farsna</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/farsna/444086" target="_blank">📅 21:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444085">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8516b58a9.mp4?token=TZ_7WHs9G6cgt6XmPptTK-tv92fjB_0942UxCR60K8tkGvHcOEBw2NP_QIGMhQQJnVXlXHu7KPF16075H_HyAbKtvOosQL5LAVAJs8ZJBZJHAzRLyQwpOr_w_Sv1nGDSbls4asSVU1PhD18OtnYkc34qEJJ0p70f5iwjVtpqQ3j-3fgVzM6lKxKxZYCmDJXX_giiNR9ngCL0MTmOMiWREzwb-dmJFKfuFZiqcJ4Xy2nK2AP5vdvSAUIlDQ0mpZDyrsW7qyCWploZdkNaCbpbaeZxHHRLUVcW-e92RXv99Coz0m7vWac-eEcwPHBUo_ZyuU48hcfyAYGUt8dqYzE0qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8516b58a9.mp4?token=TZ_7WHs9G6cgt6XmPptTK-tv92fjB_0942UxCR60K8tkGvHcOEBw2NP_QIGMhQQJnVXlXHu7KPF16075H_HyAbKtvOosQL5LAVAJs8ZJBZJHAzRLyQwpOr_w_Sv1nGDSbls4asSVU1PhD18OtnYkc34qEJJ0p70f5iwjVtpqQ3j-3fgVzM6lKxKxZYCmDJXX_giiNR9ngCL0MTmOMiWREzwb-dmJFKfuFZiqcJ4Xy2nK2AP5vdvSAUIlDQ0mpZDyrsW7qyCWploZdkNaCbpbaeZxHHRLUVcW-e92RXv99Coz0m7vWac-eEcwPHBUo_ZyuU48hcfyAYGUt8dqYzE0qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مسی مقابل اتریش پنالتی خراب کرد
@Farsna</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/farsna/444085" target="_blank">📅 20:46 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444084">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X7QTDWrOz3vJRaLM6-m1UgqYWMaR24fnrV0i7voU-GlFMgP3Slyz2KEuuePevDBXjjJohBflKSzHfTicvfe2mLu514r-XfY7cTNPdHGY5QSldnM3g4korg6eTwpboR8EusPkOa2wSgEcVtn6vv1VJrbFT3-VIr7H34IH8GIPstUc7XxiFV1o8yPdkjSrf9t8DKSx88dnwrDo4FRJw9zTW7Qga8NA8dffvm1TlfiO1woUdHPAFB3MFBEstlM_ql_XiD9xh6s8bQpgKH2YOR1XmKxVX9YD6gSV1T_q37EdeZhgB8lem3U7xO9yJ6QGOwRCheQQSedAh-sndBbShNTqtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای ترامپ: ایران با بازرسی‌های عمده موافقت خواهد کرد
🔹
ترامپ در تروث‌سوشال نوشت: همه کاملاً مطلع هستند که ایران با «بازرسی‌های عمده تسلیحاتی» جهت تضمین «صداقت هسته‌ای» در آینده‌ای طولانی موافقت خواهد کرد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/farsna/444084" target="_blank">📅 20:44 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444083">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U1svzK9_Q1vH_z9KVsbaoEJ8GETIi4_NeeVjHcS28XmWO1mWL546QUBOLHaF9Nicc-Yax7XZ3L7l3H2eEmlxd5-AmlVEljH87Uz1qm84kXNeWQFS2l6_oyPtzAkxVKUriNexs2u5B-F4gdvTM2zpGRK2HRR7yp8g7yoVMlwoOMZ1yubequmr4FnXhlVtDCwUR6M-KGUxO48K0P3CNq3dNJLwlFI3o3FZWctx4qqEeXltM5Z4XlQgqb-Q8Bq3GHo9vd5jtcsjryarc7z2II7YoXr-WD2vv5511u3ybsDiT6nSzP5SUVI5poFBxW61YUFmW90yJHbpH0tWG9LQChS4RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تمدید خودکار قراردادهای اجاره با سقف ۲۵ درصد
🔹
وزیر راه و شهرسازی گفت: بر اساس مصوبه سران قوا، قراردادهای اجارهٔ مسکن که تا پایان سال ۱۴۰۵ منقضی می‌شوند، در صورت درخواست مستأجر، به مدت یک سال و با حداکثر افزایش ۲۵ درصدی اجاره‌بها و ودیعه تمدید خواهند شد.
🔹
مراجع قضایی نیز صرفاً به دلیل پایان مدت قرارداد، از صدور حکم تخلیه به درخواست موجر خودداری خواهند کرد.
🔹
این مصوبه با هدف حمایت از خانوارها در شرایط ناشی از جنگ تحمیلی سوم و هم‌زمانی با فصل نقل‌وانتقالات بازار اجاره به تصویب سران قوا رسیده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/farsna/444083" target="_blank">📅 20:29 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444082">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6db886dbe.mp4?token=trPPyxSRLT5_WpiyOR0aQrvofr-TSQ5T1yg6ggCkdNn2Mm9akivzLzwVisKDFfCSNr8dUwQvSli2yqkbTrRCZcsrT8KyezK3Ye5Al3fPYBzlkrzViWcVtdILQtDR03C8lPJZAhkh54E84BCXv0EWycUAFohLpJQq3wZUVnyCWITBwByrk66upX7Z7IoMtgnN5QoUvNBxiplq2Srff9cngWE2Eb5y17Fl_sxV5TouS2CPe5V8H5uTTmsvR1wY6YusVHUnGMF30cYvh_wwRkQ_DJHzW69ctZjijpnLNZuC3nUUCFb6FhcgmRffznU6m0uLnP2IO0IM32q0bQIdRNuIeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6db886dbe.mp4?token=trPPyxSRLT5_WpiyOR0aQrvofr-TSQ5T1yg6ggCkdNn2Mm9akivzLzwVisKDFfCSNr8dUwQvSli2yqkbTrRCZcsrT8KyezK3Ye5Al3fPYBzlkrzViWcVtdILQtDR03C8lPJZAhkh54E84BCXv0EWycUAFohLpJQq3wZUVnyCWITBwByrk66upX7Z7IoMtgnN5QoUvNBxiplq2Srff9cngWE2Eb5y17Fl_sxV5TouS2CPe5V8H5uTTmsvR1wY6YusVHUnGMF30cYvh_wwRkQ_DJHzW69ctZjijpnLNZuC3nUUCFb6FhcgmRffznU6m0uLnP2IO0IM32q0bQIdRNuIeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تنها دروازه‌بان تاریخ که توپ طلا گرفت!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/farsna/444082" target="_blank">📅 20:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444081">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yu-iZYVrYVuQZSTHtIcah5VxcKY2FtmFFGFzfx21UIYofWP4-whKTTZAuLbwSX8ToTaBaJ9qUjU4zvl6Ow4aUa5GmpAjIgmW-v3GInoU96s9wcOwZf1yVvTa5_YwPtutqBXYEuYtrWIYg32yqQSyqTaoRFxoFrL3MK32SKBQWIdP8ICBpxZ0yNgDZBGnT1aeacD_G3swoaleMFM6eAlCveeZqKBr4zBu7mxnT-ao5PhbS6p31Pl03Cifdp1pAMGmS5kvW7DolgDqaev9FyM8GbuAeMepjjQY4IVRZOLBKnxh6d6ocNP8JMywz0VNiViDDSitV_bQzT2KKtvlvSwtYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
هنگام خرید ملک مستأجردار این نکات را فراموش نکنید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/444081" target="_blank">📅 20:05 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444080">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ajdsQumW6b0J93tEf2o3w6vNKaVOq65rm74mCH28cXfmsVF7ncA64tQqxCtdna32GuG8YvbosmFGNQ2HmZkkgHWrXTc0Tm0L-dwqilER-ssX8n-Pw8VUrHNFREa9X3Ti_uYVXEkHRWvF0vndm-wBwBXAnjEuqewfSCaxFQkxsObDvuGuIf3Yk5jt8bspIlLs5G2deVhlEzt3UD1YgxFFwz-nX6L96kK154XtZtp7jTwPqn2Pmzh1IsoCmFm8mrfg-iHJeTkrFWD50bG9lyJC9wfWOcPV9eavFA2eMnhUunOHAfotPJDyQSN7aSzkbZSpGy28hPyvLD3nKKcfI0mpGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینهٔ سفر اتوبوسی تهران-کربلا مشخص شد
🔹
رئیس اتحادیهٔ تعاونی‌های مسافری: قیمت بلیت اتوبوس در مسیر تهران-کربلا بر اساس نرخ مصوب، ۴ میلیون و ۲۰۰ هزار تومان تعیین شده است.
🔸
همچنین نرخ بلیت اتوبوس از تهران تا مرز مهران نیز یک میلیون و ۲۷۰ هزار تومان خواهد بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/farsna/444080" target="_blank">📅 19:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444079">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62dbd067a6.mp4?token=V8E_Edqy8ECo7Cm0O_274bkkq9CUUxhk4-8FxPYv9bcAziJ2olRHRhSNUPnkTpksLwVE4_1Mm3Ga1HrCdmrRUPYOIab9anF10pcyZ_bc6Y-Dp7mVmNlA0Hi-Z-wANqWs55R1HYVsxW10t_l3ux0cGYKkMW486NYh9ZoGyVrgllyek-S5C3n2-FJ0fjgrgRoSIHK8PTV00qdtFdtrUjbNHxMGcdhwpKrwnQq6V0tltl19RQx-9LTWtY5rC4sTUHOvYbRlHPyCUO6APefD-wKbTboHY12wlX2TKtk0f8dBzvbtPZSHSUDMrjBDks3kSNgnWZmk8M820SYxltBmoSehcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62dbd067a6.mp4?token=V8E_Edqy8ECo7Cm0O_274bkkq9CUUxhk4-8FxPYv9bcAziJ2olRHRhSNUPnkTpksLwVE4_1Mm3Ga1HrCdmrRUPYOIab9anF10pcyZ_bc6Y-Dp7mVmNlA0Hi-Z-wANqWs55R1HYVsxW10t_l3ux0cGYKkMW486NYh9ZoGyVrgllyek-S5C3n2-FJ0fjgrgRoSIHK8PTV00qdtFdtrUjbNHxMGcdhwpKrwnQq6V0tltl19RQx-9LTWtY5rC4sTUHOvYbRlHPyCUO6APefD-wKbTboHY12wlX2TKtk0f8dBzvbtPZSHSUDMrjBDks3kSNgnWZmk8M820SYxltBmoSehcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان: موفقیت تیم ملی حاصل وحدت و همدلی است  رئیس‌جمهور درباره بازی تیم ملی مقابل بلژیک:
💬
شاهد بودید که چه صحنه‌های زیبایی خلق شد. بازیکنان با تمام وجود تلاش کردند و سرود ملی جمهوری اسلامی ایران را با افتخار خواندند. امروز ایران در صدر اخبار جهان قرار گرفته…</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/farsna/444079" target="_blank">📅 19:46 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444078">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_lvYYe8QI5B7wVhL5UCK6KAWnlX_D2AsHYYJTyBzq77032-sl8QS6cHHeWpfilI4F8jbrLGIGqqq9VM316MOHy30zVvkvUEKChBOKpdQI_XPUvFmic7RjrDLMa7xfKP-cqpRPPedaTFwJLyCgNhiIG8Jat6jmuFLLHt-Xk_rOQ356Dvnz2aW83EH6X2An8kRXWjOzm-Pl-AV7ZXxrp83l-qcHZpnw9aWEEGeG12ih5h5UP2aXiTeRc97bdDNz32nGd1wepPLcVIMBXw9xEIWHv2VNvV1XDm04DEn3naHvtnifjLDRl2nR9Qa5Fz2LGoornraCx_xT72BO80DFp9Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تخریب کامل ۱۱ هزار ساختمان در جنوب لبنان به دست صهیونیست‌ها
🔹
بر اساس ارزیابی سازمان ملل متحد، رژیم صهیونیستی در حملات هوایی و عملیات تخریب خود در جنوب لبنان بیش از ۱۱ هزار ساختمان را کاملا ویران ساخته است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/farsna/444078" target="_blank">📅 19:46 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444077">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🎥
میثاقی: باتوجه به اخبار به‌نظر می‌رسد ۵ تیر برای سهمیه آسیایی یک بازی بین پرسپولیس با چادرملو برگزار شود و برنده باید با گل‌گهر بازی کند
🔹
گل‌گهر و چادرملو هنوز تمرینات خود را شروع نکرده‌اند.
🔹
پرسپولیسی‌ها چیزی را می‌دانستند که بقیه از آن اطلاع نداشتند…</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/farsna/444077" target="_blank">📅 19:41 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444076">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mOWDbwCAYqFcxvELghuEds7wEUie_Gn_uInYyzHYAPtJbp7sO7KsspcJWj4TSCmXRKn3LK-AAe3xdYcpMZ7CwlKFJl56TimnCG0nxVwZKzxtFlTHV6y2fDcGzi8kVJ0pFapHsoUgxAdk47BDqogRrYXgWWets3k7rNUbARw3QGuJoX9Ibio5L-N5yeyKE3AXOOq6XqiNpwpAFwY6iIs__QqFiMFhPfetajLCGT1uJiZ6Vxsi7MyGousNxUiCjrIZzT6YGnsWUn9tYq8_GiwbkI_xM7s_HDa0epQS4hzIdRHGV0dfguZwBQeCi4e8z6aiY5qlV1JO07Ts1xpFFQBCCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیگ برتر ۱۸ تیمی شد
🔹
در جلسۀ امروز هیئت‌رئیسۀ فدراسیون فوتبال تصمیم گرفته شد با نیمه‌تمام اعلام‌کردن لیگ برتر و عدم معرفی قهرمان این فصل، سال آینده مسابقات به‌صورت ۱۸ تیمی برگزار شود.
🔹
دو تیم نخست لیگ دسته اول به‌صورت مستقیم راهی لیگ برتر خواهند شد و تیم…</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/farsna/444076" target="_blank">📅 19:36 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444074">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ad93d5844.mp4?token=J6GbFr7OOZV-qLGVg5Q2oQrL_2nPiTwn0smpEv7sCShFtXnsz3G-HWNGoZG5iUAx_1XAUd0jVniPW33Nd2mmqt-LKhVmfB_LB4vIVBIYgxqOE4eKKS1rgp4mFkQD7TUnAzR2PZUk442SmIhm2jvmGVCZKPI0VW98MMCbCnCp8R-wbGtv6UK_HEDYhL3gZ-K3M692ra6CoUcBMgB9nyQx-KhjH1y1ZQGcpk7yNfv0jvCcZvusnkdRGmrolXcWqoMiecPkdcPjsUtfp5PI_uwNXZ6bkH386KAJEX9U5spduWI4YWooUSIBV7tMUFKrdv1M3IPsEMUJk9IkgalZJkVDLllHs93eljmuY95Q6R_9T5vIFMIWmHgrqi32yRj7R2vh3lOrA11dfV4LQUb8iSJHqsTN_HmAEohX0RjoqRvFb22hAffWRd4j-QJJ83lxl6Y_wB0VDFF1-3OHeNizBo7-FFgySlVSRdNb7amg0e5eLn-O7HMkKzzR_JYhesx74j0zCMwvNRq5nHeXIJl-BvMOXHWRWZSRqtO4mUMXoiSCFMhgApmKh3nxscvFf8PXMa9gOYn2-w7hmUjWc7Pm8bZwsafMqYoUY20-SqwcRNTlQgN8WaCm6IOuh9MmVBQj0LGB3oR1q4YaB9ghIAwAXbz9JeZVmOp9YvrjggbAh6jp9Uk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ad93d5844.mp4?token=J6GbFr7OOZV-qLGVg5Q2oQrL_2nPiTwn0smpEv7sCShFtXnsz3G-HWNGoZG5iUAx_1XAUd0jVniPW33Nd2mmqt-LKhVmfB_LB4vIVBIYgxqOE4eKKS1rgp4mFkQD7TUnAzR2PZUk442SmIhm2jvmGVCZKPI0VW98MMCbCnCp8R-wbGtv6UK_HEDYhL3gZ-K3M692ra6CoUcBMgB9nyQx-KhjH1y1ZQGcpk7yNfv0jvCcZvusnkdRGmrolXcWqoMiecPkdcPjsUtfp5PI_uwNXZ6bkH386KAJEX9U5spduWI4YWooUSIBV7tMUFKrdv1M3IPsEMUJk9IkgalZJkVDLllHs93eljmuY95Q6R_9T5vIFMIWmHgrqi32yRj7R2vh3lOrA11dfV4LQUb8iSJHqsTN_HmAEohX0RjoqRvFb22hAffWRd4j-QJJ83lxl6Y_wB0VDFF1-3OHeNizBo7-FFgySlVSRdNb7amg0e5eLn-O7HMkKzzR_JYhesx74j0zCMwvNRq5nHeXIJl-BvMOXHWRWZSRqtO4mUMXoiSCFMhgApmKh3nxscvFf8PXMa9gOYn2-w7hmUjWc7Pm8bZwsafMqYoUY20-SqwcRNTlQgN8WaCm6IOuh9MmVBQj0LGB3oR1q4YaB9ghIAwAXbz9JeZVmOp9YvrjggbAh6jp9Uk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: مگر می‌شود به شخصی مثل ترامپ اعتماد کرد؟!
🔹
چه کسی می‌خواهد به آمریکا که دشمن آشکار ماست اعتماد کند!؟ مگر می‌شود به آمریکا و رئیس‌جمهور پیمان‌شکن، متکبر و فرومایه‌ی این رژیم اعتماد کرد!؟ مگر ما با تجربه‌ای که داریم می‌توانیم به امریکا اعتماد کنیم!؟
🔹
همانطور که مقام معظم رهبری فرمودند، تعدادی از مسئولین، دلسوزانه و با حُسن‌نظر و مبتنی بر تشخیصی که در ارتباط با مصالح نظام و نحوه‌ی مقابله با دشمن آمریکایی داشتند، شیوه مذاکره را برگزیدند.
🔹
این امر به هیچ‌وجه به معنای تسلیم در برابر آمریکا نیست؛ اما متأسفانه گاهی برخی افراد، بی‌توجهی می‌کنند و سخنانی بر زبان می‌رانند که دشمن را خیالاتی می‌کند و دشمن در توهم وجود اختلاف و انشقاق در داخل کشور فرومی‌رود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/farsna/444074" target="_blank">📅 19:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444069">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eX1QXngigU8l0wh06j2RfPcEPpr0iwoEuYoJn6pa6ZWmefyW2qkQOa40MKTaZsCaUXshoGhUxZoes4xWyY0Trbg3g8MMQZFArY8DKeBGex__M1QJWeJcAX50Wf5vCwr0m57ZL1ITT8WUa3yYZnvZDSE9nTiRwJE_6Iom1YWvpNv7A14wyPIw9dCWAdqPmGcMUmHviJME7yHdyG1Zf89KROuPNImW_HL-myRFxTp9bLscPzdt0asLnQT3Q7f4gDXiB9faKve2scufLNdKD-9SRQLjCpCrCWe6kh2aMiYqs_s27iR_FBwJ0zCgV8feWXi3AfWo6CF1f0MfpD6eLvMXdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف عازم عمان شد
🔹
رئیس مجلس به همراه عراقچی، وزیر امورخاجه، برای دیدار با سلطان عمان عازم مسقط، پایتخت این کشور شد.
🔹
گفت‌وگو دربارۀ تثبیت ترتیبات ایرانی برای اداره تنگه هرمز یکی از اهداف این دیدار است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/farsna/444069" target="_blank">📅 19:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444068">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔴
ونس مدعی شد که «ایران بازگشت بازرسان آژانس بین‌المللی انرژی اتمی به این کشور را پذیرفته است».  @Farsna</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/farsna/444068" target="_blank">📅 19:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444067">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h0VvAGC2WdexyO-PeXTjXi57GmHTQ6VLTm6UmMAHwx2fn9FZeNfkglplnpAGTgwsxtmqwSdaFzsuU6Ji7CyESZoE6_4x7FEcQUeg4xJTj1dwLcEvM7bNIMBs0ofeekbMF64FKcWrVQO4tanAawxSZq8Gh4DjsR6oGFNgrkY8m3lCbzqRks-1ZfOohvoeRr93alka_9xSK8ivZHxX15HEK3nNyr3HPoUIYx3pp31Ep-5j2xBcerSIsRcG4OJKAAAhdWSkRYQakMORxIf65iF5pOWw3RLoVoP5FPCaqBmeJRsDBmOV96EKhR7tgITimAx0H_yZ2ok9_tZsKH714-K9zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوای محرم را از قاب فارس تعاملی گوش کنید
تازه‌ترین نوحه‌ها، روضه‌های و مطالب منتشرشده از:
◾️
مهدی رسولی
◾️
میثم مطیعی
◾️
حسین طاهری
◾️
مهدی سلحشور
◾️
سعید حدادیان
◾️
ابوذر بیوکافی
◾️
محمد اسداللهی
را می‌توانید در صفحۀ اختصاصی هر یک از این مداحان در فارس تعاملی مشاهده کنید.
@Farsna</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/farsna/444067" target="_blank">📅 19:10 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444066">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۷۴.pdf</div>
  <div class="tg-doc-extra">2.4 MB</div>
</div>
<a href="https://t.me/farsna/444066" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۷۳.pdf</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/farsna/444066" target="_blank">📅 19:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444065">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T1uMqZhzwm0OxWEVqLJ7SpGbMB6eLHjY4srh4wSSGSLyKA3Nm_y4iEAJBwiinMHIEOfIMEJSHAOnXgjpMbhW1f3y79spbZXFj4WFmCwsUZFH5iVV8Uz1LQntdNwRifUhfk1qFSIE5JBflv18MvTuPEiv3LyaSlODzQgRdPPM9Qko6pVNyqSTnk7B7ceXGrXyaCJ6ikqgPegLzUdFyrq5JZqohajw3GPrElJEe248_s40dLvb8LRAzyNcK1Kvez7QabwADzLMOX9eVEUGldhlebzuL7y-vwB9jtzC9cEkou1-zvSX_ppAmIkuTnHthx-E6t9CiJ-HzcTeW6zk6FNc0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: موفقیت تیم ملی حاصل وحدت و همدلی است
رئیس‌جمهور درباره بازی تیم ملی مقابل بلژیک:
💬
شاهد بودید که چه صحنه‌های زیبایی خلق شد. بازیکنان با تمام وجود تلاش کردند و سرود ملی جمهوری اسلامی ایران را با افتخار خواندند. امروز ایران در صدر اخبار جهان قرار گرفته و از ایران و ایرانی با عزت و نیکی یاد می‌شود و این دستاورد چیزی جز نتیجه وحدت و همدلی نیست.
@Sportfars</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/farsna/444065" target="_blank">📅 18:59 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444064">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oe4SfMzlzD07P4ulO0H_bwU84zlz6pySugauzSW-HUvScQ41sEMeeO9oj6bRYqgZtiLrNJY5cz_DVRq7KOmvcElZT7U2IfTD0uaSre4eoiuw_K_nsINFLFr02HPMW6RvrV95F6RskyX4Y3hq0YVzcRlLnP6Il0U-NV37662jzj6_mgRSHTRR0ZnyHfNuZe5zKC7MKN4c8Fc6BL1l3PiZaAWa-YkgFp18g_b0wl4Ix8OOCghP8yRho8Hsr1oaC8iGdIV59hLjyvKcBhh8N-FnlZoC3x0VMcPzE0hn92JYydmVMmSqW0P2n8SoiIG397SA-OOA_jFJIOS_RBdBs1ue1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران چطور در جام جهانی صعود می‌کند؟  سناریوی اول: پیروزی مقابل مصر
🔸
صعود قطعی با ۵ امتیاز؛ ایران در این صورت به‌عنوان تیم اول یا دوم گروه راهی مرحلۀ بعد می‌شود.  سناریوی دوم: تساوی مقابل مصر
🔸
ایران ۳ امتیازی می‌شود و همچنان شانس خوبی برای صعود دارد؛ اما سرنوشتش…</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/farsna/444064" target="_blank">📅 18:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444063">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pzELcmq54JL_LrQdeYoM73aGroSmFYGGnbk7HaPF4K2B5L-71DoUILPYc82Z2z48a-_250LzBn-8AsSkYr099GgdnMRbBOkKLR_QLqDgRKx5e5Q4QJE6zc9Kiq78ucJ0BKY3oqa76l_SdioKRmcZ0jwim6RlT3vKSyDkk55b7jKlhsfTacHKRIZjW3A0NUKJ63ZMZ9YvclxQUzYZapYxkvLY16-ULXuF7qcBUPm5AakL5Ej059R5ziv3rR3H8Gn1-jvLkrgihGDBEZ_GdkhN5svu-SMFk4RlU-J6V7tX_Kk-gFxawI3cYxNW7aVCL09-qV09RShdsJ5TcSEh3F9M6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امارات دنبال تسلیحات هندی
🔹
رویترز: هند و امارات دربارهٔ یک قرارداد تسلیحاتی بزرگ در حال مذاکره هستند که شامل موشک کروز مافوق‌صوت «برهموس» و سامانهٔ پدافند هوایی «آکاش‌تیر» می‌شود.
🔹
امارات طی هفته‌های اخیر برای خرید تسلیحات از دیگر کشورها به تکاپو افتاده است و مذاکراتی را با کشورهای متعدد در این زمینه آغاز کرده است.
🔹
اگر چه، سلاح‌های پیشرفتهٔ آمریکایی نتوانست از این کشور حاشیه‌ای خلیج فارس در مقابل آفند نیروهای مسلح جمهوری اسلامی ایران محافظت کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/farsna/444063" target="_blank">📅 18:48 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444062">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cev0WEHLWuDXCxcSUwjM2NlC3zHfRMEeZAYESNEFskkq4BnZGP46etlz08MDmy_gVePefTQ25ZGYKKsbev4lfpYxRy3RpNU9F67aumMGyZOoOPaF-vh7uPfQFISipsPzxv6_hrPbFW7Che6LIm51TK9-3JHQoFdcoQ1xsGm7UWufEzwFLAEW9YJJV-4T9ge7PW-O109IoMZD18ohrLcXfAUMzBtPRHTUFSC5M0jc4-SnEOoKShxijqd8qWYCdxyj0P6MuBseNTeAZ7bZfqrnhRVaQD6ufwA5I-7kfgGJCy1zkz4hPm8n5358dPDQFRps4ncYc-HLBhw1Sdvvs-MoGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتفاقات عجیب‌وغریب در حریم تخت‌جمشید
🔹
سرپرست پایگاه میراث جهانی تخت‌جمشید در گفت‌وگو با فارس اعلام کرد شهرداری مرودشت برای توسعۀ شهری در حریم این اثر تاریخی با یک مشاور قرارداد بسته و درحال طراحی و تعیین محدوده است؛ درحالی‌که پیش‌تر ابلاغ شده بود که امکان گسترش محدودۀ شهری در این محدوده وجود ندارد.
🔹
ماجرا به تغییرات و تصمیم‌های چندساله دربارۀ محدوده‌ای موسوم به «محور مهدیه» برمی‌گردد. این منطقه در نزدیکی حریم تخت‌جمشید قرار دارد که حذف کد روستایی آن و سپس طرح الحاقش به مرودشت، زمینه‌ساز ورود دوباره این موضوع به طرح‌های توسعۀ شهری شده است.
🔹
هرچند این مصوبات در مقطعی متوقف شد، اما درنهایت شورای‎عالی شهرسازی دوباره با کلیات طرح جامع مرودشت و الحاق این محور موافقت کرده است.
🔹
مدیرکل میراث فرهنگی فارس هشدار داده توسعۀ محدودۀ شهری در این منطقه می‌تواند ارزش زمین‌های اطراف تخت‌جمشید را افزایش دهد و احتمال تعرض به حریم این اثر ۲۵۰۰ ساله را بیشتر کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/farsna/444062" target="_blank">📅 18:34 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444061">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fe1c522cf.mp4?token=IfHB--guV6cBTtrXF9FpspALWnLrqYPUpWMuacoYXkSIr9nWlyCWoBna_TDZ7jkGPk3eamAFqc8FyE0-fxaiKrR6rVUvbtyyU2RKebRMMcHKK35XwFZPvEtz-d8TTqkMAmacBpVJUU9buxZgErFD-A4y4yJCs-AKrRFmJo37DxcN4mLIar6J1UJhxC8j0jR8Jg1H8b3O2CX6lT1md1g4MKqbgZfPMhJU2KCJeqqjSivCv0MJBpAQNX1_9TRr1_afj8r7bEEPLLV1wVNnIUjZPeGCbRHwVvTaJ5ydFEtrYOyCKkeoE6quoi__O7GL_ldHroE9a1xOhAlkkkOa6WtxFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fe1c522cf.mp4?token=IfHB--guV6cBTtrXF9FpspALWnLrqYPUpWMuacoYXkSIr9nWlyCWoBna_TDZ7jkGPk3eamAFqc8FyE0-fxaiKrR6rVUvbtyyU2RKebRMMcHKK35XwFZPvEtz-d8TTqkMAmacBpVJUU9buxZgErFD-A4y4yJCs-AKrRFmJo37DxcN4mLIar6J1UJhxC8j0jR8Jg1H8b3O2CX6lT1md1g4MKqbgZfPMhJU2KCJeqqjSivCv0MJBpAQNX1_9TRr1_afj8r7bEEPLLV1wVNnIUjZPeGCbRHwVvTaJ5ydFEtrYOyCKkeoE6quoi__O7GL_ldHroE9a1xOhAlkkkOa6WtxFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تشویق ایستادۀ ملی‌پوشان ایران پس از دیدار با بلژیک در استودیوی جام ۲۶
@Farsna</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/farsna/444061" target="_blank">📅 18:29 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444060">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2770cc08b3.mp4?token=W6bSbElCGKquG3rmVGuw3HM4dbPjfMdQFLCPYRrCjZo6PRvFhM2RUdHr3423AkQCefUnYIjSqNxGcSmLLpaC1nGLHEaQhTLS1ScdtCCzKFMOwXVnjwUwmdysi9Ft4aLq5CR3FOdwoTM_dGjhtUUO8WeHi3o69wWdeYPZhL1wL4E3AaD90yQoOnusJLqDT0Bkf_pTq0uhcubQFiac--kZAwe6DP9ZDexIWRF4Ou5tN8Hq7NEfwkhb9lrbo__UMk-q1KhRCXp5GbZJWyVFJ0VHbI4PuOXw5C1FZLxQZA7u-SS1weEo8FNaHVxlvNi6KvYBeVfPRq-ItkXdZTRwaJNJWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2770cc08b3.mp4?token=W6bSbElCGKquG3rmVGuw3HM4dbPjfMdQFLCPYRrCjZo6PRvFhM2RUdHr3423AkQCefUnYIjSqNxGcSmLLpaC1nGLHEaQhTLS1ScdtCCzKFMOwXVnjwUwmdysi9Ft4aLq5CR3FOdwoTM_dGjhtUUO8WeHi3o69wWdeYPZhL1wL4E3AaD90yQoOnusJLqDT0Bkf_pTq0uhcubQFiac--kZAwe6DP9ZDexIWRF4Ou5tN8Hq7NEfwkhb9lrbo__UMk-q1KhRCXp5GbZJWyVFJ0VHbI4PuOXw5C1FZLxQZA7u-SS1weEo8FNaHVxlvNi6KvYBeVfPRq-ItkXdZTRwaJNJWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بانویی که مزد کارش را امام حسین(ع) داد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/farsna/444060" target="_blank">📅 18:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444059">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e79f2aa661.mp4?token=Ko8_8sPGzcCN1tZKnNW4fRh7NjX6rDeU3V1nOGvY-0wjY4KZ7rX-xlCi9py2-mWwWqs9R-QAonnLeLJmR-_VB3uzVoTg0gimQykRk2p81ghARjcKaIz8EkXgtQnC48_GVW_ilmxSJ_cAc7AHLGHt6fdTZ4BGZEd3Sm1GAXEAh0aEjDDYp7x0NlDGI1ZOpYrJm6-360Q56xnPvuUr617COBB8xKR-FCODGdO01XWhqJ0-D9RrkwknYZq0bOw5KlDeLbOtY32Ci6azEXwkoX5i65gLH7A-x8601u6lwq_EJ-tHxP9zmiszxebcKF66MdgZhtz0aD4XLnjwrhrO2JTqGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e79f2aa661.mp4?token=Ko8_8sPGzcCN1tZKnNW4fRh7NjX6rDeU3V1nOGvY-0wjY4KZ7rX-xlCi9py2-mWwWqs9R-QAonnLeLJmR-_VB3uzVoTg0gimQykRk2p81ghARjcKaIz8EkXgtQnC48_GVW_ilmxSJ_cAc7AHLGHt6fdTZ4BGZEd3Sm1GAXEAh0aEjDDYp7x0NlDGI1ZOpYrJm6-360Q56xnPvuUr617COBB8xKR-FCODGdO01XWhqJ0-D9RrkwknYZq0bOw5KlDeLbOtY32Ci6azEXwkoX5i65gLH7A-x8601u6lwq_EJ-tHxP9zmiszxebcKF66MdgZhtz0aD4XLnjwrhrO2JTqGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
میثاقی: علی بیرانوند به جهان نشان داد یک ایرانی چگونه از کشورش دفاع می‌کند
.
@Farsna</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/farsna/444059" target="_blank">📅 18:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444058">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🎥
سردار حسن‌زاده: تعداد قابل توجهی از مردم آماده‌اند تا در مراسم تشییع رهبر شهید انقلاب شرکت کنند.  @Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/444058" target="_blank">📅 18:15 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444057">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21f8acdd9c.mp4?token=VuYQA43uGFH-dbl1zoYowbVqgBa0MQdzO95VyM5QvJsrvDJ1_7DmuGZCeBSU9r5J1JnwYGQy7SXhVstd3FI88TadbPAOVQmhwQ_WcdEAzvQSiOQeyi7Wi2HcqmLThoqemSIrcArbbw7hTrBs2-P_9fLmTb9yTSVKJ-oTp6Oxyl5bvc6T07Pj7rNUThh8-74nghzqNjJVHnxPFf5r3YuIUHW4i6cAWIbxv_r7u7-fyoesVnxl0KxU4MixwTTAXew96MP2BZye-u2amJH6a-Vb67eMQb5px9VvyfGyfRKQBTkeg7xRZTLGdzQcGjd4Brror84K5t4SMsm4AvJYOuk_5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21f8acdd9c.mp4?token=VuYQA43uGFH-dbl1zoYowbVqgBa0MQdzO95VyM5QvJsrvDJ1_7DmuGZCeBSU9r5J1JnwYGQy7SXhVstd3FI88TadbPAOVQmhwQ_WcdEAzvQSiOQeyi7Wi2HcqmLThoqemSIrcArbbw7hTrBs2-P_9fLmTb9yTSVKJ-oTp6Oxyl5bvc6T07Pj7rNUThh8-74nghzqNjJVHnxPFf5r3YuIUHW4i6cAWIbxv_r7u7-fyoesVnxl0KxU4MixwTTAXew96MP2BZye-u2amJH6a-Vb67eMQb5px9VvyfGyfRKQBTkeg7xRZTLGdzQcGjd4Brror84K5t4SMsm4AvJYOuk_5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جزئیات برگزاری مراسم وداع و تشییع رهبر شهید انقلاب  @Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/444057" target="_blank">📅 18:05 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444056">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس من</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eCKqai1SqgapW7lYL18Caj164D1lOul1XQWM_KCnYiyo2vhOMEUIyTnVDVuuyLYZ1rcP2K37W455GX8--YwHuXRVSkBOsAcKizCMlv9QY3GW0hUCp5hD0HM1V5-8rRdFOu-PX34SB4eXYOjZMlXP606yU1R3fE7WWEC3rrKGbZPbTDsQ1PElxM82t0L4xgyplqMpEJsd9d0S0AGjvlAg9s6HW9vp1MDr00Ry3i6rm4vGLfA06A4dq3xv8c6hmI2hhYVRJx6fEZ6Pm6ZKPmuZztgzH_jhH5h5-w39NceT9UV8Km4CvRx4sDnA7ynslJRT80QxUMsR2g-t5p9fJwbe1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۷ هزار دانش‌آموز خواستار تعویق امتحانات نهایی به بعد از اربعین شدند
🔹
کاربران فارس‌من در پویشی خواستار تعویق امتحانات نهایی به پس از ایام اربعین شده‌اند و گفتند: با توجه به حضور گسترده خانواده‌ها و دانش‌آموزان در مراسمات و پیاده‌روی اربعین، همزمانی امتحانات با این ایام موجب افزایش استرس، اضطراب و ایجاد نابرابری میان دانش‌آموزانی می‌شود که در مراسمات مشارکت دارند.
🔹
حامیان این پویش از مسئولان وزارت آموزش‌وپرورش می‌خواهند که برای حفظ آرامش روانی، رعایت عدالت آموزشی و افزایش کیفیت ارزیابی‌ها، زمان برگزاری امتحانات نهایی را به پس از اربعین موکول کنند.
🎉
اگر شما هم موافق تعویق امتحانات نهایی هستید و می‌خواهید به جمع این ۷ هزار نفر حامی اضافه شوید، از طریق لینک زیر از این پویش حمایت کنید
👇
👇
👇
https://farsnews.ir/gomnam__3__1__3/1782066119787494110
@Farsnews_My</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/444056" target="_blank">📅 17:43 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444055">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de3f775d67.mp4?token=hcu_18zg0lEdih1q7Txs_aZGt6FxaPBt-qrP7vUFN9QWGCUGynUn61RCm-1onJR37d-SKthxOhz0OeKS6ToWTnqP-f7mwwr73Oos8kHPrlTSTeoiRPEwUR7r82YH3amHxnUvwpNOaPluG58BcfwawYHkzAtHG_VFk-1ILEQjmI6YHPsoqgAqTSMOkn9wZsoq4l-3B2feEgTGJdVMyl5II0vM1DMvFGafUny5elUEQWFBkrQD6z7RuacX-mG9f2VVXoNSAf2Slhf-EZH_IMk7ktt1rJbojc3uFu3LOG1nxz7BixTpzQAn-ir9_FytF3hZjfGPat90ucGNqzoFRaLCjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de3f775d67.mp4?token=hcu_18zg0lEdih1q7Txs_aZGt6FxaPBt-qrP7vUFN9QWGCUGynUn61RCm-1onJR37d-SKthxOhz0OeKS6ToWTnqP-f7mwwr73Oos8kHPrlTSTeoiRPEwUR7r82YH3amHxnUvwpNOaPluG58BcfwawYHkzAtHG_VFk-1ILEQjmI6YHPsoqgAqTSMOkn9wZsoq4l-3B2feEgTGJdVMyl5II0vM1DMvFGafUny5elUEQWFBkrQD6z7RuacX-mG9f2VVXoNSAf2Slhf-EZH_IMk7ktt1rJbojc3uFu3LOG1nxz7BixTpzQAn-ir9_FytF3hZjfGPat90ucGNqzoFRaLCjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جزئیات برگزاری مراسم وداع و تشییع رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/444055" target="_blank">📅 17:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444054">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94a16cdeca.mp4?token=XfhUif5jGo0LrRuIemZ1S78zK8lBV06TVfKLtPLkLjH2cwx6L_ao1EO_YIkH_TLAVvKwcOIX2sLba7k1RK9_x3RzWBYdfpXU3nyau3lMEYoq7d2xL2dsbhhuxTryCnRjHAMVqDW7U2fiNfycJBfZq5vc-RhgVeeGwp9V7WlDqYS3qLsvXzFAXa08ezk4W366iSyP06mNnzEYpT3yeoi4_SLs2aRS1CvTXWzMp60_FGcvZHvtVV9JZm9YKC3blIKaapelVHISL_VnP07zHCxDwvYTVcB3BhbgHLcno06DfhdG7AYOL0bqygI2cdjCLfXmuzEZd8Z6BHN_jW-D2yiGHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94a16cdeca.mp4?token=XfhUif5jGo0LrRuIemZ1S78zK8lBV06TVfKLtPLkLjH2cwx6L_ao1EO_YIkH_TLAVvKwcOIX2sLba7k1RK9_x3RzWBYdfpXU3nyau3lMEYoq7d2xL2dsbhhuxTryCnRjHAMVqDW7U2fiNfycJBfZq5vc-RhgVeeGwp9V7WlDqYS3qLsvXzFAXa08ezk4W366iSyP06mNnzEYpT3yeoi4_SLs2aRS1CvTXWzMp60_FGcvZHvtVV9JZm9YKC3blIKaapelVHISL_VnP07zHCxDwvYTVcB3BhbgHLcno06DfhdG7AYOL0bqygI2cdjCLfXmuzEZd8Z6BHN_jW-D2yiGHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اتفاقات مهمی که در سوئیس رخ داد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/444054" target="_blank">📅 17:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444047">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BHPTnID95zaaPAkLcI-_6Q9f66MRzG8skn9w474YM1bsstqNrNELPVgFQZMVxS6REl4rQpLI9lAmOCODYFBSWF7TzRn5hxSVhmB1AUOzxl8E1H46sBtXlPv7a9M_FgcZxFahtk8CCQOA4vyx-dPQryEuxPu0j_3EhU71i8ISA_9oi99ir8kQDsrpCb8nU_uExGKqLduAZYtHx_aZOm-AqlJt6hP-D0cj10wB0W-IKeLas-fhZTtBWoUEMqhu_D3d2Xpb4UuP0eMeBzpWYGO1caXyjYcEGHY-XKyLcwuUf4rcl-DkqZp3W48UFMcdWf87iBdq5fUXFSfB0cumCLqqdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JuUvadpT3_DBhKmkLI9vzmIgL7yUsbu2MrRCXAKkpC6G3eLi7WWxu7sCTVFVmFDqpr4pI5rgeSF3fVRm0RpBpW84Xf6-ataZG4A-mw1RXcYcyLI7r98duy-m4q5l50UR5xiYzQPR4QeZFhaadC9joaotu3-kFAI31zEOL1yvxNrON0BNZjdG8Tb4-a1AqgIqRO7e7PtjxJMLotMujVG8TjUxn93DNgttG2Wa7Ql9Z0gL7U7D8mpYqrXcMWG7AFV_Ytj6dOqgYC7sa9I_qOBJdUWqOEKYP_EX9Ti0pm61DjebxKVCjHCTTyzVxwNQOxQwjWcttHZ7gIYbTTtdJRFGEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r1HTA48OwEftWJnXnSqUxy3XfAZqZnBg5VQV0bkl-nbOVCWeSdUpQKTkGT-CrZoqifzgD8YLgHqz4Jpu9nmv1J2SUjfvAYEFWjJENrL-Pp7dV8Jevh4oeGQFshkTs-Blgia47jTZaWi9sZWSyHHOA0AYBZbkybPBxj7kDFwWI_TAVV33nSCXBerCnJweJLbfOsFEbUd30492VwHa-PNK-r1dJ0ND_UUbTG8Hx1wzDPIW4VrZzZ6v1biAbEYUXZC31ohOh2kGcGdSvTZCQDFMrS91CS5DbzKHOAwrsGlGiHWHcpi4knkFrwXvlmzq79qCSWZ-H9naO720_fdGEPEQkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GW1cQwlfNGgkWHhRtutYKyG0MEngT-MgDlJwKZTT4yuM7ANwFY1WmLJqX1x5Twx0oosMzpYe4gS-FeejcQR__cUjc7llTPjU6l_G8v5DACcb0nZrt8qjengVY3xn9ZhSKsi7mnmeI_xW1tilVOWn-sNfsaXLWcvT_v9Vji9lyotJkWihVriXhmdzc76gZjP6awiEYFY6l4Uvqb-B5uTGSB3Pbo3afll7oKTd3UX0iy357ZBiYkvh2jzm_jheCj3dUPUGXAIszqel1DdMaV5L7u6-Yz0zblpAHZ60ijOKvnYwB0tkm0Affz_pIfJHtl-EikwRArMORjR6RaFAV8KT-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/daCFhIneuglG-PTDK5K0lH62m71m4S3TuAR59X1KU8pbpkHXU83RPw9RiejK4tjq1ib4LzphTHqRUwDqgGzJ4CeiCZUFvJeZJO8CeuNPCWkQ0L_5_zHv5P1FkvrGsSbqsR4KDt-O16KYk1JjgylY09GF1yc6R-DZ2h3auX2J3me0sUZJquf9-IjMzK9EKmNSTO5HDKUPo_pV2wgU1jukkWKHJaZmwa1xeFpuAqlTYWjuTSiXOgt6QF2DKIRQY2q5Y61PFrKOgjLO3wUPJ4FeVZX1BCeyVI1Iz_oLms5QP_wPBFKsuqmq2P41rJTIDQsfrEKI-SMQyRjqQSMtiU63Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MPts0_ST3-wTmZxgmTJmUNeKj9p4lpIWyO3kF0Ofvl2WYOIKORaLe7EuE4yVXPkP6k3IEuCNO3W-oK3lsrHL-dyB2vHSE8dyjN9PkubE5HIQIgZ1j2dhEs8oddAtmveOwnoIc2kY_5HCaYSX0WVG3gkSUaKM-EsQAay_JRNQfWgmf2VKpWV6s8YPV4_WKaeIuy-0BJQlIQ9qUzvqYbhEXrWS-rTAIYT5EdTp84IC1Y4FrFyLvTQooMotDhXlC5J7dzTEXF6N1p1gJVdcH-PghIblOpJNgKxhlCy1zh7fA9xEzP1X969u-IAL803wud47VbIep0p3oo6E_b-MVyAF6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Un6eBCiy7qKYJxCZwNircS4xVjpa4Twd2a5yWxp29P5XduGKUn8Xby3-GxCPfZowMV_ZSAPq7o8emaUHZPxbDKMUrmchDvOZT8-Kki5FD8rxXLflcvcTids1OyDJC1k5c4IxUW766p35hf2k7H5sga0kpMfZleuN9MA4FmLHSJds7FTeMC_lba146FlatLUdMfdiOZCcJXvmnMe4e0_99ZEkrG81xb9XtmkL0CWjAhUKgkcDG6fPbVx-p4k-Qmwt03msg9_QMbpxSbElO-38m0rlDJbNCrUZxcMA8BLXEtwB-eaSrHhMYr3IX-cDZL5e-mar7Kuxs4ugEAZhL6Sjww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مسابقات تنیس روی میز انتخابی تیم ملی ایران
عکس:
هادی هیربدوش
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/444047" target="_blank">📅 17:14 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444046">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">🔴
مجوز خزانه‌داری آمریکا برای معافیت صادرات نفت ایران از تحریم
🔹
وزارت خزانه‌داری آمریکا مجوزی برای معاف شدن صادرات نفت و محصولات پتروشیمی ایران از تحریم‌ها صادر کرده است.
🔹
دولت آمریکا در بیانیه‌ای گفته که «تولید، تحویل و فروش نفت خام، محصولات پتروشیمی و محصولات نفتی دارای منشا ایرانی» تا تاریخ ۲۱ آگوست ۲۰۲۶ از تحریم‌ها معاف شده است
@FarsNewsInt</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/444046" target="_blank">📅 17:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444045">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af61564701.mp4?token=dd_WZ669Pi9_3TbEIL5YP1sgvNpTSa6EKQT3R3rQ7opD_2NDFkRKmjIeZ0KlyxMVJW0YpAaNNHCJNOhejqkThN1Tnm0NBoY8AeMCY-jEtP57sJ7hsb-RHnwVVtsc41_vf5f3dLEDWssw1A5alxwPB3esOcwMIYhPqVajntGc1i0S7nd844iTfLkkyxcthzlUa_fJDz__XVPbbWKftdfNuGMpfDrx9RiA4tvCFmwpda_r_baTm2wQnrxHKKWwOPavUUBGqOrLov4xi6QR-584gKSE66fWjRwC7jDFVrMn6gFIAOeacSYdBj0dwQtbqxWHcygKZFnbXl22fx-VgUPVL2hpjtCQY7d-NZhuclBJTlHSuKRVrsn8K41O907IAbJULZWcTOXIvSPsxqj1m_8lLDNcoM0tmZzjquxo9RtQMEPbGsnX97U9kc3nv-C-ZndEeUSYjwQ-Uc4Y8bPmSjKeFRWLbaqObEutzvLFDrjUl38SRmeMTNoq0vCB-dcPcrclU7aeYwqHwuLiEzhQAmx6pi1WVyddMAms1tsY4Th917cvGtPkEtbG3AmA54QlGPR9LYxD_fg5PRPfI-kAOHFC7m52oaND3nhgnJqbk0-SF9LlSb88dY5-QMiHWtVOGFl4iMjLkFnz3nvipDLntC8f8q8sy-bOuhAdHj4Mcnnn-JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af61564701.mp4?token=dd_WZ669Pi9_3TbEIL5YP1sgvNpTSa6EKQT3R3rQ7opD_2NDFkRKmjIeZ0KlyxMVJW0YpAaNNHCJNOhejqkThN1Tnm0NBoY8AeMCY-jEtP57sJ7hsb-RHnwVVtsc41_vf5f3dLEDWssw1A5alxwPB3esOcwMIYhPqVajntGc1i0S7nd844iTfLkkyxcthzlUa_fJDz__XVPbbWKftdfNuGMpfDrx9RiA4tvCFmwpda_r_baTm2wQnrxHKKWwOPavUUBGqOrLov4xi6QR-584gKSE66fWjRwC7jDFVrMn6gFIAOeacSYdBj0dwQtbqxWHcygKZFnbXl22fx-VgUPVL2hpjtCQY7d-NZhuclBJTlHSuKRVrsn8K41O907IAbJULZWcTOXIvSPsxqj1m_8lLDNcoM0tmZzjquxo9RtQMEPbGsnX97U9kc3nv-C-ZndEeUSYjwQ-Uc4Y8bPmSjKeFRWLbaqObEutzvLFDrjUl38SRmeMTNoq0vCB-dcPcrclU7aeYwqHwuLiEzhQAmx6pi1WVyddMAms1tsY4Th917cvGtPkEtbG3AmA54QlGPR9LYxD_fg5PRPfI-kAOHFC7m52oaND3nhgnJqbk0-SF9LlSb88dY5-QMiHWtVOGFl4iMjLkFnz3nvipDLntC8f8q8sy-bOuhAdHj4Mcnnn-JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شهین تسلیمی، بازیگر: زندگی‌ام به ذکر «یا حسین(ع)» گره خورده است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/444045" target="_blank">📅 16:54 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444044">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HY43Mn8E5ml8KmJuTu54vXg8EkPl3LSt_jnny-a14QDge8vXsSZpFzeWoo8TPIpvDV-82d-hNNaS-2RcwmDrj01QSpZx8aHFAG4oNWqsG_sng7y3Mt3mOEtm7usVpv7KPDb7BT0LqysQw41bhfRpl6Nhq-KpoV_QyBomR1CDCUQTAIp2qq4vRR0j0RF_aG9XMQmtMaF87RSBTaFwRoywxwQKJ5oQt1y2iIFkhJP54tLjruxkG6GSaMB-kzIy-wKWhfJMUi2PPi22MIzhxZo9QkbxoBZOm3JoOIH1BvAHTk6aSaiYtsk45LfPs0NTLT143hce4VC-IQA0jZMb5wbKuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنگهٔ هرمز صادرات نفت عراق به آمریکا را صفر کرد
🔹
جدیدترین داده‌های ادارهٔ اطلاعات انرژی آمریکا نشان می‌دهد که صادرات نفت خام عراق به آمریکا در هفتهٔ منتهی به ۱۲ ژوئن به صفر مطلق رسیده است.
🔹
این رقم در حالی ثبت شده که یک هفته پیش‌تر، صادرات نفت عراق به آمریکا حدود ۱۰۷ هزار بشکه در روز بود.
🔹
علت اصلی این توقف، اختلال کامل در صادرات نفتی عراق به دلیل جنگ منطقه‌ای و بسته شدن تنگهٔ هرمز است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/444044" target="_blank">📅 16:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444043">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L0RSlsGvPZajlbYLfGLR2ivemja40DTu8OVnN7Zg1XaRFcI3U5VnYZdxAP0TrQ2R7X9pF4gjinzE-1ImGFsrgtptS6Nt_idC7UQegHEktz5tMsv1ZbPcEOfIAAKFxXBCXp9Wueb9k9_wb531oPUQbMx4V-i9oN_prxTJP8RAjIdpdOuqEWj9eHktVA6vrxQKdo1JPnMcVNIApp5yfpTEf-nCFvmknuJuQM_Gn1dQiV4n56MLLBuoeQKZVWnLONYO2hm5EoXzMT7ezhqXAUe_Oo3jE878U_QFwjwo4twLrLQU_fmV8cgz3LuMa3EyPPnW4MrQRCRnKWCB-ayGinUABw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گرهٔ قرارداد ستارهٔ خارجی استقلال باز شد
🔹
بر اساس آخرين پیگیری‌ها استقلالی‌ها امروز باقی ماندهٔ مطالبات فصل قبل یاسر آسانی را که نزدیک به ۱۲۰ هزار دلار است را پرداخت کرده‌اند.
🔹
یاسر آسانی پیش‌تر با ارسال پیامی به استقلال خواستار دریافت مطالبات خود از این باشگاه شده بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/farsna/444043" target="_blank">📅 16:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444042">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NVHYnrWvmhpJqa53zIZT-5OIOSJsuKVnjDn6K5AWKeXs75OCM1Hs3qRBuHCKgroZBcoZ9Wfq2NnD5qEf4FVTF78yjM1_ZLpv0bRrtAZC1bxGbVXaXHK8SeN2S6KnQZKNg2pKjp78OZPmqPhSkkpIZKfNoyxCOcItgvswsqc_QfqQdTI7jetwSoF0onQLjcRL6HvldhEKn0ZYG9zHmKvducMLVW0X5V2K0qC9M72vGbKvOYy6dfckwusNBU7z33bjpjr47E3TSMeulEL0QbkCP0DOFiUGy7rwnXunboWlPHI_HYKxO5gV8GsUunANsNv2Lhgfto74aA9OFL7DLPmEiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آسیب هر وعده قلیان برابر با ۲۰ سیگار است
🔹
محسن فرخ‌پور، متخصص ریه: هر یک وعده کشیدن قلیان، از نظر میزان آسیب، با مصرف یک پاکت کامل سیگار برابری می‌کند.
🔹
هنگام کشیدن قلیان، فرد حجم بسیار زیادی از دود را در یک بازه زمانی بسیار کوتاه (حدود ۲ ساعت) وارد ریه‌های خود می‌کند.
🔹
این حجم بالای دود در مدت زمان کم، می‌تواند آسیب‌های بسیار خاص و شدیدی را به بافت‌های ریه وارد کند که با مصرف تدریجی سیگار متفاوت است.
🔹
اگر فردی تصور کند با محدود کردن مصرف به هفته‌ای یک بار، خطر را کاهش داده است، در واقع در حال وارد کردن فشار شدیدی به سیستم تنفسی خود در همان مدت کوتاه است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/farsna/444042" target="_blank">📅 16:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444041">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c1d5f7f33.mp4?token=W54OEBggCZpD4mOt-3ajpU502iEtlPDb5ScwHWHY-MEImIwiGntK3I7Q2JyplhOiQ02bIrCrjD4Nx4xmNK0jxHdxB7M6sue4dwqzI1V6bfx1vnLxvse15ZkUtp2oTm0AoUe11gtG64tPCWvrjMM3wQpFWzDNv9uvhSsC1cnu5jyEkZWOmh_MYA40ysfma9gBIerh3885aa42h-Lol4uEfBDcETXgJRT21611BIeOrdBlhT7V4KfhVoHv2yI05adYDt-FqXkSGNlowzrvURY9yKIMdLtcMZLmxkRHC3umU4tC3lQV6XZtZE3UVcP94s_LmYOzm3Dg5s3SGmuYKMmI-bfteq9gwJbQXULpeUwj7vXBtRyebDGGYOd4sX1Blujx7ZCkvyKyxmfNriFNZMQPX5vLOMQQ2mqySO2wCUhuscvP5i4MIc5hgPUlVq7in1uAtatPTlcllCxjKqvhC-U9U_mp3IAEZz5jxar61boNDpqk3CStNVlPuAE76hYdj2OVs_KIY-4ddqVIJv54mHZawjFbiKU3i2kES2AGZD-_3rlywB-mjlUKaH6E7MR6NbLCnNiMi6ZEJwjLtBNUThyRBqr83SuLt89kI0dPTQdpvd9WecoiSVARESU2f1gYKfsYryqj9oHENO_t5mnF0y6367gLFN8KnTyQI0s9tQPzbMY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c1d5f7f33.mp4?token=W54OEBggCZpD4mOt-3ajpU502iEtlPDb5ScwHWHY-MEImIwiGntK3I7Q2JyplhOiQ02bIrCrjD4Nx4xmNK0jxHdxB7M6sue4dwqzI1V6bfx1vnLxvse15ZkUtp2oTm0AoUe11gtG64tPCWvrjMM3wQpFWzDNv9uvhSsC1cnu5jyEkZWOmh_MYA40ysfma9gBIerh3885aa42h-Lol4uEfBDcETXgJRT21611BIeOrdBlhT7V4KfhVoHv2yI05adYDt-FqXkSGNlowzrvURY9yKIMdLtcMZLmxkRHC3umU4tC3lQV6XZtZE3UVcP94s_LmYOzm3Dg5s3SGmuYKMmI-bfteq9gwJbQXULpeUwj7vXBtRyebDGGYOd4sX1Blujx7ZCkvyKyxmfNriFNZMQPX5vLOMQQ2mqySO2wCUhuscvP5i4MIc5hgPUlVq7in1uAtatPTlcllCxjKqvhC-U9U_mp3IAEZz5jxar61boNDpqk3CStNVlPuAE76hYdj2OVs_KIY-4ddqVIJv54mHZawjFbiKU3i2kES2AGZD-_3rlywB-mjlUKaH6E7MR6NbLCnNiMi6ZEJwjLtBNUThyRBqr83SuLt89kI0dPTQdpvd9WecoiSVARESU2f1gYKfsYryqj9oHENO_t5mnF0y6367gLFN8KnTyQI0s9tQPzbMY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عزاداری سنگ‌زنی مردم سبزوار در حرم امام رضا(ع)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/farsna/444041" target="_blank">📅 16:33 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444040">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VGV5nC-lnkXT-FQM2HgINvET1YTcyfGR8rIKzZFNmNgzEBEcRsHjySRODgGW_Zi4bMtSuNocAgBWfaJFJRdn3kISSruO2uspUrZj6VIIrmrbMrp-VAbCtb5BttCl_ZhMMxTUR27HuwNa1A3_jy-3-cxOIgv9yNxfIS0XX6JGr9Sg3o5b2pd1fK_hZpSJYD0h2rlSbhhDGpxfTcCkMGXCYbnlfPIufuh82hG1NF8mnQNOz83WbS6YDcGH0CXiYn_jw4yIEXCctUYaIFKRHO0MwdtPvDVUwShi2nOId3oBrXk_ra7has24T-8VV0ZVswLYT_CZHvpMpwhgwpnMurHV2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
تأكید مدیر عامل بانك صنعت و معدن بر حمایت از تولید و بازگشت ظرفیت‌های صنعتی به چرخه اقتصاد
دکتر محمود شایان، مدیرعامل بانک صنعت و معدن، در حاشیه بازدید از نمایشگاه ایران اگروفود:
▫️
در دوران جنگ، خطوط اعتباری ویژه برای صنایع غذایی و دارویی اختصاص یافت.
▫️
هدف، تداوم تولید و تأمین کالاهای اساسی بود.
▫️
حمایت از سایر واحدهای صنعتی نیز ادامه داشت.
▫️
بانک از بازسازی واحدهای آسیب‌دیده حمایت می‌کند.
▫️
بازگشت ظرفیت‌های تولیدی به چرخه اقتصاد در اولویت است.
▫️
توسعه صنعتی با استفاده از ابزارهای نوین تأمین مالی دنبال می‌شود.</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/farsna/444040" target="_blank">📅 16:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444039">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FMV6MXKUBUyan_7zOtyhLAb2Av0VsBAIJbZh-UkGyL9NZ2TuMdOr48X92KyGayk_N2-Hhp3VR-Zu0DJlEMzOZ7II01m8wUaF3I8_1YkPS_jyXP9qBtXbrBU6xVhfFTQmq7APEk1fftIyTJs4wwfyHS3F2erh-O2crT8aZH_aQyClpfbq1YGAAiWRCaWFrOKhUANMZako8LUoiyTCRqQgZxJovPmuoMe3dXKbbKDE2e0dw4Hbm8zLYDcS27FWNkGTlnWUErew4CkxExiNjw4vXpwM-WahpJppIT-SapuVFCM-P2Oo8CUsSY4NnNHKS6xbM7_IxbwtcWcPjbTnDFzXmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
به مسابقه جام جهانی دعوت شدید!
جام دی همزمان با جام جهانی
با جوایز جذاب و متنوع
⏰
هر شب از طریق شبکه ورزش و
ویژه برنامه ۲۰۲۶، همراه بیمه دی باشید.
پیش‌بینی هر دیدار،
جایزه داره تو دی‌دار
ورود به بازی
daycup.dayins.com
#کانال
اطلاع رسانی شرکت بیمه دی
@dayins24
#دریافت
نظرات
@prday24</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/farsna/444039" target="_blank">📅 16:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444038">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/farsna/444038" target="_blank">📅 16:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444037">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U8j7em-SENrZghaavR9jL3GBpG01HR4vavKEbyy6gqLct_y-8RmSxwz2J_KQJkh9MYQN8O0ayPjn3MleheCtNena0M9XXgGbyb3XQ9LGYJc0fetepsIiK-NXNwNEhBE5yXy0WenH61Ys0MUAao_-W9p48zkFv3bJfK-3NLoSanVI1KwEzmtpNsdGgyVFhyOgKXQb9eq6AEtBZYsOl5HXtBsk-DLNDOJHq60_3hjvnM5bMknSbFODBa0ecXpMtWmbmjEcVQb_ETzY59X9AASL-OFsyHMeKaub0STZOOU0PEDI0FP9ATMeGOBoYlq6H4cswmD6WBNpjoFylCQCdc9Frg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طوفان در راه تهران
🔹
سازمان مدیریت بحران: مناطق نیمهٔ جنوبی، غربی، مرکزی و ارتفاعات تهران در معرض وزش بادهای شدید و گاهی بسیار شدید قرار دارند و احتمال وقوع طوفان در این مناطق از اواخر امروز تا روز پنجشنبه بسیار زیاد است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/farsna/444037" target="_blank">📅 16:23 · 01 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
