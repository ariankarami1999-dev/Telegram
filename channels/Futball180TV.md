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
<img src="https://cdn5.telesco.pe/file/lPPj3Uz1NJAeVo7XfA9_dQ324LgY4skblKOo0iZHnkptENAGm9d90488XHip2pe6ZYtTSYVwO3IDZ4V_DwuR8NqrokR_Aug7WD-9lItvseMj42ahsSfhmQDEFnu7n8YIpxBJ-U7_GQj66FmBXMsrEgBPGqLQyuv1V3JxzmGZA6WHuGDYh3AcJW6gRnzzdToXnx0XOh3xk0EvDqOWlpgqDoTSG3SlTyLCn6GK32w53xBxdUzG42aPmEjIdIdD2TeALBOcRYKzBIN_tnS92CQirfuThXcZy9QZ2xULJjaZx-ILIkpY2jNMz0VK1HJ-Ff980GBezI7WabqgB0TXm-tJEw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 530K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-03 18:14:17</div>
<hr>

<div class="tg-post" id="msg-101903">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EuvSxepVcZxvhSjSpjG2b0IgHNmypdJp-QBXxZGDqVChMRdg0F-3y-3J3p71JVY4BpizNDCP4kQAUmEuzP6oxKMwLpzj-9i9PcQUVi8X095aiR1-z-6yZuajDK33P05jTiw0hxUC1TVMsBR4U_u9fM8gUtSv7ie8xe-93_F4SudpxxwnFuq6okYZCxjmR9MBTQta_evYWct_2_LbCXvlLAvzdnZ1BdfkE57DXdTzk8JqrOcUk78c7G4CzNHBiblKg6lacF6qD9w2-e6zabQgY2jaZRFztZf1Kmo7-ocBnCTMuxv98e4wLW41MF0bPKUvBIsc907rcPGWTefL_sutyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
⚪️
کاکا درباره دوران سختش در رئال مادرید:
من از میلان آمدم تا بهترین بازیکن جهان شوم، اما مصدومیت‌ها و رقابت با بازیکنانی مثل کریستیانو، بنزما، اوزیل و دی‌ماریا باعث شد کمتر بازی کنم. حتی امروز بعضی‌ها من را یکی از بدترین خریدهای رئال می‌دانند. اما آن دوران باعث شد خود واقعی‌ام را بشناسم. کاکا می‌گوید نه بهترین بازیکن جهان است و نه بدترین خرید؛ بلکه همان سختی‌ها او را به انسانی که امروز هست تبدیل کرد. فلورنتینو پرز هم هنگام جدایی از حرفه‌ای‌گری و شخصیت او تمجید کرد.
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/Futball180TV/101903" target="_blank">📅 18:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101901">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ApwBj56ADNkL1hU_VbdzVPpJOzAGEiLvMycJzmIseiM_m5ejEjM5r-tj6-BZGv1bg4BmGROdB8c8PzWhjNXeA-AfzY7NaN9nXGRuyBmRMTxNg4m6S7MxoRJvx8eCMtDfDcSPiYr9q7SvA7vTc_iN2VXT5zBRmlG9x65SqS6OfP3g5ATkFy75SyblEWoMUlIhCKRtUecQSa_MZwrsNEts13QLZF7KZMNnOkgzxE89bYAgxBBRy97aweo-96XG4ypozB1LvYw6DmFe8mVtRLIBZ2Z7u0cijdIcn_4qCjLQEzLd4EPQ8-YonZXRak8ZLrTu5HMtb-1NoIYNj4bonjYPgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/apVzD9tyd2a17FLipZlgdgbCFewRlI3sQvMKSzRvs-zEfiZr6Tcb5ASp4dISUE4M0xbRc03Heet8JrBaCtpylaKLx7W6X9nRab7cAiOhfxVKAAHJhlwDUbZLAUA3dl31HcfmbOmdOR6gvf4AWHbnW0lNy4W921VJVl17a5tKEW0DQg2mFzK6F3d-lXNyBxyMITc6xo1OJvgNmBchN-vmAhuDr1LqUVPSuEcphKwb93PKg73c1UgbgyOYND8PMePtpfFBUTxK6SOtQGNLWHueAyOBYm7HpYs5cmup90zkiKuJjZneWGJz88WF6gP9CIZ3vIWbSb0vZH-5ZWcCZ5j4Fw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
یان دیومانده درباره گرفتن یک پیراهن تقلبی کریستیانو رونالدو در منچستریونایتد به عنوان اولین هدیه تولدش:
اولین هدیه تولدم یک پیراهن منچستریونایتد بود. توان خرید پیراهنی با اسم بازیکن را نداشتیم، برای همین کاملا ساده بود. خودم با ماژیک مشکی پشتش نوشتم "کریستیانو رونالدو" و شماره ۷ را هم اضافه کردم، چون می‌خواستم به خودم انگیزه بدهم. هر بار آن پیراهن را می‌پوشیدم، تصور می‌کردم خود رونالدو هستم. فقط می‌خواستم از همه بازیکنان دریبل بزنم و تا جای ممکن گل بزنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/Futball180TV/101901" target="_blank">📅 17:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101900">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b492c31a81.mp4?token=vatavfQQ1cF7RuJP3P6a3ClqYfNK_YUJUdLZ6S6n_JCU96LWab8cPDfVgP7uiQiJVLklsqQwAqZ3aBnF7BajXycBx95Gw2LwFBgZb7elKq8Zey9mAqxRrjN-peRoXYgWe4AyoMrij3gz24w7QUi0OFhutVOMJYBYivBykb3_C2N7x3lO01MufdGj3yUBfVEi6YHXEDfNqkPOpLOc-3-gky1vdYobJxSavd5axFAG57zulPOABp4h0RnnfHmGonbqvLpn6ycEGgGl9VEJn5sR3EX7tnQKE0saNQwdUUXMef7DKbU2bQYvkl40CHc2T1PJP7qdnqWyklvQyIOim_ifCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b492c31a81.mp4?token=vatavfQQ1cF7RuJP3P6a3ClqYfNK_YUJUdLZ6S6n_JCU96LWab8cPDfVgP7uiQiJVLklsqQwAqZ3aBnF7BajXycBx95Gw2LwFBgZb7elKq8Zey9mAqxRrjN-peRoXYgWe4AyoMrij3gz24w7QUi0OFhutVOMJYBYivBykb3_C2N7x3lO01MufdGj3yUBfVEi6YHXEDfNqkPOpLOc-3-gky1vdYobJxSavd5axFAG57zulPOABp4h0RnnfHmGonbqvLpn6ycEGgGl9VEJn5sR3EX7tnQKE0saNQwdUUXMef7DKbU2bQYvkl40CHc2T1PJP7qdnqWyklvQyIOim_ifCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فران تورس تو تعطیلات در کنار بکهام و مایکل جردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/Futball180TV/101900" target="_blank">📅 17:32 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101899">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51f2886d75.mp4?token=X18DCpaEUnIt6vBGyvxU0_w0BTm73rv0aaOAJgUhY3UcXi9pjjjlbRas44gm4jrgglqgHB2hBv2iBTbEyP2C1g09AWPNJ3iscjpcoQHLhpCSwNjtLbVCiRTAhR2AL5qKJMRIFvVS-hWTHsOa-dbgAIHU8LaErHyGb-UHGiKAy6SpTI28AZs7JEqcG8KcJwCii2BCvTTDL1v6y-zSd6gEL8i4H-cVZ8x4YTRMykBX52WB9ZppJwTXuqxp2wDOCtS5s-i6Fjqq-H0cbq3IHjBEUvQbIzHdBF0oWaySaLECZuTfm9uc2D1KjSO8fT82WHH0FsDD39fgWR0Hv0kHM8zT6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51f2886d75.mp4?token=X18DCpaEUnIt6vBGyvxU0_w0BTm73rv0aaOAJgUhY3UcXi9pjjjlbRas44gm4jrgglqgHB2hBv2iBTbEyP2C1g09AWPNJ3iscjpcoQHLhpCSwNjtLbVCiRTAhR2AL5qKJMRIFvVS-hWTHsOa-dbgAIHU8LaErHyGb-UHGiKAy6SpTI28AZs7JEqcG8KcJwCii2BCvTTDL1v6y-zSd6gEL8i4H-cVZ8x4YTRMykBX52WB9ZppJwTXuqxp2wDOCtS5s-i6Fjqq-H0cbq3IHjBEUvQbIzHdBF0oWaySaLECZuTfm9uc2D1KjSO8fT82WHH0FsDD39fgWR0Hv0kHM8zT6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هر شاهکاری یه کپی بی ارزش داره
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/Futball180TV/101899" target="_blank">📅 17:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101898">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fe82274ba.mp4?token=csWtWLsQHhj64nKAplo7_tBjnir_uXSDPfMsNJ81mb7AF99fvzwDzFexCDkDfvWo9Hhwqj84ojMGRcNBrr9E9ObLOX10tl-8fNCC3vd1ws4ImBJMxn5NCRIC-1nCm4SXR8wslcCguWERN_kobFs4jOtFjEfrivy_UI8D49JntCTL2KHAbZfDI6mXRw-MD42MZBPR-ezkm0SvwZG8A1cKd67Nk7EPSnBjbbbsxbrEXOXGXNTzdnwAD8hVCeIoHq5V_IRvxuzPA3lirT8_uK2ETMtU0ka75-LHpXtUPmlvJnM0bzl-qQSGZD8cEG3WQs_Rkltat8Zeq-71-sby0BQj5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fe82274ba.mp4?token=csWtWLsQHhj64nKAplo7_tBjnir_uXSDPfMsNJ81mb7AF99fvzwDzFexCDkDfvWo9Hhwqj84ojMGRcNBrr9E9ObLOX10tl-8fNCC3vd1ws4ImBJMxn5NCRIC-1nCm4SXR8wslcCguWERN_kobFs4jOtFjEfrivy_UI8D49JntCTL2KHAbZfDI6mXRw-MD42MZBPR-ezkm0SvwZG8A1cKd67Nk7EPSnBjbbbsxbrEXOXGXNTzdnwAD8hVCeIoHq5V_IRvxuzPA3lirT8_uK2ETMtU0ka75-LHpXtUPmlvJnM0bzl-qQSGZD8cEG3WQs_Rkltat8Zeq-71-sby0BQj5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زیر ۲۹۹ هزار تومان با ارسال رایگان!
🥳
با سرویس سفارش
یک نفره اسنپ‌فود
غذای مورد علاقه‌ات رو با
همون کیفیت
ولی ارزون و به
صرفه‌تر
نوش جان کن.
😋
🔥
از اینجا سفارش بده
👇
👇
https://i.snpf.ir/wopv1
https://i.snpf.ir/wopv1
https://i.snpf.ir/wopv1</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/Futball180TV/101898" target="_blank">📅 17:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101897">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e5e82a980.mp4?token=tEzAV3FJlcuoCPei6j5gAnIOGb36NmumIflEfih5Ms2a8g1maIuroTAro3ZysuGxAra97F1QIx_2l3cXEtcUNBRZWKk5Jzq5Y0z8NNvlyw8chMI3aWvuVknsUlOXvo-0iv8R2M183xzCD-qEgDpNF_u8Pthxe8SkeNevg58pumYgi-yOqknlZRcvKBCRZMtyHGUlUv4rLxlxL458zUkrQ-2acAH74b0zSSIgW-N3mr7T6ZzPJ--6_5irpTp1VwjytAntwmm_YgZqeU7DPgE5-49OwawvgWgrSvafgqLNXkYPLR1tvqrC31PfJq1UMLUWetHvBRjGMZ8MXh7OnUpbiIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e5e82a980.mp4?token=tEzAV3FJlcuoCPei6j5gAnIOGb36NmumIflEfih5Ms2a8g1maIuroTAro3ZysuGxAra97F1QIx_2l3cXEtcUNBRZWKk5Jzq5Y0z8NNvlyw8chMI3aWvuVknsUlOXvo-0iv8R2M183xzCD-qEgDpNF_u8Pthxe8SkeNevg58pumYgi-yOqknlZRcvKBCRZMtyHGUlUv4rLxlxL458zUkrQ-2acAH74b0zSSIgW-N3mr7T6ZzPJ--6_5irpTp1VwjytAntwmm_YgZqeU7DPgE5-49OwawvgWgrSvafgqLNXkYPLR1tvqrC31PfJq1UMLUWetHvBRjGMZ8MXh7OnUpbiIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارلینگ هالند از مزرعه یه پیرزن استیک، عسل و شیر تازه خرید و بعد رفت خونه تا خودش دست‌به‌کار بشه و غذاشو درست کنه. فک کنم هالند بعضی وقتا یادش میره که یه فوتبالیسته با میلیون‌ها دلار ثروت.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/Futball180TV/101897" target="_blank">📅 17:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101896">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mKkMPKkKELd8xY653KhbXYyy__KrqnBE4L9sOhGA3N6QYHElHgl9zJ40j8m3icc1BfgieEY7BrCOd4HKD_7JKKLaMp3OtkZxBf3Q-I1eLKrzspJWcX5zJNHMN5dqmpWZi_1psIYssMBetzu9naNAW6KF2bJuaMJX3CP0Q5IxdC68-LTekwMjNt5aBd1XKfCBODd69Y39ABfnab8cG8kLXUKGLMJSd0GRUar1FsjTCl7ibt5DnJX7CBt1wEF9L9PF3Q_kuCBFYoD8IKo_Q8_sc42VE5zursNCQ9F1cWFjbCnbLCWsQmr0LjGNDDry62gnYGC409RWBOV8CVDhrL-XWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
دیوید اورنشتاین: آرسنال در حال بررسی احتمال جذب وینیسیوس جونیور است!‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/Futball180TV/101896" target="_blank">📅 17:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101895">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bxfW-nFPgjfWozcwcY5GvuA09-9OhvoE5lRLuqRg59t7-iF2yzbKT5tBMk6QqBvjcGBXGQVi1C4yR744mmzvp5RXsdw8YABPcwb-Ac4v5URsPaDotBRNCtgz6Z2I4ujnaT0fMwSg0qYb1ZaA6VUtG_n_l9t-XQK1jF_qw8KT6iUlF8u6Yyp9dCtly3sHiYXQ3i1G74-FLHsYCLbZcvNJTCAt20TMaO7GoSPfNVkKEKpHZGdOnClqZGqDfqF2GUAqG1jnLfmgSh0UWJg0j2LjgRlyvcul1kdy2P2UQihXe9jN4NiDOcSN7pL8K_omnzkp0O-WL7SyX1zhilTUkZSzrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
بن جیکوبز:
نمایندگان وینیسیوس جونیور، این بازیکن را به لیورپول پیشنهاد دادند، اما باشگاه به این پیشنهاد توجهی نکرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/Futball180TV/101895" target="_blank">📅 17:08 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101894">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36c582a64e.mp4?token=gClpTm9CQO7ewkTQw4h7eyEg0s3eAxGjz4TRfpaqY1G0oOWMFTR64OmAeSIi8DH57IBSPr4zbGLTA49WP6bV279I3ltNpgRaSYGE12-sBzHCLkv-aeIhzXAi8W_xWpcwmHiX6XV5AXXnAXZAdBI9kI5pd37v1flyegTVEo7ayjghUj_6vqDoGfMWLWEsZchRcdJiokSRpzRtLqB59-N9n_qmc8vWdnzOew_iZ4pu2GuiSKUiWoWUw34SDDCoM-G9EzktWnZ4oJ1i1zX-z_qeO9hr8g9QRFJXnZwdPqqHZj_cWu8Gjo-SqpyKRY_WMXPLZwqm8w8xMCK2va3jUnNKZa-x0HUKb1IKfI5PK7bmy9jzWYRKDSfEssGnS1VrfAQRlUGbF88YVtUaNqZ0LipRBpeEkM8IPHh55gyzqq6BYSAV0P00RaPcgGTEKzSIjRr9ED4eUtbtyZZ1YmVMUQjxz6GTK5XyZ1clWw3b0XQnF_TpOGQkXmYoUAfXvRqK4CmxI54H7Z8gbWyCT0YEIaycHVDZx4iB8U-U6GmpOA_gWP_-yka-nP9lOh7g2uEs5cjpg6YfBxhcbsduwJ3mfdpjM3YyfluSObHXb0IEgM5h8LQ69lCCM51be055j7QbAtfLV0TTsPTqlo-ao834YK-IytzcOwWVBlvh62h8cpOsLrI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36c582a64e.mp4?token=gClpTm9CQO7ewkTQw4h7eyEg0s3eAxGjz4TRfpaqY1G0oOWMFTR64OmAeSIi8DH57IBSPr4zbGLTA49WP6bV279I3ltNpgRaSYGE12-sBzHCLkv-aeIhzXAi8W_xWpcwmHiX6XV5AXXnAXZAdBI9kI5pd37v1flyegTVEo7ayjghUj_6vqDoGfMWLWEsZchRcdJiokSRpzRtLqB59-N9n_qmc8vWdnzOew_iZ4pu2GuiSKUiWoWUw34SDDCoM-G9EzktWnZ4oJ1i1zX-z_qeO9hr8g9QRFJXnZwdPqqHZj_cWu8Gjo-SqpyKRY_WMXPLZwqm8w8xMCK2va3jUnNKZa-x0HUKb1IKfI5PK7bmy9jzWYRKDSfEssGnS1VrfAQRlUGbF88YVtUaNqZ0LipRBpeEkM8IPHh55gyzqq6BYSAV0P00RaPcgGTEKzSIjRr9ED4eUtbtyZZ1YmVMUQjxz6GTK5XyZ1clWw3b0XQnF_TpOGQkXmYoUAfXvRqK4CmxI54H7Z8gbWyCT0YEIaycHVDZx4iB8U-U6GmpOA_gWP_-yka-nP9lOh7g2uEs5cjpg6YfBxhcbsduwJ3mfdpjM3YyfluSObHXb0IEgM5h8LQ69lCCM51be055j7QbAtfLV0TTsPTqlo-ao834YK-IytzcOwWVBlvh62h8cpOsLrI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔙
🔵
۱۲ سال پیش در چنین روزی، دیدیه دروگبا برای دومین بار به چلسی بازگشت؛ اسطوره‌ای که نامش برای همیشه با آبی‌های لندن گره خورد.
👑
📊
آمار دروگبا با چلسی:
🏟️
۳۸۱ بازی
⚽
۱۶۴ گل
🎯
حدود ۸۶ پاس گل
🔥
۱۰۴ گل در لیگ برتر انگلیس
🏆
افتخارات با چلسی:
🇬🇧
۴ قهرمانی لیگ برتر انگلیس
🇪🇺
۱ قهرمانی لیگ قهرمانان اروپا (۲۰۱۲)
🇬🇧
۴ جام حذفی انگلیس (FA Cup)
🇬🇧
۳ جام اتحادیه انگلیس
🇬🇧
۲ سوپرجام انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/Futball180TV/101894" target="_blank">📅 16:57 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101893">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WWMCCMO8Knw5ZLO0IFrAJE_AmBc81rAq6f4QcRoUdPk8-Wu0i0NyURy12QW3xcKs4FgMjRm9hc7eL--1xaSnBuy92wAqNzB8sCoizVqOnJJ9R8aTwquZBZUd06dYxh0nAsL9JO3FbCOL8wHZ5N5hRXh4HYnDIniytMJEzO93Cj9lbm9Opfrk-yB1dfClH7etLjBPkBCVmV2-utU6osOnLkIS_jasUqNlwa_0FlvR3SZd2JOqWVAtCpTcEHvHvAC4f1giwCRWwNdjDKgokXlCV5y3tUclNXyJf7nEUXJUrQQaRUCXnwfPcKSyCsM6LoA-N84XwEOOSM1Vf8_842B-bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزش مالی جام های مختلف
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/Futball180TV/101893" target="_blank">📅 16:45 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101892">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
دیوید اورنشتاین:
آرسنال در حال بررسی احتمال جذب وینیسیوس جونیور است!‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/101892" target="_blank">📅 16:19 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101891">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a105d81352.mp4?token=a0WkG0ZGHOhL7owufHoF-R0xS_lFc6RSV73GLSgc8FeVdKkD9BMmovHZ_tXxuJkFXdaK5gycBK-3c6oDQXLIk9A_FnJJpBIKHUb5PPRPmehJdGzN78xdSM_VEfaiwvPx_yMFttYtn3ElIrwdBMsjJXxXop3PQgslXN-F7FvYbRunJOf9EgEJKShX_K8IGYcfb3T35wcPAeIoSeeYId3L3YCOvkhrQAD6mEypNDTw9GTIq7F8hLhJ3WvB0hdiS_8F79MN1D2Vu12eM2VAvVLj-l2itj0k8z3VXOhhH-mBoaH2fr1GjvMvTv8chqOd9lvVYZpp7dz99wLUnaQX6gDbrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a105d81352.mp4?token=a0WkG0ZGHOhL7owufHoF-R0xS_lFc6RSV73GLSgc8FeVdKkD9BMmovHZ_tXxuJkFXdaK5gycBK-3c6oDQXLIk9A_FnJJpBIKHUb5PPRPmehJdGzN78xdSM_VEfaiwvPx_yMFttYtn3ElIrwdBMsjJXxXop3PQgslXN-F7FvYbRunJOf9EgEJKShX_K8IGYcfb3T35wcPAeIoSeeYId3L3YCOvkhrQAD6mEypNDTw9GTIq7F8hLhJ3WvB0hdiS_8F79MN1D2Vu12eM2VAvVLj-l2itj0k8z3VXOhhH-mBoaH2fr1GjvMvTv8chqOd9lvVYZpp7dz99wLUnaQX6gDbrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بهترین مدافع جوان، دوست‌دخترش خوشگل
پسری خوش‌چهره و بی‌حاشیه، قهرمان جهان
یه مرد دیگه چی از این دنیا میخواد؟
😍
🏆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/101891" target="_blank">📅 15:49 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101889">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GTeW4jgxG5sPMGyex-_Jd3M6gixqjfSiy1IWc_QopK7GYAPJ5Saz0ntOKm_i6XacX3bN9G2RR9atthoS0cBtEtOO8MlH_TTnCjJH-ncxqiIVX8FyAyz042WNKkNwmkgHHK-M80PVY9nGazc9O-lLXOhlo6q3h7CnR3i3dYQD43vjoUqlA1wsQ01pAUNzodNcHw71Wty02p35HZR-grAt-roMHy4KLUkooEW_xXUoEKD_whrsQVXcK2_p9ANBaZBJGpM5uaDtOFe0pwxAJQ0WZz2naTWHE4m3IlUuulzlVMJgw5Xs5ShjQxYIRpSbPf67A4E9a0Jn4eCH-cJeJs-Osw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X8OAawdPKVhfmp31qDmd4tVEaNzuYhwJLDyADfIx9-giDQNW1e9P4jGSkHehFFBQL3XoVsF4SIl6bGj008KwyaYE3q1ePCSZoeqpma1zKv0b2uLqOl65AAJW676Fiui4OuIsWcfEmqw_4jwhAoBU2-Pa_lKM6YJH43paTRG61njUWmbznNZfA9F-xeBLCaROANbRPmtlv95z5OJ9uGUWEUGvYAMv7NjNFOPKWcSchCEEKyN3p0oWdGMuIHOVKyA7yx_gbmtrJls87lhQ5QKISKwcRr1IYws-GVvSkn18OnubkObBtO9MlIg1STQLHWbodXxpOtgFepp_rAjPBaJx9A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
⚪️
رئال مادرید و ژوزه مورینیو این بازیکنان را به عنوان بازیکنان "غیرقابل فروش" در نظر می‌گیرند:
🔺
کیلیان امباپه
🔺
جود بلینگام
🔺
فدریکو والورده
🔺
آردا گولر
🔺
برناردو سیلوا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/101889" target="_blank">📅 15:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101888">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lJBQEEfseDv_eHTPgr403MLByTDsuFeqMPbQ5LU0UCRXi9vdFXGyW2PpXdce_aEHI7pkiD2X62iaQP1qz1icwfQzdmmFvoIKPA7xHJFgwkQVVJqM73PeCTB5ExX0CXX8F2CskH-qJfFI793ZoqUzd68GF_LQ_lNqmvavnrHfdzzbvG4Jt7pUAd2b5XD9Dk4nSZUj_jZTwQk6UzKOaffn6dJyv_cBzF3mNNI7ZcE5uAfkDMKkGYN94dub6eg6D0lo4xLTNYY-AszVsvSbiLfkKAWNJRjuE_8lwFauQKTOEDgQRc0etMwdnLinfLhCnnRZU6qeuu6jOZ8cb_s6LMA5mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
فوری از فلوریان بلاتنبرگ: منچسترسیتی به صورت شفاهی اعلام آمادگی کرده که پیشنهادی به ارزش 100 میلیون یورو برای جذب یان دیومانده ارائه دهد. اما تا کنون هیچ پیشنهادی به صورت رسمی ارائه نشده است. و مذاکرات با لایپزیگ همچنان ادامه دارد. منچسترسیتی به دقت وضعیت را زیر نظر دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/101888" target="_blank">📅 15:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101887">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ji2279qBP-I9MZkztx1KUyx7K4KEnYMZBFbAZkm6s6LNLF3R25qvWRnEux3RL3ucWTMpUHgePkn9GOj302aEwKJwzUtG9aEtnDIMciGWlPzNcdidpEt4Cr8r0h5u4dGwDLpL-cWCSVcpxuboQoIHunKxJM8AXOEE2Jx_Ukah9U6I3nZa3SX9kVWqmFlPYjdEzkpYvXtEJmnjmADy50_rudIQQTlC2KU9hvX88tDwgakU4giBXALiLI_KYCicFlibxazbVigx1HWLn0gGam9XBzJxn_PQObkQG6sJ3mVtGpzCRw1Ap4CtK88goeKXXZWf9HxGdUZh0bmQuomHMnk-Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
هزینه تیم‌های پرمیرلیگ تا اینجای نقل‌وانتقالات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/101887" target="_blank">📅 15:18 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101886">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WPlRT1kvLqa-pPtHy__ReRnyyZXeAXy9ZVYZrY1GIBA0XLQeFXp8nizYGui3VHfAL1AJqEdAuK3pab0Gc7QCYUt3JWuECPaKFJJ3LWPEHABggHcMhE8nszk6ca_W3Xlx7i9uZIyPcuFuqT2BDU9r0UqjJXmvBbb8SEmVyjnKRowRxDDDOovdTyZR1KwCcRMk016I_tez_YSN6am5hLUYUDQZk2ey8XsgwUvvfyrNkWBDu2egQnEiyYD9btaSn_KRpM2v-FHfWESnPh8WO87hNRo5_zVetE5g-YsgV3DFiPXuduSeFxj4qi1h-jB33_cjEYOEPphS9DOHRqcpZDp-WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
رودرا: اصلا بعید نیست که اندریک این تابستون رئال رو ترک کنه، این احتمال حالا جدیه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/101886" target="_blank">📅 15:02 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101885">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G0iH2bFSPX28-XxwOrHFngUyKhDQPsLj0aoDUoF6srJvMw2q7wsdudpouy4cPUy99WqGP0r8frTp9C47Y3CigOEz8QAAuSMdXXvMFmpikpjWh-ruYtI4bky0OXHC3_sWU-CyFV_jcob4JzaziJHzpL_qprwf8k2dfT4G3U7TS8LQXzXVRsP5LJ_5dksNRg6TzeBg47OZCjABd5mLA9XYObcNU89r9uYxYKwcSDKikSTFQ3_SvhJt9PVsbWAdcy2hDQ-0l6gHCemW7PXTrwMzzm_lxc27_Vyw5-vy1AtO-diSq_CnvgsgxmpwGT2M0PKwGHjKdIOeBpKhBndZWoqlFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
سانتی اونا: رئال مادرید از شایعات مربوط به انتقال مایکل اولیسه در رسانه‌ها استفاده کرد، در حالی که به طور مخفیانه در حال مذاکره برای جذب یان دیومانده بود. حتی آن‌ها به طور پنهانی به مقر باشگاه لایپزیگ سفر کردند تا این انتقال را نهایی کنند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/101885" target="_blank">📅 15:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101884">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f29886b9b.mp4?token=SmWbuP02jwa9yhTFtchL7YM0WvGFOKNgNCNVqhL_HCvis1frqi3ckZSdxR4d-NUCLt7GVAbZptr3b8zz1X4Uzcq6pPBCAxlJRtzOq-L0IGtjqtUQXBcMnqo1EGdXDL_s6ITiAsObbJNN02j8ePvVBJul2NCYpC2z4wonfTxQiKVBad-b5aZl7n3qExvhxLDe4J7eXMESWxiqjmwA_yZgwCtJEpGr4eLQWt3OP7LFziXm4xlz2z-rqi0hFAiy_oKHH566mUyVbitKGzK66d_3aAnIQrgXkKMjbnJ8k4EVW6gbitLZMapwhm-Gl-dj6O0aJEaMxISPoYaoY4ULVRCyxLs_IvXp9aOjnOz-VpHBiAw1j5kfE0fVr2ocoGE1c5khuKA50Kc0xFCUmhJ57yMpC4MMgpxkzEOgL7KcICMHrRTA4zejo7Qcl-P5YMTnyCFWq7xizObShVn8GAzn9cPPOkBZwnK7Oz7cfoP1XuWO6bgHN88hWdrg-08oJth_gMb35_5ex67WYh346CfdHEhoerrEABI7S2iV0JSitdhnt2Kj2O-nSfFA9Fl7EdzMY69PQOq21zcGPTaUWL2_DCiKF2JhXcHnkkFkRH7YQod1_VYfWYr6uGA1QjhbxarS1RZiDZ5Sza9BQ1leFrm2ui2tUESM7wyud5m9hv0I3UpDMX8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f29886b9b.mp4?token=SmWbuP02jwa9yhTFtchL7YM0WvGFOKNgNCNVqhL_HCvis1frqi3ckZSdxR4d-NUCLt7GVAbZptr3b8zz1X4Uzcq6pPBCAxlJRtzOq-L0IGtjqtUQXBcMnqo1EGdXDL_s6ITiAsObbJNN02j8ePvVBJul2NCYpC2z4wonfTxQiKVBad-b5aZl7n3qExvhxLDe4J7eXMESWxiqjmwA_yZgwCtJEpGr4eLQWt3OP7LFziXm4xlz2z-rqi0hFAiy_oKHH566mUyVbitKGzK66d_3aAnIQrgXkKMjbnJ8k4EVW6gbitLZMapwhm-Gl-dj6O0aJEaMxISPoYaoY4ULVRCyxLs_IvXp9aOjnOz-VpHBiAw1j5kfE0fVr2ocoGE1c5khuKA50Kc0xFCUmhJ57yMpC4MMgpxkzEOgL7KcICMHrRTA4zejo7Qcl-P5YMTnyCFWq7xizObShVn8GAzn9cPPOkBZwnK7Oz7cfoP1XuWO6bgHN88hWdrg-08oJth_gMb35_5ex67WYh346CfdHEhoerrEABI7S2iV0JSitdhnt2Kj2O-nSfFA9Fl7EdzMY69PQOq21zcGPTaUWL2_DCiKF2JhXcHnkkFkRH7YQod1_VYfWYr6uGA1QjhbxarS1RZiDZ5Sza9BQ1leFrm2ui2tUESM7wyud5m9hv0I3UpDMX8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
امروز تولد هالکه و به همین مناسبت یادی کنیم از یکی از ضربات سنگین و پشم ریزونش.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/101884" target="_blank">📅 14:52 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101882">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dRi1gNqt7fZKNfpP4_J9sgJz5PI7wb9LQfNjOK2IzLSEo71YeKa3yHk7jGRx_QU027vJ2Y3eHGUFt2x2vb-1scQttoMCDneK_EBMzYZ9VGn-VdMbjQJimBu7bAO-NQDlIAgG37X-IeJrurgqEsseE9p4CVgZB_TEwWNYwSqv2Q1N6wvXzoU2U0fcG44iHxZkxfWHWNZGl8N3JUJCeLUw8lDOEjDsdQm7utWTblmCeD9PPNEbNYPl_SWvt4FuZZqg11Ykxi1IChucb7p-Ss2klFM6lq4ZG7PiG6PlVsMVNpDPiRDFkynrjDGMgJIHfLJ1fHxOSQbOvG3bX7Sn3YVghA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6342fd750.mp4?token=M-ZA5WEOu22uaFlokNH0xZAnn6S0tOZvFKOzEV9LLL7XEw8K8QoqkBLpHcBAhfIyIU9XtQVRfKwXLyBm_cgwiDRCgFkUcK_EM5aE5wnST0la3BaXPaTEkW-bGF28heH_dCfrZsBAyUkaTkzGsHKyG5xUwiyqmax0qN-b2LeKTEL-1uRjkgUA9x6cHyuj77P7e7PXW7dmsvTGFLLdLqMcrBYskm12ylO3FCNt1zUNMHMH9YCo8SKqrj5s7wQiRq_N6Z9VjbDE6AE6204aj8IAB9mE9nK43K_LQw1EYF3WPHe5H0wP_r7VDRAmb41ALZ7mcCaXgE8_7kU-UJIgFQz42A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6342fd750.mp4?token=M-ZA5WEOu22uaFlokNH0xZAnn6S0tOZvFKOzEV9LLL7XEw8K8QoqkBLpHcBAhfIyIU9XtQVRfKwXLyBm_cgwiDRCgFkUcK_EM5aE5wnST0la3BaXPaTEkW-bGF28heH_dCfrZsBAyUkaTkzGsHKyG5xUwiyqmax0qN-b2LeKTEL-1uRjkgUA9x6cHyuj77P7e7PXW7dmsvTGFLLdLqMcrBYskm12ylO3FCNt1zUNMHMH9YCo8SKqrj5s7wQiRq_N6Z9VjbDE6AE6204aj8IAB9mE9nK43K_LQw1EYF3WPHe5H0wP_r7VDRAmb41ALZ7mcCaXgE8_7kU-UJIgFQz42A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
هِیبا ابوک همسر سابق شرف حکیمی:
وقتی سال ۲۰۲۰ با اشرف ازدواج کردم، عاشقش بودم اما او انگار به من شک داشت و فکر میکرد دارم به او خیانت میکنم. وقتی دیدم نمیشه رابطه رو نجات داد درخواست طلاق دادم اما اشرف اصلا ناراحت به نظر نمی‌رسید! بعدا فهمیدم چرا؛ او تمام دارایی‌هاش رو به نام مادرش کرده بود و چیزی به نام خودش نداشت. این یه حرکت حساب شده بود و واقعا شوکه شدم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/101882" target="_blank">📅 14:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101881">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/356f27159c.mp4?token=PZpOjPAK7SSQl0ZntKnVyKbf5aKxUwsxD6bMAuUaOdeupwrVy4ZQJx6JFX4ioaOg0qGPMBhkTWADFWt0CryEkjoJ571-3x_OVjUxYYNeBmi-KbfvIAIWnC_SdOZ4TabjBG5pVaaYAk0meZ8ZQc7PZvqoPEMGHvjeD0ot5z7q3jGhdJp85ZXeKB_IPosN2M71NZJp3cyDwB21h4ZkBrUtnX47Mdl1vTd5syeQX4-yD2R9sucRsqCLEq-dPm1nLg4QtNs_4cFJVZ4EgJal-u_qhMaEJuITDzVTWxf6ioudA6miRK2da35ifwqchoYhlcUbBfaDFbWuY-rRDbMtwCoSQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/356f27159c.mp4?token=PZpOjPAK7SSQl0ZntKnVyKbf5aKxUwsxD6bMAuUaOdeupwrVy4ZQJx6JFX4ioaOg0qGPMBhkTWADFWt0CryEkjoJ571-3x_OVjUxYYNeBmi-KbfvIAIWnC_SdOZ4TabjBG5pVaaYAk0meZ8ZQc7PZvqoPEMGHvjeD0ot5z7q3jGhdJp85ZXeKB_IPosN2M71NZJp3cyDwB21h4ZkBrUtnX47Mdl1vTd5syeQX4-yD2R9sucRsqCLEq-dPm1nLg4QtNs_4cFJVZ4EgJal-u_qhMaEJuITDzVTWxf6ioudA6miRK2da35ifwqchoYhlcUbBfaDFbWuY-rRDbMtwCoSQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هالند لاشی تو مراسم عروسی دوناروما هم نتونست جلوی خودشو بگیره و مهمان‌ها رو وادار کرد «حرکت پاروی وایکینگی» رو انجام بدن.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/101881" target="_blank">📅 14:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101880">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SBNe8E5lPk_VZ3dWsi05q45E2sp5n8ea_HthLr9vmWZfEQd1WtsY14Acan0axWvJGcfVJFWvG61Pc2GmPgE-f-XpgS3ta-uX5CkbodjNsf7zYMg4zIdil2Vh7f6ww6uWGGq4C-8bUcBOS-kAPtrxiOjc6Bg7Nfnfdhtl8FS63vWfD_2MJ5lNIQDK33BkRkZSLdpRbrQ0yPzvHslyWVPmjKTKEwZ6vUbFS4qxTcLmyu7Fsq05hR1NeeVhIVFJiOkTK2q8OlGFAEZ4ScTcQCmpf9VK212e1239oLe5zQc6bx113FW-l6Q8CQa1RKLCxIDTo_s5efmFjOqtRnoCY4AWBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خط‌حمله نیست که ماشالا فلیک رفته تیم دوومیدانی برا خط‌حمله ش جمع کرده
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/101880" target="_blank">📅 14:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101879">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ff0c27865.mp4?token=vbJwYCxzGGfGsueE__bZ1Y6WPbRo0qdwXiICv6h0Vl1tD6AqQUOaK1egT5-MVf4JgW3hjOj2NiKOH3ieMbmS-CRBqCW2EfCj3ObJ_ZruY3zWLN8RZyfx_O4GPIVPqiWxGaYxpzZLpJb615GwfjC4D06bw_TwoABmw9Nl4ZzCKgMpr0qs55Ht5orfV51Ev7Qj9lSn-P2oFKcJ6Yk2rZHBRP7d5jffbbBAtXv4j6Gt9uhTmF2AQgty88XTMtCQ_6Aji4iM_JxVKILqt1eKPgXTIhSrqE-2M-PHY6UUSn4aCW6oZ35BXhIJD9ybY_zB747ejyaQ-tsR3T5_9tV80naqSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ff0c27865.mp4?token=vbJwYCxzGGfGsueE__bZ1Y6WPbRo0qdwXiICv6h0Vl1tD6AqQUOaK1egT5-MVf4JgW3hjOj2NiKOH3ieMbmS-CRBqCW2EfCj3ObJ_ZruY3zWLN8RZyfx_O4GPIVPqiWxGaYxpzZLpJb615GwfjC4D06bw_TwoABmw9Nl4ZzCKgMpr0qs55Ht5orfV51Ev7Qj9lSn-P2oFKcJ6Yk2rZHBRP7d5jffbbBAtXv4j6Gt9uhTmF2AQgty88XTMtCQ_6Aji4iM_JxVKILqt1eKPgXTIhSrqE-2M-PHY6UUSn4aCW6oZ35BXhIJD9ybY_zB747ejyaQ-tsR3T5_9tV80naqSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
صدایی که این چند روز تو ذهنمون پلی میشه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/101879" target="_blank">📅 13:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101878">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qm_P9ZEBOMs9wKsN1vFbwxjRrLffWfgnbY_d-1sBmuBGYXJG00gneeHJmK99Qzx6pTm0b0rufodh8IDVzhfpv9aL5hiVhgggyn6OKEQ0lzpVG2L8kVayagwSdlR2bDyklojavxME0hQvz3MzuvIsm6Fv8ZqL8la_EbZtCAaeGhTbDx_VApuGJDXr3a-wWsCjiRIs1Ai3devRIezxuuLtn_ytdO0CKwy3WiHATF-09mqznW08ruPAiZbCDIjTWFEpJZIo8H4Lfkp_cVUCuXUCJvnGfUdjhWwHj8I3zbpLZivTJ71rCJM9oaCShZ7et0boA8ipN0wYmmQ2BsncXR38xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤯
🇪🇸
ترکیب‌احتمالی فصل‌آینده بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/101878" target="_blank">📅 13:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101877">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc2d82d4a6.mp4?token=EjBmTNFbvbrhub_X_2qk-GkWOwSnQDyOM-yp-eiDfpRnAUCt2LIRpsV9SLi3n7zq0P3H4uf2GhC3P8KsM9mHS5g458FtC7T0_8W-q_60f3YX0ZcM8PeXXGbdInLB1eK2NG6lZvVl3sFwKvAzq0A9BDBQM9RGjHjPQaGrz2L-FVY4bmhdge_E9YUGDXQ6sTDqJMc-cb_h0PphguUJ5E85TuAtgX-T3gyWsWLqH72GX0itrIK5gvhXgD9zG6m6dTGEO2jYG-YRewTDujymH-CslXmjz6VbV9Y1xeFgs8ITwaLUBC5hxfRBYnCV0UNogXEMqb8RGxvO0LLZaisOLABcmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc2d82d4a6.mp4?token=EjBmTNFbvbrhub_X_2qk-GkWOwSnQDyOM-yp-eiDfpRnAUCt2LIRpsV9SLi3n7zq0P3H4uf2GhC3P8KsM9mHS5g458FtC7T0_8W-q_60f3YX0ZcM8PeXXGbdInLB1eK2NG6lZvVl3sFwKvAzq0A9BDBQM9RGjHjPQaGrz2L-FVY4bmhdge_E9YUGDXQ6sTDqJMc-cb_h0PphguUJ5E85TuAtgX-T3gyWsWLqH72GX0itrIK5gvhXgD9zG6m6dTGEO2jYG-YRewTDujymH-CslXmjz6VbV9Y1xeFgs8ITwaLUBC5hxfRBYnCV0UNogXEMqb8RGxvO0LLZaisOLABcmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇪🇸
مرور دودهه تاریخی برای فوتبال اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/101877" target="_blank">📅 13:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101876">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/705177dcef.mp4?token=Qg00_XwKwtUZ0pGuuw_1uM5q5zreHyt62k-6KIHUdR3lup5mQMz6rp5cSyIjKLnGYO8STlF2ulXi0kw4lX3_a2_1ThauxOtNQpIzh7W9h_sp6SdU_2svz5y_i5gCOQeX9QoRVkTZap9V67V6rAqda7b5SWV0dqNgRTuLj-X56V6LeTm9TjQrMyj-27mc_ZdS6aD3AVDrfbrvJbvAHr6e7mOco-p_Q5HneNsIsAavfY4uj8NHzUw4CtxR-9bomlw_wEEii4gbrCuXRIWDjZsXReMBfOawvI14VKKGwWcYojUp_P93sKyOW5t-6uO2RZOiVtupJQaf5FzetApo8OgpBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/705177dcef.mp4?token=Qg00_XwKwtUZ0pGuuw_1uM5q5zreHyt62k-6KIHUdR3lup5mQMz6rp5cSyIjKLnGYO8STlF2ulXi0kw4lX3_a2_1ThauxOtNQpIzh7W9h_sp6SdU_2svz5y_i5gCOQeX9QoRVkTZap9V67V6rAqda7b5SWV0dqNgRTuLj-X56V6LeTm9TjQrMyj-27mc_ZdS6aD3AVDrfbrvJbvAHr6e7mOco-p_Q5HneNsIsAavfY4uj8NHzUw4CtxR-9bomlw_wEEii4gbrCuXRIWDjZsXReMBfOawvI14VKKGwWcYojUp_P93sKyOW5t-6uO2RZOiVtupJQaf5FzetApo8OgpBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
عشوه‌های مجری صداوسیما روی آنتن زنده که در فضای مجازی حسابی وایرال شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/101876" target="_blank">📅 12:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101875">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/umyzVG54i-5LNigzlP--Mi0JkBegA_rSl_05mi-9AEeoVTkHA8HDX9KwhVpHEkkyvO2DvE-qtzb84WRt55E5jIYHRrspYw9EkIyDGjvimaforiciKdjyavPKe5TNinkRqRJLEO2dhO72nNmGbwxNoY8iHzVlelsKOGB98rpsPLpmajfKPZUzZVUwc0Iew2GuHJxfhDDT50ud3pW8i21gWsnpzuHeOG5ebvNUeq7dCQS5x5RsslgBSIHu79nBQPgkyEr5o9z0KDIhCDghGspgRMCKgR824WxFDAUIKXjWYR_yDdDX1IiBfUE4zUOenrP8MfdRxIpwasUU2WIKYbUeQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
متئو مورتو:
رئال مادرید و رودری به توافق رسیدن
حالا رودری فقط منتظر توافق رئال مادرید با سیتیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/101875" target="_blank">📅 12:22 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101874">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09d9c9fae5.mp4?token=eDAEZENAJoI-m_4ZH6_m-oE7O3_svBZ3jUAwK2Gmuc-RL91u5lbOn2Ks_XRrg4GsouoHQMpz47h6OrbjkF0LhSw1egjMgCtYJgseMYlxfIXtMQVA3f6GjLuAPOyxNJZ4T17JRheLQ9-3KAfQ2NXCT0JLT136j9C9yrpgHwkvsdid4ly2lIx3U0WXgszOjhjNyqhU24Lbcuo132NE8pM0hdxJfyRxYMo-rHijSZJ6EB5peGqDAzjz_79KOYZUe6_xEIuUHFvhwp-EyGB0ig9vIUwqcxuk5As5GI4dLrl1UgjrtLo2GyFyw9ZpoWCJbUW2OftN28s7gysQKvlqjdsYHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09d9c9fae5.mp4?token=eDAEZENAJoI-m_4ZH6_m-oE7O3_svBZ3jUAwK2Gmuc-RL91u5lbOn2Ks_XRrg4GsouoHQMpz47h6OrbjkF0LhSw1egjMgCtYJgseMYlxfIXtMQVA3f6GjLuAPOyxNJZ4T17JRheLQ9-3KAfQ2NXCT0JLT136j9C9yrpgHwkvsdid4ly2lIx3U0WXgszOjhjNyqhU24Lbcuo132NE8pM0hdxJfyRxYMo-rHijSZJ6EB5peGqDAzjz_79KOYZUe6_xEIuUHFvhwp-EyGB0ig9vIUwqcxuk5As5GI4dLrl1UgjrtLo2GyFyw9ZpoWCJbUW2OftN28s7gysQKvlqjdsYHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😁
🇪🇸
وضعیت رختکن فصل‌آینده رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/101874" target="_blank">📅 12:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101873">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cd5ea884d.mp4?token=WZr0xp8SmadnlVuVYduf-xJuIO_0xqCOzhzbR1NUPBRXw63826Lj5N5gBDouwB-9h2Zh0z0V6f4KiYBsMdzTlI8t9V6GHWhCYtbLwC4ctrhG3ccVfw8AH-_b-yEz5DVyNihMgHxvar1U3aReTGnWErEJ_Mo2qa8qMEuvVxfJOrCs7GBJo92PKpn9e9Yx7OBwva_sEx3vDSMQzRAN-WUAitMe37_OUHNk2OVLZK09bAmj9jnKlsaK3z8k9uZOqpX4g5o7QQhMbROMG8pFl_u1TbyTnQFcUuLKhxkXQCYPngWwZ_tg3UYScHa5oyB-NGM1HahenkKeS26HJCU2j46dMCufqPqH3AQYRimFZQn2uxETfH5Mbg7fEUZunBb0evpRS7i_5At2FYgod65eEIe3hSy_sFe0ahz-OggAZwM9wjHncp7vdJyUyvfRs3kL4dRZyzFXBV_J-mgSFc0ObAK9PYjSqv-a5B84KbeK61xGJgi3Xn2VO2bi9kWwb3qSfsTomRicLTOQeYjOyjuIhgDbx2BFz368aDL5di3wNp516JM-KCbADiBrVawpucJrRDLiVMDdX5AvVCNwrXXcEzvKUZrFL3_u4jTeuR4iXXvR87cQOMTH59d0-4KoWox1_cHK4qpIVec91wvDzRAb91txl6zB_XBMQrZnRJyVPW-4KF0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cd5ea884d.mp4?token=WZr0xp8SmadnlVuVYduf-xJuIO_0xqCOzhzbR1NUPBRXw63826Lj5N5gBDouwB-9h2Zh0z0V6f4KiYBsMdzTlI8t9V6GHWhCYtbLwC4ctrhG3ccVfw8AH-_b-yEz5DVyNihMgHxvar1U3aReTGnWErEJ_Mo2qa8qMEuvVxfJOrCs7GBJo92PKpn9e9Yx7OBwva_sEx3vDSMQzRAN-WUAitMe37_OUHNk2OVLZK09bAmj9jnKlsaK3z8k9uZOqpX4g5o7QQhMbROMG8pFl_u1TbyTnQFcUuLKhxkXQCYPngWwZ_tg3UYScHa5oyB-NGM1HahenkKeS26HJCU2j46dMCufqPqH3AQYRimFZQn2uxETfH5Mbg7fEUZunBb0evpRS7i_5At2FYgod65eEIe3hSy_sFe0ahz-OggAZwM9wjHncp7vdJyUyvfRs3kL4dRZyzFXBV_J-mgSFc0ObAK9PYjSqv-a5B84KbeK61xGJgi3Xn2VO2bi9kWwb3qSfsTomRicLTOQeYjOyjuIhgDbx2BFz368aDL5di3wNp516JM-KCbADiBrVawpucJrRDLiVMDdX5AvVCNwrXXcEzvKUZrFL3_u4jTeuR4iXXvR87cQOMTH59d0-4KoWox1_cHK4qpIVec91wvDzRAb91txl6zB_XBMQrZnRJyVPW-4KF0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
اتمام حجت یورگن کلوپ با هواداران و مردم آلمان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/101873" target="_blank">📅 12:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101872">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05d40892a3.mp4?token=an5uMYE6srWdSSmw6hXVxvltlwxuUi7L5RSz3Ig1PTKfz6hoNqCDCOezmm75nGRKlbKc5_dZ7PIQOtzIpQiP-Oop9QIuFWlYvU_sRd0yRZBLP7bN7YAwyOuZbdzrN0ecSPdOwlhpoEAvmw-j257fhicO1zLRR9FVw0FuleXkqMGihZXkGdek2e2J4NINYTOA-fVfVdTql-eViuqyyKEVse60-_nTPfiMbhZr302XknT3fvbum3WZ5F9Wjwf-La_AYhMVyPztgxSsOqlXO9x69xDWcBDf6LsGgQO5LIbUtokY0pnNP6KcNv9L6gVUTBtotyK0l3i5xEyLXc9-cyj9ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05d40892a3.mp4?token=an5uMYE6srWdSSmw6hXVxvltlwxuUi7L5RSz3Ig1PTKfz6hoNqCDCOezmm75nGRKlbKc5_dZ7PIQOtzIpQiP-Oop9QIuFWlYvU_sRd0yRZBLP7bN7YAwyOuZbdzrN0ecSPdOwlhpoEAvmw-j257fhicO1zLRR9FVw0FuleXkqMGihZXkGdek2e2J4NINYTOA-fVfVdTql-eViuqyyKEVse60-_nTPfiMbhZr302XknT3fvbum3WZ5F9Wjwf-La_AYhMVyPztgxSsOqlXO9x69xDWcBDf6LsGgQO5LIbUtokY0pnNP6KcNv9L6gVUTBtotyK0l3i5xEyLXc9-cyj9ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇩🇪
خاطره جالب مولر از بازی مقابل آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/101872" target="_blank">📅 11:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101871">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Af5xj_OlUq-VRosgAvjlXLCt762bo0BHB-tlQJJkc-m8S0bULU6jtef7p_C-zyFQa0rfGf0GLcU2VYUBVYjbKG_ZyvDxucHlqmZpZX8w18mWk8RP_iL-IYHsRTugsNtvv7M0p1FuUoVzKqF-l9Kc67KZzziWps7eqoTzWikyHW-HwEx3vvvAf-k-X-vqGCoLzqHr7DO_DchD1bkyvIXM9VpR3lKFbddgop1XONGyWmdHb2CY2Ge7YjuCBSeW_--5RWauYqR19xpi-Fao3cT9JBeKMe1IMuPBnndu8tqOgKH0AEX7bpCuypYSALzzIh-VpO9VWietQK0OgyrL0aMa8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لی کانگ این رسما با قراردادی به ارزش 40 میلیون یورو از پاری سن ژرمن به اتلتیکو مادرید پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/101871" target="_blank">📅 11:32 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101870">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kiD-eUyVOekC-xXFf10UdCV5gIz3-l_Fx1Z9lXamR-g1FgjMXHMSd9Dx_clxbNFhLi1F0nGXOI1goXjGSFC2urHac_oaLuESpRkp_TyD9ywf-mQ145gi7_wYiwFLm6sLITe2gFMvmr7K0oJk2-5h1Y-mHIQKA9CbiUAJ43rE7uNcBUEAY3irPIAve7rqRYo7pOPexsZOmp_JcIkPJMZ4rizMbYs6RHC_MW7mrw2zEssP8TSeq4QQA65jdcLWh1JoSMPfk682XFEWT0BTRHs8EaFBToPvYT0AEmay6xXqU3U5MCVS5-cLuL1cNSVRSlz9eJ0tZWC4XtC5HkBL5GsHGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇷
تحقیقات سه‌ساله فیورنتسو سانتینی، تاریخ‌دان ایتالیایی، نشان می‌دهد که لیونل مسی ریشه‌های برزیلی دارد!
بر اساس این گزارش، جدِ پدربزرگِ مادری مسی در سال ۱۸۹۹ از ایتالیا به برزیل مهاجرت کرده و پس از مدتی خانواده به روساریوِ آرژانتین نقل‌مکان کرده‌اند. همچنین در دوران اقامت در برزیل، نام خانوادگی و برخی از نام‌های کوچک اعضای خانواده تغییر کرده است. این گزارش تأکید می‌کند که پس از مهاجرت خانواده به آرژانتین، دیگر هیچ سندی از حضور آن‌ها در برزیل وجود ندارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/101870" target="_blank">📅 11:32 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101869">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/917b2cd572.mp4?token=ZaZEYzh_-MUzWfUUw1K4-058GTbofNdKCT1D4pMTnuXmGBhHxGP9D6owyVTE5h2tSRvpNS3r7ECHLuNbJ6JUwKPbNyHVUaDNyiZ0qmWJpy7BJsVX8JhU8Krd7O0wUC7hiPkYwWkw5k_rDWNU5yg23wQNL0n1q_WcZXnsx-G7PyYz9qoFOOCXg_MvUlV6ba_NL9N7aZ7WHF_HyogWm2_y_4UEahV0I_WBDMTG-CmCE3TuV5B-KxRe5ompOkQLx_BikQ_OtG-bAprPfDCV7WB1fO1zs2jQdpRnPUGyh2BhqAgmP89WtrgiV_4rWdyi-PZPW0oh8GYkIJqISORGBc-xo1MdO3MWLo9_Fd1lsRM3ZUXAozHXmXeWipvFx-sEvhLMvOk0osut46P6DK_A8-zy77hr6QnKJwILKl4hNrjcmPLv1G0qgGCX6zzhjRoQf7RCiyS11PiBX_nAGhtCVRvazfSK1zLttRJRwVb3XFMaS4lbvkPUmv-O9WXTt0Jf45GTT7yoOn2zyytU6uSHsaTfMC4oKD34GUlrDFDQJpzHX2aGOjHd6LBGblAT5XzpyBCEYZ5vr2wG2Z0ZQgYPtOmQGE4eAxdqMqgFh62jKFtY9I0SkpKSIuFNeJpNQ1SsabtU1qg8YemRI7YKvsu9Y1rutbkpQBPfgJgs84hxrn3u_xA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/917b2cd572.mp4?token=ZaZEYzh_-MUzWfUUw1K4-058GTbofNdKCT1D4pMTnuXmGBhHxGP9D6owyVTE5h2tSRvpNS3r7ECHLuNbJ6JUwKPbNyHVUaDNyiZ0qmWJpy7BJsVX8JhU8Krd7O0wUC7hiPkYwWkw5k_rDWNU5yg23wQNL0n1q_WcZXnsx-G7PyYz9qoFOOCXg_MvUlV6ba_NL9N7aZ7WHF_HyogWm2_y_4UEahV0I_WBDMTG-CmCE3TuV5B-KxRe5ompOkQLx_BikQ_OtG-bAprPfDCV7WB1fO1zs2jQdpRnPUGyh2BhqAgmP89WtrgiV_4rWdyi-PZPW0oh8GYkIJqISORGBc-xo1MdO3MWLo9_Fd1lsRM3ZUXAozHXmXeWipvFx-sEvhLMvOk0osut46P6DK_A8-zy77hr6QnKJwILKl4hNrjcmPLv1G0qgGCX6zzhjRoQf7RCiyS11PiBX_nAGhtCVRvazfSK1zLttRJRwVb3XFMaS4lbvkPUmv-O9WXTt0Jf45GTT7yoOn2zyytU6uSHsaTfMC4oKD34GUlrDFDQJpzHX2aGOjHd6LBGblAT5XzpyBCEYZ5vr2wG2Z0ZQgYPtOmQGE4eAxdqMqgFh62jKFtY9I0SkpKSIuFNeJpNQ1SsabtU1qg8YemRI7YKvsu9Y1rutbkpQBPfgJgs84hxrn3u_xA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
درگیری خونین و فوق‌العاده شدید در لیگ امیدهای فوتبال کرج؛ مملکت بی‌صاحب همینه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/101869" target="_blank">📅 11:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101868">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ClkTkrriDr2LNiXkVc2-acuHd3NVQuC7PXKOwNw1efC_Ahgmb20jJglxfN-57QIQzJCvqAyYejmbq4kbz85hDEcyCima_gl9E5wMpZIfaapN77o6Lp8i-hn7jOShvTmCuCs_euExkSWtc6Xp35yQMyx7xWtjcZ2oB3sCeNsPUCc490iW7BIKQkBZjmE7ESJjP4Mm3EmTiwWovYZZj0jlv96rzPHUB8Hpy1PwFDQzeuOhNd-HykSFMgK9q8zehGnK60vFERmBs4F6crZf9zrgHCkV0Tz2Y84LtoIDFJ72CMjWGUSyLgni2iqkMFL13F26ZCQggvGFMHEzzM0Y2k_apg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔝
👀
شاهکار سرمربیان اسپانیایی در فصل‌گذشته
🇪🇸
🏆
دلافوئنته قهرمان جام‌جهانی
🇫🇷
🏆
لوئیز انریکه قهرمان لیگ‌قهرمانان
🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
میکل آرتتا قهرمان پریمیرلیگ انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏆
اونای امری قهرمان مسابقات لیگ‌اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/101868" target="_blank">📅 11:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101867">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f4c9480c3.mp4?token=b2PxyLBpzdRPMtPK1GKkH7LAtPkDog-Vy0LLYt0trrweeZ4lSRg8fjOHg3gw2oRGBDtEJ0RAKVe4-WCgT3edPvifwsagUu4YIsRMRdX_zkWjhmOE753xe2gol2pJxYHfuWRTnhUorYqX4NJEprE3jLW9RYlMix7JQE5QA0rLas0MuZ3i-MgHz2vIF46BRmOwAMwE0M3bVNwLN2PHNJ6dtF-ddrdMpjW8RLm74nFyPQhWnkZhvmGuECXLd6de_OQak52MwutHLL4wSJQLht3ai_zL6I8lztbBk-iTv26NAnxiUNSYSezGWwLUn28JDx2p2_vXNMwDLDyyc4a6hTc4iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f4c9480c3.mp4?token=b2PxyLBpzdRPMtPK1GKkH7LAtPkDog-Vy0LLYt0trrweeZ4lSRg8fjOHg3gw2oRGBDtEJ0RAKVe4-WCgT3edPvifwsagUu4YIsRMRdX_zkWjhmOE753xe2gol2pJxYHfuWRTnhUorYqX4NJEprE3jLW9RYlMix7JQE5QA0rLas0MuZ3i-MgHz2vIF46BRmOwAMwE0M3bVNwLN2PHNJ6dtF-ddrdMpjW8RLm74nFyPQhWnkZhvmGuECXLd6de_OQak52MwutHLL4wSJQLht3ai_zL6I8lztbBk-iTv26NAnxiUNSYSezGWwLUn28JDx2p2_vXNMwDLDyyc4a6hTc4iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🔥
🏆
رقابت‌نفس‌گیر توپ‌طلا ۲۰۲۶ در یک‌نگاه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/101867" target="_blank">📅 10:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101862">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KZf7ji4P2elSKJ1k122n-MKoatVIuxprC9Q4ZtHeTx6YwbrEYjav_OKwxzAYsBVm0tqtAFr-UaVoYI5K_nYwCMFH9mOZiisAnbOwu3LOLpzBYDaJi3eHuTWQLDd9CICPySm8KuX2IJhOrzSXFsiWLN8kl7FFJE87R-Lvr9yR-eFBdNi0LQwPCxEWoshRwE8xb2pD8JjcbwfL-97t9sdmqoB7s6x_BM-2h6bVaLSCwsIzsFrT4FwoL-ZJEB5nJ1l3p0O8qf4gUxbPvrb88mnoCUPh3lV2bxrOzr0TPSWguwiLDmOCgXNe0kBfaA2E_mlnY9LrjAfT8vmVmr8QwEeZGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TMi0dRIBdto8lbnFO1uS1i1XM-53CMrTjlFftfYI01OeOiR9-i3_OTE6YxObH1ta6twoAm6WTwdltksBIrxtuvh0ehV7IPDGFNxqqZIlkQD69F8RIeK3Ksi6Vok4jzSa3S5ku0gXoSmIA4ClJpD2_Tad5OVvrotloKMo0Y-eISLpDsCvW5_9jtkoHkB5r_fOI_Y9vZ9NHEifZtrWkNMysxhV9x3G2H5CBQnUoCjMnt-1H8j9E3OgV75wg8YWO6sp9aw6yL9xyy4pzyfEg8OoqcFcvkWp8yuLmCtoSZ1idul54jIs1cNW6mmvAVicY-JDnnBhfZTYKJ9YSBNn88Z3rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZNyOoveo_Ju7CFdcYUN6Lb_trva6yFar8WRg3V_hdnWHXegThlw4N1ohoRkkoSams-V9mGDQj-gJgwGi_yArEeWAIH25KQ0qEKJ1Xicx78heHpiAgsBDDMc0cfYLyUYFcLiMEnIXnMD9_Y8ep3uY4MxFsmSB7AfpyWG6a1r3SNTyAooAHq6qB5JE-Bhn_scr6_uK5LOO9qTlfuWevpSsk_mwS_f7oWfVZIBiuKDvQOWk69qsw6lf7BYVzRc7bG3b1tKn59dFdn2lVP_Rj1Mf_d6oXvrJGvO4vlqzC4ev_LfcUxfqIgZt4uhGs1Loz2mcahbc11GLf-QwxX582CYEsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TS2eWv3ucHYmQKyjUxMGzdv7FknQG5NujEhUIhg5dnncwR3WRcaIwtuDu-wKkSp1u9ulslk-RqNRp1Rc_zbIHfZjv3H9V3hfHZrHfFG0SlqOltuELSla5VfUgl3n49oDaacZHIQw4ov07NdfClcBf9CTnck1Fx8HM3B6ZxuuQXX9C599NHYHoEHL0aFoOSCMploCHCXd6pzuhqr6aW41apisZgnzKUvkEcJsq8_j0Kzh_wRR5OVBynxTzcJyNfYf0YguQ7DrTTZdlgd5b9AG8F0-qgf-29osBvSv5BwqYS-8VIUcsAcgSd6KgGaV3Lpps3yy5uy48lfpuiUSvn0Jmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GcWzRMG2s3sr0-zQE9dxEcv544LE4h0AjqX3Nxo7CyMRoMFTM_LrVQLR528MPRV19JWy9fKGK0hGvccugGjnuf7qpGLFHuCH--xVKVe8V8ReJjT1lSXpjz4UvJs7T8wQXKmAYl5RYnj80yOv3ETVFaE4Rj8F8qtXumgVqW_uykUNlJoRawRK5Vc1RhSTLuPew8UR-gjCOUzMjhdRJjCqIne4mLCmC83PFv1H0WdY-ZSN2o0jVQsIlyT_jqNwPvVZJ-mMyGbAW-HOpzzePKZ-FHJAekNiv11g7kSbJ57KwjN6F23Z-aUtyJXXMtgUAHkMomddCcyOnJxuOr_NtONfqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">+ قدرت تورم :
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/101862" target="_blank">📅 10:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101861">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5d7ccd208.mp4?token=ih9kN0VwiJtXQ-NCNyv9C1aBPSckVmMHhuK875Mps01WWzKwp2u4ql_5CQKF1nLmikp5XID63ga9PeIkIGAAhvvc4H5oH50Rpb5SVoJduW6ISEZzIt7oVGI7eklzjCeRJ5zSHjG0HfkegH89twjEsu5XNp48tmXEeBEoZV4mjl8rL3rS0Am1i9V6Z8mfSxy0DGcLWGKZpYIZZJzpRm15QHoEYdKXX41tPWlzBun9XZ7pM5KlIa1iNbT6NVJK195O_85OyJceaLLgDQITVU7YrAD9MEmjlu1LYwdUnllVVvl9DBrLQ1v57Gr4J3Xmnn2peRBkf7YlP7X6LN8Bc2xZtg--ZedjP3D0FijTDUS8J3cV5sztOx7vv6GvGbK394PI_GD9oOkbEMMpF6iIfKN2jUgMdjahA3-pkP48UmvmYtYpvua3nqXxMe-biOm_4aKLvndKLKjSpkTh_vS7pQEkGAD2AMbnWW8huOik4uTf3aXHzSg9nix1GDWB0Bc2TkWaaBoYaq5nDAnIra4LqnFhbGK78IpfilLgVgY0NKq0UZnU3raVwRNH_vB5IuDSKhOllAqG_iCXgyKvGYM1NDrI9fzAjhyr5mldcls01i67MxVdVx5jBi8AuhJronyKMVS90J_Cd1FYglvRKMqY_kekgCaUVS0J4UcSyNK0rXifIIM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5d7ccd208.mp4?token=ih9kN0VwiJtXQ-NCNyv9C1aBPSckVmMHhuK875Mps01WWzKwp2u4ql_5CQKF1nLmikp5XID63ga9PeIkIGAAhvvc4H5oH50Rpb5SVoJduW6ISEZzIt7oVGI7eklzjCeRJ5zSHjG0HfkegH89twjEsu5XNp48tmXEeBEoZV4mjl8rL3rS0Am1i9V6Z8mfSxy0DGcLWGKZpYIZZJzpRm15QHoEYdKXX41tPWlzBun9XZ7pM5KlIa1iNbT6NVJK195O_85OyJceaLLgDQITVU7YrAD9MEmjlu1LYwdUnllVVvl9DBrLQ1v57Gr4J3Xmnn2peRBkf7YlP7X6LN8Bc2xZtg--ZedjP3D0FijTDUS8J3cV5sztOx7vv6GvGbK394PI_GD9oOkbEMMpF6iIfKN2jUgMdjahA3-pkP48UmvmYtYpvua3nqXxMe-biOm_4aKLvndKLKjSpkTh_vS7pQEkGAD2AMbnWW8huOik4uTf3aXHzSg9nix1GDWB0Bc2TkWaaBoYaq5nDAnIra4LqnFhbGK78IpfilLgVgY0NKq0UZnU3raVwRNH_vB5IuDSKhOllAqG_iCXgyKvGYM1NDrI9fzAjhyr5mldcls01i67MxVdVx5jBi8AuhJronyKMVS90J_Cd1FYglvRKMqY_kekgCaUVS0J4UcSyNK0rXifIIM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🔥
روتین تمرینی لوئیس دلافوئنته‌ی ۶۵ ساله
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/101861" target="_blank">📅 10:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101860">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/025979a7c1.mp4?token=rGSzJa3v03gi9yQNVeWV0mR1KSkYHY-ygg1drETNWPjhYWs2vszd_Lutc7NGP-21Wf8FPm7WTNMcqpDKwv5Cuhzq_ogTr3GB-vvC65HxByIJuLsDotg--I_smFw81mnsmQJzw5vp_bhhHpxk_47h53KCkddiBDzuN3W2hKp4RjnfiEl3E3e8H9hmt3QyyPA36MKG68eUSFE66E0m-MVBZtIdVMf63t85tf2Th444yLktWrJO2zXfNjzHD4cXfAjL57AGDFVnamlZ-_2meh7KPo-DAi5ZEqUKOhq1Ce9n214LY6u39mqxy3rltUoL-thJs7CYLm-Hsf7qOewcuPzJ3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/025979a7c1.mp4?token=rGSzJa3v03gi9yQNVeWV0mR1KSkYHY-ygg1drETNWPjhYWs2vszd_Lutc7NGP-21Wf8FPm7WTNMcqpDKwv5Cuhzq_ogTr3GB-vvC65HxByIJuLsDotg--I_smFw81mnsmQJzw5vp_bhhHpxk_47h53KCkddiBDzuN3W2hKp4RjnfiEl3E3e8H9hmt3QyyPA36MKG68eUSFE66E0m-MVBZtIdVMf63t85tf2Th444yLktWrJO2zXfNjzHD4cXfAjL57AGDFVnamlZ-_2meh7KPo-DAi5ZEqUKOhq1Ce9n214LY6u39mqxy3rltUoL-thJs7CYLm-Hsf7qOewcuPzJ3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😐
دلبری‌های لامین‌یامال و‌ زیدش بعد جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/101860" target="_blank">📅 10:04 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101859">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/552820f16b.mp4?token=g-WFp1-UEIZJPowMEvkRjoUf5U4Ao0zuIoPIoRiPnEGUqxgPZiScZHstsXAAdzcWCFJZH2mpUDIAz3dWvHVgW55EtCBG5RVE0JEgtIfJjW0-Yjdld4_h5gui2kWOOZr4sMeEDo6Vm4ukYhlNonyrzeWovUAucAgED7mbLvBVivYCvHue0zzHo90EPNiK0wZUfEu-3fsHvzvdo0DBMObXnh4dA41M57sKxE0M2UjK6TKjtnXMGcpNq446FKsBTfvML6u27ID_Xs-L6S1MW7gBfeU50BPqjy6-xmBIY4Rp5Gnw7d_EOe-2PX6OnN2eSDrCK_yrd9m4VVcEqWlHi2xNOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/552820f16b.mp4?token=g-WFp1-UEIZJPowMEvkRjoUf5U4Ao0zuIoPIoRiPnEGUqxgPZiScZHstsXAAdzcWCFJZH2mpUDIAz3dWvHVgW55EtCBG5RVE0JEgtIfJjW0-Yjdld4_h5gui2kWOOZr4sMeEDo6Vm4ukYhlNonyrzeWovUAucAgED7mbLvBVivYCvHue0zzHo90EPNiK0wZUfEu-3fsHvzvdo0DBMObXnh4dA41M57sKxE0M2UjK6TKjtnXMGcpNq446FKsBTfvML6u27ID_Xs-L6S1MW7gBfeU50BPqjy6-xmBIY4Rp5Gnw7d_EOe-2PX6OnN2eSDrCK_yrd9m4VVcEqWlHi2xNOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
👀
⚠️
بی‌توجهی یامال به دختر پادشاه اسپانیا که در فضای مجازی حسابی وایرال شده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/101859" target="_blank">📅 09:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101858">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5533cc045.mp4?token=FfxaSAmufogAay9o-JPNb8QuZ4f4u4G41cGTQpGltE1UdGIwHFA1W6t0YvKikjj2A8PRkPoAupzwbQUoJ3hHni9X3znT8_G2p-3ZCmEXXQeGgdegvGUsd89S10cyLXoYY7Ek971BYYcwXrJ-OnTyWLmxardQ4d5cpzD6oSVBLtG615VDQni5n1RNRQbYqdOOJmX9b_JKgm9bmnV_YxuSGk4vXCSX6hnKCNWefZmmBu_3fmhcYs7Sm83Gy4WRfIdlZltzrcdK4qpGR4PqOUmdylBTV2GiQWAJQwu1oyKvFeEdrxAUjskS11EIiXHhyilay2_J_GENocA4B1m4jYyfpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5533cc045.mp4?token=FfxaSAmufogAay9o-JPNb8QuZ4f4u4G41cGTQpGltE1UdGIwHFA1W6t0YvKikjj2A8PRkPoAupzwbQUoJ3hHni9X3znT8_G2p-3ZCmEXXQeGgdegvGUsd89S10cyLXoYY7Ek971BYYcwXrJ-OnTyWLmxardQ4d5cpzD6oSVBLtG615VDQni5n1RNRQbYqdOOJmX9b_JKgm9bmnV_YxuSGk4vXCSX6hnKCNWefZmmBu_3fmhcYs7Sm83Gy4WRfIdlZltzrcdK4qpGR4PqOUmdylBTV2GiQWAJQwu1oyKvFeEdrxAUjskS11EIiXHhyilay2_J_GENocA4B1m4jYyfpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😔
امباپه‌هم دیروز اکسپوزیتو رو برده یه جواهر فروشی معروف کف پاریس و براش هدیه گرفته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/101858" target="_blank">📅 09:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101857">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kTNhvBQ44_ajb0iFPif2skqZv2-IKly2USJA2e9nzWW9oMEpkE-UHIspJw5ZMiGLR-vT_d5weL585wmt8aISAYZivQqojE-pMaEGNl_SiIdJLYYORCFSI3aTFIY00KnG98BOBXos2TGGd53SXBbVNdn5v8gL-maPpGC4RIFgUS2EPmkSDNp74m0RwU2GYG5PiYMFGmvBbRpmZ_iPVea3rMhCsINrZT6eTZmVGeNnr-sVBYaFXPcN1rpB6-3hFCFDxlqwPOkk3tDCCnzXjeirSTiGBPPj4Y6Mr891nHEJzzUlEQIYyJW0RiCb9TbWqmzDtAvlCJ2fp1jSZ_ViszyI0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
✔️
تمامی کاورهای بازی FC در یک‌نگاه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/101857" target="_blank">📅 09:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101856">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحامیان_جبهه_پایداری</strong></div>
<div class="tg-text">این یکی واقعا معرکس و حسابی زده توخال!
#من_نمیتونم
@hamiyanpaydari</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/101856" target="_blank">📅 09:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101855">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">❗️
▶️
کلیپ‌فوق‌العاده دیدنی از پایان برخی از اساطیر معروف تاریخ فوتبال در جام‌جهانی ۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/101855" target="_blank">📅 09:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101854">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2e5fe7985.mp4?token=NZTX-bKLM_KrdNwdhzm5Jp9NFj5o5sVTID2_TtpBKYQO3gRNAVc4ui4QYUkC78jbLl8v7_0pE5HspNa5mVI6jIYE0vATOzbxS7YQ1Jm8nsaosC48jDfXKYD0goCWDFAE8PPkTS-nnxVglS0fQ6stp3KI7rLqHqlaurw4zS2WG-9lQRtC7Evy-ZCjV812UuzE5UaC_-KDGheZCq7MGFLu8Nljb7BJAlOpQQIUUaWEXPJ02Lh4fKirdEfa4Tg8OceHxpJTf-lR7xIhK-_9ngslEzTh7cCGINs4afJR0RqouN9fXMDjlz6sLxTEjkUVfnMEaQ8hJkUxytxHdmOGKaiJDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2e5fe7985.mp4?token=NZTX-bKLM_KrdNwdhzm5Jp9NFj5o5sVTID2_TtpBKYQO3gRNAVc4ui4QYUkC78jbLl8v7_0pE5HspNa5mVI6jIYE0vATOzbxS7YQ1Jm8nsaosC48jDfXKYD0goCWDFAE8PPkTS-nnxVglS0fQ6stp3KI7rLqHqlaurw4zS2WG-9lQRtC7Evy-ZCjV812UuzE5UaC_-KDGheZCq7MGFLu8Nljb7BJAlOpQQIUUaWEXPJ02Lh4fKirdEfa4Tg8OceHxpJTf-lR7xIhK-_9ngslEzTh7cCGINs4afJR0RqouN9fXMDjlz6sLxTEjkUVfnMEaQ8hJkUxytxHdmOGKaiJDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
✅
علیرضا فغانی: هميشه خود را كنار مردم ايران مي دانم و از حقوقشان دفاع مي كنم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/101854" target="_blank">📅 09:02 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101853">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JNALgOGXUv59ujA8qKZKMAfnc0kQSuLrlitaDLgCrQY8mT3VsWJmHImdNK-WVZ56UJxRgbQ46E_l6OG9y30mrr1oMGy-YhxrCnRMenC3_PVAJmCeITL5u_6cYH5NfA1idQnrUKZBkjx0FU_0bmwDNRplJbQ0DisLAshWYT3nqxY2jtykAXc-8P3xwlK5WT5MS8jBYWLDwc3yAZA1Bab9mYpx0ornDXgKQsQon0Naad41xJpf-AEl24vxFV-Sp6TQYs_svT_UvyJ5mjXbl0lTrqSWxsVNx-ZJ4TuIi67_wm8auGyQqrV8gQkMkvZSps4gQJpsApoqX-9muJc4eXwVGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
رسانه ESPN: رئال‌مادرید تصمیم گرفته که به سبک بارسلونا، شاکله اصلی تیمش رو حول محور بازیکنان اسپانیایی بنا کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/101853" target="_blank">📅 02:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101852">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be7211acfa.mp4?token=gha5Gup9AWk28a96mlAumZ2LinbP02xa_qVmhvlteLn14RoL9o2Lbb-w1CbNHB1k6O5-9CbjSWnZhXZ2ZGFAeJFSthNrSfZYHAkFek6xHySfjoganF4K7j2uDR4GxxvElvWEECYXxc8S2wXw8k6tYYnQJf7eT9CKXpE1EA65jcF0v6tcT-QawyxAte_zpVYV46IEMZcbXSetp8g6eFpOo79Nt8-1XaN13Rc9PVaCMKvmV1iOgm0eD5fvh4gjaXuWfT-Z-9egOxV256vuI-O_om4acX9sSbt92KCDgymAnWnNSzRxCTXTgGTFNSn576x9E5910p2i83b9h8oRRUca5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be7211acfa.mp4?token=gha5Gup9AWk28a96mlAumZ2LinbP02xa_qVmhvlteLn14RoL9o2Lbb-w1CbNHB1k6O5-9CbjSWnZhXZ2ZGFAeJFSthNrSfZYHAkFek6xHySfjoganF4K7j2uDR4GxxvElvWEECYXxc8S2wXw8k6tYYnQJf7eT9CKXpE1EA65jcF0v6tcT-QawyxAte_zpVYV46IEMZcbXSetp8g6eFpOo79Nt8-1XaN13Rc9PVaCMKvmV1iOgm0eD5fvh4gjaXuWfT-Z-9egOxV256vuI-O_om4acX9sSbt92KCDgymAnWnNSzRxCTXTgGTFNSn576x9E5910p2i83b9h8oRRUca5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
‼️
🇪🇸
شروع‌قدرتمند آردا گولر در ترکیب رئال‌مادرید برای فصل‌جدید با خراب کردن‌پنالتی امروزش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/101852" target="_blank">📅 02:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101851">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QqBfL5eXffk83RIOptdjjsekAKpKqqa_WKRHvwWvf21h_CHcAU6DFE8-IwT5_8QHh-H2rdRrbu8SIAKmMM21aRwRVm9Dk3XGKPyGlXbfJdOH3e8hMdIhtcmjjJ5whEE4i2bwiYTZGif5ZDIsJut2vbhKTM1HIVwOLOEW48_iFeRHOWfSNfGNTLtvOd2nPeU36w3KAqP0ma89nAGs7D9Ll_wiJx4qoU6H3E4B8qgj2jz3Cyp7xRe6p0XPUgidcFdxZ5C0psFTu416pMftcnmI2C_oO2eXe0CQ-VSvUEqYC4YSavV3AEG_I7eugiaea4gLPIPAL78FzzRlbzgl3lf4YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇻
بر اساس شایعات منتشر شده از منابع خبری آمریکای جنوبی، ووزینیا گلر شگفتی‌ساز کیپ‌ورد فصل‌آینده به لیگ‌شیلی خواهد رفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/101851" target="_blank">📅 02:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101850">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/c-dxPaReRuS_mY1ZdYhm7r1tGjq6MWqQcB7KFQY49ipWzZ35Bvw89p1JgxaN4oyCR2sJqcsE9yUhclbHfL0-4mtwfXntsCJDYGPwsFiH0b4L0Z8XswqlsYxqsZcxM1hgxr3TELR9IlnHZAtUwhHbnUVEKK-baVhIUXNJ1ZGAn3DZdkKHOixN7yJZFpBuIsE6deUiYsVgVmZ-9n-9nORboljarC3jbv3vBFbURaqWNW5XZheKDnXu0XPBnv-gVvGaxQX9bao6EUmV7kBiNxnsp9f5AJ9V0tFpRBSUWUZHyFirtZbJklowJWh0zrliGICWh98OgPTa_dZ5V9n1IYC1jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/101850" target="_blank">📅 01:28 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101849">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/InQHS0KkRbHwSywQIGB9B3_xPZv8ITL1bDoYJe3E9GSty3KykZVQnJR8TBmLXyx7Qg5Qa7g0pZb8k3YAeZkE_nO7Ff4e854F8X0u-bonUp0NSheIZKkOS5bieq244UdaRXhuoqmkwQd3WIwkdKVbE8-ivznpin8Zkz6n4ktO5NhwkJpMTsHdQ9l6Lpr8nNVCWyJkq6H7n58738xAQgM0j09Ab2ohxu7iryaE9LtaWQAUbKmVN6Sc21M5AT8fQV2Xcj5XZTl4opACx0B3dQDYL4v0vBKC2MSyyZWUQZrWT-JdY-y3jiTU0r_y6KJ39eIDmts5_1gRHj2EOR4L28OhDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⚽️
🔥
🔥
🔥
مارکا: دیومانده تایید نهایی برای حضور در مادرید رو داده. این بازیکن به پیشنهاد نجومی پاری‌سن‌ژرمن دست رد زده و گفته که فقط به مادرید میره. مذاکرات فشرده برای توافق نهایی با لایپزیگ درحال انجامه و بزودی خبر رسمی میاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/101849" target="_blank">📅 01:22 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101848">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eiy0tLkafz6e5NlgE8OZSAEMIPYxqD3yByegkuWZSDo8mrUrf8iDW4CGXfHaBbj-cauNwaN9W-zLc0OSHIXtnQMp3rWYH6J0fmiNKXZF1YV4PyA5F3yuQP4O-XAWDFfU8nyHW7TQu-ncso0vkTT2avCyTdygfRuLxA7e8GU1m9G4oyInNQJYgcjbEnH6TFijjtw4-SArep7PATKU7ys8_NYS-34GI8mEge94dy3bnVS6mmcdRUb4k-UON7AGJMvDygYK-07hML9nT78MErKUswbpDrfXzI8dK8EadpM4hmXONJTNezO12LUf3FOv7DPKu_fzOfffJhZfuLFvA7bepA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
په‌په‌آلوارز: رئال‌مادرید و ژوزه‌مورینیو دیوانه‌وار عاشق دیوماند شده‌اند. این تلاش پس از ناامیدی از جذب اولیسه صورت گرفته!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/101848" target="_blank">📅 01:18 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101845">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EAI7ucwi1x_gDmhKAbBnyUzCpOS5JSH7SoJ-79ghUx2VQ8idGPdg1r_erIIsXszmr9JMPRTHXdJbpb0H9k9EMPiNCucEvuCo3ZJAxDCJiw9HIKqnqEsTcNIDBFnKULWDCP1Zg0NumoVt2ZpFEywflFpw6EqCZMDtCve0rrSdxRjKokg8ZWbUn-PXCkDqlgUhDis10n91XTbKjiMQJ6ftbwacTgZot9teSupp6IDb4luOe-3maPdqJMBHavVqrNoUg2XKYSznaNZ1nWjEfiCgIv5J9RfGlDs0Deuue_Yjk-prr0gWSlyWhpKhTxQDanTD1quWmJczWytCzpb2IBzDNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oCTN1H3XHJjlyofiJBerARkC7Nb5pr1xfINQZaiqLJRMGFghJhSs3TE59yYVyHUhoJZFo9YdcKhKZnLJFQw30wbLplUyHDgsqyCCrwVz6t_HM6PD46JbczzaaRbjKZx9e1KC2VKNadM-tuos0kSHYZhJAL6y_jNg2XJ0RafKY5YUGoSZkJV6wm2IlTx7DdQdgG3FY06xOvZpzd3smo3-cFhbqwT3g4hcVZR1RrY8-rSO7WHKdJBrxurxY6c8qeJ69vexJcYTzJaJoCyeya3zab1dPLOB_S70smHkWld3YJ0zpltLyQyETmwLtEsEXSrDryn6Iw4yqq-U9IdDxWdC0w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
په‌په‌آلوارز: رئال‌مادرید و ژوزه‌مورینیو دیوانه‌وار عاشق دیوماند شده‌اند. این تلاش پس از ناامیدی از جذب اولیسه صورت گرفته!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/101845" target="_blank">📅 01:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101844">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J5gTgF5oyyDJsMyZThRgDfnaqfkIfDBlqYIJgKAFAAYrbAxCXf3uGyUpQzDTPeD81bIUtFOW1JWfSOBt2m4N-y2G7LmYfHU__15m7lQtuAjlP6yqXiJqk6VvjZQbx8GaBdA_OkIrj19JHIL-RWqvA3sjO6mavlCy_4v2tsTeOCCW-QCOR2zuOMfghscB9cNwzENEa3fLJp7hwA8XUX9LNw8FDqn2ohS58THu06K2dURxulI6DjZIcuLzUosLQ8EnUv_RPFMLEqL5Eh4S2tFi5XS5dRjh5o9AkpSd5Triv57Mj1wMuG57PPEUoG8c4SdQZ1FAqjcP716sktDXonMVUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇪🇸
په‌په‌آلوارز خبرنگار مطرح مادریدی: در رئال‌مادرید برای یک‌فروش دردناک و غیرمنتظره آماده میشن. بزودی نام این بازیکن فاش میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/101844" target="_blank">📅 01:13 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101843">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lhfrLtnYQbm7_CwkYvJySm7ScqP1Uj_Y8RynNC4e5zlvEdFT0-y0dw9gs0WMfwUyOWwwkUPbZwephZxq0TcqnkH8TNSddGm5NosDYGih69J3DDndaAGY8RExMPmCaoJkVxGckoYZ5HlXTJOI7jCHtrk7kooAXrEOJwufpiFDOjKVcVk9DfSjhCw_dusU5I43uOWKAG6Kohw9PO-ND8uEb0ssl5fgFHusE21MdEC9NR3rjQwJ44bOiSZtfp-H6uX2HpVsjbOtiyqIBkVMtOT4zkyNda2QVdMyjqtCA7JDzN2VtXzMnz7ZKD_O6aWEsqO51mlTIX6XvNTI8iCyWMPtyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇪🇸
په‌په‌آلوارز خبرنگار مطرح مادریدی: در رئال‌مادرید برای یک‌فروش دردناک و غیرمنتظره آماده میشن. بزودی نام این بازیکن فاش میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/101843" target="_blank">📅 01:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101842">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
⚪️
رومانو: رئال مادرید پیشنهاد اولیه ای را برای جذب دیوماند به لایپزیگ ارسال کرد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/101842" target="_blank">📅 01:08 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101841">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dkl-bjDqFmLy0NWGgzqKJ8KSOr5KrpZUENoUv7uG4BgPHz47CIdCSeFDJ49Axlfguvg0dxUUUfcN23RQ3G_OuNubAaBBchgut_48afv6iKwfBq-ITQ5QW9eT65RtyrLTF0auxu4vrHkFu8cGrOoE03bodAcSynig0QBXOpQEk9wYxaEBWr2GyXNJ-riQB8OJQ3rOGS2GHzinSPpsDP5-zs2EBQ1Xb4VL04mNaIhBcyhDtTFqsKSDzMeRN50xVe2ANP2r4cvDRwB3z_E_3Fk2PeClSfzs8qB45QGHFOyN6m1tzUmSsOmg6jrtW_wnYDzKZgCt2Fsk4Axmzm-U8is5qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیژن مرتضوی و بانو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/101841" target="_blank">📅 01:06 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101840">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SOgmW3Zndc8PHocJU0jk_b1guPew-Wwz8_LlI1CnLdVAWqIa124lLWQjsm-aS9_pVAz46D9I77DDhpHLLp5PeMzt4w5G46p9pAtF3Xq6YDGwJKwXLjKHWwHjJQ-sp0Kn78kdeAbnZLEw3yhA38bu7lHyIjgpof94M9ACV86pg2PTOWbNcDtv37Wr33zbqmRiJPt3PWSqgGrxz_EBkP0dPY7kq7-cQ-fxilb3gLOj3uwpJHcUSrOAqbYdxEwXQVLheg1yogr7LusfKwSEhDRucI-J-vsyn2A-s99Ahu5E2TidbcKfUymxBNHTVWtqhkQXiXxsXYtEVuy5ObG2lRWxxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🤯
رقابت دو اسطوره برای رسیدن به ۱۰۰۰ گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/101840" target="_blank">📅 01:06 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101839">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u8hS5nyq9ZDtekpSKWSLar57xy8jXakgHmZVnxvPscClK-T_aAEP1qQuCn9gMM1NHn-s3T9q0IYgy9Mx5i4meZBuAyggVbBD0gpzJ0vAs62eTSpxUnyF7wSytTAicgQ7hXIByx44okJRDiqk6ZiqTm-gGIEIw4iwa1sslgKla2uv2tvBaxYgKr8sn1S5xHTj3rtMJrmo4C2FS6Z6O42mLGBmmPGPlxJfxI2NPiTSiT1S1825OJ_YvR76BFy4UqaQNYsOagBshacayxw77MR4z9OorZkrMVngQBpF3FN5ID2-3Ar6pp9o5cRAp6EqKHaekr9DEuPODbsy8XR8Dl5uhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
رومانو:
رئال مادرید پیشنهاد اولیه ای را برای جذب دیوماند به لایپزیگ ارسال کرد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/101839" target="_blank">📅 00:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101838">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fSh_6G2HEugxN7WF_f4Px1MX8uMTw760-Gz1HDZDWTmbYxlrmh3RiSOuOYiHc9mXPAtTGD5U5W5M13oOc52FTqnzEqdJEnVbc2qeIs8FmyZUgeWWfXFf8tjqa2dr6QQI4wzluHX0xg83gi6uvwVxfwmqs1-lc9ZmXEAtdPSHMnHVqr-AnlYwSMwd4TrYgKiS733Ek1pb89Ge8nwKZJ3eoNpwoFIOnkcsg89_hp0qUSRMFizz0mVD8u83AikAFLa4rXxMhUtHwPadOoc7N-ooGTK5edRf8L9VR18MTlLn50-8lfx9yk7pN4pWWoPBVpphdUGfM-NKKxXlMgtgql_q0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
بهترین بازیکن جام جهانی ۲۰۲۶ از نگاه فیفا و برخی رسانه های فوتبالی جهان.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/101838" target="_blank">📅 00:11 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101836">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LnGK86CA3BOjPRpZ3F4dFfF1WGC58WNLxJFjnBPAH523dm7EqH_xkYNwu3G2wXfFPirHQQNXpBv1kSLG8ulLQELyVF8IRbGZ6JhXqPrwZTqbFin8ASLdnjyT7zHtSbSDOPcuJLvnwalsB0KyRkAY0tqOhFp_CV51KfyPwZfI_f5gX5W0yEaiL4O4xIewCp15rvwxouFbNQdWsuL78FcEk80AiarulIEYuMZEigIcJuMAU--PJTufBd4baruJC_Oj4W9_Cwqs56Y_YioKrtAZl6CVdYKmg0NlwCYB6rkF70q0a2ctGUtwff1cDvBBGbkmsUhv6GLyKOODU60EvlA7ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
تیم ملی آرژانتین اعلام کرد که لیونل اسکالونی به عنوان سرمربی این تیم به کار خود ادامه خواهد داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/101836" target="_blank">📅 23:49 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101835">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KQssKl4K0sbjOY-93pUKzjemIUDfr7dn-UnhSh1sl8PWoy-2OiS_yQBf3DNpiE-7IJ6q-Aut227cidbgGswHI2s_hw3YPrpk9eH8aEeVkIzaV4eznWE9wdOsCGz6DYlqH69oBY-bG61CmYBA5swII8Zs27mQm4jOlFKgm-yWf2AtMGglfyu1aAOm8yU0RWsTolta3mZ8O_MrVzXbQAXHXvYkQi2mmwHodmx-rr8fvUFYl62Mdkm8JsXRyzG7hoNiSVkRvJKUU_I861VswUOb6-g7QApIk1qFDdYmzDBH9Vrxow_UKjnDRFAvkb7FTjg5lg6gcC-YPzpcbMc-Ju4bwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
فهرست بازیکنان سانتوس برای بازی بعدیشون مشخص شد و نیمار به لیست برگشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/101835" target="_blank">📅 23:28 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101834">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q-CEXRC4nNi_EY7zJWzkogVfcK6QZHqZZCxpE0fkwU805e26DOxvZajlGWoMBkOenZQcPJk4-Jom-7E0Tu84RY13yPzKbA8KYlVXlCfN6CNZKFF94uVS3QCA5LylEu8rZFwnKHBJRhmCW67y2c2DtSzKixRgMRRKZHg_3ugwqzBmL-QQKo5WBlxz6a7CzIpOoNFV33YpVhHJH-hA8XvNV-MtoBvhRlydZVZ80MBPJmWlPaa4W-vzt73BkotjSUZ3iJQQQ43kOAAbDQixT47d7gB0ypWOU4DYiosn073lLg86ujESHPeen1IWmhTGHz0LC81LTZ5UMBndc3NvO_HyAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لبرون جیمز ۴۱ ساله با فیلادلفیا سونی‌سیکسرز، یکی از مدعیان قهرمانی NBA در فصل آینده، قرارداد امضا کرده. این انتقال مثل این میمونه که لیونل مسی ۳۹ ساله برای فصل آینده با آرسنال قرارداد امضا کنه.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/101834" target="_blank">📅 23:19 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101833">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
🇺🇸
دونالد ترامپ: با وجود اینکه درحال گفتگو با ایران هستیم اما باید بگویم که مهمات ما برای یک حمله وحشتناک به ایران تکمیل شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/101833" target="_blank">📅 23:12 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101831">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A_ymFyJ6-gxy-gCCQDS7P3GiFINVUVl9ZCUeLmtUhb1WblcjmPLDVW4xRZl9oIjHDz0x_uL25lcRlxTOb_edkvV-BO5wSs9TFYFV6UamfBhUIOYQlXHNjAiKPub69f8872-90-pTXpLVvHJ6lYe_oQUWVSOU60Dlqovy5txXJSwW5L_UXdgc10P9EM639PrzrYTV44DNfv_L3hKkv4KbWVyFWqB7xm5QT7u6RZVA_SFAT_s8Sr3jpa9Yi-Pb4PL7DbI4lEryQXFt6zA3Q0c0r_B3RG4bfQWRlUWHhk4xZzqhBTKHwtwwPIkOdVjWNjLm4yvBPvWuRR1REvMe_R7uFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L13e_-eb4jFrIRtg_SI7-Gz2eB_RU8b1tokG6kpBq4ShBdVqevw5NueAZdeJpbyWdnERxhXHNXtKCse6EE9Huls3wfcJ0kzOumqa-vkzMhDKq4M5loHXVyPbVnim4kg0ANm3mRZT4IGWpxf0tC2URWKxotsRHSAW1lcqsWR0p5fuaUBPGAurLfkLTGn1W_udrjyKRdz_2oR9fNBDftw8oRAH5Zyv02lSaSMuEI-DkonRBTy-pMI9JnQV5hs9XjAadv5MqxURiD5rgqUhxJkpCVTC6puC-ayPMn3NPTyYDWbg8vE_VrlCoVq1TBYg7hqvUkXUlAcLPNNlknp61Ohbug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
👀
نیکی نیکول گفته دلیل جداییش از لامین یامال، دخالت‌های زیاد مادر یامال بوده؛ از تماس‌های روزانه گرفته تا کنجکاوی درباره جزئیات رابطه و کلا مادر یامال علاقه خاصی داشته بدونه یامال تو رابطه با دوست دخترش چیکار میکنه! او مدعی شده این دخالت‌ها باعث خراب شدن رابطه شده و همین رفتارو در رابطه فعلی یامال با اینس گارسیا هم میبینه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/101831" target="_blank">📅 23:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101829">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sB3NzRlGsKpU1dovk2-hnN30hYj55ZAa3A-kD_sTWWLH2_a6nR7PwsIfhMvhIh9pYNw6NnPJkBpsgIIqUi4BUAwdXiyK0C84ayLqZ7TmFxpcM9FSXKW1cJR2kPwHYY1nTYreZ6zhvSr_a0xR4eNeejz4m_yf7wYFFS2k9V9Cgw9N_Ado0deEUs4lUOZz73lEvcDtImmq0piKVdQGrOKyv1dnbB2nj1f5D4C0By3ZH3QlaLLFCje6ODaNEn5X8tU0cKFYbwfvR-EbuabR3d8QezEJnHhDN42wpZwbkn8mneyWW7w3k-Z1ijC-nr9eahcNBkTij3wiTs0yZGiWhgIWJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d8O0GqOodaOiWnhEOV1nzkWseWzu97Pdjto_15bySSk6hlCUiHhaSlz5v7PwqnMED22HiFMD5N42WPbr5nttu4-PHu-L3YxX-C3blbsJ_BDrzG1NWaqZGdssJoGk21kGq9rcg3Yo65jNOdjzsREbQoN0Mo8e2OZXjLtjZMsSBIOnxGQpE95z58Tc7pb1lQUK4w58QHb6vtS26ZqTcc7FIpBbt0tYR0qYFLNPg8E3bQicw9NGfQIztt1YXUwvWMcGWhBpLk3lK3BMUYFrDoK04vtN3bexn25JL_U68GQbRCYxMkjzMJTEoXFM8y7GEFikAVaYm6arQOx894cwB45RYA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🔴
زمانی که رافائل لیائو تو میلان بود دوست‌دختر سابقش با استفاده از مدارک جعلی تلاش کرد ۲ میلیون دلار از حساب‌هاش منتقل کنه، اما ایجنت لیائو این اقدام رو کشف کرد. تحقیقات پلیس میلان جعل اسناد رو تأیید کرد و در نهایت دادگاه این دختره تیغ زن رو به پرداخت ۵ میلیون دلار غرامت محکوم کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/101829" target="_blank">📅 22:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101828">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mn9EhdtZQd1F3179u90tlBnejif9Ih8qdX1mE_nqlQNGoVPy2FRaPoTCSxfMyx8cOmZr3PchFLlULVTTDe7pjsf4fSgDbifsMBiVK_YkN50fih0x8Hv6eSMNhWUeDk3eAno-llaqMYehmiGQU22b8AEdoPx4HP0KSYPy7zsZ2zEGt10-IB8PGETzrcQvMiCMLS_Oqw5P1_qLTGo21SI9em14DIA7rfyE6nFKezKu7LxkVRYIr_byBSd8DbxlrMTH0QWi3Bf-RwW7KP22cEyWyTkCitIYkfO5NAMVqHLJtnQh6hcJMETHSJ1lDq3Pazl7OBn7Xn8nyVK0fw5gIvO1NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
توماس مولر در مورد ادعاهایی مبنی بر اینکه داوران به لیونل مسی در زمین امتیاز می‌دهند:
🔺
"در مرحله یک‌چهارم نهایی جام جهانی 2010، ما مقابل آرژانتین پیش بودیم و مسی دقیقاً کنار من ایستاده بود.
🔺
توپ به سمت بالا پرتاب شد و به دست من برخورد کرد. داور بلافاصله…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/101828" target="_blank">📅 22:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101827">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mg5moLrcG_pGMqN7iZMuKAA06rdzXvViyGgBEqvLUGzJeWZ_qOoXOikjYRS9eq394YgvCEBOHOa2G2gYMGms_euEVzPL-wc7uY74kwQ0F-UGkUNoH42aFneCHvedKDKa13qu8zzuD9w0wW5PY2MD0B-vVRoJGKtTzCZJlmSLAX-I5SBPsJBz7Q3Mz2pSstyYOKD1D9Q6enhpbC1h3LfFv1mr9kDZuNF1egvApYz5BiqgGyVanpMv55a9o8PMjRO7txk_es3_cOgVSjsPg_bTEZfIai4rkE6CBh9FvRn3oti0MfnNbca0UjvVfIdB-Y6khRdscuwkqd4GO2TPNs_rYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇱
🇸🇦
•
الهلال رسماً سامرویل رو با مبلغ 70 میلیون یورو از وستهام جذب کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/101827" target="_blank">📅 22:33 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101826">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qPozx_s4uf7a0bywmLZeZnJClPD5_4N-LpQkOiJzOexNIFYlDUqS34ADriPZgDYR9MI3rZzL3L825gXpeVWcQS153ohDcvlJF1_f038Pa4QETwfw5vJTlwo6e3NiiglBHXJmSWxxD9yISkA4aGrehW9DUEd0R2zSqPRv75DJiUTlmAwIttCN9UqH7dxzz_SF14zm3SQSyhzM29TM1vpMgLBfN_nFkTh-lvjJVbsbkLFtAA3-2s_m9-_-Idw2sPEASTLTUj5TLVT_VP4q504VjJ7xaD6Mvd6wqqwonB5Fr7D9HDYYb2ZYhn_1crm_4O-eKMi4Hra9Pp6QynqxbA9Kig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
دیوید اورنشتین: رئال مادرید قصد داره که رودری رو حتما این تابستون به خدمت بگیره.عملکرد رودری در جام جهانی یکی از عواملی بود که باعث شد باشگاه رئال مادرید تصمیم به تلاش برای جذب او بگیرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/101826" target="_blank">📅 22:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101823">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IqvwJqDCTqYhvv2gjbIpg7ivF3MbliJY_xdBWC0MGHS5_kcDpcfjhs8RBahneFOHaO8_eatZu5y7flad18KSOC9F7MjS4Hhz2ba5NyZjxYF0wMXhZ2ib5UNJukybYm90vp-tAggno-0keq7EplfPjrf9WzCTEVGk2cdt9Iu4x-QDqCEgV9k5pT8KGtB6fzQ2UxOrTtdu9G-b_e5m-TXoMAZFZu2HtLkntaTl-bKvtc5Zqh_ZBfC1gcq3HnmkeRCzZ9eo8OS8QNhKQOcoes15bzb-pLy7JP_T_USMayHZGFn2qe5nNlnIxeET_ukAsELsewa1QB58FpDa5HNNssRL3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇻
🎙
ووزينيا درباره شایعات پیوستن به اینتر میامی و بازی کنار لیونل مسی:
من عاشق فوتبال هستم. اینکه در ۴۰ سالگی هنوز اینجا هستم، به خاطر علاقه واقعی‌ام به این ورزش است. میخواهم حداقل یک یا دو سال دیگر بازی کنم. امیدوارم باشگاهی را پیدا کنم که واقعا من را به‌عنوان یک فوتبالیست بخواهد، نه فقط برای اهداف تبلیغاتی.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/101823" target="_blank">📅 22:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101822">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YM5ObBQdA3YrjfOxTa3wRRqSfo72V-M6FNSJ5ek_238pTL0QN0hEkh_fAVhWZ34K4cDrwZuU97Vjd5YsJu6bSarj5X1M9I2hdhPY3ax2aKgXOCEj0Z9dK_TYvcSQJGTyOdTmjLfLn7kGVLCE2Go42jdzqzhMkbra2jID0xplxD-m69nCQmxosbhqYDbZIwrnAnMAfiUMl1HuLrzA5CNTXkuSn9XwWMSyC6JjbL6gXaqhOrBsJkSHAWPgYF4lRMbq7Flna-X9Pi5tkaLSnfYmdSZcDCz9y0GcMgP10h3SsYJbkVS6b8FWm7j3EcLjm1cSVeXiiC_je_01wo_1kl03Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
دیوید اورنشتین:
رئال مادرید قصد داره که رودری رو حتما این تابستون به خدمت بگیره.عملکرد رودری در جام جهانی یکی از عواملی بود که باعث شد باشگاه رئال مادرید تصمیم به تلاش برای جذب او بگیرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/101822" target="_blank">📅 22:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101821">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y4vTpA-uPB_77ol6xRQ6bR_Mq9GeZ3QmvFks5GHbCym6ZuiUh1gjl9bCLbd0V2dRScYxiTBOqts34QncLTSwPqHe8Kr9gsctXZWD1R0L8p4AgQQg_3a7f-TjJ2Z4gsH_Ty_vpNWZjSYo_mAa1MbNTwDoyJXm-vD5HXFL3Gm-0IqkOfzQnniGMPGKq87zIUtH7MWwA7r-S1JBmccGxi_uJ2mLAcF5aL1w7V5lXSQCdkFdMh7b848UKvuSXS3q9bE-5E9_VJexMHsdopUXffgvDQp3SfZJN-_EOg2L7Lf1A4ShI8avHxlVfPGFY-mrEvzBFGlI8SRBs2Yp-lDPGOMn5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
رده بندی ۱۰ بازیکن برتر جام جهانی از نگاه اسکای اسپورت:
🥇
🇦🇷
لیونل مسی
🥈
🇫🇷
کیلیان امباپه
🥉
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جود بلینگام
4️⃣
🇫🇷
عثمان دمبله
5️⃣
🇪🇸
اونای سیمون
6️⃣
🇳🇴
ارلینگ هالند
7️⃣
🇪🇸
پدرو پورو
8️⃣
🇪🇸
میکل اویارزابال
9️⃣
🇪🇸
آیمریک لاپورته
🔟
🇪🇸
پائو کوبارسی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/101821" target="_blank">📅 22:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101816">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C2LVqon7ptWJkIao9G7KGON4hjewqu5mB0GkS2vNkUvlRWIdkFC_EhMrJ8UkGbGvfeMGPotQFHnfe41dLeeBPG9qpgvBJBzgBREQboH1Kaycvfwa1FgoZbLbDayr3-5srqaJN46uIZrIwGGdfvw_hFpG_i2WYp_BnyHJzeDKdGq_OxEp9TrnVV087m41NkT5taa-fPN4hmK5Ep2h3XDbwG-Wuth_2Sjc3xTVyV6SjSlZXssaI6wyMXXgayu4gNLMYTawo9JSRTVDLzyu6HIgH8oZrGw0yu2gdpqrhcSM9RLe150Jy6DgEVXsAXQ3Ob343PgTgKAeaGmLBYWIJQxRQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uIAHhY6XCD1gxtXi7lCJ8EcRFwHrVCNziziq8joaSmQk2WdSg30qjnUiWSQgYmw5hkE1eQSriUESzL3DApM8LRYcup-biZiLHbOkwmQkoNiH1T2zQtMhpbHBqbwQfehSk19jRx53KtaUOFWeCTOk0JKnnFA4NohbcrYobjrYPsbRsEg7nH0Mc8syQ3-qnQ_AncXx6qDknWtzCZPWwylz6rjl6QKn0dR0iIcCwAQdO5TaszmQ_WKSs0aq2reG2j71UQxsXTPoya7_UkqQusMMwiTMVBnv02H9miDGgZN3yz5Uu01p14nb4f-eSR_xzgug-Mq0NnZwAxaugN5XmtlhUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UNxyCxXYyYKv6doIhAKNmlrpnyRjHBW56xFQfQbT05blqs0xBRZJI6TMk-6Xk3XZr-r1E8UXG-qOolSv62nwAkLuYIafA6o2HpGG24yYf-kjaAGuoSeOLPatMegmH5jj4zzInrOU5VGzC0iUgrOVj1c5aPqYvJ85tgWurs_K_PGd4FDQiBUeDBadJj0_-txpWs50s4Np4Y85SCQVYwqrLuXAFUmgnx91zIAN2iwu0tdArTC3xztaxr68nbjELA5rGLYoz8VFY7t4ALsCNN4NT9Kk_SzZ0zSAOnEunDcHhg_uO5NTYpfelUYB4GvhDeKfxqeSVJR2eAzxHIQBGjgmig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lpGGf89ht5sQf_CVIo6CCIDxQGzmZ34PjkpNoT0Xv9-3TC-z5icFR4osITzxwvDaJKIjav7iv9uDb9paa30oQpCsWE-4vJlxhTF0gHDVhmerwmLusbJfpB6u5HNXHpK-J18BYyDvgyVsdqfxmmJQiACQ9If5uVqzbroD2Bp2wM6QqE9rp8K8sTOG9EynvYdIMsaSZDMO8juuaCexgOyABhA2cAB0_5NczJyKaeMsSKQL5KGvRFs96lY8sXZELMmNfXtjjDz5PHscuYAHfShEC-k6Y9xQbvgIKF139EMfCoLdf0DFzvZMmiVGZVz87063yQ1RDlgQNr5pH7SufVi8-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CbB11MHzFHRe5GP4HO_J7Ad4aBfc5iDgkIYpLeQwClML7044uYc1tObn31hcr4E2E-E74-xOHxY-4799f1tJuKGMHHOj-5Qze3w82mfdDRN_WSAe99lPq2li4jnMf6Mj1Hx2m52_efbDeBUeKMrLqgX0FTXvCOgGiMVltICIzmze2J5w6wcSV-MzPYcUiOUoQJayvEWDmcnNFW2GGuvG_ZIBAkgY7jgQW0TiHivKSYhvKoS3Wi5yS8kQIrDH-R15gNfrJiO6JbEaaCGH6X63vQpj8hMqfVg99BzWLO9H1B-Vg6pb2ki5DtCyzRo-1uxYRMVKtzXpl4JQ0jXJRaEP5Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🌈
🏳️‍🌈
فران تورس با مارکوس یورنته رفته تعطیلات
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/101816" target="_blank">📅 21:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101815">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rJ5bs95M4SZpUJNFWyzDVWa-1tZZjId9YVd5jkmcnDezub3c4gupTm1PtHsQ5ymuqf318O795Y5xLwr1P2eBqqSWc5nU5bBPLyPQwVZpk7x0ebEGq74WUsr5rA_Cj9inNrjHhPU2q21GpqcrvBlhd5k65tBqP_ZvCvdK4snKs-7FEJN7MSOHdjeHGtPrWZmWUyx0bfg-AH7iI8rEjW7WB0Y3F8lz-g0QXWmnfqVn14t_aP5twqb489uTJo4LLsgsbz-_10ZGVJCDCLiObZk_M5FmhEPUIt9WYwHB9Tz10P5IY22xLguJ6lTZ5x5ZnYIekCtDdWldjTPGKn0gPjFyqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
کریستیانو رونالدو برای چهارمین سال متوالی پردرآمدترین ورزشکار سال ۲۰۲۶ معرفی شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/101815" target="_blank">📅 21:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101814">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sdPk_kD9EEdeCuZbXbkxAhLuTt3T3Y0GvcY1_kR6k7lPGt_cdmrFCdZukkQdqyL86cQlmStg9XxLdqERG_l7VgoSafogwx3KFsLUR5JIuE6yoIVYeELxLiLSxq_dOi1_5toIt2AkYpQo8Kn5juApPKCJHMkgaPVRzG-9ya4-PHmyAFNjpIw4qBticiE2N4_SGNo362iBYTyElU_oZumVzTGiH0U-uBw_uciGc3uYjczWQalR7Kx2Nb3-mwUoXsti-9tq5G7aSDVLZz4nU_LULFvsG864he_O0HhKSA6rbuXfDcGtTE3JWmzE7GNCePp1c0pskbSbDOBq3Vt1KeNb5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
ترکیب امشب بارسلونا در بازی دوستانه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/101814" target="_blank">📅 21:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101813">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tOaAODgJenAq4QZGmKQslre9LjOdDtd-0SzdfbQGDyp1MdB7Bl25xJG57Ie66ytrI_u4Z9dGlmRfrRm-foaCSOBOitJTcxu0SzmAmHQI74aMKtvX7V6aujYnf-R2sVhJHgqI5bGP0tWmoSa1vkif3DQX5hQcPnmIw9tuqkRjy2aJnaJzmwTcsIkDWASA2UdmBuSUH7YSrblAAuHFTweihUnH-bEf7BZ8Sh69ymx4ybMqyXTVPMQxOdK0oiT6X11NyGdEezfiWeH2YP6sHHipFtmhHr96pXNLJXKNqj7cdGfJZG0kwEWci-iZzxI0jIDbTg49jiQ2awhp8z7somOmuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
کریستین فالک:
‼️
بایرن مونیخ تابستون امسال مایکل اولیسه رو نمی‌فروشه و بررسی احتمال جدایی او به تابستون سال آینده موکول شده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/101813" target="_blank">📅 21:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101811">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JuQc3lTPSmw49psotXyYv-KFGQZclaRbM78KRojKzUFUi_oHbA_os0oS3QZQiNs582joEqiXTqySyQyivZFaabjcRvX1t8DlgBJTGiFOu09yOPttxXaal7LOG2aVEKVZBUShRmiL-854yJ0XL0rPE2IWdZ0x3Pqfxr-2q0SpKGpzIkgNjkb22MJdx56TkS9Wld7swEK2loMtQxMmsU3VK-lj-s_IMwLQYxj3UZtvEpwxHjFl3zTNCA1sM2TOWud_urxvENjhgMu0LxDDe5NifTmdT0c23XA-HvcBR7kQBpd2uZEWVQydJMEZQ__95IgS-BHOT5OsAEIGD3jgqc_xEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eHfRdRhb_dWSga8uX5jPZdGLsf38XwQiCA6akcedt2uGBoewXwmOjfk65VVFeQUG5cbLPG7fba69fRFuSYxOSoapWEsqDGj18xBZQc1Fc-yloaTgcry3OjKT4hDonJ9LeFNnxjaeHew47TTLdzU0gf8Licsq4mp53yqiGqNisPsYrFasvLl4dNmpAe4E8QtlfkJFkQBqAWMRk6VI-9SQA0ODsJiPkgplk5n7t38EYuz7q6hkX6DSwtBWnx1xeRbf4OZPSbEvMghGSeX0Av07Fj4r1Ltmo3Tab2Wf0Ugc5cZ6X0W0-hB7piwE8FvCbcKgIlHLrRWZg4UdLOk3FqMMjA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
💎
۹۱۵ روز پیش، پائو کوبارسی اولین بازی خود را برای بارسلونا انجام داد؛ در حالی که تنها ۱۶ سال داشت. حالا او قهرمان جهان است و ۵ جام با بارسلونا کسب کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/101811" target="_blank">📅 21:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101810">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a142d4e6b9.mp4?token=en7bXkHzYO2YrN_F8bh8SYCQDf_0F4K743llzOZx40lnxg-XF2iJxe9UfyrBnHBemPPXP096IK-mLrxL1zeZ6_he2f9U5X9sHCTYV1qxLE-1gVLtEeLUiHXbzO2lGeJaeThdzCs3HqBcxOA9jmrfTi-GkzMtRs5nd70x2kb7UYaq74OrFeBb_LxODNBlfgroZez3gh3-dud3dGS91mmykucPjVKZFnLodlt0FdaeFcyudyJ15MsQYoAGdM7u8cC1IDyY4YX4pqDOSNKeWIGM0LDeWIV3Tpscmzmmp75aZtgEK9cxgYHrAcogQ-JJn6WA57vlhVf85Sd5lmZ-8g1eoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a142d4e6b9.mp4?token=en7bXkHzYO2YrN_F8bh8SYCQDf_0F4K743llzOZx40lnxg-XF2iJxe9UfyrBnHBemPPXP096IK-mLrxL1zeZ6_he2f9U5X9sHCTYV1qxLE-1gVLtEeLUiHXbzO2lGeJaeThdzCs3HqBcxOA9jmrfTi-GkzMtRs5nd70x2kb7UYaq74OrFeBb_LxODNBlfgroZez3gh3-dud3dGS91mmykucPjVKZFnLodlt0FdaeFcyudyJ15MsQYoAGdM7u8cC1IDyY4YX4pqDOSNKeWIGM0LDeWIV3Tpscmzmmp75aZtgEK9cxgYHrAcogQ-JJn6WA57vlhVf85Sd5lmZ-8g1eoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
پیرس مورگان:
چرا نمیخوای ازدواج کنی؟
❌
🔻
زلاتان ابراهیموویچ:
چون دوست ندارم 50 درصد از ثروتم رو از دست بدم.
💀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/101810" target="_blank">📅 21:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101809">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AUyF-h80xWk70nI67u0VBvOa9D_tTFUTVIxAmTPZj5aWhf2h0kf9pmB9TeB6JtzRzGmyFytpI-aawWpOJT482cJ8tCEgmciORsvXGDs3DX3jegemsXGtV620-wmqsPN8bZiaVTiYnqPbXonv-yaRZfF-Q75S8WE6ZDwvOlolW2M4JATrJnxW7SU1oY40fAo6SYoNq_XOmzdAWIL1I8Rxk3zpt2xyOGZeC-WvJLE7Upl4h9GFtNMbdG4oxOmCx0vJ3JywVDq9qZLqIGfAupNj8HmXbCzUlH6gZbE0prJE5T-tdtu7IVGEVyRV__s_07C9nCaxKTaaQcjqfX2EX3GNuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖤
🚨
فوووووری اکبر عبدی بازیگر سال‌های متمادی ایران به دلیل بیماری قلبی در سال ۶۶ سالگی درگذشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/101809" target="_blank">📅 21:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101808">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y_x1PcXnbGa4yKwJ3s0e0KKn3Wg5O111Ah0hlsqOE_NFJNu32WJAPzgGt4m_Oy02K9mc0jLcxcrrWpmB-5AcT6V8DTjO8Ta6elB6gJwYnQZGMhLpbup3DOZyC9jol5OelTF36RRNTNhD4TLg1BItJjVNHVJDUXA8RKfqqVA5fWITzyXwkUCXChNlQ8SRRwold6-SkyfIFhgX2LLbWLRk6xU1gt7d716JsDO5MCsXXg_Hn4c_iAQPxoflnnqhd-LGKH1JBsMLRF9y-d35rk7TAu6Kx-b_QtCpOND2c2YpGx3hKf32IiKbhqQvL76LsKk-D-FEmxu6UJbfQQ_zPhnfEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
کریستیانو رونالدو تنها بازیکن تاریخ فوتبال است که در ۴ سال تقویمی مختلف، میانگین بیش از ۱ گل در هر بازی را ثبت کرده است.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/101808" target="_blank">📅 21:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101806">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TShSXZ4iomDHzRCM6LLG-JQMPBlEx47FfNz3mAmy-H7iOJziCei69Q83g23bXFW3uEbOeMIh6Jad1TE2qT_mLUl7xb5yq8QwmthSxDbacga6DBKyeu-JrIClNdWUBjQQpbADBICPB_gCiwMI9GVOk9SbSeTyZblQ2AkvGPh0lHuY9ak7p-Zz8S6mWH5FeRCgTvyJBGwr2DgrvkBZay439935X59SGOAYN-FR_DJ9WjYdmhbBayXnp93s78xqIUfaYQrag1TvhLr6Xpb4OlB_mGxSQjeRSKMYyX1V2ni2_3jDpIbpkOWX8H8fHLMKIRBbkxYs1veo6LdT4bo22pDwqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49a81621b4.mp4?token=uAuwVegcYZfDeZJpcTibKxU42VyW3tkRLndu3J0AEuOPBAEdKR2Yvbs-nEUBN4pyxmIsV2WXb4C1KGZ9RBADew7vo8RF119jQltt4bIRjfmkAGQ_Yx3seS8rR_O194_RIRsJjTeoETGlzOOnVR-nT0ieos1WSY0FJQj57hRnnDChK3yc7ijQT4Wyl5wlVgKCk6zvTylzZtKFAXPM3l7r0bzr6wRV2ACkVPKnI-mpfMVYLP6FSy5hO8lTd_niuqDFSvRnFD37KGUVJR5sgbdRq4Hsl0eHs-UdZyn4vFnSxNhfF1FgNWJRf8rvNHKWiocYmq-UQHPT1o63AzPkEhZf1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49a81621b4.mp4?token=uAuwVegcYZfDeZJpcTibKxU42VyW3tkRLndu3J0AEuOPBAEdKR2Yvbs-nEUBN4pyxmIsV2WXb4C1KGZ9RBADew7vo8RF119jQltt4bIRjfmkAGQ_Yx3seS8rR_O194_RIRsJjTeoETGlzOOnVR-nT0ieos1WSY0FJQj57hRnnDChK3yc7ijQT4Wyl5wlVgKCk6zvTylzZtKFAXPM3l7r0bzr6wRV2ACkVPKnI-mpfMVYLP6FSy5hO8lTd_niuqDFSvRnFD37KGUVJR5sgbdRq4Hsl0eHs-UdZyn4vFnSxNhfF1FgNWJRf8rvNHKWiocYmq-UQHPT1o63AzPkEhZf1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
تونی کروس، هافبک سابق رئال مادرید، بالاخره درباره توییت «فوتبال برنده شد» که پس از قهرمانی اسپانیا مقابل آرژانتین در فینال جام جهانی منتشر کرده بود، توضیح داد
.
🔺
دیدم که خیلی‌ها از آن توییت خوششان نیامد، اما همچنان پای حرفم هستم. به نظر من، یک تیم واقعی فوتبال روز یکشنبه برنده شد. همچنین معتقدم هر کسی جام جهانی را تماشا کرده باشد، دیده که اسپانیا بهترین تیم تورنمنت بود و آرژانتین نه‌تنها شایسته قهرمانی، بلکه حتی شایسته رسیدن به فینال هم نبود.
🔺
به‌خصوص مقابل انگلیس، بازی خوبی ارائه ندادند. آن‌ها بیشتر مسابقاتشان را به‌خاطر قضاوت‌های جانبدارانه داوران و فوتبالی که مدام با خطا روی حریف همراه بود، بردند. به همین دلیل از قهرمانی اسپانیا در فینال خوشحال شدم و همان باعث شد آن توییت را منتشر کنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/101806" target="_blank">📅 20:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101805">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P29sNCxFGplFRL0DyEbFF6kACkjdS6unMjOQoAnDnItykEbm7TQHK8QQuD8phmqfatRblGWeaQi2HNdaTy3HQqZlkbJ6OVgjC09ak7wcfGB0cRphtTtRj5_BTz2QCU5VlHyC7o49ncA6KWXl7HstYJDybcbqNRy8Stqxga0Iskffu5tho3s844qOJ5GXHPC5jGsBDA-QFBuNAB4K15I7chauZ0N4QY4KYvwUFVBK7YIxa615UwtSznM_MM84QDbUFID1Ehuc2o6av7YM0TXHCCNAGSrpI98i-sjP2Y8XlmyTwgyiPASjBCw7oXP744sQDYB1yNEhDD-dbLXFEk6lhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
لیساندرو مارتینز درباره کسایی که از شکست آرژانتین خوشحال شدن:
سقوط بزرگان همیشه باعث خوشحالی افراد معمولی بوده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/101805" target="_blank">📅 20:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101804">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jggmU4p-j_d1pA-Ys5fDaWfajZcOhQeOCqN1P3kCJYCk_Rkqa4QH91LQHm_phHP91lzmoOteMJPbCcLwuzT5seRtrvcr4ktQLB777i8PD3s6dat7b_n-fdqyg1twtnlBe-_lZ4KXut-NUnOUE4EBpxiPR0QBLS6o1CprGRNMduK-BxeGpGZ7wSS9DTM_PlUrJqDy1-_r1Cq1dB3FaNnLNtOzNIVFHDKFcjAKBSYM7H3z-XBXHqH9YRR6x7s1TXARXBsZ9N_YbpQ_YYd192Uk8AXOxzOGDbiNvE19z8BfZBHj0btNbdxhl6xA74jTG_AXogKZwyYYCLpGJAZQ-ULy1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
اسپورت:
فِران تورس از شرایطش در بارسلونا ناراضی است و تردیدها درباره آینده‌اش، احتمال جدایی او را بیشتر کرده. او احساس میکند هیچ‌وقت گزینه اول تیم نبوده و باشگاه ارزش واقعی‌اش را ندانسته است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/101804" target="_blank">📅 20:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101802">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aovj8j53-EZYVZOIhPwdEh2S2itty19gjr3r8GKiE8WraaRbjzitxPKCmhhaG_pU_8zoIbpDA42aDFbhPJjnweeGzLGasYREZII5jQOqn_zIhWyzK88ybyggxnpkEGuMNRD8WIUl8VGyWIhrycJHd5ECAG3Lql994J45pBXlkDTG3kovcnye7B8vyo7W52FFtbvtyrXgIUKoVKCvbsq5cNwIu1K5dAIZOHpdl8IMMyEXLeK1rWFSCCunfuxOLMQmCrrHGmubDd8ED0I9CAJYcOo_FOKzFS1PYg-XcqyMhk-hk5uRVR52vwRjvI5rL06O40hgdOuUtyUGsaoCJT8vtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NaRzOd1Ap6wz5p8Fd5vshJyZfrrvK0yRV9oUeaLMePIrBTDQqe9J8ojxSsXfBqBybfE9Vo6mshUkeBDKg6ikgh6pmIhGdC9-EkgP5uylmzO7biwu67pg1xEBIWnqJBUEZKUQN2oTsaOXM9I_yDntiPwVMsn98-vOZ8qHihe_fXq3ZlZFFpiSAD-Nb5xu7zXjiElm-GokpJRk19508Ls68t2iWA3Jz1uFqG9ZDnH6yqlyi1sQTTD4ExeQnSo__G-dc6GSoFxRJy83fOcBKToLZi-O72uq_mM3YBTiRXvlH4x6UvtDBJN65f2qjG3Karvfx4y3cwTpYI3Upb50RIvj3A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بدن سکسی‌ای که فرناندو تورس ساخته.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/101802" target="_blank">📅 20:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101801">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UI6z7ul8EPuVhL-M5eQ9iVDltxfH1k4e7H5Lx_zCyE55BHf_xIqf4Jc6iA2Rdghgtghllo4zVB22ZhyH2E3cyAA_Hbp_u_H6a9O_TqqjI5IiszC4-uMb9OAlBblv1e56J-I7mJ3FznExLw2e14jfptNjLdxMpnOvZ_eZRDRpwTZJBsgxjpY40KdWym6_8dWPqY-cTXfBHZdy1iEeVweFWZqm-lNgY9F6ir3rMMY5A0WnpfFj7cFTy7HZcBZNquUgOEiHmBmqwkIeWqIF3mgFgtJ5Nho0Fi5PlqVT9FqzFsENQUol_CTxieZ5djuL6rx5ISWriu-sVoYtwxCNMRwY7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
لیونل مسی در چندین بخش آماری بهترین بازیکن جام جهانی بود:
⚔️
بیشترین دوئل موفق: 60
🎯
بیشترین دریبل موفق: 28
🅰️
بیشترین موقعیت‌سازی: 25
🎯
بیشترین سانتر دقیق: 20
🥵
بیشترین خطای گرفته‌شده: 20
🚀
بیشترین شوت از خارج محوطه: 18
همه این آمارها در ۳۹ سالگی!
🐐
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/101801" target="_blank">📅 20:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101800">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lswblsvu46cj1Fr9xP8D4mLBLX3B6JFCe895n3cK9lJ2L7RxsiV-yn_ZSqfnaYKCclMc261WVGSoeuoIVAYgySrKBD4a3kEgl8ijamxtc-p1baaz8UszREYduxO4eUOafd7eLOq-hNJgiaM3btDXWI0RutI-CB_xA_IBtS6CnvOSYHATgbvLxGjH-FZeFQ4whXZDAX6ChEQvNP0TgkRaqCGZgPNh63mI15Q6WUcH2C_n2MvrIsVEIwsETRf8z6vkCWUGtW16p2i9BtMVtQ1r9zEvK-LokcrC72RMqb7PecLBv2ODisyY57HqbWhoJAAYCkXAXVX34S6018hig2cc_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
✅
الاهلی مصر اعلام کرد که روز ۱۹ آگوست در جام خوان‌گمپر به مصاف بارسلونا میره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/101800" target="_blank">📅 19:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101799">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YWMzxz5Sa7cqvYJ4CAGl8AKiEKXgwhnZzc47OfQI_YisBczhL8b_WCMfoBVC_qWqX4172YpVGIFo2coW3AmZKMiO_3bfrdIzDCr8kCFzYY1XUHsazs3NJCw8ZyFFimCKhNR81gzLdgVqb1xEdzcZ-PRCje53Y08Bsikqsr9wI7JRrp6O_aaQo3vK6iYcqgVoTz1ERC61UPzo5FC_3cQaN8TP0atUrSRuV5nUpg52U4UKmTWzC3Qc_O4wST4fhJIHcsN_2cCfnzOjCWpWIx-rUc_QaD8ppqwpVf1cGcnd0kRRdJ610vE-9phJYkxBSfPK0Iu6Efn4j7MdZ4gKqeQVGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
لئاندرو پاردس فقط ۵ روز بعد از بازی در فینال جام جهانی، با بازوبند کاپیتانی بوکا جونیورز در کوپا سودآمریکانا به میدان رفت! هافبک آرژانتینی از ابتدا بازی کرد، ۹۰ دقیقه کامل در زمین بود و حتی پاس گل پیروزی‌بخش تیمش را هم ثبت کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/101799" target="_blank">📅 19:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101798">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v3mAkYfZB5tNayWy3f_cvCXCuQ37VLjDpe4iSsyoHrFknflp22MN_ZMrmPMF-zmwaLtRj1WsDOJm7Jr26jjycy6xDwi3k0XD5N-9DZ5QECkHA1Qa4zHNFmbrtReqWB3cBqhRLoQ6CBLq9UjUGXqwLK39g8k2kvGSFoYQPqq8ExrXhbwZdX0GfF4t_0yxOHcUWExWFlyWSy166XfyeMMKOUqeRU5QF0gkzlE3ROD9pyoVZf-2PtCpiG7GxYjjco3_kT8LZ_7120u5luZlzFjmX5toCDTTvl0RYAtb_nqz3nLJ418sNRnwlTLolNzOArTHd8v4ve9U9AX5L5Dy4LiMaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
فابريزيو رومانو: پیرلو به تیم ملی ایتالیا 𝙃𝙀𝙍𝙀 𝙒𝙀 𝙂𝙊!
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/101798" target="_blank">📅 19:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101797">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lVd7F9ZrjZDOd0ae1gnGlB5ggBvrrIrM4uJ0DgCv1rmlnHrk8xNr9ePFtglgPnQ2wWY5jXyxCcLCtR2YdYk1sxw9Pl9dkrq5niQeey2asTKu4prAwcmvCR5O2WJzV9l03LqkUKSCkff8YqoxT_30ud2CJ0O3eU1U-ySBDVQ-7WvIt_Tal-Sv7_ggJ5Ny-Riv4bc_jlNcprg-QkfA6dLuCDuwwb9eA2FiXMfY4mzdh5oT93M3nlW4NOuzArlt5YfvFjnDQUW3IgzBTXAJ8_tBzFKCZ7tSoQHps5ILlsJzq-BkN5stRdjgEfqfhR6VN-Wth-ed4ZDsr4pRiRYjqZdHWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بالاترین امتیاز ثبت‌شده توسط بازیکنان لالیگا در هر فصل از ۲۰۰۹/۱۰ تا امروز (با حداقل ۳۰ بازی):
2025/26
🇪🇸
لامین یامال — 8.23
2024/25
🇪🇸
لامین یامال — 8.01
2023/24
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جود بلینگام — 7.81
2022/23
🇫🇷
آنتوان گریزمان — 7.69
2021/22
🇫🇷
کریم بنزما — 7.69
2020/21
🇦🇷
لیونل مسی — 8.52
2019/20
🇦🇷
لیونل مسی — 8.71
2018/19
🇦🇷
لیونل مسی — 8.48
2017/18
🇦🇷
لیونل مسی — 8.68
2016/17
🇧🇷
نیمار — 8.52
2015/16
🇦🇷
لیونل مسی — 8.46
2014/15
🇦🇷
لیونل مسی — 8.84
2013/14
🇦🇷
لیونل مسی — 8.34
2012/13
🇦🇷
لیونل مسی — 8.83
2011/12
🇦🇷
لیونل مسی — 8.88
2010/11
🇦🇷
لیونل مسی — 8.76
2009/10
🇦🇷
لیونل مسی — 8.65
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/101797" target="_blank">📅 19:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101796">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r6yjbgZHsRMXZcIet3_JB-D6F6byowLL7sV3VgqvD9j-9BHK0WJmpONiDAtaLBQMZvb5vhR9SN7hEp_kQIC7GTAlMG9_Il0JV2jdNYQz6NjCXy8fiD4jDKWNqeclRaA4_G7SUk8k_bjxJh90xqDW08atDE9ZlHvDcijYXhF45a7BPv7c8yDlMqgyX7sj6GXSOjq6KCeWbaNc64tfsVrmiilWYIOuDa2J3JD76fARchaRpT3zpj1M9vCalcOZY0t27U5BuXaniURSw-oInsy1oJR5M3M6-Z0fTrOc00j7_W6Y9-xkvY8gOnkWirPza3g5uDNmu0q369hHh5LHnRxgzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💀
مثلث‌خط حمله فصل بعد بارسلونا: GAY
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/101796" target="_blank">📅 19:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101795">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uVx3kYouhtAs8jDBn45_zvFHsVekIIwXjM1jrnh36tLCUscgnj91E1DhTEiaL3K_L4rWo2GQ21pR-zY1SYzafJ6cXdF9XTPc4qW-ppL2RthY68oOEI4FiFjG9kNuhEOOGeegF_5lWLM96tLV5RgZ8QReTb95Nx0gn_vxCG96Xvpu7-z-zJDksNBmxAJjYjjDnDd0NU26Fcgr1pg2kxeMc8HgUetjZxpKTP1DxZlxvzUYMZMggg6-empDelu8GFWq1cY1fcWDAtUlvVuV6_tj55ts_VXlokw8TO3OdXASnEb1PQuVF26UvZQrOfZzdW-MWm9o247fNRzF9xr-Ah682Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
⚽️
بیشترین دستمزد هفتگی در سیتیزن‌ها.
💰
🤯
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/101795" target="_blank">📅 18:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101794">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1da4d2bb8.mp4?token=WEd2V_l34TGNiu-2DvXnHkWdsXYBBHZL-ZLbNSBCV00BkLXTIze5KnmUCSAmcIOCT3kjQSY_OlAMbTetoPDCfwAmE8hwhXrek6U_juh3qV28tH_hL__iB6ixCKf1ciFfCFT0dgdoWAHZqbL8KHdQSePLuAPaRD-Dtp-n1Ei4AoNsK1d2MtKzhMjqB-EBlRsugQRF669VP-D_p3Ufb7eCnQyIg_CWajeWmmEwRAI-c6647r7rl8v1Kl1ENWcBVzxnMerLgYkDHRDHSwr5G3KXRn1Q7CsKQxX7PpqleJtcAeJABtpEShKFq9cTex7DkWmvC0G30rgu6v_3jvLVS-i99S4VqdSgI-GSzdxiYA4d2UUGjvGFwPreKB7da3l55odh-gcuQtA6h0lIMTw7C9PJjIXIltzXuf0lWiNDaon5ss02TxfsdBpmrWYAeB3RKKFGDvROn6Mnxx9PktOmJxEDP0qEZfKvU9jf85gDb-ovN_dQvjQHpmUAl8cW0uGnjj0DhOn4XBIcHvXwyVVY5O7a8l-j7Sr0V-fYdso5U9-VRqINnYSn4YJgjiIeWAI7EJ09R6H-rTx3ZZuq4zJAmuS5pcOmHS-Buc6p1tJ-mQe4l3yH-RhPetXaNsfdqizz4qntMrY787AzEuJHBhnAeYtJIy3j5DATTm_FxXyOguhSW_M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1da4d2bb8.mp4?token=WEd2V_l34TGNiu-2DvXnHkWdsXYBBHZL-ZLbNSBCV00BkLXTIze5KnmUCSAmcIOCT3kjQSY_OlAMbTetoPDCfwAmE8hwhXrek6U_juh3qV28tH_hL__iB6ixCKf1ciFfCFT0dgdoWAHZqbL8KHdQSePLuAPaRD-Dtp-n1Ei4AoNsK1d2MtKzhMjqB-EBlRsugQRF669VP-D_p3Ufb7eCnQyIg_CWajeWmmEwRAI-c6647r7rl8v1Kl1ENWcBVzxnMerLgYkDHRDHSwr5G3KXRn1Q7CsKQxX7PpqleJtcAeJABtpEShKFq9cTex7DkWmvC0G30rgu6v_3jvLVS-i99S4VqdSgI-GSzdxiYA4d2UUGjvGFwPreKB7da3l55odh-gcuQtA6h0lIMTw7C9PJjIXIltzXuf0lWiNDaon5ss02TxfsdBpmrWYAeB3RKKFGDvROn6Mnxx9PktOmJxEDP0qEZfKvU9jf85gDb-ovN_dQvjQHpmUAl8cW0uGnjj0DhOn4XBIcHvXwyVVY5O7a8l-j7Sr0V-fYdso5U9-VRqINnYSn4YJgjiIeWAI7EJ09R6H-rTx3ZZuq4zJAmuS5pcOmHS-Buc6p1tJ-mQe4l3yH-RhPetXaNsfdqizz4qntMrY787AzEuJHBhnAeYtJIy3j5DATTm_FxXyOguhSW_M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
▶️
اشرف‌حکیمی و امباپه در کنسرت بد‌بانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/101794" target="_blank">📅 18:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101793">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b632e2b27.mp4?token=h9acIYAbgltA3a1c52mhmUe8-1gKFqSUxl9R9oz72_vYyAmVo0L1nkYgav6lmzpz6HoiVZB5g7dhRFwDJQfI_9pKdSnv2_YND9ctSqt8l6lW7NlE5cKa0umHjn5zCZtLMdR2v_bkKVtoK79MbLXmiYzVOJy0BRVRHgACaonfh2pv8nmLO14QeB5PZ7BK6gkdAOKzX_ad-h1I9IwpDjmuD3mG4Ic2KHMMIdtPgn_kxKl--tZcNwT0QAjWENwiK8p1NiZg5UgigX2_hA2O_7oAvbf3qzg6QOSB3IyNnYIvtrpcqibDbayQ3KlKoRNJ_Lo6y_PQUhjKGRynPOj8Pf3hwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b632e2b27.mp4?token=h9acIYAbgltA3a1c52mhmUe8-1gKFqSUxl9R9oz72_vYyAmVo0L1nkYgav6lmzpz6HoiVZB5g7dhRFwDJQfI_9pKdSnv2_YND9ctSqt8l6lW7NlE5cKa0umHjn5zCZtLMdR2v_bkKVtoK79MbLXmiYzVOJy0BRVRHgACaonfh2pv8nmLO14QeB5PZ7BK6gkdAOKzX_ad-h1I9IwpDjmuD3mG4Ic2KHMMIdtPgn_kxKl--tZcNwT0QAjWENwiK8p1NiZg5UgigX2_hA2O_7oAvbf3qzg6QOSB3IyNnYIvtrpcqibDbayQ3KlKoRNJ_Lo6y_PQUhjKGRynPOj8Pf3hwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسی همه چیش بهترینه، حتی میم‌ شدنش.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/101793" target="_blank">📅 18:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101792">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e74ccace70.mp4?token=HUHkQJZEiBlQnC9OwVZwv83UH0-xemTVGhBKOIK4UmHyMeSuSIYNFpsM87onzKcUTU12hpjvqJdq7qCssROh9XrTCVO0hmQLoqy3y3PcGy5yoQUILrPbzsxPiAFiu14RmxQHqUf2cdup02MaHnKvwYomGnAJNGI9QxrxgCKERObxlU1WqLfpUcBIWz2VmJ1KLfGMW79oNdVOrQtG3fqGbp9AA-p26AIIhTF--t_3skumUAlD5SL3kjIXSRXubczfy2HTMYHeAbFc0HkzwgNoyjrfXghfbnik0oMgUYMHyYsc7T3mSux55fySF5fwEkeuBeoa-znX_v1AIySYyfFwaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e74ccace70.mp4?token=HUHkQJZEiBlQnC9OwVZwv83UH0-xemTVGhBKOIK4UmHyMeSuSIYNFpsM87onzKcUTU12hpjvqJdq7qCssROh9XrTCVO0hmQLoqy3y3PcGy5yoQUILrPbzsxPiAFiu14RmxQHqUf2cdup02MaHnKvwYomGnAJNGI9QxrxgCKERObxlU1WqLfpUcBIWz2VmJ1KLfGMW79oNdVOrQtG3fqGbp9AA-p26AIIhTF--t_3skumUAlD5SL3kjIXSRXubczfy2HTMYHeAbFc0HkzwgNoyjrfXghfbnik0oMgUYMHyYsc7T3mSux55fySF5fwEkeuBeoa-znX_v1AIySYyfFwaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
🇮🇷
عباس‌عراقچی وزیر خارجه پزشکیان: توافق با آمریکا بهترین توافق ممکن بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/101792" target="_blank">📅 18:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101791">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AsQ6EWuiSft4lHqcaeqpG6MNs85sTi9c27hofzSR-0whWETCJ5aK3yyM14q5R3lNmAHZ7QeoJ8BxrUdkKLgpRjvEkGtTlfuJN3xmcPa3a4uTSVWb6wJ9TflqakIRbcGY2DCEK_SpXDUq_4KRB550ROLmFLGFiq6cS0DRwaqlqFTcrtjSX1WR-KLj2myB36C5cOaicWez-Y6TwBLBUPOMkL45DLOks1C6Asafg524C_aN8vOThIbZznfSLgBaJo4fPa4KyTBp5BXTRh_EGMuzQ8D4ayijGBH47W5RL5lRWibJ4BrsAUfVwVmv7aMUQw8CD0tg_sgXvzR1XhlS5AiG2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
💣
💣
💣
💣
💣
🇪🇸
خبر فوری: فلوریان پلتنبرگ: رودری اکنون به طور رسمی یکی از مهم‌ترین اهداف فلورنتینو پِرز در بازار نقل و انتقالات است. مذاکرات با نمایندگان این بازیکن آغاز شده و پِرز با این انتقال موافقت کرده است.
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/101791" target="_blank">📅 17:59 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101790">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👀
یک استعداد دیگه در کارخانه لاماسیا درحال ساخته شدنه؛ سال‌ها بعد اسمشو قراره زیاد بشنوید..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/101790" target="_blank">📅 17:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101789">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gUZnEgvaolPyF9TaSPKucLd0CUyrPLfHGMj8hKZKOxT7N2-O56wrUy1QHJSMKv34LzqBIGmp3ui4-mRkHY3p_SRWr-IQdQJqfbTeTBwICFXmPTmrWiMLUUHIijLqTeI-2DfFNGi1EcdyfRK4_KgbfX_kgkGIsCW_bMzXFmJuq6hJXHhv_norx4TQRgDtQVtjfoApqTPtQUuuFQjmSwe6H7tp560o7Lr_2w2uwVlCV0HsuP_e0seelZRnF8GJijXkz0VbYPn4ZBD673kEhyMNnNUERvvxETZfjWAQ19ynqyGK5XpoNfBd-wrxwiclaJtRyTXyvZW6F3czONR2GnyVuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
✅
رئال‌مادرید به رودری اعلام کرده که مشکلی با عمل جراحی مربوط به مصدومیت غضروفی این بازیکن و غیبت برای چند هفته ندارد و تصمیم نهایی برای عقد قرارداد به این بازیکن واگذار شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/101789" target="_blank">📅 17:26 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101787">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G8SA0N4wMbMBeQPZovhlTR1-eHb701jxOBKpfcuNAvARDrZnVFJO3uaZihrg6kG4kUWycH8lIAXxbE0AzH8hXE_awpe7xy3U7CHAQqDYn4P0vJ8GYkKrh6s631wyQn5dEFcCBZczmII-gWZURnkjHxRDfeCxcOp4MrsDVZsxGUNxaxM0tiyMw0TnnQJe3z4qzDWwiwpvIs05LPNaFOQJRu7pY_BMYrruOpknjymB4a2b0DxrB8nVWxRvXmvhxBfdIV3MaV2iYJCZey4PKzMBWnUuGT8bxiWoWfuccMwSsl4Be9zUGiZKprzFI8BI-iJuQw4w7rTxngxXJl2SS2Oi1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gswavkTigrPjwUIjTZM_tbs9e6VQuqpZOcSAdcE_tmRL4ULfxMmJQ2XFfGXY5gQy9vTSriKhlMkIrGaC-mjLyRi4OLeY_Hv1Ynz97c2iUHR7nSRt9R0E3823QoERlxTyCHrnmnD4FKSnysgq2xHKtmnVdOyJNQM9W4--vwnd7wOLwHCaHVMf3qn1e1Z_wWVnL0Pdte1b8tCLbF1gIi2hQ-FlhLIr1e7uprbtq13F9f0RbTPGHEUlRiRjOiDYMFip-wHH50hPWyJQmgBw09SqeGT_Cxp4pO1p8V4yaRUfldsOZQROO-OClKa5ZhD-p1Up-U8TEujbAaHyW8eXKdHMRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
مشکوک به نظر میرسی هالندعلی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/101787" target="_blank">📅 17:26 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101786">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FpRJw6B4M0EBkUjCD9IqjPeVqfZqFjI16HvvYdPVuSWTdpOT9KJWhwZyZHN2n9rUSvrwVJtckt2XxMn2kW6PyUgQlSkvCuz54X5fdePQS-VhinjRejRbRixUIZHizq53fHLQgjEhCXLqueKWwEr5bIPCMoQ52BWrz-NzFZATd50Ei7bSbpTBfQLQ_VOGozyv_t-JTxK5LpODhswjZl1sa_Rnnq-2Yc2ruL_iLirKx-YgYmaG7c4RBWoIlegq4KkAtfCv46IwpbdLfIrv_VTPPkgNiel3z5P8XBdfhGDeH9Qvn314uautBv60L7OyKOyp1U1corwlo-fv2zZI_60Pog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
اسپورت: منچسترسیتی با توجه به شایعات جدایی رودری، مارک‌برنال ستاره جوان بارسلونا رو زیر نظر گرفته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/101786" target="_blank">📅 17:16 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101785">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
⭕️
🔵
براساس شایعات منتشر شده، قرار است یاسر‌آسانی تا فردا به تهران برگردد و در تمرینات استقلال حاضر شود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/101785" target="_blank">📅 17:09 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101784">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eSJkm4TOuKkGZijylTfmFbJS0y_UWk7nTd-JCO6xCbmffoRJMt8HRaKEqbyNli3axXmi8ET1y-1yKmpaazhla6z-4j1Xz-SioaYENksJehlRB3zOMCGszb9G6mA_Fl0uz_UOGArP3nHl7vkxTRTSWu5dMI4smkjL_7HGTFvq-fIbHHhA89brnR8nvxRdu8E_rl0jg0vYXOh5-23CTbTslXOiQe51WS5LSzvDWx0R9JxqK08RsFZbWycMUs2Qzgg-UEeVQf3s_kGjs4GcherqZiLrX4muuXzpv60MHNjTIWXpY6McCfCbH2QSu9-OaKmBPsGjHGYSO9rqNVSR2TTgBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇹
✔️
به نقل از گاتزتا دلواسپورت، آندره‌آ پیرلو سرمربی جدید تیم ملی ایتالیا خواهد بود و این قرارداد به زودی نهایی می‌شود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/101784" target="_blank">📅 17:02 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101783">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e1ed1b860.mp4?token=UTsG2JNBpCPIbpq_camSv2RVSHIr27d7dPrLJoJ2y5-HGgcqZ4sY2HmeE1uUyC0pVORjlpHfY2PNafHpOzpnnBRPXZAyzZj1fpX4RCG_e1BZW82oHKFgZMFZsQhg76NR9wlYW4kZt7zivx6FKY-SM3S4IHfTMN5L-fptldWycrmO0pwonLOqSEaW1wZ_ZWSz1c9SfizIRoClMkh3OiSzxHC9qjQMtSeWQFkboEdPrCv_L-WnOQZaluaHJXQsrF-mY6ib9oOVbsCZ_SprvpxYeg24q95I_5zfggxrqtzM67fIwJzHndYgK3E37o84HCoCIIHso7wegAPmhnIJdyw_Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e1ed1b860.mp4?token=UTsG2JNBpCPIbpq_camSv2RVSHIr27d7dPrLJoJ2y5-HGgcqZ4sY2HmeE1uUyC0pVORjlpHfY2PNafHpOzpnnBRPXZAyzZj1fpX4RCG_e1BZW82oHKFgZMFZsQhg76NR9wlYW4kZt7zivx6FKY-SM3S4IHfTMN5L-fptldWycrmO0pwonLOqSEaW1wZ_ZWSz1c9SfizIRoClMkh3OiSzxHC9qjQMtSeWQFkboEdPrCv_L-WnOQZaluaHJXQsrF-mY6ib9oOVbsCZ_SprvpxYeg24q95I_5zfggxrqtzM67fIwJzHndYgK3E37o84HCoCIIHso7wegAPmhnIJdyw_Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
مهدی‌قایدی ستاره تیم‌ملی ایران: اگر میخواید عاقبت بخیر بشید، بچه‌دار بشید
😔
😔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/101783" target="_blank">📅 16:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101781">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tzl7Nhl8p0XBQVEyE18ZXbZmn5vwhfwL1yvZrwyjGX8slqO1q8KJ6vmDJX8tgQv5Tpyrl-roA91CcXXOv3HGlUfuzf-pOjWBclGcAt-PkTHtu7R6c6BJ70wfEZdVVgWI_PBiF9wRRBterRn8V4EWjCyPKyjfYDP-VVnUIKZK5J2QXeng6YrVQUwKio51iX3vqIeUoo-q1SnSSHWobCZ4O6SDJFoPx4cmQ2J_VSOHXgWJ-tvQBX_1pM06pvv5oYFwHh48we-toOqk-xECrouArYdCvoOm7gxPgqTZFpyS8Q3IADKhbJAun3sUyYWAJ1RpHaWDxJy80jXhA9CAdbB13Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uFsYZvo1KnYhC6rmjS4eK-2BAEsJXoMKLO6o5Yb93HEWnm-JjhJnqjWMSIwB_voFyhftrHcVWYHXkVIFWpNJu1XFaUa8hRoFB48q8rZdusSTqHBWcDVzlf4DS97C0n6JgKDrXppXVRa24-WT0jzzAOYloYQDZ5oq29XJVvpgXgfM0lLsBJXFj8fvOydqS-LMX1_mlkay2wL6xWO5YQr9-BO_K164rvR6u4EjvhSnIQyQG2Ze_XliX40TvgqYCamFdjoucA9n4ZTBxf474de_Q_BCKuTnFpGqw-rtEY4fWQF4CMcsTGkP29AeHQuBLfVcrPyMOL4qbOYeDBvucAQ_vA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
⚪️
امروز، ۲۶ سال از جنجالی‌ترین انتقال تاریخ فوتبال می‌گذرد؛ لوئیس فیگو، کاپیتان و ستاره بارسلونا، با فعال شدن بند فسخ ۶۲ میلیون یورویی‌اش توسط فلورنتینو پرز راهی رئال مادرید شد. این انتقال رکورد جهان را شکست و بازگشت او به نیوکمپ با استقبال شدید هواداران بارسا، از جمله پرتاب سرِ خوک به سمتش، همراه شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/101781" target="_blank">📅 16:36 · 02 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
