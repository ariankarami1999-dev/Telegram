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
<img src="https://cdn4.telesco.pe/file/ByJo-9dl89Khdp4gk2KH5hMFuiT452PcrZi90zHfIs75IwHbZB6rYJgkT6DzNhuVUQoDv832gkclwpTzaX_cysIlIBR8AIPACTNcGXlJybR-IsGuR3Xe3ti0whTYux6uUjSzM_lIfb5wacgCk1lC7CbfBBSBG1aIXU4iPCbFZg9mwI3QifZAYkNM20cAViU1OOjuFS_VXvdHPPtJ0leyyzOWpPPBNcDr3DCxXfqRpYqcgJPFWZBhRBgnVBgF3RyNVTuOt9jCPuheSRZJeM3isMkzZeklhwwGCjVg5NVQfu2iuTiS-3XFjc08PfKdr-V7Cpv8labVVcMU1yaJz1p-Xg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 245K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-24 21:24:35</div>
<hr>

<div class="tg-post" id="msg-23459">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s8GDHVyMSwB0WaxHyAe3A98BVZl8XsuMYSno4R8oWUJZrNAPTG-aZSU1hs_GnZKUArQ45HinPGz9meyUjVx9RDsZ2e1QSdA-Wnc-rGhtGtwFRW6-eeGQpP65AzdEFzgcTYc8W6f5LMywJtGL6-QSD7aGJk9XPqK6Jr38Z6VLdsdiI31MPXEYuMstCjKwZr0sCCVx_cVAhSdAhAMojV2DVhPjmbVsousvAN1knxc6sYJNEvU68banakZugdmebx1wFdp3XDrCfP2ATsjG_d0FRGwfioZZa7WVGPmAf2pomRrUJcqeU015f6X85Nuvm5LKcU6sf71JKqNIiIla9dcg5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلیل اصلی‌ اینکه اکثر بازیکنان ایرانی خارج از کشور علاقه دارند به لیگ برتر برگردن اینه که چون شرایط کشور خاصه و ممکنه در هر مقطع از فصل جنگ بشه و بازیکنان‌ خارجی تیم‌هاشون‌رو ولکنن برند لژیونرها قصد دارند با رقمی بسیار نجومی تر از دستمزد فعلیشون در باشگاه‌هاشون…</div>
<div class="tg-footer">👁️ 611 · <a href="https://t.me/persiana_Soccer/23459" target="_blank">📅 21:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23458">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BeXlkJvKbMl_KSpxzqHjbinfsmTO2LWnh8elmyd6a60twbbvOExWK8dmnD67Xo59gbqnq3uH5lhBZZLAgD2eJX1upDMgdvzkeClJxA2Gb-hZ3r9WXG_QtzRW7pdvNHcxSl04y8Uod3JjtdfVxJkj3ZHijJUW6zI9PPJkZdD1Gg58ujMFFHMuLlLyK778EmDu1m_PEwDA56-igZoYdk_jSBlJ_LwZQ-Ng0VU3N9rgEQM9vMlx8tFarpnvajsDNzhrGDV27kFFiedYVne_1CtDgDubXW0kget4PGTSN2mEau__sYJuF04KrUkBco5pUTTipHxohzsj5TEaqZmJUo4YPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛طبق‌اخباردریافتی‌رسانه پرشیانا؛ اولویت اول رضا غندی پور مهاجم 19 ساله الوحده امارات دراین‌تابستان پیوستن به باشگاه پرسپولیس است و درصورتیکه کادر فنی سرخپوشان روی این بازیکن نظر مثبت داشته باشد جذب خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/persiana_Soccer/23458" target="_blank">📅 21:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23457">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D-9mrTb4rS8JGwe1eYAkWQYsJHodWhqqyQDb_TMn3crB9_qaNX7h-N3pSy7L97zfE5P5s07suH1_NxCi2JwxGEFBKGOilNMV9PgGjmni4PmWfmZLCHYrIrZV0kOOd4r0IKkR9jW4MUXvvil6bTcdJWytKvnTDq4IlOTTN6XzB8MwmntHGE2umgwZi2EASpf6ePmeYlMAC38phZbqdXKu1zdA8dfCmIwv4WXxNNTxH16vLtarA3A9ltf4NPtN0EjS3FqET8QEfNi6c9DFZs9Rrq-iQhG1P7OnSCiy4AdLWaUQGl-MA1B7y3coBgAxizMzfj4XwfOT99dHaLAaqHC-ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🟡
🔵
🔴
👤
طبق شنیده‌های رسانه پرشیانا؛ رضا غندی پور مهاجم‌فصل‌گذشته الوحده امارات به دنبال بازگشت به لیگ‌برتر است و مدیربرنامه های او این بازیکن جوان رو به چهار پنج باشگاه بزرگ ایران پیشنهاد داده است. به احتمال قریب به یقین غندی پور راهی یکی از چهار باشگاه بزرگ…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/persiana_Soccer/23457" target="_blank">📅 20:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23456">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tvX9BJ7OjLLASqYWuqI4uYPEDyf5qHOM7IscyyL6QzqElCEzBAt-TRSxA0mNYR-QwhVVw2ZRhYyOTKIU3cHckrZYQ_R1cnbLGjJ-GNWwoX8RsFCn9LGKpI1Wobuk2Q2lscuc9V2Cv1a_E2WILnkKOmwkaN2uAgMhMGibIN_V9YNs_BMyr1bVQaxoTO_8nucZ2DST0yENj6rQPKPkBqOeVEtelI6TNymlntjwI-Kug5DkMpQKcI_MC9EvqdyA6IZwQt7xsUFjP3K0PovEF8cG9TbAee-_IhSSwxJzB52OCs5MkjLwQwjn93hb2d4mnUvHRZQT5Wxzy5dhbtAGeB5VOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
چهار خرید باشگاه رئال مادرید در این پنجره تا اینجای کار؛پرزبرای جذب‌کوکوریا 50 میلیون یورو به تیم چلسی‌پرداخت‌کرد.درحالی کوکوریا جذب شد که اکثر رسانه ها خبر از اومدن کالافیوری میدادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/persiana_Soccer/23456" target="_blank">📅 20:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23455">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bd12ea167.mp4?token=kV6i-q5JqATGC0EGqHNCunlZF9NtThqVHazTGADyuExm0f8yEFosO_iFqdECUyV44mmAlesD5B6icky9Xj5zyCy1SlhvR3uvSo-ZqIPnp-1zkPaA9pF3qqPbg29e0kixZ_u7Gsz7H5CZQ0UoaWulJFKQjszDPBExYXXSsU__XJKLfe9kmkDuisJr2pg80NZCixGR8bDfMcOLHbeQxGy_ft5WaYLCIf3_mJEfMbBvZjxsOamfcPXOaR1Ve1OJE5kS6V23LRSpP7N8eV-iiH8hObXt57klTTsLwgW-IrsZaVJu-XaJ4UBTBLXDJJ8uYC8ao7FWv1qQc8qfQZn1T5t8Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bd12ea167.mp4?token=kV6i-q5JqATGC0EGqHNCunlZF9NtThqVHazTGADyuExm0f8yEFosO_iFqdECUyV44mmAlesD5B6icky9Xj5zyCy1SlhvR3uvSo-ZqIPnp-1zkPaA9pF3qqPbg29e0kixZ_u7Gsz7H5CZQ0UoaWulJFKQjszDPBExYXXSsU__XJKLfe9kmkDuisJr2pg80NZCixGR8bDfMcOLHbeQxGy_ft5WaYLCIf3_mJEfMbBvZjxsOamfcPXOaR1Ve1OJE5kS6V23LRSpP7N8eV-iiH8hObXt57klTTsLwgW-IrsZaVJu-XaJ4UBTBLXDJJ8uYC8ao7FWv1qQc8qfQZn1T5t8Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های شهاب زاهدی درباره عینک خاص‌ش در برنامه عادل و عزیزم گفتن‌های عادل به شهاب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/persiana_Soccer/23455" target="_blank">📅 20:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23454">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DMsenNJOXQi16lOUTOH0rIG7tApGWIZ-N7kiPRZKfQUAI06clP8xiWKJz4qPVzxmEGjeRsB-vCoQtUsSYMyXfMNqm7sl0Agb5GXOuhmsKSFPg3NiVw0mBlgzQLQqmlwAYkE-geDj6hjZ6xolH1-h_lQKopn_LZHkSIVUsa0fBHNs9PVLY--8TXneana2P1fpe5qtD7WtVnpoPw2KXD6KZEXH-7zXPmRuAv4jiA3dBI_sgdmIiX9oGcD3ZIJBjLImNEBP-vUvOrDD2RWGPK06GSNsmiWqOhTN_glp9e8UJJ6w28Keyk6bXVgaRJlQZPJpOaV0DjqjZs7_VlVCb73wrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی های
#جام_جهانی
رو بدون استرس و کمترین ریسک ممکن پیش بینی کن.
⭕️
⚽
آلمان
🟢
کوراسائو
⭕️
⚽
هلند
🟢
ژاپن
💳
حسابتوبرای‌این‌بازی در
#رومابت
با ارز دیجیتال شارژ کن
🅰️
🅰️
🅰️
شارژ اضافی بگیر
✅
💰
10% کش بک روی تیم محبوبت
💰
100% بونوس خوشامدگویی
🎁
20% کش بک بازی های کازینویی و انفجار
🔥
همراه با درگاه‌
#ریالی
📣
‌
#بدون_احراز_هویت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⛔
در صورت فیلتر بودن از طریق VPN غیر از سرور انگلیس ( سرور
🇺🇸
🇩🇪
🇨🇦
🇫🇮
🇹🇷
👇
👇
)
🇪🇺
https://trentivo6402.bar
✅
کانال تلگرامی
#رومابت
24
👇
🔵
@Romabet_official</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/persiana_Soccer/23454" target="_blank">📅 20:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23453">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MqUmJSjyb7lPvxyYQ1h5ooQmSBGr_2s8nP354ThiP65nNQiBpJgHxJ-shlzMHavSHSUM1GgkA_9YkpHJ60JAAsCY0PEujEQOyXBFvHeShaJ1frW863L52Rs0TTyI-aHGAO4D8aEeT62Htx2CcS6pXVQK-HM79uGR08LEjoanlnRbq5eOskE-FD8W5VxknHA2i2ZS_nElVRNs3z6FrSj-bWebdAlfRZivMrPqIa_ANnCZIYKM_9frH7Bf77DWozVmIWDflNaq83iGGSboEmf3Fbx78tgvVntsqsONB8SO7dNfm2dSKgDQLITWviwsFNl3sKaWp-YtNG0qLr_F8XdiUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏐
میانگین سنی تیم‌های حاضر درلیگ ملت‌های والیبال؛ ایرانِ مدل پیاتزا دومین تیم جوان این جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/persiana_Soccer/23453" target="_blank">📅 19:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23452">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kyg-ANUpF4uk8wiV-UCKktRsRftZLjExTni_sYL2ww-bT1zpQAdanhQeaG8bpqtvC5dAqdBO-V4wqOc-UJZlkr_ygK1lCKnjkusMOUe6kXl1X3PMHX8mcO4FC_BeFYm9X9wduHeoLVbob8KZjS2hQI8OTvhcno_rwWXI08Ugppz1IyziMTii5aUVg1crdAqsb5hX4AnKlf71QgVjFg15QqIYjAadWD6LBMAZPCPgdwOxHO8Eh9QVkJeRKDZ4_WVb7hQRsFurcDL59NSDhtj0wBqSJN-gi-7IWl0nd1KYHFfHvJM94qvlC6MhEeK25pLkZ8iiILyyHRXvA6BtreAPPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خرید غافلگیر کننده کهکشانی‌ها؛ مارک کوکوریا مدافع چپ تیم ملی اسپانیا و باشگاه چلسی با عقد قرار دادی پنج ساله رسما به رئال مادرید پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/persiana_Soccer/23452" target="_blank">📅 19:53 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23451">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u77ejBKK-aFHkMc4a2NzaUyJZzfyypEbmLt5AbdlcXUR3emeICktC50KZiepqkukf2A8k9EoRxNGpgigZOMG3C2fgQgymSizCgGrzH8rc3bPRNJeFv_aQivQPONoCThfsfy_9oT5TAPwwnH7Q60oF2N31SgaZRXnHsaH4_OqOYQrC-3YAxESNOO1eJIQ9mqx01d2zrmO-QWiMMPsXQFWZ7ddt4zoMXmS80RKfYqthDOV0KcGkjU-x17V6WzYaa9qge6895k4whRi3zCDNADdW8MsfMxGrpWEv1Hz2G-oLNlHW21vhirijuF-aWOlSQSVkpay4Ol-Hnhmlb-kvFSrpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ ژوزه مورینیو برای‌فصل‌آینده رقابت‌ها مندی و فران گارسیا رو در لیست مازاد رئال مادرید قرار داده و قصد داره که در فصل اینده از ریکاردو کالافیوری ایتالیایی و آلوارو کارراس استفاده کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/persiana_Soccer/23451" target="_blank">📅 19:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23450">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZGlXIDj9e2ls1zwsFITN_AJ0JF4ywLtEDemxFakQ3V7pJle6R0D7ZvhU1nJWIl94TBiI9GOFOtY2VbOXTdhWN12_clzlsgc91o87NcSyI4b3BwJ7TkAkigQHWkHcd-veLXTc7Wn-muTM5XDV98ZX2WAlYBu_OF4oyHQFatLDzudtwiZFeNDXfPO-7btCYPRUVZo_XkjdaNcxdxRohACwoQhKK8v-0ta0GIcV1nAdDMiKi_ymSnUlFTGuu0zpCTqaKQlfwaQoSj5fCFAJv7U3MvKo_TWFNNkX_vwlGOmZI0Z4OLcFkxmU1iH97vOCTLcajRVZCxlzzA3o-XRHLaBbag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باتوجه به تعداد سوالات زیادی که پرسیدین؛ لازم‌بودبه‌احترام هواداران پرسپولیس بگم که‌اوسمار ویرا لیست بازیکنان مدنظرش رو داده و از بین اسامی 9 بازیکن که به مدیرعامل باشگاه داده 5 تاش رو قطعی میخواد حالا اگه مدیریت علاقه‌ای به همکاری با اوسمار نداشته…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/persiana_Soccer/23450" target="_blank">📅 19:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23448">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/129e645eb1.mp4?token=g_rV7nU8NVUImbhZPrisGP_3mv9Yh2SI-31bBRjK5j5h0NLMzqb1nU7XxsjqPJahhquLWbzDFxG6wjJKqp0NnH7mSs3mhla0O0R04ZfknoupMCky5edbw522E967VFBG6KHtxXL3khdlKliFFFqpJgeK7JhUrLe1MF-Cbi7mN6QTW72FdUIJWQA6kGvZweO239rOy1pbejNjXI_0qjnR-K45xOZKlpzqNX3PtlqFt1ZT13fXCJfCQ8jluT8cTEKQyHezPM5GC88zhObxMPCkhYnTjdPJLR5ErHNGXeF1Ony4OHC5Y2e-aEbUxrQrV8SMSNMS-0Ktkrl2lxfQCQ_vTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/129e645eb1.mp4?token=g_rV7nU8NVUImbhZPrisGP_3mv9Yh2SI-31bBRjK5j5h0NLMzqb1nU7XxsjqPJahhquLWbzDFxG6wjJKqp0NnH7mSs3mhla0O0R04ZfknoupMCky5edbw522E967VFBG6KHtxXL3khdlKliFFFqpJgeK7JhUrLe1MF-Cbi7mN6QTW72FdUIJWQA6kGvZweO239rOy1pbejNjXI_0qjnR-K45xOZKlpzqNX3PtlqFt1ZT13fXCJfCQ8jluT8cTEKQyHezPM5GC88zhObxMPCkhYnTjdPJLR5ErHNGXeF1Ony4OHC5Y2e-aEbUxrQrV8SMSNMS-0Ktkrl2lxfQCQ_vTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛ شروع تقابل‌های جذاب جام‌جهانی با دوئل تماشایی برزیل
🆚
مراکش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/persiana_Soccer/23448" target="_blank">📅 18:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23447">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ntHa3ebWQVu7GrGUbZJqjto5ZQW6X0I-bcMozzb7dyn6RsN4bT8qy0QywiiIdLnpte7HRJpjrK79LcdQiKydwTWhKnKCmXvHHxFu_VSKgd_ii4A9AKFVcTovIR1kvgkiEpmMdji6PQgZVmowuHWE4q9uu8OtRb3yWcMtWQ_BxNUJKF1r7sASMLAWFjnDhk2iq9sLgpSc7WurgnsFvSs6m8Jt2YE7DOOwyJkCjv6ztVezLVwEi-m5AcP6XgLE8YM_SlfSAMRSe4w4z7PP6zfxufDG3VY5uqn6dRUb4g4_x9jZgFt-Nukz_Fci-4SDN7dIv7GSMo1magP33RzJU8UUPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/persiana_Soccer/23447" target="_blank">📅 18:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23446">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔵
👤
هایلایتی‌کامل‌از عملکرد درخشان محمد جواد حسین نژاد درفصل‌گذشته‌رقابت‌های‌لیگ برتر روسیه؛ قطعا‌بازگشت محمدجواد حسین نژاد به لیگ‌برتر یکی از بزرگ‌‌ترین بمب‌های تاریخ فوتبال ایران خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/persiana_Soccer/23446" target="_blank">📅 18:22 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23445">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UOpuwLucMeGfM7UnAebsBeWSs5w-fDOxkC0e8hVGCCXvfQCrshlLiuUWTXwoqCnJm2Kx5dL_DjjmbEp85Pxs_qKDtAcd3IyxWfjqf0m3QzBS6OJ9COZ3ESPFDFkv4HNXVKoZZYfCSICKcMOh5RgEf-Y6h_6J2LGSyqKU2b2X5s8Ag0S325CbenrbkJA7IsfQK9b7WbqMKxh3ZfQVKkoxjNWSPK353kGUu4jYzhJvHKSetBOCqXYTaU6F4Eu06ViVU0XGXXX9Btq1uRbwy1SONJYOh2ZfiHTDWtZyLzKy6Qb8W2qnwDqphS53paPlE9or16vKgwWMJ__hymbTuvmySg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🟡
🔵
🔴
👤
طبق شنیده‌های رسانه پرشیانا؛
رضا غندی پور مهاجم‌فصل‌گذشته الوحده امارات به دنبال بازگشت به لیگ‌برتر است و مدیربرنامه های او این بازیکن جوان رو به چهار پنج باشگاه بزرگ ایران پیشنهاد داده است. به احتمال قریب به یقین غندی پور راهی یکی از چهار باشگاه بزرگ ایران میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/persiana_Soccer/23445" target="_blank">📅 18:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23444">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QFTV14vMzcjpl2tfzV54lzj8oNLV-KxGWGJvErTdorhdGssfxraDZifcPmlonJ24vzYcGqSXN671YqcjQUCpzU-6E53HVd-U9VN6RPY4mMgDLpwUpMOzfP13vL_JsXIiSrLz6icqUZfehUAZHkE91KwLB_wHjnZ7SYiOznkBPuQWM3VdgAR8Ydzhavfm-G1mGqDnoja9AQ7NBl_lvbkHZUxjmqzYB4ODkqrFeGnJPWblrmZ78fvEtlt_bLAejAAIvZ_8csl9wHBlvIEHHgDaIVJe6jvRpzPDm-ruMjQ4vpHYFjvOYwlfp6hqC3vTktsCYNP7tZHIkT2w5S0zQsrEFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
سایت اوپتا پیش‌از دیدار ایران و نیوزیلند، شانس پیروزی‌شاگردان‌قلعه‌نویی را ۵۳.۸ درصد اعلام‌کرد. در این آنالیز احتمال برد نیوزیلند ۲۰.۴ درصد اعلام شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/persiana_Soccer/23444" target="_blank">📅 17:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23443">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d6eb70176.mp4?token=CHC-jvhmpGfhImjviKe9LSgh7jX8aYORPLFwzEpf_88OZD5w9Rg6bKoapQi0KE1jXXXqja_vP-3jKH8-rXAsUxkOxd1sLqv5IM7XJZROMwwQusB-Y2cHBZVexMMbqweSZtz85qoG1zdjwnivDobPpr-VTUEZuNVZmqURHYZ-bRxNQSP-HMXJlQ7FLupDQN4Jr993Jz6F_aaBhd4Y-IxjyZtCzQFS3KB2YcFsMbsVy30sheRN-y4z2skQ3s3fc27np7D8LgtbgN-zfzNSiz7QL3deHfFcTv1bRL3PTy7FG7lXHRid7VvdwXuaXkjFJvYfpvSqbjciFoHdJoDqqkJMjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d6eb70176.mp4?token=CHC-jvhmpGfhImjviKe9LSgh7jX8aYORPLFwzEpf_88OZD5w9Rg6bKoapQi0KE1jXXXqja_vP-3jKH8-rXAsUxkOxd1sLqv5IM7XJZROMwwQusB-Y2cHBZVexMMbqweSZtz85qoG1zdjwnivDobPpr-VTUEZuNVZmqURHYZ-bRxNQSP-HMXJlQ7FLupDQN4Jr993Jz6F_aaBhd4Y-IxjyZtCzQFS3KB2YcFsMbsVy30sheRN-y4z2skQ3s3fc27np7D8LgtbgN-zfzNSiz7QL3deHfFcTv1bRL3PTy7FG7lXHRid7VvdwXuaXkjFJvYfpvSqbjciFoHdJoDqqkJMjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
برخی از حواشی مثبت هیجده و جنجالی رقابت های جام جهانی 2026 آمریکا از زبان ابوطالب
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/23443" target="_blank">📅 17:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23442">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q1q5_tkr583yZlcmGNxW5hMW-71q1vvHhWsMjZf6RHv6Co9Hv8RSO0NlUUjUJ3_cogtu5vl-hhK6wCuJJEMV5JCOlTOUw3omxFEgZCCssiq8Y9S8VdW83S0cXfoxndHc9snljmeC_kjwCj4mWv0OSxVPi_FG80CS2BffoyBHH6DIN6pTltFlGmZi2LIIKKLsy8TA37bM463_R9juhASGriqAPepzWqNbV57As0H1KIKKftgqzyGoxwrU7TiLGxbSBOoBjC__irxFPv0XNDRottOZrWfErnvXLOJ-BoFEC_YfNvH-vP54E8A0JLKLRIMmVnhn2OLkk7KvIcIklEQjnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇶🇦
صندوق‌سرمایه‌گذاری قطر اعلام‌کرده که بوعلام خوخی پس‌از گلزنی‌مقابل سوئیس در جام جهانی 3 میلیون‌دلار و جدیدترین‌رولز رویس فانتوم به ارزش 550.000 هزار دلار رو دریافت خواهد کرد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/23442" target="_blank">📅 16:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23441">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KHcHKWeys1V4YFOenaLFIOe5PFhKWBJMXlbAJN34TlzQvbgmUQiWjBGcq7A1zYvD6iePEV1hpyvq9bQ4d66o3yfpbHT6C6Hy82bWIjIdGV7cZ6MKtQhnbgAqHfD7elEETE1fxj1i-WrobG8jzInr-_uE1UNiPE2apP4UqTsXHkLtCxVGYnbWjTJ7HInXfqR-_5Be7zof8kTocceOWkzqr9cwXneliOgfce8TMq30wQy5_m4K0csYaYZXN85WFxQ801YYlzAWqRO9UWlpyhQ8xK5hk1mRjh5oWlPn05g4nLfWr8W5gbP5pEMCReDW95v0Wrhdw7_iRxwiTU_xVUuDEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
گل‌های دیدار امشب دو تیم ملی قطر
🆚
سوئیس در هفته نخست رقابت های جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/persiana_Soccer/23441" target="_blank">📅 16:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23440">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EZ6VTCl2qm61B9Pt6lkcg7Xjq85KGLOAArL6hVwicLhdI90jgJT03f88h8CuHqazQLWXY-7qWH_ZdW98zifQbyDFqVSZzevFehErfCXfMp36TDCnDKsdJTF4rFDEdYvObkSYiLhyTTx6QO23s6hqhpiw2cpigj1pVDfRTHk3xt-hbtDp6MtEIig1os28HB2ftpRY7SFaE8C7PAfRK-CtzqWR4wbgdUAqFgZJiGdKB-vqPuuVjCnjcN9IjmWRaG7Mp9lGfFIJ_QG4h_gmx0HldI6-w-RtPk7Iyu7BeIv2tJeCjtV9OV5gTJTgZn6xcXRMZrTH72lSDmsTX7Z_0epqew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شبکه‌های‌رایگان‌که‌مسابقات لیگ ملت‌های والیبال رو باکیفیت‌بسیار بالا پخش میکنند. امروز حدود یک ساعت دیگ تیم ایران مقابل بلژیک بازی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/persiana_Soccer/23440" target="_blank">📅 16:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23439">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hOBrNbH-sTkwz6UDrgr7cBaJWiAs1gF-o20xt_Y9I9ha9uo0KFC03iDQFwmiUwgPGjwzpu7eE-qnGQOl8rrflw8ONYm55oRl9QrEFoees-xVA0QMh76NlMBmVr8aCZnHm397Ht8QypZiusfwXwVbuEVA26o76HPOHgrKDqgqMVGSmCgCxAtIuG1CCCFyeiB1-d6qsDXgO3O4IaF2OGrpLkSUwMhMev6TRZsiYrZvNCgTvqIXp4JOyHM3lK0y7Cxk6LSPFJvv4HthBayv6SWvLfAuxqD3up_C_99ocjr0jtNkyF-ld0zLRFohnKJDEGqqoeTM44XWnk1CPYpZ2iiloQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
کریستیانو رونالدو ستاره 41 ساله پرتغالی گفته: این‌پاها میلیون‌هادلار و بیش از ۹۰۰ گل ارزش دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/persiana_Soccer/23439" target="_blank">📅 15:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23438">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AuxwslTgB-n7HFkFnf90Gf-Isc4LPl45EppHHcMlYO5H80l0XDve0kysmem_pw0eubyXUT3CWuEScx9H0_s3SgzRCWIl3G-NdPZ4sy2NrtwPtbaHZDIpdZDyShaOPhTqG8C_su61MbxsPXXVPHQRsXT9z90fkSwQbpWg04ILF0burALy6z9f8BM7yGLKRAnqY080cxvREV5xzWVqIsrEAcALaT3plvmzwiejqPH6gibrUaHkYIC3iyC5EL_LYGNxDOtycaDXnk4wRQlJbyN_rk1gum_3_PWXcNQAo9SNHpUZ4-sW01qlp31UKg5v-P73FqUCYLthPiCxxx2aXjJ4rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
پارتنر برخی‌ازبازیکنان‌تیم‌ملی‌برزیل؛ جالبه بدونید کارولین لیما با نیمار جورنیور و ادر میلیتائو هم بوده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/23438" target="_blank">📅 15:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23437">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">▶️
قسمت‌‌‌سوم‌ویژه‌برنامه‌‌فان‌ جدید ابوطالب حسینی برای رقابت های جام جهانی 2026؛ عالیه حتما ببینید. شیت و محمد نصرتی مهمونای این قسمت بودند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/23437" target="_blank">📅 14:42 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23436">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bf1fd42fe.mp4?token=c20C6Jxr-RSf0TLnzEI0rN3nX2vTHfbdnaYM47gHo4xLq-D5ERUdj_Z5ftLjNUnnfctSStzklYAAccaLjOvJiOK0Ck_BYDOmloYmv-mvyImMwJwmusEdyEzTNLgzQP4xjFpWvpHTEJtI3UDiVgfDbBzCjtQJRxMWngnlaBD62M7UEHhAOrWyCIP6MwYxc8eh95riKCKDp9GqOj8fgRy5MZsAt1RS8X6PCKIX1nzISAnPZbHhm9VpgNIuICEPBYy8quYXIuJQI4VUgNzUsWSKq22SHO7XJaNqzglpuo88wAGCTNj9v6Ekn1W_Yh1KyTyX8Whu0yMSEDs6Pd2U7VRwmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bf1fd42fe.mp4?token=c20C6Jxr-RSf0TLnzEI0rN3nX2vTHfbdnaYM47gHo4xLq-D5ERUdj_Z5ftLjNUnnfctSStzklYAAccaLjOvJiOK0Ck_BYDOmloYmv-mvyImMwJwmusEdyEzTNLgzQP4xjFpWvpHTEJtI3UDiVgfDbBzCjtQJRxMWngnlaBD62M7UEHhAOrWyCIP6MwYxc8eh95riKCKDp9GqOj8fgRy5MZsAt1RS8X6PCKIX1nzISAnPZbHhm9VpgNIuICEPBYy8quYXIuJQI4VUgNzUsWSKq22SHO7XJaNqzglpuo88wAGCTNj9v6Ekn1W_Yh1KyTyX8Whu0yMSEDs6Pd2U7VRwmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
وکیل تتلو گفته‌تتلو واسه‌ماه‌محرم درخواست مرخصی کرده که بیاد داخل هیئت‌ها نوحه بخونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/23436" target="_blank">📅 14:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23435">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fddab3a3a.mp4?token=Gde4QN2ciQhgqruk2pDDu6xCIV3QjiIqzjaU52qb-wgdvea0vutjaTYzBkPX4V9TZoaKcaIEUC91ZwfBtycQEHuCew1ziNUA2gIgOy-3zRsCWu0Fy8VT8YkUBZlzZV5QpVIN5wD-a0qiIEFhIOh-GqRL1EK92bbeyW-UrnsaYAWYceAsqlTsSSkHJlFnjxeG5BPOChCn7bpmZWfaFHbq9aFCnWm8gfMIRng6zdAnb1QpKmrsIC8w01yC0rY34VClsR3blkxYK2xaSUJ1z9cULQs-RForVxJRuPZByo-LMAn2OpoL6rwDA_psWTZ_Y_3Up9NMrps76y6MHg6rCqalqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fddab3a3a.mp4?token=Gde4QN2ciQhgqruk2pDDu6xCIV3QjiIqzjaU52qb-wgdvea0vutjaTYzBkPX4V9TZoaKcaIEUC91ZwfBtycQEHuCew1ziNUA2gIgOy-3zRsCWu0Fy8VT8YkUBZlzZV5QpVIN5wD-a0qiIEFhIOh-GqRL1EK92bbeyW-UrnsaYAWYceAsqlTsSSkHJlFnjxeG5BPOChCn7bpmZWfaFHbq9aFCnWm8gfMIRng6zdAnb1QpKmrsIC8w01yC0rY34VClsR3blkxYK2xaSUJ1z9cULQs-RForVxJRuPZByo-LMAn2OpoL6rwDA_psWTZ_Y_3Up9NMrps76y6MHg6rCqalqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رامین رضاییان مدافع راست تیم‌دعوتی امیر قلعه نویی: جرمی‌دوکو؟ من اصلا نمیشناسمش. کی هس؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/23435" target="_blank">📅 14:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23434">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WNS7skMYVSCUtIDYjhvBMVHJoKESltv0XKr-gP42OzUNNlSeJg1y-1z1_S1nreCGJDrv4-D0VxarCpqAPFY5tiawI4amVhvep0XXAvx17xWkTGFRq_3aipbHDaV_aKlXi2Bey64I6fW9xcUZqGcmt5b12jyJ_3vn2OPcNrSv134LT5Y5B2x5AGH9VjX-Kh3z3lR7M1WFCHKin9Vh5mjzkPNLKAGYeZwehSnKKCmxwMLoCPp5DFqBZCTS0kcBGM1ZoScH9VPWvEW83ZiYVxBVaWHh8zVhZq14jYCWoswqg87cd_KWx_Ym0rwmBLRDUUX6AgMkZs_Y9FTclIH3r_LH1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
با اعلام فابریزیو رومانو؛ سران باشگاه آث میلان مذاکرات‌رسمی‌خود را با روبن‌آموریم سرمربی پرتغالی سابق منچستریونایتد آغاز کرده تا درصورت توافق نهایی بااین‌سرمربی جوان قرارداد امضا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/23434" target="_blank">📅 13:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23433">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3586ff8630.mp4?token=IcbMK3ogAUvHkVPV8SMrk6h8CQC9F2CLOe0FVRLgEiY6Yb8MGJ5qp10qUQ_fDOnP5yapOASKMjJGdAIPRXZL0U0grF5kCVpqoMdHyiLDMwlT8O071vsLTXoAhiF3DEe4paiLcXfvhRbKqXHKEO230WHRO9chlDChjTZaBkIikuBvR2fVx5B69FtMq1tZ_cpuNcipnEu34ajH6TRGbADQFmjw__oaUqCz9y2YDkcq0_GemjY2OgsZDfxgzZUdIlnLzFNYsxnOqZZ-Fj24qOIRHnm_X6b-wCwwNPEG_8Ox5G4JcM-UTGUW5lqVB2hj3A5cMCLRsdRQFKMBzwNObitbqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3586ff8630.mp4?token=IcbMK3ogAUvHkVPV8SMrk6h8CQC9F2CLOe0FVRLgEiY6Yb8MGJ5qp10qUQ_fDOnP5yapOASKMjJGdAIPRXZL0U0grF5kCVpqoMdHyiLDMwlT8O071vsLTXoAhiF3DEe4paiLcXfvhRbKqXHKEO230WHRO9chlDChjTZaBkIikuBvR2fVx5B69FtMq1tZ_cpuNcipnEu34ajH6TRGbADQFmjw__oaUqCz9y2YDkcq0_GemjY2OgsZDfxgzZUdIlnLzFNYsxnOqZZ-Fj24qOIRHnm_X6b-wCwwNPEG_8Ox5G4JcM-UTGUW5lqVB2hj3A5cMCLRsdRQFKMBzwNObitbqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
کریستیانو رونالدو ستاره 41 ساله پرتغالی گفته: این‌پاها میلیون‌هادلار و بیش از ۹۰۰ گل ارزش دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/23433" target="_blank">📅 13:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23432">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=iMz2r2UbAJymHHwCo7i2h-rCGPFNYbPPpL6Lb3plPAE21WfLIStXJmDpburF4nEP6E2VmLewWulXgrQrvFPyhTcSFAAweOcFSvsAat-QMlksItU7mRQl6xeppl09bCRlOXzqcaxpcNdpZbYSBcBgDec_R_OXWmE7E6yVE3lhVOQ6UBdd8p_tLt7awtMN3kB2fbvjRuh3hwRl07VWJrFhvlhfyKs7cg2gnrvtKBGiDgrp8iqXiJVU4owGkbS1f5zxt84h97RclknZU3TO5RXFJAjpGZnff-MLSWsPLezxoi01EbFFTiFDqGYefvQ41xWFdM0F-F-Hbrz3DgpfR9CNCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=iMz2r2UbAJymHHwCo7i2h-rCGPFNYbPPpL6Lb3plPAE21WfLIStXJmDpburF4nEP6E2VmLewWulXgrQrvFPyhTcSFAAweOcFSvsAat-QMlksItU7mRQl6xeppl09bCRlOXzqcaxpcNdpZbYSBcBgDec_R_OXWmE7E6yVE3lhVOQ6UBdd8p_tLt7awtMN3kB2fbvjRuh3hwRl07VWJrFhvlhfyKs7cg2gnrvtKBGiDgrp8iqXiJVU4owGkbS1f5zxt84h97RclknZU3TO5RXFJAjpGZnff-MLSWsPLezxoi01EbFFTiFDqGYefvQ41xWFdM0F-F-Hbrz3DgpfR9CNCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
شهردار شهر سیاتل اعلام کرد که ورود پرچم‌های شیر و خورشید ایران برای بازی تیم ملی برابر مصر مجاز است و از ممنوعیت‌فیفا پیروی نخواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/23432" target="_blank">📅 13:07 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23431">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cXyzXSFLLh9SfcpT6OnEsKWLoMf4KNaZgs8EWmNFfyXSD5xlcQ1I3RMliTyBD_AWGmDO-a6hyERp-aT7i4_KErBqhKiC1FqrA45iji_SGI7Mnu8EMV_IjJWl_Deb7vxRR4r9QVj_yUjJY5xCjKfpnKchNaTqfHJu4Odn7tR5Nx_V2A-GJTAA91J2ZakGG4ukT-bePyHBhgep5RpjbCf-wzxBHGUDN2Hom2LMvqXOfBColtUBPfb4LTR6HhwP4m8ulap9xR5zT4chLsmdWkvNlM44FrddReGMvbzF246vEwYwAO4yMDnftrT2jwjeROg97pEuCURYIZI7_Ut1lfDpJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
حرکت‌ جالب‌ و زیبای فیفا برای جام جهانی؛
تیم‌هاییکه‌سابقه قهرمانی در جام جهانی دارن، لوگوی طلایی روی لباسشون‌دارن و تیم‌هایی‌که هنوز قهرمان نشدن با لوگوی ساده وارد زمین مسابقه میشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/23431" target="_blank">📅 13:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23430">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XKWcPK6UeeUUeAWm6WIVzVArEJsJMI6pbEfrYIjj02fv5s1qyWaiEftTF_0sGjckB0xAWvTcIjetk_GC2l7kJkk6JmM9gN1WSdyY_3Bx1rhZw-Lrdo73NBIOsHWbopLo6Vo9ca5XPWUTUoKb-8jPgLNbOP-v8ZGfzTuhqgYy7ekdXPGXpzt2bYAOOdXdBbiobHt0vd0S5YWFonQi4YWCS_mPNk7dvs70eCsmMxI9qieIRrLNe71bsOpVD-BaUi8Z2rrt6Q2lnSmnXE1sQh7q-xPVNUxK2Y3NIEt3nbLlOBg0s9Ru2tTrGyLFQvWkIYwQEsMPvLmNR4yfA72zhIDd3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛طبق‌ اخباردریافتی‌رسانه پرشیانا؛ بعد از مطرح شدن نام جواد نکونام بعنوان سرمربی جدید گل گهر سیرجان؛ مهدی تارتار از مدیریت این باشگاه دلخور شده و به دنبال جدایی از این تیمه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/23430" target="_blank">📅 12:36 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23429">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df3302a4f5.mp4?token=Spyl_BaHjAvsf8bpPeSQxBFS9JWL0Sx9OFzwDFMJnW3RfBFfCMqsK46tiwtexnT4EALhSwDVI8u9gg3DeMup6jOMO925Ipt4wxmNLPqMxKfKBBlN1WC-kQVSMFRDKVyFjnbkducDQpk1Ks3DpLWW6mmjBEjRghXM6iYBjR5T9oLUOPBl6tpB0g8YEkr5RWpoNeNKce_kLtXTqpk5NIgYh-iMu1gR_QoBCPLySQ2o6O6_h6q5Up184xyEM4rFJ__05IFphb_vaNkP0JljzQuaYoZinb6da8FbT3fEhzF7zOHUEveL7CoS_Rxxd3zixCcJcExtxCq7a4wb-XyXViKTKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df3302a4f5.mp4?token=Spyl_BaHjAvsf8bpPeSQxBFS9JWL0Sx9OFzwDFMJnW3RfBFfCMqsK46tiwtexnT4EALhSwDVI8u9gg3DeMup6jOMO925Ipt4wxmNLPqMxKfKBBlN1WC-kQVSMFRDKVyFjnbkducDQpk1Ks3DpLWW6mmjBEjRghXM6iYBjR5T9oLUOPBl6tpB0g8YEkr5RWpoNeNKce_kLtXTqpk5NIgYh-iMu1gR_QoBCPLySQ2o6O6_h6q5Up184xyEM4rFJ__05IFphb_vaNkP0JljzQuaYoZinb6da8FbT3fEhzF7zOHUEveL7CoS_Rxxd3zixCcJcExtxCq7a4wb-XyXViKTKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
شوخی‌های‌ابوطالب‌و‌قیاسی؛یک رولکس که قلعه نوعی بهش وصل‌شده؛ عروس‌دامادها میتونن با پول این شجاع خلیل زاده رو یک فصل داشته باشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/23429" target="_blank">📅 12:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23428">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nT3peM-1W2hi5-1aSCF9h11YHou68S3b3KS-DoguSwS3HPaMIyEfw7D10Kh8PJ3jZZJxCaF6KHgC0D8hCvTEP8JHhXPBERxj4j5r_qHWGFkX4JmjD9YVSJLb1LOzHLAGyuxzvACy_hb6dFswBdjvftpYjDhO4ZkcUELkcg5u2xdXL1CFX9RkfxpDsS6aFm5Qxrmo4okMhMdyBITEERvcAnlvLJvMEjF1jzQvbN-YdmLSrYmwzsjyWJSLkH1zh7XgFnbYJlO_gtvL9QvXlWONZYxyMGGRhYUmf2XN2XO8TVse2T97GKYlivD2IpV7u-zUgG4BAzh1EEWCEW4D7JX3yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛ شروع تقابل‌های جذاب جام‌جهانی با دوئل تماشایی برزیل
🆚
مراکش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/23428" target="_blank">📅 12:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23427">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pv20H-6EAZS8ERW0IBVHkTeb98KxckWPTeFkfR-ZOFnGj30XmJ6ScCddIJP119UIZSeeiV5UemlWrRDZgFlz6nVvqsuJrnFgouSmYcoDNvi3fpUp5pC677y-siAm1GdZNa2TJ416sxdcKH1nqHGBmrpur7yj6nJIn0HUvyMYSbQZgUAihV7YNXEBNu9G2nl87zSElX0_NGzpf7lyqeGsmTs1ms_XkTk4TN1czoKp9XlfhhkQkNVK9IsPFw2vBh9kz-SezngjRYE_e5xHBFALPEWWLE6lUK1mj3xUbFsBFDBqblHaTbNSYu1VPivagqLk_NqFxvPq3bRp7XWQOkmPug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇺
سرمربی‌تیم‌ملی‌استرالیا در حالی تو ترکیب تیمش مقابل‌ترکیه ۶ بازیکن با ۲۳ سال سن یا کمتر به زمین فرستاده‌که‌سرمربی‌ایران در لیست ۲۶ نفره‌اش فقط به ۲ بازیکن از این رنج سنی اعتماد کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/23427" target="_blank">📅 11:53 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23426">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oqj8kQzqvTNNDIeCFkb4r130tPreLQ5YjP0047rM0vgrUSgW1v0a1DDQpDN20Gcvk7rtrZquQq_GNYwEG9oSn_wB0GK5TU009ykDqRjJfBpVLBZIJjRWvUbeM019v-udWfHYLtylSe8yt9BnuZEAaQQTeWilMl6Rwa1IQkD6VSA1WQbtwMPeKQeCMACZq9bQ2qFaO5r3db0YmZR7VMzRqS_vv49wab-3CVSUcDAHMtTaCpRh_zW6TuWgIS6pqCMTJiYGLK6or7AgzP2d8RAaA2xJ0CExsT7uvFVXjUZyCIumFvUJi5SAL60TUURKttbEityUapuz4PYjzNKcWFm8dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ دیمارتزیو: ژوزه مورینیو سرمربی رئال مادرید از پرز خواسته از بین یوشکو گواردیول، ریکاردو کالافیوری و نیکو اشلوتربک‌آلمانی دومدافع رو برای فصل بعد به خدمت بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/23426" target="_blank">📅 11:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23425">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hJpBsZ-T4Q1KT1L0p4-9zh_aI56PxDkVH6gj-CBLI1PQSd-nKXG2y4lTG8ONRrOhxiCr3wJWTvy5vmjxW2912Wqsn1799xHfU3wIYPOWkiTdU_K5ZpXfr1OFKL2RlEeF-8NFe7LmwztN6kuk5OpV-UxpnPCd7HLoW_vzBubQG4DnEz200Ap2LihD9tLxMB4GoTssx9En8v0jIbUenuTjpWiAZozpC07_xQAKIKfki5nNyaye_c_teQUuiYeeX_wMh4IvejsiqzMtvs__masClhRB8lSBe9zwkDE81bSB0WkCfXhiAMIC6vj_aq0cjT6IuSpwe02WFs05rNIjKVgn_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
⚫️
#تکمیلی؛ روبرتو مانچینی طلب 15 میلیون یورویی‌اش از السد قطر روبخشید و رسما قراردادش رو با این باشگاه فسخ کرد تا ایتالیا رو در یورو آینده به جایگاه‌اصلی‌اش برسونه. مانچینی در یورو 2020 ایتالیا به قهرمانی تاریخی این رقابت ها رسونده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/23425" target="_blank">📅 11:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23424">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PUSa16lCEOk1qCaa6ykryCBH8ZEoaAe8PxybzJhX-wOIKZDBSsBPCHrHagh9IEO_Upbu2FZhvUv9PLMS1tlrNWUk-wSZw31A0h3vOhbgOj6txnKllolbuOe9XWGme8cDeXhcYv6Lc_-vMLg4uWCxu62O6GK5gwaUoovSJBtUn1Yxsdu_UFaHN2hQD62kkHbBOJmvbUmqm5C_85hhl2xY6UEppU6zvk7VsIKg0uGB7PWKMdGVYdiYsgCrwh1B5D5z-QJtzJ8ogS0ToKaxM3Pbp8JeLfK6VTxAxPzmcOZ63NUOuX5xUyP5r-NXfDxR1obrMv5q5ozUpd1zGw6wbTOb_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
پارتنر آقای گابریل مارتینلی وینگر آرسنال و تیم ملی برزیل که دیشب فرصت بازی بهش نرسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/23424" target="_blank">📅 11:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23423">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fJnkcegsQ0iI1QMK3_bSfr57ZgDU1I0Wz7UPe8w5JlNUSAWx0qXbVhJP2xShViwTRaoUFa66kW5gIZcbEEH7bmXWdBn-TGMOV_Qn4HBVkj2qvqec3Z-rFahYi6jOV9k9f6hJmrar9HxiaKRaz5Ji4wYFnLyedJSxdlBDtGWJIVQCJc12iJccQkzU2mKEKnYTQRHAN9sQrzn2_96SdMeEW2uWP6fSlqetISADaFcCBwLXrhMF64YoYXEExLYq0sOiyfLxxI-UYFV9bVRUXItHJR7kOuv8Tpz4RJcZ4me7XDijerwAkdV3i6KMiA4tGmoH-fG0lWPw6byj7YN85GghnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">MelBet | جایی برای پیش‌بینی‌های هوشمندانه
درجام‌جهانی 2026 هوشمندانه قدم بردارید و روی پلتفرمی با اعتبار جهانی پیش‌بینی کنید!
🔥
امکان شارژ کارت به کارت و هات ووچر
اسپانسر رسمی جام جهانی
پشتیبانی از زبان فارسی و کامل‌ترین برنامه موبایل
قرعه‌کشی و آفرهای ویژه جام جهانی
✅
حرفه‌ای،مطمئن و درکلاس جهانی پیشبینی کنید!
📌
برای ورود به سایت فیلترشکن خود را خاموش کنید!
‌
🌐
Link
🔜
MelBet1.net
🌐
‌ Link
🔜
MelBet1.net</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/23423" target="_blank">📅 11:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23422">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dk_CtsXgLDRSWqoA_KZqbf61wL_UEJ1B0Npf3n9WPrAyTRC4B0JwFbtGtf_BPRrky4jvYbxtwD-ndIoI642BXTnCHantqVST9vnIqJqvxipwM26nf-X6_8THMD6jc5Qu9dGVMgsxglvZH-xnOAo281ZL5HgR8bPY7Qo7-151LooGAsT0Vs2VnK-AFw076-8Y-vhRZWCaUolf-3LEzCrq5qE-0HGhRNoL2Sq04jnXPJ4sN2FTZWvGKUd8W7I1uqewQrF9lYOpclXM85teJ8NqK8Cp7nNZOZiACvpSFqSSnTWTnT7cXJGhwCl-ToZsSDSFprgTbw5ZBlvwO6BA2hZCEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🔴
طبق شنید‌های موثق رسانه پرشیانا از نزدیکان کسری طاهری؛ روز سه شنبه کسری طاهری بایکی‌از دو تیم استقلال‌ و پرسپولیس قراردادش رو امضا خواهد کرد اما فعلا رسمی منتشر نخواهد شد. همون روز سه شنبه ببنده درجا همینجا میگیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/23422" target="_blank">📅 11:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23421">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jZPF-FXz6Q_OgEXLmnwgD9fHzlvfeilPFEJ3QDrQgTM5L4ZiIFTkg6EvP_QCloTIoIllg969BOKhTCcgTjN6s9h2lPT5KeATMTZqkyKcGgqof3zYGTIF_id99-9c7YsnnEyAQRjXsquRfbGsBhnRVhDxJL9CF-_-Z0YSu0q108Al07rGBlQrCwT8DsIl4Bxm8hvDYHYm_lQGUS2tJwyEmJ4KGdxSxDzzEgNo2yx-3Zk0WR4nIqvLjPVo99Aa5FrzY-zrHdTPv-nb49R7D4-R-z-w4O5pGdaqiqth2QVGPqFitoZW5gapCI1_1Q-qLSfZf1cK7jPEAf5IausYJJXKvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول گروه C و D رقابت های جام جهانی در پایان هفته نخست؛ استرالیا قاطع و دو هیچ ترکیه رو شکست داد. اسکاتلند هائیتی رو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/23421" target="_blank">📅 10:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23419">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qssFyysYyN25LumCaTdn3aub9iF3luyORMMhZoiSGR1BozCDaWg28bz9ogJON4opJok2HzgqvtZU0-VJuXwLo7YjISCR06E5AmhBjy9XW1PazFAGQ3BAv1wlCgdkzQG94jrUqLf2fPIpUmWDFJNOnovGRGEWbjmG11vpYav6ty-OcAg2bHTpkGsQi3HH3HRefq-qyfxWC5A0Td3B6cxl2laAy9GhOwVm6991ZMmCwsp6URtATXzUNIAxFo6P62_zknn-RiwJIyh4YZhFNgS1AkfjmX65HGDoSHdaf_C9FvWtvbsfzRREelPDWFNjNls00X4YZofH2zCtr8SWdc6JSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vLTY0rKNHYcQoQ4xwwhnRkIAVf2rpUHf0ZICAFlhs8TU_jjg47TV1qKI5EQKEJTpzzinQwFEH2eRRjNrxGMVEaahg16YuZt-c8ZlCJ9qnK7HxffR2L0dw08lLX_26yhyTyCZkOlFSgLPPrn_sWHEnZO9tgBCvfQS9IJapnZKBwfxdYF22Ks8Houcalz1gfD0ZsbqD2ufA6E8hDBCl4StXKf6-J1xU7hHawNPE1bGqXKK0YYdvAK_rVxslAHMRSjzBI2udUVzjwC5bwqSu2fAJ4Z_vg9qDTe_QhXYEYvUTrIvd4kCTudw17jnZz_min1-WgW_BsL8tqM78jbq5uSwsw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
اشرف حکیمی کاپیتان مراکش: اعتراف میکنم که در نیمه‌اول روی اون‌صحنه باید اخراج میشدم که شانس بامن‌یاربود و داور ندید. لیاقت‌پیروزی در این بازی رو داشتیم. هیچ موقعیتی به حریف ندادیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/23419" target="_blank">📅 10:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23417">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KaOYij-SM4BVWqZIh9Li34bnee_yBr-OOR02hVPE4yMLpk63ABSbKgJbXnQ0BG2yP_iN_BDfirm9geMOlSqPginrTEX9fgWuJrt0ab8OwfZ3Wy8gC36NfJsaZjP9CJZaFoBp7P8IWuVhpY-0YSnGW1Xlmrn_8aYz9DtZKa6Zu8iJaZQ5DIRtIRXBPm8apEBT31ldB-ABY8h0tO0nA8kf0mgqPIeIpKqxPfemV1b36mnx3xmA5v3qK68myExN8iT54AEXAtXUPglFQfg6UFRZNvLgZonajGUVbrqInu5gTQu0ofcvU0s0rpwcQW8WSRyqmsa1y6t-MHk7JxYis8YtEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc2df20eed.mp4?token=l_4CJ_0p3UWKyavZNF7UtWz2yDPQiBsfStWHOVpb3jRJk1o_g4buYXwRHS90H9sKULqVZnHdFTcsEPsE1aEyo3yiq4n0JcYhetBUL0P8HOdKCoFU7pw4hKLDTvmnCPU6lS9vV57A7R8PGhdavC241KVZ_WImrG8fS_49Q8hlKCCGqqZ63TOwO9CnglHYKKn3ts1doTCPicIVMJzI2zHSyJ6_3Rb3xQyiGQHBId6YuZlEm5L3qv28_ePUU4cIABAAMmf2uilSlMDbbX39zsZpieIQ0XML3Fx6c09HQVd2uE-tLrkFbdnTPuoxs9IORUI0VhBAvnCbpNvnysuYy2ZL_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc2df20eed.mp4?token=l_4CJ_0p3UWKyavZNF7UtWz2yDPQiBsfStWHOVpb3jRJk1o_g4buYXwRHS90H9sKULqVZnHdFTcsEPsE1aEyo3yiq4n0JcYhetBUL0P8HOdKCoFU7pw4hKLDTvmnCPU6lS9vV57A7R8PGhdavC241KVZ_WImrG8fS_49Q8hlKCCGqqZ63TOwO9CnglHYKKn3ts1doTCPicIVMJzI2zHSyJ6_3Rb3xQyiGQHBId6YuZlEm5L3qv28_ePUU4cIABAAMmf2uilSlMDbbX39zsZpieIQ0XML3Fx6c09HQVd2uE-tLrkFbdnTPuoxs9IORUI0VhBAvnCbpNvnysuYy2ZL_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
برونا بیانکاردی پارتنر فعلی نیمار جونیور و کارولین لیما اکس میلیتائو در ورزشگاه بازی دیشب برزیل
🆚
مراکش درهفته‌اول رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/23417" target="_blank">📅 10:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23416">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cJ76wRNyZZXDHwqAcjBUxjrSuZx2sDGaFpUrVtjhconreMFVKbYovoGEHNy5ZVI6mS1hjiF3NUAus2pJFRKWlvQysCTCl87LhOxFCZqJk_XEIhLFBAD8cK39LDrfBkE-mdbY9UA5FOzTOMArunao0_YN0h73djhVYDlEosLb94hi3AJBGNmPl1J-1d9If-kNMiByjcLyM_68smv3yBtGE70iJm4oBtolBqOrkRyergGFP80ooYSSRteANbG039wJIugRnjx5FM29DWvRkXUMpTXeUTK8cMcw8B_bFM-vLgGJF9nQHmp3NasFhwg_KSwUUECWXM2hL3oMQB-M7c-qWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
ازکهکشان‌اومد زمین بی‌بال پرواز؛ مثل شهاب از اسمون اومد با یه راز؛ خرید اونو قصه‌مون شد آغاز، امیر10؛ ابر قهرمان جدید ایران و جهان
😍
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/23416" target="_blank">📅 09:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23415">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/260d53aa6f.mp4?token=Xhe2KFwrk3wa83TwHRQtMsLKhIQEznQyI18FVKlrtXBrbek0xSEHlY_MndeugW2UswGhvjm1jQ7YjqGSAkv6EmfFctxqju08eFGlfqA_Xdisw9rEuAy2oWe8_5ZJvf_NMsiOdgj8gZe9wB8AVyXwvSDMYzDO-gCFjJRpgLQrpDzhQSjInLQSC7LamM6DL23g5ReTjDUms7GHSxKNRzp6UG2dqccb52Yl7_-H_24zUx78-a-_hW-qLwbwdQlgaWXByj3cPRyVcXd73SkKqJvagN1Savhz2-muHuUIK-KaVASfHoJ84fiD8_kHb6qUTm_uqYEmWjXSpHJvAyVosIbF0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/260d53aa6f.mp4?token=Xhe2KFwrk3wa83TwHRQtMsLKhIQEznQyI18FVKlrtXBrbek0xSEHlY_MndeugW2UswGhvjm1jQ7YjqGSAkv6EmfFctxqju08eFGlfqA_Xdisw9rEuAy2oWe8_5ZJvf_NMsiOdgj8gZe9wB8AVyXwvSDMYzDO-gCFjJRpgLQrpDzhQSjInLQSC7LamM6DL23g5ReTjDUms7GHSxKNRzp6UG2dqccb52Yl7_-H_24zUx78-a-_hW-qLwbwdQlgaWXByj3cPRyVcXd73SkKqJvagN1Savhz2-muHuUIK-KaVASfHoJ84fiD8_kHb6qUTm_uqYEmWjXSpHJvAyVosIbF0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نگاه عجیب ویکتوریا همسر دیوید بکهام به تام کروز و حرکت عجیب‌ ترشون؛ درسته ما فرهنگمون خیلی متفاوته ولی‌همچین‌چیزایی دیگه مورد داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/23415" target="_blank">📅 09:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23414">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KecstCP7wchN0YYiNNjBquYY2v2-WCpgxe84cIbLuQSkeerxV6nfmyWh40vbk4v3qJgRS0V5sUurtnfAsPLV7JnnvYfJL6qbb-dBLx6L0SUJacFowW0hnyLd2tuMf_9_vb5ESKg2RMCHfE8TU1Pc7Bw4UXBa_J7VvF8ZOgpQm7zqR3_NnsERrD5fORRviw8DviwACO9sYTtXQ4ex3NctVW9IIRi8L0tce1_8W_-DM2F1ONasof1gU5YSq1-7ZsPnaMWdCsfBcSCtzvy_EEGZNRK4ytC-_X17Js9j5gU9HsoFmGdnz0fD9pZBZdVm5n2kFzldPVfn-f43lw70F1pYvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇷
درحاشیه‌تمرینات‌دیروز؛ بازیکن‌کره‌جنوبی داشت وسط تمرین یواشکی از گوشیش استفاده می‌کرد که یه‌نفر از کادرفنی این‌تیم اومد گوشیشو ازش گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/23414" target="_blank">📅 09:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23413">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da531b194d.mp4?token=qxfvLlJQ5u4Tr_sn_cA_8TH9-zQm-NOXbTdS3m4QBneInfS3r4e3_Sgt2OQszE74JzmfNgKVtpGdi7f45RT_m6jJakYGIGqMVIwAdXKf-9QbHjYodXpz5jtVlmM59oiqQtnS1jWnI9qPlm1kQsXIKlt9xUMpeTWK9xGQtEH4UDL-eO4D2JtHzvwEqZB2SSIv4Idpy9tvmpbWlQLibqEDyNZU-dAQtwattr0hbkMDNhC2oTXTl1EIgmmPR-w5HKAVwsSxOW-WXXx6g5VR8bE-fFPeL_C0-nwUZ1vmOyYqGr-3oxw_-4mD5239kYVbN1pQwcoQKtxDlor2waqa_Cq_XA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da531b194d.mp4?token=qxfvLlJQ5u4Tr_sn_cA_8TH9-zQm-NOXbTdS3m4QBneInfS3r4e3_Sgt2OQszE74JzmfNgKVtpGdi7f45RT_m6jJakYGIGqMVIwAdXKf-9QbHjYodXpz5jtVlmM59oiqQtnS1jWnI9qPlm1kQsXIKlt9xUMpeTWK9xGQtEH4UDL-eO4D2JtHzvwEqZB2SSIv4Idpy9tvmpbWlQLibqEDyNZU-dAQtwattr0hbkMDNhC2oTXTl1EIgmmPR-w5HKAVwsSxOW-WXXx6g5VR8bE-fFPeL_C0-nwUZ1vmOyYqGr-3oxw_-4mD5239kYVbN1pQwcoQKtxDlor2waqa_Cq_XA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های شیت‌رضایی مدافع‌سابق پرسپولیس در گفتگو با ابوطالب درباره حرکت منشوری‌اش در بازی پرسپولیس - داماش گیلان: نقره داغ شدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/23413" target="_blank">📅 04:37 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23412">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TxML-Rr6LTUHxmafTq_UkqfoVbzqZTS0Tjm_QFFHIhU5jvrkOWF4Dt_plel8O32A2mYJUShK21_d0diCs2XodNOXxm8qIvjmKi_XT9Y2nGGXdw1uSR0gDQx7y3cXNh6uQ_nRRbXNxdP4g_etvnDkfBrzlT8hJ5poGlcCCtw1IFYJEfDyWMONOXW6rNSmkfQQbfcUAIKUtHqzktp_FGpJ6IH239jFPuQKWO-fkKdf8NCB2XB9gdhptOWyx9nf4GuCiuyroR1gSXIOvt2BrIb6ELnAQr8l38Uet6jX6-mjBC1mp5eIOYqkiZY2AROqwQ3lMLft5eMq4-frLfiKX2O0-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌جام‌جهانی|توقف‌شاگردان کارلتو مقابل مراکشی‌ها درگام نخست؛ یاران حکیمی نشون دادند خیلی حرف‌ها برای گفتن در این جام جهانی دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/23412" target="_blank">📅 03:53 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23411">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">▶️
گل‌های دیدار امشب دو تیم ملی برزیل - مراکش در هفته اول رقابت‌های جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/23411" target="_blank">📅 03:47 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23410">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">✅
هفته‌اول‌جام‌جهانی|توقف‌شاگردان کارلتو مقابل مراکشی‌ها درگام نخست؛ یاران حکیمی نشون دادند خیلی حرف‌ها برای گفتن در این جام جهانی دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/23410" target="_blank">📅 03:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23409">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hi0793k1ssFSmpgp8Q_u1DGi9K5lIGII2jDif3z7RxwmTbI2on-0uLSRA0Ay1LgfCG1a-ig0mFaAJ76HefiaOdw0fmOeO1GXAS75zKJ9bjoBIQ_VSFtYLDgXjavSPaLexyDPYHMl_f3ilCof0wnkosCWawvoKMRjgXq9A2qHgwGPlbAtXRV37hNMRVRazzwdxfhxtzNmDT1TmPXOv5pWoZ1nGkgCXHnNNNrxlYU0xk-SW7PS0ihBo1lklNHIgSAjbkbFu8eEQhqo1XWFebCb_cl5ezzYl3q3xEHZZYa3J0Q450T8WmJl4QZ4ap5YRVC_5I4yKN13vwLMgCWWHWvM4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌جام‌جهانی؛ شماتیک ترکیب دوتیم ملی برزیل مراکش؛ ساعت 01:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/23409" target="_blank">📅 03:37 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23408">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/858efb6719.mp4?token=BBSS_hlWkmEMRIWdoDcDVbeMBVqxRFrXqWRI3IIz6f76A3_LzO-GyY0X6h_zWxnaEYp3f9B1cS2do4ylWJs6ubgbTcC7mjz0mOJsZcnBfcfoKateMC4zIywvMhC8LNt7oD2-ho390M30yTcn_KDSn4z_RBXDc9cskHX0ZJmsuOLLBW1C-xxX0XVp4NURtWidUAO-mv29zVHEwumTYzo558P9CtZVYV5kgGKryPXdOgn-5KR-bhVZwU282ozTyRPorUtEb7SmryPTeuC8Q90R4Ik1jyZm4cr9UwSqKCN3aktv7O1vcNqI4XpUcDZhIV5WfaLdJ3MxYhbGFoVyfmP8pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/858efb6719.mp4?token=BBSS_hlWkmEMRIWdoDcDVbeMBVqxRFrXqWRI3IIz6f76A3_LzO-GyY0X6h_zWxnaEYp3f9B1cS2do4ylWJs6ubgbTcC7mjz0mOJsZcnBfcfoKateMC4zIywvMhC8LNt7oD2-ho390M30yTcn_KDSn4z_RBXDc9cskHX0ZJmsuOLLBW1C-xxX0XVp4NURtWidUAO-mv29zVHEwumTYzo558P9CtZVYV5kgGKryPXdOgn-5KR-bhVZwU282ozTyRPorUtEb7SmryPTeuC8Q90R4Ik1jyZm4cr9UwSqKCN3aktv7O1vcNqI4XpUcDZhIV5WfaLdJ3MxYhbGFoVyfmP8pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
ابوطالب حسینی تو برنامه امشبش به این شکل جواب محمد حسین مثیاقی رو داد: برو بمیر بابا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/23408" target="_blank">📅 01:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23406">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GcRLM-qHVPdvvf15ZhQFkfeH7iETB4CVDcKYtTF138Xf1waeaA60r1D_bovzLb03ciFEetQTRFj9HY_6A9XkbCSYuWFskSpODaz9Z7zb1VGMeWigPiR3_hEX_sf3I-RWHiST4oINNBpA4wKxhNJ-AMOhu6Rhb2g-VKCcD4opG4CkhwL8drE2xAyOTIAX6QHam2ZpkdCDqw6qo5cGTFbaE7tjWWwCBfyvdDot5pMWiaO9IsOvR90u7_y031leHNttJzUgi4CzLX-TE94_76b69OvmGxkZve-M-U3VArVzHzMHLq22bkRvwDA5MGR-I_lWGDNUelcVF3xt0IN6vlFoSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛
شروع تقابل‌های جذاب جام‌جهانی با دوئل تماشایی برزیل
🆚
مراکش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/23406" target="_blank">📅 01:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23405">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lte3F0qMI_IYeRFiu9TCFaQ9kW8-IAen6oZabfBZq8HAazQlmixUtJsKsTE1MFtuRDCQ7BxGbmz8Cx8QMDXc2Sy6N8wI3jwW_UMFGNYrDsGE5_zSPPkoO4av9dse0XdgGpn5acnOSlSvAlozHEnpry7-0igKFEACB8AWGVK-xbeAG5-T-UTiiEbwOqGgY8c8Ue0XcmpUycNChO9YTH_SY4T0fZQPqMMv8MWB4p7k5uFw9QA8E6fZTkZG-lMa2HxWxANDSZ54--FdgKG4wusjD-SC_S0rbjkx4xCpfAjYq76M8ef5OW_4LU82kydkrFcg6gzSxRQ4TcCtw5F06V58-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌‌دیروز؛
از برد آمریکا با درخشش بالوگان تا اولین امتیاز قطری‌ها در تاریخ جام‌جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/23405" target="_blank">📅 01:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23401">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WOnuKuARD8epYu8oXrvhLFHBC_DyJIcsEJD8uV8GOp3zMte7v3zYSIG9s3IkXAjf-gueMQ-sS_wNbT7LOzP41nU0pePHTshpQcJ1CIUummkMFrDXNJSuyS5uVMKumDoqJ9vLMClUlpef0Kz0XCfmVLbd5ImYNedGTtrzFWtjmDz80MZdChj3_NhQNtOKnuVQcr49Nj6uBYE7a_5jw-AvkltDe4QMUC2ltSCIOWsp910zVm9xeRaqUoBJraPZMrgxFdpUS7spPnD9BnH7B498S4fd9AQx1WmIuyyFj5zEE-cHmTgxoMFFskC8cO2XYC8zD7zItolku-Oe1B87Vs5oRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رسانه اسپورت ترکیه: کادر فنی کایسری اسپور نام پنج بازیکن رو در لیست مازاد و فروش کایسری اسپور قرارداده‌اند که نام سیدمجید حسینی مدافع 29 ساله این باشگاه نیز در این لیست دیده میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/23401" target="_blank">📅 01:22 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23400">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27db8eea25.mp4?token=o89kbguj958K4nJx58DFBw33qeoU-_BzQrmraJgzLCZdhA8yn7RAwSdsPXQmFVGSvqriTo49ktBqvtrpeH43be-RPgaANYNrRU0phZJaxsJv-cFmyXTmOqqIEt4ND9MdsPo8ZfvJUhSkbt9C34rn59JgFwyL9Ia0b7hLhmcJMqA7NI6Mkw9C2NiJi4YtOug0V-ehj7QD2kXrkUeA3Mu-0qAwjxm3Opm_yTdw3H65t_ecTVHqdpGKVHnuENVwcNBRU_-0oESGIG0xVkDFMQo2sxFFYBArjMAd79pb9nCmGKitM0sQBHxlURHUAEWmR7pyWh52BBYfqSXI3wn8solxQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27db8eea25.mp4?token=o89kbguj958K4nJx58DFBw33qeoU-_BzQrmraJgzLCZdhA8yn7RAwSdsPXQmFVGSvqriTo49ktBqvtrpeH43be-RPgaANYNrRU0phZJaxsJv-cFmyXTmOqqIEt4ND9MdsPo8ZfvJUhSkbt9C34rn59JgFwyL9Ia0b7hLhmcJMqA7NI6Mkw9C2NiJi4YtOug0V-ehj7QD2kXrkUeA3Mu-0qAwjxm3Opm_yTdw3H65t_ecTVHqdpGKVHnuENVwcNBRU_-0oESGIG0xVkDFMQo2sxFFYBArjMAd79pb9nCmGKitM0sQBHxlURHUAEWmR7pyWh52BBYfqSXI3wn8solxQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های شیت‌رضایی مدافع‌سابق پرسپولیس در گفتگو با ابوطالب درباره حرکت منشوری‌اش در بازی پرسپولیس - داماش گیلان: نقره داغ شدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/23400" target="_blank">📅 01:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23399">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">✅
رتبه‌بندی‌کشورهایی که دارای زیبا ترین زنان دنیا هستن؛ ترکیه با اختلاف در صدر جدول قرار گرفت.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/23399" target="_blank">📅 01:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23398">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RDMthpVReObAAKjOoHQcczYFFLimLiKNKTD64m2D-IVFc6HdL_nQGKZ4aAEV6qHnDt75hz-XfxFinoMBwP7rJW0g0bNneqs-_pZFvTbvio1Cr9Z-bieX-xzRap8MovVI0CbkM1rCJ3UOQqGDjeZ-77gasU1p6oPtrhakec4WY_mNqdsJ4yT-lAn8IAXaeHZzK640jo4ZWGd__lPk7MXYW9CHBMsy1UURQlMbC8BKt9bycaEvsG0um-3nR9xSKxIDjU2Qf5AgTMNt__NTtfjzQYIVb0_Lbts57U57AEM55_TB4Nf0cFouEpnjYaZ0gN0_yc7jubsSWxVSMzCiK6dtfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی‌رسانه‌پرشیانا از زبان کسری طاهری مهاجم‌روبین‌کازان:مدیربرنامه‌هام با دو باشگاه استقلال و پرسپولیس جلساتی برگزار کرده‌اند. بزودی تکلیف نهایی ام برای فصل بعد  مشخص خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/23398" target="_blank">📅 00:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23397">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c16a032b2.mp4?token=kxFmnd4SWePPf9sI2e-c8UHWZWM8PZs4DBMgMGjJFJXvu_RXzDYR4qMb2pBtuaBra39IwujOtT8y5e8p3KQG331-z_pSK_7uNW4AkeeKYtMTCZIV4vrEmqpuKrCgETV6-_Eh-n0Jo_ifSvYZrvaSCf-srzxKlXYP_WwHwp3JBOKiHpRg0ijy433Kpf8txKczLCURgTYfsGzH8mjuexGl6fCXUA7riCUzdySK25_id9cKhVKpGcWxhLbhFpJtaVLELNrVTHCG0JAflBvP88AYKwqK6ZRVyDciAnDKuLmLPTG8TtzXaZh_NSGawyOUv4EQM2svt2mp69sxcld4Jib9UWXrpBfWE-P5lVm80kxcVj2YAeD4X_UHNaiFSK88GRGAiGX8aFQmReaeMFCOczPdgd-5viwKfxEedpf1awFGCENqRKLyisaYOfEd0uCXtuHO4IZfvVQ2PlnSPQpOBNekgxH2fgD14jrM6qEchK6tgD9-xoC4Y0UnZSqglZ7Cs-yz3qZx8ZyTvSov9GXrlsX-eIod1_OE8jU7yOH5J9OI-b_5mqJGXlU3sjBv_beKNFbZNbfXomF-aEwVpSlbaWkoYS-9Vwsgc96Mi6_TsiAD3odPAEGlIDV2ARR4f-g4CV_wsmABjGBnCjC73Dp0UO4Dm2DJi14yAs2v2_1IIRzUd0U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c16a032b2.mp4?token=kxFmnd4SWePPf9sI2e-c8UHWZWM8PZs4DBMgMGjJFJXvu_RXzDYR4qMb2pBtuaBra39IwujOtT8y5e8p3KQG331-z_pSK_7uNW4AkeeKYtMTCZIV4vrEmqpuKrCgETV6-_Eh-n0Jo_ifSvYZrvaSCf-srzxKlXYP_WwHwp3JBOKiHpRg0ijy433Kpf8txKczLCURgTYfsGzH8mjuexGl6fCXUA7riCUzdySK25_id9cKhVKpGcWxhLbhFpJtaVLELNrVTHCG0JAflBvP88AYKwqK6ZRVyDciAnDKuLmLPTG8TtzXaZh_NSGawyOUv4EQM2svt2mp69sxcld4Jib9UWXrpBfWE-P5lVm80kxcVj2YAeD4X_UHNaiFSK88GRGAiGX8aFQmReaeMFCOczPdgd-5viwKfxEedpf1awFGCENqRKLyisaYOfEd0uCXtuHO4IZfvVQ2PlnSPQpOBNekgxH2fgD14jrM6qEchK6tgD9-xoC4Y0UnZSqglZ7Cs-yz3qZx8ZyTvSov9GXrlsX-eIod1_OE8jU7yOH5J9OI-b_5mqJGXlU3sjBv_beKNFbZNbfXomF-aEwVpSlbaWkoYS-9Vwsgc96Mi6_TsiAD3odPAEGlIDV2ARR4f-g4CV_wsmABjGBnCjC73Dp0UO4Dm2DJi14yAs2v2_1IIRzUd0U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته‌اول‌جام‌جهانی؛دشت‌یک‌امتیازی و ارزشمند نماینده آسیا مقابل تیم پرقدرت سوئیس در واپسین دقایق بازی؛ لوپتگی نماینده اروپا رو متوقف کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/23397" target="_blank">📅 00:47 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23396">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05ba749a0b.mp4?token=mI5w4xe0xrCOqLZ4ZfD-tn-Wxn7lfr5IXRZh7OoTKHU2-2a-VkPyqrKlOLYuPbKhAQO8qZIG1JCJ1wG75eQYgcUnxRmCnsZt1W8HQxfo_Gs7yhDH0L9z-SxY4h4y57vHDZkW6j5CTxQ3uzreaha2_Xuly-VzbB1AiHzM7Cm3u--zjWO2oev2mwpAMXju2qCbRP42ByYiD-HHY1H1oRVQwCReC7qpiGJy4TMI74Bt6Irn_oruWnlgufSH_6C0Rc8vVQw6HNT0ZZJbRoCZVGh5hFazbdxy6r81B2RYghmmUK95TgT5btedr3j6sht6rU3hpMoDdoQNw3ykuwdxU46I5GBeMhnIEm2qomJ-4oSSQ9VC8vgVykiTHhhXg05qpx69MjABNCAsa3heX02UX3BK_Jmz4FjR81uNPeIDdynjCXF3qoCLulDXOVNhXSPG29Ns8nqjnNESAehhLjXlbAyb9YO-R5Oq0mTs9wCCwqmzJmBn-3mMuOUVyKp-qhXh8tyZLaMqZ7C0f8Q78c8i-ccmLIvMgzltQQDzc8LraW8MoEuF84tEtaiHBeV3uR9dXdFH4g7UUL_TFbwaRFY9DzxcIJPGqh2GlF5mmgw7xqL1K3sdncY_gtJhARfly4kmLvN6PyE1LMIGMMoO1QQzyUn47ZRi8J7a3l0wr1F4VG4fO6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05ba749a0b.mp4?token=mI5w4xe0xrCOqLZ4ZfD-tn-Wxn7lfr5IXRZh7OoTKHU2-2a-VkPyqrKlOLYuPbKhAQO8qZIG1JCJ1wG75eQYgcUnxRmCnsZt1W8HQxfo_Gs7yhDH0L9z-SxY4h4y57vHDZkW6j5CTxQ3uzreaha2_Xuly-VzbB1AiHzM7Cm3u--zjWO2oev2mwpAMXju2qCbRP42ByYiD-HHY1H1oRVQwCReC7qpiGJy4TMI74Bt6Irn_oruWnlgufSH_6C0Rc8vVQw6HNT0ZZJbRoCZVGh5hFazbdxy6r81B2RYghmmUK95TgT5btedr3j6sht6rU3hpMoDdoQNw3ykuwdxU46I5GBeMhnIEm2qomJ-4oSSQ9VC8vgVykiTHhhXg05qpx69MjABNCAsa3heX02UX3BK_Jmz4FjR81uNPeIDdynjCXF3qoCLulDXOVNhXSPG29Ns8nqjnNESAehhLjXlbAyb9YO-R5Oq0mTs9wCCwqmzJmBn-3mMuOUVyKp-qhXh8tyZLaMqZ7C0f8Q78c8i-ccmLIvMgzltQQDzc8LraW8MoEuF84tEtaiHBeV3uR9dXdFH4g7UUL_TFbwaRFY9DzxcIJPGqh2GlF5mmgw7xqL1K3sdncY_gtJhARfly4kmLvN6PyE1LMIGMMoO1QQzyUn47ZRi8J7a3l0wr1F4VG4fO6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔴
#تکمیلی؛طبق‌پیگیری‌های‌پرشیانا؛ رقمی که استقلال برای‌عقدقرارداد چهار ساله با کسری طاهری مهاجم 19 ساله روبین‌کازان پیشنهاد داده. فصل اول 55 میلیارد تومانه و در فصول بعد سالانه 35 درصد این مبلغ افزایش پیدا میکنه. رقم پرسپولیسی ها یه مقدار کمتر از این رقم باشگاه…</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/23396" target="_blank">📅 00:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23395">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SqURnhJSCNUqWqNaQQkKbZELnmY4IMBnW2GvkIbB2xWdrqkTebAiuFi84YTaImXul3kQ2PqEMQiimpIKZsLVIHUd_tlAaYCG1XdP-Uu7mshu7DzNH9EXy9BpzaFo9b764A6VP0DTOClRLruROz0TKp1Mo4Ud8dWSVOj5D-dpZIxR8yyQvdVrmK-s4-lr0uuaq9Bdkx7t3FW6HvPekp1pOr2EW_BsmL06eSJ9W5mimYRvMdfjzs3JCt-skZxK_NdyWZGbAlSy67vF0HUPFJd84AIzt3ho6ebjSh0Q0iY2JudotkEeURKXjtCAYaH0ximQ2Xp8t0cPaTgHCRPDVj_AGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته اول جام جهانی 2026؛ شماتیک ترکیب دو تیم ملی قطر
🆚
سوئیس؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/23395" target="_blank">📅 00:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23394">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ncE0qoml4jRvqnjboDqBxvbesFJs4fb8gzDylGPjKvFfth-uCkqLjhazLyhmhvJw-OCEgzSIzgFbJ6xzdT6CcSQIAx06qumqascCfHt0EwH00pqDbYDeYoCleMwAoaDY_T6rlLcYm8oh3R0Yu4HInNdHYaGWW0-GIEOk4spZb-UySMHVFSZ8fZTHwK7VaDEna1zAdJfJa5wdq8Ynhu8C65CBhSJTLU9puUy5uLQdYvJ2-rm5FyALf3pw-vu-Ra6h0kHIzx4ZGBYGou_IIR5PS1AiYzmk_JfSpiruOXbQ5PLi2SuzXJvDKAbWqjHFTuzAZh0-g8guuOG-vS_7TosXIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛خداداد عزیزی ساعتی‌قبل با حضور در دفتر مدیرعامل بانک‌شهر مالک باشگاه پرسپولیس قرارداد یک ساله خود را با سرخپوشان امضا کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/23394" target="_blank">📅 00:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23392">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CKD2MeaXG9K94h441qPdESvefqwPO6WBktjKjy0xfrGkrc4hVsCeDkMy_DYHDq6D6Trgrdt1eX_ijZa2PogbxVA__g2H7RbjORKjD1fAFhqb036vxHe1DqTBiKFeAb219RK65L0_E_MJvI7iwE1nz1dezhbFAROFrMkGKi629WeCMt9BM_DrmoPwVAptYDwtCHNzBkJ8DoIskU4SG2hDTFeN7qFdaGRO4R1TBQWY3LGsjAC2bpK6sMkrN3QU9GKYei4pGK8Keb4UWPKkB4GF3RWHNTiCwIUcbJpZdPwftAG9-4WAPthGSw8XQa7tKvB28hd7tuYVP7_zU3Txy2U5Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UVgpFuTG7nTaj7hYQqMxSHig4BqZENsd89wU0D94cxIPWFEBCPDnrvVbGaOGUB9HJPCH1_Egt6kX-AjpXTd_9k4J2eJ6W73YMnCLr1ghBCWuxJ4kClp9LSMMveoTo8wly1dyZtxmBxNAJBR6gw8v-i-hrfSnPHnorkPjEGZ5I7oeGEot5Cq6IpwcAgo0ceCSqf5rSZ6czbsB4NRdR6bUfapn3d5BMSfHaU3xqoJrs5JNZZ3gImpDRQ8XOI2zY5NLblwCLHri7u6ilRjaQ7PNDSTzcipcH4TJk0Vy0O7snghpgUANEs6KcRP4znXEksGLF5HduMdRE4Za6tND14VKBQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته‌اول‌جام‌جهانی
؛ شماتیک ترکیب دوتیم ملی برزیل مراکش؛ ساعت 01:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/23392" target="_blank">📅 00:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23391">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2397e7f715.mp4?token=ESaJFaq2qhQGgZpYGIBqN6dCxFhVhI4PeAxMa-xVVXSPauumF6J0lZvsb-umG7AHTLwzJi8vqGjVvZLSJzhPm2DwNkcrNA7WA6MW7L-zrLAfO6oD4cycWExp8wbKkIL95vc5Yq3YpaADleUfzEBCtgfa2Ww7Y8gwihTDN8JkVhrTAvqKBe4AKUdh2N3re0LXMu_sieWOA1OuAeck8h12fMxu5QcmYAsaCQQlv1UAn5spuHWYY7FejvpDKE2MVRLmNvevA4PfdHjh6mhy6BwcScrNrwPYPS--kX6b990yDGeo5Z-kfBLw2v46PSiS4M2D7BWZQ2qcHoSxBPcBXiAPOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2397e7f715.mp4?token=ESaJFaq2qhQGgZpYGIBqN6dCxFhVhI4PeAxMa-xVVXSPauumF6J0lZvsb-umG7AHTLwzJi8vqGjVvZLSJzhPm2DwNkcrNA7WA6MW7L-zrLAfO6oD4cycWExp8wbKkIL95vc5Yq3YpaADleUfzEBCtgfa2Ww7Y8gwihTDN8JkVhrTAvqKBe4AKUdh2N3re0LXMu_sieWOA1OuAeck8h12fMxu5QcmYAsaCQQlv1UAn5spuHWYY7FejvpDKE2MVRLmNvevA4PfdHjh6mhy6BwcScrNrwPYPS--kX6b990yDGeo5Z-kfBLw2v46PSiS4M2D7BWZQ2qcHoSxBPcBXiAPOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
ابوطالب حسینی تو برنامه امشبش به این شکل جواب محمد حسین مثیاقی رو داد: برو بمیر بابا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/23391" target="_blank">📅 23:38 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23390">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ylr4fCxB2LPdgkqMLX8nFs52YPN-KWrk3nsC9jHd56VD0mAq9Fpe_4XcKqYH0T1XjONHnni0_DisaZnQ6BH_O823LsmQnXw3zEzbaLp3GmY6rFTEWbgyX9eAHYMUJqC6WXabxfx5E7MTv2-a-JwkHpzQ3ELSnKQ4Zq7KtAVkiB2xBJv6ufC26Uhz_Kz9U8g_DOzaoHke4nGSaUH0vX1A4QzSNUFCXpPE3mmQuakDyATqcekybPGienz9GwA5wSI7uCiAHTn66i6qQEBbyYsVK356oLcxcvpG_LY8tYHX6CTHs1twiDuf4KNcQ_9rxXaNrz4WsjMPvRgka1CuBHoSJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
فابریتزیو رومانو:روبرتومانچینی سرمربی السد گزینه اصلی سرمربیگری‌آتزوری است و منتظر تأیید برنامه‌هایش از سوی فدراسیون فوتبال ایتالیاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/23390" target="_blank">📅 23:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23389">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qc1A5N1y4G4t3azBnVKHN44tLnLW_0lRge-owxot2gMnn4owZClIUX-CIjMJH31w1JarlAXXg8aw7CXf5b2mrz-73CTcFtx3mzTvaP_VFMjdqn3ohKyQaOOH_a_hIeiD3Z7qf_sjIrJL4WaQ9tWiBX4Aa3l_7WGSBDAcMl1ClTPzFGISDi-_SV3uQVUTSnL04cNllqsacVMo3RKwOgg3m-PUPQ3Wn9cd0b87VnQPUbOqQ6N9VnPCl9BPWMewZEeQf9fvs2-QAdfqlDFz5Muv2vKgaXaWxSOTX0LeKKapB6zLYYg1F6leBKuk0NtnFc0-qL3gMxecBqxHSHHcpr4k8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌ششم‌لیگ‌نخبگان|پیروزی ارزشمند و شیرین شاگردان روبرتو مانچینی مقابل شباب الاهلی با طعم کامبک تاریخی؛نماینده‌امارات‌تا دقیقه 75 دو بر صفر از حریفش جلو بود اما یاران مانچینی در واپسین دقایق بازی کامبک برگ ریزونی زدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/23389" target="_blank">📅 23:06 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23388">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GrdEZPq9MeTfucclTtRdP3wl2m4vvsHSLiz3-U15xfBtdzo1JTPo63R1oCBeXnxNf6gTRZ9BzqMYDDpGbBXUL-X_bnho5U7cjxTa1MzWuQ4HObMWHSoXsOfSvIplHBWFaaoizRkDPJ2bdFSvkuIL-qnIAHADp2HjP19rl06un7QGwvJorIcHRYy3ZiHzLmxp0uyXFWjQK0lbpIytqqIvEmoWRrYyt6ey0mC8k_DnnNUq9OTtXqWbWYFr_TL4INQ2QPizkPWcZlIKwONa8RpwLQqX4fx3SG2v8tU0YN4sJ5LMKC5CGJa_UlOryFp07aj6HdZBxbqDWipxi3IQI3eKyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#اختصاصی_پرشیانا #فوری؛سران کایسری اسپور درتماس‌بامدیربرنامه سید مجید حسینی اعلام اند قصد دارند این‌بازیکن رو در تابستان بفروشن. رقم تعیین شده برای فروش او 500 هزار دلار میباشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23388" target="_blank">📅 22:25 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23387">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/721a3bbe01.mp4?token=tCwB0taGjnj7XbGV9x-tpYv_8j9G8l3fqLeoiGmeD8ekpRCZjksRyx00o3deDpROkjwqWxeXogjQ8WLI2JDQFPTTVQef5KK6AclXFpLwj9CXrti_VxJzhz3iuGoVz5ARlhiHy0n0Jf7Yrljt9b3dDjs8Re-1HpB7zjFXsAESdKgVrb7sTdYhj9KKzMogSAvJ6WdQUQ-e7-YG_4VOpVPUhegnbI5byexmU8qc-h-lSBSGdf1y0gQGxet-VSEYUQU6LcXdzY6bcF44v-6aFgSdk8OPbozVl92gYgeC9WAg3MDQS4RnJSjAUf02v3UqvM4NzaZMP_tWrAFWxq4tjhgt3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/721a3bbe01.mp4?token=tCwB0taGjnj7XbGV9x-tpYv_8j9G8l3fqLeoiGmeD8ekpRCZjksRyx00o3deDpROkjwqWxeXogjQ8WLI2JDQFPTTVQef5KK6AclXFpLwj9CXrti_VxJzhz3iuGoVz5ARlhiHy0n0Jf7Yrljt9b3dDjs8Re-1HpB7zjFXsAESdKgVrb7sTdYhj9KKzMogSAvJ6WdQUQ-e7-YG_4VOpVPUhegnbI5byexmU8qc-h-lSBSGdf1y0gQGxet-VSEYUQU6LcXdzY6bcF44v-6aFgSdk8OPbozVl92gYgeC9WAg3MDQS4RnJSjAUf02v3UqvM4NzaZMP_tWrAFWxq4tjhgt3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
ابوطالب حسینی تو برنامه امشبش به این شکل جواب محمد حسین مثیاقی رو داد: برو بمیر بابا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/23387" target="_blank">📅 22:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23386">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WUh0Y3Vsj0m3UdOedUbU8AG6pVVPpvEpvv7cwSWE1w_zHrPKs-gpXMjB8H7hvQBmTgnrDKNF17hwCIdtNApL50VVmLyzMuLiQpO0IDZOTYvJuketpaoA3vr5ySwxSlB-ut0duKmOQVFsYo1S1C1KoBhTA0Rfgep-ys2X98X_8zWcqhRy1T6xS33NjAF1kGIeFO-E5vcax2EhxoPKLARFGFyKCIDc1mUuh6llJ_HibYCGpiFVbmT1DEypVfJSLOpzfT5ysdsQlvYqbwpke3OxoPDwGycZmiNObdSC5L2KsCvURo0cy3F_8sk2CzyeO660k8d3cDxp1jmxEjjsX2pAWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
‏کل رقابت‌های جام جهانی ۲۰۲۲: ۴ کارت قرمز
‼️
تنها مسابقه افتتاحیه ۲۰۲۶: ۳ کارت قرمز
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23386" target="_blank">📅 21:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23385">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9c572c731.mp4?token=kPin-UdQjsksazWD7gcD1xNgXbBuKVufFF7R12QbIMIZjNimQpLZJPSLotnUVPJ75mekokwtkEA9MU3MyUW9tsPlDAVLe_jXKbjoqfI1L2gTUaow_UIgByEBxFk2I06eJe2Y_QEGFJhG0w1_401c7OKjVdG4KgDWvI51m9bx-An2OAzsU2XiaYsXrqTcrhKqlVC607clBaspxRIp7qQNMsRrjdoEw6jZMpZZCBBbWGN0Zr6IrypmrUZr8ZzwOfueIrg5ByAJxKfN-kVUIixHJlDoyCuBPRXFryHclq1BQerukTBrEwBrPIU2PQOz55RVXL1gQh767Dh85Q69FUzgw4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9c572c731.mp4?token=kPin-UdQjsksazWD7gcD1xNgXbBuKVufFF7R12QbIMIZjNimQpLZJPSLotnUVPJ75mekokwtkEA9MU3MyUW9tsPlDAVLe_jXKbjoqfI1L2gTUaow_UIgByEBxFk2I06eJe2Y_QEGFJhG0w1_401c7OKjVdG4KgDWvI51m9bx-An2OAzsU2XiaYsXrqTcrhKqlVC607clBaspxRIp7qQNMsRrjdoEw6jZMpZZCBBbWGN0Zr6IrypmrUZr8ZzwOfueIrg5ByAJxKfN-kVUIixHJlDoyCuBPRXFryHclq1BQerukTBrEwBrPIU2PQOz55RVXL1gQh767Dh85Q69FUzgw4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
شبکه فوق العاده MagentaTV شبکه اصلی و رسمی پخش‌کننده کامل جام‌جهانی ۲۰۲۶ در آلمان که با گرافیک‌‌های تاکتیکی مثل هیت‌ مپ، آمار بازیکنان، موقعیت‌ ها و لایه‌ های داده روی تصویر زنده، دقیقاً شبیه‌بازی‌های ویدیویی این بازی‌هارو پخش میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23385" target="_blank">📅 21:51 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23383">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fQsuR3hJetB2BfWuxTyYt4XdKWNEFlOHUuL8CIeUNqcxaIjwTyBZOzAi3x0t99Q1vlQRnpCJIhA45_79PGR81iEB3QB60zw_y4DNUGDtdNPfHG8ynVncy09ChJkYbesokOY61Mt2EZs1ogjPQpPsp6TmztGDlphJR0Djw4WEWidcgMmW5mzY36eBJCbGdLZes-jnE361naOOirAVHFs6P8lYujNwTSIkz2NWUIy60kQ2wQaHzg7kXC7JTZ4rTk7Dx2a2kGGsAyDyH81l58aZxoPEKOS0jHqx1d_iZ_m7vb68d0wNJg6I4ZmOImocw6Sb_rPFOhNQmqqarllRYjVx2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مجید جلالی که یه‌زمانی‌میگفت امیر قلعه نویی از ژوزه مورینیو بهتره اومده رو آنتن زنده میگه تازه بدبختیهای فوتبال ما بعداز جام جهانی شروع میشه. مثل سال 2011 و قبل از اومدن کارلوس کی‌روش!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23383" target="_blank">📅 21:33 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23382">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OqYK2zmwhWB0eE3U1kFa6eOGRJz_ngyLKxu6ZQWUDy2aXSnIsazayA1RdrrBgPvtLX4Kt7oIj72gSAnKpo8CEmqUTCWxEeMZgAY8085y0gzBYGbxnfV2HoB5gc956l2FN9RbLwQUGzVEHCRgmMz3bTaY4nYnpkp9mjiQfWqsb2KTVtph9FK_77JfRKC95EIgBrj9JSt7cGzAX9h-9Fg1pkVNDCuIfPnipaRyJwdf7w9K4x2fj5e8R0z7k-ZfvgxYs2cXjfdjjtE9h8oP0zH3P39Olby-SPQiV5MhZpkD9tNmsrUlgEm3Y-gwEaekNVhdx3ZpbLvc0ZG2Oi5sSwegwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
دیمارتزیو: اگه بردلی بارکولا قراردادش رو با پاری سن ژرمن تمدید نکنه اونوقت سران PSG دنبال جذب فران تورس ستاره اسپانیایی بارسا میروند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/23382" target="_blank">📅 21:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23381">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c77121522.mp4?token=TMcgKlYZjxqe0vHmhVyQfAgs4Jsb7is0YVKb1UAZUmy5YlgiCQBYmdz8qYcbjxwd7p-udcaHypxJqm1RJjl6_YZLRIt6Q0b-9mXJCOWDZuOIL3rw0Y9Em2v2WM93N3wBeh3Pjgn89J76KBlycxzhv_QNBwCWOGpterdWYliReBnZFsptz54RZ7k4-7diPh_XOvrJRIb1nR1QdPRzKWV4Bcwy4r3gcegfhy7iuV5BzH6S_NeqPexR9uBU-IUD89SjOgDH75tEKMjfWDz_zeUEKIo3UHmT_iUPUjbnNm6dKoNbgcFMU61MA_r0bhmHQKBygpqPxXHW7S6sXxCQtvZfBChgBE3TVgdNBzn_cJKCA8ZLaqAtK4yHRO9rCxGafYo2eCmaAKTrU9HY6456al8J01SWk8COFo4vXN-7fnTlzrNqQ8RW8wU5eUVj-9QcSSEQLG2oXNCxPbuOvg9Qe78jtNf2k7VfMozFr9G1U_jCvil4RHOxwtLghWHm9a2Yt0XR31OWVDExu3qhTDh41RI63TpAL6b0Xl6ATKoN_uVIyOfZFnHz2ZNs7IuK-zpuR5EQ2ZhWOFBdfcugRxFF8rJLU5vd1WtT_U2mvD_KtaC31kMkT_8CT_OvF7L_9DjZ5thITVA5SY3dMinsVbeDKJFx7dMdyULk6apNAyPsfrtsfJU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c77121522.mp4?token=TMcgKlYZjxqe0vHmhVyQfAgs4Jsb7is0YVKb1UAZUmy5YlgiCQBYmdz8qYcbjxwd7p-udcaHypxJqm1RJjl6_YZLRIt6Q0b-9mXJCOWDZuOIL3rw0Y9Em2v2WM93N3wBeh3Pjgn89J76KBlycxzhv_QNBwCWOGpterdWYliReBnZFsptz54RZ7k4-7diPh_XOvrJRIb1nR1QdPRzKWV4Bcwy4r3gcegfhy7iuV5BzH6S_NeqPexR9uBU-IUD89SjOgDH75tEKMjfWDz_zeUEKIo3UHmT_iUPUjbnNm6dKoNbgcFMU61MA_r0bhmHQKBygpqPxXHW7S6sXxCQtvZfBChgBE3TVgdNBzn_cJKCA8ZLaqAtK4yHRO9rCxGafYo2eCmaAKTrU9HY6456al8J01SWk8COFo4vXN-7fnTlzrNqQ8RW8wU5eUVj-9QcSSEQLG2oXNCxPbuOvg9Qe78jtNf2k7VfMozFr9G1U_jCvil4RHOxwtLghWHm9a2Yt0XR31OWVDExu3qhTDh41RI63TpAL6b0Xl6ATKoN_uVIyOfZFnHz2ZNs7IuK-zpuR5EQ2ZhWOFBdfcugRxFF8rJLU5vd1WtT_U2mvD_KtaC31kMkT_8CT_OvF7L_9DjZ5thITVA5SY3dMinsVbeDKJFx7dMdyULk6apNAyPsfrtsfJU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#نوستالژی
؛ بدرقه‌تیم‌ملی به جام جهانی آرژانتین درسال 1978 قبل‌از انقلاب هر کشوریو بگردی از اون موقع انواع و اقسام پیشرفت رو داشته بجز کشور ما که گذشتمون از وضعیت الان‌مون‌به‌مراتب بهتر بوده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/23381" target="_blank">📅 21:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23378">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I4t41w-1ohYw7c_gRwfVnipMrWxv13qs8LQSV0DwePC-vKsl7alfzJyxcaxOwKaJ9Neeryc-O-r-AR-UuUkL4ktgbZtjF-XNZLpNXBjQeEEX2atIlGs-olBA9jox19N69q951N1yFKS6n699j5aKA-19-tZyMN9AyZQbPKHD4uR7n0KQTz_GcabXlmXE3jypkmse3zlSfAOp3ZpnDc2n2SYeDGTj0qyOnbP3WpiZoDqA458pbqzHraG4GDOEMwPp9HTjq33DYcv1VGmv-YR3CzZsMsic2cB1aG54BLZ8hpZxBbcgXlzT9Lex1DO5HUbtQuMl3xzMh2Xo6RAiGQztBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/djxXl2qt08kXPytAW4Vow6-6YlzfqSFtWQ41s6gurGo4UkD9X4prywB_p9pvDCa9Gbum_057jy2kaLmTXkkld-gojQE1L9Csw31CEBxDILwmr449EjdtSBePtOXH1i6cMu5VEKpmLRc9Hg3EzSa7lyZypcGI6CObkMaMcE3KA84zptkO0dGxAiDm3ZZlvakOelJIw3BuHnz6FNYwgMjSlY4WZf3muo5B1RT_2_jdBIphkeaORGhRYhPaVOhAztEe4F9gqgDjUk3zH-GslcSXLOOhqK9e1HQUySmbNmSnyYJWZgRL_twBaV_5NUHJCeYKDt5K0XeTU0sj1GPLtOqy2g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته اول جام جهانی 2026؛ شماتیک ترکیب دو تیم ملی قطر
🆚
سوئیس؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/23378" target="_blank">📅 21:18 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23377">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7731c5d007.mp4?token=eSSdcubcHvObHzhr2uEp0VStWN9IB6KdvxmBDB-nDYy8WKQFih6XxpAsO5Lf91b3h0Nnfs3P00sDH5Z1h9XHPrc_s4sf6oLrqS1N5PpYhrYuEMYWla_ZhYNVzzZIGJY4tEPcMrkurwOHHdCwrQwXFvfw0XXlqOfkM0Y4cu7Jo1CuerEBWYqSw4foZaU5YHAt-QQpEhpYKl6OFYyAwB2fGa6NKxGySP0QDnWSm77ScMcSlMEPmHvQadA1dQZeO28rVoqU90ErxS67slICL_wj-U4t7vm070GBAfN25cGX7tnFtyyB8wnluEUj5NLd8km5xMKq5rApbNsU4VbQmJzu-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7731c5d007.mp4?token=eSSdcubcHvObHzhr2uEp0VStWN9IB6KdvxmBDB-nDYy8WKQFih6XxpAsO5Lf91b3h0Nnfs3P00sDH5Z1h9XHPrc_s4sf6oLrqS1N5PpYhrYuEMYWla_ZhYNVzzZIGJY4tEPcMrkurwOHHdCwrQwXFvfw0XXlqOfkM0Y4cu7Jo1CuerEBWYqSw4foZaU5YHAt-QQpEhpYKl6OFYyAwB2fGa6NKxGySP0QDnWSm77ScMcSlMEPmHvQadA1dQZeO28rVoqU90ErxS67slICL_wj-U4t7vm070GBAfN25cGX7tnFtyyB8wnluEUj5NLd8km5xMKq5rApbNsU4VbQmJzu-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خاطره‌ شنیدنی‌ و با حال جواد نکونام از پنالتی تاریخی و چیپ گلمحمدی مدافع سابق تیم ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/23377" target="_blank">📅 21:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23375">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e41d438c27.mp4?token=JmBw2piuSY2KuhxWRNJ-xbkDg1mMEwd8EtulWHtK_0hCxSZjuDC6QTN7EIoRf6vwVoZNezS4rG4bRGKgQAiy05LknWpOzrsPhiLIlGWQr7HFaZVgFhYLF4-TFTfJNiL0Ca3jVztu_4HzhxMHQ_0idLd1NbwGzK8APPHhQNZ5cBeIyU1XdEH5wZDMwzjXuFjfZ6ucPvy-OcWyYX_QN1FNxocuL-Y-vqFZTcAxh0qCLCTCc6RPWnXE-oyhBJuy1q5haS4CGMwAV_pUSFBD9QE9c8qvLEtwGQziHU5vf9FxHEMO14W5pGEy5QI4OfQHP_0q3x4Pcg_0rJWfdA3RGPcTNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e41d438c27.mp4?token=JmBw2piuSY2KuhxWRNJ-xbkDg1mMEwd8EtulWHtK_0hCxSZjuDC6QTN7EIoRf6vwVoZNezS4rG4bRGKgQAiy05LknWpOzrsPhiLIlGWQr7HFaZVgFhYLF4-TFTfJNiL0Ca3jVztu_4HzhxMHQ_0idLd1NbwGzK8APPHhQNZ5cBeIyU1XdEH5wZDMwzjXuFjfZ6ucPvy-OcWyYX_QN1FNxocuL-Y-vqFZTcAxh0qCLCTCc6RPWnXE-oyhBJuy1q5haS4CGMwAV_pUSFBD9QE9c8qvLEtwGQziHU5vf9FxHEMO14W5pGEy5QI4OfQHP_0q3x4Pcg_0rJWfdA3RGPcTNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇶🇦
هوادار تیم قطر آماده دیدار حساس امشب این تیم مقابل سوییس درهفته‌اول جام جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/23375" target="_blank">📅 20:47 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23374">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa1639bc56.mp4?token=D5lupjgKSWIkLV3byRuWmZOdfMf7xWRiWgHTugTgY6h6xYv3u6Yhh6mJXebq-KlMqMANJb_ZLVqvyaF21toDZTLD_FtyqKQaYQ3rPYcyfIzaEyRTGKtiAMEiCjPetlxYXFxYm7U52ayPSj2YxrGBtqT_egUr2ftcC3ntiR5Q5zagMlk9yuayDbtw7EKrP3RAjtmHcQFZ-qRuQ1pf4yaONdDl-zbNaLDy-oZM-Go_dR9wYBwrrkjJgHJEOapYRtMeFlvniC5JM3YbmIdAIidmjab_KWn5qLiWIJ2SG9AUgO4V6noGE0e9A8Z9zo63d1GXRFpMXMN9JPOsQ4ARDQ6e5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa1639bc56.mp4?token=D5lupjgKSWIkLV3byRuWmZOdfMf7xWRiWgHTugTgY6h6xYv3u6Yhh6mJXebq-KlMqMANJb_ZLVqvyaF21toDZTLD_FtyqKQaYQ3rPYcyfIzaEyRTGKtiAMEiCjPetlxYXFxYm7U52ayPSj2YxrGBtqT_egUr2ftcC3ntiR5Q5zagMlk9yuayDbtw7EKrP3RAjtmHcQFZ-qRuQ1pf4yaONdDl-zbNaLDy-oZM-Go_dR9wYBwrrkjJgHJEOapYRtMeFlvniC5JM3YbmIdAIidmjab_KWn5qLiWIJ2SG9AUgO4V6noGE0e9A8Z9zo63d1GXRFpMXMN9JPOsQ4ARDQ6e5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
مهمونای قسمت اول برنامه های جام جهانی
🔴
امیرحسین قیاسی: رامبد جوان
🔴
سایت ورزش سه: خیابانی و خداداد
🔴
عادل‌فردوسی‌پور: نکونام و کاوه رضایی و دیبالا
🔴
ابوطالب‌حسینی: علی‌پروین مادرقحبه برو دیگه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/23374" target="_blank">📅 20:00 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23373">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa708e81c1.mp4?token=KukJ54pR9K99Ifh1gqH43IDx-UZTzxeODBEumbL2yZ7l4G4xjcG5WIVb0kvQBF1VfMpLu6x_UwY1uOd6Es5aeP20DafNwqQS-TM5PHR9p3Rm-NEqq6V-Sq6MlNbdQHn1dpG0KXB4RZNGBpRdFjN8wu8Fcj0l_ttY0HLwKJWWt9KNouH1QbVi-9kuOq9vJEFEoXaVLDG7WdvkD0iBrYoOYbOiaZRNnvASNLBr-r1hD6QpohAv3a6Jrdtun2ImP0B9np_cTm0pZem0XgjtYiAP_2g_SumAd6cBuSJn5Q8zHpBXlZaNL8LRfq20cr2AxFJscKBk_K_JnKAq_aB1rsFidbcdcwb2kbdBN5PmmDFOW_UsUMgnbz2PrtjB2lH1sCFy0j9hhwvCbVhTgW3dhzws0e6V20LSFiT_DXqI0Hz7OZZTMljG0nX6SrSJAvOg3zwtF8BwpdpWisjwKcCX1WiMRmz3OVm8YAbd_CyNWGlPAixQ5EtJXCAaUHKG75efEWoId5ov_eTZaxl89GIgFrGonsi79DhJlR8S5kYvvhoJNneqkAkJR22cLSup30IubYz-Q8bXldTshOeiSpQpU9zdJtgsrf6l9c-64at2b5PS5eI5-bFc9f5swlKFfvcL8Tt7WqsHwH91DaWrBXP7QDuQh0qbsSR4-EeKdeJ6VQDaoxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa708e81c1.mp4?token=KukJ54pR9K99Ifh1gqH43IDx-UZTzxeODBEumbL2yZ7l4G4xjcG5WIVb0kvQBF1VfMpLu6x_UwY1uOd6Es5aeP20DafNwqQS-TM5PHR9p3Rm-NEqq6V-Sq6MlNbdQHn1dpG0KXB4RZNGBpRdFjN8wu8Fcj0l_ttY0HLwKJWWt9KNouH1QbVi-9kuOq9vJEFEoXaVLDG7WdvkD0iBrYoOYbOiaZRNnvASNLBr-r1hD6QpohAv3a6Jrdtun2ImP0B9np_cTm0pZem0XgjtYiAP_2g_SumAd6cBuSJn5Q8zHpBXlZaNL8LRfq20cr2AxFJscKBk_K_JnKAq_aB1rsFidbcdcwb2kbdBN5PmmDFOW_UsUMgnbz2PrtjB2lH1sCFy0j9hhwvCbVhTgW3dhzws0e6V20LSFiT_DXqI0Hz7OZZTMljG0nX6SrSJAvOg3zwtF8BwpdpWisjwKcCX1WiMRmz3OVm8YAbd_CyNWGlPAixQ5EtJXCAaUHKG75efEWoId5ov_eTZaxl89GIgFrGonsi79DhJlR8S5kYvvhoJNneqkAkJR22cLSup30IubYz-Q8bXldTshOeiSpQpU9zdJtgsrf6l9c-64at2b5PS5eI5-bFc9f5swlKFfvcL8Tt7WqsHwH91DaWrBXP7QDuQh0qbsSR4-EeKdeJ6VQDaoxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
صحبت‌های عادل‌ فردوسی‌ پور درباره یک اتفاق جذاب و متفاوت برای‌عاشقان به فوتبال و موسیقی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/23373" target="_blank">📅 19:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23371">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hByC_dwx6dEQZDXdZfKiUNHg7JP9QhiCxazb9YIkE-JXkJ-JF9Cydnt3g-vphPdhf6Q5LACrtZF_B6kbsqZWBcF8gNbOKJK9_zfkPadlDwRheXr_DJSwGRVDBlifKLjKJWYI76XBtW0gUPfxv__0EKIk155u3gfVIUSLEaFjq2zjYoYwzcC4ISS8xSqrnzrXo3AzE_Pj_0dryeXumIjcwJVwNH1yWlEeKFczIiV2oH6XoL8u3lBihvcbtkl7YfWKIW69RnCwCsCt8Gnf-jR-L5ABPu2jqSOojgB5yf1O8nXjLWP1chxAcg5Kus1iZoSdinxxJC68XaGVlmWgAi9IqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ucXdGYfGs6f17PM-XxMA2UOCIgIl4PRCMuZK1aFZaXq2d9kQcnhb93q6chQrJyiKXNEGYv5n3_bYrXis_tDZcYEr8J8nZpQXHtZpxIfmjoTDV-QEuR6b4ha5Te1rZyk5ZvUuGlwrQj43DTDAwbFEio-6ddQe8fEkCSGCT6uF9gtZuwDu6e_1tkm0e9NaJUcjvgRFzBXpiIzuGsRgch-yqCQQHqi8Fv88YPQRCPlGe7Fh0Uwg1Nm-Srs_CiBVpokRV7VGdWGqOpg4MunUhF2xpG3VX-UYWL4mCvnolVknT1R8JMf1rNdEhilx77SWZbbVQZ0pJnIY9KhlXmirlWHinQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
👤
شات جدید دوست دختر پسر شانزده ساله کریس رونالدو: من درجام‌جهانی طرفدار پرتغال هستم و امیدوارم CR7 قهرمان شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/23371" target="_blank">📅 19:25 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23370">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/id2eGGq5zLqtdAJaPk9lM_nYolF3m35I8Firj4l3CoJ5NFNsLWYbX6hNQyxYN-49lGZaO65B_U1Thkr2T0lO0Jnz_DiGt9lwuPIGIzoPQXahObSX1ZFglzYDCurmYwAiwADTMtRfhCGTIPOFOnJMbC7yvNE_Fn9Y278yFXa06SnAdu9QadVXWxheF6sa2DJfoZ5Vda97N0VuKs13igQrhHF62M18kdIk-clWMMOEsNDchlo8sD1M32rYQkoZIMyA4T_pjLvovJRObzBedNcko4U4JzI6o2TkVTOrUQ5aQTargPr_NNcH555fKB0lrCjM1LNKXA-KC0m-1D1zi74CAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
کنفدراسیون فوتبال آسیا AFC نمایندگان ایران در رقابت‌ های آسیایی را اعلام کرد که استقلال و تراکتور در لیگ نخبگان آسیا و گل‌ گهر در لیگ قهرمانان آسیا 2 شرکت می‌کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/23370" target="_blank">📅 19:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23369">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ftK58PhI2rgFxqeTHnPsDmbMZWF_ZQvSqGaVrO81S9SwM5g7_DCZVVbCpNedUB2cI5Raj6afI42TvfMp69cUO1vil3SpiR9y85mvnvgkkxyBJY_ilnfv9fuHeJhJHh89urOgitzW9y-iZ5an1tME0j0B_O6xgsy0WiXt5_OYd-pwakLmwLRT81iKNw9JTo2ipeuCeGOAGSrqvF6LIpKJlKoq85MlwFlkr05jKWqi53yVr3iDrCvEYsk34dMNjTVI8Evxk63fThnQ7wuGDNyvKUa6P69ZhGzg2kUVnX0UotF6Znqj0l7S0u-DUEQ9jR4ierc_GNCmlxeISCV0FMYNDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
باشگاه پرسپولیس در اقدامی عجیب در روزهای گذشته با خداداد عزیزی سرپرست فصل قبل تراکتورصحبت‌‌های‌‌مفصلی  داشته‌اند و قصد دارند که او رو برای فصل بعنوان بعنوان سرپرست جدید سرخ ها انتخاب کنند. فعلا قراردادی امضانشده اما احتمال اینکه عزیزی به پرسپولیس بیاید…</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/23369" target="_blank">📅 18:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23367">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r7z5ZK_wFn6L9sUoiKUInryu04pWpJNbtXVjGK29N_tIjFqoTzRfiXK2gKOwTSvxljyRpRIBKlFuQJTeuRh7Mjyt73zxWl5suBhXqMMnqN_xT824vmMW5HRfLUDEs8vQa21bOwiXMukvgOy7Ws6K59pEj8vMd55BB8wV0pxcfEBa3zH6bhlZrLEyUggSgaNbVBY-94mG3UREfs5u3pEpO23WazaoUreFGBATOB6KKFCHl8ZN7RKxAlU3zXgQw3yDoav4W4ZN3eAldZz8cCcecpAPWUHim8zN7YrAwhLiJ_BLnSEsgKlUaX7eGraHeQQ86D-12FXgaCplXfENjgL2vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XOwUa_tH_zL3Gr7Ie_XVfgiPtME7xFyH0yeb8YRuGIWs0FF3J5nsyepMS5gojdTuU0OsjO6ZQiUGfik8TKlCCf_16XMZcMD3qmAdleO6wC96AA0rDUdgRBepGOKaQTohFZeNJ_Uc_FepWAagI4TwPR9-hq8L2VQ2QC7eN4htoGdj0a-5maloXfoHhrNYP-po3_RVtDDLUQQoSGpbO47wEk5R-rIhMhYo_KQbBnc-bbANsBAXUT8ULBkrQmTe8y4K-L39jbaGppCEF89pGYLE3NmmSxCtsFPNYf8V63-_eogJfgN67VZjKFkI6_HZku6tHj_Y0gdQ7P_AGMEZwKH0qA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇰🇷
کره‌‌امسال‌بجای‌کیم لی‌هاش زیادن؛ البته ۲ تا کیم هنوز دارن. لامصب ۲ تالی هافبکش‌شبیه هم هستن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/23367" target="_blank">📅 18:33 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23366">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nGHmWTqsMZMXcUeosOSTaZoNczrM-2lQuIH3dQVGO32GMGA2li2gjR4QtHtV1WJgKcEmqQZ19e6HHyNWMBbC6dq5vcjC39_6BRX_xa9NvEWrwB6B6dJZLqrA6mvFBM6dw5BbeLWtTCPHOKwpYzHWw4zrPysKpG2k1WWnWm4ghbDKjrtD9d8ho1L8dDiddvrz078TlNq5IYMe4iT7Vi73TFVP_a92asysB5lMoFmXMdX2yTo7lctLbO6aR5hciRfARqFfj4HqZl10GfIoscKh69YoQv-YRuqW4zTip73tiXX3g_kFyvKS7-WDkKpTxWkeAZQukn3VnBtzZ_8HQDmarw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
👤
#تکمیلی؛قرارداد یحیی‌گلمحمدی با دهوک دو ساله توافق شده که سالانه 60 میلیارد تومان دستمزد سر مربی سابق پرسپولیس در این تیم عراقی خواهد بود. دهوک بزودی از سرمربی خود رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23366" target="_blank">📅 18:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23365">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91bcdb77cf.mp4?token=GzkBEMambqbkhwj013pvMRxZ1bjcdPtvqRsy53Q15NaxxYR_osRQ8lDe0OuhFBeIxpCATBcTA96j_lYi5gc5dubGnLK1uIczxmheZqJIJsIMoitJ5Eb6QEbwGxJQ2wuyNn7elf6SJMnJdNsLIdVj0sYNfqxDivi316EQEfRoXnmGxuOJkJIIKaa8RV8eQ3oIeinipnYaw2GElbUUMQmchA6QPOmKKHZ-Nll0o0w3v09D1KcmyV1WxMVdc9UolPDAsNnaHj_NqcCBirockHXX1IGMGIYlEs6J0UDd_GkrwjfuJyL9Yrx4U2-6LTfP8R9vCnWPXg6i0SQMjPB0t-hg5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91bcdb77cf.mp4?token=GzkBEMambqbkhwj013pvMRxZ1bjcdPtvqRsy53Q15NaxxYR_osRQ8lDe0OuhFBeIxpCATBcTA96j_lYi5gc5dubGnLK1uIczxmheZqJIJsIMoitJ5Eb6QEbwGxJQ2wuyNn7elf6SJMnJdNsLIdVj0sYNfqxDivi316EQEfRoXnmGxuOJkJIIKaa8RV8eQ3oIeinipnYaw2GElbUUMQmchA6QPOmKKHZ-Nll0o0w3v09D1KcmyV1WxMVdc9UolPDAsNnaHj_NqcCBirockHXX1IGMGIYlEs6J0UDd_GkrwjfuJyL9Yrx4U2-6LTfP8R9vCnWPXg6i0SQMjPB0t-hg5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇰🇷
کره‌‌امسال‌بجای‌کیم لی‌هاش زیادن؛ البته ۲ تا کیم هنوز دارن. لامصب ۲ تالی هافبکش‌شبیه هم هستن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/23365" target="_blank">📅 18:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23364">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمجله طلاسی | پلتفرم خرید و فروش آنلاین طلا</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GAD_wjPdQzKvVQpPUm7rj_ryk5PNyn7oeFuAJcl8SA_vUpce9gTMezLy8mLpeFu-T_JMdiB1Lg17TDp08Y1l7ks_aFfpwiAFr6OLu5gi_DbqILu8DdGCJOlEp3ArJjuqOz-WOcQd-FazUIOOi-fYpZ0V_yYJo3IKyiP1q4lBXd4VclP9POTe80O512bBBuC6x282p8ynx6_M50LWqZUZQ98il6OV5YLDG5Xbeqt1CZhwJDLWJMIqYKQJtZuNOk-ev0SD6gu6TW2luyD7rDovfX09q9tjelJWwFJM20oNC5ZTQRwBx1vmuNosviz1ASGFsjtwsD4LTA2dAKgoZHl6Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فقط یک پیش‌بینی تا رسیدن به جوایزی که همه چشمشون دنبالشه...
🚗
پژو ۲۰۷
📱
آیفون ۱۷
🎮
پلی‌استیشن ۵
این فقط تماشای جام جهانی نیست؛ این شانس توئه که از هیجان مسابقه‌ها، جایزه واقعی ببری.
⚽
پیش‌بینی کن.
⭐
امتیاز جمع کن.
🏆
برای جوایز طلایی رقابت کن.
🔗
https://talasea.ir/sh/kel
🔗
https://talasea.ir/sh/kel
🔗
https://talasea.ir/sh/kel</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/persiana_Soccer/23364" target="_blank">📅 18:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23363">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T64edwgxMn1q-vSRH6SS7hPyJikqs4N5LN0zqP3Ogf9zJvIuCizRP1Brk2VajpOEoDQAd6Ei67_mAq2Bs0cUaO8BYOKUCohqnN8-cWiKaXGs9KJ0Lc3TOjWZt-4HgbGVcY4iAKtI6m9usjMS1gWLczld426_CLCeEiPzwS1oo39u08SFrSLhNZZT-XGhDrEV3yGQD5W_Gv8GoUmImVCZeAsXg0Yg52cA6wyUlfJh8M4_a0WYYqB2lVd2bnRsotjega5gIKEJR0lcepd-0-8OfULQWBy8oflvlfRlmTvHPHSDBqq3JiIQVdkXrrK8hJFlELkQJ8Q-NtEbK6weKDadWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇸🇪
سوفی‌رین‌مدل OnlyFans میگه که ویکتور گیوکرش بزرگترین طرفدارش‌بوده‌که ۴.۵ میلیون‌دلار در OnlyFans برای عکس و ویدیو‌هاش خرج کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/23363" target="_blank">📅 17:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23361">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eSZNx5-zpCFgR7JxjcmZfqmET1t-CYq19ImXY0H2aMFeqxXrcpFJIfaxok7l9mjRAG01LviaKgGjmv6H8JyPIWzhhCmZdZMLqq0MdrStFJ-UMmN9bmncbsPOJIDQ3pKiS4304uix6A3cgnrZuBYXT_HYHWQdD_UOk-5yngLKFUn0vlDw09J27XKWTRk40BQz8SgQogpzqXeCld6Fx-Kr_0ZSYzKLxBW5RoDknxRiXQalzLslGzwCA-TcZadBWM6p9jVSoAYta454T4wJ8IzNcVpxXKb_E0TBIbWApeh1BIoeln0-thefG-d5orby4oQ7l9V6A-A7McNXtQViViZPZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
👤
علی رضا فغانی اسطوره داوری فوتبال ایران به عنوان‌ داور دیدارحساس‌دوتیم‌ فرانسه
🆚
سنگال انتخاب شد. این دیدار رور سه شنبه برگزار میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/23361" target="_blank">📅 17:21 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23360">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZGdzkWLlzwDcQgP1c5PSXIER0rjLrdVh4Wbsx_g9ip4cfz1gSmuV2Izu_B4XmxBb9kEIwKxMeFYD-gTVgz7Thfl6feYegU_c-VnZwoCNHpRUIqsp7nYDUaVi5opXFd-0w6PEofs3vd_KU6RwjiugSHE45iNdPf4d7dzGBC_yjaWLS6ZrNa5JNBmkryKWrUqnUYzjBaOpTw2QCQMB-dRxDFX4LFxU9qjBqu1Kzj5MTOmjcXlcromfDYDCCEYOiddfufuRNZip51J1Qe07dmNnEH94M9WhEgYdp42rGF4KKIKpa82FmtqXvxOiX_ka-wjQxvtoCU7akDp8bC5gseIiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛طبق‌پیگیری‌های‌پرشیانا؛ رقمی که استقلال برای‌عقدقرارداد چهار ساله با کسری طاهری مهاجم 19 ساله روبین‌کازان پیشنهاد داده. فصل اول 55 میلیارد تومانه و در فصول بعد سالانه 35 درصد این مبلغ افزایش پیدا میکنه. رقم پرسپولیسی ها یه مقدار کمتر از این رقم باشگاه…</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/23360" target="_blank">📅 16:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23358">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/im6POvnKEHZC8utxRivGcOOYyNzr9aBg6iYt7joyzQbfGGd-XHB1bX_eoEtRbGRINltULoTlcl6O238dbD1Ak9Skfzr50yhLklj0w3QSdkEkRdbQQAxLR3rPZPMcrBZrL6Kj5j-q-bpohlykDIyhshqgnSA49rBXpvq9QYjU63utSE8YfU0KThC_k25ziHSQD9EDpi2Iz_yl1aX5OUGV5IHP8vPzI0UK1HYCrwWt4BlIfrySMxQywpPaDBQ9XyYdaS42LmKmd8Xwe4_QH4nfkxq_xEyxOZNoMbzBVL0BjpcPoor84_rJA8NFoC2hM4fjsFO3SDQTupvPgWnMfZ8T2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EvaTiQaXGna8WidOYdhlDn8oYXUsnd0pBRPEiYRvKhUb1tV0JdshBp6b6QiPJXEQYWEca5yppp92vnsdYhY-VN1JOqgMWbsU3UZCRFLxmdaaVsP8D4FynuZb8_kaZUmauPQFxmtaoif9u7c_xospxFCshQozVdbtrF_or6HDSWONyjjw1bfyzpQ0O6-j6wLYf625fDntLvn35gjLdkOct8xXwhitwyFOgAFNp0N8Rq9unePn5NS_RaaQP8Omdlhi-1nqpBCeiZYDb0nqGx1E8aNwm7rkRY-II3sMrhhMbsrsKUZBXf1VzNiUC6LXvHMfxYCIed2F4SKEvXtOvGQSyA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
دوست دختر پسر 15 ساله کریس رونالدو: من رابطه‌ ام با کریستیانو جونیور عالی است و شایعاتی که منتشر شده کذب محض است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/23358" target="_blank">📅 16:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23357">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PwtNTD92h3wiKv9tZTAFB28UebAUix8HvIZPfzWb9cETAdEo_9ougwl-f8MO-ZSs0o6-Q--yZ96DtTfqLt8g6eXIt3VuP0qjwSlD9rVV_Ny2iPrwVDvc_tWTR1LF-CO_HF7kdRB0OIf5DUD_7bfG-lXHlejalzcxMBTFsneokrsPmkVEhWmuLevj-Us1dXj8RRy1ftfOR4schlY4dO7zml3TKh-yHliqRBOUTfUg4ZTjfhE7Z21EaF79wmOItlKg84keHIN85hgD6gTEDo7HvI9yC4hpoTb_emgb2Avmab-bUPy5Mr70jlPQzPgGjRF3r1P4NNYABxAjkYKnCLpJlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
👤
#تکمیلی؛قرارداد یحیی‌گلمحمدی با دهوک دو ساله توافق شده که سالانه 60 میلیارد تومان دستمزد سر مربی سابق پرسپولیس در این تیم عراقی خواهد بود. دهوک بزودی از سرمربی خود رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/23357" target="_blank">📅 15:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23356">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MqkCbiTgF5R4V3cc1JSyyFK9lbJyHk_70Dvm1N1QmM-Fw0fUrXb2t0SUQPrwwaicLsr4lwoYaU9-hip_o8oZa5b1Urtr_1wW1nbsPlkiE7w_kiJ57SI6SZOCFWMAGXVOEL7S0fVm8PX8xKHho1TYQIkI7Bc0j20eTDZh6t6tyC61JXIfxvZFrNf0jIHw_Jtusr5BVL7ttmdPfByiYd-3W5rsl7uJvXtwkWRp7TCcUCcw-vZgBzLfJnldeuEyqGj_YUKkosajfXZcFElDFAxQJKe03CkXG9glU0zGokdM5TEHg3M-ZmvDG1MNAiXQBjNLnAqx22rF3iDkJtY593NQ1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇸🇪
سوفی‌رین‌مدل OnlyFans میگه که ویکتور گیوکرش بزرگترین طرفدارش‌بوده‌که ۴.۵ میلیون‌دلار در OnlyFans برای عکس و ویدیو‌هاش خرج کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/23356" target="_blank">📅 15:45 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23355">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UhJSfPL5b2Vr1_cMfxvvxGV2Qg-18HYPHf1bNCQrzC-Tv256LgGJX3IDgJogyulYdMJh1nOBBtVqf8Ajv26zxManDcJLwHkKsBW_V-RDZFlXaeLbq_BgCGn2KhyS9_NEDSyZBVL231qTI2ggAhgy03EaonczlbLzUBA37QvlUFQKFgVkzwVHXguypb9l_1CcfCpZU1bgtxpx-MopVZWjbwoyWSYwSjdNIBmmlG_ZoUgmxAVq9Y-gS6ZznKSpTjj5G69bpgs0Dg5AU5EJHlHpZ7Ix1BLfqZwj3i7mdRieoZDKyc10L6Zm0tkBNHoEWlMc2gFhZsFIVwFYTr-7x6RK5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌عراقی‌اکسترا از انتخاب یحیی گل‌محمدی به عنوان سرمربی جدید دهوک خبر داد. دهوک تیمی درکردستان‌عراق است که در فصل قبل لیگ عراق که شب گذشته به پایان رسید در رده دهم ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/23355" target="_blank">📅 15:31 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23353">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D6Og-qk3xZEO2VdjzY04OMt0fbfeb-0GNYDRpkdJJoy31s52nwkCwD07YwqhZpcYGQ6VGOigGzZMNs28StRmioDEXR6jg4r-BcV-VJdjPo_cjJKRc9S-7o7Fu69yGLMNn883BKpTYRpNAE6z-faUvUIV0QaQE_lTmkGIYYzV2OMJc536Mq36-eCA2wYUIb52JjswnDj6MzpqhYVRyh1gPh336zLSQJT2eU0TIQksZf09sbakyjqYWOZ0uFgvL04EI7fAI9QdIRU4sNqiFjURwn4BgNklXVM2WgQJozx2yRhW6Lz06S-RQwAN40hfcYQn8KU2kggdrcd46pCB51dGZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n1txLGeIxHlZhem0-TZoE0tzC4IcqIYcODnXpHePBEBb_XlDXbtwDHEjpcSVZjH9l30_2-FJJYv6i3-L85d1IhW9pgIhuWk-VVxFJYmb0-sRyLw71AKVE1M2t77Sl8yOP-p5VjQSYPLgDupOIZqwCAcFHpW3iX1gOxvRxuG2PoCrD1sNstYatMAT9BrYrOmLUIAR6HEeCtu7ypuANHCDiqL7emWj0cAY7Z-8EF8eVbckMFLdx9LGZStDSKOPl0FR5mUgptWTTm49q04qz89ryFIHjdnGXKlRXc4mAIsssZtYqysP-ETPjJfK3FhzE3i4DPCJN_aR_6m8sqO8X_cKrg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
نگاهی به کارنامه کریستیانو رونالدو و لیونل مسی در ادوار مختلف رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/23353" target="_blank">📅 15:11 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23352">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qz7sTshCVxrY5WAY4gBmYvAon39W42ONaI_NbKSUXAvTkdjAM90IwiokXsLlRwPS9h6uO3s3p4eLwZVtET7k2DAHP5nexXUDc52PVq02zmPENlNhvdPyAfJuj2aCWVjNgLtOzYNUEID6tStUW3vhEKIGATt3fRMNyXSxt4TYmEhOu8Hwlc1XGT1pKJ1Q24ciUbCxkPQ85eb-7H-R__Q2vgr0kuhiY6oTDVuSEaARsEcbDo5ugkj9f5p0pSeMYNswEMaz0RHMg6Y8LwzVScQCFQrDcK_HtS6t-BaBWQhdbgfjLgB_wlGSt-NYkgs1bSMKrTk-MSzWQO1jrWg7QL0maw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیگ‌ملت‌های‌والیبال؛ جلسه‌‌مهم پیاتزا با بازیکنان جواب داد؛ اولین پیروزی سروقامتان مقتدرانه بود.
🏐
ایران
3️⃣
-
0️⃣
آرژانتین
🇮🇷
25|25|25
🇦🇷
23|19|23  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23352" target="_blank">📅 14:52 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23350">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V7CadbSZRJyumH6Otr1KuXoZFlvLKb_KDhp-yAAsUkn2amo8_Nm3DV2fHpS1VYMSrpsALjxkr-l_j4GDLdMGWWg7bmxDgUbvk5kdzqMp3xGSOOuuP9qo-frkU5IbtP2ZGfrsmnwU3cyvLCmVUr5RGVPBygqibpj1YfKax_MeVb_BgTK-poXJqcmogu-Qo1-hpwPpHXqEAyQDApxv1635NcpkXYgu07lRCUJpSHAkX2TLq1Sqi-C7uLMMOift3wFZwIDZd9FryD8kV0X5YbW7wL7gyP1tRqKjtmllcWx3NnT9Yh7bNfEBK7SWb72Sno69-rGkBg3TcSWC4qDJYaIgNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hp_rBN3n4kBC7l347vTxsGHZdbwxC_8ZqfoiIuM-CXWzRi6MpbEYJkv60xeef0yokfobDwPwB-jzZ9ezMBprZHExLQdNNQgb6kER5qXxTwFwvkCYC-8GvrRyzmKmnTNZQGR0kiMG_-mFkKCrNAOj0oUiEvYKYhc_0FZt_PKXuO7nUJ3v1puenZR42gV6QfE8rEZqAYYi90RNTomS2cn8oIWWcwcRMrZvEUw3Ohk0JW77B43LHYdmZsqw_J0SaHPcyDbPFI94bcY76ixwUiHKbvHOdCS85goPR5QKr-eOomBMVL9LEKwF8bU-auutOY3REQAttBOnnq9B0IznP2IwOA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇬
گزارشگر اختصاصی بازی‌های تیم ملی مصر در رقابت های‌جام‌جهانی 2026 ایشون هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/23350" target="_blank">📅 14:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23349">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jUOvezOAtB2xFVIVm5ZQECoacsC3YZ5vjjrZECaKMIdkNAf3KXxxBYM2mDUOJMYmEwCrHA30H0ytI5E42kBC574UX9IxBDZ576jG57PeGMkbtOiroY9_NFcb2nJTIa_C5VqZTlr-y-0Y3XaW3a45eB_elrNLGj0W0KeOViZ7uufroQFx61G9XegII5l7rCpGsw1vvSGjpNZc9s-beaT26hurzfwANRgSQfyHq5Q_00x3l1Fx5qhipGEihhvleEVg26yLw7KAd8HJe2-YMnVlm7RuHkXxMa1mPaNRFEJBJH2l5KfOMVcrYu217kiqvY6v2nyOYFrDA-_ydEivdk2jzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛ ازمراسم‌سوم افتتاحیه در کشور آمریکا تا‌اولین‌تقابل‌جذاب تورنمنت بادوئل فوق العاده حساس برزیل و مراکش در بامداد فردا
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/23349" target="_blank">📅 14:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23348">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ad2f53b38.mp4?token=F5cAz5jzNcIrY9LzSRdzhyQsoBv6n0p1yimMgj7k-wExR2YmM3L9OFL5K80IBAVzx_72CXhawsIkHAGMkJXtkwWm_0JAzXhoDr-yOIFbGRtjSiJqumRYMyPnqJbQve519pCLiuyUAnaaFcGdJolc9492lf7kYj8T10fBaVlSdpHOT0aUlbG0in2uHOfFRPAVSX7gy7hm-LiRmcv9egpyvI6dKV8hSKkAFqLtcjelyjMT21qjmQExdYOH5zKC6I0Bjk_KAsY1gzhLDDu97Z3bmrBvg3dunYAYesWNLMsk-HEI6jb3UFeU500oUIUUx7TwBMPdqoTnd086IzR8BKF-ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ad2f53b38.mp4?token=F5cAz5jzNcIrY9LzSRdzhyQsoBv6n0p1yimMgj7k-wExR2YmM3L9OFL5K80IBAVzx_72CXhawsIkHAGMkJXtkwWm_0JAzXhoDr-yOIFbGRtjSiJqumRYMyPnqJbQve519pCLiuyUAnaaFcGdJolc9492lf7kYj8T10fBaVlSdpHOT0aUlbG0in2uHOfFRPAVSX7gy7hm-LiRmcv9egpyvI6dKV8hSKkAFqLtcjelyjMT21qjmQExdYOH5zKC6I0Bjk_KAsY1gzhLDDu97Z3bmrBvg3dunYAYesWNLMsk-HEI6jb3UFeU500oUIUUx7TwBMPdqoTnd086IzR8BKF-ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
اسپید یوتیوبر معروف در حاشیه بازی بامداد امروز آمریکا میگه‌ رونالدووپرتغال قهرمان‌جام جهانی میشن؛ زلاتان هم این‌مدلی بدون هیچ‌حرفی بلافاصله میکروفون رو از دستش‌میگیره‌ومیگه برو بیرون بابا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23348" target="_blank">📅 13:45 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23347">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N9GmzFb0dv_GtLbbkLeu2nR4Xcs40-3HKY_R0lkDauUZb7iFNoBjdDpmggh9mNpvlbet7f6_j4lOxIIM12wrX5wTgWok6zbS1qb3loaVN3l5hRVTHEn-lgctvCEplJdWtpa1Nj-OFIpitS254Uo8uar4GZ4fQYhUHJzcMEFMrZOIGSV6BnWGjzc1Ipi-Sc_vPF_bJhPmKpAjS0d3WAUWZH2Ttov4jJzptsJRWKob2oBT7fTRN4dt3Fb4GSWtqK09QqvAXgdVQaNjNvFeHixhYgw1YTFlZrq5-dE2TpGinpAKNRYf3jvLNbeSdd4WVqUfmM6LI_WXvm5mehrkXNAW4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دقیقا 19 روزپیش؛ صبح 21 اردیبهشت؛ مهدی تاج با تاجرنیا رئیس‌هیات‌مدیره‌استقلال تماس گرفت و به او گفته بود که فدراسیون به این نتیجه رسیده که امکان برگزاری لیگ وجود نداره و بزودی استقلال رو بعنوان قهرمان لیگ معرفی میکنیم اما تماس‌های اخیر حدادی مدیرعامل باشگاه…</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/23347" target="_blank">📅 13:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23345">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r6zgruzpp3ZCOYBoI59TKqI5EyUDDb6dr9eSmPbJJNOkaUFNrRVFpTzWf5lDD1sbqknPzzgXRVmO89uw-UlHMhxabFT_Jd_7uQxgmqbY3gf5Q1u3x-PE1NU7Kobdoio3mOdvXO7EN-8qJNU29nEvSkarL005Y9L6Tj4Aw1OsJOKQ7gKaR_HNTreNNO2t6GVHFIR2p5DGCotbocamdgtdfzUAVEfNHF-PBoLb2dK10MVigIfQZ0aDuf4oy7M3oRcCHqeX0QR0p3Qnv327N3dDBVyHCQ3MNHK6r8_oSMX4PtEeKFLcsTb1pfQx7Pj4_np3vFbjigx2rpBjDnS5L-kQDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JdNkzG-LsjMwafo6eZa0ajT7f4llWZFqU5Th0kHm0NpZbw8GLhNqh3WU3IusVpLlh4VrVD5ttTqheR0GoBhbKvlY1MztD3mehxg9AtFq9A1iSFIMJnLrxNTkA4ZWsQRu61vD1a07_PF4JeQAy6g19CR_-H9-k7vZQsz-bLN-UIL7lE1uMp9JeE1zr4NjKdrue9yYY_-dbnQicRuLuvFZN0TXafJFpJShdslYKxVR18RynmjrkhI4sy5HnNAl9aecBBooUPgNJfaiNQbWgGrwISEl9XXYpcsTxMGZCsR5FhEmq8iEnrepuaAcgyBZaL52leoAyYmllESTsjihgqVdfA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خبرنگار معروف باشگاه شاختار: بازی دیشب بارسا و پاری‌سن ژرمن فوق العاده بود. انریکه یکی از بهترین سرمربیان حال حاضر دنیاست. همچنان معتقدم که باشگاه‌رئال‌مادرید قهرمان این فصل لیگ قهرمانان اروپا خواهد شد...!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/23345" target="_blank">📅 13:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23343">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WvlldZjI0dVIRbMrmXMBzbTuEWq2h-8bPtsQ91uUNjpVeZFyCcN1qfbz4aKKJrLXtoSzZnIOAXOFAurG7N76ccprtcXRkNJmLAZp0bLE_ywypVO80PGjhGfaal7K_kOXFvOIykdv79om513mzdQfrSlktimjO_Q4Fk-h-yxeK3VECXcxP7deA7zXzwsK42v6WxbXbMFUjcHeVqybwSEosPgJ0cCb3tzePMkk5uakO9Ph2SvQqpofvZlXZZcXgvuFE_CE1UCApw72YpxzJZEhXP7ywqSq7gH93xe4DhRjHGtsIT6EC7IfsGx8Ro1v4eaIryHXbHswEmwNpsDejJaxFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوری؛ رافائل لیائو ستاره‌پرتغالی سابق آث میلان در آستانه عقدقرارداد چهار با باشگاه منچستر یونایتد قرار داره و توافقات درحال نهایی شدنست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/23343" target="_blank">📅 12:44 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23342">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XicMMtP3FcSSPRZBj6oJucYR-UmKGWUnpl_8ZHTN5XiAo-8JekdUhbuH8IXs4wUhl5eFy646SPVNy2qF0pY-XMRWOJiQtVop4Caqbx_IUnvW0tKAiTd3e7BSkCq376kLmkufzjoteVyAOUhYhtWUIpOskiv5IiOtpKQ1LEUspMoEz9PeiE-vPm7pFqvdWTrulvFfHmjKWvf5OYWmrB2yG24aT92NSLIsMIwLKQ0B52h9MPlqSZWz13kdptbKmN2M8tAGXbyDeizFfHgi_2LFI3ucB332DvwVc4agRAw_lyQuvqEenwVKYtK04EEt8PhjUWR0s7xB0QHcul3VS7lgxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
کیف‌وتجهیزات تمرینی تیم ملی انگلیس در حین انتقال از فلوریدا به کانزاس سیتی دزدیده شد. بنظر میرسه که هری کین یکی از قربانیان این اتفاقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/23342" target="_blank">📅 12:21 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23341">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RetXo_vlRXBofdu5kYQfaokon1AsfC_sxzudMWMC10V3o9R6V_NDYaqq38i2HYnic0np0aZMKfyNJsn6KTuV2Qz9nRKPEfXt4dDtVT59bUQAW4qBcJkOJfTzrmM33JTetMp_uE2M7BSuweZVT0Szszx3sPTfvMME-OF_9EmHI7s6DHcR6EoGhuSarr7QwIo4Klu3L4e4C0xPa2p4u61XqmvSYhsmSFLQymI6Z5aLvVxgrxSzv34CPcq8N32Cx3djLodXnsJq5H7dYbY7LmVkGwd3huO9YcTKvsTqfNDrZnyDfcxAqYMyMwxtegtwMW0G5HgfJilOjlHQrYhK069MOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟡
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ باشگاه سپاهان برای فروش محمد امین حزباوی، آریا یوسفی و مهدی لیموچی روی هم مبلغ 220 میلیارد تومان میخواهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/23341" target="_blank">📅 11:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23340">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/upqksZb5prQzJVLtH-EUCbDJeDlitM-Ti0JqUXUp5stGuX9HfcGAJxRmOGI0xljdF3OFOGMr8GSbOdOXIVq6yg6jOE5mG-kWb1XVfLvi_bjCvGBXj2qrjqnevnA5ky3bcfuD5myl74jkwHC1uK6DjGQljrcVU5kYR4eEadEYmtvDIvrJpHZCyJrRnnwlIV4rF-tObrScqW9DgRp6xl4yD5TxHGeqwR-Lo47Zjt3Ml4UeniHotUY6lfOzL_Jl-Uy0Qtfqw3MY9ePAbu2ZAXkrqprhCgFEgDNi5nvg0kKFFb86dIU-D9nQljK2USnCQiKHwrEwipqffF1tYBblYpRgQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
گل‌های‌دیداربامداد امروز دوتیم‌ملی جمهوری چک
🆚
کره جنوبی در هفته اول رقابت های جام جهانی
‼️
هوانگ این‌بئوم با ثبت یک گل و پاس گل و آمار بیشترین تعداد لمس توپ در زمین به عنوان بهترین بازیکن دیدار کره
🆚
جمهوری چک انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/23340" target="_blank">📅 11:29 · 23 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
