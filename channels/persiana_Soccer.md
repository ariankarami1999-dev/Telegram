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
<img src="https://cdn4.telesco.pe/file/BfD5Scqb9-lcxgvvsVgL11eeyjZEiEPfFq6aJzYmBaHPtRZw8IkbdBZz9nPD2E6Ai4wgxOO7C6nbPu5uL73MravNhUYyR8-Rw7NyEn7V31dxihfY_Zea8qfiut3M9gMFXua-ZExgkVx1eWolWjAipX3N3r5Lg-t0uqYlm47eGpfPzufKhxa7Gmgsrnlhcyualh2tJWW7zH_i9NOwNQKUs96_Cp9lgSCNmQ2xEQMuT-AgfUewVV2bubCeyiJQDHC4b-5r8ExaCt-pVgFivzopkmcxbs8mH5UckaCYnpnMu_WEr-TOaOX_oQBayCGuK5EgqQPEl9JCRKdfcX61HxXpBw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 311K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-28 23:42:23</div>
<hr>

<div class="tg-post" id="msg-23794">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RRvl_94ZC_XerG7pDEN09BUoUiMQcqJGdM1zjhXL2pSUJ7KJMYyJI5MusZaHLX3HFoxBOFKpdrlxysHj-7Ys_3RHSBXcBSgmrsRrYjlFri1SyEgqCnB3fmBfF-a3Kw29GDisMSiGi3r70PAVUPU3VVc66FBGvU5-uuXnFLI53p3yRWjxP5gTpik6lUyasOgEJsafV1Fg2l00L5L_25AOTyM1ZFxiu1dg9W6_T_lqCIrxiWc3TWRso1I6KbTHLTADexBy9bRKwzOzR-yfAqoNG_mEBJ8-lr-s6ovPdcoIgi_8QKNVkqy5-XsBgUl8Y9YZOhW9TPXY7qrRRhXbFVbXmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aE1hjhM2jnt2dCxM_Y2kdjquqhNwc4Jq1DNSm6YR2u6yKen87cZkeXyyvxXoR1c5ojNK6HnerkmsfWeNlcS0qCkMNJMjsSThDsDEbMLUaeDwsKk5P7nKDdWRwEdcMgdlXn8HS68A22wkUYo8b6Ee18YOd0Vb3v_3jUPayXfVQDcYBUyOgf9dHqdHVY2Ga7bJgNVwa9okE6vYgiXj5Y9RawDS1e-tNQflb2rmfImOrubMQVUtj8NCSEFTtX2EvoUi1BsG6TEpmCSuM3Mfzi81phBk4LIRzrBqOv1csgDgMe6od2aeQNKe4W1kF0qPds9ywsgovroQi_RuLDrOWF-W3Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
👤
ویدیویی زیبا از شاهکار فوق العاده علیرضا فغانی دربازی‌ شب‌گذشته فرانسه مقابل سنگالی‌ها؛ همین‌عملکرد درخشانش‌دربازی دیشب که دو تصمیم فوق العاده گرفته ممکنه باعث بشه که از همین حالا بعنوان داور فینال جام جهانی انتخاب شده باشه.
‼️
دو تصمیم مهم فغانی این بود:…</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/persiana_Soccer/23794" target="_blank">📅 23:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23793">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UaW3ygb42RPTmKXrcwg7GS1Qu0mhI-2cVNR-JpscKgjaPKvFYbigVdFA8r_EbDAC7SW-6PAWoDezVV5yfJvyDMtR315AcgKf33TE38uZPCoS_cbqgC7GQkrRgXof9D-Ajp1WSUsNi0mCtvbYigL6WffxZ33PwnUaTOj6sIrhSRzmcD5frnyHCobwBPzlUAQyReU5Oijd428PYzCrkIpSkq6feUOjy3CyWNZwUZ9AhcVMhEqqJdWOdAECYjJJ1CluZfEbEHMfZ-k4XCyHDyD_4ZuXcbaA8lh3TPZmTevW2AypnhwJUjdsnKsWPzFGCj7mB9Ui66faGfTT734mYGJTVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
با جدایی ریکاردو ساپینتو از تیم استقلال؛ رامین رضاییان کاپیتان دوم آبی‌ ها در پایان فصل به جمع بازیکنان‌این‌تیم بازخواهد گشت. رامین رضاییان پیش از رفتن به فولاد قرار داد خود را با استقلال به مدت 1+1 فصل تمدیدکرده‌بود. همچنین وریا غفوری نیز بزودی زود از کادر…</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/23793" target="_blank">📅 23:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23792">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4f7a0d943.mp4?token=Z9iKBpbiv-1UpSs3P-KgrYb2PivjRKPyAuui-E4QlkXmmuGuQaNcAQ0O-UKrWHGhShUou1Ix38ikezkoM2AYLV7OHczIJLXQjP46esBWEKHWtqrYlzLTS8FavpAx5fncmK_ZNubENK4Q-X1kP4hG1gLHlyepF-RcJ8WOiwZLuPFWgxgiHHESsFub8FR7Fo7qxq4moJgqhphq9ywFGTs8uTdIQhLdrtkY6t_UwcETHcKbat8SFG1HnhVK4uWBbEb9dUaTse1ad4q4BoqdCjRJGP3Ko3YIf8-qbAzBbR-Y0RzOUxLlYCUHybp0ny45-Xoc777czIack3rFCjn0-jfKupMD-r6gVHQEi8E33ct3kPVkr_1HXbtS_h0fiFa-uNvutohXFJ4RmSrJ38-YjM0gkoejdBhhpBoGwCJMJ4UrPICYYmMXivJvF5fzzZXEmaoQuTJqjLKqPaxHed7L_9qoWBSstuk2c5Y3CXSH8COB58QDi1IMvrwdO6d2fNau382aVTvOsvwN1DbmQPlVdZGc0WTAMOjmD69hX8ePRcloPc350oalcWRrrh4mU9nGNFYlB_kFXmu0uMcmOdwqa0ONyyuf3272DCW3V69g5g4e0Qm4sqnj2QyOBc8ODmUj7z81IIv4nPtWwO0d1C0YqOxCDyNrjCKHYzXQMOagjrJCcaI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4f7a0d943.mp4?token=Z9iKBpbiv-1UpSs3P-KgrYb2PivjRKPyAuui-E4QlkXmmuGuQaNcAQ0O-UKrWHGhShUou1Ix38ikezkoM2AYLV7OHczIJLXQjP46esBWEKHWtqrYlzLTS8FavpAx5fncmK_ZNubENK4Q-X1kP4hG1gLHlyepF-RcJ8WOiwZLuPFWgxgiHHESsFub8FR7Fo7qxq4moJgqhphq9ywFGTs8uTdIQhLdrtkY6t_UwcETHcKbat8SFG1HnhVK4uWBbEb9dUaTse1ad4q4BoqdCjRJGP3Ko3YIf8-qbAzBbR-Y0RzOUxLlYCUHybp0ny45-Xoc777czIack3rFCjn0-jfKupMD-r6gVHQEi8E33ct3kPVkr_1HXbtS_h0fiFa-uNvutohXFJ4RmSrJ38-YjM0gkoejdBhhpBoGwCJMJ4UrPICYYmMXivJvF5fzzZXEmaoQuTJqjLKqPaxHed7L_9qoWBSstuk2c5Y3CXSH8COB58QDi1IMvrwdO6d2fNau382aVTvOsvwN1DbmQPlVdZGc0WTAMOjmD69hX8ePRcloPc350oalcWRrrh4mU9nGNFYlB_kFXmu0uMcmOdwqa0ONyyuf3272DCW3V69g5g4e0Qm4sqnj2QyOBc8ODmUj7z81IIv4nPtWwO0d1C0YqOxCDyNrjCKHYzXQMOagjrJCcaI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
خاطره‌بامزه‌حنیف‌عمران‌زاده‌مدافع‌سابق استقلال از کتک خوردن مقابل بی‌آزار تهرانی؛ حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/23792" target="_blank">📅 23:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23791">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HsZM8hCPmo-cuCOHvstd-PDqTpb6HYjlPYWiL-Tj8Nea0MtyQ0o0F7x89GP_usovq9klTsdBWgaFIsMEM4vV8ul7SMbULRC3ziLT12tOy8-ROfQ3cs4AOavJ4TrkJr0sMbLEKtidnlTp2e30FY8J91UOe6BvpHAkptufNjEe7fR1S0LPA3BArVM8SG_Oeq-7LwDO59g6Rgnx62rNAhw-sM8EakUNtiuPJGLgP7fEvEKpsavr21C1hh7SViNU1C_1rsWrV94G6gr8cLaIn3hY8wkcw9nccS98ok1Zf1u4uNKThh2WMsdrdqSIq10hTEwaYfH7Aj0WtlwWVe5gOBuwEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛طبق‌اخباردریافتی‌رسانه پرشیانا؛ مهدی لیموچی از طریق مدیر برنامه خود به باشگاه پرسپولیس اعلام کرده درصورتیکه رضایت نامه این بازیکن رو از طلایی‌پوشان‌زاینده‌رود بگیرند مشکلی برای عقد قرارداد با سرخپوشان نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/23791" target="_blank">📅 23:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23790">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YqwmEoaLrnPPdnj1Pr3wcXoY4PnnZMJtnT8xbQsB9h62cMQ-XJ0UL0hD4gvDI04CUtAuzY-8boY8aRAXBLUOADASiIkJnJgnFq5EuQ1sc1je8GQY9sgEz0crPjvsziqL_nnVfQvgrCWrTz1LJBLT9BKw1iX1el3FQTekqvhQTL2xG-9OmTzkefYRho76lzk1I1k_d9fUarFO7fg-aDAvlxPmIzOO5JQopyn3hTP3CVZoao9-R0W99VDIis5vmUhW93ZCsAECUiMMT-NeI4AmiPD-Wmv_IIywdsX8Q7F_5RB0QLlSDAM_lIIrgctyO6dsH2HFccy_FhzdaqBfUSeHJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بزرگ‌ترین تورنمنت فوتبال جهان آغاز شده…
📺
پخش آنلاین و بدون سانسور مسابقات منتخب جام جهانی
در کانال تلگرام Betegram
🎁
شرط رایگان ورزشی
🚀
100% بونوس
⚽
هر گل، هر لحظه و هر شگفتی را از دست ندهید.
امشب میلیون‌ها نفر مسابقه را تماشا می‌کنند…
تو هم به جمع آن‌ها بپیوند.
🌍
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/23790" target="_blank">📅 23:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23789">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oYm_EAJc9fJ2EUEGiYpYdEon9WpzAnIIKxj3QBscuMRylcu-VU4gUQqsseQtj7Nix0rSuAEzBUgK2D_CXLrIZAe0MWrOkbL6J8E5f3ywPcsKvmVIsmD7IHWEx-2OJqldVFIN1jxWryykafyGXgqqZ98c9ubndVIsD1ARq6BU32JykgmqOSF7snusSpolX2JpylDhwODp-HfAwozAPqvHnJEHCwyiUS7Qhxk0WneyfneAKYaPnYCrWmPa3NfcFXS6mZNfKMk5HrmdU2IRRI5XbdTE5ZIbwmwkZfJBpGu6OZi88A_5f3Sk76GjaupL_qwMUkGY6PYHfzCSaYINiOpwQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
همانطور که حدود سه هفته پیش خبر از علاقه اوسمارویرا به‌محمدامین حزباوی مدافع میانی سپاهان دادیم ظهرامروز باشگاه پرسپولیس با ارسال نامه‌ای رسما خواستار جذب این مدافع تیم امید شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/persiana_Soccer/23789" target="_blank">📅 22:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23788">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u2XNJRL6Mh4LfT_oS3too-ZZsX-ShqijxuBtdtucUgifnZByPM70g7BdSO4-OlAaC8O9_rTW_dKAGP9Uzdi02ommtQKbyY9AbPilYPdSdWBtnjBnU9IDN5p9XcsKu_reHSPjLjXO_ln5kLgkeB46QTH44Od-QAfUOrfcyiarfjd3HwMsFKZY6m8tGSvrNzb1-ktYOYtd3Ow4UR_tiK6VYJ_uBvDpJRX94MUmqahE34OMCOo7M85fK2D3mpCEDpDymzBTOf6X3CNiIoVYdJ3ZbSqbF0RfaaLQnTKB3f6U_x8kydxddR2Wpm1fxd0N6LBStzGQVjzf6BesNJ1uDxuD-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
مزدتموم‌تلاش‌های یک‌سال اخیرش رو گرفت؛ با اعلام از فیفا: رامین رضاییان بازیکن تیم ملی ایران با نمره ۸.۲۳ بعنوان‌خلاق‌ترین بازیکنِ دور نخست مرحله گروهی رقابت های جام جهانی 2026 انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/persiana_Soccer/23788" target="_blank">📅 22:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23787">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tl_VhYZaan1JHisEsSbdy4hKd6dK9oFmlFxhWxEq6BqdgqE6eYfR1AR35-c2cj38Xu6wh6S1ZqxakjNT-A-ZUw3huiRMC8mKl3KacYUdqGuCuADNJSzPNDrq7JsYv9VBMUmhxujU8GxbA3ubivNHUGTemgCSkF-LPVUMutybPEuPir29G--Xsbd2F2dy-7X8ku3GWLTmBGSbkgFzbeJfnlFQDT6PviQPRSkXgx0FkGQQDPkT6QRCbhzfkBOnjF7KW9jRZeDdAsBVW7kCw3SFtn0cQ3xVVr67n2YcIoozGCRIYnGCtr8yhMJzhMLucx5ct676SV9dbk7st0REJ6YLlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
سانتر خط‌ کشی‌ شده رامین رضاییان ستاره استقلال در بازی بامداد امروز ایران مقابل نیوزیلند؛ خیلی باید روحیه‌جنگندگی داشته باشی که با وجود یک‌فصل‌درخشان دراستقلال به تیم‌ملی دعوت نشی و سکوت کنی و فصل‌بعد با اومدن ریکاردو ساپینتو نیمکت نشین بشی و بازم سکوت کنی…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/persiana_Soccer/23787" target="_blank">📅 22:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23786">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef4d39f268.mp4?token=q2B00IyITiJfpMM49nCbpvmNsINy1a9lmNHtNDpjVJlicUAmJSUkVt6OXAOS1vm6DNf4Od_recsPncMhYwTfQ2CnA4XQjcKN4T3BKFiscp3tP8_AXiyEfFoPGzbNmcvE2DrFwGq3VjbAM_dtbRqjhApMP5S8p60FrbRY0l3R5726gnabaOX_hq6PLguTFEB5JF_6pvdTUiLfCXUvnN8PUnCqPtWrlMIWvA37Ka41AuUYbIRJwTJ43DFkkTdaQj6m_ZVJYeruXaT1vCDNFxHTg5r2lVNntaBiMjdKdURkyfaxZBJQaEOx_D7cO6_yY1529uSyddq6EpgCP0R00RjXfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef4d39f268.mp4?token=q2B00IyITiJfpMM49nCbpvmNsINy1a9lmNHtNDpjVJlicUAmJSUkVt6OXAOS1vm6DNf4Od_recsPncMhYwTfQ2CnA4XQjcKN4T3BKFiscp3tP8_AXiyEfFoPGzbNmcvE2DrFwGq3VjbAM_dtbRqjhApMP5S8p60FrbRY0l3R5726gnabaOX_hq6PLguTFEB5JF_6pvdTUiLfCXUvnN8PUnCqPtWrlMIWvA37Ka41AuUYbIRJwTJ43DFkkTdaQj6m_ZVJYeruXaT1vCDNFxHTg5r2lVNntaBiMjdKdURkyfaxZBJQaEOx_D7cO6_yY1529uSyddq6EpgCP0R00RjXfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روایت‌جالب‌ابوطالب از گلر40ساله کیپ‌ورد؛
به تموم دخترایی‌که‌پیجش‌روفالو کردند درجا بک داده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/persiana_Soccer/23786" target="_blank">📅 21:55 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23785">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iH9zYfI95X9y-6Rd0EqqmCVmE4jmjcKa0M8TxckwSuejq0HG15L9QhRyJJ_zlZJWDfPevGZwEmGYlaJRzmY1SlHHWCGdT2fMzdYnXlckCgkhfgCbmj-UupH1aWx1lKgO-P39NI56VGJ0dhnN7i1wVQtVVWrT61v0NqvKvO1gHlRjP-Zu4rdn6oByAyKMNsEmUogfirMy3hxpVSLRXafHKSMh3U_IXiDVF3L3mfAm0eu6NkERcD6T9wluPvma61EB_R0e1RbvvRgJneRPkuEyQr3AHW26W3Zs2x1ZzDnFdRAj3JPEKN-F4a2NUWrSpNn--rGopS25rFxDBWRLL_aP0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
بااعلام باشگاه لخ‌ پوزنان؛ اللهیار صیادمنش در تست‌های پزشکی این تیم حاضر شده و در آستانه امضای قرارداد است.  او پس از علی قلی‌زاده دومین ایرانی باشگاه لهستانی لخ‌پوزنان خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/persiana_Soccer/23785" target="_blank">📅 21:48 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23784">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ABvpTG4nX94hpg88y4LF4yuX5_G7iOEHFJ3YLSGXgXQWPv33S8peRq9Ja2Y9gQXm7RIBM7Zksoq7NSdgPQbf8mbVKIefBpHArp-SLtgcVKF6B-5_CpReDE-eZAjIhbqatZ4eEzPy6gayPlvd-xmUxJx2qwm9IRsVKS1s_c1YYyXYubVJbzp9Gek76ARORt79vg6nQ1D7Z8jmh5vsa7XbZQWnt4Fv9a3rkMp8prKDaiUdA9goIDcAxD-KEi2tPJnW4rJnpaGlIqnFxR47fHeV-4w-MUzYuw1JtbCcRuDJTwWIF2Wtyau5ld1DOoRf7Zhxbumg_o0Jo3x74cTh50_vEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#لژیونرها؛ پیروزی ارزشمند 2 بر 1 لخ پوزنان مقابل کرونا کیلچه در لیگ لهستانی با گلزنی قلی زاده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/persiana_Soccer/23784" target="_blank">📅 21:36 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23783">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GuzcbyZTiTFmIQS9qV_vHs7lIiT3hXiqjVxUHXhbU0N4Q-g8j373tor5vH0acheTN5I0HdvHoODelcyprs0w6i_3Fxyt1_BNcH3rP7Vie2Lib_LIRW6TH4OwiPOHUYAIAKo99V26yshoFUJ2vSEEoAfL9vWgcbw50CxRRwkwFi7y41pv6_AZQWzflhXEWJUC2KllShuIB5d1Rc3tw-hgrAKVAW29jzc3Pu1p6Q3M3J86Si7B3cklioRol1XYucPAJy5I-jz0Lwa7CvVmWMZeQThihHgj7d20IRkcw26fMtpZMB_oPnHf-SAwnLqjWU211uvNLZ2u19h050eGZTcChw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
ارزش‌طلای‌موجود درکاپ‌قهرمانی جام جهانی از سال ١٩٧۴ تاکنون‌تقریبا ٢٩ برابر شده. البته این ارزش دلاریش‌بوده.ارزش‌ریالی‌بیش از ۶٧٠ هزار برابر شده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/persiana_Soccer/23783" target="_blank">📅 21:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23782">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fSeoEXCOW4DMF_CgfbIVSt7Ihd3ts0LJ2NYdPFnhvHi1mFlFkwV4YCVefYwWVwjcoHsjQQANIM6qJZjxpwsUA2F6mjzwls7w-Vk9aelVuT5gbURHbZN3iRUsGsqnRnel0XZB9WYE7P36bcNkn10xcOhCHAXOyNTqQaVRnnvTaIDvwAVeWMoQJRgFL-d3S1OWbXifZLTlZ-rLT9c68Pz2aVknhPOa_IxItQSXgDfz9gWWsdsnh6sGfrc1o8Nuet_6po-adwyjMM0AqB5grqPlD7tFxl8YTK3MYVXs_FRLI8gXHchF15mXIm0eWELM2z1mrOlAdaQUqI0SRKttEYLFMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق اخبار دریافتی رسانه پرشیانا؛ جلسه مهم امروز پیمان‌حدادی‌مدیرعامل‌باشگاه پرسپولیس و اوسمار ویرا دقایقی‌قبل به پایان رسید و باتوجه به اینکه مالکان این‌باشگاه با درگان اسکوچیچ به توافق رسیده‌اند به احتمال بسیار زیاد با اوسمار ویرا قطع همکاری خواهند کرد…</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/persiana_Soccer/23782" target="_blank">📅 21:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23781">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">⚽️
👤
ویدیوکامل‌ویژه برنامه امشب عادل فردوسی پور برای رقابت های جام جهانی با حضور مازیار زارع سرمربی جوان و موفق باشگاه ملوان انزلی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/persiana_Soccer/23781" target="_blank">📅 20:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23780">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J3TlWDNZD0KvQE9xGJEfb90JtzKZaeVZgp_nsqqL4adLJnWDW7oR5YIblI8vxCsZ9xou3_w4u631MAX5dakO4h4_gXtSnFzthPoLq15BSBTex0-vAynq7wuQ9wyLxHSNYIfGmgO1hIgLcZVowsUBmEHr_RMFvz4dVSFDYFX1AwbgIXxekoYHHo8166GE90KxZ6v1eoWvtfeshR0uQhII1MS3yoUv2EYzyFPnMEFrxFVlm33U8-DalHPK5fpFQArhxuH5MFnFikrkS8pqUC_3jBF2RADxUxUlEt46Lao1jsrkS7U6L0fdtS2N127FIPzP8OIcQFZh4R2sKvzNHAA0Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری #اختصاصی_پرشیانا؛پیرو اخبار روزهای اخیر پرشیانا؛ فیفا روزهای‌آینده پنجره نقل و انتقالات تابستانی‌باشگاه‌استقلال بزودی باز خواهدکرد و آبی‌ها قادر خواهندبود تا بازیکنان مدنظر خود را جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/persiana_Soccer/23780" target="_blank">📅 20:44 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23779">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/okL6IhEzKQqqtfstl4C30zrXq3MezdvldRuKyl3Pl_hNxSm8BjmhnlpK6Bet_4DrABWXiUdCtFB_bqg-PleaXibaW1jAXmlCyc4dLbUZQF4EP45fSAf5JiWlNRbiwnD4dzvgrl0B-sM-LQshVIefY2PJTnRvBx9qrqxptTbH7aLFLiCVRLTty1h28rCCRaRs3gVrapEp3g60caRbuCEU5vJhL218SGQTTqrmaAu3dsEQ5n_fbtqBqWJiVhKh7nKn_RG7jp9N6ePEc9BdyHB5cYqKcBEBnKQFptReFMPmdweKJlm1_7b5NCXzHTI9kkMsZV2CO0aBTVUODvB_Y1B9CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
هفته‌اول جام جهانی 2026؛ پیروزی ارزشمند و شیرین‌شاگردان توخل مقابل کروات‌ها درگام نخست.
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
4️⃣
-
2️⃣
کرواسی
🇭🇷
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/persiana_Soccer/23779" target="_blank">📅 20:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23778">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TqY2b05oKTJLQbc8daifDEybBcuBgdHbnTy0oDYIPiLKWlV-iip13POtvdwLfPn3gdQDURQpDmZcD548LZAESAWtSE_7iL7_qKXAO-eKzjU5fDepXmxEqLDGAqnW33misfbGvSKzTVUym8omK-yZ0ah9h7f4RINLX8OIifzivC_KA60aYeq_ETlkYhSgr94GLZaF_5JSAnyDQuyfOnia4N2Ci-ZA-03YRL1WGOyswNW6KuAewMIJXwopeLkLkwiJ0Te0Y37ToZohqIHzSsCZ1QHXASYqYgFZb3C7iLm9QqF2PdccFRqnHOfdz17rJkahyR0CfzXhNmg8HMas5wLK2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ ژوزه مورینیو برای‌فصل‌آینده رقابت‌ها مندی و فران گارسیا رو در لیست مازاد رئال مادرید قرار داده و قصد داره که در فصل اینده از ریکاردو کالافیوری ایتالیایی و آلوارو کارراس استفاده کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/persiana_Soccer/23778" target="_blank">📅 20:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23777">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U1CTSavjWo7k2u1M0_7u32FSS6vOe2qSIM3MDchSjNWc_OIW4J2uHwERwFKiz155sYLndbz0AGLMsb6n35XgjYGTiMA29INZwb5oEzsFZvM3fcGqtMFVi_UE31CP2LMVdMDlQTaF62_OuqUzeF-Y2tBn2Vw7L8l9htcScrsnNkr94fTAyb_C2eTyKNt9qkWz7_wZIVefu9nCNWhV821wj-v579uRxgL_9BxmnhCMx4bvVHJJdfH0dQaDhZne8tX2NaQ4P9DUN9SM_mQ_sY80ocmO4P8FeNDdZ5xr_TPW9zPRyqCi3q5RvKXIzNEq3UUI-X2ilHE41CA5WVHvurUMZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
تورنومنت ۲.۵ میلیارد تومانی رومابت آغاز شد!
🔥
مسابقات جام جهانی 2026 را در رومابت پیش‌بینی کنید، امتیازجمع‌کنید و برای‌سهمی از جایزه بزرگ ۲.۵ میلیارد تومانی رقابت کنید
😍
🏆
هرپیش‌بینی، شما را یک قدم به صدر جدول و جوایز ویژه نزدیک‌تر می‌کند
🚀
⏳
فرصت را از دست ندهید ؛ هیجان واقعی جام جهانی را با رومابت تجربه کنید!
🆔
@RomaBet_official
┅━━━━━━━━━━━┅
🔰
لینک سایت جهت ورود :
🌐
RomaBet.tournament</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/persiana_Soccer/23777" target="_blank">📅 20:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23776">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R4nrKQXTQnS3pPwHGyddFG1ZUi4CH_XLCVON7X0P2FZJtTTtNAS9xiFNnFPhP-hxF9nBMffLwi6wQdx4Ehw9KgZDzMdl8HT8TPAjClibCPpR_Nn8WlEczTudwl4uDCnFGLwvvx_MSfWlsVdEG8jRAgR3grSF7fidax6HkzuM4pGVsVTH5c33yehRuC-HFtVWGEby6A85NZRKi_uBJ6ZWjR9VbRgCnMThjZo3mZHIj3q9N7A5BCWrTN8Lg7hLjFKFXw4WIvXbJd-vcaCXuDhAiMxoZaNsFdfWwb3wMmnpLD3kqRgubr5RsiANBOkwRPpP63CLEnKIJTDuEv3BTJ9cug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه پرسپولیس برای‌فسخ قرارداد توافقی با اوسمار ویرا برزیلی به توافق‌برسند سریعا با دراگان اسکوچیچ قراردادی دو ساله امضا خواهند کرد.
‼️
مدیریت تیم استقلال در ابتدا مذاکراتی با دراگان اسکوچیچ داشت اما عزم‌ علی‌تاجرنیا برای اوردن این سرمربی کروات صدرصدی…</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/persiana_Soccer/23776" target="_blank">📅 20:23 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23775">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ceb72d8ebf.mp4?token=PBLVnYIc7bmLhqcvFTTYmcWX1YY_Y5chfbUwkUr_KuOfclWu0SQAQR6Ie-zFhZNnvQk5rq7bL4IZz8zkBGn2ySv8XChTOJKd9Bluc9irdkKmC6FmqWCBJpTfU9jWqT53MYyY-kOINDpl44xVjgRlTdOKzsQfmGwGWxGOsYRgGhKUyN6aC2qRrDau9udDaIcrzpvL8H19OnF4Pn2L1ClXTVL3T1c5jouJQ21MFkJ6GvLxIukHj7cz44fjsxIQU-FyjBlyE10PA1Hi7Q1OOJ3m38C8HqA4AB4q3wAWMbILJOR6JfxeQp_NzDcLGZsISDxjhpbQKxCUQXv0EFGDYlHkvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ceb72d8ebf.mp4?token=PBLVnYIc7bmLhqcvFTTYmcWX1YY_Y5chfbUwkUr_KuOfclWu0SQAQR6Ie-zFhZNnvQk5rq7bL4IZz8zkBGn2ySv8XChTOJKd9Bluc9irdkKmC6FmqWCBJpTfU9jWqT53MYyY-kOINDpl44xVjgRlTdOKzsQfmGwGWxGOsYRgGhKUyN6aC2qRrDau9udDaIcrzpvL8H19OnF4Pn2L1ClXTVL3T1c5jouJQ21MFkJ6GvLxIukHj7cz44fjsxIQU-FyjBlyE10PA1Hi7Q1OOJ3m38C8HqA4AB4q3wAWMbILJOR6JfxeQp_NzDcLGZsISDxjhpbQKxCUQXv0EFGDYlHkvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هنگ‌کردن‌خداداد‌عزیزی‌از رفتار جواد خیابانی؛ از خداداد سوال میپرسه بعد میگه تو نگو تا خودم بگم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/persiana_Soccer/23775" target="_blank">📅 19:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23774">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dVbvmUk4BuZBUO2lE7wIKJXJ7jw4cE9wZKf0RTs1A-ic2idWufRDDi5BYsGf6lrZ_UYDG4T55MD9c1s-gN7qk5XERNyqbk_8I3kTiYa0TaZGIL7xoci-wfEibFMBXDJLo9dNBEbuJYqqUxYImCSh1eWFsk-7-NKW_f4bdbUthK35-DvMYy2HBwwTg_6of_BSRX9eeUEIvUqCrOq4Vm1rxMX1ZvwaimRtzMLvccpnPTNgneqwqrhIENTPdOa-bbtFhGI0Ar1bqevOL9NxpblUMNscW8HqECSx_33Fi4_HnAGgTJNh46FFZStFUcIl28L_IejY2-KEXFuL82wlfEv-Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مارکا درخبری‌فوری: باشگاه رئال‌مادرید میخواد بزودی پیشنهاد220میلیون‌یورویی برای جذب مایکل اولیسه برای بایرن مونیخ بفرسته. با جذب اولیسه و انزو فرناندز پرونده کهکشانی‌ها بسته میشه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/persiana_Soccer/23774" target="_blank">📅 19:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23773">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n15l-U_3vSKH-RWfyJTvoCWJkE54EqsJV2YC-gkeDpGVgPqH9-6NZr0IZHw5a0TKtLpwRHQM3ih_DX9HUobbmKx1ZqwfYPWC5cZhfSiwusOJlBPYyO-bzzxULwBoJIPwyd8GAulN55Pku8-ocUOAxAMmClbWQxRHDG1jXW5MocKkRCavfH15utwztWiskhNWipyW-SWXUcgwIMf37RESW1XWTdmCb5OZmQYf8XelNgkv0EYRaAb8loPwlKmDnWtSyqFrvloANREUWqEFuOiFRyKWCR5RPzCXj015IUi1YrG8hhS0ahnJMtWB8xFJUwrr9d0kcVsj2_oD3YmqGh0h_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
با‌اعلام‌باشگاه‌سپاهان‌اصفهان؛ آرش رضاوند و میلاد ذکی پور قراردادشون رو با این باشگاه تمدید کردند اما محمد دانشگر حاضر نشد به باشگاه تخفیف بده و جدا شد. رقم قرارداد دانشگر برای فصل جدید 170 میلیارد تومان ناقابل بود که کم نکرد ازش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/persiana_Soccer/23773" target="_blank">📅 19:06 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23772">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J2lpRaC8vVtWlBzA6yVYT9KKzTJP_ttJVjk_l3ofDUuHpScuArnaSANXB9Lj9kArDyi1G5QP97byhIHB0OZIuEa4MPPgw5mLkjbLivVWZnaFZpA6Fiu_j0rtzNtztZ7Xacz0nrc-Jy7_LJpTWPh8PDSGBA1jk2Ek8LeyyAuQDug-bw0oUgOfv42Fu5HKZRF4n5LJ-trO9K4oSWjHQ_dEuWbqBnM3whZ2spivyVxZjHRhAQQpiGp5imIJesrZ8SpFZ3MZq6x8U2sAf8Auqnd74m9LrxulfU0o7GUroEADli02RDxO31YEZTdNrCkstZEttR6if-nxwNG48cst-0PntA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇧🇷
👤
برخلاف‌ صحبت‌های کادرپزشکی تیم ملی برزیل؛بااعلام‌‌کارلو آنجلوتی؛ نیمار جونیور فوق ستاره سلسائو دیدار حساس برابر مراکش رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/23772" target="_blank">📅 18:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23771">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CHf4Aoy3nZYKkLjz6NiT7FNiUU7xAEf8mUHj3j-Lw0N0jxLEZ2hxNco0nZYeXtgzzSvFlpG6UvSl8Ql7g55hEMDGmSVXfzEJfDm4epeICBjvgzoGDc0BQrBpkVPzEPNU-4Z9_wRgi7TyM4AyhHLY6NoDOWeAJ-cV2GJy8bGsEFJnUKGNCKA3hnWICU0vLENzS5oWqK-zuGPWzfc1b1oQdOlFArJvk1YMHo5j2Fdoc_qxhSaOD107SSAxaGS9yBYulQbvVWvumw9jL5eu4tdmJAOVMxkEA1gVwSg4xAp-aaWoae--tK1layTPCucVrkpu_dvfe6yJAH9F1oqiSVTzPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فابریزیو رومانو: ماتئوس فرناندز ستاره پرتغالی وستهم؛ منچستریونایتد رو به رئال ترجیج داده و به ژوزه مورینیو اعلام کرده که نمیتونه بیاد اسپانیا.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/persiana_Soccer/23771" target="_blank">📅 18:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23770">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FuIYY5Mvmd6O0-fKw_RyiauPd4BiUW8rmtGkZQz_tDtGjts1vr2ZOyw9hiJnJSnfgqrpiAvHYd5Z5d1xWS8kT_taDktvOxkJ_kqaU7hHFuUe6IRCBrZ1X7zKzfytAUaAguyS1pDuIc3NoFL7jZ6-K-GdA0lau3eTju7KV-SNu30gEEw1RvNdX0Eb66hWeukmm2uof-EgNlTfSsEnCEMS2mlRpPddRpYWqkXaD20kfpxFizAZOd8W-zspaq1fhmvkZB5AG8n3PFd5nJSfXyVc94LxuxqAsKXb2n0PiaGxqAIGUhrolbvpIPdzouTvJVTsXL7F_JZn7zft73SfXpHKqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مارکا درخبری‌فوری: باشگاه رئال‌مادرید میخواد بزودی پیشنهاد220میلیون‌یورویی برای جذب مایکل اولیسه برای بایرن مونیخ بفرسته. با جذب اولیسه و انزو فرناندز پرونده کهکشانی‌ها بسته میشه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/23770" target="_blank">📅 18:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23769">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o03nm1bKaTDPED9m_B6IlmXg8AngadIBaNV9ot-kx3tWnbXIvjsiUUqXYTJkI5rQFY9u-GPuPCaVourUabo3B9Y9Tqu4WnMUGMhMTCH81NN-KxzXS63HQHzM8poMcFp7Mo2-uN7kbICmL0-cPV13SMktmbp7u8msoBL9S2qW_H5Xk5zZBZ_1EjguOxTn2TmNy70qILFIKm6qa2Z-rx18v7TBLAV7IEvlXlqR8LeoRVE_CxQqJ8qaA-zXrg57LXKqfhk3V5KdFxPEuPgiywjOURF83Eigts22mFfKhqBjMMUA63nsTgXk74QXBHaEO-qZdwxc0HPJ_lSv2edcTME_Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
#اصلاحیه؛ برنامه هفته‌دوم‌جام‌جهانی 2026؛ بازی ایران
🆚
بلژیک ساعت 22:30 برگزار میشود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/23769" target="_blank">📅 18:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23768">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/629abdf2a4.mp4?token=vTIcQJmyVbYseAu1WEpXiiu7VhDNaK4aC4kxlQPFo9NcAaMaHtzPgW0v_JET2zGKlTIQyKj5367Z4wtUFDOI8LQh36juq-pXHu8yDvax6LWnHeBKjkR2lnZvDuRAunET--YjUu52yIRoDIKb6znLR8x27uRgIv14NoY9XWxF0gp_rPYQMMPBHIxj2RX-Uw7Nwd2vc12B7tRjdApiT84IRrU1EFF3q4vtFn6phCVgkzeSlefxt5FTeiZvKS5P6LQu1oF-e3ftTMYQ4rUpPeXjTwnkMD8O_JM8yiVZaCyxhk7Q4AlPtJnKPKv_NEKEfDOLIOC5XChC5ednznh3XRneBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/629abdf2a4.mp4?token=vTIcQJmyVbYseAu1WEpXiiu7VhDNaK4aC4kxlQPFo9NcAaMaHtzPgW0v_JET2zGKlTIQyKj5367Z4wtUFDOI8LQh36juq-pXHu8yDvax6LWnHeBKjkR2lnZvDuRAunET--YjUu52yIRoDIKb6znLR8x27uRgIv14NoY9XWxF0gp_rPYQMMPBHIxj2RX-Uw7Nwd2vc12B7tRjdApiT84IRrU1EFF3q4vtFn6phCVgkzeSlefxt5FTeiZvKS5P6LQu1oF-e3ftTMYQ4rUpPeXjTwnkMD8O_JM8yiVZaCyxhk7Q4AlPtJnKPKv_NEKEfDOLIOC5XChC5ednznh3XRneBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌فتح‌الله‌زاده‌مدیرعامل‌سابق آبی‌ها به میثاقی در گفتگو باپیمان‌یوسفی: مواظب باش بعضیا صندلی نداشتن اومدن صندلی رییس رو صاحب شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/23768" target="_blank">📅 17:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23767">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p4riYTDC4yDFUPNAUHZqDyCgPV48GTD3j3XutjSKPy56QAoPWBG5jA5JKsdfI6aKthUJc3hG62wMcYlqj_IgvFfV-90upLv0LTpo9RNfznXaDYFn1IAFuJav70E637rPDT5xZlZTJZPMoOEjGhL0unDEP6R68iyEHVFbwG6CFuNQdMbAtqq8cN_E3wO3GX9bVuZtW5HQB_yYaIX9QtY8-Rh9KS9K-OMVqlq9Tv2-SSeZ5sswP4NcvQepzh37AfZ2hurl8fmGXpbrprrAD6RhW489PPy9G0z1KYJ-8IojoJHHM2fewmtSO5gZ1-zc5HJ6XXdoEwrHzo5jpJFBOiPrUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
خوزه‌فلیکس‌دیاز: فلورنتینو پرز رئیس رئال مادرید به مورینیو قول داده بعد از اتمام رقابت های جام‌جهانی 2026 تموم‌تلاشش رو برای جذب مایکل اولیسه فرانسوی از بایرن مونیخ بکار خواهد برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/23767" target="_blank">📅 17:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23766">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kUVrrt4Ol7Z3FYenRbwJYYFVS8ceTcOIxAKNxvRt5lUC7A0FBqQz5GHrTpZeC6Dc3WZeqohNvhlzk1AQL8ro2JVywobtMZt3z3SmJyd-NBgiuEE0puglT5KGepg23gFbYZD6lyC4OW0D9GcjAAKSE2N_FFajhwb-pANl2vkgMAvIXNRLzrfgfLaXHi2AumDqjNcXU7COMrtMVIsDMd3C9opVZWKzJrMMw1NhlTLdi4PP1f8-pZI_GcxZzLi7L2AVlm3ITQDhv62kJPrZXy5osKPT5NLFv-q2jGGWM5t9q9AJWZG-99rEhS4RfUtrPcolediSSCKXZhIYa7lTDVlqSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد چهار بازیکن بارسا و چهار بازیکن رئال در هفته اول رقابت های جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/23766" target="_blank">📅 17:18 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23765">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WwJXJR5m6e9uYhw9s6FadlujpPdY_sBPZIYj85ACi8qkWmMeL3qhNooKuqWsmcdqdPXaM7HvaHgzGr8fvV2JXAOqgWnOuHaJq0pLP085jbjjJL326P9e0yeBR6887ir0LYIGQ3uULXDmKj7jVm1EeU6bwf3UgGssdnv33n_9lfr06BjRb3QYHjjz9J55vGeuJB0VfsZKH4-m_X9lFJpahGzK8ystzjOQ2uNklp0UpDgA5DbCsY31vdc0qARZFu8xO5q3X2vxeYiwHTUBCM9u5kkvr1PyznflvGSJPpvkQpStWUOH-stseVIJnK5W0jLfBRYUbyQBT4lS9dtkwiboiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بهترین‌های‌دوره اول جام‌جهانی ۲۰۲۶ در یک قاب؛ از ارلینگ هالند و لئو مسی تا رامین رضاییان و علوان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/persiana_Soccer/23765" target="_blank">📅 17:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23764">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ctqPdIP_5tLvJq-Egf0rytROyKIj9MeqwX42jcK-KtW6pd7j3TdH6S2dRmX1f9qRSgXDr7m4LbMSfYCXV4Jeg93lM1WihmyI9uuVTWsIw9GsFeI1jH6ZojNma31-Ag5QRkhxtNL9tAPOWtHtsa5n2zAoxt8MZ4oVK9xOatnocrTQdr3x8PeBOy8eqVSbacy4sjcBgDCsQqSWrIyZnGzoCrNnYcDKEAYvNkyT27ter2BeWaZv0HOHdlwdExYp5QS1WbVHrEfpI-G1kR7OLbP-SayBSmDa12ppIziPAywOMFpTKERCQ-5TK1iyKgJOaAPkseTft7vye8Pu0F6lm7R31Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
خورخه ژسوس سرمربی‌سابق‌الهلال و النصر بعد از جام جهانی هدایت تیم پرتغال رو بر عهده میگیره. روبرتو مارتینز هم هدایت النصر رو بر عهده میگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/23764" target="_blank">📅 16:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23763">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bIN1ru27pk1-cM12ODcILRVD8y19ZruqDt7AkAuzVfjuDMBPPnK4DUr_mFS_gnT1u_HYdjBDBOw1TvME2NwqdvGPGhw3N3itHbB0Mxm50F51veoapgLPeBeEsvvfdbFRmtMU0JIUBeJT6Ey5tJplRTqvSEQChhTUctECAAUKFZIhaxyVvLtyVpS0dUhHKeiYejRwiuuTKrv2DFD41N1nN9nh-MfwDiSxCY3vPBrNT_Mj3qaUiy82hxTRKSWlIKjWiwdpft8Y2JmD_uZdCkG503-VV-URcx51Srfi6uiHhrJarnjWXEuZWn1yD7DynMZ6b5fbNuuBOLAUst-gPYDJhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ علی نظری جویباری مسئول‌نقل‌وانتقالات استقلال با مدیربرنامه های محمد جواد حسین نژاد مذاکرات خود را شروع کرده تا بعد از باز شدن پنجره این انتقال رو بالاخره بعددوسال نهایی کنه و حسین نژاد آبی‌پوش بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/23763" target="_blank">📅 16:27 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23762">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QrFx8ahhkepoAUAGW0yw4Et_SRbknZ55uWYixVcT3ZirlCEe6tUgDOjmdCnK4MBRnOMTPKrdoIS7xqx7zQ80npXMw2dvUylIj0eR4jQUfX0AcsLTxhj4z-ahQxOc6veaQqIJxlpi0cJwwLVSTCocZ67lVf6dkx-ZmKvXKjjcc3P6c-eO651XhCqyQ8P0TsBwq8rdb7SM9g1VX-go85Kvujhkr-Q_3ByC4p4EeaF3kUDyfdy1EWzI7jz7eOdPcd5Gl-r1fmnb-3O_IuMPv0vyLTxJT6qzUKLoQz9n8hDImtoNaG-17HE3NLo3nlm0UZEOznC1trKuItsmbK03fpaXVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق اطلاعات به دست آمده پرشیانا؛ باشگاه روبین‌کازان‌روسیه به ایجنت ایرانی که ارتباط خوبی با او دارند اعلام‌کرده برای‌صدور رضایت نامه نظمی گریپشی ستاره آلبانیایی 2 میلیون یورو میخواهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/23762" target="_blank">📅 16:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23761">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/td-RTQg0GPaX84KS_vQHby6URLhicIkgZBVHrJXJKjgi5W_TkTTG-VIStbPYf2Xi0tV7_FRzTA0wueyFejwyJTXY4eYmwNVCWLOaUxxa8LuHPG6XnQSawVe7y2JK3f-GCQqCcGNFkG12dmVIYWkUu2uEFlKkca1uoTkURG6zAxIub11szgYWT1uDF4oMhEIRSpv-IDiWq4CcK5NncfKrXVAMfleUq-3mrWLf4D7lIS3KzL8EWIxWaRtM_RU3EG75vnJNkW7ho5x8TE-_R27ns1nBVodwC8QODrr-XNKkohz4N99BxOtxxKnk6EPwIAGU8amo5n6AJaqV7Cpyr5wQ2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه‌کامل دیدارهای هفته دوم رقابت‌های جام جهانی؛ این پست رو فعلا یه جایی سیو کن و بفرس برای رفقات که تایم دقیق مسابقات رو بدونند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/23761" target="_blank">📅 16:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23760">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/umlj0jmjigfkObt5tDc3Uy4hvp4knTMVfsPczGKRmOPtU0MSPkFDfD1ZpFExkoXRUrQe4vAA8egazhufQ6f0Pk_TdHD7xMtqXnYBEXstxVBOGBcIFzYoJg2smQifbWtnSm0sRLiDQ-iwQFhaz9XZ_Ff6WyUI1z1_KZ0WZ4-ZKxD7q1C8v104tyf2vuAbfYtU8l9Z93MKNjitKTaSroY6zC6LqbCZD7IfOcR_xFi8kDB7udYTJPbDONWFSCPPYs-lzKIZOADKF6RauGybKl-GQL_-cWYqQIx8M-Z2eiBiLRveWUz_n_ySNXXba9ofvs1cfZMU-8vqbY-t6EgqZlbKZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
نشریه ESPN به نقل از مارک کوکوریا مدافع جدید رئال‌مادرید: انزو فرناندز به شدت علاقمند به پیوستن به رئال مادریده و فکر کنم در این تابستون این‌انتقال رسمی میشه و انزو به رئال خواهد آمد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/23760" target="_blank">📅 15:24 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23759">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mMB1Xrvu4xh6gn1-Y8-eApDNqXcWYnsA4Z-Bz4UnwJQ69FdewQ8pL5TLPEB9LbcOlrCfesvuOvso7-VMd7Cd_tHJlvU00hTQ9pjs57SwKZ8onXH20dnuZPYGtLZ_rIaobTpZFlRHnA-NYusQanTGguxwsq2IP-QR3ZEQpBMo9PMu29zAjMbs5B6z8pyZkuTr4kPs_eHfV_Mmo-qAJqt2a02c-DdZAnOHvQG5qM5GlGS9zRG-waSE8NkoUx-2aK1HibJ5g5w4-yU8p-peXcCz6EJS7OVr51VnVrG2k-uHEQna69_9cdakmMuPdofEsGoVh4EguVoOAMqW1T5Bh4Dp4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚪️
🇦🇷
#فوری؛ باشگاه‌رئال‌مادرید برای عقد قرار دادی شش ساله با انزو فرناندز ستاره 25 ساله چلسی به توافق کامل رسید و حالا تنها توافق بین دو باشگاه باقی مانده است که این انتقال رسما انجام شود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/23759" target="_blank">📅 15:07 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23758">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2e3fa7271.mp4?token=iAnP9eGwPao22Porxe_UJDmKTQpoYj67iJlRMdsjimGe5wbxvKPWOK2M692j2EPzYLOw-vOcsasaaMgx_TtOwoWvPP2XnTqZeg2QQ1E5NAoTgeHZ80TpxUsd9Rt4KS-OACW6YVcxpF24ZHu_R9vqdmaZyGVCcWeSrEYhdJ2TU4YQxIDKSoQAluycWG0fLu_LGU5pIC112VnSbY-u5EwX0rqVNqVx3GSwQxbBzgpceoh0B64oR0NUZ1B6rXFz6RaWw_RFuq9O-IBuagSVtIzyc12n0HPJN0HFN0Jf_sKejPXeBZS75j79UfGKCFKgwR2uP5L10BCIDp4xAxrd-zjh5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2e3fa7271.mp4?token=iAnP9eGwPao22Porxe_UJDmKTQpoYj67iJlRMdsjimGe5wbxvKPWOK2M692j2EPzYLOw-vOcsasaaMgx_TtOwoWvPP2XnTqZeg2QQ1E5NAoTgeHZ80TpxUsd9Rt4KS-OACW6YVcxpF24ZHu_R9vqdmaZyGVCcWeSrEYhdJ2TU4YQxIDKSoQAluycWG0fLu_LGU5pIC112VnSbY-u5EwX0rqVNqVx3GSwQxbBzgpceoh0B64oR0NUZ1B6rXFz6RaWw_RFuq9O-IBuagSVtIzyc12n0HPJN0HFN0Jf_sKejPXeBZS75j79UfGKCFKgwR2uP5L10BCIDp4xAxrd-zjh5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
آندره آ استراماچونی سرمربی سابق اینتر میلان و استقلال درگفتگوبا DAZN ایتالیا از محمد محبی حمایت کرد و اعلام کرد شادی بعد گل او رو پیش‌تر از بسیاری از بازیکنان حرفه‌ای فوتبال دیده‌ و معنی خاصی نداشته و فقط یک شادی بعد گل ساده بود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/23758" target="_blank">📅 14:44 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23757">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SkQNDsEmXJvH8SMbrIrb6b-3z5SoMPO7HDm3jvTlAK3j4ukie7qSAQAs2tKjcMv2udIYCvVi-k5x8DUN2oEo8YgzUWT-FCaapbHpBkHxDchirtDVQMogZ-yE7DtvGgltpCFvHevQH5MJYDug-qlKkKahuHuJCNQLnAS22PG_UOlx_v-y3lOqCq811b-xpE75UdNKHdWaZpwXbEMa1aofSJIZs0ARKc_sLWFN1w12m3iEJU9nmY9kXKoeHA0e8zP20LOrB5fnWxa-gvK4WIb3k5gJmoBrEYpgLGWnnpsE1dX0zA02xdcKpOmkdOCvymsHzd4yvYak5PJiiVWlDGmxpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#فوری؛ باشگاه چلسی آمادگی خود را با فروش انزو فرناندز به باشگاه‌رئال‌مادرید درپایان جام جهانی اعلام کرده: 120 میلیون یورو بدهید انزو رو ببرید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/23757" target="_blank">📅 14:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23756">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xze51gKGFiwnpu9nZ9wCQyJYYAfm2pj7nAeKdt_hbUaasENIfJCCsOZ3v3LTtXLKNWg1a3QxSkeUKhLBqnZ4RYKkfw-A1wlLvOm0tC0rNGpKfYJlhwbs2OJRTEooMpith0B4yAIjp-DE330pl9gj5uWf7wnzPjTUGtGAgVgSrhmsdICsuL6sXCULNesIjJZfxjfUD5oG_TrB5VY7_4Y65yX5BcrBvcc346BCuaqKkj_2E3no6nufawsMItcmPVCTVFltqJbg87NSAg5xiyoTV38lsSfRZl8lBHQemqAi0t4imkit5nox7yFbrJEV4lttTF73B4JuxRK6zbzPrNd4Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسماعیل کارتال در گفتگو با TRT SPORT: آماده پذیرفتن هدایت فنرباغچه هستم. مذاکراتی با باشگاه داشته‌ام باید صبر کنیم ببینیم چه پیش خواهد آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/23756" target="_blank">📅 14:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23755">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QTdZfsJlks25aeZGlXEvvscfwT2G1w_ubSlVZJBswoP2EVYmYRQmn7DFylpq1xTRZsAozx5zssGDWYi4LrC265v-CNhQ2HF1kV3TpqvFR92iRW6f1Xq-mKm8-F6VGqP6ZaoKWz6vDjDTedRbLYrhNTCNUto0fcuDghS1x7PezjjnqnaNnCHacISmiqPHH2gaVSFZrlUoKV-Odv0c4xNZtxokexoW9hs-5u_Wj3xFCpWn78uYOoG3w1bfXMnzC4LDqHVUOwUOSiNFXz20Oi_gTdi0T4PYYGJXnNPG4NJY6i_2Qx7cV4TlaUGO0qDIrmmc0xpXBLb2mC6s6UcxroQRow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه پرسپولیس برای‌فسخ قرارداد توافقی با اوسمار ویرا برزیلی به توافق‌برسند سریعا با دراگان اسکوچیچ قراردادی دو ساله امضا خواهند کرد.
‼️
مدیریت تیم استقلال در ابتدا مذاکراتی با دراگان اسکوچیچ داشت اما عزم‌ علی‌تاجرنیا برای اوردن این سرمربی کروات صدرصدی…</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/23755" target="_blank">📅 14:09 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23754">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sRVlPvDxQNU-lzF1FNS38f-ktqrBYWp6gylS5-BvWQa8GcfWnR2Si-N9ENsH29cOlA0vmBeygFElLNyU6KblUs__EwTDY4cLqKVNPxXOmR1waDIWrsgnhlEOGXEM3mUJKAVwBbMKzumzhPFh0X0h7da_l_wTXRTz7A9rMd9pdzVRNirExvdab3y754H96AngOAAYXXWW4fa7UUNQEURihIgP-LhV17J7vBty9yj3UVTshlfQeziWRt0wtdECaMd6eMgUhG58bIZ9SqejQfC1MlK9HgQrkmnXr98UBqmh7S3QK7PlK8eKF7K0EesRJ1VhIEBevOnqf0lbUXAjQkN_vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
جالبه بدونید مثلث خط حمله بایرن مونیخ در فصل گذشته؛ هر سه تاشون عنوان بهترین بازیکن زمین هفته اول رقابت‌ها رو از آن خود کردند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/23754" target="_blank">📅 13:55 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23753">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/otJ9ZqcBABkDFzpRsisE_FEMj3xarAG8BHsxr5Ut10GeOL2okzFPklbrkfQeIBup_ZaWq-TgKR-mdBuSeyN9DAtJrxq1TiO5V6GiB-BBrN9tIub0mbnz-vckuzMm72oukgUYZmnt0-yYKU0M23DWk2bPlWDKLoM2pButlZ6jDf3dMhEONq305THvS6DSjEKiUFInSPfEgSC13Hi1dfIbgieZovy6ArGCyPCQhNjxI_79Xv4IGNzA6k9sqbO70B-RK7HT0jQXVgRiz-tg9zc1l0Cmbp7jq6ozSUoacfPVlCAgBmHtPZiEvOrMTvYo7y7aTuVMwR9FbOVr454Eb2mdfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بانک‌شهر برای دوفصل‌حضور در پرسپولیس آفر 2.2میلیون‌یورویی‌به‌‌دراگان‌ اسکوچیچ داده که مورد قبول سرمربی سابق تیم ملی و باشگاه تراکتور قرار گرفته. حالا تنها مانع راضی کردن اوسمار ویرا برای فسخ قراردادش با سرخپوشان پایتخت است.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/23753" target="_blank">📅 13:27 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23752">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RcGDz5cweZWU3KoTwUhfMz5f_dGDk7Is0qm1UY22Xoyu1kL-sjVLKIQJBz91FYTDAiCJuuBZmKco8AwmYlAZb9XdUTCw9JoQqjlBPzkcfmIJ8Q-u4CL0A5FdOaWmXSKDbAa-LUIM-qosQXh2HCBiBLQyw4EKiU3vYT1ExbPFwHWXxy2AQBCoLhOLFnGG9xhnWLdZt5nAACp6r5PEPHXRb60r9__WgE1_Kje07xiNO4ITFk-Fdfr__5wfZb4ZimF5vmulKhUYYiN3X_2h7qk8DN-X42mdv9FFdx6yydYkh4b1U1J4yvM-v8DgFfWkndeOpi78imCOTWmtwxGbqgorcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
وضعیت عارف آیمن در جدیدترین آپدیت سایت ترانسفر مارکت؛ اعتبار قرار داد فعلی آیمن با باشگاه مالزیایی تاخردادماه سال‌آینده هست. بنظرم می‌ارزه این پنجره جذب‌بشه از فصل بعد ازش استفاده بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/23752" target="_blank">📅 13:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23751">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10541c5fb4.mp4?token=d8eJufSX1fmbJg6xiToRzrr9L4aUH13R_xlooxWwemcy-lNSVqeYcpMgseQ_owzEFaroDBfwu8YU23GV7lTmPKd9LLBLHCMpk-wfSuxfviwLQPw9Vj20u_b6puXhWlKPq72LsBmzbWRkHfbdQ66qhBu5CrXhJ19TrTS4pWpXAtWJv4AqlqjO3RLFlppXCFuDhdjct8-YU0RFgNvwvX-nFg6BQhKZXo_yHNxiFQ3jv3Hut1bn-4UsLB2i6UQCVv4yR9zis3BQRe4JhZX1RdNmjVCeJjSibCWgC_QEVLCIPZYCSSifzfOot-c8GmJmf1wvogjMfo5c2ZaxRurej0-LbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10541c5fb4.mp4?token=d8eJufSX1fmbJg6xiToRzrr9L4aUH13R_xlooxWwemcy-lNSVqeYcpMgseQ_owzEFaroDBfwu8YU23GV7lTmPKd9LLBLHCMpk-wfSuxfviwLQPw9Vj20u_b6puXhWlKPq72LsBmzbWRkHfbdQ66qhBu5CrXhJ19TrTS4pWpXAtWJv4AqlqjO3RLFlppXCFuDhdjct8-YU0RFgNvwvX-nFg6BQhKZXo_yHNxiFQ3jv3Hut1bn-4UsLB2i6UQCVv4yR9zis3BQRe4JhZX1RdNmjVCeJjSibCWgC_QEVLCIPZYCSSifzfOot-c8GmJmf1wvogjMfo5c2ZaxRurej0-LbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
جذاب‌ترین‌بخش‌های‌گفتگواخیرامیرحسین قیاسی با مرتضی‌پورعلی‌گنجی‌وپیروزقربانی دو مدافع میانی فعلی و سابق پرسپولیس و استقلال؛ عالیه ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/23751" target="_blank">📅 12:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23749">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TRN1KMZInIp1pK2Hrcm--462aDugIBaO6keV1QkI8oo9Y20p4809uzwE4baxCMC4abNodfgmyXnZ221KhZkHfi4y4V2l7e8K-PNmoE9v2HLSptSjl3ecEFKeUWFRMnwE6PFHWcGd3z73N59v3bidBTaoOIJ3l4ChEDJHLXpJ6qqpSKMw-DhnZhal_hSkJlKSKAIxkblH5GkzZYbtZyZ7s9NACE2CrOC9h2R-9QT1Fhbl3EYYG9qlCOZ5wZL4L5GssvnPKONFNsMLBZHcjgNrOem2Ol1ELMLWDUFdoURy5NKYpwejeqwGiydrsc0X1OYKWnyTVNSpNbN36HkZbyKGBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T4AOKhPQit0OCtTwi37pXtRa13xtkqn_Jb86PrkPbqLTVMWZrZoV2IJe8f2D1-QQHkr0q_wa1SADvBVGge6OWexmr70LMYO1D3uzF8C4Ng9nYmtkExQ4UcF8d_mn5la67CqL-HVwXpCk7HtHDbQ0mt5lDRZSsenKCtUYzxF_UqW0RdNEQ0JBnGHmdNPW98gzPTTDUlhStUVHyZZHIG6FzM-g7UiqAnx6XBQ56W6NZl0WHT1QJI5rzhMPIl_fy1LO6388UIvXZgd8xJKsKOr30R7jqIZeOwyZW9VUjioabJs1cvVmm9KX8LymN10OgS5U87KCrstae_9gcUZbQ-oJQA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
📊
مقایسه عملکرد آنتونیو گوردون
🆚
مارکوس رشفورد درفصل‌گذشته رقابت‌ها؛ باشگاه بارسا بالایی رو جذب کرد اما پایینی رو پس داد به منچستر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/23749" target="_blank">📅 12:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23748">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PWq_FhoOoQSR1VDxUVm8GIbhteTi0RdZw-xX4nE72MZB14tZ5ee5XhrmL8NvSaqtnaKLstZ6JTChc4bfCIYIXO-qWFMxHAtU8DkQZcKGwzDJuwrpueH6ycFc8L_E825EySSBVgitTNFk2b1iOg0PyTda-qIBBmyFKxMlDui28qtyFVOMcf7rOCSmwaobFgpd8JHWTjdf4gEw7kVNYC6ocnYqfKupDEtMyK-ulKN57LJDPvCjq5smI5wwOCEPrKa8oAbtwQkjWRmPNZmgRNIlRtnsyE4zkGoCdtdMV6F5XA2A9fHT-KiW8i96Z6MFak_wrqNLYVRh1UDbgMvi3oSt9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
رومانو: ابراهیم کوناته و دنزل دامفریس با عقد قرار دادی 4 ساله رسما به رئال مادرید پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/23748" target="_blank">📅 12:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23747">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e75ce8522.mp4?token=qrq40lFXmCou6C13CGjW4RT-QjzWsAhpMtsD--fIBZk9I_3k9IM0zfzBb953Gdy5s290KZabYc0x8PQtx3hbUyAULxb_FHXNpvQH9U2drbb3nY68xYZHZYlmmX6IHTJuAXsyNE74qBeYbXQmDA0_04Ro2duyBkdQfFwWw6iAJTeXMk8S1B2N22C3mS-GV42u7A7aDRbKM7XspxNYTWYsbVl8Ynq_1EfXhuMKT0fGRz7PXtB7Fd_Fa5D4UAKug5JgBmBwGGMPkA999W16FFi3rnEdVVR4rIJ-9m-64ARdoAWN_pYU-320Ka-kumnSUGXxF8yBwWlDu3-_qPY4peK92w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e75ce8522.mp4?token=qrq40lFXmCou6C13CGjW4RT-QjzWsAhpMtsD--fIBZk9I_3k9IM0zfzBb953Gdy5s290KZabYc0x8PQtx3hbUyAULxb_FHXNpvQH9U2drbb3nY68xYZHZYlmmX6IHTJuAXsyNE74qBeYbXQmDA0_04Ro2duyBkdQfFwWw6iAJTeXMk8S1B2N22C3mS-GV42u7A7aDRbKM7XspxNYTWYsbVl8Ynq_1EfXhuMKT0fGRz7PXtB7Fd_Fa5D4UAKug5JgBmBwGGMPkA999W16FFi3rnEdVVR4rIJ-9m-64ARdoAWN_pYU-320Ka-kumnSUGXxF8yBwWlDu3-_qPY4peK92w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
رونمایی از تنها سرمربی حال حاضر فوتبال جهان که در چند ساله اخیر تونسته ژاپن رو شکست بده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/23747" target="_blank">📅 12:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23746">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jl-wkzFi7r2zBBMQ769Y2mVdURBjdyMGLX6b33t7l79pUy7s5_58FtVxWDehOgBLG4VT9-pL0x2JQ4J71xcRiFxtKcw169P6PGMnsZT85JCDJeEv9gZCfw5-BBJuqiK3Gja2AQst1Lc39y8IXQUUtO72N8wVz4jP_sCSYN9Aaga-XSPf3wemHEiyCbViatHB8qPiHzyHLFvimi5Og0DYvo_cKUPV9Df3TJ6St4w3-29JmMmicoQokPbGWgJ7sEWTUaQQGAgXtIAPHq423T1KpA_wxVOIqtp_xpB4wPrTza-8qo39EuPKpYrX5w6v2DrpoFLvSedIRiIZ2AZSGl9DAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ مسعود پزشکیان رئیس جمهور بعد از امضای توافق‌نامه با آمریکا: به مردم ایران قول میدهم بزودی وضعیت اقتصادی کشور بهتر شود و قیمت‌طلا،خونه و ماشین روز به روز خواهش یابد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/23746" target="_blank">📅 12:18 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23745">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YS-8AK3Ufh17J65vD31cc8Lx8duE9LWHdWc8NwnkXNZRinNm8YKI1RTeDMLruiobxg6fqBuueGxgX2_e98MbKhubCyuj9q0v0p_MYPZVHikNNHxqbp2iXVNjVsoDdpEzaNANYz3S-0-LVjICU2PyAAL3M1TTBLkWDYA12jMWV_1VBGCe5pAiB0Vqt67yNTAX2qcBFCnhvI1QTUvg3EmS7lA1bXS4jd7fX1haeUFmZflvLHLFh-yBNCqcDE54tUFHbFH2kt7O4ylGTEyjYzH4uRIUVAtTDoHl5s2OWTdPqigVNostynXNFH9JDogIZTxZiyw3LSD0ZvJZ5c02XThhNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌رده‌بندی12گروه رقابت‌های جام جهانی در پایان هفته نخست؛ از امشب هفته دوم شروع میشه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23745" target="_blank">📅 11:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23744">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gY_T5hVw3opUbcR_U66iX8W6ztjof23mhtzxNQ9LQ7swy8RhmwOZEoHxtFfU_iPftF3XKCdQRRvdZONxwjxFPmU1S37B3U0Ao9kA_6ttCjRIoCRcZBLJj9ZW2-FJDBXbcWhLgBOYyZfNboNQ1NGHsD7Bdn9hXEAkQV31xhfwYfelPIMt8zpfrr55lL6Lv4ojiSlZUGQC5mir-gz_pw557ezqvfZZDaPIfYL7PiQ3vNihZ1cN5vMtJ7NNEZQTq6yEmfU2smQ7P_4R_wSWkqFdZYjvgIxOe5J7QBLu1wjhV7JAAjIRXIGfwdGsMQ5z_BVAdoeajB79QYiOaumivGAqhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
باشگاه استقلال با نیما اندرز مدافع راست 20 ساله لگانس واردمذاکره‌شده تا درصورت توافق نهایی قراردادی پنج ساله با این بازیکن آینده دار امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/23744" target="_blank">📅 11:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23743">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">▶️
قسمت‌‌‌هفتم‌ویژه‌برنامه‌‌فان‌‌جدید ابوطالب حسینی برای رقابت‌های جام جهانی 2026؛ عالیه حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/23743" target="_blank">📅 11:12 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23742">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9f495fa66.mp4?token=lJ8SbcpTz7-YfndUaC8KGohdRCk6My8l3GLMWXgk9OTO-JhBwoZwncY74CFGjlmhYlP-4TCzsZt9mLuK_NewYWdxNScdGCd0K_QiJSWowzQdjH155LBrCayc4HvHqEpvw6KLMtYxlCZu3TCJXkr1QgZ68T6DEOSXSHEvZOGTLLoEDrT8g9e9pOekOPRVp1V3OS5crlnJzaZfBBfKG4uhgRthharO3xlGM6Hab1iZF5QZ_ykyUqwRis3CnlqX1QHHlk7BI0ypnR2gAbSiEH6PkDwiKbAADZhCTl4pSuX_diMLAazbwUJ4A6NzugAmmyEOvbzVAZWLmQhSw4TwU0Ka_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9f495fa66.mp4?token=lJ8SbcpTz7-YfndUaC8KGohdRCk6My8l3GLMWXgk9OTO-JhBwoZwncY74CFGjlmhYlP-4TCzsZt9mLuK_NewYWdxNScdGCd0K_QiJSWowzQdjH155LBrCayc4HvHqEpvw6KLMtYxlCZu3TCJXkr1QgZ68T6DEOSXSHEvZOGTLLoEDrT8g9e9pOekOPRVp1V3OS5crlnJzaZfBBfKG4uhgRthharO3xlGM6Hab1iZF5QZ_ykyUqwRis3CnlqX1QHHlk7BI0ypnR2gAbSiEH6PkDwiKbAADZhCTl4pSuX_diMLAazbwUJ4A6NzugAmmyEOvbzVAZWLmQhSw4TwU0Ka_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
واکنش‌لیونل‌اسکالونی سرمربی تیم‌ملی آرژانتین به‌سوپرگل لیونل مسی در بازی مقابل الجزایری‌ها!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/23742" target="_blank">📅 10:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23741">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dmx3SirPFcJ5kiU3zmMlIWrlB8PkAHOkl4GC5febVrRl1gfUU1cDyJFoprowpZlRo32NmRlQ4qEpk0Cu7n7UbgIu7AqAWhY4IU9XwmbYD3WOYO5g1DGbnR28sE5I2uPUgqckAC7jlKZmvbCrQG1jE7nJ82rVPFq3eYBSa0ohVJhcZnyBwd4kHgDH3AFqQz4nbV0unNggQ_FvMNPhW8I-GHgcFH7HvxM_nSR2DjREr9yk7QsB-xdzsw73MuEMi75wufUTLQfSFq3NHOJ-Nmzv7whcluwUBrw3KSr_la4yWjBGDKw8OgY_k7lskYaRkmn7smEVRJzGEQfijG6O1GwJUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌اخباردریافتی رسانه‌پرشیانا؛ فرهاد مجیدی سرمربی سابق استقلال پیشنهادی دو ساله از الغرافه قطر دریافت کرده و در حال برسی این آفره. احتمال اینکه گابریل پین به کادرش اضافه شود نیز زیاده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/23741" target="_blank">📅 10:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23740">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TzM6AYjx4rx4nwWI54BzAGcZ1Unt3TC6uC4GeVjIreVEFE4V7T1_tE9omLv9Bu-WxaNMgPmb-keJMXq5wTxT8YLX0D7U1fbF8Djd_l9tcjpI_Gan1soCtSuaRo-qchhEJl4fTq3cG5QQWFFcIpgcyyLDjJpnZUXJpKbVmpvT4grgOIGpxMfoMT90qeBDFCY4pmjRfNyacOqQgOJbwU0C8FZXoJR7QFx2FzKUgrbhzKOnqkFYO9bGc3pPb5CoNFWxSIwRyZ_8UCUxqGpa_lGsW0RNHi8KCVYcHq24puvFckkLU7guWGu3m2PrZsTrOJbH1ZGl4xRElBm5uw-3Kwr1ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
لئو مسی در پنج بازی آخر خود در جام جهانی
🇦🇺
استرالیا؛ گل + جایزه بهترین بازیکن بازی.
🇱🇺
هلند؛ گل و پاس گل+جایزه بهترین بازیکن بازی.
🇭🇷
کرواسی؛ گل و پاس گل + جایزه بهترین بازیکن.
🇫🇷
فرانسه؛دوگل+قهرمانی+جایزه‌بهترین بازیکن‌جام
🇩🇿
الجزایر؛ هتتریک + جایزه بهترین…</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/23740" target="_blank">📅 10:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23739">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FNhAtnYetvSmYHv9qU_pEvca5RuaC8BEkexyKkfbgUWVjIC-8F2eUeM0WbUTlcU-cPbD7Vw6mU65w5puIuyt1kele2K_hh3r5q4yyPIktPKKPSiKvWgGn8XjBGhtvgbCD6ndsdMUY0CHdpbIiv57Ea347pDvRMzbTv6pXmvMHZJMktuf3mpGPnjfyaEwbeH6EnhsPCnJ-6cJjBoR7xoqvN69CJcomQZZ7wrghPkGPwEitFZaSFde-zYwP-CIUTBQfHO_e_6C6wDtTiwY92r5ZuDA8DCy6IeHigiMzfikwItid7WrjMG-yOyODuqCSnezhicf_1x0JWVeRdINbrmaoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
دیدار فوووق جذااااب
سوئیس
و
بوسنی
رو با آپشن های تخصصی در
MelBe
t پیشبینی کنید!
💵
امکان شارژ
کارت بکارت
و
هات ووچر
🎁
قرعه کشی و آفر های جذاب با جوایز ویژه
📱
کاملترین برنامه موبایل
🤝
اسپانسر رسمی لالیگا
🇮🇷
پشتیبانی از زبان فارسی
✍️
حرفه‌ای، مطمئن و درکلاس جهانی پیشبینی کنید!
برای ورود بسایت فیلترشکن خود را خاموش کنید!
‌
🌐
Link
🔜
MelBet1.net
🌐
‌
Link
🔜
MelBet1.net</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/23739" target="_blank">📅 10:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23738">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TxeuqcNIK73x_UBH1f69jPCOdhyfBYCOFKJJgjXZ2e5jN7hCH7Q_Y5UedSAWiSV0ajn471RGoECbrBlxB1DpB9FwM9LEstJH9QHPHbW8EvDKFe0IM21MSxLLYuj4pCWDTkG5hK-tQzMtXaOrbZpNBsvZ1Roev4ufNAdr2y9GTkuD6y0ANLKui42mP220yL1FEHb94IgYQahb5NT_VC5JRhKgF4RFYNu-zI5qYm4J3zzm91_jEHYamj45YYzWczH9JYwRvpzKviXPGZhGrLXbPrt3aWR_NHThtgp8TAQnEVxwuxnVhqi8vX9gU1NQUvRAz_Idt3qFpdV5t5mT7ZN-IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛مدیران‌بانک‌شهربرای‌عقدقرارداد دو ساله باایجنت‌اسکوچیچ‌به‌توافق‌اولیه‌رسیده‌اند و درصورتی که هرچه زودتر با اوسمار ویرا فسخ کنند اسکوچیچ برای انجام مذاکرات نهایی به ایران خواهد امد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/23738" target="_blank">📅 09:59 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23737">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75cc17874c.mp4?token=MywEGlrJ6PN_Q3DaQ5o_1Q6ULhhcfKqjcxPJVNAKgrnc-ddpYu5hyZR1wvj7MN_viz1YVYaiOVgqpLDAWa5AXcqUoh1NOT9HXPm7nnXqPXdMne8fmcz7Vggy52D1fSP-LXZWx1KfYel8ele9EskrX410UmVQW4KlPFMlRM47p4fDOCkoS6YiNxtgCfSURE0udo8EqQBQ-nEr40cL6osQwyUbgzizTTwRvSV6JCJFLWZVp-WH35pncXzEgPUXVdFJFZmMTUy7je0XKSBsJ9TtcwN-j7zgzQFqB2jzum9s3rFASWjAe5VaH0XA6i_Lzb97iCPdeBlayVQrlbgDs8TN3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75cc17874c.mp4?token=MywEGlrJ6PN_Q3DaQ5o_1Q6ULhhcfKqjcxPJVNAKgrnc-ddpYu5hyZR1wvj7MN_viz1YVYaiOVgqpLDAWa5AXcqUoh1NOT9HXPm7nnXqPXdMne8fmcz7Vggy52D1fSP-LXZWx1KfYel8ele9EskrX410UmVQW4KlPFMlRM47p4fDOCkoS6YiNxtgCfSURE0udo8EqQBQ-nEr40cL6osQwyUbgzizTTwRvSV6JCJFLWZVp-WH35pncXzEgPUXVdFJFZmMTUy7je0XKSBsJ9TtcwN-j7zgzQFqB2jzum9s3rFASWjAe5VaH0XA6i_Lzb97iCPdeBlayVQrlbgDs8TN3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های‌داغ‌وسنگین پیروز قربانی سرمربی فجر سپاسی خطاب به حسین میثاقی مجری صداسیما.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/23737" target="_blank">📅 09:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23736">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6e6215526.mp4?token=XBW3C6voa07vRvc4O0rSPco41NKSLpV15KX4_twWCveDJnTOpHpOxqFIlzXEQ3nGkeN2bQVtzjyWJNl5Ful24k6gVJj-VeOzGuL-jltCkRQhDCrFmzehx3wSgSmv8x8pb3cr74HkYiEAnKBqd-7g6mBQwBKaTa4W5ClFXzoiOMhhnKITI19W7G9xyv0w8WNYXwtMjYF5riJULHNChHljUhlgKkR7ZvPgV6KxmjoEnVJgXIpFAAIfh71L8PFrm21JsTV6y9nTWPS2X0rSWPWTrON5lyVk3CMNGQNRd6_rXlyrIU8iknnQuStBBEhUV6biWGCy-R88rF3uckZ_Wi-rcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6e6215526.mp4?token=XBW3C6voa07vRvc4O0rSPco41NKSLpV15KX4_twWCveDJnTOpHpOxqFIlzXEQ3nGkeN2bQVtzjyWJNl5Ful24k6gVJj-VeOzGuL-jltCkRQhDCrFmzehx3wSgSmv8x8pb3cr74HkYiEAnKBqd-7g6mBQwBKaTa4W5ClFXzoiOMhhnKITI19W7G9xyv0w8WNYXwtMjYF5riJULHNChHljUhlgKkR7ZvPgV6KxmjoEnVJgXIpFAAIfh71L8PFrm21JsTV6y9nTWPS2X0rSWPWTrON5lyVk3CMNGQNRd6_rXlyrIU8iknnQuStBBEhUV6biWGCy-R88rF3uckZ_Wi-rcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دکتر انوشه باتریلی‌از روی ابوطالب رد شد؛
تو عمرش اینقدرسنگین‌دیس‌نشده‌بود. عالی بود ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/23736" target="_blank">📅 09:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23735">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7467784054.mp4?token=YOcg7qP7yyMH2hq8wA-2WPRznFscWT8A1TcY056RyMn2B0e8BM3c3uaRjL9OwiAsGYwqY6ZlCceQgRUU6PYrLpRTTfk7pKote1f9oLloNCZTTvnZj8MiIcoXlYR6AMc3RyrROeHwL7s8IUn4dgOk9ENSHEJUFCdRODf8y6KyPvLVrZb233G3nw6uY-w3ovq0xyDkZawPwt2l2Vudml_NT9mOSVGE2qHgKcLMJMXc0F5eDPA4ztP2XL-ZbizQY2G6eejG_D1N-VSx5jmOG9WFO0hkcKlF36C_SecPER1PlHHy355uoCCOIzPjWWFZrPiTsXNTbVS7scbC9GuOSFLSpVdWNQGQ9BGpCvXXXPsYFBcMT151s9sMqIefzer_siMkaYS6OfAFDnK_kXfzEQo6PVwEM_fth6MEyx_BMbbjjLKJHstSQ5jRqVmCten3NzTJQZmXH-jFSCSlBKlg2TTU6MNGAuOtC3t06Noqu8Zmphyejvd1reFFeeqOKQKEH3Fbx39cYY80ghG2Nv2_nh3u11CQM-Zh44DWfz4i89Ajq4rai1ZL6wH-gZ9ZZrCZHICKkTzSnQeeAyuOpxqh6h4HpTXi4OZQABMeqWoD6D1TtUoaBkbbvTHD1zZItgjRBpFOB3CfaDQykzTWu-WsknbYvMUfzvDuN-xlleSC46BbKRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7467784054.mp4?token=YOcg7qP7yyMH2hq8wA-2WPRznFscWT8A1TcY056RyMn2B0e8BM3c3uaRjL9OwiAsGYwqY6ZlCceQgRUU6PYrLpRTTfk7pKote1f9oLloNCZTTvnZj8MiIcoXlYR6AMc3RyrROeHwL7s8IUn4dgOk9ENSHEJUFCdRODf8y6KyPvLVrZb233G3nw6uY-w3ovq0xyDkZawPwt2l2Vudml_NT9mOSVGE2qHgKcLMJMXc0F5eDPA4ztP2XL-ZbizQY2G6eejG_D1N-VSx5jmOG9WFO0hkcKlF36C_SecPER1PlHHy355uoCCOIzPjWWFZrPiTsXNTbVS7scbC9GuOSFLSpVdWNQGQ9BGpCvXXXPsYFBcMT151s9sMqIefzer_siMkaYS6OfAFDnK_kXfzEQo6PVwEM_fth6MEyx_BMbbjjLKJHstSQ5jRqVmCten3NzTJQZmXH-jFSCSlBKlg2TTU6MNGAuOtC3t06Noqu8Zmphyejvd1reFFeeqOKQKEH3Fbx39cYY80ghG2Nv2_nh3u11CQM-Zh44DWfz4i89Ajq4rai1ZL6wH-gZ9ZZrCZHICKkTzSnQeeAyuOpxqh6h4HpTXi4OZQABMeqWoD6D1TtUoaBkbbvTHD1zZItgjRBpFOB3CfaDQykzTWu-WsknbYvMUfzvDuN-xlleSC46BbKRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
10 گل‌برتر هفته‌اول‌رقابت‌های‌جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/23735" target="_blank">📅 09:17 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23734">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">📊
نتیجه دو دیدار بامداد امروز جام چهانی؛ پیروزی لحظه آخری شاگردان کارلوس کی روش با طعم کلین شیت و شکست شاگردان کاناوارو مقابل یاران خامس رودیگر و رفقا در کلمبیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/23734" target="_blank">📅 09:12 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23733">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UVwj4tJ7unhVTa8ZkgxLtyM2wh74xDmWH4Vu8T60BILfUiZeg5E9-ZpljK5CHmKMop_DhA-pgv1mlw6VjhXYXUiDI8kC_rnldfLI9EQaDT0yCYo8HriCKjVzc811enV0AsNesHdqu-Mp8UvmLPT6lPdmgScURn_QRwTme-1jzOmc8mgCJIDDylMt9TEWyUziwhPMBEyhw0DgZztQIIQj_1-lDxcT1KzVLLTu3abB2ubfRR_CtlkUf8VBJWnTF6h-jC_g3hm_rDuQlNpMWhx71_2L57STV7E772DLCtN6jMUufgciK_R05SytsyemATNAo7sAbqnQipUC7mi9F893Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه دو دیدار بامداد امروز جام چهانی؛ پیروزی لحظه آخری شاگردان کارلوس کی روش با طعم کلین شیت و شکست شاگردان کاناوارو مقابل یاران خامس رودیگر و رفقا در کلمبیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/23733" target="_blank">📅 08:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23732">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q36DBHhwHiqNDoWZtL3-QTtPgH4qaBZwBIxsU1ImzVzxY4iXUSbAFUaWXB1ZRuUON7_MwZx1q3NkKRRIKM4JjDUAb90daJOaTrLIioNeCYkVDkXQamI9kqkDeAxcFxqAK7EhCWliTJ7-nKf-e10l67FdaZH-3Czp8BNgwGlKEVAzwcFhBFLl3Y0l9vgDkYvk_DtWYa-APMI3sfNqj6lCAm0T8OscxMoA5hyT-HRFkfVs4Furbn_iIIMUSMJCNk3NDeLGuC4bsgTDXmP9oXQdlfw-yVeUca2WrSWzX6roolUsPNLe9TOxqt_cPcfu5yGpXg7sBmhLsWU3pjfcw-kWxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه دو دیدار بامداد امروز جام چهانی؛ پیروزی لحظه آخری شاگردان کارلوس کی روش با طعم کلین شیت و شکست شاگردان کاناوارو مقابل یاران خامس رودیگر و رفقا در کلمبیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/23732" target="_blank">📅 08:36 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23730">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WdmxWqNCBKC7kIFwHwUOq_taT_8PWLKHzJ3t01_o7dRmcCzzmiz6-rwYXYmoXMtbsinudx05bI8Xzh4YcZs_jz1ZgCsS9yE_ZdjVBHm69KcJjPd4ozANQRfDu67nKKuaEKYw3492fS2s9jp46zO9oWgjxpbF0fSM2l-_Qd4JQ_MHXC9WWXBnJKQ7mPGPds_beeKMSLPxXRb9VKBvW_ik7iknrXXjG3Sqm3b2ogIJhQ0GDcEng9KWdVXLdYd8XV5Z-jlu92XkGjs1plsk1ebCA5e73T7EBHjoKVU8nC1vztB8uSR8Rtjv7UptnlgwP3Fph5rkfWMd0QxVtTzlWouffg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ITSCxjkVMHK17rS6nNsEXvfvGRs27hUQ8de8zKC1dlZ0t8k9gfW_a7pZ9h3UiN9IDXlfOkOcBTuo3p9T7WQqaacPocUrXjStwywhDVQXIXvT6Cwj5-sVJtg6S0uYt5HZKgbqAF9OzjGf1_tZhWhPdYWEOQ841Da7DIPA1ujPNRk9BnnAEh1TRrKD2_WylUQXZ_3KWJTx3ErFEm9V3e_-EOSWORLMyi5SAzzt9IEKl4VSO8A9auPgbPSwM5-D6KyycInZJhiTgm_EPW4AouVwYvIJ8VUE1sFJhLlAZPvMTSwx-M0wtszPQ-p8z6jXmNrMSFoZHC2tu7ZcIrGohMnqmg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛ ازمصاف شاگردان کارلوس کی‌روش با پاناما تاجدال یاران خامس برابر ازبکستان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/23730" target="_blank">📅 08:28 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23727">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nUHOpyS7sgJ6enC1kfFFd_FBkyNkpsFwuwW34IhwoSWbCoM04cH-DVssczMPs303hbtsPgisTyF6ZGWF5L-EtcJr-9WYJgHu_Zts0V4PDgOh_yUldzYsiE__fLTjhoj5hU0cB2Dcd4C3u4HI95Ugscxkmv5AtiYttpzNn_y2hXDPkm4ZdlILVV5x-KpVRUXqD1JNPgZa6wN-zaw7ciaL8wvdKt-jrh53YJS6wSNMEgYoYyB2PADKIuiOnc7jzN6TP1e0K0ZmhTv6YM3GlV4U9C0tia_Q41rVlOL8gJQONHVll6n5Pkn022KOMygiJrfAZraHuieA7W5JC4ICXa7bVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
#تکمیلی؛ نشریه مارکا: باشگاه رئال مادرید بزودی برای جذب انرو فرناندز به باشگاه چلسی آفر میفرسته. مورینیو برای پست هافبک اولویت اصلی‌ اش رو گذاشته برای ستاره آرژانتینی چلسی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/23727" target="_blank">📅 02:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23726">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VgaUGdOv7EqjyyaYIDMYtnWm86JCGwFfAeEuPf4Xf2K0fiPA8gnjadmiW8yKChp2zVq6cOuJCYnOtT9zK0SqDM5vb-q9q28_StOtoA_yil95vCoadMFRtranE5iO80VzadjyJP25DL5uZaHKgixZm3Fo_8jfy_lCGTm_ZeWy2Vy2T7A4sPFKX7-mk8M7HaudEwABZEtIJn2w9MpMGn-jhkqUzipcU0nRMNcrIrNhnS2jhjNJg1sYaauLdQeFwWSSi-HZ3aWfxk73nV081k3nifa5dQ6ysm9w2IRrGvW_AhzDc__IWJXhjdLUXIVg8Pm4fNKLfXEVJt2sNxJaCJXEzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#تکمیلی؛ محمد دانشگر به مدیریت باشگاه استقلال قول داده بزودی 18 میلیارد رو به حساب باشگاه واریزکنه و کار به‌شکایت و دادگاه نمیکشه.  قضیه از این‌قراره‌ویلایی‌که دانشگر خواسته بخره یه مبلغی روکم داشته که‌تکمیل‌بشه به مدیریت استقلال میگه کمکم کنید این رو بخرم…</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/23726" target="_blank">📅 02:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23724">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ej5RG5qPvMzEeNS9jL7fSINn3PO9mL9CtCpzjgj4LUexW5UnTcDOm7JPfW42fs1Qq4tWVfQnAHaoVWKUxBGFNESmMfnY72fun4kCLRQDhIHCVZPzBMX_JDm3gqMOzeawj_ioVreqxEKy4Yy6NNocljr9ijKC-7t4_iBEJCTYfnzvVnOO3QEPmExCbf3142yGvVK8OWIy-u1JnyHLt2ZC99sSQv96gG5x_5V9pmVkn_WOm_OZGhiFlNPlApMuAUqw61rhmyIRrXLdP3JGXTkDBj2xS55ewfuyGb465MHGg_qELAyLvYGVt0FHPKZDLRBCd9suPHZTyifDH6TO9LqiPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
ازمصاف شاگردان کارلوس کی‌روش با پاناما تاجدال یاران خامس برابر ازبکستان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23724" target="_blank">📅 02:09 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23723">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q9bIlkSDeHM8YJ6ZE_oUBBVwN3vtXecSG1WjYI4nzQ_NZoIAdwqPusYG5a8zVNltfolu_E5iI5p_bguIynziJ6Pg_fmjKSNaabhVWrlzwW_2CfiyNcyyGUmUiJFBkDf7YscPMxET_RQpMO8wtohqvBN9Sy5mXZtpKPGm92qLBJpZOi5L8vynb-afZZHSug6ddM9NY09gAfraN4c8_eiDaRR6pMhR223cSWkw9cGGgEPbZpVStm2K5DmmPZcJSbFZOjeOWyXc_LyPej43hPB6six5mjx2Fc5yk-iQcXS7mDcw0ANZlLNGUS2sUHXHfwWUN1x9Od4uZPFw43hlPiEmSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌دیدارهای‌‌‌دیروز؛
از هتریک فوق‌العاده مسی درگام اول تانمایش‌درخشان‌سه‌شیرها مقابل کرواسی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/23723" target="_blank">📅 02:08 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23722">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b735dd21e2.mp4?token=jVYahy7wg3KmYvhCdiwPTx5Uf8ntNZjpElGyR5llH3S8RxLuMm3sOKJ1LtmsjG47loe-GbucVupCpF_8yks4v4UUAq5sbbrAPJZ_XWvZ-ckw9kxy4tU6k2wTi2fI1K0t1YVr5QgxldLHolGFKGhjI-OSZwu3qD8vC_E10nAaOr7rmws8U8cR31H05CuQigARjhkZ6Fun7nqpdnPQKt9f6BgrLMBxZm9aroQh8btF4xiurrdrA9TJVD1-lJKTs95hXDo_7hru1EvVQ5e35NVS3RyRR_9XjkJSaKpSbwYhg2rEh08s7k5i08bNHKJJeBNdORot90idEOw29ScQXlAlKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b735dd21e2.mp4?token=jVYahy7wg3KmYvhCdiwPTx5Uf8ntNZjpElGyR5llH3S8RxLuMm3sOKJ1LtmsjG47loe-GbucVupCpF_8yks4v4UUAq5sbbrAPJZ_XWvZ-ckw9kxy4tU6k2wTi2fI1K0t1YVr5QgxldLHolGFKGhjI-OSZwu3qD8vC_E10nAaOr7rmws8U8cR31H05CuQigARjhkZ6Fun7nqpdnPQKt9f6BgrLMBxZm9aroQh8btF4xiurrdrA9TJVD1-lJKTs95hXDo_7hru1EvVQ5e35NVS3RyRR_9XjkJSaKpSbwYhg2rEh08s7k5i08bNHKJJeBNdORot90idEOw29ScQXlAlKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فیروزکریمی‌پیشکسوت‌فوتبال:
بیرانوند درتاریخ بی‌نظیر است ولی لطف کند کمی تنگ تر از این باشد. این چیزی که ما دیدیم خیلی هم تنگ نبود واقعا.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/23722" target="_blank">📅 01:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23721">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e924ecdff.mp4?token=uPvWzbHo_UXO_MCSaC3o-FggfRwC9UahUuJOAh-YQgx4LyESCTCHGZjuXAy3hXEVYkcBhcbDCIqxlZTUiOvDtr9_KdBigDdbtueLqdE20L0Un5kzgfz4ZHnITR1MZUm9O53LvlW5wrS7KYBuSVz4eY7JfpLEhJ6xmjdC6KOeFFzUGe-VGBTXVUAB46VK_EEOTE59LkuBS69QLhksrLXkz3nKLFS5R8ImmrcM8uSf1urGBYeXYTXWSA8Rcij4rWSfv1d90S6drIje2R1vDOUGxMkIAE_fAIYRqhDlGkR-e_eRa1ckyafBmGHlLIMy9FdtCugxrQumKUkKq7oHsJIcCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e924ecdff.mp4?token=uPvWzbHo_UXO_MCSaC3o-FggfRwC9UahUuJOAh-YQgx4LyESCTCHGZjuXAy3hXEVYkcBhcbDCIqxlZTUiOvDtr9_KdBigDdbtueLqdE20L0Un5kzgfz4ZHnITR1MZUm9O53LvlW5wrS7KYBuSVz4eY7JfpLEhJ6xmjdC6KOeFFzUGe-VGBTXVUAB46VK_EEOTE59LkuBS69QLhksrLXkz3nKLFS5R8ImmrcM8uSf1urGBYeXYTXWSA8Rcij4rWSfv1d90S6drIje2R1vDOUGxMkIAE_fAIYRqhDlGkR-e_eRa1ckyafBmGHlLIMy9FdtCugxrQumKUkKq7oHsJIcCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابوطالب‌حسینی‌درگفتگو بادکتر انوشه در برنامه امشب: باورتون نمیشه ولی من دوست دختر ندارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/23721" target="_blank">📅 01:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23719">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/210b9e3441.mp4?token=v8J2MTnrCWMVODNCf00dzu0BV-fHO2o6qBN0L2FSZPJnAxUfWBnWoJPxdRMriBUW6Qbykln0XonvpMHCv4TmtWDnkQcwArifTe-tQ0NJ48_13ao5Zbyc8hXBPdW6hcq68tEZkN98q4-3kd-DVoEKfAzeD2NPbJ2h4MPFp3w4-RqFusB97ONisIf55GBruxjM1FDd-ZrMXG8YedJknkF5aLVmff5n6JglavM4muHuRsD26unggPD6qtjwYWDbEBHzrL1LIVt7WCsKjFhQh6_ydqdQ3bTosIQ9EwGJ2O3lPL2-2FPLyYg-dnQWX7i6WM4hpZDT8shW2COGuXftXTKcGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/210b9e3441.mp4?token=v8J2MTnrCWMVODNCf00dzu0BV-fHO2o6qBN0L2FSZPJnAxUfWBnWoJPxdRMriBUW6Qbykln0XonvpMHCv4TmtWDnkQcwArifTe-tQ0NJ48_13ao5Zbyc8hXBPdW6hcq68tEZkN98q4-3kd-DVoEKfAzeD2NPbJ2h4MPFp3w4-RqFusB97ONisIf55GBruxjM1FDd-ZrMXG8YedJknkF5aLVmff5n6JglavM4muHuRsD26unggPD6qtjwYWDbEBHzrL1LIVt7WCsKjFhQh6_ydqdQ3bTosIQ9EwGJ2O3lPL2-2FPLyYg-dnQWX7i6WM4hpZDT8shW2COGuXftXTKcGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
علی فتح‌الله‌زاده یا تام کروز در نقش ایتن هانت؟ وقتی علی فتح الله زاده در زمان سربازی فرمان آتش به جنگنده میگ 21 صادر کرد؛ فقط نگاه های پیمان!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/23719" target="_blank">📅 01:48 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23718">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">⚽️
هفته‌اول جام جهانی 2026؛ پیروزی ارزشمند و شیرین‌شاگردان توخل مقابل کروات‌ها درگام نخست.
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
4️⃣
-
2️⃣
کرواسی
🇭🇷
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/23718" target="_blank">📅 01:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23717">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qpy-Q7DHLW_SbwCMWDVBKimZMljeRMror3pD5cC4HE7HpmIn4qqGr8cAqE780og3y6zUYEhfhR2_sdIofb91ThqQm22wcssHsauqJVe3BgiI9ykgaHS0L9SwrQshWirIYbV0S2FHxYKtPluYuDb7nnGasHFMzRnrXxUCArtzoYCJombtQ3ZPmoGLyh9LAPHnifvriOm08U_A4O4QWU9-oku0UG_JRwUe9r0aLNUIqJIYsreboeXGEr_zPbvmSBHPk7X7y8D5XJyKQ_tswPehjUPu17HDLm73RVpggsLOK5p1Yv2H208dVBpB9raRjgr_2UKfdsdVNevRM_I467NmLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
هواداران‌تیم‌انگلیس پیش از شروع بازی امشب؛ برای ترامپ شعر ساختن، فیفا هم اعلام کرده هرکی شعرو بخونه از استادیوم میندازیمش بیرون.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/23717" target="_blank">📅 01:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23716">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d2128a8f9.mp4?token=AJ1F63FRZGTZrt0EQiHS79Rw6OehNRpFGbQUR2SJVtCibUtrVLh4MEGUE-muXlV7b0Ka7QHkn061JoT7ksuMLDroCe7JaQIhjnE-NCiQmgOEUVuPfnaAXh53b3nls7YVGC6brGVujdT0IwCN3mBX1bCoFyQMg5tBtD_hDVopBQWgKuHPKa76NOZPs7By4_AERsnqcMKSJhNQ5lxfCh7alXdZkOy9aPJ-kGSUXRf2fFDWAGRVCJLJbBE-e-fVYmwLO7rIdUOP0uVrtIORmZWrG8gKFAXlmIrllbMpwshXJdsJfPtBD38eRktQzvZ5m41cQdHL-Jde7scWcqa5Om8-0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d2128a8f9.mp4?token=AJ1F63FRZGTZrt0EQiHS79Rw6OehNRpFGbQUR2SJVtCibUtrVLh4MEGUE-muXlV7b0Ka7QHkn061JoT7ksuMLDroCe7JaQIhjnE-NCiQmgOEUVuPfnaAXh53b3nls7YVGC6brGVujdT0IwCN3mBX1bCoFyQMg5tBtD_hDVopBQWgKuHPKa76NOZPs7By4_AERsnqcMKSJhNQ5lxfCh7alXdZkOy9aPJ-kGSUXRf2fFDWAGRVCJLJbBE-e-fVYmwLO7rIdUOP0uVrtIORmZWrG8gKFAXlmIrllbMpwshXJdsJfPtBD38eRktQzvZ5m41cQdHL-Jde7scWcqa5Om8-0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چه‌غمی‌داشت؛ یه‌روزی به‌خودت میایی می‌بینی دیگه پلی استیشن رو گذاشتی کنار و بازی نمی‌کنی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/23716" target="_blank">📅 00:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23715">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CdJsyyuNVV3ehJfx5-SGnIL-cA6nku5TYF-KGVmE6xJ-eSHmMOArhYDSNnNbUcBXtbAIxM5Fc6sXvDGDMn0b_lvF-pYCRxE7rRUqduvAnUNWtLgGQSp2s7B-w0P33M_38jtDME04GZSAnF9ffsMSxcZMef7HRLXfbfs_3YAPL62L34rh459K1rzHjypC6cbOm0lEbmeZrlJtPYopNaMKMS6p4g8Lr7WALbizj-v1-Hk1xj47jpDwpn8lJ_WtT6EhOieY48eFU-sUfcVZb8a2uOlka5JgRLIZ-UZO-OdmnK85ZnrrrIesVmUr2JWGOgOznTFYggr9Jn2W4jE1hhlTng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
هفته‌اول‌جام‌جهانی؛ شماتیک‌ترکیب دو تیم انگلیس - کرواسی برای دیدار فوق‌ العاده جذاب امشب؛ ساعت 23:30 ازشبکه پرشیانا اسپورت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/23715" target="_blank">📅 23:27 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23714">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vbRuoY105uRHtRFj7pY9e7MSYy7ai51U43eAU6PkNt3PalpmF7Gyl1sqa5rQW5gllAb2RxNNy3ODvKEAsIbNKhbRp-EflNd_jYCvOmwT2j79NGGZnyQWGLFygOZ1bk-1RfMqri6_ZJJUlazw4h2fevBWdvmCfIIIYn-lkDLwEyyAvsnPy8bFgKZWj04qUYBaqLArW-LLNMbnKJtXTtIn1o1E4czlihzntaHQc8jXW8GIGn5eks2Mlq9JZeG2haVUeNvD_wtxPE85V6Ua_UJBcVIf1-qN2tO3YS_GAv5Iot4sMibZozujm_HmiVzB6EAo0KtpcMooddn8fhco6soUiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
با‌اعلام‌باشگاه‌سپاهان‌اصفهان
؛ آرش رضاوند و میلاد ذکی پور قراردادشون رو با این باشگاه تمدید کردند اما محمد دانشگر حاضر نشد به باشگاه تخفیف بده و جدا شد. رقم قرارداد دانشگر برای فصل جدید 170 میلیارد تومان ناقابل بود که کم نکرد ازش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/23714" target="_blank">📅 22:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23713">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79c30d0c69.mp4?token=Y2CqPDesfEnVXgWl8zNlw8l_8R6pohHZdY-dygyUqcjpbbr4MSe6kjatXBx00yworatVCkwiv8a5AxbOEx522F6iR2ByM1k_dxHQg-h8zcFbzK7IhVZZS-YAVI_wbz7YcVZn1LatzM15lBOIDqzHk6PXN1nk31Eb20EnB4-N0Rps61OAzSMsg9n8LSMiY375kt-TFVmNpxhQ0DI6PlUDidzwPP4Hx4OZN1HjkTJ1I9v5bBJDbDeHiX4imt-G7ZZWroAXR3v43VwTZCHnqsyTfxK4qV5M_W6L7a0-KwbMYqsTd-8lpzxygL9Q_6Wm54Vi7cmL2Mmwsl7umfzNbv7vJINX-Lk-Oi5zWI2jXEKTpYrX4wht40zFdLUEn6WLn3eggVBT2uN4L4apd3_w-3h7knTzenaZztMEyLVoFMLKuOpdwEut561E4DssN9YyZJ2Lxsjy5j6v1XKnj6QU9FrPWLWE4IyHlaerdbK9vF02-NqEXwpr87s2u7UjwIhN1aRIE_TvGlJmSFhXxulNQmZ5PtZ09MmCJ_eGbpxu9uGLOPQip-BzwBxKvgzWANaXDDU_W46bLvgeBqqnA4qZCXQh0wk6-8t7Pxt6N9yjUP3u1RbftUfheHBy_iJlIC392SXtbQpQAA0NoYUbnRikpwufmv4zNZEChDMOpyBbbxGT87s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79c30d0c69.mp4?token=Y2CqPDesfEnVXgWl8zNlw8l_8R6pohHZdY-dygyUqcjpbbr4MSe6kjatXBx00yworatVCkwiv8a5AxbOEx522F6iR2ByM1k_dxHQg-h8zcFbzK7IhVZZS-YAVI_wbz7YcVZn1LatzM15lBOIDqzHk6PXN1nk31Eb20EnB4-N0Rps61OAzSMsg9n8LSMiY375kt-TFVmNpxhQ0DI6PlUDidzwPP4Hx4OZN1HjkTJ1I9v5bBJDbDeHiX4imt-G7ZZWroAXR3v43VwTZCHnqsyTfxK4qV5M_W6L7a0-KwbMYqsTd-8lpzxygL9Q_6Wm54Vi7cmL2Mmwsl7umfzNbv7vJINX-Lk-Oi5zWI2jXEKTpYrX4wht40zFdLUEn6WLn3eggVBT2uN4L4apd3_w-3h7knTzenaZztMEyLVoFMLKuOpdwEut561E4DssN9YyZJ2Lxsjy5j6v1XKnj6QU9FrPWLWE4IyHlaerdbK9vF02-NqEXwpr87s2u7UjwIhN1aRIE_TvGlJmSFhXxulNQmZ5PtZ09MmCJ_eGbpxu9uGLOPQip-BzwBxKvgzWANaXDDU_W46bLvgeBqqnA4qZCXQh0wk6-8t7Pxt6N9yjUP3u1RbftUfheHBy_iJlIC392SXtbQpQAA0NoYUbnRikpwufmv4zNZEChDMOpyBbbxGT87s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
هفته اول جام جهانی؛ توقف نا امید کننده یاران کریس رونالدو درگام‌نخست مقابل یاران گائل کاکوتا.
🇨🇩
کنگو
1️⃣
-
1️⃣
پرتغال
🇵🇹
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/23713" target="_blank">📅 22:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23712">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HQNoqRLyQhorJ678bmad0QCHUUy2brHUcqBTN4AGSIFGgwkgSXc22dI1GpSQgl1OshNC-NLOego1WBZSBHtoAEmoYcJToz-ToQjf2NxQBQ_E5SEqdipj-IvA5eOuwItRHvM4GuAG6XLAb1JKpuD6TSwgjfnQVpxap9h8ju52mFhhKDHjj9I-SV5SzZ8sDdhyu2HVxaO4_4zI9vjX39sFlzPjlOtPaxkAofKz2j8A1AwrUVhC8SiRYVT4tYjMtImPwsQ7n_cdsodc0CW0nmsspoOFIbPoW0YhkrZ-TwHhUtt7JVB_5-dYUrklXH9P7UmeWi1lBYw_lufIlSDWjNIREQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باگلزنی‌برابر پرتغال، یوان ویسا اولین گل تاریخ کنگو در جام جهانی را بثمر رساند. این نخستین بار از جام جهانی ۲۰۰۶ است‌که‌اولین‌گل تاریخ یک کشور در جام جهانی توسط بازیکنی از لیگ برتر به ثمر می‌رسد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/23712" target="_blank">📅 22:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23710">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OwuUcfl8OBZ7awX3Iob9B71EKLXwTg4M2KUYoZDrhPRU-bcydHJXQtMpHVm5DaetRkLAXFhDUwTSj8dx9QkCnw5bijfLax4pf-6en0NPZrvgtlP1pvUql6xcZL5n68NhpYzuYqNX7m-ANuyfRhwYtCuwvwswh2ICRXrE2JJPazXlN_D1eBWUhPray4U3fakEp3-9jStzKre3wSrHCBWWHEV51kpiZlZ2h2VkZCYZWwcjl7WUmjS9rTx5NzAJg_YrblwXfbBs_hPonIFzW4-IzNGh-Lw5PmmsmiHCgqiWAfdP6ddOjnh_pPPYatHmmr7bb16XvyztJaIzQcgdLoeOVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HaekUEdrhM__lGRsIfqcitcDVGekLI6P03j2xfskFs4oirCwUwKF0U8v5gvb5hXtQrGS1ZIbHbSyA1KmCDUoaXhk6UcSsSbuDmFRWSadQtYkxpD5IA07NH8_J94rpA57jiQDWVdUQ949NJFOseqVCYR5vj-KqVA1uk7u4GlqOzb_R4OT0J22FnXtkOQyQMtaVSBDMu7n30EEK-M4wdaGm7TrBe15SXJ3QGmnonEN2LLGgvqi4IiATDO8e_88r0zSYQRKKDcV_K2DNrG01AHHRmiTr8WWMaVnE82vuqcg5o01DkDYEOlPWzH6ph66qQAau8VjZTmui_0uW8_GxZjzdA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
هفته‌اول‌جام‌جهانی
؛ شماتیک‌ترکیب دو تیم انگلیس - کرواسی برای دیدار فوق‌ العاده جذاب امشب؛ ساعت 23:30 ازشبکه پرشیانا اسپورت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/23710" target="_blank">📅 22:12 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23709">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p_JdNNbsXzD3zIXpXjMWDkV2kxpR_GnZ5T1-8b3buTq5NUc6XL_f8UmHleho251v4KupfDEAeYUWyQbPwESEfJVPli6dnWOgzqr_i7xP8KjvE23d7_NiTDLBBR2NjCY_77S98GKLu3xeN58NJzaNemKIp_K0JB6_t2BcYPWsBUdeMnWsOVBYDl4Ilc2lqhebET5-eXmvuPs6gq2d4mgkWaYoJ7RgSwXTRODopU6h3z-5W9ZTkeFcEyAFNAnkSMDUPKIud3SzWNt56ROlp91Da_sjCb_JpvZsoBe82JwzjdlyLjt97sPPwFlY2jbb_1_KcS4-28W9qtiFoz_aHRtoaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
رگی لوشکیا هافبک‌آلبانیایی‌ساعتی قبل با صدور رضایت‌ نامه توسط باشگاه مبدأ به تراکتور پیوست. ارزش او در مارکت 400 هزار دلاره!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/23709" target="_blank">📅 22:06 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23708">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H7sE2QDbnSfTwe6VZR6d3hybIyolFROfr9Us23yzZeMq1l6RloIVogMdfN83oUm9Pn56PgPytlC9bVr9BzMzvw_wKj0tVYDsEGFNNdU-_9HMYenoeKvMiHQ36pEAhiDRVzitAOZteZFj5dsFbVkrYQx82UVLbv_9e9rHp6Db-qizTR-SdrMQmxAewzMejg-c7nnx_8wnN-Sh4ebPYEtMgd75xB9oZbrN2HgSpOP97QalOjPIZ3K6JRX-8lbNy0nTB0IpBtJp7vJ9LJ4yp3zrgkl55sAYfFfJiWpI7E8u4CKhMnxPYBptTlBwRS_pvtvbuYIt3ij7H3yfi_MoPkDlKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
هفته‌اول‌جام‌جهانی 2026؛ شماتیک ترکیب دو تیم ملی پرتغال
🆚
کنگو؛ ساعت 20:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23708" target="_blank">📅 21:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23707">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k80xVuXZ2QD8e_kxm2gsoRWnlQV8WuCDCkALDQ9FFs7K8O53VGFSQkjtWIF9G3h2xLGTXSnywfFbsdXbw47EfXAfdtijuJV7veuPs0A_1hvOl_U9GxJU-1rPzAV1-j87a55eT-9ISUDnVswhiFgXNj30XXrdzC725mFJhg1AzAuCSdmlyTkv8J3B6IHV5k82eogJEOERR5SdEgPe2cgtaPxTsET6y3gJ5UhrrUt9CbZwMuHm8rhcvtE7x0UP126MElpdZBzCetpzp3NW-YqDwjbiwVzhV9lThSN0FduofMhBMXtUEpdfyqndPtpzrS4T5jicCQ4Fi9LD5Se2q2Pwnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌ آرشیو وار: خطای لیونل مسی روی بازیکن الجزایر یک کارت قرمز واضح داشت اما داور تصمیم گرفت این‌صحنه رونادیده‌بگیرد. شانس با لئو یار بود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23707" target="_blank">📅 21:19 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23706">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dTgm1iyZYonFpzY86GXvqrxpYFc3dz7HNm6SRyrO0vT8_MruSoIUM5Pq_jVGdg20-0A7rsRayXioWJgTp-twXEdvgVH9fD-lzmj3OcurCl6uzSgJvqJAI2Q1GV1oGZc275fkCxTl9QohXVoSh7FqzDfxQD_i0LD5G8EauheKzuNNZfrxowwOUW-Wkz5_amNhYPFkOLVIsAQjrvcgyNPLNC0Dg7lw_qCDtBeLJz4Bs_m36rXGW0W2pB6D3vZ3vA57YKxhVEnGV07gTMUNW12P4x8LxHI8yH4sPvg7D09DBxMMmPGRkVwGQEgyAoiHedbR2-JvDoW1bdf08pO8OoIBZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
باشگاه‌پرسپولیس‌مذاکراتی‌با اسکوچیج انجام داده تا درصورتیکه بنا به‌هر دلیلی با اوسمار ویرا قطع همکاری‌کردندسریعا با اسکوچیچ قرار داد امضا کنند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/23706" target="_blank">📅 21:09 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23705">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/viSZOR02_6tikKz6_i0styjF5ZA5rn0nkYvQH6R6-xGutciXuhpILhLZsqKWMN3evw5wAyo-PT5FqWub5anIgYHWXYxxLO-vYBLQWeeDaTON3cmH5ykvj-DXTVcIw_cMOavAWwK9WuHgzA0ebW599hXrs_5v_6Kz2seiwSMucFOMbSzpZ-uhXYboDxGPR4hVV-uW0ihsweWmyyOt55bXRNjlQP2fuROxpiK6q2ULzUoojr5hoy0VGm_7gIQTu8KXOcbfK6V78BocXZC3Mr3TY_Z9ha-aoUqtnZqOWaZZGV6wkSBYon1cG-NgX2jjRZQg_e75uI6uMzDakankUgFRWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
خبرنگارESPNاز پارتنر ژائو نوس پرسیده رویای چی درسرداری؟ گفته‌کلا دوتا رویا دارم یکی قهرمانی نوس با پرتغال در جام جهانی فعلی و دومی پیوستن نوس به باشگاه رئال مادرید در این تابستونه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/23705" target="_blank">📅 21:06 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23704">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aWLwu1HjGrGJZiXbHjuxfLeck_--w4w41Fawi2XlGbDb4j7X422s1gyetmT_0dbochEm0jbrfjtF4Q9jq82P0itx2_gf9G8yZS5eEeTlflPpaOiychqW4gDA3cCMTT-RoJUvC1ivlsLQVV4-FjhWlgIeKovp7jYbaixD-EAkwLM4mYSWgvp3hC5NR9SUk65iGnz6xn4p3HlIdWDbgac31udx-Xnfx20P9M6Nb8f-uB17UR2Fyb7LHEd8dUyPDlCUya11x5GlfHBN55fwkiYXebMMXMa35sl01men351BCAOjhnaqSgOUNUQboXCoOj58DW38dE5bxGoWY04NF6YiFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
#تکمیلی؛ نشریه مارکا: باشگاه رئال مادرید بزودی برای جذب انرو فرناندز به باشگاه چلسی آفر میفرسته. مورینیو برای پست هافبک اولویت اصلی‌ اش رو گذاشته برای ستاره آرژانتینی چلسی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/23704" target="_blank">📅 20:29 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23703">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GDcSyswJOY55NLuOz8lEbtBU6N-IYfqUy14sX09MWry4XmYr_9bz_fyscoo00Pxpzm4FKw1oeJXG0dQ8agcNrAbLfQxorEGBkh1oYo7bQeGN3Mtsld3HYMVBZyNj5iWSkATw5oQd3YZ77UVrr9ketAp60c09-iiqhFV2dZ35HkSns-nvWWl9eAMTw9iAXyhAf9bkE84yxj0NZfTKuMNIMnu_B30BLTk6m6rRvlITL0qcpNY7nF3Ad7pP-tQl1XXrtqHuXG_RVXfFM7XQXDEVejvpaCzSK-MJBwu-buuz1j6s6uR5InXPsXx9ZKMz9pFdXihanXVJhydUuhmOtKFBkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
#فکت؛کریس‌رونالدو فقط 1 گل تاتبدیل شدن به بهترین‌گلزن پرتغال درتاریخ جام جهانی فاصله داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/23703" target="_blank">📅 20:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23702">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gWZsjh51JvBGzEOAZHh8ZE0qdJ7RTggHoEJ8SJIIRTlkxK8_-MVdywE2ledE6S60sVQz7QarxviVN_CYul431JQla_mK_UCqFo2L0rZ8rjRvpbvXJMyBKGdMZR9L-7-kdW0nodsyjreQlRyMeuDLOGkTphJarIFCMlal-SwoUX-cN6Bme-X9vHkuv4nVRIAMlkL193UB-w7_Gv7mXyA7pB239KsgxgM36awvGgG5puprXGyW8ORoLAendgMMKsl-S8Z7BznQqkwHswvCpPzXPN6feaDSofVYNL4_yDOxtVPUchk6X2A_OS0szMm8gyvkgJvdmOOrY0gP6R6MFyXdSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه سپاهان خطاب به نماینده محمد امین حزباوی: هر باشگاهی او رو میخواهد 70 میلیارد تومان واریز کند تا رضایت نامه صادر کنیم.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23702" target="_blank">📅 20:06 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23701">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z4Dmb8EWsQpKyU7dJ6e-3Xw1S65mdxqRj7_6jR-xRx8ZcXw03Yg96HYbqHMRUN2mp8EfraR91MVB_NKxWncnwyjZ5TPFeBWKdUGifhmS1TUs3FnmecGQJY-2qKj5pgKfTkSBkMWQgt3TVeP7VFPe3No85sLRE6kxvX2_6-4XY0ak8pfZwfVvyTqH-8BpA-gEL7ETWXerWdVnpX0ZiluZ1BiEU7IH0sitZidyHt1JOWHddNP19HWSotoTwcrnsTDohwnIv-Qv8_H_daM1ty4fW49-mbm0gAjFz22qZJ1y14xxII-7JyvnUleJLVMI3HQ9xGy7kpIG0exEqWbBOmWT1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌های رسانه پرشیانا؛ درصورتیکه اتفاق غیرمنتظره‌ای‌رخ‌ندهد و اوضاع‌کشور آروم باشه منیر الحدادی و یاسر آسانی هفته‌اول تیرماه به تهران خواهند آمد و به تمرینات آبی پوشان اضافه میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23701" target="_blank">📅 19:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23700">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r-9Tx7M_NJA6Ol-h-wWscxQS4Gqp7r_BqOro-FG32ek-TQU_oJn8RcxFdKMQs3ZfV8-3uVGb2gpp2x8Xn1TLwLxZVISI-7-5zPn8z0Lg01DRrU9Crw-P8mIe2pnEHHTpgVqsckVnTbIFpZxzEYBMHlBUjIoaKV7kSbJyXEFDZeADmb6Q1dA94EwzPscPmP8rzI3WOtgGoUknwpwukulVkKIJox5IOUSR7QCuU3cYbUZo3ChTiCEcvFb0UTuGwO5dQ2Hio0Y3J2yzx10nb3m0SRESrrAFulbg-uFGoW5U6GSWaUDK0b9uY4UFoHOzV6HoI_EurhIybW9UAJeogWc3ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ علاوه بر امید عالیشاه و مرتضی پور علی گنجی، سروش رفیعی دیگر بازیکنی است که در پایان فصل قطعا از جمع سرخ پوشان پایتخت جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23700" target="_blank">📅 19:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23697">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BPuzYzq9DTJs_qrKZcPGE_LQj_8fXK-r-FjInJOyMflS9rItJcOFg90ZvdmqlEvFqhxBzDRE7GulVULkJ9inEgr7AA_FO4Msc18BAijdW4QBVREAXXjJ-mFsINuWxwnAS4wkA6URS7MjxsMNMjrjVN-xzxhfGP1GWueJIcrpHpPCAJkIlhYRbZeb-E55-y4pG6gAN9175J4s25nxaekT0Fe94Jw1LL5rViFn91iznoI5jQp3o5GHKHpnmmBlynEeVrvP1zCF__JHo8bzTXC0JsMnR6vyYJYO7GSLe7ajrnQ03SLwUKIzBQ05g_hbeDRPA89NzP5CahypWzz9u6kmNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GWUTfERLivF5OULa-eYCwS4wS30nrMbmBgrTdch2Ny5GcpGSeKg-X1GK7nq0tufzrH_uoDCYnnmPEaj5IHUDdHAFFGS_puO-XJPoxQXTedkWelaWL9udst6mdyICdDAuunsCfVtvfe9BjcIKtynzogN-w3IwsaF1F0gUHKsFr2tVikYeKizPntbssWWCq8z2FlzryaG7GsX5nKrOMVNCmJu9WtfMvuPHrfEDnVRUP91jjkEwD5TzspSQ51-napOotCw4y29sHLbhe1zmfQA6WtteRbHJSwwCqyj-94NL11RXE_ilGfbBEA3ADQvPZvM0-zBj56ntXt7ZVWl4nBFOag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
هفته‌اول‌جام‌جهانی 2026
؛ شماتیک ترکیب دو تیم ملی پرتغال
🆚
کنگو؛ ساعت 20:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/23697" target="_blank">📅 19:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23696">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WlDfbWhhkmlCIXwyy5KB_Jb9fujL07LBPfBDYCp3zk9bV8ov6KEvnt5Jc440zr3nojtn-BaYaxuFCLSwOD9tbzt9l2PoTVSOCrfLV1V-_xr62e041llfQLnXRuiaQjBObyx_P1ksgh_1AOL9OBeY68yFJIjllzUas-nObkLN7bQNPMzP7H8mHoZutKQBrZn1TAmLyPJJVM1NU2dOzksLJb9PBHZiQRNxmUJZvBVYAr-2tij_ksjHEdifF8qLSvwK6XQw1MPAlB_CwU00McA4FJqR4p1vy9M6gqer4atCWR71VQwer_y5nX5wBZ-YlD00ekoejciJUNtUNCguLQ69kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ ژوزه مورینیو سرمربی رئال مادرید از فلورنتینو پرز خواسته از بین ماتئوس فرناندز و انزو فرناندز دوستاره‌پرتغال و آرژانتین یکی‌رو جذب کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/23696" target="_blank">📅 18:52 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23695">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d86iqxhBqqZE41HHCRjOSRKSKruqrrfJH_AxvGvjW76YdvatOHyVgTa3Tpze0Q8DWELHQkKwgor07OxVWtuNPgYCFx2sSodx-8rAworgJK18kdPzmw8GEr1QJTYtQ_e-V6F3cZdQqBJLbsdmiPNjFLVNTQ1d3mp2O310HxL-ZMh_KD6RvekeRTY0Ou7Cnjj8EBZX9r7ZKlYwJF8tKNfcyLjCGj2x2RaUz8BtJ1tfdDemEVLukwm-0i9BH4wSlV9bSdJ379anx2kiwL0iTTSmoi12A6aFZWO_gPCHoLa-hN1Bm4ruv1nPtKPPxYVj36rOFDLBl_G1tdXVurxqqmArxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه دو دیدار بامداد امروز جام جهانی؛ پیروزی پرگل آرژانتین و نروز مقابل رقبای خود بادرخشش‌خیره‌کننده لئو مسی و ارلینگ هالند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23695" target="_blank">📅 18:42 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23694">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sCI1MULmkN0Cob9GQaP8dDHSQE3sSeLRt4E7gBZ-Bi42qu3ZgCttzjc8uIFNJ-wHhfbyAJ4fwtXGZ-VYZxl-C7WvOtmcLuDvu0vGH8YskzS6BdGFvRocFLinWuDszGNvnS5nFm_R9pGkJ5QzyvPWIeRHb5HI80evf399_zOt-_9Vq8ngeF1J-1hBziIzzSDgAYbf7RGWL40lUktQyNZIvH_hSO0IuMSU9UI3weWmGlLJsnS50fjsCHo9QXgM05kAhjvDSWGhqUZBrWMcrmZluPCCK0ik1VdF22CzeCKyk-Ug6xa5-JWYBUNlx5kskBi4gQ50oErnxoUHqdoxEUHzUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
با اعلام ژابی الونسو؛ دنی سبایوس در رئال موندنی‌شد و او این‌پنجره‌کهکشانی‌هارو ترک نخواهد کرد. همچنین رودریگو پس‌از کش‌وقوس‌های فراوان به این نتیجه رسید که در باشگاه رئال مادرید بموند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/23694" target="_blank">📅 18:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23693">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5EI6QHJcocHOgeVVB8o_WZ4UENayhQDDJpUjEWNs3EG4AvmkRhABYaNnwnJoj-RbM8q8WJlOppVWLoWNtAc_qTaQE1cZz0nVZ_aPbaNsScXHikti-KqhhPkchWWOM9JzWg8CvY_u4V6RECRi3ReTpsjnWeKurikVOx7UOezxn7ph5AYh2xSlBCNkJxExB5a5GWgWnHJwJiNoaIBg_vrIWoFYqd6w2QCekBf4u7DFhpASFmKWqSjIusSBykWyLuNf7eWg1RuBSbKl2zD8vUOSoXz3pTrNdpvjQkGRfS8d7xiq69Mr9rK6Sk75DD-So9xyo-aqBiO87btcITF2jzbyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد...بااعلام باشگاه خیبر خرم آباد؛ سید مهدی رحمتی سرمربی موفق‌فصل‌گذشته این‌باشگاه رسما از جمع لر تباران خرم آباد جدا شد. به احتمال فراوان فراز کمالوند سرمربی این تیم خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/23693" target="_blank">📅 18:06 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23692">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b816759b6.mp4?token=KHgBWcHighL4uu_94gbWkCzQyjaVZkFD03Tvg4wo4YKGrhQozPVXQfgNowLFTL2y9rkLtUUydINfu2a8570ZNdfBMCChd4gHTWKGACKwbFoGMeu7Up1pP2t6RmB3uShOSnwhYzoVHXpecCcv5VYGDZ9sE4HxiXvATYZSS50GeQr_O6qjvXi2s_X8ArTtafXbt2HGwVQPDU6P3b1-g7D9x8Xp5fShdSnpD8l4Ka55oVgZJJKqqhdOHOo58vl5PDDCfUIIp7_FfC6Mrjds8Mb1dtIDztgVNPz68wOLkKOxNOXlcclyeqjz5NY3Vo36Wp6d8F37SlEnzyS8hLaQSqsOLW5ptm4mUPaX8V5wsmDqN0atmQKrVjCXYsJWKrHLGRB6rlOyU-lvqIv0Xw9LZG9JDNRPmejvbC613JuaoL6cgixd9-chfRkp8yUFL62KoU9FqFmXSl5y8DOtNvu-NN76egyL-gH0GOWjDCOHkIPk7J17iCkX1FMmBA6CzIpao6Jn9FdI74_C68Sn_-0yjFNggH7yPLJzJcDU5emkDIcC9ii3SRS-EUOCK4StI2m7NvRawSjX46t0fKigvBCvOndIzMavVB4jo5MtuL7hmP4xyhr1_yr2yCM_o078kIDD8oriDzSIcdlSeNb4OIkevB8c5mP5OTluRMWWNHa0mHnTquM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b816759b6.mp4?token=KHgBWcHighL4uu_94gbWkCzQyjaVZkFD03Tvg4wo4YKGrhQozPVXQfgNowLFTL2y9rkLtUUydINfu2a8570ZNdfBMCChd4gHTWKGACKwbFoGMeu7Up1pP2t6RmB3uShOSnwhYzoVHXpecCcv5VYGDZ9sE4HxiXvATYZSS50GeQr_O6qjvXi2s_X8ArTtafXbt2HGwVQPDU6P3b1-g7D9x8Xp5fShdSnpD8l4Ka55oVgZJJKqqhdOHOo58vl5PDDCfUIIp7_FfC6Mrjds8Mb1dtIDztgVNPz68wOLkKOxNOXlcclyeqjz5NY3Vo36Wp6d8F37SlEnzyS8hLaQSqsOLW5ptm4mUPaX8V5wsmDqN0atmQKrVjCXYsJWKrHLGRB6rlOyU-lvqIv0Xw9LZG9JDNRPmejvbC613JuaoL6cgixd9-chfRkp8yUFL62KoU9FqFmXSl5y8DOtNvu-NN76egyL-gH0GOWjDCOHkIPk7J17iCkX1FMmBA6CzIpao6Jn9FdI74_C68Sn_-0yjFNggH7yPLJzJcDU5emkDIcC9ii3SRS-EUOCK4StI2m7NvRawSjX46t0fKigvBCvOndIzMavVB4jo5MtuL7hmP4xyhr1_yr2yCM_o078kIDD8oriDzSIcdlSeNb4OIkevB8c5mP5OTluRMWWNHa0mHnTquM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
تیکه‌سنگین‌پیروزقربانی به کادر فنی ایران:
من‌ نیوزیلند رو راحت با فجر سپاسی می‌بردم. نیوزیلند اگه درلیگ 16 تیمی ما بود جزو چهارتای آخر میشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/23692" target="_blank">📅 17:44 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23690">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rhicpFH-0mhfWsVtocnOrMHvexGrCRsa0cr4yBmwXdQZJZM_rPoqt_lxJx0dYimdBIjkInyYfdNWuClUD9aFCzRt4-BwkBNOGzXc3rSLZI0qx1YIE5BWO0Bj4E4KiKQ97Jz8L4O94ZZLPNrYEUgHJQbWgyo4obQ8Zx4oCT7wy7US4IaEU7vvR-NUnlPXqae_cYfe8odaZUnHVcgP3VYMJKXKlsszPqMJNGjGV5nK5JTaivr4XluByge6GNEVgcJtHxOKNEf-C25nEW_ZNdEZcKuaCU0CtB-Ami81_GYEMvGzU1R-OALKcbTKHWCW6McXl812Aohlxr0sV36ibYNL2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YctO5bK4HslXID6Y0HFUJ-NaAtNzEeBFhpNKncGNsXZDnBc3ixUZiNegg9YMyWOgjiS12Y4y9rip_LxIzUKo1Rq9T7mKqK728QiG_RvvjVOE4DAfLVslSZKDLCaP6Xb_wIFx6gBpSHTnm2Y87QHxsZp3vhpKaabguqbNlvkOKoF-SEyXzXsKaCbSJpESz_5MBJf9Zv3LeIz_RRgjIxlycSAKwjnJmWH1B4ZSl_uoD-H5bEt36Z2RLPG5g1DNPDv7afBMp6Adyj8UXEDnyB6cFhhhdEdY04GcCGpegIIdteSnxHmz-e2M6xMZu60fgVNbFMMPfYKxes2pTnDzm_leYQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👤
#فکت؛کریس‌رونالدو فقط 1 گل تاتبدیل شدن به بهترین‌گلزن پرتغال درتاریخ جام جهانی فاصله داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/23690" target="_blank">📅 17:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23687">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KsDrx9vyZGq0V0C7ghFFZq5CaXh55Hl3LRN0P2yqtiR22AgepvJlBxBZL81cuQriuPH6OLX8ve9SbUrGqaKGYbs0sRibIpNR2QJzz5Hy5plgfTO2wlpTO-dtU6QhaL86a3jehB0oDFHueUykUZ25UZ-XIjBJIdoEARySb1xWPvmIT2ILE3WgRtGHR970Wq20JkRJxmUx_-YRYRDJl06qX5pBEyP1hd51p3OBiDp90cs6FKeAOhVxVok0xVeMPjkzqguziL90zPWMuzBli_YIVlQ--NBg82u3Rz-gZo9NAb8FKiecqdY-cAvk518N6Z4cN91rIYq7WIZlaj-V9_gv_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
لئو مسی در پنج بازی آخر خود در جام جهانی
🇦🇺
استرالیا؛ گل + جایزه بهترین بازیکن بازی.
🇱🇺
هلند؛ گل و پاس گل+جایزه بهترین بازیکن بازی.
🇭🇷
کرواسی؛ گل و پاس گل + جایزه بهترین بازیکن.
🇫🇷
فرانسه؛دوگل+قهرمانی+جایزه‌بهترین بازیکن‌جام
🇩🇿
الجزایر؛ هتتریک + جایزه بهترین…</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/23687" target="_blank">📅 17:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23686">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/012fc50185.mp4?token=j6-8u6aiNQp3SZlYjyf4JbMz-NdbbxSA2wHk1RXnEqfR7vztJVkFsKvi4FCQEtx5UQU7AVQGP3NrLUKsXiOOWIAwLKl8p6fvkYOEm94B3hl3K_H5z9vURB3ygB_369qLDITlXAbGYBc52Jm-OSaIUdlujmqOii8G2PKKQRtbgI_3H0f4YdP3Q1eNaQqEEvxn9_6JfhOnZqRbhN5gEVIyJlj-LfJKYBwA2vAbtKXAL22OjTWMd6aLlr7IwJ5o2EByUXSweKpgAUbPv4n4s_FN8ABUxUg0jua272QaEUUvfvwQeiUKCp7QkTFA3tUshqblE37WfOeMsvixjApHmOcOVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/012fc50185.mp4?token=j6-8u6aiNQp3SZlYjyf4JbMz-NdbbxSA2wHk1RXnEqfR7vztJVkFsKvi4FCQEtx5UQU7AVQGP3NrLUKsXiOOWIAwLKl8p6fvkYOEm94B3hl3K_H5z9vURB3ygB_369qLDITlXAbGYBc52Jm-OSaIUdlujmqOii8G2PKKQRtbgI_3H0f4YdP3Q1eNaQqEEvxn9_6JfhOnZqRbhN5gEVIyJlj-LfJKYBwA2vAbtKXAL22OjTWMd6aLlr7IwJ5o2EByUXSweKpgAUbPv4n4s_FN8ABUxUg0jua272QaEUUvfvwQeiUKCp7QkTFA3tUshqblE37WfOeMsvixjApHmOcOVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خداداد عزیزی سرپرست‌جدید تیم پرسپولیس:
من اینجا روزی چندین‌بار از حرف های جواد خیابانی هنگ میکنم. بعضا وقتا اصلا نمیفهمم چی میگه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/23686" target="_blank">📅 16:41 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23685">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KCUspSiw7LN3EZLDutjFg9eUFOfAbishyeDFFjdeoW54slCRjx18OYCVIwJQ4mr0dx4ImO7f5dFFama2W_be_hGONUp9QPngEDYWDEi1TgiVleUGr-Mal1P6Xr6f6BqkXzyixdPWIUHkYQzrv8Rhhbrg5_GSXX74Sym_7QZxOt5DEueNxHPSLvS1EVBOMjnGaZaBDDHH9EyIpfC00xqbZF9yIZOHtEQRgjkM2NSXOiXhn2nlfxzt9Piq5zZPnGxsx06WBJiL-M-9pqYW2rK0TOUFaxN3v_NKQsMuBHuLayVF4LGwrmoLyBOU_MXuYnLM7gTnflp3f-Qep7yu8h25Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
لئو مسی در پنج بازی آخر خود در جام جهانی
🇦🇺
استرالیا؛ گل + جایزه بهترین بازیکن بازی.
🇱🇺
هلند؛ گل و پاس گل+جایزه بهترین بازیکن بازی.
🇭🇷
کرواسی؛ گل و پاس گل + جایزه بهترین بازیکن.
🇫🇷
فرانسه؛دوگل+قهرمانی+جایزه‌بهترین بازیکن‌جام
🇩🇿
الجزایر؛ هتتریک + جایزه بهترین…</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/23685" target="_blank">📅 16:24 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23684">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a3b4e42ac.mp4?token=iqevlYh1otkv6puUdJlfFj60C7HVJ1rZnGjPuNdjivLBZTERdZ85AXyk1EzSbDQzWppHRDOIE8xDkZt3mgWsUpmveHVAzUsZpY8lBauBu0l4NEQLH_z2x65RxSPbTH936_ObU6BDEqLpsIPspXjd7WwlG_LArrCcuRso0QXE93M0TLCKTkI7fR_Hj_GsrVfAHCN3GcGZ7P2QlmwWF_777ebDaT41D-OH2nJrc98CN7oGiZPLJEbTwo9QB8zIkmleQl9LwNrlNcQ93pZNZuhQtjO6aOaFJveEl6pMjXt6JDvmI_S31A3FGrsuWsA10PPnbodjZ0wvlCF5Hx09TmeTmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a3b4e42ac.mp4?token=iqevlYh1otkv6puUdJlfFj60C7HVJ1rZnGjPuNdjivLBZTERdZ85AXyk1EzSbDQzWppHRDOIE8xDkZt3mgWsUpmveHVAzUsZpY8lBauBu0l4NEQLH_z2x65RxSPbTH936_ObU6BDEqLpsIPspXjd7WwlG_LArrCcuRso0QXE93M0TLCKTkI7fR_Hj_GsrVfAHCN3GcGZ7P2QlmwWF_777ebDaT41D-OH2nJrc98CN7oGiZPLJEbTwo9QB8zIkmleQl9LwNrlNcQ93pZNZuhQtjO6aOaFJveEl6pMjXt6JDvmI_S31A3FGrsuWsA10PPnbodjZ0wvlCF5Hx09TmeTmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇶
#تکمیلی؛ آیمن حسین مهاجم تیم ملی عراق پس از ورود به‌آمریکا توسط‌پلیس دستگیر شد و بعدِ حدود هشت ساعت بازجویی آزاد شد. اتهاماتی مانند همکاری با حشدالشعبی باعث دستگیری او شده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/23684" target="_blank">📅 16:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23683">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c34750719a.mp4?token=JTz3go3ZSAwdB41J1PZqVL9JPsnl7n5PT18nA_ZRYVXpRBmjS_5QIIiHq-6uA8l_nQyZ6ikbKZM_-Wr2uYg9yb0-LqY3qsr7_hEd-WtT5gb7gEfXToeHrR6cla0AyHWr9E9WTDENLfdm62aQn91KkeNDupZo8J93dhSt3JCCHv1g2OfKWcvOWdb-hqHNI8ntTUy2xGz8Rrv_IG1g9Ds76mMDCBwIr8HWhdUkKivtpflDH1yMU3U79J5TcOuAIv_5H7IBRGfVoUvDoBX2uQWDQCpeoIG4fnYVGHBpFnlFy5Jhdws-_xKzSu3REV1OcFZrav26d1XK-4EC_Os6BThorgC-OtqEo1oxKfIR0lSJg6JdlvcrqPE1hwnHX_1ANAWCro5omaxcLXvp9Ux2vnn7dTNuMqTVoCgr-byRhhk2feoIm5_Ouk7URyCcLsTzIJdE2W44g6uo0M6lUDxYZPyUGnSS4KV3e4iAUIeA91GS3n_9RVubnysyMWFf6F5zQVIJRh-27I5PR3tH6EJqG2j6jhvhddeVI3w2ealMxB1hCi9hYIopeKDJ4mhEqng6Zehk0H2wtb-cuZWzGdU1z06fuvhy5sGV8K_MKBA6DvXRHcu8WEbBRFYGRmcEGwZi8weJMjBdc4TgHDo6l3EYyP6GBlCr0x4i0F89qjpuratpkuE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c34750719a.mp4?token=JTz3go3ZSAwdB41J1PZqVL9JPsnl7n5PT18nA_ZRYVXpRBmjS_5QIIiHq-6uA8l_nQyZ6ikbKZM_-Wr2uYg9yb0-LqY3qsr7_hEd-WtT5gb7gEfXToeHrR6cla0AyHWr9E9WTDENLfdm62aQn91KkeNDupZo8J93dhSt3JCCHv1g2OfKWcvOWdb-hqHNI8ntTUy2xGz8Rrv_IG1g9Ds76mMDCBwIr8HWhdUkKivtpflDH1yMU3U79J5TcOuAIv_5H7IBRGfVoUvDoBX2uQWDQCpeoIG4fnYVGHBpFnlFy5Jhdws-_xKzSu3REV1OcFZrav26d1XK-4EC_Os6BThorgC-OtqEo1oxKfIR0lSJg6JdlvcrqPE1hwnHX_1ANAWCro5omaxcLXvp9Ux2vnn7dTNuMqTVoCgr-byRhhk2feoIm5_Ouk7URyCcLsTzIJdE2W44g6uo0M6lUDxYZPyUGnSS4KV3e4iAUIeA91GS3n_9RVubnysyMWFf6F5zQVIJRh-27I5PR3tH6EJqG2j6jhvhddeVI3w2ealMxB1hCi9hYIopeKDJ4mhEqng6Zehk0H2wtb-cuZWzGdU1z06fuvhy5sGV8K_MKBA6DvXRHcu8WEbBRFYGRmcEGwZi8weJMjBdc4TgHDo6l3EYyP6GBlCr0x4i0F89qjpuratpkuE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
👤
ویدیویی زیبا از شاهکار فوق العاده علیرضا فغانی دربازی‌ شب‌گذشته فرانسه مقابل سنگالی‌ها؛ همین‌عملکرد درخشانش‌دربازی دیشب که دو تصمیم فوق العاده گرفته ممکنه باعث بشه که از همین حالا بعنوان داور فینال جام جهانی انتخاب شده باشه.
‼️
دو تصمیم مهم فغانی این بود:
که اول نظرش رو تغییرنداد و پنالتی‌نگرفت. دوم اینکه آوانتاژ داد و باعث شد کیلیان امباپه اون سوپرگل دیدنی رو بزنه.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/23683" target="_blank">📅 15:43 · 27 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
