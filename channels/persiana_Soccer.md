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
<img src="https://cdn4.telesco.pe/file/qfCx6nJAYKZruNdT-eLoGwGfPj3bJg64BJNDx4Gx9I0d5Iwhj9vCHY7YTZX187aQtcaRqthj8mwIgDUNDUyvYpKa9AEm8kp4OAO47J9ZJn3uaDMgxQ-Nxwyz64f_ueSRRA1EGaZYW82y2wPKI4jmA6XPfI-gB_HBeXjZnGftrglMYf9qeMLQsbbW3pIw3X4DDt4VaaA1TsOPoZ4JfCmtl4POZtWVnGN8w0kV7mqvhaxlyF5V01e6ycXV9V3iGvaCW3hO6OPMYxJExD5HsZEUOEo3ejt1hroIdNH6FJ2M5PB9fIQZ8MoRjSRtZD0jELFE9Ax9fbhpPf7q6rSFidr7mw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 622K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-11 20:13:26</div>
<hr>

<div class="tg-post" id="msg-28933">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ld7sRZ8yl7CsOuKNSeYfbh6vD5H2qrR4wtXAgng8T4LWoM4KHghi9RTbvhgCGZgHxO0_CrO2VdYsNiZ2Jf6QDGWgnuXDXZo3m2o0baDa7fs9xT5Z2EkuZjbyre7FL63tSi8n4YqtzVmlUgPvdKquS1oKBUUTIq6Eaq411mDueM2-4_T5d1TuyMKi6Nu08q2z-8a981fW7IfAhSCAZahVwDqHP4JyPHDXwiHVLP9Ni7bTE36dj8ClhYjekMzHXgN_K8eeYU71Pc0RCMGCHLDlhxva2Eg0F3hA210ZU4A5GnEDkG4u4FYO6ve-i3c5pA-LwW4DP7C858crk6iDW5gm_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته پنجم لیگ برتر؛
ترکیب سپاهان برای دیدار مقابل صنعت‌نفت‌آبادان؛ساعت 20:30 شبکه ورزش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/persiana_Soccer/28933" target="_blank">📅 19:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28932">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cJTRI8ltikY9Lx_i3iyWGzXye5fbRBzsfu8aBiWvxbYSSa4k5q4nV-1yJK2eNeDmfKxfhp_S9IyQxFfCVh4gKLbAnt7bEM1fkGNC4k5m_Z69B-xrxoQ4p13HaYLqF3YaBVAmfPleDJo3aKNkX1E7wFR9Pa4eb0EJMoHBpdUIyng0puKGoIM2w_h_KFWWG3k_pPJGfXBcPOyhYo1ugyqPd_2xyftwLKb1riLuZ0KfYo6AzZP2_M7FCwzVRSG9JaFZjhyB9umhY4VZO4AKV77e_bUkAJ5caCL8YUPqJF2Y34jKabdnv0GHVy_ijL6v0ULyoQtXfTger1CNkAcIY23EKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
سید ابوالفضل جلالی، مهران احمدی و رستم آشورماتف سه‌بازیکن‌مصدوم سرخابی‌های پایتخت به دیدارحساس‌شهراوردپایتخت رسیدند. تقابل‌ بزرگ دو تیم استقلال
🆚
پرسپولیس یازده شهریورماه ساعت 19:30 در نقش جهان اصفهان برگزار میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/28932" target="_blank">📅 19:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28931">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b4d98d669.mp4?token=LTmTZRXzW2rYx3QLpnRkbqBD1XgcLEyxX4j8emmICO-A66oQLN7GPv3-p_aiFBofrjpVRwhIC7LpME2NO2zyRd0_uFRF3Ehm1IccPg_XvRbCavMMtdDkHlIugo1vB2GnNyGQ8Oi3dkFqo331PY_RNLR9VsCsQ46cE21mojNE59ZzGRPeUkQpsLsTID529chMBq1naCOgaKJgk7epOzAn0g94mWLgIDbaahwy1JGc6N6BMRkpkNhO8UQA6q28VOFN_5KDToWbm_upltx31lIKLs-QaaURwX3S3eeTmsMfZdy0i7b3uYuobdv6k6GgtOcMKwGrTmQxz2JzRtoq8I1uPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b4d98d669.mp4?token=LTmTZRXzW2rYx3QLpnRkbqBD1XgcLEyxX4j8emmICO-A66oQLN7GPv3-p_aiFBofrjpVRwhIC7LpME2NO2zyRd0_uFRF3Ehm1IccPg_XvRbCavMMtdDkHlIugo1vB2GnNyGQ8Oi3dkFqo331PY_RNLR9VsCsQ46cE21mojNE59ZzGRPeUkQpsLsTID529chMBq1naCOgaKJgk7epOzAn0g94mWLgIDbaahwy1JGc6N6BMRkpkNhO8UQA6q28VOFN_5KDToWbm_upltx31lIKLs-QaaURwX3S3eeTmsMfZdy0i7b3uYuobdv6k6GgtOcMKwGrTmQxz2JzRtoq8I1uPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خاطره سیروس دین محمدی از بیخوابی در شب قبل دربی و گرفتگی عضله در دقایق ابتدایی دربی. ماساژ درمانی؛ جان هرکی دوست داری ول کن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/28931" target="_blank">📅 19:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28930">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eIIvYLexWLRsq3-DrVonIcYdnNrPShYokVnbTQWtvRGt2p81BEK-APS42-CclqxPqaxVclzRZLRtrvWFdynJODPcPG_xcMZ8MM9rhww0iwmM4QeNsr5oNUxMesoUEaP7UyyRnJUlkRhaCZYjSMEC_RkWE_cfuusFv3LYypQeayDw9GDYPb_vveBAru2UQE_USaMUMoPpFZZr9Dob9nJDhGjaJ2X3VUQm5c66Jgv05ls7kZov1WmF-e0kZhXAvYOS7X8Gu3SbBx8x8W2adMZaTHpD8fAHAyYawjmo2VODfDe8fGFC_8zFgUKgnUltE9eaMop0wMyxpJo7Gv4_rFeJlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیست کامل بازیکنان اصلی و ذخیره دو تیم پرسپولیس
🆚
استقلال در هفته پنجم لیگ برتر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/28930" target="_blank">📅 19:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28929">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uI3lR1VJzDZuqBXG49jP-eVS9rYb0u3cxb-yNpRyeSR1qYf_nSdBOWnGuCeddO_8SRlwvWj0vWa9suenD0B7LEbHOQJHJtinl9QKgR95DIqTx7dll5c0q0KyBDKtGEe-QbBuvSkM8jKETToG3Izd3KNKqbfA2kSFL-heLqutnui3tgFlmD127PJ_n8CxH2fbWFwUbqBOn7LMhuME-oPGutGxd2QE64IWO8rQdeNv1KDBF_qiIpmeSZAIcubKRx9rm-wqteT5On4Fb7lxbuhiQ_6l4T3b8JWFloPTlohocfsLEysFeLV__ns65eRB3ZJJuGyz0v2ZamMjLGU8R3wTeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
دور اول جام حذفی آلمان
💳
اسنابروک
🆚
بایرن مونیخ
🇩🇪
⏰
ساعت ۲۲:۱۵
🔴
بیش از ۲۰۰ نوع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۳۰۰٪ بونوس رایگان بر روی اولین واریز
❗️
💸
۱۰٪ بونوس روزانه واریز رمز ارز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔴
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/28929" target="_blank">📅 19:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28928">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d7jdXKom16nX3Gw7ipqjiq4CQdm_xL1JkX0xk0oqlRLCdiIWh8qIoWCi8DMU4lGwx1hEDbinDBrmz92_m7O-ALyIUAKMBbpsGnB-FwpaJfZLa56D7sEgMrIUTfGaEPtWeHKosc8CSK3_VhXWpGianSoDnWntSU2nYEjrLwRFUdS-sGCgzkGC2oHJoslQR0ihn001UybmhwNuBGyyTVmsaQnG0-o2LOHVCx5EeXnvAXY6ej8b1kHwR5j6oidQmmnhGQYHwaiqIvWKKW38cgDBnCtHgCbG6butCNGvX8Sf3g4mgm4f_k4ex6Dd8qxo--sG9TBpn7rdAAh_Mlr097xYew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته پنجم لیگ برتر؛ ترکیب رسمی پرسپولیس برای دیدار حساس‌امشب با استقلال؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/persiana_Soccer/28928" target="_blank">📅 18:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28926">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ktAdmI08Tvrxdi-KAMiES2DLRBgGqaBmsHiotlCq4wNGKsJRqsDdKhddmot0v979_sfzrdsS0ZeUaX8qpP25tVfIotkIcr_8hYhJaIyogWMeOcK925jIEWMIKtugQivncapByBlheQv5Azy0r-GUJyXjpF9AgfNKROB8wQJE-BoCc0zVlgC5evXQnbG7vjhLfauiAaOOn3eTPtDUoPx3xRPrNV15bRYTHIgVdn10PL60HsdGdcC96Fkio8yQsBcC9GciilddbLfJWz4Pk2L-0J3KM5KXFiW67_4FAuRQOqFDIMAh-QKzmVhbcAHEWuuckmiDfw7507q9BPhSRHxf4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/carUBFQQ0x31e4Z8xHFNKvMsWlYzH5eE-gz_P0edhCLb4am9AEujVHxTicahqX8dUEvTP516MZFXcPoa_7Qzn_crEV7fuPKcpH88TGDa2plswpI0kRQkIqif7wLgs3MvI5iDGiao6FzIX-G-wkoElQnQlK1qhUtpxaTtUI8QnCwyHm82gqdn6f_zEA927_SGD1-8asmKa4zhTPVoxjWu3h0Kxv_YidQxE-wuBk6I4K-JT5pIDPF5EfHw05ZiPcPRVkf798bMSMjdZRXX8c5onQsU9IrQl4gw5MZzLbFhlcCGPMzbXUyb-E-IU2r7k63galiasHLr1mROBo57YRYz3w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته پنجم لیگ برتر؛ ترکیب رسمی پرسپولیس برای دیدار حساس‌امشب با استقلال؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/persiana_Soccer/28926" target="_blank">📅 18:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28925">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PqMaSinfqCxEM6yyoCOTHZwkw0CgfuiwZSe2kSdNqK4k6xddDwFF37pIeP8353dlhu_WTirGIAFKGxb4q_44Xe0tC_4OZSwpKQ61ESLly5hWw55R9i9Yby-DzgIYooG_QHvHg8boJjNrb7odwwnslqgEt9kxv3ACWMCqwbZg2mVPGnyYW8DnJTsgvXtP_3ECSqzjEJDA8zRNoq47NdIrTNsbv_Lsp1FAur_mF-ZWK7picM0GiKvNPhJP-GYeRRhdUsw_1hXQi5PWowvKz1s_MXUNLMEIfDBKm3pHTNOnC-PGPWmQYGGT3M9JihC8VxXmf7vT9HkRMMgmNKYoRNvhKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همسر لائوتارو مارتینز: لائوتارو در آستانه پیوستن به بارسا قرار داشت اما اتفاقی در پشت پرده رخ داد که باعث شد این انتقال منتفی بشه و باشگاه بارسلونا با گابریل ژسوس قرارداد امضا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/persiana_Soccer/28925" target="_blank">📅 18:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28924">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uD8Hm6w0MboqcZH540oG34XASLpRQOmcSQVoKSQiULI_iQOqyYntmnGdL8jxQEIZ-VBRR44DFUYghk33E6L5i-YkUvo7iCRykvqwcPWSaTHXwjLTpsIn5buoPJ6ihSqj6m_mVFu1_ViIUY2bnAu4-f8lykyCuIHc_4q4r_l1Iqtx_639mJ6IcbOpkeZvJb_BlXCZMhICmKb75W9148_FwoCmJSOgxMjzbZWiRwvH84bMZrgs6mTC9QGrkSiofw6yJ78U5pcnilOTbe8u00HsUsPJFGqYSnjbQ5Wevxe86aS5HxIuVgbfZuqQXJxE7zExkVBNgSI95pGIB_a44cGB0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته پنجم لیگ برتر؛
ترکیب رسمی پرسپولیس برای دیدار حساس‌امشب با استقلال؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/persiana_Soccer/28924" target="_blank">📅 18:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28923">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BwmmE_yi7rFGRhxW5XVDsSdAOOzg7TTLzuUcKJXgQo87W7XGdbDM99N8Gb1NBsogSvUkZdMFSCVvlKFIfKqa5xVPCFy_p3Ij5oBODVFFGT7P5iX1a0EwJyfcPDKIcIwblwDa4Q-ZO7w-vGgnaCn_YEHfs-m38A3l340R_WpMsdH3bCjO9i2EUjrre8lVB_g92RAZFImR5h_pkiP89gHjTA_XPkKfeowDOMravVyAY4iusGn6gX-yT4aoCEbRnBUmVWZ9WcEr9vqXUk1gQDY8fTW9Upd_yKVDDCWboH2ZeueuPrvNzeEjhfocnKoeG3pB-u0z1k41gWEbp0xTsDgAEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
شماتیکی دیگر از ترکیب احتمالی استقلال و پرسپولیس برای دیدار حساس امشب دو تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/persiana_Soccer/28923" target="_blank">📅 18:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28922">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vZpV54iwL7a1Yilnkaiuzh6YAuoyvFpgRKBLi7CphCqyBptRBDm26sRBGuXhWF9x6zMrpEZ5EmfH3uIoUzsEDttOGmaiQqWwSpVRQsqNqUDuXkv7-x5OE5KUv5fV1WMvyCG2R0XmFjAEM0JlB1Aw5T2F7snklUkqdwmgODagi2pwb-VXIyXkl2baKF-EfvvQ9MS_EZ5m7jKC2O0MxV3v2COZmIxVl5E350NiXgnccTIlG-RE1iwgMj_9VoucTFVKQnz-sveBRhl7tC_6cqPYWLcyjXnfk7Z_c-tUMOgqohpLqlcQDj7xVCn2EltLrevCSyAbpkvTfvql5Dx9ryqnMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نگاهی به‌عملکرد سه مثلث خوفناک فوتبال اروپا درسال‌های‌نچندان دور؛ کدوم خفن تر بود بنظرتون؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/persiana_Soccer/28922" target="_blank">📅 18:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28921">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa3087d7af.mp4?token=pQi_Y64tlhHw7arEI-WSg17WHNNNVfRF_G4iRkgmHKWQNDru_Z3-6YKp5BgpTLjAr_V63BpFoUSSLrDnYCaajrwnofpdBhqvIhR5LJkRv_AJ-qmapZeIW1yV_-lt2ECsgjrtnoJcIUlV4TBAXbarw6u4J_MCvv5Qbu06C9QXN5cQAQEg2e2wmccdtwJMUgyxcbkJywZUmW7uo_sC_y6vfXSo7vCikG6k63f0kcy44YfI9PqIXvREaKOdvGUUEP50ihdMegStQw3GXE6IUiagrJ2v1WMg0TxU4SCfjzt7c3--082ywpJhXXV7LioH2g18AQKfejdmbsrmpEaQfxgK_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa3087d7af.mp4?token=pQi_Y64tlhHw7arEI-WSg17WHNNNVfRF_G4iRkgmHKWQNDru_Z3-6YKp5BgpTLjAr_V63BpFoUSSLrDnYCaajrwnofpdBhqvIhR5LJkRv_AJ-qmapZeIW1yV_-lt2ECsgjrtnoJcIUlV4TBAXbarw6u4J_MCvv5Qbu06C9QXN5cQAQEg2e2wmccdtwJMUgyxcbkJywZUmW7uo_sC_y6vfXSo7vCikG6k63f0kcy44YfI9PqIXvREaKOdvGUUEP50ihdMegStQw3GXE6IUiagrJ2v1WMg0TxU4SCfjzt7c3--082ywpJhXXV7LioH2g18AQKfejdmbsrmpEaQfxgK_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔴
کری جالب و دوستانه بانوان دو تیم استقلال و پرسپولیس در فاصله دو ساعت تا شروع مسابقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/persiana_Soccer/28921" target="_blank">📅 17:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28920">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gg_6wFprsn2CGTTHJZNmMuBPD9_q6IxXsf94rTNEOoqDymSSPmH5JshBwRBXN3AC6r9WZVxn6oTqp5lIUVxd90AtxvDT2ioytJ8QUfoj2AQiLPmU0rJiXXACjondrkO9k05G2emayxC50mUyX0q6PyjpYPMxEYQPbSggh-T_BZTYatEtvkYl0Q6sj8QLbnS-nweRpIXK2uOezVV-F73J_PjPm2VwVcmd64WKfJBtSarPozMifr5V8mPc4komFIdOlyfOqzoVvPkC7QKFY5BiSgZz6ifRn_GjoEiLBS-CIGrYHtPSY6icnHuSy7E7H805pU7x075E0CPD0Jmr8ypLNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
چهار دربی‌جنجالی دوتیم استقلال و پرسپولیس در تاریخ این تقابل‌ها که نا تموم به پایان رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/28920" target="_blank">📅 17:17 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28919">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HKYHNi_-oK-G3N02ZI4vHk0wfaSdpg1Q2auLRVpWK3CpDa9hpvq9_kQP-_sx6sn4Q_7HYhjloPy9e1NCdEtL1QtKV2Xrq0hj15Ms2hdg5agnT6ErnXN51GPcLGbWLMpLhjy6liEd3sxMp7vt4bNm0o2E_YLoSRPS5xtfshBaxt_JB4mmforYh4gfXyWs8sUN0gX2O8xLQ-8ruzbKR1Mth7rXgCNn0dQeXWbrRGUV2ui5vun2jLKB7Ec-Yj3jU_-uh6gBa4U4yBKYNPfmJJDfz-K-ADIKeKmlwdotKjl1gm1NI4Y2eBOQRhoTVCRePC8Zz7yYPayANoRem3StWRsviw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد پیام نیازمند و حبیب فر عباسی دو گلر سرخابی ها در تقابل‌های خود با این دو تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/28919" target="_blank">📅 17:03 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28918">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uR0GxGIxZ0i8sILbwbEwYE56yYxHXA1-HGJSF1WDQummo52TRXmXZYKNIQ2EYkMz1n57qeDEZWpxHXElb4sntBQJEjUQGI2j0ckpJA5Ub27KNZX-g9k2KX1YyLLVakP0tRiVMfZ1M_9fgJ7wH7GeCHGkHatsLq7GjYTEq68KjgSadRgb8R01mLcxlzv0AbNq2vweJ2RU4rBkrp3A4xdeg8Myvpctk2sELWpd8oImxEDBEQBVbTA9uS4MeFEEas4YDRDIhpihg99c7_bkbGCMBb51reTvPzUcCz4L0AIYdwX1rxTvVWJnwnX6Z1FGER0JHLj1ObW-rzftssQabMc1Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مسعود جوما مهاجم سابق استقلال با عقد قرار دادی یک ساله به تیم الحسین اردن پیوست. عملکرد فصل گذشته جوما در فصل گذشته: 33 مسابقه، 19 گل زده، 8 پاس گل و نمره 8.1 از سوفااسکور!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/28918" target="_blank">📅 16:47 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28917">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/osT4L4gFJpvIJfsK_oBCxGdBa6kKe1pvNElaLKqRqL_5gAawh_93RNFNGgsuhE1jgXZI4qpOLF_8YtWSCUtTIjpGUda4KKO6wWUaJ3o-uaTf5GvpYFyRbF3QmYwV3Rx_wRpjHikCoIKqTaE_uPoYwe8JDoTkQ3po6SRtMY4m5lxdQHNN_Fuo5OLKrCjhn2mrc1baBFWFZK6TSh2NSRtDEP6rlE2TZMHnBo5a4tAIG72zGUElkaUMSQ9yYXlDFmCOtbpETZx6U3fYcqXzFeTxieOSX-O5zOh6UH7LE2PzNxGBMahBaA0cDHomFkDkC-dgedOUgHyYad2UAYQOsnR_MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نگاهی بیندازیم به عملکرد تارتار و سهراب بختیاری‌ زاده در تقابل های خود با استقلال و پرسپولیس به مناسبت بازی حساس امشب
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/28917" target="_blank">📅 16:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28916">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mOJ2MaqA0Z9ehkl4b-rp5t75V67oK1b7gbfunHKsXXixKFGhZ8Y2G4cDNSHv5U3EjTDAa3mlftmky1kKZ726zi5Sy4PtBuGfZ9aXKjBhJe5y25ZWvlC404GF9KR8y18lHOQlSH40732wBWXy4vbcY2jXFvfmSN7uhAAH4Eh1WeeCIQ46LKGZYoRd6sSYpa36oMj48LkmpCA65nMIVCnObqjKWDbIB6fwD2Dn_zUtQe7xewNbbi1bjMlaSvb82ggduC8pY5BLFXC4DJz0Drm4M9gSVMdVi4sV1ZCWwQB6QbKkXlNMCpjFcX2A50YG10Yxr2NLAWTVIr2D1Ue4WonwCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
درآمد فوق العاده 200 میلیون یورویی باشگاه رئال مادرید درپنجره‌نقل‌وانتقالات تابستانی امسال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/28916" target="_blank">📅 16:03 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28915">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GgVVEDvj89V2-Nq9R1vDYyzSTxu4J960xlCEkqQ_a94mcog6tRAgVUzj1Cv3ZQGCFEMxCNYQ6OAUv5c_mArglqpJW3AdShQUwjOFcYCAiNd9sJF86if_9DqxHSKqJa0kxI3DSdtdM0nx7MpgKVdfw_LyRBeS4lnpyMfLjsvqI6cljg3GfcUC2iWpb2B2iZnsj92T5ZRapo1RHN_j_F8bs5sFzKZSn62WxhXS0EBTE03AQ7-YpvSCD0dUDZzcJf5TL0axAxnPYGyOlJadkOGGYTx_H94dKAqCc8_80Q_cY68RQgySJb3oUOe6-ROtOdehJy4YIRF-sFdnlyGkWOwZ4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پیتسو موسیمانه سرمربی سابق آبی‌ها رسما سرمربی تیم ملی آفریقای جنوبی شد. پاکو خمز سرمربی اسپانیایی‌سابق‌تراکتور با عقد قراردادی نیز سرمربی باشگاه مراکشی رجا کازابلانکا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/28915" target="_blank">📅 15:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28913">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NNyAfhzhKKXGiv25xoS9uxjyLA3VA_LB2K5Dq4C5Ltdpo3w2LGTL-Scl9PHGHcUHEQaGPUghM2SVJ4JZV24S_fCSnDAmdCSI85VGgjJrnh1YNndjjKcOGuAKF2cEVAlQiGx4L5BvuiEuWvkEPPPg_XJflr4So8IkElvhISkKQf1GoZTdDntUSXXf0R_iUXEWQT_yx54-kdaPWxZ8w_v3gwryfBFRIqXzJAIO9sj_be9gbZi2LwV3bHEQzwlXOcpf58hCMKgKVihKwH8RHYvHWG7LvxgV3AnvKEP9YKeZC-KiyUaiTkmNj9-b3_t_peFktVfJu5G8esAPju0UcCgFNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dLL6ezR_TMnFYDOuA7JgwIJ4LORsIfczKnF8pPb5y7lt0n69B5oqq-VlKc3f-gyetJeFLXTprQ2bWs4ToViq0OY7jc6abjD9Xf61VHg8eqGjpf72gw4mtmr2onJRRO57ixFOaApukmi4IAg4p_yunhE-wQZVERVAZchO3vAhsYJRkERLNLkQ4vVLmR1-_Y2hIw-AUY8DQDQ-bIfwGzY9KMMco5t7frwa8rjJ38VOtpnGbiOHzlhz798AoSmnCFb8wAoXNRL9yY26kJsWme3eRtN4jVtokLyD9cLUD00Lyt8n0jBV4xx4xd-bVZZdzwKelfDredaV74njyVJUzH_ZtA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
کارنامه و عملکرد دو تیم استقلال و پرسپولیس درفصل‌جدید رقابت‌ها پیش‌از دیدار حساس امشب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/28913" target="_blank">📅 15:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28912">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nN3T_XGVy8lDC07vUwGH5udcndh5fSkcMOW-ny0WuAA4qefiDTP3ybdMqcT6rzjxt0TG0_1jxAvdw3Me6Yclw-_xUKEeXRNHs2BY9gPc4xbfIMgCkT5V0SZNAkv6jT0n4HJremkKdoSS3eq1zA7t9y3GSZZZUKIiJbjVfjyklfRJdnWrKFHwO3DJISYg6XUw0UI-nI-4CfOHxRu8MWt-wlnFSW-1Hhzx7GWZIyFcUbsr3UHd16jQ-JPH7N-AdUQ0-S2QGwGMDBOuAr7w4DcZwjAvKBMv8yV_PZD2bDjJvnRJSU92YrTv2SE967sa1Klgjbjgbtb0pDsYfY5-ZHeoXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
کارنامه و عملکرد دو تیم استقلال و پرسپولیس درفصل‌جدید رقابت‌ها پیش‌از دیدار حساس امشب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/28912" target="_blank">📅 14:45 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28910">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iNSE7KK_nWZrhj0FbanPe-fy72hnvtnAXjz-YvF0VNnANrr1neKlfdSMU-nyu1bbWK1cLKTpRUQiZxU6fJxpATttOJ4nZwT6GpLuYoYWKpnv0T-xgNZ-X_iTyb9k3hNtdDKjfUGf1rW9qaa_G48t1w8wK2LfQnjr2RfvQ5bk8PHpS62i1V_tI9k5KutwwyAQ2ruQJIsEZifHgWSf95AayWfgXQFrzG-RUZgs3VX2EAZJwGz9Y6l13eLAqk21VsdMqYKIY-iRaGLMpHQD0IaYghX30j_e-sM4D4A22ZzC3D4mXPq58jT2_jSqFqPRecxOTa5yepet-1MR2uJFpZJu_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
عمق اسکواد بارساِ هانسی فلیک در فصل جدید رقابت‌ها بعد از جذب ژسوس و اتمام نقل‌وانتقالات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/28910" target="_blank">📅 14:11 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28909">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abd0f14bbc.mp4?token=aK5EBrCBjtmDe4hss02BffEYfosx6vTxizG-g_Q1xWtfgdEQ4HfufNvQQuLmBZuXlTNJhFvniv72fk493qK-MhJMJcIjjLjh94oyZOvxAZLN3aN3IEcJ-g9DOMKa6LVyybtc5Aec2tEK5ply411vUxM8ggTuwZiI_kRqsB8ULJ63BcinCgu7v4-J3Eprb8zvJvYruzC_NDhUnWjtudv1x9nscuwrY8l8EBok_4hq8uIeCzudtd6l-U747Q9JRacG2M70dNGBROfU7It62uIJt7EC3rk0PohvTrrPkYUYb22pw8T64WtloeojcBffIO9WGP1xcgdQv7MUMOKbc3tbIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abd0f14bbc.mp4?token=aK5EBrCBjtmDe4hss02BffEYfosx6vTxizG-g_Q1xWtfgdEQ4HfufNvQQuLmBZuXlTNJhFvniv72fk493qK-MhJMJcIjjLjh94oyZOvxAZLN3aN3IEcJ-g9DOMKa6LVyybtc5Aec2tEK5ply411vUxM8ggTuwZiI_kRqsB8ULJ63BcinCgu7v4-J3Eprb8zvJvYruzC_NDhUnWjtudv1x9nscuwrY8l8EBok_4hq8uIeCzudtd6l-U747Q9JRacG2M70dNGBROfU7It62uIJt7EC3rk0PohvTrrPkYUYb22pw8T64WtloeojcBffIO9WGP1xcgdQv7MUMOKbc3tbIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
به بهانه دیدار امروز استقلال
🆚
پرسپولیس یادی کنیم از این سکانس به یاد موندنی سریال نقطه چین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/28909" target="_blank">📅 13:55 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28908">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K4QLeTKEYj_RqCIXmohChz4-n355AhHAHuRW8jBpKILZntwunhwnZ_AECCzUdkdN67lMI7kYpvDsSbEWRbvE2CzWr9U5Js_81Lg-YY7DBl4sybhTXoS4NC2ME_xDLi7ViQIoLeiAB008pPrMmhYMvNut6RzfeLIjzTLtAwjVfzh5N5SyCjCSQ-y7baoe3-LNK0_dvDSzvloZ6gTxYlaNZ5eswkTsOYYNAiD59EHqSIVOk3lCbJwaj4t9H8iTxY8p-bJqPBVuPWOnHDtAa4__ei_V1SSWmYf0JKirxp4mvmLRGLQKMuFioXxkUZoMky5YamDA2EBJP780hzGFAn80vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
رکورد داران بیشترین تعداد بازی در دربی و رکورد داران بیشترین تعدادبازی بدون شکست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/28908" target="_blank">📅 13:41 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28906">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JDy43C1m3LtJWNK70VB_og7jmYACuM572Edp1EaHEoYducyoi4WGthQAH3TYBPTTj74IZ5Gd_QGqdqD-Ro532UHz_336s0h0hTPg3ov1iYyDQXnrMwmzTmF1tx10bEUxrS6Gu8S2s-9q2Az3fwf7aFz9W-FBBNyClEktKSMYGd5dWZ60grC03z7sCcFTDpqW-U6XC6GmmfUyAPzm643GQEiV1ZHVXv05Tj1rZGuUGdb7Smnfzr0ayhAI1awLfMwB3gdBc0rpbmxoB0f1Q7hleahNIPCUB5l3qe-Yp2f7Z0AxEhYxjMS-EiPvB7lLHf5WbCDgW5qC0Zv-2xIb7_Eh8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d_Iilv1hkrdJEPOm7rkiXtbl2jZuvfpWbX-0N3g1pdqX6yfE3VmYeIR7uWKsg5nHs3j5TN-DKLWM2oBCQKeMP4DrECY03TV8Qs9AFUsAq_DaaZHXsMP3sB31MNgMONoZKLq4MuTYP8yS6XwS-5LVbFKqrMJYbjdH4ge99dVO-AUsOLzuWjN6aYTI5l7vy78UtYt-4ekGJ9X52-0BxqFdRIG1HQzDyWZ-Wq25Nc6Zv86wl-JtXwqgcoINpzjh7J3vvKFjG4j1YXQQC5ZMqNIX4QhLYDd6VUsE13-BZMOl58A320FOmPbUeIfKMNEaoj08xKsUq_R62L95YYJtZXdLiQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
رکورد داران بیشترین تعداد بازی در دربی و رکورد داران بیشترین تعدادبازی بدون شکست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/28906" target="_blank">📅 13:29 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28905">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jnr7Itq07aj0OHSMiPXU6fR2-8peLgEYdekmk2hvlNuLxAGoF5-FPmWehFuIuqtaT58AVsUY8EMd3HJBeVihm8OsQlqs5LqDIsshbmpSsSmJUXViKFDUMDqocQRpFUzNvUQGjazFkLTbVWnfKomJJK00INNnStZ3LwS9NfSmmfoLZ-wuF86te5vvKBky6f06lmIomryfC6aKfstpTSKvGmZhlwekc7mNYNrH5_ZcF8BrRPLGY90If2imkgVUuq9VojlBoYpmqCe3X5N_yN15q5xBY-tfyH9O1NFFn5LH7JECx3yVp_xGtjbgaxS9HDIBg0dUXUxFpz2NW5NCklVXaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکرین شات بگیرید و نتیجه دیدار حساس امشب دو تیم استقلال
🆚
پرسپولیس رو پیش بینی کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/28905" target="_blank">📅 13:29 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28904">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VUdcY7O0-E6h_Ip-d8Dh686uQaMu3hFJg4fPgDCZaWHrBh5AsRopbqPk0SJD-GidrLoV7LUAIX6yv3JWwwM8SECOQaIDRPsO8m370jcp0vG0I5lF7eGBvIL8u2wPbkYIHXuHjFawQ-nYf8imTI5ZsGxYPdXOrGBGM6SqOfHGHUDTanEFHIf2BLbxB6yDSScDeOMtQKCQ8KKPYSWiuUSfqnXgGgVLe2rVrZJI5it2Vf4FfRSWJH_O2pbcwUS5NIfRZy6B0D1_YvtO2VoRpKa4pz7AQl9xWZTsBjkJ3PPhlymchQ3ZF0ZSwL2_O_Mqhe2ALk6B-tK3_cWn911u59gNCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
نتیجه دربی رو پیش بینی کن !
استقلال
🔵
—  پرسپولیس
🔴
🚨
۵۰۰ دلار جایزه + ۱ گیگ اینترنت یک‌ماهه برای همه پیش‌بینی‌های صحیح
نتیجه بازی را تا قبل از شروع مسابقه ثبت کن.
🏆
مبلغ ۵۰۰ دلار بین برندگان تقسیم می‌شود.
🟨
هر برنده یک گیگ اینترنت یک‌ماهه هم دریافت می‌کند.
🎁
جوایز به‌صورت
FreeBet
پرداخت می‌شود.
👇
ثبت پیش‌بینی در ربات بتگرام :
https://t.me/betegram_bot?start=p12_r4EF37DCE</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/28904" target="_blank">📅 13:29 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28903">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mVJn8rRtcrDYroXQD3niJAO4J5fjz5xKzuGMMVINLjpdVuyAZNNMbjwPN_3H15GJfWm_XEK2oXWY9YzsA05o433q3uf6XvavudjCrfLgZB0xRSjTjAosAeV-B4weei-z6AwRMFnd4zZG92ZN1k6w5KVAW82PMhbGzvlpBSWh5bLGMLj59kEZcwESzexqR6GDH3EVZnbaE8eAsyev71Xt7vElD-z-zyHFr73iL6yavgVnDLQxCdCKR_gJFFvWWdlyGUIhKwcYuvBXWUQhVo4uwhv9pdoRy0lQoLoEla5VK9XrIgBykFJO8YufcxVXxM_fssPya2pLrAzRMjtPWrdu5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
از ۶ روز پیش که همتی گفت ارز به اندازه کافی داریم و توبازارمیریزم. ۱۷ هزارتومن رفته روی دلار.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/28903" target="_blank">📅 13:00 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28902">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c042e7e205.mp4?token=nRdESWWqfE_zNBO2Kx96MbVVwxzqF6sU9HtwplqLp3DBJwSEi0biiw2oaA11cDsj07x9_M7AKoq3soMDlK1UsiCCaixzpMCdgW4_Fk1vcK1mCIy7pawT2x7nVVXi7TOBM18PTUvJfCVZDx1xHmpSKepGuFCxEEamqLzu4lK7ll5aETydheeN87CuDdvHdX04swdfXfTHuYhJf1oQK88CRH4bQAjAh0IiViVTFeLH1WYHRFCYfRtts7VkVDu-Be4ljzhE7ubG_Uybgj5BhAyQOhuxiVPF-7nIQJki3iG2E1AFTjqAyfsn2Hi7pVASFb3EDeUGEKVlZDQdPGhPCtMmgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c042e7e205.mp4?token=nRdESWWqfE_zNBO2Kx96MbVVwxzqF6sU9HtwplqLp3DBJwSEi0biiw2oaA11cDsj07x9_M7AKoq3soMDlK1UsiCCaixzpMCdgW4_Fk1vcK1mCIy7pawT2x7nVVXi7TOBM18PTUvJfCVZDx1xHmpSKepGuFCxEEamqLzu4lK7ll5aETydheeN87CuDdvHdX04swdfXfTHuYhJf1oQK88CRH4bQAjAh0IiViVTFeLH1WYHRFCYfRtts7VkVDu-Be4ljzhE7ubG_Uybgj5BhAyQOhuxiVPF-7nIQJki3iG2E1AFTjqAyfsn2Hi7pVASFb3EDeUGEKVlZDQdPGhPCtMmgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکرین شات بگیرید و نتیجه دیدار حساس امشب دو تیم استقلال
🆚
پرسپولیس رو پیش بینی کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/28902" target="_blank">📅 12:45 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28901">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R3B51QQVgiNV8lsBdm7tchB5C4AqjuInXKU5FfpxDEIKAysS2pktXzPa3Z2y4IuyyFt4xnkTY1BFpFXxDs7xTv7leHyr1uByISASEClxfgeBfjpKUzqzkCOrCfOnxBxahLsvnPil6TcpiQ3z3gbS9IhB9BuP5b90Gff9JU4qKil3f-XeMKxXKBOSY2P5o4zZKmopxgPMWmjNRXlHJJkr9oOkhMH4wM6xLsaewiInja6nPNHcVsPYDN2i17K0IUh5TQwQWI3-XbNHk6LiCj9MWDvvt_DPQHvU9DvbD7SRxBeHLsQ2E15Rm7BbH-cLOcCCzok_TaO6jGoRgS9jVUzO0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
گرانقیمت‌ترین‌انتقال‌های‌تاریخ‌فوتبال‌جهان؛ نیمار جونیور همچنان در صدر جدول؛ انزو اومد پنجم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/28901" target="_blank">📅 12:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28900">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eAdtol_o105m8629JyffgL67mxfPx3TcfB45TshkWpYiOlTyz9_fQzBTuI3jPw_vt-9Xwmz1gMqRlWVUS6khj2rtMm_CJHX_WMdZQnjHSRGLPERLiRfx6Vel3xOQ2p0_8gOeRd_i2rHzXMez8j_vpTLBeyS4fl4spWgvgxTWLx7DSCbXD9GYS1TYPCcP0W7hmIRNw5f-ssB5nuCA4JHqly4_GTcpt-6BGcqvyruhMjXqWomoZcU4QwXiduZnTuLoVVQYLWWwkq4bvZbNmKFU0PXGZSE4yNSQYa2EtczdznFrCiyIMhzTJV-Qp0Zv7tc8yX00XsmmLfjaae85qGfu7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست‌گرانقیمت‌ترین‌بازیکنان‌لیگ عراق اعلام شد که شرزود تمیروف مهاجم ازبکی‌سابق پرسپولیس با دریافت سالانه 1.2 میلیون یورو به گرانقیمت ترین بازیکن حال حاضر لیگ برتر عراق تبدیل شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/28900" target="_blank">📅 11:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28898">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PH_pYZaEaGXG5N-2Bv3wFtZa7qhym0BEJtiYp7luXUabby7iL35NFg45kGYtCYb3JxLVbg0j8lAyL8oke52jj8mFIciKLd0h3v6L5H3YUI-AZdyrDe9dQRg6k9faSIxhbZ9yVakTCQdz_UqD1VJ42pqFroJTRW0zYz56YQm39Z8pSyd26OJLz3Fsew0dQhnyKtEXmFAeG4hiNSa2KiWBbSGTvUe7WokFVKafkoOvq8Gp2SjLKpI5qYm5IuqvGIqhAFx8bT1WFqnb8kt3dhCU-Fw5o3ZOUxihgacqXtLGVlG7ndXftps54WNWoiTw2Bk2sy5GaXMhz2hgquuGbpDtBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a48b60637.mp4?token=QcQK6ilBMEVjWd3ELCMCZ-ZsktaXUsm8l33I_4l8Fe0GwRqaOSYGIbHDWIHT6FB2eaba2NCr8oMPJLttdeJdoLQQQ1ou8tSJZpn3sLQyrbmqi7x3UCeM9O8fajB60EzGbAAxjBf26ZC8dvAzWYlq-XVgTBYbuz8RHuyvwVpgNPR5-p7OO9TKQJSyD8BBpfglu_j3zYVrffIcSi2D8U8Pq1hAYpH98-iymtYCh9tmri0eM1-O_RtPWQeY8mO4aEfKztwvD_afws5EfFG9dVPybum08xOUEUfxsDmDaeSFF7nfvIkj1Y2uptbhnHRlYhh9-_bOTmb0_hDwTxqu2M9BFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a48b60637.mp4?token=QcQK6ilBMEVjWd3ELCMCZ-ZsktaXUsm8l33I_4l8Fe0GwRqaOSYGIbHDWIHT6FB2eaba2NCr8oMPJLttdeJdoLQQQ1ou8tSJZpn3sLQyrbmqi7x3UCeM9O8fajB60EzGbAAxjBf26ZC8dvAzWYlq-XVgTBYbuz8RHuyvwVpgNPR5-p7OO9TKQJSyD8BBpfglu_j3zYVrffIcSi2D8U8Pq1hAYpH98-iymtYCh9tmri0eM1-O_RtPWQeY8mO4aEfKztwvD_afws5EfFG9dVPybum08xOUEUfxsDmDaeSFF7nfvIkj1Y2uptbhnHRlYhh9-_bOTmb0_hDwTxqu2M9BFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
نظرت راجب آلوارز چیه؟ لامین یامال: ما دیشب ثابت کردیم که نیازی به مهاجم نوک نداریم و همین ترکیب برای دست یافتن به UCL کافیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/28898" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28897">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mfbWYz_xnPSKpb_Bhpgf-RxsvCVHP9izEMmLSluQmoAGnbeldoPw6qJmNq1Asy-MZ3GNv3qEjkkZ493SICBg_E81RTGcgacHnRpqTPJnyWwoT7QwTsrUvwrsAiJ8gcZmm5UzxWlbdBFB5asG-gIAF6pIJABNt1OOvc-1VbsHiHc_A9hmV-u_VhFYyVBdS-cPoS_tVl_OVcHXN4-0Zf1i6kyVtPiW5m5nt9DEMU1CHtEzDTwlWmDFPO9TBeLIirWf2sNSrrFTXqiChjVe6k3GU3v5IFb5twuDbm6U6_UgqqObDbBv1XzxffAhGluwpUim5AbNckqgm13NPzT4a1Tp3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ درصورتیکه‌باشگاه استقلال این هفته با عزیز گانیف ستاره خط میانی ازبکستان قرارداد امضا کنه بازگشت داکنز نازون به جمع آبی‌‌ها منتفی میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/28897" target="_blank">📅 11:11 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28896">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fwOwmXlnhs1oy5OE4X8EwRWaV6mRp9T-J_CzgCnmU2F0Ue2JOn9z1hyAG4WXfAJ1OnzF-a_Abv86-1a9vV7uCUqB6Wsji6ySE7_uot9dejgG7HHojx5-usIdZ-INfEVFXxttnFxt1tKTh6KRM03MlhwdLiho6G3m9yREQ_xQzKUyhN7Jf9EAuKiYbJNySIAsnoJItYURyHtl-bx7VJzhbpznG7FRFGOdZ_QBX6ALVpbNv5fXqf9_Ahe6ZLqZKYQO8wmb2joBKLOZLxXag59jGinUmohgoSzIQkxdjdTha7yvQte0CCK3OVd26aqiCFbYnlpX6l1HLzwX2rHhahLP_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
دو شماتیک ترکیب احتمالی از استقلال و پرسپولیس که به احتمال فراوان فردا کادر فنی دو تیم با ترکیب‌ها به میدان خواهند رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/28896" target="_blank">📅 11:00 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28894">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ekUvmUmoXJje6BF0QPINMXO4b81rMFisCg742fEq-wtjun8d82orsoHe6xyIh07vnB6tuPT9iwIfmR4I2-clwOsqyUM99P2v7hOMWXX_cD3cooI1WfHciWpKB-R2vUio63Ck9PQ2ov4xoMKStt8kzdkfMWSibVKn-oeYqhn-aJvKFyjM-3ZTrptzaBlu3O7BfGP9ety8xNTMioEcDp2ABJjuNLbDnHxbeSsTKncBkngAOoUsC2mvBcVD7qnZbj-ap270jZoOsND6yCeHXeTswFTpqdBZL3_ttrqHJt2VzDHb8A4R_YTN01ZwS9mr03A9ys1Y_40yER7kB59hqzASoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DtsCVx9moxWWHwrDVS3IG87eYHFvyH2cdEhbkwdl8PRd1WV57q6IwI2CH__sbQei96mAvgsXHGy5ss8-rgw6UflGnXUJbmS7meY8qeDlgeMzOTweaW7gwkhp3BKOXvTgj0VKLCfXjcHTxs95d3a_9UaV4JCZlGYVP9KXhUDxo5GzNvNFHiJXHunlO-U9GiRonl254htAiLVeKnhRFVVMXR-d0OALXbqE1_YLQbmhs7G2gGTn3pUg3QyB__6XcMhQL1JxrPGaD7nJ2SIwVYwi3uZDWOvDG9g_hcRv92bJWpv-PsRW3v1VOH1KibmXrky-knaNAHThFB99AdT4gPISZQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
ترکیب احتمالی پرسپولیس برای دیدار حساس فردا مقابل تیم استقلال در هفته پنجم لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/28894" target="_blank">📅 03:07 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28892">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n1tUWmZN6WOQSPzHvHo93WmWZ7rXdAxpkyxESwa8fc5pgrukGhRyM1USBrRLkPNdOlsXVuXzdgqRnmkbtL3thO3ZN10OSgr9z_6Z45G7sJLgV5Trf6mH82vwrsaOlo3E0nYOXp1ciHIqjxHEmCoy029p710vMLDEHb1dXFcSB_E8TZAEQXaHCSwsCy_yUrFeKn3EJs0OOZmws-xJP5dQX1EqxgOlhTsxnK2rmhlba_BWy2xf4Vuxc5RVh71PpS9EVw8CIOvmc5pM_qpGE6NrtbR8I2s-nc-f1eWUMAxnxz9ujXr5-QiC8BpmIFH0m63Yuau-bHScD6dO9oPhu_2_ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
#فوری؛ با اعلام رومانو؛ انزو فرناندز ستاره آرژانتینی چلسی با عقدقراردادی تا سال 2032 رسما به منچسترسیتی پیوست. سران سیتی 125 میلیون پوند برای جذب انزو به چلسی پرداخت کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/28892" target="_blank">📅 02:48 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28891">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbfb2092e5.mp4?token=Yz_w1Jdh9tFBjI_lFC4dDZJM73l73_65sYC5h73_nmyNuy22eU2RF1Buhem91PapMxcKDLsFatZ9DfYkykEJpugp_raVwfJVWmHOYeZMsuKhIoNO4-qu96oNNAqIPTglfOZ-e5w1QjD0crn4GTo6lHe8X20J2RaS2TiaswgTdO1apbpbOntB1dZrYglyqqPkawg-SaY2LQ5LVCYfJmmOl7m0VMh-ufhljKZfveDLwohNc1bgwRQX3EKk0zF5xvVIN5vn312nKlQ7OGYu5Jyy8S9nHWklNq_vdGv6U0ffk918-Qkm-Nfd6oRJo0AHosyrTam5RP4ejOEjfWno0q4iDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbfb2092e5.mp4?token=Yz_w1Jdh9tFBjI_lFC4dDZJM73l73_65sYC5h73_nmyNuy22eU2RF1Buhem91PapMxcKDLsFatZ9DfYkykEJpugp_raVwfJVWmHOYeZMsuKhIoNO4-qu96oNNAqIPTglfOZ-e5w1QjD0crn4GTo6lHe8X20J2RaS2TiaswgTdO1apbpbOntB1dZrYglyqqPkawg-SaY2LQ5LVCYfJmmOl7m0VMh-ufhljKZfveDLwohNc1bgwRQX3EKk0zF5xvVIN5vn312nKlQ7OGYu5Jyy8S9nHWklNq_vdGv6U0ffk918-Qkm-Nfd6oRJo0AHosyrTam5RP4ejOEjfWno0q4iDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
محمد نوری استاد جملات قصار!
شاهکار جدید ایشون درنشست‌خبری قبل از بازی فردا با سپاهان!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/28891" target="_blank">📅 01:09 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28890">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VXJtfX4NGMm2Lb6BpkScU_SK6mkBuq7iSrUDuJj_RMgsoJwGfRq_vaz6GZlo489EbgxoauO8knzGtviXnqDG0Umof1dRukYBX8dBVBb09MNwl1wZ5A69AKMatAvfE2BHVfK9uS2qbpq7wrGfpDEPmyVpHwQeoiU42v2IimSRd5QMyBK-FClTiwEGw4hQn23bArr-Kjz6rCgBB-BwzDW3PFwgMnnBmIabGl_zCz2WsZy813l7ZY_yLj-ocCo5nZK45fz2Czr6mbIqMga45K19F0IhjLOGZnSMExfCbRzXPvBlJdhUX-UGRgE1eXwB5A7tgWWoi8CIZkyH0nJSMOrUVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌‌امروز
؛ دربی شماره 107 با جدال حساس استقلال و پرسپولیس در شهر اصفهان!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/28890" target="_blank">📅 00:50 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28889">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GT0hBqdIPZu31sSYqmGHWBDPXWIVa3pgWZrxyMcWeECCL3RZr2Kzze4m2eAOGZI7bpgrjfhNVLGiW9XjaTyIP2fmmnMkpvMPfqJ9SKqVCaFQR27OcFLtR6G3ongT6VNm1fZLx8OkZs8uNcp6XZvrbpPeb7Y4tJXlVOMYUE5CD-cy15oeMeRcAR-Oi862CeN4W-EW2VrLznC5tBRSTt5-zOKzohF0DvmJw4aDdjlqxJeag-oDBBKRCCwetbZIbEIWrBweIccuKWBe5NzSPcDt-37W_XTPQMpU096nVZagzjUbaZ0oIr3ijA3uu3gR0eCihHaspIzlIO3uIpNUoWFcbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌ دیدار های‌‌‌ دیروز؛
ادامه روند بسته‌ ماندن دروازه تراکتور در این فصل و برد قاطع الهلالی‌ها در شب گلزنی تازه‌واردها؛ واتکینز نیومده گلزنی کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/28889" target="_blank">📅 00:50 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28888">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h4s9xt-Rf_SPR7UxgwclfmCnRmpRbQPc41vlkBrRkmB25mV9fZfVAsrh8N28UJPpQySV7qW_URoY-BBUsWgHJzfo0-rzZQgs610ncD3Ouz42WkgqAO-SIKgcTRmRyxnuzatQ1zS-4aqIvybb-cDxdUPczTTx6NsyKFQBmcrY540jFecHOy8Xgk7cY2cng9Z9z3LyIGjURaEKpD1F4CW6pSit09DSJWq-6PxwyTF-9fxw-0Kc8NCj6jszVb1RCPN8GNkufmGuXV446ZkxiOp_T0JKwK783eJGo5DK7Z4UlxznsZpORekUmPDgMvMEFYhm5hCDFS2iGMbB73s097aoxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
بعداز دست‌دادن‌فصل توسط ترابی؛ شهریار مغانلو و امیرحسین حسین‌زاده دو ستاره پرشورها در حاشیه دیدار امروز با شمس آذر نیز مصدوم شدند و میزان دقیق دوری آن‌ها از میادین مشخص نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/28888" target="_blank">📅 00:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28887">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NDSH5hh5lj91T51XNvuEM3mkefq9BfE2EFJtuGYw7lf5M-m-sDM531TBxGwZTov5hSzxODgxR9R5T7C5wiuNTBAbDsXpV--vgWD7neKsl5bguaQk9HcUCfMA_amniHRAPgkDIu5TogJimNZycEsjE2SZlw1poFOFAnaxDXG6jOrz6wxwr96ODkMLHgnp84xV69_cOGFzdubQnhusAjjpKkv5pOGm09qMQeky1Q5EjTAiv0WKjqvMVIFIAxGCyTveecYuLehCZPw2J9JJrTc9K9ZBC_z5IO2J0CrvJ6fN9FFtph5NTLgrsMZ3okdMRiM4WYxoxYRb0H1Zjx7WrzKYrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
#فوری؛ با اعلام رومانو؛ انزو فرناندز ستاره آرژانتینی چلسی با عقدقراردادی تا سال 2032 رسما به منچسترسیتی پیوست. سران سیتی 125 میلیون پوند برای جذب انزو به چلسی پرداخت کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/28887" target="_blank">📅 00:06 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28886">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rSLQ4Hr-Gz9b1vPMzbM7RsB6rEKtSzzFrDuhETM2Kc59ri3eSncVmy1q5cVvvchYV--HSCkgXFiGD_reveodp60x2xHysiYn91LtUpBl_31nA6jKAt8OGUBOkMCDfkboXHCW4EGQjGQ5-F63o17FXHtPjZIJPP4dmU4_07gpjdibKNlEcduONywhBdoBH7kww8RLSwRDrYmGNrYYeM9JVMtLEBpkYqiSEokSvlKbrCP9rLocCdGPzxxd4JaKm0HL6EO_ZcPv-FBicApw4I3K_pxTXtmx-JBD3nWXHR-jZpLrTz18sTt3DF8FNQlwA_ZZT3VM0zi868YCN7hcfu6nPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
لامین کامارا هافبک دفاعی 22 ساله موناکو با عقدقراردادی‌بلندمدت به‌چلسی پیوست. آبی‌های لندن برای این انتقال 65 میلیون یورو هزینه کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/28886" target="_blank">📅 23:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28885">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kAsApR-SJKaQlkswQpuLBscqFz7vcxZSYOHaiMXLKClZSSizYg75D4QjGzQxUsXwbHWbQEGA2UheAoroSGTyPQek51aKQMGEzDltbbP4GhC5oTelNrwQsmiQzk0pWaPl_i6_P7WteDgzicw16z-x-FGRUags2i3AFIYXI8aGOlJ_WpzWdZmtiv8Tq9AtXfroGHIvSAk-_31k1k6UiYCm8lRWSVctIl-n4r0L0WfCn7vlC5BPI2FvLpg1h4O6mfGw8fWKzym4F_RPSYBv2N_WsDzXyjyiLbXT3Y53KRMU3V9_gKx2lE2EllR6Y0x9JSFb71vZUzrNrMvxxUupM1dNrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
شماره "9" های بارسلونا از فصل 2004 تا کنون؛ گابریل ژسوس صاحب جدید شماره 9 آبی اناری‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/28885" target="_blank">📅 23:45 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28884">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H51Swddiuc-ExLfVIOk-hPmHxkfAW8vYjA_K91wPyeqT8pdbm50M_7V-GjXR00WJTQRuki_yj-8B5-yX9ORi5GlZltQ6vy-t_I2hqZiS1gz1oafdbAEEm2CykN_pmDWbMcRWsN0wBOG5i0MZQcTu2brnwh7isLnNfqGVTFFP-25NLh1wzYtiYrfII4l7iTFRPCL95RH_UmLQ76v9_Lb7Jfjgq8PQ-r_e_wAYO3pKjeprptn3cffB04qXQXloeXzSs6mVRbruOR93TJ99mz8TouFt7ZanbkcAMlHzyudJfBcGuQroXnLib9fC_4_d1_MxcbstUgWHsyel8wokr-VS2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب احتمالی پرسپولیس برای دیدار حساس فردا مقابل تیم استقلال در هفته پنجم لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/28884" target="_blank">📅 23:22 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28883">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QTyQ45MWuEb1tqfs51OK1Ko8FZBTlIMjj5-L2_CsGbQCWhQ9pHIo6PYPv8KdAhUodi62yPLI5C7NWPi2Vw2iEoWrE0y1kyobUi3IeGuU6g548AsdlomsteXn3yvX4xJ6oKbCA_G4zzLsjU_QruYgaHNpVE6FWQlpi29sEf637bF9n4Mc9D_bq1IJO-nKEqh-z5851Vjtdoe6_CjJeF-aegUkvU1JwY_t0jJjD8zgEFI8WHvkRuYzzWZfbIkx_9CBLtNOyE0NVMEq1Umt1oo9P2AUep0A2_ZjosJuT-SUZh6w-wI7W4E_FyVAMhf9N8zzl-qeO_0-YHS6Y26f4xkfMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
#فوری؛ با اعلام رومانو؛ انزو فرناندز ستاره آرژانتینی چلسی با عقدقراردادی تا سال 2032 رسما به منچسترسیتی پیوست. سران سیتی 125 میلیون پوند برای جذب انزو به چلسی پرداخت کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/28883" target="_blank">📅 22:46 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28882">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d1C8lrGBI6TYzONg72LO-zwhTqzHcfZIPkT08VLbSVzwgkMcQlXdJO6MidlbUscq1S6wU9-V3F5c0_ZGlLRBRHgpTq5sB5PSUhVwnoz2ncVLoegU7rw6Tu5Aq6TfKxIVI45CHMm5YAImbKQKjE2fJeR_2_BBt6GKummJes-rlsAKthskdfn9mP0O5LCutWcR9aB65nmyrHogld_2UY3y5vPUL1BoKuTGht1i6HnnBR68AxP6gxEJPTE6no6T2mmhxaKUeFgnffY2FAIArIMcLjFXHltm7PyixffpzhqOV6MQJO-4_BqnbDLSZ7ck2LRPoVhXxQreiPEuezUgliVxzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
به‌مناسبت‌مسابقه فردا؛
10 گلزن برتر تاریخ دربی تهران؛ علی‌علیپور تنها بازیکنی از این لیست که همچنان شانس گلزنی مجدد در این دیدار را دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/28882" target="_blank">📅 22:35 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28881">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DUE8DMaJRFPeECS-E6uQN5mJBtNnmwsj2KLxYoASiUwuHlrH4AR6c7UKc7m8GcgWKxjevcChesgfHbHGfTJ3sR4h1sYEwQpwjNNiQHvWanHbw75i3cJWeYOy_SFxEHCINxCQle_m3jff2DjIQpf1bjoLYb6TrMNvUTjFgqof5e1KS6HW7CaWgOFIHXOhffdWgm1TX0Ow1WuZh7TGSJD_gNk2SYvCy1Wz-Qeapkk2QwW2mcCplR-JEPPs__68D1Z0kD5ImKK3jWrtqWSbCbAUgkIAByOCXZshe6KbtR4iMh8I4HIYdFkNIj-Q5F1ZRMdH3f8MBVOvDyu2An9UUEFPSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌پنجم‌لیگ‌برتر؛ توقف شاگردان جواد نکونام  مقابل نماینده قزوین ایستگاه پنجم به کام بقیه رقبا.
🟢
شمس آذر
0️⃣
-
0️⃣
تراکتور
🔴
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/28881" target="_blank">📅 22:01 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28880">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b85bfda8fc.mp4?token=SzZFBrDbLObfunmFMNF5xQes0q86pxXEsA6GvufF6Ke_q6KrZ2Z7jehO1GSS-loaghvjIRxIkurDiaSHX51NQrOtvubFOFdDJl6SyO8A-VTnHdJWpibRuFYqdTuRA4dOiWkhO3MzyAcBEpTDfkj57yQ8KqwJWlvQtHcVBjRxEVGDenmXauxTNxqdne6FlVg_F0BKFTVJ1J7EpkzpavBl-slP8xXP9mt4nR1fpE5JXj5KBMOI7evlqRuH0xlzJD_Ro2yHM5TiJRs1hBdHPnci1KBC0Eawl2mnCJHKHIPIEYzj4nE3A_lAoNSt-9kY0jbPVkv7iH0-ok-KTLbNZb0lOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b85bfda8fc.mp4?token=SzZFBrDbLObfunmFMNF5xQes0q86pxXEsA6GvufF6Ke_q6KrZ2Z7jehO1GSS-loaghvjIRxIkurDiaSHX51NQrOtvubFOFdDJl6SyO8A-VTnHdJWpibRuFYqdTuRA4dOiWkhO3MzyAcBEpTDfkj57yQ8KqwJWlvQtHcVBjRxEVGDenmXauxTNxqdne6FlVg_F0BKFTVJ1J7EpkzpavBl-slP8xXP9mt4nR1fpE5JXj5KBMOI7evlqRuH0xlzJD_Ro2yHM5TiJRs1hBdHPnci1KBC0Eawl2mnCJHKHIPIEYzj4nE3A_lAoNSt-9kY0jbPVkv7iH0-ok-KTLbNZb0lOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
الان رونبینیدکه بازیکنانِ ایتالیایی عرضه‌ی صعود به جام جهانی هم ندارن، یه زمانی وقتی می‌خواستی مقابلِ این‌تیم‌بازی‌کنی تنهاتاکتیک و راهت دعا کردن و کمک خواستن‌ازخدابود! به معنای‌واقعی‌رقباشون برای سلامتی ورزش میکردند. این ویدیو رو حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/28880" target="_blank">📅 21:50 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28879">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LLk9zRugmvhk5ZggyPgOGyDOcD4IZPex7z8w9_01daxGHQLuy5zIV3BNJb5zmNLN1W9-Fm3aIUpQWrWcQedSErHyMK7LnMfuaqxdIeUaq6Pyg01QGNJvPZLTJEo88W7oTi2ZMupIAsqiS-mtp0s2uAtjnTDyZ7lCn_h6kkT-CJ0tTHZ0HlERtAitH0Vemuc49Y6Zx-HeMmJJ6piKSVhpz3g4ho-dHdk9PvbeKzsp68nPup9oGKQL9s-TVESzesOgTQ0xIhexV_In8JLMoI9luLa0j2Z6wuKsTe16QqUXkseQ-FAkxbzt9Gr-qYSa6MjUajSUVcQaZURjul-4VN9wXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
به‌ درخواست ژوزه‌ مورینیو؛ باشگاه رئال مادرید قرارداد دنی‌سبایوس رو رسما فسخ‌ کرد و این بازیکن بعد از چند فصل حضور در این تیم جدا شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/28879" target="_blank">📅 21:25 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28878">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y2IKwlH9wZMQzd7w6zRZfD3kTOT51cPClDzCWr8oDOVqIpG3uvJh5UA0U2qlyfOfiY9Z8RtzWBE9MfG-9ZyiWPqUh_zGB9IFORBSzYntj2xuPdNXQrRHow8OsKAGb6Yrt2DUshVr-_LTZaNL5JazBhOJTL1s7cLc3A4vd8SFvUJxIcePRsUMwCQZRwUuz2WD01BdNMFKf8y1cRcyBXrL9qqnZ0dsk2uTW6ustFKg5g7HhNr4f0T5BTOSZeR0UrmJXKxjVJHcbY0cSefo0jNTaI2Tr3-j6bJJHpf6cb0NDTyJwNFa-vXoCVFx9Ve2bFScBglXi4f8FX7pnvpf2oVL_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌پنجم‌لیگ‌برتر
؛ توقف شاگردان جواد نکونام  مقابل نماینده قزوین ایستگاه پنجم به کام بقیه رقبا.
🟢
شمس آذر
0️⃣
-
0️⃣
تراکتور
🔴
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/28878" target="_blank">📅 21:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28877">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af26bce4b8.mp4?token=p97M5bVabFTNcDdGxG1e7DygCukycdvZ8GhOSRP_86yFYQ5AMvQqSWEyDm4wuGAykx2nC12jF8424F4X92mvntgPpvuGI6tBX8B5HzYQuMBSP8XwXft8NLPlXwit-p8GVTaqqzYsVuY5H-zk10rfM3TTYYZCD3IStNDcUMpEXdUK5BMijk_sbi8iJRHvd3Pz7wZN8mZdWrIMiFgvlEuykj_mxKpyFvWeHnk_orytid2COMkzYDrkXvLwnyMQ7usDr44OXm33aGB12kRfBKniKSENDT8OgB51LHGLyNVRknxt_qRfpH4pltXghxa0Gx63wsczuIGClNRhfmrrP-ktLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af26bce4b8.mp4?token=p97M5bVabFTNcDdGxG1e7DygCukycdvZ8GhOSRP_86yFYQ5AMvQqSWEyDm4wuGAykx2nC12jF8424F4X92mvntgPpvuGI6tBX8B5HzYQuMBSP8XwXft8NLPlXwit-p8GVTaqqzYsVuY5H-zk10rfM3TTYYZCD3IStNDcUMpEXdUK5BMijk_sbi8iJRHvd3Pz7wZN8mZdWrIMiFgvlEuykj_mxKpyFvWeHnk_orytid2COMkzYDrkXvLwnyMQ7usDr44OXm33aGB12kRfBKniKSENDT8OgB51LHGLyNVRknxt_qRfpH4pltXghxa0Gx63wsczuIGClNRhfmrrP-ktLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ نشریه‌‌بیلد: هکتور فورت برای پیوستن به‌‌‌بورسیا دورتموند به توافق رسیده بود اما مخااالفت پارتنر فورت برای زندگی در آلمان باعث شد که ستاره جوان بارساییا قید حضور در دورتموند رو بزنه و با قراردادی سه ساله به تیم رئال سوسیداد بپیونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/28877" target="_blank">📅 21:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28875">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v5cG0_N65X45KsweOjdiF3b589QBiZFVkH-wxC5jkJ_bbvhtyyGWh2lOBOvurV7IMCNAcSKd9e8DFCcp96k6lZRgQCYwVIQVVliSu_9IsMZmvxukZG7vnkhVz52WIKoMic2fHBiq5VZgSh6TqBNKl9C5sEvpL1211PlnkSdnppLUmLcX5Ue0QEmXBQWDzup_6gC5ycTBVnInP0BsuzvPyAr4xK3L-wU2iz5jVp8aOTmC_axNHW_2q3q_vHHvbDJakCWNVtNkeR5Ukrn4jOihJv7_WcnWI5vNlwBENIkuwfYeB1Xwv7XwHg3F-M8XH6mwYtmZ0z6sRPFgil8LmV5N8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
انگار نه انگار فردابزرگترین‌بازی باشگاهی ایران قراره برگزار بشه. نه تو مدیا، نه کف خیابون نه بین مردم‌هیچ‌اثری‌ازدربی‌نیست. خیلی‌ها حتی نمیدونن فردا بازیه. مسابقه‌ای که از چند وقت قبل از سوت آغازش سوژه اجتماعی بود الان رنگ و بویی نداره. فوتبال، استقلال و…</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/28875" target="_blank">📅 20:39 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28874">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ofZWVfdaXXhNe5WC_bpnTraKoUcFuL8VLWIeC900zOo7Dp-_Aaah3T8TkZ_jiBdApImUO8DymOUTTqO8P3vM6XOhc64IawMgKyqs0UCj3spe91yH7emgPFN2vNMaWdNySC9dF3e8sdoOHgF9Qq4LjgG6nytOVP54ObEsBv2ipbh2n_f5I3FB18QuF3pSqY8ACk6CT0mEUdxLJLBWmz6hQpO3xhInfVNCfbfRjldbRpc87L1CAH57id6GHFAoPefQRWALk5nzAIKzOSdZvIRZogMUNh3sRuXb2fKEdyQgQb9TsDj_JQAIPQFX2RY11LTs4oE5pt5wPypI3nkkk6dlxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
خبرنگا رسمی باشگاه چلسی که گفته مطمئن هستم با ژابی آلونسو قهرمان لیگ برتر میشیم.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/28874" target="_blank">📅 20:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28873">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O_wm_H06DnVoLgFDngxwJbRJHubVq7LjtpEU29NEdVAymNijFn9T3pi52KT51X10p0hYN5DVquzQQ3R8GK6-QCMwVLs0hJQQbG4dft7ZsYVSAhuFXpDMQUvc_JfLCbwh-iuj40vFPcKmD-W5v4eG3N76Uaks9oWKjqXHT9NUh0OkY0QiK0jLNsiIO6G3mCAw50z-Sgo_Q0qD35YGnAyu7k19L_lxNMhZTdGLpKiViuZSn7SuZFUr--WmWRj0peDqFay7TCFec7N6O9LpVBfUwKaY6JOjdUuDCSFP6Jx_CuNQkB6DDrq57wYgs8-gyzVz3s54xluvTKMYSQ03WfwxaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
بااعلام‌باشگاه‌بارسا؛گابریل‌ژسوس‌مهاجم 29 ساله برزیلی با قراردادی تا سال 2029 به این تیم پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/28873" target="_blank">📅 19:48 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28872">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EnBTblWEU87XdrMoN25NMMp3EW-u6V9ud_wsVPMj3FAaAQOYELuC8CVV3yEcGqBju5DWSAoEGBXPXh3zEigWR0B9s5PurLaPTVgTG3VhKlriQGQ8oRRBmnqrdQ9kAahW9PALQ-XwmawxrkIyHCxOVWhE8pWHIwW034B6ft-ghMJaEh62cVX7sgvR-3V8ggsoWRmNGyHal7TYVN6fP8zIE2kqqvqWX70V3x--hrYzRHqAt21cwuxu52lQQQ5B4N88H-SX1n-8_It90xQlg1incA3UiqENLuhVj82rbl0dh1P2mF5HECoKx-CliQ5HNBf2t_-CJ8D_AU0kJLiZEQD98w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
#تکمیلی؛ تا ساعات آینده انزو فرناندز ستاره آرژانتینی تیم‌چلسی با عقدقراردادی تا سال 2031 به منچسترسیتی خواهد پیوست. بند فسخ قرارداد انزو در منچستر سیتی 100 میلیون یورو خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/28872" target="_blank">📅 19:21 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28870">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q0YiyQRiW1lLZYZ9iDASBQ4iBNABxO1Zc7M90iHMjOaHQrKIf17nX3qAkYG8TZijIkEN1YO5ix6QlF1txWGyg6NiSI6xqVpGj5oSbxNbAzqzNyVHzPrcu0mfv_fIKkZLukO7QChFUtI4Gj5kJgAblxPztzzp7eh9EAivqI5ZjS-hK3w4dYLp9CudRbfP1T-Ml7AbWYcQ63aF4fozdC8gC4b8PQ3_GVumY_3K7WCI3Pf09HEMmI5QsD87oyJrkdMBuXfAT_esg0q6C_rHSDu-Sjr0vDifGDyEPlhlJOPgqjBet5EguOc_AHD0WL6N33GSJRgOaIYC-5ev156UAH2HJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SDBxY5G9F2BFEyFQyC5RAadCk9AfGprOhpzWZBaZiUhuy6dcvf_4eM7dNVoGkKVI3z5C97t9ia9CokVJ8lXE6b8EZvmcpm6Vz1E_s15MAMdFDj-LM84LZPeGdNnVDB6EhgdK9VErdyi64-QKuWGw67E-70G263DasSN_qLqiSCaHB4ii8KI-wtqN5Spwh7wEo8OgbPyirrzaWPtLsv7s5O2S9TbzpQtI465IDqP3f4jmeylwOCtk2PksSQH-iGE1dyZbuW71mQMgQ9wde-Et4UF2fJaH2-899wBhiLP_dMAETdokpshoVps63xgFNryh07Tw5vX0_0uEq8hXPBLu5A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📱
کاپل‌های‌ فوتبالی که رکورددار بیشترین تعداد دنبال‌کننده دراینستاگرام هستند؛ امباپه در صدر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/28870" target="_blank">📅 19:14 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28869">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ccfhxzbWLq3CUCp50y5k8N54rWkB1JfuqUCR-moF-aE_KPUifiLkLqRER1o3cAYfph9EuET7KLCOQJpbqmvzDRYYigPuXRZwonGPQ9dOLD_N6071mkMLtwOEN_X9aVRSNmoUZQHwBTKa0ekzIK8onnEr33FbrU07CP_FfqdwRu6VjJCCO3vvj2wMhxCknmH99B8iXG9UVuuyQ75xqPLwUWAhahWUx-g0eZHkhKeZR52e_Dhakg6yeDWAkVthVe5rmRSMI-5d9gQBwjLwX5Ym4_0EyuOa_GsWWSTG_alc_4Q3bgeR_VxDoyk4XIdxHcKmdS84bWYw3brVTzn2D6HzTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
دوتیم بارسلونا
🆚
رئال مادرید روز یکشنبه سوم آبان ماه ساعت 23:30 در ورزشگاه نیوکمپ اولین الکلاسیکو این فصل رو برگزار میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/28869" target="_blank">📅 18:46 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28868">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/omtmkE8J0-pUXqwBENUhsKV6DikTiF_7JUFCMrBXsbnFuSJOKcn7zwVUOOhxIeqAG2pO9YzpQ80si0RsHD-jw0AIj9FrNDsRijgYJi4jqeBzJLZLMAN1zukg8ehoXeuUv-e7qZPDaptYNsMGijpS4wvMamJgSEFhOsnuCJ-6BhRq0AGJ17a_JzSermK2phWCLWttwwR3--yDPyohbRZTWT-27LPbcU219r5E1ThBsJOsT9YgO1XafP4F21aU4OIHOMaHDlHikC6csIzlbN3BuVkT89fBzZEyDJVmqLzD4T7d6768V_oNEOqxQNcGvhm_7uC-RvFtiKRKEF8BP9XRdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇫🇷
#تقویم
؛ سال 2017 در چنین روزی؛
کیلیان‌ امباپه باعقدقراردادی قرضی همراه بابند خرید دائمی به PSG پیوست و با به ثمر رساندن 256 گل زده با اختلاف‌بعنوان‌بهترین گلزن تاریخ PSG تبدیل شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/28868" target="_blank">📅 18:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28867">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PDF0Nlh2spJNVGbuKjrhu_yQNMtQH5s1IdH9n9RAzmWefaaClBNWlORHEH9yMccGDr3F5lHV-p7rDHBbwgslLuPLV12mHRv6NPj-Y6HhPlecNDKC1cdoDMv9s1_j45B74cylFarI1BnX1o8EaL6-zJ6KMdO-7Fx4Np68b1BNjqRqWZ4zEMs6-x7ddOHV9wxf73Ubpwdv9Y4n8fyb8qkkMLCiodo-7Sr6djg0IHEu-STdD16yfszraZx45YOYqPlzONgK7Yli36McEfe1m1uNszqVtf5aIgWSBgIeb1-cW7qaGG9XlFhXJg3sRMERJhPQpazH4009H3BEp0HTNnfiDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌پنجم‌لیگ‌برتر؛
شماتیک ترکیب تراکتور برای دیدار با شمس آذر؛ ساعت 19:15 از شبکه ورزش!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/28867" target="_blank">📅 18:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28866">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fLWfIl9LN6FNh2xhxt2tDNrjU_eF_GTHbqRMFnjzfaKB4odFnRbT6XZhpn5bIHzkeLygn2nydsp0TiDMNZvo-xik5lanel-W97wKorKBXZpZIk12ZqVitomqIcRl8Lxkv9g-UnaAZdkdX2CIUvb-j2y_lflAnKaW5cBlrXSdAniiq4xkLB9V1ocvCtwYuZLVNnmBuiw3BsNL-wyKq8K4KNXetXPkFk1nfOGzxyBJyS47P57EgU3nXxzlQXkUWgeb2BjbFOdU-KuIO0rrU4Jc2QYIp8JmLmR_QhJItydrKkZptJ0Ie8Sui-CfVc5Sg2v9AhTDj1k9xZKNuIrvTrHl5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
انگار نه انگار فردابزرگترین‌بازی باشگاهی ایران قراره برگزار بشه. نه تو مدیا، نه کف خیابون نه بین مردم‌هیچ‌اثری‌ازدربی‌نیست. خیلی‌ها حتی نمیدونن فردا بازیه. مسابقه‌ای که از چند وقت قبل از سوت آغازش سوژه اجتماعی بود الان رنگ و بویی نداره. فوتبال، استقلال و…</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/28866" target="_blank">📅 18:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28865">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eqv1f40qtDlKwGB2iDZ1fQWxBkQpSA9l16xYDPrH6YwF12eZMrNlOByhmf9KpWU3U_tkZme5QkHtqiTz_WpZJW5nboRMWNVZYL-OcFlo79aHEK47zIS3HKwc-L_LxVnHvqX-Bqmq4VL-nt4ZAHFe1SRtn7mgRx2zHWLaKQ7MVUe3rpFeA6KFBrvpme9_06XrfnQMde4lUezfSLZqne1VNe1TGqbnI2cv_cD5D2z9dL09U1s98gJXL1WwBGKG8UA-JLo2QE44yru3VIQfWxaTC4NngsnHN3bucURYdo0-db42tghK-01lL-UJvE_mJ5_sXYvokgZj-dZiOFrRnL3lOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
انگار نه انگار فردابزرگترین‌بازی باشگاهی ایران قراره برگزار بشه. نه تو مدیا، نه کف خیابون نه بین مردم‌هیچ‌اثری‌ازدربی‌نیست. خیلی‌ها حتی نمیدونن فردا بازیه. مسابقه‌ای که از چند وقت قبل از سوت آغازش سوژه اجتماعی بود الان رنگ و بویی نداره. فوتبال، استقلال و پرسپولیس به بی اهمیت ترین موضوع‌بین‌مردم‌تبدیل‌شده و این‌حجم از بی‌تفاوتی قابلیت ثبت در تاریخ برای نسل‌های بعدی رو داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/28865" target="_blank">📅 17:46 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28864">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57ae770053.mp4?token=mdtq51XP5oB-DjTmTxsT8VmAXJRMytmjgVamgwJZHWhLFv3T6wOZccsd3VdSDgPmz_S-P8q650KJ-1tC7XdVVuggPZGrMPVFQcFW1bTpIWsKFKN2S2h0UDp2NBV-BBCKxknCXu2o9ETt9-SD94r0PzMpJNsVDSe9lgZrbFqcUguASenSW6ZRJnwXHQZemvy_R4MyWZm0a9yEcoEH7qJnzrHjA-AFc8fZc2WV-BzaqfpXsmbdDbksWIEa54rucMklK3ce3CazRcNwZqXPNHw1SJrFDjdLEqzR-E0jY45e6RDTgRSebvDvA78ksCpEfYCTKeLji7Ij5Sv6c2JNm7UsRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57ae770053.mp4?token=mdtq51XP5oB-DjTmTxsT8VmAXJRMytmjgVamgwJZHWhLFv3T6wOZccsd3VdSDgPmz_S-P8q650KJ-1tC7XdVVuggPZGrMPVFQcFW1bTpIWsKFKN2S2h0UDp2NBV-BBCKxknCXu2o9ETt9-SD94r0PzMpJNsVDSe9lgZrbFqcUguASenSW6ZRJnwXHQZemvy_R4MyWZm0a9yEcoEH7qJnzrHjA-AFc8fZc2WV-BzaqfpXsmbdDbksWIEa54rucMklK3ce3CazRcNwZqXPNHw1SJrFDjdLEqzR-E0jY45e6RDTgRSebvDvA78ksCpEfYCTKeLji7Ij5Sv6c2JNm7UsRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گل بخودی های فصل جدید لیگ برتر تا پیش از شروع هفته پنجم؛ هر هفته گل بخودی داشتیم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/28864" target="_blank">📅 17:19 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28863">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Miw7KK3Yh4e-YoKvdFVjcndAQnIAABKWXLcMwLMZhJyA0YnI1-_XTTKh_656OB4A3OHL3rE9t-7ODz8Hnr1vjlOqhbkMwAhn3k-epLf-2R3QyPcBHn_D7XYNVHiu_a4zA-8QrFGx4fsVqcNFIWO2QI-32QCW0vvGjW1lB8pK21WsebBZNaQQWmp4RW7SZPCttRR2Ek6du5a7sSo3CZbQwx7HwOk3tg77tf3ysI3ed9HOZNdnOS9lvqY4Z99UVDECVjMWr-UZlvTj7ZI35FXNkELL0tpmCyHZ8ukF-wODpLw-Bvgq2iEDJvwwYfnaXCSOKULAmJ5PM1KQktdzzbd38w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
بااعلام‌باشگاه‌بارسا؛گابریل‌ژسوس‌مهاجم 29 ساله برزیلی با قراردادی تا سال 2029 به این تیم پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/28863" target="_blank">📅 17:07 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28861">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U6hvOS6crR-oiQPqs7xBK9i90q6SAQzS8M4-KSsJI62ucwSER5d575N1smRZXhi-OGxeeJy4JGuHwBrU_eVE7qYayprl-wCZzVMx43I2N-9BXd6QplVQemZbZ3nYukaRFkpooY78u5fOzJKGXPiG2kA6f_PGPEXbVyEPFgtK328ZBhZ534tcmsPaqnYtMkBbFJNo2D592g9chAtEHmGTfMWa9BOYGpgch6v3gh5Ict3MdpIcsYrxivL_WgzesJRqAVRL6SML-YYCyNkgEuNKOyo17n-cbdjRjY9zIvkFULISdfr0jNf0CrjeB-R-gxakbF7Rlh9kVvaQENmK69Q5RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qnbve7qXIWZRyBSzRAPe5HLg-gxIjIMckc_X0OaKNPW-0zRW7Iiwack7qnKxfbCI6g_oNgvue1PKYHTIeN09aT2-5VXqMqmQ6WbYjZNbwPH9Ds1HZXEYsuPiATe3AQkw-UidosS3mDxi9lDLv3VLGroVxUCEjWgQtpnSF9oyDkTWGuUb6mBl4Vgg_RIF8mO5eVKXy_oaSZunxtYKKwLOGmfbq760OUjFyRiiW26KpuBOkPIlOQVEuH5sdKWBwKFPSnnh8-CR1yq1MvDkpMgghUGbRQRBkzz0R-Mc1JDLSicWuutCZN1_a3lJ3zrFvV_0DGLnbS3v1NZhskMlxT85QA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
خبرنگار رسمی باشگاه‌شباب‌الاهلی امارات هستند که از نگاه‌او سعید عزت‌اللهی بهترین بازیکن این تیمه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/28861" target="_blank">📅 16:45 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28860">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MehEFRUUzlESB3qmSEnjAiTYgrU5JJXFkeSgFCKcyADJDMif9mNje9Rovn27VHEyBxXRD5Tgt2dpc8Wo1ClQbMlrK0Mdhrn_7I1cnVJ9VOCOfjCBfoMmjJz4RtDeCWojwAZfSaV9eFZ9ISVq7u2guA3vGupDcH_lwDWV45eZxECXE4nCaEd4sTwxAeYcbCPe61Fknw9-EKG-PgNW1YNIK1EV3eqkSx5brYuP8cmrPjJIVnzVNYLJjeFPRQm3TtHTZaIeic_WPyTlBQF288wYcoCdf24hLaL_VcrQHyRMiHZRWMKrjbbexN651xEv-xHa-Jplxl6N0_uU-v6HyOMrGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ قرارداد ژسوس با بارسلونا قطعی و دو ساله توافق‌شده. سران‌بارسا10 میلیون یورو بابت این انتقال به باشگاه ارسنال پرداخت خواهد کرد. تا کنون بارسلونا 174 میلیون یورو پول رضایت نامه داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/28860" target="_blank">📅 16:22 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28859">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/duZczA0qBzkw5hHula5yGrS2-XlprpK5TRdzd-vP7bnvmYpOqeSYDRtfM0dpTEhkn5Saf1tODVsxr9K5p-XUjmVO45icSpXY7FO5Kzt194BvLU4BmY-q-NtRz1VX0uJUZyZWRPTavBh1G3PMXflXXF_1LfARYA7-G30h5a7TILvhQtvj46_vUO3nzRjLHMP895BE8dy7o7WjehS-pTBzVBsCMGYxXWhVChm5bP1zXF9-49rWuG7J5oPZIjFaMETG1uqP8ch0lI5Af974CcayO8vYqxyFkFhCOjxTU07r6TfbnaH1ZOSNaFtFSAS2fUSxwNlTYPpea3cJiqhz3T3Kkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ لژیونرهای ایرانی حاضر در اروپا:
‼️
علی‌رضا جهانبخش: اکسلسیور هلند؛ الهیار صیاد منش و علی قلی‌زاده: لخ پوزنان لهستان؛ محمدجواد حسین‌نژاد: ریوه آوه پرتغال؛ میلاد محمدی: ویتبسک بلاروس: نادر محمدی: دسته دو فوتبال روسیه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/28859" target="_blank">📅 15:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28858">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jqIpuyq12KjaKntXvWa0OFWV8MqQUlgrbrrwUHVcOI1olRw8VYE8Zeavxh9lsKlgHeV6_xXY3ey0YTNTsKAchs8LRYVLX0kAWJ5C5nfXNEffeTOiBjvBOXvHTMX_-S03uGHoJ3t1ZUqKbiBGmGtEUSXR7DmRne7DHU8wWTbZWhFxZ3BRRCNl52KQAKBntMJow-DcV_uCLII659Hxt91mX8Xa0saktXKtfRyq2IyfMOKMHAu-Wxnm9JoBxRZqF5lWjn4xJAcPU3mA7RnWCZW_HbX0G34zMXuEp2-TXtb58KZKBgADngRUXeXwexTHRwUlp_xhNuhxcsqdALm8P_VoDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه‌رییکای‌کرواسی با انتشار این ویدیو خبر از عقد قرارداد با محمد محبی ستاره تیم ملی رو داد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/28858" target="_blank">📅 15:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28857">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uj7qhrUWZg4a9V2upWkXmSVCgCUE56kmINlOzhNc_vsZ1KH6oi28eW3_e4jAsbOYQUvaDBiKbN1b5XiVzqTAbQrB-Oz8vh0DPOvGzYZ9G0txSB2LaNuBmK9LIHJ3ABEFMYiKLN25MUakdKEhzRkOqtQWK8mWUYhSVBHR89gBQ7UQo0AhWxEM4o2Pqd6Xztkc0J_1AQUvowIRz6M9kdw0uWqFmpHFM8YU-LJQ89Cr574hBRHnMax5unWwzA3S3GiPj_SxFTHpHT25o3gt8_DiS0XO2c0dyNtnbxN2Npx7_Cp3LmIadTQALjErQwi_fBdkdzw-9lTen7P5q4n-dTuQWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هوش مصنوعی دیگه داره کار رو به جاهای باریک میکشونه؛ یه چیزایی داره درست میکنه که با واقعیت مو نمیزنه لامصب. اینو ببینید‌!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/28857" target="_blank">📅 15:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28855">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d453f3d9b.mp4?token=dC_wxmrV-1QzXf1hxM8qgWQrh0C1a77sfHN74Sf0ui8wazA1lLI2eBCDPxUA7WkJ2MTJjod7R3FqTNLya9rI8L9gNMtWRD7B6zabex3U7Dga4JhX9IWYMMB7wDYBF6AfSWrIpZUgi4YjvThBKnKjBoFe6X0lrgPMlGowsMm-4dpSV0H2YjE5bpwaZmSyCE-goYvB8aFvOyASLC0CXX3KKByr1fs7yJZQfEYBm41MBTj7_ANZjUcuEu3hrV-R6tcFpYFBhNrrZSxdLwuD5y7unCACC36x9hD7KOQC9Tn5Ncca-RzWoKG7C1gDQUBjyJisKTpICoF4AsPw8hrAeRPIvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d453f3d9b.mp4?token=dC_wxmrV-1QzXf1hxM8qgWQrh0C1a77sfHN74Sf0ui8wazA1lLI2eBCDPxUA7WkJ2MTJjod7R3FqTNLya9rI8L9gNMtWRD7B6zabex3U7Dga4JhX9IWYMMB7wDYBF6AfSWrIpZUgi4YjvThBKnKjBoFe6X0lrgPMlGowsMm-4dpSV0H2YjE5bpwaZmSyCE-goYvB8aFvOyASLC0CXX3KKByr1fs7yJZQfEYBm41MBTj7_ANZjUcuEu3hrV-R6tcFpYFBhNrrZSxdLwuD5y7unCACC36x9hD7KOQC9Tn5Ncca-RzWoKG7C1gDQUBjyJisKTpICoF4AsPw8hrAeRPIvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
باشگاه رییکای کرواسی بزودی از محمد محبی خرید جدید خود رونمایی میکنه. قرارداد دو ساله و رقم بند فسخ یک میلیون دلار توافق شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/28855" target="_blank">📅 14:32 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28854">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ERj-GtHO045Sd-UMj2fVmLmNjFU76eM7Oxs-V6DiDClegYR8DHZTJNX1ox18PKTo0amZlvPDShoo8zakPIdd-N9KzIeC3sV7qdVh7qEQlQl6r9tOmPt58XCq-sn_kZuNc-7H326LVO5seTWbWQoOPjxKOkuH0xoJZu_C59OVfbUHT0Un5y5u3PZI1F5ZH3qrv6VPKmi_jeOveBWLSrKEQmi48wdgson1h_3DVldkxFB9v7twz5kinKGBmlO7SlAQo0bzLPJbkHEaDZA3cA0P3pOmzRTSyCEFFyvWGbo64p4XJqSU2vKuQGJi-DTE3N2cdzJjVMpCpaQJO8W8dJWLkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
خبرنگار رسمی باشگاه‌گالاتاسرای ترکیه هستند که معتقده این تیم امسال قهرمان سوپرلیگ ترکیه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/28854" target="_blank">📅 14:18 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28853">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔵
🔴
درفاصله کمتر از 48 ساعت تا دیدار فرداشب استقلال
🆚
پرسپولیس؛نگاهی بیندازیم به زود هنگام ترین گل های تاریخ این تقابل بزرگ فوتبال ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/28853" target="_blank">📅 14:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28851">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VQP6kGdS7tVDwjCxo12pOhXPNB6_0gtx4wtwnydUcQX9nr8AwnNOEZQQWOKdDZEziR0PayF5qbHJI6cu9i5wTsNcZubkemylQxrN-BWcOglN9HcDsBdU9Pj4_3sZQKAoHQ2B9LlLEe9s3aF-JWLiO_yS88vcRK38GpAflQ_xjxGsbkjGQP25ROoY5cpFYNDCSlRuxOOaT9aHrlR5S9__ZE8byBoswVMjtfKB9qo25amU5A_FP63nU1JiLbdnouXJmwKub9lccf_OjbCHPm65FvTOtTBDpFnkgV4uC5nUiGmvhQf_U8ylGhNGFImuOj7Apo6UvGRVqdO4cybc6Sdb2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XY1qhZTylZN2cagxZGRCkBAVsvw_YByQLoMAI1grpDuzN2nDFmqVJUCNLzJ7yQXR7MMpjyJqVxel4AkV9exXepHvuUi-PfXTgwHNc0QyBlSFbDv30wgVwI0Ez9_-7A8CcM28tibn7QvFCjTYqEUDlLl6od8a5OixjvvZZHkPN7E8wdtx_GgNJpiZGOeE7vN2_IwGeIROa68fvFqp32pkuAKlOzivvvjb8TzxzkCAM4gvjdw2Li9BS3RAC-86e9ilYKLnTFOORGd1hjGJmLZ9uTV7WoFdQq0AuyFH0zYFaGouheTN_fSclBXUUxrhVheDwR8XdD01nu27ZomYKN_8cg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی‌پرشیانا #تکمیلی؛باتوجه به‌ سوالات‌زیادی‌که پرسیدین؛ بعداز پیگیری‌های دقیق از مدیربرنامه یاسر آسانی بااطمینان‌ کامل اعلام میکنیم که‌فسخ‌ قرارداد یاسر آسانی درسامانه فیفا ثبت نشده و تنها یک نوتیس برای باشگاه‌استقلال فرستاده بود و هیچ‌مشکلی برای همراهی…</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/28851" target="_blank">📅 13:54 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28849">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e-gbhZHa0UiBfRnLv6FfkXFWeD8KVlEZIGirFyUmtzo7SR1u7fmcoidXqMZ3jF0yKMEmozNa1s7SgsTNzbIvB1yCUS72FcsVo_x77JrX9ZVpd7lJ1RngX0BUg1ERVePuqMWbr4JsuXUTPTFXiS9nQG0BTVyxqOQ-9PJfUZj6U6K1ksnHLdK_Q20xy-AuLwtPXVBgcG-YPH0OpLkLRyEXmIV7lZnoL1isZdJYfvcxRgOtGZlOKKaQTXy5PeKBXIoNFmCIko-MH5GnYl9FlRwRkeQFWSXKMbBgrkBS-5L7ZaIBKv79DTB4WFUTnoWYS2LqPTYbLENM6r0jRZPGvvK_lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZgsmkuA5prmYnLgPZONZlvdvDocdAwD6IxtpgAs10I1U08bsOvXl2aXrmUp-3lURTkJSHuO9_rQ_U9wc4OVNWdGKo1ndIPgJY0qeHnhKpuMQEHuHjERe2hmG-h1zWIlUgCmDjhpyP0yQZ2-rhYyqliUQcCySZr7bmpMuMLqc13Z-mbuXcJgPrJnRj5ioXKcr3Y9ypCMZD-W-sy8lrjXvzQyUNUc6GeDVpKM_cXeYCoO9fw3BcDeQ3ki_y_OauH8A_nzjnfMjsnFiEopkyTf_E1hxCztKdoIx5exvTxats1dCGAjAKUxrUqb6DX2UIT4lSETskTgEEbnpr9nvBJxdAA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
پوستر فدراسیون فوتبال آفریقای جنوبی برای پیتسو موسیمانه سرمربی‌جدید تیم‌ملی این کشور.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/28849" target="_blank">📅 13:38 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28848">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IHcFP3AF9tqZIG3YvcrK5K0yixhlgBLVpxiZR6H7yL6-OfkUjgHzunN0Nc-ZljIS7E4BiQ-ZCcrvl7U0t6bfeuaz7Poy6YlAepDWxaQnS7VQCiGgU7AbUXUba3jh1KQBMKvSkps9Kx0BiNVi9X3THIqnDBvUpnlm2qBgQ0_i9oFn0nAEF8cS5TMhGHwPKHb-uwIlncrP0kZrzPsK9hzEPDMdjPYY0CDAaAnxz9AKq67sxv3LuzvJ0NvvRhrcIDAVUj-upSFauqGyH9E-5FogmZxF_Z9L7RudLem3hrFyqycYDZ_ht_v7oV04pK_ZjJ90hYRqH1mgphXS7yrp_zf84Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
فابریزیو رومانو: انتظار میره تا فرداشب که پنجره نقل‌وانتقالات‌تابستونی بسته میشه انتقال انزو فرناندز ستاره چلسی به منچستر سیتی نهایی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/28848" target="_blank">📅 13:04 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28847">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RmW0tvNbal4wX2OGfrRMPD1Ewe4KpQz0mKlStwhngmkTQp1eY5ik0_gCUuzccunxIzKIRIUMwKsTMIX1yzFIuuHAhR27LDoDDX_kEigzvOv84sJmZRnx7CFNZay1DunbKPuiy75JmpWdtWS_vkUIg5a5bRHXl4VAotrMb0F1oTiaHEMo07OYAqGvdQfjXsZ2Kv0D7sgoORmXOn2nH-57Lo34OYJw3wrkF0f9WkNQfbAbeE_9J5Hc78GP5d7YzRqpl4edIA5NC0WHAE4EppoI5CFtb57rO8jnmXA8iKAafSLpwebMmV8yALzyyGY7F9nMWH9HFCwwHz1hcHd3GCIcOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مورد جذاب گابریل آرتتا پسر میکل آرتتا اینه که چشماش دو رنگیه؛یکی‌ تیره‌‌تر شبیه‌ پدر، یکی روشن و شیشه‌ای شبیه مادر که توجهات بسیار زیادی رو به خود جلب‌کرده. جالبه‌بدونید در دنیا تنها چهارصد نفر چشاشون‌دو رنگیه‌که پسر آرتتا یکی‌ازاین 400 نفره.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/28847" target="_blank">📅 12:43 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28846">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jgu9GAVsiwDLiCBfoozAYvkO62FMiLAn77Tc28DuSPOeXk9NAbzPg1UMfsZcfStfghMxmPs113wX_e_ssjhLDE9LIQ0wOgYzSfukeWt6H2aZHD6WWSEekBf3CVkY7QPQRJC_GggNNt_68BB7LRw6ZChPNDeo7-_24OHM8gHLm3rVbBmZzzMrHubEYoRCPkyebnUKZfNx9A3TYoZ1BxKiIIhrVJ9YfdlxwZQKLZnjBB3yPKBaW_0D3a01V0pECb8Ohy5n-MhlmWTCzbw_lKHfaqVzU_5c4XhJLeAPe2XXaTgJa4Yqd4qSs07EOVDLezgBTSrBRpG5YyMAMe1kdc4euA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
نشریه‌مارکا:خوزه‌مورینیو ازوضعیت ادواردو کاماوینگا هافبک‌فرانسوی رئال‌مادرید راضی نیست و به فلورنتینو پرز گفته او رو بفروشد. پرز برای فروش‌ کاماوینگا رقمی‌بین 60 الی 80 میلیون‌یورو میخواد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/28846" target="_blank">📅 12:11 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28845">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">▶️
ویدیوکامل ویژه برنامه شب گذشته عادل درباره اتفاقات اخیر چهار هفته ابتدایی لیگ برترو افشاگری‌ های عادل علیه فدراسیون فوتبالِ مهدی تاج.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/28845" target="_blank">📅 11:50 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28844">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ClUXRA5_RrrrM7zSb33TKWrk5b57MyK2bz7bml__FWINQUPf-zDY_25URkbizusmbcKnXH_IgJ4hZaGeVKatFoswgfZPfmf1Gf2vhjDpZMQmzrw3d_CBgV5hchWVE9tDszwpc01vrvCnBhRFC7TqJNMCxGicA-L5lzSNiBsqq0LjMmfkEoAAkRpNFJ2jilvpPKhcE-kXp7kjLWz0ex1zPwaHphEDZRULw5jslDjDt79c9p0GrsEXUp1L77Lvio9kvlLqkFO1i3cMsETemZ4hjoovMRMkV4WvzuKq1uhT_lDZ2DcddDr6_Lk93JaCWVf6FGLsudvpY9LZMy2ljLgDng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇷
دستیارسابق‌انریکه سرمربی تیم کره جنوبی شد
؛ روبرتو مورنو سرمربی۴۹ساله‌اسپانیایی‌ودستیار سابق لوئیس انریکه، به عنوان سرمربی تیم ملی فوتبال کره جنوبی منصوب شد تاجایگزین هونگ میونگ بو شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/28844" target="_blank">📅 11:39 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28843">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KQ_FDoavO1ZFqBMuokC6qGfPCu7-5EEeBSYK7Js8KYq4-zlNGOnDFmUaW7F-QIj8aXOIHjGDehLDSOGxq_ZKbZkvA_CfmDVYubwZjU4YxkjNkaKLehQIzQqOH2_OKzIBUZ-2MiQi5uFbNSP0vlyevE3mgvUrsBgKqlYPEAE4Offonf1cwI8ZNsRe87DU-gIds6gns5rs2IcPmdor7CeaJHWIhbe9hQA1RnNxR4y4FNn5b85nIx8d0avHf9yo3EcVj0SnSg2aPMMURMbhntD4rJKnDkZmCLtlNJKNl7bO5e4_3pMNoCUccbHU6naiNMJOuHpN0rM_XIOXEB5uaDxG-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رئیس‌کمیته‌انضباطی فدراسیون فوتبال: بعد از برسی‌های کامل مشخص‌شدکه قرارداد یاسر آسانی با استقلال قانونی‌است و او مشکلی‌برای‌همراهی آبی‌ها نخواهد داشت. بدین ترتیب پرونده شکایت باشگاه‌ها ازاین بازیکن بسته شد؛ خبر ریپلای شده هم بخونید!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/28843" target="_blank">📅 11:10 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28842">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4afbdcb0fd.mp4?token=PQbwXX-jud22W8zZuaJ-WhHnjnEyc2-_URV5AJFjgvjOxLMXKpNGwzkOoG8qDUNhr6iEXExf0tiPfrCxa18eppoyJS5tTVvlqPB4wimHI591OYtJRyzUGVITHbH7M3-BLbIHtLLmAq-Uveg7s0qCXK9J3DJxcLp97NSk2rzH5tUaFkdxW8u8eEfkcK1efkE0GTiHxvPeNFrAj_xcMI25qVkPrVjJbOePqCBK2oA6o1XtHk4ygKGUWJ2QS4XCQTb_WyeZGanGf25yS4P-MllSduRaNOE26virBqc0U-zZIUDGabny39vxaCuTsExb7W4lutZi5NHEjBg3lscOHxb7yQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4afbdcb0fd.mp4?token=PQbwXX-jud22W8zZuaJ-WhHnjnEyc2-_URV5AJFjgvjOxLMXKpNGwzkOoG8qDUNhr6iEXExf0tiPfrCxa18eppoyJS5tTVvlqPB4wimHI591OYtJRyzUGVITHbH7M3-BLbIHtLLmAq-Uveg7s0qCXK9J3DJxcLp97NSk2rzH5tUaFkdxW8u8eEfkcK1efkE0GTiHxvPeNFrAj_xcMI25qVkPrVjJbOePqCBK2oA6o1XtHk4ygKGUWJ2QS4XCQTb_WyeZGanGf25yS4P-MllSduRaNOE26virBqc0U-zZIUDGabny39vxaCuTsExb7W4lutZi5NHEjBg3lscOHxb7yQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
صحبت‌های جالب کریس رونالدو فوق ستاره پرتغالی باشگاه النصر درباره سختی‌هایی که کشیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/28842" target="_blank">📅 11:00 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28841">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZAM1Y8tIysYMGAPHp8LfWaWaom-oLmTdx9fYXijLAwZQE1ZCJNNHsA-CMsk5OYWUk5i-PNUL5uCkFOPgB4fBA6tgxceY4ai0xXYfKuQUk_vIgQHIydVAq1NC_23YEI7MOK0LaqY5ur1Y520I7xLZHYf8cdE1gAPdB4Crr8qW7pKv22Pz5ycvOcvujUTepeMEFpqmF_v3ZWqr-GM3jj9JySQOwDqe-CWG7Qe1jK3NB2IUbea5mwgVVhV6tURwz_4zocYvCgblp-COdah2Mu6Jt8b7pVtodcflPhMZdJXaOsBP9z4TPaKAw9A1P5bFPMVJ0gvMRennBZ2u3RHyfP3-3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ترکیب جدید بارسا درفصل‌جدید بعد از پیوستن گابریل ژسوس ستاره سابق آرسنالی‌ها به این تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/28841" target="_blank">📅 11:00 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28839">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JRyAD0gjrdnk4TfzVtaEvn4P6MjXZEfLHZbd4R0KlLqbC7ym5niLHVLa34hDHXZq6p3hHRQEgajd0uGu8ExSz2mLZLWfE-6A6_2FLDhZs2r68sV9y32-uavFoo5YtRQpIScQyta9j2SZA-XcCc0t-1m1eg2OF64k8XwLdTNMtnNccF4GEcDBXYtSpoP261EV4VzLS6pXo6yNXBNYKgnSdXwMeERvasr-LEBrwjaLJ3MtgX2KElElksRKc3Owt3rQF8WxrQFRamv7o8r-kSgE0XwQjJNGYOajTxqGzlAxrYHrSq6Plxfq0vTiHtsqnhujsOqxcF3ZhIWgV5_wkemgXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
تکلیف نهایی داکنز نازون دیگر بازیکن خارجی استقلال نیز ظرف72ساعت‌آینده مشخص خواهد شد. یا به جمع آبی‌ها برمیگرده یااونم‌توافقی فسخ میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/28839" target="_blank">📅 10:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28838">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rARelT8FLTKcCfwvFf6eOqUY4abK1Tp3rrQ-WBJfcmMaY1DS_Dje3TN92F2vh91FrNd8j9vY6inOMiTfmtgRAylURk3iZBg165WiH8-Q-VKuo7aDYCsLiOSuw0Wot94I5ZRhnjg3_6CvWOsZgl7fe0OIy_S0thpU_wxx-FB45LUYbiL3Ll9h-m6hpqIdTrRHTmp1HAHF2Y82lzEu1rFekdaQ33mMmbXGX1vt28-B0NSO4kX_Wf_GnqlvvreLPjE4HzvA-sBtm5RlkJMm6i7e8Uz8vkdjCzQDyK2lzL8-SFjX8WCO5xNBVZS5TYKci1QsZYuHqpdaHMNOxbZhiCdOGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دو خرید برگ ریزون و فوق العاده الهلال ظرف 48 ساعت‌گذشته؛ گابریل مارتینلی و اولی واتکینز دو ستاره آرسنال و آستون ویلا به الهلال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/28838" target="_blank">📅 10:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28837">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JuTtc-PrxK1rcr-p5AZEZM6m2zlHfzF1enZpnByFsPEtH_2ijWduaFfUUzp_24hD23TWXsX-HTeFuxsTgb8NFCiiGi5aR8OQ04ypgV2WEW_djtcO6Chbq3eRpoMuJCFvMOSla7hbZ57tkbC8pyl8N-LvtSo2CF8H6IrGU4hADzjr1Xq36MhsZrr3A_W08jhbu_YY775kJYujopXP5WTy6BMMy3hlw1oG8f0uHjRziQoAfrRVon2ikIdJETkSOGg9j6wqVXnNsp1AThl379SDztkvbb71T75HeFfN1p4to5b1FnZBiXgzOPbrf47bK0uN8YP656i_CghJ6EgvAw16xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
فاطیمه یوسفی فوق‌ستاره 21 ساله فوتبال بانوان ایران هستن که با عقد قراردادی به ملوان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/28837" target="_blank">📅 10:11 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28836">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V-jhGzgWb-8Axo8yEvPhbAj_NJDVI-go8XlbcokOdJPlHbouNxH8aKFYCsOLrFgUtkzNQMb7lRYGWvn3rv4-qY-LVi-8ACWyswERaVpj6JnXGr4R4t8rJoScPNcKWAAZZgjLgRx-8ftpJStxQhb_2WESCH60K637c1YfGBsZiTX62YhkCLiGG6OsKPV54-d68ghg6pOLh9NlV9rX22ZJQGXXk9UmWxJkAFgL9Y6hqmdWzqM-eaEeccW4HrBdVDyjn_N2HR7JioT5DsFdRFzPBiOi1ngsPEpFI8Jg7sjF79JmMh5s2pSdmqp0FS63kXKWqCWF3cjC1S_ZC6Mb9FR5nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
امشب‌ساعت02:30 پنجره‌نقل‌وانتقالات تابستونی تموم لیگ‌های‌اروپایی بسته خواهد شد و از این به بعد باشگاه ها میتونن تنها بازیکنان آزاد رو جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/28836" target="_blank">📅 10:01 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28835">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ddec47474.mp4?token=beNV08LoP4PAfFLE3c7ADiwF37sevABN9oP2R85gT1GPnjHUrTTM0tfWPdIG0uaLinU2zj0i2dT5WDFy-0EmYodyjOJIcR6pyuJMsAIPRind3e3kapAEsy1NBDA0vtZnnbzvY1XfBa005RBg1DW675tqXOtBhPZpYcV4l1lbpfbYrL69148P5xhq4JfCGIIAwEpYzpUGz9W-e1_ZdEpAs2tu43lxPWWNYEsSKxP-DuAUDulq3Isy489CtCVckYgmnFpoR6mfYSaknYlkMtAgkL_vr39uTcoshdO82J4wU7QbxsQIgkjo-ZFIROdbCraC4nRk43ZjkotfXZT61VvIWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ddec47474.mp4?token=beNV08LoP4PAfFLE3c7ADiwF37sevABN9oP2R85gT1GPnjHUrTTM0tfWPdIG0uaLinU2zj0i2dT5WDFy-0EmYodyjOJIcR6pyuJMsAIPRind3e3kapAEsy1NBDA0vtZnnbzvY1XfBa005RBg1DW675tqXOtBhPZpYcV4l1lbpfbYrL69148P5xhq4JfCGIIAwEpYzpUGz9W-e1_ZdEpAs2tu43lxPWWNYEsSKxP-DuAUDulq3Isy489CtCVckYgmnFpoR6mfYSaknYlkMtAgkL_vr39uTcoshdO82J4wU7QbxsQIgkjo-ZFIROdbCraC4nRk43ZjkotfXZT61VvIWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
ویدیویی زببا به مناسبت خداحافظی لیونل مسی فوق‌ستاره39ساله آرژانتین از مسابقات ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/28835" target="_blank">📅 01:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28833">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kIJ1h0VEn900f3UAn_XgA8obddlJ-dSCgyxFnB_Gyt0U_XN3BhTLR3AMV3PGwR9S7bVH4neKmcepKCnVmidmvo-w7g4YJOoIFMYpVjYJrkJNYh0gMfXBuCD-unTBegSiiK4NrVvWzuOUk6Q4vrzGsdiE6lEL9da1kq3fpnBxQRwJvv01pjzw26KAax0TmKD0GA8ZIaSwEWvR1WGrAiLd2WoiJjglPku_ehEkNm06J3TZNrmGM2rEksV9Qpt5mwyMCu4tE2e87vVjc4tBX8h4NCWyBmQxB3CA-TxTp1UWevaMfYcIgId9zTDus7nbysSRu_pcRPF5X798UnAEXtfrqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌‌امروز
؛شروع‌هفته‌پنجم‌لیگ برتر با جدال یاران نکونام باشمس‌آذر برای حفظ صدرنشینی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/28833" target="_blank">📅 01:37 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28832">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NEAk--1QRK9vIAyGK4DY8a3kmrLyrAOOMMO3_8JrnrPQ6drQDhOnZQZ682Z31gF-a3EZ6Ums9_yCpewmoyUEShPoeREYZ5hEO9igcZ_NN0DijIn1oko6yibDy7o8o5LRAdoiO3LkN4PRfmp-oFnQwTvjy5aKfVfU3GVw5g-9sK9R32_xv3x6vSIC_vODWFaGj2XCrOMgFobo8hXXO0C3rZUPhgoE5p6y4WwqZtWZA2WUQ5FEEDnOJHW3J4oeJVAIEKwYk1OJ5F8HVu3QSLL-2KqENVS5aTfzFXVoFsDTuv3OJJgE3jpoQnv1kZ6LWpMlLv9OYq7wT5IY2CDy2dtddw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌ دیدار های‌‌‌ دیروز؛
برد اقتصادی آرسنال و جشنواره‌گل بلوگرانا بانمایش‌بی‌نظیر رافینیا و یامال
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/28832" target="_blank">📅 01:36 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28831">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd806e1b22.mp4?token=Ei591l9vBAk1MURHm9Y1_YKhsOAjfh8InD6xiUvlJeGauveKKuXWbyYBVpKpr_DG5BkMNuFTPWkuLUqlK3g2g5OuEwLb-EDY44IQIkOzndzsez6XtWGZFgQN1CBVRl8aR8rX5H1zw9CCJcVAVquv3u56fzp3hd-Ms4UHoOsNqgp2m_tOynSn7fnFBcWMrdxyYm20ZRZtoX0Tv51k_DSxvBN46kGhvBfuoYW_turQXzro82EUjgiIN1e_wN4syTDoj5ECaYi-GeIfHaqFnmJgV1lOgg9r3mRE-Y1tV18bpi4tSDLSq8sCJmt5JXOsbPCS1XOri4zucPW99EwT_NNY3YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd806e1b22.mp4?token=Ei591l9vBAk1MURHm9Y1_YKhsOAjfh8InD6xiUvlJeGauveKKuXWbyYBVpKpr_DG5BkMNuFTPWkuLUqlK3g2g5OuEwLb-EDY44IQIkOzndzsez6XtWGZFgQN1CBVRl8aR8rX5H1zw9CCJcVAVquv3u56fzp3hd-Ms4UHoOsNqgp2m_tOynSn7fnFBcWMrdxyYm20ZRZtoX0Tv51k_DSxvBN46kGhvBfuoYW_turQXzro82EUjgiIN1e_wN4syTDoj5ECaYi-GeIfHaqFnmJgV1lOgg9r3mRE-Y1tV18bpi4tSDLSq8sCJmt5JXOsbPCS1XOri4zucPW99EwT_NNY3YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته سوم لالیگا|شروع طوفانی بارسا هانسی فلیک در فصل جدید با زدن 12 گل در 3 مسابقه؛ پیروزی پرگل آبی‌اناری‌ها با درخشش یامال.
🔵
بارسلونا
5️⃣
-
2️⃣
رایووایکانو
⚪️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/28831" target="_blank">📅 01:28 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28830">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nbYJ0ELfRQzOAYyGQD9ItXfHtoPh3kWIzzC0X_wf_nQbFeSrW-WcMRI8B547RqdTrEy1QirN1gGDX4y9YNghDiT5Y64cCgr9S11s0nU8qTCh74TinYlI7M0X4kIejt5iCrjBMlzYnYrtkIgpFVcq1f3oZtfhb2ABvBk5Ga2SNrDVsYHph9NwU-ROO3QMrQRESmCu6l7-4Qkox0MeNMT9gDcZQLzoGJeX3quBxX52xvedxhluuPfBWiQX_VU-he3rpcj1s-T8LiHUawgftHZxQ3vEqZa1Ci5TfrKB4rErDRTiphVFT_URuaVvx9kJ35J-mIxnS3LGG-H57vETVQI03g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته سوم لالیگا|شروع طوفانی بارسا هانسی فلیک در فصل جدید با زدن 12 گل در 3 مسابقه؛ پیروزی پرگل آبی‌اناری‌ها با درخشش یامال.
🔵
بارسلونا
5️⃣
-
2️⃣
رایووایکانو
⚪️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/28830" target="_blank">📅 01:10 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28829">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lFZS18MhgAKw3VG6KDu-uOnf9GsIqFTAPWZN71y25UVvX19T-y8WPjba4n0qHA2nfVCy9AWe0nsdfybAk_YosWKwulAVHDWONbpgud-qL2Jme4YrQmN2nLgbeHWM0ByzXK6u-f6u_80J5NHuMOoGchVux526n_KREOg6CWVObzQ3V-TsfGCKbwu2Bw8MEhtAIY2MyFI4_kiGr5uIKCgAswv8JLx2BcfcDVzNYsdfaIQvCDsHy-69Aj5w-Dac7pAch9Lik2e2sHim0oSBr6Mp2S6jukI7kpNZ_eG7cHW1CbZ6D3gqzoZztR3x-Fnfa5aYZKZ95CEqdeX8egIGSNpoMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سوم‌لالیگا|شماتیک‌ترکیب‌ بارسا برای دیدار امشب مقابل رایووایکانو؛ ساعت 23:00 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/28829" target="_blank">📅 01:04 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28828">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f678a57f6f.mp4?token=ikl0OBo5-xixgZi6LeKWJHaCvL7At3Jzpp0Ocjgu6YQdmFYrZp-5zKOhMdCff6d02RHMW61Bv_jW5KRX67AxWgIXFo74KZZ9Jrowuwj_0nYP-7YjTjdZYBmkLvsLwjoEY7r4LWPnn7zrO9EWtyk3j-Xmej7aaDj_x1g6Yt75jW_E1s8NxtFNOADnsTSZojB0Kz8fFKvjshBK73cNBXKO8de0kEOksfTc1asmck-5XHqDr6MgXzCV6ppXgmu373jOOS5sDhRRjV2VJa-Lv6_JaglIGfNFdyZiEpTuttkwYBLt4yj7AJN7ecj35GionM93m5tnqmpCdVhWkli6FFI3Ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f678a57f6f.mp4?token=ikl0OBo5-xixgZi6LeKWJHaCvL7At3Jzpp0Ocjgu6YQdmFYrZp-5zKOhMdCff6d02RHMW61Bv_jW5KRX67AxWgIXFo74KZZ9Jrowuwj_0nYP-7YjTjdZYBmkLvsLwjoEY7r4LWPnn7zrO9EWtyk3j-Xmej7aaDj_x1g6Yt75jW_E1s8NxtFNOADnsTSZojB0Kz8fFKvjshBK73cNBXKO8de0kEOksfTc1asmck-5XHqDr6MgXzCV6ppXgmu373jOOS5sDhRRjV2VJa-Lv6_JaglIGfNFdyZiEpTuttkwYBLt4yj7AJN7ecj35GionM93m5tnqmpCdVhWkli6FFI3Ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
باشگاه سپاهان از باشگاه‌استقلال و هواداران این تیم‌بابت‌حرکت‌زشت و زننده عارف حاجی عیدی عذر خواهی کرد؛ این باشگاه همچنیین موافقت خود را با قهرمانی باشگاه استقلال در فصل گذشته رقابت های لیگ به فدراسیون فوتبال و سازمان لیگ اعلام کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/28828" target="_blank">📅 01:04 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28825">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NqK-uau97-Y2eSKJbM4AM0N5xS9OXni4tXODTvaZozVAng1K1mXlbWBucEbwt3Lw8CJ4LbGIm4wuCQlPUeIBmWDBRIMxTiLD3_XcheoDE7Gr5Vvp4UkU1hYjqmglLtx7RbtcLgBzqAA4w5CrpzsWXp2o0MBt3VmU2eOeDTu60_3qr0KJy6wgJEvAYRYNSACsizWLitqJdA7OP_R1FCW-m01sbM68QiccMoGG-LzM58hW2XY63hstXI655Xxmpzp8fLG38bKVtjZo3dDCUyiNRH3Vd6GwsxP4hSVRTt843DEK2QJP4Qr3SbGuA_r8UzK9YAGwX4IZu20FXteSztNNOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به مناسبت رسیدن شهرآورد پایتخت؛ مقایسه ارزشمند ترین بازیکن دو تیم استقلال
🆚
پرسپولیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/28825" target="_blank">📅 00:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28824">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8c6848cef.mp4?token=p58dyOEcP4V1t_-6mRZEmzcDfYlXx-xSrTnlx6exx-M8CMj0WkyJmEhVURdWcYhp4pWNnxGgVylwvQD6F8yssHb_rKWOEgFcJ01-mPR1LHwzpndiQEX_xzXmUrFitZJt-v9wiUI4UPzAGu1zJ03PxbJe_VQtlY5hTLowXKLHnRALpRm0rSkG-frgwv7R0h3q7_PglKWtAp53qBj-wv7d9k2I6fJgOSVE6Ah_n5QJgCL6Ehr0p40N8ny8ZrfUNpVgWbdfxa62hbLwU-9mm8zy4o4Zn4-D_WreMY3TOHad_kevivQ_Ibb3EGQ7wPJOOwHaWJdkn_Ttwj1SbrS-xDYSHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8c6848cef.mp4?token=p58dyOEcP4V1t_-6mRZEmzcDfYlXx-xSrTnlx6exx-M8CMj0WkyJmEhVURdWcYhp4pWNnxGgVylwvQD6F8yssHb_rKWOEgFcJ01-mPR1LHwzpndiQEX_xzXmUrFitZJt-v9wiUI4UPzAGu1zJ03PxbJe_VQtlY5hTLowXKLHnRALpRm0rSkG-frgwv7R0h3q7_PglKWtAp53qBj-wv7d9k2I6fJgOSVE6Ah_n5QJgCL6Ehr0p40N8ny8ZrfUNpVgWbdfxa62hbLwU-9mm8zy4o4Zn4-D_WreMY3TOHad_kevivQ_Ibb3EGQ7wPJOOwHaWJdkn_Ttwj1SbrS-xDYSHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
ویدیویی زببا به مناسبت خداحافظی لیونل مسی فوق‌ستاره39ساله آرژانتین از مسابقات ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/28824" target="_blank">📅 00:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28823">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WCk4F_BGX5XDeqJpg7rvJ6VYIA2glNtsTljiepcss5UTRR5zwestkuiwFbOOyjDmwYyyyZ_RohVZcbZPJY6V-AIJEnO_BnKhYWXVEIxp2EwN3h77aCv5TLDRPS9Wfw2MjDHBL3QXiQdPjD1ptqqUmMYEFWAYqVisbnRuM3n5P9zH7wY3Mm81uW43iOq2tquyvma_9tQFZdGrboEUDpPCCsQcvdq6OgZ1mtSDh8yO7E5ySfvVI0cP2z9E8aFSSyxqGUIjSAruDQ79RDX6PvNAj7VnYtBRPf7rwa0NGw9QrAcVTV5ZTNwXws29BUHSLz7WX_CYUOt_zXjUCaHR8fN9Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
به‌مناسبت‌رسیدن شهرآورد 107 نگاهی بیندازیم به افتخارات دو باشگاه استقلال
🆚
پرسپولیس!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/28823" target="_blank">📅 23:59 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28822">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vNLaKlwSklPlIM1sQ2pU1319ARJn-EAfLWT95pff5SqhPlGTQ_RHOQBtEjRlEFIun6tU_RLn2Aad4ETbmm4GwPYclnwmFMdFKVre9BKclS_ojaqKdSvISK1RNUHp8WgxWVaYuUC7wpBt5a20tT96Be8bUCdYPf0ZQei9ZN-iX-26CEW3iVxfKtCD_WnqYM-Y08vI9sBgbTNHT_kEBuEMA52iGng0qmgEphcuXVsO6lpLtFZug37ebASbBs8DO5RKwZz1kOtE-KC3TA8PFvyGnuWcxl0bokydaLXvMqYcqpIZ_9FiULWRAOSy-Ce6ojF1pIqVf4NlFK4FN_h1nCkLOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لیونل‌مسی؛ از کوچه‌های‌روزاریو تا قهرمان ملی آرژانتین در جام جهانی  دیگر لئو‌ را با لباس آلبی‌سلسته نخواهیم دید. "خداحافظی‌ام را در تاریخ ۲۱ ژوئیه ، ۲ روز پس از فینال جام جهانی نوشتم. امروز ، پس از فوت پدرم بیش از پیش به درستی این تصمیم اطمینان دارم"
⚪️
…</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/28822" target="_blank">📅 23:41 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28821">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ltel0kvtF1jqLtwbuS1MHFFcdaIEqwhCxDQNBIGhUCne1eZskVVt-Xqb17jg1aOr_e0OiWV-5kZfyhpnFNZwf2acGLDVTH_L4fuwNuukMBc9Jne8Lvg0ncjJ3SkRYD658n7Mz4LbnnDXksFTaGXnP5lx7s9dYlJKJc4fzH7tr2WpFWaFeCQtNgEvin541ttPprTBt_ymIZNNyBEzeY0TXj0aQ7hD1GgSj2pusXKat4Z5dznHDroj4-M_9YVyODFjAlKl4JYxBcmTqRENw7jVFvRLVwSxoAu6ar_2mlRDthsL8gFBplwRlZred1OERRt7wMbjRZgFSYaMqowfPj6OXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برخلاف شایعاتی که امروز مطرح شد؛ همانطور که دو روزپیش‌گفتیم‌تمام‌مصدومان دو تیم استقلال و پرسپولیس یعنی‌مهران‌احمدی، رستم‌آشورماتف، جلال الدین ماشاریپوف و سیدابوالفضل جلالی درلیست دو تیم برای دربی قرار خواهند گرفت و مشکلی برای این مسابقه نخواهد داشت. حالا…</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/28821" target="_blank">📅 23:20 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28820">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d24f702f0.mp4?token=N0Ch7jpkROxQtSVym9RLitrNZR6c1svr91by3WiB5U13x6Z9Xexlp2AXrArNZmOhZq8pVtHwiwfLKSq3xp8DNPorXCypkzXW4xAa_sMjsEm2wqjkDsIRtwlj9SwwuWW9lEZiJOknmxAxJiChyc1Fvi0Alp4ad5NG1CBMRzbKcTlCo26XKnpESAIYpnXqDSRPrr6QBnMIqQNSaoAbP1a8ZZtFgFdX4nHs0-SWOP487Z_ZWo1e_4tgfdT_fUIc22PzyE7LkNJ1O97yCo6pvry_CKhUhgIPTOB6rzHYgDjVSp1MS4lfh4PVNb1fyC3SzP-CfwQ7nsbyDj1bp4r3_h4mNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d24f702f0.mp4?token=N0Ch7jpkROxQtSVym9RLitrNZR6c1svr91by3WiB5U13x6Z9Xexlp2AXrArNZmOhZq8pVtHwiwfLKSq3xp8DNPorXCypkzXW4xAa_sMjsEm2wqjkDsIRtwlj9SwwuWW9lEZiJOknmxAxJiChyc1Fvi0Alp4ad5NG1CBMRzbKcTlCo26XKnpESAIYpnXqDSRPrr6QBnMIqQNSaoAbP1a8ZZtFgFdX4nHs0-SWOP487Z_ZWo1e_4tgfdT_fUIc22PzyE7LkNJ1O97yCo6pvry_CKhUhgIPTOB6rzHYgDjVSp1MS4lfh4PVNb1fyC3SzP-CfwQ7nsbyDj1bp4r3_h4mNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نادر محمدی هم یه تنه تمامی قوانین فیزیک رو داره نقض می‌کنه؛ در جدیدترین اقدام این پرتاب 45 متری رو در لیگ یک روسیه انجام داده که کرک و پر تموم رسانه‌های دنیا از این پرتاباش ریخته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/28820" target="_blank">📅 22:45 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28819">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e4z30cy66unK0gfVzQMds5_rGk5V4ZbwlYPeGneIz5fJ0Ai8ajEEmnLDEYPUbG1imoHzonB_dS44ZeM0AnNs85sO9LUOw3xXpi-tijtRmSyS-8FB384PRJ0VeCYTO2Zi00ayNNOO3-4YAX45Au8XTkVfaSD9-JLC4AKaj9PMLnhnGlbqtscBBo8CERWuikvLD1exI_IlzB7IacuwAIlI4s6VjfIBUSaiHgnqLt_bzTT9cdzhvKBaLZ05zvDpTujLfZb9H2WRbGPRm81HQ0mH77UHXPxoBHVg6zU-eZMbaD7Td6D6bULP7fj8lxW6wVNJ5k7x4kg9wnU7S0cw7WhINA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
به‌مناسبت‌شهرآورد 107 استقلال
🆚
پرسپولیس نگاهی بیندازیم به دیر هنگام ترین گل‌های این تقابل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/28819" target="_blank">📅 22:17 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28818">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XfceJQKaRFxh-oyyjTmZlgPRmO-RZNEwr9TCq9CKS2aHC2egBktl95wnrpVexdMApf8GfiCBI8lm8IIDTAXj5ZSQMGErKDMKTnLxANoBRHXPxEyRfJ4VFE55RkPcuoUntZYt2oAAsxe4_fXamMoI1G2TR4kF-AKEcBwevKAj1EToYjv0p-ydL1DIOzyrNyMXu0i7CXwHfhO27CkUrRgTYJkzKjOGxkwgM5OUQ97OzB4XM-gHJC156Qgppz_bzD2Ty-KvoxTtL-r-lcRL0H9I4hY1m5IWdWKSafHU_IPtlJm9Np58tiHcVPmOhZ5uGbgsV_XpR_X81zpwB9F2lvbpXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
ایلیمان اندیایه وینگر راست 26 ساله سنگالی اورتون باقراردادی 5 ساله به منچسترسیتی پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/28818" target="_blank">📅 21:53 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28817">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LR7HQoTl_DNUG-yjkVpFgFAWeZgNlvtaTbHByi-fANFbVlkBUI3HoOVNlxnKYXTlmALo7gy75DDq4PVJEeW4BGgtt09g4LsosysSUE1eSX5Dxhmn-ykNQJWZZ9XPDzaEjxXtcy7ZaHoATxuqxmm-ibeYox-MXeuvFiqrVLohciXdW4VQZ2yUzsNzAqVYKNX9AckEWYH3QIX5kVva-oTazTRqFfCaYRgnzQEVjagQW0KJF1lvM-ih7Qs-ufrHk2wwTsCL4xBsjrc-Zy853k_IJVvcwYqphGCaLh825NZ8LEMgbT9dWVxnDXV04TYHeNy9RJVWFAMN6nG0eryBkq2a7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سوم‌لالیگا
|شماتیک‌ترکیب‌ بارسا برای دیدار امشب مقابل رایووایکانو؛ ساعت 23:00 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/28817" target="_blank">📅 21:48 · 09 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
