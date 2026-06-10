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
<img src="https://cdn4.telesco.pe/file/S7F72QmCcMignJQwYJ957PtKh_B6xkSLNPTi-Xtw1sxwipbJDiawWGBOtKlnalxhjy-WbOgjouz1wX326XOknVklEk58MQA0CmmYz7XVfM0Hs3OSV3gk458Bh5olzdiwb3p71Hp61iwJxufpbM_gJ6e33-Bvh37hOawS4kcFRmajkPWRKjsRqDcZn7MmBE8dAIr-XyKm5YvKIjJUilx4UWrk3uYVPGFr546HVnd7n_yfuXi3VVxckwL-a53UqftUG_so_VqP0ZQN5EtLjLDMkLfjFPqT0t9K2dtrZknaC9qqlEBVSOyWvj4SJ_0pL2ic7bj0_VgFSKSB8Jz48wskqQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 196K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-20 21:22:53</div>
<hr>

<div class="tg-post" id="msg-23136">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wmij3XhZs47TrPLIZco2LYSHr1xR4u5FSW-rS9Ng1iwuzmOwMAUPngkyesAcj8w4YtFqNw8DMs1LIgWTGPYVJ4cG3PxNpHfrVyVC2HhFig38TF3PfDuDkCBe_KA333yr1hyOyiZc1xwgU4duPk23-pIBsWhMMIlpeZdGjtZwU3BAXQHJqDfigMqVBra2PMNupzpHsgJ2jmWlQbaT0BVDWFzm0FBf0PRndvNiueFxWTMoyiXBBQpUzZa9WYxKSHkgDeE9jkKFPOBVhS6_sHsFszin5Bv0aFAUeSLxhprqYAedDpPLtPKPono8-W7J9SmnsL7f2Z6ydRsP7NWXhXy1xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این‌اشتباه درطراحی نیست؛
پرچم لهستان روی پیراهن هائیتی؛درسال ۱۸۰۲ ناپلئون سربازان لهستانی رابرای سرکوب انقلاب هائیتی فرستاد، اما بسیاری از آن‌ها به جای جنگیدن، به انقلابیون هائیتی پیوستند و در راه‌ استقلال این کشور جنگیدند. پس‌از استقلال هائیتی در ۱۸۰۴ ژان ژاک‌دسالین به لهستانی‌ها تابعیت اعطا کرد. اکنون و بیش‌از ۲۰۰ سال بعد هائیتی با قرار دادن پرچم‌لهستان‌روی‌پیراهنش در جام جهانی ۲۰۲۶، یاد این دوستی تاریخی را زنده نگه می‌دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/persiana_Soccer/23136" target="_blank">📅 21:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23135">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i2aARVeflnpt7xD7_eqyeIIhqGuzlHZyDRLn2IoLLZPNrsuo5hXiils-qc80246qW-GhWpkv_Xjnc5LqfoojqzvFWZIi9MrQR_vziBOR8adaQflEtkLpq78gJXxCzdyoYgRk-2hZITDEi-NGJCbCmAHzRvwLIDPd4Q7LdJYHbp-z37r6FuXWrlrgXE4fwv3WW6lddqHJFpYSGmBUPvcpqU1JwWEiuQvfcFGdUqBe0DZe77l3QLUCD_5B_r5sXGkF5PKhjif3P7GirmYg0S5mITr6wSX-Ny99hVSAM4_Ewah9GV81IgNhVYDj2KJde-n7A6AFCYb8DO9jf2U6i6-ztQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
از امشب‌اخبار داغ نقل‌وانتقالات باشگاه‌های لیگ برتر مخصوصا چهار باشگاه بزرگ ایران رو هر شب با جزئیات کامل و دقیق برسی خواهیم کرد.
👍
بارسانه‌مردمی‌پرشیاناهمراه‌باشید.قراره بترکونیم. اخبار جام‌جهانی رو هم زودتر از هر رسانه ای دیگر در سریع ترین زمان ممکنه اطلاع…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/23135" target="_blank">📅 20:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23134">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PpISbseG6uwieGEmI0IAeRpdvCYL3mklmookJjqxw5jUtVZeQ0P0DMsh1gQyj-8-IDxzI3PHfVDvnimEfkORdxD2WBmovTYqBqPA6PDsTBsFhBNPZwhZtu49FlJkgyqv5SXemgPK1qxaHAWaThNwidsuJhCIkuLrCAkKcDYgmPEE7fB3BLRWTohkJM8D-lWxpyQIRoKk1y4naN94SSq5Qwqt4R8YfBbUBo6D1BDNqnyLXRZFjIdIfTySBNcZNqJLPVn3qL7zZb-8X2lqpeIm4O75FXYBPdHfldFiMdey7dZkz-1iKLPEfg-xF3pudQj3bbnJWhz1aZ1v7z_3QqFPvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
مجریان ویژه برنامه مسابقات جام جهانی 2026 از شبکه معروف TRT SPOR؛ فرکانس شبکه رومیتونید ازماهواره ترکست پیدا کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/persiana_Soccer/23134" target="_blank">📅 20:24 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23133">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rE8V1hLB6-GC3piF2Rq9i9L2nCsZcTyMpMQJa3HYCpea5aMlNdz-8-03xiTtO_JyY4pjNEym5T7-k2gFywZBlXryqnNNO5VNNLDNRJqIy0uQMdMhSoJy-EklcjUa28AKnNWe-dZ2bZh-iRzcJf6Z_ZxdRCNN31uWVyoa7a0aFpZf9n73O_lCzeYkwHq-hf6JIzEEiu7-M4F586DWpEcF4gnUS5vHbZ16rrlWInTALdHHyFnzbnFBkt-ISjHNYEdv8UglfB4sQQGVbU5-QQcJvYS8fpE24FZIfnssBOhFj6XUz4iWjUWV5AUFob82hpxYFMyd4qixolIw9YLUC1V9XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
باشگاه‌استقلال بزودی خبر تمدید قرارداد علیرضا کوشکی بمدت سه فصل دیگر رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/persiana_Soccer/23133" target="_blank">📅 20:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23131">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/keZqUI1Do89dJ_uJkfvBsPRWLY2qJArgivgt4SHSTai4S3b0-l64GtNVL9OG62usGe2YH7tcU7y9ghhD_i2GW9kpxO7zVdCgkAfxPAFIEvqf5ExgE1preRLNYIF4XTlNLLT107-jy6kUKF4JQhfIgjj_zuUmklqRGDEMirnKIwJB0Pcn1D2-CjG941S19cjsybAmT4Obqo49oddObIHL1Z-nuCZntZLKXE-gw86toL6zRugx1-SlalRlAHcOwaZClBN5Tae1QkpeL0h4nXYAt8hMD2Gdibq62j6E90aPjSocfxQRLb-HC74U7bobtwhzPzj2qhRLkirLvUZ_JuomSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g-WrfYpMTcCOG9mIR-FfaXLWUkMP8dIfvl8IufvfIE8fQV81tExVosKcZCqUf2nRC0wVOs8-H_jNQS-GbNHpx1WXuj8j7PT8-hb7OXw5xXle8Kktph3ZnDY-FznKR6b4hMoffmQp8ijrfSqvISms2amezfe90cZM8jvL9BVqNSUX0KODLC1hywlflJB65aoS29B6W4l75_U0ztYaceTg0_FSoWFTx5u0ywZ5OoPflij_ruDjRCOGfU467FunbVLJmINPYtWAmpJIY54UlMAYs_VHQblKHP7tl7dKHddGYqi-OCASxW0PdrG3kHHckpBBd9Qd9fqLK_F-T2QM-IZrcw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
خبرخوش: تولد و بقای پنج توله یوزپلنگ در پناهگاه میاندشت‌. ‏«هلیا»، یوزپلنگ ماده‌ای است که در آخرین زایمان خود در پناهگاه حیات‌وحش میاندشت خراسان شمالی، پنج توله به دنیا آورد. طی یک سال گذشته، این مادر و توله‌هایش بارها توسط محیط‌بانان مشاهده شده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/persiana_Soccer/23131" target="_blank">📅 20:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23130">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e58078f0d1.mp4?token=U7IsHC_u1AsPEAHkQbhcITBl3qVDuYsP9RCPFSyMEoNPSPrWslA2hNPvGTbLvXEHMcha4nb-qGkD54CC05rDWkXa16Uhmawh1xxHEHdQV30i6mdxtapYSXaW7lIzai16kHMEo8ud9qfVqcFk8BHyz9o_uHDIHmrlS-G1u1rojaayBgjMVDZZIlz9CapUlkzUNAtf5jtsWNUrp5lam1u30bmV8MGzMK5i-AQJSPe6zYTFWgDWzSDVgzmOwzbWA2F1fzY-2a7q_RQeJIvn4DDTgTvv9L4_110fKz-l33ZzWnKYJ0JwWAYLsfRerWtv58oaz-itE4Q-2CB5woo9yRrUGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e58078f0d1.mp4?token=U7IsHC_u1AsPEAHkQbhcITBl3qVDuYsP9RCPFSyMEoNPSPrWslA2hNPvGTbLvXEHMcha4nb-qGkD54CC05rDWkXa16Uhmawh1xxHEHdQV30i6mdxtapYSXaW7lIzai16kHMEo8ud9qfVqcFk8BHyz9o_uHDIHmrlS-G1u1rojaayBgjMVDZZIlz9CapUlkzUNAtf5jtsWNUrp5lam1u30bmV8MGzMK5i-AQJSPe6zYTFWgDWzSDVgzmOwzbWA2F1fzY-2a7q_RQeJIvn4DDTgTvv9L4_110fKz-l33ZzWnKYJ0JwWAYLsfRerWtv58oaz-itE4Q-2CB5woo9yRrUGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇦🇷
حس و حالی که از آهنگ‌های تیم قلعه‌نویی و بازیکنان منتبخش و تیم ملی آرژانتین میگیرم:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/persiana_Soccer/23130" target="_blank">📅 20:09 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23129">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJn8UyKIRy54n3hgY8coHmLVtW87xlqow3NzBkMijRUFtj6Dt3J69nbRa093IrtnLVz5QqLRscSD9C2x2FXbmkxJbiRtPoHaFaJpjEtIqeuQOG_9-2mBQGi1Vuh9TWktVCuOyZdrX9PPIUQBSPu3ItecdKkLL3bhEemFKpOVRVHWuUmg2NEuLxLOgxMOzPeATDWYFy2nwsMb5zhVGpshlUcijPTZwtjjctorAG1M9VcY-7gQL6T5v1sMkl5Myh3_7xpdoxCUzvWybHqGdd779TGR4ofdXQumzwuIK0Tjen6qrsjIUCu_O_gE0xjmWVMyDiGN-Fj6Gdn4ljvPAczqIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕔
انتظارها به پایان رسید
📃
از سایت وینرو رونمایی شد. معتبرترین سایت ایرانی
🤩
🤩
🤩
🤩
بونوس اضافه به ازای اولین واریز
🔴
فرصت تکرارنشدنی به مناسبت افتتاحیه
⚡️
هر چقدر شارژ کنی، بیشتر هدیه می‌گیری
⚡️
🔴
تا سقف ۳ میلیون تومان
🔴
⌛
فقط برای مدت محدود
💣
بالاترین بونوس‌ها فقط در سایت وینرو
پیش بینی کن و برنده شو
🎯
📺
تلویزیون لایو برای پوشش بازی ها
🛍
بالاترین ضرایب ممکن
و هزاران امکانات خاص دیگه
💰
🎰
همین الان وارد شو و با اولین شارژ تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگیر
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
📱
کانال اخبار و هدایــا eg20
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/persiana_Soccer/23129" target="_blank">📅 20:09 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23128">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZ-ggHNAAC4zyuMPWAuDmJCJQFvj4FoT1Jdk7HDX70HBzqiLQbHmcF_-d95hR2hatOAu-KNbmCcBvui5IKHr3eR98afp1HerdQsP01xOjPSCib7hEJ850ky97KUifrxSEnhrDIyzDibIEeKpJSohZbxEPmTynLeBy5a9CY7UVRLEGnHGiACdB2BxhrDl5xdTqwbyljwWohMLSami26ZgqUREf_jN6Ql3Kr3dZryzyrZ-7BLbL67adhb2g2DslTK7NdBqg4yOxdoSTfpWn3VyrbHnBROc2ncfLE8K7kDDp0CJJHgIl4xVjieYfOyperQ8fEiWNGpm_xI6k0-GRpTTSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
مارکو باکیچ هافبک سرخپوشان و نماینده‌اش این هفته‌حضوری بامدیریت‌باشگاه پرسپولیس جلسه خواهند داشت تا تکلیف نهایی ستاره مونته نگرویی برای‌فصل‌اینده رقابت های لیگ برتر مشخص شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/persiana_Soccer/23128" target="_blank">📅 19:09 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23127">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sVbcQ0nGdBSbbuYJOSoVDr9TylwJy9Mw_w_3AwA_fXsgUnKvRsZZWKS4Lot7In4QmJwNYfMVMS_KNSNipPdYtWbXh-iMzrlcg6YUoWkEwYYcM-jSxA0unppqSF-ghIlXo7wpCZ-V9ysDGenrGv9zJexo1I7LErilgTwVNvtxdzPrHzhmxpJQma4gNhqHDxY6dONaT1JhLnLSM75bkchEN3lEDeLuq_yL_BhoIPTWheSMR3WtHSfgSTWpJAeIX9BWyOv8iLBfNSS4A9t_zbuZ0fOOEtqm2V9YImgvlc119ZjOKQs3QD_Utp69PrTOaiX_lOWIKc1HS-8Ry44mUhBLTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇺🇾
#تکمیلی؛ خبرنگار موندو: داروین نونیز از طریق مدیرام الهلال آمادگی‌خود را برای پیوستن به بارسلونا اعلام کرده‌است. باشگاه الهلال اخیرا ستاره اروگوئه‌ای خود را به آبی‌اناری‌ها پیشنهاد داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/persiana_Soccer/23127" target="_blank">📅 18:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23126">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B-tc1fid7QZA7WNLJ0R3_MBBbaezM0ztCbAb10Nau7z5MVEFIKMftHOQHFkWGn6M89mMxvNspecMdBK6q_VFH4PYQoSY_UvKYwDyummRpcvlzAqYYVgT5W7vJ2-x_M8B4I0teWl4gvVMhxZZ7rHEuQzLMxJ3OL_2b3SPyO30yaiT8Z3_l3vEUS3Kiq9Ax21S6uUcRZ4xj7Pjl8j9s_4SopgRIU1_AaI8m8Mwsrb6lC7WLQqtIAFsklSUIB-tgg-dufWFICAZsu6MvJj6jbjpZhaSTved0NWVpH_c-BFPWGNxUpnxc5vt5pJs1Ap_jfwnSxX8VZHShTHv21qhhylAhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🤩
#تکمیلی؛ رئیس‌اتلتیکومادرید: هر باشگاهی خولیان آلوارز رو میخواهد باید 150 میلیون یورو به حساب باشگاه ما واریز کند. نماینده آلوارز به ما گفته که اولویت او پیوستن به باشگاه بارسلوناست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/persiana_Soccer/23126" target="_blank">📅 17:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23124">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YOkixufHAi4gRsE9yokVrcxsDU_IM1V_gteRx8EZJxAL0S24z1u-DtW0WGxM8eJb9d4SzYk9q3aRQYJLoAIhyPCacpfSm2g1ryvZZWCS9uVK753LUHDuXCPvnh0CZlqJaPop3_nS0oo-Sz2quAD0I6JfhBQSYjQ2gfKK7zcIG7LAd4_dI28-mb_DskJ9hEEnLEzHBdXBe8P4Y7MouKuBrrBDhrP5RZwZ_fgwhDohAXVYRnfX3QH8MxTXNRwCelfYQbsrOVgvrOy4rik3FLOxPWyiB_hFFFWBxXbrDIlTmO4k-Hh9JUgBCWZ9_YvsBKkxzILHxk-JISNI1UX3tPGn8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aeqkWxonFAn5eypWDczGj3rcuElDpiV-3N56UIVKEppgWUGfHzlKDn-D1Ahqh7XdzPyJoUG_c_5j_-wpX5LVDDOoib7gxbjJ_BOk2gUGBkJiPVH3yVBYdFyipGfinVs7ZYif1OTkll5oCpQPWO8gXCchE5YLvVI10VmFn4gME6JXJjMiNPrBcWUCBK6V5MjvKneZGvNQANjHJsAueriYkqmrT5ym1_IZDlD29uUfpIVz4ktn_xDXRmMQn9vlCzBicyfgZMXmPTD-7aWRLWcTggXNTQEoB-hEzUM1suRRmfZ2jijQNK-LTqPzhYOSL5grdf20UGbH0pDzawHKQUIyIw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇦🇷
🇦🇷
درشب‌پیروزی 3بر0 آرژانتین برابر ایسلند در دیداری دوستانه؛ لیونل مسی کاپیتان آلبی سلسته به این شکل موفق به گلزنی در این مسابقه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/23124" target="_blank">📅 16:46 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23123">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MPvx_nKbp2P9Q9MGsJPV8hvjkvJ4Be-uiwSyApgpT4kI_EOlwKgwBPHgaAAQmkVqLYaoNGo6B_WNhV1VpWrtHdMhCSG51bIi0zHvXg2yDdCyHBNVGTMLDCMqMzvkMhWuP_hVSMo2RolvNCbEMN9qzNFm1FzTt9MO5DPcf1p1mV2a2xKaeYsG16xkCotvE9eooPH47NdPqRkTofOUb4tbYUK-YGtYHDHJ6ISL-7vbTY_xUCLhIHWHbcD14s1H0azs2qi4YvDWFKFByRjjXRL6XRLqiBIcc7VBYFG2qtnsSPeaqGG0xo5TgOwDknHprv3FtFdplkNtJi-aSU5MULA-DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درخصوص نحو سرچ فرکانس شبکه‌های رایگان ماهواره یاهست‌سوال‌زیاد پرسیدین. روپست ریپلای شده کامل ویدیونحو سرچ فرکانس شبکه مدنظر رو توضیح‌دادیم. الان‌این ماهواره‌خودمه شبکه‌ها سرچ‌ کردم مرتب پشت سر هم قرار دادم که هرکدوم رو خواستم سریع پیدا بشه. تموم این شبکه‌ها…</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/persiana_Soccer/23123" target="_blank">📅 16:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23122">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
میراث‌ترسناک‌ضدحمله‌های منچستر که بعد از یه توپ‌گیری آغاز میشه بامربیگری کریک پس از سال‌ها که توسط سر الکس فرگوسن اجرا میشد برگشته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/persiana_Soccer/23122" target="_blank">📅 16:12 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23120">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mnZE6Qec2JeTp6BFB2Sh7vts2ctiTzuofh-K1Kkpb6rlBxoumPFdv5Tqb7SSFFurt_-wJBHar11k5bgSuG5XvrpJ4kyFOO2Kzo-RHImh6ZGTsD458uAceak3Xn72z57m2ZHKR3lJWWWZRtUdXqjfFUiWy-kt-BC4n1jYnxEFsb0pL95uR8WZJeNbua-4Q9HugdR1Opa7t9qZ6nBYS_v7aD9oikWWmRfVhLH_UnMNAkgfNYOgHWhGIZN4S0lvhz21DE2pf8aerzc59nf0WWs_tTYMa1IXnFYC-QkGu48E7r4esCmNvwzRtlwkMewMmn6NlFCM2obKunbyUf6Mf-hxzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TgEhGh4r8EQF82njjeWc_dTYSEBpr7QxfgpbI6vG6jiWCUkZ3SY2IkYvQobdoH0bSdNHF8ZSHYtV2XBX246HJfLGQgbS4TWopZVDIXlbkovSrjeZ5eq5SmALQbpX42EzNCXzDi68bLyAI-EduvDPgf7S5FzmTF5mhzSI3FJLfrfrBjGQOsv1cMeM5dnRlK1wibMaqMIjW4ES5M1tpQ_yjK3NngDqbuczDMX82iL9DoS176ovWZVSIb9FqT1nXdcdON1Qvg3cLLI9QvjA5BLQoqOq5fQCR0YvSpOHA6Of9DAYJflzDo6InX93v3sAXc5fCIYHuSNt2LLgw4anAzjc_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
مجریان ویژه برنامه مسابقات جام جهانی 2026 از شبکه معروف TRT SPOR؛ فرکانس شبکه رومیتونید ازماهواره ترکست پیدا کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/persiana_Soccer/23120" target="_blank">📅 15:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23119">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hfN6yTPE5MWEgaj6Golc42wcTUk6w5Bcu759QnG8wdSwG0iQXUpGfgTU6bJmoR8YrVg2U-TxcP3W8nrwMAYEfAWBV0ugK7VZ6IflKvPn4odgkiAvvIq4eK0RVm-UuA9jdtZmoBugGJb00Hdu8_TTGcNMQn7JqpsAEIJu5GxCw4eDWlG68gKB-hcbplVgPvL5evbLBLN9_LSCSA1WJJ48D6TiersKrKqhXHaR9lMEpS_qu6Q8Leyrff8X8sjeTQqbZtNbvxYajFGYn2SvcpV0TmFjndJvWszUeo-WRjOeSV3_Gf17CSkLOyP9u_WAGH_vpDL0D8FSGEm5u1QZE4ikpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام نماینده مجلس؛ یوتیوب و واتساپ تا پایان هفته کامل رفع‌فیلتر خواهند شد. دیگ میمونه اینستاگرام، تلگرام و توییتر؛یعنی یه روزی در آینده نزدیک میرسه این سه تا هم رفع فیلتر بشن؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/persiana_Soccer/23119" target="_blank">📅 15:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23118">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C0uWg-WR75CbOEjoLnxSyj2oXkRoyyAk8f-xyYf4A24e9RTJ_W6GeQO-12UuK8HyRkypYVKUvyt49fEb3Hx5FxiO6gEd04xUDEd8hVHsgMfNmhy7p3RBARpVUoIGro-0z0NLLlZuvaHo2FOBjMrllcEETcY_pC8OQUtcl-jSMINcYU959nPHxXWxoOZ7q__BrrC4G8snAoZTLIWglKXcwLU2cYhkUnuscUOAMYmKnoRs1wPIqdvkPsYZdaYw9D-Omh74In0Zi_F_i3miynfFInmLWJxMF7fP4qXpwObXmeommqB2mwzvQfXXnsxVzzloKEfPzgKNyqHay-8vHgT_ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇩🇪
شهربرلین‌آلمان تازگی‌ها یه مکان برای شنا زده که خانوم‌ها در اون مکان حق پوشیدن سوتین ندارند! همونطوری که مردا سینه هاشون پیداست خانوما هم مجبورند بدون سوتین وارد اونجا بشن و شنا کنند!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/persiana_Soccer/23118" target="_blank">📅 15:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23117">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ubt7G-e2Y55BOsNYiTq8AHGD7fa2eXzcqxieyAZ-fh7BYsJbdankqHOSeiKQ_x0WM79QtkdfnxMDjbq9X9X_QWJOpiETU3hDd-UsbLQEL7sZcfryLmMK1WH8xbCbEQaAF9lpLx7qdtpxOBnYUIu5gGi-QY3BcH0M8n5zHFNQbCwU_LULUrXPDGpuZA9db4UHzUcaw6OMg6lfKVt1ng7LbgcFk6YxTd_t7cHuMO97MpyOY9bFkJO9T3MS_A1fwXG1dgI9KPhsqZFGlnDSN_F2QddpmsQI-dYHroG6AJvxFCqWhnnuXS6Erirp1z8aXyh0E0lnkmHaZFeqglx-Xp8DwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
⚪️
🤩
#رسمی؛باشگاه‌اتلتیکومادرید در اقدامی عجیب پیشنهاد 150 میلیون‌یورویی رئال مادرید رو برای جذب خولیان آلوارز رو کرد و اعلام کرد مبلغ رضایت نامه این بازیکن 550 میلیون یوروعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/persiana_Soccer/23117" target="_blank">📅 15:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23116">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I3QXDSMthlDE2zKBDr1OEb3lSr5s6XNI2iCHdXv2Lqxu19Q_q1zZOLTOpz2En6AS9zAYTpJKd7MsOWjDv6KVHoXD6ekJG9KevBkJEhqogOQYG039oFskmkkM9iQ7E77QAzdWqYgubNhNce3VzL4yhyqHWwEgzVXsZcU6q4R4G74Nb-n4Cqpq2AfK3MraXPGIaGOTOeS4wUBlqlA0ZpAj8fc5l8zIeR0MSzsBmxmaWqmI5UT0c2S78BLfp35V9EzdTPPifJ6Ye-Su-ndZUIdh1O1O2i0MRTcPtAgnYMaLw1KqgvIVCk6pAfh8aLf79kJj3ba0NcrnR-46Q7pnLZX_DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ دیمارتزیو: ژوزه مورینیو سرمربی رئال مادرید از پرز خواسته از بین یوشکو گواردیول، ریکاردو کالافیوری و نیکو اشلوتربک‌آلمانی دومدافع رو برای فصل بعد به خدمت بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/persiana_Soccer/23116" target="_blank">📅 14:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23115">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f4HyyG3mghZSaFcp7GeRB_4Dum4_Jir2AXdbChNnOiujTMmabl5jUOJacmAicUch2-nej-hxqXuficrqiTfcNdsKTj7-K3AaA6Azhf6siXfuVY9Z7Prhi2AwOUgRsWjCombRaBj9Z1cP_pFdP9a2jsDb9Xx2VkKaBEgt3mrchVY2lwRwHZT6_Kkhue4LCe8wS8AJQsM7yyCBIy_COEychUKIxmYehu-87GwAZQuelvoOeUO2KJGKQm43_lQrtVTo_4EtrpQGbjIBM6MdRJPpWvb-PFJpTL-wXzM4mF4-qU-dPCRhtw_shtHnD1dw12Kud5YFS4cRd0rmap6-LS0Gsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
نشریه‌مارکا: بارسا تصمیم‌گرفته‌که‌بند فسخ قرار داد30میلیون‌یورویی‌مارکوس‌رشفورد رو فعال نکنه. بارسلونا به سران منچستر یونایتد اطلاع داده برای خرید رشفورد نهایتا 15 میلیون یورو هزینه میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/persiana_Soccer/23115" target="_blank">📅 14:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23114">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qn-AThZy_ITnM7ywhTQ06AXefEu2BYKM5-_Ixs-3FlECkxkCZOp9MHnv6MUHqrDfcJ9q7msv3eP5ueFeyoxSS307H-lxucjr2ZAt0WfqPQAG8bLRf5bfmDZU2j1aIemCvX7w2Uc8y0cVyhJDIEzElK_CK1LX66FNK_Su5iMjUpuGkpZze7IKA5Ks1i8Bit8-zIUPFnweQkd5WB1qgtsGisR9ku1bzc0nDAdXt20M3jh1n6DXbA4gpkmjpZmO4tdU3a0gtBA0cdsKoe9HA4Ud7v9RZKNy47jjDI1HFdyVLVE10q1i2FxPmaLRlo8Wfsdmi9Ezkcc6NM_jSBEPBwXSsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ ایجنت محمد جواد حسین نژاد به باشگاه‌استقلال اعلام‌کرده‌مبلغ 1.5 الی 2 میلیون دلار برای رضایت‌نامه حسین‌نژاد کنار بگذارند. خودِ حسین نژاد موافقت خود را با عقد قرار داد سه ساله با آبی پوشان پایتخت در این تابستان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/persiana_Soccer/23114" target="_blank">📅 14:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23113">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b4b886447.mp4?token=FWvQPRbaGrRwrlH5hy2vPMtC0dOA0i4QB0gIcnDQjNXDISspbnJYGEnZ-TSo32kvvPNQkvhu7VKlUz0q-L2Z3vWRDb5GzgqDRy7_hVoVthR3AGaUuFVYRizPtUKNUCZvXfRzcqUB6QiyLWSs0itw7UwZ_GpUjaG_VMaSYUU6_u9t3W4qrOxWnxQl7ANNfarEgaqWlSsX5az9__wKjNHdGHSYfVmTurEOKWrmjXNeWM2u7KKhFAXy8bczG1KWq7X9Pw5_XklVBIiynyhUg-jFK6D2gN7p87j3Zt6ppgcIQju99eWwvJwYH7SR_-SxPsOCxp4v8o64S-89wJ5AOMvC14WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b4b886447.mp4?token=FWvQPRbaGrRwrlH5hy2vPMtC0dOA0i4QB0gIcnDQjNXDISspbnJYGEnZ-TSo32kvvPNQkvhu7VKlUz0q-L2Z3vWRDb5GzgqDRy7_hVoVthR3AGaUuFVYRizPtUKNUCZvXfRzcqUB6QiyLWSs0itw7UwZ_GpUjaG_VMaSYUU6_u9t3W4qrOxWnxQl7ANNfarEgaqWlSsX5az9__wKjNHdGHSYfVmTurEOKWrmjXNeWM2u7KKhFAXy8bczG1KWq7X9Pw5_XklVBIiynyhUg-jFK6D2gN7p87j3Zt6ppgcIQju99eWwvJwYH7SR_-SxPsOCxp4v8o64S-89wJ5AOMvC14WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
اسپید یوتیوبر معروف رفته‌سرتمرین تیم برزیل؛ بهش میگن شوت بزن اگ گلش نکردی باید شنا بری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/persiana_Soccer/23113" target="_blank">📅 13:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23112">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QWqIaJoibJZpydx-wY4dnG6DOxJDY3Kh8OTsCgDodyPFDmIK4Fmz_ipcrWnAper9HXd_3taphRIGO922E35odezWxAZcfELV8VXL1pHkvGQD7q4Jw2G_OWYxtEyb2nPRcGqfgixr-i4HsTcEHEybWgCzhR4NJsB4QS9_GxfDSLPs0qdsVGhIjAWnaumZBce_iw_SaRBnhgKCijXMoElm1QtiE5btg3tU7n6KRfdh1-cjjqa-1ruIzDBk_Ko3kwD_sS4gweX1nlkW6QyogZgliA0uY19uQDqZk2Y6B8Cb8sU2I9cIY1JXKnX2KSyTl3OeUaUQrTfpXuu_jaISh48tuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
نشریه‌مارکا: بارسا تصمیم‌گرفته‌که‌بند فسخ قرار داد30میلیون‌یورویی‌مارکوس‌رشفورد رو فعال نکنه. بارسلونا به سران منچستر یونایتد اطلاع داده برای خرید رشفورد نهایتا 15 میلیون یورو هزینه میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/persiana_Soccer/23112" target="_blank">📅 13:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23111">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mVNmRPlt_bPTFQT8D5uurEueZs--AILFuA5qA3p3aSC-9FoMFvn5oWYWvX5wLlZ3oF6fRN9dOUlnHjsHwZvcoRK_xau8QS4JTTSvZ4wcVTcEib0MN5GajQopmcFKBbOzEfKWmYP0GHNhRiiVSuvbelWouqgd0VGuHZwnQt1Ojbj3AoiYjTv1-ad11gQGr6Bms1SkZ8If_dE9U5n6vdB4aI7GhsEKamNF15h4l75NEVfrP_FyptenKYZyT5WDtkfHg1JrkdmKG946lM6eRlCZhglyWty171HP-34t8qXpp1GXKE7xPKTsL1-qb89_kQhuOYeUEOFbK6qvfp01sz-RDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات|بارسا آمادس که ۱۳ میلیون یورو بابت فعال کردن بند فسخ قرار داد رشفورد به منچستریونایتد پرداخت‌کنه اما شیاطین سرخ مبلغ ۲۲ میلیون یورو برای فروش رشفورد میخواهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/23111" target="_blank">📅 13:19 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23110">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc9f0297d3.mp4?token=DdjEM1MNbsu_i0jgQ8f-9MYnQcB9DqM-b8QSH0E2Rlf0qah4uylPh3HEP2DqNoUBfDbx2oTf9foRxV39O077kMAlBv8V4UkEKsJKeyvgcfrI_NmbxjQxduIJ6idl9Dj1obS4-PL7T9uzJcDYvjZJ1cj7NxTqDuR2YG9dZfnlO8fowVpHJYLDxNR6uR7phaO0-PJwnjyiOs7npCJzG6OqXLpx6gPOTgE-AaNZDAlSzVXxLMyeK5HTbcOwoAHkiYxYDVWic2D_LESFNMiKbI_H_bZyXcGbN4Yzgrf_ahnotOuKFYvkgf1Ukw8LJChyQOA-epKDp3CdDuObyWo_ir0r5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc9f0297d3.mp4?token=DdjEM1MNbsu_i0jgQ8f-9MYnQcB9DqM-b8QSH0E2Rlf0qah4uylPh3HEP2DqNoUBfDbx2oTf9foRxV39O077kMAlBv8V4UkEKsJKeyvgcfrI_NmbxjQxduIJ6idl9Dj1obS4-PL7T9uzJcDYvjZJ1cj7NxTqDuR2YG9dZfnlO8fowVpHJYLDxNR6uR7phaO0-PJwnjyiOs7npCJzG6OqXLpx6gPOTgE-AaNZDAlSzVXxLMyeK5HTbcOwoAHkiYxYDVWic2D_LESFNMiKbI_H_bZyXcGbN4Yzgrf_ahnotOuKFYvkgf1Ukw8LJChyQOA-epKDp3CdDuObyWo_ir0r5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علیرضابیرانوند گلرتیم‌قلعه‌نویی‌وقتی میبینه باید مقابل دوکو،دیبروین،صلاح و مرموش کلین‌شیت کنه:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/persiana_Soccer/23110" target="_blank">📅 13:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23109">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nwY37agm-nxNNHque8yc5Gs4MEQC68Ozo7dQLa1pZZqErHc70iwFQ7FuhffCtavCoeXxUItsGPHOQ7LJnR8pyQ-ozSQUW_z7JsPR_tGlD_OLUTU0cP70KAQuX3L0Zl75dwhiBL1LUfkbdKkDOHkdVYoKZf8s8vQW9A_mIGOAGP1vKn9KB7zlJHzZ68GSc2hxn8l-I_Wwqr9yx7bkZjtBV6kgO0-Q4E3gW9_7rZblO02NyjoYzRzBpeOv8h4QoLSmw74sCfCU0A0U7ToEm77TuvbC7KjpABsGUUM04svlmp2FRV7QRsYv9VTXwq5zCgbkcTrSFeLpv7W1esGEUCjBKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
دیمارتزیو: باشگاه رئال‌مادریدمذاکرات خود رابا باشگاه آرسنال برای‌جذب ریکاردو کالافیوری آغاز کرده. کالافیوری خودش برای عقد قرار دادی 5 ساله با کهکشانی ها با پرز به توافق نهایی رسیده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/23109" target="_blank">📅 13:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23108">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RMgoqCFQmv_z1wKMw2NLYNHiNEgg-xRQVVKP6gB3vv_qmiiLwg25PgX9JT4lEE--dqLToDtk1Q_cDtownqvIUmUWpr5gxDMahwET3VtRN4bC7yXvgJCHcI7lYvQxpy6rEqWZcVE6aT17c0ooaKYRWRytsya9RXhLirz-hL3QCYG5HfWYtvc5VtWjE5-SSv9WsaIztfEPtQsOcK8lQDkiVO2AAeZVk_FGaWvG2vC8Y_hgvOsj5RW3TckU7WEJEcizdX7LBW4ov0ynRBa82Aeo9-hLesGxgJcjwV991kfpVxxiLxZcGpBgRHP45vYaRkX-LamAFSzMIWKN2l36F3vFLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕔
انتظارها به پایان رسید
📃
از سایت وینرو رونمایی شد. معتبرترین سایت ایرانی
🤩
🤩
🤩
🤩
بونوس اضافه به ازای اولین واریز
🔴
فرصت تکرارنشدنی به مناسبت افتتاحیه
🔴
⚡️
هر چقدر شارژ کنی، بیشتر هدیه می‌گیری
⚡️
🔴
تا سقف ۳ میلیون تومان
🔴
⌛
فقط برای مدت محدود
💣
بالاترین بونوس‌ها فقط در سایت وینرو
پیش بینی کن و برنده شو
🎯
📺
تلویزیون لایو برای پوشش بازی ها
🛍
بالاترین ضرایب ممکن
و هزاران امکانات خاص دیگه
💰
🎰
همین الان وارد شو و با اولین شارژ تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگیر
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
📱
کانال اخبار و هدایــا ea20
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/persiana_Soccer/23108" target="_blank">📅 13:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23106">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZH9o0HzbBx-a5lbFPw-OOXlz2ORSYmm3rDeXsIG2YRnvEW6Ub5iD5Fyq4LdHVg7RhHzdHB5hF3Z7X13w65NvBU8WM42RDc4sjikaRPHQHNoVvkfErkbticssYa2T4m-jnHaF-JZutCanxQ7qLHTsaErqASpr8LSIIxVlULPHHFJYXG5mWsvoQoEm2_BOhoqZbNepKT-mAvuKPgKzHKZJBpJRYTSj-AQJJZQeEDo40GrekShcbIRhoSGYeJb9MjEPxeukmy0-1DOiYTHbnatNgCKYsMgrCNeg560eTZXBoOK_11wMn5NFk-Yag66Dxxt8qWl7G5sjI3Ah0VwfA46v4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
فرداشب و پس‌فرداشب‌ازلیست دقیق ورودی و خروجی‌هردوباشگاه‌پرسپولیس و استقلال رونمایی خواهیم کرد. اینکه‌این‌مدت کامل همه چی رو نگفتیم بخاطر این‌بودکه ویو کانال برگرده بروال طبق و همه رفقا آنلاین شن. فرداشب از لیست باشگاه پرسپولیس رونمایی میکنیم. پس‌فرداشب‌هم‌بازیکنانی‌که…</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/persiana_Soccer/23106" target="_blank">📅 12:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23105">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r3Qyqt0YdtCVrUYdtc453mr5WkpCD0nhqUENDuoLnJ3iDVULqvoZCreWE1PQCI50nMRZunDzYBWW7VB3PlLO4i-nc_9lP4x7ZZIP-abWjmC-drwc3QUSbd_vhuhHKPMUs5QWYmfTqA7b89kdmPiksMwhk6xezPTPrq9zk24CYZGOw_EZOB7hIlQTPfcIdSyXRluKd_TiOhDCQ5crGHm_gFSdwkd64MxNdw9vvBP0c6QPGgm8nWAJluLiwUZLsuVICT3UJoSwf8ew5GG13RJiJ-N7gzZRpim8Om5f03JRQQWH4f7kJgFMp0xORoyHQocbQ4g0XkhA-AGlzV9uyMPx3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
کنفدراسیون فوتبال آسیا AFC نمایندگان ایران در رقابت‌ های آسیایی را اعلام کرد که استقلال و تراکتور در لیگ نخبگان آسیا و گل‌ گهر در لیگ قهرمانان آسیا 2 شرکت می‌کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/23105" target="_blank">📅 12:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23103">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gi0swB3TUr3riUyQjNNisMUTnHMC-58DZ65_C31RXAQhu81yyYuP7BUzgP_OwFoEKUXaji-tgyK8SaNtbE6lB6qzCwGt-kS3G7UXLnhcipToh87AL1VShu5wD280iHkILHYYXgMYZ-N2S9VCDnPcEJuNaoBMW_cGpavJ_RUocyobpzdcJIPw04f4iaUbfnM20hGiwOqr8sT1xdfLTZG5okQ2aK-m8iyT-2jIP9B6FxsNad4fzFoaYcMLQtzVE-sE61xg9GsFonWUpPAXVX4Hj0NtzRgkhdYdA8msKbh0ebX-l4DeULoPbP5iAWwUEYtfYJSrTsWbQRo96JbvWp3Wgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PBMbgEPuIhSq3BlG2VZBQacbTWWoMyCDRxTVVy8fXIZ-ORCsyTctcKDeBLdJlmIOkjY0gc8_Zr5fbkNcQinN56CYZIMJAup3LJIcEjx1jttUio3_o1oqUaPrL-PKdyBeBiO09y5rp_cKyAF2EuMR1LXHcM6lGsLPExjL-iWGhhiA-fZ0yrE1CiGQg5ktKZmzxefjp-RUvw4ZirJZ4I0R2iCgbhHNbOrbElRmTUpr6Zgd-4fQK7NWNX6UFUIO5wqQdtCN6rWzZWvnk9HqA5l6n3Zg7d_aNkqYEyUhsjIL6CHRP9YIWjn7NTC_2jj200Tf8-sxUCWTwNiph47l2z0S6Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
کنفدراسیون فوتبال آسیا AFC نمایندگان ایران در رقابت‌ های آسیایی را اعلام کرد که استقلال و تراکتور در لیگ نخبگان آسیا و گل‌ گهر در لیگ قهرمانان آسیا 2 شرکت می‌کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/23103" target="_blank">📅 11:49 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23102">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g0kAPUaFmF2wIZcFAZHI43ebOkouokX0GyDdoltuYOpnar28u4FWDMML8tcHVPUrppDDtG-1ivuPHJDTphUc5aIAl1qPc11HKBPHNOgmwqwf1kWmZ92iEJlqd_Z3yT8g1PnAqb0DoSGuzp2MHHrMkLGAcuLaKUCpMIk4gxdo7bFrOBcDGkHmRfT2dsDhLV-nk95Z592dJU-l4_OD7szGSRFAyhmPZyfZZiDa4xMaAUcBJ14XQY2SLC7RKalqfrOc3mpZlRmS3ogfZMrntNhGzZJhpU_JcR9k0ZZ4AwP7iJ9npztSKrqdTZdkCj2uw-U3u_VydPZRU2tsUdjIOojchA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
آب پاک ناصر الخلیفی مالک تیم پاری سن ژرمن روی‌دست‌مشتریان‌ویتینیا و ژائو نوس: این‌دو ستاره رو به هیچ باشگاهی با هیچ رقمی نخواهم داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/23102" target="_blank">📅 10:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23101">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S4QZx5jOKpthkvj-13ZEYO5bEXQVBFErHXoWhpxdjemwVBO1DlWXn5njoCvPLCG36d86kNmHdmpgn5IKGWDElhfA9-FCLgVBmQW-FbMEa0kCJGMmdacPCV7VH5i6TJsBTDoiutBojs4yMwb2BuAW5rQ4XaD4KzN67CqiSsv8_yGHO45d-jpTbeKPrUvwGGRBwm1vdXs7WRESlQr8X6v8hvTCWn7wnhqDOJPLjN4xIOQ07cnFCijI46xgeDlj0iZ308VrTPsV234d-qY1Ksupa6E31Gys7i1oPA31wPzyI1wvat6jCtQ_xtHdlYxzzjucd6kAyiTOJ5FMFvFNyYEj-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دنیل گرا مدافع‌تیم‌پرسپولیس با دریافت چهارمین کارت زرد خود، دیدار مقابل ذوب‌آهن را از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/23101" target="_blank">📅 10:27 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23100">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86dbb1bcb5.mp4?token=TLjB_zVN_zRHGiTNkuUN83zgr-VzpWGfkqY-IbqRTz0HbYER4fpPmHCxKvp3WtBSXRk3gJfX1TElQmG0Xvgke0kIVbY9-uk8AATzhwiwDS__Sri0_0Dl-bl4Q6yEWWMXMpGLPqn2l6EXYaZlWGqCI3gZNQaP4bby47kShMpuCx0sIbeU2tSWPSFbN6QJjyiPM17pQ6aANTIsa9Ak0mWxPqXIUmtcz5LH0XxoOy7Rqd3OonNeUq5KozB4qBP5thzcCWzZfgohtQG_Ecq8G4eT9Z9Lb2cYWRSnw_ZG2WmS9m3R6L8R7bybTeK6uD6bKhuXnp3ly5crXjQGMPlGYnwldg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86dbb1bcb5.mp4?token=TLjB_zVN_zRHGiTNkuUN83zgr-VzpWGfkqY-IbqRTz0HbYER4fpPmHCxKvp3WtBSXRk3gJfX1TElQmG0Xvgke0kIVbY9-uk8AATzhwiwDS__Sri0_0Dl-bl4Q6yEWWMXMpGLPqn2l6EXYaZlWGqCI3gZNQaP4bby47kShMpuCx0sIbeU2tSWPSFbN6QJjyiPM17pQ6aANTIsa9Ak0mWxPqXIUmtcz5LH0XxoOy7Rqd3OonNeUq5KozB4qBP5thzcCWzZfgohtQG_Ecq8G4eT9Z9Lb2cYWRSnw_ZG2WmS9m3R6L8R7bybTeK6uD6bKhuXnp3ly5crXjQGMPlGYnwldg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
درجام‌جهانی 2018، آلمان، مدافع عنوان قهرمانی داشت درآستانه حذف قرارمیگرفت و در حالی که 10 نفره بودن کروس دردقیقه 95 این شاهکارو خلق کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/23100" target="_blank">📅 10:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23099">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🇧🇷
👤
به‌مناسبت‌بازگشت نیمار به تیم ملی برزیل؛
ویدیویی ببینید از شاهکار‌های دیدنی او در سلسائو
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/23099" target="_blank">📅 09:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23098">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nfuZQhdmqk15qa4zYD8iOK6nzeexMmoTaBHYlNoDFFbUSW7_C8bmYHVUO2oN-w_LJf26KB6bf91SQc-Aw0GbXcYQqWEp5RVFeUemsCfJVIZkGO2Kk48On5r5OWfWh-R25w_H4Dbz8qG89P9vuOx2N_REgeqZ0IqMYsAatkoVEqd2ktdB_jwaL9o1NtxF5Yh5zo9I7INx7dlkb2Yoef4df-0sfBTC4as5MeZSU_fSthPrkHBez5E6aqhZVH1ipXqJ6ChWK3uyhXxt2yLbTLCYJO2j3rBSCXW4ZJitMtJ0euIQojqyVfyGIN5H2RC-T63GaljqTUdJM4qGvPGNgBrDEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تمامی جوایز تیم‌ های ملی در رقابت‌‌ های جام جهانی 2026؛ قهرمان 50 میلیون دلار میگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/23098" target="_blank">📅 09:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23097">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W2YWx-0NJ5v9FcVdT6U-ZsxvgzFm8tZSPGHvJ13OMybLPEOkWKq4QjoZl6PjhZkHTksDJPwPIXl9a6cpbqkQCPxTLsYYwTFoQwHXWwTPYNhqj265LwLQw4_Ggo_yuC0rdPWtyJmh6WuBceiWbBgzdhPlcSGlPJ_P51vKv8CwvH0vDLz5_EybrkDPHNQPcgvTfB6QTJ4LGAsBuHEkOV0tzjQotoBGcilnfFAuf4wVQxNSpK5iv0CxeX6vLqQYXv3inrAjrwhxGz6iJ6Ts2StYJuFr5_JaDfFr1Ydl5s3jUtBkS2AGHvwg0zjlOOG-MEbBkCztJCS1QS1hjjdGy_kGnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇿
فدراسیون‌فوتبال‌ازبکستان:
بعداز MRI مشخص شدمصدومیت ماشاریپوف ازناحیه کمره و این‌بازیکن رباط صلیبی پاره‌نکرده. براساس‌نتایج MRI، مشخص گردید که فتق دیسک بین‌مهره‌ای او عودکرده. بزودی میزان دقیق دوری او از میادین مشخص میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/23097" target="_blank">📅 09:08 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23096">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b8bf04818.mp4?token=JU5xp1SaDwco_fvejxsRdCozX_YFSxzOiw4-FG1PnTVQxWJuOWyDVxNdAXv15gOnXFQ1EfR2ns1Vp5NTjTEe5brMTUBdXD85uAPZ9mi6yP8DLjeCv-I354u0yasQsW3BeDXJseWU3c-8D60Kol4Hykaf3tvOyPqIDKwc1UYOrSApuHKN_8olZ4ORibkGh-viE7igizrpDczKAmUaFvbo1ShAKqb3ow-sN_o16PmNB9JyKZu-YFHnhd2hpklIBFnBzZan_b9cyySbkvLcyu-tnxov3nbFf3ZcEudr1vJii8JmQgpE3WoCHGnUsC3yntv7K0Etv8_uuoPIAGHXyTLpVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b8bf04818.mp4?token=JU5xp1SaDwco_fvejxsRdCozX_YFSxzOiw4-FG1PnTVQxWJuOWyDVxNdAXv15gOnXFQ1EfR2ns1Vp5NTjTEe5brMTUBdXD85uAPZ9mi6yP8DLjeCv-I354u0yasQsW3BeDXJseWU3c-8D60Kol4Hykaf3tvOyPqIDKwc1UYOrSApuHKN_8olZ4ORibkGh-viE7igizrpDczKAmUaFvbo1ShAKqb3ow-sN_o16PmNB9JyKZu-YFHnhd2hpklIBFnBzZan_b9cyySbkvLcyu-tnxov3nbFf3ZcEudr1vJii8JmQgpE3WoCHGnUsC3yntv7K0Etv8_uuoPIAGHXyTLpVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🇦🇷
درشب‌پیروزی 3بر0 آرژانتین برابر ایسلند در دیداری دوستانه؛ لیونل مسی کاپیتان آلبی سلسته به این شکل موفق به گلزنی در این مسابقه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/23096" target="_blank">📅 09:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23095">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85fc2cb234.mp4?token=itN70rr0f05wtmw9fW8b0l-fQ9ojhwu1WIPLINe5up7cqa6h7nZG7DvpmUbjZlaAu1DjGNUUjKqUKeAXoa29FQ81E2xEP-_F1qEn8vf9UsHLQzs6G25KulhWTKGaIGr5iZ5qghifykbYn3kgzZz5OjTd0gjFNpL-6zbjj4ztbXOIsEWnhg0WXiRqFq0uslVm6YwlXuCJ8ejL0SQcdrmLsc7CXFEW8OcXna7cMOXGyYu01zc2WBtX6AFR2YF91cJ9DvOONrS7CyRCmwL9kvvnM_isyqdN-pSUI89aNBwYjVqdvUeTIgWUl4DlVAAYcYdRpNPC-6FGudl3d4izpWXOcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85fc2cb234.mp4?token=itN70rr0f05wtmw9fW8b0l-fQ9ojhwu1WIPLINe5up7cqa6h7nZG7DvpmUbjZlaAu1DjGNUUjKqUKeAXoa29FQ81E2xEP-_F1qEn8vf9UsHLQzs6G25KulhWTKGaIGr5iZ5qghifykbYn3kgzZz5OjTd0gjFNpL-6zbjj4ztbXOIsEWnhg0WXiRqFq0uslVm6YwlXuCJ8ejL0SQcdrmLsc7CXFEW8OcXna7cMOXGyYu01zc2WBtX6AFR2YF91cJ9DvOONrS7CyRCmwL9kvvnM_isyqdN-pSUI89aNBwYjVqdvUeTIgWUl4DlVAAYcYdRpNPC-6FGudl3d4izpWXOcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحنه‌ هایی دیگر از موزیک ویدئو شیدا مقصود لو همسر ایرانی خوزه مورایس برای جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/23095" target="_blank">📅 01:27 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23092">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hSREuObA7hTaB9z3-b0S7FFVQpuRjEhL6P3W-TnprdkiLSqkBfX20ZHyCcLxYMNvM7JsmxVolZ-nMz7Lq88AYhioWmMKf_kUPkSFn3Lurkw4wReOi-6HVxbjjGbktTu5_1AeUnH32jZA500rix1pTg8rsubU-AvB1d4TuwkkkQKGrIUllgAki6l3GQ8PjyoPZ-WWNQNx_-Hyb796F-IzaZuJwPxwGrX2G2l7UasJtRK58hYhwbN8ddZ8lqn9rIK3UcDzkuMkAW1tyr8WtHl3H1vEt5BKYfah080gh5VUi-nIhSbhXiw_rcMilTXthblShNZz4VBF6Xn7Nw6wNlJKQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sY3DPwn5NmO0ip8IzI4M_3TUpTTDEceZ1WC0iObcFqLZEdWetVlG97ljvilno_ni1nNc5Eq3ju_pbha-obMC-6I5IRnazECM_HiwC-xSP9Qh9PF7FNEbwF40NNO_7Lp5ICbun_vdRZeHrQ8CBJX6rHU2NNKPSWJXcMF57DqdiQV7C1ZHfoyv7SFw1TUUbE41_gbVjHtasdWceFcGsLAZfvC_O5ZZiPRYOrQPwHWZakeJ_t_JqzMEb02BARq6xPE4AqLfNZPTh4cXzWsMuphHXsmjhE7-x66RmGQMQ9pJIIZCv5Z1kxWiSw6uYzx6X9tONIX_4W0alNZUbiwisNivYg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
نتیجه تک دیدار دوستانه مهم روز گذشته + برنامه مهم ترین دیدار های دوستانه امروز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/23092" target="_blank">📅 01:14 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23091">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7865bde240.mp4?token=HA4d4fv7K-1azLzlgghx3fgS9uZ81sy0dnRWZKbPPBZursahM6Lm1gu65vEsGRQ8KGY5Q5zu_bVnZ5xhK_6AFRtThtnUq8N8fkMKX1ifQZkVB8YNoq983MzZPAhpO84WjNARuv7Msk9NmnRqYwMCZW39yYO6ILpvHy29xxK6jZDAdhTDRCFOtEYsn4nt2lKX9NJJMZyW_uAI9eVcxgX0LAKrpn_x-62nVWnT0IwEwzv9Ywd_JeHoGw-T0TtVLf-mcSlCI9HymZmmgcutsk1P6EICJloTbP6nzeP_hVq0pt0Mue27b8D64EqA2C61sAUMK5tFYtjc6Z0CbeRD4qUZng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7865bde240.mp4?token=HA4d4fv7K-1azLzlgghx3fgS9uZ81sy0dnRWZKbPPBZursahM6Lm1gu65vEsGRQ8KGY5Q5zu_bVnZ5xhK_6AFRtThtnUq8N8fkMKX1ifQZkVB8YNoq983MzZPAhpO84WjNARuv7Msk9NmnRqYwMCZW39yYO6ILpvHy29xxK6jZDAdhTDRCFOtEYsn4nt2lKX9NJJMZyW_uAI9eVcxgX0LAKrpn_x-62nVWnT0IwEwzv9Ywd_JeHoGw-T0TtVLf-mcSlCI9HymZmmgcutsk1P6EICJloTbP6nzeP_hVq0pt0Mue27b8D64EqA2C61sAUMK5tFYtjc6Z0CbeRD4qUZng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ فیفا امروز صبح به فدراسیون‌ فوتبال اعلام کرده در بازی هفته سوم مقابل تیم ملی مصر؛ شاگردان قلعه نویی باید با بازوبند رنگین کمانی که نشونه حمایت‌از همجنسگراهاست‌واردزمین شوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/23091" target="_blank">📅 00:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23089">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HcUtERQv1AgZCIzvtSRW2ZINcSj2t_Z_gK9XVuiPf-OvQ_fPehHUcOkAgo0CFTVP-MJt3uymcTJZiZQqf9-x6Ro1hijnvbIfJjRDyqUMD9S4kY9aWbZWxz_yOZaIZWz-XYs22R1Pv6CX_L443FWL84FCGSFXTBAPyX29EaVw4PncBvrzvED7SzIhjnTD5-WdykvYQdV4IW1_cEf2bW-1u4w-SZbtKQfh3VBaKZlsu7Q-Whux8QOeSIMa4OOslJeVu2OmK_ZAD0Qyf4_LydKec_dPenNuin_ZnvI1p6Fh0QRCHStuRIvMKO3arFA9UgaobWOuJ5F9FwwFqjAf2f4tVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TSpjsKtExAPCnz8vYIDzm8egfOWKVJW5O8-vKqL36VjegoX2kTqPUwC4ciyrUrjtZf5EgxX_oC6uGLPRr9k0o444qrhfprXL0D4akSm_tD8lUp1vbotNw8y-mpegmYUJLfBOagyW6UgKQGed693ScgMThn4xTctgqPZY_M7fJF-YijEkeJd-MF1JyqxtWSSZrk4__VLYdfm-fKbTNZX3GFF2v0W5ejLrQnv44L8VWSqV-cgN2C7dUZh5BN_cI3WMHwmg6JUXk9Wawn1f0lsj0Nw-yn5-787fkHNVnpkrsHbERgBi-zMc3DpETBjHTlLs5N5HyY92uwHjGOev4xu3cg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
جدول‌باشگاه‌های‌برتر لیگ قهرمانان آسیا بر اساس آخرین امتیازات کسب شده در 10 سال اخیر + پر افتخار ترین‌ تیم‌های این رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/23089" target="_blank">📅 00:50 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23088">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MH08jCsAq5-JbXXjCEC7fS3Xe0Uuv-BDN-h7FnAIRTzjP8tjdOdoYtCtRPlvWJgP-jC6VgZ71h3jYs_wGYs4lp_BVYpUw46I0MQUpUnAeBs8zwA3ctBeUJshUCryiGQSyUal8nCC8obqm9uEEIfMGxqks9Q80m0j4Qgd2jQ49cM0rQddO3WXbKgoUBO0kgu8r8j62OygAeIsQT1I6s1RkViJmnsH1pIRk3hX4A3Jgy3X183HEVFm2b7BRhXM2aAT5mt2Qt6ATtFZqJMCpv1BRPrYJaDId84VEEx8Ro3IBRRpMvju73Kzn8YFAX9QwFkfjbN1TRS0aoX8DtMtD5uUTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
ترکیب‌تیم‌منتخب مسن‌ترین بازیکنان رقابت های جام جهانی 2026 آمریکا؛ به احتمال‌زیاد این آخرین جام جهانی این یازده فوق ستاره خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/23088" target="_blank">📅 00:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23087">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5366993444.mp4?token=vRt9z5W2oHLQqPi96FVVZu1TTmmr3DWal1HFuh8yUGxMIPdS5o6en07cK5QoPAq_i3mLwrsLIJVvowM_PCI4IwjUbLAi6bRxBVgFpzGFLhT94WDMjRLh0sZtsHu7SUSD4wK90VyEzxVITjWMYZx_fp0xwuMlT2q_jhUG9_RfcO94KS-WInC1bqIjNDdiZugeswUgmO0VKMUGTGN_4OeX7zzmptS-GlIPr56vt7MVPpVqRq1G3ELtRDA_KI-RfUCVl-kJckYLEqzJu7WvC-te5GYJUunNxtAnBiOAOVlV6l4yQLmMT0xtdpmSNa7DPiL_ciu5PprBzUg1O85ptr_86Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5366993444.mp4?token=vRt9z5W2oHLQqPi96FVVZu1TTmmr3DWal1HFuh8yUGxMIPdS5o6en07cK5QoPAq_i3mLwrsLIJVvowM_PCI4IwjUbLAi6bRxBVgFpzGFLhT94WDMjRLh0sZtsHu7SUSD4wK90VyEzxVITjWMYZx_fp0xwuMlT2q_jhUG9_RfcO94KS-WInC1bqIjNDdiZugeswUgmO0VKMUGTGN_4OeX7zzmptS-GlIPr56vt7MVPpVqRq1G3ELtRDA_KI-RfUCVl-kJckYLEqzJu7WvC-te5GYJUunNxtAnBiOAOVlV6l4yQLmMT0xtdpmSNa7DPiL_ciu5PprBzUg1O85ptr_86Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
جام‌جهانی‌داره شروع میشه اما همچنان با بزرگ‌ ترین غایب رقابت‌ ها؛ تیم‌ ایتالیا با شکست در مرحله پلی‌‌آف مقدماتی جام‌جهانی ۲۰۲۶، برای سومین دوره متوالی حذف شد و در این تورنمنت حضور نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/23087" target="_blank">📅 00:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23085">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pNYgU9KqiZ2Qh9g4bkIcqc2cFe4udn12PsGSsZKH9wJ725P0LPs3nadLatAUf1qM6txBqZigork6IIaklnT6OD7YFAVcWFIxkmLPumjcEiY82MZras4__bDF4cB0IVcmZzW7kmNppAoP73BDnTSYQLk7d2rKKCUqt_-lRAa7Yq0P3b5QOVCqcrhsaO_w8hMOUFrjROmgaxFNwRmoeuPPuCCrVj6OAPFWb4woJ1mvgOhN7NP-OkKFqCPqgOC8ECvv_9bJ73LAbbKJuo6LXaFBcUwHXHigaXjCgEOS8pzGSutdz0b2udjt5rfcU1t_JiWqKQ_wc30_Rsg9lujEbsScaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
مصطفی پوردهقان، نماینده مجلس: بعد از رفع فیلتر شدن واتساپ و یوتیوب؛ ما سراغ سایر پلتفرم های فضای مجازی خواهیم رفت. رفع فیلتر شدن اینستاگرام و تلگرام نیز جز برنامه های مجلسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/23085" target="_blank">📅 00:27 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23084">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hv96-rn2Axrv2pM0X6qYF1q9hLuledEcaLY-sjevne8l6nLeJmZ-Ec4h9B_yGCh53Wcuxlk325sB6XhB_gTNq9eGcHwVkA1QEBsdndS7pCxEdZu__vkmC_NARe7Gkjbzdla2jhYLAqgcbmg81tqzk7-CGfnkXt0OL21WB4Pwai_u1xH8T_WuAh1qIPIOV0Kq7P21mHjlnCfdCDb9XHO7EQIuSxiUhKPcN24btMq3gu6lgykid89KJiA0gLs6NGpDqLJGXerGF1QBbaCghEZmbt3avWAL_Pl_4eYkbelMz2NTW9OvzgMgeJK478lLx56GixO02AWzdRfDSwXJ_73ofA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇪🇸
🤩
#تکمیلی؛ نشریه کوپه: پرونده پیوستن خولیان الوارز به رئال‌مادرید بعداز رد شدن آفر 150 میلیون‌یورویی کهکشانی‌ها توسط اتلتیکو بسته شد. حالا بارسا مصمم‌تر از همیشه به دنبال جذب آلوارزه. الوارز بارها به مدیران باشگاه اتلتیکو مادرید اعلام کرده علاقه‌ای به ماندن…</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/23084" target="_blank">📅 00:14 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23083">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Axo3_GQ5KN-mhpcXk9xclH4ENdlg0mm-6sMBM2msTQLvL5zeNy11qZOqBz28_x33pp1cMzrhBrhUpgZtI6MBOK0s284xJ32xcsuqRAsHw-Bee_g1CW0IfoRM13_kDQfTrdat4FG3EvRNK7CaNePgrZIXRtLhsszl4w3JBV-XfpbI5OJtMvNdGG6VlRiHy5fL41NM4X40D8ZP0XJXncTeMgKhBHlZEieRYNun7XXv1ZOd8TNPNlaUob7OEMpHQdCPacYEytYzcbIsg8AkKpDEiRJ0VlG9Fy4Rsyj65SD99DF4i-2KEPoWAVaC1IcNQzapfCtxTa-nseN6kmehen2pwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ لازم به گفتنه که نماینده و مدیربرنامه های آریا یوسفی و محمد مهدی محبی ستاره سابق سپاهان و فعلی اتحاد کلبا امارات یک نفر است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/23083" target="_blank">📅 23:46 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23081">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gWL_RkXu9u35h5X4ICo1gyIH2Pzi8Y0oM2TLLXEIrl44J-qg4luB_UIW2vjetMZMMa9w22bRwqQzo6axZQeb8dzCM5Yhce0qaUNoJxaaZa6c7KJ--mYfQLNilroLlrvLDVFHUZgDVYGf2NHv1ziSGOlw-tjUU8YF1hvReXU-JxbLiWTqBYInhLBz4uGHIMlZABKv9Wj_uGSvoKxwznukNQ3LJrNHuvzb7xCz4cm0DYb-zn7He4g5g7dvf-J6xN-Br_Lz9tcE65ZM6LXNZp3bChtuzWAggnVtE3u34-Mw78EbdKA4NTFHHkNdPXr3pSkVsN4Kev5lWO4sw1p0OTQzfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
⚪️
🤩
#رسمی؛باشگاه‌اتلتیکومادرید در اقدامی عجیب پیشنهاد 150 میلیون‌یورویی رئال مادرید رو برای جذب خولیان آلوارز رو کرد و اعلام کرد مبلغ رضایت نامه این بازیکن 550 میلیون یوروعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/23081" target="_blank">📅 22:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23080">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GwjM5w9nyzMOvqYpg3PMzAMNY596i7JHKY4VPhDozgtdaYii3HbICojkYO5npwsfULyx2E5uwkqt0YMgzNO5VXWsdHoO-r04GPQKd4aQdl3gCrvXGFCSfooA_t1Ak8MRFFdCmRgqzeedDdymhQHUY0CvuX7tNz-w3PpmBknfwlGLMq_YmGYrIBA0v6s46TZVTwBHgZylXZDwjFCtEE7Wun4uNhkzFrWdP4UuxJ4YCApgrWU88UOSn7lposievM2MiMUszIU32vu2DMrWDvAZNbxnbgBPZ3HcvRz85rhDRYXfCcz6ikw2_PwfMRsNlkUN6DzDnbdUCyZUvs7dYA_3Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ طبق‌اخباردریافتی‌رسانه پرشیانا؛ مدیربرنامه های آریا یوسفی امروز عصر جلسه‌ای دو ساعته با پیمان‌حدادی مدیرعامل باشگاه پرسپولیس داشته تا شرایط جذب این بازیکن رو برسی کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/23080" target="_blank">📅 22:09 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23078">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r9bTJDfs19vEBXg_eTW0-x4CId3bHdyCLYg4eY2_6NvSTuUKwQFg3ontmTrjI548L2bCzITLIDGgzPWxaDZAyb-0ApyIbXUDdcXqqy7u08TUhm3B2P34E3frndgbK1W9XnXYdRZz_aStsbAbAAlmrcJHvacPlsRriwniUmwpM0otIL-WNxlVrnSCm5VLScprjzChDYN1zHhb3ZMw2RcCyc8Qj_tseaMQn6Q_ZuA4EDtvLMHaYvBDXvuxc8omMxJYy5cKE0AqV3xHC97q22u1gqnS91Leu96mEPrBqDKD9Fy2bXtMb7C7KNy3u9QjAWHbPjf8pJf_wwNcAhXP7Dei1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bVkTYgq7dVlrnS_cz4x1dON4OrURWnS7Y_2l8siE9-kCJ04UPtbViVHglBIkxRntxfi3f2PcYAUZ1-K-sYYzFJODpZy7zzEUM-oqOLxNXcq3TwhlyrsgvGXjrt635GYGC4G6_pxquLnIDvrmIZ0MJpLtxRLUHj4MgfENDZJF1oCvsEg6CDkl0fAFFWxNzr5CqkXy0Or1WbcLDH75TS-3gWtVuhXi2QQncF2r-Hg-bZm2CS_fmZDkV5kfcfvq8uxq-LDnfTHjvHiPZWii5AJPr5hkcvWwL6GU3J2ARl600VRQ8AdmAzNEL8bx0m8YKwt4g2MFOS2Tm3_B82dXkk3LVw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
👤
نادیا خمز دختر پاکو خمز اسپانیایی: علی رغم‌علاقه‌ام به تیم‌ملی‌اسپانیا؛ اما بخاطر اینکه کریس رونالدو رو به شدت دوست دارم امیدوارم پرتغال قهرمان جام جهانی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/23078" target="_blank">📅 22:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23077">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QgFm8Y5xw_vaZjgo-4Kxw8axUEmTX-i-X1npe7lmwrLLaBVJqYE0vssSdfktA1LmcHTw7vRMv_stLGMhigpxyssL4SyUxl0FgAvH0Cd6bOCxqQkJoXvHM5jtk03s3p_ILnd0RUVlDVN0W9a31jK4Ot5weWNJd7sytcjstVnbX3yIceD71QXeseIEg6A6RiYYF11whSqvN5Xs0Rux1OZ2m6zDLMwF8HAW0C_snv1OrWbHO_WZzW0tJWBI1ZULJPU3uQN8drjjl4RRrvqyWozIPdrM01x2DA5hDCXAZ1_RdaWdh9x0UMgsvpJpGp0b02Up3IxpQnmeAfMIw7dP1gwBmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#تکمیلی #اختصاصی_پرشیانا؛ آریا یوسفی مدافع راست سپاهان در بین نزدیکان و بستگان خود گفته که بعداز جام جهانی یا لژیونر خواهم شد یا به پیشنهاد باشگاه پرسپولیس پاسخ مثبت میدهم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/23077" target="_blank">📅 21:50 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23076">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K8dwP9l5BWITwu_Us0cFspDcutB30k2s6KtHPKElgxCTUWEFBUSx8V8A9sYAHSR8qg5NfxamOT_e9wreDWN2rb3On2TgV0ixdp9DWqiZEY2Kk5Tu-Q3HxDlQunIraGFwjFZ1laB-ipeXqVzGInUev5jJkov_t0NWZrd0T6uaBPCTTPIlHiNcWqv2nVuQrmciLWkADHnC7x8I1bZE0RQs5UajNdUlXJxlo2-OAEySz15Ijt4MssOcSneOSTx29Z2ZHwFCUgi57YWjwnKqI8XP6S39dFGdmNc233fS9WXF6JTj6OopLuOkeE9NinetBKW4Qn4ucxiIiElcQ0LY3tkyoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ علی نظری جویباری مسئول‌نقل‌وانتقالات استقلال با مدیربرنامه های محمد جواد حسین نژاد مذاکرات خود را شروع کرده تا بعد از باز شدن پنجره این انتقال رو بالاخره بعددوسال نهایی کنه و حسین نژاد آبی‌پوش بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23076" target="_blank">📅 21:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23075">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vVJTkYDCNsQ-RdxW2aVK7YLfLPDMESlCaITSLNlg-XTCtW9e8a4pHhvLeYpo9QVyFOhm5IRYLDPy-3lNkFF5nhIr6vBopsjfNX4Gsyi70k3v7OxCp9-cbvwWpvp27Aucr9lb3J0cM5aahhed12IAqMvwBkVcdXdmdNANqy-niZKGqiASuZPO24HY4lIu-NGv0fTc2ZXAHesjJfMwclCGwuMdQsOPHvKjzsiAmhzcUm5-HRTqxniKgOFKvnegbr_rwse0Dp-DiHxC85F9adbc83DquwOZSbpsjpCFUhGrRUOtfe8mOFnqqUBXo_TmBGbchuaItxP6smIXaSBQVGlC-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باتوجه به اینکه هوا داره روز به روز گرم و گرم تر میشه این جند مورد رو سعی کنید رعایت کنید تا همیشه خوش‌بو و تمیز باشید. در کنار اخبار فوتبالی چیزایی که بدونم مفیده رو براتون مبزارم
😂
❤️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/23075" target="_blank">📅 21:12 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23074">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FDMUDJsTF_pKCj2sdcYIAco6hwpxNmGYl-a9MZRf4bBITmlDnkt2Z8Z9v_o10MRjKDtMZj-UD8x60XAnTFCS79TcD_yIOAIj9joG7hL31L72whtK7AXLeuR_JsyAh7lP3conPYfohpz2o6B7sqAb4z3nHH2ULTB-6nssbLJ_dY5Tk9meyJXMB5aa574zA1gXDmOU5FYnwZdkA-locRGTQ-ms-qqHNvRqR7fqwBwixkoPLi_m9B3FwfEVLRQvOxCsnmkaCurBovzmDoPIhCGHEGidQbyWJ3U5EfU4UwiODZDMsCyzsetrQlYINs8H4xnQ7ixdqiSrXOrdlQtaEyIM6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ قطعا یکی از این سه گزینه مدنظر فلورنتینو پرز خواهد بود. پرز گفته پستش هافبک یا مهاجمه. گفته‌بازیکن‌بسیار ارزنده‌ایه که مثل رونالدو، کاکا، فیگو ماندگار خواهد شد... یه درصد تصور کنید که‌ خولیان آلوارز رو هایجک‌کنه و 150 میلیون یورو به اتلتیکو مادرید…</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23074" target="_blank">📅 21:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23073">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QNaLwl6L8qMrURgY7HGX2D_NNI5NqA6us-kS13d4ZQKxITVnX2dmUDXb8OWldbtb6Bq0gJvwZfGjkKaZCSM03ylNDqxjXAN3o1rsQGxCXZ1CqWx1zk4pVJMykkhJ-lNrz0aIGeIFFzg_7pvDE847XXvVCwqMm6hkm4wSU8Dn3AmGNNCnUbe-tjGPqm4Q0y5T9zCftbHZOuHZXlEeZ8pVgDoZKmHkk2FpYRz_fuWPfi3upBo_NZpjib1C0GrSWJ-OREj4vS6oMoEemqpZYDu86PuM1SoU3lSKvbytsvqBohiG1Up1RvVDoembElDy9M9-OQjcAbaxCQrjxOh_E1Ow3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#فوری؛اسکای‌اسپورت: رئال مادرید امروز شرایط خولیان آلوارز رو از اتلتیکومادرید جویا شد. اتلتیکومادرید اعلام کرده هرباشگاهی 150 میلیون یورو پرداخت‌کنه رضایت‌نامه آلوارز روصادر میکنه.
‼️
فلورنتینو گفته دوتا ستاره 150 میلیون یورویی میخواهدجذب‌کنه.مایکل‌اولیسه…</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23073" target="_blank">📅 20:51 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23072">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rmt4OhSW7psl-0av6E1moEX0NNp9hf1K9Tv-sSEHf60WXQ1wcXP8E_xtUi53r1GlsUFTzJAZqhpMG-y9i74AdtVF67ltsjO60vUSgLplMEOOVaTsEb_08MYzDIalrPrxZ55_6q70AmGKIoSR_tSY_HyIN1rorBPz-zvJISUbSAd_QG9VlJk0YOaQXolnafYelL5vbAJUI-HHMpAiefSdLV9QRvWCDBPPlTJcPolt4Q-ex-kgFg2ZhZpgjjwJJ7273CnR34Jd_fVkSAfoFo0i41c36jzxe-LQTLNGNdSGYmo3YudhX6lwDvQOSxUoah7bRNWK0SW1_qw2-_Hi-NLTqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
7 زوج‌برادر درجام‌جهانی2026؛ دراین‌دوره جام جهانی 7 جفت برادر درتیم‌های‌مختلف حضور دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/23072" target="_blank">📅 20:46 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23071">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/993bfd4bf7.mp4?token=ZmBvnJpoiG2daqirgHk1kZuODBgZh6TDKzt3vnragz70YSj0yBECrnwIge_BucIsMMxd4OTETeuA5_5feaEtH76sX6pKho24jxyOU7wFsHJc2C4-eZHBFmcIpfFdictaOPYDDI9G23pUZ_t6smnNSWsbArpNwhQBYJvVYoL3YOHgu--GGHz_7hRNCVKBm4GW12VskMPaR9rs-E5GIDAkI617LZBGTU0-GHmg0urTASM_PbFpJjO6KLL-fG8tVf4OJBnwDvz_9ewLOJiK7wCA-UlMzTnQzue7zmXdEBkVScj_qj8BBVgaEdEXl0LfFd02Ts8dlFdKf5e24Z761-N1Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/993bfd4bf7.mp4?token=ZmBvnJpoiG2daqirgHk1kZuODBgZh6TDKzt3vnragz70YSj0yBECrnwIge_BucIsMMxd4OTETeuA5_5feaEtH76sX6pKho24jxyOU7wFsHJc2C4-eZHBFmcIpfFdictaOPYDDI9G23pUZ_t6smnNSWsbArpNwhQBYJvVYoL3YOHgu--GGHz_7hRNCVKBm4GW12VskMPaR9rs-E5GIDAkI617LZBGTU0-GHmg0urTASM_PbFpJjO6KLL-fG8tVf4OJBnwDvz_9ewLOJiK7wCA-UlMzTnQzue7zmXdEBkVScj_qj8BBVgaEdEXl0LfFd02Ts8dlFdKf5e24Z761-N1Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
سوپرگل استثنایی کریس رونالدو به الخلیج بعنوان بهترین‌گل‌این‌فصل لیگ‌عربستان انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/23071" target="_blank">📅 20:15 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23070">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J3sYJp2p7pffJWSNarRnYCQOKxlqAErNrRTnx5ojPwP_8QIoJJdwqR-G8zUIH4YJA2bhUGRUj8YFnJz9_8rUpdPeARRjtmx1romD0DCwUWgFu2Hi7yMp5-xgtFG5QaRuBltYcGFHJ7Qw-eTSECXqQJDmaFSvjqGtIln-3Uhjh0nkg2TQE4l_vs1wsNvyMpI-TsxQFq5twh2oW7hNBHflAsEWKZB7K5unjLX8R9wmc6J62kh5uECVaTap8aoQ9z35UsA0gyo-sgLptCJ92ERUa7lZ_BSB5QL2Jdi5g4HiHP7bpNhE9Z1Qg5AWA3xeex8BoKgSVC5RFjfPNFGnrVJbhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فابریزیو رومانو: برناردو سیلوا ستاره‌پرتغالی به یک باره‌نظرش رو تغییر داده و حالا هم میخواد برای انتخاب باشگاه بعدیش تا بعداز جام‌جهانی صبر کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/23070" target="_blank">📅 19:51 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23069">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bd17cf6e0.mp4?token=FKFxsP2dN-buhNjW5CUSWm5m3tJ2jiufexwjJcRSF_rsXHGCXJfbS5r8wCtv0sx9MDiKvgbS4vfiuEzOcpJcz4Hc1_zZSIszZiPSh6rUaSZxGiV5ZxRZrvhkohQ3aC4HTz8Pyxwq1xdSVQMI2_UbpYddC-jUDv2ioUjh7HuuufgmWD6Az-nafEmadpaubgqtspsIEWegNCrdnuauspsHopK9U66LJTzmxBkQwxaC-f-d8D-vRM-cJOSdKtXgHnlUxLT372w7U1UDa5coTg2rlABfmur67UctPqBkPAhGHO765TKKGZJg4icp9xAQW3YpbvtY0MiTKfPoSwWBGkL2Xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bd17cf6e0.mp4?token=FKFxsP2dN-buhNjW5CUSWm5m3tJ2jiufexwjJcRSF_rsXHGCXJfbS5r8wCtv0sx9MDiKvgbS4vfiuEzOcpJcz4Hc1_zZSIszZiPSh6rUaSZxGiV5ZxRZrvhkohQ3aC4HTz8Pyxwq1xdSVQMI2_UbpYddC-jUDv2ioUjh7HuuufgmWD6Az-nafEmadpaubgqtspsIEWegNCrdnuauspsHopK9U66LJTzmxBkQwxaC-f-d8D-vRM-cJOSdKtXgHnlUxLT372w7U1UDa5coTg2rlABfmur67UctPqBkPAhGHO765TKKGZJg4icp9xAQW3YpbvtY0MiTKfPoSwWBGkL2Xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
#فکت‌تلخ؛ مردم‌ایران تنها مردم دنیا هستن که‌موقع جنگ‌بیشتر از اینکه استرس جنگ رو داشته باشن استرس قطع‌شدن اینترنت بین‌الملل رو دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/23069" target="_blank">📅 19:45 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23068">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jEOzGpCVUq9-KIWq5KbPqN2xud8QziF9ZAUHVwUHWBRCNkh_8RcTVxojpL5CShMxTEFPdUPTXMs260XX1IbvVhypqyaFOZJmdxW-BsuL-d2La-UBpINf_5oBCyoRakPFi3Z6M8hK4adsQGEpZoieBn6xc01HkFlQj_wf_JhfhHndOxqQL1hxvTC-j2IqJlMPnGGxcDvEZrNfdXEdeQgGvoaVjjYuCcY8H79Mtaj6DzaXNJzipXN7LTBsEj_YJMZRAEIikoiVHllNdY7Pl2digVIY3JK-GtJLOv6tBLmAs8q68O8UliIq0Cl7HVIY6nIQwj9_LRRAOZw6dNf_tLGyIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
🇵🇹
برناردو سیلوا: فکر می‌کنم قهرمانی در جام‌جهانی‌پایان‌بی‌نظیری‌ برای دوران حرفه‌ای کریس رونالدو خواهد بود؛ رونالدو همیشه‌سخت‌‌کوش‌‌ترین بازیکنیه که می‌شناسم و لیاقت بردن آن را دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/23068" target="_blank">📅 19:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23067">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B088SRj_0ofrN-63oJbNnc3CDBcQdxODoNPtbmeBbWWdFpovRHH2D8FoomzHPoRtC9CK81FBBzIVN0IqXkzFVBvLQzJILm15byq8aoKH74hPRUGYpWCxOvDlNXHa1DvU-IpYWV0Sfn2G8alaU4NVlUCosELCSbhP2R8bGbVlJVEd5nKMqN1D0YFVdB4pi1ZRYJEQPUZ3HKJGLwjRSNLP-a7mqnvdy__fwK-S3leL3TV27CsNCQbhkCd6-v6ZuRanSjxVc7VoN7BE0zgjYKTxYHO9opY572xm-g47anN3st-x9Px6A8bMphDHJF-sDisdEePsk_izmd-zuZUcbX_yzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🔴
با اعلام حجت کریمی عضو هیات رئیسه فدراسیون فوتبال: تا آخرخرداد اگه استیناف نتیجه ۳ صفر به سود گلگهر رو تایید کنه گل گهر مستقیم میره سطح دو. اگه تایید نشد، ۵ تیر پرسپولیس با چادرملو بازی میکنه برندشون با گل گهر، ۱۰ تیر بازی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/23067" target="_blank">📅 19:16 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23066">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A6VOD5WILokeapu7H0Fdqb2Wvd4Oca1eAndiniebP9owxuB7YqkoT9USb1_iP-u0KdJBCoSYqYwXOorgBzlrOO_rtqOrdBJAcNsedp1mb0gO_EsUvZGbXemoGBdXPeZQYnhT_KLkggZoRuFjvUHlE-2j4azS2DEBUUW5wLoarCy52vS1XrSksBCPsuvjWzrXIc_7NzP55CP3zkq8_YowAkvUML1u5v-OGGH9bXubJFQsBQ9VVtMlKJ1xUYRvF5T178OtDUoklM_wETTtVbGd-9eMNTeMCu9e7zJ1Kr4AaoZu1NcnZgyoRRWKLmMGIoJC5riipC6z5uLvQGV2RIBdqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
لیست‌کامل‌بازیکنان حاضر در جام جهانی 2026 باتجربه‌قهرمانی‌شیرین و ارزشمند در این تورنمتت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/23066" target="_blank">📅 18:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23065">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qF3WXFzrvQxLOjTyYD_tcpxNwuMruQJfbGC4ftcZWNEfPEtBa4SKcZUdDDXdXOcLHLciJeW7FIzrbJdV4Ksu4W-XVQk0Lh16mZKAeKSSYdSxjRWINiYFWwxga8Eg9fxjWV_PY-xVBka0poAEsoCB5AiS6TwE8fVLu5K-ms-Sn1DAcj5uUbOhG-TwqxPDmL6j3BCmYeGNvQsWl-P4qxN3Tq02lVt3LUmRq4HRi1HG0wnscnLlbDaTvkF7tDfNabHRptyHpe4ElC8FNg1ZHr4deMxXyL0jl6CPa753nGmtMx2oMVsO09IhUGPWixT48Qul-moC4syZmzeRcEbXFsLXIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همانطور که دو هفته پیش خبر دادیم؛ باشگاه سپاهان مشکلی با فروش محمد امین حزباوی مدافع جوان این‌تیم‌ندارد و رقم 70 میلیارد تومان برای این بازیکن تعیین کرده است. هم آریا یوسفی هم امین حزباوی مدنظر اوسمار ویرا برزیلی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/23065" target="_blank">📅 18:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23064">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gHq1YhlenXKtIMEUN_sNwHFrW6GRKC4MjRRBccV-oyyCRX6MxtYkGe3V-aZqcQxz6sJpTXtDBQHxC1PV4hZz9wNFMRRwAH3m5LonkLHZrVW2a8A49utIvpf2Hk2YAqjtnFwK0Z5d0ER-rxUe84f-fTWcb-H_vViWqCFGsweH9zfUNQfFtKjwFHyWWjO6p4XgZJYo_vtPAm_JtU6ejVMQ1XEjod2pyK4EA38UgIavjrwCl6lZtpGnpkH1Vvsx8IXG_Y8FwqwnuwG0FdKuXUJx6LMlR8XCbCIJLVc9fOuJN59e0cFY5n7Id47ShKWjW67-uXcT4Z47nmfVJUwVQiMdcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
طبق‌شنیده‌های‌پرشیاناازتبریز؛مدیران تراکتور با علی نعمتی مدافع‌سابق‌فولاد و پرسپولیس برای عقد قراردادی دو ساله به توافق رسیده اند و بعد از جام جهانی قراردادش رو با پرشورها امضا خواهد کرد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/23064" target="_blank">📅 18:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23062">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b51iD4AdU8_fIhHuzieDazav-X-fMK9W4x3a0HgpmpNnwq5wjRFN-q_83RcqaXqqJjk54Lm3LIPpZDZJq4hQ2fhZTJBT0h41AVfWioqftflskZnjYL6EPh1Fb95Uh82a1TknJJ8KlNtlkQzJQR6TO8yMZZOu018DKrP7xlWx6LLBTrH1FJvwSwVqSuO3LB2dIrP5bChE8rpDIBZEAx2_ktt7IhB_F4BZsV0lTQFVzy0Gcvj8GFITPHF5x119Uo8KM4kwc5v7aOEKOz8KrTvds8pyxpbhtmxNKZ7gmA2SX7RIXtJvHOgAUolMsfSOn_kkuMyJb8fcOuDJyMvwsEJ0ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
ترکیب‌تیم‌منتخب مسن‌ترین بازیکنان رقابت های جام جهانی 2026 آمریکا؛ به احتمال‌زیاد این آخرین جام جهانی این یازده فوق ستاره خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/23062" target="_blank">📅 18:06 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23061">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a49850c982.mp4?token=oPzNIfr0S0K6RwXhfV1EnJoxHWlCd03TvbFCwkdW6YdTZlMCEz5O4rYZyrckF_8mWv5J7XUbMlpPgrq67nzzkMjXnpGaXOFnidfzSRagO1kzmnUGEXN9KW8m2z2Zj3BUEdvdIHReuGIO-KRVnDUqn0n219PU_AJj83ZSqwciwrSp3wjUrACReq2hAmV482_rLQmlTs22a9TdCCdYLRbuKuoDpn8YMlVpxoHMCNgpxqfs2JgfUFmt5JiolgRDj0Y7zI2UF6UjdqY0PJd15V0GRaGMbQeVtSREhk1SJrW7cGjnQ_rScm0oIrnIsBrx6OwGkC1-SDYcg6YmMLEwbm5K1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a49850c982.mp4?token=oPzNIfr0S0K6RwXhfV1EnJoxHWlCd03TvbFCwkdW6YdTZlMCEz5O4rYZyrckF_8mWv5J7XUbMlpPgrq67nzzkMjXnpGaXOFnidfzSRagO1kzmnUGEXN9KW8m2z2Zj3BUEdvdIHReuGIO-KRVnDUqn0n219PU_AJj83ZSqwciwrSp3wjUrACReq2hAmV482_rLQmlTs22a9TdCCdYLRbuKuoDpn8YMlVpxoHMCNgpxqfs2JgfUFmt5JiolgRDj0Y7zI2UF6UjdqY0PJd15V0GRaGMbQeVtSREhk1SJrW7cGjnQ_rScm0oIrnIsBrx6OwGkC1-SDYcg6YmMLEwbm5K1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
🇧🇪
کم‌ ترین انتظاری که هوادارای رئال مادرید از دروازه‌بان‌‌ تیم‌شون یعنی تیبو کورتوا 34 ساله دارند‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/23061" target="_blank">📅 17:47 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23059">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JhQynUJX1DbCyIjW-0sTQhqRKT-Qce_ogDPLpF2eAoAdxmpJIw0z6iMZ_jZT-hrJXzWW13B_gjK41lZgTTcaEEdZhWzYNnUI-XP-V96SY3KcXN71D5oNcdhG9S357GCuAxpSjYJvFhF6fPbbN3Dxy5c6mhzQIv-_U16d0EbO6TFTOxKPzZlbrditxsjeDrwqyY1GeS1329MWUgJhiwFUQKYnuCJZ_p9QSazqqP3jzdo5GButPLFe2BZd2vU_2p5hI3GCaSByrTz63KGHZe5ISrGPbR82uKeBPwxz4F4NJJ2v4wpXgQ5zcjnIsfWGrKmVASYflMJbXNCXGhi2U8URog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K5C7dcsnSVtNOnzLnuBueJ9ScBJyvRlYS0gAymw1C5fMwnlRM14Gdtp97bpafM-hsHnTMEzidjOvwfAlaIY8nOjGkQXtasRp-KIQiC5dhMBD77JCuq789J4j-1Ty6rKkV8_2N5ev7l-FeU_fFUf_Hw9-5yN4jVz5SaBHHWy0hvnjW4C396B9So1hBKvEkN3D76N30YIb9tfZ-RCiWcZ7gORekeC-1kszzgTKFTSQY4ssv-eNnJEMQSjblJg60QeKRJgSqcXGZMxB90vlxinfWY91jiQ7tO5Pse_67rmaOfsVSDkXxcUXjZwY5QyFvCd4RF0veZtYjBUtlEuOkaYqHQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نادیا خمز دختر خانوم پاکو سرمربی‌سابق تراکتور: از وصل شدن اینترنت مردم ایران بسیار خوشحالم. بسیاری از فالورهای من‌ایرانی هستند و در این مدت متوجه‌شدم که به اینترنت‌دسترسی ندارند. پدرم یک سال درایران بود که از مردم‌خوب ایران به نیکی یاد میکنه. برای همشون آرزوی…</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/23059" target="_blank">📅 17:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23058">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DZqJ8umVlvZr8CkOEy48Ews2yetb_5Gfozej1KGAbiGorOPIKqUmV3ERQ5cSZ13hSVEAmGN1ac7l93i35R5KwrsQ3HmS76CFNCx-fXv5ij9cd7qrFc4k4eLApUz7yLyG-PfDSA1hbP7zz5OE4M5Gu31ezMswYnOfoQ8Bhm-ROTwQlZw5eM8OgiIwVApa_pWtUkGCxOyOgJWFKoKIAOc5NWbwxzLPUrZiGysl0i-4MQWGwyJHC5nJLemf5zWV4y3GARpQu5ikfQOMzItOCwQDALpi_fBeN55XbYAFgAS5iQuq9_PQsXPQGnqHHb4H8MCopKGcYzuOeZe_C9S4RrGXPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ ارگان‌های امنینی و نهادهای‌ذیربطه به علی تاجرنیا رئیس هیات مدیره تیم استقلال اعلام کرده اند درصورتیکه فرهاد مجیدی تعهدکتبی بدهد و در مصاحبه‌ای عذر خواهی کند مجوز فعالیتش در لیگ برتر صادر خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/23058" target="_blank">📅 17:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23057">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iBsDEKREtC7eLyNW8xZzGXU7ofRX2aShevlIaXp1XVD44zWkEKMIBo-kD4gopQqYjQJ04Eyh9CFllJdxc3mHU3YB1yb7CDNmrW57zmsAq6WwL8cL7PABqoxAA3f0NVEhfyP1Ehsmz3sZJ3P8JBYw7lhhCvjphiwzmosX1WzVH1zPrrjGqXBNZ320rRaaCPwHsF6V3UPNsDBuu2nsKU_1cJsmDp_0F5DjQ8tKF7hh2m8Rrbz8Z5vodl7lWliHQMO0MIhZmk7y6VBbnOrN_t9YFhZ1jtLh3x144p0KAouNJiqArsBsZGpE09cxW4TyTqo24B1ef2NKVUP88IJVuaxutg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بمناسبت شروع تورنمت داغ جام 2026؛ سریع ترین گل‌ها ور تاریخ این رقابت‌ها رو مشاهده کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/23057" target="_blank">📅 16:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23056">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MbupYWV1RK8JRDQuipLIDHR3sNjwgWdTsspkLNZ1aR_ZVPUarUnxDR00u6ytcVpUwGb9R4hduTpVrhYptTh107Wv9GV0rMSwRbKmdfcvITwX0DUQG19bOPH3JamgwOpzihRwDs1tsl2Rt0tMcgrVs0jK1k8ZH2OiHqqy0CZQx7IPduyKNH3EluuGmPnHZyHJ_Nfb1xJ5S8_vx4eplkAyEUFLddxHsCkegGqb9uwtS7fafYAAmC3Ujcpv4D1qSkJrHPCQ83hVlsWCx-ITpqyhWK0m8kd9jnmd0I61GuKVXgo15PDZKIdPdQiKusxhNp2z9fRsd3w3sGe9vQ_eyohwug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فلورین‌پلتنبرگ‌خبرنگاراسکای: علی رغم تماس های تلفنی با هانسی فلیک؛ خولیان آلوارز ستاره 25 ساله اتلتیکو مادرید از پیوستن به تیم رئال مادرید استقبال کرده و گفته اماده این انتقال هستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/23056" target="_blank">📅 16:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23055">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k7xLn-82F-Iyo251frpdcS-w5SiNHvCAkd3BokTuTPDnV0Tu6H4_2tYf2ndbnZgodWkD_GoMuVhHhfE1QOXEOaHpMjzb087PWkKBAU8HeR81e9WuWmG2GTQC2ZukRTx3Nn5GwsP-5Fv0cZMFjX7s5IWd2uEggH_j7IhCA0M4Zb4biy0EDc8rYuB6Mc-ZXa7SF9WiC6OSQSWoRH8LKwYh25iQaOjpghV0nqXGxFDktRXD8tJgw55u-7JcMonNk10swvD1FFHEu-gyQQDdTWGMkiANO-Ka2VbnuiC9ExE_qvVsPjG6p4c0z57Y106vVJNv3UphSCSIhj8edaN7K3d4zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
عدالت در میدان، هیجان در جهان؛ جام جهانی با بزرگ ترین تیم داوری تاریخ‌فناوری های پیشرفته VAR و قوانین جدید پا بمیدان میگذارد از شمارش معکوس‌برای‌اتلاف‌وقت‌تا اختیارات‌بیشترکمک داور ویدئویی؛ همه‌چیز برای‌تصمیم‌های‌دقیق‌آماده شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/23055" target="_blank">📅 16:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23053">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fvwoIMwY8pCnectHjlJePuEOSYvbE3IEkZPd7dcD6IHB9yMrEh6R7Bz-mhEMhzygnDixFUl8v47c6JaYG_AGQT-rD5ftaLceb3CCE2Si8kK28GjlZ5Y3VVY3sZcHtR_D-FP2Qtx8Jznbing5yC3pnrZ-dRRIEkPRM5xoSCSUUvOYk5t_n6NAsNAtF5gTpGU20SvhcpRPAofZlsqmxU0SJWviN_vUUKGyzeGe1i-4y0qKRx_s5zmLwVRB_TiiQn8LpxoUMiMeyA3k5AdjTJmPi9hrjB3ufWl_23l-Xp82a7lHVU5IC39LY59RdjA6lOFpmJ0aI_ifK6EOcYsDHTUupg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق اخبار دریافتی رسانه پرشیانا؛ اوسمار ویرا امروز صبح‌درتماس‌بامدیران باشگاه پرسپولیس اعلام کرده که به قراردادش با سرخپوشان پایبنده و به‌زودی برای پیگیری تمرینات تیم وارد تهران خواهد شد اما توقع داره که در نقل‌ و انتقالات تمام بازیکنان مدنطرش توسط مدیریت…</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/23053" target="_blank">📅 16:15 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23052">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6daa12069a.mp4?token=GG_yV4rMirpkv2mVGLFuuGnafk6Rty448oKkGmf6wPJPxvSq4vwEfrnfZZugWFJmlLHZNS1p7u100ZKKsDJmygoilNhFxS5za-YxLBF7-GswCSWUQaYWQikRt3vXmefoH6G-6ZG6uEzuK6CHV50J5lr-nVfhTXm5Gl8XGm3AtB5mPd8ja9mun5ECJvDSuvDHuWD6WpMAb6xWPCBLXp00wXBlZR4lTvJ8M5g916T33VG4OmuoMNrC35qTIGIjIFYJMzPkyqmPCTYsvnCYr1Zgdksj9yCqOls_REx7CYtlMtvPm9nAqQ0IUw2ZW52i5dDQ0vRCJ12WEjVspm3udItyPVJveBiSoo-_204HOaZj5H0sZKNdkmqMIqdLqQG9R46Yjkzp9uzKvdmUtnmFmRDsSeAvhp3jt7Uaska9r8Ll6U8TrLcaX6uDZWeSbARMgAhE0m-aWynbPsBxGyeNdnzVc_dp5Z0rZMuLodx7pa3GpyXvx1KQE6wi88I5F1Y290qFdPNDQn390_oV_Chs81swHgDEPSM5ntomJHBPVPRoe3kcltblamIDkxVkFXfv9MULjfQN07ILt6dwKc01NvzqLskymSsx10Ws7_Emog8FGHbBywI-5IcQuLLjqGQ6mtCOhdb--56gtz-dV4NLW615vImMYAkTP0cpMrHK4xnDvSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6daa12069a.mp4?token=GG_yV4rMirpkv2mVGLFuuGnafk6Rty448oKkGmf6wPJPxvSq4vwEfrnfZZugWFJmlLHZNS1p7u100ZKKsDJmygoilNhFxS5za-YxLBF7-GswCSWUQaYWQikRt3vXmefoH6G-6ZG6uEzuK6CHV50J5lr-nVfhTXm5Gl8XGm3AtB5mPd8ja9mun5ECJvDSuvDHuWD6WpMAb6xWPCBLXp00wXBlZR4lTvJ8M5g916T33VG4OmuoMNrC35qTIGIjIFYJMzPkyqmPCTYsvnCYr1Zgdksj9yCqOls_REx7CYtlMtvPm9nAqQ0IUw2ZW52i5dDQ0vRCJ12WEjVspm3udItyPVJveBiSoo-_204HOaZj5H0sZKNdkmqMIqdLqQG9R46Yjkzp9uzKvdmUtnmFmRDsSeAvhp3jt7Uaska9r8Ll6U8TrLcaX6uDZWeSbARMgAhE0m-aWynbPsBxGyeNdnzVc_dp5Z0rZMuLodx7pa3GpyXvx1KQE6wi88I5F1Y290qFdPNDQn390_oV_Chs81swHgDEPSM5ntomJHBPVPRoe3kcltblamIDkxVkFXfv9MULjfQN07ILt6dwKc01NvzqLskymSsx10Ws7_Emog8FGHbBywI-5IcQuLLjqGQ6mtCOhdb--56gtz-dV4NLW615vImMYAkTP0cpMrHK4xnDvSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
یکی‌از آندرریتدترین‌مثلثهای‌تاریخ؛
شاید اگه بیل فکروذهنش گلف‌ نبود و ژوزه اخراج نمیشد، چن جام از جمله قهرمانی در پرمیرلیگ رو بدست میاوردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/23052" target="_blank">📅 16:06 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23051">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gw9keSDmfJ47LuRnt-HPwOmqCigPEZFEhIj2m5I9gJ3E_x_Af753dEkquiOaBFjdB9suNFbYobJ6OGjvSlcm643Ee3v7XW8WLjYvTYLlOvoMrbM5cpiYHLdAVk6dd-mxQQbJvMRZE5l7Jsp7s6hchZOXBEzCWb4IR1Gm4HEfWDLqtMsksXuhNJbTy6zo0fhPKz37RBjxqfOSl1SXvAfdZPXjKGWoUCcVY-x1q-XCawVK50K3u9CGKSWp0qumU-ruZU1hKMHAffLMRI5ggcSGAOazsZkuP1Ie6DLPwwniy35c0dgieNibOg2TDfYs3odJ7p9blMxvSHcs084WCf1RYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام نماینده مجلس؛ یوتیوب و واتساپ تا پایان هفته کامل رفع‌فیلتر خواهند شد. دیگ میمونه اینستاگرام، تلگرام و توییتر؛یعنی یه روزی در آینده نزدیک میرسه این سه تا هم رفع فیلتر بشن؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/23051" target="_blank">📅 14:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23050">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcda08a029.mp4?token=JJLb0-WNI17b-JHh7ZLIzWIc6IUpYNomCakzhW_ybKYAcyxyq3AE3oZ_l91wSQoKsiFVgYoubj_3hl4lgl5_aSnFEEuZGlHlgic_fsEB85faAaORS2FHlk3UgyhU89zsI6fulSwx037Sublk71pnW-Or4qnSvx4aONndf_hyMQ0Gqw8ktQo2fKpBW5tRG-FPiVNM_waHJ1JuU4hwsVWXWr_u8GjWULppCQ2ws8Jc5OiZAgo6mtIqOPOy3fUszrdrDWcEbjhcr1YiEOo98Oh9PQUyf2nPn5y1ivCHdpBGARJOtNXZ6rVrxPgN8PFWltcbphLg4leMDo0beOyZx5AjDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcda08a029.mp4?token=JJLb0-WNI17b-JHh7ZLIzWIc6IUpYNomCakzhW_ybKYAcyxyq3AE3oZ_l91wSQoKsiFVgYoubj_3hl4lgl5_aSnFEEuZGlHlgic_fsEB85faAaORS2FHlk3UgyhU89zsI6fulSwx037Sublk71pnW-Or4qnSvx4aONndf_hyMQ0Gqw8ktQo2fKpBW5tRG-FPiVNM_waHJ1JuU4hwsVWXWr_u8GjWULppCQ2ws8Jc5OiZAgo6mtIqOPOy3fUszrdrDWcEbjhcr1YiEOo98Oh9PQUyf2nPn5y1ivCHdpBGARJOtNXZ6rVrxPgN8PFWltcbphLg4leMDo0beOyZx5AjDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
تیم برزیل در جام جهانی ۲۰۲۶ با هدایت کارلو آنچلوتی و باترکیبی‌ازستارگان‌باسابقه و جوان، فقط با هدف پایان دادن به انتظار ۲۴ ساله برای ششمین قهرمانی‌جهان‌واردمسابقات شده. اندریک قبل از آغاز ماجراجویی‌هاش در اروپا، تمام دوران رشد و شهرت اولیه‌شو درکشور برزیل و بویژه در باشگاه پالمیراس سپری کرد. اون با درخشش در فوتبال برزیل به یک پدیده جهانی تبدیل شد. رسانه‌ها هم سر شوخی رو باهاش باز کردن و روز تولدش رو با پله که اونم ۲۱ جولای بود و ۱۷۳ سانت قد داشت مقایسه میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23050" target="_blank">📅 14:47 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23049">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQn11g2_XZP9k2XwaxSZXcbN4yqk4X0qbZWZugyKcW5laKFJ0ByVytDhDfwW-sZ1E0_s9j4NLVRtc20PoXG8_onwQr0hOOOXt92xV6hdF5hOQMXAzYHZPqcsAZk7-GZB0e2ymbPNFC32aj6JmG0_zzmpkyaLpKP7pCiGRZc8jcRTSq3V4meQdYHmth1CQrzDYljRyvzdQCMeb-qD6hyCrlAsYTAGmpHGwRtXPNX65VMiKQ-q3i6NSKYabFjgGMDDVCtYEv1k9bIF3_QklipWGzdfiFk7WomWA3FFrlTjtSoAW-wIei_CgmfV5EN1piOQTioTmbdXjnF-JejsFOFWHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باتوجه به تعداد سوالات زیادی که پرسیدین؛ لازم‌بودبه‌احترام هواداران پرسپولیس بگم که‌اوسمار ویرا لیست بازیکنان مدنظرش رو داده و از بین اسامی 9 بازیکن که به مدیرعامل باشگاه داده 5 تاش رو قطعی میخواد حالا اگه مدیریت علاقه‌ای به همکاری با اوسمار نداشته…</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/23049" target="_blank">📅 14:24 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23048">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AFk97lk6McJPL0U-SXXIJEm--XT15lQuVW6pZRSvnEmKOcz5L2-_EXMKo6qdj6J7h7SLvuzZTQfJEk8GOQrYJuOieUgSpiQmteW8VhEJUO6YSj0Te8FOZ-QN-Z0mwTgkM9bwJojZmCrsXIGHgDNo224Ea9o1JFOAmmdMWVWtHGHQ1cwtgu4iTYSFJGyGFkVWhaZpjMOUo2_qMVcO1rX9dY4W51RLgoQyMBQnTJLS6om7xhM4zPdl-K3nOWAAZpnYxS5mtrTK6PGwI_aQy3hk8D7BGARuPOEcD0MucuSLJ0yV8yN8kUfZIUKGY1KPktZWpCd0BWFgBWiUXoiAZpZTMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/23048" target="_blank">📅 14:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23047">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jsrfQzSCT3KzuCQpnZ8MiGIO2Qa9fDrI2o_6QzfrBlmIWj7nC8s69lqXAAp-PemV3gVQG91QYC8w0v3Ammj8EAvphPjFzARSBligLOguomF-7nUXGrR0NxcDoGJMFFhYbHTlWz6eckawIg-v9nY12veHuNIFb14_7RRyT17xgK9mKwtxW6S5j95Cd4ij_Mg1s9f3RXV1WgmIVuOAgZbjyr1RSyGtoJgD6fLtlMl20U0d4LjSDrTfRaDn7kQLIUiEp7ZUvoETcQmodIeeQihIPj4E_LaVNAfOPgcGIduUTNTxdQ1kLg6H0gTyDVyu06xHinSWsWaUyHIpzOIM4HLuQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
👤
طبق شنیده‌های رسانه پرشیانا؛
باشگاه استقلال مبلغ رضایت نامه عارف آقاسی مدافع 28 ساله‌خود را 80 میلیارد تومان اعلام کرده. گفتنیه باشگاه تراکتور به دنبال جذب این بازیکن هست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/23047" target="_blank">📅 13:39 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23046">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U1BS9SmLNjgLA1UUfP-eWwFjvNNwEzsaAKsi8yggy4jeynJlYTadqU0DO7sCQLctOE5RfX-iPSuQhzlKfLGk3goQJqNkHO3SsMGURiyigIaPGatgowbK3aWL3IotY8YqNgVHHCADVKBdrSezPVrnbRUM1eP9kSS5Vy9jZGi_VHgGemu7vYK_P2_CVImhzT-nGhJiMnNcDViEtufxQqRr-J8iqFjS4Om0pG3AdQdkvEAnVU2UJQsU6SaMsPzU9-C33rD5wzswgWCcwd1DBwzBr_tVWEUUnYNgnC-7u4XdBVh8mKcCdujKtBqja-FE-KwAa6lJcEPU5s2bNxmebvJGsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ ‏گویا پیام‌رسان واتساپ در برخی نقاط کشور رفع فیلتر شد. از یوتیوب، توییتر یا تلگرام به عنوان هدف احتمالی بعدی نام برده می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/23046" target="_blank">📅 13:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23045">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aef75c0b0e.mp4?token=fS1cN5lZvSxxRKbnESEyuG7PKWN71TET_-y8Ipz90-oBwGSYYe6iaFHIU0mfmSTblEN5EXIJIBQ-Wtr7tMz5D0_ndO9pnysD9UlhypbYLDSvP-LH0wEgWFr2Y_uArIBNwOn2GqFVvGDcvCTcy5ar9hRh8qChsa6ijhsvwT-h9-GJmF5x6IOoXzsH9pEa-ITOiUjIO-2IYrzfKEUhJiRqwyTbvbu86ol4MM5tspCirAK-kde3btfdvenYN_R40TiuSLJrgJb38Q1PMiidbeP_HOfYinx2qUmBE5cuvZzZABEpTKTu5pJGAGEQnkCfaov-v15JzSifR9sb-aZXnvsc6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aef75c0b0e.mp4?token=fS1cN5lZvSxxRKbnESEyuG7PKWN71TET_-y8Ipz90-oBwGSYYe6iaFHIU0mfmSTblEN5EXIJIBQ-Wtr7tMz5D0_ndO9pnysD9UlhypbYLDSvP-LH0wEgWFr2Y_uArIBNwOn2GqFVvGDcvCTcy5ar9hRh8qChsa6ijhsvwT-h9-GJmF5x6IOoXzsH9pEa-ITOiUjIO-2IYrzfKEUhJiRqwyTbvbu86ol4MM5tspCirAK-kde3btfdvenYN_R40TiuSLJrgJb38Q1PMiidbeP_HOfYinx2qUmBE5cuvZzZABEpTKTu5pJGAGEQnkCfaov-v15JzSifR9sb-aZXnvsc6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
انتخاب آنتونیو رودیگر و لروی سانه بین کریس رونالدو و لیونل مسی دو اسطوره تاریخ فوتبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23045" target="_blank">📅 13:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23044">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJhSHSXVIRvWfnxOFgxsQqLZk8XVEQ903pZTBmL_0TC7Uy8yr_tggkq2YoFaqyVRkopw7KryyBD1XR_YwJjVVwZCvUzyLpzvqcH2ztDJ5MOiErUc2uAyA1sjTiU_RiIrdIysEoMlWgeaGDt77Im7JLMYDWwy3YbpcoUnvQ3CU5Hp3xaaa0bzIXVUkqFuxQxd8Lzq9qmFQYHzNO-5Jg7VvsYNNXIE2zrhNHyw86bB0fZS_cCSWnvGvAhgTJUjOXA1X75uF6lpo5PPV78gyNXAmaVSvZitWHljvsLYorsutQH5N-4BpKMqd2xIOIks8q-WEByg-BLAgXt026cjpNJWvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خوزه فلیکس دیاز: خوزه مورینیو از فلورنتینو پرز خواسته هرچه سریع تر از بین یوشکو گواردیول و ریکاردو کالافیوری یکی رو قطعی جذب کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/23044" target="_blank">📅 13:03 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23043">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IlKtj9F0OqTlQacPfEuWO2yn60CsL88abdVeOTbqrZE7EZs6oQa8hN2oMAiw6ouNoea6cjJz6b0Xun9JBu-i21p2G5oHbdicSuMetDWEjt8ubfwObDQfMsQGtaED80-sIcbdZkzSz7Zmv6KWLoTR87yuQahgEBs5f79-3cRWrMBHHPUvN9h1A0bw9uerSoC7icOpUpHrkI-SNxnZcrNzJ666SVqG8nkQLG0kFD4L1p9lY2Jq3vD6MU5g1SUuMcXOfRxx9hosfo94LxsnCkab-5gL1XJuOdxNIrfCoXevim7THjLn0YThkN2DSrrStDiCu3ZtegtWTTesKRM-u4Pjrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تمامی‌قهرمانان‌ادوارمختلف‌جام‌جهانی؛ برزیل همچنان پرافتخارترین تیم تاریخ جام جهانی فوتبال است و با ۵ عنوان قهرمانی صدرنشین است. پس از این تیم ایتالیا و آلمان با ۴ قهرمانی در رده های دوم قرار دارند و آرژانتین با ۳ قهرمانی در جایگاه بعدی قرار گرفته است. جای…</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/23043" target="_blank">📅 12:46 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23042">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bu5HfIt6465w25cy5ncp9PPc7MNoc754LEhlIwxJYgz7rZCAu_QqieW5b2kt2LUIwIXwTWMIy85IEXYOqdJRKbHU9fDRA6bVd8SvwJaoO-5ywui-jvBXBpq50UwSI9OBDfL4o6g-EhZCk19vY8Ne08hN4R2if6Zeecl9ncHZBPiZNS0_gN0v9VhC-5u5OZhnAXlDEyKZqZwe6jmuk2Vy6hyojVpLiGJ1m-Qe4oAyscUo5isL5kTgP1ZsNZtdxZtLr-D0OBGd6e1qlWAzzrTHMFAI3Bk1XwXqQXr_stPLfIhEza9EZn1mvu6XEIeu5C-WgRSAMA5vtDoVsj1o64ekYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تمامی‌قهرمانان‌ادوارمختلف‌جام‌جهانی؛ برزیل همچنان پرافتخارترین تیم تاریخ جام جهانی فوتبال است و با ۵ عنوان قهرمانی صدرنشین است. پس از این تیم ایتالیا و آلمان با ۴ قهرمانی در رده های دوم قرار دارند و آرژانتین با ۳ قهرمانی در جایگاه بعدی قرار گرفته است. جای…</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/23042" target="_blank">📅 12:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23041">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bm1eq1dJ8yZEwYE5uqY50afpKog2Gf5DP3Jm24XtDGqb-AgAca-8vsGzqLBHzIMl2nlVJpCXDKZyVzs_qZ7FBy2Dy97u1uFqGVHDIcuUo2p0ICFRBHJ0jGTp_ZHmwYCpnVh7x9rLfHFxaov8U04zbBu5Op64XxGPzgsGApkdRcsXXoxu-M-BKEn5VjWVAUxJRN1smiDPQU6ZNbuyc5eI5QzM0iJPhCc6b3hnKz7Bcxu8hZIJ0yQV5jSl2CfnOKTID5OkS0HCEGGpsSUGvRTn6kowhgsf_OqbDrcrhH0BkUpzbZLeVAwckIM7W9DIxOUnI0LY_CuTeuZZ5Biu81axUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
یادی ‌کنیم از مصاحبه تاریخی مورینیو بمناسبت بازگشت دوباره به‌یکی‌از داغ‌ترین نیمکت های جهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/23041" target="_blank">📅 12:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23040">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oyFLzcodThaiST7rdTUi0qF5oOPADhHS42unITNYHkRpU7ISe-ajLOb8Xy2VIgavuS2Zdk4pg6tYv5GYBTGK4WXSlAw8qNHM5qVLcl5qkUJ9WoETijww33VpSKdxtZxJuJLNg-WAa9Ge-oQ11KENulA57N5tFin8a7dhxkidI5BldR_Q3iWCI0ZUzIyGc8E9biUxHU0J0Xq8fSVZPEg7sggfA_eUGdCSl89_lI8OhuHfPDHTYOgvcfO9tJgoNyE-4NYQgPuEHW52OZSMskf3B5nlXyNBpxyXteQNgtLVx0u2u1tH6wziRU98wnJj3sKnPrYvMfqsWQDiA1CimeHNug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
#تکمیلی؛ ایجنت کسری طاهری به مدیران باشگاه روبین‌کازان‌اعلام‌کرده که این بازیکن برنامه‌ای برای بازگشت به لیگ روسیه نداره و قصد داره ادامه فوتبالش رو در لیگ برتر بگذرونه. باشگاه روسی‌ هم اعلام کرده هرباشگاهی یک‌میلیون دلار پرداخت کنه رضایت نامه طاهری رو…</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/23040" target="_blank">📅 12:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23039">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4860b42130.mp4?token=NnUhEFD4ctTK7l3K0-5oweqIQuRqihZekwmdXI5LO5-ju_D-c9coNwr6iYJ3kCLJNfjThj43bkUo_liVkEc6c_bUmbxE4Tj1gwRmOrhWAxO6KVn8--JAHrLqsfQkLQTuX-vEv8NndMxOdslmYZjDeY5yuSdpjkDqQ8osE5mmMUWTTB1TIdy2UwQaz0w_L51vIswvEPopnzW5rr2PX_XxGwoQll0rSrT1JQ1f4YRPURo7Srna64c-8giZ8079IcljzY__105-sJpYNK6ikwJ45ZyQZUGDeUuAfowUVU8B4EO6A9n1bLsQ5C846qgNMvrh2_LXz_WNKS3EtXJVZMftFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4860b42130.mp4?token=NnUhEFD4ctTK7l3K0-5oweqIQuRqihZekwmdXI5LO5-ju_D-c9coNwr6iYJ3kCLJNfjThj43bkUo_liVkEc6c_bUmbxE4Tj1gwRmOrhWAxO6KVn8--JAHrLqsfQkLQTuX-vEv8NndMxOdslmYZjDeY5yuSdpjkDqQ8osE5mmMUWTTB1TIdy2UwQaz0w_L51vIswvEPopnzW5rr2PX_XxGwoQll0rSrT1JQ1f4YRPURo7Srna64c-8giZ8079IcljzY__105-sJpYNK6ikwJ45ZyQZUGDeUuAfowUVU8B4EO6A9n1bLsQ5C846qgNMvrh2_LXz_WNKS3EtXJVZMftFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویژه برنامه جام جهانی با گذر زمان؛
از عادل به یک مجری وسطی بازی بدرد نخور رسیدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/23039" target="_blank">📅 12:07 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23038">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/osM5gMx2ZtGHPhWbt_NwGowyqs1Q_eVH6HBXW5tn9WcPZqIHinUIWsraGMFRX7FCcoXQ1nv-V3Y1sjLL90ybTG7ihSthiXCy5zNelGS9nYLM9vI1nADqULkpsEwVwXUtJud1nDCrv9x3G4EjllRfoqYX4jNhlxIYa1FWD7kaFaXp1Ght0bOfZP8k54BlIveDqwOCQgBy2YXi4gM2AvC_D89oF-7YJc6H8sbzEdzrqnRRAAjBcUGmQ5GFxzhQ382p1C3JQEg9u31emPo7uwWtl3J5mynV_vTQ33_Wpi0E1GqhxpHqEcTU3o-nLE331tjT3Ufjs_Eqlo1D1q0UcrMLTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تیم‌های ملی رکوردار بیشترین تعداد پیروزی در تاریخ رقابت های جام جهانی؛ برزیل در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/23038" target="_blank">📅 12:07 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23036">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eeZp3SAJfE9FgUQFu2zsJeZyK2-zlsIFt97WdPgN8IexjX170Zl9kAnS2BgRykLyc3X48x_CBW_xUKX7lLJpAAQzmIqa8HmhwffWfv3CHu8Y2yeJgeRh3JpdCUZ6VnNyM2U3IlAUGtfPGsbSaYM-pTz4KGsTJHxoJ4XkFXaFXVo7DQmQlHcFzjbBTP19Ce6bTFu4Rnx84TpbCmzqBzaAcRxYFtQt1QnZAyIFMOgvyppj68EAw-vjAvei9BdCJpUKfOPQM0gaHiSRyDlXADGJ6BBxeBAKr9rGQETbOU_qL9lKmqbnOOoc4GGvK3eJmUyDQjEzAAd8SBPsw_hAVs8mCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ پنج مکمل‌ ضروری و مهم برای رفقایی که بدنسازی کارمیکنند. هرچند با این شرایط اسفناک اقتصادی مملکت خریدشون شاید سخت باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/23036" target="_blank">📅 10:01 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23035">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sa-qp6rwyLUDo2L8Jr0MZU6IeiRRmK6rTTANZHx8gdWOEFjyTPXlG6A0hf6Jaup2fssm6HsSbj_mlXjOzgwwkb2h5B54PEKiFLWLbqsIWUE96BzkvAx4OH1bSIT9DBWF74vHZBcv-erjLa4d2quUoawu_iyis4mNqH2Dg3vgTcp81kQEXL6g3BDeG8-KkcJY7bdN-B4rCkMoCkssdqjU2UjIMwd81A0DHGtmK8LffWTOAtdjn-o4mOTpdPvttdAZEbhlSahPgUaiQfV5fYdlu_46GBljWOXxBG3kmOvZfR_MUjq74htqaUglE60f0LUasJAeEWcjJPpMkWwSV3iEyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
سوپرگل استثنایی مایکل اولیسه ستاره فرانسوی مدنظر رئال مادرید دربازی دوستانه امشب فرانسه ایرلند پیش از شروع رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/23035" target="_blank">📅 09:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23034">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q5Yk8we06H_3zPsns2X_CmBCjNNk0HFdC1_1EBzeHIRsYKvuKbTOx9TJ48rt5zM4C9JKEKxo13lBlEwjdZrb9wJqpVStx4RMwL9U5hnYwRV9v6vX2G6nsNbIbvckEtkBeTTL4xMeKltc2sd8VCAexcOpXz8bYhPvQvYmCLjTi9rdyF3fecWPdmC9UWXzQ2Qs0HfAwxMqaMxAxHgLcOjN2cyIxx08mHVUBw5R5LPUKGc_uNxW81_SQ_njGeiKNyF-oehIJ8ItnNXxmlLGK4WM_oO967LMgQpwjLS0O_rVLROoz7gH2fRiF4ODmRqo0ZqlclYwTocSwUY2xHcyvb3Zwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#نقل‌وانتقالات
|دیمارتزیو:
فرانک کسیه پیشنهاد تمدید قرارداد 12 میلیون‌ یورویی الاهلی رو رد کرده و میخوادبه‌رقابت‌های‌سری‌آ ایتالیا برگرده‌. یوونتوس علاقمند به عقد قراردادی سه ساله با این بازیکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/23034" target="_blank">📅 09:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23033">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D0-N44Exm4dOH94izNbCCtIzpykbww0VH9Bx60vwzCnpk4jg4nnGiKBqy5CLZBsQeCe4_o-GXrc3XFu3hXXemP6MDQF87sos3cBlww95C12l6ld1mhN0wzBkW-xDWuwDzuToZcEzLMAnNyHsJVTeuHAonYuHjd0fuu44hJDf0x3OZY4h0K7Z9VFiSMcZ94WyJaZBkV4zqfihKCdJGNI-neZpOZ9FCpRwxoHEEV2ADL-p8-6l3P2rSa6ltGWWgSZHWH3Bcs2cE3gckBJZtl20BWBiFNbD-rzBLslNkExnwBf_1in1jgxBJwFjx_phW15ddK8vWMPI9jBdjYCtH4-Jkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛برخی‌دیگه‌ازشبکه‌‌های‌ماهواره‌‌ای‌که‌بازی های جام جهانی رو به بهترین شکل پوشش میدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23033" target="_blank">📅 09:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23032">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MamqHpMBZ8PqV4MKtXcani4nBDkemUDjfw4vVQgUNG4FajhKht64bch3QiCdszLTD5svgW-TJWN5qS8slVl6-mCprS95swXgHuS6tdvGaTlqEJxHIHW2gsPb_snHfxIJ_MXMOLSMEsQgXZDGVyUFW_vzJrhXP9E85s6a_tPYrWiDTa-_-lIFDvMk71jyRKzRP3cimVXGtjYKTZAFurllpKY0Wrwnx3_nSC4ht537RTOMey5bGjLQp3eTIcZjxoKfZ8uRHVBrr2cRjTdMz31Xf8i_lEP4ySKyUynFYFc2hKE-OgQMRcFAEbjvCDILk5QC8_A4dSJaJ8B9IjYPija20Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه سپاهان خطاب به نماینده محمد امین حزباوی: هر باشگاهی او رو میخواهد 70 میلیارد تومان واریز کند تا رضایت نامه صادر کنیم.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/23032" target="_blank">📅 01:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23031">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PjgsarTHREyzS1zY_psxw-_pd6oBVzqxqSS0ltW5_wSO1C65ny3b_PQMqhopvTkAeszjMeMV2bN8IAdyF1Eo0PaXcWQxh0F5rctRxc-y8yLryN7FIf-Fldf6js7H6SKmkzKb7QM68G3Q17VE4UaIdUIcjy3TtMu6gSxL_v5TcUlikyk96Bg0QvD0nURSj6mGu280GTzC2ZiTSgG4JRpFCyluz9TjrQlOp1bGbxKq0nblx0p0H4cWapM6eqAHS6R0lTZWf1r72XazCxwfkl4OdrICycFsfTFsQ_D3draKHq2hUGQ7camS1eAYFGSx4oVI6JuGP0-S-taIbgA6spRlSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه ‌‌‌دیدارهای ‌‌‌امروز؛
نبرد تدارکاتی ماتادورها مقابل تیم ملی پرو در صبح امروز در فاصله تنها 48 ساعت تا شروع بزرگ ترین تورنمت تاریخ فوتبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/23031" target="_blank">📅 01:12 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23030">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SiKQ37e4C4AY4CStscm0DEw5LA93yl1Y7zH7zcC7r_FFroL6sMeq2iRptVpo-sBPJVzNlLgjWLzPO6iEma9N-8-ghffVqQke8QjXEeO31jYc3zOgEUS1Y2xEzCP2ozbSYWoIbAjDIY0y0_wgjvcCMaQ51sEz2RNdQoU4qxEJExv1So50CwOu_zkZwcyklx9dRfDprvGV0KMQAONefIe2JN_Nw-2vsQWI4nnw17cPOm9XGs34LrguvFYrutz-316-hMJCumVU7LmkXGd2ShDPvh6JXfDhcovAezf-NJVF47Bb5DAwTICJ4ZEs-cu2YT1eN17nKtw8GC6NFZhcUO95DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌دیروز؛
ازبردسخت‌هلندی‌ها مقابل ازبکستان تا برتری خروس‌ها در شب هتریک اولیسه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/23030" target="_blank">📅 01:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23029">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb89dc70af.mp4?token=bOzD_ZxPNUE-bLB6KOTafdUIeKZP6GR2lQUxH5JRfZW_e8fukwoSavsDaFKr4Q5VgF7_ve2v_GXkrfmFMbv8dcCjBa-H6u-RX4Ddfeb7fxfuPazgpAFzcOwKuHIUxz0J2azRqVfcGZ0z0V6-QT9hZTqyTUwcWeml_85sqZISqQlVhFaaqzxNwIWr1jXXCjPtz-xkpzhnXqe8_ygnRl8IeucSgCSxDHYT8vyOlbJSjfVGR547fDg3p1o2xdJZW6SlM0HlFiQEam_2bMyxUkvQ78rAsTVIju7_gNsAs3GTHsJbMvAilovRM2iUw1O_6QcarVcjMXdSMaoUZEm7GVU6oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb89dc70af.mp4?token=bOzD_ZxPNUE-bLB6KOTafdUIeKZP6GR2lQUxH5JRfZW_e8fukwoSavsDaFKr4Q5VgF7_ve2v_GXkrfmFMbv8dcCjBa-H6u-RX4Ddfeb7fxfuPazgpAFzcOwKuHIUxz0J2azRqVfcGZ0z0V6-QT9hZTqyTUwcWeml_85sqZISqQlVhFaaqzxNwIWr1jXXCjPtz-xkpzhnXqe8_ygnRl8IeucSgCSxDHYT8vyOlbJSjfVGR547fDg3p1o2xdJZW6SlM0HlFiQEam_2bMyxUkvQ78rAsTVIju7_gNsAs3GTHsJbMvAilovRM2iUw1O_6QcarVcjMXdSMaoUZEm7GVU6oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
سوپرگل استثنایی مایکل اولیسه ستاره فرانسوی مدنظر رئال مادرید دربازی دوستانه امشب فرانسه ایرلند پیش از شروع رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23029" target="_blank">📅 00:53 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23028">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rEecE0YiCylBoPi3WYs8UEhHgouzf4sOHoihCHFQp3r6D8PSM5NZLev4b7AhPyGSmd9ae7JxXvUTSP40TqSxVyqBj-tvNNl7n-2HOC2lBzKAq0d6C4JESwnkruv1BYrwxfCSJ0NEZijDKL-Fn_B_ookSFp7CJdP6bUz21vPIoxCVqFR08Ap5QoWRUnZ9g-4yHimM8MNMB7VfDEp2o66I7UHa6hn49cumWjuzML142epFrtF9hgfhC5l29Lcz1NrJdqqtrUCqQ9cd_y-4lcIJ3bAthksoaenMd0UrFFvPRPQm13TKhjx2MpfT05LPpgnSzcRtwpAA2wa9QiRQAgJxqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
🇵🇹
برناردو سیلوا:
فکر می‌کنم قهرمانی در جام‌جهانی‌پایان‌بی‌نظیری‌ برای دوران حرفه‌ای کریس رونالدو خواهد بود؛ رونالدو همیشه‌سخت‌‌کوش‌‌ترین بازیکنیه که می‌شناسم و لیاقت بردن آن را دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23028" target="_blank">📅 00:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23027">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91f877f10f.mp4?token=PxfSTcw1HDgUzZblqI1poIVeXyoHKVo9ZVif2wOVy3ZfwGUqCkI81S0m15MfowSKU_pjEpC8L2uedCRbPq-sIhoUNsSiX0ECiU7FDLSCPBUxeHJCHqxlDfCNENtwjXXXqYkrDKVUeCMzLQsT9aG76F3Qqhi76EOz5Xg56B4mB6OXyxuaILXQZEKsyJJPl3LR_GoLQG8zA34clL4WB98UJlSinr2dNnRgltLLYgf2cxNXaNaBpBycNWhJhNGLfvGSdXQuLAqCoerRD3eyCn_n7wfwqvls0-OfigD9QkWhMKYArG4TdJUPOmwSTIdzz4Sb8nwPTokYiSVYfnSu-CVrYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91f877f10f.mp4?token=PxfSTcw1HDgUzZblqI1poIVeXyoHKVo9ZVif2wOVy3ZfwGUqCkI81S0m15MfowSKU_pjEpC8L2uedCRbPq-sIhoUNsSiX0ECiU7FDLSCPBUxeHJCHqxlDfCNENtwjXXXqYkrDKVUeCMzLQsT9aG76F3Qqhi76EOz5Xg56B4mB6OXyxuaILXQZEKsyJJPl3LR_GoLQG8zA34clL4WB98UJlSinr2dNnRgltLLYgf2cxNXaNaBpBycNWhJhNGLfvGSdXQuLAqCoerRD3eyCn_n7wfwqvls0-OfigD9QkWhMKYArG4TdJUPOmwSTIdzz4Sb8nwPTokYiSVYfnSu-CVrYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇸
باتاییدرامون‌آلوارز؛
مورینیو سرمربی فصل جدید رئال‌ مادرید برای کنترل‌کامل رختکن تیم رئال، پپه رو بعنوان دستیار خودش انتخاب کرده تا بتونه حواشی بازیکن های داخل رختکن رو کنترل کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23027" target="_blank">📅 00:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23025">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61689d1d82.mp4?token=XMPivoSk2N2AT2MZnC7STRuA2jBuXRHY2dmkIUjIHehPEXxEmg7Ab2PpGCt1WS5qUv7ax9fD5e40bksYNGzrQJsIE4Nnijc4TW5h9BxPlEi7GVCexWFgEp9nlfnvACyPy15NTa_4dj4LHNdQWtlbFqXnpNcvHLw65AT7VYkPAhormo10jqx6mxOQutrwRrEh5Xd-KAaEu3aZpjc0M_ycBrKwyCCIkD4eHoRrofc0rRGjGkw2YXcRA7IMzoCxw68cafGm38m_htcL2tAduOEJvz9f7vCpmv3pkKBZ4BqFsx-khsgnWLR63hwJsQ5bMmfwh76H_qfu4DUJXbujl6nyrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61689d1d82.mp4?token=XMPivoSk2N2AT2MZnC7STRuA2jBuXRHY2dmkIUjIHehPEXxEmg7Ab2PpGCt1WS5qUv7ax9fD5e40bksYNGzrQJsIE4Nnijc4TW5h9BxPlEi7GVCexWFgEp9nlfnvACyPy15NTa_4dj4LHNdQWtlbFqXnpNcvHLw65AT7VYkPAhormo10jqx6mxOQutrwRrEh5Xd-KAaEu3aZpjc0M_ycBrKwyCCIkD4eHoRrofc0rRGjGkw2YXcRA7IMzoCxw68cafGm38m_htcL2tAduOEJvz9f7vCpmv3pkKBZ4BqFsx-khsgnWLR63hwJsQ5bMmfwh76H_qfu4DUJXbujl6nyrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
خوزه فلیکس: فلورنتینو پرز در کنار اینکه 150 میلیون یورو برای جذب مایکل اولیسه کنار گداشته؛ 150 میلیون یورو برای جذب یک فوق ستاره دیگهه کنار گذاشته. پرز میخواد این پنجره دو فوق ستاره به‌ارزش 300 میلیون یورو برای مورینیو بخره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/23025" target="_blank">📅 00:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23024">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05fac563f1.mp4?token=Ha-ANJEzsPqUnyH8xRDjXq41zqJxGxt6zQYh8dFLtKmcmJXcxJnEcrXu5JVlVpi6nz2Y_dx5cxNIG4yk2cCrisyWZ4JkhIYfa_duePkp10hI_yN0BT2k8uT49_j0ANtXoT6aJZZLutyvMGe0ehSBSflDa3RFi6_00eFMjMYHcgw6ATf_ugGok3B2vcJuGzZFg1DhIcJKyN8Ut_kHM_y8-B5bMpyL2zHkEOSG7ljfFkyfeM0ocd9jolUs8DmT6WN-gp_1X5NLRa5Ep-HRXdD4k7W8v1RgKSQarGmUyuEG6XNjatNu9B0R5W0dt5qD3mO69F_iqUUShQKSgq-YBE59FqqmPTyVXctWe2RuUTogV8W1GFnuR10_aJDeRn41OxMP9E0PQGqPANz0CVNRtxQfUvnY-UgVzd07JxCCy8AFjHbFKXUkwopojWNya8i5aacxaFr09BfqW2c2qoo31Xl79abDs09oBofZsPndzpKvTXherY3SDin0qLyjI_1mzpk-T-G6s52iG5GY1093KDNW6EP41_KD_0AYjI3YDPv95UU0wHyiuSAoTTwmvG39vuOvEa5A7T21LKz6at5rTclB4fxl43NDnl434ZJGWu_CoYj0t8eWuUtfJ35FX-SiwhpEJdMIZDndly21d8y7dlnqu6PiygLqWra0Up8Jx_bPDIU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05fac563f1.mp4?token=Ha-ANJEzsPqUnyH8xRDjXq41zqJxGxt6zQYh8dFLtKmcmJXcxJnEcrXu5JVlVpi6nz2Y_dx5cxNIG4yk2cCrisyWZ4JkhIYfa_duePkp10hI_yN0BT2k8uT49_j0ANtXoT6aJZZLutyvMGe0ehSBSflDa3RFi6_00eFMjMYHcgw6ATf_ugGok3B2vcJuGzZFg1DhIcJKyN8Ut_kHM_y8-B5bMpyL2zHkEOSG7ljfFkyfeM0ocd9jolUs8DmT6WN-gp_1X5NLRa5Ep-HRXdD4k7W8v1RgKSQarGmUyuEG6XNjatNu9B0R5W0dt5qD3mO69F_iqUUShQKSgq-YBE59FqqmPTyVXctWe2RuUTogV8W1GFnuR10_aJDeRn41OxMP9E0PQGqPANz0CVNRtxQfUvnY-UgVzd07JxCCy8AFjHbFKXUkwopojWNya8i5aacxaFr09BfqW2c2qoo31Xl79abDs09oBofZsPndzpKvTXherY3SDin0qLyjI_1mzpk-T-G6s52iG5GY1093KDNW6EP41_KD_0AYjI3YDPv95UU0wHyiuSAoTTwmvG39vuOvEa5A7T21LKz6at5rTclB4fxl43NDnl434ZJGWu_CoYj0t8eWuUtfJ35FX-SiwhpEJdMIZDndly21d8y7dlnqu6PiygLqWra0Up8Jx_bPDIU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیوخفن‌ببینید اززوج‌های‌مخوف‌حاضر در جام جهانی؛ مراحل‌حذفی‌قراره‌بازی‌های‌جذابی رو ببینیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23024" target="_blank">📅 00:17 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23023">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eiPAcZfd9rhKu_BJuVmsw2lizWwykIxJBxNXSMb74hSS1xXAbK3Epyfd8O2T5qaUbnfGBVOB8Dx7BhX14kVPAjfIQeJ9AKvkKYUZQVtZcdOqk3GS8MXy_T2XerxcDk6GCLdzYO7Ij-snxDWJ5MANsgdiIWPQ77slCNSf_RF87J0nj7gHZaoTFY8XOxBWPcez-zyLU7DvDo9TXV0tzOnHvdUHvLlvk8Pv0l8ALBQdPD5HN5tVGEhfBkurVV4gRBS5ew-Q_Uju9oy5D_XQ0CcIGtivaTkIEBF6NBwYAERVmywt6RkXy_i49kx2eMEvDwhen9CpzssHK9ofSQlZ1doLvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جام‌جهانی‌فوتبال‌قراره از 21 خرداد شروع بشه. لیگ‌ملت‌های‌والیبال هم از 22 خرداد شروع خواهد شد؛ برنامه‌دیدارهای‌هفته‌اول لیگ ملت‌های والیبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/23023" target="_blank">📅 22:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23022">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LddBlZuK67aJk73hTleR_IQ2aBv7Fe5J4qRq7iEnJy8gQPnRoP4nPxZlGEYQEFnUz9snrwFEOXMWK5Iz2ysXL-1kz_Q8jZew7SVQb3HkCoxe1Ae-2KfhgCPT0Q31nsdJ7jtngcyZ7Hdbw4Sl20tq2azqOzc4vEya4YmU7vSkNY0bQcUC09vNOwgICpK9Dgi7zlcPYu90zw6buZeyAGsJjv9NNPdkMAvd8uPpVAXWJkh7p2Wkzsb9ByV1Dt4r1riT2Wje0m3qy0tqLDlavuDw9z8SkACRkyGkeHmGE9sS-YYaUm8jf7qASmP87kSQGSCd2UIXSDT_6dJMwZM4Xcv-qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی: فلورنتینو پرز با 64 درصد آرا برنده نبرد با انریکه ریکلمه شد و باز هم به مدت چهار سال ریاست باشگاه رئال مادرید رو در دست گرفت.
‼️
رونمایی‌از ژوزه‌مورینیو،دنزل دامفریس، کوناته، گواردیول، ریکاردوکلافیوری،برناردو سیلوا و مایکل اولیسه؛ برنامه پرز در…</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/23022" target="_blank">📅 22:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23021">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hwz4_A3jrWmLkIbxyEH1iH_kOhJ4NbuiGV_XlxydNS_yEzY7odFjNMuZGbfiEaA9uIa4rzBqu_K41cv4tfI6VM3hIKmv4YGJazN-MAePdT-skUzW0LypDJ4EacvSkhlwO5pwj92h1cxni-8l2Eq3uFZax_u3IHdOskuR73VmoI7gQ9e4aP8irkQtSLMnF9Q2gTgsJLryhOcHtkjnuKDN4kedxKk_GGBx1sTtCjNTwyF6cw4SdhH6Q2D_aNLSC2hpobFIeKu5HDZsQSZcK8YK66pQG5jdrbmH3S7IDoFujpRlPzmVv0vrzOdakpA9Q4jPG9lKS8ZjjXlAflRYvRWLlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام‌رودریگو لاسمار، پزشک تیم ملی برزیل، نیمار جونیور از مصدومیت درجه۲ساق پا رنج می‌برد و ۲ الی ۳ هفته از میادین دورخواهد بود. به این ترتیب، نیمار دو دیداردوستانه‌مقابل پاناما و مصر و احتمالا اولین دیدار سلسائو بامراکش را ازدست خواهد داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/23021" target="_blank">📅 22:33 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
