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
<img src="https://cdn4.telesco.pe/file/EEYd5NW1G8miKwObW-FhR-PWt4cD3XvgYjEsGP3akvV8E28A39xM9wcSEhdLfIOVdbAZXj-lhTEwLIO7kW7fbqISQOVxUqtnDpfFNaFYrC6TsKGSTo_ropdtclJ0732rH7OqztYCs-7qB1974zdgHUHMe32Xep5rUHGOAFmp50ldMEiX8xvG5jwqLFurKYCZBbNJyTqcNd0UrE4f_0UIq8TYCKDlEP-Mio8Gq5ioCKmbIvO8kwSKbDhFRPYbQdYqCFEzKcFqyEPaioJ5nRFMw2Q_mHyrdvSwGPvGtRK3XHBNpJq1MNzmEDS7x1iUZqi3-mhBQ4GRzOlyF5EfTJjn6A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.9K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ■  تاریخ | ژئوپلتیک | بازارهای مالی ■https://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-05 21:22:03</div>
<hr>

<div class="tg-post" id="msg-21254">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">به نظر من جمهوری اسلامی بزودی گزینه آخرالزمانی حمله به چاههای نفت و تاسیسات انرژی منطقه را فعال خواهدکرد که در پی آن نفت به بالای ۱۳۰ دلار و طلا به زیر ۴۰۰۰ دلار خواهندرفت.</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/SBoxxx/21254" target="_blank">📅 20:02 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21253">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">عراقچی:  ما برای جنگ آخرالزمانی آماده هستیم</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/SBoxxx/21253" target="_blank">📅 20:02 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21252">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">عراقچی:
ما برای جنگ آخرالزمانی آماده هستیم</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/SBoxxx/21252" target="_blank">📅 20:02 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21251">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">پلیس ضدتروریسم بریتانیا در حال بررسی این موضوع است که آیا ایران با طرح ناکام‌مانده حمله به پایگاه هوایی در پایگاه نیروی هوایی سلطنتی فیرفورد (RAF Fairford) ارتباط دارد یا نه.</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/SBoxxx/21251" target="_blank">📅 19:41 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21250">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/904c5f3c14.mp4?token=HVfhI9w2D_5IxtieLCXXU67LGk1jP_H2mSouoTK1FGBPQMhdB7QFcXE5nlCFKJmXVFIrkURGxvX6nl4UIlR46Zd9xURwtyc-SOvfpYFe9EP8cfFaHKocH19hJ4olczRCsUIvyuaNbL9W5KyH6Ks6GkP7tDooB8-E-R_bQIVsk-zaLoPrh3s0zxZ1Kt9TfFmrRBXUNEUrTA7_t_YFMvEMPPc0WS6pq_lGUFgPB6D4Iz5D1enLD2iCteb47rHYfgc7TttXVqE3hs1gRBwSIVX5HAP1JtpOQR9jrgZ_eDzlb3AIpp5QEsf975PdcvJQDR0a-GofutegwC8ysKCI1lny1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/904c5f3c14.mp4?token=HVfhI9w2D_5IxtieLCXXU67LGk1jP_H2mSouoTK1FGBPQMhdB7QFcXE5nlCFKJmXVFIrkURGxvX6nl4UIlR46Zd9xURwtyc-SOvfpYFe9EP8cfFaHKocH19hJ4olczRCsUIvyuaNbL9W5KyH6Ks6GkP7tDooB8-E-R_bQIVsk-zaLoPrh3s0zxZ1Kt9TfFmrRBXUNEUrTA7_t_YFMvEMPPc0WS6pq_lGUFgPB6D4Iz5D1enLD2iCteb47rHYfgc7TttXVqE3hs1gRBwSIVX5HAP1JtpOQR9jrgZ_eDzlb3AIpp5QEsf975PdcvJQDR0a-GofutegwC8ysKCI1lny1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/SBoxxx/21250" target="_blank">📅 19:36 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21249">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sVgWFQ1DrS4PT3SaUs0N_l-NVsjnYcdKJ5STIhGPhUxJLnMXXiZmhewkzQEhJZ3arWFo81j-grA2oVh7L2Z5bLI-Ij1GSxAw2wnZxOdZVBqc2jNfENdXpHo1YHv7GZ7cghvdk1DO6sj8A54vL-tkNy7oZliEN1DIt7PDDMd_EnRdHNsHk4Lz6yfD_g8IcZKelOf-kfwInl9KeTRbnkZ_v3foBIy9tkezotu22L8oqtseXBH7bFEuLSL0HVeVgRLxaeUPdhBC06rmrKPymYKgiHWs3yBriSaVchRwdOk0abTiQ-egDHDcEvxLAZqZu0JwuCOjbkPdx4cr51wxIdlX6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/SBoxxx/21249" target="_blank">📅 19:35 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21248">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">وزیر خزانه‌داری آمریکا:
به احتمال زیاد، اقتصاد ایران در دو هفته آینده فرو خواهد پاشید
انزوای اقتصادی ایران به صورت مرحله‌ای اجرا می‌شود و ارزهای دیجیتال، هوانوردی و حمل‌ونقل دریایی را در بر می‌گیرد.</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/SBoxxx/21248" target="_blank">📅 19:35 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21247">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">حرف درستی است. به این پفیوزها گاز و برق ندهید دستکم خودمان اینقدر قطعی نداشته باشیم.
زیبنده ابرقدرت چهارم دنیا نیست.</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/SBoxxx/21247" target="_blank">📅 19:19 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21246">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qAavkaRflUzB_LufEr-SFWegQmqPEwfiGCEWGUWlQzRSQ4wd7B2lrGY5f_NsNV12QqByjrNoWU4iIoEqGCeo3UaPgX7o-dQoEQf8UaAinvS2XrsyVE0_iqAKhlL-D31QRpiDClBMQWQA9bpImGUiGBpBsGZQ4I6yOTsLSpgVZFLZM2c3azzY4KYJL2Kupe_tz3XY3tQW1JIvpEeKOeFx21rIY1sLu8TmTRKoabuCSAeh_hfTHQBB_lr9qTzAWmpWIMBPcua0fLc5CQKzY3YN4clavb8oPcyYB_qDePZbJ7R5z14Hd7qx7bnvj0nAA5zqog6nTJigCbCyO4Q5zB7LXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی دریایی سپاه پاسداران انقلاب اسلامی ایران امروز مدعی شد که یک پهپاد زیرآبی خودکار ساخت آمریکا به نام Remus 600 را در نزدیکی تنگه هرمز به دست آورده است. نام‌گذاری نظامی این وسیله توسط ارتش آمریکا، Mk 18 Mod 2 Kingfish است.</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/SBoxxx/21246" target="_blank">📅 19:12 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21245">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">رابرت کیوساکی (Robert Kiyosaki)، نویسنده کتاب «پدر پولدار، پدر بی‌پول»، به دارندگان حساب‌های بازنشستگی هشدار داد که ممکن است فروپاشی‌ای در مقیاس سال ۱۹۲۹ در راه باشد، و بیش از یک سال بعد، این فروپاشی رخ نداده است.
کیوساکی در ژوئیه ۲۰۲۵ در ایکس نوشت: «آیا حساب 401(k) یا IRA دارید که پر از سهام است؟» او به وارن بافت (Warren Buffett)، رئیس برکشایر هاتاوی (Berkshire Hathaway)، و جیم راجرز (Jim Rogers)، هم‌بنیان‌گذار صندوق کوانتوم (Quantum Fund)، اشاره کرد و مدعی شد آن‌ها بیشتر یا همه سهام و اوراق قرضه خود را فروخته‌اند و پول نقد یا نقره نگه می‌دارند. او افزود: «اگر نمی‌دانید چرا بافت و راجرز سهام و اوراق قرضه‌شان را فروخته‌اند، ممکن است بخواهید علتش را بفهمید.»
او جایگاه خود را متفاوت توصیف کرد. کیوساکی نوشت: «من محکم روی طلا، نقره و بیت‌کوین می‌نشینم» و سپس افزود: «ممکن است در آستانه فروپاشی دیگری مانند ۱۹۲۹ و رکود بزرگ دیگری باشیم.» او همچنین هشدار داد که بدهی آمریکا از کنترل خارج شده است و این کشور فقط «تا مدت محدودی» می‌تواند به چاپ پول ادامه دهد.
البته این پیش‌بینی محقق نشده است. شاخص S&P 500 به صعود خود ادامه داده و در سال ۲۰۲۶ به بالاترین سطح تاریخی رسیده است، نه اینکه فرو بپاشد.
کیوساکی همچنان درباره سهام، صندوق‌های قابل معامله در بورس (ETF)، صندوق‌های سرمایه‌گذاری مشترک، حساب‌های 401(k) و IRA هشدار می‌دهد و در همان حال طلا، نقره و بیت‌کوین را تبلیغ می‌کند. استدلال اصلی او ثابت مانده است: سرمایه‌گذاران نباید صرفاً به این دلیل که دارایی‌های سنتی آشنا هستند، فرض کنند که امن‌اند.
تمایز مهم، میان آماده شدن برای یک رکود و تلاش برای زمان‌بندی دقیق وقوع آن است.</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/SBoxxx/21245" target="_blank">📅 19:10 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21244">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aHV-r2tvwe-sL6eB5kenkfdG6Ki_urNBKyDNDdP9WSTdiojFQWgwsjq_MNirbg1Okrt437tIsKUJvuq4go_bNO9BkW0pNN1kmUJlC1q4libA84KTe2WI33XxCdce6517tqzKXP6pMs4RX3aGUPdb0GMDwTPiGJ9r96_krE2PeTQQrbQJ_JHE0OdHsao2Q6_ryWtzKCy0m0pRVZ21HADMdkR3SCpdP3YLIYeFs-gkRhvIFJZybPRRx900g3vK34KeFeACciXAIVxQ8GXJUjgdWsPRRBTFivzHuV_UQAV68HT16z4AyQuQ5Aem0VvwBXNNhfLTS32e6v_v88O5VuWSNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SBoxxx/21244" target="_blank">📅 17:11 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21243">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">حاجی‌بابایی، نماینده مجلس:  ایران باید با قدرت [مسیر] انرژی را بر روی همه ببندد؛ یا همه یا هیچکس  نایب رییس مجلس با بیان اینکه امروز مقاومت با محوریت ملت بزرگ ایران تازیانه الهی بر فرق ترامپ جنایتکار است، گفت: تنگه هرمز همان دریا و همان رودی است که فرعون در…</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/21243" target="_blank">📅 13:24 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21242">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">حاجی‌بابایی، نماینده مجلس:
ایران باید با قدرت [مسیر] انرژی را بر روی همه ببندد؛ یا همه یا هیچکس
نایب رییس مجلس با بیان اینکه امروز مقاومت با محوریت ملت بزرگ ایران تازیانه الهی بر فرق ترامپ جنایتکار است، گفت: تنگه هرمز همان دریا و همان رودی است که فرعون در آن غرق شد؟ آیا آمریکا در منطقه و در تنگه هرمز در نبرد با ملتی که خدایی فکر می‌کند و توحیدی فکر می‌کند غرق نخواهد شد؟ دیپلماسی با قدرت امکان‌پذیر است و ما باید حرفمان را از قدرت و اقتدار و جایگاه قدرت اقتدار بزنیم.</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/21242" target="_blank">📅 13:23 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21241">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">باز هم تاکید میکنم خواهرمیانه جای مبتدی ها نیست :
حکم ۱۰ ماه زندان حمید رسایی اجرا می‌شود</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/21241" target="_blank">📅 12:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21240">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m7n_VT9iISkua7NBm6q_RybfqY5Su7MBqNlpzLTEVQyLS_BXBbZS4e4ockPkjTf1grVA9WTADybIZ75gzG78Dsp5MRKThas4-Zy78MkGPwWRypsetzVhzCQUgesk7Ckui1LwVfO-rN9vZ6fx-Xt51KhAUm4mCsWeABiOrC0u_RZ3h5fiGXPrg12WoOfA5EpFv7vzIfUhF8Aevwx_UGHG-OCk2jGJSdwHVVZCK7ILP2IAI1Fm3jDDwBLQZj_zok7Prp47MAexVyd_PfZFNf8flALx-IVq2TKEWJlk4nQfzNak--apkXXkPufDCzte0fHqvXv94RiffbnniRt4bwZc7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خواهرمیانه برای مبتدی ها نیست!</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/21240" target="_blank">📅 12:10 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21239">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">وقتی برخی سرمایه گذاران به امانتداری بانک انگلستان با ۴۰۰ سال سابقه برای طلایشان شک می‌کنند؛ در عجبم از ملتی که در پلتفرم های آنلاین ایرانی طلا میخرند!  راستی میدانستید آلمان چند سال است از آمریکا درخواست انتقال طلاهایش از فدرال رزرو به انبار بوندس بانک در…</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/21239" target="_blank">📅 10:28 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21238">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">سپاه
پاسداران:
در یکی از بزرگترین عملیات‌ها  دقایقی پیش 7 نفتکش اماراتی در تنگه هرمز مورد هدف قرار گرفتند</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SBoxxx/21238" target="_blank">📅 09:15 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21237">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">یک نفر دایرکت داده خب استاد ما که به قله رسیده و سرش نشسته ایم، حالا اگر پنبه نایاب شد بیاییم خود قله را آغشته به روغن بنفشه کنیم!</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/21237" target="_blank">📅 09:05 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21236">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ترسم این است که پنبه هم نایاب شود؛ آن وقت با چی روغن بنفشه را داخل آنجایمان قرار بدهیم؟!  اصلاً آدم یک جوری می شود!</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/21236" target="_blank">📅 09:02 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21235">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">شیوه درست استفاده از روغن بنفشه</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/21235" target="_blank">📅 09:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21234">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/134b1ed686.mp4?token=PGUW7fnOWkYEhUDBdBwuNeuAYGQseE1k4X15ZJpvq-GEKaxMA3wQWznlwWa_zP1AZ8UL9e5--i7fjCovkVi1G6cOpvBRZhnncOmSF0WY0-i1YaiGAOCimqHDBVmqygeRNJ0hsFHSR7U79txe_I99SAahmuL4ujFKvHgGHjGHTXDeAd1mQXRIlQAYxEH15z7aj_-LfxkXFYvrRndUYZ7-xRxKrkespOCj1fHaC52vWobF32xaJR2uR3NE8UVuZZ85AiIXEE9GJDa9qZp2kCj3gUBOXlS73mTmMvGXuROgm3lpiAthhaOG0VLwInre_QYMMEVlmpnd8nzYouElQdf-PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/134b1ed686.mp4?token=PGUW7fnOWkYEhUDBdBwuNeuAYGQseE1k4X15ZJpvq-GEKaxMA3wQWznlwWa_zP1AZ8UL9e5--i7fjCovkVi1G6cOpvBRZhnncOmSF0WY0-i1YaiGAOCimqHDBVmqygeRNJ0hsFHSR7U79txe_I99SAahmuL4ujFKvHgGHjGHTXDeAd1mQXRIlQAYxEH15z7aj_-LfxkXFYvrRndUYZ7-xRxKrkespOCj1fHaC52vWobF32xaJR2uR3NE8UVuZZ85AiIXEE9GJDa9qZp2kCj3gUBOXlS73mTmMvGXuROgm3lpiAthhaOG0VLwInre_QYMMEVlmpnd8nzYouElQdf-PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عزیزان پنبه و روغن بنفشه به همراه داشته باشید که داروهای مدرن نایاب می شود.  در ضمن انجام سرویس تعویض روغن به صورت رایگان انجام می شود.</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/21234" target="_blank">📅 08:59 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21233">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sZR2R3BXR9ojj7XnTPt5RCpzIwHIVbUfi5wtfUzDN3med5MoW7bOrymHaQhh7zbpVmYHZ4AXQUTv8uTjUkLI2Nq4mVZyNOgRTtdaLqFUyQFZAginAwjZyyln67mqDUnMrEPZFQN_lMeFugH5qx5Y7MLIJCfXYv2zCgHulendpfDVge6mqHQADigMxN-bkVm1TBhnsiBvFTjm2AQwJxpp0z2BacQFGxLM9KHHjfLTX4JARdtolVqhIrdd55OCxs3qop-HgAR8NMt0UffgrvrrDMAVyT5W0V-Ije0oOL0V-1HU3bNU9dimAoRKbawha5c_j8UU_wcFBpYmElEohIQTqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عزیزان پنبه و روغن بنفشه به همراه داشته باشید که داروهای مدرن نایاب می شود.
در ضمن انجام سرویس تعویض روغن به صورت رایگان انجام می شود.</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/21233" target="_blank">📅 08:57 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21232">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">بوی محاصره زمینی می آید…</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/21232" target="_blank">📅 08:07 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21231">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">حملات موشکی گسترده سپاه در تنگه هرمز</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/21231" target="_blank">📅 07:11 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21230">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FL3KT-dWbnkz-jIjsBwL2vVnVbhNv-vnJyVxc-GwtnutvK1vVQNdpizB7qGuI2goYaW6uRuTvk22vV5Z8-ECf5C6t9khoQKdn3D4SnBdyLBmPWBShpB_CZGz-st9GWerwj09QqA6wlc12Fj9aXioJQfHrjpbTb31gfOO9qcTgvGmntx_98kEeVp3yXqmBz0ThVvlHO_rmFyFAdd2qoYiWuFExJfYosMznxM3kcykGU7tgmFTu2Yg06y26dy0ou1DMSRkABIqSdFxkgK30A_uQlFWd98l3i8NhCPesQmRB-0YHxLLtVl68jaSZGakg4sQG3eXwBfai9wIKsMU0I4uJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاید براتون جالب باشه
فرودگاه نجف عراق که اجازه پرواز به هواپیماهای ایرانی رو نمیده ،
توسط جمهوری اسلامی ساخته شده
😄
شب خوش!
@PiknikAnalyst</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/21230" target="_blank">📅 01:15 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21229">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">واشنگتن و پکن؛ پیام مشترک درباره ایران و تنگه هرمز
در یکی از قابل‌توجه‌ترین بخش‌های دیدار اخیر دونالد ترامپ و شی جین‌پینگ، موضوع ایران نیز در گفت‌وگوهای دو رهبر مطرح شد؛ موضوعی که می‌تواند برای تهران و به‌ویژه آینده تنگه هرمز اهمیت ژئوپلیتیکی قابل‌توجهی داشته باشد.
بر اساس فکت‌شیت منتشرشده از سوی کاخ سفید، ترامپ و شی درباره نگرانی‌های جهانی از جمله ایران گفت‌وگو کردند و بر دو اصل تأکید داشتند: ایران نباید به سلاح هسته‌ای دست پیدا کند و هیچ کشور یا نهادی نباید برای عبور از آبراه‌های بین‌المللی عوارض تعیین کند.
اگرچه در متن جدید نام «تنگه هرمز» به‌طور مستقیم ذکر نشده، اما این بند در شرایط کنونی به‌وضوح با مناقشه هرمز ارتباط پیدا می‌کند. اهمیت موضوع زمانی بیشتر می‌شود که بدانیم در مواضع قبلی واشنگتن و پکن، مسئله بازگشایی هرمز و مخالفت با دریافت عوارض برای عبور کشتی‌ها صراحتاً مطرح شده بود.
از منظر تهران، نکته مهم صرفاً محتوای این دو موضع نیست؛ بلکه هم‌زمانی مواضع واشنگتن و پکن اهمیت بیشتری دارد. چین بزرگ‌ترین خریدار نفت ایران و یکی از مهم‌ترین شرکای اقتصادی تهران است و در بسیاری از پرونده‌های ژئوپلیتیکی در برابر فشارهای آمریکا موضع متفاوتی داشته است. بنابراین هم‌صدایی آمریکا و چین درباره اصول مرتبط با هرمز می‌تواند فضای مانور دیپلماتیک ایران را محدودتر کند.</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SBoxxx/21229" target="_blank">📅 20:26 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21228">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B8mPpF7WVFaZ1BExG_HdqnU67KPGw-96n5wSSNCzPCz7cIqzPY_kAjSy5X7JibZiSXLwBpMuKObifKbBNhltj1zz3qyPqaeWXVa2WExlOPymCQVav9Pfmtb5SCNOiihuGcUvEHDwv5rtbF_bTOBPTit2fpPZ6lftWF7O4Tzyakint6FRgr65I0CB4mdKr1STW254dMDtkeXo9QEsIoq5D7pUIHPZviFQ3OfYSojQjJSXUK3CBZVh5IRP_8xXQfQa3VJc7P6PpoVCZySxRdxPWrwU0bbxBvS1Ne4n1d8QfMwAu7X1BBLZtqLGIB4ZDAgk-RheAWtbgwyixRYdFFwpoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجم عملیات انتقال کشتی‌به‌کشتی (STS) در دریای عمان نسبت به سطح ماه فوریه، ده برابر شده است.
تولیدکنندگان نفت را بارگیری کرده و با عبور از تنگه هرمز از طریق مسیری جایگزین که امنیت آن توسط ارتش آمریکا در نزدیکی سواحل عمان تأمین می‌شود، محموله‌ها را برای تحویل به خریداران نهایی به کشتی‌های بزرگ‌تر منتقل می‌کنند.</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SBoxxx/21228" target="_blank">📅 19:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21227">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">شورای عالی امنیت ملی:  «ادعاهایی مبنی بر اینکه ایران به محدودیت‌های اخیر هوایی با اقدام نظامی پاسخ خواهد داد، نادرست است.  مذاکرات با کشورهای ذی‌ربط برای لغو ممنوعیت‌های غیرقانونی پرواز به‌طور فعال در جریان است.  در صورت لزوم، اقدامات متقابل غیرنظامی برای…</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SBoxxx/21227" target="_blank">📅 18:21 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21226">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">مخبر، مشاور رهبر انقلاب:  پرواز در منطقه یا برای همه آزاد است یا برای هیچ‌کس  اگر ایران امکان پرواز و دریافت خدمات فرودگاهی نداشته باشد هیچ کشوری در منطقه هم این امکان را نخواهد داشت.</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SBoxxx/21226" target="_blank">📅 17:55 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21225">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">پسری ۹ ساله ارمنی‌تبار مسیحی در اورشلیم، پس از آنکه به دلیل دوچرخه‌سواری و استفاده از هدفون در روز عید یوم کیپور مورد اعتراض قرار گرفت، توسط شهرک نشینان یهودی با اسپری فلفل مورد حمله قرار گرفت.
تصاویری که از
کانال ۱۳
اسرائیل پخش شد، نشان می‌داد که این کودک که نامش ویلیام است، پس از این حمله در حال دریافت درمان پزشکی از سوی تکنسین‌های اورژانس در یک آمبولانس است. این درگیری در نزدیکی شهر قدیم رخ داد، زمانی که ویلیام در حال دوچرخه‌سواری و گوش دادن به موسیقی بود.
گزارش‌ها حاکی است که مهاجمان از پسر خواستند هدفون خود را در بیاورد. پس از آنکه او این کار را انجام داد و به زبان انگلیسی صحبت کرد، فریاد زدند: «انگلیسی نه، یهودی‌ها» و سپس مستقیماً اسپری فلفل را به سمت او پاشیدند.</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SBoxxx/21225" target="_blank">📅 15:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21224">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">وزیر امور خارجه آذربایجان، بایراموف:
اگرچه دهه‌ها درگیری با ارمنستان تراژدی عظیمی بر مردم ما تحمیل کرد و زخم‌های عمیقی بر سرزمین ما باقی گذاشت، آذربایجان انتخاب کرده است که به آینده نگاه کند و صفحه دشمنی را ورق بزند.
ما صلح را به ارمنستان پیشنهاد دادیم که کاملاً مطابق با هنجارها و اصول حقوق بین‌الملل و مبتنی بر شناخت متقابل و احترام به حاکمیت و یکپارچگی قلمرو یکدیگر است.</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/21224" target="_blank">📅 14:31 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21223">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">حقیقتا خواهرمیانه جای مبتدی ها نیست!  از ۶ ماه پیش بلایی نبوده که جمهوری اسلامی و نیروهای نیابتی اش سر این سعودی های فلک زده نیاورده باشند؛ بعد این هفته جشن باشکوهی به مناسب ۹۶-امین سالگرد تاسیس کشور سعودی در قلب تهران برگزار شده!  سبحان الله!</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/21223" target="_blank">📅 14:11 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21222">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NpLa_byTCitQJmZjr3ml5PUTM7MP5ViPIcSHJWxB3l6uU0qIQ0aHFKg7bf9rHHPvfzPHyh49mg1CunR8kWNRxViU2U3zVmpbZviuNIWdueL85T-YAQ3f5LaqGa9-Brbh0Mong92sfrbvEYaXq9EdLQ0Ffm2hk6Z_0CMXZ1ClQ9CkDnCafuw3LyXp5fpc74T0sq85OJynwtJP02ou5umnEFHedOBBs-HIGgNlp6YqNIODg09ZkSfweqYQvA0kuI8gC_Y0VDDlHXF31kbG9ECcM3lJNFmHtRt97HmnGxLZ8kaFsHszTA5wbDj2n1H6bn2KNh4O8j27jxAvfFek4vN65w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برآورد درصد مسلمانان نسبت به جمعیت هر کشور در اروپا در سال ۲۰۵۰</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SBoxxx/21222" target="_blank">📅 13:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21221">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/thWIVftY6U7cc8xSvJTrGsYd1aiXdodcOK6L6YqfY1mk3PygJ-ztd1aiNV7AoN7dbMC5CyO7MT5HSdvwLXhY3xa-3WKs0vxEjnL0znynS9LH7nA05axib8gnAHpBuubA9LtSD37CIOVuDpWlpaeNmYxA0sWn8XM3aePjDUpEqO0KZJEakgNwV7t4TLmktTHLVBViAnCeFmTtOG4nT8KD3py3JmKLyFtQfvjfBHacjTawH-s-hIrMeGpKBQ6BaaOVRpzzjD0wyFslKQeElaqucoG0ahSbKsf2VcZf10n72990oOhGcLkzh4Hpl04Iq6NAQr8lHz19gfIcirYojrCxiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اشاره دوباره ترامپ به تنگه هرمز به عنوان تنگه ترامپ !</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/21221" target="_blank">📅 13:19 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21220">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ترامپ، رئیس‌جمهور ایالات متحده، پیشنهاد ایران برای آتش‌بس هفت‌روزه را رد کرد و به دستیاران خود گفته است که انتظار دارد بمباران‌های آمریکا علیه ایران پس از انتخابات میان‌دوره‌ای نوامبر از سر گرفته شود.  طبق پیشنهاد ایران قرار بود تنگه هرمز بازگشایی و مذاکرات…</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/21220" target="_blank">📅 08:33 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21219">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07644aa8e4.mp4?token=QlevFCG2-9DDkXe6f5QYaEA3qiyfWf5zqPHaOIDWYSAA9zvjP3m5FyHjaN9Hzxp9t6Pdn8ALtX_r_WOmSnwKtTbJtwD1WVBhI37BaPc4qjiFRVks7EQ88MT21T8OdQxcLOLFPJmnp73IH1QfsdIAfHkLrZ9HhyoJKoneYy2oIGKnox7TWOZNYpomYMvAf-oU-LAyyHaW3HXjLBUy86-JXa-TLvKvk9Ef60oopeI6AguZ8uUovKvrfnsjUxf-Un_pA65p6nI91-r2jDBIqLFwajhfYqnyTPgkK9Q05TD02MpNfkeWQbpHBsrND0__v5xalgHDWg0ebsvMe0BPW21lpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07644aa8e4.mp4?token=QlevFCG2-9DDkXe6f5QYaEA3qiyfWf5zqPHaOIDWYSAA9zvjP3m5FyHjaN9Hzxp9t6Pdn8ALtX_r_WOmSnwKtTbJtwD1WVBhI37BaPc4qjiFRVks7EQ88MT21T8OdQxcLOLFPJmnp73IH1QfsdIAfHkLrZ9HhyoJKoneYy2oIGKnox7TWOZNYpomYMvAf-oU-LAyyHaW3HXjLBUy86-JXa-TLvKvk9Ef60oopeI6AguZ8uUovKvrfnsjUxf-Un_pA65p6nI91-r2jDBIqLFwajhfYqnyTPgkK9Q05TD02MpNfkeWQbpHBsrND0__v5xalgHDWg0ebsvMe0BPW21lpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی عبدی برنامه آمریکا و اسرائیل برای جنگ بعدی علیه ایران را نفوذ آبی و خاکی و هلی برن از سمت خلیج فارس، غرب(عراق)، جمهوری باکو، آسیای مرکزی و جنوب شرق (پاکستان) دانست و تصریح کرد حملات هوایی، تلاش برای شکار شاه مهره و استفاده از بمب اتمی تاکتیکال نیز رخ خواهد…</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SBoxxx/21219" target="_blank">📅 08:15 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21218">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ترامپ، رئیس‌جمهور ایالات متحده، پیشنهاد ایران برای آتش‌بس هفت‌روزه را رد کرد و به دستیاران خود گفته است که انتظار دارد بمباران‌های آمریکا علیه ایران پس از انتخابات میان‌دوره‌ای نوامبر از سر گرفته شود.
طبق پیشنهاد ایران قرار بود تنگه هرمز بازگشایی و مذاکرات هسته‌ای در ازای رفع محاصره بنادر ایران توسط ایالات متحده و کاهش فشارهای اقتصادی بر تهران، از سر گرفته شود.
— وال استریت ژورنال</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SBoxxx/21218" target="_blank">📅 07:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21217">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">سفیر ایالات متحده در چین، گفت که رئیس‌جمهور ترامپ در مذاکرات خود در کاخ سفید، از رئیس‌جمهور چین، شی جین‌پینگ، خواسته است تا هرگونه کمک چین به ایران را متوقف کند.
او اظهار داشت که واشنگتن به وضوح اعلام کرده است که «هرگونه کمکی که چین به ایران ارائه می‌دهد، کاملاً غیرقابل قبول است».
او افزود: «ما از قبل حرکتی در این زمینه مشاهده کرده‌ایم. این همان تعهدی است که داده شده است. آن‌ها به ما اطمینان دادند که چنین کاری انجام نمی‌دهند.»</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/21217" target="_blank">📅 02:22 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21216">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">فیلم کامل مستند BBC درباره نسل کشی ترکیه ضد کردها در عراق</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/21216" target="_blank">📅 00:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21215">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ada5e22fc.mp4?token=F5uDk5NIdOwhU_5g16jbO_lW0mn7zeXOMp1sPzMmYRmQQfLZ-SKH4pdQafTA5KjG4GfCoM14uVyPo_KTB2LmDLnu-UR5octFF21MqFsqPmz4ikWKeSdIxHwmlrIQoMvDBoDRLGQiycFO-oZhnkqUHjd5xRzwJMe1I3jSmqjyk-XruDuOL5Vt25Ewo2umeEy5acqdJ1lAyz3eXkiJf1dr90Hmy_3DoNtK6rh_egtAg7IWp2SQ4n1LpozCc5J0KOl85umGUlvx_M3du9xQwoYhuNXY5-9dUlirWF36C3IK-PGaX6XwqeSIAoFUSugHL_38INA-oawiXbb2df0pshfiOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ada5e22fc.mp4?token=F5uDk5NIdOwhU_5g16jbO_lW0mn7zeXOMp1sPzMmYRmQQfLZ-SKH4pdQafTA5KjG4GfCoM14uVyPo_KTB2LmDLnu-UR5octFF21MqFsqPmz4ikWKeSdIxHwmlrIQoMvDBoDRLGQiycFO-oZhnkqUHjd5xRzwJMe1I3jSmqjyk-XruDuOL5Vt25Ewo2umeEy5acqdJ1lAyz3eXkiJf1dr90Hmy_3DoNtK6rh_egtAg7IWp2SQ4n1LpozCc5J0KOl85umGUlvx_M3du9xQwoYhuNXY5-9dUlirWF36C3IK-PGaX6XwqeSIAoFUSugHL_38INA-oawiXbb2df0pshfiOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اثرات خانمانسوز جهش دلار روی مغز مردان سرزمینم!
گفته می شود ایشان قبلاً پرایس اکشن کار بوده که بعد از 36 بار کال کردن اکنون وارد مباحث تشکیل سبد و تخمگذاری در آن شده است و گرنه این حجم از آشنایی و تسلط بر مفاهیم بازاری نمیتواند از دهان یک اسکل معمولی بیرون بیاید!</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SBoxxx/21215" target="_blank">📅 23:23 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21214">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">علی عبدی برنامه آمریکا و اسرائیل برای جنگ بعدی علیه ایران را نفوذ آبی و خاکی و هلی برن از سمت خلیج فارس، غرب(عراق)، جمهوری باکو، آسیای مرکزی و جنوب شرق (پاکستان) دانست و تصریح کرد حملات هوایی، تلاش برای شکار شاه مهره و استفاده از بمب اتمی تاکتیکال نیز رخ خواهد…</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/21214" target="_blank">📅 23:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21213">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">— تًن ماهی — گوشگیر سیلیکونی — آب معدنی — چسب زدن شیشه ها</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/21213" target="_blank">📅 23:09 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21212">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">علی عبدی برنامه آمریکا و اسرائیل برای جنگ بعدی علیه ایران را نفوذ آبی و خاکی و هلی برن از سمت خلیج فارس، غرب(عراق)، جمهوری باکو، آسیای مرکزی و جنوب شرق (پاکستان) دانست و تصریح کرد حملات هوایی، تلاش برای شکار شاه مهره و استفاده از بمب اتمی تاکتیکال نیز رخ خواهد داد، ولی پیروزی از آن ملت ایران خواهد بود.</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/21212" target="_blank">📅 23:07 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21211">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">به پزشکیان رای دادیم که جنگ نشود، هر هفته 15 بار جنگ می شود!</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/21211" target="_blank">📅 23:04 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21210">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">به پزشکیان رای دادیم که جنگ نشود، هر هفته 15 بار جنگ می شود!</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/21210" target="_blank">📅 23:03 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21209">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">خداوکیلی راست می گوید ؛ این بار دیگر غافلگیر نشویم!</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/21209" target="_blank">📅 23:02 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21208">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JHe3sOqKsTESlrMQmr7s_7ZTPKVbjG982LYkbwJeWTaMnNfAtm4FmK4VJXfniPfwL2vmMpRbuazgFh78x_cRf86hV3OEcXIE7JYZ_RC8X8eAannCxAYpy8UkoS5ssuILVKjIciDEOVDZ4W5aQStg4yCZw9Fwb1vJUS22uZufGz8kxIrno0ED0MjE0QXrD9JgMEkM24GOqTzw-d5aMngRptvdA210F674AKmWESVVX1MjUr0iOQm0mqpCI80FeBujZ2GED6NYdYZZV7B5FNIMf3nG79RUrMWvwFFFExZWP61kn9MX8Mb94A-RGe93BAIBZ2-Qg1L4eUZoNcl-Pg9D3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من شخصاً هیچ وقت به نزدیک بودن توافق ایران و آمریکا توجه نمی کنم ولی اعتقاد دارم نزدیکی ایران و آمریکا نزدیک است.</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/21208" target="_blank">📅 23:01 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21207">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">چرا می خند؟!</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/21207" target="_blank">📅 22:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21206">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GkdU29kdZJPnRVn2IhbWSRRSboCasvXIUkORLP4jd0hCFu9sAciqIuuEgZ_gYqZYGOfYWt6ubQa0_Z3YR0zMXiYOkLgWAul9K5S04MUN8v9DiCYL_FGMHPPZH9q5GBBZFko3MSKJjUSCxtCrKcGq-EBf20rEW4V-HVr9iBfk4zauBi0XIu8hZaGv3weD7u-Y_4NCIES1oeSzbViZBbOpPoDk5B9PztbWzEY5zl8LPktFf0FBm3Al5zYZjWc2nkiPQ6gXluwP2VLhuqX5pZy7KIL5BnZh7fLYwkCvu3pOjWsUrWGNCFOZanMebCgFuK1rLKHv6oVgGoxpO9SAJEzP2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">First Time ?</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/21206" target="_blank">📅 22:54 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21205">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">مرندی ذوالاکتاف:
هیچ پیشرفتی در مذاکرات غیرمستقیم با رژیم ترامپ حاصل نشده است. منطقه به سوی تشدید تنش پیش می‌رود، چرا که دیکتاتوری‌های حوزه خلیج فارس که در جنگ علیه ایران همدست بوده‌اند، به توطئه ترامپ و بسنت علیه ملت ایران می‌پیوندند.</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/21205" target="_blank">📅 22:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21204">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xq5CgiQH4g-adZoLJeYONeXfwVfm7icHbcZHVTvqNFr4oQT9dHA7Q2FVpGyhLwyz1UIoDG8FbngFkF07UyDg1PhNOgL6sf24ncJDki7LYlvDUbN1mHttEWiZkxFDmxjlIT7sAN1uJhC_53gDHfPWAJKohweGPp45pLn0F7B68b2aDV2wAax957qCAO8Vyf11NLJwWPLzdCq5yUSCIBsmUkZg_Ek2jLMPvKRGIx0OGalGRoTJ7NU9jLb3Fdm2EwcFLJVEiXPn2AYTWbQHxu8W9YXqpG6AEsws9ZBG7WHur--G2Yj8TKYctl3ymxx2UYkOHp9fkUBSY7odWDmHVy8oww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محدوده 4255 بسیار مهم است.</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/21204" target="_blank">📅 22:41 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21203">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TLxIU-3puk8LYSsQ_sDCXd7Y7yhtvQXs8LaI1wBR2pfghtdh_UeJSur-nMMNrl8xabL2NwnH5eG8AlJDqFbikF9tdOmENKzp6ocf62WHRSfJPXa4TI4WbeFLEy3j0IglxnZtOLybr4csvu9I8b-ID6lHf-Nh32bZxFXXEmnM2FOK_K72fB5fCAJnmuYhWXu_e1m5WWGtFG7gHeuNU1DRhQKWadnyaGRTptmCZgOWZ2p3q7gWIjhglHFBwYZcSqAe1KBtvx3Uh2tMPtK1jiVALEvu_kVRsvDeHLv3xHfJ1-H-wauWoi_QG5pQ7BLuLQglmK0cLeuzi7JjgrY2IJsHiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حقیقتا خواهرمیانه جای مبتدی ها نیست!
از ۶ ماه پیش بلایی نبوده که جمهوری اسلامی و نیروهای نیابتی اش سر این سعودی های فلک زده نیاورده باشند؛ بعد این هفته جشن باشکوهی به مناسب ۹۶-امین سالگرد تاسیس کشور سعودی در قلب تهران برگزار شده!
سبحان الله!</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SBoxxx/21203" target="_blank">📅 21:19 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21202">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">Ali SharifAzadeh – انتخابات اسرائیل</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/21202" target="_blank">📅 21:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21201">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ترامپ
:
در نوامبر در چین دوباره با شی ملاقات خواهیم کرد</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/21201" target="_blank">📅 20:49 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21200">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">First Time ?</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/21200" target="_blank">📅 20:33 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21199">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">‏ قائم‌پناه:
به عربستانی‌ها گفتم انشاءالله برد موشک‌های ما به آمریکا برسد تا دیگر به پایگاه‌ آمریکا در کشور شما حمله نکنیم بلکه به خود کاخ سفید موشک بزنیم.</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SBoxxx/21199" target="_blank">📅 20:17 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21198">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">سفیر آمریکا در چین:
پکن در پی هشدار ترامپ، بخشی از حمایت‌ها از تهران را متوقف کرده است</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/21198" target="_blank">📅 19:31 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21197">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">میانگین 200 پیپ</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/21197" target="_blank">📅 18:08 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21196">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">#FairValueCurve  نمایه FVC در حال نزدیک شدن به کف محدوده بیش—فروش است.  در این شرایط پرتناقض، بهترین استراتژی فروش در مقاومتهای نزدیک (4292 و 4308) با تارگت 4235 می باشد.</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/21196" target="_blank">📅 16:57 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21195">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">رئیس اسبق سیا:   امکان تصرف خارک برای آمریکا وجود ندارد</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/21195" target="_blank">📅 16:22 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21194">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">کارشناس صداوسیما:   در صورت اشغال جزیره خارک توسط آمریکا، خاک بحرین را پس می‌گیربم</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SBoxxx/21194" target="_blank">📅 16:22 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21193">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔴
عربستان سعودی ارسال نفت به اروپا را لغو کرد!</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SBoxxx/21193" target="_blank">📅 16:21 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21192">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">بی حجاب ها بیایند توی تجمعات شبانه بعد که تمام شد لطفا خودشان خودکشی کنند</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/21192" target="_blank">📅 16:17 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21191">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">بی حجاب ها بیایند توی تجمعات شبانه بعد که تمام شد لطفا خودشان خودکشی کنند</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/21191" target="_blank">📅 14:56 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21190">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">بی حجاب ها بیایند توی تجمعات شبانه بعد که تمام شد لطفا خودشان خودکشی کنند</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/21190" target="_blank">📅 14:56 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21189">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">خاتمی، امام جمعه تهران:   کسانی که حجاب را رعایت نمی‌کنند نیز شهروند این ملت هستند و حضور آنها در تجمعات و همراهی با مردم کار خوبی است، اما دهن‌کجی به حجاب، خلاف وحدت است</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SBoxxx/21189" target="_blank">📅 14:55 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21188">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">مخبر، مشاور رهبر انقلاب:
پرواز در منطقه یا برای همه آزاد است یا برای هیچ‌کس
اگر ایران امکان پرواز و دریافت خدمات فرودگاهی نداشته باشد هیچ کشوری در منطقه هم این امکان را نخواهد داشت.</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/21188" target="_blank">📅 14:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21187">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">خاتمی، امام جمعه تهران:   کسانی که حجاب را رعایت نمی‌کنند نیز شهروند این ملت هستند و حضور آنها در تجمعات و همراهی با مردم کار خوبی است، اما دهن‌کجی به حجاب، خلاف وحدت است</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SBoxxx/21187" target="_blank">📅 14:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21186">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">خاتمی، امام جمعه تهران:
کسانی که حجاب را رعایت نمی‌کنند نیز شهروند این ملت هستند و حضور آنها در تجمعات و همراهی با مردم کار خوبی است، اما دهن‌کجی به حجاب، خلاف وحدت است</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SBoxxx/21186" target="_blank">📅 14:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21185">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t54UYCrdxt0aj-e_XUvkHTQZJuXVSVFOd5zFylL27w_Qy5sfWBStHd_oitLzA7xW8c-f4kjTBclxh_YSiw2HKYyy2QDWsLCn6J9CJyshg93dmNcz8iuhQuy1VGk_-5g5LKEwB9Fs81BGBciIUdSyu1MNCSxso2hVV8o9R1tojbtOOSw3J8TIfFqSEHo-EYr4As31iNvRHO3tBAiEABcaqEUh7EfFbCnrxefMKLf29vMJWna2AJwJam2kDvjZDvtyeU4ugCwb5X8ZmahRTWUK8F7J6S9hCmphVN5siiJVJo72XytK60lOvKMwpo3NUhfzoI4vBcUvsmG3INYFf2B5AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه FVC در حال نزدیک شدن به کف محدوده بیش—فروش است.
در این شرایط پرتناقض، بهترین استراتژی فروش در مقاومتهای نزدیک (4292 و 4308) با تارگت 4235 می باشد.</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SBoxxx/21185" target="_blank">📅 11:19 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21184">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pu8h4-DYCZYA8H4b2Jdr0EQ-4O7AT3Iihdh9_dM2TQXc8Sp__YNthv7SLFEYv1l2JXaj7rexDgsyB0IWIIAn8KwfQALmnwTEFnJsbVWRiTM6J8oLlruGAlCy4SKjNjhrgAupSHotwr6EucWSCtli_h7VEhVgOIxUlkkpjrZBhJ47Om5TMOVYDfkfGHJ78FqRj7JdjHfphupSNIDgKrf5bR95lONuw9M0OI2EeEgwPOKj2awunc9AXtiRb0g1FOcBESvRMhE2kyOkO508Uwzzus8ICl_dbpCkVUUNWCYvt2Uz21j6oL1CLaZFBEt5kpGABp1_GAaWfQRQ_aVTaZSCzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح بسیار بالایی است و هر بالایی فرصت فروش است.</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SBoxxx/21184" target="_blank">📅 11:14 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21183">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">پاکستان، ترکیه و عربستان سعودی در پی افزایش حملات حوثی‌ها به خاک عربستان، یک جلسه اضطراری رؤسای ستاد مشترک را بر اساس پیمان دفاعی مشترک مکه تشکیل می‌دهند.
این جلسه اولین گام در سطح فعال‌سازی تحت این پیمان است که مقرر می‌دارد هرگونه حمله به یکی از اعضا، حمله به هر سه کشور تلقی می‌شود.</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SBoxxx/21183" target="_blank">📅 10:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21182">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">کلمبیا تمام روابط دیپلماتیک خودش با ایران را قطع کرد
دلایل اجازه ندادن به بازرس ها آژانس  بستن تنگه هرمز رعایت نکردن حقوق بشر و .... بود
یکی از دلایل جالبش رابطه ایران با گروه های مواد مخدر  بود</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SBoxxx/21182" target="_blank">📅 01:49 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21180">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">نتانیاهو:
«آن‌ها اسرائیل را — اسرائیل کوچک — متهم به استعمار می‌کنند. و چه کسی ما را متهم می‌کند؟ در میان آن‌ها، گروهی در بریتانیا و فرانسه هستند.
به نام خدا، آن‌ها این اصطلاح را اختراع کردند — مستعمرات آن‌ها کل کره زمین را در آغوش گرفت.
استعمار؟ لطفاً دست بردارید».</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SBoxxx/21180" target="_blank">📅 22:11 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21179">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9dad7c5c99.mp4?token=jLHhshoOFs3YXLZNzr-Ond38ZYhLs1fLAge5GvU_eOyMl7BA0emlJI4VD5ezD1_X6-03dPYrtL-qhTB_niCqhkAEg2kJ4cuOzm51baYS51zxEB13w2rFSsVhOcj-Rbx1wxEcIZtjnfS4JiSgWgzny_BapiFPeRAYJlrfmkIgD1KebJp2uo3kg1fC-Rzzl5qdlvWJg-MrvFYbREjppbvhvkKmccHptO7VwZUQ4KyBRH4ReisgRoyKf2KPV8expeozAlwp2fuCc_MDK2CmE43ZiO5n9l0zZ85yDcE4PNB-BGHYuS4cwpSbNsaJgYsEUPrm7X02HcY3mTDE3lBKGC83-WmthO3gcPIo5IY2rXqb7lVc-K9j5BNaiHya-kJBda0JY_7AQCl7_qUPTSS09rX5bru-bl5q5tXJZFK5DvlKdbIISruyEXjM_m5xiQZM4rzEYUOhHmH18H5TK1ezW6pnTgYpUykZccikbbAnOQC1OFbY9YFuk25zRA8RbMv5gCFvut7x-8Picq7qfiCDEjCRK6DSP4-C3tpqTe-3a5SeljPABBtrSkRH1O0E-kwjcWuaIF--XGEysliiLLLlNhEDA8UuFnemI8R7bBZLsNQS_Ja4JhBB4GC-QBgojGkeDu0Y8kyWbSRvle_dMgEQm71vtal4_yi_PtbODOpQwcl9SRo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9dad7c5c99.mp4?token=jLHhshoOFs3YXLZNzr-Ond38ZYhLs1fLAge5GvU_eOyMl7BA0emlJI4VD5ezD1_X6-03dPYrtL-qhTB_niCqhkAEg2kJ4cuOzm51baYS51zxEB13w2rFSsVhOcj-Rbx1wxEcIZtjnfS4JiSgWgzny_BapiFPeRAYJlrfmkIgD1KebJp2uo3kg1fC-Rzzl5qdlvWJg-MrvFYbREjppbvhvkKmccHptO7VwZUQ4KyBRH4ReisgRoyKf2KPV8expeozAlwp2fuCc_MDK2CmE43ZiO5n9l0zZ85yDcE4PNB-BGHYuS4cwpSbNsaJgYsEUPrm7X02HcY3mTDE3lBKGC83-WmthO3gcPIo5IY2rXqb7lVc-K9j5BNaiHya-kJBda0JY_7AQCl7_qUPTSS09rX5bru-bl5q5tXJZFK5DvlKdbIISruyEXjM_m5xiQZM4rzEYUOhHmH18H5TK1ezW6pnTgYpUykZccikbbAnOQC1OFbY9YFuk25zRA8RbMv5gCFvut7x-8Picq7qfiCDEjCRK6DSP4-C3tpqTe-3a5SeljPABBtrSkRH1O0E-kwjcWuaIF--XGEysliiLLLlNhEDA8UuFnemI8R7bBZLsNQS_Ja4JhBB4GC-QBgojGkeDu0Y8kyWbSRvle_dMgEQm71vtal4_yi_PtbODOpQwcl9SRo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک موزیک ویدیوی Erotic از اتحاد عربستان و فاکستان ببینید شب جمعه ای دلتان باز شود!</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SBoxxx/21179" target="_blank">📅 21:33 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21178">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">رویترز:   آمریکا و ایران درباره توافق مرحله‌ای برای پایان دادن به درگیری‌ها مذاکره می‌کنند</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SBoxxx/21178" target="_blank">📅 20:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21177">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">رویترز:
آمریکا و ایران درباره توافق مرحله‌ای برای پایان دادن به درگیری‌ها مذاکره می‌کنند</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SBoxxx/21177" target="_blank">📅 20:01 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21176">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">اسرائیل می‌گوید حملات جدید علیه ایران «مسئله‌ای زمان» است و تأسیسات هسته‌ای ممکن است مجدداً هدف قرار گیرند.</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SBoxxx/21176" target="_blank">📅 19:15 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21175">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">محدوده 4255 بسیار مهم است.</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SBoxxx/21175" target="_blank">📅 15:51 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21174">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sy3kJ0BgHlfjM2NNrEeh1fqmik2wwfux6sdhvur3l7M4W_Zaf-wRsDHzNv41dIr_BLKXCMmDKpfT-TK1JSZq8ZZCxUddo3QZWbw-32gVEA55W_xtgLiKeXRJBu_fnisasYy8LlEKogGLpBMXfRbiv6dN5gVce6_kz0yGqQUa2s2Z97893uErbRAc2tE5MYJAteY0VDoUaQTzTPMmkbWfe1i96Xj1RDkK3r8TXDobRYasrao5FFVMiGQB8ro8mOoXHMgmkNlJkufPAYnmp68ft957Njmu1kQ3EJaHzt4AwWPo3BLtXF0hcINRxUF8axq9cW7-CozsZa_j8_lU8asZ-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کارشناس صداوسیما اشاره نکرد که اگر ما توان تصرف بحرین را که میزبان نیروهای آمریکایی است داریم، چطور توان حفظ خارک را که مال خودمان است در برابر نیمی از همان آمریکایی‌ها نداریم؟!</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SBoxxx/21174" target="_blank">📅 15:49 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21173">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">کارشناس صداوسیما:   در صورت اشغال جزیره خارک توسط آمریکا، خاک بحرین را پس می‌گیربم</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SBoxxx/21173" target="_blank">📅 15:30 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21172">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">کارشناس صداوسیما:
در صورت اشغال جزیره خارک توسط آمریکا، خاک بحرین را پس می‌گیربم</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SBoxxx/21172" target="_blank">📅 15:29 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21171">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">مرندی ذوالاکتاف:  اگر کشورهای خلیج فارس جلوی پروازهای ایران را بگیرند، ایران فرودگاه‌هایشان را با موشک باران تعطیل می‌کند</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SBoxxx/21171" target="_blank">📅 14:28 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21170">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">یک پرواز از شرکت هواپیمایی وِارِش ایران، که قرار بود از تهران به دوشنبه، پایتخت تاجیکستان، پرواز کند، لغو شد و به فرودگاه بین‌المللی امام خمینی بازگشت.  علت لغو پرواز این بود که اجازه عبور از حریم هوایی جمهوری سلطنتی باکو به این پرواز داده نشد.</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SBoxxx/21170" target="_blank">📅 14:26 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21169">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‏
مصادره ۶ میلیون بشکه نفت ایران توسط آمریکا
تانکر ترکرز مدعی شد:
نزدیک به شش میلیون بشکه نفت خام ایران (به ارزش تقریبی ۶۰۰ میلیون دلار) که توقیف شده، بی‌سروصدا در حال عبور از اقیانوس اطلس به سمت ایالات متحده آمریکا است.</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SBoxxx/21169" target="_blank">📅 14:26 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21168">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b70a5ce7e.mp4?token=hhhvzMkturfVFqydlDX-PkaI1298FFX7ypbwv11MootcrT-vk7PI_L9rKkZw4kwsLIPfT4SGE8U8bKHlEYz3Pt9o0rF3OL2ZeyAhEbVPCS0CQC4Rp0S41cF1bZcbRLtgkh0975WhTNAv97uNz8WEDY_gyaRHiw2mo7A73CxoejZQ85k3a2KZMIWG0RjOB-DlSEXkJRzJoHd-qaUIdCqrIWa4xfXWKHSH5CPvRmRzB6alsrw-dAIXpHNUq_JAK9CSs2f9LWEhghIzIFUuvFslQxKVqG5kvtE9Ft1iLmU9kdsXxVXpQhBvWU0nYgwtHx7u3W6xBC8xEuRA2zk4kYPpFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b70a5ce7e.mp4?token=hhhvzMkturfVFqydlDX-PkaI1298FFX7ypbwv11MootcrT-vk7PI_L9rKkZw4kwsLIPfT4SGE8U8bKHlEYz3Pt9o0rF3OL2ZeyAhEbVPCS0CQC4Rp0S41cF1bZcbRLtgkh0975WhTNAv97uNz8WEDY_gyaRHiw2mo7A73CxoejZQ85k3a2KZMIWG0RjOB-DlSEXkJRzJoHd-qaUIdCqrIWa4xfXWKHSH5CPvRmRzB6alsrw-dAIXpHNUq_JAK9CSs2f9LWEhghIzIFUuvFslQxKVqG5kvtE9Ft1iLmU9kdsXxVXpQhBvWU0nYgwtHx7u3W6xBC8xEuRA2zk4kYPpFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک پرواز از شرکت هواپیمایی وِارِش ایران، که قرار بود از تهران به دوشنبه، پایتخت تاجیکستان، پرواز کند، لغو شد و به فرودگاه بین‌المللی امام خمینی بازگشت.
علت لغو پرواز این بود که اجازه عبور از حریم هوایی جمهوری سلطنتی باکو به این پرواز داده نشد.</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SBoxxx/21168" target="_blank">📅 13:51 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21167">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">پاکستان حملات هوایی متعددی را در افغانستان انجام داد که هدف از این حملات، مکان‌هایی بود که برای ذخیره‌سازی و پرتاب پهپادها استفاده می‌شد.</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/21167" target="_blank">📅 11:29 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21166">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UA_LGy_iyDUVjRHm1f02A9CxaOGwxe1kYLvxkR0gOTHa335GvH6T9_N6tEatT8xjHM4S9IEbHkgs8AidcK9BbzkRg5QHAZBzKbnBTLE5cGs49hmoRJHVaGCV3AbZL2i8NyRjCwUAWb_qXBrokuwY9l8rPOWT0rkutO61WE8IkX786n-pK-sltF2cAPlWI0vvlNYiTGl1aYLCMorZ2lseZqpz8Nlm97ur4g-hT6D0xtbOtrwJwQWKwtrSlc78UTVv_8uAThmDO4GXtG8l2qJ0CaM4yf0_LovAtXYF04_6ql4x-zBVbymey7OYGVs62rZE750WuWVPdAjL4DOrvmA_cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve  نمایه FVC در حال نزدیک شدن به کف خود می باشد.  در این شرایط و با این تناقض، 2 راه داریم:  — صبر برای رسیدن طلا به 4335 برای فروش با تارگت 4230  — خرید در محدوده 4260 الی 4255 با تارگت 4300</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SBoxxx/21166" target="_blank">📅 11:09 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21165">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/21165" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سخنرانی پزشکیان در سازمان ملل اینقدر تند بود که حتی کانالهای ارزشی 6 سیلندر نیز از او ستایش می کنند!</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/21165" target="_blank">📅 11:06 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21164">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">#FairValueCurve  نمایه FVC کماکان نشانگر پایین تر بودن قیمت نسبت به سطح ارزش منصفانه طلا است و لذا خرید توصیه می شود.  محدوده  مناسب خرید:  4302</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/21164" target="_blank">📅 10:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21163">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R0GsMRoidnXL9lFN_QPTrqN7eZCO8fSR-08SoyNnE3fyxZPJzXzkjC55fRkR1idJ68x6_0xbkgVsQhVwx2eZ8YcHoIBHWdRDOFclRZEdKJg6HSMAugrW0hFkXGVSz77PBroHhVVKCE_b1DBKiUumlbfCJ9fmYIfKyY-NerIqPqaCgfX1-jp80nQqjxpvBqd52PlqOMBg7ecOJGTEdFWZl0nuzUmVLrrc-9T3jKIGPlI5ZzQpRfwetppC6avpC9hehA5xCcBY0uxccocmC4k2Gis68ZaoCLR8GiMon10Lkliy5hDEk1Q1JDa0G3p3ger4-KY28gUG_og4ITFMyR063Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه FVC در حال نزدیک شدن به کف خود می باشد.
در این شرایط و با این تناقض، 2 راه داریم:
— صبر برای رسیدن طلا به 4335 برای فروش با تارگت 4230
— خرید در محدوده 4260 الی 4255 با تارگت 4300</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SBoxxx/21163" target="_blank">📅 10:58 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21162">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TgEumDL9i0RM_desuf_-9glHKT3GozkIVhy6JanNyM7Q9ZfFAfp8QXynYBZAYCefnn6F2AjVrlLaU61ZKh2TjRn3Sptm9HgTz6uKRTe27EbbnVoRnQqtIfvGLkDnitKnBbwDYADwCwGD7qNFOQT7n3cVL5I47S44G9SN-JPsgnD6U5PVCpEta_liSeLqVdDHpeQDY4j7hvJzK4otOaZTeHMyhVKZ-iwfV8gnvf9pNlqq04MTVMM0YC6XjP4XT_ex2KRHFANPSkBc6T9c0-5XX_9cwfhrcR3IRZ2CBG-HtK91WFkBNGR9uqXSdWzgENd4S-Aw_Ab_-erqzhrUPjaAAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز هم در سطح بسیار بالایی قرار دارد.</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/21162" target="_blank">📅 10:56 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21161">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">حملات هوایی پاکستان به ۳ استان افغانستان
نیروی هوایی پاکستان بامداد پنجشنبه حملاتی را به استان‌های «خوست» و «پکتیکا» و همچنین «قندهار» به عنوان دومین شهر بزرگ این کشور انجام داد.</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SBoxxx/21161" target="_blank">📅 09:37 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21160">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">مرندی ذوالاکتاف:
اگر کشورهای خلیج فارس جلوی پروازهای ایران را بگیرند، ایران فرودگاه‌هایشان را با موشک باران تعطیل می‌کند</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SBoxxx/21160" target="_blank">📅 01:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21159">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">شلیک موشک به سمت هرمز</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/21159" target="_blank">📅 01:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21158">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/luZADcFarme_byUMCGNEVRFA5NvHeiH4ZNFtTO-YTNQUOOZCM7fL76R-bQpcAuXMbtw5GkHCglANv7z2Jr4DPCEUlEw4MN3WfeB4PjnlPSdMThiZ2RzAbuECuX9gM7bwuQdguj60J4KMXicjLVMHXrNUtY08lXP-k1uS2hffiYdCF3vcSJV8XmrHk3QHEbBYVHSYfWVVgLXb86_e-ATqfBGfVW5-Gl638yYSiDZPra7nRJZj9I3WoJ8h06bZIyDX1oEknlL4x7qetwqGlDtUBlhJOX2iVFmiBZjAlkTt8IYRf083kE0gIDgTBbwsMTNkh2NQC4aCd8LOBgt4se2Yqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تی وی جبلی هم عجب سیرکی است!
خود مردم ایران صداوسیما را نمیبینند بعد اینها برای اسراییلی ها به عبری زیرنویس میزنند!
باز عربی بود یک توجیهی داشت؛ دستکم بدبخت‌ها میفهمیدند کی قرار است توی سرشان موشک بزنیم!</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SBoxxx/21158" target="_blank">📅 23:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21157">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">بیانیه مشترک ترکیه و عراق اعلام می‌کند که ترکیه بر اساس یک زمان‌بندی توافق‌شده، به‌تدریج پایگاه نظامی بعشیقه-زیلکان خود را به عراق تحویل خواهد داد، در ازای آنکه عراق به‌طور کامل اقتدار دولتی را در سنجار برقرار کند و گروه‌های مسلح خارجی ممنوعه را از آنجا خارج سازد.
آن‌ها همچنین توافق کردند که تجارت، سرمایه‌گذاری و پروژه جاده توسعه را تسریع کنند.</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/21157" target="_blank">📅 23:49 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21156">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N3YkRMNlFixeM2nKGomB3gyL7s-AeiXiWkofTxpYBcrdKYzZVvdoAd1Wwa9yRg9hYgl5fI6UYFA58lQU6-rIzq67Iyy7xG6vrIs6AAS1izWrPhecXwDjZuOUFr4--uGnCY_qKPy7I3oDwGpHty_pj8LBWmIPm-L977dZ6EU_ZzZTfmvMoL5FOewKCSDZk5TNc1plVTUeXrrHvuvFtXQddhKm4dSg2r82Lw5X43d8XDVqpRlxphieGVKPNZ0KLB9c9yym6hJ_1Wub9w8JrpNMMwXeWcg-kExTRqMJhzNTEfCPjRgaLwRyPUHg5ePwefkgj9Ow6aywKBua8SxTl2zuHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا چین به عنوان قدرت بزرگ عناصر کمیاب جهان غالب است و چرا این موضوع اهمیت دارد
چین ۸۵ درصد از تولید جهانی عناصر کمیاب تصفیه‌شده را در اختیار دارد و در سال ۲۰۲۵ بیش از ۵ برابر  ایالات متحده استخراج کرده است.
این ارقام تصویری از بازار جهانی عناصر کمیاب پیش از بازدید آتی شی جین‌پینگ از ایالات متحده ارائه می‌دهند.</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SBoxxx/21156" target="_blank">📅 23:36 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21155">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">درگیری مسلحانه‌ میان نیروهای امنیتی و افراد مسلح در محدوده جهادآباد سراوان</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SBoxxx/21155" target="_blank">📅 20:38 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21154">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">صندوق بین‌المللی پول: جنگ در خاورمیانه که از اواخر ماه فوریه آغاز شده، به طور قابل توجهی مسیر رشد جهانی را از طریق اختلالات در حوزه انرژی، کالاها و زنجیره تأمین، تغییر داده است.</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/21154" target="_blank">📅 20:00 · 01 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
