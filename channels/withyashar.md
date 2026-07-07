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
<img src="https://cdn4.telesco.pe/file/osdWt1GLC7NyW_x5VFgBwooyo6rUnF4bJBGE1lSt8yaqkk6BKtJolol1lI9i1kG7WeTmX8XWljmYa-KpL3jSyaNLhhuh5CmDIFMJwOHf-gD_A2r0ZprT7MEiRCGtX6KVubnCivqRF4xpLOI0nFBtVVu5F7_1NYAf36t1E14Xed-7-uyyTD9CLVtFjwHYMnOMgU3vqi3nPutrGcxPpcoKAffnIzn2Lu93C_kyJiu6ro5bNQm6J0n1rCF9guBQOQrHYE1XHxWJI4UdMCnm2jLnP8-X2b_vEORvuaVG06XtwoOPWdYW10UAXRf923PCYBK6M-EftC36TwPbqKerLh7Rjw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 339K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-17 01:19:51</div>
<hr>

<div class="tg-post" id="msg-16727">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/withyashar/16727" target="_blank">📅 01:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16726">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">وال استریت ژورنال: کشتی های جنگی آمریکا در حالت آماده باش برای احتمال شروع احتمالی محاصره دریایی با دستور ترامپ  تا ساعات آینده هستند
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/withyashar/16726" target="_blank">📅 01:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16725">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">رسانه های داخلی میگن سپاه قصد داره همین امشب پاسخ بده
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/withyashar/16725" target="_blank">📅 01:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16724">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v0RVVyKIVEmzZW_EPOxhJ0mLTI1ogycz-Q6ntWZzljqOs9Eqo6fguPDz0QOa9t895SZVt5ISK85f7lytpvEf8VhhNiyNrgT6_no7HBkTqqPn59ybypOIA-wuGLmIJYiBTCCmjCd_99THUiTHngZxajHmciaouZaX9BCcsujoMIKtCSaFFbsHCBV2718gH0RhqwJ5nDwfVoD0fS75DNGAtIYooE9RLYAxF_RexddZbUruiuhOfpKPgUKHjzAvXuyM-zElQLBsLR8dRVVhJ0elA1mShgI0Y5Avwinj5XtAQaOgd-IheQPDd_j6pGrFPoI2uu2FGExzEtNkR_MlI45u4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لحظه انفجار سیریک
😳
@withyashar</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/withyashar/16724" target="_blank">📅 01:09 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16723">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">😞</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/withyashar/16723" target="_blank">📅 01:08 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16722">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">گزارش ها از حملات هوایی به قایق های تندرو نیروی دریایی سپاه در اسکله بندر سیریک.
@withyashar</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/withyashar/16722" target="_blank">📅 01:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16721">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HiIDVtQdNTKnxfzESNc_ApQAZSXsSYlEk1Q-PB-6-2miuSfuMdo6ycMnaLfQM2gOhYgGSshU-oJGC5ClczLeQjjuJPXwb2UwaYbBeaMfhLaWu9iNfERVhnAKxRDR4dv1H33RCv3if9MpQ1t8fpZodNcKHPvaTmKvnM1HiqzdBO0fI8TAsiTiyWqwTecacM4cgZ2UUiJM89FZAUvEjzdUlUVTlY2Snf_T-iwrG9rz0CAgNbScopMlnkUuTaY2yQvOwrtt7CfVkR2hVonfwkm1zy8qYGtAEML60oifSzFFJOEYGprYsPEyPZQHCDvNFrdI6zV32XS_eVOdV5gxUoGC1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجار مهیب در
اسکله سپاه
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/withyashar/16721" target="_blank">📅 01:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16720">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">شنیده شدن صدای ۲ انفجار دیگر در بندرعباس
@withyashar</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/withyashar/16720" target="_blank">📅 01:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16719">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZHo2GCDW58CLWN0bcRhaxuvutx0eSqoLsEkSmBtrDdC42CTfQrbvcnMZkGT0_meGqf5K-Fz1OO5TKPV4qytNrzICgVhF8Llm4xMku6E3ejN94FeZeeYk05F9PfB4HL5TylihuOvbw1V8lkgaaM74aawGctR9n6vHz8nkOSUcdk5oPZ-LRGYH8aid2vZWEZaJn-GEEjtdI_Dwf3R4U3fuuh8Rqq5bhXbDw-rzpq6043CNvjqZAWz-9SjYRoDNkFK_zgh1t_dx_gXwcwnQnM2heK8LvSWeMsLWM-e7n4RJQ4-yYyVspkUlFrAVt5tTeD__qb72ocjkoMwUbDCfnb3mKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بندرعباس هم اکنون
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/withyashar/16719" target="_blank">📅 01:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16718">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b07c5ad9e.mp4?token=IebQeDvIFDVTexYiDi_eQ0hArQFeeXi4p23vWM7tVYVLsZjafD6ZOD51z_IE1ppDYeyZIPrNzGoE0RJUAImi1cwEQ9e_WHyQgF0dsv0dox-r539KUY0Gj2WglIm4scL7ri0ClbVe4O6U0RkmwXfzmZhkgISJ9AzgItpSW3UzHaOg4rfKNu067mUHkWTY8r5U8vj16khAEQyUMSDUE5CHo8-7OMTVHhHk9_Rj-OWD-qs5lLXg1DZmyWhpa2AgbRmLW9gq3VB1t9qm4CS7QS45v8GH_dXJolJaiSW-trYX-ldX41wB4eOnrpFnqwtsq7eN5mhv_SwK2nY8pgjdWYBTSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b07c5ad9e.mp4?token=IebQeDvIFDVTexYiDi_eQ0hArQFeeXi4p23vWM7tVYVLsZjafD6ZOD51z_IE1ppDYeyZIPrNzGoE0RJUAImi1cwEQ9e_WHyQgF0dsv0dox-r539KUY0Gj2WglIm4scL7ri0ClbVe4O6U0RkmwXfzmZhkgISJ9AzgItpSW3UzHaOg4rfKNu067mUHkWTY8r5U8vj16khAEQyUMSDUE5CHo8-7OMTVHhHk9_Rj-OWD-qs5lLXg1DZmyWhpa2AgbRmLW9gq3VB1t9qm4CS7QS45v8GH_dXJolJaiSW-trYX-ldX41wB4eOnrpFnqwtsq7eN5mhv_SwK2nY8pgjdWYBTSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روشن شدن آسمان به علت انفجارها در پایگاه هوایی بندرعباس.
@withyashar</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/withyashar/16718" target="_blank">📅 01:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16717">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">پرواز جنگنده های شیفت آلرت نیروی هوایی ارتش از اصفهان به سمت جنوب
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/withyashar/16717" target="_blank">📅 01:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16716">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/idLGvhhMl6VPTJng1M_iCnO2RbpbhYbdWbv5mVGhkhXzy44iDOW06IbE8zQ2lWkmRFeu93U7Cm9IbyBFL1Go4SNsSlO5DTU1dL0IP_EkxbXhO7iUPoP9AWXVDlMKRytQCFa5-uspjJjul_3tUP1Wywtr9QGIytQEByvc_bS1y7QL1uCMwkETna12IYeMYYOaDdW-7bmsTdOrtgBff5cyxgqqxMECJCgx2SIsjfqR_1DzlEd8h7L7YdV_bNeW8f3SJyI2dVP_i5uZ5Vma48E6_djAiTW63zwbIFlmk06rT09y1C1USOKTZFb6NztIDJ02uNuI51JbFdr1aDs7_Zpmkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون اسکله سیریک
@withyashar</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/withyashar/16716" target="_blank">📅 00:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16715">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">فرودگاه بندرعباس که روز گذشته پس از چند ماه شروع به کار کرد، دقایقی پیش مورد حمله قرار گرفت
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/withyashar/16715" target="_blank">📅 00:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16714">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">انفجارهای جدیدی در نزدیکی جزیره قشم گزارش شده
@withyashar</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/withyashar/16714" target="_blank">📅 00:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16713">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">انفجارهای بندر عباس به قدری شدید است که پیامهای بسیار زیادی از شهرهای اطراف دریافت میکنم که این موضوع را تأکید‌ و تایید میکنند.
@withyashar</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/withyashar/16713" target="_blank">📅 00:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16712">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">همین الان بندرعباس رو 6 تا صدای انفجار بلند فجیح اومد
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/withyashar/16712" target="_blank">📅 00:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16711">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">یاشار بندرعباس 11 انفجار رادار های دریایی اسکله رجاییی
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
@withyashar
🚨</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/withyashar/16711" target="_blank">📅 00:50 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16710">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">سنتکام:نیروهای فرماندهی مرکزی ایالات متحده، سلسله حملات قدرتمندی را علیه ایران آغاز کرده‌اند تا هزینه‌های سنگینی را برای هدف قرار دادن و حمله به کشتی‌های تجاری که توسط افراد غیرنظامی بی‌گناه در یک آبراه بین‌المللی اداره می‌شوند، تحمیل کنن
این حملات آمریکا در پاسخ به حملات ایران به سه کشتی تجاری است که در تنگه هرمز در حال عبور بودند. این اقدامات تهاجمی ایران غیرضروری، خطرناک و نقض آشکار آتش‌بس بود
@withyashar</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/withyashar/16710" target="_blank">📅 00:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16709">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/withyashar/16709" target="_blank">📅 00:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16708">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">سامانه های پدافندی در بندرعباس فعال شدند.
@withyashar</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/withyashar/16708" target="_blank">📅 00:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16707">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">دکل زبون وا کرد
😩
@withyashar</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/withyashar/16707" target="_blank">📅 00:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16706">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">خبرگزاری اینتل : هشت بمب به یک پایگاه دریایی متعلق به سپاه پاسداران انقلاب اسلامی در سیریک اصابت کرد
@withyashar</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/withyashar/16706" target="_blank">📅 00:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16705">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">هم زمان حملات هوایی اسرائیل به جنوب لبنان
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/withyashar/16705" target="_blank">📅 00:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16704">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">صدا و سیما: برخی منابع خبری از شنیده شدن صدای چند انفجار طی دقایق اخیر از محدوده قشم و بندرعباس خبر می دهند.
@withyashar</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/withyashar/16704" target="_blank">📅 00:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16703">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">انفجار در جزیره‌ی هنگام
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/withyashar/16703" target="_blank">📅 00:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16702">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">بندر عباسسسسسس بدد زدن
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/withyashar/16702" target="_blank">📅 00:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16701">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">مهر: صدای انفجار در قشم و بندرعباس هم شنیده شد
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/withyashar/16701" target="_blank">📅 00:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16700">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">سیریک زارتان زورتان شدیدددد
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/withyashar/16700" target="_blank">📅 00:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16699">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">گزارش ۶-۸ انفجاااارررررر
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/withyashar/16699" target="_blank">📅 00:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16698">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">تتر پروازززز  داره میکنه  ۱۷۸۰۰۰
1$ Tether = 178,000
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/withyashar/16698" target="_blank">📅 00:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16697">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">گزارش های بسیارررر از صدای انفجار در قشم و سیریک
🚨
🚨
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/withyashar/16697" target="_blank">📅 00:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16696">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">شروع شددددد
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/withyashar/16696" target="_blank">📅 00:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16695">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">باراک راوید خبرنگار آکسیوس : امشب بیدار بمانید
@withyashar
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/withyashar/16695" target="_blank">📅 00:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16694">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/494c1afd8f.mp4?token=pI4Qm0-0-cR8qOCQ5qbU_9GuVJJEJcWu2iFRy72Vx8z3gFKfzjLl7fUqKEUd3-fucE2-KdJ_STscyrsP4LhlTeb0puC3WLWCr5EZbRYQawxtXiMo4rIFacOdIU9PvEkD-xYvn75ql7vUD8zHE2ojgcNUB9e2qLuKOGNxFV0w80yoieHh9Has690gMYYmLxXj1_2euIU4vSUpaUwdKHwWtPRnUxlYDRgPUkUY1xPSoyiiHsRe6OSQl8ZgRtb1JEn8ln3hWqG6F3caJOoYpp8lV-4246PFnUDEsNpy3CvWLUgxTnYhK2_fz963KJ88IJ6Pu_5G2F1rnYCwqv1VRLBhOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/494c1afd8f.mp4?token=pI4Qm0-0-cR8qOCQ5qbU_9GuVJJEJcWu2iFRy72Vx8z3gFKfzjLl7fUqKEUd3-fucE2-KdJ_STscyrsP4LhlTeb0puC3WLWCr5EZbRYQawxtXiMo4rIFacOdIU9PvEkD-xYvn75ql7vUD8zHE2ojgcNUB9e2qLuKOGNxFV0w80yoieHh9Has690gMYYmLxXj1_2euIU4vSUpaUwdKHwWtPRnUxlYDRgPUkUY1xPSoyiiHsRe6OSQl8ZgRtb1JEn8ln3hWqG6F3caJOoYpp8lV-4246PFnUDEsNpy3CvWLUgxTnYhK2_fz963KJ88IJ6Pu_5G2F1rnYCwqv1VRLBhOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک هواپیمای باری بوئینگ ۷۳۷-۴۰۰ متعلق به شرکت هواپیمایی کی ۲ ایرویز پس از پرواز از شارجه امارات متحده عربی در مسیر کراچی پاکستان مفقود شده است.  هواپیمای باری با شماره ثبت AP-BOI ظاهراً پس از یک سقوط بسیار سريع از صفحه رادار در دریای عمان ناپدید شده است.مقامات…</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/withyashar/16694" target="_blank">📅 00:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16693">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">به ادعای رسانه ها دولت مصر با یک تصمیم سیاسی، تمام برنامه‌های سالگرد درگذشت محمدرضا شاه پهلوی شاهنشاه فقید ایران را که همه ساله در مسجد الرفاعی برگزار می‌شد لغو کرده است. ‏همچنین گزارش شد که از سوی مقام‌های مصری به وزارت خارجه این کشور ابلاغ شده اجازه ورود…</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/withyashar/16693" target="_blank">📅 00:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16692">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">یک هواپیمای باری بوئینگ ۷۳۷-۴۰۰ متعلق به شرکت هواپیمایی کی ۲ ایرویز پس از پرواز از شارجه امارات متحده عربی در مسیر کراچی پاکستان مفقود شده است.
هواپیمای باری با شماره ثبت AP-BOI ظاهراً پس از یک سقوط بسیار سريع از صفحه رادار در دریای عمان ناپدید شده است.مقامات هنوز تأیید نکرده اند که چه چیزی باعث سقوط هواپیما شده است اما
برخی منابع تایید نشده میگویند پدافند آمریکا به اشتباه هواپیما را مورد هدف قرار داده است
@withyashar
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/withyashar/16692" target="_blank">📅 00:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16691">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">گزارشات از پرواز جنگنده‌های آمریکایی در مرز ایران
@withyashar
🚨
🚨
🚨
کانال اگه میوت هست دربیارید و نتفیکیشن های پین اینستاگرام رو کاملا روشن کنید</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/withyashar/16691" target="_blank">📅 00:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16690">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WCHOaivG352aoQJwV3O6ydmO7bdPePW6xQeHRFofyHEtdOl-Ci7J8K79Ou0zoHwJSPkEsJUdVn10QW112CxRx0q8PIjc5sz7-mdnHhwrZxV-0r69Do1WCjddLumhsVwN2tQp5kyyKqUwYU6fA9OZk5kqARKwaC3HwBbSg2gX_JjnBK2ROeeCHcGECM1uRMxuFOoy5hWlF0yMi95SOW8LPDMv7tX54xX1ZClXagNpusIrcrkctmBjSh1WGB-i1_GXpcKh7FiFJ5UCoSuANjWvX6ZGyXW7Rpqtn1T-QNCOmXiOTXIEFxPTn7SH2n7mvFxrdeNuC1llFI8Jf9XhOn5aIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از رسانه های رژیم در کانال تلگرامش اومده، آدرس محل اقامت ترامپ در آنکارا را اعلام کرده، که مثلا حمله بشه.
@withyashar
🤣</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/withyashar/16690" target="_blank">📅 23:59 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16689">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">گزارش ها از فعالیت گسترده ارتباطات رادیویی نظامی در سراسر خلیج فارس و تنگه هرمز.
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/withyashar/16689" target="_blank">📅 23:49 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16688">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">رضایی:  دوستانی که مخالف مذاکره هستند صبر کنند؛ خود آمریکایی‌ها این مذاکرات را ازبین می‌برند
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/withyashar/16688" target="_blank">📅 23:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16687">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">فرصت ۱۰ روزه آمریکا به مشتریان نفتی ایران
در مجوز جدید وزارت خزانه‌داری آمریکا به طرف‌ها اجازه داده ظرف حداکثر ۱۰ روز به تمامی‌معاملاتی که قبلا فروش تحویل و فروش نفت خام، محصولات پتروشیمی‌و فراورده‌های نفتی با منشا ایرانی را مجاز می‌کرد پایان دهند.
در مجوز جدید همچنین تأکید شده است که ایالات متحده آمریکا از امروز (۷ ژوئیه ۲۰۲۶) هیچ‌گونه معامله جدید از جمله خرید یا بارگیری نفت خام، محصولات پتروشیمی‌ یا فرآورده‌های نفتی با منشا ایرانی را مجاز نمی‌شمارد
@withyashar</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/withyashar/16687" target="_blank">📅 23:46 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16686">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">نیروی هوایی اسرائیل برای مشارکت برای حمله به ایران اعلام آمادگی کرد
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/withyashar/16686" target="_blank">📅 23:45 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16685">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e75ced6192.mp4?token=QYemZObaQLy-ySS67wP3LgDIE8I5O4WDTbxuwWi2U4aElTo3DIVq4U7jOLLkOxAHWP5ntOHyI7EioaoZ7iRMvxP3-WzMQw_2TNEqoo8FJ5CmxHx2BmBn1V_ERxsaxB57WKOtkhW0FugZntwssJQgzCKg57_ZC7ZYVj9oeC84M6uSZpJTxwhMW83WYheLYCFRk8An_WKI8pXyp9ZA9emLkHX7GIbzPOxMT-79ZGwQ3FJtKQpLVGsuZA0NjcgZbBD2g2OF32Te3IWqnAQ_iV1nKs-WnIXMnbDE6dpuKOtyMyqI2DdG8gsJ6rdmURF0qCiYSNYjyl6stI4BbuRHsvgxrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e75ced6192.mp4?token=QYemZObaQLy-ySS67wP3LgDIE8I5O4WDTbxuwWi2U4aElTo3DIVq4U7jOLLkOxAHWP5ntOHyI7EioaoZ7iRMvxP3-WzMQw_2TNEqoo8FJ5CmxHx2BmBn1V_ERxsaxB57WKOtkhW0FugZntwssJQgzCKg57_ZC7ZYVj9oeC84M6uSZpJTxwhMW83WYheLYCFRk8An_WKI8pXyp9ZA9emLkHX7GIbzPOxMT-79ZGwQ3FJtKQpLVGsuZA0NjcgZbBD2g2OF32Te3IWqnAQ_iV1nKs-WnIXMnbDE6dpuKOtyMyqI2DdG8gsJ6rdmURF0qCiYSNYjyl6stI4BbuRHsvgxrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رضایی: آمریکا به دنبال عبور دادن ناوهای خودش از تنگه هرمز است
آمریکا در عمل زیر تفاهم می‌زند.
@withyashar</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/withyashar/16685" target="_blank">📅 23:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16684">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">دستگاه های اخلال گر GPS در سراسر خلیج فارس و تنگه هرمز فعال شدند  حتی تا کیش‌ کاملا در سیگنال قرمز فرورفته
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/withyashar/16684" target="_blank">📅 23:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16683">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">خبرگزاری آکسیوس : آمریکا امشب در جواب نقض تفاهم نامه توسط ایران و حمله به کشتی های باری،حمله ی گسترده ای انجام میده.
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 73.1K · <a href="https://t.me/withyashar/16683" target="_blank">📅 23:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16682">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">بعد از ۳۷ سال و دو ماه از آخرین سفر خارجی علی خامنه‌ای که در تاریخ ۱۹ اردیبهشت ۱۳۶۸ (۹ مه ۱۹۸۹ میلادی) به کشور چین انجام شد، در زمانی که وی در دوران ریاست‌جمهوری خود بود… و همان طور که نشان دادم با پرواز بوینگ ۷۷۷ ماهان در همین لحظه لشش از ایران خارج شد و…</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/withyashar/16682" target="_blank">📅 22:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16681">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a4d715020.mp4?token=MzeBzCp9FoTNwq6TevzPRTH4_ghOWSWpC9iLWG7tHBpfkT0S4duF2otiXdYMKofVfUaU9Jh1RsBjGiiUweU7UsD45ZuZq89JeggjbSBln9Qv8NvtWw1NPEGmgvxVxSA3yQXmurnHasGbnqsjcQw-wJEeGd3G30K6ZxPhFWw6F0v-uitB4087orqsnWKn8mllph_RjqfvtLmXiGQiWnApIsaY_HmIFqAvJp1TIfK9G9lUjuGfMaIDEpsGQhm54AX27XRffAeRZZReXqp6vOZpcVgNbMqJNvtjLDj58YemzLP6GUd1QWzd2wCd8D2edXyJCjIJ8PwkQ0Y18aTtmKAwkwRRS3p-aFq383egHhEVgupQL7tPKurjikIUI29OdLU-RcW0EYmSkgvBM5bd9koIeiAu9LQ5Hdxj1v_NDwoHNSlbgvBnK8vts8mxU9G59sCAj5NUliKU2xMJfPXZ9vqNDVwTcsLeipgUifCLFUg-X4t_B4eRa08TUjDOQXyosk8ZKnBXd-gP1SGa9w--RhHWPmOYK-k73QInts1oHA_aWTdIirSLhEaRC4F3NjxhIn-SlWbCDH4jvaVudsLicsxnf6MZ06YYd3UfhigzLRjVkI7ud06X3eY9TzYtJJFht5EbgncMv0lArQ4_HlQG6icR85h56M3T7VId_iRSokmRwRE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a4d715020.mp4?token=MzeBzCp9FoTNwq6TevzPRTH4_ghOWSWpC9iLWG7tHBpfkT0S4duF2otiXdYMKofVfUaU9Jh1RsBjGiiUweU7UsD45ZuZq89JeggjbSBln9Qv8NvtWw1NPEGmgvxVxSA3yQXmurnHasGbnqsjcQw-wJEeGd3G30K6ZxPhFWw6F0v-uitB4087orqsnWKn8mllph_RjqfvtLmXiGQiWnApIsaY_HmIFqAvJp1TIfK9G9lUjuGfMaIDEpsGQhm54AX27XRffAeRZZReXqp6vOZpcVgNbMqJNvtjLDj58YemzLP6GUd1QWzd2wCd8D2edXyJCjIJ8PwkQ0Y18aTtmKAwkwRRS3p-aFq383egHhEVgupQL7tPKurjikIUI29OdLU-RcW0EYmSkgvBM5bd9koIeiAu9LQ5Hdxj1v_NDwoHNSlbgvBnK8vts8mxU9G59sCAj5NUliKU2xMJfPXZ9vqNDVwTcsLeipgUifCLFUg-X4t_B4eRa08TUjDOQXyosk8ZKnBXd-gP1SGa9w--RhHWPmOYK-k73QInts1oHA_aWTdIirSLhEaRC4F3NjxhIn-SlWbCDH4jvaVudsLicsxnf6MZ06YYd3UfhigzLRjVkI7ud06X3eY9TzYtJJFht5EbgncMv0lArQ4_HlQG6icR85h56M3T7VId_iRSokmRwRE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعد از ۳۷ سال و دو ماه از آخرین سفر خارجی علی خامنه‌ای که در تاریخ ۱۹ اردیبهشت ۱۳۶۸ (۹ مه ۱۹۸۹ میلادی) به کشور چین انجام شد، در زمانی که وی در دوران ریاست‌جمهوری خود بود… و همان طور که نشان دادم با پرواز بوینگ ۷۷۷ ماهان در همین لحظه لشش از ایران خارج شد و به نجف رسید
@withyashar</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/withyashar/16681" target="_blank">📅 22:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16680">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">خبرگزاری وای نت وابسته به ناتنیاهو از قول
یک مقام رسمی آمریکایی: آمریکا مجوز فروش نفت ایران را لغو کرد.
@withyashar</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/withyashar/16680" target="_blank">📅 22:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16679">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/withyashar/16679" target="_blank">📅 22:28 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16678">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">رسانه های عبری : به تازگی، شناورهای نیروی دریایی ترکیه به تمرینات نیروی دریایی اسرائیل در دریای مدیترانه نزدیک شده بودند، مانع از پیشرفت آن شدند و به گزارش‌ها، تلاش کردند نیروها را به سمت درگیری سوق دهند.
بر اساس گزارش "اسرائیل الیوم"، با دستور فرماندهی، شناورهای اسرائیلی مسیر خود را تغییر دادند و از رویارویی مستقیم با نیروی دریایی ترکیه اجتناب کردند.
@withyashar</div>
<div class="tg-footer">👁️ 73.1K · <a href="https://t.me/withyashar/16678" target="_blank">📅 22:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16677">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/022cfc7780.mp4?token=Ndn1rWW46GVeSSOR5d1340Y41QIwWqSWpMjw2I_BW_jovkqp_wokNXayHNCMwXS-5izeSelIBGfPbhh6T-iLep0YmitBnr7razqKvbrnk-e_WiGPQMEf5aREFqNuLUPjtACJjflglzwzHONoWt6q8fCLA7DlCqiC5aW711hDjhUoXhxcqYputeHKtHxi9W3efi5G76BAHZTXNCosIym_tO87Atjnk3A7XdTScawg5qqDyKQbFwUyuWVvR3Iej9JbTCn5DbjRNuccfdZUTFU9Gw3e5gEdp1ayPHBpKdCxDltNe-y87uDybrvaTDHP9INYcJt4w0bkqu70pFbWdeAqPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/022cfc7780.mp4?token=Ndn1rWW46GVeSSOR5d1340Y41QIwWqSWpMjw2I_BW_jovkqp_wokNXayHNCMwXS-5izeSelIBGfPbhh6T-iLep0YmitBnr7razqKvbrnk-e_WiGPQMEf5aREFqNuLUPjtACJjflglzwzHONoWt6q8fCLA7DlCqiC5aW711hDjhUoXhxcqYputeHKtHxi9W3efi5G76BAHZTXNCosIym_tO87Atjnk3A7XdTScawg5qqDyKQbFwUyuWVvR3Iej9JbTCn5DbjRNuccfdZUTFU9Gw3e5gEdp1ayPHBpKdCxDltNe-y87uDybrvaTDHP9INYcJt4w0bkqu70pFbWdeAqPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اولین
تصویر از خودروی
ن
ع
ش
کش که فردا قرار است در عراق تابوت خامنه ای را حمل کند
@withyashar</div>
<div class="tg-footer">👁️ 74.1K · <a href="https://t.me/withyashar/16677" target="_blank">📅 22:11 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16676">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">طبق گزارش ها یک نفتکش بزرگ دیگر  نیز مورد اصابت موشک در تنگه هرمز قرار گرفته است.
@withyashar</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/withyashar/16676" target="_blank">📅 22:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16675">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">قطر معاون سفیر ایران را احضار کرد
دولت قطر در پی حمله به یک نفتکش قطری در تنگه هرمز، معاون سفیر ایران در دوحه را احضار کرد.
بر اساس این گزارش، قطر از تهران خواسته است فوراً به تمامی اقداماتی که امنیت منطقه و آزادی کشتیرانی را تهدید می‌کند، پایان دهد.
@withyashar</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/withyashar/16675" target="_blank">📅 22:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16674">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/withyashar/16674" target="_blank">📅 22:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16673">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">داریم به این لحظه نزدیک میشیم. گفتم از الان داشته باشین، سیو کنین، چون اون موقع ممکنه اینترنتتون قطع باشه و نفهمین چی شده.
@withyashar</div>
<div class="tg-footer">👁️ 76.2K · <a href="https://t.me/withyashar/16673" target="_blank">📅 21:54 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16672">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">آرژانتین ۳-۲ زد جلو</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/withyashar/16672" target="_blank">📅 21:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16671">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">کامبک سنگین آرژانتیتثن ۲-۲</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/withyashar/16671" target="_blank">📅 21:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16670">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">مصر دوباره گل زد ( این دیگه درسته ) ۲ بر هیچ</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/withyashar/16670" target="_blank">📅 21:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16669">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">یک مسئول ترکیه‌ای به شبکه الجزیره گفت: رئیس‌جمهور ترکیه، اردوغان و ترامپ، مسائل مربوط به إيران را مورد بحث قرار دادند و بر لزوم یافتن یک راه حل قابل قبول برای جنگ و باز شدن تنگه هرمز تاکید کردند.
@withyashar</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/withyashar/16669" target="_blank">📅 21:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16668">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">مصر‌ ۱ هیچ جلو هست مسی هم همین الان پنالتی رو خراب کرد ! شخمی‌ترین جام جهانی تاریخه !</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/withyashar/16668" target="_blank">📅 21:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16667">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">مصر گل دوم رو هم زد</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/withyashar/16667" target="_blank">📅 20:56 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16666">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">مصر‌ ۱ هیچ جلو هست مسی هم همین الان پنالتی رو خراب کرد ! شخمی‌ترین جام جهانی تاریخه !</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/withyashar/16666" target="_blank">📅 20:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16665">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">نتانیاهو درباره ایران: توافقی بشه چه نشه  من هیچ‌وقت اجازه نمی‌دم ایران به سلاح هسته‌ای برسه، این دقیقاً همون موضع ترامپه
نتانیاهو : اردوغان فقط مشکلش با اسرائیل نیست , حتی یونان (که عضو ناتوه) رو هم تهدید کرده به نابودی
@withyashar</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/withyashar/16665" target="_blank">📅 20:49 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16664">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">نتانیاهو به سی‌ان‌ان: به رئیس جمهور ترامپ توضیح دادم که فروش جنگنده‌های اف ۳۵ به ترکیه توازن قوا در خاورمیانه را برهم می‌زند.
ترکیه جاه‌طلبی‌های متجاوزانه‌ای دارد و نیرویی حامی صلح و ثبات نیست.
اگر ترکیه هواپیماهای اف ۳۵ را دریافت کند، اقدامات متخاصمانه‌ای صورت خواهد گرفت
نتانیاهو : هنوز خیلی زود است در مورد آینده ایران صحبت کنم.
@withyashar</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/withyashar/16664" target="_blank">📅 20:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16663">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bv81Dnl8cWvqGZzZPGBS60zl2HNX2Z3dQh8HToE5LikyYaAebAlXI5eqhyRu_xFrFA2eWlhWXBxdacHpdpA5wA69lBitf-As_lqjT_VF1iKf-RrS0KFQd9qs18Q8dz9AldFYIB2DHyh0EgtXJlmWAph9kBKc1nLnqMevF26WV3_p7u9xQjNDvAOLJL7SYJQQiwn8LdkzXbUWre-jyiGcdRCih2wQ5AQ7i3DNNboK8tW3gwx2oWfwN2cSp5kGc2fXIotrc6QFOydm_IGpK1KjgseY9MLPWRql5PZVtwq93unCMkyS_ySohanCq69zmpNkDAgamNPY9_xAteP0sd0BKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : هواپیمای بوینگ ۷۷۷ ماهان حامل جنازه خامنه ای تا دقایقی دیگر وارد نجف می‌شود
@withyashar</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/withyashar/16663" target="_blank">📅 20:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16662">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hcip43WDUljTPrqaIlt1t8cC5dz9xiMJR-UOJKb2ZSpy4_sq87_FyQZYA_AH4I_xoCsgz3bbAN96Olf-JHmphS1lbZ1ArbUKg4itOQfyfzL_gzqxXJ4YchB7psXjpaMl0e1xawAbgT8_GoGTaWG_3oQrMPklbZo0mN67d559E2IuQjDdSD3XCSZeLNqy4W8oCS5Tfnx-dg5xfvb-xPGa0LZByCPLOZZajXV_NGG0kPvdIPYi_R64ya-_nwwzbcuUi5FrbIWDY2EH_E1SxEHYzI0ATDQW1dcAo4dDbblg4HdOOIzdBJNYCrS6mYxeu0CsqxvaYQR6HlgjmedmSP5tAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه گروه تندرو ناشناس برگه‌ای روی ماشین و خانه قائم پناه، معاون پزشکیان چسبوندن و به حذف فیزیکی تهدید کردن
@withyashar</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/withyashar/16662" target="_blank">📅 20:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16661">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">مصر‌ ۱ هیچ جلو هست مسی هم همین الان پنالتی رو خراب کرد ! شخمی‌ترین جام جهانی تاریخه !</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/withyashar/16661" target="_blank">📅 19:56 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16660">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">بلومبرگ:ایران به سازمان بین‌المللی دریانوردی اطلاع داده است که بر تنگه هرمز تسلط دارد.
@withyashar</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/withyashar/16660" target="_blank">📅 19:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16659">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">مقام ارشد آمریکایی:ایران با شلیک موشک ها به سمت تنگه هرمز،یادداشت تفاهم نامه با آمریکا را نقض کرده است. @withyashar</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/withyashar/16659" target="_blank">📅 19:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16658">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">مقام ارشد آمریکایی:ایران با شلیک موشک ها به سمت تنگه هرمز،یادداشت تفاهم نامه با آمریکا را نقض کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/withyashar/16658" target="_blank">📅 19:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16657">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16ecd9127e.mp4?token=LU_ZUJJU-29oDej8uoegnaC_Yrn07PgHm3NQJub9qOzEMqhqu9_so6tO43qVBxx4czxTgDK97jCu_aGpOVDtAOjDWNSkJKXZLhKRKhmnvN10uJvXbQLKKyViL3gsFgQAu9-fYli8XippnLOvX_MT0s_himJGqfsM8cu0j50vbmesEsNym370AGr9_PpLHruGTCDNU4nbjjf957HcNrMfyi3EkKb6PoZEgtGfn4jkr-F5o0lmH-n1hp4jNQd4V5rZNh3ra-lIXQ9g6kvHObKwXSDIb7namalfYbzqAex-jeNKlLKEbfrUnmIXUL0H4zThijYFs4Zu1rgzLLnvaI2nzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16ecd9127e.mp4?token=LU_ZUJJU-29oDej8uoegnaC_Yrn07PgHm3NQJub9qOzEMqhqu9_so6tO43qVBxx4czxTgDK97jCu_aGpOVDtAOjDWNSkJKXZLhKRKhmnvN10uJvXbQLKKyViL3gsFgQAu9-fYli8XippnLOvX_MT0s_himJGqfsM8cu0j50vbmesEsNym370AGr9_PpLHruGTCDNU4nbjjf957HcNrMfyi3EkKb6PoZEgtGfn4jkr-F5o0lmH-n1hp4jNQd4V5rZNh3ra-lIXQ9g6kvHObKwXSDIb7namalfYbzqAex-jeNKlLKEbfrUnmIXUL0H4zThijYFs4Zu1rgzLLnvaI2nzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دکل زبون وا کرد
😩
@withyashar</div>
<div class="tg-footer">👁️ 74.9K · <a href="https://t.me/withyashar/16657" target="_blank">📅 19:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16655">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b528ebf23a.mp4?token=ksnFPAuyXHnoRgyk0mjU3FKqG8WSbB8Oi4LwkG_Hzceq5pBo373NupCL_YTTZH2Jwt_qb0N2tDpGdsfmYfFmYWPY4gPvM0xFNiPcUZ6uORwBPYLtX2GTTr1X4Utveh48qIzzhpVIhptEKz-dOrVtvNsFpWk0rnaxf974KCAick07RfKWpzCbfmXUCCRrBZFGmCe1Mn0oh584jSQ9pjA2Q5EAJAdvnZxbsl-1Vu0XKgPUf3lX_lp5WQrZKdbHuxZtYV_xAYTvSnWR7frN5I_W3vYh_ntBOWUr3Wn41K2pgXMAFOLJUat_tfEgpwkD49FnWgSHm-4CX9Xg-BhL7EO3Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b528ebf23a.mp4?token=ksnFPAuyXHnoRgyk0mjU3FKqG8WSbB8Oi4LwkG_Hzceq5pBo373NupCL_YTTZH2Jwt_qb0N2tDpGdsfmYfFmYWPY4gPvM0xFNiPcUZ6uORwBPYLtX2GTTr1X4Utveh48qIzzhpVIhptEKz-dOrVtvNsFpWk0rnaxf974KCAick07RfKWpzCbfmXUCCRrBZFGmCe1Mn0oh584jSQ9pjA2Q5EAJAdvnZxbsl-1Vu0XKgPUf3lX_lp5WQrZKdbHuxZtYV_xAYTvSnWR7frN5I_W3vYh_ntBOWUr3Wn41K2pgXMAFOLJUat_tfEgpwkD49FnWgSHm-4CX9Xg-BhL7EO3Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جایزه موش طلایی سیرک هم به این تاپاله میرسه
@withyashar</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/withyashar/16655" target="_blank">📅 19:09 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16654">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">شبکه ان‌بی‌سی به نقل از یک مسئول آمریکایی: ایران شب گذشته دو کشتی را با دو موشک که مسافتی کوتاه را با سرعت بالا طی کردند، مورد حمله قرار داد.
@withyashar
اتاق جنگ با یاشار : دو تا هم  الان زد ، پس امشب دکل سیریک و برای بار ۴۸ ام میزنند
🤒
🚨
@withyashar</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/withyashar/16654" target="_blank">📅 19:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16653">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cl-2ZtBDHaVPPZJDMrB-F9rINXPNFY0EgQ3X_3VIC3aln78inpYtCB-_5iJcMOuYRThfwFWM8-lfu1qMyIuoZM78tSKnWTuNFRLa6GksLbuaMKOgHVQ8hPErhaxXxV4sL7X04D0NHlAmQXG5x-gUmR30O01nXWhlS69Njxp-A7sfrAu8CLnTb5DoBSkrsxMrOswm3oU_uFl0xO3Ky6NbaIs4QxiHkOhQdBy8cGv8z-YeWauor067IBsAyHDcrHhrUDIapXGmBxod-3KZBY-ASkO5ESsZwUGa7Vs6zX_Tn0hFEb80Bq9L9sKHvvVHWQlbDkVGQraOO2qdgpRhZzQ9_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اینم یکی از کشتیایی که دیشب بهش حمله شده، به وضوح نشتی سوختش مشخصه، قبلا خیلی گفتم ۳پا میخواد بخش جنوبی هرمز(مسیر عمان) رو باطل کنه و به طبع تمام ترافیک رو بکشه بخش شمالی برای ایران، اینجوری نبض هرمز هم دستشه
@withyashar</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/withyashar/16653" target="_blank">📅 18:56 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16652">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sk2Gu3R9KGfh8rO9qFTBYQHLoPDfi-qFoV8OMu5GugNEjyZsGOENb9I2KZh5kBLA6SoWvgxEP5okXzQuQ2vo3-Xor0-EKhlfXNiBHE3PEYZPgcZ2LbadQPdDfE32em-oPjzUCcDkISMW5CRbVxJ416-eGJvVg2c4haI4To9doUYjjEaHxefINHR1gzDWVxniuRwL6Qw7bPytjkCfUqnjnWSiZ8vieD2Tg0KOQ8ip4d-hAyVgV6GgvslWkIPXHj81Kd2R6e5kntYsNYoFfrB2TszZhxmWIXCdjzG2xEFNleghJ4sPt25ibDcA3DPCAny8rM9kbv9Y0LilRgS5rzkmpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک حمله دیگر به یک نفتکش در تنگه
سازمان عملیات تجارت دریایی بریتانیا (UKMTO) از اصابت یک پهپاد ناشناس به یک نفتکش خبر داد.
این نفتکش هدف حمله یک پهپاد با هویت نامشخص قرار گرفته که منجر به ایجاد خسارات  در بدنه کشتی شده است.
@withyashar</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/withyashar/16652" target="_blank">📅 17:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16651">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">یک مقام ناتو به الجزیره گفت: رهبران این ائتلاف، در نشست خود که فردا چهارشنبه برگزار می‌شود، به موضوع تنگه هرمز و آزادی کشتیرانی خواهند پرداخت.
@withyashar</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/withyashar/16651" target="_blank">📅 17:36 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16650">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">گروه فرانسوی "مهاجرین" که از جولانی حمایت می‌کند، مسئولیت انفجارات در نزدیکی کاروان مکرون در دمشق را بر عهده گرفت
@withyashar</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/withyashar/16650" target="_blank">📅 17:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16649">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">درگیری مرزی طالبان و ارتش پاکستان
منابع محلی در ولایت ننگرهار اعلام کردند میان نیروهای طالبان و ارتش پاکستان در نقاط مرزی شهرستان دوربابا تبادل آتش صورت گرفته است.
@withyashar</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/withyashar/16649" target="_blank">📅 17:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16648">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FqqvLLdlNLXU0r-rhyruydF3Ri8e39Q7k6rp9JRbHWoxmJTfhkB8Lq-QcKKfQJMBAk_X2JKtXddUXzrwQBfa5F6CKxX8_bG81ZO94QkarLu4CLF52x84_SXjXTiYURKIhohqK-o6EaKQCSlbFPGewsvK49TP5TvL75iDPGTC7qfZrs1w-o1jzSHFI5Q1DaqLMw8WdCUcoBsF-frH9caVNJgeDze5niSUDbhw9zcIvzi-Q2yWCGSb2V4m9g9iBnLnssN4w_nKvpxMjDtONjgQXZPQCnPS0Hj6rLJPMfaNMp4Jio_mvnnq69qs6K6OnLi6rgYQ7vKEXMrMf7TmHMtTQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرکز عملیات دریایی تجارت بریتانیا (UKMTO) گزارشی مبنی بر وقوع حادثه‌ای مربوط به یک نفت‌کش در حال عبور از تنگه هرمز دریافت کرده است.
این نفت‌کش مورد اصابت یک پرتابه ناشناس قرار گرفته و به نظر می‌رسد آسیب‌های ساختاری به آن وارد شده باشد.
@withyashar</div>
<div class="tg-footer">👁️ 72.7K · <a href="https://t.me/withyashar/16648" target="_blank">📅 17:16 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16647">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">هم اکنون از سیریک صدای دعوا در تنگه شنیده شد @withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/withyashar/16647" target="_blank">📅 17:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16646">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">دبیرکل ناتو: بدون اروپا، آمریکا نمی‌توانست به ایران حمله کند
رومانی بزرگترین فرودگاه‌های تجاری خود را بست تا به هواپیما‌های آمریکایی اجازه برخاست و فرود دهد
@withyashar</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/withyashar/16646" target="_blank">📅 16:59 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16645">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ترامپ: ترکیه به خاطر من درگیر جنگ با ایران نشد و نمی‌خواهد شاهد دستیابی ایران به سلاح هسته‌ای باشد
@withyashar</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/withyashar/16645" target="_blank">📅 16:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16644">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">بدل موشتبی خامنه ای خودش دهن باز‌ کرد !
این ویدیو رو پرت کنین تو صورت عرزشی ها !
@withyashar</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/withyashar/16644" target="_blank">📅 16:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16643">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ترامپ به ناتو : کاری که تو ایران انجام دادیم، اصلاً به کمک هیچ‌کس احتیاج نداشت
حتی خودم هم کمکی نمی‌خواستم. البته قبل از اینکه برم، گفتن کنارمون هستن
ما هم تریلیون‌ها دلار خرج ناتو کردیم؛ برای چی
@withyashar</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/withyashar/16643" target="_blank">📅 16:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16642">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">خبرنگار: آقای رئیس جمهور، آیا قصد دارید جنگنده‌های اف-۳۵ را به ترکیه بفروشید و محدودیت‌های قانونی آن چه می‌شود؟
ترامپ: ما قرار است تصمیمی بگیریم. فکر می‌کنم خیلی‌ها - می‌توانم بگویم، خیلی از افرادی که همین جا نشسته‌اند - بگویند چرا این کار را نکنیم؟
ما رابطه بهتری با ترکیه داریم و ترکیه از بسیاری جهات بسیار وفادارتر از سایر کشورهایی بوده است که فکر می‌کنیم وفادار خواهند بود.
و مطمئناً چیزی است که ما در نظر خواهیم گرفت - بله
@withyashar</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/withyashar/16642" target="_blank">📅 16:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16641">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">قطر: ایران مسئول حمله به نفتکش ماست
ما ایران را مسئول قانونی این تجاوز و خسارات احتمالی ناشی از آن می‌دانیم.
هدف قرار دادن نفت‌کش قطری هنگام عبور از تنگه هرمز، تجاوزی مردود به امنیت کشتیرانی است.
ما از ایران می‌خواهیم اقدامات‌هایی را که به امنیت منطقه آسیب می‌زند یا کشتیرانی را تهدید می‌کند، فوراً متوقف کند.
@withyashar
🚨
🚨</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/withyashar/16641" target="_blank">📅 16:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16640">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">رویترز: نفتکش حامل گاز قطر که در تنگه هرمز هدف قرار گرفته، به دلیل آتش‌سوزی در اتاق موتور، در معرض انفجار است
@withyashar</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/withyashar/16640" target="_blank">📅 16:13 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16639">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IOf3-V2lCIBsOCBUZH-jHIZ5wa-CR_gWAHcXKxiE1utrbTsl1TiBw7hqaAEIMH35WK-Qiy78K9nAq_oosX9GLZpbttZkQ6n6MdX4SLXpOBbZvnKoPK01Zv7Nt-IIbgMV_ay5mhXsrUHa3GXg5aKwJmSVRcJX0NJSeX8EVwoxS-RaD83x2rqFNVTq7Wxf5peY-_Ch72rcw_UReYkYpWic0YTpWPPS4LeohgIXbbHmBmbD2OZFJIJt__CP_eRnJOnHX06jyLmJzNALOt8J7lf1xZYVhTO5npXz8YSikLHmXG1sQNvq9gtnuIyvFUnmGEffZULAAYxiSrD63BFoOO9ozQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در‌ تروث : کارخانه تویوتا از مکزیک به ایالات متحده (تگزاس!) منتقل می‌شود. یک معامله بسیار بزرگ. تعرفه‌ها در حال اجرا هستند!
@withyashar</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/withyashar/16639" target="_blank">📅 16:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16638">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ارتش اسرائیل و شاباک : ارتش دیروز در شمال نوار غزه به دو پایگاه تروریستی حمله کرد ابتدا، احمد یحیی ابراهیم بتش، فرمانده یک گروه نفوذی در سازمان تروریستی حماس و در یک عملیات دیگر  جنوب نوار غزه، حمواده ابودقه، فرمانده یک واحد اطلاعاتی نظامی در این سازمان را به هلاکت رساند.
@withyashar</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/withyashar/16638" target="_blank">📅 16:10 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16637">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">هم اکنون از سیریک صدای دعوا در تنگه شنیده شد
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/withyashar/16637" target="_blank">📅 16:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16636">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bfc7d0dc6.mp4?token=V6TOHo6EsB8NX33aCZgJpwpgPq0oX4AmELLGcXPAEPrT4FsSELrd6lagX0ZWSv2gY7MOYAOGvPqDi3s5_IA_LP6GOpC7G5kTDFlo9C5giCm_7x3CjycTBX4F6wdc_e4Qw2nFiBOGhYv-9149i5k4-eg0pjh1VjcllMd36Q69aUtMINbPsyzO7G9I_L1ipOC4-VXsefWVzekqfqJ1l5SdEVtUFXz_TAaAunMtbXDVZwCL8i3gv5H39txGTLcWHyWg0MoACwQ4RM2B1ysiEvdhjPimerKDXPKEwGLM3BYM-YnHFgT9Y9hz_x9yMoAQNKebopqrmz4XLavbN9bizWl06Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bfc7d0dc6.mp4?token=V6TOHo6EsB8NX33aCZgJpwpgPq0oX4AmELLGcXPAEPrT4FsSELrd6lagX0ZWSv2gY7MOYAOGvPqDi3s5_IA_LP6GOpC7G5kTDFlo9C5giCm_7x3CjycTBX4F6wdc_e4Qw2nFiBOGhYv-9149i5k4-eg0pjh1VjcllMd36Q69aUtMINbPsyzO7G9I_L1ipOC4-VXsefWVzekqfqJ1l5SdEVtUFXz_TAaAunMtbXDVZwCL8i3gv5H39txGTLcWHyWg0MoACwQ4RM2B1ysiEvdhjPimerKDXPKEwGLM3BYM-YnHFgT9Y9hz_x9yMoAQNKebopqrmz4XLavbN9bizWl06Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرتاب سنگ به سوی وزیر امورخارجه ، عراقچی که با چند متر اختلاف به ماشین کنار وی میخوره
@withyashar</div>
<div class="tg-footer">👁️ 74.3K · <a href="https://t.me/withyashar/16636" target="_blank">📅 15:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16635">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79f08747f0.mp4?token=i9lo8TUrUTxeJ7589qXVr3J7Rr6nDF2EehHIQu55-Ee1w-y8CSGDFrP8UW2arQeTkF-m-YK9WktSgljEeeL3i1J19XA1h1_mPSvvmNZYFl8Sci1BXT8flZklfau54KbJ--XC88Uzzj4N89VcYKXKrjdiETYmkicHYqUea7Ogr8MYfrNb580vg7egpj3AwAVXNYGfgY1rSXoWA1hnhKAO6c4VRyG7Pz4CQIQNmrBv-PqQDnfpe59uer3BUumsOuOTYPZHnP7FRWCR-55cUe54rIRa9sOjV2GNFAS1erSGHT5HAmm5cGYa9W7zyEOgMFy80R0yTuxp0PGpu6VgDcQa3TqRQsJ6DiVnUozoiNM0oDvyLlKgXORiu9TnF8Y_e0nF0bmuVd-1Rsh_8AFe3tCxbAYcHhUspz8qtM6YvT4UNjGi82qjc7rY9V2LwHydrMslh16qjuPgjGaHzFN5BzGIw1TD931W_-IYng5Xfif9AlfcbW79vuwZmKNqjQmFvI7ZaeAAlpJVB25lb8pPY--UWgSaOiOfblFMyHCZTdYzlRpKiKdj2XjFWDRaMmv5Rv4vJkoJLjT0VJP1Y1vkozMQGpSd4MfnGivSTs_KcoeWBrcLjTRaIxJ_mhgsUCtGpsW_X5cECNVwV-XfMtCevkiKDqqW9D4ghwF7KPEiAbqj87o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79f08747f0.mp4?token=i9lo8TUrUTxeJ7589qXVr3J7Rr6nDF2EehHIQu55-Ee1w-y8CSGDFrP8UW2arQeTkF-m-YK9WktSgljEeeL3i1J19XA1h1_mPSvvmNZYFl8Sci1BXT8flZklfau54KbJ--XC88Uzzj4N89VcYKXKrjdiETYmkicHYqUea7Ogr8MYfrNb580vg7egpj3AwAVXNYGfgY1rSXoWA1hnhKAO6c4VRyG7Pz4CQIQNmrBv-PqQDnfpe59uer3BUumsOuOTYPZHnP7FRWCR-55cUe54rIRa9sOjV2GNFAS1erSGHT5HAmm5cGYa9W7zyEOgMFy80R0yTuxp0PGpu6VgDcQa3TqRQsJ6DiVnUozoiNM0oDvyLlKgXORiu9TnF8Y_e0nF0bmuVd-1Rsh_8AFe3tCxbAYcHhUspz8qtM6YvT4UNjGi82qjc7rY9V2LwHydrMslh16qjuPgjGaHzFN5BzGIw1TD931W_-IYng5Xfif9AlfcbW79vuwZmKNqjQmFvI7ZaeAAlpJVB25lb8pPY--UWgSaOiOfblFMyHCZTdYzlRpKiKdj2XjFWDRaMmv5Rv4vJkoJLjT0VJP1Y1vkozMQGpSd4MfnGivSTs_KcoeWBrcLjTRaIxJ_mhgsUCtGpsW_X5cECNVwV-XfMtCevkiKDqqW9D4ghwF7KPEiAbqj87o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استقبال اردوغان از ترامپ در فرودگاه آنکارا، همینطور حضور سربازان ناتو با یونیفرم جنگ جهانی دوم.
@withyashar</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/withyashar/16635" target="_blank">📅 15:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16634">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">علیرضا فغانی کاندید قضاوت فینال جام جهانی 2026 شد.
@withyashar
🏆
😍
💥</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/withyashar/16634" target="_blank">📅 15:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16633">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbedf1332c.mp4?token=Y0lJ5K3F7T9LChcfpAhwOaeedV3KCGxRGjAvtslSj5vI9cAXYBEcmWHjlDgAk4Zp_uUAbxf1N4cI21ezN6w-JA99M3BQIyBr_aEggVmGwUmWFRysWyDOkoOJSlZyOYdc7w1Og0OC6Z7I9aAcjZe6HZ1sEvoSWT5bR1uk5ccrrK6v_2g0xmH0x8IRhx_uYeqfNoK3sz7iOSBQOE2f_Bo_FB79ld0M-GYR0yiiwrrP23cDmMs__yVW28YDkZgNQmL7Vfh6NYBl6S8SVkZLASSuWDMUxiak7I6BMsKIMUup787fskyEvIbYHVLFG_5XQchGo--iJ2tbn8KRxwy_RPaREg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbedf1332c.mp4?token=Y0lJ5K3F7T9LChcfpAhwOaeedV3KCGxRGjAvtslSj5vI9cAXYBEcmWHjlDgAk4Zp_uUAbxf1N4cI21ezN6w-JA99M3BQIyBr_aEggVmGwUmWFRysWyDOkoOJSlZyOYdc7w1Og0OC6Z7I9aAcjZe6HZ1sEvoSWT5bR1uk5ccrrK6v_2g0xmH0x8IRhx_uYeqfNoK3sz7iOSBQOE2f_Bo_FB79ld0M-GYR0yiiwrrP23cDmMs__yVW28YDkZgNQmL7Vfh6NYBl6S8SVkZLASSuWDMUxiak7I6BMsKIMUup787fskyEvIbYHVLFG_5XQchGo--iJ2tbn8KRxwy_RPaREg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اردوغان در فرودگاه از ترامپ استقبال کرد
@withyashar</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/withyashar/16633" target="_blank">📅 14:54 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16632">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">در سال ۱۹۷۵، زمانی که رضاشاه به همراه همسرش به ترکیه آمد، همسر فاروق کوروتورک، رئیس‌جمهور وقت ترکیه، سرویس کامل اتاق خواب خانه شخصی خود را به کاخ چانکایا برای ایشان منتقل کرد، چون در آنجا امکانات مناسبی وجود نداشتیم.  اما امروز، خوشبختانه، با همه امکانات موجود،…</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/withyashar/16632" target="_blank">📅 14:51 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16631">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2a9d31515.mp4?token=VzfvcFOQsT4nN308uZ_NhZ0aLSFvucOgknHr71lDWqdflluxaRfu5SMYjjpVgmMx0bzF-KUOJsh9t7i8sOUbba2SqVBbmQ2qPEtc9Yadi3cw4S3PLZ7dOjj9irx6lgFq6rlhyFP7voOolM5kh8DtEyXYGaBg2RaasFsBkdmcB3gjNk-Q7XNEhkrw8koDR43uptX9-y8ZUjurKfn2MUvkDjSjPEb_zDhU4H5Hpdv_B_oIy6e3PIE-A87-3ErWloxprDV6jWkhwPdllba8vhVrUElZSYZ26AIEApvrnyefXWO0czt3d8KbnDPAQjAXggof0k-KJ3S-QfQKG8xISbHP2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2a9d31515.mp4?token=VzfvcFOQsT4nN308uZ_NhZ0aLSFvucOgknHr71lDWqdflluxaRfu5SMYjjpVgmMx0bzF-KUOJsh9t7i8sOUbba2SqVBbmQ2qPEtc9Yadi3cw4S3PLZ7dOjj9irx6lgFq6rlhyFP7voOolM5kh8DtEyXYGaBg2RaasFsBkdmcB3gjNk-Q7XNEhkrw8koDR43uptX9-y8ZUjurKfn2MUvkDjSjPEb_zDhU4H5Hpdv_B_oIy6e3PIE-A87-3ErWloxprDV6jWkhwPdllba8vhVrUElZSYZ26AIEApvrnyefXWO0czt3d8KbnDPAQjAXggof0k-KJ3S-QfQKG8xISbHP2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در سال ۱۹۷۵، زمانی که رضاشاه به همراه همسرش به ترکیه آمد، همسر فاروق کوروتورک، رئیس‌جمهور وقت ترکیه، سرویس کامل اتاق خواب خانه شخصی خود را به کاخ چانکایا برای ایشان منتقل کرد، چون در آنجا امکانات مناسبی وجود نداشتیم.
اما امروز، خوشبختانه، با همه امکانات موجود، از تمام رؤسای کشورها به بهترین و امن‌ترین شکل ممکن پذیرایی می‌شود
@withyashar</div>
<div class="tg-footer">👁️ 77.1K · <a href="https://t.me/withyashar/16631" target="_blank">📅 14:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16630">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/withyashar/16630" target="_blank">📅 14:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16629">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2d3acaa8f.mp4?token=jKn1qspfKlQV9SPg6HabDCepb2lnBJPyiYA6W9fQ_cvOwC5U25vi99pB2yDxNKcgSmASYq2uPlLKMzJMZtphCba3NO_UaUAfysiomBbfn5cEl32CFyxfI68N04ZnlayQo-RHP6Maxt9uXpFBgta4hHqx_cdC-KT2NnaTxKbwahnK_V3JR6azXF3Vc1pYSWf72Cmd3u95B8fCCBSYMvGfzy83XBTqrLiDntrWxZY4-EQ7WjARB_6XbH1Iv6ZGClRjvcFjzagT3FlujPTqSSHiTsPyIy7lbtX7xnt8S_0cn6lguWt1bK-VLuf-NOZN0Fg17w1YOxDOFTUzGR27iHIafXkclJE6toKBzYD9SJNfG6hBX8AoAl0GMKz5TwBoxTuVTQv09gUtm5X9P8PpBKUMh4lOmUitX8wmjLCGTcon8TL4NoEK6TPODgEkF3tCublzMZ7cgas9JvT8Y_fqmWHEhkKC8h3abt-9lGzmgQl76bE9pzhwRKOW8XquZXhV0KDuA5UnXkUzPLVkS2L1TxjxDbLsih9MDB3si4YvSktO_ytd0BbiB1248mWJPX-XBxd7oBmaq_TrFLOREry1VWfHC67Ot6BRGT4dxXNpYlR8Wv8fe3cXkJRftLlSPtY_BVFf2QZFsnEERqLHvoFJOTZy6Lm8_OQCot-_M7A1BIm5Q_4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2d3acaa8f.mp4?token=jKn1qspfKlQV9SPg6HabDCepb2lnBJPyiYA6W9fQ_cvOwC5U25vi99pB2yDxNKcgSmASYq2uPlLKMzJMZtphCba3NO_UaUAfysiomBbfn5cEl32CFyxfI68N04ZnlayQo-RHP6Maxt9uXpFBgta4hHqx_cdC-KT2NnaTxKbwahnK_V3JR6azXF3Vc1pYSWf72Cmd3u95B8fCCBSYMvGfzy83XBTqrLiDntrWxZY4-EQ7WjARB_6XbH1Iv6ZGClRjvcFjzagT3FlujPTqSSHiTsPyIy7lbtX7xnt8S_0cn6lguWt1bK-VLuf-NOZN0Fg17w1YOxDOFTUzGR27iHIafXkclJE6toKBzYD9SJNfG6hBX8AoAl0GMKz5TwBoxTuVTQv09gUtm5X9P8PpBKUMh4lOmUitX8wmjLCGTcon8TL4NoEK6TPODgEkF3tCublzMZ7cgas9JvT8Y_fqmWHEhkKC8h3abt-9lGzmgQl76bE9pzhwRKOW8XquZXhV0KDuA5UnXkUzPLVkS2L1TxjxDbLsih9MDB3si4YvSktO_ytd0BbiB1248mWJPX-XBxd7oBmaq_TrFLOREry1VWfHC67Ot6BRGT4dxXNpYlR8Wv8fe3cXkJRftLlSPtY_BVFf2QZFsnEERqLHvoFJOTZy6Lm8_OQCot-_M7A1BIm5Q_4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ همکنون در آنکارا به زمین نشست
@withyashar</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/withyashar/16629" target="_blank">📅 14:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16628">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">رئیس‌جمهور آمریکا برای شرکت در اجلاس سران ناتو، وارد پایتخت ترکیه آنکارا شد
@withyashar</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/withyashar/16628" target="_blank">📅 14:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16627">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cVNyTggYunkFaNaeiQwdJdLO94tZy-LqtCCVeZI4Rdh3Rr1BbRBXZAflPftcZNCuhYhV6Uu_wuYMGK073X5mO0S0LoOXlEqvgYPxFXBUMTEXm2Y2lA_StP4BmVVNpHRI4NMKpodJ-LBAxi8aoJS8As0pTlWE4bfVPBL4ck5Do3Ady2vXoggL9d6hyOKgpiqn2rmtwsZ-PBwzQ4tdklYeVfLkGvSjyZ8KHHPLY1A2n9rG32i9CK1jA-suCm6DJwh21jDwRWs_XS5J4Fw0XD40A2nO1NaJaxfOnqLO15aUZkXXxiKtzaFJLcu68M2fSt8I5HApTHDyTcJSHTOYcwDjlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با هواپیمای ایرفورس وان جدید هم اکنون در حال ورود به آسمان استانبول است و حدود چهل دقیقه دیگر در فرودگاه آنکارا به زمین مینشیند.
@withyashar</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/withyashar/16627" target="_blank">📅 13:41 · 16 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
