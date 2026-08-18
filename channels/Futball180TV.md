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
<img src="https://cdn5.telesco.pe/file/r2lH4ZFr8H4chZZ9tMIsPraTLvjab0fQixETX8G4meLDObWwMxf2HHw0OdmDsfpjoMA-fLVEF6wuacjyKNAYpVeqD-S18uUJlUj0kIPa6gvwO_9BibbYmnxtYOHPCMwyx735Ls3hLZWNMSxBl_Vqo45XSPJNXqH2mKN4oqZurRSLCsU9KT9tgy6ox_3fN9jD5uA2WU1FzvKD_mxDlKs2YZ99CLH3RBaW7qQjL6QrWgW3M5ArW8sd6HPzDpG8o5NffgkY86O0L42EIl3qow5lIqpX_8QjfHNy4DMcsZVWGOv6npuxjZxNZlKGUJBAtJMA9suF1b3AFYexfUYMkoLkiw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 458K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-27 21:20:59</div>
<hr>

<div class="tg-post" id="msg-104082">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lWyu4-8eeIzM84IimpApzcBLwXV4MGzaPvSK17ZaD8kOC_GhPwK5Jp7pEzjHCzVuTZXvmvrFH0_WrqL0ZjMhBFukpRqe3CdtpoCJQ96QBnprnQguPLwQDM11XYcsld4pG8MWk4Xh0gsJyjzITxDt8ofZm9_rYELuVux9x7Vrt6O0yyaDLvQqM1fk2unT1nMhQqfqA41o7tx0FcyizmxbEiJfC5ZyNL1Rm858ilaTk4YcuPAI9lLbTmdMQ133n-OjRLg8RmjxgCVDaZYeVSh7ZMl8s-UlR_jQRlOa7PuD3VnrX7qo7PC6Svgtucot8sdyyewugHg_6F5CDMPYGxHkXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇮🇷
پایان‌بازی هفته دوم لیگ‌برتر؛ استقلال به سختی برنده شد؛ فرشته نجات سهراب، محمدرضا آزادی بود! آبی‌ها با برد شیرین به استقبال سپاهان می‌روند
🇮🇷
استقلال
😃
-
😏
نساجی
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/Futball180TV/104082" target="_blank">📅 21:15 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104081">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66e078a045.mp4?token=HoX7CSmxKQQbIAGSOiIBfxjcGvzJHwAnoZjar1JUsO0mqKuV6jNmtyw-FczQ356SeMpAcnwT6hdSIWOv80ACIENVGSre34g5Ke811Q0xEG66IrpggdmwBxlHSvVm2Ox29Y6ieflFLUekTt1qaGQPWSHSAuy8BZu1y-cTlfJh8UI_6avuqljHpr2awQvvfe0zxYhVaPys7Vq9IY-XkiS_yzfqWMzQRda-N0BcU4CRowgtEOzwEQtspJAtT_tsmOUqpivQwHUTvtFubGgZ9dur9U7Yw-8sorYdBCzmIx9aAWYoiwobKV8RWUjc5w0FVn89Qvq9MZPW-dqRcu19pH2VzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66e078a045.mp4?token=HoX7CSmxKQQbIAGSOiIBfxjcGvzJHwAnoZjar1JUsO0mqKuV6jNmtyw-FczQ356SeMpAcnwT6hdSIWOv80ACIENVGSre34g5Ke811Q0xEG66IrpggdmwBxlHSvVm2Ox29Y6ieflFLUekTt1qaGQPWSHSAuy8BZu1y-cTlfJh8UI_6avuqljHpr2awQvvfe0zxYhVaPys7Vq9IY-XkiS_yzfqWMzQRda-N0BcU4CRowgtEOzwEQtspJAtT_tsmOUqpivQwHUTvtFubGgZ9dur9U7Yw-8sorYdBCzmIx9aAWYoiwobKV8RWUjc5w0FVn89Qvq9MZPW-dqRcu19pH2VzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇷
گل اول استقلال به نساجی توسط محمدرضا آزادی
82
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/Futball180TV/104081" target="_blank">📅 21:00 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104080">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">محمدرضا آزادی برا استفلال گل زد
😆
😆
😆
😆
😆
😆</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/Futball180TV/104080" target="_blank">📅 20:58 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104079">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🔻
#فوووووری
از دیوید اورنشتین: باشگاه نیوکاسل درحال مذاکره با سیتیزن‌ها برای جذب نیکو گونزالز است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/Futball180TV/104079" target="_blank">📅 20:39 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104078">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9CdFZREGw5hRjNo0_ifsZl35n6cv2SEBbVaVgRU36XWSEckH76ITzfc0J82Bc1OWCOFoYPwewkK0AF1IPFefaUTuUYcPhYOZ1R55w4ZkPUnptSJ4HpxSPKzIDO7ls_FYtDRjg4UPREFtudrmC913O_OmEVbD1wmAyB2cTPukeP2TxnL6YXBkuC4dLh0GblhZF8WWr8tQd4rhriXSrkgTYA6IHPuC_4LWlbBwNX5KS4VE5mju0ICATA1dzvRY5BeGFPMyAh_R43Wu6_2zDxgKUov5-IpeOh6m8Q_n4zkh0oMpflLcXt_yw7V_ZkRE-XXvr5v5zNIf8UhO1fETzH_nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🇪🇸
🇪🇸
رودری:
"گزینه‌های دیگری هم داشتم با حقوق بسیار بیشتر، اما بارسلونا انتخاب اول من بود، و این را به وضوح بیان کردم."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/Futball180TV/104078" target="_blank">📅 20:31 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104077">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qzzx_5DYMvZ8CvQ0GO15kWqGCfR3gvqLTqefCrTcgRRkR3mwHmcUwTYs1orC_f2M1M2VTix0_0ojzM5N1bIasG8IHeoj4giQ0Oi0nlSK543QDTPwe4i0Z6IrbhEGQVUrsApVPbMPg86TZKykwisBwAdnNQzDURkQuEhk5CO5fVlkRFesH6Q2Irb_W2T3L-L58ZUAtCHjp5I1_91G4knIDkUMSzEy0gqYlF6VwrH9bnF0C6G5f8DKDT76byX23jJNtvsHBIG04b3lnsgveFKodGz42SglJrfgBmj0MOSJlzEwJgNAZmXOwZSgkaY8F-BJLbDHkxyiQ9Pr2gUR4P9rMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
🔥
🔥
🔥
رودری در کنار مدیران بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/Futball180TV/104077" target="_blank">📅 20:21 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104076">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m7wiOWX6ohq56fIWe2ottCQqsOmjtgPh0sJdd1F768zHh-cfbjbzuhEPvmXnQoRFPa-AARgeYBaV_z_o-UspbTWIajn8wS3uz7vnPF7yYCmHAsDdYElRZKnzADtgT6NR8UFi6egonc5hTR4Yr98riNwXaG6zWSiU-MUMWcydSV3rd4q9YrPm0aVW2gvuh1DEc7EQu1xcPWHQ_rGE5zLy5TjtjMN_GhEWB-mMU8SBCvJkt8INF4zWvQWUEHDtBP5zp45xGxp1OWANX9A13vHwqRTSQndZlTfAA0GWj5kDlUTmJmXLfspKZDhCJmaT8XaA2pXfpIDjrX4csl9P1Hd9Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
پوستر منچسترسیتی و خداحافظی با رودری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/Futball180TV/104076" target="_blank">📅 20:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104075">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/944bb3a08a.mp4?token=ZWMHwDLsNqINdPTs1mg4NwSHvG1pjGIByfVaoZ0cWScP8pZ_p7AI6mjbdsqeDVP2AsZpHA4qu-xRy8VayH02W4GkAsjBxtoiz4Sqo0DCkbpi9uKOsGll62zxkFJ3BdMvSXQ7OrQIiboese8ytU-H4gnhv33SGUNb3Nzw2GTqwxdQFl1CU3g9vOfg8nCcjiD43Fh9752pTP1d1buv-EnA0-x78Rdbmac-PO1Se9tcBykEudSNSF8hIP82RBHNZja283ND6_ykoTWU6GzQ4kzaVZTFBPIJUt5YPrVhbfSn4PW4m-OJh0QLqDHI2MCoZQ5sZtFu0TRwNhaGX6SK0fImZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/944bb3a08a.mp4?token=ZWMHwDLsNqINdPTs1mg4NwSHvG1pjGIByfVaoZ0cWScP8pZ_p7AI6mjbdsqeDVP2AsZpHA4qu-xRy8VayH02W4GkAsjBxtoiz4Sqo0DCkbpi9uKOsGll62zxkFJ3BdMvSXQ7OrQIiboese8ytU-H4gnhv33SGUNb3Nzw2GTqwxdQFl1CU3g9vOfg8nCcjiD43Fh9752pTP1d1buv-EnA0-x78Rdbmac-PO1Se9tcBykEudSNSF8hIP82RBHNZja283ND6_ykoTWU6GzQ4kzaVZTFBPIJUt5YPrVhbfSn4PW4m-OJh0QLqDHI2MCoZQ5sZtFu0TRwNhaGX6SK0fImZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🔥
🔥
🔥
🇪🇸
تیزر فوق‌العاده جذاب باشگاه بارسلونا برای معارفه رودری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/Futball180TV/104075" target="_blank">📅 20:14 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104074">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/szBGq6F9nqTc4z_yNz7EPDcFgWU3O2qDXEr4FuQhmN-KFHhrajICYJVeMjdykrUINPInIGhAssvfsNSoNKu0qvIuwvVcPgv_LLBAlteT4BlOpsonsckUvisAAongBtdE_ws4erRO-BxYf_gOTQ73idd9Cfq7q1p-OpEfQN0QHBWnv06HwOsMcWc4-tvKOKyJ3921tgdiWmDuE5mpkOpqgdpGyIA6wKEdAoUrAF8Hi__ojGkdR09pU7_pOo4nOJHRb1afRT81fskjSp0A1NSBNgeNn1-7zc-LNkh-NznvAJXcVjbJN1oIOm5CuXDINpUqUdibZir5y9lPrvXdX_D-IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
#رسمیییییی
:
رودری به بارسلونا پیوست.
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/Futball180TV/104074" target="_blank">📅 20:13 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104073">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
🎙
🇮🇷
مهدی تارتار سرمربی پرسپولیس:
🔴
قهر اوستون ارونوف؟ هنوز یکی دو بازیکن دیگر نیاز داریم و تیم کاملی نیستیم. در برخی پست‌ها کمبود بازیکن داریم و نیاز به جذب بازیکن داریم. باید تقویت شویم. حاشیه‌ای احساس نکردم و اورونوف با همراهی کادر پزشکی به رختکن رفت تا برای نیمه دوم آماده شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.98K · <a href="https://t.me/Futball180TV/104073" target="_blank">📅 19:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104072">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/anJdlhitVA0DosNu0A2OoGSL0_u9gJE1eAiyWBiVdqP3yCH-OreDfzkmvyoRkP_Mu_yji0kIprZi3x3oT18Ihc-Kf7U53KrezSN_jgYh089IjLI-FcQXypWFDJRNHZ6gmuceKmYyEYKDt6YoEBCbosoW4bhiALIiJdpPHY23qxxT7iW7FTW_OL70FhnRJagrOmh-V1pfNjWpGht3m-Z60n8okcAO9aCi8-NzYoo1drGG4jObhR7rJsM9WuCrUiW4RTaJ6FoBEmMGyQWYCLQ_1MulexOPwqcLyO-6iVIIAtbI9kPdct5jW2BmxaTW9AEqUhPNHKcFSgHawR_W1zcC5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
❌
🇪🇸
جرارد رومرو: احتمال حضور آلوارز در بارسلونا این تابستان بسیار کمه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/104072" target="_blank">📅 19:37 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104071">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t3hB8gLfTc4_w6Y3WuNv_wdczP3IOMoXbVmRymfNlGHflOAqO3CmSQTfd8xc0bySAufdHlnt8jlGZkF932LLaUe4R6Ogvzp89UWmmSWCdZWp8YSof21FyTCO9eyLySVCbRprF5JFkBnIR6rGvET_vCulACSVTTqcbw86hj4NB3iIbFpw-S_AYsnHznSpQzUECdjjLyHKDEVXAmfav5W3Yfvq-7xMMW-Vw4pCVE7k7K1sYVElCQaGEhAo6nn4R0ZucFJOnhnBLoBW865pQDF6H5uUvIbGHejMV7Fw1z1Px_DwUKJenNEDa-9aF5RhI6y3kF6MR_VltVudfiM702tkGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌏
🌏
برنامه کامل مسابقات نمایندگان ایران در لیگ نخبگان و لیگ قهرمانان آسیا ۲
✅
🇮🇷
برنامه مسابقات استقلال در لیگ نخبگان آسیا به شرح زیر است:
🔵
استقلال ایران – السد قطر، دوشنبه ۲۳ شهریور
🔵
الغرافه قطر – استقلال ایران، دوشنبه ۲۰ مهر
🔵
شباب‌الاهلی امارات – استقلال، سه‌شنبه ۵ آبان
🔵
استقلال ایران – الشمال قطر، سه‌شنبه ۱۲ آبان
🔵
العین امارات – استقلال ایران، دوشنبه ۲ آذر
🔵
استقلال ایران – نفتچی ازبکستان، دوشنبه ۱۶ آذر
🔵
پاختاکور ازبکستان – استقلال ایران، دوشنبه ۱۹ بهمن
🔵
استقلال ایران – الوصل امارات، دوشنبه ۲۶ بهمن
✅
🇮🇷
برنامه مسابقات تراکتور در لیگ نخبگان آسیا به شرح زیر است:
🟣
تراکتور ایران – شباب‌الاهلی امارات، دوشنبه ۲۳ شهریور
🟣
تراکتور ایران – الشمال قطر، دوشنبه ۲۰ مهر
🟣
تراکتور ایران – العین امارات، دوشنبه ۴ آبان
🟣
تراکتور ایران – نفتچی ازبکستان، دوشنبه ۱۱ آبان
🟣
تراکتور ایران – الوصل امارات، دوشنبه ۲ آذر
🟣
تراکتور ایران – پاختاکور ازبکستان، دوشنبه ۱۶ آذر
🟣
تراکتور ایران – السد قطر، دوشنبه ۱۹ بهمن
🟣
تراکتور ایران – الغرافه قطر، دوشنبه ۲۶ بهمن
✅
🇮🇷
برنامه مسابقات گل‌گهر در لیگ قهرمانان آسیا ۲ به شرح زیر است:
🔵
گل‌گهر ایران - الجزیره امارات، سه‌شنبه، ۲۴ شهریور
🔵
گل‌گهر ایران - المحرق بحرین، چهارشنبه، ۲۲ مهر
🔵
گل‌گهر ایران - آرکاداغ ترکمنستان، چهارشنبه، ۶ آبان
🔵
گل‌گهر ایران - آرکاداغ ترکمنستان، چهارشنبه، ۱۳ آبان
🔵
گل‌گهر ایران - الجزیره امارات، چهارشنبه، ۴ آذر
🔵
گل‌گهر ایران - المحرق بحرین، چهارشنبه، ۱۸ آذر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/104071" target="_blank">📅 19:25 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104070">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i_cG_IRVcTp_pKJ_C4GYx4q3YGmVCDRKmMFFzP3nC_Cr3hJDV_mW3jqP6e04N3utapA9gJVE7iVepe0EdJGNk8eSiMQViIRfshR2F6PxCsu1LwTklgB-6LeHIggmUOnK_odt7KUIc-jKkNqxDlMXAICplxeETAj_-1ev58sSb9qJGmgCW-49V1iejz4DN73_7WLlFhloEiaHjnMpwVTr8L6tiNWRg0S0aOmgqxCtJWo6wAS3jxRpRHgWxS6i7V_27O9QIjEkn52A0KTKX5hxkc1GvDUfM8crye1-QcXU4CZtWgj8yXwEWmf64BCJzv_vN38pl2WMjI8NI4q6DI7jSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
❌
ویکتور ناوارو:
‼️
بارسلونا برای پرونده خولیان آلوارز حداکثر تا پایان این هفته مهلت تعیین کرده. اگر تا قبل از شنبه هیچ پیشرفتی حاصل نشه، پلن جایگزین را فعال خواهند کرد. سوپر دکو همین حالا برای پیگیری پرونده مهاجم راهی سفر شده و در مراسم معارفه رودری حضور نخواهد داشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/104070" target="_blank">📅 19:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104068">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DKmPyrClGo59hjKyL0FES3YVvfOHERN7-XPLfnC-SPdFjEeeeTrEXll5UtIuQ8vpkH_V_PcBmKN9Hxslk8Q0MiW11ePdE2coJ_sJd-S7k50wJywWeVvo-qLVj6lGUEDEXB7CrGYpvkn6UUIfu-KfhHSGHC0yPHnlxqwFiCFFbCHEMEDl5ybFY6cFAuiHh7OARgzXl9nZbBxSCJlWJehbYT-4gc8pFzXHsw2sQKLBSau-RchbQtYjNwIqCVhbnLR_89JIvXFdrX_xw1pSkkJgIbgm7L6wo4fc7LKU9FmVEHjH2nM6aV7WqYOIHSWHE0H05Q0JdjD5k_gpPfSfJlEW-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gJ_8BDJYtSGSeRPLHSpDHFNCFLhyFlKa2GMeZdabLs5JtqB72ClIKHTtAY5guvlCfOWeF5cnylljltked228iHNzNHyJghjUzFuzvhS7be1XZ9RlTHZ49wTd1lL5t2Zcv5ICHQwZ96Ukf9p0vsx00CClJGd2icM8E1Qo2gmFOe5JKOwEtCsetiyNj38CWknPqoSDmV56fxlCnkrwOHDYYQKdoFIcDbL57IjWAmtEdothRAfGPq7f-SZi4MQRUUuhs3phk-A8gm2uS_m0LUxpCcGQOFSIyw5OsDMw6G9hSJ_Z2cJ6rYQIF6JDLQIaau8aKvt7phy7R_2Yjmnh_9jjtQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
ترکیب سپاهان و تراکتور
ساعت 20:00
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/Futball180TV/104068" target="_blank">📅 19:08 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104067">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">46.2 MB</div>
</div>
<a href="https://t.me/Futball180TV/104067" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇩🇪
آپ اندروید سایت جهانی Melbet
💥
🎁
بونوس ورزشی هر چهارشنبه
🔥
💸
واریز و برداشت متنوع
💵
⭕️
بدون نیاز به فیلتر شکن
⭕️
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 8.58K · <a href="https://t.me/Futball180TV/104067" target="_blank">📅 19:08 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104066">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IPuzZGEpX--13WxeBiFxeUK4bmEwfJPrz9G0L_PyMDhJK-XpU_6p8NTzCqOpm-TjgTVOPc287_Otkv8X35oJrJg7ufiZ2qCDBBszOIMJ69KBph4umscFVnYvx1TE0kSwmU4ifGi8A-vDkLang41LYZQ9-wY1o-_FsgnNtpZe3KFYYCYrotKUek4PobAQbNrNooHSIEi1lV0cHoAc4M8ubEam9hM8kRtGa2NGshKDkqqlNUPW0cdEA6PJ1R-rVuIwM8CtRWbF6hu3a0F-_uQ5iKmr1F5Hw3WPomushdCfJ0gHFZQhwfnJcu2_79ntzj-VuO6uWBJLK48HhxiJ50DWNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎲
سایت جهانی  و معتبر
#Melbet
🔴
بازی های مهم 27 مرداد
🆗
ثبت نام آسان و سریع کلیک کنید
🆗
✅
🤩
🤩
🤩
🤩
بونوس اولین واریز
✅
پخش زنده ی تمام مسابقات
✅
درگاه اختصاصی برای کاربران
👍
پشتیبانی 24 ساعته فارسی
🎟
Promo Code: MELBET90
🇩🇪
دانلود اپلیکیشن MELBET
📱
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
g27
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/Futball180TV/104066" target="_blank">📅 19:08 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104063">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9118e624d.mp4?token=uqZiF9PQQRUiqHB286Uxcsg5wjdiQ9VUBp8H0MC0maSq3qqYqw1mjz1CqxcejVhi6YP_WXw3zYrHKdHKoAxN_sRkJtK9H94SzQVeJ6gZCdeYL7MkXBVwDH02oLqum8TgWqiiJohzAvXidx0OADj8wg7l6EUyNjYY5QmxKmASpTW3SvcQ0ysIFMXgEtSmojcYS2yth174IZ91ctJMRfdBtt8CDRX_gd7eg1QAiADRPHW3Zo8USjrJ0e8l9YTZRMRTXTNYEpP2QJt_K7YNx6_qX4YYUlFc4mn9U6TKRlW5AReeKW09K62ZEatn9aE6IGhScM8Z87VuWE-mEkxUtkVUMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9118e624d.mp4?token=uqZiF9PQQRUiqHB286Uxcsg5wjdiQ9VUBp8H0MC0maSq3qqYqw1mjz1CqxcejVhi6YP_WXw3zYrHKdHKoAxN_sRkJtK9H94SzQVeJ6gZCdeYL7MkXBVwDH02oLqum8TgWqiiJohzAvXidx0OADj8wg7l6EUyNjYY5QmxKmASpTW3SvcQ0ysIFMXgEtSmojcYS2yth174IZ91ctJMRfdBtt8CDRX_gd7eg1QAiADRPHW3Zo8USjrJ0e8l9YTZRMRTXTNYEpP2QJt_K7YNx6_qX4YYUlFc4mn9U6TKRlW5AReeKW09K62ZEatn9aE6IGhScM8Z87VuWE-mEkxUtkVUMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
👀
🇮🇷
لقب جدید هواداران استقلال برای «رزاقی‌نیا»:
سرخیو بوسکتس ایران!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/104063" target="_blank">📅 18:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104062">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tNY2AvSLQKZwYQPBn8X8k0cB-G2IXq3ymMFm7DpSP1S_x73UXZybP4uWDQOF5WSYWGje3-SaLfwehQLEHFQpSlONmBfZ7S79j_5qZ2Y0DPjr_bKHl55kBLHeJbzqrnM0kZdZGSwVjZTwUsoPwPFponpajzAXkJIhYXD5xmJO-QlogVdmpWN50iA70FLtpL0aZI1t7mpb2WHD_s1-cvMBm5WEJf9auDEx9SNcuJPQoEfyjTx6c8f5blmo0tBqF_qx5TAtBQqPJnpZgh27hLd4RzTzyS0flz6CVzXz6p80Xm_Ir3VCpjyrTPYJWu3TQmii2JJ9gs9oiNI5CqbYXIiWVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇮🇷
شماتیک ترکیب استقلال برابر نساجی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/104062" target="_blank">📅 18:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104061">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oE7n8_wd-fAHFQaCcBPhFZ0TqGh5oHQLq_MfoKs2qrj7sfIq931fOY48EKnWIkHKvf5rYKa1e4nKwlcKPX1kdsPJanE-FKw80gi1grEHKraVXrVViIr67bDMC9TH9ofrEw8Fe8mCDr0ZH5KFo9eufzmfN4J_FOhsGua9oQ-sKbrdBl8LDACSCZoUuetiZdpX1MFsjduHu22EruY3NSQpIQMx3G7YRzMgMErITXvA9UcFTjVKh98JBUdFgkEQLzO3ZBItRCLpxlTWWPMJxqBLKtzul760VGM9um65KnIzlfVA5q2GnbGvbbItb961FlLXV6Hw-6nIB_1evIC4wmtdcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇷
ترکیبببب استقلال مقابل نساجی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/104061" target="_blank">📅 18:15 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104060">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9049374609.mp4?token=tQ2GlijZAeLa5r4afMasridmoFBezpsVUDl1jJ6OUqnJ3MA-OEGnkFLjSbd8Jp6532qY_b-PxS1svK1sEzxg42ngmQHfEAbiFMXxlmWqajf-gMGkvAXJbqOZMUMzmyODfs2tBocrG71yPzqAtcKqZpAlNEZHUdCvYNUVJKBgX8COet05BssWuVAAfxnKET_760RxD7IPFr6EEOkVRnyQn6PyOhoiqeiYDs24mc7dpco3_XGXy3PWbe-hOyP3yo2YKQsFWpPRMx_KTNPW4LHjY979SosDwKTpsWxdOr0ZVV9Tzo5M2eNWaDznQ4pbKASl6LL9oC6rVL8uWlJFFsjo0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9049374609.mp4?token=tQ2GlijZAeLa5r4afMasridmoFBezpsVUDl1jJ6OUqnJ3MA-OEGnkFLjSbd8Jp6532qY_b-PxS1svK1sEzxg42ngmQHfEAbiFMXxlmWqajf-gMGkvAXJbqOZMUMzmyODfs2tBocrG71yPzqAtcKqZpAlNEZHUdCvYNUVJKBgX8COet05BssWuVAAfxnKET_760RxD7IPFr6EEOkVRnyQn6PyOhoiqeiYDs24mc7dpco3_XGXy3PWbe-hOyP3yo2YKQsFWpPRMx_KTNPW4LHjY979SosDwKTpsWxdOr0ZVV9Tzo5M2eNWaDznQ4pbKASl6LL9oC6rVL8uWlJFFsjo0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کنایه‌های شدید هواداران نساجی به دانیال‌ایری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/104060" target="_blank">📅 18:14 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104059">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZQaDt9dZuAtzGmebUf1b4akTg_DXoVgMXrej7WhKITBjV67sRWKxhYCsVGOi1XxomZ9xsI2K3PaWytxMoJlCUnmr5W-oimM90XfzIG0wMqw4mbQWb1UsTZwP_lc4A_5WqezAamU9CktTNC1pKBEhvWD7I0ZDGo5OkdDSfHkW1yhcmeaadkNP8Nwx76u9Cf59729gEgr41c8ig46arvSDuoTl0evFJSlFrSxo4tBD7EVA5JZUii-aUGBBJ9K8Pppp1FUd12jyR2KfFtJk7Dnh_aHfy5Rbcf6tTfaxPTvl3V-iT7ZD-eyUfhelZHOmEEvRTFuCTdYHh_qymXYB0k9Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
✅
پوستر باشگاه برای بازی فرداشب با تصویری از اوستون اورونوف
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/104059" target="_blank">📅 18:13 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104058">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qojXp4PUvpfFwMkXOMZrdxDGJWavNktQG3tX--kHdhG4NShsSaw254ONeptD1F5CCc80BaUp35XNWd1xwI8h5nwKlDJ5r4vHMp-SoS9Ei6rz1rEtuKyjvR77O4bF9qS2KPXfVBClI6MZqBOVdx3XA5J_apqkWhZMOBx-AP36XKaxI4ZxszVHdASGaCc9KleoL7QZyJH60STkTcVmJy6PoAaHdUZEVaNH9YLhdYsOooxB0QK2e1_1TTTlMkRxGg4S8m6jnrgRd7m8CWcfcdrBVkJu0K7g_j4vZBz-IRUelHG0Qn6Vp-J8a0OuIuAPPpSH5mLxBxsof_oDEKYsYrMz0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😆
یه HERE WE GO که بارساییا منتظرشن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/104058" target="_blank">📅 18:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104057">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aba95804b8.mp4?token=Zjm6_LiROycYhhoUD2yXN38NHuekPlgvqEiewTd9IWpNHlTm-DJ_t62w9VBb5WPFVfnMKp6KoF8tOYX-G01opFO-Lqfwf0Q9LaXo297iRE-n6FKWFZTQ0G-RRJx6MGcLdkBd9dxEMPeDrewSvrvYcpnOrrVUDflTYZFs1ZjlG7Dn09hQMp_Pg03eh4EVfZshWBwSTMq5EYcEMBrsei74n5m97rwnI7va-6iTo2_liOPMXnBNO_eWJpnDbhNVg0yJLUPOZV6Z1PbtUiNVseNSsN_KVPno09dd3TTuTXtfjVikvq5W9kTzljxw3vmT3_Vnx2rBqjGmG7Xgey4T_X2Q9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aba95804b8.mp4?token=Zjm6_LiROycYhhoUD2yXN38NHuekPlgvqEiewTd9IWpNHlTm-DJ_t62w9VBb5WPFVfnMKp6KoF8tOYX-G01opFO-Lqfwf0Q9LaXo297iRE-n6FKWFZTQ0G-RRJx6MGcLdkBd9dxEMPeDrewSvrvYcpnOrrVUDflTYZFs1ZjlG7Dn09hQMp_Pg03eh4EVfZshWBwSTMq5EYcEMBrsei74n5m97rwnI7va-6iTo2_liOPMXnBNO_eWJpnDbhNVg0yJLUPOZV6Z1PbtUiNVseNSsN_KVPno09dd3TTuTXtfjVikvq5W9kTzljxw3vmT3_Vnx2rBqjGmG7Xgey4T_X2Q9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
🇮🇷
🇮🇷
هوادار استقلال در اصفهان: فقط امروز طرفدار سپاهان هستم/ تورنمنت سه جانبه؟ قهرمانی حق ماست!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/104057" target="_blank">📅 18:07 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104056">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c1f1fb50f.mp4?token=a33pNwjnk3XNcEJ4lx6_piB_AEU_B6sahHU2o6yjfSQKQiV0IIc_mlV-dDOyg9NOl_1AD4zgMJXGkL9iJQx9lrWODy7LcpCUkIwNkiALQHrEsbCl5s6q3VQXwe1QOwKDpJ69AqCFXtOUxw6uKW3xffk5p3UFVsCWailTqX3ezZ3wLi0bV2e0ErEuZzaDpveEqudJjYoe3xIHF4vagPHa_37BXCjTUPEhbvzqcyDhVxngU5D6esOgRBeZX5RrxyV7or9QOqjcyxKLEAUA7cpbbzHiWLqq2BH2NruUsDt4o79cjIGEsGPJru4XZz0qH6Hj0AZO56PpsMwaJky6olG60w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c1f1fb50f.mp4?token=a33pNwjnk3XNcEJ4lx6_piB_AEU_B6sahHU2o6yjfSQKQiV0IIc_mlV-dDOyg9NOl_1AD4zgMJXGkL9iJQx9lrWODy7LcpCUkIwNkiALQHrEsbCl5s6q3VQXwe1QOwKDpJ69AqCFXtOUxw6uKW3xffk5p3UFVsCWailTqX3ezZ3wLi0bV2e0ErEuZzaDpveEqudJjYoe3xIHF4vagPHa_37BXCjTUPEhbvzqcyDhVxngU5D6esOgRBeZX5RrxyV7or9QOqjcyxKLEAUA7cpbbzHiWLqq2BH2NruUsDt4o79cjIGEsGPJru4XZz0qH6Hj0AZO56PpsMwaJky6olG60w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇮🇷
فروش بلیط جایگاه استقلال در بازار سیاه در مقابل درب ورزشگاه شهید وطنی قائمشهر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/104056" target="_blank">📅 18:06 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104055">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tBcV3263nVSE-KU8olvO9X6SzcXg7vtva1EmHz6KKkjQvJBGpJO_3YM7TmPEScEzUpy5OpHB4rt7fBickQRndBPwbrU0sesNxN5gbrJ0qqx8hDux2RbgkSPbRyWdODtWggCDVxYK2nS9wBlWq-ml0siktyzthXUnJPfcKCHwKqricugTgKC5kCUoax4jy3wOBTMHJlA1JrcdM8TjsFXhQzSCloqjl8D68Nc1ZT2R0nUOhNhyhHAJQqHXDEGai172HPvgM87IV1J8RY3uhir4JISSjWczGeLPVW-ZjNvRo4DJTC1Sl6CRret8rDtpbc7ZhqaXXHvTH_BUT85qv1SszQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
خط هافبک منچستریونایتد تو این فصل پرمیرلیگ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/104055" target="_blank">📅 17:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104054">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3846d0c4b.mp4?token=hIQ-cMHrEeWUl0jASesdHuhJYkuAgjrqmRry-_KM3xMKXDFJJc6hAv9afwQVVw84wfT5pPKxV5Ni-SF3Iq02PGaG5-3yhtIxf8Cuqv0YV51reYZRMQbAE8-JYA2nLHKlBqSmpAAno0GtOQ44Ouyqcydk8-Lg_YV16JTZMFq4QL8KPFsqXevAG1Cgfm0BZtgkJR5ECWP6lIdRZCQBBs3RymZj9SRk9p84josi1tOtRuuEGZSSPowOFm6xTvzMc3tB86MR8zNtD3kbvUYQ9wDvsIfMQkV4lOW4dnO-HQa0momiSBsqGDJkKZ96Qf1U0L1-kfMQKTPevx200C3pRokQcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3846d0c4b.mp4?token=hIQ-cMHrEeWUl0jASesdHuhJYkuAgjrqmRry-_KM3xMKXDFJJc6hAv9afwQVVw84wfT5pPKxV5Ni-SF3Iq02PGaG5-3yhtIxf8Cuqv0YV51reYZRMQbAE8-JYA2nLHKlBqSmpAAno0GtOQ44Ouyqcydk8-Lg_YV16JTZMFq4QL8KPFsqXevAG1Cgfm0BZtgkJR5ECWP6lIdRZCQBBs3RymZj9SRk9p84josi1tOtRuuEGZSSPowOFm6xTvzMc3tB86MR8zNtD3kbvUYQ9wDvsIfMQkV4lOW4dnO-HQa0momiSBsqGDJkKZ96Qf1U0L1-kfMQKTPevx200C3pRokQcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه یارویی علی‌آقا دایی رو گیر آورده شعبده‌بازی انجام بده که اسطوره به تخمشن نیست
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/104054" target="_blank">📅 16:44 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104053">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EqOvGCoDNXIpii9hAkK06VIfBAn-KDKTP2Jev_JBJmyuthEWzqMFKmnfhcNQ9LT_SRM6Dj_5HqL3rNX10ZF9OJOmYkZH2_ahqOoyNWI_TNAmGKPBQbos5dVPkA3JUkDfg6F2UIHse4knN6O7u_x5W83apHxhp46jk2EK4L-_g1QjQAIiTbh9Mp9OF4dPmA6h0Fxi2svQbvCG8T6qzOb0KP7cm1WUFqDFhKkZlupMCegDR3fcSI5LbKNeAE0PAORGdYDqbUuHKP7ExJ51Yhzeq7BnOHUqO1ntEGz8E-vLB9pd3qzNANfpU4y6hA49M5TXCfoktQWXjdijXxlYR_in2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
نرخ های جدید کارمزد خدمات بانکی برای سال ۱۴۰۵
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/104053" target="_blank">📅 16:44 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104052">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fcgJ4ZMWGtY0ijbGQVWvd4aiD5USLzt-W75oOlPt3W14hKI41QVtd2yq_i-EKGPTkTgT0W-VXZODuO4qjcg2uyBFTvj5Evc0KyUxQF0Cezo0cCi7SGNvPypbmqDed74IHENwHAbbD23hEce3HXfKI86OrGfziAvckOUgFO6AEEVVPw89llb6DEjoUtYeEcVedzUYphxMk5qFJ6KPmNlR9j8CzxopUyKc1jL4oPdHoO0URttfdxLq8CsF047aZl03sfoYP6qmHgLY14XiQL8qoVh3phoAepjLtCFiQiJ6spIBQi-OjGb8Blxjdqy0RpSsa04LGKgu_QtKd95iWftlOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
هفته دوم لیگ برتر ایران
🔴
نساجی
🆚
استقلال
🔵
🗓
ساعت ۱۹:۱۵
🔴
انواع آپشن پیش‌بینی برای این بازی
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۱۰۰٪ بونوس رایگان اولین واریز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔵
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/104052" target="_blank">📅 16:44 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104051">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/426246250e.mp4?token=KayD5JcNXMZmvZnTiS5MSHsl8RtDVN-Nb1nGhXksZp65jfoSWAgO0gGGKd6d6pzxA7SOkSq2YjUTSRbii60YMufHkxRvGKi80WuvQ-LVoSKI0Z0--DdlD-sduDUWzUpNzufn59dRXTMuNDlcgmEUZ4v_5km0v1eEBb0ycYVoLO99E5zVidVDxZF8ggrutoeTO7_b6CNjOnowTJahUaY7BV6PYzAKy-g1k5d-ZnvulA1sUXTd7mrk9T64C6saW3r7UQyFakD2kQlq1DfScH3J4WfnLYT1EpheSgICIREAX4frUF7l-4Vcspm16zz_UztOsaenOg9Niy-xAfWVhZmBcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/426246250e.mp4?token=KayD5JcNXMZmvZnTiS5MSHsl8RtDVN-Nb1nGhXksZp65jfoSWAgO0gGGKd6d6pzxA7SOkSq2YjUTSRbii60YMufHkxRvGKi80WuvQ-LVoSKI0Z0--DdlD-sduDUWzUpNzufn59dRXTMuNDlcgmEUZ4v_5km0v1eEBb0ycYVoLO99E5zVidVDxZF8ggrutoeTO7_b6CNjOnowTJahUaY7BV6PYzAKy-g1k5d-ZnvulA1sUXTd7mrk9T64C6saW3r7UQyFakD2kQlq1DfScH3J4WfnLYT1EpheSgICIREAX4frUF7l-4Vcspm16zz_UztOsaenOg9Niy-xAfWVhZmBcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
😞
استقلالیا وقتی صحبت از نساجی میشه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/104051" target="_blank">📅 16:31 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104050">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28f2dfd54d.mp4?token=oXVS-X-jHjm0lKC8AhjBEfhjZiShAwW-FZ0CGlbC4Z_Zenq2CmygbxUodP9o1FTdOoXpkaLVv_BTwVEr2x0zJOubj_AG_oJch25arWq9EmxaEMgAxBN0tZhkE4dH7qV1WqbUXiWAB2Azym7Sg-kg5xdBzgs-R7m33xae1pWd5JiGnV9atZweoAWKMVIZ9WnBdewSOVdpJawIgK4mBIZkWYb95A4hpDjINyKFHMH5UMcGvQ4Kiz8TZWlI-HOUJUJMQChRoCEs7hQ_vNY-OCpW1V2HsDNdyeGq3HDwTGbvsu8LeJOZEhCTQKWaE1nIHKLV9xu2yhl6uibrfo3CDvEUhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28f2dfd54d.mp4?token=oXVS-X-jHjm0lKC8AhjBEfhjZiShAwW-FZ0CGlbC4Z_Zenq2CmygbxUodP9o1FTdOoXpkaLVv_BTwVEr2x0zJOubj_AG_oJch25arWq9EmxaEMgAxBN0tZhkE4dH7qV1WqbUXiWAB2Azym7Sg-kg5xdBzgs-R7m33xae1pWd5JiGnV9atZweoAWKMVIZ9WnBdewSOVdpJawIgK4mBIZkWYb95A4hpDjINyKFHMH5UMcGvQ4Kiz8TZWlI-HOUJUJMQChRoCEs7hQ_vNY-OCpW1V2HsDNdyeGq3HDwTGbvsu8LeJOZEhCTQKWaE1nIHKLV9xu2yhl6uibrfo3CDvEUhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💔
وقتی میگن رفاقتا بو شاش گرفته:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/104050" target="_blank">📅 16:05 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104049">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea98bda8c8.mp4?token=G3m1Ato5HsdvZAN4SFe_-AsRmEZTfYL3mLDw8T6tRriARmCKhnN9LswzJ1EYOVMiOuEtJ5lkJut02lFVAlyWW-m8URve-yrF_ihSIDujEDwg_2fb1ixpLiYiUw-ZtkylEV3DO2FboRX4GkTj5UpzajJ378-rn54LsAFcpyBVs2zBqW6WUByvdqF_6iLvk4rkHXd1_NYHnEmjXyFXSabxUhkjvY_HRHMowP4Ea3TCicut9zyzFqOB4H4PSmMGdZRwQZKkHbIfZfQa7xgSgnCTrvZlst7uRDu7UERVBbsiA8HybbctBgjd2-iz9bfCt9PMAGbeFvOryfHWcpJy4LuhqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea98bda8c8.mp4?token=G3m1Ato5HsdvZAN4SFe_-AsRmEZTfYL3mLDw8T6tRriARmCKhnN9LswzJ1EYOVMiOuEtJ5lkJut02lFVAlyWW-m8URve-yrF_ihSIDujEDwg_2fb1ixpLiYiUw-ZtkylEV3DO2FboRX4GkTj5UpzajJ378-rn54LsAFcpyBVs2zBqW6WUByvdqF_6iLvk4rkHXd1_NYHnEmjXyFXSabxUhkjvY_HRHMowP4Ea3TCicut9zyzFqOB4H4PSmMGdZRwQZKkHbIfZfQa7xgSgnCTrvZlst7uRDu7UERVBbsiA8HybbctBgjd2-iz9bfCt9PMAGbeFvOryfHWcpJy4LuhqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😢
😢
وقتی رامین‌رضاییان از اساتید و اساطیر تری‌سام برای مردم مظلوم‌نمایی میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/104049" target="_blank">📅 15:40 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104048">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0df89bd7ee.mp4?token=YBWT3K75yo9LTKDg_3mp-NinNszP8gO-X4hvl6IJiTZJaMSv9tGYoIETa8Lff9H4AnfZDI68ze-PAxRe9hxabnWvqp5OGWZwo-eCtGiy654IiX0sy7CikYL_N0cCksmA_hWJQ7WfDoAR9N1bAuGcZlFeJYAJzUz_oxYE0-peflEFVHEmaH0b0c-lJCrvyUnBLfpUr4_3QHXyO_sxfSr0v2Ff9W_rVVBjU6Z3RjIDTwveN4h7HAXBBQ-KpLSDRwFnCvg4NQie1U1I9iWk4oPSFCVXljHo0nj6wCibOtYmf-ciXhFI_FEr7g7-dvrFuuRajp3hp0JFdytYLUsHvJeHxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0df89bd7ee.mp4?token=YBWT3K75yo9LTKDg_3mp-NinNszP8gO-X4hvl6IJiTZJaMSv9tGYoIETa8Lff9H4AnfZDI68ze-PAxRe9hxabnWvqp5OGWZwo-eCtGiy654IiX0sy7CikYL_N0cCksmA_hWJQ7WfDoAR9N1bAuGcZlFeJYAJzUz_oxYE0-peflEFVHEmaH0b0c-lJCrvyUnBLfpUr4_3QHXyO_sxfSr0v2Ff9W_rVVBjU6Z3RjIDTwveN4h7HAXBBQ-KpLSDRwFnCvg4NQie1U1I9iWk4oPSFCVXljHo0nj6wCibOtYmf-ciXhFI_FEr7g7-dvrFuuRajp3hp0JFdytYLUsHvJeHxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❗️
وقتی هومن افاضلی دستیار قلعه‌نویی اندازه گاو نمی‌فهمه و معتقده از روی شخصیت اینفانتینو قبل جام‌جهانی فهمیده که ایران با دست‌ پشت‌پرده از جام‌جهانی حذف میشه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/104048" target="_blank">📅 15:15 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104047">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/785fe1cdc7.mp4?token=masZTDVuxz7fAjkmYY_c-drzkNz6TCQAAbkNQ3_MAoH474-dxQUw2GEzlhOpBjg2mAKNj2pMjGArnmjszzFYBmsPjTF9FhIIBQVQ2ganr3DHS2tfiNaTPGoArVt7-lulzfCoRL8aZpKYlbS1OeohVFsan7jtKD3H7W1DQoXWOISoAdPCGCvyF3x2ka-olnsisCzqZSUh5NzJR326KBWirrtE1AbulkkpHC25mPLuJdR0HmAEkiUl10WW_YZ7FGoUHeK2M0uUkRpNCEOVewdIlQCBYe_EevaS5QcnePdlaLW9e-LGlNUAaPB403bNbjeMGBiLW4wWT5BbZ_NgrHEPhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/785fe1cdc7.mp4?token=masZTDVuxz7fAjkmYY_c-drzkNz6TCQAAbkNQ3_MAoH474-dxQUw2GEzlhOpBjg2mAKNj2pMjGArnmjszzFYBmsPjTF9FhIIBQVQ2ganr3DHS2tfiNaTPGoArVt7-lulzfCoRL8aZpKYlbS1OeohVFsan7jtKD3H7W1DQoXWOISoAdPCGCvyF3x2ka-olnsisCzqZSUh5NzJR326KBWirrtE1AbulkkpHC25mPLuJdR0HmAEkiUl10WW_YZ7FGoUHeK2M0uUkRpNCEOVewdIlQCBYe_EevaS5QcnePdlaLW9e-LGlNUAaPB403bNbjeMGBiLW4wWT5BbZ_NgrHEPhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
⚠️
جنوب ایران فدای جنوب لبنان؛ اینو یادتون باشه بعدا قراره به کارمون بیاد!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/104047" target="_blank">📅 14:50 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104046">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oHahc2KSKEXdd47xLe5Clh5iNe2NN8u6NmAOwMFWJWRim4bhTtP8DJ-vMGkvcxpNfwALS_SPwAWR5FZQsuj0fUQwGeffcgfI0lGyuWS5VM0c8-6je_XOdlW2upAddsZEUk_jvhbsZlanc6J_rqCRThNsX5FKTmSiE9kcdu6enAaJZKIefiJXurmqIWBU59L06jJzLUPf8ImVgVP95LmtQ80RL08fhc0ROoNclikMBAiDISZm6juzeUHJgLmujrg7UNWHEtiCpXm8LkcHmmCBACPFI4dUrWnGaaxwcjDnw5or2kJFFD0n2TuwjUip2JBxVYR61RMnfbMnYZY66-I7Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه هزینه سه خرید جدید خط‌حمله تیم فوتبال پاری‌سن‌ژرمن و دیومانده در رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/104046" target="_blank">📅 14:25 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104045">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c1ac47d0e.mp4?token=X6kWoC2dDD8Bv62b6SpBFOjK9hV53sr2GIblZfh6yYNlSl2ce0ZJIMhL9HtPmkIaM4tFCjYtv_idVUwr9oz0FvCIW-myH2-EfBcuilgFT3wz5vTRjlX2ZscmojF_ouZqnBCt7uhohH_sZIEC5bCNiX0sC-d5I-apEghHAYJIhh4NtfK6gx6R8LNOFC2VVgaOxGD3HZNH9ID43XkciIyjjr-uov3Vi5fDCUtQp46q1BQ2aaFWC-U3LlQEuGFYQXymCTJA_zAwT5SDdPQtccLG7vG0fexeJPRu1I8llN9-rZaxVArcKdxZv0r5tBrHUlmjoyLUHtwt86EQKv-g46E7aA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c1ac47d0e.mp4?token=X6kWoC2dDD8Bv62b6SpBFOjK9hV53sr2GIblZfh6yYNlSl2ce0ZJIMhL9HtPmkIaM4tFCjYtv_idVUwr9oz0FvCIW-myH2-EfBcuilgFT3wz5vTRjlX2ZscmojF_ouZqnBCt7uhohH_sZIEC5bCNiX0sC-d5I-apEghHAYJIhh4NtfK6gx6R8LNOFC2VVgaOxGD3HZNH9ID43XkciIyjjr-uov3Vi5fDCUtQp46q1BQ2aaFWC-U3LlQEuGFYQXymCTJA_zAwT5SDdPQtccLG7vG0fexeJPRu1I8llN9-rZaxVArcKdxZv0r5tBrHUlmjoyLUHtwt86EQKv-g46E7aA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
خداداد عزیزی: ما همیشه تو فوتبال ترسوییم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/104045" target="_blank">📅 14:01 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104044">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EX4_F7Np8uWF6QvdRyZQr4LOvUosaLakUi0UfjyN5y4caVuQiMo4kSpYcPLPoypelIOz0nWU5D6ZrYr6QtP1X6b2kJ2LvxlcEZXhhPGpe_ANRp-9_UjXeTT_5JFMy_ZmqdeC0AcTqiWfGDxByd92W1rUKI-qd5r_B-zlRTaycc9nkchPoZDDFLKwZBuBOwf2slOikPx9YM8OetABJnLJ9MuxHTvmNP2YAP1_TAcyKY9A2y7Uk6hD_-FoQu94FEtJNkAlnitl_MW7vhRAUxFEPforKF5KtRWRdn0iURdnQJLdBCcHZ6v3sG8mAfju3P38wMCKJxTHtxClAS_P2IHSzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
خولیان آلوارز
🚨
🚨
🚨
🇪🇸
🎙
دیه‌گو سیمئونه:  من می‌خواهم تیمی را دور خولیان بسازم تا بتوانیم از تمام توانایی‌های او به بهترین شکل استفاده کنیم.‌ حرفی بیشتر از این ندارم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/104044" target="_blank">📅 13:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104043">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y0mXVuwGBrNw3gLywLhWpdXrSfz078bibm1udlAmevXkCck8fS8-CPfNphMAwm5FUXluR7j1d2mgm7VfsvT-yDu_NNhb4tO-7DRF1ah2HSKxJ6o8UKoz47QE_WtWEtKQtNfsNoUtTPf0DzMEhZ5PuiE79UAquhhqMpNN5Ny23j3hy9LMCSy-xY_oNss_f2r9EEL88_VhKQ9vRjPt3INQR_p-gpJF2VLibk4l9vwcy-ejHy51tDk5l42Bcx1gORY6IP3fA0uqnKh4o4bjH5bxP5Y5b-rZk64WSq4PyewC6_suAJpo6lcoJEWk1RCiMzOeWs461wtsQRkIdq5RPvNPWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😍
🇮🇷
استوری خداحافظی رامین‌رضاییان خطاب به هواداران باشگاه استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/104043" target="_blank">📅 13:46 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104042">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">⁉️
خولیان آلوارز
🚨
🚨
🚨
🇪🇸
🎙
دیه‌گو سیمئونه:
من می‌خواهم تیمی را دور خولیان بسازم تا بتوانیم از تمام توانایی‌های او به بهترین شکل استفاده کنیم.‌ حرفی بیشتر از این ندارم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/104042" target="_blank">📅 13:42 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104041">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/buQiZCPdJUT0v8WphYNqVMsSk-ArNqn9wLdsT_29tyuocjq3lYqJLFaE0NgdcLkE7VOleBVuA8YyGAH8FRVGDU8ukEKx6WsVf5cQhyy3vGpE4iT-S7Rb2JQTXuOCKDWdvddcKQe7K2edEFECIL54TfyOikstqrfXvmL2HddSWerAfzKKHLN29wWt-7d8s2aHJ1Y_8ASjn8s_hrYfZHvEUpnPytOGPVTVmMos9x1RAJzdu2cIO8VfeEFiNASU3eEAKVeWYzs4SBVRHp3XAqp9Tp4QEejBZKUt8qVU4eFkyH6qLJwnaVDjLdumXF0sE_vYD6DOFffg9Vi6TOsWag8Fgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⚽️
#فوووووری
؛ برونو فرناندز پیشنهاد تمدید قرارداد با منچستریونایتد را رد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/104041" target="_blank">📅 13:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104040">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/339d8cb9ce.mp4?token=nKrqdq_mAhLayR4pVR2FIbDZDKUhDS-OQ2YWa69sN7-2dZF6VxKzzX57B6UBeqzg1V-ZNI1d7zYeqL5xzNcPl3X-oo5xISMAJjWwNkK92znHgOr_hBE5tta4OacrUAsoNTN3MieUu7YXSM-JpLbFFI5Lx86eGAgeBzeATWtchK_CG9RNWp43StU2UxJDYiodJXBHlmbRZtc4t9VOpQf4_o9IrkkLtowA8M6RiAffL6SAUlzJ5jq8DLd-VCGvS3VSkzMGNT9pY-6OEWb7tHaHJ5_Qwt7kStxrGZUGLlxgoQcT5ifl2-4r4aGZPujqKhIRWGy4keKdwCegaDmp0Hc9anO-_WvLht-NxqpIxUiiIvv-9YbVtmuDqD4eMaST_HOQTggw3uyVB5cUs3tkUG28IeTeEQNwlHBm6w4qM30Gi4kiMNP_q7VPmca0mNEbcp4zqLkFk7oqAxryqwQsV3Bt8_Dr5UTnA4Hb7NG_Xl1D5wia7qUq5puG9EzJhdHBHotUYa-_Ux-90YrEHKorWYraBOIVrrFzy7SQlM1kWmTkF5OCq-4V6uCpn-99AFxzB1uc3YYof5tcfzFp-TXbZ2fUJByP5CGO0rRltN7gvygp92-MB5G_voWo1h7VTnFNq79N7QM_IRkR00LtD5yjfnA30PyzZA2IJbqeb_AP-ysJbRM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/339d8cb9ce.mp4?token=nKrqdq_mAhLayR4pVR2FIbDZDKUhDS-OQ2YWa69sN7-2dZF6VxKzzX57B6UBeqzg1V-ZNI1d7zYeqL5xzNcPl3X-oo5xISMAJjWwNkK92znHgOr_hBE5tta4OacrUAsoNTN3MieUu7YXSM-JpLbFFI5Lx86eGAgeBzeATWtchK_CG9RNWp43StU2UxJDYiodJXBHlmbRZtc4t9VOpQf4_o9IrkkLtowA8M6RiAffL6SAUlzJ5jq8DLd-VCGvS3VSkzMGNT9pY-6OEWb7tHaHJ5_Qwt7kStxrGZUGLlxgoQcT5ifl2-4r4aGZPujqKhIRWGy4keKdwCegaDmp0Hc9anO-_WvLht-NxqpIxUiiIvv-9YbVtmuDqD4eMaST_HOQTggw3uyVB5cUs3tkUG28IeTeEQNwlHBm6w4qM30Gi4kiMNP_q7VPmca0mNEbcp4zqLkFk7oqAxryqwQsV3Bt8_Dr5UTnA4Hb7NG_Xl1D5wia7qUq5puG9EzJhdHBHotUYa-_Ux-90YrEHKorWYraBOIVrrFzy7SQlM1kWmTkF5OCq-4V6uCpn-99AFxzB1uc3YYof5tcfzFp-TXbZ2fUJByP5CGO0rRltN7gvygp92-MB5G_voWo1h7VTnFNq79N7QM_IRkR00LtD5yjfnA30PyzZA2IJbqeb_AP-ysJbRM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
👍
موزیک و برنامه‌ خاطره‌انگیز گزارش‌ورزشی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/104040" target="_blank">📅 13:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104039">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hpL2KCXZNy_FBKeq1d1kXiyBn-lRqkS5qVjWN9t-udVBFIWlFa3QF3urHYbf2Zg5EM632IGNApIQ9zpI00m0RoxyPEAw8hl2vT50uallKSWkm25tv54DmaknTSTKOzfFnVJgQGwDGI0sxvdOLlgXjNKXVXuFBy8UeU0rdb0bWKKV16INls8kGV_De6WZGpNd-gyEVqy73KwkNUAdNBeGa_yBiA1XufqoocARToRM6I3nPU4eMzGgV0LxtpZq6wZdGBuxvQMRB8276vGjI5ybtWFqjtCDg5x0PBYctJyMe-VMPfQoYq0rNYKyU1ZMudXwt-JB3I7EC444ONhUJxm6vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇮🇷
#رسمیییییی
؛ رامین‌رضاییان با عقد قراردادی یکساله به فولاد خوزستان پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/104039" target="_blank">📅 13:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104037">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o0tcSa17u4zJ2wytbSaJ1iK-slozNNGrXqhssMyd_RTTWulS3wLs_bQVBIWO31Jx-Pv5RaUIzSdAsC2-GdqvJ-9lQFMQbDB2wyC7-yzcPo1mOTrv4nqXjoI0fyxWf8AjugqL9hpgso8rMp-1IH-cR-xF1BnZGcRMv03StrVhNqwRPeh0px5P0_iykrDYe0WzOWTid3AxLf--RHONVe23Cc2Ic7MyuoP7arIZRh5VvJmbGCNXxMErQkkbOfhinyGhMlXEy-8CqfsY3yBszp4gazvkLrplzI4wQuPWZv4sXwvU7umOexDoWpkuUSmyvnpk8kMlVwv-3GgQB9jZuWAySA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iSzz4uhOcYAKIU6TtI5Ln7_02Xn6FNUiGDQaXJIu6OsHrYXOKBNugzvghnnLxUataj0mEdhlx34pSOipoW_pU5a_uW0jZrHZnSMaDHi6AWkahNzfPJ8_wiCVLTGBV_1PyHJjyJe3Wyb9QeV2Ie9N-DMZ2NwBHKvekgDPw-ay5ljRn2vwan5py1631zqzSSfF2RPf8Rd_HQq-2n9njF5k7cBeFABA6xKQgnKCmDlzz5NvX9M7LqhV0jw7T_N_E5-X_HHysrN61nmaVgvhw-A6jsrChgSbSB6ua0Cx7sd507Jm4ydv9B79ydWuiw3V9GRKcdEUxQr9DzPrLmw9z0ViFg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🔵
برنامه کامل بازی‌های ۳۲ تیم حاضر در مرحله گروهی لیگ‌نخبگان آسیا منطقه غرب و شرق
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/104037" target="_blank">📅 13:03 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104033">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V9ySHt5iQ_4cBfboUhGWFThpdqeGpZNaEVIWiUpi5Dzp-nmUw8gLtVI2tRl5-ND4z1lSkT2njT92mehVMYLPZ1nSa8dbo3cgJLJDZ-qIRFIQABBRj3pMViuXtt2a3dj6TABtNBrpiBd_U1pT5UEY4u6Mq43tJj2Qd6CmhYQ6QQYCamME32DYzOiHYeWtuyzEcqrI-_jU9YJd5yKO2SPJbyVIg-9IpJnGZbZzlgYsPllWD105BdqzqwEuEvZklhg32sS09go5mYN_gzN2DWLAZXGUUtkQHh3jkbCChwEnDuvcpCg0PMCsG3vewSkE5zNHKh6YNhAbEtHiLwW7Q4adtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oCKPFv5lC_uBlcfUd-FdiBW2ZJZ21gZnFvawv6WOYc5LlZf0MCorQ_eaJL-z8BOBoLSxLBxa5P_P_mzk_PlKgzgdXWo7cepCFGPyB3gZmxaPU1JN9KLGZlq-2EJtrY6ehs3_O77GWIP6TlbFBAvknUQVon5EYNOE-dy_U8YfDw3j0lDTp-7x4BnNlY1NnyaBv8VyFELI4K9AJtWSWUVklvPJ8DICF0u2NlJJlMFZizXN8A-cUAwasqVzmgbcRMKZPAoBOl2tIYbtgx3vnV4SC3P4gtzog-3s9hVjvk-2FA1KcjsSLnd5waqiGrNC54My6OxDq1-r7OYF7vhIEz_Wfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qiZoH6OK6WVGdGjI0NP-d6A0-pV1eInSc9JRuodc0dh-W21fig1OzPxI0ZzpNk_PfSbCuLEmR6Xp_F8kivRhNT6xvt_XpXv3_i1AXd0DMFyKE2jfjmm6Ur_ZO9ZVLqAQLhJ9uY89EXVrza1Jx1d2yg_aMoqKraPcE8T7uTHS7BxCtVBn5d1efuVfq2yYH0m9O1IYKZPUwYkSiUgjtY1g_mNDUk4ogsZuQ6iKxlsqtysZQZTUPV5APMLtndunB0NvvQFHYNFzwWMPNlvBB6YJKfLhg6MElFX5HHa0_fP0_LuVN6unonSa3Jr1DRohkUrI-QoUYpS5SJBYtS0fd5TP5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sMhzDDZAd5P_QBjsut4WFyuBREEqrDqngcexfMnE7e0VgqrysJCZ099G4nbhK1LWwlxwT7JWXMA4Pfd0o2NfvPgVMVRBbyhJkEgSiSoNTIQX9KT0_bCRyfsHHbuzDAK3Ezy3IpZ8nA_Dnf4_BeGsK3H9n2BcCRgD-N6fvDJzdUTjWIXWP40piRGtygKRVwsVRzxUTBQMrYOaix7kpKZxKVX_6GPLng_hUsfOSXnBBjQjB6ViRfWzZ030uTgNDnsaRIInFUNkxKUVRjuk5K40zbOvL9ak9J149JOyPGBDcpupWAD6gjzs-S2qTlgHujRId-Mwoeuo9NlqYALOQSmtdg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
🔵
رقبای تیم‌های عربستانی در نخبگان آسیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/104033" target="_blank">📅 12:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104032">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8832387bf0.mp4?token=GnSJOo_52oPgPZIm3NgSNfrZEGMhRNqBNKZy-xoNWZuDHW3bgGasMI84AVg5X1dMlx0lS8bBYO7N8_8Ko98Oaq8tINtulIz8SFqfFrnfo1vujYtzdIFRtEtgCTE6RSDPo8p7SsPeW24sbkBopluI86lEX-j7oD5k93HCOvL31sOlYF6oRk2Z1vDyz1ttPG3NPxBa1izIHHRCQgleBdkj6pDYNOECCSt4RA2mA-2ciOYXP9lJm4VBsoV5HYRVe4KdB4NgSknuvIvP6oCln2oxwYc-PqXbbXQ5D9c_eWeNiN7L0RNA_Xz_w8izpwfgw0D-VC_VRAdcQR5gg3uPSS74OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8832387bf0.mp4?token=GnSJOo_52oPgPZIm3NgSNfrZEGMhRNqBNKZy-xoNWZuDHW3bgGasMI84AVg5X1dMlx0lS8bBYO7N8_8Ko98Oaq8tINtulIz8SFqfFrnfo1vujYtzdIFRtEtgCTE6RSDPo8p7SsPeW24sbkBopluI86lEX-j7oD5k93HCOvL31sOlYF6oRk2Z1vDyz1ttPG3NPxBa1izIHHRCQgleBdkj6pDYNOECCSt4RA2mA-2ciOYXP9lJm4VBsoV5HYRVe4KdB4NgSknuvIvP6oCln2oxwYc-PqXbbXQ5D9c_eWeNiN7L0RNA_Xz_w8izpwfgw0D-VC_VRAdcQR5gg3uPSS74OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
واکنش تند رضا رشیدپور به صحبت‌های زشت و زننده نماینده‌مجلس درباره مهسا امینی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/104032" target="_blank">📅 12:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104031">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UBImMKjLuPA6IqvZXpJVkZzUscuiIVm2c0_QEJAck-_UKlhK9Vy5Fu4BxRiZxrD4RHn2DHhcgEboLoZeW_ygKZZMT5DB-b_pNA75IVqUDa5TIbBur9xufsWhMSQtespFdvIoRQPvOqtWEULu5JELkhuzBD896o6irGpfWiPFLcuiD-KGc6qbX_G5eONin7YcXkTXkoaVrOUTS9BD6PbStW1_u_uHHhUTNi0jMyNsoSly9slDn89UJflkpec35--eohSjRIwWa9J9d_XVUjE_ZwzmpYTtAu7sECqsJ5dyEovNStWQs0Lau1-r3y_WlkYM6Y3DhYnUf5wbJwOtAAVTYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
تاریخ برگزاری مسابقات لیگ‌نخبگان
🟣
هفته اول:  ۲۳ و ۲۴ شهریور ۱۴۰۵
🟣
هفته دوم:  ۱۹ و ۲۰ مهر ۱۴۰۵
🟣
هفته سوم:  ۴ و ۵ آبان ۱۴۰۵
🟣
هفته چهارم:  ۱۱ و ۱۲ آبان ۱۴۰۵
🟣
هفته پنجم:  ۲ و ۳ آذر ۱۴۰۵
🟣
هفته ششم:  ۱۷ و ۱۸ آذر ۱۴۰۵
🟣
هفته هفتم:  ۱۹ و ۲۰ بهمن ۱۴۰۵
🟣
هفته هشتم:  ۲۶ و ۲۷ بهمن ۱۴۰۵
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/104031" target="_blank">📅 12:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104030">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WZ370_OhlmzToN8l3rdYTX7-O9mdM73co7VYBjvVvB7RctoGhNyALp0fsGea25BRoc7J2xBx5bl0NZfvvHVPo75w7dZqb7BdhmQumUChv2b-Fp8SMYGLxgDgqXFMU7DJIJjSof5itukq1Owj7ACBeXuY2AQZ4os2uE03c_prRC2HXCKBjIfv4a9h2zY_Cj4mcXnkuQrofowt_FvfC_ZR54JzpVavWTmIZ-zi9vAZxsRVzNpBN11RbQRwy8WC4MrCfN7LeFOuXQbsVwG3F9XPu9fYekUPU_j-AYc8oVFTifFGQ5GrPDBobcYaJkmnLYr-xpGTuYQG9m2Y7O405-UFlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔵
قرعه کشی لیگ نخبگان آسیا
🏅
حریفان استقلال: العین، السد، شباب‌الاهلی، نفتچی، الغرافه، الوصل، پاختاکور، الشمال
🏅
حریفان تراکتور: السد، العین، نفتچی، شباب‌الاهلی، الغرافه، الوصل، پاختاکور، الشمال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/104030" target="_blank">📅 12:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104029">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔵
قرعه کشی لیگ نخبگان آسیا
🏅
حریفان استقلال: العین، السد، شباب‌الاهلی، نفتچی، الغرافه، الوصل، پاختاکور، الشمال
🏅
حریفان تراکتور: السد، العین، نفتچی، شباب‌الاهلی، الغرافه، الوصل، پاختاکور، الشمال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/104029" target="_blank">📅 11:58 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104028">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dru1NstaLBaZs-ER-R_Z5LER_-gPSKOJtyfEf6-IUNtzSgFWDUfIhDI509MqdC-Y0zQCnukY3xZn4cB0ac4wgTHCIfNNUOxmTxXPIVcCzXPRHpk4smSSCz3yQfEeSTbf3MZRQ4EU-86xWjPbVrtsxG1UiYtn48Qodf-nMXwizAy2RKBycKC149U4kNtccrqKvAt7K_TfMf2XHnGenqzliuhOnsmNQ0I2JAGIMvn5CnKZbHgvq5Z758ge6yz7jOrZTZYUEQ9GT-QcqBV48WcJB25qCwvJ46rb0fCV-hBM4pxf6Nwmg84VL0lvMu8wizZS4lR9bD44xCwM-D2wUZGPaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔵
قرعه کشی لیگ نخبگان آسیا
🏅
حریفان استقلال: العین، السد، شباب‌الاهلی، نفتچی، الغرافه، الوصل، پاختاکور، الشمال
🏅
حریفان تراکتور: السد، العین، نفتچی، شباب‌الاهلی، الغرافه، الوصل، پاختاکور، الشمال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/104028" target="_blank">📅 11:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104027">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🔵
▶️
مراسم قرعه‌کشی لیگ‌نخبگان آسیا آغاز شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/104027" target="_blank">📅 11:41 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104025">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GXZvFwS0ToV-VUMTOSXScBvIJkh4BeDtqTJvW-QTFhoykJYr_4ZuRgQAK17fLWWyWdjjhWutQwiJUG37wAbRrRVHBqt9eRpAaLgsg7lev17RNXkF4ev421PshldW8akaVcNL7uyk2ZT9s94j4YfuHSw2jkE47ca5rY1VustZqvM6kmdqveWgyxrtUcDfvcOYwG02N0Sasi6HqbOUCs-brcc7wjhPeK4O7SrQ-1MJqRinLgoJ6xT3UrSRA7G5Goo3fsTVlDwDKHmJrLp3pNazH69LbJ0s0Q-TfRr6rH_-mEwapHRTNg-HKWxmkCgpHmh7nfkIOiiXmdfZSrhC4UL-9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BHM__XKVoQ6rCsT0PxK13m5RgXe-mnMoqNqRQ8Fcl_-IU6ueewXyUG_xrzAPifBDpil92hpJS55oFLeeSRm7Gcdls9xg-HOgvnWj-J4YidSHIfJl8YWuDToOPL5Nu-8JaMh3cK45dx7vd_zQBGBqnUOFPNOn9AOr9QVC-a2sNhEIU83stRqZsg3oylc4bH5DVp-Omxm_aU-PzqyF-xJ0ykGEhCRJRgaqSlxStCz7DZ5djjhm8QwbvNWHnPwBV0_WbRf5z1XZ4GydxAK5Of0_SkagLIg5wsu_mi5CK9Y1BrfALy7gVfjEXY9rXXdj082d2eA927gHjDvYSg76uuxYoA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
حضور نمایندگان استقلال و تراکتور در محل برگزاری قرعه‌کشی لیگ‌نخبگان آسیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/104025" target="_blank">📅 11:39 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104024">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d388dcd36.mp4?token=DjhhdAGii-tHsU5iOQzj-3x_4c9zDZd_VlAZjcmSaevdP08Xz0i_Iq4kJEfkzszU6eDV3mGTryofUknQdNZe9hvuu517Y0HqCur7Mt3lFj4wvbqdlM8N8D5gVCnylHh2v3LTCFuk4po0u2H1pNGK5Pw_2-WlX7J6GCOz7mnR15XzJK5yldRDOjO3J2wXe8GcUAhhkzs6uICxXM5qm0tc8U2FsIu3o8g2wQKZwIj7Jv78WB63Fi6V-R_iCV67yMcRnhNqXZ4Sw2X_NHYRzHRqP5lUUp1zRB05E6_JHC8MUUBR6-s0hSJcwffzryFEMNdK_IPNECQCkEeWN2Vup-nq57SdgUmL0eI2eJYv-K9KSu8nqlvYp9Se72Zwwqzx9yr8Nsw6MiKaIECkfUz4F0rVsqu19In2VeAUdBOT9uld3KpiLLPFFTb8UKji-k3_4CRPvmTvZ5Ud_q9CxENUeK0xWca2X639FooFqPECl9-_tGElCHOL3sLaP31j05ao3-anT2-796oHAT9cELzSTpms3nWmjCUsZtexZDEvmb4-ejMq_xlvcPGeojRINhoRaVTAcfC377VQVJr21HAaxUmYlJ2btqeT1jrb4yF6UKRx1Dd2_MA04-dl1qZ-sSNGXXxrB1bd2HsE82PvK8phsJeyysezaEXbP68M0HqwBvKJ43g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d388dcd36.mp4?token=DjhhdAGii-tHsU5iOQzj-3x_4c9zDZd_VlAZjcmSaevdP08Xz0i_Iq4kJEfkzszU6eDV3mGTryofUknQdNZe9hvuu517Y0HqCur7Mt3lFj4wvbqdlM8N8D5gVCnylHh2v3LTCFuk4po0u2H1pNGK5Pw_2-WlX7J6GCOz7mnR15XzJK5yldRDOjO3J2wXe8GcUAhhkzs6uICxXM5qm0tc8U2FsIu3o8g2wQKZwIj7Jv78WB63Fi6V-R_iCV67yMcRnhNqXZ4Sw2X_NHYRzHRqP5lUUp1zRB05E6_JHC8MUUBR6-s0hSJcwffzryFEMNdK_IPNECQCkEeWN2Vup-nq57SdgUmL0eI2eJYv-K9KSu8nqlvYp9Se72Zwwqzx9yr8Nsw6MiKaIECkfUz4F0rVsqu19In2VeAUdBOT9uld3KpiLLPFFTb8UKji-k3_4CRPvmTvZ5Ud_q9CxENUeK0xWca2X639FooFqPECl9-_tGElCHOL3sLaP31j05ao3-anT2-796oHAT9cELzSTpms3nWmjCUsZtexZDEvmb4-ejMq_xlvcPGeojRINhoRaVTAcfC377VQVJr21HAaxUmYlJ2btqeT1jrb4yF6UKRx1Dd2_MA04-dl1qZ-sSNGXXxrB1bd2HsE82PvK8phsJeyysezaEXbP68M0HqwBvKJ43g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
😐
حرف‌های عجیب سلطان خر ایران؛ ویدیوی باور نکردنی از نگه داری خر و خوابیدن کنارش در منزل!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/104024" target="_blank">📅 11:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104023">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JQ0IqvYfmYgUAAFf9j36b2o_cvfYTlCxBsopAAqR7LjhQqn58Y_kuUK94QVLbH_qKS9-fMHBo1fTlg-_tee9NFDZs_9c0oYx5za65LtSlwmjuuz0ou4ABntew9aNUmeyV5SVhEtNagTr6ELAbbxBzXYL4VXdec1NsdwqPYp2b7kXbwfLCeMWeEh-pFeYGXLKL8tJqA0UyJ9tIbeQHZcr-eOH_qZ1fUIc_0-FZpenJ62Hw32heKtVOGwINpry-ugPeKiUk0W0DaXAjb7pXrWowQSIj-eMGWUE3PdTnGtmKqCsI9HAbvbrECyY2XwKdbxYULTZazlIMVbhv_SWdw1tbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥶
⚽️
تفاوت آمادگی جسمانی فلوریان ویرتز قبل و‌ بعد‌ حضورش در لیورپول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/104023" target="_blank">📅 11:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104022">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/Futball180TV/104022" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">⚠️
#پیشنهاد_ویژه
⚠️
🔥
حتما ویدیو‌ آموزشی بالا رو‌ببینید بازی ساده و بسیار شیرینی که راحت میشه میشه ازش کلی پول درآورد
👌🏼
دنیای سرگرمی و بازی های جذاب رو در این‌اپلیکیشن تجربه کنید
⭐</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/104022" target="_blank">📅 11:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104021">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/936a75dbba.mp4?token=EaCTHjRkj1_qoc3uxsumit_MTAMaPliw0CYKDsJosHiMbLs0SZIjQvF_4X27sL1O4Ep0ddcIPkFWshNYZ1Yxg-XixmdKbaZJm6Tnacpu-JsnGH_vknfLk0nIqpivRB3SvcPCe1tlSouoPnidFeGpu24U0IPesCD7t6nRzkEkMG452U4mMQL4itEkAV0hEj_bIi31pB0RuSlNnWDThWTBhQJXBMMdposBzb3kjWLoUW6v9N0LTiXO3jrw7TY3pJvTgeGAIh5Qktg7M33im9Dk21zMcRDF-69IfzKx9GgBEU6uBx6y6F3VnCG0eLfuc1XqVuBIB_vBFJ3vR6doG2ckPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/936a75dbba.mp4?token=EaCTHjRkj1_qoc3uxsumit_MTAMaPliw0CYKDsJosHiMbLs0SZIjQvF_4X27sL1O4Ep0ddcIPkFWshNYZ1Yxg-XixmdKbaZJm6Tnacpu-JsnGH_vknfLk0nIqpivRB3SvcPCe1tlSouoPnidFeGpu24U0IPesCD7t6nRzkEkMG452U4mMQL4itEkAV0hEj_bIi31pB0RuSlNnWDThWTBhQJXBMMdposBzb3kjWLoUW6v9N0LTiXO3jrw7TY3pJvTgeGAIh5Qktg7M33im9Dk21zMcRDF-69IfzKx9GgBEU6uBx6y6F3VnCG0eLfuc1XqVuBIB_vBFJ3vR6doG2ckPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖱
به راحتی کسب درامد کن
💵
💰
🟢
ویدیو
#آموزش
بازی chicky choice رو براتون گذاشتم خیلی راحت و بدون ریسک و میتونی بازی کنی و کلی پول دربیاری
🔥
💖
حتما ویدیو رو تا انتها ببینید
😅
😂
😆
:
💻
betinja.bet
💻
betinja.bet
🌐
کانال بونوس های رایگان
r27
@betinjabet</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/104021" target="_blank">📅 11:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104020">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93a7cbf260.mp4?token=Wgs8VQr4GVvG54aK6tHzxjflUEc7MQscAtqnAD3OlCh4hWCG29YdptvDFAPP3hLus-U_gAqyRCdd2-_4AG6IsyJPYmcLZxfjFd9I6prcxvPuc_JgIW_TgjwITp1fEKen3AsQFQ4EuNKquU0MoWrdw6RyTaGBHftF_u1OGeh-3OEBr4fCCSwulD6pyj_fHnDzOfOkumX-C_Go6_x8fqcFNMqf0bvLOngpc9JX_A4NSFMxyhBE3xbcpS1OjZVEMb4ZmechBorYMeIp_5oCO5mR1wjaUwonaFJY9mTneAUUrm1ktmWmGE72rYHvjM1Ixiud3UywxfhP6rTM0SXpY46l5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93a7cbf260.mp4?token=Wgs8VQr4GVvG54aK6tHzxjflUEc7MQscAtqnAD3OlCh4hWCG29YdptvDFAPP3hLus-U_gAqyRCdd2-_4AG6IsyJPYmcLZxfjFd9I6prcxvPuc_JgIW_TgjwITp1fEKen3AsQFQ4EuNKquU0MoWrdw6RyTaGBHftF_u1OGeh-3OEBr4fCCSwulD6pyj_fHnDzOfOkumX-C_Go6_x8fqcFNMqf0bvLOngpc9JX_A4NSFMxyhBE3xbcpS1OjZVEMb4ZmechBorYMeIp_5oCO5mR1wjaUwonaFJY9mTneAUUrm1ktmWmGE72rYHvjM1Ixiud3UywxfhP6rTM0SXpY46l5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
وقتی مجتبی‌حسینی سرمربی نساجی به بازیکن تیمش قوانین داوری رو یاد میده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/104020" target="_blank">📅 11:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104019">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vwLHozMHjcB7Zjazmw_cngwrLf23SAG-cjLMNsoPFWRul6wHMzPR_twtu2FSD3fVRXVsxu5zans0pvkLRqDVyXWFuZQTuJiIjd06wuLH8HBtZbaxHXX4FTBdwa6fnn5EEGd6uLFJxwrwNpgeoQJ3lCiVSgMKr4GhMx5thJVk6tNjatRfRxLZuRnmmVLoXVOW0wlWfW0cBi0V7siKDLOmjfZzDWLe7BeHr2vQkyp9RnBXu9inMc0n1gY745uorHmR7nacmx81mBop967pW1PN26Hn_oB50GVP00cGxbv5A17dm_AjnwCc8X8bqpG-FtDZ0UzmttTrAlBJWyR6vX4PaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🚨
🚨
🚨
🇪🇸
جوتا جوردی :
🔻
آلوارز برای بارسا بازی خواهد کرد!
✅
بارسلونا از جذب خولیان آلوارز دست نمی‌کشه. آنها تا آخرین لحظه بازار نقل‌وانتقالات برای جذب او تلاش خواهند کرد. حتی اگر این انتقال تا آن زمان انجام نشود، ممکنه بارسا در ژانویه دوباره برای جذب او اقدام کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/104019" target="_blank">📅 10:49 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104018">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f82bbb56e.mp4?token=vrHbLVz4EYS8Gzi9QwddyMPuxqG8FrBVRe3S9PVW5tRgCGCsWMuDJVdp6ofpL4Il-9HVswo1B7nbPI7DbYinA4AbWaOGDwxSlaxYO93PLLS-RtrF7vSYcpefvEizG8nxzDLQKG6fDVUr0S-Wb9kLgfIY-BJ28VsP2ElmozBu_xdroeRW8tLc22SltqUVj9g_Hyj1DkV5qDfYksRCvks1mfW-Gz85hpYumGhbK6mYog2ob51GRwLUcuChgyhmWoWbQEQOwwFSUotfIwXgdBtlMk4gRljzJjBNiHu70qu94JiAi4E7ZS0UElF9tMcXdTaOxf7M4GlWLeQcsrQhfM8SKkSspDc3b7J33GGAIRjja71126VVkM5xFpvC-_nZStHDFCn6vCh4x0RkuuhR3WLCl__iwY_xjcrBd0tsVCr3nBwdnfuidA2z99FS2Hkle4Ctxq_cclPgZFSALJRE-WzAPNmTTHiGuKfs-6YTEZzbIOYe9-CZFshK6Gu4w0OPUQK3nTcYPBRp9Sw6eXdXW7qC9F2RamZK9qn5ZazW0IIijfaGfCRN_WarYwZijlORRrioWdGyEXpsLU_fHGTocnMttXvNPMslQFQVETqe9zirITEVY1X4n4aqltk0sciUNm6H27aJU26YJ7MDLiO_DgLH4sc_wKe6ewj6OO7lOr0aEn4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f82bbb56e.mp4?token=vrHbLVz4EYS8Gzi9QwddyMPuxqG8FrBVRe3S9PVW5tRgCGCsWMuDJVdp6ofpL4Il-9HVswo1B7nbPI7DbYinA4AbWaOGDwxSlaxYO93PLLS-RtrF7vSYcpefvEizG8nxzDLQKG6fDVUr0S-Wb9kLgfIY-BJ28VsP2ElmozBu_xdroeRW8tLc22SltqUVj9g_Hyj1DkV5qDfYksRCvks1mfW-Gz85hpYumGhbK6mYog2ob51GRwLUcuChgyhmWoWbQEQOwwFSUotfIwXgdBtlMk4gRljzJjBNiHu70qu94JiAi4E7ZS0UElF9tMcXdTaOxf7M4GlWLeQcsrQhfM8SKkSspDc3b7J33GGAIRjja71126VVkM5xFpvC-_nZStHDFCn6vCh4x0RkuuhR3WLCl__iwY_xjcrBd0tsVCr3nBwdnfuidA2z99FS2Hkle4Ctxq_cclPgZFSALJRE-WzAPNmTTHiGuKfs-6YTEZzbIOYe9-CZFshK6Gu4w0OPUQK3nTcYPBRp9Sw6eXdXW7qC9F2RamZK9qn5ZazW0IIijfaGfCRN_WarYwZijlORRrioWdGyEXpsLU_fHGTocnMttXvNPMslQFQVETqe9zirITEVY1X4n4aqltk0sciUNm6H27aJU26YJ7MDLiO_DgLH4sc_wKe6ewj6OO7lOr0aEn4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🙂
ویدیویی در شبکه‌های اجتماعی منتشر شده که مرد سالخورده‌ای ایرانی را نشان می‌دهد که سه سال است هدف حملات پیاپی یک کلاغ است. او می‌گوید ماجرا از روزی شروع شد که جوجه‌کلاغی افتاده را نجات داد؛ از آن زمان کلاغ به محض دیدن او به سر و صورتش حمله می‌کند. حتی با پوشاندن صورت، او در امان نیست و کلاغ به افراد شبیه به او نیز حمله می‌کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/104018" target="_blank">📅 10:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104017">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/STdwBvMdQaZa1jCZBWu8hFHsb5My-l1L9z09oMnCUYSVmlw7pSbULPuNaTvWzXkx1mHQuDrohmpD99edpVEs8yD_3qpMSojUpiJROlxhiaxX-yuEkHJOJKednusIYjbeSzSnEgwFgTrR2D7td-BZDvpi9mnUJdcbN0tOp_EW3PoNCnYMKjjryb0F65qdBFjEkvdY4Bbj-iY6onQqw9SxTGeDvQA0r4BBp02Zq4Evi8MvP1oV_VJaHOxxFGhsRl3Vw0lmvfWtQs8Vqo-J_aQwYDYErzPCrNw0Ppt_rVSqtydP9Ymh9uLrEmS1PemqROF5iAhI1e5OLg4vKBDEm5oq2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇪🇸
تکمیل ۴ خرید از ۶ خرید احتمالی بارسلونا در فصل نقل‌وانتقالات؛ رویای کاتالان‌ها تکمیل میشه؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/104017" target="_blank">📅 10:20 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104016">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RxDWSTMEiYjPjW8kTHkjWB8KyqOy98D2NGxUIOWoZdXBIlVWIEn9PySNmX86NaYLCzIS0bFo6BJPVkyMtfYPl7qkV3mzQa_QMX-hzICHX-uC73jgMSGbiFP4d-hpjZMo_FsscTpuGUDlUEsuSIuBS6S_b-zUf5u8IAb7uFFY9mgqKPqcvLOu-DTYpgZjuu1_hjwWe__sPx68do_w_pS7oRbj0WpsT7FG9u1o0p6RjSChqt2-Yi-8SYd5m_Ex6Q3q83cKb8AL8aBiXU48zK62bcKzDi51L5xrfq_tmnB--dQ01GNH09ewG0U66IdwyUC9Ovfyt1lH0_ygSfQShfGKWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
✅
🔵
نتایج قرعه‌کشی دور گروهی لیگ‌قهرمانان آسیا؛ گلگهر در گروه  B قرار گرفت
🔴
گروه A: الوحده امارات، نسف ازبکستان، الکویت کویت و الخادلیه بحرین
🔴
گروه B: الجزیره امارات، گل‌گهر ایران، المحرق بحرین و آرکاداغ ترکمنستان
🔴
گروه C: التعاون عربستان، الریان قطر، الفیصلی اردن و النهضه عمان
🔴
گروه D: الحسین اردن، الشرطه عراق، السیب عمان و بنگال شرقی هند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/104016" target="_blank">📅 10:03 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104015">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bade9483c.mp4?token=frrqveSIAXo-L8s6sthIdc4mVMhfGabUy9xMB0MAyTutR7FENVipyjHe5ZpgdBo8k-2PNEiKh1u2xXPnLhfMVyGnz3O9xl8Hh69mlgT6cNCD7dMOpKSyoH1K3iaDOMCoI81A_1qMMsdntxYUOa7JoDkzOIOO_DFnIZBvgwdbXiD08J2SqDR9YRe5gM_NTUHf371J65kx-OpUbLOGnr1e1IKQ3B15-OPeJUkvkiNuXc4mHXvXoybf8omkuGrIiL9swnIB-7bU2bi7dNEehxIOWSpm_nDHm89sCTaQP335hre2asUWpItjRpdIJAtBCWx9Eu53fyg7XoUPfELQcspSYTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bade9483c.mp4?token=frrqveSIAXo-L8s6sthIdc4mVMhfGabUy9xMB0MAyTutR7FENVipyjHe5ZpgdBo8k-2PNEiKh1u2xXPnLhfMVyGnz3O9xl8Hh69mlgT6cNCD7dMOpKSyoH1K3iaDOMCoI81A_1qMMsdntxYUOa7JoDkzOIOO_DFnIZBvgwdbXiD08J2SqDR9YRe5gM_NTUHf371J65kx-OpUbLOGnr1e1IKQ3B15-OPeJUkvkiNuXc4mHXvXoybf8omkuGrIiL9swnIB-7bU2bi7dNEehxIOWSpm_nDHm89sCTaQP335hre2asUWpItjRpdIJAtBCWx9Eu53fyg7XoUPfELQcspSYTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇪🇸
نقل‌وانتقالات بارسلونا در یک‌دقیقه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/104015" target="_blank">📅 09:50 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104014">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b1d68db4d.mp4?token=q7fiYjDJpgPYBTmwu02L2rG4dA4cMN6sU0nJyN4fuUGfIo9DjNfOdv2BaFyH132kq9Pj-SqROhbLJWBFIJDatAIy_sOb6xqhIphuFjWYhzaVicG7GlphJMeUl8c4rVRyRNWn3iJgSEVwZ7Oni6HLd4rLs-Q8KRp9NrdMaLDJY3hoAbVMQWKvJHmd_M0WDMNyZeQDgXFVp2V_69lGU_3ppnqPg7ODw4N_qaOEkGXh2QTzAaD8gYG9QDKDCZ-0RCvTc-THNH94CNGHd9K3u6JDvIpiU-YVk51BJZtIykWWYi6zOrhBuIqFOT5hB4p9ECFQk7xGrHIGSHuenvS2Tk61PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b1d68db4d.mp4?token=q7fiYjDJpgPYBTmwu02L2rG4dA4cMN6sU0nJyN4fuUGfIo9DjNfOdv2BaFyH132kq9Pj-SqROhbLJWBFIJDatAIy_sOb6xqhIphuFjWYhzaVicG7GlphJMeUl8c4rVRyRNWn3iJgSEVwZ7Oni6HLd4rLs-Q8KRp9NrdMaLDJY3hoAbVMQWKvJHmd_M0WDMNyZeQDgXFVp2V_69lGU_3ppnqPg7ODw4N_qaOEkGXh2QTzAaD8gYG9QDKDCZ-0RCvTc-THNH94CNGHd9K3u6JDvIpiU-YVk51BJZtIykWWYi6zOrhBuIqFOT5hB4p9ECFQk7xGrHIGSHuenvS2Tk61PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
👍
#نوستالژی
؛ شوخی و خنده‌های بامزه مرحوم علی انصاریان وقتی استاد اسدی داشت خاطره میگفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/104014" target="_blank">📅 09:25 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104013">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c7d0d9c01.mp4?token=YzWkr20DStJJmN8Pjn1-bP-vR_yGJA_j5DlYtL8frOUKz2eiVD4kQaOB6Evgd3izItHyOw5pfKvw8ETuZvkODygNky1O8XdTkhPX0QXswrKCTMw0EXcAv3omFklkYdQPovmHoPrf4RIsY2QuAiVy_z1eDy3K5hyhZlpOMUrL8FIlhTNcDG5jf7zrJkk3OcmZzgLb7XF6nNZL4v5CvyppNCVXUcPaF1FgJdsFmI7XUJRLiSU2I9lSt75YzpGuHFYt0JboZjevBXGl67D39Ph5-jArL0eIqnqpg0gVQlV_mzk8qZt2Km67XsaoYnBOsT9jrojvFTyibr-zSUmwZ_iIKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c7d0d9c01.mp4?token=YzWkr20DStJJmN8Pjn1-bP-vR_yGJA_j5DlYtL8frOUKz2eiVD4kQaOB6Evgd3izItHyOw5pfKvw8ETuZvkODygNky1O8XdTkhPX0QXswrKCTMw0EXcAv3omFklkYdQPovmHoPrf4RIsY2QuAiVy_z1eDy3K5hyhZlpOMUrL8FIlhTNcDG5jf7zrJkk3OcmZzgLb7XF6nNZL4v5CvyppNCVXUcPaF1FgJdsFmI7XUJRLiSU2I9lSt75YzpGuHFYt0JboZjevBXGl67D39Ph5-jArL0eIqnqpg0gVQlV_mzk8qZt2Km67XsaoYnBOsT9jrojvFTyibr-zSUmwZ_iIKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
❌
افشاگری و ادعای جنجالی امیر حسین اصلانیان بازیکن سابق پرسپولیس
🎙
علی پروین سمت بازیکنان تیم پرسپولیس  پرستو می فرستاد تا از همه شون آتو داشته باشه  واسه روز مبادا
⁉️
مجری : از کیا آتو داشت ؟
➕
اصلانیان: از همه آتو داشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/104013" target="_blank">📅 09:03 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104012">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aab9f085ab.mp4?token=GGpUNn7VM4qvvman0iBt0x_hEbQKAmedpM4nOedNv7pDd9T6dqpVpdYJYlHrBkDbWsGjPXiYPgmQEaJdvgsqkRlVjNPMKUULqPMld0E6gMzoltLFSfQbHJH8kCVWCOtipgWpaq9v3CAPR9x38UWzgR6zdUcmYUl6vs5e9xTqLbSN5t6MmmWul4LeBSdfdMXpH7ub6hKx_otStNNZmMufdBZWomBuo0yZf2tH0Yocklz969TnaPI_oRGgxXXqOdBpCCI5cL8EYeZLXTZgBaTPLnvwI70Py0O1HKUCFRj2zBPJnbsB9l_xhFMqDmy3xApaberRIbXASQM7B59wDhWJFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aab9f085ab.mp4?token=GGpUNn7VM4qvvman0iBt0x_hEbQKAmedpM4nOedNv7pDd9T6dqpVpdYJYlHrBkDbWsGjPXiYPgmQEaJdvgsqkRlVjNPMKUULqPMld0E6gMzoltLFSfQbHJH8kCVWCOtipgWpaq9v3CAPR9x38UWzgR6zdUcmYUl6vs5e9xTqLbSN5t6MmmWul4LeBSdfdMXpH7ub6hKx_otStNNZmMufdBZWomBuo0yZf2tH0Yocklz969TnaPI_oRGgxXXqOdBpCCI5cL8EYeZLXTZgBaTPLnvwI70Py0O1HKUCFRj2zBPJnbsB9l_xhFMqDmy3xApaberRIbXASQM7B59wDhWJFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
🇮🇷
میرشاد ماجدی رئیس هیات فوتبال استان تهران: این که استقلال به عنوان تیم اول اعلام شده و جام نگرفته است تناقض دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/104012" target="_blank">📅 07:21 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104011">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84d4c307b5.mp4?token=gUjFWufYPedEmPoCp9TGWwNVjiAKd5qoxmDM8pSK4Vc0KsSHN_ZUTPUbwBeCImFVrfcJwAOH_0QCmlJANS0aDmsELlyWMwsODpeZQY60G9NzwqvGJLGn_NaoiG5yBstwJiA_o76OqoNLbN_tb2zOcTpUzkN22yWdog_nJH4ORRXWzyDTTTTAcrHt8H9kmptC2B82lmA0P2M8-hZLzbIFOFI_2zVwFSUqPfQC1chakkmBdraoySfWCipOS1BJ_i7DfR3p2-zc-005RPEJjzIedT1YxHLkoxBewfCj6Z2pMggel8j7Q3wsQ8T9jjuyDJeMGQiM91jW04uAoL9oPmA9xA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84d4c307b5.mp4?token=gUjFWufYPedEmPoCp9TGWwNVjiAKd5qoxmDM8pSK4Vc0KsSHN_ZUTPUbwBeCImFVrfcJwAOH_0QCmlJANS0aDmsELlyWMwsODpeZQY60G9NzwqvGJLGn_NaoiG5yBstwJiA_o76OqoNLbN_tb2zOcTpUzkN22yWdog_nJH4ORRXWzyDTTTTAcrHt8H9kmptC2B82lmA0P2M8-hZLzbIFOFI_2zVwFSUqPfQC1chakkmBdraoySfWCipOS1BJ_i7DfR3p2-zc-005RPEJjzIedT1YxHLkoxBewfCj6Z2pMggel8j7Q3wsQ8T9jjuyDJeMGQiM91jW04uAoL9oPmA9xA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🥶
🇪🇸
🔥
انیمیشن جذاب و دیدنی حمید سحری از شرایط نقل‌وانتقالات این‌فصل بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/104011" target="_blank">📅 02:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104010">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f966553cd6.mp4?token=nnhmSLn_6ZEx9Rqge-i25zbPFgaeYLCJk1HjXLBFfVSKyVIQ8pVGOPugqcua36dpUkeV1V3l3_caFT-5EJQt9J9PoUSK9A1rD7rd_qs1AZDB9lsuWHkNH-wYn8wLP0Vc_5mvGs8lC-lfOcUaZQSVZ_qG_UXuE0fVF_rUn3vvZNqRa4h16vZLeTdKcGNJkhPhiEvR9f-k3zn1lMvjzdtFR63tE-aEmu-nY9POEFdbaewWiaoLVb5tIWxCvQZSn2Y4CTSDTu0ov6TIHmYmVSvKPgwgXUoN8PkVNFC6b3p6cHRdYjEpHqhEv3ZFCPHEGjmXh5K79X5nKIqtSUQdOag1cCK6_sRuS8n2aC-YGZx3ObZsX1gAZCTQwBB5DGbqDoWxtWwQwJw_qOA8F9CB-cwAVJ90Nuz9SYlEQpARYUG1Dy9dT83ev7nQl5Yj6EntuzohY5BnAB6qH9vYTdM4fRiPC6OtZ8ixidv5Vc_kaFzIljE9y5Iydwdgw_1aZMFjfXbwTXXvjCh2Uv9TtykhREc2obJM0IK6T9XIoE4EECtzxJLBQXnYygVFg5umwHwnTFZ2DlqaoOV1HSnjrarIdW12wxtSu-AKLGnvoI41F6auJEhvvxZI1UgG0R6Vn5SnBcYYEhMRzvxfRp_AZJTWqkIQVhOWrzwnxWHFQugyA1UHBMY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f966553cd6.mp4?token=nnhmSLn_6ZEx9Rqge-i25zbPFgaeYLCJk1HjXLBFfVSKyVIQ8pVGOPugqcua36dpUkeV1V3l3_caFT-5EJQt9J9PoUSK9A1rD7rd_qs1AZDB9lsuWHkNH-wYn8wLP0Vc_5mvGs8lC-lfOcUaZQSVZ_qG_UXuE0fVF_rUn3vvZNqRa4h16vZLeTdKcGNJkhPhiEvR9f-k3zn1lMvjzdtFR63tE-aEmu-nY9POEFdbaewWiaoLVb5tIWxCvQZSn2Y4CTSDTu0ov6TIHmYmVSvKPgwgXUoN8PkVNFC6b3p6cHRdYjEpHqhEv3ZFCPHEGjmXh5K79X5nKIqtSUQdOag1cCK6_sRuS8n2aC-YGZx3ObZsX1gAZCTQwBB5DGbqDoWxtWwQwJw_qOA8F9CB-cwAVJ90Nuz9SYlEQpARYUG1Dy9dT83ev7nQl5Yj6EntuzohY5BnAB6qH9vYTdM4fRiPC6OtZ8ixidv5Vc_kaFzIljE9y5Iydwdgw_1aZMFjfXbwTXXvjCh2Uv9TtykhREc2obJM0IK6T9XIoE4EECtzxJLBQXnYygVFg5umwHwnTFZ2DlqaoOV1HSnjrarIdW12wxtSu-AKLGnvoI41F6auJEhvvxZI1UgG0R6Vn5SnBcYYEhMRzvxfRp_AZJTWqkIQVhOWrzwnxWHFQugyA1UHBMY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🔥
🇫🇷
دینو تاپمولر سرمربی لانس بعد قهرمانی دیشب: لانس یعنی همین. ما از هیچکس نمیترسیم و اینجا میتونیم هر تیمی رو ببریم.⁣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/104010" target="_blank">📅 01:46 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104008">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FEGtcVbJtbYrZLPhRK-Krz3upieSyWGntM7FIxM4o9u7TAT0LFda2VFy4-wvd-4s2OBK1IiGOJe4-gblgtJT4losrzCYZz-rGLL5XIxaCndeNiAqx611R_yci6sZoQgVptIVcQBR6px6NzZRvteu3PVWM2yqLI9JobSp1w3R0EQ5mMK9bOFpExZnoOglk6wcAsuTMWuVtK_0UdKKYDzPa2s2s2ZAe6niGGu6Ywoq0aQgdausfyDBX3xHzjqbyxIsZ-yiVUu4B8asupCA2kx0J-v2lPELdFPIUtco52L-vPgRxpe_iu06GHmkuH_PiJoUCNrlq4XWOsiAlGiQxkGdlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q7ApCZarxo77EqZn3nhgKuLXsSLYcOR4Nv_VeSTnIfMpsdkH0vu_SC1uME9RAR-_zJ2ek5baeNEvZWpM50XLPL5iUV9vG9U-2SLJ3GYYCnRwLUbF0aBq6S2eF7nDljvkWikz_tg5H7Za5_bzNcSb3QajJqyFMKxURjRiUpJnyjeMM5pbQ2ZRLvQsLp6FlZO5mn-V6FKjOJ9_mIfTCZg9JJU6uC82YZR-XBHqqSh60V_kga1EbASboIJ-PcV6icwXFD0JPy0fXrH2UrBtfrHzgzGKFZLKprl9yLNkk8EQGbpaZWZ2L1EDjRAoTMf52R_L8mu2MmDx5MyCWXaolTBwDA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🤯
ساعت لاکچری رودری ، مدل
IWC Portugieser Perpetual Calendar
- بدنه از طلای ۱۸ عیار
- صفحه نقره‌ای
- بند چرمی تمساح قهوه‌ای تیره
- قطر ۴۴.۲ میلی‌متر
💵
قیمت:
۵۴٬۸۰۰
دلار ( ۱۰ میلیارد تومن )
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/104008" target="_blank">📅 01:21 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104007">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r1Q5AGeEz6LkZw3FFzgj-EMClnKiwoG4QcfhDAt4UoiLMdgRqm1Pn1QY9SSse6F3P6DsNRMpHiLUzDjCO7sTXv59nuRRkkhL93xEK7H3CLTzFU0UHrpZUeQauN5E3Gv4S8t9USKV0ROFTaR8bHNsOykJX8POCgz5t8VsVTH34vLnPS-CNN_nP-OF2RgjX71zuC45fRcwrEaZbDcuY4t0e82lKMaXhp5iWCZOZZDNiLUBXhc0TdoAlyKYl7uCRpG1kji3wXrqwUFq3kD3lmnTrDt2ZXQsvJBDWMVa18NFpVlGgogG2_6sPok6ZEGYNz8Yzk256dHYKmG34MhqZdERWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😳
🇵🇹
پاولیدیس مهاجم وحشی بنفیکا امشب در برد هفت گله تیمش تونست طی ۷ دقیقه هتریک کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/104007" target="_blank">📅 01:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104006">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o7S2z3JadSITjbnf82eU4U6fxp-CPD1XxiAMJ_Rn7wHtX-H45JJ_-oB0BXFBmDN_4cFJio0X4MAhVZbQPJTS3feee-DBFHeSjUUBYg66av1gqvgomruNjqzC0Li0lKa2m_XEPIAvdjZ3ca_hW5nGm8LD23fGGkppYvediGoDGnbAdzc6ymXClGnYNrfLTe-1oRjUiiKn5cIrP_t6aTN0GwUIqUM1Hx0LpVzjbG0YOxuU-sqgitYE5YRU65mwxZpps3U55bDR_dgQycZ9o5gB5d-P8OtXWDYicKSvw45mmZnJP4korRnqRHd-ZUFveVhhWVTayZqiwWCSYWOXdNSBeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
با حکم علیرضا دبیر حجت‌الاسلام والمسلمین عباس فقیه سرپرست هیات کشتی استان بوشهر شد. دبیر درباره این انتصاب گفته که ایشان سوابق درخشانی در روایت پهلوانی‌های اهل‌بیت در منبر های خودش داره و قطعا به کشتی پهلوانی کشور کمک میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/104006" target="_blank">📅 00:51 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104005">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇷
🔵
خبر فوری روی آنتن زنده فوتبال برتر؛ AFC انتخاب استادیوم را از استقلال گرفت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/104005" target="_blank">📅 00:37 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104004">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98a00c0468.mp4?token=JuR7ybbgdaD7KEPFeJ7hRwYurOGmmR-WTjBUgFMnrmQJ3xwmZNArAb-iH1fMNIV7u7FcRUY0OB9iY_R8BC5FqLKMseZNkra6m3u8XCyTNSXb-rEAkoBuF2EZVlkznK0yzuNF0mIZWIj4wb-vqQUVgOvzdXs4FqqOn_0mev9r82bO9FULmZMVC9V5GIiDe5u4-JkRc2-Fk2sOf446D60AWqvVRq1J5TAdQyHRxes7jGTMvFEtShU3zxJIcifWhq9s8NGpbDMOkM7JZfKckEtd0G2kwgmPucizNqCwlvYPaHCOYMwryWAA115kkqB8L0SoAuegQooRMvOsFl5MXDdjdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98a00c0468.mp4?token=JuR7ybbgdaD7KEPFeJ7hRwYurOGmmR-WTjBUgFMnrmQJ3xwmZNArAb-iH1fMNIV7u7FcRUY0OB9iY_R8BC5FqLKMseZNkra6m3u8XCyTNSXb-rEAkoBuF2EZVlkznK0yzuNF0mIZWIj4wb-vqQUVgOvzdXs4FqqOn_0mev9r82bO9FULmZMVC9V5GIiDe5u4-JkRc2-Fk2sOf446D60AWqvVRq1J5TAdQyHRxes7jGTMvFEtShU3zxJIcifWhq9s8NGpbDMOkM7JZfKckEtd0G2kwgmPucizNqCwlvYPaHCOYMwryWAA115kkqB8L0SoAuegQooRMvOsFl5MXDdjdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
😆
🇮🇷
ریدن رامین رضاییان به خودش از صدای انفجار ترقه هوادار فولاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/104004" target="_blank">📅 00:30 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104003">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcdaa9a811.mp4?token=pgFR63CmTYdNa4Cye9YRErYF59QlK8Ybne5uFUKomAUofsCOTbsZ0bI9C_JtE0ETdYZxyL2qNvb_sDlyT8TE69VKgQt1nqatfptCdez_ow4U1rjWLCp3JoKUPKlSUTX-WsXwkGCyaemxaNFAePR5CWaxQk1jajde0fufHBALc9q7VnzRQjf_UZ_qnnbvAflxJNzUCNJl-4xwP_5H8jyl0FDOKTrQ4v2lGHrGSQroO3ML4Kkvn7AY49zeWAZV8UXJRCMctdALH3kPKrQPVOCNklA7GME6J7mRyksqgyerZ5E2a_KXTjm1x3RBnj5_E78vv_gdxtcXWLZ1ot6QQ4wo54i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcdaa9a811.mp4?token=pgFR63CmTYdNa4Cye9YRErYF59QlK8Ybne5uFUKomAUofsCOTbsZ0bI9C_JtE0ETdYZxyL2qNvb_sDlyT8TE69VKgQt1nqatfptCdez_ow4U1rjWLCp3JoKUPKlSUTX-WsXwkGCyaemxaNFAePR5CWaxQk1jajde0fufHBALc9q7VnzRQjf_UZ_qnnbvAflxJNzUCNJl-4xwP_5H8jyl0FDOKTrQ4v2lGHrGSQroO3ML4Kkvn7AY49zeWAZV8UXJRCMctdALH3kPKrQPVOCNklA7GME6J7mRyksqgyerZ5E2a_KXTjm1x3RBnj5_E78vv_gdxtcXWLZ1ot6QQ4wo54i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇷
🔵
خبر فوری روی آنتن زنده فوتبال برتر؛
AFC انتخاب استادیوم را از استقلال گرفت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/104003" target="_blank">📅 00:29 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104002">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">👑
فقط کافیه مرغ از خیابون رد کنی و‌ پولت چند برابر کنی راحت
💵
👌</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/104002" target="_blank">📅 00:29 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104001">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=ockknqpxqYl2vcb1kqVTp4xiDCeVm8aMoaL23GYgCw8qpX7lYaRJ1iCgQSkkswdfgKzMCk-lzkoWg8KyLdIJYOsbIGER77LFCzMlJQ7ya5ohTwZW5JObQ7jyR59NprYvN5-r3xyvVZI-G3qgm6IgPGm3iEtNgT-theRdgynR34Bu7lFIa63BVeEFfmgfSCwXE4wnVA2sQz7Zwo8Wh8a5TsTaesKDjoQef7uQxSm6Nad7tjtTS_uLOCdbDKPE5KhaP5jkLMBZ_tqV9h7vNLxSYbWrqSSEeO0hdcv4tWV4Ahm3KqaF5PdSKCL6U6KVGon1A08t99lazz7XFu0Nm2FKXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=ockknqpxqYl2vcb1kqVTp4xiDCeVm8aMoaL23GYgCw8qpX7lYaRJ1iCgQSkkswdfgKzMCk-lzkoWg8KyLdIJYOsbIGER77LFCzMlJQ7ya5ohTwZW5JObQ7jyR59NprYvN5-r3xyvVZI-G3qgm6IgPGm3iEtNgT-theRdgynR34Bu7lFIa63BVeEFfmgfSCwXE4wnVA2sQz7Zwo8Wh8a5TsTaesKDjoQef7uQxSm6Nad7tjtTS_uLOCdbDKPE5KhaP5jkLMBZ_tqV9h7vNLxSYbWrqSSEeO0hdcv4tWV4Ahm3KqaF5PdSKCL6U6KVGon1A08t99lazz7XFu0Nm2FKXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
🔔
کانال کازینو شبانه راهی برای چند برابر کردن سرمایت
🤷‍♂
➕
کسب درامد انلاین با یه ادم حرفه ای یاد بگیر و‌ پول دربیار
💵
a26
🎯
همین حالا عضو شو و شروع کن
👇
https://t.me/+FaoDjhEVG34wMWFk
https://t.me/+FaoDjhEVG34wMWFk</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/104001" target="_blank">📅 00:29 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104000">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38b070f200.mp4?token=rI1-l87p9q3LXVQkMvye3_FSjNZNknxPY_22phATu_RxaKZrFmBu3D7Y2VoKms1-dvS2ruQhoRH__yCsBeWtwiCjAiknJYkJBYC33soS8EkWy3ccAGkSq_INzbwO-pVoWeGvsHbUPXso8w_oBE9DLnpLY0CxWY-7WACPMzFFnSRgpLfM0JVmeKQbreiDfenvqm4jQQiGByJlBZoMkCYQNZsCGXK6FDlbNeQswbDe6zauj0wBxwU0cZvr22EqJXALUoJD1X3U9lDAFLSao9An82BisOsq-sEK8TDJqmTDlMrIeYR-6XgLW-2PrBZnG4rloOoziPB7VoohDl9husZSJaaG-7K_m15rfIelOVTtl9UsrtCcorXRDWmIIOE0B-Y7TYsMvJN7AkThLpprlXzsESmb1rcLIdiMe8JMl-TaMOam3nVZVIbwElxKAl2By4JFia2N9FSBfwHHfoe7Yw9XFDCjsJqreJ_9x95n9avpLaUHhvgD6mi9HFBlJNsCRSNMUkV3YdFSWvnPXL92srbO9t7JvomGuTeepdsvsToH8tKiflqu4e1mFMuYQGhRHn3ZNY1ZzsqzszMeopywFm2YYXWmE0sQ7tchQz7sUaQ6slnacOuypoz_KaGl53YuY3bWnseNOpRmhyJRYT3srWHx1f9wWOvkr8GT9Hwm6KPc87A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38b070f200.mp4?token=rI1-l87p9q3LXVQkMvye3_FSjNZNknxPY_22phATu_RxaKZrFmBu3D7Y2VoKms1-dvS2ruQhoRH__yCsBeWtwiCjAiknJYkJBYC33soS8EkWy3ccAGkSq_INzbwO-pVoWeGvsHbUPXso8w_oBE9DLnpLY0CxWY-7WACPMzFFnSRgpLfM0JVmeKQbreiDfenvqm4jQQiGByJlBZoMkCYQNZsCGXK6FDlbNeQswbDe6zauj0wBxwU0cZvr22EqJXALUoJD1X3U9lDAFLSao9An82BisOsq-sEK8TDJqmTDlMrIeYR-6XgLW-2PrBZnG4rloOoziPB7VoohDl9husZSJaaG-7K_m15rfIelOVTtl9UsrtCcorXRDWmIIOE0B-Y7TYsMvJN7AkThLpprlXzsESmb1rcLIdiMe8JMl-TaMOam3nVZVIbwElxKAl2By4JFia2N9FSBfwHHfoe7Yw9XFDCjsJqreJ_9x95n9avpLaUHhvgD6mi9HFBlJNsCRSNMUkV3YdFSWvnPXL92srbO9t7JvomGuTeepdsvsToH8tKiflqu4e1mFMuYQGhRHn3ZNY1ZzsqzszMeopywFm2YYXWmE0sQ7tchQz7sUaQ6slnacOuypoz_KaGl53YuY3bWnseNOpRmhyJRYT3srWHx1f9wWOvkr8GT9Hwm6KPc87A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
محمد محبی با انتشار پستی در صفحه شخصی خود از جدایی‌اش از روستوف خبر داد
. مقصد بعدی محبی احتمالا تیمی از کرواسی است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/104000" target="_blank">📅 23:47 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103999">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d25894916.mp4?token=WliCC2EuAASyapdT5DFEjXrx2pgRh_2L5lS9rlJL5aj4F9znEOSKV0cFlURFch0kET290GUfQoR6Rl94X7BT8TYGxwRq1cwhEO6N31XYFiY0vu0xGR1s5VlqiKDwpc3HOj6gR7efZKZu_vv5VWDGqnlojSWYP-NMmTjePI7f129hc4iBjdysuz2LUOPEnjIeefywWjJemIzrDEsugiu4l1ngoiwhJuPVhj60kNUSTg6EHi8IbeFt0qw3fLnvBWVRT3p9rhMQmc-X0-7IVmty62leZd1bMYfZy5IM0qCwOSRUXbl1WVU42yMXJNlkD8jFyDVpuZWI8NBNDOj_RPN0Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d25894916.mp4?token=WliCC2EuAASyapdT5DFEjXrx2pgRh_2L5lS9rlJL5aj4F9znEOSKV0cFlURFch0kET290GUfQoR6Rl94X7BT8TYGxwRq1cwhEO6N31XYFiY0vu0xGR1s5VlqiKDwpc3HOj6gR7efZKZu_vv5VWDGqnlojSWYP-NMmTjePI7f129hc4iBjdysuz2LUOPEnjIeefywWjJemIzrDEsugiu4l1ngoiwhJuPVhj60kNUSTg6EHi8IbeFt0qw3fLnvBWVRT3p9rhMQmc-X0-7IVmty62leZd1bMYfZy5IM0qCwOSRUXbl1WVU42yMXJNlkD8jFyDVpuZWI8NBNDOj_RPN0Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
میثاقی: افتضاحی که در تورنمنت 3جانبه به بار آمده تا الان ماست‌مالی شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/103999" target="_blank">📅 23:07 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103998">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/473efcace0.mp4?token=i1OczMvsJIV8iW_nEHQUO2qCghdIbluMqN3WoqpLUHEWNAOON7LWReIzuyHmt03w577nJKr7Xbe0Ov0lRUlwNvxd6SyK9SublYL0CmE5k2Xz9k_J-8g-_9th4cIViKsXDv525HdLeVVHv_y8MM7y--lnxNhij1wL59a9XPPDa91-FU4xUgTTyuFh4bGcg8uwZWyAmy0YAth1oI3ltnRABrIm7d8aWPC5HQ-rmhbaEAZM5W2PerdGoIQClojxqNQUxt869DD7OFIAqQKfDa2qVD_MfL9rDDOAkmpRkNUtx_OlGuq_SVLNHSvQiK6rFutSGku-nEeRAKikLo__WdYEJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/473efcace0.mp4?token=i1OczMvsJIV8iW_nEHQUO2qCghdIbluMqN3WoqpLUHEWNAOON7LWReIzuyHmt03w577nJKr7Xbe0Ov0lRUlwNvxd6SyK9SublYL0CmE5k2Xz9k_J-8g-_9th4cIViKsXDv525HdLeVVHv_y8MM7y--lnxNhij1wL59a9XPPDa91-FU4xUgTTyuFh4bGcg8uwZWyAmy0YAth1oI3ltnRABrIm7d8aWPC5HQ-rmhbaEAZM5W2PerdGoIQClojxqNQUxt869DD7OFIAqQKfDa2qVD_MfL9rDDOAkmpRkNUtx_OlGuq_SVLNHSvQiK6rFutSGku-nEeRAKikLo__WdYEJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
وضعیت کاندید اصلی توپ‌طلا در بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/103998" target="_blank">📅 23:06 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103997">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">همه محصولات زناشویی و بزرگسالان که پیدا کردنشون سخت شده یا ترجیح میدی با خیال راحت و محرمانه تهیه‌شون کنی، اینجا موجوده
😉
👇🏻
@luminooo_shup</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/103997" target="_blank">📅 23:06 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103996">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gWOmap08PnZ8o7x7WfhYlwU1atkd3MfPR0oNzdMYXABG1Qm7C-dP5--oYxH2WvG-a-B1hPcdPpLTysJhQh939cbGneILGCsqoI46Npbnin7cXz059KWXeXU3yOQzVh5c6bhBSdmYqvdi1BVx8ChS61Dc6DuCr6N62tMkUlOyuGkN_F2DGNDl4QU-mqDVP-r3s-AaIDdu_JDunFA9-N6brnAXmnsNJ-GOmD8dNem478dhLDaiMUOl8mT2ZTzz__chZdCLTSslJzTSfhtOSPhhSgfshRANd23k8OStmuw_XIDf9ybWUkP9Fk95XQvwg3_VcIu-kBeJHEK2d2XfnHpesw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
⚠️
ریشته اختلافات نیمار و تیاگو مندز!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/103996" target="_blank">📅 22:45 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103995">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b498c41df.mp4?token=e0Gdnysm9aqun3t-B71mD4NGB93XRCJ92th2QIy1bldNiq9bJS5UBko-elxFHyn_PPNJXzLlOoRnKVzDiSavpF8k3hdgwAb9EzwpomoiHHw2FtaqkNzglhAS0oSc6BEi9ov4C_hjKfznXqRM6otny9pfZcBQ7Nv_YkUrfexWjdPqD_hHzu2PD3kau9KysmuqhTXQ87_FSL3jAJs9ReWJDAbeQMxFv1nGRPkb1ppQjHwdRjtFSxgKjzz8oQKKz2tHqn0Rmyi1QpTpmrlivCVF1ox2nDds50DIul4PpjCw3kJP4ATLl226uaqa-U2gzj5ft8pKiMvYznEToEdRTSWaJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b498c41df.mp4?token=e0Gdnysm9aqun3t-B71mD4NGB93XRCJ92th2QIy1bldNiq9bJS5UBko-elxFHyn_PPNJXzLlOoRnKVzDiSavpF8k3hdgwAb9EzwpomoiHHw2FtaqkNzglhAS0oSc6BEi9ov4C_hjKfznXqRM6otny9pfZcBQ7Nv_YkUrfexWjdPqD_hHzu2PD3kau9KysmuqhTXQ87_FSL3jAJs9ReWJDAbeQMxFv1nGRPkb1ppQjHwdRjtFSxgKjzz8oQKKz2tHqn0Rmyi1QpTpmrlivCVF1ox2nDds50DIul4PpjCw3kJP4ATLl226uaqa-U2gzj5ft8pKiMvYznEToEdRTSWaJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با شروع فصل جدید فوتبال گفتم یادی کنم از کمبود دستشویی در فوتبال ایران
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/103995" target="_blank">📅 22:15 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103994">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sEYEKYQN_Z7LPxgQBz5luQ_qOP_CwGZbFJ9c0WRA_1X2ZHILDKTHiVdJJ_jTdQ3ixSO_n-aDQZy_Fh4H7ReKcXWIJbI4PU53nICVB3YjuOW98kgy9CVHlnd8KaZdf06pmJ_2wBs0OYlsdoo97dGFFiMfX3c5DXIUgLN1-kxz37EBv_oz9_jT-WCahHOGPO32pMcLNb1RSdmZPWWJyTmbpYECEdb0dPGZ9hZRFpEc2DXVxVRER6vO66X3nc32Osmk1K0Gt4lhFsgfSpJe_tUGDbsK9hqZe-BMWpXA5Wkznohw-IGkXKyUjGPG3Du1nKzXpAUkYG-ZRbEZ0lXjv0eFmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔥
🔥
ورود رودری به بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/103994" target="_blank">📅 21:59 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103993">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7a3205803.mp4?token=Evsh3KfO_hcKhLLRbgNw-C0EZlbBnzzo46FjzV7MbMNbaFXV7Eac5qxsWSfmZrjESMHDkfUnqs3fj2cA0VBpmzKbpl7QXul9D-wbiyG0E_--peS6AzPcyvSYMSt9oPCbDBjxRD4v_SodwQwtHKYs4f70V0TUiBbzSSDy4NPqBH8btLWNvzBWJ9OmrSQjwB6EpdI_XTg3_3En9RzQnDp4pguEWUjF4rXRg0CDQN1Kr-qO6TWvbVADRWmmIsLYlybvz6RD7Q0uoCftOoLlGv8KK99EI870Nkn8mruRe8hEC58S2mytTLml47f36r9YNwBJGldZNAMsL09GYa1XfXq_Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7a3205803.mp4?token=Evsh3KfO_hcKhLLRbgNw-C0EZlbBnzzo46FjzV7MbMNbaFXV7Eac5qxsWSfmZrjESMHDkfUnqs3fj2cA0VBpmzKbpl7QXul9D-wbiyG0E_--peS6AzPcyvSYMSt9oPCbDBjxRD4v_SodwQwtHKYs4f70V0TUiBbzSSDy4NPqBH8btLWNvzBWJ9OmrSQjwB6EpdI_XTg3_3En9RzQnDp4pguEWUjF4rXRg0CDQN1Kr-qO6TWvbVADRWmmIsLYlybvz6RD7Q0uoCftOoLlGv8KK99EI870Nkn8mruRe8hEC58S2mytTLml47f36r9YNwBJGldZNAMsL09GYa1XfXq_Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔥
🔥
ورود رودری به بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/103993" target="_blank">📅 21:58 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103992">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbda4c8e1e.mp4?token=RDGKeN6c73fyG0-REi9T9Q-aMT3u0aoj7iXTPeLtBcghJV2cpBccZLNWElNM1oHp6ho96QjXgOePGBmv72dL6mPoLcS95Q_zNGaPeXEf3lDtopRmOjv-sXijYnVDdrBzFmWmlFmMUhZEYBxOdJjJFcwj1mbpOM6X6Tb_DOtnN_HohH9mUHpDYlGoaVNT98rGyUoLUhN6PS6e2OZkU36Qy9wHN84EVXxEeva7JNq-wjSsvHdoweJnxz0k0yZUuoSrPEV2kQwiSxau53kFP6AOPQOYMd06Co0P9bBhLzIB9lKwUUUIy2LR1Ih01s0Z7TxCHxWkQTcWOFeKuX_ZtYR9THPt6NnmupGXyEAchyb0RfmC_NBlSO36WSLqPiUnfXRQ5VHuX6kibAKEGunLWhjl1uWdJOO1oDUqmQUoz8c76U1crrdCSBi2cSyZgWxAufQhZHNThKiiT7FrbGGu_d06I-gSWAAVXpSib1d31ge1_ScYUHBsIsXwKSjuril7ru0iOJJRe_nycOsxCtWAeKTuKo0rskI6ns5fUOmxXlwWkPEC_hGxhgORby4GUTuBhGab830HqgiyVUY6pdNQJt9UwEG75pXbR-myexbMJQMyzGp3MOThAV0VItDzLTdY0qM2QZysPPMFMlwVUBTMPAwJjrcUQg1VmyKcSLI3HEiNo_s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbda4c8e1e.mp4?token=RDGKeN6c73fyG0-REi9T9Q-aMT3u0aoj7iXTPeLtBcghJV2cpBccZLNWElNM1oHp6ho96QjXgOePGBmv72dL6mPoLcS95Q_zNGaPeXEf3lDtopRmOjv-sXijYnVDdrBzFmWmlFmMUhZEYBxOdJjJFcwj1mbpOM6X6Tb_DOtnN_HohH9mUHpDYlGoaVNT98rGyUoLUhN6PS6e2OZkU36Qy9wHN84EVXxEeva7JNq-wjSsvHdoweJnxz0k0yZUuoSrPEV2kQwiSxau53kFP6AOPQOYMd06Co0P9bBhLzIB9lKwUUUIy2LR1Ih01s0Z7TxCHxWkQTcWOFeKuX_ZtYR9THPt6NnmupGXyEAchyb0RfmC_NBlSO36WSLqPiUnfXRQ5VHuX6kibAKEGunLWhjl1uWdJOO1oDUqmQUoz8c76U1crrdCSBi2cSyZgWxAufQhZHNThKiiT7FrbGGu_d06I-gSWAAVXpSib1d31ge1_ScYUHBsIsXwKSjuril7ru0iOJJRe_nycOsxCtWAeKTuKo0rskI6ns5fUOmxXlwWkPEC_hGxhgORby4GUTuBhGab830HqgiyVUY6pdNQJt9UwEG75pXbR-myexbMJQMyzGp3MOThAV0VItDzLTdY0qM2QZysPPMFMlwVUBTMPAwJjrcUQg1VmyKcSLI3HEiNo_s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
صحنه عجیب از لیگ‌سری D فوتبال برزیل!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/103992" target="_blank">📅 21:50 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103991">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4baf3554a3.mp4?token=dzjW7N7HZnbt8I872tTwPKTNRPuuBieWE5rheAcf5g4CVwXror1yNiqf8j7X7M9yEH6dyKiCCiI3DsqsBSMNDGG-VkXy55E0y8tI-LzxcVyXOW1r_0Vp_YHdE-J02Th1N3h9SBC3Wb_zGtHPQQ0LUL_eN9SQhGrXgKZFUARyr_AxC8LueMNoDvGUZIJugqg7H8vtLDCe8pFZ_05P21SyO-WZLurdv3Vhb4Vpn7_ezzDargecoSBc9Xa7-AkXdBN2Hg1Ja0LRKidMoEed_5FfXfJlCFr0dVt8BujBHO76K3ngBwkFH3asVMfr66o6ZZhtN8FGhlmZJ3PvZVJZ3m_6YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4baf3554a3.mp4?token=dzjW7N7HZnbt8I872tTwPKTNRPuuBieWE5rheAcf5g4CVwXror1yNiqf8j7X7M9yEH6dyKiCCiI3DsqsBSMNDGG-VkXy55E0y8tI-LzxcVyXOW1r_0Vp_YHdE-J02Th1N3h9SBC3Wb_zGtHPQQ0LUL_eN9SQhGrXgKZFUARyr_AxC8LueMNoDvGUZIJugqg7H8vtLDCe8pFZ_05P21SyO-WZLurdv3Vhb4Vpn7_ezzDargecoSBc9Xa7-AkXdBN2Hg1Ja0LRKidMoEed_5FfXfJlCFr0dVt8BujBHO76K3ngBwkFH3asVMfr66o6ZZhtN8FGhlmZJ3PvZVJZ3m_6YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🚨
خداداد عزیزی:علی دایی خود خواه است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/103991" target="_blank">📅 21:45 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103990">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VJDROqVJs7WWh0SHBkQ5-_dpf8SK3BsWiMviDjnoIilQMoPyz_uWSHxRjuy1o5bLyt-ZqIeOrlLj10g2_SC7ZmJceJG_ekaLqtQrAChZAkExYWOswu89bUGYwdq07BBipw9JKfro0tJUgAjovZkOo13mvONSC1Py6qmPTRGlBMDi3exy-7uGTigTrikWXWaSG9PZkkHt2TY6nLgVtn_rbOvr2c-FwgJadGF1tA7WKdtNyPnblMOYadF6KN4JiqiOzejYmrXUmRPl1-oej3c5A4kIIbaUhE2xhTdvcLltowIJTIXtKVud9FqgNbpoX8DKcb86ElvMOX_iwOwIvTFjUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
ارزشمند‌ترین بازیکنان فعلی رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/103990" target="_blank">📅 21:15 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103989">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d07263cf3.mp4?token=HgA0lpaiJqxrlOUjzNNf6b2eAYvq219VI00HFLw6thKeb3m1SKeYOCmgFd9X7BM52OjQqot1-gEvdBOaItN5H_7yAzIg1JkCdAECQXcRjnoU4wAk0B6j9uPp7aHhuRgIuA89Ns9J6_DqroxRz0GRRYpERIMWCYaRg4qjjNc2QITwSjkvDNxxIMW4q_u0HikOM8MrASzAnfSjdiffmh3OP3qcmFpuWwllKg-4HvpTnXJfMxWW95tc6AnEV9Jijn5bM4-wdM93u_e-nwTfn0Dehu9MiNDDwCC27wRL_f-f18Yf4umpzo44w1MneL2cdQyaSavykWCV_hqIQ4HGxOxmyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d07263cf3.mp4?token=HgA0lpaiJqxrlOUjzNNf6b2eAYvq219VI00HFLw6thKeb3m1SKeYOCmgFd9X7BM52OjQqot1-gEvdBOaItN5H_7yAzIg1JkCdAECQXcRjnoU4wAk0B6j9uPp7aHhuRgIuA89Ns9J6_DqroxRz0GRRYpERIMWCYaRg4qjjNc2QITwSjkvDNxxIMW4q_u0HikOM8MrASzAnfSjdiffmh3OP3qcmFpuWwllKg-4HvpTnXJfMxWW95tc6AnEV9Jijn5bM4-wdM93u_e-nwTfn0Dehu9MiNDDwCC27wRL_f-f18Yf4umpzo44w1MneL2cdQyaSavykWCV_hqIQ4HGxOxmyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
خداداد عزیزی: دوستان قلعه‌نویی بعد از بردن ژاپن به من پیام دادند که دیدی میشه با سیستم علی‌اصغری هم ژاپن را برد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/103989" target="_blank">📅 20:50 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103988">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XWAdXEXYmTlxURcj0l8xpzs940LQA2THD7ule4u9HSxhH-kdkIV4S4LVxXWj516vCSOKcvTW5fZZS0evwUkPdug7vXaReioyqHf-9dw6CxAnCaHrNne8BPWziRJA-oEU6LQhnSoT_d5k-ZwTbDVhvVDfDl547dx-k8avtjLyd5_oJMmWe-6hILF2Gi6_xbhGjjA5rEBWz5qiNXMWjkvpiRCD3fiAUcqodtJKbmiWgaErU5RMego-couzOXZD1uHMb4owEKfYLP9I7qnxA8q7_vOwBJ8vLKnN2GiAHRS73qwi3oLn6eZ1fg_0q6PSETj01b16bum8GQS4oVRqiGgZkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
نخستین حضور دانیال‌ایری در تمرین پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/103988" target="_blank">📅 20:36 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103987">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HLgqnoJQW0d6xYy4HW8MeGDFZ5GMPRqEkBKtAg4V0MQwhpxYCsj4U7bRcHB4ocPkMlFaCz4ZMekN5w7OXCrm82fXkKxet5Jl0mbKOYTFe37JyxC9wfMQxjI_SgrBoHUTfYfYctkz6KZlb86AbmT2wAwYtmwkPMN3GLHD7w5hn-P-tixT45K4PXGGFJyGtcxTvGzZRrSQ7xjGL_vPLxVL-W8PmCVN4EW1foHSItBqWY3WvE7VPbJHAJuFUe0h7m9YvLVai3lnq6rApA92f90rjfXpEbXR7z7DtCiPymgTlaGic4IoK_Dd-3UB-Aj2nb6W3P7zLbcMnyqzpjF779XveA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔥
تیم فوتبال خاتون بم در نخستین دیدار خود در گروه E مرحله انتخابی لیگ قهرمانان زنان آسیا، زسکا دوشنبه را در شهر دوشنبه تاجیکستان با نتیجه سه بر صفر شکست داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/103987" target="_blank">📅 20:35 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103986">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4c623e2cb.mp4?token=AJXzekqXqUQUmVcvUuu7r3itWpinqmQxa7DVAEAskN5o7BgdWv9E8yvGXmuX6SKBIXCESlUV_JKSRG5VPTomxBPGyPxeHQ-5brHZ6_uWsk8U1IxiVviR79mHvAoMdWCmYJIWfyFY8X-IYpG1R_9FwmFsEBCPK3ZJIEzPM67w1nnsVCS4wHak-kjWOOwBJy3k_cwLDDmWm9EDKX11SglPmfnntzcqhNyLdHF04at4NDfhSVrISBvdEQgdt0FoF1Y7Sc6BPHRNtLSSVLpwKyMtuRNaIVdOxRtVY3wZ4S6pJQT_iBz0ZY5ksX3vUjFbUUXQzVOAGUwf2NmehW-WWL_tGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4c623e2cb.mp4?token=AJXzekqXqUQUmVcvUuu7r3itWpinqmQxa7DVAEAskN5o7BgdWv9E8yvGXmuX6SKBIXCESlUV_JKSRG5VPTomxBPGyPxeHQ-5brHZ6_uWsk8U1IxiVviR79mHvAoMdWCmYJIWfyFY8X-IYpG1R_9FwmFsEBCPK3ZJIEzPM67w1nnsVCS4wHak-kjWOOwBJy3k_cwLDDmWm9EDKX11SglPmfnntzcqhNyLdHF04at4NDfhSVrISBvdEQgdt0FoF1Y7Sc6BPHRNtLSSVLpwKyMtuRNaIVdOxRtVY3wZ4S6pJQT_iBz0ZY5ksX3vUjFbUUXQzVOAGUwf2NmehW-WWL_tGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
تمسخر مسی در استادیوم‌های کشور آمریکا:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/103986" target="_blank">📅 20:20 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103985">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PXmSkzRTnatgtvDsxquI9whBTBtWTswWAz6QhLvlX26KVphZpZtx1DKdjJjIR794l_2tMXH2yvEsv3EDce9Mw1JLlm-lA-8rV6eE73eqaVLiIlFAb5ysU1XN6d9GQTINoTP6_HDKPX6NzyShBOigDMA4mz6Oxil3ItTqM-m8Y98-8iA0H_ynXIkKcLDDNrA2U2P2eYpu3aEXnrmVh-DMhjvKAh5oXJyey8VArtlLgF4Vsz9wvJxtNDmpJa9iA-skfrztyOlQxh_4-URDvf1Om5w6-ndRgBFEsdWWy0HVDE0FMjuxC7241spl_hPtwjKMrNdkHlfHNjswrWG1Rftdew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
متئو مورتو(معتبر): احتمال موندن خولیان آلوارز در این فصل برای اتلتیکومادرید بسیار زیاده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/103985" target="_blank">📅 20:10 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103984">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KP_qJVNZXrUfW5byoR6tsuACKYTm9uiWLSgWRQNZ8bN07hJRqx9Xn-mZw5oirQidTvAvaQLBL5Pkr5iS0vF_9ScRQ28M5iUrIoLg7p7YnPkIj8ygCDDCk-gXDDv5rejuU3bKgdqV-ZZKXF98oItfJ81uyBD9Q6HtBGa5cDzI2EfPAzf4Kvdf0wl0WlwXRJxm-vtVrh_V1dCvJQNxUh76BtuHEVNOW7kLvZg0JnLvI01sMc2zwl0yIBbTuoOypqRZX4JR2ak83qhwdiROCu1vdpjS7bawiUXzyV8sP-jE5UNRlCiUOrc2tQo8NxgyWgRM4sYu2kTi8lkEH6biy5txDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
😐
😐
🔶
پشمااااتون بررریزه؛ دختر تهرانی با دندان هایش گوش دوست پسرش را از جا کند
🔴
حوادث رکنا: یک درگیری عجیب میان یک پسر جوان و دوست دخترش با آسیب شدید به گوش این پسر پایان یافت. به گزارش رکنا، این زوج پس از بروز اختلاف و مشاجره با یکدیگر درگیر شدند و در جریان این درگیری، دختر جوان گوش پسر را گاز گرفت و بخشی از گوش او را جدا کرد. شدت جراحت به حدی بود که پسر جوان برای دریافت خدمات درمانی به بیمارستان منتقل شد و تحت مداوا قرار گرفت.
🔴
نکته عجیب ماجرا این بود که دختر جوان پس از وقوع این اتفاق، خود نیز برای کمک به پسر جوان او را به بیمارستان رساند تا جراحت گوشش درمان و بخیه شود. جزئیات بیشتری درباره علت درگیری، محل وقوع حادثه و وضعیت فعلی پسر جوان منتشر نشده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/103984" target="_blank">📅 19:58 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103983">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NvWtR-RvqkIwXu1f8GumCjw8DGATH6LjKs-uO2pcf26P4EMhitUKiiPBD5ClwbbKEZUP9coElVn671RtZibZzmckBGpRejT1Y-40kuVIa1r77t26GMISVK9csbEaVmGufizRqsJ0j8v8SiP6PTrr8Nkm2ZH7H9F95Ug4LJ6hHqGCSi2AfNlCu-llu7J9jyqu19x90xJAaS5JgYDsDQ3wRsenJxZDgt-spJsfPkL0YVnU3TlaTXN1djBAf7RsKqvozkPqQd5gWsP_70GVCqmIyiyFijNU4Fs_SDXA6y3_Qf8QpO9Unl0N100e0VR9sj-6ZzWpMT7nRV67wBkWoI1D9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇮🇷
رامین‌رضاییان تا ساعاتی دیگر با عقد قراردادی به فولاد خوزستان خواهد پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/103983" target="_blank">📅 19:49 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103982">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MEF1Hajlq0wF4xUELYQRqfYA2Ie4jtgm4sebpDcbYqEjCI6dLGdbkDgoo9irjdvV4qXhzU7gLNsRayQ6bNbqBJB_7Q3tq1mntQR0A0RUB9yj0YRE-6-rA2PvsIMAbUU5k3o1Ylty2VYY7fpF75qyRADwI7H3QyPtPsNLRDPCBrZXnzCF3FmO5giQvMNwSZv1NnjfDkFFfDpbt_SVLet5005kwldquea6FY_LcCVe18NES1U7s9sR3yrBVKHjIW-TVzxHPVrdnvdGIsY1OpSOP4RNJ4tX0yqoXKVu33QJm2Klvj5DRUDNYoBEte6DdhnV2weh_modYIBSPACemSCVwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
رامین رضاییان داخل هواپیما: انتخابمو کردم بقیشو میسپارم به خدا!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/103982" target="_blank">📅 19:46 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103981">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g0FYLEFXN96tulTmh1rUrqlhDirdnnmSDCgC-EK2yYFzaYin8mNlPCPOlVzeb6sOD8YkR8CJU3IrNPgeDOSDdMVQCb28lGDLvb1woIsL3Sh3302I6ghfdf8J6QCl8KEtEfkwalMM8MpZKHTaNUVJrrLgTPIbNfoX_uxlkFIppjOv5o5USa1lco1OWDuuWIgMD3sfQD9dMV1Bu_OcJfMVA4mSPQjCSNGzaVw1ioDY7tkkelVRB48fzrOAVWWW7HhwJ5U074BCO-aqvN81xooEm3X89Pk4coNOJbirw8cExky9dVoYVMeY9mYc32BNUQTpIv01_Ok4UPRlP5f6ntculA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
قرعه‌کشی فصل‌آینده لیگ‌نخبگان آسیا فردا ساعت ۱۱ صبح برگزار خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/103981" target="_blank">📅 19:44 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103980">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VVTxQ2XHgSV-bem-vMG9MwRt3VlYDMXOGexFdOMOM7Pm5EH9DrdDzKbUGmFIjtC5VYx8OvMEUvVFjPqg8XYDFp0_7SydVh-n_xKLj346B7igz_3jFHdxT7GdJfQRvoiRX1b8mxYVR6kposu694w6K1nniY2z1yVD1Dbf6bd6hOhnXN0Jw8CSQZyKAaRruqTLBI3iV13N2FD6yWtPh0XrlsyUPIJCNC13ZHX_yPMhjLJPaNKBII86XWXgd6LITCaK57wuCCZvwUFhptW2Z4WKIfnYi_l9JiveNrigRhmXNDN0pbz-C8rmpZ9IPg-bZHoWK1nDYQnPAYfqSjNmIIPTGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
دیدارهای مهم روز سه شنبه ۲۷ مرداد
💥
بیشتر از ۴۰۰ آپشن پیش بینی برای هر بازی در سایت بتگرام
✔️
شارژ حساب از طریق کارت بانکی،ووچر و ارزدیجیتال
✔️
۱۰۰٪ بونوس رایگان اولین واریز
✔️
امکان فروش شرط های خود
✔️
تسویه حساب بسیار سریع و بدون معطلی
⚡️
همین حالا ثبت‌ نام کنید و و از بونوس‌های ویژهٔ بتگرام بهره‌مند شوید.
🔴
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/103980" target="_blank">📅 19:44 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103979">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K6IPwWd2GY-yfceQWIgViJYY0_5sV2j9vOX49oZNVJSYabhy05tRl0dRMlS70nbhqj6dspq1K4jywTipxdiWICqLwQYOZWQgd0Ny5-8fEhlMn7kY16cL5Vmnpd6fqOs5P7ZGZqbw_ZJOK8KrXfauhrpUMPJwEREvrpTw4g6XsGLykD2YmZvmyL_FcrLeM9M9-grFok_oQK3M8Zf7NvZPlpfRdlEHGCOw4-Xtx51rNeXzFkP-AL8iGp9KCjhN4EfEGOBDyXUrh9Qu5xO4fpD33HUaknYSEaMkyy1LW3Cd7aMpDDgMTpvaEsS5szGcW2Ibs6j6H2P4nhOA7qA_LfVEPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
رامین رضاییان داخل هواپیما: انتخابمو کردم بقیشو میسپارم به خدا!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/103979" target="_blank">📅 19:28 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103978">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/868e8de9ba.mp4?token=mWigcyjyZa4nVK1MW6afPR_OVZISZ6S7DLNcI7JNUX2zCyKSGVI04dLKJVX713lkltFUKbq-jp6pN_Flhan7doidyVGSwH4AnH4XIoFRu25GPMPk0mGmA1FAp3_9UoZU3saToRJCXwjbq1sxbB8T9jKZDzJ_3Ijf9yVt_pmNbU_-a5xyOfvKZCQFZMJqTkdmvJxFyFYqRC60TYGQ4daUOLPBITU1t6hfHyMJl-KJLa_bocQ1sKTMHKbWaeulpfpQOg0Ps7qtToHQf23n2AOSwuJZ-G9USUy9Uf8gsdAWuQE5LXkddjABC0Caq16ukaERf34mePfwqvgFm0syurec3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/868e8de9ba.mp4?token=mWigcyjyZa4nVK1MW6afPR_OVZISZ6S7DLNcI7JNUX2zCyKSGVI04dLKJVX713lkltFUKbq-jp6pN_Flhan7doidyVGSwH4AnH4XIoFRu25GPMPk0mGmA1FAp3_9UoZU3saToRJCXwjbq1sxbB8T9jKZDzJ_3Ijf9yVt_pmNbU_-a5xyOfvKZCQFZMJqTkdmvJxFyFYqRC60TYGQ4daUOLPBITU1t6hfHyMJl-KJLa_bocQ1sKTMHKbWaeulpfpQOg0Ps7qtToHQf23n2AOSwuJZ-G9USUy9Uf8gsdAWuQE5LXkddjABC0Caq16ukaERf34mePfwqvgFm0syurec3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
نمایش درخشان آرائوخو در اولین بازی لیورپول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/103978" target="_blank">📅 19:01 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103975">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/URQcosEptALejfKGgjy56WeZMM1wR9DQ1xH_NAATxFY9_R5s8UqscOErick3c85_3lEsmV6BW-MNBezNa8D_cYewPxNQlpZYuALRqWTFLjrio-ILeOxG0hvbV8xL6IIqzRBMW63AoKL3WlaDSXO0JpC9f2O5MLc5V-fn2o8sSQzTpr2tiWJi8dfmuZSng_5l1hlOAWDGSDhCfuPVEjA59Nixu13Me59fhQORs9Eac2RAC6XCJthfpnmZ3Wup9eIQPJC-pr5-107jhOCJrxwPIWxBVwgCpS4_vOld7QJ8DbKfs045Oq9777kUDODiRb4apZPxNeTsa-4N0hMO-UD2qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DECxKfS8jSaWhNuxfongA72mjANgehc3xvIZv8Y3_RhOdQWwUL0Y34Ta_BeysJ5jqt4IBK9Ie6fmD93GPUtATVy3JbLgSfrU4PC3MlVX2yOzJBrIykothb-Hz1fDRm8UV4LxR3AcLyJgMskSbnojbatUVYwEuc-YSFdk9wsDUQqYGGgGW4mFyP34aKRwonddGRcGiN3ta0Rj3r1K8bWzx0qAuq5BTffFfh-tV5P570FEZY0PR1nxVlUoM6AlREm2kX6cj30iB9KlKDeE2zI0SKyoHUyKZwD8Ia4WcMfaWBEVihkaMbjz4p2GFcUt1dzpHlMNzEyEjqqqvSJ219fLTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pceZLbqxXu3mtBngDjAYbl5yJYWrBg0Az2udFVaiwlEbC4SK8-zXpvs6UbkEtM1OznbPqluS0-zmCyMrmeOochzcJvN8DwhVpO3MN_K1YWJv_xjBzlcSpxdnIrIl0mVOKWtCLeQnAXFfH-yoHhhCs9PBGmqGJM5BETwiElHJkIQDaaikJk7NbsTXvjDQJj9p5V5GI5nBx0p34-xJ7K7btt7IITYOG_G0FDc_dnlvDN0QSQH44dYbTRxTWkgvRsp2MLmKFIJUKbmcWG42KRDdjNn7FOxP4YTqX6D-BYfmyBGOAA4REnRaZDsOjV07oAv7a6W_fd62ywQ2Wf9krhs4qg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🚨
به‌طور رسمی: کیلیان امباپه و ارلینگ هالند، بالاترین رتبه‌بندی را در بازی FC 27 دارند!
⭐️
🎮
دمبله، ویتینیا، رودری، کین، اولیسه، پدری، یامال، بلینگهام و کورتوآ با امتیاز 90.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/103975" target="_blank">📅 18:43 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103974">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20aeb6e887.mp4?token=Qg2xpRpC-PgkwoBJe3mln5mnPVCJ099ivfVEdBTeYzrRXIG67fd6AAkGU1CEBh-wcLpdD50ijt_jAnFmis834UPKifGpYWoUW4S5AgdBT2Z9JI6PavoPbpiyAKFncIwLweINQBS6PDGxRMUTh9fDSJXkeo_YybJVXLQVshsbSuUmX-BkN59x1HhVxh-4YyCEoFh7w_w_npSlox_Ywy6Jp77B6vYtWK3N2MhPMx1Ahb2P0igkMT8svELmmW8CVhcDqTLrdcRLJQ3xBvI8mOlT17SssyENdtDIlxDtjJksWyO-feWJYHCKjWH_dKPYCO-WqyIq_hnnOW3HQl6V-qrtOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20aeb6e887.mp4?token=Qg2xpRpC-PgkwoBJe3mln5mnPVCJ099ivfVEdBTeYzrRXIG67fd6AAkGU1CEBh-wcLpdD50ijt_jAnFmis834UPKifGpYWoUW4S5AgdBT2Z9JI6PavoPbpiyAKFncIwLweINQBS6PDGxRMUTh9fDSJXkeo_YybJVXLQVshsbSuUmX-BkN59x1HhVxh-4YyCEoFh7w_w_npSlox_Ywy6Jp77B6vYtWK3N2MhPMx1Ahb2P0igkMT8svELmmW8CVhcDqTLrdcRLJQ3xBvI8mOlT17SssyENdtDIlxDtjJksWyO-feWJYHCKjWH_dKPYCO-WqyIq_hnnOW3HQl6V-qrtOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
آرسنال فصل رو با قهرمانی آغاز کرد.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/103974" target="_blank">📅 18:35 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103973">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47bede2499.mp4?token=FmSOKSr39oLENqsODCe612fE3ys1jauPFnyeV127G9Nu7JbSwJyZqwNGaP_DudwJoJguLrFiZiekzoyTbtRr1-SIfsL7Du7TMllhg1sCbgLO8d8cjrtRF418iPjZDXLMkjFw43-36G9ah0AXKbZ7E2Im_klvKgWzo1nmc_fcV1PcFwZYUxLf0ZwUUVHznMYNDdOUhz6fC_ofKr76ohtXnJTcjJVc72DyQxvDODMfLPZT-4sVPxCtz4IzGnSiDJoP8sj1PzycDoKKBlp6LQJZrDglhUjnfBWtc089Uq9c6Xq-ehqhloZNM4l2UHZmBuoUqgewrrjhBbaHxHpwl9SXf4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47bede2499.mp4?token=FmSOKSr39oLENqsODCe612fE3ys1jauPFnyeV127G9Nu7JbSwJyZqwNGaP_DudwJoJguLrFiZiekzoyTbtRr1-SIfsL7Du7TMllhg1sCbgLO8d8cjrtRF418iPjZDXLMkjFw43-36G9ah0AXKbZ7E2Im_klvKgWzo1nmc_fcV1PcFwZYUxLf0ZwUUVHznMYNDdOUhz6fC_ofKr76ohtXnJTcjJVc72DyQxvDODMfLPZT-4sVPxCtz4IzGnSiDJoP8sj1PzycDoKKBlp6LQJZrDglhUjnfBWtc089Uq9c6Xq-ehqhloZNM4l2UHZmBuoUqgewrrjhBbaHxHpwl9SXf4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😢
🇪🇸
کیلیان‌دیکتاتور به بازی‌های رئال‌ هم نفوذ کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/103973" target="_blank">📅 18:26 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103972">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">معتبرترین سایت بین المللی شرط بندی که به ایرانیا خدمات میده
✅
وقتش رسیده قید سایتا ایرانی بزنی و توی سایت بین المللی فعالیت کنی
⚠️
https://t.me/+fxq9NcirUag3N2Zk</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/103972" target="_blank">📅 18:26 · 26 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
