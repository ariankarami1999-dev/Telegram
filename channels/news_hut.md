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
<img src="https://cdn4.telesco.pe/file/s6aD9SqDNdRDkR3qA5JqmmXyF8OJG6y2yXKnNUp_jzEMu6OY740KbywtNZYcWkeUQn5LGi_aw01EOG0w9R1PFTgCAifmj853bd3xbvWE9jVt-_OW2q7Ct3s5VW39g0v_INM_E1ScXZ_mCJ4b2CWRyrqHcGuxizlABTv4GptcrWgHHuMUaoJpRLDZwuQigjKFI9I7XaefAXcp_0TWFs68ch8o7hf9F9p4h9tgct-PEE7tX7772As_arjkUNNiZIcWDhRRjdTAvHugJb2OFHSRhgSzpy8aijHy4JZjtnFcvwggksX7oiOpbYwvRCIgjN_FHfolGqTtY6ogkkbF4j0M8g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 104K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-22 16:41:30</div>
<hr>

<div class="tg-post" id="msg-73281">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/544a54e3ac.mp4?token=qpDFtX32nue8v8o4uXyiroI9lJrc-a2mClBbNFIUTzbhPInBcjQopN767U6YdzUn7kmwdvS_I7GHUMe-XAJu75Iy6PADK0LGNi3D9E4Pm6JB7pCqXwexxVXRmO51Q0kTPSk_vLk6PzlDmf0-fJMkR5Yj7HtVyCnGYV2KEvxeYsQY5-BARwgRFJw05X8HmnkykYm61LFBQRj6fdsSnbdKokqNDnT2sPpoS47qrxwHt0UtP-6hAVnh-zGFXcn0QXtVz8v4-JFcnnaC-fWRJetgyT2Ppfh3v9Lp-MyVG3KNdU4jKcFIHHB6GTkjUR4UsZMpHCg4s_Ueo4zt-5ITfU37vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/544a54e3ac.mp4?token=qpDFtX32nue8v8o4uXyiroI9lJrc-a2mClBbNFIUTzbhPInBcjQopN767U6YdzUn7kmwdvS_I7GHUMe-XAJu75Iy6PADK0LGNi3D9E4Pm6JB7pCqXwexxVXRmO51Q0kTPSk_vLk6PzlDmf0-fJMkR5Yj7HtVyCnGYV2KEvxeYsQY5-BARwgRFJw05X8HmnkykYm61LFBQRj6fdsSnbdKokqNDnT2sPpoS47qrxwHt0UtP-6hAVnh-zGFXcn0QXtVz8v4-JFcnnaC-fWRJetgyT2Ppfh3v9Lp-MyVG3KNdU4jKcFIHHB6GTkjUR4UsZMpHCg4s_Ueo4zt-5ITfU37vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در جریان اجرای ارکسترال «آرش» در سالن اسپیناس تهران، در شامگاه جمعه ۱۷ مهر، تماشاگران در واکنش به صحبت‌های اسماعیل بقایی، سخنگوی وزارت امور خارجه جمهوری اسلامی، او را هو کردند.</div>
<div class="tg-footer">👁️ 1.35K · <a href="https://t.me/news_hut/73281" target="_blank">📅 16:33 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73280">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41a28d4b0f.mp4?token=G65KOthb1w7WkWcVJxtZg3YLlc21zAYPbsg1CeOM7btrGRdaSlQTEqKYWX1xy-sUEBABkuiMvL3r-x5GfUtXnLmLjfB5aMQY-xrAuY929bfEh4M9CIvx6jYElZJCrzu1X0OxmvD0QZgWDKzRSoSokZSn9Xar-hxDmvKNlfk7FJ45CnFpKtZYbPJBptr7uqbPHfJ2c73r6eGaunzR5LH7bowiqM1a0h27Ojsk7i6apdZVFyF92v4MGzk7KVN3VPqlVwzrLhEgGbF0g0vDgD_kwtvJOS2vPLxbneiNjcudIZIsBfY6C6mJT0JtpEwBzhBT1KNl-wgGRCTnT1i7YNRfjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41a28d4b0f.mp4?token=G65KOthb1w7WkWcVJxtZg3YLlc21zAYPbsg1CeOM7btrGRdaSlQTEqKYWX1xy-sUEBABkuiMvL3r-x5GfUtXnLmLjfB5aMQY-xrAuY929bfEh4M9CIvx6jYElZJCrzu1X0OxmvD0QZgWDKzRSoSokZSn9Xar-hxDmvKNlfk7FJ45CnFpKtZYbPJBptr7uqbPHfJ2c73r6eGaunzR5LH7bowiqM1a0h27Ojsk7i6apdZVFyF92v4MGzk7KVN3VPqlVwzrLhEgGbF0g0vDgD_kwtvJOS2vPLxbneiNjcudIZIsBfY6C6mJT0JtpEwBzhBT1KNl-wgGRCTnT1i7YNRfjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو ژاپن یه زن 29 ساله برای خودکشی از طبقه یازدهم میپره و روی یه دختری که داشته از خیابون رد میشده میوفته و دختری که از خیابون رد میشد جونشو از دست میده، در حالی که زنی که میخواست خودکشی‌کننده زنده میمونه!
حالا قراره این زن اعدام بشه...
@News_Hut</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/news_hut/73280" target="_blank">📅 16:01 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73278">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v3YusCmCAc-_gWsfDVSqO-taFD2Z2dJJaVOI-HO4tvATQezyrxxiMbWRXTkGhYN2pLZF0Q4rvzE1Ri_PZVFg2yxVZ1qT1bkHXJLA8Fp-jO8G9n3ocm6c7GuVSdQj7V47s042nQqruCbbqHaOi_iklqbdv7Br2roru1u3CwMKzsLlyx7MRUV3XcLzKgCY_NVm4hIaex28OnDRQDsptnclvxgum2AHmYDKuMYnB9PMHzcttQZm2J0cMgMSbSqMptCMyf_mQ2hizpPRpJxwTG5dzUomUP2PX4bvIRZmiSAIqbPJkeq709WYi2rFQSDpxf4svvFXoan01d4iSf-WuYpt2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1f8ef828fb.mp4?token=Qo7v4KsuvUOeSrxqOnTqCmlSO7hPm_iwBbd2S3sIXYvMqp2WJFKRnwnkCavw1Ed9je6awHu0-WwGn-MKz4fYEJJGnWUzKF9uVyEuRdFfNqOkRq391LMW4KUiv77Qr3UUUtc_vCLXNS35FTdE5yalLfPDG8MQmCTAU2LWB-xpTG-JbPZ5w-lsHSKD1BNBLrlv-CG1GzV5wAwnnE-XpdJhjKKM49y2gMiFmEgq--IPbr13fHwnch2CA_GGRGun01CBYOJxCYxpkx_myT3uVyRL6E_0MWwcU7yCLl5Pl8vZm-Y1Tsw3G3JsFAppFy2te4QGGalE71xL95URuSd5L97vtg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1f8ef828fb.mp4?token=Qo7v4KsuvUOeSrxqOnTqCmlSO7hPm_iwBbd2S3sIXYvMqp2WJFKRnwnkCavw1Ed9je6awHu0-WwGn-MKz4fYEJJGnWUzKF9uVyEuRdFfNqOkRq391LMW4KUiv77Qr3UUUtc_vCLXNS35FTdE5yalLfPDG8MQmCTAU2LWB-xpTG-JbPZ5w-lsHSKD1BNBLrlv-CG1GzV5wAwnnE-XpdJhjKKM49y2gMiFmEgq--IPbr13fHwnch2CA_GGRGun01CBYOJxCYxpkx_myT3uVyRL6E_0MWwcU7yCLl5Pl8vZm-Y1Tsw3G3JsFAppFy2te4QGGalE71xL95URuSd5L97vtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی سینا مصطفوی از بازداشت شدگان دی ماه، نوازنده و از معدود کوهنوردای ایرانی که قله اورست رو فتح کرده بود، امروز همزمان با اذان صبح اعدام شد
💔
@News_Hut</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/news_hut/73278" target="_blank">📅 15:25 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73277">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/016589a6d1.mp4?token=esgVeyOqEBA9cSRNh3DeQXlvknnnH2tnIz9lvo_cf3woWnH5c1V-V7LzzCAn19JSl59ta6T6Jrdn27fDhGgSHD2B00YARblPKPGhpVTpgUyAdLupwbUdXwROg3ricJdmJLaKW-3_Iv7Hw50WCS4cXUsZSEtMPpkIjD8m96_3JKSSawDrlkXk55GxC4r-XcH57ElPmf6GfquufsPQ3D2v3dqCsTz_kWLWeHkejcuxaLelxSIxbnJ9qnlA-RnjxeNUnFFxMTxxqmdpU_6N-Uhmh0EHZFdQwkpHujmWqfHiLBYkTd5Ci2rBIUpc6HaHybClHa0hFwXFyFIfw3e5JIzd1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/016589a6d1.mp4?token=esgVeyOqEBA9cSRNh3DeQXlvknnnH2tnIz9lvo_cf3woWnH5c1V-V7LzzCAn19JSl59ta6T6Jrdn27fDhGgSHD2B00YARblPKPGhpVTpgUyAdLupwbUdXwROg3ricJdmJLaKW-3_Iv7Hw50WCS4cXUsZSEtMPpkIjD8m96_3JKSSawDrlkXk55GxC4r-XcH57ElPmf6GfquufsPQ3D2v3dqCsTz_kWLWeHkejcuxaLelxSIxbnJ9qnlA-RnjxeNUnFFxMTxxqmdpU_6N-Uhmh0EHZFdQwkpHujmWqfHiLBYkTd5Ci2rBIUpc6HaHybClHa0hFwXFyFIfw3e5JIzd1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیل کاتس، وزیر دفاع اسرائیل:
اگر حزب‌الله در حمله به اسرائیل به ایران بپیوندد، ضربه‌ای سنگین دریافت خواهد کرد و بخش‌های دیگری از خاک خود در جنوب لبنان را از دست خواهد داد.
بیش از یک میلیون شیعه در لبنان آواره خواهند شد.
@News_Hut</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/news_hut/73277" target="_blank">📅 14:56 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73276">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b6d991be7.mp4?token=HMftivBomX7eBGVpDfHalOU5gd4Gck1RrD-jk_fWYsReclTiKjaUcBWwZzBNA2Wnf7HZJ-Z0yly3i7LSAvRaqePgIGqnQ6CwicClQqFN2vBtGJF3414tyg1L2uZRk74g4dvztxIaJuQqHmRFJoZfY6dbP4A3y1H6TBaLg-t0l7DBZcVV3lAOy8Kl-Xd3kXGq8nvGriQ-rMTYd9rteXZEDASnt9X5nu25l7WKEQoyehlMqpfNi3z956OWPYZCh6F6pftYmuqgMTii0uwRby8C1GhtOG8IbdNoo6uHtmxSBLLk1XDyIHGfJlgnzNEr1FrxQO4Mzf2KPfAQm5wkfz2czA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b6d991be7.mp4?token=HMftivBomX7eBGVpDfHalOU5gd4Gck1RrD-jk_fWYsReclTiKjaUcBWwZzBNA2Wnf7HZJ-Z0yly3i7LSAvRaqePgIGqnQ6CwicClQqFN2vBtGJF3414tyg1L2uZRk74g4dvztxIaJuQqHmRFJoZfY6dbP4A3y1H6TBaLg-t0l7DBZcVV3lAOy8Kl-Xd3kXGq8nvGriQ-rMTYd9rteXZEDASnt9X5nu25l7WKEQoyehlMqpfNi3z956OWPYZCh6F6pftYmuqgMTii0uwRby8C1GhtOG8IbdNoo6uHtmxSBLLk1XDyIHGfJlgnzNEr1FrxQO4Mzf2KPfAQm5wkfz2czA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خانوم دکتر:
یه خانومی به من پیام داده و گفته که من به غیر از شوهرم 3 تا دوست‌پسر دارم و با هر سه‌تاشون رابطه‌جنسی دارم چون هر کدومشون برام یه لذتی دارن ...
هیچکدومشون هم از اون یکی روابطم خبر ندارن و 7 روز هفته رو تقسیم‌بندی کردم و پیش همه‌شون میرم !
اخیرا حامله شدم و چون نمیدونستم بچه از کدوم یکی رابطه‌هام هست، بچه رو سقط کردم ولی الان به‌شدت خون‌ریزی دارم ...
موقعی که با همسرم رابطه داشتم اون از این وضعیت شاکی شد گفت برو دکتر ببین برای چی این شکلی شدی؛ الان سوالم اینه اگه برم آزمایش بدم مشخص میشه من با دوست‌پسرم رابطه داشتم یا اینکه از دارو سقط استفاده کردم؟
@News_Hut</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/news_hut/73276" target="_blank">📅 14:32 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73275">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">خبرگزاری مهر:
«افسانه عقیله»، عضو سپاه پاسداران و فرمانده حوزه بسیج خواهران شهیده افضل در مهرستان استان سیستان و بلوچستان، امروز در حمله‌ای کشته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/news_hut/73275" target="_blank">📅 13:56 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73270">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJmiOUW-ier5qCH6OLfZ1MJOFV8fyHeW-5kMjJV5HdeOl949kM1yuIBsAj513LPkrJi0OWQ3B7O4c3m0qYigNQzNOcJkQBkA7td_zlzroOQV5Sg42bf81qwG1ei1Kxd65MxyIDfp5gPRPYz0407sWxIjQqqGAyZxljHNOEQQ8lhVWcY4teSpcXqddYQdpwVOlzG_CZW1NzINVjqrHGZHnk2SBgkTJTObVwlSWZNr-i3mqhS-QOmsZIsJbQUxjcOuvmovfc2N88YdRnauQq2BNiAVy_4TsudQM8lWIpLHtYQ3kKoftjB5WjfDU8Y9K05cadfaCVRRjPf8CU5DCksArA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0bb97d458.mp4?token=m9oCi1uD9Otm4bcP59jG7wxunc5Lkgs-Hj9ZKHRs82y7XdjuIetjGIDFC21e7BvLq-eh5nTEYo2pVTnvcujVN3kPddJu_XZIzz9pMj5i6KZ_gvMp_pp89mZGZ--Vjydb22sWP3nNvD40TapjfJ-FdP5flK462HItrXrNneDUgp_q-dwYpqHVlynY2Geb6z15PMU95QPdY2zJ_KR83IPIlp507EsbOemNHNSkRlQwn58cVoQN_AqEz1J6IYV79U_RJh7GB0fcGpaRNUhmzT-x0ySZtJcz1AiMpo-GB7nLUHRL-2Xw_eyF6Ra7bE93ZtszgVgGZbDP3NoJx_6BGWo7RIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0bb97d458.mp4?token=m9oCi1uD9Otm4bcP59jG7wxunc5Lkgs-Hj9ZKHRs82y7XdjuIetjGIDFC21e7BvLq-eh5nTEYo2pVTnvcujVN3kPddJu_XZIzz9pMj5i6KZ_gvMp_pp89mZGZ--Vjydb22sWP3nNvD40TapjfJ-FdP5flK462HItrXrNneDUgp_q-dwYpqHVlynY2Geb6z15PMU95QPdY2zJ_KR83IPIlp507EsbOemNHNSkRlQwn58cVoQN_AqEz1J6IYV79U_RJh7GB0fcGpaRNUhmzT-x0ySZtJcz1AiMpo-GB7nLUHRL-2Xw_eyF6Ra7bE93ZtszgVgGZbDP3NoJx_6BGWo7RIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساعتی پیش، اوکراین بوسیله پهپادهای انتحاری به پالایشگاه نفت نووشاختی در منطقه روستوف روسیه حمله کرد که باعث ایجاد انفجار و آتشسوزی گسترده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/news_hut/73270" target="_blank">📅 13:40 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73267">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FIvqD2Ppw9CdmG_M2WQZvzmT-W-J6NghR07ZefA_GiimJ5uq-DC5YcT5UN7we3pxATeklZC0xJq4R6zfADhoI7b8LDKA4pAT6FrD8NneoNZTZhDaqIggu2YmbKBakJ1-yv0VMzsXSU5ZpRMGoBV3y72AOJl5XLMZc7i4GgchkVmUIZC1oEK8LnueWTwUzqbvoXd0cuecTBkMD-5lNRTHj1OwAff_HCGFqKd2eglGqcwitqBfGMqjVFfmIbdsfj8U2UNWrPCoM6-D1dpYKWwui8hHBTzrv_HT4pwA6xNltEt6wGc_Nona0rpXBM2J0tJN6nMD1N4pCwM1rrxL--dt5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y_NT-VEbIPblTfi-BM6KAvstYRdgiENf1KRbVUOJ-hx9cxMTexxwduuOh2RRLu0bacj0Ryk8-EIhTeIguE9DhUibmJ_9ulSLJkpGTbBROzsGZQMPxVpRqlV6o_UpN4WRADhqwkS9Oq-ts1mHY7ZpSYQIxvLWKG4Sh3QL1461X1LvlcItRN3yw6VuNm7cQlFXegXsYtJ5pQ_dyggOsMpi2TZLeRhFkpJhrcl4JX1eMRoIocpitV7KUVhebai2-9-5-HG6JspIj7FSvFYma0OsB7tABRX47NYfTpCEDh7jeqS9j358tXzC2-ws_uVOW2zEOgqHi1AHn4O-Xfff5Nfvhg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd22e2bf5b.mp4?token=o52HQh8fFicUO3jS-3QzVaEfmNGH_XoI8tYqqlnVdDNl9rVYdr6KvJOGLcyz-X_FMx39UstAzh7sjhfg4B7r_H3udbU_DCMrPB5gBm4MABr3-jJYpve3nnjmUf8mxIOSx38uLZa2Q4KYOLCkwBS5I9fDHMboIoWgEmpSMPl3QQ9BqpcZcs2FXMGjhEp15vy0vt1ZeBZAy2UiSrgo398xiv1ms-59ifhtxNb6rO0A5J6V9Lp8H7WCvZz1P2oKlZ0-ruv1BRYxCgLxgSsUBSHQ-fNaHgOmDHem857t-9swy5dQOdQKz9O33yPF8M8eqvqUP0im1be0yDWyNgxWFM8TOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd22e2bf5b.mp4?token=o52HQh8fFicUO3jS-3QzVaEfmNGH_XoI8tYqqlnVdDNl9rVYdr6KvJOGLcyz-X_FMx39UstAzh7sjhfg4B7r_H3udbU_DCMrPB5gBm4MABr3-jJYpve3nnjmUf8mxIOSx38uLZa2Q4KYOLCkwBS5I9fDHMboIoWgEmpSMPl3QQ9BqpcZcs2FXMGjhEp15vy0vt1ZeBZAy2UiSrgo398xiv1ms-59ifhtxNb6rO0A5J6V9Lp8H7WCvZz1P2oKlZ0-ruv1BRYxCgLxgSsUBSHQ-fNaHgOmDHem857t-9swy5dQOdQKz9O33yPF8M8eqvqUP0im1be0yDWyNgxWFM8TOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروی دریایی سپاه پاسداران اعلام کرد که یک کشتی کانتینربر حامل بیش از ۲۵۰۰ کانتینر، هنگام تلاش برای عبور از تنگه هرمز از مسیری غیرمجاز، با یک مین دریایی برخورد کرد.
این کشتی صبح چهارشنبه در جنوب تنگه دچار آتش‌سوزی شد و غرق گردید.
@News_Hut</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/news_hut/73267" target="_blank">📅 12:56 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73266">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">تا انتخابات اسرائیل و آمریکا چقدر مونده؟
فقط ۱۳ روز تا انتخابات پارلمانی اسرائیل در ۲۷ اکتبر ۲۰۲۶ مونده.
انتخابات میان‌دوره‌ای آمریکا هم ۳ نوامبر برگزار می‌شه و ۲۰ روز تا اون باقی مونده.
@News_Hut</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/news_hut/73266" target="_blank">📅 12:14 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73265">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HrOCkWdbFdIzq0-lt5n5trn5CdahiXPtWyBvRK38NnOCheRWVmoDB6bTj_62Kdmw4oq5GBAS59tj9ARMuNhE3XNddduuOYlubhLwyBz8tdjqmSAsucd7ef92Jaz7FRs3HMwpIdXdQUhaEFvLClzCCqaJQamaG9zijr4rFDEMF1WPI4fK2lKJY2W5oyX9E_5Ppn3RmD8XEt9amOzMJrbtRVs-bdTpuvaLp6ux9aFQDgKe1v2sUb5nJdJESECFJMAf_m77m9jDdKqV9R2Pm5SS-XeCGevZt2KqAcqyISwfHwa0_pgeDTOH6XKo3kCEb7baSN4xAGqRgnhuHaiCz9wuZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری؛پست جدید دونالد ترامپ در تروث سوشال:ترامپ ویدئویی منتشر کرده که در پایان اون بخشی از سخنرانیش در زمان آغاز حملات مشترک آمریکا و اسرائیل به جمهوری اسلامی آورده شده که میگه:
🇺🇸
ترامپ: این رژیم به‌زودی درخواهد یافت که هیچ‌کس نباید قدرت و صلابت نیروهای…</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/73265" target="_blank">📅 12:04 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73264">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهات نیوز | HotNews</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/240fbc3c81.mp4?token=bGw3NjM1rnnKQ1mtkU-owFxFtQPjMBFp70Imw4lad7jpMKbafzFXNo_YaJGcjC-ySP5a_yjs4Z_mLyrUSkmHY0tUR8VOUC-0oLEMkd14BjPnzXAPuZWPFZQPKeAqUk7vDtve_jqaFtQSvNMlW1XkP7mUmMq2kSLqklvUKwqjzqMRQ-Y6PGgHqM-5Kv4-sthKwyOO-QH4d7_wM4Q-Itr4l4xZ6UkfN1MX3Bf1gBP9DFU3GuVkYtcP4xkd5NBFa38rWVbTkVxbnKFp9N4j3dqv2xhPE2j6_rAGW8ZyTAGNyYp19d2RhC-UuO87BgmCruGX_7Wkb9FIYO5Vipy4WjgnWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/240fbc3c81.mp4?token=bGw3NjM1rnnKQ1mtkU-owFxFtQPjMBFp70Imw4lad7jpMKbafzFXNo_YaJGcjC-ySP5a_yjs4Z_mLyrUSkmHY0tUR8VOUC-0oLEMkd14BjPnzXAPuZWPFZQPKeAqUk7vDtve_jqaFtQSvNMlW1XkP7mUmMq2kSLqklvUKwqjzqMRQ-Y6PGgHqM-5Kv4-sthKwyOO-QH4d7_wM4Q-Itr4l4xZ6UkfN1MX3Bf1gBP9DFU3GuVkYtcP4xkd5NBFa38rWVbTkVxbnKFp9N4j3dqv2xhPE2j6_rAGW8ZyTAGNyYp19d2RhC-UuO87BgmCruGX_7Wkb9FIYO5Vipy4WjgnWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری
؛پست جدید دونالد ترامپ در تروث سوشال:ترامپ ویدئویی منتشر کرده که در پایان اون بخشی از سخنرانیش در زمان آغاز حملات مشترک آمریکا و اسرائیل به جمهوری اسلامی آورده شده که میگه:
🇺🇸
ترامپ:
این رژیم به‌زودی درخواهد یافت که هیچ‌کس نباید قدرت و صلابت نیروهای مسلح ایالات متحده را به چالش بکشد.
🎙
سخنگو:
او به جهانیان یادآوری کرد — همان‌طور که بارها و بارها گفته است — که آمریکایی بودن، نمادی از چیزی شکست‌ناپذیر است.
اگر آمریکایی‌ها را بکشید، یا هر جای این کره خاکی آن‌ها را تهدید کنید، ما بی‌هیچ عذرخواهی و درنگی به سراغتان می‌آییم و شما را از بین می‌بریم.
ما آغازگر این جنگ نبودیم، اما در دوران ریاست‌جمهوری ترامپ، آن را به پایان می‌رسانیم
جنگ آن‌ها علیه آمریکایی‌ها، به انتقام ما از آیت‌الله‌شان بدل شده است
🔴
ترامپ:
خطاب به مردم بزرگ و سرافراز ایران:
لحظه آزادی شما فرا رسیده است.
وقتی کار ما تمام شد، کنترل حکومت را به دست بگیرید؛ این حکومت از آنِ شما خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/news_hut/73264" target="_blank">📅 12:02 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73263">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/377d554e40.mp4?token=NjSCYPcmvQBRr19QBqY5T9T2v2eTv5pYBLqL5cVQ2pzolMCcwEeIk2XGB39OmHl-JPiL6ozQTFUxQ2s3tYBjxsxfac8ZJah6cRcHcPBVkWhAQX9Z5BT7uJih-5EcPZhdUoRHj3qZfPqcXy5JdoWL0ZUNWtec7TenI0Md_4FSfpFYGimJcdZ3RGw1QDHB-n5_f6rSbElrIsp9zoaUzm1YcSyQ6JJPrczaXXnxI1CZssuAWMtuFF_M-YaVG-L5SMhncBOwG6eyZ5uhHIcggVL-UVLgh-BX0sSrqsyIkUiOGeXSJYRZ7J36vm5cZVAemXafk2J13skHqApR6EVP0HB1xQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/377d554e40.mp4?token=NjSCYPcmvQBRr19QBqY5T9T2v2eTv5pYBLqL5cVQ2pzolMCcwEeIk2XGB39OmHl-JPiL6ozQTFUxQ2s3tYBjxsxfac8ZJah6cRcHcPBVkWhAQX9Z5BT7uJih-5EcPZhdUoRHj3qZfPqcXy5JdoWL0ZUNWtec7TenI0Md_4FSfpFYGimJcdZ3RGw1QDHB-n5_f6rSbElrIsp9zoaUzm1YcSyQ6JJPrczaXXnxI1CZssuAWMtuFF_M-YaVG-L5SMhncBOwG6eyZ5uhHIcggVL-UVLgh-BX0sSrqsyIkUiOGeXSJYRZ7J36vm5cZVAemXafk2J13skHqApR6EVP0HB1xQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیروز تو بریتانیا، یه مرد جوون وارد محوطه ببرها تو پارک حیات وحش یورک‌شایر میشه و اونجا یکی از ببرها به نام آلتای بهش حمله می‌کنه و نهایتا میکُشتش!</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/news_hut/73263" target="_blank">📅 11:31 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73262">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/73262" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/news_hut/73262" target="_blank">📅 11:31 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73261">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ivZNOOcw4-QqUJ56b5pICbZEBFaPUQgQ1oiHIBbGXdJFV9vppfocuw6LfHgpie3WZRdLm1tbeu6MuMmtRlfh5UbzRcHEihIkOVLXxqbulNg9_iBDqBJy6x4oce_FLs1R2JXtDKKXGBbQ8rwUZ3vhStNt-5qOp2KzXrywxkbA4KllouHfVxFskHryFbAbr_NIcK_DYPbqRGxrWmKErfG0_7fHmjO2xqW9Pf9ZBMwzSzLwiT1BfV-dOnuP3vxmoraaVWMU5jDKu90aUsQ2ABmitOrPvW7BW-6Jhwh5fqFOwu3gUJlZmQs6fQPICE8lZ2Sm4DnnZuhvNOC-USN1gwBI6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین المللی
TrexBet
لیورپول
🆚
لاسک
فنرباغچه
🆚
استون ویلا
دورتموند
🆚
بودو/گلیمت
پاریسن‌ژرمن
🆚
منچستر سیتی
پورتو
🆚
رئال بتیس
رئال مادرید
🆚
رم
پرسپولیس
🆚
خیبر
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت، ووچر، کریپتوکارنسی
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/news_hut/73261" target="_blank">📅 11:31 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73260">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">استانداری هرمزگان:
دقایقی پیش یک پهپاد با یک لنج صیادی متعلق به شهرستان سیریک در محدوده بندر کلاهی برخورد کرد. بر اساس اطلاعات اولیه، در پی این حادثه سه نفر مصدوم شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/news_hut/73260" target="_blank">📅 11:12 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73259">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf6e01fafb.mp4?token=mkA53g-Z7WuUc9y7iZAkgQO0IacDxOtLOFt_dJt3Pv5qEZTdCZ_2ZlTpgXk1c1NqahEfNtafTBRy3uIQwJ_s5VT4HxBMo9zPkzkTVz7W6eLwFtFx1X5CFwSxoxz7cyARtwnw8UdBcri47HW21a4ozwd-m8baY4rti3EsDgz4X9c6UOnfGasnCbDef5OJ-u4O9D1SmTEeO3E_bW_6DkFEBQHaB4mlyfdKwH0siKUk3h5Z1YHVS0ARN1cSVeOOaHEOOx8CkLTt3AmuPjq-Qn9F0f8MSJuw5Q_KhKGu9SV--QjR6zxLjupTIgjQoIlt02Lh1gFKdScipIMpUwnA6HfG2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf6e01fafb.mp4?token=mkA53g-Z7WuUc9y7iZAkgQO0IacDxOtLOFt_dJt3Pv5qEZTdCZ_2ZlTpgXk1c1NqahEfNtafTBRy3uIQwJ_s5VT4HxBMo9zPkzkTVz7W6eLwFtFx1X5CFwSxoxz7cyARtwnw8UdBcri47HW21a4ozwd-m8baY4rti3EsDgz4X9c6UOnfGasnCbDef5OJ-u4O9D1SmTEeO3E_bW_6DkFEBQHaB4mlyfdKwH0siKUk3h5Z1YHVS0ARN1cSVeOOaHEOOx8CkLTt3AmuPjq-Qn9F0f8MSJuw5Q_KhKGu9SV--QjR6zxLjupTIgjQoIlt02Lh1gFKdScipIMpUwnA6HfG2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند وقت پیش تو مکه-عربستان، یه کفتره با گردنی شُل درحال مرگ بود؛
که گروهی از زائران رفتن بالاسرش و گفتن حیوونِ خدا داره نماز ميخونه و حسابی به وجد اومده بودن:
@News_Hut</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/news_hut/73259" target="_blank">📅 10:57 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73258">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c20d7f23a2.mp4?token=i3SeBbcZFwzBde2iCKrBklKbL5reeKZ6OoTxDmuvpClyndoLM1jegVqNrz4WhubfhGuWr8w3liGX25NOMgEKvCVw21hznW4CX6Bq7aANWKujN1Xy7DvK_xR--ROlBdsPe1uPwBo0IDIsL350OezQWQCpTu1XKDJnaVQFLCknXllTky7ijQON1J-V253C5iM472ocICi1L4U0A-sA4EWhQLqi8vpKuxardp7kjmgFPFAYpRhzMNTch1BviSDMSUmiAGc7Yin9u4TPt2GLp8pnw_jwHJ5peNd-EiPIerVRk_Oit8jx3Y_1eeW_SkIxgdEhOCgYMsUs23q1QIEkuQy_yQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c20d7f23a2.mp4?token=i3SeBbcZFwzBde2iCKrBklKbL5reeKZ6OoTxDmuvpClyndoLM1jegVqNrz4WhubfhGuWr8w3liGX25NOMgEKvCVw21hznW4CX6Bq7aANWKujN1Xy7DvK_xR--ROlBdsPe1uPwBo0IDIsL350OezQWQCpTu1XKDJnaVQFLCknXllTky7ijQON1J-V253C5iM472ocICi1L4U0A-sA4EWhQLqi8vpKuxardp7kjmgFPFAYpRhzMNTch1BviSDMSUmiAGc7Yin9u4TPt2GLp8pnw_jwHJ5peNd-EiPIerVRk_Oit8jx3Y_1eeW_SkIxgdEhOCgYMsUs23q1QIEkuQy_yQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این کلیپ شاهکار از کنسرت چند تا پسر توی خوابگاه دانشجویی، فقط توی چند ساعت میلیونی بازدید خورده:
@News_Hut</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/news_hut/73258" target="_blank">📅 10:29 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73257">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qPn_ZbvZY5rXdq4fkdKESYLWgMpfaa9VoPCpz3uvteQehWa59b74VoUKwiGaV-43e29o6Mqe3H9sbSqVXyjZECjkEtfYZQW6cnsxA1fKbSPOnSyKD4KrUN-0yaTTrTQ-5b0fDvlgRwWmzNO8nUuS7htzhHnBJ7Jztj73TUFvHEcDFOeG7Ojx_jGmHzwTe8pKkUMN-kI74CMEuximGKCpeW-WfTdLDHs4XhCWxt4gjRraAYySFqp3aL32BUdRx9ISDsKq0U51N4AoXd2s_4ozMN-cIYgh3OavIYo27hJx50sp451WKyozYPfVQidYe-fOc1iAIvkU2Jt1Z_OFHdmreA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رصد ۱۰۵ هواپیمای نظامی در منطقه طی ۲۴ ساعت گذشته
۱۰ هواپیمای ترابری ورودی از خارج منطقه:
فرانسه: ۳ فروند
آمریکا: ۳ فروند
بریتانیا: ۲ فروند
عراق: ۱ فروند
کویت: ۱ فروند
۸ فروند هواپیمای ترابری نظامی منطقه‌ای
۴۵ فروند هواپیمای سوخت‌رسان
۷ فروند هواپیمای جاسوسی و شناسایی
۳۴ فروند هواپیمای ترابری نظامی که در داخل منطقه جابه‌جا شده‌اند
۱ فروند بالگرد نظامی
مجموع: ۱۰۵ هواپیمای نظامی در ۲۴ ساعت گذشته.
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/73257" target="_blank">📅 09:49 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73256">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a8ff56bcd.mp4?token=m10YpRDQxIUJX1_r3EWCqclMNXxqhGmqYIybu_zLDOdGYKICeP9H5Hcu_aLINeWHnNSnTblmWX8DSTdH4WK8HwsAHIxfPjcGO-oEiZPf8RR3LEjZXhYUDyvYGZTL-4cyN3aOVBJZmaakzzQ-8BSpn6s3q5KPjCxpiAncqjTleTbvQWAz36efPM866LzKy0bOECkqpSqTVNXFwjvTBARgrT8Q_h8lWlA7JJYXi2fRjRe8gZv49mLh_2Dl_J2YZJpTT301QTSXZJm79Ba6MXlhM9BeorTD7XNZSpDH67ruMQZ12s1aoYF0drJ2-HNJ5SV2rSvE2cL-GsdaLXJtdq85Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a8ff56bcd.mp4?token=m10YpRDQxIUJX1_r3EWCqclMNXxqhGmqYIybu_zLDOdGYKICeP9H5Hcu_aLINeWHnNSnTblmWX8DSTdH4WK8HwsAHIxfPjcGO-oEiZPf8RR3LEjZXhYUDyvYGZTL-4cyN3aOVBJZmaakzzQ-8BSpn6s3q5KPjCxpiAncqjTleTbvQWAz36efPM866LzKy0bOECkqpSqTVNXFwjvTBARgrT8Q_h8lWlA7JJYXi2fRjRe8gZv49mLh_2Dl_J2YZJpTT301QTSXZJm79Ba6MXlhM9BeorTD7XNZSpDH67ruMQZ12s1aoYF0drJ2-HNJ5SV2rSvE2cL-GsdaLXJtdq85Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو درباره ایران:
این رژیمی متعصب است. تا زمانی که پابرجا بماند، برای احیای خود تلاش خواهد کرد.
تلاش خواهد کرد برنامه هسته‌ای‌اش را از سر بگیرد؛ دوباره برای نابودی ما، و بازسازی حزب‌الله و حماس تلاش خواهد کرد.
برای نابودی کامل این تشکیلات، باید این رژیم را سرنگون کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/73256" target="_blank">📅 09:40 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73255">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc5f754c70.mp4?token=hYSvOUPiZdC6psz7X26Djlc2CjA-Wxzoaa76yl6wLMG_kEg2J7CUbx74C0CSLJtXyMoUpG2qjhe9Pgqud-VojdocHK3IvU3yt5UhQR2NdZtH-a72g1e4ImuMuEFx8ofaCaa17Wf5gGyhjdX4Fh6ilicChgdiVYDxZ2wC40gOENRTsyzm3-CNm0nNdq5TrQG3EKvC0vGi574W4fhcoTTuy5Xec7LCZaYzVxk57_DTRYZm5sJVSpA208a-9qnUz_yC0DJ0_7NOl4IjI19TI44gCx1X1XLhMNHPV9nATnrXTnbS-7Onb6h6yzbJ1qWUdvrNLLaCEJ4Wpmov0vfpy3-U_VGv7MgXdxx_hEVCwlCYiDQzqK3GwB4LxB1MM0jp48y8KT3XdqMABSwqDIX0rIQhqEUrDqySIWBKfBbJEXTDe4zL_E0mvRI3o8tpiGgbVtd-BJkxNIcGmAzVi7AH9pUzYefKrKcjQHI4PwFPYJ_0J5BBA9OdZsaFz2maR-fPDxNi8cSg0lkhpFb1IPyyiK06CYZDyUhzcyVig_9aqkvzSq-Kqs41O1ehx6TYYLAHPFGnbDvy6pA76hiPk_ghCFT5Uzw6Xx7c1k8AcVBB8W_iC9t6w3d2xwoNaIzKj-ny7p4WUyxO7GeuBEutv3cYd4XjH-LM-1nbUCkO1q3VtbWxvvY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc5f754c70.mp4?token=hYSvOUPiZdC6psz7X26Djlc2CjA-Wxzoaa76yl6wLMG_kEg2J7CUbx74C0CSLJtXyMoUpG2qjhe9Pgqud-VojdocHK3IvU3yt5UhQR2NdZtH-a72g1e4ImuMuEFx8ofaCaa17Wf5gGyhjdX4Fh6ilicChgdiVYDxZ2wC40gOENRTsyzm3-CNm0nNdq5TrQG3EKvC0vGi574W4fhcoTTuy5Xec7LCZaYzVxk57_DTRYZm5sJVSpA208a-9qnUz_yC0DJ0_7NOl4IjI19TI44gCx1X1XLhMNHPV9nATnrXTnbS-7Onb6h6yzbJ1qWUdvrNLLaCEJ4Wpmov0vfpy3-U_VGv7MgXdxx_hEVCwlCYiDQzqK3GwB4LxB1MM0jp48y8KT3XdqMABSwqDIX0rIQhqEUrDqySIWBKfBbJEXTDe4zL_E0mvRI3o8tpiGgbVtd-BJkxNIcGmAzVi7AH9pUzYefKrKcjQHI4PwFPYJ_0J5BBA9OdZsaFz2maR-fPDxNi8cSg0lkhpFb1IPyyiK06CYZDyUhzcyVig_9aqkvzSq-Kqs41O1ehx6TYYLAHPFGnbDvy6pA76hiPk_ghCFT5Uzw6Xx7c1k8AcVBB8W_iC9t6w3d2xwoNaIzKj-ny7p4WUyxO7GeuBEutv3cYd4XjH-LM-1nbUCkO1q3VtbWxvvY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوووری
؛پرزیدنت ترامپ درباره ایران صبر کنید تا ببینید با ایران چه می‌کنیم. کارشان را خواهیم ساخت؛ صبر کنید تا ببینید. آن‌ها هم فقط منتظرند.
صبر کنید تا ببینید با ایران چه می‌کنیم، چون دیگر کاسه صبرمان لبریز شده است. می‌دانید، دیگر به آخر خط رسیده‌ایم.
اما خب، این‌ها اهمیتی ندارد. مسئله مهم این است که قرار نبود آن‌ها سلاح هسته‌ای داشته باشند و نخواهند داشت؛ این موضوع زیر هزاران تن سنگ دفن شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/73255" target="_blank">📅 09:12 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73254">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a1adb1098.mp4?token=h7PKOfOYoOCCBBcU5fsnUJrSUBvJXwM7nHgy9LvCOMngEzePDIhPQiZe14pJyidfmgsaCs5MRptbx77bCABKcIo-2RoJp5ZA9eNH0IghGnWncovm4tkQO7demWZD4meRH3P8KbtnMjZG-KmRgqBkr0TuqNxy71zk5DDAIIQ2Bj7q93Z3jQend4FngR21KxnkHPuGxrZq5BGcUmFlOggi2-HgJ4e4Wg93xALJEMjVrzdI6zcD-BNW8etvPWyxfBP6-z-OFcXJGI3qoDRkEJpIYSSzwL_qCyzHQfYGljTNjUU5QrIDPnZ9ZB-r6kfKiHj7WC_uFRji1Y6ICjfIdyQCkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a1adb1098.mp4?token=h7PKOfOYoOCCBBcU5fsnUJrSUBvJXwM7nHgy9LvCOMngEzePDIhPQiZe14pJyidfmgsaCs5MRptbx77bCABKcIo-2RoJp5ZA9eNH0IghGnWncovm4tkQO7demWZD4meRH3P8KbtnMjZG-KmRgqBkr0TuqNxy71zk5DDAIIQ2Bj7q93Z3jQend4FngR21KxnkHPuGxrZq5BGcUmFlOggi2-HgJ4e4Wg93xALJEMjVrzdI6zcD-BNW8etvPWyxfBP6-z-OFcXJGI3qoDRkEJpIYSSzwL_qCyzHQfYGljTNjUU5QrIDPnZ9ZB-r6kfKiHj7WC_uFRji1Y6ICjfIdyQCkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تولیت آستان قدس رضوی:
توفیق اقامه نماز با رهبر انقلاب را داشته‌ام؛ حال ایشان بسیار خوب بود
رهبر انقلاب پیش و پس از تدفین رهبر شهید در مشهد حضور داشتند
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/73254" target="_blank">📅 09:00 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73253">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب :)
😊
😂
میگی نه؟ بیا تو چنلمون و ببین!
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/73253" target="_blank">📅 01:52 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73252">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KbZTe0tADKDZHnRz16yGi3KOj9OU73psdbA8gHfEepfo8RJJ7THTVR6TX1gRQagLsA_4LHtjLG7lwuTs9_syJduE3z64lvITtrvDLmoT5JhXdiYeZtxvBO4AWgKfwmOFuuBA5KkLJFrCbjFkwu9bbrPTw8bN9pB5Bas6yhHKVZ4GF6RbtImyUx1e2pSoyQiceZPFg8EXf_wFdV0MEcvADar5nzHa09oUN65w4Z-s-YjInr0SlJliF42rh3NUbgqLTVlfaVOSrNT8MdhZcPDANCIPQPLJ98yJIGozqXQ-hxWPq_Fnmb0JrvdrArJ7WTj6JpDJ6kHNibiMXvQjpV81iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب :)
😊
😂
میگی نه؟ بیا تو چنلمون و ببین!
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/73252" target="_blank">📅 01:52 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73251">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">حوثی‌ها به مقر شرکت «آرامکو» عربستان در ظهران حمله کردند؛ این اقدام ساعاتی پس از آن صورت گرفت که آن‌ها به‌طور علنی این مکان را به عنوان هدف تلافی‌جویانه معرفی کرده بودند.
وزارت انرژی عربستان تأیید کرد که یکی از ساختمان‌های اداری در مجتمع آرامکو در ظهران هدف قرار گرفته و منجر به وقوع «آتش‌سوزی محدود» شده است؛ این حادثه تلفات جانی در پی نداشت.
خبرگزاری رویترز از شنیده شدن صدای انفجارهای مهیب در نزدیکی این مقر، وقوع آتش‌سوزی و صدور دستور تخلیه خبر داد و اعلام کرد که به کارکنان گفته شده است روز بعد از خانه کار کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/73251" target="_blank">📅 01:30 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73250">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OvljAGjdte4WSGPjrOT5Iu88DaKju_a4mqfeyEDOpPiXi2KH4X5a9dnnMydZVozJEOgL41au1d5bfviJBuhc4hsPbQ25dm7_XR4jNBLjE7AVLMOorHPEFsOVA_61Lo-ZPzoF0AyfONbhBub3eNoiHwNYe7PfusoIvz9oyhNlwaiWrHVSpLK5JvTvZqxjaV6E__LV0oZ-Z_xyiHJ1Ja0VpAWCcLkA_bPG8Yf9hw7GDxp7CU7J3sGtak2ZC3VPhca1fOKV7DX-GaRcF0wo1sAlQez_muUWCiDI1eed3J-8ByGdiWCJpF1AWNd9FAfslVUOFs29k8ka8EI7bE4lLNm5nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ناو هواپیمابر آمریکایی «جورج اچ. دابلیو. بوش» به همراه حدود ۴۸۰۰ نفر از کارکنان خود، پس از شش ماه پشتیبانی از عملیات‌های ایالات متحده در خاورمیانه، برای یک دوره استراحت وارد پوکتِ تایلند شد.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/73250" target="_blank">📅 01:20 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73249">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">صدای دو انفجار از سمت تنگه هرمز شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/73249" target="_blank">📅 01:12 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73248">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf7e4aede4.mp4?token=XormlDmSJSk3diuhBT2N7W_441fC8NqClXlH_oph63Uwny8Ghvz2N-rU9yOHkLL6t7GNkZBmqQbqyFt5ziP6wprPLBbhOG15R08-zbm_ggp2u3IifXbv4GGs9NKq2okbNb0-BbySZWvkteLOp1zSICsURByjL_pkHmMvvn_2Vgch6mibaiec6cVcplL5tyyIWftDg5YYHvvkFKHOL-13Dnowh-g_GkU4AsFUe_IIi04onBhEHDA-Q7e_UQGqn5GBa86lCBnzDclEc60oAaACd9LzqOg14jwIt3BF9xdCpA8MjLYxtGOt3-w_RJIACInYVvn_U5Yva6hy2ZAMef93Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf7e4aede4.mp4?token=XormlDmSJSk3diuhBT2N7W_441fC8NqClXlH_oph63Uwny8Ghvz2N-rU9yOHkLL6t7GNkZBmqQbqyFt5ziP6wprPLBbhOG15R08-zbm_ggp2u3IifXbv4GGs9NKq2okbNb0-BbySZWvkteLOp1zSICsURByjL_pkHmMvvn_2Vgch6mibaiec6cVcplL5tyyIWftDg5YYHvvkFKHOL-13Dnowh-g_GkU4AsFUe_IIi04onBhEHDA-Q7e_UQGqn5GBa86lCBnzDclEc60oAaACd9LzqOg14jwIt3BF9xdCpA8MjLYxtGOt3-w_RJIACInYVvn_U5Yva6hy2ZAMef93Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امروز خاتمی داشت با عصا به سختی راه میرفت که یهو ملت شروع میکنن به تشویق کردنش که یدفعه شفا پیدا میکنه و عصا رو میذاره کنار و راحت میشینه!!
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/73248" target="_blank">📅 01:10 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73247">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de41df8bac.mp4?token=AG1zbT5w9VypfmqdtrMcOR3sYeE-dG2ulPALsr17g22o9t2PAzeVpS2mAwy0IIilZDGoFM1MwRoGByN2xu9u9oJVHIRqm4S-gR1tX2vQvCog2IBGdltebTWEUXdtuz9eEOVpBznEQhCBMg2o_jx1dlPsQGgtbrBUduSr__fNZOliVe9ffXnhRWuIPGaY9Ug8mc0_Fy_ok1VSuPnnbrdsFUAdEZuHxv_wiZWlKFmsTnxQZODC83aeBF89EyDz9XsEvxG8YxIiaYUR186WYtUCO9LR7i0RhWlAmIQPycvD1pKg44Uq-WCd5H6c2bVkVY0lnahKp3yiVP2MZdCB9q7FjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de41df8bac.mp4?token=AG1zbT5w9VypfmqdtrMcOR3sYeE-dG2ulPALsr17g22o9t2PAzeVpS2mAwy0IIilZDGoFM1MwRoGByN2xu9u9oJVHIRqm4S-gR1tX2vQvCog2IBGdltebTWEUXdtuz9eEOVpBznEQhCBMg2o_jx1dlPsQGgtbrBUduSr__fNZOliVe9ffXnhRWuIPGaY9Ug8mc0_Fy_ok1VSuPnnbrdsFUAdEZuHxv_wiZWlKFmsTnxQZODC83aeBF89EyDz9XsEvxG8YxIiaYUR186WYtUCO9LR7i0RhWlAmIQPycvD1pKg44Uq-WCd5H6c2bVkVY0lnahKp3yiVP2MZdCB9q7FjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ابوالفضل ظهره‌وند، نماینده مجلس: پیش بینی میکنم ظرف یک هفته تا ده روز آینده جنگ از سر گرفته شود.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/73247" target="_blank">📅 00:57 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73246">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lSovd1F_eB7ZnpQqh0mXfTOorg_Pqs9vBVroaYvujPxgdoI7acxHE-6jELr8buwmYOM0_HTBiwFeOVptd69IhldUlpUtdjQoffn5W63VoN0urNok-y28pPtITVaP0G5pCj6yZ3smtKeyhKi6oevUGIQ9s05Vn7jGNKpTElCsnaTKwf2sFu3-4FAqB81mIQBrsjzgwlNLEo0-GxktNC55Py4MpcMtTzUGT3axp-rvtVQX6RA_w3oX_fltwIAZ0BGxaamlyFckbaeEICRNMciWxRQXZsuYTVE94hfXgGfYqhFYaUuJRQpvLOS4p0H-ATxC1X4n5Hju0l_iZuhX9KW5Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#مهم
؛
اکسیوس به نقل از یک مقام آمریکایی:
به نظر می‌رسد «بی‌بی» (نتانیاهو) می‌خواهد دوباره دست به اقدام بزند. او چند بار در این باره با رئیس‌جمهور صحبت کرده و رئیس‌جمهور هم گفته است: «خب، می‌دانی بی‌بی، برو و آماده شو.»
اما در واقع هیچ تعهد قطعی‌ای وجود ندارد. عبارت «برو و آماده شو» ممکن است به معنای «الان»، «بعداً» یا حتی «هرگز» باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/73246" target="_blank">📅 00:32 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73245">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/15a3b1b7fc.mp4?token=Snh3-NsM0Rc2SX4wzpckWbdg-poeCEQTGFbLCkGhvhcLAYS8Wm_9rtyA09gwpQ1DNH5Ei9jVpYWWGrYJBTy25BudeI-59AyKaGdNEiXQ6CGNQSScLM2Wu0kDVallg-cmYznZnC38sVP_6UBLDtOCwDmuqaigtQasxlhw1RJxMvFhg9t_DDUEEtdoJYj0DJxrQ8vb8faBXnBuVwEDjWw4CUMvOYnbS-RMmglQiVedPkzwEjtMFACOKYtOqN1EQKzitUvNVXfuojLLXnFbo4N6F98_cypCKqSXZT90wNgShxJuIFj7BZxZufMDWiXDLmRC_NkVJAli34sOFMd3AjqTUg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/15a3b1b7fc.mp4?token=Snh3-NsM0Rc2SX4wzpckWbdg-poeCEQTGFbLCkGhvhcLAYS8Wm_9rtyA09gwpQ1DNH5Ei9jVpYWWGrYJBTy25BudeI-59AyKaGdNEiXQ6CGNQSScLM2Wu0kDVallg-cmYznZnC38sVP_6UBLDtOCwDmuqaigtQasxlhw1RJxMvFhg9t_DDUEEtdoJYj0DJxrQ8vb8faBXnBuVwEDjWw4CUMvOYnbS-RMmglQiVedPkzwEjtMFACOKYtOqN1EQKzitUvNVXfuojLLXnFbo4N6F98_cypCKqSXZT90wNgShxJuIFj7BZxZufMDWiXDLmRC_NkVJAli34sOFMd3AjqTUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دستشویی یه کافه تو بالاشهر تهران:
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/73245" target="_blank">📅 23:59 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73244">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">یک مقام آمریکایی به «اکسیوس» درباره ایران:
مذاکرات نه کاملاً مرده‌اند و نه واقعاً زنده؛
ما صرفاً در حال افزایش فشار هستیم و این باور وجود دارد که در نهایت، عقلانیت و تدبیر در آنجا پیروز خواهد شد.
ایرانی‌ها تصور می‌کردند که این رئیس‌جمهور به دلیل فشارها و انتخابات میان‌دوره‌ای عقب‌نشینی خواهد کرد؛ اما او به آن‌ها نشان داد که در اشتباه بوده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/73244" target="_blank">📅 23:16 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73243">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DC89r0yKo-uG7qGBiOFTxcjpy2ncjnNuQroMVwmdMviMgpo2tVs8HapjISnlprKHfOpuHFHUAUiLBAXAn9v7iE4PCll2DoXPX-EvBEjmqMHtZCjepSlSwm7kr-2zIWEVJaBdca2OjpYNplY6H2VrDAWIHKsThkY83_vavqcsI48UDB37fheOX3Bx-xVzUP15mvsUcBIq1pSKRDgkaUFAPsL7opT0zlwJTlU7Hua4SWqbMUEYtzvkknZPwpxrt2TYsS65uMJNp9zYis2H8O0hKEDJANQ-P0r9_IzcTGOJGNObppUCgPgDOGyERe0AUiBJQcImA7EHHfCMkoap5QFHhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان دریایی تجاری بریتانیا (UKMTO) گزارش داد که یک کشتی باری امروز در تنگه هرمز مورد اصابت یک پرتابه قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/73243" target="_blank">📅 23:14 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73242">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6d007bae0.mp4?token=hd_ReR1_0OlHDa6pS_ZhpfQok7gNq5Lpw4fShb0Tnr0rbHG8BwhGCwhaaq0OONuUpHZ5GksFkYYa5jWdoh2Ag1iQteOJ4lCB2AY1rvDTgkm66q_LreRoJl_JaDcgzMuCSfM64Un-ZqnaHwtOSAdXn49J8ldpZy3lvThLS6NxcKy-Y2Pk9bpTVojTW1NhGVWS95HCdFhHdUomtXlWoNXTf2h0yqB78wYGa6534n_pjTnBVsEiUB-V7V_etK7GGiH-bBnF4j5MEWmfuBViZoC78PiRijL8CLWTerFElpro_G9uXI7xyCNy8Fh_FgC8k1XfnD-jJzNeWhl4CJj49KEY_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6d007bae0.mp4?token=hd_ReR1_0OlHDa6pS_ZhpfQok7gNq5Lpw4fShb0Tnr0rbHG8BwhGCwhaaq0OONuUpHZ5GksFkYYa5jWdoh2Ag1iQteOJ4lCB2AY1rvDTgkm66q_LreRoJl_JaDcgzMuCSfM64Un-ZqnaHwtOSAdXn49J8ldpZy3lvThLS6NxcKy-Y2Pk9bpTVojTW1NhGVWS95HCdFhHdUomtXlWoNXTf2h0yqB78wYGa6534n_pjTnBVsEiUB-V7V_etK7GGiH-bBnF4j5MEWmfuBViZoC78PiRijL8CLWTerFElpro_G9uXI7xyCNy8Fh_FgC8k1XfnD-jJzNeWhl4CJj49KEY_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار رکنا از سخنگوی شهرداری تهران پرسید: چرا در تهران در تمام ساعات
روز ترافیک سنگین وجود دارد؟
محمدخانی در پاسخ: «اینطور نیست، مثلا ساعت ۳ نصفه‌شب که ترافیک نیست!»
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/73242" target="_blank">📅 23:01 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73241">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26766391a1.mp4?token=egW5bQ4V0y9y-E1iqeY2ymBGHD9StMQ5O7b1npYkGoZfaqTEqVT0w729inc-3XcsmlgVczW6HKK0Pv9MHHKbdv4mzr8dwGlRucDUjLKrtm9MyeTrDzYUEbZu-TpChYGjOi1eXsv7g4d53AeK75JiklY6cT9c6q794GNS02G57ou-rlbpgI7SzaIWfQU4d3k4Bo5O4kcI5D4-iYTWD_aU4OTiLpGsawdbQb0CiL9We2o7UorFYu2CFFI1rdZuUDhgiuaT-dVJrlZrug50F_C1yfImT_mmy9fw32jfK3xcb6jU4YyhyRxn5nIfc82liR6WSZ_klJLNZxQseyRdjoiy0oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26766391a1.mp4?token=egW5bQ4V0y9y-E1iqeY2ymBGHD9StMQ5O7b1npYkGoZfaqTEqVT0w729inc-3XcsmlgVczW6HKK0Pv9MHHKbdv4mzr8dwGlRucDUjLKrtm9MyeTrDzYUEbZu-TpChYGjOi1eXsv7g4d53AeK75JiklY6cT9c6q794GNS02G57ou-rlbpgI7SzaIWfQU4d3k4Bo5O4kcI5D4-iYTWD_aU4OTiLpGsawdbQb0CiL9We2o7UorFYu2CFFI1rdZuUDhgiuaT-dVJrlZrug50F_C1yfImT_mmy9fw32jfK3xcb6jU4YyhyRxn5nIfc82liR6WSZ_klJLNZxQseyRdjoiy0oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تجمع عرازشه در مقابل منزل حسن روحانی و شعار بر علیه او:
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/73241" target="_blank">📅 22:15 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73240">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6568459aaf.mp4?token=oAb709mQ6FBug0iSUQqNZqPlOuMDiflJnIEmFpW7mlPQgl6nKeX5dQE84QdpcQOBTxTm6tOvLWH1P5S3SDk33PuRGz16oGrPe2j1FeumwTZez0RNjweKWpswEEQJaore5J2UP5gzkB92WNNrv9hAikxINWPANtPaZrjGuV5ixOiApU8oy_Qv9A7pCagEgWqk4caWX2js2V1iXSB-zvEU2e8KIf2lQy6FZ6zUK570pRhlKjq5YPXnY6MdP4VLPMeQONpELiFFHqErqfEmTH_6_3Hu8Nn70OLEx5803lLjewreDUfPdCYuon5mJejZtJIjw3cI41sM-xR7SqPI40Lsdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6568459aaf.mp4?token=oAb709mQ6FBug0iSUQqNZqPlOuMDiflJnIEmFpW7mlPQgl6nKeX5dQE84QdpcQOBTxTm6tOvLWH1P5S3SDk33PuRGz16oGrPe2j1FeumwTZez0RNjweKWpswEEQJaore5J2UP5gzkB92WNNrv9hAikxINWPANtPaZrjGuV5ixOiApU8oy_Qv9A7pCagEgWqk4caWX2js2V1iXSB-zvEU2e8KIf2lQy6FZ6zUK570pRhlKjq5YPXnY6MdP4VLPMeQONpELiFFHqErqfEmTH_6_3Hu8Nn70OLEx5803lLjewreDUfPdCYuon5mJejZtJIjw3cI41sM-xR7SqPI40Lsdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت سرویس بهداشتی یه مدرسه پسرونه در تهران!!
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/73240" target="_blank">📅 21:34 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73239">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g-oQBpyhS0_eKmmeLfYgo2E_UM0RezNOAER_WvK4Lo8DpukEZxa3KWAerQ8QFnNImpqvJfaXJ9lfR_KS0lMXRDKmLdM9c58jZQMZO9reC_sU7kV8AX-zVtEXoj9dfLfdOChYT18kchS9br3jvt2tMe0j3OooiyAsUVNuJWP2vt1T9XZGs38xZnIz6zhl7cHv2-jTja7kEQhWLOw834ra3802ow_zBRXlw5-MJI4luqFNFxq63jH_69OVtbQGd42OXiXZkldTLsvyP77-FLIbukF6-DxAz419yXRxsPQy7Zwh4HpcoaN9Wo1Q1w3VTq-JQVBgJ6Q63TqR3l8HkMab_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
؛به گزارش شبکه ۱۲ اسرائیل، بنیامین نتانیاهو، نخست‌وزیر اسرائیل، طی دو هفته گذشته گفتگوهای متعددی با دونالد ترامپ، رئیس‌جمهور آمریکا، درباره آغاز یک عملیات نظامی مشترک جدید علیه ایران داشته است؛ عملیاتی که احتمالاً پیش از انتخابات ۲۷ اکتبر اسرائیل و انتخابات میان‌دوره‌ای ۳ نوامبر آمریکا انجام خواهد شد.
نتانیاهو با ابراز نگرانی نسبت به تلاش‌های ایران برای ازسرگیری فعالیت‌ها در تمامی بخش‌های برنامه هسته‌ای خود، این تحولات را توجیه‌کننده‌ی انجام حملات مجدد علیه تأسیسات نظامی و هسته‌ای ایران دانست.
یک مقام آمریکایی اظهار داشت که ترامپ به نتانیاهو گفته است «اقدام کند و آماده شود»، اما تعهد قطعی نداده است؛ در همین حال، مقام دیگری گفت که موضع رئیس‌جمهور همچنان در حال تغییر است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/73239" target="_blank">📅 20:59 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73238">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">حوثی‌ها (انصارالله) اعلام کردند که عربستان سعودی طی ۲۴ ساعت گذشته ۱۰۴ حمله هوایی و موشکی علیه صنعا و استان‌های ذمار، تعز، عمران، لحج، الجوف، مأرب، صعده و الحدیده انجام داده که منجر به تلفات غیرنظامی شده است.
این حملات توسط جنگنده‌های اف-۱۵ و تایفون که از پایگاه‌های هوایی «خمیس مشیط» و «طائف» برخاسته بودند، و همچنین با شلیک موشک از «نجران» صورت گرفت؛ امری که مجموع حملات ادعایی ائتلاف به رهبری عربستان را به ۲۲۸۱ مورد می‌رساند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/73238" target="_blank">📅 20:15 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73237">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sJUz52oqBBZ_ZQWHG2iE32L5m3n-9NNuxfFd4JhSL45aFWUhbPOlQPZI8ofSgTPVewUW7K6q8NjAcSFGEE6qngfFkFq5FFgWud2DNzKn8bJWBT_hkeyT2oinCLQB9AmvkbaMVbATzX1bYYAE84TWrNDw3Kmok54aGI6HEZVYUyjFmGSfXvgPGm02eq3DO2Dw0OjDax4WgbF8r2VvUi0bbS7gNEj24HSwb7vNCBRIdYqHrzvZ3OORvwByYje3pdgvgVEQvoXUpqqzoNb55RZDTyrpF5acxhTCerufpCjHaFipEE4UhNEdwM0Z4D2cCh1fWT8v-vz421vrVrBcac1uig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#مهم
؛ترامپ در تروث سوشال:
«حوثی‌ها رفتار خیلی بدی دارن. فکر می‌کردم یه سال پیش، وقتی حسابی بمبارونشون کردیم و به درخواست خودشون حملات رو متوقف کردیم، درسشون رو گرفته باشن.
اونا مدت زیادی سکوت کرده بودن، اما حالا دوباره ظاهر شدن؛ احتمالاً به دستور ایران که یه کشور در حال فروپاشیه، نیروی دریایی نداره، نیروی هوایی نداره، بدترین اقتصاد دنیا رو داره و تورمش به ۳۰۱ درصد رسیده.
اونا به شکل خیلی بدی به عربستان سعودی حمله می‌کنن و عمداً سعی دارن قیمت نفت رو بالا ببرن؛ احتمالاً هم قبل از انتخابات آمریکا. این اصلاً قابل‌قبول نیست!
یکی باید بهشون توضیح بده که من دیگه نامزد انتخابات نیستم؛
من قبلاً با اختلافی بسیار زیاد پیروز شدم!
اما بعد از انتخابات دوباره وارد ماجرا می‌شم و این اتفاق رو هیچ‌وقت فراموش نمی‌کنم!»
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/73237" target="_blank">📅 19:41 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73236">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb0e101b64.mp4?token=GADSdIwg-9koaTcDPiuiR4h49yYD5tKNaDSNhZPpdCNBtfJPY1nOS0gB3ulvlYNwQPCgJOZblXcsjaCdMxvhyKt3UFoRp9plCGX5ElMkNqiqZFJS82pCcDiQ7NPJFeSUS7ZHXS4MI03Ykl5lWMqktWeeuE6M2FKyiPOc7APdMx9rZBA8ABJrgsbOD_OhLx-lnkU_A6fVPtdSExNljRhwA-0XB_rLW7b1cFaxuqWr6arqZ4maaeWFTRRInPC2VzQbKBDYujkP32bXfcBzo_EWxJx1g75Gy4FasClXC2zrQA1RNAdxq78xnMiNzCpSY9M6UvgrM1wMxUlfE0Q8SIzAyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb0e101b64.mp4?token=GADSdIwg-9koaTcDPiuiR4h49yYD5tKNaDSNhZPpdCNBtfJPY1nOS0gB3ulvlYNwQPCgJOZblXcsjaCdMxvhyKt3UFoRp9plCGX5ElMkNqiqZFJS82pCcDiQ7NPJFeSUS7ZHXS4MI03Ykl5lWMqktWeeuE6M2FKyiPOc7APdMx9rZBA8ABJrgsbOD_OhLx-lnkU_A6fVPtdSExNljRhwA-0XB_rLW7b1cFaxuqWr6arqZ4maaeWFTRRInPC2VzQbKBDYujkP32bXfcBzo_EWxJx1g75Gy4FasClXC2zrQA1RNAdxq78xnMiNzCpSY9M6UvgrM1wMxUlfE0Q8SIzAyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ خبرنگاری رو که همیشه درباره وضعیت ایران سؤال می‌پرسه، مسخره کرد:
ترامپ:
«ایران؟ باز هم ایران؟ همیشه ایران!»
«ایران یه کشور شکست‌خورده‌ست. هیچ اقتصادی نداره، تورمش ۳۰۰ درصده، پولی نداره و حقوق نیروهاش رو هم نمی‌ده؛ نه به نیروهاش، نه به هیچ‌کس دیگه‌ای پول نمی‌ده.
خیلی زود درباره ایران تصمیم می‌گیریم.
ما تنگه هرمز رو کنترل می‌کنیم و نفت زیادی هم از این تنگه خارج می‌شه.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/73236" target="_blank">📅 19:33 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73235">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2628e9cb18.mp4?token=AHpTpHln_aK14cWzxbvu1-oYl2dv-Gw-3dy9KCYnnVMhK6ICs_19z3-borXs4TYHR3q0WV4t05zyqBkeBTKOjOE27aNOrD1_wln1as6zc_UrfqxI8guaoE6x470kyQXt_0f1p7lJRslgBcahQCyJGYXZ3CB2a0Whl9TZRoG61Av6T0xRDXpqcE9RyS0MVOlsBgMblwUUEnfY4iEjNp-JG9huEh1vAlQ-6kombv8CHX_tZWJpdKzdGELVBuD0u8lnqdlQdZsor7XvxaJmW8PlZX-RlebJ6m5XFFxLxV20SMYuj78i7dgBdW7GEPTJwZRqv_5fMt4C5MrmTFJznIrybQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2628e9cb18.mp4?token=AHpTpHln_aK14cWzxbvu1-oYl2dv-Gw-3dy9KCYnnVMhK6ICs_19z3-borXs4TYHR3q0WV4t05zyqBkeBTKOjOE27aNOrD1_wln1as6zc_UrfqxI8guaoE6x470kyQXt_0f1p7lJRslgBcahQCyJGYXZ3CB2a0Whl9TZRoG61Av6T0xRDXpqcE9RyS0MVOlsBgMblwUUEnfY4iEjNp-JG9huEh1vAlQ-6kombv8CHX_tZWJpdKzdGELVBuD0u8lnqdlQdZsor7XvxaJmW8PlZX-RlebJ6m5XFFxLxV20SMYuj78i7dgBdW7GEPTJwZRqv_5fMt4C5MrmTFJznIrybQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سوال: آیا از ترکیه می‌خواید که در واکنش به اقدامات یمن ملحق بشه؟
ترامپ: «ممکنه این کار رو بکنم. اردوغان دوست خیلی خوب منه و احترام زیادی براش قائلم.»
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/73235" target="_blank">📅 19:30 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73234">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7fdc0493f.mp4?token=jJhP3280DJhjMckL5Lwj_3hhS9-34isSQ5e9l1lx8JFy1u1qHP1E8F45zMxRlAkKX5euqFI4ZjvaLm4aqtxP5lvt6RvzuGIjhyx1G3kNfLz6ls71KyLgIlvsuxVToJ2UkHwkYpxeLxaKN0rSX2RG4S0qSETul2NuL0pzeCX1kDBca92IGZoLm91rM1RW-Fq9UV-B2K4P2LjxUpqCZLiRz8-VJDV8MhJfr8XgQ8aoHartq7X8cJ0fh5cHMm2SXiBKFcpRpQObWIdYEgPlMX7iOAiiMhpMY8o6tRl-jMlqcBKlweQNr720JOhrs971dwiFUapb6THJk4qBpzVpOqICSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7fdc0493f.mp4?token=jJhP3280DJhjMckL5Lwj_3hhS9-34isSQ5e9l1lx8JFy1u1qHP1E8F45zMxRlAkKX5euqFI4ZjvaLm4aqtxP5lvt6RvzuGIjhyx1G3kNfLz6ls71KyLgIlvsuxVToJ2UkHwkYpxeLxaKN0rSX2RG4S0qSETul2NuL0pzeCX1kDBca92IGZoLm91rM1RW-Fq9UV-B2K4P2LjxUpqCZLiRz8-VJDV8MhJfr8XgQ8aoHartq7X8cJ0fh5cHMm2SXiBKFcpRpQObWIdYEgPlMX7iOAiiMhpMY8o6tRl-jMlqcBKlweQNr720JOhrs971dwiFUapb6THJk4qBpzVpOqICSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در پاسخ به این سؤال که آیا حوثی‌ها رو هدف حمله قرار می‌ده:
ترامپ: «اونا خیلی بد رفتار می‌کنن. اگه بهتون بگم تصمیمم رو گرفتم، اون‌وقت... حوثی‌ها واقعاً خیلی بد رفتار کردن.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/73234" target="_blank">📅 19:25 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73233">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bae90f7f46.mp4?token=pCM3-iZAuwj5jpIj75eShBEJQyPDcs_dwhq5My-2UINugw5EHNwWi2DeH6uSU4iKVGD8bQaF3maeTfTXs_QJhUUvAT3Mo1DzFfBfNIrYQJsBNGwFfvAEkEb3MYb87fSDWpCjHTL4kBxoGeMMQdKNAG0xhIvWpndp1qc9hJ-GJ-LhGTL_6UEceNMUYDvb1LzBhZfP2qUyRCAFakAEfDI8cRHkJbEo6pgAA80hDaejd87FaJPDjusOuYFv5x8b_lV28zE95o-itnoM4_cnwGS6Dc5zgoN4WXz93VWOK8R1ITHwLI_PHJFWS_q6k5vFsLCqPlb5z_bc4qQ1TviAj8kBGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bae90f7f46.mp4?token=pCM3-iZAuwj5jpIj75eShBEJQyPDcs_dwhq5My-2UINugw5EHNwWi2DeH6uSU4iKVGD8bQaF3maeTfTXs_QJhUUvAT3Mo1DzFfBfNIrYQJsBNGwFfvAEkEb3MYb87fSDWpCjHTL4kBxoGeMMQdKNAG0xhIvWpndp1qc9hJ-GJ-LhGTL_6UEceNMUYDvb1LzBhZfP2qUyRCAFakAEfDI8cRHkJbEo6pgAA80hDaejd87FaJPDjusOuYFv5x8b_lV28zE95o-itnoM4_cnwGS6Dc5zgoN4WXz93VWOK8R1ITHwLI_PHJFWS_q6k5vFsLCqPlb5z_bc4qQ1TviAj8kBGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیتر دوسی، خبرنگار فاکس‌نیوز: «اشتراک‌گذاری اطلاعات و داده‌های اطلاعاتی با اوکراین رو متوقف کردیم؟»
ترامپ: «نه، متوقف نکردیم. ما بهشون کمک می‌کنیم و واقعاً داریم کمک می‌کنیم که به یه نتیجه نهایی برسن. پیتر، ما می‌خوایم جنگ تموم بشه. داریم بهشون کمک می‌کنیم و اطلاعات هم در اختیارشون می‌ذاریم. می‌خوایم جنگ تموم بشه؛ برای همین با اوکراین و روسیه همکاری می‌کنیم تا به این جنگ پایان بدیم.»
این جنگ بی‌فایده‌ست و باید تموم بشه!
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/73233" target="_blank">📅 19:17 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73232">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3fc7b7be7c.mp4?token=OZLiQCs3uEWLSdC1qNK3DcY7f8ZR3vIs913eW0HeL40nFAi8KsMGuAk66EyeCOOzofTbjGQjJV2ure292O3Bb4x86-KakBOl9Q8wXOSSYJNJJKR25wYmq4KV-uWMOG7mtzeLTbCc2wMvKq-fYcuIoXs4UXfZXlVdrIQK-hJ2nL27ebDkGndHDskuzzHaYJsbb0D5gNw4fMDFAglYfKssEsAx80L5NvpDWeHDlTRcEmgZGGdCkLBoMTqCsPXSq2IZzTDYmfgPrpoc_bLEhE3fpY4jJ1p6jzDG5cuUWxl8BLSy8jGeDUoUav3qy6OXhuNQ1lcXo7s5RkG-kXzAXP5jvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3fc7b7be7c.mp4?token=OZLiQCs3uEWLSdC1qNK3DcY7f8ZR3vIs913eW0HeL40nFAi8KsMGuAk66EyeCOOzofTbjGQjJV2ure292O3Bb4x86-KakBOl9Q8wXOSSYJNJJKR25wYmq4KV-uWMOG7mtzeLTbCc2wMvKq-fYcuIoXs4UXfZXlVdrIQK-hJ2nL27ebDkGndHDskuzzHaYJsbb0D5gNw4fMDFAglYfKssEsAx80L5NvpDWeHDlTRcEmgZGGdCkLBoMTqCsPXSq2IZzTDYmfgPrpoc_bLEhE3fpY4jJ1p6jzDG5cuUWxl8BLSy8jGeDUoUav3qy6OXhuNQ1lcXo7s5RkG-kXzAXP5jvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در پی حملات هوایی نیروی هوایی سلطنتی عربستان سعودی، مخازن سوخت در بندر الحدیده یمن (تحت کنترل انصارالله) دچار آتش‌سوزی شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/73232" target="_blank">📅 18:56 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73230">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3237ca4f82.mp4?token=TLGarE61Y5iB-vdFe1Qg5aEsYa41SGaxymj-nUT6ZwQ3xKgpbrtVGrJLi3BdyJuTEDNeGrZmywx5MWaFfF6V00CKEQ3s34FL-implF3Qbby7F95DdsMmje81RYYNlluoLPQT6JQi8N3MWgj3Z2L0eBnvpZ0sgySt87Pthm5x9a348emovLWXqlZp8bjctZCbo7waKSbWNxs-l3iPizGNs4OBOIfrfKCR5GMujZW_okCfgPaAaB-q5OY5QTHX6_if3DjE_-cCYRcKEt1LcAXu7Xo3gWF1dsuweDgBg7m641VKDynRz4BOVrc0pdLOFh6nKZkRYEYm2x_m0DjMUKtOGRMYi9eAeVIAEuA069T9gqZOkfRcUohwPI9_lQD9xvvEeXUhqXOBRaDvHTyvRxQbdU_lMNCuNRqeypmTihc0g2nL1qBBJtztlev1rbKLBFVuhu8A77tqP4y23l2mSvUiUpLDLALmdIILI_nXzwave7mWgB8mff-8McVr3x1R6Yam7zyYOqIo8M4eoADZ4qrJ5WxEJZ_rhsGPGwXYKdPvKORmSFslSc69A5XtVeVa8SIF3z6ktsQAWHKd8_5Q5X8taE_g4XsXUo56hrge9gRSQc46uyCOTDZTdeHqG6wLOnWJ1tjDaMI7JNgLbfZ4Rqc-lYDKsB93stkmMeuXtdWROm4" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3237ca4f82.mp4?token=TLGarE61Y5iB-vdFe1Qg5aEsYa41SGaxymj-nUT6ZwQ3xKgpbrtVGrJLi3BdyJuTEDNeGrZmywx5MWaFfF6V00CKEQ3s34FL-implF3Qbby7F95DdsMmje81RYYNlluoLPQT6JQi8N3MWgj3Z2L0eBnvpZ0sgySt87Pthm5x9a348emovLWXqlZp8bjctZCbo7waKSbWNxs-l3iPizGNs4OBOIfrfKCR5GMujZW_okCfgPaAaB-q5OY5QTHX6_if3DjE_-cCYRcKEt1LcAXu7Xo3gWF1dsuweDgBg7m641VKDynRz4BOVrc0pdLOFh6nKZkRYEYm2x_m0DjMUKtOGRMYi9eAeVIAEuA069T9gqZOkfRcUohwPI9_lQD9xvvEeXUhqXOBRaDvHTyvRxQbdU_lMNCuNRqeypmTihc0g2nL1qBBJtztlev1rbKLBFVuhu8A77tqP4y23l2mSvUiUpLDLALmdIILI_nXzwave7mWgB8mff-8McVr3x1R6Yam7zyYOqIo8M4eoADZ4qrJ5WxEJZ_rhsGPGwXYKdPvKORmSFslSc69A5XtVeVa8SIF3z6ktsQAWHKd8_5Q5X8taE_g4XsXUo56hrge9gRSQc46uyCOTDZTdeHqG6wLOnWJ1tjDaMI7JNgLbfZ4Rqc-lYDKsB93stkmMeuXtdWROm4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروی دریایی ارتش جمهوری اسلامی تصاویری از یه نفتکش در حال سوختن تو شرق تنگه هرمز منتشر کرد و از اعزام نیروهای جدید به دریای عرب، دریای عمان و شرق تنگه هرمز برای رصد رفت‌وآمد کشتی‌ها خبر داد.
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/73230" target="_blank">📅 18:16 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73229">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7853c789a5.mp4?token=m9Et5YNhy1tqQ0t1E_rGI5vW8AeDABO6sXSOKa332MJxy5EpsMCTWCOly89ippI5BXPoCmunYhVStqeT6uJTbvelR8HrqOujbhGVJJdmAZdhmbm-9hjOowzlc7vc_9WyLwXgEYynVFunSINNSNsECEdm6YiosXluE97JHJqqTF0mcGeeVHPqyGlz0UAFurmKiYckAJx5qZKkzI4WkuiMvg-n9wCeOSWcxv0UqbtKX5BFqas05YypwFTiUg5_WFuCZb7ywT8Dv54UiR4eprxFDAxNvJL2JJj8bO0aPfxQROM0Ff_hUoUhPvEgq_Tq10uXmyxUAMnqUO5k0q21Zouzpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7853c789a5.mp4?token=m9Et5YNhy1tqQ0t1E_rGI5vW8AeDABO6sXSOKa332MJxy5EpsMCTWCOly89ippI5BXPoCmunYhVStqeT6uJTbvelR8HrqOujbhGVJJdmAZdhmbm-9hjOowzlc7vc_9WyLwXgEYynVFunSINNSNsECEdm6YiosXluE97JHJqqTF0mcGeeVHPqyGlz0UAFurmKiYckAJx5qZKkzI4WkuiMvg-n9wCeOSWcxv0UqbtKX5BFqas05YypwFTiUg5_WFuCZb7ywT8Dv54UiR4eprxFDAxNvJL2JJj8bO0aPfxQROM0Ff_hUoUhPvEgq_Tq10uXmyxUAMnqUO5k0q21Zouzpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۸۰ تن میوه به علت بسته بودن تنگه هرمز رو دریا خراب شده و داره دور ریخته میشه:
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/73229" target="_blank">📅 18:11 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73228">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/73228" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBe
t
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/73228" target="_blank">📅 18:11 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73227">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/patPdm-b9qTYQL6oaA276jkPlZ1XdWVexxGiGWnBRXsasEp4XSlMgpmsa_PSThkoB78GIS0-NJdlO3cwgspiLSAw5m3aEuUhj7Bv36BBcIik5iI3rULyPdV8nQ2Sq5XYrFlSZt-es_UaalZUU6cnZN13nnWsvcO3LeFpclRh5EfF7TShFAfrc6o1SUDUNKTuJJU56GVYnivs_jlYy2SXJFsJhCEPriq-4VsNmX6GN5z8VYToaTyx0Z0Fenp2vyvGiF3z75IgqtgSIswx4mjPTxcDmPbgWpOWH2spb-hWQ73wVOXRXvTK34FoNcVYTKfD38CoFz8192EXQayIlrLKPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منچستر یونایتد
🆚
اتلتیکو مادرید
🦖
این نبرد حساس چمپیونزلیگ را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید!
📉
نگاهی به آمار ۲ تیم
در ۵ رویارویی اخیر :
منچستر یونایتد : ۱ برد، ۲ تساوی، ۲ شکست و ۷ گل زده
اتلتیکو مادرید : ۴ برد، ۱ شکست و ۱۲ گل زده
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
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/73227" target="_blank">📅 18:11 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73226">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">حملات هوایی نیروی هوایی سلطنتی عربستان سعودی به صنعا، پایتخت یمن تحت کنترل انصارالله.
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/73226" target="_blank">📅 17:49 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73225">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f155f86ad3.mp4?token=RTfun2WaCbgdaSQnLp0yxas7dLmDCHrv3apUDLNEL62eFjRDhW_YfLGgoYn1dVtCXk4qlNw4aIlqvsm0rS7ocasfgunkKbU7S5mp5yIZAlu3Lu6vPe8xzsyWnVa27Hge2t_n49gi6r4nc_ve_phyhNavqGmHZg8Yb-tdfabdYlBOhBZ60fqTjB_DcgJh3DF7aRL9VfSMNJ6MNr1W8wOtADxMz8np7adYK0BLr-SPiAQYrROkPLZtgmQVeDyVwJeQ8Nbw15DxRHuo2R0Yavu_PYHWAkEVJK-jEVrP6p1jeO6UtG4Nvw3djNBbMRd80awAvCydf-YtMYWhEqDaNG5fmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f155f86ad3.mp4?token=RTfun2WaCbgdaSQnLp0yxas7dLmDCHrv3apUDLNEL62eFjRDhW_YfLGgoYn1dVtCXk4qlNw4aIlqvsm0rS7ocasfgunkKbU7S5mp5yIZAlu3Lu6vPe8xzsyWnVa27Hge2t_n49gi6r4nc_ve_phyhNavqGmHZg8Yb-tdfabdYlBOhBZ60fqTjB_DcgJh3DF7aRL9VfSMNJ6MNr1W8wOtADxMz8np7adYK0BLr-SPiAQYrROkPLZtgmQVeDyVwJeQ8Nbw15DxRHuo2R0Yavu_PYHWAkEVJK-jEVrP6p1jeO6UtG4Nvw3djNBbMRd80awAvCydf-YtMYWhEqDaNG5fmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شهردار کرج:
همه شهروندان ایران کرجی‌ان، فقط خودشون خبر ندارن؛ چون بالاخره هر کسی یه فامیل کرجی داره.
آغوش کرج به روی همه بازه، ما هم آماده‌ایم از همه مهمون‌نوازی کنیم.
از پارک‌های زیبا و اماکن دیدنی تا رستوران‌های خوب، همه‌چی مهیاست؛ فقط مونده بیاین کرج.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/73225" target="_blank">📅 17:31 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73224">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">#فوری؛ائتلاف به رهبری عربستان سعودی دستور تخلیه ایستگاه مرکزی «الصباحه» متعلق به شرکت نفت یمن در صنعا را صادر کرده است؛ تأسیساتی که تحت کنترل حوثی‌ها (انصارالله) قرار دارد.  @News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/73224" target="_blank">📅 16:49 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73223">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">حوثی‌های یمن بار دیگر به همه کارکنان تأسیسات نفتی و فرودگاه‌های عربستان سعودی هشدار دادند که محل را ترک کنند و این نشان می‌دهد که حملات بیشتری در پیش است.
حوثی‌ها به همه «کارشناسان، مهندسان و کارگران در تمام تأسیسات نفتی عربستان سعودی» هشدار دادند که مناطقی را که نشان دهنده اهداف هستند، «چه قبلاً مورد حمله قرار گرفته باشند و چه نه»، ترک کنند تا از به خطر انداختن جان خود جلوگیری کنند.
آنها همچنین هشدارها را به خطوط هوایی، فرودگاه‌ها، مسافران و کارکنانی که قبلاً به عنوان مناطق هدف تعیین شده بودند، مجدداً تمدید کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/73223" target="_blank">📅 16:46 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73222">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BrMo0aGdw93kGeIEwjG4erevonJ8AoE2uCgfw-olx5QA24kKcVF-XCOdfwp2sIh3cPDm5261xsrfsry4mk4UcB-Djdj7TD3CiGhsEzhT8P88R8azEj-yjpaeU2pFRfILAPoD6EmkqRZUK_6s4ZU4-KJivZsMQ7ebnmzqM7wOXy04I-DRlBhm9K7cHSOv4XtJGNxd5_p7rSDCUYmv0LTO6ZUgJFFeUTLhfZFRI88558fPng9lKs4YHPb7TYEvbL6v9YMjJRr9AENey9z2TbzdKMghPcJPY-Kzg2sW1Vfp6Y4heqfhNU0JWAlKQHSbeeug1YnBeDGmLcYqnZzN1VJ5WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
؛ائتلاف به رهبری عربستان سعودی دستور تخلیه ایستگاه مرکزی «الصباحه» متعلق به شرکت نفت یمن در صنعا را صادر کرده است؛ تأسیساتی که تحت کنترل حوثی‌ها (انصارالله) قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/73222" target="_blank">📅 16:42 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73221">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/73221" target="_blank">📅 16:42 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73220">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ntlsf4HhQw5a0RF5BwhFRytCR32F6GeRbPIStpKoGpmxsM5GgSh1c7wJZ20JMN5YZqW8axew8drklWrcKdB6Q2fRbtJqzg2pe-RI0emVP6sDZfcg-N3ubPD4CY-tl-mebkqieXFvuWggpSIiknNXjvr1vcKJoG_ZlvhHtf9uo16hr61wN2BEF9TeH4FXPsAmYIdhj6s8sABuYgIUs1dby0EWwCKbQVGvIzbomvS4-EtyDErLqkoSONf9m0Z1c3wfKCbmK5BHKiA5g-5TTbwm-ZTg_VXSTD4BiItYUt_1zSEUDAkCtF5aCWN2-y3EUQOyE8w8_ouEp83KoCh1CeDclQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk
https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/73220" target="_blank">📅 16:42 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73219">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/N8aCXv_ykFuqV7jA6ZgC0flBsItdKNdV2NKYS22wv-1ROmcLnIu0RnoT-pRW2J16ZPFMEit8pJ0DlSEX2uspbBbeS2hY4-vWndShKaldb_Wda72FTHJbWh61zsAb0-q8QczVJ7GAYM4sOeMWnnadMRa6DDr1qPd6lvC-pFaG0RdWlWN0dPI8TPJJm87x0my6KWgC7MQXhIBS26rGXQVTsY_oRWd2tjUNhIq5Onouh5AhyuTXS5sfGfTWbRDUnklzr7gnIUjVtSZfdKLibtJDFjAXWbmDDqYBLSv82ZwLrF0V9YUXRFCQ2Ksl63Ui-ZLkyLK2FARddsetwojgH7Ivog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گزارش وال‌استریت ژورنال به نقل از منابع مطلع، ایران به کشورهای منطقه هشدار داده که در صورت آغاز دوباره جنگ، ممکنه نیروهای مسلحش حمله زمینی به کشورهای همسایه انجام بدن.
ایران همچنین به مقام‌های عرب هشدار داده که ممکنه تأسیسات نفتی عربستان رو هدف قرار بده؛ در کنار حملات ادامه‌دار انصارالله به تأسیسات نفتی سعودی.
به گفته این منابع، ایران قصد داره در صورت شروع دوباره جنگ، حملاتش به نیروهای آمریکایی رو هم افزایش بده؛ از جمله تلاش برای غرق کردن ناوهای آمریکا در غرب آسیا و کشتن ملوانان حاضر در اون‌ها.
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/73219" target="_blank">📅 16:25 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73218">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f037a6e61d.mp4?token=AsZNbrnoR7B-LgxjB9VFUk40c5sUm-Loy-X_4TkJX1z409plQYbtRgj8riDFwk51vSl0RcQ70pwKAS7wHekGDvhfp8Hv9ldD9dh978ierqDY_DM7r0xVTftG4pUYINv4zCuAc8SYFads0xiBtAMIwjzw67qogq2L_ilMN7MxtDBIONqZkdOQJhQ7xBa1EHSIbQ7_5NCT24IAQ_MJjTQw8sHtpSqJBGptqUkpnsDLhkwx1Z0eE35l85oJiVF8KG8o1sg-MEa-1TrEKN6nlQydCXSM7Yrlt3gPXALjspFmut6GqsttAHHO77F-hwq3c3JBRR7HrSJknhvpFVDJrA5MDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f037a6e61d.mp4?token=AsZNbrnoR7B-LgxjB9VFUk40c5sUm-Loy-X_4TkJX1z409plQYbtRgj8riDFwk51vSl0RcQ70pwKAS7wHekGDvhfp8Hv9ldD9dh978ierqDY_DM7r0xVTftG4pUYINv4zCuAc8SYFads0xiBtAMIwjzw67qogq2L_ilMN7MxtDBIONqZkdOQJhQ7xBa1EHSIbQ7_5NCT24IAQ_MJjTQw8sHtpSqJBGptqUkpnsDLhkwx1Z0eE35l85oJiVF8KG8o1sg-MEa-1TrEKN6nlQydCXSM7Yrlt3gPXALjspFmut6GqsttAHHO77F-hwq3c3JBRR7HrSJknhvpFVDJrA5MDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">درگیری‌ها در ارتفاعات چاه‌احمد تفتان، با گذشت بیش از ۷ ساعت، همچنان ادامه دارد.
به گزارش حال‌وش، در حمله افراد مسلح به ستون موتورسواران لشکر فاطمیون، بیش از ۲۰ نفر کشته یا زخمی شده‌اند.
پس از این حمله، بیش از ۴۰ خودروی نظامی و پهپادهای شناسایی و رزمی به منطقه اعزام شده‌اند و نیروهای نظامی همچنان با خمپاره و پهپاد ارتفاعات را هدف قرار می‌دهند.
این در حالی است که رسانه‌های حکومتی پیش‌تر از پایان درگیری و کشته شدن تنها سه فرد مسلح خبر داده بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/73218" target="_blank">📅 15:54 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73217">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ائتلاف به رهبری عربستان سعودی:
به‌زودی به غیرنظامیان هشدار خواهیم داد تا مکانی را در صنعا تخلیه کنند؛ این اقدام به منظور انجام یک عملیات ویژه صورت می‌گیرد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/73217" target="_blank">📅 15:44 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73214">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IsWdQYQaXRtzb6N4-3ZeljjvSbOQBfkbKPsBqwXApxojUGIAK_zMaDxhMVM89vXgMb4eAAsQLZ-stjieset1okiNGkoDJz4gpoQGEvjit5Qnabshqdk4bs-otsPCEARhVipkfXdntwVCmI4R2ugSTzdrhwGqOvU4NFNc0Iq4yEraSHbq0dn7fM2Y1udIcjB53nQdgDtz4tIyR1PoU-kee0IzTqgQC7DVKRIm9GI6BGbTPCCEPThyJhTOJDIy4GBSk7hC85bw_Rj4B45avX_4eR4PT63xjBXhY8Dovv9nu5uogyBPgRpz6hkXA9wHf6c1e5b8sEjkrkCIcSp9AVQyfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oq7M60dbjRstx9fP-KogP0JC-YwQV5qfquzJng9Pml1p_O7bN_TDLw_9ivAPu4vgeN5hyoke2r44C0zou54OCFm3pUbblcVN5LDMfoMmr6DHWi9rJ0k43ezTKTbzhX8xCVMUFSlBF39cUoozOQmliuFDqSHwqansXpQTZOq-nn0mP7a5x27EKG9nH2VX7KxmLj9oTT2q5UKvt2DGXpZ-X29rBal_4KDvUtbEkJQZFskgdBXM_V5_qhEztfcECuT28yXhoMNuavjMGsKimUXMamTUYrm1QI8Tk-Kdri6gdMQpZ92h547wsORRXaD0foirxDF_B_WtyaraO0nGWUzLDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mjqJTQU7Vg4miXfeEypuSDHGKEJ5wmwqEvUKcoYuj-x27O8pusR3Ol52Oo0Btv_zbnNQkpiPtTSWdoXHmnhIUundbj2LOjQUui_LUVXJ2jKIAeHsBRsj8tVAICGUbxV3Q1YPuJDL2yZjedU9K-KKNbUARZHE4WCteArcaj5_BrgRC4FKpSnCJ6O2VueL2Rs7ekQ7Ko9_lMiYRqA4RGoXgPUdCWD8gRWME_2tdTrAWNnCtYHDdvGx2xAlU9hXGqbgVlQS6qUOg6ELkqFP3__9Sv4QVomR_F0Jre8seK6Zh2a6CQiL5F2Foj-miiBcG2aAk3Y7XbPlUeg-MdvyVdBGpQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حدیث ستاری، مدل ۲۵ ساله ایرانی و دانشجوی دندان‌پزشکی در امارات، در مسابقات بین‌المللی زیبایی «میس گلوبال ۲۰۲۶» موفق شد دو عنوان «ملکه زیبایی خاورمیانه» و «برگزیده مردم» رو به دست بیاره.
+لباس ملی حدیث در این مسابقات با الهام از سیمرغ، پرنده افسانه‌ای ادبیات فارسی، و نمادهایی از حکومت‌های ایران باستان طراحی شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/73214" target="_blank">📅 15:27 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73213">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90850a02ad.mp4?token=vvAvjIlp3XTIAKRysIvk1hiIAXxe9i-ShG0g-2T_isarPWy8TEMGkMjVlmsZpEbIOwTCSucHXmVoPr4B0BhyYUtx0xczIlzz2z3NS4Xy6fNKqLUhegZEmMrMz1xmM0QMcveLnTP0OjWZ9nMwEH9tAS2iNdhDP2pA7fdS_3xi57zj9pazTwzLBSXd2uNhqbtLv6xZ_s36RbJAYZ-SDftQEY1oUqEpULJntUJFlS9qItFV1vk3_YuWEo6-3gbEZPUdp4QNrwdLSFEGtJ5fA3tgLz8xdd1Zf4JwEh2Z9Rbjoa3UV4Ra412YigphN_Vc1yCQGsB5cpHOjl1ZXKz9WAPLkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90850a02ad.mp4?token=vvAvjIlp3XTIAKRysIvk1hiIAXxe9i-ShG0g-2T_isarPWy8TEMGkMjVlmsZpEbIOwTCSucHXmVoPr4B0BhyYUtx0xczIlzz2z3NS4Xy6fNKqLUhegZEmMrMz1xmM0QMcveLnTP0OjWZ9nMwEH9tAS2iNdhDP2pA7fdS_3xi57zj9pazTwzLBSXd2uNhqbtLv6xZ_s36RbJAYZ-SDftQEY1oUqEpULJntUJFlS9qItFV1vk3_YuWEo6-3gbEZPUdp4QNrwdLSFEGtJ5fA3tgLz8xdd1Zf4JwEh2Z9Rbjoa3UV4Ra412YigphN_Vc1yCQGsB5cpHOjl1ZXKz9WAPLkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عرازشه شب گذشته،  در میدان انقلاب تهران علیه مسی شعار دادند  !!!!!  @News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/73213" target="_blank">📅 14:57 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73212">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gjFsEchtQ_gC7QLCOKA-Df7i91297Qhj0wkNgz7qSh72aR1BOMCdCKF-cN6BUtaXwjxPf3JTzo5UmJyfBRhr4n_ipgZ58o7EACi_AOfINeo6jgd8ML4bMUt01XvL6dOh4sH29kPZYfFf5s1bl3M70hn5q0aYNqJs0sQ1J46wsel5ASxxJ0yOcHVDkMWSP5zDk2BelCvVYuifgQL-USY_-9yXiy-iU8KTy0wQzIP6OncME-eHZiOvLOUHSmcpEu8P4BA7NMWuO6KdSr0jugeveotWd-iHVX2SbjdTS2gds5WPbpcDUdyVkmDveuhPyG92ixbc-lzCgH9dXt8_XKg8QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش روزنامه «هاآرتص»، بنیامین نتانیاهو، نخست‌وزیر اسرائیل، از طریق میانجی‌گری ایالات متحده به دنبال جلب موافقت عربستان سعودی برای مشارکت اسرائیل در عملیات نظامی علیه حوثی‌های یمن (انصارالله) است.
نتانیاهو این پیشنهاد را فرصتی برای تقویت روابط با ریاض و پیشبرد توافق احتمالی عادی‌سازی روابط می‌داند.
با این حال، محمد بن سلمان، ولیعهد عربستان، به دلیل نگرانی از واکنش منفی افکار عمومی در داخل پادشاهی، با مشارکت اسرائیل مخالفت کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/73212" target="_blank">📅 14:31 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73211">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/876aa9210f.mp4?token=mtCoYgh9nu45kN1j-YvmMg1RHWCiayyfsKaUebGFPY_hQxRaJsLQGT2xDG9ZbqM_LxnUvCiTY1B09DGSb5g3TlbFYGOXOPJPiKGSJDKGB1c1mQ0Ft9ksJlhiHNUtR2H23DLVfSbiTXmq-cmaBAk25go_hx7UbqqcVI-3jPvOTr70K75IlR_Od0PDy5LZ4ekwoHSt5rvCTtvqjj4nnXDqIfv0sCpJPmFRYk-ibLHHbYk61BXrWb1LHWPArKs2j7Qt0ng9v5oZIC_8uYtcn5_oGyL7Kc7wcLBrhaN5iFOdzZS6K0xj8L9FePCfKi4pPlBfEB1IfNSqQ3XGOLJ0JZ6E-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/876aa9210f.mp4?token=mtCoYgh9nu45kN1j-YvmMg1RHWCiayyfsKaUebGFPY_hQxRaJsLQGT2xDG9ZbqM_LxnUvCiTY1B09DGSb5g3TlbFYGOXOPJPiKGSJDKGB1c1mQ0Ft9ksJlhiHNUtR2H23DLVfSbiTXmq-cmaBAk25go_hx7UbqqcVI-3jPvOTr70K75IlR_Od0PDy5LZ4ekwoHSt5rvCTtvqjj4nnXDqIfv0sCpJPmFRYk-ibLHHbYk61BXrWb1LHWPArKs2j7Qt0ng9v5oZIC_8uYtcn5_oGyL7Kc7wcLBrhaN5iFOdzZS6K0xj8L9FePCfKi4pPlBfEB1IfNSqQ3XGOLJ0JZ6E-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدیرعامل شرکت آب و فاضلاب استان تهران: قیمت آبی که به مشترکین ارائه می‌شود ۱۱ هزار تومان است درصورتی که قیمت تمام شده آن ۸۸ هزار تومان است؛ فاصله وحشتناک است.
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/73211" target="_blank">📅 14:26 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73210">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c54425bdea.mp4?token=QKFMMPUTXg7y0yZ0Tz9z7rWhyMw0aSb7Mn3ie067zfcJowjmei_xWGJCSo2O_raK5bCNQYa3hbBTwGrQWRzbO5hSETKIsgOr55TAJr7JtzpC1FS_K9ut8JS7QBPQ3-LuqcWR5p5TZaZgZXiKTbowHKf22iMbFTN5ZfI8GpgL77YsDGEctAIoA8NaiJ5__zXja3ukdu9UERdU1mVVammYhD_6FQ-pB3pxlzuKEHy1yhuhRLUskcAiSkIMSP-LwwFVwtfBM_UeqDf7on57gyd2vH-KF_w0ki2KCDffGG63pna9Y_leb8Maoj5f0QmvorkdIFA_Ra-uL6xM6XJevScZSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c54425bdea.mp4?token=QKFMMPUTXg7y0yZ0Tz9z7rWhyMw0aSb7Mn3ie067zfcJowjmei_xWGJCSo2O_raK5bCNQYa3hbBTwGrQWRzbO5hSETKIsgOr55TAJr7JtzpC1FS_K9ut8JS7QBPQ3-LuqcWR5p5TZaZgZXiKTbowHKf22iMbFTN5ZfI8GpgL77YsDGEctAIoA8NaiJ5__zXja3ukdu9UERdU1mVVammYhD_6FQ-pB3pxlzuKEHy1yhuhRLUskcAiSkIMSP-LwwFVwtfBM_UeqDf7on57gyd2vH-KF_w0ki2KCDffGG63pna9Y_leb8Maoj5f0QmvorkdIFA_Ra-uL6xM6XJevScZSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخست‌وزیر نتانیاهو :
کشورها، حتی آنهایی که به ما حمله می‌کنند، به آرامی و پنهانی می‌گویند که رژیم جمهوری اسلامی باید سرنگون شوند، آنها ما را خفه می‌کنند.
ما مطمئن خواهیم شد که آنها(رژیم جمهوری اسلامی) سرنگون شوند. آنها سرنگون خواهند شد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/73210" target="_blank">📅 13:46 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73209">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de6a75e3c2.mp4?token=aNMpPWP3My8Pt0PuoMAO3fzuVjvAaCVGhdU-3g-ykNyST6Sdosk-IHWnLSybl7oYNCKAITmulCCzVvoUGpgkIPrUwwDS1euIWH5LgtvJ6mHTGx-6LPjSy1jWlXmJx_MtuFFLzQ0ANwsI3OaTrV3lZ3Lwislz8xU13QnwRT2E7p6vJkpfz_pq6cPEZOtOdSgaWYiy8joKaPN6V_rSvSqnU1H-GS0zbVEquQRdoZnmg-U04Q19QdKl_2K7Z5U_Qh2BRDZuBCq_J7PKV9YR2CjUHu-TMKRCoxlJk4RT-AfGA3p3-a-QWdoUmfZj3TMOVtPS1TC6Ia2zsBinVzHaSuQd_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de6a75e3c2.mp4?token=aNMpPWP3My8Pt0PuoMAO3fzuVjvAaCVGhdU-3g-ykNyST6Sdosk-IHWnLSybl7oYNCKAITmulCCzVvoUGpgkIPrUwwDS1euIWH5LgtvJ6mHTGx-6LPjSy1jWlXmJx_MtuFFLzQ0ANwsI3OaTrV3lZ3Lwislz8xU13QnwRT2E7p6vJkpfz_pq6cPEZOtOdSgaWYiy8joKaPN6V_rSvSqnU1H-GS0zbVEquQRdoZnmg-U04Q19QdKl_2K7Z5U_Qh2BRDZuBCq_J7PKV9YR2CjUHu-TMKRCoxlJk4RT-AfGA3p3-a-QWdoUmfZj3TMOVtPS1TC6Ia2zsBinVzHaSuQd_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جالبه بدونید این ویدیو که خیلی وایرال شده یه بداهه از خواننده و طرفدارشه و بیت شعرش از قبل مشخص نبوده:
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/73209" target="_blank">📅 13:11 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73208">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a96bc792f3.mp4?token=UmRnl4kH9WYySCtqEvDpKDPP5cS1rWmJc6g8-UC02Pfo0jGstQA0AFOQALfSrE1BUo7iRfyDz9rP7HU1WQt1t0QX_5eVdnq9JkqDIzKzLgcBh-7TY1rNuBBUk4RAnZzvL5_Uek42oNz8u2RtgdEU2zlnlHwz9tqSwFL3rLrHSiV0awcgOw4LWwjniZrnE3GkstWZD8pK7-mpojEJvZdne45p7p5R02qknP7G-8SOHj98d_4tsejh1iZ9iSEfPPZM4F073jTCnnhtonizwKG3fYf40ncpDowWZGYdiuK0sU48U-LyW8qbe-wHlRn2L_doER07_a1pyxrC_W30SCzUmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a96bc792f3.mp4?token=UmRnl4kH9WYySCtqEvDpKDPP5cS1rWmJc6g8-UC02Pfo0jGstQA0AFOQALfSrE1BUo7iRfyDz9rP7HU1WQt1t0QX_5eVdnq9JkqDIzKzLgcBh-7TY1rNuBBUk4RAnZzvL5_Uek42oNz8u2RtgdEU2zlnlHwz9tqSwFL3rLrHSiV0awcgOw4LWwjniZrnE3GkstWZD8pK7-mpojEJvZdne45p7p5R02qknP7G-8SOHj98d_4tsejh1iZ9iSEfPPZM4F073jTCnnhtonizwKG3fYf40ncpDowWZGYdiuK0sU48U-LyW8qbe-wHlRn2L_doER07_a1pyxrC_W30SCzUmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حال‌وش:درگیری در منطقه تفتان-سیستان بلوچستان بین نیروهای نظامی جمهوری اسلامی و گروه های مسلح ناشناس:
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/73208" target="_blank">📅 12:36 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73207">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98721d1ae5.mp4?token=KpslO5CYWeGnspCMC5MIsZwfS0S_a16YBJuHoahfIy0TC_g7SLe8d1YkggqA__8XWvm68Z5rbrhLQ_PY6D64r2QT9n8Q2feqfP38znMgyQDAWil2AN2ioOfhg9BM3TlPYIO3t5sEwRPbjPn0EHuy77dn49Erq6JkBdUX42Mw9UAsmRvnd219gqyukwPubl0WyyTsk2MS2Z7ADTO7PIE1OgDH8Nqp54GQ7KGvXGkkxGrStyF1-WF3PJ4qszuKQhlu4SRIoEBlOJiGsgDQ0_DLqFZQlbzDvcSEHIbmFGmx6qS2ZjceuHrmLsqM6bo_v0asT96QQBKPUyirqHuDezRPcUFCW_qbo05qDoQftFuY5inFJckKDmryqsIkABu7Wwb9Jqex7fXr2jBiH-KDtisURsrPMYPnnkbdxq7AZLR9pg6yvCOrV_OZ8RezjCGOPTXGG4v2vk_tvbuw_fPBdHXCkk6E7GB8pO_A6ZTtpxv5jwgZAVH7x_UB86p-FpXl2-tQqpmkvPQWRPPqstbfpPrBTmE3NXtK0HHoToaDG2kO9NhanpwwA4UfD7uyw5gb-huC4nVSIQ_hhDN4jb5g9eqLCQVYOVFo4oRQc4LpfDmy3AWTGmL5OtadBW3EMxHTz76I51VWVJkL8Po5zqmafmPmkj2pfDWlcRB4kg7QreeePCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98721d1ae5.mp4?token=KpslO5CYWeGnspCMC5MIsZwfS0S_a16YBJuHoahfIy0TC_g7SLe8d1YkggqA__8XWvm68Z5rbrhLQ_PY6D64r2QT9n8Q2feqfP38znMgyQDAWil2AN2ioOfhg9BM3TlPYIO3t5sEwRPbjPn0EHuy77dn49Erq6JkBdUX42Mw9UAsmRvnd219gqyukwPubl0WyyTsk2MS2Z7ADTO7PIE1OgDH8Nqp54GQ7KGvXGkkxGrStyF1-WF3PJ4qszuKQhlu4SRIoEBlOJiGsgDQ0_DLqFZQlbzDvcSEHIbmFGmx6qS2ZjceuHrmLsqM6bo_v0asT96QQBKPUyirqHuDezRPcUFCW_qbo05qDoQftFuY5inFJckKDmryqsIkABu7Wwb9Jqex7fXr2jBiH-KDtisURsrPMYPnnkbdxq7AZLR9pg6yvCOrV_OZ8RezjCGOPTXGG4v2vk_tvbuw_fPBdHXCkk6E7GB8pO_A6ZTtpxv5jwgZAVH7x_UB86p-FpXl2-tQqpmkvPQWRPPqstbfpPrBTmE3NXtK0HHoToaDG2kO9NhanpwwA4UfD7uyw5gb-huC4nVSIQ_hhDN4jb5g9eqLCQVYOVFo4oRQc4LpfDmy3AWTGmL5OtadBW3EMxHTz76I51VWVJkL8Po5zqmafmPmkj2pfDWlcRB4kg7QreeePCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عرازشه شب گذشته،  در میدان انقلاب تهران علیه مسی شعار دادند  !!!!!
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/73207" target="_blank">📅 12:27 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73206">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5be338c559.mp4?token=LS9j7aevmuar49kQJum_AdRpRtOaOVbQXKor1fZouQvNDroNiZR_X21VR3VfuNYsFbo_u8jTbnWLx9iZ5RJlUu7Gyfzyu4CviMrpUjB0zL_Ew-oy_KfivGp6R1wT9hRouGd_NtfYij6ZzEIasyRqQUi1VvOcJKmnJOCkAAWRdUspe6F3Ea7lw2noyojv0Zz8TxduwDXDXJ2BIviLCR5J59ghBitQbuajqCPv9Xgxxay8009S60O0YdlMlILCptYTDLPhaId9VgxJ9tgzYNnVbz9hLS-ahRCVXKmVr_-aNkx5sC0U8CznY4MFvUzDWbROQiOYa31m2xqiGvbbxSzpQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5be338c559.mp4?token=LS9j7aevmuar49kQJum_AdRpRtOaOVbQXKor1fZouQvNDroNiZR_X21VR3VfuNYsFbo_u8jTbnWLx9iZ5RJlUu7Gyfzyu4CviMrpUjB0zL_Ew-oy_KfivGp6R1wT9hRouGd_NtfYij6ZzEIasyRqQUi1VvOcJKmnJOCkAAWRdUspe6F3Ea7lw2noyojv0Zz8TxduwDXDXJ2BIviLCR5J59ghBitQbuajqCPv9Xgxxay8009S60O0YdlMlILCptYTDLPhaId9VgxJ9tgzYNnVbz9hLS-ahRCVXKmVr_-aNkx5sC0U8CznY4MFvUzDWbROQiOYa31m2xqiGvbbxSzpQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عده‌ای از اراذل و اوباش سرکوبگر سپاهی و بسیجی با لباس شخصی و پرچم فلسطین و به بهانه حمایت از دانش‌آموزان فرانسوی در برابر سفارت این کشور در تهران تجمع کرده‌اند و علیه دولت فرانسه شعار می‌دهند:
«مکرون حیا کن، دانش‌آموز رو رها کن!»
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/73206" target="_blank">📅 11:59 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73205">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/73205" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBe
t
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/73205" target="_blank">📅 11:58 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73204">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MWgJ1HrPh2C5M3fOC--CcxYbqyGj0Yj4EGbcp2a2JqzXVyr8AHXlc2V8wd7m9EcoY06YjIUKdixGoihd1NtDZ6PKUoTpLVlhlR8otBcl1c39nR36iAYsvGhWbrYkgKeqQKYD-bKiBpnfql5RqV2DeF9juOSXC9f-rWb1mHQJcjL50O-NcLXdHJ1Rle1WZ5B0_LDrBb_yn7lHhbxWBPsUod4nhwl8z74CZutg8Cpy3amaSEg4MmZxERB846WxnnBJMPoaPrhifi8yLoZeWeWMK43GeD_TLobpWAXflDiCbp1xwWDOu6sZQU92AAdtvdq07FqzRA83Vqm6g-rcR1us_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
بارسلونا
🆚
گالاتاسرای،
این نبرد حساس چمپیونزلیگ را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید!
🦖
گزینه پیشنهادی:
بالای ۲۸.۵ شوت در مجموع بازی (Over 28.5 Total Shots)
با
ضریب 1.64
📉
با توجه به سبک هجومی دو تیم، تمایل به خلق موقعیت و آمار شوت‌های مسابقات اخیر، انتظار داریم دیدار گالاتاسرای و بارسلونا شاهد موقعیت‌های گل‌زنی متعددی باشد.
📉
بررسی ۵ بازی اخیر هر تیم نشان می‌دهد که مجموع شوت‌های مسابقات آن‌ها به‌طور میانگین نزدیک به ۳۰ شوت بوده است. به همین دلیل، خط ۲۸.۵ شوت می‌تواند گزینه‌ای قابل بررسی برای این دیدار باشد.
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
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/73204" target="_blank">📅 11:58 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73203">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">پرونده کنکور ۱۴۰۵ بسته شد /نتایج نهایی اواخر آبان اعلام می‌شود
با اتمام مهلت انتخاب رشته داوطلبان، پرونده کنکور ۱۴۰۵ بسته شد و نتایج نهایی اواخر آبان اعلام می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/73203" target="_blank">📅 11:27 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73202">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e31f93a352.mp4?token=P1UnLQmxfoOJsoW3nIPX6zykOcg7B64a5sGqysgkjE5ushDpu1XOCC0Pzm6r264_J6Mqvt6-0rh5tAkQ7XwlHULiQcZSjs1Mo7HYevVQzgSKsV4xxUpqd2TO48xn18oaUGPAUQu8Lp53It2Ihw5UolaWPxlT10uJVNTvSjmu4mfqXhT9V2UM6DZBojOPjsT7VlVnT-42LAneFRG4925ffGvwV_JsRTgQ5Xlia_hw08TUD3mwDKMzcEMP6UzIgOjnNYQpkxlbpWvwNgnfrdyhnmqCrke2qm45zvvy-qwyijAEi-W0TQh5VVDYZl2HjFCStdy3kjiJvG3F3Ba4DUlc_3w6XvChZH4yYfObNWs_aNh1g2j_nXbiYRDi3sZCSzKVVBmaaCUKHdl1f6uaVk2AruLyMoI28nbs8pawVg8sB17v8BBXJ525jmzsakVHoVtXCw7nwbsN_fookauyj-aUTvQNL6otzmxldxLXkG8FURU9h3Rtn0vHu2ByRpdqTgWudeGvjJ2TaKj6SSnDofTHWZ9fWLyxOsNKlxGFdqLmmbjPTfF9Ndn6eA-5Exj63JfFTE8RlFlArCazp-KDyCiBbeJFngPnXMtY-fFXISxG0uPScAOf3knz-WJjLqIpAtI4xqcbhCkZpHzytI_bNRGWEw6OEFayc7Jf7uUjMd41c8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e31f93a352.mp4?token=P1UnLQmxfoOJsoW3nIPX6zykOcg7B64a5sGqysgkjE5ushDpu1XOCC0Pzm6r264_J6Mqvt6-0rh5tAkQ7XwlHULiQcZSjs1Mo7HYevVQzgSKsV4xxUpqd2TO48xn18oaUGPAUQu8Lp53It2Ihw5UolaWPxlT10uJVNTvSjmu4mfqXhT9V2UM6DZBojOPjsT7VlVnT-42LAneFRG4925ffGvwV_JsRTgQ5Xlia_hw08TUD3mwDKMzcEMP6UzIgOjnNYQpkxlbpWvwNgnfrdyhnmqCrke2qm45zvvy-qwyijAEi-W0TQh5VVDYZl2HjFCStdy3kjiJvG3F3Ba4DUlc_3w6XvChZH4yYfObNWs_aNh1g2j_nXbiYRDi3sZCSzKVVBmaaCUKHdl1f6uaVk2AruLyMoI28nbs8pawVg8sB17v8BBXJ525jmzsakVHoVtXCw7nwbsN_fookauyj-aUTvQNL6otzmxldxLXkG8FURU9h3Rtn0vHu2ByRpdqTgWudeGvjJ2TaKj6SSnDofTHWZ9fWLyxOsNKlxGFdqLmmbjPTfF9Ndn6eA-5Exj63JfFTE8RlFlArCazp-KDyCiBbeJFngPnXMtY-fFXISxG0uPScAOf3knz-WJjLqIpAtI4xqcbhCkZpHzytI_bNRGWEw6OEFayc7Jf7uUjMd41c8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
«شاید در برخورد با رهبران ایران زیاده‌روی کردیم، چون دیگه نمی‌دونیم دقیقاً با چه کسانی طرفیم!
راستش رو بخواید، به‌سختی می‌تونیم بفهمیم باید با چه کسی مذاکره کنیم. فکر می‌کنم زیادی جلو رفتیم.
می‌تونستیم همون سطح یک متوقف بشیم؛ رفتن به سطح دو و حتی دو و نیم، احتمالاً دیگه زیاده‌روی بود.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/73202" target="_blank">📅 10:59 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73201">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ec03fa2f2.mp4?token=AcgFZIlZSO4AwEXb3NkBtSe-XGPZuMVU1GVvGnyeS_JFhJwzEJc9DZlEHcRU0NFqymPccqKVKU90tlg435Nn4ePVdY8SiFznz0KYuCvlFKs7e0_cUE-k_tmrfFPk__QigW_XHZpAvhVgjtLg-qMUaXu9sywcuOC54FQufKtyv4qqW5wfYS4tpm465EJEu30H0XFM_Lguhsg9Dne5_Q3SH7KNVI63qIaFbt-FyldIDcnoUGb9LT0mG9GazaLi_V-LjPSu9lEXeWnuhZ4xS1ZdlCjxxDib3izCM0KhXxfIsxdhvIqDYUSBqY7cMol7rRoVFuADA_hcrpE4ciVJGAKzBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ec03fa2f2.mp4?token=AcgFZIlZSO4AwEXb3NkBtSe-XGPZuMVU1GVvGnyeS_JFhJwzEJc9DZlEHcRU0NFqymPccqKVKU90tlg435Nn4ePVdY8SiFznz0KYuCvlFKs7e0_cUE-k_tmrfFPk__QigW_XHZpAvhVgjtLg-qMUaXu9sywcuOC54FQufKtyv4qqW5wfYS4tpm465EJEu30H0XFM_Lguhsg9Dne5_Q3SH7KNVI63qIaFbt-FyldIDcnoUGb9LT0mG9GazaLi_V-LjPSu9lEXeWnuhZ4xS1ZdlCjxxDib3izCM0KhXxfIsxdhvIqDYUSBqY7cMol7rRoVFuADA_hcrpE4ciVJGAKzBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند شب پیش در تجمعات شبانه تبریز، یه دختر توی ۲۰ ثانیه کلاشینکف رو باز و دوباره سرهم کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/73201" target="_blank">📅 10:31 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73200">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">دونالد ترامپ:
«شعاری که از همه بیشتر دوست دارم، «همجنس‌گراها برای فلسطین»ه!
می‌دونید اگه تو اونجا همجنس‌گرا باشید، باهاتون چی کار می‌کنن؟ از بالای یه ساختمون پرتتون می‌کنن پایین.
شما رو می‌برن بالای بلندترین ساختمونی که دارن؛ البته ساختمون‌هاشون خیلی هم بلند نیست، ولی لازم هم نیست بلند باشه. از بالاش پرتتون می‌کنن پایین. با این حال، من مدام می‌بینم که می‌گن «همجنس‌گراها برای فلسطین»!
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/73200" target="_blank">📅 10:00 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73197">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/p0CaNZLcM1tQGvxpEwy2cLSdsic2Bdj9iYK7XFneAJY_PVPQWewutaw3XCzXRYEOUS7_GksoJdpWlB-zynq4O5vdbEgYP043cYo2veXnkOHj44RNehk0GuoAJS-p3d1KLalHIAnEQUY4MT8rgb-QuCoOBiuFkHBI7r9RCeQ8oSa6HrD6TYuCV_WkELCehbitDlIqmmO3l5r4XLKw5NIDcYnfa_-RZad-0IHI593riKLunaEJtrmAccLwyGsIO1CzUa0pOUK2LdcgUCeLqCGw8Z7SU7RUS-bmxXFIsTLV-vrwWehOOK2iKvQCxppFRLzR_JLJxH3DviXkYtd2c6wwpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aCJ3FEryFaZKRqTGbBiuISxa6h_pAc_pN6Z5blqId-vua8Q7At46UBian_jceqWsnszHRx4GMVO5njtgdMXl8qz0_bCK7SKcuNJVxL4RfqEY4EcM0SCU1m1dPEZAlQVxP5ERvw6CpYVOqbKpKBhwlsNKwABnyjxI3zaFpoINnxUEjR9O43osGKRbks5q46lCPTx38-ibEZF0tFALDp0LS_ZIRWSZpz0bK4WzX71SgIS56ZzwIs-LSf2_NEchuHazlFiS8waI-B3mrWFu7hiojpUDcdQECrmjc_Ki6F06lk5t0iJGPKcBAA27BOf0vT8mb8GLmN8EMt-Ovjh8TQ52hg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/352c619970.mp4?token=taRoeHiJtvUigvjn6nU6fdKwRUbrY9_cPZ0077LhlVfw4ff-bNcRw8_DoZ00qEazxNxytDIkHBf6R0jFNwCaXYwXND2vmfS-YwIrrZk66ohf4jZ4qPA9MAb-c2liU3Jo_I-uU4UINQV2qUfM4lCed3LjoAhMYKwxzrod3Ju8cYvQ-FTP9tJrNbaU0xMG5AWS9kNxZ3ldo5AYAu48hDRIVCcx4vBTYWE6ORFellasLrfM-n3KIpR6S1bOIRC25kfzkOAREQMkmdjAB-rinN76y95ILuYvr5Gh0RzEzpUB3opsdo-CjU5TdNfWxiIUwrbipZfoMiMX4o6hXYO_GlknOw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/352c619970.mp4?token=taRoeHiJtvUigvjn6nU6fdKwRUbrY9_cPZ0077LhlVfw4ff-bNcRw8_DoZ00qEazxNxytDIkHBf6R0jFNwCaXYwXND2vmfS-YwIrrZk66ohf4jZ4qPA9MAb-c2liU3Jo_I-uU4UINQV2qUfM4lCed3LjoAhMYKwxzrod3Ju8cYvQ-FTP9tJrNbaU0xMG5AWS9kNxZ3ldo5AYAu48hDRIVCcx4vBTYWE6ORFellasLrfM-n3KIpR6S1bOIRC25kfzkOAREQMkmdjAB-rinN76y95ILuYvr5Gh0RzEzpUB3opsdo-CjU5TdNfWxiIUwrbipZfoMiMX4o6hXYO_GlknOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه پسر دانش آموز ۱۶ ساله از اندامش فیلم گذاشته و حالا کامنت دخترا زیر پستش:
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/73197" target="_blank">📅 09:32 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73196">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b63a7342c7.mp4?token=knCZP9cuZ7HvN64aTIcNy-r5fs9qV-Gm0-PfvRkc2_jwsx9u5_8cGLoxoSFdfo59IO2ML4nrohBc3bn6_BvV6q_2Yg43TshFMLEVi5ySDOHpD87uLu75Plua_KmIGIwVLFws7JF1zEvzE_8kfXWwfQhx5LZIsV40tDCFZiZ89v2RCodQS_bPqw-mAy_808cl-4-Lu07iBjohPVlKgIZAwH-c34ROf8YhDHy9ekx-RqTuIZ_sOxr6BJxRWJRf65tWCs7yqnnRfVr-XeXVly24ep8faERdZhrBX88daCNTwDGNmMv4elhvTW2QTLe44Sp5ATXw1EU0oHqZoC-8pzm1Jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b63a7342c7.mp4?token=knCZP9cuZ7HvN64aTIcNy-r5fs9qV-Gm0-PfvRkc2_jwsx9u5_8cGLoxoSFdfo59IO2ML4nrohBc3bn6_BvV6q_2Yg43TshFMLEVi5ySDOHpD87uLu75Plua_KmIGIwVLFws7JF1zEvzE_8kfXWwfQhx5LZIsV40tDCFZiZ89v2RCodQS_bPqw-mAy_808cl-4-Lu07iBjohPVlKgIZAwH-c34ROf8YhDHy9ekx-RqTuIZ_sOxr6BJxRWJRf65tWCs7yqnnRfVr-XeXVly24ep8faERdZhrBX88daCNTwDGNmMv4elhvTW2QTLe44Sp5ATXw1EU0oHqZoC-8pzm1Jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اولین تصاویر از ساختمان پلیس دیپلماتیک در میدان فردوسی پس از اصابت موشک در جنگ ۴۰ روزه
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/73196" target="_blank">📅 09:03 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73195">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/73195" target="_blank">📅 01:51 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73194">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTrexBet IR</strong></div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/news_hut/73194" target="_blank">📅 01:51 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73193">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ترامپ: انتخابات میان‌دوره‌ای آمریکا تأثیری بر سیاست من در قبال ایران نخواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/73193" target="_blank">📅 01:31 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73192">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52adbd7bd6.mp4?token=ofOUkKlmfDqIQ2OWy6XJaXaCeLYCsEJGQR3u07fw55_5he9r8IT5yXnnR7M5lPZw-7_MaxhsKgyfp0EjVTCOcb9IMlLfTDpC28couE4MbHokIelAwlKuXC-wP7GTdtpP85ylCHuqNwGDjcqOJuSZWppvY5N2muTlF-OTlS7GmyEVFpfo4sQOG8PJHdDzJWjJsNB44PshV_2_Idka40pITQckrH7ufPhHTXYGO21_kd5BLQHlJN1-uVPDdfmYdpIRBynw62ZTwke6O27lcV0K58KZG-9gVNRr6LEFeSwhoF-ri6dVi9pWvDHmVi3ZQ7lwD4jJVuxiVzRxxLC--YFcIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52adbd7bd6.mp4?token=ofOUkKlmfDqIQ2OWy6XJaXaCeLYCsEJGQR3u07fw55_5he9r8IT5yXnnR7M5lPZw-7_MaxhsKgyfp0EjVTCOcb9IMlLfTDpC28couE4MbHokIelAwlKuXC-wP7GTdtpP85ylCHuqNwGDjcqOJuSZWppvY5N2muTlF-OTlS7GmyEVFpfo4sQOG8PJHdDzJWjJsNB44PshV_2_Idka40pITQckrH7ufPhHTXYGO21_kd5BLQHlJN1-uVPDdfmYdpIRBynw62ZTwke6O27lcV0K58KZG-9gVNRr6LEFeSwhoF-ri6dVi9pWvDHmVi3ZQ7lwD4jJVuxiVzRxxLC--YFcIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: بعد از اینکه متحدان ناتو ایران رو به طرح حمله تروریستی به پایگاه هوایی فرفورد بریتانیا مرتبط دونستن، آیا قراره اقدامی علیه ایران انجام بدید؟
ترامپ: «باید ببینیم چی می‌شه. اقدامات زیادی در جریانه. وقتی می‌گید اقدام علیه ایران، (باید در نظر داشت که)اونا دیگه نیروی دریایی و نیروی هوایی ندارن. تورمشون هم الان به ۳۰۱ درصد رسیده.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/73192" target="_blank">📅 01:29 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73186">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/e-QwP-S8PDEl_h57qecTxa1RLnOfgTXtmmT0dykIiXKWP47xMS7jEP8r1wLvdsh6Z4rqmFpz2m59kcombBeJXE0jlRtX3AvAHbdKYh7-jkimivDR6BZTb-Pxw-LrS218ZVc8XVLdpOrFfPHpT4S7i6nO_BhtU_DjT-x_t0i_ZbaTZHyt-mK8hnWts1CzyC649yHooH_qmNl_Y4ZXZPPFxwkvOV4pjPqUbjAY_5EWHThksI6W4tDRBH6ogQjbuPvug7WUEC9r8Wq5NKFEVmkwM4DeViOoZnUHSOnFKkDMSzHPNkgwtmkCsSY3mfoljs7dPRvSuOVZsutMzA-aQMsvYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/uf7EyijQCdtimdrL85-lbfmIXjOQJ2f8M71LNMlKO9Ug_6IP8LKvYZht5ieVZBta019pZQfJoWxhwuuY7W5sgwgAbcBn1TizLpb0Va1FqUdxOSGqy9oHM8veD0I1aX1t_58cayKJ5dBWQYiW4hAcluf27lMzaRyKXnsUfabr6J40jWvCJbdZNG7f1FBANZdLeFjDODGEN0q07AUf4URUrvYdNIppNtHHDn0DWpXeR8wPVgYv3KNCZNedjR_ePjHfLYWe-Fzq_-2W4PxP-tjoWd74XUYvhJEiQvYg6l934xUXIsHMlftN0K30kZuARsKTp2wBXrklk92tQQfCpUqNEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/oUnkQ9ewGC0JZLO6UwGxtKTZoNpNm39XGJbP7tSHfLWvqAdWkJxajy13jl4IFKF4pgA3atPAkLKRadnxTSbVDeNF84djCchAn9dCVG23EGI4jhErLBzjdIDgyH7rsdkCbrql6So9yEVFZdaM5FuHHseFgkKAnh40aYA0CtIviOyfDH83RswsYgZJwUNaFXs-5JqHvR91mvhPXVNZeJ73UDWyZgQKCiXhwar-qhvBB6SA3RBxNBr_Cg5STPdK95PT5BWTHskBleUFyzPCXKkJdsApSQMvnS9GbZ6gSFWkDuALwCc6g5PyyAvQ37k0cvx7p_I-IilK_LkYzMGmYjzCxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZVGH0cD_EC36LB88G92KJcgv9149u7KoWmbjUw6b_RZN-ZRzHtirTVy1BcEe-uYc5TC0Z0ntkp4e6rN9tky_xcdeye64cM_F7ERStswAJppIQsUgyQzvHw-ycYqYrZD47GhPcCuei_AnW5thlqkSr66FI1vbC_wj8RwWyWNjHiHz_T6dC_6Z7JhgHOMlAS1-XepeWlEzLO1UixGo78oeQxcAy962na4HhE8J0NR9H6k55vYDRVYMRhkNeOvsZs0gskwNFRUzca_HDTQEbxEU9tES778FxNBpZj4CdcP4LDe8u3ura4OzcbzMB8Si15sKWujJlpzC7Xcj6KnKjefSdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OEZBdmOhJq-z_TMe8hatwWHs457QccpPU8faCLrCFJn05myQcQs-IYtisE02aRuvr8Jt7_stiZ6CdBnPhLtuE_6XJe0ensK3DPKbknv6mCKivO9BgPc9SyHJh6FkV2yn1hZLBjURV0AcmYAeSU0I_KkQBhAO3CZHMxVDZ67u1w9Yi1fWORCNll6CqW6GelwG9WccNg3OyEsMflg3aTlgjBoxhchClZgUXHL8Ct2mZTp6Jtdk6xl3FdYNoGCj0rxFJ9b0ueJ0o3c9TP2zD_PHorE8P9ROpUTbD7trPfmDjvOgtVzehjff4vKYg49oRHLhJONZn5OfvaoD95dpEQ2LRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sJ6NSCWoFAF7ZReKcukmTPOo4X41DaYqcXoa9FdOxOCT38NsuVbUcusE0i0j-nsvTlirUq78g3QI5LcL0O3Di0nR81jxOduHmfoQYR3H4MomVXZppNuHIqoFM4jrgjrv3O6V5_h_6JXQTMO5rIf2fRb_GP2ysHbDSFFDw3pvABb1SQiEr9DN0mWY--mbF6jtvWniLtoqrjRh12RbLAJgfNYlDUV4lb9DIRi9PoHe8HzH_BQAcXK7NkywBlhVHhU79fS65H6gLKn_gYcbtPd-9DC7NcNgP2MiUOGIWiMIHSG-bxHS56__8oUVxzqA-6XZEni8cPEBhzombG0NkUdjWw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در ۲۴ساعت گذشته سپاه پاسداران به پنج کشتی در تنگه هرمز و یک کشتی در ساحل عمان حمله کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/73186" target="_blank">📅 01:13 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73185">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23f60941af.mp4?token=inFANAIAANGq4JmPSnEMgRuspOmGn9oGm3bYLMOBTAM4VbUb4UeK3HbYQOv1Liv88LsMQwr9ylbCqZkouE_FKbJzlT_mXvFYqiq-NbqSdytKIz8hfht4QltAzbb40aa40Q0pMMoFZ9IOxZeGAwl_pcWw8LBaUM4vUk8HSVZAgxFV4Gw9fsiOV_pSL1D5kw2IDAb9fyMx7XZxpBwZBto-OuzGV8yIo9sBDWZfRJHvFKd95bjCSjsU018eoIKxnXEu22xozgBRz7CHX_JJ2f1EBFIpOIZ-KwAN5mXAnCqwIPRJdukTZ9-jAiB0KtFm7_INzEh07CPx-qx2VBXt6W1V-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23f60941af.mp4?token=inFANAIAANGq4JmPSnEMgRuspOmGn9oGm3bYLMOBTAM4VbUb4UeK3HbYQOv1Liv88LsMQwr9ylbCqZkouE_FKbJzlT_mXvFYqiq-NbqSdytKIz8hfht4QltAzbb40aa40Q0pMMoFZ9IOxZeGAwl_pcWw8LBaUM4vUk8HSVZAgxFV4Gw9fsiOV_pSL1D5kw2IDAb9fyMx7XZxpBwZBto-OuzGV8yIo9sBDWZfRJHvFKd95bjCSjsU018eoIKxnXEu22xozgBRz7CHX_JJ2f1EBFIpOIZ-KwAN5mXAnCqwIPRJdukTZ9-jAiB0KtFm7_INzEh07CPx-qx2VBXt6W1V-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: انتظار دارید جمهوری‌خواه‌ها مجلس نمایندگان رو ببرن؟
ترامپ: «ما عملکرد خوبی خواهیم داشت.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/73185" target="_blank">📅 00:55 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73184">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20acd7602d.mp4?token=GS-0ovyGfK1Ym2XGsz8BavNO4qY2uBY9bTN-eDkpKabxWyZlbvKZ6KhWrtj5QHrzxbSd2elqh9zlwe4eAnTUsnSnxZclyogS3kHfPAtW4TUG5uzssz0Sw81du6anOBcoNQ0yDm2Ife2t7bTKgyPiLxB8dNQs9yR1fvqb-wId0B4kBpGnZpgDZgIyxoGMzszkPRo2zT1RapdrJjRUgs3WWcG-Z9AdA9uxERxr2MwdIWDBO90J14k1oJ57QBui6JfJI24gUW17Rth9ZH_Zitx203LdgkaoMs8aDZt5ZhgkjK0UQlHoGQzMOPBE8_-dJcYZNOGg84eFU_ILQDsoKwE0mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20acd7602d.mp4?token=GS-0ovyGfK1Ym2XGsz8BavNO4qY2uBY9bTN-eDkpKabxWyZlbvKZ6KhWrtj5QHrzxbSd2elqh9zlwe4eAnTUsnSnxZclyogS3kHfPAtW4TUG5uzssz0Sw81du6anOBcoNQ0yDm2Ife2t7bTKgyPiLxB8dNQs9yR1fvqb-wId0B4kBpGnZpgDZgIyxoGMzszkPRo2zT1RapdrJjRUgs3WWcG-Z9AdA9uxERxr2MwdIWDBO90J14k1oJ57QBui6JfJI24gUW17Rth9ZH_Zitx203LdgkaoMs8aDZt5ZhgkjK0UQlHoGQzMOPBE8_-dJcYZNOGg84eFU_ILQDsoKwE0mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: شما گفتید روسیه و اوکراین با آتش‌بس موافقت کردن، اما هر دو طرف می‌گن چنین توافقی نکردن.
ترامپ: «موافقت کردن. می‌دونید چرا؟ چون من گفتم: شما موافقت می‌کنید! دلیلش هم همینه.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/73184" target="_blank">📅 00:44 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73183">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b813e1384c.mp4?token=qgQDOMdZ0FRgbd1q2zI8_4y2OCE9u5KphmixA_4-c7RM_XX2DIrFRYnIrg_4YxlmVSdBZ4hrpdryfMw3V_n4RAraSpYD4dAb5P4yKW8oFwfuxGHqVoWEN1ttkj5jwG30Kpy2o5q2-cH5bi40Oj1Sl0sOlCVaqSNC1O_hHLykFYMxJC3LXDXGyeaEBdgTkH8_hxlu6YQ9JrfYGX931X9RSQh0yYseBuqlA_e8s8T4ZsGQELxXO3WOpbvOdUf1w5MiXjBWc5N_4lnegfSK_Cg7GSmsBOVgQozvblzrRi2uXRHfg3ZGX9348w_NTk9yMiADDbWUzT8GhSv8FPssPdUjVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b813e1384c.mp4?token=qgQDOMdZ0FRgbd1q2zI8_4y2OCE9u5KphmixA_4-c7RM_XX2DIrFRYnIrg_4YxlmVSdBZ4hrpdryfMw3V_n4RAraSpYD4dAb5P4yKW8oFwfuxGHqVoWEN1ttkj5jwG30Kpy2o5q2-cH5bi40Oj1Sl0sOlCVaqSNC1O_hHLykFYMxJC3LXDXGyeaEBdgTkH8_hxlu6YQ9JrfYGX931X9RSQh0yYseBuqlA_e8s8T4ZsGQELxXO3WOpbvOdUf1w5MiXjBWc5N_4lnegfSK_Cg7GSmsBOVgQozvblzrRi2uXRHfg3ZGX9348w_NTk9yMiADDbWUzT8GhSv8FPssPdUjVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: روسیه همین حالا آتش‌بس رو نقض کرده و دیشب به اوکراین حمله کرده.
ترامپ: «در این مورد مطمئن نیستم. بررسی می‌کنیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/73183" target="_blank">📅 00:43 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73182">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BZU1ZouUOvxpWaxJZUDCV00FNDpkgqhaxIpU1cauKnLIPcTrWmN5KOelZhYgzqWGqNDcGdJAfKzTchP3Sk4Ky_hi_VE8KOFkMJWLo_A9-5ByFVBo0WybvXCPWEPfBrsqa9_QVXHr1FihwTw6oReZQK2vIg-Oifu-KW3ZMwbEjNvv1lfLugSJmW44HdJR0ypgo5W52H3g-IaQqQTB8yrDzwAz5enB4PedbS8spGVOEB0RK_YjrpNbHB_qpYzK6Ja2zEMwFfo9Ec8p_cPIEt851cSOxDBlFw8k85eIe5s4G-mCP9QAAEoabxUfD1tEQ9nfxQEV0OZQKumNneGmqEL8cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آر. جی. میته، بازیگر آمریکایی که به خاطر ایفای نقش «والتر وایت جونیور» در سریال محبوب «بریکینگ بد» شناخته می‌شد، متأسفانه در سن ۳۴ سالگی بر اثر خودکشی درگذشت.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/73182" target="_blank">📅 00:18 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73181">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a66098169.mp4?token=HFOuBFJSfJ9D0ZnWeCvHfRBLBvwcHCHLRBudHM-UPmFsbxik4Ujd3Y-XJ-UCQzT3lJ7nnh4ntqDjDl0-A2Ngp2YDHvYjQjuxy73lfg32z9uzbCTb9BsZcaZrstGAndfniILxEyd8jRZ_QwTsLZtcKT40lu1rZ5WqDLUotjt-nTqxodNxjB4t5Yt4VeUQSBb0YWBJT_saiCr0NKCBxR0fprgQeCJzemj8ItN4PZwq18nZbz3vYvkwvRKMkjJocVwch1WbXXKGO7KqO_0Xb67ziyLQtiNxIw-bviJ7U3maz82uZYrujleQU3lNb6Ue1JZsDQYf7dd5R8AlM5A4PAkLyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a66098169.mp4?token=HFOuBFJSfJ9D0ZnWeCvHfRBLBvwcHCHLRBudHM-UPmFsbxik4Ujd3Y-XJ-UCQzT3lJ7nnh4ntqDjDl0-A2Ngp2YDHvYjQjuxy73lfg32z9uzbCTb9BsZcaZrstGAndfniILxEyd8jRZ_QwTsLZtcKT40lu1rZ5WqDLUotjt-nTqxodNxjB4t5Yt4VeUQSBb0YWBJT_saiCr0NKCBxR0fprgQeCJzemj8ItN4PZwq18nZbz3vYvkwvRKMkjJocVwch1WbXXKGO7KqO_0Xb67ziyLQtiNxIw-bviJ7U3maz82uZYrujleQU3lNb6Ue1JZsDQYf7dd5R8AlM5A4PAkLyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عبدالملکی؛ وزیر کار دولت رئیسی و عضو هیئت علمی اقتصاد دانشگاه امام صادق:اگه گرانی رو در نظر نگیریم، هیچ مشکل اقتصادی توی کشور نداریم.
+اگه ۴۷ تیم دیگه رو درنظر نگیریم تیم جمهوری اسلامی تو جام جهانی قهرمان شده
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/73181" target="_blank">📅 00:02 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73180">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">بریتانیا دو تبعه ایرانی به نام‌های «روح‌الله بازقندی» و «شهرام علی‌رضا تمرزاده جاکی» را به اتهام دست داشتن در فعالیت‌های اطلاعاتی ایران و توطئه‌هایی با هدف قرار دادن افراد یا دارایی‌ها در بریتانیا و سایر کشورها، تحریم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/73180" target="_blank">📅 23:26 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73179">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/na2s4HeJ_QQ1XSUneKT3GDQZpGSWVvc18OckpEEWObzVdTOTL7M2MsTw5wFSANwbMpXJljL_KS2_oiCOm-abs-fUJ5qXIwtxALS6j0HPsqlCHZLLAPW6RUJcE-Inc63DLP0LgvMaHvdwYx_v3645KHaYiDcDVPZ8dDodV1Uv_dAvfa8rPC-86dRNOBsqe1jDl7wIbbWOVofeEg3FEKjznWIhI1ShWWtzYgkqII_ZsPhPFuIAz8cv-qNd7yyjLI5x9KiGupPBxMNchRXlN6axTWv8urM0WGpX4tmA2hgFEU0M_79sQuZBaThVgHqYBVkpWq1mVYgx6zr9LpipuAMQOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو امروز لایو گذاشته بود و خیلی جدی داشت در مورد انتخابات اسرائیل حرف میزد که یه ایرانی این کامنت شاهکار رو گذاشت:
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/73179" target="_blank">📅 22:43 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73178">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21384b098a.mp4?token=gaImMG86RjbWI8rxAwQIJRHWoGnZvaX4UKzFCsCjbae7pKB4EUkzWj92yqVB1uMLpztAUdpyoiMftn5XoTkj--9SQjl9lPk5ba8k_O7FyyOn_DiVKUWH5nslIFR6nxduYr9Q0MMpMgZYL7xHZOZOf8OHVXrwrUQqfzEjoqIGMro4mdJPFHYnwi7Qojf6qLvZSyAwKosoCswDiGot1AExCYSB5wQniobN3GmwVAilSB9aqEgpfOuLfulAFKNRxcqD4gdNvAPf9jZ80mQWj9B7W8_IGxb0gNuiOxW0wwMPIUprJSRBjIgcsLBPUGEvXEVxE5av9Yai7LUc5QX08y8Upg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21384b098a.mp4?token=gaImMG86RjbWI8rxAwQIJRHWoGnZvaX4UKzFCsCjbae7pKB4EUkzWj92yqVB1uMLpztAUdpyoiMftn5XoTkj--9SQjl9lPk5ba8k_O7FyyOn_DiVKUWH5nslIFR6nxduYr9Q0MMpMgZYL7xHZOZOf8OHVXrwrUQqfzEjoqIGMro4mdJPFHYnwi7Qojf6qLvZSyAwKosoCswDiGot1AExCYSB5wQniobN3GmwVAilSB9aqEgpfOuLfulAFKNRxcqD4gdNvAPf9jZ80mQWj9B7W8_IGxb0gNuiOxW0wwMPIUprJSRBjIgcsLBPUGEvXEVxE5av9Yai7LUc5QX08y8Upg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازی النصر عربستان و نفتچی ازبکستان به دلیل حمله حوثی ها به ریاض به تاخیر افتاد!
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/73178" target="_blank">📅 22:28 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73176">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sY5as1HrLamis23WK9q3ma4-pwkyd8ZKXtTaIEOr29Ga3VfnjYk-hTEIMk3FklHTR__aBYXlxDu2WfV18MEtiJV8_xyjxsSV2M966PQoedgRFU4j4oqmsLwDb2Hj3Kbhb21iN-djIet6ucI8EZS_lXth_OIBHdezJLGo52-xgg5YgkD4RH6te6O49doo1Kb6UMwVj27febfueybJOCLe_WYfZWfO8Q2N4Q8tEIOBeWo6u7ZxIDjNuG1NO0FdyxfF30sgibyzwp_NZvauCNFxlLH9rDY4VYww_2A4Fe4QMPI6F-PomnVODNVvkeyCy8RuFpdxRbAc3o3mQyj85IB1LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) گزارش داد که یک نفت‌کشِ حمل فرآورده‌های نفتی، هنگام عبور به سمت خارج از تنگه هرمز، مورد اصابت یک پرتابه ناشناس قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/73176" target="_blank">📅 22:13 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73175">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f2fd3a4fd.mp4?token=V9HxXF132ofeIuYPotgsicPKU-ajUTT8r6cELbx4f7dJMuCSo7SxfdclgBVUzJydxhXXG0Er7tUvNkXw_N6CZYmOF3WZstAjot8-IiUDzdoGOx_tbBFMY7X4mHtLF45ulmRaug4D_8II05jjKWLcHdD8nLdonbWX_KCtHFIPlN_VFqtEWtGl9TRIO5xj7nKmeJwRnOsq4JN_dFFF3_E6Ip8RlRGFKNqr1yYWFlVcwcbBsbNPpXLTSenfxvxjLRxDMsY6YASGsirVMpC0X7BhVdnTPBY0akuYGSfRRoqtCtKzxJYTiZMrIggByIpeFMMsykmZMzFtPKreHz0shMl-kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f2fd3a4fd.mp4?token=V9HxXF132ofeIuYPotgsicPKU-ajUTT8r6cELbx4f7dJMuCSo7SxfdclgBVUzJydxhXXG0Er7tUvNkXw_N6CZYmOF3WZstAjot8-IiUDzdoGOx_tbBFMY7X4mHtLF45ulmRaug4D_8II05jjKWLcHdD8nLdonbWX_KCtHFIPlN_VFqtEWtGl9TRIO5xj7nKmeJwRnOsq4JN_dFFF3_E6Ip8RlRGFKNqr1yYWFlVcwcbBsbNPpXLTSenfxvxjLRxDMsY6YASGsirVMpC0X7BhVdnTPBY0akuYGSfRRoqtCtKzxJYTiZMrIggByIpeFMMsykmZMzFtPKreHz0shMl-kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی وایرال شده از یه مدرسه پسرونه!
معلم اون جلو وایساده داره درس میده، دانش آموزا دور هم جمع شدن و کله‌پاچه میزنن...
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/73175" target="_blank">📅 20:50 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73174">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KhYRkatWJFAdepXWTBmA55H0H-b0jRXmNSA69hVAqecw9DickGNgNyOIAxYu63dBKUm0G56BrhJb7etoW756UHrtztaKtHzNmtVOM7JVFOb7AzxHtgmILQDJG2bjRQ7STqleCkYtnks6SAncmG2TdA87rsPDnfyJd7OboOFaGP3E_APC9sbyC_-EtlZmZX5wMkk4W9mHq1TaZQiQQEUVsKUIgTBu24_S59Vjrvv7f-3SoCJ69HW5BLWrDjqL_5Lsjvq3l9uPm723SSuplkFpeMIGAFmVeqgxOOz7l2z5FHSRWpa-tzvfZ5nP-obaEIf9x3pKwPaKAFsPwER_OSlPiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با انتشار تصویری، اعلام کرد ۱۵۹ کشتی ایرانی در دوران ریاست‌جمهوری او نابود شده‌اند؛ همچنین مقایسه کرد که در دوران رؤسای جمهور قبلی این کشتی ها روی آب بودن ولی الان کف دریان.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/73174" target="_blank">📅 20:12 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73173">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7da0f71e2.mp4?token=NzQso5QNuirq-ygiRC8dB3-vJWSTEMTb3xyt6A6G2FfLi-rvJCtWr48Ifx3AftMCREQpFVCfjEiElv5PB-3yS0LRyQ-_TvoAooPk9PBmJ3LpKVau3YnnPnQH-UZo3Eo56XdZmTCYylRVqvonNlBr1h7vSUo0-mSU6MBTbCyPqy7JON0gmhfKMkcMmXE-2zdYOx3QDxCKZsCCymaP5jlpCYDydjdRPoJrgmYt1k2sNTxPbEuJbCqo0JiuIPtA1hDoAwaYCaY6BRO0r86dHuriKrXs14I3SpHfq0hCUkE5RWcoxVAi3QL6WFfo2YcHAk5_uRhzH1cURkw_1YB-mx8MUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7da0f71e2.mp4?token=NzQso5QNuirq-ygiRC8dB3-vJWSTEMTb3xyt6A6G2FfLi-rvJCtWr48Ifx3AftMCREQpFVCfjEiElv5PB-3yS0LRyQ-_TvoAooPk9PBmJ3LpKVau3YnnPnQH-UZo3Eo56XdZmTCYylRVqvonNlBr1h7vSUo0-mSU6MBTbCyPqy7JON0gmhfKMkcMmXE-2zdYOx3QDxCKZsCCymaP5jlpCYDydjdRPoJrgmYt1k2sNTxPbEuJbCqo0JiuIPtA1hDoAwaYCaY6BRO0r86dHuriKrXs14I3SpHfq0hCUkE5RWcoxVAi3QL6WFfo2YcHAk5_uRhzH1cURkw_1YB-mx8MUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه سرباز روس تو خط مقدم، سربازای اوکراینی رو که از پله‌ها بالا می‌اومدن، با نیروهای خودی اشتباه گرفت!
وقتی اوکراینی‌ها به سمتش تیراندازی کردن، تازه متوجه اشتباهش شد و درگیری از فاصله نزدیک بینشون شروع شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/73173" target="_blank">📅 19:32 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73172">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8047543035.mp4?token=jwA5dncdR-rJpjxPhrxwe4cfWF7O2lQnLHHt1qqCVciWZkxFWOxNsTUbAuS8oAJGIocrAWa6XN7axQajFllMi-rJ4BG7thaflE4EGgvy9irNH9AvdsXxjFOJyzON9-di1Wf-7ngrtB82WAmsNkq83SSz6G_eRoFb4KXPSjQ_j-4k5ioKWCunbMoPoOQgWd6Ygm-_DGQCjQQtp_1Z3N7WVUI_vAoshDM8r33qHyTVOpGyWKm1QkyPLmXnkwTnRabbwj18WpSrVw6kdCcmb9bJSpYpZBH3EpUw_IcJbykLnoR7ByhSvc0RdyQOYPvxWJiON_9Em8DjoHSPYL3I5pUx0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8047543035.mp4?token=jwA5dncdR-rJpjxPhrxwe4cfWF7O2lQnLHHt1qqCVciWZkxFWOxNsTUbAuS8oAJGIocrAWa6XN7axQajFllMi-rJ4BG7thaflE4EGgvy9irNH9AvdsXxjFOJyzON9-di1Wf-7ngrtB82WAmsNkq83SSz6G_eRoFb4KXPSjQ_j-4k5ioKWCunbMoPoOQgWd6Ygm-_DGQCjQQtp_1Z3N7WVUI_vAoshDM8r33qHyTVOpGyWKm1QkyPLmXnkwTnRabbwj18WpSrVw6kdCcmb9bJSpYpZBH3EpUw_IcJbykLnoR7ByhSvc0RdyQOYPvxWJiON_9Em8DjoHSPYL3I5pUx0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش علیرضا خمسه به کلیپ معروفش توی فضای مجازی(خلوت کنید آقای خمسس...) :
منم مثل همه شما یه آدم معمولیم. صبحا میرم پارک پیاده‌روی، بعدش میرم نون میگیریم و ...
بخدا من بادیگارد ندارم چرا به من فحش میدین؟
چرا به اون جلوییم که اون جمله رو داشت میگفت فحش نمیدین؟
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/73172" target="_blank">📅 19:26 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73171">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/73171" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/73171" target="_blank">📅 19:26 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73170">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lrqFPV6bIzj8wiGCkq0zQy8ASdqBWDWYm45fsKmUgwKC7ltDkOdADqd_ydt4A3UZevV5IKdo1vpYLvz7-zXRyxq4rSUgPB0ArlAMZvlHSo2jeHYiqiaG-YQu_5SMNBc1MVp6hb3wFFYGhKw568UaVBpd5k47ODjrVaS3nACDs7sYvwVs_9LSkLPRHylvE1ofKYyHUDo3d_3ruc3a541P7CELYEAGymNyq90dYFpfQxpVDwnCVIAzobC9cWGpPm_3iSFUyCIZO2tMyRRPXBpm9h6ARBmhb5ne00lW-EZGiMdNIrnFyGlthugEtlufuTPUWZUGeJQRQdQsGxljHFifBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد هیجان انگیز استقلال
🆚
الغرافه رو در
TrexBet
از دست نده!
📉
نگاهی به آمار ۲ تیم در ۵ رویارویی اخیر:
استقلال: ۲ برد، ۳ تساوی و ۶ گل زده
الغرافه: ۱ برد، ۱ تساوی، ۳ شکست و ۶ گل زده
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
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/73170" target="_blank">📅 19:26 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73169">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">#مهم
؛
اندی برنهام، نخست‌وزیر بریتانیا، می‌گوید می‌تواند تأیید کند که حادثه پایگاه «آر.ای.اف فیرفورد» (RAF Fairford) «تقریباً به‌طور قطع» توسط سپاه پاسداران انقلاب اسلامی ایران هدایت شده است.
من می‌توانم ارزیابی خود را مبنی بر اینکه این اقدام به احتمال بسیار زیاد در ایران هماهنگ شده و تقریباً به‌طور قطع توسط سپاه پاسداران انقلاب اسلامی ایران هدایت شده است، تأیید کنم.
ما این تهدیدات را در خاک خود تحمل نخواهیم کرد. ما با استفاده از تمام اختیارات قانونی خود برای هدف قرار دادن شبکه‌های جنایتکار مورد استفاده ایران و همچنین منابع مالی آن‌ها، با این اقدامات به‌شدت مقابله خواهیم کرد.
ما تحریم‌های بیشتری را برای محدود کردن توانایی ایران و سپاه پاسداران در آسیب رساندن به خودمان اعمال خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/73169" target="_blank">📅 18:40 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73168">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50742ac121.mp4?token=lki7gfxMKuV8vemOJq39-nVlY_1fVKaQ0LXn0afw2qIXvxrC9vpn-8U5P_F1iIYr7dd5Cx3XzRjpmQqq41lUMhzsZ_sz5IeTPUsLHdRqRoQLNk7m3eMYq622ihIiGWDmVxQYZWLQUD-UQiJVqzN74wLsUQoQeNHfLHUTV4jyBvGqHkxBtlIr9PLlhXiHsMNg4xvIOADvqD-dW57LIvABk_93-hacJNKyRkzYveycASFfTu8_3U6SwlMn33h-CE5oJOx2N4U5N3an0p9Ggr5Djv9EHQOpPBbfrbaSYZp0RYec0rvpX8EUaiv5pLPPBuGev6oGE625nRzX9FXGChqfZnZLCSMcDE6pYGV3BEEc7KhVxTO16w0IlPbvzspZlGrDsKmRt-Yn_x0dn8sWHdWER_Sbxhylbq02aayxqFmJW5_AW7xyZYXCOAB3NvYH0EBitTx7Wqe-g1sxtFHb5FSDz9CvWazi3vQmbvMAX6feIWqxNhpBGu8p8jiXy4wPUxfKub24aHIupH6tXGDOCFUj9xxKv2eGGoCPlKU5UiZZKp9ZP0ZPbyi4d1hah91xhi0MYQIcxnRshPrKBks6Cy-ZrS6XA-9hrT-imhGaDY22IMkv9N9-C_o9VTfvh2-g3cw1uxE0jCd0Rq6fughFTpxr_xBqEW1lFbV8Rsm-nZB77Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50742ac121.mp4?token=lki7gfxMKuV8vemOJq39-nVlY_1fVKaQ0LXn0afw2qIXvxrC9vpn-8U5P_F1iIYr7dd5Cx3XzRjpmQqq41lUMhzsZ_sz5IeTPUsLHdRqRoQLNk7m3eMYq622ihIiGWDmVxQYZWLQUD-UQiJVqzN74wLsUQoQeNHfLHUTV4jyBvGqHkxBtlIr9PLlhXiHsMNg4xvIOADvqD-dW57LIvABk_93-hacJNKyRkzYveycASFfTu8_3U6SwlMn33h-CE5oJOx2N4U5N3an0p9Ggr5Djv9EHQOpPBbfrbaSYZp0RYec0rvpX8EUaiv5pLPPBuGev6oGE625nRzX9FXGChqfZnZLCSMcDE6pYGV3BEEc7KhVxTO16w0IlPbvzspZlGrDsKmRt-Yn_x0dn8sWHdWER_Sbxhylbq02aayxqFmJW5_AW7xyZYXCOAB3NvYH0EBitTx7Wqe-g1sxtFHb5FSDz9CvWazi3vQmbvMAX6feIWqxNhpBGu8p8jiXy4wPUxfKub24aHIupH6tXGDOCFUj9xxKv2eGGoCPlKU5UiZZKp9ZP0ZPbyi4d1hah91xhi0MYQIcxnRshPrKBks6Cy-ZrS6XA-9hrT-imhGaDY22IMkv9N9-C_o9VTfvh2-g3cw1uxE0jCd0Rq6fughFTpxr_xBqEW1lFbV8Rsm-nZB77Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوووری
؛ اندی برنهام نخست‌وزیر بریتانیا می‌گوید می‌تواند تأیید کند که حادثه تروریستی در پایگاه نیروی هوایی سلطنتی «فیرفورد» «تقریباً به‌طور قطع» توسط سپاه پاسداران انقلاب اسلامی ایران هدایت شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/73168" target="_blank">📅 18:24 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73167">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/294900b4d0.mp4?token=vOp9LL23rhUJnNSG_HIIQa2fIEAo6qtAdN6-a4MPHvE4KvrorZlxEknU8_vhWTYEsJmyWjiR2MFpe1hyxcllPp2VOxrqc4zZQgfNsIxREONCErdzsxE6o4jwhQhqRN9akS8XRW_RuOaJa9u-efd_hUVBo6nblzExAaL2e5ugnrxT9m161Ho1L1fjTfCPXXZeAmS76bIRsduFGjsCRa_foXgdG-9y-erR369jK3Ik9CZfQuwGNs1X7qtJQ4jjoWoCeh9ExK8zTtnoDQ-SlkDgNCKqGx8_9K4gl3qsS-bMpxRT_A_TR4nBQYMQEu4wWPb61Qry_HlhuTXgbExJjsrvWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/294900b4d0.mp4?token=vOp9LL23rhUJnNSG_HIIQa2fIEAo6qtAdN6-a4MPHvE4KvrorZlxEknU8_vhWTYEsJmyWjiR2MFpe1hyxcllPp2VOxrqc4zZQgfNsIxREONCErdzsxE6o4jwhQhqRN9akS8XRW_RuOaJa9u-efd_hUVBo6nblzExAaL2e5ugnrxT9m161Ho1L1fjTfCPXXZeAmS76bIRsduFGjsCRa_foXgdG-9y-erR369jK3Ik9CZfQuwGNs1X7qtJQ4jjoWoCeh9ExK8zTtnoDQ-SlkDgNCKqGx8_9K4gl3qsS-bMpxRT_A_TR4nBQYMQEu4wWPb61Qry_HlhuTXgbExJjsrvWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروی دریایی سپاه پاسداران اعلام کرد که طی دو روز گذشته به سومین سوپر نفتکش در تنگه هرمز حمله کرده و موجب آتش‌سوزی آن شده است.
سپاه پاسداران اعلام کرد که این نفتکش هنگام تلاش برای خروج غیرمجاز از تنگه، سامانه ناوبری خود را غیرفعال کرده و به هشدارهای مکرر بی‌توجهی کرده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/73167" target="_blank">📅 18:02 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73164">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bHx95P0CGTN9x5DDB7fWchWCyjzsWpcknhnQWNNA49GrxKXQgxSRLUaZ_8kXG7CvNwuVZsyalCXOVFLlYEV4uZJuhnR4IogxsLKTHRtqIu3UBbVSgGXz_5Ptt4JaovrlCsgcH10jBMOrP1qgv3tU9g5B5jGy1c8pi7F71FjQrHU0ejJfsbU8QRpJYy35i80NwTO0ULKh0m4zxE-JVnIjXQchJkseMyyJMwHGCqgT3RYtXSrKFmTlrJrh73k5ZFEmfVc_ie1vvzRDUwirPUcnczMy3qwC1sDa6AETa5_VYjE4R5b-pYavW987Y2zOqWa8G7YEL5zF7bjo9Zx4Y1lfcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HiPs1fTiAqIVDV6-P-3jcZoOIrrvNFZIP8VBUv6JmCR1aV17dlpE2sHqCEZx_j00ZjYMIyTj4V827v_gIcvsWMTCqypYPHno7sRnFhpgZwS0i29pYVzjqE80tV9JjK0aD8ExTc09LRrZvEhgwLEGvHHzRuplMKysaiP5RaJX21t0lo5293zoPR7lZfzDUK-HbalNYSv1xXJRT9VNXY581g5k6ggnzsCm2bg7z353k40UxpGd4wXLKnP89uxXIXY7qrLGBSGKonzME2TjIuSMH5CSS-jDSI5vBJKIj4c-0sfMiChRFl6KaOJxGFvoyEYRw9k_xtyEv4S6PsiqG0LKoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WgdyVzVbdfHgssGmQJaQpeiwuQqiQ42qSJRpvsqSVL2xzbpEG4P6DWEMz1QbrKNBz5ir9JjwY58YHnpTWQ9NHqOvJZOUtWBoc_fc8zmS30anfDI21TlAFjQsu2fosLFbxgqYfAYzUJFeA26Jn-p-XdkX6T-2pHR8uCr4-CibSiaJdzCLku-3-6UTEgkqhJ4SMl3IVnzgoI-Xsw_lictjidR09MopluZJP8kepgYvDVV7oi-h3dsNcDZHvMQjiQpTVxGOlFFYv1I7dPmPqRsLwMC-s74TNUtv-ZWlAXo4koLvIflkhgy7tnBD2WxBwaX_0JpFWFEnMjUANvrxMVdVyA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آزمایش موشکی سپاه در یزد:
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/73164" target="_blank">📅 17:20 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73163">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b1f4cc034.mp4?token=a7nI2bJqz1P9xXjkvhBNJm3KGRRfNKxVX0jXdLartJWuNXsX1WmLbbk6GsZxBZ_82cmH4kepLsl_kaMgB81m_Gc1oRhXAwj9V8RNPzmHyBZCXHJxxoH-UlbcfT9oLvVSF9FXUXGbZ-qemLTQbwDwWtltzRl8DVeZL4XZoai1yzy9I5_oZGh4BpqDfkEdQYzGIiMoc4QVQtBfJ5JmYLLiK56aaBsmkluMZC3GzMf9JjCmObOXu6er7kX4Vn4pKOgf58p7FWFG-hHjO_X5K7kPteQ9lOwLJX2RC1DP31m9xfGRi5nHWk8QUphY0ZIaNCtq3uuOYHNYLRooH_GPkldJfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b1f4cc034.mp4?token=a7nI2bJqz1P9xXjkvhBNJm3KGRRfNKxVX0jXdLartJWuNXsX1WmLbbk6GsZxBZ_82cmH4kepLsl_kaMgB81m_Gc1oRhXAwj9V8RNPzmHyBZCXHJxxoH-UlbcfT9oLvVSF9FXUXGbZ-qemLTQbwDwWtltzRl8DVeZL4XZoai1yzy9I5_oZGh4BpqDfkEdQYzGIiMoc4QVQtBfJ5JmYLLiK56aaBsmkluMZC3GzMf9JjCmObOXu6er7kX4Vn4pKOgf58p7FWFG-hHjO_X5K7kPteQ9lOwLJX2RC1DP31m9xfGRi5nHWk8QUphY0ZIaNCtq3uuOYHNYLRooH_GPkldJfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی از اولین اصابت و انفجار ها روز ۹ اسفند در پایگاه سوم نیروی دریایی ارتش، کنارک
؛
در این ویدیو ، یکی از پرسنل که به ناچار و طی غافلگیری به اطراف پایگاه همراه با هم رزمان خود پناه برده بود، می‌گوید ،"جایی نداریم ،فعلا همین جا بمانیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/73163" target="_blank">📅 17:04 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73162">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/73162" target="_blank">📅 17:04 · 20 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
