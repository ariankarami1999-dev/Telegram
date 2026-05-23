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
<img src="https://cdn4.telesco.pe/file/FZNIidTgPxgjDzmqFvMc33nI3t9kJ0z6n5o0qsLWre9uObRIsOQZAjUG678VaXzQJvbMKC2gHYGSC9malGOCmZJsd7UKk-rR6PeOkGMloXlodeNqvpVv_Ts3AVREpC2HhHFaC6_9c0wZXalvjEd346eClzV80JA1Ky3wbQbQh0x9Q6_sXqaik088hq6gpwJKgC34S7f0ADlWHTWYADExNDxPpRrR2sLW1w2PQNgMLSelJ8wyiKKmMKXCyCVl2VS_9yxtZ0b2Fn6m7NrTQme-80bWs4idrAwf7cfi3tHvxJN_kSUeHSA4mJDtyl3RpQmPdTa6NRGK5BpQvw6X-LTq_g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 9.87K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-02 21:26:25</div>
<hr>

<div class="tg-post" id="msg-16562">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">—مقامات اسرائیلی به آکسیوس:
« نتانیاهو نگران توافق مورد بحث است و از ترامپ خواسته است تا دور دیگری از حملات را آغاز کند».</div>
<div class="tg-footer">👁️ 721 · <a href="https://t.me/SBoxxx/16562" target="_blank">📅 20:53 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16561">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ادعای جدید روبیو درباره مذاکرات:   شاید خبری باشد، شاید نباشد!</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/SBoxxx/16561" target="_blank">📅 20:16 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16560">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👽
ذکر نام "ایران" در اسناد جدیدی که وزارت دفاع آمریکا از پرونده های UFO منتشر کرده است :
4 شیء ناشناس پرنده به صورت گروهی 26 آگوست 2022، روی آبهای ایران مشاهده شدند</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/SBoxxx/16560" target="_blank">📅 19:46 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16559">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔴
تقی پور ؛ نماینده مجلس
:
جمهوری اسلامی ایران می‌تواند کابل‌های حیاتی فیبرنوری جهان را قطع کند</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/SBoxxx/16559" target="_blank">📅 19:40 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16558">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v-C1dOoXqMZQgrDaSKHbkgmAQ_pd0r8tvExSOci_FkzFiO38wIqE_rxA9MCVyxeSH_F_ZADdGy8UKq2ljj0MDAhYy_suAQr0qYQbcoAwn02a1CzjJmZ8ZvWRY_duRO7ZD8Wv9EKZVY-Kr39EfOSGPt0phmv_pcREBiJj-eijDqnQ_U4XBo-PstUMw3jaI16O3LW4B7bYvUy8hdi05ez_X98Us08apm6fRyq1mwnAol2P-_o_bO8HvQ9UAlmOKq3w50k21OqgeoDXWa22nTZ9v5wKvq4mpqDIbT3kfe3kt5cyfWmJ8GyP_L69IqX0ON4-QU0-mWK3zZkogKntiBS9-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/SBoxxx/16558" target="_blank">📅 18:58 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16557">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">سخنگوی وزارت خارجه:   ما به توافق خیلی دور و خیلی نزدیک هستیم</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/SBoxxx/16557" target="_blank">📅 17:42 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16556">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">سخنگوی وزارت امور خارجه ایران، اسماعیل بقایی، به زبان عربی:   اگر دندان‌های {آرواره}  یک شیر را باز کرده ببینید، فرض نکنید که شیر در حال لبخند زدن است.</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/SBoxxx/16556" target="_blank">📅 17:38 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16555">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aJ43xYQMC8FTwhEoPxGHn-zNUZ6mRtHcEzXuboCE4xrl3TrSgd_XwVF9_IYM--PDQ_UNDRvuMp6wTRxGV-_4KGfUzT2VRvtULhtdxZOr9Wzq-LPo4DA34ieTESg2ImT1P7MWU6qK7jgSD--NlaxYZbXcXS3AvTxz2pGSXc8vv6mmCYvBA3k0GWRYlJVZu2JLIlnmbBTdQeA6MWSpRSf26JfASNWw1I5pSIpWYn5KD1l4BPlAQowaChSfRI7cbU3Ru1OSReunKclyL6_f6GlM9EMmQtfN2g_557bmf1aZxQR79M5gMDdkmO_OASmW-6U_74S60Vuef5_ZsjIVWBw4hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی وزارت خارجه:   ما به توافق خیلی دور و خیلی نزدیک هستیم</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/SBoxxx/16555" target="_blank">📅 17:35 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16554">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">سخنگوی وزارت خارجه:   ما به توافق خیلی دور و خیلی نزدیک هستیم</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/SBoxxx/16554" target="_blank">📅 17:33 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16553">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">سخنگوی وزارت خارجه:
ما به توافق خیلی دور و خیلی نزدیک هستیم</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/SBoxxx/16553" target="_blank">📅 17:31 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16552">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">—یک مقام ایرانی به الجزیره:
«ما با میانجی پاکستانی به یک تفاهم‌نامه رسیده‌ایم و در انتظار پاسخ آمریکایی هستیم.
تفاهم‌نامه شامل پایان جنگ، برداشتن محاصره، باز شدن تنگه هرمز و خروج نیروهای آمریکایی از منطقه جنگی است.
تفاهم‌نامه مسائل هسته‌ای را شامل نمی‌شود زیرا پیچیده هستند و زمان کافی برای مذاکره نیاز دارند. پس از ۳۰ روز از توافق، دربی برای مذاکرات هسته‌ای می‌تواند باز شود.
پیش‌بینی شده بود که رئیس ستاد ارتش پاکستان تفاهم‌نامه را در تهران اعلام کند، اما برای هماهنگی با واشنگتن رفت.
برای ایران امکان‌پذیر نیست که امتیازات بیشتری نسبت به آنچه در تفاهم‌نامه مقرر شده است، بدهد».</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/SBoxxx/16552" target="_blank">📅 17:28 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16551">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rjcPEaztXhW4rgaxlazHJiceSFPAeCCbVvWOeTBcQiwy11ocRP0rq1q4emsCZXJsIAETmwH_w7n-7vEDS0wSd1yFMKXZlEVjrwX1UvUukFuwjT07rPc-X4ivYZrNg5TYdznJdcRPa1dPS65emQ2gpTtXXzFAApj5l0iW3QHCEs68fNf2vxP-Tc8c53P0RkpgOxwbPsOHn08ujVhJ87htfkPbSt9dW28IJNK4wmKSvPKqbvlfoTlS6XExIr1z_SinqE0qRP60BRV5Cr7JQdkC5YETlXuNkLfE6sFOv_kybWAtpzrjy_RDfjueVdva3VfyeLrXhFnKeWgJuhrpjt0adA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سبحان الله!  نکشی مون آبجی!  انشالله فقط کاربرد نظامی دارد دیگر؟!</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/SBoxxx/16551" target="_blank">📅 17:21 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16550">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m360p69-SNCNJs9hPZcbpw_E-VQPkVF7RRs0dg6ntChO7OFHu8BDlWEUJhPd1wyXqw4XNsyJkAFaqFDMolftsDjVuTpxQEhoDldHJ8OzeO7Zcztp5bBJia-jPrWQ3dPPYlHH_hNBT_w7wli9naytPEkYR414rOEN8WyHfiNQOXD8B6eFnnTd0CkTNXIghKmzKYQ868vNyRvugFG5os5DFSThyYUV7jfsfunoZ4PvLmY-sunZ6d1Dya2JMnmAPistvCgsi7w_bqBGB5i9rd2TqHNkVCCwrOBUMSO3xLXz0HyXf9V3qEj5zUMoJkyzJC-zNJTIuZTuvBeqL3vojFaOLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
تایید واگرایی میان اقتصاد اروپا با آمریکا پس از جنگ ایران
داده‌های اخیر PMI نشان می‌دهد اقتصاد آمریکا همچنان در محدوده رشد باقی مانده، در حالی که اقتصاد منطقه یورو به‌ویژه در بخش خدمات وارد فاز انقباض شده است. این واگرایی می‌تواند در ماه‌های آینده به یکی از عوامل اصلی جهت‌دهنده بازار ارز، سهام و اوراق قرضه تبدیل شود.
در شرایط افزایش تنش‌های ژئوپلیتیکی و رشد هزینه انرژی، آمریکا به دلیل استقلال انرژی و عمق بازار داخلی مقاومت بیشتری نشان داده، اما اروپا به‌دلیل وابستگی بالاتر به واردات انرژی آسیب‌پذیرتر شده است. تداوم این روند می‌تواند به تقویت دلار، فشار بر یورو و تغییر مسیر سیاست‌های پولی بانک‌های مرکزی منجر شود.
🔗
ادامه یادداشت را از اینجا بخوانید!
💬
ارتباط با پشتیبانی :
@cyclicalwavessupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/SBoxxx/16550" target="_blank">📅 15:50 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16549">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/SBoxxx/16549" target="_blank">📅 15:23 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16548">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">کارمای اجدادمان که سهل است، کارمای قابیل دیوث را هم سوزاندیم در این زندگی</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/SBoxxx/16548" target="_blank">📅 15:22 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16547">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">صبح تا شب این وضعیت مجریان ماست در سداوصیما ، در ماهواره هم که فقط صحبت جنگ و حمله است، نت هم با گیگ ۵۰۰ هزار تومانی باید برویم تانکرترکرز و فلایت رادار و اکانت کله زرد پفیوز و حساب محمد something های وطنی را چک کنیم ببینیم کی جنگ بعدی می‌شود!
بعد این نکبتهای انگیزشی میگویند بیدار که شدی به دنیا لبخند بزن!
به … عمه تان لبخند بزنید قرمساق ها</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/SBoxxx/16547" target="_blank">📅 15:21 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16546">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">سبحان الله!  نکشی مون آبجی!  انشالله فقط کاربرد نظامی دارد دیگر؟!</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/SBoxxx/16546" target="_blank">📅 15:18 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16545">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GtvxaaIynmaWQ0MtfXwq9mnikOfFfMAiuwKmnyHBKcBCM9qLiwLMy7EMJp5dsuCCqOUEb_k-J5oWdqlwS84TQuHTCEOLwYVmWo670toYFHfCxwoc_9iHndZ080zypRmq18bOVrOnerufNdYrDJ7XyPP-eSk_51-9xjwHNNsbAvukXqrDCRdzMYwehb7bS-2rICs98TI-ArGFl8lH8a1s2-PXqnAcEFHqn0zCaVJ6EBntWri-Jdlg2rfUMOgTxTg_Vwr72h5JJERCcUawo4KUciLZ3mliY6cjKaVvh9jspYtbLyPvScHSFISVoyfo3VyjW12IbMOxAhiO6oAKspj68Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سبحان الله!</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/SBoxxx/16545" target="_blank">📅 15:16 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16544">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ترامپ اسرائیل را از مذاکرات ایران حذف کرده است!
به گزارش نیویورک تایمز، این واقعیت که اسرائیل «تقریباً به طور کامل از حلقه مذاکرات آتش‌بس» بین ایالات متحده و ایران خارج شده است، به یک «شکست خوارکننده» برای بنیامین نتانیاهو، نخست‌وزیر اسرائیل تبدیل شده است
نکات کلیدی:
🌏
دونالد ترامپ بیبی را به عنوان متحدی از ایالات متحده می‌بیند، اما نه به عنوان یک شریک نزدیک در مذاکرات با ایرانیان
🌏
اسرائیل از شریک برابر کاخ سفید به «چیزی شبیه به یک پیمانکار فرعی برای ارتش ایالات متحده» تنزل یافته است</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/SBoxxx/16544" target="_blank">📅 14:54 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16543">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ژاپنی‌ها آمپولی ساخته‌اند که می‌تواند عمر گربه‌ها را تا ۳۰ سال افزایش دهد.
یکی از دلایل اصلی مرگ‌ومیر حیوانات خانگی پیر، بیماری مزمن کلیوی است. به مرور زمان، پروتئین AIM که باید بدن را از زباله‌های سلولی تصفیه کند، به سادگی از کار می‌افتد.
اما دانشمندان تزریق‌هایی با AIM مصنوعی ساخته‌اند که مستقیماً تصفیه کلیه را تحریک کرده و با سموم مبارزه می‌کنند. این تکنیک حتی در گربه‌های بسیار بیمار نتایج قدرتمندی نشان داد.
انتشار جهانی این دارو تا سال ۲۰۲۷ پیش‌بینی می‌شود.</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/SBoxxx/16543" target="_blank">📅 14:37 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16542">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">📡
وزیر ارتباطات دولت
:
این نگاه قیم مابانه که اینترنت را خلاصه در ۲ پیام‌رسان داخلی می‌داند و برای مسیر اینترنت مردم خط کشی می‌سازد ، نگاه قوه عاقله حکومت نیست</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/SBoxxx/16542" target="_blank">📅 13:06 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16541">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ایران یک اطلاعیه نوتام صادر کرده است که پروازها را تا صبح روز دوشنبه در بخش غربی فضای هوایی خود محدود می‌کند.  البته خب منظور پروازهایی است که می‌شود ممنوع کرد ولی خب  از توجه شما به این موضوع سپاسگزارم!</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/SBoxxx/16541" target="_blank">📅 12:28 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16540">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">استعفای تولسی گابارد: ایستادگی در برابر از سرگیری جنگ با ایران؟
تولسی گابارد ممکن است به دلیل سرطان همسرش استعفا نداده باشد، بلکه به گفته مجری TYT، چنک اویغور، به خاطر امتناع از همراهی با برنامه‌های ترامپ برای از سرگیری جنگ با ایران این تصمیم را گرفته است.
ت.</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/SBoxxx/16540" target="_blank">📅 10:21 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16539">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">هیئت قطری که انتظار می‌رفت حداقل تا روز یکشنبه در ایران بماند، دیشب پس از دریافت دستور فوری، ایران را ترک کرد.</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/SBoxxx/16539" target="_blank">📅 09:16 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16538">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ایران یک اطلاعیه نوتام صادر کرده است که پروازها را تا صبح روز دوشنبه در بخش غربی فضای هوایی خود محدود می‌کند.
البته خب منظور پروازهایی است که می‌شود ممنوع کرد ولی خب
از توجه شما به این موضوع سپاسگزارم!</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/SBoxxx/16538" target="_blank">📅 08:45 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16537">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">تحلیل من این است که ترامپ فعلا میخواهد یک دور کوتاه از حملات شدید را انجام داده و سپس اعلام پیروزی و پایان جنگ کند تا در آستانه جام جهانی، کمتر زیر فشار افکار عمومی باشد.
اما جنگ اصلی برای چند ماه بعد خواهدبود.
در واقع این جنگ کوتاه را می‌توان یک موج B درنظر گرفت که از سقف موج ۳ ظاهرا فراتر می‌رود اما هنوز بخشی از موج ۴ است
سبحان الله!
این هم نتیجه مکاشفات و مطالعات ما با گیگ ۵۰۰ هزار تومنی در روزهای مثلا تعطیلات!</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/SBoxxx/16537" target="_blank">📅 08:10 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16536">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jnwsbZSveXdpWoWzW8QqnawiFdohLarJen-zpsWQ9Hb_-b22XZZpUlhmWtR4c8NVOf5a-l7r1-7THZWnb_CCYw8JO7D9BXVCUpdpjgo7OxnbCabe3afXZX4WKkGIO862tj1iUWSWH7C8XimhoMX5bTXtyeT6qJ7jZeld01DZCz3UsnGbSigebL6R1LHJ4ms4zhQnAgqtpdu_FDUm0rxLtdmHIWdgV1YIQ7vc24r9JOtDu1Kueno1ryb1Y-ZxyNZqaB4Dvbq0ThfrzcTkYQgvpZE5VFtF2Bdu0RkkeYOiyutso5WTAbppekG7DrRyYI8Cyrva6VWWVouR7SQF1Unnsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت دادگستری ایالات متحده دستگیری محمد باقر الصعادی، چهره ارشد در گروه شبه‌نظامی عراقی کتائب حزب‌الله که توسط ایران حمایت می‌شود، و انتقال او به خاک آمریکا را اعلام کرد.  طبق این بیانیه، الصعادی حملات علیه منافع ایالات متحده و اسرائیل را هم در داخل ایالات…</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/SBoxxx/16536" target="_blank">📅 07:54 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16535">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LKmwnOquiu-3ZmDM4H9w7CbRT7UgW47XmJz_4Xd0rfRQTkP5a3aHAXSNc3bao9-ODQOO5FVQglavyRPGE74xW0C4RlwgtL0qygpwBT1Bzubjpuak9u4oWB6UIfZiyKUIf9sWMr9XKY4icRrts5etsVlHIMfrjl6AZL4on4l84_213_O7kMytIyWeNgTHcrIIg1NVMf1bQV-iyJXVxVWuuzdFBhEzK-ngm7FaWTEfhDNpXEl83jACKgRI1GKw9qQeCeIa4yfg_nCPTaYZHUzi4B82vvf4dCaS2QVM9cjr8zALYMUIL0JfKtFwsP-3BUaPGiIPHOb0biRAN9iG3OmDVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری سی‌بی‌اس در یک پیام فوری اعلام کرد که دولت ترامپ در حال آماده‌ سازی برای احتمال دور جدیدی از حملات علیه ایران است.</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/SBoxxx/16535" target="_blank">📅 05:10 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16534">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">یک مقام آمریکایی که در جریان تلاش‌های دیپلماتیک قرار دارد، مذاکرات را «رنج‌آور» توصیف کرد. این مقام گفت پیش‌نویس‌ها «هر روز رفت و برگشت می‌کنند» بدون اینکه پیشرفت قابل توجهی روی بدهد.
یک منبع نزدیک به رئیس‌جمهور آمریکا، ترامپ، گفت که ترامپ در چند روز گذشته به طور فزاینده‌ای ناامید شده و احتمال یک عملیات نظامی بزرگ نهایی را مطرح کرده است، پس از آن ممکن است پیروزی اعلام کند و جنگ را پایان دهد.
میانجی‌ها در تلاشند تا یک توافق موقت بین ایران و آمریکا را تضمین کنند تا از حملات جدید آمریکا و اسرائیل که مقامات هشدار داده‌اند ممکن است ظرف چند روز رخ دهد، جلوگیری کنند.
پاکستان، قطر و دیگر بازیگران منطقه‌ای در تلاشند تا اختلافات درباره برنامه هسته‌ای ایران، رفع تحریم‌ها و مسائل امنیت منطقه‌ای را کاهش بدهند.
هدف، توافق جامع نیست، بلکه چارچوب موقتی است که آتش‌بس را تمدید کند و اجازه دهد مذاکرات گسترده‌تر ادامه یابد.</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/SBoxxx/16534" target="_blank">📅 00:41 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16533">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BKhHLdsIwWMGc4JqJRGWLP36tjW6y0JtEm9D5yZAdV_MmJwBQg1YJL76FCqbYNNW2kK1A2QM7bSVCwiOI-WZplv4dcvu5fcCNvROGxdmu9l9DJGmagE-EOaBqzSfcUV7W__dHCHn4CLmYP4MWsZKzVTFHf3AxqjAibIR43VIug9Q1lMUSDZ8c1PLMwVCpWf5RXXfhFJk3cX8VtepG8vqBZfrZTgzpbt4S2cgrHm-W6y9ti1jLq4NrhuArzBwpUTAENEgKjSVxmSlLlzHvBGAxEV3B9bdzPpGGWjkY6PJnirUCSIKdRQ36wU4TbYPR2NDB6p65dKRXTqqF05Ndl274w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کوین وارش رسماً به عنوان رئیس جدید فدرال رزرو ایالات متحده سوگند یاد کرد</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/SBoxxx/16533" target="_blank">📅 00:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16532">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">خب به صورت رسمی از این طرح رونمایی شد.  در واقع در این طرح که حریم دریایی نهاد تنگه خلیج فارس نام دارد، عملا بخش‌هایی از دریای عمان هم شامل می‌شود که اساسا ربطی نه به خلیج فارس دارد نه تنگه هرمز و صرفا برای فشار خفه کننده بر امارات طراحی شده است.</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/SBoxxx/16532" target="_blank">📅 23:25 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16531">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ایران: آخر هفته‌ای بر لبه تیغ
۲۲ مه ۲۰۲۶ | پیترو باتاکی
مذاکرات درباره ایران همچنان ادامه دارد، اما اختلافات اصلی همچنان پابرجاست. قرار بود امروز ژنرال عاصم منیر، که بسیاری او را «حاکم واقعی پاکستان» می‌دانند، به تهران سفر کند، اما بنا بر برخی گزارش‌ها این سفر لغو شده است.
شکاف میان ایران و ایالات متحده همچنان بسیار عمیق است؛ به‌ویژه در موضوع برنامه هسته‌ای، انتقال ذخایر اورانیوم به خارج از کشور و همچنین مسئله کنترل تنگه هرمز. طی روزهای اخیر گزارش‌های متعددی درباره اختلاف‌نظرهای احتمالی میان واشنگتن و تل‌آویو منتشر شده است؛ گزارش‌هایی که حاکی از آن هستند که بنیامین نتانیاهو برای حمله مجدد به ایران بی‌صبرانه فشار می‌آورد، در حالی که دونالد ترامپ با احتیاط بیشتری عمل کرده و در تلاش است از طریق مذاکره به توافقی با تهران دست یابد.
با این حال، این احتمال نیز وجود دارد که چنین گزارش‌هایی صرفاً بخشی از یک عملیات فریب و انحراف افکار عمومی باشد؛ تلاشی برای پنهان کردن اهداف واقعی آمریکا و اسرائیل و فراهم کردن عنصر غافلگیری برای موج جدیدی از حملات که این بار قرار است سرنوشت‌ساز و تعیین‌کننده باشد. از این رو، به نظر می‌رسد آخر هفته‌ای بسیار پرتنش در پیش باشد.
در میدان نیز وضعیت تغییر محسوسی نکرده است. آرایش نیروهای دریایی و هوایی آمریکا نه تنها کاهش نیافته، بلکه در هفته‌های اخیر ده‌ها پرواز باری تجهیزات و تسلیحات جدید را به منطقه عملیات منتقل کرده‌اند. این جنگ هزینه‌های سنگینی به همراه داشته و فشار قابل توجهی بر ذخایر تسلیحاتی وارد کرده است. تنها در شانزده روز نخست درگیری‌ها، بیش از ۲۵ درصد از ذخایر موشک‌های تاماهاوک و حدود ۴۰ درصد از موشک‌های رهگیر تالون مورد استفاده در سامانه‌های دفاع موشکی تاد مصرف شده‌اند.
بر اساس گزارش اخیر مرکز پژوهش‌های کنگره آمریکا، تنها یک ماه جنگ حدود ۳۰ میلیارد دلار هزینه در برداشته است. همچنین ۴۲ فروند هواپیما، بالگرد و پهپاد یا نابود شده‌اند یا آسیب دیده‌اند که ارزش مجموع آن‌ها حدود ۲.۶ میلیارد دلار برآورد می‌شود؛ هرچند نویسنده معتقد است ارقام واقعی احتمالاً از این میزان نیز بیشتر است.
در سوی مقابل، ایران همچنان بخشی از توان فرسایشی خود را حفظ کرده و گزارش‌ها حاکی از آن است که در طول هفته‌های آتش‌بس، چندین شهر موشکی زیرزمینی را دوباره فعال کرده است. در چنین شرایطی، اگر جنگ وارد مرحله جدیدی شود، نمی‌تواند برای مدت طولانی ادامه پیدا کند و باید ماهیتی قاطع و تعیین‌کننده داشته باشد. در غیر این صورت، طرفین ناچار خواهند بود برای مدت نامحدودی با وضعیت کنونی کنار بیایند؛ نوعی «جنگ سرد» که در حوزه‌های اقتصادی، مالی و شناختی جریان دارد.
کنترل تنگه هرمز همچنان مورد مناقشه است و حجم تردد دریایی هنوز فاصله زیادی با شرایط عادی دارد. همچنین محاصره بنادر ایران که از ۱۳ آوریل توسط آمریکا آغاز شده، همچنان ادامه دارد. محاسبه ترامپ این است که ترکیب تحریم‌ها، محاصره اقتصادی و فشار نظامی در نهایت موقعیت مذاکره‌ای تهران را تضعیف کرده و ایران را وادار به عقب‌نشینی خواهد کرد.
محاصره دریایی به‌ویژه فشار قابل توجهی بر اقتصاد از پیش آسیب‌دیده ایران وارد کرده است. ظرفیت مخازن ذخیره‌سازی داخل کشور به حدود ۷۰ درصد رسیده و همین موضوع تهران را ناچار کرده است برخی نفتکش‌های قدیمی را به انبارهای شناور نفت تبدیل کند. طبق گزارش‌ها، دست‌کم ۵۰ نفتکش ایرانی در حال حاضر برای ذخیره‌سازی نفت مورد استفاده قرار می‌گیرند که نسبت به آغاز محاصره، حدود ۶۵ درصد افزایش نشان می‌دهد.
ترامپ بر موفقیت این راهبرد حساب باز کرده است، اما این رویکرد ریسک‌های قابل توجهی نیز به همراه دارد. زیرا تداوم این وضعیتِ «جنگی که رسماً جنگ نیست» می‌تواند پیامدهای گسترده‌ای برای ثبات اقتصاد و نظام مالی جهانی داشته باشد و در نهایت هزینه آن نه تنها بر دوش بازیگران منطقه، بلکه بر دوش شهروندان عادی آمریکایی نیز قرار خواهد گرفت.</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/SBoxxx/16531" target="_blank">📅 23:20 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16530">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XaXCRYpDMbxd3fE-MrgKjWlvaBZ0pN06DXCxSP5lYuss6RPr4qZbNwAiLrAeLKB6JfoVehke0ozzcVUCu9wbRP8N2-Zl_iop0MQ1LZ62zVQLl_EI6F6MsM305OyCrylLzi-6jzywi-Ou7PxsGm_Z9yRrecesBJygcisNYW4xjDdUEO1KzUgLtMTc_jJwX8ySy1Xve8DRBi6HxBdOr-oqazVgxxGdOU0FCfl4XY1Oll7v10GXJWsj48FwFyDo3-8Tjfq9s23QHXDFet70rq4GDM4nAynVF5VKYjZJkoc2LcVSQ5XTBOWoKs5LJPjKpfi1MYsI4eNengrm-d5gUc05eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ فرزندآوری در کشورهای جهان
نکات کلیدی:
حدود
۷۱ درصد
از جمعیت جهان اکنون در کشورهایی زندگی می‌کنند که نرخ زاد و ولد در آن‌ها پایین‌تر از
سطح جایگزینی
مورد نیاز برای حفظ اندازه جمعیت است.
نرخ باروری چین به تنها
۱٫۰ تولد به ازای هر زن
کاهش یافته است، در حالی که هند نیز با
۱٫۹
پایین‌تر از سطح جایگزینی قرار گرفته است.
آفریقای زیرصحرا دارای بالاترین نرخ‌های زاد و ولد جهان است که به ترتیب توسط
چاد، سومالی و کنگوی دموکراتیک
رهبری می‌شود.</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/SBoxxx/16530" target="_blank">📅 23:11 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16529">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26ffd0c130.mp4?token=P7puX7K9nRfmhDyT__WoN2n2Ivxu5r3Gu9Rv0vi8qcuE1LtVZ6QlZnC7-LapTVggEYuy4XcTtMsBR6DriAs-kQUcAgZ_8KZ0PDDT2XStzrV0asqUm-oL81CZtkTwSCYMu9qMjhTOM6qcFdJDDRgrMYoENwrDcWti1MLhpZqr0so7Ksh_OLjxZh4wmYOZ-Onwh93eHG9Hbv2evIQ7wP6dCAN204CQJczG495zqfE637M_RmS82131DnptbjLNTiSOyLyr8bVbsN-CFUqWc2xwHlO2ONu0FKUPZtXdv94vseF4ueXvhxvxP7LMz5CHD_hDWEEK_DP5VelLVpN3tk5pKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26ffd0c130.mp4?token=P7puX7K9nRfmhDyT__WoN2n2Ivxu5r3Gu9Rv0vi8qcuE1LtVZ6QlZnC7-LapTVggEYuy4XcTtMsBR6DriAs-kQUcAgZ_8KZ0PDDT2XStzrV0asqUm-oL81CZtkTwSCYMu9qMjhTOM6qcFdJDDRgrMYoENwrDcWti1MLhpZqr0so7Ksh_OLjxZh4wmYOZ-Onwh93eHG9Hbv2evIQ7wP6dCAN204CQJczG495zqfE637M_RmS82131DnptbjLNTiSOyLyr8bVbsN-CFUqWc2xwHlO2ONu0FKUPZtXdv94vseF4ueXvhxvxP7LMz5CHD_hDWEEK_DP5VelLVpN3tk5pKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭕️
آزمایش و رونمایی گسترده چین از نسل جدیدی ربات‌های انسان‌نمای پیشرفته با قابلیت‌های نظامی و امنیتی
این ربات‌ها در نمایش‌های عمومی شامل حرکات رزمی، تعادل پیشرفته، پرش، و تعامل مستقل با محیط هستند و توسط چند شرکت رباتیک چینی به‌عنوان نمونه‌های «آماده کاربردهای میدانی» معرفی شدند
فیلم ارسال شده مربوط به رونمایی حرفه ای یکی از ربات های انسان نمای بومی در آنتن زنده صدا و سیما است:</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/SBoxxx/16529" target="_blank">📅 16:59 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16528">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🍆
طبق ادعای برخی منابع ، عاصم منیر ، بلندپایه ترین فرمانده ارتش پاکستان به زودی راهی تهران می‌شود
🔻
رسانه ها این امر را نشانه ای از پیشرفت قابل توجه مذاکرات می دانند</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/SBoxxx/16528" target="_blank">📅 16:43 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16527">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
الجزیره به نقل از منبع پاکستانی
:
بالا رفتن سقف خواسته های جمهوری اسلامی ایران و دولت ترامپ در بحث تنگه هرمز و اورانیوم های غنی شده ، منجر به بن بست در مذاکرات شده است . ما همچنان به حصول توافقی واقعی خوشبین هستیم</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/SBoxxx/16527" target="_blank">📅 12:45 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16526">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AvJpa8SsGwZdN6u2SU75F4Xuf8G9eFP0v9cEi8HuxH6M2_Iqigirg9jjC3jqqXWxUNytTTurEvgZUzGeImDEDJpHwrRCAFjIXSq0vaRQDkSbKblF4-WLUEJHnNLL1owSi7JPd4cTEtAzwj0AyuAyurKPIZunj7eFnzY39cD_HqHbhg9cZIOQ2scsI2Q4NVHFA7bNcdl94MFwJve1wxORj6u8OU6mtz7LHGzUreRWbDJDsboN3Pd5yGT5OQvas8_5zFqlM7GPra-h28vmXHv-Oq4KuwOwxB8EOG7qsIvjMXbfzFeZXiTRC2sF4jJMzpOYSi18MLtVZ-jH7Sqjk9ffyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#TUR — D  عیناً طبق مسیر می تواند با تکمیل این سروشانه که همسو با پایان یک رالی 5-موجی است یک افت سنگین اصلاحی داشته باشد و سپس رشد اصلی طبق مسیر پست ریپلای شده محقق بشود.</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/SBoxxx/16526" target="_blank">📅 10:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16525">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VXt_onhHchBtLUkLFme62Z9XK6y_J3F31oqTRcTtdW1G6A1w1N9LFw239JqtzNJy_d6A1bD94Pig-WrKoWbhQs1q_qDsFd4h-QHwet7RwJ9NOpzlCp6LL3VaX02EvMG5W_2Uk_SobwNU4ghyBG1ThDWh7NmGQebLL-Zej2oHWuwersaRMT7dREWBushmk16Ru-v-u5e_al4sVG23-rBMxz5cSvLMSw8iuyO_aSka9J5oucxGUTigtFt_zKlDB3UjCNBNGUab_iRwR2nUgK241ZUGinClSttfLqIseF_5d4GLvOA5JtEPbGislnFTMtkBl5_Ylu2tG6CsJEYnZ-rCxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#TUR #Turkey
🖊
با داده هایی که اخیراً منتشر شد (موافقت ترکیه با پیوستن سوئد به ناتو و انعقاد قرارداد خرید تسلیحات 23 میلیارد دلاری بین ترکیه و آمریکا) به نظر می رسد سناریویی که اینجا گفته بودیم (نزدیکی دوباره ترکیه به غرب) در حال تحقق باشد.  این نموداری که…</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/SBoxxx/16525" target="_blank">📅 10:50 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16524">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hL2iJd0ShxAOschXpqeKYbcoBuvYZlpvn70zUzgbCF05TTtqISgiGzf-RDLPGAbiaEtyNoqOZXaqAteL26u-NbPAw7BcsTL_uj6hkSST0yIf8mQ4zx0ir7R3DJjkaXx--ZlQp3ReVnEiPBYLsuSWqqkbN7QFizvDRkwWylNIyjiyah5bTBw2DFl9GW6FD6g44-MSfL_0kapyld1NxA0xzNM04wvCLadJNqgJ9yE4C0HD59HERcd5yfSyqUtjl8hTFOUcY6X11Y2N5gHuCQ12mBJZJlcVYztDNTdq0hobCSIgIAHj8uGJKYQOv2kj-uefP_noDMuuMq_P-3SXzxDpDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سقوط آزاد شاخص بورس استانبول در پی صدور حکم دادگاهی درباره ابطال نتایج رقابتهای درون حزبی حزب اپوزیسیون جمهوریواه خلق</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/SBoxxx/16524" target="_blank">📅 10:46 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16523">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">دولت ترامپ فروش ۱۴ میلیارد دلاری سلاح به تایوان را متوقف کرد  بر اساس اظهارات هونگ کائو، سرپرست وزارت نیروی دریایی آمریکا، دولت ترامپ فروش ۱۴ میلیارد دلار سلاح به تایوان را موقتا متوقف کرده تا ذخایر تسلیحاتی آمریکا برای جنگ با ایران حفظ شود.</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/SBoxxx/16523" target="_blank">📅 10:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16522">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">به نظر معامله بزرگی در راه است.</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/SBoxxx/16522" target="_blank">📅 10:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16521">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">انفجار در ابوظبی!</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/SBoxxx/16521" target="_blank">📅 10:04 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16520">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">وقتی صحبت از عقب ماندگی ذهنی میکنیم منظور ما این است!  رفته با دیوار سفارت آمریکا در ترکیه عکس سلفی گرفته!</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/SBoxxx/16520" target="_blank">📅 10:04 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16519">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iCHx3TCEEDr2zfXqBEclZWsT5dq7qiLFLEtlQwcnB3MxdfGiw0FKtPadJOEYWpQB6btVnr80CnL5d4R7NjMD0QAHY6J715_A7F8xWcnZig0ZPEJ2YmuTihMOL5trjzAQw2ic7rUAOlYA7uBBWjki-5o_gM4JwyBRGtFlP5I5791AjnJonZKuYpWMZYb5idC5t1Yq_dG_lWnszsiNjV0wdOHDTpM5aVUIFB7b2YUk4WXtjvbWCNMUBS39vdZZ2OVetV5wkgC1dOJ_tu_bgoaUv1DNOtk-kpDuBxu_kzeHylf2kwh5pGcXw0E8KS20hPt0Dy0FbUrGvE_VYl2ku4Yeiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۸۰ درصد هم عقب ماندنی ذهنی داشتیم که ۱ درصد آن را جبران کردیم ولی خب هنوز خیلی کار داریم و نباید بهانه بیاوریم.</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/SBoxxx/16519" target="_blank">📅 09:30 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16518">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hNLFWT15YWQ8Gkjd_B2p1CrpXkI-uAbJLGeqiLiXjrc4dWs43knAjIARJBSPezpheWfjcdYeNsEMtqy31lWbjkikT0W5jGmuazgAwIWg6HRvk-DEq07nERQUT-i7FbjHY8gomYGQryuVu6MD2DQ4rjz8oadxVJ_lLn_ESTdKHgVIrXPQy6JJjSi5SkDnMuqzyYbEsFm4KwGGrNncmpUKuM6dGm8ll6D-4XC-63Y-QtUwebGWL-mF2FuiGpw8bKBd07G4zxREPpoGPspZAYE_QSZh50S3ueofe91DJS7QocByCkzxzzj9u0Wq1v0B4VP2wj6q9Uu9DiLXsQ5YhQiXdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت سهام چین</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/SBoxxx/16518" target="_blank">📅 09:17 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16517">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">رئیس کمیته نظامی ناتو:
پهپادها نوعی مسئله انقلابی در میدان نبرد هستند. آن‌ها تنها سلاح نیستند، اما احتمالاً برجسته‌ترین سلاح خواهند بود و بر کل فضای نبرد تأثیر می‌گذارند.
احتمالاً در درگیری‌های آینده، آن‌ها اولین چیزی خواهند بود که در جنگ درگیر می‌شوند. آنچه اساساً آموخته‌ایم این است که آن‌ها به‌طور چشمگیری زمان چرخه کشتار را کاهش می‌دهند.
این موضوع به دقیقه‌ها — یا حتی ثانیه‌ها — برای شناسایی، ردیابی، تحلیل، کشف (شناسایی)، شلیک، ارزیابی خسارت و تغذیه اطلاعات به عملیات بعدی تبدیل می‌شود.</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/SBoxxx/16517" target="_blank">📅 07:50 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16516">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sxd750INPahebUKvPdJF5JEK-Ei4A8bw_RSGC6Un6tfobQIhx1R0etJpiFaV3NckMOyWfqh0pCbZuX47aW8-qXLKOEswrdfoAcVKAajy74SZUUxtYV6-b2p40AyVWJucT5uf2Lc6OgiaTOKxv58LYeFH-1SzXsEnBv3bXr-3abV-Wd4vB3a1jSdBWAnCc9Eruw45FyZpRuzTRl-_pGM19TKR6zsl3xYErgscwJjcXqcKPr-UHrC7Wb_TAdNF2pTZSpQYXr9xOGAHBPlzyRDSw5KCDRUCgIVx3reErROOqwKJgA2ZjCFujPvfuBbpaRTMT54-A3CO3RGKTvr5iPzoRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/SBoxxx/16516" target="_blank">📅 01:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16515">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">این جنگنده ایرانی هم امروز در تهران مشاهده شده که ولی خب.</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/SBoxxx/16515" target="_blank">📅 01:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16514">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">شماها چرا شب جمعه اینقدر میخند؟!</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/SBoxxx/16514" target="_blank">📅 00:14 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16513">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">این همه زحمت میکشیم بهای نفت را بالا ببریم تا هزینه جنگ برای دشمن زیاد بشود آن وقت این دوم خردادی های چهل پدر میزنند زیر کاسه کوزه مان.</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/SBoxxx/16513" target="_blank">📅 00:13 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16511">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">العربیه:   «توافق میان آمریکا و ایران با میانجیگری پاکستان قطعی شده و این توافق ظرف چند ساعت آینده توسط ترامپ علام خواهد شد.  این پیش‌نویس شامل آتش‌بس جامع و فوری در تمام جبهه‌ها،تعهد متقابل به عدم هدف قرار دادن زیرساخت‌ها،تضمین آزادی ناوبری در خلیج فارس و…</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/SBoxxx/16511" target="_blank">📅 00:09 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16510">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ادعای العربیه:
عاصم منیر امشب به تهران نمی‌رود</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/SBoxxx/16510" target="_blank">📅 00:08 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16509">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">العربیه:   «توافق میان آمریکا و ایران با میانجیگری پاکستان قطعی شده و این توافق ظرف چند ساعت آینده توسط ترامپ علام خواهد شد.  این پیش‌نویس شامل آتش‌بس جامع و فوری در تمام جبهه‌ها،تعهد متقابل به عدم هدف قرار دادن زیرساخت‌ها،تضمین آزادی ناوبری در خلیج فارس و…</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/SBoxxx/16509" target="_blank">📅 21:51 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16508">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">العربیه:
«توافق میان آمریکا و ایران با میانجیگری پاکستان قطعی شده و این توافق ظرف چند ساعت آینده توسط ترامپ علام خواهد شد.
این پیش‌نویس شامل آتش‌بس جامع و فوری در تمام جبهه‌ها،تعهد متقابل به عدم هدف قرار دادن زیرساخت‌ها،تضمین آزادی ناوبری در خلیج فارس و تنگه هرمز و مکانیزم نظارتی مشترک است.تحریم‌ها به تدریج در ازای پایبندی ایران برداشته خواهند شد و مذاکرات درباره مسائل باقی‌مانده ظرف هفت روز آغاز می‌شود!»</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/SBoxxx/16508" target="_blank">📅 21:35 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16507">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">فیلد مارشال منیر پاکستان امروز به جای فردا به تهران سفر می‌کند. با این حال، به گزارش‌ها، منیر به ایران سفر نخواهد کرد مگر اینکه نشانه‌هایی از پیشرفت واقعی در پیشنهاد فعلی که ایران در حال بررسی آن است، وجود داشته باشد.
گزارش‌هایی منتشر شده که احتمال توافق قابل قبول میان آمریکا و ایران را کاهش می‌دهد. به گزارش i24 News به نقل از منابع آگاه، آمریکا به اسرائیل اطمینان داده که هر توافقی با ایران شامل خروج کامل اورانیوم غنی‌شده از ایران خواهد بود. با این حال، امروز گزارش‌های رویترز به نقل از مقامات ارشد ایرانی حاکی از آن است که رهبر معظم ایران، آیت‌الله مجتبی خامنه‌ای، به تصمیم‌گیرندگان ارشد ایران دستور داده که با توافقی که اجازه خروج اورانیوم نزدیک به درجه تسلیحاتی ایران از کشور را بدهد، موافقت نکنند.
این در حالی است که فیلد مارشال عاصم منیر، تصمیم‌گیرنده اصلی پاکستان، قرار است فردا به ایران سفر کند و دونالد ترامپ، رئیس‌جمهور آمریکا، می‌گوید زمان برای توافق با ایران رو به پایان است</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/SBoxxx/16507" target="_blank">📅 19:12 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16506">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lsCpxhvxxQVDXLJRhdKJakDDaUFWZYD4e-WfER4dPLkTe65p2B8QReWv0Cscvm7TPET_SEH8cJfa9j1A_gk5NcFIQ1KH4_gowQ8M53QesduHDtY2cHki5F7aYa-np424nHInwjxKAY9Wh1EfgHvJOGxsAJshWrp7nH3BfN9ejmnYAVeOVVZ3Q2dcAz-faxmBzI77cWWM9LuMw11aplA8zcA4bcT4Zb1dfqhoI2gWe88Vd9ezdLanq0jFbxQ32xs1dAV7IKmuPf7Bk-vNNKVA0xZn97uHKruIJGDgr6_vdhETeNFTajRyybFIK1zvC7e9BCETDFC1bK3VDgacMHV08Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاتا الکترونیکس و شرکت هلندی ASML در ماه مه ۲۰۲۶ یک تفاهم‌نامه راهبردی امضا کردند که هدف آن پشتیبانی از راه‌اندازی و توسعه نخستین کارخانه تجاری تولید تراشه‌های نیمه‌هادی هند در شهر دولرا ایالت گجرات است.
این پروژه که ارزش آن حدود ۱۱ میلیارد دلار برآورد می‌شود، یکی از مهم‌ترین گام‌های هند برای ورود جدی به عرصه تولید نیمه‌هادی‌ها به شمار می‌رود. بر اساس این توافق، ASML تجهیزات پیشرفته لیتوگرافی، راهکارهای فنی، آموزش نیروی انسانی و پشتیبانی عملیاتی لازم را در اختیار تاتا قرار خواهد داد.
فناوری لیتوگرافی یکی از حیاتی‌ترین مراحل ساخت تراشه است و ASML در این حوزه جایگاهی تقریباً انحصاری در سطح جهان دارد. انتظار می‌رود کارخانه جدید تراشه‌هایی برای صنایع خودروسازی، ارتباطات، هوش مصنوعی، تلفن همراه و کاربردهای صنعتی تولید کند.
با این حال، این تفاهم‌نامه به معنای انتقال فناوری‌های فوق‌محرمانه و پیشرفته‌ترین دانش فنی ASML، از جمله فناوری ساخت تراشه‌های نسل بسیار پیشرفته، نیست و هند نیز در کوتاه‌مدت به رقیبی برای غول‌های تولید تراشه جهان مانند TSMC و سامسونگ تبدیل نخواهد شد.
تمرکز فعلی این پروژه بیشتر بر تولید تراشه‌های مبتنی بر فناوری‌های بالغ و میان‌رده است. با وجود این، همکاری تاتا و ASML از منظر صنعتی و ژئوپلیتیکی اهمیت فراوانی دارد و نشان می‌دهد هند در حال گذار از یک مرکز طراحی و نرم‌افزار به کشوری با توانمندی واقعی در تولید نیمه‌هادی‌ها است؛ هرچند موفقیت نهایی پروژه به توانایی آن در دستیابی به تولید انبوه، بازدهی اقتصادی و سودآوری پایدار بستگی خواهد داشت.
گفتنی است شرکت بزرگ تاتا توسط پارسیان هند بنیانگذاری شده و مدیریت می شود.</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/SBoxxx/16506" target="_blank">📅 18:00 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16505">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">اورشلیم پست:   ایران پیش از جنگ اخیر ماهانه ۲۰۰ تا ۳۰۰ موشک بالستیک اضافی تولید می‌کرد و تنها در ۸ ماه حدود نیمی از موشک‌ها و نیمی از پرتابگرهای موشکی از دست رفته خود را جایگزین کرده بود.»</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/SBoxxx/16505" target="_blank">📅 15:19 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16504">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GandIOcByF7zLmoeP20Nl4Fb96VhqEiFG9I25pbAojNv_BL2Adqxpq9AyrXBMibJGarF7SdBDsHPJG2iAupdDKSEs6jUOv9JYpwW3BzRw1Pqm_vESp0eZyvl0N-71NI8md2XFEpOB4F5JBBw3B4i0l8RuxM-8UdTurH7M_NmohvjQy5YLuAGuDSOp8INvuNQV6FXO-yjStaQs1THvwpbHAvKfksOSmb-ZDFSzB2-1JW43csG8LA4a3IkklhwWPwmsm9Q9y6l_Vf_dIyFKNHqJgLwGKEbUFOzQRxPM-fqKL-pa-QNk91oSp_-qvGklWWpNs7-huM6d0GzJsPBrEa4pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/SBoxxx/16504" target="_blank">📅 15:04 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16503">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">رویترز:
رهبر ایران دستور داده است که اورانیوم با درجه نزدیک به تولید سلاح باید در ایران باقی بماند</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/SBoxxx/16503" target="_blank">📅 15:03 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16502">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rZZ36Yd-TQ-M8EDD4wEeZJ6Cy3aiNr5sQ-YGnzNx7WDZPgUFZa3yLHUe51ySIm45PIVlPnxOMABvx8M25x7jkqLAy1wMusL3qVFBVhmynobGOTLpQNtRDMZ3kL0Py8PFjRKw620RcBYhdx6QbD4HtP8CD8T2Y3pn9KexgXmdtJLIv18rrUFEgf0HMfh1DaIAVjw4V3dbfFllYaJD-lrRMlh4q-DtexzitwSQYt4XDd7Gxctvb58TR6ukhKRdrd2DVO9hFaUHmgt24FpUzadWW925Mvveb-Zzpol7P-7YFKtOsa13Xc7qKgVklKm_KoNjnGylz5xKbMxJqrpbH_nJYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔷
هوش مصنوعی "بله" همچنان بعنوان جایگزین چت GPT و میرا ، در راستای رفع نیاز کاربران فعالیت می‌کند</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/SBoxxx/16502" target="_blank">📅 13:18 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16501">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n44UQ0VxsBWnFPRF_7-02b8EN9JnAtp6ehirleaDxHjjutn1-684HIGvuTaf27f6GorDhFhC93WUSYUcLdJctG3X55HC_aut9BWazGiVEsoeFIEnl7mOStC7dFbuYxa0LFmV0MQaDBecvBKsKqtnvjeC9B-RvqkTjW3GPB3RViaKplVGwx24PJ7e2Yj71N6EE2etKBbp9ktL6ah0LrDInauMRK8UBbqCh3bL8VFL1x9nDGfOpchtRoPlcujFNmfrIuWnHimWeCLlRJ5pp-5lRarry7wxDWmUCNFC4lWPxakhg6lFWCyvpI8Agrm77We8GjHkT27vdZc4luqOsF5xgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
ایحاد شکاف طبقاتی دیجیتال در ایران طی ۳ ماه گذشته
🟢
در این مدت سهم کاربران اندروید از ترافیک اینترنت ۲۵٪ افت و کاربران آیفون ۱۸۰٪ رشد داشته است
🔴
آمار فوق نشان دهنده خروج میلیون‌ها کاربر حاضر در طبقات میانی مالی جامعه از فضای آنلاین هستش ، به این معنا که کاربران آیفون بطور معمول از طبقات توانمند جامعه از نظر مالی بوده و امکان خرید کانفیگ با هزینه های هنگفت فعلی را دارند و روشن می مانند اما کاربران اندروید که درصد بیشتری از طبقات میانی مالی جامعه را تشکیل می دهند،  امکان تهییه ابزار دسترسی به اینترنت آزاد را نداشته و خاموش شده اند</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/SBoxxx/16501" target="_blank">📅 12:14 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16500">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🛜
روزنامه الاخبار :  اسرائیل درحال برنامه ریزی برای ترورهای گسترده علیه حزب الله لبنان و جمهوری اسلامی ایران است</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/SBoxxx/16500" target="_blank">📅 11:25 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16499">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">خیلی شرط منطقی است، پیشنهاد می شود حتما در شرایط توافق گنجانده بشود</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/SBoxxx/16499" target="_blank">📅 11:03 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16498">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🛜
روزنامه الاخبار
:
اسرائیل درحال برنامه ریزی برای ترورهای گسترده علیه حزب الله لبنان و جمهوری اسلامی ایران است</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/SBoxxx/16498" target="_blank">📅 11:00 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16497">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">خیلی شرط منطقی است، پیشنهاد می شود حتما در شرایط توافق گنجانده بشود</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/SBoxxx/16497" target="_blank">📅 10:40 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16496">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🌊
شریعتمداری؛سردبیر روزنامه کیهان:  تا زمانی که ترامپ را ترور نکنیم ، تنگه هرمز باید به روی شناورهای آمریکایی بسته بماند</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/SBoxxx/16496" target="_blank">📅 10:38 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16495">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🌊
شریعتمداری؛سردبیر روزنامه کیهان
:
تا زمانی که ترامپ را ترور نکنیم ، تنگه هرمز باید به روی شناورهای آمریکایی بسته بماند</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/SBoxxx/16495" target="_blank">📅 10:37 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16494">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">شرکت SpaceX، کمپانی xAI را تملیک کرد و به این ترتیب ارزش کل برآوردی آن در آستانه عرضه اولیه اش به 1200 میلیارد دلار رسید.</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/SBoxxx/16494" target="_blank">📅 09:57 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16493">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">روایت ترامپ از مقابله ناوهای آمریکایی با پهپادهای ایرانی با بهره گیری از سلاح لیزری!</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/SBoxxx/16493" target="_blank">📅 09:36 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16492">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ریزپهپادهای حزب‌الله   فیلم‌هایی از جنوب لبنان تایید کرده‌اند که حزب‌الله بارها اهداف ارتش اسرائیل، به ویژه تانک‌ها را هدف قرار داده است، در حالی که اسرائیل به عمق بیشتری در سرزمین‌های جنوب رود لیتانی فشار می‌آورد   گزارش‌ها تایید می‌کنند که یک حمله پهپادی…</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/SBoxxx/16492" target="_blank">📅 09:32 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16491">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j-0fjaAp2SKh19aSD3xyC1VJlRVhtiXBnZ3a3FVe7OEVCvSiocuIApj2TAsMtuAbzLdBV3Log396P6uj32Sr58GNicg2goYe3olxxUAwa-Ew6PUub2fymzPtuKaPx_51wG1NJs1vIF6fdGhf90xdkkFmabGQRdvuiV-0l2YhoB3FT3jPaOOKLuIslLVbf8Z7Xy6nxPxs160adS6ti4SngPCoIzolfmAiXzpgJsb07ZJ4z0gRoq-PDT4ddwdX5B3uAhVD8BnE8_uMFXt6FXMSOurrcMVy6mR_9vHcmT4CrVUFzk7B76Kji9GX0q1U0SfJv7gGvjbOO-MxykMZGNjCJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در طرح جدید سپاه، کل منطقه بین این 2 خط تیره حوزه دریایی تحت کنترل ایران تعریف شده که ملاحظه می کنید بندر کلیدی فجیره نیز درون این حریم قرار گرفته است.  در واقع آمده اند تا خود فجیره این حریم را تعریف کرده اند تا امارات نتواند از این بندر صادرات جایگزین انجام…</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/SBoxxx/16491" target="_blank">📅 07:34 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16490">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CMSFYow_sib8bPtd6fO68-dlj3ActFIx6y-fxznzD8Vi1N81W4O13PRHe5qhPAp9PSabWiVZZKor40Zy-8JLRv7Ca3eK8GecAJ_gAo-bNo5W20E7ZThIbUsxF_jO3bT_fVwSLeDyxUgN4tc34mbuFClFjadYjSA7J07MYU87WL7yVLZ3yUcRrOwY8ki4h5iHxuCP0WSI22NxHtJnd563j3Qy5Nv8dRIBfU8bDgWi1nZXWMip2JscrizXZ_IfcJzPOEv34X5vkZo3ZuX-RJ3AKjmgKGWLLetQx8j5fyrrRuyp5s4sFcHa7BtzuacRdnihQJHSrPx32QZnvUzCPUPjJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متن کامل گزارش کنگره آمریکا درباره هواگردهای سرنگون شده ارتش این کشور در جنگ با ایران:  بررسی کلی  در ۲۸ فوریه ۲۰۲۶، ایالات متحده آمریکا با هماهنگی اسرائیل، عملیات‌های نظامی علیه ایران را تحت عنوان عملیات خشم حماسی (OEF) آغاز کرد. این درگیری شامل نبردهای هوایی،…</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/SBoxxx/16490" target="_blank">📅 07:28 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16489">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TtcPb9ohQvk3xKvn3BQzCkJy6BdTbtQIvImOQjdg_Rka_xywFBjXckur3q3vc7RQbO8B3LGy9qZZYlGH71DXk-ltCvcm5vBTjheWCu2WmJ1zJYyk-TcKUEcMgsSzatV0w3KGLih2Ng552aXVHtthSCeiQudGbKWBTbRPRf5pKibuLDmSDFXVD8gv31mQ897gO-dOHGcYP4ETT8OCUvhtbyvJo4QlOXlgbf1baFdTa7M9X4GBw9ts7NuEJZxtnjzFEgulaXYkXH-IaZi0N9jMtanGF9kre7pCU8xgEmAgzNvhxF3UWJhVRUranTHe2G7uYuyyjqNpsIrVUi6pFT554g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران، احتمالاً با کمک روسیه، الگوهای پروازی جنگنده های آمریکا را نقشه‌برداری کرده و خود را در موقعیت بهتری برای استقرار سیستم‌های دفاع هوایی خود قرار داده است.
یک مقام آمریکایی اظهار داشت که نابودی یک جنگنده اف-۱۵ در طول جنگ نشانه‌ای از این بود که الگوهای پروازی آمریکا برای ایران قابل پیش‌بینی‌تر شده‌اند و با طولانی‌تر شدن جنگ، ایران به موفقیت در نابودی هواپیماهای جنگی آمریکا نزدیک‌تر می‌شد.
ممکن است روسیه به ایران کمک کرده باشد تا الگوهای پروازی آمریکا را نقشه‌برداری کند تا تجهیزات نظامی و سیستم‌های دفاع هوایی را با دقت بیشتری مستقر کند.</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/SBoxxx/16489" target="_blank">📅 05:24 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16488">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">کانال ۱۴ اسراییل:
نیروهای آمریکایی یک نفتکش ایرانی را در خلیج عمان توقیف کردند .</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/SBoxxx/16488" target="_blank">📅 05:16 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16487">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
کانال ۱۴ اسرائیل
:
باید به یاد داشته باشیم که ترامپ یک تاجر است و اظهارات امروز او با هدف تثبیت قیمت نفت بوده</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/SBoxxx/16487" target="_blank">📅 23:48 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16486">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">توماس ماسی جمهوری‌خواه ضد اسرائیل در انتخابات مقدماتی در برابر نامزد حمایت‌شده توسط ترامپ شکست خورد
توماس ماسی، نماینده جمهوری‌خواه کنتاکی که از سال ۲۰۱۳ در مجلس نمایندگان آمریکا فعالیت می‌کرد، پس از باخت در انتخابات مقدماتی حزب خود به اد گالرین، کنگره را ترک خواهد کرد. ماسی تنها جمهوری‌خواه بود که در پی حمله حماس به اسرائیل در اکتبر ۲۰۲۳، از حمایت از این کشور خودداری کرد و گاهی در رای‌گیری‌های ضد اسرائیل، همراه با دموکرات‌های رادیکال رای می‌داد.
در شب انتخابات، ماسی با کنایه‌ای تیز گفت:
«دیرتر خارج شدم، چون باید حریفم را پیدا می‌کردم تا باخت را اعتراف کنم. و مدتی طول کشید تا اد گالرین را در تل‌آویو پیدا کنم.»
گالرین، که مورد حمایت دونالد ترامپ و کمیته‌های حامی اسرائیل بود، با کسب
۵۵ درصد آراء
پیروز شد.
ائتلاف یهودیان جمهوری‌خواه، که مدت‌ها با ماسی مخالف بود، این پیروزی را به عنوان پیامی واضح از جمهوری‌خواهان کنتاکی دانست:
«در حزب جمهوری‌خواه جایی برای کسانی که پشت به برنامه MAGA می‌کنند، وجود ندارد.»
آنها گالرین را یک میهن‌دوست واقعی توصیف کردند و رفتار ماسی را در طول کمپین انتخاباتی، از جمله تبلیغات ضد سامی‌گری او، محکوم کردند. در یکی از این تبلیغات، که به شدّت مورد انتقاد قرار گرفت، ماسی مدعی شده بود که پیروزی گالرین «دیوانگی بیدار ترنس» را به کنتاکی خواهد آورد و این کار را به درخواست پول سینگر، میلیاردر یهودی حامی جمهوری‌خواهان، انجام می‌دهد. در این تبلیغ، یک ستاره داود رنگین‌کمانی کنار عکس سینگر قرار داده شده بود.
با خروج ماسی، حزب جمهوری‌خواه گامی دیگر در جهت حمایت از اسرائیل برداشت. این انتخابات مقدماتی نشان داد که در حزب جمهوری‌خواه، مواضع ضد اسرائیل دیگر جایگاهی ندارد.</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/SBoxxx/16486" target="_blank">📅 23:40 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16485">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">خبرنگار آکصیوص:
ترامپ به نتانیاهو گفت که میانجی‌گران در حال کار بر روی یک نامه نیت هستند که هم ایالات متحده و هم ایران آن را برای پایان دادن رسمی به جنگ امضا خواهند کرد و دوره ۳۰ روزه مذاکرات در مورد مسائل مانند برنامه هسته‌ای ایران و بازگشایی تنگه هرمز را آغاز کنند، یک منبع آمریکایی گفت</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/SBoxxx/16485" target="_blank">📅 23:13 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16484">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">گزارش موسسه مطالعات جنگ از کمک های نظامی و اطلاعاتی روسیه و چین به ایران  روسیه از تلاش‌های ایران برای بازسازی توانمندی‌های نظامی خود در دوره آتش‌بس حمایت می‌کند. نیویورک تایمز به نقل از مقامات آمریکایی گزارش داد که روسیه قطعات پهپاد را از طریق دریای خزر به…</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/SBoxxx/16484" target="_blank">📅 22:44 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16483">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ترامپ در مورد تعلیق تحریم‌های نفتی برای ایران:
هیچ کاری انجام نمی‌دهم، مگر اینکه توافق‌نامه‌ای امضا شود.</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/SBoxxx/16483" target="_blank">📅 22:38 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16482">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ترامپ:   نتانیاهو هر کاری من بخواهم انجام می‌دهد</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/SBoxxx/16482" target="_blank">📅 20:11 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16481">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🇺🇸
🇮🇱
ترامپ می‌گوید پس از پایان ریاست جمهوری‌اش به اسرائیل خواهد رفت تا برای نخست‌وزیری کاندیدا شود.</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/SBoxxx/16481" target="_blank">📅 20:11 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16480">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ترامپ: درگیری‌های بیشتری در راه است مگر اینکه ایران عاقلانه عمل کند.</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/SBoxxx/16480" target="_blank">📅 20:00 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16479">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">#US10Y — H4  فعلاً موفق شده با این سیرک امروزش مقداری نرخ بازده و نفت را همزمان سرکوب کند.   خواهیم دید چه خواهدشد.</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/SBoxxx/16479" target="_blank">📅 19:25 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16478">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KCPFw4YXar9eyJV2ZO6katvH6YgMv4yrTCM5vvTsZwqE0yqm3ozI_nKz83aHgQ6Dxn4P6ALLs0Gk77aDV03pFBcc3c9QM45VlvxmVBkc7Vi_BB9DqlK2QRwNVi8FJ0W7Ng9W0vnNbGBUCiUJtu1v6ZlVoSLO7UoLp3cTmXYWIz8C3vsT9IkxmNdxbMfnT7iCN_13wMpxn-bUdx02rjSNPx0O_JloJqStN9KIQ2HZ-7mkbg4DEIFAn7ih5ZTG5_yDN6kIjw9dizh2hIpnMygtTpUVrkyu4Mf2qUwQnMIEhmepkhB1lktxXSRrsiHtMOJ1XZvwA5EaxQtlZ4-xYD5i7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#URA — D  #سهام_خارجی  این یک فرصت ویژه ایرانیان خارج کشور است. صندوق ETF اورانیوم می تواند در قالب موج 5 خود دستکم 70 درصد رشد داشته باشد که در چارت می بینید.  نظر به مسخره بازی ما در تنگه هرمز، احتمال هجوم سرمایه ها به انرژی های جایگزین بالاست و انرژی هسته…</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/SBoxxx/16478" target="_blank">📅 19:06 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16477">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fEy8ocpQdbO6RG6lwMmQ-8NqgkTlwLXME9RqEelSqmuOy0719QbLdMQHeMam4uGz0NpU2bPhn5TFFPBcuOlad7puyUm0Aa8fKP4oErOE-k8-x7J77CfOwxgPMjgzXI287g37bVk7pP7hi65aYBn-ijr6Mu8ysy7ZDYB7Jn4J-DcfmPsjOVjI4V4dPtlTfTWmvxHwp44L2zoT5PaKT_jujdp6GCO9TV2TdC1ppkmbRDPaEcouSXQlBIeR43tkxG918ICvVoTfefgG-gb29Hx7xaoVUCsEjyEc91H7yZGhnSKAiUDq6ZrlO4wQHaOif6xrpg30jdeHaRYaKcq_4e8NUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ بازده اوراق قرضه 10-ساله خزانه داری آمریکا سقف مثلث را شکسته و عازم سطوح بالاتر است که فشار سنگینی روی دولت فدرال برای تامین مالی اش وارد می کند.  ترامپ اگر تنگه را باز نکند، بازی اش با نفت میتواند از کنترلش خارج بشود.</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/SBoxxx/16477" target="_blank">📅 18:57 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16476">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">❗
⚠️
ترامپ: آمریکا در «مراحل نهایی» مذاکرات با ایران است</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/SBoxxx/16476" target="_blank">📅 18:48 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16475">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🇺🇸
🇮🇱
ترامپ می‌گوید پس از پایان ریاست جمهوری‌اش به اسرائیل خواهد رفت تا برای نخست‌وزیری کاندیدا شود.</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/SBoxxx/16475" target="_blank">📅 18:18 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16474">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔻
ریاست مجلس
:
دشمن از تجاوز مجدد به ما ، پشیمان خواهد شد</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/SBoxxx/16474" target="_blank">📅 18:14 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16473">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">⛔️
اخطار قوه قضائیه بابت برخورد با کشت خشخاش</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/SBoxxx/16473" target="_blank">📅 12:22 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16472">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">به خدا قسم این مردک روانی است</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/SBoxxx/16472" target="_blank">📅 08:44 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16471">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LhYuJBXip489XPULFL5mr4kZBS_ueQ-p_rwLtGwtoKIiOkWxiylT0IjzVD1kU1xRd1xExqmWvb0gHtJNnNJmmlOT1_NmP2Ii4XarR8-K14Am7Hzjbv1xpd8XNBQw5RXnK0vIKOkStUB7R7bJfyCLWrc8PbE_JgRZ0LU1Nmbt3HFFtiIiK-aAVNyYlqeAXb1kV_-TSFob8sdHhs6XOXt-ngH8gQOsHp4Qev43KWMeJR8qxQb3O_mtlYgOb4aIkIojNK36dy22hV8RA6JiDJXvHaYBj1HHen1rgIh21ZCzWFpmvZG76-OzXi19xG3JhCYV7MyTvuNzM9SR6PPJNd78SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نگرانی هند از ادامه تسلیح پاکستان توسط چین  پویایی در حال تحول قدرت هوایی بین هند و پاکستان وارد مرحله‌ای بحرانی می‌شود که عمدتاً ناشی از ادغام فناوری پیشرفته موشکی چین توسط پاکستان است.   نگرانی ویژه کنونی هند ، استفاده گسترده از موشک هوا به هوای برد فراتر…</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/SBoxxx/16471" target="_blank">📅 07:47 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16470">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">متن کامل گزارش کنگره آمریکا درباره هواگردهای سرنگون شده ارتش این کشور در جنگ با ایران:  بررسی کلی  در ۲۸ فوریه ۲۰۲۶، ایالات متحده آمریکا با هماهنگی اسرائیل، عملیات‌های نظامی علیه ایران را تحت عنوان عملیات خشم حماسی (OEF) آغاز کرد. این درگیری شامل نبردهای هوایی،…</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/SBoxxx/16470" target="_blank">📅 01:08 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16469">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">متن کامل گزارش کنگره آمریکا درباره هواگردهای سرنگون شده ارتش این کشور در جنگ با ایران:
بررسی کلی
در ۲۸ فوریه ۲۰۲۶، ایالات متحده آمریکا با هماهنگی اسرائیل، عملیات‌های نظامی علیه ایران را تحت عنوان عملیات خشم حماسی (OEF) آغاز کرد. این درگیری شامل نبردهای هوایی، دریایی و موشکی در سراسر خاورمیانه بوده است. سرعت فعالیت‌های رزمی در جریان آتش‌بس در آوریل کاهش یافت. در عرض چند هفته، برخی حملات از سر گرفته شدند و شرایط همچنان متغیر است.
وزارت دفاع (DOD، که «از یک نام ثانویه وزارت جنگ» استفاده می‌کند، طبق دستور اجرایی ۱۴۳۴۷ مورخ ۵ سپتامبر ۲۰۲۵) ارزیابی جامعی از تلفات رزمی در عملیات خشم حماسی منتشر نکرده است. در جریان جلسه استماع ۱۲ مه ۲۰۲۶، حسابرس موقت پنتاگون جولز دبلیو. هورست سوم شهادت داد که برآورد هزینه‌های وزارت دفاع برای عملیات نظامی در ایران به ۲۹ میلیارد دلار افزایش یافته است. او گفت: «بخش زیادی از این افزایش ناشی از برآورد دقیق‌تر هزینه‌های تعمیر یا جایگزینی تجهیزات است.»
در اینجا ۴۲ فروند هواپیمای بال ثابت یا بال گرد، از جمله هواپیماهای بدون سرنشین (پهپادها)، که طبق گزارش‌های خبری و بیانیه‌های وزارت دفاع و فرماندهی مرکزی آمریکا (CENTCOM) در عملیات خشم حماسی از دست رفته یا آسیب دیده‌اند، فهرست شده است. تعداد هواپیماهای آسیب دیده یا نابود شده ممکن است به دلیل عوامل متعدد، از جمله طبقه‌بندی، فعالیت رزمی جاری و نسبت‌دهی، قابل بازنگری باشد.
گزارش‌های تلفات و آسیب‌های هواپیماهای عملیات خشم حماسی
چهار فروند جنگنده F-15E استرایک ایگل
در ۲ مارس ۲۰۲۶، فرماندهی مرکزی گزارش داد که سه فروند F-15E بر اثر آتش دوستانه بر فراز کویت سرنگون و نابود شدند؛ هر 6 خدمه هوایی به سلامت بیرون پریدند و نجات یافتند.
در ۵ آوریل ۲۰۲۶، فرماندهی مرکزی گزارش داد که یک فروند F-15E در جریان عملیات رزمی بر فراز ایران سرنگون و نابود شد؛ هر دو خدمه هوایی در عملیات‌های جداگانه جستجو و نجات به سلامت بازیابی شدند.
یک فروند جنگنده F-35A لایتنینگ II
در ۱۹ مارس ۲۰۲۶، یک مقاله خبری گزارش داد که آتش زمینی ایران یک فروند F-35A را در جریان عملیات رزمی بر فراز ایران آسیب زد.
یک فروند هواپیمای تهاجمی زمینی A-10 تاندر بولت II
در کنفرانس خبری ۶ آوریل ۲۰۲۶، ژنرال دن کین، رئیس ستاد مشترک نیروهای هوایی، اعلام کرد که در ۳ آوریل، آتش دشمن به یک فروند A-10 اصابت کرد که پس از آن سقوط کرد و در عملیات جستجو و نجات نابود شد؛ خلبان بیرون پرید و به سلامت نجات یافت.
هفت فروند هواپیمای سوخت‌رسان هوایی KC-135 استراتوتانکر
در ۱۲ مارس ۲۰۲۶، فرماندهی مرکزی گزارش داد که دو فروند KC-135 در حادثه‌ای بر فراز فضای هوایی دوستانه درگیر شدند؛ یک هواپیما در عراق سقوط کرد که منجر به کشته شدن هر شش خدمه هوایی شد. فروند دوم KC-135 در منطقه‌ای نامعلوم که نیروهای آمریکایی مستقر هستند، به صورت اضطراری فرود آمد.
در ۱۴ مارس ۲۰۲۶، یک مقاله خبری گزارش داد که پنج فروند KC-135 در پایگاه هوایی پرنس سلطان در عربستان سعودی در جریان حمله موشکی و پهپادی ایران آسیب دیدند.
یک فروند هواپیمای هشدار و کنترل هوابرد E-3 سنتری (AWACS)
در ۲۸ مارس ۲۰۲۶، یک مقاله خبری گزارش داد که یک فروند E-3 در پایگاه هوایی پرنس سلطان در عربستان سعودی در جریان حمله موشکی و پهپادی ایران مورد اصابت قرار گرفت و آسیب دید. در ۷ مه ۲۰۲۶، یک مقاله خبری گزارش داد که E-3 در یک مسیر تاکسی بدون حفاظت پارک شده بود.
دو فروند هواپیمای عملیات ویژه MC-130J کماندو II
در ۵ آوریل ۲۰۲۶، یک مقاله خبری گزارش داد که دو فروند MC-130J که از عملیات جستجو و نجات برای یک F-15E سرنگون شده حمایت می‌کردند، پس از اینکه قادر به ترک محل نبودند، عمداً در ایران روی زمین نابود شدند؛ همه خدمه هوایی به سلامت تخلیه شدند.
یک فروند بالگرد جستجو و نجات رزمی HH-60W جولی گرین II
در ۶ آوریل ۲۰۲۶، ژنرال کین در یک کنفرانس خبری گفت که در ۵ آوریل، یک فروند HH-60W در جریان حمایت از عملیات جستجو و نجات برای یک F-15E سرنگون شده در ایران، از آتش سلاح‌های سبک آسیب دید.
بیست و چهار فروند هواپیمای بدون سرنشین MQ-9 ریپر با ارتفاع متوسط و مداومت طولانی
در ۹ آوریل ۲۰۲۶، یک مقاله خبری گزارش داد که ارتش آمریکا از آغاز عملیات نظامی علیه ایران، ۲۴ فروند MQ-9 ریپر را از دست داده است.
یک فروند هواپیمای بدون سرنشین MQ-4C تریتون با ارتفاع بالا و مداومت طولانی
در ۱۴ آوریل ۲۰۲۶، یک مقاله خبری با استناد به یک سند نیروی دریایی آمریکا گزارش داد که یک فروند MQ-4C در یک حادثه سقوط کرده است.</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/SBoxxx/16469" target="_blank">📅 01:02 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16468">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eXdhDOYaknl_28BSbjRg__3R8PsCb_w1cJREecS6pqk2tC-uFvMNQVLZJ99epNA8QW_7e2LLEGBGaTGQDNIb3kpOTkvddUKOiHJF0gEtCv4vZudwebOxkbg-9IUByjuGqH3566E2sZWJ0xOmYefpgZDfYGGm_6MO3rjXs2XVBV8qMJUIf-uSK6z5QImvuvMH8oeZSBPwdqTnOS6CjyplyKk_F0NDKgVOK2P5MhLTabOPuq4xnJ8O2vnZTbQlj8b2vKW3yVEmLN--6k6ZmVtjHD7B-nD4urW_8BlvltimgcGT9Ibjn8AxSyBHbuc7e9i7LrP9ouTyiTmdHVZYuVtLfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظرم با توجه به اینکه این بار نه نفت افت کرد و نه نرخ های بازده خزانه داری و عملاً توییت مثلاً صلح طلبانه ترامپ بی اثر بود، هر لحظه احتمال تهاجم نظامی آمریکا و اسرائیل می رود.</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/SBoxxx/16468" target="_blank">📅 00:33 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16467">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">خداوکیلی مملکت عجیبی داریم!
انفجار روی می‌دهد دلیلش نامشخص !
گردوغبار همه جا را می‌گیرد دلیلش نامشخص!
وزیرخارجه مملکت به نیویورک می‌رود نماینده مجلس خبر ندارد!
سبحان الله !</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/SBoxxx/16467" target="_blank">📅 00:01 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16466">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">خبرگزاری مهر ایران: صدای انفجار در جزیره قشم شنیده شد، علت نامشخص است.</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/SBoxxx/16466" target="_blank">📅 00:00 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16465">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">خضریان، عضو کمیسیون امنیت ملی مجلس:
امیدوارم خبر سفر عراقچی به نیویورک برای مذاکره در خصوص تنگه هرمز دروغ باشد
چرا ما در خصوص موضوع تنگه هرمز باید در خاک دشمن مذاکره کنیم؟</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/SBoxxx/16465" target="_blank">📅 23:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16464">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ترامپ در حال ساخت یک پناهگاه زیر سالن باله است
او می‌گوید بیمارستان، تأسیسات تحقیقاتی و اتاق‌های جلسه برای ارتش، در حال ساخت زیر سالن باله کاخ سفید هستند.</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/SBoxxx/16464" target="_blank">📅 22:38 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16463">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">نیروی دریایی آمریکا یک نفتکش متعلق به شرکت ملی نفت ایران با بیش از یک میلیون بشکه نفت خام  را در اقیانوس هند توقیف کرد.</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/SBoxxx/16463" target="_blank">📅 22:27 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16462">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">نیروی دریایی آمریکا یک نفتکش متعلق به شرکت ملی نفت ایران با بیش از یک میلیون بشکه نفت خام  را در اقیانوس هند توقیف کرد.</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/SBoxxx/16462" target="_blank">📅 22:21 · 29 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
