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
<img src="https://cdn1.telesco.pe/file/vhU8vp1rSGrAo8yVbbvsPUf-w7BhxCOpzttFRKNw5iscqavLF6O74NRQI0haedgULLYxJ0too144hyv_pRbu_5-v3My1fPP6N1gDecLP-RaUXWMw8r_ufV4FTwb3w_ui9tr8B9Ad3Ut9Fpn1UziC_cRjpTsm24uIFNSoyfD7CoWqvHz_8CAVq7BkHcb1DnC4ayHmz8lIyXBSYgAntYAzjEr6OfUb4_dxmRVNx22hWzCsaiSyRe_7st3Ke9M-9gDFuXR4vBXGnfiTLXAkeVjDzct5lHhkAdR0tfjATZaTQIaVE0IXVskFw3b1qTpdy4T37UmaFJvOfQM1_QZtUxY3Nw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.43M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن.اینجا بعضی از چیزهایی که می‌خواستم ببینم رو همون‌جورکه می‌خواستم به خودم نشون داده بشن، می‌گذارم.استوار بر حمایت‌های مردمیماهانهvhdo.nl/patreonگاهانهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-10 13:43:38</div>
<hr>

<div class="tg-post" id="msg-77695">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JM_kwUsoFiCAVlhA6vC5NL3OZ-_BSX5PDgiCYAlqTDu-p-0DXDZfLG93k02v1WcoFlqtV9atvhja6guJaIA-jO0j9PLgf1Mwnuv1r2pqIjl5aYlV1KzjRmA9aa1sMkruu3iugu8GHWsmgHqxNajNRAh1YJRI45BlK2hTEp4ci1SZUCRU8FosSKkBlVSCOgNiTZi-VbAp8Ly0sqMICCbve6_--E2xsANaBzfmLhfjApZ-4nUkdV1BWvkgoawIP-aChAEjgMqUNIt8Y7Xfz5q5338RNm9D4VwYRnUtS0q-rBePGhq4GWg7WXJ3rvouJrJqdjtw_sm9o9C9CYNlMYoZ_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکانت ارتش کویت، ترجمه ماشین:
سامانه‌های پدافند هوایی کویت در حال مقابله با حملات پهپادهای متخاصم، در پی تجاوز جنایتکارانه ایران، هستند.
ستاد کل ارتش اعلام می‌کند که اگر صدای انفجارهایی شنیده شود، ناشی از رهگیری حملات متخاصم توسط سامانه‌های پدافند هوایی است.
از همگان درخواست می‌شود دستورالعمل‌های امنیتی و ایمنی صادرشده از سوی نهادهای ذی‌صلاح را رعایت کنند.
KuwaitArmyGHQ
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 199K · <a href="https://t.me/VahidOnline/77695" target="_blank">📅 10:04 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77694">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JnFl5oI27DZ58QsNBSIAUinufW9RIQa9EkvU83dsy7ydML2Z5axniQFq8kR3okgH2ZSRMqLj7LQGTXuZYrEXkNMK8wUOUlPocvP7GAQ9nLkdB5Xbv8d1d0sM6uPO-ep8fnQFRXSaBUU8GbVs_K_MnWYy8tTELzAdMi5iRU1YvWO7mGSYsRGUDbX-J_wn8a3lKoAHdKKcn_lSn0xIXmoTRzMIi-_4Q8jEKtVSyYExMTECrrNSjnyzLnL4FC2SDmodjgr_tX2VV7qQIm-Im37UaBMuZx8wkj7-l7OrPwRwNLxnVhRhk2LyuA_lhsIaCEkQiSxXHj9CLg0ouvTVAjlcfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا از وقوع یک حادثه دریایی در شمال شرق خصب عمان، در نزدیکی یک نفتکش گزارش داد.
ساعاتی پیش نیز گزارش شد یک نفتکش در ۱۱ مایل دریایی شمال شرقی لیما، در مسندم عمان، هدف اصابت یک پرتابه ناشناس قرار گرفت و پس از آسیب دیدن موتورخانه، از کنترل خارج شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 203K · <a href="https://t.me/VahidOnline/77694" target="_blank">📅 09:57 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77693">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ryp-35HT_g64F7pgHDtIzXVwMUHNUsfn-fG3noQvEGWWysCMHFyVr6UX65PWrdG_oSafFNjttK_jRTr88spmqPgt8i2dZxWPTQnBQHLFV1HuRRe09y0vhNtrJdhY8Tn8AgdAU_txY0x__19fhgKducX4W9mOnpr-K78Ruxq4NdUGpVo2zTt-vTkqSrT_rUtvYol44i_jIEpR9733YHLjMcSyDMBE8KHlHrjMWQSi2_CxNd06WrEyZG9Gd7mymaQm4dwIZ1y11Flv3wAIlgsIsg4mDuxBt47U0QJ9LPHa_6GE2R0LIqIdAqmQ717ntkz-lFouL2AiMss0WKLyPyeQJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدباقر قالیباف، رییس مجلس گفت: در روز اول جنگ در ۹ اسفند، ما یک‌ساعت بعد از بمباران فهمیدیم که رهبرمان کشته شده است.
او ادامه داد: تا ما توانستیم سران قوه را جمع کنیم و لاریجانی هم بیاید، ساعت هشت شب شد، آن جا تصمیم گرفتیم اعلام خبر مرگ رهبری صبح فردایش باشد. بعد این جلسه هم سریع پراکنده شدیم.
او اضافه کرد: بعدتر تصمیم گرفتیم همان سحرگاه خبر مرگ رهبری را اعلام کنیم و به مردم بگوییم به خیابان بیایید.
قالیباف در حالی می‌گوید که همان ساعت اول از مرگ خامنه‌ای مطمئن شده که مقام‌های جمهوری اسلامی تا بامداد روز بعد خبر مرگ خامنه‌ای را تکذیب کرده و اعلام می‌کردند او در اتاق فرماندهی حضور داشته و مشغول راهبری جنگ است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 202K · <a href="https://t.me/VahidOnline/77693" target="_blank">📅 09:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77692">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lbxn7IddwtWdRLxHfh76Febx1BpzLik394M4H83D3_F7tWpZ3IYHyS7RzYf6Ld_uCKdyolhgr9veMA8sVzvgCBGrpM0822KP3TP4LQtBOxXTVPvFlQa4oGJOMcHM55GKR4OhnONyCqu5Y0SPmFZq71vD1JqdtgqGU0pXPUiE1dJESyd-zrqLmEK-DKk_P75O3szddD88eT_phY4NurRFWwdGD_henRm-p0_b9AuBRp5-AI7oYEHt1dHTiZAvEv1s9Si8NKazkCP_OV57641FoNz2kLsHgB4UCfz_UpW883cqoeIXPznWjBs2cshK5VM0DPODj-dhBfzdXr9AKenGFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا اعلام کرد یک نفتکش در حدود ۱۱ مایل دریایی (بیش از ۲۰ کیلومتری) شمال شرقی لیما، در استان مسندم عمان، هدف اصابت یک پرتابه ناشناس قرار گرفت و پس از آسیب دیدن موتورخانه، از کنترل خارج شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 283K · <a href="https://t.me/VahidOnline/77692" target="_blank">📅 07:02 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77691">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Dw9e7Z6dZGHMiRemvEA4R4mwdrr-gmaJ6kwYxnoP8W1ueGhXpJJYS4q7iv_uiLU6nTfpooQb7Qk5JAUhGKgfqKIM_d_mCFu6JJhCTe32zqKu73iypFyIi3cV2R3w2nGyDsRFROOSZw1DJg8h_QGEXdplxn6ZNpbRl-wq551P43REBUddkFqUVC1Y89r8prprJIPy1TQmMLkod0SG1l3Xgy8_3hi8d348Zw5rsw7zb-RcK5549ncoO5NM-ToWkyznHPelNBYw9mlNY-2xTinAzVJmvEBEuE9DGkJqfF829e1-IuWEj9tF8-HjcIjN1HvRwGsqJ76-Aaj04t1JSh5qfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مقامات آمریکایی و اروپایی آگاه به «ان‌بی‌سی» گفتند که روسیه در حال به اشتراک‌گذاری اطلاعات ارزشمند الکترونیکی و ماهواره‌ای با ایران است که به تهران در جنگ جاری با ایالات متحده کمک می‌کند. به گفته این مقامات، ردیابی ماهواره‌ای و اطلاعات سیگنالی روسیه احتمالا ایران را قادر می‌سازد تا نیروهای آمریکایی را در حملات هوایی با دقت بیشتری هدف قرار دهد، دفاع هوایی خود را در برابر حملات ایالات متحده تقویت کند و در عملکرد تسلیحات ساخت آمریکا اختلال ایجاد نماید.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/77691" target="_blank">📅 03:06 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77690">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Wf8xUov8AVZnz8CKCEYIa8-DXj9CgimUpityJGQJYlQ4ywPgCg6UcMUeMaBru0BDC5fZxah2mcCc8bMO1CW6ZoPOZ0aVlXkj8WAdYR5c1U3t-1f8VsPN3L2NYltdjT12w3319fBTAsBKDQyrasuObiNRbcpBo50RdN2TcAo5dC4BXwCKpIXTd9MHvGx48V1TagY3vq9DKHGFRfKX-MzRLxcAC9eqxVp4VjrvCqOc7m79tA3AEx5DJYXOJRCgFg-B9l3IvRYsttq7g5LDfkN0kEMC0R84Wkd4U3JHEvZti8phejUbkcJVmb4sRBxBtmqcXwh6ahRVGAWuGNA7Dk5w2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">"
ترامپ دستور حمله‌ای تازه به ایران را صادر کرد
"
وال‌استریت ژورنال
به نقل از مقام‌های آمریکایی گزارش داد دونالد ترامپ، رییس‌جمهوری آمریکا، طرح حمله جدید به ایران را که در کمپ دیوید ارائه شده بود، تصویب کرده و این عملیات ممکن است از آخر هفته (شنبه و یکشنبه) آغاز شود و چند روز ادامه یابد.
به گفته این منابع، هرگونه پیشرفت فوری در دیپلماسی یا تغییر نظر ترامپ می‌تواند اجرای حملات را متوقف کرده و مسیر مذاکرات را دوباره باز کند.
این روزنامه نوشت یکی از گزینه‌های مورد بررسی، کارزار دو هفته‌ای حملات هوایی فشرده برای تضعیف توان موشکی جمهوری اسلامی است.
مقام‌های آمریکایی گفتند ترامپ معتقد است توافق موقت صلح کارساز نبوده و همچنان بر توقف برنامه هسته‌ای جمهوری اسلامی و پایان کنترل تهران بر تنگه هرمز اصرار دارد، در حالی که تهران از مواضع خود عقب‌نشینی نکرده است.
وال‌استریت ژورنال افزود مشاوران نظامی ترامپ کاهش ذخایر مهمات آمریکا را یکی از مخاطرات احتمالی این عملیات ارزیابی کرده‌اند.
@
VahidOOnLine
اکسیوس:
ترامپ حمله به اهداف انرژی ایران در چند روز آینده را بررسی می‌کند
ترجمه ماشین: دونالد ترامپ، رئیس‌جمهوری آمریکا، به‌طور جدی در حال بررسی انجام حملاتی علیه اهداف انرژی در ایران طی چند روز آینده است، اما هنوز دستور نهایی اجرای آن را صادر نکرده است؛ یک مقام آمریکایی روز جمعه این موضوع را به اکسیوس گفت.
چرا اهمیت دارد:
هدف از کارزار جدید بمباران آمریکا علیه اهداف انرژی و زیرساختی در ایران، تلاش برای واداشتن ایرانی‌ها به پذیرش شروط ایالات متحده در مذاکرات جاری آتش‌بس خواهد بود.
▪️
این حملات ممکن است برای نخستین‌بار پس از چندین هفته، ارتش اسرائیل را نیز درگیر کند و چنین تشدیدی احتمالاً به حملات موشکی ایران علیه اسرائیل منجر خواهد شد.
▪️
سی‌بی‌اس نیوز و وال‌استریت ژورنال نخستین رسانه‌هایی بودند که درباره حملات احتمالی گزارش دادند.
آنها چه می‌گویند:
ترامپ در آغاز جلسه روز جمعه کابینه به حمله احتمالی اشاره کرد و گفت: «خب، ما خیلی سخت به آنها ضربه خواهیم زد و می‌دانید، بالاخره در مقطعی خواهند گفت که دیگر نمی‌توانیم تحمل کنیم.»
▪️
او افزود هرچه ایالات متحده حملات بیشتری انجام دهد، ایرانی‌ها ضعیف‌تر می‌شوند «و بعد کم‌کم از پا می‌افتند.»
▪️
کارولین لیویت، سخنگوی کاخ سفید، به اکسیوس گفت: «همان‌طور که رئیس‌جمهور ترامپ امروز در جلسه کابینه گفت، ایالات متحده پیروز خواهد شد و در دوران ریاست‌جمهوری او، ایران به سلاح هسته‌ای دست نخواهد یافت.»
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 384K · <a href="https://t.me/VahidOnline/77690" target="_blank">📅 01:02 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77689">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EcYyU7HUvSoC4fnh9xm7XSpwFLUNmCBWs9x1ORfFZK-y0Eoomc4zXaJTm8CL5CJ9cfZbg96OLiZAFkkb4A--MH9NdbDy7Z9ZM6gdXYm1RHSHgO6U2DHkAOVf4M6ety3h04S9H0IrFL3gMJDEKDzeikgzVH4MsTiHrBpdp4WRlnJCYjDYlOHf12zc7JeMg0CMX7cdYJmjKNhmgVE02nMeOYhid0LmPf30xKx_Y3JiymeeFUjep2Bk8HHuTZ0HClxcjPVPC5r4Z892mOdhm_B2dljuMXefhZv7ugV2XcNr-GpSMA9YqxnneAhTFllB2D8we_F-6ah84OusYfpCDfO9Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">"
آمریکا و اسرائیل برای بمباران اهداف مرتبط با انرژی در ایران آماده می‌شوند
"
سی‌بی‌اس به نقل از منابع
ترجمه ماشین:
واشنگتن — چندین منبع به سی‌بی‌اس نیوز گفتند که ایالات متحده و اسرائیل در حال برنامه‌ریزی برای اجرای یکی از شدیدترین کارزارهای بمباران تاکنون علیه اهداف زیرساخت‌های انرژی در ایران هستند و احتمال انجام حملات در طول تعطیلات آخر هفته وجود دارد.
بحث‌هایی درباره تلاش برای پایان دادن به عملیات تا زمان بازگشایی بازارهای مالی در روز دوشنبه مطرح شده بود، زیرا نگرانی‌هایی درباره تأثیر بمباران‌ها بر اقتصاد آمریکا و جهان وجود دارد، اما زمان مشخصی برای پایان عملیات قطعی نشده بود.
به گفته چندین منبع آمریکایی، اسرائیلی‌ها در جریان قرار گرفته‌اند و در حال هماهنگی با ایالات متحده هستند. این منابع گفتند رئیس‌جمهور هنوز دستور نهایی آغاز حملات را صادر نکرده است.
سخنگوی دولت اسرائیل به درخواست اظهارنظر پاسخ نداد.
یک عملیات مشترک به معنای بازگشت اسرائیل به عملیات رزمی خواهد بود؛ عملیاتی که این کشور در جریان آتش‌بس میانجی‌گری‌شده از سوی آمریکا متوقف کرده بود. از زمانی که تفاهم‌نامه از هم پاشید و ایالات متحده در اوایل ژوئیه عملیات رزمی را از سر گرفت، ایران اسرائیل را هدف قرار نداده است.
به گفته منابعی که بعداً در جریان قرار گرفتند، طرح حمله نظامی روز جمعه در نشست کابینه دونالد ترامپ، رئیس‌جمهور آمریکا، در کمپ دیوید مطرح شد. یکی از منابع گفت برخی از دستیاران کاخ سفید که بر مسائل سیاسی تمرکز دارند، به‌شدت با این طرح مخالف بودند.
زمانی که خبرنگاران در اتاق حضور داشتند، آقای ترامپ گفت: «ما آن‌ها را بسیار سخت هدف قرار خواهیم داد. بالاخره در مقطعی خواهند گفت: “دیگر نمی‌توانیم تحمل کنیم.”»
او در پاسخ به پرسش خبرنگاران درباره احیای دیپلماسی گفت: «فکر می‌کنم ما فقط می‌خواهیم پیروز شویم.»
دو منبع گفتند زیرساخت‌های انرژی، از جمله نیروگاه‌ها و پالایشگاه‌ها، احتمالاً هدف قرار خواهند گرفت.
کارولین لیویت، سخنگوی مطبوعاتی کاخ سفید، در بیانیه‌ای به سی‌بی‌اس نیوز گفت: «همان‌طور که رئیس‌جمهور ترامپ امروز در نشست کابینه خود گفت، ایالات متحده پیروز خواهد شد و در دوران ریاست‌جمهوری او، ایران به سلاح هسته‌ای دست نخواهد یافت.»
شان پارنل، سخنگوی ارشد پنتاگون، گفت پنتاگون پیش از آنکه رئیس‌جمهور تصمیم نهایی خود را بگیرد، درباره اهداف اظهارنظر نخواهد کرد.
پارنل در بیانیه‌ای گفت: «وزارت جنگ کاملاً آماده و مهیای عملیات است و می‌تواند در هر لحظه دستورات رئیس‌جمهور را اجرا کند.»
یک مقام پیشین نظامی آمریکا به سی‌بی‌اس گفت، فایده حمله به زیرساخت‌های انرژی این خواهد بود که بر توان نیروهای نظامی ایران برای ارائه خدمات و اداره مؤثر کشور تأثیر بگذارد.
یک مقام ارشد اسرائیلی گفت هنگامی که آقای ترامپ و بنیامین نتانیاهو، نخست‌وزیر اسرائیل، اوایل این هفته دیدار کردند، نتانیاهو او را در جریان سه گزینه برای جنگ قرار داد که یکی از آن‌ها حملات نظامی متمرکز بر مسیرهای تدارک‌رسانی زمینی بود. نتانیاهو همچنین با هگست، وزیر دفاع آمریکا، دیدار کرد.
یک مقام آمریکایی گفت ایالات متحده در جریان این درگیری پیش‌تر به پل‌هایی با کاربری دوگانه — که نظامیان و غیرنظامیان از آن‌ها استفاده می‌کردند — حمله کرده است.
روز جمعه گفت‌وگوهایی در سطوح عالی دولت آمریکا درباره قطع برق سراسر تهران انجام شد، اما تا بعدازظهر جمعه هیچ تصمیمی گرفته نشده بود.
هفته گذشته، آقای ترامپ در تروث سوشال نوشت که در ازای هر حمله به یک کشتی در تنگه هرمز، یک پل یا نیروگاه ایرانی را بمباران و نابود خواهد کرد.
این خبر فوری است و به‌روزرسانی خواهد شد.
cbsnews
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 359K · <a href="https://t.me/VahidOnline/77689" target="_blank">📅 00:38 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77688">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kYNT11sfpBm2fMxUs9d2GBOgECiB9IzRs8NKcWPtYSSf17_7WspVCHNhoeA5EZBtSYC7GYp7-A_zEFVH2HCT8gGtwtesiXP7osUZLspt-1dXXPwe49JsxP-jD8qS6SbX9tOiwA6r8bUkQaaYDDQ1CVEJhu60DQJPydVjtXiNTegprRPyZrSs4ISufgMOrTj4_KDRaPzSXhqXZzwIFAUO7lQD2yFFy3GHtVxN7UuJqu2AsDlmj-HnGgFdlrsJOrmMsrgtFahhTqKmsJATIpssgpS-yO6Fy2RuV7tkFr1aSrIIEjZ5rVM1yK4534qx1OaZHArVSvaWnDG-fmxgvsk5fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایتالیا پس از بحران مهاجران در سبته، اجرای نظام تردد آزاد در منطقه شنگن با اسپانیا را به‌طور موقت تعلیق کرد. این اقدام پس از آن انجام شد که مقام‌های اسپانیا روز جمعه اعلام کردند بیش از ۶۰ هزار نفر طی ۲۴ ساعت از طریق زمین و دریا وارد سبته شده‌اند. به گفته مقام‌های…</div>
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/77688" target="_blank">📅 00:30 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77686">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bc5klE3kZqrPXhqRhs9RykW_HIwmfxkvf0AeKviNeiY5PYyQ_BEpXuprtI6ymxnHdSasju3kmHZAZ-_B2bmVyqDHZ1YJo0LwDnJlpV-GDaBpugKUV57w9pBz_jR0iXncg6_k5dP84PjY2eX8pCahcExjb-KRzwuJaUUbFcK2Kpe4uetP7iHGigSVJjbJgJ58r61CmxVaCLUIW0u-esKbQmmu6z7G-_VWBZX2skBzxuxVLZ0I2Pfn4x19ZNLNVr7qfvzGvsawqUNWjuOhcnP_Q_GRhg4EfdIkmu6DT_CTcS4Fry9FcRlL-uVWJH2jNLh14ToQy9nzKw9MHLKKe9qVyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رویترز روز جمعه ۹مرداد۱۴۰۵
گزارشی تحقیقی
منتشر کرده، از استفاده سپاه از شبکه قمار غیرقانونی ایران که با آن میلیاردها دلار را به رغم تحریم‌ها جابه‌جا می‌کند.در این گزارش به یک صرافی ارز دیجیتال مستقر در دوبی اشاره شده که  به مرکزی برای جابه‌جایی پول‌های غیرقانونی ایران تبدیل شده است.
در گزارش رویترز صرافی مذکور «شل‌بیت» معرفی شده و تایید شده است که این صرافی، یک شبکه گسترده قمار را که توسط دو اینفلوئنسر سرشناس و بین‌المللی در شبکه‌های اجتماعی اداره می‌شود، به فعالیت‌های استخراج بیت‌کوین و بانک مرکزی ایران مرتبط می‌کند.
بنابر گزارش منتشر شده، «شل‌بیت» صدها میلیون دلار ارز دیجیتال را به «بایننس»، بزرگ‌ترین صرافی ارز دیجیتال جهان، منتقل کرده است. دو شرکت تحقیقاتی حوزه ارزهای دیجیتال و یک تحلیلگر مستقل مدارکی ارایه کرده‌اند نشان می‌دهد نشانی ثبت‌شده صرافی بدون مجوز «شل‌بیت» دفتری در بالای یک هتل ارزان‌قیمت در محله‌ای معمولی و نه‌چندان مطرح در دوبی است. این صرافی توسط یک ایرانی مقیم خارج از کشور اداره می‌شود. رویترز اطلاعات ارایه شده در این زمینه را تایید کرده است.
در بخش دیگری از این گزارش آمده است که یکی از مشتریان اصلی «شل‌بیت»، یک شبکه قمار فارسی‌زبان متشکل از بیش از ۲ هزار وب‌سایت است که توسط دو اینفلوئنسر مشهور ایرانی در شبکه‌های اجتماعی تبلیغ و اداره می‌شود. گفته شده که این دو ارتباطاتی در سطوح بالای حکومت ایران دارند.
یکی از آن‌ها در یک ویلای گران‌قیمت در مادرید فعالیت می‌کند و دیگری تا همین اواخر در یک هتل لوکس در هنگ‌کنگ مستقر بود.
هر دو اینفلوئنسر اشاره شده و همچنین فرد اصلی اداره کننده صرافی «شل‌بیت» در سال ۲۰۲۳ در ایران به اتهام مشارکت در یک پرونده قمار غیرقانونی، محکوم شدند.
مطابق قوانین جمهوری اسلامی «قمار کردن» امری غیرقانونی است و مجازات‌های حبس و شلاق برای مرتکبان به‌دنبال دارد با این‌همه گزارش رویترز تایید می‌کند که این شبکه قمار تازه شناسایی شده به سیستم پرداخت آنلاین ایران که مستقیما تحت نظارت بانک مرکزی است دسترسی دارد.
شل بیت بر اساس گزارش رویترز در مرکز عملیاتی است که شبکه قمار، بانک مرکزی و دیگر نهادهای تحریم‌شده ایرانی را به بازارهای جهانی ارزهای دیجیتال مرتبط می‌کند.
یکی از چهره‌های اصلی این شبکه قمار، «ساشا سبحانی»، پسر یک دیپلمات و سفیر پیشین ایران و دیگری «پویان مختاری»، یک چهره مشهور شبکه‌های اجتماعی و خواننده است که پس از اخراج از دوبی در اواخر ماه آوریل، مدتی بین هتل‌های لوکس هنگ‌کنگ جابه‌جا می‌شد.
پویان مختاری اخیرا و در جریان جنگ آمریکا و اسراییل با انتشار ویدیویی گفت که مخالف جمهوری اسلامی نیست و دچار «تحول فکری» شده است.
تحقیقات رویترز آشکار می‌کند که سپاه پاسداران سال‌ها پیش کنترل بزرگ‌ترین وب‌سایت‌های قمار قابل دسترس در ایران را به دست گرفته و از آن زمان تاکنون از این وب‌سایت‌ها برای انتقال پول به خارج از کشور استفاده کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 345K · <a href="https://t.me/VahidOnline/77686" target="_blank">📅 22:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77680">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cMBR_HCxcqt4tI7TfA3KTctUQmRNJrHuk4TJZ9JbnRVn0A06YKmu6ekDODeSyPQB1ZLg1qg4r0UaqfafqSZDWgZnnIvp0peOL8Jm3uYjzm_ylMPUgSXRV-QlCPRFY_1uicvc2km3wWmr6VAVqxTG5KHrEbs_1Gy0FHtR-VXLFxWikBDkneIEb_SmCAg9XhoQBT1DnElG5UzueOMNt1U6k6H_HA_2rPzoG-MiKjSkXsMYpMz7yOT1uCGzRVmNHONYhFzOM4Qa_Yjo2-0O_0o7KQLRP46cr8wzsbE5BSnaqsCgelU_N5UZ-T1BQnZTjna_UKEURTQqN91UObin2FmGgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eERBPJsyjgcucyy7v5OGLekDAyiAfB039_eocFmRUGtvGEM-jNP4In3Qn13wWeHxSa8IrjopIo1IoU5ahwxyL1g0Wb6Hf7XIcGALKyKOyhlVQNnu8h1_0xGo42-eRdnrzV_melt0I6Pg4UWX1QuSgTtBxJPq243AM8AaplAt7Cwq7gljjJz0qFTS2O4aySKgUQoPZ0ySAK-_RAdIjoLcBtCS1_Z2B-J2lZhMqq9FYCayAtjGmSXAVvAMsTZ5h665AFW55erPLHTADlxkY9G0BRzfFID1wT7j-Yneq-0jK3ZAY6vfNb0eOWIEDY95XyN_CoKSn3-al0OpVQEpe6zcpg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ac9f2fb35b.mp4?token=Nv593TtHrjJ6kBQy6FJftJ0ROslEcOVu90Sx4jSlR0Ez2ILSq1IxJ7RsvPn1B353s0Z42MxP8LzlHyGLK1IE1D1dxswvPtutG3yaHP8DhsCB2Rgvzj2AUC-TxN0STA347dAmkRK3lZOL3VghlChji8yGLUKaC4X2gK8s1swB7mQyZQoGpGXtkQxoqjbmYKi3rVyFo8M9LhsrIdR69tr9Yce-_iUXkP5NceYz6mMnDmSsubO49GSn7fD6TkpV43NoBJXOrJ5ZTTzCkc0RpxlWAzyPIg37WeOeArSbhggqkn7-w7BildhJI8BLFRQ9fUcR7ykAME0aluLoelvHBE5nkA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ac9f2fb35b.mp4?token=Nv593TtHrjJ6kBQy6FJftJ0ROslEcOVu90Sx4jSlR0Ez2ILSq1IxJ7RsvPn1B353s0Z42MxP8LzlHyGLK1IE1D1dxswvPtutG3yaHP8DhsCB2Rgvzj2AUC-TxN0STA347dAmkRK3lZOL3VghlChji8yGLUKaC4X2gK8s1swB7mQyZQoGpGXtkQxoqjbmYKi3rVyFo8M9LhsrIdR69tr9Yce-_iUXkP5NceYz6mMnDmSsubO49GSn7fD6TkpV43NoBJXOrJ5ZTTzCkc0RpxlWAzyPIg37WeOeArSbhggqkn7-w7BildhJI8BLFRQ9fUcR7ykAME0aluLoelvHBE5nkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایتالیا پس از بحران مهاجران در سبته، اجرای نظام تردد آزاد در منطقه شنگن با اسپانیا را به‌طور موقت تعلیق کرد.
این اقدام پس از آن انجام شد که مقام‌های اسپانیا روز جمعه اعلام کردند بیش از ۶۰ هزار نفر طی ۲۴ ساعت از طریق زمین و دریا وارد سبته شده‌اند. به گفته مقام‌های اسپانیا، پس از این موج ورود مهاجران، حدود ۳۷ هزار و ۵۰۰ نفر به‌صورت داوطلبانه به مراکش بازگشته‌اند.
در جریان تلاش برای عبور از مرز، دست‌کم ۵۷ نفر جان باختند؛ شماری بر اثر غرق‌شدن و برخی دیگر در ازدحام هنگام عبور از موانع مرزی.
پدرو سانچز، نخست‌وزیر اسپانیا، این رویداد را «نقض حاکمیت ارضی اسپانیا» خواند و گفت روند بازگرداندن مهاجران فاقد مدارک قانونی با همکاری مراکش تسریع خواهد شد.
اتحادیه اروپا در شرایط استثنایی به کشورهای عضو اجازه می‌دهد به‌طور موقت کنترل مرزهای داخلی منطقه شنگن را دوباره برقرار کنند.
@
VahidHeadline
پیش‌تر:
هزاران مهاجر از شامگاه پنج‌شنبه تا صبح جمعه با عبور از مرزهای مراکش وارد مناطق تحت اداره اسپانیا در شمال آفریقا شدند
ورود مهاجران در تمام طول شب ادامه داشته و صبح جمعه نیز همچنان ادامه پیدا کرده است.
همزمان، تصاویر خبرگزاری رویترز، هجوم جمعیتی از مهاجران به گذرگاه مرزی میان مراکش و شهر ملیلیه اسپانیا در شمال آفریقا، را نشان می‌دهد.
در سئوتا، دولت اسپانیا برای مقابله با صدها مهاجری که از مسیر دریا و خشکی وارد این منطقه شده‌اند، یگان‌های نظامی را مستقر کرده است.
تصاویر منتشرشده نشان می‌دهد صدها مهاجر با شنا کردن یا استفاده از تایرهای بادی از سمت مراکش تلاش کرده‌اند خود را به سئوتا برسانند و گروهی دیگر نیز با عبور از یک دروازه مرزی زمینی وارد شهر شده‌اند.
@
VahidOOnLine
وزیر کشور فرانسه روز جمعه اعلام کرد پاریس در پی ورود هزاران مهاجر از مراکش به سئوتا، کنترل‌های مرزی خود با اسپانیا را افزایش خواهد داد.
@
VahidOOnLine
فنلاند اعلام کرد از پیشنهاد ایتالیا برای تعلیق عضویت اسپانیا در منطقه بدون کنترل مرزی شنگن حمایت می‌کند. اقدامی که در پی ورود ده‌ها هزار مهاجر به منطقه سئوتا، تحت حاکمیت اسپانیا در شمال آفریقا، مطرح شده است.
@
VahidOOnLine
پدرو سانچز، نخست‌وزیر اسپانیا، روز جمعه نهم مرداد ماه، ورود گسترده مهاجران به سئوتا، منطقه تحت حاکمیت این کشور در شمال آفریقا، را «نقض و حمله به تمامیت ارضی اسپانیا» محکوم کرد.
سانچز پس از موج اخیر عبور مهاجران از مرز مراکش به سئوتا، این اقدام را محکوم کرد و تاکید کرد دولت اسپانیا از حاکمیت و مرزهای خود دفاع خواهد کرد.
@
VahidOOnLine
ایلان ماسک، میلیاردر آمریکایی و مالک شرکت‌های تسلا و اسپیس‌ایکس، در واکنش به ورود گسترده مهاجران مراکشی به شهر سئوتا در اسپانیا، با انتشار تصاویری از فیلم «جنگ جهانی زد»، این وضعیت را به «آخرالزمان زامبی‌ها» تشبیه کرد و نوشت: «وای، اوضاع اسپانیا واقعا دیوانه‌کننده به نظر می‌رسد!»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/77680" target="_blank">📅 22:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77678">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">نشست خبری دولت ترامپ در کمپ‌دیوید
ویدیوی کامل با زیرنویس فارسی:
۱۰۰ مگابایت
نسخه یک گیگابایتی:
اینجا
متن فارسی ۱۶ بازه از ویدیو
بخش‌هایی از متن لینک بالا:
🔻
ترامپ:
در مینه‌سوتا یک حمله سایبری رخ داده و آن را به ایران نسبت داده‌اند.
فکر نمی‌کنم چنین باشد. من مینه‌سوتا را مقصر می‌دانم، چون به‌شدت بی‌کفایت هستند. حمله‌ای سایبری به ۳۰ تأسیسات آب انجام شد و من مینه‌سوتا و فرماندار فاسد آن را مقصر می‌دانم.
آن‌ها دوست دارند بگویند: «اوه، کار ایران بود.» ایران باید خیلی خوش‌شانس باشد. ایران مشکلات بزرگ‌تری از نگرانی درباره مینه‌سوتا دارد.
....
🔻
ترامپ:
جنگی در جریان است. شاید شما آن را جنگ بنامید؛ من شاید آن را عملیات نظامی بنامم، چون آن‌ها دیگر نیروی دریایی ندارند؛ نابود شده است. نیروی هوایی‌شان نابود شده است. هواپیما ندارند.
بخش بزرگی از موشک‌هایشان از میان رفته است. هنوز مقداری دارند، اما بسیار کمتر از چهار یا پنج ماه قبل. ظرفیت تولیدشان تقریباً از میان رفته و ظرفیت پهپادی‌شان نیز تقریباً نابود شده است.
تعداد بسیار کمی دارند، اما هنوز مقداری باقی مانده است. از نظر من اگر حتی یکی داشته باشند، همان هم بیش از حد زیاد است.
🔻
به ویتنام نگاه کنید؛ ۲۰ سال آنجا بودند. به افغانستان نگاه کنید؛ سال‌های زیادی آنجا بودند. به جنگ کره یا هر جنگ دیگری نگاه کنید؛ سال‌ها طول کشید. ما پنج ماه است وارد شده‌ایم و توان نظامی آن‌ها را نابود کرده‌ایم.
باز هم مقداری برایشان باقی مانده، اما به‌زودی همان مقدار هم باقی نخواهد ماند.
🔻
مارکو روبیو:
نخستین موضوع، دادگاه کیفری بین‌المللی است؛ سازمانی بین‌المللی و نامشروع. خودشان را نامشروع کرده‌اند، چون ادعا می‌کنند حتی اگر عضو آن دادگاه نباشید، باز هم می‌توانند به سراغتان بیایند.
معنای واقعی آن این است که در آینده نظامیان آمریکایی، رهبران سیاسی و افراد دیگر ممکن است از سوی این دادگاه کیفری بین‌المللی تحت کیفرخواست قرار بگیرند. ...
🔻
ترامپ:
هیچ اطلاعاتی وجود ندارد که نشان دهد آن‌ها دنبال من هستند. البته ممکن است چنین اتفاقی بیفتد.
حرف من این است که این یعنی او نمی‌خواهد از من دفاع کند؛ می‌خواهد از بی‌بی و افراد مختلف دیگری دفاع کند.
افراد زیادی هستند که نباید به این شکل با آن‌ها برخورد شود، اما در حال حاضر هیچ نشانه‌ای وجود ندارد که من یکی از آن‌ها باشم.
....
🔻
پیت هگست:
... تعجب می‌کنید چرا حوثی‌ها در این درگیری حضور ندارند، با اینکه نیروی نیابتی ایران هستند؟ چون ۴۵ روز سنگینی قدرت آمریکا را احساس کردند. و شما شجاعت انجام این کار را داشتید.
🔻
اسکات بسنت:
... در مارس ۲۰۲۵ شروع کردیم. در دسامبر ۲۰۲۵، بزرگ‌ترین بانک ایران فروپاشید. بانک مرکزی مجبور شد پول چاپ کند و این باعث تورم شد.
اکنون تورم آن‌ها ۱۸۰ درصد است. قادر به پرداخت حقوق نیروهایشان نیستند و به دستور شما در سراسر جهان به‌دنبال دارایی‌هایشان می‌گردیم.
این پول به مردم ایران و آمریکایی‌هایی می‌رسد که از اقدامات ایرانی‌ها آسیب دیده‌اند؛ چه در ماجرای ناو یو‌اس‌اس کول، چه پادگان‌های لبنان، یا حملات ایرانی‌ها به آن کشتی‌های در حال خروج.
مشارکت در این کار برای من افتخار بوده و مشتاق ادامه آن هستم.
🔽
درباره ادامه جنگ:
🔺
خبرنگار:
آقای رئیس‌جمهور، در ۱۰ روز گذشته حملات میان ایران و ایالات متحده را دیده‌ایم. چگونه آتش‌بس را احیا می‌کنید و دیپلماسی را دوباره از سر می‌گیرید؟
🔻
ترامپ:
فکر می‌کنم فقط می‌خواهیم پیروز شویم. عملکردمان بسیار خوب است. تلاش می‌کنیم تا جایی که در چنین شرایطی ممکن است، ملایم باشیم، اما آن‌ها در حال نابودشدن هستند.
دیگر نیروی دریایی، نیروی هوایی یا پدافند هوایی ندارند. این به آن معنا نیست که هیچ توانی ندارند؛ مقداری دارند، اما بسیار اندک است.
فقط می‌خواهیم پیروز شویم. نمی‌خواهیم آن‌ها این توان را داشته باشند. موضوع بسیار ساده است.
آن‌ها نمی‌توانند سلاح هسته‌ای داشته باشند. ایران سلاح هسته‌ای نخواهد داشت و نمی‌تواند داشته باشد. اگر چنین سلاحی داشتند، خاورمیانه تا الان نابود شده بود.
اگر من برجام، همان توافق اوباما، را متوقف و لغو نکرده بودم، آن‌ها اکنون سلاح هسته‌ای داشتند.
فکر می‌کنم اسرائیل دیگر وجود نداشت؛ در بخش‌های بزرگی از خاورمیانه و شاید کشورهای دیگری در قاره‌های مختلف نیز، چون صادقانه بگویم این افراد دیوانه‌اند.
بنابراین نمی‌توانند سلاح هسته‌ای داشته باشند و نخواهند داشت.
🔺
خبرنگار:
[پرسش ناقص و نامفهوم درباره آنچه در چهار یا هشت هفته آینده باید انتظار داشت.]
🔻
ترامپ:
می‌دانید، به آن‌ها حمله خواهیم کرد؛ حملات بسیار سختی به آن‌ها وارد خواهیم کرد. بالاخره در مقطعی خواهند گفت: «دیگر نمی‌توانیم تحمل کنیم.»
🔺
خبرنگار:
آقای رئیس‌جمهور، بازگردیم به ایران. گزارشی منتشر شده که ارتش پیشنهادی داده است تا ظرف ۱۰ یا ۱۴ روز حمله‌ای بزرگ و سخت انجام دهید—
🔻
ترامپ:
ما همین حالا هم حمله بزرگ انجام داده‌ایم. منظورتان از «بزرگ» چیست؟
آن‌ها ۱۵۹ کشتی داشتند؛ تمام نیروی دریایی‌شان همین بود. هر ۱۵۹ کشتی، تمام نیروی دریایی‌شان، در کف دریا قرار دارد. من این را حمله بزرگ می‌نامم.
تسلیحات پدافند هوایی بسیار خوبی داشتند، اما کار نکرد و همه آن از بین رفته است. تمام رادارهایشان از بین رفته، رهبرانشان از بین رفته‌اند؛ همه‌چیز از بین رفته است.
🔻
ترامپ:
برای مثال، خواندید که پنج موشک شلیک شد. سرعتشان ۸۶۰۰ مایل در ساعت بود.
فکرش را بکنید؛ اگر با خودرو ۶۰ مایل در ساعت بروید، کمی سریع به نظر می‌رسد. این موشک‌ها ۸۶۰۰ مایل در ساعت سرعت داشتند و موشک‌های بزرگی بودند. به سوی اردن شلیک شدند و نیروهای ما آنجا بودند: بنگ، بنگ، بنگ، بنگ، بنگ.
[خنده حاضران]
این می‌توانست کلیپ صوتی خوبی باشد! پنج موشک شلیک شد و هر پنج موشک را پیش از آنکه نزدیک شوند، ساقط کردیم. هیچ کشور دیگری چنین توانی ندارد.
🔺
خبرنگار:
آقای رئیس‌جمهور، گفتید هنوز مقداری توان برایشان باقی مانده است. آیا آمریکایی‌ها باید آماده باشند که این حملات متقابل ادامه پیدا کند تا زمانی که ایران دیگر توان حمله فوری نداشته باشد؟
🔻
ترامپ:
ضعیف‌تر خواهند شد. شاید اکنون کمی قوی‌تر شوند، اما ضعیف‌تر خواهند شد.
🔺
خبرنگار:
و بعد به‌تدریج از نفس می‌افتند؟
🔻
ترامپ:
بله، فکر می‌کنم همین‌طور است. احمقانه است که بگویم نه. همیشه باید مراقب باشید.
🔺
خبرنگار:
وضعیت مذاکرات چگونه است؟ چه کسی از طرف دولت در مذاکرات حضور دارد؟
🔻
ترامپ:
آن‌ها همیشه می‌خواهند مذاکره کنند، اما بارها زیر قولشان می‌زنند. استیو در حال مذاکره است. جرد هم هست؛ افراد بسیار خوبی داریم. جی‌دی به‌شدت درگیر است. افراد فوق‌العاده‌ای در حال مذاکره هستند. مارکو هم درگیر است.
افراد بسیار خوبی داریم؛ بهترین‌ها را. اما آن‌ها توافق خواهند کرد.
برای مثال، درباره موضوع هسته‌ای صحبت می‌کنیم و هفت ساعت آنجا می‌نشینیم و درباره برنامه هسته‌ای حرف می‌زنیم. می‌گویم چرا هفت ساعت؟ ده دقیقه کافی است؛ پنج دقیقه وقت دارید، باید حلش کنید.
اما هفت ساعت صحبت می‌کنند، بعد بیرون می‌آیند و من می‌گویم درباره موضوع هسته‌ای گفت‌وگو کردند. آن‌ها بیرون می‌روند و می‌گویند: «ما هرگز درباره موضوع هسته‌ای صحبت نکردیم.»
می‌گویم چرا؟ چرا چنین چیزی می‌گویند؟ تنها کاری که می‌کنند این است که من را عصبانی می‌کنند.
🔺
خبرنگار:
با توجه به آنچه گفتید، باور دارید می‌توان با ایران به توافق رسید؟
🔻
ترامپ:
بله، می‌توان. ببینید، دارم اعتمادم را به آن‌ها از دست می‌دهم، چون دروغ می‌گویند و واقعیت را تحریف می‌کنند.
چند روز پیش پنج موشک شلیک شد. ما آن‌ها را ساقط کردیم، اما در میانه مذاکره بودیم. منتظر تماس استیو بودم تا ببینم مذاکرات چگونه پیش می‌رود؛ در عوض پیت تماس گرفت و گفت: «آن‌ها همین حالا پنج موشک به یکی از پایگاه‌های ما در اردن شلیک کردند.»
خوشبختانه نیروهای ما تجهیزات را به کار انداختند. کارکردن با این تجهیزات بسیار پیچیده است. از این افراد می‌پرسید کجا درس خوانده‌اند و پاسخ می‌دهند ام‌آی‌تی یا کلتک؛ دانشگاه‌هایی که معمولاً با نیروهای نظامی تداعی نمی‌شوند.
افرادی فوق‌العاده باهوش این تجهیزات را اداره می‌کنند. وقتی چنین افرادی نباشند، شلیک‌ها خطا می‌رود، سامانه ایمنی خطا می‌کند یا دقت کافی وجود ندارد. ما افراد فوق‌العاده‌ای داریم.
فکرش را بکنید؛ چند ماه پیش در یک بازه کوتاه ۱۱۱ موشک به سوی ناو هواپیمابر آبراهام لینکلن شلیک شد؛ ناوی بزرگ و زیبا و از نظر طراحی یکی از زیباترین کشتی‌ها.
هر ۱۱۱ موشک مدت‌ها پیش از رسیدن به ناو ساقط شدند. در چند مورد تقریباً همان لحظه‌ای که پرتاب شدند، سرنگون شدند. فناوری باورنکردنی‌ای است.
ناوی که میلیاردها دلار ارزش دارد و موشک‌ها به سوی آن در حرکت‌اند؛ هر ۱۱۱ موشک ساقط شدند. من با افرادی که این کار را انجام دادند صحبت کردم. دوست دارم به افراد پاداش بدهم؛ من رئیس‌جمهورم و با آن‌ها تماس می‌گیرم. آن‌ها کاملاً خونسرد بودند.
🔻
خبرنگار:
آقای رئیس‌جمهور، در دو هفته گذشته سنتکام حملاتی انجام داده است. سنتکام گفته هدف این حملات کاهش توان ایران برای مختل‌کردن تردد در تنگه هرمز بوده است. چند حمله دیگر لازم است تا این توان به‌طور چشمگیری کاهش یابد؟
🔺
ترامپ:
هیچ‌وقت نمی‌توان دانست. بیشتر مردم تا الان تسلیم شده بودند. آن‌ها دیگر نیروی دریایی یا نیروی هوایی ندارند. بیشتر مردم تسلیم می‌شدند، اما آن‌ها نشده‌اند. از این بابت به آن‌ها اعتبار می‌دهم. سرسخت هستند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 343K · <a href="https://t.me/VahidOnline/77678" target="_blank">📅 20:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77677">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ltv7ZH-y-AQj3GdFAY4bC64c_cYiW0xIv1El2XBxzE-4dg4FyJZ-WNewIbaqAp6Rs0m2sM5k_jkDGpFxdO44dyyeaRXMwexpwgLBHz97iADx0xAdGfJzt3oywxfpJ8ckfQAKzL9zU4lsMAiJJFzGdVPUwHbRkFTCTbYSRaonSqPm28MjtPXd3LQ6SogFQw-0M0EGnPb4wh6Vm2wN_QmcwmTMwY_uw6ZfhNYEqmCnMsSyVYW5GIUjnDeOBt8sa_c-uuRPdUiTG1cj7aRtpnhUljVijlyOaypXKHRxHjBEmIlGFoV6_1ogl9bZkOY4uL_27HE2o9m9cpWSZMfpWo-bpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
🚫
ادعا: دولت ایران بار دیگر مدعی شده است که تنگه هرمز را بسته است. این ادعا نادرست است.
✅
واقعیت: تنگه هرمز همچنان برای عبور کشتی‌های تجاری باز است. ایران کنترلی بر آن ندارد. طی چهار ماه گذشته، هزاران کشتی از این آبراه بین‌المللی عبور کرده‌اند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/77677" target="_blank">📅 19:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77676">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CIsCEQASLDwqojxtOwER9OmOOWdwpMg-mZDEk5iJ1sZXLbT6dlWzS4pAYaUSFdrWDA2sS5qckhJVlszPsSqzW6qxEAxV0RCUNNmOO7gqPL-baH04aY0WyHKevpvXFlRxsjkgIJijd1wopdZwFWgmyskUa9lejRasXMMHgHXOQzStiuRxWtHc0qfyJv7vO5pVw8plV9JtHv2mJr6bc0MwGM-4nlgdx21bcuoWIprq2csB96HGfE-XIEGL4IlLAzPKwvmvCZDqbBHZCizwFnf_hFJYuG832P0bvywOHMmV6RtaMkwkgi3Oiy4dUn9k3_tl-XG1bND0PC7-wiDo4PJlYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاول دوروف، بنیان‌گذار تلگرام، یک روز پس از آنکه اعلام کرد روسیه او را به دلیل مخالفت با درخواست‌های این کشور برای اعمال سانسور و نظارت گسترده بر کاربران، در فهرست «تروریست‌ها» قرار داده است، با انتشار تصویری از ملاقات مقام‌های طالبان با سرگئی لاوروف، وزیر خارجه روسیه، به این اقدام واکنش نشان داد.
دوروف در این تصویر که در شبکه اجتماعی ایکس به اشتراک گذاشت، عکس خود را با برچسب تروریست، کنار تصویری از دیدار مقام‌های روسیه با مقام‌های طالبان قرار داد و زیر عکس دوم نوشت: «شرکای مورداحترام» و برای عنوان این تصویر از عبارت «گیج نشوید» استفاده کرد.
دوروف پیش‌تر در ایکس خبر داده بود که روسیه به دلیل خودداری او از اجرای خواسته‌های این کشور برای نظارت گسترده و سانسور در تلگرام، نامش را در فهرست «تروریست‌ها» قرار داده است.
او همچنین به کنایه نوشت که بر اساس قوانین روسیه از «انتشار اطلاعات در اینترنت» منع شده است و افزود: «به نظر می‌رسد مقام‌های روسیه درباره اینکه چه کسی می‌تواند چه کسی را از اینترنت محروم کند، دچار سردرگمی شده‌اند.»
روسیه تنها کشور جهان است که رژیم طالبان را به رسمیت شناخته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/77676" target="_blank">📅 19:35 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77675">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b2mNr-DQtpUsKhPi8IwII-X7A5LOR4q_JjDmaB571GH0EgbE9hLZdpOdHUTKNFYtBbicNpuQJFs5A9Etl1dO9e4GycC2BJ2xHnaoS1VwjtDPAbTE0JDJK4ywOIk3pty-Jan1K9900QciuaFzB9pRaBJ-NTKL_lBjzBUyi_DVPQxCKLK-WPVCTtJ5oogvLgk5ev9KfO76O0Qyb5dJFvqL9hYt7iTWv7rwE7Gz9BfikvC6dmBlBpNljTtTqPpx9zse984cYrPJBF062TqlEZD8SD0EGfdBAwPgerMdQoKr-yS7VwO0UTvDhr5Jnyf3TgUSK8s4gKuI6KOc3uSIr2xPug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسن عاملی، امام جمعه اردبیل، در خطبه‌های نماز جمعه این شهر گفت: «نتانیاهو در دیدار با ترامپ گفته قدر مرا بدان، من جلوی موشکهای جمهوری اسلامی را گرفته‌ام. ایران موشک هشت هزار کیلومتری دارد و به راحتی می‌تواند خانه تو را با موشک بزند. من جلوی ایران را گرفته‌ام.»
او ادامه داد: «ترامپ همیشه از نتانیاهو گول خورده و حالا محل بحث است که آیا این بار هم گول خواهد خورد یا نه.»
امام جمعه اردبیل افزود: «ترامپ پهلوان رسانه‌ای است، عملیات ما کمر او را شکست. او هر وقت شکست می‌خورد به جنگ رسانه‌ای پناه می‌برد و خود را پیروز میدان نشان می‌دهد. اگر این کار را نکند دق می‌کند و می‌میرد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 300K · <a href="https://t.me/VahidOnline/77675" target="_blank">📅 19:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77674">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pe8gGgNhXe1dUOkj6j0DPe-POLOHv_1dvi2qCk_rqHC8EaX-oE8UgxanP0f4pkHIt6P0013eJxF4OhdPBU_u6uX8Rl65HYZjdYfT1xQbizQ1Qk6n66ztQNJJ4D0yo1oAgFNTWwleaxhiQzSMomUkf40xoJTIwjJL2v2cGl4MQSWXv6YnYHCHDsecHKAOVz_14O3kEjUMtXhaZc57DKN42JvO6q4_RN-M3SBFY_O91EY3YwxWLSk2QFajbxuvuAe_uaBBBMi58w2fIHfBr8tx471jrsIXy-82iOYSfzFRMJXa1n-2vnPeBqPoeMYMZz6BPcbPqG2avBP9yJQJA1AR8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رییس‌جمهور آمریکا، روز جمعه ۹مرداد۱۴۰۵ در گفتگو با شبکه «فاکس‌نیوز» گفت درگیری با ایران «به‌خوبی پیش می‌رود» و با اشاره به حملات ارتش ایالات متحده اعلام کرد که ایران در نهایت چاره ای جز عقب‌نشینی و تسلیم نخواهد داشت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 294K · <a href="https://t.me/VahidOnline/77674" target="_blank">📅 19:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77673">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PJoHy-ulePTFZrxRXUZ4SZi97A46pyj0L70dkleqmae8ZkCJj7XJEer-LnlLUdLrpI5zOQbsRFASFYI2uAww7RR8fjHK3iewPUqPxqdz6uyrW28WSbTdcUfEv1VCaU5tatPbgOXOeEepQ_3744ORfohh3Ev_pexO9ewTdVDSvdliI1TJKQe-ebn-ESUnFxzJ29qLp7I_JMhh_my6AUih8Ac3pLuKY2gJtsom-AfIHVyNLfpsCIF9Ko6TjAT_m1x9l2-aQTGD-5WPflVGlkZnMC2xP61Z0qpkeghWl8hzAO3QUKU9dIzGeDgQyPu5S4PP3VXWD-XEbVQW_7fa2zIa_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهوری آمریکا روز جاری و در میانه تشدید تنش‌های خاورمیانه، نشست کابینه خود را در اقامتگاه کمپ دیوید برگزار می‌کند.
این نشست در شرایطی برگزار می‌شود که دونالد ترامپ در تلاش است راهی برای پایان دادن به جنگ با ایران پیدا کند و همزمان قیمت بنزین را که به تهدیدی برای جمهوری‌خواهان در انتخابات میان‌دوره‌ای نوامبر تبدیل شده، کاهش دهد.
انتظار می‌رود سیاست خارجی و موضوع جمهوری اسلامی بخش عمده دستور کار این نشست را تشکیل دهد. ترامپ درگیر حملات متقابل علیه اهداف نظامی در ایران است.
ترامپ برخلاف برخی رؤسای جمهوری پیشین، در دوره ریاست‌جمهوری خود کمتر به این اقامتگاه کوهستانی ریاست‌جمهوری در غرب ایالت مریلند رفته، و این سومین سفر او به کمپ دیوید در دوره دوم ریاست‌جمهوری‌اش خواهد بود.
@
VahidHeadline
چون جمعه هم هست و بازارهای مالی تعطیل میشن باعث توجه بیشتر هم شده. دیشب، توییتر:
فردا ترامپ قبل از رفتن به باشگاه گلفش در بدمینستر، توقفی در کمپ دیوید داره. در هر دو باری که به کمپ دیوید رفته اتفاق خاصی افتاده. اولینش حمله بمب‌افکن‌های B-2 به نطنز بهمراه داشت، دومیش هم توافق با رژیم...
J74wabx
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/77673" target="_blank">📅 15:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77672">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/csUFr0p1KJFT17JGyCzv-jrO8k3oOhkIgfZBM0u5SdRn_Pi3C_4dg_tRqoXVs7rNB1AaPnUUbYjMynngp9sBuOCH14gIBLwGJx9bfIz4idDd1KFmx6bW6YqVdTIFR2IcA5isMS3zST02rdnUpKr8Q4jDVP9LLSDDYKwSTMbDWxA2riMw0kPOGvHncABGLbI8rhrn8PEzjm2bp38ZdpV81Jm3YT8RgSMzTRQzM0XkvZneQwt47Kbe4oNkjel0uXgwyveJn3ca3yxtn02ekMoWSPX56YmF_EVDBforS366uagKbRoeb0YLJuSirlzdCvMo1-PLMc4HWDgwNFFwdey8Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی رسمی وزارت دفاع کویت اعلام کرد نیروهای مسلح این کشور، بامداد روز جمعه نهم مرداد ماه، چند پهپاد متخاصم را در حریم هوایی کویت شناسایی کرده و آنها را منهدم کرده‌اند.
سعود عبدالعزیز العتیبی در بیانیه‌ای در شبکه اجتماعی ایکس نوشت: «تجاوز گناه‌آلود ایران تعدادی از تاسیسات حیاتی و نظامی را هدف قرار داد که اهداف متخاصم رهگیری و منهدم شدند.»
او افزود: «در نتیجه سقوط ترکش‌ها، خسارت‌های مادی وارد شد، اما هیچ تلفات انسانی ثبت نشده است.»
پیش از این بیانیه، ارتش جمهوری اسلامی با انتشار اطلاعیه‌ای از حمله به پایگاه احمد الجابر، محل استقرار ارتش آمریکا با «پهپادهای انهدامی» خبر داده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 308K · <a href="https://t.me/VahidOnline/77672" target="_blank">📅 14:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77671">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NiZFfAhv6nwR0OIc5dmRiqqy7Nnw_sDlTkXvg3C0s5drhAI8w_T2KGItEUqWdaB-6ZqoYYyGf3PuE8BPn_LxOyPLZGjQA7WNNfi635FHa5idf4QDelQzwhsO4xAObT1Ni_x2_ZG3axX82wdS80YsIuRmMCME8dO34zGPXWsXBogA9aQ_MVy6hj0iHgGXa1ckd2o76sd2rrkk-SrWWH2Xf_ycAQjirUtzMSDzFXwK8wKWg_VTZn-lizJNh2naZMKvF8WJb89sTbqIoikq0uNH553VnCaDY6PEvTe3dhG3eNGtEbafRSP8ayco8b9x1zc63t7JcnH3PtNTelVg7N-Ahw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه پاسداران انقلاب اسلامی، در پی اعلام فرماندهی مرکزی ارتش آمریکا مبنی بر تکذیب ادعای سپاه دربارهٔ بسته بودن تنگه هرمز، با انتشار بیانیه‌ای دیگر با پافشاری بر ادعاهای قبلی‌اش گفت به دو نفتکش دیگر حمله و آن‌ها را متوقف کرده است.
سپاه در کنار این بیانیه که روز جمعه نهم مرداد منتشر شد، همچنین تصاویری از یک نفتکش را که در میان شعله‌های آتش در تاریکی می‌سوزد منتشر و تاریخ آن را روز جمعه اعلام کرد.
سنتکام بعدازظهر پنج‌شنبه سه ادعای مطرح‌شده از سوی سپاه پاسداران و رسانه‌های نزدیک به آن دربارهٔ بسته بودن تنگه هرمز، انهدام سه جنگنده اف-۳۵ و عبور یک نفتکش ایرانی از محاصره دریایی آمریکا را را «نادرست» خوانده و گفته بود این ادعاها با واقعیت مطابقت ندارند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 299K · <a href="https://t.me/VahidOnline/77671" target="_blank">📅 14:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77670">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6f37e7edd3.mp4?token=TFXJVzmit6Pn00WxIn3VadZjbLVoDB50vMAN7r8bbgpEszqKDICkKxeROBS9Os3wejyCLSfDmXc678A7f-JOMasD9Yg882jDPJBWxLKCJMJcn0LMQ-75Tsqk7KJZBoRkpFcQvS7HaaECzIUia7Luda92UYXzQQThnfWwL78-EPwDn3rxJ_kqiJT3IjDKxM0GWLAWYIwedsunh2-oQTY8hND4pj4OATyNibouvK_HUQ4rPzSITBeyp4lyRa6I7KUuoNiWBX092sUAcfnIY9QYZCOwMA6-l5MPc90kLGYRPddsl8dPxQtk7j687gepb698UPyQVtQvAniPVKRJ8wbXYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6f37e7edd3.mp4?token=TFXJVzmit6Pn00WxIn3VadZjbLVoDB50vMAN7r8bbgpEszqKDICkKxeROBS9Os3wejyCLSfDmXc678A7f-JOMasD9Yg882jDPJBWxLKCJMJcn0LMQ-75Tsqk7KJZBoRkpFcQvS7HaaECzIUia7Luda92UYXzQQThnfWwL78-EPwDn3rxJ_kqiJT3IjDKxM0GWLAWYIwedsunh2-oQTY8hND4pj4OATyNibouvK_HUQ4rPzSITBeyp4lyRa6I7KUuoNiWBX092sUAcfnIY9QYZCOwMA6-l5MPc90kLGYRPddsl8dPxQtk7j687gepb698UPyQVtQvAniPVKRJ8wbXYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیش‌تر در صبح جمعه:
ارتش جمهوری اسلامی ایران مدعی شده است بامداد جمعه ۹ مرداد، پایگاه هوایی احمدالجابر در کویت را با پهپادهای انهدامی هدف قرار داده است.
روابط عمومی ارتش در بیانیه‌ای اعلام کرد در این حمله، آشیانه جنگنده‌ها، سامانه‌های ارتباطات ماهواره‌ای و انبارهای تجهیزات ارتش آمریکا در این پایگاه هدف قرار گرفته‌اند. این ادعا تاکنون از سوی فرماندهی مرکزی آمریکا، سنتکام، یا مقام‌های کویتی تایید نشده است.
احمدالجابر یکی از پایگاه‌های مورد استفاده ارتش آمریکا در کویت است و در گذشته نیز ارتش جمهوری اسلامی بارها از حمله پهپادی به مواضع آمریکا در این کشور خبر داده است. در یکی از حملات پیشین، ارتش جمهوری اسلامی مدعی شده بود ساختمان‌های اداری و سامانه‌های جهت‌یاب در پایگاه عریفجان، محل استقرار بالگردها در اردوگاه العدیری و ساختمان استقرار نیروهای آمریکایی در احمدالجابر را هدف قرار داده است.
ارتش جمهوری اسلامی حمله ادعایی بامداد جمعه را واکنشی به حملات اخیر آمریکا به ایران توصیف کرده است. رسانه‌های ایران پیشتر از حمله آمریکا به بخش‌هایی از جزیره قشم و کشته شدن شماری از غیرنظامیان در این حملات خبر داده بودند.
با این حال، تا زمان انتشار این گزارش، مقام‌های آمریکایی و کویتی درباره وقوع حمله یا میزان خسارت احتمالی آن اظهار نظر رسمی نکرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 294K · <a href="https://t.me/VahidOnline/77670" target="_blank">📅 14:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77663">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ICo9VMKlJGMtW2bW5Uy8xIut5B5BVw_yqqManwKOBTFLZ5lGeuRnCyC_VxfjtxgrWtbxF5hRNXi7U9ui0Wu6s1Sz_-qX0tzbU4R2oVmedViNc_8irSYFH8wRhS_Ocd3-mCfAX4fFcIoTs_gXh6IWydXQAR5k0qkbb4XHkrkF_JYsKs-xv_uk9IxNSOs10ag8ONajg5jr5Hatbcl7abIhKfGxoICVK5UBR6AHK_4ALT_9Qhu9tfKbDwfQq76kFlfa2NcshwUhoI6zLBTDUtu49D8qiu_I9SBZIWGrHV1bPVQmZhI80r_0FCi3pdYaSX5zkznN6iAKcEz2toCAa_bjQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qCiXJAAoA0WT78a2sb3T3CYYOus2F4FH_U0d9dMDIxYhVIeuJEBnZbcc3nRBHlYFpTJKs0lzofVESXyK0wA2j8Wh4-UdCReO9mlZHZR4B7jVTH--rP_PR8oWsXJR3mpyhug1eg9p3dH4P5G4nhOQTDfe3X6W4uWQa0zT1flLe2Bp6X_ba1UzHdhSN7zENOU4nbflfRFAu1rgigwGWjwEbTD5qjlxX_j2PshOEErhlsDjqYVNcl2BXqBZUXH8troBIhHRV7vdg4vW1sqPEKrx82GbyP5p3CdR0nrjnVxydX2u06ell9UShvcZ721IyjgJYKFnAIXsFcE3hBdyurjV6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tiMOv4L4DUuVeWhWysR6jWSY_JOAtsGlgahX_35AVdZ1rYYNAHyY7FvMsQz7RERAaqiNokH8hWBd-RPwO7auV1g5B0iQpGRa33dnuYNu5DyBuwCd7UhLyd00gAiE8gdyQQn-skgvNZv6hM0TGW6I6rFmiu2hQZ2XT_qDneHEXE2ViHlsN5NrH3Sp2L7_Z3CU4IcUYxlxO-FU2J6ALUgD3jNVvasozhxD7BJGFi9NlAhdc779ze_AEZ6sgcmezcD9DaoUZJjhLvbN6CRZf9YEKMDtcmjNAUGHfoHm16iNi2M5p6PSoYHVYVivrwkiNje3fcfRFP3CWGu0Cmecb2I9og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AOAw4k5HrHlqrNZOjPj9sDbbDJTuYXeVX9J5wixLT7hd7mqzGsOranltwG8KPP1Pf8t-XZ7Acc2voM0hUqj6s3DCxEPCIeEqTJDeyVewjz8-RdTqmHkcgytwadD_QA6tH_slaIKx_XIUdM13K45oigr2XWDKdSgYGApvcTW1riLGfQVdCZ6VLjShbhYRQqUcBFbZmIHoAYCEeWT1tcC_hmhmQw9Lku3fv9j5NLyWWk3ahgkaRt-6Ni3UN_hegz1zqyiqJ7WVIvx5lX9xvqorG4Z5cjegDEUGSzpT9fSiRdz1FT8lRM8LGmWy6LgIsAwTYqVkGJBmewA_s5yrQFAGNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SGz-M2FzI_7yVmHIL-JAAzDzKNQA2GDSYay5SRFHjhAp4p8U3GDAMC9CTEVB-u13wz13Vfv9zM4fvX-UOrlAwiYKwYBSuwdr3W2aNiqiz4e5-EeRfa36QUgZfx-PU_PE3D5SgFFuSjM4ZHuqtNdcfm_qkUYGGCPyZOh-S5rlzKda-7OBc9uBgDkdl_ISFqagBqmFG8AW4-iosvXIWuZad4nBZtZC8e6GlP1Ei5DfHC3lr7LP6_KRelGDSWkSiK2GX62SWiV-jnJZiksrzpRhVLUjSZhrGP87h89X-UQ3WuKVUqkOUQnfMCmlhjUSH3jRVRQZOcdduXCoBcrvsgCxwQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/36c757e90b.mp4?token=BIrEq3W2NqunWH96GWSy_hmk00qXoEAUwx9j8Durw6UfAGIzKYfmVPSrRL1oNUdpxbMWUPp80RBAsGRNlLqybE5IV6PJvrsmd5HDT1DIPCzZG6gTElRMcmyryKd_6vzPMt1BAkluKHaXiKmQDiRa3C7l8NNM0jOYKCNdPQtwxQDjaaZ6Euwn83XomxphD34Zex6Cf5VKN2_asymjtjpyLqA_Aot0vDRlf65UNN9eB3eVaskeDBf4HpMqNeCQlssDSoKGefQ4fddJ_ywYZG0hUtvGmTsmjFUv5WEi2nK7Ooik-bxUsFPWT-9s9HIwFI-mJP03oBkzftvw4MOBI5Yy9w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/36c757e90b.mp4?token=BIrEq3W2NqunWH96GWSy_hmk00qXoEAUwx9j8Durw6UfAGIzKYfmVPSrRL1oNUdpxbMWUPp80RBAsGRNlLqybE5IV6PJvrsmd5HDT1DIPCzZG6gTElRMcmyryKd_6vzPMt1BAkluKHaXiKmQDiRa3C7l8NNM0jOYKCNdPQtwxQDjaaZ6Euwn83XomxphD34Zex6Cf5VKN2_asymjtjpyLqA_Aot0vDRlf65UNN9eB3eVaskeDBf4HpMqNeCQlssDSoKGefQ4fddJ_ywYZG0hUtvGmTsmjFUv5WEi2nK7Ooik-bxUsFPWT-9s9HIwFI-mJP03oBkzftvw4MOBI5Yy9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی ساعت ۱۰:۳۷ درباره پرتاب موشک از یزد
همین الان از یزد موشک فرستادن ساعت10:37
۱۰:۳۵ پرتاب موشک از یزد
سلام الان موشک زدن از یزد
از یزد موشک بلند شد ۱۰:۳۷
از یزد موشک زدن الان
وحید جان همین الان ساعت ۱۰.۳۲ پرتاب موشک از یزد
وحید جان همین الان از یزد موشک زدن
جمعه ساعت ۱۰:۳۶
یزد ۱۰:۳۵ یه موشک زدن
بعد از مدت ها جالب بود سمت جنوب پرتاب شد
همین الان از یزد موشک شلیک کردن
۱۰:۳۷از یزد موشک زدن
همین الان از یزد موشک زدن
جمعه نهم امرداد ساعت۱۰/۳۰
سلام وحید جان همین الان از یزد موشک پرتاب شد
سلام خوبین الان موشک از یزد رفت
شلیک  یک موشک الان از یزد
وحید الان موشک از کشور یزد زدن
همین الان ساعت ۱۰.۳۶ دقیقه از یزد موشک زدن
شلیک موشک از یزد به سمت جنوب
ساعت ۱۰.۳۶
سلام ساعت ۱۰:۳۵ یک موشک از یزد بطرف جنوب کشور شلیک شد
از یزد موشک شلیک کردن ولی مسیر متفاوت از قبل بود
سمت بندر و جنوب میرفت
ساعت ۱۰:۴۰ صبح یزد  موشک پرتاب شد؛ صداش خیلی بلند بود
سلام جمعه ساعت ۱۰:۴۰ از یزد موشک پرتاب شد
۱۰:۳۷ از یزد موشک زدن جمعه ۹مرداد
سلام آقا وحید ۱۰:۴۲ از یزد موشک شلیک کردن
موشک از یزد زدند
وحید جان شلیک موشک از یزد
چند دقیقه پیش
ساعت ۱۰:۳۵ از یزد موشک زدن
از یزد همین الان موشک زدن
امروز جهتش سمت جنوب شرق بود
بر عکس روزای قبل که روی شهر رد میشد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/77663" target="_blank">📅 14:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77662">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">اکسیوس:
ترجمه ماشین:
ترامپ از توافق «تاریخی» برای خلع سلاح حماس و بازسازی غزه تمجید کرد
دونالد ترامپ، رئیس‌جمهوری آمریکا، روز پنج‌شنبه اعلام کرد که «هیئت صلح» او با حماس به توافقی دست یافته است که بر اساس آن، این گروه خلع سلاح می‌شود و کنترل امور غیرنظامی و امنیتی غزه به یک دولت جدید فلسطینی متشکل از تکنوکرات‌ها واگذار خواهد شد.
چرا اهمیت دارد:
در صورت اجرا، این توافق تحولی چشمگیر در طرح صلح ۲۰ ماده‌ای ترامپ برای غزه خواهد بود و مسیر بازسازی این منطقه ویران‌شده را هموار خواهد کرد.
▪️
اما این توافق مستلزم آن است که حماس و اسرائیل طی حدود هفت تا هشت ماه، مجموعه‌ای پیچیده از اقدامات متقابل و مستقل را که اجرای آن‌ها راستی‌آزمایی خواهد شد، به انجام برسانند.
▪️
مقام‌های اسرائیلی همچنان به‌شدت تردید دارند که حماس سلاح‌های خود را تحویل دهد؛ در همین حال، اظهارات یک مقام ارشد حماس نشان می‌دهد که ترتیب خلع سلاح و عقب‌نشینی اسرائیل همچنان ممکن است محل اختلاف باشد.
آنچه می‌گویند:
ترامپ عصر پنج‌شنبه در شبکه تروث سوشال نوشت: «امروز، هیئت صلح به توافقی تاریخی برای خلع سلاح کامل حماس و تمامی گروه‌های مسلح دیگر در غزه دست یافت.»
▪️
او افزود: «این گامی عظیم به‌سوی صلح و امنیت پایدار است.»
وضعیت کنونی:
دو مقام آمریکایی گفتند حماس پس از چند ماه مذاکره با میانجی‌گری قطر، ترکیه و مصر که یک مقام ارشد دولت آمریکا آن را «بسیار حساس» توصیف کرد، با مفاد توافق موافقت کرده است.
▪️
این مقام ارشد آمریکایی گفت انتظار می‌رود اجرای توافق طی هفته‌های آینده آغاز شود.
▪️
یکی از مقام‌های هیئت صلح گفت این نخستین بار است که حماس و دیگر گروه‌های فلسطینی در غزه با غیرنظامی‌کردن این منطقه و واگذاری مسئولیت امنیت و خدمات غیرنظامی به یک دولت تکنوکرات موافقت کرده‌اند.
بر اساس این توافق،
حماس از هرگونه نقش در اداره غزه صرف‌نظر خواهد کرد. «کمیته ملی اداره غزه» موسوم به NCAG به‌عنوان جایگزینی برای حماس و تشکیلات خودگردان فلسطینی فعالیت خواهد کرد.
▪️
مقام ارشد آمریکایی گفت: «این ساختار به نفع مردم غزه خواهد بود.»
بررسی واقعیت:
غازی حمد، از مقام‌های حماس، در گفت‌وگو با الجزیره تأیید کرد که مذاکرات «دشوار» به توافق منجر شده است، اما توضیحات او بلافاصله پرسش‌هایی را درباره نحوه اجرای آن مطرح کرد.
▪️
حمد گفت: «ما پیش از عقب‌نشینی اسرائیل از نوار غزه هیچ اقدامی در زمینه خلع سلاح انجام نخواهیم داد.» او افزود که کمیته ملی اداره غزه بدون دخالت اسرائیل خلع سلاح را اجرا خواهد کرد.
▪️
این موضع ظاهراً با توصیف ترامپ از یک روند مرحله‌ای و «با ساختاری دقیق» تفاوت دارد؛ روندی که در آن، هم‌زمان با تکمیل خلع سلاح، نیروهای اسرائیلی عقب‌نشینی می‌کنند.
▪️
مقام‌های آمریکایی و هیئت صلح گفتند اجرای توافق از طریق اقدامات متقابل و مستقلی که راستی‌آزمایی می‌شوند پیش خواهد رفت، هرچند اذعان کردند که جدول زمانی عقب‌نشینی اسرائیل هنوز در حال نهایی‌شدن است.
تصویر کلی:
بخش‌های وسیعی از غزه در جریان جنگ ویران شده و بیشتر جمعیت دو میلیون نفری آن همچنان در چادرها یا سرپناه‌های موقت زندگی می‌کنند.
▪️
مواد غذایی و دیگر کمک‌ها در حجم زیادی وارد غزه می‌شود، اما وضعیت انسانی همچنان وخیم است.
▪️
وزارت بهداشت غزه که تحت کنترل حماس است می‌گوید از زمان آتش‌بس ۱۰ اکتبر ۲۰۲۵، نزدیک به ۱۲۰۰ فلسطینی کشته شده‌اند. برخی از آن‌ها از نیروهای حماس بودند، اما بسیاری دیگر غیرنظامی، از جمله کودکان، بوده‌اند.
نگاهی نزدیک‌تر:
این توافق بر این اصل استوار است که غزه باید یک دولت، یک نظام حقوقی و یک مرجع امنیتی مشروع داشته باشد. انتظار می‌رود روند غیرنظامی‌سازی بین ۲۰۰ تا ۲۵۰ روز طول بکشد و هر بار در یکی از بخش‌های غزه اجرا شود.
▪️
پلیس غیرنظامی حماس ابتدا سلاح‌های خود را به یک نیروی پلیس جدید فلسطینی زیر نظر دولت تکنوکرات تحویل خواهد داد.
▪️
پس از آن، سلاح‌های سنگین حماس از رده خارج و در انبارهای امن نگهداری خواهد شد و تونل‌ها و کارخانه‌های تولید سلاح این گروه برچیده خواهد شد.
▪️
سلاح‌های سبک مطابق قوانین فلسطینی جمع‌آوری خواهد شد.
▪️
تمامی گروه‌های شبه‌نظامی دیگر در غزه، از جمله گروه‌های مخالف حماس که اسرائیل در جریان جنگ آن‌ها را مسلح کرده بود، نیز ملزم به تحویل سلاح‌های خود خواهند بود.
کمیته ملی اداره غزه
تنها زمانی کنترل هر منطقه را در دست خواهد گرفت که یک سازوکار نظارتی تأیید کند تعهدات مربوط به آن منطقه اجرا شده است.
▪️
مقام هیئت صلح گفت در پایان این روند، دولت تکنوکرات و نیروی پلیس آن انحصار سلاح در غزه را در اختیار خواهند داشت.
نحوه اجرا:
بر اساس توافق، یک نیروی بین‌المللی تثبیت‌کننده به آموزش پلیس جدید فلسطینی کمک خواهد کرد، در جمع‌آوری سلاح‌ها مشارکت خواهد داشت و میان مناطق تحت کنترل فلسطینی‌ها و نیروهای اسرائیلی مستقر خواهد شد.
▪️
یکی از مقام‌های هیئت صلح گفت این توافق بر مبنای «اعتماد صفر» طراحی شده است، زیرا حماس و اسرائیل از همان ابتدا به‌صراحت اعلام کردند که به یکدیگر اعتماد ندارند.
▪️
این روند تا زمانی که ناظران تأیید نکنند هر دو طرف به تعهدات خود عمل کرده‌اند، از یک مرحله به مرحله بعدی منتقل نخواهد شد.
▪️
این مقام گفت هدف آن است که از وضعیتی جلوگیری شود که دولت تکنوکرات در طول روز غزه را کنترل کند، اما گروه‌های مسلح شب‌ها همچنان قدرت را در دست داشته باشند.
طرف مقابل:
عقب‌نشینی اسرائیل به‌تدریج و بر اساس جدول زمانی‌ای انجام خواهد شد که هنوز در حال نهایی‌شدن است.
▪️
ترامپ گفت هم‌زمان با تکمیل خلع سلاح و برعهده‌گرفتن مسئولیت امنیت از سوی نیروی بین‌المللی و پلیس جدید فلسطینی، نیروهای اسرائیلی عقب‌نشینی خواهند کرد.
▪️
اسرائیل همچنین عملیات نظامی و ترورهای هدفمند در غزه را متوقف خواهد کرد، مگر در مواردی که تهدیدی قریب‌الوقوع وجود داشته باشد.
▪️
مقام هیئت صلح گفت: «تمامی فعالیت‌های نظامی در غزه باید متوقف شود؛ چه از سوی اسرائیل و چه از سوی حماس.»
پشت درهای بسته:
مقام ارشد آمریکایی گفت دولت ترامپ در تمام طول مذاکرات هماهنگی نزدیکی با اسرائیل داشته است.
▪️
دولت آمریکا همچنین قصد دارد با وجود تردید اسرائیل درباره خلع سلاح حماس، اطمینان حاصل کند که اسرائیل به تعهدات خود در چارچوب توافق عمل می‌کند.
▪️
این مقام گفت: «ما از اسرائیل چیزی جز اجرای تعهداتش در چارچوب طرح ۲۰ ماده‌ای نمی‌خواهیم.»
▪️
او افزود: «اگر آن‌ها این کار را انجام ندهند، رئیس‌جمهور ترامپ بسیار ناامید خواهد شد. فکر نمی‌کنم اسرائیلی‌ها در شرایط کنونی بخواهند تنش‌ها با ما را تشدید کنند.»
در پشت صحنه:
به گفته دو منبع آگاه از مذاکرات، مصر، قطر و ترکیه فشار شدیدی بر حماس وارد کردند تا این توافق را بپذیرد.
▪️
مقام‌های آمریکایی و دیگر افراد آگاه از مذاکرات گفتند حسن رشاد، رئیس دستگاه اطلاعاتی مصر، نقشی کلیدی داشت. او میزبان مذاکرات بود و رابطه نزدیکی با خلیل الحیه، رهبر سیاسی حماس، دارد.
نکته قابل‌توجه:
به گفته یک منبع آگاه از این دیدار، هیئتی از حماس در جریان سفر اخیر خود به ایران برای شرکت در مراسم تشییع علی خامنه‌ای، رهبر پیشین جمهوری اسلامی، با مقام‌های ارشد سپاه پاسداران انقلاب اسلامی دیدار کرد.
▪️
این منبع گفت مقام‌های سپاه از حماس خواستند برای امضای توافق عجله نکند و با وقت‌کشی زمان بخرد.
▪️
یک مقام ارشد آمریکایی نیز مدعی شد ایران تلاش کرده است حماس را متقاعد کند که توافق را امضا نکند، اما گفت این گروه تصمیم گرفت به توصیه ایران گوش ندهد.
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 408K · <a href="https://t.me/VahidOnline/77662" target="_blank">📅 06:18 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77661">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dVfZ-1i4wdvPwQ3BVCpadq1-UlmyAhw_JoYiwumG7DTbvsHdY_u4qsLNULeMipi7rhrJb9s4i1uM-I9zGb8V53AKQVFKmX7cwLmYuBxd-FXPHR-GzFaE6ZoVWpTyaUV42qN3V8Yb-6aXLIJqzDnWPMI9NBxgivp-cXsL6QQJWBjeDn8J6p7eQzbyn6pqAUebwyzVhUyqIxwXlvmUrhIjlG9cQfJCcmi1jRymzFQhPc5EMxd4W8J4IVZ4bHwKrA_N7l7HNDzOa8zqv17u68DMVyTzHW9Z_XVVkHBXTJLgrp-_Mo9U7cRm-BLvJb2-oyXduEHAVfPMzvOgiR_61y_a_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ ترجمه ماشین:
امروز، «هیئت صلح» به توافقی تاریخی برای خلع سلاح کامل حماس و همه گروه‌های مسلح دیگر در غزه دست یافت. این گامی عظیم به‌سوی صلح و امنیت پایدار است.
این توافق، گامی حیاتی در مسیر آن است که غزه سرانجام تحت اداره یک دولت جدید فلسطینی قرار گیرد؛ دولتی که برای کمک به مردم فلسطین، از نزدیک با هیئت صلح همکاری خواهد کرد. هم‌زمان، اسرائیل نیز از امنیتی که شایسته آن است برخوردار خواهد شد و غزه دیگر به‌عنوان پایگاهی برای حملات تروریستی مورد استفاده قرار نخواهد گرفت.
این توافق، نقطه عطف بزرگی در اجرای طرح ۲۰ ماده‌ای ترامپ است. این توافق در مراحلی که با دقت طراحی شده‌اند اجرا خواهد شد. هم‌زمان با تکمیل خلع سلاح، نیروهای اسرائیلی عقب‌نشینی خواهند کرد و «نیروی بین‌المللی ثبات» با یک نیروی پلیس جدید فلسطینی همکاری خواهد کرد تا مسئولیت تأمین امنیت غزه برای ساکنان آن و همسایگانش را بر عهده بگیرد.
یک سال پیش، جنگی خشونت‌بار و مهارنشدنی، بحرانی انسانی و گروگان‌هایی در اسارت وحشیانه وجود داشت. ما پیشرفتی تاریخی کرده‌ایم و هنوز کارهای زیادی باقی مانده است.
می‌خواهم از میانجی‌ها—مصر، قطر و ترکیه—به‌خاطر تلاش‌های مهمشان تشکر کنم، و به‌ویژه از تیم فوق‌العاده‌ام که تلاش خستگی‌ناپذیرشان این دستاورد تاریخی را ممکن کرد.
تهدیدی که در ۷ اکتبر از غزه سر برآورد، اجازه نخواهد یافت دوباره شکل بگیرد!
بر اساس این توافق، غزه سرانجام در اختیار یک دولت جدید فلسطینی قرار خواهد گرفت که به مردم خود خدمت می‌کند.
این تحول شگفت‌انگیز را که همه می‌گفتند هرگز دست‌یافتنی نیست، به همگان تبریک می‌گویم!
دونالد جی. ترامپ
رئیس‌جمهور ایالات متحده آمریکا
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 412K · <a href="https://t.me/VahidOnline/77661" target="_blank">📅 02:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77660">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lrZc2ygur29p024k4yRnX9LjygbZkOl1lDMCpev8ZBtNmHArfQPMPdJmTp6-HNbbdrLbyBtDz1OB9EsMi01ykTafNVQDJ4IEV_I6GSjA4nwYpzaiWKFElMzpTmmKH6ldEgftsrHCclyLCWi7uc_i-BU2z8aTABXW1_chGNpqyW_Cy0RAcvsQ-9BsJLRU0bTeF3jl85xuxNhT4vPyDCYzLEMULhmC1DVg-THDWlDI9ntdmork_BwpaK7TCovvS0bhwIYAoE3qEotCnvSiiPd5-rrMbJyw2ZDcTtDCJiMISIkPBAd5WZCAzle9Kfb8a9viVq2xC0GgIV7CL3ZXY1QyqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، با انتشار پیامی در شبکه اجتماعی اکس اعلام کرد افرادی که به سپاه پاسداران انقلاب اسلامی یا هواپیمایی ماهان خدمات مالی، پشتیبانی لجستیکی یا حمایت تجاری ارائه می‌کنند، به تداوم فعالیت یک سازمان تروریستی کمک می‌کنند.
او افزود وزارت خزانه‌داری آمریکا به شناسایی این افراد، افشای هویت آن‌ها و قطع دسترسی‌شان به نظام مالی ایالات متحده ادامه خواهد داد.
پیش از این، وزارت خزانه‌داری آمریک، شش فرد و نهاد در ایران، چین، هند و روسیه را به دلیل همکاری با هواپیمایی ماهان و سپاه پاسداران تحریم کرده بود. واشنگتن اعلام کرده بود برخی از شرکت‌های تحریم‌شده به‌عنوان نمایندگان فروش هواپیمایی ماهان فعالیت می‌کردند و در حفظ شبکه بین‌المللی این شرکت نقش داشتند. وزارت خزانه‌داری آمریکا همچنین شرکت «استودیوی استارت‌آپ داده‌نگار» را به اتهام همکاری با سپاه پاسداران تحریم کرده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 407K · <a href="https://t.me/VahidOnline/77660" target="_blank">📅 02:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77659">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">پست عراقچی، ترجمه ماشین:
مصر دوست و شریکی مهم برای ما در منطقه است و امنیت آن برای ما از بالاترین اهمیت برخوردار است.
همه ما باید در برابر توطئه‌های اسرائیل و عملیات‌های پرچم دروغین که برای تضعیف صلح منطقه‌ای طراحی شده‌اند، هوشیار باشیم.
تهدید روشن و مشترک است و از همبستگی مسلمانان هراس دارد.
araghchi
پست قالیباف:
ایالات متحده هر روز دست خود را به جنایت جدیدی آلوده می‌کند؛ حملهٔ تروریستی به منازل مسکونی غیرنظامیان در جزیرهٔ قشم، ادامهٔ جنایات در میناب و لامرد است.
امریکایی‌ها عادت کرده‌اند که سیلی‌هایی را که در میدان نبرد می‌خورند با ریختن خون بی‌گناهان جبران کنند. تاوان‌ خواهند داد.
mb_ghalibaf
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 420K · <a href="https://t.me/VahidOnline/77659" target="_blank">📅 23:41 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77658">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dKcSdSFs9Dtpu0x9PsYOAAeQzKc1dE7kfi2Pli5RKyAKmnP2gficaU8lGH1a-Tfggie7-7LpflA9RKFHmXGnrBbQkPFoSjUZXiZU8S7liBnk4b5FkhyaA7tA-gPmE9L0XbolqcLqpc4vQpuDGKonRUG3h4qV0C08Thaaap7-Wu6ZORMoebBIdnSM5b3rw_NP9U-ITbD-rNKiks_PBJsjLFg_a4OjOODFbWS8TKr_bpXbunJXlcYDFOKzoOpR_PBiZ74rguvP-hdr7WINN5XZgUTNDki87wLQdv-oyJb2o4LK8YxLgdJPIa2hI2VA2jzYbIpkmbcRx2uJOqGK558KZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عربستان سعودی روز پنج‌شنبه از طرح تشکیل یک ائتلاف بین‌المللی برای دفاع دریایی با هدف حفاظت از کشتیرانی و مسیرهای انتقال انرژی در دریای سرخ خبر داد.
وزارت دفاع عربستان اعلام کرد نمایندگان ۴۳ کشور و اتحادیه اروپا در نشستی درباره این طرح شرکت کردند. بر اساس این پیشنهاد، عربستان به‌عنوان کشور بنیان‌گذار و رهبر ائتلاف عمل خواهد کرد و مقر آن نیز در این کشور خواهد بود.
به گفته وزارت دفاع عربستان، این ائتلاف با هدف تقویت امنیت دریایی، حفظ آزادی کشتیرانی، تأمین امنیت مسیرهای تجارت و انتقال انرژی و حفاظت از منافع مشترک دریایی در تنگه باب‌المندب و خلیج عدن تشکیل می‌شود.
این طرح پس از آن مطرح شده که حملات حوثی‌های مورد حمایت ایران به کشتی‌ها، یکی از مهم‌ترین مسیرهای تجاری جهان را با اختلال روبه‌رو کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 431K · <a href="https://t.me/VahidOnline/77658" target="_blank">📅 22:24 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77657">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b839da73e3.mp4?token=updvH8Zk9kjA6UwQrcJIxRU7dgiTHWrzwpDgMYL_D6cNVe4sAFspbwVHPywMxYmRhbfOpcudtoWHsvv_mZnZSp6TqCOdnaLSKKuF7OUH397C9zg6H1MWjgzZUZ6DN8z_KMSe3EEdDjJy0po7R_W2JID-kGUTwcXCVZSH6OSiYyPlkgApLMVK6TGCtEmnchFNrkawpVfC0cQyzmbzq6imq5A5stnW6tiA7d18iO3C78xhptA6hhSTj_oqbWwrsoD1D7U_o1jAkzCzVZ7S1GGwuVQ166iAocgiIyggmTS5-GuV0XxiJTdjgHGehychSNkAYgz5SyTZwCRzvb8n010Z3g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b839da73e3.mp4?token=updvH8Zk9kjA6UwQrcJIxRU7dgiTHWrzwpDgMYL_D6cNVe4sAFspbwVHPywMxYmRhbfOpcudtoWHsvv_mZnZSp6TqCOdnaLSKKuF7OUH397C9zg6H1MWjgzZUZ6DN8z_KMSe3EEdDjJy0po7R_W2JID-kGUTwcXCVZSH6OSiYyPlkgApLMVK6TGCtEmnchFNrkawpVfC0cQyzmbzq6imq5A5stnW6tiA7d18iO3C78xhptA6hhSTj_oqbWwrsoD1D7U_o1jAkzCzVZ7S1GGwuVQ166iAocgiIyggmTS5-GuV0XxiJTdjgHGehychSNkAYgz5SyTZwCRzvb8n010Z3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مادر جاویدنام آیدا حیدری، جوان معترض کشته‌شده به دست حکومت، در سالروز تولدش بر مزار او می‌گوید که آیدا حیدری «شیرزنی» بود که جانفدای میهن شد.
آیدا حیدری، دانشجوی رشته پزشکی دانشگاه علوم پزشکی تهران، در ۱۸ دی‌ماه ۱۴۰۴ در تهران با شلیک گلوله جان باخت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 417K · <a href="https://t.me/VahidOnline/77657" target="_blank">📅 20:48 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77656">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9d7d99f314.mp4?token=TlESrJhQUVSYL2SsK-QYndHEVNn9gdo2hFwYIUFsIQsLKP81EFi-1pYYLnnChPFbL24s2-lXF561PFebNlq3kDUhBzu2SOldP6GbjsEdimqMzVHzu1yLv_vOnfdwmM0REL_DFAoxA7Z5GAQJXqYPDP6JNEJbggTk8QhRlGYkvRhszL2rHKEJncO14ZAKWKrAs8TwEsrSby3Ixq4VjUV-WFMSUQQnBYu7gcj2O1THXAHmPQUz0XtxWUNZC0ePmabXhviWld494Pn-wXU_zbdrJK_Z77BX-4KlxMS63tOeKzqXFUadOQVlfcqImX21eqihPAEU5ZbqWyTWMg6O9iQy2A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9d7d99f314.mp4?token=TlESrJhQUVSYL2SsK-QYndHEVNn9gdo2hFwYIUFsIQsLKP81EFi-1pYYLnnChPFbL24s2-lXF561PFebNlq3kDUhBzu2SOldP6GbjsEdimqMzVHzu1yLv_vOnfdwmM0REL_DFAoxA7Z5GAQJXqYPDP6JNEJbggTk8QhRlGYkvRhszL2rHKEJncO14ZAKWKrAs8TwEsrSby3Ixq4VjUV-WFMSUQQnBYu7gcj2O1THXAHmPQUz0XtxWUNZC0ePmabXhviWld494Pn-wXU_zbdrJK_Z77BX-4KlxMS63tOeKzqXFUadOQVlfcqImX21eqihPAEU5ZbqWyTWMg6O9iQy2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
در چند ساعت گذشته، رسانه‌های دولتی ایران همچنان ادعاهای دروغین سپاه پاسداران انقلاب اسلامی را منتشر کرده‌اند؛ به‌ویژه سه ادعای زیر:
🚫
ادعای نخست: سپاه پاسداران بار دیگر ادعا می‌کند که مسیرهای آزاد و باز عبور از تنگه هرمز برای کشتی‌های تجاری خطرناک است.
✅
واقعیت: خطرهای فوری برای کشتی‌های تجاری و خدمه غیرنظامی آن‌ها، تهدیدهای لفظی و تلاش‌های سپاه پاسداران برای حمله به آن‌هاست.
🚫
ادعای دوم: سپاه پاسداران مدعی است سه جنگنده رادارگریز اف-۳۵ آمریکا و سه هواپیمای دیگر در جریان حمله اخیر ایران به یک پایگاه هوایی آمریکا منهدم شده‌اند.
✅
واقعیت: در تلاش‌های اخیر ایران برای حمله، هیچ هواپیمای آمریکایی منهدم یا آسیب‌دیده نشده است. همه موشک‌ها و پهپادها رهگیری شدند یا نتوانستند به مناطق هدف برسند.
🚫
ادعای سوم: رسانه‌های دولتی ایران گزارش می‌دهند که یک نفتکش تجاری به نام M/T Nora محاصره آمریکا را شکسته است.
✅
واقعیت: این کشتی تجاری نتوانسته از محاصره «دیوار فولادین» آمریکا عبور کند. بیش از ۲۰ ناو جنگی آمریکا، صدها هواپیما و هزاران نیروی نظامی همچنان در آماده‌باش هستند و اجرای کامل محاصره را ادامه می‌دهند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 405K · <a href="https://t.me/VahidOnline/77656" target="_blank">📅 19:24 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77654">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XpxIH01Oa-uerSQ72Zpa1XAo0qJyE4gOr5ziekY_Pmhrf7Cu2y0kMjmgR_WBMhpizFN75_TWh6vbFDdprgb1S6qreAsVlREmEbgnAK3jFLlgoGJltTWefiwxlZhZ5mRyQYwl7q8qQzj3gA07vgfEmo7ftLMMnyS9AXeTWkrXSLQQya2eOgRozjEc4tGMUxmXn9naek8AFCh83hy_dDx5YEgCoTgWx4r93fu_y4PEbryvyJ6z0FbqxRioAvJwQhUv6HzEbzrTYLLcQFLlX0j1pLORezzi7kuVqGYnHga0_ua-HBpEuoO9uh6_bWjDNrncWNMZS9O6Uh0-6G7qvbLJYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/032c2aacd6.mp4?token=SzUSABtQDStLVi3-Fj4rSvQtyITQPkeUfymSvJDj_LmkMK7nTQlh8OGdX-j4PrPcdi9dqMYRIT_R9a3Nq3hCj8EuKvnCULC6Po0gXX9m0CJTP5Ngzi1Sc9klhjc_6x3Z-gvi6-6VcgXnVYQ1Adgj981zzKDBjPpHiD5rC5qv4xjoIzqiS09AxaTgckNmZm15VIP4zSWX-FW74cyTyEH1tW7urIVBqiHM4IniWcaC5ZyStaN2XyJt_enhHbd_TNVtJmh8khO-ErUWZ4WYrXMzwnNQFop9UJ9DxfJ_STmpR6JayXTMOYCkgmHxGJ9SEzgi9yC4akZT6k8aB13kDbUDbA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/032c2aacd6.mp4?token=SzUSABtQDStLVi3-Fj4rSvQtyITQPkeUfymSvJDj_LmkMK7nTQlh8OGdX-j4PrPcdi9dqMYRIT_R9a3Nq3hCj8EuKvnCULC6Po0gXX9m0CJTP5Ngzi1Sc9klhjc_6x3Z-gvi6-6VcgXnVYQ1Adgj981zzKDBjPpHiD5rC5qv4xjoIzqiS09AxaTgckNmZm15VIP4zSWX-FW74cyTyEH1tW7urIVBqiHM4IniWcaC5ZyStaN2XyJt_enhHbd_TNVtJmh8khO-ErUWZ4WYrXMzwnNQFop9UJ9DxfJ_STmpR6JayXTMOYCkgmHxGJ9SEzgi9yC4akZT6k8aB13kDbUDbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی قدیمی منتشرشده در شبکه‌های اجتماعی رقص علیرضا سپاهی در اصفهان را نشان می‌دهد.
قرار بود او بامداد سه‌شنبه اعدام شود اما پیش از انتقال به محل اجرای حکم دچار سکته قلبی شد و به بیمارستان الزهرای اصفهان انتقال یافت.
@
VahidOOnLine
یک شاهد عینی گفت پس از انتقال علیرضا سپاهی، معترض محکوم به اعدام، به بیمارستان الزهرا اصفهان، فضای بخشی از این بیمارستان امنیتی شده و شماری از ماموران امنیتی در آن مستقر شده‌اند.
بامداد سه‌شنبه، ابوالفضل سپاهی بادجانی و امیرحسین صفری حسین‌آبادی، دو نفر دیگر از بازداشت‌شدگان اعتراضات ۱۸ و ۱۹ دی‌ماه ۱۴۰۵ در اصفهان، با حکم دادگاه انقلاب اسلامی اصفهان اعدام شدند. ابوالفضل سپاهی بادجانی، پسرعموی علیرضا سپاهی بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 369K · <a href="https://t.me/VahidOnline/77654" target="_blank">📅 19:19 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77653">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eebec49421.mp4?token=VqoZ_sReq25VhZAVhCSxihRrflxe37jvyRa_64g-bUEWsTS1aB3VChndpdWviTlQvq9643TGiWP5Xz-yWvI-9BAW7rzRNrt4sIlF89C22qS79FHaYiSkdCJ9ckFk1nfJMbc4v4yzAkYUdvVZZiPgYQKuDfSyKm47iYWMBaDqoAShG2orGhWuESgmhfUd3baDuIWg1C9Ph2Lsiz-9dJOa0qOdCsk3BKM0sumXZNokGyj-gb33_CtaBCrgdc7vp2UZwmRfk-AkyiDJJ7wt6vrNDUL1oK-iPpEQDju0y2vzFTPPp8lJEkWxIQqE7uOl1pPgQa-yjzoZuC8oNlWJ98fiKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eebec49421.mp4?token=VqoZ_sReq25VhZAVhCSxihRrflxe37jvyRa_64g-bUEWsTS1aB3VChndpdWviTlQvq9643TGiWP5Xz-yWvI-9BAW7rzRNrt4sIlF89C22qS79FHaYiSkdCJ9ckFk1nfJMbc4v4yzAkYUdvVZZiPgYQKuDfSyKm47iYWMBaDqoAShG2orGhWuESgmhfUd3baDuIWg1C9Ph2Lsiz-9dJOa0qOdCsk3BKM0sumXZNokGyj-gb33_CtaBCrgdc7vp2UZwmRfk-AkyiDJJ7wt6vrNDUL1oK-iPpEQDju0y2vzFTPPp8lJEkWxIQqE7uOl1pPgQa-yjzoZuC8oNlWJ98fiKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیدار خانواده جاویدنام محسن رشیدی خانی‌آبادی و علی ایازی با خانواده عرفان اسفندیاری و امیر حسین صفری ـ گزارشگر (ویدیو صدا ندارد)
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/77653" target="_blank">📅 19:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77652">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pEBfEkDHGraoirRPO0SNVqYAj6eLY8VMiZvFrUUpSHB9FXBdT8ZpBrv85Dp7nIgE39pvQIO6uXAOgsOMzhqYqsPtq7a9qDjg9guDaFA-O4bAO-mxSwzfGJJtgVe0pAcAEXKG3_84PiCeoQoz6N9rA_PwV3_zlQ1rAa9SM08Em-CurHjakBimhW4qpZ2vIblFRVIFMgXH3DnSWl0thH3ImhiJNhy9NQE1WXSb65-x7zmhOxSfVCRwEWlven9ce_qsjHxYdBAU4SCBW3Wz3MUkcWVH_7FqC-LHwtuozS_WJmJiXEunP9RnbqhwwWWQryhhiQyZiYpkjI1VlqC-YJD2aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه ان‌بی‌سی نیوز روز پنجشنبه هشتم مرداد، به نقل از یک مقام آمریکایی گزارش داد که دونالد ترامپ، رئیس‌جمهوری ایالات متحده، در جریان نشستی در هفته گذشته از فرسایشی شدن جنگ، محدودیت گزینه‌های نظامی علیه ایران و دست نیافتن به توافق خشمگین شده و بر سر مشاورانش فریاد کشیده است.
به گفته این مقام مسئول، بر خلاف اظهارات عمومی ترامپ مبنی بر رضایت از روند جنگ، نه او و نه مشاوران ارشدش از وضعیت موجود راضی نیستند. یکی از متحدان ترامپ در این باره گفت: «رئیس‌جمهور کلافه شده است؛ او تصور نمی‌کرد گرفتن امتیاز از ایران تا این حد دشوار باشد و هیچ راهبرد مشخصی برای چگونگی رسیدن به نقطه پایان وجود نداشت.»
این گزارش می‌افزاید نبود شفافیت درباره اهداف نهایی واشنگتن—از جمله این‌که آیا هدف اصلی جلوگیری از دستیابی ایران به سلاح هسته‌ای، بازگشایی تنگه هرمز یا نابودی برنامه‌های موشکی و پهپادی ایران است—برنامه‌ریزی برای پایان جنگ را دشوار کرده است. یک مقام آمریکایی تصریح کرد: «ما پیروزی‌های تاکتیکی متعددی داشته‌ایم، اما بدون داشتن یک راهبرد روشن، با یک شکست راهبردی روبه‌رو هستیم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 305K · <a href="https://t.me/VahidOnline/77652" target="_blank">📅 19:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77651">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LV37g8LtkpftWK6nj9M1xdcSsDUZpYYRoZ_68GWLV7GUuwGc0ul9UAI-FUyuxOtcaYBLBdWCuOoAShV3_rK8wU6RcXfhcFQmfBhelGKNrG8zfsh_8rK4FPxCMLQ_g_FAs8yz8P-sbXZZGFBSogG0AZW7UcLRWNOGM1fi0TAgfHC5hTCH7zMGTcgc6-A49bR2ZLPfEm97bP1qTECC5jYFYkPiuSUIzge707XZSNG-gbnr30TGX6p4KILZyWGubSJC2Ad-K0RGF4aUAViaoZdHTdXE3ytikqvT_n4t3vTZ9Wr35_V7g6ArzzM5ukUlY05gpyjWtMQS2MB3_iOQ25a4gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌وزارت دفاع چین گزارش‌ها درباره برنامه آن کشور برای تحویل صدها سامانه پدافند هوایی دوش‌پرتاب به ایران را رد کرده و آن را «کاملا نادرست و خلاف واقع» خوانده است.
جیانگ بین، سخنگوی وزارت دفاع چین، روز پنجشنبه در پاسخ به پرسشی درباره این گزارش گفت که ادعای مطرح‌شده صحت ندارد. وزارت خارجه چین نیز پیش‌تر گزارش مربوط به این معامله را «بی‌اساس» توصیف کرده بود.
رویترز روز چهارشنبه به نقل از سه منبع آگاه گزارش داد که ایران قرار است ظرف چند هفته نخستین محموله از مجموع ۳۰۰ تا ۴۰۰ سامانه پدافند هوایی قابل‌حمل ساخت چین را دریافت کند. به گفته این منابع، قرارداد مورد نظر شامل موشک‌های کیودبلیو-۱۲ و اف‌ان-۱۶ است و ارزش آن بین ۶۰ تا ۷۰ میلیون دلار برآورد می‌شود.
بر اساس این گزارش، قرارداد با یک شرکت مستقر در هنگ‌کنگ امضا شده که گفته می‌شود میان ایران و تأمین‌کننده چینی نقش واسطه را ایفا کرده است. منابع رویترز گفتند که قرار بود محموله‌های اولیه از شهر ارومچی در غرب چین ارسال و از مسیر پاکستان به ایران منتقل شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 307K · <a href="https://t.me/VahidOnline/77651" target="_blank">📅 19:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77649">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/A4dxjtlX-nJEqipLwsgiRuBIxokews_4YpcOixN8KCBAx5_xrYv0RHd8xgOmUlTtJ1jwevqUT24evWpBdy5AHPFYO1-ias9TgI7cBXjZHj53eCLl-kom3TSFvPFpW_ab-yFXl-BIJ3C22taSJ6AXPgNfyLJY19RRc2YGVxhxzaUHP_PPHLpPYbqtc6ASugAfswsezdHu4UWcuHnlUk8VckDJzkRPzjtjcIGea4yOuTEQ0SCCG-LbRCLlNmnG0mk9AIy9_Ksmv2QHb9ltaOnrv7RLU2gSSD8Y9RGT9F1s-MFxvpTc6q3LzlAnPnID0kyn71GzXLK6P2OlUmRde4U2yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AIPeqaVrEaXHBrSzdZWx74xgd0bUBF8qfU6ApBj5NTIeMOKkcyC8jQiWoRIVBIUTjOcdtQeS0Q7BqJ1XG69askcgflIiWWPbvOUAfY11rSnHHXm0MkvHhAarGrqDBUcTV3Sjhja0UDgDh9_yMMPjpIS9BHFFH4-tru8AANX7v5DKGmLDtNh5sEz1NUHHfyi9d-W-GFSpD2DIOaMUxoj_3l9sQcZ4SJC0WHDMVEZHjfD2-U2A3ZYxhiei_FRtXTJ9mmhmcrBKHnPg5JFJDVfU2t_P87KrzLXTgDIYiEz1Jv2kuxGV3ljdmit3qASPZhljnkW_NVNDD-QpbYbEdyZZ1g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نتانیاهو: با شکاف عمیقی که پس از کشتار دی‌ماه بین مردم و رژیم ایجاد شد؛ حکومت ایران در نهایت سقوط می‌کند
بنیامین نتانیاهو، نخست‌وزیر اسرائیل در پاسخ به مجری ای‌بی‌سی که به او گفت طبق گزارش نیویورک‌تایمز شما به ترامپ گفته بودید که ظرفیت موشکی حکومت ایران ظرف چند هفته نابود می‌شود و تغییر رژیم ممکن است رخ دهد، گفت: این ارزیابی اولیه من نبود و این بیان نادرستی از آنچه گفتم است.
برآورد من این بود که باید برای جلوگیری از دستیابی ایران به سلاح هسته‌ای اقدام کنیم.
نتانیاهو گفت، من گفته بودم که می‌توانیم شرایط را برای ضعیف‌تر شدن رژیم فراهم کنیم اما بر عهده مردم ایران خواهد بود که سرنوشت خود را تعیین کنند.
او درباره احتمال تغییر حکومت در ایران گفت: «فکر می‌کنم ایران از همیشه ضعیف‌تر و اسرائیل از همیشه قوی‌تر است، اما نمی‌توانم بگویم رژیم هم‌اکنون فروپاشیده است.»
نتانیاهو گفت: بگذارید یک پیش‌بینی کنم؛ پس از چنین شکاف بزرگی که به دنبال آن قتل‌عام (کشتار ۱۸ و ۱۹ دی‌ماه ۱۴۰۴) بین مردم و رژیم ایجاد شده، فکر می‌کنم که رژیم ایران در نهایت سقوط خواهد کرد.
نتانیاهو هشدار داد اگر ایران، اسرائیل را هدف حمله قرار دهد، «اشتباهی بسیار خطرناک» مرتکب خواهد شد و اسرائیل «بسیار شدید» پاسخ خواهد داد.
او در پایان گفت: «هدف من این است که مطمئن شوم ایران با این حکومت به سلاح هسته‌ای دست پیدا نمی‌کند. این موضوعی است که من و رئیس‌جمهور ترامپ هر دو بر سر آن توافق داریم، زیرا در آن صورت جهان متفاوتی خواهد بود.»
@
VahidOOnLine
نخست‌وزیر اسرائیل روز چهارشنبه در گفت‌وگویی اختصاصی با لینزی دیویس از شبکه ای‌بی‌سی نیوز تأکید کرد که دونالد ترامپ تصمیم‌گیرنده اصلی درباره جنگ ایران است و او تلاش نمی‌کند ترامپ را برای ادامه حملات علیه ایران متقاعد کند.
نتانیاهو در عین حال گفت نسبت به امکان دستیابی به راه‌حل دیپلماتیک با جمهوری اسلامی تردید دارد.
او گفت: «نمی‌دانم این احتمال کم است یا نه، اما نسبت به شیوه عمل ایران بدبینم. آن‌ها همیشه دروغ می‌گویند، تقلب می‌کنند و زمان می‌خرند. آیا تحت فشار کافی ــ فشار دیپلماتیک و اقتصادی ــ ممکن است این رفتار تغییر کند؟ می‌توان امتحان کرد.»
او افزود: «واقعیت این است که ما شریک و متحد هستیم. او شریک ارشد است؛ فراموش نکنیم که او رئیس‌جمهور ایالات متحده آمریکاست و من شریک کوچک‌تر هستم. اما من نخست‌وزیر اسرائیل هستم و هر زمان لازم باشد از منافع و امنیت کشورم دفاع می‌کنم.»
نتانیاهو همچنین از نقش دولت ترامپ در مقابله با «دشمن مشترک» قدردانی کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 291K · <a href="https://t.me/VahidOnline/77649" target="_blank">📅 19:13 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77648">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nqYPB9O58KF83UqnU9hyxa-Z5Uvs2vmt1ZXOwpJeNOyCPNA05mzqpw0nh-7NbXnKna3RicMIZ4s2THDuE502AEILrrrLgFKTRT7pNHBy-6_jOeh3dJk3lJbRDXZTzAG4f-ydnBw1wMzg3ebmYN-2QR14bbqFX5CRT278fnNggLtu3v6jTGTlw2KGRL16Lug-I6k-aHcCfr8dNp9YTjqzdTGbZxJx6v6QE4ZSut7TbOiJ1O-ElLHRTfB9BxxEeLyhvpnIZ4XuR2Js4de_Ifx64XXBTblmT3QA3J47XjtqW1xUyPgN4zJoocpUQUepj3PGxxGjgteHy198t9Cbvh3HOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتشار ویدیویی از ضرب‌وشتم چند زن در ایران در جریان یک پخش زنده اینستاگرامی، موجی از واکنش‌ها را در فضای مجازی به دنبال داشته است.
به‌ گزارش خبرگزاری میزان، وابسته به قوه قضائیه ایران، پس از انتشار ویدیوی این لایو اینستاگرامی با دستور مقام قضایی برای این فرد پرونده تشکیل شده است.
سعید راستی، معاون بخش «مبارزه با شرارت و جرایم خشن» پلیس اعلام کرد که این ویدیو باعث واکنش گسترده شهروندان شده و اطلاعات ارسالی مردم در شناسایی متهم نقش داشته است.
آقای راستی اضاف کرد که این فرد بامداد پنجشنبه، ۸ مرداد ۱۴۰۵، «در عملیاتی» در مرکز تهران شناسایی شد و «به دلیل مقاومت در برابر ماموران» دو گلوله به پاها و یک گلوله به دست او شلیک شده و در پی آن بازداشت شده است.
هم‌زمان، ویدیوهایی از این فرد پس از بازداشت در شبکه‌های اجتماعی منتشر شده است که او را در یک مرکز درمانی نشان می‌دهد. در یکی از این ویدیوها، او در حضور پلیس از زنانی که در ویدیوی ضرب و شتم دیده می‌شوند و همچنین از  شهروندان و پلیس عذرخواهی می‌کند.
@
VahidHeadline
دیروز بارها اون ویدیو رو برای من فرستاده بودند و می‌خواستند پخش بشه.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 291K · <a href="https://t.me/VahidOnline/77648" target="_blank">📅 19:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77647">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A05gCnz3Prm407fGwEfneuqj7oz2GF3CV7_fdtazA3s1HScZqehXf76ZjtF1_QiGylE8a_fPggH-PPwVfad1acDKWlTZ0S_E0eEcF516mdIMSUnZz1tosnxxXTKhwIE7psmT-2hO2kkwg5xAc9E0UyOsycIwuylJoXnBgXgRh9ZU4YgYea3LoZ8txRV8n_bVS8vYR3o0fV3YaQmf9UhFYiwN6p2S27PYVWvUOBO64b-1SCm5Eb9kysX7HdZVRSa4eHvqTlTlIuq0jg7NmLKDWNlMeT4pJe1JQQkJCe3xbcFkaHpflKcvBCwwmQbamb5j-vhnRSjL-cjwDgo8TxHIlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدعلی (آرمین) جنت‌خواه، فعال شبکه‌های اجتماعی، برای اجرای حکم قطعی سه سال حبس بازداشت و به زندان فشافویه منتقل شده است.
بر اساس این اطلاعات، آرمین جنت‌خواه روز ۳۰ تیر ۱۴۰۵ بازداشت و پس از انتقال به زندان فشافویه، اجرای حکم سه سال حبس او آغاز شده است.
اتهام منتسب به او در پرونده قضایی، «تحکیم مواضع اسرائیل» عنوان شده است.
جنت‌خواه پیش‌تر نیز در دی‌ماه ۱۴۰۲ توسط نیروهای امنیتی بازداشت شده بود. جزئیات مربوط به روند رسیدگی به پرونده و نحوه صدور حکم او به‌طور رسمی منتشر نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 286K · <a href="https://t.me/VahidOnline/77647" target="_blank">📅 19:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77646">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eNMfLTkoyPmDlainJUAuIlvsChcV_jubvWKeJHRuvXuvjzMCePdzbcSVGh4BzbjP7Uvzm46DvJ8laSpvWMbpmi0dsQEHnNJFlThr_4_lcescEGLmkg3qhkJCZ0RsTyZfu7_fd6MWjpehmw7kfrYE1HJo9Y_E8ZiHwAhXTiNvM6gO9_xfxPtRVqOVd55NqXx9tPMwU8hWhA7PIuwVChgNjsRdteA4yEsMXW40XlVCsXghqs2ObKY9CWnKRaU_QmzhvvA0-x_qmgoUcXS8aZZmmt4hOEROr3saiIMG7kDHeBJ90zl7obpjHn4de6J3KL0oaAYgYs7Fda4Y-hVBkwfvVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه پاسداران زنجان با انتشار بیانیه‌ای از کشته شدن سه نیروی این نهاد نظامی در حملات بامداد پنجشنبۀ آمریکا به نقاطی از ایران خبر داد.
در بیانیه روابط عمومی سپاه استان زنجان، به‌جز اسامی این اعضای سپاه پاسداران، جزئیات بیشتری درباره محل کشته شدن آنها و درجه و محل فعالیت‌شان اعلام نشده است.
این در حالی است که تا ساعاتی قبل، رسانه‌های ایران این مناطق را به‌عنوان نقاطی که هدف حملات بامداد پنجشنبه قرار گرفت، اعلام کرده بودند: «اهواز، آبادان، بندرعباس، قشم، بندرانزلی گیلان، کازرون و فراشبند استان فارس، چغادک بوشهر، شادگان و اروندکنار خوزستان و جزیره کیش»
@
VahidHeadline
پیام دریافتی بررسی‌نشده: در خود زنجان کشته نشدند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 282K · <a href="https://t.me/VahidOnline/77646" target="_blank">📅 19:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77645">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KU5PpP_IaOx6EMPgWqZks2ZFBGdXn_pM38F54IzMJgZqOWlvN3G5tjyJXFtcWgV1rb8biXMLvAZyxkwRm56XQ7BOs2-dTRQNxmk2IBB10SWBZrjFb0_o4MtZPPFZZAIMAoSL6qQV6lzceBv0TmBFPI2cWTytEY2ZJ1sQTY8kO_U-gXU1urOb8NxHquIr3ov58nm_rtlVzXrLaUYtGw7UlZ9lERqpcxGgh7YmbbsNfTdkk8w_UKfiJ0N9tKhwSSkKXfW0c5U-Ho-s2fTp_sFeQTVtnuraPPeO5Pr5JK4-WbQC-JnH26WfX6NQjd-SAflYG5tFocrVh4vHydccUTXBQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه پاسداران ادعا کرد که در حمله به پایگاه الازرق اردن «سه فروند هواپیمای اف۳۵» را از بین برده است.
سپاه پاسداران در بیانیه خود ادعا کرد که پنج‌شنبه هشتم مردادماه، با حمله به محل استقرار و سوله تعمیراتی جنگنده‌های اف۳۵ آمریکایی در پایگاه هوایی الازرق با چندین فروند موشک بالستیک، «سه فروند هواپیمای اف۳۵ را به کلی منهدم و به سه فروند دیگر خسارت سنگینی» وارد شد.
سپاه همچنین ادعا کرده که در این حمله «چند افسر و کادر فنی و تعمیراتی» کشته شدند.
این ادعاها در حالی است که پیشتر ارتش اردن اعلام کرد که پنج موشک شلیک شده از سوی جمهوری اسلامی را در آسمان این کشور رهگیری و منهدم کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/77645" target="_blank">📅 19:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77644">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h_C_wmVVG5vIpaEsM2VSwwYUownTRZsg3vJax28DoYssJPhhvQ_m1_nwbIMJ-TPRTcG8DK3tZNupB3TElW3Jzh4vz0Wzrdtgzavfh3--gt0EpdTFIlUxcV0uswwbF--rtqC5XgW6FtC7mtE-LhwY5Dc2D0yBk0ZsjDUxqCYLLtJSwMJy2VGVREFt5tmljZxh236vbccSuVxgQoNh0xwBRJOBWhSa7CqcXfxLq5ftaDTZ1eWio1O3JSmeBjvuD9iqKbzv2Vr6U6jTlZ5zOcz8m-DTaNBYLwO2jmfRg7rYTyNmKHRzBA6ygE233kQBUc5kYbR9tl9BTCzaemk2Hm7Rfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شعبه ۴۱ دیوان عالی کشور حکم اعدام بنیامین نقدی، از بازداشت‌شدگان اعتراضات سراسری دی ۱۴۰۴، را که پیش‌تر از سوی شعبه اول دادگاه انقلاب شیراز صادر شده بود، تایید کرد. وکیل او می‌گوید با وجود ابلاغ این رأی، درخواست اعاده دادرسی به‌زودی به دیوان عالی ارائه خواهد شد.
بنیامین نقدی شامگاه ۱۳ دی‌ماه ۱۴۰۴ در جریان اعتراضات در شیراز بازداشت شد.
بر اساس گزارش‌ها، علت بازداشت او شعله‌ور کردن یک کپسول آتش‌نشانی در مقابل نیروهای انتظامی عنوان شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 358K · <a href="https://t.me/VahidOnline/77644" target="_blank">📅 18:59 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77643">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s-IMyRMuhWM3uTiKbQsvHElnZNeZBOjv2KoagKxkt3mj6mzKRQ6OP2eADGLruW0bHtEqmbqNuJoz3-OMS9wbZjC2lBCOxn0Dhy6yAWDMb7JrXVkmzJMp7amUnPHM_UMXPXt6oXY9gxQ2ne0NTklSmvmqoVVOubuNs_1OnMLq6rPCnzNU6p4J0QuVXYkIpuyZ4vrKZcmke6NeJ0ADLSQyRIORozz7NzaHTmpR8a0hED_4bt_uUs-dTaRsbUtY45UZSEKZJeAYhVgKeZ0dlKMyrzMujbKFThreCFcermYicKO4Q9JfFyA3WV1uDA1RAPRAQW717rV4f06KehpMVQmhEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس دریافتی: آتش‌سوزی پس از حملات آمریکا به نقاطی در
#اهواز
پنج‌شنبه ۸ مرداد حدود ساعت ۵:۵۰
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 412K · <a href="https://t.me/VahidOnline/77643" target="_blank">📅 10:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77642">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mOc7Y7q4bLwOZohqrfWtrFCi3VKjNIwsahiuc0kD1heNWAziwdHIIIh1xU8iLAjRdck_JU-O6pgGBZne59jjKH8KboFPeR70Qe6vhg-aMHn2H-DUJuu8vtsA6BWugKiovhY7-p8E1NEoXN05y3xW7jEI16YhggaicVL7hcLdkgo_7wj_25VSvZh0kAEKMACZbdJ0P99PKlcfU6tUB5EqtIKYNuwOOs9rEwVUrvaOkjPqfTTECjC6dEysh3O1dyeBnPPYweItTkEiSbTrLwvGLbGG0bDYAh9o-YfzpunpS6YEmBfPxpEUp3_TdTmTlEe3yhRiSYrivogNyBbYKbOEGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اردن صبح پنج‌شنبه هشتم مرداد از مقابله با حملات موشکی ایران خبر داد و اعلام کرد پدافند هوایی این کشور «پنج موشک بالستیک» شلیک‌شده به این کشور را رهگیری کرده است.
سپاه پاسداران روز چهارشنبه نیز باوجود توقف چند روزه حملات آمریکا، به سمت اردن موشک شلیک کرده بود. پایگاه‌های ارتش آمریکا در اردن از ابتدای دور جدید حملات متقابل آمریکا و ایران از اهداف اصلی حملات موشکی و پهپادی سپاه پاسداران بوده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 416K · <a href="https://t.me/VahidOnline/77642" target="_blank">📅 08:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77641">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cd4efa1761.mp4?token=FPWuekMC2GknOzPn74bxl5phihus7x7zEJwe3BKvJIQZlrjgLsTDVgh43cCeZFAHpGLw9KVr1yxvP80VrerWxww_UtAnZ0AKV212_MGtwwsRkr5SbyahQVZGvd5KuwHfIhsqIO8IURjP4wrAky6w3DWNQcBGuhUZbzMETnLaJpckO0p-PGMPujniW74Tf6WfO4vfJFlI8VHvR-5l5ZJJl99MzAHESNur3thPGFAtU84ANOcF5uPyu-4b6bfx2hHM5JPvgLo5BFDT4iJSTMNg6zSRAd3UhURHD4vPXHjnpwwRhmWieok4UQmcn68Atv1h_3GCBhutJbG5N1yc8kfVCw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cd4efa1761.mp4?token=FPWuekMC2GknOzPn74bxl5phihus7x7zEJwe3BKvJIQZlrjgLsTDVgh43cCeZFAHpGLw9KVr1yxvP80VrerWxww_UtAnZ0AKV212_MGtwwsRkr5SbyahQVZGvd5KuwHfIhsqIO8IURjP4wrAky6w3DWNQcBGuhUZbzMETnLaJpckO0p-PGMPujniW74Tf6WfO4vfJFlI8VHvR-5l5ZJJl99MzAHESNur3thPGFAtU84ANOcF5uPyu-4b6bfx2hHM5JPvgLo5BFDT4iJSTMNg6zSRAd3UhURHD4vPXHjnpwwRhmWieok4UQmcn68Atv1h_3GCBhutJbG5N1yc8kfVCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از پیام‌های دریافتی درباره پرتاب موشک از اطراف تبریز
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 409K · <a href="https://t.me/VahidOnline/77641" target="_blank">📅 07:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77640">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jYBrwfUbtr4heRvil_RHsaBb06KyrmaSM4EwdonbHSEdtQrsw2wAEiE_8JuPXleCgQXBmPsX84eb3W5HVggxK5e2SpKk41mOBpt9_dpO3RUjEG3UcFnv7NImrPG_OwkpH5rP7glYMk-dAnXaeFzJTVU-PMB4h9qDBIPyAlbAwwwZhiCCQVvh3KyrmeS-0RoGA5r3PzeKFihTsQENHvsbld2KpsGN1Pmyq_EpDIhBhID9v0H8R7ysCO00x2EDVn2yejT5WvEywcydEnQvL3sNWsrY3bvm6MuCg5A0cmImaCGY1JG8D23sNAwkuKiKrl53eZcXNwQT6KmyYIXjxPTyIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از پیام‌های دریافتی درباره پرتاب موشک از اطراف خمین
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 408K · <a href="https://t.me/VahidOnline/77640" target="_blank">📅 07:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77639">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rhq1aR2N_9Z0D7FD1Z7BLtDf3xhGZ9q2hSRlTRQr4IXiYOBAeFZdDvYcfsX_FQ0ZtFFdqneUDa7mAfkE-ChQK_YbPSGAhIZcoOlJLvveF-yhZj9OptpzLWTOcbFqDPZIPsrVIvBJ0DTSKdT1l0MvyjAG1zhZ_4w3A_Les8L-cUkhIoeWM2Lt6_rTHGkFNGvFQsLMpewyFK3qE4_d5fXQIIzJqFJlhUKPimCoC563l9PLHjADedHULH1zjKurgzFAQe58IQ7V6HZSQR6Om08SmIwd8Ky_7lIFqoeg2ribWkZyXhIWiHDripp3xH9_LpzGFbkaLcYILbAwm3LRoVCgUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های دریافتی درباره پرتاب موشک از یزد
سلام وحید از سمت یزد دارن موشک میزنن
از یزد موشک زدن
سلام ساعت ۷:۲۱ صدای ارسال موشک داره میاد،
سلام از یزد موشک بلند شد ۷:۲۲
الان یزد 7:21 دقیقه  موشک فرستادن
سلام وحید. جان ساعت ۷و۲۰دقیقه از یزد موشک شلیک شد
وحید جان از یزد موشک بلند شد
۷:۲۱ پرتاب موشک از یزد
همین الان از یزد موشک زدن</div>
<div class="tg-footer">👁️ 395K · <a href="https://t.me/VahidOnline/77639" target="_blank">📅 07:22 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77638">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ROBOoE-U7XhMPtkxq5oH_s06bu3bGcy8hsX9uIWsNNKboR37wIQyGSNsCZnrB8PAKNvBLSEw5eoizGX7_cqE6DD8L60mdSlsQNDkmRU4-PqBA8ZbxNE06xwjGZ0q_E5yHdS7uWz5UHW7KI3cvuIPF6OfKT5lpmYq6evPhhtz9gMiG1xNPpjQ-LZnv9aXWb3WmZnTM_KLZg119cLazVRCrktQLA7V_7ZrfEKPZWZIhM52aMIZhkdAM5DUWu_2c8Zj4Q0LRDll0Q654HW-PswogZKPT5eNPCPh9FtYzofNeNDAut5G419kprImL90nXzbra7d3cj3f4WhquzaMpI8JAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وال استریت ژورنال در گزارشی نوشت آمریکا در پاسخ به حمله موشکی جمهوری اسلامی به نیروهایش در اردن، بامداد پنجشنبه حملاتی را علیه مواضع سپاه پاسداران انجام داد.
به گزارش این روزنامه، با وجود گسترده‌تر بودن این حملات نسبت به عملیات‌های پیشین آمریکا، یک مقام آمریکایی گفت این اقدام به معنای بازگشت به عملیات گسترده نظامی نیست. امیدها به دستیابی به یک پیشرفت دیپلماتیک فوری نیز با این حملات کمرنگ شد.
ارتش آمریکا این حملات را «پاسخی قاطع» به حمله روز سه‌شنبه جمهوری اسلامی توصیف کرد. این حملات چند ساعت پس از آن انجام شد که دونالد ترامپ، رییس‌جمهوری آمریکا، وعده داده بود به این حمله پاسخ خواهد داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 372K · <a href="https://t.me/VahidOnline/77638" target="_blank">📅 07:19 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77637">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/79133fc57f.mp4?token=J4kT3zp8oexdhGiFAZ1pvX6Ply9aMD0fxRsV0Ag-P1O1He0Bdt_4D5jSH8PzzyMHZOu5svNi1Tnsov3b3Dz26sequ3wd78V4mjEiLGQMqfMLgLhzfX73WR_IZs0_JcQkVoAKmv-OfvP2aSVuTZ68Y11HKh1ZJw7KAFzntlNWpOkGgaUPaM5IstGxeZRZAcNxCABlv7r5DWMVg98X3nxZCn4K2DzgM20uBWEx3WKu5iCOHG8S-u46mUCXex9wKo9cUU-1qMnKvyi4Gtun6OO1J2qvmNjSCaxrT0AKRTKGbYUvVsqSXVsOx0I-Nea6-PlEdczEuSFIBl_21Fxf2CwWRw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/79133fc57f.mp4?token=J4kT3zp8oexdhGiFAZ1pvX6Ply9aMD0fxRsV0Ag-P1O1He0Bdt_4D5jSH8PzzyMHZOu5svNi1Tnsov3b3Dz26sequ3wd78V4mjEiLGQMqfMLgLhzfX73WR_IZs0_JcQkVoAKmv-OfvP2aSVuTZ68Y11HKh1ZJw7KAFzntlNWpOkGgaUPaM5IstGxeZRZAcNxCABlv7r5DWMVg98X3nxZCn4K2DzgM20uBWEx3WKu5iCOHG8S-u46mUCXex9wKo9cUU-1qMnKvyi4Gtun6OO1J2qvmNjSCaxrT0AKRTKGbYUvVsqSXVsOx0I-Nea6-PlEdczEuSFIBl_21Fxf2CwWRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
آمریکا پس از تلاش ایران برای حمله، مواضع سپاه پاسداران را هدف قرار داد.
تامپا، فلوریدا — نیروهای فرماندهی مرکزی ایالات متحده (سنتکام) ساعت ۱۰ شب ۲۹ ژوئیه به وقت شرق آمریکا، در پاسخ به تلاش‌های دیروز برای حمله موشکی به نیروهای آمریکایی، موج سنگینی از حملات علیه ایران را با موفقیت به پایان رساندند.
تجهیزات و نیروهای سنتکام ده‌ها هدف متعلق به سپاه پاسداران انقلاب اسلامی در ایران را هدف قرار دادند؛ از جمله مراکز فرماندهی نظامی، تأسیسات موشکی و پهپادی، مواضع نظارت و دفاع ساحلی و توانمندی‌های دریایی. هدف این حملات، کاهش بیشتر تهدیدهای ایران و نیروهای نیابتی آن علیه نیروهای آمریکایی، کشتیرانی تجاری و کشورهای همسایه حاشیه خلیج فارس بود.
در ۲۸ ژوئیه، نیروهای سپاه پاسداران چندین موشک بالستیک را از ایران، در تلاشی برای انجام یک حمله غافلگیرانه به نیروهای آمریکایی مستقر در خاورمیانه، شلیک کردند. تمامی موشک‌های ایرانی با موفقیت رهگیری شدند.
در حال حاضر بیش از ۵۰ هزار نیروی نظامی آمریکایی در خاورمیانه مستقرند و همچنان در بالاترین سطح هوشیاری، متمرکز، مرگبار و آماده باقی مانده‌اند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 379K · <a href="https://t.me/VahidOnline/77637" target="_blank">📅 05:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77636">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">پیام‌های دریافتی:
۴:۴۹ اهواز انفجار شدید
انفجار های وحشتناک و پشت سر هم در اهواز
خیلی وحشتناکه
پشت سر هم
حداقل ۴ انفجار
اهواز رو زدن صدای ۲ انفجار
اهواز و دارن میزنن شدید
صدای انفجار مهیب توی اهواز ۴:۴۹
همچنان ادامه داره
تا الان ۴ انفجار بلند
صدا انفجار پشت سر هم ۴ تا زد ۴:۴۹ اهواز مرکز شهر
سلام وحید ۴:۴۹ اهواز ۴تا صدای انفجار شدید اومد
اهواز سه تا انفجار ۴:۵۰
سلام وحید الان ساعت 4:50 اهواز زدن
5 بار صدای زیاد اومده تا الان
اهواز رو زد چهار بار الان!!!!
۴ تا انفجار سنگین ظرف ۲ دقیقه
همین الان اهواز چهارتا صدای انفجار شدید
ساعت ۴:۵۰
همین الان اهواز نمیدونم چند تا افتضاح بلنده
تمام شیشه ها داره میلرزه
اهواز همین الان ۶تا انفجار
۶ تا پشت سر هم اهواز
اهواز ۴.۵۰ دقیقه صدای ۵ انفجار شدید .
سلام وحید جان ۴:۴۹ ۵تا انفجار خیلی شدید اهواز
وحید واییییی خیلی بد بود چندبار زد اهوازو
۴:۵۰ وحشتناک نزدیک ۴ یا ۵ تا انفجار شدید شدید ماشینا به صدا درومدن
ما همین الان با صدای انفجار از خواب پریدیم اهواز ۴:۵۰
اهواز ۴تا اتفجارشدید پشت سر هم
اهواز تو چند دقیقه چندین انفجار شدید داشتیم و طوری که خونه میلرزید و برقمون هم به یک باره قطع شد
اهواز به گلستان خيلي نزديك بود ٤ بار
😭
😭
😭
سلام وحید جان، اهواز اطلاعات توی گلستان رو زدن ما اونجاییم
اهواز فکر کنم سپاه توی اتوبان گلستان بود، سایت اداری. ۴ انفجار.
اهواز کوی سعدی بعد انفجار دوم برق رفته الان ساعت ۴:۵۴
سلام وحید،4,49دقیقه4انفجارشدید دراهواز احتمالااسنگرشکن بودن،
سلام وحید جان ساعت ۴:۵۵ دقیقه صدای انفجار پشت هم از دور شنیده شد
ساختمان اطلاعات اهواز توی گلستان رو زدن
اهواز سمت سعدی و گلستان نورش بود،برق سعدی هم رفت
من اهوازم جفت خونمون چندتا پادگان هست الان زدن چهار بار
خیلی نزدیک بود و وحشتناک
اطلاعات اهواز واقع در پیچ گلستان  رو زدن
وحید تو کل جنگ همچین صدایی نمیومد اهواز به طرز عجیب و وحشتناکی زد در حدی که خونه میلرزه نه فقط پنجره ها
ساعت4:50دقیقه صبح هشتم مرداد
حفاظت اتوبان گلستان رو زدن
🔄
ترکوندنمون اقا وحید
این یکی خیییلیییی بد بووود
بازم انفجار اهواز. ساعت ۵:۲۲
صدای انفجار مهیب در اهواز 5:23
انفجار مجدد اهواز 5:23
5:23 اهواز انفجار خيلييييييىىى شديد
اهواز دوباره زدن شدیدتر از قبلیا
۵:۲۸ یکی دیگه
یه انفجار شدید دوباره اهواز
اهواز صدا انفجار دوباره
وحید همین الان اهواز رو زدن
وحید دوباره انفجار اهواز
وحشتناک همین الان
اهواز ۵ و ۲۳ دقیقه همین الان شرق اهواز صدای انفجار
مجددا اهواز ساعت ۵و ۲۲
۵:۲۱ یدونه صدا اومد،۵:۲۷ هم یکی دوتا صدا اومد
باز اهواز رو زد وحید
زیتون کارمندی ۲تا دیگه الان زد
اقا وحید دوباره زد اهواز
اهواز الان زدن دوباره شیشه ها لرزید
😭
خیلی صدا و‌لرزش داشتتتت
هم اکنون  بازهم زدن05:23
5:22دوباره اهواز و زدن
5,23حمله دوباره اهواز
سلام گلستان اهواز باز زدن.. ساعت ۵:۲۲، ۵:۲۷
5/22" بازم اهواز رو‌زدن شدید
۵:۲۳ اهوازو بازم زد
سلام ۱ انفجار دیگه گلستان اهواز ساعت 5:23
چرا ول نمیکنه
الان یکی دیگه زدن5:23
ساعت 5:22 انفجار شدید اهواز
سلام اهواز وحشتناک بود گلستان سعدی اگه چسب نداشتیم رو شیشه احتمالا شیشه های دو جداره خورد میشدن
ما هنوز برق نداریم
🙏🏼
🙏🏼
انفجار های آخری بشدت به ما نزدیک بودن
آسمون قرمز شده بود از اتیش و صدای ویراژ هواپیما میومد
راحت میچرخیدن
با انفجار دوم برق رفت
۵ و ۲۲ دوباره زد همین الان
🔄
الان دوبارههههه
یکی دیگه5:27
دو انفجار دیگه ۵:۲۸
دوباره زدن وحید
دوباره زد
خیلی شدیده
الان ساعت ۵:۲۸ دوباره بد زد
اهواز همین الان دوباره زدن خونه لرزید با همون شدت بود
باز الان صدا دو انفجار
۵:۲۸ دو صدای انفجار مجدد اهواز
بسیار شدید و لرزش شدید تر شیشه ها
دوتا انفجار دیگه تو اهواز ۵و ۲۸
آقا وحید انفجار به شدت  شدید موج های بسیار زیاد در خانه
بازم انفجار خیلی شدیدی اومد ساعت ۵:۲۸ خیلی ترسناکه
دوتا دیگه زد ۵:۲۷
بندرعباس ساعت 5.24صدای دوتا انفجار وحشتناک بندر
پایگاه هوایی رو دوباره زدن
به نظر میاد یک جا رو دارن چندین بار میزنن. احتمالا سمت گلستان
انفجارها پشت سر هم شدن دوباره
بازم دارن اهوازو میزنن خیلی وحشتناک تر
همچنان داره میزنه
۵:۳۰ دوتا انفجار شدید
سلام اهواز بد دارن میزنن برق رفته مثل اینکه اطلاعات سپاه زدن
هر ده دیقه یبار تا خوابمون میره یه قلمبه میزنن
افتضاحه خیلی نزدیکه صداش
همه شهر حسش می‌کنه
اهواز، همون اطلاعات توی گلستان رو همچنان دارن میزنن
۵:۳۵ اهواز
بازم انفجار سنگین
همه شهر رو بیدار کرد!
یجوری اطراف مارو زدن که کل هوش و حواسم پرید حالمون بده و دقیقا ۱ ساعت دیگه باید سر جلسه امتحان باشیم ...
اهوازیم .
پمپاران در اهواز تمام نمیشه مرتب داره میزنه
سلام وحید جان.
خواهر من دانشگاه علوم‌پزشکی جندی‌شاپور می‌خونه. خوابگاهشون  توی گلستانه، روبه‌روی اطلاعات. می‌گه بعد از انفجارهای مهیب و‌ پی‌در‌پی اهواز شیشه‌ی اناق‌ها شکسته و   همه‌ی بچه‌های خوابگاهی هراسون توی محوطه جمع شده‌ن.
صدای دانش آموزان خوزستانی باشید
نیم ساعت دیگه چطور به سمت حوزه های امتحانی راهی شوند؟؟
🔄
دوباره اهواز رو زد 5:43
ساعت 5:43 دقیقه ی انفجار
بازم زد همین الان صداش دور بود
اهواز ۵:۴۲ مجدد زدن
ساعت ۵.۴۳ صدای دو انفجار در اهواز
دوتا دیگه اهواز رو زد
وحید دوتا دیگه
بازم زد این یکی لرزشش بیشتر بود
.۵:۴۳ گلستان اهواز دور بود ولی دوبار زد
دو انفجار مهیب دیگه در اهواز
تمام خونه و شیشه‌هاش لرزید
اهواز ساعت ۵:۴۳ دقیقه صدای انفجار
اهواز ۵:۴۳ شدید ترین انفجار از ساعت شروع حملات بود
😭
یکی دیگه
سمت شرق خیلی شدید بووود
دوباره انفجار در اهواز ۵:۴۲
سلام همین الان ساعت۵:۴۳ دقیقه روز پنجشنبه  اهواز و زدن
ملی راه هستیم صدا خیلی نزدیک بود
۵:۴۳اهواز ۲انفجاد شدید دیگر
بسیار شدید سمت کیانشهر‌اهواز، دزدگیرا به صدا در اومدن و خونه کامل لرزید
۲ انفجار پشت هم اهواز خیلی سنگینن انفجارهاش
شدید کیانشهر ۵و۴۴دقیقه
صدای انفجار اهواز همین الان ساعت ۵:۴۳ صبح
وحید بازم زد اهوازو دو تا ۵:۴۳
اهواز، ۵:۴۳ …این یکی شدیدتر از بقیه بود
5:42 صداى انفجار در اهواز
ساعت ۵/۴۲ دقیقه انفجار فوق شدید در پدافند اهواز کیانشهر
5:44 یکی دیگه اهواز
دوباره اهواز انفجار شدید ساعت ۵:۴۴
وحید جان الان دوباره صدای انفجار اومد دوبار پشت سر هم اهواز
وحید زد همین الان زیتون اهواز لرزید
وحید مجدد زد دو بار یه صدا انفجار دیگه هم اومد اما لرزش نداشت و نزدیک بود خیلی ساعت 5.44
سمت کیان ابادیم ما شدید صدا اومد ۵و ۴۴ دقیقه
همین الان اهواز کیانشهرو زدن
جفت پدافند
ما کیانشهریم
فکردیم داخل خونمون رو زدن
تا الان ۸بار اهواز رو زدن ۶تاش اطلاعات اهواز بود دوتا دیگه خیلی دور بود معلوم نبود کجا بود
انفجار آخر پدافند بود کنار میدان تره بار
سلام وحید بالای۸انفجار در اهواز رخ داد صداهای خیلی وحشتناکی داشت تروخدا صدای مارو به برسونید بچه ها نیم ساعت دیگه باید برن امتحان بدن گناه دارن اهواز رو ترکوندن
اهواز هم ۴:۴۸ دیقه هم ۴:۵۰ دیقه
هم ۵:۲۰ دیقه هم ۵:۲۸ دیقه
دوتای دیگه هم الان ۵:۴۳
مجموعا حدود ۱۳ تا انفجار
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 378K · <a href="https://t.me/VahidOnline/77636" target="_blank">📅 04:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77635">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d1-CxTyIRJzeKSektHShXGbxrLHewBpif1FuC0rdDMS-m2xb4fy2nAPJtcjSis5oLt4npXGQ74SjrRMZdx6qcQOVnIm4TvFhdQJKmQShzfYcMR6nx6tHf2e_leJxtyLOIy1X1cOtPV7xQgWtC1Hs6XMa7lt4ByBuTJroDZwXJP0mwGKvW_QSZPfoo4BnfhhUr9V8btQqyJGRSNBPxMKHqHTRtaEBUF0so8cJfIVcxb4EU-wnENLeAcWQOxeBeya_nK4sRHGXaXJNNpP8R0Dbi89b08pRCh6qCGyvoASa1WcpLnUakpvHGZeoQ2ksq6yMI6Hb-c1bLL2ASojrLCOkCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش خبرگزاری تسنیم، در پی شنیده شدن صدای انفجار در استان فارس، منطقه‌ای در اطراف شهر کازرون هدف حمله قرار گرفته است.
پیش از این رسانه‌های داخلی ایران از شنیده شدن صدای چندین انفجار درنورآباد استان فارس خبر دادند.
@
VahidOOnLine
پیام‌هایی که من دریافت کره بودم:
درود کازرون خونه ی ما لرزید
در نزدیکی کازرون صدای چند انفجار اومد ۳:۴۲
ساعت 3:41 - 3:42
کازرون چند تا صدای انفجار شدید اومد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/77635" target="_blank">📅 04:48 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77634">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">پیام‌های دریافتی:
‌
۴:۳۵ قشم دو انفجار
۰۴:۳۶ دو انفجار بندرعباس
وحید دوتا انفجار جدید بندر همین الان۴.۳۷
بندرعباس ۲ تا انفجار در حد لرزش در و پنجره ساعت ۴.۳۷
۰۴:۳۶ دو انفجار بندرعباس
صدای انفجار بندرعباس
دو انفجار شدید بندر عباس ۴:۳۷
بندرعباس شدید تر از قبل
دوتا همین الان
۴ تا انفجار مجدد بندرعباس ۴.۳۷ دقیقه
وحید جان صدای دو انفجار در بندرعباس ساعت 4.37
بندرعباس مجدد صدای مهیب ساعت ۴:۳۷
بندرعباس الان ساعت ۴:۳۷ صدای انفجار
وحید ۴:۳۷ زدن بندرعباس ۲ تا شدید موج داشت
الانم دوتا سنگین زدن از خواب پریدیم 4:36
سلام وحید جان همین الان دوباره صدای انفجار میشنویم
دو انفجار شدید همین الان بندرعباس
دوباره بندرعباس انفجار به همون اندازه ۳.۳۸
صدای سومی اومد شدیدتر۴.۳۸
دوباره ۴:۳۸
🔄
دوباره انفجار پشت سرهم ۴.۴۳
همین الان انفجار دوباره
درود ۲ دیگه زد ۴.۴۳ بندرعباس
چند تا دیگه هم زدن همین الان
دوباره ۴:۴۳ بندرعباس
این جدیدا فقط موج دارن
بندرعباس ساعت ۴:۴۳ صدای انفجار شدید
محله چاه تنگو درگهان چن تا خونه دچار آسیب شده انگاری ک زیر آوار موندن کسی بعد انفجار
ساعت ۵ و ۱۰ دقیقه باز قشم زدن
قشم محله ی نریمان،  زیرانگی و محله چاهتنگو رو زدن.. یه دکل هم زدن
سلام وحید داخل قشم محله چاه تنگو  یه خونه مسکونی رو زدن الان رفتم راه رو بستن معلوم نیست فعلا کی داخلش بود ولی خونه پودر شده
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/77634" target="_blank">📅 04:38 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77633">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oXuA3K3C6eSG4Crf_j07mPFfwb_oc7gWEL14TL3geskVWp78xwJQZD0UyCymK-o93SVoSjHLpNJJMvNsMp2_ezcNyUIsCtpBhkI7_Ch9P8ow-Hb4vLa_WJV0ct9tAJtnUT8CDB0QRTAK-Cva8VUVtA0S8P_nbqKgnEXY1Dc8QVTPMjYwv4fAEJmh3PJGtvkX-FCIW4j892wM3F_jSb7RPtmZ5cZ_Lye4M7p6d4uatmQgJIqX7bhLmPkQGUYLNhvdBzdtcC8elmI1YY3jFeG19YDbvYSXlR9HghefI9FosEMwmsIOgzZ3I4TwEKc06PNJeNh7lth60rKRq-yEkvI5lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
نیروهای ایالات متحده امروز ساعت ۸ شب به وقت شرق آمریکا [۳:۳۰ بامداد پنج‌شنبه به وقت تهران] حملات علیه ایران را آغاز کردند.
این حملات، پاسخی قدرتمند به تلاش‌های دیروز ایران برای حمله به نیروهای آمریکایی مستقر در خاورمیانه است.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/77633" target="_blank">📅 03:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77632">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">پیام‌های دریافتی:
سلام وحید جان بندرعباس صدای 2 انفجار
3:40
سلام ۳ و ۴۰ دقیقه بندرعباس دوتا انفجار
۰۳:۳۹
بندرعباس
حداقل ۲ انفجار
درود
هم اکنون صدای ۳ انفجار بندرعباس ساعت ۳ و ۴۲ دقیقه
هم اکنون صدای ۳ انفجار بندرعباس ساعت ۳ و ۴۲ دقیقه
۴ ۵ تا انفجار توی کمتر از ۱ دقیقه بندرعباس
سه تا انفجار ذیگر
همین الان ۳:۴۱ صدای چند انفجار در بندرعباس
دوباره یک انفجار دیگه 3:41
دوباره یکی دیگه تند تند دارن می زنن
صدای انفجار بزرگ همراه با لرزه زمین بندرعباس
3:41 همین الان بندرعباسو دارن میزنن در و پنجره میلرزه
دو انفجار شدیدتر ساعت 3:41
بندرعباس صدای سه انفجار اومد ساعت ٠٣:٤١
سلام وحید جان همین الان انفجار شدید بندرعباس
سلام وحید جان بندرعباس رو داره میزنه سمت فرودگاه و پایگاه هوایی رو
قشم ساعت ۳و ۴۰ دقیقه انفجار در حد لرزش خونه ها
قشم همین الان با جنگنده بمب بارون شد
صدای سه انفجار شدید در شهر قشم
بندرعباس رو زدن همین الان ۲ تا صدای انفجار
شد ۴ تا
بندرعباس دو انفجار مهیب ادامه دار
صدا دور بود 3: 40
سلام وحید جان الان ساعت ۳ و ۴۰ دقیقه صدای انفجار اومد قشم ،برق ها نوسان پیدا کرد
بندرعباس همینننننن الانننننن خیلی شدید یا خدا
همین الان که دارم تایپ میکنم زدن
همین الان 3:40 دقیقه قشم با صدای انفجار بیدار شدیم
قشم صدا میاد پشت هم
سلام صدای انفجار۳:۴۳ شدید تر از قبلی
۳.۴۱ بندرعباس صدای انفجار
یه انفجار بزرگتر تر
با موجش در و پنجره لرزید
بندرعباس ۳.۴۳
قشم 2 انفجار نزدیک شهر
بندرعباس الان دوباره صدا اومد و خونه لرزید ۳ و ۴۳
بندرعباس ۵ تا انفجار پشت سر هم
انفجار بندرعباس ۲ تا شدیدددد بود صداش الان ۳.۴۲
+ ده‌ها پیام مشابه دیگر
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 361K · <a href="https://t.me/VahidOnline/77632" target="_blank">📅 03:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77631">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">پیام‌های دریافتی:
بوشهر انفجار
بوشهر زدن
بوشهر چندتا صدای انفجار اومد
جم همین الان دارن میزنن
۵ تا زد
دوتا صدای انفجار اومد
بوشهر ستا انفجار ۰۳:۳۸
سایت موشکی برازجان رو زد الان.ساعت ۳:۳۷
بوشهر، جغادکیم
همبن الان از خواب پریدم
دو صدای خیلی بلند
سلام ‌وحید ساعت۳:۳۰ چندتا صدای انفجار شنیدیم صدا خیلی زیاد بود پنجره هامون انگار تکون خورد
سلام برازجان همین الان صدای جنگنده و یک انفجار
وحید جان جم الان چندتا صدای انفجار با لرزش اومد
ٰ3:38
بوشهر دارن میزنن
درود، سه بار جم صدا اومد.
۵ انفجار بوشهر همین الان ۳:۴۰دقیقه
بوشهر -چغادک ۴ انفجار ۰۳.۳۷
اقا وحید بوشهر چند تا صدای انفجار شنیده میشه
ولی خیلی صداش دوره
سلام آقا وحید ساعت ۳:۳۸ دقیقه بوشهر رو زدن
صدای جنگنده توی برازجون چند دقیقه هست که تموم نشده و هی بلند تر میشه
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/77631" target="_blank">📅 03:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77630">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">پیام‌های دریافتی:
همین الان سه انفجار در کیش
کیشو زدن همین الان ۳:۳۱
کیش دم بندرگاه ساعت ٣:٣٠ ٢ تا زدن
وحید جان کیش ۲ تا ۳:۳۲
سلام وحید
کیش رو الان زد
دوتا انفجار
وحید الان کیشو زد
۰۳و۳۰ دقیقه انگار  تووآب بود
سلام وحید کیش همین الان صدا اومد
سلام وحید جان
همین الان ۳۱:۰۳ کیش صدای انفجار اومد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/77630" target="_blank">📅 03:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77629">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f5dd2ae3de.mp4?token=kv1bt4dAcWQD4mPlGseVyAzl5lr3KfpwUufsq1zw5-FQOVbFPegWIM35QTk_kUe8paPFnmeNm9EjRbWVPwZwbmF8SchWVAVjx4_xJG5z1GOxTIV1vKY4gDkp86rAbh5fcouvhOcxwc-4MDbMnXDdACgNdh6TP4oWbQr4RWU-F3Kn4npM6gDy647Ygy66eviuJHhMdlN3QGYPFDRPvczknZCo-ZgkBoBvDy7pKFe9agLicRSXEjiCXlJS4D5Mnd4cYF_NLyrKe63Zkd2mt8mRRYMu8wk5fyV13tej0vi98VXA5NlgMZx8I7bYpimrjOfzRjVSCeQKuDz2JS3tVg771Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f5dd2ae3de.mp4?token=kv1bt4dAcWQD4mPlGseVyAzl5lr3KfpwUufsq1zw5-FQOVbFPegWIM35QTk_kUe8paPFnmeNm9EjRbWVPwZwbmF8SchWVAVjx4_xJG5z1GOxTIV1vKY4gDkp86rAbh5fcouvhOcxwc-4MDbMnXDdACgNdh6TP4oWbQr4RWU-F3Kn4npM6gDy647Ygy66eviuJHhMdlN3QGYPFDRPvczknZCo-ZgkBoBvDy7pKFe9agLicRSXEjiCXlJS4D5Mnd4cYF_NLyrKe63Zkd2mt8mRRYMu8wk5fyV13tej0vi98VXA5NlgMZx8I7bYpimrjOfzRjVSCeQKuDz2JS3tVg771Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی:
آبادان ترکوندن
سلام آبادان چندبار پشت سرهم صداهای وحشتناکی اومد زمین لرزید
صدای انفجار آبادان
سلام آبادان چندبار پشت سرهم صداهای وحشتناکی اومد زمین لرزید
سلام وحیدجان همین الان چهار بار صدای موشک شنیدیم آبادان ساعت ۰۳:۳۲
سلام آقا وحید تا الان آبادان ۸ بار صدای انفجار اومد ۳:۳۰ دقیقه
احتمالا دارن موشک هوا میکنن
سلام وحید، آبادان ساعت ۳:۳۱ پنج شیش تا صدای انفجار بلند شنیدیم
وحید سلام
۶ تا صدای انفجار
همین تلان ، ابادان
وحید سرساعت ساعت ۳:۳۰ ابادان صدای چندتا صدای انفجار اومد ولی دوره احتمالا خارج از شهره
حداقل ده تا انفجار آبادان ساعت ۳:۳۰
از ساعت ۳:۲۰ شروع شد
اقا وحيد صداي ٦ انفجار ساعت ٣:٣٠صبح در ابادان
وحید آبادان ۵ تا انفجار شدید ۳:۲۸
همین الان صدای ۶ الی ۷ تا انفجار از آبادان اومد
ساعت ۳.۳۰ بامداد
آبادان نزدیک ۴/۵ تا صدا شنیدم ... برای اطمینان حتی به دوستمم گفتم اونم شنیده
۳:۳۳ آبادان رو بیشتر از ۵بار زد. بیرون شهر یه چیزی آتیش گرفته، نمیدونم کجاست
آقا وحید آبادان رو ساعت سه نیم زدن شیش تا انفجار
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 337K · <a href="https://t.me/VahidOnline/77629" target="_blank">📅 03:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77628">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/I5unLXEWQd2LkjixRLrF2AT63M-83hskqPzuyenKMhsx29z2tLVCai3VOO5wXeaVaGpk2Oa3M_WAyIZDmfpxFjjNu-YjFvpuS4NEQbu2fGRz6wTPszXFM7OhOg6Nf_t2v3HkUQ6pBmddbQ-zb2ptPfL8yNHmvNO8-YypXAxKxRfrbjVTHfcOVqWsfvC_63yrmpz9uByggEm7YhSxYpd344ROJnrBP63YUYbz-qH4w6f3tmhxPUzSbUlTn6SlBGoFQo4vLk-71NLfdagnaKZmQN6dvkouMhe0s5AMQjeLzRufXTkx3ZENPSEltr1yBUkT333C5X1JTbrCp3iazMp8MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست خبرنگار اکسیوس:
یک مقام آمریکایی به من می‌گوید ارتش ایالات متحده در حال انجام حملات هوایی در ایران است.
BarakRavid
آپدیت:
بعدا همین گزارش در خود اکسیوس:
ترجمه ماشین: یک مقام آمریکایی به اکسیوس می‌گوید ارتش آمریکا روز چهارشنبه اجرای حملات هوایی در ایران را آغاز کرد.
چرا اهمیت دارد: این نخستین حملات آمریکا در ایران از زمانی است که دونالد ترامپ، رئیس‌جمهوری آمریکا، جمعه گذشته کارزار بمباران را متوقف کرد تا فرصت دیگری به مذاکرات بدهد.
حملات روز چهارشنبه در تلافی حمله موشکی ایران در روز قبل انجام شد که یک پایگاه آمریکا در اردن را هدف قرار داده بود. به گفته ارتش آمریکا، همه موشک‌ها رهگیری شدند.
محور خبر: ترامپ بعدازظهر چهارشنبه به خبرنگاران گفت که آمریکا در ادامه همان روز ایران را «بسیار سخت» هدف قرار خواهد داد.
ترامپ گفت: «حالا نوبت ماست.»
ترامپ مدعی شد ایران پذیرفته است که شلیک موشک‌ها اشتباه بوده و از آمریکا خواسته است تلافی نکند.
تصویر کلی: ترامپ پس از ۱۳ شب متوالی حمله به اهداف نظامی ایران، حملات را متوقف کرده و فرصت کوتاهی برای دیپلماسی ایجاد کرده بود.
حمله موشکی ایران این وقفه را درهم شکست و ترامپ را واداشت پنج روز بعد کارزار نظامی را از سر بگیرد.
یادداشت سردبیر: این یک خبر فوری است. برای دریافت تازه‌ترین اطلاعات دوباره مراجعه کنید.
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/77628" target="_blank">📅 02:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77627">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">پیام‌های دریافتی تایید نشده از ساعت ۲:۱۹
سلام وحید جان صدا ۳ تا انفجار شنیدیم نوراباد فارس
۳ تا انفجار همین الان نوراباد ممسنی
آقا. وحید نورآباد ممسنی رو بد زدن
۳ تا شیشه ها لریزد
وحید همین الان نور آباد صدای انفجار اومد ۳ تا بود دقیقن
وحید جان چند لحظه قبل صدا چندتا انجار شدید نوراباد فارس
آقا وحید نوراباد ممسنی رو زدن
صدا هواپیما هم میاد
وحید همین الان نور آبادو زدن
🔄
پیام‌های ساعت ۲:۲۴:
اوه یدونه دیگه
یدونه دیگه ام زدن
البته دور بود
وحید بازم زد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 385K · <a href="https://t.me/VahidOnline/77627" target="_blank">📅 02:25 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77626">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">پیام‌های دریافتی شاید درباره پرتاب شدن موشک که با صدای جنگنده اشتباه گرفته میشه:
یزد الان صدا جنگنده اومد
ساعت ۱۲:۱۰
صدای جنگنده روی آسمان یزد
الان یزد صدای جنگنده امد خیلیم پایین پرواز میکرد صدای انفجاری نیومد اگر بیرون شهر زده نمیدونم
سلام وحید جان
۰۰:۰۷  از تنگه یه صدایی اومد مثل انفجار
شایدم لانچ بالستیک بود
ده دقیقه پیش از یزد موشک بلند شد
وحید جان صدای جنگنده میاد یزد
آپدیت:
پیام‌های دریافتی  بعد از انتشار پست:
یزد هواپیما رد شد
موشک و جنگنده نبود
ارتفاع به شدت پایین
سلام یزد جنگنده خودی بود
سلام وحید جان صدایی که از یزد میومد مال هواپیمای مسافربری بود
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 401K · <a href="https://t.me/VahidOnline/77626" target="_blank">📅 00:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77625">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/chd0UNE6CAzBu7qaoZUoKRMVmF5XET0p1oNa2kl3nQxSizfV0WKpx3v4lOAkv7MWGVFrr9uTgSbBqd-RUiP0ApTqmk5sy-pI6Ca4-sqFEHI2d5dCKJXifdJkIN8IQxpYrpc1R71JzALDi60BU5ZJYb1N957Vc2qnzdOWjJdgfigFazn2zVqDOcbxPBwmPdvpP8L8xHv838CVMKoqSJa88X6c3Yw55ml1jZrF1kDB8SAAz9L2sEFm2KgKET2RNBB7EBsjWXukWYyQQi6pRQ1ambXLPnNpAaOZwkZoMV3fk_RPTfXUOMu86ayprVKCkZIVZdTKWPqDX3y700-bHB3pEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اسکات بسنت، وزیر خزانه‌داری آمریکا، با انتشار پیامی در شبکه اجتماعی اکس نوشت «رژیم ایران که با سقوط آزاد اقتصاد و تورم سه‌رقمی روبه‌رو است، به‌شدت به منابع مالی نیاز دارد».
او تاکید کرد «ایالات متحده اجازه نخواهد داد ایران تجارت جهانی را گروگان بگیرد یا از کشتیرانی بین‌المللی برای تامین مالی «سپاه پاسداران»، اقدامات تهاجمی و سرکوب استفاده کند».
پیش از این، وزارت خزانه‌داری آمریکا چندین بسته تحریمی علیه افراد، شرکت‌ها، نفتکش‌ها و شبکه‌های مرتبط با صادرات نفت ایران اعمال کرده و اعلام کرده بود این اقدامات با هدف محدود کردن منابع مالی جمهوری اسلامی و سپاه پاسداران انجام می‌شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 387K · <a href="https://t.me/VahidOnline/77625" target="_blank">📅 00:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77624">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c878874010.mp4?token=LeLah8LcmBhbKzjpm_lRRT9-iCEyRHD8Xp7HQmrAxLbPy3Kjp9curjAjMC7mIO5ooiRrS3xDY9hYPHnrcjFOzvpPmGHqzKImHcG7tf48fMM06OLSfHav3MUGtf_3MIr-ImNIKmZQaoNq8zRYb0AQwMeNfOc7Vi9tG5B-EKp1QfeejgVk_2oveYGX2W__FUUp0haXIPNM0r_QzZG3spvE3YRC5BkcZ_cTWqnsniPG0GfMM47DLekYQ5--K78J8P1-LgFRjZ8HR-d9Hce1TnnS0cbJjUArOhyjL-V3DRibOBWsJpMUbf95YFFnJk-6vvNUub5te-xXSeEZf-aAfgbFJA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c878874010.mp4?token=LeLah8LcmBhbKzjpm_lRRT9-iCEyRHD8Xp7HQmrAxLbPy3Kjp9curjAjMC7mIO5ooiRrS3xDY9hYPHnrcjFOzvpPmGHqzKImHcG7tf48fMM06OLSfHav3MUGtf_3MIr-ImNIKmZQaoNq8zRYb0AQwMeNfOc7Vi9tG5B-EKp1QfeejgVk_2oveYGX2W__FUUp0haXIPNM0r_QzZG3spvE3YRC5BkcZ_cTWqnsniPG0GfMM47DLekYQ5--K78J8P1-LgFRjZ8HR-d9Hce1TnnS0cbJjUArOhyjL-V3DRibOBWsJpMUbf95YFFnJk-6vvNUub5te-xXSeEZf-aAfgbFJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بخش‌هایی از گفت‌وگوی ترامپ با خبرنگاران در کاخ سفید، ترجمه ماشین:
خبرنگار: در مورد حمله پهپادی به نفتکش LNG در سواحل مصر چه اطلاعاتی دارید؟ آیا نشانه‌ای وجود دارد که این حمله به ایران مربوط باشد؟
ترامپ: خب، می‌توانم گزارشی به شما بدهم. در این باره توجیه شده‌ام. این کمی از همان ماجراست، اما اوضاع رو به صاف‌شدن است؛ وضعیت دارد روشن می‌شود. در این میان، ما قرار است ضربه بسیار سختی به آنها بزنیم، چون نوبت ماست که ضربه بزنیم. آنها می‌دانند که این حمله در راه است و از ما می‌خواهند این کار را نکنیم. اما دیشب سعی کردند به آن شلیک کنند.
ما پنج موشک داشتیم که با سرعت ۸۵۰۰ مایل در ساعت در حرکت بودند و هر پنج موشک سرنگون شدند؛ اما با این حال آنها شلیک کردند. پس نوبت ماست. خواهیم دید که آیا در مقطعی به یک توافق می‌رسیم یا نه، اما ضربه بسیار سختی به آنها خواهیم زد.
—-
خبرنگار: در چه سناریویی تصور می‌کنید ایران به تأسیسات و پرسنل آمریکا در خارج حمله کند و شما عقب‌نشینی کنید؟
ترامپ: چنین چیزی را نمی‌بینم. نه، ما عقب‌نشینی نمی‌کنیم. ضربه سختی به آنها خواهیم زد. واقعاً می‌توانم این را بگویم، چون آنها در این مورد کار زیادی نمی‌توانند انجام دهند.
این گروه با گروهی که ما با آن سروکار داریم متفاوت بود. آنها قبلاً عذرخواهی کرده‌اند، اما باید یک ضربه‌ای به آنها بزنیم.
خبرنگار: وقتی آنها حمله می‌کنند، آیا همیشه پاسخ خواهید داد؟
ترامپ: بله، تقریباً.
خبرنگار: آقای رئیس‌جمهور، آیا این در پاسخ به حمله موشکی بالستیک شب گذشته به اردن است؟ وقتی می‌گویید نوبت ماست که ضربه بزنیم.
ترامپ: بله، فکر می‌کنم بیشتر به آن مربوط می‌شود. آن رویداد کوچک‌تری بود، اما آنها پنج موشک با سرعت ۸۰۰۰ مایل در ساعت به سمت ما شلیک کردند. خوشبختانه افرادی را داشتیم که بهترین تجهیزات جهان، یعنی سامانه پاتریوت، را به کار می‌گرفتند.
فکرش را بکنید؛ پنج موشک بزرگ با سرعت ۸۶۰۰ مایل در ساعت مستقیماً به سمت ما می‌آمدند و هر پنج موشک سرنگون شدند. چطور است؟ خیلی خوب است. فقط ما می‌توانستیم این کار را انجام دهیم؛ هیچ‌کس دیگری نمی‌توانست.
—-
خبرنگار: آقای رئیس‌جمهور، در مورد جنگ، آیا می‌خواهید مجلس نمایندگان پیش از ۳۱ اوت برای رسیدگی به لایحه تحریم‌های روسیه و ایران بازگردد؟
ترامپ: اگر لازم باشد، بله؛ هرچند راستش نباید لازم باشد. آیا منظورتان طرح لینزی گراهام است؟
خبرنگار: بله.
ترامپ: می‌خواهم ایران را هم به تعرفه‌ها اضافه کنند، نه فقط به تحریم‌ها. فکر می‌کنم این مهم است و همان چیزی است که لینزی می‌خواست. شنیده‌ام روی روسیه تعرفه گذاشته‌اند، اما روی آن پنج کشوری که به ایران مربوط می‌شوند تعرفه‌ای نگذاشته‌اند.
دوست دارم تعرفه‌هایی علیه ایران ببینم. این موضوع را بسیار قوی‌تر می‌کند. شاید بتوانید به آنها بگویید که به نظر من باید برای روسیه تعرفه بگذارند، اما برای ایران هم باید تعرفه در نظر بگیرند. این دقیقاً همان چیزی بود که لینزی می‌خواست.
——
خبرنگار:  رئیس‌جمهور شی به شما گفته بود که چین هیچ سلاحی به ایران نخواهد داد یا نخواهد فروخت. اکنون گزارش جدیدی منتشر شده که می‌گوید ایران قرار است ۴۰۰ پرتابگر موشک از چین و از طریق پاکستان دریافت کند.
ترامپ: خب، این تعجب‌آور خواهد بود. چنین چیزهایی پیش می‌آید، اما واقعاً تعجب‌آور خواهد بود. او خیلی قاطع به من گفت که در این کار مشارکت نخواهد کرد و می‌داند که من کاملاً ناامید خواهم شد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 390K · <a href="https://t.me/VahidOnline/77624" target="_blank">📅 23:44 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77623">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">اکسیوس:
پشت پرده دیدار تعیین‌کننده «بی‌بی» با ترامپ در کاخ سفید
ترجمه ماشین:
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در دیدار خود با رئیس‌جمهور ترامپ درباره احتمال دستیابی به توافقی با ایران ابراز تردید کرد و درباره افزایش فشار اقتصادی بر ایران «از طریق ابزارهای نظامی و غیرنظامی» به گفت‌وگو پرداخت؛ یک مقام ارشد اسرائیلی این موضوع را در نشستی با خبرنگاران بیان کرد.
اهمیت موضوع:
دیدار روز سه‌شنبه نخستین ملاقات نتانیاهو و ترامپ از زمان آغاز جنگ در ۲۸ فوریه بود. این دیدار در حالی انجام شد که ترامپ همچنان برای دستیابی به توافقی با ایران تلاش می‌کند، اما هم‌زمان بازگشت به عملیات رزمی گسترده را نیز در نظر دارد.
▪️
چند ساعت پس از این نشست، ایران برای نخستین بار از زمانی که ترامپ روز جمعه حملات آمریکا در ایران را متوقف کرد، یک حمله موشکی علیه پایگاهی آمریکایی در اردن انجام داد.
▪️
ترامپ روز چهارشنبه در مصاحبه‌ای با فاکس‌نیوز وعده داد که پاسخی جدی خواهد داد. حمله غافلگیرانه ایران ممکن است رئیس‌جمهور را به سوی تشدید تمام‌عیار درگیری سوق دهد.
▪️
مقام اسرائیلی گفت نتانیاهو در انتظار تصمیم ترامپ است، اما به‌روشنی به او گفته است که اگر ایران به اسرائیل حمله کند، پاسخ اسرائیل فوری و قدرتمند خواهد بود.
آنچه در اتاق گذشت:
ایران موضوع اصلی گفت‌وگوی ۹۰ دقیقه‌ای بود.
▪️
مقام اسرائیلی گفت آن‌ها سه گزینه‌ای را که ترامپ برای گام‌های بعدی در نظر دارد بررسی کردند:
۱. دستیابی به توافق با ایران.
استیو ویتکاف و جرد کوشنر، فرستادگان ترامپ، همچنان با ایرانی‌ها مذاکره می‌کنند، هرچند در حال حاضر اختلاف‌ها همچنان گسترده به نظر می‌رسد. مقام اسرائیلی گفت نتانیاهو به ترامپ گفته است که نسبت به امکان دستیابی به توافق با ایرانی‌ها تردید دارد.
۲. ادامه محاصره دریایی ایران
هم‌زمان با افزایش فشار اقتصادی.
۳. ازسرگیری و تشدید حملات نظامی.
▪️
این مقام گفت: «همه این گزینه‌ها را به‌طور مفصل و بسیار صریح بررسی کردیم؛ نه با هدف ترجیح دادن یک گزینه بر گزینه‌ای دیگر، بلکه برای بررسی اینکه هرکدام چه نتیجه مطلوبی می‌تواند داشته باشد. موضوع گفت‌وگو همین بود.»
نمای نزدیک:
مقام اسرائیلی گفت ترامپ درباره تأثیر جنگ بر بازارهای انرژی و اقتصاد جهانی ابراز نگرانی کرد.
▪️
نتانیاهو به ترامپ گفت حکومت ایران عمدتاً می‌کوشد از تنها اهرمی که برایش باقی مانده است — تنگه هرمز — برای وادار کردن آمریکا به دادن امتیاز استفاده کند.
▪️
مقام اسرائیلی گفت نتانیاهو نگرانی‌های ترامپ را نادیده نگرفت، اما به او گفت راه‌هایی برای افزایش بیشتر فشار بر اقتصاد ایران وجود دارد؛ اقتصادی که هم‌اکنون نیز تحت فشار شدیدی قرار دارد.
▪️
مقام اسرائیلی گفت: «درباره افزایش فشار اقتصادی از طریق ابزارهای نظامی و غیرنظامی گفت‌وگو کردیم. درباره امکان ادامه محاصره با هدف تحت فشار قرار دادن ایران صحبت کردیم.»
▪️
مقام اسرائیلی گفت در درون رهبری ایران میان کسانی که به‌شدت نگران فروپاشی اقتصادی هستند و عناصر تندروتری که معتقدند تا زمانی که کنترل تسلیحات را در اختیار دارند و می‌توانند از پایگاه حامیان حکومت پشتیبانی کنند مشکلی ندارند، اختلاف‌نظر وجود دارد.
▪️
مقام اسرائیلی افزود: «آن‌ها با مشکلات تأمین سوخت، صف‌های طولانی در پمپ‌بنزین‌ها و کمبود گازوئیل روبه‌رو هستند. اعتراض‌های کوچکی شکل گرفته است، زیرا مردم به‌شدت ناراضی‌اند. حکومت بسیار نگران این وضعیت است و می‌ترسد مردم به‌دلیل شرایط اقتصادی قیام کنند.»
پشت صحنه:
مقام اسرائیلی گفت مجتبی خامنه‌ای، رهبر جمهوری اسلامی ایران، «درباره همه‌چیز» موضعی بسیار منفی دارد، اما مشخص نیست دستورهایی که به او نسبت داده می‌شود واقعاً از جانب خود او صادر می‌شود یا نه.
▪️
مقام اسرائیلی مدعی شد: «او زنده است، اما هیچ‌کس نمی‌تواند شهادت دهد که واقعاً او را دیده است. به اطرافیانش گفته بدون تأیید او هیچ کاری انجام ندهند و حتی گفته می‌شود یک بار وقتی بدون اجازه‌اش کاری کردند، عصبانی شد.»
نمای دور:
مقام اسرائیلی گفت نتانیاهو نقشه‌ای از سوریه را به ترامپ نشان داد که براساس آن، مناطقی که ترکیه در سوریه کنترل می‌کند «۵۰ برابر بزرگ‌تر» از مناطق تحت اشغال اسرائیل است.
▪️
مقام اسرائیلی مدعی شد ترکیه ۵ درصد از خاک سوریه را کنترل می‌کند، در حالی که اسرائیل ۰٫۱ درصد آن را در اختیار دارد.
▪️
یک مقام آمریکایی گفت برخلاف اشغالگری اسرائیل در جنوب سوریه، حضور نظامی ترکیه در شمال سوریه در حال حاضر با رضایت و به دعوت دولت سوریه انجام می‌شود.
▪️
مقام اسرائیلی گفت نتانیاهو به ترامپ گفته است اسرائیل تا زمانی که تهدیدی از جانب «گروه‌های جهادی» وجود داشته باشد، حضور خود را در «منطقه حائل» جنوب سوریه حفظ خواهد کرد.
▪️
مقام اسرائیلی گفت: «نتانیاهو می‌خواست این موضوع را به ترامپ نشان دهد، زیرا او گاهی براساس اطلاعات نادرستی که بعضی افراد در اختیارش می‌گذارند، به دیدگاه‌های مشخصی می‌رسد. اگر در همان مراحل اولیه راهی برای تغییر نظرش پیدا نکنید، آن نظر تثبیت می‌شود. بنابراین می‌خواستیم واقعیت‌ها را، در صورت امکان به‌شکل تصویری، به او نشان دهیم.»
▪️
مقام اسرائیلی گفت نتانیاهو همچنین درباره توافق هسته‌ای آمریکا و عربستان سعودی با ترامپ گفت‌وگو کرد. ترامپ به نتانیاهو گفت این توافق را در چارچوب عادی‌سازی روابط عربستان سعودی با اسرائیل می‌بیند.
▪️
مقام اسرائیلی گفت: «اگر شاهد پیشرفت واقعی باشیم، درباره موضوع هسته‌ای حرف‌هایی برای گفتن خواهیم داشت.»
تصویر کلی:
مقام اسرائیلی گفت نتانیاهو به ترامپ، معاون رئیس‌جمهور ونس و ویتکاف گفته است که درباره کاهش کمک‌های نظامی آمریکا به اسرائیل تا رسیدن به صفر ظرف ۱۰ سال جدی است. او تأکید کرد که خواهان پیشبرد مذاکرات برای تدوین یک تفاهم‌نامه در این زمینه است.
▪️
مقام اسرائیلی گفت ترامپ و اعضای تیمش اعلام کردند بازخوردهایی از جمهوری‌خواهانی دریافت کرده‌اند که نگران‌اند به‌دلیل حمایت از حذف تدریجی کمک‌ها، به ضدیت با اسرائیل متهم شوند.
▪️
نتانیاهو به آن‌ها گفت شخصاً و به‌صورت علنی رهبری این تلاش را بر عهده خواهد گرفت، زیرا می‌خواهد اسرائیل به استقلال دفاعی دست یابد.
▪️
مقام اسرائیلی گفت: «درباره یک فرایند ۱۰ ساله صحبت می‌کنیم. از پیشنهادها استقبال می‌کنیم و شاید این اتفاق بتواند سریع‌تر رخ دهد.»
▪️
این مقام حتی گفت نتانیاهو به بخش دفاعی اسرائیل دستور داده است روی ساخت یک جنگنده مدرن ظرف یک دهه کار کند تا نیروی هوایی این کشور حتی در صورت توقف تحویل جنگنده‌های اف‌ـ۳۵ و دیگر هواپیماهای پیشرفته از سوی آمریکا، همچنان قدرتمند باقی بماند.
▪️
این مقام گفت نتانیاهو نمی‌خواهد اسرائیل به «حسن نیت کنگره آمریکا» وابسته باشد، زیرا معتقد است جهت‌گیری سیاسی هر دو حزب درباره کمک‌های نظامی در حال منفی‌تر شدن است.
▪️
نتانیاهو معتقد است وضعیت اقتصادی اسرائیل به این کشور اجازه می‌دهد کمک‌های نظامی آمریکا را به‌تدریج کنار بگذارد. مقام اسرائیلی گفت نتانیاهو پیشنهاد کرده است تفاهم‌نامه جدید شامل ۱۶ میلیارد دلار کمک نظامی مستقیم آمریکا و همچنین ۵ تا ۱۰ میلیارد دلار حمایت از توسعه سامانه‌های دفاع موشکی اسرائیل باشد.
▪️
افزون بر این، نتانیاهو پیشنهاد ایجاد یک صندوق مشترک ۱۶ میلیارد دلاری برای تحقیق و توسعه سامانه‌های تسلیحاتی جدید را مطرح کرده است.
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/77623" target="_blank">📅 23:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77622">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d13dda12b7.mp4?token=capqSTmOyDU67JfHrnJWr6LtxAdG0-tBDbRwodUu1_leNneT12CCwpUznFUNEiZXQRHiVMloMyZ8CV4UvZSf-KEv61lAe7bp12TFsOLTe8PP1jE2YerV2n8cdvI8oLwRa7y0g486JotHedXDZ8E3JdQRwfOdnOXQjWXyFBol2k9UZoV4W7NnbWNZQLr0CEi4VlBjMERhuzVB6s0clI_EKTPSEKlMJIlf0hZQ2t8HeqdVuC4kRj-OO-UmftkfvHW6AAV8UHqpGYPLKiNTBiZ8Xh6dDEjkVUqBlxwRhr3F3lXjkSWT6tBJyRL1d7PB4izxB205edLyp0UL-j0pQF_2fw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d13dda12b7.mp4?token=capqSTmOyDU67JfHrnJWr6LtxAdG0-tBDbRwodUu1_leNneT12CCwpUznFUNEiZXQRHiVMloMyZ8CV4UvZSf-KEv61lAe7bp12TFsOLTe8PP1jE2YerV2n8cdvI8oLwRa7y0g486JotHedXDZ8E3JdQRwfOdnOXQjWXyFBol2k9UZoV4W7NnbWNZQLr0CEi4VlBjMERhuzVB6s0clI_EKTPSEKlMJIlf0hZQ2t8HeqdVuC4kRj-OO-UmftkfvHW6AAV8UHqpGYPLKiNTBiZ8Xh6dDEjkVUqBlxwRhr3F3lXjkSWT6tBJyRL1d7PB4izxB205edLyp0UL-j0pQF_2fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، با انتشار ویدیویی، جزئیاتی از گفتگو و تبادل نظر خود با پیت هگست، وزیر جنگ ایالات متحده که روز چهارشنبه هفتم مردادماه در واشنگتن انجام شد را به اشتراک گذاشت.
نتانیاهو گفت: «هگست در این گفتگو به من گفت وقتی به وضعیت جهان نگاه می‌کنیم، کشورهایی هستند که اراده مبارزه در کنار ایالات متحده را دارند، اما توانایی لازم را ندارند. در مقابل، کشورهایی هم هستند که از توانایی برخوردارند، اما اراده جنگیدن ندارند.»
نخست‌وزیر اسرائیل در ادامه افزود که وزیر جنگ آمریکا تاکید کرده است: «تنها در اسرائیل است که ما هم‌زمان شاهد وجود اراده و توانایی مبارزه هستیم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 373K · <a href="https://t.me/VahidOnline/77622" target="_blank">📅 20:35 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77621">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ho-kws33_JTuG5c6C8YkrTvXaG6Ww3_1yxg1LQ-Ghv3x37c16GLzMfSmYjXqfQagWKBuSaXhmQMaaJn09yMFRD6n0EbQJvEC80-wMeYr5JwtPiH7rE8w6A1l7F5VIAAkxvQO0_9RvGCXaB-RVzNczL0thfZQPu1yHI_to8u2_s--eXsBK-iMyL42Dn_YCfcRJNtRzYcmMrin2bNjdHZr_FEvjn6fhfG7jXBG1LlS_VJigkPAw91iQRybAYE-cND24rnmyBqScNp32ZjClzWvCa6xOgf9jzLBdGbvROzKejhpS5D7r6D_zs9tfm0XRHFMSOAsS5krcVM8Nv59Bi68RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌ها از وقوع انفجار در پایانه گاز طبیعی مایع بندر دمیاط مصر هنگام تخلیه محموله خبر دادند.
همزمان، شرکت امنیت دریایی امبری و منابع امنیتی اعلام کردند یک پهپاد به یک شناور ذخیره‌سازی گاز متعلق به آمریکا برخورد کرده است؛ حادثه‌ای که به آتش‌سوزی دو کشتی منجر شد، اما تاکنون گزارشی از تلفات جانی منتشر نشده است.
بر اساس گزارش‌ها، این انفجار هنگام تخلیه محموله در پایانه گاز طبیعی مایع بندر دمیاط رخ داد.
شرکت امنیت دریایی امبری اعلام کرد یک پهپاد به یک شناور ذخیره‌سازی شناور گاز که تحت مالکیت آمریکا است، برخورد کرده است. به گفته این شرکت، در پی این برخورد آتش‌سوزی ایجاد شد و سپس به کشتی دیگری نیز سرایت کرد.
شرکت خدمات بندری اینچ‌کیپ نیز در گزارشی جداگانه اعلام کرد دو کشتی حامل گاز در بندر دمیاط دچار آتش‌سوزی شده‌اند.
امبری اعلام کرد خدمه هر دو شناور تخلیه شده‌اند و آتش تحت کنترل درآمده است. این شرکت افزود تاکنون هیچ گروهی مسوولیت این حمله را بر عهده نگرفته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 360K · <a href="https://t.me/VahidOnline/77621" target="_blank">📅 20:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77620">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NX3D6OaIPB553NPgGdwRdqzmgzT_9oC8a0PA8qVRNEpPUN53jqq42t68zMLQ-bT97XtbPgUKx3gdOQsT-7e5h2l_U74DA_t2EUZA6eJeUIZG4suf_rqDmbrjQZQ64OoweoIbBlr-5ILjjhkcH1ZVOttk6u4waKuygJzeIQZXcz5znT3CFxOXslBjM1_w1CAqfAasP2Hz3QYr5f6hlFMP-B0cGeLRBm6ru9f2oycdMDB0kIsQxp9j0xYkwsaEmXauq8-4O9YZi3soMbuPRYKT4QQj3CH07MimDqLaEGSBI0K2nFmLFzl8Zi_r6Ojs7tBHB_EjCjSVNVxDO9AYKXWPQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
🚫
ادعا: پس از تهدیدهای اخیر و تلاش برای حمله به کشتی‌های تجاری و دریانوردان بی‌گناه در حال عبور از تنگه هرمز، سپاه پاسداران انقلاب اسلامی ایران همچنان ادعا می‌کند که دریانوردان بین‌المللی باید فقط از مسیرهای مورد ترجیح سپاه استفاده کنند.
✅
واقعیت: تنگه هرمز یک آبراه بین‌المللی است. سپاه هیچ اختیاری برای تعیین مسیر حرکت آزاد و بدون مانع ندارد. کشتی‌های تجاری با حمایت نظامی آمریکا همچنان از این تنگه عبور می‌کنند. از اوایل ماه مه، نیروهای سنتکام به عبور حدود ۱٬۰۰۰ کشتی و ۵۰۰ میلیون بشکه نفت خام از این آبراه باریک کمک کرده‌اند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/77620" target="_blank">📅 19:13 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77619">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NlNw3NdGZVR5h0bu47FVwnfOwoBrjG9L8FtextDAOBCBAYBPy4Px4iwA3EkN2ZCPvsk0ZeVnZozsxsTd5xzJjki6U4jnXnYegswOdV0LSQIOR-DCd1a5vspWY7phtUAFXvqOlrg0nWK9p9sER0rggjRmjYspr2TGPpkgKHTXuZ9W3N9tHKV2ZMcXUkZwiHv7m88K3hkJlqfE9oXyyO6jlz92Zg3jUPfZ7u-LT6o3AFj33Gf3HLYPUScl0vpWYfy0lJ0KSr34W5VAzi4D-xcKibAS75HMPLWmVsQU2c9rcSF2CjyIBYYVdDRh8Dbwicj6ZJE8cC5iJPsgOjL8C_kjag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش تسنیم، نیروی دریایی سپاه پاسداران انقلاب اسلامی روز چهارشنبه هفتم مردادماه، اعلام کرد سه نفتکش را در تنگه هرمز به دلیل بی‌توجهی به هشدارها «هدف قرار داده و توقیف کرده است».
در این گزارش به نام این شناورها، مالکیت، محل دقیق حادثه و جزئیات تخلفات ادعایی آن‌ها در این آبراه اشاره‌ای نشده است، اما تهران مسیر جایگزین جنوبی در امتداد سواحل عمان را رد کرده است.
بر اساس بیانیه‌ای که تسنیم منتشر کرده، سپاه پاسداران تاکید کرده است که «مداخله‌ها و دستورات غیرقانونی» ایالات متحده از سوی شناورهای حاضر در منطقه «بی‌پاسخ نخواهد ماند».
مرکز عملیات تجارت دریایی بریتانیا، هنوز وقوع چنین حملاتی را تایید و گزارش نکرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/77619" target="_blank">📅 18:49 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77618">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/e-bStwhvUWEaSYnUR1sTgA8YRoy2TLc8IUbBMt34uHD1db9G0g5nWUf8U4t-exsLZj_IfZb37_bKedT_mkEqM91dFe5-Wuwk_h7aM01QuIa1sReXhI-nIsY8QiAmXjSSGhLc7qovSVS_cVzEAtyaLYVKwMfgSB4P_6egwZAWuYTQi1M1aZhQfFI4C1U6sOKI41MPAmO2lf7PjHnUnZYXJH4gM3-uQgiEvGN8fHPcG1ODallKWvZmml22rwRGGbhmKoKv0FO5Dm1YB8u7v43vauFu6i4WL27SGqR2G9GNRZBHzP4ACkfZcj__Ez9wcMsMmvqURveSPKYGG6KVyuAgTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچ دانشگاه ایرانی در رتبه‌بندی تاثیرگذاری تایمز ۲۰۲۶ حضور ندارد
در رتبه‌بندی تاثیرگذاری و پایداری دانشگاه‌های جهان در سال ۲۰۲۶، نام هیچ دانشگاهی از ایران دیده نمی‌شود؛ این در حالی است که در فهرست سال ۲۰۲۵، ۳۴ دانشگاه ایرانی حضور داشتند.
تایمز امسال نحوه مشارکت در این رتبه‌بندی را تغییر داده و آن را به عضویت دانشگاه‌ها در شبکه پایداری و ارائه اطلاعات از سوی خود موسسات مشروط کرده است.
برخی رسانه‌های ایران این تحول را با عنوان «حذف ایران» پوشش داده‌اند؛ تعبیری که اقدامی هدفمند یا تنبیهی را تداعی می‌کند، در حالی که هنوز مشخص نیست نبودن دانشگاه‌های ایرانی ناشی از تصمیم تایمز بوده یا شرکت نکردن آنها در سازوکار تازه رتبه‌بندی.
رتبه‌بندی‌های موسسه تایمز از شناخته‌شده‌ترین و پرمراجعه‌ترین نظام‌های ارزیابی دانشگاه‌ها در جهان است و نتایج آن می‌تواند بر اعتبار بین‌المللی، جذب دانشجو و همکاری‌های علمی دانشگاه‌ها اثر بگذارد.
@
VahidHeadline
برای نخستین‌بار از زمان آغاز انتشار رتبه‌بندی «دانشگاه‌های تأثیر‌گذار» موسسه آموزش عالی تایمز، نام هیچ دانشگاهی از ایران در نسخه سال ۲۰۲۶ این فهرست دیده نمی‌شود. رخدادی که در کنار افت مداوم جایگاه دانشگاه‌های ایران در دیگر نظام‌های معتبر رتبه‌بندی جهانی، بار دیگر وضعیت آموزش عالی کشور را زیر ذره‌بین برده است.
بر اساس نتایج منتشر شده، در رتبه‌بندی سال ۲۰۲۶ تایمز، یک‌هزار و ۶۴۶ دانشگاه از ۱۱۶ کشور بر پایه اهداف توسعه پایدار سازمان ملل متحد (SDGs) ارزیابی شده‌اند. با این حال، برخلاف سال‌های گذشته، نام ایران به‌طور کامل از این فهرست حذف شده و مؤسسه تایمز نیز تاکنون توضیحی درباره علت این موضوع ارائه نکرده است.
حذف نام ایران از این رتبه‌بندی در حالی رخ داده که دانشگاه‌های کشور از زمان آغاز انتشار آن در سال ۲۰۱۹ همواره در فهرست تایمز حضور داشتند. تنها در سال ۲۰۲۵، ۳۴ دانشگاه ایرانی در این رتبه‌بندی ارزیابی شدند و برخی از آن‌ها در چند شاخص توسعه پایدار، از جمله «سلامت و رفاه»، «آموزش باکیفیت»، «صنعت، نوآوری و زیرساخت» و «برابری جنسیتی»، جزو دانشگاه‌های برتر جهان بودند.
همزمان، نتایج تازه‌ترین رتبه‌بندی جهانی QS نیز از ادامه روند نزولی دانشگاه‌های ایران حکایت دارد. رتبه‌بندی QS که از معتبرترین نظام‌های ارزیابی آموزش عالی در جهان به شمار می‌رود، دانشگاه‌ها را بر اساس شاخص‌هایی مانند اعتبار علمی، کیفیت پژوهش، میزان استناد به مقالات، نسبت استاد به دانشجو، همکاری‌های بین‌المللی و اشتغال‌پذیری فارغ‌التحصیلان ارزیابی می‌کند.
در این ارزیابی دانشگاه تهران ۴۵ پله سقوط کرده و از رتبه ۳۲۲ به ۳۶۷ جهان رسیده است. دانشگاه تبریز ۱۰۸ رتبه، دانشگاه فردوسی مشهد حدود ۱۲۵ رتبه و دانشگاه‌های شیراز، اصفهان و آزاد اسلامی نیز افت قابل‌توجهی را تجربه کرده‌اند؛ به‌طوری که دانشگاه آزاد از جمع هزار و ۴۰۰ دانشگاه برتر جهان خارج شده است.
در مقابل، کشورهای منطقه روندی معکوس را طی کرده‌اند. ترکیه با ۲۵ دانشگاه در رتبه‌بندی QS حضور دارد و دانشگاه فنی استانبول به رتبه ۲۷۹ جهان رسیده است. امارات متحده عربی نیز سه دانشگاه در میان ۳۰۰ دانشگاه برتر جهان دارد.
حسین سیمایی‌صراف، وزیر علوم، کاهش سرمایه‌گذاری در پژوهش، ضعف همکاری‌های علمی بین‌المللی، کمبود زیرساخت‌های آموزشی و پژوهشی و محدود شدن فرصت‌های مطالعاتی را از عوامل افت جایگاه دانشگاه‌های ایران دانسته است.
شاهین آخوندزاده، معاون تحقیقات وزارت بهداشت، نیز اعلام کرده بود که محدودیت‌ها و اختلال‌های گسترده اینترنت در سال ۲۰۲۶، پژوهشگران ایرانی را حدود یک‌سوم سال از فعالیت علمی بازداشت؛ موضوعی که به گفته او می‌تواند به کاهش حدود ۱۰ هزار مقاله علمی و افت بیشتر جایگاه علمی ایران منجر شود.
کارشناسان آموزش عالی نیز می‌گویند کاهش ارتباط دانشگاه‌های ایران با مراکز علمی جهان، محدودیت در جذب استاد و دانشجوی خارجی، کاهش بودجه پژوهشی، ضعف زیرساخت‌های آموزشی و دسترسی محدود به منابع علمی بین‌المللی، از مهم‌ترین عوامل کاهش رقابت‌پذیری دانشگاه‌های ایران در رتبه‌بندی‌های جهانی است.
رتبه‌بندی دانشگاه‌های تأثیرگذار تایمز از سال ۲۰۱۹ با هدف ارزیابی عملکرد دانشگاه‌ها در تحقق ۱۷ هدف توسعه پایدار سازمان ملل منتشر می‌شود و تنها نظام رتبه‌بندی جهانی است که نقش دانشگاه‌ها را در حوزه‌هایی مانند آموزش، سلامت، برابری جنسیتی، نوآوری، محیط زیست، عدالت و توسعه پایدار می‌سنجد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 348K · <a href="https://t.me/VahidOnline/77618" target="_blank">📅 17:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77617">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OvSsWfY1rIaDLcGxwO28IppH1EkbznlUaQldnkUmM1GFd8A9lxDAXVX9rcb0ArT89gRJoGSXx0BdyyEPyKI8R86lyVJJ1cqu8-aqUFiTC4z0fFdNRQPGExds2LGUQj1WS946ULdAOi2D4W3UZ8pL2NCXYF7j2RpP0oW2bupQtTijHpsyAHsjhQzd1cxshN-tRANt3oPlOLIinwv0zRhXyKTguy-rYQWdv3VLkG7fe1565TQ6hMOeuEiwnoSIFzLv3VXusbo2LawWnwjiUtQ_eakL4jyJh7WNGOoSLN2TUn8a48tjJV8YH18WfkwP3NtYJTgYvoVSQjegUpaRl9E1Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، روز چهارشنبه پس از آنکه ارتش ایالات متحده اعلام کرد چندین موشک بالستیک شلیک‌شده از سوی ایران به سمت نیروهای آمریکایی در خاورمیانه را رهگیری کرده است، وعده داد که ایران را به‌شدت هدف قرار خواهد داد.
او در گفت‌وگو با شبکه فاکس نیوز گفت: «حسابی نابودشان خواهیم کرد. خیلی سخت به آنها ضربه خواهیم زد.»
این گفت‌وگوی تلفنی به‌صورت کامل پخش نشد، اما یکی از خبرنگاران فاکس نیوز خلاصه‌ای از اظهارات ترامپ را منتشر کرد.
@
VahidHeadline
گفت: حسابی نابودشان خواهیم کرد. ضربات سختی به آنها خواهیم زد و به‌شدت تنبیه خواهند شد.
ترامپ همچنین درباره حملات هوایی آمریکا و عربستان سعودی به شبه‌نظامیان مورد حمایت جمهوری اسلامی در عراق گفت این حملات با هماهنگی دولت عراق انجام شده است.
رییس‌جمهوری آمریکا این شبه‌نظامیان را «سرطانی برای جهان» توصیف کرد و گفت در حال بررسی صدور هشدارهای بیشتر علیه نیروهای نیابتی جمهوری اسلامی و ارتباط آنها با حکومت ایران است.
ترامپ همچنین گفت اکنون موضع بنیامین نتانیاهو درباره جمهوری اسلامی را درک می‌کند.
او در پاسخ به پرسشی درباره احتمال ادامه مذاکرات با جمهوری اسلامی نیز گفت: «اجازه می‌دهیم به گفت‌وگوهایشان ادامه دهند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 325K · <a href="https://t.me/VahidOnline/77617" target="_blank">📅 16:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77615">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/76c3174d20.mp4?token=NZXOLMgkUrQ1LB7kPukD3z3qjtJnR6Dmw-QrL1S9QzwoSrDpN0gjizt4cnsN6mWsjT9k-puUl2iM9nlJCUd70vkPEJEhM6GkOEOGadYQ38Eh4IJN-j2rbiVtdCJsDRRfR8o8_PHyFDA2EUb2TQ2OWwXZzpV-CGBrVVFuBRunsfze3jj8Y9WnZiQvZ9ha4i8lgI0dbcaBjQzEVRKaXL7IDN6267c15TCFa_TxuTgw1SMi0xlGJausNi45CuSeNTqoQ0uv_ga4IA6uq2zXVHNY0PD9eT1PSEdjtSmGbCael-Hf45TReaL7asRc7MkaV_dL96sp5Vr15cIb6bX2to8e5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/76c3174d20.mp4?token=NZXOLMgkUrQ1LB7kPukD3z3qjtJnR6Dmw-QrL1S9QzwoSrDpN0gjizt4cnsN6mWsjT9k-puUl2iM9nlJCUd70vkPEJEhM6GkOEOGadYQ38Eh4IJN-j2rbiVtdCJsDRRfR8o8_PHyFDA2EUb2TQ2OWwXZzpV-CGBrVVFuBRunsfze3jj8Y9WnZiQvZ9ha4i8lgI0dbcaBjQzEVRKaXL7IDN6267c15TCFa_TxuTgw1SMi0xlGJausNi45CuSeNTqoQ0uv_ga4IA6uq2zXVHNY0PD9eT1PSEdjtSmGbCael-Hf45TReaL7asRc7MkaV_dL96sp5Vr15cIb6bX2to8e5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شب گذشته نیروهای آمریکایی و عربستان سعودی در عملیاتی مشترک، مواضع گروه‌های مسلح همسو با جمهوری اسلامی در شرق عراق را هدف قرار داده‌اند.
@
VahidHeadline
بر اساس گزارش‌ها، پایگاه‌های حشد شعبی در استان‌های دیاله، کرکوک، کربلا و نینوا هدف حمله قرار گرفته‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 291K · <a href="https://t.me/VahidOnline/77615" target="_blank">📅 16:52 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77614">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bdtAsKhrHiAfLsLHcr3fgEW-Et_u3cnFl2yjkDqv3iEq6r0iovBr_43rd3Y-MHCWLQWomjadgITqCHHHYUXPBgm64YdIfG7zWLu3yBYbZ6j24Cz6b-0SZ6KfjXORafwcm2v0s4rRZYf29PXzV_rKZ23G1cVXUqLcJZDMG6Cc4NEBdpVlfDSskvjN89DCvd51G-SLbJHQZmkHXSvDnkFRdrSrOAhprmHhh7qkPQ1QTVZhh7uiAvMlpirW3HHAClaVLLWThEo5KKTz1So_lE_VBEVMBwtWEVJKhYA4UcXush417I39ovRtkkE3zI0sOh7SES0NrSnI57s3_lARFL7flA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنای آمریکا با ۸۶ رأی موافق در برابر ۱۲ رأی مخالف، طرحی را به مرحله بعد فرستاد که در کنار تشدید فشار اقتصادی بر روسیه، تحریم‌های مرتبط با ایران را تا سال ۲۰۳۱ تمدید می‌کند.
این طرح که به نام لیندزی گراهام، سناتور جمهوری‌خواه درگذشته، نام‌گذاری شده است، هنوز باید در رأی‌گیری نهایی سنا تصویب و سپس در مجلس نمایندگان بررسی شود.
@
VahidHeadline
و  در خبری دیگر:
دفتر کنترل دارایی‌های خارجی وزارت خزانه‌داری آمریکا (OFAC) اعلام کرد ۱۰ شرکت و هشت نفتکش را به فهرست تحریم‌های خود افزود.
این تحریم‌ها بر اساس فرمان اجرایی ۱۳۹۰۲ و در ارتباط با جمهوری اسلامی اعمال شده‌اند.
در میان نهادهای تحریم‌شده، «اداره خدمات دریایی هرمزسیف» و «شرکت بیمه دریایی خلیج فارس» در ایران نیز قرار دارند.
وزارت خزانه‌داری آمریکا همچنین اعلام کرد این دو نهاد مشمول تحریم‌های ثانویه هستند.
شرکت‌های تحریم‌شده در هنگ‌کنگ، جزایر مارشال و چین ثبت شده‌اند و نفتکش‌های تحریم‌شده نیز با پرچم کشورهای مختلف فعالیت می‌کنند. این نفتکش‌ها به شرکت‌های تازه تحریم‌شده مرتبط معرفی شده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 282K · <a href="https://t.me/VahidOnline/77614" target="_blank">📅 16:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77613">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uv3HPnRS5w5rsgZ8s4JT-Ob9rrUrzOZRbAkIJMj1__gMU4kFyKzRLn5BjDQbW9a0j-yGBpGhqvDKGPgJ6r94xXqeRutUQP6CX0h3ZY3FoOUnKIHHF_Bokp_90lESU1rqpMZ7vpQg4WoKs6dKXNVvOxmeOGsep8TYXLfvxeOAZCr_cvm4XgFeDMoiQHKjcdvVxCFlLygXLUKkE2yBZCAwaK2XBbOduQ1AGpGuvG6MKw6Ok6pjlNlnIArWZMdA7mKpoNhTnrDW-U8EwzbGsz2E9Ozz3xq5wenuwU_pukozOh6M3uJGJ9e2FqLbj7PSdT0yIuhD3554JprLhlQUZ6RiiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رویترز به نقل از منابع منطقه‌ای گزارش داد که حوثی‌های یمن در حال بررسی طرحی برای دریافت عوارض از کشتی‌های تجاری عبوری از تنگه باب‌المندب هستند؛ اقدامی که به گفته این منابع، پس از اعلام محاصره دریایی عربستان سعودی مطرح شده و می‌تواند فشار بر آمریکا را افزایش دهد.
به گفته این منابع، حوثی‌ها در حال بررسی دریافت عوارض از بیشتر کشتی‌هایی هستند که از باب‌المندب، گذرگاه راهبردی میان دریای سرخ و خلیج عدن، عبور می‌کنند، اما هنوز زمان مشخصی برای اجرای این طرح تعیین نشده است. دفتر رسانه‌ای حوثی‌ها به درخواست رویترز برای اظهار نظر پاسخ نداد.
دو مقام منطقه‌ای که از سوی جمهوری اسلامی در جریان این موضوع قرار گرفته‌اند، به رویترز گفتند مقام‌های حوثی در سفر خرداد به ایران برای شرکت در مراسم تشییع جنازه علی خامنه‌ای، درباره دریافت عوارض از کشتی‌های عبوری از باب‌المندب با مقام‌های جمهوری اسلامی گفت‌وگو کرده‌اند. به گفته منابع، هدف از این طرح عادی‌سازی دریافت عوارض از آبراه‌های بین‌المللی و افزایش فشار بر آمریکا است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 294K · <a href="https://t.me/VahidOnline/77613" target="_blank">📅 16:47 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77612">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V2x75_fwyP2g6gUgTfk5Rg0xa56RmBLtvM-FLn0YUc36S3iF4W905CR6QRFrq88vF_VZ7WlFhP9uGzA0VjrG-fYMT8ChmRrJGAqp-CotCyol_DxoahQZSDkQXF12R3_U0juxNrGu_ZWJEx1U7Y9GE5KQKatE3l9PzLyCIA4eqQ7Mej_V-arKalZdmXMqjTMk4U5AYxkVxS1udYQhEej53w9wm-OUIJkOf3iGNtzTQ36pV0gi3VLTj5Q9zK3jaq5B-aHtPoAtLSk-c04BgvgOoRVTuXDlw5NON3U4lp_qkckVQatqC0dKWcGUZ4UcxBYga-z8Y3eJ3I6ZQqn4kFJR1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلویزیون دولتی جمهوری اسلامی گزارش داد منطقه‌ای در نوار مرزی پیرانشهر در استان آذربایجان غربی هدف حمله هوایی آمریکا قرار گرفته است. در این گزارش آمده است: «منطقه‌ای در نوار مرزی پیرانشهر مورد حمله هوایی دشمن آمریکایی قرار گرفت.»
پیش از آن، خبرگزاری فارس به نقل از یک مقام استان آذربایجان غربی گزارش داده بود موشکی به منطقه‌ای غیرمسکونی اصابت کرده و تلفاتی بر جای نگذاشته است.
فرماندهی مرکزی آمریکا تاکنون این حمله را تأیید نکرده و درباره آن اظهار نظری نکرده است. تأیید مستقلی نیز برای این گزارش وجود ندارد.
پیرانشهر در غرب استان آذربایجان غربی و در نزدیکی مرز عراق قرار دارد. این شهر پنج روز پیش نیز بر پایه گزارش سازمان مدیریت بحران استان به خبرگزاری ایرنا، هدف حمله هوایی قرار گرفته بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 270K · <a href="https://t.me/VahidOnline/77612" target="_blank">📅 16:46 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77611">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h_rI3fFesIDOdaBU0gUFU7YVXB3UoJJmgeR7bNnHgtCG3RuPWFm6M8_LQdVz7mtSeQARH1Tu1UzxCddUjSWnpf7P9s9ZI4YG8C2YmQ2WMvp-dEHGFEkb8Qoh03x1cY-tQiRqmJXuWN08JCQFxaWofExrWUl_nHaGvUkelfUoOxE2s2jTAlEFEtAx7dtl3cTBzUSDMqe9H527Ny3sf2OluyhRJKaN9wcXSp5oNYt2hQ-lEytGxH2_YD81ylsC84yiSBzkafaJ51R399ak5J9fkkYuwOeKyJvV6YYkK4TMTL-wWpJgpB-ktb9bcZHjrYrYQ8kO0idgNHzEpsx1SlaAiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقتدی صدر، رهبر جریان صدر عراق و از رهبران شیعیان عراق، با انتشار بیانیه‌ای از سپاه پاسداران خواست خاک عراق را هدف حملات خود قرار ندهد و هم‌زمان از گروه‌های مسلح عراقی نیز خواست با اقدامات خود به کشورهای منطقه بهانه حمله ندهند.
صدر در این بیانیه که روز چهارشنبه هفتم مرداد منتشر شد، نوشت عراق نباید به محلی برای هدف قرار دادن جمهوری اسلامی تبدیل شود و از «برادران در سپاه پاسداران» خواست از حمله به «سرزمین مقدس و مستقل عراق» خودداری کنند.
او همچنین از آنچه «میلیشیاهای خودسر» خواند، خواست با اقدامات خود زمینه حمله کشورهای عربی خلیج فارس به عراق را فراهم نکنند.
رهبر جریان صدر با محکوم کردن هدف قرار گرفتن خاک عراق از سوی هر کشور یا هر طرفی، از دولت بغداد خواست حاکمیت خود را اعمال کند، امنیت را برقرار سازد و مانع کشیده شدن این کشور به جنگ و درگیری‌های فرقه‌ای شود. او تاکید کرد عراق و مردمش بیش از هر چیز به صلح نیاز دارند و سال‌ها جنگ، توان و ظرفیت‌های این کشور را فرسوده است.
این بیانیه در شرایطی منتشر شده که از آغاز جنگ ۴۰ روزه، سپاه پاسداران بارها مواضع احزاب کُرد در اقلیم کُردستان عراق را هدف قرار داده است. هم‌زمان، فرماندهی مرکزی ارتش آمریکا (سنتکام) بامداد چهارشنبه هفتم مرداد اعلام کرد نیروهای آمریکایی و عربستان سعودی در یک عملیات مشترک، مواضع گروه‌های مسلح همسو با جمهوری اسلامی در عراق را هدف قرار داده‌اند.
@
VahidHeadline
مقتدی صدر در بیانیه‌اش به جای خلیج فارس از عبارت دیگری استفاده کرده:
Mu_AlSadr
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 284K · <a href="https://t.me/VahidOnline/77611" target="_blank">📅 16:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77610">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ft5bsW51lxcUbrLt1-nntcMpd8ZugKQQoJatrgUP-_uOvKSnm9A-ArT9yEJFwLmm2tae5ekF5INFDBBhLcspdKiF6kBd5YIpSpsCrdELkYLM7CwzE3aq6ZNoXZ69Nbn2_T8EcKio4wMD7U_90Pt31sg1wr-sqgGUXIaURuTD-bJkvQBGjMogvRWUzvkYO76szQ_ePne_NGTiBmtDQ0Lb4Qsj8zzxz6wuHMDH2hjuAAGHsiCrGMhSUmHajOmzLCGUyKM6pNAbuwHHtKvHxpq90k3IpXBXf-OA-yqzmKaxoUegleHBJ_gRDM5O3c5wjY3IGvlyBCq4lgjF4sp3XG8QSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامهٔ نیویورک‌تایمز، به نقل از چند مقام ایرانی و غربی که نام‌شان اعلام نشده، گزارش داد که حکومت ایران قصد داشت در واکنش به حملهٔ اوکراین به یک کشتی ایرانی، به یک بندر در اوکراین حمله کند، اما به‌دنبال اقدامات دیپلماتیک از انجام این اقدام خودداری کرد.
این روزنامه به نقل از این مقام‌ها نوشته است که انتظار می‌رفت ایران در این حمله یک موشک بالستیک با کلاهک کوچک به سمت اوکراین شلیک کند تا خسارت نسبتاً کمی به بار آورد و به‌صورت نمادین پاسخی به حملهٔ اوکراین داده باشد. این مقام‌ها گفتند که هدف حمله احتمالاً یکی از بنادر اوکراین در دریای سیاه بود.
بر اساس این گزارش بامداد چهارشنبه هفتم مرداد منتشر شد، مقام‌های جمهوری اسلامی امیدوار بودند این درگیری با حملهٔ تلافی‌جویانهٔ آن‌ها پایان یابد، اما مقام‌های غربی هشدار دادند که پیش‌بینی چگونگی واکنش اوکراین دشوار است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 255K · <a href="https://t.me/VahidOnline/77610" target="_blank">📅 16:44 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77608">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ADkSnemhyg7gO6XkELSkq4kZHbqwhopSITcGjquzBGjsPTMFhRoI5rn3FutcXKTq55BnpW_h9jfUBbQqMiSzpJrgbHBVKUVOyM-_mNPJjlQcACTk9ELbmEip5UuYyMz-r1flo0KJSoS_kC6aFJrjgn45wmcZALF70bTsdaYjsD7RzIcsXyx9btW1FOuY8wOumIdDMbQVkfpjmtXR9jpRZWi6MBQyJgJbBY_cpXd_EyfMpZoKcL4cDJRYBDW9IzBvEJ0Gt4a-3wJKa0johCNAPQITTMRItfyF5Ir6rtDrVPIOoKUaDkzoqCuN4ovlldio6bdAb6GjP2T2MqZ5DetQ5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ikiLtIGM_f41tZoYaip9WxIeJ_qQh8vafSXdXgrANvY-6xqqU3msyxlxhL5s7HxU5jldUjGhhVAeh1QBgOcPle_LLfi4Mt-3unIFY_OBXR5uew8p986LcY92Xh8KgLzcuwkuhPjCVFeqBcDJQvuY3x7ppm8VkYo0FPKE9FOwSOSblZIqFI8dCRwTkqwJAEG1IeU5HGMHo3DVNC6E44r1O-F5BWcsD6Yt-o4f0I6_rkWRWeFr_W9A4a088wuFY4_hlpYOteK0latDjao933EE1F2SxYZEa7442RQGgE7b54kif-qiCwzcflW3k2w6H2MQo47ZHwFEBxNfs9-EqJy9lw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برخی رسانه‌های ایران و کانال‌های مرتبط با سپاه پاسداران گزارش دادند که چهار عضو سپاه پاسداران در حملات منتسب به آمریکا و عربستان سعودی به عراق کشته شدند.
به نوشته این رسانه‌ها، این افراد در حمله‌ای به کربلا جان باختند.
بر اساس این گزارش‌ها، علی اصغر آستانه، ابوالفضل متقی، مرتضی اکبری و امیرعباس درهم‌فروش از جمله کشته‌شدگان هستند.
@
VahidOOnLine
شبه‌نظامیان حشد‌ الشعبی صبح چهارشنبه هفتم مرداد اعلام کردند شمار کشته‌های حملات هوایی مشترک آمریکا و عربستان سعودی به پایگاه‌های این نیروهای تحت حمایت ایران به ۲۰ نفر رسیده است.
حشد الشعبی در بیانیه‌اش این میزان تلفات را آمار «اولیه» خوانده و گفته است که دست کم ۳۲ نفر نیز در این حملات مجروح شده‌اند.
حملات مشترک آمریکا و عربستان علیه مواضع نیروهای حشد الشعبی در بغداد، واسط، نینوا، بصره، کرکوک، کربلا و دیاله انجام شد و خسارات مادی به تأسیسات و تجهیزات نظامی نیروهای حشد الشعبی وارد کرد.
فرماندهی مرکزی ارتش آمریکا در بیانیه‌اش گفته بود که این شبه‌نظامیان طی روزهای اخیر بیش از ۲۴ حمله پهپادی انجام داده‌اند.
به‌گفتهٔ سنتکام، هدف این حملات «تروریست‌های همسو با ایران» بوده است که سپاه پاسداران انقلاب اسلامی آن‌ها را برای حمله به نیروهای آمریکایی و زیرساخت‌های انرژی عربستان سعودی هدایت کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 264K · <a href="https://t.me/VahidOnline/77608" target="_blank">📅 16:37 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77607">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c924ab1dab.mp4?token=WuyGAwu6VqIMv_AJnCjkNBeL9fWa9l3XeTFQco_WPDw-AjdEOOEf1a4dv7UsAWEENnfJpVdONamHKj-6mIAWIw7bOXTVC6tfcMxqEKDw1I652KB5LZGeDNcq_UdeEkEz4SpedSHQNGh2y6V5DXDuMj6dx2fUu19lrGFbd8zzG2TCDZch2e-nMyrV4bwFparQAMVZVVmkk9VcHDWM0p-lmiwedIejrFxeQvUddIuIB6OP6fGiZMPRJwpWdVmNib5WN6X2i9MkJJqEWWIBW8nPsGzTAcbtt3tkFM1AfFkLaaIPfJxK6Fqoxy62lMmMOsRQ8c7cQaKvYHe6WN5gbH7OL5qenDLnEcoktN1YrJ9h5Nr6zJEqiq7XzambOylm0FE8hqfKj05obxxcg6TJpy2KNZV6Yciye1CA5JJ2ehb7zxeBPIZQSpMGm2n0JSuEOp4aS8bwuzVw2agjfZfsHC-4MtbllRhaWgFn9zbt1oxtQWxOcPIewNTzULFzuNwqktCXupA-N0epSKMrHDoQhsbwSsgttcKzhcKhs1YwIk2IZZgco33P3GTuxoU6VY5YuDOdGSVvGJWvDxWl00gKGo3emiuCWzGwfo-aFa9Uv8U3fB30gH2d9aNnb8QXKV9mJ1ni1BUTduz3Bejv0Th2O63_IONP6xWCvJtOIf1K7pNWWTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c924ab1dab.mp4?token=WuyGAwu6VqIMv_AJnCjkNBeL9fWa9l3XeTFQco_WPDw-AjdEOOEf1a4dv7UsAWEENnfJpVdONamHKj-6mIAWIw7bOXTVC6tfcMxqEKDw1I652KB5LZGeDNcq_UdeEkEz4SpedSHQNGh2y6V5DXDuMj6dx2fUu19lrGFbd8zzG2TCDZch2e-nMyrV4bwFparQAMVZVVmkk9VcHDWM0p-lmiwedIejrFxeQvUddIuIB6OP6fGiZMPRJwpWdVmNib5WN6X2i9MkJJqEWWIBW8nPsGzTAcbtt3tkFM1AfFkLaaIPfJxK6Fqoxy62lMmMOsRQ8c7cQaKvYHe6WN5gbH7OL5qenDLnEcoktN1YrJ9h5Nr6zJEqiq7XzambOylm0FE8hqfKj05obxxcg6TJpy2KNZV6Yciye1CA5JJ2ehb7zxeBPIZQSpMGm2n0JSuEOp4aS8bwuzVw2agjfZfsHC-4MtbllRhaWgFn9zbt1oxtQWxOcPIewNTzULFzuNwqktCXupA-N0epSKMrHDoQhsbwSsgttcKzhcKhs1YwIk2IZZgco33P3GTuxoU6VY5YuDOdGSVvGJWvDxWl00gKGo3emiuCWzGwfo-aFa9Uv8U3fB30gH2d9aNnb8QXKV9mJ1ni1BUTduz3Bejv0Th2O63_IONP6xWCvJtOIf1K7pNWWTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
بنیاد عبدالرحمن برومند از ابتدای سال ۲۰۲۶ تاکنون، اعدام دست‌کم ۸۸۶ نفر در ایران را مستند کرده است که ۵۶ مورد آن تنها در ماه ژوئیه انجام شده است.
🔸
زندان قزل‌حصار یکی از بالاترین آمار اجرای احکام اعدام را در سراسر کشور دارد. همچنین بخش قابل‌توجهی از اعدام‌های صورت‌گرفته در ایران مربوط به جرایم مرتبط با مواد مخدر است؛ به‌طوری که طبق داده‌های گردآوری‌شده توسط بنیاد عبدالرحمن برومند، نزدیک به ۴۵ درصد (۲,۹۴۶ مورد) از کل اعدام‌های ثبت‌شده در بازه ۱۰ ساله ۲۰۱۶ تا ۲۰۲۵، مرتبط با مواد مخدر بوده است.
🔸
از ۲۲ تیرماه، در پی انتقال شش زندانی محکوم به اعدام در پرونده‌های مواد مخدر به سلول‌های انفرادی زندان قزل‌حصار، جمعی از زندانیان واحد دو این زندان دست به اعتصاب غذا زده و برخی نیز لب‌های خود را دوخته‌اند.
🔸
با گذشت بیش از دو هفته از آغاز این اعتصاب، مسئولان نه تنها هیچ پاسخی به خواسته‌های اعتصابیون نداده‌اند، بلکه با اقداماتی همچون جابه‌جایی زندانیان و ایجاد محدودیت‌های شدیدتر برای جلوگیری از ارسال پیام و ویدیو از داخل زندان، در تلاش‌اند صدای آنان را خفه کنند.
#نه_به_اعدام
@IranRights</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/77607" target="_blank">📅 16:36 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77606">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">رویترز: منابع می‌گویند ایران ظرف چند هفته سامانه‌های موشکی دوش‌پرتاب چینی دریافت خواهد کرد
▪️
منابع می‌گویند قرارداد شامل ۳۰۰ تا ۴۰۰ سامانه پدافند هوایی دوش‌پرتاب QW-12 و FN-16 است
▪️
منابع می‌گویند ارزش این معامله ۶۰ تا ۷۰ میلیون دلار است
▪️
چین این گزارش را بی‌اساس خوانده و پاکستان دخالت در انتقال‌ها را رد کرده است
ترجمه ماشین:
۲۹ ژوئیه (رویترز) — سه منبع آگاه از این معامله به رویترز گفتند ایران قرار است ظرف چند هفته نخستین محموله از مجموع حداکثر ۴۰۰ پرتابگر موشک پدافند هوایی دوش‌پرتاب ساخت چین را دریافت کند؛ اقدامی که هم‌زمان با بازسازی توان دفاعی این کشور در میانه جنگ با ایالات متحده صورت می‌گیرد.
این خرید که ارزش آن ۶۰ تا ۷۰ میلیون دلار برآورد شده، یکی از بزرگ‌ترین تلاش‌های شناخته‌شده تهران برای تقویت پدافند هوایی کوتاه‌برد خود از زمان آغاز جنگ با آمریکا و اسرائیل است؛ جنگی که ضعف‌هایی را در توانایی ایران برای حفاظت از مراکز نظامی و زیرساخت‌های راهبردی آشکار کرد.
با خبرنامه Trading Day، تحولات بازارهای جهانی را بهتر درک کنید. از اینجا ثبت‌نام کنید.
به گفته منابع، این قرارداد خرید بین ۳۰۰ تا ۴۰۰ سامانه پدافند هوایی قابل‌حمل توسط نفر (MANPADS)، شامل موشک‌های چینی QW-12 و FN-16 را در بر می‌گیرد.
این قرارداد با شرکت Zhongqing Baoshang International Investment، مستقر در هنگ‌کنگ، امضا شده است؛ شرکتی که به گفته منابع، به‌عنوان واسطه میان طرف ایرانی و تأمین‌کننده چینی عمل می‌کرد.
ایران پس از ماه‌ها جنگ نیاز به تجدید تسلیحات دارد
منابع به‌دلیل حساسیت موضوع، به شرط ناشناس ماندن صحبت کردند. وزارت امور خارجه ایران بلافاصله به درخواست اظهارنظر پاسخ نداد.
وزارت امور خارجه چین اعلام کرد: «گزارش‌های مربوطه کاملاً بی‌اساس هستند. چین همواره در جهت ترویج صلح و پایان دادن به درگیری نقش ایفا کرده است.»
گروه Zhong Qing Bao Shang مستقر در پکن، شرکت مادر Zhongqing Baoshang International Investment، تا روز سه‌شنبه به درخواست اظهارنظر ایمیلی پاسخی نداده بود.
ایران پس از ماه‌ها درگیری، که طی آن آمریکا و اسرائیل تأسیسات مرتبط با برنامه‌های موشکی، پهپادی و پدافند هوایی این کشور را هدف قرار داده‌اند و تهران نیز با شلیک انبوه موشک‌های بالستیک و پهپادها پاسخ داده، نیازمند تجدید تسلیحات است.
این درگیری دشواری دفاع از مراکز ثابت نظامی و راهبردی در برابر هواپیماهای پیشرفته و تسلیحات هدایت‌شونده دقیق را برجسته کرده است.
واشنگتن روز شنبه به‌طور ناگهانی بمباران‌های دو هفته‌ای خود را متوقف کرد، اما دونالد ترامپ، رئیس‌جمهوری آمریکا، گفت اگر مذاکرات برای پایان دادن به این درگیری پنج‌ماهه شکست بخورد، حملات از سر گرفته خواهد شد؛ درگیری‌ای که در ظاهر از ماه آوریل در وضعیت آتش‌بس قرار داشته است.
تحویل صدها سامانه پدافند هوایی دوش‌پرتاب، موجودی تسلیحات پدافند هوایی کوتاه‌برد ایران را به‌طور قابل‌توجهی افزایش خواهد داد و نشان می‌دهد روابط نظامی این کشور با چین در حال عمیق‌تر شدن است.
منابع هشدار دادند که هرچند توافق امضا شده است، برنامه زمانی تحویل، تعداد سامانه‌ها و دیگر جزئیات اجرایی همچنان ممکن است تغییر کند.
بر اساس طرحی که طرفین بر سر آن توافق کرده‌اند، تحویل‌ها در مرحله نخست از طریق هوایی و از ارومچی در غرب چین انجام خواهد شد و سپس با عبور از پاکستان به ایران خواهد رسید. منابع مشخص نکردند که انتقال از پاکستان به ایران هوایی خواهد بود یا زمینی.
روابط عمومی ارتش پاکستان، ISPR، اعلام کرد: «گمانه‌زنی‌ها درباره دخالت پاکستان در انتقال تسلیحات پدافند هوایی از چین به ایران کاملاً ساختگی و نادرست است.» سخنگوی وزارت امور خارجه پاکستان به درخواست‌ها برای اظهارنظر پاسخ نداد.
منابع می‌گویند چین و ایران مسیرهای زمینی برای تحویل را بررسی می‌کنند
کارشناسان نظامی می‌گویند با آنکه ایران طی دو دهه گذشته سرمایه‌گذاری گسترده‌ای در زمینه موشک‌ها، پهپادها و رادارها انجام داده است، سامانه‌های پدافند هوایی قابل‌حمل اهمیت دارند، زیرا می‌توان آن‌ها را به‌سرعت پراکنده کرد، با تیم‌های کوچک به کار گرفت و مرتباً جابه‌جا کرد؛ ویژگی‌هایی که آن‌ها را در مقایسه با آتشبارهای ثابت پدافند هوایی کمتر آسیب‌پذیر می‌کند.
یک منبع امنیتی اروپایی گفت مقام‌های کشورش از چند قرارداد در حال مذاکره درباره فروش احتمالی سامانه‌های پدافند هوایی دوش‌پرتاب سری QW به ایران، از جمله سامانه‌های QW-12، QW-18 و QW-19، اطلاع دارند.
یک منبع امنیتی دوم در خاورمیانه گفت ایران به‌دنبال خرید موشک‌های QW-12 و QW-18 بوده است، اما او از نهایی شدن قرارداد اطلاعی نداشته است.
‏QW-12 و FN-16 سامانه‌های موشکی زمین‌به‌هوای دوش‌پرتاب و هدایت‌شونده با فروسرخ هستند که برای درگیری با هواپیماهای در ارتفاع پایین، بالگردها و پهپادها طراحی شده‌اند. قابلیت تحرک آن‌ها امکان استقرار سریع در اطراف تأسیسات نظامی، زیرساخت‌های انرژی و دیگر مراکز حساس را فراهم می‌کند.
تحلیلگران دفاعی QW-12 را ضعیف‌تر از مدل‌های جدیدتر خانواده QW، از جمله QW-18 و QW-19، می‌دانند، اما می‌گویند این سامانه‌ها همچنان می‌توانند لایه‌ای مؤثر از حفاظت کوتاه‌برد در برابر پهپادها و اهدافی که در ارتفاع پایین پرواز می‌کنند فراهم کنند.
دو منبع اطلاعاتی غربی و یک مقام ایرانی گفتند تهران همچنین استفاده از مسیرهای زمینی را برای انتقال محرمانه‌تر تجهیزات نظامی و قطعات دومنظوره چینی و کاهش خطر ایجاد اختلال در انتقال بررسی کرده است.
این خرید نشان‌دهنده تداوم اتکای جمهوری اسلامی به ترکیبی از تولید داخلی تسلیحات و تأمین‌کنندگان خارجی، با وجود سال‌ها تحریم و محدودیت بر واردات مرتبط با امور دفاعی، است.
رویترز پیش‌تر به نقل از افراد آگاه از مذاکرات گزارش داده بود که ایران به امضای توافق جداگانه‌ای با چین برای خرید موشک‌های کروز ضدکشتی نزدیک شده است. رویترز نتوانست مشخص کند که آیا آن توافق نهایی شده است یا نه.
reuters
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 419K · <a href="https://t.me/VahidOnline/77606" target="_blank">📅 08:07 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77605">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IjZosv_YmXv3iU_l-8ZqORC6PkgAiU6wifRCiXwTsJbP85Cl82HZjTpFs2Qq2St9m_6e0QNG2C6E5Wemoc1nyrVLp7GqA61AQ--pukYNOwp4lVeX6PuRJXwSOPcbWkZEuNC08C50nX3OeQUgKTJbIf88XN3fSbrB8ecJ1JAdk8NtkBoKD7AA7yMhwTK_SHnz1ZdqJH0zTqEa1uUirw9Js_of9nB5KA7NCFpCUT18vlNbFrO_W5WKiZvIzWuYhRnoZdwWEPN6kkkh46uRh2cwCFSG7s7t1Acne5LEX7bT-7IWCCSj8AkiwI8Rdw4XYAN9A5yPkvoTHCNwL_aL_HJaig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روابط عمومی ارتش جمهوری اسلامی ایران هویت خلبان کشته شده مجید کاظمی رو پس از چند ماه اعلام کرد.
نوشتند یکی از ۴ خلبان دو جنگنده سوخو ۲۴ بوده که در حمله به نیروهای آمریکایی در پایگاه العدید قطر هواپیماشون مورد هدف قرار گرفت.
نوشتند تلاش‌ها برای تعیین وضعیت ۳ نفر دیگر همچنان در جریان است و مجید کاظمی هم با آزمایش‌های تخصصی و بررسی DNA هویتش تایید شده.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 404K · <a href="https://t.me/VahidOnline/77605" target="_blank">📅 07:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77604">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G4bAh9enhwMoqOxo6Mof8gZjCJOxUZA8aovJNl26PR9NNHlmNvntKVEXCNh8bTuh53XpukTYDx8wxkdouHSdgsrBKXxc9LKAVreV9LsTKpObvxJYOyWyLOVDd5TIoZZ9vvaTTtodsOp4aL0eIyniKZla1lJsFKE-49WEg-5h5K5RyPOtrdqxCrh06LKXXVs0NKkvOq54DIJWZz3YWz88R0X0DJuXuN-wrcC4zMSn28_8C2gdIYKtPXL639yqCGpHcBziMUM2wbR8WeTVNOvzOwJxqG9PnaPAeQ3fEYUG9bIrVJVUHiY1HZD2JJOIQ3SehWRSah5lwURC4WxjNn8W2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه پاسداران، صبح چهارشنبه، با انتشار دو بیانیه از حمله موشکی به پایگاه هوایی و مرکز فرماندهی ارتش آمریکا در اردن و همچنین هدف قرار دادن سه نفت‌کش خبر داد.
نیروی هوافضای سپاه اعلام کرد پایگاه نیروهای آمریکایی در اردن را با چند موشک بالستیک هدف قرار داده و هم‌زمان نیروی دریایی سپاه نیز گفت: «سه نفت‌کش متخلف که به اخطارها بی‌توجه بودند مورد اصابت قرار گرفته و متوقف شدند.»
این درحالی است که پیش از این، فرماندهی مرکزی ایالات متحده (سنتکام) با انتشار بیانیه‌ای اعلام کرد که تمام موشک‌های شلیک‌شده سپاه از ایران به طور کامل رهگیری و منهدم شده‌اند و هیچ آسیبی به نیروهای آمریکایی وارد نشده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 392K · <a href="https://t.me/VahidOnline/77604" target="_blank">📅 05:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77603">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ولودیمیر زلنسکی، رئیس‌جمهوری اوکراین، می‌گوید دونالد ترامپ، رئیس‌جمهوری آمریکا، با اعطای مجوزهای لازم برای تولید موشک‌های سامانه پاتریوت به اوکراین موافقت کرده است.
آقای زلنسکی شامگاه سه‌شنبه در گفت‌وگو با شبکه فاکس‌نیوز گفت پس از دیدار با آقای ترامپ، با نمایندگان چند شرکت بزرگ تسلیحاتی آمریکا نیز گفت‌وگو کرده و امیدوار است زمینه تولید مشترک این موشک‌ها فراهم شود.
رئیس‌جمهوری اوکراین که روز سه‌شنبه در واشینگتن با دونالد ترامپ دیدار کرد، تأکید کرد مهم‌ترین نیاز نظامی کی‌یف همچنان سامانه‌ها و موشک‌های دفاع ضدبالستیک است.
هم‌زمان، سنای آمریکا با ۸۶ رأی موافق در برابر ۱۲ رأی مخالف، طرح گسترده‌ای را برای تشدید فشار اقتصادی بر روسیه و ایران به مرحله بعد فرستاد. این طرح که به نام لیندزی گراهام، سناتور جمهوری‌خواه درگذشته، نام‌گذاری شده است، به رئیس‌جمهوری آمریکا اجازه می‌دهد بر بزرگ‌ترین خریداران نفت و گاز روسیه تعرفه‌هایی تا سقف ۲۰۰ درصد وضع کند و تحریم‌ها علیه نهادهای مالی، مقام‌ها، الیگارش‌ها و ناوگان موسوم به «سایه» روسیه را گسترش دهد.
این طرح هنوز باید در رأی‌گیری نهایی سنا تصویب شود و سپس برای بررسی به مجلس نمایندگان برود؛ مجلسی که تا پایان تعطیلات ماه اوت تشکیل جلسه نخواهد داد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 377K · <a href="https://t.me/VahidOnline/77603" target="_blank">📅 05:54 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77602">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z-1alz6NSi6RH8MJIp0gt84ZymtSzlVB8JIEEJ9j0mrEQL54ZaMwh7bG5YaNLyu6hCJB53RJwrNsN0t3Es3I7DRAfQ1E_P5LDq3iXo3XPHWAR15ExbaVxZdst6KjAf7wfV2GROwIPD0bsrkyuaO_aD3MqSk6gBHsjpq0tANLjkEH4Ib8aXw7KAN6KnTaCFSo_G9eabrSBaEHlVfVhyqhPi-GnjIkoK2E3n04lBMuyXT62svunaL-m_XAIdmhQHjKXqMVOYXvqGB3YdCavcosgF6rPTZrKuFuKV9r_WFxG97_Bs47IOeVF2z76_rfHX0iRhhGnQ3mQUTfT8esADFOSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، با انتشار تصاویری در «تروث سوشال» از دیدارهای جداگانه خود با رهبران اسرائیل و اوکراین، درباره دیدار با بنیامین نتانیاهو نوشت:
«نخست‌وزیر بی‌بی نتانیاهو از اسرائیل، همراه با من و نمایندگان، نشست بسیار خوبی داشتیم. بدیهی است که موضوعات مهم متعددی مورد بحث قرار گرفت.»
ترامپ همچنین با ابراز خرسندی از دیدار با ولودیمیر زلنسکی افزود: «دیدار با زلنسکی از اوکراین افتخار بزرگی بود. موارد زیادی بررسی شد و این نشست بسیار خوب پیش رفت.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 365K · <a href="https://t.me/VahidOnline/77602" target="_blank">📅 05:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77601">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iCKbwspFj_e4e5rf-3Xjt3oXP2j-IRWPO6azx39avkNHvhqWo5kfeBl9-hDptUnCuZu-OGxa4Wg8pLhDY77Ko2gG2OeTB9nQeStEpNXeMCKPDPS5D1RhRxwkJwwgEGxpCAM9Jtt_1RisGoFl-2_k-UreiBp-y8lHRgrK-ininKsObIiY7hgYzrkJPPsuThC6Yi3PiNJ-Gno4oXUlOEJ8TOkcWpKflTIKgMdfOeoqerCI7WzU7o1yL_JKNd__FGvoz-G2raiHbcGRareN5tNQhyldFhBeR6Csy1hLCJCt0rG6vjRyM4KNBXSfAbWbIR-FSOpInnDn-iC19Iy07puoVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر پست شده در اکانت سنتکام
متن پست، ترجمه ماشین:
نیروهای آمریکا و عربستان مواضع تروریستی مورد حمایت ایران در عراق را هدف قرار دادند
تامپا، فلوریدا — فرماندهی مرکزی ایالات متحده و نیروهای مسلح عربستان سعودی روز ۲۸ ژوئیه حملات دقیقی را در عراق علیه تروریست‌های همسو با ایران انجام دادند؛ عناصری که سپاه پاسداران انقلاب اسلامی آن‌ها را برای حمله به نیروهای آمریکایی و زیرساخت‌های انرژی عربستان هدایت کرده بود.
جنگنده‌های آمریکایی و سعودی در پاسخی قاطع به بیش از ۳۰ حمله پهپادی هوایی که طی ۷۲ ساعت گذشته به دستور سپاه پاسداران انجام شده بود، چندین مرکز لجستیکی و انبار تسلیحاتی تروریست‌ها را در سراسر شرق عراق هدف قرار دادند.
حملات ناموجه علیه نیروهای آمریکایی موفقیت‌آمیز نبود.
از فوریه تا آوریل ۲۰۲۶، شبه‌نظامیان تروریست همسو با ایران در عراق بیش از ۶۰۰ بار تلاش کردند به شهروندان و تأسیسات آمریکایی حمله کنند.
سپاه پاسداران و نیروهای نیابتی تروریستی آن باید برای جلوگیری از واکنش نظامی بیشتر ایالات متحده، این حملات را متوقف کنند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 353K · <a href="https://t.me/VahidOnline/77601" target="_blank">📅 04:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77600">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m1QHU6Yp8CECIa_6VqQ5Jt-n13D2kc1kU-mij7QRkafpDCfF-D6SnIAp9sPKKtajBN8gEW5H2t_JTdeN_LdbubsciaqSKaBnekf_Up8XJsyKaMNiHUo9Q7HEFFiwLE9Dy_00f8MaOAqaWjTyIv4p6yyc_WnfcTJZdXq8SO_b3LkE8WqmbUzf9m8xJQtXXMJIVk2p60oC52weG7GwTZYAaiyQibq-xbqzBep4mu7uA06zX6Qww9bywg6I3-576YheUEf7DuzVSYsYFpN6Pom--SfYTqTAy6zJXTcNb9P5YQ4oyb3sR5GB2s3eBPUoDtAwzn2eln7WECbDPBWHqdiTPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت دفاع عربستان سعودی اعلام کرد پدافند هوایی این کشور چند پهپاد را که تأسیسات نفتی در استان شرقیهٔ این کشور را هدف گرفته بودند، رهگیری و منهدم کرده است.
ترکی المالکی، سخنگوی وزارت دفاع عربستان، روز سه‌شنبه در شبکه اجتماعی ایکس گفت این پهپادها از خاک عراق و به دست گروه‌هایی که او «شبه‌نظامیان تروریستی مورد حمایت ایران» خواند، پرتاب شده بودند.
او افزود عربستان سعودی حق مشروع دفاع از خود و تأسیسات حیاتی‌اش را محفوظ می‌داند و «در زمان و مکان مناسب» به این حملات پاسخ خواهد داد.
@
VahidHeadline
خبرگزاری صدا و سیما می‌گوید که یک »مقام آگاه نظامی» در ایران، در واکنش به اظهارات وزیر دفاع عربستان سعودی، هرگونه ارتباط جمهوری اسلامی با پرتابه‌های شلیک‌شده از خاک دیگر کشورها به سوی اهدافی در عربستان را «قویاً» تکذیب کرده است.
این مقام که نام او اعلام نشده است، به این خبرگزاری گفت نسبت دادن هرگونه اقدام علیه منافع آمریکا در منطقه به جمهوری اسلامی ایران، «خطای بزرگ محاسباتی» و ناشی از «کم‌اطلاعی از اوضاع منطقه» است.
@
VahidHeadline
📡
@VahidOnline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 355K · <a href="https://t.me/VahidOnline/77600" target="_blank">📅 04:07 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77599">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gcHKfhdQpNVKqDm_jMRpyyMXetrjv0l36vbPP1X0xeDRZmfar6pqENWk0WDQnSZAKvrQ6HdPFcYXx2h5JGwGCLUNRA4_tFBf_0CiQxIvLJM-UGB4FCvba0camFPtUJPPM_R3Y9WcXvi24dR53vtDz7thsVQnOn7CE4f6f-fkjPra62Wt6bGqNb5hj9KOtMNpSNRBl6fI8OopsipCKX3MvTOzJSQ_b6hZZgksPogT2fE8uwVjnKpzimSTPnH6W9JnKSPdkI74Pmz2emKiLy711Xe3XOaFZ07YftZQFLPgRv6J9ByduZYZ0hk0pxSxYaSsdXQhITv5IkJDKr8kw-PuSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
امروز ساعت ۵:۴۵ بعدازظهر به وقت شرق آمریکا [۱:۱۵ چهارشنبه به وقت تهران]، نیروهای سپاه پاسداران انقلاب اسلامی چندین موشک بالستیک را از ایران، در تلاشی برای انجام حمله‌ای غافلگیرانه به نیروهای آمریکایی مستقر در خاورمیانه، شلیک کردند.
همه موشک‌های ایران با موفقیت رهگیری شدند.
نیروهای آمریکایی همچنان هوشیار و در بالاترین سطح آمادگی قرار دارند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 367K · <a href="https://t.me/VahidOnline/77599" target="_blank">📅 01:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77595">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sOraCgQhAjAjx3m-MjO5XcTqwPRfqrXTFaeVauapr30cB1t9CKpMUpFGat_QzKF1FDOQIL7hkP2wiGU5l51UAbQezYJawzUQDcbFLYo8rIUK5IbgWBb9uU9-BbbtBHk4rtYnuXgtsF0knNbMgIE7dYmuJlZsh-c2MCNcuzotRNQvJRSqtVtt6gBpTvv8-ZYjs5n44Z7pO_1QVX2HkDOKxc0v5M4-YdfrCuvol17fk7ZCw8WeoKQaby3zwTKBc_9d4_3qVe1j6AiaNOCDON_BqlTw2ZwHEcNOzvXwYyAF_2sBs75LWt1B7uqY7HgtBhh3lOnN_2gupcAtvPSn0ag-uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XcTHPe77Mc-6tAeAIc2Z5gjZTSh8Kj4i1SHaw0cNrQhjbTDiOQXcLpcDYfUwwJTdpTyqGuPThJ6NcWrn-Rg1uyB5sc2iWgwGJhO08o2ETOF1t30_dJQr7S9_KnLhK4_FXxEHwXI_nxMD_FITqawvgy_0z0sj-zIh9tXZDWsQPTiVTNU6wAQghZvY5lfciWN5MR_8myLMxwXAFiwbiw0VFw7XcDlnWFuhya4YYE-7wzRa-aM4Xl7nA7NAs-aZ9KdOFbp-_ExqaJFi9u7oKJm09TkJLXtA9iE7GxlSY9bzCPddbmSMNtELNw7oGrTAtsqvLLWIxDu-RVH7f7SeKVdJ3A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/41f8819418.mp4?token=fYEwIegk01HPQHSBXqjcGo4pckSpLHs8-83R8ckBgNa6zFrqrks6sVqwbKSV46HDXjERoN7SHLzobkRXea9G6n2H814VdoYeQFKsZCIBC_fKQtHdYhNgLyxsq1SitFU1kUvNhFkqaDV8_vNpAUsKU5FY2MfutqanRLgKT2NtV8NlR8g_h_hLgK2Pm9e3e3nrYOwqLaB37V_1p_Xj5bC92FnJHXFp8HICxqXF5zDuU4tZcFolii1sbmStyxtIGlyrDA8i1oCnJc5RG1GmsG7Uq3tRtXLaHId3HXVW9p_cgQNKFLbTZ95po2s1I8cqcUd41htlPWoeo75DnmnOZ3kqhA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/41f8819418.mp4?token=fYEwIegk01HPQHSBXqjcGo4pckSpLHs8-83R8ckBgNa6zFrqrks6sVqwbKSV46HDXjERoN7SHLzobkRXea9G6n2H814VdoYeQFKsZCIBC_fKQtHdYhNgLyxsq1SitFU1kUvNhFkqaDV8_vNpAUsKU5FY2MfutqanRLgKT2NtV8NlR8g_h_hLgK2Pm9e3e3nrYOwqLaB37V_1p_Xj5bC92FnJHXFp8HICxqXF5zDuU4tZcFolii1sbmStyxtIGlyrDA8i1oCnJc5RG1GmsG7Uq3tRtXLaHId3HXVW9p_cgQNKFLbTZ95po2s1I8cqcUd41htlPWoeo75DnmnOZ3kqhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">'پرتاب شدن چند موشک از
#خمین
'
تصاویر دریافتی از شهروندان با شرح بالا
چهارشنبه ۷ مرداد حدود ساعت ۱:۱۰ بامداد
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 361K · <a href="https://t.me/VahidOnline/77595" target="_blank">📅 01:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77594">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Zj2JgA4BsxE89lDh80mBgkIvRAN0F9flDfQiYJvxf25QKIOmFsiYfIjZT9-v1ny99OMYWy_Wq69WLHB0EJAqSntKun5vLfHntH-aMTvc5qRWDW_qlnb7iDvgWlEi7Y4KY2T8xjdzJi_i3_E6nDq59eD7wqNlICkUDoACZ1VCWiWUADBtfcGYtRnXTOz8v-2OOjGFapOVRZwXaR75VBMOio0AE6GEgIXXJefnDFq04D7VG4FjW3pP2qRaMZ4MvDYiDM9kU5owWJKH7fWpT2evZfTIqbE8eLP4vrRx2nakauv61itjRxhs9KviSj8-53sT94twRAbI9hl5UdHJWItscA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های دریافتی:
از خمین موشک بلند شد
سه تا صدای انفجار
همین الان از خمین ۶تا موشک زدن
۳تاشون صدا نداشت فقط نور قرمز بود
سلام همین الان یک موشک از خمین رفت.
داداش
خمین موشک زد
ساعت ۱ و ده دقیقه
وحید داداش ۴ تا موشک از خمین زدن همین الان
از خمین موشک زدن
سلام،الیگودرزم،،صدا ۳ شلیک موشک اومد صدا دور بود احتمالا ازخمین بود
پرتاب سه موشک خمین
سلام وحید جان
سه تا موشک تو آسمون لرستان از سمت اراک دیده شد
صدای انفجار تو آسمون لرستان میاد
من ستا موشک بین نهاوند و بروجرد دیدم خمین نبود فک کنم نتکنستم عکس بگیرم
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 374K · <a href="https://t.me/VahidOnline/77594" target="_blank">📅 01:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77589">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6b678bb6b2.mp4?token=D2dUpsD_WAn9KusjLwjLaWU50-GwNYJOuogZ3ew2S8_g18lj6oTIC8ebe9hxxRtqqmmNfgjth8hTiyEn4WQYQXt_xLmaScOp06UaKxO2sKw2_5fWRszynBJNIOZUR3d0_S1YHREA3OWQm228J1ds9hHb3Mq0b24Mm_RRYlJWSWzOLNWIhiVXHxWSin8EWs0kTbDhNJgHvYqklgrghijPqJIBh-3xFaFkayv9rZWa8IAeKGxq4tNSFkh5GHsDJwnJ3jqVDmfIsPT3hzpxcywnsAZnD_3Yzgxm7kcd4vFQoQ3y0iH5GwC1nKFDJM9YBIYZtnqqwc7pY4IYxOX1vNnmxg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6b678bb6b2.mp4?token=D2dUpsD_WAn9KusjLwjLaWU50-GwNYJOuogZ3ew2S8_g18lj6oTIC8ebe9hxxRtqqmmNfgjth8hTiyEn4WQYQXt_xLmaScOp06UaKxO2sKw2_5fWRszynBJNIOZUR3d0_S1YHREA3OWQm228J1ds9hHb3Mq0b24Mm_RRYlJWSWzOLNWIhiVXHxWSin8EWs0kTbDhNJgHvYqklgrghijPqJIBh-3xFaFkayv9rZWa8IAeKGxq4tNSFkh5GHsDJwnJ3jqVDmfIsPT3hzpxcywnsAZnD_3Yzgxm7kcd4vFQoQ3y0iH5GwC1nKFDJM9YBIYZtnqqwc7pY4IYxOX1vNnmxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مراسم ادای احترام به لیندزی گراهام، سناتور جمهوری‌خواه که ۱۱ ژوئیه در ۷۱ سالگی درگذشت، در ساختمان کنگره آمریکا
به غیر از نزدیکان آقای گراهام، صدها نفر از قانو‌نگذاران آمریکایی در مراسم حضور داشتند.
برخی از رهبران جهان هم برای شرکت در این مراسم به پایتخت آمریکا سفر کرده‌اند.
سناتور گراهام از ایالت کارولینای جنوبی بود که چهار بار به عضویت سنای آمریکا انتخاب شده بود. او در سال‌های ابتدایی فعالیت سیاسی خود از منتقدان سرسخت دونالد ترامپ، رئیس‌جمهور آمریکا، به شمار می‌رفت اما بعدها به یکی از متحدان وفادار او در کنگره بدل شد.
او از چهره‌های شناخته‌شده جریان محافظه‌کار و از مخالفان سرسخت جمهوری اسلامی ایران بود و زمستان گذشته در جمع مخالفان حکومت ایران در آلمان حاضر شده و سخنرانی کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 377K · <a href="https://t.me/VahidOnline/77589" target="_blank">📅 00:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77588">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pkUBYAtp-vwP-kV50Tq603UYjoIODY6s54dCR0GEAYaefjNT79e-ZEV5K1C5kt5xsFyzkxqF9LCdcEnt9SiY1yQaCia8_R7j4ziPzFOMf70nOIN5QUnFEn8v0qSK0rpTw_JjIR3dXSXY7B2SbHeMzMAObcqkMPfke40CyXhAV8y4DW1KeBFY-lnpKfq2qn1AoNe7_Xs8SlnbEKTlnoZXGcWb4CP_nj07u50c83xtDcwtnuMm0pObWL0mecuUMWoMc9JNknZRZqezNE-CNm7kRheXjmFKPUzTOr58F4VA2uL45pnG7TW25R_YKsUp4CfvBTfeDV2D9kg-16N2-3g9Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهنام نواب صفوی، ۲۲ ساله، خواننده رپ فارسی و از بازداشت‌شدگان دی‌ماه، از سوی شعبه پنجم دادگاه انقلاب اصفهان به ریاست قاضی همتی‌نژاد به اعدام محکوم شده است.
این حکم با اتهام «محاربه از طریق مشارکت در تخریب اموال عمومی، تبلیغ علیه نظام و اجتماع و تبانی» صادر شده است.
به گفته منبع این گزارش، مهنام نواب صفوی دو وکیل داشته، اما وکلای او به پرونده دسترسی نداشتند و امکان دفاع از او برایشان فراهم نشده است.
همچنین دادگاه او به صورت غیرحضوری برگزار شده است.
مهنام نواب صفوی در جریان اعتراضات دی‌ماه در اصفهان بازداشت شد و اکنون در زندان دستگرد این شهر  است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 384K · <a href="https://t.me/VahidOnline/77588" target="_blank">📅 23:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77587">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HXk2mRZCHVmh6W6bsTSli83pBq41B5h0bxB7qljafqOuhRkQIhm-3HWaKqxD5lVgiU89N2d5KdKD4TXkrL_79ZMwRUQ88YHTO6j5TnfMPtNvRyeQVqXZEZyu1KraT7fMYeeyD2hVjdqRVQsKpIAOhILx1qDxo6uWz22YIK-DCWdUO4JNlZ4w8l3ZpJLCsodVffsIKCGVIDfuSolLKi1x8OJHPzyOIpLrPG0aZL1kqJ7JX5ulxAfQK9LJP7In9WulntaF6ORxJABU8grl-WuDaM-t138J95Wf156U-fMNQpxOdOXVkoo_bAumhEbTen5-ms0jqcGgrZyndQ4jx306jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست وزیر خارجه اوکراین، ترجمه ماشین:  برای گفت‌وگویی صریح با وزیر امور خارجه ایران، @‌araghchi، تماس گرفتم. دیپلماسی یعنی گفت‌وگوی مستقیم، حتی زمانی که دشوار باشد. تأکید کردم که هدف ما جلوگیری از تشدید غیرضروری تنش‌هاست.  بار دیگر تأکید کردم که تمام اقدامات…</div>
<div class="tg-footer">👁️ 358K · <a href="https://t.me/VahidOnline/77587" target="_blank">📅 22:43 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77586">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/54fee52c22.mp4?token=Px3ZuDmnYUPDw7SBT715vBM8qELYGNpREkZtkt9_IO2r89cttcX0gosq5-TO2bFzdMRjjuf0keefMl6Ty2k97WXBv9Zbk9wGlXzI2sv5zcOwhhSyzhV-zOMi50J-4uRvlvUHBOFUttsgRJpV2MXd-hgF6hgN5j-kVI6ivW4fIsUXl6wfXViHqARE_Og1zkV_4AYGHSwusPO_mGCwWthMBZLRqal7IQwdwT7meh482lLUhQfIRYXj0qAp_0QlrqFfjL9nTKhSKb-NG0RjEBx-zW1cPe_lOQKc6K-l0V8suUfzWgEwkuOCpzCh_VO0lNgUPf_fJIgdN0tW9TXRtV7_MA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/54fee52c22.mp4?token=Px3ZuDmnYUPDw7SBT715vBM8qELYGNpREkZtkt9_IO2r89cttcX0gosq5-TO2bFzdMRjjuf0keefMl6Ty2k97WXBv9Zbk9wGlXzI2sv5zcOwhhSyzhV-zOMi50J-4uRvlvUHBOFUttsgRJpV2MXd-hgF6hgN5j-kVI6ivW4fIsUXl6wfXViHqARE_Og1zkV_4AYGHSwusPO_mGCwWthMBZLRqal7IQwdwT7meh482lLUhQfIRYXj0qAp_0QlrqFfjL9nTKhSKb-NG0RjEBx-zW1cPe_lOQKc6K-l0V8suUfzWgEwkuOCpzCh_VO0lNgUPf_fJIgdN0tW9TXRtV7_MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاظم غریب‌آبادی، معاون وزیر امور خارجه جمهوری اسلامی، روز سه‌شنبه اعلام کرد تهران پیشنهاد عمان برای تقسیم برابر مسیرهای عبور و مرور در تنگه هرمز را نپذیرفته و در مقابل، طرحی موقت برای بازگشایی این آبراه به مسقط ارایه کرده است.
غریب‌آبادی در گفت‌وگو با تلویزیون حکومتی ایران گفت عمان پیشنهاد داده بود مسیر کشتیرانی به گونه‌ای طراحی شود که ۵۰ درصد آن در اختیار ایران و ۵۰ درصد دیگر در اختیار عمان باشد، اما جمهوری اسلامی این طرح را ناکافی دانسته است.
او گفت: «ما گفتیم این موضوع رفع‌کننده نگرانی‌های ایران نیست.»
به گفته معاون وزیر خارجه، تهران در مقابل، طرحی موقت پیشنهاد کرده که بر اساس آن تردد کشتی‌ها در یک مسیر از آب‌های سرزمینی ایران انجام شود و بخشی از مسیر رفت و برگشت نیز در آب‌های ایران قرار گیرد.
غریب‌آبادی همچنین تاکید کرد سیاست جمهوری اسلامی این است که تنگه هرمز «هیچ‌گاه به وضعیت پیش از جنگ بازنگردد» و هشدار داد هر ناو اروپایی که به گفته او به تنگه هرمز نزدیک شود، «هدف مشروع» جمهوری اسلامی خواهد بود.
او افزود عمان همچنین پیشنهاد کرده بود کشوری برای مین‌زدایی از بخش جنوبی تنگه هرمز اعزام شود، اما تهران با این درخواست نیز مخالفت کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/77586" target="_blank">📅 22:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77585">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0bb06747b7.mp4?token=t7s5mVY9r0Fhcyv0FUmAyRnHR0AhdX8IvnSBE9kfoeOCmfOSqfySX9Q41i_xgpo0PNoKoOoHwqTKSACxye421JBJ2rQOK4FntOGTE2FS6TrI3wiebkclX2F_qnK_rMrAQ-XJ24p-LR5nx2L6k94OC5LWrlEoy2nIrinFLA1gg_b5aN5X0y3qaMVrpCL2NPiXr30IRTUYOhbm5MEiK5wl2Xeq9Lq4Wtta-XD6JqiPYuyHLzftq6fI8krdoLiooYwrf5ypOVKbNQt201fS5gul9SqN1XoO6pdjopunYYtskMuGU2AWztoVkE9sRKosBdMencr-VS19i28kLyKdMmB3lg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0bb06747b7.mp4?token=t7s5mVY9r0Fhcyv0FUmAyRnHR0AhdX8IvnSBE9kfoeOCmfOSqfySX9Q41i_xgpo0PNoKoOoHwqTKSACxye421JBJ2rQOK4FntOGTE2FS6TrI3wiebkclX2F_qnK_rMrAQ-XJ24p-LR5nx2L6k94OC5LWrlEoy2nIrinFLA1gg_b5aN5X0y3qaMVrpCL2NPiXr30IRTUYOhbm5MEiK5wl2Xeq9Lq4Wtta-XD6JqiPYuyHLzftq6fI8krdoLiooYwrf5ypOVKbNQt201fS5gul9SqN1XoO6pdjopunYYtskMuGU2AWztoVkE9sRKosBdMencr-VS19i28kLyKdMmB3lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در ویدیویی که در حساب اینستاگرام خود منتشر کرد، دیدار روز سه‌شنبه ششم مرداد خود با دونالد ترامپ را «عالی» توصیف کرد.
او افزود: «این گفتگویی بر پایه مشارکت کامل، حمایت متقابل و درک هدف مشترک جهت اطمینان از دست نیافتن ایران به سلاح هسته‌ای و همچنین سایر اهداف بود. این یکی از بهترین گفتگوهایی بود که با رئیس‌جمهور ایالات متحده، دوستمان دونالد ترامپ، داشتم.»
نخست‌وزیر اسرائیل در حدود ۹۰ دقیقه در کاخ سفید با ترامپ به رایزنی پرداخت؛ دیداری که پشت درهای بسته و بدون حضور خبرنگاران برگزار شد. نتانیاهو تاکید کرد که «تمام تیم ارشد» ترامپ و همچنین «تیم ارشد ما» در این جلسه حضور داشتند و این دیدار «فرصتی برای تبادل نظر و هماهنگی ترتیبات مهم برای امنیت و آینده دولت اسرائیل» بوده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/77585" target="_blank">📅 22:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77584">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/r5d-CBJHkLBpoqKxlnPwgI2FuElpniQHTur2nV8Vb7mXDyTUiTUGf1lPmKJirVdnZ_xGxCXy3r3n8ZwhTSzUjFZmBr72JLSUpJQ7Kc5qwf2LA7IhsZjM3-0yg-94xdMfMJXlZ8h-iSEXhSa7j1FaYu0lWh_QfuXA_d6aYMaTNAsKLzocUCwtfKudUTm9BO4fdi5IzclUFewMjItKGUMOF4BThs0fOjBpRwRS4tKDNggBy2IzO-Z7v2Ha6i8ujx2LrOi_KcVsMyTBKBEQ1Vs6olmQlKhdHdadmQckez_-AxmHYAp7ZJrT33W8_ugS47prf5zigNdSacG3FN5jU6adyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست وزیر خارجه اوکراین، ترجمه ماشین:
برای گفت‌وگویی صریح با وزیر امور خارجه ایران، @‌araghchi، تماس گرفتم. دیپلماسی یعنی گفت‌وگوی مستقیم، حتی زمانی که دشوار باشد. تأکید کردم که هدف ما جلوگیری از تشدید غیرضروری تنش‌هاست.
بار دیگر تأکید کردم که تمام اقدامات اوکراین صرفاً با هدف دفاع از کشورمان در برابر تجاوز روسیه انجام می‌شود و هرگز قصد هدف قرار دادن شناورها یا افراد غیرنظامی را نداشته است.
این موضوع درباره اظهارات ایران در مورد تبعه این کشور که جان باخته و نیز یک شناور غیرنظامی که در حادثه‌ای اخیر هدف قرار گرفته است نیز صدق می‌کند. هدف ما مقابله با تجاوز روسیه است که ریشه اصلی همه این حوادث است؛ و این روسیه است که مسئولیت کامل همه تحریک‌ها و تلفات را بر عهده دارد.
بر ضرورت خودداری از هرگونه اقدام تنش‌زا و همچنین پایان دادن به هرگونه حمایت از جنگ روسیه علیه اوکراین تأکید کردم. این جنگ غیرقانونی است و باید پایان یابد.
موضع ما بدون تغییر باقی مانده است: اروپا و خاورمیانه شایسته ثبات، امنیت و صلح هستند.
andrii_sybiha
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 335K · <a href="https://t.me/VahidOnline/77584" target="_blank">📅 21:42 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77576">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QshS1XHd2c4HnJzY8nh7UdX2xyiZHIuRZGduuRPLtqsumXxNcMQO-id8r1HRxG3WohAfXTBryAT5O-5-6TxiqMZvPsm7OH3TtwbrjoIyxW4jTLu-erwIOU99LFhIyZ71XjXqMNy_zYbDb7COUBa4fLNfbXtYDurFTG_cvAO9g3ulrner_CB44MfPRyvwrK2PRSXXXMwC_rJhfzaPNRN7V4R7ScYIH6DAOA6sJ40l6GfWubZse1Y5ygG5NAFY5dWw2urQEETPoVVTuO_mCfzrlHkswj4RazAorPEcJYQzEQRfrA6oZ5ShEVnniw9PzdjCdtfOlrfL_iTZary9GdLCmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/epkwDvnczSQ5nUekkqbd8Wlv_YmO2gkI7T0NZXhdKcbkwX-pkbe0XS1hgumLge4pgVmrcHVdohsKfoSd6ujf048j72CrqCypQemOvAAwcCXWlP9o13gfo3C_3qWCPZCZhJ9dDx1LP8yltMD9ShieAoDbyP7cjDzwxI1C1bJS47MM0LOlhHpkiQ17s7PyKvlwUSVJi9gwk9ZJE5ZognJ6nsfHBstsz1IJjeUAxoqkiBH4ecYqE-nKf4QY-cE506j2Ckle6fMWCYHYh5rnk94DbTh-7o_x3uDPoQxnA9srTyvM90sfXhYuOfNF1DDEJ4gh-OVRfyYtRAJ091KxIW8VeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SanSWtRCIGA70sA4tlrkg9RStgWUtqVegl0a-P-5wVOchSpclAOU-w1qY9nQKc5qiel65AfkRlrILbKBDl3jQ2GCmp3THdzORjGLABIGlZHsUhO3WF2WuyCcFakxzGV7T2lMBiZeSgMBbDNJcXGSGHO3rmbiF8OVaHDlWnxH6-efPD0IQZASgyzHz2KijnckKOjfKCdS6qk2PHGb0ElSk_v7B6UedSu5bdFkpqYFAi53qW9JAWeCKP9CyiHZ2wUMzyilAhqZ1ZX6UvWsZhyrhDHpS2I3ZMUt44IfaqwsyJNMsm06Ju9hsi4UiUxWqVGmZS9526r5j9_nSh969HkCrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RFg86IdQwnR9dqhBygrZpS7XpBTnBGFbA-sguTn3ald8b1fW_W7GyPRXwIlm-0nUDZ4_X7oq3Db9nfdqeg84usBZkaxw6J_0Ti1yivCyx1JRNgYbnMiE92k6QTOZJSz-dpmNf2Ue3SFNBn85-Y0C1cx8ODBonANPd9rl3_6seJU7XYUpKarVsQBT06xm6rUViptCeMnsvJQTT0jyDUO4lpYJTeRbu_yzf-96r17dUhLKCZM-hPJy8Pkr0s-cG5PNBpOh9NUFaj9lgafc-RcX71IZj6oa5cgB1icmTqhuOGX3CmYVYoGbfuQPtco3MTTsf2lu4jVjBph2mwJCkZ7oGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/C7n_eVgwKTm87nEk6dG5hnHvAy6P6QxcPEDBd0nQP_8lr7qZMMvePhUnqTghgwRxri64ybH9TIO8QUw2k4HzBI39uFgt_K6EKcZqXaGm893fOJFmgfmeBsNeUyGNNN5x1W8iTeXvNtrFXZt0DB268Xuc2kDjTiyv8lOoViXaXB0orsvYx1UswGw6sQJ_eIMt4rcATS_H5jC2MyjjF5dxmGTOG8bLwAfrpqsl1zY7_qXJp8yeI0fbhcXxO-Abq19hV8g26utiQwqk1OWB0QpLAFmGtqw-KxbWCQLIwvyktAchdgCdnE2hkdhyRaVY3N3FjhZRCnI6fbLCQyBUvsqEdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PnEzoifPUWFXSTSdF9A9VAdn45jp5StkkUck7nXjc6YFqrpyiIeIUTjuF7jTq-KX0a1bphZa-uDrIz_7q8uWLfxc8HcnHLSH1Kb_V-pq5TZXUnesnosnUQLhsykwKBFds-uOmMM5Z4D9pelOZBHTJcxxzyENaph7kF13Nhqjr-7VQt9w66tBrfvRXbscEZCSw923xiNeysuRqgLHbQi90gj_2BlieXc9PqwWqpWPYK3KVvjYGECQ-agCMzaSK6Q7i9wkUW9Vx3y4I2jdrdV6HuAjDIeCupwBsMFO0-nIOI6h1I3wmlBdWa0RzyZEZ3Uvn-2iozdS1Y-N9PXZFv8J0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Djp-dI5lgx_zad7pUyApgJTf9gCRWeIEQDtHix3uJS-VnTI5YLBQyjDMIeMuqiUgtsP8HzIydPJnP6f9horEFBUg24FIxvt7Lsy0J8_mpeGoTrSU15MTJ8MoX7xEapCIy7gRTJBK6wrbnRctRq3_tN1b9AYFpdCt3SfvYEAYDknzOQJnxkpJFeLhoxsi92ilqO1TB5BG142hIwue9Q8Dt3p0xzgoZvnHuHpB1MnUk0lINbhUDbTZM7qYhfMM7z39tPb8rjsJ8xLMks4ksuhOD9aCVRchHMdYEWyNHt4m0jJPbRYwUiKA-Mvq4XwckEAgxD3zf8mYRKjYAcDdVR7Kkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iK6XqNc4amxtxLU7k4A3nC2dcdZ2G_0hTfile2GIeKeaK09dw_Glpk_CFLGg0enfc_YaYcnx6yf1XEZQF5QvWCXtIPcQVkajpadS6Zt0BQI9EM_CumSbE0L0AJpQbtODASeP45xHvVPY5yBtfV94jDneG1aNmysfa4XLx7jsu0clZV36pJLVStP2KJ1GfN2MqcXXDmp6pqEK8E0sxRoFRba25M40OHDxxyDi_z7T77vun8dnX5MyHSo7qClfjuz7ZxE7fXyM9cvC39jIxH6hgHspiGAAJcNqB2-KjSqh_sTsR4aZxvUHoGLe1OsTvL5iA6jwv7p5j1j_G3R-InxfNQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل روز سه‌شنبه ششم مردادماه برای هفتمین بار با دونالد ترامپ در آمریکا دیدار کرد.
این دیدار در کاخ سفید و پشت درهای بسته انجام شد.
دقایقی پیش از نتانیاهو نیز، ولودیمیر زلنسکی، رئیس‌جمهوری اوکراین، مهمان ترامپ بود.کارولین لویت، سخنگوی کاخ سفید هر دو دیدار را «مثبت و سازنده» توصیف کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 374K · <a href="https://t.me/VahidOnline/77576" target="_blank">📅 20:37 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77571">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Wj6wcGSU5zpmWyRAkHWKAIXt6jzZqdAw1qV9pnsu_UIY73BlSisAIvC_EVb9qhZYYn3ATe_TguRByEplMeIXlZ4trl3Q16WwK-AGUGH0Dz_k4VZ1NFahhnBXW-iRxvrWWWtGT7uPtxLGPhxPKedCFVUvpTdFthTOWitoOeqippQe7rooLpMgwaK3IfyULVeyVuFOEiAEYvEPgTkdfAAc2qbxVwPfn-zfKgBZVWSWnCjeKnyDDEybCjDjDPbLw2pCkj3zKH6Jid6Ka5c4K_a6TOkbT6fRCr2WtlIWqt9yrQsvXKIFGG7c6ORhNUZl6KFO2v2NP3gp-G0NPEQmR9n9og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/A2nyjEATmabQrtDivGillWeeMqcbbmWXxYx1tRRQIvQ2sSj6eRSFq4uDhdlCD9oEhr8wPoAq5yd9UXeEyphiJnxXJXUmKsKugGQraAE0hqnpKN5yUyWH3qYsW_QUlBITCsPo0s3VACAkox8jlG-TRMSZSg05M7a5dSqZ65osSUirfY12T9QAylxyjXkURizcbk6nzLwimCyrPDSeW667ub9AE5Xa2mEvVCA_IM9GByMujIETz0Ekj3Nmj4kDIVPgaCqb64OGft0RUaGCp_fbiNg3tk_ciCFMN18pKyb4o7xAsAttO9SL23ezKuYEB5Qg12cnsOjiLjLCEUIYwLhlyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/H88dkX-7Q9SGGROjsLGdDHcWa5s8IvqFlknzEeNnPEbgK3Z1yi_EPRGiXjoXk2PYhwpDdU6i2nzsePjJctdjNh061sDXp6Pf3OooSF1v0lYm1OLQ-RXg-eDG72d-Lmaw_qVPAhBASnaiENqVRmi6SmZxhcyZRVy_l8gvnhforupd9nkbpzVj9aXCWO1ES49t7L7H6coGOdM2a-Dg7vhESnWr4uBTGv764cnL-vbFgkO2S7aQ3O34pxm2f2SyWyncSgckJVIyo0TCeU7bzvkt01UsqORSHuzefi2TwApjgGRI9PT9xf5kfD1JQVauii4Y_yfBY9AYCUPm7bkaZEX3xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bjX0k3bmfhwjEi6_TKAPDgHzSWYulS-EqgaqMnJOQJ2QFy9E97yW40danaKC-t1oxPUXTtCpuuU0xzfnUFlfU-xBmKkv1G93ndFUhXNH8m9zLBbZcM2c73N9GWX5WDonVV56TSujwO1d7VtxIIYFJC5aYjMen7melwuYwYNU3r93hte1fdzybaRQCOsFGuTKbSBzdXUPQZdMc-uJ-_45YQVFk2hz0lGW5J1f0cfN2bz35JhJHDj11c69znqZSbQ9aLGoNxbEY8PyYFtvmaV0u608nSzjU_Od9u8H4ZExaSA89i7mchAGM1DlaIRnzp14PxPMiO4KOm4rwCB034X4PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/K71RaqtmpxNNxyLXVBszI44JPBcDJUa8b8Lkfdeeq0gk4EgMv7tBDxMlXU6mP1fWiOVDR2Zu4XT7SlzIqsQVk2KmrLql8B15TgFt8xoRSOxXcTGSEIWf9C7IHEe0GP4KlgfOPJtX-20DTHMv1Fhk3oQrXjPjuUuc_TGZXeHaoiMxZtYVCfK5B-ejo4T-6n1rZDJP_B04Or855VrZ7sVquPgtRR6gPpJI22kwUoKGk81yrDXiseGeIz8PQSBjEOCbsYP9KOeFm5lZGYL9CKJLp5EqztEtbScw2biT0UqfSVQAagBcFvUMx-hO8t87MfTIm7RiQNakRRpab1n7BaeIOg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویر دریافتی در ۲۵ تیر با شرح: ترمینال مسافربری فرودگاه بوشهر و باقی‌مانده‌های یک هواپیما
سخنگوی دولت، امروز: فرودگاه بوشهر دیگر قابل استفاده نیست و باید از نو ساخته شود. از یک هواپیما که تازه خریده بودیم فقط دم آن باقی مانده است.
Vahid
سخنگوی دولت جمهوری اسلامی می‌گوید فرودگاه بوشهر در حملات اخیر آمریکا کاملا تخریب شده و دیگر قابل استفاده نیست و «حتما باید از اول ساخته شود.»
فاطمه مهاجرانی روز سه‌شنبه، ۶ مرداد، در نشست خبری هفتگی‌اش با خبرنگاران گفت در بازدید از فرودگاه بوشهر «بقایای هواپیمای نوی به تازگی خریداری شده» را دیده که بر اثر اصابت مستقیم موشک، جز بخش کوچکی از دُم آن، تمام بدنه آن نابود شده بود.
این نخستین بار است که یک مقام حکومت ایران از تخریب کامل فرودگاه بوشهر بر اثر حملات به ایران خبر می‌دهد.
@
VahidHeadline
یک توییت به همراه اسکرین‌شات‌هایی درباره اطلاعات یک ایرباس ۳۱۹:
عمر این هواپیما 24 سال بوده! سال 2019 هم خریداری شده بوده.
iranimerican
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 383K · <a href="https://t.me/VahidOnline/77571" target="_blank">📅 17:47 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77570">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/D_NM0NaFaH_V2C_fKuAX_jOn7S1RqlDuVjZh_-0YKyI8Qe22GWkwdOeNjgFqM_P4wk-BPq8NKMvc2O-OdiLzSmJrVLFpjBAyb0CTfpYj6IHPWhPLnUSoBQTtAp-RrxfKVN6zanphMsxjbvOF03I3lZBYrycsaOZNz5r_gZMYj2400jl0lVsgQFzqvVOuzpOkTQtlG7gUtyVLS6lR-Bgy42c8Iuls3IGgwT7pOQ3fH1UT1LJgI0FW_JEJh5XKuozOoJMtCxi-o2Kgp7cHUavCQQDlxAjX-dtpHokNtSu-GdxRYu0vzeOZG5FuMYy1oLjlEUvRPabsDyMonXF_kQq7XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های نزدیک به حکومت و شماری از مقام‌های جمهوری اسلامی در روزهای اخیر بار دیگر بر اجرای قانون حجاب اجباری و برخورد با زنانی که از این قانون تبعیت نمی‌کنند، تأکید کرده‌اند. هم‌زمان روزنامه «همشهری» با انتشار گزارشی، از قوه قضاییه و نیروی انتظامی خواست با آنچه «هنجارشکنی» و «بدپوششی» خوانده، برخورد کنند.
روزنامه همشهری، وابسته به شهرداری تهران، در گزارشی با اشاره به انتشار ویدیوهایی از حضور زنان بدون حجاب اجباری در سواحل کیش، مراکز تفریحی، مراکز خرید و برخی رویدادهای فرهنگی، این موارد را نشانه «حیازدایی فرهنگی» توصیف کرد و مدعی شد که ممکن است بخشی از این رویدادها در قالب «پروژه‌ای سازمان‌یافته» برای تضعیف ارزش‌های اسلامی انجام شود.
این روزنامه با اشاره به ویدیوهای منتشرشده از ساحل سیمرغ کیش، برگزاری نمایش‌های مد، جشن‌های مختلط، کنسرت‌ها و تغییر الگوی پوشش در اماکن عمومی، خواستار ورود دادستانی و نیروی انتظامی و برخورد با افرادی شد که از نگاه این رسانه، قوانین مربوط به حجاب اجباری را نقض می‌کنند.
هم‌زمان، شماری از نمایندگان مجلس نیز بار دیگر خواستار اجرای قانون موسوم به «حمایت از خانواده از طریق ترویج فرهنگ عفاف و حجاب» شدند. محمدتقی نقدعلی، نماینده خمینی‌شهر، مدعی شد «برهنگی و بی‌حجابی مانند خوره به جان جامعه افتاده» و از مسئولان خواست اجرای این قانون را در اولویت قرار دهند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/77570" target="_blank">📅 17:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77568">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/i2CDNGggqbiPGsH8yr7tiEs48j8_0O6CVzuQBKyXJNZC9-qVmE0dmmZgTAG4VdQWKtkLohknePSK06RmkDzSG-uGL9xXC_SOrDViQ0hVa5LQT_rewXtSjoWyOUG7aYxT4B2Lrz56gd5p2Mf7b7WaIiapy-ApEg0N_xJjDw0SXoYLWpWflI0CUXKqw7FdEvq_hYE7hndJAukZDAuM534L0cp7dXl1oBBB_lNmSs-1zGdxeAtgHtbCqNUn1oWOuUsJw_-eSfqGjRBs5A_fVdBROyhwE39aWo3bSbApnvUasS70fasCLC9kjzF0H53OYKzAT7_wji1RttrGwDwBlrMCHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f23cdb858b.mp4?token=IJIGkzD-cPvj2OggnZlW8SWN2LpLexahG6dVZCLOHWEsfXoP1QsBO4fB1eRuAqAuSHZEzjRaSm_TTiOGlNH-DiFi4q-twjw0dh7QmbZlLyty9R1vt_4O6ev8Hq9IZIGCJCWSfw7-hRHrv-EJY_-eKJqsyuJPKRV2OfoTd1X9g0PubcpuxSyOAEaw4Q3_IByJchxsZSAmR-1Z82uQ2u7lwd7Xa3_OuMjbjYGhaOoOdmJs7_fcWq5vB9uul5svHFzvwsWz4zyBfzN1n7mcMbKK-P4YJff-ZW-_wVhRL_udPWV6ffGVtUNVKXejJfRT0trWGEsRAhbfQMW7mTUoGopbZg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f23cdb858b.mp4?token=IJIGkzD-cPvj2OggnZlW8SWN2LpLexahG6dVZCLOHWEsfXoP1QsBO4fB1eRuAqAuSHZEzjRaSm_TTiOGlNH-DiFi4q-twjw0dh7QmbZlLyty9R1vt_4O6ev8Hq9IZIGCJCWSfw7-hRHrv-EJY_-eKJqsyuJPKRV2OfoTd1X9g0PubcpuxSyOAEaw4Q3_IByJchxsZSAmR-1Z82uQ2u7lwd7Xa3_OuMjbjYGhaOoOdmJs7_fcWq5vB9uul5svHFzvwsWz4zyBfzN1n7mcMbKK-P4YJff-ZW-_wVhRL_udPWV6ffGVtUNVKXejJfRT0trWGEsRAhbfQMW7mTUoGopbZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: اگر ایران تن به توافق ندهد، کوه «کلنگ گزلا»، پل‌ها و نیروگاه‌های برق را می‌زنیم
دونالد ترامپ، رئیس‌جمهور آمریکا، روز سه‌شنبه گفت که گفت‌وگوهای خوبی با ایران در جریان است، اما بار دیگر تهدید کرد که اگر تهران با آمریکا به توافق نرسد، تأسیسات زیرزمینی در کوه «کلنگ گزلا»، پل‌ها و نیروگاه‌های برق ایران را هدف قرار خواهد داد.
او در گفت‌وگو با شبکه فاکس نیوز اعلام کرد که در صورت امکان ترجیح می‌دهد پل‌ها و نیروگاه‌های برق ایران را هدف قرار ندهد.
ترامپ توضیح داد: «من می‌توانم همه نیروگاه‌های برق آنها را ظرف یک روز از کار بیندازم. تمام نیروگاه‌های برق آنها از بین خواهند رفت. فکر می‌کنم حدود ۹۱ میلیون نفر باید بدون برق و بدون پل زندگی کنند. و این یک توازن بسیار، بسیار ظریف است.»
او تصریح کرد: «آنها می‌دانند که اگر توافق نکنند، من این کار را انجام خواهم داد.»
دونالد ترامپ هشدار داد: «می‌توانم بگویم ظرف دو ساعت، بیشتر پل‌ها، پل‌های اصلی، همگی نابود خواهند شد و نیروگاه‌های برق هم ظرف یک روز.»
او افزود: «اگر بتوانم از انجام این کار اجتناب کنم، ترجیح می‌دهم از آن اجتناب کنم.»
رئیس‌جمهور آمریکا همچنین با اشاره به تفاهم‌نامه امضا شده بین واشینگتن و تهران در خرداد ماه که در درگیری‌های تیرماه به آستانه فروپاشی رسید، گفت: «ما دیگر نمی‌توانیم اجازه دهیم آنها توافق‌ها را نقض کنند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/77568" target="_blank">📅 17:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77566">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BiYtlaTvZZhgaqhP3923hkmEWML7_ng2SEi8EhWmx-YEmD6ueaZmMaQZe9TiLhQnXNziI2fQJ3j-tlPKwn3t050Uj_HUySjh3zR9AcfVjeuUKcfzq2uSKC7E_bkqxQysIp8h-3oZonQb34H-9ihRUGSa48x-XsBERtrOsdWFvOP9UgdrAL2IMf_Fu2_35ORDYNyRfY8IKat8gYChaO4AIXQSRn8sIJuD0pQHUO32qni3O-y8o_eNxjvkVQmzJ0_v2V6-4umYM_9zS46VbxKfOJBOQmSxHbTRNrO-U4kzzOQDlr_KszaS11te9oBF7ePs8YWVdOZey1D4P0i6HsAe9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sQlX1edGzxELRnaQYn8TSxnUAGEl1SFeCMcaDnFwFe3fMmrp8ri5cHcaXlsSRRE5J35PukEwsd3abPdGroOLimHKjrDcQ-Ty3_HfYOxF9AvZlYbGIRwMZw1hP-8LxYe6VlnkS9rn7Yr0x6kOj0Y-hW59kslYDnyCLCiLpYhcANuUNuEj7fB7o28Uf3DnATq6Hp88si5UPT2G51Ps6HviYuFtl4Et3zrBzsWFVL2pEBx_wFWhdc6vJHTCRiG_bbCufrl2Ye2jqNTcsc6my4fHL4QToGnFm5aECe3mtVjoWIWi8Y9VkyNi3Wcvq1UAKPNYwaTxk67vnUUeFARRU07vXA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسرائیل کاتز، وزیر دفاع اسرائیل روز سه‌شنبه ششم مردادماه در مصاحبه‌ای با کانال ۱۴ تلویزیون این کشور گفت که در هفته‌های اخیر، جت‌های جنگنده و بمب‌افکن‌های نیروی هوایی ایالات متحده از پایگاه‌های هوایی اسرائیل برای حمله به ایران به پرواز درآمده‌اند.
کاتز گفت: «ایرانی‌ها می‌دانند» که این جت‌ها از اسرائیل برای حمله به ایران به پرواز درآمده‌اند.
به گزارش اورشلیم‌ پست، کاتز در این مصاحبه گفت: «امپراتوری مغروری که اسرائیل را به نابودی تهدید می‌کرد، فروپاشیده است.»
@
VahidOOnLine
یسرائیل کاتز، وزیر دفاع اسرائیل، در کنفرانس امنیتی کانال ۱۴ با اشاره به دیدار دونالد ترامپ، رییس‌جمهوری آمریکا، و بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در واشینگتن گفت آمریکا در موضوع ایران منافعی دارد که فراتر از منافع اسرائیل است و افزود: «بسیار مایلیم به ایران حمله کنیم، اما آمریکا موافق نیست.»
کاتز با اشاره به آنچه دستاوردهای اسرائیل در برابر جمهوری اسلامی خواند، گفت: «امپراتوری متکبری که اسرائیل را به نابودی تهدید می‌کرد، در هم شکسته است.» او تهدید کرد: «اگر به سوی اسرائیل شلیک شود، با تمام قدرت حمله خواهیم کرد. ما آماده‌ایم با توان خودمان به ایران ضربه بزنیم.»
وزیر دفاع اسرائیل در پاسخ به پرسشی درباره واکنش احتمالی اسرائیل به پهپادی که روز سه‌شنبه از عراق پرتاب و در مرز اردن رهگیری شد، گفت: «ما می‌دانیم چگونه امور را مدیریت کنیم؛ آماده‌ایم.»
کاتز همچنین گفت که دونالد ترامپ، رییس‌جمهوری آمریکا، «درک می‌کند که اسرائیل از مناطق حائل در لبنان، غزه و سوریه عقب‌نشینی نخواهد کرد». او افزود: «هفته گذشته از غزه بازدید کردم؛ هنوز تونل‌های بسیار بزرگی در آنجا وجود دارد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 301K · <a href="https://t.me/VahidOnline/77566" target="_blank">📅 17:23 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77565">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rG1VGw8y99k_RjrptiB0Tx7IsWavgtzipolKtbVE2-BETyat-z1BIuWZWvc9JhpsxzJJf5SUuMMfM87ToC6iDbS546f_KLBudlLkBaDqZINtK9aGT52CkeUMqd-TmcUP_7ndMs2wR8atx5jQAX8vtTQAgVIOI90aRoXdwQFWMj_IXT1oo2S9qsket-F-HGYu7Iglhh_YmyUtp8bW2sr7xtnw1etGFVR2MFPNEhYiCOPLCoBrcjCn2Q0SOxz6yGeclhgZnF9o3L36mnxjKgI-ZgghIhw4cRwc9W2mfB3U9YtIuPE-Hf-Tprt0k0ulYY4vn5KsStgdNJRyjzh193zZTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه می‌گوید که حمله اوکراین به کشتی ایرانی در دریای خزر «باید به‌عنوان حمله به خود ایران» تلقی شود.
دیمیتری پسکوف، سخنگوی کرملین، هشدار داد که این حمله نشان می‌دهد که از بین بردن «تهدید ناشی از کی‌یف» تا چه اندازه اهمیت دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 286K · <a href="https://t.me/VahidOnline/77565" target="_blank">📅 17:18 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77564">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/byRETmRuLHHM3i2KQI-uPSPUWXoJcDcvU-EkRtdJLvw1keeSVJe7lm9XBn0u3WKU4TWJYJlwnAVopMSJcZ7Gm81XGgPutCaRM5r607F8IslMeft03QFfJoUoRB_zJuFgKpfoTsqeVcZ_YaOnK_5WB7ljNoyXEc9hl--l_xzdEk6iLf55W9q5O7TVTnPafRit2U9FUfSFfLozAdLzyX7VZ_9sJOL7Q7qq5TWiSdZzZqs9HoRUERbEvuAmLAyRLf_oDL2OQr0M62gd9R1O5tV_rncPbUVcAEAJH0YfTbpVgmDwkwDUuA98kQbZnwhcEWDzG31DtIkCxoWneAQc6AzX0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بر اساس برنامه‌های اعلام شده از سوی کاخ سفید، دونالد ترامپ، رئیس جمهوری ایالات متحده، روز سه‌شنبه ششم مردادماه، با رئیس‌جمهوری اوکراین و سپس با نخست‌وزیر اسرائیل دیدار خواهد کرد.
دیدار ترامپ با ولودیمیر زلنسکی ساعت ۹:۳۰ و دیدار با بنیامین نتانیاهو ساعت ۱۱ صبح به وقت محلی برگزار می‌شود. برنامه روزانه کاخ سفید نشان می‌دهد که این دیدارها بدون حضور خبرنگاران برگزار خواهد شد.
با این حال انتظار می‌رود که پرزیدنت ترامپ، در لحظه آخر اجازه حضور خبرنگاران را صادر کند.
برنامه بعدی ترامپ پس از دیدار با نتانیاهو، حضور در مراسم یادبود لیندسی گراهام، سناتور جمهوری‌خواه فقید است و نخست‌ وزیر اسرائیل نیز در این مراسم حضور خواهد یافت.
پیشتر نتانیاهو اعلام کرده بود که موضوع ایران در صدر گفت‌وگوهایش با پرزیدنت ترامپ قرار دارد.
دیدار ترامپ و زلنسکی نیز پس از آن برگزار می‌شود که شامگاه شنبه سوم مردادماه، نیروهای اوکراین شناورهایی حامل محموله‌های نظامی جمهوری اسلامی به روسیه را در دریای خزر هدف قرار دادند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 295K · <a href="https://t.me/VahidOnline/77564" target="_blank">📅 17:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77563">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pnjL5tzXVgf90ofEwwgEVUAHTRCMYNbk2W5_-HRebpHwRJpR8DkckjtXmxL3TP6whjsrZfSFq-DEUkEgoMFlBFjOU_V4_fHW02dAimtheux4hEGIdrKZQRtWmvdW2MmNZX5ckhPe0prJW2Ovt_ctvoyxwY8IG7pSB-oUW48W7MK0rODL-PMJNLt3JE7NPGPEmjAGHdbUsWOIGJZm7xmI0m8LM4FXMYeP5TEt6PJ5q5-ITsIL22VY-i8g6V-UQsxx6cWgA3zT5OE0BIkWj7BVFF_7yHNG4zrc7ADRVdP8nmro0CLn4H8ucZVPiXm5eH9AAw2NH5kTn6r7MjC5joRO3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یاسین سرفراز، بوکسور ۱۷ ساله اهل بجنورد و عضو تیم ملی بوکس ایران، که در جریان اعتراضات دی‌ماه ۱۴۰۴ بازداشت شده بود، به سه سال و سه ماه حبس محکوم شده است.
کمیته آزادی زندانیان سیاسی خبر داد، پرونده این ورزشکار نوجوان در شعبه چهارم دادگاه کیفری استان خراسان شمالی رسیدگی شده و او تنها در یک جلسه دادگاه، بدون دسترسی و حق انتخاب وکیل، به اتهام «اجتماع و تبانی علیه امنیت ملی» به سه سال و سه ماه زندان محکوم شده است. این حکم حدود پنج روز پیش به او ابلاغ شده است.
یاسین سرفراز از ورزشکاران شناخته‌شده بوکس ایران به شمار می‌رود و پیش از بازداشت، در رقابت‌های کشوری، آسیایی و بین‌المللی موفق به کسب عناوین قهرمانی شده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 287K · <a href="https://t.me/VahidOnline/77563" target="_blank">📅 17:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77562">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YeJ2h7jfUSLx8Q2B7x6eiuU-yPB5-CHoa-l8NoJLNb-hXoRY7FQxn2UficpGrGTepdypIRzYHGkW5rbTW70g-U0nRZWyCM2APyRCEqhQe3kXmELP7FvHUskWDOzwwH98q_8QTExHOJu7AVV3GcC3siZjVqhajgnFLyDFBstw-UzthN-k2D6azU4dGX0Zyne7Pvs6SZMEKeO3MwiubzSSaUJRAMDJ-agj6fmnwbBraLtYvfSJECziiI_77t0qDm9nP3vthzwlE7UCKLm3eMR1Lcoi_gX4Qjy-SGtrOl1euXWSEkFLVSc6hx4YarFXin-UoTyYaynzVW4LkHPFMNVrEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رویترز روز سه‌شنبه ششم مرداد به نقل از یک منبع آگاه در خلیج فارس گزارش داد که عمان پیشنهادی برای ایجاد یک سازوکار مشترک منطقه‌ای با پرداخت داوطلبانه عوارض یا هزینه‌ عبور و مرور برای مدیریت تنگه هرمز به ایران ارائه کرده است.
به گفته این منبع که نامش اعلام نشده، پیشنهاد عمان مورد حمایت کشورهای منطقه است و بر اساس آن ایران کنترل انحصاری این آبراه حیاتی را در دست نخواهد داشت.
این پیشنهاد الگو گرفته از نحوه مدیریت تنگه مالاکا بین دو کشور مالزی و اندونزی است و بر اساس آن، عبور از این آبراه با پرداخت داوطلبانه هزینه در تأمین مالی ناوبری، حفاظت از محیط زیست و جستجو و نجات همراه است.
عمان پیشتر به طور رسمی اعلام کرده است که با مدیریت متفاوت تنگه هرمز به شکلی که ایران می‌خواهد موافق نیست و پیروی قوانین بین‌المللی خواهد بود.
پیشتر مقام‌های ایران تأیید کرده بودند که مذاکراتی را با مقام‌های عمان در زمینه مدیریت بر تنگه هرمز انجام داده‌اند. سخنگوی وزارت خارجه ایران هم روز دوشنبه تأکید کرده بود که در حال حاضر تنها مذاکره‌ای که ایران در آن دخیل است مذاکره با عمان درباره تنگه هرمز است.
دونالد ترامپ، رئیس جمهور آمریکا، روز دوشنبه گفت که این کشور «مذاکرات خوبی» با ایران داشته و احتمال توافق وجود دارد، اما او هشدار داد که اگر مذاکرات به نتیجه نرسد، حملات ایالات متحده از سر گرفته خواهد شد.
در همین حال، عباس عراقچی، وزیر امور خارجه ایران، روز دوشنبه با همتایان عمانی و سعودی خود در مورد تنگه هرمز گفت‌وگو کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 319K · <a href="https://t.me/VahidOnline/77562" target="_blank">📅 17:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77560">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PFwEISL4wgB21jeLWG6m5e1NnOCq3i50Hbl2SjEWNfNApV7SZnNwdeEpmDTsiygu9rNz3LtBlOsXQR11v4p-YyKXbUuOuB3dGaJRSRWEKb-Gk3M2w_OwwszEkpDfLAJkJfyCHYaGd7HEI7p_eRkFK5xhHhuEp8wJ2bQZBey_Ne_gddSdTpeHGu64kS05oXlQcPvjJwfkvGvwBcTT3wdMefuB2MDsYRChjBrR50uXbYih5YJ6sUfI5pDWGiYEMiXYmGb_XVkAJy_vDqj6I9TKsUvhGgb5M96CS1_0J7_SJD3Otj8TmREH8-X1YXVr0tKch6W5qJ_1jZxdBshw-dyFSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/M1X2t4GuNK4YSjO1If1DJdQvCSpKf0bQe6pz2QJ5b4z-g_tzf3Krj75SOwVoS6ejrUysHzDRe5k0yVqIyttux1sNRtzRB6_w1CoB9v2oNRjjv1TK5z9f3VSJjXDKbmQ5tL-RLRJTRyDfv0sgM6pZUA-l6BZ357plVxB5AM-4DFSwAONigfyDRGHpyMTOckLn9VtLL-p2qsCGpSpejY8tuWsXxdpV_bUFmCkUpNlyTsKdsTCGsgQIzAM56d87RCrh-PWz9MabWTCHSUmG9_ExeanLmiW0Rk4tHyH2QM8MnMHqzl-wh_7CsYJJYBVgLXKl5pZ7VNpJbxZN6x_FUR7Bbw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قائم حسینی، امیرحسین ملکی و علی دشتی، متهمان پرونده میدان علیخانی اصفهان، در آستانه اجرای حکم اعدام قرار دارند.
از خانواده‌های این معترضان دی خواسته شده برای آخرین ملاقات به زندان مراجعه کنند.
قائم حسینی پسرعمه گل‌محمد محمدی است که ۲۸ تیر اعدام شد.
این پرونده ۱۲ متهم دارد که علاوه بر محمدی، تاکنون سه تن دیگر از آنان به نام‌های عرفان اسفندیاری، ابوالفضل سپاهی و امیرحسین صفری نیز اعدام شده‌اند.
@
VahidOOnLine
شروین باقری، از معترضان پرونده اصفهان، در آستانه اجرای حکم اعدام قرار دارد.
به خانواده‌ او گفته شده برای آخرین ملاقات به زندان مراجعه کنند. شروین باقری نیز در حال انتقال به سلول انفرادی است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 413K · <a href="https://t.me/VahidOnline/77560" target="_blank">📅 17:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77559">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K5SNEBbXYIVsY_gxeNh4mSI5Vu7Zboqfc2-VkQZDHGvW8MOaI77flSNuxGIysoCLp4P5oDExIo0rrnWAIwlOZ9iB182m_DvQoyRbzRWaBDX6xxzLwSEjOzGkmWh-2fgUu1b1IyiJzCn6-eSPy_tETk9FfAIMWfiFuHX0DBL8eVARf0PHEehTxC5qClzF2Fi9hEqZP9D6QUDPyml048wGUvfcIe0CvM97brL-nP1rEdThvNE0MbuQlacyMJrH4xg8-BpNjqQ2K8o6hU_rajLMmxUOwCbHuaDvonokM5jkAvqPd0YeKdBFBxuWDIr46966YWx9-q-yOMLYFBvGp2q8fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منابع حکومتی بدون نام بردن از کسی نوشتند سه نفر از پرونده ملک شهر اصفهان اعدام شدند.
آپدیت:
بعدا ویرایش کردند نوشتند: دو نفر
آپدیت:
قوه قضاییه جمهوری اسلامی اعلام کرد بامداد سه‌شنبه حکم اعدام ابوالفضل سپاهی بادجانی و امیرحسین صفری حسین‌آبادی، دو معترض بازداشت شده در اعتراضات دی‌ماه در اصفهان، اجرا شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 501K · <a href="https://t.me/VahidOnline/77559" target="_blank">📅 05:16 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77552">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/75dcad3a9d.mp4?token=aQ8HnQqXDl42Rdzmug_exstC3rv4RO_RfzajAzzMsflAtMOFBxK3_rO128itJieY9hmov0HDVgrYgCiyfPExU8qYUS_lTMFv8zBdQp-XFAw1biFN3JLRQ0FGH-t9uVy59xdcivFFkTsiGT-o-t3flsLgzB8cndUkRzBBs2xY8J9PU6gfDAiEF5_oowduXPtvdKgVcmdffA7MZKqdmOJSR7sOrTorbwcEvfNO9LRVkuyulZ4lMfFLkEGn2kbVmdTa4-f_gKwW_qAjK0luTMFlniGSMXcBzV3qK2Iz_-YRF7hgoesi6aErTx_nQLAT4CXd8nZJ8POvhAS_bs1jTfianw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/75dcad3a9d.mp4?token=aQ8HnQqXDl42Rdzmug_exstC3rv4RO_RfzajAzzMsflAtMOFBxK3_rO128itJieY9hmov0HDVgrYgCiyfPExU8qYUS_lTMFv8zBdQp-XFAw1biFN3JLRQ0FGH-t9uVy59xdcivFFkTsiGT-o-t3flsLgzB8cndUkRzBBs2xY8J9PU6gfDAiEF5_oowduXPtvdKgVcmdffA7MZKqdmOJSR7sOrTorbwcEvfNO9LRVkuyulZ4lMfFLkEGn2kbVmdTa4-f_gKwW_qAjK0luTMFlniGSMXcBzV3qK2Iz_-YRF7hgoesi6aErTx_nQLAT4CXd8nZJ8POvhAS_bs1jTfianw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اخبار منتشر شده در شبکه‌های اجتماعی حاکی از آن است که خانواده‌های زندانیان سیاسی محکوم به اعدام و شهروندان در میدان علیخانی اصفهان تجمع کرده‌اند و گزارش‌هایی نیز از درگیری یگان ویژه جمهوری اسلامی با معترضان منتشر شده است
این گزارش‌ها می‌گویند نیروهای یگان ویژه جمهوری اسلامی با موتور، خودروهای زرهی و سلاح‌های سنگین در محدوده محل اجرای اعدام مستقر شده‌اند و اینترنت در اصفهان دچار اختلال شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 495K · <a href="https://t.me/VahidOnline/77552" target="_blank">📅 05:11 · 06 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
