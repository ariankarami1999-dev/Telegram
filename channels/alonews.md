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
<img src="https://cdn4.telesco.pe/file/COUeBOHS89lnRK1xf9cHnOL__ll_W_sm3n1t06vwbpUDJr3Mylx_AhC9GzRdIKHozcyjGWUOZShI_wL7wFUNr4wzB1dIjZTmuwLa1Fs1A6hah6wBTLbjkm3gB5WzbNOs52utfIyV1veXQdzvWV8DGuu9ArkPDFqNjxR4k_GOnGaNqiHfN9PA2Bd3xW7BlRhNRHGaNRPQvI0E5mT0z7zmGTOsdCh4bF_LvQ4Ui7l1689Gzyz7Wvjo_BHzG3jL8IT8Mm5tloC5Ts9Rn2Sw_4aeQfHP581eBDsatVFPLiKwR0enivG_IYzYYlz-I0VcRvD_-bqwTdrJAyh7hW0OGIpnLA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 932K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-02 18:50:40</div>
<hr>

<div class="tg-post" id="msg-137252">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
رویترز : پاکستان و ایران دارن راهی پیدا می‌کنن که دوباره مذاکرات با آمریکا شروع بشه؛
🔴
این روند هم با ابتکار چین داره پیش میره
✅
@AloNews</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/alonews/137252" target="_blank">📅 18:46 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137251">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cf8ecb014.mp4?token=sCLBNv-yL2zWdQr5nc9OjrChOplyInyD__JUxnkF6hU9mnFSg20SW4qpEzC3bo4hLUKIZ1C3iBSdZxfjhk6JMGoH1leRacCwCrsRKkfuBFy_E44GRu4lA8sj3XoeWsAy-E9uGS7x44BFoZlhUnb1HT1UUJOhzUDqeQcpPWEgTbSVGtCTT-08-Tcrfzgz9Uc0kAUyMk1vc5UuXD7FKj9t1OnJmFWXohI17_teapQk4T_CorqOPwYf8oaXPlLTZudF2XU6XAUhQQVdCojMqxk8AKaAChXU0G-5EeVm2IeQZFSihZRg2I0WX361XFY1a2sKEBN3K9tRXvuG15BC37iwGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cf8ecb014.mp4?token=sCLBNv-yL2zWdQr5nc9OjrChOplyInyD__JUxnkF6hU9mnFSg20SW4qpEzC3bo4hLUKIZ1C3iBSdZxfjhk6JMGoH1leRacCwCrsRKkfuBFy_E44GRu4lA8sj3XoeWsAy-E9uGS7x44BFoZlhUnb1HT1UUJOhzUDqeQcpPWEgTbSVGtCTT-08-Tcrfzgz9Uc0kAUyMk1vc5UuXD7FKj9t1OnJmFWXohI17_teapQk4T_CorqOPwYf8oaXPlLTZudF2XU6XAUhQQVdCojMqxk8AKaAChXU0G-5EeVm2IeQZFSihZRg2I0WX361XFY1a2sKEBN3K9tRXvuG15BC37iwGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کپلر: عبورهای تأییدشده از تنگه هرمز به شش مورد کاهش یافت که نسبت به روز قبل ۶۰ درصد افت نشان می‌دهد
🔴
به‌جز یک کشتی، همه شناورها از مسیر یک‌جانبه تعیین‌شده از سوی ایران استفاده کردند.
🔴
در مقابل، تردد در باب‌المندب افزایش یافت و به ۴۹ عبور تأییدشده رسید.
🔴
داده‌ها نشان می‌دهد  بازگشت به تردد دریایی در منطقه به‌صورت محتاطانه و گزینشی در حال انجام است و شرکت‌ها همچنان در حال ارزیابی شرایط امنیتی هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/alonews/137251" target="_blank">📅 18:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137250">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
حملات اسرائیل به خان یونس در جنوب غزه
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/137250" target="_blank">📅 18:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137247">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mmjPIk1UwUeHY3ci_2Yosc5GPvJrrSbsNcjMwSUr387nbaD9ovdJwpwlLTsg-3UMKtbzuqp5aDMlK9z7J4-6eBClJ2jfg_GB9Qjzp4SqolgwLKWCd-Weu8jZC0KtJKsyEROYSsklEi469HWHg-nKWsy6BcHXlcyFBA_61hqTVyDfSkpPocwGI0DellMLpSan8qPBC3woQb8nSXI_qSOoRqQ8L56yZIzoPI1qBcYLPG3yqDBV9UxzaDX__KjnQkUYQRWJc62MqniH9B3zY-S4uiU3c8weRigrda0aBYb5iHhxvzKEd5dsrK23O_9GT0rA_K349f3XFCG-DahuB6assA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CEZtWYz6rInDufSMJlqHEm0dPMHS7mNYhH246sdZSSZPY35OHRhGL3FZwaSqSwAhUs2Hx8O3V1t-Mbk5E3KklxUc1NdelU9bENtvzIMQu4G8imTz9vniS5boEhbygNTIitOaNjZtD2MkpRdRBRvAl3IkiflM4I4qhxAcFECBBwMEN5c8c94pxSTah69uuQCzmfBjpv4ArJMHLdGXncOwi1nQaJbxChr9Na77GO_js379jTIrnvTyemvm2LIPZPnZQTDjxIccWnOO8In8DIC4oJO-jGgaX-GlvufqZ3TnNF9OJXoWFfqhnP7dd4Z9i9OpATrPl1U_ibIk6uLceY1l4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VL0Gi7Pdbd-yUA2cU4-lWQIsoP6sRLXL7SlFFKlNcXywIgHMVAkX24LV49ujoknZD4JftSsjWn4tq2wzoJOvucEF8JcMN5v1pb2cl-JMyD_VnyoSq48HWWoAPkl4Zrb8Kn5Cw8osjk82F--hTpZWAxKAN_sJpTiF2scGWVwvZaTy16Au2TtM77k9JReFRM4Nn_Nuu5Advlpv_z0me2veOVWj0lSqW0lyHV89LBS8iaxh_M0vY4P0vUDuk2Mu7D39KoE3uttkrh0MyCx8r0QTdJGPDM3Cl_KilUnoQM-_3oAVcs10AWVV1PLsRxwtuOpZMkSBeL-uJx8f0-SzC5_TWg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
سنتکام منتشر کرد :  تفنگداران دریایی آمریکا یک سامانه موشکی هیمارس را در جریان یک تمرین آموزشی در خاورمیانه سوار بر هواپیمای ترابری KC-130J سوپر هرکولس کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/alonews/137247" target="_blank">📅 18:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137246">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3927f843ee.mp4?token=lu4eSGaKYSPhmOyBAWYx5N11uxlKLlmz4zTxgHx1pW9ulml6J35VU74lDSZ76iiBgDZcTBmmylKI4ULKUOKzLWGac1uSAw3iuQ5RAToelpwV7OYE6ZGuPV7EVCYRbT4a6yAc6zrOmzIeBZJ6nA2fdjn44NFkMTNBGqqjgCQ1Ez9n0wrESg_JwcfKnKjHzjrHOFDH19Ahu2uWQFSnIzeYI6egxFEuA1Tf9NKQQPfEFlMs-2pfe3QNdxO1mmZPmKAJsXgqh2tfqbXh57utFwIVhmUM1aLq0_6t8OuVC6SD_XrQDO7Ef2-vWib4uVoX65rgmtZyBKv1grQNN5YOYDrs3ii0izKIoYyIh83xm48jU6iYf8TSILF8baueyOktSAMkYhmpc-GEyBqWzsObHgy0H1knIiva5EZy56VOgjr-ktKljiNYtkDTha7HGU2EbtScQRQ0Lu2lMGE2aK5GQLJ8E0Ao0Ad-fYtVqwPIcKEFyKGfh1R-4Ph9NaIdgJ0g1qfWtA-z9iuwMtziGbSuhY0jMJh8CyOv5fqcG9PTk-D_rOg6IHwl2JNep_pvSkhfndVFayUymO4lmIGVMzOgKTDWt_X_i7ObxwIJRmUMUiIkbvYRglmPsv_WgcPe2sIkpVcHmfesQe67yKX7dPKIIyFfSGHz4a6RPdnZThhAp1lJ3mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3927f843ee.mp4?token=lu4eSGaKYSPhmOyBAWYx5N11uxlKLlmz4zTxgHx1pW9ulml6J35VU74lDSZ76iiBgDZcTBmmylKI4ULKUOKzLWGac1uSAw3iuQ5RAToelpwV7OYE6ZGuPV7EVCYRbT4a6yAc6zrOmzIeBZJ6nA2fdjn44NFkMTNBGqqjgCQ1Ez9n0wrESg_JwcfKnKjHzjrHOFDH19Ahu2uWQFSnIzeYI6egxFEuA1Tf9NKQQPfEFlMs-2pfe3QNdxO1mmZPmKAJsXgqh2tfqbXh57utFwIVhmUM1aLq0_6t8OuVC6SD_XrQDO7Ef2-vWib4uVoX65rgmtZyBKv1grQNN5YOYDrs3ii0izKIoYyIh83xm48jU6iYf8TSILF8baueyOktSAMkYhmpc-GEyBqWzsObHgy0H1knIiva5EZy56VOgjr-ktKljiNYtkDTha7HGU2EbtScQRQ0Lu2lMGE2aK5GQLJ8E0Ao0Ad-fYtVqwPIcKEFyKGfh1R-4Ph9NaIdgJ0g1qfWtA-z9iuwMtziGbSuhY0jMJh8CyOv5fqcG9PTk-D_rOg6IHwl2JNep_pvSkhfndVFayUymO4lmIGVMzOgKTDWt_X_i7ObxwIJRmUMUiIkbvYRglmPsv_WgcPe2sIkpVcHmfesQe67yKX7dPKIIyFfSGHz4a6RPdnZThhAp1lJ3mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کاژا کالاس، رئیس سیاست خارجی اتحادیه اروپا: ما با آمریکا توافقی داشتیم و به آن توافق پایبند بودیم، به تعهدات خود عمل کردیم.
🔴
منظورم این است که مذاکرات آسان نبودند. برای شرکت‌های ما مهم است که پیش‌بینی‌پذیری وجود داشته باشد.
🔴
به همین دلیل است که شرکت‌ها می‌گفتند: «به نتیجه برسید، به یک توافق مذاکره‌شده برسید،» زیرا پیش‌بینی‌پذیری بهتر از این است که نتوانید پیش‌بینی کنید چه اتفاقی خواهد افتاد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/137246" target="_blank">📅 18:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137245">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
عباس عراقچی وزیر امور خارجه: رایزنی ها با روسیه و چین مستمر و مستمر است و ما به طور مرتب با دوستان خود در چین و روسیه در هر فرصتی مشورت می کنیم.
🔴
طبیعتاً با پاکستان به عنوان میانجی در مورد ابتکارات و پیشنهادات آنها گفتگوهایی صورت گرفته است. مشکل فقدان میانجی…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/137245" target="_blank">📅 18:29 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137244">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
عباس عراقچی وزیر امور خارجه:
رایزنی ها با روسیه و چین مستمر و مستمر است و ما به طور مرتب با دوستان خود در چین و روسیه در هر فرصتی مشورت می کنیم.
🔴
طبیعتاً با پاکستان به عنوان میانجی در مورد ابتکارات و پیشنهادات آنها گفتگوهایی صورت گرفته است. مشکل فقدان میانجی بین ما و آمریکا نیست، بلکه مشکل رویکرد مشکل ساز آمریکایی هاست.
🔴
تا زمانی که اهداف و خواسته های برحق مردم ایران برآورده نشود، طبیعی است که به تلاش خود ادامه دهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/137244" target="_blank">📅 18:23 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137243">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
ایرنا: حضور هیئت دیپلماتیک عمانی در تهران
🔴
یک هیئت دیپلماتیک عمانی برای گفت‌وگو در خصوص ساز و کارهای تنگه هرمز به تهران سفر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/137243" target="_blank">📅 18:14 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137242">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tt4NvkNuhuNef7m3rO5H98z5ok8tiL0dcIr8sRqFjVYsEtEkRpF7xZj5QZvOFsjqx8fGSgGok9q7l0JqlyMu2InjGyY3WRIaeeK40KeTdTtW1_zkyLdeWAI9_ZacoiuJhpYGpcg9f-2wQFbSIvOI-lVW5mSgoIOaIAtkH4rlWX9ri4ZG9eMN23TE4g8BY9Wn0YaxWvBw_x2l9wkqgn7aEEEtFBm5p-cCb6I3tzNhmL2hDdpyB47FL8NECA2TgG4OKetVG1MbZxsxqGO51kDWLSGWONhrVwHOzXu41UMM3pecQeT35ClhxWjKIEVXCpdZ4wsefeUozs_zamQmd3V8Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرماندهی هوایی متفقین ناتو اعلام کرد که امروز صبح دو فروند جنگنده اف-۱۶ رومانیایی و دو فروند یوروفایتر ایتالیایی برای رهگیری یک پهپاد ناشناس در آسمان رومانی به پرواز درآمدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/137242" target="_blank">📅 18:12 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137241">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oXifYFdKxfIXDUdUIds--JWNVbO4NY3BpcOy7aHcjQFrGoUpYLVR6CWrb2hhT2rePrA11uLvNGXJDSLvSd0s6qhSVOZYSsx6JjcSduotkUbFpuCrMc9h_Sz45KbxOKHF56XUcnkIInlW5YWGqkkyM715KoOEFWr8BlpZ468HZTelmr91zwt9pNI4OoB_Zb47gYapNOM8-uocM6LEQ79qTgD5JTr8TcPdKMn6FDUre3Yt6M9tPnEXCssBS-FAB3ngKy--RbhltO73_UNnKwam8IneGyOBqNy6MmdfBZlhxGtjaUvFPgspaAy0MHNBmfADIBTRImLZ-RRLjR2ZgX17Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امروز 2 مرداد تولد جاویدنام نازنین‌زهرا صالحی دختر 13 ساله ایه که در اعتراضات ۱۹ دی تو کرمانشاه کشته شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/137241" target="_blank">📅 18:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137240">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
وزارت خزانه‌داری آمریکا اعلام کرد ۴ فرد و ۹ نهاد مرتبط با ایران را در فهرست تحریم قرار داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/137240" target="_blank">📅 18:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137239">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
عراقچی: ما آتش‌بس موقت را نمی‌پذیریم و این موضوع مطرح نخواهد شد مگر اینکه خواسته‌های ما در مورد تنگه هرمز برآورده شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/137239" target="_blank">📅 18:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137238">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔴
فوری/ وزارت دفاع کویت: درحال مقابله با حملات موشکی و پهپادی هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/137238" target="_blank">📅 17:57 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137237">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
بنیامین نتانیاهو روز دوشنبه آینده به واشنگتن سفر می‌کند/وی علاوه بر دیدار با ترامپ، در مراسم تدفین لیندسی گراهام نیز شرکت می کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/137237" target="_blank">📅 17:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137236">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
شورای اتحادیه اروپا امروز با اعمال تحریم‌های جدید علیه ۶ فرد دیگر به دلیل آنچه که «نقض حقوق بشر در ایران» خوانده، موافقت کرد.
🔴
بر اساس بیانیه این شورا، ۵ قاضی دادگاه‌های انقلاب در استان‌های مختلف ایران در فهرست تحریم‌ها قرار گرفته‌اند.
🔴
اتحادیه اروپا همچنین یک مهندس رایانه ایرانی را نیز تحریم کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/137236" target="_blank">📅 17:53 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137235">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
نیویورک‌تایمز: پنتاگون در سایتش آمار نظامیان آمریکایی کشته‌شده در جنگ با ایران را از ۱۸ به ۱۴ نفر کاهش داد.
🔴
۳ مقام آمریکایی گفته‌اند که دلیل این موضوع این بوده که مرگ این ۴ نفر پس از اعلام آتش‌بس توسط ترامپ در ماه آوریل رخ داده است!»
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/137235" target="_blank">📅 17:52 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137234">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WA60LtHgGNA6EzwRhq_KjxwKBM-xqFsAK0mYQ1aL0RVdgKGD3y5BVtAOa751n8RbCw1iP6LOFUvZJCiK_3nlZ5KKqpWb1b3pdQx0BSCnmpU2hH_VNpLU9xglWNIbw1ZHcXQxJt6aJo5c04a0B53j99pREM4y7rgBviOeH-47RX3_O-HmF_Axh9c08rFCR7lL8PmPMYBqWTnDehGmKjQiFWsG4-IiFERQLsdw0hO6MqgcMUKkvipSjNJ-JYOzPspqkQqe5RWsHAdnguo-XmYnSFWJdEvdbQo15Z7ulNUSLCHO87gxKNwet7QsBBQJZP4XUH2ZhrAcQyTAw4YLxtSVBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جبهه پایداری افغانستان(طالبان) اعلام کرد در صورت حمله زمینی آمریکا به ایران ساکت نخواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/137234" target="_blank">📅 17:49 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137233">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
وال استریت ژورنال:
ترامپ در مورد ایران بیشتر به گزینه نظامی رو آورده و فعلا پلنی برای مذاکره با سران جمهوری اسلامی نداره.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/137233" target="_blank">📅 17:39 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137232">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
سخنگوی وزارت کشور:
برای هرگونه عملیات زمینی دشمن آماده‌ایم.
🔴
روز رزم ما، روز عملیات زمینی است، اگر بیایند به خدمت‌شان خواهیم رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/137232" target="_blank">📅 17:18 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137231">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
سخنگوی حوثی‌ها بسته شدن تنگه باب‌المندب برای همه رو تکذیب کرد و گفت محاصره دریایی فقط عربستان سعودی رو هدف قرار میده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/137231" target="_blank">📅 17:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137229">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rMcFkLdNZlPuHqunJjCoG2qtFXGy7-Gt8eQSBi79X455R69Cinl6WE8asBtzbQNOEqjD1L32BCMl-2Rht2hWahaN_LRJC9AK11yaUtLcaFrW04peso0mqFg_0dGbk_2FeT92PkgQvVeY18v50A2m_0gVsi_ZD_BlShGW-_1EUQs4FQFxKo6QFwOnHV_cMUZIeGNtnuzTM_wViPL3_JHrvUYXUrzHzvguQNQHVH8a-ypwyL0wmdBJPkyCiLAKvCR9lvoZvvlkRXO9ivrec_mDx7AmwWsfaM1YDWvRFKbetbbAE5CVMgbpxe8GFkh2rr4YX7v4QHCF-jtOMi3QELfLXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YZyPnV6fv9DxUDhGBtLgW8f5VNg48UPQg9kW-6Zwdg7up0ST2RC08W6_fTlf73TjqDMmq4KRtiP9RYvNyom7D8V0XPMX3SpddiqgaaQNaH9MRg9PZ8EuTyL8vhzLe3MzN5KHIKnodPCr2mPLZ-SiYNgxmV0B8A3TMomxbJi-qAcyKwO-qc3tk5AaUUJlEnwVzdvFg0m3Va0mv6FhouMfAlNbhuQ6puJ3RWqCJyvEBuAHsK6lbfZRltyTU89NTX30u8BOgHAcplD4Bpjx6Wo137FV3_Tu-Bc0WKCaUFlHvg1YVD6LVEZ9Ptv-Tz1yQXqiMHMxJFo2-CfVIf7oXERO8Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برند معروف گوچی از پوشک جدیدش برای بچه ها با قیمت 88 میلیون رونمایی کرد !
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/137229" target="_blank">📅 16:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137228">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
وزیر خارجه عمان:
تنگه هرمز باید برای دریانوردی باز و قابل دسترس باشد و از هرگونه اقدامی که مانع آزادی دریانوردی و جریان تجارت بین‌المللی شود، خودداری شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/137228" target="_blank">📅 16:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137227">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2ad0195b5.mp4?token=OJ4VIcQ5L9NKeLr6LeevKw8Ga558m0dRm9XGGfRy96n_e4uoUmo5eeBpJT0jiysfVidmFWJT5yQY4EmL3yKwCjJxHKx3y7VnZcxViXLC48GbBpsekmLFOrewVIOngeDo13sYWF5S6bzirrcsM1F9N7EF7m_bsWvQFC1PBxxLh9bsZvW9vRiADD7dAGk0zCBdE4PaP-Q-dJ5EnACjGFMwhUgJ59wu43sZuqLi5a6Uz3TMB7-0CMtRAxf4MgVGSswOHXblA0snGG6NpOx1AZru9bsq6sUpl1rho5lVv1sQCCIZqmrprT6vVMpCnYN1EIUY-fQ7nCmmomuE9UHtzrV2Kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2ad0195b5.mp4?token=OJ4VIcQ5L9NKeLr6LeevKw8Ga558m0dRm9XGGfRy96n_e4uoUmo5eeBpJT0jiysfVidmFWJT5yQY4EmL3yKwCjJxHKx3y7VnZcxViXLC48GbBpsekmLFOrewVIOngeDo13sYWF5S6bzirrcsM1F9N7EF7m_bsWvQFC1PBxxLh9bsZvW9vRiADD7dAGk0zCBdE4PaP-Q-dJ5EnACjGFMwhUgJ59wu43sZuqLi5a6Uz3TMB7-0CMtRAxf4MgVGSswOHXblA0snGG6NpOx1AZru9bsq6sUpl1rho5lVv1sQCCIZqmrprT6vVMpCnYN1EIUY-fQ7nCmmomuE9UHtzrV2Kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیو عجیب از تجمعات شبانه
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/137227" target="_blank">📅 16:37 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137226">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
چندتا عکسای صحنه‌هاش که منتشر شده رو ببینید
◀️
مشاهده تصاویر  زیر ۱۸سال نبیته</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/137226" target="_blank">📅 16:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137224">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/beaR2rpytZf1KsyWvZRkp9SaJ8DoH9YxsUsYYZ71cfPgV9s8JViupuA2ry5IYGfD1QeRSewTg7EpC0fwAXQ0a5BchkR89MMRdBAp5CQEMOZQ0L6g1-1oEiPXbQJP4WnvmbYIQrF374y_Sh765OztxvP7XgjZRHdt4AC_kZ_-yjSjorMjtJPE7rI9BGOANnlxtIhooEx291raxs4Clv_40qY1E3wZvzfU1dCyzjlNLoFJ6S_echerFzT2tLuWZBrSFX0Sa3lq4CBTNx9EraSngohXnJyGY7GeBh3LP4tsWrPA11HyvqXkNVFwRc-mvioihCbANHaJybEwX2AItcKUGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/h0Pul3TrsIAi4Cksr2gVZn1QJupDmMzo6sHLQr1bhL7BLfbdt31L5-av7dA7e3RK3lROOGfz6ne1a0nxOQDVcuQ9LdMGcm0w6IZSGHzPbSqnKb4deQmkj9U4Y-GNq53J_Xa7YO70SbMXX1LTpBAjLKpdpNL5zK3I_j1BkWdEc3bSHnBpl_wCS0ogCbaLCX1pVrBL3LifslUwmmacDkRzHZPvOuNBj-gDn0ZbnSLC-ogLXOfoI5wvXDv-M5Qc5XDN76pn-cITvtHE-S514-nq_cgJUFDKHZTnfNyWVTDWWITky-MshrGpgVtC18NYoBeHYG2MuS8xDY8-cMzaI7VHCw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
بمباران فرشی یک پادگان نظامی در غرب شهر اهواز توسط بمب افکن استراتژیک B1 آمریکایی
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/137224" target="_blank">📅 16:22 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137223">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p7qzwrc-Ce0M8z8qVRZGHEJwhA9-2p5r0CauCYCq2F6zIxrnapim-w2by9VPL07HPgsE3UVadSsemTvRFdwWNOPDjWQCgPpPOnZeBmlR7Dv--IwLYy__54v2CrUtin9gq12zUsjkOvkiyWsfjHCWEAEtgdiEuIBEtWaToBNyTRcQYPODvDqjmH4di1ES7OtjKCwXJK_wZmeP-zcbmS0WwkD6AqtyXYjVsK1oLu2MdY03IA4mTWkFF6IvcMzOMlu3GwpaeMZNP1YTVypmGLbhjFeZeycFKfx9N1sa6oMylmdZS-kKfWIr2Dh5FK_9vr_PBtv93mF1RWCMEtxdeTNucw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علم الهدی:
آمریکا پول داره اما ما خدا رو داریم
🔴
پ.ن: فعک نکنم
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/137223" target="_blank">📅 16:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137222">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51678b4c9d.mp4?token=lqb31H9uKeFh9D2TQ0QFhFeSOrJ8kJMXmjFuvOb3smLRWKQQW4rwlJozkU9rpvrZzLYytfImWlDjLpaaoa9bbcc6troeiwbTNJtHhl6dv1CXE4ATB-UGNDOaQxRlvrz6VDGLBk5W-WSk4B86ngi978KTXoecEYREPZ1EfnDD91AfnuSDSQPwwZiGCXhRp-csIMUASgdzlkz2anl2Cty-_2lZ-68gMUNX_1NovnuKIfMkcnxezUosat-nygfTRpaV3sUj0Rt0-z6MeKv8ABC2C3coJ4mnofuSnZwKtzPB_V9n2i6msan3O70kybL0Rdd8QNVdlfiLEwFTvmJ1xtwIBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51678b4c9d.mp4?token=lqb31H9uKeFh9D2TQ0QFhFeSOrJ8kJMXmjFuvOb3smLRWKQQW4rwlJozkU9rpvrZzLYytfImWlDjLpaaoa9bbcc6troeiwbTNJtHhl6dv1CXE4ATB-UGNDOaQxRlvrz6VDGLBk5W-WSk4B86ngi978KTXoecEYREPZ1EfnDD91AfnuSDSQPwwZiGCXhRp-csIMUASgdzlkz2anl2Cty-_2lZ-68gMUNX_1NovnuKIfMkcnxezUosat-nygfTRpaV3sUj0Rt0-z6MeKv8ABC2C3coJ4mnofuSnZwKtzPB_V9n2i6msan3O70kybL0Rdd8QNVdlfiLEwFTvmJ1xtwIBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
این مجری تلوزیون داره دم از فرهنگ ایرانی و اسلامی میزنه و میگه غربیا و نمادهاشون بدرد نمیخورن و ....
🔴
بعد خودش رو گردنش تتو داره و سعی کرده بپوشونش
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/137222" target="_blank">📅 16:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137221">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/080c6cf800.mp4?token=VosMTjXL_jqAQ-O2prDiHQV8jEawUofalAFjYkGjsPv0T5wi0jehryDuS9Xxkd5dGhAvQ7_EOzg6DFaS27xJskS49cUyo49pOi0NkFufQpDoaNuxdnmEzc4JVcv6-12LJY0BN56ym0rQ4-BkHrrPluEV6kKlRqffbO6kGmIU0oa_ksjY3hfOdmbUYsgH32FmsaIb9mTiu6zeBckNv_KDa7LSNj_8NiLBZWR4Iw8w9O6o3SQjE_3b6bhVqR1ymvPoMf3UMz6RrfRJGR0xurJr8k5Nfi-1pHQ5Krr4QHpzeolKTKJLmkXaIWafeZphDQkBVws2YBtXxMtPDMmeGZsJDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/080c6cf800.mp4?token=VosMTjXL_jqAQ-O2prDiHQV8jEawUofalAFjYkGjsPv0T5wi0jehryDuS9Xxkd5dGhAvQ7_EOzg6DFaS27xJskS49cUyo49pOi0NkFufQpDoaNuxdnmEzc4JVcv6-12LJY0BN56ym0rQ4-BkHrrPluEV6kKlRqffbO6kGmIU0oa_ksjY3hfOdmbUYsgH32FmsaIb9mTiu6zeBckNv_KDa7LSNj_8NiLBZWR4Iw8w9O6o3SQjE_3b6bhVqR1ymvPoMf3UMz6RrfRJGR0xurJr8k5Nfi-1pHQ5Krr4QHpzeolKTKJLmkXaIWafeZphDQkBVws2YBtXxMtPDMmeGZsJDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مردم ایل بختیاری: علیرضا بیرانوند از ما نیست و سر اون به ما توهین‌ نکنید، ما اونو گردن نمیگیریم چون با آبروی ما بازی کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/137221" target="_blank">📅 15:51 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137220">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
دقایقی پیش سپاه هشداری عمومی صادر کرده است و از شهروندان در سراسر منطقه خواسته است که حداقل 500 متر از پایگاه‌ها و تاسیسات نظامی آمریکا فاصله داشته باشند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/137220" target="_blank">📅 15:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137219">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
بنیامین نتانیاهو نخست وزیر اسرائیل و وزیر جنگ یسرائیل کاتز در بیانیه ای اعلام کردند: ما به ارتش دستور داده‌ایم تا عملیاتی گسترده در روستاهایی که منبع تروریسم در کرانه باختری هستند، انجام دهد.
🔴
ما به ارتش دستور داده‌ایم که سلاح‌ها را از برخی روستاهای کرانه باختری جمع‌آوری کرده و مجوزهای کار ساکنان را لغو کند.
🔴
ما به ارتش دستور داده‌ایم خانه تروریستی را که حمله تیراندازی علیه اسرائیلی‌ها در روستای تل را انجام داده بود، تخریب کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/137219" target="_blank">📅 15:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137218">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Il327xU6sXI5O9tFqVcSZmuRi9y49isW5ccd8PDatsemeuDkNWMGIFIzIWvLuRaMNZ_DNSbYhUHDE7IaxbsiY9R2_V_W_1IWO1p1JwEbcbdnXvZykFtg2BT4oeu6OxAHdMDUNVinbFOivQkzzY6DRa4-yhh-GZQNzLVe_EInh3mX9rT8fg5lkbxNW-kSMidkL7rZFJdaZs9WH1zq7Ka0GNM-MQ7B_7IRdUkChuor4bgxv7WSVyS2Myap1-yzzqbJV40YFU44hxgSiGqK8WHzMWHXTmWli3_g4UWulKqeLnQjO8ioG5u29Z2YO84us6j6sIJPlzTg6Gim_EHZ2uHGew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طالبان آرایش، موسیقی، استفاده از عطر، رقص و انداختن حلقه در عروسی رو ممنوع کرد و اونو خلاف شرع دونست.
🔴
همچنین نشستن عروس و داماد کنار هم در مراسم عروسی رو ممنوع اعلام کرد و گفته هر کی اینکارو انجام بده جرمه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/137218" target="_blank">📅 15:37 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137217">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
ویویان نریم خبرنگار نیویورک‌تایمز در ریاض: شایان توجه است که با گذشت چند ساعت از اعلام دونالد ترامپ مبنی بر اینکه توافق هسته‌ای آمریکا و عربستان سعودی مشروط به عادی‌سازی روابط ریاض با اسرائیل است، دولت عربستان هنوز هیچ واکنشی نشان نداده است؛ همچنین هیچ نشانه‌ای وجود ندارد که سعودی‌ها هنگام امضای این توافق از وجود چنین شرطی آگاه بوده باشند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/137217" target="_blank">📅 15:37 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137216">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
صدا سیما : صدای چند انفجار در جاسک حدود ساعت ۱۴:۳۰ شنیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/137216" target="_blank">📅 15:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137215">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BKPUVlPJ9_4Cy9ttF2QF9zQxohAudWsJ_jM3VokMX8MQ_nCJjKBndHkYwRVcjQUhrUeWW8Mc4MH6g-n3zk305d0FySu-vnbcGld0TiPslKB2YlUG647_oTZE5KADBp-UqCfKBll7FhRK_Ir4_ZJRfyICMyWJuTyKTFmt5veNsTndtc2K5DfR6y_fTC_hd2Em-CZcUSZxI3FKBJTv3RtaaVrOwBahCl79dMFqVRGAq1W5NqX_7kQeI35isOyizu0J7X0QjDmg7qmw_Kcm1VK7zsOSt3Acm5RG3j9SB3ZnDRhV6AXnAblvlO9SX_W7AZIINtraHaJ5nZMDvYOG3zsHLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شرکت تورم دانمارکی:کشتی حامل محصولات نفتی به نام "تورم اینوویشن" مسیر خود را تغییر داد و به جای عبور از جنوب دریای سرخ، از کانال سوئز عبور خواهد کرد، به دلیل تنش‌های امنیتی
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/137215" target="_blank">📅 15:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137214">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dGIItF5tp9fGn5XqihIIyJ3y_SHcdR00k4u6Mlf1OJZwA3O0rDhuxaEZU8qr8wNdx3THrm3uPUn3E8-31qSk75XIVqlh-yzGR0ItxoPv4iGbnMmT7Ih3pTU0ggakCS9XhfGvQ8VHWI34j6u_uJL44zDvyMWy1wO5EKer19eOFzT4UcfqUbTITN2vPo4arDlnTq2T6tM5Vq-LcTPko_kuiYALEDFmXDlN7W02o_BRJDZ-tKrPWYtPDrsm7ZtqzK38ja8qH6rfbQeluG0MfiYLd7ieQRt-swOf6qk1qHWvl65C8He66F8_IfuVtXpAQTyaQ4A9RnMgqs2w7RwYxUnJ6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
برنامه امتحانات نهایی پایه یازدهم برای استانهای جنوبی اعلام شد
🔴
مرکز ارزشیابی و تضمین کیفیت نظام آموزش و پرورش، برنامه امتحان نهایی استان‌های خوزستان، بوشهر، هرمزگان و سیستان‌وبلوچستان در پایه یازدهم را اعلام کرد
🔴
این امتحانات در روزهای ۷ - ۱۱ و ۱۴ تیر برگزار می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/137214" target="_blank">📅 15:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137213">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/672cf5b815.mp4?token=bhi2jP7UgJeuUeq_Qv4dWo9smsmf_fiSnE7eXUgTEH4Liik2HTL9s0TNH-CAUKdTSc-FpjFz-9hLvpRaLLN8tbzhvV3dFKJ104_n0kngnzfnSyh7z9VmOiyMwBWDoFNs1u_wfb2UYK3BKVZ_cDCMsyLiYapWBa0PCRIbTlzUZG_XWtVDm173DQpXTfT1FdioqX4AN63ijKTkiH7SHL70W4igaX8vD3oHW46UJSXlD_Jck7zn8PlX6VhNHrNPSNOC7QlJljzUbgOLugVONx5iokiqdn-Aeb2bT62DnImYrHcxX7IL3a5U0nWOr8rJm5KYfaDUKl2g6nwHEzCEBmyYGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/672cf5b815.mp4?token=bhi2jP7UgJeuUeq_Qv4dWo9smsmf_fiSnE7eXUgTEH4Liik2HTL9s0TNH-CAUKdTSc-FpjFz-9hLvpRaLLN8tbzhvV3dFKJ104_n0kngnzfnSyh7z9VmOiyMwBWDoFNs1u_wfb2UYK3BKVZ_cDCMsyLiYapWBa0PCRIbTlzUZG_XWtVDm173DQpXTfT1FdioqX4AN63ijKTkiH7SHL70W4igaX8vD3oHW46UJSXlD_Jck7zn8PlX6VhNHrNPSNOC7QlJljzUbgOLugVONx5iokiqdn-Aeb2bT62DnImYrHcxX7IL3a5U0nWOr8rJm5KYfaDUKl2g6nwHEzCEBmyYGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از سوله بالگرد در خارگ که مورد حمله آمریکا قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/137213" target="_blank">📅 15:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137212">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
وزیر خارجه پاکستان : با عراقچی برای کاهش تنش‌ها صبحت کردیم و نگران تنش‌‌های منقطه‌ای هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/137212" target="_blank">📅 15:16 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137211">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d26cedb2b.mp4?token=CFydEWDGfFjzGqPCeJUydM3ypUwNmAkBmNdS-2KxdSFHzJfN1xwG1ua4xpF7POUzBxmJW3YDMc_JFqYfa9gy2cEh_95A3LmlXZ0igIalAtYb3quN9TMzrbHF_8FnFKGduV2xuWhvJeUxtSPk8mH6rqu2MQbTVQsm1VJ2_jA5AHnAKjITJJFb2LpdmybyPTkukjQaHsgZM-ir34-VxlHo0EFWidfkpdTEx9nM8gf8elrMmW7-K-zPyTQ6H_JsPQ5S0NP6C5HoLx7CRXwyQVQR2Gp6qt9bR9F-ud1wxM81b-V9Pt2bkQiBIF5xw295-eyMC3aQRlB14dwwIgy4WjEpXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d26cedb2b.mp4?token=CFydEWDGfFjzGqPCeJUydM3ypUwNmAkBmNdS-2KxdSFHzJfN1xwG1ua4xpF7POUzBxmJW3YDMc_JFqYfa9gy2cEh_95A3LmlXZ0igIalAtYb3quN9TMzrbHF_8FnFKGduV2xuWhvJeUxtSPk8mH6rqu2MQbTVQsm1VJ2_jA5AHnAKjITJJFb2LpdmybyPTkukjQaHsgZM-ir34-VxlHo0EFWidfkpdTEx9nM8gf8elrMmW7-K-zPyTQ6H_JsPQ5S0NP6C5HoLx7CRXwyQVQR2Gp6qt9bR9F-ud1wxM81b-V9Pt2bkQiBIF5xw295-eyMC3aQRlB14dwwIgy4WjEpXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یه سرباز روس، بعد از شنیدن صدای نزدیک شدن پهپاد اوکراینی ، قبل از برخورد پهپاد با خودش، با سلاحش خودکشی کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/137211" target="_blank">📅 15:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137210">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
فوری / وزارت امور خارجه جمهوری فدرال آلمان از تمام شهروندان این کشور خواست که فورا ایران را ترک کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/137210" target="_blank">📅 15:06 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137209">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
کان: پناهگاه های بمب در جنوب اسرائیل در حال بازگشایی می‌باشند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/137209" target="_blank">📅 14:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137208">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
در پی اعتراضات مردمی در هند، وزیر آموزش این کشور به دلیل انتشار غیرمجاز سوالات امتحانی اخراج شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/137208" target="_blank">📅 14:46 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137206">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n6IaRiud4zpcB8D6zDHYwEbRLx28bdqGStfcLHCXpUCzw4_LjlPnizb5AZVCvYVVBSgCtLr9IfIfm8dupWUZqPdttUQUt5ws8-HLzhei4mwEC7mkyoSfEXvifQIGtF3KLvFegZXTzE6Ntqw8P99UWufaFWZ5G2ToLB_UG5kaJCId_UcgPVto7wnb2C8R_GyEa-0VdfkNJiacsNWDrc3sUcT5riydTiNE9G7qK3kIbzd-MpSkxHX3mY7aIk1PY9Hbv_495bv47nN1NM7_Isb-nu9kvJL4meqOvUzonZd9SeiT8Ad0i4guTc-rtNMT-qwppkbU1yysRou6daxZdL6WXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QlJDQdRpKzDRMNMFuga8SY241ErqNP_xj-O_XgdPObtFFC6UI_Kn0gd0mUR6zBDzSzL7-1MQRwM2vuFkYWcJTh31qqexkRzDqomPzNeVN-R5lt4h7kMvbUjBI6UtBAC6_ODHsElcbW9zWapG-laDVByKucbLTyYMER4glt5N3G2w1LeSkuj0QBMATFQXYXpu-h-z5cvLULOONxes4R4ved6XCkXEd55touNyPMrNat2Ru1HrwlUepyxSZ1lo6jGQrR31QdrAuqCzjUJr1CkT4_Erx058aMcA8GYUvZFCoShQf8Own9XpACMXRrZqos1akQDC9Wfaxg3G8RPeSQLQmA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تعدادی از هواپیماهای تانکر سوخت‌رسان آمریکایی به پایگاه هوایی سلطان در عربستان سعودی رسیدند، این هواپیماها از آمریکا به این کشور آمده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/137206" target="_blank">📅 14:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137205">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I5Ge4FENWBXsCKnusfx3EmJPPZYL_Qe6IftsTXjFL8dymG7QGC5itFIaZg8KDejtFP2625NhBLY7hx47a_s_Y5nqlRpGDeSG_OOxV7JTva7vXmn0nXEPjYYKGg3f8MK7mXvqXKcnDR6xlpYCQPeeTNBoc7Kpg7iqwgXc6Ztn2vxQ9aVbDmJmu7IhTS7YF98d7ysFDAcKczr_LcyZxoXIXHsV4hvsF6sSMeV0JAi_tauYEukVlJ7qY98vthDbrbAA6ba4x5ZH2vAyh5yeKuXDuajJFEBjoyN27fEHxLhqzJ3z4xYasWP44rytfFovL0-jZ9AvI-VJKR0sRti21_Vqng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دوباره عجیب اما واقعی
‼️
🔴
تو ایتا یه پوستر برا ظهور امام زمان منتشر شده اما این پوستر برای فیلم اونجرز دومزدی هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/137205" target="_blank">📅 14:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137204">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bmd_qGF_4RxExHGm9rmBVVCrhHh1UCUoFoSG5ewSXsULvN5dewtoHvF369sSG5hxJNHw_cQTUbyvWpWYN-CUUpfdFRO3eDtRj9xg_VVGx6qYQ58s_YVAK4wI7lUlcX0OqztpDlSQ9giDlUQmOldWQI1v3e4uLrSB1IaN72QvMFnV6CIE_7rkrJaxluEvz0-SH84P8d0B2c5VaGQ29Hb9Eg5Rmos73wLpGhDyR-UWa0ycji3Z3ZAOqfKjMbggVCRKH0ZNPOYXssgSmvHsTfocLBhtvUW6VkZG5FDo4gMmT8fDFTYKMSdEZs16QRk7Gi0vNC59bAMxNEXCNqWStpx7Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عجیب اما واقعی
‼️
🔴
روابط عمومی سپاه تو پیام رسان بله یه حساب باز کرد اما به دلیل ریپورت زیاد دیلیت شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/137204" target="_blank">📅 14:33 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137203">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
رویترز: ایالات متحده واردات سوخت عراق از طریق سوریه را آغاز کرد. در ژوئن و جولای، سه تانکر «آفرا ماکس» حامل سوخت عراق در بندر بنیاس بارگیری شدند و به سمت سواحل خلیج مکزیک حرکت کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/137203" target="_blank">📅 14:33 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137202">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/882fddeff7.mp4?token=UpKwPu8mwkMrUi18NT_BQ94v5K_pezlOaiLBNr0XPZLHVZr3X1e1V58UGUdPDAx1GKRT1yuDwzBefif3WdOBa-G8c6KLr1Xv8i8qVjghIOuMDfOXEE7e4szGw23ZVfJnTMN-HBWMZV4xWddSeEBzuDwP1oqtYPMiKkHObtBRzjEOAsfaUqW861iz763W9FtKWvYqh3z61d5c0xaW90pjFQ1NS458kzaW3-pOla2RDYXgKKJQOA9AMrJZD5y1ivawNbAtlSVDydRUtRpFbDgo_xRkKrKmqoGZwUhgY_b5HGzsvDmNXhhanbCQ95uZeVq8FP7lme5Vv7JfGgbM7WhaBXKJRb9Z3M4LfdwXblcjbiAtdn2jVRJytyAMTvGuqEH_VcHhtBNXxEZLzL7fpC7NyEalOY0TzYBooFU8QjOuCRdZ9t1keAXMODDNA1dmd2F3-ESuMSlIe0Kp9l-tZJJOwQdBCwmBCUsTdAVLhi199XW141tZUGl17Fl3fIVr4wFM88ynF-GAx7thOxossGCLnT5mec_Pb21hIg_Azezzhv38se2l56mGOk0kJ-llrcgnTiTsP0uHVg8Z2bUJI5BMPuFQz93jfnlcMmZH8Xcu0VXu-y9ngdFhaFO62r7Wj-3tQEKtUNUzD6izJnL47II5jKWoyZ_E5bitSBKpxneP5K0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/882fddeff7.mp4?token=UpKwPu8mwkMrUi18NT_BQ94v5K_pezlOaiLBNr0XPZLHVZr3X1e1V58UGUdPDAx1GKRT1yuDwzBefif3WdOBa-G8c6KLr1Xv8i8qVjghIOuMDfOXEE7e4szGw23ZVfJnTMN-HBWMZV4xWddSeEBzuDwP1oqtYPMiKkHObtBRzjEOAsfaUqW861iz763W9FtKWvYqh3z61d5c0xaW90pjFQ1NS458kzaW3-pOla2RDYXgKKJQOA9AMrJZD5y1ivawNbAtlSVDydRUtRpFbDgo_xRkKrKmqoGZwUhgY_b5HGzsvDmNXhhanbCQ95uZeVq8FP7lme5Vv7JfGgbM7WhaBXKJRb9Z3M4LfdwXblcjbiAtdn2jVRJytyAMTvGuqEH_VcHhtBNXxEZLzL7fpC7NyEalOY0TzYBooFU8QjOuCRdZ9t1keAXMODDNA1dmd2F3-ESuMSlIe0Kp9l-tZJJOwQdBCwmBCUsTdAVLhi199XW141tZUGl17Fl3fIVr4wFM88ynF-GAx7thOxossGCLnT5mec_Pb21hIg_Azezzhv38se2l56mGOk0kJ-llrcgnTiTsP0uHVg8Z2bUJI5BMPuFQz93jfnlcMmZH8Xcu0VXu-y9ngdFhaFO62r7Wj-3tQEKtUNUzD6izJnL47II5jKWoyZ_E5bitSBKpxneP5K0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صداوسیما کدام بخش از صحبت‌های پزشکیان را سانسور کرد؟!
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/137202" target="_blank">📅 14:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137201">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tE8Y8PyRrUWlIAYEOOZzoeHilW-CpGAPURGYfqHichgtn7SWnHRKNH73hpIgva9OiGjpn9sTFbXBnQy-_87dtk2vzuYZqXi8FULADxwscxBYdgLnNr48PhKF81_MYul2__xf06BmhL9QIsUAYSbbQeRnafNcbEbUsIxfpKTWJqFwMaymUAhaxAHHqSTEAiDavxCM9yI4cWH_CIrhaiSTgXn0WPllp9X1jMT4QO3bwUChVLKLpGvWQCBCD7cVP2L8ZQN_Zq1EBm3D9q4U4Z38B7Ib8RzIbobUFFl8nddWroccizIF0829iOyX-L3rPpdJ0nX5Lct3hWY1F8uyJGEkfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محمد مبین، مدیرکل تولیدات رسانه‌ای دفتر رئیس جمهور: سانسور سخنرانی رئیس جمهور پزشکیان در جمع تولیدکنندگان و صنعت گران توسط صداوسیما عجیب نیست، وقیحانه است
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/137201" target="_blank">📅 14:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137199">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
دفتر الزیدی گزارش نیویورک تایمز درباره میانجی‌گری میان ایران و آمریکا را تکذیب کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/137199" target="_blank">📅 14:19 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137198">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
عراقچی: کتاب نوشتم، «قدرت مذاکره» نتیجه‌اش هم داریم می‌بینیم.
🔴
همین دیشب یکی از وزرای خارجه آفریقایی به من گفت میخواهیم دیپلمات‌های مان را بفرستیم ایران برای آموزش
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/137198" target="_blank">📅 14:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137197">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ab99fc66e.mp4?token=RfJCs0q_-RxSuF7I1BACYdJGdwGoBaRmEdxY8-zLEQ2O_o47rTr4jee28Ubn5EL2Uxw4Gf5GPBcBLzVKGSy_3uUrduSdF1ypAQgo97594p_Ebr0_D8dkYtD8fcErPGsY-UA00DArrGprOrv3LbbyJktDnFYjcRudSPUzX9tgZVFPSveBCpraliVXjAu2siA4ZZWH9NZ93xwNVbjOi8M41IwXt-VR6f_0d7uJxuRlFL2lJt6cMDXoYobQZCdqJ747rrWaWpqv5sSxbT1g9Ku3Hiuhwe6WxuWjHoOFINbU6JiU8RNP_4wfWPwZZoWih5zToDatc5KmEb8HbfN5HHtn0JiM9w0R0cLyqbjc9eSrsj9ZzwR_9fCppkHz7bwsbjIeU9VfBUHRFu5QpV1d6GB4hliZxHHiTdbV6lnXS5Vd8X0c4C2CyZbP5W3wzLbOHjyX6GjupMvPPKptsv8dQKqUAHvhdw-beBe3TSuC5nHg4rxz1-zjgqN9c-Zv4CSyjbSCSIAg8ffNH8oFQS8fUAM1ZTYeAcWayIsNKwWAjS-dVaI0FWSEeb2Zcv2_fEkeDX5iMRi-TUCJjBMoa8JVpP0LReRJri0hgjD8QKVhvcIULHfpaUEUf2JzCqDO-bXd87UFBfxccTJCKjGT-Xl2xLx7X5KzEto6zcu_3suaMCri4gM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ab99fc66e.mp4?token=RfJCs0q_-RxSuF7I1BACYdJGdwGoBaRmEdxY8-zLEQ2O_o47rTr4jee28Ubn5EL2Uxw4Gf5GPBcBLzVKGSy_3uUrduSdF1ypAQgo97594p_Ebr0_D8dkYtD8fcErPGsY-UA00DArrGprOrv3LbbyJktDnFYjcRudSPUzX9tgZVFPSveBCpraliVXjAu2siA4ZZWH9NZ93xwNVbjOi8M41IwXt-VR6f_0d7uJxuRlFL2lJt6cMDXoYobQZCdqJ747rrWaWpqv5sSxbT1g9Ku3Hiuhwe6WxuWjHoOFINbU6JiU8RNP_4wfWPwZZoWih5zToDatc5KmEb8HbfN5HHtn0JiM9w0R0cLyqbjc9eSrsj9ZzwR_9fCppkHz7bwsbjIeU9VfBUHRFu5QpV1d6GB4hliZxHHiTdbV6lnXS5Vd8X0c4C2CyZbP5W3wzLbOHjyX6GjupMvPPKptsv8dQKqUAHvhdw-beBe3TSuC5nHg4rxz1-zjgqN9c-Zv4CSyjbSCSIAg8ffNH8oFQS8fUAM1ZTYeAcWayIsNKwWAjS-dVaI0FWSEeb2Zcv2_fEkeDX5iMRi-TUCJjBMoa8JVpP0LReRJri0hgjD8QKVhvcIULHfpaUEUf2JzCqDO-bXd87UFBfxccTJCKjGT-Xl2xLx7X5KzEto6zcu_3suaMCri4gM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دومین پرتاب استارشیپ از داخل مکزیک این‌طوری دیده شد : استارشیپ بزرگ‌ترین موشک شرکت اسپیس‌ایکس متعلق به
ایلان ماسکه
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/137197" target="_blank">📅 14:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137196">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
ویدیوی جدید از پل کهورستان شهرستان خمیر که طی حملات دیشب منهدم شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/137196" target="_blank">📅 14:06 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137195">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lXIJ744eJPvyrNJMkx6TaCsam4E6FN7nc4jPRuX05Mi558Hoy46twNmSwt0vJiigi1iQ1c4hZppUskdTYVFYg6FbzIBtcUCnxwXA4fA4Q_hR_0dUrOpUVQsA6M041bVAGzeguW8SWwJDDMT-T23a7kPzNl-ogwcdUbh2npm-XracZw9YSWFa9OR9Gn8Ilijwqgr02i1fuOlBnkpy7n668TJoFDxRs4IIZAPk3W0dZGEwx9YVoCrFVNlG4DSi8sJt2OXgulSieMvhxZRCMYiWY-VEBNS_CEL7c5xeGjJaRnIKW6WlERA3RG7c8DYwwHYd-1oklP0kdlZdZehCsbB2NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واردات LNG چین هم به بیشترین میزان در ۲۲ ماه اخیر رسیده است
🔴
چین از شروع جنگ ایران واردات خودش را به شدت کاهش داده بود و جهش تقاضا این کشور می‌تواند فشار قیمت به LNG در جهان را افزایش دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/137195" target="_blank">📅 14:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137194">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YeDXL546OlbgIKZ5swibT3peGzldPIYGw07cBUIPdfE9uRL1-g1l2vb6oA1ULnXlaIJFFpoVJY1kaUXxYgS0uK31_HF2grqkXxzxbeUoEf5qvLOS4zx85cfq5b-te6lEhnQO7HsGCvzcg0b-Vd5D4yGye530GK24nPv5rxdE3h2bQ9tWhTm7UZRbNJrfQpiam3CiUmMLIlP5_la9KIj43lxVoft2qFHLRcCnERWhZbS4ScDyHvnTOqdPCbV5MZC7ki2oO8NCOyq9J92dNw0JJKGsej0PyyBI01ZUmRS166fiVamxEPg0puDpBx4JN3JyKBCMlZmEqTKgKFZw44UCjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آرامکو عربستان فروش نفت از طریق خط لوله سومد و بندر سیدی کریر مصر را شروع کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/137194" target="_blank">📅 14:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137193">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Grrhtd0GffkJ-u5kpTYMSoIbCsdyY8_ZmFiKYiSVac_-csbzbjpnct9qrltw5QjUhC9qQidzSv4TFVCBBDlOXCgHFsueH-6Y1sl3BN0oy2aN-Mj0Q1CdayBTS9b8TqaKchgveQ-H12Vyw_CHmo68mevuhJaM7D2gwlnCX3u42j_G-g7IQVHLy7taHrIhGyxz6g-tbrPThjUiIcH-i_jJB6C6TEIkOQca-6QxzYB5NpH44dPD041DpjYm83sQF7jRh-2vRqtGdbLLpIsuUEcsKRHE8Z59szyG_H0NdKeHiQJ41Umcj8yfLcL-NGVTRzF9LC-gQwLzKqrI5EwyT_xqrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توییت حساب وزارت خارجه آمریکا؛ سیاست رئیس جمهور‌ ما  :  یک سر در برابر هر چشم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/137193" target="_blank">📅 13:57 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137192">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VR-Cak1co2_z7RmTm9QF1q6Qv7DZZJe7NGzaKeM4eRwu8RFDo3_UJoqzaCVB_-mwp0KXyn5nyvdzeDj-lFLDnsmWq5dc6JrhaagdApXRe29hsWuSQntlHIZhJqPASAJmTUNDGvUoGNBay0uECAgNHabAgybm9bWEo0rrtzQSOUqALXw7AmbKhtwyTvs_6tNaAt476-Q0GkBTOOrfgxS585s5Sw2zPc3lj1vrHzMV6Wh4JWBw6WUBbRcgW0G_y5pc-5rLVGA4zY43ROWhmiygKU3mnS4HEeJqowytBfYPW2VcZPz7E-4TaZSEF_nULtP_e9Cwm7DQzWlDQ2tb5HAjFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دو هواپیمای جنگ الکترونیک EA-37B کامپاس کال دو، مقر انگلستان را ترک کرده و به سمت خاورمیانه در حرکت هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/137192" target="_blank">📅 13:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137191">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
عراقچی: عراقی‌ها استقبال عجیب غریبی از من کردند
🔴
عراقی‌ها من را قهرمان خطاب کردند
🔴
صداوسیما سانسور کرد و پخش نکرد
🔴
برخی به ما شعار مرگ بر سازشگر می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/137191" target="_blank">📅 13:46 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137190">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
پلیس فتا تو مشهد یه دختر ۲۰ ساله رو دستگیر کرده که پسرا رو میاورده خونه فیلم های سکــسی ارباب رعیتی و فیتیش پا و... ازشون ضبط میکرده و بعد به قیمت های بالا میفروخته.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/alonews/137190" target="_blank">📅 13:36 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137189">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/myL47O1tp2WCo6r6NpUslScm_5R_rJyqkwwbefHy2gZkfKyyRLxJhhvjcAxJd3j4SrG34W7i2nNQlE7oQUCLczYRWGO9BH-PyhcjMlwQS-SjRBPli4c-j7ugB5V6ore57VS2Ay43qML45wksrCaF9Fh8ijMOJHZBf9TXM4L-ngYyPp8RwZdNE8PdDxMxCDX3b8ygkuPQweWvmJ443MvmkIA4yJH8arQjIl1ftRBGW_h2M13rU7EpcKMvyVRSUhehRXBDnaB1ciYTPeHWLrS4H29gnv0flkk8aE_hZj2LQZ8-n80xcgaeidAAIa3O6PqBUxAWnxXp88c00vBODs4Pvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پلیس فتا تو مشهد یه دختر ۲۰ ساله رو دستگیر کرده که پسرا رو میاورده خونه فیلم های سکــسی ارباب رعیتی و فیتیش پا و... ازشون ضبط میکرده و بعد به قیمت های بالا میفروخته.
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/alonews/137189" target="_blank">📅 13:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137188">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
نیویورک تایمز: ایران، پیشنهاد آتش‌بس موقت آمریکا را که توسط دونالد ترامپ به تهران ارائه شده بود و توسط نخست‌وزیر عراق، پس از بازدیدش از کاخ سفید، به تهران منتقل شده بود، رد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/137188" target="_blank">📅 13:29 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137187">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
رویترز: در ۱ مرداد، تنها یک نفتکش از تنگه هرمز عبور کرده و این کمترین میزان از ۱۷ اردیبهشت تاکنون است و هیچ نفتکشی نیز وارد این تنگه نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/alonews/137187" target="_blank">📅 13:18 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137186">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KYkqfdZeCV0QfGv0Am33gFDvAdSwI2v0Xpx0u7R3JJVCXjtQNwXQGyWG8jmAXytNo4f8K3ABCzWSXpN7LAvSJk4Q3xIuA3knSG6wndCnf7yI4bab9fTc-VySQAYc3hdRIyMvEVZ44o0mROQD3UJJ8PG8MzKvN5zDQ5t2_BRj0FGalTE3jCSl4YhTvLpIxM4iykwRdS7OSvFhNpBF8pRj5o66GqE1VbKjm_-LswOba4IQjDH7T1Rzb6MR1qyQUSFjKgPq1_LHhyr-Y4FBGigKofOhKlf7i3LococfAqG52TF7BJvfr2sMVqaUF9TCvyLkTBdMvKsS2_eT70zOq47IEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بورس آمریکا همچنان سنگین داره می‌ریزه
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/alonews/137186" target="_blank">📅 13:12 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137185">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T2EojfSDvHyquYhE0CsqIwL6OTcAigk3X8oSIBP_2rprSnLRwOFGX_BbfWLrKUz070JA2B_ZHTo3oCDBKmXUrMn-E9EKzFVe2OR73YIaoOBhmdntR1iJwOw_qrm6dpdV_4VKeuTut6B4MQ62CSrq1l-tkhr_xJuWtCnd-79deYv_DwKnwyhh93JhYa9BKd-tDHkb6BSsSQtzRkglhalpefV42aeG2ZHsM8m1XPBowBVzBa0vAJg-Bzq3YD54wQnvE91VWoLQLBJVBWCE80t8NDwGUIbVLoLQvbwjJ5cYIulk6Laa7SYslali5dVDtdBoQFKfsHAml23KX_6FWjWJDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
منتسب فیروز آباد فارس
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/alonews/137185" target="_blank">📅 13:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137184">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ba25b1275.mp4?token=KqcKjSrJGWgMVatgGLMeoNB1sDYSlFo46yyHsbS4zc5oxFt1fLARm7-LF8MxBjPxhKYn5rrukYvoMERfHz5JRHv4hOx2gI5Qr-F0nqzvFATAsIQWmkSzSJmCEfe96pkJTdSxj3rTSIbtFURYHr9jdRw0VtThhJisON2OhF07vssO9Y-Grua9elW5wS7jEk-HX4-jb0cSJ80Sba0USr6YE00G56mntYa-0uY64VBsxuUUJsdSyN1yKpHFT_oUuEF5_hjyqLsnaxfzZVYln_UecWjXqayulFQ5QpyFytLwNvtTM11nRfQhLQu-_zZwaXYlf_zTW-q_DsMtPGypvCYxIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ba25b1275.mp4?token=KqcKjSrJGWgMVatgGLMeoNB1sDYSlFo46yyHsbS4zc5oxFt1fLARm7-LF8MxBjPxhKYn5rrukYvoMERfHz5JRHv4hOx2gI5Qr-F0nqzvFATAsIQWmkSzSJmCEfe96pkJTdSxj3rTSIbtFURYHr9jdRw0VtThhJisON2OhF07vssO9Y-Grua9elW5wS7jEk-HX4-jb0cSJ80Sba0USr6YE00G56mntYa-0uY64VBsxuUUJsdSyN1yKpHFT_oUuEF5_hjyqLsnaxfzZVYln_UecWjXqayulFQ5QpyFytLwNvtTM11nRfQhLQu-_zZwaXYlf_zTW-q_DsMtPGypvCYxIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رائفی پور: آمریکا به روزای آخرش رسیده
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/137184" target="_blank">📅 13:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137183">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
شنیده شدن صدای چندین انفجار در اطراف فرودگاه بین‌المللی اربیل و مناطق غربی این شهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/137183" target="_blank">📅 13:07 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137182">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2d9d6f9b1.mp4?token=n9NI2ouggvXeWqb2-5vwzibetGEsudzLy-aRal1Hx5Z2EQ9I1v8rDR_wjBsmqUu5_KGKdEYNtayZ42q19RRMWLVAtxO3-t5tIKXuZix5Z412CZfvw3djMdqz6MYThkrp2yI_iuiLgqeOUma4Rl_t1GGSfcLSutt4bwO5nhrMmdW03he1Ni4n920owe6mP098_rLKPSscDECvduLQ_QX3dp0gN1NhkCVVDKCM6u-jDO9lvDRyNeV5dF05m16xA_kuSmkzqNezkUjKUENMbWxOTYjcTG9XORL5fDOBIz6tv9iW7FIHin7lQyqpwpp2DWAeOe6vsspQNrQojRdcO3ry-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2d9d6f9b1.mp4?token=n9NI2ouggvXeWqb2-5vwzibetGEsudzLy-aRal1Hx5Z2EQ9I1v8rDR_wjBsmqUu5_KGKdEYNtayZ42q19RRMWLVAtxO3-t5tIKXuZix5Z412CZfvw3djMdqz6MYThkrp2yI_iuiLgqeOUma4Rl_t1GGSfcLSutt4bwO5nhrMmdW03he1Ni4n920owe6mP098_rLKPSscDECvduLQ_QX3dp0gN1NhkCVVDKCM6u-jDO9lvDRyNeV5dF05m16xA_kuSmkzqNezkUjKUENMbWxOTYjcTG9XORL5fDOBIz6tv9iW7FIHin7lQyqpwpp2DWAeOe6vsspQNrQojRdcO3ry-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صحبتای احد شکوهیان از داخل زندان:
من یه کارگر ساده نان‌آور و سرپرست مادر پیرم و پرستار برادرِ 55 ساله‌ی ناتوان جسمی و سکته‌ی مغزی خودم هستم که همیشه وضعیت مالی بدی داشتم.
تو شلوغی‌های 18دی دیدم که مردم برای نجات دونفر دارن میخوان مسجد رو باز کنن و وقتی رفتیم داخل هیچ کار خاصی نکردیم به جز یه نفر که تخریب و آتیش‌سوزی مسجد رو انجام داد و دوربینا هم فیلم همه‌چیو دارن.
بازپرس‌ها بدون در نظر گرفتن حرفام و فیلم دوربینا، میگن که اون شخص که مسجد رو آتیش زده و باعث کشته‌شدن دونفر تو آتیش‌سوزی شده، منم.
از مردم و جوامع بین‌المللی خواهش میکنم که صدای من باشید و نذارید یه شخص بیگناه کشته بشه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/alonews/137182" target="_blank">📅 13:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137181">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">گرفتار قومی شدیم که کلا ۲الی۳میلیونن اما خودشون رو نماینده ۹۰میلیون نفر میدونن
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/137181" target="_blank">📅 13:02 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137180">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
گزارش انفجار انتحاری در منطقه خیبر، پاکستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/137180" target="_blank">📅 13:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137179">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
عطریانفر: جریان سعید جلیلی فقط هیاهو است ، اما به حاشیه خواهد رفت
🔴
این جریان فقط قدرت اخلال دارند.
🔴
این جریان ضعیف خواهد شد و به حاشیه می‌رود
🔴
این جریان با ضریب دو برابر به سرنوشت احمدی‌نژاد دچار خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/137179" target="_blank">📅 12:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137178">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
وزارت بازرگانی چین : علت اعمال محدودیت بر صادرات کالاهای دو منظوره نظامی و غیرنظامی به ۱۴ شرکت اتحادیه اروپا به دلایل امنیت ملی است.
🔴
این ممنوعیت از امروز اجرایی است و این کالاها دیگر صادر نمی‌شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/137178" target="_blank">📅 12:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137177">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sUoMX8VG5LoY_JYjUjE3Ke17PUVu6FlXzcRnfEx8JNHf_jlBbtBDW6wLhFb6X-ztq6gW-vQ5dJcc5hOGCPmCXUdnTZWgqhTiBXbGCBkg5q4rmWH8W77WStXPP3_d0x6Sk54v0xNvMjz5NBVbfHcl982Fm7664rynIV1Lz0Yg63us-WfzW1hoYui6-ITnyhdSs2j5tU3Ya_fHl-72YCWdj4Pfawu5EGetamp8zrvB2yEpHyPftP_IAX8zEe9cym0iLZ0qZ68rIG6txBOCa1X1HsPWQbNs_r8fH0zKzI2km58xPj4d8cZo03WWcRiX5fxhaDx4leR8nPRKzYXVHvWZ0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ثابتی: مردم ایران عاشق رهبرن
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/alonews/137177" target="_blank">📅 12:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137173">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf63a433c0.mp4?token=pWIJaFGI2S62Fx9fuUo7MmmDqYtfhrHskQmLWouEvIzrUXdz_JJctbanGD87IbU5lJCi0eeCHjLcZQyvkJvqH33BmmpBG3uWOKDopqVl13kklUw36ihNd3wBZum9CHq1_1iJa-4G2TOwv-Gu2lSMCiIGljbPh3tn8Yxidi1t0D62c-3nzcOjfMHRy5B7jQ8oRcKzifOuTeWm5gJoTfxkqlsgoO1thy2fe_rC7GmvGUn9gaf_8ojxo1JqVSmF8bUOFi1dTiMknDeXWpCOtjSpRREn0aC6pbuf1H3F7zP44P8whTESsORxVy_bN4Z68iFH-JJm7-jk4r3RceRNQVagwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf63a433c0.mp4?token=pWIJaFGI2S62Fx9fuUo7MmmDqYtfhrHskQmLWouEvIzrUXdz_JJctbanGD87IbU5lJCi0eeCHjLcZQyvkJvqH33BmmpBG3uWOKDopqVl13kklUw36ihNd3wBZum9CHq1_1iJa-4G2TOwv-Gu2lSMCiIGljbPh3tn8Yxidi1t0D62c-3nzcOjfMHRy5B7jQ8oRcKzifOuTeWm5gJoTfxkqlsgoO1thy2fe_rC7GmvGUn9gaf_8ojxo1JqVSmF8bUOFi1dTiMknDeXWpCOtjSpRREn0aC6pbuf1H3F7zP44P8whTESsORxVy_bN4Z68iFH-JJm7-jk4r3RceRNQVagwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله پهپادی اوکراین ، چند مرکز فروشگاه زنجیره‌ای «وایلدبریز» روسیه رو نابود کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/137173" target="_blank">📅 12:39 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137172">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
وب‌سایت کپلر برای داده‌های دریایی: تعداد کشتی‌هایی که در ۲۴ ساعت گذشته از تنگه باب‌المندب عبور کرده‌اند، به ۱۲ فرارسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/137172" target="_blank">📅 12:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137171">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
گزارش از هند: شرکت کوکاکولا قیمت نوشیدنی‌های رژیمی (دایت) را در این کشور بیش از ۱۰ درصد افزایش داد. این افزایش قیمت به دلیل اختلال در زنجیره تامین ناشی از مشکلات در تردد کشتی‌ها از تنگه هرمز است
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/137171" target="_blank">📅 12:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137170">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97ddf0a505.mp4?token=pxP119UnA1rUNdJuYvxDr9kv7yUVbjI9NHUN5ptp2lVWelDhEZH7tw-w5loP_d8VU2a6FXoLv8KL5gMPGNjD48kTkRrOdr5DXsGZa0TxRHvKssELTctcqE8T0uBieISqhf4h8KwDETwL5ZELq43C7t2Fgf-lEO4ZR8xxvjwbkbISZqhYg7yOiuRjdXn1P4oVfGpKWSLEYC5OPEr6dACJ2DQ_bbRSfOmR7wWSMei6Cc3X4NzJHfTyzhC-1lWyOgsNXHTuusdQ_RApZq9h7zc55x3KMY9omRMKnpAn8xzIb74_sEWRl0tcaSWyiWpHaqSeNUkS9qIxZAyO-oKJl6XmXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97ddf0a505.mp4?token=pxP119UnA1rUNdJuYvxDr9kv7yUVbjI9NHUN5ptp2lVWelDhEZH7tw-w5loP_d8VU2a6FXoLv8KL5gMPGNjD48kTkRrOdr5DXsGZa0TxRHvKssELTctcqE8T0uBieISqhf4h8KwDETwL5ZELq43C7t2Fgf-lEO4ZR8xxvjwbkbISZqhYg7yOiuRjdXn1P4oVfGpKWSLEYC5OPEr6dACJ2DQ_bbRSfOmR7wWSMei6Cc3X4NzJHfTyzhC-1lWyOgsNXHTuusdQ_RApZq9h7zc55x3KMY9omRMKnpAn8xzIb74_sEWRl0tcaSWyiWpHaqSeNUkS9qIxZAyO-oKJl6XmXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شهریاری: ثابتی جان جوگیر نشو، رهبری رهبر شیعیان دنیا هست نه رهبر مسلمانان
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/137170" target="_blank">📅 12:22 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137169">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
رئیس‌جمهور رومانی، کلاوس : یه جنگنده F-16 یه پهپاد رو که وارد فضای هوایی کشور شده بود، سرنگون کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/137169" target="_blank">📅 12:18 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137168">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eA_Qd2BUewEHMc7oRIM-KpLCHVasobpYSGIqEABcqIbHHBpEWW4uyuFlD6fZ-ct-Y3GRX5fQ9niiBvMSLmSMbXrol7yIO7RQObjyLvQvopgsBdPdUr2P4A5Um7_vtefMebMJOhMbl-GGcjcw27lIdnBUx1wX0wTGp7JzB3ub3rKWD9A--1yvcbJ8e3Kcfm6YYZrkjYU3a7DXs97c4b6-N4CJTGcQ5PMCElKb5Kkrd2uTK2SEHdMdENc85Ilt40d6gSc7PxvEArpg6BraUF0K36yXNbAUzvczd_oDh35-UP_kPYpYhJBsCq7plitcOzw_iR4Tmfyh05k6R58Uxn45mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی: "توقیف دارایی‌های یک کشور برای پرداخت مطالبات احتمالی و نامرتبط در آینده، ایجاد یک سابقه خطرناک و التهاب‌آفرین است
🔴
کسانی که از چنین منابعی استقبال می‌کنند یا از آن سود می‌برند، باید به خاطر داشته باشند که وقتی دولت‌ها مصادره اموال دیگران را به یک رویه عادی تبدیل کنند، دیگر هیچ دارایی‌ای از امنیت و مصونیت برخوردار نخواهد بود. آشوب و بی‌ثباتیِ ناشی از چنین روندی، نه خوشایند خواهد بود و نه صلح‌آمیز"
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/alonews/137168" target="_blank">📅 12:07 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137167">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
بقائی: با چین و روسیه درباره تحولات غرب آسیا بحث می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/137167" target="_blank">📅 12:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137166">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
سپاه:
باقی مونده ساختمون آمازون رو نابود کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/alonews/137166" target="_blank">📅 12:02 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137165">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W57sO88pxOurPToLBGfsF4jaI1ycZjFrzLY3nc8EfbJODyF7uYozQTDkd0YENYewv4I_06CzM0qaVoQfP13DuPWa7HBrYTf0lKWLqqZ1BzGoY6HkKdhRZM08yE-b8Thd9g_w2RiYlTfQMHbkVaIll12TZhRz6Bol8q_M8XeBE8UfsHxt2b5HmvV-gYqO15wTtny0oG2Pp5zAyxRXAwsLjURXBK72vrBi3CyMo3DeCLhRI6PM3wGWb9hakuK6D8EB2YN-C_0MX6cQD3mxHWH31uIlKso6PTpX53MJZsLqYEf2QpwvgmMYpWifIrv8c48FN9iAvHNJQItjMTMP-bciSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گویا یک موشک کروز آمریکایی در حریم هوایی شهرستان کهنوج، واقع در استان کرمان، شناسایی، رهگیری و منهدم شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/alonews/137165" target="_blank">📅 12:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137164">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81a7d74649.mp4?token=mCXt4cbePqu-OmTfAUZLrWROLpW0ERd4vdpXwALBLrRWDNfSXBf5P7NE8rjta3zRYl6mz5-nQc0O_-Io7bLj9Qy7fQWgTw8DeL5okKy9joHq8JX43u16D5uDW3YFT5_aT5m9JSC5FNWPEkqqRvGTgprlkxq8cdbwW8Yj2hzPKHI6E1aSNSHNEFZJMQKQwcx3sDgW_1O0XqoVG7qihktrPOCd3T39HGCddQSfMeNSi9ltvi3JQWCS6KDGBOKMMGSyDKZjHmd-lo_0vYrN-hUFb11UuO8MoCsOAmmCm09f-GF47UwWl0mYlK-XG1Xp1LvDX1H_F2XUAeFAp_H3HlZsKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81a7d74649.mp4?token=mCXt4cbePqu-OmTfAUZLrWROLpW0ERd4vdpXwALBLrRWDNfSXBf5P7NE8rjta3zRYl6mz5-nQc0O_-Io7bLj9Qy7fQWgTw8DeL5okKy9joHq8JX43u16D5uDW3YFT5_aT5m9JSC5FNWPEkqqRvGTgprlkxq8cdbwW8Yj2hzPKHI6E1aSNSHNEFZJMQKQwcx3sDgW_1O0XqoVG7qihktrPOCd3T39HGCddQSfMeNSi9ltvi3JQWCS6KDGBOKMMGSyDKZjHmd-lo_0vYrN-hUFb11UuO8MoCsOAmmCm09f-GF47UwWl0mYlK-XG1Xp1LvDX1H_F2XUAeFAp_H3HlZsKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش اعلام کرد که با استفاده از پهپادهای "آرش"، انبارهای تجهیزات ارتش آمریکا را در پایگاه العدری، و همچنین پادگان‌های نیروها در دوحه و تعدادی از مواضع را در پایگاه عریفجان در کویت مورد هدف قرار داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/alonews/137164" target="_blank">📅 11:53 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137158">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41ff96b40d.mp4?token=nK8ZU6cSNTxxgG5zyXfeN12rd0cTAD9UHY5bUDLVRaOuCoij4tSiSErzwSkXusgtSgvXxdBl9Z5v_HzSwbMm0jDnHvQ6PzrbZ3ncHp5jA1jn6iZeNFy4WOx6Cq9tMx5yJCe2zYLm_ChIw10lXNC5J5NwY0nbRi6Dd0BrxNbSH1nQlh59iQernTshMK8lj6dsSkri2VT2ZEjjzhjPgLluV-MEJ9wwTYHJVkHYML37pqa-2LFmA6BFTMFrH7NZcGaZSP5aDonuttjEKhXqiowdAI1AQdzPEocgOZ6p_9KZPH7-PAOwKGRDtoDliO8fo05b-qPiYm4tqMt8MqbWfZXDtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41ff96b40d.mp4?token=nK8ZU6cSNTxxgG5zyXfeN12rd0cTAD9UHY5bUDLVRaOuCoij4tSiSErzwSkXusgtSgvXxdBl9Z5v_HzSwbMm0jDnHvQ6PzrbZ3ncHp5jA1jn6iZeNFy4WOx6Cq9tMx5yJCe2zYLm_ChIw10lXNC5J5NwY0nbRi6Dd0BrxNbSH1nQlh59iQernTshMK8lj6dsSkri2VT2ZEjjzhjPgLluV-MEJ9wwTYHJVkHYML37pqa-2LFmA6BFTMFrH7NZcGaZSP5aDonuttjEKhXqiowdAI1AQdzPEocgOZ6p_9KZPH7-PAOwKGRDtoDliO8fo05b-qPiYm4tqMt8MqbWfZXDtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیوهای وحشتناک از انفجارهای دیشب در اهواز
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/alonews/137158" target="_blank">📅 11:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137157">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
انفجار در بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/137157" target="_blank">📅 11:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137155">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J3Kd4q07aJAohdA6eP8RzK53oKxKT9oFC4GBgd5UgWIAEu5zEwBiUR0uaa3QN5xSGUANk6rObbIk4xnS2ewFVNzXA1Vdh9uRoo86OmaXdCxTPoH-enF6Htgq3Z0pOYDkEKmZL1NQ8LMFSXlKoLDl2rqMOx7VMhRsGOzYgmIZh7AJPuRRLAy5Vx1wFLBtBldlYeHmP_z5-oXT1tqC79nsiee-noLkPFYytpEz3Jj82TfQqa-KgJIoeMGZBKliEDRlEbBDQCfUXcOmDoFzh3gwrSYtnuLzuMu9xSoVQUvNQJZGYNV2QeNBVEU4kRDmqT1oNT4m9WZiG_TmCoKGLc5Vhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kdYKeQS3MuNP4369i_0poqb4mEV60hTMEjC2WySnBs9vL2PFH1EbjdyE5hubzaKTzkDV5QmpTBbz66Zq16TPAgsM8MQD0FppEDdiTVfkHV5cwNHnK_bHDjHmPtVw9ddjL3NaC9ABQNPDjN4ft57tKgdLzDFy-6pCLp6kQJcBKJBhie7QAaarz05YxK7D_NUgOjcDcu5VwJDsyVnbhAHAzZtbFxsy2KQCIbAXRbl9xvTKNUW3zXt3vPdxWZjjDdYs9eysZBI4x0dsl8MG0boYpmseGL-j2GV4pokDeHJJtwDpecZjVEeB7_GqImct0cX1m4M4fEtVS1RWil8lOg8Dtg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای مستقل Sentinel-2 آسیب به مرکز داده Batelco RJR در منطقه عسکر بحرین پس از حملات ایران را تأیید می‌کند. این مرکز که از زیرساخت‌های مهم مخابراتی بحرین است و بخشی از سرورهای AWS را میزبانی می‌کند، آثار متعدد اصابت را در تصاویر ثبت‌شده در ۲۲ ژوئیه نشان می‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/alonews/137155" target="_blank">📅 11:36 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137154">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
شمار مجروحان حملات اخیر آمریکا به ۶۴۵ نفر رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/137154" target="_blank">📅 11:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137153">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
هواپیمایی قطر پرواز به بحرین، کویت و اربیل را تعلیق کرد
🔴
خطوط پروازهای مسافری به بحرین، کویت و اربیل را تا پایان ماه ژوئیه جاری به حالت تعلیق درآورد
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/137153" target="_blank">📅 11:28 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137149">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hmjQsm1WougwxNlB52NjE3LlNXuApzUgkauy_YEsokWtOyWYrwaETCbFT_tOGrVpQ6n2Hh36cyqyaTPpW2eQI674m4Wvr4BU3tVtTmtwZGHt7_k7gsqVtA1EBZ1nnlX-IXOgrP2wK_dcjRRq48RGdV2VIdKo32Q9qrY1fZ1EYOd7RqAQV5D3_6cQYqqD16JLLEx8WFyKw80U-O0DJZnwRSHrCw-N8ZZEJqHb8g17YHbtsuKvXSwpjzKBzIXDM0KxDGXoEpzksiFXfg8SVtPlSoq5iJ-T3OM-ACA5yD2hEqERMzfrrI9m1tgAD8ay0jEBE_MbgQ_Yy_dwsVEpvp_rbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ciDXDa8F6_KDnXwc3NU2_gJBFRpnkqMRJY-GGNpflMuiGX9cZM86R0Nf9RzayH9OzGhGsDOYxtK1cAAHgHqAG8goE5_tRSerWEzXO4aH94cBCiF0NtwsOkK1_oVIADjff3XAjzZKt8HzuhFvbhw534rUNrBWAGxPX3q9f8ecYDxa50DZIyh46O5Mm1QCt5kPg1LHD5vKXvdUX28vC5y6E0MM1k_aW5ZskzF_ehd0ihBov3ZgqpTRByUOoyhGPlf2GNeNjCIj3wdCSbufAi2kGxtmErloyhFLinVFJ7Kw7oCHmlAMzu4FEy-6Sc7eDL3eNAs7hIYHRjHKBOtnXhIJFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FMNkN96AKePoM7EHn9TyVjBXMj0efd0InSqU1xr6q4jncY1goRFmNkEgLQWp2BJGREPjBQIjBNvvRF3ZU2XTIg7twsc742X4NKEgvYx91HXIJvTuwd4HZYXp296C46_SyNk2tdN_6sZGVmjJArJ8PNMLfMUuwgf-t5HQnnTPlHzR2sn5iya4HIf_b2Gj_4wP38OaoB7xnJUO4ph1LwJiZfAyZJiDid_V5pIioWqXccnP1Z-Udwpa4ImQ81xV4hKSQ2eH96lX2FPVxf1iC_bJNfaz2gwxGfVIDisXqC1NdKeel-6cHsS8lK2U-5RwAay8lbgwW0MnuKFNxzfSnke6Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U4ro9UitdepW-7RZTW69u_5sY4VGv5xm_IbhlZRAV56-QAx6RWYcOjwR7O6UXeB3WKxpzQNbZ6X2_gU6nPDY7mLFp8TjSDYqDokGAVXJPwC0a6-bUft0N62jUXbtBt_aP0_HBIMWL3PWpCUWtqyY-v0mJcA-5tGBOaRXo90QHBaPevSXXwbZ3r5E2jL4FRNpLR31PD0i01S6jdRGfO_lB0t2yih_CwQLXyySDtc7NCEB3ULfRwsCb4_SrLjPEgIbpO2fkC5asoZYAcnxElT_3SHJLXkL0V1eJUhwbSYjaowrB0tGoFL0J_8oGVHPLEAXWpxUyFVvG1kA05mgKNLLEg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تمرین آمریکایی ها برای مقابله با ریز پرنده
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/137149" target="_blank">📅 11:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137148">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
صدای انفجار در بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/137148" target="_blank">📅 11:16 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137146">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5552f9e237.mp4?token=YWToalxbz3lCdhcsIGF-GpEKPbAHVs2tI6fPGvFZ089p5S2pnwEqvBdfXKdF9Grog5AhpIbsq9LdqGRZV1CFhXrjRXHgu5MZ2N4PQVOf3SA7pZ3bcDJCJQq4OL_mt1UGcDHOcLI68ZnjvmQYvG0OJVrKSfoArM4aAywkLFi6lbl-ltQMRQuvIUQkPRdQbKjJM_ye44sT4bZnKQ7evJUmq5g_6j2oU3MIFAp0Mp2Hp8356viL8fEZAa9Pl8b0NssVQrLiCkbrIwhU7THslWVmSZJGIDXO8xDasae6q9gzrppZbr9Ae71eE5AIcoQLM11phyQr31H_zNJQTeqIOPBr0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5552f9e237.mp4?token=YWToalxbz3lCdhcsIGF-GpEKPbAHVs2tI6fPGvFZ089p5S2pnwEqvBdfXKdF9Grog5AhpIbsq9LdqGRZV1CFhXrjRXHgu5MZ2N4PQVOf3SA7pZ3bcDJCJQq4OL_mt1UGcDHOcLI68ZnjvmQYvG0OJVrKSfoArM4aAywkLFi6lbl-ltQMRQuvIUQkPRdQbKjJM_ye44sT4bZnKQ7evJUmq5g_6j2oU3MIFAp0Mp2Hp8356viL8fEZAa9Pl8b0NssVQrLiCkbrIwhU7THslWVmSZJGIDXO8xDasae6q9gzrppZbr9Ae71eE5AIcoQLM11phyQr31H_zNJQTeqIOPBr0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پهپاد شاهد در کردستان عراق قبل از اصابت مورد هدف قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/alonews/137146" target="_blank">📅 11:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137145">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
پرواز های فرودگاه اربیل تا اطلاع ثانوی به حالت تعلیق درآمدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/137145" target="_blank">📅 11:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137144">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d440c579ec.mp4?token=ROrr_PXNFEmNw7Ry61xEne8NJz03qFTtn34p43aMc3-rjl6eRPVPEAGz95bAGaHstI2lW-Z77SFxBh6wAbICDXPH9R9lZFgl0KqhI9ZqooB65i581zx5MV_KrXMkjl75HsGj4hgS_h8Am5o4hg4vz1wMIyZcia3FCViF5O4UraZrbmMTAh--_vAv9qB8MvSbLHoWJgQSitv3UnPJrVhmQtvNVj4hISLpxTyZuUdIJ0JwHmO2bf_HISa6HkA55GLQboYNatKh5xDV7dgboDWEDcUEzom6wM6UjRcIKJPBHms-yCmpWT6QLjt0gD6iKBgwn2uXRW7ojllD0H6V8ml_5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d440c579ec.mp4?token=ROrr_PXNFEmNw7Ry61xEne8NJz03qFTtn34p43aMc3-rjl6eRPVPEAGz95bAGaHstI2lW-Z77SFxBh6wAbICDXPH9R9lZFgl0KqhI9ZqooB65i581zx5MV_KrXMkjl75HsGj4hgS_h8Am5o4hg4vz1wMIyZcia3FCViF5O4UraZrbmMTAh--_vAv9qB8MvSbLHoWJgQSitv3UnPJrVhmQtvNVj4hISLpxTyZuUdIJ0JwHmO2bf_HISa6HkA55GLQboYNatKh5xDV7dgboDWEDcUEzom6wM6UjRcIKJPBHms-yCmpWT6QLjt0gD6iKBgwn2uXRW7ojllD0H6V8ml_5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
انفجارها در انبارهای کنسولگری آمریکا در استان اربیل، شمال عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/alonews/137144" target="_blank">📅 11:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137143">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
۲۵ سند در قالب ۹ تصمیم در پایان نشست وزرای خارجه سازمان همکاری شانگهای به امضا رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/137143" target="_blank">📅 10:57 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137142">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/B_8VpBfF8O0lxn3ObZPSYh7GUC4TIfaRKOdBItpSf6yAp3RYrlJi2e4od6zikLQUOImJkGQL5HKSMcClo6Y6p0s8w6KFTwxZfVSgeHu0pY6tuFTSBaxh-Cu9V3Mj7857RIRyVKEZlfR42pTx3qKkNzYwi3OEIB2Q1cov669fORUS0SnrLiDF25g3MZ5Mpqn_RDrhf-7QsmQ5BOfvPx7N7yy_-D9TQrJGkwWHm_4nriM2XxRblMfL75-iQLlUdkT58fpjP5HvSn_mzUG_QufEKBhPWNqPGDcXlqWiJvSOO_J3O4dWWSXLwE4NChQ9afqDU0pKnkWa-SuPB-P2ZD8Y7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله دیشب ارتش آمریکا به یک سوله ایی در نزدیکی اهواز که از قبل منهدم شده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/137142" target="_blank">📅 10:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137139">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mpsaOCVc5sqeCMCSIlaRzCJMNLGaroImFmnqLXwyutq2fMOltUzjImFOgf6Ml17oX2FJrMJbEIKhQyfxrevJmjXjC_oT4MIO8PugXak-qc-kFyLPOVxpdpOJqBQOdGR6IgmTWpow3aE64oSDdYsZ8FwSvGfv3emZJsdNLn8nE4ud2cIsEjEnxbwo1Jv9VPzgNxUY6CkqzWmia0fLyPQlHQXnH7sKZ2dFgKP5L8K3FFZI6vgtLjMRIVw-H0sklw-7EOQFBxojw6hvx8BUO1BBdZ7bifDLdVygFVxvx8QPFD9oQs1tItX9WexXjUTjoUfRBfDV_UP9ApoO2uc7u7N_oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pIwVGoWaj97oWeFzfEYXPOrpJ0_xkRP7BjG_FyDSX0VkEU2rn4mGghD9pSdBJQgOcyCIb7SKHNZYS2l53nKtCWX04T7y15UAxRy4jvmkTPeEhDslEZ9VMFBN03y13MnV6XD82YoZUnlUW-qUZRv30UHHIwZDYtiGcoETZXM7sEg0Ers-iTwRRE1nsT7Tk1LOx40LXlC9pwRE1nDzS2zDSaFSbeUP0LcuUeLDorDbyBCJdJ0M7ZANW2-w72eKkhG08nCEqJ6UlB2uAHucNAfPooxRT2XIRj3PXoKzPZ0jvhn_Rjuozl2HusH_6zJhkHEqK1DzZczIT6gnCu1BUTl1Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ujmN5EknypubzxDuS40D81KBckj5NCxk-aBnIzMcm6bX0ADLFlkQp0GwdNMPNvpd0jUrENGtc7VjBwgbP9l13LyMVk3WRjo3O48ZNdLi0SGur8miLpOexJX2q7yV-HeJRewCWP2oIrEdXApH6kp_dc1cMljE0-kTokQRGBBLsMK9KPCrjbkJEBRGOafIzYVPtOW_QKVgjRArZL4qutjSOkXpnrqG3XRCmow-JxvBv0aCGu94__hIWEk7slv5cwz5NQEetgXD2BC4Ytgp6-CDBqw1y81Stw3oWm9lQYdb3TYrCR0F8VQQ6-4drgLQgEVNRxjMuQoyvAruhhIYFcmk1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
استانداری گیلان: حمله موشکی آمریکا به مقر نیروی دریایی سپاه در زیباکنار
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/alonews/137139" target="_blank">📅 10:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137137">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81df070eb2.mp4?token=Hl1Y24m4AFrXSnqONfN3iRMK_pJnaducwD2JHJrDJKyRweXMXPkXnUfSc8td8X-jrfhgRKnLLvBTC4UKRXZ5Hmb34Dw6PRfAhZsXtKp1A5T9ptNGuVE1EG_MhlCuqDR70TFH-_9EogiXmw5LU_YWsxhThndME5sSVNozAcrBSHFuSV0H5DVi7vSCl8QsIK91yZ2GiH3EmI1rlnBj5EFBja-ob64zyPiSqJ7iBqOjJBcQgjpG3CI3juV7m5wIFeY2vEPad4NOjqd6f__1IWneWSCxpoAkRCok_Mi3JLc-RzSTaeYujMqlsSSdkV341XC1Z0KUcn7ilgqCWfNmeOwiWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81df070eb2.mp4?token=Hl1Y24m4AFrXSnqONfN3iRMK_pJnaducwD2JHJrDJKyRweXMXPkXnUfSc8td8X-jrfhgRKnLLvBTC4UKRXZ5Hmb34Dw6PRfAhZsXtKp1A5T9ptNGuVE1EG_MhlCuqDR70TFH-_9EogiXmw5LU_YWsxhThndME5sSVNozAcrBSHFuSV0H5DVi7vSCl8QsIK91yZ2GiH3EmI1rlnBj5EFBja-ob64zyPiSqJ7iBqOjJBcQgjpG3CI3juV7m5wIFeY2vEPad4NOjqd6f__1IWneWSCxpoAkRCok_Mi3JLc-RzSTaeYujMqlsSSdkV341XC1Z0KUcn7ilgqCWfNmeOwiWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از محل برخورد پرتابه در نزدیکی فرودگاه اربیل عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/alonews/137137" target="_blank">📅 10:29 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137136">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
استانداری گیلان: حمله موشکی آمریکا به مقر نیروی دریایی سپاه در زیباکنار
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/alonews/137136" target="_blank">📅 10:22 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137135">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/314e4b0791.mp4?token=q86rNIlDOgZ50onlH4ypRNXfba52_drO6iKbDwfvlkL9zU02HXFgjgHrH68pGpY1f2StLGfo7EYSBSGXK7XJr0P6qSiww1x8Tw-RNoPouL082YOSHi7UoCtsSGcmda_VdIh4wKU4b1ySMaaMJ1_JM7v7pBbzloh35xU46rtVoEwYfFi0TBxC3SVDhjJTyiJnH5U97QZWZmATPdjmUfudn7nWzhNjiPJZJ_CbcbmTNJUUQsXQt6tFu6qwOf9etDsP1gh8tSHYc-WkkgCZ7BnjCXtjYCTKBvCQUgOotDinzK8tYfyksyQeVYx1iljA05zHBq1lNoNtO_NnHwOFSqSv-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/314e4b0791.mp4?token=q86rNIlDOgZ50onlH4ypRNXfba52_drO6iKbDwfvlkL9zU02HXFgjgHrH68pGpY1f2StLGfo7EYSBSGXK7XJr0P6qSiww1x8Tw-RNoPouL082YOSHi7UoCtsSGcmda_VdIh4wKU4b1ySMaaMJ1_JM7v7pBbzloh35xU46rtVoEwYfFi0TBxC3SVDhjJTyiJnH5U97QZWZmATPdjmUfudn7nWzhNjiPJZJ_CbcbmTNJUUQsXQt6tFu6qwOf9etDsP1gh8tSHYc-WkkgCZ7BnjCXtjYCTKBvCQUgOotDinzK8tYfyksyQeVYx1iljA05zHBq1lNoNtO_NnHwOFSqSv-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هم اکنون حمله هوایی به اربیل عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/alonews/137135" target="_blank">📅 10:17 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137134">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vgz5XKHQlpm3eCk_I3s2xwAE0SyPWwEFhJYNzNTpJ4x-UiV-TWsqbrqgKBV-LqYvfK1oZG_HHJE3QLWvITD5c1fDuzq-iwem3_0HU3UHgHNG40wQp_J_HXd3Gp3YnS4kpJTV1l_WpGhf6UKMSTAM4G-y71J_A6cSPGf23RYsnxKzE8H4KChCwFtXI3f8FJc0559l8lP6nnPkvtOy74wix9kY3OopkLAppf5VzAbkckWaRY3EGHUuGefXNJLjhEpw02UVSos_llu1pcV9QUWmVC8E4LQnS3pdwTfnWqBUcuPNMt3j-ItpN5UY7WsTHep6yCv2mTFQrxKjgIOBYA6ckQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
۷ فروند هواپیمای سوخت‌رسان دیگر آمریکا راهی خاورمیانه شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/alonews/137134" target="_blank">📅 10:06 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137133">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
نیویورک تایمز : تهران در صورت عملی شدن تهدیدها تلاویو را هدف قرار میدهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.7K · <a href="https://t.me/alonews/137133" target="_blank">📅 09:53 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137132">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
روزنامه نیویورک‌تایمز در گزارشی مدعی شد دونالد ترامپ از زمان بازگشت به ریاست‌جمهوری، درآمد قابل‌توجهی از سرمایه‌گذاری‌های خارجی و بازار ارزهای دیجیتال به دست آورده است.
🔴
این گزارش می‌گوید: افزایش دارایی‌های ترامپ بار دیگر این پرسش را مطرح کرده که آیا او از جایگاه خود به‌عنوان رئیس‌جمهور برای افزایش ثروت شخصی‌اش استفاده می‌کند یا خیر.
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.8K · <a href="https://t.me/alonews/137132" target="_blank">📅 09:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137131">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
گزارش صدای دو انفجار در نزدیکی پیرانشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.7K · <a href="https://t.me/alonews/137131" target="_blank">📅 09:42 · 02 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
