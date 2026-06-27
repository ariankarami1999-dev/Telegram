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
<img src="https://cdn4.telesco.pe/file/U3MfJiXJ6lyJ-mSvlAvGo1gTMsKafdfL3tuwCJ7tC-VfMv-0FYjL9mKoUssHD-f-3MuCsn4NpqaVjPueQshbAEk-Yusl9nt3V1fZxUk829e79LlE4n9rLyRtSnVuqkfg5B-5pb3ckDpVHxZmY5xCSHlGHB3qp3MgU_vpLuIH78fEt0GsJOM1dLOTvwo6rgI4MEf4q6bnBbNDbCahq61vvAsRUmTal4jdluFOZOCsMB1q4Q1WXcxMNOgdE9rartWPTf_Lctklo_p1EPwC_SVl4XD1dXmR50zZPLWLzcp4x5K6NDr1tHdY62clUBFrIq-87QNByfkggNtxY3YwQGhhyA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 219K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-06 12:39:33</div>
<hr>

<div class="tg-post" id="msg-66918">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fvWRSqtPgJWEfT1gkr_wSEesoZpL8nGvhH4NcMUpsB31gE_Lyv85edsGJuXtiOXPZdAXipPfWsjloB1n5i1L472bCmQfxHOjcH6H67k_CGjgIwzkJpiGBiSqxH7BG9skAlyvVcQgL6QgbfoYbSc_6JEob2SPj3O7H8_4ioDTHhZNr_2vDJK-CXYnsF5TDavFFhYD1Ds7CI-VXq8Ic-QOXiaJKOembwg4uPE9hNeLrho8c0qi5-f7Lw5ck2yY_b6fGsaqUdqv5MslcUpiSZMhWlEmEfafS-QfdUPf4SdTy2c1rcjk9aDfdVTfZtYdJvMl-nkbi4w66FKaeqoG-H_r8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
نبویان:
ضمن تشکر از سپاه قهرمان ما به خاطر پاسخ به تجاوز دیشب رژیم امریکا و در نتیجه نقض بند یک تفاهم‌نامه، مطابق بند ۱۳ قبل از عمل به بندهای۱،۴،۵،۱۰،۱۱هیچ مذاکره‌ای نسبت به سایر بندها نباید آغاز شود.
منتظر تحقق شروط و واکنش شفاف و پشیمان کننده‌ی مسئولان مذاکرات نسبت به نقض تفاهم هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/news_hut/66918" target="_blank">📅 12:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66917">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6e496d9ac.mp4?token=bynGzpRYPjR8mCLsLwumKO0O17RBUGUCAP4Bc0HyzoE4NRQIZSe3T606qyWS46_T1KSbWB5DCT4zTazMZGnT4jfvv_ijhsmSzrnhrEIvsC_bkl9AnTb2QWq7l3_VH4YHzQAIy8MjhVuCsDdnRTQv_4F220VA6tnu9nh9v8I5i56q_ELelmP3gFNTnf0JkXGN1RmncW-U-tJZzl4DPTNnYG7fWO7-D1YNrDAx8jW-h1RXLGweQscT-xitxRI_vDl36-fWfjIFLhuvQm1iOqftngGFMM8rdqbxcKqpxIIq7u3gjmrUpTF_PBCU83oQTGq1_jxf427W0U-b5dgOegeWiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6e496d9ac.mp4?token=bynGzpRYPjR8mCLsLwumKO0O17RBUGUCAP4Bc0HyzoE4NRQIZSe3T606qyWS46_T1KSbWB5DCT4zTazMZGnT4jfvv_ijhsmSzrnhrEIvsC_bkl9AnTb2QWq7l3_VH4YHzQAIy8MjhVuCsDdnRTQv_4F220VA6tnu9nh9v8I5i56q_ELelmP3gFNTnf0JkXGN1RmncW-U-tJZzl4DPTNnYG7fWO7-D1YNrDAx8jW-h1RXLGweQscT-xitxRI_vDl36-fWfjIFLhuvQm1iOqftngGFMM8rdqbxcKqpxIIq7u3gjmrUpTF_PBCU83oQTGq1_jxf427W0U-b5dgOegeWiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله شیر تعذیه به جمعیت
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/news_hut/66917" target="_blank">📅 11:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66916">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e02aab4b18.mp4?token=Ncm46_2bEu6Z8BGvTmHFjjrB_iJegPM_SmC3EeLx3TNkkG2DHLCM5kEF-I97ImcO0v1NtqcLLOMr_46BlqvmM6fUQ56eFX5n_Ag5v7azb5FuX3tO8zfUhdQQF-fqbagULrgoX4znbRwAf3cp7K94BIl0EewHm88VMXLg2NZ0L3OVYfoHCLdA21jJM5U3b3hwn_agrcKKnndfbmim2GJusDmacExwOm_vfINWY5BvmbnUWSGPaHFUw_2OqJxUf3WKeKp1oLWDphJdrZTnedy1_Odc4EYBv5Wpf3hTQWZV04waTPnPuQPrV_mTqe7bpxEMF4h6Bkrl69sDL4T2dTnE_qm8cERdV9VQb2xhM-fz0lAqD8n-lc_yLJb2Qp121AI5GjV80yR_dX52YPDn7NedYzgaSKsrd5Z6FBRhlBniGABk4kRKGk7h1C_QPkhrUzbiN07Bg-95Map9b5W2UR2L24rc4Zb29NkCwCQg3L4WsXwCiOsidFNljgRJwzcrFtxsFiHY7A7W9MmzJQGNso8zRPMXivOucb1hqB8HdCtVr85dYzY4v11fijnQ049oW1mKXN5mJg45kY_RGD-7FATCrn8AmcQYcSUx4YZPKOFtGpCa0LAkT4dtotfkV1zYZdA8uAzocNj0iDyVZf5wGO8EH8V9G1JfH__5wWSFuMpkki4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e02aab4b18.mp4?token=Ncm46_2bEu6Z8BGvTmHFjjrB_iJegPM_SmC3EeLx3TNkkG2DHLCM5kEF-I97ImcO0v1NtqcLLOMr_46BlqvmM6fUQ56eFX5n_Ag5v7azb5FuX3tO8zfUhdQQF-fqbagULrgoX4znbRwAf3cp7K94BIl0EewHm88VMXLg2NZ0L3OVYfoHCLdA21jJM5U3b3hwn_agrcKKnndfbmim2GJusDmacExwOm_vfINWY5BvmbnUWSGPaHFUw_2OqJxUf3WKeKp1oLWDphJdrZTnedy1_Odc4EYBv5Wpf3hTQWZV04waTPnPuQPrV_mTqe7bpxEMF4h6Bkrl69sDL4T2dTnE_qm8cERdV9VQb2xhM-fz0lAqD8n-lc_yLJb2Qp121AI5GjV80yR_dX52YPDn7NedYzgaSKsrd5Z6FBRhlBniGABk4kRKGk7h1C_QPkhrUzbiN07Bg-95Map9b5W2UR2L24rc4Zb29NkCwCQg3L4WsXwCiOsidFNljgRJwzcrFtxsFiHY7A7W9MmzJQGNso8zRPMXivOucb1hqB8HdCtVr85dYzY4v11fijnQ049oW1mKXN5mJg45kY_RGD-7FATCrn8AmcQYcSUx4YZPKOFtGpCa0LAkT4dtotfkV1zYZdA8uAzocNj0iDyVZf5wGO8EH8V9G1JfH__5wWSFuMpkki4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یک آخوند:
غلات آمریکایی آلوده هستن و میخوان ژن مردم ایران رو تغییر بدن. آمریکا قبلا شکر شوروی و برنج ویتنام رو آلوده کرده. خون هایی که قبلا برای ایران فرستادن هم آلوده به ایدز بود.
@News_Hut</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/news_hut/66916" target="_blank">📅 11:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66915">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vlf3k9TXdq8D44ve_uadCLO5tJwOJMbkafc9XA6e6ITVCvjqOgP4Ln681-ffb2P8hxEq9KPQdtfoictJbf77s8tFiz91JzG3to4o7cf58YM1J2cQMhc-0sFBHWoZXles4PGF3y172UR7QIN9zlGpSScw5vp-x7JGmebZyvScbzB_Ij2XIcWbCaB5SWDCER6GzkZsdJg14f_KImnxIA2u3jJKyi-9nr1qt7gFzxjiH4DDuDd2bmD7fpa1ZmQMavSPJnCVK5qDqzx2EBaWFlRV8Yp7saR38PHmjeJysQ_Wjsag2t6Kr69l5We61lfi12YNkQFDD0NCL0BnBNc4En3A_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇸
پرزیدنت ترامپ در تروث سوشال:
نمایش هوایی چهارم ژوئیه، در آسمان واشنگتن دی‌سی، پایتخت بزرگ ما، بزرگ‌ترین نمایش هوایی در تاریخ ایالات متحده آمریکا خواهد بود.
صدها هواپیما از انواع، اندازه‌ها و سرعت‌های مختلف به نمایش درخواهند آمد. من حدود ساعت ۹ شب سخنرانی خواهم کرد که پیش از آتش‌بازی است که باز هم، مانند نمایش هوایی، تقریباً ده برابر بزرگ‌ترین آتش‌بازی در تاریخ کشورمان خواهد بود.
پس اگر هواپیماها، آتش‌بازی و دونالد ترامپ را دوست دارید، آنجا باشید!
@News_Hut</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/news_hut/66915" target="_blank">📅 10:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66912">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uhYx6bnAVroOoIUDEcnLljcxhNe8hxDSN1CsHaSeIenouILd2uBxEN35iOLtpwLBgQVSzJMde5AH3J7FMHeJ17Be6dXf9BsSXm-C3mRE7cjvwDuYjnyS18WMB-dGdCOBZ1PxcT8VLXofX4q1b7vUE0MtpBC30B5-stb7jF2QVPu_4iiiL5GIK5XGS1WUmDCcTYZNQKs3_ofBbD4CUCQ5tDtvhXbnD5XY9lENJNB-W9OlMw9Pki8wrXx4_RpAMTxyu6GOlcFLj4JOm9JuviODvCFzBZCqHyP9JFXuLOF4FTVOhuoJf9hV8bSgMtydZu9z5ZLmagKHKtwxvugnth73oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aJJn9gM8OEL-Wy9GzVzbXm_kop0eBm6ncb_RsketF2hyZE82D59rBZuX2DTCRAwl5lAx6bgykV23BhUPxBXz1Yg_NXFC3o53-wSYdp-T7iqzOP5TfM9BWIpPydXFF2aEchRdowAAJzRW0eT1KPlYWnmUDrYuq9HH3is-WWsCfqWyeGwL1noKgenMWLyt_UCaD1zm3K34Hr7wn5QQQXgo75MiL0_ATLhWGQUp_HKZvak2Sax24i0xX0xfJM77mHL15_5eqLSsPc-3Gm2hR5Fc_gvl-8v2Z5KWWDpgVKRGbThCIZgnyCZF-j6QWD99rZz4SFPKBwWfolhmZx3m2Z0rcA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/812712f3b6.mp4?token=oZQYx_UDDBEWf21Y5gapWIyvSR9fMfumnAe6Vl1TEE8hHtMrpHSrQG2AgJh9LI6l9LTIT0Kwn2S5AXnZwyUN9iY9Hu6hJwLaEoltZX3iWzCRrzEXfg-cfbZ_SBZ9Gv96feeBaUan75VKEXktMchx-dI3XzFs_NERW_yXIRZIMgH9Celmfb81_zKSKprNIOmtHIjVt6SIbeTMzWqchL1ZJVX0eXcQwBQYSx7tdw28vxOtN80VaENQX8S7thvhl6-JZjGIUNyrLBCL358bPLfJdKX9FQfDfqoYujsKJpnBqIxllfkhDI4CbIALS2RcMeTrjmKtBUJccVm62aSut0d7jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/812712f3b6.mp4?token=oZQYx_UDDBEWf21Y5gapWIyvSR9fMfumnAe6Vl1TEE8hHtMrpHSrQG2AgJh9LI6l9LTIT0Kwn2S5AXnZwyUN9iY9Hu6hJwLaEoltZX3iWzCRrzEXfg-cfbZ_SBZ9Gv96feeBaUan75VKEXktMchx-dI3XzFs_NERW_yXIRZIMgH9Celmfb81_zKSKprNIOmtHIjVt6SIbeTMzWqchL1ZJVX0eXcQwBQYSx7tdw28vxOtN80VaENQX8S7thvhl6-JZjGIUNyrLBCL358bPLfJdKX9FQfDfqoYujsKJpnBqIxllfkhDI4CbIALS2RcMeTrjmKtBUJccVm62aSut0d7jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
برخورد هواپیما به آسمان‌خراش ۵۱۸ متری در پکن
یک هواپیما با آسمان‌خراشی به ارتفاع ۱۷۰۰ فوت (حدود ۵۱۸ متر) در پکن برخورد کرد و سپس به زمین سقوط کرد که منجر به تخلیه ساختمان شد.
در اثر این برخورد، دو پنجره ساختمان شکسته شد و هواپیما کاملاً متلاشی گردید.
دود غلیظی از طبقه همکف ساختمان، جایی که لاشه هواپیما پراکنده شده بود، به هوا برخاست.
شمار تلفات هنوز مشخص نیست
@News_Hut</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/news_hut/66912" target="_blank">📅 10:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66911">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BuNBMKsztCCxFntWtE9Go0oZWamr6oy5ffPJtq5HdcUq-UEjFzsAxZ8y0cN6RbDWeMPaechVP0Wq9TG2WCPyRWvGopbkkxyLkBeK2Fk44Fz25d2zkcBO1qxH_twjufgsTgR1jOQeUQmk9BaTpgzQDPcZlYOq2snXt0HuTjwNxOK3r64k3oR8Bj0xo4oYp2Z_1V4WHJE3-ZU8PBrjSyA2Y3txDaX_dV_ogvyNUPtF888E4mtdZJW0chxhAUCMKznSIEs_on04KGs9zib0mErS0mNeA7iR01ZASabG_uxvwgWCXbSRfside9smgBQN5c69kMCtdYfb9zqEGzt_mY8-zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
❌
🇺🇸
آیت‌الله جی‌دی‌ونس:
ایران توافقنامه آتش بس امضا کرد. ما آن را گرامی داشته ایم. اگر آنها در مورد نحوه اعمال تفاهم نامه اختلاف نظر دارند، می توانند تلفن را بردارند.
اما خشونت با خشونت روبرو خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/news_hut/66911" target="_blank">📅 10:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66910">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01b5404ad7.mp4?token=XhvxPJEmhgn-76YWVC-XEYzi62ECdFEhGWsdiKAMiQGpKiZCY2lBBce1b7dIjtHfSE-X9XFsw7zwFhdIoQUXgc4faE_l-LwmyX-7fwS6CKYF_TzG9eDpshwsoQ_K88dcOyQbmE-28fYY2-7ieHG4xpPvpP_Xz6516i--8LqsXXpJ-ppab7zLBlxlp1Kriyje5EakWFKduzEFgE4pBlyq5_Eg_dmqmeiRf_PPM6QGD5CXLSzEwynKfWmKBszdgSNv5F0onDl7oosMnjo5XX6oZaJVv7dI_JWF4islQPaZkBFhQFXgQe0T5XT01Y0oGk3cBF_UjWeNYpQDr0MIfeG5Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01b5404ad7.mp4?token=XhvxPJEmhgn-76YWVC-XEYzi62ECdFEhGWsdiKAMiQGpKiZCY2lBBce1b7dIjtHfSE-X9XFsw7zwFhdIoQUXgc4faE_l-LwmyX-7fwS6CKYF_TzG9eDpshwsoQ_K88dcOyQbmE-28fYY2-7ieHG4xpPvpP_Xz6516i--8LqsXXpJ-ppab7zLBlxlp1Kriyje5EakWFKduzEFgE4pBlyq5_Eg_dmqmeiRf_PPM6QGD5CXLSzEwynKfWmKBszdgSNv5F0onDl7oosMnjo5XX6oZaJVv7dI_JWF4islQPaZkBFhQFXgQe0T5XT01Y0oGk3cBF_UjWeNYpQDr0MIfeG5Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قلعه نویی:
اینم یه ازمایشه؛خدا داره منو میکنه
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/news_hut/66910" target="_blank">📅 09:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66909">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e70e539fa9.mp4?token=PDiiO3IXLhEri4L9UeiIlNtbtzmd6muDXpQmq7K9c2mF7C6cnAMlxCmRTV6qDVKp8S8QHaKBg2pDyBI3GNMOL8Hd-g-BmFrNzBEosURYEr2n0QcxjmM4-ZTU5Ju5w33pJCMzQy3_61uUg1E8LJqrwodaMEpwflSE3XbXMqBTUu9Sl4zdchsRtsnQySKTlbs6ed-SuAQl3stvvvHI3pb-lqHxVPZmmKZlXq82TLCkbtHxibESkgWds854kbjnvH6qHqJucPRYkep7GlpzqCsoa9VTZfKErnuculFfTklThe3GwnszXCsp6R1_Tw9EzjdQ0_wKx7Zutj0e0yJb2X2wCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e70e539fa9.mp4?token=PDiiO3IXLhEri4L9UeiIlNtbtzmd6muDXpQmq7K9c2mF7C6cnAMlxCmRTV6qDVKp8S8QHaKBg2pDyBI3GNMOL8Hd-g-BmFrNzBEosURYEr2n0QcxjmM4-ZTU5Ju5w33pJCMzQy3_61uUg1E8LJqrwodaMEpwflSE3XbXMqBTUu9Sl4zdchsRtsnQySKTlbs6ed-SuAQl3stvvvHI3pb-lqHxVPZmmKZlXq82TLCkbtHxibESkgWds854kbjnvH6qHqJucPRYkep7GlpzqCsoa9VTZfKErnuculFfTklThe3GwnszXCsp6R1_Tw9EzjdQ0_wKx7Zutj0e0yJb2X2wCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه رامین رضاییان بعد بازی
@News_Hut</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/news_hut/66909" target="_blank">📅 09:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66908">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/449f3cb5a2.mp4?token=NxDv2qsU88Uht_eMdoupW-SKbUj4Ut1TasWu0b_Adhtjicd6CDZi2K80c7T7UF7MEEFxMfCkGQEt9Tqn2fQ7sfnBKM2OPrjumx94MBHqtLycjmGV5hbNfeZfajmCqkLhtromXXjyXFjjWOcm8gQmkIwMHQmZyXNan5tYlaqp3Bgai2yAzpKQjUkfHRy2DHAJz72E0e8WrJ_fPj3PJeXqCND4gZPwhu6SAsKf413wTAwr6LW0E3GsIQlYyXsUnMp30N21JXLynW9BkFFs0Ohb_VZtAhDh1ylp3NH1cUQx8JRVqN8LA58ysvU1Po0XEiUIvdTk1A4VafRVDcJJtoeHDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/449f3cb5a2.mp4?token=NxDv2qsU88Uht_eMdoupW-SKbUj4Ut1TasWu0b_Adhtjicd6CDZi2K80c7T7UF7MEEFxMfCkGQEt9Tqn2fQ7sfnBKM2OPrjumx94MBHqtLycjmGV5hbNfeZfajmCqkLhtromXXjyXFjjWOcm8gQmkIwMHQmZyXNan5tYlaqp3Bgai2yAzpKQjUkfHRy2DHAJz72E0e8WrJ_fPj3PJeXqCND4gZPwhu6SAsKf413wTAwr6LW0E3GsIQlYyXsUnMp30N21JXLynW9BkFFs0Ohb_VZtAhDh1ylp3NH1cUQx8JRVqN8LA58ysvU1Po0XEiUIvdTk1A4VafRVDcJJtoeHDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
فرماندهی مرکزی ایالات متحده (سنتکام) ویدیویی از حمله نیروهای آمریکایی به یکی از اهداف مورد‌نظر در ایران را منتشر کرد.
حملات سنتکام در واکنش به حمله پهپادی پنج‌شنبه سپاه پاسداران به یک کشتی انجام شد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/66908" target="_blank">📅 09:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66907">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">‼️
بازی تیم جمهوری اسلامی و مصر با تساوی ۱/۱ به پایان رسید
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/66907" target="_blank">📅 08:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66906">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66906" target="_blank">📅 02:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66904">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qrO7cSrShcbA7oEVSGy5OWRjzxGLCxF-edMDWKn1RPt9HA9KJVM3fXvMWYGyOQsPlN68UOuZ0g8AHCZgyZ7L3BWLKZtMlLzsQSY1x0O0QdGP7qSCPQLv0GaI9GUDiVk0GA1dmY-QquKn3M2ufhxBj6mgV7dTo_P12UOu8c6qVOv6_vBlLp0jPzhbm7XZCQh1DPPQ7kSRx7BqnELKKgbLNgcJHjiavAahFoarTXpMkfnAlxY3UENbDS0V1bja6AbgWFiYB539GxTZ0SpjFhldfLt2L2yEb19ChY_es5VRk8i1QiKevT7Ghc24Xg_jMvOSAxlKKD6nFUghENAHiByVLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66904" target="_blank">📅 01:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66903">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
سی‌ان‌ان به نقل از یک مقام آمریکایی:
حملات آمریکا در ایران اکنون به پایان رسیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66903" target="_blank">📅 01:13 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66902">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
🇮🇷
بیانیه سپاه پاسداران در واکنش به حمله آمریکا به سیریک:
نیروهای ما موفق شدند این حمله را خنثی کنند و نیروهای مهاجم را وادار به عقب‌نشینی کنند
ما تأکید می‌کنیم که این تهاجم بدون پاسخ نخواهد ماند و پاسخ ما در زمان و مکانی که انتخاب می‌کنیم، سریع و قاطع خواهد بود. هرگونه حماقت جدید با پاسخی سخت مواجه خواهد شد
.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66902" target="_blank">📅 01:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66900">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/378d83ba5f.mp4?token=ZlsvbDClqvN_jrciemggC96xQ3ivTs219Hanke4olGno-WXNGEkHYv4kGcFMr-Y04ucP8cSGTr-_s1eIEIVSg7G-INKl2Ss1HOy3JK4vXV6VsUT2yHdO_m3eh46aadH9Eycdlr_GMcrzgJaES9LJM67OGOl99BEcmy5MKwkbA3dW_4TgnCrtSTle54p-gSDd0TLT6pCnsjd2DKl6IElc0BWoKmRhgAXgFMArPpb1-EM5sETpFjxmLBXFhXIuxgfsKP7rFgFF-gEiuBgn8BwD75q3Jr0M1mJ5fsrsm8yPt0lqopGw98CLG83C-2ZEXKOVS9CHjUPXl9kcGbu-Yyyxaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/378d83ba5f.mp4?token=ZlsvbDClqvN_jrciemggC96xQ3ivTs219Hanke4olGno-WXNGEkHYv4kGcFMr-Y04ucP8cSGTr-_s1eIEIVSg7G-INKl2Ss1HOy3JK4vXV6VsUT2yHdO_m3eh46aadH9Eycdlr_GMcrzgJaES9LJM67OGOl99BEcmy5MKwkbA3dW_4TgnCrtSTle54p-gSDd0TLT6pCnsjd2DKl6IElc0BWoKmRhgAXgFMArPpb1-EM5sETpFjxmLBXFhXIuxgfsKP7rFgFF-gEiuBgn8BwD75q3Jr0M1mJ5fsrsm8yPt0lqopGw98CLG83C-2ZEXKOVS9CHjUPXl9kcGbu-Yyyxaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
اغتشاشگران در حال حرکت به سمت مقر های دولتی در بیروت
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66900" target="_blank">📅 01:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66899">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🤯
🇲🇽
پشماتوووون فر بخوره؛ یه‌زن مکزیکی برا اینکه شوهرش رو سوپرایز کنه و بلیت جام‌جهانی بخره، یک هفته قبل مسابقات عکس پاهای خودش رو‌ به مردان کشورهای مختلف می‌فروخته و از این طریق تونسته درآمد زیادی کسب کنه و علاوه بر کیر زدن به مردان هول خریدار، شوهرش رو به…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66899" target="_blank">📅 01:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66897">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X6bycQ0H_-bQHyYXuerZVIJXGJPtf5k8WsGXCSgJHv49PhG4nmXW-iQu-VJCQd7kWV55iEoHQ0ZOChaxQNIVrTDcT--J8rDU55g_m26OMG_NMnIZpPd0f6iFRIYFHk1nhbD4p8gvzjIjALxeOz3IOea9vWUXvSrv6ZeDqWRxgCcmcWD1rM8_Iz5Vsla0ptPnx77bdiM0EkQ-flrpXVVYi0HCEmtenVkLCLPkeQxFy3QSW0F96Jw7YioerOXieHpnIekFPoqu2AwO902ThPjSxMerVsP40LwQyS5TY0Q2LN_-f6eQZJKXTU804dKwVekKZ_IwRG4Ibo8HGvTu62LO-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c146777e05.mp4?token=j_anMZe4xYmoKy7QSkaAWb0ci3chYBWUunVSY3erLkX4CzoeQJ0WbZUqUFQ924StGLxuwyCqjIRaSNFqusy1Uds445x0kxq-Fcm-v6HHkM3Bx7xU6ZphtjRMPNbRzAUMlN9jylmaP4-Lppymkqa2evQ3n3hTnODPlJ_q7sRCOcxXNaMhDTt-GfgPGawMRhcTYBUIqQC6V_jk80jOzadCv0HcE8DuUNRevjK2hsicPSMx0mIoku_S9dwAyGKwVS4CbwnvWK6PI602QqfcEzkno5RZa5YjA44BTzxTT0as0sJQJXh1dh6KB93IgtSR55-hm5Ojo9PKmlBjj0HmX1F-5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c146777e05.mp4?token=j_anMZe4xYmoKy7QSkaAWb0ci3chYBWUunVSY3erLkX4CzoeQJ0WbZUqUFQ924StGLxuwyCqjIRaSNFqusy1Uds445x0kxq-Fcm-v6HHkM3Bx7xU6ZphtjRMPNbRzAUMlN9jylmaP4-Lppymkqa2evQ3n3hTnODPlJ_q7sRCOcxXNaMhDTt-GfgPGawMRhcTYBUIqQC6V_jk80jOzadCv0HcE8DuUNRevjK2hsicPSMx0mIoku_S9dwAyGKwVS4CbwnvWK6PI602QqfcEzkno5RZa5YjA44BTzxTT0as0sJQJXh1dh6KB93IgtSR55-hm5Ojo9PKmlBjj0HmX1F-5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
اغتشاش هواداران حزب الله در بیروت در پی امضای توافق اولیه میان دولت لبنان و اسرائیل
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/66897" target="_blank">📅 00:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66896">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
🟥
فاکس نیوز به نقل از مقام آمریکایی:
حملات آمریکا به اهداف ایرانی همچنان ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/66896" target="_blank">📅 00:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66895">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KkiGCAYrMkEcIiEKerwXI8yjSyj2J_fmpcZhuFpg18dKLC8aRWNPupQyzQBC94UtZ0i-FT4WLgPW_ikcb2awnNCecJHV8fRKP3e36VNEcFmrli29iVY7CFsQ5s32ulgiJ9nEO71uQRh_GWAcWkVzIbseopNmFHlJf4Lygu_xGxoqMj3FELFHzeoVdFDezSNew66jdm8Ub0-0TpMG1VtIyenIfdXXl1BVSUI4QVPX9UMkvq5giNL-xhXNbzk_SPZeOQvXddNfajOkmVxY35CMnoVvOq2NKAQXyqS7MzJ4FJxsFh0lGPQ9Pgd3nLewM8mpDdggUk7vFLYR78Zn9vD8TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
سنتکام:
نیروهای فرماندهی مرکزی ایالات متحده (CENTCOM) در ۲۶ ژوئن، به عنوان پاسخی قدرتمند به حمله دیروز به یک کشتی تجاری که در حال عبور از تنگه هرمز بود، حملاتی را علیه ایران انجام دادند.
هواپیماهای آمریکایی پس از آنکه ایران در ۲۵ ژوئن با یک پهپاد تهاجمی یک طرفه، کشتی M/V Ever Lovely را هدف قرار داد، به محل‌های نگهداری موشک و پهپاد و سایت‌های رادار ساحلی ایران حمله کردند. این کشتی باری با پرچم سنگاپور در زمان حمله ایران در حال خروج از تنگه هرمز در امتداد ساحل عمان بود.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/66895" target="_blank">📅 00:14 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66894">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
🚨
#فوووری
؛باراک راوید به نقل از منابع آمریکایی:
ارتش آمریکا به اهداف ایرانی در منطقه تنگه هرمز حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/66894" target="_blank">📅 00:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66893">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
❌
صدای انفجار ها به «طاهرویه» در سیریک هرمزگان مربوط بوده.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/66893" target="_blank">📅 23:58 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66892">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c003ad7ec2.mp4?token=d-RtZcNGlxHO_lp9wyyiHV8oCkXWlznjvejuOnCeLrkpJ2jeOd9QzH9EF0BIAcFl8flbRd1h6-2pyVCCg4IHSwWVbXXsft2LCsZ7Gw0SXHFHhvwn9eINJb79b4gIEbHaJo8Z4R-Q_YI6Bh_68_GId63R9ONBlbvuvCiA5OrVMSMWpe1uWEQXtM1_worHnHrTztJNigirSZKkqtuWZ25GoSswxIHjF1dJWraHbavUamtB16S__QkXPOz5yYJ8vORzzyctKUD2RMVGkhAa14rGdCVndxpFuoPBL8H8tGAtOK7N8QNJoJxnnCNZHnuItuF5v_uqwDz3K4JK1xx8qJaB6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c003ad7ec2.mp4?token=d-RtZcNGlxHO_lp9wyyiHV8oCkXWlznjvejuOnCeLrkpJ2jeOd9QzH9EF0BIAcFl8flbRd1h6-2pyVCCg4IHSwWVbXXsft2LCsZ7Gw0SXHFHhvwn9eINJb79b4gIEbHaJo8Z4R-Q_YI6Bh_68_GId63R9ONBlbvuvCiA5OrVMSMWpe1uWEQXtM1_worHnHrTztJNigirSZKkqtuWZ25GoSswxIHjF1dJWraHbavUamtB16S__QkXPOz5yYJ8vORzzyctKUD2RMVGkhAa14rGdCVndxpFuoPBL8H8tGAtOK7N8QNJoJxnnCNZHnuItuF5v_uqwDz3K4JK1xx8qJaB6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ: از اینکه ایران پهپاد شلیک کرده اصلا راضی نیستم!
خبرنگار: شما گفتید که ایران آتش‌بس را نقض کرده. آیا این کار عواقبی برای آن‌ها خواهد داشت؟
ترامپ: خب، به‌زودی متوجه خواهید شد.
خبرنگار: آیا آتش‌بس همچنان برقرار خواهد ماند؟
ترامپ: از اینکه دیروز شلیک کردند، اصلاً راضی نیستم. در واقع ۴ شلیک انجام شد که ما ۳ تای آن‌ را ساقط کردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/66892" target="_blank">📅 23:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66891">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
🚨
صداوسیما: صدای چند انفجار در سیریک شنیده شده
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/66891" target="_blank">📅 23:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66890">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">❌
🚨
🚨
🚨
گزارش ها از انفجار در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66890" target="_blank">📅 23:34 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66888">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d178038cac.mp4?token=RUokZ1ZYaSKQcPhM_VqqSgbZXD2EAdTHxaqPF75aKHI3Tf93D2vlG1LymRC5UZqQA1TqYE8o6ifqp-525kaKeaYdEvSp_7SJZDd2QQEc1I3x-awSe4PvXesti8Kia2l0MPlccggbfnurBXpj3Yh2OpoC3w3ELziyi6dRyD6ltEMkx84Fj3qTBKWoI6EG1zOsAW7-W-wNE2wxMbtGAJyvBzkNhRA0rfySO4rLTQmaMpxansRLumP0BRBL3tgxfAfPmKvLepuZ0O_oxCLcWyhH4Xmh-zXJCIY104odkD7OrRZ4Du3ZPAsAiYDyZWWhTiwvtD-POtV3euMO5jWyLdSlgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d178038cac.mp4?token=RUokZ1ZYaSKQcPhM_VqqSgbZXD2EAdTHxaqPF75aKHI3Tf93D2vlG1LymRC5UZqQA1TqYE8o6ifqp-525kaKeaYdEvSp_7SJZDd2QQEc1I3x-awSe4PvXesti8Kia2l0MPlccggbfnurBXpj3Yh2OpoC3w3ELziyi6dRyD6ltEMkx84Fj3qTBKWoI6EG1zOsAW7-W-wNE2wxMbtGAJyvBzkNhRA0rfySO4rLTQmaMpxansRLumP0BRBL3tgxfAfPmKvLepuZ0O_oxCLcWyhH4Xmh-zXJCIY104odkD7OrRZ4Du3ZPAsAiYDyZWWhTiwvtD-POtV3euMO5jWyLdSlgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وزیر مسکن و توسعه شهری ایالات متحده، اسکات ترنر:
خداوند تنها دو جنس آفرید، مرد و زن.
و زمان آن رسیده است که این حقیقت را یک‌بار برای همیشه در کشورمان تثبیت کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/66888" target="_blank">📅 23:17 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66887">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kIvAtVKWQrCTZ79Vzsw2MchdGpUsl9tVnCaUpy2achFD5nKZ9onCI01c2FYfouv19UwYAWJynGpEcNgOwERx0V-M_ZztSOQk_ySL23pgjLJIQvQOT0A7FwHCv0ty975tcjFuCUN72LTJdPsbQ28CjQ-BsrEA-JEmHVi0p_wX_ldOemjsndxvHBWjxJmyoyB-f09_UmQio6xTXO9STIxSrggjIZbpI2w5UC14JOaO8J1xEb36k6cPDqg2j2QJOd1ep2zO_CPAWaj3hZZOtJGEFG87qWOb040vXu6iOzHYCtMw3GEvkYC3INCWO2llEkkYrBCO-fR7o6r1hgDehEzsfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 380 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری واقعی
✅
مناسب برای گیم
✅
تحویل آنی
❗️
پشتیبانی 24 ساعته
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66887" target="_blank">📅 23:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66886">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4fe545d1f.mp4?token=ml0SsmA39C9oFX36l76J6O9u5O3ORgjSRv_6Scp5YtHW9dzlFjYXhObDyiiyymloIAQwb8jj2Lc4ODOQT7vtdvTl0Mw9BPCmknvHQAAzfN92uQLsoMgShbpEmae7_jDBKQCJ6vWJONwZv0Rx3tpKugPgZUGPwaXswzaLyFSQeuoQaH3gaNE6AQV6Y59tYXcnSZx-ELfoPbGeEPZRfu6QSx6wVjPgABUhc89dHNt6_MlG2E8NptD59mD1A8Jru3nttWRxiFHhtYPs9aiE9PFKeXz7ZnICPEn6TQbR5_LhwbreZFPGNk8wSkOXaM06aGWXwKlevAbzZohJqEyLKME3xA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4fe545d1f.mp4?token=ml0SsmA39C9oFX36l76J6O9u5O3ORgjSRv_6Scp5YtHW9dzlFjYXhObDyiiyymloIAQwb8jj2Lc4ODOQT7vtdvTl0Mw9BPCmknvHQAAzfN92uQLsoMgShbpEmae7_jDBKQCJ6vWJONwZv0Rx3tpKugPgZUGPwaXswzaLyFSQeuoQaH3gaNE6AQV6Y59tYXcnSZx-ELfoPbGeEPZRfu6QSx6wVjPgABUhc89dHNt6_MlG2E8NptD59mD1A8Jru3nttWRxiFHhtYPs9aiE9PFKeXz7ZnICPEn6TQbR5_LhwbreZFPGNk8wSkOXaM06aGWXwKlevAbzZohJqEyLKME3xA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ:
کشته شدن سلیمانی یکی از بزرگترین اتفاقاتی بود که تاکنون در خاورمیانه رخ داده است.فکر می‌کنم خامنه ای و دیگران در ایران از کشتن سلیمانی توسط من خوشحال بودند.
چون آنها هم از او می‌ترسیدند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66886" target="_blank">📅 22:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66885">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🤯
🇲🇽
پشماتوووون فر بخوره؛ یه‌زن مکزیکی برا اینکه شوهرش رو سوپرایز کنه و بلیت جام‌جهانی بخره، یک هفته قبل مسابقات عکس پاهای خودش رو‌ به مردان کشورهای مختلف می‌فروخته و از این طریق تونسته درآمد زیادی کسب کنه و علاوه بر کیر زدن به مردان هول خریدار، شوهرش رو به…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66885" target="_blank">📅 22:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66884">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l9aaPmD8ku8QCo40rkUEq905DJ2ziQVyszLEUyicimOw6V8amyCfeYV7tGEHA5OhmlnE8C89S9TIPohj962MKvDZNQMk6gizwKprQHRuB5y4QGhTDAYF2r5T4p0JS4A4vQUQBIWxMFgQMay41IPPdeCgUM0bPscHOcgWb8nTXeXHU5x3tlTS5fvoki7WDL9xPHQbvl5DtmTdEQBjQ2zsoJAG3U7fc6_xdmbBt9IyDKIY4lcxjjsEL64j01qYPmr3ilhGLPVwKwAWuZCrNnKXMqW8GOAlNbUL74IlqzJcNoG2Ew7Y5z3719QT0B9SBZDOTiKiM4vB6pkO7WMaTVB2ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
رئیس کمیسیون امنیت ملی:
به سران شورای همکاری خلیج فارس هشدار می‌دهیم، قمار بر سناریوی آمریکا، ثبات و امنیت شما را بر باد خواهد داد.
دیدید که پایگاه‌های نظامی آمریکا در کشورهای‌تان چگونه به جای تامین امنیت، به منبع تهدید بدل شد.
قدرت موشکی، پهپادی و همچنین مدیریت تنگه هرمز، خط قرمز جدی ایران است.
تنها راه تامین امنیت منطقه، فاصله گرفتن از امریکاست.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66884" target="_blank">📅 22:17 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66883">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bda20ad94.mp4?token=m5rtOOSHjGo_qsmINgYR6AShuInQEa9KJuGxwRXNae6cIfd66Urf3271qR22nB4Hca79Iso2ojenelkXefslgX4zLzGrlFskPdwG3NGANTSgOdolVNWwJXcpwH5C-1EwRYjkDVvWbiYk1EIaoqDVthbnrlYmibKqrcCbHUkG7NTiZUs5UGRg7YPEnBdwblogeeo6LixGR3SaF5cOQUI4C095K013srVYlQg2Mgfysyzw-2GZLuTTMryaekfbBuknSSauUS2iewkN3X2-CRmbcD0J-s7BopQQgD4vCXqRUIuZFkwc90s7juA6AZsHjsGQbqdEwlJFO3eGJGgcmFE5bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bda20ad94.mp4?token=m5rtOOSHjGo_qsmINgYR6AShuInQEa9KJuGxwRXNae6cIfd66Urf3271qR22nB4Hca79Iso2ojenelkXefslgX4zLzGrlFskPdwG3NGANTSgOdolVNWwJXcpwH5C-1EwRYjkDVvWbiYk1EIaoqDVthbnrlYmibKqrcCbHUkG7NTiZUs5UGRg7YPEnBdwblogeeo6LixGR3SaF5cOQUI4C095K013srVYlQg2Mgfysyzw-2GZLuTTMryaekfbBuknSSauUS2iewkN3X2-CRmbcD0J-s7BopQQgD4vCXqRUIuZFkwc90s7juA6AZsHjsGQbqdEwlJFO3eGJGgcmFE5bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
‏نخست وزیر نتانیاهو: اسرائیل تا زمانی که حزب‌الله خلع سلاح نشود از لبنان عقب نشینی نخواهد کرد.
🔴
«شهروندان اسرائیل، پیش از آغاز شَبّات می‌خواهم خبر یک دستاورد بزرگ برای کشور اسرائیل را به شما بدهم. همان‌طور که می‌دانید، ما در واشنگتن مذاکراتی میان نمایندگان اسرائیل، لبنان و ایالات متحده در جریان داشتیم. این مذاکرات طولانی بود و امروز به نتیجه رسید.
🔴
مهم‌ترین نکته این است که اسرائیل در درجه اول در منطقهٔ امنیتی جنوب لبنان باقی می‌ماند. این یک دستاورد بزرگ است و تا زمانی که حزب‌الله خلع سلاح نشده باشد و تا وقتی که خطری متوجه کشور اسرائیل باشد، این وضعیت را حفظ خواهیم کرد.
🔴
این همچنین ضربه‌ای بزرگ به ایران است. ایران تلاش می‌کند با زور ما را وادار به عقب‌نشینی از جنوب لبنان کند. اما در واقع اسرائیل، لبنان و ایالات متحده به آن‌ها می‌گویند: این موضوع به شما ربطی ندارد. شما هیچ نقشی در لبنان ندارید؛ نه شما، نه حزب‌الله و نه هیچ سازمان تروریستی دیگری.
🔴
نکتهٔ دیگر این است که ما به ارتش لبنان اجازه می‌دهیم تا سازماندهی خود را برای در اختیار گرفتن برخی مناطق آغاز کند. ما دو منطقهٔ آزمایشی (پایلوت) ایجاد می‌کنیم که هر دو به توصیهٔ ارتش اسرائیل هستند. یکی از آن‌ها اصلاً خارج از منطقهٔ امنیتی و در جنوب رود لیتانی قرار دارد و دیگری در شمال رود لیتانی است؛ بخش کوچکی از آن در منطقهٔ امنیتی گسترش‌یافته‌ای قرار دارد که طی دو هفتهٔ گذشته به دست آورده‌ایم و ارتش اسرائیل به آن نیازی ندارد؛ ارتش این موضوع را کاملاً صریح اعلام کرده است.
🔴
ما همچنان منطقهٔ امنیتی اصلی را که خارج از برد موشک‌های ضدتانک قرار دارد حفظ می‌کنیم. اجازه نمی‌دهیم نه حزب‌الله و نه غیرنظامیان وارد آن شوند. این وضعیت حفظ خواهد شد. و مهم‌تر از همه، اسرائیل می‌گوید: امنیت ما بالاتر از هر چیز دیگری است.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66883" target="_blank">📅 21:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66882">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f7by9ovzNCTUuzuvljDnvOkYW3BIh-ojVhpQ5213QTSXuRx0nSVc1c9o1GvDiITFKjIPEQ5EkZ0zpI66cW_0QBczIb1wxO7XOAU4dJ7EdODBQkKBV93MTsuxYttCev_GWcrFgzLGBTENDnFzUoiWWVLH_r7Yugcz8Ajr14hQLU8znLxW6gAgjhAMVT5HlCIPnc6_3LdjKTFaJ9ro-mRduuAIVEtnpgITq1k1aiZfrvIdS-4DIzojBG7yqIvCtt_cZiNMS-SgF1YbGYTGlaTGW0P4HC0PSvjEOl0Jxs0SlrBCYVbcT9VtNLKSfxBKN5V0DAAQ4XVqinONC1olcGYIew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
اتاق جنگ اسرائیل:
اسرائیل و لبنان به تازگی در واشنگتن دی سی توافقنامه‌ای را امضا کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66882" target="_blank">📅 21:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66881">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">‼️
🇱🇧
حزب‌الله تصرف تپه «علی‌الطاهر» توسط نیروهای ارتش اسرائیل در جنوب لبنان را تکذیب کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66881" target="_blank">📅 21:08 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66880">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qTxzdzTtoLPXAaIHb9PrFEI6-5iSWQ9OT1JCraFCsOK5DZIOc3xdjsPF0ccSQmVUuxYiRfzbP77Y7os_IV9VGCQj7p6fz7A6tncHUnylyReY72uUZsEPV2GG-eLpi_8lcyKD4bP1tYHtP3wVyFrG1WJ9xIComITjYmfYvX5C8QH8Gg465v-kaNo9nyQ9sf7R0qTTZ60rYDQpUVF1A-hJWnQH8pxVkEdiHZjsKv7pL8i8kigAkSfefJLcDwdeQs4XOIv8eIQXpYTo2J-eyvR1El59hk4-_apIifb_3U1EYXiMhL4-qlx9N7sICK_DBeoZlneaFTzwVsTienETcMYrbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
باراک راوید اکسیوس:
مقامات اسرائیلی و لبنانی به من می‌گویند که انتظار دارند پس از چهار روز مذاکره در واشنگتن، امروز توافقی کلی بین دو دولت اعلام شود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66880" target="_blank">📅 20:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66878">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E1ulUgHkIey6LMac6kFmh8sSihVumSrPpuzB6_I7_WWcTLKTCUgKn2p2uhrnM8CxsNzrHzw1A2J4CW_K-irYHM2EaVsOQY34cJlVgNASppg6-t3A4YLmJ-tKnV0e-JYwROhBEVJezriL4k8FeN1DweorBr413uZy9UjuUrFxtQ_LX9bue5y2DupfJ9uMBZlwaypxKk8CXAqJBqHSt7-HIhD6Pmc_czEym2tjoAZenl-qmeIgCNassm_KIzoZA8_Lv6DZ7O53uHk1OJS5g3zatQP13trVUJl9KO4y98OTviNwbpT2o3O9pgjrbf3Zqv2gGvWg4yLZlqdlNUBbow_Sqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HOu6j0D43QutiDtS1hXWMSYY7HyOGKwZ9zjacrqo3J18Zk7X3shjTnGnVvo7Ry4xDs_Pp0ALOtbrNJ8nJr_Oq9rPhzX3SMeSnUI5-Rv1X62KGThY-n1fOhat6VtQx13OKAm79agj6uwilIRJJD9a19t5-T-BKMFX--hBCw1wDsROo1UQJYsk2HjBy8dBx-HSIjIkkCgO2k5464tASNGYKeOD19f9YZKk2k9SQRvBmUIESnoHDBipRr37uDjLpPZPvGjEtR5kFX9stpH_fWTM9WhVO3M_vQOOgis7Owghk5rNlGl_4wTuN9UcneovWGSM2RFx3nRxTF-TOb5d4nlPFw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
در فاصله چند ساعت مانده تا آغاز بازی حساس جمهوری اسلامی و مصر رژه‌‌ی همجنسگرایان در شهر سیاتل آمریکا آغاز شد!!
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66878" target="_blank">📅 20:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66877">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lNKGdqSnziT3uHxSf01xFMVaF9hTs4tZ4odrOjXK0XksIlGtHJGNj0KCW2WnS-9g3XUwOpcdc4oYhAOZZfwJjvdzEb4ZGZvuQPG9gfYhzsdevSep3Tso-myCx2iLWX0YB4WTTfm1O7siWP2gZwjvqPa8Y7PNmVPlYAIdoLT4ndPmJx3bVM0sRbqUmTiLSxtafu_yd5TUdEYf08lLoTh_ZjsZOXd1s_ojmwlBHJ7xsTfaY4MMm94ZfR23B05dGJUCtj7-GFxliVAqZ2VXm1GhxQtEq6dZBYBpPpFBucFtJhgkZwPYN3SP7NyqU0oGmYfkBzadkBQ2C2ObTcAWpUL__g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: ایران حداقل چهار پهپاد حمله یک‌طرفه را به کشتی‌هایی که از تنگه هرمز عبور می‌کردند، شلیک کرد.
خسارت وارد شد، اما کشتی توانست به مسیر خود ادامه دهد. ما سه پهپاد دیگر را سرنگون کردیم.
بدیهی است که این نقض احمقانه توافق آتش‌بس ما است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66877" target="_blank">📅 19:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66876">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uf2cATGwsjayOeANy-rPKQpx_7eUDf6X8daybiMrXDgRkhAz_I71aM2ZouRl5GyP3y9fHri0lBeYaS2IkOnOW-bu93qvFx0mejt3H7srkWxZM0UmDb4RHIkLuuFrzquFHhSOgwvQ9hpGITRm2aca8HuCixsFgT5LIzaMTHXfnZ2MjSGrvBMXo7dnxxTEMQeIEumVfkI1a75sMqw4HP9XugFnqcAdoFQcirFi9ArN3OlGb1rkr6O5ndqCuIttkLLz8g0-9TS_4rvFWzEPBucYNRl2D1lovgsjA97JZWAPOQDINuZGRo8Q5eJdZItiJ1x_2O_ZC0w3hF_xVsozNnLr4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بلومبرگ:عمان هشدار داد تنگه هرمز به شرایط پیش از جنگ باز نخواهد گشت، کشتی‌ها ممکن است مجبور به پرداخت عوارض عبور شوند
عمان به متحدان اروپایی خود هشدار داده است که تنگه هرمز به وضعیت پیشین خود قبل از جنگ باز نخواهد گشت، که این امر نشان‌دهنده احتمال اعمال عوارض عبور جدید برای کشتی‌ها است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/66876" target="_blank">📅 19:27 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66875">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LFFytp1dtyWy0luhPq7a0yceBi299hhMiVyYNVhMOVkF_3wyXOo9k1i_-WiyRfvwV9ZhVrJuJEuGoMjJNjikwWF4WbpUPXz2ZNqoaxxMdhMpuJQTjzge_KDpRXpQmDJYl_2eo2lhiJ4iomfYBhMd9okyeP6GcGL0fD9ZB7uEJfESM6PltQHq6HtqFIowm8_RZnEKJkDy5I30nSDdM2FgBifhRVssJqb4TkuY20hyf5u4JLvaepN34ZbEj4JXb4DhRiKwvG_en3KIZgo48dMsOmcKjpTGb9V7lwZYeKgvOfw6zYaNjsEw1xRdUjUU_pJpYZ2yojvAGHzsmzFmmvyVbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😢
رونالدو تو جام جهانی گریه می‌کنه؟
پلی مارکت می‌گه ۶۵٪ بله. احتمالاً آخرین تورنمنت ملیشه و دوربین‌ها منتظرن. البته رونالدو رو که می‌شناسی، شاید حتی با قهرمانی هم گریه کنه!
قبل از اولین اشک رونالدو، پیش‌بینی‌ات رو توی 30 ثانیه روی پلی مارکت از تلگرام ثبتش کن
👇
https://t.me/PolyBaaz_Bot</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/66875" target="_blank">📅 19:24 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66874">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99cd497f75.mp4?token=cUDYYiC5DkE5iVDY9kC4XhE-lEpOn3yJ0xbafBxxqjqJNzZzGPweXYcMg_Z9Y269O0X18w_zYqyzHFyFzks1UqZVr_HOmX752nHn564T5iSSp5knUftZoZgN8zs7wvSa7KO6NAIAuuNbu6I-c0f1NyZTZNYdclvaEDHPFHfy0WollAchjBCEhWHklK9W4tBz3ISIpgXaASZG5NAwdznNVyWRWbWAgdO_x3HQGqQPVmDYNYEXABaWafYYDB72ozDgVqDs9kJ2b-ixmX4Jq5fdiAqaLuNWE_fFzGHpjWDZT7p0JatlgFNEfqb5Dma24DLKi-NNDo14NAM1hlNV3TWGhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99cd497f75.mp4?token=cUDYYiC5DkE5iVDY9kC4XhE-lEpOn3yJ0xbafBxxqjqJNzZzGPweXYcMg_Z9Y269O0X18w_zYqyzHFyFzks1UqZVr_HOmX752nHn564T5iSSp5knUftZoZgN8zs7wvSa7KO6NAIAuuNbu6I-c0f1NyZTZNYdclvaEDHPFHfy0WollAchjBCEhWHklK9W4tBz3ISIpgXaASZG5NAwdznNVyWRWbWAgdO_x3HQGqQPVmDYNYEXABaWafYYDB72ozDgVqDs9kJ2b-ixmX4Jq5fdiAqaLuNWE_fFzGHpjWDZT7p0JatlgFNEfqb5Dma24DLKi-NNDo14NAM1hlNV3TWGhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قاسمیان:
به تعبیر قرآن باید اینقدر با آمریکا بجنگیم تا صلح پایدار برقرار شود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66874" target="_blank">📅 18:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66873">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jN_uoPsOPvCX34e3OKt58sH9ScV9qC4SeZ6resNuRQEQhhFEdKBousHvRlxkLpFdxV8d_yVE6aBchonZBRU1U1WZu-vglJ0NZF8kEo_lGDAsZPwBkYopXjiTdjKRzkThsujdlIcr0nzWFFwML7Q_KbIK4G8GVJp2kogIkUY5zS9HHcdKv2lsNRXLineYeim8pXiDlw-ifRd2OEXO54OyXehs8bDloBxn6Z6TEVFeOUomvyWhTU-ToGcQ_j_6e5bevFcD8NnCn1gMYyCyn0_cNOyAytf7a86YhDyHsfeKk3atRplW9TtbUgvgZrrQn6WusIvKXA3IkR8QO6I0wwgwRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇱
توییت کاتز وزیر جنگ اسرائیل که قالیباف و عراقچی و پزشکیان رو تگ کرده:
فرمانده نیروی قدس، قاآنی، این روزها مدام اسرائیل را تهدید می‌کند.
به نظر می‌رسد نقش یک جاسوس و خائن خیلی بیشتر از این ژست‌های مضحکِ تهدید به او می‌آید.
در هر صورت اگر جمهوری اسلامی به اسرائیل حمله کند، بزرگ‌ترین اشتباه خود را مرتکب خواهد شد.
نه هرمز به آن‌ها کمک خواهد کرد و نه حمله به غیرنظامیان، هیچ‌‌چیز ما را متوقف نخواهند کرد.
نیروهای ما آماده‌اند تا کار را به پایان برسانند.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66873" target="_blank">📅 18:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66872">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9a88d77cf.mp4?token=rPjBb8ZcuKy-c6iA0O4Zw5MmyCXFaG8sXZmtS1r9tIT6VPRJ8SKNHsFjbXz-4BCZeZvRozg6mSjWiaYqs0uWsr0xY3mtuO7GskZfafHtHrY-J2tl0q8k7a7TpHkl-VbQKb_x-KdC0wMmF4d0Ti3F_Ckzn6De-hNsXruvFs9thvzsyJm6zJiOgs8GAzV0AtByv47ajH7WxoTviDOxnWaNsS_N3jBXLqD2o-DYOz9NJL3mLIiFvXWgVa21f948j66FHg4m4KhSwRUV8T2bX2Z2TsxZR9n_CVeO-PkHPy1yrEA8ztaJCtQdMzJ44UO9cQMtu4A4lWRR57pZS6xTcNS3Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9a88d77cf.mp4?token=rPjBb8ZcuKy-c6iA0O4Zw5MmyCXFaG8sXZmtS1r9tIT6VPRJ8SKNHsFjbXz-4BCZeZvRozg6mSjWiaYqs0uWsr0xY3mtuO7GskZfafHtHrY-J2tl0q8k7a7TpHkl-VbQKb_x-KdC0wMmF4d0Ti3F_Ckzn6De-hNsXruvFs9thvzsyJm6zJiOgs8GAzV0AtByv47ajH7WxoTviDOxnWaNsS_N3jBXLqD2o-DYOz9NJL3mLIiFvXWgVa21f948j66FHg4m4KhSwRUV8T2bX2Z2TsxZR9n_CVeO-PkHPy1yrEA8ztaJCtQdMzJ44UO9cQMtu4A4lWRR57pZS6xTcNS3Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبتای وایرال شده‌ی یه آخوند تو یکی از هیئتای مملکت :
حضرت آدم دید هر عضوی از بدنش به درد یه کاری میخوره که یهو یه نگاه به وسط پاش کرد دید یه تکه گوشت اون وسط اضافه اس٬ گفت این دیگه چیه؟ هرچی دست بهش مالید دید اضافس بدرد نمیخوره؛
حضرت آدم خنجر یمنی رو کشید که کیر خودشو قطع کنه که یه دفعه حضرت حوا ظاهر شد گفت آی آدم چرا میخوای بیچاره‌مون کنی که یه دفعه آدم دید کیرش راست شد؛ بعد با خودش گفت این مال کس دیگه ایه٬ این تو اختیار ما نیست!
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66872" target="_blank">📅 17:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66870">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GSXV6mOxO015lYWV19Oda6pwaW-cJYc9PKGhhQaHxujnXP9U1rA62xaL0jtItD0933XP3VCZe0S6VwNGDO8t8sUflDgS3K3PXLOTcO-WZzitpGeedXa__DZLSqTGjJGSD_Puthvk6urJT_jRrqa8sWUE_7k5rlOjiAu2TO0jsptYNHwN8ccw5pCkTjg9NUroLkP_qIscn6n62GWWGHkfX9iiy4QuMBFrhHq5VVhX3zNgFh2C2UjYk3fIKRtXuS5V9J5H2fkUirHZYVWXJgo5QdkZTPPnOa9vHx0m2LpEnAupbNfJOmcnajTeWGGRY-oZPpz9MWcXvU1TfZ_jZNEebw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FxYJi1B2wfOe-YzzBnZsbeSlO4lH4JUzxjMt9jNT7817CwE7E5504D7pZ58avj9qYk284wEcSwV-2GwGQ9CX__6MGEBMgO348YIGf-OSbXbfVig8GfbLQyxAt1BEHpgmfxfBz-Hfx9K9v6pHL2OI9SGWjkPQRUa02TYbQDEUGz4a_ueFuqLkxt13Uylhm5tnrOS29W0BcHvdJPVaIvn2BmM60sqIfG9ed94AaHitAnMMYzMVu8-Ynp-wRIGFp5Ld8zWkRI_-UA1_5BqFpJd74zCvdNuDQcTI5pmaBtNDNSgKGWKIOWydk1Dx80zN_92pSlzf9C6QrIKletUx2UfCxw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
‏
بر اساس تصاویر ماهواره‌ای که روزنامه وال‌استریت ژورنال تحلیل کرده، حملات موشکی و پهپادی ایران خسارات گسترده‌ای به پایگاه نیروی دریایی آمریکا در بحرین، از جمله مقر ناوگان پنجم، تأسیسات ارتباطی، انبارها و ساختمان‌های پشتیبانی وارد کرده است .
با وجود اینکه پنتاگون اعلام کرده عملیات ادامه داشته و تلفات انسانی ناچیز بوده، این حملات آسیب‌پذیری قابل‌توجه پایگاه‌های آمریکا در خلیج فارس را آشکار کرده و موجب بازنگری گسترده در آرایش نظامی ایالات متحده در منطقه شده.
مقام‌های آمریکایی در حال بررسی انتقال یا بازطراحی تأسیسات کلیدی به نقاطی دورتر از برد موشک‌های ایران هستند. گزینه‌های مورد بررسی شامل پراکنده‌سازی نیروها، تقویت استحکامات پایگاه‌ها و گسترش استقرار در مکان‌هایی مانند اسرائیل است.
برآورد می‌شود هزینه بازسازی خسارات واردشده به پایگاه بحرین حدود ۴۰۰ میلیون دلار باشد و مجموع خسارات واردشده به پایگاه‌های آمریکا در منطقه از ۲ میلیارد دلار فراتر رود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/66870" target="_blank">📅 16:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66869">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60f93beda6.mp4?token=cYFzwv1VVfH9fe_EvyWejNQnyaQ_dVUa43bU4X0pSywDuaxgFvy3hXVG3Oi_gvyzvOYBrvvhZKn_bf-FtT3FZke2sfUPfM_-YMvuinIXV0wuyTwEy3TZoJNh8r4seS7oPpS_jfJGv-od3tg17UMjYSzojp_WqENd2xM_Sp1iTjjomvjtewvgUPALz8DYKEg5AG15WBbO0n1BvpXat1QwLNrsBHSTycnDvkc2Ls2vP1csQkXVNu8w2s1J2EttacYK01QsAFRwV_9YdOW9iKcas1mKi25PhPb4OCAHfpGw21jXrxmeWLDo_HHPYuARNIHwLtW6rIvcE6QCDBWk2Ul6rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60f93beda6.mp4?token=cYFzwv1VVfH9fe_EvyWejNQnyaQ_dVUa43bU4X0pSywDuaxgFvy3hXVG3Oi_gvyzvOYBrvvhZKn_bf-FtT3FZke2sfUPfM_-YMvuinIXV0wuyTwEy3TZoJNh8r4seS7oPpS_jfJGv-od3tg17UMjYSzojp_WqENd2xM_Sp1iTjjomvjtewvgUPALz8DYKEg5AG15WBbO0n1BvpXat1QwLNrsBHSTycnDvkc2Ls2vP1csQkXVNu8w2s1J2EttacYK01QsAFRwV_9YdOW9iKcas1mKi25PhPb4OCAHfpGw21jXrxmeWLDo_HHPYuARNIHwLtW6rIvcE6QCDBWk2Ul6rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🟥
فاکس نیوز:
دبیر کل ناتو  فاش کرده در جنگ اخیر فقط ۵۰۰ جنگنده آمریکایی از مبدا ایتالیا به سمت ایران پرواز کرده اند؛
«اگر ایتالیا را به‌عنوان مثال در نظر بگیرید، ۵۰۰ جنگنده آمریکایی از پایگاه‌های آمریکا در ایتالیا برای پشتیبانی از عملیات “Epic Fury” به پرواز درآمدند.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/66869" target="_blank">📅 16:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66868">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/403bcac56e.mp4?token=IhV4fb4N-pbU-ggrP8nSIygr8y-nD9UZTZfbuZgFqmpZyxOG-f719A7bWOXmSHBPLdtJkvvWASxRFju-oyEql8mR6OJufZFeqQMlpsAtwkN7XN_ICJ2S1ulJ9gjQj3_qdSUehkok5DeJH5gGtw4_kYH0opdeEMpsWT-36KazVK6WK4qdmuWDueZOVEK69-rgHsjt67ln68td1FTH6D3PTwCg0O9wQhIZ9j-3GCihYc-sF2vEqU8GJ0iagC0rqry3VLEwM2yqwNkxNr764Xg4oAQ5Rmg2gKS7jpvq7S1yiP_kil2sjp58W1LbqubF25aWLq7gyp-jpI1WQpN0hvyUjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403bcac56e.mp4?token=IhV4fb4N-pbU-ggrP8nSIygr8y-nD9UZTZfbuZgFqmpZyxOG-f719A7bWOXmSHBPLdtJkvvWASxRFju-oyEql8mR6OJufZFeqQMlpsAtwkN7XN_ICJ2S1ulJ9gjQj3_qdSUehkok5DeJH5gGtw4_kYH0opdeEMpsWT-36KazVK6WK4qdmuWDueZOVEK69-rgHsjt67ln68td1FTH6D3PTwCg0O9wQhIZ9j-3GCihYc-sF2vEqU8GJ0iagC0rqry3VLEwM2yqwNkxNr764Xg4oAQ5Rmg2gKS7jpvq7S1yiP_kil2sjp58W1LbqubF25aWLq7gyp-jpI1WQpN0hvyUjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پاسخ سخنگوی وزارت خارجه به دست ندادن تیم مذاکره کننده با ونس با شعر مولانا:
چون بسی ابلیس آدم روی هست
پس به هر دستی نشاید داد دست
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/66868" target="_blank">📅 16:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66867">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66867" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/66867" target="_blank">📅 16:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66866">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=GQslQ7EerTRkf-lxWdonyTijs2S7AcL4EQ2OQ29w5QQtCNqz2G4Y9Gje16ZuIU_ZziA9ZIg5KnXucv7dfFYUPoXDFyZ1rQSD9GYtmWeQ9Ckan5oU9MH4NR-_CWwfW58aPadyHxD5-F1Nr6NEcbuejSmati187qPMTjYkkPMI1j1uBHiYtSdBms3dBZyjQdCHnnozcMhnN2QcpI4OvI0mfUqmoFqylQ_-19-ZRF7c8KJ0mu1M8lxw4RQdPXfNpw9J8z2wC_ZcvCFs33ykWsqZQn4rS22gzl17PgL-e8cCqy4P9Yh86lmIsnwfMEOryNfJT70QC0q70GEROwY8zBd8-Bi4A6QEfsGWPnIPm4m6J6b-STQlyWOkP9mCBXbXeu9fZT8npt-0B79azw1BkZnDANmoXHpsX5C9hn1NJVzTaIr8hr6qpThZ-IWB4Jt9I7xtecNqWTLf4LllO_rMA6wdxRHDzEFhs0ha9Hx6FLiYnHfkUEjT_azn8loqBo0_XBtao96sVtup2vx35TpjoLCkLPZQqGtELKL2ukHxUUnoX-ftizWwCT2_PTr8qH4eEMNiIZGB_05XlIl9IHXcYPfvdqlVNMKHqWpgmjCiQxR70xLW-vxlSrYlVv1pslngxpKeoh9BqAVssmMyHvBoybDjYeHcbm9l5yRnEWbioZiHpCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=GQslQ7EerTRkf-lxWdonyTijs2S7AcL4EQ2OQ29w5QQtCNqz2G4Y9Gje16ZuIU_ZziA9ZIg5KnXucv7dfFYUPoXDFyZ1rQSD9GYtmWeQ9Ckan5oU9MH4NR-_CWwfW58aPadyHxD5-F1Nr6NEcbuejSmati187qPMTjYkkPMI1j1uBHiYtSdBms3dBZyjQdCHnnozcMhnN2QcpI4OvI0mfUqmoFqylQ_-19-ZRF7c8KJ0mu1M8lxw4RQdPXfNpw9J8z2wC_ZcvCFs33ykWsqZQn4rS22gzl17PgL-e8cCqy4P9Yh86lmIsnwfMEOryNfJT70QC0q70GEROwY8zBd8-Bi4A6QEfsGWPnIPm4m6J6b-STQlyWOkP9mCBXbXeu9fZT8npt-0B79azw1BkZnDANmoXHpsX5C9hn1NJVzTaIr8hr6qpThZ-IWB4Jt9I7xtecNqWTLf4LllO_rMA6wdxRHDzEFhs0ha9Hx6FLiYnHfkUEjT_azn8loqBo0_XBtao96sVtup2vx35TpjoLCkLPZQqGtELKL2ukHxUUnoX-ftizWwCT2_PTr8qH4eEMNiIZGB_05XlIl9IHXcYPfvdqlVNMKHqWpgmjCiQxR70xLW-vxlSrYlVv1pslngxpKeoh9BqAVssmMyHvBoybDjYeHcbm9l5yRnEWbioZiHpCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/66866" target="_blank">📅 16:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66864">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NhlrkRniMrMu-NeeBSjHxr4q2jzQDd8SOCC5rbX7sOvCtae5MMOS2kgEFBOFJw90Obdak8oXQcB_ASSXOeDN1OihpthGj15vWCob_hDmLU-OtFLFC4J6hV3SmnZqFhsvwvsG3Y7b3yBATYUuRk3c3t0O9hrai2LESnoKFfXW9qvmLeRZkMSrEBmrsEhJbxVO3cn8rDHOAT2Peix7eFPK0SBY8XpqOWAN6Opz4HHqlCuREix6nnZPXxaknXTKH5e9ttd1rUU5jOpcCIq_uuXNuNQxxJqRw-LQ50uvR7XwA7HcQ2sMcyXkL7L8Q2I_SqdXLrVQbEIH429n-4fnS3UCZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a41ee6c687.mp4?token=eGORY-wtFguA9_7uZVF5WBrStuTbiLmPjioGNEJyuMO4a8OP8lgTEu3sdhn5qAC1bNRqZvFCUaQFpehD221C5MMJSNzu9F6E9JOgPRfguQ7FBKtOX3hndQh6U1OpgtTX2ByJW4ztTzm_o4IoNmX5Bio0A2pW9CRRW-Bbf1NBG4dLB6QkqypiiJDSNUOsj9Z8G3jr12iy-VFQhV9NoAmuReT0lY_P_cOGydQxkR5kH65it9snD20nljnCNQD5yAfV7th1FlQ9H9k9M3fPPsAaV_CBTggMSnB2n60kF0SLfJH5Pclft17iXtV3uI2cMWtfSLHR_j7Epxi3ER-STRHqfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a41ee6c687.mp4?token=eGORY-wtFguA9_7uZVF5WBrStuTbiLmPjioGNEJyuMO4a8OP8lgTEu3sdhn5qAC1bNRqZvFCUaQFpehD221C5MMJSNzu9F6E9JOgPRfguQ7FBKtOX3hndQh6U1OpgtTX2ByJW4ztTzm_o4IoNmX5Bio0A2pW9CRRW-Bbf1NBG4dLB6QkqypiiJDSNUOsj9Z8G3jr12iy-VFQhV9NoAmuReT0lY_P_cOGydQxkR5kH65it9snD20nljnCNQD5yAfV7th1FlQ9H9k9M3fPPsAaV_CBTggMSnB2n60kF0SLfJH5Pclft17iXtV3uI2cMWtfSLHR_j7Epxi3ER-STRHqfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رسانه‌های لبنانی گزارش می‌دهند که یک پهپاد ارتش اسرائیل، اعلامیه‌هایی را بر فراز شهر منصوری در جنوب لبنان، نزدیک صور، رها کرده است.
روی این اعلامیه‌ها نوشته شده است: «منطقه خطر! دور بمانید! هرگونه نزدیک شدن به نیروهای ارتش اسرائیل شما را در معرض خطر قرار می‌دهد.»
هنوز تأیید فوری از سوی ارتش اسرائیل وجود ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/66864" target="_blank">📅 15:35 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66863">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22157b34b4.mp4?token=YJqe7-lzaSiSlm3qQpcm4HPq4dKB9lozrdo7Nr157fYo1PfkDl4CNfbj2RXBEjqTz8BPhjQtmTBrEf6_kA5I5AB2YX-mpsw0qFOi9xNpHpnabeVJ-AlEgQtsHIsiDiajiTn0F3gSxaY6drk-onV6dKzQFAufeRAM6xtnBGPEq5xApvK_tDxF_KvV6eFLK2Gmmry-GxRsVmfgcZK1M9Sm7D70sm4UGG3K04cnSUH5KJUuH-hBNnATAcN495l7HenH8jO2iCAquPije5pl855C50lNwGxpSZU1pT8lufg6dKXDiXy6XIvoDUxPnXwsthQWETyXBwrNgoq0wmeHOhLcDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22157b34b4.mp4?token=YJqe7-lzaSiSlm3qQpcm4HPq4dKB9lozrdo7Nr157fYo1PfkDl4CNfbj2RXBEjqTz8BPhjQtmTBrEf6_kA5I5AB2YX-mpsw0qFOi9xNpHpnabeVJ-AlEgQtsHIsiDiajiTn0F3gSxaY6drk-onV6dKzQFAufeRAM6xtnBGPEq5xApvK_tDxF_KvV6eFLK2Gmmry-GxRsVmfgcZK1M9Sm7D70sm4UGG3K04cnSUH5KJUuH-hBNnATAcN495l7HenH8jO2iCAquPije5pl855C50lNwGxpSZU1pT8lufg6dKXDiXy6XIvoDUxPnXwsthQWETyXBwrNgoq0wmeHOhLcDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ:
اکثر مردم نمی‌دانند که حرف B در کلمه dumb وجود دارد
😢
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66863" target="_blank">📅 14:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66862">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">⚠️
خبرگزاری فوق معتبر فارس:
درب تاسیسات فردو، نطنز و اصفهان به روی بازرسان آژانس تا زمان رسیدن به توافق نهایی بسته است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66862" target="_blank">📅 14:13 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66861">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bfb3904efc.mp4?token=NZ1Yrw6xqpmCP_kPOkntx332QjvsYqAXghcs3IJCYc9s7HokFiCd6ydL3yt4NPRsynpgT1SfXWo_DU3y8UYUuAVlID_dEuyUt7rZURXJ0yx8oF9SJOKz09j5yZo6td23RKllBvsLRvyvPlwAvIYTLuv1fBbmzX7kg9nFctUo2HG2dPJY7I-YoGTLjbNMWDaw010AZBNX5HtSbOdAKw9q5NnOxOM0KNvVE39UP1Vas4jgCwLp3cs0GGM9HJOfxg_RW23N-cBLUKuvVsQkClAMGIC-DkCGnHy_4znRrXl4OSHSLRYh5oq_NE8wj0UdtLEz3-Uu2VB9f4eSUrmNvM2MYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bfb3904efc.mp4?token=NZ1Yrw6xqpmCP_kPOkntx332QjvsYqAXghcs3IJCYc9s7HokFiCd6ydL3yt4NPRsynpgT1SfXWo_DU3y8UYUuAVlID_dEuyUt7rZURXJ0yx8oF9SJOKz09j5yZo6td23RKllBvsLRvyvPlwAvIYTLuv1fBbmzX7kg9nFctUo2HG2dPJY7I-YoGTLjbNMWDaw010AZBNX5HtSbOdAKw9q5NnOxOM0KNvVE39UP1Vas4jgCwLp3cs0GGM9HJOfxg_RW23N-cBLUKuvVsQkClAMGIC-DkCGnHy_4znRrXl4OSHSLRYh5oq_NE8wj0UdtLEz3-Uu2VB9f4eSUrmNvM2MYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو یکی از مراسمای محرم، شیر تعزیه افتاده بود دنبال یکی از لشکریان یزید، که یه لحظه جلوش رو ندید
🤣
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66861" target="_blank">📅 13:29 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66860">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">❌
قرارگاه مرکزی خاتم الانبیا:
🔴
پرواز هواپیماهای نظامی اسرائیل در نزدیکی حریم هوایی ایران یک تهدید مستقیم محسوب می‌شود و اگر ایالات متحده اسرائیل را مهار نکند، ایران این تهدیدها را تحمل نخواهد کرد و حق پاسخ را برای خود محفوظ می‌داند
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66860" target="_blank">📅 13:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66857">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BZJAmX-2U65z0hiTlZbn6GKOOA1XQQ9UL_wmIg3K3a3L71oLCBzpCuElvWLtynCPjvPTOr-9B6fDbgNm7gJEFWh8T5yrkuOiCEvPjchllBBUSqwjCK66IN4bJYRyLaLz98fnU9am4Wc1oxKpPBo8wLhOk3p7ASuA7tIFIfwKopdUziZLxqLfmrfOjPr0orE5-6nB2C-aS0w2YyLEwlCtBclUXJoGMzY_0B4Lg1QKSYV1g_x4ke93jVgkQKriqIBCA0UkNo_4iLxUcKryCOqPRvu8BGmmj5BCJP76uSV8x4s841dz7jIEXhYCjAQJLJoPQk1sOChrcK_jE0uQkAm3vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FRW-_nOYH8W7tdiiiosw824m1YS8HjsMh3oPIGHjIG_cb4Tt3F1fpXDm5almHG_cWo5awOVv5LOXyKIlSBcBzwRos1FCMaDTNhhZFgUP5TZMld-W1ORKEcsx23Vg2ZfzQbYaN7Spxg0HjhE2IkoN7EG5JVQHh3O7UM4KYH0uGlMLBIogHF4EbaT4HlJfkQcK5KOkJZnaVkMpJxl_Z9TKaMn-mm6cf5Vp6-NWVZCcnpR66j9cigrLg9Z7L4ESgOu_K4LMdozKBhIoX9fHhjAD4v75iK4MBbcfT6C2EFeZjpvhxMo6S2sldgdRiw2OAOLAchv7Cm7dBO3yM4i2ZyID1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M0W1Pxt2pmC1L6g76UosOa90zJ_HUPrScqtQghoMCSCm1H1WMR9iDEASg1ZCDcN9wULgnJibSeEn5OUJyxtgnhGjBejsW9qDgt05ru3bxcCyHIUl5cZOR6Y_RQbLuvOZJfOIDdf7Pz5SQ8igeMTRlOktlc9lAM1nXISni6NZ4oiOvVJPeMIikO4PAopxLq_e01pP2WVDW1bPVbx3KKG1niI0Etb1JnUBoi9MenYZH-KEgh23rxRUEVZpgEUAh3nqFeSZ0AscgqF6FZwmD0noJuIenG0zyLhHm_3GKDHm3ySeFo34reizc2DNz_gvOgaTUbNCc3w9rbPGWBQYqIQO6Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
حملات هوایی صبح امروز ارتش اسرائیل به جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66857" target="_blank">📅 12:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66856">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67fdc892f6.mp4?token=S1PSjKQwHvBuZGB9a7jnuoYcZ2wpcejPNYo5YRD06MLngI4aDJIrOUh3qWSy9hQIACHGxRSHcC9fVFI7nQNVdE5Z_Xr3vQJng00CqCfnenghBh8Inz9TeJWziAkmFx-2H2E-nZhrs6SvQiIAuubyRT_F4s71MNEmoICp8Iz9hWcOdSAfKrV2N5qhpxCjR4pCffHoP9-8pJcKTuoJc504cj93xnq8ff2Ijm0Nr-LVsbSxWUKoD4DOGIJuKXaB_aIvcq0HjjoWvaVg8o3bihBgzOx3IRKUHcs1rf0j1ZY4bhzDkfH60Glc1iZmB7SghSCIbe3J07BdfbsQfExjTS6tMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67fdc892f6.mp4?token=S1PSjKQwHvBuZGB9a7jnuoYcZ2wpcejPNYo5YRD06MLngI4aDJIrOUh3qWSy9hQIACHGxRSHcC9fVFI7nQNVdE5Z_Xr3vQJng00CqCfnenghBh8Inz9TeJWziAkmFx-2H2E-nZhrs6SvQiIAuubyRT_F4s71MNEmoICp8Iz9hWcOdSAfKrV2N5qhpxCjR4pCffHoP9-8pJcKTuoJc504cj93xnq8ff2Ijm0Nr-LVsbSxWUKoD4DOGIJuKXaB_aIvcq0HjjoWvaVg8o3bihBgzOx3IRKUHcs1rf0j1ZY4bhzDkfH60Glc1iZmB7SghSCIbe3J07BdfbsQfExjTS6tMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ درباره ایران:
«یک بازار جدید دیگر هم در راه داریم و آن، کشور دوست‌داشتنی ایران است.
ایران کشور زیبایی است. کسی دوست دارد به آنجا برود؟ جمهوری اسلامی ایران با مشکل تأمین مواد غذایی روبه‌رو است و ما قرار است بخشی از پول آن‌ها را بگیریم و آن را خرج کنیم. همچنین قرار است مقدار زیادی گندم، سویا و ذرت خریداری کنیم و این روند به‌زودی آغاز خواهد شد.
این برنامه هم بسیار بزرگ خواهد بود.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66856" target="_blank">📅 12:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66855">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e_1oosUl2hYcK6SleI0V8qSNF9bUA8r5JoFCfnSKk1QO4UDd_bFwfLCzEJeeRE_tJPxbI1srKZoPpjB5IIqJlzD2LPZz2lIGRPavCgpN-cLR-oJDQdLq-KyhXssPSCBigOqbSDeIMYBZdKhAPW4_qctxAcg_A66qX7r76Y4OCsD1JQhmGQC8sOmphFDuYSEQRbu0x-EsJKEWed9GFUeH6NSzMdvTUopaNoyFBx034bDRorW6O6xSc2qT1aH--P0rJoMGweIEN7jwizJllajv8eC6Q_BT4UOSuQwKjDA5qUxMlywQ1bn8-uzLotGm-8Fuz3Pes5xSoWudMwKTFY-vFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇸
پرزیدنت ترامپ:
روند خرید محصولات کشاورزی ایران از ما خیلی زود آغاز خواهد شد و من انتظار دارم که حجم آن بسیار زیاد باشد.
ما پول ایران رو گرفتیم و بجاش ذرت و سویا خودمان را دادیم!
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66855" target="_blank">📅 11:03 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66854">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">‼️
جی‌دی ونس درمورد ایران:
🔴
آن‌ها دائماً سعی دارند مأموریتی که دونالد ترامپ برای ما تعیین کرده است را تغییر دهند.
🔴
او در ابتدا چه گفت؟ «من می‌خواهم ارتش متعارف آن‌ها را نابود کنم. من می‌خواهم توانایی آن‌ها برای اعمال قدرت را از بین ببرم. و من می‌خواهم تضمین کنم که هرگز سلاح هسته‌ای نداشته باشند.»
🔴
آنچه دیده‌ام این است که برخی افراد سعی می‌کنند بگویند: «خب، این عالی است، اما شما باید هدف متفاوتی داشته باشید.»
🔴
به نظر من دلیل موفقیت رئیس‌جمهور این است که او از تسلیم شدن در برابر آن تمایل خودداری می‌کند.
🔴
او می‌گوید: «ما کاری را که قصد انجامش را داشتیم انجام دادیم. ما اهرم‌های دیپلماتیک، اقتصادی و نظامی باورنکردنی ایجاد کردیم. بیایید از این اهرم‌ها برای کسب پیروزی بزرگ‌تری برای مردم آمریکا استفاده کنیم.»
🔴
این همان چیزی است که او از ما خواسته است انجام دهیم. هنوز تمام نشده، اما تا اینجا همه چیز خوب پیش رفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66854" target="_blank">📅 10:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66853">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aefac4ff7d.mp4?token=HUn2Y-U_NIF_gLzHLAFphcjhfVQyf_TZAL_w_rZkhYMH8U7OIrWl1eFFDCOgVjmNCDEoQOl8bLjvN-onpkVnb1TfFZuzaQ67rLQwTbGL_vepBlC9jUVMowP7YFaqEdB5wWqWrV38dAQT9JikeeH8n2ZSaNpVEdWchCOyLe5PvT1nwCjWAaHzeFu-oCm-KES0CWKwdWfdBtO0qVBDqoUdNfmhS-Iky98yIAS-XntK0EU-Rilpa9txZcj_oCk07ReSOVsCGKRTZslEo_fWLLETK0U4evS3qF-O8wJ_U99SB0YAlC00VPZY-sxwbp317PNK3adcEfPfMlw6lk_Rm9AZ8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aefac4ff7d.mp4?token=HUn2Y-U_NIF_gLzHLAFphcjhfVQyf_TZAL_w_rZkhYMH8U7OIrWl1eFFDCOgVjmNCDEoQOl8bLjvN-onpkVnb1TfFZuzaQ67rLQwTbGL_vepBlC9jUVMowP7YFaqEdB5wWqWrV38dAQT9JikeeH8n2ZSaNpVEdWchCOyLe5PvT1nwCjWAaHzeFu-oCm-KES0CWKwdWfdBtO0qVBDqoUdNfmhS-Iky98yIAS-XntK0EU-Rilpa9txZcj_oCk07ReSOVsCGKRTZslEo_fWLLETK0U4evS3qF-O8wJ_U99SB0YAlC00VPZY-sxwbp317PNK3adcEfPfMlw6lk_Rm9AZ8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎯
ارتش اسرائیل: ۶ عضو حزب‌الله را در جنوب لبنان ترور کردیم!
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66853" target="_blank">📅 10:05 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66851">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73a731d25b.mp4?token=PzrUu3HDUQADRBH3CBmQRW5wZEmaVYG19t-6IPWjx6dRrEeoywJ9VQGOcX7QxJ62B0fW8EzfBaemnhy83ihKJbxIXGg83xRY3w6GXzhl8e-nX9q61XUHtHbPtQiWORTA4AkNpCifJNyr3anDWaOHlNEGqqHkVvkE4OqZOwecH-Yr9PVKlqv1fJvSLqkq7fjEs6d_c69DpKsnNO7oH7EIA0mwX0BLeA4UH9JAuJOTsXQRITYHmaxV7Z5UckEf1d5kQWrUtlbAHQf0TDWsknIPZV3YDC579aebeE2AZyIZ_JQU1nsgE_yIyCIgcXVxuYDOmO2qKnx-adLtYgPxgIfvMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73a731d25b.mp4?token=PzrUu3HDUQADRBH3CBmQRW5wZEmaVYG19t-6IPWjx6dRrEeoywJ9VQGOcX7QxJ62B0fW8EzfBaemnhy83ihKJbxIXGg83xRY3w6GXzhl8e-nX9q61XUHtHbPtQiWORTA4AkNpCifJNyr3anDWaOHlNEGqqHkVvkE4OqZOwecH-Yr9PVKlqv1fJvSLqkq7fjEs6d_c69DpKsnNO7oH7EIA0mwX0BLeA4UH9JAuJOTsXQRITYHmaxV7Z5UckEf1d5kQWrUtlbAHQf0TDWsknIPZV3YDC579aebeE2AZyIZ_JQU1nsgE_yIyCIgcXVxuYDOmO2qKnx-adLtYgPxgIfvMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قالیباف با روسری و ماسک اومده بوده هیئت
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66851" target="_blank">📅 09:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66850">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cff13197ee.mp4?token=mudW1OoQcrRnAjq14g31VcEt4v88pRrvdqmMCCQmCbXwzf_U6_ZvW3n0-RFqv1Dxjh6xl97x5qT18X4M6AMGgTezgfayDfNK6bF6El2JfJk902hIx87wlKJH2UWZE1Qa0FCrsq-AS2HYbkS5el0v_1urQUpV0eG-YDLNB1BcxgHl_8PZCbo7Z7JKS7mo6kMfLQStNQCFtPsy0ThVLEumfFunuu3mA4ZMjNwYNX46VKClXrck97W-l_N_x3XC_ZyeeWmrvT-SD3U_MGL0P4X3xayEc__eRoZPB0Ea7_dp1UE5VWjK7rKqCkakcV_M3T3zw3C-B4zp0AobabsMgyel2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cff13197ee.mp4?token=mudW1OoQcrRnAjq14g31VcEt4v88pRrvdqmMCCQmCbXwzf_U6_ZvW3n0-RFqv1Dxjh6xl97x5qT18X4M6AMGgTezgfayDfNK6bF6El2JfJk902hIx87wlKJH2UWZE1Qa0FCrsq-AS2HYbkS5el0v_1urQUpV0eG-YDLNB1BcxgHl_8PZCbo7Z7JKS7mo6kMfLQStNQCFtPsy0ThVLEumfFunuu3mA4ZMjNwYNX46VKClXrck97W-l_N_x3XC_ZyeeWmrvT-SD3U_MGL0P4X3xayEc__eRoZPB0Ea7_dp1UE5VWjK7rKqCkakcV_M3T3zw3C-B4zp0AobabsMgyel2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
فرماندهی مرکزی ایالات متحده:
جت‌های جنگنده اف-۳۵ بر روی ناو هواپیمابر یو‌اس‌اس تریپولی  (LHA 7)، ناو پرچمدار گروه آماده آبی-خاکی تریپولی/یگان سی و یکم اعزامی تفنگداران دریایی، در حال برخاستن و فرود هستند. ملوانان و تفنگداران دریایی ایالات متحده در دریای عرب در حال عملیات هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66850" target="_blank">📅 09:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66849">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">میخوای به راحتی از فوتبال و باقی ورزش ها کسب درامد کنی؟!
⚠️
پس همین الان وارد کانال @Palang_Bet شو چون بهت اموزش میده چطور دلاری پول دربیاری
❗️
💵
اینجا میتونی روزانه درامد داشته باشی و سرمایت چندبرابر کنی @Palang_Bet     @Palang_Bet</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66849" target="_blank">📅 02:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66848">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TYYlzJ8y6dABYE4GP43mpxF-QNwj-gOrTKt5MbZTQH58xKaRVWMFC42h7jHYWsq67Jpu8VegPg7hPeb0zjMV1YB0Vd050iTJ-xTucXlDwzeYL33H-6qoIaQ1WFeo8ngWhmvR0A9ttAb4Xi_qtR9uxIIM__S7yms4AFLkVQHU_FIy423LN5aikcXJjiinsAPBoou94wzU2B5VADiUNxysZwMkiukk5HLBdts7FaYTLMi_LsNXXJX9mWS6buXhr5az_Xlhpldc9CiGVQ_ZCg00cEGoTbFZdv0B9nSVNSwMMyPcEQ-FxBsn6YEsU2OJgxN1sb7gbrnIvvCn4if919BuuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میخوای به راحتی از فوتبال و باقی ورزش ها کسب درامد کنی؟!
⚠️
پس همین الان وارد کانال
@Palang_Bet
شو
چون بهت اموزش میده چطور دلاری پول دربیاری
❗️
💵
اینجا میتونی روزانه درامد داشته باشی و سرمایت چندبرابر کنی
@Palang_Bet
@Palang_Bet</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66848" target="_blank">📅 02:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66847">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UaAU4J9kF54F6-rT4sUWGjgZRh_8Ld_46UI8eDLRsiwWEKGmoo_zuoEF4Cuj74wKtw0NX2jWps2iZQSNPuYf_x5DeXutJe-rQIm35IwptJ17SDLhLPKFHXYpJ8fsLJqoD7gZdHPVC2q2gAiJAF8Hl9jrq044VulEch-86Z5PculQ-SBak7wbH33lbuSK8UwdRRkWEKXJByd9obWQUxLAcmnRTXJ_ryr1AfELSWoY0Axa61Hs6Pd971jemDQnWIQfuZh_ZWeNZEgaqyAEYwAOukJGoy3srvYEwAcmdwsWTCPHV7cCGlNx2TDB75H6V4gV12xBK2c5_UkTJH5VjxDvIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏بر اساس گزارش وال‌استریت ژورنال (WSJ):
🔴
ایران روز پنج‌شنبه به یک کشتی باری با پرچم سنگاپور در تنگه هرمز حمله کرد؛ اقدامی که به‌عنوان آزمونی برای توافق هفته گذشته میان آمریکا و ایران جهت بازگشایی این مسیر حیاتی کشتیرانی تلقی می‌شود.
این حمله به پل فرماندهی کشتی آسیب زد، اما هیچ تلفات جانی در پی نداشت.
این حادثه چند ساعت پس از آن رخ داد که ایران به کشتی‌ها هشدار داده بود از مسیرهایی که مورد تأییدش نیست استفاده نکنند
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66847" target="_blank">📅 01:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66846">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">رسانه های اسرائیلی اعلام کردند طی درگیری ارتش اسرائیل و نیروهای حزب الله در منطقه بیت یاحون در جنوب لبنان چند نفر از سربازان ارتش اسرائیل از تیپ ۷۶۹ مجروح شده و با بالگرد از منطقه تخلیه شده اند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66846" target="_blank">📅 00:57 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66845">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">با بحرانی تر شدن وضعیت ونزوئلا و مفقود شدن بیش از پنجاه هزار نفر گویا به نظر می‌رسد مثل زلزله سال ۲۰۱۰ هائیتی که ایالات متحده آمریکا به این کشور نیروی امدادی/نظامی ارسال کرد دولت ترامپ هم به سمت همچین سناریویی پیش می‌رود.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66845" target="_blank">📅 00:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66844">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
وقتی نت ملی بود ، تنها سرویسی که برامون قطع نشد همین بود
🔥
🔗
@Kaviani_Vpn
🔗
@Kaviani_Vpn</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66844" target="_blank">📅 00:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66843">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CO3tVJdrHul1q-lB_SLgvRdG6BsxPPwD_PEoKNtVawjZIN0H3ewssT7WWwx02perJQm3Qgxus7Ka4LKqEZ1o1EJLM9u0QoYsxL8ZCb1TsrJtsy0Wm1fVep0Rton99kN3reeU7Kn88_2fze7LWejhKZWOBdOIR6rfUUwtUj0EYBbsw0khbWQiuMOAGQXq2SQo7bPzUpviXiZE2gMvW_BBiYMPXrf1Fq03a-UTU4qKInVlCy_AnIFgPn8O2hvuutHZniDouF5k5NLT_ki_it77iqW8TDM4EZAtQN8gjmIl0UHOaskGX1dVu7EYVHL8F7QUgHgO9ut99zjNRlHMPy2I0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
کانفینگ نامحدود برای همه اپراتورها
🔥
⚡
سرعت بالا | بدون قطعی | تحویل آنی
💵
یک‌ماهه: 380
❗️
پشتیبانی 24 ساعته واقعی
❗️
✅
سازگار با تمام خطوط
🚀
اگه سرعت مهمه، همین الان پیام بده
🔗
@Kaviani_Vpn
🔗
@Kaviani_Vpn</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66843" target="_blank">📅 00:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66842">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RwFJNJKPIE6oZTSN1Fe2Zs0je3IDQnqVDqWpLwxoPKFN3cTzJHp9sgZ9B3hy1vV4kE8fWTvHrlppDkcsAf8h1YnqhRt-QIYKasSWqifibmD3lP41nNZJkmC05WRt_z7-SrKTof2uvme7MlyozSG3bEEwQ_bRzD4_WzLqLN91TV1hjE2jImyTjc7rPaemAURAlp2-Eo5pcKAsQTWdfPQUBNkBlDr-5nNpXcQMpDX8YyX0FHB4AwfBi_s9P2RGJtwnolhpRTrI055VMtNge3sDarVKu69bA_eQZxDZoQ4Br407U33KFvLB6K_INqy2WLWAv5R26nr6m1pAJ_y4dVfEvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
گزارش از لبنان: جت‌های اسرائیلی به بیت یانون در جنوب لبنان حمله کردند.
این پس از تهدید امروز سپاه پاسداران علیه اسرائیل صورت می‌گیرد
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66842" target="_blank">📅 00:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66841">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b6d00bedd.mp4?token=Bl1CTPgAbCQSuIKHI03AKN39vmfpivKAjjhLLQT9Tr_pMjKjZu8alwHAM56hdO4_B4d8E8Sm2QNgXXldpBj2HweGunVzjrbVM4Vkfljy7FAJwuLDxCi9qg4Al7hsG2i4O1B9Sutq7RAyQP0tShHLpzHZRDp_O0rQy-lsmASl-ZEXIcQLXaswZLe9r2d4pDGfXCkrwrnRQ2Jx3uLXkj869Oprqbs9d5tEIL-Vypnw0ZTcM1NDni_34IzsXEN8MNwdfad-Qf7HadyX9M5izYg8cVbRhldaS22rmQ9FJpIOPY52QkD79KVjd8KEs6JqwQxgjrpEaUnrXh2az9xx12EfYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b6d00bedd.mp4?token=Bl1CTPgAbCQSuIKHI03AKN39vmfpivKAjjhLLQT9Tr_pMjKjZu8alwHAM56hdO4_B4d8E8Sm2QNgXXldpBj2HweGunVzjrbVM4Vkfljy7FAJwuLDxCi9qg4Al7hsG2i4O1B9Sutq7RAyQP0tShHLpzHZRDp_O0rQy-lsmASl-ZEXIcQLXaswZLe9r2d4pDGfXCkrwrnRQ2Jx3uLXkj869Oprqbs9d5tEIL-Vypnw0ZTcM1NDni_34IzsXEN8MNwdfad-Qf7HadyX9M5izYg8cVbRhldaS22rmQ9FJpIOPY52QkD79KVjd8KEs6JqwQxgjrpEaUnrXh2az9xx12EfYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار:
«شما قبلاً آن‌ها را «دیوانه‌های دین‌سالار مذهبی» می‌نامیدید. آیا هنوز هم فکر می‌کنید این توصیف دربارهٔ رهبری کنونی هم صدق می‌کند؟»
🔴
مارکو روبیو، وزیر امور خارجه ایالات متحده:
«ببینید، موضوع این نیست که من باور دارم این‌طور است؛ واقعیت همین است. نظام ایران توسط روحانیون، یعنی روحانیون تندرو، اداره می‌شود. همیشه هم همین بوده است... البته در بخش‌های سیاسی حکومتشان هم افرادی هستند که ظاهراً انعطاف‌پذیرترند یا تمایل بیشتری برای همکاری با ما دارند. ما در حال مذاکره با همان افراد هستیم. باید ببینیم نتیجه چه خواهد شد.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66841" target="_blank">📅 00:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66840">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/345e633380.mp4?token=nh4n-1zgt-T8zSM1u27E7X7MfwkEs7-KEqfOJHzNgMCjVU9ChZRYutekJAGtyb5gq7Ow5I7LiMQ3Qcyfnc2sHLvkZ4XRtoZ-31NL5C39kqaUpPs3eAo_ViXCmhwd91Hjzj3X9Ifr_qgcA_oLvCYZfB-nuvjTQcu18E0z78KN5fjAyMKdiBY7lTktVojKfpguf5uonE3iI3otsSleewJzPLT5f3Ah9qcZKIHUeCmBlkH5qI385RKnuBqFIl004FB_DF0olnNhoUYWAyQpb-h6n-yOtArgvAYZpy6qE1uMEI0yS4t0sUXYQXfaKR7pmr29SrYW972r-PK738S0uWihfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/345e633380.mp4?token=nh4n-1zgt-T8zSM1u27E7X7MfwkEs7-KEqfOJHzNgMCjVU9ChZRYutekJAGtyb5gq7Ow5I7LiMQ3Qcyfnc2sHLvkZ4XRtoZ-31NL5C39kqaUpPs3eAo_ViXCmhwd91Hjzj3X9Ifr_qgcA_oLvCYZfB-nuvjTQcu18E0z78KN5fjAyMKdiBY7lTktVojKfpguf5uonE3iI3otsSleewJzPLT5f3Ah9qcZKIHUeCmBlkH5qI385RKnuBqFIl004FB_DF0olnNhoUYWAyQpb-h6n-yOtArgvAYZpy6qE1uMEI0yS4t0sUXYQXfaKR7pmr29SrYW972r-PK738S0uWihfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مجری:‏بهای بسیار سنگینی.
رئیس‌جمهور ترامپ این جنگ را آغاز کرد،
و وعده‌های بزرگی دربارهٔ تغییر رژیم داد
و وعده‌های بزرگی به مردم ایران داد.
آیا ازنحوه‌ای که آن را به پایان رسانده،ناامید شده‌اید؟
شاهزاده رضا پهلوی:خب، نمی‌دانم هنوز تمام شده یا نه.چون همان‌طور که می‌دانید، هر چند ساعت یک‌بار ما یک توییت متفاوت از این
رئیس‌جمهور دریافت می‌کنیم و ناگهان موضع
از یک چیز به چیز دیگر تغییر می‌کند.
بنابراین من خیلی به هیچ اظهارنظری
که مطرح شده، وزن نمی‌دهم.
و در واقع، من فقط، می‌دانید،
کمی دنبال می‌کردم که
در به‌صورت زنده چه می‌گذشت.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66840" target="_blank">📅 00:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66839">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">#فوتبال جام جهانی فوتبال
📊
2 گل آلمان و ساحل عاج  کد:YXA6P ضریب:2.3
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
دانلود برنامه ملبت @Palang_bet</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66839" target="_blank">📅 00:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66838">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f455bc9393.mp4?token=eysE8H9RDwZhMKlCAS1lM0b6Xdw1Ck_GdAiEqjKXWTunpV80lzLk-hx25CRx7ZNIjtc114ds7FNxWDiWmPwZTQ84siY5smIoSjYUSuRPUNP92SDg5nXJuXIPdjzhLx_jEFmpuVf7p6lYGBmNPXhX2MeRF0pnUiQG54JoVNLsCMwCn6V73f4fcUSNTgSx-okgt3Phfu2QNsI-3JyuaqMat-QoE7IXGkuC_g9hmq2a7Di2Y_qejurd7D5g0TX4iPxmuM1bYBzA0KNq5n6AEqu7mhuU6JZJQdtwLznKuNqar_iKPI06sIcNyn4Oehq_QdnwPWb-y5X_v1EhyXD8wu4Kpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f455bc9393.mp4?token=eysE8H9RDwZhMKlCAS1lM0b6Xdw1Ck_GdAiEqjKXWTunpV80lzLk-hx25CRx7ZNIjtc114ds7FNxWDiWmPwZTQ84siY5smIoSjYUSuRPUNP92SDg5nXJuXIPdjzhLx_jEFmpuVf7p6lYGBmNPXhX2MeRF0pnUiQG54JoVNLsCMwCn6V73f4fcUSNTgSx-okgt3Phfu2QNsI-3JyuaqMat-QoE7IXGkuC_g9hmq2a7Di2Y_qejurd7D5g0TX4iPxmuM1bYBzA0KNq5n6AEqu7mhuU6JZJQdtwLznKuNqar_iKPI06sIcNyn4Oehq_QdnwPWb-y5X_v1EhyXD8wu4Kpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مفقود شدن بیش از ۲۱ هزار نفر در پی زلزله‌های ویرانگر ونزوئلا
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66838" target="_blank">📅 23:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66837">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lr2pT94gWz-JmBR3qUNa2Vfh1lIPpGR7UzAgpnn4y3KpPOYzG8dmPuUcLWOw9MwNQGVAhnFHAX_tVuKrJmup0T7WNmb8BDeoDfi7Z1wFxQ2W9UxLxxSYV_XFsK0AE-9aM6EEGzVLnNoJqLaYFjrsBRYf6_jkd2YONPv6J9MuuJf1YPFQ0PsiMrhzLWXE2a_Kewlei3HID1VV1GzJjHZBS7AUAOjvd6PgNhbPA4qtSm70qg2MrKf8u9VMXai2iLEMSf1AtZnSjlwAeaFicZcOSkzjEdVI67j149YW5wnXt8gKvI4KnNn43iVMciIpRPOF__nYfm2jbMtCtGwl3sHt1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عراقچی:
پس از بیانیه مشترک اخیر در مسقط، تماس تلفنی سازنده‌ای با وزیر امور خارجه عمان داشتیم. ما مجدداً تأکید کردیم که ایران و عمان «برای تعریف مدیریت آینده و خدمات دریایی در تنگه هرمز» گفتگو خواهند کرد. ما مصمم هستیم و این کار را با همسایگان خود انجام خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66837" target="_blank">📅 23:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66836">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eab5d7e42e.mp4?token=meo6mBnrqtpu3qkFR5hAqsEGCvuM6hIBfn8Xlzwrf0Hke2ruwYvHAWum95oQ-D6eG56whwrLn4bQlXV41f6GZo1xPai91qY-gGREg9x55NEQrt_qJHpwbW5hwGqE6Nsscc5o9j2SuMM1ImYfEDPrUQ4IvltTXjm4edyoNoWwfLAwcwOhUGc2axF1YWFWMBTDSbttrhFHe0Ndo3NhwYlRNu7MBJ0vwL1B4OUBfv8-2AlvhtE4DjaIZpwun_ya_a2P6BVd0vIXBtG-QKz_yQlTREL5arrj8MGm-ZJj5SwTw022nA8zcjtnjDr6jYCtnfDqjLz_rYx39xUgD86R3uz1fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eab5d7e42e.mp4?token=meo6mBnrqtpu3qkFR5hAqsEGCvuM6hIBfn8Xlzwrf0Hke2ruwYvHAWum95oQ-D6eG56whwrLn4bQlXV41f6GZo1xPai91qY-gGREg9x55NEQrt_qJHpwbW5hwGqE6Nsscc5o9j2SuMM1ImYfEDPrUQ4IvltTXjm4edyoNoWwfLAwcwOhUGc2axF1YWFWMBTDSbttrhFHe0Ndo3NhwYlRNu7MBJ0vwL1B4OUBfv8-2AlvhtE4DjaIZpwun_ya_a2P6BVd0vIXBtG-QKz_yQlTREL5arrj8MGm-ZJj5SwTw022nA8zcjtnjDr6jYCtnfDqjLz_rYx39xUgD86R3uz1fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
روبیو درباره ایران:
ما می‌دانیم افرادی که هنوز در بالاترین سطوح آن حکومت حضور دارند، همان کسانی هستند که به همان ایدئولوژی و همان طرز فکری پایبندند که رهبران پیشین آن حکومت به آن باور داشتند.
نظام ایران همچنان توسط روحانیون تندرو رهبری می‌شود.
همیشه همین‌طور بوده و همچنان نیز همین‌طور است
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66836" target="_blank">📅 22:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66835">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd736f47d9.mp4?token=k7aBXrjfeWlxXJKVBlSW7S_Oq3Ltew-hExZ-gUni7LiO1W5ek45AFj11gFrQHEEEytavXO0O7kBd_7ph3qgBuHAQfK5mEwLLWTNLgtsDlzPf3r3kjFmZ7paeV3U3q59J1IxSwhKfXwUbiiBk0o2BqUHM6-YDDH9L-NSNAkBZggY5XRJXcKwHwqFv6XSxu82Mv8UT4v6FAqEjpma_-xG12d4zGTIaTfRzfw5jcNs92i3vJqyPontAjIzC1INvLoXCg6_KANQB2kkzIk_Hc-mCyFrle4NOjEpBq5vjE1As-eYme_41gJisoZhBGRdF5eOLDoe-8aNqeufI5GCUOQNdBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd736f47d9.mp4?token=k7aBXrjfeWlxXJKVBlSW7S_Oq3Ltew-hExZ-gUni7LiO1W5ek45AFj11gFrQHEEEytavXO0O7kBd_7ph3qgBuHAQfK5mEwLLWTNLgtsDlzPf3r3kjFmZ7paeV3U3q59J1IxSwhKfXwUbiiBk0o2BqUHM6-YDDH9L-NSNAkBZggY5XRJXcKwHwqFv6XSxu82Mv8UT4v6FAqEjpma_-xG12d4zGTIaTfRzfw5jcNs92i3vJqyPontAjIzC1INvLoXCg6_KANQB2kkzIk_Hc-mCyFrle4NOjEpBq5vjE1As-eYme_41gJisoZhBGRdF5eOLDoe-8aNqeufI5GCUOQNdBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پزشکیان:
نمی‌شود برای امام حسین اشک بریزیم اما در جامعه شاهد ظلم، بی‌عدالتی، فقر باشیم
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66835" target="_blank">📅 21:49 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66834">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h6Ddoly2oFYJ1jvGC5wM9sMNo5RliEZsiMYajr3uOvy6MIkbOx0NOo3zH82kHPkP6tjI9MeOZFrvxJndYbBlg_LtckFVOEPee0awFUniDdQWAWMFD_yYEbNH5aK0HQC9NyPVYfyNCYBxTrd290as-BiDg2ZOAolQXFVisvDEc5vY8WoDn54ifbCGX34GdX1gW5cR9ug79HtibbafsOGZv7f1EAsbSKufE-JhjIlo68UiTKTSfgBjto7LzzSycqTPzeQ22TxMLQ1-ZnC4HhxM6KRFOxBFcqoAuGcbt9NJ5OnljUhVP6paBOn3Gps2IaMb-Q39Rr3_fQ3aRDU3479rbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیانیه پایانی نشست مشترک شورای همکاری خلیج‌فارس و آمریکا:
🔴
تاکید بر اهمیت بازگشایی تنگه هرمز بدون محدودیت و بدون اخذ عوارض عبور.
🔴
تاکید این که هر گونه تجارت یا سرمایه گذاری با ایران باید به انجام تعهدات آن به موجب توافق منوط شود.
🔴
تاکید بر لزوم خلع سلاح همه گروه های مسلح در غزه.
🔴
تاکید بر ادامه حمایت از دولت سوریه در بازگرداندن خدمات، فراهم کردن زمینه های بازگشت داوطلبانه پناهندگان سوری و مبارزه با تروریسم.
🔴
مذاکرات لبنان نباید به نتایج دیگر نزاع ها مشروط شود
🔴
حملات متجاوزانه گروه های شبه نظامی مورد حمایت ایران در عراق علیه کشورهای خلیجی محکوم شده و از تلاش های دولت عراق برای حصر سلاح در اختیار دولت این کشور اعلام حمایت شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66834" target="_blank">📅 21:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66833">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/965348f417.mp4?token=ZNsyu2t1_Y7cxRhrgTpyzy0tVRepmXpdqPpMiswLB9pbqP-5U9jUFx44y8SRGBq_7MAGVso3qqLNXO2YDLCWWehA2AIwlw8rd4Q8mXVu29Ytq2ALBUDix5SOVRVFagCrJW9uYEntFPaZ4pa6iAu3BPZnKmQfRyucKypR9SRhCjzCwSR0G0bv1r2Ud-8PMvZP70JxymO-rRFDTUA7UbK9oFfL-hHu3_6Wje5V3qQ-05b_l9-3XsJ5yMNudvFOqw8j7ktVycriKqennudVBiKXhzxyIirPKWtBnNwjEzNXYUNQWVHdY7-dscu3gRABSiEJTgnr3C8Xe_pk2JOL5XTjqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/965348f417.mp4?token=ZNsyu2t1_Y7cxRhrgTpyzy0tVRepmXpdqPpMiswLB9pbqP-5U9jUFx44y8SRGBq_7MAGVso3qqLNXO2YDLCWWehA2AIwlw8rd4Q8mXVu29Ytq2ALBUDix5SOVRVFagCrJW9uYEntFPaZ4pa6iAu3BPZnKmQfRyucKypR9SRhCjzCwSR0G0bv1r2Ud-8PMvZP70JxymO-rRFDTUA7UbK9oFfL-hHu3_6Wje5V3qQ-05b_l9-3XsJ5yMNudvFOqw8j7ktVycriKqennudVBiKXhzxyIirPKWtBnNwjEzNXYUNQWVHdY7-dscu3gRABSiEJTgnr3C8Xe_pk2JOL5XTjqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو:
فقط یک آدم کور می‌گوید هیچ دستاوردی وجود ندارد. دستاوردهای عظیمی وجود دارد.
من همه آنها را فهرست نکرده‌ام چون می‌خواهم شما را نجات دهم. شما اینجا زیر آفتاب سوزان ایستاده‌اید - فهرست کردن همه آنها زمان بسیار زیادی می‌برد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66833" target="_blank">📅 20:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66832">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B7KNNm-mvBvCDW0EFnoB6VUOIi3l5lZZB35rPB1NAYyKpwYkvsl6Cf9978mLjlmIkTFc8e-su5ndR1rCzgiKTwEaP65EuqscA0VXVXoPdT9OEDMhnB6s9K2zheI6_czfUz6OIegNlvUALJyYjSpMw-Ve3VdJPS29cIXXmfxl0dLqmJw6gvBrfIeYKeR5WNdLP1fBPSr9YdVC8kgH0ok3tSscRxKJIdwSgDuapmuT4wiFoFLlNZgXoa9jp5otlTCKYtWHeh0BwEp_OsD0zhHigl3A0xiqzSAXs1gPHKg6Rw8BGGG0YHtbbzMuHO2C8hbhfJiOgsmpVwg8fabzIqk7rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عراقچی:
با نهایت تاسف از وقوع زلزله در ونزوئلا. مراتب تسلیت خود را به دولت و مردم ونزوئلا، به ویژه خانواده‌های قربانیان، ابراز می‌داریم و برای مجروحان آرزوی بهبودی سریع داریم. جمهوری اسلامی ایران با مردم ونزوئلا ابراز همبستگی می‌کند و آماده ارائه کمک‌های کامل است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/66832" target="_blank">📅 20:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66831">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">این آمار فقط مال روز اول جام جهانیه
🔥
😤
میخوای از پیش بینی فوتبال پول در بیاری؟!
⚠️
تو پلنگ بت جویین شو بهت آموزش میدم چطور پول دربیاری و تا اخر جام جهانی سود تپلی بکنی
❗️
اینجا میتونی روزانه درامد داشته باشی
💵
🔥
@palang_bet @palang_bet @palang_bet @palang_bet</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/66831" target="_blank">📅 20:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66830">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VybOb-grC6jwJUOMPX-XMjSYbKt1KaKLLsgH4UZLsx3qlGQhKLMW2go7l6tn5rXvsIsMu3GJQqo0vX8yaILbh9On3W6QmJ0x7H1uOTvjRv9iUj_daN0q74mJGZJbLtLvY1udorUx78HsR9B6FeH_lxwqtAqvzTXDljWgyXkCdZlCpWTT586gD7cMdjhSJhF1HrJBQKU8NFjJXd8EHx3QuG4ugw2PJFyUuoft_beWxsAQnkIlupZOKNUQIgIpA3W_vKZdytcwLjNFXcQImKWgpFn0FuLlVvQne0Rpf5RhZrTwFZyvALKznqucZkrOjBPy5ZtGZfVXXdtfj6igvx5SnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این آمار فقط مال روز اول
جام جهانیه
🔥
😤
میخوای از پیش بینی فوتبال پول در بیاری؟!
⚠️
تو
پلنگ بت
جویین شو
بهت آموزش میدم چطور پول دربیاری و تا اخر
جام جهانی
سود تپلی بکنی
❗️
اینجا میتونی روزانه درامد داشته باشی
💵
🔥
@palang_bet @palang_bet
@palang_bet @palang_bet</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66830" target="_blank">📅 20:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66829">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c8c286a22.mp4?token=DJT63-ur9QDwCEAGwjoJbqZzBklD46OicxP0QcmspxdbmsE-a8_zL1kMSfWkMOvUdVdWlIh2mP3fv2ttByahJqFnrjBCVnd5rhLWI82Lov28qGlIwK1KQEgS5Yad_5UolvCMSlV6pmrrbiqqShp5tPnlVKA4Q0NDckE4-tzl3J8JHXxf9J4KdBN6J7cx41aHmDrvXCWmwyX9Qi_fhiq0Y13gV3dmvTEE7OsQWbLHnQbI4S4Zvkm6VrjY1K6um70rJYc4PsziQ2_WuIi8gTzs5JdOTHAIFfOHVqPdmxgdU2iwe2kjQWw1Cq4T0mcemqFtONZMU9I7kbtNlTeVUNTzkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c8c286a22.mp4?token=DJT63-ur9QDwCEAGwjoJbqZzBklD46OicxP0QcmspxdbmsE-a8_zL1kMSfWkMOvUdVdWlIh2mP3fv2ttByahJqFnrjBCVnd5rhLWI82Lov28qGlIwK1KQEgS5Yad_5UolvCMSlV6pmrrbiqqShp5tPnlVKA4Q0NDckE4-tzl3J8JHXxf9J4KdBN6J7cx41aHmDrvXCWmwyX9Qi_fhiq0Y13gV3dmvTEE7OsQWbLHnQbI4S4Zvkm6VrjY1K6um70rJYc4PsziQ2_WuIi8gTzs5JdOTHAIFfOHVqPdmxgdU2iwe2kjQWw1Cq4T0mcemqFtONZMU9I7kbtNlTeVUNTzkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
بنیامین نتانیاهو:
من ادعا نمی‌کنم که پیامبر هستم.
اما فکر می‌کنم می‌دانم چه چیزی بقا را در منطقهٔ ما ـ و به‌طور فزاینده در سراسر جهان ـ تعیین می‌کند:
قوی‌ها زنده می‌مانند.
برای ضعیف‌ها جایی وجود ندارد.
آن‌ها طعمه می‌شوند.
و از میان می‌روند
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/66829" target="_blank">📅 20:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66828">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63d4c620ba.mp4?token=oQjYaDCdsYtGX9MNbr5_tcAHxpCP31_tSCz7i_u2J-1f4HYHoNpvAuNQX18gQsaUQQh4kKhFKnPsR4Oq978U2HCr-yRqKGkKbNkkKmL5OLopVFCOXTzKcXB_FU0Y239TLSUcHG8e55ZdN2wJeRSAv7q6kI6CBBrlAYf7HKvnQa4qtti_sodxWo3ecXmHFhLz_2IRkQfNnB5cg-MTYIE50SOKCp-LC-FlP05K-YcXcGRmCIVr1-a6pS6HZqU96XfIw9B6y_Lw7V1waXZthX4R2rE5BF6Fl2sEcStsE1MHYpn5fW1YhiANramhs82R0q7ooj5hBt7jSP-CQXLr7Y8Fqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63d4c620ba.mp4?token=oQjYaDCdsYtGX9MNbr5_tcAHxpCP31_tSCz7i_u2J-1f4HYHoNpvAuNQX18gQsaUQQh4kKhFKnPsR4Oq978U2HCr-yRqKGkKbNkkKmL5OLopVFCOXTzKcXB_FU0Y239TLSUcHG8e55ZdN2wJeRSAv7q6kI6CBBrlAYf7HKvnQa4qtti_sodxWo3ecXmHFhLz_2IRkQfNnB5cg-MTYIE50SOKCp-LC-FlP05K-YcXcGRmCIVr1-a6pS6HZqU96XfIw9B6y_Lw7V1waXZthX4R2rE5BF6Fl2sEcStsE1MHYpn5fW1YhiANramhs82R0q7ooj5hBt7jSP-CQXLr7Y8Fqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بنیامین نتانیاهو: در مورد رژیم ایران، من فقط یک چیز خواهم گفت: با توافق یا بدون توافق، تا زمانی که من نخست‌وزیر اسرائیل هستم، ایران هرگز سلاح هسته‌ای نخواهد داشت. به هیچ وجه اجازه نخواهیم داد ایران بمب‌های هسته‌ای توسعه دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/66828" target="_blank">📅 20:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66827">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 380 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری واقعی
✅
مناسب برای گیم
✅
تحویل آنی
❗️
پشتیبانی 24 ساعته  جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn @kaviani_vpn</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/66827" target="_blank">📅 20:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66826">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WHJOVk8CczfMHeIH_zhXXiznhazfcXuCKAlL5IVKygEe7CEsigDv3Avn2FyjKtiBEevgSsyr3wMnm8FH7mcR0txglEN04wKQwryrxvY-pffjQ_Mblb2pMNnrrIv6NgzGsj71CRDFqQnCqt3FfJmsct03q3273wfE0tUcOYfKnmCHIXeJ2HMBghofmVmDJfeaH0zmj9bYioq5k_V7I_lh4GvO4G5sRb-pxjb_EmHQPDjgTMDpltzWWz0DACsZ6PhJJmv3MbkABl9aI_RqIIXG2I6mvPzp4nIUt_MPGbXlQ6xqxhY4830KbS2YW0Tk5c1_3vu7XCVX21RzcJwLJqG7QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 380 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری واقعی
✅
مناسب برای گیم
✅
تحویل آنی
❗️
پشتیبانی 24 ساعته
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66826" target="_blank">📅 20:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66824">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xl7Uqjfzct0X_IrrUf9c9BCsNeRPsJh20oFs9P2M9IHoY4PWTWX4RXVa310B6A1BAkKnrLQ-K_7ce97qVoW2isbbVHgZRWir4h7ARrdwYzprwOk7zSCamv3V6wfyzBQtRarfwYrFVE_vIFJgaosOOy6HE7WiGLpZkA23lqtpszBUZ5Imla7KL8aFzOGdDF5yOGjqsfEBUPsSm_LeYvSmT3HyEZzKrPw6AoJHVB9EfUS5Zu0HSqndDBvUOTNwJr3kLb8mHmoat58ZqsnNx-sKR4J-PqP5uJ2TSU_2Omt1w_3Z8CZ4hPgoUGRqKSKxFVQ-zRDYbceTM_IaM5Frga7Z7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1b8ae4df4.mp4?token=jQVQ-VQwlPqDp-J4MqwOE_ZzlRX8yZcajTaCbhHsGSG1IISZBAeMifU5m7VUt57rUm_91FkWNBWaRcKAJzH24xInT7mRDUrlTIXBb6DVG1jYB2n-dfXZRwa30cT_CrJK8FH7k7ixrw1mgxKYJB6GIMIKXYjXSuN_L7yzR45aYWuNczTtj-qYpskkknVOWkJ9gxwmYkvHcGNLuWp8-2k-cKuzEp6CS7pILlFiTL5m0WbdlCLYcFgGIqCtE2-LvTxeBEfNVE-8DYftihfyHkQXN-6JlHh1VE7pF6YHSlRCSbKC827FkTHjat7JbnxuBr815ngy4t9R97mrffq3IbBoeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1b8ae4df4.mp4?token=jQVQ-VQwlPqDp-J4MqwOE_ZzlRX8yZcajTaCbhHsGSG1IISZBAeMifU5m7VUt57rUm_91FkWNBWaRcKAJzH24xInT7mRDUrlTIXBb6DVG1jYB2n-dfXZRwa30cT_CrJK8FH7k7ixrw1mgxKYJB6GIMIKXYjXSuN_L7yzR45aYWuNczTtj-qYpskkknVOWkJ9gxwmYkvHcGNLuWp8-2k-cKuzEp6CS7pILlFiTL5m0WbdlCLYcFgGIqCtE2-LvTxeBEfNVE-8DYftihfyHkQXN-6JlHh1VE7pF6YHSlRCSbKC827FkTHjat7JbnxuBr815ngy4t9R97mrffq3IbBoeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فستیوال محرم
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66824" target="_blank">📅 19:08 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66823">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/113cb570d9.mp4?token=jvGreXUcu-WhUrSeltGnAzh-KowAv5YvqB83HuIwmOCJFQWtODvnFsHG6aSlhSeAMjiDavZgyocU6joWjL6QUiKo693Vp3J5rA7o17Fl03yMQd4t1RTkhE7AV_1anSSfBZzOq84xwrGVJq8n0tgLwTaT59NBR9-E20wv0fpKEGmW-2v7062kG-nwr_8ZfnOBqagnc9nlUZiF6xzr8uLAOtsMZbVWkauhxaDD4Gk7qlCE4sEyTHRU0DOqrNFt0u33HGBjdACGwSJ7jsYNC0_U2nOK8r12bodamTRw0ZPH2v41P7xKLGMzhTq1gehJDfdAPTQTnfrlpO_rpytY9xHRSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/113cb570d9.mp4?token=jvGreXUcu-WhUrSeltGnAzh-KowAv5YvqB83HuIwmOCJFQWtODvnFsHG6aSlhSeAMjiDavZgyocU6joWjL6QUiKo693Vp3J5rA7o17Fl03yMQd4t1RTkhE7AV_1anSSfBZzOq84xwrGVJq8n0tgLwTaT59NBR9-E20wv0fpKEGmW-2v7062kG-nwr_8ZfnOBqagnc9nlUZiF6xzr8uLAOtsMZbVWkauhxaDD4Gk7qlCE4sEyTHRU0DOqrNFt0u33HGBjdACGwSJ7jsYNC0_U2nOK8r12bodamTRw0ZPH2v41P7xKLGMzhTq1gehJDfdAPTQTnfrlpO_rpytY9xHRSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
قالیباف پاسخ مجری صدا و سیما رو داد
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66823" target="_blank">📅 18:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66822">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0453856b46.mp4?token=JOWeruX8CvvuV-1H_bCfENLA1M5QY9FyZgIpbLeBkY3T84iM5bYRX6uL3uLNTLBLcqzrdxlhoj4JZcqbQaMjfKpS3UVwV_Ik3K7ASLqT2wS-jbw2nAlP74t97pAl6kZRHy596e4tP1hfvO97SJLyqocvwn6X2tL_44AugxrsWo9kf6L_HaO7T265w9U-YQDYJfCpDkAG_ar_T4_aZe-AAkWq08nqyR9ILflbtEKoruWZ0RUUz9Z0PsMMR8e-4Q3hv9ndoU7qDM3EhUlMW7VsEMoPauzqgP2BzrjT4zdgEtSbturKX4YPFgnJKV-6U3HDh26cWi6tZavACI5rGCxaAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0453856b46.mp4?token=JOWeruX8CvvuV-1H_bCfENLA1M5QY9FyZgIpbLeBkY3T84iM5bYRX6uL3uLNTLBLcqzrdxlhoj4JZcqbQaMjfKpS3UVwV_Ik3K7ASLqT2wS-jbw2nAlP74t97pAl6kZRHy596e4tP1hfvO97SJLyqocvwn6X2tL_44AugxrsWo9kf6L_HaO7T265w9U-YQDYJfCpDkAG_ar_T4_aZe-AAkWq08nqyR9ILflbtEKoruWZ0RUUz9Z0PsMMR8e-4Q3hv9ndoU7qDM3EhUlMW7VsEMoPauzqgP2BzrjT4zdgEtSbturKX4YPFgnJKV-6U3HDh26cWi6tZavACI5rGCxaAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو درباره ایران:
🔴
اگر کشتی‌ها در حال حرکت باشند، واکنش ما هم بر همان اساس خواهد بود.
اما اگر کشتی‌ها حرکت نکنند، این نقض توافق محسوب می‌شود و در آن صورت با یک مشکل جدی روبه‌رو خواهیم شد
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66822" target="_blank">📅 17:55 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66821">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50938460f0.mp4?token=hFBcjjA6aP_vqi3L2vGad0MCkJ1NNRtqMG0fE-qvOOyJUjsSFnutNP4w8IiCJtw4pUgwVdP4WDHYqZ2b96DcZ6Sai0G4DXX_ao0lLmZV3d6WWZWf0JDn2-ne5vNMygqw4swuJ3xkZUa-NvE_Po8qP6VoLpU9jQBMVS1RcPLARVLF9PmMwZSnEW7bHKnUWbF0RSPCRoXlVWE6ilD9IZfGeeDav1IHB6mVeA8T0AFFRVH5pyGjOGTVZMmor547ehv-TB1zFfPsQShPk94nv9b06ztSfimD12bee8X12ATUGaGZNe39MbI20HYOLxtyzc_YvDjOHzXj5NExh-CLIfS3Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50938460f0.mp4?token=hFBcjjA6aP_vqi3L2vGad0MCkJ1NNRtqMG0fE-qvOOyJUjsSFnutNP4w8IiCJtw4pUgwVdP4WDHYqZ2b96DcZ6Sai0G4DXX_ao0lLmZV3d6WWZWf0JDn2-ne5vNMygqw4swuJ3xkZUa-NvE_Po8qP6VoLpU9jQBMVS1RcPLARVLF9PmMwZSnEW7bHKnUWbF0RSPCRoXlVWE6ilD9IZfGeeDav1IHB6mVeA8T0AFFRVH5pyGjOGTVZMmor547ehv-TB1zFfPsQShPk94nv9b06ztSfimD12bee8X12ATUGaGZNe39MbI20HYOLxtyzc_YvDjOHzXj5NExh-CLIfS3Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو درباره ایران:
🔴
فرض کنیم که ما کاملاً دیوانه شده‌ایم و عقل‌مان را کاملاً از دست داده‌ایم و تصمیم گرفته‌ایم با ایجاد یک سیستم عوارض یا دریافت هزینه موافقت کنیم.
این قرار است چطور کار کند؟ اصلاً شدنی نیست. چون اگر کسی هزینه را نپردازد، چه اتفاقی می‌افتد؟
فرض کنید یک کشتی بگوید: “من این هزینه را نمی‌پردازم.” این مثل عوارضی یک جاده نیست که بعداً یک قبض جریمه برایش ارسال شود. به آن شلیک می‌کنند.
اگر به یک کشتی شلیک شود یا یک کشتی غرق شود، دیگر هیچ کشتی دیگری حرکت نخواهد کرد.
بنابراین چنین سیستمی نه‌تنها غیرعاقلانه است، بلکه اصلاً نمی‌تواند اتفاق بیفتد.
حتی قابل اجرا هم نیست. پس بهتر است همین حالا این خیال‌پردازی را کنار بگذارید.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66821" target="_blank">📅 17:50 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66820">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FYluyCRKzCxrLmyJi9cXYUxz4ajQFmyJ1g37Qnhy6_XmGk0N_Ffh5HVrq85b-PWH72CXw1Jj1tgSvDc6iJHAjbCzuwf-eZCrL_i1os5WcDjbgVvRFJuo5h2Q-m1SIqHOviXsMpxbiR0YZ90M2zG9cqA_DS7YkTs5Vhz2FGHmS7DsqzUaYW1zFUuVPHRntCLsDW1CPV3DQgCa-zA3aV2K6RGkoGon6MQleyYr5iPLBz_dvAVvKy0iwMHRoi9gC5iJC1UE3UB53xYxb4YxMxDipSqgcZtu2KAi2wXdFZoyg5p14dBgz3Ed4MA3sKPqR0kmq-48_ZlQYm8bAazpvNjljw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قالیباف:
آمریکا به دروغ ادعا می‌کند که دارایی‌های آزاد شده ما، کشاورزی آنها را می‌خرد. جالب است. تنها محصولی که ما برداشت می‌کنیم همان چیزی است که شما کاشتید: دهه‌ها بی‌اعتمادی. این محصول ارگانیک، فراوان و تولید داخل است. اما ظاهراً ایالات متحده فقط سویای تراریخته، وعده‌های عمل نشده و حرف‌های بی‌اساس صادر می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66820" target="_blank">📅 17:19 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66819">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/477cde7837.mp4?token=UjbupZF4S8T1-2hwOKrC0hQHcgR6TTAf8Fr8QefCZwLUq9kHma-N4XwVbOB1iBD3mU1lMzOAQ_pxAXMQbwENh3i_3xOTGSvc7HWuxoqvYz_h33NvZb7Tdv6gvPDgfjoFYMHY2U9_mIX2bUFy8SlHebTMOpf6BCq50dDcLL6-7e2oa6l6XX4LDBv5qvgx01fNk1rx70Il3we-jHQqlaKIpLMdhOq1WraL6vBR7zkQPNEoiNc6JhU-440YaxBRwLj2n_VjYOCw9gMQcM8ZM8W5slN2q1XMNHWiGxPzu1P8zCE9L81fHijB158Ch6oN9bghGbzbIWQrt4hmHUw5O9u6dIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/477cde7837.mp4?token=UjbupZF4S8T1-2hwOKrC0hQHcgR6TTAf8Fr8QefCZwLUq9kHma-N4XwVbOB1iBD3mU1lMzOAQ_pxAXMQbwENh3i_3xOTGSvc7HWuxoqvYz_h33NvZb7Tdv6gvPDgfjoFYMHY2U9_mIX2bUFy8SlHebTMOpf6BCq50dDcLL6-7e2oa6l6XX4LDBv5qvgx01fNk1rx70Il3we-jHQqlaKIpLMdhOq1WraL6vBR7zkQPNEoiNc6JhU-440YaxBRwLj2n_VjYOCw9gMQcM8ZM8W5slN2q1XMNHWiGxPzu1P8zCE9L81fHijB158Ch6oN9bghGbzbIWQrt4hmHUw5O9u6dIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویرانی‌های بر جای مانده از زلزله مهیب ونزوئلا در شهر کاراکاس
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66819" target="_blank">📅 17:08 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66818">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rkNk-ErOjq-pLXD5eP4aZpD3G-PB5fuY4_0Vraz-BaVPZjSp8dHnA6v4Qg7QU2877u3qcED7uNuFNlBRoOy_S55VSw5gc4323nyTMh3G2UGYcTpvUz7mDp0P6RkbucH-f0ZUTIKTq-qxfDa_S99CCPTDZbumkkhKBYz_nUMnU_wsn8XwrsWV4qEB7FcdwEsXXLMWThUkb3L7hUySKdY582kvFA1M2FaZZaYljfYrDizbgfhuP0Zgm3RfXne232RQRu1NyKahC-HXpKD5MeeRkXeRQBf4XXlKl6T4W4a1ID3WB01-TI40JcAG-p374mRO-kWXoH1Ms82t1fImELJ2Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسماعیل قاآنی فرمانده نیروی قدس سپاه پاسداران:
اگر اسرائیل امروز داوطلبانه از جنوب لبنان عقب‌نشینی نکند، فردا مجبور به فرار با تحقیر و شکست خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66818" target="_blank">📅 16:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66817">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4301a5bfb2.mp4?token=Avh7QxaywSGx-ur6OeY6qfplG1U1SBrQmUbyx12dfb_zudPubfa7q87avBFg62Jc7fEY66XQuVayPK27fZ5-eG7XclQs7Za8gXCvDpAo2p1OCIDK5TI3YRLjsjeRASlG313EIHzcMpBX28Eb1RUiSlqM8Ifu_8ZA92rsRzZ-k5QGM3dRsbUxwucRN-UGjPHSncxuc5PU5SgfTzmO5Ov-KO1Mekf2aaYssBzJbcurD_l2oDYGKkfVLVWfvNOM6C94JA7gjwe_u8UnXJZUgRpKPffjmXJvs3dycQiGkgOK4hEZkSyf4kbQpGQYgFkqWXYequsoJSLAvigrIF188mNbNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4301a5bfb2.mp4?token=Avh7QxaywSGx-ur6OeY6qfplG1U1SBrQmUbyx12dfb_zudPubfa7q87avBFg62Jc7fEY66XQuVayPK27fZ5-eG7XclQs7Za8gXCvDpAo2p1OCIDK5TI3YRLjsjeRASlG313EIHzcMpBX28Eb1RUiSlqM8Ifu_8ZA92rsRzZ-k5QGM3dRsbUxwucRN-UGjPHSncxuc5PU5SgfTzmO5Ov-KO1Mekf2aaYssBzJbcurD_l2oDYGKkfVLVWfvNOM6C94JA7gjwe_u8UnXJZUgRpKPffjmXJvs3dycQiGkgOK4hEZkSyf4kbQpGQYgFkqWXYequsoJSLAvigrIF188mNbNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇷
نیروی دریایی سپاه:
تنها کشتی هایی که از تهران مجوز دریافت کرده اند حق عبور از تنگه هرمز را دارند و با هر شناوری که از این دستور تبعیت نکند برخورد خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66817" target="_blank">📅 16:09 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66816">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jxOAhnC-VHFJg0B4SXDaI9uo8dm8jfubMH_RzMdPpHXOGMLplScTqI4SZBa4Jir-tpxrmAUXcTKA6WSnl11QUd38n3IRxcAfax9MoUb7vYbn99lOChgsV3RrTqdrdKLUOJDln4PB5-qMYTyTS4HDVgxsjhcIPTb0o32N_0SANDGmaA9B41zpDdAs8UCCiIrtmJVzoa5CAyZN5QbovgwAJ-JARphTrA2EpFHL6bAamDYn80xK-S785n9Fndr1BESwugnVGajrEg19-Xs95jTO9sU_-1TltmU8E71lvxiwR-tg6b4Ay3q3z-0HJQqP707U-SyI8sBwBCcDKd5YSV0alg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇸
پرزیدنت
ترامپ در تروث سوشال:
«شگفت‌انگیز! سنا رای خود درباره ایران را از ۵۰ در برابر ۴۸ مخالف، به ۵۰ در برابر ۴۷ موافق تغییر داد. رند پال و بیل کسیدی رای خود را تغییر دادند. از جان تون، لیندزی گراهام، برنی مورنو و همه سپاسگزارم. این رای به ایران هشدار می‌دهد.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66816" target="_blank">📅 15:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66815">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">❌
خبرگزاری رسمی عمان:
وزیر خارجه عمان اعلام کرد ترتیبات آینده برای تنگه هرمز شامل دریافت عوارض از کشتی‌های عبوری نخواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66815" target="_blank">📅 14:53 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66814">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a64b900d33.mp4?token=mtCCZlaDDrrLIH9JXN1ViYowN6v8A--GRzCpFYYZSM-l-LSAaF-qkaGF2cLbYQFsf5jJSngTXhgHjJof2LHPmfOz3qnjNcGBKGrD4P-Hrj2t8EK2soUO_Ofhjbh_mHdts-dL9__D_TjbRtrR3eFXXNe5T6-rPsMtUIgT0y3_4EYZq4fYoOnFo_nEjWOUIREp1iu59FdeC31td3PaML_E1RYFkNKVq4uC7USFSu_ePeXoJjtoI2aU-d59kkSKqBIXTI0yfFtUwONUCjklq8k5S8P3hCJybgxUc7rzVHzAnlUEULcNTTpHh5vjNHU0im2bkcoaBXEzAZXm-_Cs_YM46g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a64b900d33.mp4?token=mtCCZlaDDrrLIH9JXN1ViYowN6v8A--GRzCpFYYZSM-l-LSAaF-qkaGF2cLbYQFsf5jJSngTXhgHjJof2LHPmfOz3qnjNcGBKGrD4P-Hrj2t8EK2soUO_Ofhjbh_mHdts-dL9__D_TjbRtrR3eFXXNe5T6-rPsMtUIgT0y3_4EYZq4fYoOnFo_nEjWOUIREp1iu59FdeC31td3PaML_E1RYFkNKVq4uC7USFSu_ePeXoJjtoI2aU-d59kkSKqBIXTI0yfFtUwONUCjklq8k5S8P3hCJybgxUc7rzVHzAnlUEULcNTTpHh5vjNHU0im2bkcoaBXEzAZXm-_Cs_YM46g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ درباره اردوغان:
🔴
او دوست من است و از جنگ دور ماند.
می‌دانید، او یکی از اصلی‌ترین گزینه‌ها برای ورود به جنگ با ایران بود.
شاید هم در طرف ایران، چون همان‌طور که می‌دانید، او طرفدار  اسرائیل نیست.
و من از او خواستم که وارد جنگ نشود. او هم وارد نشد
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66814" target="_blank">📅 14:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66813">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oltq-9A-1w1Z7uFLfyyb_6EKOVW9CPeHZs-LBdGWpZ57sCPKSsrEes8fgD5h3apJiPhbvtpKkq5aqfUO-RFPWl50itS1LsflvdpMH-8q40tvgadSXnNrQ_S6lItxXrtda9f3CbuJPbweFo2zA-dUsVRqixeakEs-XExCsMOUYQFy7D13oRb2t0y1k3Fgdm6IU10SJOW2VrQH9bnfh-J5nYGzHHlm1Je2D9yOub9nYq3OdPPBzd2NymY_DRmiWPCQx7HgYTer9uKB8HV8UC1Dj-ba__2ATCU91QnBsNbI8XTnmT5H2WSUZobJi8ciTbbbvDRmJj2X-NrL-in4XP3PwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو:
🔴
واشینگتن خواهان توافق با رژیم  جمهوری اسلامی است، اما نه به هر قیمتی.  هر توافقی باید واقعی، قابل راستی آزمایی و همراه با پایبندی کامل به تعهدات باشد. اگر رژیم جمهوری اسلامی به جای صدور ایدئولوژی بر رفاه مردم ایران تمرکز کند، آمریکا و شرکایش آماده همکاری خواهند بود، اما انتخاب مسیر کنونی نتیجه مثبتی نخواهد داشت. هیچ توافقی نباید امنیت، ثبات و شکوفایی شرکای آمریکا در منطقه خلیج فارس را تضعیف کند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66813" target="_blank">📅 14:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66812">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0835d639a.mp4?token=obQ-zLXeoS-cf17KikuAho7uSld_TsBjJpdp8ZSIYIgnX1AYrrgYKQDpow4N-tNaaDNk0zkHnnu8xRjn_Gwdh6xXhF2GCdCYl77pZwJ8Ev7SbbPEqii9zpXi54xuekkTysbX9Q3W24AwKQzUVWstsODL7UHmP_n3usgaDp5M25Wo_Hf8D3V_Xc6mZpo1CsaDWM-XhH4gp6cp54OJ5y96qnMxOlOjw8juZAdNEcj8-GUuTDXtvo6zTzE4lsEcYFBaOboHuOA6ARXs5ju2EoP2QOO1o8FJ4VltJe5GOFi3yM_5zhTotQAg1HMDfX8o1-ERLarlyNyj9NMcAX0USmQKNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0835d639a.mp4?token=obQ-zLXeoS-cf17KikuAho7uSld_TsBjJpdp8ZSIYIgnX1AYrrgYKQDpow4N-tNaaDNk0zkHnnu8xRjn_Gwdh6xXhF2GCdCYl77pZwJ8Ev7SbbPEqii9zpXi54xuekkTysbX9Q3W24AwKQzUVWstsODL7UHmP_n3usgaDp5M25Wo_Hf8D3V_Xc6mZpo1CsaDWM-XhH4gp6cp54OJ5y96qnMxOlOjw8juZAdNEcj8-GUuTDXtvo6zTzE4lsEcYFBaOboHuOA6ARXs5ju2EoP2QOO1o8FJ4VltJe5GOFi3yM_5zhTotQAg1HMDfX8o1-ERLarlyNyj9NMcAX0USmQKNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حتی در کیس بیماری هم عجیبیم
🚬
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66812" target="_blank">📅 14:10 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66811">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce6df862a9.mp4?token=pNg_S2AEhHy6Pz_h0Gibzoz4arVfhF9aIyp-CspgSXVQR044LHdUPc5KnhZlRltK-dVNkzQmb4iT0108F04lPIaXdoK-SW_MSuc4sR0SfHypO2-alzVRiUl9TGIdwApFK3f6JiHGaRzAd2wR_mfff9AnSZhzt1vIeaiFvw0RFnueqJTPm2Dh9UHtwuqyQglIT_EO8MCxbRe6STqAMulNoJREuGtgSX8ClizZpft2k2ZtnV7LcTl4b57l2SaDwAhes0HZDEPIDNrU31Ez6MakViQcBT83DK3W1SZW8YfEd38uiNaBDHXBg3iKMMjyasTcoKHLx1OrHGAJL5eQWgdqwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce6df862a9.mp4?token=pNg_S2AEhHy6Pz_h0Gibzoz4arVfhF9aIyp-CspgSXVQR044LHdUPc5KnhZlRltK-dVNkzQmb4iT0108F04lPIaXdoK-SW_MSuc4sR0SfHypO2-alzVRiUl9TGIdwApFK3f6JiHGaRzAd2wR_mfff9AnSZhzt1vIeaiFvw0RFnueqJTPm2Dh9UHtwuqyQglIT_EO8MCxbRe6STqAMulNoJREuGtgSX8ClizZpft2k2ZtnV7LcTl4b57l2SaDwAhes0HZDEPIDNrU31Ez6MakViQcBT83DK3W1SZW8YfEd38uiNaBDHXBg3iKMMjyasTcoKHLx1OrHGAJL5eQWgdqwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حدود ۷۰کشتی در ۳۶ساعت گذشته از تنگه هرمز عبور کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/66811" target="_blank">📅 14:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66810">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">53.2 MB</div>
</div>
<a href="https://t.me/news_hut/66810" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
نسخه آپدیت شده اپلیکیشن ملبت
🔶
• لینک سایت مخصوص کاربران خارجیMELBET:
🌐
t.me/ConnectMELBET
🔶
• آدرس سایتMELBET
🌐
bitly.uk/connectmelbet
🟠
نکته: اپلیکیشن بدون فیلترشکن کار میکنه برای ورود به سایت باید سرور فیلترشکنتون رو کشور های اسیایی یا کانادا یا ترکیه تنظیم کنید</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/66810" target="_blank">📅 14:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66809">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SWbJ83JnCMpOs9toe-9kg79pFpT8NIfKAIerHkSO7nWU_vFqPVRVteH-uDuzAbOlHzoiKiOw8LJAUnHGS-DfBqYUXevhCp-psHWUq4U3WuOXJc_O2uvW5jOh2qdtwkRel4Xl4HkvGfT_aWLeuJNNKG14MKf46VLygMk32zg0BPCky5aQrbY1yuPGYPQJ9sKJ7kS9P3dEApRv3RHwiZ1m_0-1N6wk1HTZxEpvYjaRuL-fSLWR8dUZ8TKpNpsJiFldV7HM7Ql_ORAcQ2TqVsGEfUPKBdzLfSjgA_RWz7jP6f1WNi5ZDSjt689HyNYd8FG0_onrjhqrhh9RYkmATB5RKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
بهترین سایت برای بت زدن سایت MELBET هست که مورد تایید ماست و خودمونم چندین ساله توش بت میزنیم
💸
با اولین واریز اگر با کد هدیه
ml_459049
ثبت نام کنید تا سقف 100 دلار 130% بیشتر شارژ میشید
واستون لینک و اپلیکیشن ملبت رو میزارم که ثبت نام کنید
🌐
https://refpa3665.com/L?tag=d_3312431m_45415c_&site=3312431&ad=45415</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66809" target="_blank">📅 14:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66808">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ead28978b.mp4?token=p9rOu1VEWr60CcfAihzTtpEtv6mPCzbQZYH2mQO5Y-M92aBaPvm79sG4XMP4nRhg6s7oTcn50UO5065pNHoayhsglhRan_hxwia3NGNpnkcJQteL2TYeAJRMUz4r_HMWzx-qXNgTExk7QHcN2HLI1pXr23MBOS8YsPsJ_ANWahnZOZmmrS5X3K_CJ8Plq0WJrFNVy-Hq-ZT5eK-yH52E3A22xfTry-IRxUkuQBzP-PWKyVQe4tjRCjIj3nYcEbMUehlo7V7QBnLDYOHQZ_i-nQILPgSdHke-TWKBPKCs30c9gE97h6pEQR6A7G2125x0iBhF-m6_eh0mxVyL-BsDDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ead28978b.mp4?token=p9rOu1VEWr60CcfAihzTtpEtv6mPCzbQZYH2mQO5Y-M92aBaPvm79sG4XMP4nRhg6s7oTcn50UO5065pNHoayhsglhRan_hxwia3NGNpnkcJQteL2TYeAJRMUz4r_HMWzx-qXNgTExk7QHcN2HLI1pXr23MBOS8YsPsJ_ANWahnZOZmmrS5X3K_CJ8Plq0WJrFNVy-Hq-ZT5eK-yH52E3A22xfTry-IRxUkuQBzP-PWKyVQe4tjRCjIj3nYcEbMUehlo7V7QBnLDYOHQZ_i-nQILPgSdHke-TWKBPKCs30c9gE97h6pEQR6A7G2125x0iBhF-m6_eh0mxVyL-BsDDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚬
بسیجی‌های صادراتی دیشب تو میشیگان آمریکا نذری بین آمریکایی‌ها پخش کردن
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66808" target="_blank">📅 13:11 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66807">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba9d2db1fa.mp4?token=KiKuQJhIIR718AAj5YpdkRxS0ZP06hDZGRqFdCMcKlDvIWspMDeNZP3HQom6IsmRL8VruXeTw4ekaeEUkSqLgxFwUAg_OYgaE-JVrjpmDp-vRNFFTiBWnISvHzRDpIeABQLSo9HE4j6VRo0YAyigu5TdHQE6zsg0dvI9PVLBxzrC0yHD-OFBOSe1anmBSFwgjShzpchdTWmeVS_Mr5jFZOxJl_2-1xyOf_bd6nuY9GXHtansWjikPkV5y32V9AnolL6v9sDS65lJyYsTj_fQMeEUIASTDRYLv1kVWwDp3RjdtKFSlToLHQVkvXx-jz9Ueiysu3DcV2AwlOxEwCtRPTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba9d2db1fa.mp4?token=KiKuQJhIIR718AAj5YpdkRxS0ZP06hDZGRqFdCMcKlDvIWspMDeNZP3HQom6IsmRL8VruXeTw4ekaeEUkSqLgxFwUAg_OYgaE-JVrjpmDp-vRNFFTiBWnISvHzRDpIeABQLSo9HE4j6VRo0YAyigu5TdHQE6zsg0dvI9PVLBxzrC0yHD-OFBOSe1anmBSFwgjShzpchdTWmeVS_Mr5jFZOxJl_2-1xyOf_bd6nuY9GXHtansWjikPkV5y32V9AnolL6v9sDS65lJyYsTj_fQMeEUIASTDRYLv1kVWwDp3RjdtKFSlToLHQVkvXx-jz9Ueiysu3DcV2AwlOxEwCtRPTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنوز تو این دوره و عصر مدرن یه سری کسخل وجود دارن که با عقاید عصر حجر خودشونو بگا میدن
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66807" target="_blank">📅 13:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66806">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81f4c39a8d.mp4?token=K0g5pRQl7A5JererU_0S4rPe1y7b1Xr5UHKCT7yoMYmoos8y3tGM1Emcb6sBsdUGrPP5_4Jsc-QHWrybqaSAYKgChsxg2LcyQ8ONThvBYJOL1O69meKgLzITa2_q1p-EeeNDqA57-_RtogQcgIQMBhPOAWNNwDet74-Fl5ar2w08YXg7DxQZRueEIpFwjnWGFRxenMUslZK__yRC5on3BKNvnjt_9_cQKjDI0GAkj7WECyY_OwoFUHkJnK1Rq_iC6aYvX7Gw1C3fzEmt0dK7LOZVHGGzYBpWw0vNQLebzuejiNzYpib8gUoG7SoHE4Is8E-Roz6dO1I_QdvmDmBNxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81f4c39a8d.mp4?token=K0g5pRQl7A5JererU_0S4rPe1y7b1Xr5UHKCT7yoMYmoos8y3tGM1Emcb6sBsdUGrPP5_4Jsc-QHWrybqaSAYKgChsxg2LcyQ8ONThvBYJOL1O69meKgLzITa2_q1p-EeeNDqA57-_RtogQcgIQMBhPOAWNNwDet74-Fl5ar2w08YXg7DxQZRueEIpFwjnWGFRxenMUslZK__yRC5on3BKNvnjt_9_cQKjDI0GAkj7WECyY_OwoFUHkJnK1Rq_iC6aYvX7Gw1C3fzEmt0dK7LOZVHGGzYBpWw0vNQLebzuejiNzYpib8gUoG7SoHE4Is8E-Roz6dO1I_QdvmDmBNxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پرستو نظام با کلی عمل زیبایی که البته هرچیزی شد بجز زیبا: قلب من با امام حسینه
😐
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66806" target="_blank">📅 12:34 · 04 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
