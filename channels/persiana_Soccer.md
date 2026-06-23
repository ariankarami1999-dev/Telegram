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
<img src="https://cdn4.telesco.pe/file/t81a61ha7dw951owfe-wfSmRb9ArlCuFugppRJp3lToPy1Kddk_m6kP_ADQy4Jf6-nBZDGs9AAUICR0xxDtRbC_vLH29K1yN8RzLgbF5WCQMVqV4JwUvinF_IWroRHPpt8wIMBC_fwELPtEl4WRw9JQ8qQbl4DCBfFKTTfbK7cKQ133McaeC46uG9yhWj2ZXLJ6ej5PMiD29mTZ9BIa4LAoRE83f6CK5XwcvAenRA2MwDDeajnCykUgIGDFDQ4_23qP-Yjlxz6sh-t_1plwtJx06QqCtmhoRK9gbn50wAshSdn2i9RAXPx4VDZw3PgYNMMi_Zps2LTLuPrT7pn128A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 311K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-02 08:07:29</div>
<hr>

<div class="tg-post" id="msg-24110">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TF7EIFC4m7904qOyBYPb0ap-sPnhqxOQiLtrZrvJcWumudgrHOgHb62G1Tn1nJ9mOBEpS2uHuskrka4FE6Pw5zlzY6XXudh4iI6DYKjLdzXLgQyqvw2FIW2ue8Dz9P53us_TpLHLlVhDZpmXfxcg3mk-5Ng9XssaT_acFzYKGCRlH6fA3WlIimrrHHu-7mSs5FRAwGAgODRg_iLDPXyCujCjnY4-xOhXXMolCV_UmDVSVV7qNl0rYN9g8IGtm_9VGKzki4qgzmsFNY2W60RPimV1_aOUcSgQLnv8hv0Bs8OHAllQKyODJ_1bgtpAlaOLDOuGGWyoiadPzI4Oudi3tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌برترین‌گلزنان‌تاریح‌رقابت‌های جام جهانی بعد از هتریک لیونل مسی و دبل کیلیان امباپه
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/persiana_Soccer/24110" target="_blank">📅 06:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24109">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">⚽️
گل‌های‌‌بازی‌امشب‌فرانسه
3️⃣
-
0️⃣
عراق؛ صعود راحت خروس‌ها به مرحله حذفی با درخشش امباپه، دمبله و اولیسه مثلث خط حمله خود؛ کیلیان امباپه بااین دبلی که کرد تعداد گل های خود در تاریخ جام جهانی رو به عدد شانزده رسوند و بعد از لئو مسی به رکورد تاریخی کلوزه ژرمنا…</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/persiana_Soccer/24109" target="_blank">📅 06:17 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24108">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HvO_IpUGxCu8xTNBDFk6WoGBwjmkaV-9WTF7DdiPRjTPbGXciLpBPV4_syADgF0UBJGUHhWQdetBY_ODY2PPcBpDTCvQ4hbwZhANLDcQawJiMWx4fNC5zSjwxTDxWsacJq65KIvl3obp8lo0ll-onl42aCqcK7pdzp_cp9GHchljRtD412jQAdBEgLPZu3RLJDXwJMZiA72G946g5pDqPVIPTDdchP6Rc71wbqFNPX5qxUHvQgXxoyfFwNjm2kjoGwbvOOiiMxwVfURiZbytVeavnklJ3hLs1HhoPsHGj6tMKN4qwPmiUkR72si4USIFrrNS5J0TZ33ZmHkMhwxEeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
گل‌های‌‌بازی‌امشب‌فرانسه
3️⃣
-
0️⃣
عراق؛ صعود راحت خروس‌ها به مرحله حذفی با درخشش امباپه، دمبله و اولیسه مثلث خط حمله خود؛ کیلیان امباپه بااین دبلی که کرد تعداد گل های خود در تاریخ جام جهانی رو به عدد شانزده رسوند و بعد از لئو مسی به رکورد تاریخی کلوزه ژرمنا…</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/24108" target="_blank">📅 04:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24107">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">⚽️
هفته‌دوم‌جام‌جهانی2026؛ شماتیک ترکیب دو تیم عراق
🆚
فرانسه؛ ساعت 00:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/24107" target="_blank">📅 04:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24105">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rgANFirsfmjIbmZtHDbTaAygnKJsSXq8EwGOWtQQEDiqOyX3hhfoegJNr0_VpQLfckhRJYMfAVAUmGExHaaSEHtu-D-_kQuFAJpBpu8-cmrdV12HOYU8yOpAPFsRQOi1OKkCtV3VR_T2ZOBWXLiBn9yQGBe6Pfm37luva7BEYrRmV6d90rBuOknhqmFDFJ2UulAcFGkXeuDpzmtLhXAn2vzDcgKyeDTwcwmfHQHb1hUKUql76T59XHIdXZu-aWrv9BZ863bNCI5EZMfcO2Y1FGWGOUEYIknQekyKsOAdDgxDlHI3Y9BG2KRfHL4DID6bQUvhF5GGckarAnge1suQYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی؛ رومانو: شماره 9 فصل آینده تیم بارسا به احتمال99درصد خولیان آلوارز خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/persiana_Soccer/24105" target="_blank">📅 02:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24104">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rSq12U6TL_NaRxKuelc4dlagrpJGrf_Z1P_hzhGJ_LRoPCjlEe1mh-VeDkeq4LY9aGOOkrjp10JCIob7OJMn7BVS1KJf8GjbDk7IWpeMsolutlXix0glcX1H_jmQ83FEgqmGZBL_k51tXHPBbBI57N6iZ8mrYBAtPv8Ki_IHW90BO7Tj7KWjelB7y1zB_rWVX08tfzTwWVOP1gKqU29uWyyqWrpZTSTnP3c68aCWREdiqT8x69jUJe9-yK1-Jt7Jso4EZrQLeB2eln6IeRpZIGNTFkr8rqvMhSg2zDFbdVUnL_gHV_gdP6BTQNyo0tv5WV3_lwdneBkO90izl8PhEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پیشنهاد تراکتور به مهدی هاشم‌نژاد: 3 فصل 250
🔴
پیشنهاد پرسپولیس به هاشم‌نژاد: 3 فصل 180
‼️
ستاره ملی پوش فصل گذشته تیم تراکتور بزودی تصمیم نهایی خود را برای فصل آینده خواهد گرفت.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/persiana_Soccer/24104" target="_blank">📅 02:25 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24103">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hLkqGufaL85nI0FeSB2RQ-s_-ibiXTiq7oz-ju5QMUw9kET9nfmUsGYN0ePKVyTnF5qbrJCmgy6XCETZoZgjj-wSNOhR6mdeaHnLe9IEwAKVNUsQDHvZRhkJVRAt6hLb3qUtnFwxgLpUEtxhkgXbZQl-ZaLWxR4gUxH7iwneXZGcWokIu0FDdQKIC1IuMUWW_AoP18Rxyqxmvxulq1knScjCVpSw_rnvV0N5WQSxOOtD0OfmVxvsheVNgL5KzWmLbRRzHq40E602u9TlI2utxOFvWx0KZL0jeBwZow0iSjyIG6_vuFjHwJQMFDPpE-KT3lJ4I7B47KnxtoySO03Bmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
⚽️
فیفا برنده‌اصلی جام جهانی
؛ مروری دقیق بر ترازنامه‌ مالی ۶ دوره‌رقابت‌های جام‌ جهانی نشان می‌دهد که بزرگ ترین تورنمنت ورزشی جهان، برای میزبان‌ها یک‌قمارِپرهزینه برای کسب اعتبار، و برای فیفا، یک دستگاه چاپ پول بدون ریسک است.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/persiana_Soccer/24103" target="_blank">📅 02:21 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24102">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6ad27d0d3.mp4?token=kpkNyjZUZ0i4L87M0FIJkwabJf1sVWY7ZW1a_rNOWEU29jrplGjmcoEoK_oTS5qDYSSHwepY2EO2o2PuQPuEcGHTXxoikRsVO_qJ3s6AA_KxwIld3TgXrEU4qW7x4qzwcUcxEcLVCtKGAqXSD7jqB7RdioNaXcdamfTcNCbL8g6H55NYFZf8yLxDjwVYsxJ05dd4djRJDUOzQddsEnQsvRYJZJvdgZnKYLeGa7ic1D-k8OWiofztQxT_N9S3HJCEbtqjet1iJWF43Scln7CV8h7nBBLF36qlCqRM_q_JqyELO6Y9GWASfyOAkIj6WU3p7oE-x9__y0-iliRnXxdc7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6ad27d0d3.mp4?token=kpkNyjZUZ0i4L87M0FIJkwabJf1sVWY7ZW1a_rNOWEU29jrplGjmcoEoK_oTS5qDYSSHwepY2EO2o2PuQPuEcGHTXxoikRsVO_qJ3s6AA_KxwIld3TgXrEU4qW7x4qzwcUcxEcLVCtKGAqXSD7jqB7RdioNaXcdamfTcNCbL8g6H55NYFZf8yLxDjwVYsxJ05dd4djRJDUOzQddsEnQsvRYJZJvdgZnKYLeGa7ic1D-k8OWiofztQxT_N9S3HJCEbtqjet1iJWF43Scln7CV8h7nBBLF36qlCqRM_q_JqyELO6Y9GWASfyOAkIj6WU3p7oE-x9__y0-iliRnXxdc7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جمله سنگین زلاتان ایبراهیموویچ در ویژه برنامه جام‌جهانی: من فالوور ندارم، اونا پیروان من هستن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/persiana_Soccer/24102" target="_blank">📅 02:21 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24101">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vh4kwqzfKk1JC8Mtd_jnkCu5_a9RTmcODTzxyiPoRvzB7QidMY2283dNC5l0xHJaj3lpCOp45Cf59ErZ9u1bZI7yUMG6HAKrTIQCkaXFwZ5-FXzsCUleZughrIZ9_f96HljdV6S54P2OySkSPuipQfFEl9LPQPYPqUPGlwun4QkLDBB8LS4O6MowFnpa6y3gQtn7_9ogitmUtT_4IOJVWhtBq1KNrZnh4XUJ2Nh2dMPils3zmRE6oM9zbcKO_YCieeIoUvKYsrLxSTyEgXWge4PHETlfwcD_HH8nDqYZh5SO7IpP7VOBurNLtdbt9Pd054_-zwivaDGb3910qxE2jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا
😄
😄
😄
😃
دلار درآمد با معرفی دوستات
🤝
بامعرفی‌هرکدوم از دوستات به وینرو میتونی تا
🤩
🤩
🤩
🤩
دلار درآمد داشته باشی
💰
🔝
فقط کافیه دوستتو به وینرو دعوت کنی و کسب درآمد کنی
این‌پاداش‌پول‌نقده و لحظه‌ای به حسابت واریز میشه و به صورت آنی میتونی برداشتش کنی
💰
💣
بالاترین بونوس‌ها فقط در سایت وینرو
پیش بینی کن و برنده شو
🎯
📺
تلویزیون لایو برای پوشش بازی ها
🛍
بالاترین ضرایب ممکن
💰
expert tips bets
🎰
راستی با اولین واریزت هم میتونی تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگی
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
کلیک کن و درآمد کسب کن
📱
کانال اخبار و هدایــا eA1
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/persiana_Soccer/24101" target="_blank">📅 02:21 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24099">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dsY7LZng9lHYzxvaxF3uA9fziQcYp2cXLzSikw84YZxEecK7WEhrxXmmKkR2tEWa02oE3NLLWvMYSB98xxoG4Fn82qTMPpr2jNkVNdfMPXMlWo34RkN1IFS5u7ncXq5APgaxok4HehTd7Bs3-cSSbxDoUKgLrdsKwNxviHwBp32f5dGzQQmwYXMu2i9wqfvXYwa8cmgnxPrto7oPeVbwy2F87nLibI9YlnzESp2DLUwISWxOPqTBdrT_bYD_YXwew1h9wdcvraAoDx0vyoSpilAcD1RYiXWSt-fesjPaxPzl7sIZuH51onUYWnsK3zTk-ZmsXHLAI1XQ_2Xse6vA8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#فوری؛ خولیان‌آلوارز درخواست خروج از اتلتیکو رو داد: میخوام به‌رویام برسم؛ با افرادی که باید داخل باشگاه صحبت می‌کردم، صحبت کرده‌ام. بهترین گزینه برای آینده‌ام، انتقاله؛ رومانو هم گفته: منظور آلوارز بارسلونا هستش و اونا به توافق شفاهی باهمدیگه‌رسیدن؛ رابطه‌سیمئونه…</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/persiana_Soccer/24099" target="_blank">📅 01:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24097">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eGVZVM58G1JXLLSX8MyED2j9Lu-_UVLS8whr-NMJFyzZdp3UPuLn7xqeOvFubVBWkem_zS4vSJ9el82cT9djrDQqxXYKGlMH9eqDyZwsOOhvI5FDRGOXOEAdO48VBEXlpK-3PauF4vWw0xMp06drgeSEk91Ur-JbfZnvl9WQCrEe-BT58MH9mgss-91j9EyMhTpLo52mh5liiCLpISCooY3HiVoTK6KGv4s2b4qz0zVvAjDqznoFuH4-W_hDHNTFCF7ck-SwjusLmG0z1Kfy7HjrklqdhvKVdmdjb2dca9iN8On1fXGugq1_6cQ-IRigLwfXwynXtPyuqflTa7XCyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ اگه فردا دراگان اسکوچیچ قرارداد خود را با باشگاه پرسپولیس امضا کند بلافاصله یکی ازستاره‌های خط‌حمله تراکتور رو جذب خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/persiana_Soccer/24097" target="_blank">📅 01:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24095">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f709c9542d.mp4?token=FsBXTiJv7r74wA0dOKc27c9mSizRa8OVqtM5t7ns6wXM2I47A0sz6qW3fx8-O9ew65AXs2_w48S4fTgiGf8ev1EyYFvnflO9ogSVZT1wul6Rz890-1g8dbqeltMK6Wqi20UG46URp1Eiuea069Zp5MQ9dUFKd-vtpun1WH6Syh1maLoBdzLPPnnGqGQ5esR4rkCE40AC8FCltLAMnE2C5OfwdYW4sQyavirBpmJQG1q85P6pD0ML6tFGblxm1TH-jVrGix8P7_LgPi9ZCb8-WJtsJcdYNjkFuOV7GJ52vvydJPUlIQt9J4NTERgDIsRTgiEHm5ruP75COqeVCfM-iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f709c9542d.mp4?token=FsBXTiJv7r74wA0dOKc27c9mSizRa8OVqtM5t7ns6wXM2I47A0sz6qW3fx8-O9ew65AXs2_w48S4fTgiGf8ev1EyYFvnflO9ogSVZT1wul6Rz890-1g8dbqeltMK6Wqi20UG46URp1Eiuea069Zp5MQ9dUFKd-vtpun1WH6Syh1maLoBdzLPPnnGqGQ5esR4rkCE40AC8FCltLAMnE2C5OfwdYW4sQyavirBpmJQG1q85P6pD0ML6tFGblxm1TH-jVrGix8P7_LgPi9ZCb8-WJtsJcdYNjkFuOV7GJ52vvydJPUlIQt9J4NTERgDIsRTgiEHm5ruP75COqeVCfM-iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🤩
#فوری
؛ خولیان‌آلوارز درخواست خروج از اتلتیکو رو داد:
میخوام به‌رویام برسم؛ با افرادی که باید داخل باشگاه صحبت می‌کردم، صحبت کرده‌ام. بهترین گزینه برای آینده‌ام، انتقاله؛ رومانو هم گفته: منظور آلوارز بارسلونا هستش و اونا به توافق شفاهی باهمدیگه‌رسیدن؛ رابطه‌سیمئونه و آلوارزبسیار سرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/persiana_Soccer/24095" target="_blank">📅 01:19 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24094">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6f0643b9d.mp4?token=swztQrZ-1RwSIKD_DZjYIMAgOhccTi_dnln3yhuX9UNEs-zJ6aBqR_yAbCXkuSrVcnfuypVXsCARcPD0a8wHJZPzsx2eXW8TBF4z10rKiHz3CAygWliEgBCkQPVTo5kbUmPQvjAdWTEH3HcgW0gQfvEtXcB9Jj93JxzMFfnGt0zysTo6XrFkaDJQTLorCwjkMSIc6fOSvxc9sSsoLwXnMX666HkZB-H9RjsCC6P0bTZkg2zzNuIZR8SUWaFxwt_EgXTEHVTn9QsLT90JgNVbLQEjIk47R6w1EUbwsaTPzgb5CyCAQHK_BglpYiFREeZ7FAEK4yBzKY5ojOgKkhlWKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6f0643b9d.mp4?token=swztQrZ-1RwSIKD_DZjYIMAgOhccTi_dnln3yhuX9UNEs-zJ6aBqR_yAbCXkuSrVcnfuypVXsCARcPD0a8wHJZPzsx2eXW8TBF4z10rKiHz3CAygWliEgBCkQPVTo5kbUmPQvjAdWTEH3HcgW0gQfvEtXcB9Jj93JxzMFfnGt0zysTo6XrFkaDJQTLorCwjkMSIc6fOSvxc9sSsoLwXnMX666HkZB-H9RjsCC6P0bTZkg2zzNuIZR8SUWaFxwt_EgXTEHVTn9QsLT90JgNVbLQEjIk47R6w1EUbwsaTPzgb5CyCAQHK_BglpYiFREeZ7FAEK4yBzKY5ojOgKkhlWKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤩
صحبت‌های لیونل‌مسی کاپیتان تیم ملی آرژانتین در پایان مسابقه امشب مقابل اتریش در جام جهانی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/persiana_Soccer/24094" target="_blank">📅 01:04 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24093">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LMgNAPQ-Udews5dVFw_L5nqzcxiY6nubaudy0jhCe1equLiw-Gl_9tq476q7H7iC1QqGJeyvECqa2mFLNsGJFAvh6OyOiezIYW8m79nHkDjfII7jky6UyXMdAMIwDGQA2szjoIUNn4zw9i2OiFcXDr1uIK9r2N7d-2HQCH_KwG13h6JhIQyISvCDibvxQZt28JUgm849N1HhOG2X2x3dmRhj4xcyKsxTnLgQFNqc2avQP4SKAk_bjm_YnmA6-A6X3lEFJ8-MWBWCjIbTj1HPcWEzqD37zo4KRzMYVPsG2Untg5vAl0PpoX6Kx_NnULraAINXZ56sV0vRJVStkd8YKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛
از مصاف یاران رونالدو مقابل ازبک‌ها تا جدال مجدد کی‌روش و انگلیس در مسابقات پایانی هفته دوم جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/persiana_Soccer/24093" target="_blank">📅 00:14 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24092">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Peu1s81To10uCWrRmOUcc2mSSn78vrwtVMHZPvYVutexSRqBzkHaqVoN1chEB3yNsruFLTaTxw_xWP7lg9SZb3OvStBu-ZtiboElLFk9-VvcZyPyY7L_jtTlBhdau9sNHnf9Vj9Dql4Vcfuw1tZKsHXR7Z1y49rVXqaLVGozIlMrCbjX2wbZ8zACAbiriPDdG5YD6BLUATue3cWmrQ587sNgxOzdmVYjGJxCD7BdblR3b7j7YNNJvWUAg8t3kJmFGi_xqLEfywGTHUA6oa9M_hSbGpJXLuGzkdPggTMazeXrjJ3ehnoOY1yMLv7A-ogt6wozQpnaF-wqqBcbEB_68w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌‌‌دیروز؛
از درخشش ادامه‌دار مسی این‌بار برابر اتریش تابرتری‌مصری‌ها با اثرگذاری صلاح
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/persiana_Soccer/24092" target="_blank">📅 00:13 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24090">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fb1vTGCsa1_gzRlkV9Sae877KNK6y2Zp10qiV6IbXgvTM8NMlQbDm2I3LhWtpTvXYh2bUdzGeB-mG0VsUbxhH9X8JRAAEhCK5oeh8XJl6XJFdaZeNbFbAiPzX8X7t6KCCEkJdVctS4rC9D0nCeb7ElRDc1YXhIRpCpBAc5LtLWgOwDTAseTUu11-S_lRBq4H-v5QUyrFkXYNkSH0AmmPr2TKHOw6jV7wwaVvBWmVgKNpH4YGHWjk3T9fAGM9zk7Y4dtKCm7m3WFknHJA3h0AXrJWOpTK3Bz8DdJCf0U2cijv1Uv5_dvy9CUcmKALLErYHhcNLUWK5jE6mkZejsuiSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
بادرخواست بختیاری‌زاده سرمربی استقلال؛
عارف آقاسی مدافع28 ساله‌آبی‌ها در تیم موندنی شد و حتی به‌مدیریت باشگاه اعلام کرده در پایان پنجره قرارداد او رو به مدت سه فصل دیگر تمدید کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/persiana_Soccer/24090" target="_blank">📅 00:05 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24089">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TvaHdMVyO7ZLY2Y6LG_UXM7JsIl1arE5WOaRxhNiG6N7MfX57-_pVgihLN2EgBgg1kGlOWpNBHJR19cHTI0Xebjy8nIbov0yIvEMMsqmmyW12S4rhhfvWaY_aX9MfFAvBD0AQKhHWCgz6pMUq9Zisk8MfkohA-xvpxNXpV6uhzkUrdn0CxW4u1Zb1Tv4fdWQ4f93KOQ7XYgWAslQLyiZKEKRFdr1adqkB722L06WATJZGMoehiWQbmSRefR2e7JdD9BZgPXVxMOHOXm2kTWfd3yk3r7lX8lTcaCVS83XZ0MJdlTyelsmGh51F0UDf5PjuM8w8CGilWpxSZjH-hJyRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
تافرداشب مدیریت باشگاه پرسپولیس تکلیف سرمربی‌ فصل‌پیش‌رو خود رامشخص میکنه یا با اون دوشروط دراگان اسکوچیچ سرمربی‌سابق‌تیم تراکتور کنار میاد و او رو میاره یا با اوسمار ویرا ادامه میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/24089" target="_blank">📅 23:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24087">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EaW6pdKfhQmz86Xd_DVuh6P7ifEiCXXHIMVgXI3ImPv_LJF_dFf2jnNiK6OfK5FbqYrbdAYfnMhKSYAF0jEyFX7IQH971Y3Dxi5T0WE_VYCvsMCvjbeb_LF77pEPQ9aTs9b-eAtYl-AND5Sgmup0AMTcRY3L1ZMxl11tRyGDVXCbTj27TTi5D8yS3KstG9dwfoMEkrb-jkxLzMiRToxSr-qAIidRHoknkxZQxOpQYfobZQdT5xylPHxWTmeIbGv9Qblim3ZYaUz_lUOEgkJbPtnIe-zoCvxLz4-DawcWtULLk96Y25_oQRygYkiqS0qPOENqsBrYnZN0YUFRDkH08g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IEm2iS0hAUC6AT8vAyeOWGjlUB7VCm-6JKY5vEyau-ftgehDyZeQN2CDZ7BBy4PVCiBAOAZ9QFfoAm43UEUr8O9zPFo3gLJMksBHpYkWQgsOQ08xoVr13qHaxH0BqrxeDSuEIOLHx1HOerFeOnEwqGIH9TVsMqBKZBoGLrTPbwc6fY6A-Mo_wscKMT5ywLMduyVpzMMDfV0SZlpuO0AVETj8eLv4fiW4D-O-dpJvCDY8rbO5n7AvcsqKrbpfyAUFqi7lolL85GSFNoivI3hCkCuORAKinCGCqCe3nfkaVcy787kCPWm1pvNyr65DrrkrMfM2bjAII70RAXZWJBzang.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
چهار تیم ملی که تا به امشب به مرحله بعد جام جهانی 2026 صعود‌کرده‌اند؛ آرژانتین امشب به لطف لئو مسی دومین پیروزی اش رو بدست اورد با شش امتیاز مقتدرانه به مرحله بعدی‌رقابتها صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/24087" target="_blank">📅 23:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24085">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7535185668.mp4?token=IHsf2aRRTp7V4fo5XF1hB__5MX91C9_cUGFD0RrqINATB6KgZVfYRg2A8l3GVK4UUPDj_QNXcmT4sEfKhOjfOawRGsvbSdhdDgygJwzSCI6ptiJz8g_98Xr4tisG53flYhfGjWDp7XYtm-8x-B_Uyo0nxd1nTMRsCVUTlF-SoFXYyr8-NM_ECeiKfP2h6ouu_10N6OqukgeJohIpH1LsWBXoJfrmqR8kHIw5IfjYNYwcDEaEKQeN0Hj6jcJw2Wa8JaurWXiCCaUsglnxU7CbvLboxiCh0hV0HzIWbtK9L43OuZZRXAPaIIjAvu7OkCe1zpwTDJU9m0MpyrulTEbDMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7535185668.mp4?token=IHsf2aRRTp7V4fo5XF1hB__5MX91C9_cUGFD0RrqINATB6KgZVfYRg2A8l3GVK4UUPDj_QNXcmT4sEfKhOjfOawRGsvbSdhdDgygJwzSCI6ptiJz8g_98Xr4tisG53flYhfGjWDp7XYtm-8x-B_Uyo0nxd1nTMRsCVUTlF-SoFXYyr8-NM_ECeiKfP2h6ouu_10N6OqukgeJohIpH1LsWBXoJfrmqR8kHIw5IfjYNYwcDEaEKQeN0Hj6jcJw2Wa8JaurWXiCCaUsglnxU7CbvLboxiCh0hV0HzIWbtK9L43OuZZRXAPaIIjAvu7OkCe1zpwTDJU9m0MpyrulTEbDMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤩
نمره درخشان لیونل‌مسی در دو بازی آرژانتین در رقابت‌های جام جهانی 2026؛ لیونل مسی 38 سالشه که اینجوری داره گرد و خاک‌میکنه. واقعا لئو و کریس جفتشون تکرار نشدنیه. هیچوقت به‌این دو نفر توهین نکنید جفتشون به شدت دوست داشتنی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/24085" target="_blank">📅 23:10 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24084">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HbUaeKEmZ0WRYCoiRFQmbWmd9UmOxj8MZVt_xJj4xAVqbCN5SwSkP2_xHdneHZCtNTZobY6ZLUjbhZ7gZcLP48Q0TLJzu7rXYwea8wlRvOuQYsoe0TnM-tWxBTgeFrB_W_PxF98Cyr-VjC6m1Gs4JS-GAXjZBtTE3CkQONlNd75VkNbsU3_VXmEeiuFWSl-swFAWpJMtcbDnGuRQzuOqY4jrTPcrRg_qd92muk__S77V7h2QDwjETWg8uhnV9YOzfAkGkBQ9WQy5KtGstLVuInVTJSz50azfVKEe9180orWtzcFr0Ze6FWiS-5ip7Qa8JTnQYOpRof9xUfbTxn2EbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نمره درخشان لیونل‌مسی در دو بازی آرژانتین در رقابت‌های جام جهانی 2026؛ لیونل مسی 38 سالشه که اینجوری داره گرد و خاک‌میکنه. واقعا لئو و کریس جفتشون تکرار نشدنیه. هیچوقت به‌این دو نفر توهین نکنید جفتشون به شدت دوست داشتنی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/24084" target="_blank">📅 23:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24083">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Um2_njqp5T_Ixq52Y0gwvzZhTf3Vp0pgja1MKZ2fDwaQ0_PKxnTSf9avfgDDS5LxfUL6L2FRv4mirN4b4NRFH2xAqtm1g2kbFkldgmUupumyqBPu9V6Rip81NWDnm8Pvmtc3wRrobAx4nZWyQnV5wx4Jwe9NTmk7E7EzBSA7xFr-pZfZW_8AfiVpFvM9WPbRW0w-kDyIr3Ll0BxG9z-PlB8Qaa2r661x-RKEheSuPxkJpNzwW-KJr2l6upsoT36Csly-p5l4mCtdw5fzNFCm0Sj28Nwwc84arTsnI6ZL4innz_WTRwQOXxo4lq3gIl05lgiMh6T0F6mk1zhYpp6vMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نمره درخشان لیونل‌مسی در دو بازی آرژانتین در رقابت‌های جام جهانی 2026؛ لیونل مسی 38 سالشه که اینجوری داره گرد و خاک‌میکنه. واقعا لئو و کریس جفتشون تکرار نشدنیه. هیچوقت به‌این دو نفر توهین نکنید جفتشون به شدت دوست داشتنی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/persiana_Soccer/24083" target="_blank">📅 22:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24082">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tUhXz-_wZbxm7q-hfZctcrWoKP8fEjOSUr-C7u5N7V9QPCS8jNaOnqOXoqTLER36jc6bIGL7gHPI1ghdW9hIegYxS3r25M8FyublTs2SR2gM1QolNf5Mtdl4wwXzXo-wm3-Pg9O_qVU0BhU6K6PXlaV1fo75CgU5Krq8QQXisSBF4Kfph8KP1P9Kq2J79BcnclbU_G6lP8a1ZWfXdDRtAcRa69UtdlbTOeVtlZdF8-uKT07-ktIfaJyOyLxvrkWS8jzML7J3AimT1hzZ7E_sk4plrIDgcWs2l8x-ZBQL3DsKyxTfnKvs6GH1khpilpg3P-1eylScFe65rflD_a80OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
سفر پر هیجان لامین یامال ستاره 18 ساله بارسا و اسپانیا خارج از زمین؛ 6 دوست‌دختر تا اینجا
⚪️
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/24082" target="_blank">📅 22:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24081">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rhOjrwO6GRf06v92nV3DLNz0FVzSDL6zc54fYnes7ToEuGkf54-HX1T7jwX58rZU6xC7x_sjAC5BC1UWDU6QVHzWVUTeTfM3ckQ8SZ7rxWQSedG9pGUFGDUj5y7k_rUaE__TDUh6HJYEahODo4flHJbqMaCZ_bxKO5SVfWUgA1I92jgmRmNwAYHep4gYwpH-smSaP7ZQ-8guvGSBL83iGRARqftZjOWJKe5ga-N8AGh2ymwTs753-L0UKgy72AuILv4X-72VAGdRUJ8qntV5YyxEnBdYFbfyhxNbaHh4cBA2jaudlJXonGx-YI12qNIAxknZND43CkUs3oxtSrlIwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بزرگ‌ترین تورنمنت فوتبال جهان آغاز شده…
📺
پخش آنلاین و بدون سانسور مسابقات منتخب جام جهانی
در کانال تلگرام Betegram
🎁
شرط رایگان ورزشی
🚀
100% بونوس
🪪
داراي لايسنس بين المللي
🌐
فعال در بيش از ٤٩ كشور
⚽
هر گل، هر لحظه و هر شگفتی را از دست ندهید.
امشب میلیون‌ها نفر مسابقه را تماشا می‌کنند…
تو هم به جمع آن‌ها بپیوند.
🌍
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/persiana_Soccer/24081" target="_blank">📅 22:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24080">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sODJbI47tK4uUPtxmakOdewQ0VMYjivej9MPzKMTgY4KYoXxwzo13s-KGe3nq3z575tIfM8jYufmfAv8ZZthQbZx1oaSJp74WHfa8gilOWQZ12CNN8WtFqeo31e__OTxy_zHfHdt4vvr3Eheh6bRUBV6DydQuQAqjKl8xgBy2JS9ptFZ6p2grAU5k1ULWsYdg-4j6t8Su4aRGHED5tC7ig7W5uFvVi6y_XoOk5UjMRuAScn--XGhN1zR7VUBDUXXSC3OvP_QT-jMfnmsZCFOcTIHdvhrdhgAElhxIFfp5mv06_pkG0xrcqmOJQlK6stE9SfLOlAC0yfa7jx9GFrbdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
شروع طوفانی لئو مسی در جام جهانی 2026؛ دو بازی، پنج گل در سن 38 سالگی؛ این 18 امین گل لیونل مسی در تاریخ جام جهانی بود. آرژانتین تو این دوره جام جهانی 5 گل زده که زننده هر پنج گل این تیم توسط لیونل مسی اسطوره‌ای بوده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/persiana_Soccer/24080" target="_blank">📅 22:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24079">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a48741736.mp4?token=l8cxNvI9ZdmVY9cxVolk_aDPeyQdkJMavgo4MonOIovf7gZipQtgOCDa7CkFeuVkq2APCs-d03VVns8gRPur3HpGxZqiJ1oAjBCJIFbpmxAopvJWwCKmUjXdvLFRgQKU4WS4HFKgDbcE6hTQWmitsnogJIpztZE8YLbRFwtNuix14cxoAj8zHAOnmiM-dfLqUgr_cAiLQ3wCMpJeEQn8jWKjC3NVbWO9SnIFY5AT_lfervX7BgVh-bXE-4AY2TQiVE3-jCOHIKEYWAFClsEbLtgegJOpZHcA29ug-xh79q_lMQIgc5vo4WUp0ynmmAfbxK4UdZoqtlAi2uez1p5z8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a48741736.mp4?token=l8cxNvI9ZdmVY9cxVolk_aDPeyQdkJMavgo4MonOIovf7gZipQtgOCDa7CkFeuVkq2APCs-d03VVns8gRPur3HpGxZqiJ1oAjBCJIFbpmxAopvJWwCKmUjXdvLFRgQKU4WS4HFKgDbcE6hTQWmitsnogJIpztZE8YLbRFwtNuix14cxoAj8zHAOnmiM-dfLqUgr_cAiLQ3wCMpJeEQn8jWKjC3NVbWO9SnIFY5AT_lfervX7BgVh-bXE-4AY2TQiVE3-jCOHIKEYWAFClsEbLtgegJOpZHcA29ug-xh79q_lMQIgc5vo4WUp0ynmmAfbxK4UdZoqtlAi2uez1p5z8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
گل‌دیدنی لئو مسی به اتریش با طعم رکورد شکنی؛ با گلزنی در بازی امشب آرژانتین مقابل اتریش تعداد گل‌های لیونل مسی درتاریخ جام جهانی به عدد 17 رسید و بالاتر از میروسلاو کلوزه آلمانی در صدر برترین گلزنان تاریخ رقابت‌های جام جهانی ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/24079" target="_blank">📅 22:33 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24078">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5beb8a2493.mp4?token=CBFWGnvBHFC0sHm3twkP6ZUDVO9HQvTMY6WiKIZx5AM9xOiWViWd_GDsdR-j1FxVob1cNV592ebZLmMFQRAOPoKJa0ErJGKyRd9Gj_ezAFkZcFehokbibXIpqau6t2Rq64rg3QOUBBZhBDau-QXuuUxqavQe0B5QxABxvElA1rGScGW04WB9-d8BSxcVcitvEJFb5JxRkHeOmDgNfB6rJZlH0945Xvpam-4juFqR_RdJA79XikhNZV4Ea1pdOFgKQCKFK50Y3ZkCn3JzY8C5zZW1224BS2ekWmyTdSfRVDN9xZBmqw_hyolLaVpcGABTCxu5Io_FDqUgVrP6USHHWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5beb8a2493.mp4?token=CBFWGnvBHFC0sHm3twkP6ZUDVO9HQvTMY6WiKIZx5AM9xOiWViWd_GDsdR-j1FxVob1cNV592ebZLmMFQRAOPoKJa0ErJGKyRd9Gj_ezAFkZcFehokbibXIpqau6t2Rq64rg3QOUBBZhBDau-QXuuUxqavQe0B5QxABxvElA1rGScGW04WB9-d8BSxcVcitvEJFb5JxRkHeOmDgNfB6rJZlH0945Xvpam-4juFqR_RdJA79XikhNZV4Ea1pdOFgKQCKFK50Y3ZkCn3JzY8C5zZW1224BS2ekWmyTdSfRVDN9xZBmqw_hyolLaVpcGABTCxu5Io_FDqUgVrP6USHHWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
گل‌دیدنی لئو مسی به اتریش با طعم رکورد شکنی؛ با گلزنی در بازی امشب آرژانتین مقابل اتریش تعداد گل‌های لیونل مسی درتاریخ جام جهانی به عدد 17 رسید و بالاتر از میروسلاو کلوزه آلمانی در صدر برترین گلزنان تاریخ رقابت‌های جام جهانی ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/24078" target="_blank">📅 22:10 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24077">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A_nqjdEyW_dgi162pI0AQCY1FsHB41ClHDpD5alXMiSQzAfTrjtwOXoOMi9Mz0z9BO9ZPIEG3SljDh0FsYxAxEa4TJx350pJxopAULWTAqRO9YEWeii0XwE357MWKbyhRDhbVwDy8nLa7Tq7eQU4aUdJ8xdrvnE3H9a1IWimvYAvXP5vbxSapg-VWd9suG5AuLHV9uuOf_A91gtJW8BZbx38KX9jpSHxUI6xXpHSjIk5u7Ix7W9l6uo3P_M9Fe7aJFh2Hq59bXcN6aJS1lC15pAB2WcYNG2gdVYX5O3k5hOE73pQRZPLEJqznFK5PvrxIQL0QZM39Cf7-371tIYBKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔵
باشگاه استقلال: سیاست‌ما در نقل‌و‌انتقالات تابستانی جذب‌ بازیکنان جوان است. باشگاه با انتشار این‌ اطلاعیه‌ دست رد به سینه بازیکنان سن بالایی همچون محمد دانشگر و سید حسین حسینی زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/24077" target="_blank">📅 21:46 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24076">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DSMJ6tkQNswtaWQLRCBoftzfoaNQkLON2GQRqP9f1hBiQCr6Z_SWW4byQqrO1wzEfYNZlvCEoyC_4lKK39tSXSP1BD7q3KT-nk4TxnAQAiiabg-d8SlKL0meXzvByg4vV7XWrHr1m8_utKB_5PqUQSF6XaixerAaCjLjXDLJzWfcppSWroSGNWXWk5Djl13x0DCPdXkuMTMJYwrfRZ7DJl_dLPA1hvXz9th07AEXPDqZlXWEV4gPr413QPRn3UuMsWMYRWevoIWTHmqU9nk-NCz7_TCAKBvrfgUKSkKxNHF2bPWwc5zWx7YRt-wbgl3LQT64FCJtXHHtERn45b1zyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
گل‌دیدنی لئو مسی به اتریش با طعم رکورد شکنی؛ با گلزنی در بازی امشب آرژانتین مقابل اتریش تعداد گل‌های لیونل مسی درتاریخ جام جهانی به عدد 17 رسید و بالاتر از میروسلاو کلوزه آلمانی در صدر برترین گلزنان تاریخ رقابت‌های جام جهانی ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/24076" target="_blank">📅 21:24 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24075">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70f39b8ab1.mp4?token=o0CXKqe48OUGRGt26fVnbZ9S-i3tnT1edYguoJnxpX6-aUuKK4NhtZd8uZl2x-RbR6Yiwd1s4Tack85J1OX1SngBODOTzZnReQiZXWvLl_MSnLIXKNWqL2A1k0s_DW2c7X9VbCKdAJ0Sbn38bGO-myaF5qb6wv7ooX1hkHoTohjjDX6ByW5H6a7hE6j_EjhwNgf1dhLw82DfJeWLrz2qloePor9UZ0xT_XNVsK6X2cyt_luqXkM0jI6uleJNKoFP0D3QTkYwW6EfAwgY2rO42fLVj8BqrpuBpAyyVx23G0rg0k_wscp27SoimKZZTncaHmORSErBN9ugemOUUCfeGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70f39b8ab1.mp4?token=o0CXKqe48OUGRGt26fVnbZ9S-i3tnT1edYguoJnxpX6-aUuKK4NhtZd8uZl2x-RbR6Yiwd1s4Tack85J1OX1SngBODOTzZnReQiZXWvLl_MSnLIXKNWqL2A1k0s_DW2c7X9VbCKdAJ0Sbn38bGO-myaF5qb6wv7ooX1hkHoTohjjDX6ByW5H6a7hE6j_EjhwNgf1dhLw82DfJeWLrz2qloePor9UZ0xT_XNVsK6X2cyt_luqXkM0jI6uleJNKoFP0D3QTkYwW6EfAwgY2rO42fLVj8BqrpuBpAyyVx23G0rg0k_wscp27SoimKZZTncaHmORSErBN9ugemOUUCfeGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤩
لیونل مسی امشب دربازی بااتریش میتونه دوتا رکورد رومال‌خودش‌کنه. یه پاس گل بده تا تبدیل به بهترین پاسور تاریخ‌جام‌جهانی بشه. یه گل بزنه تا به تنهایی تبدیل به آقای‌گل تاریخ جام جهانی بشه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/24075" target="_blank">📅 21:14 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24074">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99b9463294.mp4?token=A29-TAcxA2QFLsAXg38LjxFiBBLPfPlwGhPpE9_QCu8yBSNHQJGA35NEbiQhdXdlP4Wf9gJrcuVazsKpQyAr5vS9l2fh0LRFmPk4udGQNRs5kHmvPE1DCmlFI9V6rxghQeHMq63h3JrGauoaqMPOwxFIaaujLLznll6vJvsF_qJhUWG77OfE7LfcOWTdDxRB7HnRHKPHxM4bjCimcURdSbhTf7m6-o29I4PlvrHh9wPmondXk2geOaG0MsGwLBvy3O7kMYLP4Im81qZR9XsesDeAxIXDbzWzyByJvkW38IqMyQNjkN4H2pA829qEFRwVABrRV9Qk0qEQac6GnOucAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99b9463294.mp4?token=A29-TAcxA2QFLsAXg38LjxFiBBLPfPlwGhPpE9_QCu8yBSNHQJGA35NEbiQhdXdlP4Wf9gJrcuVazsKpQyAr5vS9l2fh0LRFmPk4udGQNRs5kHmvPE1DCmlFI9V6rxghQeHMq63h3JrGauoaqMPOwxFIaaujLLznll6vJvsF_qJhUWG77OfE7LfcOWTdDxRB7HnRHKPHxM4bjCimcURdSbhTf7m6-o29I4PlvrHh9wPmondXk2geOaG0MsGwLBvy3O7kMYLP4Im81qZR9XsesDeAxIXDbzWzyByJvkW38IqMyQNjkN4H2pA829qEFRwVABrRV9Qk0qEQac6GnOucAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تکرارخلق‌این‌صحنه‌تاریخی‌وشاهکار امین حیایی دراخراجی‌ها در بازی شب گذشته ایران
🆚
بلژیک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/24074" target="_blank">📅 21:09 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24073">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tkkdyNuHqCaXK2qEkh56DGrKT-Pmn53EWLBvm3BHrtpv-W0sfspfdnmnErqxjflafccC8u7oNWnDxRd_pJ0WgBkoDwPyVOW5k7jpG8OIG3-uuGyfwveuDmH6sbalmWDKcliLwV_dEtJBDuH5Xs_VvVu1JY4V8Yn2w_b_X64-6eNA57X6BYYQmytR9zaJjrAH0UvHLLdPWONikoIwwZU22FKMWvSTlV7MEdFGTMY8EnoQkKYkxnIb_cDSKveV930MucidUgAoyea5Qn0Rgtq5O72i5C1DktpxOXHsqsFziRQNu7LHmcDYLwrGs1flgG8b1MMfL5DG5LGPMvd0iMct2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لیونل مسی در دقیقه 9 بازی امشب با اتریش فرصت بثمررساندن هفدهمین گل خود در تاریخ جام جهانی رو از دست داد و پنالتی‌اش رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/24073" target="_blank">📅 21:07 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24072">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">دکتر انوشه مهمون برنامه جیمی جام اسم ابوطالب رو از قصد میگفت یونس یا چی؟
پامپ که برنامه جیمی جام رو ساخته، ترمز بریده و داره یک کیلو طلا بین مردم پخش میکنه،
هنوز سهم خودتو نگرفتی؟
این کد سهم: pump
اینم لینک :
👇
👇
👇
ثبت نام و دریافت طلا
دیگه خود دانی...
@pump_vod</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/24072" target="_blank">📅 21:07 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24071">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/275cd8fdaf.mp4?token=kqZwfysiDTXkmRB4k5us5hFvk1pD1gHQcVHoCIItpmP3LETkEPXbGcGAd73BUPBGuXtB9LxSVmao6z4ppMskQRnQWCSxMvmTAQy257cWVxypAal_H8r774iuzOvRZocvkOQn6yw0ubccMrYBWb6pZBUw-VM8K_TgeeC2A98nnaa9KKqJj2VC-07ZXTN9eqAiK_K4Hm_KVULs-no0EArmEIGWpzeckkJs9TCYIG0LGA7ZuvGOlWNSr-a4xNNcJ_kspIEv_tu5fTaiF9wDQ4L9dbmuNCzoaxCxWvb9kALzDEn5l39dSOoATBTlESN8xgY9Hjk4XMpfR2EQXTvKiqo4Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/275cd8fdaf.mp4?token=kqZwfysiDTXkmRB4k5us5hFvk1pD1gHQcVHoCIItpmP3LETkEPXbGcGAd73BUPBGuXtB9LxSVmao6z4ppMskQRnQWCSxMvmTAQy257cWVxypAal_H8r774iuzOvRZocvkOQn6yw0ubccMrYBWb6pZBUw-VM8K_TgeeC2A98nnaa9KKqJj2VC-07ZXTN9eqAiK_K4Hm_KVULs-no0EArmEIGWpzeckkJs9TCYIG0LGA7ZuvGOlWNSr-a4xNNcJ_kspIEv_tu5fTaiF9wDQ4L9dbmuNCzoaxCxWvb9kALzDEn5l39dSOoATBTlESN8xgY9Hjk4XMpfR2EQXTvKiqo4Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤩
لیونل مسی امشب دربازی بااتریش میتونه دوتا رکورد رومال‌خودش‌کنه. یه پاس گل بده تا تبدیل به بهترین پاسور تاریخ‌جام‌جهانی بشه. یه گل بزنه تا به تنهایی تبدیل به آقای‌گل تاریخ جام جهانی بشه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/24071" target="_blank">📅 20:43 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24070">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jpzSVfl2d8GdCqIbhwIdy0cC2cYqDOjfS0hElIbjL9UeVVydotgpK8Y6zYW0U323r2Xud_SoObxB5Od9qQMiheuNHYiu7ZYpVZfTtpuIkEPKXYqTAEH9t9dwbIV9lI5DZHwMhCJPXWglbUMFauP9TtwGi9GAwj68CXaK3PeG7uUDfykW8FBjmx46dnyApyfi9T68xeavIVljf1t2gfhlhuIGpXFs-R6OR805fqyDuREKCarNV16q7DzHJE00v1cpmjXzCE-lNxKjngvt7F-RtB9jJgNuLqBjCVsYuqRaDSHRGN3VAQ8j5kkpM9tAyRtA2pz7hqTmeeN3tU1_kEK0HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
اولین گل مسی تو جام جهانی: 18 سال و 11 ماه
🤩
اولین گل یامال تو جام جهانی: 18 سال و 11 ماه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/24070" target="_blank">📅 20:37 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24069">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/436443b2d6.mp4?token=PTi47VaF7XwtnXROmoFrsR06xC-hS9sEbbKxFmg3lHPGbJNxElWiKKlg-Vqv_XVmwwhYP98gkksxFkHyPZKVwxHvnzf798N6CGJZRopWPwsTD5BAIRGP3ZZKeRWi0gUQwOJXziLETGYkbZbYbmnRZ_0SvQqYGcC97grWJoV6bvIQkXF0njcC4PCrn5j8D0g5G4nmHidXIYNeLG1-GQRABod6SKuVswHUQO6caOZsBMqA5dhkIxlIWZS8rPG7y6Mb6oR5sGKUw9jCqjLg_mWKPdAN-ztjMBKzK4nX8gCO9bWmqfSIlrdaEcayNXMnvu5NUyy0uAfE2WP9acif_6y6Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/436443b2d6.mp4?token=PTi47VaF7XwtnXROmoFrsR06xC-hS9sEbbKxFmg3lHPGbJNxElWiKKlg-Vqv_XVmwwhYP98gkksxFkHyPZKVwxHvnzf798N6CGJZRopWPwsTD5BAIRGP3ZZKeRWi0gUQwOJXziLETGYkbZbYbmnRZ_0SvQqYGcC97grWJoV6bvIQkXF0njcC4PCrn5j8D0g5G4nmHidXIYNeLG1-GQRABod6SKuVswHUQO6caOZsBMqA5dhkIxlIWZS8rPG7y6Mb6oR5sGKUw9jCqjLg_mWKPdAN-ztjMBKzK4nX8gCO9bWmqfSIlrdaEcayNXMnvu5NUyy0uAfE2WP9acif_6y6Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
دیگو دالوت درحمایت‌از رونالدو کاپیتان تیم ملی پرتغال: "فکر می‌کنم دیگه همه بدون کریستیانو چقدر توی کنار اومدن با انتقادها مهارت داره‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/24069" target="_blank">📅 19:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24068">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tq-Rn3yrlgCF4L59MKIk7NV4gYmpyjKxEmIT-Q-rr9YcH3LrjMEDzARiy0ZMZ7bFtNh5JNiUicweAOewcT-FifCg-_6fHli-tyUlT3A3pPV4eSqMu2S6yHzwSqkqcMMo1N0CZ8dpeW7sEYU50XoiIRfDBCLBhYv8CF_oE7jPr-OA9yO5X8W6ds_A4uzNVmuPNNTGY2UZ1kGf0ARczimm07l7gF_SOSIpdqMf_B7oSfHm9B_hNRTSIckeJUwGF7cWkpMhzfq2Woi9IaPd3fdzQJY3VeZwUGdJRSDxtNj3eYTALE-T6CcRWa-QRWK4HK2uXNOKH8Gofo1u-0a15X3_dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته دوم جام جهانی 2026؛
شماتیک ترکیب آرژانتین برای دیدار مقابل اتریش؛ ساعت 20:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/24068" target="_blank">📅 18:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24067">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vDxhA-0omTUZ4n8tjRwOYAIFEGmylBOmz4VuyZSeHIEhRFRvdGCHpfdD3jXFfaHaJ6fAXlKn8ZuIlb62zhwfxugKI0f1_fsfH_9hJ2PXgRszda8qt-R36OxzsI--hrdcQcz10t16clKWcJ1XWJWKkx0BIuubj_LZ1V1QA15FDW6L96P39DzeNrCSVm9sIXExu6Hz0aU_OQBOhj0QycvhZd_ILw-2e15nayt-Z-L-uJGkVNz3WCtXx3MZ0ox5IgCeUcbZoN00gKDsa_-Vub-xxKJ_wUVVDi-RC2IaBHIxuiHAhuVeBntVu-F8B3U_J9Etz2Lw03C0xU2xq9uSIJiM6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تعداد فالورهای وزینیا سنگربان40 ساله کیپ ورد در همین سه چهار روز اخیر از تعداد فالور های بوفون اسطوره ایتالیایی تاریخ‌فوتبال بیشتر شد. همینجوری پیش بره یه رکوردهای عجیب و غرب میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/24067" target="_blank">📅 18:09 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24066">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">⚽️
خلاصه‌بازی اکوادور - کوراسائو ببینید لذت ببرید ازنمایش گلرهای دو تیم؛ بازی‌ای اگه قراره صفر صفر هم بشه اینجوری‌بشه‌قطعا به دل تماشاچی میشینه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/24066" target="_blank">📅 17:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24065">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aa115feff.mp4?token=jJq-_SRkXKdnwvk7HZS-E4qpSfPfwDr_7YX-_mh69RZ_rJjJ0ekZZcu9sGuKOw25gzraNtXzZ2P6NgSwd_2Od0MZb8AW-bHKzx0HbL0LR4BdxkQGa7JxidBevsfu5WjpepIHPCsH-2OLLSxlYO4_lF3bMggdu6s9mY01Y26uHKh4f-FVyj0HuD_f6fHRJbAhMNwNYOnOhF9MxHMXkYe2Oe90FVFxJOEdbYhNEXqUieUsvrDtT6IddcDcVSkGQPlFn7c4Kr6U0XxxkG7w-0rq2oVgai8ZBPEYOka3wIZ_yvsXsYkDhJsiKJ7pnDAXdQt4RbkXJQiMDHZQF4K03O_j0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aa115feff.mp4?token=jJq-_SRkXKdnwvk7HZS-E4qpSfPfwDr_7YX-_mh69RZ_rJjJ0ekZZcu9sGuKOw25gzraNtXzZ2P6NgSwd_2Od0MZb8AW-bHKzx0HbL0LR4BdxkQGa7JxidBevsfu5WjpepIHPCsH-2OLLSxlYO4_lF3bMggdu6s9mY01Y26uHKh4f-FVyj0HuD_f6fHRJbAhMNwNYOnOhF9MxHMXkYe2Oe90FVFxJOEdbYhNEXqUieUsvrDtT6IddcDcVSkGQPlFn7c4Kr6U0XxxkG7w-0rq2oVgai8ZBPEYOka3wIZ_yvsXsYkDhJsiKJ7pnDAXdQt4RbkXJQiMDHZQF4K03O_j0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحنه عجیب از خوش و بش آنجلوتی و اعضای برزیل؛ آخه چه‌وقت دست زدن به اونجا بود.
😒
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/24065" target="_blank">📅 17:34 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24064">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KaSXMXMtcj5hITMdzvm24Al2L5II1D-ojrqrg-CevX4mePoOsj5IHtgZDaORgtCQe-0Q15WSeIMtQIakCCbudLbJu5AHmaz9lB4sEj2Y_kev17YftHB7TwWMASEYi9kDyP_-GEjwqTPyG15MX5p7kq4SqDtlZJ8rQGBWNmNcSrliIimjmdFMPqYuvR5JoQXICH4cb5dipp2fadbuk_ECCI2fQwlCkTXyCi29-WIhUEEIGM3k4U6A2rGJhpGcgzySSTJynkyfYl5j1CHoZDbR3kAGGO8M_ioO7eE8dl1nnQRjX6afosIRWf07wi9pKjWdAqtyKsXThMyTS1kj-rCjLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛خواستیم‌بعدِ بازی امشب ایران با بلژیک جزئیات‌مذاکرات‌روبگیم اما رسانه‌های دولتی نزدیک به پیمان حدادی جزئیاتش رو منتشر کردند.
‼️
دراگان‌اسکوچیچ درمذاکرات‌امروزخود با باشگاه پرسپولیس دوشرط‌سخت گذاشته است که یخورده مدیران باشگاه رو برای عقد قرارداد…</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/24064" target="_blank">📅 17:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24063">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gZns7ESvqyNCmyp2EBWO3-NKo84H_riopFPAc359jEQg_mCfQPGiRQ5aTEgWsJNGzj7JTDUVhb3UBInOoqmSSGXP3_X2-z9sGJl7TZ_ABt_rnxwleYy1e2U2hctpM6cbmt2hUkikX4O6FMfthcz9k7dQ62TNH517rnZPaXCQj8kVYcDPHgODG_ImSP1i7A7bX1Vd08XzeoDiC3l5xRwZxfkX-CZ7TGoIV15SGkiwsZ2At_KRDi8JZB3DChY-PP7z4R3Fw-1Oq4zcXDt1Na-jQiPCbcLpPs3AK0U4SvQqq7JbNQwtJfgrLnXz1vvbc9rziOYkxzZCxcOWb9F7VunzHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
10 گلزن‌‌برتر‌تاریخ‌رقابت‌های‌ جام‌ جهانی؛ لیونل مسی به رکورد تاریخی اسطوره ژرمن‌ها رسید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/24063" target="_blank">📅 17:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24062">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gqwVXMmIxzUXbrlksQ7BFEDp5y4Okg048UVw9X8mdYOK96R-gQviBcpeIDb-tzxYkC7N35TLxC4tYctemtazW7tyV-wWHkYwv3iEGryhIxdyP47X1d98rrmmSeM7AmSyKlR6e_zXReIbKFhOqWlvDB6Cn8uhx1qxKiK1BGfiIuzgenzwDrroMHFrEGiixDWM8H9LgFTv4jSD-zWqf35Dgec7cVrdOPMqY_uiKWkGK95o4Do1hfZqpM_jgYDM-uQ6i7XLsobX_IKx0XvP0JTRRcOSIi5PRd6Aa0uLyKcS67X2X346by_EvR0ifQCHT0NEm7bpOQuxdYMAhqqpBLkgRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
یاسر آسانی وینگرآلبانیایی‌استقلال با انتشار این استوری‌خبراز موندنش‌دراستقلال رو داد. مشکل پرداخت مطالبات این بازیکن برطرف شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/24062" target="_blank">📅 16:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24061">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f988706b3.mp4?token=YKI2sKuBRJpKiZB9TB6uWx_m9nnlmKQU9V55CXwkOR5etHL2oDM39mvXT03ZSb4W419way8D6ceQCEB8-YS_T0oQqjSEM6E4n4pVWJlBerQ11LwC1seXg9UZgUoVppk-5yGsfPMrO6ILG3JSRXfxEAKiy1v0St0WNny2qv1LpB8FiH4EmPDVcaamSfI8FGIyp69pyFs0jhxNbWzKbJTMNIvWfblpW5V7X0Lh4DuAL3riYl1K21vdc1nQ_FjXgy-mcH2xsVSUP0FGp-AOdm4X-LuArRxqYzPHAZT8FMhjgUBLruhIXGwC_0GZ_ECkIiHXiW-B5A5flwZhRHsVvKP_LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f988706b3.mp4?token=YKI2sKuBRJpKiZB9TB6uWx_m9nnlmKQU9V55CXwkOR5etHL2oDM39mvXT03ZSb4W419way8D6ceQCEB8-YS_T0oQqjSEM6E4n4pVWJlBerQ11LwC1seXg9UZgUoVppk-5yGsfPMrO6ILG3JSRXfxEAKiy1v0St0WNny2qv1LpB8FiH4EmPDVcaamSfI8FGIyp69pyFs0jhxNbWzKbJTMNIvWfblpW5V7X0Lh4DuAL3riYl1K21vdc1nQ_FjXgy-mcH2xsVSUP0FGp-AOdm4X-LuArRxqYzPHAZT8FMhjgUBLruhIXGwC_0GZ_ECkIiHXiW-B5A5flwZhRHsVvKP_LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏐
برنامه‌دیدارهای هفته‌دوم و سوم تیم ملی والیبال ایران در لیگ ملت‌های والیبال؛ هفته اول تموم شد که یک برد و سه باخت برای شاگردان پیاتزا حاصل شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/24061" target="_blank">📅 16:41 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24060">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aCgb-k24sYBmYjXrCPnDnumGTaNbysBQmP-c_bDTEmlooLXbb2TcYZs3zcrARY6nht0Lmd9G7KiTI_9N_dCBScC91UMQyMg41gBQ7syk-KfZs2PZ-4aNYPMuNhQU5lbijtFSgf3SDKtRQmO7m30yncBl_ugpPblkD3SLJDjxyG_fje1baN8CvR79xG0rUw7RWdkPeT5TNrr-0HAPohd_a0Mobm89YhFIijaebVOp6Ag-XNOc84kGsQq_dWc3MQ75OxYY2HLNBhB_SiyEeZBBd8cDR_U4Dqaj-7uDC639CFw5OwI6RZad3qsrQUnZcNroT0oYUAKVWKFtdht0DddIrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
گلرایی‌که‌درتاریخ‌جام‌جهانی‌نمره 10 رو گرفتن:
🇵🇪
🇳🇱
رامون کیروگا، دروازبان پرو مقابل هلند.
🇺🇸
🇧🇪
تیم هاوارد، دروازبان آمریکا مقابل بلژیک.
🇨🇼
🇪🇨
الوی روم دروازبان کوراسائو مقابل اکوادور.
⚪️
🇧🇪
علیرضا بیرانوند دروازبان ایران مقابل بلژیک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/24060" target="_blank">📅 16:35 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24059">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l3R0D4P17fMCICnQPCBfhDmQhEidQp_qX02FIsmgIblsahQLxpR6kqCOZiq1fjZA2CHWnpgstn0yJYKsWdfDbSG0EvbUxC6eQTcudgiHCcGcyHonFMKEupJah6EZHVS23B5V3lTyomibvf1E6UEtP_KgQKoVgBH0zHuW1_utSEPftqO5IvKOfKQUi1PyFpXsIocN4wzNHurgIErN4r9HJwO_OStgJHN8jtYakuDrwfbZWuIH1kfI1axRT52RMjxgg87b_pQPegh4fTWnc_XTPzVcMJRfQ62su4LtQN0fZy0f7BAhOEn5RutZPB5eh7DCiMVzaV2_D4Z9EBE3VNA2Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ ایجنت مهدی لیموچی ستاره 26 ساله سپاهان امروز باردیگربه‌پیمان‌حدادی اعلام کرده این بازیکن اماده‌عقدقرارداد باباشگاه پرسپولیس است و درصورتیکه‌سرخپوشان بتوانند رضایت نامه او رو از طلایی پوشان بگیرند لیموچی سرخپوش میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/24059" target="_blank">📅 16:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24058">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PiyRE1Z-pljjyVPh6WyFJ64bkfnJWomfFfRdEFA4OGopDOw_HpqsTDrV37_sIxTBlOUDvjtF3IRvKw39wJxV8S9zbs8MqmNTiqTbCFskm4Fqi6vVGkOg3rJEXEV1az-41H_G1x9oiTvk4LB3TjZbPJayuqQ4igfPU6_lcT1gzefhwuDMgCpjulO1SVfgp_yIGpeFzH1s2F6mKW8T2B1z6WCAME-sjY3LEkpo9wVRuQOs_Hy7gQHb94Mg9fBMOnhPJ5dBb_ksohu1GIYjcMZGcW6DxLvvHQo2FYfVV3AJp8y_vHf0DYBrgCNOSkKC4nRsmiyx2lNVxH7D7nV32pDV1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
تمام‌حالات‌ممکن برای صعود تیم ایران به مرحله حذفی جام‌جهانی؛ازتقابل باعربستان تا یاران امباپه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/24058" target="_blank">📅 16:18 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24057">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ALBkCWwskFeeYUAen-S1-TPLmzg6_aumPtAFocAp90W_yr5UyCtrMYgTf1n-iKDcH5qwCsh0H1tveTvvB3EZsw5bsCmcPZkXnLWsPzY0Kx1CKu8QmD7La_A_Spwui8dJRqYoZNQWRoiLZ3HQ2EDcwGdN7nPtE-RJigxl67xRM4aNRowgaRpWdL9xeyA6LhjyHHfd2ePMznDhqw8upklj9Sn_SP5kIwoX7DIi6_A172dZ3lY9A8ybP06SPqUBcnK2_CY3V8vqkauvwaBO_o4U6EVR68e1iOU0hO6e1wcTWPrlLpyMpY0dFmv-T8CRXq2JiW0f0MeQsduVR5Js5UPT-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فیروز کریمی درمورد عملکرد علیرضا بیرانوند در مقابل بلژیک: این سری خیلی تنگ بود خدایی
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/24057" target="_blank">📅 15:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24056">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2fba3c01e.mp4?token=SObbQ9xxr6jQ0z3QI03OwEElQv7odLnBD1BLemOfTUW5mNB9Mi2R56wh7C9913EuLvQM3wQGuBJFaTGB-3Mu43-hWEjBmqxUMnqNiSZBYebYT9i93NQGd7U8bTfqLtUvVl3tVgvwpr2qd0tUwBu6QXAkjDcwxxPOoqUCta3ss8iQaXiYZRclusgcDLaV9UX65qQUARyhUmCvW7vJAN14SZqWKlkZN9NPnpa1QZ1zRTunkRju2fV-lj-X6-YlIhoE8QwWP4pee1LirEc5bekQu1nIU210obG3BGYKVJuGiaHgD5zbb68zASEgtbWFqWDcmHkZjShzrE3Y5LEE0GRKlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2fba3c01e.mp4?token=SObbQ9xxr6jQ0z3QI03OwEElQv7odLnBD1BLemOfTUW5mNB9Mi2R56wh7C9913EuLvQM3wQGuBJFaTGB-3Mu43-hWEjBmqxUMnqNiSZBYebYT9i93NQGd7U8bTfqLtUvVl3tVgvwpr2qd0tUwBu6QXAkjDcwxxPOoqUCta3ss8iQaXiYZRclusgcDLaV9UX65qQUARyhUmCvW7vJAN14SZqWKlkZN9NPnpa1QZ1zRTunkRju2fV-lj-X6-YlIhoE8QwWP4pee1LirEc5bekQu1nIU210obG3BGYKVJuGiaHgD5zbb68zASEgtbWFqWDcmHkZjShzrE3Y5LEE0GRKlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جواد خیابانی چرا اینطوریه؟
واقعا دیگه خیلی عجیب شده، یه‌چیزی میزنه به حضرت عباس؛ لحظه آخر قیافه خداداد عزیزی خیلی خوب میشه
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/24056" target="_blank">📅 15:55 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24055">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KC7ZcRlJaK-PxNIGGFugGqHaxDEEG4mk3PRWAtCI5ms1BZ91Jf5xtOQSBCP2kFpkt9o4N4uPSX9sxzAusfeG-aUWoJJXfy4vIDLijCwzJjKJq7pT0xvW4JMqUoLV_MCzJ-zIlo49n115mR4LbVQl5DdEtm15yKDM3bHIq5PLd4DYuzAEDHJL1OQHfadtxKFO_3RXx3gsBdzaNFBt162RmY2w86RDsBLAtimTxZkBRt0S7wXQxwP5p6nmPbZs1D249O8UhVDDfGsouucKMGcE88DlmwT7dcu-PpR0euyu1qA3SddRQjyXlMzEPQRgwi9fRpCr5hSVUJRbuAdfE3-uuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
👤
#تکمیلی؛ علیرضا بیرانوند با 7 سیو و کسب نمره 9 ازهواسکورد و نمره10 از سوفااسکور بعنوان بهترین بازیکن دیدار بلژیک - ایران انتخاب شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/24055" target="_blank">📅 15:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24054">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6565fae72d.mp4?token=T7i37vBdmXjDoc6jVKu9D64MifQLH-jtoFrFYf1HJdKR-gocjgn_Wptg_gTRRJCFE9t2XYHM6hGeUFQ5GaThPMQVAVZ9SokerF-MnGZPhnaU5wIyQ1THiHOqoOUW7exhR6EZDMeLJVR6FQ0J7Ip5Mfxpr9dGl5GiI_gb_DYatNZai4iJoSUMZWsRcamziLRYGRDkdt0C9WMsXGBSyxpJp2tZCO8VyEAj_nlG36PlOOsqwTYdiy0bH49mxUwQIZU1zRGYdnFGBC6gKQZruw3GndEEc6cO0LmzGauCPSqejUkmJvJptQ6xW6xEQ9JtOqG-py1PgKtCLFKQF4KrKiMMPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6565fae72d.mp4?token=T7i37vBdmXjDoc6jVKu9D64MifQLH-jtoFrFYf1HJdKR-gocjgn_Wptg_gTRRJCFE9t2XYHM6hGeUFQ5GaThPMQVAVZ9SokerF-MnGZPhnaU5wIyQ1THiHOqoOUW7exhR6EZDMeLJVR6FQ0J7Ip5Mfxpr9dGl5GiI_gb_DYatNZai4iJoSUMZWsRcamziLRYGRDkdt0C9WMsXGBSyxpJp2tZCO8VyEAj_nlG36PlOOsqwTYdiy0bH49mxUwQIZU1zRGYdnFGBC6gKQZruw3GndEEc6cO0LmzGauCPSqejUkmJvJptQ6xW6xEQ9JtOqG-py1PgKtCLFKQF4KrKiMMPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚪️
نمونه‌ ای از وضعیت متناقض جامعه ایرانی درحاشیه بازی شب گذشته دو تیم ایران
🆚
بلژیک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/24054" target="_blank">📅 15:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24053">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d16aWjPoQRmUWBJLky0pfGNE78av3J8wMk08KJiFSmLrZZ19s5QZZwgi6Dam8HLweH6gkikd45AyZHw17vNK_yvnQWLpUqlqHe628y_HD3NseVwHh9-YJk1WEKAHtHLCrMOtDiIhnhF_pm0QJ6iFHVRH6HWvrvjUMUymmiPQdfrGlXQo6Wc0ANhs3qwvpFyYAWh7OzrPRIZUEd3XURKtm5R6V3u8GPrCvGPDwMaUIuU778pAkOa0LSR3V9ygCbznFSvNHVDFb5YZrRq1sQ6QO13TVlgjvIVvfNM5bxCW0ERY54Cp4UkYzmmvUogJcvn2nMcBrxHJgsxNRa24pJWgnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
استوری معنی‌دار اوسمار ویرا بعد از مذاکره باشگاه پرسپولیس به دراگان اسکوچیچ: خدا همیشه خیلی خوبه... متعهد بودن، حرفه‌ ای بودن، با دیگران مهربان بودن و قابل اعتماد بودن یک انتخاب نیست، اصول شخصیت انسان است. داره به مدیران باشگاه تیکه میندازه میگه وقتی با…</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/24053" target="_blank">📅 15:23 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24052">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TaQCaYT22uW6wEiOjehp7nJzsqQZKNkpYHuUnpZ06U0amqRxX-OFCjxBsgCMmNKQPUh48-IvlfSCTp6sUbL1K_MqsQc63QddE0zMTxU-6MNvmx2m69oY1HWMsTuQc4XbjchAEa9dvFV6pW6A-gKOqUSbKPLkTGMICU4QCbzTmlEc0lbPvUUEUKz_FPe_5oW-Xzwu-YwtEBVknyvpQ5f7g6ALNaumDyqffKyicYUhmDeoNXzvQA5Q7KTLrcMxl66eAIVv0-zxUfDVSAUgmxQuCTMFHMYswG37u6R8YAfW06txrr91K8XQvReNY1skoxw3IASsZXvObgHg2SC02bEzDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛خواستیم‌بعدِ بازی امشب ایران با بلژیک جزئیات‌مذاکرات‌روبگیم اما رسانه‌های دولتی نزدیک به پیمان حدادی جزئیاتش رو منتشر کردند.
‼️
دراگان‌اسکوچیچ درمذاکرات‌امروزخود با باشگاه پرسپولیس دوشرط‌سخت گذاشته است که یخورده مدیران باشگاه رو برای عقد قرارداد…</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/24052" target="_blank">📅 14:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24051">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BrsK6s5r7fnRajp4p0SLziPUUhddHL3sQqAwYlph9dQixLOeytmik4Sw3w64gnBsmVnNwKPaXTv_f_hlRP3G4Xs_1HuTH36SVbe10gjYWeF1ki0U37pxI8IextknawneFZNz-Rfy5mRtXyN2n2xIWPNPuwj6NI3X82WCTsWEjGPiL1tfOOQT4Q4-bi-LYE200cGUT9kj32v---hMqfp5uaV1PInmKPjS-Fieclr6fp_0a_uZO_26CMxNQTI9-uNkzbGOGKhE9zLhP94k6SkVTs-9UcXK4WEomf7MUTNa-wyRN8WHEi6bepfB7j71wnQkEhvdfYLtOVBywWFoXYMymA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
در آرژانتین یک دین جدید به نام مسیسم متولد شده؛ این دین جدید که پس از قهرمانی آرژانتین در جام جهانی ۲۰۲۲ پدید آمده در روستای لا اسکوندیدا درایالت‌چاکو آرژانتین درحال‌گسترشه.درحال حاضر 3900 نفر در این روستا زندگی میکنند که مسی را مقدس می‌دانند و به آیین «مِسیسم» اعتقاد دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/24051" target="_blank">📅 14:09 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24050">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">⚽️
از دخترانی که اطراف ورزشگاه‌ های جام‌ جهانی هستن سوال میکنن که جذابترین فوتبالیست کیه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/24050" target="_blank">📅 14:09 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24049">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PM_EjY-ZQLKAGfWayghD7MlvH817yCuz35Yljy0BxJsAFk46Fyyaejuf-s7MWX2qb9VfkszrFrUhUIim1lcIDr-NnBYeU2NhWkd9hTaoGh8nU-MLzM9d2EOQaQd-m5dzbp4bnx9ci-eIWg2imeZHfb8BVMFp6dMwWqYKdjAM7k5r2vP22szg-Y7aAM6OakultQOb3pb8fjNzNmew49jJtngABbx5ovpgUqrM4frhZJHkSj8f_W36QKl7kl2W9AZDBOeWBdgv8zWludgUnn84aiVH2GRL4cV6X5-kZxMBDTDEIh-QnwlBeDXZWghgJJgc23yfPOft9ja5v8ZUDIK3yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا
😄
😄
😄
😃
دلار درآمد با معرفی دوستات
🤝
با معرفی هرکدوم از دوستات به وینرو میتونی تا
🤩
🤩
🤩
🤩
دلار درآمد داشته باشی
💰
🔝
فقط کافیه دوستتو به وینرو دعوت کنی و کسب درآمد کنی
این‌پاداش‌پول‌نقده‌ولحظه‌ای به حسابت واریز میشه و به صورت آنی میتونی برداشتش کنی
💰
💣
بالاترین بونوس‌ها فقط در سایت وینرو
پیش بینی کن و برنده شو
📺
تلویزیون لایو برای پوشش بازی ها
🛍
بالاترین ضرایب ممکن
💰
expert tips bets
🎰
راستی با اولین واریزت هم میتونی تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگی
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
کلیک کن و درآمد کسب کن
📱
کانال اخبار و هدایــا er1
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/24049" target="_blank">📅 14:09 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24048">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KS4vfviphsew9QRCrE8hndzCpE8QJ0Tve9T43mtxQn8UOFsTlXyjzp6Jtk1v-j1P0Hd95NeX3vgfxTlntWu-MaZdNMA0ztXQqEAshO2Fq4KrOJMu0gZrPdRU5GVyoVSYP-Z8nxA3ZLM2hgNz7Hb6VkcFtH3RH7IGOyssAdNB8_fWWJvPp8iizE-F1m5jpkh9QjX0cuiue5E337Yvkb_hWDrJgBnO6LRkhUGEHxMrwFa3JeExUJ1yl9ZFctYqZvgarMxoBizdLb4WRNFtXUD0XybBwJNDTKa5im7FjzZ20Km0lcJWJDttFzu4PX_5MPc9q4NHDyouSHhB3DKeD-5c4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ علی تاجرنیا رئیس هیات مدیره استقلال ظهرامروز با محمدمحبی و ایجنتش جلسه آنلاین یک ساعته‌‌ای داشته و پیشنهاد مالی بالایی رو برای 3 فصل حضور درباشگاه استقلال به ستاره تیم ملی داده است. محبی ضمن تشکر از پیشنهاد آبی‌ها اعلام کرده اگه با تیم خوبی در…</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/24048" target="_blank">📅 13:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24047">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hGI_flAFaFTD8iI3FC6ZUimOq4G2Pq5p57W8S0ePb24jSgvaoKmAI6jJqQP-F1cyu96LqbiGytcypdGkWFtlUNqHzgJL_9PrRnQWAMG4PuFCKT_icqcigUpIbsBSiYKAjYi7RzJXe141Y4T37kflxScn71c5dQYw-Z3Xylkd__jPrxF-YopozScGFnltyrWxxckExak4eiHlvlC1Mi5rhGQ_xTdxvgpr8sqWbNhIa8x2D9OFc0ctGFRGaclSSv5fd4KrCJBJwx-6JfHEy5VPJqsKSN2ksGmhnILBXy2MhqSVeTkzHfQoGULFGy4ihuYN5EpefTOQobRZol-6-l6AEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
تعریف و تجمید بوفون از علی رضا بیرانوند:
قبل‌از این بازی هیچ‌شناختی ازش ندارم اما عملکرد درخشانش در بازی شب گذشته باعث شد که راجب او تحقیق کنم. انتظارداشتم او دریکی‌از باشگاه های اروپایی بازی میکرد. دیشب فوق العاده کار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/24047" target="_blank">📅 12:55 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24046">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ej7LNxIfKHR-fSNXZXx7icM795bgXxq5h8C9fcz-m76fBTFYqWFKynEeNT1BfOQgO5yBH6m-efIpSbv1mM2iVJnZFQN8ofv4ox8Grl_TypjtH9b3JneFpdCmLy2IoBe9YQymJwRjZD94q_OoNC-XoqTtdy3pOXYeG_wnAgSZj19_XecZIL-uBXv0JLhZNVjvP_FjPtGH5RHJSd-xJZ08uDzu_98nHh7Z20ipp_jgaHKwJGfEJYNocL5SWzHAljT8aN0RLxmiqElz_3bGfzl85N1JfCarI5hFW9EYww_8FSAPu-UaJvIW6143-nbr4eMg1WhPyPLnoDYTRNTJRg6aRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ ایجنت مهدی لیموچی ستاره 26 ساله سپاهان امروز باردیگربه‌پیمان‌حدادی اعلام کرده این بازیکن اماده‌عقدقرارداد باباشگاه پرسپولیس است و درصورتیکه‌سرخپوشان بتوانند رضایت نامه او رو از طلایی پوشان بگیرند لیموچی سرخپوش میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/24046" target="_blank">📅 12:34 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24045">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FYgUBGISZRZJSveGdnwVNRYgUwronU6Qxj8J7_chjiMRRHmQ9d9GEZYQaBQfHbJvLXh4MsXDmbzw1w7dXx8TC9ofZrfZVMH8TUCsWZOvC0QV1jI15gPYOrcfE0VqlPEreeQG_m0x0Dz86nuZVmR5dfuGWOb3lebQ_IOIKGjHNGBY6TwdgxaBNBV3CiJ-SCnvDfI6rapYyxvtKICw1H_U5d5gGCQfgAkfTIiOKmDpPpmb6Hi_qFardV5ewEllVlUp7r1vkMSLGozkDhBN4mdQ2IZ2hiGLPgSZuTWHNNg3Dfvulg5WNn7hAcAzC-fPVllE6fUfZBFR_VHVTNhydwQciA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
باشگاه پرسپولیس طی ساعات آینده مبلغ توافق شده رو به حساب‌باشگاه‌روبین‌کازان پرداخت خواهد کرد و سپس پوستر کسری طاهری رو منتشر میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24045" target="_blank">📅 11:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24044">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I88vWWQZ6Z7RrD1YYcECZMYTgtFYEYH-rXe5yfHfq9WANMRihS-6ztDBOHNWtVhsx5AaLx-zjsfwr7wsziKxHEqHUURBoeBUWkKUKe7oszv5naawAGLpS6zFGc72pFr6XtBFe8BO0USOs_hTHKjlt0f1CBz03uldPoaukAJ2P-AFprsABWUYZs8Arhp2ypYTYGymzbZWlOx1SWXvns5MJCOweJYCCoPf3PuTUZY4sPmOQ6NKTlYmhqCKxZh_J6a9r_Ex7DyC169gYAwSH8ONdr5j_X77kEjGlvPdOEIFVtp0Qmhu6lRNXGgyQwwgH8qQJAU0WgaAVeJiCv5SzwkOTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ورزشگاه آزادی از هفته چهارم لیگ برتر در فصل جدید دردسترس خواهدبود و استقلال و پرسپولیس بازی‌های خانگی خود را دیگه اونجا برگزار میکنند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/24044" target="_blank">📅 09:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24043">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pq2_B6SOvNLwobKTL5FOp_Xek1HXMG_IPSgXZPhn4Fi1aWBLPnUZgb6qz3WaWL8MQc1ZJuhxADW0o1XXr5w0tAo_1tubVpqQ9jXCCJ9dtszsYk5OnDvXQAOkNViXN2iRi7sl8h9dNRa0hO-U-ue1eitlhC4e-Dov_iFOFq8pdIXOsBfMm4w6cwFUUxIzAQDy_597vvj40BYX8JciWdnK_c1ZuwEoRmMdZzqsKGwsDeHmwvakvw5wwI-lOmYUrIAF6Xa-96XAYwu-x6-KlyGP1QF-dVni3hRmE3NE8tvIXhpQpixKIwgu7zlLlkPB8lMJ0rRGjlZYV9nRDBp5bL7Ibw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
گل مرود ایران به بلژیک از نمایی زیبا و متفاوت ببینید؛ جوفوق‌العاده ورزشگاه رو هم مشاهده کنید.
‼️
اگه‌که‌فرم باسن مهدی طارمی دقیقا مثل سهراب سپهری‌میبود احتمال‌اینکه‌شاگردان قلعه‌نویی‌ امشب شگفتی ساز میشدند و بازی رو میبردن زیاد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/24043" target="_blank">📅 09:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24042">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fqhz2PRm6ndYMcYWmmmceEDpWPSq3fgzOZfM9tAyhUmIxNRO_0Ao-RM2sHzX7TV_fmI88GMppyMr3_Q_JeIKkh9XDYy6R7-edlQC2NdjlYdNwwrD0Xeo6E4OeCYXC9ivA9XCAgqot-PCq6ThHV77eqdGCKfloW_Xj3iPl1M-KaqOkvfiY2WtT-2OGT6woArBB_Jf7t0iM5xcU93AZOlnpR5kHE6FNhA_tBkeJAl1InbA-Jlh_e6Ozu-SsOmJjCfNkLCPKKnr-ryoiOFs_fgPsCUKRVksgWJeuoSbdXQ_Apn3qc3ISyKiyZ6Qt9tQM-VYuCnNoArbMvCcBNG-HZD9fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تعداد فالورهای وزینیا سنگربان40 ساله کیپ ورد در همین سه چهار روز اخیر از تعداد فالور های بوفون اسطوره ایتالیایی تاریخ‌فوتبال بیشتر شد. همینجوری پیش بره یه رکوردهای عجیب و غرب میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/24042" target="_blank">📅 03:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24041">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X8-MyjfT93rHeHwwIkLuC9Q3QLoNKJZ4cFAkMBMPLJ6G1N9CBCclNSIeMPsYTfMwQCLLONE7SchLy13NZAZHTpEeIJyEovBF9ldZcE5pcLpbI01l7AKeVlPNTU4Kp2X8x_YEP2FES_C0kfLxlDm8D0QMzQyRI7Td9-vsKKMJJXzukHGHunkgvWysFpqiaCyTFT5VKKP13J8OMXwlp_djUd1lJTA0-vB_7RYfiA6qqvn_0Yjx5K1ECLlqFqHSUr_9AksqSv3K61YKWfQJaOdGvSdJ3qk9YKLadV6jJEW_8NZ8Zd8bOALUw088_PFaxY4h_kX5NomzPQzgQwMNmhH9Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
گلرایی‌که‌درتاریخ‌جام‌جهانی‌نمره 10 رو گرفتن:
🇵🇪
🇳🇱
رامون کیروگا، دروازبان پرو مقابل هلند.
🇺🇸
🇧🇪
تیم هاوارد، دروازبان آمریکا مقابل بلژیک.
🇨🇼
🇪🇨
الوی روم دروازبان کوراسائو مقابل اکوادور.
⚪️
🇧🇪
علیرضا بیرانوند دروازبان ایران مقابل بلژیک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/24041" target="_blank">📅 03:23 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24040">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">⚽️
گل مرود ایران به بلژیک از نمایی زیبا و متفاوت ببینید؛ جوفوق‌العاده ورزشگاه رو هم مشاهده کنید.
‼️
اگه‌که‌فرم باسن مهدی طارمی دقیقا مثل سهراب سپهری‌میبود احتمال‌اینکه‌شاگردان قلعه‌نویی‌ امشب شگفتی ساز میشدند و بازی رو میبردن زیاد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/24040" target="_blank">📅 02:44 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24039">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94e90d0111.mp4?token=pJHZczcJKhThm9LDod_BcYGK8EI0Vk935JT2WMQCy4IzeNbctjxxaFwd7mdx_vInhb_k2IZzfiVVutWipgCqT8uCN36ik4iMjMscp7ROyRroG2ycTxaykYjQRo0Nt4chBCI6KdDMnnGOJUkIAfNjYNf7tEPkwtDCJcl_N0uHggU6s7TUx_Smlp5Slzb3HPXGOhYQlR6-iIa1nM5EPevU_nUS5F5t4PO3BdrjALQt2p68MV9MvNWO61c7GFv0GTsK5CZo0Ux5gtGEeCDUNBJCFU86hEVbQ8fphDI5BzDb6ZGxVbCAOmYLRX36_O-4o5YPmZq5mLQqoa_9LZn4i-fWuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94e90d0111.mp4?token=pJHZczcJKhThm9LDod_BcYGK8EI0Vk935JT2WMQCy4IzeNbctjxxaFwd7mdx_vInhb_k2IZzfiVVutWipgCqT8uCN36ik4iMjMscp7ROyRroG2ycTxaykYjQRo0Nt4chBCI6KdDMnnGOJUkIAfNjYNf7tEPkwtDCJcl_N0uHggU6s7TUx_Smlp5Slzb3HPXGOhYQlR6-iIa1nM5EPevU_nUS5F5t4PO3BdrjALQt2p68MV9MvNWO61c7GFv0GTsK5CZo0Ux5gtGEeCDUNBJCFU86hEVbQ8fphDI5BzDb6ZGxVbCAOmYLRX36_O-4o5YPmZq5mLQqoa_9LZn4i-fWuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
گلرایی‌که‌درتاریخ‌جام‌جهانی‌نمره 10 رو گرفتن:
🇵🇪
🇳🇱
رامون کیروگا، دروازبان پرو مقابل هلند.
🇺🇸
🇧🇪
تیم هاوارد، دروازبان آمریکا مقابل بلژیک.
🇨🇼
🇪🇨
الوی روم دروازبان کوراسائو مقابل اکوادور.
⚪️
🇧🇪
علیرضا بیرانوند دروازبان ایران مقابل بلژیک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/24039" target="_blank">📅 02:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24037">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KIN4Ww-9qehChu8q5hoD31LDmwrzv8kkryt4PaTZrR1L28XZV65vP7zr7H4676P6XQQ2fLDK6zjsko_xY5NZ-DCm2vuy0nHIWdgDQcQBSU0JCGAtIpmNdqnyYdbfyDA64tXmzThVnL0qJFUCIdOFu-Zarl2d6Cr8epnJpWCGqto9-CZdDcryBjFXSX8E5ofRsnU9UNX1ZZgU8i_sLptvFTjXlfmX8UUaLwbzBBgBeCTwv6LedOlJNph6P74wScB9TbXnIYA9hLnlF2ou--Hv8GMvzLfdkcgV7z71T6X7aXalNaJLX3rM7yWFNjUIRPSUkOffdd8XwpkZzGekoiRdEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
گلرایی‌که‌درتاریخ‌جام‌جهانی‌نمره 10 رو گرفتن:
🇵🇪
🇳🇱
رامون کیروگا، دروازبان پرو مقابل هلند.
🇺🇸
🇧🇪
تیم هاوارد، دروازبان آمریکا مقابل بلژیک.
🇨🇼
🇪🇨
الوی روم دروازبان کوراسائو مقابل اکوادور.
⚪️
🇧🇪
علیرضا بیرانوند دروازبان ایران مقابل بلژیک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24037" target="_blank">📅 01:54 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24036">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GWNpHlyN0yp3D_6apeEEFrMiAktooOG4T0FyLDynu-aO00IN3bcEP8m3eRqWec0zKO_wbM4HvQRNOTn-2mok49LyRedGb8eWhbw6o3TKaOUu9xu6SXrJcQNw0Pwik01LMxYGyYM9VnD_VMzdkj1IELY75HhEAOi8tpqwf7JTBbdHH8f7ifqwfrOzrmlK1_4IG0ZZcaTPt_GsBDU2Xn5IsN_-MY79kp0v87d2VeTA50xuaXrM-zMB98A8WUhF84MglIBofzVOmrE8nhaoQqzD50PaS_QNWQb7pDvOh3vlJUFS0EoSHyvCD9izgnIt6nYKrZNbye7Yxm3BPVPQS0n7vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
👤
#تکمیلی؛ علیرضا بیرانوند با 7 سیو و کسب نمره 9 ازهواسکورد و نمره10 از سوفااسکور بعنوان بهترین بازیکن دیدار بلژیک - ایران انتخاب شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24036" target="_blank">📅 01:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24035">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d43c42ae5.mp4?token=ldum2j3sos0At2Gkl4oJW4iHUsuQZJn5nWifENkPalzV8SwHnZ7aLuQ5ZQ_EElrHXctrCQuwm6vwJiw0Eh6yLknlp5rQk9hcJS6EBPHFNmGwX4F2tTfhow0uDh4Vg-A_uZF_PMFQ6I7kfYakyCNPdFLu0Mbaa6AL2zWe84EL8Atgt3L6XWcPqgungKevM-ZOHKrR6wEeYAXCTSnxzMlDr_ouilmEVWA6lOP28rX-9lpNGRAasfsBcdDgcMOvPs5i82dgCJb8KaGctXkXto4wUXCxAoCagK-MEbkDnot2PON11EL5hb_ZQ2CDCOGCfzsXnPcVfVXGvzPwzgnsI7ANvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d43c42ae5.mp4?token=ldum2j3sos0At2Gkl4oJW4iHUsuQZJn5nWifENkPalzV8SwHnZ7aLuQ5ZQ_EElrHXctrCQuwm6vwJiw0Eh6yLknlp5rQk9hcJS6EBPHFNmGwX4F2tTfhow0uDh4Vg-A_uZF_PMFQ6I7kfYakyCNPdFLu0Mbaa6AL2zWe84EL8Atgt3L6XWcPqgungKevM-ZOHKrR6wEeYAXCTSnxzMlDr_ouilmEVWA6lOP28rX-9lpNGRAasfsBcdDgcMOvPs5i82dgCJb8KaGctXkXto4wUXCxAoCagK-MEbkDnot2PON11EL5hb_ZQ2CDCOGCfzsXnPcVfVXGvzPwzgnsI7ANvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👤
گل‌اول‌ایران به بلژیک توسط مهدی طارمی در دقیقه 27 مسابقه که‌افساید مهدی طارمی گرفته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24035" target="_blank">📅 01:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24034">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pe2ruXU8O8MVFCnDUuEFBMvUwz127LICPM4w86eKftgSaeKyXJw-MvqhHpeH4Od2MvPnCyHjQDfbv89BxznpH14JomKc57_ZeQ-kSQ0XC5m3hfmAcDWUK34_zCu2Uy_olxqG3NmB5ZZ442ICy-vlU2UBCbpHSRvkA3BZqWEydliagaw5t7h19y2YPmAVQPYsWwzVryguGKMoKQnG3IBp7-zsGo4BbwWoeI3g8GTagDXTPxZVHhkmSfh27bKZ2UhjEoO-579w52C8l3s4lCUh-mVB_oteq7MGin4CNe3r21pVve8l1ZMOncNbanqaGL3Uv8FIcBPvnLrS1rRisGyjHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
ازنبردتماشایی یاران مسی با شاگردان رانگنیک تا جدال فرانسوی‌ها مقابل عراق
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/24034" target="_blank">📅 01:28 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24033">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a2HsUigjNk9TnTe3okeVi2yg59PtEoBpjT5pR6qZVE_tybJgSBeOlF6BGeta2YC_YxsHLppvLooI9jhEy5w9cJh1Mk_18DlWTXwLRpXwZUY7oWVU8bu7412wWGrMprAU9Qdzhf_lblE53-8ipdEQX60zpWSz9BMH703gVzldin40Mgih82CLe-s_OYfxetelRLe8GYOxXTgUeVkdw8QBwCW5-q4EOv_5_n3kcxKITXvIbhFqIZ49N7nXc01noqQW8NeLKb65xh3QdB-P7Cu_mDu8Cri96apZXIamtpTt76fLk3PUodRSboLJ8kIGrgKOx6u7Fu4B7edDAV3q9W8Q2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌‌‌دیروز؛
از برتری ژاپن و اسپانیا تا توقف بدون‌گل بلژیکی‌ها در جدال با یاران قلعه‌نویی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/24033" target="_blank">📅 01:28 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24030">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77de046aa0.mp4?token=hhWatSmWvtsEMsApUjZjs1sZ2SIfmu-d4qe7941ppG7hea8ZN79ykrJ0HY1WRzpjrRqAAUmDhyhDMEJ-bivCSLK996JuQMqi4Ql2AHFICrsAaSxv_vdIAzKsCRGT9ZefKj42uUHCwv3BvSonZS8rVih1iidTjTJ8UzFwOd7dwZ0V7mK23WzZr5j1MHIDjSKr4o20F_yXk4qm8gdudjZwvGsxPQdyxYmeOc1A8ffDOxdK9N-JlPKTZvoa8ac4XEtIeNtU8HB2KkT3mojOfBCg01AWJLX7q9yOvFnFFyA7_xH3SBRzHrmSamLLFqM9t5e-Q6j2LN-vYf6_HgM17M-H_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77de046aa0.mp4?token=hhWatSmWvtsEMsApUjZjs1sZ2SIfmu-d4qe7941ppG7hea8ZN79ykrJ0HY1WRzpjrRqAAUmDhyhDMEJ-bivCSLK996JuQMqi4Ql2AHFICrsAaSxv_vdIAzKsCRGT9ZefKj42uUHCwv3BvSonZS8rVih1iidTjTJ8UzFwOd7dwZ0V7mK23WzZr5j1MHIDjSKr4o20F_yXk4qm8gdudjZwvGsxPQdyxYmeOc1A8ffDOxdK9N-JlPKTZvoa8ac4XEtIeNtU8HB2KkT3mojOfBCg01AWJLX7q9yOvFnFFyA7_xH3SBRzHrmSamLLFqM9t5e-Q6j2LN-vYf6_HgM17M-H_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فیروزکریمی‌پیشکسوت‌فوتبال: بیرانوند درتاریخ بی‌نظیر است ولی لطف کند کمی تنگ تر از این باشد. این چیزی که ما دیدیم خیلی هم تنگ نبود واقعا.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/24030" target="_blank">📅 01:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24029">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ms1a74pSQt1q10fVZav9AGUq7VJVwlKr8a50RFNAGFqnP0yL38el_GyHA6GnkriTLS-n7RS9-PXwjRtCK_VYHFNL8M0W-IwD4KSgLDxjwCeNHCUcBnSkMBHZ6RvnS2ueG5bRaSx8BZy01MCY2Rs544wlmG9DYAmWsVFvAYvEXqSpS5I7W3bBO9jw3J7qGY7tuR4YxKjcVy75_WImDGNeT-OsgBzUTdWG6GcTYfZTonbBiwiYuUiY2MD5n5mdrTUuNH0DiuNU5xvHuJVmM-34TecfSVtzI5hjDTuCz-pHr-dS2Ob_N8_KPPcmdlvT8pjyPGR9f2o9uRQTSizzIX_aAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم جام جهانی 2026؛ دشت یک امتیازی شاگردان امیرقلعه‌نویی مقابل ستارگان فوتبال بلژیک درشب درخشش‌علیرضا بیرانوند؛ سوفاسکور بهترین بازیکن زمین رو بیرو معرفی کرد.
🇮🇷
ایران
0️⃣
-
0️⃣
بلژیک
🇧🇪
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/24029" target="_blank">📅 00:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24028">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lI4nbtVAFOtBe9bMP48UGVoMC7gYdo8PBPHHm0kVeMcwmgN8weESeMZj-GBWKiMIiB3rn3YJUoxU-StT_j7Sc8RsN60ktq1AZih7paSeS4dbwcM5ECz-tQQIdH4_SHoyJeR-mgHuYEi6ZaCBU4Kf_cEm29GpaJ64yvdNhSNZgXxXYQtzagMLEe9dyVwcOfZiY3TvezDnf3bNM2p-Ar4ZibwgS4Jnhq9PEifGaTsPI9Ol97kbd5rKUWYV3ULG5O0bzBeWmEz-vbmmtrFDVbZxNOTweTQ5PBlhXqFzEKarldogGfDBP0h01reeVgAO6COBD-74N7kr-np8hgrQmZdu6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم جام جهانی 2026؛ دشت یک امتیازی شاگردان امیرقلعه‌نویی مقابل ستارگان فوتبال بلژیک درشب درخشش‌علیرضا بیرانوند؛ سوفاسکور بهترین بازیکن زمین رو بیرو معرفی کرد.
🇮🇷
ایران
0️⃣
-
0️⃣
بلژیک
🇧🇪
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/24028" target="_blank">📅 00:36 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24027">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aowJv88LhQ3MRrwsEPjxfVtjg_56yq6CcQ6R6oEbgz_UfOR2qeCuZh3nhl5oS2t7GIBgE3E4XjzrIv3iV1TVGGsirHKPRe9SIvqrRyMlPHmRjcdMdgYORg04mOxubaGAsQ_CY7qRYbX-EqNqZY2SP-QGkApF_X-5JLdMGlzZ9Hye4mlm_FhHNT_-5ZhLPMc2sA1WSQUTshjHPUatPj1ZybXepaf2Er3ykvg8msVoJ12v-4L2KuLu8Jc9ZQX5BhD7WaeXplTwS3i_NOTlzJ4y3q_ildit2oNWJDN2r0NhUbRE49DCQAF7YrdmkXoy0VkBkdGGjC3nnOcvg-DyueAJBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
یک واکنش دیدنی دیگر از بیرانوند که دروازه تیم ایران را از فروپاشی نجات داد؛ تمجید رسانه تاچ‌ لاین انگلیس از دروازه‌بان ایران: علی بیرانوند مقابل بلژیک بهترین بازی‌ دوران حرفه‌ای خود را انجام می‌دهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/24027" target="_blank">📅 00:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24026">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54539b7e86.mp4?token=jMlMAO5GjnuZwdb2Le-vmwHWTggNuTQrIhcEfAYAXczpn-gR8cv4zmslmKHDbR792h-_uFcQQyYPEx95MnYuPgcP9KMNEosKKpAogG6y7FidpxyTGY4ZOPvtO1FUU3a-B3E6aBBD_ChXvF9TjpcDHyakLHWhNR5KUCjXYVlj9CvHWK2FrfOqtpUSO3QFGIaKFiTtePDZcOc1Ap8nvtVDRPUyJKJD9w841RkrxUvGELb0Rl2uj7Qx0XSM5unG9-xk3MPZB0mdfdq02Mh7CZwivJzKc__ZUMQCzs0fi2IMsOSkRkIKnHGxP6qb1ynCH_qqVHTWmjElkynWmbaLh0hVUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54539b7e86.mp4?token=jMlMAO5GjnuZwdb2Le-vmwHWTggNuTQrIhcEfAYAXczpn-gR8cv4zmslmKHDbR792h-_uFcQQyYPEx95MnYuPgcP9KMNEosKKpAogG6y7FidpxyTGY4ZOPvtO1FUU3a-B3E6aBBD_ChXvF9TjpcDHyakLHWhNR5KUCjXYVlj9CvHWK2FrfOqtpUSO3QFGIaKFiTtePDZcOc1Ap8nvtVDRPUyJKJD9w841RkrxUvGELb0Rl2uj7Qx0XSM5unG9-xk3MPZB0mdfdq02Mh7CZwivJzKc__ZUMQCzs0fi2IMsOSkRkIKnHGxP6qb1ynCH_qqVHTWmjElkynWmbaLh0hVUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
سیو عجیب و غریب و استثنایی علیرضا بیرانوند که میتونه کاندید بهترین سیو جام جهانی 2026 بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/24026" target="_blank">📅 00:25 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24025">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94db339245.mp4?token=OOHyRbxENwfl-kkbGhHcR0T8ene4ODN6p0M0nNmY7iuB_YUDy1S4QIGrQYtTtWv9bas7s1dZMtAW34y3NQIozq4DUV9kNotf7nrYd8lq48xR5D5RV_moZBc92cZ6hqJhJaejpTT6uFx0QBt2I8f1v2Z7Egw8H6o0flZt8bbFENWXhb5cpvj8D_2aDJPVcGTW-LLTiPJyrTEdRkSih9nND2eYtjeazf41WZ4zCxq3pJ6dBYckmXPjbnuDHiYfHQ2wMWBIOXr2B1NvLFHB5YL2rzcX5JahGOIpVC0AGfdAEhDTLlNzTLNxu4dZthTQQ0TSKMwxbv9W_40lTcYyETn56w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94db339245.mp4?token=OOHyRbxENwfl-kkbGhHcR0T8ene4ODN6p0M0nNmY7iuB_YUDy1S4QIGrQYtTtWv9bas7s1dZMtAW34y3NQIozq4DUV9kNotf7nrYd8lq48xR5D5RV_moZBc92cZ6hqJhJaejpTT6uFx0QBt2I8f1v2Z7Egw8H6o0flZt8bbFENWXhb5cpvj8D_2aDJPVcGTW-LLTiPJyrTEdRkSih9nND2eYtjeazf41WZ4zCxq3pJ6dBYckmXPjbnuDHiYfHQ2wMWBIOXr2B1NvLFHB5YL2rzcX5JahGOIpVC0AGfdAEhDTLlNzTLNxu4dZthTQQ0TSKMwxbv9W_40lTcYyETn56w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
نمرات بازیکنان ایران
🆚
بلژیک در پایان نیمه اول بازی؛ علی بیرو دومین بازیکن برتر زمین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/24025" target="_blank">📅 00:07 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24023">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cqQm8kxUITzxLxc0nPw-jm4JdejQpMoEu1nORDg5BpzBJMx-Itvkfl4fFLfcahZidyYiB2_qqYMjV_nCY04rhWE2lktqXPdqr5l_Q-YtFx0u4LLiV_09Dk3hpSuGA8yH0VixTDssQHYt2wHnxC_g_ASjvNRAdioW87heMuSFx9uiM0rkZ-fzjWfzfR9Nt1xd1pq8ruANsVv5aBWsigesxvO5I3esO7L3lDH4sZyoO0p8RyzkPs3P-yKo3D5JSmzBqGT4r8oxEb_WcKvQH_HHCcmHP1s7c8pIJ6vOkX-qTXH1ki_lDTPQP6AO_0sxki8pTzHwObFeODCw0dtW2UwooQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tl8l19-QL4HUx3nXtmobOxXPHoQA3Rqgo_8hHndDGKGExo7YzZT-C6PyN08KhjbDUYdfHJc7fcHH5aT0-SJdEp-aHERMWlIcc79VczmKUXDHgRyR8l2Hr7CRaI5VpDHY2Ffulx6B1nj0H7tG4uHfApQ5vBSzfTSrkzdP9XrdULnVlJmlA-OZlh0nRasc1upCCEMVf_lw4uBrIcUYgDdyGj0qrwTahwes_ub1MZspwT4YtC05cGNY3lc_SewnM1XYebJZHeIgXFtkfEUlHXDdhVDrbSd2msg0mPhdaRaOiigeZ6EUG03tu887BHcWhFV-IAXPILaNgQa0u_tk1OsLKw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
آمار نیمه اول دیدار امشب دوتیم ایران
🆚
بلژیک در هفته دوم رقابت های جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/24023" target="_blank">📅 23:37 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24022">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QMiZSalpKYo2ixXjdlxsy5EiIpBA0pU8ENoCfPduxuw9YGfGD3cLqiz9TJkjdgq6TzMaVJDY3bQlu08m3HMeVwirFb_oQqgJQ-x8WEHUTPtql8eXMW47nQ0GI00lXyn_fsUliVExwzkRxlrShl2zkSMCZp7_cow9P4lo27sLMNYDhKJNRPLBmGUKbol8Xt1nguJ6e3aVleLQKwc8yjxHIBWsYilZvG-BTE_Isq3NCLj358a0VN3_w3JMne1oV_24I4Kk1pE_J45d7pqIJbrdGl34JBbHopVd94XwaMG6SYg2bm0zKbyAXblUhxaAPBvDfrTLTDkc0e9Gy17RHQmYRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👤
امیرقلعه‌نویی این تاکتیک تیم کومان در جام جهانی 2022 که منجر به گل شد رو برای شاگرداش گذاشته اما غافل‌ازاینکه‌باسن طارمی توافساید بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/24022" target="_blank">📅 23:26 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24021">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a43b24a8b3.mp4?token=TaHqCiVIIVoJPFGy3CMuZgpFp9AWW0_4PlyhJ8gu9Msex8UQwfmZH4KUFf_zDJUGpCFPY8yqVZkeu8X03WGsLitbDvBLU9keL0oXQEdBdq88k8Z4ibDbmww3FvYGI71vN5_oDAPxw16Lx3yyTMudmmiEakjEygjW1kcufUTmO3mIfciWWdhtkdvuU3n1LS-nE7qDFZHjtz2GmkyDiJgG3aeHXF0RZ75mey97cD1L5jSyKPBdxe29d9vB_pw8pQjaeWX2CVoD7CpfxYYCrAslijn5BmLDtcVUhjUPMF1_uMTqmunhhSturUE7_Fbp7bQ8gtE1L4H3Ny0bM2MoPACUgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a43b24a8b3.mp4?token=TaHqCiVIIVoJPFGy3CMuZgpFp9AWW0_4PlyhJ8gu9Msex8UQwfmZH4KUFf_zDJUGpCFPY8yqVZkeu8X03WGsLitbDvBLU9keL0oXQEdBdq88k8Z4ibDbmww3FvYGI71vN5_oDAPxw16Lx3yyTMudmmiEakjEygjW1kcufUTmO3mIfciWWdhtkdvuU3n1LS-nE7qDFZHjtz2GmkyDiJgG3aeHXF0RZ75mey97cD1L5jSyKPBdxe29d9vB_pw8pQjaeWX2CVoD7CpfxYYCrAslijn5BmLDtcVUhjUPMF1_uMTqmunhhSturUE7_Fbp7bQ8gtE1L4H3Ny0bM2MoPACUgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👤
گل‌اول‌ایران به بلژیک توسط مهدی طارمی در دقیقه 27 مسابقه که‌افساید مهدی طارمی گرفته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/24021" target="_blank">📅 23:22 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24020">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d61647a74d.mp4?token=C_b-byjcRoNtdrvLAXDFmDn0bBOIGyDr7gogsw8fWxT4qXthM9cxH_2PsJN_PJAoGXZVDygKBv_JBlq0Di04jXAasxCmY9ZofrFPzr20CMruittoq5rEDDUvhHnMPS6Ti76Ad6zQvBDN4S60GbgsyXC90vBYv2oZCNlHWCwefx70ZqRe-PkgElIJUio8ikd-XKoQH6DiXtlZO-d41808V2HSY1BIQfKfqpF24ZYsa_COy0aAb7SsdElU8zv3EC1-ja2X-L-tz22GZ-WQ26EXEpaKiI9cvmt680xEKI4uhwP8LPtZ7ZoXN7OiqVfpwFtnDBB1DMCoXYzxoL2OxJyXng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d61647a74d.mp4?token=C_b-byjcRoNtdrvLAXDFmDn0bBOIGyDr7gogsw8fWxT4qXthM9cxH_2PsJN_PJAoGXZVDygKBv_JBlq0Di04jXAasxCmY9ZofrFPzr20CMruittoq5rEDDUvhHnMPS6Ti76Ad6zQvBDN4S60GbgsyXC90vBYv2oZCNlHWCwefx70ZqRe-PkgElIJUio8ikd-XKoQH6DiXtlZO-d41808V2HSY1BIQfKfqpF24ZYsa_COy0aAb7SsdElU8zv3EC1-ja2X-L-tz22GZ-WQ26EXEpaKiI9cvmt680xEKI4uhwP8LPtZ7ZoXN7OiqVfpwFtnDBB1DMCoXYzxoL2OxJyXng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته‌دوم‌جام‌جهانی2026؛شماتیک‌ترکیب ایران برای دیدار مقابل بلژیک؛ ساعت 22:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/24020" target="_blank">📅 22:59 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24019">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DrRhLwlb4b9JuUA-WtfRtCbNVoddksv4ttyixD5CelehKKjZ5-CopWWtJ3JCmrwZQVhH-s45arDpywHK8tIuz5kO53B4XR2xJrPIT8jvYHezfa9bCtaasPkPzsj_ZHpObGBdWVzGqlQ4m1Ow3MCYsJuglGcr7XnSxazmNl1innmUMzEfrhktvE2FZ36MzJ0IThQDRliRx5Yn2TaBA2Wyc74sLzp9Foa-kZ2Lg2yKNCZyCxDCpURG1kjfBOhDhL3EGaeEBRmJkw0udWq_UmWuM77VJdb6EsLDzkGwrH7kyoDeiwxpvb8fZ5k7bYQtN68glTu6ZGMIFXiVJ-5UvCBIkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇪
شماتیک‌ترکیب‌بلژیک‌برای بازی امشب با ایران؛ درحالی روملو لوکاکو و تروسارد به بازی رسیدند که سرمربی بلژیک گفته بود ناراحتی دارند و احتمالا در ترکیب‌ نیستن. احتمالا خواسته به ژنرال رکب بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/24019" target="_blank">📅 22:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24018">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GvDOBFpjbk7EDRjYuAsO9kq14LI5utHhvbG1nc74ftC0fw5vWl54wPllC8sqHfo3iPGcMPo3cn4Qu3By0vEmkrhgyTXQPIrq8ba6YxBVwFS12_AavOyu0AMoq8AbEoDGQFjKVHz11DRoycaIl6OvNIZ7EWTCk_0ks9NZO7tNTt-qPPdJXzxU7kuY9K0tTzbVSRK8a0iK3Z0Zs14gLceVyLO4F8TguUvbvnZDGaUNidIoOPxn5U7bISP_NdTGicVQYNQ2tAcMUnvfvVFJi3pmjveU0kRtG6eNR5JLnvxBL0D1aBiW0GRqBSnE57FyWojiKKoNbdknjnt6YWPrvHztuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
پیمان حدادی مدیرعامل تیم پرسپولیس: تا پس‌فردا بین اوسمارویرا و دراگان اسکوچیچ یکی رو بعنوان سرمربی فصل جدید انتخاب خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/24018" target="_blank">📅 22:03 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24017">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o1xU_53mNlHKVXMhVEhzkkBRRlDsk2vOelxA3pY5LOOpn_n7xZEbZ9LZzapC_rFgg8oBUAwjIQooS-_hGWeDfccw5FLyLvzrg6DY852F4oiU7JDG3TJEBhyB8uS1qI1XZ8jMXgvd-QztApYrrEIiBGcMtA7TOu8Y2jWcItKFbt-MQQA7120KlxTRwOLwsyfFATdQ1KY7K0oFm_Ie4xToi-UHoT2JC44PfoZPrbPKgfOkt6Dk1i0D_Q1W-dOHYm9PW3iExr7MFUV08igetYfzEtWc6bvfrbOkF9hnCUBWhI77-DvkGtLlg39cK27bGdAosoMgAHL8jkUYULJ2DknSxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
هفته دوم جام جهانی؛ پیروزی پرگل و شیرین لاروخا در گام دوم رقابت‌ها مقابل عربستان سعودی.
🇪🇸
اسپانیا
4️⃣
-
0️⃣
عربستان
🇸🇦
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/24017" target="_blank">📅 21:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24016">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">⚽️
هفته دوم جام جهانی؛ پیروزی پرگل و شیرین لاروخا در گام دوم رقابت‌ها مقابل عربستان سعودی.
🇪🇸
اسپانیا
4️⃣
-
0️⃣
عربستان
🇸🇦
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/24016" target="_blank">📅 21:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24015">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ckVScvF0tCDwL3FcfpIluf2XyakweYjtt3vQ11w0opb6JHs5ZP10LI5XoR3UO4iSUZWBBy4rKqvBS9CXrnlWRzvoAGFqmj5a8h4xtqSajvkgQM7GBviDN_Na3iJcwFKx-zplp_BeYEeNIoXfUIj0221WBAUlHJe1GZyVA5DnbmUMml9iz2DBTY6IH69t5vS89W0r9GMAmEIpooSVw07eTP7hFLs_aD8undXWmZqszfRTlLn3CzaW8BliNgXveN8pJKNpkKKTvDwjZsrk-0oVDa-MdRihrY_QaCvjQtx6agtjoqR7oRxuxAPXF_vt7s8nr-1TsVWFBqq-ethBphEEsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
هفته‌دوم‌جام‌جهانی2026؛ شماتیک ترکیب تیم ملی اسپانیا برای دیدار با عربستان؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/24015" target="_blank">📅 21:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24014">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qzij86dTJsVgw6hqkcltAYQnE7hn4dikAgopVaudtd0tfzg1839HP3se5cZksrYRWLCq7Vm0WC6ivbULXBPh7v66q15CAoqHxTGR8u-0YFrcwtlIfzmndlZxwR6AWvTHfErNtFpeOwk-UiVREZSsEzIeU_gt-RkKtz2khygpl4xvVQgl7WnJkHdLigAQDfm0u6mibN0MYgs-PhAPAJa0biGf4xzroc2dcBfiVwiHgLJJaiFK8NcTN1ZYpAsVZ70FkLNYMhjt93P5ZIMvNrWXUJ1eaVuR9o4udwSB73_3adyS8PGoHnPtTXGIhBDlERtsASAEMjALWO8aQ7wWhpQOyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌جام‌جهانی2026؛شماتیک‌ترکیب ایران برای دیدار مقابل بلژیک؛ ساعت 22:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/24014" target="_blank">📅 21:14 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24013">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N4Dg0pca_4d3by76ZfSVWb0n4nJPeCxaM-MqyF8mLFok2OkURqDDKs13nBV3_0L5ZLDp5ugfe9hmrlH-CR7CWJ_QfXj-zYxcmE6Umldb6x6Cn67faceHthEPgIPvalPKuuGDqZGR13AQibRov9YOz3k6y-Ip_U5ijYcvdVWqzEDFsvyssWBYSxLQ6zUWiTxz5siOyf5DvPmz1Htha80KDerFgsIIvFfUPeH3FTCJiKvseuZlAllJiJmlyotDS0AZvYSbWr_HYQ9gJnaAkvE9LDnIS7WtKPYpYpUJUkcwKgrSdgL_CKhXQkebz4Ssg76Xd7KXFn1IN8MYNPo5PL1RAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌جام‌جهانی2026؛شماتیک‌ترکیب ایران برای دیدار مقابل بلژیک؛ ساعت 22:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/24013" target="_blank">📅 21:09 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24012">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PDEJEPm5izOxe1kih9LWKBAdN44Vi0E-T4c9IgUS_cpYMS-KTKqYj4pvHXTO1gt4lkLm5-93Bu_El2GXVqCDM3QlEHztcna4g-ICtgXUewQZsMNfORRK90iTDcqhHJoGOtNxJFwgxkhP-FhxQ1F82H3S8GQZJB4Eq6HO1wCy-3hIOesMMQYToLr8zEDeoqLlWwpvEDmK8N3Ou83zoqpbgAAsHZMaiTxd74ojoe9JbWHNPyR30Yy1wFLLp-G21GqlBXvwz6s6nWO3DzMgEiylraHv1Nreol4CMAcznQnD_owvzIL15lTcJvTC2rNh2s_dx6JR560vUx3uf7oArQOmBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌جام‌جهانی2026
؛شماتیک‌ترکیب ایران برای دیدار مقابل بلژیک؛ ساعت 22:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/24012" target="_blank">📅 21:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24011">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KKDG4B5rkhUgKimcULVVD1tdudtIypNudyyTmelamgqCCwss0hpPSZ2mkMg0o0dNeveOMOmi1-l9Z73XC9AddHGugwfLnHah3qzxPfamggVkwI2rBpJM6KXZcWSAZe3W7pQD0GA8Hei7LA5_5cmZ4-inDqWjiPkm8z7GWZJk52J39s326ST_SGXg1xrKqTA7Tgp4-UFbucMOLVn4mczu2Awlw-IdTg8k5j49IJzBHGQkkkBOyZ1HXtw27WvX4qDnsbMRUNFsAhUDmy_HwQU-gWEe3Rn7xvRBi882yFcMJmyF5qfHdDeID-O0L1zeRdmWQYGmMEXZO_QbQmE1iThrRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛خواستیم‌بعدِ بازی امشب ایران با بلژیک جزئیات‌مذاکرات‌روبگیم اما رسانه‌های دولتی نزدیک به پیمان حدادی جزئیاتش رو منتشر کردند.
‼️
دراگان‌اسکوچیچ درمذاکرات‌امروزخود با باشگاه پرسپولیس دوشرط‌سخت گذاشته است که یخورده مدیران باشگاه رو برای عقد قرارداد…</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/24011" target="_blank">📅 21:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24009">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EXxiEczkjf3U9frXq5Taew7fqhv6uLSvwCe_5gwQkorOauFBaZUa7RpV6RualOYBPh64-F31mRoV-_m_Anl_bZywiBZjxjCKEANW3-Y_GKu_5wz16QJt5d8RptknQgB0GPG_DvvnbUBcL_fPsZPWIllqreZ_BiQFimKABx6BBldUBUwW_qTduMAG4jxiBGF5ihzX_mHVpMZd3VaeGvLdqrCsFnLGahEK_Cvw9UrDLjEKtUU19-hSOyaEm_Dq96fMhxZP4otpMtFjaWCwDHcSChhCKQQG120ALhXjRMUAcVB86ePgfQ62XldcoVj7Soiwi9LiEzMihvl7hLSvfIx9VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛همانطورکه‌بعنوان اولین رسانه خبر ازمذاکرات محمد دانشگر با باشگاه تراکتور دادیم و صبح نیز درباره پیشنهاد مالی این بازیکن خبر دادیم دقایقی قبل تراکتور موافقت خود را با این آفر اعلام کرد و دانشگر به زودی راهی دفتر محمدرضا زنوزی خواهد شد تا قرارداد دوساله…</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/24009" target="_blank">📅 20:44 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24008">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c-LC7uPIrgiomO8U1WQfjwP1ggxtTn4ZfZLiSqy51yW-LjrsWkye_xbTGNZBV1v3HQA8kE69Liy6zqyK87PLGJybpmPKvnRF8yYJgX0HazxhyjTyx1oCmAfOmUh7CMRp7K4HdHNPfGnxi1aSfmv3DyH3bMpzk5kMYwOND6GBD8hsRPFePOQglVZUOXRzbSMqBDneDwY3BPXJ_0m50zEzfGH7booEWFJPaRPDWOAIyKwvQkrPWKJMwQ5s_IM75OHx3Ni4jfqb7iNXmsRHvXuaepOoFdjPiT4GgEfXXPKvX6S3tmBAmYrDQwzBIZdT0B9aPWYolBXBsybGAR0bgWDqBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
هلدینگ خلیج فارس و باشگاه استقلال برای پرونده بازشدن پنجره نقل و انتقالاتی آبی‌ها روی هم 850 هزار دلار هزینه کرده اند. وکیل ایتالیایی آبی‌ها هم‌امروز ظهر ایمیل جدید به باشگاه فرستاده و گفته شما تموم کارهای‌نقل‌وانتقالاتی‌خودتون روانجام بدید فیفا پنجره نقل‌وانتقالاتی…</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/24008" target="_blank">📅 20:27 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24007">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WHSnA331ueeKkxom0quLecW82VaTvVlxf-_m1FNJraRtR_m-ZEv7Ed5sM2h-bEVlfdDm-jEvugN3gZfLQ_pn1P-lrQ4R8HPR3NOjBIlhkevcTctQZfchVnfIQ0Pnzm-mE53n2moNCU-nmMtirEjnAdHwOiQmlBFn1ZstOV1nfkp1q5FnAaexM9V3ugwur8S3ahJMcuKMReQKuqJXIXpvkWgWwE1SXfkvnHuN7SToj5VP54MIXrf_q0WGF3AUhK7-ACtOEfYBv5VFqWD78Gz9sFKlYcV_TGc4_OMPH5MZuV5JbBV2oINAkQ40qIkfLdieYwe7cc8TpuD4bMuvtp96wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
👤
قرارداد محمد محبی با باشگاه روستوف روسیه به پایان رسیده و با توجه به اینکه برای تمدید قراردادش‌اقدام‌نشد او بازیکن آزاد بشمار خواهد امد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/24007" target="_blank">📅 20:03 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24005">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JR8RR5UUpVlIcPZBOZyHQrPaiTvbbmhOuDekYkbXamLMhZ1eexIaurV4bZoSepGvNtJWJGgrW28wNoh81Q2si1ugGtKyZYTArYjoQqYvVQ5l5t2a6bEmB0u9eGLWmDDfwAucj2nLsyZXdguaZEOKgo22vSX4sbJtq7UmP3ZxbLB5A7dwNqlYjy-wu5C5IVybmy_QCrDJQFCsgWuz9D_ei3nRYmGbGWCgrp0qbAnjSNWJBkwVT1P0fhiPrv4jfN-5Wxv5H4Ko72T-pPMe1vw8vTfutSPr0NMFt1GiBvy48Ci_Si9pX2z_M50E_iFspW6FXPerduTpclNo0uVRP66a9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ جلسه‌مدیران باشگاه پرسپولیس با اسکوچیچ و نماینده‌اش‌دقایقی قبل‌درترکیه به پایان رسید. پیگیری خواهیم کرد نتیجه جلسه رو تا پایان امشب بعد بازی ایران اطلاع رسانی خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24005" target="_blank">📅 19:35 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24004">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/isC6S-ge5AvHrhd3igc8cSdfTz5vTuQ-S0c_wF3Atr4SIJEwsJ19itDQpQ4Zaqp1YbUX4q-AJk5JTmHTx68nAq3fNPr9gDVtFzDTNIadEfXxxZsyc32qLfs3YRXFKdvwndXTvJT8BDajDKLTQcublKhE6K5q3vIG1YHPFu5eTnNJ03YhkLyDwdboeiac2hkbnDNx92bT6B9kxfTXNVnJeky58oTKEjb0UlLeW7QyEKaXgqXBIhvi1RxfaCawibg02Cxm90bIBp4Di5AZV2rYyz8tG_V5OPnpXbzSjiLe6mCD34UA8Ezp6_-AR2rlYxWYUoXT8kGpuWfPXjIDDdHMLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ محمد دانشگر در مذاکرات خود را بامدیران‌باشگاه‌تراکتور برای دو فصل حضور در این تیم خواستار 190 میلیارد تومان ناقابل شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/24004" target="_blank">📅 19:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24003">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Jw5WPsXy1vDPujCNZXLCX1h7wvkpF83Gqzfj1JfUBUFHYLuRFBRev6ycPT37QMXgQ5421YcSkPS26w7FpUQ8CMPygR0yyYfT_IwgnkzVo8pCCTOZBnmL3wBnajFs-3W7sKe-GCZPjmGLpclDw3Vaoq5u5sQE50hOhMGsuR56Rs8jwGoYfS0_eDT-9Py1TJk96UvLrE8Zh7PzrBip5gwxQqkeyaGa65F50sdfSLy4ly6hRPiMYMCbv6uhKjbwOY0uKte2xOUf-qaMpF3uxKirgVY0QZ7VgBnuOZ8Z_q4CGo7Y-R1bOeltgOCEr87e2lRRyViltySxcc5xuUTCUicLng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
کشور نروژ اعلام کرده هر کی تو روز عرضه بازی GTA6، بچه بدنیا بیاره، یه‌نسخه‌رایگان از بازی بهش میدن. وقتی‌نمونده اگه نسخه رایگان میخوای، همین الان پستوبفرست‌براش تاکارای اداری‌شو انجام بدین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/24003" target="_blank">📅 19:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24001">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GtxhaDKEbWXrxAuMdknYYhfz_oY0xdhlk5ka2Ghz4bAVyvrlWGPYnrtmeWVvUtuseGfevBkW2ELVRVkl2Nb6dwuUdxuA614UMS9F5vIACRpbvii7ZC6T6LOcbwkxb_IyRkGUCUaGiBTQukR3r2d1KTF4Wc6blL3DcCXGYD8_Yj9o9FWsajWfyo1rqOoOWfs2mJYXtu0W0o9Wnd0gdNuIrooL4f5lBiNPQTKZN9oRQQecewzCypPak5lkEunH6uNLPNha5NEEpMX9dyJwSklx6y2sPd80CLmYAHGZ_asQOfd-wfSsh9ZpQI3uctC_sJleDb9xAVUO5p7ytH_ZPUNYfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیاست باشگاه استقلال در این پنجره نقل و انتقالات جذب بازیکنان جوان ایرانی</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/24001" target="_blank">📅 18:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24000">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FVhCip_-R86kmfWrCPEUN_J-GGjytin-TNaRy0YihZBa06Gl4Qq9IL7mXF6oX-6lE93FKZ3jb6NJPYS4pvkzPeXhPGiETmRDZHPhMPXd_KC8RS8sNJnwgvBFx2uxo0sKKh1SWbFu1nk_3wk4P7d-2pTw9xyXAO171oFUAEtclalUcUYqTwDjoX4c_yrMP2bVqZ35cftt_5EeDhlFx-1RJ7cHe77CLr-ZD3K7FbZORKBR_2JsLjzSSuxWf7QHbRIXahoGOtljVnX7ZRKKn_ZZewQg_koEiROo61SXj5y-k7jK5D3IVM9JuuUSIaKdY9cEIRyXtA3IvVl5X8CKOM6txg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رکوردجهان توسط یک مرد اهل جزیره کوچک کم جمعیت‌در دریای‌کارائیب‌شکسته شد؛ الوی روم دروازه بان 37 ساله کوراسائو در بازی دیشب مقابل اکوادور موفق‌به‌ثبت 15 سیو شد و رکورد بیشترین سیو در 90 دقیقه‌یک بازی جام جهانی رو شکست!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/24000" target="_blank">📅 18:44 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23999">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe31d4a415.mp4?token=tybP7_9hI0SwxKerAKNfKvtNslOYEsak6K3B6wMi1Qp24chrHGlpCaPOfHpOLk84ArYEO95t8O3kiBhJpATJoega2a26vbCWKYKj5o0coRoXAQx1cPzHX8UBCQh0wFsVtOIUplbErms72UHBhsyasb4DtiaXKFfZpYsn5-cJnNr5YMMZBstMJctwNtlILOzzgSGF0R0BUoDt2n0NMrv_EET-f3JClD0bU5gwfKgQYnVlkGtWAyjzVM-kuyoZeQiWDe_-2Z46gtl0WzNdJf4MsyTvR7H-Id1ZEPd4_OCebJSLUh_hB1KaCq6h2LUPeD9-c4HV3k7pz7pUFMKAXQnwDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe31d4a415.mp4?token=tybP7_9hI0SwxKerAKNfKvtNslOYEsak6K3B6wMi1Qp24chrHGlpCaPOfHpOLk84ArYEO95t8O3kiBhJpATJoega2a26vbCWKYKj5o0coRoXAQx1cPzHX8UBCQh0wFsVtOIUplbErms72UHBhsyasb4DtiaXKFfZpYsn5-cJnNr5YMMZBstMJctwNtlILOzzgSGF0R0BUoDt2n0NMrv_EET-f3JClD0bU5gwfKgQYnVlkGtWAyjzVM-kuyoZeQiWDe_-2Z46gtl0WzNdJf4MsyTvR7H-Id1ZEPd4_OCebJSLUh_hB1KaCq6h2LUPeD9-c4HV3k7pz7pUFMKAXQnwDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بعدِضربه‌موزی‌شکل؛ و حالا ضربه پنبه‌ای
😕
😂
رونمایی سرهنگ علیفر از دیگر نوع ضربه در فوتبال
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/23999" target="_blank">📅 18:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23998">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RMx5JkCbZkDbclGUWkrVwrMqrisPdP24dclO99nLoXjvQTzMLFvmcnPffrJioNZOenNmWl262tpw9x61iPtN26fH_LkBTFtNhCT7vJHpcbbXSbanXZuC2z30VDo1e16YwfQ-WkjBJnNkYsazMbKMDzElgGj9DZnMtPT9b-a_PLl6OkuzdRdLw47mWMjbJWe_G4U1FZ1HZNsxdHCBXJfxBJD_ZTp7KrMZjLHiHJ884zzpj5Qb_9jSTZJiiznr_26x8kDj4fk-0dhovkQgHVxUGggTkrYr1bawBk5hPokwF_93En9OFQPSxwVD2fXT_CRoNh1JgDk9o92rgDhZNtTfWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
#تکمیلی؛ باتوجه‌به‌تعدادسوالات زیادی که درباره آخرین وضعیت نیمکت‌پرسپولیس پرسیدین لازمه در این باره به یه جمع بندی برسیم؛ امروز پرسپولیس با اسکوچیچ مذاکرات نهایی روانجام‌میده اگه به توافق کامل‌برسند بر سرجزئیات قرارداد امضا میشه اگه به توافق نرسند اوسمار…</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/23998" target="_blank">📅 18:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23997">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CCdM35Fqyud_GYj_0PklBRFBCCWASt0N1JldO3MY74qIHIj2lHGATuvjYHZUA06cgHqgTy-2_hTKVj6B1NVf2P3IXDdDhXmL5NXVEmAET-qzsNKVnlSEp5tEVyd1wmvyNyF1Yoh4_jtwrhajGEGHizDLbMuJbb0EGGKunBoKYmSGYk5DLdb2_ub4bGcDkSN4ykhyXJNAoQFiUwwiYcl9xHLKlkxA8Phn4Jw3BUk-6tlaZhMMzRBcVxcnDa7aHzSj4AdEfakfkpLB9miKXEsSzaHdleO00eYJWptVQj6vg8Tuwrq90w-mQ1_PHUQ4RbKcIQaTDUylO9kCiBiYwiAzcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
هفته‌دوم‌جام‌جهانی2026
؛ شماتیک ترکیب تیم ملی اسپانیا برای دیدار با عربستان؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/23997" target="_blank">📅 17:55 · 31 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
