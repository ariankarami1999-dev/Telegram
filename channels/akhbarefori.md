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
<img src="https://cdn4.telesco.pe/file/jnNIBoT0Zvav2-BPdLDskPicgRxBGg7VWJoqBzldU211QotPy8A9gfirYGFhBk2l51Pi6UojckdgLcPTG6Ru1nqPvIL8LlB3fvxj2D62At4rv3LcmA1JqiHa4gAAPRrdYCJ8bpANAuq7SIs0sLq6FzkJbRA5kxv58tblGhXzHBGjKr6P9_fxDyKF59MHVJaUmaTEANgNEkt1LMY7RjAV0HWNkcJaDN4hZkUpTenMEUd0oDfYAIGGQszpXP517msD42nVlFPdAEgbIhh35R8iP3wXiMrclyWPKBnmfggslqXmoAGLqOHqXsAUWTbEpnS-q34s-JpxZHuqkAfSUUUTOA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.12M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-24 23:14:42</div>
<hr>

<div class="tg-post" id="msg-690248">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/566a2e474c.mp4?token=RToxW8G06G7QTbyZcVIWCXicwrBhA-GY1_-qKO1anVDiWC7O8XpB5lNvQWEgf8LZqM2qQrQQqr0XfB7w9AfXbiS__tMWXJTl2Nm94C2IvotXfAEbhx2z5Q_p78i8vPevXRKF6fI9BBawoklJkooH238hQqt1PSvPWZjom__sP_gyB6_SIVMn3Aquj1QxnYQEW5l3zc7EAvLrwTaFsPppEuz1py1DAcQB65FEuXjW5wDbUS2_dT1oiK1OYhR-eFfK8ot2R5p8LuTCR9ax6K-vfJ6dhZiQvd5LFzBoH5tPeDT7_YzOFgSjk-8xOBGm-G1amypsg5Tn1rEncKhxc9JAig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/566a2e474c.mp4?token=RToxW8G06G7QTbyZcVIWCXicwrBhA-GY1_-qKO1anVDiWC7O8XpB5lNvQWEgf8LZqM2qQrQQqr0XfB7w9AfXbiS__tMWXJTl2Nm94C2IvotXfAEbhx2z5Q_p78i8vPevXRKF6fI9BBawoklJkooH238hQqt1PSvPWZjom__sP_gyB6_SIVMn3Aquj1QxnYQEW5l3zc7EAvLrwTaFsPppEuz1py1DAcQB65FEuXjW5wDbUS2_dT1oiK1OYhR-eFfK8ot2R5p8LuTCR9ax6K-vfJ6dhZiQvd5LFzBoH5tPeDT7_YzOFgSjk-8xOBGm-G1amypsg5Tn1rEncKhxc9JAig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دوران طلایی نوکیا؛ زمانی که هر ایده‌ای می‌تونست تبدیل به یک گوشی متفاوت بشه
📱
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2 · <a href="https://t.me/akhbarefori/690248" target="_blank">📅 23:14 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690246">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/955fbe362f.mp4?token=t7ugcdHvL09KlW8NiIUPoXc8deumSWVrKuKZZd3ChqjcLS8Y95lozTO_6UlSr2lTUhw_vjXk5KivUz1ECVuG7ohtze1m19ChzZ9qE4MmTapWGizfWQonweHIagAQXGo9UAPw6Pd4cdbzfWkpP192kfOd0Sz7O5WhYPgu8Ut3iZIv4DYhBFDG3Cv24WsR-LLFaiO0XUdsRJUAw_CgQ69IliUAMZlI-RGXzpuGpPfoHy0H49_Hcop0d_bvsUMAKcpNUvMVWI-I1CO0A7aqHwxJmEXBq09bS1p5VjXwppYn_pAEk3YgZ5skmQbQnYzX4U0pXnAXgFLaGZBUE47GAXh9Dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/955fbe362f.mp4?token=t7ugcdHvL09KlW8NiIUPoXc8deumSWVrKuKZZd3ChqjcLS8Y95lozTO_6UlSr2lTUhw_vjXk5KivUz1ECVuG7ohtze1m19ChzZ9qE4MmTapWGizfWQonweHIagAQXGo9UAPw6Pd4cdbzfWkpP192kfOd0Sz7O5WhYPgu8Ut3iZIv4DYhBFDG3Cv24WsR-LLFaiO0XUdsRJUAw_CgQ69IliUAMZlI-RGXzpuGpPfoHy0H49_Hcop0d_bvsUMAKcpNUvMVWI-I1CO0A7aqHwxJmEXBq09bS1p5VjXwppYn_pAEk3YgZ5skmQbQnYzX4U0pXnAXgFLaGZBUE47GAXh9Dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کلاهبرداری از پزشک سابق استقلال؛ پیش از سفر به عربستان با استقلال ۳ نفر با یک وکالت‌نامه تمام زندگی‌ام را نابود کردند!
/ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/akhbarefori/690246" target="_blank">📅 23:06 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690245">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cGOdyEvkGe9JIRsWQ5Lhv9PtYTYdvSAoTPjl69LpUCCWnNBCYYdJh58Yx3v06AZTDPn1R5G3QHmli2j1vNGcoMmr1TmSpKWQkzaGt4tNvYJRJC9hFw_jQ1v0cZKCXgSb-36PM0T2Qt1j4gLiWByXm1IaTTDB9Wl2rHYC4u2JFVkMa43Fo5nAaDHGH5MvSAs6w25Zw-s9oFB640Z9nWpehHaY4_jq0vXTFBGwStoqwjDPILe3SeeBTJU98Mzg7y0qR1FoVDxMgYeo5fHCCjBaTjcEfPhcECh-JxInsl6zHpZfB2IF3L-yKc5_OTQJEHQBu6zGMSRmWy2R3mn9EiahBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طبق گزارش شرکت دریایی Vortexa: عربستان سعودی از روز شنبه هیچ نفتی از طریق بنادر دریای سرخ صادر نکرده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.09K · <a href="https://t.me/akhbarefori/690245" target="_blank">📅 23:01 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690244">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
حملات موشکی یمن به جنوب عربستان
🔹
منابع عربی از فعال‌شدن آژیرهای خطر و شنیده‌شدن صدای انفجار در منطقه‌های جیزان و ابها در عربستان سعودی خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/akhbarefori/690244" target="_blank">📅 22:58 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690243">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UsYDyOr3h6i6acEPRQwFoWBqkpg3gx3yTeunSjLA0KVYvgM8YNTRq8OJp_6t3Jwgzpmu3KsF8j1Ep15Ah1AjyprbxTKW2Hi8XbhCMnoVYVg-rvtilFC7McFZCqBm1sR8qmx0Y8ihDEYHVE-3gBK5EaPPs96yKY_NDamOjiuVMvrnmEQBGhLi08QOyfBOGETyUT99lq_gptWV6RnqDGQENvThwVrTjKbnm31HjoK3Er0Xufy6yGE9sXtLEvxX2-oPptf54tgtQqoFftqc6QF9pu_T-t_4I9XuxjrfIiB-6SwFyBwC8TsX7xqMCqFfqFaKcM2cKz7v2ygKRPBWOJ98kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رویترز: بارگیری نفت در بندر اصلی ینبع که در دریای سرخ واقع در عربستان سعودی قرار دارد، متوقف شده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/akhbarefori/690243" target="_blank">📅 22:57 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690242">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/908b07ec94.mp4?token=TQg4QQVzis7XTeNnMNgyyd1usfHGOPspTPyI2znQpSnJdERqkL12y0Ke79WTsC0HGaHOZ3JWq5hfANhAWnrXOMsUPZWKkLCnWN2bkNQW0Er4ZiDQu11kPSC_il55pLLLf0LBqkGwi793_-5mlL-ocrlYYgkEiP42pjGiXucyGI8zVwPXkjsXF6helrhVfSi6XExdl_zBCwR4KRnU1CbJduRCh37oi-uSb9_ufHy9do7rzBd06Iu7z8ada1d3dPPEr14yiiS6-oNozin3FSfvoxteqDH7CtkEEWV4VpWAiwjo0TJmdMy4KHaiUcqzAUzYiw6UGDh708R9ER2VAZ0VxL2WFUr0XBLaWP876BgdYpLBHVaQOkiGki-XJPF6RgbFdUwPXx1jy6ILvuoQ7r20KUUcnQXS4ZW5tS1KE6BfBDfi0HBWMLi4H9w7pb5QyX9UZ6E1YW4uXViG4BP39IoyI3yd8CEpCCTSUCTGFLZk7F9o0ZqP9F64r6FTvx60O47JI8G59ebZ-uU8JP3zBaufRJB6GtP0pNTN4s1uhbgoxJAbbJGidDbm-LTBsrlhUkjRYUlTtWdLMMKUb7Ry0iZMCIQUdMREAoDfGD06tACaiY8E2VRQf8gI1ITPJsvKVGoI1JIp96Cip7GpImSBavp2PFDdWG_UJ5pLwo9oNOgQ0pI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/908b07ec94.mp4?token=TQg4QQVzis7XTeNnMNgyyd1usfHGOPspTPyI2znQpSnJdERqkL12y0Ke79WTsC0HGaHOZ3JWq5hfANhAWnrXOMsUPZWKkLCnWN2bkNQW0Er4ZiDQu11kPSC_il55pLLLf0LBqkGwi793_-5mlL-ocrlYYgkEiP42pjGiXucyGI8zVwPXkjsXF6helrhVfSi6XExdl_zBCwR4KRnU1CbJduRCh37oi-uSb9_ufHy9do7rzBd06Iu7z8ada1d3dPPEr14yiiS6-oNozin3FSfvoxteqDH7CtkEEWV4VpWAiwjo0TJmdMy4KHaiUcqzAUzYiw6UGDh708R9ER2VAZ0VxL2WFUr0XBLaWP876BgdYpLBHVaQOkiGki-XJPF6RgbFdUwPXx1jy6ILvuoQ7r20KUUcnQXS4ZW5tS1KE6BfBDfi0HBWMLi4H9w7pb5QyX9UZ6E1YW4uXViG4BP39IoyI3yd8CEpCCTSUCTGFLZk7F9o0ZqP9F64r6FTvx60O47JI8G59ebZ-uU8JP3zBaufRJB6GtP0pNTN4s1uhbgoxJAbbJGidDbm-LTBsrlhUkjRYUlTtWdLMMKUb7Ry0iZMCIQUdMREAoDfGD06tACaiY8E2VRQf8gI1ITPJsvKVGoI1JIp96Cip7GpImSBavp2PFDdWG_UJ5pLwo9oNOgQ0pI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
علیرضا دبیر: شبکه صهیونیستی و دوزاری ایران اینترنشنال بداند که من اهل باج دادن به هیچکس نیستم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/690242" target="_blank">📅 22:53 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690232">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Eb4nKCNuoWeZAWfY5b0YU0Lnre5WxXKCQgSO-MNBEajGMl94zHafmwIIxHX6lLmMTrmc16hGhrRhPKcundwcyG3aB5HcRwR6BJTMrQ98IKG9O1eqBF3fFP2Hrbx1d67bgMp8Wftm61zUmQhvm_XxYwEVcoTtvk7FfhLEk23BtLHPrbHAHTV_MltvXiNZVwtNsOrj95bBpMs6osZKp27HG00EHy4YfEIrl0Ztd8eJciMEy8y0J6lJrHHnOxypHM9TPhJnFQCoAazsQK34bqf1ZLCOH5xg_Eqge2KmaRRsZfEZah7ExvKQJyUh7j6scE-JFf_Pu9c4EHMe7I3kauZxpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qh1_VxX1LThttFG-GVp9eZAdV607bAvKebFEkHuKW9gRvHzxXnRzWCypub_qG6im0PX6zC4iUJT6HVxRQh395t-na1MzI-3pdKyiHpop8o1jtuZ_N_qeFsGcG9Y6HxTOtgEnKM9ALkle0GHl5Cq0tyu3sBlyCm-Yy3wJUMps5MkLN03o7yC9bZiDLSiXuWavsA6KXzsaIER02HMVIjUYQHz6aixIagDVmlmTJYhzjIxejJMjaKyJ-qiSRFPlNBpxXPbJ-o0YO32HrYy4NkRpihtqWVuVaEkm1yJokYsg_WPCLIctgsNdHWwZj4xIn0zzgBT2_ZYjvSy8uqy2KtKwUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oF52vjeMfQXyA5nlMy8RF5-SasfDoLvIKPTm70HuxfEkOCk-RRbUH3Zw_UqG5NawBHi7iBozm0TGHpfG29JxUPtn41e7lABFS25mhSZD8fjuEzf1uJIn8IBVq8u0PhBANF3F_Q41vIawv_Qz33-7BDyOK9-ddOFcTco3T3cveNZVH8mY5Sw820FfD6O3oq5GpTioxjc08e2CPvxxerDlzs0fdVIdzMzpQ411fattSvZxrwgB6HBKpaeMpprr0zdO7B3s2DGKm0DEEw0_iGHT43q3ST2ChjGrDB0W0aTmvMy_UEB1k0OIVEGepl0bZfKyxO1rob24Vf4uH-UU398uKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UI9HcLkyzBLoLMO6t7Fwp2mLoAYRkFlk4TlplCIVg2LeF2OGB5czhVvExvvVbrnQSRDkAOddBxLmrHVKcKLEHgB_B4nmF6W7jirDtdRbua9FuXOvB5Vv4p5kuNUAz3I3VnsJydJsXVHnSYKTqh3HhDtkXyVDHnZwkw9wSlwq9wZDwvKr3yZkmPilR9wE73pc9jMnI_sO2G1Wq9s05SANFEBwdbGEp0sD4CxeV0ZGLDSvCktxd8Tg_ILCkdWl4eByYrDyJ9Wfh_WM0cohKIUIDxGsIAv3lT8kZMxEoLr390658fhH5LAMl-Ydom4Y3ekoCNGv9egGnHOL8nwfxohc3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EvQwQmYfNbCXNiEFcOUYQi-LPM8OJdnj9UcABtI6t19xuJ-ySElNGNVgHv6b-W0oPKwTqFYbjTLWwWX18h2rxIfNA3k9MCkHo7H0qjp3wFYenE3ZgtAO4B26JqbP9T9ZfuavQnKWnYvz-NBfHZf_fOIpX0uaDpYfVOjN-TxYmgmaibq7_YxGY_KiMLh1krY3DAaFKjvca4m9MYUHrJ0z7eJwDf-LGIprQol0g-LUlIz7gy-ZQd6N4bIU71MOupsA2zxjuorTH223Aqjqq1f40WNWyziOlJXYUBtbdoSl1E-8jgnoehX59OJJJ1f1sWkrmp1fwJOO2P5uoIhh-wT4NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BE4f2wlBXQ8rOT8ofvoFJisDPxt1XpQ39JQ6cIJNWWcoQNuiplvF0GV6tx91vCjuU16-fPyikw7lhlxSZOgFuNakSniMVFuuQ4ee0hLPqUV29TFnQ63GrlEDv7PGm83ElI3RFslBgkeZvcfLrP6tcEW8onukAVpM0dIgb5nlwiB5SkyjCcIamNA7GpKLc0W8TqausGiH-fPhyG8q2KNnN35Bb0Y91i2XMc1chM4DMlL8yQ5CNBdzkgLyIMEnmQFWXQhZXTIb87MSsnFnF2wx4x1Hy-rdATitFdYa-xk4COnN1gcdopyfgx4M98j44t7o-oiC46pYogpqwuH43LN-fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NX4DVg2Zp3qaZBxFW7WKVUPzWu4W2tLd0iWOZxzIiKEbfgcmaKjhdM_r-7no6QDa8jI3yrX3JhGfKQTF73Uk1hWm2ULmGatHW-tXhfnNjtO0bLN__H96JihX0YUl1XrzMXdLbt1e1JOTvA5ZLNPOZcKr8rl2WsPH3nNbNsSYDWAAdpDUAMbnBftDr6BRwKoZAhsKtCA05CPbnHMyQ4-Ni4cjvpYucgIXbWZalMdkQxVKW1S_SGi7lCb_ef7mWTVmoeXsxNOSpHq6pVmSmpiaC9Thq3ePU_ddSdMkgOSj3Hpv8qRvFs8OJkYb_T3p1xmSDVX4Juh5zmpQ3_YQDu_2Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qxEZex-Eth64kQ0Ra2iLzGpd37g_fZtKfC4Zplf-oHY0JTexii5uXY498NLQf8oKt-9wj7vAzJYp8Y2N1lUhp2Zn5pZxRScHXGR6ieqllAsdonh2p5673jT9Id26osxQPq-L6rW1Qh8vrqAjpJBng_Xn3MkaM9VPJc310Qr-i_vHluNXZ07EsG2dUwzDXbu2vz52gbPM8pKOeSkN4SRNSKGWH48RzromsFyOfpwanoSzXKKBDdXsAYoCAz_LNHWYpTapSxnqIVS2mSAQGlWbCY3rztiB2LCizQidetU3lHu2Z1AAJRqd5u0yRNIPslgO3GlLDAZoZYVak8IfXp86Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CUVBFa-hZ6RtNtINKESsrD8q4FmG476f5uVSrBhxypKiptbtXNqqREXtbng66daPCbnUqves3hbX-KAEySo6m4ksDf6AWrpMMZNGgN1NPJxuFmHYTiDcxyTugoAu6NUzELRN7ic8ygVRY5eGf3juEDBB_fJDXRNR0RXwYEyDNZ-16oe90gDTWW7yhIe5mbNGBqaDCQDgsPOqEsezA5y7pId4JOnLjvKHU2u5aWBhXBS9oNEN9Zl6XFzHnZjNMi6t0Xa35rLwKi_QZAqehWsg62EndqUzITmKDKh4krFmjLTUsV0GGbO7AK1u_fKX9p19VrJvhwl4bcZMquyn99O5zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dxD74u7aaN0Mpj6XO5W6xMwu60kxkaH7CvhxhdPVK_5QvYLu2ttJMPaJR_8fjTzHcfykheUQ1zcdwhKTSyI9k8s6mtBqmcP5s8U9K6wTTLS-eyyLotrA_HKgPUqcPkF7yAFCe-D35P8p1cM8hj5EPzCAvElCA9Sm5DFUpK1AlVRF8sr76ZHp84mH0SQKf2Z2wDRSnnvo-X068e6BScK1JcWN-17P-Y6DjLjpNEhCocPYNr3WnkTn2hXx04-6uwPw-yFFuPWAGiV6oALADmmAJDqyfVITTGXv19573qESn6pI9BIryzFQbzeO3m3WUmgahWHFqWKyjoZrJRK8wEBGPA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
درد دارو
🔹
روایت مخاطبین از گرانی، کمبود و جست‌وجوی بی‌پایان برای تهیه دارو.
🔸
در چند خط  روایت خود را همراه با نام، شهر و نام دارو برای ما ارسال کنید
👇
#درد_دارو
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/690232" target="_blank">📅 22:50 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690231">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
حملات موشکی یمن به جنوب عربستان
🔹
منابع عربی از فعال‌شدن آژیرهای خطر و شنیده‌شدن صدای انفجار در منطقه‌های جیزان و ابها در عربستان سعودی خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/690231" target="_blank">📅 22:44 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690230">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AeMJafpcrlAIzspDHED-OHC7sfT-RNpQsaRF-VRV9AARdC4_G3R7-wYo0h2Sxo1TYuvzp3ISivK4Vuy74x19j_rBGdBAYTnue6XbI4pHxS-dl9_y4nXJMOdD-EbAP7VUg2tBBzkc1Wcsx3B2PxBh2EnK_yMiw_NcYlUwYo6QQ-t_TN_n9QqE9b6mQ42dLHZ6Pg0-JRIF1DsdFQHl6uqItkLslHF2XpgF6J9s2IldHhspyygNhJb7WelUl9070XG_DrmmAU45Vv8GO7BykaBN27H_-e6NnInb0KKjVnR3yW3A0GyVnd24tYAhItcbrQmaNOB-XyRHoN1oNUXTQ5ZnGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روزنامه‌نگار انگلیسی: آماده باشید برای جهش دوباره قیمت‌های سوخت
🔹
حمله جدید حوثی‌ها به پالایشگاه ۴۰۰,۰۰۰ بشکه‌ای آرامکو - سینوپک در انتهای دریای سرخ، آخرین کریدور نفت خام عربستان سعودی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/690230" target="_blank">📅 22:38 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690229">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o78vlt4fHaFlNfLRFX-5l3rYKFz2HQIONKdEWEKpabBiE07WkaM2z1-qtYlsb3eTI5RfMYfUvyx1BCVHcalV5oK8hyH3V-g5zT-c9BO35SO2ba1D730bmzsiPOYOGHMoUC79JcKCszlMkdc6FD5-Rm1ZWkQNkDMsrY6KbA5jugv-dF1AMlvss8oMp6E1KUydBoBKzkj8dt9eifHKnnf1Us27uJo3EpXJPy_gL124iXO4POi6k_husVCj_Vp9ez-vOFZ6MwPKY1rHuT2PM0mdc-V8FvYeDjyt0q2Y3hFdXVkEA8XamrIo-5p4kNqtv7XeQDY1HNYpC6m7kBLdkt9yFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
از شوگر ددی تا موساد؛ حرف‌های جنجالی امیر نوری | پولدارم، می‌خورم و می‌خوابم!
🔹
امیر نوری در گفت‌وگویی تازه با مجید واشقانی، از وضعیت مالی و دلیل ازدواج نکردنش گفت و درباره روابط عاطفی، حواشی «موساد» و فیلترینگ و حضور احتمالی‌اش در جنگ زمینی اظهاراتی خبرساز…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/690229" target="_blank">📅 22:33 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690228">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
چند روز حساس و سرنوشت‌ساز برای قیمت طلا
🔹
این هفته یکی از حساس‌ترین هفته‌ها برای طلا است؛ چند روز آینده مشخص می‌شود که طلای جهانی قرار است یک حرکت جدی دیگر داشته باشد یا وارد فاز اصلاح شود.
🔹
جزئیات را در این گزارش ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/akhbarefori/690228" target="_blank">📅 22:25 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690227">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13ca3e41fe.mp4?token=fVW1OLS5Qvjwq6uZLvNdPY3iV5wLt7Yx4C7oSyVJu1g7PEa3PeGYt5usQ7ypLOiJEdXosO2P-NZjW1C0tFXN6URsQ_ybzFFnqYCYvH9VL0FesdR-m_0h5c7VoDVLH0Eker_XpB5dpOO5pG_HlbU4o2XLmbOIeiqaqcwmkn9edTXjnZKd9omG1swPareO5ZxCLdfh6N08A3dB0WRtOzGHy3SxcXFw1arMsdtSRRCi3c5vdqlRM0pDRznbbo-_rmMUgPp4F7y60Te-STn8vIsj0k4l11IK6HVGI-rtwpd0aF81_7GloSpO3afRGHJigOcVcswurgpl4WbBxNnfj1p5Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13ca3e41fe.mp4?token=fVW1OLS5Qvjwq6uZLvNdPY3iV5wLt7Yx4C7oSyVJu1g7PEa3PeGYt5usQ7ypLOiJEdXosO2P-NZjW1C0tFXN6URsQ_ybzFFnqYCYvH9VL0FesdR-m_0h5c7VoDVLH0Eker_XpB5dpOO5pG_HlbU4o2XLmbOIeiqaqcwmkn9edTXjnZKd9omG1swPareO5ZxCLdfh6N08A3dB0WRtOzGHy3SxcXFw1arMsdtSRRCi3c5vdqlRM0pDRznbbo-_rmMUgPp4F7y60Te-STn8vIsj0k4l11IK6HVGI-rtwpd0aF81_7GloSpO3afRGHJigOcVcswurgpl4WbBxNnfj1p5Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یادش بخیر؛ سال‌هایی که بازگشایی مدارس، یکی از شیرین‌ترین اتفاق‌های سال بود
🎒
📚
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/akhbarefori/690227" target="_blank">📅 22:19 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690226">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XFirMzuEtgPnaHJI6B8X_TQl-xm9IFkXaFxp2vHiEjNh9VcUIRzVw4pymUYckw9hqY18SjahT8OE00hBOXGD-4By4w6likb-2Ve5NJj0c_vDIEVabcHyuhe4DcyIzK4WLGXnsWcW1IUEWE2SN3XSBPUw5UTiyJnbb0NFpxmWRTSUmlAuCJ4ADYJduJAousAOmUzgpHdpkhPZDKW_wIBEmWy2UKJMdxt8Yza7lUyVcVhsYDRd5bwRFtpKJO9-m3WvLTDJP2419HdJ27nDjqed2HideF13_44DPKHcLnvsTWBQCh2uOoDj19vYJkoHQNYyCNeYKiL3JQ9uXj2ou81OYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ویل شرایور، با کنایه به ترامپ: «ملت شکست‌خورده ایران» تمام پایگاه‌های اصلی آمریکا در منطقه خلیج‌فارس را درهم کوبیده است؛ پایگاه‌هایی که اکنون همگی غیرقابل‌دفاع هستند
🔹
ایران، همراه با متحدان منطقه‌ای خود، همچنین کنترل مؤثر سه گلوگاه راهبردی مهم جهان را به دست گرفته است: تنگه هرمز، باب‌المندب و کانال سوئز.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/akhbarefori/690226" target="_blank">📅 22:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690225">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WcpBJB7b84HjEkhY503nfGuK0NDXolpXc8Cuvf34oIHCQyiXvSDLJeF0y1q9QB0UcloAzVnHOIFV7RlOtzNHUx02ZkRMylJOIL9oVpalmz97z54w6PsV4rNz-l9u8ovAQskCZlYyILpHq2h2XpaD2TkUC4hPhpqzdCn_DRDQ-uuid66pncnrlLYpzuzraFmuS1hh4Yl0B8IL48xR604cchYkfoIQWzu6YKGgwOHcfVxxqmZUXvfVFDgFOr0dhVO9IcEP6guM5fy8FxOnsGTzpB6VeIr_tWulcxf9diLd476Jln4UR8wm0Und_Ybk7QsMrmuoNGWR4qKLPHaXPHsKZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت نفت خام شانگهای به رکورد ۱۳۵ دلار رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/690225" target="_blank">📅 22:07 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690224">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/akhbarefori/690224" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">گزارش بازارها سه شنبه ۲۴ شهریور ۱۴۰۵
بورس با تقاضا همراه بود
طلا اصلاح کرد
دلار در محدوده ۲۳۰
همه چشم انتظار جلسه فردا فدرال رزرو
@Titretejarat</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/akhbarefori/690224" target="_blank">📅 22:05 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690223">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbaab5618f.mp4?token=a_fjHbCqmcjhLgL5wV7q1TAM7U85-2vrcybcFvFXvRFoAo8LSJUwxte539iKMDoGZHp4VphNP3yR_DnFZXGf9N2ND2Wk0RbqqbEvIDhncT0-7ASkOdy0Ktxrk66rL1--Wcx_du8f-FH615zu1FyQ1gtjCPIKfD848V4d6SMTL6V4DoI0xgCRx-fDJ1iWixewO4Rou2q4D5FSq_BwGgzGqF28R3H8y2x--F4mAeRylqw_WgjM5WDEuH7MvEuNM_c-bKeaL2kog1piEYN-731AGA18XZl_Ygukz1zfSeVwGoC7xJVgMbJJ7Uc8Ar3U7lleaWu2KrlO5uN_8Lqku0RkiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbaab5618f.mp4?token=a_fjHbCqmcjhLgL5wV7q1TAM7U85-2vrcybcFvFXvRFoAo8LSJUwxte539iKMDoGZHp4VphNP3yR_DnFZXGf9N2ND2Wk0RbqqbEvIDhncT0-7ASkOdy0Ktxrk66rL1--Wcx_du8f-FH615zu1FyQ1gtjCPIKfD848V4d6SMTL6V4DoI0xgCRx-fDJ1iWixewO4Rou2q4D5FSq_BwGgzGqF28R3H8y2x--F4mAeRylqw_WgjM5WDEuH7MvEuNM_c-bKeaL2kog1piEYN-731AGA18XZl_Ygukz1zfSeVwGoC7xJVgMbJJ7Uc8Ar3U7lleaWu2KrlO5uN_8Lqku0RkiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اطلاعات تکمیلی سخنگوی ستاد مردمی پویش جانفدا از فراخوان آموزش و سازماندهی یگان‌های مردمی جانفدا
🔹
ساسان زارع: افرادی که پس تکمیل ظرفیت ثبت‌نام می‌کنند در لیست انتظار ذخیره و پس از هماهنگی با نیروهای مسلح سازماندهی خواهند شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/690223" target="_blank">📅 22:02 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690222">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3482a7dc19.mp4?token=YD8YDwyPJJkVRHonka8yMpuEyN4AgIfiVwUSr_YlJGeMFKpGMXXU02nWCymAGKknd7P8czC9wYY6nCUtXzaqsSmvl9UzlijEdYglPVFTSJx5euf8-9dnMiXmyXPnX9-fimydBcj5cfA8hSnT4sq2JC1h-S5VvMtuTOtzIyS9q8fnB3B4k62Y6aySBL2NuaTwvmkktpXhYbCJAJt9t4rSeoTmRj3ErKqWoX3Tk7tTfYlU4tCvz7oG4LA4ZajarXlbAVQnNhRIli_3VZC1i3-hJp7yQ2qS5OHeFQF7FBY4eP3jWjam9qMOBo1QTby2S6a-7SbumfpRtAlX-RE_8UWV9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3482a7dc19.mp4?token=YD8YDwyPJJkVRHonka8yMpuEyN4AgIfiVwUSr_YlJGeMFKpGMXXU02nWCymAGKknd7P8czC9wYY6nCUtXzaqsSmvl9UzlijEdYglPVFTSJx5euf8-9dnMiXmyXPnX9-fimydBcj5cfA8hSnT4sq2JC1h-S5VvMtuTOtzIyS9q8fnB3B4k62Y6aySBL2NuaTwvmkktpXhYbCJAJt9t4rSeoTmRj3ErKqWoX3Tk7tTfYlU4tCvz7oG4LA4ZajarXlbAVQnNhRIli_3VZC1i3-hJp7yQ2qS5OHeFQF7FBY4eP3jWjam9qMOBo1QTby2S6a-7SbumfpRtAlX-RE_8UWV9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آیا فرماندهان ما به وسیله واتس‌اپ ترور شدند؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/690222" target="_blank">📅 21:59 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690221">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
رییس سازمان نوسازی: بازسازی مدارس آسیب‌دیده، بدون استفاده از اعتبارات دولتی انجام شده است
حمیدرضا خان‌محمدی، معاون وزیر و رئیس سازمان نوسازی مدارس کشور در
#گفتگو
با خبرفوری:
🔹
برای مرمت مدارس آسیب‌دیده و ساخت مدارسی که به‌طور کامل تخریب شده‌اند، از اعتبارات دولتی استفاده نشده و تمام این اقدامات با کمک گروه‌های مردمی، جهادی و نهادهای مختلف انجام شده است.
🔹
بیش از ۲.۵ میلیون نفر در پویش فرشته‌های میناب مشارکت کردند و کمک‌های مردمی از هزار تومان تا ۱۰ میلیارد تومان برای ساخت مدرسه اختصاص یافت.
@Tv_Fori</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/690221" target="_blank">📅 21:56 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690220">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9258f4680.mp4?token=JzAVmi7a7kHFzaoCC_0Dn9pzGaqqfS7AIwn1afMIOWo1b7l7-YtgTpan6EpeQMJ9DeFwh9oeEO5_n0g6EbmGzXabS_vaYAlfMjFUiVn_52ZAnbMsaKJyqD2diZz5sPqreRV6KVjCrRbLVvVP_xYLfqMgFDK19RRVcBKjjL41VMbwF0IwByR5C5epL_tZEQkAraCdw11CyQeNOW0a7WLuFhlxkQwugCwaJNHfzGlN5cD0x4Vgu0qlGy_FCid7-3WfuBDKthGaWE57PmWiiXyQTl0SmlUmcZn5p7muKV2Wxlxp-7-PxLrOP2MR0_AsRchuy0H6izFp6gQ8L1Ah8Dts0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9258f4680.mp4?token=JzAVmi7a7kHFzaoCC_0Dn9pzGaqqfS7AIwn1afMIOWo1b7l7-YtgTpan6EpeQMJ9DeFwh9oeEO5_n0g6EbmGzXabS_vaYAlfMjFUiVn_52ZAnbMsaKJyqD2diZz5sPqreRV6KVjCrRbLVvVP_xYLfqMgFDK19RRVcBKjjL41VMbwF0IwByR5C5epL_tZEQkAraCdw11CyQeNOW0a7WLuFhlxkQwugCwaJNHfzGlN5cD0x4Vgu0qlGy_FCid7-3WfuBDKthGaWE57PmWiiXyQTl0SmlUmcZn5p7muKV2Wxlxp-7-PxLrOP2MR0_AsRchuy0H6izFp6gQ8L1Ah8Dts0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چند ترفند کاربردی تاچ‌پد لپ‌تاپ که احتمالاً تا امروز نمی‌دانستید
💻
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/690220" target="_blank">📅 21:50 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690219">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
درخواست ۴۰۰ همتی بانک‌ها از بانک مرکزی
🔹
عملیات بازار باز بانک مرکزی در هفته گذشته بدون تغییر ماند. بانک مرکزی حدود ۷۰ همت منابع در اختیار بانک‌ها قرار داد اما با سررسید شدن همین میزان ریپو، تزریق خالص پول به شبکه بانکی عملاً صفر بود.
🔹
در مقابل، تقاضای بانک‌ها برای منابع از ۴۰۰ همت فراتر رفت که با ادامه سیاست پولی انقباضی و محدودیت منابع بانک مرکزی برای مهار تورم رو‌به‌رو شد./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/690219" target="_blank">📅 21:43 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690211">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاقدامات هیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vYzbSU0SCYA59Mlla_0xz2uA-Tk6oNmNtbkPPl4Ki1PpnQy0Gz_rzups4fd7aWaKfJhxvnwCpP5HOwyZ8eRIxpsBWHNilR9nhxKaaDWcFj0_39EPewS89NpAEYsGbsg8TQoD4GrMYZ5wmj4z7_S-yug6EELLVlBciHjsc8RbCZFkCPtqVFncTP4nXB9D09hen2zGHqC1khI4ftSw11gjbw_5SCLq3373lsYQwhLPPMVjOA-k9DFevwyljGk6v5NxDP_qOAcYHsioUqobzxX4BIiEGMNdYY73AUi_ALayUxTBLlc9E94JTK-EkxTCSvNBVQPrKd7wIx2QPxXQc4gBSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RbAOLNHy2WZde1rXA3sMik3555MFzxSR0e0WdvGz1U1CRh-w94RaF5cEK8HwKqafxqNmmEDmFg9KY_VltdKdgmcDFZ-kVYaUu4_IjmZHq5X2ydPUW82FxbZfwVHWBcQZ_RM3aUHfb42wvJTtBYBt8_OIEx-JjOw7mxZqgHB215LN4-1SFeaJ4Zbl4yvvRaN5_6rwmC7t1tfhj-3hDD4DuD9Oxv4dEkLhdiKMp6MmteCVWiuMbYESr-AwxdErqmgdqzynAEGBbVn1-GhX1Me4nM4n_xAnGtuG8412YgHAxNMjs8wY6_pn0RoecZlVMI7rUG0oeBbJR7ptaS_dnwMatQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jGwbWcoIbMezYVrvzYvi5h4Olkg329mWwESHcdV1A4-YaikmtIaQoVhC63ihN2pEW0Ho25jd4q7mpBLMRq_L--Ds0i6Adxqpnkn9YhHJ4WZiB0d-CeTgj7Igb42ARm3Z__TwJOaiIt32pJ-wTEY3erTy1OEdV94Dmj6Lj1fCBXjEZRxul7DGn-vehR-tGNVMM6kF9hK1xZCs2A1daNVBG8P1qqW8aRZMltmK7SDmlvIRRHJ3-8o1mee6cae0nzQ06Y79ce8OlkiqHbQzyur_G3pXSXZZX0jw6SoPap3dy0VPYEIn5bnG4JoUMdWiR2awBZyrAMstDQViJq29n0hxMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dXwdykDordaCMJDxzGVVQTvZn0j5k38z4VP50-JUh_WY1gGkWHcUvmthl1I90-C8wbVSEp8JN-REAKBWonSOZAr2NEFmjnObwr5CcEZqboa5ojLCRjG_ltjILN6BbkZ4zZU7eWd6BDaexYJBo5ELjP7TG7knfdeDifwqC8EBsq6NY_P23vdKPuk4M1uxIpFP7xNik1XT2Xi44EWIBcV6vHIQYvfUm5k0Z1XaQXXGI3G4rwDNW20JwzMF5MvWE-RALXGkTbECmwQ_y2S0m723hZDQS_JEpFz1yi6v8HL_y3GcdEE59sWrmTGpQPH9qMpDg6nrK0d8Z1XY3e8yiPchXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q1g1yFkl1A_F1DkRR3qqn2mSQXf6ZWqFNpwxlH2krvTUAUwwmaewegji_D-xTIFGOsx1elCMY1MlaGc3dzaaNAaQwZu5cYPhabQHgCReGpnzDNaYtc-akaW3vMvWFYLlxoKB7g_NKq-ovlI3-6WqtX99i4-1kjS0VRVk1caAp9sG_ZaX9V8u1wlnoKdGcYiwcxZ37Mt_AZ8QBqIJovwtULK73OT1n9W29YHlNza8CErFVXtntscCkEJ8IXrjmYczTGiheG9VzXNbC1sMCcdQK_KxKjSzjycXZUF37bL3ZzJ009GuLjYmbxKsOVokBEj4H4c5TX-JjkuCAY5Kj0HMTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B7kwZNz8HTz0AzS89vhUxf3fiKlCMOLrGpHkyKaW-WfA5QDjIQLeqVKvOSggRj6fgGOZVOhAzX4pIq-BsT9w7TW6RDn__iD96a4_KuZxzUYCiB6FLjhfgs9VXvnDTqnidDR-dSIVIb9RmgGO-pDaG4ca3SEw5TKhc5T-ahr3n54MPhvca305yHP_bBXVCc8J3MXdi7_Io5OaPtm8ixGvTmaLDe9jY_yC-isda-7qutw7VUQp9xkpoAgnrhmd9PopxTVQqo0Xe_cYh9wFb4cRfDTQdC-xrrX2p-Ex5kAkeFU7ojVvRB1La6v1nZIxsDbw9DeS4vxdx0vitlZeERBTzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YGKLbnyKkeZA87LKdGVpXYdWNp7AMaNIJMwDWbLJ78PS3wAzQ4b-PuW9jkGZkvfvA_-QvpzzOAPpsmsc2pHU-OZl4V_GqvtLIjY2RPgdkea0nZYLXdT69mozhofN9nAb59J3L71LH-Vr99GykaT7x-Ec27abwOJsXlEoLwO72JjBrdIkFAEI3A6vkDpfDGrp2s5M8xNuL0TAGQDdA9jLMCs9C1dITF7-Roj6x-hpJNyOWSz3xlEYEb83FzV-klHFNxFFS3uRctdbYNy6sFFbxSgf0DC-nb9322e2LOa9W_98-GuvmvOFwhQ8PkGlPyw7_P-pdDDpTt6eTtH-qb1Djw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SwNchPvip7HQNEXnfVrwQF4DTPZglIVQluRRN4Se4_kduXlSt3i-U3dIov1Zua7qhsFGy0wnn7Bxu6L0aATzEh7eS7o-cdkscE6Dc_rsI5ACERi9vmO6j93yGXnAmc1FNUuNo2y9_a9P55exc4LbImPrAS4Yy9fJzbEsVs-KWDOGM5OiJOLwMECe6sqAMkWw89QAhTZfCN20e_tS1iYGgY2HWgBYkjxMrru0N0hQAHl9t5nFtFiDGZFhJZtSOrDanDsPMrjx39t6Ljpbr1T0WSNHSHzGde_ZcXaagfQDAdghFy2riEgTtReK8emTAJ6Ewz0ubl7SHSsogMd8Wi3neA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💫
روایت مهرِ جاری
💫
✨
مهری که از دل‌ها آغاز می‌شود، وقتی به دست مردم می‌رسد، معنای دیگری پیدا می‌کند.
🌱
#هیات_قرار
با همراهی شما مردم عزیز، هر روز با نذر و قربانی و توزیع گوشت قربانی، در مسیر حمایت از خانواده‌های حائز صلاحیت، این مهر را جاری نگه می‌دارد.
گزارش اقدامات هیئت قرار را در کانال زیر ببینید
👇🏻
@Heyate_gharar
شما نیز میتوانید در این کار خیر سهیم باشید
👇🏻
5029087002135690</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/690211" target="_blank">📅 21:40 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690210">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
وال‌استریت‌ژورنال: بحران بزرگ سوخت در جهان آغاز شده است
وال‌استریت‌ژورنال:
🔹
مدیران شرکت‌های بزرگ نفتی آمریکا که در ماه مارس و همزمان با آغاز حمله به ایران درباره پیامدهای بازار انرژی به ترامپ هشدار داده بودند، اکنون می‌گویند بحران سوخت وارد مرحله جدی شده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/690210" target="_blank">📅 21:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690209">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
سه‌شنبه‌ها روز بدون خودروی کارکنان دولت
رئیس سازمان اداری و استخدامی:
🔹
به همه دستگاه‌ها ابلاغ کرده‌ایم که تا حد امکان، روزهای سه‌شنبه را تا پایان سال به‌عنوان «روز بدون خودرو» در نظر بگیرند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/690209" target="_blank">📅 21:30 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690208">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
طرح استیضاح وزیر جنگ آمریکا کلید خورد
🔹
توماس مَسی، نماینده جمهوری‌خواه کنگره، طرح استیضاح «پیت هگست» را به دلیل تداوم عملیات نظامی آمریکا علیه ایران و نقض «قطعنامه اختیارات جنگی» ارائه کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/690208" target="_blank">📅 21:29 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690207">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PnQkOGvxbz-GUa5mwBuEpE31Har_lQ_eiWUlcM44-B1KrNIX8KOG6zvG3l-GQhS9yCoBndLlMNrNLWi56-TAvOp2kqQjNvgEUxs9vtoU_QZ3kbQ9YE1pVe6bFK6uG-OzRBbHmDOlItsWb4ekji_VIEucYoyYtl7TFor5MIou0D4A_Di6N0kkn-qv59OQ7B8YipL1dnEdYMKrl116dB6Z39tlTMnoxwxVUi8zGVtcdqTbc_fsVbAkdZYQHwL8Jm8FQLxSJIZ9eIEE_Mdraw85yM0XQTTfdlOyRCJDv0NKFoZ2BR66cxeIa5_LLiE2FXbNMArVX5OfhUKVSa759oql1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای نهادهای اطلاعاتی بریتانیا درباره جاسوس‌افزار ایرانی
🔹
سازمان‌های اطلاعاتی بریتانیا، آمریکا و هلند مدعی شده‌اند هکرهای مرتبط با وزارت اطلاعات ایران، مخالفان، فعالان و روزنامه‌نگاران در سراسر جهان را هدف قرار داده‌اند.
🔹
به گفته اسکای‌نیوز، با جعل هویت افراد مورد اعتماد و ارسال اسناد جعلی، قربانیان را به نصب جاسوس‌افزار «CHOSEN BRICK» ترغیب کرده‌اند.
🔹
این بدافزار می‌تواند پیام‌ها و اطلاعات تماس را سرقت کرده، از صفحه نمایش عکس بگیرد و به موقعیت مکانی و میکروفون دستگاه دسترسی پیدا کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/690207" target="_blank">📅 21:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690206">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uaYTjHgyycZYU1Tep7hf9KZuZcKxtiXznmWt_XPuqgR6dAazUj1anXcA5gNbyR4zzvzhQ9ACjEsA-uek0cREoVooOQnLWYWqsD50aVl6wYUn3Q7YLmSFidJF7OHGqtBYp9vcEiKDbPzkca-GBB4ZjDA9SGF2d9bfE1TfntbZrkVLBkzLfMwhUPDnhvm7hee_MHce-UbAeyel3_PaitjYEiG6EzV6mtDSgfRtpwlmzzKB83qvFBAip7sjiT4IdoP00t_hy3vr2QxsV-WrCGbzS1Pp8RPm8jwXV6NuMGGjeP9PGgMMA4cKusrqnfg7ChB5DbSm2oobrquDH1jbJh6GIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۲۰ به ۲۰۰
🔹
۲۰۰ شب از آغاز جنگ گذشته و خیابان‌های ایران همچنان شاهد حضور مردمی است که با وجود همه فشارها و نگرانی‌ها، پای وطن ایستاده‌اند. از نخستین شب‌های بحران تا امروز، این حضور برای بسیاری فراتر از یک تجمع؛ روایتی از همبستگی، ایران‌دوستی و دفاع از تمامیت کشور بوده است. مردمی که آمده‌اند بگویند در روزهای سخت، ایران تنها نیست و پرچم این سرزمین همچنان بر فراز خیابان‌ها و در دل مردم برافراشته است.
🔹
هشتصدوشصت‌ویکمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/690206" target="_blank">📅 21:06 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690204">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YXid2fWJ3b7RPhF2xS35O-_x2XeEwTBGMpvn6UAboih18f_hns6QZZB3npS6wM4a-UJaqTbc2G08jLcBeLjth7M8QW8dr8PTH1vJKZxWzTE_5e_wh0NakDQcUjKq73mOHPFH4P88JoNUntQc5XAV5XyPWZhkJTfEeYygbyrJLpStjV0sjUp_jYbRvguPrOQbf6NFkwQ86bsEW9BC0Za_lOBFW8iE9t83yscnUySiVR81hM0Cy_lznJVceS8P_PuAnt-Ir1YWYEHQnVIAALY8U-mCD5ccxq4VfBYvvXc45JFW2kNIppXziXF4xy_tyjVPmFqLgIgkfV67dfWOnGnwJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BriD7gkXSE3Jj8OI-0wHDLs3gp--fqCzH4Ul3E9xrMlMPuYBSkSTduTk7DGj5Dzkg5f5hDurYhYviWwh8QN3FQ1TEehBVVzLDQEnqQs97xD0u-V8pu8cPvUXjHs487xKjJLA3C8gkMLTqzKeM5U8b8lWII2RtrFKzYan-eaYjJG0fQVRSc-1vZYIUa4Id9OeHVhPcuFCPyxgfJxOmTYOxhtSs6wAtt53bNVXZ09dQgwCW9wSRb-LVQeldjoSYzHSveryRcWD69gFZZywaRAs0JwpeGKioFMuieCmmU_r5fOlttKf5Klnnr2MfSxGEzs6etGFc1onQ6Nad1S6Cioo0A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تولیدمحتوا در اینستاگرام رو شروع کردی اما هنوز از این هوش‌مصنوعی استفاده نمی‌کنی؟ #هوش_فوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/690204" target="_blank">📅 21:06 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690203">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W3Aa8i0hqSXnuYMpQfmmz9g2j8Bp4dgPiuwQ-hErMvif4sSkv-sSwQSj-4k5wRdQSvAR5VPybp4UivxhQrJqEzkus-svapkG7lqC9faum02wfmy0OJ9HQh9xIYkdO913UECXlzyTDA4kfm4iCxnhQeHb8zgueHeM1tjzvS1DmtWfz6DUmaWL3T3NFm9czB_-FltM4EtSwYksypDZpgJlr7GhHlvYcH8cbcZpDoQGwAhjJPWgC_jQd4Sf9xAM5PPobIjtJ0raafPwmcINRpe_K3m8_MAgYKwtZj03pMrrTSZazqjogTGo8SAmyeR9ir8lAOKl-max51wMcxsDyzD9nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💸
وام رو راحت‌تر و مطمئن‌تر بگیر
✅️
♨️
تأمین و واگذاری امتیاز تسهیلات رسالت و مهر
🤝
همراهی و پیگیری تا دریافت وام
🎯
مشاوره تخصصی و رایگان
💎
مالی پلاس؛ سرعت، انصاف، معامله مطمئن
🔗
عضویت در کانال
👇
👇
:
https://t.me/+fJZdA3Fcu28zM2Nk</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/690203" target="_blank">📅 21:02 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690202">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
آکسیوس: هفته گذشته فرماندهان ارشد نظامی از ایالات متحده، اسرائیل، عربستان سعودی، امارات متحده عربی، بحرین، کویت، قطر، اردن و مصر در آلمان دور هم جمع شدند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/690202" target="_blank">📅 21:00 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690201">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HBfmR_qsVyfwao8DZuZ6JOmDKrsAVeMc8hAQR1tk2PEsuisQcBi1xCSSS5x-56mKblyROSGJ7fn8pUJ-t5G4FGCYtOpj3MpTjBQmISHDnnG0hT7I4jjnKDLFVOfKBkgqbLOeEgVWXPIO9mJcUIIJenARl1ogACGdblFETZy2W9gJqteia5rliGx-8Ddc05qnIhGQnJ364p3hRywZGqijzSaj18NWxYXLUFYG1qQBON0V24b8R8gYYqaatYOr-T2mGta4A1H31dp1bT8-S3yZMr1mjYKDW9qTipWA2WjXZvK2IpJ6wo5I3MEABuFOdXpl7tUzaK9JzKVJI7VYOqVmmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واشنگتن پست: آمریکا به اسرائیل چهل هزار بمب ۲۰۰۰ پوندی می‌دهد!
🔹
این اقدام بزرگ‌ترین فروش از  این نوع مهمات در سال‌های اخیر خواهد بود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/690201" target="_blank">📅 20:58 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690200">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e292778a2d.mp4?token=nZGCO41sOvdhtW8Cd7udBUOXU8zuVCTz0npn1O0BZuxSHmREHNWNRIFEQkYrcPW1ddvQBKrNs5HCXA-OGZzYW7i8fY5DS3zEAtwoUv7EzC6yye8ZnmXqkAwKVXGNroIPlva3IhWP59zPAT99Nkc-kYNEl59HeS0pzBZBpEoFe3cJMkNj_bzr_XTY2Xni4xi7lxS3P_1myPQ_ld6uzhWBS_5fBx6YCQhU4mQVMBVI9ZKEsOwMrgEYZrx_wc1t9LHBtIVKElOTJ_c1dnqLxD0J_cmr0nFK6v-JwYS48ICvojSwes1lTAbzojbedqLLVTRSUM2MgkYQM2whpjaZC0SkNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e292778a2d.mp4?token=nZGCO41sOvdhtW8Cd7udBUOXU8zuVCTz0npn1O0BZuxSHmREHNWNRIFEQkYrcPW1ddvQBKrNs5HCXA-OGZzYW7i8fY5DS3zEAtwoUv7EzC6yye8ZnmXqkAwKVXGNroIPlva3IhWP59zPAT99Nkc-kYNEl59HeS0pzBZBpEoFe3cJMkNj_bzr_XTY2Xni4xi7lxS3P_1myPQ_ld6uzhWBS_5fBx6YCQhU4mQVMBVI9ZKEsOwMrgEYZrx_wc1t9LHBtIVKElOTJ_c1dnqLxD0J_cmr0nFK6v-JwYS48ICvojSwes1lTAbzojbedqLLVTRSUM2MgkYQM2whpjaZC0SkNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تفاوت‌های سکه با عسکه ۲
🔹
افت قیمت سکه نقدی، لزوماً به معنای افت ارزش اوراق «عسکه۲» نیست؛ این نماد یک دارایی مالی با سررسید و حقوق قراردادی است و قیمت آن را باید با توجه به سازوکار حمایتی و اختیار فروش، نه صرفاً قیمت لحظه‌ای سکه، تحلیل کرد./ ایبِنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/690200" target="_blank">📅 20:58 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690198">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bQffwhFlAJGO2lqPULMh39s3Xqgr5VmIcOsyM8WymTE2bhAWYZTU1NsX_9GfD7VRMtcBT9YxGPrpmUDr53ktJ4OTpHBxqPVOPR58STaeRVq07y_moclWmhNcXwoQZ2j0BCJ_-2Id07PDgjUDEg0WbXyr8B5d059XrNilTYM8LFKGVzFVDaKWfLx7bT9tYvYi6-L5I8OKtjHaEhjQlZDlwpJBNKYZSo1jfxvioiy8S_xnQEvRedLHn18Lf1DqasUUUB7E_dXx2AI_1qfML4lTO7VSemhFRsPKXGcvl_2xx2fvencRtK62e0fqQFDCWfkxkhbYAUID1tQCxbQHNmYNiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
علائم بیماری تیروئید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/690198" target="_blank">📅 20:55 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690197">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
تغییر مهم در جنگ ایران و آمریکا؛ غافلگیری بزرگ در راه است
🔹
اتفاق‌های این روزهای یمن، فقط در مورد چند متر خاک نیست و پای یک معادله خیلی بزرگتر در میان است. معادله‌ای که یک سر آن آمریکا و متحدانش و سر دیگر آن جبهه مقاومت و ایران است.
🔹
جزئیات را در این گزارش ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/690197" target="_blank">📅 20:49 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690196">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfd06de7b9.mp4?token=EfNsmLbuNxKct2Z59qJJK8Xa6uzumfZEIn9ql9BySmFbNdlEKTyGTg9eqUBvIqr6-zel0PnWHzwlqlEsZ8JS10K6VKjC6H7R8AYKkq95qfMWHBW7vcgZCfnip2B_uhSRcRSepXvap7i-9J-hHXzAvBao5-Q40_cepd_AxRlBic2Ky_wZfQV7lNAZjNNhx_BgBRZi-g8RotIYpT1hP2ahQyiiy1_ycKuuzAVzDhA4tu3-XopLoz-68UZRWYx3gHW7VaSAQqUTTNgOOiq3ELT-Doygcspe5A5KhyD7s_LrInO35Sp8J6NtDlsHrteMGcogEE02o1xh9MlEiRSNRepZ_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfd06de7b9.mp4?token=EfNsmLbuNxKct2Z59qJJK8Xa6uzumfZEIn9ql9BySmFbNdlEKTyGTg9eqUBvIqr6-zel0PnWHzwlqlEsZ8JS10K6VKjC6H7R8AYKkq95qfMWHBW7vcgZCfnip2B_uhSRcRSepXvap7i-9J-hHXzAvBao5-Q40_cepd_AxRlBic2Ky_wZfQV7lNAZjNNhx_BgBRZi-g8RotIYpT1hP2ahQyiiy1_ycKuuzAVzDhA4tu3-XopLoz-68UZRWYx3gHW7VaSAQqUTTNgOOiq3ELT-Doygcspe5A5KhyD7s_LrInO35Sp8J6NtDlsHrteMGcogEE02o1xh9MlEiRSNRepZ_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من هرطور شده خلبان میشم...
تصاویری از شهید حسین مهدویان، خلبان جوان نیروی هوایی ارتش
که در حمله دو هفته پیش ارتش تروریست آمریکا به جنوب کشور به شهادت رسید</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/690196" target="_blank">📅 20:44 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690195">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
معاون هماهنگ‌کننده نیروی هوایی ارتش: چهار خلبان پایگاه شهید دوران، مأموریت بمباران پایگاه العدید را انجام دادند، اما سرنوشت سه خلبان هنوز در ابهام است
🔹
تاکنون به جز تحویل پیکر مطهر شهید مجید کاظمی، خبر دقیق دیگری درباره سرنوشت سه خلبان حاضر در این عملیات…</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/690195" target="_blank">📅 20:40 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690194">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
سخنگوی سازمان انرژی اتمی: ایران تسلیم نمی‌شود؛ برنامۀ هسته‌ای ما صلح‌آمیز است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/690194" target="_blank">📅 20:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690193">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/398be23961.mp4?token=K083L83gn3U5e3rU1B6zkZxUPUcUvAEu7LZ-x8j7AOPbKxLPq0v7ZKKcIxjLS9JRnJQ7udZ7WX2T_60ouLj2yN1eJWxcEdVTNNBgocPxtF2yW8sZL9kScOQJruUeXVF7NQtv0bBStVBiuY9NYbu-tE6TjqfX61_MiJjZErKItBXJSNnQkSJkvaOSR0C_CioiIxGBY0EjfsEsiFlcYMWfZE9gNqrncsEGeuwq_rdyMrvbEdoYEdRxnMxBdeOIN_3M-GAHdaEzxpTZTXR9kj1qIa711dRxXarsBs3sZ1R3bzJ9_XcXcK8EWNA9ZZiJ3OKD4zv6RwXag95aEKWC0q-lNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/398be23961.mp4?token=K083L83gn3U5e3rU1B6zkZxUPUcUvAEu7LZ-x8j7AOPbKxLPq0v7ZKKcIxjLS9JRnJQ7udZ7WX2T_60ouLj2yN1eJWxcEdVTNNBgocPxtF2yW8sZL9kScOQJruUeXVF7NQtv0bBStVBiuY9NYbu-tE6TjqfX61_MiJjZErKItBXJSNnQkSJkvaOSR0C_CioiIxGBY0EjfsEsiFlcYMWfZE9gNqrncsEGeuwq_rdyMrvbEdoYEdRxnMxBdeOIN_3M-GAHdaEzxpTZTXR9kj1qIa711dRxXarsBs3sZ1R3bzJ9_XcXcK8EWNA9ZZiJ3OKD4zv6RwXag95aEKWC0q-lNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در ۱۰۰ دقیقه ۱۰۰۰ گردان جانفدا تکمیل شد
🔹
با اعلام ستاد مردمی پویش جانفدا در کمتر از ۱۰۰ دقیقه ۱۰۰۰ گردان آموزش نظامی و امدادی جانفدایان ایران تکمیل شد.
🔹
افرادی که در ‌ادامه ثبت‌نام خواهند کرد در لیست رزرو سازماندهی خواهند شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/690193" target="_blank">📅 20:32 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690192">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/639235263d.mp4?token=UiVo1MObwSnHeCZ2SMlZeF8nsqQeIoxBAciU37a9qtaOAuSBdp4MBq5wgM_eeaaCgDqetyMb-P4Oum3KHK6GXS7OOpksJWoC8LON57lGbob3kwhMGtLx9wkQvT5O3YDYo2nav9OMPQVSVO-cHf-pKT-POHzJgRMHllJ_pzENVO6TspuSE_P0sKZcW3qUNyR65WVfdOlXwou6eNP-HXN2SPtZVAY7oIGR7HW3nOHahxCwp7dqV3J6HUGJM62iwUYTrtaGBYtajaQAeRDT8uhy8SgbRNaxXp_UuzxzonmEP4OGD7f4GNBuDLCyrWSgek-R5kUIeRYR6g6-M32mJEbcPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/639235263d.mp4?token=UiVo1MObwSnHeCZ2SMlZeF8nsqQeIoxBAciU37a9qtaOAuSBdp4MBq5wgM_eeaaCgDqetyMb-P4Oum3KHK6GXS7OOpksJWoC8LON57lGbob3kwhMGtLx9wkQvT5O3YDYo2nav9OMPQVSVO-cHf-pKT-POHzJgRMHllJ_pzENVO6TspuSE_P0sKZcW3qUNyR65WVfdOlXwou6eNP-HXN2SPtZVAY7oIGR7HW3nOHahxCwp7dqV3J6HUGJM62iwUYTrtaGBYtajaQAeRDT8uhy8SgbRNaxXp_UuzxzonmEP4OGD7f4GNBuDLCyrWSgek-R5kUIeRYR6g6-M32mJEbcPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گاهی منشأ سردرد، گرفتگی عضلات گردن است و درد رو به سر و اطراف چشم منتقل می‌کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/690192" target="_blank">📅 20:27 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690191">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
۸۰ درصد مردم به‌جای خرید موبایل، گوشی‌ خود را تعمیر می‌کنند
محمدرضا رمضان، رئیس اتحادیه فروشندگان تلفن همراه و لوازم جانبی تهران در
#گفتگو
با خبرفوری:
🔹
یک سال قبل، از هر ۱۰ نفر ۸ نفر گوشی جدید می‌خریدند و ۲ نفر تعمیر می‌کردند، اما اکنون این نسبت برعکس شده و ۸ نفر تعمیر و ۲ نفر گوشی خود را تعویض می‌کنند.
🔹
با توجه به قیمت‌های چند ماه اخیر، تمایل مردم به تعمیرات موبایل دو برابر شده و رقابت در فروش نقدی نیز به حدی شدید است که برخی موبایل‌فروش‌ها، حدود یک درصد یا حتی کمتر سود می‌کنند.
🔹
فروش قسطی موبایل نیز طبق شنیده‌های بازار دست‌کم ۲ تا ۳ برابر افزایش یافته است. گاهی با تغییر نرخ ارز، فروشندگان کالای موجود را پایین‌تر از قیمت خرید عرضه می‌کنند تا کمتر متضرر شوند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/690191" target="_blank">📅 20:18 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690190">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
آکسیوس مدعی شد: یک مقام آمریکایی گفت که ارتش آمریکا و کشورهای خلیج فارس، عبور نفتکش‌ها از تنگه را در طول روز آغاز کرده‌اند، نه فقط در شب که در ماه‌های اخیر روال بود
🔹
این اظهارات درحالی بیان می‌شود که قیمت نفت این چند روز صعودی بوده‌است و معمولا ادعاهای آکسیوس در خدمت سیاست‌های مورد نظر ترامپ و کاهش قیمت نفت قرار گرفته.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/690190" target="_blank">📅 20:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690188">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R-VSihTz9g81ZMFprf5mJFV8CUwSEQmH2KvLvPFIcsGozrk7D12S52W_sAHyWhAiTP6FA0J-Z1q17nrCdpzR16tYewrE7tQSLfNP642j1ElPU9vM9_Ddqb1NeQxF8i4bJn0uZoJ01tDNnCccrJQ_pXHkZcDNU1VaB6obudCi4pWba8uWWc3WqakBdSkWthpVUVcgGu7w1R19Qa8cs41tTBd_iWXW-fu4uUUzXT7NH8Pvh3mjpyfTtGKgvTLKY0fHA79JWbTLk6y0Y_N_yaM-D4DJ4a-y0O3Q0ltrd-JroGgqfaBxjnOivWfQJaIkGXvEDVbeZBFyDPut9uzLu199Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wv-1uS25rTQ2kS8iU6zxGSDhasQyy467ywS9vai34ezmB-grM2_1iieL8xeWvtp5yocACqVx0DvJtQ5abZMobZvpfXmeeLdNmRaBnALKgJM1M9-lSjbZ0SVCWEcI2r8Df4TytNFRTaHXiRs4RFnzwRGKGtaU7wta1XKRekvAGZDFRfVQdx9LMIiPok6KdKzOYgbt0gt9beTJLqGn0MzbyoxIPgvxq7Ew5-sVJlQ3QOIn2HjJJojwhO5wEO2v6Qn7Gp-XZZHSZmpGfIz4G_A2QZEJsli-CBmj5WVmjXXK05paGwnzQDxLyz3HXGfeSzVIv-6Pj7lj0cIdRjjRusBVyA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
عراقچی: در زمان مناسب میزان واقعی تلفات نیروهای آمریکایی را افشا خواهیم کرد
🔹
ادعا: ایران بی‌دفاع است.
🔹
واقعیت: صدها پایگاه و تأسیسات نظامی آمریکا در هم کوبیده شده و ده‌ها فروند هواپیمای آمریکایی به آتش کشیده شده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/690188" target="_blank">📅 20:06 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690187">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
محموله‌های نفت خام ماه سپتامبر عربستان لغو شد/ نفت برنت به ۱۰۸ دلار رسید   رویترز به نقل از سه منبع آگاه:
🔹
عربستان سعودی به مشتریان اروپایی خود اعلام کرد که برخی از محموله‌های نفت خام برای اواخر سپتامبر لغو خواهند شد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/690187" target="_blank">📅 20:05 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690186">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c54a0e2c8b.mp4?token=F97kAJfgp-H_HDkjqTQ6Jp3Hxv162vfLk2Jqz7WlMFg0LazRArEl848yYMfWyznO2HAt5raU6Uvq0bRffezWvGQ4zf0NA9weHf-XZFt3-s77K9ArFJ5yver7PSjVf3kNqlQ8Vp8Q6jyJR2SzhjjFDfabXoJm-TLz38iNOv3R5Gkpp3S09A-hkiZeZKyv7GZLTxcPel2oZKIXxF0aKkIEQE4_J7tQW62HO-eoeQxJEEwBdF8oDx1vdUpkvD05OK1MDLQsk0ZYHiKP8JZKX73DHAOfglUet8ZM03V53xRQemStOArQTK54osTygzZqle_B_9KDqbUwqvi4lpbQmsvK0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c54a0e2c8b.mp4?token=F97kAJfgp-H_HDkjqTQ6Jp3Hxv162vfLk2Jqz7WlMFg0LazRArEl848yYMfWyznO2HAt5raU6Uvq0bRffezWvGQ4zf0NA9weHf-XZFt3-s77K9ArFJ5yver7PSjVf3kNqlQ8Vp8Q6jyJR2SzhjjFDfabXoJm-TLz38iNOv3R5Gkpp3S09A-hkiZeZKyv7GZLTxcPel2oZKIXxF0aKkIEQE4_J7tQW62HO-eoeQxJEEwBdF8oDx1vdUpkvD05OK1MDLQsk0ZYHiKP8JZKX73DHAOfglUet8ZM03V53xRQemStOArQTK54osTygzZqle_B_9KDqbUwqvi4lpbQmsvK0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عینکت بخار می‌گیره و کلافه‌ت می‌کنه؟
👓
😵‍💫
🔹
این ترفند ساده رو امتحان کن تا شیشه‌ها دیرتر بخار بگیرن!
✨
#ترفند_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/690186" target="_blank">📅 20:05 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690185">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NmFZcU4uRP7q7vYLphWIXyyqlMW9naGverKAB2cco22TSb5ZSTywC7uYH1XXTMU-hqcJgfj-LCWp3dOBSaRyymSuen-75mz7HsD04eum65d5qfptFNSNJ7Xc2ZHApO9KpdwgRsg5zyA6X2A6VyM207byOrGYCX5ULlCss3Xtgleg8XK5IaiBIN_2ah-hA_8732EVY7FBgKiXB7DIRVeaTie20_8ChmqlASh0BdBv_aZNFfmW8KtRjqaelsCNidzu7KN6jf2rWa6UB5i5UNBP_NFo77dHRNGpsUtJmt7xWdOUYhp8hd4njLAWUhhgHR-aWj63jwZdJ9C6_E9Da5BN2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
دنبال لوازم خانگی با قیمت مناسب می‌گردی؟
از بازار بزرگ لوازم خانگی گناوه مدل‌های مختلف رو ببین و قبل از خرید، قیمت‌ها رو مقایسه کن!
@genave_shopp
از یخچال و لباسشویی تا ظرفشویی، کولرگازی، تلویزیون و ده‌ها لوازم خانگی دیگه
👇
✅
خرید مستقیم از واردکننده
✅
۵ سال گارانتی و خدمات
✅
پرداخت درب منزل
✅
ارسال رایگان به سراسر کشور
🚚
📲
برای دیدن محصولات و اطلاع از قیمت‌ها:
@genave_shopp
ارتباط با ما:
👩‍💻
@tejaretgenave28
📲
09176333145
📲
09176333146</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/690185" target="_blank">📅 20:02 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690184">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o2RNBF4aMxRE07fpuaQNSk3c9e6pO9oDKPGglOKcjwsG9g24nzKvfy4jAbNFI8q3GBL16eyWJZ0vXK_5qJaxXgUic4X9gPHWxEcAjSh_uH_KM8qPbeqSh0PufbZkHnRNk_mAwU48miXkyr1CyN5gCaVfbaxzjbspWWwXeoZ7hwffCxZvsg2Gdl-T8LseqfhGEcE_49UYnWnBJI-79bSMQkXuLwIYr-B_3oHcg0btsASlaxjkG7boea6C5_wJ_5lBfrsZB9VSOqM0D5QaYxRX0_J5rw4HbLRqyV7W0XM53qD6kehm4IES77p4UtGLleC-rLSsnwUqUL2tymTlPmkUSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌸
لباس‌هایی که وقتی می‌پوشیشون، عطر خوبشون حالتو بهتر می‌کنه!
😍
با خوشبوکننده‌های لباس
Lenor و Yumos،
لطافت و رایحه دلنشین رو مهمون لباس‌هات کن؛ ماندگاری رایحه‌شون باعث میشه حس تازگی رو بیشتر تجربه کنی
✨
🧺
💗
در
ارکیده شاپ
با
کیفیت عالی
و
قیمت مناسب
میتونی سفارش بدی
🎁
🎉
و یه خبر جذاب
🎉
با خرید از
ارکیده شاپ
، شانس شرکت در
قرعه‌کشی بزرگ آخر شهریور با ۶ جایزه نفیس
رو هم داری!
😍
https://t.me/Orkide2025
https://t.me/Orkide2025</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/690184" target="_blank">📅 20:00 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690182">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
ادعای بلومبرگ: دولت ترامپ از ورود رئیس سازمان انرژی اتمی ایران به کنفرانس آژانس بین‌المللی انرژی اتمی در وین جلوگیری کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/690182" target="_blank">📅 19:50 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690181">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
تماس میان عربستان و اسرائیل از طریق سنتکام
ادعای آمیت سیگال خبرنگار کانال ۱۲ اسرائیل:
🔹
تماس‌ها و رایزنی‌هایی میان اسرائیل و عربستان سعودی، از طریق فرماندهی مرکزی ایالات متحده (سنتکام)، در جریان است و هدف از آن، ارائه کمک‌های اطلاعاتی به عربستان برای مقابله با حوثی‌هاست.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/690181" target="_blank">📅 19:47 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690180">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942bfea51f.mp4?token=JpUkIUdtoQ_BCOewDVR7kMv57pMqRJ_f_HfQTbWcbuI_ISJlUl_61Zfm6b6RKRQlg0L0kOn1xTDRIVwfFnzw37d2VDvXyiOVNvf6GmYnLgydxk35HcGSV2ppraogSrcu2EwSt8JvW3SOZOXh-eq8gUP8q9rwTVaaTSYeTpQjuZQqoFywAwwGqlgvWX4VhCT_1XkItHT2CE_kqWvvqAVSHuzB2lINompICdwYgCNUi7E_gCEosohHG4xtF-O3XWd978zuVkOw4N5taYCA_9kEVJX1aQl8V7j1x_8pyilf2l5xkdJ0o4yb5DaF3_RUIXsxj7ym6ZQK4tHBZfvbmV0gZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942bfea51f.mp4?token=JpUkIUdtoQ_BCOewDVR7kMv57pMqRJ_f_HfQTbWcbuI_ISJlUl_61Zfm6b6RKRQlg0L0kOn1xTDRIVwfFnzw37d2VDvXyiOVNvf6GmYnLgydxk35HcGSV2ppraogSrcu2EwSt8JvW3SOZOXh-eq8gUP8q9rwTVaaTSYeTpQjuZQqoFywAwwGqlgvWX4VhCT_1XkItHT2CE_kqWvvqAVSHuzB2lINompICdwYgCNUi7E_gCEosohHG4xtF-O3XWd978zuVkOw4N5taYCA_9kEVJX1aQl8V7j1x_8pyilf2l5xkdJ0o4yb5DaF3_RUIXsxj7ym6ZQK4tHBZfvbmV0gZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این پلنگ پس از دیدن بچه‌آهوی تنها، موقتاً از شکار آن منصرف می‌شود؛ اما با نزدیک شدن کفتار، بچه‌آهو را به دندان گرفته و برای حفظ شکار، به بالای درخت می‌برد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/690180" target="_blank">📅 19:44 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690179">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ix77USHw8g2yFnyPoeCo-wivJuy566_uj5jNHPkpsuDzpXT2-kNZA8RicnnssMrh3DBoyZDN4dnMU1-ka4rF3ZgOkiu_b80Sj8jTRK917HxRKWEn2_3Fh_FqDKgbbdT_7V9hhM6falKZ5RLD1eoiHlhmYO3g_VHjbbOfwrcJ1roLtOYnfnVQUE0p3cstk5iBqiFBTJ1R_579Hmjhw9xFSHO0kUEUajcPqOORruywm28YHmSICDtkaoe7L593drosjJ4Nubr18Y77i5MNnYk2prTbp3fzRWQNKSHn50fJe5uqGK25mDwB_rOQfj7fCENqWEOzljhiQZ3PmZM91M0rUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
همه پروازهای خروجی فرودگاه جده متوقف شد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/690179" target="_blank">📅 19:41 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690178">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
شهروند آمريکايی به یک نظامی این کشور: آهای، قیمت بنزین چطوره؟!
🔹
نظامی امریکایی: خیلی وحشتناکه
🔹
خب امیدوارم توی ایران کشته بشی، اونجا بدجوری قراره به حسابت برسن.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/690178" target="_blank">📅 19:37 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690177">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18e8e89d76.mp4?token=DP_OEzfHmnZ_XMUHcm7-GgrJ6oyvJnHM_E_00deC4Rp7gc7mTApW6NyqV0wkv-ums7OAaAnObVuvh8I3K6jesONH2rbKJKZTQu3-_4f4-vYpVtoYGdeSSrbWWruWrK4mJTrSbru6RdGRISZSR8qoiROXp_-KmQssJL3b-Nh2Lqsrg9yehVe8PDc0A9hlx-0x6RwGhVKgzvnW6HCUmyojWQ9eB1QkfPgefN1TkuMH3j1vxtktTBebNSiDqVOmK8lEBjbnfGBTyShWw-MWoM2GETU9piineAzkZlOXtZQwC2NhKVjzHiclgV2xVi8cE3ec6GUM6Kw7usTun3DZ2Q7h-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18e8e89d76.mp4?token=DP_OEzfHmnZ_XMUHcm7-GgrJ6oyvJnHM_E_00deC4Rp7gc7mTApW6NyqV0wkv-ums7OAaAnObVuvh8I3K6jesONH2rbKJKZTQu3-_4f4-vYpVtoYGdeSSrbWWruWrK4mJTrSbru6RdGRISZSR8qoiROXp_-KmQssJL3b-Nh2Lqsrg9yehVe8PDc0A9hlx-0x6RwGhVKgzvnW6HCUmyojWQ9eB1QkfPgefN1TkuMH3j1vxtktTBebNSiDqVOmK8lEBjbnfGBTyShWw-MWoM2GETU9piineAzkZlOXtZQwC2NhKVjzHiclgV2xVi8cE3ec6GUM6Kw7usTun3DZ2Q7h-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی‌های گسترده در تأسیسات ذخیره و توزیع عمده شرکت آرامکو در ابها، در جنوب‌غرب عربستان سعودی، پس از حملات پهپادی و موشکی روز گذشته ارتش یمن
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/690177" target="_blank">📅 19:33 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690167">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v1awN_Fbm0vNYsS96EX0FeoWny1KMxdG_oPkR70q-kslxTvuSDz6E-l1vtqAOm543YhzT4vcHzrzuZJnuoACh5sGtnwRQZycqwScX9QF1V_Ul8cSYqTo9oWPpf-veiOMl9-YWqGEgSAl-wn2olpfFSVG0v-l8ajS4jGuCQLkgggkoMjZ7yjCHMA4odYPH34ykxB3LYv7tvg6neCl6p24ua6S0C_N_OGiS2yBffD5IcrWdauz5HMR9EJZntWpCtT_PLzVQC4ngtyBnCiN9BYo7x5R4qn11IXT7DsPjyrjOlBuGyPz6P_ec2__2URJxtKtOg05oxkR3_v5zsXlJZF9Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cO2gcXFIKs5teGi8MUbdQxv5FPZkF6h5qROss1dGiy3CIblweYqTOnhxGBOzEBEFxHmwAwI1KN8qA67c-1x5ceGYq4Lh7njnjrllCq2bP5q-XaTlVfk55xONnX3J7x0LC11JodFWtoZTraarOQ56Tlon96dx9xA2ixjgMFgsK4E_-THsubhJcN3mWLdNR4NQQI8aZ8mOWfkIHnZtFwna4KkNQwxXQaYjSuBLVfq5WhymCKdme0Py8uriaCNDALXj5MgjLo7GthYAAsI080MqZIzuVmuhXfqg9lW4JiCsH2Tj_CSk0cEV0Ds-_NCDZgTZBqZcyrrKbvtTVSwSVbmQjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/veO8EZ4dYZ-fPu3_NRBBW71XNGKIG7ifKYGLTAqUO60QvlDzcNOk0x_C9n7gY6SW_G-2bBjqsVF7e67eISz3lRin1UN2D_R57CUrl9Do-rsP7gtluabHxAj4oad5aR_ccr1pWTGVpPatphyG7lV6SNtoft8rAsXb-iA25Wnx7ZvKikpq4jlLQKZINrD5F7MRB1GN38chjh2klwQh69eBAPA9iLDMnI_WycAXdSTOzEju7AYp8NLgPI7MbQRTClAKVnXFW8ZF3Z8-ChYgbEYYAhnebAUCfUPXtiib4QmloUWxIbQ2hOZumD5kanNU6RWljyabW9ynX0jRI8p3cpKsLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nEUZYYildH6Uj5pZrC47TJSDKBwTBgH5KXchPvHj5nVz5ES2tykirqeF0KfrNdceHWay28ks5UbYcrE4h0s1YxbAQfh1Byord4K7XhTudpS6rxz-r5S05J_TpYskn2gzs0ZXJgIp93yZy50iOx91_B4fN8m_BZSPCzVAshUot_aP3q2b2R2EtrnvUnBSxrs6EqjLJ4vf7jQwhNP5icwTnhSQdT30hTre2ykmAQG8-EKVbv2HG2G8EEVTzkuEIBYqKshdEbZ4P5vIFdhQ2QE1ir-sTavuDwDUuy2c_z4xIaxSdhdYvqDfPR481yRQHRdBwfaUgzlBTyW3YpksgslGfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qdS9hp6HerOox-2ix5zyrq3Z8rEC5hUsY2HEO9yF9E8shxeTFeT_fWhgdyiWVGe4x1UJQhVa7wJ6kbBh68GM2e2mYGLSite1RKDy0mgMRbHMBPxvh7U0byUTkiIQa93z4pQAjAH7f9wtALMtaCa2z4JrbC7r-Vn7NRcreBB5biyoiHKAlyswwBrd3MBk-7ouHqvrwqhchXqCEN9GSMdWPx3gZe7pVBoETgQTw8iV9cPb1KyGohPOsqSMPzK1qcQ35L_16pgHAX7Q3Pgy5gHAxsQKj102OhJYX3y3gCLyaa_eLti5l5vaybSRxy51rtYkyUFhwvzwnhLRA7obaklHZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DVBb0Z59O8OxkCHG7xEuUfNI2KHw2MxI-F66tZGRG7eUVcAXQc1bbVUlFk6XwVs4a-ss2x_A4cnSu5estuJmP2Pv-O0fUJEv1Dxvyh9XiG49ZNe6pYNMUxeFQyMfH7uL0B8F6Gy9VOMkdnWiR3fckoyxEzCvtqMbQJ7Y1NdZuuRjCfA3DrWvn1NYopU85cggFpHgBAC26EeU7KAUCLuhwK6wrW2t0z6mBcZyxEQKfGf7Ac6tWqaxnJlWdFMYCeOmY8AkAupmv726GykfYIp7cub2Yk2jQLWSFKYB6-j2Od2qpGiEX0nn-wBiG-DfO3V4_J31a9NKp-uWJzcYqOP1Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ROqlF9IgMlnIB7zfpUMpU1N4dLJtgT9IgOQjKzWWWmSeKEoOwKgchKmRXxjyyW4SGEbjuRG6lEBeWEEGrnr6pRQTOwy0ogB4Ws9stVAFkBt_WyD15cixlZD5cDu7K0ci6pRs_444eas6Gfwk_0uT8tiMMzlk96Adn5i-CIld3KqukMGx7xqww-Yw6YCFezPqbt6nvwBE5pz6aYCC4E9H99KwB8YSsF0Qqo2Ko2QDPtYXfgz0XFvB7DnDoO3ZqT_eKzSGFa-1uFTeUJeen284-eZVjbkYPlFFOqRlM3HdyPs_rKX8LE5kWSUsduiRHpkg2CxfOz1i0LBdIDL2gkDUwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qbbW5G3aAwz0VDoF9lJ9JK7UVswyQxgBGCtXAziXAkwQYv6TNVXFSE4gV5twGepr0xw5FMdhavJ14IeTeejKHbS6nWvUTuJm5VoX6R2H7UI1KiHJV17LK9yucVZr6kMSDXqrIZ7ldUh8mo5KWCuXktnn0R6GIa5nTnJ6bNE-WV3jK_MQwZVikeuHsauYYkaPtZnqn8azP_N78-j8SJPqPGgIzgoFNIW4f7exsdkSWZAf45INLBJNxW5pBQd-RkhHoJjsRo1XYM_yvYoSMDCNO3ADhM3RAdGQr1mr6F4eUADQ5Eut9qCAVQI0pnVR_gfMTTV4KXhQJAsuGfTeEKqDlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aEFL0ZYDoThqVnkyl1R8GFy782XHF7A98illfsYjTWfRcql_7QcxnCUXyLgcwN0km0Qmpf6Nw_23G8N-5-hfvE_fb12UaAgPuc7nYdGz6BiMt_pG0USYFcIlm_SeJd-dO2Cj3JtYMFfThK0hHvMEsCbHUr0iNJlK7ZalSoRLF67HAWotfqOla7fWpD1l2qu1Rc51E7M-Nzoc65RNrt-req_KGt4L_oZI1qVs512UwMl1fOCNoajHIwMI8uq9vYLvUSuJvnP5k6PWUIR68ShWRHnAdt-CTgNVyPzYKfDE4iKuAH_4_XwnwFAi7zpw8C8p8TBtqnj20c7Tfv8PY85IAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LAA3B6e1Rl9bICqSzEhPd2qcPDzoJWbcOMsWtkURTB7TSAQUfBv3jbKyyWPub_1Vjp6dyzq9XQzvpq_0CQSbAhrlTBKSXWXXtWnOzllw7wjEZ5Jh20msBxKaBx5Qa32W7fdHuka3eQy_AeROE_cfO0hpVUSUpOCv1CWtppLlEa21TeuBWX2p8f4cp7JdxxYJ1sEFjlHpEtr42S48wukuu3zyCdfYT1K5vWsyIlh3nh9nmJ1NgNelbNwp_yKeY5pm004rFk-V-TQS0dlIacgflzKcy6y9dJTrekYi17kWXqABfl6mOd1yifHECWeQOnp-lzP2fdXYzeUDwOZO9SHzyA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چالش‌های شروع سال تحصیلی
🔹
انعکاس دغدغه‌های مردمی از مشکلات ورود به سال تحصیلی جدید
🔸
ما پیگیر مسائل و بازتاب‌دهنده دغدغه‌های شما مخاطبین عزیز هستیم؛الوفوری را دنبال کنید
👇
@Alo_fori</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/690167" target="_blank">📅 19:29 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690165">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
ادعای وزیر خزانه‌داری آمریکا: مذاکرات خصوصی خوبی با چین در مورد روابط مالی با ایران داشتیم
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/690165" target="_blank">📅 19:21 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690164">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6acb873e3.mp4?token=TCHX1Gy-ZZCaYLV0G31DWxdgEcWmhslTHin1Iif1Sh-h4nEAbqPrPcAEZi_C4qE6Tqgwf5JOjVi5OtNhEvRk2mO9RgR4_l3Wua5g5181bKRfspa8Yf5wDOCNYV3Cxzp8mk4fg_Y469UzHwsIpBBoG2g1KQWlmYu2upHT35gByTsw6w0Mq8ZrGw2pi6mXI4NAg8zsmxR_ydF2DpKI9qJoJZjkqm2WISzUPtI3k4CJo79-JOYWDOnS9R-ddlr44humoPVXf8Ho6oTpY253x9WxiPsJ_jyHX2KFhEONYySRXsi-upsYDIrDZJxRFiUpUwYPiymZxdpfggnB9-o7qEj_-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6acb873e3.mp4?token=TCHX1Gy-ZZCaYLV0G31DWxdgEcWmhslTHin1Iif1Sh-h4nEAbqPrPcAEZi_C4qE6Tqgwf5JOjVi5OtNhEvRk2mO9RgR4_l3Wua5g5181bKRfspa8Yf5wDOCNYV3Cxzp8mk4fg_Y469UzHwsIpBBoG2g1KQWlmYu2upHT35gByTsw6w0Mq8ZrGw2pi6mXI4NAg8zsmxR_ydF2DpKI9qJoJZjkqm2WISzUPtI3k4CJo79-JOYWDOnS9R-ddlr44humoPVXf8Ho6oTpY253x9WxiPsJ_jyHX2KFhEONYySRXsi-upsYDIrDZJxRFiUpUwYPiymZxdpfggnB9-o7qEj_-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مرکز امنیت دریایی عمان: نیروی دریایی عمان ۲۳ نفر از خدمه نفتکش الگایا را خارج کرده است. عملیات جستجو برای یافتن دو فرد مفقود شده در حال انجام است
🔹
فرماندهی نیروی دریایی سپاه نوشت سوپر نفتکش «ال گایا» که قصد عبور از منطقه ممنوعه در جنوب تنگه هرمز را داشت،…</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/690164" target="_blank">📅 19:05 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690163">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
اعتراف بسنت به جنایت اقتصادی آمریکا علیه ایران: اینکه مردم ایران باید چند ساعت در صف بنزین بمانند نتیجه محاصره اقتصادی ما است
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/690163" target="_blank">📅 19:05 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690162">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">▶️
پروژه‌هایی که در هلدینگ خلیج فارس آن‌قدر خاک خوردند که از «پروژه» به «سرمایه‌سوزی» رسیدند!
⌛️
سرمایه‌هایی که می‌توانستند به تولید، توسعه و سودآوری برسند، اما در چرخه‌ای از بلاتکلیفی و تأخیر، گرفتار شدند.
سؤال اینجاست: هزینه این سال‌ها توقف را چه کسی می‌دهد؟
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/690162" target="_blank">📅 19:00 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690161">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i6DIgBO_dzQoHXQpaLrLoApwpmXiz-A4nrWy698lGK5uyNb5xZMKqKNtbuAMLEj9mQ2X6lq3ABQ5WpMRZMeiyMWP3sFqaExXY8tVq9Pf5DM9mDk9753SmTMrf9DoadLJSAODGH9n6fozSNNNjLs0oh0qrUlWHKSQFApwz6UapXu959tY-boaXuj2NU0fDME68WbM1J8uZqCxm6QzfOtSjQ6kK-fBd3_iCQPsU_JRePMYRLshzD7huMPI6GmwXjvoQNwHJL1aQGX9Ocjx0UUjh_y1LxoHLLVXX9N_lMZE_6a2YhzGEqzkmGZ99XtX_68iJYHYxzCXBU5HUtzNDvOidw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۶ نوشیدنی برای سلامت کلیه
🥂
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/690161" target="_blank">📅 18:49 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690160">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/029883431c.mp4?token=XpHIEjy9i_Dm5y537NvW6XtkyAkJDN2sN7VK89L6vgrbAzVnGOiOSxA5ZF9YLdg5aw87s4c4ArJn-wXDxyKbAKTacRZcEsGeXwGqOVOEsYE9EdIuvYrG44lYqWACJzmLNovjTvinYNr9iT6NIRzRLw8ihsbyrSTvVnSpz7eOkxCVx21gIKEUykY0dPD5H4ajEpgiJFmHNDFXVTVTOApqlLKk_B1x2RI8ca4aS8sbG3GiawSLmonIgpxN5vLahR65LMel2XaCG-K_FLsr0cMnb0hYKvjFBckmMmDnX67XVkqhfJLwMBWaedjC_nfgdy5cWbOl4hGF2-HE2o-_kMmYcQkr70SujZf3M06FG27lawuN44hIbJ1awDmJNTJI2nR1im2Av1eVQgeoEVQZaLy02AMHXIWT9Ls6b4QTnqli_nK-m05XGlOaCbdwcaPfoVbXH1pUVZkJ8uPx6bOYzPbiV8h4ZwumuWaZtkvepTh-ZIkqa7NpR2LdJy8Ed_XRQrkBZa0PZm1ABYHuXA1WlcwgqqqA_c12HQAXh3my9Y8KyWPFsDD8gi8PfgXkFsQjqTPwR9G_lEnZg7dWC24RXFt5oBjcLAZCNKRcLGgZVIMEaAmNTJvS6lkf9RUmhsc6W7FGVlERgRPz2vupS_3lgs-ZKY0T680btgYt394tBgvytYo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/029883431c.mp4?token=XpHIEjy9i_Dm5y537NvW6XtkyAkJDN2sN7VK89L6vgrbAzVnGOiOSxA5ZF9YLdg5aw87s4c4ArJn-wXDxyKbAKTacRZcEsGeXwGqOVOEsYE9EdIuvYrG44lYqWACJzmLNovjTvinYNr9iT6NIRzRLw8ihsbyrSTvVnSpz7eOkxCVx21gIKEUykY0dPD5H4ajEpgiJFmHNDFXVTVTOApqlLKk_B1x2RI8ca4aS8sbG3GiawSLmonIgpxN5vLahR65LMel2XaCG-K_FLsr0cMnb0hYKvjFBckmMmDnX67XVkqhfJLwMBWaedjC_nfgdy5cWbOl4hGF2-HE2o-_kMmYcQkr70SujZf3M06FG27lawuN44hIbJ1awDmJNTJI2nR1im2Av1eVQgeoEVQZaLy02AMHXIWT9Ls6b4QTnqli_nK-m05XGlOaCbdwcaPfoVbXH1pUVZkJ8uPx6bOYzPbiV8h4ZwumuWaZtkvepTh-ZIkqa7NpR2LdJy8Ed_XRQrkBZa0PZm1ABYHuXA1WlcwgqqqA_c12HQAXh3my9Y8KyWPFsDD8gi8PfgXkFsQjqTPwR9G_lEnZg7dWC24RXFt5oBjcLAZCNKRcLGgZVIMEaAmNTJvS6lkf9RUmhsc6W7FGVlERgRPz2vupS_3lgs-ZKY0T680btgYt394tBgvytYo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با اعلام رسمی سخنگوی ستاد مردمی جانفدا ثبت‌نام گردان‌های ملی مقاومت ملی جانفدا آغاز شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/690160" target="_blank">📅 18:45 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690159">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
وزیر خرانه‌داری آمریکا با توهم ساخت سلاح هسته‌ای توسط ایران محاصره جنایت‌وار خود را توجیه کرد: چون ایران قصد داشت بمب هسته‌ای بسازد، بزرگترین کارزار اقتصادی جهان را علیه ایران اجرا کردیم  بسنت جنایتکار:
🔹
تاکنون سه بانک کمک کننده به ایران را تحریم کردیم…</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/690159" target="_blank">📅 18:43 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690158">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفروشگاه قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cwInQ5_5NfFzI9cBY6byOjYdQq44CAeII-4RHOzEBQBgS_F9snVhexk6niKmLMlZcMdvFmxyK_VWd37vxt16tF9JeW7ZPJmjYlV4HdvIA9Ul7hW9sjhO3m-h-sH7TMQEFhEpFvUySdt5xQh3SXm7_tsWdBbXSkCFWfltkd-6-rh0HVinoNkzVq7Id08EZlSV1GuQnVkFzlE7xWF0gR_iNskA5un3oOq-c_ffKsPNCIazoKsDnAzWQoQhK3K_T1fk_WkkvUodzgyPqr5XaX9vnSXWXeX3bymI-UPx79KXNCr82eN419Zzf98qFs1OwMl2h5OqeTMi0d48rAbGe6qilg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
پک ویژه سوغات رضوی
یک هدیه معنوی و ماندگار از مشهد؛ ترکیبی از عطر، مهر، قاب‌فرش و تسبیح رضوی برای کسی که می‌خواهی یاد حرم را با خودش داشته باشد.
🤍
داخل این پک:
🌸
عطر گوهرشاد — ۸۵۰,۰۰۰ تومان
🕌
مهر تربت مشهد — ۱۸۵,۰۰۰ تومان
🖼
قاب‌فرش ۱۵×۱۵ — ۱۵۵,۰۰۰ تومان
📿
تسبیح رضوی — ۲۰۰,۰۰۰ تومان
جمع قیمت اصلی: ۱,۶۳۲,۰۰۰ تومان
🔥
قیمت ویژه پک: ۱,۳۹۰,۰۰۰ تومان
📩
سفارش:
@gharar_order
قرار؛ تجلی هنر و ارادت
@ghararshop</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/690158" target="_blank">📅 18:40 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690157">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KsaWqGCV3s9Q-k26IzDS8wbKGX0RXJuRZ-74NAPZqo74Mfdlo0z_C-jDpHHATJEYPW6amJbDJEt5qxVbDjuXkG5H7DLhZ_F6mxWxvO665ztx_vDnNEraz8SCPflFxMDryn1bWEdaCOvkV1bAd_pu92QVog2E2RyLNuLmXnV0EkvlIm5pQjP_5O9P_myqvuibvKDDmO26N77fg7qSiC33bgFnNkmWZnNb5SYSCdzDWjdgL-PIkeIOhk3yXq1e8rmrF9qXIXKiP8eCQMyCd2LQsdCMTo0_D94NCLxy7Y9Lld8Mf4P_x9zm1kQbHrzdTmIWErVwv2yyAuwaHZ4TND6cHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
در ویدیوی منتشرشده از سوی سنتکام درباره عملیات نجات خلبان آمریکایی، هلیکوپتر به سمت راست گردش می‌کند، اما سایه آن همچنان در مسیر مستقیم به حرکت خود ادامه می‌دهد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/690157" target="_blank">📅 18:39 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690156">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
محموله‌های نفت خام ماه سپتامبر عربستان لغو شد/ نفت برنت به ۱۰۸ دلار رسید   رویترز به نقل از سه منبع آگاه:
🔹
عربستان سعودی به مشتریان اروپایی خود اعلام کرد که برخی از محموله‌های نفت خام برای اواخر سپتامبر لغو خواهند شد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/690156" target="_blank">📅 18:38 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690155">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a1a4b63c66.mp4?token=NTnz20U3i7t7QMPx6YIUaQf_tnEKF3l1jI8wgRyFXwNBUwPGYUo0diU1M9Wgz7oFjYkO77rn6dW6h10hFvg4rr9ynaWdJf4_8sbmtMqcFBsi09kv8VQAtRAoKTSHQOt7cUK2oOn4XgWgzbeX1hH6jtS5MHcLaDW0VK7HZPLs8fn30DDxOWr0xfqa24CEYgoBu7TUr1SC-pPPsMQbABGmLaAEy7a2ibycn8br-Xeiw3x8dc7Er3io9j_rxB87GAUjWe6lIje73ivPQR20kwaxoInQYRXS9occV-avzLGX3tMo-m6zreuUri1YPkjGtMMg-yGt-pRQzd_E2biWKbGYRg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a1a4b63c66.mp4?token=NTnz20U3i7t7QMPx6YIUaQf_tnEKF3l1jI8wgRyFXwNBUwPGYUo0diU1M9Wgz7oFjYkO77rn6dW6h10hFvg4rr9ynaWdJf4_8sbmtMqcFBsi09kv8VQAtRAoKTSHQOt7cUK2oOn4XgWgzbeX1hH6jtS5MHcLaDW0VK7HZPLs8fn30DDxOWr0xfqa24CEYgoBu7TUr1SC-pPPsMQbABGmLaAEy7a2ibycn8br-Xeiw3x8dc7Er3io9j_rxB87GAUjWe6lIje73ivPQR20kwaxoInQYRXS9occV-avzLGX3tMo-m6zreuUri1YPkjGtMMg-yGt-pRQzd_E2biWKbGYRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شاهکار عشایر برای عبور گوسفندها از رودخانه
!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/690155" target="_blank">📅 18:37 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690153">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YIrmZD6AGuHYVvy2KcmkbEcSZkpcrCfkCroc31XkJN_hP2LtIQnlsVByU7Zt2hdX2CwG-1YgEKT7yB6INI50sozM43BExOHlGzdqeqRoUwqE0FkD9pYxhgoablBlu0VGK3ooAOKoxpziWiM871vnbYGW6lNUGC4PEpIYj8-pGwZ-ZTesgY7NSyRuqv4YwtYxIunssHdZ8s7HnY8vvmx2osiFxyaMVcFEJlnUkRUdjHIqDwFnQo_0STImi0b4EX58I9KIslhWC8C8EjuTnaUZr73VGZPimMMpSisezSqF2nqGc3O9JH5QIRRvX6BFwHpAqFs5RJPJR6hhKbexTgUtiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محموله‌های نفت خام ماه سپتامبر عربستان لغو شد
/
نفت برنت به ۱۰۸ دلار رسید
رویترز به نقل از سه منبع آگاه:
🔹
عربستان سعودی به مشتریان اروپایی خود اعلام کرد که برخی از محموله‌های نفت خام برای اواخر سپتامبر لغو خواهند شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/690153" target="_blank">📅 18:21 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690152">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
حضار کنگره آمریکا با شعارهای (نه به جنگ علیه ایران)، بسنت را تروریست و جنایتکار خواندند و صحبت‌های او را قطع کردند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/690152" target="_blank">📅 18:15 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690151">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0d207f274.mp4?token=Ijia8mfywiwlAJo14WNhD4pJaLnhHivmiMpWMRD9qpM3ODnxtixJXXpdISgnHfVEsVzn4yoSow2L2b49SbUkf_RCieeIMdQ6amdtYGi3gzTJlgjHZbpqLubmrSgKOYJONDxGLY0B_C6bJY2X92DdTFku0juSukYIPZVkbLFgXTJitK31YS-wO4Tdry5NQ59axEcGW2QOnOdJ4KmjAk7uNBtAWqU4N1RdA1hERA3_ItRXLQSt3bI2B3klWu5qrZWjgU194W_BgPr-hSaEcCbsUuVT9f6lqVmFNV4c7Gk4ZDvil2XyjCNwCEmoMkGlRqTBmQLV57VAmnRm_CDnnFoBXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0d207f274.mp4?token=Ijia8mfywiwlAJo14WNhD4pJaLnhHivmiMpWMRD9qpM3ODnxtixJXXpdISgnHfVEsVzn4yoSow2L2b49SbUkf_RCieeIMdQ6amdtYGi3gzTJlgjHZbpqLubmrSgKOYJONDxGLY0B_C6bJY2X92DdTFku0juSukYIPZVkbLFgXTJitK31YS-wO4Tdry5NQ59axEcGW2QOnOdJ4KmjAk7uNBtAWqU4N1RdA1hERA3_ItRXLQSt3bI2B3klWu5qrZWjgU194W_BgPr-hSaEcCbsUuVT9f6lqVmFNV4c7Gk4ZDvil2XyjCNwCEmoMkGlRqTBmQLV57VAmnRm_CDnnFoBXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضار کنگره آمریکا با شعارهای (نه به جنگ علیه ایران)، بسنت را تروریست و جنایتکار خواندند و صحبت‌های او را قطع کردند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/690151" target="_blank">📅 18:13 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690150">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">‼️
خبرفوری/ انهدام یک پهپاد MQ1 دیگر در شرق تنگۀ هرمز   سپاه:
🔹
لحظاتی قبل چهارمین MQ-1 در چند روز گذشته به وسیلهء آتش سامانه نوین پدافند پیشرفته هوافضای سپاه و تحت کنترل شبکه یکپارچه پدافند هوایی کشور در آسمان شرق تنگه هرمز رهگیری و منهدم شد.
📲
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/690150" target="_blank">📅 18:10 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690149">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lvtr9ZTexWNhqvEe20B--ndoCrlOw6uNGlnU3JMifZCRtRwiCvuvCNWPaMHOsH8JTbMmto_hOYpwNbIT_E3kiwXbzjh130CjIU2pO_Z3IENU7rOUcckkQpqFIQ67KGOSQlRgLYTp9JO3FOOQinygorcvYDass5KwBP6hW62jq0wgEHaQHn5TKG0BSeORdf4tXzInCnEfbb8CyHMzpnLRFFS2bMhFoQ0WW_LqlDFZOEHT9HPQBneUjxEmwNMwJgY5LF_zZCaBa2kzCxk9lue0ql0-thuwwlax4FKjbKRNFk0Jy5u_39VUr92lxv5tVevdx-dkLJQueT7_u0ACimdFMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
همت راهداران از پسِ خرابی‌های جنگ برآمد؛ پل بیات به زودی زیر بار ترافیک می‌رود
🔹
مدیرکل راهداری و حمل‌ونقل جاده‌ای استان آذربایجان‌ شرقی گفت: پُل بیات در آزادراه تبریز ـ زنجان که ۱۸ فروردین ماه سال جاری بر اثر اصابت موشک‌های دشمن آمریکایی - صهیونی دچار آسیب شده بود، با پیشرفت فیزیکی ۹۵ درصدی در آینده نزدیک زیر پل ترافیک می‌رود.
🔹
عبدالحسین علی‌اکبری با اشاره به تخریب دو دهانه میانی پُل بیات، اظهار کرد: پس از گذشت حدود چهار ماه از آغاز عملیات اجرایی این پروژه، در حال حاضر مراحل نهایی بتن‌ریزی در حال انجام است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/690149" target="_blank">📅 18:08 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690148">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aYrmV1FmicLHrLEb3f5fO162ttNQYV-tuvhVna-hUIbKrz01Tk0XoPXebbVH_7wnv0qlOaImGh570q_3_1p8jIgZUAMXcm9sTvxN1kdaQyv9lp5afLjG_6-1HTF0P2Q7dPIHvgVFAHzWEBckYDhEHnjU8vm06Xmu7kudPD8VCcDENrou_QjXyMmrVlMRMakf4AKcN30LlM3rQIJWrNfpZFX3agG40mnKyJPt4WZ8SJPz2yHjyjoeIBk6mKBPxJklvxlypgpWlxzZ4s6mbKjHLf-_Av5wQgGqxd61wCOzSoedRSSDl4bbibpjAGz9eUUzeP5wiK7S6AgZG9v8nsofgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جنایات آمریکا، تروریست شماره یک دنیا
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/690148" target="_blank">📅 18:02 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690147">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a91ec24c8.mp4?token=l3UX2RRgy84bNlrU-paxoFz1GBJ23sOxtFf7LwETL9dQ3RzoVytPW2iRWoF0ZVEMPwLplFRl3UCr-HRLqfd6uVWPTKOow0V9WSzbtmYamv-ZJPW4gACiydG3ljdCfadOFHaG9ucpOH_E9BVs8NAEW7YXtXiRZZkF45Pgzz-zKstgWqtMVBLQt2nd2g5LKTIwgIKb69CsEw6XNHoNzHBkxEk3VZZORo8vSDsPy3Jy9aQlAbMkATlax6rmv2jzzxfhVmSVW9PVeRjqq5BFuk9_SdW_-fhO8HWNuv6wwntuSK5KK4ZNd6bahXPjJz_Stb7ZiI4NXKfRgPJUKXvkS_GMwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a91ec24c8.mp4?token=l3UX2RRgy84bNlrU-paxoFz1GBJ23sOxtFf7LwETL9dQ3RzoVytPW2iRWoF0ZVEMPwLplFRl3UCr-HRLqfd6uVWPTKOow0V9WSzbtmYamv-ZJPW4gACiydG3ljdCfadOFHaG9ucpOH_E9BVs8NAEW7YXtXiRZZkF45Pgzz-zKstgWqtMVBLQt2nd2g5LKTIwgIKb69CsEw6XNHoNzHBkxEk3VZZORo8vSDsPy3Jy9aQlAbMkATlax6rmv2jzzxfhVmSVW9PVeRjqq5BFuk9_SdW_-fhO8HWNuv6wwntuSK5KK4ZNd6bahXPjJz_Stb7ZiI4NXKfRgPJUKXvkS_GMwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اولین فیلمی که ادعا می‌شود مربوط به عملیات نجات خلبان F-15 سرنگون‌ شده آمریکا در ایران است
🔹
این تصاویر برای نخستین‌بار لحظات عملیات نجات خلبان پس از سقوط جنگنده آمریکایی در خاک ایران را نشان می‌دهد.
🔹
در این گزارش ادعا شد که خلبان آمریکایی با استفاده از…</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/690147" target="_blank">📅 17:53 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690146">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4f9b252d2.mp4?token=qxrdMkIPJIQd8OYrTlPDiZ0JWipht9Z7z7V6UKi1pJiUfZNBNi7dC4hjZbKV6AK8t1yFTyXj6kcU1Pvh1-5ApatRUZaAiNkzZ7SlgHrdXSAGiHOxxpQbpus_9VJ3w0jt98Amg319Yt5rbzYUytQJge86d_WNpqMwdxHXo8T4-n1Cyj8JtLQ0Mt4jXyvq-efiu4MRzOUeIX2ECejWpmUN90bEVCz1WBMvgZgY3sxwq18AUFckot_LX47aujpHscXt_fG9aQNMYuOikhW0iiEnVH6eQpC5CUhVM0JIVP6C8QVM_924NH1X2_MBfcSLU4tkqp-Woz7WaW8LfNK3yWEYPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4f9b252d2.mp4?token=qxrdMkIPJIQd8OYrTlPDiZ0JWipht9Z7z7V6UKi1pJiUfZNBNi7dC4hjZbKV6AK8t1yFTyXj6kcU1Pvh1-5ApatRUZaAiNkzZ7SlgHrdXSAGiHOxxpQbpus_9VJ3w0jt98Amg319Yt5rbzYUytQJge86d_WNpqMwdxHXo8T4-n1Cyj8JtLQ0Mt4jXyvq-efiu4MRzOUeIX2ECejWpmUN90bEVCz1WBMvgZgY3sxwq18AUFckot_LX47aujpHscXt_fG9aQNMYuOikhW0iiEnVH6eQpC5CUhVM0JIVP6C8QVM_924NH1X2_MBfcSLU4tkqp-Woz7WaW8LfNK3yWEYPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش اختصاصی شبکه ۳ از نفتکش هدف قرار گرفته‌ شده در نزدیکی سواحل عمان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/690146" target="_blank">📅 17:50 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690145">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
وزارت علوم: دانشگاه‌ها در نیمسال اول پیش‌رو حتما حضوری خواهد بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/690145" target="_blank">📅 17:48 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690144">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
نیروهای مسلح یمن: یک کاروان نظامی وابسته به عربستان در منطقه «العبر» استان حضرموت هدف حمله پهپادی قرار گرفت؛ برخی رسانه‌ها از کشته شدن ۳ نفر و زخمی شدن چند تن دیگر در این حمله خبر داده‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/690144" target="_blank">📅 17:48 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690143">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IMkCfPfQrOUp1wTJLSgf2UHd3a0WFx4ttT2iEOIVnIZiMtk_xPzYHL_KcsSF2MPTMzGXq3RQ3E2WcsrlFjjoVymUldsE8_1e_dS43hvB-XhFDTM1BAayQ5g8TfSDuOypYNv2dmHnYojLexBbH0TKR16EUAx_QDfzaMUTF0myujLln3xE0qPI3na--YPgjg2gUJHyB38GQdgwhhHgogWM6bUJrS5k_HYk1DANjNxaoBu00iK2D0yijDv6_BQuDtPaXpC0kaNj8akDUfmLxcbYoBW3w7hpN4YjdJPxyNl5F2mbiF1dYSMn79VgC9nJKlb0trICXWdv5i8Ktl_sYSiIWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا پرستاران مهاجرت می‌کنند؟
🔸
در این نظرسنجی بیش از ۲۸ هزار نفر شرکت کردند که سهم روبیکا ۴۸، بله ۲۵ و تلگرام ۲۶ درصد بوده است.
🔸
بیش از دوسوم شرکت‌کنندگان حقوق و مزایای پایین و ۱۰ درصد هم احساس تبعیض در نظام درمان را مهم‌ترین عوامل در افزایش موج مهاجرت پرستاران می‌دانند.
🔸
تداوم نارضایتی از شرایط شغلی پرستاران، مهاجرت آن‌ها را به تهدیدی جدی برای تأمین نیروی انسانی و پایداری نظام سلامت ایران تبدیل کرده است.
@amarfact</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/690143" target="_blank">📅 17:44 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690141">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f67759b99.mp4?token=tubHrLrR_7p6brUM07jpmXh7Ri31_GZWeANCnB-z9c5stEl1VW9AGHudA5NKd361rKsv0yuEKAYfqMXWB-RySLtOLnglebnjl5LA6ecL-sVrCfn3N69t1V5iQJ2pdAddM9BcMQ1IjvkJh3oVCUkuHR8UoeaOj8b6h1cbdBWMWIDyCxSlNMF_ipTdGW0B2aV9CwEWHZMJu8eFGjTlpcQeB85QQareGWz24uhOEQTl4xGKN_lAG3uK0ipNi-qX4dt9l_Dbc8WZVmvLfrEqIENDKoR11ciaP_F8VzQaIouTye-_A96y23Kzs3Vv50F2GzfDvo9sEVGJXaqHaB0OZMEKWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f67759b99.mp4?token=tubHrLrR_7p6brUM07jpmXh7Ri31_GZWeANCnB-z9c5stEl1VW9AGHudA5NKd361rKsv0yuEKAYfqMXWB-RySLtOLnglebnjl5LA6ecL-sVrCfn3N69t1V5iQJ2pdAddM9BcMQ1IjvkJh3oVCUkuHR8UoeaOj8b6h1cbdBWMWIDyCxSlNMF_ipTdGW0B2aV9CwEWHZMJu8eFGjTlpcQeB85QQareGWz24uhOEQTl4xGKN_lAG3uK0ipNi-qX4dt9l_Dbc8WZVmvLfrEqIENDKoR11ciaP_F8VzQaIouTye-_A96y23Kzs3Vv50F2GzfDvo9sEVGJXaqHaB0OZMEKWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خلبان آمریکایی که در ایران نجات داده شد: چتر نجاتم در حمله اولیه آسیب دید و به طور کامل باز نشد
🔹
با سرعت ۱۶۰ کیلومتر در ساعت به زمین برخورد کردم و در این حادثه، ستون فقرات، بازو و شانه‌ام شکست. با وجود این جراحات، از دره‌ای که فرود آمده بودم، یک مسیر کوهستانی…</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/690141" target="_blank">📅 17:39 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690139">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
مشاور دفتر رییس جمهور درباره لایحه مقابله با نفوذ: به مقدار کافی نهاد برای شناسایی نفوذ داریم/ با این طرح‌ها کسی در کشور نمی‌ماند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/690139" target="_blank">📅 17:26 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690137">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4775902ea2.mp4?token=Xe4GXY9bG_0H1q99Z84LEwDWMtUrGQw6De1QvGILzAK-vde6LI_QjyK--Myx8jc1cLHM8gwX_m-yfyJ0OZvRwd_1zKbcFAegICXimHf5o5MApMmL1_O6hI4A4sAciEErfNPS7ZuLXnyST2Y63mE6LNPQhyi6rkydhd5m-Ytk4wXT4OJpflG60IOi--B6RM1PBaCcuqJwJmAnZ1vSUKAcRYBWHpAAwZU9agt267lUegC6GpEI1Pd28s-FgeMLqXs1vVpMkromOF4BbQmn_Stgkp2LP0KxIlFzNKYI6hA2s5dF_5rLz6uNhrpTkLvxf_8iRwvkmjuNAdKOeNj47yyhdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4775902ea2.mp4?token=Xe4GXY9bG_0H1q99Z84LEwDWMtUrGQw6De1QvGILzAK-vde6LI_QjyK--Myx8jc1cLHM8gwX_m-yfyJ0OZvRwd_1zKbcFAegICXimHf5o5MApMmL1_O6hI4A4sAciEErfNPS7ZuLXnyST2Y63mE6LNPQhyi6rkydhd5m-Ytk4wXT4OJpflG60IOi--B6RM1PBaCcuqJwJmAnZ1vSUKAcRYBWHpAAwZU9agt267lUegC6GpEI1Pd28s-FgeMLqXs1vVpMkromOF4BbQmn_Stgkp2LP0KxIlFzNKYI6hA2s5dF_5rLz6uNhrpTkLvxf_8iRwvkmjuNAdKOeNj47yyhdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عامل پرتاب کوکتل مولوتوف در میدان پونک دستگیر شد  مرکز اطلاع‌رسانی پلیس تهران:
🔹
فردی که سه کوکتل مولوتوف به سمت شهروندان پرتاب کرده بود، هنگام تلاش برای خروج غیرقانونی از کشور شناسایی و دستگیر شد.
🔹
این فرد در جریان دستگیری با مأموران مقاومت کرد و از ناحیه…</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/690137" target="_blank">📅 17:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690136">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
اف‌بی‌آی مدعی خنثی‌سازی حمله داعش در پنسیلوانیا امریکا شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/690136" target="_blank">📅 17:11 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690134">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RAug2aoRdGazoxEBwjtQH_T0rAP92Oe8jn1GBxtP9mEl0U_zDANJFI9uxAqqpLEcFQLVd5W8hHChpW7xr6TOmfIAf3_zogEg9_Q2jzwpFoJzYuipxwhqoFDnyIobquFUxcQkLO5PjMtizouqPXgcRx2pc0NvGOVdkirJY44eBxuK1lUmp6ufP_L_cIbpXo58HQQRCq4kM7uSfZIMWfvXP1ATtd7KtzXLVRgoa7-yOCagoJ__1fKUlbXhIqWMPrDuXbzA90GNGDIHspMFmeU6-w8EYoDoA5wXVbvqj3qwO7bniorf5YNc5H03wvG6_wET35LAJuqbDAEus8VvzDAviQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✈️
خرید قسطی خدمات سفر در فلای تودی
🔹
فلای تودی با هدف رفع دغدغه هزینه‌های سفر و ایجاد انعطاف در شیوه پرداخت،
سرویس خرید اقساطی
را به خدمات خود اضافه کرده است.
🔸
با این سرویس، کاربران می‌توانند بلیط
هواپیما،
قطار
،
اتوبوس
و
هتل
را در مقاصد داخلی و خارجی رزرو کنند و هزینه آن را با اقساط 4 تا 24 ماهه بپردازند.
🔹
این قابلیت بخشی از توسعه تجربه خرید در فلای تودی است. تجربه‌ای که در آن، علاوه بر انتخاب خدمات موردنیاز، شیوه پرداخت نیز متناسب با شرایط کاربر در نظر گرفته می‌شود.
برای مشاهده جزئیات و رزرو خدمات، به لینک زیر مراجعه کنید:
👇
🌐
خرید اقساطی خدمات سفر
کسب اطلاعات بیشتر
:
☎️
۰۲۱-۴۲۴۰۵۰۰۰</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/690134" target="_blank">📅 17:05 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690133">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
ادعای آکسیوس به نقل از مقامات آمریکایی: ما دیروز دو قایق ایرانی را پس از تلاش سپاه پاسداران برای توقیف کشتی ما در هرمز، منهدم کردیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/690133" target="_blank">📅 17:04 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690132">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mKtUbPAbV-UPE1Z-DKqyE-Z2FkSji4KQuJVhMHCUFYZwZaesbsF1ui1zqlAYCGdeNC1_RzXQQcYJcPOCVjVB4ZGuxHFbT8ZulC_CMqbcCrhoZE_L_2fEJMr5Z9CY3VBk983E3MG92zzqM4pe7AtqsNsXe0YQVUvZW7G9Rhybx7PKHKhC9Am1dGMIh71GVbuN2Tg5bS6sgU53aYajeeErf_V6fibpKOXWOpxQJktvejghQPN_ThxFsHy6yn6o6vMnqxDpxii5h2faB9Ztlv5AhbGEzli9jUzDWuXsB3vn1M9iZ-Ay_6y2UMDK8Norz4xz6Fzvyy5L9_xxCTaPC7Dh9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیشنهاد: آقای پزشکیان! آقای کاظمی! زنگ مهر امسال را به نام دانش‌آموزان مدرسه شجره طیبه و با روایت قصه میناب به صدا درآورید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/690132" target="_blank">📅 16:57 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690131">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63eda0fef9.mp4?token=EMnkJxinla-sgLrJ2N2YL41VyakEuZCC9kZkn044hg7dAjbWUTh4FbKQMYGo_7Q5KpUAATESbDjrxYLD8_vX_Q5eeomCHxMxIn8cpix2IgArGsMJCNjZHOORYiM98qsvKPgGA_eIDAtpt8KOmEtCQCIDaJnIxcKObfu95HiKRu8LCwqSXSIA_AGZtTYGtBVBloAxHH1MPnTg4JvpDRDpsVFBbAMNJ7bYZao-M-yvUnrdhwWMtsTOrSeic54ZLMIEHRU8zTLIhrdbeCyQVmNWPZrGdJoSyUv7f6rYLupMIpKkUE-7vON7NqobNttZs2_NkSW0hjYrxXOWWeJqzcbu2in8mSPTB1cH2w_ijZgpLoFnpuNOxI1f5cHUGGqn19j3EbzW1AXaxmSxiCF9YI3bphgAdUtonqY069eNtAkmpIVvnveNkgnXHECa1_FU-btGdgEmJit6Re8MRxlN6XQVfYvpiXgp-qUKx80BSX1lJOWgLv5Pos5o7h_UvjJMbDZDyiunMklK-9kKzMroha5_igjJbjPdM17x5hRfaXTeDXXz_Xmg3F-8GOV1laFS62rzzaOANh0HThFwO05wumbXnpVGAI96lY-j7izzvQj-K3SSF_stz_VGzdPhCtveqXLLUIIklR-rp-WT7xv5lpNqoHnUv1kFB6ZvCUasOT0pVeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63eda0fef9.mp4?token=EMnkJxinla-sgLrJ2N2YL41VyakEuZCC9kZkn044hg7dAjbWUTh4FbKQMYGo_7Q5KpUAATESbDjrxYLD8_vX_Q5eeomCHxMxIn8cpix2IgArGsMJCNjZHOORYiM98qsvKPgGA_eIDAtpt8KOmEtCQCIDaJnIxcKObfu95HiKRu8LCwqSXSIA_AGZtTYGtBVBloAxHH1MPnTg4JvpDRDpsVFBbAMNJ7bYZao-M-yvUnrdhwWMtsTOrSeic54ZLMIEHRU8zTLIhrdbeCyQVmNWPZrGdJoSyUv7f6rYLupMIpKkUE-7vON7NqobNttZs2_NkSW0hjYrxXOWWeJqzcbu2in8mSPTB1cH2w_ijZgpLoFnpuNOxI1f5cHUGGqn19j3EbzW1AXaxmSxiCF9YI3bphgAdUtonqY069eNtAkmpIVvnveNkgnXHECa1_FU-btGdgEmJit6Re8MRxlN6XQVfYvpiXgp-qUKx80BSX1lJOWgLv5Pos5o7h_UvjJMbDZDyiunMklK-9kKzMroha5_igjJbjPdM17x5hRfaXTeDXXz_Xmg3F-8GOV1laFS62rzzaOANh0HThFwO05wumbXnpVGAI96lY-j7izzvQj-K3SSF_stz_VGzdPhCtveqXLLUIIklR-rp-WT7xv5lpNqoHnUv1kFB6ZvCUasOT0pVeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نامه سردار سید مجید موسوی فرمانده هوا و فضای سپاه در پاسخ به نوجوانی که با پویش حفظ جزء ۳۰ محفل ستاره ها شروع به حفظ قرآن کرد
🔹
از اینکه شاهد رویش‌های نسل جدیدی از فرزندان مومن و متعهد در کشور عزیزمان هستم بسیار خرسند و مسرورم و مطمئنم تا زمانی که همچون شما دلیر مردان جوان، با ایمان به خدا و روحیه جهادی در این کشور رشد می‌کنند دشمنان ایران اسلامی ما عاقبتی جز شکست نخواهند داشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/690131" target="_blank">📅 16:54 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690129">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
وزیر کشور، برای دیدار با مقامات ترکیه، عازم آنکارا شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/690129" target="_blank">📅 16:46 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690128">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
استانداری هرمزگان: شامگاه دوشنبه دو فروند قایق صیادی در حوالی بندر کرگان در آب‌های خلیج فارس مورد حمله پهپادی دشمن جنایتکار آمریکایی قرار گرفتند
🔹
در پی این حمله، تعدادی از صیادان حاضر در این دو قایق مفقود شده‌اند و عملیات جست‌وجو و امدادرسانی برای یافتن…</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/690128" target="_blank">📅 16:39 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690127">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار مشهد</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cc8c949d2.mp4?token=F8yYyvVs8Wa0dHCN0E2t-E0IhNoIXGlHMGWNUBarAGCXHd_zxnVqhqbNB_kAR_E7l2QSqz_y_mhu-0b6UWl4oViBC6TSagjvvmh54DG2bn0UsxJ10lUCPDaDT1qy22y1tk-yr5vOCyRgk3_5wLwqRwkx5ht5ZVLgNv-wXR3U0vcLZhPyXIToU1fwVz6MXwT88KhBan2BtS1VroMSAli53zjgqFFppYlg-gKF5Z8mdIFg2bEjoBRjZ5QJaGnAylkBtxPGB3cH1R6B1dAcInS-GzTUDjJVT-G82UhVz5y48NCTvbzz8_Lkzhbrvjg6m6fykUrYH6ZoCeYPLyvCrsDslg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cc8c949d2.mp4?token=F8yYyvVs8Wa0dHCN0E2t-E0IhNoIXGlHMGWNUBarAGCXHd_zxnVqhqbNB_kAR_E7l2QSqz_y_mhu-0b6UWl4oViBC6TSagjvvmh54DG2bn0UsxJ10lUCPDaDT1qy22y1tk-yr5vOCyRgk3_5wLwqRwkx5ht5ZVLgNv-wXR3U0vcLZhPyXIToU1fwVz6MXwT88KhBan2BtS1VroMSAli53zjgqFFppYlg-gKF5Z8mdIFg2bEjoBRjZ5QJaGnAylkBtxPGB3cH1R6B1dAcInS-GzTUDjJVT-G82UhVz5y48NCTvbzz8_Lkzhbrvjg6m6fykUrYH6ZoCeYPLyvCrsDslg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔸
فیلم وحشت مسافران در پرواز کرمانشاه به مشهد
🔹
ویدیویی منتشرشده از داخل پرواز کرمانشاه به مشهد، لحظاتی پرتنش و دلهره‌آور را نشان می‌دهد؛ در جریان این اتفاق، بخش‌هایی از کابین هواپیما دچار آسیب و شکستگی شده و مسافران لحظات پراسترسی را تجربه کرده‌اند./رکنا
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/690127" target="_blank">📅 16:33 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690126">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
استقلال با نخستین پیروزی آسیایی مقابل السد، ۱۰۰ هزار دلار پاداش کسب می‌کند؛ حضور در لیگ نخبگان نیز ۸۰۰ هزار دلار پاداش دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/690126" target="_blank">📅 16:29 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690125">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d0bc4d3c9.mp4?token=pCCIUmKwK3nUv2DWBr5ES6d5N5-XDmhmrdzuHnMEgw72ra5d0TprvkQyVpPTfO2MkbEqASMjtqVa9KtJd6kbTzMW6FVIdRfrZKKqGJkqxfYNghGijcICurdyM8_-exx7c7YvfSXewgpeaNguhzlFsrQRG_nKvXjGykyCyf6GdMxW2xtkp7G6ElYwa6s8IM8YO4l0poQLvF6XJGbg6vIbbwKsXujSByc6a-ytGWSyi4aYJqS5v9ztb_fK9dHQWYGMYsU47J_Yj85U6GlAijdr-EqcldGbaAOaio1ls_4Jbke4GFxteWlDm6pQdvbq5ljcXhmT3buPmjg7Z_mnqJj74g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d0bc4d3c9.mp4?token=pCCIUmKwK3nUv2DWBr5ES6d5N5-XDmhmrdzuHnMEgw72ra5d0TprvkQyVpPTfO2MkbEqASMjtqVa9KtJd6kbTzMW6FVIdRfrZKKqGJkqxfYNghGijcICurdyM8_-exx7c7YvfSXewgpeaNguhzlFsrQRG_nKvXjGykyCyf6GdMxW2xtkp7G6ElYwa6s8IM8YO4l0poQLvF6XJGbg6vIbbwKsXujSByc6a-ytGWSyi4aYJqS5v9ztb_fK9dHQWYGMYsU47J_Yj85U6GlAijdr-EqcldGbaAOaio1ls_4Jbke4GFxteWlDm6pQdvbq5ljcXhmT3buPmjg7Z_mnqJj74g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چند ترکیب خوشمزه و مقوی با خرما برای یک میان‌وعده پرانرژی
🤩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/690125" target="_blank">📅 16:15 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690123">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A37w4d_YUvuXv6iz_WAYth--wlWUv4xZaLUOTqynX4THTsWwRtyFhsno0mVzfYKQNgjTnQc_Cp4AxQSjxtT3FNUilb8vBYBc7-GkaDx1nJ8hp1fW-qZur-BB_gMQRj_xTvHeELEicDn-1t9mGS6-Zg74iIKyTFxxoh_T66DMUcHu2baaxiHLpSm1wzYmxb1dsJZZC_KPvJOHSAsVMDshi-AhwxJtlPtbLtkA-kujENAyDvqMwuhMaq4ab7dnae5k1tGbP5V4gQ6sp07YnkqrCKz4qzkMSyPSOc22Ztau98Jhe2yu_hzkArAqYuMdE0z2CAAEXIX_BYC6NqU5rvDKqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آغاز دوره‌های آموزش نظامی و امدادی یگان‌های مردمی جانفدا امروز ساعت ۱۷ از طریق ارسال عدد ۱ به سامانه ۳۰۰۰۱۱۵۵ یا سایت
janfadaa.ir
🔹
نکته مهم: با توجه به محدود بودن ظرفیت دوره‌های آموزش مقاومت ملی جانفدا اولویت با کسانی است که زودتر ثبت‌نام کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/690123" target="_blank">📅 16:05 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690122">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf0869ece7.mp4?token=RZNjqnFXUtOlfmAXXX6FTiE0iAqzEb8hba1dWzFiNKCoLrP8XEQEkGzhKOie4lEHONXGF1YJGSCueuhb2JHLX9gw3o5BqDIVpf4Aal1OVU9TNwKIVi6FuSSKbi8iNS59oyw1VeM4rUJAN6WUl4fYelPaYR0XlPCqy1Tc1jAjKTaSE7SeGuXf0TTCequHvcizRxQ9rJzu7GaCTJq2y_IbvfPTlmt-lhuhFCsMnvQFACsj5WCYiqmS1q7S6FYGjII-I3H3HTwdPyOsuXpiKLnNz9PU3zLlON3m_vagoMUdrHhZI1NVvfc-lwFlCN1AR5Q7a0GfvXS8qXee6jv2LcFSJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf0869ece7.mp4?token=RZNjqnFXUtOlfmAXXX6FTiE0iAqzEb8hba1dWzFiNKCoLrP8XEQEkGzhKOie4lEHONXGF1YJGSCueuhb2JHLX9gw3o5BqDIVpf4Aal1OVU9TNwKIVi6FuSSKbi8iNS59oyw1VeM4rUJAN6WUl4fYelPaYR0XlPCqy1Tc1jAjKTaSE7SeGuXf0TTCequHvcizRxQ9rJzu7GaCTJq2y_IbvfPTlmt-lhuhFCsMnvQFACsj5WCYiqmS1q7S6FYGjII-I3H3HTwdPyOsuXpiKLnNz9PU3zLlON3m_vagoMUdrHhZI1NVvfc-lwFlCN1AR5Q7a0GfvXS8qXee6jv2LcFSJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ملک بخریم یا طلا؟ کدام تصمیم بهتری است؟
#دارایی_هوشمند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/690122" target="_blank">📅 16:01 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690121">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/888f1a581f.mp4?token=LXl1WKAUd7h6gK2mc-A9NEzZqk25qYdojjg7-1awqceH4VVwltLJoeFAs53wWZu-75w5N4tZYFtPQbfoh6nCyGIkxHaMvDT6ecb05oCzZPtjlL8u5cyZqxEtfhfG1jEopEGfEDBDRtq2sEynD4A21XD82pqZsKOxMPmK00LRsDUTU61GYwWvfzKS2Qn8imblWCDwlyR2-4rFpevTX146xdkXKlj5yC0FcPZbNz83DfUt9kcKWFaPke2o0npmGwGt0LYR__suspg24Kp6Hv0bJlrsDWjgjMiVCLrQ-06egArmLMYBNldpw3YwJKGmhqDiqavnpaPKW_ajsMZrIupMlTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/888f1a581f.mp4?token=LXl1WKAUd7h6gK2mc-A9NEzZqk25qYdojjg7-1awqceH4VVwltLJoeFAs53wWZu-75w5N4tZYFtPQbfoh6nCyGIkxHaMvDT6ecb05oCzZPtjlL8u5cyZqxEtfhfG1jEopEGfEDBDRtq2sEynD4A21XD82pqZsKOxMPmK00LRsDUTU61GYwWvfzKS2Qn8imblWCDwlyR2-4rFpevTX146xdkXKlj5yC0FcPZbNz83DfUt9kcKWFaPke2o0npmGwGt0LYR__suspg24Kp6Hv0bJlrsDWjgjMiVCLrQ-06egArmLMYBNldpw3YwJKGmhqDiqavnpaPKW_ajsMZrIupMlTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
علیرضا دبیر: در فدراسیون کشتی جاسوس داریم؛ ۳ سال برای مجوزهای معدنی دویدیم وگرنه باید گشنگی بکشیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/690121" target="_blank">📅 15:54 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690120">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/An8W2aYFUG73q8jMZTtxtzr5Y_C58pxYuLKCJsnIX3cCpSuEgXsvRq-2fGerQKjQCS0nkEp2J3x8vwYPGfGT-q3gVr_aH62pvVKgCCCfVv1zHAYJN5sHwt0LOfH4JHHzfXx6-QVPibWkgXqCzImi2mzEF3RL9XjsPYPuiyKKwqd4lFhZJhcY4qWA_DqbfVCJepsmdb7mJWCMFuIcS-QDh47NWsh0GtABtjK0xZAx_CcC1B4YwnDA5u1B6jCRU55Ysi2WJkyApHjrOWKORubC9yJU9WaIQdqXlCcRZScJp6WjrCecuRRLN4Xkom_BFaUxcdgWIyHF8iWtlx-qAQv_Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بریکس؛ فرصت فعال‌سازی دیپلماسی معدنی
سیدعباس حسینی، عضو هیئت عامل ایمیدرو:
🔹
در بیانیه پایانی اجلاس سران بریکس در دهلی‌نو، برای نخستین‌بار بندی مستقل به «مواد معدنی حیاتی» اختصاص یافت. چندی پیش نیز چنین اتفاقی در اجلاس سران گروه ۷ رخ داده بود. این تحولات نشان می‌دهد اهمیت مواد معدنی حیاتی و رقابت جهانی بر سر آنها در اقتصاد سیاسی بین‌المللی، هر روز ابعاد گسترده‌تری پیدا می‌کند
🔹
از سوی دیگر، نخست‌وزیر هند، به‌عنوان رئیس اجلاس بریکس، نسبت به «تسلیحاتی‌ شدن فناوری و مواد معدنی حیاتی» هشدار داد. این موضع را باید در متن رقابت فزاینده بر سر عناصر نادر خاکی و دیگر مواد معدنی راهبردی فهم کرد. چین در بخش بزرگی از زنجیره فرآوری عناصر نادر خاکی، نقشی تعیین کننده و مسلط را ایفا می‌کند؛ هند به دنبال کاهش آسیب‌پذیری خود در برابر تمرکز زنجیره‌های تامین است؛ روسیه و برزیل از دارندگان مهم منابع معدنی جهان به شمار می‌روند؛ کشورهای آفریقایی عضو بریکس نیز از ظرفیت‌های معدنی بزرگی برخوردارند و در عین حال به سرمایه، فناوری و زیرساخت نیاز دارند.
ادامه خبر در
👇
https://www.titrtejarat.com/fa/tiny/news-10937
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/690120" target="_blank">📅 15:51 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690119">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6cfc2473a.mp4?token=WQNpFi0EnOPhi1_yWso-TvWaRxf-R6xTsbvMyN6P_vg35Gr-EF3SsJXGao9EaWGbJ2CHWp7erqDzdfzm3MGWFf1Xea5oH2FlyCwZzRef55MmKdZzOa1hMYlqs7PdAq5aTEjj1Xi7IXD2px83ZHU_dFMmcbOfakWCQnKyNr8PNKV1-voDaAkh9GySF3toKxdU1kGDaB4PiWcvbEiMY_bkpuGZJqDUlS46S9TkbxC6efTAS8DeJ45CFIWt-YWYTMyLabdqNlBIC3bvM2FMIekYSD58JuwzC2blE0VT9F6nFVnpSRQBMZHpuZwNLuTljVf-n5SNKaSXikXAT-hOBH0ywQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6cfc2473a.mp4?token=WQNpFi0EnOPhi1_yWso-TvWaRxf-R6xTsbvMyN6P_vg35Gr-EF3SsJXGao9EaWGbJ2CHWp7erqDzdfzm3MGWFf1Xea5oH2FlyCwZzRef55MmKdZzOa1hMYlqs7PdAq5aTEjj1Xi7IXD2px83ZHU_dFMmcbOfakWCQnKyNr8PNKV1-voDaAkh9GySF3toKxdU1kGDaB4PiWcvbEiMY_bkpuGZJqDUlS46S9TkbxC6efTAS8DeJ45CFIWt-YWYTMyLabdqNlBIC3bvM2FMIekYSD58JuwzC2blE0VT9F6nFVnpSRQBMZHpuZwNLuTljVf-n5SNKaSXikXAT-hOBH0ywQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معاون پزشکیان: حساب کردم اگر بنزین ۸۰ هزار تومان شود و برق و گاز و... را هم گران کنیم، می‌شود ۷ میلیون یارانه به هر نفر داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/690119" target="_blank">📅 15:48 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690118">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
واکسن آنفلوآنزا از اواخر شهریور عرضه می‌شود  سخنگوی سازمان غذا و دارو:
🔹
مردم به وعده‌های فروش واکسن آنفلوآنزا در فضای مجازی اعتماد نکنند. امسال واکسن‌ها از منابع مختلف از جمله چین، روسیه و فرانسه تأمین می‌شوند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/690118" target="_blank">📅 15:43 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690117">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gsn7iJfqj9WD0yKVV-3cFgh0vpkJUJ0pFa1REAG8BGfLv7ZQIs_uNfeoSxx_dl2aCR2kv9NPW4JdN_xpXWw5Mn03xT1mzRoiziMU79_iui3GXpUKUEt1zfL_U5lcEUaktwp-x8w9yzB5FGHRg46bgYlU7GdXigSGUF2LMWQA_Y5y2jVn4rLQiQvaI0mNmAsz8T1Hqeo49igmh_Tyh25F10Q5ErvoFexOEXTMxtDXgu0scWRqCETgsN_fFmwEiZxu6WrAlOnu6Y6B8femyd9jAg4JOi3bwASOwOsnbacw50f3GSNkP-T9BgintBLxSCgeN0Dfp5oTa1MnKVb7fSGGNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رکوردشکنی قیمت گازوییل در آمریکا
🔹
میانگین قیمت گازوییل در آمریکا امروز به رقم بی‌سابقه ۶.۲۷ دلار در هر گالن رسید؛ رقمی که حدود ۲.۵۸ دلار بیشتر از قیمت گازوییل در یک سال گذشته است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/690117" target="_blank">📅 15:36 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690116">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
پاداش ریاست جمهور بدلیل فداکاری‌های نیروهای مسلح در جنگ رمضان، امروز واریز شد
🔹
ستادی: ۱۰ میلیون تومان
🔹
عملیاتی: ۱۵ میلیون تومان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/690116" target="_blank">📅 15:32 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690114">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JydaHfIyji_JyF8RWNGDgLvI7r2tFdn01sLh7x1Tzet8X6uh8oO2fCN50ziWTA3-TLrwrypNPg_7mjjnpmMY_DGMpvLp6w45OKL3QicTwAWNT8McSj-ORXVYrLTPHfE-7cmASokyXCgE11PhxVKQD3sFrfhzxjWszuUm0drDgKZ31BcTc3nhJKjbN9Z5t_AN7hDWXfqdi8DBSKUGRZ_3vC7jPUBiRyevW8Y7uNi87tys-PISN5ImYdvcecKnPlnDXU6AH3g2Qo394pRQgM1me_cpUnAp35z3_76IsdJedFM-c32lwHCiphndc14h40kMaT7aG3KZFDbgtJaYBqjttQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F86NynLMNhZbNCxyZG43EYqVZJ3Dq0a4SzCyrfZv6MSp5oK00iHJESZ9S4HMF8zntVakJ_hagdxSXQQIzQeEFTfyv8WgNIKzswK9mbIOF5lIiEYzp_nB7JwTfWYTbWvaxQ-XwxQi1Cs-EYZa9Hp3YYPq-q3n6qi1EPSSM_vvi6NGNHW09RFPf4gHwey0cmdbM9Eq7xqmL1D8-EJduEkWxH6LPZ_DWeLyPnAAkO4RiUxJCU6IAFsWqXSbfePP6SW2Gxsnar-bz_O6sRCcOqRyReE0f_0GcTYlJDIO6Pe0OT0loK544zuwVNmRlI9rhQIgvvOyVanIWDuKqDBtwYefKA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
سوزش رسانه و ‌مجری شبکه ضد ایرانی اینترنشنال از فراخوان و سازماندهی داوطلبین جانفدا تحت عنوان آموزش های نظامی و امدادی
🔹
این جیغ بنفش رسانه آمریکایی-صهیونی پس از فراخوان آموزش نظامی و امدادی داوطلبین جانفدا که امروز ساعت ۱۷ از طریق سایت جانفدا
janfadaa.ir
انجام خواهد شد، درآمده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/690114" target="_blank">📅 15:29 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690113">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BIrK8U3K6IUVNhN-29A0wmm-6Pg7inDbQOUBAmcs1BTQ6Px6ms_E9DSRFHADRP7JFx02smE06Da3t8LXxxb8XIJtk8MBn_rzR5ZLT6bPE1mlj6hgRTFGULGjaX5LmAHsB4rvYJwWG-fr5LdFmn21_tivuaTXJS6PR-VvRD8K4VE8Y7jkVio1RiXlx7G-3XGBYexe4B9gzmuTQA9CF0gJHWOZiHiqnfYSQOqc1UU2fq01pdCZn3UhwoaiCz1Gl9d7EEATRl_4PBYyvKcBc8X9kiBhUqMWRwQQfabWXT6cKaE9thV-4bOdRiajkzHvBky4FyjBTHckkg5beX-h--TdpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمریکا اصابت جنگنده اف-۳۵ خود با «آتش ایران» را تایید کرد
🔹
پنتاگون برای نخستین بار به‌طور رسمی تأیید کرد که یک جنگنده رادارگریز اف-۳۵ این کشور در جریان مأموریت بر فراز ایران، «هدف آتش دشمن» قرار گرفته و آسیب دیده است؛ موضوعی که پیش از این تنها به‌عنوان «فرود اضطراری» یک فروند اف-۳۵ اعلام شده بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/690113" target="_blank">📅 15:24 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690111">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sNvaMx9g7JG5iTbDn6wL9XNYsVdA0ZlVpWVBegMbtGFkozcEBwbDLw_hVo9EQyiTOydJi3QAewGBRQGBXgMPivpcsPrfx4C5EscpJ1sBpNN6wgC9UZ4nVCu5boZh4By64ZExFuJk2kleH5ml-s1hbaHIafAsjxUv0_p2vmsAGpL4bGTFIWX9SKrgxq1Dc4rKXV6f3Nts4mpfFjKn-05ZpLKdF8QxyOJARJuByADfXofX_ay5sx840tmi0NJXMCTy1T6fUJoAjon6Ii2NOlgHGzvHn4kwYo0XxcZuz8rwZyq48MORobJqBah59tzgfaIJ3D69oX6sriNl0k_J-khplA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BurpcgSZuMxxK21Q9FSO8ZNyePrd2h7yJTWMZI2VsU58jP5LXCW0jFXBtxeiqs-PqxTskIbpzRndZnLelgJ-xnIGM3DsiU22gelVyj62VlEfzV6N3eaS-s3WsSBHULpsSZK5KUHRx6CEsFk1pvH-iu4i3wFa2AcfwoOSEbh5KWB2QncnluLlJe9hbSEYu5gXwRBM3UCUdpWrOl-h1SRIPifNNUGHAuEk1tnhkvIlyictLRjCqxfD2ljcmqfAag3lxBytoWIJUNa-Fq5pIZFmvDzT9YHulF1r2rtCxgq1-BohaILZ2RRKGqedKyfOpYYt20JOGxJ0pHfqvvHUEekkww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">افت تولید ایران‌خودرو و سایپا در ۵ماهه ۱۴۰۵
آمارها از کاهش قابل‌توجه تولید در هر دو خودروساز بزرگ کشور حکایت دارد. تولید ایران‌خودرو با کاهش ۱۸٫۴ درصدی و تولید سایپا با افت ۴۳٫۹ درصدی مواجه شد.
@titretejarat</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/690111" target="_blank">📅 15:21 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690110">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IS6-DWJj_05Nd1BS-ExXbqhKnBRNAEqGxZEOSrYCpHI9H78PDQ_eOmBUJwOY8WZpmnX8W6x-dr_WZ9SdpXvsTGN2s6GbAI8B52rpYVJEC48eu4zUJc8K_Dvtk1RZMsiAtpcocKHhAj4ynfHuPqsq7l0Js1rU2ZgFkOKke-DPg5tLTaB7R_qpEiOPvb4tdp4yUnRIS1HVXUyx0lFwHDslkZGlQioULGHslmJefj0m-kxapM0C1sgKB3ZernyS935rztcSu3Gcl_Bki4ySRrIB9CVIDrKmtNdTzRv6wyNnUZ1ANqQ2LISyBicYRQsWVyiHI52NSYcxJ5icDNDcSYIxbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نمودار افت شدید درآمد قطر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/690110" target="_blank">📅 15:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690107">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vw5x07DsFdLZ35dn9Eaf7YdcfsRzt_8LCCfw7yY_BgbD0yrmkoO0jsigd788xZywWXVXdKOJj0zI0wmlJ492Ajx6tH-iHPyjpstF8fNIDspYkZ1YbrlEFQYuHYhnEBeH9z4Lcwiexqqk31RvojkKJH2Hq58TfWEbl7_p-pr7hZCO1eHH3b02fAxZS7z70IwDfqKqqAmpY1OBvzVv_xBYrUiCb0XRNKFGNQruOTXAPTbKzPHWETBDNub--DRoEbXuo4nJ3QWCv4mGIP38XIiCsHUpd8-yr8N1ITj3V9AGUc3YLyVrty4MqwxzIHQcBgrOBUnY9XInI3lHK--WImzEQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QqNd1l4OUSc-fOuJ-zipnPFwN9D03NikD0KP4xRHCSbbAc1Dc5xwAi_pv5QQMpQoz7fpVQYerjZxM9mJEoL6FO71SFD5wTNbSkGD1O66uRhNK0zASHp-6-KwN1LAHolaxPWRd6XiOYAng433F2t3GGK2SNQYnl2R44aZTAAdS60XV7AsXxQDU2g783I0uUdSAPRAU4F_t3_F02oUo-Os7vRAhKNdbjmHOMCnHRBBCMO3rBDO9CvUz86gpRZnMU9KfFSoDhsl_aXZGAl8VoDDiXeifoXEPlGtiWZCIZjacHWWUvtpPyMiSIHtYmH6MZpUYGXCA2LCjUHNoEInLs5OVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HErwarXiEUlqix-ZoNAaLzBfenhE_joq3NVyTnRywI3FGNL1ZJl51gYb4jcS-R-00x1_XRPaHbtUOU9VaxWItH3LgUpYlLIgZoAzEx2cMFJPCKTq4pk5NjfWje1RikTkJ6mvmJN4mFNiggoamfEf1NcmXeE5N829mLDhbb6UcInl4t2PpYUu2q8bKu0GqWyymTKJsNlg6lSAVqB1eEERGRks8m7tmpgFkKNgpmpFt7jiphi6ZnjedzsT4rB0tUlKXySjWnBKXs8VZ20LF8UHDRYBRealXjRynA0jPkeqhHz_rnHon7UobnYlH3I1z5utqtXi9iP6_UKbQRNUYXigJw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
هویت خلبان آمریکایی لو رفت
🔹
پنتاگون هویت خلبان اف‌-۱۵ سرنگون‌ شده بر فراز ایران را به دلایل امنیتی مخفی نگه داشت، اما نمایش چهره او در مصاحبه با شبکه سی‌بی‌اس، عملاً شناسایی این نظامی را ممکن کرد؛ اقدامی که کاربران و کارشناسان نظامی آن را یک تناقض و بی‌احتیاطی امنیتی دانسته‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/690107" target="_blank">📅 15:15 · 24 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
