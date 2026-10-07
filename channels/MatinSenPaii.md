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
<img src="https://cdn1.telesco.pe/file/hsYpDWebHjyBXJ0oNvX6tycXeLZGp4ojsOnVCD741QdtED2w3R-vePb7s0vXRMBEIySfSUPKx87FN5CoUIeFLXaMrN2Z7WQumzfb6bkAX25oJP2dKHDWTWQ2aDUq_9G9AekCMAaA9KeSWVhCiToGbS6z4oLsGNOKmPxPswqQQj7eaDPKcQ0TRy0XI7UelkwEss85ZQuLq8XqrsBzGiGSmaGVMTox_seJsWI7CLdf1JqPM_xvkXw2JyGEs-Fns5JJCzpjj5smUPCTp78r7jiEa7m-No6r8V0GZ-KIUtQ6T-7p7Jmfut5IyGBo6wfSPkEa0jSejttGuoFLXupD_48KeQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 154K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)ارتباط با من:https://linktr.ee/matinsenpai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-15 20:36:45</div>
<hr>

<div class="tg-post" id="msg-5540">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">دوست دارم چیزای واقعی بسازم توی ویدئوها. محصولات واقعی
و فکر میکنم با ویدئوی بعدی
یه قدم بهش نزدیک تر میشیم</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/MatinSenPaii/5540" target="_blank">📅 15:41 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5539">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">برای ترجمه و کارهای روزمره‌ام، اکانت آنتی گرویتی کم آوردم گفتم به یکی از بچه‌ها دوتا اکانت بهم بده توی پنج دقیقه بهم داد:) اصلا باورم نمیشه و چقدر ارزون. یک دهم کلاد یک ماهه، 18 ماه داد هرچند خب استفاده‌ی دیگه‌ای داره کلا.  اگر که اوکی بودش و نپرید و اینها،…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/MatinSenPaii/5539" target="_blank">📅 15:36 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5538">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">رفتیم توی ویت لیست اپ Muse متا ببینم این چیه که همه ازش تعریف می‌کنن</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/MatinSenPaii/5538" target="_blank">📅 15:11 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5537">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">Math lovers, check this out:
https://github.com/openai/math</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/MatinSenPaii/5537" target="_blank">📅 14:40 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5536">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">یه skill واسه claude و بقیه اجینت‌ها نوشتم که اون حس اسلایدشو رو از ویدیو حذف میکنه و با استفاده از ۸ تا تکنیک مختلف که برای فارسی بهینه شده، موشن دیزاین‌های جذاب میسازه!  تکنیک‌ها رو از حدود ۳۰ تا توییت motion design درآوردم و بعد با کتابخونه harfbuzz واسه…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/MatinSenPaii/5536" target="_blank">📅 11:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5535">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/135826faf3.mp4?token=j6Tr-Km50ekSKjslcuYS-eeFNzIYND95NIKOscC8xJ55_6d78iSJlDUWgTDVv6n_bug5tJa38gwMXjNklUKs9ft_3grgngqIB_BvM8AS_NDJTKD5JMLya_B5r55cyns2W2NCjipbSZ7KriFYi0KWbHz9pkKKNhnwqp89NFM_l4xfMd91thM1AkRsfhEl4Kd2u3Jze2biHZlT-FVawSaSznhhBpmjdSRBO_TcffQRu6MMkdnKVHX-5K24LxwTg_ZItebNcwwUmOIX1B3z3-dJbf-XdGpzVWmv4lqfx7A3fyPwL2edr0ghmX0PHCnf9_ou-ovjCMeDSXQPVJCaIGB1_yamQ8YLwI5Lag_6coxBUxUTOkwsXrEjd7SmYOL5ubFSUYFz4Lh8DIC1vWIlDUyZX7psTSHiDpOxYrEACrZ2BDM0IXLfELzcvEnKh351la3NJdLM99Dmt-JMVE3gvyu-YKx33mEe34RmBFnM2A85HlJfORLcKhqpI2L6TZqysb_SMnHV0WnjBRSMdE2jRcjLbQoT9WnXwkNiWMuTySkQCHSKJMtsq7woNHoPtMrTljEMDtgumkHlcgZRLy6Kuxwj_Dx0hnjGEfztpf6MSejbiiDziKfSgHZlTxaY0pzmZkv8Bu2THwMR2BtpjPM8kU6OB9gi3n0JF-ipNY_TbvqgDu8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/135826faf3.mp4?token=j6Tr-Km50ekSKjslcuYS-eeFNzIYND95NIKOscC8xJ55_6d78iSJlDUWgTDVv6n_bug5tJa38gwMXjNklUKs9ft_3grgngqIB_BvM8AS_NDJTKD5JMLya_B5r55cyns2W2NCjipbSZ7KriFYi0KWbHz9pkKKNhnwqp89NFM_l4xfMd91thM1AkRsfhEl4Kd2u3Jze2biHZlT-FVawSaSznhhBpmjdSRBO_TcffQRu6MMkdnKVHX-5K24LxwTg_ZItebNcwwUmOIX1B3z3-dJbf-XdGpzVWmv4lqfx7A3fyPwL2edr0ghmX0PHCnf9_ou-ovjCMeDSXQPVJCaIGB1_yamQ8YLwI5Lag_6coxBUxUTOkwsXrEjd7SmYOL5ubFSUYFz4Lh8DIC1vWIlDUyZX7psTSHiDpOxYrEACrZ2BDM0IXLfELzcvEnKh351la3NJdLM99Dmt-JMVE3gvyu-YKx33mEe34RmBFnM2A85HlJfORLcKhqpI2L6TZqysb_SMnHV0WnjBRSMdE2jRcjLbQoT9WnXwkNiWMuTySkQCHSKJMtsq7woNHoPtMrTljEMDtgumkHlcgZRLy6Kuxwj_Dx0hnjGEfztpf6MSejbiiDziKfSgHZlTxaY0pzmZkv8Bu2THwMR2BtpjPM8kU6OB9gi3n0JF-ipNY_TbvqgDu8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه skill واسه claude و بقیه اجینت‌ها نوشتم که اون حس اسلایدشو رو از ویدیو حذف میکنه و با استفاده از ۸ تا تکنیک مختلف که برای فارسی بهینه شده، موشن دیزاین‌های جذاب میسازه!
تکنیک‌ها رو از حدود ۳۰ تا توییت motion design درآوردم و بعد با کتابخونه harfbuzz واسه فارسی بهینه‌اش کردم و نتیجه این ۸ تا skill شده که اُپن سورسه و می‌تونید برای ساخت ویدیو استفاده کنید :)
https://github.com/atmirrr/persian-motion-director
✍️
AmirAnonn</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/MatinSenPaii/5535" target="_blank">📅 11:09 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5534">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">کم کم دارم فکر می‌کنم یه نسخه از خودم کلون کنم بذارم هرمس جام کار کنه
🍿</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/MatinSenPaii/5534" target="_blank">📅 00:46 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5533">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mw2g_1aG6RSM1jcfYGRMKjE3JqWkJ0xpvp44lC_lzifRkKJSW3rMAs8a5yrEd9cIuttuA_aumCVdybRITLz_9r8Mo-j7a7CJh_xBKH1L2mGThJD0hqNLoteJZqIStjLdfIULVvPb_c-sQ4AfDMOYAOJtyLzjtGeyTmakA19jDwMDmrIlM2AVRrQFTQbxw-9ob8KQgFff2TcWAcEfKpfQlFnh8GQkACzdAvJyF3GxA1XixnesAxWLz_LzZ2EAvi86deDMmrA52bsi6aA9h5wYUvwBD8SxxAVTHva6cePQrX26zQbiZ_pq9OsUqYuF5b1BCCV4kdCH10KQEFLKldV8bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپلیکیشن OpenChamber؛ یه اپ موبایل جمع‌وجور برای مدیریت سشن opencode
نویسنده این پست توی ردیت گفته بود اولش فکر می‌کرده پست‌های OpenChamber فیکه، بعد از تست کردنش می‌گه در عمل، به طرز عجیبی خوبه؛ جایگزین opencode نیست و همچنان opencode رو روی سرورش ران می‌کنه، فقط با OpenChamber از روی گوشی به‌صورت نیتیو به همون سرور وصل می‌شه و تسک می‌ده. برای کسی که opencode رو ریموت اجرا می‌کنه و نیاز به اپ موبایل داره، تجربه‌ی تر و تمیزی داره.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/MatinSenPaii/5533" target="_blank">📅 23:26 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5532">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kKo9zZS0j-HG80O7z6iGF-1QN_4-cyB3Bb2YSlSsrplRXAOumKMPrA6blX4gYtfO8kG2Fwtkm6dF_nZ3BNIu3AEEjcnjVEr4Zkf2NVj-3dWccuHtfmbW6rN8zwcyI2dUIlaG1fZQV5OIp2qVz49PooMCRYuC3f23GT2ECGCS8HxtKQotAj2CMS4sjNHKvr6bdl4xyg7CwtBJ9JGajxMMhqUZENy5xSQqKPIN3wRshSjwJqFUQ28THCq2GbztzgEJd-Ts2BrPRVjBiDtZF6oJLLPgu-ZTVNmNXeuEC4fKddAHKamE5iI_tQKkopdg-3-aUdfda7h9_sDY2Al9zILTtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل نانو بنانا 2.1 اومد روی Google flow من، و افتضاحه. اینجا با GPT 2.5 مقایسه‌اش کردم:
https://x.com/MatinSenPai/status/2107527090019131503</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/MatinSenPaii/5532" target="_blank">📅 21:15 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5531">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">اینم کانال تلگرام یزدانه پرسیده بودید توی چت فراموش کردم بگم:
https://t.me/antimatter0x1</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/5531" target="_blank">📅 18:05 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5530">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gx8Dgrq4jaeU2436IoX7IHhxBqp8qWXAWrQsd2Au_YGH1iMlspQBSU6T2igtsYSQz1XAs5niWX3JodwkblPIlKf-LW60dOe0slAeAk5WvtOCYuEA9ORO_fY-WR3VXMkez8JvMOIFrWhyaLG-5toKSUurBtNCaoTdf0B1Z8NihGZy9nA8Y9kIGKtE-O-pkD2hiolBTRB-4TIEleLputQ8kDr3J_E_7TXNjhA9sHrgQAzI_keR4Koy1xhbLFgqNzzhhYuW933xBhb_DTBlUFOaE_MVemVrkRCXk4wzx1HRYfrzJCNSvSkaxX2qePfb7tMXc_eStvuQZ-b-bnWWeNAmaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لایو تموم شدش
می‌تونید از اینجا ویدئوی ضبط شده‌اش رو ببینید:
https://www.youtube.com/live/nbOls9zPckM?si=xnkhmSfdlmhENs_2
توی لایو توضیح دادم که همین overlay رو هم کلاد توی 15 دقیقه زد قبل از لایو
😂</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/MatinSenPaii/5530" target="_blank">📅 18:04 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5529">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">لایو انتخاب رشته و دانشگاه بریم یا نریم برای برنامه نویس شدن؟
🥸
https://www.youtube.com/live/nbOls9zPckM?si=dnW0hyhkqq7wyJ4-</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/5529" target="_blank">📅 16:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5528">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">نانو بنانا 2.1 توی Google Flow در دسترسه(رایگان) با این پروژه می‌تونید کانفیگ مناسب وارد شدن به Flow رو پیدا کنید: https://github.com/MatinSenPai/Gemini-Config-Checker/</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/MatinSenPaii/5528" target="_blank">📅 13:35 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5527">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KPFrp2HmvQfQAj6KhL0cV9UXAG1Pym3W60iHzQRNMMP7P51LyaZk79Np2mcptLewHvmtIoP_qKSI4bberdglp2EX8LW1CececxOd5HOQbm1PKoj2Yk-BwXhs3AoAIVMRImZYc-so7qPPlTekJtjzpqQFP5q9uxcBfjWTJUbMSJPoT8xGpeqeoNQQhQYIk2I2-TDJv-3rg6_FUdmDbjpm_bER4YvgDUFUUFropvx8dNgGfpx31ffIsfjQ18h70qf7ftL-_QwmV8NtbWgHhbSHchW3zmh5-CtQzC0Z0E7G1HugnNM8O30d9VvBQLibkRHGf0rDklI5Zzp1164O-wrMdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نانو بنانا 2.1 توی Google Flow در دسترسه(رایگان)
با این پروژه می‌تونید کانفیگ مناسب وارد شدن به Flow رو پیدا کنید:
https://github.com/MatinSenPai/Gemini-Config-Checker/</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/5527" target="_blank">📅 13:33 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5526">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">Matin SenPai
pinned «
جمع بندی راه‌های کنونی اتصال به کلودفلر بر روی فایروال همراه اول:  1. CDN/WORKER with ECH  برای اتصال به یک کانفیگ cdn/worker از طریق ECH باید ابتدا از یک آدرس مناسب به طور مثال 188.114.97.6 استفاده کنید، finalMask و cipherSuites را پاک کنید، فینگرپرینت را…
»</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/5526" target="_blank">📅 13:11 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5525">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UwgzwGtKLi4MtR88ofKwwsfJuxJG0s_HAW-OkPnIlq4SAmTLNHtBIfxdyBYOf-d-ye6PjQC0rlWIGOwVS82W9uzE1AMBygwvWkW84Aw9GUFfDUImh_u25SsXMXqrAi9vcMO5GW2ogd1h7Q9w-4YKwjCgH-qBCtUkf_W7mp7UlTpRnzW-lz5sne0RfOWrwrEQDZYbpfTUAYWmoqCm8WH2pjgUruHsRownoxofVGHvQurnO_49YXyHsuN_VVxqTrOs89Qd_aBhxzTWsp74dXwOXZt7cSSrSTK3z7bNviBV_dqiKZsGTxwbSBM-Esy9R38UD2lHMvDNSMY1bDz9ehdmPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیتای کشور به قدری اوپن سورسه که الان سایت زدن کد ملی و اسممون رو با شغلمون میفروشن که مخاطب مارکتینگ بقیه شیم :)))
✍️
davodm</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/MatinSenPaii/5525" target="_blank">📅 11:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5524">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">یه قابلیت خفن به Cursor SDK اضافه شده که بهت اجازه می‌ده هوش مصنوعی رو حین اجرا هدایت کنی. دیگه لازم نیست صبر کنی تا کارش تموم بشه؛ با تابع run.steer() می‌تونی پیامتو به نوبت بعدی اضافه کنی و مسیر رو تغییر بدی.</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/5524" target="_blank">📅 08:51 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5523">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">برای ترجمه و کارهای روزمره‌ام، اکانت آنتی گرویتی کم آوردم
گفتم به یکی از بچه‌ها دوتا اکانت بهم بده
توی پنج دقیقه بهم داد:) اصلا باورم نمیشه
و چقدر ارزون. یک دهم کلاد یک ماهه، 18 ماه داد
هرچند خب استفاده‌ی دیگه‌ای داره کلا.
اگر که اوکی بودش و نپرید و اینها، معرفی میکنم</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/5523" target="_blank">📅 23:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5522">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArasTey</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tfPQou0tPWmoH7K4xqUrdNgDeKrS05JOYXslE8U3prN9HTSOapYco5cY0jI36FQFAgsP1XR0NC-gaJ_TwBXV0jZSKJn-9GX3aPXL2AQ9Hoi8lTMHhXlmr7na-rfZKBL-k6PIgX3i3gIcXEIG3XvXsuZGPiFlxpts7aKOOCPokl44wCUEJBTGFdXX5NHZDRzyGM0j-G1-rMMh7i-1CI7cMZDXB9zJNzoP88q1UsVpFYkslxBJnhQgERXzF8VERFHvmxGi6L8dMUyBc8z6E1Id_XEPVSvkAGMhdudU4vhlqN5Roz44MW7WUaVT-50lpHTHf5C5XJ4Cc4VivIjQwijTmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه آپدیت هم دادم روی
بهینه ساز
که الان میتونید خیلی راحت ECH اضافه کنید به کانفیگا و کارتون راحت شد.
ArasTey.Github.io/cf-optimizor
Github.com/ArasTey/cf-optimizor</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/5522" target="_blank">📅 22:53 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5521">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">جمع بندی راه‌های کنونی اتصال به کلودفلر بر روی فایروال همراه اول:
1. CDN/WORKER with ECH
برای اتصال به یک کانفیگ cdn/worker از طریق ECH باید ابتدا از یک آدرس مناسب به طور مثال
188.114.97.6
استفاده کنید، finalMask و cipherSuites را پاک کنید، فینگرپرینت را روی chrome قرار دهید و در قسمت echConfigList به طور مثال مقدار:
cloudflare-ech.com
+udp://1.1.1.1
را وارد کنید.
2. CDN/WORKER with IPv6
ابتدا echConfigList و cipherSuites را پاک کنید، فینگرپرینت را روی chrome قرار دهید و سپس از یک آدرس IPv6 به طور مثال 2a06:98c1:3121::7 استفاده کنید.
سپس در صورتی که دامنه‌ی شما فیلتر نیست، finalMask را خالی بزارید، در غیر این صورت finalMask را باید tlshello-0-len (همان مقدار متد f&f) قرار دهید.
3. WARP with IPv6
از قسمت add aether ابتدا پروتوکل را روی wireguard/warp-in-warp قرار دهید، نوع آیپی را IPv6 انتخاب کنید، اسکن کنید، بعد از پیدا شدن آیپی اسم انتخاب کنید و سیو کنید.
////////////////////
جمع بندی راه‌های کنونی اتصال به کلودفلر بر روی فایروال ایرانسل:
1. CDN/WORKER with F&F method
ابتدا echConfigList را پاک کنید، از یک آدرس مناسب به طور مثال
188.114.97.6
استفاده کنید، finalMask را tlshello-0-len (همان مقدار متد F&F) قرار دهید و برای فایروال ایرانسل حتما باید cipherSuites را روی semi-python (همان مقدار متد F&F) و فینگرپرینت را روی unsafe قرار دهید، همچنین دقت کنید که مقدار ALPN را درست انتخاب کرده باشید (http/1.1 برای ws و h2,http/1.1 برای XHTTP)
2. WARP
همان مراحل فایروال همراه اول، منتها روی فایروال ایرانسل میتوانید از هر نوع IPی استفاده کنید.
3. MASQUE/H2
از قسمت add aether ابتدا پروتوکل را روی MASQUE-HTTP/2 قرار دهید، فینگرپرینت را روی semi-python و finalMask را روی tlshello-0-len قرار دهید سپس اسکن کنید، و بعد از پیدا شدن آیپی اسم انتخاب کنید و سیو کنید.
////////////////////
دقت کنید در برخی مناطق سیم کارتتون میتونه همراه اول باشه ولی فایروالتون ایرانسل باشه و بالعکس سیم کارتتون میتونه ایرانسل باشه ولی فایروالتون همراه اول باشه.
سایر نت ها هم معمولا از یکی از این دو فایروال استفاده میکنند.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/MatinSenPaii/5521" target="_blank">📅 22:06 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5520">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k13EzF7gg3GxcQvjq76ez_LxUG-CK6OE1G9gk3jDCIiW26OqpKKf0bG_ZK4_Dp9sxzxkJl0DJQ1sL4F6wh-honCWw1Jd6gEZbshoVBv5DDM9OO1APINvp9QtLdWpTtM88MHbrV8-UtxMVE8nQuZWUr-vViDHGihzVA_XUAEhhV9qxl4eeOFTxNbJV_q1ebfdByRdpbBYz0A4mhgSKPNmS-LKyJwWHjnYn3Pu68U8ZL0iRT_gP0wBVEw3FNHIJdVeLPE0_6Wdl4QDboYNA-BegLkxor2_vVggBn_7oI12ys-Ue1k23eDRXn4Inryo1OYsr7-yOWvmp5TDT3F9zYR4BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستاپ مموری Muse رو کپی کردم برای Hermes خودم
یه کاربر توضیح داده چطور ستاپ مموری Muse رو برای Hermes خودش پیاده کرده؛ بحث اصلیش هم انتخاب پرووایدر، مدیریت پنجره کانتکست و مشکل فراموش کردن زمینه‌ی موضوعی بحثه. اگه ایجنتتون وسط کار یادش میره چی به چیه، ایده‌های توی تصویر ممکنه به دردتون بخوره.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/5520" target="_blank">📅 21:08 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5519">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/MatinSenPaii/5519" target="_blank">📅 17:21 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5518">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">استریم ما داریم میاییم</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/MatinSenPaii/5518" target="_blank">📅 17:17 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5517">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rLImvjSbJKhr7QKTmXlTl1Rn6cvtEsxgxnCQELPeZDLeBSbI5rRCyJTXoM4S7nP6EDv_GhKBgS2h8Hxs5hcoVEfdAjAyK577qHhVSTaj59Uz3mB2ul_Um1Q3Ql5UYsdEe6HaY4T3lY3pDr4ULmUPr9rpWOPV6xa1L3h_EPqdkKAHtNhxzqyRtV7oBZYYUbhNomYIoN2ej6IaaNPlrsUGQESqYnHtaV_zKhrCK6m9Pf4HJ8yYkrGJOFpb18tistKJbAC44kmZbtN3snntlc2O9MfapxF9_Ir5CuVoIPjzQcbfJOR0S1m6IgKedifJZsQfKW2xLkbWHlz92O8g_8_Kag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استریم ما داریم میاییم</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/5517" target="_blank">📅 16:34 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5516">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TBgPSJ8Pq6jbCYQw9viCq1DQ_kpcEGWXofKA-dIJintVV16TYU5-oNYaJoUmmetRz4lV5BVwO1USkmGeA9VugBVMj8keMyVKjB7fOyEF3mEZphZbBSBRFBBcY81vySI-elbkVmme9tbJzEpkN0oCvUVIOPBC4xBUgHJbxDAKJLZ9q9AOaDj3KDx6B4vwpJY2pXbwUCjK0VKy-XD23h2exXyPo43WSV1pAGnpruHWYnKCw_Bq72H1ZnxU3okq-itydiXI9Rl4fe5vKT3SnxDnyKHAK0_wowUuVFQ09H2WjddGZxnqZRGQ5RS3VeJiHxr0d075xpsua9M1i9JDpqHzPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا رو شکر اوکی شد
مشکل اینجا بود که سرور ایران، دیتای اتصال‌هایی که از خارج شروع نمی‌شن رو نمی‌پذیرفت. و با همون قضیه ssh هم میشد فهمید
و حتی تانل هم "اتصال" رو نشون میداد که به خاطر هندشیک کوچولویی بود که رد میشد
و الان اتصال از خود ایران به خارج شروع میشه و همه چیز اوکیه فعلا
این روش فقط mux و reconnect نداره اما چون فورواردش توی کرنله، چیزی برای قطع شدن نداره عملا.
همون آیپی تیبل خودمونه</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/5516" target="_blank">📅 16:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5515">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cFvV88NEc2poI5GWQLdzCgKSCzQs-7aAoaK71DRGfj4EqfPxaRrpMvMNZmRkXZBr6_DVllNsMHqRoXB0C2iYCP_6mOT4060--k_v-8SUTc1WoHl2OL-J3801SL1JjGJ-5aH5jvXy5OK1NeJh-Hvu8moAYcqbt96MZMLoWXKe1rp1r3uXRMQW8CxOVVQTtDhiqWkA44j2NmFKLR5rN_W82BG16S7fNGJQiy82o1dVQztFJJUJTkWj43v6aCpSWyvGCzm6IeN_ywdWRO5FJkTGwq3fGd7LWm458uEUJLZfh7FqwhYMHmb5_PwNjF4BaYZMAgJailBt1TZVWRbn6EKAtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلا Claude رو گذاشتم تانل بک‌هال بزنه بین ایران و هتزنرم ببینم چی میشه</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/5515" target="_blank">📅 16:26 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5514">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">سعی میکنم استریم انتخاب رشته رو امروز یا فردا بریم. متاسفانه تا الان هم که نرفتیم به خاطر وضعیت نت بوده</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/5514" target="_blank">📅 14:44 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5513">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">سعی میکنم استریم انتخاب رشته رو امروز یا فردا بریم.
متاسفانه تا الان هم که نرفتیم به خاطر وضعیت نت بوده</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/MatinSenPaii/5513" target="_blank">📅 14:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5512">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">از اخبار بی اطلاع بودم.. نمیدونستم صبح چه اتفاقی افتاده...
🖤
🥀</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/MatinSenPaii/5512" target="_blank">📅 12:39 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5511">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ای کاش OpenAI این تیم مارکتینگ و مدیریت محصولش رو از کف توییتر جمع میکرد
https://x.com/MatinSenPai/status/2107032765916999892</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/MatinSenPaii/5511" target="_blank">📅 12:30 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5510">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIRCF | اینترنت آزاد برای همه</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TmY3ng6K-J5_yv-d1386LDTT-a4053VnbeZ6XNrsLGxJW7KhBbX8LRzJ3nT_eELen5-NwTyN3MwKtkMSsqB4X4ZwGSqEBMccoB8byqdztsBREYAGpDTp8vKbH0SQchCLrrZQhviN37eVWTv9OWAaivlBSDTPuBGEAP_5EF5H8CYqhGTJ0wM9Plg2xX3dkGvT-gZJpMIjrJNia7s2pBLwuZ4EMfAYXlbLXvmnmu2llCda_rEccXKLkdrb-UD3bc0YZ9CoBi1wqT2fnay2FWlMjT2Ap9icCHIPAIkJ1i67ptULstgSLYSBU-1g0Xgn0czIX6-N_n-cTUm2BbUOYACyng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق آمار رادار کلودفلر، از ۲ روز گذشته ترافیک ایران به کلودفلر به شدت کمتر شده. اکثر کانفیگ‌ها و اتصالات به کلودفلر مثل وبسوکت و xHttp مختل شدن، فرگمنت روی همراه اول و مخابرات بسته شده و روی ایرانسل ضعیف کار میکنه؛ همینطور پروتکل UDP به سمت کلودفلر کلاً بلاک شده و اکثر رنج آیپی‌های هتزنر و OVH از بیخ بلاک شدن.
©
mahsanet
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/MatinSenPaii/5510" target="_blank">📅 08:23 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5509">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">اگر سیمکارت همراه اول دارید هرچه سریعتر از پنجره بندازیدش بیرون. اعصابمو به هم ریخت دیگه فیلترینگ روی همراه اول</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/MatinSenPaii/5509" target="_blank">📅 01:29 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5508">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">سه تا ویدئو ضبط کردم واسه AI اما اصلا حتی دلم نمی‌خواد بفرستمش برای ادیتور. خیلی وضعیت نت زده توی ذوقم
الان اینطوریم که خب من آموزش بدم، کی می‌تونه اجرا کنه اصلا</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/MatinSenPaii/5508" target="_blank">📅 00:49 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5507">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">متد یوسف قبادی</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/MatinSenPaii/5507" target="_blank">📅 20:53 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5506">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">Fragment
🪦</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/MatinSenPaii/5506" target="_blank">📅 20:50 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5505">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">حساب رسمی مایکروسافت در ایکس با بیش از ۱۳ میلیون دنبال‌کننده هک شد</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/MatinSenPaii/5505" target="_blank">📅 18:12 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5504">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/etP2SJKwmEDgioMzlV9IxGmcmzyvpFwwq8BHJJFWlw4HJzK6dgiHK68A0Xs2PH8ahJez_IekTVwL3kUnrCYnSXLMNbuA_sscM6ibK_-3O8ZNBvsup6aBV4xQN1fZFvxyZk1xqVvs8Q-a0FvzWcKqnGwHOWTR9AQgKXT5cvOQlheK4BMa6egbIvA6JbpHawts9WpOlYt2xwQXowPYBE8DLAZ6wNJwb-Xse-8Yt7KdINzA3M3NM4-PWFFlfvTyJfgVTCpLYmnsLLUR4HEtGKe7KeiSCqsY5SYWlfwLrEhXq_qKghMpwKnJFyFvokpIK4NBusvLg1qrxoxxu7p2Da16sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل Ling 3.1 Flash روی Cline تا ده روزِ آینده رایگانه</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/MatinSenPaii/5504" target="_blank">📅 16:59 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5503">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">استارلینک توی ایتالیا با کمک اپراتور fastweb سرویس direct to cell رو تست کرده. توی سرویس direct to cell شما میتونید با یه گوشی معمولی نسل ۴ به استارلینک وصل بشید. مثل یه اپراتور معمولی موبایل. توی حالت عادی وقتی آنتن موبایل وجود داره، گوشی به همون شبکه زمینی…</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/MatinSenPaii/5503" target="_blank">📅 16:26 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5502">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">استارلینک توی ایتالیا با کمک اپراتور fastweb سرویس direct to cell رو تست کرده.
توی سرویس direct to cell شما میتونید با یه گوشی معمولی نسل ۴ به استارلینک وصل بشید. مثل یه اپراتور معمولی موبایل.
توی حالت عادی وقتی آنتن موبایل وجود داره، گوشی به همون شبکه زمینی وصل میشه ولی وقتی میرید جایی که پوشش شبکه وجود نداره، گوشی وصل میشه به استارلینک. یعنی همون اپراتور قبلی ولی با آنتهای فضایی. واسه همین اپراتور تلفن باید فضای فرکانسی خودش رو در اختیار استارلینک بذاره.
حالا در مورد ایران قطعا هیچ اپراتور ایرانی‌ای این کار رو نمیکنه ولی لزومی هم نداره حتما اپراتور ایرانی باشه، مثلا یه اپراتور امریکایی میتونه این کار رو به عهده بگیره. اون وقت شما وقتی دارید شبکه‌های موجود رو جستجو میکنید، اسم اون اپراتور رو میبینید در کنار ایرانسل و همراه اول و غیره.
یعنی از دید موبایل شما انگار یه اپراتور جدید داخل ایران فعال شده.
ولی مساله اصلی اینه که توان ارسال از موبایل به ماهواره خیلی محدود و ضعیفه و حکومت میتونه با ارسال پارازیت کاری کنه که ماهواره‌ها نتونن سیگنال کافی دریافت کنن. حتی توی مسیر ارسال از ماهواره به موبایل هم میشه پارازیت انداخت.
تفاوت این تکنولوژی با استارلینک اینه که توی استارلینک امواج رادیویی به صورت مستقیم ارسال و دریافت میشه واسه همین شناسایی و پارازیت انداختن روش سخته ولی امواج شبکه موبایل توی همه جهات پخش میشن و میشه راحت روش پارازیت انداخت.
من مخابرات بلد نیستم ولی اگه کسی تخصصش رو داره بهتر میتونه نظر بده که آیا روش عملی وجود داره که بشه سیگنال به نویز دریافتی و ارسالی رو بهتر کرد یا نه.
ولی میشه گفت توی مناطقی خالی از جمعیت که پوشش شبکه وجود نداره و در نتیجه پارازیت هم نیست، این روش جواب میده چون پارازیت پخش کردن توی همه نقاط ایران اقتصادی نیست.
✍️
aleskxyz</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/MatinSenPaii/5502" target="_blank">📅 15:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5501">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">امروز روز آپدیت بود
دیگه تموم شد فعلا خدا رو شکر
🥸</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/5501" target="_blank">📅 13:50 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5500">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iqVbUsA4TNkSB8nyiWj0_uYnZz6u2CkXoKop6WUAPGUSVflI6gekCOVNoFVROKsjIvb3BBw-6afS9m3ke6NHN71Pu8r6Wx5ZrWyzAmQTtaGJIfRVjUt7wHixzjupR24jbCt4Ib-DY_gprdmOMnlC82Dds4M8ld1hnMC6VSJfDffgiTHR1M5YWdSRGKo8OBp_x_r1oOFFwgukN4Jh796GC8J7WRgwE2MmWfvCx9TaDj0PBe5TLt7NZhEN0sbKJ03ieVZuEkJtTMZxkpIqzfZWCMcxHGfvto6DyPbQsl71CVW3L4xKPq9bM--HRvAJV-clOQfYwy2pACr3QPZnA46DEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه 0.8.0 از Aether-GUI منتشر شد
👋
- آپدیت هسته‌ی Aether به آخرین نسخه
- اضافه شدن شبکه‌های Psiphon و Tor
- اضافه شدن MASQUE-in-MASQUE
- افزوده شدن HTTP proxy، upstream proxy و exit-country
🐱
دانلود از گیتهاب:
https://github.com/MatinSenPai/Aether-GUI/releases/tag/v0.8.0</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/MatinSenPaii/5500" target="_blank">📅 13:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5499">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hBsmbfpj7lGnTdjwynkPn_KM5Q0AZxyBtO3-jxhEjEuHbx-M3YB1j7ZsrRVfBPB5yVMuHOHJiW-qgDhLzh_LTzMEN5ynsVUuJXakfAMPrBhFQVrA8L4sX9CnKAsicGTp-N6L9l6n6lg2BZ51giJCpviAfBBWbcIt9ZJguFS1OiURJ1_klSZXY3SgmYXaaFDAA0EjOsnnbcXaVGF2VQUyW3BqiLW8RhxUL64E7LCtM5XrEWzctfoI5FdsYsMlD_59qEsTcteeQ5KYxYaVjxor_eXN4imc-tMUnZJG6GoYtPHj1dcSarZpKIPCfXUbdemfMMLuYbyz0PvPveyvNzHCWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ری استریم رو هم اوکی کردم، به زودی میریم لایو، روی یوتوب
🤠</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/5499" target="_blank">📅 13:25 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5498">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mMrJtly6hGXul4aC85Gvw9dV5UmqPn6I__-jaCbfozWGOgGH-NXtGeF3FGIjrodGLLTDpdyJaBi_iQmnYZInmEv_4Tp1ph0eKZtq-Pl8OeBKgSvS1XKWR4ne-jgRSmZY1YBwIrsdRoNgfZyQ91jejE5QnO0ksw-TDnYlQVFiSq0wHuEoZ62RiHRKtEGfZ7m27ikJxVqZ8V7AkSuL6V-3TxeovjIHUwxL-GlZ4cgFYWPi5Q7XW16r1uqBd3JFnhvrgQhaqI2-SgHnYYShtaZLY_73Tkf-5FFBb4lazM2T7FjtCoeezAEpVWSL4XrnwjWH28sTIfkYADr6HP2g7sKhww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه SenPai Scanner v1.1.1 منتشر شد
"برای اندروید، ورژن قبلی رو حذف و نسخه جدید رو نصب کنید"
• حالت متنی برای صفحه‌خوان (NVDA / JAWS) و افراد نابینا(ببخشید از اون سه عزیز نابینا که درخواست داده بودن و انقدر طول کشید. این آپدیت رو به خاطر شما خیلی زودتر دادم
❤️
)
• قابلیت Anti-DPI: ClientHello تکه‌تکه می‌شه، همون کاری که توی PattNG انجام میشه. مقادیرش هم قابل ویرایشه
• حالت Gentle برای اینترنت‌هایی که وسط اسکن قطع می‌شن
• Paste کردن IP / رنج / دامنه و شروع مستقیم از فاز ۲
• ذخیره و ادامه‌ی اسکن بعد از قطعی
• اندروید حالا همه‌ی قابلیت‌های دسکتاپ رو داره(برخلاف نسخه 1.1.0 که دیشب فراموش کرده بودم. این الان 1.1.1 هست
😂
)
• نسخه‌ی ۳۲ بیتی برای Termux
🛠
رفع باگ
• تست سرعت مستقیم همیشه fail می‌شد و الان نمیشه
• و Stop بعضی وقتا روی اندروید کار نمی‌کرد
📥
دانلود:
https://github.com/MatinSenPai/SenPaiScanner/releases/tag/v1.1.1
این نسخه‌ها تماما روی گیتهاب بیلد گرفته شدن(مشکل اکانتم به لطف یکی از دوستان برطرف شد) و دیگه شبهه‌ای توی امنیتش نداره
👋
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/5498" target="_blank">📅 12:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5497">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EYu-ZQWSuwyZl0wp1BvMe5wXAB0TXHCcIo3tqoH3VDgbWRNuOJ7HdrvdNSZLvy_mON5LU8ijT7XbdQNzo5x7t4JxtMV8BWEc7FoXpPU32B5bQoQIDfomkfo9GwfpC92D6fj-t8YdQzVLgHpCz-C5DxYQv_4OQnkfWhZCjKjeRm-LpukQnCkLbsL0Lq0ByxRYWs_iL7TuAJaIDdOuz2qS6Hb_8PNvEh62Gu5j7AZo4iWuAWgDdzQN-HgNitSyfCTP9eclgsE3JSwXZz-XrvspCVEBE_oo4b9WcSrC3ib0YIvMx11fGo-qq-mNViuOMcKXFM0C52Tkv_Jx_ZopIaw65w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایجنت گفت تمومه، دیتابیس قبول نداشت!
مایکروسافت با همکاری هاگینگ‌فیس بنچمارک ThinkingBox رو منتشر کرده که ایجنت‌های هوش مصنوعی رو نه از روی حرف‌هاشون، بلکه از روی ردپایی که تو دیتابیس و state نهایی می‌ذارن نمره می‌ده. مثالش بامزه‌ست: ایجنت ۹ تا تول‌کال تمیز می‌زنه ولی تیکت مشتری رو بدون حل واقعی می‌بنده. این بنچمارک ۵۰۷ ورک‌فلو واقعی کسب‌وکاری رو هر کدوم ۲۰ بار با مدل‌های مختلف اجرا می‌کنه تا معلوم بشه کدوم ایجنت واقعاً قابل اعتماده.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/5497" target="_blank">📅 11:46 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5496">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">اسکنر زنجیره‌ای کانفیگ برای Google AI Studio، Gemini و Antigravity https://github.com/MatinSenPai/Gemini-Config-Checker  " دقت کنید قبل از استفاده از این ابزار، طبق این آموزش حتما باید ریجن اکانتتون رو تغییر بدید: https://t.me/MatinSenPaii/2881 "  کانفیگ‌های…</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/5496" target="_blank">📅 23:35 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5495">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eFNo59qW3ngbDdV3nPlejgKBoaTr-3RC4I5zF0mPJxucrFNvOsA4e-UdXv9X4Ej3-NvIjQ44d5CPkjonXvLc3t07Gqvevi68gPcMm1Wd-6_i7kcQjXi5fgYzixPt0CCe561Tl6k4RPB0Z2JGNI0kqV7UXttjXIDFZWzHYa8sBK8VvK2ZoJMkR9jXQ93zFzoZN7v9UU2EfoLcMO9Fgd0KBAPrku_l9mh-trYngHaGFKT5wlciC6xM2qRLMpdCx4qQ1Y2z_01FjTr50qbCNu4EATMFbE-i2EryWUmFRaUgicdArAJYyEO3c4oI8RpPx23o-B-flOrMaIgwqxW1O_QK3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکنر زنجیره‌ای کانفیگ برای Google AI Studio، Gemini و Antigravity
https://github.com/MatinSenPai/Gemini-Config-Checker
" دقت کنید قبل از استفاده از این ابزار، طبق این آموزش حتما باید ریجن اکانتتون رو تغییر بدید:
https://t.me/MatinSenPaii/2881
"
کانفیگ‌های رایگان زیاد هست، ولی کدومشون واقعا Gemini و AI Studio رو برای جیمیل خودت باز می‌کنه؟
این ابزار هر کانفیگ رو همون‌طوری تست می‌کنه که یه آدم استفاده می‌کنه: با حساب Google واقعی خودت، توی مرورگر خودت، از مسیری که واقعاً ازش وصل می‌شی. چون Google ریجن رو فقط برای حساب واردشده و بعد از لود شدن صفحه تعیین می‌کنه، تست‌های ساده‌ی «پینگ و API» همیشه همه‌چیز رو سالم نشون می‌دن و دروغ می‌گن.
🔹
دو حالت ساده و پیشرفته برای انواع شرایط
• ساده: کانفیگ‌های خودت یا لیست کانفیگ‌های رایگان (لینک، ساب، base64) مستقیم و بدون زنجیره تست می‌شن
• پیشرفته: کانفیگ‌های رایگان از پشت کانفیگ پایه‌ی خودت تست می‌شن (تو ← کانفیگ پایه ← کانفیگ رایگان ← Google)
🔹
تست واقعی ریجن
• ورود با حساب Google کاملاً لوکال، با Chrome / Edge / Brave خودت؛ نشست فقط داخل حافظه‌ی برنامه می‌مونه، چیزی جایی ارسال نمی‌شه
• AI Studio و Gemini جدا بررسی می‌شن و می‌تونی انتخاب کنی «سالم» یعنی کدوم‌ها
• اول اتصال سنجیده می‌شه تا کانفیگ‌های مرده زود حذف بشن، بعد فقط بقیه به مرورگر می‌رسن
🔹
پروفایل ضد فیلتر
• Finalmask (fragment)، Fingerprint، ALPN، Cipher suites و IP تمیز
• مقدارها رو از خود کانفیگ یا لینک می‌خونه؛ کپی‌پیست کن و تمام
🔹
خروجی
• «کپی با Chain»: کانفیگ کامل و مستقل، آماده‌ی PattN / v2rayN و Xray استاندارد
• خروجی لینک، JSON، و ذخیره در فایل
• انتخاب کانفیگ‌ها، مرتب‌سازی بر اساس تأخیر، و چک‌کردن دوباره
🔹
همه‌جا اجرا می‌شه
• ویندوز، مک، لینوکس: اپ دسکتاپ و نسخه‌ی وب (برای سرور)
• اندروید (APK): فقط تست اتصال؛ اندروید اجازه نمی‌ده برنامه مرورگر رو کنترل کنه، پس بررسی ریجن واقعی رو روی کامپیوتر انجام بده
• رابط فارسی با تم تیره و روشن
• متن‌باز، با موتور Xray-core داخل خود برنامه
این پروژه، به لطف این پروژه‌ها و آدم‌ها ساخته شد (حتما اگر دوست داشتید استار بدید):
• patterniha: PattN / PattNG و مقدارهای ضد فیلتر (Finalmask)
• 0xRadikal/Free-v2ray-Configs: لیست‌های کانفیگ رایگان
• bia-pain-bache/BPB-Worker-Panel
📥
دانلود و راهنمای کامل (فارسی و انگلیسی):
https://github.com/MatinSenPai/Gemini-Config-Checker
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/MatinSenPaii/5495" target="_blank">📅 22:55 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5494">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">یه اندروید کوچولو هم براش زدم سعی می‌کنم تا شب منتشر بشه</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/MatinSenPaii/5494" target="_blank">📅 22:33 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5493">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLinuxor ?</strong></div>
<div class="tg-text">وقتی یه مدل رایگان لوکال پیدا کردی و پروژه رو باهاش می‌بری جلو...
@Linuxor</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/5493" target="_blank">📅 22:15 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5492">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l-ot1VFS0TTSTvadGTW3vkw0NdAG3TBeqX2k9epEaTjCSi_B-r5UecLnOmtdee4EY1p6fUYreVnmgc23D-eZqzmLto02auITiRBJ0eJPRVYs5O45hDJpAeF4a4bJrfmLGLlXFK9csGL0e6mu8vdXVtsiTAPM6_0DUCi-b31Jv_Zrd05cv0TKEJGDkYwxkDp8qAAUVWEQV8RNN67tUB82_yhEaznx2NVgGiF4ajQvIFCboYrN7d1JUzLH8-bXVF_UVvg-PSbaabxq_RjlY7n3yGMhGu7aYFx5gVZDY1ZokP4C_HWFdOTi0tGYIC7V_lkrqaTT5FtmAHJY2CW2fOAvkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه دسکتاپ Cline برای لینوکس، منتشر شد
روی Cline می‌تونید از مدلهایی نظیر
Muse spark 1.3
Deepseek 4.1 flash
Mimo 2.6 flash
به رایگان برای کدنویسی استفاده کنید
https://cline.bot/desktop
ویندوز، مک و لینوکس
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/5492" target="_blank">📅 19:51 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5491">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d6249e0466.mp4?token=eqnei67wKLzvDHBjzKRKYkzgKTjtIK6PNZEPgMe2OLCrjAKK2SGmHYuFvTCYKNVTvIg3Cu4fbEmqR2ayqS6GOXcGhbh7bf8CSz_btIA-fbYymRgiT5fLabxUh9qFTEnglcA8AyDY288rN1960UYgLoHf0ibSSpRl3ixR-4GkGf6ShhNv_spWVlZlFiQ0ba8tlKbHvPjh_Zqy7aIzeNkMhDzw3qRblJdtQWfaedxzbXDkccDY8_4LiBSs1AidbQkXMC9clzp2QiWZhfHes5mz2Lke8JauPrMjDSPTQ_7F7EdYSX284tA5YLUNMFcszMvGA105YjePTXv6QntUwngrdg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d6249e0466.mp4?token=eqnei67wKLzvDHBjzKRKYkzgKTjtIK6PNZEPgMe2OLCrjAKK2SGmHYuFvTCYKNVTvIg3Cu4fbEmqR2ayqS6GOXcGhbh7bf8CSz_btIA-fbYymRgiT5fLabxUh9qFTEnglcA8AyDY288rN1960UYgLoHf0ibSSpRl3ixR-4GkGf6ShhNv_spWVlZlFiQ0ba8tlKbHvPjh_Zqy7aIzeNkMhDzw3qRblJdtQWfaedxzbXDkccDY8_4LiBSs1AidbQkXMC9clzp2QiWZhfHes5mz2Lke8JauPrMjDSPTQ_7F7EdYSX284tA5YLUNMFcszMvGA105YjePTXv6QntUwngrdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه اندروید کوچولو هم براش زدم
سعی می‌کنم تا شب منتشر بشه</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/5491" target="_blank">📅 19:11 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5490">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIRCF | اینترنت آزاد برای همه</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J_wBWlQMB1Sp3XUAmRrJ0YuHXt6vB8B-DyXGM0nen5DcZxxaylLUvXuJWZidUzqCEcMd2v8-G_h2bdv9mh-fJhASdYp2u_2l1c-gxb2VfJgUNfAsRQbTgqc8Gc4vNzJzNPU40qkJTEan4dY47cmFYrhGlb0HvNLhVCfjsZHcu6bZL0cP2P8A8UN-Ho0J1CTGvWp8NzkFVklLFi_haSE3bPk-frX9_yahGRacWKLldKLBwnVeNVcGpETFfu_TXww0w9QqnSsAXv823msTVu79jBBOrnQD3wiDbYBVSGscB-vyXsHPZCoCvfKPgBC2KTMkgaWCyFMizraB9_ORjemiaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر میخواد تبدیل به یک مرجع عمومی صدور گواهی دیجیتال (CA) بشه و در قدم بعد، گواهی‌های جدیدی به اسم Merkle Tree Certificates رو هم در مقیاس بالا صادر کنه.
هدف اصلی این کار آماده‌کردن زیرساخت وب برای دوران کامپیوترهای کوانتومیه؛ چون الگوریتم‌های فعلی مثل RSA و ECC در برابر کامپیوترهای کوانتومی قدرتمند آسیب‌پذیر میشن. MTCها کمک می‌کنن گواهی‌های پساکوانتومی بدون اینکه حجم و فشار رمزنگاری روی اینترنت به شکل شدیدی زیاد بشه، قابل استفاده باشن. کلودفلر گفته هدفش اینه که این گواهی‌ها رو از اوایل ۲۰۲۷ وارد محیط عملیاتی کنه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/MatinSenPaii/5490" target="_blank">📅 18:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5488">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GjJVwIfyHJetsWRUMs6cHVuMe7_str5FQSkT0gdtzskbcfWf01sJfhjhFt0OjEZsnsdAxWKAXf50COuG4hyuQ2qxVR43TXqcrl3IB6EOW689W6SLtNNOtd4_YdIQXf64s2plgf8ofr7UBsPGQKW0D1aFRYsoRcquQE808_XNgfLCm4GyXDukeXPXQZA7a_MngkZvCNbiugkECSY7Gg7Y-b_8fqFYYRiENOUB0i6TK1yLN5UAq6AeCctOLBx4rMwt1FovrvaCxmgJfMOnB7r6AbhRhaJcn_evWOeIGQBqBmMTirPsUWWrCEwa9QeKK9Q2qvlG5PNoOXo3T1f74p9vvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CWMShhtGrJrOqnDja_735jSdQl0QBEOrr_cSNvKofNCL5KysaA-mtyHIppgC_fgdRQ8QvL_Fbvy-RmLy2ku6n9b_c2e8hpQZwbkIv3fPOkArOk--YlPy7p02dfRoobnSso1NV7sIrTTdgzWwUTUMZZZiN2iMvkgiQe89kt2eFFDUO5PVWJLAYuy__chZy6Kl-H0nrsazfLQfSygQwlUoY-KakTpNcdw0awdVH8iXKPFFM9dItBGrMh9GG6lBJ0L5-ybpL-fxDyaqTddEwO81DHK_EGMlJCOE5h7jSrdZY7EHPB-lg4bkOXNMeK5OdETnvyQ5L8vS8Wedykz2duD-XA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دنبال راه رایگان، عمومی و بدون دردسر برای دور زدن تحریم Gemini و AiStudio بدون نیاز به Veepn و این ابزارهای ناامن هستم. تونستم دورش بزنم، صرفا در تلاشم یه ابزار بنویسم که عمومی بتونید استفاده کنید بدون نیاز به VPS و..</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/MatinSenPaii/5488" target="_blank">📅 16:18 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5487">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTaleo Comics | مانگا، مانهوا، ناول و کامیک</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nas-U90HzQA2HHxt-c7MMmluOORE4dLA2_lLiV4X6QGbzOoDLRQ6XxTaiy6yaOb6IMfUtichhVGrLQSQ4GoEihexpE7qGgI8S_HOjyCHYRiHZzIUKy0WKyRmGnygAHe-XTujEJ87O0ZQNbPyRX8PQzRvBYoshRhK9E8fxi9WXzCzq4Nd-ieMfMirb4YroP1WWeTl2SmIH_lQNe4Ta5qMsFLhYmW9p7vQPUBSrPum7yg6dr7sjq8dPf2_3QuDhxvqX6xGCgwHwlRncnPPKh_B9WjXvCc5KpAlLhtIz6gP7dJJB8kfP1iMqHWbXhRPj2gJpm7X20M2xBWUo-2DRmXcjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔤
🔤
🔤
🔤
🔤
استخدام ادیتور مانگا و مانهوا در تیم تِیلو
😳
شرایط:
1- تسلط به Photoshop(برای ادیت با کامپیوتر) و یا ابزارهای مربوطه در گوشی موبایل
2- حداقل 3 ساعت تایم خالی در روز
3- مسئولیت‌پذیری
4- کار کلین(پاکسازی متن) و تایپ‌ست(جایگذاری متن)
به همراه یکدیگر
انجام می‌شود.
5-
استفاده از هر مدل AI برای بخش Clean، هیچ مانعی ندارد.
وقت شما برای ما ارزشمند است.
حداقل حقوق
به ازای هر چپتر مانگا/کامیک: 60 هزار تومان
حداقل حقوق
به ازای هر چپتر مانهوا/مانها: 40 هزار تومان
نکته‌ی مهم:  پس از استخدام، یک ToolKit کامل افزونه‌ی تایپ اختصاصی برنامه‌نویسی شده‌ی فتوشاپ + اپلیکیشن کلین با هوش مصنوعی در اختیار ادیتور قرار می‌گیرد تا کار، ساده‌تر شود
برای انجام تست اینجا کلیک کنید
🥺
t.me/TaleoCo</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/5487" target="_blank">📅 14:38 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5486">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">دنبال راه رایگان، عمومی و بدون دردسر برای دور زدن تحریم Gemini و AiStudio بدون نیاز به Veepn و این ابزارهای ناامن هستم. تونستم دورش بزنم، صرفا در تلاشم یه ابزار بنویسم که عمومی بتونید استفاده کنید بدون نیاز به VPS و..</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/MatinSenPaii/5486" target="_blank">📅 14:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5485">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gSe59v8lrWV7jZs9_9S--86xlwHezlolcvKQNBqoPOA9KNmAsXHzD9dmgT-Y4IjcMsxgyAFJxlT6bj28yDasXT8GyGOYq1OQISB1sdubIGH4nHFp_E7JWZPW0epnra9pRmQ9leaoip-NJBLaPBSBLmla5x98YDROkCb9pCfQ3rKrXnkHewBA8KXaFFavX5YbTnLNZUfpQETuxa9ulx8cofuYXKmMaCvuqvzR5nIO45mR2mxgIh8gksrZ98yxec5Tbt_l_g1DY32y5S8ehTQG3zcOdxSeL6EjSnCt60umzOpT8anRWtw7j_sQR2tiMm_EoUcXfeYxb4fOrCi93LGbDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایان دوران بارکدهای سنتی و آغاز سلطه کدهای دوبعدی
بارکدهای تک‌بعدی خطی که ۵۰ سال پیش اولین بار روی آدامس ریگلی تست شدند، کم‌کم از بسته‌بندی‌ها حذف می‌شوند. طبق ابتکار Sunrise 2027 سازمان استانداردهای جهانی GS1، بارکدهای سنتی جایشان را به کدهای دوبعدی مانند QR Code می‌دهند که می‌توانند ۲۰۰ برابر دیتای بیشتری برای رهگیری زنجیره تامین، هشدارهای فراخوان سلامت و تاریخ انقضا در خود نگه دارند.
من هم قبلا یه ویدئوی کامل راجب داستان بارکد و اینکه چطور اختراع شد و سیستمش چطوری کار میکنه، ساختم توی یوتوب:
https://youtu.be/PAHA55mHLWs
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/5485" target="_blank">📅 13:12 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5483">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ALsI-OygATXAAyxorguqeubRyIBnuDgDEtigpJ-Bl83PFKZ2QrmRYiIJXRu-mlexkVCV9hUi3MstLGg0bSOqBIL82m3UhwcAVAy-UtnvUxc-GYKc66AHhTo1MTLB6HJaAS8pmRuDNbpFC5C9IwkUg4KHaAGdCt7ZNS7DzzmXLF3x94lJx1a-B7eCsGx9ha0gTsE0jdMjZz0eKTnIrqdgMdxSoAIcq_CTuBvcR9fueGvKGNL8A4IE_mPqIrrSyHdsm3SFmdmt5YMlhhOtSFhAGYndnqoHzGAkFOcPwmqU-jC_Bf_ediuMUNX9ISNlhXZ_Ia36lYoDQqys6WWE4pwDqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
عزیزانی که با WhiteAether سخت وصل میشن یا مدام قطع و وصل دارید، این روش رو حتماً تست کنید.
به‌دلیل اختلالات شبکه، ممکنه Endpoint انتخاب‌شده مرتب قطع بشه و Fallback به‌صورت خودکار Endpoint دیگه‌ای رو انتخاب کنه؛ همین سوییچ‌ها می‌تونه باعث کندی و ناپایداری اتصال بشه.
🛠
برای رفع این موضوع :
1️⃣
وارد بخش Routes بشید و از پایین صفحه وارد Endpoint بشید.
2️⃣
اسکن Endpoint رو انجام بدید.
3️⃣
بهترین Endpoint از نظر Ping رو انتخاب کنید و روی اون بزنید تا Pin بشه.
4️⃣
گزینه Fallback رو خاموش کنید.
🚀
حالا دوباره Connect کنید و نتیجه رو تست کنید.
چند نفر با همین تغییر مشکلشون برطرف شده؛ ممکنه برای شما هم در شرایط فعلی شبکه بهتر جواب بده.
@whitedns</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/MatinSenPaii/5483" target="_blank">📅 10:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5482">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CmrkAYAPL45a6-xJfj_wV53mL1mNjDICxHkS6A43J7zI9sEcEju2oO8_IPAYpz0yNamCon60n7Y0xhCRNCbggCAnIihE7oQJgqSRiFPUvJLa6Kq6gfphod12v0uXoLXuvAMWMIniTMHWegTAr6X8yS-Ye6xNP-Q4D6MAZ3rYMG5PvvBKT3Bjmgq9BxsFATrdwLVEQ8YetNvL76gi2DQCWTGiof1wmb2ua3-cYULkRUINdJ_Lmgd-AMc6zKDlrMb_yqwVHiTnVyOthP93KWKhPt-aOcUhTHmr8VGonP0EcskRC7cCs5EPoYmozL7g26M8YMdh2-fZUVnL3c1kwOL2RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل رسماً سراغ سوئیفت سمت سرور رفت
گوگل کلاینت‌لایبرری‌های Google Cloud API برای سوئیفت را منتشر کرد؛ مخصوص سوئیفت ۶.۲ به بالا با SwiftNIO، مولتی‌پلکس HTTP/2، انتقال gRPC و ایمنی race در کامپایل‌تایم. گوگل می‌گوید با کانکارنسی سخت‌گیرانه سوئیفت ۶، این زبان با ایمنی شبه‌راست و پرفورمنس قابل‌پیش‌بینی ARC برای میکروسرویس با Hummingbird و Vapor و زیرساخت ابری ایده‌آل شده.
مبارک سوئیفتیا
🎨
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/5482" target="_blank">📅 09:55 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5481">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SKZ_msM0nYHgyQMehyf8itfJT3B1BvtShln35m0aMHiiRyxK7xfPpznmICjGkGSSEJSFvWs15txk39DOaRg_qQZEOaLuyBqOVwSR2nOZ7JDRqQFNJEBSCoPly8Ku8rsBW690cTmOsCRjIK5aZ3TM43BFSV6z69dIERTzFPS4HzrIzO_eEnTVGFalYzLUb-R18kKQGtmmP40nzjvYQacOfV0lCDpSAjMFKTVNfYYzBeOk6JXO7_VFOeYY-NrovLezO8V5bpLYH9hFCXXs4AiDY6Nvvfv73b1H3j7e3ZR-7Tm0e_0nxpTgYr_bxuh1vWTcbIz_djvPwsNTCmN1GuoZpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجرای آفلاین LLMها، روی سیستم شخصی! | مدلهای هوش مصنوعی Local با OLLAMA  من این کار رو توی دوران قطعی نت کرده بودم و بدون هزینه، هوش مصنوعی داشتم روی سیستمم و همونطور که توی ویدئو توضیح دادم، ازش استفاده کردم. الان، تکنولوژی‌های جدیدتری اومده و توی ویدئو یاد…</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/5481" target="_blank">📅 18:52 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5479">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/b1tztgmIWJJ2Tp8CBbhCWiT958W0U1FevBO5bXKup3ofyhHUFEq79yEZI8ORbh6crDpS_QTjfCZfgjji8vWH4y5H6mU64nKdCqIXt3nQJLCEas8U-Hn76ybTrSjFE2BwVtHVw5WgkhqLlhBXAetkojoS_ihOvZPfeWxBLCvsOOmPYdY1VgJlihxErpJTfa0OIhSNhmlgtkEFaO_ohNWCRmvZnRB75MRBbmEqnKdzDp-LAGuWxJ8AcBRsOSq_BytxpW-1mKuSmHrXjv6j8L2nc-NoOasStSx28z1h0n_iG_3CWUoh4DA0MJuFNfCzgmBSdNHqITDYXnK0dNtQfNz91A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qgwbg8Fuckvj8W1Jf0_3pzkAAjfeF7fG9ZxUtbRqW9z0l92eUVqChkoXvDKGYr-Xgw-L6tnOhlsjcHxCZU6AoVI02HDAJunyOpTSco4ll8PO5ixRTKSWNU0sqM5fimipeiTWgaFikffG8Q90YywgAm4fUJL_BiP6pzZDAo2ajNRZUZWlMOTWIghjSLyFgIVWdAFor1-q0GnpxRdKJ1lD4VXTxINBnSEhAiYMQIRWdGfxHlXo1uKvhw9uDob3ZIY57NB8qL0cQnh-4FvpZio4T_vB6LnX5W357zlUaeSXABwPcvABuF8sz_EZJFdyPn-qUy5pMRwfvp9o61j9eKqVFA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هر ویدئویی رو رایگان به فارسی دوبله کن! آموزش Gemini 3.5 Live Translate  توی این ویدئو بهتون یاد میدم که چه شکلی، هر ویدئویی رو از هر زبان به یه زبان دیگه، دوبله کنید!
📹
تماشا در یوتوب: https://youtu.be/dPKSMUR5cQE</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/5479" target="_blank">📅 18:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5478">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K9UnrXg3C64AJHpGZNggbBqO2duAOxy-SksBffjaDEBHBj-705PI0-I5h8tJCChWdShRs6K1igV6Pkp-oMjygG6pgUG8J3zRrWoWJIWvHV5CaTqc2mm3Yv65USu4X0NrO_zpdsgJjF3pfQ7QvFc45gI-nuxP9Mezna7i0dVkxKqrPMdPLiYBpK9IIgMgcRkXm68vfxAJ_bYxuNpYYevGaf-rDB7brEKGd_4a_rO8tADF2Q65xCTJfrmjEa_IzobXgSroV7gODTNS2BgHCwEGm4NW5POO9BzJXEACpesv2wIiqZxYL5mmp76n0--nlgx4lzZB9rRZbQgIzWlbRGVxNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجرای آفلاین LLMها، روی سیستم شخصی! | مدلهای هوش مصنوعی Local با OLLAMA
من این کار رو توی دوران قطعی نت کرده بودم و بدون هزینه، هوش مصنوعی داشتم روی سیستمم و همونطور که توی ویدئو توضیح دادم، ازش استفاده کردم. الان، تکنولوژی‌های جدیدتری اومده و توی ویدئو یاد دادم چه شکلی ازشون استفاده کنید و حتی با اینترنت ملی هم بتونید دانلودش کنید.
امیدوارم که مفید باشه واستون
❤️
دانلود Ollama:
https://ollama.com/download
📹
تماشا در یوتوب:
https://youtu.be/EAF-hMPUMYc</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/MatinSenPaii/5478" target="_blank">📅 18:22 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5477">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">آموزش دور زدن فیلترینگ کانفیگ‌های کلودفلر با PattN و PattNG (نسخه آپدیت شده)  1- ابتدا اپلیکیشن PattNG(برای اندروید از اینجا https://github.com/patterniha/PattNG/releases) یا نرم‌افزار PattN(برای ویندوز از اینجا https://github.com/patterniha/PattN/releases)…</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/5477" target="_blank">📅 17:55 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5476">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JY_XAgDAXQ-NHxfK8DxCigtJZa-10RplMqBViJaCcRZ_zXz9uWwESnGLUCJhnLCs5NYbUNnaEwQdMpfXrNoxxmjdhYZef0Wh7NFyZl5ay6Nq4bAZr0V-Q8leIXPfuT3ieqraw77F8HhRswTuYWQnJlxkyrdTeQtRnZnoqwXjgV7DtbJeNQuJqoAIlfI-JA9_u8wRveYBWtSJkOL9mXWQtmI6IVrZlLxOPtgPHAALFGyc-Jc-WWVbs-0v7F4JbG7CgoqbGi7POlGqWQ1UF92xlkAoh245_cYMvzoUJXrM-Q05y93wwBW0XOHm2fitK3bu2qTdKKl5t90zdXwe8ZWLxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به جای توضیح دادن «اون دکمه رو می‌گم»، روش کلیک کن
👀
اگه با Codex یا Claude Code رابط کاربری می‌سازین، احتمالا پیش اومده نصف پرامپتتون صرف توضیح دادن این بشه که دقیقا کدوم قسمت صفحه باید تغییر کنه
😅
ابزار Agentation یه نوار ابزار به پروژه اضافه می‌کنه؛ روی المان موردنظر کلیک می‌کنین و می‌نویسین چه تغییری می‌خواین.
مثلا:
«فاصله این دکمه از عنوان، ۱۶ پیکسل باشه و توی حالت loading عرضش تغییر نکنه.»
⭐️
نکته کاربردیش اینه که بازخورد رو همراه selector و اطلاعات المان به agent می‌رسونه. می‌تونین خروجی Markdown رو کپی کنین یا با تنظیم MCP، کامنت‌ها رو مستقیم در اختیار agent بذارین.
برای Claude Code یه skill راه‌اندازی هم داره:
npx skills add benjitaylor/agentation
بعد داخل Claude Code دستور /agentation رو اجرا می‌کنین.
فعلا به React 18+ و مرورگر دسکتاپ نیاز داره و بهتره فقط توی محیط توسعه فعال باشه. تغییر کد رو agent انجام می‌ده؛ نتیجه رو هم همچنان باید بررسی کنین.
برای رفت‌وبرگشت‌های ریز طراحی، ایده کاربردی‌ایه
🔥
معرفی و دمو
·
راهنمای نصب</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/5476" target="_blank">📅 16:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5475">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCluvexStudio</strong></div>
<div class="tg-text">در کنار بلاک/فیلتر شدن دامین دریافت کلید وارپ، اومدن sni مسک (Masque) فعلا فقط h2 رو بلاک کردن :))</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/5475" target="_blank">📅 13:18 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5474">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">آموزش دور زدن فیلترینگ کانفیگ‌های کلودفلر با PattN و PattNG (نسخه آپدیت شده)  1- ابتدا اپلیکیشن PattNG(برای اندروید از اینجا https://github.com/patterniha/PattNG/releases) یا نرم‌افزار PattN(برای ویندوز از اینجا https://github.com/patterniha/PattN/releases)…</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/5474" target="_blank">📅 10:53 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5473">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">چطور فاصله‌ی بین Hermes و دستیارهای اختصاصی Dots و Grok رو پر کنیم؟
یکی از کاربرا توی یه راهنمای کاربردی از اکوسیستم هرمس توی ردیت، بررسی کرده که چطور می‌شه بدون نیاز به پلتفرم‌های بسته(مثل grok bot و dots و muse و...)، قابلیت‌های پیشرفته Dots و بات‌های گروک رو توی ستاپ Hermes پیاده کرد. راهکارهاش شامل لایه‌ی مسئولیت‌های موندگار (persistent responsibilities)، سیستم دیده‌بان پرواکتیو (Scout) برای وب و دیتا، مدیریت وضعیت تسک‌ها با SQLite، و تعیین سیاست‌های دسترسی قبل از اجرای ابزارهاست.
که البته خیلی از ۱۱-۱۲ تا قابلیتی که گفته همین الانش هم هست، صرفا دسترسی باید راحتتر بشه توی UX خود هرمس و به نظرم کم کم به اون سمت هم میره
👍
پستش رو توی ردیت بخونید، بد نیست:
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/MatinSenPaii/5473" target="_blank">📅 09:08 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5472">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">مهار دزدی و Distillation Attack مدل‌ها توسط OpenAI
شرکت OpenAI اعلام کرد یه کمپین گسترده و سازمان‌یافته برای استخراج و تقطیر (یا همون Distillation خودمون) قابلیت‌های استدلالی مدل‌های پیشرفته خودش رو متوقف کرده. گویا مهاجم‌ها با کوئری‌های پیچیده در صدد کپی‌برداری غیرمجاز از متدولوژی استدلال منطقی مدل‌ها بودن. اوپن‌ای‌آی دفاعیات و سپرهای نظارتی جدیدی رو برای شناسایی و خنثی‌سازی تریک‌های Adversarial Distillation مستقر کرده.
(ببخشید برادران چینی. راههای جدیدی پیدا کنید
😭
)
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/5472" target="_blank">📅 01:06 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5471">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/5471" target="_blank">📅 23:08 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5470">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">آرنا توی این ویدئو، قدرت Gemini-4 Argon رو بیشتر توی زمینه‌ی 3D و قدرت پیاده‌سازی گیم‌ها و محیط‌های مختلف بررسی کرده
که خب کامل نیست و باید توی تسک‌های ایجنتیک و کدنویسی و بکند و... ببینیم
انگار که کلا قدرتش کمی پایینتر از GPT 6 sol هست که خب، ازم بپذیرید که قابل قبول نیست برای گوگل، اونم بعد از اینهمه غیبت کبری
توی دیزاینایی که نشون میده، قدرت Sonnet 5.5 هم می‌بینید
😂
خداست این مدل
https://www.youtube.com/watch?v=h5EL5zThKaI</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/5470" target="_blank">📅 23:04 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5469">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/W9Lr4cy0UblJ9kEJpn1_dSwdxbslXyKCsRwHzLEijFYxkVNVD5q5my3rpxocZXIkDHuQgPyrtsF2F1R50AYQU2Zh3cAy9uh-j5qXRuNt94L5JKR9svtMgcD4fY6l3xM5dpdHoYjGHih1t552lRcnoQj2ZSdLC3Kxe-qJC6eQ8pOvhyV8G2EJlkJj9Vr8w46t7-u_muumGJF54h46hVelJC9mVS3q-OQblXcJm5Tvmpw8WBFqMGkb_jukqJ0oyxkFlKVq7N6oMqxzpFOtA12Nu_q-pHGh4_WRzi1Uzbbqw1oCx6MlLRxdHhQrtcAzDWwcsBX5pczSGgg8cLTr2UD2IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش دور زدن فیلترینگ کانفیگ‌های کلودفلر با PattN و PattNG (نسخه آپدیت شده)
1- ابتدا اپلیکیشن PattNG(برای اندروید از اینجا
https://github.com/patterniha/PattNG/releases
)
یا نرم‌افزار PattN(برای ویندوز از اینجا
https://github.com/patterniha/PattN/releases
)
دانلود کنید.
2- کانفیگ V2ray خودتون که با Worker کلودفلر ساختید(آموزش ساخت کانفیگ رایگانش اینجاست:
https://youtu.be/iAbYpjXyLpY
) رو وارد اپلیکیشن(PattNG یا PattN) کنید
3- توی اپلیکیشن اندروید، روی مداد سمت راست کانفیگ و توی اپلیکیشن ویندوز، دوبار روی کانفیگِ وارد شده کلیک کنید تا پنجره‌ی تغییر تنظیماتش باز بشه
4- توی بخش Finalmask raw json، این مقدار رو وارد کنید:
{"tcp": [{"type": "fragment", "settings": {"packets": "tlshello", "lengths": ["0", "104", "1"], "delays": ["0"], "maxSplit": "0"}},{"type": "fragment", "settings": {"packets": "1-1", "lengths": ["114", "1"], "delays": ["1"], "maxSplit": "11"}}]}
5- توی بخش Fingerprint، مقدار رو روی
Unsafe
تنظیم کنید.
6- مقدار Alpn رو روی http/1.1 تنظیم کنید
7- توی بخش Cipher Suits، این مقدار رو کپی پیست کنید:
TLS_AES_256_GCM_SHA384:TLS_CHACHA20_POLY1305_SHA256:TLS_AES_128_GCM_SHA256:TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA:TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA:TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256:TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256
8- کانفیگ رو ذخیره کنید و پینگ بگیرید. دقت کنید تمام موارد رو انجام بدید. آیپی تمیز
188.114.97.6
عموما کار می‌کنه. اگر کار نکرد، از اسکنر
https://github.com/MatinSenPai/SenPaiScanner/releases
که هم نسخه اندروید داره هم ویندوز و مک و لینوکس، استفاده کنید و آیپی تمیز پیدا کنید.
مقادیر ممکنه عوض بشن، مقادیر جدید رو می‌ذارم خدمتتون.
موفق باشید
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/MatinSenPaii/5469" target="_blank">📅 21:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5468">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GuxkZfE1fNaXI7tb6_bnKbDSmMfXK1yCtb97ocBw14k5QOTuGooRkBB_cHwdrLcB1QcE7keWEk6s6AwZNvCqbw8nqchKwLR9TlrnrSVyXJ_xn0aDoLU090IZUCOZwsXbBttiKUP6QrHbm6ttYiVmUcelu3CdKUkqXO65m3sSR542XeiPxEGi-Era6tYwiskkdKIuR7QDbo_tfLNEJKmMKyXWYbFZXPaLzsEORfnF-e4n1_2N8sfUMlAEvatEKXV0C9Al94ahfPGbE9k4ogMXBrRHqzFQMSfB-N0va6H9ZQhNz917aFiEcmpKrVXLUZwQZheh4--YBnEMCub01Cl_2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیرعامل Airbnb: ایجنت‌های هوش مصنوعی به سیستم‌عامل اختصاصی نیاز دارن
برایان چسکی، مدیرعامل Airbnb، توی گفتگوی جدیدش تأکید کرده که
پارادایم اپلیکیشن‌های فعلی پاسخگوی نیاز ایجنت‌های خودمختار نیست و دنیای هوش مصنوعی نیازمند سیستم‌عاملی مستقل و AI-Native هست تا هماهنگی بین ایجنت‌ها و خدمات به شکلی پایدار صورت بگیره.
خب مشتی یه کاری بکن. ما هم میدونیم
😂
طرح نیاز که خیلی وقته شده
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/5468" target="_blank">📅 20:20 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5467">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">بزرگترین مزیتی که ایجنت‌های شرکتی(Muse, Grokbot و Dots) دارن اینه که با مدل خود کمپانی یکپارچه هستن
برای هرمس، یه کم چون دستمون توی انتخاب مدل بازه ممکنه گاهی اوقات گیج بزنه یا دو نفر با کار یکسان، تجربه‌ی متفاوتی داشته باشن
اما همچنان هرمس رو ترجیحش میدم</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/5467" target="_blank">📅 19:22 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5466">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">قراره با هم یه اپلیکیشن تمرین زبان با روش Shadowing بسازیم.</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/5466" target="_blank">📅 18:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5465">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Prb6aFOaGutrCyXjnBKAx0z3qcOyl-h7j2mCFR9KN7RQnkCUI1KAeoMTFsqkjV_QMghxgBf1ERlUvjqo7t5xCiST1RhrQQ027nkgWOnYSORqZ-rxdYWkCZngaLJQD6zpHy-WZTLqOENq8_aNemJAYNsn2UG6tOOGNSDOGqdLOkUXMveXRX4JPIUoPdpPuKvYjcq-5lbAzjIrvxgkZAvig6kI-XEUWE-433XQhC0sfeA3YMzc8a9h_sTuzcZ5gJkXDi-MlorwnG-uPsd10KXU_urCEIEo9j7Xqx8YkTLfWXlOcZpeZaVPLyLOEXac1dVIPhtF72kmFymNvGKQ11eV0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ردیت فیدهای RSS را متوقف و دسترسی عمومی به API را مسدود می‌کند
ردیت اعلام کرد که به دلیل اسکرپ گسترده داده‌ها توسط بات‌های هوش مصنوعی، پشتیبانی از تمامی فیدهای RSS را از ۱۳ نوامبر به پایان می‌رساند. این شرکت همچنین تاریخ توقف کامل دسترسی به API عمومی را مارس ۲۰۲۷ تعیین کرده است. این تصمیم در شرایطی گرفته می‌شود که فروش داده‌های کاربران به غول‌های هوش مصنوعی به بخش پرسودی از درآمدهای ردیت تبدیل شده و این پلتفرم دسترسی رایگان را کاملا محدود می‌کند.
که خبر بدیه برای ما
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/5465" target="_blank">📅 18:38 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5464">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">امروز زیاد ازش استفاده کردم
گفتم یه توضیحی راجبش بدم</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/5464" target="_blank">📅 18:22 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5463">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">یکی از قابلیت‌های بامزه‌ی یوتوب، Hide user from channel هست
این شکلی که وقتی کسی کامنت دری‌وری می‌ذاره، زمانی که هاید میشه، هنوز می‌تونه کامنت بذاره، اما کامنت‌هاش رو فقط خودش می‌بینه
نه من می‌بینم
نه بقیه
اصلا هم متوجه نمیشه که هاید شده
😂</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/5463" target="_blank">📅 18:21 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5462">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Sk8QKy0URh3ksXuShycLLr9fhkLXZGj4LXxYtGPap1w4EjBlRu9mdrnqoS5Q1F24xuk_zCj_vOwC7H-noV3jApulHNd1Og8bhvJBQL8EPt4DgVPMQxBVSklsm31x5iIkZ6uKEILc61thkCPDWtSxUXtuKAvds1PuwTgqkYeSYC815YCInzGXzcuseh9sZUR1spHTaG20UUECBLZf43_hsnCzbenWTcx_jD3FfyN4gpJ1K601uUOPeq9q75iMif72FQIuNl8WjwVbpSM7O9UNQLVgBbyS72v14DTpI1Qwmn6dhLArXM01msYP5OoBCjpHI9l-UBKjL9Vr78zN2Hjx6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر ویدئویی رو رایگان به فارسی دوبله کن! آموزش Gemini 3.5 Live Translate  توی این ویدئو بهتون یاد میدم که چه شکلی، هر ویدئویی رو از هر زبان به یه زبان دیگه، دوبله کنید!
📹
تماشا در یوتوب: https://youtu.be/dPKSMUR5cQE</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/5462" target="_blank">📅 18:18 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5461">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vyzJ8ZYRc85iVITQ0sVUQeivV3Nj2GKmDBshIqz_XBGDl7aJ_OKjs8YKp8rPc4nTzZNC0icGE05wCdLrMT8ILWQMOGTn8q2bV0X1q0ENkddpLLr6T_WO4WrZa-pdL4QrpHRYsq_oj6MXlhd1A-1SX9vh0__pNBbOG38oN_biT1EIeLADXLNHufs66xnMPrL5ceCXFBxlMKTLTY0YGOQ_YgDCJyVVNCujsS_5POgMXpyvSdhd55SXJneb-bvcLZgwaIJNiPLefsaZO8FUvMnLc2e4uNn2lT2S09Z-GSqzF8D_hih2nmmvtTE_9GblMo2GgG9GRLrOY4vnuTH02ApDZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی Decisions API توسط OpenAI برای اتوماسیون فوق‌سریع تصمیم‌گیری در ایجنت‌ها
سم آلتمن از عرضه قابلیت جدیدی به نام Decisions API خبر داد که ساختاری مشابه مدل سریع Jev از استارتاپ TypeSafe دارد. این رابط برنامه‌نویسی به توسعه‌دهندگان اجازه می‌دهد مجموعه‌ای مشخص از گزینه‌ها را به مدل Luna بدهند تا با سرعت بسیار بالا و هزینه بسیار ناچیز، به صورت احتمالی بهترین تصمیم یا اکشن را انتخاب کند. این رویکرد به ویژه برای کنترل ازدحام ایجنت‌ها و اتوماسیون لحظه‌ای نرم‌افزارها کاربرد دارد.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/5461" target="_blank">📅 17:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5460">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/o52GQpbRgUu2bARtJFec_9eAyyPLaJYko30ohxClIun-Z69YueiEPIWNHp3t0y-eJySBauERZepw4HzEyIS1svoXrhdCcOyYSbvSs2qNJGl7VTeun6pUTDvgughz4TqjXzLF-0X_7MtblLZ84AFplpGlDPNPnwVMy2BdJyNMEc1yYcUXk7AwsKhW0MdPaHB-stva2lMT327RioZWRUrmHJQtM0pl-YrSGH_bqfu-akzwY7Ha4EOQ-ZcTWNF43Z1QRofnMDaL0iziqySuE9Ip5DKFz6pLBhY3b1itpYICbZM191NAmrHiuPNarnu9csbtkL_KgxaXP1XQE4LrILL5yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به قول Theo، چرا واقعا OpenAI هنوز داره از GPT-5.6 Sol استفاده میکنه توی چتش:))
نه تنها 6 sol اومد، بلکه 6.1 sol رو هم دادن و چت هنوز روی 5.6 گیر کرده
اولین باریه همچین چیزی رو میبینم حقیقتا بین کمپانیا</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/5460" target="_blank">📅 14:07 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5459">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U-HW7TwjKpkuggjHATu-Pk5iQUxvMBo0i3bFXhSPs15WZ7KoHokSS_Jz7JjoqzKbhq-I73-CFqJ7tAXWs5lM8qGhktova95im6apNSk2DN4TRt6KUmuQxF0DYiOmNR1BQRrOcFWe8oj_8QKjH8g-_SE9hRLU4iQCJZx8d2LqKlwpOic78Y3V8l7IsbncLt7NpmojQXw_sWwMb1uX5svPEi-JsT5pp7rft9Aan31Q0c-HXQCI6HbigAiXKL83zawqpZyGk3ixW0i8i2pIIjnYZYGSUJpt2V2HjEy2AI_UasJ-4CXZt3J-Qox2yD4RhAK11K-tYNrbqdbHPC_fJ2L35g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بله ما نسل Z هستیم
😂</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/5459" target="_blank">📅 12:41 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5458">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LpKcxNQv8XW5mL2Taz3MId-05mQcId5Ibzjqlc4OFMHCBMjqIYYZkDVNiObLBjv3WG-KvhNWL3Fi17OsA42lGfqCzAUjq0AL8iECTZ556L-NezgKFY6lQfpTuEGpnX7aQLxDu0wfbFK8bG-1QKAwMUSEk1pqWNaec12rxKeMv35tWWP-EZOK4I7iW-cfBV8VNhsrtezbDbRNX0eGR6SRB0wLWUeoGkkz3dwXBKgCqMp18OR3aGhPIWkvAmw0Fti37jLQvRazLsXdVgnvsmhiC1wtdALMUwO89EDyc-T-c0k0x5racnDLhcRhsWY4tpcMuO9Qzu_jKKUHKxDSAjYx3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر ویدئویی رو رایگان به فارسی دوبله کن! آموزش Gemini 3.5 Live Translate
توی این ویدئو بهتون یاد میدم که چه شکلی، هر ویدئویی رو از هر زبان به یه زبان دیگه، دوبله کنید!
📹
تماشا در یوتوب:
https://youtu.be/dPKSMUR5cQE</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/MatinSenPaii/5458" target="_blank">📅 12:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5457">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">شدیدا حس میکنم مدلهای چینی اوایل که اومدن غول بودن، بعد از عرضه یهو ضعیف شدن
مثلا هممون به Ox Alpha دسترسی داشتیم، بعدش که glm 5.3 flash معرفی شد اصلا اون هوش رو نداشت.
یا من به Qwen 3.8 preview دسترسی داشتم و خارق‌العاده بود. سرچ کنید توی چنل نوشتم از تجربیاتم. اما الان Qwen 3.8 max وقتی ریلیز شد هم از مدلهای Frontier خیلی عقبت‌تره هم توی بنچمارک و هم توی عمل</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/5457" target="_blank">📅 11:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5456">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GDDSdTdex-AQA79u_gETQE0AP6I6NO-fPqkKhWZh0QdS-2PQRcbQ4-rahKjOQ5ci4giEsRzO3wBR_jLciAhE_BNH-hoq9-gcHBN8EzU8WqV5ONjd5Yhf0XW6uP0xET4_ORnpg4hSTkyzUsbr9GleWGdAHyoHO-jzpkgo8jwmXAdj2GhqFNAl-b8HsMwPo_jklt7hdT680c48lQcLKOZRyMTeU55l_7z-RwdApiOt_4ysh1wA1J2g8_a9L9hNjF_alkvqALAVxoWxoz-xrJqTIuZNssUxrvrzmUHs_WY5Zgat6njrB1e38QIBNRXIiPh50G6TQwp_vnSL2tObVxo9Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هم به نوبه‌ی خودش عالیه
Hallucination یعنی توهم زدن ai
که این یعنی جمنای 4 به ندرت از خودش یه چیزی رو در میاره</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/5456" target="_blank">📅 08:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5455">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">کلا هر مدلی که میاد
این قضیه‌ی Benchmaxxing پیش میاد
نگران نباشید
میگن توی کدنویسی اونقدر هم خوب نیست انگار و باید منتظر موند و دید تا فردا پس‌فردا که شایعات و تست‌ها به کجا می‌بره ما رو</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/5455" target="_blank">📅 07:43 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5451">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IMG5Kme_MDA5W--eqk_q2teE_j3glr0yxImd00ZVitXuGM2jnz0J_4avNqhjYA1GAhren4Euqnz8SgDzL3xuJtKeGHJwKc7s7q7yDzK3R4FfqL5YyUv1n5WY2u4zXYhYi4ansznnLT9z1YcaOQgYM4u5XtrFv5WSJS15aUsdDzfNS2xJmpTop9_mp1p70JLvQfyyNjxscZVfML4GAiJr_0agJFwgGdCgE_NdQ4hFgBwdwAe4GNOrIFjOspgohAkawaGdJNBEWTAloEa5YEEdhHkqJFm8l4LlauQuUCTQTPALg9nYY9fZhyG7mhDM30nl7s_IIAFyllIV791fIvkPwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HqESsCSQsByZCqGLTIkZLepPUUEclMHnr8dlWjEVFE3BEnYQ1kXW9pQV2suYQs--bHCS7f4ca22-IyZ-HEVYP5-nPNJj-9FLR49cbJpRP8Tdps6d0xFH-fNp8m3JB2pEHztNZEIUijjVPQLPHu_rVhCWXa9-POitCowR5A_6jHfrN8xWDCIQjfgS2cMgjRUcL3KDonN_1_L8cCrIL1pGg5CdRt5pGxkcP1T6ENSliJwatCNqgjlDTd8cVsiwk-ghOXIn9qqk3tz4hvtnmsfhclPXo-c-t2acxwBJp6IvJXYvbVEUj-qAvUC4bjUCxEPDAWWDakQxspNgcJAH_LCDuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YdDwoS2MZ6uiHY59MQ3hYQz1Nbh8sV7XgTZVA7Q9o8VyMGXEUKYhgJOg5EgNrz6aanQu19gsgDmwA1U9rGGEpAexsks-llgYdSsdV6q2q6CXPLhr2wo6X0xKy1n-A3d0o_L2VNWs5UbTEftr4FFujSUmKlVZXWbhBCdXUCj8b619cfnpwT4iU8sbe_ll5NQCyKZYDwSdAMyTEkF5c5PDOmxcf0Mgx_EBPdslevm4k4sWn5MxIWe5wz195AVMXnzIdGUJrNPF5Mw0EyUv7Klsf0IPLzArFCZU_MpxGvkMwjbHM3fc1eyHBkppIONA5RoBkn0um0oBRhUUkwayIiJP2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cRzL1RFg3nMD12zDYCgX9iwE10FavkXZ3cxGOjocm91O_AdbUUQBORR9hTPx1E7lozJY7lwrEdOdzIs6rd1qcvRI0Z3_PYzsxHJEKC2wddAlsX4qc4xyugaYl94IdBiQd9HySRs8bfCXUuFBKzGToRGfDsG7mUjnO8z3g78AlWpBbM08eAMixbrH4n7Q5moerRppDyQUrqRze6KRr6uEcwXPozw71ww-iBhI2nR71UxKOdmgfnxlb1uWHHLsGReDd5_rM3NJ3AMeflFNcuAGWt31ym_wms44bEmwychpHSzI7qP5ypbT93i35IB_V3LyKreMZ-b8Xgi2La2d-woTqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گوگل از Gemini 4 Argon رونمایی کرد: تمرکز ویژه روی مهندسی نرم‌افزار و امنیت سایبری  گوگل دیپ‌مایند نسل جدید مدل‌های پیشروی خودش رو با نام Gemini 4 Argon معرفی کرد. این مدل خروجی وحشتناک تا سقف ۱ میلیون توکن(پنجره Context نه ها. Outputای که همیشه 128K بود برای…</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/5451" target="_blank">📅 01:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5450">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eb66b496c.mp4?token=NFX9GaJgAvJxC5MOxsdMOxrKC3MY9EPgK3Qw5X4e7GU3LRg1Veuub7oJHB-FBVb7skAtII74To8u_5HE7hNlDibU7Dq0tbEnsrlTL8SQKjFWanZb-LVmPMeZK6z8b61ofZlitPCW4lhIO251EBx6m1O-TZ9uRfA5Kytvz7SqNmJw3D4UvkPXaIOTKO4DuEKOngm5jRIXdBS_fWA56KHUcPGKmWUTNkNvKbo8jiPMdt0uFt4pu2nK4raNnu6CcsyQDaSL4LaAbPqMWj3d9Qyfax9VRA2hKTZ6Kl8LXs_ZSxBTVeniAyTSWRkXadATc-qQcc38d3JKWEnoscPF_lsGGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eb66b496c.mp4?token=NFX9GaJgAvJxC5MOxsdMOxrKC3MY9EPgK3Qw5X4e7GU3LRg1Veuub7oJHB-FBVb7skAtII74To8u_5HE7hNlDibU7Dq0tbEnsrlTL8SQKjFWanZb-LVmPMeZK6z8b61ofZlitPCW4lhIO251EBx6m1O-TZ9uRfA5Kytvz7SqNmJw3D4UvkPXaIOTKO4DuEKOngm5jRIXdBS_fWA56KHUcPGKmWUTNkNvKbo8jiPMdt0uFt4pu2nK4raNnu6CcsyQDaSL4LaAbPqMWj3d9Qyfax9VRA2hKTZ6Kl8LXs_ZSxBTVeniAyTSWRkXadATc-qQcc38d3JKWEnoscPF_lsGGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوگل اون پشت در حال آپدیت دادنای مرموزانه و کار کردن روی مدل‌های Aiاش و بیرون دادن شایعه‌های مختلف:</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/5450" target="_blank">📅 01:11 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5449">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YoVOtJq7MM9Ibwc5TAUtyCtvqs_WaX7mf1Y48jftoyO-E12rcZg8DRe1rvUb2etD8vLSx1pPjSzyNtHH02Q3235_InKqAKDL6cUwyj040y0SIP3biaPW4jd_sTlyVdp3eIjATvbYkZ-rMWVa2IK5iZfk8aGsB_5ifB2q4WM-qoU4wTEZaaX-YPgDbCGkaDiLpq5jk9d_Yfh-QQM5oGSgLfLsrEHv2AOMZnkqVwvHHxRkjzFi4AefMmx2d5D5BYbnaetYwgy9pHmSnl3bBckIn5uXwyezIbOFhjR0kwIXPPffqnyl_DErqvaaCKzET2-0iF3OuKFXBbTvLtlPlDEG8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل از Gemini 4 Argon رونمایی کرد: تمرکز ویژه روی مهندسی نرم‌افزار و امنیت سایبری
گوگل دیپ‌مایند نسل جدید مدل‌های پیشروی خودش رو با نام Gemini 4 Argon معرفی کرد. این مدل خروجی وحشتناک تا سقف ۱ میلیون توکن(پنجره Context نه ها. Outputای که همیشه 128K بود برای اکثر مدلا) تولید می‌کنه و توی بنچمارک‌های مهندسی نرم‌افزار (امتیاز ۷۷.۹٪ در DeepSWE v1.1) و امنیت سایبری پیشتاز شده که به زودی می‌ذارمش. آرگون با هدف کارهای سنگین کدنویسی، تحلیل دیتابیس‌های حجیم و کشف خودکار آسیب‌پذیری‌های امنیتی طراحی شده.
هزینه‌اش برای دوره معرفی، قیمت خیره‌کننده‌ی
2$/10$
و بعد از اون،
4$/20$
اعلام شده. با 0.1$(بعدش 0.2$) برای هر یک میلیون Cache ورودی
دقیقا هم‌قیمت با Opus 5.5
باید فردا ببرمش زیر تست ببینم گوگل واقعا پرقدرت برگشت یا هایپ الکیه:)
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/5449" target="_blank">📅 01:03 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5448">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">بیدار شید بیدار شید
جمنای 4 اومدد</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/5448" target="_blank">📅 00:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5447">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MiHNd5V4QVWv3RVDOldkxqlQLMyBnSpjpK6wUoI3bMZKv61ul6kyIgZdSh1gV-0u0nhEXpI_yc4ekD57Pg_2llY6OaAnRvbevx_lTzMK-pvTvsK1ZI-cztUayXQStCYzWvRn2xxJ7h-zhrnsfqyJTZSNLNVeilzJjdI67TBa5Vuosqk41Gk2fGAaDi-88_8Miwn59C417MvWceudGM2pcDHGfL51thHn_mrmlFUxuahr5HjMbkhvJw_Yo_EWRDaTkicayJCBIHCsWelqp_JFzBVjG79DdSq3g3pnraocHGk0VlnAt5j5fdvL-GVnrGWv6M3lgZ6NLgQ12syp1IiNjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاهش هزینه‌های هوش‌مصنوعی با Auto Router در Cloudflare
کلودفلر قابلیت جدید Auto Router رو به سرویس AI Gateway اضافه کرده. این سیستم توی لبه شبکه (Edge) پیچیدگی هر درخواست رو می‌سنجه و به‌صورت خودکار بهینه‌ترین مدل رو انتخاب می‌کنه؛ یعنی برای پرامپت‌های ساده مدل‌های سبک و ارزون‌تر رو صدا می‌زنه و فقط کارهای پیچیده رو به مدل‌های گرون می‌سپاره تا بدون افت کیفیت، هزینه‌های پردازش به‌شدت کم بشه.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/5447" target="_blank">📅 23:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5446">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">من معتقدم با مدلهای رایگان، مدلهای چینی و ابزارهای رایگان هم میشه به خوبی کد نوشت و ابزار ساخت
و به زودی برای اثباتش، یه سری کار انجام میدم
چون میبینم دور و اطرافم کسایی رو که هیچ کاری نمی‌کنن، تلاشی نمی‌کنن، به بهونه‌ی اینکه من اشتراک Claude یا GPT plus ندارم و...
و این کارو انجام خواهم داد که شاید انگیزه‌ای بشه، و شاید ترغیب بشن یه سری افراد که شروع کنن ایده‌هاشون رو بسازن</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/5446" target="_blank">📅 21:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5445">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ویژگی‌ای که Dots و Cues و Grok Bot دارن نسبت به هرمس اینه که اومدن قابلیت‌ها رو محدود کردن!
بله درست شنیدین
همین محدود کردن قابلیت‌ها خودش فیچر خوبی بوده(برای اکثر مردم و برای مارکتینگ خودشون) و باعث شده کارهایی که میشه باهاش انجام داد ساده‌تر به نظر بیاد و سرراست تر بشه. از اون طرف، چون با LLM خودشون سازگاری صد درصد داره، به 99 درصد ارورهای مدل‌ها و api و... بر نمی‌خورید. VPS هم که نیاز ندارید دیگه
اونور قضیه، هرمس به شما "کنترل" و "هزینه صفر(روی لوکال)" میده که اون هم ارزشمنده برای قشر عظیمی</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/5445" target="_blank">📅 16:23 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5444">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">بچه‌ها ما قراره استریم داشته باشیم راجب دانشگاه و انتخاب رشته
اگر سؤالی دارید، می‌تونید به ایمیل matinsdungeon@gmail.com سؤالتون رو بفرستید با Subject استریم
روی استریم می‌خونیم سؤالاتتون و جواب می‌دیم با مهمونای گل</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/5444" target="_blank">📅 14:54 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5443">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d2ToPTub2gSx-Zo1AymPUT2lVD9ttTbxhkfLdDWSNAysVDE-W6Fgz8DcKXoRpsro2dPk12Q4mDRgIg60Tnj-eblXFzxOcci2YhKjYkUBD3pa3F_KPa9tku3aX7MvF9JZXdw8lFeCXscbbH2reY-Kuw7SZ6beGkAeiiEZZ5MWJh7iObqvaXQOrzFRNHBc1TKTv4eRlzAshV1L9y9t_RwgdOCfPO3xjUob3j5s_N6diAqF1vXSiAhrBoepz4SC_fTbRoHjPHOGaVdWG-xUfbq9R2E9T0tqrgBjxJyj091NW_dvusvA4UaRPoub_W6UnS_wEGRbAyQwVXrft8nivyTadA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همکاری رسمی OpenAI با پلتفرم Hermes
در اعلامیه‌ای جدید، همکاری رسمی OpenAI با اکوسیستم ایجنت هوشمند Hermes(Nous Research) تأیید شده است تا قابلیت‌های مدل‌های جدید و ابزارهای کدکس به شکلی منسجم‌تر در اختیار کاربران و توسعه‌دهندگان این پلتفرم قرار گیرد.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/5443" target="_blank">📅 14:44 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5442">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">بچه‌ها پدی 2500 دلار کردیت OpenAI داره که میخواد باهاش یه اپ بنویسه به انتخاب شما
رأی من زمین بازی سیستم دیزاینه
😂
❤️</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/5442" target="_blank">📅 14:33 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5441">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-poll">
<h4>📊 کدوم ایده رو با هم بسازیم؟</h4>
<ul>
<li>✓ تمرین انگلیسی با Shadowing</li>
<li>✓ زمین بازی سیستم‌دیزاین</li>
<li>✓ تبدیل کانال تلگرام به وب‌سایت</li>
<li>✓ ایده‌ی خودت رو بگو💡</li>
</ul>
</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/5441" target="_blank">📅 14:33 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5439">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jAcrJyIIRYtoUrca4G0kd_7tsU_scU0f2U696pQAVOoF-ZYSX7NuDy-njX4Rxi2kctNLdHFSqe94LBCtUUGCIEufuCGXPuNEwzr3alWxB6Ngn4Sv5vSs2Ynh_1zPNbNNl7ZopolrsJ88jI4RqSl33i-3YRrtnh-9O9sYwKZ5uezoo1zLdoJ4NnBcGvrL_PppN3mrt_zKMw60NyKTB84TjlCg8bTcp-eAw3qwcPEbIEywHyK0iS4Fj-Ez4YdyasidohVMI6QsGDZ8d293dqUjsq8wbkBIP6TqiN8kmbMk8hMVyt346qIajBIGMLRSiDUdVSEZOG5bm5u3sU5Le9DiEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bmxmqcJTDFmPr4XrXgpvMwYMaB2uZfIFLDoJ6rcR4MDL25nWeCI_oXUosk9pNHbKIBoZCRExVIBuUzX0dSUhLJJhFtWY2eEgPLies9PMIWPbGZpUPVwcfLrRvefjCrPx-SHzdTYMSJJaNKh2tWxevE4Q1qI8MgSd-v7d3k3gTOshzDSYgduFqBahqFTVlCLLMoUY9ylYHVe0wp59VSE4gy-PxjXzn--5JnfNgq4FdqvK7fa00782FJ1myyJvGQ9Jv5pX3auSJL5or5aMiBP6xiBpmSgQlAgNTunGherMUP-CvWrDZcVAK-WsAYXVkLxxskBkPQxSfgrw-dlIxkxF6g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قبلا برای این کار شاید 20 دقیقه زمان می‌ذاشتیم.
پیشرفت ai واقعا عالیه</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/5439" target="_blank">📅 14:28 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5437">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HaldrxVoRou2G21fzUlEGuqbFDhMH3-PCSbJg34SVpuoNDIMgODWnk5nA8RNxetu-pNA_RyAww28nSqRNueJPFZSRSDdVe82EugJEL3iiO8MOcj74CHSS1LdRWDuIb58n5uLJWAlwdvLjWGUATsFfDfdiL7-0Sx08sXvGRgpLc9o8EFnSWalJv6vlJfvGYo2aHODxcLkBKZLHtB-fOzVRxkv7H3eWOW-cXFh3OW9WRf_WWqCbKhCkevClYD_W9EX5YVylcG47ut5eIfyd8L_8GnQsDz4cZxTPisqWSMiVCH25eoSWgpccqwiUsesbMpmee8TlD8xR8h5EcPNmnpMew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aFZ-Al8zwhrjrzi4rvVw_I29LlCw6dwth1VIJk7ssdCPrewOFk3FO2K_d-Z85xFCBITen6wsZplwjqABG3aauAXAevFtQNMv5oq77EvAY2pna6TAxpdbZGmoLxCrmoPhrTXKnAczo9bP2dB8VT2LKMxh82p288XpTgVqWsBydQlja1p6qwwGeXrX3M4SkGW7IvEbqKDbTt0sqzHlycedxNFu9GGged-mbWaQUS83Dz30hvypkZ0AqTPTX9J_RkMHIccH6ZjlvguE-2A2gEJcwenAiW9EnDDpAUODGEhJWY9qDnAgVSQZDzBFoyN5G1DnhlRbi6ts90YRJAR8WLI3Zg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیروز Manus پلتفرم Cues رو رونمایی کرد
چند ساعت بعدش، OpenAI از Dots
و طراحی بصری ساب ایجنت‌های بامزشون خیلی شبیه هم دیگه‌ست
😂
نمیدونم چه توطئه‌ای در کاره</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/MatinSenPaii/5437" target="_blank">📅 12:41 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5436">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">گویا همه روی GPT 6.1 Sol مصرف توکن کمتر + قدرت بیشتر تجربه کردن</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/5436" target="_blank">📅 11:34 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5435">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">عرضه نسخه ابری OpenAI Codex در رویداد DevDay
اوپن‌ای‌آی بالاخره بعد از شیشصد سال که رقیبش آنتروپیک این قابلیت رو آورده بود، توی رویداد DevDay بالاخره مدل Codex رو به فضای ابری آورد تا توسعه‌دهنده‌ها محدود به اجرای محلی روی سیستم خودشون نباشن و بتونن از راه دور با گوشی یا هر دستگاه دیگه‌ای ازش استفاده کنن.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/5435" target="_blank">📅 10:03 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5434">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cd71a513a3.webm?token=cMpiYM90mQhGK3uJNbVOGZ__KbGZuLC6CSsOnudlZv_F_cqDDPiCtMbz2VMiAMOfn_GtMQBVGux7wrysoAkGWWiLVJudDSSfDmtQiwtaAG_dVfOMlnNAJvr5dhnI_3qWC-VTtSQs8x-kTSvWI5r_3hyo6v6BkyfBQzbIOGlwySW-hJYLa2QQCyCbFOP5RWw7vK6CBk7cXe6Ks3JfZgQLuxM7BsLxJH9r096ol-_DokCx8AO3wbQs8nvV1MPyfNJQDi_5mDddl8rAmQfOBdu7R6i4hnOWjsiKMO0xV_IXiX9FDUEkqufcOeCMCDMe6FFw8B6pqfAjbAx-LnM7wjkUtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cd71a513a3.webm?token=cMpiYM90mQhGK3uJNbVOGZ__KbGZuLC6CSsOnudlZv_F_cqDDPiCtMbz2VMiAMOfn_GtMQBVGux7wrysoAkGWWiLVJudDSSfDmtQiwtaAG_dVfOMlnNAJvr5dhnI_3qWC-VTtSQs8x-kTSvWI5r_3hyo6v6BkyfBQzbIOGlwySW-hJYLa2QQCyCbFOP5RWw7vK6CBk7cXe6Ks3JfZgQLuxM7BsLxJH9r096ol-_DokCx8AO3wbQs8nvV1MPyfNJQDi_5mDddl8rAmQfOBdu7R6i4hnOWjsiKMO0xV_IXiX9FDUEkqufcOeCMCDMe6FFw8B6pqfAjbAx-LnM7wjkUtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/5434" target="_blank">📅 08:12 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5433">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">حس می‌کنم یه رقابت خیلی سخت بین سرعت ریلیز مدلهای جدید AI و بالا رفتن قیمت دلار شکل گرفته</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/5433" target="_blank">📅 08:10 · 08 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
