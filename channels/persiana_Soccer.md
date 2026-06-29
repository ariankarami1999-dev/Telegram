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
<img src="https://cdn4.telesco.pe/file/KQYllhrq5fquFtHCl-q3zQgK6mHyFRITxhPfTjZAVFfEZxjL5smCcAsz8EuTtYbMnZoqBTW9beNEJdLakE6fiB2sox75YXmlda737VXHmtfPUH1khrPvscjX6W5fIxMnXHtaszLHO_QSeMSxyPpnaA7ThK6IdDznx9KKY3E87D3kIbWk2dhgeDXuo1Dd6qWtUjqfXa_Fj9O2vHHdraHj7EKGhZRLgCKNQLvMAJNJDK1g8YOIrVCjTXVph6WRw0BVEoA4CHwCvtKlT6F-UQwbJe2BG1Bg18qrPDNY3gGYWeWmiNT9Sje-6VnaYHNd2t7tZBzDg6iTNDj8aEN2Lh3-Kg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 345K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-08 20:58:30</div>
<hr>

<div class="tg-post" id="msg-24624">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7056183539.mp4?token=XJrXqclN13soqQT_0fo0ApG9TO_VPwjcO_Ky4A0Uf_8psrIMhsuzxuJRV_uDY5vSgHsIFSm7wXMU9-HQLtl_d9Qa6_f3p6867eSJ7RgPe_hNZ-KyN5VAIkXM_yYhT0gE-rgoPrYSKWKLxxJgL3bK48BzcpxJaSLjGwi6y6m40GvOBkwu60U8GMzQmYo5eC53HFIAITAsaT00Hu51GXMk8DZQPxAS3jEK_a262jj0-wrn5lWYlgeYVMy8dv-qX-4vxCfnSbT2PcV7N43WJQHnh9ycUJILvSRmD4W21BE1n-Mut3trKupiSyjG_FKcRBrFi8nyL1fyTcPPLpC5a8VD5avR-OXLirvxz8ndwv75k0ZBqxMjS87A651YlMM-UCKbOu70zLpF2lWoYhysQhVLwnLjJcZviJke7yjYO6R-HO0vlpOBAS-DDWKPhejZUjuEK6nZi6PFT7MKWlRMlQEO0Q41D5hrozWLAU1kcO-wWpriyeC2BM0BP9GEjCOFwpldHx6JNfth4FsJCZ6w9ao7Zq0Ep_TnOVir-YBDJ5dDS2U0CLVoY2H_IfZp5BNN8okd66E0hm0hs3TARmt1qhTH0t_TEoCivLttJpDlWh-NjidSCWsSNkLfIHEhVfUqfK4-d4hCi5PjpUGgRDL_rtXLj9AE0LTIr7g0IFaatv36-54" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7056183539.mp4?token=XJrXqclN13soqQT_0fo0ApG9TO_VPwjcO_Ky4A0Uf_8psrIMhsuzxuJRV_uDY5vSgHsIFSm7wXMU9-HQLtl_d9Qa6_f3p6867eSJ7RgPe_hNZ-KyN5VAIkXM_yYhT0gE-rgoPrYSKWKLxxJgL3bK48BzcpxJaSLjGwi6y6m40GvOBkwu60U8GMzQmYo5eC53HFIAITAsaT00Hu51GXMk8DZQPxAS3jEK_a262jj0-wrn5lWYlgeYVMy8dv-qX-4vxCfnSbT2PcV7N43WJQHnh9ycUJILvSRmD4W21BE1n-Mut3trKupiSyjG_FKcRBrFi8nyL1fyTcPPLpC5a8VD5avR-OXLirvxz8ndwv75k0ZBqxMjS87A651YlMM-UCKbOu70zLpF2lWoYhysQhVLwnLjJcZviJke7yjYO6R-HO0vlpOBAS-DDWKPhejZUjuEK6nZi6PFT7MKWlRMlQEO0Q41D5hrozWLAU1kcO-wWpriyeC2BM0BP9GEjCOFwpldHx6JNfth4FsJCZ6w9ao7Zq0Ep_TnOVir-YBDJ5dDS2U0CLVoY2H_IfZp5BNN8okd66E0hm0hs3TARmt1qhTH0t_TEoCivLttJpDlWh-NjidSCWsSNkLfIHEhVfUqfK4-d4hCi5PjpUGgRDL_rtXLj9AE0LTIr7g0IFaatv36-54" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
صحبت‌های جالب حمیدمحمدی درباره شبه علم، خرافه و فوتبال در ویژه برنامه جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/24624" target="_blank">📅 20:14 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24623">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ufmRqLNLDeJlqFYpsADBdn0_RezOR3lGimo9wXNDPgTvIvbamzXAlVb20lR0wEEcXRhhpLBgSj_H1NdJKhcW78qfZLOPIVsPhfqGU6GKaHUafNichqXhF2V-wvUkuQC1n-wLsyxNYTDUAB2kIhMszaOdsEnyW3WPPmEDimz9k4pIcdwybLN-IQ6wO2N9Izt6L99Ej-MUq1sD1fRfEDqaDGnD6jVzNqAgzIlRSK0mLYEzSCIzyOwp_-jBmk_f4V8Bi9Iatg8Mbd276u3_TR4rm6p_FEP5kqd-6y88IHgjx0Cq1Xkn1u8puf4mTM4hvnJJmtchcHo_02Ehp4KZXUr8BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
طبق‌شنیده‌های‌پرشیانا؛
جواد نکونام در جلسه با مدیران‌ایرانخودرو برای‌پذیرفتن‌سکان هدایت باشگاه پیکان برای یک فصل حضور در این تیم خواستار 55 میلیارد تومان شده. درصورتی که پیکانی‌ ها موافقت کنند نکونام قرارداد خود را با این تیم امضا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/persiana_Soccer/24623" target="_blank">📅 20:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24622">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YmSRFaKSRNz3TsWZ2HEO3qH6ZDhrCrdLFTVilXHYSCWDy9mARSSsY9_4QRLUrTy_UHVWdKSvC8ETOFYZ_2Ey8hdGYIfr9MG5CSz53EBJHo62sMHuNzPD8GKKoa_lCP2j_UuO2ze2yeX9xQrIGwBTJBnT2t9gUD2c9__NPQ5BO8AA8UH6JCWtgZt-9gHzI6GEfIeyfpLcFVLLgKZRcrw5YJ58wMsRCgFrwXG7sp4z2oZdKHcLYi01xgMykx_MKnpgvxlE89Co8_EhFnHiq7co1MwSzg9Rqd3PnyoPMiiAETS6wUggGBS5uMgdyGtqAZdzAoiXXj-rnUoLvzY8QJjR-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌شنیده‌های‌رسانه‌پرشیانا
؛ سیدمهدی رحمتی بعد از عدم توافق با مدیران ذوب آهن؛ با صنعت نفت آبادان مذاکرات مثبتی داشته و احتمال اینکه به‌زودی هدایت این‌باشگاه رو برعهده بگیره زیاده. تیم صنعت نفت در آستانه بازگشت به لیگ برتر ایران قرار داره‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/persiana_Soccer/24622" target="_blank">📅 19:35 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24620">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uZFn6PvIKjH6YZQ6HLPS01OmOjxx0vr56v16UFNp9F2wpVauMqh9ekAZ3fN1yUWCxiLqrH2gvmlrsbi6bfKe-Ukyjm98hOrNT90GDcI9DgOUcW1i8zymZwYGQwvyKn3VX5ea4o_uscI5T2t0xSgsPkwTLuBmq907FNbQ0Bd4eAeYJ8AmxKGNPRCACVCZkyc44YU9TaTb6-7vvnfFvHrzuD8YjflW2lg6lZlFxQYanzbbFpc-hjpy9lOzcNG8ZVRoPhfeNFNgeX9z8RKCevtg4QiZtTeKPXXE6JPCrsnux0loXrHd7zlhieaUhogqkjTxie_m0ZfBmnOVpUQoKiMy9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/givv9g2lmwSCgvhOJveNTQeS8tsFKkGcmWj6BBsqnCYZsDIv_sfw7AiY1knUrW5ZyDgUAHrIP6bEK9p2uoBsEGqSOxOvinJlqpvXpFBc0jopYou2MaKm072UKgDIBRNrojBtycFuMVb_iJqxQbbqv4pzPqg_31fe8SrTEs3B3h0dGQjlc9pKkSUtpIylM9Uja6HIZYuiNGCNasm-GUPkAi9AhaPJPNFjowVSbSJtbA8qvPDRZNVIa-UOpSWjwzpsvMJP7STjjxb4iTCMS0PDWLMoq4o7Jaom0Jp_526jaV1ElXE4JEwkRabyyIroexDAqlbjJDlDH2TzYgUi70JYGg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
از تلویزیون تا زمین فوتبال؛ بالاخره اتفاق افتاد؛ تقابل جذاب ژاپن
🆚
برزیل؛ امشب ساعت 20:30
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/persiana_Soccer/24620" target="_blank">📅 19:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24619">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qQ6sgMqG4FCjjw0QEtylPseHHICwGhLs5sTnFYJ_70iNqy5dTbHdQaD3eWXowIjFMpCBXS72KLV0PBM74EHT1gphC9nk1cCdFjx4aJi6iQRlDGKPdsHevyA3GsEYUTkZ0JKC1Ok36NBEUQEJSce7vPEyPYZ5zRejyMUeQilIlfB8VmSoklveKWTht7BgfKmZ5UJQY7C2uy3k0ye0jd6t9f57e8VEwK0kT-tL9ehP16JX6-tfU9HM1188BSVqnsbcpNFHLD9yym4zlaeD0LQycZRFWzm248ZZ0IIeyM5_xLYwxIE28M5mApU0KOnSTp2yJ6gsqXfrR0zDo51CQ1JP5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
شانس قهرمانی تیم‌ها درجام جهانی ۲۰۲۶ از نگاه بازار پیش‌بینی؛ فرانسه با شانس ۲۳ درصدی در صدر قرار دارد. پس از آن آرژانتین با ۲۰ درصد و اسپانیا با ۱۱ درصد در رتبه‌های بعدی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/persiana_Soccer/24619" target="_blank">📅 19:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24618">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nnFl49s9FRRHJJeiQtrFsm4shTqSbzlqHMxTzQGIDjyrBoXCiIOVd16m69os9EMqzT1peEJ96UWyIBJxZ8GynQAWt_kHeE7at10keOM4LUL2s3vZ_Cy02xMBDO_U6pRvIPmio2HVYu_Vp3K8QmL1_qPk3zt6uMthV3h7h8qgGQfGZ50V4nyTgF4JSkPA_03rCQ27F0kWjCc7wXt3bX6eRHDldwsYtApx656cJrZTbChfeo7ndClBpn_S8z7--ZOImehpQEmLsiEKU49aizyXh4wYy2pW9p7dNZDKFf5ZSrn2ZLGXQtxkCmvfvAi-DjN_wa4M2lXUetfsLeAQrwvTtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
تورنومنت ۲.۵ میلیارد تومانی رومابت آغاز شد!
مسابقات جام جهانی 2026 را در رومابت پیش‌بینی کنید، امتیازجمع‌کنید و برای سهمی از جایزه بزرگ ۲.۵
#میلیارد
تومانی رقابت کنید
😍
🏆
هر پیش‌بینی شما را یک قدم به صدر جدول و جوایز ویژه نزدیک‌تر می‌کند
🚀
⏳
فرصت را از دست ندهید ؛ هیجان واقعی جام جهانی را با رومابت تجربه کنید!
🆔
@RomaBet_official
┅━━━━━━━━━━━┅
🔰
لینک سایت جهت ورود 8:
🌐
RomaBet.tournament</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/persiana_Soccer/24618" target="_blank">📅 19:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24617">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FEypeBVWv_eM_wYHJ1pIoOMD1nnn_iXzJF5Cqmv1OlTmRjt-XdohIJLGNh-dipd13N8gKHDFgscrR6StDYKFl8HyvlV5P33BK-RZxZ5bjE5VPEhmdFZOPodnasWpNuMWIVkJcV7Uvw0C52yOxq3gp390gc_NToEHPVSEDCtRowYVm5erbckkCSZKMnQSENwhtj_Gz8f9NCn1gZInPz7UqRbMP4Psti7FOiNJeTKe5SNtqeRh17D2Dx_v1vZaIyJCcJAFGzDEyXHg-LJRqLq3viVYmlF1MxFyo1Y_XkHPZNi0MMMNKvn_qZvyK0AHBGpMebN-Q1wFWJNWzU5k19VJrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قفل کردن تیم قلعه نویی روی عدد سه؛ ایران توی این‌جام‌جهانی ۳ بازی انجام‌داد که با ۳ مساوی ۳ امتیاز گرفت،۳ گل‌زد، ۳ گل‌خورد، ۳ گل آفساید زد، ۳ تیرک‌زد، رتبه ۳‌ گروه‌شد، بازی‌هااز شبکه ۳ پخش شد و برای‌صعودباید منتظر ۳ بازی آینده بود و در نهایت باتساوی ۳ بر…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/persiana_Soccer/24617" target="_blank">📅 19:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24616">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nGdcYmPQsNnby908Iyt0A7oXkDldiBsuOMN7_T2pQ7pMSoCHxts7ybxKAYN3ar3vEGZz0gjLhKa19HyAmdyaamWnWO_7LvV9UMsQWMACsv6ozTdLjWPK1S8VfthHZW9GIG26pz91Dux-8pZOwjwztD7PlhOqcjOvw1_x2ObiRmpv-1AT-VPGGIO6uJ1095VGKwQo7eJMj0tPnzG3OhvTcdJava6LkDxRwVqaFowsAKV02fpcjY24vqP3AZp9_6J3aSOkHyBsa6YzMkhBc-LYXgyLkocRl03FAAxegX5giDS62GVcJLI0YR-kfmW_yaVIpnFF2nOg16xs7HIOsgY6AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
باشگاه‌هایی که در جام‌جهانی رکورددار بیشترین دریافت جایزه انتخاب بهترین بازبکن زمین‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/persiana_Soccer/24616" target="_blank">📅 18:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24615">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aq9I0Qo7DWHnzRX35-60ucdvG5pe2M9GboVTNBhhlk_Df6HNKTNjo95VLwcL9tXN_3kWFPhnpC46tVduZl4aOECGYUdrdJFM-jyLNlkfxNPbog-YsEQnOpf_rfJuUyZlk_qcPEFOdi-G2ZCNuXJJIBJFBnPMi6QwU15rE4rmXCBbrRuCrmYLtfG1P_Yv9i7V-kN1VDm_E7fOX7aGz1ImVazu264nckzZekSDKdp57XK6uP0PKUNyI6wRVLhdZSHioX80Zhz7j6TOWuduPjdD4AAB8u8yKSWXgiWGwuINUJnmp5hpjI_EtISRHRdGtXPqiEQWv5O0i20ZAFhp48W3hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
باشگاه‌هایی که در جام‌جهانی رکورددار بیشترین دریافت جایزه انتخاب بهترین بازبکن زمین‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/persiana_Soccer/24615" target="_blank">📅 18:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24614">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R1ecOWSbOcQ6kXIjndACDuuOifidFZtagJNBmb_6scZflJRy5o9uYTqxWA5KXBIZ0vMz4pVTqHHm2FDlKJmIDWd7ArFvYRKIH5Bn0-e-zvpGJaUNlU-nLfETpHQMywK1nm0mq0yi_mGnyetLuG3kfBx6K3XeOsXZuCcBp5aJTd02w8LrryK4SaLX9dO_OleX3QOn6DhhRH-t5z7kX8xjefZjK_t2E0gctL1p0sPI0icVIwR2XnocZkwNyquNmevRvmVkJqDd3xDHaPPMUUPBG_GfD5Us0FbvDHT9FXSpKUEbX30KTiKSw0AB9dpCgqaVHdxXnC_Ckq_8HHfaDgkjJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ نشریه مارکا: مایکل اولیسه بله ضمنی رو برای پیوستن به رئال مادرید به مدیران این باشگاه گفته و اعلام‌کرده‌درصورت کردن رضایت سران بایرن مونیخ اماده عقد قرارداد با کهکشانی‌هاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/persiana_Soccer/24614" target="_blank">📅 18:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24612">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L6nj-C6R4jjJZGce3j5955l7ZJeeMBKpy9QQFVPJpUd4CKRVZFswQL07tz8qKXkN-rFF3ebfeGNmZjTLCONVBuIHV8Q_mXX2MP5UHREFg30SI3eWdykhKcPlulMdphR8sp3KPeEUHasVKCHlFKpQ3EOkfJLdn9ONbO7HDDrSuTGcBD4vmpeGFCxwQEt2bPaW3fwJx40Nfs7ja0RGY4zXlNOvDeZOl1V5K2RWw4UAUliLyA-t2WcC2AIBxYQZZftdxvMgrMml3bPs1yAQp1P4fAoxzye25mLGWmq5NlA5XtHtnrkC5uV2k5r95wx56cjWDSqdfPTMeBaUI2EfzvooRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
محمدمحبی امروز به‌ایجنت‌ خود گفته تا دو هفته‌آینده‌افری دریافت نکرده به استقلال برمیگرده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/24612" target="_blank">📅 16:56 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24611">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f9BcLJDYjDEieQCSTxXMquzIDqkYtckUrxar7W173a42EykiWxHARE_qrATRyE0abowfh7Z4XINWJRi-V8KoLDBp5RH8ynjrOLmZ9BNbeHqMweMXZNV3ge02rXlG4NoO3MrRtzeailSAgyF_9OnFsYFYp-kSvJ6k8I4SwuaAIqk4QSlJq81EhKSCDDnKqSDdIYAibtiW8Z6-zWaMVvQvtlFB4-WtTKsqMo0pAr4Y1GMiBQO9S3UOb1OluoOUKmJOVTJ3OVn7ixcdywynBOPGooQAJa9CuGI6zXQvQWdqqPSwzRCjMwFF6QHct0GVW0suAAFbjazh8Wq6MW07ESZEdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فابریتزیو رومانو: انزو مارسکا با قراردادی 3 ساله به عنوان سرمربی جدید منچستر سیتی انتخاب شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/24611" target="_blank">📅 16:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24610">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jUX0tRd4MCovODNxLfXHE_8Ktea0SKPvS8PFQPMQj_Q0OOEx1yFVG74OVaQs0r9gO-PjeI1itlgfISsiIHDZw6Gvse4ilSvkLyQkiH1-9tXb6EVf7emrby2iAW3T8YN4CHcTOuQI6up6AZNjRdxIncKfn9tHA5d5HUXLm97Ygzydgu1Uea50g7bXQzwaAyhK6jepTT7KiEWas6-tXYHkOI9xJRv_VGq-kd1xnc2D3ntPItAI1XCl35o-LsvfDXW2blTZ0c7b8EN2O1zXJl34Cup3Soz0UaSp8AiXHMitF4B-7Re-ZwfcbvhG_QnmT0gwXW_f9WnqxKYt7qCyYEC6PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇫🇷
باشگاه رئال مادرید رقم فروش ادر کاماوینگا هافبک فرانسوی خود را اعلام کرد: 60 میلیون یورو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/persiana_Soccer/24610" target="_blank">📅 16:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24609">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6c7c83867.mp4?token=bW6r6TG5Bn2aj1ky498wzlmM6p354JAnOTx1UfYPFyjgnLbkuZydwjaPLo7KoAKpBP3HDmZ0QUKYjEXp4KskpDLlgX_hm8Vi_vlUh74PVu6Wj9gbRgTZ84TNr7Xrmu0S0GlAdJHCRLSwJ1tGQEmPgdRPPj-6N9UDsK6D0mB4PrJqqQsoY9sKRPUrTRdnGR7a_KDCcZs2eRw_RvruZt7oyIgFQg7zm0cxHaJ3rjV0BCs3iHVhsO8mXCQwvKDfhcnQlRJUZfXHljkXodug04ligfOEMhJ9aCkzKpTZrQlUeb-V6V1ozuvjDOUdZ2zSrN6dR0vwLn8e69CrEcVxutC4jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6c7c83867.mp4?token=bW6r6TG5Bn2aj1ky498wzlmM6p354JAnOTx1UfYPFyjgnLbkuZydwjaPLo7KoAKpBP3HDmZ0QUKYjEXp4KskpDLlgX_hm8Vi_vlUh74PVu6Wj9gbRgTZ84TNr7Xrmu0S0GlAdJHCRLSwJ1tGQEmPgdRPPj-6N9UDsK6D0mB4PrJqqQsoY9sKRPUrTRdnGR7a_KDCcZs2eRw_RvruZt7oyIgFQg7zm0cxHaJ3rjV0BCs3iHVhsO8mXCQwvKDfhcnQlRJUZfXHljkXodug04ligfOEMhJ9aCkzKpTZrQlUeb-V6V1ozuvjDOUdZ2zSrN6dR0vwLn8e69CrEcVxutC4jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آهنگی‌که وقتی شاگردان قلعه نویی بعد حذف از جام‌جهانی به ایران برگشتن باید براشون بخونند:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/24609" target="_blank">📅 15:38 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24608">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eQzgWv_TEX2nqwbU8no8sadVq6oPMf_sDKC2tBH1FTypVpAsaqBQkAZ_XX9sA6neUkcPTbciAlk_18-Th8_NWn4FSVXdOinx3AfNK2ft1lqgYn85lnTXDNXkimbckU6_emv9PcSnoahoG5gpQkuc6XchCrwU1klwQQdG4BIoQbS-Jd5FXaeKA-yV3AqXdCGRXmjnzL5bPf-34P0eOhQVfgJSSEgkZJXYHccyTLbOArUWA8JiZWWhbVz8KMF0TXnnjJ0iuwnNZToLSTrbD3zoiNSVxhEV-_JJ_CnCp1LWNQfVCrlgxXFr6O8ycIfJThuUKeRHNiZL21wHDEiBT99Kzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رسانه‌های‌اسپانیایی: هدف اول و اصلی مدیران بارسا برای تقویت‌خط‌حمله این تیم خولیان آلوارزه و درصورت‌پرداخت 150 میلیون یورو به اتلتیکو قطعا این انتقال انجام میشه. حالا اگه یه درصد این انتقال انجام نشه گزینه دوم بارسا هری کین 33 ساله است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/24608" target="_blank">📅 15:23 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24606">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rd0gdzoX7N9CRdmfhq8E9Ee_W6UlDIjNcZrnv4yA3BwuVWFBGEgKFnylQkXWLateR30cnDkm-tCM7L3E_55rducv6XCZ86l_uf2y_AG3nvb2cGtiJxMuQx3h-FQQYEDeqUazAgdzRKMC7onuHCeTp9sHTLPn9EuLnx0TYea5ebA2Eokk4RBb-TjT9gImEOrB8SHEAtfZKOq8oxvwaF_VeesKBpYyyTZa3tF0eIAHq1LFQzAYRHYkGj__22lDjyJZ1yLM-6O1bNVgPxO6Xs1UsEeArccSdctlmqgtLguzVsUwmri9f2vefrYM7iL1kn9wpTe4fKZS72hkz4dszMrFZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j_3AnMh198Igvs-6lPiBLhQHfSzsaojKLg9sk09iMqwCVZF1_KK6pSsPR-UEQt7viXfFwcWRtCnksRhGP3BS6SCyyF4-KF1EyEtx9N7pvQjfvYUpnq18cKcJyIntnQydJvueNfiJaQyWzoqXQj_YGJibNRY9izNWFm-xSaIj0tTE41qr9rkUx88AbJ6nTI1JjvZ-w6wlAan7OsMBRy95GpnowyBLpgHuz5aBueipW5XjcmKukh60CjKn9Exx7a6Wlw2umi6UNSRvQkfahER1vnuMRQYUktGTgPmonn1Nx6w6TbwhU5NjHzQx1jKIA8YbSKbmnep6-XmWNd7EH7sVSQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
🇧🇷
نیمار جونیور کاپیتان دوم تیم ملی برزیل: وینیسیوس فوق‌ستاره جام جهانیه و مطمئن هستم که میتونه ما رو به قهرمانی این رقابت‌ها برسونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/24606" target="_blank">📅 14:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24605">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X4MqMlB1bXMj_o7J1d2OFBGuvQRgD8RooGCoQWwwQVrf1Z4vD89OWUwAUjGZ6691WC9X8H5xcuefXBSWFu6M3jDj9bmbM5zab_PibYg5GVhpPT3lfbXhUd-J9f2Vv3xK2dGRK8hDGzrmJAR0iQAMjTX950qk-8wtd7cmIufEzF_rj5X2Dj4jxdGehFn6hO3cmRcYX0JY1T5ixmTvJvSgEk55_rbBap2cKEsP2vm9f0MQdknBa4o1nSWfNHoXF9zyDtoxyxpUNmnEwg84IpbNAICJiazdTdPN_N3FC-BtXTLJxTRlUvgxaqInSyKAZ29_iqby1ul-thYOJ6bpIJkbhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این بلاگر و هوادار تیم ملی اردن در پیجش افشا کرده یکی از بازیکنان متاهل تیم ملی آرژانتین بهش پیشنهاد دوستی و رابطه داده که او رو بلاک کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/24605" target="_blank">📅 14:38 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24604">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aNOUWE_kmX4u8Zjy0W9aosIqansoCQG8a3g7tNFCSFsG1LoouYuy2akJ-0GDig8yE_-nOp4ZHma5tebhS9cJoNqa0JPQyGPMBnh_0dAdPwf0HO5EL8TJgoL2fnRyCZkyBNd1Rf45HBed69xC5kVDBeiM3MiKCVSYipYQZRCPMM5holjiIvURmZVS3yZltlrKjn3Gml1Gu3Pcwv5mZ8q4kS3AMb2X9fcgSnCVCix91kNyNu7o6LoYAoeZVt20Ny3KXEtEnwQpqQKEP0JUFp5sOXh-ZEMoF5KjkETNl4XN9vwO7AQ53-W5hHQmCLmIPoAxcKlfnBq2_i6y9IHtX8vWeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
مسی باگلش‌‌به اردن حالا ۷۲ گل با کاشته به ثبت رسونده، همون‌تعدادی‌که جونینیو افسانه‌ای داره. لئو به۷ کاشته دیگه نیاز داره تا این رکورد رو هم بشکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/24604" target="_blank">📅 14:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24603">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DxSzHR9jYPEL9Po-vuy5YPmIVMjxqKkTbz7CQBouXnyhSc-FxS0RNCReX57AR9HM_VZTr9964V0iMFbo6-MXU1xMY3iYUWclg4-EMZ6uVnhW9bdYVZKE2jGM4o2NnsaFm-ZCgldJTzmaVJeLC6qP7fxGfqJmFA4BDZV1H6xMdb9TuKAKF0l2bmokxBGE3GQjWJKFor9maftwGkzHKXxsRT5FI-TElciGEXGQHgtS3txvHgtg1qPeZ8nYdeIYzEOoSwRattZTp75sWAXonAFHS88IH9rOT6MvaCne7Z9Jem1T0sBgTnnaGZ4MLCgoXsPVyX7T8Rb7rg8VOknZ5DPkKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
درباره اسکوچیچ پرسیدین؛ با پیگیری هایی که داشتیم پیوستن‌این‌مربی‌کروات‌به پرسپولیس منتفی نشده و اوسرمربی‌فصل آتی سرخپوشان خواهد بود. فقط بین مدیران بانک شهر یه اختلاف نظراتی بوده که تو کانال پرشیانا آنلاین بازش خواهیم کرد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/24603" target="_blank">📅 13:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24602">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2df383dff2.mp4?token=ajffm4VdZssihP7gUVfxYmISQyX--02MrPAWemTGS3eO4KzcZDCNop5oBNLzZ0OQmKzOFRlxdLDbM_yUihF5zH0OpK5L5wDXHzo7zDkZP6iX4tmRE8wUhYUAEng9_K6aNaLuD9mpyffNIWTlMi-P9jvc7JytTjlHO0JqaObyADDwuVV0jGH6OvfPFZ8gWH9lI3YN7Ns4KiT80bEqZrXTtwKVXgnrfoRatFz_F3OT2HHMmAzxtG_d7FlSb4gAtHjb39Ginxso0pkcQNDIekSiTD0bY8LdEl3HYhxkXyP3Fy0A6AKGe00xNaepqCJj3FzEmAvq9dQrHP3UzkRcXoAHbB2xX39BxN8Kw6ruFed-Sn0RfRbzUEo__aXXKl2ETK4UAjP9XLr5zwN2e9JYoHjn3mwTtz_ywtnRHtW8Oa3w_R3XBLQ9m564LQiKRVhMIs9pfRpD94lRki-zBt3ytzBU_q2PI5b8pdS4F78YPg4492WDPCiVKrpNJWSf7xg1pwe5-AeU9P6mcj3ewWZryuedKUW8ImdLRSC6_WH2S5bGY4VeyJq1zbeahDPtKf2vbYEBEAFbJLjzvU3Rj5sU7dPNNajIfjRkOD-6F1tU_B1VfQ3bS2zwG6ZfrcAX4377h7BbmFz8EDDpJCMUJZXEiKLWUQKAAygHEBb5FBEKJqCmKc0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2df383dff2.mp4?token=ajffm4VdZssihP7gUVfxYmISQyX--02MrPAWemTGS3eO4KzcZDCNop5oBNLzZ0OQmKzOFRlxdLDbM_yUihF5zH0OpK5L5wDXHzo7zDkZP6iX4tmRE8wUhYUAEng9_K6aNaLuD9mpyffNIWTlMi-P9jvc7JytTjlHO0JqaObyADDwuVV0jGH6OvfPFZ8gWH9lI3YN7Ns4KiT80bEqZrXTtwKVXgnrfoRatFz_F3OT2HHMmAzxtG_d7FlSb4gAtHjb39Ginxso0pkcQNDIekSiTD0bY8LdEl3HYhxkXyP3Fy0A6AKGe00xNaepqCJj3FzEmAvq9dQrHP3UzkRcXoAHbB2xX39BxN8Kw6ruFed-Sn0RfRbzUEo__aXXKl2ETK4UAjP9XLr5zwN2e9JYoHjn3mwTtz_ywtnRHtW8Oa3w_R3XBLQ9m564LQiKRVhMIs9pfRpD94lRki-zBt3ytzBU_q2PI5b8pdS4F78YPg4492WDPCiVKrpNJWSf7xg1pwe5-AeU9P6mcj3ewWZryuedKUW8ImdLRSC6_WH2S5bGY4VeyJq1zbeahDPtKf2vbYEBEAFbJLjzvU3Rj5sU7dPNNajIfjRkOD-6F1tU_B1VfQ3bS2zwG6ZfrcAX4377h7BbmFz8EDDpJCMUJZXEiKLWUQKAAygHEBb5FBEKJqCmKc0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سه‌شاهکارتاریخی مهدی طارمی مهاجم 34 ساله تیم ایران در ادوار مختلف رقابت های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/24602" target="_blank">📅 13:19 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24601">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gB20u6QVJbVe94RuDRVGbosyI03CIttM6flA36ejQlFiRw8kdY9TEOsMuPB-OX263c2-civ7U25TkpeFLp81xwbCr7P6jvzvGkkyPGsXlmM54_t-z83B4O1_efQA3gppfHOs-vgmk13IKg8JA0r-5d5FUq2mzRW4QYod99oo1UlSeJrnDYcIfQbwsNt2cRGajL_xyGVxOrJ8OhxE8QhCw9ZrW9XzJok7lvpbfsy46KfCXYQofu-fG9ctjWBrZ4yf-77M8vkJfrOCS_0tJ8PLBlEQv0-IAegJ_Vl4lSCqXLqt-H8D4cHYIhXzbAyPhA1kWP8CgVWZ6rDZE-VlXzMDFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
کاشته دیدنی لئو مسی دربازی بامداد امروز مقابل اردن درهفته‌سوم‌جام‌جهانی‌از زوایه متفاوت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/24601" target="_blank">📅 13:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24600">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/268dcda4c9.mp4?token=INcHkPvSgXrybGzl2xs0ufg9XPJ7s0jmITlvwIeEZ6xzkTzisyjq3_jd0j6hh9C-Wb73vv_HYrC7AHKvLtc8oECUNSKIqU6qTTiRt6K0Ro6-UEwTsDc1kiSGmaUXkXe6_eKjxlIEoShWEWo1c7JXKkvPANoTtU_EEweZehwYuYpah6V1GUodkFDVZTvfZmtoq7IAI2m0kRXIX6wFA7vxIIezlrvUJ_Jqy9OAC3vYcL2CPc06DW68q8psDky8PPlEiDW2MkPue13j4rY6JA8mJJdZwS1a0IyUu_Dk4UKgrBDWLPAw0pcmCqT0wWm7whXrwnumNvJPzaAup02xctXuRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/268dcda4c9.mp4?token=INcHkPvSgXrybGzl2xs0ufg9XPJ7s0jmITlvwIeEZ6xzkTzisyjq3_jd0j6hh9C-Wb73vv_HYrC7AHKvLtc8oECUNSKIqU6qTTiRt6K0Ro6-UEwTsDc1kiSGmaUXkXe6_eKjxlIEoShWEWo1c7JXKkvPANoTtU_EEweZehwYuYpah6V1GUodkFDVZTvfZmtoq7IAI2m0kRXIX6wFA7vxIIezlrvUJ_Jqy9OAC3vYcL2CPc06DW68q8psDky8PPlEiDW2MkPue13j4rY6JA8mJJdZwS1a0IyUu_Dk4UKgrBDWLPAw0pcmCqT0wWm7whXrwnumNvJPzaAup02xctXuRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
به‌مناسبت‌دیدارحساس امشب؛
24 سال پیش، فوتبالیست‌ها رؤیایی را به‌تصویرکشید که میلیون‌ها نفر باآن‌بزرگ‌شدند؛ نبرد دو تیم ژاپن و برزیل، جایی که هیچ چیزی غیرممکن نبود. «رویای ژاپنی» فقط یک مسابقه نبود؛ یادآوری این بود که با باور، حتی بزرگ‌ترین غول‌های فوتبال هم شکست‌دادنی‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/24600" target="_blank">📅 12:37 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24599">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ATdGWwg_yMwVuKwSWuoiGvmNvJcLjjpEkMvPF7PfXt8huXxyfW5bqKsMhyEZ1MapHShOx-XUlcfM5W73HtE8wJr_O0uTfqQQ8vFasLY1Gb3fyyXhJlLquNZCYBs9nn-xkyg2zDY-N0cLHKuEcZvSf5LkqR2bAvkniJPOyoEYf-I_OrsGJp1XVpv6otACyBUvWgDvglcKST-SHOaR2GfdoXQW7RJ7OCwMc4AoXS6sjNu58-k9o3b2YVp5K3xgMWIFO8YNCvZHNBuBA8tMlvzQeUVRw_vvyPaR_1ee3oi2Xo_otL-0gdqg9czGL1HGCeDoqNN8Al-Th9YuGMBq0Tct1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
خوزه‌فلیکس‌دیاز:فلورنتینو پرز رئیس باشگاه رئال مادرید بعداز فروش نیکو پاز به کومو با رقم 60 میلیون یورو به‌اوقول‌داده در تابستان‌سال‌بعداو رو به رئال مادرید برگردونه تا برای کهکشانی ها بازی کنه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/24599" target="_blank">📅 12:23 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24598">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BMTYZZdQgaurSEknHtllWBjMizYTJD9rEReN3Db95CGfiVWrWgfMm-74da8ChKu2E4qAps7GWL_Od4UPKwMUyzJ0oz5HLovRsraljYs9DkyujMNMTrERkEuZic44gtdsoD_FNLLYd8Zh3pre2-kQwbGuDzV1-4KyLoIOqnHea3HjQpNI8l0M4kItbIVa1V5Iv-J6cLVOBDH2tvzKLMt9ItF0_vyYKZTG7xnig_kXPgz_AiPEZe14bYzGo0u6nB0alOUj5dES1-HspzR-HMZ07uKm76jKlra1PffA4n-1-dhpWQZjBfERGX_fulGkpPYUP9r2SvBe8SmpJcWvVnh0wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جالبه‌بدونید؛
پدرو همچنان‌تنهابازیکن تاریخه که لیگ قهرمانان اروپا، لیگ اروپا، سوپرجام اروپا، جام باشگاه‌های جهان، یورو و جام جهانی را فتح کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/24598" target="_blank">📅 12:06 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24597">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HDKHmGShm8GGzCk0aBco3NUKTMPQQ3S5GVLMQ7xCyiCzgSOI3UDd7KuNKRqFfPV_42SFzL_eOry0QV990bmjv9N_G614dJtSXz1LXFBdesWSWdMr2bEmc7DGfIReOTQeIrnzLyJkq7aCDsc9xDtXIc4aaEGRfcieYG4YzVKhiIY8AUi_Sj0wKJ10Lh1RD0Ln7lptehAsp48yuYS-yjupTtlhX2aR7MFwZaisCQ6_iD6TJbZVdPQxFh6lzNP4F3YdXsZsviqCl0Y7HV45nkH3tEPLL7jTVyW3rAleYYk54ei3QAH1Cs4VKWm2_PtzQJT64J2Mw_P23t7RDcXb3wejHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا
#فوری
؛
طبق‌اخبار دریافتی پرشیانا؛ اگر اوضاع منطقه آرام باشد در جام ملت‌ های آسیا سرمربی خارجی روی نیمکت تیم ایران خواهد نشست. با امیر قلعه نویی قطع همکاری خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/24597" target="_blank">📅 11:51 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24595">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u1UnNdStfMHmWlaH0wyorUqmQE2A1LVJygZWU7qJA9Xpz-ii6DGkiVVabKzq_iPNH9KD3Ny58cuSxbflo3u1M2WiYeCPpzO0QlnBWta3QpGeiBos-oWk5UeShECrHNej8SLbtUnRIDEcEoUXv84-6zW9UBnvv9Nu1GvTzQbC68AmKHWjnngk3C6xeNTpp7TpQKlw6mUMTgdB87LZPb0egCk7fpyzDSdoXKar_qH0AqJLkLWEIsa-FhJ6T2ZhxLcvPWTfohM63QgzsFO_jt7BGkbwK5ta81Liglf6uzwIDG9vePPHxNPQ7X8x53FlHtTb7_Qsna7GqLrMr43tfej7cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدار ها‌ی‌ امروز؛ تقابل‌های حساس دور حذفی جام‌جهانی با دوئل جذاب برزیل vs ژاپن
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/24595" target="_blank">📅 11:34 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24594">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QXZ1STOSt6-NJInPz_ats-6qHbZBSN23n4JZzOvggy2uJf4qMeiNLdNIYhLiwN8esW741jMutwPjzJ4Ug2LflOPIYxj5ieEUxc1GVWuJFUHehGnV8YLk_HhEyHvI-yhOPNx7uiOBDKrS-d4IU45uZossVXmGJj1N2R5ZYbJVSBIIA687fmo6FTWAol8lXu9Zjh5VXKEgEo49j3-gVr_uHYbZKElLGd-QqUCUfR8_SV46fcnjv4zX6dmePKDxrns1xwelqWN8cws7I4TSm_Rv4ffQEoHo2j3CZuzx0rM8GRPvC47p6s5NKdjhdCMxC8YVmO7lX57zrdFos1mt2HUuTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
👤
#تکمیلی #اختصاصی_پرشیانا؛ باشگاه شباب‌الاهلی پاسخ نامه باشگاه استقلال رو در ایمیلی داد: 2 میلیون دلار نقدی پرداخت پرداخت کنید تا ما رضایت نامه رضا غندی پور رو براتون صادر کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/24594" target="_blank">📅 11:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24593">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GktSHnhWr4mDfhu7D-VOzLbWbiBqVg4pH-km_jGybUJ99D3swE0K65Hmw6rd8T8C_pdbWkK7_Grr2MrOfBLcaj10HLXfbb9VlVdRUMZTWWN00vWCwII0HMZZ0De5evROkA1UPZqKlYBx_51V4n1UmP0miyUJRhSg5XU96-tIIWsR67EN4TIfjfQH-ePgdSSWb0-_NorNscjB4l6U4PtX7jsveLsUwOY3VkhX5zPKZBD3y5DVW5zRk7nMvyF1dgtJ2cVivWD-f5Vyy3Shg98yn8D60pCV_J_1CkkrRJNa_HyadMDXDTxIG7uT_S-wERO-XEFdhOsRPUXnxalxmmY9oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🟠
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال در تماس با مدیریت فولاد خوزستان آمادگی‌ خود را برای‌پرداخت‌رضایت نامه یوسف مزرعه وینگر چپ تکنیکی‌این‌تیم اعلام کرده و این بازیکن بزودی با عقد قراردادی چهار ساله به استقلال خواهد پیوست.
🔵
باشگاه‌استقلال پیش‌تر باخود…</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/24593" target="_blank">📅 10:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24592">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99ad96741e.mp4?token=DgTOA0g1eLRWZ0OPWIc8s_k-1_OhxtMqp89rxPcuJ4NnPWjqDncgcDAmOUMnhmipYEMzuTKMLFiWWcgcu5MFqw7lxYovo2Ebk-WfBqIsHB56ODIjMJo9KEv1Jwp9-bsYKP8SNrfm7pCzHtx1Q9ekzZ32mt7SrSr_3OxZT8Njxc-RuN-HKKOboQ1IsHM3VYQKo9qCb-DNq4K2nku_gBLoJXUMPxgha1ybzaBK2aIowRJjfSjQGD57y_A8zQslZf91Jy3EuMPzxOY_5MGkYtXTEUTpVsRqVqgYrObNV3TdwafwPW4yUEbUhahtMiO1V8mzyLVhHhZEYvJCFlEoBQyCig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99ad96741e.mp4?token=DgTOA0g1eLRWZ0OPWIc8s_k-1_OhxtMqp89rxPcuJ4NnPWjqDncgcDAmOUMnhmipYEMzuTKMLFiWWcgcu5MFqw7lxYovo2Ebk-WfBqIsHB56ODIjMJo9KEv1Jwp9-bsYKP8SNrfm7pCzHtx1Q9ekzZ32mt7SrSr_3OxZT8Njxc-RuN-HKKOboQ1IsHM3VYQKo9qCb-DNq4K2nku_gBLoJXUMPxgha1ybzaBK2aIowRJjfSjQGD57y_A8zQslZf91Jy3EuMPzxOY_5MGkYtXTEUTpVsRqVqgYrObNV3TdwafwPW4yUEbUhahtMiO1V8mzyLVhHhZEYvJCFlEoBQyCig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شمامصاحبه امیر قلعه‌نویی درپایان بازی امروز با مصر رو ببینید؛ از اول‌تاآخر این مصاحبه سم خالصه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/24592" target="_blank">📅 10:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24591">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WHLXPa9susxWacgHntIKmAqHnIo0yFzLo5fqlhwg1RhB4teZzqAx6cmsT18bzScjbV9M_lRrwCFSbZw2SAouZTgb3lKrt8CuoXj5sCJFSrFWf-GbMAdT5KURIJsoumcFTVQJmRjcrMAsxbAYnaLynoWbfrVg40_GGxZxJ6O5okJdPeBAY9gvDvwprUbHAmhH0bCxK7d8H2Wa3gjTKy_w2Q7EMJb7WEuQYAINlRYmBq4kvWZX6fkDZHBnC_wBcCHnEvy4yr0beLdI1bLHnG4fvu5yEMGQpWehRIVWQzuR35iTiCvx5Gvgh8uyD8M_FJljG04PIEq-oHkCMWlLzx52zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تجربه پیشبینی مطمئن با
🅰️
🅰️
🅰️
شارژ اضافی و ریسک خیلی پایین در
#بت_اینجا
رو از دست نده
❌
🛍
ازاین‌لحظه‌به‌ازای هر 1,000,000 تومان واریز بهتون 1,200,000 تومان شارژ میده
💰
🤩
🤩
درصد برگشت وجه در  صورت باخت
⌛
همه بونوس ها بی قیدوشرطن:
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان
r8
@betinjabet</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/24591" target="_blank">📅 10:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24590">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UzGWG9JvE0m6x8fA_-0YkN_-FVU9hDf0BQHvOjein4UiIYpFfIC9EtcOaAOlmJoI7P522x5uZQe5VmzPU0hRdoXDWWHpfVG0x4r7h_1xcCtYPWO10EpmSFKrKUpz39ihEt2qxqzlurP2VjQNS5dTMPpzaVaZUDTT6kM_BCa3_wQuNZ8PTcELc2ezzOU4o3CGsBgk0retrDZ11PBc10iWmNVsqDpUHLC_1V6MIaPiD8RAvYCMPjRq4-MD7NGbv2R2v5HFzflV5yV2x4i8okiE8jbHmOpYWhdNMyekVCjfdwQHHJec9kOJbe4jQTylz4uxo0ZIjgbW3O400aRbbLAWsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رسانه‌های‌اسپانیایی: هدف اول و اصلی مدیران بارسا برای تقویت‌خط‌حمله این تیم خولیان آلوارزه و درصورت‌پرداخت 150 میلیون یورو به اتلتیکو قطعا این انتقال انجام میشه. حالا اگه یه درصد این انتقال انجام نشه گزینه دوم بارسا هری کین 33 ساله است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/24590" target="_blank">📅 10:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24589">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eVX77WPDS0vXwjHculdefrAzj5kHeUT013Wvudbh54_7Ha4PQIfS9iAbMym-qnjbRK8aQzm9KLU5fvdkrorrMzKWYB5BMXdAaqX-ZfkjlkdbRaYLfzoAP_UkcasrmoQRp26uCsmNEmQP-7WFHa1YKmQZhcUOF7rirVfBIBk16sVwLE_RbSi2qKUQzmRH1pp6ZcxitgrNZIEOxPT0GT7_Lwbn2fesL4SDd13_nwgrEjbSqz81IaB7wFdNkCubtVTm78PdIp-XghsllDTtFzt5WnFhl2twgGIkSm6UIc4coJpxLt2nfvP8dxCDJGu2blIjkP8NPtd1ahJ5q_1ihLPeBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
پارتنر آقای گابریل مارتینلی وینگر آرسنال و تیم ملی برزیل که دیشب فرصت بازی بهش نرسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/24589" target="_blank">📅 10:22 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24588">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26bb073d91.mp4?token=sAVcxOh6EVzStoPlClRx3qIwP4j0zKIwEaXzsVqiZ2-ya-a1su9-3SSb49KM897564snE--0HtoOZRMN5xbJhgboSR80hmdQ730hIYhWYJCGsxo_B7da8CzGBR_IGzgbbXdbkmovjvZEgoWzoXnOn8xzVLOE07k8zgr5rp3A44Koii6zBag5Mo2P8Ps8G1rduTLFM2LlXynFczzRnJwN2hXrvfSna8ik1Ahvsba-2HwQJ-SdUaig0DjvUMouILaQ4GsLCuV7f7VUsQtX4MtossxI8KE16778II6d1-brQFVoiBQ6GfQHeeVBcKGbCfYWFGJYxuOods0fR1BSk2nldw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26bb073d91.mp4?token=sAVcxOh6EVzStoPlClRx3qIwP4j0zKIwEaXzsVqiZ2-ya-a1su9-3SSb49KM897564snE--0HtoOZRMN5xbJhgboSR80hmdQ730hIYhWYJCGsxo_B7da8CzGBR_IGzgbbXdbkmovjvZEgoWzoXnOn8xzVLOE07k8zgr5rp3A44Koii6zBag5Mo2P8Ps8G1rduTLFM2LlXynFczzRnJwN2hXrvfSna8ik1Ahvsba-2HwQJ-SdUaig0DjvUMouILaQ4GsLCuV7f7VUsQtX4MtossxI8KE16778II6d1-brQFVoiBQ6GfQHeeVBcKGbCfYWFGJYxuOods0fR1BSk2nldw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
👤
صحبت‌های‌رامین‌رضاییان ستاره استقلال در دوره از رقابت‌های جام ملت‌های آسیا و جام جهانی‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/24588" target="_blank">📅 10:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24587">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b1c18abd6.mp4?token=VRlSzhWFEwgRKth1fCbOCrogMSLTYb1nvRpuSG_xZm3ppwvlFhwyGBmJ-nN-Kc4nCBGQF84teNXKFITjCppO6lkYvAklFOEQE2bd6l9GAvBfJ5nW4nNoxl9ZYSa7RmschPWSDYdo88rrGue5fC_AXf0KQpZgsnWb6r6soSaTBnMUsaml9X-EOUhxwYP3TU_A1whYNl-OEm5MPPgIHSPiGyRu7qR8phxTqgWRkqbbJSxc7kpaECz36TyLLPxXOEuCNDHAMgJaoVFfUMKawnDeHcrY2dQRTs9XFLip12gneDT5hvSrtheNDDCRrd3knAAByqvjgI4BMMcSbf23uWW3bIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b1c18abd6.mp4?token=VRlSzhWFEwgRKth1fCbOCrogMSLTYb1nvRpuSG_xZm3ppwvlFhwyGBmJ-nN-Kc4nCBGQF84teNXKFITjCppO6lkYvAklFOEQE2bd6l9GAvBfJ5nW4nNoxl9ZYSa7RmschPWSDYdo88rrGue5fC_AXf0KQpZgsnWb6r6soSaTBnMUsaml9X-EOUhxwYP3TU_A1whYNl-OEm5MPPgIHSPiGyRu7qR8phxTqgWRkqbbJSxc7kpaECz36TyLLPxXOEuCNDHAMgJaoVFfUMKawnDeHcrY2dQRTs9XFLip12gneDT5hvSrtheNDDCRrd3knAAByqvjgI4BMMcSbf23uWW3bIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های ابوطالب‌حسینی درباره بیانیه اخیر جواد خیابانی با زبان عربی برای الجرایری  ها؛ که گفته‌بود تلاس کنید که اتریش رو شکست بدید‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/24587" target="_blank">📅 09:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24586">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2aa6f9110a.mp4?token=u_SVDu7YmyL7-PTY182qoML5sA51ij5r5oylnnj3n-rvpxOZtYQ9ApzIijVD8i5ggAzCvxcA80nBYXpRP7r0jtCNVeUIcJ3mxD8iBKZAB84-SgPqoiCmehzFc0WP4R1Tr6BTwcG0kmlnLA-qVgcVcHS6NGXZdcUuRrldzWHmiYBloESDuCvrAPK2kKQT2mwvOrmZXxQT2NpzE5PCIwv9-II6lS5iWBLiHYQWylK95yCsyymxhxLDuVpRhR5iiYziLRFyVYbXdtL4K2SW2A51NtwtuuKW1QG4zV8aceZLW3zJ5lVWZwb6nCr1EXkgMJSXRJrrKMFrud50o_VlTDfhiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2aa6f9110a.mp4?token=u_SVDu7YmyL7-PTY182qoML5sA51ij5r5oylnnj3n-rvpxOZtYQ9ApzIijVD8i5ggAzCvxcA80nBYXpRP7r0jtCNVeUIcJ3mxD8iBKZAB84-SgPqoiCmehzFc0WP4R1Tr6BTwcG0kmlnLA-qVgcVcHS6NGXZdcUuRrldzWHmiYBloESDuCvrAPK2kKQT2mwvOrmZXxQT2NpzE5PCIwv9-II6lS5iWBLiHYQWylK95yCsyymxhxLDuVpRhR5iiYziLRFyVYbXdtL4K2SW2A51NtwtuuKW1QG4zV8aceZLW3zJ5lVWZwb6nCr1EXkgMJSXRJrrKMFrud50o_VlTDfhiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇱
فوت پسرتازه متولدشده کودی گاگپو ستاره تیم هلند و باشگاه‌لیورپول درکوران‌مسابقات جام جهانی میتونه بدترین‌خبرممکن‌برای این ستاره هلندی باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/24586" target="_blank">📅 09:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24585">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👤
واکنش عادل در ویژه برنامه امشب جام جهانی به حذف شاگردان امیر قلعه نویی از جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/24585" target="_blank">📅 09:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24584">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VkYK98JkPTAwtu7FhyOPlBtl5mMTzhEkV40X-XxwSntJjPtMiOL6Kiu9ZpmNk5nKtK4H6iHi9nH5v1BtY0AilN5Hn_T8i4F_dyevPBAUQVH92nlKE_MYBbrJuihzR6s-T99a8N4AjxEvws8tHFEykYagB-HB1acRf7wJh8B8PI_7heIfbb7u2gED9eJIpMTfV5rKd3qYEdb1pfuKxmMxV_KAyE0dF1Ut2Hc1JNaGtomR2Mi6spXNr2g7TjhImHVfLHBUB2Sqi0FA7XpzG1V-fyG7mW-EZiGTaxBKuLHpnCRRNcNclkxkCbHLLYcWsl5XqoLioSC3oai_pa3Abl2xNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
شکیرا به پسرش میلان میگه قهرمان‌های جام جهانی رو بگو اونم شروع میکنه همه رو میگه بجز قهرمان سال ۲۰۱۰ که باباش با اسپانیا قهرمان شده.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/24584" target="_blank">📅 02:56 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24583">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U7QndJBIOb_qQAbZbmcReH71aU99qfTsYf7ZLqYQTXiEqMXYVkxWGyP8kI3Vg1N5hqxZwiyVz3moB7RMUhiUclyE_c-bEnIN65um5rhPxapTkcAWQzs7sXYxIVAA9MWlMNVS6kj3jmz9PumLzhMbkE5-mBddUQgH82HHaVdWq6hQVPvLax2YDRSZh3z7JaORP6jNcCUsAHKvphhZz6cTc_4acmv_Rn7VzYDChH2D3mxbKzmFDZZIOqoovxgyGHcokB5qo-o0ZxufIDYSU5p28MWOhkIDPScH6XHlAH7X_u4lpdQxaMllRRhNbjIjQ75RoDvijDno2wh-9t84VBRPiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
رامین رضاییان با گلزنی در دیدار امروز با مصر، شمار گل‌های خود درجام‌جهانی را به عدد ۳ رساند و درکنار اسطوره‌فوتبال‌برزیل کافو، به صورت مشترک درصدر گلزن‌ترین مدافعان راست تاریخ جام جهانی قرار گرفت. رامین رضاییان: ۳ گل؛ کافو: ۳ گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/24583" target="_blank">📅 02:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24580">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKFQWQo5COPaXdOd0gu-gJjGQBzUY0IVxCDL8CePcnFgUYTqfSf4DMz4k7TQGcJtzB7S88YriNfBkxdlDujA8E4pMjP0EhmDTcQOKxbKBK7SpzlhRkSN0cfzbEkV96w25Gkr5OFiQA_5qIKgoCrf-KkrnCdszngZcPdeyjKrpmo-5Nxhzldt9ZsQ3UqQEJtZ132CM4GBAv8kb1sraW_qSY3hy6kIIJjTWMPFIckKRK0VyuGW0gAmd356AHuJIkx8f0izawULIq2f0UhJ32a2yz3rat6bMKJyzlvWKVmIZ8jJnwW5cH6dlfJ62PkxuhUv1m91p46D9run_IlVMMudZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
دو بازی، 36 سال فاصله، یک اتفاق مشترک!
‼️
سال ۱۹۹۰ دیدار برزیل و اسکاتلند درجام جهانی باوقوع زلزله رودبار و منجیل در همان شب هم‌زمان شد. و حالا، تکرار همان تقابل در دیشب، هم‌زمان با زلزله‌ای بالای ۷ ریشتر در ونزوئلا.  اتفاقی که بیشتر از آن‌که نتیجه‌گیری…</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24580" target="_blank">📅 02:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24579">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mq_cReMwl8ze98VqSxyLHjiGWdTmMqXUGMyI3ipsSYaEMiA00ABWa2bUcr6EllRXGtftSCH8Uo5bl-CjRLsg-Kk8W9EAbwzKdHRT5i77d470NlazeIHSQ7cs6k-i7WLLLQUissm3nvmhSFQfZxfHBzUJGuHy-sKfEaBWZiMpAXBXWioy6_Onb7I3TvdoLNM0bh9KEr86BvYYRn0fK5cnNYOSuigfCvfxX3oV0O4IKoSdHTvNUmnnWri2W61A5VfR3UyulXs3OGAgBcUISHopXvCLk8FJGJKb6rIlGpKOYls91gBIZfDpt50lS8W-eNHR3lCsoMkOYR06sIQHN5dftA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ اینکه گفته میشه‌درصورت عقد قرارداد بادراگان اسکوچیچ؛ بازیکنانی همچون سروش رفیعی و امید عالیشاه که‌کارایی‌سابق روندارند در جمع سرخ پوشان ماندگار میشن کذب محض است. سال گذشته قبل از چند دوازده روزه کارتال عالیشاه رو در لیست مازاد گذاشته‌بودکه بافشارشدید…</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/24579" target="_blank">📅 01:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24578">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W3c_GEHVtRBU5DfuIdUpNIpqGRQt9Q-d8sJNAq9GZOzrog6wzma-AU2UxU4oP_y85SOm51TQ78JpH_1dkysSAQ_piUs6T1qr-4ttypO-R3svLBlVba396r3qO303ItEthd_7jiekyiLBNDyf0K14MT0ryKytiKAvNPDl_NTZ4Sd68fcR8eNw0tQQnotfwFlmZ2SH_KyZYJnuic5XuNTGRLcGhuB0_nCi4iD-TuqZ5FCegax3TTOksi1AGDee1lrnpKjaDELLwxHD9iETPCmzWunJ8ooa099-6ikCL0bzT5Xf_BLpVu_j2WEwak5obgiCr_EIvt60UMlu8yEc24C7dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدار ها‌ی‌ امروز؛
تقابل‌های حساس دور حذفی جام‌جهانی با دوئل جذاب برزیل vs ژاپن
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24578" target="_blank">📅 01:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24577">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XsEGogv22e97bpWuT9wq9h08J1iV59dqh5-IFD1HZMWCcnO8aR4Umd1PNYiiKQwHjT6cDhfhqm37YMEaTtbc-HitmZVqgaXUBmQmiuguK0Qa2Q-G9pxaLAMVFuL1BPwInGfW5-LEqw8NGfTm3sFZiwswNdfHAZ9NesGuo4u_Q4LvZeBkILurerS6Dz_eBstav0Ok6Cl6jIWw3lJpADr_psz12lbLNI8O7dIGwPCt9i1jpSfVWCUZz7-pezO2PRTOI0fOa9QdM0SxHyomP509UnoKCKS1sVx-VxbKPbQTvFIU1cE5o5P7Yv-O9q4nwMUL0JjU68fl_egH1sTxmRwoNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌دیدارهای‌‌‌‌دیروز؛
از توقف بدون گل در جدال کلمبیا - پرتغال تابردآرژانتینی‌ها درشب گلزنی مسی و راهیابی کانادای میزبان بجمع 16 تیم برتر جام‌جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/24577" target="_blank">📅 01:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24575">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Es_HVBD5ZMVlCkpDcDGKTyJgtsSYeRC4SNyFrl8yuFLt82PNLsXdyjhTdmZ3hFnszZpGdf8IRL1UbOp8OUA7R_IbebzbGQtWtH68VPVyG0kVLTjZfYWpEUolWEXbJgd7K_fA6UBDLB4NIXxCJKQ2B5vFMvLuw0QrzzyDy5FRVr4HcOKgg1sWQUkH-qf_3xk89JVJYEQoNbYyRHNb8puttBJOGgWNmnHsGunmYOdDpZJpWO3M77Q7mIU9Qup5rQ21YYx_pqTy17_jrLrHrTaXaAbiN444PZtqus_qzyp0ykus2BDcVi7dYBX1_0d6Ie28h4x-tTH7I6-_4N6cNGmFvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه‌ مرحله‌ یک‌ شانزدهم نهایی جام‌ جهانی؛ این پست رو سیو کنید و برای دوستانتون بفرستید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/24575" target="_blank">📅 00:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24574">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b80d476e65.mp4?token=BH7WXLP7wIQ-6OV96rGTmSbqiYZxAiuPrfsn42xgptLCS-OzdfOwsD0JSqdnuLnMoBMGfmbNK5qWNGtEeGEWDc4zLNMrx9TwfQ-Qwwk4P7mhYndNImrp64uSVMkJgnYfdERhvZ2ePlFhImhS59OC7tM65Rt5IqvxHldqN3JsE3uSbj9X_oPxLG2XFS00t9W15W2HVhH8LiCdxu3oXqp83_61lt3C2lLs3cGlA2Fo_YInp-K4rTCK9ipt_qLL5XtLmp4cEYVeUHXkeP4fA_LAr7e9OMWeR1DcSR7XrK0hRcmyu7bxu3J2lQ-eoyYaIwLBmDWQsiBaOS5p9qLudi3jDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b80d476e65.mp4?token=BH7WXLP7wIQ-6OV96rGTmSbqiYZxAiuPrfsn42xgptLCS-OzdfOwsD0JSqdnuLnMoBMGfmbNK5qWNGtEeGEWDc4zLNMrx9TwfQ-Qwwk4P7mhYndNImrp64uSVMkJgnYfdERhvZ2ePlFhImhS59OC7tM65Rt5IqvxHldqN3JsE3uSbj9X_oPxLG2XFS00t9W15W2HVhH8LiCdxu3oXqp83_61lt3C2lLs3cGlA2Fo_YInp-K4rTCK9ipt_qLL5XtLmp4cEYVeUHXkeP4fA_LAr7e9OMWeR1DcSR7XrK0hRcmyu7bxu3J2lQ-eoyYaIwLBmDWQsiBaOS5p9qLudi3jDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خیابانی‌این‌بارگیرداد به تتو روی‌دست امید نورافکن میگه حالا که‌اسم بابات‌علی اسم مامانت چیه
🗿
😂
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/24574" target="_blank">📅 00:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24573">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nWSuED_giG8lgVraoWc2OCOlA70jKMfeKUIEPL3zIfxhwS8QtdtutUmvj6SxINwOFNwt8tTvyo8IyIn6bgfNvQiwc3LSJ73FglmsUl-4v5QZE78K_CIG2_aKAZAB5_rbhzzeg4oWBn31mW8vGDacv2fXyr4RmiTjA6NyfTx7TNvY5E58RXSBHrXz2EywvgY3Fgj-0dSULQXbfZkQyIqxFKGD6dUJcGGzQtx9U74jBvxO1qjisTaxazJCIIq1jcwauE8kHh4La8k0grfrhYlFxmjXio5amXywojDhPM5m2xhhUegBC97zWS_6K7_J1JDl5BSezkCWSJinYQF2r_Ye6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🔴
👤
#اختصاصی_پرشیانا #فوری؛ مشاور محمدرضا زنوزی مالک باشگاه تراکتور که در نقل و انتقالات اختیار تام گرفته با باشگاه اتحاد کلبا وارد مذاکره شده تابرای‌گرفتن رضایت نامه محمد مهدی محبی ستاره ملی‌پوش‌کلبایی‌هابه‌توافق برسد و این وینگر 26 ساله‌باقراردادی 3 ساله…</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/24573" target="_blank">📅 00:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24572">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TLEugskvdzCa9MbQbU886Q9Z0mWtNRNc-Hx6gqNOaNkA_aIF3vehMmgsBA9BDsTa4PiwSxuraSetT6ArbY1OVYsPJ5GerJZVBneW-yzsKPpZZxT9yHe_U-YYBuop7YcRHVLTT59MmzHX77finutA26TQOgeFEw3kmuGXJ1gnMsp6DNcTWDKVwmKdq5dJDzrzqeNTdNiPn-yr-huQ0N4VVwOBwH7-YXuQ5_0tIFJrBlS-n_VWss7nnAito1LF25z1PxesZNVPC7T3ylypOHeB8lte8F0oqwUER4iT_39idd-TX-SEXB34RnYtB4DpJtRxBRb5tHYoJbtPG3CQmnqXMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جواد نکونام در کنایه به امیر قلعه نویی: شرایط جنگی نباید بهانه شود، عراق سال 2007 در شرایط جنگی قهرمان آسیا شد. پ.ن: این رو کسی میگه که خودش بعدِمساوی‌تیمش باد و هوا رو بهونه میکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24572" target="_blank">📅 23:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24571">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bbd868c90.mp4?token=kL2BrhBhu0e-Fb16ArYmxq0MOx2VVb6W6DiwO_wVvT1kBH4tdUnbJ4Ljmsfi2FQwytEoK-9fGcqXvzpWGjnAj1qvRC5Fz9C6K-ps9wyTSjVChK2_4V8OKCNRn3IMnh_dpXyywWIHvcfnxFHaXylvnzrUSH6CbJpzCiyZTBjPpuYSZHti3WKKcKfiamk2rBqSaJwFL6srBExGLlfv_9d6wvXiKYtuN89ywg_43HGW1u6J51tGOKXAHxlCt9tRppd8bPiNcXrHJjXQPfVTK9DCigiqmifaKePBoIi48zkxwiT9WmIuhbYmvq-RQ_QaBN98LPIDUwcsIsoBtfrhqbTtVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bbd868c90.mp4?token=kL2BrhBhu0e-Fb16ArYmxq0MOx2VVb6W6DiwO_wVvT1kBH4tdUnbJ4Ljmsfi2FQwytEoK-9fGcqXvzpWGjnAj1qvRC5Fz9C6K-ps9wyTSjVChK2_4V8OKCNRn3IMnh_dpXyywWIHvcfnxFHaXylvnzrUSH6CbJpzCiyZTBjPpuYSZHti3WKKcKfiamk2rBqSaJwFL6srBExGLlfv_9d6wvXiKYtuN89ywg_43HGW1u6J51tGOKXAHxlCt9tRppd8bPiNcXrHJjXQPfVTK9DCigiqmifaKePBoIi48zkxwiT9WmIuhbYmvq-RQ_QaBN98LPIDUwcsIsoBtfrhqbTtVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
صحبت‌های جالب ابوطالب حسینی درباره حذف شاگردان امیر قلعه نویی از جام جهانی 2026.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24571" target="_blank">📅 23:46 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24569">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c12652e71c.mp4?token=oD-wAPhvc67vs6lOXccJKX1y0h2v2vH3JLY7VpbgGg0QLQTJPGBSsIOfcMfFhs1ViqFn3-78mTDFgl1eqez9Z5TFS90TfBXKRVMiEArprzqLDGqenO22jEiex7BmqeZyeCwzuT8nHIBR_QHiRa8ehoS-39Le96GLU7PGbMYk25Xf_NeorVi3IA2gPYVLznoFdf-JVsmchCIlMxw8VjtxN7bIctrex3RvnQwsJXA5ROfkqaIRs3RGA_Y98q9WozOMCjArevdAkWQO_YrTaQDgYPXP_czAm_v2TtAffSzUeYf18qYlJb9xlq-asg2LW6Q6OD73cXsdZ3nIfRiGqeTpxKrQsxQyNsszx2EU_xAkBW7uAbtMpIloRD6r1UgdGbLtSs8jAi9sOxrBj-3Wz-4uqufdiCYvJPdu9BHM3fbKllGZb34g0_B5UVW437diPdSxiWrSDnWstL42uFtZgDL_e_Rblhb5OPyFvhE3uOE-RpZBzWFOAhRdqn-Nao31DTNsgj7QmVtQbXMx4Ex9vEEtzB1Bk_YZY3b5I7n7rZrFiN1D5J48mnwmXjA4E4QVewH_1FlaX2oTHLZss63-05TVKGpW3F_GsGTYv7grvOPcx4kDGcXP1YP4j3sDVfuJHZ6cRqsYol_BkF6DehttHZhLYeVbbzl8QCZuyvOERP0mjOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c12652e71c.mp4?token=oD-wAPhvc67vs6lOXccJKX1y0h2v2vH3JLY7VpbgGg0QLQTJPGBSsIOfcMfFhs1ViqFn3-78mTDFgl1eqez9Z5TFS90TfBXKRVMiEArprzqLDGqenO22jEiex7BmqeZyeCwzuT8nHIBR_QHiRa8ehoS-39Le96GLU7PGbMYk25Xf_NeorVi3IA2gPYVLznoFdf-JVsmchCIlMxw8VjtxN7bIctrex3RvnQwsJXA5ROfkqaIRs3RGA_Y98q9WozOMCjArevdAkWQO_YrTaQDgYPXP_czAm_v2TtAffSzUeYf18qYlJb9xlq-asg2LW6Q6OD73cXsdZ3nIfRiGqeTpxKrQsxQyNsszx2EU_xAkBW7uAbtMpIloRD6r1UgdGbLtSs8jAi9sOxrBj-3Wz-4uqufdiCYvJPdu9BHM3fbKllGZb34g0_B5UVW437diPdSxiWrSDnWstL42uFtZgDL_e_Rblhb5OPyFvhE3uOE-RpZBzWFOAhRdqn-Nao31DTNsgj7QmVtQbXMx4Ex9vEEtzB1Bk_YZY3b5I7n7rZrFiN1D5J48mnwmXjA4E4QVewH_1FlaX2oTHLZss63-05TVKGpW3F_GsGTYv7grvOPcx4kDGcXP1YP4j3sDVfuJHZ6cRqsYol_BkF6DehttHZhLYeVbbzl8QCZuyvOERP0mjOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یکی‌از یوتیوبر‌های آمریکایی وسط بازی ایران در مقابل بلژیک عاشق یکی از دختر‌های ایرانی میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/24569" target="_blank">📅 23:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24568">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rAjUDZQI73TMQ0swz-s9MVeXJHCpGDDT7jpBdJL2vinD7NQoexIgaCB9XrvbNXAAc73koFywum2YfZT4GAuu8cRBfoD2a6Lbv0B7FKFWSn5zUCRu02vCaXuXpXg8r6Eph1RLJm9FYwNY0JIblaNf2EVyUuG7ozvoEoSJk74RL8UZTCHki-y2s2VgHKPSLzUGHtdvoACkCel0aHNEtSHgWs7XdemgT_KxF_cDWhUGrSVNLQh725JkbDO4AQv6csS3YxU7pVVSJ8xr9De77JIjRROpYysrEW5mSBygKEL-IL-FQgq0cY6YjV2ROX1DIFOvdnf6Ss2IUboHK57PqzNriA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
باپایان یافتن مرحله گروهی جام جهانی نگاهی بندازین به جدول برترین‌های آسیا در این رقابت‌ها؛ برخلاف عملکرد خیره کننده‌های نماینده های افریقا درآسیا تنها ژاپن و استرالیا راهی مرحله بعد شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24568" target="_blank">📅 23:07 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24567">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b02328cf0c.mp4?token=FBYs8FEvjFP96Xqr2uzsYx4-9pzaZGR5jkifBfFl0H3w1ql2-N1QPp89QCVN4XIfif_HMDWAheyQFFMv7d39m-B7Y9qQXN6bQDaLW2aEIiFy8n4utfEBmv24SS6nWe4tNoD8DYiom0mMZpVodCJR7GKmWTSiTs37fmm6_LSZuLVePz24R527TEE1P5DcdDj1UY9MBb_wUsVyA8B3z_QwXKS1DahjXd6ArSTKGGoT6xj4LFu_WqxevbdgvIuxVJQtjYoIwNJFwor5kxE7_Yv2Vys1GF17SJD5KakucwUVn7YoBJYPp8gar5dWfwJtI-CG6XXLQGYd_RrsR4Z5wZWONQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b02328cf0c.mp4?token=FBYs8FEvjFP96Xqr2uzsYx4-9pzaZGR5jkifBfFl0H3w1ql2-N1QPp89QCVN4XIfif_HMDWAheyQFFMv7d39m-B7Y9qQXN6bQDaLW2aEIiFy8n4utfEBmv24SS6nWe4tNoD8DYiom0mMZpVodCJR7GKmWTSiTs37fmm6_LSZuLVePz24R527TEE1P5DcdDj1UY9MBb_wUsVyA8B3z_QwXKS1DahjXd6ArSTKGGoT6xj4LFu_WqxevbdgvIuxVJQtjYoIwNJFwor5kxE7_Yv2Vys1GF17SJD5KakucwUVn7YoBJYPp8gar5dWfwJtI-CG6XXLQGYd_RrsR4Z5wZWONQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
سانتر خط‌ کشی‌ شده رامین رضاییان ستاره استقلال در بازی بامداد امروز ایران مقابل نیوزیلند؛ خیلی باید روحیه‌جنگندگی داشته باشی که با وجود یک‌فصل‌درخشان دراستقلال به تیم‌ملی دعوت نشی و سکوت کنی و فصل‌بعد با اومدن ریکاردو ساپینتو نیمکت نشین بشی و بازم سکوت کنی…</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/24567" target="_blank">📅 22:46 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24566">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🏐
دربازی‌امشب‌آرژانتین - لهستان در لیگ ملت‌های والیبال ست اول این بازی به شکل برگ ریزونی 50 بر 48 به سود هموطنان لیونل مسی به پایان رسید. قشنگ به اندازه دو ست تو یه ست بازی کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/24566" target="_blank">📅 22:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24565">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qvvcklBkWz0Wc0i_jL_SzPFW1aWiEHszu-eq5fUV19PpQYYZPUFZ-vwnVO7ObDOrPPktTdqKEYY8ekgHvIP0viFFY2r5L6b1rOl6ma-T9dAut31XSmiL_v5FtD9anS4valVKzV23KgpShR4dfjSGRBD0tSeDK78LWK1qqYu1zy3VKVDUqvbNbBWEL7UWZjf4GilIqqVC27dBdEi1VDQ4RkQ5ex5slPoiFMMYFhvOU1Wx-JMtJOTxuds547Y3p03SOMnx_3tdZIutF1l6bIdq7Fpv0HUFA7_ZD_z4lJmYG1kcNfWAroP0Cog6LUry_XsZ3MTrWq1RP2UTtAfhKPMp-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
سرمربی تیم ملی مصر اعصابش از کارت زرد‌های مارسینیاک داور بازی این هفته با ایران بشدت عصبی شد و خواست‌که مشت بزنه دید آهنه گفت نمیصرفه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/24565" target="_blank">📅 22:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24564">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/feee4e8bab.mp4?token=pv6TfDLus12njHc7k_gNgGbAGJeYv6_0-dprYE284K9yyghtdhi6LlhdG1Sb8t5nEsZKylwdeCrev1O7o4kDNmFEyrk6lf6_XTCRSZJHGMXXigdjo1M6rx9a9XJ6rjkVXljOYSy6V7K2tlLgu3EZXHxBGmrpSDoLphggzXr3GTUHiQMhMlf4-qzTuZ0D74pNCIW8mZmBRaSABA2aEPnWJdkYpWYyZSvCCygBgKedgSwMWqBCQmAtZhyxCt2uvFBZzu4epamVCFcxDH6PDWQnU0W6fyiI1Vr4zQDPD31D8-NMkFtI94_jLkNRGvACXqszRDcSREvTQ8oR1YJ9Kfy7vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/feee4e8bab.mp4?token=pv6TfDLus12njHc7k_gNgGbAGJeYv6_0-dprYE284K9yyghtdhi6LlhdG1Sb8t5nEsZKylwdeCrev1O7o4kDNmFEyrk6lf6_XTCRSZJHGMXXigdjo1M6rx9a9XJ6rjkVXljOYSy6V7K2tlLgu3EZXHxBGmrpSDoLphggzXr3GTUHiQMhMlf4-qzTuZ0D74pNCIW8mZmBRaSABA2aEPnWJdkYpWYyZSvCCygBgKedgSwMWqBCQmAtZhyxCt2uvFBZzu4epamVCFcxDH6PDWQnU0W6fyiI1Vr4zQDPD31D8-NMkFtI94_jLkNRGvACXqszRDcSREvTQ8oR1YJ9Kfy7vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
🇧🇷
دلداری‌دادن‌کریس رونالدو به رودریگو ستاره جوان رئال مادرید که به‌دلیل مصدومیت جام جهانی رو از دست داد: باید صبور باشی تا موفق شوی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/24564" target="_blank">📅 22:19 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24563">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1f28bba8a.mp4?token=qO0iGAtG_VwZ2k-4kZvIw-0Ng6JNe71luSMRFXcsgy25PqoFwYF6dD8QJSzJ2kCVM9YTRes437gXYEtipqA4FcEq15_oSrY5n2nwKEKZBzY_pUHPNaZLXCr1pGtQ3QuiSo6QqlUCZcqfJTR-a_XVFJ0Nv2J4lA3Z9qxHkkh292GkIQhjd8_00h6lmlsKkXlM_tlImJD0VYBgUWt6I2Dit836lsXjAYIbeMCRkuUua4ykRgv5-uIZp-9KUXF-86PTWnNlC8raNSThqdHnlYGM67doevyEd5zzcRGr3HzsRnpJTSAV5Cwu78czIFT109WAKhiyZgKJBFOADGQLV-V_HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1f28bba8a.mp4?token=qO0iGAtG_VwZ2k-4kZvIw-0Ng6JNe71luSMRFXcsgy25PqoFwYF6dD8QJSzJ2kCVM9YTRes437gXYEtipqA4FcEq15_oSrY5n2nwKEKZBzY_pUHPNaZLXCr1pGtQ3QuiSo6QqlUCZcqfJTR-a_XVFJ0Nv2J4lA3Z9qxHkkh292GkIQhjd8_00h6lmlsKkXlM_tlImJD0VYBgUWt6I2Dit836lsXjAYIbeMCRkuUua4ykRgv5-uIZp-9KUXF-86PTWnNlC8raNSThqdHnlYGM67doevyEd5zzcRGr3HzsRnpJTSAV5Cwu78czIFT109WAKhiyZgKJBFOADGQLV-V_HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
کاشته دیدنی لئو مسی دربازی بامداد امروز مقابل اردن درهفته‌سوم‌جام‌جهانی‌از زوایه متفاوت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/24563" target="_blank">📅 22:19 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24562">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fKpOQqguidvyFX0uzyQss-vzGZZAfFC3XVI6sIj7J70ws0BUugNIawrM5NVpS731dXrtEvscMKfHL-8jzEleHa1PcvR3ga3PhP7GwDtvXKAsQB36kVCTH6xofdFByj4WH_Pyp0r204jjMscrJhaFlEx7ogPjY4Yg3r0D5xQ_eeZWmVaE9urtEcEmzbb_dD7qXM2_7YKpUh9sQ4wyu9qqFPZABLBw3iD7-NkfAXosyx77eHeHX_va7MYKYn_rZ6SPtROV2bppSOe6wnVhyQiCGxjyQROZdediN2t6SNbpCKgbvg6PeFu4vS42CrzbGWqmMRhP58Cc1YkYN6VWTUl1OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمودار کامل مرحله حذفی
🏆
⚽️
در بتگرام پیش بینی کن کدوم تیم قهرمان این رقابتها میشه
⚽️
🔝
بتگرام در تمام مسابقات جام جهانی ۲۰۲۶ همراه شماست؛
🚀
پوشش کامل بازی را در بتگرام دنبال کنید.
👉
🌐
betegram.com/affiliates?btag=3_l7
🔥
⚽</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/24562" target="_blank">📅 22:19 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24561">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc1de478f0.mp4?token=ZGoVZW9NuoM4ctiddhrYLtD_K4JBhvoxyXF_tfDPLmHskxqgvfRG4QmTvZjXTh6yJM6OBKRnL4g09bDEl9eAoNp_ko0loNn6gWl7hh5XEl_PEeoS9bs73-1b368mi-Efymdqk19iSzsuDlzrcvPaAS9jcXoDGWVWKTdTevqLPvEmRzjhbwhIgxwcjKvG8TU7l2u1XJmO2zHsm6TrKHiGu34J_KHweTzWfXOD9Bxsf5MbLySllHczhQJ5KkFpDNKv6_ar_nB9xgmR3HOIHHpusoH7Ydpo0ZBdz9H99_wXtgs_T9EdHmf15SmueQjDAI02I1llIQMb8GEllt9pBdHo0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc1de478f0.mp4?token=ZGoVZW9NuoM4ctiddhrYLtD_K4JBhvoxyXF_tfDPLmHskxqgvfRG4QmTvZjXTh6yJM6OBKRnL4g09bDEl9eAoNp_ko0loNn6gWl7hh5XEl_PEeoS9bs73-1b368mi-Efymdqk19iSzsuDlzrcvPaAS9jcXoDGWVWKTdTevqLPvEmRzjhbwhIgxwcjKvG8TU7l2u1XJmO2zHsm6TrKHiGu34J_KHweTzWfXOD9Bxsf5MbLySllHczhQJ5KkFpDNKv6_ar_nB9xgmR3HOIHHpusoH7Ydpo0ZBdz9H99_wXtgs_T9EdHmf15SmueQjDAI02I1llIQMb8GEllt9pBdHo0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌ های تامل برانگیز آیسان اسلامی درباره باخت شاگردان امیرقلعه‌نویی از جام جهانی 2026
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/24561" target="_blank">📅 22:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24560">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc38dbe3cb.mp4?token=uJGUwVsnWHFsF6FUGOtVGYjMeUodb2nHwd2_amFM1j8EBay7EwTaPD1ItI_G2G-65150mVAgcFx7AOpds2kFFiXrCpO_izqyC_UXw4KeJuIMJLXEEWnp1aCNHBA34TCk1JCZYd182PUd7KwKQf-xI9DECCtLs3MsBpHUiuA1zfsmWtRrubb-TkI1KqyFmy50Ta5T_vkGA7g2thhVJ35UQCjpdhKzYSaSsK_m3-ohSnLhf4WCGPlIopeKh3hJXPIMlUj93cjLMJVAfiOshStvU1PJmNcpA25fg-2m5f5dVJOjd2AQYLprD4QqN6c9rwDFevI_3vCKToWn03Jpf3wyUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc38dbe3cb.mp4?token=uJGUwVsnWHFsF6FUGOtVGYjMeUodb2nHwd2_amFM1j8EBay7EwTaPD1ItI_G2G-65150mVAgcFx7AOpds2kFFiXrCpO_izqyC_UXw4KeJuIMJLXEEWnp1aCNHBA34TCk1JCZYd182PUd7KwKQf-xI9DECCtLs3MsBpHUiuA1zfsmWtRrubb-TkI1KqyFmy50Ta5T_vkGA7g2thhVJ35UQCjpdhKzYSaSsK_m3-ohSnLhf4WCGPlIopeKh3hJXPIMlUj93cjLMJVAfiOshStvU1PJmNcpA25fg-2m5f5dVJOjd2AQYLprD4QqN6c9rwDFevI_3vCKToWn03Jpf3wyUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
یادی کنیم از این ناگفته های عادل فردوسی پور بعد از تعطیلی برنامه دوست داشتنی و محبوب نود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24560" target="_blank">📅 21:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24559">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kUz7kTIALtCpzF-vnNw7MZZR2dRLTxyx7LBAskLsrjMD20NhbTMlASAk7EcT0NYl07yTl5dw07cjNbbuF7cLxFjc5oQ68LUejt5thxAoInszb1h1e4a02hhBqntD_PJ1FT3Qq89dP8fveN6PG9j9D96vz1zDXuxDxOLJk7xL2ldPRFKsJGps0Y8jAQsmWug0AoXtKgh9bXnK2hW5tJBHtfMUaZNu7T6FipX4hUjd-WV45ckdSJUMtjGPRA2TKC2ZIMDKucBLUhA69cWqx6YScXWVS8MLhyKnT22L6wUeS1mHQLsOMHqsWelFqNge2M6eKcBRdvs9CPt-FQvhGySK4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#تکمیلی؛ باشگاه اتحاد کلبا به ایجنت محمد مهدی محبی اعلام کرده که‌حاضراست با دریافت یک میلیون دلار رضایت‌نامه‌این‌بازیکن رو صادر کنه. مبلغ قبلی که باشگاه اعلام کرده بود 1.2 میلیون دلار بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/24559" target="_blank">📅 21:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24558">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RQcqbIEluXhVi4REwU-_9SszwiIN6lRher5lPWt4cdkYuFJcVyUXo-BShGRjqt5EcEGzbZa3d4t-pI706ImNYfJgkOSLyWGvCl4VCD0d6I8SDvFuXmr2dh9sXUjiRzIzFYesXotrf6-NsIECdBHViXJ9n2nzsCTEJJStR1wR50Z0CZee8Ql-VsKLmeO9hg5sK2k4ky3dcWe9YfmdhdRfTlb-6poUQYuhjTz-TQ94wguMShXOo2v-n-uz-xmhTMRKGYrSAfANDHBoBnwZc5wwA1NMzpnFmi2CAhM17d2eeZco5qiWgttmis0nBE7Qzxy4na1UCqJtViyVHvDQiuat3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
باشگاه سپاهان 72 ساعت به سید حسین حسینی دروازه‌بان 33 ساله‌فصل‌گذشته خود فرصت داده تاتصمیم نهایی‌اش‌رو برای موندن یا رفتن از این تیم بگیره. مدیریت سپاهان همچون بقیه بازیکنان از حسینی خواسته رقم قرارداش رو کاهش بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24558" target="_blank">📅 21:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24557">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jfcuJxo4H2aem1t2Gk3Jw77kWguz6ZSzccyGIhop61M85147KouiTTU33llrcxaVjPZ4MDIqbolJ4bINdlz1Y-KvMUxmGKeKomtPVHS3xPxTZdxVDJpv6lOegCCby2_UkMGVMzeqTMMNcM_2S_GicBK32YBngOpGDA0_r1hsBFQcT3qBX8F-PgWOkH7o0VUwTINJg_-7P3ZRL1ZVOw-gZgekg-xVza542B24rgQUwrC0Ft7Nyyg8vP3WEx4icXc2TOPJGbu2WDUOT4cJNvGakRsHU53auYSTNygQ-nMatTaT11OJjMhOQkCtfRg0WD3JzT_IjKjcZM4EPn3o9BXnZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#نقل‌وانتقالات|رابرت لواندوفسکی با ایجنتش راهی‌آمریکا شده تا با باشگاه شیکاگو فایر مذاکراتی انجام بده و درصورت توافق نهایی با این باشگاه قراردادی دو ساله به ارزش 6M€ امضا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/24557" target="_blank">📅 21:09 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24556">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FssX0gz12GVwMl8x9jT6Oe8rZhnpvVAwh8z06-Kw6cMaB82oIFR__TxAXdrHyZaOK0Kd_dhEF7CRhMd3xS7uYHjXbVuWV0zkr8vXimljLkfM9DZVNAhm4c_LLm7_mT7O0UXLotu7hKzxWco3YLXSsha4FTgjcuQBES-Aj7v9IO1i0BBCEPu6tL4l5N81Gc2nqXTEuWuklWZnVWa4G0FwF3fv6fBCTrNMeFyC5TIpCj11Gz8H6CULRb5YNMD1z01rAjj82faCNpP7iDx03X5y_HDEt8uHc0v4-tXgrq1mYQHZISjIJ-vM9FXo4JUt11eyMOIMWKzm-4nvbdG62BfNsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇷
🏆
#تکمیلی؛ سرمربی تیم‌ملی‌کره‌جنوبی بعد از حذف در مرحله‌گروهی‌جام‌جهانی ضمن عذرخواهی از مردم کشورش از سمت خود کناره‌گیری کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/24556" target="_blank">📅 20:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24555">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c72aac9a71.mp4?token=jucCqbgp9v1XuQS1AYq-aeiYHVu6tKtAWNtJu5hTy_HnFpJLUB_ju7bfjjL3nIAsKdCT_QV1wfmyjYxjqcIYdf6ixIzxkaQ8m4U1k3JwIBOCNlTpiyA2sSkp_l31na7Q5qyFhIfcvFVSNZjaDPpBBT9lR-K8B5--encrJbOeGC-7GQKXHbBoEBEeySVPZ5gHx_vuHissNNWvmPtyxOsaD18O0oQvaIs3JFeSmT6miDIceiGK9TgNYwDyHRWOs-MbfXzODn3GkcrP7alR_2Qw5fJwiH3hNojqGYy22_oaNTAaPpk9qWBIUrRK6pcAYbyZIrK44qCr79Sp79kxuW8VDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c72aac9a71.mp4?token=jucCqbgp9v1XuQS1AYq-aeiYHVu6tKtAWNtJu5hTy_HnFpJLUB_ju7bfjjL3nIAsKdCT_QV1wfmyjYxjqcIYdf6ixIzxkaQ8m4U1k3JwIBOCNlTpiyA2sSkp_l31na7Q5qyFhIfcvFVSNZjaDPpBBT9lR-K8B5--encrJbOeGC-7GQKXHbBoEBEeySVPZ5gHx_vuHissNNWvmPtyxOsaD18O0oQvaIs3JFeSmT6miDIceiGK9TgNYwDyHRWOs-MbfXzODn3GkcrP7alR_2Qw5fJwiH3hNojqGYy22_oaNTAaPpk9qWBIUrRK6pcAYbyZIrK44qCr79Sp79kxuW8VDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یکی‌ازتاریخی‌ترین گزارشای صداوسیما از رقابت های جام جهانی که تا ابد ماندگار شد. ببینید حتما.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/24555" target="_blank">📅 20:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24554">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df8b1e3bd0.mp4?token=frjtvDZU_nmfapsjXjvVd86xm2ItJZyGd8UCpjToRRU3E5EqW2mfpSF94-eDMKCIlY0f6QQjgOvmtIzXsJEXvEk5XTghCckrBKrtJlaB9s4vXMVfjKsB3zUY6eJiuSPSLN_D_bwJjx3rOKkFRe2hSNg9KuRVJpZDUYF-3bR-AD0s1YshByK3DFzm9R1gdN4cpCg7YS5U7ArKn3tiyE-LRn6ls0Esf4awl0o35ruTkdVbsoFvlhRZMjeklWsM8L_czuWA51n8bdeal1cliJ3o1KHQp53vCvuum3tVJN2GMedyt8qt5fTpg0jqxF34NVAnwkU2WVpxM7KguWBgwS47yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df8b1e3bd0.mp4?token=frjtvDZU_nmfapsjXjvVd86xm2ItJZyGd8UCpjToRRU3E5EqW2mfpSF94-eDMKCIlY0f6QQjgOvmtIzXsJEXvEk5XTghCckrBKrtJlaB9s4vXMVfjKsB3zUY6eJiuSPSLN_D_bwJjx3rOKkFRe2hSNg9KuRVJpZDUYF-3bR-AD0s1YshByK3DFzm9R1gdN4cpCg7YS5U7ArKn3tiyE-LRn6ls0Esf4awl0o35ruTkdVbsoFvlhRZMjeklWsM8L_czuWA51n8bdeal1cliJ3o1KHQp53vCvuum3tVJN2GMedyt8qt5fTpg0jqxF34NVAnwkU2WVpxM7KguWBgwS47yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
باپایان یافتن مرحله گروهی جام جهانی نگاهی بندازین به جدول برترین‌های آسیا در این رقابت‌ها؛ برخلاف عملکرد خیره کننده‌های نماینده های افریقا درآسیا تنها ژاپن و استرالیا راهی مرحله بعد شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/24554" target="_blank">📅 19:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24553">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vQFv382zbyYrp-jlNQtDW8EKZyOXve8ZKPn3248kIzRixri948P7zHp1jpfq9EY_1NcwKrTQLNL9K8afykkZhAUSuGZSKqLT7BtgrQrzRtr80IJBPPxKmCnfEouKurqxlIvQsyaxLJCs8O88A5ZQrIpotwEykNSo32imR1rrfaGHL_OPpgUwWAqYL79QbaIJ7nHQ4jnXCs1RSMsuuoqCjKQhBSbslAfi71yiOwdE-uKVbwNTOVSYziQZgJonEskWdrc5tekIJLQeYGg2SmkRWeye8EjkqUrmZTr88yyhlLPL4Ng_Qtz0sKm5ft81cTt9w0nu1Y5kG4_qsNjWqyqQNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛ دراگان اسکوچیچ سرمربی فصل گذشته‌تراکتور؛ بادوماگوی دروژدک ستاره گلزن فصل قبل تراکتور صحبت های مفصلی داشته است و درصورتیکه فردا بعنوان سرمربی پرسپولیس انتخاب شود به مدیریت باشگاه خواهد گفت اقدامات لازم رو برای جذب این ستاره کروات 30 ساله انجام…</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/24553" target="_blank">📅 19:22 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24552">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a030de140d.mp4?token=qiPVMCMRd_izr8qGgzu_9IP1wWtWFSuYNeWxUNvEyOg3neQYqvuG4xMhFGOdQd0mZ_F_XAlHcTM-qr19J4kffhnV4J_hDfcCqJcpNvgwnODGKlXpsm6VSfVH0fZlx2rftipCp_ic51zYqyEX_QIBghbaJ9g1eCOh-tk09f8_5-OYO5d_kSQwrK4lp5C9iQpjV4ZHhK1UwDy_Tz1XVzr5G-mZ4hwYPYgaWQR8MHsHg5LK1DYBFRlQW2vdO_6lEq7WeF_1PUFkPT1DM78K0ES9rgf3bdUMUQvzR_bV7PGBC2CRLN_hvsb8Nvap3_aGZ9L1kt4hcv6uKK680Na_9optfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a030de140d.mp4?token=qiPVMCMRd_izr8qGgzu_9IP1wWtWFSuYNeWxUNvEyOg3neQYqvuG4xMhFGOdQd0mZ_F_XAlHcTM-qr19J4kffhnV4J_hDfcCqJcpNvgwnODGKlXpsm6VSfVH0fZlx2rftipCp_ic51zYqyEX_QIBghbaJ9g1eCOh-tk09f8_5-OYO5d_kSQwrK4lp5C9iQpjV4ZHhK1UwDy_Tz1XVzr5G-mZ4hwYPYgaWQR8MHsHg5LK1DYBFRlQW2vdO_6lEq7WeF_1PUFkPT1DM78K0ES9rgf3bdUMUQvzR_bV7PGBC2CRLN_hvsb8Nvap3_aGZ9L1kt4hcv6uKK680Na_9optfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
سرمربی تیم ملی مصر اعصابش از کارت زرد‌های مارسینیاک داور بازی این هفته با ایران بشدت عصبی شد و خواست‌که مشت بزنه دید آهنه گفت نمیصرفه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/24552" target="_blank">📅 19:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24551">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96448b3dc3.mp4?token=hsa87rGC8OkhNx4KeT7gzUGPJ1XgxUfwXhhBYtVJAchJgs4eiXyGcLmH0IA2vnSxomsoqP9aL7lB_BoRYcqQDnuyXElL-5nEnw_J-Q4VU8AP0jk4fQfNXeqBsPP95ik_BvpTL9GbQv1XJ5SbQ32GNmjL4e06yWG5uru7JQXVdT2XyFuziiF1wHw5Bd6-hqxjT1Le1t3k8u8n6i1OWyFX7AyzeXQn0_ytj4t3VED6yClzFkFVPiH45RqRsCGSamknjGVzXgNCmXFnSfvndog3MRKL6bH2aYi9OQjK2m-3zQQAGUM2HDN3pGF9R-vNPb79gawJfczOqnLC7U5w1rp8WTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96448b3dc3.mp4?token=hsa87rGC8OkhNx4KeT7gzUGPJ1XgxUfwXhhBYtVJAchJgs4eiXyGcLmH0IA2vnSxomsoqP9aL7lB_BoRYcqQDnuyXElL-5nEnw_J-Q4VU8AP0jk4fQfNXeqBsPP95ik_BvpTL9GbQv1XJ5SbQ32GNmjL4e06yWG5uru7JQXVdT2XyFuziiF1wHw5Bd6-hqxjT1Le1t3k8u8n6i1OWyFX7AyzeXQn0_ytj4t3VED6yClzFkFVPiH45RqRsCGSamknjGVzXgNCmXFnSfvndog3MRKL6bH2aYi9OQjK2m-3zQQAGUM2HDN3pGF9R-vNPb79gawJfczOqnLC7U5w1rp8WTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
تیمای‌صعودکرده‌به‌مرحله‌یک‌شانزدهم نهایی جام جهانی به‌تفکیک هرکنفدراسیون؛ AFC با 2 تیم از 9 سهمیه عملکرد فاجعه باری را در این جام رقم زد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/24551" target="_blank">📅 18:51 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24550">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cS7DqTa5Qg93FzZfeJz9RYrmLjZAhmpxE8yjTM7nJBGW7vm7wk-2yngetE7y-Ar8y-gLadfVx3VEcUfAbmE0-bu4OUf292ld_TL03s7ACUPyLbvQmH8KtuPTcsZq69uHnB3rWpupWvsebKMgyf0JgRGMYgbjVW72Mqa6GKHfQo0UoDQUy-8XEmTGGQSSkd7kiga14Rt8gy6xKoGUjV9EqNFTQl1p0sJfwRlNWJybf6vEgBnUTvBj9HIarKjB4Tk5EtJ0Ulqx397GG2Wz5YsDGKFvsZhKb0Mqb8VcVTQeMtJD7hrzrr5sUavb0E2WyaueWyrxkLfVBCIPjGzpykQN3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ باشگاه پرسپولیس 5 روز پیش پیش نویس قرارداد این باشگاه رو برای دراگان اسکوچیچ فرستاد و مربی‌کروات باامضای‌آن رسما سرمربی این باشگاه‌شد. حالایکی‌از مدیران بانک شهر از این اقدام پیمان حدادی دلخورشده که چرابدون هماهنگی با ما پیش نویس رسمی قرارداد باشگاه…</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24550" target="_blank">📅 18:37 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24549">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aN9RMiSOzNqI3pp180VFTxIVQAKQ7RZHOlhR6bmY2c5ZILJ9z-RvesGOjRdUtAXwX7zI6U76M8J7qpiYWbpt7d9IvbrRXKI7nFP0XEItyq2I5L0yKCbjYR-VtMjMS1DgXC0igB5znYSyi7xe-zKzw2DlDoHxtlK9wLZX_hDSt2MtbONqwe_q_luynroN_X9OuiLulEXR88-7HtXjx6K05uibm1haEpOvNgx9vGYHOQElLkH0Zmfsp-qCPH3RaZxB-xFX5vEM_YfCdoDIzeOsPxU6MKds1ySP0kjwHSCg0vNOBkcbBBuORT7VoC8_Pf3oRCQEoukVXrNKFZpYV0yFuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیمای‌صعودکرده‌به‌مرحله‌یک‌شانزدهم نهایی جام جهانی به‌تفکیک هرکنفدراسیون؛ AFC با 2 تیم از 9 سهمیه عملکرد فاجعه باری را در این جام رقم زد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/24549" target="_blank">📅 18:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24548">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HY89TG4F98Z0atxZm4CSowDDyL3X1rKWT6Ak_ubkUqmHB4xL9pOuYbvbTtBKnubT7dn8Un_nPXmddZMhmricidE9hN-8e-t415CX54wQCFN7AKgfGMRDKLPIMnCkk9Z2NTwqHMFHYcmYdjl_cPT8N1bOG9aLmTUV2O96a4rBbv1X-mF1NTSsipC6aNuxF5APK1sX7lmpQwUFBl9gQiW5eL4epEg-yZBhjoZeNiWx0K334LqF9IWEI5xUdLAjQ547MGRKcyzQYufCAleXqHAesj1aMGV5AsjeyiWRb6HKeWP4kOgyz_KtUoz3h1wwTJBbldhNZTHC5ubD_fnGH07Cig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌لیگ‌ملت‌های‌والیبال؛ پیروزی ارزشمند و شیرین تیم‌جوان و بی ادعای پیاتزا مقابل کوبایی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24548" target="_blank">📅 18:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24546">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbcff344a4.mp4?token=UaN-9ArgZ3rOZSdTke1w4xKsgHxMbhgY9H7wfTcjhl5uXottdEhtYRJQSWarqA1jCT34lF_OzG-JlrmH5Oz9X3y-_KXvvb2CMqwA5kIYXKlPXQnax6lGfzCuRlTVbBuM_GyYQLm5bF9RH21uy-lXvF5lABLOnH4tZRhwQXLtPEXtUIt1Xg54I5uGVqptCcptzk671Snt78itxhcsEtF_TptPGGlaDp-1V2MoX0TLShWyifL6YeJfRY5Dk1lWrxR4ZIeSN0C2WIeYI8GT9Z-_eywth5GZvW3dETymuSiU49Vvp6j7ZOhU3lKoDSy0AJkOifgKIO9X74PxWUFRUbwhxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbcff344a4.mp4?token=UaN-9ArgZ3rOZSdTke1w4xKsgHxMbhgY9H7wfTcjhl5uXottdEhtYRJQSWarqA1jCT34lF_OzG-JlrmH5Oz9X3y-_KXvvb2CMqwA5kIYXKlPXQnax6lGfzCuRlTVbBuM_GyYQLm5bF9RH21uy-lXvF5lABLOnH4tZRhwQXLtPEXtUIt1Xg54I5uGVqptCcptzk671Snt78itxhcsEtF_TptPGGlaDp-1V2MoX0TLShWyifL6YeJfRY5Dk1lWrxR4ZIeSN0C2WIeYI8GT9Z-_eywth5GZvW3dETymuSiU49Vvp6j7ZOhU3lKoDSy0AJkOifgKIO9X74PxWUFRUbwhxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سه‌شاهکارتاریخی مهدی طارمی مهاجم 34 ساله تیم ایران در ادوار مختلف رقابت های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/24546" target="_blank">📅 18:08 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24545">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Viwle0GCkjAE_CzlWp-yp7_HJSoX_X5cL3q-0xxOT_sMBrhKA5KVZTfk_u40xBl6KG1PAKEjfyRcEGa_uHLAZ9dF_DHoJXpQJosPvgWZdwNKoychp9VZ01EW160qLDxDrehPjmksAbdly4NsJ15x_nr7Jb8b3xOCMTyTOJ6Hf98EI0iLYDESWN5-n1LI48-40Us8S4dG8ir9oCunpw6zionMxU7UG8O6JPebwD7-DNc9KQYq9SliLQeL7XPwL6rJGkJurIlP10pqe3bNtaMMZWeY1lj_D_-Gr0KwuCITLoYBIAhoYoXR74lYaIqa0fv4l-recaH2dhh58tiE2MHqGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
جادوگرغنایی: کریس‌رونالدو میتونه راجب من هر حرفی بزنه اما بازهم تاکید میکنم این تیم به دراماتیک‌ترین‌شکل‌ممکنه قهرمان جام جهانی میشه. کیپ ورو مقابل آرژانتین همه رو شوکه خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/24545" target="_blank">📅 18:04 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24544">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uEjmDUXkGNlaGGVFJeBGPdn_ZzqAuLxft-EXY86QZ2RtpcoOghiEDM8JpuDkjOLrkliG8ru9aGNhdbCn-cqdYf3IBQgyWQGtO-2aIrYyDFPbG8kFZQzcY4qHYfcVOYaI9oZ35c-9AybbYi76E8395U4hbPlidU5CzRvnFJakEZa_jj8O5YlhCqMwlquln32eyGtQk6yzFbcg1U2xW1-h-XBME4CJECuaoChvpjHx-TSkctOo2tUsi8hxqmBBOqtcJt8TfkWoG8Z6pGbVWI3p-cr8sfqOg-zX71LSk-Zf4xgzz8IZSQHQYQVInP9ToQ6gZrkWG8OmK29r4afNyY3Bqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇨🇴
صحبت‌های خامس رودریگز ستاره تیم ملی کلمبیا درپایان دیدار با پرتغال و تقابل با رونالدو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/24544" target="_blank">📅 17:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24543">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UjXNZ7XenFE2Yy_1rcOBTKlfzpe-EVy9N7oPD4PXVOegAyrk_SGLsIXQKh74yItiuQv_8Un35_QYQFKskoRJS6LMdUUpUOWdXnw--8J8z3izFVTXZo0K9GjiZepRooRWvCIUgK8GjTHCKKlp973VRRuls8XAmEvALHVM7v24ShXnv09OFitdYfntnNx8ElOQhJD8mQDJwZt0_Iv-A6tpImgCTcLOZJLLsnK3AXdbVPpCUWw_ytmWhK_iuPRsccgBVo1lj5iP3Tw4bLfqfZZsoBf3q0llnPB__sJeT4gwcT-6dqWtsJd7DxGFgxUucZpfEY-RwJ8bPEAxEqTWwgk1uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مصدومیت دردناک و شدید خاویر کونسپسیون بازیکن تیم والیبال کوبا در جریان بازی با ایران؛ چه زجری داره میکشه بنده خدا. مچ پاش خُرد شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/24543" target="_blank">📅 17:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24542">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QZXHkqurhkCBv5osqPGYZrumu81URQ-OVUH0vF2BXHYgPQ4kq3Eux-Atu15IN4Pb_EuErO6ic1yP6JW-EN0tmyFgzg9p-FO8Nr9ssmEr6BdNZni9ftMty0JaGJwwmpqqFcl5BNa_XkRf8TzKkRwuqURxeaaaVfOFIms2eq4ML4OT577NtEvvCi1nKqcz0_sav1R220-Fr1_DQKAxwtHXt3jPxhkfOYqXvNKqtBhKFh2GHf0zK_XSnOcgPvK6_NMrqQsuFr37BQBc3frgvjlFtx-pahCZhWwT5jrtl4mKpjZ7dq6xHaIb4i1inxY4s9RYgA3CYKlhYqVwzq9JUtXt0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇴
🇨🇴
#اختصاصی_پرشیانا #فوری؛ یکی از مدیربرنامه‌های‌حرفه‌ای و کار درست فوتبال ایران که رابطه‌خوبی باستاره‌های‌بزرگ خارجی داره بار دیگر با خامس رودریگز ستاره34ساله‌کلمبیا و سابق تیم های رئال مادرید و بایرن مونیخ ارتباط بر قرار کرده تا او روبرای آوردن به لیگ‌برتر…</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/24542" target="_blank">📅 17:16 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24541">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NkR9ULkquvGWuIJpalmUQSjzEKC4YW8z0Wduy5Yt54k6YXYB2x-EIGOAOC3rbm0U_VbfRs7a2E52pyWw2tpPAamgcnEdQ5duXkWJI1EtqKobeJN5f_xFY5yeZ1xVsQ9iDqhVj5Oo66ZCmYgcUf-oz0R7YGlizcuk8ugPRj8g5RGx730Acpsxi3hxqxyeaKtUfGHQuylHtOkCDE27pi_s4lzXTu7eF1qugMwiziPwTe9Bsa31lkoT39xgoCtl50ahqTx5kcFx7kDzNX_D7P_DB5MS_vHg85nBPFAMtomX6JdZttahCdi77_kjkOAcj73DIwvoOEtEKiL8xTHHOCeXhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇵🇹
🇵🇹
ادعای جدید نانا کواکو بونسام جادوگر غنایی: من‌احساس‌میکنم که جام جهانی 2026 برای کریس رونالدو و پرتغاله و آن‌ها قهرمان خواهند شد. قهرمانی‌پرتعال دراماتیک و باورنکردنی خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/24541" target="_blank">📅 17:07 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24540">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TeQ96V-APsNDtbQfuKZHevjK6gFdVoujMBJIzey4YGLIuB3iMV0-LoHB4OZrA9-JlCMCt7_8bsuXmf_qX1qcd1eNgD-DsBAru8Vr3iYh76D9Y280r51Cpq2eEtOcc_WXPaDZyPaDxujrdGxGlRk6mMCxS1w8OuqAfnp1J4B4DE2hjQe_jAtB6IDK56Ut6js3bUn_LuIOowtdgiVCwFlOw1GHeY-cRdvLhZzbZDKRsjX1Z1LJDCK8VEzu0HmUlw-Ng-De6nlyef-EkHIpaL6V91P2r9ILsMcLc3KbesaTGtn-3vg6yZnJGpiyI2E7W-Chs44b0yB3vPaEaSEFDnZzqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه‌ مرحله‌ یک‌ شانزدهم نهایی جام‌ جهانی؛ این پست رو سیو کنید و برای دوستانتون بفرستید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/24540" target="_blank">📅 16:55 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24539">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/usLES---1dCDIiNPrb5RS0GvUTQYuv22ayi7j1fizU6sj3LJ2ulPo9J-SRAeAebx9zWI7vLHUr8pkjf43xkYeeH2QyrrQwos61Tqin0vDj4WkprmnKAjPWyQriYocBnHeYhx0EFvMYj3ImTYvffFJrkDZrhMmAc8Qf5i_0MD_x91i9CkSAyp1Pw4Pp7_BRE1-t74ZSzNnZI40GN0Q1H1maBeFvX6hgWkxLI9WX6bp6-GL8XB0Q87NPNceOKidE1On34xVzsVc3ju8HvENtAQEFaKDEDI-st4jpLGv8ZzAcF2YGzdWf6fcDqtENQJwxrccBeLmXUelUlmdhlfBOHKxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
سوپرگل دیدنی لیونل مسی در بازی بامداد امروز مقابل اردن؛ این ششمین گل لئو مسی 39 ساله در جام جهانی 2026 بود و 19 امین گل او در تاریخ رقابت های جام جهانی بود و با اختلاف در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/24539" target="_blank">📅 16:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24538">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DdFfOdjKfzlyzaKyivHjNlH7krNIUK2JbgAMpbUkRO_GJ56lN7E3MuYRyK2XWIBC9ENvjPy9Bn5gn990rBn6Kp7NpQEFaNAJXewtCi9wDPoYBHG_ivQro1KR3Pwrt4nisaIY-CpzK1Q4u1yKEFmVPSGQSA3CsCkWZ1VYSB3Dq4emR3uq2x1fwGhIEM-hy7_io8plbX3hZ53rnrYTAqvM3ubIsZWHxAeGU2jCpq61HY4iq7jMuZV6UG0QP5tH51bjGiZF7uWXhb1lO7Rw_-vbivg-1MRzaKUEjPkKGutgPaHCzSYux2CdRv7MfPKMkBNduAiPqWDD2_WQdACzbDz9SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قفل کردن تیم قلعه نویی روی عدد سه؛ ایران توی این‌جام‌جهانی ۳ بازی انجام‌داد که با ۳ مساوی ۳ امتیاز گرفت،۳ گل‌زد، ۳ گل‌خورد، ۳ گل آفساید زد، ۳ تیرک‌زد، رتبه ۳‌ گروه‌شد، بازی‌هااز شبکه ۳ پخش شد و برای‌صعودباید منتظر ۳ بازی آینده بود و در نهایت باتساوی ۳ بر…</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24538" target="_blank">📅 16:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24537">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc88812ea0.mp4?token=pcQXboRfnnTjl0aC9NmRXfQHDEqIpo14TPv3B2A3iPLUHd3hB7JfGgjLmePtLKXXJIcvLSAj_MrqEwFT9dBCNA_l-P-5tvq3klEP-PhPT9YXio_aFlSXo8-UK44pacAi-NykWX96tTX6T6AfdDd9ZeY9r3VNyZM88XYfqh7F7Ly_Hqf-U3cUl3ocdFdmwrOlpMyXBQms4ics2qKxlraem0iUbxIrWGafRH7sEUzrWCN_aF6oSSvIldlTFMk3AYKx9kl-PfHq65dWWEcIJObWb1WHX7apq4cMFDAOJssElw3Ig7FwQ_RBykYUFG1BxtaFlOrFsFfg68HZw2rqYXdOLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc88812ea0.mp4?token=pcQXboRfnnTjl0aC9NmRXfQHDEqIpo14TPv3B2A3iPLUHd3hB7JfGgjLmePtLKXXJIcvLSAj_MrqEwFT9dBCNA_l-P-5tvq3klEP-PhPT9YXio_aFlSXo8-UK44pacAi-NykWX96tTX6T6AfdDd9ZeY9r3VNyZM88XYfqh7F7Ly_Hqf-U3cUl3ocdFdmwrOlpMyXBQms4ics2qKxlraem0iUbxIrWGafRH7sEUzrWCN_aF6oSSvIldlTFMk3AYKx9kl-PfHq65dWWEcIJObWb1WHX7apq4cMFDAOJssElw3Ig7FwQ_RBykYUFG1BxtaFlOrFsFfg68HZw2rqYXdOLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته‌دوم‌ لیگ‌ملت‌های‌ والیبال؛ باز هم ثبت یک شکست نزدیک و میلیمتری برابر شاگردان پیاتزا این بارمقابل سامورائی‌ها در پایان پنج ست مسابقه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/24537" target="_blank">📅 16:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24536">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ShUjQRtRJ-nOeQiJffSkt9BKR-VstqvBS1pFiYzgp6skcugvKZJrW-OBBCDzOSeGudRMykLiF-meDuEd4b74LlD4zCv1za-zvEojEnQZvrYN-rWERdI0CBqQHR7x5GCHHg759HdxdRD7n4NGQp83jdVAJjKF5wA5PWy6FW72W-pTRg2nW7_gj85mqelYKPM-EA7RfvVFitjvKi-EcJgibpOk0t0byTJWKHNS63WYzf2y97jfRCv72YXtoMb4Xnw4FboslMyj0DFFtH5iDf9rRyJQfzHGT7KGb4RIzSDFEnkWNrG0Uu431PW-vSAl9KmGsxxlTMhYkKjsXiiqXhkulw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇴
🇨🇴
#اختصاصی_پرشیانا
#فوری
؛ یکی از مدیربرنامه‌های‌حرفه‌ای و کار درست فوتبال ایران که رابطه‌خوبی باستاره‌های‌بزرگ خارجی داره بار دیگر با خامس رودریگز ستاره34ساله‌کلمبیا و سابق تیم های رئال مادرید و بایرن مونیخ ارتباط بر قرار کرده تا او روبرای آوردن به لیگ‌برتر درفصل جدید متقاعد کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/24536" target="_blank">📅 16:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24535">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L6PTjceM9-8FcAsvIqHkr1BCCAm0gAcFWgYOUxmDltQQK8DidwVtWyz3iSLnlYHC2shxYGzdewgdnB-9pAGq6slSioOc8IfLKNcSqyO47jHngJxBXGDUyWK8mXiUe3VV0YSmh-SnwX_Wzq4IKPVBm1DF_WuXBcRvaZlsUbH85lCXbHDlD6P3MVmO1OfSEzPNRlzroPoqnnkwzbJa68PABa9pgHKBU2_GBbuyLg4QYmPIpox1O0rg5s4bxqszaO0wfZMs0HghurdpuZ6i7aa4O1-A-pMuWkrK50z3DaF-I-sM9MbO7jdVosHCOQxsywVSrgXzOYjV2gZuPbkaVDZAEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
درباره اسکوچیچ پرسیدین؛ با پیگیری هایی که داشتیم پیوستن‌این‌مربی‌کروات‌به پرسپولیس منتفی نشده و اوسرمربی‌فصل آتی سرخپوشان خواهد بود. فقط بین مدیران بانک شهر یه اختلاف نظراتی بوده که تو کانال پرشیانا آنلاین بازش خواهیم کرد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/24535" target="_blank">📅 16:01 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24534">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UjFq1B5jOo9bCTykMeOqUk_kqBSp6-_YmrtR3q9K7yjG5gV3Xq4WCuyrGubEuodzqTr0dL2noWGS2kvngRn47OoiV3TaqiANS_j4oJR_ODuNTKm_FjYhCIXO-g0nWZlDEvp6yiLstyMT8xsh65iYEpEZbJQDSBZraSytSDLNAFKDi7MVQ87wNtRsVEIQe5TBRElMf9S7tb0Hw2PAKaI_ALR9l2Z9NUjarBpJuu4EXSRpYGJw8X21bFRnRjFosjxnftXKeYMlQuQXB3Vee4vbE_tCYezy7qsEJlVRoEbFIKSBDfnOBNVNafYgPDyzP7OCF0YBQmmWLBzxT6uXY2Xq9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
برخلاف‌شایعات‌مطرح‌شده؛ پیوستن دراگان اسکوچیچ به پرسپولیس منتفی نشده است اما یکی از مدیران بانک شهر گفته چرا باید این دو شروط اسکوچیچ رو بپذیریم. ولی چیزی منتفی نشده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24534" target="_blank">📅 15:41 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24533">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🏆
ویدیو کامل گل های روز گذشته رقابت های جام جهانی در روزاخرمرحله‌گروهی این‌رقابت‌های جذاب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/24533" target="_blank">📅 15:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24531">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mnMsRyHzrQO0gj_ilIMG5Yg5Lz8O6XOHPSskkr2CsSycWWfMZhDJ13upjaoZt3shKvJoha5HHsiFemEJ9ytj4EZozBH0jPvk41u0xyauF4OjLX29tlejTXwd4e4tTs_YLfhZLFccbAWM_Y38EIoiiubhq3k1SnhHDTk8lcB8gvI7TVH0hXSV60QzY4JyuspuhIYNrWq6XC6mrERyZ1GSLUU43me2OFL0_QmKcpfIE7WuWAB5_hCr3s0tX_TvHUl36aC36X8DfX_LvJwokAjdAxEvF7sgwl821z7wYCBO6KpaziGZWyVGz0orI0KR1Nv9c8KkjQJ9kDGNKa_bqqD2hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f11edc5879.mp4?token=XHQIWthX6byrSg-iZQab_qkaXH-vYyBk2rO5EwmdVXmn9XCTE738BUXk-AIsakzfwF1HaeN8zbVaicnLQxA3KVENNyoLa03rlN2MkUJivRyYC-dDyPJNOsxnLLWb6fSW26fgHz3ejfoYN2eZcvqNeVj4HCcUQiY8J3xwutSIHRPPMG_3t0tQVt51qEVAFCJzwFSNcjjG8K9A-1ffLAJoZCw4DDu-O7abKeSQbof04hYknl0gL8GdwObZ-x139S5F7Hpo5tDpVKiiwMZrQGd2YHrRHkD8wooZVzTHhOo6qhhg1g5oSDy5-6BuoDIJAXMLozSVrwThSIvOFnCJazxtbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f11edc5879.mp4?token=XHQIWthX6byrSg-iZQab_qkaXH-vYyBk2rO5EwmdVXmn9XCTE738BUXk-AIsakzfwF1HaeN8zbVaicnLQxA3KVENNyoLa03rlN2MkUJivRyYC-dDyPJNOsxnLLWb6fSW26fgHz3ejfoYN2eZcvqNeVj4HCcUQiY8J3xwutSIHRPPMG_3t0tQVt51qEVAFCJzwFSNcjjG8K9A-1ffLAJoZCw4DDu-O7abKeSQbof04hYknl0gL8GdwObZ-x139S5F7Hpo5tDpVKiiwMZrQGd2YHrRHkD8wooZVzTHhOo6qhhg1g5oSDy5-6BuoDIJAXMLozSVrwThSIvOFnCJazxtbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شایعاتی پخش شده که آقای هنکاپیه بازیکن تیم ملی اکوادور با سابرینا کارپنتر خواننده و بازیگر معروف آمریکایی وارد رابطه شده؛ سابرینا در بازی اکوادور مقابل المان هم حضور داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24531" target="_blank">📅 15:16 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24530">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R0W9WaNsytsTrIHJuU-0wkSPdO9TXzz7BMj5d0Ot6HK80S2ZnFstQL8QE-_bW2LZLCZQcgUypzLhVuHg5hCKkACc52rHOpT-IcYzeKV8ts3c6U1YIqZR0vyNw9k22zPiuuZUFBmfdzclG-8wWJcrqLzoD26oWvWEEfcb0h77oPLIGysG5Ufq9k1TOl2yPSdRnhu0PdW8agZ-W9hAWR3DJCxrC96S7kbnF-5vkwNGktWeGeJ_umenPuOkNL2QIsIh9vmVcjcZW7Y0Fpz-hMLuMFYXXQ3iZBG5ApKL4czIwwgn97WrkdI0_yqgCU4DfBej8xFPA6l9dXGXiHlJr-bbdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قفل کردن تیم قلعه نویی روی عدد سه؛ ایران توی این‌جام‌جهانی ۳ بازی انجام‌داد که با ۳ مساوی ۳ امتیاز گرفت،۳ گل‌زد، ۳ گل‌خورد، ۳ گل آفساید زد، ۳ تیرک‌زد، رتبه ۳‌ گروه‌شد، بازی‌هااز شبکه ۳ پخش شد و برای‌صعودباید منتظر ۳ بازی آینده بود و در نهایت باتساوی ۳ بر…</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/24530" target="_blank">📅 14:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24529">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t2E7dgXhD9pA_0tE63B4Kzazudu0jocovnyFv6in2DnXjMmAY7Mcj6hiY_ZGy7Xmet2U_JHMYWIdYijXKVDDGisCKotX9CVkc-tIjr_xuOmmNv7VZQ1sYUp8jhvBfigDlH5Nt5F5_wyN2Lhxa_U1xDjHBFoCE0fLm2BapScRsP4KNhJ-ItY3OB7z9Tf42wjEkoeF2hcQlrlvbyd_o4yL9GTJ08_Nvy_Tfrh0xqFFxQSpn28P6CLpijHhPnCzg_kgXD6jWVDIy_x4gEL5fQLustq2s66Wvmi7ccn8VlnWwwsTki7DXe6gNbayyuzg5Xi6Ix6H1iSb7GSaCJxKR5QkTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار کامل مرحله‌حذفی جام جهانی؛ الجزایر و اتریش در دیدار تماشایی سه بر سه مساوی کردند و همین مساوی باعث شد که تیم ایران حذف شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24529" target="_blank">📅 13:57 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24528">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aabc5e40eb.mp4?token=j0YwM480_vZC1mwe0sx0zxfHq4nhjQivXTaFsNXdz2bSjMddj8EBZkZSxCRYKG4ZRCiUxDpqp9lPrzhIylx6mfu95CLmgLdNtwtwpaSDRsb_CDB4dNSeXrQVe3XfV7z-V9IZzp1KABfWZkH4MF5pRHzGEYHEMauLiIvbBtCYnJRjT7M8abkCjL7kPLL5fEVg6Ld5_X23_lLkBdZfm0dHLao_g6zCXNZI7v3LAR7k3NMg2WYR_qdCZTYiJZxS2aYBxDNDeXE_jpx_beZ-pqmDoFARQTWLltvw-u2sgPDIWbCnJSbvWKeP31TJhLxqJrYY1o2SBE9vLMFOVwo5obvIyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aabc5e40eb.mp4?token=j0YwM480_vZC1mwe0sx0zxfHq4nhjQivXTaFsNXdz2bSjMddj8EBZkZSxCRYKG4ZRCiUxDpqp9lPrzhIylx6mfu95CLmgLdNtwtwpaSDRsb_CDB4dNSeXrQVe3XfV7z-V9IZzp1KABfWZkH4MF5pRHzGEYHEMauLiIvbBtCYnJRjT7M8abkCjL7kPLL5fEVg6Ld5_X23_lLkBdZfm0dHLao_g6zCXNZI7v3LAR7k3NMg2WYR_qdCZTYiJZxS2aYBxDNDeXE_jpx_beZ-pqmDoFARQTWLltvw-u2sgPDIWbCnJSbvWKeP31TJhLxqJrYY1o2SBE9vLMFOVwo5obvIyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
جدول گروه K و L در پایان مرحله گروهی؛ کرواسی غنا رو برد. انگلیس با درخشش بلینگهام و کین پاناما رو برد. پرتغال مقابل کلمبیا متوقف شد. طلسم کین بالاخره شکسته شد و گل زد.
‼️
باصدرنشین‌نشدن‌پرتغال و صعود بعنوان تیم دوم، تقابل آرژانتین و پرتغال تو یک چهارم نهایی…</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/24528" target="_blank">📅 13:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24527">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9a62c2d12.mp4?token=RWoBTTZLtwcmbVzY7eGw2B6w1TmcZkF3wnSnl9YOaWKcUdysBatjY-J2_cJaG9J2-2vHAi0lzOE7idRpAJ1GK-gKe7BB6_7L3pbIcN5CSi7QEc1LKBtUFftEBkHLbvHHVgmeIQGUPmywZ2WwniTEmUg6gpotVQ_xN3lbIlyBu5Wo6KXXFzCdU4S0rHjdJ-zbf4fVw4j5EBMCU0AfKlm7VgV241nv-L3VITzfrE49GAonOXv9n2EaXgtU_B9zxD5W0XCDOwAamA53j1SuKFvXioz1edHu5FwFD4XRaCK52xmnzWuQnWfsLge9_iRDjPZqoTDKXqojJQos6gFF7Wz4vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9a62c2d12.mp4?token=RWoBTTZLtwcmbVzY7eGw2B6w1TmcZkF3wnSnl9YOaWKcUdysBatjY-J2_cJaG9J2-2vHAi0lzOE7idRpAJ1GK-gKe7BB6_7L3pbIcN5CSi7QEc1LKBtUFftEBkHLbvHHVgmeIQGUPmywZ2WwniTEmUg6gpotVQ_xN3lbIlyBu5Wo6KXXFzCdU4S0rHjdJ-zbf4fVw4j5EBMCU0AfKlm7VgV241nv-L3VITzfrE49GAonOXv9n2EaXgtU_B9zxD5W0XCDOwAamA53j1SuKFvXioz1edHu5FwFD4XRaCK52xmnzWuQnWfsLge9_iRDjPZqoTDKXqojJQos6gFF7Wz4vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قفل کردن تیم قلعه نویی روی عدد سه؛
ایران توی این‌جام‌جهانی ۳ بازی انجام‌داد که با ۳ مساوی ۳ امتیاز گرفت،۳ گل‌زد، ۳ گل‌خورد، ۳ گل آفساید زد، ۳ تیرک‌زد، رتبه ۳‌ گروه‌شد، بازی‌هااز شبکه ۳ پخش شد و برای‌صعودباید منتظر ۳ بازی آینده بود و در نهایت باتساوی ۳ بر ۳ الجزایر و اتریش حذف شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/24527" target="_blank">📅 13:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24525">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YdNCKhYMcWjANNAiAaomssqZ_XGTIDXd7lzlmuPdce_bpFj1TR9Ze8Q3CCklmq6_xZbqV0-PzNnB4AhC2EY2mLRGsun1eX2KxvxEk5vgzGs45OVATEwDmDjDxk8a5vAdDr9uOME9EC8J9lW_7By2Fyx5aHy3HlETGNdAj8yrQWeuIsP_-G3slys1bay6c1VfXctBEq6CHe7GcgwmcbpCJe8AuWrpbfdtMCRgTBIb07Jw7TA9fgMtZck0kp8h9L9BVDXDC-cNEvJ7-NriprYj-sLnimhhVA9we04nHWmFPk7tAZdyPiqopVJhXmU2s3HFzuukhEp6LgGg9dGVheQm0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏که‌مردم‌ایران نفهمن و بی عقل آره؟ خدا هم یجور گذاشت تو کاست که ده سال ترند سوژه های جهانی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/24525" target="_blank">📅 12:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24524">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29e51a32c9.mp4?token=SWWVPpRTXAtUxtWfDfX6hew-TuCviNW9fF2fhkifypLrH-GQWYyuF2Ax_xhQ4ICQPaPkRTJvXqW5BNA253dw29hngyBRSBqM2wSQqUJE9_Zz2zZqFAutb2O1CGMRsW484fV6E8N0yy6H_vgcPdm11xxQvX0xNuJ7lOFK_YMToqkhcq7RhmqwW1K__5RF4rwrqgpMj99NKcIjR0EvqXi8G0dR7Wu8ciQXIAnNxGpnd6moFkSUnBGNLYQdYQ1FYnGjL2txUNNni9v6DIZKX1vVeEOluwmHQPyRCokAL-NmmIlXKPGHfTiRB1dioYOxMNYrawh9EIYtUtDtegEMqFiiEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29e51a32c9.mp4?token=SWWVPpRTXAtUxtWfDfX6hew-TuCviNW9fF2fhkifypLrH-GQWYyuF2Ax_xhQ4ICQPaPkRTJvXqW5BNA253dw29hngyBRSBqM2wSQqUJE9_Zz2zZqFAutb2O1CGMRsW484fV6E8N0yy6H_vgcPdm11xxQvX0xNuJ7lOFK_YMToqkhcq7RhmqwW1K__5RF4rwrqgpMj99NKcIjR0EvqXi8G0dR7Wu8ciQXIAnNxGpnd6moFkSUnBGNLYQdYQ1FYnGjL2txUNNni9v6DIZKX1vVeEOluwmHQPyRCokAL-NmmIlXKPGHfTiRB1dioYOxMNYrawh9EIYtUtDtegEMqFiiEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
وضعیت نهایی گروه های دوازده گانه جام جهانی بعد از اتمام دور گروهی+ جدول تیم‌های برتر سوم جام جهانی 2026 در پایان بازی های مرحله گروهی این‌مسابقات‌فوق‌العاده جذاب
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/24524" target="_blank">📅 12:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24523">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K2dN9JLZ1uohZkF7shKOK_SyiVaJu7bHGEja3enUWbdy_4Owodms7e_Pj72m_dSW_k87LfjBY1__NE7MGP32WSYehGAc--t4Vi35GXpYCv2DWgsX8h46ru6MP9BPi45Wxhcl5vQMP8WCTvx4Lp3oDLykKqHWhYeQ_ptYWDw262tDP3oxB8Q0u3_EORZfqKlajHwTjwQJf1UssBMDM3iAQAQnruo9Ct4Q2mkQ4YfgI9lzx-_k4LdRvqSMk6Z0iQcHbYPDmmIMbeHA9lWBgYkBr1V3n0PliGVBqzwWbsdz5bcOtRHkzLhq_Hnr4CB5jH0yZWHj899qtrR9YkRdWJ85uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
#تکمیلی؛طبق‌اخباردریافتی‌پرشیانا؛علیرضا بیرانوند به‌مدیران‌دوباشگاه تراکتور و استقلال اعلام کرده دو هفته‌به‌او فرصت بدهند تاتصمیم نهایی خود را برای فصل بعد بگیرد. بیرو هم از تراکتور پیشنهاد تمدید گرفته هم از استقلال پیشنهاد سه ساله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/24523" target="_blank">📅 12:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24522">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rT3pEEqb_3BF5E1Y4cS0_EdL9-BctGvjNNR82HlFmReEKJbGWl12jhYNkhKw-QiS-R88IKs2FzuvirKPjOa2EA24UJUEWpnhlfLx_9X0WZkkV5FNWqxtCk0bEvnJvXlmz4gMFIFt7Wp_UJBNhCLQaUvGI1JiYUSIiRMDs7ttRKnbV5Ph8USC52NTDkPpAeJoHUEm_tWUyDs5TOn1dROak85H8ugOxKO1aUdvyatNxC5Eft1I5G3sYAl7FM4tZRc8YIEb7vU9aCJPb9A5Du5XT6atZ-5Bl6DbSLqigFv7HMdg98bdfTzTwbQopM5yFLDzJQGlYwuF2DXRCAoFYfEK_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
خود درگیری‌مدافع‌مسن تیم‌ملی بعدِ بازی با کیپ ورد؛ خلیل‌زاده بعد از اون صحبت‌های گوهربارش در تمرین تیم ملی خطاب به پزشکیان حالا بعد از برد دیشب انواع اقسام توهین‌هارو به مردم کرده.
‼️
حالا این‌کیپ‌وردبود که بزور بردین. فکر کنم اگه تو جام جهانی یه برد بیارن…</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/24522" target="_blank">📅 11:42 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24521">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jAsjwjuk224S2BZo2Xbxr6LnH_NIxc6FSNv3iN3siZYlNyxCNxUb4NeKRcdnxL0m4L75Z3wRT92j-cdbZPXbhAoCoW_XwPm_ZX8DKaP9WtXg6C1MbhJY5Az4PXqhu3k9l6M_Qwrilc_R-itiYnPLAW3EUj8dM_ex9Yoh-unonmsUuSlTSM25ZcFo-uXWI8GYTQpnd_0ehe8ELumBnjqyHjbBVrSOtZLHEn3YA8J9MYsRqBniTuGqFiWDvSPwfIACsrwXjb1TlQch69q4-iOgyEu0hLB23VmaLka52050gpTBoE2K9hgAEi-K8TLLqgdRtqz_ZaS9DYGd51-ZZrWVqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#فوری #اختصاصی_پرشیانا؛قول بزرگ وکیل علیرضا بیرانوند به تاجرنیا رئیس هیات مدیره باشگاه استقلال: پنجره باشگاه‌ تون باز شود بیرو بعد از جام‌جهانی با تیم استقلال سه ساله خواهد بست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/24521" target="_blank">📅 11:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24520">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">‼️
خوشحالی بازیکنان تیم ایران ازگل دقیقه 90+3 الجزایز به اتریش قبل از گل مساوی اتریشی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/24520" target="_blank">📅 11:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24519">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cy_2cEnq-xkfUh6aKW0rj1c_7dbHxSMPP6uY0vXovvPH0Y6OH9Uk11KhUFmq09LVA0XNqaDICUr97D2GUmn77sl6dyzL0EXm_NzyqPP8IS-W9GndXVjgG6XKIqWCECt7KWh4JQDHV8HyNKhZO_YdFS_eOQTIISYJqG28isT3pTcd054chj8Y1dV37w9BaTxPrmhsAhebqsVX613odGSgrkmqEj2FwIVxOUBQTH0O9spIbjfvaeSnQzYViJsEOtkW2M97wS_1AWED645_xO3KgMHtD11dyPn7l3h4tEmJahsYscuRx3roeBflSpxlQ86oSo4ZD7iRopgB6XEE_OUudA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
‏3 قهرمانی‌پیاپی‌جام ملت‌های آسیا؛ ‏صعود بعنوان تنها نماینده‌آسیا و اقیانوسیه به‌جمع 16 تیم برتر جام جهانی؛ ‏صعود به‌جمع‌هشت تیم المپیک؛ ‏صعود به سه المپیک پیاپی؛ ‏بهترین نسل تاریخ فوتبال ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/24519" target="_blank">📅 11:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24518">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/317abd2bf5.mp4?token=uRLaM1AeUh6PJ0lrUS88zhUjXU9KTlt-mTUsWLp6d0SVM3mCOR0z8dpw3KPB_DFQp9VC1py9JCU_XlT0uEmiDNV5HSxHiHxQzf4KUQitSZgM_2BFk4FNMoLhIs4VakQ80r3srV-NDckQx7ljbDCpDdUfAkngXkOZFJ3mR4O0FtbUDNqSbSrboh3FrtmD5f_qjgaAL98zbKc0W_ql_7dzAj8OjY4J3WTnZNwXEn4AJfq5Xj5I-rNOAeKpkhBw4krqFpArvoQG8HiKOzZ-a_c6udjz4aA_8ijDvovAvuKWynva6wkjtfWZLmdS8dPxVu6dxh91s88qdRCPgeq51_eakg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/317abd2bf5.mp4?token=uRLaM1AeUh6PJ0lrUS88zhUjXU9KTlt-mTUsWLp6d0SVM3mCOR0z8dpw3KPB_DFQp9VC1py9JCU_XlT0uEmiDNV5HSxHiHxQzf4KUQitSZgM_2BFk4FNMoLhIs4VakQ80r3srV-NDckQx7ljbDCpDdUfAkngXkOZFJ3mR4O0FtbUDNqSbSrboh3FrtmD5f_qjgaAL98zbKc0W_ql_7dzAj8OjY4J3WTnZNwXEn4AJfq5Xj5I-rNOAeKpkhBw4krqFpArvoQG8HiKOzZ-a_c6udjz4aA_8ijDvovAvuKWynva6wkjtfWZLmdS8dPxVu6dxh91s88qdRCPgeq51_eakg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بهترین‌میم‌از بازی و تساوی پرگل تیم‌های الجزایر - اتریش که توسط پیج‌های خارجی ساخته شده:)
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/24518" target="_blank">📅 11:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24516">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24998fe60d.mp4?token=tc22Yz9tm9HbsDe5ZFoMde8i0y-XTkKYUoD6BLX_FS8-j3yiJa8sIHEiTsmB9xzPiClwm9mkh3tQb9k6ER5PDMNjtlx53cvq0Yfvsxzl7TI7oY7hA1k0vo6tvo3SRThdHHSk7jhWREogI3bvJ56tSJJMc5MXnKSko6RrrQLJTCNwDtFIcBLX3w9fub1w_bC8zVGmqtW888PypXYBOwb5q8Z8UAMjZR45h0Q6-BSnQ_Az2rXi00_zjR3voLDVsEmqJkXaE0phN3d6Pvs7MhzvN1e7sgif64LGS_pzVS2jSmV4que14S9FDDUmTpgBfemiPGZjGYpLBBhRLnplwuZ5qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24998fe60d.mp4?token=tc22Yz9tm9HbsDe5ZFoMde8i0y-XTkKYUoD6BLX_FS8-j3yiJa8sIHEiTsmB9xzPiClwm9mkh3tQb9k6ER5PDMNjtlx53cvq0Yfvsxzl7TI7oY7hA1k0vo6tvo3SRThdHHSk7jhWREogI3bvJ56tSJJMc5MXnKSko6RrrQLJTCNwDtFIcBLX3w9fub1w_bC8zVGmqtW888PypXYBOwb5q8Z8UAMjZR45h0Q6-BSnQ_Az2rXi00_zjR3voLDVsEmqJkXaE0phN3d6Pvs7MhzvN1e7sgif64LGS_pzVS2jSmV4que14S9FDDUmTpgBfemiPGZjGYpLBBhRLnplwuZ5qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های ژنرال به زودی بعد برگشتن به ایران راجب بازی‌هاشون و حذف زودهنگام از جام‌جهانی:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/24516" target="_blank">📅 10:37 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24515">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4da3d833bf.mp4?token=sRgvIQC68mLKrrQKTufS3heflR4H8EDAWfbMCOmnHXqnWDZpRSqah_8TvqBDUR9AK0A3Tc3Tcp9Fg8QnqTAzeo4tGvAT-RMY56xd8qCk1FIzsERFIEGqIZFSZFjTX5qq8K9uZxEVV-Gys3C8pomxJ21T8rQAL2g6wqd1Z0n1IFyZOAcSEqkiOjToA612mIflW1KOzle7ipjY1fOXEtCTm3ebmFOc108sk_WSOfhJRbaZC6I5lrQG3ukaYfv1-kB4H8E3aY083T_5onEfZhr0BWdxYHzs8k2bjC5FY-f8ZG-OJ5hFUiYzpDP__z_-V_S3nfPskQnu_zTB_22vLRD56A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4da3d833bf.mp4?token=sRgvIQC68mLKrrQKTufS3heflR4H8EDAWfbMCOmnHXqnWDZpRSqah_8TvqBDUR9AK0A3Tc3Tcp9Fg8QnqTAzeo4tGvAT-RMY56xd8qCk1FIzsERFIEGqIZFSZFjTX5qq8K9uZxEVV-Gys3C8pomxJ21T8rQAL2g6wqd1Z0n1IFyZOAcSEqkiOjToA612mIflW1KOzle7ipjY1fOXEtCTm3ebmFOc108sk_WSOfhJRbaZC6I5lrQG3ukaYfv1-kB4H8E3aY083T_5onEfZhr0BWdxYHzs8k2bjC5FY-f8ZG-OJ5hFUiYzpDP__z_-V_S3nfPskQnu_zTB_22vLRD56A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
باحذف‌قطعی‌ایران از جام جهانی و بازگشت آن‌ها ظرف 24 ساعت آینده به کشور منتظر اخبار جذاب لحظه‌ای پرشیانا درباره نقل و انتقالات باشید.
🔥
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/24515" target="_blank">📅 10:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24514">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/947e6ca793.mp4?token=dP71dRzoBdHSwMbDFyZwBt72wPIOT3IkMN7-AQRi4KUEbuBiF5kay1IGa7iOyXlW18ndG4_rVYvh9FudbQJ0OnqeGmTj8RhMZXgj76vhryX8xhVoQzvtGEQa-2tzrPtu4hvBvLV4hzXfYr5EaF3iYmqQWgvtIU0Atv40Ycot6-adQCj1bnlQ4UnETSrtaoISvE0RlcIONyimIBCki9N0JP1DR2uJCow9XsQNwqwoEwnXAFXNRJvw2w_Lnu3XaVDJ6whMwCsuBmKNoayxj-u4EzPG6J5RvgHqF0L3EW59JtoqKpmexfF_DxIzCjGlToyk36554fuL8aEhtpmhFZyOGHG4zTaLvnzEyqymQQFXK02wyr5C7G7y_w6F24FHzKBmtwK28xuCo7axh6fPWirAyr3XuuAkRUJYzoYIbEHAkC5YVMAWoq655x9WhLUxwMGtocI-Hx8r37cfevHUeeOLXeBp1KhT6p0i3yNMuduyrTW-XcZTVKbOOchp5SjvCGLinf3PKWFA6WPCN5Hlk9__RidrAbE0_YqwvcdHA0Vi3_1XJcwYSb_Gps2l8mfXd22913FQ0mv_RofxwLMmCZ_N3UgXYzGVHFYeBghjxTka2Z7PPo25oGY8MHyyTSTH6RlMaMKVg8j10VAxtDbLIXED9SdK4475boz1ck5jdNuZbm0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/947e6ca793.mp4?token=dP71dRzoBdHSwMbDFyZwBt72wPIOT3IkMN7-AQRi4KUEbuBiF5kay1IGa7iOyXlW18ndG4_rVYvh9FudbQJ0OnqeGmTj8RhMZXgj76vhryX8xhVoQzvtGEQa-2tzrPtu4hvBvLV4hzXfYr5EaF3iYmqQWgvtIU0Atv40Ycot6-adQCj1bnlQ4UnETSrtaoISvE0RlcIONyimIBCki9N0JP1DR2uJCow9XsQNwqwoEwnXAFXNRJvw2w_Lnu3XaVDJ6whMwCsuBmKNoayxj-u4EzPG6J5RvgHqF0L3EW59JtoqKpmexfF_DxIzCjGlToyk36554fuL8aEhtpmhFZyOGHG4zTaLvnzEyqymQQFXK02wyr5C7G7y_w6F24FHzKBmtwK28xuCo7axh6fPWirAyr3XuuAkRUJYzoYIbEHAkC5YVMAWoq655x9WhLUxwMGtocI-Hx8r37cfevHUeeOLXeBp1KhT6p0i3yNMuduyrTW-XcZTVKbOOchp5SjvCGLinf3PKWFA6WPCN5Hlk9__RidrAbE0_YqwvcdHA0Vi3_1XJcwYSb_Gps2l8mfXd22913FQ0mv_RofxwLMmCZ_N3UgXYzGVHFYeBghjxTka2Z7PPo25oGY8MHyyTSTH6RlMaMKVg8j10VAxtDbLIXED9SdK4475boz1ck5jdNuZbm0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این‌ مجری بی‌ریخت و مفت‌خور صداوسیما که بیس چارساعته خدا گوه‌خوری میکرد اینجوری روی آنتن‌زنده‌شبکه‌دو صداوسیما ضایع شد. می‌ثاقی هم که کلا فشاری شده بود گفته بود دو تیم بت زدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/24514" target="_blank">📅 10:08 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24512">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nMRsya5PK8tICm3YWNHdGS8SpWwU4I3sm1K7u0cg9615ewJv8rSOvsSRXw_PIXPbl69I1ujCY9g3qZgIhnK2_h5A-2ayr9QTOol30X9Tp5vieYSdFBOepfhMlTHw9F_e4jKlhdA6ptslVAZupiirV46WHaXpddVEwYCNGQXaRQlkDHvxaUo89P1uTAipUKmrpwCDcQRSy8MvPuA-XtkgPefaY-uHIHA5SqlaKeMQUtdZQKluIJQqPvB75l5-CrGt8Y2wJQFgABy-JlF6ayf8Xr4zZ6T7a058tUgKN7lT3g-pXX5GrCjbUQ-qSgKxLsIGU-OzTfHHO9yGS5PKmL4ikA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دقیقه 92 وقت‌الجزایر گل‌برتری زد؛ گزارشگر: 7 تیر رویادتون‌باشه؛ یه‌تیم مسلمون باعث صعود یه تیم مسلمون دیگه شد. دو دقیقه بعدش اتریش گل زد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24512" target="_blank">📅 09:52 · 07 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
