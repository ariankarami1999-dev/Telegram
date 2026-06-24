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
<img src="https://cdn5.telesco.pe/file/NlRYHpfbA9eTs8I9V2rRcsntGC62IRydWo03sd5Zt6THfZ4NUaU_peuzXCT7svTbwHxXR3tc-ad6tUBsaWwp6ZGQwVArUloMGg8-C908ojgR3vG7kVuzJ7XTheoNCyYTvPeydYmyDGhoJ-VaWE4Cc-I6o3kqMwRgO15HAxAj6dMPWV-x9WRD5Xvfg__z6D_eit_stShGKDM_XnOKb-93AlG4ZzzbP1qICZKZNbRMETzYwREHiFlSC_IXNFrKL4KQdGzZRBc6_twA2zSCOzNQlMn63LDObI4Be0e1FCLa_OXBX6bN9PnkL6wbHk7ZDsJ5SHpnUMTayf73Bve2o_EhCg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 716K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-03 05:59:41</div>
<hr>

<div class="tg-post" id="msg-95579">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hwinwJvCaGxpsdyELLAzJMDzCWlCVtUtAJmPp9aYo0b3gvU1JuESF1TiDF1xNWi2OftpwWjJJUGkDucJ3NuNuhI7iCIm1H-8lTLPozd2NCwL5cj7toJSXy09mH2jpOa65ceBsmQ0QaK30LMNWU0Odx-NVdXfHjoWrRABf6_sbk-6JczhJcbuOsIYCkFfcCCm-TZxJBNEAjwf9vjvhE0FC1TkpuTdq7CGLcCOlIe8eVm0V4qaheoQHNEWL3d7Ko9v2AnlmAJ7M12ZU30wE84u5T0Muesgj-OfrpV8TdRW7_4cP4VtNcT71Yu1XYegmAWWq7UbxXDO9zVK2bP6FMoiTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k9Bjapf99nFN2i-aAnwQ5seiwFe2ginGazSkKvLNqnR83JZG4oWislKmxqn-eramfcZ3t_u3HS-21Uhw88PDa9t0zzHKj5MPrn0bUUnjC62kI92CxcrijxZit68C8SkAIrXnRp7OfMi2XU-0wi2e8lJi2rTf7zRnuzAqxdyZkugF2oFD3GdRGqNohQkn2_kMJW70V-kxuVRPKILYp4wOYoVEqwMx5_gRNLyNPU19i6G70ILVVzuJ_o2njVS7vTahBHWJyyJvgB8T_Z8Ws9v5Sjt3q-twE0KUNF2a7LbdSgnMJPRWRfI4XgMP2_UZf4M4U580Bq3QqflmVbjwgk085A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jS9WjiS2QjVXjFKeckE74IRm4nIxcDHSfW8SBkBmffvN1d6F3mY2JQba8qaTfrywDAZ8cJ3jFqy38LHTO87hv-3XXD8qlCw8Ttc6B32ku-XniblbA4qzTphRh_9g_EW_K9ThH8qFMuy51dyi7mL1v5B_MByUAPOQIcTUEH9va7Invthnf0oov1BzECOrw8D6ZA8ZpoOVwDv9He5j-vfiL21xDKEZWR4eeEfwiJlSAgFD2n3oND9BAoj8IYWaiappB3LBvdajFqrJCfuPaojXjBMpuiftNMAJH7TveNNqr48GVnK91ciFYy5dn89OPVelzQC3d-gkn6I5Wxp5ITUi_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ما که خیلی وقته بخاطر خامس طرفدار کلمبیا هستیم
🐸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 943 · <a href="https://t.me/Futball180TV/95579" target="_blank">📅 05:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95578">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">رد شد.</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/Futball180TV/95578" target="_blank">📅 05:37 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95577">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">گللللللل کلمبیا زد.</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/Futball180TV/95577" target="_blank">📅 05:37 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95574">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aOKTm9g8GxQ7IaiudAuXAEptW570ePWq7A4hzaXBgcVHGVOkHpaMl1YA6ewFaBGe6I-2bonAm6D3GuNxbXc2QHX4B8nME6RbkkD7esFwojwnC4P2zaYsQIXtJG0Ua2nqy-wZ0M3p46wp7FACyUs1y3XbsjICQpFHwGj9S5lSzYomHK4PlS-9_HFgUat2XS4LuWwaXhODB7uQSBqsf774KIaWtlNSjigIf1AIexeWda3j1j7e125ycNzpTEZ131ZDzOWIVj-lPsvSLlsxuWdxyk5qCO2jDAtEg7ZWeNAyQ2t0as-Yn8VqsoWQ53ensfrV1Vjea-NaOdgiMMhgCVUMpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a3xMF9gelCIJ98mJlqeZy-3KdTBYlcvkvmTWO0FVPWn4i7Y6quD5qKqhZ5c6ytE8VSVV2PT0KEXtRpyTu5uAn8UU4KZG5ADYAbzr0XcXaD1xMbs5vU2aXNaks6ggY-IBa56nVSA2AjAn-PdfcWEyVchkBhfCAFXRilKqBIrFbFuenqQYI7ezefxqKffEwfkdiRMjAfYGWM1hUN31-Ftz1Hu5-Ebj0RkIe53qw29JHg_GekzeJj8mV8xUXSct7UizNJF5d72-3UG-uNGxJrMk0EVV7cKIseGmZozBCWz3R80xYhNdD4oRFCfaReTwvNqbE647AsUvKYW88A_HeuWjBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zwy1u5d33JijGkMhLUBLK2IQ-RmX69RZWLJPaQK6NhbR5wHtM3eHQr13cFS-P-Apgn2SJ_j27C_WCQem4D4dAN--YftMtOYpJrlYYvtSMEijsyM14E2xq16-h9hJ0ECfcluWMNhmjv4eqL0OVPUo30h09pgCxhtN0ZjeUcBTugDmRy7avVRKz1-9K573GzMOvLOtT8Kq0bEAl-YmgS3iz8xsMePgrx57OeeqhYcHzF0D4KiQ9tLNFZ8gSu54sp3UeBDhJGiAo3IEe3dt7nlYDpQRxMlZ5VSzwbp8rTaUjDIMQ0wA5k9Ofglh-5lWgqA9U8XAciH9FpKu9hTwapzaxg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
🔥
جشن بازیکنای کرواسی به مناسبت رسیدن شراب ناب به 200 بازی ملی:
⚽️
200 بازی
⚽️
29 گل
🔥
31 پاس گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/Futball180TV/95574" target="_blank">📅 05:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95573">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">بریم سراغ بازی کلمبیا - کنگو
تنها نکته مثبت این بازی حضور فیکس خامسه.</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/Futball180TV/95573" target="_blank">📅 05:29 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95572">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rAH1gWEQ4sL57-tWYl44GV6f4_uqn44C7Faqx8OqdDm4-jWnHrOhSvxFcFbscf-Nae2WeahtokjMWCWg6DCJvRMh6bsnBR_TuNB7yVgOzWypQl3NXhvxkHbH0A4ZNwf7-00Fj2lDSFzSY3W2hyFbxD5la1H_4lsPATXEG0P_sGVHekspLb1EyZMsC_tYt53sPZ4FmHtfFazmuwoT0Me8_4By0a2bDKQqRWznBFjqeiqOgY6v_Acr0NXlebCAWrQU-5tT-gxz6-nKfYK89a5qIj7e2zALrezaEuoqVZd2yI2qM3SHq0hR-8WF92zqiHJZaU24DAaTC9GHXl2NjqkrYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تکراری ترین عکس این چند روز چنلای ورزشی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/Futball180TV/95572" target="_blank">📅 05:27 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95568">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RkPuy47QxqGRqs9qlHcgcCxZhCqwd7POk18ynu4P8gy9z2bUSRebwBJb2JCxF4--iO_XNn9bKzWrdzsFaeHGSRkbntx3kdTJR9yJTLWmz8doEoSQWHawuQjAkIujQl925wmfKsgjc3nOLJ_ppbTwJmLJSaGX8oowMwqIz6L3kK5xW04_3HpYCF7gBDEcsw5JZ2VpQhKUoCpqw3l_NrXJX6_PmcxcoeyhR1LDUUIYeyKsabI7qtgKEdbyEZnL8QyW_pAOfkieF01FizQxbB4S4pSk_E2xv4GouCdo0n_n0soo3wu5fuhNVf64X4w6YC5JYSn_Bsfh_L9Qe9Jj9ctI-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g3A0zicE_Q-hJIxLT66-w_Dzxg3AsBiss1nXeVYgVewYVEoF-1dFB5xjLkDP5OVnjmhJ03ekB9EV-CCKssXFxPdu-V2Y0Sj2yFDGrOdMibdMEMOQrQ3bFcWpPiVMJV5ZQ-ysc-IVAtIvjQPr20r5yG6jxQ4bjSQH9C6dUZs3y2MCSnRF8LFA-VJEoKNqsnyN45Gnq1FkKNCgHl-XfH7tXVVtm6kLN5K4OnKScrsa-mKmH_x4pXmIu7rWcdwjtzJ1wFiBydO_L4SlZsxx4NItv1Airo4eEAdB_uT_q_UBUQCTtfK53pV33krsUEL1L0YZJ9G9b_OrhFyNErTiOBQwdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J2PhKe5uZExWsaNz3MhqRcf5O4fzhDAMiZq_AqW9jaBLHcWGWmfd2nTBtozF2eG9hPUcgNP-6wSnrnu_yQGbAoTLRPF3voYV8IsJWW9nT2MQthzVIK1jlR9sSnbz40Ayc-6zxuExhYfIo73zvONGEdzZA_UFdBQopB0pY5TymMkQA0c_doMmX1UPu-kGKlxa_Qc9XZKHsnXo-5Nwom8OmHFjlOTIEdyWzDw3ukWUTDcUcMprLoPCnJxboHkIIcPVLkzVoCG6pxo-Gh1YYQ5936FTiltTz6_RPEe-S1V40BSnPLNQYC2d5kqQf08UGHqaTfk9iZ8XmXsswW7bS61cEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sk7OmLW2qR7SzpooaeK0S_AfURi-bVU-ROWl0b9BhXuLLwGERfqCLN5gRHs2MJiMdbGyeNPATDrSJWZ1Uq7BfVDr_dPQXqZ8x5jImy8ZpFkJDl80gGub1fWtXxHjbvvj06elagJo99rcwySS8mVrR9gf0PXrY7RVNdtxYpMi6cozxzGFK_rrsXy2IsTwgVLd6uoQVg2Qy_BctXfgk52HPheam29sxM_0e9jU0K2iLIhXF3Qbt_rHex2ioyA5rE7iPcvuBgTKHwZP_x4UEtY-Ihcxi3tXwy0vMN6UAQwF9w5Yc-5Yx6Mf91drPn2pA47EQDb0e1F9yUFPAgXQd9i3UA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این عکسا چند سال دیگه می‌ره تو دل تاریخ
🍷
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/Futball180TV/95568" target="_blank">📅 05:16 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95567">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U5u9dpHVgmAtJPGRp8sExyGg6JAe_OvBGChDCe62aRTrhvqUoycQGSCdQzm-vBCEIk9OehwZg36U0qT1zL9d6UudkECOeEw6AFZyNp0cSd_ApbWmviNqNEyJgUn1196Ct8hEiFFCBexbvDl5nhHZ94wcrBNF_KVuh9nX3dNCM6Aj9SmeREoFgpmo_jbX_0_HO4HWK6qkYjq273Mort156kGN0CDv3xiT8pJ6pZQoQG_x8PnksFFnDIjL5zzMptEU6L6eK47ouFwTSGZJ4JRICSkW9zM2SOSGzADmx6YWUAsoDdsNiSMYDKWs8ql5ZPOJl02Bkg_9xfH47BcYZNBvog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🔥
فورییییی از کارلو آنچلوتی:
نیمار کاملا بهبود یافته و آمادست تا 90 دقیقه برای برزیل بازی کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/Futball180TV/95567" target="_blank">📅 05:10 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95565">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/of05mGqhytEUjJ-5p-D3u23MsFVrTUjAm3lvV3p7sOP-3XpES3497NNYQq-ev-dkX0wxNcVUXzykwBHHka5nvh3EDKtKt3nvZRPHNLxHDqFOW_GVgaxDiQHWp_oQnjlKvRIiwDnKZwVEs6aozcHEgx6tHIHsDZwXXKguSghFc64eTeKY0o2AcIT53BRLClo6hww3ZI-rSeprUEEyQjrV3AyW79ESmc4ZhN9S8fqxttiYVL8NDXhNH2bbOwrvhweC4srHyOP2d3k5rHMr61bmyNXOCf5n0xAZ8rv0SZi6la9J-0WrOrXQQTYUCgTXKt07Ay5p1Fl5i7y0nsv6qcVngQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vVVIvSepcoT7PsEvGnnopGleJOhqkWqrmmcElb09aIMZbeJUB0YpLYuxiWRVOtEpKlKEaugXLqNoox8VV4DP-J5NnxKkXE-S8tUn8oZg0KsYxT6T7xnB73Z5d0mAgc3JouTn4f20_o2U5ZeAZAwzZFR6_G2hFVuG8AiZ6R3-ZbQ2GzbJGA_FwsoNZw9XJpWJjSmb-Xc-sHpzIJZVwCyhePl5_dqc0jAJwjlNR47ckhKWbV66EoMCvQ1DB-EBKQRCJAuLwaTPokrOGJIRexwje4MsBWw81aoJJlLB2xZKVqeJ0_8AJ9qrYJgakprRMJumqP3mm6NanNdKtlKUMZoeUQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇨🇴
🇨🇩
ترکیب کلمبیا و کنگو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/Futball180TV/95565" target="_blank">📅 05:08 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95564">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fwYOSqwdZBynj5w3who9CFKbpCHeB7qcQKpGsYb0C13lOVa9lB4BC2W9V7jtsZMbeSJAvvh9ILu838I67nfVb_YQwuILwNMsj_KVXLzUafCJfnlHvtVPSmjQ7kjGWIb5oWdPHAFILTE9F1Tb1JKM1jy1y12ODi_B2Leuxn48pT-JbTzOkK2vgyHoZDeGlGIghs8kQyhONbBD33Ae3sj9YulbwIcp0YvXl7vJ7uSnNI8pgs46AYrVbH9crycGz7DWNNUme7UK5KotbtT7OW-B1ANn1OGL821FuJNgdxop_bQDubm3myyMgf9jAcl5JXfrK_4_wqdWoXnyjFcm0ojPwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
📊
فقط ۴ تیم تاکنون در جام جهانی ۲۰۲۶ هیچ گلی دریافت نکرده‌اند:
🇬🇭
غنا - 0
🇦🇷
آرژانتین - 0
🇪🇸
اسپانیا - 0
🇲🇽
مکزیک - 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/Futball180TV/95564" target="_blank">📅 04:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95563">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NbUzEhlZUAZZY8bGfcDLxhTpZe9eVIRJA5p7pTTrs4lb5H7KV8iUiFMC9nADGvNEuJNZ0BG82zsCQXPOgp0IKxRtST5ohyE1ISGx4HH-PRBYZo8yfWQ3HQV7As3Mep76O7TZEk4MVEWnXjLDyFOYQxTTiLssJB8I4IpLrkkiAS0SSqZmz-ZHkFq6Kb1ykjJ8Yz4pKmr0DExjnHvSHfNj2wdEWT6MiBCZpG1UeTcLqFGE_0nJDdNDUaDfzL5wcPkFpMojRWfh01iRs_dADu8rzO66qMG0o2JaFtIFi0VfjYRpqnVRKbrWPi9sCsl9-i4V9CoLqqZYFxZyPdk4AgFhTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
❌
🏆
تیم‌های حذف شده از جام جهانی ۲۰۲۶ تاکنون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/Futball180TV/95563" target="_blank">📅 04:49 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95562">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oqc5yKRhUrXfbQwe9UXD5rd3tE5BNJ41McutOmKwemvAjnExKvfM2_ewN2SyPM-imGk7PQjggfK5Wsjq-6fjA2PUH479B9VClyCMB8bOmUJXIQ_vjjicNqlmwKxu8e7vGOjxlf5mlOHOjtvRiCeO3kx7GK7wlWXUhi6VeGJw8VK3pJXffSXT51mbLq4IgbicCEhpIJ3TEr-BrhkcqqWhTg2KxNOb6KtanFMGhx3p1o6UHk1bTDCO5RibuduX1QlcpGzaNgPo3NmmRVMcsKP74bQO1QwW1v8TSYu1CwrHAibgeDfVsw2V1iBWbiUEORqBhXIIJPQd2ZmJJEIYTyNRGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
جدول گروه L جام‌جهانی با صدرنشینی انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/Futball180TV/95562" target="_blank">📅 04:41 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95561">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YVoBbIGITMwa9_nkOh8_AMTF2J_xLjB1VVIltSqigUfUz9cmYhpQbVGSJGvyFH9uoaQNsoEy8CG3VD5VKEZINLEwFHXBDOE41sgTjEfNfh7ch-o_LpVgMTs3bt3yWf01vUisAhFnS-aDXvmEPjrACABFFi1vxYDoWGFN-lEBXnN9AsbdFrjSnA-sCVULWYRwodaD5pdq1LeiliEQkZ5wNMNIpTxhCvDauAj3QQY3zZsX03ObI4XhKyL7jsuQpXwXKlcqsi_HdSp13aTJ8h4Y8jc3tG79h2M8J8B0GwdNVSdT2flXIVKweAW0JP8G4xhXZn6AvwQewYJDoullEhCZSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | بای بای پاناما؛ زنده ماندن امید کروات‌ها به لطف تک گل بودیمیر
🇭🇷
کرواسی 1 -
🇵🇦
پاناما 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/Futball180TV/95561" target="_blank">📅 04:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95560">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54adb67650.mp4?token=BdlUNUyAyj0cZjQuNRI3EIGpqZoF4FWcw2KHk_9vj1y8O2Yp5g_4eEFrRpma5-IfdFJSSXf_BOj3siMPobzVkC7ND5NtuzXLpsSuVhL_Crgq9y-PAPIREijf33AFqAdnap2flv4RzznPvr44cRwmO8O1SXAYFbzqcAXTXitDnaf3W6N88RRq8VCB9HT56g3kbFTgxnbH-K8KQbE0sLFznIF-yYknI1WSvi3vtW2tXvbTAhUgfzZhNmeKCEJ1gfksKcDIvXgYK868dAsf3oQwmTvASBie88QW51CUzDHP3sY2YqFqt9d1eRtkGhJirTrM3HzwPo5h7LJrq1U8-QJL2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54adb67650.mp4?token=BdlUNUyAyj0cZjQuNRI3EIGpqZoF4FWcw2KHk_9vj1y8O2Yp5g_4eEFrRpma5-IfdFJSSXf_BOj3siMPobzVkC7ND5NtuzXLpsSuVhL_Crgq9y-PAPIREijf33AFqAdnap2flv4RzznPvr44cRwmO8O1SXAYFbzqcAXTXitDnaf3W6N88RRq8VCB9HT56g3kbFTgxnbH-K8KQbE0sLFznIF-yYknI1WSvi3vtW2tXvbTAhUgfzZhNmeKCEJ1gfksKcDIvXgYK868dAsf3oQwmTvASBie88QW51CUzDHP3sY2YqFqt9d1eRtkGhJirTrM3HzwPo5h7LJrq1U8-QJL2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بودیمیر به این شکل کون کرواسیو نجات داد و تک گل کرواسی به پاناما رو زد
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/Futball180TV/95560" target="_blank">📅 04:33 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95559">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kt47UDpcbwBB6m94yYlSVQIA_jGtvm0dma7pyBNbpyJSIlU-Txb9-KKiR81efF1LjfYRzZKolUILVXUQM5vO1t4antVUfsgQ1FHkMduG3HTp0Mn6dkyEcwyxbQxjeIV7gfPD_C49pZTboeOpY8NSqV3JvZqWonJF6gy2pYwfYvS-VVXdTx4WyesfU62pu6hUB0LXRUFkYdmeeLoHWG3vesRQwqAiUcRTmcbIlw7z6CPXrmWYhGoBGtyFvgTYTkmMQsQvePwEjSvVT1Dv-bHIOBnBou31UmxzwHGflHgeetXmxEMS-AAXtD_h5n11Mzy0aKhWw-ASQVP03UBfar_vjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رومانو:
جولیان آلوارز احساس میکند اتلتیکو مادرید به او خیانت کرده است.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/95559" target="_blank">📅 02:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95558">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ADMgJdezPKM2uorx5rw56sDe61ZFobrMEVWeFlZIxGl7pwuvXKi7vdVk_Cy6vV72aQx7p-wEub1BuehUkZdYCCBgvam_SqxBxKAsNHLbnzoDZD6I3-6sIPkjOTQFhqPnIek25daebb-l0P_wbOK7G2dPBuGRL7iqt6hIstU2KcvcX8UnTF3sSbEFQPIvbXgT1-JlmkHTP66-ZQ8vNIpBlQLi1bmsYIV7BF053cGe5CVBpAf8qwVP0lSL-hrekjhL4TWWOIPz8jizMkRtPXMWbe5qkja_6ox-smVuBhrBgaJS_91ijuCkaTdeELwTKlG6DajTpnBFtp_FOMtRGcKp_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
برونو فرناندز:
کریستیانو برای گل ها زندگی می کند و ما به او نیاز داریم که بیشتر گل بزند. او همیشه یک گلزن استثنایی بوده و همیشه تشنه گلزنی بوده است.
ما به مهاجمان خود خدمت می کنیم، نه فقط کریستیانو، اگرچه او سلاح اصلی ماست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/95558" target="_blank">📅 02:16 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95555">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WvAY1qSWQ_X5RyHdjqh7cHBQHO7MuieXg6HlJdZVUxOtOTF5HjuByai2xDs9UsypuxLBoQrjAjSHWBNliIZuUMVBk4VUysDN50EtRiIaF6-YZJn0N4_Hsx0ZRXF6haNBsKhCKcsoWqx7dZZL1ANIgrr4WVJCDDjKuWUibUK5CT1pp2vw49NTbqC2Y55rgZ2JodFm-gqjuknhXR3QOAO1oU6hx1YRk4umAgsSI_Fc1fJvSvrkzHtcGKGcKuzo-KzCfW_xa9Ki224YCnqUh-7kLYwHTCoPCHjQzqEnThja6OIh7PfB_jmpo849K-rvnPd4uoh5U9cJdV9h8CJMlyNOeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v25c4RS0KlYbxO_7Pl0e0nHvk1_NF7nm3ZyaFQ8EhmhU5Wb681GODtSCxoltrGw7l2_6Cne7NnmkXONM-t3VZcViz7zANT_4YFDwpel1gdwW8wv9fZUtUuPSPoV7LrYRS2rFnKgEwoUiKZoNTUWRNr6Tds908TaEgYdv8oBt2yCa8pviSE_T_dXNCM1_OWrR3BF54IHLl2ij_F8PKd5sOh7in0DCHw624JC215QvQBYgfvbSwnF89-UNYPULQ7fS-pFInGqarDS80PEydXiftetpYWtfbZr7rOnDyrQpaFVn0QrlSIt3-tYl11PfbHynH05oX58ROfgG18FNyMoj_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VK07ZaAksB2aKRWWm7vk6p6hwJPcwSRBItic_oD7zpm1k5vrMJi7ckrkOiE78NtlfVI8iy83S4ND7FzhmZ66PWDPpkCvgHilvq1RluC8KCo5HrYZqry9SIsNZp77rQd7iT6A_rSfhZXCv4l6_3hBhUvN2V-Hwu3PveK6qlKceYD13TNzlQhJgbaUSKUSiNLqWul1k2s2JGdoyHMWYj6Mof6ZK9YwLJOi79CFoQJN-lFQMxMkZGwWVerxRZLjwXJc7UrpfaEXOGIlsTgOAr21fp0G5j9gjLFjwR45BdgkAvOLkr4BQTIqsE_kBJ8I2wg3pqPcB_P0oLv52vUP79a9Gw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بانو ایوانا برای حمایت از کرواسی تو ورزشگاه حضور داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/95555" target="_blank">📅 02:05 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95554">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dfd384cab.mp4?token=KSP-TafQD81zt9PJ_1S-2bTJW5njkrjnQrlYvUp0Z49lPvq20Ta4S8Z2Ul3JNns8cohp4AN_4Zbe1SOde6NiCIxfz-ElK3Vk99to0SH5Xp5cOCsa_uEHKyO0fDy95XuDuMFBL7LSW-_jBnhgiZ3n28h1CurqaQJ2ZT_Ms4MVme9zV378wU0NidTfrd0BLS0pgNzAS84hqaBSxuhWoMHF4Tk2-bw7EPu1N2v82Xm10Bw6EJf4usZz-50Rl4KNXe7OlAvbeGadkZyff1_kUWOKB96PpCJ5XJ3BW2OFzm_MYIc16KOxDY-bElfOFDk7ruLSoIpA2fQ-aikFqVQV-8TnLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dfd384cab.mp4?token=KSP-TafQD81zt9PJ_1S-2bTJW5njkrjnQrlYvUp0Z49lPvq20Ta4S8Z2Ul3JNns8cohp4AN_4Zbe1SOde6NiCIxfz-ElK3Vk99to0SH5Xp5cOCsa_uEHKyO0fDy95XuDuMFBL7LSW-_jBnhgiZ3n28h1CurqaQJ2ZT_Ms4MVme9zV378wU0NidTfrd0BLS0pgNzAS84hqaBSxuhWoMHF4Tk2-bw7EPu1N2v82Xm10Bw6EJf4usZz-50Rl4KNXe7OlAvbeGadkZyff1_kUWOKB96PpCJ5XJ3BW2OFzm_MYIc16KOxDY-bElfOFDk7ruLSoIpA2fQ-aikFqVQV-8TnLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انگلیس در مقابل غنا 78.8% مالکیت توپ رو ثبت کرد
این بالاترین میزان مالکیت توپ ثبت شده (از سال 1966) توسط تیمی در یک مسابقه جام جهانی بدون زدن گل است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/95554" target="_blank">📅 01:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95553">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ht71tNAX93OuXnW7c3vf47DSE05k901ipGR2j2YODNwNSiljWt3-OAdAlgUeVXIXIOc5Y_Tf88HNjSl6J8U9UUZYnPlDgMx65HP5IZkze89gC7Ifi7L_-i3BlyNY7TGJxi7Fwm4Cbrbu_TJxrMBuc1K9qlZ1hdDcOpAf0noQN3W_uHfWrz-WcM-0tzW-zebL-eXhgaOT7hHMrmZ27Wtsu5407NOCFkzPtlGp1pVIrKMiw3sMOWCG5akGREIBs_d107F5RyCiE6XeBxCFZvrMnTUkEyWc_vdLsl7mT857W2KqiyZszFVzhQPcJ6iAcS3cUawW28BwyK5DwXzp8yjY4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیونل مسی 39 ساله شد
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/95553" target="_blank">📅 01:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95552">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/95552" target="_blank">📅 01:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95551">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FzANFafTIxgAci-UUqkHYdxraUvRbi94Y-eMKpRu2b7uzTD11ShXf3KJyBMWuUWADvJQddertoFqwM7fstWCsUxsjqKkjHcdEPUUCkNB2XCoeojp5os_vdG5QEPWHtXfI4b82K2_8cDpx2Oj-9oSUThhJ6uCrvUC7oXbI7YEKw1Pj4VZcFyqNT-tiagGJMgNFVflp96ZWaSf8lq2bB_ZeKshindX5JdAUVI7JE425b4plbEZhwKkS1IOYI0z2-0Mw_oypy8n23T8pnMUpaVYAjTkZY05wBg_zIe0k1A1BCFozRxLdRDKPw8WaBoBlPZBq6coSuW1VaCm8tnjooxMgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/95551" target="_blank">📅 01:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95550">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qxpTSgPr6pMEu7qHvnB3hD-IgICIQDWPdfDUZ4IVoB1WG_AgkVDHztMV_-w3LpMvXMmQmNrsDj-nOZGSDU1mSe3OQ0ni51JyqyqXl7LR2aNx10RtY1tz4B-iYT80TrkZvUi6bdtgD_bQknILPZLfo5RY2da6iHvTTbM5XPl97zthXVVpbYZxu57P76BA3NqR0XghcWQ5ED-NezCR5dUDYA0fxVrdd2JJ45meSr_Fiw2cRIgO6XGlNK4Zz15FNzdjWS_7xEs8tu0GX-DMP69cX5-fGPCILaXudOZNLn_CxMdg3aB4X2_rf4_HaVSljGVMzurYHyK3f9qb--hu40K1Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جود بلینگهام بهترین بازیکن زمین شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/95550" target="_blank">📅 01:36 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95549">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oB8Z0Zf2jbzFT2MMotdtqn4bbi96W-3CqVLqVMgi9SGANxTf5s59app2ccir0wHdqThEHADgXvs-Opqjl46GVh7H5VVESzMJ_zGEAtmlL9FgFVGEgeLKNrILnOcoFxyww5MkpmasAmqxzHdklfuZLfCRHLsDTyFe9m4rqV9lFIHwh4iqAErsv4Bo7a5l2rPGmIeIYF-jY_5WtTNBxL7HzFlaafEn1wimFexkFlKGVnT-liYiH0Kqvudhd80th5LiQupoBODZA66k2XsKLuhSquUkzR4tALz8eYZFp-0CYF9zTaFeL7tTPfJZmDRbPtHctOcu4rR6ps7rghT2uxbAjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | شاگردان کی‌روش با اتوبوس از حریف قدرتمند خود امتیاز گرفتند
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس 0 -
🇬🇭
غنا 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/95549" target="_blank">📅 01:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95548">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qGAhZlJZPTZfvaugDM101fmTaxomgKQSHCddI_P0tBbaRX_SAfV_eWM1Ltwpx49RptqazoiKxSrygdimF_cY5q8l0H8Ct_7afSGeq09btburur2q0mXGAVp3RjTPhU2Z29pv6WSTHdHuvlN87I9a-FWLcKLZW7Vp2sqcK9SwDh_5EBmYw1_wEAWSdat0lADV7I-NlDCUQwsXEWWexm5_RjEn6IsUQbW6xAgK9ZEZX93ISdMShwnQ5U9VIXEhNJ_apxzv50HnyXIL8FIlXSPyfqzsyHjTKAE43Rcs6lPVaWsJBmzSm2aUUdXjseBjfC6iSCU-gM6hOMT_6UutLOlAsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
موقعیتی که کین نزد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/95548" target="_blank">📅 01:21 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95547">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">چجوری این توپارو انگلیس گل نکرد</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/95547" target="_blank">📅 01:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95546">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">پشمام غنا چی رو گل نکرد</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/95546" target="_blank">📅 01:12 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95545">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O9eapAmK50IXIRQ08SucyIbfby9d_DocN1_D364AmRztcL69PYH8-tmiv0pPGQPVAfTJ1FRT9WkpXqGGpISAXBr3gGB70bsJY-VvwMUDFc3QDYRXd2bPBYQ1lBm73vpDsflwsbPEkVH1qJOFUhb3ODG-QFxaY2gbhkO1i-xTt9o4vqSyz1EO2motgLEKJfybIo6YdAjd4SVzQwSd9KiW5rHfnR9CvTiR7I3e6C6iOGjLoe3mcIIRTXcKGhrB5eCjrKwMDmgPxGqv8X8wuIYJ7by_cHiA55Qq2GZTa1V_nvOd03G6jp1fsVVuCHzFizp9pXPMJdMXfJFuz7F4bAdlKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇦
🇭🇷
ترکیب پاناما و کرواسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/95545" target="_blank">📅 01:07 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95544">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-jHyuSodp1V91iVtKzCV1l0youcNw1B97jbTeyDiC7J3sIthTYtN8o4_lzHy3kZ_GL02tqkjRb6PtZwAyKAdTv_t4mr2rtZKmajW6pQ4u4cIFvRq6Kp5mQjbaYtRpz5xnV6lMTWg_aRgIsWILQGtzrsdQcQiOiA-Ppea2m2vOp7miMVm5yFpvqsURTe1eZBRp157eIQXAVtGFsFNzxTBdWcrHOnJE0ds3KVvq9641pdgy_wDQkNi2gJXH7_VYF4PtmfjbvC1Ubs60roXDXB6DM8YWLU4nomJk2MF5IiQxGbdX_aT9K55Bv_X0m_UMiSYKtcdsXUKtGPkMHnpw5iFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کی‌روش داره حرامبال رو به بقیه یاد میده</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/95544" target="_blank">📅 01:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95543">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caad3dc61a.mp4?token=Hose1c3OtbWt_6UgqFkTZgFKbI-4ZDxYh7HCPniAg-gg82R9Jb98sOeAXcDRfiNia22-MOOISdBECKJnvWYDDdqXMfnpsC91mpbR8r8zv30duSgnLdsKJPS0v5NnIGD0eXF_wsCVloDGvah4Koxpnwahxbko-K2jrdqEBzRct5ec0tXb_kWs97Tcrko_XMZSD-rW2yn66m591QsHMkSVqApjg18fuslJ6Xdoqt_wRfm6M0IBJmIyKQQYQl6rACoUJs7xocI0SP0SM6XZtW-p5RLGk75Xh-LA1epFliYE3cm1pIJ5zpLr2tG0G-prnHM-DksdO_pr7ukGIxiMXH8gmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caad3dc61a.mp4?token=Hose1c3OtbWt_6UgqFkTZgFKbI-4ZDxYh7HCPniAg-gg82R9Jb98sOeAXcDRfiNia22-MOOISdBECKJnvWYDDdqXMfnpsC91mpbR8r8zv30duSgnLdsKJPS0v5NnIGD0eXF_wsCVloDGvah4Koxpnwahxbko-K2jrdqEBzRct5ec0tXb_kWs97Tcrko_XMZSD-rW2yn66m591QsHMkSVqApjg18fuslJ6Xdoqt_wRfm6M0IBJmIyKQQYQl6rACoUJs7xocI0SP0SM6XZtW-p5RLGk75Xh-LA1epFliYE3cm1pIJ5zpLr2tG0G-prnHM-DksdO_pr7ukGIxiMXH8gmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🔥
رونالدو بعد از دبل مقابل ازبکستان:
"یه جوری رفتار می‌کردن که انگار من دیگه از فوتبال خداحافظی کردم و تموم شدم! اما من تحمل کردم، مثل همیشه؛ چون من بیشتر از هر چیزی به کار و تلاش اعتقاد دارم. سخت بود، باید بهش اعتراف کنم، اما خب... ما دوباره برگشتیم!"
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/95543" target="_blank">📅 01:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95542">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">غنا چه دفاعی میکنه</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/95542" target="_blank">📅 00:51 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95541">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">بریم واسه نیمه دوم بازی</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/95541" target="_blank">📅 00:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95540">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i3indWf14tjegEkJgdI3r05o2-dvpAdU4l2hVsRMd4ZUFjoWzbFsuZGZRFhj-mGFazTsX3ZmKoJtHKNPix6vQK-vCk0Ap1LcJHzfG8U_yc13-cjSsCEPSrlf5ciGjzNoht_RmZYsnDS0KAuQgt_1ASamd-ycftayeQ1-6rbaWkwz8rKqeJ66-McaWP7pogZvI1uWjGAR9FiTZReOXUIRMRXfrOnd8YLIC2r5bGbvF6oFR-MviDEdQEjCLgkmULh7fMSCK-g1EfoiYwEt6BCGgu5dZagWQIzMKNE5QGBbdvXQRTbanT3m7O7L1Ibcw3A9U1ioq32MECcbR_K4yPnCBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دالوت تو اینستا : عین بچه‌ها میخنده
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/95540" target="_blank">📅 00:37 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95539">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B3D5o_BXAfbKUUgQbwP0F8YRH8PdgZXvmqp3AfmtjKafthNZrGfDHzTGvvYh8BPRjfGkoP5FZw0pH4hcAcPavhSrBb0E19bWYQAFXdq0KdUg-SEo87v8ZYWaPrw7vZcstDCbvZBs7518i5id6X2XZulFWZXiEfIG0qzce3UbsMe_d0Nj8O-uECuGu9rfa3crDiL8Mc0PXDdH91Bs26TxeISC8JrErW3CJ5m49Utw4HKvq3oIAsalSwrxECog-hBP331I8_kBH2Co01SPyXWSYTTFAz_EAv1tUM5PVGQvbEDzEn2IgC-9sxQUR28C4pRiqpDjTEz_R-ppuRJeo-WeKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیونل مسی 39 ساله شد
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/95539" target="_blank">📅 00:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95538">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">پایان نیمه اول
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس 0 -
🇬🇭
غنا 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/95538" target="_blank">📅 00:21 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95537">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f5DsCaonoV04zXYJorBrAxn_kpvhasRf1ONK5f5mP1hsN1MRmjd_3UaZI2AxdnGXiwc3fWRfHRoZBgWKun4sl_TY6_EKanKW2qUy-BqiMVbW2GaXpr0TAfCthuqlydE7bjVZ4F5-aNNhW3gC3jIJ6rKasvBdJBtDt7N8ICsJxAp-yfZGg8O3Dcw7kBOn-Rdv_jrOSd0IzopGqR0YgSIB9qr589-egc3tGCS11IFyqDWslXSsySX-f1T61bDEyG2DQU--eYUZESoVh8FKmf0TKaCQGNyFV7Afs5gXiFDN7rmnvAu4RlZySpXSjJiG5CJMbxgZNbjmR-ackY8cZmWKSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیوید بکهام تو ورزشگاه حضور داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/95537" target="_blank">📅 00:14 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95536">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TQaRpyxsrZaJ4KFlFl9I2gAiZbmp-GIbmWusgZSY0F3wcduvHTJBcW_Jti_76uNPQlQM-OY2uLA-PFGWLoXMibQGijiVOIDXEWdeLAK-4aKfzWfjM3ZjIwvgrXLZAjrW6SN73Wp1U_cC0rtItTAEXyO-I58Rl73vcIH5cSrkbCKO7IOprYAYzKHw8wMEbNyvc9Cb1OgypsojYtK4yf3tzpMax-nntAOu9JGXbgtbqQYQz6MYMjKwM7BEIMgvn3nTDoWcZGEi0ADtoM7QWduG-z7IqDHxj8WEKXRvlKPPce8PjT5doQGuCybEu0DaWJLtOr6M6pkdGYCTqczwYZDgzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
🏆
نظرت راجب گلزنی لیونل‌مسی چیه؟
🎙
‼️
رونالدو: تو جام‌جهانی هالند‌ و امباپه هم گلزنی کردن! چرا سوالی از اینا نمیپرسید؟!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/95536" target="_blank">📅 00:12 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95535">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">شجاع خلیل‌زاده: اگر بازی‌های تدارکاتی خوبی برگزار می‌کردیم، قطعا نیوزیلند را می‌بردیم/ امیدوارم در آخر دشمن شاد نشویم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/95535" target="_blank">📅 00:10 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95534">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/095322bde5.mp4?token=umEBSrn8ro-1-n2B-aLmXlr5iA5E0ki3WKATzeDN8KkTcu9W-_-6vVSlGo_ZHModNN5_B6nh7If8LCRJLQnoPw6ZMGtWzegiG1avIVYR_80-frU03ABKR5Utu-3e0evAtik3xRc_4EPYpiEocAgc-hk-KeQzkXcNCiNyGbeCoYwHAqZdFKcVNT82T-fOx8bMFQVQe_owwUwWsTVraosrXhb2CM6MtoL0TyMZfZmbrjlymVbqafsB0EDsg5KFICudCjyfe9sh-GU2tYsKwMRTrFFZR3q_fZAitA9D7FkCJECgl299zi0RxUQU_hmq7o7iirasJaJfkhVsYkc46zsivw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/095322bde5.mp4?token=umEBSrn8ro-1-n2B-aLmXlr5iA5E0ki3WKATzeDN8KkTcu9W-_-6vVSlGo_ZHModNN5_B6nh7If8LCRJLQnoPw6ZMGtWzegiG1avIVYR_80-frU03ABKR5Utu-3e0evAtik3xRc_4EPYpiEocAgc-hk-KeQzkXcNCiNyGbeCoYwHAqZdFKcVNT82T-fOx8bMFQVQe_owwUwWsTVraosrXhb2CM6MtoL0TyMZfZmbrjlymVbqafsB0EDsg5KFICudCjyfe9sh-GU2tYsKwMRTrFFZR3q_fZAitA9D7FkCJECgl299zi0RxUQU_hmq7o7iirasJaJfkhVsYkc46zsivw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل‌زاده: اگر مقابل مصر نتیجه نگیریم فایده‌ای ندارد و مثل جام‌های جهانی قبلی باید برگردیم/ بازی با مصر خیلی سخت‌تر از بازی با بلژیک است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/95534" target="_blank">📅 00:10 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95533">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EGCETlgI66acSGC_L6GU39smG6XCY3Tm5kF6MESxtgn89Usm8sOHRl4tAdqqfDaxj6S5JpUrWTAFIObDpf_pTDe3D7i90uZp1LPjt9z-GjzqHZuDyh1P255lfF3zA42_zDzynhiV4NN45TeB3humGGk2Qzm4ALBXQsaw6kVFKVjp6snTkz1DW1mVtnkboQ80tjYJw_oN5vYnNEP-bxVZx-DGdnpeTN3Kcj2LFPlU-o1v-zdnKfMhEZzrcIB4dBdpJzC1XtlcHm3LiwDCeYCo-9mw5FoXyld2QZdEWpj-mGEWj6s1vclUC-KwMzHGGpAc7nhg3MzK9KSY6YJV_uUejQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
🔵
همسر رافینیا درباره شایعات مشکلات مالی این بازیکن و احتمال پذیرش پیشنهاد نجومی الهلال
:
راستش اگه بخوام صادق باشم باید بگم اگه حتی ۱ درصد درآمد فعلی رافینیا رو داشته باشید به راحتی جزو طبقه ثروتمند هستید. خانواده ما یک جت شخصی، چندین آپارتمان لوکس در سراسر نقاط اروپا و برزیل داره و فکر نمیکنم این موارد به منزله مشکلات مالی باشه. امیدوارم رسانه‌ها برای فشار به ما حرفای خنده دار و مسخره نزنن چون دلقک فضای مجازی میشن
﻿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/95533" target="_blank">📅 00:01 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95532">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">کی‌روش داره حرامبال رو به بقیه یاد میده</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/95532" target="_blank">📅 23:48 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95531">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Igx3J0p934dtAGRVqquj0ajkguuUoPSSC9E-Nyx9MBGx1DS1NPwBIgg_M4MzDrJIT08ZKM6J9YF7KsL7SkLXQFM0i_Lp5ms9QyM-P5ldl6fSK4mywAE81VHhSyTzIm057o_iG_RJC7IcO6I27mG0Ci9ywig9DNBFeH35UAQ6SVvw7OWxXCXRzxCaNYqL1lzpM6IzMe6QM2-_DXIE-MXrA-Q8uerSnVJFgJFJYQ_SXbSAhOtDxkGLnOAkUZ9o50Zuj5Fwk19oJ9-9DwzUxKY2btgpr8vmfFYLG2DuOylkE25jVIamLzS_mSwUAM6t_6lp38tI3VKCeNZOjHxPv-Z8ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بلینگهام با 22 سال و 359 روز سن، جوان‌ترین بازیکنی شد که به 50 بازی ملی برای انگلیس میرسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/95531" target="_blank">📅 23:46 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95530">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">بریم واسه بازی انگلیس و غنا</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/95530" target="_blank">📅 23:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95529">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vgFYl3ZBBX6J8zVDdNkmUwf7knc3P2-X1BM8WWmvMxvhWFHWfC2yalZ3u7zGLWaAwHnVqUPTUFkNJ3vkUu6npCFgaqr9NeSJ-_JOw7riNmC7EzAfBhsYJBaDbDChOKj4KzRXhbaTdiADTSi5GMY6c3O5le-bR2nwxS9_RTJbCB8vkSnaGJxYgBqrwCq1FPgRfFFsrNYGec37iG-RWw8wyYeF_55ykRjSJNI-q1NrwC0vlvDjKk64UHsjVnrFkCoV1uFPJSxt5cFgK1tDi6jtNt9hR2ukzrG5Ha6HTL0UFERQF9V67CjfXH0hWPHK_jN-V30L_DVYeLoQOgx4vDfeTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
مادر دیدیه دشان فوت کرد و اون بازی بعد با نروژ رو از دست میده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/95529" target="_blank">📅 23:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95528">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Je6tgvO9fcWjidZeqvn7kUJ3tndwWzFYT2QeFDiR6xKmr2Rqu05Rvs6vXVg8wI2Lwj_5ArAKAut1JMR2a4iHSl4aEfXFE5CwehtUTmkOpKmqtZu8yWHHUnxHvuzdwd_aCAp_rAMaoSIYqbpeE7VdT0U5dWtFOo8Ao3rLq7gCiIuhKkzMzCI5lJfOegerZjY8zNEsJdxRjTAR_SPYVz_9Pkhu4N_fv_0PQIQ0jqc0iGpYcXBAySc2KQ8hw0arRzrwPrDMKBakDjp_9werHpfWubg3ZNzP708iOqueZEJa7SehT1S1Pn_O3L4Fq6MyZseOtTQE3Sn1dQ9RbgBkGe5wSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
کریستیانو رونالدو پس از بازی:  "ما برگشته‌ایم".
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/95528" target="_blank">📅 23:08 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95527">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d5f913d17.mp4?token=XHxVpML2rRRcS6ecK43L4SGDi5Q7Pp4l-eZPRQC2bN_i2xXU7R-Eoxwv0i-yMyFRlK_Z9Ik7xvVEgx-xBSHW_2NxfDPkP5xVvnNhcOQcNpTfKI7p5VYJXtT49O6KOVsmMBEdAEnmJtZTSienjvgGlqD-SXQ3Tss2dAfK-C8CY2Rj8KP2eODDVhJ9lA4kj7fApNs6fyq86jl71sh2vctMG2nNgOX8k60EDg86qERZ7L5TC7P50HbMKkk6H-S0XKudVMCP2l3_i61ZY8HSuDIyFXTtl5CcjrCqPzDRlC0jq9-YocMkdXZwJj1gyNaYZcChvyhVzB5_iZ7XDyAeKZmGMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d5f913d17.mp4?token=XHxVpML2rRRcS6ecK43L4SGDi5Q7Pp4l-eZPRQC2bN_i2xXU7R-Eoxwv0i-yMyFRlK_Z9Ik7xvVEgx-xBSHW_2NxfDPkP5xVvnNhcOQcNpTfKI7p5VYJXtT49O6KOVsmMBEdAEnmJtZTSienjvgGlqD-SXQ3Tss2dAfK-C8CY2Rj8KP2eODDVhJ9lA4kj7fApNs6fyq86jl71sh2vctMG2nNgOX8k60EDg86qERZ7L5TC7P50HbMKkk6H-S0XKudVMCP2l3_i61ZY8HSuDIyFXTtl5CcjrCqPzDRlC0jq9-YocMkdXZwJj1gyNaYZcChvyhVzB5_iZ7XDyAeKZmGMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
😐
ثبت قاب ناب این هوادار از صاعقه عجیب و غریب در بازی بامداد امروز فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/95527" target="_blank">📅 23:05 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95526">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/36a825c4c0.mp4?token=ZE8A0WPFFB3gOYGRCO9XHLquT-aecx6XCC8j0A7AQ6Ks7KgaREUi8xbNboHRlB0EdRi7afuhycKNZ_oLp2Zgqg6Y4YlZiKYKz9m40aCF1lXnJuDsdpuw_UU9FrIJz2LGpW9uPiOtlNx0Qb_cPm_AWCQ9Y-OYrjX8lQezqDfgrQElIyL-IYmJk14dJNt0R3Msy8xvYzgMRZSqoxAIzQ5vbSD-RuQXYSjGMUkfX7ljzt5uVIBobonyk7RZy4c-h_0c9HHcKb43R3sGhZ9qBQFBKOaHh92S8jUWNF-U2zRM5jKdipK6QhtZEdxFfbJF0Av6bQcIwrTZm7q59XVxD65nqEAjG82KouxmNKK7Upwn-7usCesud5YUqzl76Do9_7hGzOMrzTIgM9I4v5wyYV8vWpN-9S-KTA_f96Dfvyrb6F1V1RgbTGbudioMpCnMNOqM53N3c2HqMqSmfjxcqc595qjuehR9mAwkCIJih7Plyf19W9ce4J9Iu6BgT6zkF371h1RgPGU5dqOltlWCuOAVt5lxCWH-9PpldwtJD1Ky_06qKG5pCq4Ea_nQ03iOCSE0gvFmeiDfqcOOYHbbIOhrXsZX4d0QrBO46OakRm7I2oe8gQMqYkHIkPf12hiCbcFk5bJOD36A_iWeKrGGf-InkEznvOeuN3FDMtERJNtraMg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/36a825c4c0.mp4?token=ZE8A0WPFFB3gOYGRCO9XHLquT-aecx6XCC8j0A7AQ6Ks7KgaREUi8xbNboHRlB0EdRi7afuhycKNZ_oLp2Zgqg6Y4YlZiKYKz9m40aCF1lXnJuDsdpuw_UU9FrIJz2LGpW9uPiOtlNx0Qb_cPm_AWCQ9Y-OYrjX8lQezqDfgrQElIyL-IYmJk14dJNt0R3Msy8xvYzgMRZSqoxAIzQ5vbSD-RuQXYSjGMUkfX7ljzt5uVIBobonyk7RZy4c-h_0c9HHcKb43R3sGhZ9qBQFBKOaHh92S8jUWNF-U2zRM5jKdipK6QhtZEdxFfbJF0Av6bQcIwrTZm7q59XVxD65nqEAjG82KouxmNKK7Upwn-7usCesud5YUqzl76Do9_7hGzOMrzTIgM9I4v5wyYV8vWpN-9S-KTA_f96Dfvyrb6F1V1RgbTGbudioMpCnMNOqM53N3c2HqMqSmfjxcqc595qjuehR9mAwkCIJih7Plyf19W9ce4J9Iu6BgT6zkF371h1RgPGU5dqOltlWCuOAVt5lxCWH-9PpldwtJD1Ky_06qKG5pCq4Ea_nQ03iOCSE0gvFmeiDfqcOOYHbbIOhrXsZX4d0QrBO46OakRm7I2oe8gQMqYkHIkPf12hiCbcFk5bJOD36A_iWeKrGGf-InkEznvOeuN3FDMtERJNtraMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله تند سعید اخباری، سرمربی چادرملو به پرسپولیس: سهمیه آسیایی حق تیم ما بود/ باید با تیمی بازی کنیم که از ما امتیاز کمتری داشت و سه هفته است در حال تمرین است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/95526" target="_blank">📅 23:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95525">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HeMrGAfIwFyiC2qHysLRBKc_hFk4rOZLwjdrA180Nfx515PpYWaiMvlpoZOuFWq3fygKjDeJhkm3yARO2vcHbmVwr17c9hXd6DqjS3ul73-pGK8aigNP6uPy5kn-bffnE0UdSBzu44QJJTGRCMPMxsskagbfs5f4CJ5sdSgReuzWm6geGYskGQZd0O6-MfB4hnLjnDiQP7RHrUoM4mBvNVOt5U5eaEylwyCf2egSSQDdDsFOds0HyH7UFM66MKSAavjn213o0qy88sUq2YnMVP4J7d_Gy2r_5kfYbLkWHyiZHRMiWzbtVZQ7ERbHfeIvemy0WYE-MNAVk3C05Ni0zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کریستیانو رونالدو: شایعات از بیرون پخش میشود، اما در داخل ما متحد و یک تیم هستیم.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/95525" target="_blank">📅 22:53 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95524">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FD7u3JdI9mcJNofAq27BooI28jJZGNgthJQW0P_pF59BV2gNTGI5WNuSntnoiNosjJIsjqnw8DWBIbeHZvGwSj7br1vCwZ0Bmh2Bywl4frcVF0VTQsOmLjsuU2JCwZQvsji5Q9z-Up2PbmVVL3_DD_owrnaqN2fyKTqpbdWL0Vt0Blb1QAdoBbnKf05Iid9iFN60_OOCyoqhKKoMANeR7J8bKdwnlvx032OGtBKEDHTMEaKPp1sf8EW4VCahLwiH2qixACgjKKJHxeS35CHs0fim0wP3KKxdG0uY0AGx9r_gUT_RlXqwChO1bVm9zz_GeE_MvEN3HluZttncBd2QFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کریستیانو رونالدو:
شایعات از بیرون پخش میشود، اما در داخل ما متحد و یک تیم هستیم.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/95524" target="_blank">📅 22:49 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95523">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B_-4uUqIHwmkXYPc4FyZwa-iHAAfVob5_vMBq5_3bGWiII_6Dn1kJyUrV6wPpSwTk5ZkxH__G7VUZnuT0g2xFJlTiwPvuhue9JpSE55lvdH5Ms3MjAh3CN_xRl_2qcuY5vG7V5UvYlofwsAq8f_mRgzWc5xN_T1uAFROcZBA2EGIbPxfWDyp_-x8SdocrjUNuJ_Y1KKakr4sULHTmoZ5Qpw0IMehF1RpxIKlrbyhICyo0yoir5JGXhItKzWAcr-jObPn-3A35hiuZX6XTWrtf96T3pVBrTR-fXA9OmVIdiaPp6ChwybWCXkMYWnd8V1UWZ8GJTI4OtQjSkLG5sEmtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فارغ از تمام کری‌ها؛ خوشحالیم که تو دوران شما زندگی میکنیم و پرایم‌تون رو دیدیم.
👑
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/95523" target="_blank">📅 22:48 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95522">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
🇪🇸
#فوری؛ اتلتیکومادرید به آلوارز گفته حتی اگه کل فصل بهت بازی ندیم، نمیذاریم به بارسا بری. تنها شانس رفتنت به انگلیس و آرسناله که خود بازیکن کلا رد کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/95522" target="_blank">📅 22:46 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95521">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇵🇹
رونالدو بهترین بازیکن زمین شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/95521" target="_blank">📅 22:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95520">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bR6my208vS2jkhaHeX8xJO7jKMKkgxEyFK_A8XN-bo_HnjAZNbv-e_71Sau3VPy0gattyYWiHjraPKI8WQnmzKJ_-ZQ0y5Y5c8dLst36J8fR3JzdtQHDIWgX1GOzc0SUB5SekQqgroEGjBY2LMsIGCyJDRl74wRPjiFRvURsGtOpfCA_8ME0ImdIOZdpGJQKf35Gd9JIWPNy3tWmG2QVFtWYa_WUjoy2zglJ5q5UYD69Pgk8Jp_qQC7NVM596-kZe9p4Akmf3u7W3J2yCVUBv2cYZPtKT7ehAOMyMgsWZcYynMc1i1K0ry2zu0GNOskeRgYA-ydNky5UA5Qiju1XCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
کریستیانو رونالدو پس از بازی:
"ما برگشته‌ایم".
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/95520" target="_blank">📅 22:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95519">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🏆
پایان‌بازی|تحقیر ازبک‌ها و برتری مطلق پرتغالی‌ها در شب دبل رونالدو.
🇵🇹
پرتغال
😄
-
😏
ازبکستان
🇺🇿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/95519" target="_blank">📅 22:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95518">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s9gAzm26D16_yNV3xDNK67zDGBuq3VerCMO-aP26AeZLwIkZKUrrMrKpa5tT8IHMlYRDcFz9-rUMQvJJs4JC10K0onyE69q9ZEFasQ3rkSaOFRAzcUCJnJ3wdG-dX5_7BeVaJ_Oep6XPi_A3OGckfVrQXSyyigtI5MSEvH5k3i9KJP7VrhwhNNwkXVSXbaQd0Rc0jkNPi7MJja0EmhkwlpjYSYxNBWYv_5l4eLI7wuUvitUljev6ZdWkiII0UQCuQJACqafHJysT3riwELLpz9ynGFoP_420zN3bIDC5or9FEkVO_tnL10xShCAPdl14BEp3Ebj9IAbFIpB3ZlhlKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
رونالدو بهترین بازیکن زمین شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/95518" target="_blank">📅 22:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95517">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T8aI7fOrCFTULtLqbhshmO5AdJCFZBVTLc78hBkhgdBO5b5GeUu5mYPhO-yFO01ASEe8-SQeSRU1FHHJYyNL552KT3TopeuPB1dhW6cXbO_sbDWDaeMdFTLZz0iyOiMb9AaGEyoU9G5fFplFoN-6Z_1iSJaO0jb0yfbl11C8ELLIBkkHXT1juIspDgW8XwqUWpfk1PebHAifuZj8V7VPZwpkkytl9py90RP0tzqU_yAGtMMuJvcYjsyhtp5aXM0w3ThGK394dwyDG8hYfQX-8TE0TV4JsjkIxXrys2nzJPP26QMYJ35I_Fg72s_riGKQyrdiVumsBKDMREIskJY5wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی|تحقیر ازبک‌ها و برتری مطلق پرتغالی‌ها در شب دبل رونالدو.
🇵🇹
پرتغال
😄
-
😏
ازبکستان
🇺🇿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/95517" target="_blank">📅 22:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95516">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">وااای کریس چیوووو نزد</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/95516" target="_blank">📅 22:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95515">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🇵🇹
گل پنجم پرتغال به ازبکستان توسط لیائو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/95515" target="_blank">📅 22:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95514">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">پنجمیییییی</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/95514" target="_blank">📅 22:21 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95513">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">لیائوووووووووو</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/95513" target="_blank">📅 22:21 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95512">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">گگگگگلللللل</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/95512" target="_blank">📅 22:21 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95510">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TI1Wjwd5Y3qExBknit-E5hN0cLLVmINWWUjFt_HyDfxPlYSou7WOMCGnaeF07ylqRFxK44x2gwSnjpn1gCCnk2eDQ-cF40PSob1nCoTBDSURj6gKroc-cPlnc2CG5r8XcRLEKO5ALA5XVk4fldd5AQ1E0slxtQ_Vn7F_yGgUwk12N1BsAKXiUQdd8KocrXVigRzuyTu9mpV2L4oxL0TsxqFKYlS6yWShoNQ39OSs4oaGNzWNPjt3zm_ug9C5bEam6ESga0_fZiyXft66mUxBhKp-d2TJUS9YIabbk7pTGmTG1r7BumHNVCi9RMX4U973KkiVBODdg7m9xkH1cAGC6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h3q48KibmGpHOSN9bTDsb7Rxh3WdKvMeAp1x4SERWr99kxkJTp10CZ09dlLuLJ2KC0f0_TcPtZ4GzNMnCo4wtRG6VPq4VqMaunchncBApUMCTy04UhUWYLdXQ019RgpgwPaXOzKfR3FAbWtvMOOhVgr35myqApejaNB3U47ESHds5jQfF0mXpoAXVA6L1oITlWMscG1sI0bJYWIj5YhPWCvoiNUeowceQ3G6j8BjxrMKwA1QOpOS4M7_rz9C6LZZSHLDdZZF96P3qHaORAHFJGCMXX0pvzBfrAohYsBW6qpj99BOhmBDfOG1Pi2UWejapEXvzr2pBlCaBc1KRC6vHg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇬🇭
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ترکیب انگلیس و غنا مقابل هم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/95510" target="_blank">📅 22:14 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95509">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">نزدیک بود خییلییی</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/95509" target="_blank">📅 22:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95508">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">نزدیک بود رونالدو هتریک کنه</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/95508" target="_blank">📅 22:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95505">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V_5NLlCQTUtv1i3ksO15NNypYwBQ1X7J7kBodp_Ik7YXOQHyvJTDvHpjYYpQy2e1PLpaMiuBr-v-i2EfhYHR_eMSx13lKe67pXjvKm_1--ajaZ1O5Ar9Bq5b3Y1PaJB9WQXf3feKROR6iWUUN0z0YDrucdF_t52tHibBCCm-LNirz6ohgbr0VAKL9xOfAawPlXpgl9XyMvTo1CFHvaQlTxJaY24uyaGOk3ym_9PPPyXb_k05XbfsQjkVQ33lkGIbEvXes0hL7QcX6WGu7e5YyfdCr96tgOOA6s9H3pjEDfhGLP_eQwNzACONYWp9W15IBsAZwZw3Uq1vZtOEgyzW_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZlWklQaMFguoW7lYFuXKVftumSRsqSNCAyx3QJn8EWlCa4BONp2zmQK2OdhJqZE2hNpx9IG0XD7mlvEOngmDEzhaNFRpeXjxEmcUZYZ3gHEmZRtMRuXMotaYeMLI1vgIaul1JF6aFwU5K8Z-s18MdzSjmkmPDAPhpcb_7cXMxODkOlUWN8hl-_eT_bDPXudnWE5KYrX4G1Zcz_Jwovv4KXoLAFaIpHjDWp5xUdf2IQxj3YCUqf7DOAbKYmNrElEQqIKA1bGB4qhkYrJtSrsyBE_q2Zmugym1ZCEEbKoSL8sfoDcWj_JvGZkss1ZlzD0yTmhtzscsMlo1ZzpaaCTCQg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دوست دختر نوس تو استادیوم بوده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/95505" target="_blank">📅 22:04 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95504">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b28394b6d4.mp4?token=L4Sk6cla44OhAglxldYzIhxfF-L1_i0CAvVaZFvEIJHLHpA0TR9-pJTLwZTI7PhrZPbg3Vaq_oIMU8rTwz6Y0XisFCPgnWiqT1whKYTWkuKednHAB9uN76H3tqpEbHJKzCsKyFB_wHUUuaalPMBhA7p36iVyGavFf_nWptUO2RkPni0W56QL15V6IXf2u2tRdUv9AjQ9uKSyX3zXKRUKk8qrAyfSFdUX1eyUIujQVkWqfHPpYRvElBcLMrQLJ6sbRgI--4zceOc2577u5SK7mADo6VAHwRl3SxtSsY-jTMhJASWxNeSGmDO_XIdTenhskOle74b_IK2M_Smt0UpH_JfCQs0CB5uShZQTOzgx_YxZr2EmydgMrzuZdWAoEbqhDbWOqw-iaexspLKPwdfFaMv3mZI2e_0SCv7_i8jXYWmfBkPi_dwG8MDwMOzkk3leGIJg-0AQwehf1cJDYtV5Bflj5D31Aw5N07u0gbtiJbA7ls8eLYO-o9okzA_yoEz7D--XXcmsqlzRG7jaXs-Boh-fVe3tbAIVicpd6P5zIN5EJ7VK2W3ldMWrIuNm-7G-oligKyyEiKk0FAVDHjamCxs1EgnaRIbqqvZhDTSmIMOUdoemm1sN9GENEO5wiuIRkal9VCe4z4PlvCJpQejEVCkIMREdZx7QElN_efs4cMg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b28394b6d4.mp4?token=L4Sk6cla44OhAglxldYzIhxfF-L1_i0CAvVaZFvEIJHLHpA0TR9-pJTLwZTI7PhrZPbg3Vaq_oIMU8rTwz6Y0XisFCPgnWiqT1whKYTWkuKednHAB9uN76H3tqpEbHJKzCsKyFB_wHUUuaalPMBhA7p36iVyGavFf_nWptUO2RkPni0W56QL15V6IXf2u2tRdUv9AjQ9uKSyX3zXKRUKk8qrAyfSFdUX1eyUIujQVkWqfHPpYRvElBcLMrQLJ6sbRgI--4zceOc2577u5SK7mADo6VAHwRl3SxtSsY-jTMhJASWxNeSGmDO_XIdTenhskOle74b_IK2M_Smt0UpH_JfCQs0CB5uShZQTOzgx_YxZr2EmydgMrzuZdWAoEbqhDbWOqw-iaexspLKPwdfFaMv3mZI2e_0SCv7_i8jXYWmfBkPi_dwG8MDwMOzkk3leGIJg-0AQwehf1cJDYtV5Bflj5D31Aw5N07u0gbtiJbA7ls8eLYO-o9okzA_yoEz7D--XXcmsqlzRG7jaXs-Boh-fVe3tbAIVicpd6P5zIN5EJ7VK2W3ldMWrIuNm-7G-oligKyyEiKk0FAVDHjamCxs1EgnaRIbqqvZhDTSmIMOUdoemm1sN9GENEO5wiuIRkal9VCe4z4PlvCJpQejEVCkIMREdZx7QElN_efs4cMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
گل چهارم پرتغال به ازبکستان (گل بخودی نعمتوف)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/95504" target="_blank">📅 21:58 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95503">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">گل بخودی نعمتوف ثبت شد</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/95503" target="_blank">📅 21:54 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95502">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">پرتغال چهارمی زد</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/95502" target="_blank">📅 21:54 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95501">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">گلللل</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/95501" target="_blank">📅 21:53 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95499">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">چه توپی رو گلر ازبک گرفت</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/95499" target="_blank">📅 21:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95498">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KO_WE27VvkOtyiIr5kTJIbOBEJhkj4w5vQpzyyuY4MqpGxObuV4f5DVo6HOZgzDYdLVhG7cVwMpoFxTrojnj26SBwAU5w2qPfBxlBD-3BXs2mVSYuXaKy2aylNOJ3t7MwZXVdhmbklpVAKsYbBtKQczDfPS8xhQApV4RRjejUHFJmERcom-fA1Shn8iy9KR6zP1ttiRma_he8DoI7VXPCttvnCS43Iy3KZA9BVz2JeqcN61EpVYpMSGeYkOFPiL-2RTOoiF_uUWkKLizfQvcmU97hZExuV2aEbWZap-0wKMUgwrFBCskpImFW-ptQgSWl0He5lTOsQBomME4Zu4AiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
واکنش ریو فردیناند به دبل کریس رونالدو: ببندید دهنتونو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/95498" target="_blank">📅 21:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95497">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">بریم سراغ نیمه دوم</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/95497" target="_blank">📅 21:39 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95496">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TGF1mNMcSoaOIdh1z2eNOvZYmAUHOZRSUr_X2UjXKTKRgTRVdvRcqFKqEYTEqPf7KAOrWrIVXCrT3qJWKVoFkAC2GGSmIfphKdyJ8NSxjIto-6XkCrm1-veMxKeUeAYmmLfLTupGpRQKxndvLkZj0EbSeWP5Zw39lc4y7IikIBEPljx29UEXmPHjZZdZMYUwQUlWfQZWTABNARGQMi2h4MdMXEGRR1QUY6EPuRzbk5veN5qsdFyrqHXzPX2cRg27NB8J5m2B9uYA9f4fyhqzi3QMjKDvWo0ZJaeSv84Pq63Ks6rvz2TdlBjnI3c0tM2n2YwgdjMIcREmekl3QEEYyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
کریستیانو رونالدو با سن ۴۱ سال و ۱۳۸ روز، به مسن‌ترین بازیکن تاریخ تبدیل شد که در یک بازی جام جهانی دو گل زده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/95496" target="_blank">📅 21:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95495">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQ1IioFqjfPGOgy-aALMeUacZ-KmouSYrafWZZqu8MQixofHHbjAldXOD-fSF-pRXUZotSR54GEQufrYh3oBi7UcqFXCFoXuH5Ww-NHjmV2AdPi2BsGX6kAyNEfPyLjJ2-zqmnP7ZjDnpayKAFiQAOWymBHziSv_RAwidR9gzH8ZzwBbA10bre4qkgtwV8BhK9faFTbXpLNUBCpm04sbz8dcpNXyJuHz--7dnSfwQ-n6nRF2H1FinJli9LC1p1FAt-gvXt9gcfTfSJoPcbs2Ay6ZUt_1r-m8dHkMt1lSrVDQCkr_xH-TwFPfXwkh3HZU5MjGZSSKEYLBFRiV_dB3Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
نمرات بازیکنان پرتغال در پایان نیمه اول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/95495" target="_blank">📅 21:25 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95494">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">پایان نیمه اول؛ پرتغال 3 ازبکستان 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/95494" target="_blank">📅 21:22 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95493">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j_gEh1FXxm1sIiE_9-3h21qFLGdOvXhzGD0lSKCqjsBrywe2fA2JeMEoeSujlnchzkI5v8sNFKHJ0-IudlSMENw2vwjHNwafhMOOby4uuOsA2paM2CcX6xDUW1K9JTN1DreeTptnp7ghOm_HmFQ8RpQSLNl5hPNb0RxnSIBEeCDdDrYDCMZpzKSkrX8fUgkM5w9-ZisDWYdP6j5TnfM69fVwJ4_ax2Pot8D10i_DbuUMbuQ-i3_ZenfwNadM34c9-F2dQaZXDpW7DN0jqnWa7-Jl0gAYVBOTfdipK7Bu4PpqSVnmroToy5pkjs-hGVpmq4FGtEqjIeA8bo1w4LNvvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری بانو جورجینا واسه آقاییش.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/95493" target="_blank">📅 21:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95492">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67baeb0629.mp4?token=ICG1PY6lSTDdma4BHH8y0MZU2UXuk1NAEKSz_91mVj2khi270Zp3kMtt-zUAmkKazUTaEn7ZVAGoD2Y9T-pXWnNf_gwW982t3MVqOaN9ewI_OzuMfeykcsKegvl8F-052Xt_YQFRPtPIGpc6OtZQlu8IfgvENhZwplBT3Smd3sB5BhbG-uYKkXyh6YDp37qGGEub-myEqydwa4GGTrDV6-dr8bSTJXmDjPXmQUSWYG3sXg_wjVCktGZ9wskCIm7K5QQaut0KR__KmW5ZkWr8D3KxT2YG33o9V4KxRkecluHP40kvZxSEFXyMV5O7jxPN-gmk40r4Dm_LqLVFa07UUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67baeb0629.mp4?token=ICG1PY6lSTDdma4BHH8y0MZU2UXuk1NAEKSz_91mVj2khi270Zp3kMtt-zUAmkKazUTaEn7ZVAGoD2Y9T-pXWnNf_gwW982t3MVqOaN9ewI_OzuMfeykcsKegvl8F-052Xt_YQFRPtPIGpc6OtZQlu8IfgvENhZwplBT3Smd3sB5BhbG-uYKkXyh6YDp37qGGEub-myEqydwa4GGTrDV6-dr8bSTJXmDjPXmQUSWYG3sXg_wjVCktGZ9wskCIm7K5QQaut0KR__KmW5ZkWr8D3KxT2YG33o9V4KxRkecluHP40kvZxSEFXyMV5O7jxPN-gmk40r4Dm_LqLVFa07UUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسپید لاشی بعد گل دوم رونالدو
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/95492" target="_blank">📅 21:13 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95491">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">برونوی بیچاره هم الکی فحش میخوره خدایی</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/95491" target="_blank">📅 21:11 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95490">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇵🇹
گل سوم پرتغال به ازبکستان دبل کریس.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/95490" target="_blank">📅 21:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95489">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">سلطان همیشه سلطانه حتی با ۴۱ سال سن
🔥
❤️</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/95489" target="_blank">📅 21:09 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95488">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">رونالدو دبل کردددد</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/95488" target="_blank">📅 21:08 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95487">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">گلللل</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/95487" target="_blank">📅 21:08 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95486">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">رونالدوووووووووو با پاس برونو</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/95486" target="_blank">📅 21:08 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95485">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">گلللللللللللل سوممممممم</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/95485" target="_blank">📅 21:08 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95484">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0F16X7rno9qg9S6g3cflZjhr69u_humNqGepxTSVWW_Q8vnEJoE45OHDFqrlbzNHUQbYg9dSrF8n24jrU4ThoCTzV4JnQAIj_WBhh7kzmJh-uaRE9apMKKJBjHeN9JErtfBvvfHPELXrnW8yFRH6pIqiPAbTY5hPqm-Ru0lwofLpwoYeB1fvbCxNZkztFjK6TPn76MczrcbGMqfJAKrzjOGYkzcRjykOwE18owID_Un4gcW4wfUQy9UmivGtg4SJq6NMEGuq7FwqRiEIFZ4L427xqMLw4f3Ep7bZM9kWXJvfO_N6SH_aMC4I0bREl7hQi_eCZrZqnDAXckZ0eGYKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇿
سوپرگل ازبکستان که رد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/95484" target="_blank">📅 21:04 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95483">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/843fc3ed89.mp4?token=A3T5NbS4EojYyzwQTnejy5_w1BSQ98PpbozTvG-dcTWdYGlTGv4O1U3SY4W1Uf1fzsYorSEKBt_DO4-yal_PW-TVUO-dpYvkBMm-p1chsPWk3dih0JBCQH3A0HW17uW1jwUytYkt-nFeNlWKvjpFS7dy2EfI6eChEnEe-O60juFPEe4heD5QQmwczUIgAhUV7byeiHGXGM80KwbcUZwYt4WK1Tn3L4QzhGgjPlPY2nCsSfmoBcwO9srbsNiO5rkXY-uI6Ds-TtvshGXlJWmRABwaRYFkY4E0F5Q-P6jz-VFQNtsvvo3hNxXpd10L-bm5SWRCLKqNnsg0Xdd0bv-KO6sQj2YeYJjCzgNE3Ylo8wZmjaEpp_mUcOBgrGOqyP1JJ9xCPCzXL0kv_74A2MVQXZ-L6PMMv2BVRef0INDXKkFBozM-mvCANxB5YyJ7d8RWFMfUvKXL0x7j5BLlPgewqtCui0wec8eB471aBpRWuyWwLVouqH2UdCK5Diu6i9lFyr8Q_QyAPIig8NbgwWHRUkIUDj1VhRWlR-DUw1S0wiZ1bJ8sCM5Ferzzwhz0kocp08xk1ds1xQBtDRNDu0cr5iwuI6HiFF9PFffryz6YsjX24snglI1SL5U6j4htGR6hq13G8Z7EFjeiudIKmHY2DsNySSp1XgtERUhgK0lE0fE" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/843fc3ed89.mp4?token=A3T5NbS4EojYyzwQTnejy5_w1BSQ98PpbozTvG-dcTWdYGlTGv4O1U3SY4W1Uf1fzsYorSEKBt_DO4-yal_PW-TVUO-dpYvkBMm-p1chsPWk3dih0JBCQH3A0HW17uW1jwUytYkt-nFeNlWKvjpFS7dy2EfI6eChEnEe-O60juFPEe4heD5QQmwczUIgAhUV7byeiHGXGM80KwbcUZwYt4WK1Tn3L4QzhGgjPlPY2nCsSfmoBcwO9srbsNiO5rkXY-uI6Ds-TtvshGXlJWmRABwaRYFkY4E0F5Q-P6jz-VFQNtsvvo3hNxXpd10L-bm5SWRCLKqNnsg0Xdd0bv-KO6sQj2YeYJjCzgNE3Ylo8wZmjaEpp_mUcOBgrGOqyP1JJ9xCPCzXL0kv_74A2MVQXZ-L6PMMv2BVRef0INDXKkFBozM-mvCANxB5YyJ7d8RWFMfUvKXL0x7j5BLlPgewqtCui0wec8eB471aBpRWuyWwLVouqH2UdCK5Diu6i9lFyr8Q_QyAPIig8NbgwWHRUkIUDj1VhRWlR-DUw1S0wiZ1bJ8sCM5Ferzzwhz0kocp08xk1ds1xQBtDRNDu0cr5iwuI6HiFF9PFffryz6YsjX24snglI1SL5U6j4htGR6hq13G8Z7EFjeiudIKmHY2DsNySSp1XgtERUhgK0lE0fE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇿
سوپرگل ازبکستان که رد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/95483" target="_blank">📅 21:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95482">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">گل اول ازبکستان زد</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/95482" target="_blank">📅 21:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95480">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">سوووووپپپپپررررررر گل ازبکستااااان</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/95480" target="_blank">📅 20:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95479">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">گل اول ازبکستان زد</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/95479" target="_blank">📅 20:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95478">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57cc14c630.mp4?token=nxFXu_05eaa86Y0-IuBpgVHc122-v1J5ikqADi6TidF5tJ_Rw5ulmsaVZvF6bs8E3exJ89NzJ-3rU9dNtYVmfH2QipOPjFyylKEwRox7hgc_DSkLQQjXvA36XxYlFH52q2UpJM_OD7PD4pnDnv0dvardVM57RaRuFG4fuaUcq6glMVhjGhHAh3UBkkjfhBxmLk6YabKQoWgGQt1ajYm3vwEOXGyFLZ19yXHElAsounxiMLdJ_4OdDhmzlZJ2P4VhrvCJgXgUzwjusE9sPb5Aj5SymB48Mj4HyXcvP67slkWWvvnYjXoCWsQKqOgdcjzJW0AVloDBWMOixW1BdWOWRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57cc14c630.mp4?token=nxFXu_05eaa86Y0-IuBpgVHc122-v1J5ikqADi6TidF5tJ_Rw5ulmsaVZvF6bs8E3exJ89NzJ-3rU9dNtYVmfH2QipOPjFyylKEwRox7hgc_DSkLQQjXvA36XxYlFH52q2UpJM_OD7PD4pnDnv0dvardVM57RaRuFG4fuaUcq6glMVhjGhHAh3UBkkjfhBxmLk6YabKQoWgGQt1ajYm3vwEOXGyFLZ19yXHElAsounxiMLdJ_4OdDhmzlZJ2P4VhrvCJgXgUzwjusE9sPb5Aj5SymB48Mj4HyXcvP67slkWWvvnYjXoCWsQKqOgdcjzJW0AVloDBWMOixW1BdWOWRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Siiiiiuuuuuuuuuuuuuuu
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/95478" target="_blank">📅 20:58 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95477">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b8dd0a3bc8.mp4?token=VbDuqO6SZnCpb5ciao37b-eo3NzJyGMq29FAL_N48o9mWbgmYZbuN_vNES6IWsKHJ2KSVITX1SRnkdL74jSlflaAJGmkNoriw_lUc-RTH1abWaQD9jvzwuk7GAB5I1rT2nIAC1E85yPlFteZxt3LXrWmrEYjeaYKXtRKxeDaKjNAJSi7_NVaqGiOfxG3K3Qdgo1svlbMOjlu6MncpqMM02Aaw1TaQ6DmpUTSaMolDWc4SIsolCVLljmuGUwLqCwRKlZGe3qLs0V1oPCtG8n4fDU46LQ0yUMGs3y73WDy0nZtxWPAE0q5km5Uh-6anTmiazw99zXe462zHvHbNwdnJ4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b8dd0a3bc8.mp4?token=VbDuqO6SZnCpb5ciao37b-eo3NzJyGMq29FAL_N48o9mWbgmYZbuN_vNES6IWsKHJ2KSVITX1SRnkdL74jSlflaAJGmkNoriw_lUc-RTH1abWaQD9jvzwuk7GAB5I1rT2nIAC1E85yPlFteZxt3LXrWmrEYjeaYKXtRKxeDaKjNAJSi7_NVaqGiOfxG3K3Qdgo1svlbMOjlu6MncpqMM02Aaw1TaQ6DmpUTSaMolDWc4SIsolCVLljmuGUwLqCwRKlZGe3qLs0V1oPCtG8n4fDU46LQ0yUMGs3y73WDy0nZtxWPAE0q5km5Uh-6anTmiazw99zXe462zHvHbNwdnJ4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
گل دوم پرتغال به ازبکستان توسط نونو مندز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/95477" target="_blank">📅 20:49 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95476">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">منددددددز</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/95476" target="_blank">📅 20:47 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95475">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">گلللللللللللل دوممممم</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/95475" target="_blank">📅 20:47 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95474">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bedn1sJik5MXVwbuKc33AEE7HHc7I-oNOgdZ6MGAvsaHltwbBDrhAT2m2_zCDY7Pd61NEx2vgUplRkkGXJ-PFY9eOuvyleNtdpSJEjD-y_D7n2daDprxe9d1T518nTcjU6BEd7VPalHuoKJ9wn5Vyx97Tk9FpuC91ZRWt6X29YqC9LoCYsKoK8_rqfMLhfiUmzJZ6hA_k7YpzyXMPyCs7ppRonhrnjRHtxYDfWzpD_SJZb4R4NiB-YSPi4QPYkqdjX-U-Ho7nq1CxtIh0B1GMq8PSiyEtJswPqAZJXSeA1rCuFPyYYf94y4otisNTSyECXcqL0hfXr9f9kDCcC3ffw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رونالدو به اولین بازیکن تاریخ تبدیل شد که در شش دوره مختلف جام جهانی گلزنی می کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/95474" target="_blank">📅 20:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95473">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">گوت گل زد
🔥
🔥</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/95473" target="_blank">📅 20:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95472">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2401591606.mp4?token=VD1usQKfX3ah3iZ8rzOsfYXOJKwVKYieDBYfvm0NQxAJU4RPm4R1BoewKwfg0ymSCsNpFpW2lPtcf_9nhMzkAAOJefyKKu9g0xj6_jIZOTiOlDyaR5UXVGsL-PyZffiiME8yYkV2nCw1FEL8Br2m51jGDSutwuNfpf8NjZxpWDQBu6gmzZv3ZNUbML8X2jAdn-mijQoLXEnrKQdmRFXz41RPDRCGPoDty_4eqFzSs1pJYl3Rlz9N9FnwH3LpyA3CbaZeoH6oNqJuevc0MF4yLYwlnAH1WCxvV3EzMHj4aN3ko05KYnGLum8WMKWm-VTWGJEG38getK2VceOlgf0vV0Fq1aJlrKMlA3s1WGK4KHTh-w1InZOnwjmXnDp8yxWlf5xATGYxL2NYXyp0CMI2kDayhxwD66_dDPcKQ0bHzW2u7lyQ5ckc1DTzpSU7ced0NXV0ZUN_Yl2w-ZzOqLNsRaE99FYSeEY1UKiQYhvFBzj0E560SwiqJ8Wu4443Sy7GOt1CHRyuRggBmBEXiWkRf_-68h2yz7RuigrvC24y_0vi9cfk3O3IpyudvSj0mPVxpWnDJfjMcgtiEeYZb0ZmXabOdsqVUrDKf0Pj5lFlv9jB46u8d_OiV8-iFUBfKUq_-GdrxkqutqoAoLnuorWeYhqMU0SxIBoG6i19M5qDzUc" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2401591606.mp4?token=VD1usQKfX3ah3iZ8rzOsfYXOJKwVKYieDBYfvm0NQxAJU4RPm4R1BoewKwfg0ymSCsNpFpW2lPtcf_9nhMzkAAOJefyKKu9g0xj6_jIZOTiOlDyaR5UXVGsL-PyZffiiME8yYkV2nCw1FEL8Br2m51jGDSutwuNfpf8NjZxpWDQBu6gmzZv3ZNUbML8X2jAdn-mijQoLXEnrKQdmRFXz41RPDRCGPoDty_4eqFzSs1pJYl3Rlz9N9FnwH3LpyA3CbaZeoH6oNqJuevc0MF4yLYwlnAH1WCxvV3EzMHj4aN3ko05KYnGLum8WMKWm-VTWGJEG38getK2VceOlgf0vV0Fq1aJlrKMlA3s1WGK4KHTh-w1InZOnwjmXnDp8yxWlf5xATGYxL2NYXyp0CMI2kDayhxwD66_dDPcKQ0bHzW2u7lyQ5ckc1DTzpSU7ced0NXV0ZUN_Yl2w-ZzOqLNsRaE99FYSeEY1UKiQYhvFBzj0E560SwiqJ8Wu4443Sy7GOt1CHRyuRggBmBEXiWkRf_-68h2yz7RuigrvC24y_0vi9cfk3O3IpyudvSj0mPVxpWnDJfjMcgtiEeYZb0ZmXabOdsqVUrDKf0Pj5lFlv9jB46u8d_OiV8-iFUBfKUq_-GdrxkqutqoAoLnuorWeYhqMU0SxIBoG6i19M5qDzUc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
گل اول پرتغال به ازبکستان توسط کریس.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/95472" target="_blank">📅 20:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95471">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">گوت گل زد
🔥
🔥</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/95471" target="_blank">📅 20:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95470">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">رونالدووووووو</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/95470" target="_blank">📅 20:36 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95469">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">گلللللللللللل پرتغالالللللل</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/95469" target="_blank">📅 20:36 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95468">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">نزدیک بود بزننننه کریس</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/95468" target="_blank">📅 20:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95467">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">پرتغال حشری شروع کرده</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/95467" target="_blank">📅 20:33 · 02 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
