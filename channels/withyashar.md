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
<img src="https://cdn4.telesco.pe/file/OG_0QGB-q0_5h2KKxyGgdJHPW9qpbzqgQPFjMQt1V7slUm7EIR5YEksDuUeyStZY5mjhGECw_N0PoF2gPWvX60rKcPIsqck1wGSV7Qz7YTRToZZGS7OBwToqUM5F0skSdOC9rBFaUQZWV5uwBzK1GQgWIBtu7iT-7BeLMU_8tGLAoezvZP-r2SY7zlXLO0KSsMWO4Sgo0Ofcw_gptdU4zLFNyWCm_4gqD2Yill2KKgTNhmwvNZD2pEJ80LfK3iEwx6aSwiv_0DzvLIERLhtuq7ITRu772-yZ7vRsifhEPsE_REuVmh-z9iA0wtOOVGtuDGXmciJn5lbgZgz3Yyv9iQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 358K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-18 22:35:41</div>
<hr>

<div class="tg-post" id="msg-17188">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">تحلیلگران رژیم
: احتمالا حملات امشب کار کویت و بحرین است
@withyashar</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/withyashar/17188" target="_blank">📅 22:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17187">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">العربیه: ارتش ایالات متحده مسئول حملات اخیر در ایران نیست
@withyashar</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/withyashar/17187" target="_blank">📅 22:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17186">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">اتاق جنگ با یاشار : میپرسین بگم که ، نظر من اینه که هر کی هم بزنه بدون همکاری اطلعاتی و زیرساخت جنگی امریکا و اسرائیل و کسب اجازه امکان نداره بزنه… پس در نتیجه چه سوألیه
@withyashar</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/withyashar/17186" target="_blank">📅 22:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17185">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">کارشناسان تلگرام : گویا حملات از سمت کویت بوده
@withyashar
😁
🤒</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/withyashar/17185" target="_blank">📅 22:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17184">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70d6bd72f1.mp4?token=Ib6o9t3DginCevxYp3wJoDGgaaMeKec3faVgSEasp9lLMSCyZGT7GMdQ00ATpYTnSJAdBckvwOt0OZ5ysi4cYjNzBHchdCcnxL0GflpS7hVl4w0pYpky7eR1s5HQ38KCSO5EdA_navGCC-AcgB_YHiSKOxhCG_2zeKAXrJ5LXS3lqXNP4hMMGFxqxOHfT53_epG6KCrGoF9RdHj2qQ4u0MRkWLQPO91MlElcMGPSXGXsB-mWwS98o6xqnBZeZ0ALtr0UfgS-rHQMH-NCMKupco90b0h1GP5p_iv2z9TI9lVmTppO1QvqIiM3pJIML1Z0eSC2q6y8oWBnDNaySfIX9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70d6bd72f1.mp4?token=Ib6o9t3DginCevxYp3wJoDGgaaMeKec3faVgSEasp9lLMSCyZGT7GMdQ00ATpYTnSJAdBckvwOt0OZ5ysi4cYjNzBHchdCcnxL0GflpS7hVl4w0pYpky7eR1s5HQ38KCSO5EdA_navGCC-AcgB_YHiSKOxhCG_2zeKAXrJ5LXS3lqXNP4hMMGFxqxOHfT53_epG6KCrGoF9RdHj2qQ4u0MRkWLQPO91MlElcMGPSXGXsB-mWwS98o6xqnBZeZ0ALtr0UfgS-rHQMH-NCMKupco90b0h1GP5p_iv2z9TI9lVmTppO1QvqIiM3pJIML1Z0eSC2q6y8oWBnDNaySfIX9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهده لگو غول‌آسای ترامپ در مشهد/ هنوز مشخص نیست این مجسمه با چه هدفی ساخته شده است
@withyashar</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/withyashar/17184" target="_blank">📅 22:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17183">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">اکسیوس: یک مقام ارشد آمریکایی ادعا کرده است که ارتش ایالات متحده در ساعات اخیر حمله‌ای را در ایران انجام نداده است!
@withyashar</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/withyashar/17183" target="_blank">📅 22:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17182">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">آتش‌نشانی اهواز : انفجار ناشی از نشت گاز شهری در یک ساختمان مسکونی دوطبقه در منطقه حصیرآباد اهواز است @withyashar</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/withyashar/17182" target="_blank">📅 22:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17181">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">در‌کیش‌فقط صدای جنگنده شنیده میشود ولی هیچ خبری‌ نیست</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/withyashar/17181" target="_blank">📅 22:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17180">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">من هیچ گزارشی از قشم ، کیش و ابوموسی ندارم. نمی‌دونم چرا همه جا دارن این خبر رو میزنن. حتما اشتباهه.</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/withyashar/17180" target="_blank">📅 22:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17179">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">گزارش انفجار ‌جدید بندر عباس @withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/withyashar/17179" target="_blank">📅 22:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17178">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">صدای انفجار‌ جدید اهواززز
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/withyashar/17178" target="_blank">📅 22:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17177">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">شنیده شدن صدای ۲ انفجار در بوشهر و چغادک
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/withyashar/17177" target="_blank">📅 22:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17176">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">گزارش انفجار ‌جدید بندر عباس
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/withyashar/17176" target="_blank">📅 22:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17175">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tHTxA6co9uk_zry5mTVcetGfNf0BGO2g54RjBx8ZPLlymtV_ywlUAstAIxtqoJ8QOhMkQwLVN99G1TJwEPcQt1PJUeehNXhoKcskjGGiQ4qL6HiFdUGWFmhQTcrZIkOOUxF35vcPA__FYjPNBHdB6M3ixefmOa5qYngA8pGmDDXJZI1iEBm0k2Cb_lAL6-nk2xxl6i7imcoD0KgH2y0vqZdwpk34AvuU50qnIisF92XGHnCTeAwJW6qPfXabg1EoMpFe5KXl2Rwheg-1MsIWG3ctONwabVpIOAhwQGvvFyN6xbA7At_N50LmA24BZHkquZOpF5CdWRcD6JFAGK7BIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسر بزرگه داره نماز میت رو اقامه میکنه
@withyashar</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/withyashar/17175" target="_blank">📅 21:55 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17174">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">گزارش انفجار‌ در اسکله چابهار
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/withyashar/17174" target="_blank">📅 21:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17173">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">مهر : شنیده شدن سه انفجار در کنارک
دقایق قبل سه انفجار  در کنارک شنیده شد.
از جزئیات و میزان خسارات احتمالی هنوز اطلاعاتی در دست نیست.
@withyashar</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/withyashar/17173" target="_blank">📅 21:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17172">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromM M</strong></div>
<div class="tg-text">یاشار من بچه اهوازم ، اونجایی که خبر دادی زده ( حصیر آباد ) دو سه تا دکل مخابراتی هست که روی کوهه ، احتمالا اونارو زده</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/withyashar/17172" target="_blank">📅 21:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17171">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">آتش‌نشانی اهواز : انفجار ناشی از نشت گاز شهری در یک ساختمان مسکونی دوطبقه در منطقه حصیرآباد اهواز است
@withyashar</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/withyashar/17171" target="_blank">📅 21:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17170">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">اهواز ارسالی :ماشین اتشنشانی و آمبولانس زیاد داره توی شهر میره به یک سمت ولی نمیدونم کجا میرن
@withyashar</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/withyashar/17170" target="_blank">📅 21:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17169">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">گزارش تایید نشده انفجار در اهواز
@withyashar</div>
<div class="tg-footer">👁️ 71.9K · <a href="https://t.me/withyashar/17169" target="_blank">📅 21:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17168">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28fdd7b746.mp4?token=gC7nM-8k_ajSQ9BHOdOa8Kz38fVQFGRcs3p4fwGVDQlqZAiaefnDBVsjZxIvtNWeSdkbUO5fluQHGS7JXTeWkNGplEpB-hpcszXW1tWTRJtjNpw2wSy5oLucl4Uy85IuS7aTvAjIDRCyH2R4sK_dY3GLJ0fvD8tzpchLiKErXQ87q7p0y10T5eO9gafSYsePqtfhlLTkk5ioO6n6Xgrt0re7Vlbxe719GsxFONST1Vgc0D0E66MIIeS7f5Xbd1HAczw7zHuJzmO4O0O7EbkKLhZy6vXUu7SYz_1AzGyVx9AnCCFJFBf1q8t2jP_3k30MXQE-_ZgpRD3eyay3T4dQeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28fdd7b746.mp4?token=gC7nM-8k_ajSQ9BHOdOa8Kz38fVQFGRcs3p4fwGVDQlqZAiaefnDBVsjZxIvtNWeSdkbUO5fluQHGS7JXTeWkNGplEpB-hpcszXW1tWTRJtjNpw2wSy5oLucl4Uy85IuS7aTvAjIDRCyH2R4sK_dY3GLJ0fvD8tzpchLiKErXQ87q7p0y10T5eO9gafSYsePqtfhlLTkk5ioO6n6Xgrt0re7Vlbxe719GsxFONST1Vgc0D0E66MIIeS7f5Xbd1HAczw7zHuJzmO4O0O7EbkKLhZy6vXUu7SYz_1AzGyVx9AnCCFJFBf1q8t2jP_3k30MXQE-_ZgpRD3eyay3T4dQeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اشیاء ناشناسی در آسمان جنوب عراق مشاهده شدند که به سمت ایران در حرکت هستند، اما ماهیت آنها و اینکه آیا موشک بودند یا پهپاد یا دیگر، هنوز تأیید نمیتوان کرد.
@withyashar</div>
<div class="tg-footer">👁️ 71.9K · <a href="https://t.me/withyashar/17168" target="_blank">📅 21:36 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17167">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">فعالیت پدافند  چابهار
@withyashar</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/withyashar/17167" target="_blank">📅 21:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17166">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from♱ ᴀᴍɪʀ︎ ♱</strong></div>
<div class="tg-text">آ‌واکس
❌
یاشار
✅</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/withyashar/17166" target="_blank">📅 21:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17165">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">تو نوار ساحلی میرم میام هرچی نفر اول بگم</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/withyashar/17165" target="_blank">📅 21:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17164">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from۞۩ ¥𝕒z∂𝓐Ｎ۩ ②①:②⑧</strong></div>
<div class="tg-text">تو نوار ساحلی میرم میام هرچی نفر اول بگم</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/withyashar/17164" target="_blank">📅 21:28 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17163">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">پدافند بوشهر درگیر شد
@withyashar</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/withyashar/17163" target="_blank">📅 21:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17162">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">دو سوخت رسان از رامون و بن گوریون به سمت تنگه هرمز به پرواز در آمدن
@withyashar</div>
<div class="tg-footer">👁️ 76.1K · <a href="https://t.me/withyashar/17162" target="_blank">📅 21:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17161">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PtbTiFWp6MGVzvJTF7BnSc3-AmyX41ZSCW-f-6yCS_Ebs2Exyv7XJ1ny6Xd_wS3lZWLVffcYn-2nNrWhqOM0eEWUVkJ42_Gydq7d1v74_I3DdL_DoVxi9iNjNFwwhsB-wQKijjaMKilxjNeUwd4BlRpClJPrrjYqaJS9D_RbH23fTZZGL0NluN23TkZx1QnnTtnMhlEjwBYbo1XbNwLyJck3WPnKwSHupv0F8fc4rWH8nC-mFFi0B7w5Nb74uoY2a8ypfJX3KIatyaQKg-wDY0FaMJRl_zMDHf_85B5kRge2WfkmdDReA7JXy_G-HTYECCMntU_BEjlUdEA1TYa10Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همین الان پدافند سلمان حاجی آباد هرمزگان زدن
@withyashar</div>
<div class="tg-footer">👁️ 77.1K · <a href="https://t.me/withyashar/17161" target="_blank">📅 21:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17160">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">گزارش انفجار چابهار
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 77.1K · <a href="https://t.me/withyashar/17160" target="_blank">📅 21:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17159">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
شروع شد</div>
<div class="tg-footer">👁️ 76.1K · <a href="https://t.me/withyashar/17159" target="_blank">📅 21:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17158">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">اتاق جنگ با یاشار : کاهش 5 درصدی نفت جهانی  با وجود درگیری سنگین نشاندهنده بی تاثیر بودن حملات ایران و استراتژی درست آمریکا میباشد.
@withyashar</div>
<div class="tg-footer">👁️ 78.1K · <a href="https://t.me/withyashar/17158" target="_blank">📅 21:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17157">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">به گزارش شبکه کان، مقامات ارشد اسرائیل تمایل دارند تا مجوز لازم را از رئیس‌جمهور ترامپ برای از سرگیری حملات اسرائیل علیه ایران دریافت کنند.
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 82.3K · <a href="https://t.me/withyashar/17157" target="_blank">📅 20:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17156">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sA_fVsG-moBfkYqzYBW1X7jGOsh2V2LMiWoUrCNlfNMD61CYtPLaubY6bbCRrZ_f-lLSZtaf4-X_ifgr2nB8oGVKR97Qs0greJimvXlhLKoMcvjzanjytrwT5dMll2iCpAdKke3T6d40tXorZx6Uu0XUzA4E6rG-6aMLiQudG_EcsnQBIU-BUnMsxZa-jFzzWc2oyRtMK6Olnvy0qijf8VA1mdVaGWvGYhcpz4YjWAgnQVLfkyUfUwUySmk8ilq7XgYc59wJxr-BL9cGmSBA1zuR6o1JUOAqlkbnPdzUzjtBS7Wa8lHMevkoorCMRKNGTkTzQA612C9DHU-NjP1FfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داره شلوغ میشه …
🚨
@withyashar</div>
<div class="tg-footer">👁️ 83.3K · <a href="https://t.me/withyashar/17156" target="_blank">📅 20:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17155">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">سلام  امشب هم ردبول بزنیم؟</div>
<div class="tg-footer">👁️ 78.2K · <a href="https://t.me/withyashar/17155" target="_blank">📅 20:54 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17154">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromFarjam061</strong></div>
<div class="tg-text">سلام
امشب هم ردبول بزنیم؟</div>
<div class="tg-footer">👁️ 78.2K · <a href="https://t.me/withyashar/17154" target="_blank">📅 20:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17153">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ارسالی : حمله آمریکا به اسكله صيادي بنود در بوشهر خدا راشكر خسارت جاني نداشت ولي خسارت مالي حدود ١٢قايق صيادي دوستان اتيش گرفت @withyashar</div>
<div class="tg-footer">👁️ 78.2K · <a href="https://t.me/withyashar/17153" target="_blank">📅 20:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17152">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/231716a55f.mp4?token=thsw_LwL0ertzRjKSRghvmh-9sQBmgxe4WK824XgN-4ImIUNKMzFjrIsF9oUykUl9n3LmYkZz9UWUeVv7x-tceg4aZro-FnL6373ySQ961LLycQO7e16wBKs1LoLjuWBeZH-pYNEN7oF7x2XGz6svW_TFjhKxqCIWvSN-eb96vp2h5-K-Gf0xzVUrsAnNIo47pwFBnhRm-uW8duSP8wZeqe4z5iL--wf-9teTO5jIY-ax1-GHDQ2aTBHQ43Ht32UMB5LymNKh7VgdNQG1K8plmznivcRCLVpZd3xeYwFl4sUjT262Q3Zkcag4n82nChqNysPAkDBOVAU31olW9gn1CaYJu69K4dcr1PGDLWHJ04-blG_-UtGwwGw8V__5TXe0TAhT7d-Et8fmOBmtBLK2h4QGKybE5kPpEDomiQPh11MvXtA1DaJLwVbxyz5Ihu-asPZLg6LUkG7jdSA19IZYEhVUWtHniDir5WlZIPLQSDPzn6ChfVFNYOGg7mT0PZblwkRLvqiTDzVO1jZdtmAGp-vL2FzYjAepI5zV2h2aYYTE6l0EeFvlQt3hlsC-li1f3cjpFAdyyrmWYtNG-p_UKbDLSGBIi3AY_VER2lzlew-scDPomuznPD1LP59Z7kWI8Dmgx8ifTGQx3HMe5GtHmPYH62sk_d8PX37YI63PKU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/231716a55f.mp4?token=thsw_LwL0ertzRjKSRghvmh-9sQBmgxe4WK824XgN-4ImIUNKMzFjrIsF9oUykUl9n3LmYkZz9UWUeVv7x-tceg4aZro-FnL6373ySQ961LLycQO7e16wBKs1LoLjuWBeZH-pYNEN7oF7x2XGz6svW_TFjhKxqCIWvSN-eb96vp2h5-K-Gf0xzVUrsAnNIo47pwFBnhRm-uW8duSP8wZeqe4z5iL--wf-9teTO5jIY-ax1-GHDQ2aTBHQ43Ht32UMB5LymNKh7VgdNQG1K8plmznivcRCLVpZd3xeYwFl4sUjT262Q3Zkcag4n82nChqNysPAkDBOVAU31olW9gn1CaYJu69K4dcr1PGDLWHJ04-blG_-UtGwwGw8V__5TXe0TAhT7d-Et8fmOBmtBLK2h4QGKybE5kPpEDomiQPh11MvXtA1DaJLwVbxyz5Ihu-asPZLg6LUkG7jdSA19IZYEhVUWtHniDir5WlZIPLQSDPzn6ChfVFNYOGg7mT0PZblwkRLvqiTDzVO1jZdtmAGp-vL2FzYjAepI5zV2h2aYYTE6l0EeFvlQt3hlsC-li1f3cjpFAdyyrmWYtNG-p_UKbDLSGBIi3AY_VER2lzlew-scDPomuznPD1LP59Z7kWI8Dmgx8ifTGQx3HMe5GtHmPYH62sk_d8PX37YI63PKU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سناتور
جیم بنکس: جمهوری اسلامی در صورت ادامه نقض توافق با «جهنم» قدرت نظامی آمریکا روبه‌رو می‌شود
@withyashar</div>
<div class="tg-footer">👁️ 81.3K · <a href="https://t.me/withyashar/17152" target="_blank">📅 20:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17151">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tUZrONEuGnHHY9naGw85JwkF_2e1ri1jRRdtJ4FhDuut4fSghyKCtb_ouQ8LS7w7EDst7JM4N2cplTp7B02zRSJ4LxpCdnXPrLGtBdwj4FbGYiVwRyIZV2J9IIwkUF_nA2WibXslWcPSTAvpWvineW0XGB4blvKs-z1BLVQ6-nh1Jq4HQgjvNF4gDEqNH9KIV-niQs24goluNh-YZHdh3j4DwgE2ogbGaFVFGiQYttaCcIxX4R6m34J6p23Z5wcNDHvdbjFK68YzFE3ipmoU--O_qk1Fuw3ABUfT4j85WGjXJhhIMnRXw1e8XEhe2WUNUhEKyoVHqV_o0XRSKKnBFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حازم قاسم سخنگوی حماس در غزه ترور شد
وضعیت کنونی وی وخیم اعلام شد
ه
@withyashar</div>
<div class="tg-footer">👁️ 81.2K · <a href="https://t.me/withyashar/17151" target="_blank">📅 20:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17150">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">الجزیره: سپاه پاسداران ایران یک مرکز فرماندهی آمریکا در غرب آسیا را امروز هدف قرار داد
@withyashar</div>
<div class="tg-footer">👁️ 84.4K · <a href="https://t.me/withyashar/17150" target="_blank">📅 20:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17149">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">فوری | شبکه خبری ABC به نقل از یک مسئول آمریکایی: ما از دیشب تا همین لحظه ، ده‌ها موشک و پهپاد ایرانی را رهگیری کرده‌ایم.
@withyashar</div>
<div class="tg-footer">👁️ 89.5K · <a href="https://t.me/withyashar/17149" target="_blank">📅 20:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17148">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">مدیرعامل راه‌آهن: با تلاش مهندسان شرکت راه‌آهن در کمتر از ۱۳ ساعت پس از حمله دشمن آمریکایی به خط راه‌آهن مشهد؛ یکی از خطوط بازسازی شد و به چرخه خدمات‌دهی بازگشت.
خط دوم نیز تا ساعاتی دیگر بازسازی خواهد شد.
هم‌اکنون تردد قطارها در خط بازسازی شده از سر گرفته شده است.
@withyashar</div>
<div class="tg-footer">👁️ 91.6K · <a href="https://t.me/withyashar/17148" target="_blank">📅 20:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17147">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">منابع : پس از پایان رسمی مراسم تشییع (آیت الله) خامنه‌ای، احتمال دارد که سپاه پاسداران (IRGC) بار دیگر فعالیت‌های خود را تشدید کند.
مراسم تشییع امشب به پایان میرسد و خامنه ای در حرم امام رضا در مشهد به خاک سپرده میشود.
@withyashar</div>
<div class="tg-footer">👁️ 93.6K · <a href="https://t.me/withyashar/17147" target="_blank">📅 19:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17146">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0da60dd210.mp4?token=MFR5qcVn7G-jEBrTOphXyAtFqNw8vuA7QPWhkNejQ9NpX5y5eIc_uYmkWm8Dv0d7eNpfc1G0GvxCbcLLDuSeSGwXu1CLk5qnyfdmbmv4OKMYd6qLyjI6UxZIYLThz27Va9dpur1-0wCouYl4rxdMyEjvFQroUIFHVnPKmv9XwZqb-fUD5nwR23NgJU8wiZ3gToe3yUYlpOvwLsonld-3-rmejbSXd3HXLmtTLioULz-qcql15683zm-PkFnjBUaGZC4nPLN31lK44Is0mLkvmrmCKp_k4CNXDmzy_TjMKlfbL5XwyrfJwvzCL-Q2O3zrWP36BrkK7Bg5qZkoUxj_PQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0da60dd210.mp4?token=MFR5qcVn7G-jEBrTOphXyAtFqNw8vuA7QPWhkNejQ9NpX5y5eIc_uYmkWm8Dv0d7eNpfc1G0GvxCbcLLDuSeSGwXu1CLk5qnyfdmbmv4OKMYd6qLyjI6UxZIYLThz27Va9dpur1-0wCouYl4rxdMyEjvFQroUIFHVnPKmv9XwZqb-fUD5nwR23NgJU8wiZ3gToe3yUYlpOvwLsonld-3-rmejbSXd3HXLmtTLioULz-qcql15683zm-PkFnjBUaGZC4nPLN31lK44Is0mLkvmrmCKp_k4CNXDmzy_TjMKlfbL5XwyrfJwvzCL-Q2O3zrWP36BrkK7Bg5qZkoUxj_PQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلمه از نزدیک آتش سوزی شدید زنجان
@withyashar</div>
<div class="tg-footer">👁️ 94.7K · <a href="https://t.me/withyashar/17146" target="_blank">📅 19:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17145">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">شورای همکاری خلیج فارس
: حملات ایران به کشتیرانی در تنگه هرمز، امنیت انرژی و تجارت جهانی را تهدید می‌کند
ما از شورای امنیت می‌خواهیم که موضع قاطعی برای تضمین آزادی دریانوردی در تنگه هرمز اتخاذ کند.ما ایران را مسئول این حملات می‌دانیم و از آن می‌خواهیم که فوراً و بدون قید و شرط تمام اقدامات خصمانه خود را متوقف کند.
@withyashar</div>
<div class="tg-footer">👁️ 93.7K · <a href="https://t.me/withyashar/17145" target="_blank">📅 19:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17144">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H5fspNLHD_XkjPkdg587O4bwBOScf_1b5yiBT_s2WYWJPGXLFGLnWdJXkE2YbBot00_zFR_6zoK5tgU4Vh7wHoYkZ4bUE6d63jJjTwE_FD_YROz_Y6D_30qTzzVVCLYsPDsiomMkhBTevAE8Pz8pNz_TnDjdbrju1qTTfxqY9jG8sm2V1z9OqcJKTCrW35_9ezyCVqAgSpJQWkohP_YfFutFSKc5gOpPwLbtUVKMB2P7lwCJM6Jt5cyfja46EX6Oc3cwSPHtUECIK9cV_arFrBb8qxfM-jzSI7JgOSTL7kmgt3zBl8jYI9GdNbxnO9ZKPiJrPXQy7u3zwZJkRkK97g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زنجان الان از زاویه های بیشتر ( دم بچه های زنجان گرم
😁
🫱🏼‍🫲🏽
)
@withyashar</div>
<div class="tg-footer">👁️ 96.8K · <a href="https://t.me/withyashar/17144" target="_blank">📅 19:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17142">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f0aX8ccFfv9u4bkfAe76Z4026IwqM34zfNRodxg6dMicb0RdtES3jn7JSFXqELBMFXi1NgrJMdpYOvCxJGyomYXedBR36aawU6PlrvhTA1dF-NRP3hLTSxqP6JDSdcMaoFoicaaqIiQiHbI__F5BddBmJ-IPJARJp4c6HxeJjYi6kjrFXMBdM_ct_37NZuwUSEnWo4qRDAi-U-86Cq1-gLqVwM_feNhq7ClsQNsn_kWKgfzHfrXnAwMXhWpz_dxnZaSoWACQkodLRzJQA9GnZU7775NP7gMyW7YQe50lYlzOjk_1Khx8k2MSRoWJPLWRAaoIqj_rMVDWGaxAYxcYOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ENV7WsOmvA0XW3wah6c2sdSLB34BauNh2vGiXDOjxRNSP9dk5VRHW3rQ_LfdQbDmO5tFrgzOnh-E7T8NkiVhOEFgA8C-tDj9m8vlicfKjfpOnEKIB_glsdvLPrRVRyCHHwRzqZCD38i4PnSLdy1NHlAmTTgwFit6ZRF6e9mgB6GXHBHt_EjGhUBPMihlZK3PRb5VHvD0K5zO1PWvMzqTZ5pNEFllVupH9h-sxApLPl3uIrlMpEY3oqwmceFs0cBnDLmwKuUlQZz66sJnMm4Zq25uH7hYoYonvMAThnf_3PmCtRdAPf64WHXuTkICKKTpQ1Za8P9HKkxpxE5vob0Z_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">انفجار‌ در شهرک صنعتی زنجان (تایید شد)
🚨
🚨
🚨
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 99.7K · <a href="https://t.me/withyashar/17142" target="_blank">📅 19:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17141">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">گزارش تایید نشده صدای انفجار‌ شهرک صنعتی زنجان
@withyashar</div>
<div class="tg-footer">👁️ 97.8K · <a href="https://t.me/withyashar/17141" target="_blank">📅 19:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17140">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">نخست‌وزیر نتانیاهو خطاب به خلبانان جدید نیروی هوایی در مراسم تحویل نشان‌ها: "جنگ هنوز به پایان نرسیده است، چالش‌های جدیدی در حال ظهور هستند." وزیر امنیت اسرائیل، یوزی یعکوو، در این مراسم گفت: "ارتش دفاعی اسرائیل آماده است تا عملیات را از سر بگیرد و به صورت…</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/17140" target="_blank">📅 18:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17139">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">نخست‌وزیر نتانیاهو خطاب به خلبانان جدید نیروی هوایی در مراسم تحویل نشان‌ها: "جنگ هنوز به پایان نرسیده است، چالش‌های جدیدی در حال ظهور هستند."
وزیر امنیت اسرائیل، یوزی یعکوو، در این مراسم گفت: "
ارتش دفاعی اسرائیل آماده است تا عملیات را از سر بگیرد و به صورت مستقیم به ایران حمله کند - حتی برای بار سوم.
"
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/17139" target="_blank">📅 18:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17138">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/976290cc1c.mp4?token=Su-qTxvlqH0fmkmqzk_pskadtYeKbFQVUwzWJsr2mR1NiZSjnqBoNhRr0zUWo3-ZAqGpnyBQF8iEUq9_OSaFYlM2BD3jS65UZUfoI4_ZvoCrKuAsREcbt0aVvOlyLHYHlqG2PW8VEg_2xTvFO3-UyY8Wc-pet6JMFImLdcbzg4sGq4DYvWqffUcrsfqd3JDXFtYnfTzjDiqiMPSGAF89C9POYO3QmeiYDGC3m8KmodZlXqZPzkHVUzOLqZC7U1Js4Bh2ndxyghObKHHvFp6otnc6tS3X83No1vW-UXQeeo_H8bx-nOH4dOURpQW0Bfx6ipDlO0molSfoqPeiKFlO0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/976290cc1c.mp4?token=Su-qTxvlqH0fmkmqzk_pskadtYeKbFQVUwzWJsr2mR1NiZSjnqBoNhRr0zUWo3-ZAqGpnyBQF8iEUq9_OSaFYlM2BD3jS65UZUfoI4_ZvoCrKuAsREcbt0aVvOlyLHYHlqG2PW8VEg_2xTvFO3-UyY8Wc-pet6JMFImLdcbzg4sGq4DYvWqffUcrsfqd3JDXFtYnfTzjDiqiMPSGAF89C9POYO3QmeiYDGC3m8KmodZlXqZPzkHVUzOLqZC7U1Js4Bh2ndxyghObKHHvFp6otnc6tS3X83No1vW-UXQeeo_H8bx-nOH4dOURpQW0Bfx6ipDlO0molSfoqPeiKFlO0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مقایسه زیبای قبل و بعد بیت رهبری برای درک بهتر شما
💥
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/17138" target="_blank">📅 18:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17137">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cac8f1356.mp4?token=febXmLZIQKhEu5myDJ_c9hjgSJ3uLei6Xc6AaNkvVbA3B_6pDhCsu3B5WMkXfSg5WQZkSPa2luXLFc2SCZKwTpdhCwzb44Bor6BbSNRWxTwXpOXTouW8BDxCfD3IIFQnVU3LmZi5flvANQn0LpgxAA0PkPW0etpKDbrLR3RoSkGMLumoAhKfRVGvGngfuwbDMAoTT_8ha13I-d_XuDD4IR1oFgTG-0ElirC9lond20--MXob869pHRsxPbRiA3YV759tZJgHmfWcLUerrHQ22pTG3xzpvM4Ct9wsgpdtR3aCBp-fjHR2JSlEY0pMlUDcYlKQDHm8aKjsinK595GJhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cac8f1356.mp4?token=febXmLZIQKhEu5myDJ_c9hjgSJ3uLei6Xc6AaNkvVbA3B_6pDhCsu3B5WMkXfSg5WQZkSPa2luXLFc2SCZKwTpdhCwzb44Bor6BbSNRWxTwXpOXTouW8BDxCfD3IIFQnVU3LmZi5flvANQn0LpgxAA0PkPW0etpKDbrLR3RoSkGMLumoAhKfRVGvGngfuwbDMAoTT_8ha13I-d_XuDD4IR1oFgTG-0ElirC9lond20--MXob869pHRsxPbRiA3YV759tZJgHmfWcLUerrHQ22pTG3xzpvM4Ct9wsgpdtR3aCBp-fjHR2JSlEY0pMlUDcYlKQDHm8aKjsinK595GJhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارسالی : حمله آمریکا به اسكله صيادي بنود در بوشهر خدا راشكر خسارت جاني نداشت ولي خسارت مالي حدود ١٢قايق صيادي دوستان اتيش گرفت
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/17137" target="_blank">📅 18:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17136">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">آلن ایر، مذاکره کننده سابق آمریکا در برجام: فعلاً احتمالاً در چرخه بی‌پایان «حملات و سپس کاهش تنش» گرفتار شده‌ایم ! دلیل اصلی این وضعیت، اختلاف بر سر تعریف «باز بودن تنگه هرمز» است.
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/17136" target="_blank">📅 17:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17135">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ارتش اسرائیل (IDF) اعلام کرد که اخیراً دو تونل دیگر متعلق به حزب‌الله در شهر مجدال زون در جنوب لبنان تخریب شده است.
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/17135" target="_blank">📅 17:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17134">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">وزارت امور خارجه ایران: عراقچی، در گفت‌وگوهای تلفنی جداگانه‌ای با همتایان خود از عمان و ترکیه، درباره تحولات در تنگه هرمز گفتگو کرد.
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/17134" target="_blank">📅 17:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17133">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mbiu-K4QacS09w44dA_CFb_gLgldzOkVuAJQgAUvzr_cOgi-1-iW6N8nbLSWsYP9pzjAI4TL9nYQTk2GLZJl7Jgw1pJKIiFmhqxJPleKDGHsnTgFWGUZHtTfW6OF2PBgmGcipGAchGN7d9tlSISDkHXEeXPE5Y7ELHiBxvN_XppRBwrChFg8rQAXKugjwFXItn6H42fgUMYGE6B6nYmpNMt5y7kmIbS3auT9O0F4IdX86Jo0ztw8BGc9yV-56-o9_aJnXwxMfA7wNAb4iOBj7ApRWY7IIGTBBIQfpzH5XnitECFfUF17Nh7rdPNQReSezkA9LUVqMxDCc0XnDPCURg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاویر نادری که صبح امروز توسط یک دیده‌بان در شهر اصفهان، مرکز ایران، گرفته شده، جت‌های جنگنده F-35A Lightning II نیروی هوایی ایالات متحده یا گارد ملی هوایی را نشان می‌دهد که بر فراز این شهر پرواز می‌کنند.
@withyashar</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/17133" target="_blank">📅 17:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17132">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">۳ پا : مرکز فرماندهی کنترل دشمن در غرب آسیا و پایگاه هوایی الازرق اردن با ۱۰ فروند موشک بالستیک در هم کوبیده شد.
@withyashar</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/17132" target="_blank">📅 17:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17131">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">نیویورک تایمز به نقل از فرماندهی مرکزی آمریکا (سنتکام): طی دو روز گذشته، بیش از ۱۷۰ هدف نظامی ایران را در جریان حملات هوایی مورد هدف قرار داده‌ایم
@withyashar</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/17131" target="_blank">📅 16:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17130">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57f75c9892.mp4?token=btsbk2D2UB38FKftMRUIWfEfIDHpbtx2PjC43jR0XpKz6KBRCQwAWJj9cGmk3UPo9V5MIQOGoN-8Vf3Tr1GhC8IRulH_c7e5u-DxUNQ8lhvZ0X4NqBUBo5SormTABMGkrymI5bwXt-dJyqUFVn6A5NuTq_w0Er5t4zB_llbRuDzuZnzIkWrYBXlWB6rYmN0Ga2VzlZZ569e4SBiJ2CpgbhlJvRGp5AE104me2kI09q5XMXUNeaxdCy_XgB9yGSebgUcS4SChVvMqmVPquAXtEEsa5Ii2wI-zapWTwWsMruLchUKNbryQXKBb5-ESWYPKybYl41SJA897J3A-RltFDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57f75c9892.mp4?token=btsbk2D2UB38FKftMRUIWfEfIDHpbtx2PjC43jR0XpKz6KBRCQwAWJj9cGmk3UPo9V5MIQOGoN-8Vf3Tr1GhC8IRulH_c7e5u-DxUNQ8lhvZ0X4NqBUBo5SormTABMGkrymI5bwXt-dJyqUFVn6A5NuTq_w0Er5t4zB_llbRuDzuZnzIkWrYBXlWB6rYmN0Ga2VzlZZ569e4SBiJ2CpgbhlJvRGp5AE104me2kI09q5XMXUNeaxdCy_XgB9yGSebgUcS4SChVvMqmVPquAXtEEsa5Ii2wI-zapWTwWsMruLchUKNbryQXKBb5-ESWYPKybYl41SJA897J3A-RltFDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">l
نتانیاهو : حمله به ایران مانند برداشتن سرطان از بدن شماست.اگر سرطان را از بین نبرید، خواهید مرد.
@withyashar</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/17130" target="_blank">📅 16:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17129">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NyMgk5ST3pTPpZbKdSEp_8sxmI4SeuPR0WRLi7EYHTWSI2GVUpafRBGkaZPS54a4DCC6LVtRyGlDRT9-4cT-i29HxVIO2bRX6eSsYcETOsjf8uolOgUA8dWahpzLxxZWiNhDWZeykBKupeDfv-zeXSeg8FObmEyGyjDqqQh-l8uQKkR-B1qMqYX94H_k3FdHXXgBlce_g2sL0TySKi-dO4J8vHC08atalud-DS7hyvJamo--0XdIYllCWHYTHaNfIXZYULYGmZ9_u7ixAtW3lDIkxdsA8s5E4HH7E6sUMnpvdhFkXqVd8S4pxrDvHD1GdUBSLuWHzg_8ejNYc7L5wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان پهپاد شناسایی آمریکا در آسمان زاهدان سيستان و بلوچستان
@withyashar</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/17129" target="_blank">📅 15:45 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17127">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54fd028548.mp4?token=QpfxbNR0tZgRD-o6YBkIQex9BPZMA08aklyeiMopDyIn0ANyeR93q8c4GsMrwZ_9TVcTr_XHyAhEMYi5BqEuS2i6tZuzFvQABB7FJZTevgoIL6euVUz-5dnBrFB_niVSC5a4QPDryounS5IAx4RfsjUIShG02pXRS6aLoVi5WXGH-3IF-WO6guDHet_Ym9aC-dwvAWdvIU4NANqog5xxA-BMmxG50vWWQFrvjO5hWQNClLsUdLlsFmN-u658ba_CQ_2-3mBQ7PwnEuf5R0S4tN739ccSy2jkVR9gBIMtuI1IiW2ubwaqeQerRdiEKTltUcWQmqGOAJqza1OhXW4AEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54fd028548.mp4?token=QpfxbNR0tZgRD-o6YBkIQex9BPZMA08aklyeiMopDyIn0ANyeR93q8c4GsMrwZ_9TVcTr_XHyAhEMYi5BqEuS2i6tZuzFvQABB7FJZTevgoIL6euVUz-5dnBrFB_niVSC5a4QPDryounS5IAx4RfsjUIShG02pXRS6aLoVi5WXGH-3IF-WO6guDHet_Ym9aC-dwvAWdvIU4NANqog5xxA-BMmxG50vWWQFrvjO5hWQNClLsUdLlsFmN-u658ba_CQ_2-3mBQ7PwnEuf5R0S4tN739ccSy2jkVR9gBIMtuI1IiW2ubwaqeQerRdiEKTltUcWQmqGOAJqza1OhXW4AEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برج اسکله گمرک تجاری بندر چابهار @withyashar</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/17127" target="_blank">📅 15:39 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17126">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc71b6295f.mp4?token=JhpEsILITa_wMQhkarARw3bHr39KPtH4KvyAcuFLAQ5RbrW-Iaq1EBuMPipfLXnEgOT1FaBwFFidc6oemQXHq2xx6iSWSPm7UzZqpOXgMcZxbnLPNOspljAirAr0x3GprrxmKAEZNUynhOME5dLU4ORzWFNmWd4bi9hZInltpjJ8BtaobEkAwBgrK6uS-ERb2lIpG3rTn2RwsngEepmJu004uHiaQzinZqIDhvKDl5y0ckUDLKEGK6_lYfoJlL9RLkeG08uFOA2DLCxotbhrmKsxRRHTpAqgXVpL4oLwBnP39n0jXYh9gFtjecHrJqyqtvQ27YmOpcIRPnF9Lieztw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc71b6295f.mp4?token=JhpEsILITa_wMQhkarARw3bHr39KPtH4KvyAcuFLAQ5RbrW-Iaq1EBuMPipfLXnEgOT1FaBwFFidc6oemQXHq2xx6iSWSPm7UzZqpOXgMcZxbnLPNOspljAirAr0x3GprrxmKAEZNUynhOME5dLU4ORzWFNmWd4bi9hZInltpjJ8BtaobEkAwBgrK6uS-ERb2lIpG3rTn2RwsngEepmJu004uHiaQzinZqIDhvKDl5y0ckUDLKEGK6_lYfoJlL9RLkeG08uFOA2DLCxotbhrmKsxRRHTpAqgXVpL4oLwBnP39n0jXYh9gFtjecHrJqyqtvQ27YmOpcIRPnF9Lieztw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم اکنون ترکیدگی لوله گاز شهریار
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/17126" target="_blank">📅 15:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17125">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">۲ موشک بالستیک از شبستر، استان آذربایجان شرقی شلیک شد به سمت اردن
@withyashar</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/17125" target="_blank">📅 15:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17124">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zv7bTkC5fK3RNONYaS6WUGGmXusBE291SIg0uNYn4HbxBgWsaiGHofA2bqwHAux_tfsZEOwNaAAWRt0XeRG1CCIrqIrkSv0Ddxp2AQyS-ny5vqJWqF03NNsZCjwX0AL8W0fnUJhwVRWCdpBozJZu6sbOyYd4CxFjdq1jMnaozXWW0JibkjEQQo1T5GXp7xmHgDtDt1VvPH9sOmtAZBcoT5QcRXhgmXHQ-LZlcl9KpeywFinpRiqY6eSF1LUNFWq_sXFng3mUs_ArzbgYUZ4r9g9V7FeMihjfH5pKCFupD0d_wOkNrhCMHz5T3EU9hr8Qlqrafx3bH0YqxNKm-UlbDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش از پرواز گسترده جنگنده های نیروی هوایی ارتش بر فراز مشهد از ترس حمله به مراسم @withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/17124" target="_blank">📅 15:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17123">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NVzdeyvDGnznBgn7Z0pzHV_e6khaKk8r2cgSALHLUfFu-KueNyIJHtGiKcwAlWdrUsyR4jYByWnvMRKdfVVC2VdTHKmB8bX0Rh50GkeJi6rkmZQqK0Ifu0VDcZT55rfD6qOKBUA0okbfVTtweZi6lGTKqEkU5eX9lRsfIxbaehonKxnzXvFSXr7USwca1EogxPs6I99sh5G6E1VxezSYQERDnJZsmDgeynVps7vaY4JFKGCb-bmYBuzMv5cDAsp7lYBAmQv9yz42N00Fal_jL8N6tqJaWCGUT4YKnkpwtWOSg9v12kV8ttcKcbhblcAHYJm0dHD5ZcGDhxOLcRRxhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمو ترامپ داره بصورت زنده از تنگه هرمز گزارش تهیه میکنه برای صدا و سیما
@withyashar</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/17123" target="_blank">📅 15:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17122">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">سپاه ثارالله کرمان هدف حمله قرار گرفت
@withyashar</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/17122" target="_blank">📅 15:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17121">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">آژیر ها مجدد در اردن فعال شد
@withyashar</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/17121" target="_blank">📅 15:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17120">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">کانال ۱۴ اسرائیل : علی خامنه‌ای حدود 600 میلیارد دلار(۱۰۹ کوادریلیون تومن) ثروت داشت !!!!
رهبر سابق ایران، علی خامنه‌ای، در حالی که تظاهر می‌کرد مثل فقرا زندگی میکنه، املاکی تو ترکیه، کوبا، مکزیک، ونزوئلا، سوریه، دبی، بریتانیا، روسیه، عراق، ارمنستان و صربستان داشت. همچنین مالک چندین هتل تو اسپانیا بود.
@withyashar</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/17120" target="_blank">📅 15:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17119">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">نیروی هوایی اسرائیل:وضعیت حالت آماده‌باش در سراسر اسرائیل اعلام شد.
@withyashar</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/17119" target="_blank">📅 15:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17118">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">حریم هوایی سوریه بسته شد
@withyashar</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/17118" target="_blank">📅 15:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17117">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">گزارشات از شنیده شدن صدای انفجار در کرمانشاه
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/17117" target="_blank">📅 15:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17115">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UhbpDEc7Jbblxgie5C0mqJL9B6YENK-qDRW5_c1yJLg0HMuBZDVQiAaBtUbaaioQBlz3g0hycmebmMtj0YcGA-hvxpfyQBnHIdh_HXxxG8aEC6cvR_vkPzsGC2FzY8nQI8p7JVbqcKiQyDstQNzASRmJxy1GN8k-w1Fx-lkFIAIE8T_YgAMfekvTNogiQPlSILjXbs_KLpILE9JReX7cR2L0gb9tX30bTfzyZWGkbHP77NYM1YhhsgKRBd8-kN4LPJncP1req680XzD-RDmSJKkCy4I-iR78EgydkbdDPD-5pIRNiYTqr-fv1O_AqxYJRfwu94Nf-CuQ3jCnKkCFuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tQCrRICO-99ttUop-ETwpUishGenAl0yKRfJ2vizeCSYucBtaXbet3libpiWfmWK-8tLoYGMjujErGsIXycWFT6huOnCHwtA7GRySO8WGOH95oSA43g1-OqkEuHMAB1qecUoxEE5rRupf_fOZHVgp6xRmwGhiM_kslw827dkxEpQ770U5UXEwH6VccsdUmGM4aqPU8ucprl6FEv04giTM0HHWgbdUtSTRpAj7m-b_CIO5xv8ASnvxRc_QAdtUPRTcTQy60zVi-nGb6X2NHV2Q55SBugJBxatB70bBJRB8wvGnms-tjELxvuTBi31GabrowPdSVUyk0SJHdYTCJT2xA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وضعیت قایق های سپاه در اسکله بنودِ شهرستان عسلویه
@withyashar</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/17115" target="_blank">📅 15:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17114">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">حمله آمریکا به شادگان در خوزستان
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/17114" target="_blank">📅 14:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17113">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">وای‌نت:  مجدد یه کشتی جنگی دیگر آمریکا تو خلیج فارس مورد حمله قرار گرفت
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/17113" target="_blank">📅 14:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17112">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">گزارش از پرواز گسترده جنگنده های نیروی هوایی ارتش بر فراز مشهد از ترس حمله به مراسم
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/17112" target="_blank">📅 14:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17111">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">آژیرهای خطر در پایگاه نظامی آمریکایی التوحید در بغداد به صدا درآمدند
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/17111" target="_blank">📅 14:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17110">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">تانکر ترکرز: ایران به علت احتمال ازسرگیری محاصره دریایی، 10 میلیون بشکه نفت را در شب گذشته صادر کرده است
@withyashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/17110" target="_blank">📅 14:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17109">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">پایگاه سلمان حاجی آباد هرمزگان دو موشک به سمت تنگه شلیک کرد @withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/17109" target="_blank">📅 14:45 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17108">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">گزارش انفجار در شادگان خوزستان
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/17108" target="_blank">📅 14:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17107">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">پایگاه سلمان حاجی آباد هرمزگان دو موشک به سمت تنگه شلیک کرد
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/17107" target="_blank">📅 14:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17106">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">خبرنگار وال استریت ژورنال: علیرغم صحبت‌های دونالد ترامپ مبنی بر پایان مذاکرات، این احتمال وجود دارد که به زودی به آنها بازگردیم.
پویایی اساسی، بیش از هر چیز دیگری، تمایل به عدم تشدید تنش است. و من گمان می‌کنم که این موضوع در واشنگتن شدیدتر از تهران احساس می‌شود، هرچند که در هر دو مورد صادق است.
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/17106" target="_blank">📅 14:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17105">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">سامانه های پدافند هوایی اردن در حال فعالیت در آسمان پایگاه هوایی موفق سالطی. @withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/17105" target="_blank">📅 14:41 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17104">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">منابع رسانه‌ای: آژیرهای خطر در پایگاه آمریکایی «حریر» در استان اربیل در شمال عراق به صدا درآمد
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/17104" target="_blank">📅 14:39 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17103">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bd8d735f9.mp4?token=haLO73GbV1CCZR4D9NFeFVPjka68XZASBjDxhQPN1sGy_ccBZHtH3tTeTi_7Jx_WI7mpNW1HWaroOIeRI76K31---Aj7h7XIszMP6hz-iC5RhnkFCc7LxUuGrWTv_FyfmqUx7Y8a3JMrcF4mcaCQ5KMt7o5iP1ZDRxzTcwCoL2fnB8I_DRIjMjzk_c2gX7OMT0rechbmt3sVyWZ5fq-8sAmS0OpRK-doikiBunrlfKC7JlHFgDjlag8V2DMT6jw13cOIfhdKGKKSOQNIQzCcs9U6s1OJv6Yz-B7jtS4qg2TQYOy-_ay9BRBnVeoMzt-ASJ8axxsfIlVhRzILNJbvRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bd8d735f9.mp4?token=haLO73GbV1CCZR4D9NFeFVPjka68XZASBjDxhQPN1sGy_ccBZHtH3tTeTi_7Jx_WI7mpNW1HWaroOIeRI76K31---Aj7h7XIszMP6hz-iC5RhnkFCc7LxUuGrWTv_FyfmqUx7Y8a3JMrcF4mcaCQ5KMt7o5iP1ZDRxzTcwCoL2fnB8I_DRIjMjzk_c2gX7OMT0rechbmt3sVyWZ5fq-8sAmS0OpRK-doikiBunrlfKC7JlHFgDjlag8V2DMT6jw13cOIfhdKGKKSOQNIQzCcs9U6s1OJv6Yz-B7jtS4qg2TQYOy-_ay9BRBnVeoMzt-ASJ8axxsfIlVhRzILNJbvRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سامانه های پدافند هوایی اردن در حال فعالیت در آسمان پایگاه هوایی موفق سالطی.
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/17103" target="_blank">📅 14:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17102">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">سفارت آمریکا در اردن به دلیل «گزارش‌هایی مبنی بر وجود موشک، پهپاد یا راکت در حریم هوایی اردن»، دستور فوری برای پناه گرفتن صادر کرده است
@withyashar</div>
<div class="tg-footer">👁️ 97.9K · <a href="https://t.me/withyashar/17102" target="_blank">📅 14:36 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17101">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LgnrQLTJsCV_0c4CxhUCTOqsbwsLpFmWk7TzXkx75x6r__M_9De782VQKaUB3ZayqI_U_8i3Nz9KBtVp2ifZ7Kuo_eh835cFzDy85vpko-RRrx0L9QcrG0e7nTelLWUOn9GxXrq_uiOYMMeRZPszzuMMmosdOmsnUcZGq5SCfVWZKQtCZLSWfV-wc2phJCo57BV-ij1bHQ-Okm7Dnq00xyszKJlv2RwFOo6Ottrd4sVlmhTMvOTnm2TSFRkzJavB5jgpaBztIM8HUNnZ-7wHvF0TMs3PNyR71O1PMLFEnAb8loesCfaB1bV258NSIXMIQanQ8Ei7d9Ipi5YrFCwSdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شلیک موشک از حوالی تبریز
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/17101" target="_blank">📅 14:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17100">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">دقایقی پیش موشک های کروز تاماهاوک در بوشهر دیده شد
@withyashar</div>
<div class="tg-footer">👁️ 98.9K · <a href="https://t.me/withyashar/17100" target="_blank">📅 14:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17099">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 98.9K · <a href="https://t.me/withyashar/17099" target="_blank">📅 14:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17098">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">گزارش ها از نزدیک شدن جنگنده های اسرائیل به مرز عراق و سوریه خبر می‌دهند
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/17098" target="_blank">📅 14:28 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17097">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SXpOVGWVt5glfjA1MWNI9VB7Lj6UkywhAlfoLU1UuMIOoX_URSEtz7qoWycRCrychuZD6i0saQILxvzpX48PPniT8B8FC26LKen01QQ7B1g_ocdNjrKWJkWAyUFuXHtRIBLsjPUpPDFsPpJEcRKH0JtFVDmpoiwRapkCergy-e_DaQT3YoNTQuSNrJK3RMrgm-u9DuTRcqWxhn5ktHGR4glwFQOlpPGMNIJp6789RPlmKtki582v7K86zMcIGyA2YG3br5cgrjpfVUyA9N1eIfIMfTDMTVb_kXVRJ183mrm6idH-njYTkRxQu6bCXh8BIwqYIYR3bxowQTnt7luwZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس زیبای مقعیت و لحظه شلیک لانچر موشک در خمین
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/17097" target="_blank">📅 14:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17096">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 98.9K · <a href="https://t.me/withyashar/17096" target="_blank">📅 14:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17095">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">بعضی رسانه های داخلی خبر دادن مجدد کنار نیروگاه هسته‌ای بوشهر مورد حمله قرار گرفت.
@withyashar</div>
<div class="tg-footer">👁️ 99.9K · <a href="https://t.me/withyashar/17095" target="_blank">📅 14:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17094">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">تانکر ترکرز: ‏تهران، در انتظار ازسرگیری احتمالی قریب‌الوقوع محاصره دریایی نیروی دریایی آمریکا، در یک شب بیش از ۱۰ میلیون بشکه نفت خام و نفت کوره را بارگیری و ارسال کرد.
@withyashar</div>
<div class="tg-footer">👁️ 99.9K · <a href="https://t.me/withyashar/17094" target="_blank">📅 14:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17093">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">گزارش‌ها از صدای انفجار جدید در کرمان
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/17093" target="_blank">📅 14:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17092">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">گزارش صدای انفجار هایی در پایگاه  بندری علی السالم در کویت
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/17092" target="_blank">📅 14:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17091">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">شلیک موشک‌های کروز به سمت کشتی‌های آمریکایی در نزدیکی بحرین.
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/17091" target="_blank">📅 14:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17090">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">آلارم حمله  صدای انفجار و درگیری پدافند در اردن
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 99.8K · <a href="https://t.me/withyashar/17090" target="_blank">📅 14:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17089">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36ca620126.mp4?token=bgyMTUtQeWY63zNtuKa3YWqAlcjQLP52cxKAf3C5UP1XIfyGLxhdQSXIHGjHxkpOjYpJRITf9Hn8syDUy6nCSCzZYZipdEq_394QcE00dagAh5hZb_r0XiWJycgCW_V0dZAu10YIehGryuz72ueSIVP5jxaso4gdX901GPtsH6ws8uxyvCEZsKiLq9bVZgov7vEcxXexSgaKTf-3KwHu6jcwrPfRxDcIYNgJEVZskRdVV5SosPhzKzB0qdEYqM2Rdlw8waq0sE9GgCy78rihHsWdA-ehQpJubeWMxv4kpPKv-b9yLGacQSwI-R5phNyNoohtps9wywB7gZlIOkLDDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36ca620126.mp4?token=bgyMTUtQeWY63zNtuKa3YWqAlcjQLP52cxKAf3C5UP1XIfyGLxhdQSXIHGjHxkpOjYpJRITf9Hn8syDUy6nCSCzZYZipdEq_394QcE00dagAh5hZb_r0XiWJycgCW_V0dZAu10YIehGryuz72ueSIVP5jxaso4gdX901GPtsH6ws8uxyvCEZsKiLq9bVZgov7vEcxXexSgaKTf-3KwHu6jcwrPfRxDcIYNgJEVZskRdVV5SosPhzKzB0qdEYqM2Rdlw8waq0sE9GgCy78rihHsWdA-ehQpJubeWMxv4kpPKv-b9yLGacQSwI-R5phNyNoohtps9wywB7gZlIOkLDDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از زنجان هم موشک پرتاب شده
@withyashar</div>
<div class="tg-footer">👁️ 98.8K · <a href="https://t.me/withyashar/17089" target="_blank">📅 14:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17088">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">آلارم حمله  صدای انفجار و درگیری پدافند در اردن
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 94.8K · <a href="https://t.me/withyashar/17088" target="_blank">📅 14:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17087">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tozikOAgZSj5eHhsAkwhA74bSficJ8D4H_PMP6J19JxakHW-sm7_ZTkdEdAelhJjbdXt1iuneCahEC6iIT-yCaWWfpNJhcURX6hkhnLMP6gyxt6PXSd8fd6kFQXx2jMZlSDu-n2F5fzrh-_yzbjzpqyvVUOokTf63n7PDnmQl3Qj7ON80wfKhUOPsz0-uofuvrajsv8ap1NnSi_1dYiZjRWWhpRp5vxpwnWpXgdpo-X-B9a92HPmF6RufjzwyBOjMn5PuN_D7dRy2SgRxDuaWfzIXzkqZaA5V5p0Aqr-pGbfFw8yT1N4oelvhZlkTFpDK87yqFfd_xEdWyYXMiP-Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه موج جدید حمله را شروع کرد :
۳تا موشک از بین خمین الیگودرز بلند شد
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 96.8K · <a href="https://t.me/withyashar/17087" target="_blank">📅 14:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17086">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/857d372470.mp4?token=W7ZdyWvbUpHSCqoKWukYi8F3LkAhnzKs4ShOW5VbQanWa8DkvhUPEc0xJ70uyvXVBTgdEoAoOmzTlc3CAHuUUBmbotCt7QZLAjQz2z5mkkfLrTfyJJiiH6X6TjBc6YvIb0-Y8DXTIWtIaJns1Bso36hXFqgkKUbCzoUjerLvzChJQbz9aW5STcrjFFRtNpky2gJrPdEJUxfp0PzFkpgapAHwx9Tg5xAnn5G5KQJiV4rsL27wbNlcnhBz9GVmwEioXM9ecdgXXFGYN9cZ8KwYXsyQWOMYATG2P1Mbj1ALeEivC6h2MLYWoc5rKG86xMXe4U_WuWM8jFvXzrQQErlghnB4aZ-oWFmBGmm3HF0_rG2Dhgq8wAy_qI9j-djdTwaYnXOGgNqcTfDJAtlZboIbXr9Mvsv0vK6lardNVa_Uf13Ct7aBlumKkGOK-GYTkr-noMuNrDXolBk60piFO8T8m5vVMDUa5YXdTmGJeaL6yuNoeMo-oyiep-WG8QpkTR8RV_Orii--qInRvEMATC5_fHTajwK3__syQ-fIu9smdzhZvEbp4SY8VPJZI1F093RuOwv_PTSAuhb6z-MsTJGh3jHJW1OYQOXvD3KLjqwfnmsqlhqh-wgREpGbegY086J-QgSDVsd8hT1mhljkdAD-ZSFoQk0QwgceCt26oeNPkKY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/857d372470.mp4?token=W7ZdyWvbUpHSCqoKWukYi8F3LkAhnzKs4ShOW5VbQanWa8DkvhUPEc0xJ70uyvXVBTgdEoAoOmzTlc3CAHuUUBmbotCt7QZLAjQz2z5mkkfLrTfyJJiiH6X6TjBc6YvIb0-Y8DXTIWtIaJns1Bso36hXFqgkKUbCzoUjerLvzChJQbz9aW5STcrjFFRtNpky2gJrPdEJUxfp0PzFkpgapAHwx9Tg5xAnn5G5KQJiV4rsL27wbNlcnhBz9GVmwEioXM9ecdgXXFGYN9cZ8KwYXsyQWOMYATG2P1Mbj1ALeEivC6h2MLYWoc5rKG86xMXe4U_WuWM8jFvXzrQQErlghnB4aZ-oWFmBGmm3HF0_rG2Dhgq8wAy_qI9j-djdTwaYnXOGgNqcTfDJAtlZboIbXr9Mvsv0vK6lardNVa_Uf13Ct7aBlumKkGOK-GYTkr-noMuNrDXolBk60piFO8T8m5vVMDUa5YXdTmGJeaL6yuNoeMo-oyiep-WG8QpkTR8RV_Orii--qInRvEMATC5_fHTajwK3__syQ-fIu9smdzhZvEbp4SY8VPJZI1F093RuOwv_PTSAuhb6z-MsTJGh3jHJW1OYQOXvD3KLjqwfnmsqlhqh-wgREpGbegY086J-QgSDVsd8hT1mhljkdAD-ZSFoQk0QwgceCt26oeNPkKY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئویی که ترامپ از بمب افکن ‌B-2 تو ثروث سوشال پست کرده همراه با آهنگ بمباران ایران
@withyashar</div>
<div class="tg-footer">👁️ 94.8K · <a href="https://t.me/withyashar/17086" target="_blank">📅 14:11 · 18 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
