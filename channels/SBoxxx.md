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
<img src="https://cdn4.telesco.pe/file/id5uQZ5JDqhCR7wbXivEfWa01wvd7iHPRLRHwOvCOOY3tC1qSMA6ljkjgsKBksjDN40_ILXVp9vCppuupAgfuONCR1-2jc4047kwtNjFay9dXj66dLCqWn7Obyo0t4mXj4O1GQ9dRVJpaHeYB_4jwqVPxYQ2iVdkHTmq31ug4-JskfmNSSKHQ4QCU1etrVbPQaYvgxJcwcqho7AjZ8FqcG1MxFmTbmQg984koqBjOu6QoU7BiJWI_AwWRrtFD5_3XWHcQytdGtnw26ynbeLN11kABZ4biAMZH38NEvs5mV6y34MTRy-zGSDFaUbev0I8vHAYv0maK_0-cHqkG0E8ig.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.2K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-19 22:25:00</div>
<hr>

<div class="tg-post" id="msg-18494">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">صدای انفجارهایی در کرج!</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/SBoxxx/18494" target="_blank">📅 21:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18493">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">وزیر دفاع روانی اسراییل:  امروز در مراسم اختتامیه دوره آموزشی "کنافیم 192" شرکت کردم.  اینها فارغ‌التحصیلان دوره خلبانی هستند که رهبری اسکادران‌های هوایی بعدی را به سمت تهران بر عهده خواهند گرفت.  ارتش اسرائیل آماده است تا عملیات را از سر بگیرد، برتری هوایی…</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/SBoxxx/18493" target="_blank">📅 19:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18492">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jUWAD6WgjH8zs26Vm8RUIYt4GsW84f38FmoEBtIXVaFRka1RUXmxpngJuF6-jL-GmRCAMVDO29Np0u57QwzATPkgolJzkWFTWx-Xb5h8Ww3kKjRCTaatqYXZTXtHhb1x9gxUfJ9o41NOwCTOvPrQf7D7w-5N4vwzvG77wOfamjM8Dc2hbZ8q7Ie7hP9xqOHsteqbNdVQnHBvT1YGTbut9hx3tPLDtDIMENHCvGcqVF7a0owJ_0APNGiCkKTiWcRgnhVMMW7C61qFyZve-aiuePtc1NiMGLFFq_CS_fQ5cMpexVzj-RMvdorIULeM_7VKXzRrtKx-qZ_ZTbjXu4iFQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر دفاع روانی اسراییل:
امروز در مراسم اختتامیه دوره آموزشی "کنافیم 192" شرکت کردم.
اینها فارغ‌التحصیلان دوره خلبانی هستند که رهبری اسکادران‌های هوایی بعدی را به سمت تهران بر عهده خواهند گرفت.
ارتش اسرائیل آماده است تا عملیات را از سر بگیرد، برتری هوایی را دوباره به دست آورد و برای بار سوم به ایران حمله کند.
احساس می‌کنم خلبانان جوان در آینده نزدیک مشکلی در کسب ساعات پرواز نخواهند داشت.</div>
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/SBoxxx/18492" target="_blank">📅 19:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18491">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">انفجار در پالایشگاه نفت پلدختر در استان لرستان</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/SBoxxx/18491" target="_blank">📅 19:41 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18490">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک به درستی پیش بینی کرد که یک اصلاح نزولی در طلا و دیگر دارایی های ریسکی داریم که پایدار و شدید نیست.  اکنون هم سطح شاخص کاهش یافته و رشد بیشتر طلا را متصور هستیم.</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/SBoxxx/18490" target="_blank">📅 19:41 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18489">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CgTs28mOv_7nuF7eEsRbY5uOsNJvgZ33b-oJ1Mn4vXvA0AyizUvYATw8eRKSP08VsaZyV1LMHKRCgP2-bs_gpmeBNt40L99aziYPBlKMbnma5rM-j2Aq2kdplfT3RXDMLJEJItE8rmFJg8bsLJFiPjQ735087_frV9iwE9epC8AIGz2NsvLD6T2qe_3ch2F73gInCTlRo6k0ceH5sW7AgLctGcctgXFZpYU_m1HK_mBo0TPRwUu6FkmsB76jRT2JRGsA3dXDCkTVz2BfCMNqY20EJgYusVqfmktIOtIH2cbRyBA8wnhcXN0Bi36y5WEAQUp8ATU_O3xcQ2IjOB4a-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک در میانه بازه خود قرار دارد و پیش بینی می شود یک اصلاح نزولی در دارایی های ریسکی داشته باشیم که عمیق و شدید نباشد.</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/SBoxxx/18489" target="_blank">📅 18:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18488">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CCpk72bq344ZZU8HsfNuzP5Ib6DVuIhc2iYpoPb5cAE0uaznB_Q7_7SN17glK1OT2qQVvKkhEarONXHZMrhcnhhry7s5gznyTFsVMTn5gWjkVxjAdXzY6pJlC6v2W0yPcRMebPeDCAesc6Gfae5RfWMhI0L0UQrI5gZQoRvAjD9Db8ZaT1qVc9aoPyF3zJjvHU0CjRTP76kY2JtOmHu0hf6jCtZEmBudV8Il3IGsbnH9t0QBtpUnrPbHE3ldjOpYDswQ5iXsP8YBzdjtnNqYoXaxk2Vdk60igeLC4J66dFcp1K2j7H8efMsTD4rnSEzjJy5elFD5g_iaCt1SFy_3qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بنده خدا واقعا باورش شده ما برنامه ترورش را داریم!  یک نفر به او بگوید ما از سال 1367 هنوز سلمان رشدی را نتوانسته ایم کامل بکشیم.</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/SBoxxx/18488" target="_blank">📅 18:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18487">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mwqmi2aNxnqpbM4_jCoCFy2_hELidIG2kKm-_fjnMBonVwdmZ0uKgl9P9wSIpTaXeGIkYwI9mhpaD8MU7tpRWq3AimCW1ToUDvIXtUHfxEEEfZ2tZuqXvT1RgyzBABW2cz-hhPILpwrDp3YNfHK3FdvqH2X2j9iTeqD4nCa7I2a9dhAMRPKiXZ_TpgLsmyCdPYq1yq48A3B2dVV76Tp6BOj0_we48KuhlhC5gu7ebwcMd4tCi-0p02Wou6r8O_e-ZfD9SbWunx0hCeU7dg5Fun7PlDtNson06q31Sz9kuWOwf0uxFpz00yFK4hq5zINdYMw5rohSA3GvtUyODS9y_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/SBoxxx/18487" target="_blank">📅 18:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18486">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">بعد از اینکه ترامپ گفت آتش‌بس با ایران به پایان رسیده است، گزارش شده که دو ناو هواپیمابر آمریکایی به طور غیرعادی در نزدیکی ایران و در محدوده برد موشک های ایران دیده شده‌اند.
این موضوع می‌تواند نشانه‌ای از آماده‌سازی برای تجدید فشار یا اعمال محاصره در تنگه هرمز باشد.</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/SBoxxx/18486" target="_blank">📅 18:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18485">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ترامپ :  در صورت موفقیت ایران در ترور من، دستورالعمل‌هایی برای اقدام صادر کرده‌ام</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/SBoxxx/18485" target="_blank">📅 18:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18484">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">وال‌استریت ژورنال:   بر اساس اطلاعاتی که اسراییل ارائه کرده، ایران طرح جدیدی برای ترور ترامپ طراحی کرده است.</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/SBoxxx/18484" target="_blank">📅 18:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18482">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hwh69LLJjq0GBsTELxns5Kw465T9AZYEazVC31RxZW7pS55uy_VNZ6dM0TYYRc_UZXpbXf3ViK1dJIibQ1DbjNzPMCP7TocJB5uvvnOETRynlx1q6CVMZzLtCjs_5bcDaSXbjSn5Ox9CsNzYA18MSsc5UQBt_cP2aWHutgL42mFWKsBEpuhyjVoyrL3qumDB9eeK0P1Kb22d6mdciJ-CDVDnUbVOzCxCpoIFMn1Jh79UpR8cCsJkxHtqog725lizkbHH6qf_b8guSgogADc436IvMD5t0Rb6nKlRAc0R0y_OUQMIpDp1jPaoa0F1NNqkuTA5U0Nmu2SdyF7LCY44wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ می گوید جمهوری اسلامی از آنها درخواست ادامه مذاکرات کرده اما آتش بس تمام شده است!</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/SBoxxx/18482" target="_blank">📅 18:39 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18481">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">یک هیئت قطری با هدف نجات مذاکرات بین ایالات متحده و ایران به تهران آمده است.</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/SBoxxx/18481" target="_blank">📅 18:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18480">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">فقط میخواست ما را ضایع کند که گفتیم فقط شبها برنامه بود در آن فیلم</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/SBoxxx/18480" target="_blank">📅 18:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18479">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">عجب گیری کردیم به حضرت عباس</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/SBoxxx/18479" target="_blank">📅 18:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18478">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">صدای انفجار در کنارک !</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/SBoxxx/18478" target="_blank">📅 18:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18477">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">خوب خاطرم هست در دوره دبیرستان یکی از بچه ها یک فیلم ویدیویی آورد که رویش نوشته بود «جدول تناوبی عناصر» و دقیقا داستانش مثل همین مذاکرات ما با آمریکا بود
روزها صحبت می‌کردند و شبها با هم حکم بازی می کردند. حکم تفخیذ.</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/SBoxxx/18477" target="_blank">📅 18:27 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18476">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ترامپ می گوید جمهوری اسلامی از آنها درخواست ادامه مذاکرات کرده اما آتش بس تمام شده است!</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/SBoxxx/18476" target="_blank">📅 18:16 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18475">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MEjyb-e3I16BA8LK-c9Mlrjy-O6RcOZy55RttzrqV1Dl9G4lmISRJepx7fnrX2Kjb5gUkLjHpvGcAOBLn2ZSlztmMaILO_kttqtpbLG9HSKxu4TSBY727wW6XgMiJaLCc9CvM2aHCk3kbBqoj0dnzNK-66qwOiB4YXeLdTdDVq8VufQNOM26r2iJGXgMCztWK2RX_AiLwPx0qB6V2CJhDSG-d8oSSNxWF4X9_bZeVNefEGMTfLCqTLznUTzO4Br8Xg9c1jEC6RWZY9oshmHGEZlID11EOa8QKve7ldOs5vOZWYkdXg-uamox2bL-l94rG4ezwWcIwg0ShO1NL2F6Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ می گوید جمهوری اسلامی از آنها درخواست ادامه مذاکرات کرده اما آتش بس تمام شده است!</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/SBoxxx/18475" target="_blank">📅 18:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18474">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ادعای بابک زنجانی در خصوص خرابکاری در راه آهن آق قلا</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/18474" target="_blank">📅 14:14 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18473">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H880P9E3CwIAryiSoET3XK3jl42e0lEO4XniOnv3ReOWb_IpvaoNUiuVwB1teWHSfIbcMDtks8Ymhzqq-U5QYk5Y-rhEvOWgWWRjI4b6LCfvz0FZetsJJ6U9HXY_wejYjfyiZxPrRj0kxuM-NxrZN8h4lOiHEoU_7wSg6xcB3ZVoclCiPItouLL6cK1Fpvg_g5KbDGnqx1h9uIWBVHDL3kQX6DiRgaTYEcpa2gBkE6kDgWPPKN__ktNGIiqSpAFIC8FXaTe1aMEzhHK8gqrKIzqxetlkM1DZ3AGF8PFerB_2ThREj1hZAxr7YUEIeKW9qz9OQEqcBmCCDvgw7TypTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای بابک زنجانی در خصوص خرابکاری در راه آهن آق قلا</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/18473" target="_blank">📅 14:12 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18472">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">#پادکست_GeoMarkets  شماره — 5  جمعه 10 جولای 2026</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/SBoxxx/18472" target="_blank">📅 14:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18471">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">دو نکته:  — از این میان ما سومی (J-20) را داریم. (البته ماکت ش)  — آخری (جنگنده کان یا خان ترکیه) فقط یک مشکل کوچک دارد و آن اینکه موتورش هنوز پیدا نشده که انشالله این هم حل می شود.</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SBoxxx/18471" target="_blank">📅 13:19 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18470">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ep87iBVaCTr-R_LdWtEqOJYZC1oZpAqR2uFlLhNJTdz5xd_jUY4Y8pOV0nxybXSM6S8PxYTsT7BD1MGhwhNhCJXPHq7F_aGKn0Om-eZc2wCMzyYGQs31xxadxNCUezcuz-sBQ6HR4rLuY7dcOFvZL9XQtVu187EPsrCuA2hD62Wz4ORDouloHfK4GZb2YdDi_sCYT9EBcTTj5gLFQ2h9nSS0ujHOh_Sk_2Ht0PQ96lJn6tB-iyL5zKQDdRyPQ6z5OgseZSr36Yj4g_3osoi4kyJNiEKyfikywZ9RXXGKcEjhlCXXOtfB7UitprjcBsrws3FjusgqEwSgTLML6Q947g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا افرادی با لباس نظامی به نیروهای بسیجی مستقر در یک ایست بازرسی حمله کرده و دستکم ۲ نفر را کشته اند.</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/18470" target="_blank">📅 12:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18469">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">الشرق الاوسط: حماس جلسات رهبری خود را از قطر به ترکیه منتقل می‌کند.
در ماه‌های اخیر، این گروه بخش قابل توجهی از فعالیت‌های سیاسی خود را به ترکیه منتقل کرده است، در حالی که قطر سال‌ها به عنوان مرکز اصلی فعالیت‌های سیاسی آن عمل می‌کرد.</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/18469" target="_blank">📅 12:38 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18468">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fW8sShqPenn7Sanex-gA9svDqsgoPjztXPChV0piWaaxySUlqAT9z6a_39Ek5NZtiOrKXgZCZf29khOiKpqcHtiR85ED-VC9asAqnwvjIni3hSbZwM4mDhFdqGTsJWdTecruGcu7M8jM_opz2iA7IFKl2pLtDbLK-I4E1wfm2p6i_cUBGDvJXbSw2RyFaz_lY_o-LsRphopbN6Mb5VyNs2J1Va2QrdQ2kvCsqxVYhLAPCmP-t9c6ieKqj8rxOAcOgwUVIyMR_6TBjmWQetEIYIB-61CHoJQiL4WWAREiL9ZBX7pclokW4tf01GKKu45ht8nv5psmgmx7ioVzwHGHPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک در میانه بازه خود قرار دارد و پیش بینی می شود یک اصلاح نزولی در دارایی های ریسکی داشته باشیم که عمیق و شدید نباشد.</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SBoxxx/18468" target="_blank">📅 12:08 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18467">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/18467" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 5
جمعه 10 جولای 2026</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/18467" target="_blank">📅 12:07 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18466">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">یک مقام آمریکایی به شبکه CNN گفت که ایالات متحده و ایران در حال انجام مذاکرات غیررسمی برای کاهش تنش‌ها هستند، این در حالی است که پس از یک سری حملات متقابل، این مذاکرات در جریان است.
ایالات متحده در حال حمله و سپس توقف است، به این امید که از تشدید بیشتر اوضاع جلوگیری کند و به دیپلماسی فرصت عمل دهد. در عین حال، واشنگتن برای انجام حملات بیشتر امشب، در صورت لزوم، آماده‌سازی‌ها را انجام می‌دهد.
بر اساس گزارش Axios، دونالد ترامپ "به شدت به دنبال راهی برای خروج از جنگی است که آمریکایی‌ها از آن حمایت نمی‌کنند."
پاکستان و قطر نیز در تلاش هستند تا هر دو طرف را به میز مذاکره بازگردانند. میانجی‌ها معتقدند که حملات اخیر ایران در تنگه هرمز، توسط جناح‌هایی در داخل رهبری ایران صورت گرفته است که با توافق‌نامه همکاری مخالفت دارند و در تلاش برای تضعیف آن هستند.</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SBoxxx/18466" target="_blank">📅 11:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18465">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LPfgrt77jJcashSJCZcOSxJkmDwWjMGx7K6F0mDcc6xssU59PPCEc2xePO-8mZs4jRa7ajzInt18mHUzwhaShblGa-rAeu0iiIktPMT20sDyzZmHW7WRlJF9QIKcPcO553dI_twwsGkg0G-zm4Nz_iELdLvOak5dVciNwNCKCS8q8LN6ZdVcqlafxyKNvnfqMGplw3JXYR0pPmym_gkPWtgfkBrDrpxdLS-9GXr49uF5yz6S2pWVdS4NlaenP6-v_fCqjhRdEf-cGvXmPQUs6JtXHGiKhCszpRUmbw2lSJTYSq2CU8hYopUckjVBGQ58sCwYuwyJBZKGJj2nJBIb1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک که از صبح پایین بود و منجر به رشد طلا و افت دلار و نفت شده بود، اکنون جهش کرده و پیش بینی می شود در ساعات آینده در بازارهای مالی شاهد یک موج ریسک گریزی باشیم.</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SBoxxx/18465" target="_blank">📅 11:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18464">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Df1iIjGuzYIE--LVtOzCsQgajnnwZnSKDTo5hnzoxBISZR1mLKqmhZ9yHfRzkKoEF0FT2jvphzUrR4901Wq748hw78TGs2DJR8Ajp_1lXizrv4cJB-eQUekm03Ot8R8aYWpAgKArgsQCmTC_QgRlJzCeVlkUreiB3-tXhl3WVc-i-DgOHfTXB8Vt_lqtmymLLCqpRO0AVsMqnrCkpL2vVoAbiACscmZzQhw10Ei03ah9dL8juq0ioVXs7-MHGRB7Urt36BVb8ZJmN1NpFhEBV8zNuBZrxcgi7nMJW8Ax7HTo27L0fJFpKSLaZPKaXtJwk30jwh5oYK_J4ONk6_1SLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگ-۲۹ همراه؛ جنگنده‌ای واقعی اما با محدودیت‌های مهم
انتشار تصاویر اسکورت هواپیمای حامل پیکر رهبر پیشین ایران توسط یک فروند میگ-۲۹، موجی از بحث‌ها را در فضای مجازی به راه انداخته است. برخی کاربران مدعی شده‌اند که این هواپیما در واقع یک
میگ-۲۹UB
، یعنی نسخه آموزشی دو سرنشینه، بوده و به همین دلیل از رادار بی‌بهره است. بررسی مشخصات فنی نشان می‌دهد که این ادعا تا حد زیادی صحیح است، اما نتیجه‌گیری برخی مبنی بر اینکه این هواپیما «جنگنده واقعی نیست» نادرست و اغراق‌آمیز است.
نسخه MiG-29UB برای آموزش خلبانان طراحی شده و به دلیل نصب کابین دوم، رادار اصلی N019 از دماغه آن حذف شده است. در نتیجه، این هواپیما توانایی کشف و درگیری فراتر از میدان دید (BVR) را مانند نسخه‌های تک‌سرنشینه ندارد و نمی‌تواند از موشک‌های هدایت راداری به همان شکل بهره ببرد. این موضوع، توان رزمی آن را در نبردهای هوایی مدرن کاهش می‌دهد.
با این حال، حذف رادار به معنای از دست رفتن کامل قابلیت رزمی نیست. میگ-۲۹UB همچنان از دو موتور قدرتمند RD-33، عملکرد پروازی مشابه نسخه استاندارد، توپ داخلی و امکان حمل برخی تسلیحات، به‌ویژه موشک‌های کوتاه‌برد حرارتی مانند R-73، برخوردار است. بنابراین این هواپیما همچنان قادر به انجام مأموریت‌های رهگیری دیداری، گشت هوایی، آموزش رزمی و اسکورت تشریفاتی است.
در مأموریتی مانند همراهی هواپیمای حامل پیکر یک مقام بلندپایه، هدف اصلی معمولاً نمایش اقتدار، احترام نظامی و ایجاد جلوه‌ای نمادین است، نه مقابله با یک تهدید هوایی پیچیده. از این رو، استفاده از یک فروند MiG-29UB برای چنین مأموریتی امری غیرعادی محسوب نمی‌شود.
در مجموع، اگرچه میگ-۲۹UB فاقد رادار است و از نظر توان رزمی با نسخه‌های عملیاتی میگ-۲۹ برابری نمی‌کند، اما همچنان یک هواپیمای جنگنده با قابلیت‌های قابل توجه است و نمی‌توان آن را صرفاً یک «هواپیمای آموزشی» فاقد ارزش رزمی دانست.</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SBoxxx/18464" target="_blank">📅 11:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18463">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">سوزاندن ترامپ لگویی خندان دیشب در مشهد!</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SBoxxx/18463" target="_blank">📅 11:08 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18461">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/keZBxrxRK89L5sLoeVMuGUbfJ1VqWsw0ZtJpL7R9Cr1ikTuiaLJdSo5eLAplkRA7rlOMgtvlrKNK2kP5MyscqSplxKqQEHAf_v2rR2wzUfkigB6uG2N5PPa595PAGRh3jGNGb520kFIlW48hhz9ICA9gEIx6E0cUrx355Mi_xhNI98ltb7psoQ-526N0IfwbAyMgOuXzNXQZhQM5kGRbi7Ld0S9fKZaaH54CSIrOHXBrh39Kqi811z7G6ZbbaWu60wWAoqA5XWrq5oqD_Qb9MyIRibEzkZDD9zZEc2fpdZPERYbBHiqj2V1WlUlX99sIlAJaXgtkKylu1VYD1QsgUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WySmR-zJpiV2KBtOn9f23s6sV0IJtfsM98ZdpNnzGd5TWtSLfX9ZambuE8yzqqcyHuqXwzx4PFlOiJ44awEPjJNTOywVVrCvX3dO3Ub1dtMpe9bBw9ZrHPwhApoyrOPwGdgiWuf-1SWtVxhsYMPURZ9ag0YDP0O4py_0OjVNTR-jhA8jcvii5_QfAtP2O56ysbWldhLCbmSFQKbzn8n6HZKI8RT2q9UKFfNwWvhw5qhngewl3QseYu8sBkNhsu0FAcvdRHVkUC6GdZTrryPjc2QFnceR4kGiNDlcyyLmJaGmH_gFMVQziP581ezDChYMV3J7jHJFeZzFi2DH80FcAw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هر چه فکر می کنم به نظرم چهره آقای نجاتی در عکس سه نفره هم هست!</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/18461" target="_blank">📅 10:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18460">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ترکیه سیستم پدافند هوایی S-400 خود را به یک کشور خلیج فارس – احتمالاً امارات متحده عربی یا قطر – فروخته است.  جزئیات نهایی شب گذشته نهایی شد و انتظار می‌رود امروز یک اطلاعیه رسمی منتشر شود.  منبع: عبدالکادیر سلوی، روزنامه‌نگار ترکیه‌ای (روزنامه حریت)</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/18460" target="_blank">📅 10:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18459">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">وزیر دفاع یونان، نیکوس دندیاس:  یونان از این موضوع که ترکیه جنگنده‌های F-35 را دریافت کند، راضی نیست. یونان از این موضوع که ترکیه موتورهایی برای یک هواپیمای نسل جدید دریافت کند، راضی نیست.  ما یک سوال مطرح می‌کنیم: آیا این موضوع به منافع واقعی ایالات متحده…</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/18459" target="_blank">📅 10:55 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18458">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">وال‌استریت ژورنال:
بر اساس اطلاعاتی که اسراییل ارائه کرده، ایران طرح جدیدی برای ترور ترامپ طراحی کرده است.</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/18458" target="_blank">📅 01:39 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18457">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T5LWjfzzv-w4m6cv6GzNm4n4ub6j-0kHih2FsgazJmuTS2nsLZBTBd4ytYF8vM5-RA8CYzhJWy4je7uyTvzM8XOfIdyl0hkerSQILAOYo6RM3-D_p2TCZjvQF0Zxu-lEdc-XWZ06cVKGievYUfEwxLTAdvsFVjfl6pm3ofSG9gLDYuhKPwjinQ6RsDluP65fvMi79xLkFg7f7iLtOWSxP4Y4RSrf_mijZazbrzKArPo6ejzhhaeMRrW8GEZjVNqPL-mnXh7wOdl8DMWBzFPCYdhK8-rr7d9deVkInl5rcbXRDs9cSgs9updMbMVkSrk45SVrh47SU3EZGxDWV0bTog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا افرادی با لباس نظامی به نیروهای بسیجی مستقر در یک ایست بازرسی حمله کرده و دستکم ۲ نفر را کشته اند.</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SBoxxx/18457" target="_blank">📅 00:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18456">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">انتشار اخباری تایید نشده از تیراندازی در اطراف حرم امام رضا</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/18456" target="_blank">📅 00:27 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18455">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">انتشار اخباری تایید نشده از تیراندازی در اطراف حرم امام رضا</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SBoxxx/18455" target="_blank">📅 00:09 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18454">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">تیم فرانسه به روزی افتاده که بلوندشان شده امباپه!  سبحان الله!</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SBoxxx/18454" target="_blank">📅 23:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18453">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">فرماندار کنارک:
منطقه نظامی نیروی دریایی در دو مرحله هدف حمله دشمن قرار گرفت
ایرنا</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SBoxxx/18453" target="_blank">📅 23:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18452">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">برخی گزارش‌های اولیه حاکی از یک ترور هدفمند در اهواز علیه علیرضا خدادادی، مشاور قرارداد استانی ولی‌عصر سپاه پاسداران در اهواز، استان خوزستان، ایران است</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SBoxxx/18452" target="_blank">📅 22:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18451">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">اگر کار آمریکا نباشد ۲ گزینه باقی می ماند:  — اسراییل — امارات</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SBoxxx/18451" target="_blank">📅 22:28 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18450">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">آمریکایی ها هر گونه حمله جدید را منکر شده اند</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SBoxxx/18450" target="_blank">📅 22:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18449">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">گزارش‌هایی مبنی بر حملات هوایی آمریکا در شهرهای اهواز، چابهار و بوشهر منتشر شده است.</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/18449" target="_blank">📅 22:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18448">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">گزارش‌هایی مبنی بر حملات هوایی آمریکا در شهرهای اهواز، چابهار و بوشهر منتشر شده است.</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/18448" target="_blank">📅 21:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18447">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">انفجار در بوشهر!</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/18447" target="_blank">📅 21:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18446">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">انفجار در چابهار !</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SBoxxx/18446" target="_blank">📅 21:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18445">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">فوری | رئیس ستاد مشترک نیروهای مسلح اسرائیل: ما به هر کسی که بخواهد به ما آسیب برساند، با قدرت پاسخ خواهیم داد.</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SBoxxx/18445" target="_blank">📅 19:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18444">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک که از صبح پایین بود و منجر به رشد طلا و افت دلار و نفت شده بود، اکنون جهش کرده و پیش بینی می شود در ساعات آینده در بازارهای مالی شاهد یک موج ریسک گریزی باشیم.</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SBoxxx/18444" target="_blank">📅 19:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18443">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mS-tKs0ztVYWm_CorLgvUaC0myUbP3ihpR2eootW8Wd8dpUt9V7RwXlrlfVJOk3CtIM53KLFywtSJfU5dnK8NgPgUEUCrJDeuz9DcP7mmpJD-NFCJcHY8DgOPQxW-qyPVo-YKVwCHTQu4qn_is7nq-l7hpVU8PNlgkaIZi7ML4stmtojvcExdGykU7vZyG07EuCtuxKiVeViqFErETh_jvuQNBJY2mWuEjRHgvy9-Rkap5jePlPVDQx92i1xJnufmtEOXQJ5KaTB3Cjf_kiWaA38qlneOwKy7lyU4F2jWO_uWjfXWc_aQDInbkVyGmjyMNicNHLTJiHUinTO3rjrCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در سطح پایینی قرار دارد و ریسک پذیری پیش بینی می شود.</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/18443" target="_blank">📅 19:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18442">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">سپاه پاسداران: مرکز فرماندهی کنترل دشمن در غرب آسیا و پایگاه هوایی الازرق اردن درهم کوبیده شد.
🔹
رزمندگان هوافضای سپاه ساعت ۱۴:۲۰ بعد از ظهر امروز مرکز فرماندهی کنترل دشمن در غرب آسیا و پایگاه هوایی دشمن در الازرق اردن را با ۱۰ فروند موشک بالستیک درهم کوبیدند.…</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/18442" target="_blank">📅 17:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18441">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">سپاه پاسداران: مرکز فرماندهی کنترل دشمن در غرب آسیا و پایگاه هوایی الازرق اردن درهم کوبیده شد.
🔹
رزمندگان هوافضای سپاه ساعت ۱۴:۲۰ بعد از ظهر امروز مرکز فرماندهی کنترل دشمن در غرب آسیا و پایگاه هوایی دشمن در الازرق اردن را با ۱۰ فروند موشک بالستیک درهم کوبیدند.
🔹
در صورت تکرار تجاوز ارتش تروریستی آمریکا سایر پایگاه‌های آمریکا! در منطقه از آتش سنگین ما در امان نخواهد بود.</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/18441" target="_blank">📅 17:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18440">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">وزیر دفاع یونان، نیکوس دندیاس:
یونان از این موضوع که ترکیه جنگنده‌های F-35 را دریافت کند، راضی نیست. یونان از این موضوع که ترکیه موتورهایی برای یک هواپیمای نسل جدید دریافت کند، راضی نیست.
ما یک سوال مطرح می‌کنیم: آیا این موضوع به منافع واقعی ایالات متحده آمریکا خدمت می‌کند؟ بله یا خیر؟ و البته، پاسخ این سوال بر عهده مردم آمریکا و دولت آمریکا است.
این موضوع قطعی است که برای دولت ایالات متحده، ناتو و به ویژه ثبات در دریای مدیترانه شرقی، از اهمیت بالایی برخوردار است.
بنابراین، آیا ارائه یک پلتفرم به یک کشور در دریای مدیترانه شرقی، بدون این شرط که این پلتفرم نباید علیه یک عضو متحد دیگر مورد استفاده قرار گیرد، به نفع ایالات متحده است یا خیر؟</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/18440" target="_blank">📅 15:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18439">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ارتش اردن اعلام کرد که ۸ موشک بالستیک ایرانی که به سمت خاک این کشور شلیک شده بودند را رهگیری کرد.</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/18439" target="_blank">📅 15:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18438">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">انفجار در شیراز و کرمان</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/18438" target="_blank">📅 15:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18437">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">— دونالد ترامپ:  «به نظر من، اسرائیل نیروهای خود را از جنوب لبنان خارج خواهد کرد.»</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/18437" target="_blank">📅 14:34 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18436">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">سخنگوی دولت ایران، فاطمه مهاجرانی:  "ما در حال پیگیری قانونی شکایت مربوط به ترور رهبر سابق هستیم که با جمع‌آوری شواهد آغاز شده است".</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/18436" target="_blank">📅 14:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18435">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">‍
💢
وزارت خارجه: حملات جنایتکارانه آمریکا نقض فاحش بندهای یک و پنج یادداشت تفاهم است
🔹
وزارت امور خارجه حملات تجاوزکارانه ارتش تروریستی آمریکا طی بامداد پنج‌شنبه ۱۸ خردادماه به چندین نقطه در استان‌های ساحلی جنوب و نیز دو پل در استان‌های شرقی در مسیر ریلی…</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/18435" target="_blank">📅 14:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18434">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">سخنگوی دولت ایران، فاطمه مهاجرانی:  "ما در حال پیگیری قانونی شکایت مربوط به ترور رهبر سابق هستیم که با جمع‌آوری شواهد آغاز شده است".</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/18434" target="_blank">📅 14:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18433">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">مانور کلاهک موشک ایرانی که دیشب به پایگاه آمریکا در کرانه های جنوبی خلیج فارس اصابت کرد.</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/18433" target="_blank">📅 14:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18432">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e86d2fb7c7.mov?token=TCbF1RbIMZ8aTMmy_Yp8ECh37KPOuoccc3bQvoDI0Ygp9J7WF_VqrRK97xb-4v1dQXMFeD9cBgKyhS5gHS9m1rxfOUxYrJdnEUpRfteKV-bsKNncZ_g_OxZj7-iSzjn3E9KeKmcZKZESnTuj1FepzvcJxyjJ31QQ4fkSHDHl2l_zqMHHTq9I5-ChfICcCUmiSFas84DKDvfwTUSrdiEZ0vt3-fwaFr3l6uQmwM8uaOHnTPCy9Xnydmvh_hg0-xgzdFR6vJexVTnmPYIRcxh0u98o3T2lyXYAKGJHKVlXHYVXrJIwLNxwYfBCyPS58Kg6qgcF4ZacUQJdjgShe08o1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e86d2fb7c7.mov?token=TCbF1RbIMZ8aTMmy_Yp8ECh37KPOuoccc3bQvoDI0Ygp9J7WF_VqrRK97xb-4v1dQXMFeD9cBgKyhS5gHS9m1rxfOUxYrJdnEUpRfteKV-bsKNncZ_g_OxZj7-iSzjn3E9KeKmcZKZESnTuj1FepzvcJxyjJ31QQ4fkSHDHl2l_zqMHHTq9I5-ChfICcCUmiSFas84DKDvfwTUSrdiEZ0vt3-fwaFr3l6uQmwM8uaOHnTPCy9Xnydmvh_hg0-xgzdFR6vJexVTnmPYIRcxh0u98o3T2lyXYAKGJHKVlXHYVXrJIwLNxwYfBCyPS58Kg6qgcF4ZacUQJdjgShe08o1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مانور کلاهک موشک ایرانی که دیشب به پایگاه آمریکا در کرانه های جنوبی خلیج فارس اصابت کرد.</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/18432" target="_blank">📅 13:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18431">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UacJ-ei8sW86Kr0rK_P3L_OcxDfeKNOgjKQwVZlrII3XD2K04tCMZM3vMblF4CiG-v0VSddaI1czeR6-xVSvQsNlTCgSHgriiY-UbSmUa3wu6Hc6eAZTmNchHkZwTlCBqVKk-URk3nvpJUzVDu4dGFgNoE26r7Ij7DD6bj0Ny-xf5cFAdHEhYsgbqhbDtl1cmLakcMleqgjEjXtEPC15o6WiiwUA6WjqhcOok_FD_3JCIPMiwFdBCHU2cHHejlfpHAzAy5PS-Kv-uuCSuryfbVaGVsiyEc8skNmwxOrU7jQ-juUxvYi5XrqbpVOu_MyqWPYXZon754iRbiE7JxMIBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با اینکه ترامپ برای عزیمت به ترکیه آماده می‌شد، مارکو روبیو، وزیر امور خارجه، و پیتر هیگست، وزیر دفاع، در دفتر بیضی‌شکل کاخ سفید، او را در جریان گزارش‌هایی قرار دادند مبنی بر اینکه ایران موشک‌های کروز و پهپادها را به سمت کشتی‌های تجاری در حال عبور از تنگه هرمز شلیک کرده و به سه فروند از این کشتی‌ها خسارت وارد کرده است.
ترامپ پرسید که آیا تهران هنوز به دستیابی به یک توافق نهایی متعهد است یا خیر، و پس از مشورت با مشاوران ارشد امنیت ملی خود، به این نتیجه رسید که اینطور نیست.
این جلسه، نقطه‌ی عطفی بود که باعث شد او طرح آتش‌بس را کنار بگذارد و مجوز حملات نظامی جدید و اعمال فشار اقتصادی مجدد بر ایران را صادر کند.
منبع: WSJ</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/18431" target="_blank">📅 13:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18430">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">انفجار در بوشهر</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/18430" target="_blank">📅 13:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18429">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y-57W2mDTlFAeBEA0GOZT1FQjkfgjm8bpHckbCOGuG45utX_H_7QZ8lrvtR7Y6ZiARDwiSDK9Chb3-VsjGg3D1AfxDrQWvILhiY7OS6JXjjDzljWH2Wh6GcgvpknSoJb8FpP_UavhrdCleIpdUIiaC3v4jDBL_F8VeIBbsEdVtM6IKrKaQu2ENm669Zgof5RfeE6greK5gujHGpr3skaWfhDuuYjY8rmaSKszPbzQ_BWlcmg8J0Y7cdEoAlsA1sWZjuvmTHTNpTFdZPNHYbNATaIyFuKZTZjsCKnOHCtg_ncbaOS23zi98N4TINeUSWihyr0dumtyriadMT7qwLqlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسکو با فروپاشی بنزین روبرو شده است.  پهپادهای اوکراینی عملیات بزرگترین پالایشگاه مسکو را مختل کرده‌اند  و این واحد تا سال ۲۰۲۷ تعطیل شده است، - رویترز</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/18429" target="_blank">📅 13:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18428">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">عمدا جاهایی را دارند میزنند که در شکستن محاصره نقش داشتند و کریدورهای جایگزین برای ایران حساب می شدند.</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/18428" target="_blank">📅 12:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18427">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
🇮🇶
🇮🇷
✈
هواپیمای حامل پیکر آیت‌الله سید علی خامنه‌ای و خانواده به فرودگاه مشهد رسید.
📮
@IRKhbarFori</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/18427" target="_blank">📅 11:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18426">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبارفوری جنگ امریکا فوری/ خبرفوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3075b8e37.mp4?token=FYWi8z-Nw_LTRoSyQFvRUiHbZm6W_1WIY7Xtrp8SVJZWOYd13bm6GLCcqBArNbpaflXY42ffcgGgUQKVUono-3wjRnNREUxdoJWN2hGg-to7nCF9iBUmDxfgrCDpMqmKo0Uv4GwfTPFUVc43SRygNXt_oXi3dKvA41-aE8XCZwWJmIyU08V-RFX_aKBMuAv3tIWhBXxpPx3JuQJqE60Vq4N7mVemh32ZBGauHB7GxXqtvBebVCt5iUYyFnPL7RlRi2VLJ-yZxZFAw--JS3XlsjTXGI7mC2Y8Io9KQuwfKy2Ko6NBAKS1efLzy7ibLBD4w0o6G76EhpwiodRGFcm8-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3075b8e37.mp4?token=FYWi8z-Nw_LTRoSyQFvRUiHbZm6W_1WIY7Xtrp8SVJZWOYd13bm6GLCcqBArNbpaflXY42ffcgGgUQKVUono-3wjRnNREUxdoJWN2hGg-to7nCF9iBUmDxfgrCDpMqmKo0Uv4GwfTPFUVc43SRygNXt_oXi3dKvA41-aE8XCZwWJmIyU08V-RFX_aKBMuAv3tIWhBXxpPx3JuQJqE60Vq4N7mVemh32ZBGauHB7GxXqtvBebVCt5iUYyFnPL7RlRi2VLJ-yZxZFAw--JS3XlsjTXGI7mC2Y8Io9KQuwfKy2Ko6NBAKS1efLzy7ibLBD4w0o6G76EhpwiodRGFcm8-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🇮🇶
🇮🇷
✈
هواپیمای حامل پیکر آیت‌الله سید علی خامنه‌ای و خانواده به فرودگاه مشهد رسید.
📮
@IRKhbarFori</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/18426" target="_blank">📅 11:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18425">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبارفوری جنگ امریکا فوری/ خبرفوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25cd71dba4.mp4?token=Li0f-VaJVmlfCaM7Y1hl-_Y0ZnFr0bAHwhLFlx1aVti2omgLnnyzF3GgaUUNlBkwMtB6plkR88w2NesasVCmyGC6jlLg6Dt5hvnymP8LGjulHMd68rwoWaZzLoI5gCUeG825GufNgwrj3CKSG_yIXm8JaK5VlKfZGxCjfUZB4VkyZ7jEKjaIRlxQDOrAK56Ess931zPniPOH4oGTBxxs4_mnTrgmTWrvblkeMjalG99CHE4TmzhtjwGjTJJyNGQ0GS2QJxxaCm8KLhU-BISDrm7zuwatV8D2JcqqVaU3H_SpvjgqqBuQhNJrOxIGk_6JN26dOIQCO9-Btnsutdi7dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25cd71dba4.mp4?token=Li0f-VaJVmlfCaM7Y1hl-_Y0ZnFr0bAHwhLFlx1aVti2omgLnnyzF3GgaUUNlBkwMtB6plkR88w2NesasVCmyGC6jlLg6Dt5hvnymP8LGjulHMd68rwoWaZzLoI5gCUeG825GufNgwrj3CKSG_yIXm8JaK5VlKfZGxCjfUZB4VkyZ7jEKjaIRlxQDOrAK56Ess931zPniPOH4oGTBxxs4_mnTrgmTWrvblkeMjalG99CHE4TmzhtjwGjTJJyNGQ0GS2QJxxaCm8KLhU-BISDrm7zuwatV8D2JcqqVaU3H_SpvjgqqBuQhNJrOxIGk_6JN26dOIQCO9-Btnsutdi7dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🇮🇶
🇮🇷
🎬
هم‌اکنون هواپیمای حامل پیکر آیت‌الله خامنه‌ای و خانواده، فرودگاه نجف را به مقصد مشهد ترک کرد.
📮
@IRKhbarFori</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/18425" target="_blank">📅 11:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18424">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">چرا درگیری بعدی ایران و آمریکا احتمالاً جهش تاریخی نفت را تکرار نمی‌کند؟
درگیری نظامی میان ایران و آمریکا همواره یکی از بزرگ‌ترین ریسک‌های ژئوپلیتیکی بازار انرژی بوده است. هرگونه تهدید علیه تنگه هرمز، مسیر عبور بخش قابل توجهی از صادرات نفت خلیج فارس، در گذشته می‌توانست باعث جهش شدید قیمت نفت شود؛ زیرا بازار به اختلال ناگهانی در عرضه واکنش نشان می‌داد. اما شرایط بازار انرژی امروز نسبت به گذشته تغییرات مهمی کرده است و درگیری احتمالی آینده لزوماً به معنای تکرار شوک‌های نفتی تاریخی نخواهد بود.
یکی از مهم‌ترین عوامل، ایجاد مسیرهای جایگزین برای انتقال نفت در خارج از تنگه هرمز است. کشورهای تولیدکننده منطقه، به‌ویژه عربستان سعودی، امارات و عراق، در ماههای اخیر سرمایه‌گذاری‌هایی برای توسعه خطوط لوله، پایانه‌های صادراتی جایگزین و افزایش ظرفیت انتقال خارج از این آبراه انجام داده‌اند. این زیرساخت‌ها به بازار اجازه می‌دهد بخشی از نفت منطقه حتی در صورت اختلال در هرمز همچنان به بازارهای جهانی برسد. بنابراین، حساسیت بازار نسبت به تهدید بسته شدن کامل تنگه هرمز نسبت به گذشته کاهش یافته است.
عامل دوم، افزایش ظرفیت عرضه و انعطاف‌پذیری بیشتر بازار نفت است. تولیدکنندگان عضو سازمان کشورهای صادرکننده نفت (OPEC) و متحدان آن در قالب ائتلاف اوپک پلاس، در مقاطع مختلف توانسته‌اند با تغییر سیاست تولید، بخشی از شوک‌های عرضه را مدیریت کنند که یک نمونه جاری آن را با 3 بار افزایش تولید اخیر اوپک که آخرینش هفته پیش تصویب شد مشاهده می کنید. همچنین رشد تولید نفت شل در آمریکا باعث شده بازار جهانی نسبت به دهه‌های گذشته تنها به خاورمیانه وابسته نباشد.
از سوی دیگر، سمت تقاضا نیز تغییر کرده است. رشد خودروهای برقی، افزایش بهره‌وری انرژی، سیاست‌های کاهش مصرف سوخت‌های فسیلی و تغییر الگوی رشد اقتصادی چین باعث شده رشد تقاضای نفت کندتر شود. در نتیجه، هرگونه اختلال کوتاه‌مدت در عرضه ممکن است بیشتر به یک شوک موقت قیمتی تبدیل شود تا آغاز یک روند انفجاری پایدار.
موضوع مهم دیگر، پدیده «نابودی تقاضا» است. اگر قیمت نفت به‌سرعت افزایش یابد، مصرف‌کنندگان و صنایع واکنش نشان می‌دهند: استفاده از انرژی‌های جایگزین افزایش می‌یابد، فعالیت‌های انرژی‌بر کاهش پیدا می‌کند و اقتصاد جهانی با فشار رکودی مواجه می‌شود. تجربه بحران‌های قبلی نشان داده است که قیمت‌های بسیار بالا خودشان عاملی برای کاهش مصرف هستند.
البته این به معنای بی‌اهمیت شدن ریسک افزایش بهای نفت نیست. یک درگیری گسترده که تولید نفت ایران و دیگر کشورهای نفتی یا زیرساخت‌های اصلی منطقه را هدف قرار دهد، همچنان می‌تواند باعث جهش کوتاه‌مدت قیمت شود. بازارها به اخبار جنگی با سرعت واکنش نشان می‌دهند و عامل روانی می‌تواند قیمت‌ها را برای مدتی بالا ببرد.
اما تفاوت امروز با گذشته این است که بازار نفت ابزارهای بیشتری برای جذب شوک دارد. مسیرهای جایگزین صادرات، ظرفیت‌های ذخیره‌سازی، تولیدکنندگان جدید و تغییر رفتار مصرف‌کنندگان باعث شده‌اند احتمال تکرار جهش‌های تاریخی نفت در اثر یک درگیری منطقه‌ای کاهش یابد. در سناریوی درگیری بعدی ایران و آمریکا، احتمالاً واکنش بازار بیشتر یک جهش سریع و محدود خواهد بود، نه یک بحران انرژی مشابه دهه‌های گذشته.</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/18424" target="_blank">📅 11:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18423">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ارتش ایران:  «ما با استفاده از پهپادها، سامانه‌های پدافند هوایی پاتریوت در کویت، یک مرکز هشدار اولیه در قطر و تاسیسات ذخیره‌سازی سوخت ارتش آمریکا در بحرین را هدف قرار دادیم.»</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/18423" target="_blank">📅 11:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18422">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
حملات پهپادی ارتش به پایگاه‌های آمریکا در منطقه
🔺
روابط‌عمومی ارتش:  در پی تجاوز ارتش تروریستی آمریکایی مناطقی از کشور و یگان‌های ارتش و در پاسخ به آن جنایت،  ساعتی قبل و در ادامۀ حملات ارتش به پایگاه‌های آمریکا در منطقه، سامانۀ پاتریوت در کویت، آنتن ماهواره‌ای…</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/18422" target="_blank">📅 11:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18421">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">به گزارش اکسیوس، پهپادهای ایرانی دو کشتی تجاری را در تنگه هرمز هدف قرار داده‌اند.</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/18421" target="_blank">📅 11:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18420">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">شبه نظامیان آزادی بلوچ یک حمله با بمب دست‌ساز (IED) و سپس یک کمین سنگین را علیه کاروانی متشکل از سه خودروی نیروهای امنیتی پاکستان در منطقه سچی واشوک، بلوچستان، انجام دادند.  خسارات سنگین جانی گزارش شده است.</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/18420" target="_blank">📅 10:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18419">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">مقر تیپ 110 سلمان فارسی نیروی زمینی سپاه در زاهدان بمباران شده است.</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/18419" target="_blank">📅 10:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18418">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a32wJJLI21ucx19hCt475jAAGTsof9RPVUoMcqke0GdTAEu4FK1bGpvZMUCfW_-4cENFddNw7WIDtSymsa4vQwZWrtowejKL4FCcUMqNZInUyOSdGjevIL3P-275-SBYFAsoszCnZejz0nNNA3IR-n0b-Ifjn7RTD_Ghna4vLu_wj5XUBiIXJ8DTdTxuy283YRxpgTzBJqa1DY4yTP0dDRCMh6MO9-cY4ZmmchSVNBQzDoztyqMXdPDTMH3aoj2wGO9yeUpZscw1U9qWhlLAwS4LNiJY0bddbVlbJ-LxYG0GyXc29yeI_o0YAXXI7T1X2wvZWcH_VdSsZ2OKcbYDog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز در سطح پایینی قرار دارد و ریسک پذیری پیش بینی می شود.</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/18418" target="_blank">📅 10:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18417">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/18417" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 4
پنج شنبه 9 جولای 2026</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/18417" target="_blank">📅 10:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18416">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">بیانیه سپاه پاسداران انقلاب اسلامی   بسم الله قاصم الجبارین  قَاتِلُوهُمْ يُعَذِّبْهُمُ اللَّهُ بِأَيْدِيكُمْ وَيُخْزِهِمْ وَيَنْصُرْكُمْ عَلَيْهِمْ وَيَشْفِ صُدُورَ قَوْمٍ مُؤْمِنِينَ  ملت شریف ایران، ملت کریم و مجاهد عراق؛ آفرین بر شما مردمان مومن و بصیر…</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/18416" target="_blank">📅 09:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18415">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">کاخ سفید برای یک درگیری بالقوه طولانی‌مدت با ایران بر سر تنگه هرمز آماده می‌شود.
مسئولان آمریکایی می‌گویند مدت زمان این درگیری به اقدامات بعدی تهران بستگی دارد.</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/18415" target="_blank">📅 08:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18414">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BTk2CitDFJQD139XxXQAxoPzhtEiRk2WYj_w1AuiCmQRpjOAlLsIHuCC9pPO81x4URMnfGLTEohJ5c9b3NYVnUoMARugyEmiIfP8ex6gQ8-j3ei_OV4p8aFCAY4XB1eibLou4e35sRkRCX1Rfj7t8g5_MnoGpEi4E5HRnK33qfAiD1Moxv4f-a-fWUFFaiifAdbOddIdcOBghLjFr9MRF6ZR0-bByX5rFpqYtqjsxZz-Qx4aav12FYWZ0JU0EUUB9hgQVDxmaTUFXv80YWrPtx8Xta2GYx8o9qoPnajNV9_ibqNKdmCQhwluAOjxCOdTfB1i2LgViAybysNQxcQUQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمدا جاهایی را دارند میزنند که در شکستن محاصره نقش داشتند و کریدورهای جایگزین برای ایران حساب می شدند.</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/18414" target="_blank">📅 08:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18413">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">راه آهن جمهوری اسلامی ایران:   به دنبال حمله جنایتکارانه دشمن آمریکایی بامداد امروز به یکی از ‌نقاط مسیر ریلی تهران-مشهد، حرکت قطارهای مسافری در این مسیر با وقفه مواجه شده است.  برنامه ریزی لازم برای جابجایی مسافران محترم قطارهای متوقف شده در این مسیر، از…</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/18413" target="_blank">📅 08:39 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18412">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">راه آهن جمهوری اسلامی ایران:
به دنبال حمله جنایتکارانه دشمن آمریکایی بامداد امروز
به یکی از ‌نقاط مسیر ریلی تهران-مشهد، حرکت قطارهای مسافری در این مسیر با وقفه مواجه شده است.
برنامه ریزی لازم برای جابجایی مسافران محترم قطارهای متوقف شده در این مسیر، از طریق ناوگان مسافری جاده ای به مشهد مقدس انجام شده است.</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/18412" target="_blank">📅 08:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18411">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">توییت محمدسامثینگ قالیباف</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/18411" target="_blank">📅 08:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18410">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e9MGDup4oNST6PiBZ5ggT3AHPH3zAIhvaW7TM1qdyZJrv-6Kt7JVEP-hamizIdJrvjan1PoICfJVFDaEhPP-rI-GU7sQjcXZAjkzi6Iraddmf_smRSF3WNzHyEz8f6RZTnl9kPbcby5oRNBw_1fZJpIP_qxPls-xcftcpl2sKftwCIYu16oBeGfGK0BL-wHIhamJuAKeZACRSq_xsPiqqQ2U2iKykkw4nkpSoremTDR07kVKqufaRBt2K2TI_M7YA2G7wGSNvebh6CBfuDeddCU6VujGYGYkhwvDen6_aOBrFn_KXaPXGIJHP0HlTgm7tI1fDhuBKZv3svNiq2qLkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت محمدسامثینگ قالیباف</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/18410" target="_blank">📅 08:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18409">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ایران به اهداف دشمن با نسبتی حداقل دو به یک حمله خواهد کرد -   تلویزیون خبرگزاری ایران، با استناد به یک منبع امنیتی آگاه.</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/18409" target="_blank">📅 08:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18408">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">بیانیه سپاه پاسداران انقلاب اسلامی
بسم الله قاصم الجبارین
قَاتِلُوهُمْ يُعَذِّبْهُمُ اللَّهُ بِأَيْدِيكُمْ وَيُخْزِهِمْ وَيَنْصُرْكُمْ عَلَيْهِمْ وَيَشْفِ صُدُورَ قَوْمٍ مُؤْمِنِينَ
ملت شریف ایران، ملت کریم و مجاهد عراق؛
آفرین بر شما مردمان مومن و بصیر و وفادار که با موقع‌شناسی و تشییع بی‌نظیر در تاریخ جهان قدر و منزلت ولایت الهی و عشق عمیق متقابل مردم و والی اسلامی با مرام امیرالمومنین (ع) را به رخ جهان کشاندید و با شعارهایتان یادآور شدید که هزینه تعدی به مرجعیت و ولایت فقیه مسلمانان بسیار سنگین خواهد بود.
هرچند این تشییع باشکوه به ویژه ۲۳ ساعت تشییع عاشقانه در گرمای شدید سرزمین عراق حبیب، مستکبران کاخ‌نشین را وحشت‌زده و آنها را به واکنش عجولانه به این قدرت نمایی مردم واداشت و آمریکای عهد‌شکن با زیر پا گذاشتن همه تعهدات بار دیگر نقاط متعددی از استان‌های ساحلی جنوب ایران و در اقدامی ضد مردمی دو پل در استان‌های شرقی به سوی مشهد مقدس را مورد تجاوز قرار داد تا اخبار این حماسه بی‌نظیر را تحت شعاع قرار دهد و این رویداد الهام بخش را از نظر مردم جهان پنهان دارد، غافل از اینکه این جنایات مردم جهان را بیدارتر و آنها را برای نقش آفرینی در مبارزه‌ با شیطان بزرگ مصمم‌تر خواهد کرد.
رزمندگان اسلام تجاوزهای ارتش کودک‌کش آمریکا را بی‌پاسخ نخواهند گذاشت.
در اولین مرحله از پاسخ تنبیهی علیه پیمان‌شکنان آمریکایی، رزمندگان نیروهای دریایی و هوافضای سپاه طی عملیات مشترک موشکی و پهپادی، ساعتی پس از حملات دشمن و نقاط مختلف کشور، زیرساخت‌ها و تاسیسات مهم دو پایگاه‌های استعماری اشغالگران آمریکایی در عریفجان و علی السالم کویت و جفیر و شیخ عیسی در بحرین را در هم کوبیدند.
سپاه پاسداران انقلاب اسلامی به ارتش کودک‌کش آمریکا اخطار می‌کند که در صورت تکرار تجاوز پاسخ‌های کوبنده ما به سایر پایگاه‌های آمریکایی در منطقه توسعه خواهد یافت.</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/18408" target="_blank">📅 08:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18406">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">به نظر شما ترامپ با این سه سگ (اردوغان، فیدان، کالین) چه صحبتی می تواند داشته باشد آن هم وقتی که جولانی هم دارد به اینها می پیوندد؟!</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/18406" target="_blank">📅 02:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18405">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UK8XSFdYVhORaiR7rwHL2wLD6Q8qpFndcrLPs-5I_Awx5FITRYx1ncB5GtlcMekghImKJ2Y5sfWpWJAHpcNupg-N9fStn--DMPNfqdcwSgoYn5Lhs352d7ZIce6tMgqSKa50EYYZpQCKRPndp2MK-ql9zSksTLJzAg4yLZOyezCToQUJrxe0Z_4hRiDICmJ4t9e-cVuztFKre2nlwvajKH1JgpxqR6WiQEE7X0S9fi4_VpaNEs1C-JInWeesE6ynH-n423k_W83Obfmz7_ENAhxwI3EmWmaqvgk5mdje6fWvtZgoYm_DW2tMfHYmCdX3bKD1YqwtgIeA08yZZBI1Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در حال انتشار زنده ویدئوهایی از حملات آمریکا به ایران در امشب است</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/18405" target="_blank">📅 01:39 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18404">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">مقر تیپ 110 سلمان فارسی نیروی زمینی سپاه در زاهدان بمباران شده است.</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/18404" target="_blank">📅 00:50 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18403">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">زاهدان</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/18403" target="_blank">📅 00:50 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18402">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ابوموسی</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/18402" target="_blank">📅 00:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18401">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">تماس شبکه خبر با اژدهای بندر!</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/18401" target="_blank">📅 00:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18400">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jM0MvEhzQ7gdiRNbBEdCP2yKMnj4sZVeEH9Wpe_mfBMa7ToIt1A1bJU6ynuqdFhLkwlolpRpr87tFYheJJVLSgjVtPhcKcPCfI7MpZ30B8uyj0TMQrvVCd6O_RsMsILGDeGbZhEpf2eWIHhLNesbGu4-3kyHzDK8IaUHnsP_fGnlnBH4pRRZo1FRoT9Pe3MvPg6sJAhLvLrSS_iC1zAp8riSDer-eHDf20uGx5mr3S9k3sAA7F3rVD0awsMI3J461ueFHDjfJxaAxq5GSVHdKye9V9CSbNirtFMGaAr93B1oXgXpO1jLV3eYIvWh9A3dj8c8Sl5g96yTjeytfhFoAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/18400" target="_blank">📅 00:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18399">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">گفته می شود تا 200 هدف امشب مورد اصابت موشک ها و بمب های آمریکایی ها قرار گرفته است.</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/18399" target="_blank">📅 00:28 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18398">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">انتشار اخباری از آماده شدن پرتابگرهای موشکی سپاه</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/18398" target="_blank">📅 00:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18397">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">خارک، قشم</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/18397" target="_blank">📅 00:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18396">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">تسنیم:
براساس برخی اخبار غیررسمی، پایگاه امام علی نیروی دریایی سپاه در چابهار توسط جنگنده‌های آمریکایی مورد هدف قرار گرفته</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/18396" target="_blank">📅 00:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18395">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">عربستان سعودی در حال پیشبرد طرحی برای کنار زدن اسرائیل از کریدور اقتصادی هند-خاورمیانه-اروپا، معروف به پروژه «راه‌آهن صلح»، با تغییر مسیر این کریدور از طریق سوریه به جای اسرائیل است.
دو منبع به نقل از جروزالم پست</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/18395" target="_blank">📅 00:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18394">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">کی حضرات می خواهند بفهمند که ادامه این مسیر احمقانه یعنی نابودی زیرساخت های باقیمانده کشور و سپس ایجاد یک دولت شکست خورده و نهایتاً تجزیه ایران؟!</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/18394" target="_blank">📅 00:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18393">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">کی حضرات می خواهند بفهمند که ادامه این مسیر احمقانه یعنی نابودی زیرساخت های باقیمانده کشور و سپس ایجاد یک دولت شکست خورده و نهایتاً تجزیه ایران؟!</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/18393" target="_blank">📅 00:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18392">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dFnKglFkmreLtHJktNlcBrBhOlc5r5yMRN1Qpgv5B364-M8fyT6u7GTz-m-LsdMyrza5h4L9UTC4lf-vHk6ADFw-FnFKAj4hcTu63KKeKEeMA3LJ0408aW2ucFluZs8lZQXs4aQCxbJGvRDfa4MMB_kj-ZH23umaFKACs_G51lqWQoGzgZwMOx-5WWF4gOseJNjncxABIv2N1c4f_nHUrSPSE1zFBHuHhGyp1Fz-GaqqDmWAtqShIO-6YWY5aI5m2dguTKfd7GDbmea34stk-4lamF_QXia6R2QLiJjlcqC2sUuVI811s_SCjXeWnkegXe5x2RcpeCp_UYb0NdFR1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروگاه برق چابهار ه زده شد و برق قسمتهایی از شهر قطع شده.</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/18392" target="_blank">📅 00:05 · 18 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
