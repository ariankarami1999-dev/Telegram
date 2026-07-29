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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-07 11:32:26</div>
<hr>

<div class="tg-post" id="msg-6403">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/farahmand_alipour/6403" target="_blank">📅 11:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6402">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=edI5JjcBNI8rcSCXsj3snl3tO-j3GuiCFujTxfhw1-C5Tw4H-X9p22CMfNjyZp0dRocizdpJCgZX9KQhVm3egB6ApG9PNERLFqFO_VSke77YTUNebJvHE0vVAdEICnPhEWr7ilHpapIzLfbh51Sqs1ARoyCfErPSezQiBgBBqWwgNb6XZ2PXoBrPZCvvtiUQxz-eITRSlIsUM3qpRk_0P6z11q64oXeA3rRL3Fv0c7FR91nsRuoB8Ivx__WpZsnvhzvxkvX22neS3T6gS6VH1GSRAAkrhA8MltVyn4vJYUx8pRNpeCoalF3xBaHeJXvSozefcc_KFyD2oLOTVXfOzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=edI5JjcBNI8rcSCXsj3snl3tO-j3GuiCFujTxfhw1-C5Tw4H-X9p22CMfNjyZp0dRocizdpJCgZX9KQhVm3egB6ApG9PNERLFqFO_VSke77YTUNebJvHE0vVAdEICnPhEWr7ilHpapIzLfbh51Sqs1ARoyCfErPSezQiBgBBqWwgNb6XZ2PXoBrPZCvvtiUQxz-eITRSlIsUM3qpRk_0P6z11q64oXeA3rRL3Fv0c7FR91nsRuoB8Ivx__WpZsnvhzvxkvX22neS3T6gS6VH1GSRAAkrhA8MltVyn4vJYUx8pRNpeCoalF3xBaHeJXvSozefcc_KFyD2oLOTVXfOzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب چرا همون موقع نیومدید از تفاهم نامه دفاع کنید؟  این تجمعات شبانه دست کیه که هم دولت و وزیرخارجه ازش  ناراحته و گلایه داره و هم سپاه!!   کی بهشون یاد میداد که بگن «بزن» «بزن»؟  کی موشک میزد به ۳ تا کشتی در روز و توی خبرگزاری خودش (فارس و تسنیم)  می‌نوشت…</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/farahmand_alipour/6402" target="_blank">📅 11:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6401">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/farahmand_alipour/6401" target="_blank">📅 11:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6400">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
سپاه ساعاتی پیش از هدف قرار دادن سه کشتی که قصد عبور از تنگه هرمز را داشتند خبر داد.
همزمان با سفر نتانیاهو به آمریکا
هر روز دارند به کشتی‌ها حمله می‌کنن ولی به اوکراین میگن حمله به کشتی‌ها خلاف موازین بین‌الملل و  حقوق دریاها و آزادی کشتیرانی و … است!</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farahmand_alipour/6400" target="_blank">📅 09:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6399">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g2jvxndXuOlDQ90AS4zSGOMX9a898jsjr8sv3dRWPhb-jHNTbppzu0wHR2u3nPPCIa2kQ13MAftcNDA5C15hlyvmWitzWY-eu5RHfFcUgM_-OrcUBVGu6QTlicHiP_ZXgZJMYGhUO4IdyB-X7PjZf2faOOJ1FEd4fJObt5xlo9hhALXC2yyvhJfUD0ik4VSFoGM8J2UDoggZ4X4qVj_UlnIDP40Y94GFlWbt62bme7hvhZEq2JH_LbPiEt2y3krTRG5u7epc2cfL3tmq3QG-7bxrQhJo7ubGcsZJqj7U2_MeDTL9sHbZXsumbwdRCtc53QSWFFSSzrXOpRVrO3-ULA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها دائم میگن اگه جنگ زمینی بشه دیگه قطعا ما پیروزیم!  این تصویری از عراقه و نیروی قدرتمند زمینی ارتش عراق!  نیروی زمینی که پشتیبانی هوایی نداشته باشه وضعش این میشه!  فکر میکنن سرباز آمریکایی قراره مستقیما  بیاد با سربازان ایرانی بجنگه. بالای سر اون سرباز…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farahmand_alipour/6399" target="_blank">📅 08:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6398">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9aPxx-ivjmeebdwMhUPzMmBWJpkYla_Xuv6QeLWSjWSFrJE7Fwmjw9I5b1cjQ6sjBTkwoFBS5FtEj6_pHYjXXpBxX95jsrcHb1EWMdeTRcEQTkv7X9t7n0eYDRxyV1ngsecIv1Dnf9RSFCG8wU9lG4BXqRLFAJ2PEoBxp5b_sU53LzjLuR6JdV_5673tscO_RQJgqGMd-VktOu8ZCvziRkGq9tDjcsXMr6u7CdIcoenWluSpdFHKQaG--jG4mCcaRrg86CuTCz2N0XfXniMAL96cKLLPt71EgktRMnFBo3zt2VrDMhap-XfekVCdHTPvNEppxJyg0hI-rMmGSjTlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱- جنگ زمینی چیز بدی نیست! ۲- اینکه جزایر رو بگیرن،  اتفاقی نمی‌افته! جزایر خودمون  رو میزنیم و بعد پس میگیریم!   اینها قبلش میگفتن آمریکا جرات حمله به ج‌ا رو نداره! امروز میگن، حالا جزایر رو بگیره هم مهم نیست! قدم به قدم!</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/6398" target="_blank">📅 08:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6397">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">۱- جنگ زمینی چیز بدی نیست!
۲- اینکه جزایر رو بگیرن،
اتفاقی نمی‌افته! جزایر خودمون
رو میزنیم و بعد پس میگیریم!
اینها قبلش میگفتن آمریکا جرات حمله به ج‌ا رو نداره! امروز میگن، حالا جزایر رو بگیره هم مهم نیست! قدم به قدم!</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/6397" target="_blank">📅 08:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6396">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TtxaaGa2NHgdANT6h6NVASJI_uCrr1X6OkpWbWA_CK2TIviPIeIQi9MYYFHKuUsTXjpvk_aw3gIi3rLa0ff6Y0NNlI3wHEBrzWoHd3UsB56U2f2lp3fCxKlG4YqQCDPar43PzAd97dUIEZo68MhH8gdcYmSbef6POekZynlaY_8dhhEP_sIAPFMahunBSlhAKjFzFg4SDajTLxbimArdzwLWd5mmG3oJCoGoUd8MAgnMXjch9bVJiJH7xW_i80VfxW_1C9qg-i3j1JMo4aGqclXhmzcwLz8dGYsAnUuY8-UD_JGqKcdIBMIbgkLT2IvK2K8l3JfYr7Vmm9ped5j-HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۱۵۰ میلیون دلار
هم براش هزینه کردن</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6396" target="_blank">📅 21:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6392">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YDyfFjTye7nEyMKk_CTVYaigurmUBdJjjq25DtfPE9NSbgCmj3Mctf2Cx-ExX1liX1ZKNZvEDaRerfTiaLg3o9htunliWUtKSM0-FLKk4q2BsaQfPA_ZrYz4Gr5T2fZDqXf61zJumnnWWv_dIPxdQCpD4GSD-kok-n2Ad1vnBexqc7mB5DLlM45MdpTDeCLqWF5aYx_7E-mSpY6SG12qy4oc7xj1fkZyHB8IKWm7xpu1nBBbKBObX2zWcYHU9B1S3zLqwPXzbIvvAfd2FtuPmNyHLFsSmfDnqv9GJfcrYmOU89E6arkeWWbkowcCrMIwlAaZnBe32z1SJEgK8PIJHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tq4FFCiSrLHABNGk-4kB30QMBZ-uszNP8idHLG2880AavKf_iydTe9v5LrH-7aMXbtUsTinNvvT-IHgIhyHOpyxsbgVcwhI9RyF6VU0DBDMqzjBzTc7OXXJYNWme_-mXideRLGGdBusb9wjnbOaLJ0NEtUjDNBLQux55aps9rr7ca4UbGUMyyzKRasT_nBpRh1plOy7Q6ZbomlpzlPy8r1GKVc-JXS6zL985Q1mOQgUgK_loHpcP86zA_VFn2DrWpgFbtqR2Q-Csc1kElIFi9z7NKWsARexoOOpqe0RpUlRNkBwUZ4qYwN7QsSQ5KCgfXP2ap70spGmpr8g5PLqO3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PTQhEZCUZ4qWZcT0th3x3TDgLdupWpnF63h9KEvI-llq1J0B2FLubTq7cHBD65DjpuWHZsTE3WadJg86WRU_R6Eny64I8tuMPJnpKewW5MEXp7Rm4241HiSjci8_k19RMY4vJqD_GIqYr3630gEn2dQtV0TKv75nULaPuHHSOrf5eU5-tVP-7QwQ7jaAsA0NjUplR6gULfuqLkT-YdfS50N0kPq6E3F9Zxy1i1mWeuEDspN_uJAwijN7xM5BF5-RokNzKzntgK7PwLDN2mjTC4dEDJ4zr8T0eDbYgoGgitoT5Lc0ELGJ9IE7OngdfSPKBVAUfn7oZ_kgWnUrge5sVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JwipT02uG6P8hl5vwe9yOk0IBbKqvGpT7zRYYGaHm6V2pYh1SJ7DoFG4X_sn2b_zFinp3KCWjWtQI3OfbDEd3zrJWj7JwpxQMvrIUGa5xQemRKYKJgq4VuBEyMM7WEkWpLDXnhXGAgP0pgHV4cpXqZvkX0DWFWkhiW0aHcB9MIAH1528tsvWh6MQUtvXhpQTYDiNK401IyeCr4grpQEL-25FB82ay-N6djXNfuS4Ny6bZirRRGpyPF3jJ7ri-Jw4gv0zH-V8Z96T_v9IkSuHOagbOeGjBRvtUmuTnl5qB4e0tCeyauqoUEtyKSK6O7BTtxenoj18bWrPe8zJyzd-gQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویری از ویرانی فرودگاه بوشهر
از این هواپیمای مسافربری تنها دم آن باقی مانده.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6392" target="_blank">📅 19:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6390">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6390" target="_blank">📅 15:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6389">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">مراسم خاکسپاری مهدی توکلی، مدیر خانه عکاسان کُردستان، خواهرش سمیه توکلی، روان‌شناس، و مادرشان مریم اصلانی برگزار شد. این سه نفر شامگاه چهارم مرداد در پی تیراندازی نیروهای سپاه پاسداران به خودروی حامل آن‌ها در جاده بانه–مریوان جان باختند. نیروهای سپاه پاسداران…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6389" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6388">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIranwire</strong></div>
<div class="tg-text">مراسم خاکسپاری مهدی توکلی، مدیر خانه عکاسان کُردستان، خواهرش سمیه توکلی، روان‌شناس، و مادرشان مریم اصلانی برگزار شد. این سه نفر شامگاه چهارم مرداد در پی تیراندازی نیروهای سپاه پاسداران به خودروی حامل آن‌ها در جاده بانه–مریوان جان باختند.
نیروهای سپاه پاسداران بدون اخطار یا دستور ایست به سوی خودروی این خانواده شلیک کردند.همچنین پس از این واقعه، از خانواده قربانیان خواسته شده علت جان‌باختن آن‌ها «تصادف» اعلام شود، اما خانواده تاکنون از پذیرش این درخواست خودداری کرده‌اند.
@Farsi_Iranwire</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6388" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6387">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cMODDd1cMvrMyM_Pe21cIuFswf_eBb4wqYMsEReKs9Ui-zaKSrEg77gLXnc9Rvkzvog4QJVKlaDE-4ARIFaKZUSk8fpV5PiV0Z49cibKNp9OCFgovyBe8gLT7THx1jc6cdMtLObzCQrPV44Cd0K-mBBu3GvnkW1FWQHIajEaiHeb3EIoGeGyMpiSCjPdniHGE0ft4jZuIuH4zZgpXVcYkDa6ApJoKavfELLRJUZ7dcpxREm5VtqyCjSa9TtjNaiT7sHwuBZMFqu3SQnFTw07agKzUFm-eSMx3Wik47a_5NYGQtnycqB9ymyMleJh6D4n25ZeomhgYBjDRQN4bEPILg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باید آن قدر آن‌ها را زد تا پدرشان را درآورد.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6387" target="_blank">📅 11:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6386">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‏روایت اردشیر زاهدی از درگذشت محمدرضا شاه</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6386" target="_blank">📅 10:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6385">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LAvAYgamA9BFS3pY48LtvLsHEabPREd6axNebhy3q65VSv7_0ngkU3HAbiAH2PvITBr8PlUuIBL0JBS5syQQu_DbmMn3nzU3GGYCa_w_tiaER6UEJeY0LH-V1S64IkoGvFiDc0y-tEZDxsTDD0NsG9vUC1AEkzxVGw1rlvpPw9txMKuw5yr97i47Vs_qOEIUQYHHGt_jBqfaz5IzS853o2HXTVb77AZ5wnmFXkppxHSGTNrE80qm9sG5Dwd4IvhJMga8yGZEWH-e8HSYyqusQzRVO29rm09v8mWLPS4HhHRXUT55MTJpai79kSNt6BrlQALcHYRtz1DcsHenEz5TOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لعنت به ترامپ که ۶ ماه بیشتر بهش فرصت داد! تا یکی از اقداماتش،
و حاصل دو روز بیشتر عمرش، قتل عام دیماه باشه.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6385" target="_blank">📅 10:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6383">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6383" target="_blank">📅 08:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6382">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=omkuBje3klJEnX6kOcjSvHTgtzc4ls3NVBYwAB-f_Y3SB2ZtXiU9TSNSjHHQ_kLhSojilZxAf6pUuX7SJR6xOHGVCOB3-MJQV2lQvTnIbZAVxU61IwwZFuNPoL61ccFm8T8kLol45sdgKbyv54mXHKKr9CYsANKPVq_6g6i-wgxQCFRGMEZ1ErtiDzBWOJE1Bi0cXbowkQNL_NMZgmFnN2tjCwrLeVZrDWiP5QGPbPGjLx7oOFvFT8GFeEQJyKd-feZ1wPSee6UABijhseADblpRh5tdFlJzvEmVVrGSUN6PFnsW1EY0f8Y-XKpz9JNiUbAoNLO1-hcHadTORY-RaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=omkuBje3klJEnX6kOcjSvHTgtzc4ls3NVBYwAB-f_Y3SB2ZtXiU9TSNSjHHQ_kLhSojilZxAf6pUuX7SJR6xOHGVCOB3-MJQV2lQvTnIbZAVxU61IwwZFuNPoL61ccFm8T8kLol45sdgKbyv54mXHKKr9CYsANKPVq_6g6i-wgxQCFRGMEZ1ErtiDzBWOJE1Bi0cXbowkQNL_NMZgmFnN2tjCwrLeVZrDWiP5QGPbPGjLx7oOFvFT8GFeEQJyKd-feZ1wPSee6UABijhseADblpRh5tdFlJzvEmVVrGSUN6PFnsW1EY0f8Y-XKpz9JNiUbAoNLO1-hcHadTORY-RaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرزوهای خامنه‌ای : جوان‌های ما تا ۲۰ سال دیگه همه باید عربی بدانند.
https://x.com/farahmandalipur/status/2081803094522757301?s=46</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6382" target="_blank">📅 21:35 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6381">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">جاویدنام مجید پوررستمی - قرچک
۱۸ دیماه ۱۴۰۴
قلب آدم هزار پاره میشه</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6381" target="_blank">📅 21:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6380">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ترامپ به شبکه ۱۲ اسرائیل: «در حال انجام مذاکرات عمیق با ایران هستیم. اگر موفق نشوند، به اقدام نظامی قدرتمند بازخواهیم گشت.»</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6380" target="_blank">📅 18:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6379">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ed1a3118c.mp4?token=T4bL5JiHTGc631pDwhxFPf31iG-v-nIbYEO2YSMrUZVgX4pr8ynpRb1hpSggfzVXInNjim0R9zDF6CrVRv2D1k4kJyIiaCi5snbXPCTQHaj7IJ0-KQKcTS2XHx_KMtaf28Md5JCIPLPnSXheGLhh8aMZoXZoI5RHPdB24tKpj1roBvsBESTJlWA30jkp64KuvPu34KlGphBfCPUOYzRaouY4vw9BSS546OvH_0LEqoaTwrgsDUi-B514jzMFq0Ed0gaWs2o3NnmYusEBdP3nTGbM7kuXfUQuTqBCeccUdbFE9e9f0oIPBY2yc90JGUX0vaWc6EG4h33XNCnx2nnO_mG5mRKDF00-ms-PVRJ2vNKDJvxyEYsoQmkMVEb4vzyxpaR2_VabEDsRsucrkP2E2ii2zUJJJZgbuyZSFLdLSXEJfklPTXpUAHGj6AGGHTLsUW6ZZuX-zubAiR3Pk4cubgVQTfqaaNfK5s7aGhvPdTN0XnQBCJGDUxQJ8xsJduN3_Io2OML6bdT59WTVM06VEPKfkVsJPOQX08FAMf8vNYR-CCkzzZnOSH7_3CccWIjqUdSxH06hsOAI7yt-r7lHRnHdvf71nC9r43KZVul--Tmk4IL2oCbkuLpCvMeR32-kJdvyk7bOY6moZ0x_FP0DlUO4sMhdtwxT1zjMZnl0ri0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ed1a3118c.mp4?token=T4bL5JiHTGc631pDwhxFPf31iG-v-nIbYEO2YSMrUZVgX4pr8ynpRb1hpSggfzVXInNjim0R9zDF6CrVRv2D1k4kJyIiaCi5snbXPCTQHaj7IJ0-KQKcTS2XHx_KMtaf28Md5JCIPLPnSXheGLhh8aMZoXZoI5RHPdB24tKpj1roBvsBESTJlWA30jkp64KuvPu34KlGphBfCPUOYzRaouY4vw9BSS546OvH_0LEqoaTwrgsDUi-B514jzMFq0Ed0gaWs2o3NnmYusEBdP3nTGbM7kuXfUQuTqBCeccUdbFE9e9f0oIPBY2yc90JGUX0vaWc6EG4h33XNCnx2nnO_mG5mRKDF00-ms-PVRJ2vNKDJvxyEYsoQmkMVEb4vzyxpaR2_VabEDsRsucrkP2E2ii2zUJJJZgbuyZSFLdLSXEJfklPTXpUAHGj6AGGHTLsUW6ZZuX-zubAiR3Pk4cubgVQTfqaaNfK5s7aGhvPdTN0XnQBCJGDUxQJ8xsJduN3_Io2OML6bdT59WTVM06VEPKfkVsJPOQX08FAMf8vNYR-CCkzzZnOSH7_3CccWIjqUdSxH06hsOAI7yt-r7lHRnHdvf71nC9r43KZVul--Tmk4IL2oCbkuLpCvMeR32-kJdvyk7bOY6moZ0x_FP0DlUO4sMhdtwxT1zjMZnl0ri0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6379" target="_blank">📅 11:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6378">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oshdxFpi2elfzVSiycUDEvxP2SslOzkSmEoRyn5O7w4WTwchzw__BjSllvz5hqtJKksXxVs-pucJzrwJWTse6nKESQEqtzbcEbo7n-OrN6-jlHr_lzQc8aAbtGVTgkGKnTuBjHAxniQZK6lLGTWE15l-J8tZPFeOBXyGIxJNYIyTPqF5YH-6nzQ65Rewe8FPRsUPZOGyj2f9xAYIR2xekcjFuM826868ssY1wf-1W3ELqHN4cb3Wi1lHEvynnpc7Sk88JwCvE63sRSaoyZBqWQIlvk5m-2bVvINSwKyGZmmOAyaJB_I2Fvyi4qGq3W7kJ3v0KTNncFSJcA7BNzlwLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو راهی آمریکا شد</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6378" target="_blank">📅 10:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6377">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=PvgyYXBxBLgF6gLK1zrR-72avp41brD1KIDu0FhQ7yIIrRLjgRGK9YiS4J6av62zPA913vdoY-dqKHC-DSWPiO-wdgFssiWI8BjSr2KoRjdPYQMfZOPViOcqErorwndMl9fsCh72x5v2R0uI8ThcJVK6KcHnfSfwLKSsbDLAFrPGTaNUQEEMDKvMvJcmjOMljJwkVwOocoqHM6OdAVdAP9XZmdshDNH-Jhv9TWHeBMTbBm2Arqiy5TANzbQBuAXlK3B8SQ0mh6guBQ9qZ2T6tUbGrKE9JNGJvkvOrbpyRbTksFeS7Vl5LZNfUzlLYcZQq1-Z_HlN8NXmL1lRvtmwcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=PvgyYXBxBLgF6gLK1zrR-72avp41brD1KIDu0FhQ7yIIrRLjgRGK9YiS4J6av62zPA913vdoY-dqKHC-DSWPiO-wdgFssiWI8BjSr2KoRjdPYQMfZOPViOcqErorwndMl9fsCh72x5v2R0uI8ThcJVK6KcHnfSfwLKSsbDLAFrPGTaNUQEEMDKvMvJcmjOMljJwkVwOocoqHM6OdAVdAP9XZmdshDNH-Jhv9TWHeBMTbBm2Arqiy5TANzbQBuAXlK3B8SQ0mh6guBQ9qZ2T6tUbGrKE9JNGJvkvOrbpyRbTksFeS7Vl5LZNfUzlLYcZQq1-Z_HlN8NXmL1lRvtmwcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله یک پهپاد سپاه به یک کشتی در تنگه هرمز</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6377" target="_blank">📅 09:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6376">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U7RTJsCxPejHhjfsNrQcd_ykGHBdEvHXMLkDaw_x9hfi26_dmuqedWk2ZjL7YXKncidlBzH1Kdk3buzdrmJkAEwE549Jk3T-ngy34GeVL8IqHJq_GrtPltdPJE_n5B7rEhCCTPyluUKdgDgOYSl8MrmYjmSLcwQ7AdSmOKVY3YzxuH_v_s1yMORjqfz7rGdLwrjwf9XihfpMgAMEJYYTPa0NvxpEQ8p5Y3UkLO_ZIZoNJMCPlWWZNkmrixkeG8Qetfpe7R-H43mcTkJ4nxo8nrHe1F1t_Bz452Q5BysNvGzykclDu4BGLG2GLPKPjSpy5zNC7sZnGeheGjiP4y1ivw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«مسیر ناامن»
منظورشون آب‌های ساحلی عمانه
چون از مسیر ناامن میرن، با موشک بهشون میزنن :)</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6376" target="_blank">📅 08:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6375">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">۷۰ سال داستان دلار و تومان</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6375" target="_blank">📅 08:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6374">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AVYqDNmHt5wu_74ANKks5WPdroQn34AKr7Xk1wVNHejoow_E74v3FrYuzhs_yhUmT_99k37exAE0FyV4zoS-86MDXc_fnmtQyDtQ5q_c4bfsrwXoctVzubnm3DgQ_7SWOPhumMtxlmfzkTOjOr3cyCJ5gNwwj9yjFU5bdnrEfo6UeBUOjFnPmkM0O2AEQBby0qguSYBI3NX-VjJQKEZz_1LsSun0rX4yO25kgTG592c-64azP30sI2_YZjexlFd0fJMsNN2FL5YmyElerhemcxnSMmpti_Rtv_cxndmD4DdR7mV6Os5GW3eCGHrQqeifcfdksj1p5PftSIetgVCjxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشسته هی طرح میزنه و منتشر میکنه :)</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6374" target="_blank">📅 00:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6371">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l-EVbhKZVNoyzl_JpPpbqpjBDzL-fqNtSVPxO9gX7CVqpNUUCs64lfxIIMeRHs2SseYSQcK-bHkacvfYzXkDzN2gLOQjQ6x7nfRbZ1etltyzGQFkO-2z77kbI5JTCoNwdNGBz3rHDN3Au4WmQV0kBm39I5EBa9sXJZus4FzdmeePqWo3JG6WwOrKboYrNOoKl083Pum7roYPB4ogDbizIjViulPOV5vixF34hikctQ6ODOn2g9kJcpVbq75DAksAnJAUIfr5h3nSmEFuYAxssZpn4NudDHMSFNgGQbVppRkNWwdg0KcDq6g8DQCGfOi0avE-SfnV88rh0vMDiXGyPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W89GS_jFKATpgRlUixS0SnI7F4kYIuIoEEAdBO6AemfCZ84cwZeaXaHfwGLMMAgkmjDJE29Ab273rNRzC6F9z48sSm1yHlVmr6tMPHmCSoBdXsck2rWK-3WmuyS1PXSf7AO_RFaIhB8CLkhnPRRZecFFlIwqQNsKX2jVUwMxCb8aPqLhM3xdCyt3vdOMJ54f49LJu91FbmDmUumaE4ipNM3PH0ClEIhrwqhocuzW5SNBz8C3me7riYhFd1-MmiZccfivX-jsOehfsTatlLurqHPVZq7EU6QbPn610vit6DLwUxjTwH5ZwZVFNUiN0uKQ64SZz7zSFkV928GIvD9Qxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tyVRl6mPMxd6g-_GlmWQJAK47W9OBGR25QR0Fetuees4Ur-oS2fN3qHLhSnLMRsJpH9WLN_1qND3TKQeYCQdgziyLktcjpSCnQoTq0zyQtI9hXZTrL4GCR2hroQGTm1IFfdWNha4UK-G1YmI4m7LQ_dBq_4m6D_8pAdkOvzvwLbjeq8Mf0-WQ1DjFE2sqosD1M1x2zJ_9D1tvEGq1dp64bG8jdJLvVspdDRQeARTCYRSUvHA28acQmePybwQSBJyxT_nqyVi51tfQLwd4cWFbC0XlXoBw758m4tK0otnRgHjAQ4F_m-otn3__8EpDJ53XrVyzO4xv90HBGPStwxsbg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طرح‌هایی که ترامپ با هوش مصنوعی درست کرده :)
حمله به خارک و تصرف نفتکش و… رو :)</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6371" target="_blank">📅 23:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6370">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZnibUKu_wIA8qh9rJV62sWsRKAccrEetmEXbDmtqqvjlYSqQYmWxUgs20IPwxfSijyDx5Qfh1YVSUl5_4y4xLkikwtFEX7Ns8R7HipCg-ai-CwckzJPa0XilqJLJW7DYpGYjC68Qndz7VasCZ_Ui3mLAiKVTjAkq2R0dE0kmRrRyGANi8xVDazU8aLdPCLHlmwlZPai64ekSLSV2SDrhJk5mboPNwc-dL3fEVffLWFXz0GQSgcwGnrcrjqysJcXFYVVTuYWZ5yn6TbtA6JKmpt_3KqPP-mcP7O2Zzi8bQFt30uYqSSf469R4uAID4L-8D378APb9vmHB_-Wk87xW5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه منتسب به مجتبی خامنه‌ای :
در برابر آمریکا و اسرائیل راهی
جز مقاومت نمانده.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6370" target="_blank">📅 21:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6366">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vdc8VmtquC-Chf_5sXq_OGCQ8oEUHArnZYb7wdwthqWYYQ4dzFtpOo2QDKLWKcRCMO1Z7NNfEdi-PnNsrkHwRqKyikj_Gizff-uzuRrp-mw4tLhRKnJwN0VacDErqRD3P1Tds5a2jh-K0F9j2hA5HWsRzoOoUktL6Yu6al7YIJkm51NbOsfgRCRqaNguDl6LWCJOqqhWSykN4BWhp0tQ3X7qi_YGCog-9ujODxIszRwLpCTkLaTKafi1ja39urYrVMqb3YGAYcoaBOp-OQ-KhXyGV6lkHdgY5INrin4Wdlz1-F28wh6wKjcGcS1OpXtxKV7yr5sonfG_IOPG653G0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l6jTc3UUp3th7xLUzAKF_XkDisa2p97sjXSPOPlfxyEuIdqHszhtqJdkUtB4rU-Csdta2M3PlE1JrpYeP3PCRk0Z2lUXpHu0C1ZlAvlOfZ3-P_bhEqQtMZY3-WqqE6Jm3IepakaQU04hdmWE1NaC0oqEQlL28NhMEpUC1aD9lkHcP-gs-bscWiYX567ieR6tueWH54M0wcRip9Q6tmh0PhM5gnkBI0TymHVVAhFmxY92-SmWx7VyP8HKmtcel6bqCWkncMh2Np-aqwlFrankPq_roB9Jw9Q7lIan71plz7Pru1cttCGN4Iro2nOFjpL7kxC0sE-2Se35xfoMwjaEKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y7VwMfKJySUPmxvnAXTmsP-OA1KhJan7Qg9LBIfC32jABlxuu1cCTqVONBWn_S_upZ9vXfkQAVsbtzNKIdKgKu1jZwskqkjGtc_Uuhxhwji3CzjMxOoo90MoBWv5fNcCXL1VygTrGY4VWcyy8DT73isesLLma9qNKncAvYAuxIVEWPbyFlt1KRjoR0uSJ1C5iCP9-QQKzGTEb7f4pfrppZ9lsABPSOSzM2ip_vT31MhOtxTzEiWfBC-qgc0yUx6Q6zqIZmXqWZBVroeYqcW7VaskhA3VArWWK1V3in3dwYL2Og65JkBj7MmTywR6_gEF673bbZegM3X07_theH9PPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZzaLxXypcuCQ_8CqGD_xttCWDZgQ9aw1cFNa9Rf-Afl0JeRFPFpCa8s6EzO5942olQD1BkEF9Qq3IluMEu9o9yyHvywmwlAzPj_UKeg1_YdpLDHy92obhbE0Ki-OAI9wRw-ig_Vxl7yGjbSElUbLsXmUjaN4oMGLUXOzlPegHF5zj8oV7mO2uEFmYiL-1j-zVTSdCUU_qF7OH3LAJE8rPuoNCwCCkFwOPUaRjPBPiQBx35j_SSOahP-XlK-6mHfD0MfBcKOJRNp1-evGSflDZxOaKaagYfTfzb7apOkQ9NMstdbVy9Z4wE9HedFbr-5RNF1CYDvSn7geADTL0NRnJA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جنگ اوکراین
تا دیروز افتخار میکردن
امروز نوبت انکاره</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6366" target="_blank">📅 20:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6365">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">۱۱ سال پیش
خامنه‌ای با غرور و تکبر از مسلح کردن غزه میگه و اینکه باید کرانه باختری رو هم مسلح کرد.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6365" target="_blank">📅 20:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6364">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ABgZrCmhxWgE8ciOftaTsRHHeFlmupAnCb2DxH6ujTuIRBDKt8rjvILGyO8zhL-c9m1t8wrxsRmzyHfGaZH5zPH6ag_1TiB6_h9XEmJQeVCJEVfU4bJNcWnMz_yI4KiHM3afz8WCarxVvGO1ZTCwhZ0bIl5ESKXfZBy4DrikS2rx8hYS1RaNHSNpRK61U9ZZa9ikthKZ1LcWJTEeFJXWnuX9MamVNwNb0sEdFtdUJNKqjmci93Q79RGYpe6sZqQL35wjszPIP68bFq_LKWARJsNRpl_RjHRJvpH1aX-Hygt0BdCuR0SCHmrt8wVK4ySgx1i5ZOBzz3W_mLXUzemmTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6364" target="_blank">📅 17:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6363">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RaqU8J_AoVEDJq2QOUwA9CHNMh0Scnx3UmVgqacVlOyGbvdeJfPvwKo5QqFq7kMYpfn7Xn4IyyIJbvCgS2JFO3kWS-KXW0BjZ01fEn_L0zJ9BzZ2PpkINyzLA3S_8g9q41tLXHuj3cPejHmB69eKmPV9yTGK9ZpcwjyzWP5onF00MjVkXK9WsK9mnebpuXqd8TFBn3-49p4LL6M7UaYhfXLZDLfDjmu3GyTw0GKopqtzh3sMHiVVdZhJPkgBycyrsdPDumYDvL-RZYAJZpfFKxgXw1FuWPJ717UfXkgUbwy28rJVRQkf6Tb9ratuAPIQawWI4xdpi_QfKGBunzLPgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های حکومتی از برخورد یک کشتی با مین در تنگه هرمز و وقوع انفجار خبر دادند.
مین گذاری توسط ج‌ا انجام شده بود.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6363" target="_blank">📅 16:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6361">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bxVVGVfcvPnvoS3GFSyAxd84phbdCBC0T91NVk-X7E1dz4dB8B8BnMnH93FCnykGFMlGnduXgfUq4lYYaCgR5bdRtsocyAOdLWORQMueSsG0ie3U3gihBB8yKFl3VxKKWzxQUXN_Qbe5RL_t-bma5ViUVwQzj8OP6BCANC22IcL8JNr2EgQ-a4D5pwmOe7pZzgNUCPJIKGMBLvq0Tm5QqwyRH_6lNazkQBJJNt-15cSRADTb8smvq8xHVNYUXy6VbPRZjpK1hauh0scbXvElT0ZYN51m7oTOUzTXkKofP9mvcGn3BrVGrRgSQ5apBHD5rBLrwHbnm3wW42e_1J_xiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jhsn3_A0tJF6o1EPZhyEhpX1i63sTKmq4iZQNUkL8BXNoqobHqbC3d2pOKEL3pANZuu4mLhZmAuUmZiKEY7KmlY8OK69A2VrDSSFHOTBLinWXkB39pDcewwTl4kAKZ8o6gLjxiwtJMH6E5d_q-Xan8_BhDy_NwssSc5l9c_NeWiAbsoaEpfWlJC9rS697Vj1Gl-2pVqOb35Q28nDTwmfzzK0RhzyHJ_aUS1oH8DvTFlalAeBESLQuRyJg_KWOf9OskiDU3hO5_sHXNudPuJLaqq6LtjK8ScKEbR9uNCHe5-ONO15dh6OQvfRxGg1dM-x7aZSHbiDCIIw3zu1DxnKYQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6361" target="_blank">📅 11:49 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6360">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">عراقچی در این بخش مصاحبه‌اش درست در خصوص آخرین روزهای منتهی به جنگ ۴۰ روزه صحبت میکنه. جنگ ۹ اسفند شروع شد و عراقچی از مذاکرات ۷ اسفند می‌گوید.
اینکه جمهوری اسلامی در مذاکرات به هیچ وجه کوتاه نیامد و آمریکا را به این یقین رساند که مذاکره نمی‌تواند گره منازعه هسته‌ای با جمهوری اسلامی را باز کند.
عراقچی به صراحت می‌گوید که چگونه جمهوری اسلامی تحت رهبری و افکار خامنه‌ای، جنگ را انتخاب کرد.
(با بی‌حاصل کردن گفتگوها و عدم انعطاف)
وقتی مجری به این نقطه می‌رسد که جمهوری اسلامی می‌توانست در مذاکرات، مانع جنگ شود (که می‌گوید باز ادامه میدادیم چند سال دیگر…) عراقچی می‌گوید : تصمیم گیری دست من و شما نیست.
این برنامه فتنه‌انگیز ۲۰ ساله هسته‌ای که هزینه ۲ هزار میلیارد دلاری بر ایران وارد کرد و حاصلش فقیرتر شدن مردم ایران بود، این سیاست ۴۷ ساله دشمنی با دنیا، این دشمنی کینه‌توزانه‌شان با مردم ایران، این جنگ‌ها را هم به ایران تحمیل  کرد، که عراقچی همین جا هم می‌گوید: مسئله ما زیرساخت و تاسیسات نیست!
«شکست در نابودی تاسیسات نیست!)</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6360" target="_blank">📅 10:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6359">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">پیام فرستاده برای «شیعیان» ایران
میگه اون روستای شیعی لبنانه که کاملا نابود شده،
اون یکی روستای مسیحی لبنانه،
که دست بهش نخورده! چون رفته متمدنانه داشتن.
این هم روستای اسرائیلی (یهودی) است
که با اینکه تحت حملات راکتی حزبالله بوده،
ولی داره زندگی‌اش رو‌ میکنه!
و میگه دست به اقدامات شامپانزه‌ گونه نزنید!
چون - مثل روستای شیعه لبنان - نابود میشید.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6359" target="_blank">📅 10:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6357">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XttbmbrIYnRiv_V_CnzJ-vasPKsvzfEFi8cs9LqkV-R0fAm3V4WOnmD4ctk22VUL-Nza13qGkE86aqQBF-EhmU70RiX4rK4EIO3Z7wXyqV6pSZAVrVopfLdLWR58mJojWbQzZVzgb_ojfILFCt7sva0gooJOiMtBDawOosFBC0K-cwN9E12QG05ZjFElH2TFH817HzphR_gQQ9HSsJ6TO80yOQMlDDespyylTmSTpMmR-4n9L88DNsDvhPtALtuqnAmYUAwkgQDPCx2jtqQLQI0BKkTZT5R18Q08BP0vK65txL87WrcWQDpu1lTvMWyLD92rLSKWZfRrbw2KzDst9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JCDzib7EXLhLOEBu3BtNYHofDdXY2wvwOoPvrZzaPLAu6dhJMkU0TilwjwKwOvcN_oPg473pvFNV3_9o_Segrd9wH1gdOnIRyaqo89SnkStsTHRwZ_l6IJkjB-eh8KBIZsUMaIewYtltKaxX5P1TG55Yc3waEcb6tDt8R8SGKDiVCiFSChi6TKVtXb7A0OfPIdVkL3qgy4MrdDWRDZVUCgjpW9jsbykM-YMaSORf-2FU49KN5L7ngqywhMi1z9Nl5Z9Pp3jJrXCi9SvXd3U1B4PUlbnpU1QbdZivikn2gWQ5ghXslhABH9vObYse4FYgHV4pexjS5-Kw7t5GERPAHg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این متن رو کامل بخونید.
در  بخش سوم می‌نویسه اصل این
بحران ۱۵ روز اخیر از اونجایی
بود که کشتی‌ها از سمت عمان عبور کردن و جمهوری اسلامی حمله کرد به کشتی‌ها
موردی که ۲-۳ روز پیش کامل توضیح دادم.
جنگ رو ج‌ا شروع کرده و دارند زور میگن به عمان
بخش ۵ هم بسیار مهمه، در خصوص کوه کلنگ، ج‌ا در عمق این کوهِ سنگ، غنی سازی میکنه که حتی با یک بمب اتم تاکتیکی هم نمیشه نابودش کرد! و چون خیالش راحت شده از اینکه غنی سازی‌اش متوقف نخواهد شد داره رو تنگه هرمز هم فشار میاره. اگه امریکا بخواد برنامه هسته‌ای ج‌ا رو جمع کنند، باید هزینه زیادی بده (جنگی بسیار بزرگ)</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6357" target="_blank">📅 10:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6356">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ثابتی میگه تنگه هرمز رو بگیریم‌ (که بخشی اش متعلق به عمانه) بعد بقیه کشورها از جمله عربستان رو هم مجبور کنیم از همین تنگه عبور کنه و اجبارا به ما پول بده.
(عربستان سواحل دریای سرخ رو هم داره و بدون نیاز به تنگه هرمز می‌تونه نفتش رو صادر کنه، ثابتی میگه:
۱- تنگه رو بگیریم
۲- عربستان رو مجبور کنیم که از اون بنادرش استفاده نکنه، فقط از هرمز استفاده کنه و به ما پول بده)
شهریاری میگه خدا رحم کرد شماها قدرت آمریکا رو ندارید.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6356" target="_blank">📅 00:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6355">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">‏وزارت خارجه جمهوری اسلامی اعلام کرد حمله اوکراین به یک شناور ایرانی در دریای خزر در بامداد شنبه، موجب انفجار کشتی و کشته شدن یک نفر و مجروح شدن یک نفر دیگر شد.
‏همچنین این وزارتخانه افزود،  این اقدام اکراین میتواند آتش جنگ را شعله ورتر کند.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6355" target="_blank">📅 22:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6354">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">‏ترامپ در گفتگوی تلفنی با شبکه فرانسوی LCI:
‏«اگر از جمهوری اسلامی ۱۰۰ درصد آنچه را که می‌خواهیم دریافت نکنیم، قطعاً بازگشت کامل به درگیری‌های نظامی را مدنظر قرار خواهم داد.»</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6354" target="_blank">📅 22:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6353">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h5aEP8JQ16iIXtj3oVpei1-R4xP-2n_rUzOAUTl2yWq9KzGs6hL79OKk3yhzWjdxD638udNeBWvr4KswDt5ubByC5w6iwKdBGEDOdhSU67ufxqTnSF9yHNZGGlExui47TLB5xEEoNb49FEOJwXeEWrgyLpW_AMDZeNl8xPH0ksO7kG1C3eG18KIZAN2p0pBcp8YjyBPx3kA_0nYtFeCzpCYaA7g3uod08knHNSY8WzxrEPP1aBkrFWg31dkAy92d2aqnyqek2xYiNUv2VP-PHdFdirJUWiAIkAsDXHKD1JycVQ0PEZxeq9L00TyHJvHLCa0-_CmD6wccYNbGP9W7_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجابت دعای هر روز مردمه</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6353" target="_blank">📅 16:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6352">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">‏فرمانده سابق سپاه:
جمهوری اسلامی و انصارالله (حوثی‌ها)  دیگر وارد چرخه جنگ، آتش‌بس و مذاکره نمی‌شوند.
‏حسین کنعانی‌مقدم، از فرماندهان پیشین سپاه پاسداران، گفت که‌جمهوری اسلامی و انصارالله یمن دیگر وارد چرخه «جنگ، آتش‌بس و مذاکره» نخواهند شد و این الگو، به گفته او، کارایی خود را از دست داده است.
حوثی‌ها دقایقی پیش نیز اعلام کردند که به تاسیسات نفتی عربستان حمله کرده‌اند.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6352" target="_blank">📅 16:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6351">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=magmvAViSI8Q1KWV_uFsrVoVNQJLj0PLylGyX-wKwBuDZjCL5NUqbfA3QLnDS_roGL6fEH82wmD667HXbItnR67jPgRbgqmrEUvAvqA1f3EAM_5StTq8KUVXThn3OdrLtiobPPxAFtAnya6q7yyd-tjOdyDm4rbv9PB1llvOimsp-LVvlvTPsubxQAagMY5hmvvs1N-oXs0MdlBel-A9OmWwoJJHg7fD-4AdyMYvtfDNdEfju4wAcInEpxq4DWTa303MzmEFqOOuujDge47ry9IGDnM6yeTlzx1ij2IpqpzpMpK-LAHyLodii_sxtkk_VPxb7hbdF44Ukv_ofBAxSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=magmvAViSI8Q1KWV_uFsrVoVNQJLj0PLylGyX-wKwBuDZjCL5NUqbfA3QLnDS_roGL6fEH82wmD667HXbItnR67jPgRbgqmrEUvAvqA1f3EAM_5StTq8KUVXThn3OdrLtiobPPxAFtAnya6q7yyd-tjOdyDm4rbv9PB1llvOimsp-LVvlvTPsubxQAagMY5hmvvs1N-oXs0MdlBel-A9OmWwoJJHg7fD-4AdyMYvtfDNdEfju4wAcInEpxq4DWTa303MzmEFqOOuujDge47ry9IGDnM6yeTlzx1ij2IpqpzpMpK-LAHyLodii_sxtkk_VPxb7hbdF44Ukv_ofBAxSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حمله موشکی اوکراین به کشتی حامل محموله نظامی روسیه برای جمهوری اسلامی در دریای خزر
زلنسکی با انتشار این ویدئو  در توییتر (ایکس) نوشت که نیروهای این کشور در حملات دوربرد در دریای خزر، شناورهایی را که برای انتقال محموله‌های نظامی مرتبط با جمهوری اسلامی استفاده می‌شدند، همراه با یک ناو جنگی هدف قرار دادند.
«با حملات دوربرد در دریای خزر - از جمله کشتی‌های مورد استفاده در حمل محموله‌های نظامی مربوط به ایران و همچنین یک کشتی جنگی - به نتایج بسیار قوی دست یافتیم.»</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6351" target="_blank">📅 14:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6350">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pdoaiEGlRBcu-2cVINsn5btYnMQWhxeaWFDKhgKt0rB3oRZdQxl2gxaY9eZKLz40sUPAMyszzVx1N0brIMK_teQE4C4FklKdk-me4zEg1a0csYlglUaQ-zf73arzI-k95xMX95xbkjvouqotG2xp8MkkS_74T7avGFEqhnLmk7TZs6JlR51ObvQN5SOeDjbRMPL8fDq6aWtIDq-PBz2GDVTmOyoA9ovB8kg87UXzjDvs2kER6GSR5V-d-ThNBlvKTjB1SJW1TC0z60FH2ADleRoy0V46jp8UKw1pgRGTnUo-62hooMrELUQx3q1ITj4hceDRZRzC3souSOlsDPYGNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازرگان می‌گفت ما شب می‌شینیم با اعضای ارشد حزب جمهوری اسلامی مذاکره می‌کنیم، در نهایت به یک توافقی در خصوص سیاست خارجه و….. میرسیم فرداش می‌بینم  در «روزنامه جمهوری اسلامی» و صدا و سیما کلی به ما فحش داده که اینها خائن هستن و…..!  بهشون میگیم مگه ما این تصمیم…</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6350" target="_blank">📅 11:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JbwxfBNE6W-xVOvJAaHrpFBMTkJQW4SiztLana2x7XIhT6MggAL7uVjU6mNTjSfjxaRIWECGzDYmHJMtWRqcqWXrmImdBqkv4GbfEC7-tmuhVc0U4XxUj866CeygXVKUntpf0LVkphzNLYZIRFTKS5NcpZ4WuLLnhGvMhff8fVHRKJMHuIOET79XfElPbvtuCHR5xkTp6BzzkZ6wGJcpXwYA_2RSkzrRnHXMO-7GxiH8CN1ncGpcJwaPuqGxSgEqFy8u0vc1bNhT9xeMzGP1wBaNed1D7F9T2IaS_khvkjXtsaA0p6Y1L84Q-QtOcbkkl8g-R_k-QnuUJAnLl2Zd9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خمینی بعد از انقلاب سریعا بر دو چیز  اعمال کنترل انحصاری کرد!  یکی کلید زندان و در اختیار داشتن تازیانه و دوم: منبر و رسانه!  تا اینطور بتونه به راحتی صدای دیگران رو خفه کنه و روایت خودش از هر جریانی  رو جا بندازه، رقیب رو از حق‌ دفاع از خودش محروم کنه، مردم…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6349" target="_blank">📅 11:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6348">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J04wREcyi94O_oxL_1-mPFsepxQqz19jI3NwrayFf65DFGL7ocOX4ul3GWdee341sNnkEZZPo_Yignkq8rj95ft6NDFnuoXN9IMOBseVMBHVpT7wVkOMFnAiHZdnHvWXYn3f-UNGYwBcFTADv2q0BktdxEVmKrS6kjkD7wTshmD2-qnGDTDxqDslPlnWq1AaDYaqkvbYV6T8UmCjKUz7B-rolx27UkTk6NnWuzTE_FG4489HV7DxW7WeLpam9seCq-Hf3TnoOR-jbm55uRPFL2mcNk5fhagA6kHiljA7C4q2a95D2VJ551YWfjWLb_nq-Q59DjWGg3FDufuKAdxDCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو روز پیش صدا و سیما،  بخشی از سخنان پزشکیان رو سانسور کرد!  اونجایی که اشاره کرد که خامنه‌ای در نهایت  طرفدار مذاکره شد و کوتاه اومد!  وزیر خارجه‌اش ، عراقچی، اعتراض میکنه که صدا و سیما مطالبش رو درست پوشش نمیده! و میگه یک گروهی خط می‌دن به سخنرانان و مداحان…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6348" target="_blank">📅 11:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6347">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6347" target="_blank">📅 11:18 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6346">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=rnj4y1vtlLwbcbHvmbILjS9Tj_eq4WrOOC-7l0dJXfrzuMtVUC67gKB1thswcFbP5Bt72rbZpAJAgx_wKmk_HPvuG5Pkg8pI0mdkRFsIfJWBAY7eHzZaSVxEYHLYaWYHVAVeGy01Hf38rXi_A2Pxxt7AH00QMOpSC7st1Ey6lA5j2C0rcMP58hEgqCQxcM6k5wyOZjd3iuHH3HkD6kRJWjmKS9vUPyFhtadte-KxADreLhe9HxGmzehCXgDcruxPC3Y6Vbms5Lfbq7kT-_Vn6tRLEivHoniJXrOYTDRhELyPJj-oLJTG1XVH-KA7pQWMP-Q7E31dpKWFJtwEf4xeAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=rnj4y1vtlLwbcbHvmbILjS9Tj_eq4WrOOC-7l0dJXfrzuMtVUC67gKB1thswcFbP5Bt72rbZpAJAgx_wKmk_HPvuG5Pkg8pI0mdkRFsIfJWBAY7eHzZaSVxEYHLYaWYHVAVeGy01Hf38rXi_A2Pxxt7AH00QMOpSC7st1Ey6lA5j2C0rcMP58hEgqCQxcM6k5wyOZjd3iuHH3HkD6kRJWjmKS9vUPyFhtadte-KxADreLhe9HxGmzehCXgDcruxPC3Y6Vbms5Lfbq7kT-_Vn6tRLEivHoniJXrOYTDRhELyPJj-oLJTG1XVH-KA7pQWMP-Q7E31dpKWFJtwEf4xeAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری : در برجام ما به تعهدات
عمل کردیم اما اونها عمل نکردند!
عراقچی : ما هم عمل نکردیم که!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6346" target="_blank">📅 11:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6345">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cgku2rjYLgh-hqD3FzXUKQHVLZPbh3VFNd6NvVQpwTUjPjM4BVRt3wXlWMVYwqE8a_GSBdJ_f3CCQjA2vm7IfGDlve7JTAkUbjuFMJNSS8Jjvml4OyW0lWMjH6uqsy0f_oexNSLjR8Ees7eEEkrYZR8I--DSq3XDjy9LkrrD9ZFuKkaygEOi7uiu3vVnpoGv86JiXacYQvlrF_fE0IdUU7sB2zPIB6R3mAqBCUzfbL-JLmfuzL8iRXRZDj-2-TOVQqCFUD8K3CAVp7zb9OA_KNsz-L7Brz3UNvHgC60gdzGWbFNLlFu2eAsuF5UwB8bg46v6wk0D2l4LqV61TJCUCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ‌ «در دوره من رژیمی که زمانی قدرتمند و هراس‌انگیز بود، رهبرانش کنار گذاشته شد.»</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6345" target="_blank">📅 09:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6344">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2f4e943e0.mp4?token=DMZt_PXR0Jltbd3tIV9PQEdWK-DKKoHquyLojFtidsFSHVEq94pvr0QuRhMUCz5VD9uFVUopNtTMt9QEsdOvP5DnhRYPRKtqiaGX8lxW--NiMc3kGRwIaziLBXvPtirsvPvaD3Nm2NNZKGcOkIk6SO_2Uxrt6sCgtLgdtL6Ei31kz79_lv4KB2WowAE2pUPxBO9ee0f9lTnmByVUa0xJfcNcquEi9ghdiyV3IMxUlEv6ZVLDSsNnAeLAAIxIUGA1gkMN-xy4pz5fC9pR1NG7OS9tLrQOygNbITCzEuupWBTAMn4IKxl5MuYGRAlr6-oOZH5-qDPKUSKb6XcTaadzxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2f4e943e0.mp4?token=DMZt_PXR0Jltbd3tIV9PQEdWK-DKKoHquyLojFtidsFSHVEq94pvr0QuRhMUCz5VD9uFVUopNtTMt9QEsdOvP5DnhRYPRKtqiaGX8lxW--NiMc3kGRwIaziLBXvPtirsvPvaD3Nm2NNZKGcOkIk6SO_2Uxrt6sCgtLgdtL6Ei31kz79_lv4KB2WowAE2pUPxBO9ee0f9lTnmByVUa0xJfcNcquEi9ghdiyV3IMxUlEv6ZVLDSsNnAeLAAIxIUGA1gkMN-xy4pz5fC9pR1NG7OS9tLrQOygNbITCzEuupWBTAMn4IKxl5MuYGRAlr6-oOZH5-qDPKUSKb6XcTaadzxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/By1ocA3MUqdxsBxBzGS6sx9Zgy70rQHtNdUqInJSYgTJ9a75-cuzSwqjlcWqKvB5otsxb7L6n9FajtOh5AFTh2esbvNbYsm8fXac9pF9M88cHsKQhp57zwoCIbZAXwAxxLhnl6LIeOKeOPZ8QYZsEDT8L3LCnwRBn0NFuUtQZtkqtiJJlQHm-pmL_9jktUWIficxPPWwhQmilAtgKi7YtkRf8flTrVRTrQzIrj0f5e8N-ThRd641smY_5nJwYNNuOK2ohNE7m7LGIF7GUWVDBZYbFWfZGH36vkQerdTcmdXP2jiIBfDiG_mjx-RfRXY_LLs4q5326C6p9eHEbEraBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حمله نظامی آمریکا به ۵ استان ایران
۴ نفر کشته شدن!
فکر کن جمهوری اسلامی هر صبح
با صدای اذانش، بیش از این تعداد
از مردم ایران اعدام میکنه!
جنگ ۴۷ ساله جمهوری اسلامی علیه مردم!</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6343" target="_blank">📅 19:38 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6342">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">عراقچی میگه توافق ما بهترین توافق ممکن بود
اما به سخنرانان و مداحان تجمعات خط داده شد تا علیه این توافق شعار بدهند.
همه می‌دونن ریشه جنگ‌ها، تحریم‌ها، تنش‌ها، انزوای ایران و….. همه از خود اینهاست!
قبلا هم همینکه در بیرون به توافقی میرسیدن
موشک آزمایش میکردن و روش به عبری
شعار می‌نوشتن!</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6342" target="_blank">📅 19:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6341">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">سپاه خطاب به مردم منطقه : فورا تا شعاع ۵۰۰ متری از محل‌ حضور آمریکایی‌ها فاصله بگیرید.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6341" target="_blank">📅 14:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6340">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GamcLkShi6X1QSlBNP4cwMpVv4Al6s39SZvuX5h7kZdmH4qqxK_N3a9trttydXfXOvdQ5_39giWTd7Ccg0rV6GEYdSIE4Nfpeaw8d0_SYGxxHSrD3aO4Vt-aG3Kl1GArTKqBukzyFMJSYRoWIRiu3i0HRRCDY81iSZE3Z7UXx_Dct125KkWqPy5YVB1BkFM1teVEzeYv0sQIlIFd0WyK5maOxpMBAbJ6TI7Ue19y37b0AmwgGYiDsE6wOambUUsF8rwt5NGRsnUExU0UWzC4I_rOg7958E2EZoYZHsR-hw7BZnaO5ly_l2j_JJiMYtu0-xMjmoz3bu4_LBE8O81THA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه دوم روزنامه کوریره دلا سرا - ایتالیا
حمله دیروز گروه تروریستی حوثی
به دو کشتی تجاری عربستانی،
حدود ۱۰۰ میلیون دلار خسارت وارد کرد.
ترامپ : هزینه این خسارات‌ها رو از پول‌های
مسدود شده ایران بر میداریم!</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6340" target="_blank">📅 11:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6339">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07c232479.mp4?token=JJyv48JfZi_5tXLG-szBNxt8q9LAgvAZ8BpP5BKfpbdOkp5DpB4Z-6B10Yd8E4DiUxzyLbAMhcXwDSxowolbenGvg_31e_75ZiSXpooOc1N0iJGrhbcDvjcYMHB_ESjnPTV5RTar13vEtGa17DIjpvvzdV3kOwQMS1_gAuXq3KqHxdGqvHsBTdonlSwFMVovKCOlRFB1Egjk99QrqzG12ZzRjFxzmEVHEdacWsJxBzfnjamjkdjdPc085YTFkOHJP7KwQ4jdjSczQ-P_3jHr2ntX-xbAlyJ5tR6DZA7QTD_SIQfka1dPtGMWwZJ2RSUcI-mYyOc---WApC6pkZSLzp_lC8M3AMfDoSS80nDeJCAiO-5f8os_CuoPsSWPimsSb-DOp18SdwR2hiQmjFKRNjLkDQRIpGbAUzN0OnMHVSP8AJwXCFUgb26WqJy43YeDnaJGFGe2GPrPy7eQHRnfx9uHJqIfs-SK-Kt3pQ3KAdftunV9J2cTh6KbO4InqUFX1BLWeg8lSY8RBX3pZAyk5VJlwOV8vW1zgpuvkvHvKREQAoTb0XAQg1YunuwanWx30bhuntTEYENJU6k-VcS7huVmJubkuCo0q9HeOh1q_JFfCw8lVPdplhgIgm8r7bZntBhl8TWNeZ6MKLnt-sy5rw8OSc-QscrShrXyHMJfZvU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07c232479.mp4?token=JJyv48JfZi_5tXLG-szBNxt8q9LAgvAZ8BpP5BKfpbdOkp5DpB4Z-6B10Yd8E4DiUxzyLbAMhcXwDSxowolbenGvg_31e_75ZiSXpooOc1N0iJGrhbcDvjcYMHB_ESjnPTV5RTar13vEtGa17DIjpvvzdV3kOwQMS1_gAuXq3KqHxdGqvHsBTdonlSwFMVovKCOlRFB1Egjk99QrqzG12ZzRjFxzmEVHEdacWsJxBzfnjamjkdjdPc085YTFkOHJP7KwQ4jdjSczQ-P_3jHr2ntX-xbAlyJ5tR6DZA7QTD_SIQfka1dPtGMWwZJ2RSUcI-mYyOc---WApC6pkZSLzp_lC8M3AMfDoSS80nDeJCAiO-5f8os_CuoPsSWPimsSb-DOp18SdwR2hiQmjFKRNjLkDQRIpGbAUzN0OnMHVSP8AJwXCFUgb26WqJy43YeDnaJGFGe2GPrPy7eQHRnfx9uHJqIfs-SK-Kt3pQ3KAdftunV9J2cTh6KbO4InqUFX1BLWeg8lSY8RBX3pZAyk5VJlwOV8vW1zgpuvkvHvKREQAoTb0XAQg1YunuwanWx30bhuntTEYENJU6k-VcS7huVmJubkuCo0q9HeOh1q_JFfCw8lVPdplhgIgm8r7bZntBhl8TWNeZ6MKLnt-sy5rw8OSc-QscrShrXyHMJfZvU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت وزیر نفت دولت رئیسی از تماس موساد با او و انجام حملاتی در ایران
🔺
جواد اوجی وزیر نفت دولت رئیسی : ما ۱۰ خط لوله بزرگ و سراسری گاز تو کشور داریم، تو یکی از شبای بهمن سال ۱۴۰۲ ساعت ۱ شب موساد با من تماس گرفت گفتن امشب می‌خوایم آتیش بازی کنیم‌ باهم،از من پرسید ۳+۵ چند میشه؟ گفتم ۸، بلافاصله گفت همین الان خط هشتم سراسری گاز رو زدیم، ۵ دقیقه بعد دوستان مسولین بهم زنگ زدن گفتن خط ۸ گاز کشورو زدن،تا داشتم لباس میپوشیدم، موساد دوباره بهم زنگ زد و از من پرسید ۴+۵ چند میشه؟ گفتم ۹، گفت خط نهم سراسری گاز رو هم منفجر کردیم،چند دقیقه بعد مسولین مربوطه بهم زنگ زدن این خبرو هم تایید کردن،من تا رسیدم سه تا خط اصلی گاز مارو زدن.</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6339" target="_blank">📅 08:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6338">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=WqcV8jo_SmyYNUa3JLBW1dedlR8PW0E3PCNmToLc3j4-rH3wqELUwWF7Kap8wlpjBUhXXdnTcfflZxDluS7fH4h6nhLzWsK0l0KFSaObQseW9XE1v-eoC5_awRmzault87FGxELRTMnINaREzdTfFaOJeTJZqfI4u85wE786nDp94DmYwWHi4_f00OIvIRYDBQ_63CV4qKltGjqGdW-aR-cBCptDgWR9xav8kWPAu94Jb58cA_AdE9cAwp3_zlTNpuj2h1xc94wkO3LA1Hw7efnspr1NhVBlp3yPJseSC43eAXl90vq8uzqqzVG60Udv5o2S4ZgG80x6iWkZjjbhpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=WqcV8jo_SmyYNUa3JLBW1dedlR8PW0E3PCNmToLc3j4-rH3wqELUwWF7Kap8wlpjBUhXXdnTcfflZxDluS7fH4h6nhLzWsK0l0KFSaObQseW9XE1v-eoC5_awRmzault87FGxELRTMnINaREzdTfFaOJeTJZqfI4u85wE786nDp94DmYwWHi4_f00OIvIRYDBQ_63CV4qKltGjqGdW-aR-cBCptDgWR9xav8kWPAu94Jb58cA_AdE9cAwp3_zlTNpuj2h1xc94wkO3LA1Hw7efnspr1NhVBlp3yPJseSC43eAXl90vq8uzqqzVG60Udv5o2S4ZgG80x6iWkZjjbhpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - انفجارهای پی در پی در بندرعباس</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6338" target="_blank">📅 08:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YkW5Z13XQyQ65WPzeAc4G7uPjWRTTuZrkZ4HIAoEWnbZKessc-JLuzmgEeVt06BJ73U6o20aAF3v88h6ShOwmYNZUHo6zNtuNnPCx6jNcf4rj9tS3Fxx4KwRsZybrlTzW6R-RR6z_iynLAM7XAb8xmb_HWzw2vKRPWqmZU5AHLhvnmQunuH4qXE8XwftABjmKg0vsj7qki9u-VHdCYbXpf6wquf5vyTFbqQ1hF1hc50oYFNIyGjfqSrESZdrlDs7BL-yn4x-D6Q3T-DhS5fP4W2zPc9IfcuFCaaEZrDAUKfLBrc1hYfZfv1V-1HZNn1lPvu3eHkk9wxuAjuRRJQjVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید تازه ترامپ‌: از پولهای بلوکه شده ایران، خسارت کشتی‌های آسیب دیده توسط جمهوری اسلامی را پرداخت میکنیم.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6337" target="_blank">📅 08:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6334">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=udazh-trLwBsSEE8stqHQYTv01ZtW2jdXAlBjH_wGqTPoJPWghATfLoAej2lU1uKuLKsWZUVji2DES517uxUdCyASXie70U9K9eSTkRP_fEUnmtanX6UMZVu7ORD-zjHxS5fFCkaF0vQ7vyiC5tVDW2QJ01XlRmN6f9B-or7Jqfwl9xvJlaf41je93bCD5b7px6MlahXSac-3i0VklX1AqMp3vsI3TIns7wSvaNILFIeQQbbF4lGjnWHV-EGMg_7f4nHFdUzJdESwlmNpT4A99lnNfk1bva0Vss5JBMIx6kSKk8jgJgkUW_xqIWmacfexUM_gL8VBiTkPEEl_1Q8eTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=udazh-trLwBsSEE8stqHQYTv01ZtW2jdXAlBjH_wGqTPoJPWghATfLoAej2lU1uKuLKsWZUVji2DES517uxUdCyASXie70U9K9eSTkRP_fEUnmtanX6UMZVu7ORD-zjHxS5fFCkaF0vQ7vyiC5tVDW2QJ01XlRmN6f9B-or7Jqfwl9xvJlaf41je93bCD5b7px6MlahXSac-3i0VklX1AqMp3vsI3TIns7wSvaNILFIeQQbbF4lGjnWHV-EGMg_7f4nHFdUzJdESwlmNpT4A99lnNfk1bva0Vss5JBMIx6kSKk8jgJgkUW_xqIWmacfexUM_gL8VBiTkPEEl_1Q8eTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نصب ماکت آبگرمکن در مرکز تهران</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6334" target="_blank">📅 22:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6333">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
ترامپ به کانال ۱۲ اسرائیل: در حال بررسی یک حمله گسترده به جمهوری اسلامی هستم؛ حمله‌ای بزرگ‌تر از هر اقدامی که تاکنون انجام شده است. به تصمیم‌گیری درباره آن نزدیک هستم.
او در خصوص احتمال مشارکت اسرائیل هم گفت اگر از آنها بخواهیم ظرف ۲ دقیقه آماده می‌شوند، اما برای آغاز عملیات جدید به هیچ کس نیازی نداریم!</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6333" target="_blank">📅 21:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6332">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">‏هشدار سپاه: هر پایگاهی در بریتانیا که برای انجام حملات علیه ایران مورد استفاده قرار گیرد، یک هدف مشروع خواهد بود.
‏واکنش سخنگوی دولت بریتانیا به هشدار : نیروهای مسلح ما آماده‌اند تا از بریتانیا در برابر هرگونه حمله محافظت کنند.
بریتانیا به‌صورت شبانه‌روزی و در هماهنگی نزدیک با متحدان خود در ناتو، آماده دفاع از خود است.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6332" target="_blank">📅 21:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6331">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CMgGnt-qGHzpM3d2My1erroP_DqTuyp8AasywZK8NmFvgynOE6YJW8aSJ7W_2SQrTsoc46HjSZovS5x7Q94Jxmp8OoGp38p1Hbiz8-Hu4q_9dJ9soOR9ZqeEb_aRda_3c4wCJKFL_MVh8So3WoX4XZsDIUX60kszbzNk1mI4vZB-NVJBjebl54m2sz1uHjpCJ_VsQGVgQX8o5HTKJQlvSQ2AuRhMEHHnus07-Dm8bXvZ2gylc7zg2x0EMIV5KYzErs_KAJj0voYEnVC0mpjGD4j1TLGWgbj1fQ9P_T8ZbdXPulKL_GQJamAJqSRfgI38dP5MKPMgLcIzhEu5JCXxtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضرغامی : فعلا حرفی از مذاکره نزنید!</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6331" target="_blank">📅 21:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6330">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_cm8U4qnFu16rSPkUAt8B24y9PafGiWKEExyxBxsEUTgTpWNEIrRM4gk7-mVaVaAzWpSseIIFjnMBkAiMJ6Dapl5f9hRMhwQQdVXSfZov9tc0UCe_Ch0TigROxu-qCY8VXc8G5H81IC_Yfk_8Z06IMb2kkMBm_1sMo1aJwflW3TIupDF9WfaqLgGX0xxIE6btMqhmdZd3yR6NqzhTIrtBGKdkWxFgDBuNPzxrLSYJkUYekfj0oACOSi6dL9yVg7O5g0l94TnVoved0UO4ugrCblFO53Ch-jpBUPSpqzcS0Oy3e_cjsLo-Uccs8HBClddxlRcEkhIe3CyJd9BC-vrw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XuuZCaDA_YZXWVidvdi-VA8gH8KAQyKQMV2FR4NFeGyRyThYyJhGVG57KD2agtaaLHjLKFXwQhdUe26epnUgvTM_DFB7LlDmMRnwuAfBQ7ggZM4jN9zmMosBryjfI_tl19knC-lgHFHud5mfHHlnsihDIk-y-olDn_hgdUXqS5Ekg4J7PejO2geQ9I4kejPjHGMfzHb_p8w2whAZkVxC72obg6ELWVBDBwj6bFRENoPhhJyhRSYiGwpjUvZTPOHgiK6XAsty5gaaRsFj4c52V0d-Afnf8OLTd30RzZM4indKHvj5EZrW89xa3_oX-8XlHbuYSdMehcnzek1Bb9sGyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاآنی، فرمانده سپاه قدس، با ارسال پیام تبریکی به «خلیل الحلیه» نوشت: «آنان با انتخاب شخصیتی که نماد مقاومت و شهادت است، بار دیگر اثبات کردند که همچنان بر استمرار مسیر مقاومت اسلامی تأکید دارند. مقاومت اسلامی امروز قوی‌تر از همیشه، مسیر عزت‌مندانه خود را ادامه…</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6329" target="_blank">📅 18:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nlZeE8GdGFxV5j_Co8k-PgTuArxQmGFCotElPqxnpDGDSvz9pKF1Sd9cxTBE9XygFIBh76QhJcMNJrL8EWMSA5_eyG_Y0QKZVi_h9PfLO9jXYYLRMAZB5QTlhbSv2txaKLRwWz8c0lzAWyJyX6IE_RasyTp3noVnJTcCAAh5vUlIjitCvr2kp0aLjHW93lHAdTYFCTHaWHdZr8ixkPDIJQgRXOjPsxFp0YTTSI9-UFJUrcAYs3rSYcl9jLn9gyGByLHkprXCzvtAdngPcl9jNrl_bkqdeIJoj1ncBNosPhkrd8LLTiD30qhSJcEYnN33je5ZwdPUBZso82LA73fA3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6328" target="_blank">📅 14:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QNI0HV0ueQykpCRg9ArCzfBeBxRgoRDmnvN5wZra4o9zYeZkO8Gq8h1fagf4cnhYCdpkTmh88ncnCKf3Oc9ZXZPFzrO6lDPSB38TFh5B09wiQTHGOxVUVgK7mbYTNS7MP0jHJfOpolPtaVioTxCN46hcxQ_Vj2e7wHctKAQR6TExmdukgW7GoHZmdVp5My0VOX403-JCuoX-23M0tLvDfmh6ktA191TjoxQbWzyq5Gi62cUx_aotgoNDE95E_bsfKUHy-z06AMRsOLSJLe_kJc_atFJ7UmRNptSO5P0kj06tpXn7ZOcal52bFPZ5NnTjYPB_6diq-G4X0Pa3wdHH1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6327" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6326">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=CCvfstPzrIcMCK61iZM2JPLr0P8PPcAbJ9llv2yK8oeHwWAerR7Sw_AvTLB-zpDKcVOOXnaJMVP-CAsaS9Jy1_RIEPyxPp-QqrT9Eetq4Ie227PbLIQcumeIxlSc-643T8ZeeMytmd8brqm2hzo6Tq0FZUig61xCMQcFfkIc6xnCzAxYDmeFrsdaC_oQEd2hs1-FEddv3b-74zs9sW5jFMXfwC8-sMguVIlj9mTl1Liaxxo1-2pFrQ-4TrW1fP1ZUfBf9V_xmYE33o5aJK1AGxJZtd_fhj_gP7RjgCOzYswn9zUVBIN7by1cYCWr6wsapqbiQeKs0u52zfgj5tmm3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=CCvfstPzrIcMCK61iZM2JPLr0P8PPcAbJ9llv2yK8oeHwWAerR7Sw_AvTLB-zpDKcVOOXnaJMVP-CAsaS9Jy1_RIEPyxPp-QqrT9Eetq4Ie227PbLIQcumeIxlSc-643T8ZeeMytmd8brqm2hzo6Tq0FZUig61xCMQcFfkIc6xnCzAxYDmeFrsdaC_oQEd2hs1-FEddv3b-74zs9sW5jFMXfwC8-sMguVIlj9mTl1Liaxxo1-2pFrQ-4TrW1fP1ZUfBf9V_xmYE33o5aJK1AGxJZtd_fhj_gP7RjgCOzYswn9zUVBIN7by1cYCWr6wsapqbiQeKs0u52zfgj5tmm3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AOIHOWzqx6lH0asFnfl5yA9vbiHZrQtWTJuOC-SuEVM_9wyJLJ8sryfhHD3QzIZq4Cvh_gZUOPoRXkBdNBSKAa8mjYlbrGFxtUVImEneJOaVJGLY2jwakvJHbLwzXIywaHu6Jl-uB5J98DzM1627P8nltB-VVpjr_FqyheZpgVxnW96i7Z3FTH_MLqHCLDSgliXe7BF_P27QCPTN0J4wlbuDTx98JA4i0wNLEQGY1atzLX0M3M3xXXRNuWA5xl_vJy3CBNsicCr8hP0oW3PtCr3AdF-mH7dpTp-1KYIacslnZ2Uh4dvfG9Q2KXAHkqNwzM_V375LOKQqZuQKlnp5vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6325" target="_blank">📅 08:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/My1Bo6_-9UgsgTiEBcwCH-Mt9Ok5AqDhvhhQ5ob4m2YqJs7K9-ObEbHy1ESK2_Z6PMIn60OtdLFQfNqyrTjDbX0zdFEtv7eyCXR451uXbDKRBaiqoyofhS1ZakShF6Z1wVX8m451CdGxRLYgGeh7nVfJ14K6irYjsl8OstB9Iuy6rNcvlTpS7A7oLFOxvcrDpaZ4V2hr0fmy_LIeGfTqcdyBf5E-P8F7TtSx_pABpFt86xMbXz5-6kCWoWINVtbkajGDU0ZbYftDblg-pKm1IyHpNzyaRkZTgJ6wV77VjcZsFI_6SXAwhMAk3TCSfSESQESVSHpXh8ZVyVvmKdIH9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در یک تحول تازه در حملات‌ ۱۲ روز اخیر
و نشانه اینکه حملات وارد فاز تازه‌ای شده.
«بی‌ ۱» برای حملات بسیار سنگین و عمیق
استفاده میشه.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6324" target="_blank">📅 08:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6323">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6323" target="_blank">📅 08:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6322">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">جنایتی نبوده که جمهوری اسلامی
در حق مردم ایران انجام نداده باشه</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6322" target="_blank">📅 07:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6321">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=v3CN9pmXVs9-j3cXTABagckhYycYa0WCMKWEw5eritqk82CC7-LRMygOdxU7DOiX9Gg8XpMZ4zA26V4buLr1TUsDuQqo0-RMmXlNk2sghPS0BH3GZc66K0CWC70pNaldDvP0JULiNtzVq73ZP3t1IxU6h-WHUHLaRWTLX21WfSdz5mU-vSL8RoO7ycLAIyN8IpdIiEzLdjXMoZdKkLwJN5tsPAvrzztIl4BJoP88JPR70YSvPxLdv4_XUHK5BKBtRaRTaaOgF0iE_epUPWKVISqQnLpLvqHXqboqR-ZV-XfnuNPUWnx6rVPT26efjZ46NEZunqQNIme5BlBi7HOFhjqvLmh6Qh7WRr9IXEPV-jLVGOTB3Oaj6DfIgrOSWOn2UasXT06NRyMTQeiMvq48Cc0pBei38Mg8_o2M3S2OYVHKTuwo-tJ01tc0695gxe030sJKd0wA2u2mwakhWpHDczQqFtKhbUFOmsuOc0t2ihz5d6FYIad5TN8ikBZnDAaBjvMQ24N8_RR1INoXC14_GO8zTKaB53UQUzVIEsnswBdXm7fW_89hE9Fe6941HrnJjUQF7WVT5g6Gjb3Y4FKPlJPG_lpHYNRxGXxrv-yJSgeFJLzy3JwSLZn59Ri1kmT_aJsAL7Gu_kRmSreu-QxNiwc37EylptLx5HeQHv0hrKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=v3CN9pmXVs9-j3cXTABagckhYycYa0WCMKWEw5eritqk82CC7-LRMygOdxU7DOiX9Gg8XpMZ4zA26V4buLr1TUsDuQqo0-RMmXlNk2sghPS0BH3GZc66K0CWC70pNaldDvP0JULiNtzVq73ZP3t1IxU6h-WHUHLaRWTLX21WfSdz5mU-vSL8RoO7ycLAIyN8IpdIiEzLdjXMoZdKkLwJN5tsPAvrzztIl4BJoP88JPR70YSvPxLdv4_XUHK5BKBtRaRTaaOgF0iE_epUPWKVISqQnLpLvqHXqboqR-ZV-XfnuNPUWnx6rVPT26efjZ46NEZunqQNIme5BlBi7HOFhjqvLmh6Qh7WRr9IXEPV-jLVGOTB3Oaj6DfIgrOSWOn2UasXT06NRyMTQeiMvq48Cc0pBei38Mg8_o2M3S2OYVHKTuwo-tJ01tc0695gxe030sJKd0wA2u2mwakhWpHDczQqFtKhbUFOmsuOc0t2ihz5d6FYIad5TN8ikBZnDAaBjvMQ24N8_RR1INoXC14_GO8zTKaB53UQUzVIEsnswBdXm7fW_89hE9Fe6941HrnJjUQF7WVT5g6Gjb3Y4FKPlJPG_lpHYNRxGXxrv-yJSgeFJLzy3JwSLZn59Ri1kmT_aJsAL7Gu_kRmSreu-QxNiwc37EylptLx5HeQHv0hrKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">- رئیس جمهور سلام میرسونه و تشکر میکنه
- باشه</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6321" target="_blank">📅 07:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6320">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
در جریان حمله آمریکا به مرز شلمچه ۲ نفر کشته و ۱۱ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6320" target="_blank">📅 06:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6319">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">مارکو روبیو وزیر خارجه آمریکا : جمهوری  اسلامی تفاهم نامه را نقض کرده و لذا دیگر  معتبر نیست.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6319" target="_blank">📅 06:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6318">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65da400742.mp4?token=NXHN-0zrh1jEfaXH8lgwTD2tM-Bac-g38AWkBfgNo4xTdJ6lzY7az40DFISgVtQWDGnHyRV50OXBLWIpW25B3s30xhNtjmCJeO2Dbody93JbAkjcjUhRNQ_iMCPXx1He468ytBx11TAHeTTQ7lHOpAcUiluxnHexgHMkTK28wuAqwdL9IQDGZUoZssDf8oiPDkMCdWaeGZWsyspcmslCnH7ySrefRomgj13ExaRdh_q_DYBzoFuWCCvXZ2e_kNhVQCINgkyFToF3CXsyHGbVcbNB7OBfMBM22MgQQDV2A-VCFFdAcOauAdu1gBuAfV-Xlf90kX9H7M-UROqg4W_9TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65da400742.mp4?token=NXHN-0zrh1jEfaXH8lgwTD2tM-Bac-g38AWkBfgNo4xTdJ6lzY7az40DFISgVtQWDGnHyRV50OXBLWIpW25B3s30xhNtjmCJeO2Dbody93JbAkjcjUhRNQ_iMCPXx1He468ytBx11TAHeTTQ7lHOpAcUiluxnHexgHMkTK28wuAqwdL9IQDGZUoZssDf8oiPDkMCdWaeGZWsyspcmslCnH7ySrefRomgj13ExaRdh_q_DYBzoFuWCCvXZ2e_kNhVQCINgkyFToF3CXsyHGbVcbNB7OBfMBM22MgQQDV2A-VCFFdAcOauAdu1gBuAfV-Xlf90kX9H7M-UROqg4W_9TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون بابایی که با نخوت …</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6318" target="_blank">📅 22:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6317">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=RY8iORhWeianzhFDk1EeJxrAeIpPD09KiR3AT5-U9YZRzrGqmIMVMK17J84sqYwYp3Jts5i0Xq3p9-LO5aAI-IR-m9wKqJOVUNJSJX8kY2Y7DaU7RQfyywauAtDHMd_wY5X-tCdiJcIH9xB0vZlzvfDFSA9ivS-9r7QfTtjMJ7RY1BUajvCbhxsiU8QLkNKUuN-aZVnE__B7ohY3ymyQ661m15nUBUjWUMlDST4AAXAldiXRIuvFkHBDLiUNASD7jBqr5b_WcKD7wjLYtJ1oGOJBQclTbP5Y3UJ4VuWiBj88JmBKVTqaXZ_n7qHBDkMl-f4oZb-i6wRkRTy1fS2KCoMzM_WnvAVAhe8NNWvN-nVpISLf23l4b8syVGbXQkFfZetvh5zNxLtmg_9L3HI9NO8n3rEel0zbh_9HPOcl_tv5YAy1wnweZF37AObKe1E8ZzTenUVVfiMQP-FIx61UoXRW9DTgoZgxk4R4xwMVH3pDWiJfOBKvpE4FvUz6IdTnbYudwfvGw321aAESxdhvWVIvQQ3QLIpSLUFOAtc-KTuN5e2XKD6hpn8Mg-Stqxywyoh2ECSwsFZmqpPuQYnMDNRvi--JYwlpTnSrGvAlLuD6Kkvx919h8B0F9m7nz9A7_Xq52ABoBbnyr_zmNKA3RVQZzB9i0eR2UEmmgHTgQR8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=RY8iORhWeianzhFDk1EeJxrAeIpPD09KiR3AT5-U9YZRzrGqmIMVMK17J84sqYwYp3Jts5i0Xq3p9-LO5aAI-IR-m9wKqJOVUNJSJX8kY2Y7DaU7RQfyywauAtDHMd_wY5X-tCdiJcIH9xB0vZlzvfDFSA9ivS-9r7QfTtjMJ7RY1BUajvCbhxsiU8QLkNKUuN-aZVnE__B7ohY3ymyQ661m15nUBUjWUMlDST4AAXAldiXRIuvFkHBDLiUNASD7jBqr5b_WcKD7wjLYtJ1oGOJBQclTbP5Y3UJ4VuWiBj88JmBKVTqaXZ_n7qHBDkMl-f4oZb-i6wRkRTy1fS2KCoMzM_WnvAVAhe8NNWvN-nVpISLf23l4b8syVGbXQkFfZetvh5zNxLtmg_9L3HI9NO8n3rEel0zbh_9HPOcl_tv5YAy1wnweZF37AObKe1E8ZzTenUVVfiMQP-FIx61UoXRW9DTgoZgxk4R4xwMVH3pDWiJfOBKvpE4FvUz6IdTnbYudwfvGw321aAESxdhvWVIvQQ3QLIpSLUFOAtc-KTuN5e2XKD6hpn8Mg-Stqxywyoh2ECSwsFZmqpPuQYnMDNRvi--JYwlpTnSrGvAlLuD6Kkvx919h8B0F9m7nz9A7_Xq52ABoBbnyr_zmNKA3RVQZzB9i0eR2UEmmgHTgQR8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن روحانی ۱۳۹۷
تا آخر هم افتخار میکنیم به نفوذ
در عراق و سوریه و لبنان و…..</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6317" target="_blank">📅 22:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6316">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IjjGPQrZ3nFOyFArf4_PeR8FfyHM031fli28kCoxiEDRaaSHmu8BsXJnmka0j48poG8PJuNjfVfiS4Es_Oabtyzj87KgQRCqoCdo67POLrP1cFBx55WBgIx4apKiOV_KgZl-MxGQjJRVeujVBFjJilYF_fEx54qLrcGwY6A4UzU5Yc-WY4hMinhMlhfaTlF4ub0mlv3Z9Pl2TTQVzhGbjccYPfwG0ntPvWtB_f2QSR1ZSuFi8C6CKDqm94pcssdS0X5ifFUPeCyFWnVT5b1kxVefJbMVwnwbYMExJeEUSUez2qLy88PNNrwnlw7hbUheoec3P9uMuQNIp2VYBWXRcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏سخنگوی سپاه خطاب به شرکت‌های کشتیرانی‌:
مسیر مین‌گذاری‌شدۀ جنوب تنگۀ هرمز  [ آب‌های عمان] مسیر نابودی سرمایه ی شماست!
قرارگاه خاتم هم دقایقی پیش هشدار داده بود که فقط از آب‌های تعیین شده (بخش ایران) باید تردد کنند.
جمهوری اسلامی رسما آب‌های سرزمینی عمان رو هم ناامن کرده.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6316" target="_blank">📅 22:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6315">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
قرارگاه خاتم :
تنگه هرمز همچنان بسته است و اگر قرار هم باشد شناوری از آن تنگه عبور کند صرفا باید از مسیر تعیین شده [از سمت آب های سرزمینی ایران و نه عمان] و برابر ترتیبات اعلام شده قبلی تردد نماید.
‏
🔺
در صورت عملی شدن تهدیدهای آمریکا، نیروهای مسلح جمهوری اسلامی ایران اجازه صادرات یک قطره نفت را هم نخواهند داد و زیر ساخت های نفت، گاز، برق و اقتصادی منطقه مورد هدف قرار خواهند گرفت.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6315" target="_blank">📅 22:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6314">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JVN7NtBMqtxf3KZqn-1ElPl3Tycqq0tpYD16YjSTxZ-uqpV0SEZcdRQUBuUYtU2LdIyitN3bFbyYEOKt-fSeUvv5VM4qUAgCaYdonAmdz3jKtzGT8Vtx_52DHyvvxwHsXqGYYmw5Nn2EX-sIX5ZYNDGayo-7vlEPfC_Amgh1zHAxe4lCJf0FN5Bs4GI3PnU2ht_iuCTcrjn-H094fQ3A1DyuRXWLTcmOWi0_QY1E-pz7GUuJl_3opAhc8mujTtterdqbtIEuCvV5sxlGui3VLFeuSxlx3vfUztLdI-IIw_i2ZkVqcTZCD6ZT1ao2UdW9Db3vGt7PJZcJmT5ZMkFZEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6314" target="_blank">📅 18:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6313">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pTssT9mBDGcFaaB2-evoHtO40LB5XsUWZ1yCd9CAHfsh35ThzexoQOlWT5Oz58qNSPypiPt_hLWD0Fu08s4TJMpaX_UtFCkDaPDiEkUDRXsaeq-dB_E0HJbZSWAA2qaRPO6Ofvuz7Ei8zPTIPA8WZYQ-06HbO9A-Fy2-LqrW9HTWGYVwdtgHsZ4kd0HlcPssR3ZDDV4ZjDg9xyTL--I7uQg0mnXIlGNifzGzxvI_MH0tEDNh2G4aSOS2en7SA0S99LHh_WGFrZHfgjel3s6EgqBdTqyjNnUXDxZymTCQebasq_pnBThbGTpen1UAZvOP4x-4MMv8706eqsMjvafG7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6313" target="_blank">📅 17:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6312">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
شب گذشته صدای انفجار و پدافند هوایی در ۱۹ نقطه کشور
تهران،  بهبهان، امیدیه،  ماهشهر، سیریک، بندرعباس، بوشهر، چابهار، کنارک، تبریز ، بانه، کبودرآهنگ،  همدان، خرمدره، ابهر، زنجان، دینارکوه،  چوار، آبدانان و انارک.</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6312" target="_blank">📅 08:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6311">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=uc2WFgxNwJGBzlGuGEtb-jKqTxuCkF4SMensrN-FwE9iMw-V_YjkB62K3sV2mNjC6mVKc0CRjaWvCsNC-c9vVRcfTMTDxrEALYMDIeYr77ImKOzmQuTGSUQ0fAATjZGqFEUoHgOu59h_SR5nZ2DYvIDd-JpF-r6e-mUINKJhHNDq81NguW-PkwILuhLnlf3HulP2Vvz_VwnuHydFy0mwLEiSQLypKS8BqXCFzoCOLZxUn4ooy_L4BnGP9pltU5hHx4kGGMfFBHPZpEgH8RL7DAMk6Q2GSsWLWI3n9kkDbcBQDs8PKwKJKa8zvHc6xFBHpOfycXikQjPyaPBxRg9waA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=uc2WFgxNwJGBzlGuGEtb-jKqTxuCkF4SMensrN-FwE9iMw-V_YjkB62K3sV2mNjC6mVKc0CRjaWvCsNC-c9vVRcfTMTDxrEALYMDIeYr77ImKOzmQuTGSUQ0fAATjZGqFEUoHgOu59h_SR5nZ2DYvIDd-JpF-r6e-mUINKJhHNDq81NguW-PkwILuhLnlf3HulP2Vvz_VwnuHydFy0mwLEiSQLypKS8BqXCFzoCOLZxUn4ooy_L4BnGP9pltU5hHx4kGGMfFBHPZpEgH8RL7DAMk6Q2GSsWLWI3n9kkDbcBQDs8PKwKJKa8zvHc6xFBHpOfycXikQjPyaPBxRg9waA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگزت وزیر جنگ آمریکا از ضرورت
برخورد با جمهوری اسلامی میگه
ونس، وزیر خارجه با ناراحتی به او نگاه میکنه.
(ونس طرفدار گفتگو است)</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6311" target="_blank">📅 08:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qiyn4eNalMmhJgdRbjd8d59mqD_iCH79Kh_YGM69t7A43CN0SQ_um9XMk17bkY2BwVV9VjBEBccB8dt_Sd6MnYh5tnpt1w8D-6tlwSBetZSt6WG-s7FX3avGkVvBmXhnlSEHNyWlFTQi_-dVtnlXDas0UOljRPUVR3HvaEb6vVbzJsSJ-Xmyrlj8k7ncWggLYgB_TrS0KL1J4AuthnMKMUtDHHhEYRVPIetL4rR1JvIY2v7Jbs-D_KTV-SdZAPbmti6rETpvBh15A8IHYYq-JYd-1kc1JMvrqPqCdBJaaUT4gDkGyYg1I_cUT5i-mZJmF-2oncAwbTX0u6Qsci7UnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اندی برنهام نخست وزیر تازه بریتانیا که از دیروز در این کشور قدرت گرفت، با در اختیار گذاشتن پایگاه‌های بریتانیا به آمریکا برای حمله به جمهوری اسلامی موافقت کرد.
پایگاه‌های «دیه‌گو گارسیا » و «قبرس» از مهم‌ترین پایگاه‌های بریتانیا و مشرف به ایران است.</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6310" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A1SjOpgT4TG-3lcZlbEimktS6ZyKEX2bzclDeD7LnJ_WlGeQUoSWTJw8r3q6GADDEFaAfZ2DimDkV8jOeLgGzQ8MGRLE8Jdh1iGZkmCdwJDmSnUDk0CeZne6mGDlqoVg5_zXaNwjPvJS4vEi0XMGrFGqX53miGj-lL-5mySFWHLAbs_e2gZy8EA5x-6w2kO8iwKXufUPDLOYEe42M-tdm_god8m2RijUok-EWsjIXDaS4XdTJeYCmjUG_jd1j54QipgNCeldi6YYBbwcwnKrobDw2Yh3GYVwAKwcqVdAExxEatsXABixEAE_2Mx7U2RmKZI8TIWC2BtUc9t5yCZjGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kYqGHDEc7VkyKL5kJlKlKxbBkIyoYWcxT7E5mk5-A3kaMomnbVPGqSy5MyCGWtaFvr2ynlHIvN66S_qAwJSoqSNTqCFyoEOp87uOifvgq1Su3iTxUXAk7LC0EqWTNVe0gesPl0ukaIfQztE1ro0Pq1WMMh6CbYr9UANf6E6f7qLmEMWMHOgsQoB-eT6SGEHNwJsj98ugfTcjjoTvRO6-NODUOT_RMvllnT03tL2wIAxdyufQuceMwSZh2onDR7Tk8G6rv-cM0Hla_-GwCJ9kuRf7mxIuHwU4qZV6jyeP-JaNCQncHzbVbuOEG12Fv-A2GzrtuYuIOUMPOMLbAbwGrQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسن روحانی رفته خونه لاریجانی تسلیت
چهره زنان رو!
بعد همین ها میگن اگه ما نبودیم داعش می‌اومد توی ایران
داعش ۴۷ ساله که در ایران حکومت میکنه.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6308" target="_blank">📅 23:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6307">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
گزارش کانال ۱۴ اسرائیل :
جمهوری اسلامی به سفارت اسرائیل در بحرین حمله کرد.</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6307" target="_blank">📅 22:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6306">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nBW0mE1JBOiPl2ETZMR8jsJg6VQfeBMfYh2lloL7sIc11Pji_UEDbCX754XU7vpfmOYtyfECAKVTgdNGzcBcdFaQB9DO4O-kkYzUGtAuetC82GOz1X-5mNulNYpr0xMfaKNyKiA0YgvJ71dLzUhHIST9QucuMCUWqgF5dUho_8Pu7gKaycv0WTtwv0h3e-K2Iic2xPR593t3Qr-6SiQ7WVgmQ3SEbpX3e-OPLwncNwW7ShGqxdIJI7cZRA1O3l_Mp4wYLaqFCwDaUKtwH1oNxDZAMacMW8J_ojN4m2voOs6p-vuUna_5sunN_bFBjq1mbvK_lzldz_RahWTtn_xWUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موقعیت کوه کلنگ، در نزدیک تاسیسات هسته‌ای نظنز، گفته می‌شود تونل‌های بسیار گسترده و وسیعی از چند سال پیش زیر لایه‌ای ۱۴۰ متری
از سنگهای سخت ساخته شده است
و پس از جنگ ۱۲ روزه،
هزاران سانتریفیوژ به این تونل‌ها منتقل شده.
گفته می‌شود اورانیوم غنی شده ۶۰ درصدی ج‌ا
در زیر این کوه پنهان شده است.
بازرسان آژانس بین‌المللی انرژی اتمی هرگز موفق به بازدید از این مکان نشده‌اند.</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6306" target="_blank">📅 19:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6305">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=LXv9sliNil6_RUnjCvOlpn9fKE2nZNbLVXCk2cv6NRRW_8WlYN8LtURkWFph8hU-tQMQGWFg6vBrSWY8XOwYYGCcm5VxxvxNmNcoGN2nMzU-RcfXgJtywY2J4aRo4PkKPTZbpYn-_6zdCDO0EMPrz4n_GJyBFQg3CW-uK-2YwwGdlGOMASu6f0RFK-34PdbIUlcYyCC14MQTctdgbv3Thj9Wp2e8RvGUmZXzVLWXSoaBK2kIrsPsTs73LlEYWEWIdmpEbRXc2WZSJZnr_tGjV8Bbc6RaUoL_xKFAHjuOifrjGgGrNncyt5C1pthXJIyuh3_ETQt81pOdCVShZfD_rjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=LXv9sliNil6_RUnjCvOlpn9fKE2nZNbLVXCk2cv6NRRW_8WlYN8LtURkWFph8hU-tQMQGWFg6vBrSWY8XOwYYGCcm5VxxvxNmNcoGN2nMzU-RcfXgJtywY2J4aRo4PkKPTZbpYn-_6zdCDO0EMPrz4n_GJyBFQg3CW-uK-2YwwGdlGOMASu6f0RFK-34PdbIUlcYyCC14MQTctdgbv3Thj9Wp2e8RvGUmZXzVLWXSoaBK2kIrsPsTs73LlEYWEWIdmpEbRXc2WZSJZnr_tGjV8Bbc6RaUoL_xKFAHjuOifrjGgGrNncyt5C1pthXJIyuh3_ETQt81pOdCVShZfD_rjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=WfnVMPl-FHbXGNWxSJkbZX85wuo-BG6NsU9FC5xroMsWWIiCh7Ablxvixza-aQxAoBQDW_oIZK4D_im6ml0c27526AC_vCdtJuMInTgyPJlzkzaEi6LYHqvgxOddzrjTfzNf28w9ObqGWkZHJ9DUJPLyZzg7lbRsrQg11-FiMqVsyeEwi4v6hcviKM-0263x08mpdxcHcitv8pTHLg9Y1grWs9ymb1-cmmac5SHxv62Npq87-yh_ZIatbKceFmtnW-AJIInXIP55UouTWRVCZ_lTDES-VwznA6B4ZlcC5Nb_7KLeIso7g5Vf5fNHLJ8wnoePCazv7BlVErmNCGbsYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=WfnVMPl-FHbXGNWxSJkbZX85wuo-BG6NsU9FC5xroMsWWIiCh7Ablxvixza-aQxAoBQDW_oIZK4D_im6ml0c27526AC_vCdtJuMInTgyPJlzkzaEi6LYHqvgxOddzrjTfzNf28w9ObqGWkZHJ9DUJPLyZzg7lbRsrQg11-FiMqVsyeEwi4v6hcviKM-0263x08mpdxcHcitv8pTHLg9Y1grWs9ymb1-cmmac5SHxv62Npq87-yh_ZIatbKceFmtnW-AJIInXIP55UouTWRVCZ_lTDES-VwznA6B4ZlcC5Nb_7KLeIso7g5Vf5fNHLJ8wnoePCazv7BlVErmNCGbsYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
نخست وزیر اسپانیا : «در تهران، یک خامنه‌ای با یک خامنه‌ای دیگر که بدتر است جایگزین شده؛ چون مجتبی از پدرش خون‌ریزتر و دیکتاتورتر است و او واقعاً سلاح هسته‌ای می‌خواهد.»</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6304" target="_blank">📅 18:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6303">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=HGAalwyv1AAspIAHHMPuC2yqLqYha1x_addBjmSdcU_3dNYm4Iteg6JjqLSfTwinClQslv8pCH-oaYT-8M4O1t1KXCC73DUs2hEC1iAutPGcghZOSHmudfEXnNSY2Jrldr1o59vcDAqOl0zqS9J_O4_NNKEXWNKlUPp5dSkKCWMcZ4DMsGn22yFGR0cd5iIJ_NG-rMK7oPsSMrBvYfyAPyvgAoLiEIXTQ6jhnlkLYF4IOISNZg2lxiEqGXME7Nsa2w9Bv9o2UfkkqUC8kyu_VYSXnb1dOTe3MD0c8g_qmtbQsW8-N2jVzP4QkEmHoiATOw9OvUf72HEyowOVc2yXsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=HGAalwyv1AAspIAHHMPuC2yqLqYha1x_addBjmSdcU_3dNYm4Iteg6JjqLSfTwinClQslv8pCH-oaYT-8M4O1t1KXCC73DUs2hEC1iAutPGcghZOSHmudfEXnNSY2Jrldr1o59vcDAqOl0zqS9J_O4_NNKEXWNKlUPp5dSkKCWMcZ4DMsGn22yFGR0cd5iIJ_NG-rMK7oPsSMrBvYfyAPyvgAoLiEIXTQ6jhnlkLYF4IOISNZg2lxiEqGXME7Nsa2w9Bv9o2UfkkqUC8kyu_VYSXnb1dOTe3MD0c8g_qmtbQsW8-N2jVzP4QkEmHoiATOw9OvUf72HEyowOVc2yXsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسپانیا که این روزها دارند
پرچمش رو میچرخونن!
می‌خواستیم ۲.۵ میلیون دلار بهشون بدیم
برای اینکه با ما فوتبال بازی کنن، قبول نکردن!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6303" target="_blank">📅 18:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6302">
<div class="tg-post-header">📌 پیام #14</div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nlEOoTu-e-2kYTtNJSDFoO5vYq18lYoqhadx8JDE_MPifatQKV7ieUzQvRUciH9phBLcC05Izxdl6d8Y3ZkUdrF-RvA4eILFaPWTREh0Q4JI3-hHG3kH4jWKA3KGQSTY7_EP_47k_McI0_8pdvFM9ne7Zss-so-1jB6nFVHiKa5CSIpYPpZf1vKOJStUO2ZYrdklEu-WIzFu8eK7Thct75TeSCNwJMQ_yB-Nku1xls-vUwgvDGt6uPOa6ie3wkHkmzG2fJ_GTsMozdWQU7YlfIhqHpKFcl5huv2xwtHMGRfbQPyb222wOBN2sPEzOfoZmEMF8KdhMq54u4hsk20KRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با بازنشر تصویر گل‌محمد محمدی ۲۳ ساله، که امروز به دست جمهوری اسلامی اعدام شد:
«جدیدترین قربانی از اون ۵۲ هزار نفر  معترض کشته شده.
وحشی‌ها!
کی قراره دمکراسی‌ها بیدار بشن؟ (نسبت به جنایات ج‌ا) »</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6301" target="_blank">📅 16:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6300">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46c8806804.mp4?token=cpcQFzKMEMeVyJ0YZsZm_47bftwufojB7koGLFltDucFhOTtBlrytKa1CNLaOeX1gXkCnUyUFLugiZBZOWjj_hCZOlzyBQIDcSVclFel_m2YUYqg_axNt9ivQAjgQ6ahxCCV4NjLh1n6NPxMVtdi0pv7jIgLLi5xKTIeHg4gbYhmY1nF55NEbLJKU7mykanMkEg1ec4BhVIpfBOiAUjBZ_WY2SSmOkMT4vl3F0HCYYNqvS5ndERMn-hJnIezYjB-ZWXU03iEMBM1ZKfcuJBH4DBzOxSclo2V35z9qnc4jGO5pETsWG1XEyO4gbMyhm5JtGGUErNzw0Z9iT3pHlx9hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c8806804.mp4?token=cpcQFzKMEMeVyJ0YZsZm_47bftwufojB7koGLFltDucFhOTtBlrytKa1CNLaOeX1gXkCnUyUFLugiZBZOWjj_hCZOlzyBQIDcSVclFel_m2YUYqg_axNt9ivQAjgQ6ahxCCV4NjLh1n6NPxMVtdi0pv7jIgLLi5xKTIeHg4gbYhmY1nF55NEbLJKU7mykanMkEg1ec4BhVIpfBOiAUjBZ_WY2SSmOkMT4vl3F0HCYYNqvS5ndERMn-hJnIezYjB-ZWXU03iEMBM1ZKfcuJBH4DBzOxSclo2V35z9qnc4jGO5pETsWG1XEyO4gbMyhm5JtGGUErNzw0Z9iT3pHlx9hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خامنه‌ای: ما دنبال اقامهٔ حکم الهی هستیم! ما هستیم برای تحکیم دین خدا! برای رونق اقتصادی و… که دیگران هم می‌توانند انجام بدهند و در دنیا هم انجام می‌دهند!  بله! بقیهٔ دنیا دنبال ساخت کشورشان هستند، این‌ها برای تحکیم دین خدا!! پول و ثروت ایران برای این خرج…</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6300" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6299">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">‏رویترز: حوثی‌های یمن در ایمیلی به شرکت‌های کشتیرانی نسبت به بارگیری یا تخلیه بار در بنادر عربستان سعودی هشدار دادند.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6299" target="_blank">📅 14:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6298">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
جمهوری اسلامی امروز دست به حملات گسترده‌ای به قطر و بحرین زده.
علاوه بر این جمهوری اسلامی به دو کشتی یونانی در تنگه هرمز حمله کرده.
حمله به اردن هم ادامه داره.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6298" target="_blank">📅 13:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6297">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=PvT2XoP53G4bLoDL7I_MFw1En2540rwX6crg6iwFfosKYoKz5UtYPOXNuywAdjdLAYl7viWZgwSid1Z6K-c60yA4qGqqzqRiS7ZW1fu8ps4-9yTga2v2cG-2NEBRApAGF-NdyFSQcKJigVsVHISNJ9w0T840r558wIu0ktGYrmaDEBy8o4DZDXc5OIivU4bMk1atGn68OolBnzJx8h-DAoHIT64bd79SI9BbjFDnuRWDF7LUtPSX_kX9VDeQBML0UIfq1anFGHSP2Fwmva5RTBKxSZ0qI0z04f1p2I7KvORItYezgsB5stfLdb2mUn8PKYNS_g31gqY_xeg8cv_4rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=PvT2XoP53G4bLoDL7I_MFw1En2540rwX6crg6iwFfosKYoKz5UtYPOXNuywAdjdLAYl7viWZgwSid1Z6K-c60yA4qGqqzqRiS7ZW1fu8ps4-9yTga2v2cG-2NEBRApAGF-NdyFSQcKJigVsVHISNJ9w0T840r558wIu0ktGYrmaDEBy8o4DZDXc5OIivU4bMk1atGn68OolBnzJx8h-DAoHIT64bd79SI9BbjFDnuRWDF7LUtPSX_kX9VDeQBML0UIfq1anFGHSP2Fwmva5RTBKxSZ0qI0z04f1p2I7KvORItYezgsB5stfLdb2mUn8PKYNS_g31gqY_xeg8cv_4rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=B044K9ykexA5YRVqOH-78JDXOJ2LsLMsWH-K8cetuXbvlk2GjcbqVWX7ij5XUk-m7KoO0cGq1fePPzGHWchNtYKGdKl_HWXOiaGRUeK4pMtN1_z1CUx-4-NCXec5F2phBuk1o3TP292n_3Z6IbZ5uG3FnVTYURYRz7JmkBYmouQ6glSQo3hAJ_eLpdY7UdRuhyFsilDdumBSTV6UQp-h949bDrfMQOdES87XdjyIEiGIxaIsvWt-hPM7xf3PSUU65be_D1F6rPx3RYkBGmqpZQHz4l13H-FHmptMp40pZij9CGMsM_FWmOhM0XAxgUbJOEy3QM60ZOdCyam2QqV0mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=B044K9ykexA5YRVqOH-78JDXOJ2LsLMsWH-K8cetuXbvlk2GjcbqVWX7ij5XUk-m7KoO0cGq1fePPzGHWchNtYKGdKl_HWXOiaGRUeK4pMtN1_z1CUx-4-NCXec5F2phBuk1o3TP292n_3Z6IbZ5uG3FnVTYURYRz7JmkBYmouQ6glSQo3hAJ_eLpdY7UdRuhyFsilDdumBSTV6UQp-h949bDrfMQOdES87XdjyIEiGIxaIsvWt-hPM7xf3PSUU65be_D1F6rPx3RYkBGmqpZQHz4l13H-FHmptMp40pZij9CGMsM_FWmOhM0XAxgUbJOEy3QM60ZOdCyam2QqV0mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد اکرمی نیا سخنگوی ارتش
‏به روشنی میگه اكر آمريكایی‌ها
بيان در جنوب ايران ما خاك خودمونو هدف قرار میدیم.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6296" target="_blank">📅 11:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6295">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=MqfV48F4Tbq3CEK_nhq5CvvlxCKu_ETCSG0Ut1m51qxRgTjhIeQrtca0Zwu9_AEMbrDMhgL10y_FeC04tmzj3mgutdBNqBAcc9KkKP9LbZ2q41JmSZWrt7FYKpIHx0Y7XRTB4w6jlkYJRL8VBG9TQrDP8u31JKwPYmZsOJwOA2DLWO7FC8nRSZZbT2lELHRuwRNqk_-iD96mj9vgRai0KI7G_pEcSh1q23OPqyqZSWQH-l3FYunifofGEJd956FZG0XV47QeV4E4yevFf4R8Yu9JsBdyUiSmHNYvDe43oa5tnBkLb_zxWVe3oqWP9CSQQT_YqonOmUb2xwC6dhUFBjApkn8S1YRBcc1a2xNB9uqn-JD6blskFWTSqeIl900E6UUpq8lxmAv56NYF_irm93bIC9UlEXyw71kHWSvyTJtTmhmZxfcEHk8HXbMeiKqvKx3cLCx0a4LpP4tb7yCtzFqhht5AdizTXmORm2R_nWTegWLrgqbDhapgsCJu0jNUqVYZ6OCDG7YJFG2me6fTXxCFUm2oVAiMpQiRiAkDuyzErrJJ0hlEN3Atjhdwm74caPqXpAev5UmRt4PAeDcjd-Qx2Out5NC8WttYsHqcZxQCLSXiDYFjGwoewvQaDZaYdHFIfboRlKDuxPw7dyyk9hhBVNF4qLQhcKyYm4rpRKY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=MqfV48F4Tbq3CEK_nhq5CvvlxCKu_ETCSG0Ut1m51qxRgTjhIeQrtca0Zwu9_AEMbrDMhgL10y_FeC04tmzj3mgutdBNqBAcc9KkKP9LbZ2q41JmSZWrt7FYKpIHx0Y7XRTB4w6jlkYJRL8VBG9TQrDP8u31JKwPYmZsOJwOA2DLWO7FC8nRSZZbT2lELHRuwRNqk_-iD96mj9vgRai0KI7G_pEcSh1q23OPqyqZSWQH-l3FYunifofGEJd956FZG0XV47QeV4E4yevFf4R8Yu9JsBdyUiSmHNYvDe43oa5tnBkLb_zxWVe3oqWP9CSQQT_YqonOmUb2xwC6dhUFBjApkn8S1YRBcc1a2xNB9uqn-JD6blskFWTSqeIl900E6UUpq8lxmAv56NYF_irm93bIC9UlEXyw71kHWSvyTJtTmhmZxfcEHk8HXbMeiKqvKx3cLCx0a4LpP4tb7yCtzFqhht5AdizTXmORm2R_nWTegWLrgqbDhapgsCJu0jNUqVYZ6OCDG7YJFG2me6fTXxCFUm2oVAiMpQiRiAkDuyzErrJJ0hlEN3Atjhdwm74caPqXpAev5UmRt4PAeDcjd-Qx2Out5NC8WttYsHqcZxQCLSXiDYFjGwoewvQaDZaYdHFIfboRlKDuxPw7dyyk9hhBVNF4qLQhcKyYm4rpRKY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به زیرساخت‌های فرانسه و منفجر کردن پل‌ها، قطارها و خطوط راه‌ آهن در جریان بمباران‌های متفقین برای آزادسازی فرانسه اشغالی از حکومت نازی‌ها، ۱۹۴۴
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6295" target="_blank">📅 09:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6294">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها @hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6294" target="_blank">📅 09:31 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6293">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=Owznjzv7P8WFL717zJi21o1RJTyZhBhnBzFMtG_kzO8_lwxv5lmA67q8ph1aH1C8VD6DmdejB_j_6YXidYc3ljIPE56OS6wn2EPGgY-dxO4dhkpEO_7IKq3HGfcsluFcbhE1ZTow_sbu3ImyqrP8ynicFQu97_NMfTgpDfCksrlN0gOI89x5kuyXk9fO-fHEPGFpbpcdPuOjymgHQxC648XkxxJsE4OM4Kf4EhBQ69FLv99gWn5S0-XO9hdceaUoU6bc28OS00whAhcfTdLb-35RrS4mrimlQI6DUnxUkoNHvNCdbAl1hsI-P1loVFS3fUFCTpfsG1ZjtGgaQcOqTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=Owznjzv7P8WFL717zJi21o1RJTyZhBhnBzFMtG_kzO8_lwxv5lmA67q8ph1aH1C8VD6DmdejB_j_6YXidYc3ljIPE56OS6wn2EPGgY-dxO4dhkpEO_7IKq3HGfcsluFcbhE1ZTow_sbu3ImyqrP8ynicFQu97_NMfTgpDfCksrlN0gOI89x5kuyXk9fO-fHEPGFpbpcdPuOjymgHQxC648XkxxJsE4OM4Kf4EhBQ69FLv99gWn5S0-XO9hdceaUoU6bc28OS00whAhcfTdLb-35RrS4mrimlQI6DUnxUkoNHvNCdbAl1hsI-P1loVFS3fUFCTpfsG1ZjtGgaQcOqTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6293" target="_blank">📅 09:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6292">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=X7tvX5HXcmZzBXRWKSFGQnHOc4nocR5TcNzmh4vfdTq0cGLzUgiCyaFbyp-HLVt0dwNy6ft75NmTgbt5nc14qZCUE4gIY6plavDzuE40dvOFXUO1Jjw-6r__bvcsVWb77eAWNO4Z10cAZizcNPTvMYQ6lq8ITHzeo0CuplVYNXggLaYQC3u4cEkCwXVJfg3uFAFdx1zdgGiqbJbLvwl_mxbZHR3U61mc4UgPs1RBIidEgSANs1w7yUydAGy4kDoFhkzkGkmd4eM4uLZ4HFR_FpIWZofBBcuKdzc886Lr8acTr0y0QzP_LsNxbKNrPIP9nsnjNV4gBe214gd5NNAs0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=X7tvX5HXcmZzBXRWKSFGQnHOc4nocR5TcNzmh4vfdTq0cGLzUgiCyaFbyp-HLVt0dwNy6ft75NmTgbt5nc14qZCUE4gIY6plavDzuE40dvOFXUO1Jjw-6r__bvcsVWb77eAWNO4Z10cAZizcNPTvMYQ6lq8ITHzeo0CuplVYNXggLaYQC3u4cEkCwXVJfg3uFAFdx1zdgGiqbJbLvwl_mxbZHR3U61mc4UgPs1RBIidEgSANs1w7yUydAGy4kDoFhkzkGkmd4eM4uLZ4HFR_FpIWZofBBcuKdzc886Lr8acTr0y0QzP_LsNxbKNrPIP9nsnjNV4gBe214gd5NNAs0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.  او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6292" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aXOAtN_wsRyvijiM_UxCXvuNXLSJUrEgN9raLc7E27QnT-UhJWVUXppaw5M_GYQx582OwNnV_1zaO7mSW5ezNeMwjvfX7Tfm7JRcqEyQ_8tmk65tUf0eL7vPY8xZtw9lXnWWVjgcN-3al8HsOb_nGiA-iQL4BQGlDgUCoZNQHTbS16ouRaD9cDfwwDq0J9XW8SDg3pXhAEz6Qx6SoHgs-_21npi8ViwFc4VZtM-YKIiM8igEFA971eY-25AHa0ZLx0mISKagGlQP1EwBKQc3-1mO6JkjYvMNet34Pw9nFjgXGIjacogLu9F72oJY9Va1s9pPe4RqH_ZydV2D1mMXQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.
او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی جز فاجعه برای غزه نداشت!
تصویری از خلیل الحلیه، رهبر جدید حماس با خامنه‌ای. هم خامنه‌ای و هم یحیی سنوار توسط اسرائیل حذف شدند.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6290" target="_blank">📅 09:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pDi0Q3dIjVez4HTAPW-zl3k33tgQ3DtnH9XUeiH9Rvoc4x3CxSue9iyOiFPTtICFUmDIWJmPcsvZ_Ey5C2Jc7n7317-IUe02bobRf3Bb3cs2uo62MgVxCAK1UYtiRDX3HGD43d7zEqkZ5tMqUfjhj1_7YzS50kbiB_vOWL0F5PiOrfUPoGrEmlNpZhk_Fs89s4O4j9qP31LvW_-QN0JhA_BY8cMSoxgwlGIR9NqbAZfSISJ6ogRujsomlgvlYDuwbah56BaLhoJLyTtgaA9jb3AZmx99D4XL2fGt2iJFx7dsD5CxtrGzbbps8DcaRIl-rys-qdAC6Y9Pd0i2MSIRsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزیابی اطلاعاتی اسرائیل نشان می‌دهد جمهوری اسلامی پائیز گذشته هزاران سانتریفیوژ غنی‌سازی اورانیوم را به تونل‌های عمیق در کوه کلنگ منتقل کرده است.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6289" target="_blank">📅 06:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6288">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">یک ارزیابی جدید از نهادهای اطلاعاتی آمریکا به نتیجه‌ای رسیده که ظاهراً مطابق میل ترامپ نیست:
حملات اخیر بعید است رفتار ایران را تغییر دهد و جنگ در وضعیتی از
«بن‌بست نامحدود میان جنگ و صلح»
گرفتار شده است.
به نوشته
واشنگتن پست
، تحلیلگران اطلاعاتی به این نتیجه رسیده‌اند که دولت ایران احتمالاً نه فشار قابل‌توجهی از موج جدید حملات احساس خواهد کرد و نه موضع خود در مذاکرات را نرم‌تر می‌کند. این گزارش که توسط سازمان اطلاعات مرکزی آمریکا (CIA) تهیه شده، پیش‌تر در اختیار دولت آمریکا قرار گرفته است.
نهادهای اطلاعاتی معتقدند واشنگتن و تهران در وضعیتی
«نامشخص و طولانی‌مدت میان صلح و جنگ»
قرار گرفته‌اند. همچنین در یک ارزیابی CIA در ماه مه آمده بود که ایران حتی در صورت اعمال محاصره دریایی، می‌تواند
سه تا چهار ماه
دوام بیاورد و تنها پس از آن با مشکلات شدید مواجه شود.
Jonathan Panikoff
افسر پیشین اطلاعاتی آمریکا، درباره این فرض دولت که «حملات شدیدتر نتیجه خواهد داد» گفت:
«این ارزیابی تقریباً به‌طور قطع نادرست است؛ زیرا اولویت اصلی حکومت ایران بقاست و حتی اگر این حملات به مردم و اقتصاد کشور آسیب جدی وارد کند، باز هم حکومت حاضر است این هزینه‌ها را تحمل کند.»
مارکو روبیو
نیز آشکارا به اختلافات داخلی در ایران اشاره کرد و گفت: مقام‌های ایرانی به آمریکا می‌گویند که خواهان توافق هستند،
«اما میان آنها و جناح تندرو تنش وجود دارد»
و او نمی‌داند اگر تندروها دست بالا را پیدا کنند، چه اتفاقی خواهد افتاد.
هم مجتبی خامنه‌ای و هم قالیباف آخر هفته بر ضرورت
«وحدت»
به‌عنوان شرط پیروزی تأکید کردند؛ نشانه‌ای از اینکه حکومت در حال بستن صفوف داخلی خود است.
این ارزیابی دقیقاً در نقطه‌ای منتشر شده که وب‌سایت
Axios
نیز از آن به‌عنوان یک دوراهی یاد کرده بود:
ده شب بمباران، سه کشته آمریکایی، و در نهایت این جمع‌بندی تحلیلگران خود دولت آمریکا که مسیر کنونی به بن‌بست منتهی می‌شود، نه به وادار شدن ایران به تسلیم یا عقب‌نشینی.
به تعبیر نویسنده، جامعه اطلاعاتی آمریکا عملاً به این نتیجه رسیده است که
«گزینه دوم»
ــ یعنی یک عملیات نظامی گسترده و مشترک ــ تنها مسیر نظامی است که می‌تواند وضعیت را به‌طور اساسی تغییر دهد؛ در مقابل،
آتش‌بس ۱۰ روزه
تنها راه خروج از بحران است که نیازی به چنین عملیات گسترده‌ای ندارد.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6288" target="_blank">📅 06:40 · 30 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
