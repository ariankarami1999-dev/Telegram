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
<img src="https://cdn4.telesco.pe/file/EV2MqBw1UVHiVE985kcfIKpVREe4wNLiDznHDuk7drhdh2seC384itudXtYEokGSo4bL9VnDJI9MMZd8o7LpFfh0_Z0nOwUDuuME4b0yaioALblflBX7BsLnXiX6BFhs5HnWjvCX_KRAxsk6KxYzcX05PM8bIORt2RHJkmJsoTyUndNhDZCY3GM9cC97l75lSambeShB9wYfT7jeyH3vhdsYzPMLQC9dQqjkXcH8cQ_e-MCyJNGBWAHy8YqbnsfMiY4IfX8kNCuMuREbRN6dpZuGe8fTutx4YFWxcut_1TyvTEZWVcFJLb_mmKFQGDCWRxS3BjEsqVtVNlrFCCAAtw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 64.9K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-07 14:29:53</div>
<hr>

<div class="tg-post" id="msg-6405">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jJrw3ChXN3NCI9-ptnOcieOxVzrDApaY8cG7XHGcX80bifNNc1oCbcpsNtBAYT8WSZJguD_If1bchEoAANRUiNdgTxjjtR2nu0WusDDWjaMRRyLdKW67MQZWoaZLYlBlpB6nAxGRNCK_7buokA5LxL3ZN4aGItZS6f4CMC8Gocno_cBnr04eyi8fU--e-49hMdCXGQPfPXkiO1cShOcoO7SKLRsNKo0EIqUxdhpUkb7M5l4uVjxB6h6nVlNEJEsPnxH7WhiQnXryCGshjY4sVqJ-CNadxLGowYOQB-Q6o9slsVHWI8PeDX0ALzltigpjvOuytS72-_aAvocI0vuKwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقتدی صدر با صدور بیانیه‌ای به شدت از «سپاه»  و «شبه نظامیان افسارگریخته» انتقاد کرد که از خاک عراق به همسایه‌ها [عربستان] حمله میکنن و موجب میشن بقیه کشورها
- عربستان و آمریکا - به خاک عراق حمله کنن!
این داستان دقیقا همون وضعیتی است که سر لبنان آوردن! از خاک لبنان حمله می‌کنن به اسرائیل، این بار هم برای خونخواهی خامنه‌ای از خاک لبنان به اسرائیل حمله کردن.
ولی اونجا مسئولیت دست آقای «املاکی»  - ترامپ - نبود، اونجا اسرائیل بود و چنان درسی بهشون داد
که خونخواهی و انتقام رو فراموش کردن و «آتش بس» در لبنان شد مهم‌ترین و اولین خواسته جمهوری اسلامی!
سفیرشون رو هم از لبنان اخراج کردن!
در هر جا و هر مدلی، تحقیر بشید
خوشحال میشیم
✌🏼</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/farahmand_alipour/6405" target="_blank">📅 14:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6404">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
صدا و سیما: دقایقی پیش نقطه ای در نوار مرزی پیرانشهر مورد حمله هوایی آمریکا قرار گرفت.</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/farahmand_alipour/6404" target="_blank">📅 14:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6403">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=IwKb054uRCtUHTVCZZ09_lXiAeZyjTX9p8F71v8Qep6O9sqcP5xj1wSvzhkn0Lc3lkoUExRODxehDdqx01HfvnCuJcH3YJtqqQueDpv38K1wntMbCt5x3YDIlrOWgodcHuI8W8Hum2vdOjf7aJ_v6J0j4Ij2WMuQ58luQfPCZSRucYw0tf4viT9NP1lpnU_2z-eGXYS1F9zuId2oLstoCUUMU6x0a7rPW1XgaC5YzIODXVkZjc2VWrQBYwt99k6jXiuyOCeeseLT3XXw8IwdvTswjOBcj2fU6wA3iHVEH5ovUMakRoR1qTw8KVJo0-cIRwXVCsjI45xnTwshMx0f3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=IwKb054uRCtUHTVCZZ09_lXiAeZyjTX9p8F71v8Qep6O9sqcP5xj1wSvzhkn0Lc3lkoUExRODxehDdqx01HfvnCuJcH3YJtqqQueDpv38K1wntMbCt5x3YDIlrOWgodcHuI8W8Hum2vdOjf7aJ_v6J0j4Ij2WMuQ58luQfPCZSRucYw0tf4viT9NP1lpnU_2z-eGXYS1F9zuId2oLstoCUUMU6x0a7rPW1XgaC5YzIODXVkZjc2VWrQBYwt99k6jXiuyOCeeseLT3XXw8IwdvTswjOBcj2fU6wA3iHVEH5ovUMakRoR1qTw8KVJo0-cIRwXVCsjI45xnTwshMx0f3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا و عربستان شب گذشته
به چندین مقر گروه تروریستی حشد الشعبی
در عراق حمله کردند و تاکنون اعلام شده که ۳۲ تن از این نیروهای وابسته به ج‌ا کشته شده‌اند!
حملات به مقرهای حشدالشعبی در ۷ استان عراق صورت گرفت بصره، کربلا، نینوا، کرکوک ،
دیالی و واسط.
در ۷۲ ساعت اخیر حشد الشعبی بیش از ۳۰ حمله پهپادی به عربستان انجام داده بود.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farahmand_alipour/6403" target="_blank">📅 11:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6402">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=edI5JjcBNI8rcSCXsj3snl3tO-j3GuiCFujTxfhw1-C5Tw4H-X9p22CMfNjyZp0dRocizdpJCgZX9KQhVm3egB6ApG9PNERLFqFO_VSke77YTUNebJvHE0vVAdEICnPhEWr7ilHpapIzLfbh51Sqs1ARoyCfErPSezQiBgBBqWwgNb6XZ2PXoBrPZCvvtiUQxz-eITRSlIsUM3qpRk_0P6z11q64oXeA3rRL3Fv0c7FR91nsRuoB8Ivx__WpZsnvhzvxkvX22neS3T6gS6VH1GSRAAkrhA8MltVyn4vJYUx8pRNpeCoalF3xBaHeJXvSozefcc_KFyD2oLOTVXfOzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=edI5JjcBNI8rcSCXsj3snl3tO-j3GuiCFujTxfhw1-C5Tw4H-X9p22CMfNjyZp0dRocizdpJCgZX9KQhVm3egB6ApG9PNERLFqFO_VSke77YTUNebJvHE0vVAdEICnPhEWr7ilHpapIzLfbh51Sqs1ARoyCfErPSezQiBgBBqWwgNb6XZ2PXoBrPZCvvtiUQxz-eITRSlIsUM3qpRk_0P6z11q64oXeA3rRL3Fv0c7FR91nsRuoB8Ivx__WpZsnvhzvxkvX22neS3T6gS6VH1GSRAAkrhA8MltVyn4vJYUx8pRNpeCoalF3xBaHeJXvSozefcc_KFyD2oLOTVXfOzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب چرا همون موقع نیومدید از تفاهم نامه دفاع کنید؟  این تجمعات شبانه دست کیه که هم دولت و وزیرخارجه ازش  ناراحته و گلایه داره و هم سپاه!!   کی بهشون یاد میداد که بگن «بزن» «بزن»؟  کی موشک میزد به ۳ تا کشتی در روز و توی خبرگزاری خودش (فارس و تسنیم)  می‌نوشت…</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farahmand_alipour/6402" target="_blank">📅 11:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6401">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k5tsr5IzXk3jiI-qoQqo3P4SPx_vRWaDQm_DX-IZfkX5TpIJcq8vuS_cQGuQL-bVkDvfZLrzgjd8M-R5s4enJLlTPsEv0qV5grl8GN6RwVLmZ9S2FN4ykDfltQNVHHEiCFPffBUBCfoMw-qKWnFBbn1E7ED6Q1udNAsIEuZBPYULgL3uJFPIsGIRFvg1zriXsbe7H20I2Wa8In9LQ3v9XooNPQ-ABtY3cWuJF08k_RuwpiwqJd2m228GkOk2Bb8e72uKLbtiqXl4mUWWiYq88vbcUvWO0Cq--lSw4LOtN-Eey9vMbGu8Hu13jlQg_oi4BHCpvmUx9mIz6nKoXKk_xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب چرا همون موقع نیومدید از تفاهم نامه دفاع کنید؟
این تجمعات شبانه دست کیه
که هم دولت و وزیرخارجه ازش
ناراحته و گلایه داره و هم سپاه!!
کی بهشون یاد میداد که بگن «بزن» «بزن»؟
کی موشک میزد به ۳ تا کشتی در روز
و توی خبرگزاری خودش (فارس و تسنیم)
می‌نوشت : «به تیر غیب» گرفتار شدن؟؟
مگه معاون سیاسی سپاه در یکی از همین تجمعات سخنرانی نکرد و نگفت
: حملات آمریکا به ما «واکنشی» است! یعنی ما اول میزنیم و آمریکا پاسخ میده.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farahmand_alipour/6401" target="_blank">📅 11:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6400">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
سپاه ساعاتی پیش از هدف قرار دادن سه کشتی که قصد عبور از تنگه هرمز را داشتند خبر داد.
همزمان با سفر نتانیاهو به آمریکا
هر روز دارند به کشتی‌ها حمله می‌کنن ولی به اوکراین میگن حمله به کشتی‌ها خلاف موازین بین‌الملل و  حقوق دریاها و آزادی کشتیرانی و … است!</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/6400" target="_blank">📅 09:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6399">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g2jvxndXuOlDQ90AS4zSGOMX9a898jsjr8sv3dRWPhb-jHNTbppzu0wHR2u3nPPCIa2kQ13MAftcNDA5C15hlyvmWitzWY-eu5RHfFcUgM_-OrcUBVGu6QTlicHiP_ZXgZJMYGhUO4IdyB-X7PjZf2faOOJ1FEd4fJObt5xlo9hhALXC2yyvhJfUD0ik4VSFoGM8J2UDoggZ4X4qVj_UlnIDP40Y94GFlWbt62bme7hvhZEq2JH_LbPiEt2y3krTRG5u7epc2cfL3tmq3QG-7bxrQhJo7ubGcsZJqj7U2_MeDTL9sHbZXsumbwdRCtc53QSWFFSSzrXOpRVrO3-ULA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها دائم میگن اگه جنگ زمینی بشه دیگه قطعا ما پیروزیم!  این تصویری از عراقه و نیروی قدرتمند زمینی ارتش عراق!  نیروی زمینی که پشتیبانی هوایی نداشته باشه وضعش این میشه!  فکر میکنن سرباز آمریکایی قراره مستقیما  بیاد با سربازان ایرانی بجنگه. بالای سر اون سرباز…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/6399" target="_blank">📅 08:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6398">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9aPxx-ivjmeebdwMhUPzMmBWJpkYla_Xuv6QeLWSjWSFrJE7Fwmjw9I5b1cjQ6sjBTkwoFBS5FtEj6_pHYjXXpBxX95jsrcHb1EWMdeTRcEQTkv7X9t7n0eYDRxyV1ngsecIv1Dnf9RSFCG8wU9lG4BXqRLFAJ2PEoBxp5b_sU53LzjLuR6JdV_5673tscO_RQJgqGMd-VktOu8ZCvziRkGq9tDjcsXMr6u7CdIcoenWluSpdFHKQaG--jG4mCcaRrg86CuTCz2N0XfXniMAL96cKLLPt71EgktRMnFBo3zt2VrDMhap-XfekVCdHTPvNEppxJyg0hI-rMmGSjTlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱- جنگ زمینی چیز بدی نیست! ۲- اینکه جزایر رو بگیرن،  اتفاقی نمی‌افته! جزایر خودمون  رو میزنیم و بعد پس میگیریم!   اینها قبلش میگفتن آمریکا جرات حمله به ج‌ا رو نداره! امروز میگن، حالا جزایر رو بگیره هم مهم نیست! قدم به قدم!</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/6398" target="_blank">📅 08:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6397">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">۱- جنگ زمینی چیز بدی نیست!
۲- اینکه جزایر رو بگیرن،
اتفاقی نمی‌افته! جزایر خودمون
رو میزنیم و بعد پس میگیریم!
اینها قبلش میگفتن آمریکا جرات حمله به ج‌ا رو نداره! امروز میگن، حالا جزایر رو بگیره هم مهم نیست! قدم به قدم!</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/6397" target="_blank">📅 08:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6396">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TtxaaGa2NHgdANT6h6NVASJI_uCrr1X6OkpWbWA_CK2TIviPIeIQi9MYYFHKuUsTXjpvk_aw3gIi3rLa0ff6Y0NNlI3wHEBrzWoHd3UsB56U2f2lp3fCxKlG4YqQCDPar43PzAd97dUIEZo68MhH8gdcYmSbef6POekZynlaY_8dhhEP_sIAPFMahunBSlhAKjFzFg4SDajTLxbimArdzwLWd5mmG3oJCoGoUd8MAgnMXjch9bVJiJH7xW_i80VfxW_1C9qg-i3j1JMo4aGqclXhmzcwLz8dGYsAnUuY8-UD_JGqKcdIBMIbgkLT2IvK2K8l3JfYr7Vmm9ped5j-HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۱۵۰ میلیون دلار
هم براش هزینه کردن</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6396" target="_blank">📅 21:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6392">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YDyfFjTye7nEyMKk_CTVYaigurmUBdJjjq25DtfPE9NSbgCmj3Mctf2Cx-ExX1liX1ZKNZvEDaRerfTiaLg3o9htunliWUtKSM0-FLKk4q2BsaQfPA_ZrYz4Gr5T2fZDqXf61zJumnnWWv_dIPxdQCpD4GSD-kok-n2Ad1vnBexqc7mB5DLlM45MdpTDeCLqWF5aYx_7E-mSpY6SG12qy4oc7xj1fkZyHB8IKWm7xpu1nBBbKBObX2zWcYHU9B1S3zLqwPXzbIvvAfd2FtuPmNyHLFsSmfDnqv9GJfcrYmOU89E6arkeWWbkowcCrMIwlAaZnBe32z1SJEgK8PIJHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tq4FFCiSrLHABNGk-4kB30QMBZ-uszNP8idHLG2880AavKf_iydTe9v5LrH-7aMXbtUsTinNvvT-IHgIhyHOpyxsbgVcwhI9RyF6VU0DBDMqzjBzTc7OXXJYNWme_-mXideRLGGdBusb9wjnbOaLJ0NEtUjDNBLQux55aps9rr7ca4UbGUMyyzKRasT_nBpRh1plOy7Q6ZbomlpzlPy8r1GKVc-JXS6zL985Q1mOQgUgK_loHpcP86zA_VFn2DrWpgFbtqR2Q-Csc1kElIFi9z7NKWsARexoOOpqe0RpUlRNkBwUZ4qYwN7QsSQ5KCgfXP2ap70spGmpr8g5PLqO3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PTQhEZCUZ4qWZcT0th3x3TDgLdupWpnF63h9KEvI-llq1J0B2FLubTq7cHBD65DjpuWHZsTE3WadJg86WRU_R6Eny64I8tuMPJnpKewW5MEXp7Rm4241HiSjci8_k19RMY4vJqD_GIqYr3630gEn2dQtV0TKv75nULaPuHHSOrf5eU5-tVP-7QwQ7jaAsA0NjUplR6gULfuqLkT-YdfS50N0kPq6E3F9Zxy1i1mWeuEDspN_uJAwijN7xM5BF5-RokNzKzntgK7PwLDN2mjTC4dEDJ4zr8T0eDbYgoGgitoT5Lc0ELGJ9IE7OngdfSPKBVAUfn7oZ_kgWnUrge5sVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JwipT02uG6P8hl5vwe9yOk0IBbKqvGpT7zRYYGaHm6V2pYh1SJ7DoFG4X_sn2b_zFinp3KCWjWtQI3OfbDEd3zrJWj7JwpxQMvrIUGa5xQemRKYKJgq4VuBEyMM7WEkWpLDXnhXGAgP0pgHV4cpXqZvkX0DWFWkhiW0aHcB9MIAH1528tsvWh6MQUtvXhpQTYDiNK401IyeCr4grpQEL-25FB82ay-N6djXNfuS4Ny6bZirRRGpyPF3jJ7ri-Jw4gv0zH-V8Z96T_v9IkSuHOagbOeGjBRvtUmuTnl5qB4e0tCeyauqoUEtyKSK6O7BTtxenoj18bWrPe8zJyzd-gQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویری از ویرانی فرودگاه بوشهر
از این هواپیمای مسافربری تنها دم آن باقی مانده.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6392" target="_blank">📅 19:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6390">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">میگه ۷۰ سال پیش ما در خفت بودیم
که وقتی اسرائیل به مصر حمله کرد
حق دعا برای مصر هم نداشتم!
اما امروز باید خدا رو شکر کنیم
که از اون وضعیت به جایی رسیدیم
که آمریکا و اسرائیل مستقیم به ایران حمله کردن!
اینها از اینکه به مرکز فتنه و جنگ تبدیل شدن
احساس غرور و افتخار میکنن!
امروز با مصر قطع رابطه هستند
اسرائیل و مصر دوست هستند،
اسرائیل و آمریکا روی سر ایران بمب میریزن.
زمان شاه که در خفت بودیم هم مصر با ما دوست بود هم آمریکا، هم اسرائیل! معجزه آخوندها !</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6390" target="_blank">📅 15:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6389">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">مراسم خاکسپاری مهدی توکلی، مدیر خانه عکاسان کُردستان، خواهرش سمیه توکلی، روان‌شناس، و مادرشان مریم اصلانی برگزار شد. این سه نفر شامگاه چهارم مرداد در پی تیراندازی نیروهای سپاه پاسداران به خودروی حامل آن‌ها در جاده بانه–مریوان جان باختند. نیروهای سپاه پاسداران…</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6389" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6388">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIranwire</strong></div>
<div class="tg-text">مراسم خاکسپاری مهدی توکلی، مدیر خانه عکاسان کُردستان، خواهرش سمیه توکلی، روان‌شناس، و مادرشان مریم اصلانی برگزار شد. این سه نفر شامگاه چهارم مرداد در پی تیراندازی نیروهای سپاه پاسداران به خودروی حامل آن‌ها در جاده بانه–مریوان جان باختند.
نیروهای سپاه پاسداران بدون اخطار یا دستور ایست به سوی خودروی این خانواده شلیک کردند.همچنین پس از این واقعه، از خانواده قربانیان خواسته شده علت جان‌باختن آن‌ها «تصادف» اعلام شود، اما خانواده تاکنون از پذیرش این درخواست خودداری کرده‌اند.
@Farsi_Iranwire</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6388" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6387">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cMODDd1cMvrMyM_Pe21cIuFswf_eBb4wqYMsEReKs9Ui-zaKSrEg77gLXnc9Rvkzvog4QJVKlaDE-4ARIFaKZUSk8fpV5PiV0Z49cibKNp9OCFgovyBe8gLT7THx1jc6cdMtLObzCQrPV44Cd0K-mBBu3GvnkW1FWQHIajEaiHeb3EIoGeGyMpiSCjPdniHGE0ft4jZuIuH4zZgpXVcYkDa6ApJoKavfELLRJUZ7dcpxREm5VtqyCjSa9TtjNaiT7sHwuBZMFqu3SQnFTw07agKzUFm-eSMx3Wik47a_5NYGQtnycqB9ymyMleJh6D4n25ZeomhgYBjDRQN4bEPILg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باید آن قدر آن‌ها را زد تا پدرشان را درآورد.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6387" target="_blank">📅 11:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6386">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">‏روایت اردشیر زاهدی از درگذشت محمدرضا شاه</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6386" target="_blank">📅 10:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6385">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LAvAYgamA9BFS3pY48LtvLsHEabPREd6axNebhy3q65VSv7_0ngkU3HAbiAH2PvITBr8PlUuIBL0JBS5syQQu_DbmMn3nzU3GGYCa_w_tiaER6UEJeY0LH-V1S64IkoGvFiDc0y-tEZDxsTDD0NsG9vUC1AEkzxVGw1rlvpPw9txMKuw5yr97i47Vs_qOEIUQYHHGt_jBqfaz5IzS853o2HXTVb77AZ5wnmFXkppxHSGTNrE80qm9sG5Dwd4IvhJMga8yGZEWH-e8HSYyqusQzRVO29rm09v8mWLPS4HhHRXUT55MTJpai79kSNt6BrlQALcHYRtz1DcsHenEz5TOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لعنت به ترامپ که ۶ ماه بیشتر بهش فرصت داد! تا یکی از اقداماتش،
و حاصل دو روز بیشتر عمرش، قتل عام دیماه باشه.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6385" target="_blank">📅 10:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6383">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/139cdb38ba.mp4?token=sJlReZHoGbPYDHalIcyssPwwsNoHZn9WnQ6z1S8rzgDNkmzpa7108QZTgANwno2Uj7rKIOYT335gfqdJjWQwfWgsJV_bZyk_gG9tdO9xaQ9OAdM5Iht04d4BLl7YiA-tv8phj77Ccg_RP4qASIodi1P0RaDmTzfY5Lx3WfCl_5qYTABr-LJ0qtG4lSOLTEVz_utykvZVzMm-UmZgc3OZkr-jjfbKz1gMLoje04HDDqlk3nAflNsEuU5UKfwY5kSasRD22yypYvfuUB-5JDwoPOrdoXXok6e95R4WB9MIx8BJJA9Y_3yaJAkg6SPnXnkTrfiQLy3nsriM0Gfnh52E2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/139cdb38ba.mp4?token=sJlReZHoGbPYDHalIcyssPwwsNoHZn9WnQ6z1S8rzgDNkmzpa7108QZTgANwno2Uj7rKIOYT335gfqdJjWQwfWgsJV_bZyk_gG9tdO9xaQ9OAdM5Iht04d4BLl7YiA-tv8phj77Ccg_RP4qASIodi1P0RaDmTzfY5Lx3WfCl_5qYTABr-LJ0qtG4lSOLTEVz_utykvZVzMm-UmZgc3OZkr-jjfbKz1gMLoje04HDDqlk3nAflNsEuU5UKfwY5kSasRD22yypYvfuUB-5JDwoPOrdoXXok6e95R4WB9MIx8BJJA9Y_3yaJAkg6SPnXnkTrfiQLy3nsriM0Gfnh52E2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همزمان با اذان صبح،
دو جوان رو در اصفهان و در ملا عام
اعدام کردند!
ابوالفضل سپاهی و امیرحسین صفری.
مردمی که تجمع کرده بودند به
حکومت جنایتکار جمهوری اسلامی
اعتراض کردند و درگیری‌هایی میان مردم
و نیروهای سرکوبگر رخ داد.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6383" target="_blank">📅 08:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6382">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=uT_fzI_OL8mU31h-Z8kmc_L5sQaxpnTc96XvZRzc5T0d5gGi9zpXdN2iMSsuCZlBkh0RLIUl5cRgbJneFXy4rbX0fs91jE6Kd4OTbKpwSVMG_9A3clOVlWhRbtXpnljz_3ER7NzIgqe_iaBXyAZax0tHd9fh1vj1CueIY6CWTig0w69hlPCGHSo3A35NGpGa5J0COVLGiHhctgUcoh0bEcioM71yj0H0tbp8PuVArFtszCUBsbQyj80cdj0uoAqRGvUXCAB7UyuqyJmDEWqFRgLuWqWHH-Oo9mEJLcOzMh2YBuUbruhHOEAqO9YwHB7RD-R4tSJCcbKOTy9yL0DLJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=uT_fzI_OL8mU31h-Z8kmc_L5sQaxpnTc96XvZRzc5T0d5gGi9zpXdN2iMSsuCZlBkh0RLIUl5cRgbJneFXy4rbX0fs91jE6Kd4OTbKpwSVMG_9A3clOVlWhRbtXpnljz_3ER7NzIgqe_iaBXyAZax0tHd9fh1vj1CueIY6CWTig0w69hlPCGHSo3A35NGpGa5J0COVLGiHhctgUcoh0bEcioM71yj0H0tbp8PuVArFtszCUBsbQyj80cdj0uoAqRGvUXCAB7UyuqyJmDEWqFRgLuWqWHH-Oo9mEJLcOzMh2YBuUbruhHOEAqO9YwHB7RD-R4tSJCcbKOTy9yL0DLJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرزوهای خامنه‌ای : جوان‌های ما تا ۲۰ سال دیگه همه باید عربی بدانند.
https://x.com/farahmandalipur/status/2081803094522757301?s=46</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6382" target="_blank">📅 21:35 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6381">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">جاویدنام مجید پوررستمی - قرچک
۱۸ دیماه ۱۴۰۴
قلب آدم هزار پاره میشه</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6381" target="_blank">📅 21:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6380">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ترامپ به شبکه ۱۲ اسرائیل: «در حال انجام مذاکرات عمیق با ایران هستیم. اگر موفق نشوند، به اقدام نظامی قدرتمند بازخواهیم گشت.»</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6380" target="_blank">📅 18:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6379">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ed1a3118c.mp4?token=NG3omz-9IHIm51gFggZFGH8SGtsQizKH8Aej6LWUh5ucCuDh0VUOztod41WkgJr1OK0ciiWBp9itUmRDx2hGtWseLdVGs9JSlHvSNGFhNcYA2kqGed0gLsFo0_UezIIUuyP9uC68f-YJBL5ets0TsBI_B6k3MNh2o-XnhD08Lz74ynBsm_I1RrdVGFLPXgS1p3Mr_3EPqlPLa8d5jiaVG-GPSVGTW_LoWQfKtH5bQP4U26vuPubXAjK_R0G9Y3XB4dQmFqsMv6ZpnvIVAt_CYCN-HUBCHU2byzyuwZ4vMEqYQ00h91ytiIwgG7x-eksL1YyMhIcdK826wo1mTmkNEi7hoj8uldNaA7J3LQWTkasBOXvaMQD0meFjLXoRKqYMzyKvCsSLyNKUhFDHaxzxso_8qrt3s7s3q18uzaI2q3A3xPAAgJAFpZ5hYkAgpDEDo49rcY8aeABXPlEvHT6XmzjKeXwVWy5SQCRdcJmS-FzCqenxFcbY6KGAg3L7JtL5TyvdO1wSHVEymFoqa8zZBjC1T5_7J_s11TrwLSUx51IpjW9QWzO8x_VRNFJYi4AX-FfgNTQP3GiXakvwzBhWykFkoZtYJkvIIfj8-CA1tFzWSa5lLvCuhEnSJZ-AtTZT0NCUnUhvEb4bJrzdg6mGRCD4B-Hi8AndeS87fjZnDvk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ed1a3118c.mp4?token=NG3omz-9IHIm51gFggZFGH8SGtsQizKH8Aej6LWUh5ucCuDh0VUOztod41WkgJr1OK0ciiWBp9itUmRDx2hGtWseLdVGs9JSlHvSNGFhNcYA2kqGed0gLsFo0_UezIIUuyP9uC68f-YJBL5ets0TsBI_B6k3MNh2o-XnhD08Lz74ynBsm_I1RrdVGFLPXgS1p3Mr_3EPqlPLa8d5jiaVG-GPSVGTW_LoWQfKtH5bQP4U26vuPubXAjK_R0G9Y3XB4dQmFqsMv6ZpnvIVAt_CYCN-HUBCHU2byzyuwZ4vMEqYQ00h91ytiIwgG7x-eksL1YyMhIcdK826wo1mTmkNEi7hoj8uldNaA7J3LQWTkasBOXvaMQD0meFjLXoRKqYMzyKvCsSLyNKUhFDHaxzxso_8qrt3s7s3q18uzaI2q3A3xPAAgJAFpZ5hYkAgpDEDo49rcY8aeABXPlEvHT6XmzjKeXwVWy5SQCRdcJmS-FzCqenxFcbY6KGAg3L7JtL5TyvdO1wSHVEymFoqa8zZBjC1T5_7J_s11TrwLSUx51IpjW9QWzO8x_VRNFJYi4AX-FfgNTQP3GiXakvwzBhWykFkoZtYJkvIIfj8-CA1tFzWSa5lLvCuhEnSJZ-AtTZT0NCUnUhvEb4bJrzdg6mGRCD4B-Hi8AndeS87fjZnDvk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به این سخنان «موسی خیابانی»
فرد شماره ۲ سازمان مجاهدین خلق
و جملات و کلماتش دقت کنید،
اول دیماه ۱۳۵۸ دانشگاه تهران.
انگار همین امروزه
و جملات یکی از سران جمهوری اسلامی!
که داره میگه
«اگر ما اهل چانه زدن و گذشت از اصول بودیم، امروز خیلی عزیزتر و گرامی‌تر بودیم.
اکنون هم که وارد این میدان شده‌ایم
باز حاضر به عدول از اصول خود نخواهیم بود.»
یکی هم اون وسط فریاد میزنه : یا حسین!</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6379" target="_blank">📅 11:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6378">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DEKdsbRGHs8EoxCjjzDFet8-iMKHPBDLDyW6EygzZxamj9IaYXbVcG_tfWURCGbw3pOdlc4PPIG0DAyTQGmWatkrBr0mtl4wJlS7UmPw5Wrr18D7HmvlicQLS67s_KGcia52COyhr17JPvKunwQOknBqT53VCFevRgFUv4ERc3yJG-4EvM6TsDbhQKh-ewh6qAH8zLvD-dCRp8bFji82Im8ruiZdzcjm7NTdD0-2N_JHkQWmFqjsAiZi-Rwp0HgLZ9pExwxgMyhOTeVh2BHw2k6-lfo8Y6vXZPa3dE-Bz1PDZ3JSP7yxCal3HhazU-nJDJuUf_BXNcVZPeIEKD6Mwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو راهی آمریکا شد</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6378" target="_blank">📅 10:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6377">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=CeogoeJac960VZHludK8QDlCqXsCUistD8GBOJUhAgdLo6jKYJnnn9z-MpXLVp9-luP5Ah271tZLAlEOPe6GJQB9Av3lwJWMYuS5LeFDvUUCF18KtJYYWur_9I3SMf1ASjdLQJkNCf5tH4H6GFgmNtD-OZ5LOABEoli-S-THGs8lcbNh7crCx7lAXTcQ0lDTP8qX8L0hDF3EXqRPvxabCnPNeHfX0nsz57rFTsQ5iQVIXCRoWHG4Xzeu8isEQfuhztPw9486eYaIbu8VeUAANUqTuRdAI03XrRqms4vyix9htiZi9Z7L_B1_oSdejqhQeSLJZPvRRK8ARZw_X82tAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=CeogoeJac960VZHludK8QDlCqXsCUistD8GBOJUhAgdLo6jKYJnnn9z-MpXLVp9-luP5Ah271tZLAlEOPe6GJQB9Av3lwJWMYuS5LeFDvUUCF18KtJYYWur_9I3SMf1ASjdLQJkNCf5tH4H6GFgmNtD-OZ5LOABEoli-S-THGs8lcbNh7crCx7lAXTcQ0lDTP8qX8L0hDF3EXqRPvxabCnPNeHfX0nsz57rFTsQ5iQVIXCRoWHG4Xzeu8isEQfuhztPw9486eYaIbu8VeUAANUqTuRdAI03XrRqms4vyix9htiZi9Z7L_B1_oSdejqhQeSLJZPvRRK8ARZw_X82tAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله یک پهپاد سپاه به یک کشتی در تنگه هرمز</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6377" target="_blank">📅 09:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6376">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/euz8p7YGA_PT_ROLeu9kx4RJoL048dX5uM6M5__IPQdCNxBFFjEHInGwSQWzfzIhVx1ypctFfJfpQIYdWFNIsJCSLm7XaL_sq3gneZNannrXU85SRyRKrLXbgXskTROCMhvVrB6zMO6ro8oFS_c6FhdjwFGs8F-r3Vhy_NmaqqqTazVqb14UZPuwL2VsKBgE0sDPsnLNAYejmDzbVJiMAQqChfhJWbssLD3U9GjQjgm8a0Tt__FAUec3tremVXVZ-tPFGFQZvSBqSPPC6BtnFuA8aCfkL-1QFTvxOhNpb84XXmVm8ZCXXg0OqJ43-8wFdjFc5SFGqjTXPJ8vjISC-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«مسیر ناامن»
منظورشون آب‌های ساحلی عمانه
چون از مسیر ناامن میرن، با موشک بهشون میزنن :)</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6376" target="_blank">📅 08:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6375">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">۷۰ سال داستان دلار و تومان</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6375" target="_blank">📅 08:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6374">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jBJI--odd44c-aj-cw5piD63x2ELrrkCkGF5jYtC4jVNyKiuAxeiTUWc0LyMA2k2fi_DYyuirs7nBa1PoTKS4nThuH-kuIcUxa57K1rpFig2-TSJ5HddYr2nnzMMhKngkD9xxuNkaxk6taLKTDIoiDrs3-XFmFOMI0LsYYD2GqeRAd_JGii_EjpG1QbOMFAQI-36oHXPEpog82iF5Ul3CyxpwCp6E_dSgL5o4tdyZ6SOReKWeG-cr5VyWTgifoVB-ZM1FIpwOsbVQJ9fSCktmrEthEffPK_-OnaS1-ZLiXuD9txm_WXHultxbOiefLZt1E23I-4UPLeHrhc2B2e-Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشسته هی طرح میزنه و منتشر میکنه :)</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6374" target="_blank">📅 00:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6371">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rmmuCGIc1cqdKZUS3JoVeXDecbWG5aiQEUMzDv-LqJLwh9i4YjlyWgXr9UoUhldBfNQPb40p-9cUwucQMpfjZB1Go5KdxpdZf0L6orgypwHDfB0ORzph52tIO3Po1I4PMDx4SMFbJ26tVqQGqLvbDY3PcXxx-Vr1XblMiWJysbdwXtlwsLBUBIlNHyQ6erVNYytFi9qL1r-fT4z98uu3hLqUKqyy5gBasQIjqlANU44fnkjrI3-jbURswA4Wr1_ho_VlhigKsRUcq67MrrnbTzYUlypq2zpEgTVuouP9Wvxx7nlEef16-97-BVd2sCf8k2eFh_SZFBLnQ9dbNaGUsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fwaqwxFh2stDslQ0L5AklZPrY-ZbYq-WNk_kJsbCzGxcILHXQClGhcRMKs0sn39_OdeWf8_6lQxYGGaSA_wW-WiTyEUUiRqg8xVAJbmwDdbK4EArYQDPkvnGX6p-SM1CmAVuztkmMadvCBOMvvOPpI7b_oew8hrRw9XnD1BVLxJ-HCpuRA6uVQbnT62u68CGTTUmxw3wqrvfv7zhIOmCrNXhWStTc6GgymWg_ot160e9ZH3h2FPJBMLNZ_A67qhR_Jp8fXQhKUPuA1xnmmmmb86BUI2S7yRHTbGISo1A42LK2KY-C0oEKsjLw-8e556jk8qnGB9uzBSNN2JM0qj8ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rnS6HRgyzL7Em2dfw9bONqwH6tuFFTcB8OfvpQthHVX3l9cyQTwgsmYUx-zVU7QCZSO3_i7Q6ykLN9WnnKao-f9oDRox_bzflqvRIGDWgj0XeI28HDk_IXlVttS1xW2QFubUS_yO4mmkHHboIq40eTaZ7622b5AfwHUp5nRBb2-LJzRqqvjDIMK_eFsl8twcBwzKQ8I4k2oZTOekAiqG4nDSddSlfnr4OxwUKCjY79PMFXx0XwZgQj6Ube9ff-WOnbtlP6aWRRE-ViaCDwOWGO10yP_Y22BS4sO4-lNlJRgyF7M-nUXAD6_FNupSu_e4E9Yxaax5wlaiGyCphjD4ow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طرح‌هایی که ترامپ با هوش مصنوعی درست کرده :)
حمله به خارک و تصرف نفتکش و… رو :)</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6371" target="_blank">📅 23:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6370">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rAsHd2Tx9uQWiVSn6BSsWWb09CuptmtHwqQ0NbX150FGqTYBuz06LarU7-1qI0Psdmlo7HE4VWPmb9oyH6ibFA38DNJOBVHdfPQ1kYNC1rxGt1ZioYJJEcBji2C9b_Q2lXKln7Mam0Ddr0RKIs2d5oPHvFj63KqzXyQVwjq1SJHvCeWODiCh5T9CgAwkMyCsL-p0N3b6_m10QAbk5lVnznvbY0MuIcUyXhVniIxlE8No54QvS5WnKd8DkBHHKWAZfaIMRy0YVTfgqGegd62K4j0iEXQw-AHEwTICGZ3MdI8P7xuFZo9dDgM8CRoAUwGl0nQObYEx05acAMVu-YqdqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه منتسب به مجتبی خامنه‌ای :
در برابر آمریکا و اسرائیل راهی
جز مقاومت نمانده.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6370" target="_blank">📅 21:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6366">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zrd5-2IsUtfLBdFvyB_C5nyRq8u0umFHLd__AUpSQYGcM_F6EdtF4Q5Gp27uaCfCCH7XGoxyEQ3SwPmhHsBXpqB3Z5ptWLkgPvE35HsmWZbDeRxonRsdOcOWJOv9MFv-9qEA1ghn5wcjL0kyhPygkqDvl2HW8DxpoQ8BY7ru5JAhJ2tzVn3tGsnc-cZMWg67AyzcDT83VYBF8zvwpxaZHtxYYndJMTqOtyyvUTdaoOKhd7GOIJMHUjN_gdmzYXKgg5UZRq2i5yhsTZifKwHRE_q3HljGX4khoOjq5n7VrtbTfQ977YdJqlVWgV6xzV9_pE2Oon3ZEtBkKCeZBkUo2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JdnX22hdboAds3ON2KnW9EYa4jwKsaiCv1Gql3tgD-UMHwC8AfheMG5JPoFDRmFoQwV8LIWKhlryNWGGR7D3Ia4YuW0MZ8st5H00b6Fwol7vu_mo-8uS025UVSzTrP9LIO5PlDipyf_gdL-lbuOX7oPf_bmOptsN82QoiXol5oV69OrTjPhcOO1K-nXRaeNxa9vnLMuaUpLUf1icbQFInHDDZ4RBy2mj8vZTNyUx3LO-_YMJTPJ1_v4aer_XrGa3U_JduyGYGfmGtnugCI8frPSCjZyCOlhrt11llq6NkQiQAUmxz06OM_XwZZFC6HEQlbWW-5Awrugp55q8GJ2iGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BV9ktNJLccCOZk9ZnLRxtUMCjwq6__yPWoTmBInFQQjv_2eVpjl1Pe3oTLuT4IpSRFTi-1VbpiK71m3BuCsTfMhXh2UrMNv7fcQYAImeiWUWRVG74_GFkjucI6Y23HH-7MjtwPhXAndkAmIY7qPYiNWDaxw40e7VMpCvCySurPkmFmm_90lFNSo23e8NodoHgGIKtynEpoqn3FmEtBNbakzbHtolqdrOaeN8LEyB9Iox26F8aArWkj0Sc8WQTzClxNTHE8lKbAwamKrR-NF_KcRGMnKXbxKtHINJ7vKB0MqIDCdipbs0Dg46D6nZcSc0Qew82DkZNofLc452S1XQUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TFO4RSaBoiUeiytZT5pvloybJlgppAMgVNpibNLjpVnyA8ucTmMtPC7aDgEvh12eOhhihK_txVeJkv3xZ2cffSw73dJRZOroLasQCQD-qSXdlQvuzXNOMe_wTaAMudT2SrGRpmScgguW9kaQwi4MZc6f8r7401DqwPf-6F5QvU3qAlwMAl9dwucLP1izonf8YQWTNMW-mIiGFKiZgaw2cR3nKpvtthFFEtDxl41CM21_pMoRUMeWd78u1EqV6_m3Nj4G4y2ST0YvY_YHGnuBiCNZPQrtiR-jNdhlg52ZWHcFib9RMmgNCDi06IdrJh4_MTUdkuCow4plNSugh3ZtUA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جنگ اوکراین
تا دیروز افتخار میکردن
امروز نوبت انکاره</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6366" target="_blank">📅 20:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6365">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">۱۱ سال پیش
خامنه‌ای با غرور و تکبر از مسلح کردن غزه میگه و اینکه باید کرانه باختری رو هم مسلح کرد.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6365" target="_blank">📅 20:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6364">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dGK5ozbNqkyj73amXn9fPRZ-VXx03mfMDYssQQPhF8BuVbHFmXaQMWeH5bjPFvd0T8-arCnGFXyochbjaORLDjT5X03W1DsSEtrG1i24QZwyzXW4UemWBtMoHaUxqzzQOM_RSkEF5dDa5_nC55XsgxloovfOFn4CKiF6W_lKqVKJHCo_ct-C-se6th2plqKXNfkEWq_Z8Co2d9anmLrXQGUW_Ld7Yo5E83Ds6wXviCOHtxON0bg2v5fJw6TaxAqf3whLBvPhtbCNJLQSpi2BHD0kkAZxJnPUy74ENB6l3Vagw4YIoAKQA19w9CJRQplZ6Mr00RUvHKYZWVMPJC8a3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6364" target="_blank">📅 17:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6363">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/urS4_A6o9oHAhPsJTQUJps86Tvr4OWZU62P2xCAwrXD_tQ1NR_5muWYQPC1sTnaD56N_skRtcusMOuaxD_T7EZeCCJlcNnUtaXmpO2dvMPE__MrxNdlUrSS2jZlYWd-rv_YoQY6JagrPw8X0129SczPFjqAAfDup-befOy8bkcDX7sDa_gLiXj-7mWTwTtNwEjxPamHD-hQ4b8yg_nFme4h7QlOqWfjGmLh12HBp_N6vDVCwm95YDJa3MmkMjkvO046HehZTmG-DorkIDVXclToj8cqOFTUkzScJNrqfJh4rAAeNeDo9kFhoxPrV9q06BlvYdOOMHCp9Tc3K4JR6_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های حکومتی از برخورد یک کشتی با مین در تنگه هرمز و وقوع انفجار خبر دادند.
مین گذاری توسط ج‌ا انجام شده بود.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6363" target="_blank">📅 16:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6361">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YlwFk2sF0rl7vDyxEzAG_KGXMHFF8rl40o4IupFW_aAdAuqiZK4WwUAvVlRpoaP3x2uKCaVcWxEXhW_86A-oAOdTPpW7rzaG2stvU6K58QYXWpn1kUaq2WkXeDALXDletV2H1qng6XN_Qc87S77vYQGOkCIaUmzZJeLh9Vc3ZPmBYe63cnfdYb-nzaQQfOj6nR9RTknTWMgb6-iUQ83T3dD0cKvkbnzZfEuc_MQ-dYhuNSxeJoKlF9_0Vd_qHoM_6Cd6agDxpb1FTFKkD0eF-YYyN_6QHChOc_gGzxpNu4z6F9WN_PWepSCqoHIwqjt2ZduO8DBpH5JKi7hC_gkAUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n1D6ek3jnpbjq4ENa2VW1-aKb0mMxDhFOGdDPzUkjeayGWxyk2apnwcc3rDbh8wFlTWyX4rkmcweAhkB2xDR6vAm7hBDM_j9KXVkdWYI6GL0v6rBkYVkRSG7WwnGEenAB2PUFB2vrVujHVxLjgJ4m5yG1boWaL2wsKmnQEmk0YsyWxsqaSnuNl0fX0jM6WNIgVW1nYSOrC5J5JZS_v5mKwUwYKmemZzuqi7-4d0-UFaIa7mzXttm-ePm7SqFbQjZLYnue1UtsnWTFqCKtmEXl-zosiXVPI5t9V8Q87kURCShcG5AlVEINvxpDy7QoB9E0m6PMSbcm0MuYDhPTwSxFQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اینکه بارها نوشتم، چپ‌ها، با اینکه گروه گروه توسط ج‌ا «اعدام» شدند، آواره شدند،  نابود شدند و ماهیت سرکوبگر جمهوری اسلامی را به خوبی می‌شناسن،
اما نوبت به تقابل جمهوری اسلامی
و آمریکا که میرسه، یهو مصمم و قاطع
میرن کنار جمهوری اسلامی می‌ایستن
و ازش دفاع میکنن،
این یک نمونه‌اش!
به خاطر اینکه برای اینها مبارزه با آمریکا
مهمتر است! اولویت اصلی است و اینگونه است که جمهوری اسلامی تبدیل به یک متحد میشه براشون که باید ازش حمایت کرد!
و این روزها خشمگین هستن
از مردم ایران،  که چرا کنار آخوندها و سپاه علیه آمریکا نمی‌ایستید؟
تصویری از پست ایشون و یکی
از هایلایت‌های ایشون.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6361" target="_blank">📅 11:49 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6360">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">عراقچی در این بخش مصاحبه‌اش درست در خصوص آخرین روزهای منتهی به جنگ ۴۰ روزه صحبت میکنه. جنگ ۹ اسفند شروع شد و عراقچی از مذاکرات ۷ اسفند می‌گوید.
اینکه جمهوری اسلامی در مذاکرات به هیچ وجه کوتاه نیامد و آمریکا را به این یقین رساند که مذاکره نمی‌تواند گره منازعه هسته‌ای با جمهوری اسلامی را باز کند.
عراقچی به صراحت می‌گوید که چگونه جمهوری اسلامی تحت رهبری و افکار خامنه‌ای، جنگ را انتخاب کرد.
(با بی‌حاصل کردن گفتگوها و عدم انعطاف)
وقتی مجری به این نقطه می‌رسد که جمهوری اسلامی می‌توانست در مذاکرات، مانع جنگ شود (که می‌گوید باز ادامه میدادیم چند سال دیگر…) عراقچی می‌گوید : تصمیم گیری دست من و شما نیست.
این برنامه فتنه‌انگیز ۲۰ ساله هسته‌ای که هزینه ۲ هزار میلیارد دلاری بر ایران وارد کرد و حاصلش فقیرتر شدن مردم ایران بود، این سیاست ۴۷ ساله دشمنی با دنیا، این دشمنی کینه‌توزانه‌شان با مردم ایران، این جنگ‌ها را هم به ایران تحمیل  کرد، که عراقچی همین جا هم می‌گوید: مسئله ما زیرساخت و تاسیسات نیست!
«شکست در نابودی تاسیسات نیست!)</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6360" target="_blank">📅 10:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6359">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">پیام فرستاده برای «شیعیان» ایران
میگه اون روستای شیعی لبنانه که کاملا نابود شده،
اون یکی روستای مسیحی لبنانه،
که دست بهش نخورده! چون رفته متمدنانه داشتن.
این هم روستای اسرائیلی (یهودی) است
که با اینکه تحت حملات راکتی حزبالله بوده،
ولی داره زندگی‌اش رو‌ میکنه!
و میگه دست به اقدامات شامپانزه‌ گونه نزنید!
چون - مثل روستای شیعه لبنان - نابود میشید.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6359" target="_blank">📅 10:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6357">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rVoC8c8K8b4nV287Sze-5oQzjxqd7RhcuGpJAkCk8oq_JOMg9xhnM3A2LeAlsk-fU1v-iC_kttH0PyM31REHpoNkEBNyFwtlwWKdzL06zsn8EejydGatK7U2wsru_ZK7KKaNhrOvdqMfmZrj9TCGPzpoJDmvQEi7A5TjCi7GdzsxxBXfdcpu9ndDKqyJhpTZzepwNdTxSDVLfBx-6zopwTppMdb0omBfEI7mra5mFVbVPtciCkVOPbLBe6Fq_I6pDcyrAeOGEs_ymPg9Cr8m-_bb7d9YYc4SMO61_xvaG4H-lagO-N1mr2bkI2pBL851crMoR8L5ajQ7XCsbv2owfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jq-IfZpf6xqSn_ekBqfNqubW__ojZqS05EOt4gPj7oirlNeKCPI_IoX2LObl3-DJAhWHLz2ImTmSLqpf44JasB30sm0-WLDsQyp8xir5-YbjSVLJkgdyTUghpN8e8C2DaCwthMzVnHZwlod2cu4bEbJXc5Wb9jw3T_QWB5GsNtC5XIp6AEcGQXub_2lrWIcmz0lmJWHETB-ab-gv1etbesvhkF5sayyzFl5xrOsbA1jP0SQH35u_ASpWmXzHIsgtc3nT4qs2reFNpNpvVrdIa4Reu_y_vGw5qTX9YH2k7t2MgyPhDZcPcjMjZ1AZTZy1UOPktQ0J33q_vruIaWqvnA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این متن رو کامل بخونید.
در  بخش سوم می‌نویسه اصل این
بحران ۱۵ روز اخیر از اونجایی
بود که کشتی‌ها از سمت عمان عبور کردن و جمهوری اسلامی حمله کرد به کشتی‌ها
موردی که ۲-۳ روز پیش کامل توضیح دادم.
جنگ رو ج‌ا شروع کرده و دارند زور میگن به عمان
بخش ۵ هم بسیار مهمه، در خصوص کوه کلنگ، ج‌ا در عمق این کوهِ سنگ، غنی سازی میکنه که حتی با یک بمب اتم تاکتیکی هم نمیشه نابودش کرد! و چون خیالش راحت شده از اینکه غنی سازی‌اش متوقف نخواهد شد داره رو تنگه هرمز هم فشار میاره. اگه امریکا بخواد برنامه هسته‌ای ج‌ا رو جمع کنند، باید هزینه زیادی بده (جنگی بسیار بزرگ)</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6357" target="_blank">📅 10:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6356">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ثابتی میگه تنگه هرمز رو بگیریم‌ (که بخشی اش متعلق به عمانه) بعد بقیه کشورها از جمله عربستان رو هم مجبور کنیم از همین تنگه عبور کنه و اجبارا به ما پول بده.
(عربستان سواحل دریای سرخ رو هم داره و بدون نیاز به تنگه هرمز می‌تونه نفتش رو صادر کنه، ثابتی میگه:
۱- تنگه رو بگیریم
۲- عربستان رو مجبور کنیم که از اون بنادرش استفاده نکنه، فقط از هرمز استفاده کنه و به ما پول بده)
شهریاری میگه خدا رحم کرد شماها قدرت آمریکا رو ندارید.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6356" target="_blank">📅 00:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6355">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">‏وزارت خارجه جمهوری اسلامی اعلام کرد حمله اوکراین به یک شناور ایرانی در دریای خزر در بامداد شنبه، موجب انفجار کشتی و کشته شدن یک نفر و مجروح شدن یک نفر دیگر شد.
‏همچنین این وزارتخانه افزود،  این اقدام اکراین میتواند آتش جنگ را شعله ورتر کند.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6355" target="_blank">📅 22:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6354">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">‏ترامپ در گفتگوی تلفنی با شبکه فرانسوی LCI:
‏«اگر از جمهوری اسلامی ۱۰۰ درصد آنچه را که می‌خواهیم دریافت نکنیم، قطعاً بازگشت کامل به درگیری‌های نظامی را مدنظر قرار خواهم داد.»</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6354" target="_blank">📅 22:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6353">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UTtY5B2ysvHBF-IxU_VKmOs6wsamc8ii_XXGSTwZZbzEwtmnaUWTxza8aI8UYA7weTlM5KvXqVlZl6w1PhnnbB6xz6RiNj9euVQUp25CexS5TTGlaAX7tjMYiRe-6VjubO6pkpyweM2MGAIXjzAl9srkVvNHNkTG4AQhz2e2Y1ONRSN7m4DHNKttAz3ugXFa8TcnHJcHhvs2aqvsmcKPq7YjV03pTgDs0ScnAV2We8VSCiSPL6v3bvHO6WPaeC3FBuG59wVenWgsR74Qp0KMr6P0KnEaFDRwrZLZz-c25nN1ePZAnsFdyqWtPl7D2k7lBlRpZIr4xbSBjiqlh5pBcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجابت دعای هر روز مردمه</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6353" target="_blank">📅 16:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6352">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">‏فرمانده سابق سپاه:
جمهوری اسلامی و انصارالله (حوثی‌ها)  دیگر وارد چرخه جنگ، آتش‌بس و مذاکره نمی‌شوند.
‏حسین کنعانی‌مقدم، از فرماندهان پیشین سپاه پاسداران، گفت که‌جمهوری اسلامی و انصارالله یمن دیگر وارد چرخه «جنگ، آتش‌بس و مذاکره» نخواهند شد و این الگو، به گفته او، کارایی خود را از دست داده است.
حوثی‌ها دقایقی پیش نیز اعلام کردند که به تاسیسات نفتی عربستان حمله کرده‌اند.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6352" target="_blank">📅 16:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6351">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=ozDRZgp20kbFX2Y3OIhq6riI-u5fSpMHeAgqFNaLFAygt3id4LjHgBx7mzLcIdO8A-l40HKpGIIJxPM96u1yqQ8jmp9GQnV-v9p-NrCyK0OWFewzNiQzlvS5CJuyUNk9zcvDpf5-_vaxIqUS_G4udopMnKDpFE3UyNnS5gd-P2gbYitXKeG-3fN8kKiV-c3uhQMNqzEgEnyB59oy_HJyVudxa-9nN8SAT_SVUNy3rvtJgvxNi-0QQwNCoki6tUD9YevzVgnQLl98sgZETUgCzfYWchi9NV1JwYQqMjatLKALVfsxV3TPwmFB42IUc1pOki49_ZQxTkn_38q_2G3PZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=ozDRZgp20kbFX2Y3OIhq6riI-u5fSpMHeAgqFNaLFAygt3id4LjHgBx7mzLcIdO8A-l40HKpGIIJxPM96u1yqQ8jmp9GQnV-v9p-NrCyK0OWFewzNiQzlvS5CJuyUNk9zcvDpf5-_vaxIqUS_G4udopMnKDpFE3UyNnS5gd-P2gbYitXKeG-3fN8kKiV-c3uhQMNqzEgEnyB59oy_HJyVudxa-9nN8SAT_SVUNy3rvtJgvxNi-0QQwNCoki6tUD9YevzVgnQLl98sgZETUgCzfYWchi9NV1JwYQqMjatLKALVfsxV3TPwmFB42IUc1pOki49_ZQxTkn_38q_2G3PZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حمله موشکی اوکراین به کشتی حامل محموله نظامی روسیه برای جمهوری اسلامی در دریای خزر
زلنسکی با انتشار این ویدئو  در توییتر (ایکس) نوشت که نیروهای این کشور در حملات دوربرد در دریای خزر، شناورهایی را که برای انتقال محموله‌های نظامی مرتبط با جمهوری اسلامی استفاده می‌شدند، همراه با یک ناو جنگی هدف قرار دادند.
«با حملات دوربرد در دریای خزر - از جمله کشتی‌های مورد استفاده در حمل محموله‌های نظامی مربوط به ایران و همچنین یک کشتی جنگی - به نتایج بسیار قوی دست یافتیم.»</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6351" target="_blank">📅 14:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6350">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vMz-UvPh6M1Vf39A2lIGE32yXT55dq2BoAHD3o4NDJsf1dYCkBj6-WJyLLGtqppeZqQ595OXsWpEFgpSB2bp8NDmQDJuyp1KaPCK9SaACdlUbJHfGABR9dgu216nhBelHWUpdY43hSJqCBQ27ZyRTe6DTfTWET-ANVVXKOH_3vCY5XSeyeLlInrS-q6hBdEGRrJN4moaLnnchMDijZXvyF-fItnvdfnIRdggg6j4sbAQJNIP_mP5-E1czINkmEytvwJBhoaz94CzOoGDWQtgUe_dKrQz3oPwXTKNgECcm7NfQG5_lSB7TEozYpw0RkqD-bqoQVLuNChmnqjg7DWI8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازرگان می‌گفت ما شب می‌شینیم با اعضای ارشد حزب جمهوری اسلامی مذاکره می‌کنیم، در نهایت به یک توافقی در خصوص سیاست خارجه و….. میرسیم فرداش می‌بینم  در «روزنامه جمهوری اسلامی» و صدا و سیما کلی به ما فحش داده که اینها خائن هستن و…..!  بهشون میگیم مگه ما این تصمیم…</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6350" target="_blank">📅 11:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RacO6Aaq0jDfAGPdsp3hkwO8pKVMaTW-5BgzQABSOKVMA0kv0--FpbLFlKASJxeGluuxHtqlZT_vJrV-cklclecEaRgcIFOEYZDR15HTCYTT-Aks5mFfhOUFUdMcrRw-JabzoODS7PguZal3r4vjHvYIzyLP-U3PDehJ__elTDoH3JRu_F5IYkoypNmK7WenO_CgtEDjtjrjjWEd6HK7sOCIP5S9zwPPPm_SlFyV1SxLgewSToWiaFzYE1w5KMbDUqe_DjtR6ERodJvH8lEi1ZpSsmKuuPhA_ypPKac5Ra_CKLZtC9pRCyMiZ9E2p37NzeBUThBoP1Lfm4G0IegGFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خمینی بعد از انقلاب سریعا بر دو چیز  اعمال کنترل انحصاری کرد!  یکی کلید زندان و در اختیار داشتن تازیانه و دوم: منبر و رسانه!  تا اینطور بتونه به راحتی صدای دیگران رو خفه کنه و روایت خودش از هر جریانی  رو جا بندازه، رقیب رو از حق‌ دفاع از خودش محروم کنه، مردم…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6349" target="_blank">📅 11:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6348">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RLhjZcqDj53hTh_iexhneCPToscvusJ1zZddlDbdRZE2a5dX1ibHATpQvzbjGCfTjYhXDlMMYG6B1jXsNqqi8SfPjf84TlktIBGERYbWtfq95M5aKqV91rW5O74Bi8NYeeDIVGSAE49IHw5-nJznlIwxJqsMgmdBTPFAtcpdiJyctEKPvZVbME0qFxQjpMfFY0_6WYY-AMZQjObPWYN8_sSG9C2LvngrLcEoTC-GQv-ZZON4jQ97XLmttOm2XeLO2Z-Y_azN_QbHE0KaekKGFHWf9ek2CWvrN0dxNNocb0CyFUASUCWxAQrs_Drmj0uHEN9vlDujTgXnevLhX8c1-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو روز پیش صدا و سیما،  بخشی از سخنان پزشکیان رو سانسور کرد!  اونجایی که اشاره کرد که خامنه‌ای در نهایت  طرفدار مذاکره شد و کوتاه اومد!  وزیر خارجه‌اش ، عراقچی، اعتراض میکنه که صدا و سیما مطالبش رو درست پوشش نمیده! و میگه یک گروهی خط می‌دن به سخنرانان و مداحان…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6348" target="_blank">📅 11:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6347">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">دو روز پیش صدا و سیما،
بخشی از سخنان پزشکیان رو سانسور کرد!
اونجایی که اشاره کرد که خامنه‌ای در نهایت
طرفدار مذاکره شد و کوتاه اومد!
وزیر خارجه‌اش ، عراقچی، اعتراض میکنه که
صدا و سیما مطالبش رو درست پوشش نمیده!
و میگه یک گروهی خط می‌دن به سخنرانان و مداحان
در خیابان تا علیه «تفاهم‌نامه» صحبت کنن
در حالی که به قول عراقچی،
این تفاهم‌نامه، بهترین تفاهم ممکن بود!
[همونهایی که موشک به کشتی‌ها میزنن
همونهایی هستن که این تجمعات رو سازماندهی میکنن،
اینو عراقچی هم می‌دونه،
همون‌هایی هستن که در صدا و سیما هستن!]
قبلش هم صدا و سیما،
بخشی از حرفهای قالیباف که مسئول اصلی مذاکراته و رئیس مجلسه رو سانسور کرد!
(یادآوری : هم قالیباف و هم عراقچی خودشون  از مجموعه ۳ پ هستند! و باهاشون اینطور برخورد میکنن!)
این دعوا از اول انقلاب به وجود اومد!
صدا و سیما شد ملک طلق
و منبر اصلی «ولی فقیه» و شد چاقویی
علیه دولت!
حتی علیه خود دولت خامنه‌ای! وقتی
خامنه‌ای رئیس جمهور بود،
رادیو علیه‌اش یک برنامه پخش کرد و‌
رفت گریه کرد و قهر کرد و…..!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6347" target="_blank">📅 11:18 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6346">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=EPBrpgTEvFg538zN-pTYBPaUXu5aJ1HHyFaoDIxOB5v-4i8cUMgCnKIYoAWSk1QC41cNSiuzIGGVIywziLt0pTLl1KnW6JAOhEPcn58rHg-UDS64qqWrw0BL8iDuGHgI2mpHtfW9tiHRsa7fikBf4Kp3TThUzk0dl6X2f0Vo2-7c_EeeH_jmGKBh-Rnn1BNZIDZGHuQ90TEpErbk-sMlJpSo6zewZLW72-FL-HZf2YluvZI5PLeckwWhbDhKOwgSCd2WESguFMcEPe4CM1qchUNky-fk0FWmz6e0jM4Qh4OKyo4rBF9JDpf0kJUbxAoyrI5aXGkSgZZoilKS6tYU5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=EPBrpgTEvFg538zN-pTYBPaUXu5aJ1HHyFaoDIxOB5v-4i8cUMgCnKIYoAWSk1QC41cNSiuzIGGVIywziLt0pTLl1KnW6JAOhEPcn58rHg-UDS64qqWrw0BL8iDuGHgI2mpHtfW9tiHRsa7fikBf4Kp3TThUzk0dl6X2f0Vo2-7c_EeeH_jmGKBh-Rnn1BNZIDZGHuQ90TEpErbk-sMlJpSo6zewZLW72-FL-HZf2YluvZI5PLeckwWhbDhKOwgSCd2WESguFMcEPe4CM1qchUNky-fk0FWmz6e0jM4Qh4OKyo4rBF9JDpf0kJUbxAoyrI5aXGkSgZZoilKS6tYU5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری : در برجام ما به تعهدات
عمل کردیم اما اونها عمل نکردند!
عراقچی : ما هم عمل نکردیم که!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6346" target="_blank">📅 11:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6345">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/se6OOb702L_mVlvM0PF05-8xb34iHfSLUfnTe-4yNpqUDY6DuGhsJqWwkkXdeLEweF-esnYiIIxZI8I6dNEAV5oN9oxp_doz84dW7m6JKLhkFEj6Zz_3Rk_K9ZzSaf9ppJlMh2ZEmXOw7tTLVUTDJEDP-q9km18tjSAQ46Tn6hND-8eYDdgKiSljs3yZyIfgdMk6WlkR2ZOKs47pXtdT85kfygtcT6fLYgIsdFfVg0opHCAeqlfMc8f3bmAei_J0As3L3LR5Ax7JBfObpk_YwU2rXo-pk0Lkpsj4j5FizkN3UKz28rAuSL68JzwedMG0yY6p_zPhleauYBuY8g2g_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ‌ «در دوره من رژیمی که زمانی قدرتمند و هراس‌انگیز بود، رهبرانش کنار گذاشته شد.»</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6345" target="_blank">📅 09:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6344">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2f4e943e0.mp4?token=auirdRN_hJnrh-FDWpOjpgZtjW8SxIhu8Rzo4CemiYiVISq5IwU-8sFkia9XZQQpFNWX_0Vr3B0COHgUDRVfVIN_GoAWj8tTtWCzsREpnEIFLB8CtqlbUINPiAQl_viuJzlkWtiVfZwg6W__0-nPpWo6orXN0VD6_W7tnmrgQXMsK7b1dRyupVgDZtlp_OV3xU6ojf6XruSa5bRHzSsFKvJ_tzPgn187cvASA9y1wiEK_rkePnxHUa3XZxd7Elj2n9Z8Pg2GFTc-9riE4y7AFibKD1PCfBQCSfVWCbxY6qsvwbL4hP7ucs5SdNchl-njb03dNObmhVdiE1Rr-3qevQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2f4e943e0.mp4?token=auirdRN_hJnrh-FDWpOjpgZtjW8SxIhu8Rzo4CemiYiVISq5IwU-8sFkia9XZQQpFNWX_0Vr3B0COHgUDRVfVIN_GoAWj8tTtWCzsREpnEIFLB8CtqlbUINPiAQl_viuJzlkWtiVfZwg6W__0-nPpWo6orXN0VD6_W7tnmrgQXMsK7b1dRyupVgDZtlp_OV3xU6ojf6XruSa5bRHzSsFKvJ_tzPgn187cvASA9y1wiEK_rkePnxHUa3XZxd7Elj2n9Z8Pg2GFTc-9riE4y7AFibKD1PCfBQCSfVWCbxY6qsvwbL4hP7ucs5SdNchl-njb03dNObmhVdiE1Rr-3qevQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در سراسر این رجز خوانی
نه اسمی از ایرانه، نه دفاع از میهن!
نه رستم تهمتن!
شعارهاشون اینها بود!
تهاجم و حمله!
تا ظهور مهدی «در راه فتح فلسطین» میخواستن با اسرائیل‌و آمریکا مبارزه کنن و حیفا رو نابود کنن.
نه در راه ایران! نه برای ایران!
بلکه برای فلسطین!
https://x.com/farahmandalipur/status/2080726571627774147?s=46</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6344" target="_blank">📅 22:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6343">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n5iV9IlIfxaPrWNQ-wXQyvGRUbAs1xYubwB32CovEDl522k06SHGJaFTW9yPLdGHL2apGa50KvUA5bVMfO98GjY75Mxr-d_7mO2U51BBF0uhE2g6GTDPOuD8MUGCkUGMRji8lc4H6Hm4fwAQkiVQBngLErD6u-zzEougc0txa0pcj_8JoTBom_Gmrbrj8jJhwUEr0KLgqHIzmpPkljKyI15xPiYUDKWUn2j_u01L76vil-1Li44y99-Qgnn5XJP_RK9VhVQ5Q__I724MlQ-xExH2xY0EOiaVkPCICAxF7aQuvn78WarFQTj_-3vxXM_bmEzY8sEUlBHl6r_C7OUWZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حمله نظامی آمریکا به ۵ استان ایران
۴ نفر کشته شدن!
فکر کن جمهوری اسلامی هر صبح
با صدای اذانش، بیش از این تعداد
از مردم ایران اعدام میکنه!
جنگ ۴۷ ساله جمهوری اسلامی علیه مردم!</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6343" target="_blank">📅 19:38 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6342">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">عراقچی میگه توافق ما بهترین توافق ممکن بود
اما به سخنرانان و مداحان تجمعات خط داده شد تا علیه این توافق شعار بدهند.
همه می‌دونن ریشه جنگ‌ها، تحریم‌ها، تنش‌ها، انزوای ایران و….. همه از خود اینهاست!
قبلا هم همینکه در بیرون به توافقی میرسیدن
موشک آزمایش میکردن و روش به عبری
شعار می‌نوشتن!</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6342" target="_blank">📅 19:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6341">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">سپاه خطاب به مردم منطقه : فورا تا شعاع ۵۰۰ متری از محل‌ حضور آمریکایی‌ها فاصله بگیرید.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6341" target="_blank">📅 14:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6340">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fIHWRufp1a7nFCxqfZITRvZ0Wuk6T6q1Z4os0nLwDAeoQxV8G4_Z0E4LFc0zpA3wOPXag9x4fr594X34Aug_my0_ZnhWol6yiY8UdXpGrCPUL-GgqRMx3RaE1tjO6bXZ1zVu3AWbLuA8XyBdYgsIXT2bkiN-HgMRyDnFR7mzoZwgQDfGUHbxJP5fRV6GhhUs98-uqFyquTzX7zMLdwmJRNN0pN1QATU5u8sRwERPJ9xZegfn4934TY-FHrBHRuoN3GYIP_2fcDYnl1U9ORXu9r9Hhcx5dL94AE1HpRJ4MlSE0KvoLiNR3jdLRdsmbb3o5faXHfc-EoUeWiWHniQAsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه دوم روزنامه کوریره دلا سرا - ایتالیا
حمله دیروز گروه تروریستی حوثی
به دو کشتی تجاری عربستانی،
حدود ۱۰۰ میلیون دلار خسارت وارد کرد.
ترامپ : هزینه این خسارات‌ها رو از پول‌های
مسدود شده ایران بر میداریم!</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6340" target="_blank">📅 11:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6339">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07c232479.mp4?token=D2iKvYYDFOwL5Ga--Udic0ZQE2NodvCk3mqwQ_X7G7nz2YLqJ2P7kuTP2AV6DCeCGHcKhVCiGoVSPgQen6NZ66DjNPpTdM3LvNeRmjCrz_35bR3gccIox6SE7Un_aEnyJ5-v09M9IoqdRBd7ck94MHIBsQ8TWm6RLAYuNT-Kt7tPKmWHwj_EFrDQhjoI5xs9Ik1kfMijre1uVijekxXNXvYv16fQzlfCtI2wpMHCJaJ0W3J5b96IP5hUQlGPOTnuwfkzUPZ2yO3OxOLf9wmvlxJ6yskzFtjs4H2CZAysPVgJjfzI-b2lWRGHTlpi6U9z_-9snRtzNPxT6Ht30OQxyKuQvnGz5Otu6ZVIjoLsve3OVxKJnucch0eIy5u96Uaq_oCUFDB1c4L1_IA9lCId5LsCP3_DQO551ABGg9aX6EIe4NK-2uJ3qjJ4ZBH1beWERKauceT419OVTKSaHEBcuQ4iNNBmZtK5xnwTMFM3VFPD56izs29qbTz6ZRAYMV4jhhWM77ZtBRgBd95BFYp9MQUUsPpPhACeTZ3kiX4vBjq1_rYk59NcSlIZI2vJu62WJvRNt2EvCur8W0zXouw61qmAlGRlId4Yk0ncIrpHxyMzb90i3DQNx6wewgF6F6aNw6R1Ow45cN634FDLag9zmVD0491oKgiEg7N_dDQ4akw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07c232479.mp4?token=D2iKvYYDFOwL5Ga--Udic0ZQE2NodvCk3mqwQ_X7G7nz2YLqJ2P7kuTP2AV6DCeCGHcKhVCiGoVSPgQen6NZ66DjNPpTdM3LvNeRmjCrz_35bR3gccIox6SE7Un_aEnyJ5-v09M9IoqdRBd7ck94MHIBsQ8TWm6RLAYuNT-Kt7tPKmWHwj_EFrDQhjoI5xs9Ik1kfMijre1uVijekxXNXvYv16fQzlfCtI2wpMHCJaJ0W3J5b96IP5hUQlGPOTnuwfkzUPZ2yO3OxOLf9wmvlxJ6yskzFtjs4H2CZAysPVgJjfzI-b2lWRGHTlpi6U9z_-9snRtzNPxT6Ht30OQxyKuQvnGz5Otu6ZVIjoLsve3OVxKJnucch0eIy5u96Uaq_oCUFDB1c4L1_IA9lCId5LsCP3_DQO551ABGg9aX6EIe4NK-2uJ3qjJ4ZBH1beWERKauceT419OVTKSaHEBcuQ4iNNBmZtK5xnwTMFM3VFPD56izs29qbTz6ZRAYMV4jhhWM77ZtBRgBd95BFYp9MQUUsPpPhACeTZ3kiX4vBjq1_rYk59NcSlIZI2vJu62WJvRNt2EvCur8W0zXouw61qmAlGRlId4Yk0ncIrpHxyMzb90i3DQNx6wewgF6F6aNw6R1Ow45cN634FDLag9zmVD0491oKgiEg7N_dDQ4akw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت وزیر نفت دولت رئیسی از تماس موساد با او و انجام حملاتی در ایران
🔺
جواد اوجی وزیر نفت دولت رئیسی : ما ۱۰ خط لوله بزرگ و سراسری گاز تو کشور داریم، تو یکی از شبای بهمن سال ۱۴۰۲ ساعت ۱ شب موساد با من تماس گرفت گفتن امشب می‌خوایم آتیش بازی کنیم‌ باهم،از من پرسید ۳+۵ چند میشه؟ گفتم ۸، بلافاصله گفت همین الان خط هشتم سراسری گاز رو زدیم، ۵ دقیقه بعد دوستان مسولین بهم زنگ زدن گفتن خط ۸ گاز کشورو زدن،تا داشتم لباس میپوشیدم، موساد دوباره بهم زنگ زد و از من پرسید ۴+۵ چند میشه؟ گفتم ۹، گفت خط نهم سراسری گاز رو هم منفجر کردیم،چند دقیقه بعد مسولین مربوطه بهم زنگ زدن این خبرو هم تایید کردن،من تا رسیدم سه تا خط اصلی گاز مارو زدن.</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6339" target="_blank">📅 08:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6338">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=AGGA2pmQyRz9BzLNOBH84-2F49TYsPzBWCSV-9vrJfptdEWJU0Lm2KvxOPJiLYw4qhOyE3c1Y4-1uzJ8yEDzLk9doE-FxEjoFa6MFHosDZgJY-m-_E_BC6xBRMh98ZaQ5mZVUrbx6C8j9GKJqV52Lya_3xmdXLsnBRoHlBKrCmW513TQJPv7-CMs7FPIrEvBZhtCIut9U2fnRL0vtisMOPgFI_ewAvWdTAsYq_q-_ofn--s7pc9eE-71oiuNubZ4U4DxOMbAvwovo9IIZNDj6i6T2SXKsEKF_18p96hjP78RiiC0F9Ft73kvWuEkmBLzIK_DX7Wuoo8SS2IcdrNiXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=AGGA2pmQyRz9BzLNOBH84-2F49TYsPzBWCSV-9vrJfptdEWJU0Lm2KvxOPJiLYw4qhOyE3c1Y4-1uzJ8yEDzLk9doE-FxEjoFa6MFHosDZgJY-m-_E_BC6xBRMh98ZaQ5mZVUrbx6C8j9GKJqV52Lya_3xmdXLsnBRoHlBKrCmW513TQJPv7-CMs7FPIrEvBZhtCIut9U2fnRL0vtisMOPgFI_ewAvWdTAsYq_q-_ofn--s7pc9eE-71oiuNubZ4U4DxOMbAvwovo9IIZNDj6i6T2SXKsEKF_18p96hjP78RiiC0F9Ft73kvWuEkmBLzIK_DX7Wuoo8SS2IcdrNiXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - انفجارهای پی در پی در بندرعباس</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6338" target="_blank">📅 08:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IMzoedkgExgtojCS9jji-DLeBPnQwBpIaW4rjOQOYMxo3L-hZwmfKSScs2vpaPu_AJdQOnhBY76S4sAxgOKj-9ukjlgIx5GxygtP-B5UgU_K4s6_s4EJYfybvzw6Ex2jOxKtAie_l3g4sUW5oKAaLJ55Ywh8T8LqCQ1OlhR-oP4PmKdxgFJINhFDhNQHP6bR8epLTOFU2dIJT36xrNoDMwlPA2geOLd7MY4k8gXu_Wk1fbt7akoxGMhDb2Sg2RWOMHBVcXoE6AmM52rYj9ChefzRE8WVfI4wpcpxxJrDkPHiarfKzGYFYlc3pGR9UCK3PJmt2tDYxdMXyWn1u9fDjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید تازه ترامپ‌: از پولهای بلوکه شده ایران، خسارت کشتی‌های آسیب دیده توسط جمهوری اسلامی را پرداخت میکنیم.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6337" target="_blank">📅 08:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6334">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=JusnSQUDWb2ZTVbsDS5Ckl3xW4YxFXB-F01yZXdOXofhnt0yGvBpTHi2fYA0_CUa2-ME5D6Kcky8095gWgbHyRJX6EpypFZSrtdnYYd8xXixV-T7FeRw2EG_cVoixvG_wYmSxLDvAJcnxEcKsqbn08OOnEwFPMli6TnGzPCO34-1_r8K48sIUpCjt0HkYIZQB9E9Gt9sn-wekX06qDxEhdUa9RJ1hHjiRBmvBLGRXA2lp9igfLYbHQXDJRICvtfo0xS6qKynK90-yaL5VeRqtVVNDSaehEwhbaSJ-NpeWkfDWkYB5xlROtBTc1FxQcjhXobI_R6elgTWasBA10ScQTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=JusnSQUDWb2ZTVbsDS5Ckl3xW4YxFXB-F01yZXdOXofhnt0yGvBpTHi2fYA0_CUa2-ME5D6Kcky8095gWgbHyRJX6EpypFZSrtdnYYd8xXixV-T7FeRw2EG_cVoixvG_wYmSxLDvAJcnxEcKsqbn08OOnEwFPMli6TnGzPCO34-1_r8K48sIUpCjt0HkYIZQB9E9Gt9sn-wekX06qDxEhdUa9RJ1hHjiRBmvBLGRXA2lp9igfLYbHQXDJRICvtfo0xS6qKynK90-yaL5VeRqtVVNDSaehEwhbaSJ-NpeWkfDWkYB5xlROtBTc1FxQcjhXobI_R6elgTWasBA10ScQTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نصب ماکت آبگرمکن در مرکز تهران</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6334" target="_blank">📅 22:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6333">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
ترامپ به کانال ۱۲ اسرائیل: در حال بررسی یک حمله گسترده به جمهوری اسلامی هستم؛ حمله‌ای بزرگ‌تر از هر اقدامی که تاکنون انجام شده است. به تصمیم‌گیری درباره آن نزدیک هستم.
او در خصوص احتمال مشارکت اسرائیل هم گفت اگر از آنها بخواهیم ظرف ۲ دقیقه آماده می‌شوند، اما برای آغاز عملیات جدید به هیچ کس نیازی نداریم!</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6333" target="_blank">📅 21:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6332">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">‏هشدار سپاه: هر پایگاهی در بریتانیا که برای انجام حملات علیه ایران مورد استفاده قرار گیرد، یک هدف مشروع خواهد بود.
‏واکنش سخنگوی دولت بریتانیا به هشدار : نیروهای مسلح ما آماده‌اند تا از بریتانیا در برابر هرگونه حمله محافظت کنند.
بریتانیا به‌صورت شبانه‌روزی و در هماهنگی نزدیک با متحدان خود در ناتو، آماده دفاع از خود است.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6332" target="_blank">📅 21:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6331">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FFhBEgv0-AAu2UuuvdEqW3B2YO_3BydhBNLGu-gpY7w_P-lVjhMueJJu4XAPYjsl6afnaSBQ0UCv9kWhCKwt5wI7qYKKg9OOKYXVgJwW76fdSL5InSOMHCR7lpS2qOS2eAQw93xD7pQGtNnV080J8wF8LLX01hvQ1mLBy4egXvP7aX2iDUnnagBDsShc_3KP0XbBV6PAGBf6aGA-oMu3VuoIj8poDby6nK3E9mYiRKhabKOp72bU91oJfYKwnAzRZY5cOyfISgummtLD6ecoCVM-OLttL7y2Hln7M9etfg6aYCjS-vu1ehaVhid-M4owc3CLZ0qLcZy6_Vw7qLeGUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضرغامی : فعلا حرفی از مذاکره نزنید!</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6331" target="_blank">📅 21:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6330">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qnTdFyNNzIqHVAiUCCd2vply_6Zg32r1KFDk6W-UKkM6INO4BafX5YXV2MLTNnLCQ7wsmq9hec5E0zYBYGvAjjGEf10kJG53GMNSu2t_v84yyu45NWVBdMl9UfCUputcSdtHiIec44kjr4totgAhky4rK0ftW4cW0JctRXudvMLGZnCQ_tF3tEbb1fhYzCHuzof2Ymn1IUlXSy74xN2U_mFBglAiap9WY03-tGZOxn_V6ptax-NlQT71KPaTSFYB_gfHWOiZTrDkAWUE7wIJLvkxeByeI8a6ogoXR_dt_9gY7PSzfbebpAz5sv4F0tW_eifrbNVHY8uDzBk7i2oJ0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو حقیقت محض
۱- تروریست‌های حوثی به تحریک جمهوری اسلامی وارد این جنگ شدند و به کشتی‌های عربستانی حمله کردند،
پس مسئولش جمهوری اسلامی است.
۲- حوثی‌ها ارزشی برای جنگیدن ندارن!
اینه که ترامپ مستقیم میگه فاکتور هزینه
حملات حوثی‌ها رو شما باید بدید!
و این یعنی بازهم ایران باید هزینه سیاست‌های جمهوری اسلامی و نیروهای تحت حمایتش رو پرداخت کنه.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6330" target="_blank">📅 18:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6329">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZUCqjmAV4tkWsxdQIsw9_DzOu87T2X25jDZ1IE4P-qLMMC7xgNIogicJ3ZuQRePC0s4Exa0INC4_qz1FdGFowdA-87yIVnLIo32tVfUIR5m_CDrs8wYJWJvqJQeZfXjbBDuRvIDnN5EEP44SlabV5M-8U6kKX1hXw-sM1ByK936QOxsMSPfSjXJJSrrqrEtfVtSYmZH7VF8sxVHBcYmjxcJf1nsrQy1jtzktS08RYoX00DyVqB_Q3jq9KW9Gjkjx-t6tgQrBs_f9ai0Xm5raOOawmDy6-fdKfXH3nBTibqqqGBd7yuEH2xUPrRi-KF26TX3gaigObL7EhrQpPwBriw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاآنی، فرمانده سپاه قدس، با ارسال پیام تبریکی به «خلیل الحلیه» نوشت: «آنان با انتخاب شخصیتی که نماد مقاومت و شهادت است، بار دیگر اثبات کردند که همچنان بر استمرار مسیر مقاومت اسلامی تأکید دارند. مقاومت اسلامی امروز قوی‌تر از همیشه، مسیر عزت‌مندانه خود را ادامه…</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6329" target="_blank">📅 18:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/juTyyJjFunTeY7XbRzqjChBjwMie_fzfCD7T7-AnR_MOPhyN9GMTrkHlUcDUw_B3efpMAl64_0JDzVYJF1CaQcGY_DbuV-XeFChX0CcbVpJe1M_5Q2CGgeRVg07yy1lgSPcoZlw8qfOEgyMLI5_Dy_lVYxwg6I_bUQYveAofYXzzZTrwtq2x-1mFEYLfXa3vG0LT-qNDp-fc4_fGeeT-Y9927RpxiRxaOEuLp6e7Jj4hJzzFMayj1xmIVV6H-15-fcnuAK0WleFndfLS_8mtvNktxqUoOsSTzuJIx-j-GuFnLzspvlG8OiltGU3fs02nujwxPOKTuX8BvA846-t8oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6328" target="_blank">📅 14:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XqINZuvZjjAZYIUqAn7QJ3dsfL6cePL3LTiF8znt_skRXcaot7oZIBZZps-3WD_dw6L6n4z8TsoNV84XyALqeIHIaqMDU4etzTWRbDWJJVRbuAGaYpS7l39atl5gMjYOiol8uRXmoLowrwoXt5Uq7WOZO9j4al95-aA5lg8s5X8NK7TJwPYp8cUEcmOKN-VyxvhfSi523jPe-nIieSxwxTnGQTm358sTmrJQL503ZzQvyEyFVT4CUFsX4hpd5qt5ZTjmj2LGiv-1XjBiKVewOoTu1vKoFStkFKDUA71KEDk0PwhPayfvodImV4XR1gNYO5S84uIJQSBnP5-VWxUZWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6327" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6326">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=oRnau4V0eIlR1zDFOXdTfxhWiDCC4ffJlcz8SkpT9Ygrk4_rlOHqWR3yyU2x8WGCeLzlYp8qzGhyHTiVBVqLGqPr9bL_zFegdc87ZdLVxr1HR8v6-TONOJSbyMfFxfiKkpJIC1XNd2uEa-1Lp6pg6Zv6BGFUHeGA_qTZ5bKAaDkoJzwbuaHvGnodOlFRyMfviNMU8ZOt9T5UQ0SeG7f4e3Oi82UUIVZKtm3gzcGZrNw1nGcIISmai3bKxOyCbDDuOmNgepzKC5TgNG4rl6RL5S3HsQlnklHpV-KbrUv_i_71k-b2IUMKdlG3V--2CCapj-EEQOn_DapbMy9HrWnJ4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=oRnau4V0eIlR1zDFOXdTfxhWiDCC4ffJlcz8SkpT9Ygrk4_rlOHqWR3yyU2x8WGCeLzlYp8qzGhyHTiVBVqLGqPr9bL_zFegdc87ZdLVxr1HR8v6-TONOJSbyMfFxfiKkpJIC1XNd2uEa-1Lp6pg6Zv6BGFUHeGA_qTZ5bKAaDkoJzwbuaHvGnodOlFRyMfviNMU8ZOt9T5UQ0SeG7f4e3Oi82UUIVZKtm3gzcGZrNw1nGcIISmai3bKxOyCbDDuOmNgepzKC5TgNG4rl6RL5S3HsQlnklHpV-KbrUv_i_71k-b2IUMKdlG3V--2CCapj-EEQOn_DapbMy9HrWnJ4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جدال لفظی دو نماینده مجلس
بر سر تنگه هرمز
(پشت پرده دعوا : شهریاری اینجا داره میگه
که تنگه مال ما نبوده  که بگیم میخوایم بدیم بره،
و میگه تحت یکسری قوانین
بین‌المللی است و زمان جنگ می‌تونیم ببندیم برای فشار آوردن و….. ولی مال ما نبوده)</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6326" target="_blank">📅 13:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6325">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l56ukeOTvJVui8hHKY3clhHafqeeJ3ux6mgKwxD9AymxXYn2LSgsRPI3PLSkpWJgOMHelZTn-BG-tY84_PD9VsTJxVuRVlF2FQjLHOPYGYnf70ExcXEDJ7l_nrOCQ1T0aUJfqKQLzuyAc66CHonN9uUKO7DvckJvn_LuBqo32dDivzH0Db2Hy-Kg1sK6F4GoLRWbfEVSBPpdGBBY8c5kPWo36r5bDZhTJxG1YJkOA3zTDUsY2wmZgePbYhOtKjRtU5-2uzjPYjSysXtm3RaDVVDlhB0k-dVq7rW4Vmgh5kN9bvrOsJxal63HMW3N6TGR638CebGwkdCO0B9f_qnNIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6325" target="_blank">📅 08:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ujOQKOFO728mTgSMIMx4Y99-OV6mIEbY1ajXyUWEwAOiWlC0ytv07VFWWRx6EXjkyKd3VaBGmSRslLR4H-J4zmOsd8eis752l6vIGL5YHBVDka9ZeHvs3PfI1YunJdfyO2wlzbAz6KEq82Tda7CuDkgvpnIM0DeJPsOI3zs7BpwE08y1mFrGXxGCguA9EKeXc2NgCGToBi3IUu8RmYflEuUgDjvmIgxhM23y2IlZ3KjezURnwFB3tQPirOWtTHkaqelSRDQLG6g2cEwwGrP3Z4nwfKUblCtKJZQ7JS458URo-LHX7gRszVlFFMOfSRMVEU9-8eomEthPXd8B3xNX-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در یک تحول تازه در حملات‌ ۱۲ روز اخیر
و نشانه اینکه حملات وارد فاز تازه‌ای شده.
«بی‌ ۱» برای حملات بسیار سنگین و عمیق
استفاده میشه.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6324" target="_blank">📅 08:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6323">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6323" target="_blank">📅 08:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6322">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">جنایتی نبوده که جمهوری اسلامی
در حق مردم ایران انجام نداده باشه</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6322" target="_blank">📅 07:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6321">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=jk85znVGnzkRj8PH3r_7d0OW3F2X0wok153QugxhosrNOhyEqouLyOvWWPd8QW9RIQcJNAuIz591DYro-74CLUc-olttAEquZe264nY89eh99Im46bsVmXbNzHK60poFhhk7ZKYXg4RULGhBQw9nWU0EllR183Zhv5LVf0nHhW0gaxNqwKswBSdoDNQLSwHha_cGGBJDMx6XFJFK3qmNZ5p5gKuSkGpqeto_1ve6bW7oI1rnHzdBLc9BYMMRSdfWYfctMsL45X79wuqT7gocpMWijbRjXyv1EWcXWZ8815Mn_Mumo4dCTaXFqkLbohMdt574YoYA_gg63VychA4EW5rPqALYynkQnDwREb5v7mtfJz4_8hbgMg5GXxOKPVgDros3zRWg2tSYo54I7zx7OnmxZExebA5bt3k_YdtK-I9K2Z4xONKZmfYxDbc0n-RkVARXM-kRbEGMxyOj4kWKOWej-2ARQW6BuIJ3L_1HgG1kxb5_sXQdbN9jOELrGmU3yvI35uIS7LU99fxb2ItP3CF5Moyba0cKC-fDcWlpMYpUwoeZxIDbHRmFnI36kEVDKH9hvIpu_Nbf2z7qi8UrV1iHc4_xVk3OjQljVoq742fDCRUy_eAECoj9W5STUSvmdh3HVCaoI3OWbmqmF9rzf4Iq1pyitPuOVUvOzWvjdgc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=jk85znVGnzkRj8PH3r_7d0OW3F2X0wok153QugxhosrNOhyEqouLyOvWWPd8QW9RIQcJNAuIz591DYro-74CLUc-olttAEquZe264nY89eh99Im46bsVmXbNzHK60poFhhk7ZKYXg4RULGhBQw9nWU0EllR183Zhv5LVf0nHhW0gaxNqwKswBSdoDNQLSwHha_cGGBJDMx6XFJFK3qmNZ5p5gKuSkGpqeto_1ve6bW7oI1rnHzdBLc9BYMMRSdfWYfctMsL45X79wuqT7gocpMWijbRjXyv1EWcXWZ8815Mn_Mumo4dCTaXFqkLbohMdt574YoYA_gg63VychA4EW5rPqALYynkQnDwREb5v7mtfJz4_8hbgMg5GXxOKPVgDros3zRWg2tSYo54I7zx7OnmxZExebA5bt3k_YdtK-I9K2Z4xONKZmfYxDbc0n-RkVARXM-kRbEGMxyOj4kWKOWej-2ARQW6BuIJ3L_1HgG1kxb5_sXQdbN9jOELrGmU3yvI35uIS7LU99fxb2ItP3CF5Moyba0cKC-fDcWlpMYpUwoeZxIDbHRmFnI36kEVDKH9hvIpu_Nbf2z7qi8UrV1iHc4_xVk3OjQljVoq742fDCRUy_eAECoj9W5STUSvmdh3HVCaoI3OWbmqmF9rzf4Iq1pyitPuOVUvOzWvjdgc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">- رئیس جمهور سلام میرسونه و تشکر میکنه
- باشه</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6321" target="_blank">📅 07:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6320">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
در جریان حمله آمریکا به مرز شلمچه ۲ نفر کشته و ۱۱ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6320" target="_blank">📅 06:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6319">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">مارکو روبیو وزیر خارجه آمریکا : جمهوری  اسلامی تفاهم نامه را نقض کرده و لذا دیگر  معتبر نیست.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6319" target="_blank">📅 06:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6318">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65da400742.mp4?token=el3c6i-rGEnQZpN3Hk-zf7wajDZBFrecD2RsYU45scdqwCGGeE7EF4cbUmfuYtSFxNHy6CYIF79SykHfEyOPFZgQ6wwwLctndUQnwWSrfyaBMpmS3ZAeEy0J_sLQjXw2zYYkGNfEjLxYQcd65VAe1uVPYDtWLf_ncHLmOvoqFxzfCpjMvh6PrnFxwIb88gLA9nWMYH99x35tA7MAUXVKFFSH6sZ7VA7tcghUMsD9PCKEXY6JCdTn_l2F1HS0dNe2UXXc3QxIxX6DG80M8SxGHiHXWNXHBO9ch0_NOaqYgk7OxvrBXU4viEUfxcHTHGgIs8uRyBFOZCThQ6P-pFifVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65da400742.mp4?token=el3c6i-rGEnQZpN3Hk-zf7wajDZBFrecD2RsYU45scdqwCGGeE7EF4cbUmfuYtSFxNHy6CYIF79SykHfEyOPFZgQ6wwwLctndUQnwWSrfyaBMpmS3ZAeEy0J_sLQjXw2zYYkGNfEjLxYQcd65VAe1uVPYDtWLf_ncHLmOvoqFxzfCpjMvh6PrnFxwIb88gLA9nWMYH99x35tA7MAUXVKFFSH6sZ7VA7tcghUMsD9PCKEXY6JCdTn_l2F1HS0dNe2UXXc3QxIxX6DG80M8SxGHiHXWNXHBO9ch0_NOaqYgk7OxvrBXU4viEUfxcHTHGgIs8uRyBFOZCThQ6P-pFifVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون بابایی که با نخوت …</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6318" target="_blank">📅 22:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6317">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=t-iLWePhESkLrxXqQiPfcAYeNYsh5QE8zXxwBYWtfApjSzcCSRHwjbHFZhRQVtwykJ7Ml0RMB4yvUkSH8WxNIORokDv4kdC29P0b-cGh_gwigY6geCIZsAHYZ06zy-vdHPlIppept9yUW2FnPvipDTmeY5mGn8oVTolfilTlxEhsE5cZB-zFST-8zDuj7U5aCztK3Vl0RuQ3TofNYjUPXKIPLw6E3kKA7GMtuZ55a8jyXS8yamkoNvk2n5EsqA0Ihs0cETXyla0T6SLuR2BzLpFrHsOS65mX84nvgzpkDz3a00OltxyqGkB5380U3ps4PZftv_2q_PXwtAvr_D7JIkATkAxWSMG0jFBw4ci4z1Vet5GiZC_5eaulKKr6Vto15BgfaVsnQeDa1Eg2XxWS3561v7Zx-WrVlV6_5grH9G3NUlIah1s00hsknsulM04LMTq4XpRqyF6RG7mKw5bR4uRGFviEucMxzmV0uTAnEXv5uCVLN8BNiJY1jd3LnfueQJnz2JkbXk-OVre9Iiy60Bsqf7hFReNqpY6O4w_DTt01cnfZCM0nH29ppw1iGTXeKIna7InLQnzsCwdrmbCXa26pMDsyqpgRGJVzAtDU1u3IlXU0fIpw9c35kAoWhWRSccapLEDR7LUZ12dDT6IVwjWhYEFfBEYA3d-xDnQsKhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=t-iLWePhESkLrxXqQiPfcAYeNYsh5QE8zXxwBYWtfApjSzcCSRHwjbHFZhRQVtwykJ7Ml0RMB4yvUkSH8WxNIORokDv4kdC29P0b-cGh_gwigY6geCIZsAHYZ06zy-vdHPlIppept9yUW2FnPvipDTmeY5mGn8oVTolfilTlxEhsE5cZB-zFST-8zDuj7U5aCztK3Vl0RuQ3TofNYjUPXKIPLw6E3kKA7GMtuZ55a8jyXS8yamkoNvk2n5EsqA0Ihs0cETXyla0T6SLuR2BzLpFrHsOS65mX84nvgzpkDz3a00OltxyqGkB5380U3ps4PZftv_2q_PXwtAvr_D7JIkATkAxWSMG0jFBw4ci4z1Vet5GiZC_5eaulKKr6Vto15BgfaVsnQeDa1Eg2XxWS3561v7Zx-WrVlV6_5grH9G3NUlIah1s00hsknsulM04LMTq4XpRqyF6RG7mKw5bR4uRGFviEucMxzmV0uTAnEXv5uCVLN8BNiJY1jd3LnfueQJnz2JkbXk-OVre9Iiy60Bsqf7hFReNqpY6O4w_DTt01cnfZCM0nH29ppw1iGTXeKIna7InLQnzsCwdrmbCXa26pMDsyqpgRGJVzAtDU1u3IlXU0fIpw9c35kAoWhWRSccapLEDR7LUZ12dDT6IVwjWhYEFfBEYA3d-xDnQsKhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن روحانی ۱۳۹۷
تا آخر هم افتخار میکنیم به نفوذ
در عراق و سوریه و لبنان و…..</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6317" target="_blank">📅 22:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6316">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sslcTtXubYgGbcHhb-EtHU7_8SWPwGQqCEKe07GyhD9FNf5uuHzk95vtlN-Xp2-JUBg16niXXOrM-355ZOrwfj82Nvb9SRx8Mz6j0sc4bH-Emc_4fb-OBFC8BxSg_Pn8rleITLl2MbO7xigffC52J2yQvOsN9PYyuU9-xD5OaVZ4w26-Nx3fG_TgsWe8M0WxKbhY_j4kh0uUhefYERUgrVaDnEqPqKFnwce66EvsGCBlnzZrvkL2DWHILJyv6XL-34olYPAyr0keGUDDQY-FB-DqYuFb6qF9KiIvS-wnzZUk7OS5TK1CFJq-i_ZK1g8a1wUNTNievIVoq5b76gkg2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏سخنگوی سپاه خطاب به شرکت‌های کشتیرانی‌:
مسیر مین‌گذاری‌شدۀ جنوب تنگۀ هرمز  [ آب‌های عمان] مسیر نابودی سرمایه ی شماست!
قرارگاه خاتم هم دقایقی پیش هشدار داده بود که فقط از آب‌های تعیین شده (بخش ایران) باید تردد کنند.
جمهوری اسلامی رسما آب‌های سرزمینی عمان رو هم ناامن کرده.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6316" target="_blank">📅 22:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6315">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
قرارگاه خاتم :
تنگه هرمز همچنان بسته است و اگر قرار هم باشد شناوری از آن تنگه عبور کند صرفا باید از مسیر تعیین شده [از سمت آب های سرزمینی ایران و نه عمان] و برابر ترتیبات اعلام شده قبلی تردد نماید.
‏
🔺
در صورت عملی شدن تهدیدهای آمریکا، نیروهای مسلح جمهوری اسلامی ایران اجازه صادرات یک قطره نفت را هم نخواهند داد و زیر ساخت های نفت، گاز، برق و اقتصادی منطقه مورد هدف قرار خواهند گرفت.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6315" target="_blank">📅 22:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6314">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U8O93BRzFSBF5j7oKKp67JEhMc9q-QNnbGRNXcHqjwS7ikfpz9fIU07a39FVBtT7G5SfsCZLKnmN2h1G9K3VT6kVFT_mOdC_ZAf7xQS4J989Mv6BZPGtQvYvgoYbYY1jgMoW2HMmDAcZ9oRE190kex1Jhi6X43k5hTg4-3jHbQggtsFWqrsxKmD2_cjBG6gUYNOpVxPc-r2NEmjeKHdVUJawbcB9c3uotURQLsiBRcZ_2H1Hqk7SDJ3BXTJaKJ_2snc0hB125c4TuT_UNqxnvI8RCG30j1xug-Ev0IkeHQVHpK8rS5AzOvBEsPSOAKjij4sPZGeL2T5xzL1XOHRvog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6314" target="_blank">📅 18:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6313">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vzVfvX9jlsgDWOiaqJHovOYVgwi9A3HZyBRKa9p21ZV76rday4oy35QKZbq2yNlF3ZixaE4tZGmbOZKMJ2rDr0hQegVsurHIXbyL4V3rNaVgYuDPNTOK5AYdQBYmPtRZp9GOHjavYV4I9gMO6MW2HkyO0MVxRHCuyMxpL3umfdlL8xPjR81v300JySS934vAU_az0cOdsz4YOMtoguVwDY96QoaujA4Cdn3GLQ6XSAs9SA69L1HmLGGoMtBKLa-AmASZpiUu7uiSonyBOBpOnjtWCoLlFxlDcl0SVIUdOuART9_97HpeY96uVkU8myiUggt1YCR57KFgHtc_8-ggVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6313" target="_blank">📅 17:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6312">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
شب گذشته صدای انفجار و پدافند هوایی در ۱۹ نقطه کشور
تهران،  بهبهان، امیدیه،  ماهشهر، سیریک، بندرعباس، بوشهر، چابهار، کنارک، تبریز ، بانه، کبودرآهنگ،  همدان، خرمدره، ابهر، زنجان، دینارکوه،  چوار، آبدانان و انارک.</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6312" target="_blank">📅 08:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6311">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=nhocHYsNgO1IUFE4JxadrDrTwJEeenhtZZNm4qJ1k6e2GchmG8yKoiVx-yMNCzghWa6RwOSC0KSnFkK04H3ixS28C5KdZzKma8OqmCl2p75UU_eG6RlHzGhpRKHuVC8OTMvr-aleHeQaW1SVaKa-7obVdKe8TpzPYpWNzdxSEg6EClrDn4C3FpO0ymnDRvqsONG2rns55ZNaB1adEXe65Y_WRC7TYulFvi497AjBPip6rHmjM30XT8N-r3aYl26FVe8QR6f-NQMxVNPknoo57TyiO9PsjwaGB6eYrGmOggso5R-0jZAqs89YrkpMZW4Z3SVPCKCIqKsVL6Tf3A0i6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=nhocHYsNgO1IUFE4JxadrDrTwJEeenhtZZNm4qJ1k6e2GchmG8yKoiVx-yMNCzghWa6RwOSC0KSnFkK04H3ixS28C5KdZzKma8OqmCl2p75UU_eG6RlHzGhpRKHuVC8OTMvr-aleHeQaW1SVaKa-7obVdKe8TpzPYpWNzdxSEg6EClrDn4C3FpO0ymnDRvqsONG2rns55ZNaB1adEXe65Y_WRC7TYulFvi497AjBPip6rHmjM30XT8N-r3aYl26FVe8QR6f-NQMxVNPknoo57TyiO9PsjwaGB6eYrGmOggso5R-0jZAqs89YrkpMZW4Z3SVPCKCIqKsVL6Tf3A0i6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگزت وزیر جنگ آمریکا از ضرورت
برخورد با جمهوری اسلامی میگه
ونس، وزیر خارجه با ناراحتی به او نگاه میکنه.
(ونس طرفدار گفتگو است)</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6311" target="_blank">📅 08:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vJJLd0lF6D3mdTPwOqW6GbAxZfMW0QdXxISSI9UiLoOyKmDtrpafLYcUnF1YBWO-CFd9MCYGAOpG_dDFCsG3j37ZNkYl-IabTbvc70sMe0t4kWGsLzDLDyrxuG62bgNJNT9oNWruBT4cUxprtaUyZyYNIVw0wxfzauIUxsQsKx-NTg5SRVHQo434gupNXGJiE5jpf1SASiIs-VgUApCoNnzv3zdkkmyUYvB6sUDtxTR36xpHelQGofjsG9Ug7a03DgFw19TEkrMt0Sm5L2TBkksPP15cLpkA6FBFqffKAzlG-eJ3enYjXCiOPyzBC0wDehLqP8o11H16WS7ZI4xXDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اندی برنهام نخست وزیر تازه بریتانیا که از دیروز در این کشور قدرت گرفت، با در اختیار گذاشتن پایگاه‌های بریتانیا به آمریکا برای حمله به جمهوری اسلامی موافقت کرد.
پایگاه‌های «دیه‌گو گارسیا » و «قبرس» از مهم‌ترین پایگاه‌های بریتانیا و مشرف به ایران است.</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6310" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OZuX_pUu6mHI9EihHbczaXtmEVBY6NzwE8Em5p2bTVR0-vOAyXuUGgnYzevYNHaSBGXKgSNOhfnqNmO3jxZEhYlSUVp8B536U1O9yLQdneXigdUJoY5iJoz6w3hJYkKVdqcZHdx37g4c_sOv28RhEyqA5I9eF6MAE1-8CR-M0Z8bKxsxrYGQs8XF73bKsRd7rq7VsJs8S-mF3A9jDrM1eAm64AlAQWK_zrfczuzKRyfdfxjZjkcvEofiziP74QOH5YaHq3uD0L2EvJWPVODO8tpj2dG9mswxCqzQJF2Pr0O-yjedqyZX13Xra-HQg_HYKrU-pfIiTaJ9Rm8tG-jp5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rRts_Ky_WXQymeMur04afa3_65FuAA8Cro5rAQiHs1Ob2X7OeWGuOViYHuHU15cC77WRs3htkjtXs0asuT2H8D8zE5KIrFADxYp_DWlFuvQSbjwpAk7C4M--LlzpGvRW90mXa3VFaQFRNCm7jPZedgZ8JE92Xm1pU8HhDRo7UTdwHLZdFENWRWPKEqBVW8Blt-W7saSsAnS5HJM6hn9ar1vzFx4KzmbkVHtgB5IR3Jpbj00P9CzPF1kBZyRV_d7HPqwTAuqPW9ZSmbHRFLdkNlFK3i65qealrVE6JMk3yEU0V_tW-ys1VSlhNpbFURFXmkae2fkZCu56s08LDzix1w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسن روحانی رفته خونه لاریجانی تسلیت
چهره زنان رو!
بعد همین ها میگن اگه ما نبودیم داعش می‌اومد توی ایران
داعش ۴۷ ساله که در ایران حکومت میکنه.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6308" target="_blank">📅 23:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6307">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
گزارش کانال ۱۴ اسرائیل :
جمهوری اسلامی به سفارت اسرائیل در بحرین حمله کرد.</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6307" target="_blank">📅 22:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6306">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RuVPOu9lirUFiqctTxW-IYOwQdD3yBWBFHFSpOuJA40IDTYGwh3K6oQMGn-YDFAe2uQhYN7WjVTaqRXzMIS9ENnIA4lijidSBBKLLKaZ4QVcv722_dYKepALlL1BBy1CRUrJGnXv_JTQSyQXMy8ByG-u4XNTxHvCJuiPrA9_JH5C7VZZcoSVl461f2UtLANgtiFHV7VL6LDgn_HQVFQLK35-74OnVTf0qQno584jKhpEeOhwcSfFTE4QvuZ-f_gjSYVMIxovSypzzSr2JhWvTPcCZT34_z69I_Qfpp4snegdTl84JLnI5HP241iwH6Yy2a6VQA_jBQQMhYK2v_L24g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موقعیت کوه کلنگ، در نزدیک تاسیسات هسته‌ای نظنز، گفته می‌شود تونل‌های بسیار گسترده و وسیعی از چند سال پیش زیر لایه‌ای ۱۴۰ متری
از سنگهای سخت ساخته شده است
و پس از جنگ ۱۲ روزه،
هزاران سانتریفیوژ به این تونل‌ها منتقل شده.
گفته می‌شود اورانیوم غنی شده ۶۰ درصدی ج‌ا
در زیر این کوه پنهان شده است.
بازرسان آژانس بین‌المللی انرژی اتمی هرگز موفق به بازدید از این مکان نشده‌اند.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6306" target="_blank">📅 19:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6305">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=oYZNdtoqZ7QvXW8KouIdjusuSHWClG_fYF_x_IzLtnTB7xmGm6eJrE7nv-YJPm7AsjLPzNGOcdlISxb2lGeYsO-L6p4OwhrdIDXFWLw__sDQnYIUi2umJTh06IvACMoPh9LmKIbOrqyOu0cQyjUT-zuc4xYR_yMvd9A6EU_Se4GWHVeVmjlTt69nt1j08vfahy931KeQrpa-4cvbZ75VBLixcvU8CLukAC3dHhGh1hwnSm5sZXfO3DI1bzWQdUis4jQqDUXrjwrn2aCbgDRDVeG70Wl7YTR9vPSRJOxxhfv9S0z3f7BqsFpUXu3dFCgf8G8U5BjGTb6fGsJjRqnyeIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=oYZNdtoqZ7QvXW8KouIdjusuSHWClG_fYF_x_IzLtnTB7xmGm6eJrE7nv-YJPm7AsjLPzNGOcdlISxb2lGeYsO-L6p4OwhrdIDXFWLw__sDQnYIUi2umJTh06IvACMoPh9LmKIbOrqyOu0cQyjUT-zuc4xYR_yMvd9A6EU_Se4GWHVeVmjlTt69nt1j08vfahy931KeQrpa-4cvbZ75VBLixcvU8CLukAC3dHhGh1hwnSm5sZXfO3DI1bzWQdUis4jQqDUXrjwrn2aCbgDRDVeG70Wl7YTR9vPSRJOxxhfv9S0z3f7BqsFpUXu3dFCgf8G8U5BjGTb6fGsJjRqnyeIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🚨
🚨
ترامپ: قطعا به زودی و با شدت زیاد به کوه کلنگ  در ایران حمله خواهیم کرد و هیچ کاری از دستشان برنمی‌آید.
‏ترامپ در دیدار با رئیس جمهور لبنان گفت: «ما قطعاً به سایت جدیدی که آنها در مورد آن صحبت می‌کنند (کوه کلنگ ) حمله خواهیم کرد.
آنها به دلیل سلاح‌های هسته‌ای در این وضعیت هستند و سعی در بازسازی یک سایت هسته‌ای دارند.
‏ما به آن سایت ضربه خواهیم زد. هر سایتی را که آنها حتی به سلاح‌های هسته‌ای فکر کنند، با قدرت بسیار بسیار زیادی خواهیم زد.
تا الان زیادی باهاشون راه اومدیم!»</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6305" target="_blank">📅 19:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6304">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=u0in7iegSYByv_x-cwrzi2jC-lQTVJg6GwnkBNqIOp5vldFUu5xNG9MH0U0B5Dy4v0FSR5Ig3Ir7gMA1YRw-RTmQdXVJcrRpN7kuScMCfgLcUxBrf-1Vkqa7cIUpgyjAHbxIkaWgLIuV6YzncOHRUCs1cnQx0nuWYYpLDdrxLXez_jRtjDsLaJ3KiYDCe-WKhn1sTALK3lRDiBTht9VVL-vhDBynagdM7hS5jitL3qtYUaSJD8bUyo_tL8HYWedmE5mxOEqQoJG8Jn3_cdjwblFKl-GjO0dqsNmMvGilNgvRe-AXlWSagI7PqCWryCcO73_gM5hCjkjlqpgctUpudA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=u0in7iegSYByv_x-cwrzi2jC-lQTVJg6GwnkBNqIOp5vldFUu5xNG9MH0U0B5Dy4v0FSR5Ig3Ir7gMA1YRw-RTmQdXVJcrRpN7kuScMCfgLcUxBrf-1Vkqa7cIUpgyjAHbxIkaWgLIuV6YzncOHRUCs1cnQx0nuWYYpLDdrxLXez_jRtjDsLaJ3KiYDCe-WKhn1sTALK3lRDiBTht9VVL-vhDBynagdM7hS5jitL3qtYUaSJD8bUyo_tL8HYWedmE5mxOEqQoJG8Jn3_cdjwblFKl-GjO0dqsNmMvGilNgvRe-AXlWSagI7PqCWryCcO73_gM5hCjkjlqpgctUpudA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
نخست وزیر اسپانیا : «در تهران، یک خامنه‌ای با یک خامنه‌ای دیگر که بدتر است جایگزین شده؛ چون مجتبی از پدرش خون‌ریزتر و دیکتاتورتر است و او واقعاً سلاح هسته‌ای می‌خواهد.»</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6304" target="_blank">📅 18:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6303">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=HZ4tSTrOlj2UmoC-ekPZBjzsXO30Wq7nwETqWZsKpaq-dnGl9_EpCJj2VyJvvlTqbyMuRFsMHLWNsHPaMxoApUZN2uNtVQvX2E09uPzMCU8JsKGZ39cBpKHZUL38MfXi5vZegDbp_feSg_TZEVbxTk_R0yyxzl7LQU_In-B3zW2IveJL65OfG7Ngj471KVnshRdnMmfaIUsbuooyVsItKZrnpKZjEwyXt0bYdbhQdymA7QXwOjjTn1Q-EGJ9qU2KJOqCzlVsI_bg2nGzJWXc_aEAX-HxHBZZxYdPxJUTfgYtxB7UiudfXwE2t865mmd2ZZlykIZmRlSlknaMvAsq8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=HZ4tSTrOlj2UmoC-ekPZBjzsXO30Wq7nwETqWZsKpaq-dnGl9_EpCJj2VyJvvlTqbyMuRFsMHLWNsHPaMxoApUZN2uNtVQvX2E09uPzMCU8JsKGZ39cBpKHZUL38MfXi5vZegDbp_feSg_TZEVbxTk_R0yyxzl7LQU_In-B3zW2IveJL65OfG7Ngj471KVnshRdnMmfaIUsbuooyVsItKZrnpKZjEwyXt0bYdbhQdymA7QXwOjjTn1Q-EGJ9qU2KJOqCzlVsI_bg2nGzJWXc_aEAX-HxHBZZxYdPxJUTfgYtxB7UiudfXwE2t865mmd2ZZlykIZmRlSlknaMvAsq8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسپانیا که این روزها دارند
پرچمش رو میچرخونن!
می‌خواستیم ۲.۵ میلیون دلار بهشون بدیم
برای اینکه با ما فوتبال بازی کنن، قبول نکردن!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6303" target="_blank">📅 18:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6302">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">در مصاحبه عراقچی
حرف از تونل‌های زیادی میشه
که سران حکومت به اونجاها پناه میبردن،
سایت‌های موشکی‌شون هم،
که همه در پناه تونل‌ها عمیق در دل کو‌ه‌هاست!
جمهوری اسلامی فقط برای سرانش
و برای موشک‌هاش، پناهگاه ساخته!
ولی برای مردم حتی آژیر هم نمیکشد!
چه برسه به پناهگاه!
اینترنتشون رو هم‌ قطع کرد!
خامنه‌ای رو هم غافلگیر کردن و الا
مثل جنگ ۱۲ روزه که تا دو هفته بعدش
به «کمین ‌گاه» رفته بود، به مخفی‌گاهش میرفت.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6302" target="_blank">📅 16:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6301">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DXZLZm08Q3QgL1IEPSh5rzWLBUq6OF_JuTT7GbIKvMGatiS7Ux9z06exg5vJEZaAP_qAGdD2SurLrQPbFU-Cg90TRh893yqvidCrSo0OnUIhxyz-mwsvOmUCjnv_kuFLJmY8kCPlEAtiL7bwPuGZL5-phC9PbxJETqdOTdfZ8xdnBNj48AFezh7azz3LzF15PHxtmN_9LjxcC6HHgyWLzf9SdrKooXLgDa9PT9x-H8LpXTtJXlx2ynPNtPPxMXoDioz39DC9NdrZ6MHc2BE4sqWByPVMSdHp1z1n3SFVgZlvUG7xG25RQE4uZR3JchvVLm5ExZz-C26mwyqgZpny_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با بازنشر تصویر گل‌محمد محمدی ۲۳ ساله، که امروز به دست جمهوری اسلامی اعدام شد:
«جدیدترین قربانی از اون ۵۲ هزار نفر  معترض کشته شده.
وحشی‌ها!
کی قراره دمکراسی‌ها بیدار بشن؟ (نسبت به جنایات ج‌ا) »</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6301" target="_blank">📅 16:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6300">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46c8806804.mp4?token=SktgoaINSiNUeIuu0Bfhph14zJ2EZSO8O-gZ5GZHH8A5hDtzOJ_wAiLHsV_lx5p0fTnUw2sNU1rliCkG-2hki3uUo4i8qLw-GqSF67KTjlFPCUxIol2fwSnGu_C0eHRFt4WH-K_zR6VJhb8bDVLseP6jlqlrKlZoVRiJNNknKijICR0wNxVmqs4mE3anHlo-VW4-1TuPJ6DLk0GnFC96RIfY6UGnarxsLL-hRDZeNpPuV6vREhOdkJXD6vmBCURzfJ4olCmXGPKyoPhpJU0R-ckDzNf5MxiP2WBUYyTcV8dcOP_uoeaO9QxZMEFktRZS3dixAthsHsL7kxvGfLCvAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c8806804.mp4?token=SktgoaINSiNUeIuu0Bfhph14zJ2EZSO8O-gZ5GZHH8A5hDtzOJ_wAiLHsV_lx5p0fTnUw2sNU1rliCkG-2hki3uUo4i8qLw-GqSF67KTjlFPCUxIol2fwSnGu_C0eHRFt4WH-K_zR6VJhb8bDVLseP6jlqlrKlZoVRiJNNknKijICR0wNxVmqs4mE3anHlo-VW4-1TuPJ6DLk0GnFC96RIfY6UGnarxsLL-hRDZeNpPuV6vREhOdkJXD6vmBCURzfJ4olCmXGPKyoPhpJU0R-ckDzNf5MxiP2WBUYyTcV8dcOP_uoeaO9QxZMEFktRZS3dixAthsHsL7kxvGfLCvAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خامنه‌ای: ما دنبال اقامهٔ حکم الهی هستیم! ما هستیم برای تحکیم دین خدا! برای رونق اقتصادی و… که دیگران هم می‌توانند انجام بدهند و در دنیا هم انجام می‌دهند!  بله! بقیهٔ دنیا دنبال ساخت کشورشان هستند، این‌ها برای تحکیم دین خدا!! پول و ثروت ایران برای این خرج…</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6300" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6299">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">‏رویترز: حوثی‌های یمن در ایمیلی به شرکت‌های کشتیرانی نسبت به بارگیری یا تخلیه بار در بنادر عربستان سعودی هشدار دادند.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6299" target="_blank">📅 14:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6298">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
جمهوری اسلامی امروز دست به حملات گسترده‌ای به قطر و بحرین زده.
علاوه بر این جمهوری اسلامی به دو کشتی یونانی در تنگه هرمز حمله کرده.
حمله به اردن هم ادامه داره.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6298" target="_blank">📅 13:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6297">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=A8JG-wzeAIQwQIEG7tb2fAiSMkR4Lc3nncfCCgZpyGPyThJNxp3J95U5ZpHuPAKSnBZxGBHrzRlhv08oxRvfkHMiKLrtZUjpJVPcRZ0qlOdUxcxOjU54FZZSx3FsTlV2Z5HUxe51hflx47fuyFD7c9b8YRAUyWDe3AE6pvQQM440m9deteFxVtOrX1Bt6G6wo4LSdwkgYA0CS02sX9aoZH6VLt5Uo06DPvWa0zcHi-HltCIO3UZSSOVEcJSq47s1SEm3ld8An-y9RAcZT7XVT_hfJ-8lrwErvVM14vwTQNcjHU2VYdCdVmmrsqT_blTa6G0K2yra0mfjxdx3eboNgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=A8JG-wzeAIQwQIEG7tb2fAiSMkR4Lc3nncfCCgZpyGPyThJNxp3J95U5ZpHuPAKSnBZxGBHrzRlhv08oxRvfkHMiKLrtZUjpJVPcRZ0qlOdUxcxOjU54FZZSx3FsTlV2Z5HUxe51hflx47fuyFD7c9b8YRAUyWDe3AE6pvQQM440m9deteFxVtOrX1Bt6G6wo4LSdwkgYA0CS02sX9aoZH6VLt5Uo06DPvWa0zcHi-HltCIO3UZSSOVEcJSq47s1SEm3ld8An-y9RAcZT7XVT_hfJ-8lrwErvVM14vwTQNcjHU2VYdCdVmmrsqT_blTa6G0K2yra0mfjxdx3eboNgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«آتش‌بس نظر مجتبی است؟ »
عراقچی طوری پاسخ میده
که گویی نمی‌دونه این نظر مجتبی بود
یا نبود! «ارتباط سخته»!
خودش هم میگه مجتبی رو هیچ وقت ندیده!
اصلا معلوم نیست زنده است یا کشته شده
برای همینه که نمی‌دونن نظرش چیه</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6297" target="_blank">📅 11:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6296">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=V7NlE-E0Sdh7iVDSplvtaxMjiI2ELZK3HewfWmS2APC2LRvZfT7V7QmD1r5y1ZbqZT2PvKz9OauIohIcF29AklQ9wWeWI-0Az5MEsMTuAWFpQN7WVOfgNHDKtFYcYWLyr7Tb0QMNdQXTp3IKWCywSGJk7J9rluJ2vQbcHZW-T70SGAzEgsv1h1ZnVRkff3SU-h5RHeNF39AyFmNGbTVAxwNOXQBt6XzdbvG6TDa2ajb4dl_Hdeh2TpKFVlaNblMExb8iCBMIWw8NqYrCe4Wfvs26IhStsE6wDI78qv7AqVu-7BRo-tuy0DOag9IamrsfGzhnQXJIUfOWxXQDwULFjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=V7NlE-E0Sdh7iVDSplvtaxMjiI2ELZK3HewfWmS2APC2LRvZfT7V7QmD1r5y1ZbqZT2PvKz9OauIohIcF29AklQ9wWeWI-0Az5MEsMTuAWFpQN7WVOfgNHDKtFYcYWLyr7Tb0QMNdQXTp3IKWCywSGJk7J9rluJ2vQbcHZW-T70SGAzEgsv1h1ZnVRkff3SU-h5RHeNF39AyFmNGbTVAxwNOXQBt6XzdbvG6TDa2ajb4dl_Hdeh2TpKFVlaNblMExb8iCBMIWw8NqYrCe4Wfvs26IhStsE6wDI78qv7AqVu-7BRo-tuy0DOag9IamrsfGzhnQXJIUfOWxXQDwULFjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد اکرمی نیا سخنگوی ارتش
‏به روشنی میگه اكر آمريكایی‌ها
بيان در جنوب ايران ما خاك خودمونو هدف قرار میدیم.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6296" target="_blank">📅 11:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6295">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=ibmAsjx82vAlMeezons48MkX439Zo4hqeByOtYpx_5LiI0PtkNuA6tG7oZSVLsp4CtZYzgNskz7nMunYvu1Mv3N9W49cot3eSYUipai7yr4VJ_UEOlEqyqzJ2PEBtH1YJk1-PrB7p8mVltjZJuRpgeY-TeLV44CHHqe7ckXTbFdtxo9doLvj_c1n9trGSMk8TwIyxv6shoGCtLPLsPDbN6e5pr2B2N8mKCpL-t3PCasQg5jIbQrI8SBAy7oYmhD_6vik55Gslfw0HRteNnRlzmDUw1zPDEsofqrLsf7QBz6Avp-46eCU35LydBgYYv38ZdKoYWFCAaoZq_GY5bl-LpBo4weyFGXZY0fd2yD4hSwHkfE5Q5E8lUOEaeG2WdRfR2do2BeaV1Bg7p4kBZG7IVSt-_5F8Lu_2o6TapePBScygeHJFZBWtnaWcaNkW3UvWANC3BqRoEZQVygEFbS73OsGKYpPTlVvF97qc74xhrcvmCIP-9KtKMXutx8XW9yPcdJ7mDtY87W4oHQepxLqH9W15al0qYDgQZM2fqHz8ckRAOh93daH_giHjzgFHEQA8nnRk9Wz8IMcmnsRSYEq65_8mSiONibtIN5Athm2Bb3Za3Sj5U5zkaIwdK8toi0DTxXGfTtyPZ1m7flq0n15_r8jowmt_9oDhLfPPQ-SkS8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=ibmAsjx82vAlMeezons48MkX439Zo4hqeByOtYpx_5LiI0PtkNuA6tG7oZSVLsp4CtZYzgNskz7nMunYvu1Mv3N9W49cot3eSYUipai7yr4VJ_UEOlEqyqzJ2PEBtH1YJk1-PrB7p8mVltjZJuRpgeY-TeLV44CHHqe7ckXTbFdtxo9doLvj_c1n9trGSMk8TwIyxv6shoGCtLPLsPDbN6e5pr2B2N8mKCpL-t3PCasQg5jIbQrI8SBAy7oYmhD_6vik55Gslfw0HRteNnRlzmDUw1zPDEsofqrLsf7QBz6Avp-46eCU35LydBgYYv38ZdKoYWFCAaoZq_GY5bl-LpBo4weyFGXZY0fd2yD4hSwHkfE5Q5E8lUOEaeG2WdRfR2do2BeaV1Bg7p4kBZG7IVSt-_5F8Lu_2o6TapePBScygeHJFZBWtnaWcaNkW3UvWANC3BqRoEZQVygEFbS73OsGKYpPTlVvF97qc74xhrcvmCIP-9KtKMXutx8XW9yPcdJ7mDtY87W4oHQepxLqH9W15al0qYDgQZM2fqHz8ckRAOh93daH_giHjzgFHEQA8nnRk9Wz8IMcmnsRSYEq65_8mSiONibtIN5Athm2Bb3Za3Sj5U5zkaIwdK8toi0DTxXGfTtyPZ1m7flq0n15_r8jowmt_9oDhLfPPQ-SkS8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به زیرساخت‌های فرانسه و منفجر کردن پل‌ها، قطارها و خطوط راه‌ آهن در جریان بمباران‌های متفقین برای آزادسازی فرانسه اشغالی از حکومت نازی‌ها، ۱۹۴۴
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6295" target="_blank">📅 09:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6294">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها @hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6294" target="_blank">📅 09:31 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6293">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=YcUyIAPbazI6D9S0VtMeV5kPu_ufnbacysxEa3f3nhIbZhrChbqMDaW_uzqRsaglVaTQ45P7ttL8qMa2udR3Ae_tvrGB_nWmGK7UBhKn9f7if1LyKi4o2hOTRnD91dzUBSOWfqmUKx0lEDoJby1HRZzp8LB1Yrfblqm0OoyWH5CCrwpZZCRo6OyK2YeBWMWFpmN0rZsN2cafq2l7p55bw1dKynssxFzd3YZ5xk0jDVm7Ezh6k9KCEnX6cEtqh-SCJjRo3ZeYX4sqqNPqtmUro-aIe6uvxJceluXo073zeofKBhqCc5Rfr5l8GuaPtA0Q6a_IQD5mAXLpaIeNnLwtiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=YcUyIAPbazI6D9S0VtMeV5kPu_ufnbacysxEa3f3nhIbZhrChbqMDaW_uzqRsaglVaTQ45P7ttL8qMa2udR3Ae_tvrGB_nWmGK7UBhKn9f7if1LyKi4o2hOTRnD91dzUBSOWfqmUKx0lEDoJby1HRZzp8LB1Yrfblqm0OoyWH5CCrwpZZCRo6OyK2YeBWMWFpmN0rZsN2cafq2l7p55bw1dKynssxFzd3YZ5xk0jDVm7Ezh6k9KCEnX6cEtqh-SCJjRo3ZeYX4sqqNPqtmUro-aIe6uvxJceluXo073zeofKBhqCc5Rfr5l8GuaPtA0Q6a_IQD5mAXLpaIeNnLwtiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6293" target="_blank">📅 09:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6292">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=GYEayNFhbR_H0-PoM3JDo8neYPwxC7oPjtkoHbm7dCrK8wt0PLwuumXSWtB4VybenEhfWCS8hLe3kkl9Utw4SMoMIm-savzxlmKBYyXJihnlVxRj4Xjd-xc6y7Mpzzp1SJeRe0WQ95A5bEU6OPCxUqA1FO4josLcRiH6hJ7pOVTcOy9w0OQiWjzxfJiMro54qbZD6RYV78ptziXy8DySF4Bwjd2tfI7YaT0KpRupD0ZIhlYUdM2B_fod1F3aRPNwX6s7xZaPOfwhJiU_yeqHhvYoV5uE9U-makvr3eF4GqoneFOlJO6jixX2Aco2cV_34v8hpzHjW3VSSPCIndjjpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=GYEayNFhbR_H0-PoM3JDo8neYPwxC7oPjtkoHbm7dCrK8wt0PLwuumXSWtB4VybenEhfWCS8hLe3kkl9Utw4SMoMIm-savzxlmKBYyXJihnlVxRj4Xjd-xc6y7Mpzzp1SJeRe0WQ95A5bEU6OPCxUqA1FO4josLcRiH6hJ7pOVTcOy9w0OQiWjzxfJiMro54qbZD6RYV78ptziXy8DySF4Bwjd2tfI7YaT0KpRupD0ZIhlYUdM2B_fod1F3aRPNwX6s7xZaPOfwhJiU_yeqHhvYoV5uE9U-makvr3eF4GqoneFOlJO6jixX2Aco2cV_34v8hpzHjW3VSSPCIndjjpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.  او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6292" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AOMchfkw5GjOghcZByxartK4h3Bh-3759hZ62kfODizFvStM7JGc8QLfvtg3zV3to04b8HlEa2KkQceytJVWHcO28EZuu1XkGAwd1huAjqFcJaLhrEfJMaIIetSjVnhNb7LwSyQnZq6y8MrIZ2nr9EMEZuF3gKE9OGtXPGhciZcuuEEwPAYPTOcEnPHuu3FSR1QWboDgwKd1lCN1VlafzCrd_zdxITJoQdFoCybW1pfNx45XVdLJlUKdMpCrtZlnMwXXPGOSfjsa0VBdCkZ0Ir71ZLOtTUfOXfrnTANH3LP9WiBTaWgm-2eYafcLXO7MO6-HavCu7CrGeDqE2pv1UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.
او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی جز فاجعه برای غزه نداشت!
تصویری از خلیل الحلیه، رهبر جدید حماس با خامنه‌ای. هم خامنه‌ای و هم یحیی سنوار توسط اسرائیل حذف شدند.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6290" target="_blank">📅 09:12 · 30 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
