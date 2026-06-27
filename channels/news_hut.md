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
<img src="https://cdn4.telesco.pe/file/GtgpS4OSr6-C3lKDcBTpU0TTIzrlOuB0-an4VuSbr0DROZgN1gtvmWYdfD_V9ATD7KXqbp_IEQRXEBe0BmfzoDtujY1DI14xTM37MwOM4nkeg7BZp6guvijfJb_YWpMy8ZtN7jDLejTy9cHEffsNzOL0U-q2pACYNvSMoweHj8l7IdJ1BAjKQ8l48fMnOPQTcv3iWcprBh0r75E2oIIC7VIRGNQX1nkH2iIG8bG0YljPFRw_H--WsKRujNw-GiXM9nENIxq74GuBRARD-8tmrA-mpikxcYiMHJw-IqQpnYiAFcLa2W-pstEvb9couoX1bHzYQikI6UACRdLUpUVi1A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 219K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-06 14:39:06</div>
<hr>

<div class="tg-post" id="msg-66922">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UgC2Gh9lAPm-Sytlwe2MJTZn0rqvEs3J-UCCWAPQrj0nk6V4ZkS58U6al_JP2ND2Q4Y87FE0ldZt8J3Xiyec8Sxd90KdvKgTYbDcym4oF3igqADc03jFYzWqZNELx3H9ctOfbM09GKwN46UusthHhmknOZO1NuOZ7qrarPkPJdi43TpuDlFXA6WHTGhclawMrmnm9sDLQJ_73i1LTO03BacuYhZtnj4Rp2ZlM0MrmXAcU5WNs46JXijcKFYel5x3_ystu__2KakJ_jdEXMIi5ErfkKpMwou1vSqsJVfTKqF6ulhoD2JopNVfjzPh-TYPwHZVuRyDILZwTjHYX6EsIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محسن رضایی:
پاسخ به ناقضان تفاهم‌نامه سریع و کوبنده خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/news_hut/66922" target="_blank">📅 14:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66921">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
⚠️
صابرین نیوز:
این نفتکش، برخلاف مسیرهای اعلام‌ شده از سوی نیروی دریایی سپاه پاسداران، قصد تغییر مسیر و عبور از آب‌ های عمان را داشت که در پی بی‌توجهی به هشدارهای مکرر، مورد اصابت قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/news_hut/66921" target="_blank">📅 13:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66920">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UuVa4pik5EfxKduS_tZMDPZQZmR0FmuHUqNZPwjLmzCTCysUaFlXvbWe9RtnOeuVecweDvbNo3EKJ8SLNa7ceVFmHrIFwEVNDOc2umjrie3zAPvMAFKR7QdzrJPJMh5RKfv0xTbQgSfKDXqarxmMNjCNyLVv55PEj8zabG_ekIBddlfA9saLnlK66DJpq36Z_wN38m37rArC0WTewgzyp5Tqx9BMNe9QwUWVrNy0qvdTE2R89ZYgKFbDjNB0D7d3MlZAPF2jrJammzPL45Oaep72HtyB-H9aehmyqH9Mvxob2tmRJoTMebg8rBfYBvQc4WJxq3FPwHEi9AD2tRJPZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوری
؛لحظاتی پیش اکانت عملیات تجارت دریایی بریتانیا اعلام کرد یک تانکر در شمال کشور عمان و در ورودی خلیج فارس مورد اصابت یک پرتابه‌ی ناشناس قرار گرفته و عرشه فرماندهی کشتی دچار آسیب و خسارت شده.
@News_Hut</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/news_hut/66920" target="_blank">📅 13:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66919">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
🚨
بحرین:
صبح امروز جمهوری اسلامی با تعدادی پهباد به ما حمله کرد.
ما این حملات را با شدیدترین عبارت محکوم میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/news_hut/66919" target="_blank">📅 13:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66918">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fvWRSqtPgJWEfT1gkr_wSEesoZpL8nGvhH4NcMUpsB31gE_Lyv85edsGJuXtiOXPZdAXipPfWsjloB1n5i1L472bCmQfxHOjcH6H67k_CGjgIwzkJpiGBiSqxH7BG9skAlyvVcQgL6QgbfoYbSc_6JEob2SPj3O7H8_4ioDTHhZNr_2vDJK-CXYnsF5TDavFFhYD1Ds7CI-VXq8Ic-QOXiaJKOembwg4uPE9hNeLrho8c0qi5-f7Lw5ck2yY_b6fGsaqUdqv5MslcUpiSZMhWlEmEfafS-QfdUPf4SdTy2c1rcjk9aDfdVTfZtYdJvMl-nkbi4w66FKaeqoG-H_r8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
نبویان:
ضمن تشکر از سپاه قهرمان ما به خاطر پاسخ به تجاوز دیشب رژیم امریکا و در نتیجه نقض بند یک تفاهم‌نامه، مطابق بند ۱۳ قبل از عمل به بندهای۱،۴،۵،۱۰،۱۱هیچ مذاکره‌ای نسبت به سایر بندها نباید آغاز شود.
منتظر تحقق شروط و واکنش شفاف و پشیمان کننده‌ی مسئولان مذاکرات نسبت به نقض تفاهم هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/66918" target="_blank">📅 12:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66917">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/66917" target="_blank">📅 11:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66916">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/66916" target="_blank">📅 11:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66915">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vlf3k9TXdq8D44ve_uadCLO5tJwOJMbkafc9XA6e6ITVCvjqOgP4Ln681-ffb2P8hxEq9KPQdtfoictJbf77s8tFiz91JzG3to4o7cf58YM1J2cQMhc-0sFBHWoZXles4PGF3y172UR7QIN9zlGpSScw5vp-x7JGmebZyvScbzB_Ij2XIcWbCaB5SWDCER6GzkZsdJg14f_KImnxIA2u3jJKyi-9nr1qt7gFzxjiH4DDuDd2bmD7fpa1ZmQMavSPJnCVK5qDqzx2EBaWFlRV8Yp7saR38PHmjeJysQ_Wjsag2t6Kr69l5We61lfi12YNkQFDD0NCL0BnBNc4En3A_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇸
پرزیدنت ترامپ در تروث سوشال:
نمایش هوایی چهارم ژوئیه، در آسمان واشنگتن دی‌سی، پایتخت بزرگ ما، بزرگ‌ترین نمایش هوایی در تاریخ ایالات متحده آمریکا خواهد بود.
صدها هواپیما از انواع، اندازه‌ها و سرعت‌های مختلف به نمایش درخواهند آمد. من حدود ساعت ۹ شب سخنرانی خواهم کرد که پیش از آتش‌بازی است که باز هم، مانند نمایش هوایی، تقریباً ده برابر بزرگ‌ترین آتش‌بازی در تاریخ کشورمان خواهد بود.
پس اگر هواپیماها، آتش‌بازی و دونالد ترامپ را دوست دارید، آنجا باشید!
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/66915" target="_blank">📅 10:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66912">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/66912" target="_blank">📅 10:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66911">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BuNBMKsztCCxFntWtE9Go0oZWamr6oy5ffPJtq5HdcUq-UEjFzsAxZ8y0cN6RbDWeMPaechVP0Wq9TG2WCPyRWvGopbkkxyLkBeK2Fk44Fz25d2zkcBO1qxH_twjufgsTgR1jOQeUQmk9BaTpgzQDPcZlYOq2snXt0HuTjwNxOK3r64k3oR8Bj0xo4oYp2Z_1V4WHJE3-ZU8PBrjSyA2Y3txDaX_dV_ogvyNUPtF888E4mtdZJW0chxhAUCMKznSIEs_on04KGs9zib0mErS0mNeA7iR01ZASabG_uxvwgWCXbSRfside9smgBQN5c69kMCtdYfb9zqEGzt_mY8-zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
❌
🇺🇸
آیت‌الله جی‌دی‌ونس:
ایران توافقنامه آتش بس امضا کرد. ما آن را گرامی داشته ایم. اگر آنها در مورد نحوه اعمال تفاهم نامه اختلاف نظر دارند، می توانند تلفن را بردارند.
اما خشونت با خشونت روبرو خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/66911" target="_blank">📅 10:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66910">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/66910" target="_blank">📅 09:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66909">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/66909" target="_blank">📅 09:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66908">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/66908" target="_blank">📅 09:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66907">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‼️
بازی تیم جمهوری اسلامی و مصر با تساوی ۱/۱ به پایان رسید
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/66907" target="_blank">📅 08:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66906">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66906" target="_blank">📅 02:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66904">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/66904" target="_blank">📅 01:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66903">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
سی‌ان‌ان به نقل از یک مقام آمریکایی:
حملات آمریکا در ایران اکنون به پایان رسیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66903" target="_blank">📅 01:13 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66902">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
🇮🇷
بیانیه سپاه پاسداران در واکنش به حمله آمریکا به سیریک:
نیروهای ما موفق شدند این حمله را خنثی کنند و نیروهای مهاجم را وادار به عقب‌نشینی کنند
ما تأکید می‌کنیم که این تهاجم بدون پاسخ نخواهد ماند و پاسخ ما در زمان و مکانی که انتخاب می‌کنیم، سریع و قاطع خواهد بود. هرگونه حماقت جدید با پاسخی سخت مواجه خواهد شد
.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/66902" target="_blank">📅 01:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66900">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/66900" target="_blank">📅 01:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66899">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🤯
🇲🇽
پشماتوووون فر بخوره؛ یه‌زن مکزیکی برا اینکه شوهرش رو سوپرایز کنه و بلیت جام‌جهانی بخره، یک هفته قبل مسابقات عکس پاهای خودش رو‌ به مردان کشورهای مختلف می‌فروخته و از این طریق تونسته درآمد زیادی کسب کنه و علاوه بر کیر زدن به مردان هول خریدار، شوهرش رو به…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66899" target="_blank">📅 01:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66897">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/66897" target="_blank">📅 00:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66896">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
🟥
فاکس نیوز به نقل از مقام آمریکایی:
حملات آمریکا به اهداف ایرانی همچنان ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/66896" target="_blank">📅 00:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66895">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KkiGCAYrMkEcIiEKerwXI8yjSyj2J_fmpcZhuFpg18dKLC8aRWNPupQyzQBC94UtZ0i-FT4WLgPW_ikcb2awnNCecJHV8fRKP3e36VNEcFmrli29iVY7CFsQ5s32ulgiJ9nEO71uQRh_GWAcWkVzIbseopNmFHlJf4Lygu_xGxoqMj3FELFHzeoVdFDezSNew66jdm8Ub0-0TpMG1VtIyenIfdXXl1BVSUI4QVPX9UMkvq5giNL-xhXNbzk_SPZeOQvXddNfajOkmVxY35CMnoVvOq2NKAQXyqS7MzJ4FJxsFh0lGPQ9Pgd3nLewM8mpDdggUk7vFLYR78Zn9vD8TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
سنتکام:
نیروهای فرماندهی مرکزی ایالات متحده (CENTCOM) در ۲۶ ژوئن، به عنوان پاسخی قدرتمند به حمله دیروز به یک کشتی تجاری که در حال عبور از تنگه هرمز بود، حملاتی را علیه ایران انجام دادند.
هواپیماهای آمریکایی پس از آنکه ایران در ۲۵ ژوئن با یک پهپاد تهاجمی یک طرفه، کشتی M/V Ever Lovely را هدف قرار داد، به محل‌های نگهداری موشک و پهپاد و سایت‌های رادار ساحلی ایران حمله کردند. این کشتی باری با پرچم سنگاپور در زمان حمله ایران در حال خروج از تنگه هرمز در امتداد ساحل عمان بود.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/66895" target="_blank">📅 00:14 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66894">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
🚨
#فوووری
؛باراک راوید به نقل از منابع آمریکایی:
ارتش آمریکا به اهداف ایرانی در منطقه تنگه هرمز حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/66894" target="_blank">📅 00:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66893">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
❌
صدای انفجار ها به «طاهرویه» در سیریک هرمزگان مربوط بوده.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/66893" target="_blank">📅 23:58 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66892">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/66892" target="_blank">📅 23:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66891">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
🚨
صداوسیما: صدای چند انفجار در سیریک شنیده شده
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/66891" target="_blank">📅 23:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66890">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❌
🚨
🚨
🚨
گزارش ها از انفجار در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/66890" target="_blank">📅 23:34 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66888">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/66888" target="_blank">📅 23:17 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66887">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/66887" target="_blank">📅 23:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66886">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66886" target="_blank">📅 22:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66885">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🤯
🇲🇽
پشماتوووون فر بخوره؛ یه‌زن مکزیکی برا اینکه شوهرش رو سوپرایز کنه و بلیت جام‌جهانی بخره، یک هفته قبل مسابقات عکس پاهای خودش رو‌ به مردان کشورهای مختلف می‌فروخته و از این طریق تونسته درآمد زیادی کسب کنه و علاوه بر کیر زدن به مردان هول خریدار، شوهرش رو به…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66885" target="_blank">📅 22:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66884">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l9aaPmD8ku8QCo40rkUEq905DJ2ziQVyszLEUyicimOw6V8amyCfeYV7tGEHA5OhmlnE8C89S9TIPohj962MKvDZNQMk6gizwKprQHRuB5y4QGhTDAYF2r5T4p0JS4A4vQUQBIWxMFgQMay41IPPdeCgUM0bPscHOcgWb8nTXeXHU5x3tlTS5fvoki7WDL9xPHQbvl5DtmTdEQBjQ2zsoJAG3U7fc6_xdmbBt9IyDKIY4lcxjjsEL64j01qYPmr3ilhGLPVwKwAWuZCrNnKXMqW8GOAlNbUL74IlqzJcNoG2Ew7Y5z3719QT0B9SBZDOTiKiM4vB6pkO7WMaTVB2ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
رئیس کمیسیون امنیت ملی:
به سران شورای همکاری خلیج فارس هشدار می‌دهیم، قمار بر سناریوی آمریکا، ثبات و امنیت شما را بر باد خواهد داد.
دیدید که پایگاه‌های نظامی آمریکا در کشورهای‌تان چگونه به جای تامین امنیت، به منبع تهدید بدل شد.
قدرت موشکی، پهپادی و همچنین مدیریت تنگه هرمز، خط قرمز جدی ایران است.
تنها راه تامین امنیت منطقه، فاصله گرفتن از امریکاست.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66884" target="_blank">📅 22:17 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66883">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66883" target="_blank">📅 21:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66882">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f7by9ovzNCTUuzuvljDnvOkYW3BIh-ojVhpQ5213QTSXuRx0nSVc1c9o1GvDiITFKjIPEQ5EkZ0zpI66cW_0QBczIb1wxO7XOAU4dJ7EdODBQkKBV93MTsuxYttCev_GWcrFgzLGBTENDnFzUoiWWVLH_r7Yugcz8Ajr14hQLU8znLxW6gAgjhAMVT5HlCIPnc6_3LdjKTFaJ9ro-mRduuAIVEtnpgITq1k1aiZfrvIdS-4DIzojBG7yqIvCtt_cZiNMS-SgF1YbGYTGlaTGW0P4HC0PSvjEOl0Jxs0SlrBCYVbcT9VtNLKSfxBKN5V0DAAQ4XVqinONC1olcGYIew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
اتاق جنگ اسرائیل:
اسرائیل و لبنان به تازگی در واشنگتن دی سی توافقنامه‌ای را امضا کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66882" target="_blank">📅 21:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66881">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">‼️
🇱🇧
حزب‌الله تصرف تپه «علی‌الطاهر» توسط نیروهای ارتش اسرائیل در جنوب لبنان را تکذیب کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66881" target="_blank">📅 21:08 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66880">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qTxzdzTtoLPXAaIHb9PrFEI6-5iSWQ9OT1JCraFCsOK5DZIOc3xdjsPF0ccSQmVUuxYiRfzbP77Y7os_IV9VGCQj7p6fz7A6tncHUnylyReY72uUZsEPV2GG-eLpi_8lcyKD4bP1tYHtP3wVyFrG1WJ9xIComITjYmfYvX5C8QH8Gg465v-kaNo9nyQ9sf7R0qTTZ60rYDQpUVF1A-hJWnQH8pxVkEdiHZjsKv7pL8i8kigAkSfefJLcDwdeQs4XOIv8eIQXpYTo2J-eyvR1El59hk4-_apIifb_3U1EYXiMhL4-qlx9N7sICK_DBeoZlneaFTzwVsTienETcMYrbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
باراک راوید اکسیوس:
مقامات اسرائیلی و لبنانی به من می‌گویند که انتظار دارند پس از چهار روز مذاکره در واشنگتن، امروز توافقی کلی بین دو دولت اعلام شود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66880" target="_blank">📅 20:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66878">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E1ulUgHkIey6LMac6kFmh8sSihVumSrPpuzB6_I7_WWcTLKTCUgKn2p2uhrnM8CxsNzrHzw1A2J4CW_K-irYHM2EaVsOQY34cJlVgNASppg6-t3A4YLmJ-tKnV0e-JYwROhBEVJezriL4k8FeN1DweorBr413uZy9UjuUrFxtQ_LX9bue5y2DupfJ9uMBZlwaypxKk8CXAqJBqHSt7-HIhD6Pmc_czEym2tjoAZenl-qmeIgCNassm_KIzoZA8_Lv6DZ7O53uHk1OJS5g3zatQP13trVUJl9KO4y98OTviNwbpT2o3O9pgjrbf3Zqv2gGvWg4yLZlqdlNUBbow_Sqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HOu6j0D43QutiDtS1hXWMSYY7HyOGKwZ9zjacrqo3J18Zk7X3shjTnGnVvo7Ry4xDs_Pp0ALOtbrNJ8nJr_Oq9rPhzX3SMeSnUI5-Rv1X62KGThY-n1fOhat6VtQx13OKAm79agj6uwilIRJJD9a19t5-T-BKMFX--hBCw1wDsROo1UQJYsk2HjBy8dBx-HSIjIkkCgO2k5464tASNGYKeOD19f9YZKk2k9SQRvBmUIESnoHDBipRr37uDjLpPZPvGjEtR5kFX9stpH_fWTM9WhVO3M_vQOOgis7Owghk5rNlGl_4wTuN9UcneovWGSM2RFx3nRxTF-TOb5d4nlPFw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
در فاصله چند ساعت مانده تا آغاز بازی حساس جمهوری اسلامی و مصر رژه‌‌ی همجنسگرایان در شهر سیاتل آمریکا آغاز شد!!
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66878" target="_blank">📅 20:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66877">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lNKGdqSnziT3uHxSf01xFMVaF9hTs4tZ4odrOjXK0XksIlGtHJGNj0KCW2WnS-9g3XUwOpcdc4oYhAOZZfwJjvdzEb4ZGZvuQPG9gfYhzsdevSep3Tso-myCx2iLWX0YB4WTTfm1O7siWP2gZwjvqPa8Y7PNmVPlYAIdoLT4ndPmJx3bVM0sRbqUmTiLSxtafu_yd5TUdEYf08lLoTh_ZjsZOXd1s_ojmwlBHJ7xsTfaY4MMm94ZfR23B05dGJUCtj7-GFxliVAqZ2VXm1GhxQtEq6dZBYBpPpFBucFtJhgkZwPYN3SP7NyqU0oGmYfkBzadkBQ2C2ObTcAWpUL__g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: ایران حداقل چهار پهپاد حمله یک‌طرفه را به کشتی‌هایی که از تنگه هرمز عبور می‌کردند، شلیک کرد.
خسارت وارد شد، اما کشتی توانست به مسیر خود ادامه دهد. ما سه پهپاد دیگر را سرنگون کردیم.
بدیهی است که این نقض احمقانه توافق آتش‌بس ما است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66877" target="_blank">📅 19:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66876">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uf2cATGwsjayOeANy-rPKQpx_7eUDf6X8daybiMrXDgRkhAz_I71aM2ZouRl5GyP3y9fHri0lBeYaS2IkOnOW-bu93qvFx0mejt3H7srkWxZM0UmDb4RHIkLuuFrzquFHhSOgwvQ9hpGITRm2aca8HuCixsFgT5LIzaMTHXfnZ2MjSGrvBMXo7dnxxTEMQeIEumVfkI1a75sMqw4HP9XugFnqcAdoFQcirFi9ArN3OlGb1rkr6O5ndqCuIttkLLz8g0-9TS_4rvFWzEPBucYNRl2D1lovgsjA97JZWAPOQDINuZGRo8Q5eJdZItiJ1x_2O_ZC0w3hF_xVsozNnLr4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بلومبرگ:عمان هشدار داد تنگه هرمز به شرایط پیش از جنگ باز نخواهد گشت، کشتی‌ها ممکن است مجبور به پرداخت عوارض عبور شوند
عمان به متحدان اروپایی خود هشدار داده است که تنگه هرمز به وضعیت پیشین خود قبل از جنگ باز نخواهد گشت، که این امر نشان‌دهنده احتمال اعمال عوارض عبور جدید برای کشتی‌ها است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66876" target="_blank">📅 19:27 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66875">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LFFytp1dtyWy0luhPq7a0yceBi299hhMiVyYNVhMOVkF_3wyXOo9k1i_-WiyRfvwV9ZhVrJuJEuGoMjJNjikwWF4WbpUPXz2ZNqoaxxMdhMpuJQTjzge_KDpRXpQmDJYl_2eo2lhiJ4iomfYBhMd9okyeP6GcGL0fD9ZB7uEJfESM6PltQHq6HtqFIowm8_RZnEKJkDy5I30nSDdM2FgBifhRVssJqb4TkuY20hyf5u4JLvaepN34ZbEj4JXb4DhRiKwvG_en3KIZgo48dMsOmcKjpTGb9V7lwZYeKgvOfw6zYaNjsEw1xRdUjUU_pJpYZ2yojvAGHzsmzFmmvyVbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😢
رونالدو تو جام جهانی گریه می‌کنه؟
پلی مارکت می‌گه ۶۵٪ بله. احتمالاً آخرین تورنمنت ملیشه و دوربین‌ها منتظرن. البته رونالدو رو که می‌شناسی، شاید حتی با قهرمانی هم گریه کنه!
قبل از اولین اشک رونالدو، پیش‌بینی‌ات رو توی 30 ثانیه روی پلی مارکت از تلگرام ثبتش کن
👇
https://t.me/PolyBaaz_Bot</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/66875" target="_blank">📅 19:24 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66874">
<div class="tg-post-header">📌 پیام #59</div>
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
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66874" target="_blank">📅 18:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66873">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66873" target="_blank">📅 18:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66872">
<div class="tg-post-header">📌 پیام #57</div>
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
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66872" target="_blank">📅 17:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66870">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/66870" target="_blank">📅 16:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66869">
<div class="tg-post-header">📌 پیام #55</div>
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
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/66869" target="_blank">📅 16:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66868">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/66868" target="_blank">📅 16:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66867">
<div class="tg-post-header">📌 پیام #53</div>
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
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/66867" target="_blank">📅 16:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66866">
<div class="tg-post-header">📌 پیام #52</div>
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
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66866" target="_blank">📅 16:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66864">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/66864" target="_blank">📅 15:35 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66863">
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66863" target="_blank">📅 14:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66862">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">⚠️
خبرگزاری فوق معتبر فارس:
درب تاسیسات فردو، نطنز و اصفهان به روی بازرسان آژانس تا زمان رسیدن به توافق نهایی بسته است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66862" target="_blank">📅 14:13 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66861">
<div class="tg-post-header">📌 پیام #48</div>
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
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66861" target="_blank">📅 13:29 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66860">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">❌
قرارگاه مرکزی خاتم الانبیا:
🔴
پرواز هواپیماهای نظامی اسرائیل در نزدیکی حریم هوایی ایران یک تهدید مستقیم محسوب می‌شود و اگر ایالات متحده اسرائیل را مهار نکند، ایران این تهدیدها را تحمل نخواهد کرد و حق پاسخ را برای خود محفوظ می‌داند
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66860" target="_blank">📅 13:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66857">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BZJAmX-2U65z0hiTlZbn6GKOOA1XQQ9UL_wmIg3K3a3L71oLCBzpCuElvWLtynCPjvPTOr-9B6fDbgNm7gJEFWh8T5yrkuOiCEvPjchllBBUSqwjCK66IN4bJYRyLaLz98fnU9am4Wc1oxKpPBo8wLhOk3p7ASuA7tIFIfwKopdUziZLxqLfmrfOjPr0orE5-6nB2C-aS0w2YyLEwlCtBclUXJoGMzY_0B4Lg1QKSYV1g_x4ke93jVgkQKriqIBCA0UkNo_4iLxUcKryCOqPRvu8BGmmj5BCJP76uSV8x4s841dz7jIEXhYCjAQJLJoPQk1sOChrcK_jE0uQkAm3vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FRW-_nOYH8W7tdiiiosw824m1YS8HjsMh3oPIGHjIG_cb4Tt3F1fpXDm5almHG_cWo5awOVv5LOXyKIlSBcBzwRos1FCMaDTNhhZFgUP5TZMld-W1ORKEcsx23Vg2ZfzQbYaN7Spxg0HjhE2IkoN7EG5JVQHh3O7UM4KYH0uGlMLBIogHF4EbaT4HlJfkQcK5KOkJZnaVkMpJxl_Z9TKaMn-mm6cf5Vp6-NWVZCcnpR66j9cigrLg9Z7L4ESgOu_K4LMdozKBhIoX9fHhjAD4v75iK4MBbcfT6C2EFeZjpvhxMo6S2sldgdRiw2OAOLAchv7Cm7dBO3yM4i2ZyID1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M0W1Pxt2pmC1L6g76UosOa90zJ_HUPrScqtQghoMCSCm1H1WMR9iDEASg1ZCDcN9wULgnJibSeEn5OUJyxtgnhGjBejsW9qDgt05ru3bxcCyHIUl5cZOR6Y_RQbLuvOZJfOIDdf7Pz5SQ8igeMTRlOktlc9lAM1nXISni6NZ4oiOvVJPeMIikO4PAopxLq_e01pP2WVDW1bPVbx3KKG1niI0Etb1JnUBoi9MenYZH-KEgh23rxRUEVZpgEUAh3nqFeSZ0AscgqF6FZwmD0noJuIenG0zyLhHm_3GKDHm3ySeFo34reizc2DNz_gvOgaTUbNCc3w9rbPGWBQYqIQO6Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
حملات هوایی صبح امروز ارتش اسرائیل به جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66857" target="_blank">📅 12:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66856">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67fdc892f6.mp4?token=rFnYdWj5_vDeni9wWR-yIvO1Jy9NBiw5m8KbOg6KzAGZj-TQDCNn1P7-xfVjBvihtvX7JJyZiyPNvaKPjKhHBWvGdk7H2SwRAmIBYl_eu7W5tb7CQacI6IY0gBpHSr1o0Fi5OPuMGnWxyLtXiu_VsVhpY5zGzrWKsBZLP93EN6YylZUUykp_jd-Hm__IgYoarihiBPIgrZM-OV0_-j_VDBYUkf5Rur1DtWmzmZjEiccDYH4-YwvNXDlMiuguYAEZ6hbnLpLW_q_kxnTx6i6-b9pCyDplorZjYAU9Mg8wuGZ0BSri4uYuDYKjRRBR3_ysyvfmrzuKFdt4kcOUy5YICQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67fdc892f6.mp4?token=rFnYdWj5_vDeni9wWR-yIvO1Jy9NBiw5m8KbOg6KzAGZj-TQDCNn1P7-xfVjBvihtvX7JJyZiyPNvaKPjKhHBWvGdk7H2SwRAmIBYl_eu7W5tb7CQacI6IY0gBpHSr1o0Fi5OPuMGnWxyLtXiu_VsVhpY5zGzrWKsBZLP93EN6YylZUUykp_jd-Hm__IgYoarihiBPIgrZM-OV0_-j_VDBYUkf5Rur1DtWmzmZjEiccDYH4-YwvNXDlMiuguYAEZ6hbnLpLW_q_kxnTx6i6-b9pCyDplorZjYAU9Mg8wuGZ0BSri4uYuDYKjRRBR3_ysyvfmrzuKFdt4kcOUy5YICQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ درباره ایران:
«یک بازار جدید دیگر هم در راه داریم و آن، کشور دوست‌داشتنی ایران است.
ایران کشور زیبایی است. کسی دوست دارد به آنجا برود؟ جمهوری اسلامی ایران با مشکل تأمین مواد غذایی روبه‌رو است و ما قرار است بخشی از پول آن‌ها را بگیریم و آن را خرج کنیم. همچنین قرار است مقدار زیادی گندم، سویا و ذرت خریداری کنیم و این روند به‌زودی آغاز خواهد شد.
این برنامه هم بسیار بزرگ خواهد بود.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66856" target="_blank">📅 12:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66855">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nITjEOCo7zq3-KFNNFL3EywsvmFcBoFA-Ll9wAczYdO83FiQcuesHZhbikeYHTBYlZLmCz4CLddk1RepvulkVLLgi_Drj2t4pM8ku26vrHubEWoQTidLJQCeC66U7rNnHglW3StTKQAfP60DCItwKK2CRNdRe77BqelE0LtYHUDnjr5t3p0sG-uBjWKJdbv4GHY4ogTszhqhWlphMf8ccH_IQ-sO9MbazgTx9W4Xzm98LH6VX-gwha12tmfqDVkWV6lVBo2ArpemyuoiLqK89llA9iuuQtDSWDB17GQPSyikvReU8GYGpwc6TWp-7Mh261XUrILQ6ofm2AFm8MFNZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇸
پرزیدنت ترامپ:
روند خرید محصولات کشاورزی ایران از ما خیلی زود آغاز خواهد شد و من انتظار دارم که حجم آن بسیار زیاد باشد.
ما پول ایران رو گرفتیم و بجاش ذرت و سویا خودمان را دادیم!
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66855" target="_blank">📅 11:03 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66854">
<div class="tg-post-header">📌 پیام #43</div>
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
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66854" target="_blank">📅 10:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66853">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aefac4ff7d.mp4?token=LryEEzv6nguFCnYdbJbr_T7hdHfUKTaoEAHNCCr4yxmBdFcou7QUUC-oM-VlnBpL6_ZA_3aNi29UU39sgnDTdE_od6V4DslmGo5__mCaaXrKnHnGVkNJ7pgNd4NlOUV0DLMo8bfvWP0xxXPD6FZUP7UIHUINoynH7fC9aFsCxUVOpM1rzTlClV4BX3TC2gQ3JkOd7Mv-cD9FTlbDC6R5e1Gd4ePbTj2_w-WlNV5Y8eJ2bxvIKjXP9zpRAZvERX3R-Y6oRWaK7AtdthfcOTopvoBEL2doz5Hmoi8P0b6vTV9gtJKg8kQAoWfg0cH3ywj072nueR8F5zIvMu5dKaEHHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aefac4ff7d.mp4?token=LryEEzv6nguFCnYdbJbr_T7hdHfUKTaoEAHNCCr4yxmBdFcou7QUUC-oM-VlnBpL6_ZA_3aNi29UU39sgnDTdE_od6V4DslmGo5__mCaaXrKnHnGVkNJ7pgNd4NlOUV0DLMo8bfvWP0xxXPD6FZUP7UIHUINoynH7fC9aFsCxUVOpM1rzTlClV4BX3TC2gQ3JkOd7Mv-cD9FTlbDC6R5e1Gd4ePbTj2_w-WlNV5Y8eJ2bxvIKjXP9zpRAZvERX3R-Y6oRWaK7AtdthfcOTopvoBEL2doz5Hmoi8P0b6vTV9gtJKg8kQAoWfg0cH3ywj072nueR8F5zIvMu5dKaEHHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎯
ارتش اسرائیل: ۶ عضو حزب‌الله را در جنوب لبنان ترور کردیم!
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66853" target="_blank">📅 10:05 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66851">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73a731d25b.mp4?token=X0HhP7cEIwIntHx10h3J20w_SFP76TIUQh7Y6j9F2eKBHhbo01JpeYhEks1Fk1le80M2TRSWbSbyFrzxjw-GrRm4UYO7Ax91AQ2p5uia2CfUB1VXWOHT5vwt76tk0-_aPUCqdcECCx99ID_28wCWBjkYh9oOtxqKmqHz-UGgWTcJXgJHzJ61oGQgJo9U4cdmz541FKWN4BOxXRUNWpIVAGsyvZcML4iIE9UUAqO7DFlnqTEiVVMbUEnH7QzRMPVPL6rm6OtctVpors8qUPB4rejFgPwE2l7N4YZkRPL1Rm_8h0uMehGwGXaRKCnrcDZsKxtyehXKBKD4FWVpOgdx4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73a731d25b.mp4?token=X0HhP7cEIwIntHx10h3J20w_SFP76TIUQh7Y6j9F2eKBHhbo01JpeYhEks1Fk1le80M2TRSWbSbyFrzxjw-GrRm4UYO7Ax91AQ2p5uia2CfUB1VXWOHT5vwt76tk0-_aPUCqdcECCx99ID_28wCWBjkYh9oOtxqKmqHz-UGgWTcJXgJHzJ61oGQgJo9U4cdmz541FKWN4BOxXRUNWpIVAGsyvZcML4iIE9UUAqO7DFlnqTEiVVMbUEnH7QzRMPVPL6rm6OtctVpors8qUPB4rejFgPwE2l7N4YZkRPL1Rm_8h0uMehGwGXaRKCnrcDZsKxtyehXKBKD4FWVpOgdx4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قالیباف با روسری و ماسک اومده بوده هیئت
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66851" target="_blank">📅 09:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66850">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cff13197ee.mp4?token=Fx7hEt3rJEcpobxZXVQPg3lMWSSxWCc-49aTDyakj1SvR3kBt1cKJ1ptWo5ujNsjoMtL3XmqDrQg3m096DjlQEeee7hoyVNd5vQkMdYn0oTj00S8ecI2wDLNtbVMmwY7PWtA7zfZTmtRxuZ3bOOt3-OI7HjUgkjzNQFzn9Ns_52ljTRO0vUHrLJRgHW-Do50wDqxCGWvNSLvUBQkVqLoIN3aNfywKJ_DvcXjE6OJpFhSWmIDSrwi2k5mhKF-qyLqt7i7b6nPc7U57ec4Jj3Wd-1xZhbYL9DEK372OOseOGQEaiZ0q31NCIaWRy5nRwyuU4jVB283GtggqCMIJXtrWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cff13197ee.mp4?token=Fx7hEt3rJEcpobxZXVQPg3lMWSSxWCc-49aTDyakj1SvR3kBt1cKJ1ptWo5ujNsjoMtL3XmqDrQg3m096DjlQEeee7hoyVNd5vQkMdYn0oTj00S8ecI2wDLNtbVMmwY7PWtA7zfZTmtRxuZ3bOOt3-OI7HjUgkjzNQFzn9Ns_52ljTRO0vUHrLJRgHW-Do50wDqxCGWvNSLvUBQkVqLoIN3aNfywKJ_DvcXjE6OJpFhSWmIDSrwi2k5mhKF-qyLqt7i7b6nPc7U57ec4Jj3Wd-1xZhbYL9DEK372OOseOGQEaiZ0q31NCIaWRy5nRwyuU4jVB283GtggqCMIJXtrWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
فرماندهی مرکزی ایالات متحده:
جت‌های جنگنده اف-۳۵ بر روی ناو هواپیمابر یو‌اس‌اس تریپولی  (LHA 7)، ناو پرچمدار گروه آماده آبی-خاکی تریپولی/یگان سی و یکم اعزامی تفنگداران دریایی، در حال برخاستن و فرود هستند. ملوانان و تفنگداران دریایی ایالات متحده در دریای عرب در حال عملیات هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66850" target="_blank">📅 09:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66849">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">میخوای به راحتی از فوتبال و باقی ورزش ها کسب درامد کنی؟!
⚠️
پس همین الان وارد کانال @Palang_Bet شو چون بهت اموزش میده چطور دلاری پول دربیاری
❗️
💵
اینجا میتونی روزانه درامد داشته باشی و سرمایت چندبرابر کنی @Palang_Bet     @Palang_Bet</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66849" target="_blank">📅 02:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66848">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hf3L7WXdqOwMj3rQB_OxbVn1iTPZJSEAENYV8G3sM0zAgEgwmz3BTE1NPmg2Pl5xLYBvHdR07AoUZof5DafZS0T-TsjP8sPiA2Io4mxJ2Mpo8ykMCzhJOSPbGxrggRiH2Mz41JkcifMM-60cyPbklE32vKoHARK8rShRFCk6NzjCF0j_bsxY9A4zYBMSJLC_9nt_k2oK0K6rvaeGoU_XpV7CMg4GUOzlI7N5mf4mO_E3Gj6UySYkD0uYYfFm0exSgLqptmRofc6JmqrNM4xhvXG4Itz9w1mvM0UnYB0DzDHsxvyxLiI33beRaevCmgdD6Ni_s5ewf0XQqmstKDiqMw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66848" target="_blank">📅 02:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66847">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kvuEpmXJDgxys6NGb98UXP--4tdzK_0h52kSdJe2ByhPXeB0-dC967AfwDJsOSi7lHreNqtJ3e9z9If3Uyz-64eObq6D_0FHuuve1tc_9XKLIOQHFXMBRsOtMzJJKTDEMzuT23LIU9PB6bEatkssrScWm8NBMuPPrPDNzIHjW8UzS1PvDo-eoi_msW1y_C4YZnMwJp5v96DDLnMlvv0FQuVnqBtSesk3G17Bu16ZPZ8lG7y2WtUt3Onv2CHRP5WCE4hWmwCFXFEt5XvBXrBqY7K9dJEgv696XvBM2aTXy7BAMkE3a3ARz5OIZgA6541QN50m9WEyBtTq4IM0yF1aNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏بر اساس گزارش وال‌استریت ژورنال (WSJ):
🔴
ایران روز پنج‌شنبه به یک کشتی باری با پرچم سنگاپور در تنگه هرمز حمله کرد؛ اقدامی که به‌عنوان آزمونی برای توافق هفته گذشته میان آمریکا و ایران جهت بازگشایی این مسیر حیاتی کشتیرانی تلقی می‌شود.
این حمله به پل فرماندهی کشتی آسیب زد، اما هیچ تلفات جانی در پی نداشت.
این حادثه چند ساعت پس از آن رخ داد که ایران به کشتی‌ها هشدار داده بود از مسیرهایی که مورد تأییدش نیست استفاده نکنند
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66847" target="_blank">📅 01:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66846">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">رسانه های اسرائیلی اعلام کردند طی درگیری ارتش اسرائیل و نیروهای حزب الله در منطقه بیت یاحون در جنوب لبنان چند نفر از سربازان ارتش اسرائیل از تیپ ۷۶۹ مجروح شده و با بالگرد از منطقه تخلیه شده اند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66846" target="_blank">📅 00:57 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66845">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">با بحرانی تر شدن وضعیت ونزوئلا و مفقود شدن بیش از پنجاه هزار نفر گویا به نظر می‌رسد مثل زلزله سال ۲۰۱۰ هائیتی که ایالات متحده آمریکا به این کشور نیروی امدادی/نظامی ارسال کرد دولت ترامپ هم به سمت همچین سناریویی پیش می‌رود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66845" target="_blank">📅 00:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66844">
<div class="tg-post-header">📌 پیام #34</div>
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
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MMNjBCu4I3pk-Dnh76dHDkWP_HU1YlYzIWQAjBufGb0syKQomFZl08jMgWCd1vkW1-8daqU8IDJlCT0ft-uwBSs-a8kwXhjX-fGuSILyY5LDwEfjFeUn7BQCzLry4Hnp077kEat3sxXogNE9nUHcZfNOPAenM9yKEp3D-Ow1HGohAhzYkrEakaDijaVZ2lPuBB-WaC_gj2q28P0TzTv-ujCxVF5OuSxuTf20h8O4VvDBtYXcnk9BmV7ObMYCtJU4jAodp8hEegFZg6cMZNbvC9YdhYxzlhVVuSB4h9dMUWufGCH69xwWbTNprSsot9wEOxQAS5p2EvCOQnaoD0lY5w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66843" target="_blank">📅 00:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66842">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YXHwh3ixYb2I_yZVr0H160ZRD8YpdxOsHC9Dg5FmQYFH3miiURp4SPM2n0mZlRdKRik-ROyh5XxJa-tyblh6wpJlyRERVp04p5GDmJ4eotuHlIJcsglEQPn2pqU78VDykwFf_fCjAUmlP_2FM-RhjXfRYRFS0Z_A3gtBMZHqLrdf1pfbbfkHBIvJj62PLm3nU8EYV2Z0Ci-1pZzFeTC_vJARBtm8rMF5HTMUP0kBXR58Jkq58lGXd0YHaNS9Y2HtjjqCS-3XkXHa28zkMQys3cUMlnHHss4pMuFYQuAreewQCH7ueV-SwO6FzZccJfcL-RA-DarGaa4qs6yvdUBamg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
گزارش از لبنان: جت‌های اسرائیلی به بیت یانون در جنوب لبنان حمله کردند.
این پس از تهدید امروز سپاه پاسداران علیه اسرائیل صورت می‌گیرد
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66842" target="_blank">📅 00:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66841">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b6d00bedd.mp4?token=AlvDB8TvEMhuo0kEYyKEFD_WU537-F6HFonQXrXdN7zpGrs9RWSfEqFdAwP_EZpY5bH2dAHtdd9XsOdBb09ONQfT42RNZoeMwkOSUWXdGf-cAF9_fYWT2PFXmvla3RcA-4yoBriT7EAgwZ3oshMSmGgFyWfFSQsgjQuNh-wtOtgo-PZ5qgTvbg_cVOBmSxBzCWxtew6NjcueboIPbSNhO1NtP4u1bQ0mFRfIgOtNKQQO9AuGL1s8sybJQ0BZcc629wggtzSY3BxP-JgEfvmKwQ4hqYG-TmrT70BzmdklAZlHGNy83oQgmwE5UtiNCje3xHGKreS4A0CuA-NY_4j0rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b6d00bedd.mp4?token=AlvDB8TvEMhuo0kEYyKEFD_WU537-F6HFonQXrXdN7zpGrs9RWSfEqFdAwP_EZpY5bH2dAHtdd9XsOdBb09ONQfT42RNZoeMwkOSUWXdGf-cAF9_fYWT2PFXmvla3RcA-4yoBriT7EAgwZ3oshMSmGgFyWfFSQsgjQuNh-wtOtgo-PZ5qgTvbg_cVOBmSxBzCWxtew6NjcueboIPbSNhO1NtP4u1bQ0mFRfIgOtNKQQO9AuGL1s8sybJQ0BZcc629wggtzSY3BxP-JgEfvmKwQ4hqYG-TmrT70BzmdklAZlHGNy83oQgmwE5UtiNCje3xHGKreS4A0CuA-NY_4j0rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #30</div>
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
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66840" target="_blank">📅 00:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66839">
<div class="tg-post-header">📌 پیام #29</div>
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
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66839" target="_blank">📅 00:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66838">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f455bc9393.mp4?token=dRwrih1PqMeGO5ENZas-kc7kZZp_-lt4llrttZ3LI9YzM7PkBDRg67Wmvj_JDqqX8qnMUbTK5AqQzpMcIK7y1XRjPjSt02mKHSWtTf6kxXioODF2RFp2MAxtWmDZsjY5ws1KCjO4iuTahfWKAphLNSGOlrK6vRDeGZPiR1PsKYw6VJqyL6zi9tktnlrInRZdYBUirCD_OoYrOmbbd61avSl7ZwtVEj0G71P_yJY6A75j8VofkFMgt6R7ZXZYdurJSiDBBWHvGQGQqdg5JHqXveV2ZHqRiaaPg8xkHWdyU8Q1lIVlVFoNyty6nrBXKELKCg5bTYSpYVRLvcloifuw6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f455bc9393.mp4?token=dRwrih1PqMeGO5ENZas-kc7kZZp_-lt4llrttZ3LI9YzM7PkBDRg67Wmvj_JDqqX8qnMUbTK5AqQzpMcIK7y1XRjPjSt02mKHSWtTf6kxXioODF2RFp2MAxtWmDZsjY5ws1KCjO4iuTahfWKAphLNSGOlrK6vRDeGZPiR1PsKYw6VJqyL6zi9tktnlrInRZdYBUirCD_OoYrOmbbd61avSl7ZwtVEj0G71P_yJY6A75j8VofkFMgt6R7ZXZYdurJSiDBBWHvGQGQqdg5JHqXveV2ZHqRiaaPg8xkHWdyU8Q1lIVlVFoNyty6nrBXKELKCg5bTYSpYVRLvcloifuw6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مفقود شدن بیش از ۲۱ هزار نفر در پی زلزله‌های ویرانگر ونزوئلا
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66838" target="_blank">📅 23:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66837">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KWxCdlcq7P08VYS8NBGsI51fLNrkO5rRAiKXXBs_2BaMQijv7wxlm7_soWtm1tBPQmYvzeZgGlDy9YH6m9RibEuJcT8G7seISXcRxwQ49UkcSvk_5eX0u36OeJk8yDRlJNWtDBx4RknL6RmMG6V_n5SUAnAGauAan80ngabom4Ib2rZAC_LhGiVwQvExMU4sWrAKm_6ShTC9iIx0HI9jHs3GWsNvdwzIaIliNNWIS3XNR3ngWBn-uxXS4-WTJN3fTlx545W_EGr7skU5Fucj-3a8py0yj0lxRpTGlZdWgo9CKOGy_epFHZ1jBpFmviNKHguRMrc1uuqZkMbQAsEwJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عراقچی:
پس از بیانیه مشترک اخیر در مسقط، تماس تلفنی سازنده‌ای با وزیر امور خارجه عمان داشتیم. ما مجدداً تأکید کردیم که ایران و عمان «برای تعریف مدیریت آینده و خدمات دریایی در تنگه هرمز» گفتگو خواهند کرد. ما مصمم هستیم و این کار را با همسایگان خود انجام خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66837" target="_blank">📅 23:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66836">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eab5d7e42e.mp4?token=obndtTDnNx7jkp8k4bkTKhk1o65P5iB--Oqbtutbcj6H9rj2utgwerqh-WHOZyDqpOmXTumFyzk2ZNwEgR80wEJok_zMqJGQQyiPD37n2PD5J_91aDb3GEmVBul79P8kg8r5CGsDtCvVdvPqhJbdbGtIbcIBBFmKV8l2431WT0oHMebHBcrxyXG5MWLHOab7ovz78Z-v3r9cOWQxa2ShX7XlEP6bXOF7cutevb56mm7vilcNpX0ksqfz3AZ1EOG-7hPKDHHHQ-uptQ-szBZP52r6BmzM8JZvpI1C6IkG4WeGh_quQHSPiQfJT6v8MyA3-SUffZSiBKTTDHXiZ1TRkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eab5d7e42e.mp4?token=obndtTDnNx7jkp8k4bkTKhk1o65P5iB--Oqbtutbcj6H9rj2utgwerqh-WHOZyDqpOmXTumFyzk2ZNwEgR80wEJok_zMqJGQQyiPD37n2PD5J_91aDb3GEmVBul79P8kg8r5CGsDtCvVdvPqhJbdbGtIbcIBBFmKV8l2431WT0oHMebHBcrxyXG5MWLHOab7ovz78Z-v3r9cOWQxa2ShX7XlEP6bXOF7cutevb56mm7vilcNpX0ksqfz3AZ1EOG-7hPKDHHHQ-uptQ-szBZP52r6BmzM8JZvpI1C6IkG4WeGh_quQHSPiQfJT6v8MyA3-SUffZSiBKTTDHXiZ1TRkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
روبیو درباره ایران:
ما می‌دانیم افرادی که هنوز در بالاترین سطوح آن حکومت حضور دارند، همان کسانی هستند که به همان ایدئولوژی و همان طرز فکری پایبندند که رهبران پیشین آن حکومت به آن باور داشتند.
نظام ایران همچنان توسط روحانیون تندرو رهبری می‌شود.
همیشه همین‌طور بوده و همچنان نیز همین‌طور است
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66836" target="_blank">📅 22:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66835">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd736f47d9.mp4?token=kSBVqM2o9IR5H5K8pNsKCgNTHF3fBxKKo3gvMNoYljKkRetervA9l2LriAU3epgRlXaVo866b-6qhgbwvgmlHkwE8YX8xV7o2HX15Q-ItlmIQM_9qHqOFD6aPkPe93AR8SC7KOhwnXUyFwq7I0KyLYk-iy9kCdaqetruTJBD-RvUxMBJ8McUHxnsMcAgEQh5RgyznYwf7Xo5Th0aQnB8uVhsm7v2n4NyRf-dBQSunQFOEmNwRVKhMJGiUZj-YuRtQVPRbpU3UL8pKDl_O5MBFZyQQQd_DYGzPjJyxgO7xGmEY0KNqAhdeTob8BbSQ16CxdHNhkfy2aQzZ5WJTMDsew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd736f47d9.mp4?token=kSBVqM2o9IR5H5K8pNsKCgNTHF3fBxKKo3gvMNoYljKkRetervA9l2LriAU3epgRlXaVo866b-6qhgbwvgmlHkwE8YX8xV7o2HX15Q-ItlmIQM_9qHqOFD6aPkPe93AR8SC7KOhwnXUyFwq7I0KyLYk-iy9kCdaqetruTJBD-RvUxMBJ8McUHxnsMcAgEQh5RgyznYwf7Xo5Th0aQnB8uVhsm7v2n4NyRf-dBQSunQFOEmNwRVKhMJGiUZj-YuRtQVPRbpU3UL8pKDl_O5MBFZyQQQd_DYGzPjJyxgO7xGmEY0KNqAhdeTob8BbSQ16CxdHNhkfy2aQzZ5WJTMDsew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پزشکیان:
نمی‌شود برای امام حسین اشک بریزیم اما در جامعه شاهد ظلم، بی‌عدالتی، فقر باشیم
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66835" target="_blank">📅 21:49 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66834">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FjlWlbHz-2YN_2aZcMuoxFWbJEEjkUrlwXJ9fqNiikRtZySfZiJmklGrRJ1t56tvx0EunQhEUA7akHWWpXHq5H62jppTVNGJgnfkbRCu3FuAkVIm3jQKSYAtFFA0KV72bhEI3oT9GOB4_BdgIjvhudzNcpyJtPvY22zYiFfCu31lbilJPOogVHReNS3VK2aIHQJQRQRUZF9YhqL7ZujQ6SLUlzLx5KWKuRnTPh-u8D9JJJ3uVRKYxaO6cyArwR5CKc6KzvhCwc8EwtIE5tccbcRsSztwolyQNEHSQ8ZNqUwoY3AenyxlMdBoIPqp4yKhf_SUEpKkFHvCAE5rLxuXPg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/965348f417.mp4?token=u6Oz8qL-S3earQ2LoYfNlmtaHAEC7rlyz0RoCUgI3wt2ecOp2wjaVEtmhBFDv_FDMt4jeIbsbcP8iBLTukhlkL9snAvo2R-j0VQHIJw1uozMy7i48n9_M1FN7_OMPrKqnVYfejzmPXQ0ea0DQrQurcATRXEowR6E5OeePJnZk0ogCsLMqnPUBWSkU1R1aiDJ7KQlCALkRekL2FG9EvJm_u0OBJIoRBozHgUfEsRjltG-6J2PW0yfnrMjZPrmz5GcYa_mEUi-cgmKnxs7bhRkrpmnaZnYDsRF81uWxMN2_vfiAjA0ay2WdCMqJ3F1gSlJpxoMbUnLGLchB8EQzWBIpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/965348f417.mp4?token=u6Oz8qL-S3earQ2LoYfNlmtaHAEC7rlyz0RoCUgI3wt2ecOp2wjaVEtmhBFDv_FDMt4jeIbsbcP8iBLTukhlkL9snAvo2R-j0VQHIJw1uozMy7i48n9_M1FN7_OMPrKqnVYfejzmPXQ0ea0DQrQurcATRXEowR6E5OeePJnZk0ogCsLMqnPUBWSkU1R1aiDJ7KQlCALkRekL2FG9EvJm_u0OBJIoRBozHgUfEsRjltG-6J2PW0yfnrMjZPrmz5GcYa_mEUi-cgmKnxs7bhRkrpmnaZnYDsRF81uWxMN2_vfiAjA0ay2WdCMqJ3F1gSlJpxoMbUnLGLchB8EQzWBIpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو:
فقط یک آدم کور می‌گوید هیچ دستاوردی وجود ندارد. دستاوردهای عظیمی وجود دارد.
من همه آنها را فهرست نکرده‌ام چون می‌خواهم شما را نجات دهم. شما اینجا زیر آفتاب سوزان ایستاده‌اید - فهرست کردن همه آنها زمان بسیار زیادی می‌برد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66833" target="_blank">📅 20:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66832">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PWCveC5i3Vbqn40JYUxWmpEOG1W1-zgac3fhqzJJvYxvhBQguHUkqkdZJhMLzYX7Riiv-_2cGg7qtIY-cbsQ9J0FNliv4HpT2XAzz9NSnaOR-KHUHWhs42EyFZzX4drveg5M5ea93utoSuV9d6kGAuEJnRPEjjy0_DgizdsptXrfBTzNlCdd-7CrPSnOEB0AjFAVdr-qUx3JwzJZ9nzzsP2zZ2U07Qh21qMSZ2-O0bBYUvUawV5XltAkbnoqzX75CBJhLDSP0o9ARJvW4tHOFUwinxoTnwTHRywgSV1qIZHFp1YSwG8DI4Dnhog8xFb3aZ8Kfiuqzd0pJuBxljwIQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عراقچی:
با نهایت تاسف از وقوع زلزله در ونزوئلا. مراتب تسلیت خود را به دولت و مردم ونزوئلا، به ویژه خانواده‌های قربانیان، ابراز می‌داریم و برای مجروحان آرزوی بهبودی سریع داریم. جمهوری اسلامی ایران با مردم ونزوئلا ابراز همبستگی می‌کند و آماده ارائه کمک‌های کامل است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/66832" target="_blank">📅 20:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66831">
<div class="tg-post-header">📌 پیام #21</div>
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
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/66831" target="_blank">📅 20:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66830">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fYmjD7obYXf-rEqDReO2jl8rGyeZde7Gq4jOMqsKbik2aimCg7UHcC5Zi5Ck_EVQxIGhjwSiHUCE69xmZ4SyGze0T9QXx2G12cMgABz0YryrmJeILXXExxCm0elefUyHYVeEmvNFr16XqoCqNJ43c-EM4WxPFEeIG5WHxiNGvMLmYo5AYKSjfjN2rO4WP7XKUhXlYJbsESmnGQIXzO2Cyt4VyqhamlZLefaz8UJ0ItlD1vHy6XZ_iUHb8E0_dZjBvLEMMTqjwRs3kSLvZTwzi_5tr_M6dIn_yn_KrfcPupWz6LkSEPxLW5yEMvwGl1PDHsn4DH-abgMNG75wY-zObA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66830" target="_blank">📅 20:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66829">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c8c286a22.mp4?token=i79MqNS9yzLvxXyLyurDuPSOqxkASMrv20TaMscvdhdb8RwvXUFF_92YJm6E6HT_xR6NQQ9O-7spSYRH9uu82-_BuTx9lEuYmilbawVdY1WWo9yIC9CM0dfhN5e5dhM1rKtnXq1xDO7GvU3c_nHLF7rLSMNHBTRrxGqgnd3a8mZKDEXtqj-qi5CDTmGVQx6Blt5LGZPsMiI0_tKJTSk34ECE9wMtKPQzSBGPILcBqXHTETZ4R__Ei28nUDX_76jCKhIpJG6UcCiAjcQaQpkBbOd3i0QafHQcr-NaIjy62U1GipR0Db8aOC0XGaRHAyEoxKGYtouqyD3v1KSuaahyRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c8c286a22.mp4?token=i79MqNS9yzLvxXyLyurDuPSOqxkASMrv20TaMscvdhdb8RwvXUFF_92YJm6E6HT_xR6NQQ9O-7spSYRH9uu82-_BuTx9lEuYmilbawVdY1WWo9yIC9CM0dfhN5e5dhM1rKtnXq1xDO7GvU3c_nHLF7rLSMNHBTRrxGqgnd3a8mZKDEXtqj-qi5CDTmGVQx6Blt5LGZPsMiI0_tKJTSk34ECE9wMtKPQzSBGPILcBqXHTETZ4R__Ei28nUDX_76jCKhIpJG6UcCiAjcQaQpkBbOd3i0QafHQcr-NaIjy62U1GipR0Db8aOC0XGaRHAyEoxKGYtouqyD3v1KSuaahyRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #18</div>
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
<div class="tg-post-header">📌 پیام #17</div>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nSHgqeV3CAu2ggVYniZ_XwjBnsaQ4xnEHCUrGC9qMImdyppZOeTexUYnRvr7VZ3ynNEjs2D-ZssB7svIyWBLLu9BwVK5e_BPCnqGx1TLuaVAnW4DxrZVO4VW7m5bf1qG8KPIcWzm3o6p7WDfmk3uplys2fR8X2CSJOkIiyhzQSdFImHGSFdiH9RArSk_fGRW-5oUmFB41_QIRfR106YWnql84pz7Q9zYNsOns9zS9314LnQXp7e0uJay9GzyJWzZDIJL_rh2V2e9ZKkQixIqTdENADWv9ySmhYyoLl1GNngwe0eu42-36gjFMXXzd1w-PRmdgaN_r4MCuYy1kdGtWA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66826" target="_blank">📅 20:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66824">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HFDc83YSquNiTVlGnS8JofP_ISt7n3GTb9EoMp7fOrBF6a4h4QvBuAnPgUgJGPT1EkyV2ZIN2nBeIdJuxe1QYOskb-uQqMJtAah0m5g-tkdeVbwVdEly2cZ2m7DBlPCNr1zT2SaYzkn3L-OxrfrITQyI81IHZU0wKVd3mlcHezXDcnsz1e8odCHdBijFt8hvfimgIBuGcEuogiEukv0kt6dy-KVIDqvGaSm8DsKINn68qEcBl4AK4lgYTdZvxUJvRXZ_9fLJi2Ylqk0qlbyxUWY6X6hHPsPcp82YyTMEZKJZISgMB3A97gk73He1mOrFh4CYIhbJ9hIT7py-Vavagg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1b8ae4df4.mp4?token=CJym2STRaF-FrseMwNWeA-gKzUrpuQmd7xhPdJbjMiPBUuRczzDf9fa6HUdwIz3lgGvmw0oN4CD6q9Cqv9IzkKAxPRdW_DwdtiRMFsLx_mBRCZ4Aqjo51SZWXr1U8Ols-bJGRAAPrXBwWT-r-fbmWblvJi3oLa2KhKIr9K3LDcrLqUg6vhgJwunmp3Nrus3BsRvbDxgt-MNtmz5L_2nG5znmhLpYmRRO0g23L50QqtARPW4PmLADtbF6N64jJ1VLyJ7z858sscsh89QRqvmk6iTuueBR3uUSVzjY1n8z2aUTUs6cEB278fcNq9o281iOO-MPWY9ysocbc37H0HOjaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1b8ae4df4.mp4?token=CJym2STRaF-FrseMwNWeA-gKzUrpuQmd7xhPdJbjMiPBUuRczzDf9fa6HUdwIz3lgGvmw0oN4CD6q9Cqv9IzkKAxPRdW_DwdtiRMFsLx_mBRCZ4Aqjo51SZWXr1U8Ols-bJGRAAPrXBwWT-r-fbmWblvJi3oLa2KhKIr9K3LDcrLqUg6vhgJwunmp3Nrus3BsRvbDxgt-MNtmz5L_2nG5znmhLpYmRRO0g23L50QqtARPW4PmLADtbF6N64jJ1VLyJ7z858sscsh89QRqvmk6iTuueBR3uUSVzjY1n8z2aUTUs6cEB278fcNq9o281iOO-MPWY9ysocbc37H0HOjaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فستیوال محرم
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66824" target="_blank">📅 19:08 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66823">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/113cb570d9.mp4?token=Vkp6FrDqWaH2VxDNZameMJEFnetVv3TbKy9P_bAhpMdl0qdB2RP3yVI359ZHtLUQnSb2FhyjPdL7FYBKKXbNoaDI3t3f_R226vyzSSQ7qcMVmVKSrSkJvy9kXhRxGU84PCZZQeo8dvXtY7vjrc_QN21NEZPP4wNRXzP6CM_6xS2mdXdLsIrcEW8uyUWJd8PVc2rzNg9mjWhSCEpWNKTpkfiS3Suxq5NYYwKqyQ9ZUxDfCB3cxbmjD_YiaMLhhZEbO0YO1u6rBJjPbIbhfK3h_5uZKM-wsbH7BFPBRJJx3sv23xZa7V9bsNJOwMBJPGgn4EYB_mw1PIVsUSc6Tl9p8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/113cb570d9.mp4?token=Vkp6FrDqWaH2VxDNZameMJEFnetVv3TbKy9P_bAhpMdl0qdB2RP3yVI359ZHtLUQnSb2FhyjPdL7FYBKKXbNoaDI3t3f_R226vyzSSQ7qcMVmVKSrSkJvy9kXhRxGU84PCZZQeo8dvXtY7vjrc_QN21NEZPP4wNRXzP6CM_6xS2mdXdLsIrcEW8uyUWJd8PVc2rzNg9mjWhSCEpWNKTpkfiS3Suxq5NYYwKqyQ9ZUxDfCB3cxbmjD_YiaMLhhZEbO0YO1u6rBJjPbIbhfK3h_5uZKM-wsbH7BFPBRJJx3sv23xZa7V9bsNJOwMBJPGgn4EYB_mw1PIVsUSc6Tl9p8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
قالیباف پاسخ مجری صدا و سیما رو داد
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66823" target="_blank">📅 18:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66822">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0453856b46.mp4?token=lYLKgPFTlfcNqgZKNlGVuvJTk7cI3miXhBIoBPLD42589pmAg8DEAUNSnJSijdTPCzH7g5kX5Za0HXCHU5tH-0MIC1JwDP_0EIhSvFIENR1Z0d75H0PRXEymsmYaMb9hJ6qAK4JWVQ8b5bqG9iUHzELD6lafi9li-NEuI2Tuc0XyvVetD3nNQ3CsNAUVaczJpDk7tCLcfpGXunk4lXYWvqjfBGdtxGN0PeZg6PtvlaeKus7A_JyvbYmzVvxOC5s-s-fONboUiojOCDc1UTcApM7QQ5A9EQy6bB8Ax1R8EVBoLTNlfqZ6d9rltk7kKZqZo8rs3RnZVN-XOdLFLuvBqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0453856b46.mp4?token=lYLKgPFTlfcNqgZKNlGVuvJTk7cI3miXhBIoBPLD42589pmAg8DEAUNSnJSijdTPCzH7g5kX5Za0HXCHU5tH-0MIC1JwDP_0EIhSvFIENR1Z0d75H0PRXEymsmYaMb9hJ6qAK4JWVQ8b5bqG9iUHzELD6lafi9li-NEuI2Tuc0XyvVetD3nNQ3CsNAUVaczJpDk7tCLcfpGXunk4lXYWvqjfBGdtxGN0PeZg6PtvlaeKus7A_JyvbYmzVvxOC5s-s-fONboUiojOCDc1UTcApM7QQ5A9EQy6bB8Ax1R8EVBoLTNlfqZ6d9rltk7kKZqZo8rs3RnZVN-XOdLFLuvBqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو درباره ایران:
🔴
اگر کشتی‌ها در حال حرکت باشند، واکنش ما هم بر همان اساس خواهد بود.
اما اگر کشتی‌ها حرکت نکنند، این نقض توافق محسوب می‌شود و در آن صورت با یک مشکل جدی روبه‌رو خواهیم شد
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66822" target="_blank">📅 17:55 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66821">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50938460f0.mp4?token=N_Tfey7AKyEY2q3bQDGa5LhWk8AL9DTV7NHW7A_x0td7JqVunkXTmYnKID6jAzW9SkfYuTr0anS2J2RgTItPPiVSPUpJYvvUom5GEUYjOa583XmtkUBEpnUGaoUvzZqABeY_DBSxAmB2j3rzlSri64HHJdtWtCN5445riat_VKkTKEXJZ-qlXfpjC1G8BzaU2wJPeTAcUT9i_K1_v493VqtSJn7eRTARkZhOzvUeseFm7Vp-mkhHe06-3AeDFoxrFu82aqS2_rPYn6JYwT9EpapL26KvxsZqzx2iTcH0rIZTBxz1m5MHExTPDrccspMauzc5lWjyB7ado3QzcXLwlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50938460f0.mp4?token=N_Tfey7AKyEY2q3bQDGa5LhWk8AL9DTV7NHW7A_x0td7JqVunkXTmYnKID6jAzW9SkfYuTr0anS2J2RgTItPPiVSPUpJYvvUom5GEUYjOa583XmtkUBEpnUGaoUvzZqABeY_DBSxAmB2j3rzlSri64HHJdtWtCN5445riat_VKkTKEXJZ-qlXfpjC1G8BzaU2wJPeTAcUT9i_K1_v493VqtSJn7eRTARkZhOzvUeseFm7Vp-mkhHe06-3AeDFoxrFu82aqS2_rPYn6JYwT9EpapL26KvxsZqzx2iTcH0rIZTBxz1m5MHExTPDrccspMauzc5lWjyB7ado3QzcXLwlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66821" target="_blank">📅 17:50 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66820">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ULYTUPezee3fnZKT7_Wb8cBWOxyG9ELDIAYtwW2RrnUPHmPPuFQenZwnK93RW5sh07yWR6FjXkhn6VwkQJb93_QZ_0UwZDcdm_yMGERS3sVYH-hkDB6L-FNiFRQy4c4H7G1N-zaQA2PheZu34rkKkE4ch6-yBpwSqSq8smyJG23FoaGNYvKCHlOLeXacb5JEYTBsnp9chxyX-XR2zdXkrQKnp_o5gQkHktelny0NL1NxclVly_g7zEL3o8N8wYsJmu7P7THeUIIeEpRi5aX5x09JnrbmNbKILpLmqkPBiImKB-dv16sxRJclzjXKIgQ2e10tBwtfxqCXG5CrzEklwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قالیباف:
آمریکا به دروغ ادعا می‌کند که دارایی‌های آزاد شده ما، کشاورزی آنها را می‌خرد. جالب است. تنها محصولی که ما برداشت می‌کنیم همان چیزی است که شما کاشتید: دهه‌ها بی‌اعتمادی. این محصول ارگانیک، فراوان و تولید داخل است. اما ظاهراً ایالات متحده فقط سویای تراریخته، وعده‌های عمل نشده و حرف‌های بی‌اساس صادر می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66820" target="_blank">📅 17:19 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66819">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/477cde7837.mp4?token=to5GrJotyFg1muhpKzwbHSSwvIjF8LmUVZ8fA_seU5CNprfGqKuNU9J-_AQ4IUNi7TXs2ZA3rn6yozmlz12H4cjm_R8m5YNRliqG-AOl41SUqzsnTsKdWhaMdIXpL9obDAzD6IGJ1cdoyLKxgCAYBNtlXPl3Ot6fgRw1jXgf3YqMzkHc3YseufmlA6KZIkYGskd0VcHC98zDt5Tc8eXxrBKAspVQfFgD-eUcbAimlfyuGwz5TWBP40Dq62HbDsYZWZf6gdm_8sWA3qk39SbovpqxQRcRahOFrna3qC5JhB9nw1TJhW83FJeNPzNjzXQqQp1_LKtlM5GLcRp8ukJbBTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/477cde7837.mp4?token=to5GrJotyFg1muhpKzwbHSSwvIjF8LmUVZ8fA_seU5CNprfGqKuNU9J-_AQ4IUNi7TXs2ZA3rn6yozmlz12H4cjm_R8m5YNRliqG-AOl41SUqzsnTsKdWhaMdIXpL9obDAzD6IGJ1cdoyLKxgCAYBNtlXPl3Ot6fgRw1jXgf3YqMzkHc3YseufmlA6KZIkYGskd0VcHC98zDt5Tc8eXxrBKAspVQfFgD-eUcbAimlfyuGwz5TWBP40Dq62HbDsYZWZf6gdm_8sWA3qk39SbovpqxQRcRahOFrna3qC5JhB9nw1TJhW83FJeNPzNjzXQqQp1_LKtlM5GLcRp8ukJbBTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویرانی‌های بر جای مانده از زلزله مهیب ونزوئلا در شهر کاراکاس
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66819" target="_blank">📅 17:08 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66818">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V2m9GIzCCDODlYVAAE44ovDOPdQVZTmyyOUQHzeIV66Cgk57C5wCaNfWmKfI8flTvU2OrCvTv1ugh8GsYX12Zw3_A8zAcUuBFwQAw_-gx8ZxItu4TwwhTVHSEUAfT4VwJ-KwPVj7oaZqVRtiX_ECkSFaL0TiQF_lCckyhVW4sfHmi5juUw-jijxmwBvA5-R1izY7cko8gFvK86tEisgmfWFm530zjyEcJ4b9TCGD8Kr_Llvhvf1_KwjVGtowkh_HUB-Eb-X4e38Q6PgxBLqM-Upc9bB7eHjmHqfDrV0empOnfAxLr-PjLMqV5lIC-V_zoECin8fYlaYwCzEBJ3mJMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسماعیل قاآنی فرمانده نیروی قدس سپاه پاسداران:
اگر اسرائیل امروز داوطلبانه از جنوب لبنان عقب‌نشینی نکند، فردا مجبور به فرار با تحقیر و شکست خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66818" target="_blank">📅 16:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66817">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4301a5bfb2.mp4?token=GpPGKHtMhRBrmmnnOfWJA_Uwjpbn_M1MSr9lbnGQdMgBku6h6wF-K-ZYhE9DtqLNZikS5y8_FiXF9CAJFaZYiQQEfsjXpJjIEwddl-Lcp97FoNF0Rrw0YgORQcxKdaMGCscAA6m7D-dKkB68AQy0wuS_19qDRjkQuO6b2C6KTrDkmZ7pABKFKJjQq3BIg6odhyZaf6E8uh008iM8jv5A5CJLw_pLDp5wzdafKxzxF_Rwu3QmK1X77wmISPvC8kxzhuCJPVuyqu1NtOjK-bLoc8ikCvF7iuLhcJKgvTBniNWlXSpedk9dkRP6AnKd93xTRxU0G0QKwKxGNA7qZ06ziQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4301a5bfb2.mp4?token=GpPGKHtMhRBrmmnnOfWJA_Uwjpbn_M1MSr9lbnGQdMgBku6h6wF-K-ZYhE9DtqLNZikS5y8_FiXF9CAJFaZYiQQEfsjXpJjIEwddl-Lcp97FoNF0Rrw0YgORQcxKdaMGCscAA6m7D-dKkB68AQy0wuS_19qDRjkQuO6b2C6KTrDkmZ7pABKFKJjQq3BIg6odhyZaf6E8uh008iM8jv5A5CJLw_pLDp5wzdafKxzxF_Rwu3QmK1X77wmISPvC8kxzhuCJPVuyqu1NtOjK-bLoc8ikCvF7iuLhcJKgvTBniNWlXSpedk9dkRP6AnKd93xTRxU0G0QKwKxGNA7qZ06ziQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/msTqLWn7yemw9JVIJowS9iI0zxjBwkQJpUvBYZ-A7hCdHh-kWTWplbx3gsXl_biwGc4qlxAuSi6GF7SU3e__TPA68w6a7xEFgZ3pf54EPKKdxKXDLFyHr1bRxXtZ4TzFMZUzZu3qcx0cmevvVulHuWUhvX3rFD0TR7-cnhaLLABKkMynNHUCiowNDfEOpoy5m3ahB22bVZmmPD7Y78P7kyo_3nS5pOXDiNgwM5ftqqDDueT719AfwMBUYRaXMD-7HQk8mMv-DNrhkLKgT7DD_DvyNwdNL0GSSIFmb155MgY4qmTIsp9k3iXIcSg7WwD9auc6JQ0ddtM-bh0HZ_3ReQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇸
پرزیدنت
ترامپ در تروث سوشال:
«شگفت‌انگیز! سنا رای خود درباره ایران را از ۵۰ در برابر ۴۸ مخالف، به ۵۰ در برابر ۴۷ موافق تغییر داد. رند پال و بیل کسیدی رای خود را تغییر دادند. از جان تون، لیندزی گراهام، برنی مورنو و همه سپاسگزارم. این رای به ایران هشدار می‌دهد.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66816" target="_blank">📅 15:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66815">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">❌
خبرگزاری رسمی عمان:
وزیر خارجه عمان اعلام کرد ترتیبات آینده برای تنگه هرمز شامل دریافت عوارض از کشتی‌های عبوری نخواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66815" target="_blank">📅 14:53 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66814">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a64b900d33.mp4?token=rvRtIZL2JriLqdWSA4vTKpwshzDGOxNsYyw8tzPZBkLOKKN-fh8AW_DbPUWiI9Dk4yBuvLiTcAal3dDlz4QxPKTUJaBcvRmiataHm0hOi_g_ZGpV-02C28SDfTtbTO1bNRaZ_EaLeu-hf3m03tcQbFrfAiF0FTZgcnUY6CHq4quBU0q1fLgauA98SQulOAic3JtCRpTp4Qpf97dk_6iUvD7cbRrRnA1WPaIoh_8b6JaQ3xQY1DIF7j4JkTbEAtx5B_IRxNTQj9KFNe4zLFBf0bJoDwvLUmX4hxTjtKUGyE0a96ANZ7itVq3hB-tq_Af6fN4ySsbR2oygluhQrTk9qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a64b900d33.mp4?token=rvRtIZL2JriLqdWSA4vTKpwshzDGOxNsYyw8tzPZBkLOKKN-fh8AW_DbPUWiI9Dk4yBuvLiTcAal3dDlz4QxPKTUJaBcvRmiataHm0hOi_g_ZGpV-02C28SDfTtbTO1bNRaZ_EaLeu-hf3m03tcQbFrfAiF0FTZgcnUY6CHq4quBU0q1fLgauA98SQulOAic3JtCRpTp4Qpf97dk_6iUvD7cbRrRnA1WPaIoh_8b6JaQ3xQY1DIF7j4JkTbEAtx5B_IRxNTQj9KFNe4zLFBf0bJoDwvLUmX4hxTjtKUGyE0a96ANZ7itVq3hB-tq_Af6fN4ySsbR2oygluhQrTk9qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QSomuGDAKgtApzB15tGn1sWVVjX_J9FmcCFVCE-LQMsTUw7Of5n0fxK7jHhdUaP8zOsgyefvuVngy5LzuowPNX0qB1s59CaQ9mLhdjPR6Av9gl94O_Enont3npARCybkkQaZsW167TWLLDKFCGEKpVdULJ1HcEKqsApgE61LBXuBda8FqwPINbLZ_5198aviNxO1QE6n3R--NzQpIBJYgaptv_7ekffTSaBC44lCdVN6ofunsCfYI6U2kY22jPJzZA5pKHXxKNot0A0qG-etCFPp0pD-plz9fmnVfKYFHpVR0SDAlgOrkPwoflSMGPZlDKo2ATdeKcwwWCOXes7HUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو:
🔴
واشینگتن خواهان توافق با رژیم  جمهوری اسلامی است، اما نه به هر قیمتی.  هر توافقی باید واقعی، قابل راستی آزمایی و همراه با پایبندی کامل به تعهدات باشد. اگر رژیم جمهوری اسلامی به جای صدور ایدئولوژی بر رفاه مردم ایران تمرکز کند، آمریکا و شرکایش آماده همکاری خواهند بود، اما انتخاب مسیر کنونی نتیجه مثبتی نخواهد داشت. هیچ توافقی نباید امنیت، ثبات و شکوفایی شرکای آمریکا در منطقه خلیج فارس را تضعیف کند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66813" target="_blank">📅 14:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66812">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0835d639a.mp4?token=iHMgzd2txs8zWoC10a9Ou5fDaMDlA3rUp44G8AMfT1UMdOtPhIDK24mfUD1lA7ua5PXHh9XRjhsQfDcsKTPD1i9jtsNGd_DjaZqyxgsRlQK-pg4QCjJ8reeXpiQ9SAe--aOiCf3JhbIdxOeVHU2hGlDYxKQDHoVkbkZm4PbVtvwr8A4VohCj5fPL4SibP3sDhPfnUkCVLFRUaDxsuo5P5HgvAYsN8swir-bnJ2vcJLBpGrX2mfIi-fBcSykRfA8Q64C80c245DnLfNIr6YME-xuMOv3CZDOXls-m4Ch6DySXgaO5ETYgW8tcLmNUUbqykMEabed1psl6V2sOfkHvTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0835d639a.mp4?token=iHMgzd2txs8zWoC10a9Ou5fDaMDlA3rUp44G8AMfT1UMdOtPhIDK24mfUD1lA7ua5PXHh9XRjhsQfDcsKTPD1i9jtsNGd_DjaZqyxgsRlQK-pg4QCjJ8reeXpiQ9SAe--aOiCf3JhbIdxOeVHU2hGlDYxKQDHoVkbkZm4PbVtvwr8A4VohCj5fPL4SibP3sDhPfnUkCVLFRUaDxsuo5P5HgvAYsN8swir-bnJ2vcJLBpGrX2mfIi-fBcSykRfA8Q64C80c245DnLfNIr6YME-xuMOv3CZDOXls-m4Ch6DySXgaO5ETYgW8tcLmNUUbqykMEabed1psl6V2sOfkHvTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حتی در کیس بیماری هم عجیبیم
🚬
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66812" target="_blank">📅 14:10 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66811">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce6df862a9.mp4?token=ayNhOa8WCnkVAMM1CDYLcClOupDMKyLpVr13ggAwrDASKjXEaPL4CI_9vMxfNZ7DD9HNeu3qQdw3Hv3v6gwPgQlKGCImPFcS9zh95q4CxHQ3yF476kJ6mD0u0ArXk_USpKiHAlcpYa9UPtfhCdmGjaLF-YVuOXx8EZoloE9KEtaZW_j0h3Y45t5EC87lD2ZrJy8YyVR2SWBSWuZmRDsnU5O43EUGmfZp-SM5oktJ-9YN8aWcAH3jYDKOdTxYUareMzqz3QpLX0oZzm-2vBBcZzKtx9S84xe7OUkjvpRIF9Pa-m7SzhhHJw2fMn_vkYZOLKA29-_P8HuPUApEIXpEQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce6df862a9.mp4?token=ayNhOa8WCnkVAMM1CDYLcClOupDMKyLpVr13ggAwrDASKjXEaPL4CI_9vMxfNZ7DD9HNeu3qQdw3Hv3v6gwPgQlKGCImPFcS9zh95q4CxHQ3yF476kJ6mD0u0ArXk_USpKiHAlcpYa9UPtfhCdmGjaLF-YVuOXx8EZoloE9KEtaZW_j0h3Y45t5EC87lD2ZrJy8YyVR2SWBSWuZmRDsnU5O43EUGmfZp-SM5oktJ-9YN8aWcAH3jYDKOdTxYUareMzqz3QpLX0oZzm-2vBBcZzKtx9S84xe7OUkjvpRIF9Pa-m7SzhhHJw2fMn_vkYZOLKA29-_P8HuPUApEIXpEQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حدود ۷۰کشتی در ۳۶ساعت گذشته از تنگه هرمز عبور کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/66811" target="_blank">📅 14:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66810">
<div class="tg-post-header">📌 پیام #1</div>
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

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
