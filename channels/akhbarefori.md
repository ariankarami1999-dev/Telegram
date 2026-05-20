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
<img src="https://cdn4.telesco.pe/file/OFE5oDEnUDY7AjKDgSgdiI62nAypcSxnUGYpltYJsH8f_4zpEte5PSMxJ42R1cS1sHLjaiT9mEb7_Q-SES6WtrOwkif63jmAmw7xpvcdZ4QO39r5S3GJtPo_qerBfbjaRnMu25o-AEolm56o2g69DwVy0uphkwQogBQfTEMrNbWbRsMdVCTF7mVessPMSjB1cl-BM7IfbW4F--3-KRQlTj7eZMp1Q9xR00nsZvd-zXL8jVbTg1YGuh-3M0gy9cgZsOLQfwx-uQRoyk9hdDHr7hkUsK0eDq9tJYC6LVxvNLG2hd4dRS8NszTqzrq89VMlSvH76l6M9zjjOBHOog1ufw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 3.99M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-30 03:34:16</div>
<hr>

<div class="tg-post" id="msg-653144">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ua5SeezokOZngeo_xFfBTcjLwe3LdDkT5H12IywxfBwz7UnpJDr0Ig6mQqfFZ5d8YbR0H-gp9mHX7UU2GfXk_caIlG58abdfq4eq57zXBuIUDp1zLHlI8p0qC8sQ-oQ8R2kEggfUu_FTwC3jfvHtGNiTZNtl9qHTmTH80MRnCGSYoPJ_D7YY4TgHVfDgi41-JtUGxfLalUbbNyBG_hox4dm_6maBBMdO8WP92Gy7QeSl58tbzZDt1neklaiqbUwn-nE2ZxdTDc7quRfl3QPcgyaAq3EytAQ4U-jfK-qJQb0t6twvhwE3B74tw3kcDDvY8zTy60TnePIAttt5j1FRpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تأکید بقائی بر محاکمه و پاسخگویی آمران و عاملان جنایت میناب
🔹
سخنگوی وزارت امور خارجه بامداد امروز با بیان اینکه تقلای شرم‌آور آمریکا برای توجیه جنایت میناب نمی‌تواند ماهیت این جنایت را مخفی کند، گفت: فرماندهان نظامی و مقامات آمریکایی که مسئول صدور دستور و اجرای این حمله فاجعه‌بار بوده‌اند، باید طبق قوانین بین‌المللی کاملاً پاسخگو و محاکمه شوند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.27K · <a href="https://t.me/akhbarefori/653144" target="_blank">📅 02:41 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653143">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gu1yHQqYSoTG114XP_gCYYEVz1wtQte7-twwElrFHwswa3COo-mbRTm_qOVtKlFTp9OCvSFgXyxjW44obpjSBFB7LCAX8U9_I97c2O9FyjlzydtQGPzpGIJjFqesuB9dGA0oIKO5t7hF0xWEsYUcJE6DtlKHNsE0DJ4v7Nhk58dbilJNCvbMGOCsIPocrJKtM391cscxlLISWk1zDGQNY1ub8Av49v8n-i_iHZKLVKDKOGk5WMtA97dyiQ5M_hBsJ-B79JBEXIuuiMP3HzOCByYV0UB0FmNd9rgPbS4ells9dfYgoRy7zzGIG1xaKDQ-toBiWmmhmYCbhK26B9yYJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نمایندگی جمهوری اسلامی ایران در سازمان ملل متحد: ایالات متحده آمریکا از شورای امنیت سازمان ملل برای انتشار دروغ و اتهامات نادرست علیه جمهوری اسلامی ایران و برنامه هسته ای آن سوءاستفاده می کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/akhbarefori/653143" target="_blank">📅 02:34 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653142">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
دستگیری مزدور موساد در شهر ری
🔹
دادستان شهرستان ری: یکی از عناصر مرتبط با سرویس جاسوسی رژیم صهیونیستی (موساد) در جنوب شهرستان ری، شناسایی و بازداشت شد.
🔹
هم‌اکنون روند رسیدگی به پرونده وی در حال انجام است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/akhbarefori/653142" target="_blank">📅 02:22 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653141">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gQaCo8Cs-qqLIvzSPiPY1w8eEk9R6Ll6GNmCcwTZLUM7NstyjrmqaKzekTuqG093tk2XqHlDafC2JTs9-A87Jy6G2gKZCL6gCsWGLezARguZrzwZqpfg6HLrEPp5R0k_fdi-WMajWZwsVqNfxOuB8Dt7yZEciZ2fZh3S79Qyp9RWDXb28qgWm0RcVs-vuJ_xT7sYbJ0oazPrkhBqWKJnNA0H8MAhql1bPPqpxQ3TeV977khU2BDmi6xHm_UQcJqhYyGHwg2CXpBWMO2omKAOT8l_sG4k_Brc13J6ogxTrz3K2E-zTAt1LQo4ImwnM7biHn2vJ4Qp-3hf4jL2LRwtEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویب طرح پایان جنگ ایران در سنای آمریکا
🔹
سناتورهای آمریکایی بامداد سه‌شنبه طرح محدود کردن اختیارات جنگی رئیس جمهور این کشور علیه ایران را، بعد از ۷ بار رد شدن، تصویب کردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/akhbarefori/653141" target="_blank">📅 01:43 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653140">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iKc9azQ3jRncEG1rFT-_T_yq9WyTqF4j1Ry75509hU3aJo3UdgN8BUXWncCadNNdLzkfJ3HaJEyrn1nISyILhn5X5l05cuUtpNoE5xaGs5HToIsOyPAjykvIetYsSrqn4QuYrpPpLMfv-BBH2KJG5pvOT7qY9nOr5nGltxLRAwo-iFUmZ5kTAz_1dCFxco4cumNsa9y5FAYulA2gp8rpYLX1Hv3HWf-Pv19ATyr3KFA7_t1_tAPSJmWtbtmE724OWL5cl5QwufDRHi7jIuYo_slLI53S-YXLXJ5KzHlWkOTDL1DNbB0q5tUK_c_Y6sbS1-tzUJOYArEuOKUr6IIBOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رویترز از تصمیم ترامپ برای توقف حمایت نظامی آمریکا از اروپا خبر داد
🔹
ترامپ قصد دارد سهم توانمندی‌های نظامی خود را که برای کمک به متحدان اروپایی در زمان بحران‌های بزرگ در نظر گرفته شده، به شدت کاهش دهد.
🔹
پنتاگون تصمیم گرفته است تعهدات خود را در این زمینه به طور قابل توجهی کم کند و انتظار می‌رود این تصمیم روز جمعه طی نشست مقامات ارشد دفاعی ناتو در بروکسل اعلام رسمی شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/akhbarefori/653140" target="_blank">📅 01:27 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653139">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cGkrLq4IgDMlQwdH2ZjbTEwTfG6la0K1vCDTZ_R_EI2GfJ-PjidyVxkixgzNitoqy4XnTOtGEYKy3J85gZuUgsuHN5DLwEtCMcWdtTpF110EoWMf8fepf-Uz6GP5tGpB8ZWbBjDiQHFcb7QtqTayjVBkHZD43kXUYCGx3aWlRFj4y3L0jk78-Sxv85ZFalp4-5clstZtsZrKSr2pjUWi-i8Su7tBCSiJKuml1uuaK-2qReqbXIlrnvBtddvRByGJXI3UnVMEk5kgWJ-1VErATrSHLDyapfuHfajdAg188FxfPBXUvFnb9LnsLzGKbXexcvpIsxQ0_XE8WVjoVe_YXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بقائی: تقلای شرم‌آور آمریکا برای توجیه جنایت میناب، ماهیت این جنایت را مخفی نمی‌کند
🔹
سخنگوی وزارت امور خارجه، در واکنش به ادعای فرماندهی مرکزی ایالات متحده آمریکا درباره دلیل هدف قرار دادن مدرسه شجره طیبه میناب و کشتار بیش از ۱۷۰ دانش‌آموز و معلم، نوشت:
🔹
ادعای فرماندهی مرکزی ایالات متحده آمریکا (سنتکام) مبنی بر اینکه مدرسه ابتدایی شجره طیبه میناب در محدوده یک مرکز موشکی بوده است، کاملاً بی‌اساس و انحرافی است. این تحریف آشکار، تلاشی واضح برای پنهان کردن ماهیت واقعی حملات موشکی ۲۸ فوریه است که موجب قتل عام بیش از ۱۷۰ دانش‌آموز و معلمانشان شد.
🔹
هدف قرار دادن یک مرکز آموزشی فعال در ساعات مدرسه، نقض فاحش حقوق بشردوستانه بین‌المللی و مصداق بارز جنایت جنگی به شمار می‌رود.
🔹
ماهیت غیرنظامی این مکان را نمی‌توان با توجیهات فنی و بازی با کلمات پوشاند. فرماندهان نظامی و مقامات آمریکایی که مسئول صدور دستور و اجرای این حمله فاجعه‌بار بوده‌اند، باید طبق قوانین بین‌المللی کاملاً پاسخگو و محاکمه شوند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/akhbarefori/653139" target="_blank">📅 00:46 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653138">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PzNKcjve1o5a6vksl3122v-SU_S0fJeSjNyCl_eyWP7u5f6dC0Kh7lRzioyyvQkTaPtOv9Nf-X9lHCYSjO5pXC8_LfCFulDAirUXjwIaCs_Qc3cje0tWfax8-4ckZLDeAsC9CRdDQtLM5CWsMj9h28vK1VjZTRFMyLncw2BaJt1OYPhYKhiw5Il7fD23DJ_x1DeKC0iRzCVtkBU8_flewUDfMm9EYyjeO-P8RwvujTvSmrZmkAy15PrhFzwzKcwXp1CsHTNKxdP_R-_2t3C_qO27YYPFYaFX7hePqVxk8__YE8WQpFuah28gli6Kxn1RkrWx6EF7WcVs2aGEB7t2pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عراقچی: مطمئن باشید بازگشت به میدان جنگ با شگفتی‌های زیادی همراه خواهد بود
🔹
ماه‌ها پس از آغاز جنگ علیه ایران، کنگره آمریکا به نابودی ده‌ها فروند هواپیما به ارزش میلیاردها دلار اذعان کرد.
🔹
اکنون به‌طور رسمی تأیید شده است که نیروهای مسلح قدرتمند ما نخستین نیرویی در جهان بودند که جنگنده پیشرفته و پرآوازه F-۳۵ را سرنگون کردند.
🔹
با درس‌هایی که آموخته‌ایم و دانشی که به دست آورده‌ایم، مطمئن باشید بازگشت به میدان جنگ با شگفتی‌های بسیار بیشتری همراه خواهد بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/akhbarefori/653138" target="_blank">📅 00:40 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653137">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6df5fd590b.mp4?token=bAxdDFHC4eMKE9-tCvfpb_c7rYaODmBXYpfVs2pysbHZm-26p2hfQDIvrd-Wl_7uiTZYdtt3l7GlHA5-2i1e5HBLaUCB2Evwc7OSkUrLu6zJQHD1R9DtGeDp4QKxeo-F8pwXJi9IIt88D6fkn9iu2bGuv5VrLALKGKFozJ7Hdm-rtXyjDdXEBPttvyLCtEzBu25NUf3C9IL0YzQOMZVkXJNm9apgGQztL0ZC3TeXMX6e9DRyYLLo1TFqxjoO9yex00ze0_td-TrGYE_IhqaHmf-cKCF5QaXdPBB_1HgdzpweExlBkee3I_lRkmiOk6Cwhg_qq08SLprjJa9oPSFqwD9MnfMQlO8DB7X6AgWJgyopOCKwCeSn35ePI8ayPk5JnASMaYVou3YIpiGQMKyLctVGDJL8b8Wf4xSmTo8Cg6anlu5EBXZvgnsu5mR3Il22Amt-9H8azvICkt_xaNdfNcyT6froYIxTEyr-rKP0lqemGrgInxeakruX6Ez6YyBOLRn4YF81CM5ztG5yd3lE1Qv6fqUU8giEM_P312W1KuAkbhrlwMMqFZ0hEzGpZwwbKTieZXm6NCq8ZUGfwYt9fENfY3GJ6LOhiQyMHZYWBPyOOGQJah8Y1wDitLiBtNUFhz2WKsGj4p7GQhssyAtG_LRsXtcb4Y5cEkL6ikvov1k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6df5fd590b.mp4?token=bAxdDFHC4eMKE9-tCvfpb_c7rYaODmBXYpfVs2pysbHZm-26p2hfQDIvrd-Wl_7uiTZYdtt3l7GlHA5-2i1e5HBLaUCB2Evwc7OSkUrLu6zJQHD1R9DtGeDp4QKxeo-F8pwXJi9IIt88D6fkn9iu2bGuv5VrLALKGKFozJ7Hdm-rtXyjDdXEBPttvyLCtEzBu25NUf3C9IL0YzQOMZVkXJNm9apgGQztL0ZC3TeXMX6e9DRyYLLo1TFqxjoO9yex00ze0_td-TrGYE_IhqaHmf-cKCF5QaXdPBB_1HgdzpweExlBkee3I_lRkmiOk6Cwhg_qq08SLprjJa9oPSFqwD9MnfMQlO8DB7X6AgWJgyopOCKwCeSn35ePI8ayPk5JnASMaYVou3YIpiGQMKyLctVGDJL8b8Wf4xSmTo8Cg6anlu5EBXZvgnsu5mR3Il22Amt-9H8azvICkt_xaNdfNcyT6froYIxTEyr-rKP0lqemGrgInxeakruX6Ez6YyBOLRn4YF81CM5ztG5yd3lE1Qv6fqUU8giEM_P312W1KuAkbhrlwMMqFZ0hEzGpZwwbKTieZXm6NCq8ZUGfwYt9fENfY3GJ6LOhiQyMHZYWBPyOOGQJah8Y1wDitLiBtNUFhz2WKsGj4p7GQhssyAtG_LRsXtcb4Y5cEkL6ikvov1k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نماینده مجلس: تثبیت تنگه هرمز به همت شهید تنگسیری و رزمندگان عزیز ما، با تدابیر مقام معظم رهبری، در جنگ اتفاق افتاده
🔹
روح‌الله متفکرآزاد، عضو هیات‌ رئیسه مجلس: تنگه هرمز آب‌های استراتژیک ملی ماست. به همت شهید تنگسیری و رزمندگان عزیز ما، با تدابیر مقام معظم رهبری، تثبیت این تنگه در جنگ اتفاق افتاده.
🔹
ما تنگه را بسته نگه نخواهیم داشت. موضوع، موضوع حکمرانی ماست که باید تثبیت بشود.
🔹
هرکجا نیاز شد برویم به سمت سیاست‌گذاری اجرایی آن هم شعام، هم مجلس با تمام قوا انجام خواهد داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/akhbarefori/653137" target="_blank">📅 00:25 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653136">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
۱۰ شهید در تجاوز صهیونیست‌ها به شهر صور لبنان
🔹
وزارت بهداشت لبنان: در حمله هوایی رژیم صهیونیستی به دیر قانون النهر در شهرستان صور در جنوب لبنان بر اساس امار اولیه و غیرنهایی، دست کم ۱۰ نفر از جمله سه کودک و سه زن شهید و سه نفر از جمله یک کودک نیز زخمی شدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/akhbarefori/653136" target="_blank">📅 00:19 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653135">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mGsX-udoAuOG5IiDVhxgU69OM68b7vEKhoPwMZZu0YLff2kZkhEL9CWFgWEGCBrQiTNCurm7QKivnSDlk4k14p3G84xtbMP1bIeo4yLkCfxPJP9kUU-NWMLT0Z1_xu8Gr1TRMI_NnKPVE4iBpMcQdRiqqwpA9NooXg-D-13bVMyCZ1SQwde1uSuptIc4IJSrc8DRt8usRpAp0XpmDmbEyHfDy9ly06anK1-Hv2rRw545fjYmodYjtAPEC6MYfb3Yg5SkqiC1TxYjem1pYO3Jzuy1EJPFlpWdkuemtW4orZZ-MjZqEDLmdnhboxAWFYDDCZjrP6rtXCZI4FWvkECrgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آرسنال بعد از ۲۲ سال قهرمان لیگ برتر انگلیس شد
بیشتر بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3216390</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/akhbarefori/653135" target="_blank">📅 00:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653134">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccca31dbb4.mp4?token=vlRy4XOPOuZAtsGU3Kvdja12gz1l7-HOBMnNmN_nnZ9lfy1UEyaoXQ8hDmTQ4ek-IvCqMWQPrmsbLA3uw7a1KE2doMnZeNjkiGh8D1PWUp6lAPtXVt21wY52so3yRv1gGf3zKxU0pwfB8Crz242LJmzFSvhgoYzQ9X740TZeSVd1GCMItglA-dV-2emj14zYugycbI3JXmTQdcvtxYZgSGuWvcUna6qOzFby8Rx7CfzD0jjFdfQyBoSXLu8_-HEfz7u-WyyJelljTf7cX4r8izWwxQV8PsNpgEkJ1OKAN7Wn3BdXuCRu1GJelSSygn6Fbd0NpcrIE2cCtlhs7UjToA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccca31dbb4.mp4?token=vlRy4XOPOuZAtsGU3Kvdja12gz1l7-HOBMnNmN_nnZ9lfy1UEyaoXQ8hDmTQ4ek-IvCqMWQPrmsbLA3uw7a1KE2doMnZeNjkiGh8D1PWUp6lAPtXVt21wY52so3yRv1gGf3zKxU0pwfB8Crz242LJmzFSvhgoYzQ9X740TZeSVd1GCMItglA-dV-2emj14zYugycbI3JXmTQdcvtxYZgSGuWvcUna6qOzFby8Rx7CfzD0jjFdfQyBoSXLu8_-HEfz7u-WyyJelljTf7cX4r8izWwxQV8PsNpgEkJ1OKAN7Wn3BdXuCRu1GJelSSygn6Fbd0NpcrIE2cCtlhs7UjToA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تسویه‌حساب پادشاه جوان ایرانی با امپراتوری عثمانی !
برای ادامه ویدئو
👇
https://youtu.be/rCuQWD1D_es?si=Cxi0mh-CjPIi0Nmk
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/akhbarefori/653134" target="_blank">📅 00:08 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653133">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
از کنار داغ‌ترین خبرها و گزارش‌های امروز ساده عبور نکنید
🔹
گزارش لحظه به لحظه از تحولات روابط ایران و آمریکا | شبکه ۱۲ اسرائیل: ترامپ تصمیم گرفته حمله کند!
👇
khabarfoori.com/fa/tiny/news-3216088
🔹
حقه کثیف ترامپ در اعلام تعلیق حمله به ایران | این عدد همه چیز را لو می دهد!
👇
khabarfoori.com/fa/tiny/news-3216090
🔹
نقشه پنهان اعراب برای ایران | پیشنهاد محرمانه عرب‌ها به چین | یک اتفاق غیرمنتظره در دو سه روز آتی!
👇
khabarfoori.com/fa/tiny/news-3216309
🔹
خبر محرمانه یک اسرائیلی برای حمله به تاسیسات هسته ای ایران | جنجال لو رفتن یک نقشه شوم | ماجرای حمله به اصفهان برای استخراج اورانیوم چیست؟
👇
khabarfoori.com/fa/tiny/news-3216091
🔹
جنجال رقص منشوری در خاکسپاری | هیاهوی دختر خواننده مشهور در مراسم عزاداری + فیلم
👇
khabarfoori.com/fa/tiny/news-3216016
🔻
ویدئوهای جذاب را در آپارات خبرفوری ببینید
http://aparat.com/Akhbar.Fori</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/akhbarefori/653133" target="_blank">📅 23:57 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653132">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bfcf97015.mp4?token=rfiGRb7rG63uXFT1QjFr6rZ72OFoHNuQzLM7g81rnX1AwNb7ulL1qRizg-Pp7qdFn2tooGmmW3v8ZvVZUKngRMz2iFmvR68QiVw3dzfPfdfBtWnYfoRktcCOdApJoyy3IxOGQ-kHnKIlhyg3WXXKW1X4AAzRRWAu_l_4MNSSv56FCcW4i6dVS2cSk9W2KQkCLyAiBuCMawvaV7WKC4XwQ55HgDbnSfM7azpX5O5S_tAJFYeC3aKzPb0jz31C9lWUqtCIdRPDc3ZbdwHwpBrcs6utRGMngRqTH7YCdGgBNinZKor-pEaevRuHuKqZs0OdI_r1TOEQJNCvX1Scc2Kmcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bfcf97015.mp4?token=rfiGRb7rG63uXFT1QjFr6rZ72OFoHNuQzLM7g81rnX1AwNb7ulL1qRizg-Pp7qdFn2tooGmmW3v8ZvVZUKngRMz2iFmvR68QiVw3dzfPfdfBtWnYfoRktcCOdApJoyy3IxOGQ-kHnKIlhyg3WXXKW1X4AAzRRWAu_l_4MNSSv56FCcW4i6dVS2cSk9W2KQkCLyAiBuCMawvaV7WKC4XwQ55HgDbnSfM7azpX5O5S_tAJFYeC3aKzPb0jz31C9lWUqtCIdRPDc3ZbdwHwpBrcs6utRGMngRqTH7YCdGgBNinZKor-pEaevRuHuKqZs0OdI_r1TOEQJNCvX1Scc2Kmcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خضریان، عضو کمیسیون امنیت ملی مجلس: وزیر امور خارجه ترکیه حد و حدود خود را بشناسد و بداند اجازه ندارد درباره جمهوری اسلامی ایران از کلمه باید استفاده کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/akhbarefori/653132" target="_blank">📅 23:49 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653131">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
وزیر راه و شهرسازی از ارائه پیشنهاد تعیین سقف افزایش اجاره‌بها در هر استان و تمدید خودکار قرارداد‌ها به سران قوا خبر داد
🔹
رئیس دانشگاه تهران: ۷۰ سهمیه جذب هیأت علمی برای رشته‌های پیشران علم و فناوری مانند حوزه‌های هوش مصنوعی، کوانتوم و فوتونیک اختصاص یافت.
🔹
فرمانده انتظامی استان هرمزگان: هزار و ۸۲۰ تن برنج پاکستانی که در انبار اطراف اسکله شهید رجایی بندرعباس احتکار شده بود شناسایی شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/akhbarefori/653131" target="_blank">📅 23:44 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653130">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
معاون توسعه روستایی رئیس‌جمهور: اینترنت به وضعیت گذشته بازخواهد گشت، زیرا دستور رئیس‌جمهور است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/akhbarefori/653130" target="_blank">📅 23:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653129">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ow7M4TVahOYGxpn8nuaa0yo3FmOYQJGklYUul66hymhXh4TKko8ii9p20I5Xjxb5SYSseJjdhHqKNaWetiVAX-uDl25Qf2jJpY-38oVAPHD9Cn9_ziMqwYwQh7ENIE91UFS2si_jsH1xbH3bWDJ_WOAwfBH3YfVH7iqWFyegm1KaSBhqvC_Gp_w1ivmN8e16T03iIgF40nqF5n_uk8ixiz-wSRVMLz4a63kGqQ5FszvCS63lSzLrxDUItT4gfq8pdkxXT2S1HmLAO4VJoYkO1AzeSc-69m1wQ_kHvoKieiQhLpsJzegPjalwhDykRmUmULKtX0XJhAz-YwjWViMbwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معاون بازرسی قرارگاه خاتم الانبیا (ص): در آستانه تحول تاریخی بزرگی هستیم
🔹
سردار اسدی: با تاکید بر اینکه امروز در انتهای یک پیچ بسیار مهم تاریخی قرار داریم، گفت: آنچه از همه چیز واجب‌تر و لازم‌تر است، حفظ وحدت مسلمین است، زیرا دشمن تمام توان خود را به کار گرفته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/akhbarefori/653129" target="_blank">📅 23:40 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653128">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
انسولین در بازار کم است؟
محمد هاشمی، سخنگوی سازمان غذا و دارو در
#گفتگو
با خبرفوری:
🔹
تحریم‌های آمریکا با ایجاد محدودیت در حمل‌ونقل، تراکنش‌های بانکی و افزایش هزینه مبادلات، به‌طور غیرمستقیم بر واردات و قیمت دارو از جمله انسولین اثر گذاشته است.
🔹
افزایش قیمت انسولین‌های وارداتی بیشتر به دلیل حذف ارز ترجیحی برای اقلام دارای مشابه داخلی و نوسانات نرخ ارز است.
🔹
بخش زیادی از نیاز کشور به انسولین از طریق تولید داخلی و مطابق استانداردهای بین‌المللی تأمین می‌شود و سازمان غذا و دارو با پایش موجودی و تقویت زنجیره تأمین، تلاش می‌کند دسترسی بیماران به این دارو پایدار بماند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/akhbarefori/653128" target="_blank">📅 23:35 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653127">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/103f07f218.mp4?token=eXx7RS2PWTNC3rOE-YcC0YlGsGdg6c0yw9Sny7VXzHvT33DpvAZkOFiH-W6HS4PjNHSvk4nqJq0UJ_tUwrkm98N_f0oYxU5gexQz0T_gUesK5uKIjOeLKybOZtrVnztS8o94ZK33NYvNx5B7rhqwU4Hdp664l8e-DpfaB47ntSzCMrmE2iUCARC_-mUL4vHafXghULb-fHCKu38fX-H4uo8Vq5MoMKNpodrjPpR0BZqAXXvv50szD9cjbnUPnQaCVgS06It6rfb41dh9CjKkAcyi1ebJfIWn0RggJjTPP8uwzhTthF7So4b99uSsKZQVMd3xnpl0VNYDVBgC9fXo1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/103f07f218.mp4?token=eXx7RS2PWTNC3rOE-YcC0YlGsGdg6c0yw9Sny7VXzHvT33DpvAZkOFiH-W6HS4PjNHSvk4nqJq0UJ_tUwrkm98N_f0oYxU5gexQz0T_gUesK5uKIjOeLKybOZtrVnztS8o94ZK33NYvNx5B7rhqwU4Hdp664l8e-DpfaB47ntSzCMrmE2iUCARC_-mUL4vHafXghULb-fHCKu38fX-H4uo8Vq5MoMKNpodrjPpR0BZqAXXvv50szD9cjbnUPnQaCVgS06It6rfb41dh9CjKkAcyi1ebJfIWn0RggJjTPP8uwzhTthF7So4b99uSsKZQVMd3xnpl0VNYDVBgC9fXo1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر صمت: قیمت خودرو متناسب با افزایش قیمت ارز تغییر می‌کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/akhbarefori/653127" target="_blank">📅 23:31 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653126">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e15dd1d8c.mp4?token=DcXwuacBC2PF2XpdMlvGgtCb9DTh2tWEhvgwP3g1yPa3AnX25nofUaiXB_98YqBQFtY4Xfr49ZFKM9C0oTLNDy9WAl1MA08a-IT8qPJG9H6w_ZoQgLgX3hIaC--8qKAJL2XIZX3jRaxh-6-MI-zCUbXrbuHChsJS52j5La1pc-uheUVHI117SUNJp988-T0Q-G7cag-oUMnBtR2lHy1el1XrLyIgMy8JKWBjfiN9Qb6kx27iaFBQ-nacPMZ2fzVC0wffFQo6QwLgfF2P_8klc_YxsvB9UBWFj43rpIS5VW8xBfuWJIbRSQGjeaVRpsbSgJtLW3x5_P_mPptyP0INrTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e15dd1d8c.mp4?token=DcXwuacBC2PF2XpdMlvGgtCb9DTh2tWEhvgwP3g1yPa3AnX25nofUaiXB_98YqBQFtY4Xfr49ZFKM9C0oTLNDy9WAl1MA08a-IT8qPJG9H6w_ZoQgLgX3hIaC--8qKAJL2XIZX3jRaxh-6-MI-zCUbXrbuHChsJS52j5La1pc-uheUVHI117SUNJp988-T0Q-G7cag-oUMnBtR2lHy1el1XrLyIgMy8JKWBjfiN9Qb6kx27iaFBQ-nacPMZ2fzVC0wffFQo6QwLgfF2P_8klc_YxsvB9UBWFj43rpIS5VW8xBfuWJIbRSQGjeaVRpsbSgJtLW3x5_P_mPptyP0INrTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خضریان، عضو کمیسیون امنیت ملی مجلس: امیدوارم خبر سفر عراقچی به نیویورک برای مذاکره در خصوص تنگه هرمز دروغ باشد/ چرا ما در خصوص موضوع تنگه هرمز باید در خاک دشمن مذاکره کنیم؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/akhbarefori/653126" target="_blank">📅 23:31 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653125">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0090d76668.mp4?token=jrTA93hcUr41ypTw4gMrmzCenWXSf9d-iAVml4efxtD-pxbJu2yHuJhHZwC5oZIKpRfWF6iu0jdMWFwu0tIVw1dSStTK5QBbT5vWv6QDtPdTo5CrJPl137ebtIkj_K6Clqn_WmIwWJYq07cr5u2RXIsr816XgvAAKwDyZ-u_kb9cZMGgTyuO4OdLf8p21SnZ5VRg3m35Rcj3Mj-xaHh1joqsT8l5asZSaKxIyg0jVfaYNNHLv0VAGTSxrhMCvbNinX9yPkr15XrDL68S8C9NR9lwFgk_c-nxJ1cZHylgnwwyqGweOMJQfe4lV4RUn5j7nVnICfdKucUQkz9dn0TXBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0090d76668.mp4?token=jrTA93hcUr41ypTw4gMrmzCenWXSf9d-iAVml4efxtD-pxbJu2yHuJhHZwC5oZIKpRfWF6iu0jdMWFwu0tIVw1dSStTK5QBbT5vWv6QDtPdTo5CrJPl137ebtIkj_K6Clqn_WmIwWJYq07cr5u2RXIsr816XgvAAKwDyZ-u_kb9cZMGgTyuO4OdLf8p21SnZ5VRg3m35Rcj3Mj-xaHh1joqsT8l5asZSaKxIyg0jVfaYNNHLv0VAGTSxrhMCvbNinX9yPkr15XrDL68S8C9NR9lwFgk_c-nxJ1cZHylgnwwyqGweOMJQfe4lV4RUn5j7nVnICfdKucUQkz9dn0TXBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نماینده کنکره آمریکا فرمانده سنتکام را سوال‌پیچ کرد
🔹
ست مولتن: دریاسالار کوپر، شما در مورد ایران مدام از عبارت «به‌شدت تضعیف‌شده» استفاده می‌کنید؛ تابستان گذشته به ما گفته شد که برنامه تسلیحات هسته‌ای ایران «نابود و محو» شده است. آیا می‌توانید تفاوت میان «نابودشده» و «به شدت تضعیف‌شده» را شفاف‌سازی کنید؟
🔹
فرمانده سنتکام: جناب نماینده، هرچیزی که به برنامه هسته‌ای مربوط شود...
🔹
ست مولتن: نه، نه! من از شما نمی‌خواهم درباره برنامه هسته‌ای ایران صحبت کنید. من از شما می‌خواهم درباره زبان انگلیسی صحبت کنید! تفاوت میان «نابودشده» و «به‌شدت تضعیف‌شده» چیست؟ آیا این دو یکی هستند؟
🔹
ست مولتن: ۵ ماه پیش ترامپ در استراتژی امنیت ملی خود دقیقاً از همین عبارت «به‌شدت تضعیف‌شده» استفاده کرده بود. اگر این ادعا ۵ ماه پیش صحت داشت، پس چرا ما این جنگ را شروع کردیم؟ آیا او آن زمان به ما دروغ می‌گفت؟
🔹
فرمانده سنتکام هیچ پاسخی نداشت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/akhbarefori/653125" target="_blank">📅 23:28 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653124">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
اسرائیل همه کشتی‌های ناوگان جهانی صمود را توقیف کرد
🔹
ناوگان جهانی صمود: همه کشتی‌های شرکت‌کننده در این ناوگان که به سمت نوار غزه در حرکت بودند، از سوی نیروی دریایی رژیم صهیونیستی توقیف شده‌اند.
🔹
بنابر گزارش‌‌های عبری، نیروهای رژیم اشغالگر تاکنون ۴۱ قایق و کشتی از میان ده‌ها شناور شرکت‌کننده در این ناوگان را تصرف کرده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/akhbarefori/653124" target="_blank">📅 23:25 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653123">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38bbc55be7.mp4?token=FStT2mzY3VLJo_S3wkvzZqXXpDYrjV8dIA1wZOwcNpFtjQSJkycePmat7pid9mrb04hwpm0Kf_EG-2pxndAB3nXRO9cnn3kFyv_hZ0HdbN5qoCK2YY_y5e5MyYBiNtT9DtSs2ZLlm4meb2Dj4BmD9t_yThsTDdGMri4Z-iq_ER1FWuR6NfOOeAXjabif3pwT-FaD8cc8Mu4esnzVHCngH9pre46qVrxsOZYuxnWxrjwjRit6fAv4oS_ekkE3zpVExDNYap898ZdjU_TYDKXoBSOyCdCOw-0mP1bQKo2jO3uWpm5FA3p8UerigkRBxtl5L80R_IHcaCyaOcBQ-iRinA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38bbc55be7.mp4?token=FStT2mzY3VLJo_S3wkvzZqXXpDYrjV8dIA1wZOwcNpFtjQSJkycePmat7pid9mrb04hwpm0Kf_EG-2pxndAB3nXRO9cnn3kFyv_hZ0HdbN5qoCK2YY_y5e5MyYBiNtT9DtSs2ZLlm4meb2Dj4BmD9t_yThsTDdGMri4Z-iq_ER1FWuR6NfOOeAXjabif3pwT-FaD8cc8Mu4esnzVHCngH9pre46qVrxsOZYuxnWxrjwjRit6fAv4oS_ekkE3zpVExDNYap898ZdjU_TYDKXoBSOyCdCOw-0mP1bQKo2jO3uWpm5FA3p8UerigkRBxtl5L80R_IHcaCyaOcBQ-iRinA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خضریان، عضو کمیسیون امنیت ملی مجلس: ایران باید پاسخ نظامی به نمایش محاصره دریایی بدهد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/akhbarefori/653123" target="_blank">📅 23:16 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653113">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاقدامات هیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U5eWTaSsLdnjzdoYtWiBPj-zMAzgBNljYJ7Zg42bl5Nz6Mknj2m1gA83VCSClNQ_hvOP86hpmaLcS2lh_TwCMivQfvLd_S2uZ1mo7jILvsGKkqp_shAy7wOyMQ2UtHuMgn7S9VyqgorLhDalXCGDRmDm4EE23Wmrzze0jwzW_yQTv7cciaKGgtRH7wH9_szs8WVW8b6CJALCkSst7vktThmpWTK3tnI6sMvEBkvSRxnFzLSudwTRJ_7zqrt04LjclvY6yMgC7_lPb1j_1t8uj0POwAEuSEhJkiLVMAKYc7ks2kb04os6zFBanEy3N0dQTHAX0YyWB5xi5FGFmL2OFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/miqeUcqrekvBB8VVln0AjH28cwP5qGYL6o-EbXT1WjE27xdlZ79fK-aF6qlK7RDmpq3F4-iywpOwwX8H4rKmflRX1b4b8cvjSS6BpxveCM1B0DdPsl8O1SlH_LgDoCh_yqz5JL1z2zvAR53x75h_vZ6OXTUMt9SiIqyS1tG3LrQ9lZRxPNN4fzMrALGOMfYlQkz0NKT7wtk9C_1k7Xcr0_bjg0OQz_pmLSQvYy9Hy_-iWimhi4rxL3utKwEDUY0ylbA545a8DBU3DA7Rwv1pRUScdUAMjMwD4ihjPw7l0rIEz5_SiPLdKcQNd52UawFuukoAdn4TpJMoqOKJD8MWtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DcWgiroCgcZAU6QlpA6Akm304E5aR03evOtFIl9xb6blfnkEHScLF48IZ-OVaRnijRZjILzFW4NmzXt-9EZiEjsSuRAG0M7r4q8yJakCuMtWaeDgH85lc341KmhSL7aoy_KV21hM1OGthLe5lkeClIPsoQ1S90iQ73M3FlXlBfLVmOJ_euKOU9teZehMVgO80oyN3VuDMnNB8QsYFcQaWZFwBM1GHeJWGZKuryvbtQaqfNzNgemq02fOnS1MBcYZ-9BnQ28LnWws4Vsf0f8YFdN4MjUMcwhxKpfTxrvYRqXMXUEno7dHto_GLLTEhmWUtqxU3BVCBdtON8fhXs57oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o0xEvXG3tTkgjtqPBEcJqJjBKQdu4eXPhR3BIPtmv_TSrblAECBOK5FABE6__F5-rTFLUkgVYYubvbwnpkEJlFGXn6HZ0_t2W72PaU6WErPkkrxJxrA9lj6SjkdWsJCscecKQj0A5HZq-8Q0gOxQIE5lvSAsBbz_cWDaPTuDzyzuNZTnNYz18XX5vioGxcAXnSU2Yj85sjiU4VJUN8Yd7KNQBE1OvlACFYIzCJiQJUhyj5pTZGX4L0oxD832Oj_CW1QgAL5RtP6Jn-1gKFI69c24k--F_Ig8Dm5wcU-rI-YHPYthCgGbWY7kJ3Mm2NwNOuB182e9gjoDxKO2h7n-KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ehIhTgoJla8nQpFyNDQmsHtUgSNdgxFdXfs6ihKn1d_s370liGEiGIWmlGgQSXb4dv6uPeKNUjDXLnjmxp27icmJC4exTCbdJsBMzVN5ImiNLGJsxQSuV1zG8usl1PzJIaEMKOWsy9y9ZeAvXLVNNl4u_GJ5VJZE3_qIFLeS3rKi9rtW24Qc31gAff7jFJ5a6PAL-YF_VHHIkR792-_xmeCcND7dU4q_NLe-X1Qq_x1_s1fRmrNmR_FsWl-O3-9didrxQLK4Z64PiteURG1vKyxfH67Amu-xd8OS0XVjcpe5HenGQ260sF3eZF_qvqhaeGF1hnhm6dyw1X5KnWkvjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XTJf6qJglgwEwURbroB2fyIX7d9z5oKhb1TA7jT9Q4zUsDZRZxBr4zA7TVTtRAQpY36DM0qTqBWE0qU8QQJgLfhuLeLIOaLnjG0xzJpZbKdHtH0_rQUfgcgyxErAcRayFu5IAd_OMOrPRzairbJ03cxsukIT0jDrJyxuYOAbr-cDQ7aA3-JuN-YjyiyP2cRYP3RitEsn6Sg3Cb-EkihbEa4PKzWo3u80J73pOdYGPFO1Xt8KFwwu02nG3gG3Zun6dL3RjhRgx19yIm4emlGF7s-8UshDMsb0MA-XCeJaFfgC3-_OM1XhOXZp5mNEGN4pEiOephNNCCGBe9dVrjQasg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V6MWQeWEQOsW9pBu2MhF-VWZa3Iw1WLgswHmtPAUHRH-OwRoc3ZBpFc2DeMDRIyOZk30LCmpIoLMDJnhyMowlS3jWpeUNYsV-75Oj4bxW8NOAOBIwLnf2OnS_gCIULnVA-RlryZ_EtTq6vu7Cp1yaAtvV391qSsnXjNlDE5rDI2z41P5BgoJNKQWm9ER3Lg8L3LJ0Orm4VArHWjU1099YPoIjEzG24HnaRT3qpH3qtf7zKUCF58rl2d4urOuPuLyrGp0sU8Sa8tmFLTmFiNnY3jCmGU1JeCCA8B1JFheddS_O2KLwu54SMtfTJKKgRyFzHowP4fgp35rFFIk5bjH8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nzShiXPK83a0ZAvoEaocLzTWZfE19L8jhEqqAUtB0pdQ7rs0k2QDFNffnNtAKI7mBHMZGs6KCboO-HXVyw4pKNkvCpLhJyA3MSRUvRIWZANdOPpcMzK2B16APzvCvWFbV_Jvw4gDZrn1i7NWNoTbmjvEVmT7HdGNoBz8d45DD_Dzus3d_atUTJCHTKN1Di7b9r0vkXMCF4jxTEeuOR1GNOXhoZvjgvMJ7vbVNVxcFuxOqgWpdR47VnMVCzPDaYEVLpJtXRBcBb03c4FZcOdURVtGw5dgvM1lLarX9sRVxLqSbojDja_MSi6HCK_jrFoll8UDTTh6HixYu5zTFDWGDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pgPpzCoV0sxR0J5GBtWG0JwukIKe3dyGYdHf7z-aKIoG81gvOPXSzGe34lmff1AiYeBQiHvdhqyWBnLLOvHXiAGTzm5UmbhaD5WIGbkh5bJzpS8Nv2ZHq2dvh4tlGuCRr6YPWEImvpvobOS9_Jv7OTerMDP5FJ65IHgkswjQyf_H0proXKlXaU83TMBaKLlJJQkePBLQ-R-s37LIbRB5nGjIHPZLZbzqDVWhcEInAMfC73iOQY8ythXIWWXF4PUN_u76QR7ZQBfW9zSLoxagjtiazaCPlsAjmUHIU67tb05KJAWG9OfKvcP85sE-n6BYbyr5-zDph3ZUSs4ky_zX9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XWMewIL-z0lbs9dgsPkvvGIiR36Nn7s-Ww8j4sFnB-XI3EzmEwz8v4tYt_j6w2hGi91_U_M2CAgoY5BudyhU8E7Wow4ElWGSEEu9FcFC31-wRBQNtamexShCcVbwWhgg-qiiLxL-H_hS1WLu_55iKm86Lnr39pM1VGJyPUCqzTQHvry5WlPoVo8PV78o4zuJZh-6cYxUDIcUMzPXAQsOOJhISr_AhDNtzmpCz2CTLkVCqjDityAIDwC1txxG_f2k9Nxhk6RVTUjUKiBchU9A1UNUe-AKWGt-6HJBj5mFF1IEq65ej6js4_Ln0czGZDIymMIWzQGaSv4m-q7ocSwTaA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💫
روایت برکتِ همدلی
💫
هر روز، به پشتوانه
#همدلی
و همراهی شما مردم عزیز،
#هیات_قرار
با ذبح ۳ رأس گوسفند و توزیع گوشت قربانی میان خانواده‌های حائز صلاحیت، گامی در مسیر حمایت از خانواده‌های ایرانی برمی‌دارد.
ادامه این مسیر خیر، حاصل اعتماد و حضور ارزشمند شماست
🤍
💳
گزارش اقدامات هیئت قرار را در کانال زیر ببینید
👇
@Heyate_gharar
شما نیز میتوانید در این کار خیر سهیم باشید
👇
5029087002135690</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/akhbarefori/653113" target="_blank">📅 23:15 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653112">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41f0e41066.mp4?token=FPmEWsJTUEE7IhpenJXX78u-d-WGzqy6mY9UeySB964KoMLK8rmAo23FifUXdGGu2pvdwfLpuPYv6e5HDBmbau2ovX5u4iWG1mqsWvHYNd2qdhRlllzRI1-pLjrr2PsafTwfUbdd0roeCT6ef23466Xg0AbE1NvsZv_Iog0so8E9P97-RAkq6d6pXfoTDILWXPC-tei-0JKTtP5TOe7wxCwtRV-vP6s03dNTycuVVBFzW6desXUXc96ChfjbBpmgMkYqtlTEhAVJokjxbrn9RLOEU5kNH4OQV9nuKPiWBp4QHp-g2VI-63h716QzBA1pk5YY-VdItPT-kQqCGusGLHFT_dvnWkHyqntPvnUhNRUp3jEvsY1yGFpl4RBJ7bIlWSmgLNvXWyJnXiMEBS95-Tih-Wb1DygOIO__n5pFbzZya6-xcRCQU__Au6SjnBlcTvZ4P-2KyPXxy4vw2gQz0G9jyE6Ld5nz-000iXEy4ziZob4cVxObQseY736KYBEfMZPfOJfBMfX9BPRUP1QJ59fVp5Of3M5CYxNmAq0rziaj9nVPM6iPJB87cSgbPRTOQX7ccKR1ApsczWI3R9NOq9-omb-dGMsxBlLFpDkg7Yqg0qV4xpR0Mx1Ta4s2v-peBPrpxm249RpJiACY5xKe4kuGJwmdnCiddkZo-9s4IpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41f0e41066.mp4?token=FPmEWsJTUEE7IhpenJXX78u-d-WGzqy6mY9UeySB964KoMLK8rmAo23FifUXdGGu2pvdwfLpuPYv6e5HDBmbau2ovX5u4iWG1mqsWvHYNd2qdhRlllzRI1-pLjrr2PsafTwfUbdd0roeCT6ef23466Xg0AbE1NvsZv_Iog0so8E9P97-RAkq6d6pXfoTDILWXPC-tei-0JKTtP5TOe7wxCwtRV-vP6s03dNTycuVVBFzW6desXUXc96ChfjbBpmgMkYqtlTEhAVJokjxbrn9RLOEU5kNH4OQV9nuKPiWBp4QHp-g2VI-63h716QzBA1pk5YY-VdItPT-kQqCGusGLHFT_dvnWkHyqntPvnUhNRUp3jEvsY1yGFpl4RBJ7bIlWSmgLNvXWyJnXiMEBS95-Tih-Wb1DygOIO__n5pFbzZya6-xcRCQU__Au6SjnBlcTvZ4P-2KyPXxy4vw2gQz0G9jyE6Ld5nz-000iXEy4ziZob4cVxObQseY736KYBEfMZPfOJfBMfX9BPRUP1QJ59fVp5Of3M5CYxNmAq0rziaj9nVPM6iPJB87cSgbPRTOQX7ccKR1ApsczWI3R9NOq9-omb-dGMsxBlLFpDkg7Yqg0qV4xpR0Mx1Ta4s2v-peBPrpxm249RpJiACY5xKe4kuGJwmdnCiddkZo-9s4IpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حزب‌الله پرچم رژیم صهیونیستی را به زیر کشید
🔹
حزب‌الله ویدیویی از پایین کشیدن پرچم رژیم صهیونیستی از مقر ارتش در شهرکی واقع در جنوب لبنان منتشر کرد.
🔹
حزب‌الله در این ویدیو که متعلق به دو روز پیش یعنی یکشنبه گذشته است، ابتدا تصاویری از حملات متعدد خود به مقر تیپ ۲۲۶ ارتش رژیم صهیونیستی در شهرک البیاضه را به نمایش گذاشت.
🔹
بر اساس این ویدیو، پس از حملات متعدد حزب‌الله که غالبا با کوادکوپترهای انفجاری انجام می‌شود، نظامیان صهیونیست ناگزیر به ترک و تخلیه مقر خود در البیاضه شدند اما پرچم این رژیم را در این مقر باقی گذشته بودند.
🔹
در انتهای این ویدیو، کوادکوپتر انفجاری مقاومت با اصابت به میله، موجب پایین افتادن پرچم رژیم صهیونیستی می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/akhbarefori/653112" target="_blank">📅 23:05 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653111">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
بحران پشت مشهد و تهران؛ آب شرب مسئله شد
عیسی بزرگ‌زاده، سخنگوی صنعت آب در
#گفتگو
با خبرفوری:
🔹
با وجود بهبود وضعیت بارندگی نسبت به سال گذشته، هنوز یک‌سوم کشور با کم‌ بارشی و تنش در تأمین آب شرب مواجه است. استان‌های تهران و البرز و به‌ویژه شهر مشهد در صدر مناطق دارای تنش آبی قرار دارند.
🔹
در حالی که میانگین پرشدگی سدهای کشور حدود ۶۶ درصد است، این رقم برای سدهای تهران تنها حدود ۲۳ درصد و برای سد دوستی حدود ۵ درصد است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/akhbarefori/653111" target="_blank">📅 23:01 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653110">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RW-YwWO5txR7TtTC71IHdreS1-9z7hHucfgWswJ4SP1ILzwr7cf1xvZGaO43DQ3U_Ar7wGS7ennFrA-bZ4ttyQDfjx6rEhpD6JveUQ-8cTeMJnhSbPSeC7Vq-kausp14P8a09mVqh7RzEjbmoGgbXH0tLsD3kNXVdzYm2YC2DZlfj7QVLnBDSQ-fV5bvk7iObV_16rffQ8yWxs_VknU0xXiNUiPE2gJv1m5XWNjKCdSh_JoDG-RjAj_yi5n7_lhS5g52XVLjUdAGJa-KKQ24sgzgZ3qlHzKltV23QV5eipBTKg3ebonGxIiDAQ_kcR6ooY7BMQ1qF8vwLDrWiF_f8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اولیانوف منطق گراهام را زیر سوال برد
🔹
نماینده روسیه در سازمان‌های بین‌المللی مستقر در وین اتریش امروز به اظهارات سناتور جنگ‌طلب آمریکایی و حامی ترامپ لیندسی گراهام درباره ایران واکنش نشان داد.
🔹
گراهام در پاسخ به این سوال که درخواست شما حمله به زیرساخت‌های انرژی ایران است، گفته بود: بله خواستار آسیب زدن به این رژیم هستم. شاید اگر به اندازه کافی به آن‌ها آسیب بزنید، حاضر به توافق شوند.
🔹
میخائیل اولیانوف در واکنش به این اظهارات گفت «این آقا ذهنیت و طرز فکر بسیار خاصی دارد، اگر بخواهیم مودبانه بگوییم».
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/akhbarefori/653110" target="_blank">📅 22:42 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653109">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
نیویورک‌تایمز: در صورت ازسرگیری جنگ، ایرانی‌ها تاکتیک‌های جدیدی به‌کار می‌گیرند
🔹
«ایرانی‌ها خود را برای ازسرگیری احتمالی حملات آماده کرده‌اند و سیگنال‌هایی فرستاده‌اند دال بر اینکه در صورت حملهٔ دوبارهٔ آمریکا، درگرفتن انتقام و تحمیل هزینه‌ای سنگین بر منافع آمریکا در همسایگی‌شان و اقتصاد جهانی تردیدی به خود راه نخواهند داد.
🔹
در هرگونه دور جدید از درگیری‌ها، ایران ممکن است روزانه ده‌ها یا صدها موشک شلیک کند تا «به‌طور مؤثر با دشمن مقابله کند و محاسبات طرف مقابل را تغییر دهد.»
🔹
کشورهای عرب حوزهٔ خلیج فارس باید خود را برای حملات شدیدتر به زیرساخت‌های انرژی‌شان آماده کنند.
🔹
هدف‌قراردادن میادین نفتی، پالایشگاه‌ها و بنادر کشورهای خلیج فارس، یکی از کارآمدترین راه‌های ایران برای آسیب رساندن به اقتصاد جهانی و اعمال فشار بر ترامپ است.
🔹
اگر آمریکا به زیرساخت‌های اقتصادی ایران حمله کند، ایران با بستن تردد در باب‌المندب به آن پاسخ خواهد داد. یک‌دهم تجارت جهانی از تنگهٔ باب‌المندب می‌گذرد.»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/akhbarefori/653109" target="_blank">📅 22:33 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653108">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/akhbarefori/653108" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
مراسم دعای ندبه - جلسه پنجاه‌ویکم
رائفی‌پور:
🔹
0:03:30 مرگ جاهلیت به چه معناست؟
🔹
0:07:40 دعای پیامبر در مورد محبین حضرت علی (ع)
🔹
0:21:30 بازخواست چند برابری علما در آخرت نسبت به سایرین
🔹
0:34:00 مرگ مقدمه بیداری از خواب غفلت دنیا
🔹
0:41:10 حجت تمام کردن امام زمان برای تک به تک مسلمانان
🔹
0:51:20 عدم وجود عصبانیت در مؤمن واقعی
🔹
1:01:40 تفاوت هدایت عمومی و هدایت باطنی
#دعای_ندبه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/akhbarefori/653108" target="_blank">📅 22:29 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653107">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf3870ff30.mp4?token=VYuqzzOyFX1ZU0emicbMjCTt7tO-Z9Y2sIiCjw5l0ZKywpd59uptF3L5bDgLMOFlnDdkACy4fyS3NVJcnSWcxfVy8BGU0DPjnrF4bkvyYgRk9P2RK0-QN5c6bVE3Sm4cvJOadfEqYBQreWymbV7eRGsXGZ8zJvx4WhQYdXGUhwI40IRaibDVlLA-VVGfnz6Uh01qOzBVnp2AxW5qZCAskI6neHsCNbowwfiLMM1B79ArsXyGeh7JlKVFlBVCUBudWQB7fg7ghXtElQcXXeK0jfqhJTH_ryfITvQdMoi8RFHJv1rBKrTZ1PmXEzDGvI3fflMNNZaBexcWT_uFVFodwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf3870ff30.mp4?token=VYuqzzOyFX1ZU0emicbMjCTt7tO-Z9Y2sIiCjw5l0ZKywpd59uptF3L5bDgLMOFlnDdkACy4fyS3NVJcnSWcxfVy8BGU0DPjnrF4bkvyYgRk9P2RK0-QN5c6bVE3Sm4cvJOadfEqYBQreWymbV7eRGsXGZ8zJvx4WhQYdXGUhwI40IRaibDVlLA-VVGfnz6Uh01qOzBVnp2AxW5qZCAskI6neHsCNbowwfiLMM1B79ArsXyGeh7JlKVFlBVCUBudWQB7fg7ghXtElQcXXeK0jfqhJTH_ryfITvQdMoi8RFHJv1rBKrTZ1PmXEzDGvI3fflMNNZaBexcWT_uFVFodwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بدهی بیمه‌ها به داروخانه‌ها کی پرداخت می‌شود؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/akhbarefori/653107" target="_blank">📅 22:21 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653106">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6579b980bf.mp4?token=CEEVGEyPuIEUqwDXZ0klXjulFWJ3qlJ8zBKFIVcM0hbAIde6SANCfc5TBWPiKUfHmE8Ye3AKZXOpWW-tEUbxNKI9eTTPE5tS2ORRhPLhEnFQ-yvFrJZxL4waCYm8ntZzz4VrfEYWM2pEY28IDyGKikJgmj8n-iZKYayUWn7xArZIHdntkZW2GjHIEh1rAdeXHigEGmEXBA41_Nai9vNliHWtZOHOa-NgaQQM3pGVe8M5QnQz2BRQo1OYYzbtgCBjzxQCOwUPg7zMLK0y5sxUI_fR5dxMbLAj8md9446lZzJ2y1lS25s8GoiCPF23lDskhWwbnrznSzEbCBezZ7NdPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6579b980bf.mp4?token=CEEVGEyPuIEUqwDXZ0klXjulFWJ3qlJ8zBKFIVcM0hbAIde6SANCfc5TBWPiKUfHmE8Ye3AKZXOpWW-tEUbxNKI9eTTPE5tS2ORRhPLhEnFQ-yvFrJZxL4waCYm8ntZzz4VrfEYWM2pEY28IDyGKikJgmj8n-iZKYayUWn7xArZIHdntkZW2GjHIEh1rAdeXHigEGmEXBA41_Nai9vNliHWtZOHOa-NgaQQM3pGVe8M5QnQz2BRQo1OYYzbtgCBjzxQCOwUPg7zMLK0y5sxUI_fR5dxMbLAj8md9446lZzJ2y1lS25s8GoiCPF23lDskhWwbnrznSzEbCBezZ7NdPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک سیگنال مهم اقتصادی برای تصمیمات ترامپ درباره ایران
@Tv_Fori</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/akhbarefori/653106" target="_blank">📅 22:15 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653105">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b6c4c745d.mp4?token=gNj0teAt0dn--R9rDAfgbz6Z1Lee_HbgG15IBkBX3oKtsa4o0uo8jKVXuGRlpDLpvXhauVmToPVaDcFINMSqVPqTnwOTugZHsmZuDnXNarndsz3amyz0-89qVdEUofozJTd822TXL7cC-_uaPtjryyeiK2t7janjJrKZu4XHLjlXhXCW7YoMpyi-NMudmLWHHFEN97fBNfekzKquWpaqJCqI1GCSdZgsQU1KA8fetjh58u2h41PxiEy5w1ZMJb5qZGlrXHoqDWMcEAwm0LWSCj1iQs_yivwBy6R02-yKTwLXqT559kBWUTve1N01rXnIhD74CNP5NwTRuz1irHctbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b6c4c745d.mp4?token=gNj0teAt0dn--R9rDAfgbz6Z1Lee_HbgG15IBkBX3oKtsa4o0uo8jKVXuGRlpDLpvXhauVmToPVaDcFINMSqVPqTnwOTugZHsmZuDnXNarndsz3amyz0-89qVdEUofozJTd822TXL7cC-_uaPtjryyeiK2t7janjJrKZu4XHLjlXhXCW7YoMpyi-NMudmLWHHFEN97fBNfekzKquWpaqJCqI1GCSdZgsQU1KA8fetjh58u2h41PxiEy5w1ZMJb5qZGlrXHoqDWMcEAwm0LWSCj1iQs_yivwBy6R02-yKTwLXqT559kBWUTve1N01rXnIhD74CNP5NwTRuz1irHctbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توجیه بی‌شرمانه جنایات آمریکا و اسرائیل توسط ونس : طبيعیه که غیرنظامیان در حملات نظامی آسیب ببیند
🔹
معاون اول ترامپ: هر زمان که حملات پهپادی یا موشکی به کسی، به ویژه جمعیت غیرنظامی، آسیب می‌رساند، این چیزی نیست که ما اصلاً دوست داشته باشیم ببینیم و این یکی از چیزهایی است که گاهی اوقات اتفاق می‌افتد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/akhbarefori/653105" target="_blank">📅 22:05 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653104">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GEzpbcUfOdXgthYhXLvR0GiEN42QL67LTCp4gIAlYVlAFc4sbCoVoWm9IVtnH6HWyZ9jhGT4Zr2C8rTJwa0ipCD57feFzHgQ3rBMK4HiogDQzxuqWu0xKXilQfgTaX59sHzsg6w6_8s1uCk1bGL8oH7cIvU9FxAzjVZQF2QEdqDf-aY7g6GSSkiw9gspnEnDEABXvFrMRE1hwT6o2DokYwmgaldfZM9cadtJi0tsCZdXFAChEnP3s_Ng46Ks2OisHNi6Dtj3AGdhZM4eNA-EDDw9IW7jQVoX3NL3y0y7j8s8Q4IjWnY6gcciPKfbLcyZ2jn5rE8-lO14rfoZg2mzOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیروزی غافلگیرکننده ایران در «جنگ وایب»
مجله فارن پالسی:
🔹
ایران در جنگ جستجوی اینترنتی (جنگ وایب) برنده شده است. ایران اکنون با تولید انبوه ویدیوهای رپ لگویی، پست‌های طنز سفارت‌ها و محتوای خلاقانه هوش مصنوعی، روایت جنگ را به نفع خود تغییر داده و به شخصیت اصلی فضای مجازی تبدیل شده است.
🔹
در مقابل، کمپین‌های دولت ترامپ با میم‌های تهاجمی و محتوای AI بی‌اثر بوده‌اند./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/akhbarefori/653104" target="_blank">📅 21:53 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653103">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0c29eff5b.mp4?token=uSAzFRFgNXj-az-c50Geawp3py002-mdSHSs-aJlgRcAW8xvoUe62Y6pEQHVbHbClf56f17dU6FoNO7WrJ2VpI45wNXOAeMBw-sp359sAgVOa-DPakl0z1e9rU0jfB4b56vJ_yzixfnuZsNf1s8EkBGLm_a6yjep-yf5ayfzY-MxrgE2wBe8qZAe5uq4N7ReM6YLJmPuio4vWHFXg1ia5yplRdlNY0OS3AR4VDHXZSuXXd3aLYkBFgsUZPboXYZMdDVbRXDusBemZxyFLRp8EgVA7vP6TJ_qwpvFJg_rRnVU86qhVxNOoRszEruvjokZaq4VJG8JBDY4DvYJXnxz6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0c29eff5b.mp4?token=uSAzFRFgNXj-az-c50Geawp3py002-mdSHSs-aJlgRcAW8xvoUe62Y6pEQHVbHbClf56f17dU6FoNO7WrJ2VpI45wNXOAeMBw-sp359sAgVOa-DPakl0z1e9rU0jfB4b56vJ_yzixfnuZsNf1s8EkBGLm_a6yjep-yf5ayfzY-MxrgE2wBe8qZAe5uq4N7ReM6YLJmPuio4vWHFXg1ia5yplRdlNY0OS3AR4VDHXZSuXXd3aLYkBFgsUZPboXYZMdDVbRXDusBemZxyFLRp8EgVA7vP6TJ_qwpvFJg_rRnVU86qhVxNOoRszEruvjokZaq4VJG8JBDY4DvYJXnxz6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
میزان حمایت از جنگ ایران در غرب چقدر است؟
🔹
نتایج مهم‌ترین مراکز افکارسنجی دنیا داده‌هایی را به شما نشان می‌‌دهد که حیرت‌زده خواهید شد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/akhbarefori/653103" target="_blank">📅 21:39 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653102">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
رئیس سازمان بهینه سازی انرژی در مورد شایعه گران کردن بزنین: دولت فعلا قصد گران کردن بزنین را ندارد
🔹
سقاب اصفهانی: برخی تاسیسات ما آسیب دیده و نیاز به صرفه جویی داریم.
🔹
درصورت اینکه با کمبود مواجه نشویم گرانی بنزین در دستور کار نیست
🔹
اما اگر این موضوع رفع نشود ممکن است به نرخ سوم بنزین فکر کنیم تا بتوانیم بخشی از یارانه دولت را به بخش‌های ضروری مثل دارو اختصاص دهیم.
🔹
من هم می‌‌توانم مثل خیلی از مسئولین بگویم مشکلی وجود ندارد اما اینگونه نیست و ماهم دچار کمبود‌هایی شده‌ایم.
🔹
پ.ن: نرخ سوم بنزین ربطی به نرخ‌های ۱۵۰۰ تومانی و ۳۰۰۰ تومانی نداشته و معاون رئیس جمهور از طرح موضوع نرخ سوم این است که مصرف بیش از سهیمه با نرخ سوم محاسبه می‌شود که این موضوع نیز در صورت صرفه جویی مردم ممکن است در دستور کار دولت قرار نگیرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/akhbarefori/653102" target="_blank">📅 21:32 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653101">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
توزیع مرغ منجمد با قیمت کیلویی ۲۶۰ هزار تومان آغاز شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/akhbarefori/653101" target="_blank">📅 21:30 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653100">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oOt4kySUnBM1WkWE0F7dJjJdkxEvCUgzH2fyZ9WNnWl52dqPb44nEdLuCuPx1xKFuGM_sr5szJ5c-C1fLaMR_3EuyG3FIeuz4TEmPJOTtyo3Bi1KcyPgN1QNS-Veoy_6W91KJiPdcAHth-LEt0BdXUq2JWdVEj2DVFuEp7x5cFhao8pmluubbj3fBjvlcQDxyghNR80KlzAEjLIbQrfBAejgzgmDtzZgKSvNoRmKMIcvBL2AwZ91Syn9DeSya-sAlNktR0p2DWQ2Dl-A4l7_UReNxLdxFgpZ8x2qONGDoAjW-K3uuq9XSY5jVnwNlpEKbT60SR0mXCQB0UN6efoCKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فارن پالیسی: ایران می‌تواند بزرگ‌ترین شکست ترامپ باشد
🔹
ترامپ امیدوار بود که بتواند رئیس‌جمهور چین را متقاعد کند تا میانجی‌گری یک توافق صلح بین واشینگتن و تهران را بر عهده بگیرد. اما این اتفاق نیز مثل خیلی از اتفاقات دیگر برای ترامپ رخ نداد.
🔹
ایران هنوز ۷۰ درصد از ذخایر موشکی پیش از جنگ و دسترسی عملیاتی به بیش از ۹۰ درصد از سایت‌های موشکی خود در امتداد تنگه هرمز را دارد. اینها یعنی ایران می‌تواند تا هر زمان که بخواهد به اخلال در حیاتی‌ترین گلوگاه انرژی جهان ادامه دهد.
🔹
یک بحران غذا در جهان و کمبود نیمه‌هادی‌ها که به هلیوم متکی هستند، از هم‌اکنون در پیش‌بینی‌های اقتصاددانان برای سال آینده گنجانده شده است. هرچه این بحران بیشتر طول بکشد، هزینه‌ها بالاتر خواهد رفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/akhbarefori/653100" target="_blank">📅 21:30 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653099">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M90bn2kVQ2ya0AIj2JpbHhUcRQzq7Vxx4V7KR3PFbH4aAJcoHiTw36-Zrd1lPPmhCr5Oc8d3Wr7jLXWxzFvvXrE_hOh_H3Bt0xBqrmvXi4kMoUnzAaD35IlCWEGYt0joGocmTOeI-BPbZ54ts3_SCBFTDm9hsN-6fSqlYnJSyoMbZcElkRwt5NW1xCfrLBh0LLiRWqB2e6hXxXgjzWkSFY9Niqv-IwAYnuOlVXt5HSOfwlvJT4qeayLTKxjRD6iT6TDXkerFJm01f5TWvacomKXSIyRAPwceO6HNi2nrOeTEqsLOuBaw2eq_sCZAHr8EcTnhIbTybI753P5r68a_wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بوس به بورس
🔹
برخلاف القای رسانه های معاند و کانالهای فارسی زبان برای ایجاد صف فروش بورس تهران امروز عملکردی امیدوار کننده داشت. شاخص کل با رشد ۲,۵۰۰ واحدی به سطح ۳ میلیون و ۷۱۶ هزار واحد رسید. شاخص هم وزن نیز بیش از ۲,۶۰۰ واحد افزایش یافت. جریان سازی های منفی نتوانست روند صعودی بازار را متوقف کند و بورس خلاف جهت نمایی ها ظاهر شد.
🔹
هفتصدوپنجاه‌وچهارمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/akhbarefori/653099" target="_blank">📅 21:27 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653098">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e6ae8ec25.mp4?token=Afno2qNTswTx_IminBbuo099GF5d1V_QhsrRS4F1XuVEjvaXLkriB8O6kUrJTVPbo09EbsWyhkYIddrrkQXJLT2h6FRZPqeLjVqWZOGtrUrES5x7P76H6T6BJk8eI82IQmVQOj35eD6bDO_C2L5K8CXCnd4KdSfzTztHiUNxEeMUS2aLw13ooea2cFT2a4zkQ2AcBwR96RsfJyN5yjGU8zMkMJW88hSIz-0il-d4HX8zgb6dwmrWB2o2zDQSpKw4b5-0wxvJbMqTFcCIPBCkR8Q328XLdI3IMbOw70kMqWTVJNsNVHRpzvu9HlzV8QunfRgqWFdFrOTqkDx1vZtNZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e6ae8ec25.mp4?token=Afno2qNTswTx_IminBbuo099GF5d1V_QhsrRS4F1XuVEjvaXLkriB8O6kUrJTVPbo09EbsWyhkYIddrrkQXJLT2h6FRZPqeLjVqWZOGtrUrES5x7P76H6T6BJk8eI82IQmVQOj35eD6bDO_C2L5K8CXCnd4KdSfzTztHiUNxEeMUS2aLw13ooea2cFT2a4zkQ2AcBwR96RsfJyN5yjGU8zMkMJW88hSIz-0il-d4HX8zgb6dwmrWB2o2zDQSpKw4b5-0wxvJbMqTFcCIPBCkR8Q328XLdI3IMbOw70kMqWTVJNsNVHRpzvu9HlzV8QunfRgqWFdFrOTqkDx1vZtNZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وضعیت بازار مرغ در میادین تهران
🔹
توزیع مرغ منجمد با قیمت کیلویی ۲۶۰ هزار تومان آغاز شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/akhbarefori/653098" target="_blank">📅 21:20 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653097">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
ونس، معاون ترامپ: اگر ایران به سلاح هسته‌ای دست یابد، بسیاری از کشورهای دیگر نیز خواهان داشتن سلاح هسته‌ای خود خواهند شد
🔹
ایران اولین دومینو در یک مسابقه تسلیحاتی هسته‌ای جدید خواهد بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/akhbarefori/653097" target="_blank">📅 21:18 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653096">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
صورت‌ حساب ۵۸ میلیارد دلاری بازسازی در خلیج فارس!
🔹
مؤسسه «ریستاد انرژی» برآورد کرد که هزینه تعمیر و احیای زیرساخت‌های مرتبط با انرژی که در جریان جنگ خاورمیانه آسیب دیده‌اند، ممکن است به ۵۸ میلیارد دلار برسد.
🔹
رقمی که سهم تأسیسات نفت و گاز از آن می‌تواند تا ۵۰ میلیارد دلار باشد. این رقم به‌ طور متوسط حدود ۵ میلیارد دلار خسارت در بخش‌های صنعتی، نیروگاهی و تأسیسات آب‌شیرین‌کن را نیز در بر می‌گیرد./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/akhbarefori/653096" target="_blank">📅 21:16 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653095">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aEJzdvnQSvIIJltnOH05QSsnHirFtVswb_Z00c0N5q7RDTZFomQLAjJ7BV2GbRFBnrscLxck5pHfDYqRuReSTMuh1SxSox6m-4QkAI60J_e8ZLZwEus-mldHzyHDxNRJ6jC7Tvzji5oFeOL7EZH44IlD7owd_r6B3kHyHk4gtDoztbXW4HEIeD-dg7OkVuNFOtWDQ9bUNca4UabhsFb-LRtvALQHmY6SlpnKOL0E0KYz4CaAEsZOiU-4RWr-UG_CPvoNYVJy0brY1QALqm8mHcVEgDVkYmxUQ0qYywVYF5YD8HQFqPTRIptMRW7hzXDptih6Oh4Q0F_ErV-_SfTEMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تعداد متولدین هر سال در ۱۲ سال اخیر
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/akhbarefori/653095" target="_blank">📅 21:11 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653094">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ojZ9MslwyyE-s7cqImmtsGVTpZtxCehn0IvJ1yfAr7rTJY5giFElTowySRz1xkLaeg0zl6xvNiyzx93Ld7ZAoE-BE3FzAMkR_M2DufonHPXDt0EEzBGMMaAS1S82ru8Fbs3_a-WkBjHgOz64L2QGH0Tef7ZDEW9UUCOT2EWLoKW-_AJEkk55nT9X8U7W91aml3d5xPyrqJVCERrFC4eh3sTSGGrbddvKN3T7A0zUhXxwgkST9YrFtHBo67qhXv5cnO5yEUqVeyxS7QT2m46LpyWbclV6VKNhqaOSnaV_TQjVERQMWSCiCLHDCuE9n8jiv9MhAIx7QgG6HEqm6YVV-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مقامات اسرائیلی: حمله به ایران فقط مسئله زمان است
🔹
شبکه ۱۲ اسرائیل روز سه‌شنبه گزارش داد که مقامات اسرائیلی ارزیابی می‌کنند که حمله به ایران بیشتر مسئله زمان است تا احتمال آن و حمله به ایران را قطعی می‌دانند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/akhbarefori/653094" target="_blank">📅 21:09 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653093">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3b3e60533.mp4?token=joqukIKQuDCihzlbcxEHtr_tVuXqPUChPRz5MWDakezcpRCRpI14DL8v7jIFZkWchAgXdulT9jBZvP-g9GXl__sLts3wcgd-BMyp0OeyknyScOgxoIdbYFvwExXHAc2SYLQp4tUecCJLbJieBodWLlLgIeYtHRm21x5K9v8G6Uc3rYRNVJgnwA1aCZvwxHrTDkS1S_zE2duQ0uwQYpdNtkX10Dm1hMVAg-z1o4tGrvZ_LuX98Oq5RKf_rWSyD8OpE57OSTTwXFoUfvIsk1R98zsVHM7k71M3WHvILkBRe4vDrcFEampr1z8k-maohK6A4sByPJwRq8zbIys91Cjmu4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3b3e60533.mp4?token=joqukIKQuDCihzlbcxEHtr_tVuXqPUChPRz5MWDakezcpRCRpI14DL8v7jIFZkWchAgXdulT9jBZvP-g9GXl__sLts3wcgd-BMyp0OeyknyScOgxoIdbYFvwExXHAc2SYLQp4tUecCJLbJieBodWLlLgIeYtHRm21x5K9v8G6Uc3rYRNVJgnwA1aCZvwxHrTDkS1S_zE2duQ0uwQYpdNtkX10Dm1hMVAg-z1o4tGrvZ_LuX98Oq5RKf_rWSyD8OpE57OSTTwXFoUfvIsk1R98zsVHM7k71M3WHvILkBRe4vDrcFEampr1z8k-maohK6A4sByPJwRq8zbIys91Cjmu4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مادر عسل دانش‌آموز مجروح مينابی از رنج‌هاى فرزندش مي‌گويد...
▪️
مستند تلویزیونی
#من_زنده_ام
به روايت مژده لواسانى
روزهای زوج و جمعه‌ها حوالی ساعت ۱۸:۳۰
📺
شبکه نسیم
▪️
محصول مرکز سیمرغ
قسمت‌های گذشته این برنامه را در تلوبیون ببینید ...</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/akhbarefori/653093" target="_blank">📅 20:52 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653092">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/svXmkwn6ajcwMLog2zZWnwQWjv0SgrvQvI2IsRIOctNLYQsncQjp7RCH2V6nCi5Sj1azXIP5Ta-_1b0Yst-vz2Ob8kt5PJr6FLQuCpJxHiYOYruXOKyu4oCt1Gts0v7vsnzJVDnOJfd2DT7rUei-9sNgn_pVo06G-iSbdZVbsbcWFMWpMtmrICa5IuB7iBIQttxT7LceNAV5mWNycawd9Do5Yia5dT9vqou-bKl3THjnKu5cR3XazFZEYUXC3R0MNvmGLX7nUaHahngcWs8K5EGG0Q4ulGS79Cvq1j8gYNb-XKJjnWW5Qx1XO37qBffWKKIRqDFuQgXwnaZqjJq3kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هلاکت یک نظامی صهیونیست در جنوب لبنان
🔹
رسانه‌های عبری از هلاکت «ایتامار سبیر» از عناصر یگان ماگلان با درجه سرگردی در نبردهای امروز جنوب لبنان خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/akhbarefori/653092" target="_blank">📅 20:31 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653091">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J-Sx92NSEmCDsqqDu59-7geTpsB1fKE_XwfL6Roi5kRvEO_a-7UOQ4ObwSjRTLt9Oc0oneLO_HWncFRzAJsaV83ykcm-lbiLQB2CpQIF8ZxJ_gDH_icHC-ZeZhM5yi1LKj7y_TwSvYjw2SoKhUkOFVe5ccnG4LFH8QE9-BrQ7bsPx8a3tp8MQq6O3LzvLHYCxJyRof1csfa1XJ3bAFTg2nTa8IZ14W7ii1070Mw338HdVST3w2n5y7mfyammUOurZcsuTpoKIhQ2X585P4maBPWTey-oWH9g50uVY_cBkpHmmXFHg0wW0oEWferqinPvPILz8iETUKVwZ6WYTjvw7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سردار عباسعلی فرزندی به یاران شهیدش پیوست
🔹
سردار عباسعلی فرزندی، رئیس پیشین دانشگاه عالی دفاع ملی امروز به‌علت بیماری و جراحات ناشی از ۸ سال دفاع مقدس دعوت حق را لبیک گفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/akhbarefori/653091" target="_blank">📅 20:22 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653090">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3da56e431.mp4?token=XGqsYupM6avIFYqHb5UW6I3HiLouOlu0-MLvXVzCflRWx1U9yTwWo_UkFmMLGIbr2aps3asgfIaWksdRf6OD4UCDv2igDO08invh_n0EFoPg5h4VbAt3girWPVxzvRNX6DGYF_pdh8rLYTys1OFHiEGlAGhr1rxukObh0-qr4UTKDiCjX7L9BPV7jpij6J3Xw0gSLIBJrw7l6qrC094Lc0ZCzXmMrYqR6gX4-6VWtOgVz1kB8LAXyp9bV7Av-YCGZ7qXPpfY0zwUSXCpm1kbXveqeJ-l5bIiYhSOA2Iv0N_CZDqFGDI82VIPQnZiPFOhtPq8nAQlqEUWi2IyhBqPgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3da56e431.mp4?token=XGqsYupM6avIFYqHb5UW6I3HiLouOlu0-MLvXVzCflRWx1U9yTwWo_UkFmMLGIbr2aps3asgfIaWksdRf6OD4UCDv2igDO08invh_n0EFoPg5h4VbAt3girWPVxzvRNX6DGYF_pdh8rLYTys1OFHiEGlAGhr1rxukObh0-qr4UTKDiCjX7L9BPV7jpij6J3Xw0gSLIBJrw7l6qrC094Lc0ZCzXmMrYqR6gX4-6VWtOgVz1kB8LAXyp9bV7Av-YCGZ7qXPpfY0zwUSXCpm1kbXveqeJ-l5bIiYhSOA2Iv0N_CZDqFGDI82VIPQnZiPFOhtPq8nAQlqEUWi2IyhBqPgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تنگه هرمز چه زمانی بسته شد و چگونه باز می‌شود؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/akhbarefori/653090" target="_blank">📅 20:11 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653089">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a17997558.mp4?token=q3tlAnobxvAe0F21mMDNyX5oTSc-xMxnfhnUyaY9QFrh1Q3SZ638fqFF9opPgV4bvfXlHRB20KVwJrw1OGZsXFRpwBeVqjegWD1F7TUUr2jf0saodwqlKZ-HD6i3soAZd75CwcHJllA6-JXO_IvdU8dyaOoJKN8HhPVi_wcZl8Eyp6Zufpg9uLCHbj5De33Nr_fHBRQh7S8kts4rH78k_UMgjxfQ_kXxbInxjIURK11qV4nQ9KK5EiMsJ0jdRIHYytvZyAomKnC9yy65WooVsgT32Ei8y5okVdW2WrMR3T5DceQlIabQeX3hnq-Ed7x-NUnigjv8290-vGAUek8dxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a17997558.mp4?token=q3tlAnobxvAe0F21mMDNyX5oTSc-xMxnfhnUyaY9QFrh1Q3SZ638fqFF9opPgV4bvfXlHRB20KVwJrw1OGZsXFRpwBeVqjegWD1F7TUUr2jf0saodwqlKZ-HD6i3soAZd75CwcHJllA6-JXO_IvdU8dyaOoJKN8HhPVi_wcZl8Eyp6Zufpg9uLCHbj5De33Nr_fHBRQh7S8kts4rH78k_UMgjxfQ_kXxbInxjIURK11qV4nQ9KK5EiMsJ0jdRIHYytvZyAomKnC9yy65WooVsgT32Ei8y5okVdW2WrMR3T5DceQlIabQeX3hnq-Ed7x-NUnigjv8290-vGAUek8dxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اشاره رهبر انقلاب به دغدغه رهبر شهید درباره افزایش جمعیت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/akhbarefori/653089" target="_blank">📅 19:56 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653088">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lV9oOyHZmS3CIY-4El2GlYu-5sIbEetnQJXfk4jnfwb2UoM95rTdHG1NTa33GZDxthq8uWla5GJ03h4kmZp6zVdLZea1mHLiP0YS7w30zSSZVC4rUEIS8yxP9Wh2n5lD-PoKpTPEAm-jZx5x5zJf732AC6F21KsCF2PG9tzZelY9UmlHKGdDJzAxvfZBmDUvldRjEuYSUCy-hsZ_5GVKrbmV3PHJ-9b5llOQkO-LunYscvmYv4B003Eguembi_m8DnbekEPK5Wd9C-ZqcXVeC4afaxkZCIbFCtH_d86FFSy_F-JXHWcw9k7eGS8AySL7CX-JSJ8jtk8RqE2fjMuzqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزیر صهیونیست، ترکیه را تهدید کرد
🔹
«میکی زوهار» وزیر کابینه نتانیاهو در سخنانی با بیان اینکه ترکیه باید به عنوان کشوری متخاصم برای این رژیم تلقی شود، تهدید کرد در صورتی که جنگی دربگیرد، آنکارا تاوان سنگینی خواهد داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/akhbarefori/653088" target="_blank">📅 19:54 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653087">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
تکمیلی/
🔹
آمریکا ۱۲ فرد، ۲۹ نهاد و ۱۹ شناور را به فهرست تحریمی خود افزود.
🔹
اکثر این تحریم‌ها با ادعای ارتباط با ایران وضع شده و تعدادی از آن‌ها نیز مرتبط با جنبش حسم مصر، فلسطین و حماس هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/akhbarefori/653087" target="_blank">📅 19:48 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653086">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73c56a8557.mp4?token=cUfX0NRFY6oipns733Dbujvd43EPYKY7aPdm9zY6ChAlrhoVE8qIqM6722Xbx5pFfnAZ1J7q7cEU2w1ZXFCKsYsvbo8v7nCT1RfYBSVlnsc7nzNNoXNGxNiIXoBaaIuBTx4vT4bsi8i8XXkw263mcKpnVADDN4AM0iv1ZxQs3A5rvSowz64D-oI7w1YVi6GNCm4ahFQbJLNycJYYwbsTd39JB_qZDcysrSJHuTVr71lXlBCx9GU5GYquWdDfIDpusu_p80k2gJPWTFWPnx-J0rz6SxaMKuYnUbYrmHrjt9wqcXQVF8Xb6_2Wo_puALZ-FR5RuG0xRcxc1gqGDkRFriVRmv8SMruRbs080Pq0MgK3P9beZm7LUJlyDT9x-T7CfGvM5DfRBLtqsPYPhvPUN71lEY_u6T8e9N34Y9NgNAOSEvuK2u0r70K2yllsWAGOnpII10a2zAkS-YU0L8Knhosu9CfBqQ0aG_tse6PXz2gLox_a-tnGyatZLX8fDwSUwBCR8UTqBggYPw4nB09rDmsG81Gis2bzsaC5XLmZrsD4tHG5GvZ34HpMzLAs02tsdIrepUPrf8zOWkrXQ6sQwIVUjAvJCTK895X_LVi6K_TF0PrORJ4MBQavY77fZ_zvP2omqFCTiI-7dVTHYil1ccknP2BimLoA7DKDDr2SJCI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73c56a8557.mp4?token=cUfX0NRFY6oipns733Dbujvd43EPYKY7aPdm9zY6ChAlrhoVE8qIqM6722Xbx5pFfnAZ1J7q7cEU2w1ZXFCKsYsvbo8v7nCT1RfYBSVlnsc7nzNNoXNGxNiIXoBaaIuBTx4vT4bsi8i8XXkw263mcKpnVADDN4AM0iv1ZxQs3A5rvSowz64D-oI7w1YVi6GNCm4ahFQbJLNycJYYwbsTd39JB_qZDcysrSJHuTVr71lXlBCx9GU5GYquWdDfIDpusu_p80k2gJPWTFWPnx-J0rz6SxaMKuYnUbYrmHrjt9wqcXQVF8Xb6_2Wo_puALZ-FR5RuG0xRcxc1gqGDkRFriVRmv8SMruRbs080Pq0MgK3P9beZm7LUJlyDT9x-T7CfGvM5DfRBLtqsPYPhvPUN71lEY_u6T8e9N34Y9NgNAOSEvuK2u0r70K2yllsWAGOnpII10a2zAkS-YU0L8Knhosu9CfBqQ0aG_tse6PXz2gLox_a-tnGyatZLX8fDwSUwBCR8UTqBggYPw4nB09rDmsG81Gis2bzsaC5XLmZrsD4tHG5GvZ34HpMzLAs02tsdIrepUPrf8zOWkrXQ6sQwIVUjAvJCTK895X_LVi6K_TF0PrORJ4MBQavY77fZ_zvP2omqFCTiI-7dVTHYil1ccknP2BimLoA7DKDDr2SJCI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مخبر: مدل حکمرانی امام خمینی و رهبر شهید ما را به جایی رساند که ابرقدرت انحصاری جهان در مقابل ما زانو می‌زند و التماس مذاکره می‌کند
🔹
مشاور و دستیار مقام معظم رهبری  در بزرگداشت رئیس جمهور شهید و شهدای خدمت:
🔹
در جنگ جهانی اول با اینکه اعلام بی طرفی شد بین ۸ تا ۱۰ میلیون نفر انسان کشته شد. در جنگ جهانی دوم هم ظرف چند ساعت تمام ارتش رضا شاهی از هم پاشیده شد و قسمت بزرگی دیگر از کشور رفت.
🔹
مدل حکمرانی امام خمینی و رهبر شهید چه بود که از این کشور چیزی درست کرده که امروز با ابرقدرت انتحاری دنیا که بر همه جهان تسلط دارد درگیر می‌شویم و او به زانو در آمده و التماس مذاکرات می‌کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/akhbarefori/653086" target="_blank">📅 19:46 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653085">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eUiu4eBm0DNv81TUlRhMBAkSs07oyUITD8yyy6vnQYjqkDyy4KVIH9L83Grs_5aVE7UiGsfzGL3316TwCrVMM-NIYngsz1QFT-6sCLqGXvRvvOgKE_PJ4qGJkdIgCHxrXYAN-a7Sdeedm1yJEh7bV3TNapShWoFWsK9FwD28u_VF7WpicUujIgz1reX7i4gTGPxbS-aiPPxALubUHvGUlpp37cebmcs0-2sVehTPNS8AsCrzJp9CjJJngL3331wxD8K50yblA-5059CwWDYRst0q9QNPg37ucgqxNJEtTO2iqjIPMKSQnV0cbOZmh_rR8-xipKy4vzRqqaRb0JqVpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی وزارت امور خارجه روسیه: سکوت در برابر بمباران تأسیسات هسته‌ای ایران توسط آمریکا و اسرائیل وحشتناک است
🔹
ماریا زاخارووا: بمباران تأسیسات هسته‌ای ایران توسط آمریکا و اسرائیل نزدیک بود به یک فاجعه جهانی منجر شود؛ این وحشتناک است که هیچ‌کس پاسخگو نبود.
🔹
مسکو معتقد است که ریاست آژانس بین‌المللی انرژی اتمی می بایست گام‌های مشخصی برای جلوگیری از گسترش تهدیدات در زمینه ایمنی هسته‌ای بردارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/akhbarefori/653085" target="_blank">📅 19:45 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653084">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71f0ea4219.mp4?token=Xvv19QtO5CqkI-cb6jDxNSW7AmMxrkYo88V7uzgBp-K2gJaBImLS-q9kO5JpN3wpEq1eQgKJ1PlFtM__zUacrR2fUqHCwoChGAt9CdxASK7cdBPT25TMWxtuHlKU74T3Hx2N8vC9f-WCsrtX0hmKCA6I4WTyZI06glDndF71LmP9-2P1dsDIwchTyyrsPxji3vidRKPDGTA_0-TDGudWqG6o9TN2YWvOUcynbF-550cbt9ycEzzX1dpO2NQkbc4kiXCnR6MCV0jPJ_28FunTU5O_uvsHRBdosFFjlnldB1C9rDsZn_VIFe-8E2yd3k98bydBK6XGteixKRRQ_cLdmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71f0ea4219.mp4?token=Xvv19QtO5CqkI-cb6jDxNSW7AmMxrkYo88V7uzgBp-K2gJaBImLS-q9kO5JpN3wpEq1eQgKJ1PlFtM__zUacrR2fUqHCwoChGAt9CdxASK7cdBPT25TMWxtuHlKU74T3Hx2N8vC9f-WCsrtX0hmKCA6I4WTyZI06glDndF71LmP9-2P1dsDIwchTyyrsPxji3vidRKPDGTA_0-TDGudWqG6o9TN2YWvOUcynbF-550cbt9ycEzzX1dpO2NQkbc4kiXCnR6MCV0jPJ_28FunTU5O_uvsHRBdosFFjlnldB1C9rDsZn_VIFe-8E2yd3k98bydBK6XGteixKRRQ_cLdmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی دولت: مقرر شد سازمان برنامه و بودجه ۵۰ درصد از پول گندم خریداری شده از گندمکاران را پرداخت کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/akhbarefori/653084" target="_blank">📅 19:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653083">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
ترامپ: گرفتن مواد غنی‌سازی شده ایران از نظر روانی مهم است
🔹
رئیس‌جمهور آمریکا دونالد ترامپ با تکرار ادعاهای خود درباره اورانیوم غنی‌سازی شده ایران گفت: فکر می‌کنم مهم است که غبار هسته‌ای را بدست آوریم، شاید از نظر روانی بیش از هر چیز دیگر.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/akhbarefori/653083" target="_blank">📅 19:31 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653082">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HXtyfX4nfsiRAZin6Ts79EHt75fjJqxN6AdsOj_uPhtPa2YwRkHmW7bXGzI6z2X1yG0Y3XaTdtreLH7peOqUkURQ2HB_hog8ZnZjtPrOv7RSggQEAJgQkobyjHzrfJzq1DRD9TJ2Em6OahwRYiSsp5Q0S3fs1mJApFuVYuJa6Zq_HzwfHbFYw1I4t0jGFvD2IYMc6mWaJMm6U4_qvZ2t8sw_HRF3Np8Xg5GRrVRYE7mwvtbMO3qvx9GMoNn8jYd2GYLzHG1-mOkBz-OPBHlhVW--tbrgn8vDOMBux1RVIQ1QzBAGzlD8NHbnNEguF2O0UEV4GZsWkMXXMEClbZwlDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رهبر انقلاب: لزوم افزایش جمعیت، یکی از مهمترین دغدغه‌های رهبر شهیدمان بوده که در بسیاری از جلسات، مراودات، و دیدارهای عمومی و اختصاصی بر آن تأکید داشتند و همچنان از مهمترین مسائل راهبردی نظام قلمداد میشود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.35K · <a href="https://t.me/akhbarefori/653082" target="_blank">📅 19:23 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653081">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bJeIdvIpczRA16m9hggWWowxotFY_48cK5nQ-lOmuSZYtjZacwLmdXms4Iop_UdPXmTiKPhXIBx1V8EsR7yw8J_FKDJHK0CJAtjVzPpG5at7xsJCWFzyCi3h92VK5kFMrUbJyCjuW04tseEPSk1uBmHczIUG4mkfgofL_Y2y4WyHcsDn1-mO6o0VgarD3MUbSxd0JS_OOUX40hOy9viae_pxOmwgVoGzdMTXn_ndrEMyIwdHB0QQxBuwZ68-FmWrVr8Dq2hBXZuFwQkLgxxvpTh4JHReAqEzkWo07jcv0sXN53d7oPwxwpT-z3NlGFS1uqYjQB6LSC8CJJxuZTksDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رهبر انقلاب: استمرار قدرت ایران نسبت مستقیمی با مسئله افزایش جمعیت دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/akhbarefori/653081" target="_blank">📅 19:14 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653080">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e9AeeETEzBeDOkqkQHBtxJ20odsekyVET6f1Etl8ilmuTU7LFv3IG3OFA5_Ej6IQ4l8qcdECJxCJKy_8-xpjRr-_RlTp2L5m1VWfHAHBx1EumbgzJdd40ZE2rcE09_UovyOsVlh0ZYuT1vfaT7UmcHVEPVWntTHIKOC2zJiLapoFUZflGOIslFziWv6Qw6RkuiKfLKEWFsLvT3SYYx-zb3eYgdK_DSPP4l-xm2P3OelhbPB-4mmmIRSZNT5pxsTYvBP9Z014MGmceWZ49gSwJAr9mMaiBuOncnUjgYYO2CvaQyid6c5CzzT4UPoYi-mBLSw9FoDhi_YMWZJ8-69uCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اطلاعات جدید از نابودی دو سوخت‌رسان آمریکایی
🔹
دو تانکر KC-۱۳۵ آمریکایی در تاریخ ۱۲ مارس بر فراز عراق با هم برخورد کردند و شش نفر کشته شدند.
🔹
پنتاگون اعلام کرد هیچ آتش خصمانه‌ای در آسمان در کار نبوده است.
🔹
اما گزارش‌های اولیه اطلاعاتی، آتش پدافند هوایی ‌نظامیان تحت حمایت ایران را در آن منطقه در آن زمان شناسایی کردن؛ که نشان می‌دهد خلبانان ممکن است اقدام به مانور فرار کرده باشند.
🔹
رهبری نظامی آمریکا این گزارش‌ها را اشتباه دانست.
🔹
انتظار می‌رود تحقیقات نتیجه بگیرند که این حادثه ناشی از خطای قابل اجتناب خلبان در فضای هوایی شلوغ بوده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/akhbarefori/653080" target="_blank">📅 19:13 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653079">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cek8k4j1TzsCROU-4tKjh5Y6swBrNfpN2zsMnSrIWjeBaxMaYMj8HPiHv7R8sdiDJZcRM4pA0UdKrkXDiQjfn8rA9Q6XyMZ-8IiybxjgbIASs5BvwjzRVZ2omuH6L_sDhdLHqzRx25HFR2ngpUteL9D781FXHziqVHovlyvU_1RzUelBRNEzTfLtjdr7VxUa_c2OftF04RIF7tghagHnskH8rnVxQIx4o-vN2hfsL1cdkM1GEMs-93Lth052zxcNwGDXAXkvGYyZQL8Bdbh1zL6DFosKru9qpD5CLU-rRzkQ4COD7UKt5pkRgWYtjRSYwpr5NEJJqTAs3KXG8FnOcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش ترامپ به واقعیت‌های جدید تنگه هرمز
🔹
رئیس‌جمهور آمریکا دونالد ترامپ با اشاره به بسته بودن تنگه هرمز ادعای جدیدی را درباره این آبراهه مطرح کرد.
🔹
رئیس‌جمهور آمریکا مدعی شد: ما تنگه هرمز را باز خواهیم کرد. ایران ۴۷ سال و حتی بیشتر از آن است که از تنگه به عنوان یک سلاح نظامی استفاده می‌کند.
🔹
ترامپ افزود: اما این تنگه آن‌ها نیست. این آب‌های بین‌الملی است. آن‌ها درسشان را یاد گرفته‌اند.
🔹
این در حالی است که تنگه هرمز تا قبل از تجاوز نظامی آمریکا به ایران باز بود و کشورهای مختلف بدون محدودیت از آن تردد می‌کردند.
🔹
اما پس از حمله به ایران، این آبراهه به روی متجاوزان و متحدانشان بسته شد و ایران تأکید کرده است که حق حاکمیت خود بر تنگه هرمز را اعمال خواهد کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/akhbarefori/653079" target="_blank">📅 19:02 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653078">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OwrksJHT1VH01FNQJoa7cZVsNX_m4pQcEMDW4R9D7nYdZ2Dowm-nd4RwpecpGaR7_63_P4omX_XVXEwEXkl7uZ8-cFm8bFw4BYafVPZx2s-KvBUYZQN1A3jNP0hnhSso-ZJOBqu83-GIuRq_h7KhzagdFPBBqjfk8WsRQUMbYeXp67nXCqov4TyQFWa19L-UhrZa9p53jnpZaOX7N57k_acl_ey0Zv2N1uUw2npngKZrrPDZMB4q9OpEx69Tn5N_b58EapxQAhdj6L9KeD-iAAs0xVtWuiyz287NZ6xo0qB1yCh7f_12OiHGEcWBEDSew0E8VQOHxuUUnZktrnOomg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
غریب‌آبادی: قاطعانه آماده مقابله با هرگونه تجاوز نظامی هستیم
🔹
معاون امور حقوقی و بین‌المللی وزارت امور خارجه امروز در واکنش به تهدیدات ترامپ با بیان اینکه ایران، یکپارچه و قاطعانه آماده مقابله با هرگونه تجاوز نظامی است، تصریح کرد: برای ما تسلیم شدن معنایی ندارد یا پیروز می‌شویم یا شهید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/akhbarefori/653078" target="_blank">📅 18:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653077">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vS13CbiPoN5lySu_9dKpjZJzGQ92gfqNyobSwBalr4WW8NFtikWhVI87wukn9b5aetg1tuj2-Td5GJSRIdYUpZzg1Hby4R3agetYB8Za4ss_WyI4AJdEXIlXkPpBJ17Nz8iqmsiEp2pjKaVYBBqCWcUiCPzg-5-O694wHg4XQM1dcodRKd0UhcbL6AL7wufs40k8kJa4w_-c8iUSJtQElx64a5R4ABilpkxMpDFFntJe_a5Ow11f6KfbXKCS0zuaNC8ik8QcL84YBbxDlxa3YXjYD_SkLCfhmn8Nsgrtd5BLC-s0RBLTSvhYdCk9hALkMjrHfEedw_6maU0lXt2cIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روایت اسکای‌نیوز از حملۀ آمریکا به مدرسۀ میناب
🔹
اسکای‌نیوز در گزارشی میدانی حمله موشکی به مدرسه شجره طیبه را فاجعه‌ای هولناک و خطای ارتش آمریکا توصیف کرد.
🔹
اسکای‌نیوز با حضور در دبستان ویران‌شده میناب و گفت‌وگو با خانواده قربانیان ابعاد تازه‌ای از حمله موشکی روز نخست جنگ آمریکا علیه ایران را روایت کرد.
🔹
به نوشته این شبکه خبری هرچند گزارش‌هایی از جمع‌ بندی اولیه نهادهای آمریکایی درباره خطای عملیاتی منتشر شده اما آمریکا پس از گذشت نزدیک به سه ماه همچنان تنها یک حرف را تکرار می‌کند: در دست بررسی است!
🔹
اسکای‌نیوز در پایان نوشت که مردم جهان این روزها برایشان سوال است که چرا مدرسه‌ای که سال‌ها روی نقشه ثبت شده بود هدف حملۀ نظامی قرار گرفت و چرا هنوز کسی مسئولیت این فاجعه را نپذیرفته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/akhbarefori/653077" target="_blank">📅 18:53 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653076">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vXsqjIUTFOHpS4zU1tnUML27eHG8fHtn00D_1frPJ_BHxBqEjAyN8GsoCvj55BXPmGKgx9CzFQhbTmT0x-BsBstbTOhRz5LUq0i67pP_aID7QNNA0yEQc6pTL-NSLVgjDKJBEMMhVNbIqteNCVGPRbyDDiiI0bUnaRbq74oizdEO_JCGKtsAM17htsSc7EnEUjfXKG0vxB1qs5paJTfLyloEDHZkaVb51MeIGTeY4BeUUUNA5_n6qAQ-Rb5q2tmWL3vgw6xqbmzivEQXn9jt8bj-897UTvL8lTBpMWaIl_WYOtsj4xBptbmA78zEvq16NBHlkcc06yxdiu18RHaDhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
افزایش ۹ هزار مگاواتی تولید برق ایران
🔹
وزیر نیرو: امسال حدود ۹ هزار مگاوات به ظرفیت تولید برق اضافه شده که این میزان تقریباً معادل ظرفیت برق کشور عراق است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/akhbarefori/653076" target="_blank">📅 18:50 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653075">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3769add69c.mp4?token=sN4TfSpSxX5dCTuFZJvwAgFyidWL3p4E2TARpqikdccXR1KvAg1c_wyt-ao1mbaFWVS9TgcafwW7X2GRL5FojAgygR_9weJkcPTxguGWRtmytUVw5RBXL32y0Xyq5kYQenkeRJkFf9NYfhNSlppxHNGpyVekZIyTjkh2tqimc6jm_BxUmsBPnEuZ3b-RCjlHZDfoUjvgV9eSSxxYBOhWZ7QfQvfQxGig4lQnvH35gpUQQo9bf2pAdDankqBWHtzSm78PUKBLy-3aIrr6eDb_68q_ANYQcllKWZooaPRajzq75yd6kA37fy3-JWsRsaPEbGrhzBH4KeZno0g3IjbQVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3769add69c.mp4?token=sN4TfSpSxX5dCTuFZJvwAgFyidWL3p4E2TARpqikdccXR1KvAg1c_wyt-ao1mbaFWVS9TgcafwW7X2GRL5FojAgygR_9weJkcPTxguGWRtmytUVw5RBXL32y0Xyq5kYQenkeRJkFf9NYfhNSlppxHNGpyVekZIyTjkh2tqimc6jm_BxUmsBPnEuZ3b-RCjlHZDfoUjvgV9eSSxxYBOhWZ7QfQvfQxGig4lQnvH35gpUQQo9bf2pAdDankqBWHtzSm78PUKBLy-3aIrr6eDb_68q_ANYQcllKWZooaPRajzq75yd6kA37fy3-JWsRsaPEbGrhzBH4KeZno0g3IjbQVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ: همه می‌گویند [جنگ با ایران] محبوبیت ندارد، اما به نظر من محبوب است
🔹
وقت ندارم موضوع را به مردم توضیح دهم چون درگیر اجرای آن هستم؛ اما وقتی درک کنند که هدف، جلوگیری از نابودی سریع لس‌آنجلس و شهرهای بزرگ با سلاح هسته‌ای است، همراه می‌شوند.
🔹
در هر صورت، چه محبوب باشد و چه نباشد باید انجامش دهم؛ چون اجازه نمی‌دهم در دورهٔ من دنیا نابود شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/akhbarefori/653075" target="_blank">📅 18:49 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653074">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aWv-Hj9KgGvI1LXQtBZB26PNX71iE3frhGr147yqc108F9nVANGv1NLWELEKFUksLTq_43TWypVTyfUroLY8QIhFEX1v_NUtrHzUu0o2pYTe0qxZh6RHhltwoClz0v7VeKkj2NBtMNtSpj2NXqWeqGVz8BUrEix53EhKXc3b_BSKhq2XF5VPpi8SeVwPtAtDsMHRXxyCHIeGwDtMNhozUJGnG5ALlpjEEqNJSQv6l5IOK6bq4dU834o43ZPjYXBqYiURBrH_O8OdXJrWJA4clzEfSu5MibcCYilwMqkhv07beVoWDf0JbLQZ1Zi06aQRbQj53KUqHVIY0rsp-6BGfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصمیم جنجالی اسموتریچ در واکنش به احتمال صدور حکم جلب بین‌المللی
🔹
وزیر دارایی رژیم صهیونیستی در واکنش به گزارش‌ها درباره درخواست صدور حکم بازداشت بین‌المللی علیه خود، اعلام کرد دستور تخلیه فوری منطقه «الخان الأحمر» در کرانه باختری را امضا کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/akhbarefori/653074" target="_blank">📅 18:45 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653073">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
ادعای ترامپ متوهم: فکر می‌کنم گرفتن غبار هسته‌ای (ذخایر اورانیوم) مهم است، شاید از نظر روانی بیشتر از هر چیز دیگری مهم باشد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/akhbarefori/653073" target="_blank">📅 18:40 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653072">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاکوهشت - دیده‌بان رشد اقتصادی ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WUsWNMMKKHjGaFkvzRZ7psy9467WT3d9aTl9Tv7nH_Y8BU0PdsnmYxNcYvHfEUT9qf7AXGrpUhrGOU1TGl0nJVn9sDdwC6491WX3R2aCgYGErZ2UyDOOai0pN1pwJRc5uWEA7WIcLfVLDGy31xUXJTPnz8oV4Gu8Wve536zYWnSuEz04vKcpLU-_k8NVMrykXcWmnorZgNmOtzGkGdQ1USdQQ1Erf7KvGvS4tPBwgvlMPStJnjq5w7G9xNUL7rxgUiSv878sxZEUxH1_gOL1QYOs5mNYfrmVaLFjcKSLb42D2m9VV-RoAQ0zOJyh-NCTcjdj2tLpdS6jQRADH1xGog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚇
اگر شهرداری تهران این‌قدر پولدار است، آن ۵۰ همت را صرف مناطق محروم کنید!
📰
فردا در شورای شهر تهران درباره طرح
رایگان شدن دائمی حمل‌ونقل عمومی
تصمیم‌گیری می‌شود و سخنگوی شهرداری نیز موافقت رسمی این نهاد را با
رایگان شدن خدمات مترو
اعلام کرده است.
⚠️
این تصمیم در صورت تحقق، مخاطراتی جدی مانند
افت کیفیت خدمات
و تحمیل
کسری بودجه
به شهر را در پی دارد؛ اما استقبال نمایندگان نشان‌دهنده
جیب پر از پول
شهرداری است که حاضر شده از درآمدهای این بخش چشم‌پوشی کند.
📈
شهرداری تهران سال گذشته حدود
۵۰ همت
از محل مالیات بر ارزش‌افزوده درآمد داشته است که ظاهراً نیاز چندانی به آن ندارد؛ از این جهت اکوهشت پیشنهاد می‌دهد این مبلغ هنگفت، صرف مخارج بااهمیت‌تری مانند
توسعه مناطق محروم
شود.
اکوهشت
- دیده‌بان رشد اقتصادی ایران
@ecohasht</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/akhbarefori/653072" target="_blank">📅 18:25 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653070">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d31e39e6b.mp4?token=njraxm0hx9lFEDF3HM7NErI9lfyzbnRrYo1KeB8m0jJFgyzoS4o2ov4-1nbAzzeemWpPyiUhJKv4vIdBqLFd-nxb9sjLDznxIIXbnWw31qQjfmcu0ImRtbwha7BDY1drTkN8Tq4o2thjmFfpIe2IkIXSlNe2sCUQZeagAhO0b9OcbiYj8eKj0snLoyPCcA664BkQHXhWYg-smr7npDsWIgxRqFXZOn2K0dpdlhETYquoLFQP1KsKrH00RfPp8YRGChMRwdCecD2vn58SM3w4L0XbA-4T2wF_T5f-iCsk9ueDFXELNGAljgQAkVVqkcGxdiX9ntmodRWxFHIihwy2zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d31e39e6b.mp4?token=njraxm0hx9lFEDF3HM7NErI9lfyzbnRrYo1KeB8m0jJFgyzoS4o2ov4-1nbAzzeemWpPyiUhJKv4vIdBqLFd-nxb9sjLDznxIIXbnWw31qQjfmcu0ImRtbwha7BDY1drTkN8Tq4o2thjmFfpIe2IkIXSlNe2sCUQZeagAhO0b9OcbiYj8eKj0snLoyPCcA664BkQHXhWYg-smr7npDsWIgxRqFXZOn2K0dpdlhETYquoLFQP1KsKrH00RfPp8YRGChMRwdCecD2vn58SM3w4L0XbA-4T2wF_T5f-iCsk9ueDFXELNGAljgQAkVVqkcGxdiX9ntmodRWxFHIihwy2zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار: دیروز چقدر به حمله به ایران نزدیک بودید؟
🔹
ترامپ: یک ساعت فاصله داشتم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/akhbarefori/653070" target="_blank">📅 18:15 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653069">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WRvTs-neqnReGF_pZN3HByH4aDpeaCXzYcSCLcFjT11lqwiPcIvNCTbucL3Ypxzl6-MNP1yX-kgX3uJuPFqgziegmqS4LEmEEq6zgSeMzBSYTnluusFmfULADiso_QK8lY5X4qLG2EhUQ3PKUbmYRnqej596wMU5ntj-fpO_LjA52ntnOAxqVNZHmJntpLRY2B6GInmP6hWqEnBg2u0behG7vAdx5xrxPBLEVcjL5sEcUoJJnIP9POKUCTiGwjxRm7FcmOMSBeYLz_XboqZsT977NDcO0X3-T8iEXCOxpBzsLByGdReQqt8RWEBVxq217ZXupqdCaAxGwAcUTXq0Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادامه تناقض‌های ترامپ درباره ایران
🔹
رئیس‌جمهور آمریکا: ممکن است مجبور باشیم ضربه بزرگی به ایران بزنیم. هنوز مطمئن نیستم. به زودی خواهیم فهمید.
🔹
این در حالی است که رئیس‌جمهور آمریکا شب گذشته گفته بود که با درخواست سران کشورهای عربی، حملات به ایران را متوقف کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/akhbarefori/653069" target="_blank">📅 18:14 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653068">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
رئیس کمیسیون اجتماعی مجلس: ۲۲۰ تا ۳۰۰ هزار کارگر ناشی از شرایط جنگی بیکار شدند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/akhbarefori/653068" target="_blank">📅 18:10 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653067">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X4ax91Znsvq-pigsfIE8lRpn4PmzPwrEkLT_NYy7i2tOZ9q3Owd2kzvhBocHfQ3MN8J0KoIXcHb1gJ0Beqnhn47L95QN2U4OBjFfXYYnZJwaNP6OWl5s8o6b2QLzC33G5BgEgi-9ByV5LiZpRFCUANQCkJhnIedQLjarHS11W9b8ZJQnS-lYUS9hOIJuBGLiXfoC8ZZFZhQpHwSyxsqk1CXIyv0VpGO3UxCl38oj3Ou5zeymenZQWMJzfNtwXbO73sLyNnjZ0n_iweV_QFKamJKjSltswasW2CYbeNpBhhyjukjBjg5DK2xOylaRMRhKJV-Fu7xBAvTt1RKwesfrkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هوای غبارآلود در شماری از شهرهای کشور
🔹
وضع قرمز و ناسالم برای همگان در شهرهای: تهران، کرج، سمنان، شهرکرد، کرمان، یزد و کاشان.
🔹
وضع بنفش و بسیار ناسالم در شهرهای: اصفهان، همدان، دره شهر ایلام، زرند کرمان، اردکان یزد و فسا فارس.
🔹
وضع قهوه ای و خطرناک در شهرهای: اهواز، شیراز، اراک، خرم آباد، دهلران ایلام، بافق یزد، انار کرمان، مرودشت فارس، دهدز، اندیکا، آبادان و دزفول در خوزستان، پلدختر، دورود و بروجرد لرستان.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/akhbarefori/653067" target="_blank">📅 18:06 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653066">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
کشف نیم‌تن مواد مخدر توسط پلیس بم
🔹
فرمانده انتظامی استان کرمان: ۴۷۴ کیلوگرم تریاک که در یک دستگاه تریلی جاسازی شده بود، در مسیر بم-کرمان کشف شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/akhbarefori/653066" target="_blank">📅 18:05 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653062">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TFmIRWD4j5EpEGxkPDxLV9Vw0go1P3q-jCBf1v-1UEQ10RafNvHPxiOoj4XihCrZGKfM6mIpntZKEty1lLQVNIz3WcXOJaQziEtp9jtgjBNgJKaLZr63KKyWQ-H7X2A7YkeM0ObzpYiwgeQJTCHpo1HRcfpfNwN7ZqxHoykYfNQboyUhQMhZhmudyYamwHPmtrLOMY9WKvsTFiope6UroxzCS0RXXDifJsvlSdl1aNnQE9RoFNcp_dymjmt-9sTk2MMuODmLIliHhFM0U5dtnASyreJAlCplVXDzyX8e7a6GxLOCoIqV6jJm6d8Y8RrFiG9rFftRE_o31CClbjOqkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I4CTLL_M17eKtooElVSl4oT0aJhvTzamjfMTo_Yt9y1IPsBDmlX6vw32By2jykErkixScvaxAbQbVF7ynmMY3YP2VAsEMR5DOSfj88ZSgsQL2fHKa1hx_G0dUv3GwsWYkXB_YcxeNyUBeAelXc3v4qFij7_D1rKsjrPyUk-2aqnUc4eRQBkQe3mVts4bmmK_3T_BOxyaXNFrIAwVophvbHX28WpYdDzopp855cddM9Dg6qWZ_IlSL-A1xvM-eXq2ne7ZUu74LUekkrxSrOnZ-iVqXEUOAfSCFrqIK3nJdD01tmY1nqnrJPQXMK19SkLF_WYQgs5ietpouPTRlm7Xmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M48YUc7TmEAYSrEAEAquuvPgKy_P0bLO6v2NkJvRsdVU3wCg6kF6TKgKgTwUiuFqycru94buuNiv0AeSc0k-kROn6PM1igs_kI81opPm0IA8yEAvxd2zdcE68hPlnhh7OFzHENg3OS8-yFTUjlFhr4uSMLKVm_2ziAcQex-3yGFFLMpsPlQE_vO-1BFOiL5hECEG5YRHPw9BR2SHyCO1IyuphGVQmjlcAKTDoKG5P228cz9voV1DUx869rQ4T_-HpM1M4D17fKc5CTZ6gfxKmL3Ve43GAlSQy5oZ_YVWauWHBs68iJVLXeY5Q6F18aqPuYe01oqkhHLZRcJCiKa3Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rqrABcQz70G5Lrh434BT7AXgOL6LBkH4TBNVQyQ7AdLYB6jp8Vv1TI7TuoutwXGp2Zzhu6_pXmVsHDkJWBwUXxAqTkvh21Hm6fWCjDornAlUCbYTqPXrDD4OHx9HJcVoF6XAD60l6YCDvc3GTnjZUVkSOg9loehSuphuR1tMFmnthp6yMp2SB8Ei4pNZ6wtAgcMSKQwNgobXCkHuD_eNUeIpBzpZGMZAc1MToaCVxypAcMaCgj59ZGygqv6jOgezlp6xRxe2dr8Qo7w739uvKVhuQohUyUGxcbQXM4HvZ0dlm2xYNYWJT7WdciXqYEIB6LE6wpLqYil20Xfomdblbg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
روضه‌خوان میانماری
🔹
همین یک جمله کافی بود تا بغض، میان آن همه آدم راه خودش را باز کند و در آخر مجلس یک نفر را از پا بیاندازد. زنی از میانمار، روبه‌روی مسجدی در قم ایستاده بود و از رنج دوری خانواده، مهاجرت و دلبستگی‌اش به امام حسین(ع) می‌گفت؛ اما آنچه دل آدم را می‌لرزاند آن یک جمله بود، جمله‌ای که اشک همه را درآورد، حتی خودش!
🔹
قصه شکستن مرزها همیشه شنیدنی است؛ قصه پل‌هایی که از روی باورهای آدم عبور می‌کنند و این یک پل بلند بود، پلی خونین که «نایپیداو» را به «تهران» وصل می‌کرد.
🔹
یادداشت مرتضی‌درخشان را در تصاویر بخوانید
@Tv_Fori</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/akhbarefori/653062" target="_blank">📅 18:01 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653061">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
‌ ادعای امارات: پهپادی که به محوطهٔ داخلی نیروگاه هسته‌ای ما اصابت کرد، از خاک عراق آمده بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/akhbarefori/653061" target="_blank">📅 17:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653060">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57f590c845.mp4?token=iy6oIM3NooL-lG7TqIDuE_UfbtFC6a6rIc-84tzRjni09F-MGAYYXwO5x0w1YlqKA8L44EEgJ6w1db5MnSLGGnm2bOom067ZCZlQabLleY_jW1Qt7Ei_8ZMVzRFPm6VXTDHeB1qqKIXskcgulLbDRYNEdVOUscqhQItyE5CUsfhB_7OP6MojFE2x2ozkTYKtNZXDt81Ii0NHrRil8jG55NlrHtbcPJZf7r-P-ApxjrjiqhPtbZi99q6j1qJU-3zQqdhxfxM-Hh3bygimCt-9sHMXmInLSRXF1BPS0fRjZOyr2gAofUglUiCPnkhgvhVmM7RXredUKWV7ZfPD9MoHHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57f590c845.mp4?token=iy6oIM3NooL-lG7TqIDuE_UfbtFC6a6rIc-84tzRjni09F-MGAYYXwO5x0w1YlqKA8L44EEgJ6w1db5MnSLGGnm2bOom067ZCZlQabLleY_jW1Qt7Ei_8ZMVzRFPm6VXTDHeB1qqKIXskcgulLbDRYNEdVOUscqhQItyE5CUsfhB_7OP6MojFE2x2ozkTYKtNZXDt81Ii0NHrRil8jG55NlrHtbcPJZf7r-P-ApxjrjiqhPtbZi99q6j1qJU-3zQqdhxfxM-Hh3bygimCt-9sHMXmInLSRXF1BPS0fRjZOyr2gAofUglUiCPnkhgvhVmM7RXredUKWV7ZfPD9MoHHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آلمان: برای بازکردن تنگه هرمز نیروی نظامی خواهیم آورد
🔹
صدر اعـظم آلمان: بستن تنگه هرمز توسط ایران خسـارات عمده‌ای به بار آورده است.
🔹
ما همراه با شـرکای خود در تلاشیم تا هرچه سریـع‌تر آزادی ناوبری را بازگردانیم.
🔹
اگر شرایط لازم فراهم شود، آلمان نیز آماده است تا برای این منـظور توانایی‌های نظـامی خود را به کار گیرد.
🔹
ایران باید به مـیز مذاکره بازگردد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/akhbarefori/653060" target="_blank">📅 17:58 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653059">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V3UE1caWvYnuzFE5IYIRFvp9pP6gOdSj3mh1lMVK4K8syfRUJVanLhMMpe2Jc6zKgaNeE0JMAlLm6j3qXPde3CNAq3IfKVRrt6MDMz4Vmldg-eyp8lVoQepGsGHQqNe7gyAm6bVyvD5iP-QmPrdoq5oEaT7ow90Q_bkSudKicIOsPZe5BNrNvfsAb6PYQX1YrPIaC7u0ZIWmUbDEF30KCcyM0i06b_JJ1njnt9IaDMrMR4T2TdXxnH6b6q-wiCZ_O3xLCj8MXJn2kZ3rrfGXbjlEwiBPhV6dFTNujeLdAFw0oNu53-HaIW4Wdd8Eoa7N_sgyxywCaCmlc1H7pzcDiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معاون وزیر خارجه: ایران یکپارچه و قاطعانه آمادهٔ مقابله با هرگونه تجاوز نظامی است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/akhbarefori/653059" target="_blank">📅 17:56 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653058">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
انهدام سکوی گنبد آهنین با پهپاد FPV حزب‌الله
🔹
حزب‌الله در ادامه ضربات مستمر و جنگ فرسایشی خود علیه نظامیان صهیونیست در جنوب لبنان، از انهدام یک‌ سکوی سامانه گنبد آهنین این رژیم خبر داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/akhbarefori/653058" target="_blank">📅 17:54 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653053">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ap5HBQ4ePVE3nKRCwFentgVj-MwfbO6ehKLOYPA36LzibY3LDtjDrPf5ng8LWowXCAjwR-vqy3U5IrJAkNMX5tQ53WxUUf9jFKW3drqQZ49VyNRVP_Xp_8QejCR20q1RxFSZjFUjKJHImvT9dCjUpO4J8DXSCxBkGwBEAyZtXpHL-qyeAD2Zbbk1aOrKd8SRsHaB2--rvW6qknGBOfBmov4mQSWHPXi6gXTzwqjmTwLlq_jd9voFAJAfrQ8nzeVZIFBgjSyhuZZ0w0RxY5jSz_1YgoozwdsOg1l2yupCDzmRV-7OI8B57aLxhZewvf4UWLNoErZBRzbwv3r3oEjJYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری برای سالروز شهادت شهید رئیسی؛ «لحظه‌ای که این خبر را شنیدم...»
🔹
همراهان عزیز خبرفوری، برای شرکت در این فراخوان کافی‌ست یک ویدئوی کوتاه حدود ۳۰ ثانیه‌ای برای الوفوری ضبط کنید و از لحظه‌ای بگویید که خبر شهادت شهید آیت‌الله رئیسی را شنیدید؛ اینکه کجا بودید، خبر را چگونه شنیدید و اولین حسی که تجربه کردید چه بود.
🔹
لطفاً ویدئوها را:
- به صورت عمودی ضبط کنید
- در محیطی آرام و با صدای واضح بگیرید
- با ذکر نام و شهر محل سکونت آغاز کنید
- حداکثر در ۳۰ ثانیه ارسال کنید
🔹
ویدئوهای منتخب در  خبرفوری منتشر خواهند شد.
آثار خود را به آیدی زیر برای ما ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/akhbarefori/653053" target="_blank">📅 17:50 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653052">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
وزارت دفاع امارات: پدافند هوایی طی ۴۸ ساعت گذشته با ۶ پهپاد مقابله کرده است
🔹
این پهپادها درصدد هدف قرار دادن تأسیسات حیاتی امارات بوده‌اند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/akhbarefori/653052" target="_blank">📅 17:50 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653051">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
مخالفت سازمان برنامه و بودجه با افزایش ۵۰۰ هزار تومانی کالابرگ
🔹
رئیس کمیسیون اجتماعی مجلس: وزارت کار می‌گوید که پیشنهاد افزایش بیش از ۵۰۰ هزار تومان یعنی ۴۰ تا ۵۰ درصدی نسبت به رقم فعلی کالابرگ را مطرح کرده اما سازمان برنامه و بودجه و مجموعه دولت هنوز به جمع‌بندی نهایی نرسیده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/akhbarefori/653051" target="_blank">📅 17:50 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653050">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iGL8Uhb8F1B4GO7dNLVlykMTiGMDWbVgOHhvvQpMgAFHxE6iOiebaTkEaA9-GkR7cDROXFpqNniJKtIVp_zdoV0N3MFLxe7eLqGW4l6AxMjG4_eiAJMjQ9r90yzDC5Ujs_8VWfFunzA4smKJHtkOC2lYjYbB3dS9my-kWSKlheL1vnEJuIf7NeRCMnycN2KcbTAirfxScVDOBKhl0RjcuI9RIAXybkPiAFN0srU6kcd0infOuf09hxoB7QXR105ZlqvoZ1t03v9GqWx-y0kjLAeX_N-0hZWjaacwfOww0k98FoMa5ldV5K9hAQ3bR7-GnzK5FSlny4ZCJ6y98CZilQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هوای غبارآلود در شماری از شهرهای کشور
🔹
وضع قرمز و ناسالم برای همگان در شهرهای
🔹
تهران ، کرج ، سمنان ، شهرکرد ، کرمان ، یزد ، کاشان
🔹
وضع بنفش و بسیار ناسالم در شهرهای
🔹
اصفهان ، همدان ، دره شهر ایلام ، زرند کرمان ،  اردکان  یزد ، فسا فارس
🔹
وضع قهوه ای و خطرناک در شهرهای
🔹
اهواز ، شیراز ، اراک ، خرم آباد ، دهلران ایلام  ، بافق یزد ، انار کرمان ،  مرودشت فارس ، دهدز ، اندیکا ، آبادان و دزفول در خوزستان ،  پلدختر ، دورود و بروجرد لرستان .
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/akhbarefori/653050" target="_blank">📅 17:45 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653049">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71e7f64ef4.mp4?token=PrAloZRkt_KvCxUMp6gbhvDXBSAs0vJtSDZQqny1X_tWa6VwfzwzIX6hc7HnFn9SuZ8iCiRYZCR2JDEFf2xZWu33CTo4EXXtmTDxZxpeZVR_P8TUsJYDXTSgjIS7fsQImfwFNKQ6Wm2eSFKrVKNNDia1RMsMq29DrCDj5Z4Z5NMgSSZvXKo0WWT7vBC-69qwjraMwQoICqhXR8R6JeiTgWGztYVe8tvT3JZqZ1oE90l8KTmMyGQ9t6S-_qOrwJGXShQkHMr5mJ5TiXQCWGiVvJyXXJEEYyXQDFajZkRhoqxYSs7jLvUcyObsaYoe5bTc_OuYILE5RMQ8DM4X09cw0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71e7f64ef4.mp4?token=PrAloZRkt_KvCxUMp6gbhvDXBSAs0vJtSDZQqny1X_tWa6VwfzwzIX6hc7HnFn9SuZ8iCiRYZCR2JDEFf2xZWu33CTo4EXXtmTDxZxpeZVR_P8TUsJYDXTSgjIS7fsQImfwFNKQ6Wm2eSFKrVKNNDia1RMsMq29DrCDj5Z4Z5NMgSSZvXKo0WWT7vBC-69qwjraMwQoICqhXR8R6JeiTgWGztYVe8tvT3JZqZ1oE90l8KTmMyGQ9t6S-_qOrwJGXShQkHMr5mJ5TiXQCWGiVvJyXXJEEYyXQDFajZkRhoqxYSs7jLvUcyObsaYoe5bTc_OuYILE5RMQ8DM4X09cw0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زن چینی خیّر مدرسه‌ساز در ایران شد
🔹
«خانم مندی ژو» خیّر چینی برای کمک به ساخت مدرسه شجره طیبه میناب داوطلب شد و مبلغ ۵ هزار دلار نقدا برای کمک به ساخت مدرسه در میناب پرداخت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/akhbarefori/653049" target="_blank">📅 17:42 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653048">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
ادامه تحریم‌های ضد ایرانی آمریکا
🔹
وبگاه وزارت خزانه‌داری آمریکا از تحریم‌های جدید مرتبط با ایران خبر داد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/akhbarefori/653048" target="_blank">📅 17:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653047">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
نیویورک‌تایمز: ایرانی‌ها الگوهای پروازی جنگنده‌های آمریکایی را مطالعه کرده‌اند
🔹
یک مقام نظامی آمریکایی گفت: «فرماندهان ایرانی، الگوهای پروازی جنگنده‌ها و بمب‌افکن‌های آمریکایی را مطالعه کرده‌اند.
🔹
سرنگونی یک فروند جنگنده F-۱۵E در ماه گذشته و آتش پدافند زمینی که به یک فروند F-۳۵ اصابت کرد، نشان داد که تاکتیک‌های پروازی آمریکا بیش از حد قابل‌پیش‌بینی شده است؛ به گونه‌ای که به ایران اجازه داده با کارآمدی بیشتری در برابر آن‌ها دفاع کند.»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/akhbarefori/653047" target="_blank">📅 17:35 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653046">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/488e524088.mp4?token=gPp5LHduKkSvyRBfQxIzN406_XHua02lbeNlp4ujmphfqwHX3LdaR_SxwPFPyUI6kDWWH8SjIu31vyx9bIrnvPT84A5KgkS5RlxwiIrSc6Q98fwXduQIM6fLPLvn8mAK8fsdS0rnwBuZI1Wz5pTltn_Z6-aI4aumnKLgbP62j2fuvzI3fYGqh85bHevGMOTUgDq3eDkpfjpmyUIrQvTooTUa5sS_wUAw7QPF_os6modfmmmGlcGR3eUCSyJFIWoEgBs-0nDTagQiR_qjBuqGG5hc9ZABpaOTqC1ctReB7SqXzZf4egXbbD8mikgyXPF8Gv-Ddwhoqxgpr6HXMobFgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/488e524088.mp4?token=gPp5LHduKkSvyRBfQxIzN406_XHua02lbeNlp4ujmphfqwHX3LdaR_SxwPFPyUI6kDWWH8SjIu31vyx9bIrnvPT84A5KgkS5RlxwiIrSc6Q98fwXduQIM6fLPLvn8mAK8fsdS0rnwBuZI1Wz5pTltn_Z6-aI4aumnKLgbP62j2fuvzI3fYGqh85bHevGMOTUgDq3eDkpfjpmyUIrQvTooTUa5sS_wUAw7QPF_os6modfmmmGlcGR3eUCSyJFIWoEgBs-0nDTagQiR_qjBuqGG5hc9ZABpaOTqC1ctReB7SqXzZf4egXbbD8mikgyXPF8Gv-Ddwhoqxgpr6HXMobFgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
«ایران، نفوذ نظامی آمریکا را به سطح پیش از ۱۹۷۵ بازمی‌گرداند»
🔹
سمیر سیفوویچ: آمریکا به سفارت سابق خود در تهران حمله کرده، چون می‌داند دیگر هرگز در ایران سفارت نخواهد داشت.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/akhbarefori/653046" target="_blank">📅 17:14 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653045">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m8-xQ6caMJwztCZ9sIWDzZIVCtbMq_JcXLSXG0HP60sOQxDmq5v3Bc91FFiBSPd7S12qzOnPrazyl6YTcA_8jMvp2iq5KUinXZdRX4yQFQ0DzOA1rCMkrki_Fv7DCRpe7Fcb0zEsfSBG7wkVyKKPE5bmB-WPvxdpuoBMN0VPxEu1AtBj4L2EwlFMAsiKMF_PXn8_UYuPD8GEl0D-cjdTQCOvxHxQrbRGavCMjKhMo2pj9Hu5By0-GB0J1QhU7rzit-dPaNwOhX6DXpUAQJmQBxJ4r9oGxeZBvda_4J65BtqU2szjXig5PyKJ6FLplrIW9SivfCH2w2_Oik7LbtBvGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جنگ با ایران رکورد گرانی بنزین در انگلیس را شکست
ایندیپندنت:
🔹
قیمت بنزین در بریتانیا از دوران بحران نفتی ایران نیز فراتر رفته و به بالاترین سطح از دسامبر ۲۰۲۲ رسیده است.
🔹
میانگین هر لیتر بنزین در جایگاه‌ها به ۱۵۸.۵ پنس رسید که از اوج قبلی (۱۵۸.۳ پنس در ۱۵ آوریل) نیز عبور کرده است. این جهش قیمتی پس از آغاز تنش‌های خاورمیانه از ۲۸ فوریه رخ داده است./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/akhbarefori/653045" target="_blank">📅 17:10 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653044">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
اذعان
عضو کمیسیون صنایع: خودروهای داخلی تا ۵۰ درصد گران‌تر شده‌اند
مصطفی پوردهقان، عضو هیئت رییسه کمیسیون صنایع مجلس در
#گفتگو
با خبرفوری:
🔹
متاسفانه حاکمیت در مقابل مصوبات مجلس ایستاده است؛ یعنی ما در سال گذشته تعرفه‌های واردات خودرو را از ۱۰۰ به ۲۰ رساندیم و به مجمع تشخیص مصلحت نظام رفت و مصلحت را در این دیدند که میزان تعرفه‌ها کاهش پیدا نکند.
🔹
خودروسازان با کیفیت پایین و قیمت دلخواه خودرو عرضه می‌کنند و مردم در صف‌های طولانی می‌مانند. قیمت برخی خودروهای داخلی به ۳ میلیارد تومان رسیده و طی ۲ تا ۳ ماه اخیر، خودروهای داخلی ۴۰ تا ۵۰ درصد و خودروهای خارجی بیش از ۱۰۰ درصد گران شده‌اند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/akhbarefori/653044" target="_blank">📅 16:52 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653043">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
یک کشته و ۱۲ زخمی در انفجار دمشق
🔹
مدیر بهداشت دمشق اعلام کرد در پی انفجار در این شهر، یک نظامی کشته و  ۱۲ نفر از نظامیان و غیرنظامیان زخمی شده‌اند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/akhbarefori/653043" target="_blank">📅 16:28 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653042">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5af7fae77.mp4?token=uVKSvTDV0cWMfPuzk_cul6pOfzC6d8MBFLJaZU3xvAH1-30qhd6NjYwz-iWbS5nYwhFKUQ4p2Hi4x_d1zPbR3eIsWLOBDl7BJUo28DkQ3of1FAYv6VX5MoghtEnPMjERMEhUxQ0uKzCcUtwB3-RpdW97z0vcACJbyc7WABTcn2WStgFfZIADvJuTrTbCJPdxZ0x5mQwp_XRHdwZjMfZr1Nw0PqBvCJORupZqk7Qu_xQ1M1WTHm_BQKTFpT4fYIGPEBu-z6GQq39wFvBYwsl9Z4qbPNdq5u0-0tZBvuHJMmFKFU7QepCWBHFHIB8dM19BF2dZHJWdcMYx-mj0HPxo5nOqq7so1n4L2FK2Su1tBxNEytuNsXvEVrCbiJDJE70-0P-Sk8EH3VXfjfjTC_ioDtv4qBn_VqrLXHCkn32MyG-3FYvJjOaPsEz7ZFKbvzZoHEQKT9olSG4zM6BRdvodUigIK26diEbFo_6lOhcpbL4srOzaSUvWDoxaVEhYyagrgI2jvhqQ9yMBCTO9ftUPg_1aL4U3i5YF-iIoowt3tWBPdicuFrvc9vJVacuquyCLuh_2VoWoNshx3k-FIDyrUO6DXmrnJ_ttLyf10U2tPttduDUsUJ6Ur-_HMX1mGiHtljIVSJMNYytV1bOIgNstJG6rPVEXSeXyn0KIilKRuEk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5af7fae77.mp4?token=uVKSvTDV0cWMfPuzk_cul6pOfzC6d8MBFLJaZU3xvAH1-30qhd6NjYwz-iWbS5nYwhFKUQ4p2Hi4x_d1zPbR3eIsWLOBDl7BJUo28DkQ3of1FAYv6VX5MoghtEnPMjERMEhUxQ0uKzCcUtwB3-RpdW97z0vcACJbyc7WABTcn2WStgFfZIADvJuTrTbCJPdxZ0x5mQwp_XRHdwZjMfZr1Nw0PqBvCJORupZqk7Qu_xQ1M1WTHm_BQKTFpT4fYIGPEBu-z6GQq39wFvBYwsl9Z4qbPNdq5u0-0tZBvuHJMmFKFU7QepCWBHFHIB8dM19BF2dZHJWdcMYx-mj0HPxo5nOqq7so1n4L2FK2Su1tBxNEytuNsXvEVrCbiJDJE70-0P-Sk8EH3VXfjfjTC_ioDtv4qBn_VqrLXHCkn32MyG-3FYvJjOaPsEz7ZFKbvzZoHEQKT9olSG4zM6BRdvodUigIK26diEbFo_6lOhcpbL4srOzaSUvWDoxaVEhYyagrgI2jvhqQ9yMBCTO9ftUPg_1aL4U3i5YF-iIoowt3tWBPdicuFrvc9vJVacuquyCLuh_2VoWoNshx3k-FIDyrUO6DXmrnJ_ttLyf10U2tPttduDUsUJ6Ur-_HMX1mGiHtljIVSJMNYytV1bOIgNstJG6rPVEXSeXyn0KIilKRuEk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تورم جهانی نتیجه جنگ با ایران
🔹
فایننشال ‌تایمز: اگر تا ماه آینده تنگهٔ هرمز باز نشود، به‌دلیل تخلیهٔ ذخایر استراتژیک شاهد موج گسترده‌تری از کمبودهای جهانی و افزایش قیمت‌ها در حوزهٔ انرژی خواهیم بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.64K · <a href="https://t.me/akhbarefori/653042" target="_blank">📅 16:20 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653041">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/917179b9ce.mp4?token=eQqiSJvLc159yiL9RKBr0AKnb6sDPGJOzZCKZVgxPW4JmvcpgMWYg393UOwMO7i3SGvNsU88An_mz3mcKR8oNn4R8w08JLUd_MNfl-4RDeCBM-yz7Uu-f7jDlZI81WMvAewwvvMmzR22IMtBB0-y4E1jZ_0ashZJBUP2xCOgbYjg1e0wzhFG1YVT79A0Ix4FKcm2GboubA95yk5fl3Lq72RlCEW5JrSykUJR_esnUJl1HgJteEzE1OmLS9DWf5UxT1zrpp4d6znwYyg8iNTmEaPai4DPs7n61uWzjptPBFgAoCXDf0P0VQ512DpIefWeq6tmOtEUtIUAKhkEc4rrTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/917179b9ce.mp4?token=eQqiSJvLc159yiL9RKBr0AKnb6sDPGJOzZCKZVgxPW4JmvcpgMWYg393UOwMO7i3SGvNsU88An_mz3mcKR8oNn4R8w08JLUd_MNfl-4RDeCBM-yz7Uu-f7jDlZI81WMvAewwvvMmzR22IMtBB0-y4E1jZ_0ashZJBUP2xCOgbYjg1e0wzhFG1YVT79A0Ix4FKcm2GboubA95yk5fl3Lq72RlCEW5JrSykUJR_esnUJl1HgJteEzE1OmLS9DWf5UxT1zrpp4d6znwYyg8iNTmEaPai4DPs7n61uWzjptPBFgAoCXDf0P0VQ512DpIefWeq6tmOtEUtIUAKhkEc4rrTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گنج ۱۰ تریلیون دلاری در کف تنگه هرمز
🔹
وقتی زمان به شماره می‌افتد اما نه برای ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/akhbarefori/653041" target="_blank">📅 16:20 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653040">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uAdKHr2099T9w4vFoBI5EVQrwEOTVfXCIggBUvUcAr2idDL6NIFpqDNqyv1RdJshXns5So8cXTFcSQkVz28brIq-tuVyOPwwW6P5ieAfvMYxMIwwqi1r_9vNN8rTZWv-QeA_2BsSSbxNn1An7ldAlDHXM0BuLtkddWWwYYPSjFLQsSVN6-CXL-3fkz2DqeGXMTHegb1DQVxgUHZUlZ4rofgDKMyhlEjKkmjly2aucOe8UZOzLh5_E2fP_EK08dYC5fecD1ZVyuzxu7OeXo_WpA5twH_sGcxF9dg2W-wiH5HtTSwqOBVdjwGjtRuYqxxE-dSDLJ2qG7PVAVgGVpGuTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دریاچه‌ای از زباله، نه آب
🔹
آب دیگر شفاف نیست؛ پلاستیک جای موج‌ها را گرفته. هر بطری رها شده، انعکاس مرگ طبیعت در سطح زمین است.  شما هم به کمپین #نه_به_پلاستیک بپیوندید و تصاویر مربوط به این کمپین را برای ما ارسال کنید
👇
@Na_be_pelastic #نه_به_پلاستیک</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/akhbarefori/653040" target="_blank">📅 16:11 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653039">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dfec4df9b.mp4?token=OTVhaAJvwqq-aIvE2bOKg8TW_9CUjMLywMI36zNj1-ncW97TaobF4bGay-8YaKEHyj0fD9kdvtaO7fNx8N1ivo64VyC5xTfj1khoOkOa6xkw86gbC0hcNmTYt8CbBAetTYwCqU9XaoI2R02us5WxwwIFhJthdf9ZPeqUEc8fZP-AgWhBRAkEbAbJUqmAkcDf1-I8MNMQhYjAOjiAFZmogaQDZiIT4X3G4PyKlXKgR5nDGzlCqVcaMZ9Wcm4sR-IBF-DCNsU3Gt34ihAlJK8fNSiyoo9txhGVnzv14BIoRWfzxD-F0qYkcgllBlSmrinyIt6x6Mo-hnRTej84MUVi7zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dfec4df9b.mp4?token=OTVhaAJvwqq-aIvE2bOKg8TW_9CUjMLywMI36zNj1-ncW97TaobF4bGay-8YaKEHyj0fD9kdvtaO7fNx8N1ivo64VyC5xTfj1khoOkOa6xkw86gbC0hcNmTYt8CbBAetTYwCqU9XaoI2R02us5WxwwIFhJthdf9ZPeqUEc8fZP-AgWhBRAkEbAbJUqmAkcDf1-I8MNMQhYjAOjiAFZmogaQDZiIT4X3G4PyKlXKgR5nDGzlCqVcaMZ9Wcm4sR-IBF-DCNsU3Gt34ihAlJK8fNSiyoo9txhGVnzv14BIoRWfzxD-F0qYkcgllBlSmrinyIt6x6Mo-hnRTej84MUVi7zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خیابون‌ها سرجاشونن اما خالی از زندگی؛ یه مهاجرت دسته‌جمعی و بی‌صدا ...
@Tv_Fori</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/akhbarefori/653039" target="_blank">📅 16:06 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653038">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
نیویورک‌تایمز: آمریکا نتوانسته شهرهای موشکی ایران را منهدم کند
🔹
یک مقام نظامی آمریکایی نوشت: «بسیاری از موشک‌های بالستیک ایران از غارهای عمیق زیرزمینی و دیگر تاسیسات حفرشده در دل کوه‌های گرانیتی مستقر شده‌اند که انهدام آن‌ها برای هواپیماهای تهاجمی آمریکایی دشوار است.
🔹
در نتیجه، آمریکا عمدتا ورودی‌های این سایت‌ها را بمباران کرد تا با ریزش کوه آن‌ها را دفن کند، اما خود سایت‌ها منهدم نشدند. ایران اکنون تعداد قابل توجهی از آن سایت‌ها را بازگشایی و پاکسازی کرده است.»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/akhbarefori/653038" target="_blank">📅 16:04 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653037">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qvEdR-3nzuaJ0HZYxDYl4P3n__-jzAJvJpLkc5xlFuXRWlvrRLVyX5GOYPwIvZmyqeoeEX6uIbVkS8MeA4p_dcbFXh3Tp6Bi7O05IB3V-twdtj9MFsGpoZZhdyFn7dGnkRvzZE-IL4o91iI-MJiub2dRmAOeVoB9ukajePU1-2-vRaXQ3olKaCKizoyqgZca5nC9P0SFhv-9iLtQYdUVnleIvnfas3MrQk11VhCNTGr__dVUNr3JIgVqjTbjezw32uOcE_o46ZPrzizAhSeYN0c4pinTWTzNLvhfeLn0h3cYvJSLfMNXBs6DJhk9EtxwFiMwnDDX4Y97Ka50ly6huA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای رویترز: آموزش پهپادی چین به نظامیان روس حاضر در جنگ اوکراین
🔹
نیروهای مسلح چین اواخر پارسال به‌طور مخفیانه حدود ۲۰۰ نیروی نظامی روسیه را در چین آموزش دادند که برخی از آ‌ن‌ها راهی میدان جنگ اوکراین شدند.
🔹
جلسات آموزشی عمدتاً روی استفاده از پهپادها تمرکز داشت که در توافق‌نامه دوزبانه روسی–چینی که نظامیان ارشد دو طرف دوم ژوئیه سال ۲۰۲۵ در پکن امضا کردند، تشریح شده است.
🔹
این گزارش در حالی است که پکن بارها بر بی‌طرفی خود در قبال جنگ اوکراین و دیپلماسی به‌عنوان تنها راه‌حل تاکید کرده و پیشنهاداتی هم برای برقراری صلح ارائه کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/akhbarefori/653037" target="_blank">📅 16:00 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653036">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
قلعه‌نویی با مدرسه پیرمردها در جام جهانی؛ تجربه تیم ملی به جوانی می‌چربد
🔹
تیم ملی ایران در آستانه جام جهانی با لیست ۳۰ نفره‌ای بسته شده که قرار است در نهایت به ۲۶ نفر برسد. با وجود تأکید روی جوان‌گرایی، میانگین سنی تیم همچنان بالای ۲۸ سال است و حتی ممکن است بیشتر هم بشود.
🔹
ترکیب فعلی بر سه اصل تجربه، جوان‌گرایی و چند پسته بودن بسته شده، اما در اکثر پست‌ها بازیکنان باتجربه دست بالا را دارند و شانس بازی برای جوان‌ترها کم است.
🔹
در خط دفاع و کناره‌ها، بالا بودن سن بازیکنان و افت نسبی عملکرد به چشم می‌آید. در خط میانی هم احتمالاً همان مهره‌های باتجربه مثل عزت‌اللهی، چشمی و قدوس بازی خواهند کرد.
🔹
در خط حمله، مهدی طارمی حضور دارد، اما مهم‌ترین غایب لیست سردار آزمون است که به دلایل ملاحظات سیاسی و شرایط تیم کنار گذاشته شده. همچنین مصدومیت قلی‌زاده هم یکی از ضربه‌های مهم به تیم بوده.
🔹
در مجموع، به نظر می‌رسد وعده جوان‌گرایی فعلاً به بعد از جام جهانی موکول شده و تیم ملی با ترکیبی نسبتاً مسن راهی این رقابت‌ها خواهد شد./ تابناک
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/akhbarefori/653036" target="_blank">📅 15:55 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653034">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VNTCHVZsz-s5zHtoP-G_7KMD6UcSQDksMUAYKg_M2WQCq9No4Oeff1gMeH7H7vk2fddFR8H7FOEcPyIWRRjDJf6L6a2AjNmBLm8wMDmFGt781zUcI9xMMx5BB7OBT8tyfk1X_Xs5DOMGitNhGo9AQHra7IV7BIptKiK7QJ4i5zsJ35LZ3506Mcz7ZE2VMDAmLDLvZ7kYOx_5iyaU8K6oW7ENU3_IxoE74yYEgB46eireUBUdpHfdG_fvmpva0Ip24bmzSFQq9MaKewjFA41lDIYISPCkcZVlwCUz6J_s51txHo3VnUh3HYpbso29O0YRow8LdqUst95dXx4g-UC88w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ضرورت تسریع بازسازی مناطق آسیب‌دیده و ساماندهی اسکان خانواده‌های متأثر از جنگ رمضان
🔹
مسعود پزشکیان در دیدار با شهردار تهران، آخرین وضعیت اقدامات و عملکرد شهرداری تهران در مدیریت شرایط جنگی، خدمات‌رسانی شهری، بازسازی مناطق آسیب‌دیده و ساماندهی اسکان خانواده‌های متأثر از جنگ رمضان را مورد بررسی قرار داد و بر ضرورت استفاده حداکثری از توان مدیریت محلی، شبکه‌های مردمی و زیرساخت‌های خدمات شهری برای ارتقای آمادگی پایتخت در شرایط بحران تأکید کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/akhbarefori/653034" target="_blank">📅 15:42 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653033">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
رسانه‌های لبنانی گزارش دادند که ارتش اشغالگر چند تن از شهروندان را در حومه کفرحمام و کفرشوبا در جنوب لبنان ربود و آنها را به مکان نامعلومی برد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/akhbarefori/653033" target="_blank">📅 15:40 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653032">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
هم‌اکنون زلزله شدید در استان لرستان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/akhbarefori/653032" target="_blank">📅 15:40 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653030">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa6601c6a8.mp4?token=jVaYcAH9vy7BXXXztxYKsNS8GXC_jF1RbYeJmIMCdvq3srJWGoRB_QPuLTERYXskPQGA4hIOkkAxrRmhgGApa4FxrI0F_qW0AVaMcvwtv8PYHh4zsvXjh-71aFz70RjVfpTWAa9FJeCsjwPcI8jZmofgES04YocbgU4z2_0WW0bTiYY35_xvHLXZvKqVE_LzCLvgo43NAktgIRxrfeA_1ma_fEQtxZ_-CKRZ6CRyu3e5XZ_yZzTpNM8cjUcyaZk-YiUMU74OJDapQirWhcW2gnRhCzG7VypLB_W9BQtAmFLmSxJrY9oYABiFRAPCFB4W_RkC1xrqX6IURL4daDAzNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa6601c6a8.mp4?token=jVaYcAH9vy7BXXXztxYKsNS8GXC_jF1RbYeJmIMCdvq3srJWGoRB_QPuLTERYXskPQGA4hIOkkAxrRmhgGApa4FxrI0F_qW0AVaMcvwtv8PYHh4zsvXjh-71aFz70RjVfpTWAa9FJeCsjwPcI8jZmofgES04YocbgU4z2_0WW0bTiYY35_xvHLXZvKqVE_LzCLvgo43NAktgIRxrfeA_1ma_fEQtxZ_-CKRZ6CRyu3e5XZ_yZzTpNM8cjUcyaZk-YiUMU74OJDapQirWhcW2gnRhCzG7VypLB_W9BQtAmFLmSxJrY9oYABiFRAPCFB4W_RkC1xrqX6IURL4daDAzNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تکمیلی /
🔹
شاهدان عینی گفتند پس از انفجار، صدای تیراندازی همچنان به گوش می‌رسد. هنوز خبری از تلفات احتمالی منتشر نشده است.
🔹
در حال حاضر نیروهای الجولانی مسیرهای منتهی به محل انفجار به ویژه مسیر فرودگاه دمشق را بسته‌اند و در وضعیت آماده‌باش قرار دارند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/akhbarefori/653030" target="_blank">📅 15:40 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653029">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
رئیس مرکز ملی فضای مجازی: در ایام جنگ روزانه ۱۰۰ حملۀ سایبری به کشور می‌شد
🔹
در جریان جنگ رمضان روزانه بیش از ۱۰۰ حمله حرفه‌ای به زیرساخت‌های کشور از جمله حوزه‌های بانکی و انرژی انجام شد که با تلاش متخصصان امنیت سایبری، بخش عمدۀ آن‌ها با موفقیت دفع شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/akhbarefori/653029" target="_blank">📅 15:40 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653028">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AynlM-DToR1CfGRUCJfrkd2EuA9-m2z3LawzlvsE9lSc1seinplLKzDawWhTvawDRVS6upSjk6cnj0QB_3bObDW5mSVM-JIGXHyaZavjl5G1wLpTxsyPtyCZpsDz216JHMY9bWjsFMi7qets7jBtmGaUnkZOjONMBWEdfc18xjhDSD8FZqA7g0PgzLAYDIuqLX_H6Sksm8ntxJKp7dSerTbfdn7EW5d_toF80DShmmjhuVMzuK55Pantt2rxAq0_Kt9ESvwGp3xykPIdK1FGcA7y5x6XvYmezmjHtCyyi4MKvDo991zbnNHRI0sphKcu2-Y4TWwbXMkb4J3HKan8og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۲.۷ همت پول حقیقی وارد بازار شد
🔹
بازار سهام امروز روندی مثبت داشت؛ شاخص‌ کل حدود ۲۵۰۰ واحد و شاخص هم‌وزن بیش از ۲۶۰۰ واحد رشد کرد. بیش از ۱۲۰ نماد از صف فروش خارج شدند و نیمی از بازار سبزپوش بود.
🔹
ارزش معاملات خرد به ۱۷ همت رسید و ورود ۲.۷ همت پول حقیقی نقش مهمی در بهبود تقاضا داشت. بازار در نهایت با صف خرید ۶ همتی بسته شد، در حالی‌ که صندوق‌های درآمد ثابت با خروج ۵.۱ همت نقدینگی همراه بودند./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/akhbarefori/653028" target="_blank">📅 15:32 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653027">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i3SyzlGDL2xCTtHy_1SUbCnZ6RC-ezgRGQ3c78N05R6Kr8gGMneUhAl303cf-t_Oq82XOdapVo2_jGBM2pF3_iZmdGzU7fG8UZY6fvoyl82srLpD0ZZd6O7S0NK7ADXgzX9dbkPbGN5Fohmd6Gt_2ZJwlud8WiNjTPqDaHgQeDc3inbL8ZPo3uF8WQt1ugPRo3AY6eKgECf5F1b_LgRuyXSAR2g0JxeWm9Kyp8jCGSs2Akt77eaSFoHHq43w3vgboGZr_QObnn4XeGlUp-uVQ9V9x4A4l3dlYaBg--4EFGfN1YW4r2Ezlw7FX9w7MmxnC2lk1gBNy3Mbww7bcWnLjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شلیک صدها موشک در روز؛ پاسخ ایران به حمله دوباره
🔹
نیویورک‌تایمز از سناریوی تازه ایران برای پاسخ به حملات احتمالی آمریکا پرده برداشت که در آن روزانه صدها موشک شلیک خواهد شد و انصارالله یمن نیز با بستن باب‌المندب می‌تواند یک‌دهم تجارت جهانی را فلج کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.62K · <a href="https://t.me/akhbarefori/653027" target="_blank">📅 15:18 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653026">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f38fb7d6ca.mp4?token=spArX3yZB2Fb6WTqcSOicricvFG-4QJT4zVxOh3VzNLnASLV0-ZRxrl3nIFwCVHuv6PFzKjEmEbcZAtZKH0x6wno3kX7JXgYvrRc5WrVIhEFVArTDNVib2GZSveyas9pQTp9DpcsbJXu7C-g72d6uX-TZ3yaX6rdFiWuNhfB2VhDLZaSNvJ2jgwKXTNnDgAfC6QmPutlQlbgFSPNq2b2OQg0-rvPLE9lEQQskcdTVsJg5E-SMGrAwLyMtAAHqXnk6BsraB_jy_lMtq8EMhUAZFQgiAAO-TuzOnbk6-R3xgyWWF6Z1bAKYCL6rf2WpEI2TfY3gY-SbIGYgUQWeKaTWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f38fb7d6ca.mp4?token=spArX3yZB2Fb6WTqcSOicricvFG-4QJT4zVxOh3VzNLnASLV0-ZRxrl3nIFwCVHuv6PFzKjEmEbcZAtZKH0x6wno3kX7JXgYvrRc5WrVIhEFVArTDNVib2GZSveyas9pQTp9DpcsbJXu7C-g72d6uX-TZ3yaX6rdFiWuNhfB2VhDLZaSNvJ2jgwKXTNnDgAfC6QmPutlQlbgFSPNq2b2OQg0-rvPLE9lEQQskcdTVsJg5E-SMGrAwLyMtAAHqXnk6BsraB_jy_lMtq8EMhUAZFQgiAAO-TuzOnbk6-R3xgyWWF6Z1bAKYCL6rf2WpEI2TfY3gY-SbIGYgUQWeKaTWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چالش‌های آموزش مجازی از نگاه شما؛ مشکلات روحی و روانی، افت تحصیلی و اضطراب و استرس در دانش‌آموزان و دانشجویان
🔹
«تجربه شما از چالش‌های آموزش غیرحضوری چیست؟»
مخاطبان خبرفوری در پاسخ به این پرسش، از مشکلات روحی و روانی در دوران آموزش مجازی گفتند.
🔹
در ادامه، بخشی از این روایت‌ها را بازنشر می‌کنیم.
الوفوری را دنبال کنید
👇
@Alo_fori</div>
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/akhbarefori/653026" target="_blank">📅 15:06 · 29 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
