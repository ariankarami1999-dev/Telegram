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
<img src="https://cdn5.telesco.pe/file/NmvmpTe7GEian4gTDnLLqm0XAduXjdy5fpN88Kb93KqZbB0x2dM0WJzw05c-KTePRvBOmnpjccjzyq8D-LvzuSl4SWz2Nt6TMiZ40IXy59bEbn71FNH__mWAd6qQrrXTC-cW8N5B7qHzKVJUFLo4W7sZzPF4xTkcJkD1ndbUX-NM6PiNk1TrYiuoKqi9Bjc8GREGfWOLuDU3BROKVTfEjwTU1-pvtHE_5cAoTzbc8hO_zsUhSOD2vlpU-FHE8BMHa4qyr_UmcZcRekkYb2w1_6vemd1yafFcm4Y4ZQoDTlQ5yicKkZMFcAxDd1dFErFuu3kVO1atbpSa8-IqFkN4Qg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 412K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-25 14:01:41</div>
<hr>

<div class="tg-post" id="msg-106667">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NrVGw4mWFHqLvRJ6CGXiwil_MIQkTACs3545HiNCAaX_gp1FpJS1oW9blDHfTC0w90QZ-MHZxgHhqh01atlf1ysin3qIQoz6AspP1Rvw8geWSLtvtfAd_g3YMO1hk9YL5eeAnY0fBokSknn0XhocA8QcdpBid0rqCSYm2PR3o-xjXSM1fNG8RxvNT1RhlVEouDUSsLsrF9-Afm6aGqBHJI0PGzpj6Oxx765dYTRZpCCAYy_FgYC_JMX6oGllinYRNkC41GWO-wbkNT9d9UActGMYvMs5BOCcWjqoPnJk_a4UgP0x50yLigAwAJMKcL_fgJMn07NLasZa5Jf8TIOEAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
📊
لیدز یونایتد تنها تیمی بود که در میان تیم‌های میزبان هفته‌گذشته پریمیرلیگ، به پیروزی رسید. تیم‌هایی مانند لیورپول، تاتنهام، چلسی، منچستریونایتد و استون ویلا، و دیگر تیم‌ها، نتوانستند در خانه خود به پیروزی برسند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/Futball180TV/106667" target="_blank">📅 13:35 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106666">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d150b918d.mp4?token=Dxtj2faxxpKQBiec_LlxqvTnidrRCPFXJAIkzsH00zePRPzo_jdYAcWJuLECDWBPzAQ7SwsE1MaBKQ9acUVghHs9XwKQ81mwuNCBJ1mo1T8XOm-KaFhWlSet_4OpqKv_NSeIqYxebb9jJgx5FMwOOqNDCjpOUtlotWoYZPBnFVTC-my94_Sp07tLeSfbe3QMpSDp96nReIO7F7E4qDnZ0LR78JdctbjI-DqeKdwkemz-b2_N-6Riae5PTaPCqKzYVqvahCA62Pbm1PIxPmhHQ2nQV_lMAuSCYV1n3RBfqFawzSwExItxGT92k-a0XsnUmbquicvR7Xsnvf8Af0XO400I5NLMVSRGknaRULWProfT1PNZtefNQmikgc2hR8BX5iYRS-6-kZkTUQ4Bh4BeNEAu4AeNBbPESGFv0fZELjVDRonVqWW9w4MFzPDWsxlQjSwF_OYH6G_-jadi-p80QVub29GXYfLyFL7EnqwukE-lVm5DhPo2n1M6FY9eAvYuf0Qger9gOyoZ2KscxNMrGC8bDeoiksVyslAyBoCqyq9W_pWyd3Y5cYtthtpr-Vq2VZvExO-SbpeJ7r1yWicdL7sl5C9fUlu8Q4Zy62SqrPK28QjQcR7Z-ThwpbzssZTp4HXWc1I13vgqKijHR9lTm4Ze_TEOwIEn4NZd0Ev24dU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d150b918d.mp4?token=Dxtj2faxxpKQBiec_LlxqvTnidrRCPFXJAIkzsH00zePRPzo_jdYAcWJuLECDWBPzAQ7SwsE1MaBKQ9acUVghHs9XwKQ81mwuNCBJ1mo1T8XOm-KaFhWlSet_4OpqKv_NSeIqYxebb9jJgx5FMwOOqNDCjpOUtlotWoYZPBnFVTC-my94_Sp07tLeSfbe3QMpSDp96nReIO7F7E4qDnZ0LR78JdctbjI-DqeKdwkemz-b2_N-6Riae5PTaPCqKzYVqvahCA62Pbm1PIxPmhHQ2nQV_lMAuSCYV1n3RBfqFawzSwExItxGT92k-a0XsnUmbquicvR7Xsnvf8Af0XO400I5NLMVSRGknaRULWProfT1PNZtefNQmikgc2hR8BX5iYRS-6-kZkTUQ4Bh4BeNEAu4AeNBbPESGFv0fZELjVDRonVqWW9w4MFzPDWsxlQjSwF_OYH6G_-jadi-p80QVub29GXYfLyFL7EnqwukE-lVm5DhPo2n1M6FY9eAvYuf0Qger9gOyoZ2KscxNMrGC8bDeoiksVyslAyBoCqyq9W_pWyd3Y5cYtthtpr-Vq2VZvExO-SbpeJ7r1yWicdL7sl5C9fUlu8Q4Zy62SqrPK28QjQcR7Z-ThwpbzssZTp4HXWc1I13vgqKijHR9lTm4Ze_TEOwIEn4NZd0Ev24dU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇵🇹
عملکرد ضعیف اسطوره رونالدو جلو العین!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/Futball180TV/106666" target="_blank">📅 13:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106665">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a01bac8019.mp4?token=ZGQjUbREnlEKepIO2wGrbPPJLV8MS1e3XFP8noFN3o9WV1_Hu0s5rSCxDWZGcqBgmCWhCFxRbo04vAgXh92sWlAa022kv7Y9mkZmCA6WtvirshyGiFdSfdL1ZrpE60N0r7QQ0Oo5sgOnUUm7EKh-5Npp60yzb_mg6T8Z4EFd_Ue-hFxxVaYBKZLAMx_TTjs7_Q1fcVu2A6f_uYAyeQuHnuhqtrYsSuFJ8aXkiAAbkEq9xy0KW1CODLse8AA1u-BOmIXDoVB97c6B12oPV_llhLzcpad8GzEqZHZ6MYWlryMEGo3ub4U1ygMI37IHGOLCjBsA9V_W2bIhfr78lq5L0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a01bac8019.mp4?token=ZGQjUbREnlEKepIO2wGrbPPJLV8MS1e3XFP8noFN3o9WV1_Hu0s5rSCxDWZGcqBgmCWhCFxRbo04vAgXh92sWlAa022kv7Y9mkZmCA6WtvirshyGiFdSfdL1ZrpE60N0r7QQ0Oo5sgOnUUm7EKh-5Npp60yzb_mg6T8Z4EFd_Ue-hFxxVaYBKZLAMx_TTjs7_Q1fcVu2A6f_uYAyeQuHnuhqtrYsSuFJ8aXkiAAbkEq9xy0KW1CODLse8AA1u-BOmIXDoVB97c6B12oPV_llhLzcpad8GzEqZHZ6MYWlryMEGo3ub4U1ygMI37IHGOLCjBsA9V_W2bIhfr78lq5L0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار از علیرضا منصوریان میپرسه چون الطلبه مشکلات مالی داره این باشگاه رو ترک میکنی؟ اونم در جواب میگه: اگه تو این روز سخت تیم رو تنها بزارم کم لطفیه و امید هوادارا به منه و نا امیدشون نمیکنم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/Futball180TV/106665" target="_blank">📅 13:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106664">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfbc375b35.mp4?token=FU-_WbLJU8VhfrHs_1sUwTRoemcoP8kehm3pyrjsPJINATx1ukcbPAujHd9quFug3jJN8TKvqE-W7lC6tZeU7LK6Tdub5fOmHbHGp65G7qk52qLBIrO9uRNT4X8uxaZ0YB2atotXd-reLv3X6VKgO1u66OX4sFNVBiUILGoGvNEW-f5i4aZKLjXomrz3A2Dsido_WYear0F8PX1XmmZEqikEHZemOBM_ysQA50g_d8fGIKDEYJG7rOQQTdyHbErHOb9-0BYZzTc3dc3aLJ9DuMrGy-XV7my-SGPmW5zKwRwYRO6kg1bmRtZA8EscOuhMA4H65_wykVTfaTR6LRQrrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfbc375b35.mp4?token=FU-_WbLJU8VhfrHs_1sUwTRoemcoP8kehm3pyrjsPJINATx1ukcbPAujHd9quFug3jJN8TKvqE-W7lC6tZeU7LK6Tdub5fOmHbHGp65G7qk52qLBIrO9uRNT4X8uxaZ0YB2atotXd-reLv3X6VKgO1u66OX4sFNVBiUILGoGvNEW-f5i4aZKLjXomrz3A2Dsido_WYear0F8PX1XmmZEqikEHZemOBM_ysQA50g_d8fGIKDEYJG7rOQQTdyHbErHOb9-0BYZzTc3dc3aLJ9DuMrGy-XV7my-SGPmW5zKwRwYRO6kg1bmRtZA8EscOuhMA4H65_wykVTfaTR6LRQrrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇦🇪
🇸🇦
هیجان‌بالای گزارشگر خانوم استادیوم هزا‌بن‌زاید العین امارات در بازی دیشب مقابل النصر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/Futball180TV/106664" target="_blank">📅 12:45 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106663">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e050d24ce.mp4?token=WZCHgDQh2acCHspOHYCgCyrvyHeu89nOILtZH_Tarr_x9gEUc0GLMWfhSoH4SkHdniVGNsx-MJywP6pFdzwX38U-a27HXrrqTsFR36dnDHIgWMYBPv9e6Rviqfj7xjL9rReCtOpd0ImFH-p4__YUBwCySSkcppfuppo0sGMQpnKBipTBsPH1hVxwn-LXqCNAvnWfbGOgTuGP0ppShSs3UfbEQ7hMFGhygNbDhSLXlDgHTYas1bNd4DVbrLuienmf3nbo5BOB3eEqk2_XnNwuSnryHhT7A4ZQWyj2OFIIk2EV1LIRlRjNChZ5ML_E9GFHqa1zyH5ogPztBiIwwWDNjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e050d24ce.mp4?token=WZCHgDQh2acCHspOHYCgCyrvyHeu89nOILtZH_Tarr_x9gEUc0GLMWfhSoH4SkHdniVGNsx-MJywP6pFdzwX38U-a27HXrrqTsFR36dnDHIgWMYBPv9e6Rviqfj7xjL9rReCtOpd0ImFH-p4__YUBwCySSkcppfuppo0sGMQpnKBipTBsPH1hVxwn-LXqCNAvnWfbGOgTuGP0ppShSs3UfbEQ7hMFGhygNbDhSLXlDgHTYas1bNd4DVbrLuienmf3nbo5BOB3eEqk2_XnNwuSnryHhT7A4ZQWyj2OFIIk2EV1LIRlRjNChZ5ML_E9GFHqa1zyH5ogPztBiIwwWDNjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
✅
قبل از ترک باشگاه چه‌کاری مهمه که انجام بدیم؟ برای دوستان بدنساز‌تون حتما بفرستید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/Futball180TV/106663" target="_blank">📅 12:20 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106661">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HC4tR2rKlUBaeu7u1TBft-l_bPjD1AkuQZBgj7wL2lCw8CQ3eCuxAzBmv3U9vYw6z79eQt9C97G2gfluv9evJ2M5ude4nbJ4mgLqcfPsaJfZ-fG23SqPBMJ1wFMH_Zma0ib88DvFnImuHdRHI0x0uLgF7GiCtZesMl74e0rTKi1xSciOHRvsoWnC53EQRmPSBjSkn3GpKZoeecWGvKxCMvrAGz7QfOYlxb7VJiG6a9Xi9Ub1mEeRY9n9L4HLZ6-LQhSFl9PwQ9J9MQPpNEsOHa4T1SUIVDXyktHs55zEjM0cgFnL_LKJHJ-5MazJpCoXCp-mKr6fpaqo--czPaC-aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pz0k2q6k9mx7kf59CrM9PSNPNgn6crgTdxDU3BPPbjcqycDX3OgQiWDlaeOd9UA1gb7aVSEYCE0EmeumO4FEhChjVT_iDnS4X7kZNSMCzlhCPTQdlw4H0FSBYp3BTE1MmzKEjjNDv35L5_EOd9lgBqShofLDscndIy-6TQhfCagaIDfy4iV_8DZ187mhqgBEp03_u1ZXdMNahN__yhCEivpeZvdj0Kl3_IHFHgQOkYwp-koKghWaXky2Upph1EwvZoHBx6io6VJFoR3RkJocr1mSdprssh_5inZeC3_AqdqxljPILdMmCjVoc66IDQ7tg1n64A4r9zDIH3QZLUKHcQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
عکس‌های جدید شکیرا در ششمین دهه زندگیش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/Futball180TV/106661" target="_blank">📅 11:57 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106660">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">‼️
🇸🇦
🇶🇦
درگیری شدید دیشب بازی الهلال و الغرافه از این زاویه؛ بن‌ناصر بخاطر کشیدن موهای سامرویل کارت قرمز گرفت و جلو استقلال غایبه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/Futball180TV/106660" target="_blank">📅 11:50 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106659">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106659" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/Futball180TV/106659" target="_blank">📅 11:50 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106658">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nmnbf4s2u0dHgeeRUoD5g4rgcQHwi_Jcgzpr7U-NM7VK-g3angtBKTvW5uCeNcNyrRfquk_GOOkm1cEJGgoQfnFc4Ic62YkkjCnzwFsn6xcbW0S2ty7JFu5jIo5MUtttsfpJ5y2FLMt5lzw0zte3gQdwqL6sj9ZdSX4ZuU0xFBOJjtNdl5oM035rDZplgH_8M7qmEYK1NQHOuQ_7LIaWPa4hYKxw5GFBJS9GB3JvbhBrurQ2KfAHAsySj8uycj5LWHkfIwEf7vporVJznIAtWqdft912pno-2m9ReV99e9XJ0pnuWoiRYq3AikBmak4i94JkYbVVmcMEvya9sVdo6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
جدال جذاب لیگ اروپا!
نبرد هیجان انگیز
⚽️
بنفیکا
🆚
میلان
⚽️
را در
TrexBet
پیش‌‌بینی کنید!
📉
نگاهی به ۵ تقابل اخیر دو تیم:
⚽️
بنفیکا: ۵ برد و ۱۵ گل زده
⚽️
میلان: ۳ برد، ۲ تساوی و ۱۱ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/Futball180TV/106658" target="_blank">📅 11:50 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106657">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qp3RSa0INf1IKRlWK0xPQ4KByasm3vo_w0QKte2s8CT8a-36sSEzLNpIwzVda0Q9scTcaiNPvRnSyw1mOwGptPgFj1z1bJBYDzRrAh7QgqlQ5XWMdRK7w36qpkPF5fdVYRJyVyQxlOC9-RZ1dKGAzvtjP-1Pj1qEPZl0KLICedVOXi1UVhj0fTRwJf0KKkTATHJK4ElK7QqiVR1VLB0BTb2_8e_itn_XUNh_-eH3DXM_1la-GClolpJhck07MUt1YRy8UF5oSxs04MFBreO_xsL-iYtdcko--latbee1Kz9gXSY7TbDaPRg8Vp0pLi6XoKPd2IKKVarvt7qSTI82-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
📱
استوری اسماعیل قلی‌زاده بازیکن استقلال: من هازارد فوتبال آسیا هستم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/Futball180TV/106657" target="_blank">📅 11:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106656">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/796caa8457.mp4?token=sPyer2Ewtz1v6gV4okaS_eaxBl5yBDHnwW2GCgJjUaUpewklViqF9E-2nysNjlscbzNgo5GSF2avij1aHe3bfq0xBJ7-gdSIklodynFrhBOvUbQ3MAuvX8a8x0jXAiO5PxMSEEy841C-ssnZyjBHl9Y0dzz3tKJNQUogo2A3cEvRu9LXATYXhb992bj9mKOMht5Zetc6QgQGvnVJigEQszNBMrpIk9YevGSOUc2KaYTzYS3CHsPD-hXRAPajnozQtSq3G3YWPDt3QYaIcnB0QcwjOv8FEhT2xNlL4bUGb3RHQ_veBUcZmtHAM_qSJqhvzRfM8_LCeM6YpK5qF9vtmrYGQZoLKOfVv8FxTArSzSQiyPBmJnjafT2p92kNJVvTxPUjKX8BVuguUcBv03u91U17Mrao_r9Ac1CWRjrmilScSCKsOf_1wmp1nk6WN8q7xL1nu0Lda88e1S5bzA3sfR_Qyb8V7Tpfrfp1teKjkl5S0hDI904fcR_IjAGZ4fvatmZZhn31VCQsT0TnA5ZdGAOYNYhMGn7QD9E0u59PV2KhJhDiZHFVrgm1bePty1bcD351KDybKKI26sq0e5djIQ06B-9EDVemGx9OXqyohKdg7wjssQiYhARKyPn5RuDkbpwUJ4m7wEgQCrtkrbQMbRGPBwq0tFNugF0NAJj2PSo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/796caa8457.mp4?token=sPyer2Ewtz1v6gV4okaS_eaxBl5yBDHnwW2GCgJjUaUpewklViqF9E-2nysNjlscbzNgo5GSF2avij1aHe3bfq0xBJ7-gdSIklodynFrhBOvUbQ3MAuvX8a8x0jXAiO5PxMSEEy841C-ssnZyjBHl9Y0dzz3tKJNQUogo2A3cEvRu9LXATYXhb992bj9mKOMht5Zetc6QgQGvnVJigEQszNBMrpIk9YevGSOUc2KaYTzYS3CHsPD-hXRAPajnozQtSq3G3YWPDt3QYaIcnB0QcwjOv8FEhT2xNlL4bUGb3RHQ_veBUcZmtHAM_qSJqhvzRfM8_LCeM6YpK5qF9vtmrYGQZoLKOfVv8FxTArSzSQiyPBmJnjafT2p92kNJVvTxPUjKX8BVuguUcBv03u91U17Mrao_r9Ac1CWRjrmilScSCKsOf_1wmp1nk6WN8q7xL1nu0Lda88e1S5bzA3sfR_Qyb8V7Tpfrfp1teKjkl5S0hDI904fcR_IjAGZ4fvatmZZhn31VCQsT0TnA5ZdGAOYNYhMGn7QD9E0u59PV2KhJhDiZHFVrgm1bePty1bcD351KDybKKI26sq0e5djIQ06B-9EDVemGx9OXqyohKdg7wjssQiYhARKyPn5RuDkbpwUJ4m7wEgQCrtkrbQMbRGPBwq0tFNugF0NAJj2PSo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
برخی از زیباترین پاس‌گل‌های اسطوره CR7
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/106656" target="_blank">📅 11:05 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106655">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc02fbddb0.mp4?token=bwRUaBxiCoVS9nPodx44PmULUBeKfZRjc3voDS8yGpoAo0IkHPSpcLL24cPcpmHXc5mswQtJq7pZ4XWfDI33eOy3lj2UysKNWL5XiWXstl-m1Az83PHrC9QkKVE_TJYR0SV2moAPEPYENxpbzJfHFJoudcVPHjtcZ1hXbykD8WyYoLHwZi3XRTiVtxz1SXWdz1jCPKuUf-ZLyL02kQ2FUohPPJ1JLJCoao_76VLkSvojB3US2wQ9928V8jqkNjoz612WApqsGnY5Mk7zYP0xlAe9q1AQgqQOwnUTA9DDuG90Fz2mvh6z_ZFxBQloEb0FmgLxOH0wff2GgaxL6VSkfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc02fbddb0.mp4?token=bwRUaBxiCoVS9nPodx44PmULUBeKfZRjc3voDS8yGpoAo0IkHPSpcLL24cPcpmHXc5mswQtJq7pZ4XWfDI33eOy3lj2UysKNWL5XiWXstl-m1Az83PHrC9QkKVE_TJYR0SV2moAPEPYENxpbzJfHFJoudcVPHjtcZ1hXbykD8WyYoLHwZi3XRTiVtxz1SXWdz1jCPKuUf-ZLyL02kQ2FUohPPJ1JLJCoao_76VLkSvojB3US2wQ9928V8jqkNjoz612WApqsGnY5Mk7zYP0xlAe9q1AQgqQOwnUTA9DDuG90Fz2mvh6z_ZFxBQloEb0FmgLxOH0wff2GgaxL6VSkfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🏆
یهو هم دیدی سر توپ‌طلا غافلگیر شدیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/106655" target="_blank">📅 10:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106654">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f24687d0a.mp4?token=oKAoiEqp2jsoUcQ-m6u7Ik48A6BEhfFl6cGTzyqT68XHis91i1Z35Jwfq_i73Yxr6E-GiMcLklIuZ441iFZpvl5qTno8iDYOtURIFXlpg2nGaVSW7vGcyX2YFQanTA10nH5NVpKOBsQ5LY5HsAglCJ4zj4zZa6lPM1dY40A9nspanbh9H44Lsk9Zqs4lxgJnaU-OZLaWrz65WKfCyItfafP9H6I3UDBgLvZFIa4uUTymjuBe-IqnxcLk3O4i7GdXCJrqtEA4aGQXZm9dPdoFaG5WBZ6zzAOYhkL2qx5LLYZRoqQUM2qbfj7NuHpfPegt7lU4oELcBtqgBO49ONpdHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f24687d0a.mp4?token=oKAoiEqp2jsoUcQ-m6u7Ik48A6BEhfFl6cGTzyqT68XHis91i1Z35Jwfq_i73Yxr6E-GiMcLklIuZ441iFZpvl5qTno8iDYOtURIFXlpg2nGaVSW7vGcyX2YFQanTA10nH5NVpKOBsQ5LY5HsAglCJ4zj4zZa6lPM1dY40A9nspanbh9H44Lsk9Zqs4lxgJnaU-OZLaWrz65WKfCyItfafP9H6I3UDBgLvZFIa4uUTymjuBe-IqnxcLk3O4i7GdXCJrqtEA4aGQXZm9dPdoFaG5WBZ6zzAOYhkL2qx5LLYZRoqQUM2qbfj7NuHpfPegt7lU4oELcBtqgBO49ONpdHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
گل سوم ایران به امارات توسط مزرعه(89)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/106654" target="_blank">📅 10:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106653">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/679dc80276.mp4?token=LOr-5fY7ihEPIWtPbQvgCHmm1lTWGY-HKQbHIK8LJzYfazAEFd_1z-0_wH7NN_7EgbCoVQ8LfujgPXSMTo_i-NzmKkiQzkn9VxEhWZGIqBLUAIgzh2ILvFQbPlQ1hP7srNntgBMoqTeDytoiAC78AgJFAE7Bp-UZeYJAhc9PmGVQdobZAa0nqiNvE2_IZ8BrvCYEU59tKj3TeJxffy3CmoT67ixa59Iy3R-zp3Ko7QaoHVTKDNf61T2wTSlhAwUOMwlvnV3nxudEqEwt9NHWocvjyFh74ostjP9YP5cri03aFVCof0PYQnPL1nk4JwXvi1GfuIKzw29k0wdIUtbZ1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/679dc80276.mp4?token=LOr-5fY7ihEPIWtPbQvgCHmm1lTWGY-HKQbHIK8LJzYfazAEFd_1z-0_wH7NN_7EgbCoVQ8LfujgPXSMTo_i-NzmKkiQzkn9VxEhWZGIqBLUAIgzh2ILvFQbPlQ1hP7srNntgBMoqTeDytoiAC78AgJFAE7Bp-UZeYJAhc9PmGVQdobZAa0nqiNvE2_IZ8BrvCYEU59tKj3TeJxffy3CmoT67ixa59Iy3R-zp3Ko7QaoHVTKDNf61T2wTSlhAwUOMwlvnV3nxudEqEwt9NHWocvjyFh74ostjP9YP5cri03aFVCof0PYQnPL1nk4JwXvi1GfuIKzw29k0wdIUtbZ1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
🎙
انتقاد طرفدار همیشگی هادی چوپان از رفتار وی: درس خیابان با ساندو فرق دارد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/106653" target="_blank">📅 10:15 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106652">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eP_bcI_FmXx-ZQxhJftO-v54ds0Ka6DmSyhWMEQCT2HgSVt2ZqMcmRwlkJ5VK7A1Pb7dsi42jk0eBDCazeVPjC1v1EGiRfrslTrVhKfNGra2OCNhU0Kgtqun4_8pYtLeoJh0fyLy7y6p-gte8PsMNjGGf2zMy-UTskjQqF5_7eYbQ9xLOoE86OU0Bhaf-U2lOAtQsquUQOkOjW0e-73dmw-lAKq8WP9TdVSVcq8F8ZfeP1KXGKMBEkW68ZgD1_i6pP2Jgw0OkmvFYIV6tXB0s3WPp-7Izb-p-crwAZXGcVZtpz-maCEMcEdesBZb9kNMg6iRlbO7f-j9jiDZFbnWfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
تفکیک گل های لامین در فصل های مختلف
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/106652" target="_blank">📅 10:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106651">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccc7f1ed9d.mp4?token=sMyQWjz1hXrTbcetGdaOV7O8heDlT5PssfOlNOwYalZ5lk4hrMfXeP1jtdWZsUopaRQLlSyWZ5uQEY3ble1OZeJ4SIQb6o-7Q-EcYpgKUoAxoZ-meRroJwCPaY1HiewNrf6359gGtYYMf-aY7S3tMferdtaZy_e0ilGf0sTyfV5nhGe-9SCCjtS2-IOvlnxMEYSmMrBOVzOOS9dv2Spda6N3dSP-PVGzTTb6nKa9Q_TojrXXwQf7tJ-Y-rIaboh_eebopZh3Oz8qi8mZnjzII8jCU7CWT5W1uUOIq9Szc9IXpaWlsI-X4Hhr2o6Pdrma61oXCNMJ4HaPkzo9cZXtIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccc7f1ed9d.mp4?token=sMyQWjz1hXrTbcetGdaOV7O8heDlT5PssfOlNOwYalZ5lk4hrMfXeP1jtdWZsUopaRQLlSyWZ5uQEY3ble1OZeJ4SIQb6o-7Q-EcYpgKUoAxoZ-meRroJwCPaY1HiewNrf6359gGtYYMf-aY7S3tMferdtaZy_e0ilGf0sTyfV5nhGe-9SCCjtS2-IOvlnxMEYSmMrBOVzOOS9dv2Spda6N3dSP-PVGzTTb6nKa9Q_TojrXXwQf7tJ-Y-rIaboh_eebopZh3Oz8qi8mZnjzII8jCU7CWT5W1uUOIq9Szc9IXpaWlsI-X4Hhr2o6Pdrma61oXCNMJ4HaPkzo9cZXtIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
گل اول تیم‌ملی امید امارات به ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/106651" target="_blank">📅 09:49 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106650">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6962fda1a.mp4?token=dzZzlYuXBFn8Imkvo6O1KamMVcg-G3qjqTcBHM5E3hmMS0jcOXvTXtdlHRchhO4c0O2KqrRHbHjoEBrPsoILW70aFmT8Sl0lkQA-UQHHhdiyNXDCXbkR0bJNqkYha1dF1iZ9d7F0Af7n-zrg7-I72NS6VkKQwE6iiP01Bj2GTruUUSQq0g8tDu8BcfxIowglnoaQI7anc3Vo37xHHgCrAoTHrlExf0Nww3ShNQ4Slxd9-zwi1Jsyqcjn31g6Tv36apNKoNxlpK-s9SPoOULhZ3seKjVLl6-kyyDNg9k-UgFyh_5aFsqeZ-eDDYRQo2wkd6c4WNiJk8kPnTgEpNieTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6962fda1a.mp4?token=dzZzlYuXBFn8Imkvo6O1KamMVcg-G3qjqTcBHM5E3hmMS0jcOXvTXtdlHRchhO4c0O2KqrRHbHjoEBrPsoILW70aFmT8Sl0lkQA-UQHHhdiyNXDCXbkR0bJNqkYha1dF1iZ9d7F0Af7n-zrg7-I72NS6VkKQwE6iiP01Bj2GTruUUSQq0g8tDu8BcfxIowglnoaQI7anc3Vo37xHHgCrAoTHrlExf0Nww3ShNQ4Slxd9-zwi1Jsyqcjn31g6Tv36apNKoNxlpK-s9SPoOULhZ3seKjVLl6-kyyDNg9k-UgFyh_5aFsqeZ-eDDYRQo2wkd6c4WNiJk8kPnTgEpNieTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
گل دوم ایران به امارات توسط شهرآبادی (51)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/106650" target="_blank">📅 09:44 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106649">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0c59ac2ee.mp4?token=cZYxeQPCds39kDpsW0-zQwWNm6NSp_-6rqddyKVKN1qf7jeK5Mzi_uFoOVyA_M5WGQkzDR4J4riOkwR1JuxAnAGdGG-mU47wHzeRmkxzUICbNYHBDr5SyxWbX2DJIbDoOzTlhli-6u1K7L4-VDW-p0CT97DNju7Imso0jzQvxXiCdwD9UTXdlZs5zE_Dty2FCPx-6Bx8_DoBC4fDF0eH5_INjH-MgBdRFrtu2iwes3owNJAteiLdOJimL_mBcM6HEiKCNRcWJo4tg8P9SvoqwQvT1Ae1fjO5V61WEcQOwZEDOsiVNPUV9BwTFm5zs9I2Rf4BLdwF6T67s7Mt2poF5m4Z13mcH6zjjpnCuG6B5j2INz-KyHayZx2SXhDxHPUDaFiIReI3iOytskHiDY2Vqqi0gkf3-ozgkhOSKchWJx6UXKGs3RtzQhRBjvKE9Qv_SGdkV5sYD7jbW3W_eVeQcQtjv7bwOLgXTn0vPQNiMIM4e7-hf6Jl1kEwJR6NqUlCJKYzhjR7uaC1-AqOMuiEulG8PWMeqcTI2Yn33WMSQMbLO_svPsCua2XjMFd1-EAA6EQMdAi3Ub25n3xoZQ-gsDF2L1L6mAEFS-xp40xrHTFUP7OKl8IY3qFMstHZawG-wZJP0vj44RMYjTS-hry-39udzJ9iZ7lqMO9JM1dGnfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0c59ac2ee.mp4?token=cZYxeQPCds39kDpsW0-zQwWNm6NSp_-6rqddyKVKN1qf7jeK5Mzi_uFoOVyA_M5WGQkzDR4J4riOkwR1JuxAnAGdGG-mU47wHzeRmkxzUICbNYHBDr5SyxWbX2DJIbDoOzTlhli-6u1K7L4-VDW-p0CT97DNju7Imso0jzQvxXiCdwD9UTXdlZs5zE_Dty2FCPx-6Bx8_DoBC4fDF0eH5_INjH-MgBdRFrtu2iwes3owNJAteiLdOJimL_mBcM6HEiKCNRcWJo4tg8P9SvoqwQvT1Ae1fjO5V61WEcQOwZEDOsiVNPUV9BwTFm5zs9I2Rf4BLdwF6T67s7Mt2poF5m4Z13mcH6zjjpnCuG6B5j2INz-KyHayZx2SXhDxHPUDaFiIReI3iOytskHiDY2Vqqi0gkf3-ozgkhOSKchWJx6UXKGs3RtzQhRBjvKE9Qv_SGdkV5sYD7jbW3W_eVeQcQtjv7bwOLgXTn0vPQNiMIM4e7-hf6Jl1kEwJR6NqUlCJKYzhjR7uaC1-AqOMuiEulG8PWMeqcTI2Yn33WMSQMbLO_svPsCua2XjMFd1-EAA6EQMdAi3Ub25n3xoZQ-gsDF2L1L6mAEFS-xp40xrHTFUP7OKl8IY3qFMstHZawG-wZJP0vj44RMYjTS-hry-39udzJ9iZ7lqMO9JM1dGnfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
گل اول ایران به امارات توسط شهرآبادی(49)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/106649" target="_blank">📅 09:41 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106648">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4029ff1503.mp4?token=KyRIgt-63ZJBLf0Q62-fs7hOzeRK18JXcN0iVIo4nIOUViBiQN_QBiQSDozfpYpX_5FcUuLpMtKJUQWLXOxmrRCCHQFix0ak_Epfiag1nygswCpdniQsyrOhXGerY-yU4g5WlH_q4KtmpqQ88m3gIcweSAGu5kJls--DCXDrJcIG6JWpcldA2tm3eMiiXhT0hTCYOPBmm5XDVUXpnkQf6UGVS2a6vKfEdbx7w2rVxjTxEhsnHN_aTsQIO9GIYswu3vApll2rsF70C8aS-_zfwgf77C59NO0OY2r6BJRqSE3eOsJg2G4TWM5Zg-PVfRg4L6gVlxtnHuveqL5VuDO64Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4029ff1503.mp4?token=KyRIgt-63ZJBLf0Q62-fs7hOzeRK18JXcN0iVIo4nIOUViBiQN_QBiQSDozfpYpX_5FcUuLpMtKJUQWLXOxmrRCCHQFix0ak_Epfiag1nygswCpdniQsyrOhXGerY-yU4g5WlH_q4KtmpqQ88m3gIcweSAGu5kJls--DCXDrJcIG6JWpcldA2tm3eMiiXhT0hTCYOPBmm5XDVUXpnkQf6UGVS2a6vKfEdbx7w2rVxjTxEhsnHN_aTsQIO9GIYswu3vApll2rsF70C8aS-_zfwgf77C59NO0OY2r6BJRqSE3eOsJg2G4TWM5Zg-PVfRg4L6gVlxtnHuveqL5VuDO64Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
رئال مادرید با شکستِ الچه به تونل وحشتِ نیم فصل اول رسید.
👀
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/106648" target="_blank">📅 09:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106647">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25ec17c4bb.mp4?token=N-VvoVw1QMPPax5M_egdI4xLSKXamEF-93PmBBAhXQq6VeUL8tURBWJxrPG1Ps26gnXd_LpF30BnTIKkbBTsMlCpal9SH-XF_U4t_Y1aukzL-FH39OIvTCF4x3N9ohgipefAH-VGGGgPsMSNU-E1qAbgBHRu2FsTaw3UBPCPcoeg9FVvngGzrOEOg6a-oB3BA5JSpsgji_U8u2h7l_rh2tGtIjKzfnnbs8K-ORw8JLZnk-lMJxcZ1aSLTtIpA0DHIUN0fuBw4sq_wmCBy9qhmxy8b6MKHizZstIPscRuCRt7dxOW2E2euHlIT7QtLteBf2QeugTz0Pa1ICORmhrvfYSgpJYr-X10V7XydOv8GZXVu0klT3t3tCrnWFAk84_Kztm9VrkFgqTK70FE_UD6cY69bqY2Cfmq2oC116W_LejmCo-2pGUoPhw1_WZdIWxQ7Xspybt89s6XzGqU3r3-MFk4A_B_olVHrs1J5WtjG9D5zghY1_Ms63Mbc9AvMF9ANNXJjtAOA3G8Kd3OwddJr02akFlBDyE1gHU07Adfj1Dazjv_iMPmMR2tXW9hJmBovy_SLTtAfEluzw4UQH6kkgaVe33yyzJ-1VnWEhaOcJybAoRjZe1L5rmaHf-OTfvhldE4o6acqunQ0v8EvEcZtHT7busoBHWMpxZDs3mtM9U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25ec17c4bb.mp4?token=N-VvoVw1QMPPax5M_egdI4xLSKXamEF-93PmBBAhXQq6VeUL8tURBWJxrPG1Ps26gnXd_LpF30BnTIKkbBTsMlCpal9SH-XF_U4t_Y1aukzL-FH39OIvTCF4x3N9ohgipefAH-VGGGgPsMSNU-E1qAbgBHRu2FsTaw3UBPCPcoeg9FVvngGzrOEOg6a-oB3BA5JSpsgji_U8u2h7l_rh2tGtIjKzfnnbs8K-ORw8JLZnk-lMJxcZ1aSLTtIpA0DHIUN0fuBw4sq_wmCBy9qhmxy8b6MKHizZstIPscRuCRt7dxOW2E2euHlIT7QtLteBf2QeugTz0Pa1ICORmhrvfYSgpJYr-X10V7XydOv8GZXVu0klT3t3tCrnWFAk84_Kztm9VrkFgqTK70FE_UD6cY69bqY2Cfmq2oC116W_LejmCo-2pGUoPhw1_WZdIWxQ7Xspybt89s6XzGqU3r3-MFk4A_B_olVHrs1J5WtjG9D5zghY1_Ms63Mbc9AvMF9ANNXJjtAOA3G8Kd3OwddJr02akFlBDyE1gHU07Adfj1Dazjv_iMPmMR2tXW9hJmBovy_SLTtAfEluzw4UQH6kkgaVe33yyzJ-1VnWEhaOcJybAoRjZe1L5rmaHf-OTfvhldE4o6acqunQ0v8EvEcZtHT7busoBHWMpxZDs3mtM9U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سوتی وحشتناک پویا پورعلی در گفتگو با عادل فردوسی‌پور که باعث منفجر شدن برنامه شد
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/106647" target="_blank">📅 08:58 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106646">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a5PlLLgR4kkpZXKMLp7fHYAXt1_nD_dICykRYUPz8J2cEyMFTDaAj3wecI_tIVn5XRVDhMVMs4P5W4iDG-OjwyY-cyjPp6gmHKRBnVKxOu8BnTPL1o14JVmHidt5_32Kc2rFre3XQqfxoV3d0XqRzhXWdpFXOzOPKnXPkoLstASKm9tk2jMaouMAfaeFW6MJhu9nMcHUUWA-TFyvKFlCXIpWwCzqJq5xLMEReGAtQEG1jYtI1ngefSw4C7ivKq1GuLM-UAyX0eNxwH_GXZSMzGgRXXN5PMcmSZMCWsEU7ljUFIQQEnlOjvPmQIwBPsGZHpZwBj8v3y3OPoBPyYW8Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚠️
اتوبوسی که رحمتی امشب پارک کرد:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/106646" target="_blank">📅 08:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106645">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106645" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/106645" target="_blank">📅 01:29 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106644">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iMNp9qeQeRh7m0CxvLIAGAT6mH68CZqPIvpxy_dFIaepbcHGrsjWNWORDy5545uKWEsK6upXGKPhgrYSDqi-vj-s4rEBfPc3ITe8-xicf4ZDAPTejKolkPqypmuQ93-mivZ54zPxIXz1McfinUB43eWcyCWocrkCEv21XrYOKqJBBFtalS0-syxwOHRPlFbe3IeYhgV6av3w3eDSu7qVZUKOqLaskNHyyRlXi-H7q1UsGVuY3aY-9TpWzBOpmMJmLbbrjjoSl8EhsFYM4b1OsdIo_aeUuCO1hRSQYUgBT2sIBV70W2m1sVcKD1ZKoqnPsnkNcmSbRuDb5PeijzyaGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/106644" target="_blank">📅 01:29 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106643">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/106643" target="_blank">📅 01:29 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106642">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MYybT00NXv0Ajeg5pmDLLWIqIn5lqe8_E2QUWWEqn_OhnuqEI21rHui2zniStZ_49-EeHC9eXwubhLXReql2bpj8HLyMz08w-uIU0uCchCRtebyTjV4G7R8-1Z0U58LmQTg5S6_kcj_0vV_AjNNvhdnMxzAp8JBVCTnWrlquQkRt_-zJudNecRjTt_Z06hRVyxfs7_ZiwI1mUd9UpxlLIat3FquInnj9HIYWCUIunNXVwUez2rqC_m8I0B_njCzeFlOlxFQbfzWWPgu0J4xejhfn7COsBbkyUeDRW6iCqXBKBs7oY3bWffzyZf1849lhzb6-OU_LdXPYepkOT8FhVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🇪🇸
🌟
یان دیومانده در حال حاضر بالاترین درصد دریبل‌های موفق را در هر ۹۰ دقیقه بازی در لیگ اسپانیا، در این فصل، دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/106642" target="_blank">📅 01:23 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106641">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F7H-K1f7vv8fGKXwod4WyubJCEy0eVxgwFegezV_1KHNqLb_JufrOzOsuqL7NvIJEKYg9DiHoTEZnDe7rT1fvFCPP4hYVffC31ezP2UIa1ImRvC5wQvDa611UFjQ3BCFW61aDBcK0bK1gS0zDAnuHoe-s745iF0FWRO0QHh6-ftzXfzGeF9rT2vqsh7UVKhp2wfOzkJXeTa0VXk3ADPnoyUjiZeq1ZZ3fIVFbVBV3x7GThEybJeuE_fftAZdCmGq_Xie35cp2wJYamK7cTMx6TTf62aizYORJSOFA6k647t2qvUob2OpnEORA2EZY1jce7kv_bgu4GQk_anT0Xxg8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
🇪🇸
ژوزه‌مورینیو: کسب سه امتیاز اهمیت زیادی داشت و صحبتی بیشتر از این وجود ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/106641" target="_blank">📅 01:17 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106640">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pl9Leew-JKIVBmWn89Yr6v1fJ0G8BwBA1x7LnTAM4OU9q0jr857oKeXYH3SNmiA_lxoDh-uQiseoQvJTzV2cvTSFvDUnxd-N43xpXxkSDjQo2nYl8JjBiCvkOWZ2d7bVpCDmdaV-X_QFWrQncOTq6aNEeR8d0AU_rnkw8sv6nHcteCZggMxjl0VnrL_ZrvLoO_Bc75us67SctSl3RTh-bPK_h_Ptqy7u5LyDPf9oAp4YUM7ndY4TTjNHEFxFEfh75QvEQvfOFEXq50BedjGzD7WQnFhLRoOUNkBSbDcG75U2OQbnUxNPMfdDxTji--gxTIv6yYBsjiX-dhwfb2Q9fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه اسپی یکی دوتا بازی گل نزنه، شعار حیا کن رها کن تو سانتیاگو شنیده میشه
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/106640" target="_blank">📅 01:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106639">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0d40ec75d7.mp4?token=tvChMYiGIpPfXAo_8-91Lf5k1PDQhRWeVKC6jP4QJZ13Qckv5vEI03h1oEhIrj-wSpzWwDQTSus-KPLh2S0l2_nIsAO4PBvCkdkDt6tT3o04bATarHe-iI2uK9VFlmJOJm6eI8UsRPcDT8sIj-MmM3ssvpLzH8r9nHHCsdrgVpZk472qYyp4KtK-LnfyeliQSG0gyT_N5SPwHyfqkmtSRF2jlQZ2OpXZPKggsxM1W3ag0xUkDuUueq7z5H_4E7YOtUSGDls9dFpGLI97LgxoylUk3zp-VteiNNbKF3b7sLXlZ4gbmg0wE90env0mrchH8DRc4pq6RTNbL1ybFQrRFoiUN8cTnrX9y_NmsB78YmNlcEx22AfX_8JwYCnb4KhKcWUOFuUKW-fcSN3c3IemD5_jzArpQsb-TvSG61c5M5ljDybOS9wHtvEP6B-arSiU6dthuTpR7m152er7YQAm_aHvqRIfKLG4l59WMMVtWCKsXuXQN8Y5x96HI9vn2CcwyIgbpqPj-CfhQr5Up_105Tmazn6u36w5O5eCECrYpqcJDl4pnOUGnoO42qcr8G9qojRiTWSsOcB3d2EqZ0wzPXTXNNur7-BMunrVqYZZLxVzV-8xnIy-lKw5iH5kgL77uNV26zjlvq3sKTJG15OIPBrmz0oCrrXwTjM-G0ZNenQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0d40ec75d7.mp4?token=tvChMYiGIpPfXAo_8-91Lf5k1PDQhRWeVKC6jP4QJZ13Qckv5vEI03h1oEhIrj-wSpzWwDQTSus-KPLh2S0l2_nIsAO4PBvCkdkDt6tT3o04bATarHe-iI2uK9VFlmJOJm6eI8UsRPcDT8sIj-MmM3ssvpLzH8r9nHHCsdrgVpZk472qYyp4KtK-LnfyeliQSG0gyT_N5SPwHyfqkmtSRF2jlQZ2OpXZPKggsxM1W3ag0xUkDuUueq7z5H_4E7YOtUSGDls9dFpGLI97LgxoylUk3zp-VteiNNbKF3b7sLXlZ4gbmg0wE90env0mrchH8DRc4pq6RTNbL1ybFQrRFoiUN8cTnrX9y_NmsB78YmNlcEx22AfX_8JwYCnb4KhKcWUOFuUKW-fcSN3c3IemD5_jzArpQsb-TvSG61c5M5ljDybOS9wHtvEP6B-arSiU6dthuTpR7m152er7YQAm_aHvqRIfKLG4l59WMMVtWCKsXuXQN8Y5x96HI9vn2CcwyIgbpqPj-CfhQr5Up_105Tmazn6u36w5O5eCECrYpqcJDl4pnOUGnoO42qcr8G9qojRiTWSsOcB3d2EqZ0wzPXTXNNur7-BMunrVqYZZLxVzV-8xnIy-lKw5iH5kgL77uNV26zjlvq3sKTJG15OIPBrmz0oCrrXwTjM-G0ZNenQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
کارلووووووووس اسپیییییییییییییی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/106639" target="_blank">📅 00:55 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106638">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">وینیسیوس بیاد برا اسپی چند دست میل کنه</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/106638" target="_blank">📅 00:53 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106637">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">عجب بازیکنیههههههه
😂
😂
😂
😳</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/106637" target="_blank">📅 00:53 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106636">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">کوووووون رئال‌ نجات دادددد
😂
😂
😂
🔥</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/106636" target="_blank">📅 00:53 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106635">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">اسپیییییییییییی</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/106635" target="_blank">📅 00:53 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106634">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">گلگگلغاگاگا</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/106634" target="_blank">📅 00:53 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106633">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/90c95a451e.mp4?token=sAjS8tFVVvHwBAQ_j5d340uffUZccp3zB-YCR7SHdxIlSAKajOSpxCj7r7dBY5yvhrkJq2wVibBW96cQFGS41BkixbCf_9meLtuhR55ZwOCaP_I0veIh3GOAULKAbVnndZNZmDNJmDATSNoU9pXg_aG-bEV7OQZ04LE67lAph-PA2FOBnIR8NzKj8jqLw91Y_CngcplKK53UnwwS3W_wo3e4vKd-a705-8FHGZ4u7W7HAqD9H2ykS5FAvkfAA_wUaPR_PwTwW1SJAAY1GsSQ4X-dHHtdqPXIG8OvGVnceY2EGW_2jhuN4lQ0BJ1mM0OMPnaS6-gUn4hCS3qIQyORnWtsbS4GBHoXatkHUbgec62frcaRYAmHHjgocYED0CR0vftiEYfoIIwOyAuaC98hT819KFM2RpmWHQaU2_WeiHfv3Aan7J5HcD2zupO0_siDsUBzzYIzSa4kBPUErp_75gGM8ZGSJ4t4saIYFGRcxeQTsXf_k-6msW--9mwuGjDmO2mXHa631D2xgCUlgnX2oUkkSoaqgf3qrnKl--uX6TTSIlkDPSAKjgKiM-z0T2vc2VPuUVvJbUsj9RCpCC7lhCWULAqlkf7MyD9jdoqpg5-KIntHnWqlQ9fwnJmlEEmiyumZHZPECBH2bXa4cmEuqoNYSro09g2vweI7NR-Z5bM" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/90c95a451e.mp4?token=sAjS8tFVVvHwBAQ_j5d340uffUZccp3zB-YCR7SHdxIlSAKajOSpxCj7r7dBY5yvhrkJq2wVibBW96cQFGS41BkixbCf_9meLtuhR55ZwOCaP_I0veIh3GOAULKAbVnndZNZmDNJmDATSNoU9pXg_aG-bEV7OQZ04LE67lAph-PA2FOBnIR8NzKj8jqLw91Y_CngcplKK53UnwwS3W_wo3e4vKd-a705-8FHGZ4u7W7HAqD9H2ykS5FAvkfAA_wUaPR_PwTwW1SJAAY1GsSQ4X-dHHtdqPXIG8OvGVnceY2EGW_2jhuN4lQ0BJ1mM0OMPnaS6-gUn4hCS3qIQyORnWtsbS4GBHoXatkHUbgec62frcaRYAmHHjgocYED0CR0vftiEYfoIIwOyAuaC98hT819KFM2RpmWHQaU2_WeiHfv3Aan7J5HcD2zupO0_siDsUBzzYIzSa4kBPUErp_75gGM8ZGSJ4t4saIYFGRcxeQTsXf_k-6msW--9mwuGjDmO2mXHa631D2xgCUlgnX2oUkkSoaqgf3qrnKl--uX6TTSIlkDPSAKjgKiM-z0T2vc2VPuUVvJbUsj9RCpCC7lhCWULAqlkf7MyD9jdoqpg5-KIntHnWqlQ9fwnJmlEEmiyumZHZPECBH2bXa4cmEuqoNYSro09g2vweI7NR-Z5bM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌تساوی الچه قعرجدولی به رئال‌مادرید
😳
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/106633" target="_blank">📅 00:49 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106632">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">اندریک بدبخت بالاخره اومد زمین</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/106632" target="_blank">📅 00:48 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106631">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">اسپی رو آوردن زمین گل بزنه
😂
😳</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/106631" target="_blank">📅 00:46 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106630">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">دفاع رئال جلو حمله بارسلونا رسما خاله میشه</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/106630" target="_blank">📅 00:46 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106629">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">مورینیو ریدههههههههههه
😳
😳
😳
😐</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/106629" target="_blank">📅 00:45 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106628">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">الچه قعر جدولی مساویو زددددددد
😳
😳
😳
😳</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/106628" target="_blank">📅 00:45 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106627">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">گللگگلگلگلگلگلگلگلگاگلگ</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/106627" target="_blank">📅 00:44 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106626">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6efefc36b3.mp4?token=AGMtYZy2szwMJi2rhptXbqitdSKK4mp8EFXYN2jMe69rg1_VEPLTVgMgFYQ3rWwtdFoHXKGLJywygSY_jzeB_UGMdZTp4RndIJ9Al9nHNb7QTHpmRnbtFIuziwpJKOL4Yu_ckmmBF2t0YvDC7UEf3k3ZjUya1_ORCG3FFFgDpOoZYi4wNw1QfIAZeBA6ft24goaCGyLiAbW2OyoxIbUBydxCnjYmFuJj8gXOivLvNvmLlKoQxJmRr7lyIGHt-Eoh0dldhsxroRVWdQdlVX0-I6oxj9IRqtgyiJbY8hPVMiseyXBM2A87g6gjbTz6iM4CX8gm2FoCjljzO3af6fiBYTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6efefc36b3.mp4?token=AGMtYZy2szwMJi2rhptXbqitdSKK4mp8EFXYN2jMe69rg1_VEPLTVgMgFYQ3rWwtdFoHXKGLJywygSY_jzeB_UGMdZTp4RndIJ9Al9nHNb7QTHpmRnbtFIuziwpJKOL4Yu_ckmmBF2t0YvDC7UEf3k3ZjUya1_ORCG3FFFgDpOoZYi4wNw1QfIAZeBA6ft24goaCGyLiAbW2OyoxIbUBydxCnjYmFuJj8gXOivLvNvmLlKoQxJmRr7lyIGHt-Eoh0dldhsxroRVWdQdlVX0-I6oxj9IRqtgyiJbY8hPVMiseyXBM2A87g6gjbTz6iM4CX8gm2FoCjljzO3af6fiBYTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
گل‌اول الچه به رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/106626" target="_blank">📅 00:37 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106625">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">الچه زدددددددد یکی</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/106625" target="_blank">📅 00:33 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106624">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">گلگلگلگگلگلگلگلگلگلگل</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/106624" target="_blank">📅 00:33 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106623">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01890ef1a2.mp4?token=f1gfZEkJvVCVGPcL0rtsM8jrhxMi-bA1cjm-mH7F3jt0K1TeSDvcPOF9NuoEvNv1XPq17I__7khCrCpgf6af5gGBOieiIXv0h9v4b5RiVKJMwozrU5-bP1mrpHDfnXwMWPtyl01229Hyp6jkS5Bfma7fsIgz5rdtDM7BMTEa1-zux7gGT0TsBr1NQXaGNdIUHff0z2zCDBmszzlIkrWd5SoekpDNsvffkFZGbovCDzGMvlRKSAPMDbJktVzs4iDPsL19CSOXExyBTPR1pwD31ArVQ2qIH9gxQZtpf3CYDrq5M9GpUiZMdep428czJrjMt61mftRHkO8OLtvwkXtklw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01890ef1a2.mp4?token=f1gfZEkJvVCVGPcL0rtsM8jrhxMi-bA1cjm-mH7F3jt0K1TeSDvcPOF9NuoEvNv1XPq17I__7khCrCpgf6af5gGBOieiIXv0h9v4b5RiVKJMwozrU5-bP1mrpHDfnXwMWPtyl01229Hyp6jkS5Bfma7fsIgz5rdtDM7BMTEa1-zux7gGT0TsBr1NQXaGNdIUHff0z2zCDBmszzlIkrWd5SoekpDNsvffkFZGbovCDzGMvlRKSAPMDbJktVzs4iDPsL19CSOXExyBTPR1pwD31ArVQ2qIH9gxQZtpf3CYDrq5M9GpUiZMdep428czJrjMt61mftRHkO8OLtvwkXtklw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
سوپر موشک تاماهاوک سوبوسلای جلو تاتنهام
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/106623" target="_blank">📅 00:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106622">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">سوبوسلای چه سوپرگلی زدددددددددد
🔥</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/106622" target="_blank">📅 00:20 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106621">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">پشماممممممممم</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/106621" target="_blank">📅 00:20 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106620">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CCAIBv5x2AVeTFwvmvM7GjJqi_jPnugs5XS0EnlluGsKXrM8vVOgkdsRQdJveGz7DUJbiSJicctUjioJSqjR7ieUqd2aoYbixMG7Aw2A6Vu7a6O_fmboUIAtjxDCtRElZEqNR2mRR70lLkCBmLMEg-0lt0XzjbqDQ3XsU-9OCw1XI2-4VKN8Cv_-t9svJ8Ty6TdP6xvzcnUgB2ZwxTvjTFOUshfp7OxkL_s8IKKL5g2Hfk5N5dfKuhU_dVZwSHnoIf0ajXIMwQGfHhep1co80mHgicuchIjgG1ObiTMb-sQbNwlO9IS4b19bvPysyUQR5jHpBDxnXh38V8QIQvHlNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
لیست تیم‌ملی آرژانتین برای فیفادی با حضور لیونل‌مسی؛ بازی مقابل بنین مراسم ویژه فدراسیون فوتبال این کشور برای خداحافظی اسطوره تاریخ فوتبال برگزار خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/106620" target="_blank">📅 23:58 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106619">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/drVnztR0ebwXRgKEyYiB3VRWzLuDc30PS9ZoF53_sFlT34EzOG1JHVknfcVsgTU7z7lnOukY3Dg2wPWy-UOOAnpXzsMUXonyOBW5l52dxxkgvwnp44IslzDBhYO-8db54PK82QR5gg0uGAW0s_cXpXJypR6MistloVa61enpjPZnzIKUXPjmuS9TnTYia9lMbdWRD3-KKqlvUnTRbpvHuZSm_1tEzfLPc84aHGMQaAEFUC7onv8d9Q-nK1_uhqa2ZLVfkBcGhYr30EMoPxpJhrSlqckIC1JD2zJxLbbItZkycOkSHHfO9I07TK4LsaUSR-jKRTMdVnpIGq30gDpSSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟣
جدول لیگ‌نخبگان آسیا در منطقه غرب پس از پایان هفته‌اول و حضور استقلال در رده دوم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/106619" target="_blank">📅 23:41 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106618">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/01ef226cc4.mp4?token=jAPlrjapM5Uh0VPH8b-d7VEL4ULF2rrXtdJe6-dL3mEwZ5l1IDr3ASrS7fztWtVv-nnnxejrVvwIuDQ7nycDtsZtJaKl6kHxq-vA1vC_HeC_xP8NzTmdsx7DdWjFyZmeeP3ichdiA5pRpI1Mt52xttgQCtcRSivWeqcSeUinT2kgg7UNh_OJa251epiZ5lwJuPZwLxL4Gg34NL9yaPa4zQOMnBTmSKaaCueh2-GaaGQhdmN-TEeVMCAQYOY2CaqSuQZrGNygZ1Ki2SC0APVatHD7PhwMhcOvxg9seIK89mWNT2ez29Nmunz2rRGJZF3X55PywW44ltN1Ydw8XlkHYiXT5hnuqRAPWGLPkP5MN7c19tDh0tGndbOHAzQ97SQugUq-SBb6VxBQYYpfp_j-vA7aRh-vVqgZp_Zyejmh_zxZEtpeD7Fh9ipRkKdAA77oW0qoPNweeui_O1hi0h7xRV3mI0RyN0oLmUiSdvXrtcSmBViEvbivqgzzFu03EvRObIIWqyCyQy0F2v2X4OseUCv7Fopm0RK7-WVW5vP1VBolLi9rgP5-8OVSE-OmowCv5ecOBWVHY-9BfhsZFCN63nl7eQudvldN_5lxE0S4aP-RNKfPtzDwDujm3XWoFf-Gi0IsKn8E0ggq2BN9Xz8KRAI6esL_G2LAiA5QPINUstQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/01ef226cc4.mp4?token=jAPlrjapM5Uh0VPH8b-d7VEL4ULF2rrXtdJe6-dL3mEwZ5l1IDr3ASrS7fztWtVv-nnnxejrVvwIuDQ7nycDtsZtJaKl6kHxq-vA1vC_HeC_xP8NzTmdsx7DdWjFyZmeeP3ichdiA5pRpI1Mt52xttgQCtcRSivWeqcSeUinT2kgg7UNh_OJa251epiZ5lwJuPZwLxL4Gg34NL9yaPa4zQOMnBTmSKaaCueh2-GaaGQhdmN-TEeVMCAQYOY2CaqSuQZrGNygZ1Ki2SC0APVatHD7PhwMhcOvxg9seIK89mWNT2ez29Nmunz2rRGJZF3X55PywW44ltN1Ydw8XlkHYiXT5hnuqRAPWGLPkP5MN7c19tDh0tGndbOHAzQ97SQugUq-SBb6VxBQYYpfp_j-vA7aRh-vVqgZp_Zyejmh_zxZEtpeD7Fh9ipRkKdAA77oW0qoPNweeui_O1hi0h7xRV3mI0RyN0oLmUiSdvXrtcSmBViEvbivqgzzFu03EvRObIIWqyCyQy0F2v2X4OseUCv7Fopm0RK7-WVW5vP1VBolLi9rgP5-8OVSE-OmowCv5ecOBWVHY-9BfhsZFCN63nl7eQudvldN_5lxE0S4aP-RNKfPtzDwDujm3XWoFf-Gi0IsKn8E0ggq2BN9Xz8KRAI6esL_G2LAiA5QPINUstQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل‌دوم رئال‌مادرید توسط کیلیان امباپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/106618" target="_blank">📅 23:40 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106617">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">دیومانده بالاخره پاس گل داد
😂
🔥</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/106617" target="_blank">📅 23:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106616">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">امباپه زدددددددددد</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/106616" target="_blank">📅 23:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106615">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">گلگگلگلگلگلگللگلگلگ</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/106615" target="_blank">📅 23:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106614">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/96af48f644.mp4?token=fY7qZHXrGmGRbqYIy9Px9eGPz1h1yFTbWzo_tuYZYBHuFrzJEStXr3QulZS534BUqtPAjlD2Ghm1_G7cTEO0xACYGdaiXaTLGUtsCvetMpBTfjpzkWI6R0ruOJIe28S0_cB781hnk0J13rXvV2bxcJH5hwLCqIm4DrZ2iYa-6ZaDO3P6XrF44lIf7no88Uuvg9TFX_bKdgSo_1v3oZBts1fwm9ck1hXI2gaHCLyGLkcYe14SrRjVAdNVnzKftWWi9JyOnvxwKQXztnmSa1Yc4E93dNOZjf3UfTkWlBAfnq-McrziwpML2SXWpB0gteiTbtRy1nFNuusIloE0ogaugjXeOWVk3OqbSWLtnp2G8OiZidSyq0l1vxW-SoXWZt24M3Qy9nmFl52JU95AIMFOqIHmBSXywOt8ySP1rA5OtDEEMUCnLo8xnu72ju1skT04gy9nFQBAT4alzZEOQYqX1q5W4FB-KGo7_jfLOSL2A8lnVKb8Rf_CaBQcmkJF9EHpoLK9xU7hD4mpuC-N26h6Aoo6opi4A2BCtYSRFnCTreZID5SEWYWZvGM7PhcaUxluJkjuwbkHCYvBeWLQUBssvrE_AK-qqZAw9dgWq7YA5ofX5k6dB5F1MpAsU6vYBIif1FFicw2V8tJm9XNsGDeD4qWOyDNweZ2Xtyhpgu8EO3o" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/96af48f644.mp4?token=fY7qZHXrGmGRbqYIy9Px9eGPz1h1yFTbWzo_tuYZYBHuFrzJEStXr3QulZS534BUqtPAjlD2Ghm1_G7cTEO0xACYGdaiXaTLGUtsCvetMpBTfjpzkWI6R0ruOJIe28S0_cB781hnk0J13rXvV2bxcJH5hwLCqIm4DrZ2iYa-6ZaDO3P6XrF44lIf7no88Uuvg9TFX_bKdgSo_1v3oZBts1fwm9ck1hXI2gaHCLyGLkcYe14SrRjVAdNVnzKftWWi9JyOnvxwKQXztnmSa1Yc4E93dNOZjf3UfTkWlBAfnq-McrziwpML2SXWpB0gteiTbtRy1nFNuusIloE0ogaugjXeOWVk3OqbSWLtnp2G8OiZidSyq0l1vxW-SoXWZt24M3Qy9nmFl52JU95AIMFOqIHmBSXywOt8ySP1rA5OtDEEMUCnLo8xnu72ju1skT04gy9nFQBAT4alzZEOQYqX1q5W4FB-KGo7_jfLOSL2A8lnVKb8Rf_CaBQcmkJF9EHpoLK9xU7hD4mpuC-N26h6Aoo6opi4A2BCtYSRFnCTreZID5SEWYWZvGM7PhcaUxluJkjuwbkHCYvBeWLQUBssvrE_AK-qqZAw9dgWq7YA5ofX5k6dB5F1MpAsU6vYBIif1FFicw2V8tJm9XNsGDeD4qWOyDNweZ2Xtyhpgu8EO3o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل‌اول رئال‌مادرید به الچه با گل‌بخودی گلر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/106614" target="_blank">📅 23:31 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106613">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aVraLHIpr0ReAS6Qm8bx2XrZXtPEkYB08D0Op14BBOW8x5v-_LwEH-VxlMFq_khBkGZrb5BiINhqmAR6YfkEzYgrbiW-1tr62CnkTkexfsVascO5OYGJQoEzwqJx9nSABZL613T8R4Uxxv7eQbfS6-qcncEQs8NncPd_AAgyg6C5Slr-sQtytbcT0xv9MvuNTpVyOoZSEHRrTLRN45w5mQTpbYhJSJV6bFbNOJMTqmgqfTs0ZG38fNfPXtpMyRol8PchPcu_n6uoNIT1ZdfgFKHBXBmUa5FSv7oCsgaDu42dGVrXeD7jA4oIw7YwqiezeSjemomNgkahUxsa5yRgTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوووووووف
🔥
🔥
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/106613" target="_blank">📅 23:30 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106612">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">عجب سوپرگلی زدددددددد
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/106612" target="_blank">📅 23:28 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106611">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">آردا گولررررررر زددددددد برای رئال
🔥
🔥</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/106611" target="_blank">📅 23:27 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106610">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">گلگلگلگگلگلگگلگلگلگغگ</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/106610" target="_blank">📅 23:27 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106609">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb9c936306.mp4?token=sSwUwe-GPENDrE_cTrnG7X5T5kXHFRtUKRmDW8jo8YZvwBTUMO2gxbuKM0AYE9pqCQtsXtcDlqat9iCmc4GYTSiQprragP5sNkCmMIeMf_tT_47nu5LZLDaAqysOgG9Q7GkkugTJyBUCfxwrg2elSvuGJL_Ho7hotUUpx4Cg003vb46yVt8KW7X7jALlbSYGvipT1dRITOMe9jCJ8vyqmOIr13cQrcmMFobGRbCDO_usdwtOQb4pz94g5fo2YhXfd6YLzkRGpCuLSmzBedzio_6VVgGQHp4TbvYDHLsRkNsS23P5K9y8fSBhdjclJZORCZIGMyg6onm_9H1nwl1XkYKoX4fNN_XuRDKM0SaMzNwn-guQrQE0kjAuRunH4sMMD5YDSqrFIIA6BQQFY5Y-vNpODexks3xS1HSVgMHtTw_q0xBtqzKGVgWnQfIFPULvlJPkY3NKToeKQiSQHEqF83dkq7aL-g7cIrHaLTLLzMC4X9hN-H1ICB-qFGc0MS-aW5nNyYbNROMrdhVkK2ExjaSSVpVG4jdzIRAGVBeQDsNFhOQt-EUOCPhBFqNzSVH5kLdzf1Mbux_tdi9lQp_JTFk08Gjtf2AFTioSyQNaVrhGr26_doy9jp8HjCTfnbpBTrecvzO1G7tKL4hcQHwrJ17PbMhSX1-8h-wK29wTad0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb9c936306.mp4?token=sSwUwe-GPENDrE_cTrnG7X5T5kXHFRtUKRmDW8jo8YZvwBTUMO2gxbuKM0AYE9pqCQtsXtcDlqat9iCmc4GYTSiQprragP5sNkCmMIeMf_tT_47nu5LZLDaAqysOgG9Q7GkkugTJyBUCfxwrg2elSvuGJL_Ho7hotUUpx4Cg003vb46yVt8KW7X7jALlbSYGvipT1dRITOMe9jCJ8vyqmOIr13cQrcmMFobGRbCDO_usdwtOQb4pz94g5fo2YhXfd6YLzkRGpCuLSmzBedzio_6VVgGQHp4TbvYDHLsRkNsS23P5K9y8fSBhdjclJZORCZIGMyg6onm_9H1nwl1XkYKoX4fNN_XuRDKM0SaMzNwn-guQrQE0kjAuRunH4sMMD5YDSqrFIIA6BQQFY5Y-vNpODexks3xS1HSVgMHtTw_q0xBtqzKGVgWnQfIFPULvlJPkY3NKToeKQiSQHEqF83dkq7aL-g7cIrHaLTLLzMC4X9hN-H1ICB-qFGc0MS-aW5nNyYbNROMrdhVkK2ExjaSSVpVG4jdzIRAGVBeQDsNFhOQt-EUOCPhBFqNzSVH5kLdzf1Mbux_tdi9lQp_JTFk08Gjtf2AFTioSyQNaVrhGr26_doy9jp8HjCTfnbpBTrecvzO1G7tKL4hcQHwrJ17PbMhSX1-8h-wK29wTad0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
صحبت‌های عادل فردوسی‌پور درباره اسامی عجیبی که بازیکنان استقلال در پشت پیراهنشان در بازی دیشب نوشته بودند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/106609" target="_blank">📅 23:25 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106608">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/001b323a9f.mp4?token=GIfg3Bu3eVCZe-9pXA6Fda7BE1jzrdaj-3y7sqyNUh6ThsvjDZ00bQnEqE3ZOuNRYfXqQy4lGBWjvB4rNEThCuXXnV2Zc4-DWQldyI0s7Kt7I4GBawZMqxbIJBPp1f6mofB1oJssponKRUHUpbcy9fFfElgvWq1Jk6w4_m83xmLMbYxXwMbPhMBOMErnD0JrdD-2pWJBixViKtadWhW5oKWEo-TSpetSgpcfLHLoOXwFo0m3K7d0jjI-YMvWk940BMYBhkqrRyvctyXtdOpfShAuTmnpEQtXLnatdTjQ-YcKETz4B9Q3wWW5NPcHZpBp6TYIEbe9NubE1gLNlqWQmYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/001b323a9f.mp4?token=GIfg3Bu3eVCZe-9pXA6Fda7BE1jzrdaj-3y7sqyNUh6ThsvjDZ00bQnEqE3ZOuNRYfXqQy4lGBWjvB4rNEThCuXXnV2Zc4-DWQldyI0s7Kt7I4GBawZMqxbIJBPp1f6mofB1oJssponKRUHUpbcy9fFfElgvWq1Jk6w4_m83xmLMbYxXwMbPhMBOMErnD0JrdD-2pWJBixViKtadWhW5oKWEo-TSpetSgpcfLHLoOXwFo0m3K7d0jjI-YMvWk940BMYBhkqrRyvctyXtdOpfShAuTmnpEQtXLnatdTjQ-YcKETz4B9Q3wWW5NPcHZpBp6TYIEbe9NubE1gLNlqWQmYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
گل‌دوم الهلال عربستان توسط ساویچ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/106608" target="_blank">📅 23:22 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106607">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">یه گروه همفکری بت زدیم مخصوص دوستان بت باز
😂
✅
https://t.me/+6XLorNFkXGgzNmE0</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/106607" target="_blank">📅 23:22 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106606">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">یه گروه همفکری بت زدیم مخصوص دوستان بت باز
😂
✅
https://t.me/+6XLorNFkXGgzNmE0</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/106606" target="_blank">📅 23:22 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106605">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e75776b642.mp4?token=mtRRL1zEwqSruwTP3aES7y-gwF1JERXZDrIEywrz3Q-kOcPWGQTiIQBz_S_X8BNK8unKDpcE51ZrL9oQb184ePbAlCkIUndkRQqOKXU80dblkBcd81jpkZx-7bbU16_8NmeGl3hLCQCsLahiGAmtFFqozS1zzHr-CmYkn7uR8ot49UO6IvIZBlKxHkNlSBE6vbngZ8IMMMUUTigln-vtpqE_QGXplpNCXHyQTZ-DOCC3_TxfhAU1ifTCKlCGrsI_bnKvmNxskiuiOBJTvHkA7xu5Npz0Dt2bJWmAn8pn8EpP4f0b004gyoDyPpoRm9UlySf4YbBM0zDbwcVuJ_3Cfw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e75776b642.mp4?token=mtRRL1zEwqSruwTP3aES7y-gwF1JERXZDrIEywrz3Q-kOcPWGQTiIQBz_S_X8BNK8unKDpcE51ZrL9oQb184ePbAlCkIUndkRQqOKXU80dblkBcd81jpkZx-7bbU16_8NmeGl3hLCQCsLahiGAmtFFqozS1zzHr-CmYkn7uR8ot49UO6IvIZBlKxHkNlSBE6vbngZ8IMMMUUTigln-vtpqE_QGXplpNCXHyQTZ-DOCC3_TxfhAU1ifTCKlCGrsI_bnKvmNxskiuiOBJTvHkA7xu5Npz0Dt2bJWmAn8pn8EpP4f0b004gyoDyPpoRm9UlySf4YbBM0zDbwcVuJ_3Cfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
گل‌اول الهلال به الغرافه توسط روبن نوس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/106605" target="_blank">📅 22:52 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106604">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🟥
🇶🇦
اسماعیل‌بن‌ناصر هافبک الغرافه بدلیل دریافت کارت قرمز دیدار با استقلال را از دست داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/106604" target="_blank">📅 22:19 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106603">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jxL2Dzu5TvxkAbw55V-huuCQ04oQHo88LB6UVd5KEn7R0PntljQ_nONMpLPaNB6f-ZnAmNJX3bxOifNvWZAyqnCQcKdgNrek4_0gEHqlf9ShKWxKCi3oBgI-4JUuVNlMdXhUZP0XyEHEV6SnWqV8c9j8jW-R4kfGomE7eseIura1SbylRnM678jGEpioTSDZnglnIDdA9m4CDJQNcFbzVNKmL2xzZrGYYg3BdGSkITHn4yBx2bzKn-Ap1Jc9VqJ3RFXENmukA3lkUD5mcA9ARGU7wMjcYJgDjTo1567vHZMLAc0l1cpk9mn7ym0Mv_ZDnMsq8gvS-TNSyHNgLIZJiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🇪🇸
ترکیب رئال‌مادرید مقابل الچه؛ ساعت ۲۳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/106603" target="_blank">📅 21:47 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106602">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">‼️
🇸🇦
عصبانیت
رونالدو از مدافعان النصر!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/106602" target="_blank">📅 21:28 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106601">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d5839d9f6.mp4?token=U7qg4VRhAFSt__gEGlgVsibQlonfS1zHhGpvOvvF4FBxZQmNtiF82672i3lHPPhmepLKVtke8g0Hie4oG-TbfZmJ5Dx7ukhBaHVSGEjQ9W7xT-MPSPMs3HyDG5WfbOnblLG_DshQ0pv0006xLfXiPgicRju4mTJ_jsHe66RpDEIkm3h2fsddh5KviXhWzfPQmif9FXEecjktQ3iBWcE2aQodhoCGzx7terQ5NvOvID8N50h8_7WoKJF0zXE2_F11kMClYCF0dF0c-_aBA6Llb3K5TiJ_woILPtOCq9PWmOORnzqup7yiCSY-ySTFm0Pi44KcSZa2N2tawroTP1sw8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d5839d9f6.mp4?token=U7qg4VRhAFSt__gEGlgVsibQlonfS1zHhGpvOvvF4FBxZQmNtiF82672i3lHPPhmepLKVtke8g0Hie4oG-TbfZmJ5Dx7ukhBaHVSGEjQ9W7xT-MPSPMs3HyDG5WfbOnblLG_DshQ0pv0006xLfXiPgicRju4mTJ_jsHe66RpDEIkm3h2fsddh5KviXhWzfPQmif9FXEecjktQ3iBWcE2aQodhoCGzx7terQ5NvOvID8N50h8_7WoKJF0zXE2_F11kMClYCF0dF0c-_aBA6Llb3K5TiJ_woILPtOCq9PWmOORnzqup7yiCSY-ySTFm0Pi44KcSZa2N2tawroTP1sw8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇦🇪
گل‌چهارم العین به النصر عربستان!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/106601" target="_blank">📅 21:24 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106600">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vvGnF-ouDd4PvcHsLjB_xsNCyOWZWBoRcA53dGvYtascjkMOeME3au4dins8eJmvFi0wFGoRQFU8nbotD_GTaTd3x9CnwO3o-Nxw4urLOQxbShZLe45f9LLvaEI1YonfJifAaMF75OoVxHKNazagVgOP4YlGlRPTOn9YZtoVcZ4T_JelE3pSCmiKTgOtMvjHebyZMGdNR8gEMabaP-Le7P7iXh_TmHDXwITGExS2vRptnPMo--nh2Sv2P_WBGWi1Rew1Ex15b20CVmVHqA4RGsUw_s4PYn2QnYuCX6jl2w2Oj4mC1RrXkmeo-8i0p0jIS19SjEA4mfbM3tof3EZHkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇪
گل‌سوم العین به النصر توسط سوفیان‌رحیمی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/106600" target="_blank">📅 21:13 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106599">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2424b5a6f9.mp4?token=f3eMK4-UjtRUKVBKqDLLGH-go-1RGBCAJ2ZerEtvTMA5MYSC4GcN0jee8ksH5iVm9iIFAnqn4DtlYjgbX_4lpd0N5yDr_DvcNX0reiSNV1E6kJ9E8rOPtlfwW-YXOZqKpeg8PCwXXM26a7LLXFT9TPC2F0vLsc_2ufUcc1-efs4rblf-t-1caSvuzoIyQInSUioPAJJHLF2y8QvRud5d1MSdtqNFmkS9Us3SBh4dtCvU2tbcovf1POwrQ8Dtcbx24ZHAMkLIE7gGOWrKvdOU2PDmAwGmLltJFpP_mYc5fJSQFu5NQXH-N75MiWUi-_t51BE3-L6Aa2hVCc0PJNNt8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2424b5a6f9.mp4?token=f3eMK4-UjtRUKVBKqDLLGH-go-1RGBCAJ2ZerEtvTMA5MYSC4GcN0jee8ksH5iVm9iIFAnqn4DtlYjgbX_4lpd0N5yDr_DvcNX0reiSNV1E6kJ9E8rOPtlfwW-YXOZqKpeg8PCwXXM26a7LLXFT9TPC2F0vLsc_2ufUcc1-efs4rblf-t-1caSvuzoIyQInSUioPAJJHLF2y8QvRud5d1MSdtqNFmkS9Us3SBh4dtCvU2tbcovf1POwrQ8Dtcbx24ZHAMkLIE7gGOWrKvdOU2PDmAwGmLltJFpP_mYc5fJSQFu5NQXH-N75MiWUi-_t51BE3-L6Aa2hVCc0PJNNt8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇪
گل‌سوم العین به النصر توسط سوفیان‌رحیمی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/106599" target="_blank">📅 21:11 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106598">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">گلگلگگلگلگلگل سوم العین به النصر</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/106598" target="_blank">📅 21:08 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106597">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d9f6b6fba.mp4?token=dbadIF7PydG3KKpFKvPDCTee353IdfkfR4z_qf8sk5X3Q--R0sFCxY2tL-G3yHI84z8yw4-_wuMBKV6mttEvmBi8m0K1qry3zcG_v1z-RPH4-7dyUAwbxmPUuJGsqGjr0d5QgX3FX_S0HV_cn4IXrCZ_Fjd5y4_WeCTk9JpZbYVworIjxxMBMPRgb8lTQV-Jn-HtietJ6KPZYaH-CHsLizmTS_ti1QJ2KD3lKhjyoTUfY-oXuu2c7RZoiNrcnU8tF1gwCF6KlOeSI8_Q71dsXJTiViFmtT77qRCy4HgSjzPRIawTRyZSU6vH7gV3g9laCXwyDKd6roLgktyfRanWQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d9f6b6fba.mp4?token=dbadIF7PydG3KKpFKvPDCTee353IdfkfR4z_qf8sk5X3Q--R0sFCxY2tL-G3yHI84z8yw4-_wuMBKV6mttEvmBi8m0K1qry3zcG_v1z-RPH4-7dyUAwbxmPUuJGsqGjr0d5QgX3FX_S0HV_cn4IXrCZ_Fjd5y4_WeCTk9JpZbYVworIjxxMBMPRgb8lTQV-Jn-HtietJ6KPZYaH-CHsLizmTS_ti1QJ2KD3lKhjyoTUfY-oXuu2c7RZoiNrcnU8tF1gwCF6KlOeSI8_Q71dsXJTiViFmtT77qRCy4HgSjzPRIawTRyZSU6vH7gV3g9laCXwyDKd6roLgktyfRanWQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گل‌دوم العین به النصر توسط حسین‌رحیمی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/106597" target="_blank">📅 21:03 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106596">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">العین دومیوووووو زدددددد</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/106596" target="_blank">📅 20:58 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106595">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">گلگلگلگللگگلگلگلگ</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/106595" target="_blank">📅 20:58 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106594">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef7815d7dc.mp4?token=WSlflJivzSOEw9vhRWTnrFldeE2V_xTbaE3xS7dejQ48iPOr6FVWgUx9EYudZPBcGtOx59v4rUrOEqvrUpuwJBWghBAGdjUAxpNL1_po-aI3VztZgPQFku_F7a-JHNeU0S5Aq9iWTCMcmCjnA_DGWIGRfekIvd8yWxnChU-q_nOcbKQSYdazLJtAU998xnXpkY5E7kDjsulNPbpz4Zzk7q4cYzBKh2jsyLWKh85vAMjUsf5d3Gt4KaaRLo8u-iMLDsD3WbGtW86K5hwzmrQz2jEwlXO-RMwpTW85Qg4e2Epw7TInrWd6fSr550e1AGLqdrzVWW9xgCR-4zKN3up6iKxlkP5SlbJa3RtSa0mk7TbXE89_dLYlmdCyHJF1fphL9UnvSW1DNmMMa-ba9gNvFVT7TksEpTeiYmOYKOQMlG0YbYohpz_gXJro5XCxuvBHyylTqJU9hPuVcn34NSowmArTGA1q407G9_ZccZDHLNuRK-qAxcUFbic1anX4WnAXe1DkFf1xdEqNNXTr0pqE2zYB8z-t8IQnJ8ccoBTz0d1PBA0Z-loJ9qYUF3W5y0UX9v4fYg8Lf8e5yGmiUtfRbSOiGIa96X80LV9U_Dyo7wiHNjGujR-5ncpRl4Y7QK3iRDVSTzSy_wwe48wnICpU8-0Jf1K1jYq0LW0vkdPpYV8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef7815d7dc.mp4?token=WSlflJivzSOEw9vhRWTnrFldeE2V_xTbaE3xS7dejQ48iPOr6FVWgUx9EYudZPBcGtOx59v4rUrOEqvrUpuwJBWghBAGdjUAxpNL1_po-aI3VztZgPQFku_F7a-JHNeU0S5Aq9iWTCMcmCjnA_DGWIGRfekIvd8yWxnChU-q_nOcbKQSYdazLJtAU998xnXpkY5E7kDjsulNPbpz4Zzk7q4cYzBKh2jsyLWKh85vAMjUsf5d3Gt4KaaRLo8u-iMLDsD3WbGtW86K5hwzmrQz2jEwlXO-RMwpTW85Qg4e2Epw7TInrWd6fSr550e1AGLqdrzVWW9xgCR-4zKN3up6iKxlkP5SlbJa3RtSa0mk7TbXE89_dLYlmdCyHJF1fphL9UnvSW1DNmMMa-ba9gNvFVT7TksEpTeiYmOYKOQMlG0YbYohpz_gXJro5XCxuvBHyylTqJU9hPuVcn34NSowmArTGA1q407G9_ZccZDHLNuRK-qAxcUFbic1anX4WnAXe1DkFf1xdEqNNXTr0pqE2zYB8z-t8IQnJ8ccoBTz0d1PBA0Z-loJ9qYUF3W5y0UX9v4fYg8Lf8e5yGmiUtfRbSOiGIa96X80LV9U_Dyo7wiHNjGujR-5ncpRl4Y7QK3iRDVSTzSy_wwe48wnICpU8-0Jf1K1jYq0LW0vkdPpYV8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
لحظه‌مردود شدن گل السد از جایگاه تماشاگران در بازی دیشب مقابل استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/106594" target="_blank">📅 20:30 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106593">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f5e9475ab6.mp4?token=n_hxWfpTmcl3LyLPYGzLFtDVq_rjbfFnm5oDo0KHcYiDc8bwyXAWCEx_ajbkcq7r_Jt5o6xJYdVxndQM2UR4_PpjzMn6Qso5NQwCUcre9P31QZrioSHyOsp8up53U-Cxrw0Kds7itOjOi2sqKLSfT9_16Lgew1lKEi880KHdERjF7j0CRjfMMUI4AZvhJ-SrwBGKtQct7NAvYoRtZZVKlWCzX8TCRyi3tPWli_BQEtP27YJOmkIobQEuDT5jO8yyjAPkAtp_0hySt28WHi6tpKgA_c5IZYP7N6ksNCj6VaXcW0czchGf4vRuIFWTne-hflfvVCLH0QWnbQuJDCIEQn7_80LeMKldGOTqyoFilztbR9ZfyNHZFKGDzhJ5AG9JfNAsIT-MlU-PE445l5H2ovu2sVb-kxqvT4Q0od-A30NWTFePv9Yimo5YrntNOstYQUzGyE3uWGPqPuy497QVz4p3oT7UunJm2-HDraSIspVNPn3SyBroVauvTOy4TWd_pfAskkqNdo2as-coCi9ndCIANmvHcU-WNUaiJuQ82ohypzxrJrFV2OrgPNf7Aw1epfJAYgTLFigrqzaH_yfEFCyUCt0UhpXj3F2GZHLO7bDfnaQbndgw-_uy5zLZwAqgCIVyU9bxwOCZVtNdaEhHjzdklt0UnmtjLhVCnTM8w5I" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f5e9475ab6.mp4?token=n_hxWfpTmcl3LyLPYGzLFtDVq_rjbfFnm5oDo0KHcYiDc8bwyXAWCEx_ajbkcq7r_Jt5o6xJYdVxndQM2UR4_PpjzMn6Qso5NQwCUcre9P31QZrioSHyOsp8up53U-Cxrw0Kds7itOjOi2sqKLSfT9_16Lgew1lKEi880KHdERjF7j0CRjfMMUI4AZvhJ-SrwBGKtQct7NAvYoRtZZVKlWCzX8TCRyi3tPWli_BQEtP27YJOmkIobQEuDT5jO8yyjAPkAtp_0hySt28WHi6tpKgA_c5IZYP7N6ksNCj6VaXcW0czchGf4vRuIFWTne-hflfvVCLH0QWnbQuJDCIEQn7_80LeMKldGOTqyoFilztbR9ZfyNHZFKGDzhJ5AG9JfNAsIT-MlU-PE445l5H2ovu2sVb-kxqvT4Q0od-A30NWTFePv9Yimo5YrntNOstYQUzGyE3uWGPqPuy497QVz4p3oT7UunJm2-HDraSIspVNPn3SyBroVauvTOy4TWd_pfAskkqNdo2as-coCi9ndCIANmvHcU-WNUaiJuQ82ohypzxrJrFV2OrgPNf7Aw1epfJAYgTLFigrqzaH_yfEFCyUCt0UhpXj3F2GZHLO7bDfnaQbndgw-_uy5zLZwAqgCIVyU9bxwOCZVtNdaEhHjzdklt0UnmtjLhVCnTM8w5I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇪
گل‌اول العین به النصر توسط حسین رحیمی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/106593" target="_blank">📅 20:01 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106592">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">العین دومی رو زد ولی مردود شد
‼️</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/106592" target="_blank">📅 20:01 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106591">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">گلگلگلگلگلگلگل</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/106591" target="_blank">📅 20:01 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106590">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">العین خیلی قویه بیشرف
النصر رو کرده تو قوطی</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/106590" target="_blank">📅 19:58 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106589">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">العین یه گل به النصر زدددددد
💥</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/106589" target="_blank">📅 19:56 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106588">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">گلگلگلگگلگلگلگلگلگا</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/106588" target="_blank">📅 19:55 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106587">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NXeSsIMXg4PzE3hQ8PK0JY4FXZtU-Dzte6dSa_mQ52odgJOR-x5n5CqepxQwMfVJOmFIYffyfCLGVVtA_FnyKCRbJJwYerDlrTsgMdtGEYywH7rfIrN2oJRvSILjp3ajyenuw3nug-jPVnom93P_aB1Gf_txOc_YCjLRRJqFKjj5vCeFQW3fy_j6nFx9x4_cKW-m7w4zORFFX5tyfvPTqqdBnfXWi8MTdR2bOmjWHDXXraYqsBhA_Gx_7QswqJQwpy0Xkvtdag4I0DZol6Q2tgxmJf_l22QnEB8O6j748CtZt7IVjqXSQ_Ce-6M_szgvN453e4QhZs-opXeklulPWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🇮🇷
🔵
گل‌گهر در شروع سطح دوم آسیا مقابل الجزیره امارات به تساوی بدون‌گل دست‌یافت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/106587" target="_blank">📅 19:49 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106586">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8940fb69d5.mp4?token=nmuZprnU1UjvRibC1exrsBBkZKiV-4RvT7_b3nFf1dMPCHrO408kCT90OyZFfTTSVWi9-0zqJvOTM2DOeMF5Os6tspvjzF_pW61immwiV3nzt7m5ewBKiTq7YGFF32REoZvgEJOQBT8I8KBY9OFjS-e3EhZuq6D5rmqg0kOSF3aHQPFeIqTbT3zShH8PL4q8AO-JbCmZJykMmaEjmm7HiGMdY2Vr5hH2NY_rJmb0imyJQu8XDoG5iJpQrurfnsC8JDiVjNA90ncYJh06WQuKCFYt4Ttv-5c4Hx8QjGC98X4IDXDkml9LIjVfnBGdabuX9UWnrBLfVsVw1e4TZutV9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8940fb69d5.mp4?token=nmuZprnU1UjvRibC1exrsBBkZKiV-4RvT7_b3nFf1dMPCHrO408kCT90OyZFfTTSVWi9-0zqJvOTM2DOeMF5Os6tspvjzF_pW61immwiV3nzt7m5ewBKiTq7YGFF32REoZvgEJOQBT8I8KBY9OFjS-e3EhZuq6D5rmqg0kOSF3aHQPFeIqTbT3zShH8PL4q8AO-JbCmZJykMmaEjmm7HiGMdY2Vr5hH2NY_rJmb0imyJQu8XDoG5iJpQrurfnsC8JDiVjNA90ncYJh06WQuKCFYt4Ttv-5c4Hx8QjGC98X4IDXDkml9LIjVfnBGdabuX9UWnrBLfVsVw1e4TZutV9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
🇪🇸
پست‌سمی الچه در آستانه بازی با رئال‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/106586" target="_blank">📅 19:24 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106585">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">✔️
🇮🇷
🔵
گل‌گهر در شروع سطح دوم آسیا مقابل الجزیره امارات به تساوی بدون‌گل دست‌یافت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/106585" target="_blank">📅 19:08 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106584">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vMOgmpqU8aVOhLiNVqVVXfmIKvVNepiTC0ENcJgk0YZcm37GqIuWJzLveCY6zjOAFTl-5vZ2hbVvoA7SiUPJ9HMhe3bomvy7WQYhF_T4BBK1DoMKw2cbMnhO2lhLJOSQAeGpjEUErgvpO9FgobRng2ltqCjbBYhSjV_f40ME7_x0O-n3DpLmVQAiBi78Yc1e715PerdcECsh7W3UUOizIiT2Vfcn4bAoOFbSt26fPGkOtDXmDspitwtUB2rj6AaIRjzctckQ-rmRJYTPILKOwuPHidtqQdEmIXeuARIzKVKVpYN6KVgm9guk1tVVGsimrcqnn9LJp5YRdGOHk9f5Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
📊
🇪🇸
🇪🇸
لامینه یامال دومین بازیکنی در قرن بیست و یکم است که در 5 هفته اول لالیگا، 3 بار هت‌تریک اثرگذاری در لالیگا کرده است. تنها کسی که پیش از او این رکورد را ثبت کرده بود، لیونل مسی در فصل 2012/13 بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/106584" target="_blank">📅 19:04 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106583">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e25f47d65.mp4?token=FjMM_c3UKdykwQ19Fm43pk-GScv6ouqIPZ39GNuO7UYtgY7O0tCTuMAbcvzPnFbtQ483YvNBYlBvDhJKpACYi0lG0J77c47ksubwFGSqMfFt1A3B2q42cIgNlCMnFjEfWjGhjKBWHs3IlZhjaan-81MyDUEpQE_RMFn8s5uNxfZq37-89vA9FOSnMcKNxUuySXz_Q5AEE7TE8YZyDe2ZOYTP1N_8kWUMrxX2zjpaDi8oHFaMT2aSPjUdf3tj3Q_pf36zV53kRDbPWIMPGJFGdOQxPGp-HmulZCFdurHM6L865N9L9DB0uLqrs7nlSyJrAwv21bJLXSSgo0jEYBlebA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e25f47d65.mp4?token=FjMM_c3UKdykwQ19Fm43pk-GScv6ouqIPZ39GNuO7UYtgY7O0tCTuMAbcvzPnFbtQ483YvNBYlBvDhJKpACYi0lG0J77c47ksubwFGSqMfFt1A3B2q42cIgNlCMnFjEfWjGhjKBWHs3IlZhjaan-81MyDUEpQE_RMFn8s5uNxfZq37-89vA9FOSnMcKNxUuySXz_Q5AEE7TE8YZyDe2ZOYTP1N_8kWUMrxX2zjpaDi8oHFaMT2aSPjUdf3tj3Q_pf36zV53kRDbPWIMPGJFGdOQxPGp-HmulZCFdurHM6L865N9L9DB0uLqrs7nlSyJrAwv21bJLXSSgo0jEYBlebA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
امیر نوری بازیگر سینما: والا منم جای نتانیاهو بودم به ایران حمله میکردم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/106583" target="_blank">📅 18:31 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106582">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8cfdd069b.mp4?token=Okrn2lclBCLnNBQidkB-GVp-6CALJxbcTYcCm-TJP7fgwgTYEt4A5_Lm2uWNoOkOB0F-gcDMrmHkcMJOTsuNxfg_z67FYJ294OSY2KqLaYrScykC-Eqt1KYqmoGZKnqupZJJhKW5swTThljqOTE8SFZu6Wp6uLz1nsXme-KDU-Et2Dmkud5BJWKyhG9ZanQjMO27BQHrsA7dwcM-f3xVJ9tf4GE63CWpzFs-ZVTriNOvIG7uRb45iP41TrSOF8nu0cF-cj5FMgw2U2wev1oReM3vhhAqF61vIHA0nOAn0Pyx5AaWpIoeQsgKjDe6N4BYceXvXiXPJpW2DQSSLvsM7ro3jWcdBMOBOkS8mhHgXS9_JUjvRK36jU57OVKuZbv1tz9UJtwQ-ZCkQl6B_cBGQLqjMKAZbYh2nXSgrczsReG6E1_N5EBdwUsxW-u-dXeQW7WePScdwsXU23GmHP9jSx68su308c5Ag0K4fymdH_iaZTCm3Zxm7d5e8Q_tH2vGd3GDQ7ryIw0Fpf-KjxabBilH6VoNN_pAC12wMHAsyN1BCKzi6jeiHcKpjGgSxN3PRaH1d0wYUYpiMd2iB7mK1uZOfSTps4o4qoSWBeI-mtQsZMTo2CUCcCeASoDYb30TAvkjf6w5p1S45vvRBmUzvDDN5PC6oTGQUEohi8Uz5bc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8cfdd069b.mp4?token=Okrn2lclBCLnNBQidkB-GVp-6CALJxbcTYcCm-TJP7fgwgTYEt4A5_Lm2uWNoOkOB0F-gcDMrmHkcMJOTsuNxfg_z67FYJ294OSY2KqLaYrScykC-Eqt1KYqmoGZKnqupZJJhKW5swTThljqOTE8SFZu6Wp6uLz1nsXme-KDU-Et2Dmkud5BJWKyhG9ZanQjMO27BQHrsA7dwcM-f3xVJ9tf4GE63CWpzFs-ZVTriNOvIG7uRb45iP41TrSOF8nu0cF-cj5FMgw2U2wev1oReM3vhhAqF61vIHA0nOAn0Pyx5AaWpIoeQsgKjDe6N4BYceXvXiXPJpW2DQSSLvsM7ro3jWcdBMOBOkS8mhHgXS9_JUjvRK36jU57OVKuZbv1tz9UJtwQ-ZCkQl6B_cBGQLqjMKAZbYh2nXSgrczsReG6E1_N5EBdwUsxW-u-dXeQW7WePScdwsXU23GmHP9jSx68su308c5Ag0K4fymdH_iaZTCm3Zxm7d5e8Q_tH2vGd3GDQ7ryIw0Fpf-KjxabBilH6VoNN_pAC12wMHAsyN1BCKzi6jeiHcKpjGgSxN3PRaH1d0wYUYpiMd2iB7mK1uZOfSTps4o4qoSWBeI-mtQsZMTo2CUCcCeASoDYb30TAvkjf6w5p1S45vvRBmUzvDDN5PC6oTGQUEohi8Uz5bc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های شنیدنی مجتبی پوربخش درباره جاویدنام سحرخدایاری ملقب به دختر آبی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/106582" target="_blank">📅 18:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106579">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be0ea3f6da.mp4?token=kN_nZGYfUI9n4hwx0-Q8cws6MrTr3XjWpsvc4gL955fRyVNRwzgG10AVRK27mMWH26fXeKcOu7CxzfVT-2QG7aqcRgDNDfHkp2uwX6pVZf_ULwf5uWu-LHsuNjjCFgHUvN0LDq6xFQShvmlcr09Ss80bDJnl11hHCdEjmjmXLlIGBJypG9k0du6CR1bRvP3Bxe9x34CyK6uF82QCrZ8Zc3aRHyJyHnkvv8h5StlvQKMOYA60KAhM7hn2nPoP-GhGA2ATIy4a_oJgnLoe3Jpd6suS5a__ZJXsBA_Bwpq6vwhwqmEW5sK-IxOiRAA1QqOEyNundoZwbVw88kxa14EKEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be0ea3f6da.mp4?token=kN_nZGYfUI9n4hwx0-Q8cws6MrTr3XjWpsvc4gL955fRyVNRwzgG10AVRK27mMWH26fXeKcOu7CxzfVT-2QG7aqcRgDNDfHkp2uwX6pVZf_ULwf5uWu-LHsuNjjCFgHUvN0LDq6xFQShvmlcr09Ss80bDJnl11hHCdEjmjmXLlIGBJypG9k0du6CR1bRvP3Bxe9x34CyK6uF82QCrZ8Zc3aRHyJyHnkvv8h5StlvQKMOYA60KAhM7hn2nPoP-GhGA2ATIy4a_oJgnLoe3Jpd6suS5a__ZJXsBA_Bwpq6vwhwqmEW5sK-IxOiRAA1QqOEyNundoZwbVw88kxa14EKEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
وضعیت ریسینگ حریف بعدی بارسلونا:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/106579" target="_blank">📅 18:03 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106572">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zy5c6IL4y62QNJ8kOcerHoxb803lZEkOLYrHHsR4N8Cf-4yh0yUKdh-8FGUxmjvC5aSdnlJPOOnk3YpTz-S_6R9temo6Yxi50J25XcIcW99g1C6T9mkOl25q2KLCz6YFDZ4CQ-NAGrDIFcB4nvHuGXxhb_7KEen0f8jn0G9q8MdZOXEk9uf3yqis8q69OxAjz0WBdGcjI5VUFnKB3g4GVhZ0Alp0nHaQeX3BJtWp79kBWGHlxv4sAr0RZruiK47gsXGrvaGACtXI3cj2BuRXtEcYxGxL-TCex2uv8rBaoxko1hej9w-wkJC-YQCG3EAHzo-H8KtMnwXQds9JNwP7aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🏆
جلد امروز نشریه لکیپ‌فرانسه که بنظر باید برنده توپ‌طلا رو از بین همین ۵ نفر بدونیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/106572" target="_blank">📅 17:20 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106571">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4542b716f1.mp4?token=UEVHvGCtiB_1Y26D2NfQENcljZ3a1oIafpFTJ7bGKA_7ro-4fJLSYa5QZTeO_fXz5-jefqYLaiz8zbVzcwv-O7VUUWmcOmwUnzIdmhPlU9q0pd9ebOWLJZ2AN_sk7BUbqX7fDJ3eAO260zHdL_2e68pGPVQpMNvJ2z8AM08TvtSiuMWqga6Vx5MylFsW1YSYgx4l3NjB3cS4Ax_ZooNqCrnxJIWzfzBbj3YjDhSeD0jU6YNpdXtvudcNYfn5LFcZdYyIRkbrEXwRghQCzX5t5pNs1BhXbBWYr5eJq4Un34KB1nGkYPqwUKIwDW886panFLxWSRRj6_F0UPJsJAkxiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4542b716f1.mp4?token=UEVHvGCtiB_1Y26D2NfQENcljZ3a1oIafpFTJ7bGKA_7ro-4fJLSYa5QZTeO_fXz5-jefqYLaiz8zbVzcwv-O7VUUWmcOmwUnzIdmhPlU9q0pd9ebOWLJZ2AN_sk7BUbqX7fDJ3eAO260zHdL_2e68pGPVQpMNvJ2z8AM08TvtSiuMWqga6Vx5MylFsW1YSYgx4l3NjB3cS4Ax_ZooNqCrnxJIWzfzBbj3YjDhSeD0jU6YNpdXtvudcNYfn5LFcZdYyIRkbrEXwRghQCzX5t5pNs1BhXbBWYr5eJq4Un34KB1nGkYPqwUKIwDW886panFLxWSRRj6_F0UPJsJAkxiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⁉️
چطوری سرشونه های گرد و پهن بسازیم؟
به توصیه های استاد هانی رامبد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/106571" target="_blank">📅 16:31 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106570">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E-QdcsZgegfiErpEL7sH5yNKfB7bA7VwriC7EkVtOzhDfPQeFiPAzJVEM6qZXZldl8qn9q-PFZ1BomzeCR3Pk2FUN83KZB28hKLuSMyHX2NWSa6ODso3lQPSjY-GcTZFINpqa9Xhuw_eP2gxDFIr8vt_M8DNpCnKWpzOeKVZHOi1YTIf5cvR065YZLwjDFSobBrzqhbjEausiMZvR9DjcWMJgZ-ut4E1nl52AmRgOlWSm49ubSdv-LHYpaCCkShmTUsKh2vuRPbJAs7--9zCooVk4wDYFk7xuxO_E0yJr7stLH-EjHlEa1PJX7LK8mIDnEjU8Psj1arlhQPjlBS2uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
عملکرد فوق‌العاده‌ پشم‌ریزون هری‌کین در بایرن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/106570" target="_blank">📅 16:05 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106569">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2aef2c9a7f.mp4?token=QisQBO1tAkB8PfeMP2_gK0xAgRs00_o4YF9oSp9G874gd-1UtdnTqYsHNOJyJaqhGQ0w5GJh2FTh_ELWHbJ2N-IGiEsWxRgHkmX_burQY3Y-uVipiWtmIbabDsBP_6fz7LzJuwRpGEf64k9uhxV4GU5M3CkueqGbe81H37BUUB-kHFsDjdvD0WhNsrQ1TMZPWp5YLPxE1xFTqnOHyTyw_3QlWWV_uTPJ3zTSP1ixi3kj1ZintTbvlStQSNk01-Wa0M4_-9Vb_yEfKVuHqflMCULhuPWwZurQLvpLTCuzcTlZH6MA7rbLRmFlk2phL5DzVuCP1oaVT9gyds2mkvOfww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2aef2c9a7f.mp4?token=QisQBO1tAkB8PfeMP2_gK0xAgRs00_o4YF9oSp9G874gd-1UtdnTqYsHNOJyJaqhGQ0w5GJh2FTh_ELWHbJ2N-IGiEsWxRgHkmX_burQY3Y-uVipiWtmIbabDsBP_6fz7LzJuwRpGEf64k9uhxV4GU5M3CkueqGbe81H37BUUB-kHFsDjdvD0WhNsrQ1TMZPWp5YLPxE1xFTqnOHyTyw_3QlWWV_uTPJ3zTSP1ixi3kj1ZintTbvlStQSNk01-Wa0M4_-9Vb_yEfKVuHqflMCULhuPWwZurQLvpLTCuzcTlZH6MA7rbLRmFlk2phL5DzVuCP1oaVT9gyds2mkvOfww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
🇮🇷
فاطمه‌مهاجرانی سخنگوی دولت در پاسخ به سوال یک‌خبرنگار درباره چرایی تبریک‌نگفتن برد دیشب استقلال: ما فقط بابت بازی‌های تیم‌ملی تبریک میگیم و توجهی به سایر مسابقات نداریم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/106569" target="_blank">📅 15:40 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106568">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec515fb788.mp4?token=W0kX3y7klXyAM0i7m0NPa-hUz5TdIpkiiZzrdb-uXNp0RFGSCitLzdRn9fsDrTT3Wkb2_dlvkTPogFizQ0P3vmH1Qf7KNXdH_mW2sqwTH9KCGq3aKAWSMsfe4N5rH7_jhKS0Ek-UqFPcyboxI3dTcl0qpeiQlRJBvOAfuW6_JyptSDcxjz949ONfBxfJtCmMefgicuHcrk3KaWWOFlqiak9ip-xlFDrtI3F1Fw3l0MYVObsQLuaAzx8VJK0VRYX9sgNAVV00Mg22jd3cFn6c9tIsXdwqo8_3cOIOh2WsSMpnqb9x2lfObXVsWtWp_2VHg8QshZneyfrJlx4aA6iQ8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec515fb788.mp4?token=W0kX3y7klXyAM0i7m0NPa-hUz5TdIpkiiZzrdb-uXNp0RFGSCitLzdRn9fsDrTT3Wkb2_dlvkTPogFizQ0P3vmH1Qf7KNXdH_mW2sqwTH9KCGq3aKAWSMsfe4N5rH7_jhKS0Ek-UqFPcyboxI3dTcl0qpeiQlRJBvOAfuW6_JyptSDcxjz949ONfBxfJtCmMefgicuHcrk3KaWWOFlqiak9ip-xlFDrtI3F1Fw3l0MYVObsQLuaAzx8VJK0VRYX9sgNAVV00Mg22jd3cFn6c9tIsXdwqo8_3cOIOh2WsSMpnqb9x2lfObXVsWtWp_2VHg8QshZneyfrJlx4aA6iQ8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
حمله تند مصطفی هاشمی‌طبا رئیس اسبق فدراسیون فوتبال به علیرضا فغانی عزیز!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/106568" target="_blank">📅 15:15 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106567">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64d6b37a2c.mp4?token=bO6-Es7wbmqINC8srGpTmG-wK5uDmdQlLKQPXQMpBpbBssicHiR_f5SRij2NvWlZDhXZX_ECZF_WXqWejS4TFGxz7bjnNLftJLpcrU-bMD3zAqReVlJl7h8cnj5iGPRKtfZEeONlbcry6BpJqZ0DRv5YV5K4HmvgYXdh8nqli45_81FfSHHl3AlLRTCc11zYBjwh_KaCkoWyjSZ-E5_kcTAmv2NRrmQ1OZpKNqpqvlHlUi5nmruvRSpKUjQy-Jw96YB2CPzv0wK3Sm4jl9K3DsmuMA0Xz9Rp4ORK-1Cn6UkIw36nClxJgqifGHHZa9kewKJ4UXtxhXtfyh9c-KEpyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64d6b37a2c.mp4?token=bO6-Es7wbmqINC8srGpTmG-wK5uDmdQlLKQPXQMpBpbBssicHiR_f5SRij2NvWlZDhXZX_ECZF_WXqWejS4TFGxz7bjnNLftJLpcrU-bMD3zAqReVlJl7h8cnj5iGPRKtfZEeONlbcry6BpJqZ0DRv5YV5K4HmvgYXdh8nqli45_81FfSHHl3AlLRTCc11zYBjwh_KaCkoWyjSZ-E5_kcTAmv2NRrmQ1OZpKNqpqvlHlUi5nmruvRSpKUjQy-Jw96YB2CPzv0wK3Sm4jl9K3DsmuMA0Xz9Rp4ORK-1Cn6UkIw36nClxJgqifGHHZa9kewKJ4UXtxhXtfyh9c-KEpyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
کل کل خبرنگاران استقلالی و پرسپولیسی در نشست خبری امروز سخنگوی دولت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/106567" target="_blank">📅 14:50 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106566">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fdGcMHYoGfPNCB8R_36ShF94sg7zivmrT4pL0iLj6SCRAakqMHeCgg98CRr6C1ovdL-IBLwShNgg9r214_ZR1Azs9Vz6en-NchGSE2i7SA-cgd-6OP1E_Rng1jK4bcn2AduPQHtVORISGPe2_k7ss9Um0ToGrdgt7LpEBY0GS9IbxN4Yn0t8UQaOGz8JqxzV0RM_tmL1Qkmh77VJk0wDscXN9zb0AqUUmANJPkAAp8S7wVzUDw7klntvlDU32fTtQWMypG0ZjCuVkEF0uogvPy4UsP3VYZaSeIVfJMzUzSnhEtMkYtjbZR5xilS_5OoMbVr6L3EThflK7hyQDGDq0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇺
🇪🇸
هانسی‌فلیک: مطمئن‌باشید تا سه سال دیگر حتما حداقل یک‌بار قهرمان اروپا خواهیم شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/106566" target="_blank">📅 14:40 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106565">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UaKmMNiMmNJDQg-lzBjUnwz5H03k2SId5LPegueRHpXM5tacc0qbvL0xier2x81sqNrOwuc9bK0-7JBfYTQK4OABq_indNK9rgqQkr9vWzFLVGNY_SSTS7XHo7re5bzGgnqgX-9jYpQg8RQWQMvUwwzz0heiDWnMszwOvgTOXVKgCbNaIA26XV3yno_DRmzd-m4jq-XGkuasFbHUIi-pQO_PpUkBjQjyIiEomqqCo9gjCeyjqPcfxrXXkuHr7xo9RlBQubM9DzhJHV5PZVIjs6od91ADeD886OlciPuFesRoajubxIEv1EqMowR6blM0D8kWBqqXUz7jG9dsOX--yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
اظهار نظر عجیب و معرکه از پیمان حدادی مدیرعامل پرسپولیس: چرا استقلال سه بازیکن تیم خود را به اردوی امید نفرستاد که امشب دو نفر از آنها گلزنی کنند؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/106565" target="_blank">📅 14:27 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106564">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kY3q16356JofLVfxUyCwXOX4J9kOdCvRZ71sYToJqKPXFdMJpM0CwcZdHQqUvXoBSRJ9fdClNGcWZaF_-H_a8_4ntep0BAHQYpw14FHvZ5-GBURS-vBkJXmesVwPX1bTjt1m6sYab8KOV904L0SUInGbvn73HPBaU6PA05BpDPv7YIcxL-D5xE4-NFcknSKW-8l1HYO2iRj2cOfKygy3AmbczCdBWzd_N-K1DZ2EjgudmPecxLzN0ghW8R-DvwdHX4r5iF5qobz7yrTNkT1ZLbInxIW-BxYEsBAfdDXE4v3dR2URY3aq-qfjAgW_7bSmr8uaVWFzRSdSwQuAwXqH5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
تا ساعاتی دیگر میزبان فینال لیگ قهرمانان اروپا در سال ۲۰۲۹ اعلام خواهد شد. نیوکمپ گزینه اصلی میزبانی از این فیناله
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/106564" target="_blank">📅 14:10 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106563">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed1f3faef6.mp4?token=LEinsVpW07V1HfA6UY839IjuT6L3FkzAd51uJbnKJ6x4_hsOaP7tcf9MsJYLk1Nps8j1MFKoXaHhKeZA6opSaWhHlYq5iMoIpa6QG6BTSkQ84bUhIGSEx5MuRvz10qzqW-CvQzHfr7WSW0RRSFADPM0-Q08wchQKwjqJ2c_NwkgAXuhlvVgWWNlq3VKWt0b3Kws3CGc4rdyTLysU7Z-O3MvLP8rzRGVDv8c-uCRot4UKZHElA67bflT31TRDp2tQZw3MFbPukL7vMJS0A-8jm2-2P_JI8HlawJFJXFKYn5Vw9w93OnLG3Ma25GQwIxJudVSvLaljWRVauPMQWXBv0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed1f3faef6.mp4?token=LEinsVpW07V1HfA6UY839IjuT6L3FkzAd51uJbnKJ6x4_hsOaP7tcf9MsJYLk1Nps8j1MFKoXaHhKeZA6opSaWhHlYq5iMoIpa6QG6BTSkQ84bUhIGSEx5MuRvz10qzqW-CvQzHfr7WSW0RRSFADPM0-Q08wchQKwjqJ2c_NwkgAXuhlvVgWWNlq3VKWt0b3Kws3CGc4rdyTLysU7Z-O3MvLP8rzRGVDv8c-uCRot4UKZHElA67bflT31TRDp2tQZw3MFbPukL7vMJS0A-8jm2-2P_JI8HlawJFJXFKYn5Vw9w93OnLG3Ma25GQwIxJudVSvLaljWRVauPMQWXBv0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
حمله تند و‌ عجیب یک آخوند در صداوسیما به صحبت‌های لاله‌مرزبان در حمایت از مردم مظلوم ایران در جشنواره ونیز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/106563" target="_blank">📅 14:02 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106562">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/589bf63655.mp4?token=TGBs44QnJQxJpWmh4HkE0FdADX5OBxIbPx3FLkBw19FzwSCFiA2UQ5OGzD6CAMTTLdGDGrVPXmmeNEYUmc4Ew4EBxjCwY9uyqHW7Sk7yR_o94dQeZxzjekmyt3U7yZPhqWekROGOmSItgy6hwSr_PwVM2xk6zjbO_Es-n-nVlFbg_mxONnQ5scof2IMj_kburXzCeWj8EECzqqd0VTfKwBFbhdeq80HQC02EWVbpDdZDFqw2Onw5Pkr5a66sxi2JETDFkh-2XYs3Alt_wWXROk5AEGJ6uHYuu603GXKazMzR6-OBL5-uJIp2c_ZV3phy7AFR2FeywbNco6UFjrSjlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/589bf63655.mp4?token=TGBs44QnJQxJpWmh4HkE0FdADX5OBxIbPx3FLkBw19FzwSCFiA2UQ5OGzD6CAMTTLdGDGrVPXmmeNEYUmc4Ew4EBxjCwY9uyqHW7Sk7yR_o94dQeZxzjekmyt3U7yZPhqWekROGOmSItgy6hwSr_PwVM2xk6zjbO_Es-n-nVlFbg_mxONnQ5scof2IMj_kburXzCeWj8EECzqqd0VTfKwBFbhdeq80HQC02EWVbpDdZDFqw2Onw5Pkr5a66sxi2JETDFkh-2XYs3Alt_wWXROk5AEGJ6uHYuu603GXKazMzR6-OBL5-uJIp2c_ZV3phy7AFR2FeywbNco6UFjrSjlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
🎙
رضا شاهرودی بازیکن سابق پرسپولیس: نعیمه نظام‌دوست گفت هروقت احمدرضا اومد پیشت، بهم زنگ بزنید تا بیام چون خیلی دوسش دارم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/106562" target="_blank">📅 13:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106561">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a994c05864.mp4?token=rD5OY3_xZdgwCz-cJAv1RHvbgqb3vkcGuCQNj8GWW2LlbfRPw5sbb5S37dNZx1TbzlZUZ6cE16lvUIYiJU8ANXUvw5fhkIIROth3MbMXfB34P9cCCx7AorE2mU6XI5wEQ3tNo__TydmFJ0r9EBh6eKnVXsvlnYF9pW8D94Vmsejbq6KX3_QL_NyuMw6e9Wclj4_R1fyn79E3ML0qT5ei1BlC70YWB4Lu82cQjb4hiqHZVuws9O4tQM6bt9EZ1WBG8mwMWgpXmZGuO_pj_5pel81-r3f3XOTHxdIs_0-VsRwfKoMiNzK_EygbE2MsmSZ4WSHxOVbMr2U4zrgbcp68Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a994c05864.mp4?token=rD5OY3_xZdgwCz-cJAv1RHvbgqb3vkcGuCQNj8GWW2LlbfRPw5sbb5S37dNZx1TbzlZUZ6cE16lvUIYiJU8ANXUvw5fhkIIROth3MbMXfB34P9cCCx7AorE2mU6XI5wEQ3tNo__TydmFJ0r9EBh6eKnVXsvlnYF9pW8D94Vmsejbq6KX3_QL_NyuMw6e9Wclj4_R1fyn79E3ML0qT5ei1BlC70YWB4Lu82cQjb4hiqHZVuws9O4tQM6bt9EZ1WBG8mwMWgpXmZGuO_pj_5pel81-r3f3XOTHxdIs_0-VsRwfKoMiNzK_EygbE2MsmSZ4WSHxOVbMr2U4zrgbcp68Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🇮🇷
🇶🇦
توصیه جالب صالح حردانی به نیمکت استقلال بعد از درگیری با بازیکنان السد برای سنگین کردن جو علیه حریف قطری: همه بریزید داخل زمین!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/106561" target="_blank">📅 13:10 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106560">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HFfyQh6HeJdsRnkDB2F8vNweYfQcQvfOn3j6gZYW-y7-hOURpRlBJDXyasuOqZDxXNl9GBzD-4L3-GnLu2KGBVkmXaXRreFgI6u-y05jcOe_glXqV9EmF0LeyATP1KVia1cT2wuqUGsU7u4LZnSmzMVGW9woUMO0-yDRJanoLWQbifpq2tw0AMHrGYj-D4Oc7ixHucWBLZks7auyrVX2sZ1FgsGKheOlnU4D3iaXEO12l1V-JHl2XzP8V4i9jaJUFiJiFiEGMoFjlW8MThL-xkRaKUBz4YkuBhRfqw3FK26NCAxpXyRlWjcUdxGLkDvvc1yo_w_ooiw1yv5qits63Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🎙
🇪🇸
آنتونی گوردون:
من با این باور اومدم بارسلونا که می‌تونیم تمام بازی‌ها رو ببریم، ولی خودمم فکر نمی‌کردم قرار باشه همه بازی‌ها رو با ۵ گل ببریم. ​الان واقعاً هیچ‌کس نمی‌تونه جلوی گل زدن ما رو بگیره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/106560" target="_blank">📅 12:38 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106559">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OjpGkikYI9YoUGmRiNjtCO7OF8drBKcjYo9oKBDrYZKm1NWNps3flVCRZ51XLvTbpeWiLsGisDce6zjpBfxH5KvB6pdKCFYUVz9Ug9tH9mMPYN1XxnmfcDMspQNDhXfU4wT7Nfg29oKcoxtawoTS6Xq35die1heYOqUCNIRvxcSH-Z3kTRmBDSYmAWIVOM7rDI41Sjy8ddHKK-xXWpm14Y6L_iVMm2fcND-bCsunOpg_uGxkyBmOj3j_c8el21Yebwh5tzvuyg2ZKA2t25exJfVEdguPBIhK_voXz7ci2qoySg8i-Ekb9IxAF1j51ahQB0jydBQnJt432Ac4SlcWdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
برنامه‌مرحله گروهی گل‌گهر در لیگ‌قهرمانان آسیا ۲
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/106559" target="_blank">📅 12:33 · 24 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
