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
<img src="https://cdn4.telesco.pe/file/tSP6EFCatCb_T-cGtttEHt-aqJYScKiSYgTsXPhkrJKdzSJ55zxbuUvRX4jf1PdTKonG6SjJtcNgBVL7dnppdT-2qAarvLOoniM_-zc4oFzU8NS8KbANE7p9IKfZaof7E6JWEOat19BMEhQE8eowe-PtU4I4nAV7REtEgNfZAm2DqRmVLl3m4w7zF05d3M0R9Kgl-Z2dUZAKSF6AmhuZTo1_nzVpNewgcr_lxVVviovSwhJZDvfBbsJLS5qJm75JfsHFa4gxZXx598g3JDJCW27xNe3kzTK-zGnDxOhi35DMuRWkDATVcR5xUGT9EZ07M3oAy-nXpKoEOtFPEO3PqQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.31M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-04 02:16:58</div>
<hr>

<div class="tg-post" id="msg-663042">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔹
پایان ست چهارم والیبال ایران و فرانسه لیگ ملت ها
🔹
فرانسه ۲ - ۲ ایران
🇫🇷
۲۵ | ۲۳ | ۲۵ | ۲۴
🇮🇷
۲۱ | ۲۵ | ۲۱ | ۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/663042" target="_blank">📅 00:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663041">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/797a3a0159.mp4?token=fT0K0iFhoJcQv9NqPBIFRJ8Tbgjvo_9FQDORo7zBtqbG-Fd6TfznIU8s2zxtzwyYAtqM5jLnTOXRBW6rEi_75hIgk5X32bT86Oz4iRaM61wLBjwTMNkEsvl806yhnR6pNU8Cj60xwrc8B-vwXj68LzaGUEHMXGk-ul0sI1apb8D_iXyq8vJ5wECd9MzIFxm65Se3U94y-5g7kwApNGHZC7JiEhgR_wu957qhErPSxSYguQMA3ByirjtVsbnyahpLsMuZp0w2GCjx_yniVWvI0OuILQl1W0rHmPcnOh-_xSLn-179xKoo73tmn8lnypqqG9y2rv78QFqVIwFIfsNvKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/797a3a0159.mp4?token=fT0K0iFhoJcQv9NqPBIFRJ8Tbgjvo_9FQDORo7zBtqbG-Fd6TfznIU8s2zxtzwyYAtqM5jLnTOXRBW6rEi_75hIgk5X32bT86Oz4iRaM61wLBjwTMNkEsvl806yhnR6pNU8Cj60xwrc8B-vwXj68LzaGUEHMXGk-ul0sI1apb8D_iXyq8vJ5wECd9MzIFxm65Se3U94y-5g7kwApNGHZC7JiEhgR_wu957qhErPSxSYguQMA3ByirjtVsbnyahpLsMuZp0w2GCjx_yniVWvI0OuILQl1W0rHmPcnOh-_xSLn-179xKoo73tmn8lnypqqG9y2rv78QFqVIwFIfsNvKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
چاک شومر اساسا فلسطینی شده است
🔹
شومر (رهبر دموکرات‌های سنا ) راهش را گم کرده است. او اساساً فلسطینی شده است. من درخواست کرده‌ام که یک لباس ابریشمی زیبا با لباس سنتی فلسطینی برایم ارسال شود. چاک شومر یهودی است. #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/663041" target="_blank">📅 00:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663040">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔹
لیگ ملت‌های والیبال، پایان ست سوم
🔹
فرانسه ۲ - ۱ ایران
🇫🇷
۲۵ | ۲۳ | ۲۵
🇮🇷
۲۱ | ۲۵ | ۲۱
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/663040" target="_blank">📅 00:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663039">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8683ecaf49.mp4?token=p2rWkThUE_lyZpWE9jwoleLIrS05PJ1KK77p0OloUgcRqOc4mQG6zdKD_-wQShWZH8FfzGdkCkzNBPWwRxvx-mLmNa6b7DVlpzPsb1gXRjRn26iFI_37n9CqVODDOYJysYAk_rGBCH_hN4AcXbGBCw0RKllx-0zyTPrCzm-ftHOeb7yvjTLyTw--laJbj13MwzVnE74LzBEjdzPxSawEplJAvBtfBt_cAYsLUkWwcoBRiXq940rzbCdO9zPUmBtInyjYsely5evhJy6aaptjZTmYb1LqBv9UPWPgeZ85fZML06BPLk_FD5HwFGGFpFlhDp0L-2hrOd2mXIk1mknPlT7OxMA-qKeGiOnzZ7dMIby2XvplwipHMEND4R8qXPAdeVmdSSRoWYHPZEGDA3NiCRLyqMH-qfSGSX8kc_G2c_I954cf1cuEoCZ5TgtOX3TWe6r7uSM5Vdn0NNAT2MET95xDEJ0JJziaelFoEaDt0a7KC2uJo0L8N4T27cva3EIgOJYsDDrd17x7uPZ1jKgUImy9D8swExN8JKFu5C8xyGYXf1d_-84OEpxudjJC-UirmzWXfyhrkAM4ucLJXeyWGUIcn_qGmcuOpU1GzgVcQSN09uz9sv17nbf1gYUkT2H47pBtPPLjGyAmQClPyhkUES9F2HVpcrmkgG-rqTlpsKk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8683ecaf49.mp4?token=p2rWkThUE_lyZpWE9jwoleLIrS05PJ1KK77p0OloUgcRqOc4mQG6zdKD_-wQShWZH8FfzGdkCkzNBPWwRxvx-mLmNa6b7DVlpzPsb1gXRjRn26iFI_37n9CqVODDOYJysYAk_rGBCH_hN4AcXbGBCw0RKllx-0zyTPrCzm-ftHOeb7yvjTLyTw--laJbj13MwzVnE74LzBEjdzPxSawEplJAvBtfBt_cAYsLUkWwcoBRiXq940rzbCdO9zPUmBtInyjYsely5evhJy6aaptjZTmYb1LqBv9UPWPgeZ85fZML06BPLk_FD5HwFGGFpFlhDp0L-2hrOd2mXIk1mknPlT7OxMA-qKeGiOnzZ7dMIby2XvplwipHMEND4R8qXPAdeVmdSSRoWYHPZEGDA3NiCRLyqMH-qfSGSX8kc_G2c_I954cf1cuEoCZ5TgtOX3TWe6r7uSM5Vdn0NNAT2MET95xDEJ0JJziaelFoEaDt0a7KC2uJo0L8N4T27cva3EIgOJYsDDrd17x7uPZ1jKgUImy9D8swExN8JKFu5C8xyGYXf1d_-84OEpxudjJC-UirmzWXfyhrkAM4ucLJXeyWGUIcn_qGmcuOpU1GzgVcQSN09uz9sv17nbf1gYUkT2H47pBtPPLjGyAmQClPyhkUES9F2HVpcrmkgG-rqTlpsKk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
اردوغان و شی و پوتین به درخواست من در جنگ ایران دخالت نکردند #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/663039" target="_blank">📅 00:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663038">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6384093be9.mp4?token=Snn-RPYsXHzlFEZpEqAddr_Gk3MAwSfbBUvKR4jCQXI32DK97yESXrXRr8Da0o9_0GtHf64GqZEnS9_vFoN9Hje2hAT3Rt8kSZRHOJoEsAP5rsmv82kxL4amU5NB-2tZysjhKAIBn_RR2T8YUaawdg2baHp1eOm9w6bA3k5HQAaFPGYWWd5JAmqJUzu_u_WxdBVWtjjuFSCN_bqBWJJDSp_Dw9aMg8QH5zFf_UP6LRZrF1kgbE9Yu_eJdJHi0WnvUnOT5P56avxoNDmB4AYIw3sUAxRNRZ6I7GxyCTtZOhwcRt_cTM8yjhykrzNAywPIOoVPqbhrpixl-88lhpIBAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6384093be9.mp4?token=Snn-RPYsXHzlFEZpEqAddr_Gk3MAwSfbBUvKR4jCQXI32DK97yESXrXRr8Da0o9_0GtHf64GqZEnS9_vFoN9Hje2hAT3Rt8kSZRHOJoEsAP5rsmv82kxL4amU5NB-2tZysjhKAIBn_RR2T8YUaawdg2baHp1eOm9w6bA3k5HQAaFPGYWWd5JAmqJUzu_u_WxdBVWtjjuFSCN_bqBWJJDSp_Dw9aMg8QH5zFf_UP6LRZrF1kgbE9Yu_eJdJHi0WnvUnOT5P56avxoNDmB4AYIw3sUAxRNRZ6I7GxyCTtZOhwcRt_cTM8yjhykrzNAywPIOoVPqbhrpixl-88lhpIBAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
ترامپ مدعی شد بمباران مدرسه میناب و کشتار دانش‌آموزان کار ارتش آمریکا نبوده است #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/663038" target="_blank">📅 00:22 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663037">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e068d317d5.mp4?token=DlTHyrWc0afRnH6uV2ZGUGVhZh5wXCy6BuI-x5HnOaZxp9igtSjDKnBdox2tp-daoMh8b3M1f2PFMtGiBj4OcKe7tIqhUKGO-fmsW5bgswR7X-dNgwWahmnZO40jXBl7HcWFxMq57vYalPl3ACeNM6gFQ1oTjOG0le5J9UoBpc-fIhTUZ7qx-ohSzAXHpsC_lzZBBgrWHjRqX88GYEPg7hveFGuR3Kb4PBMAQh7RPiojCju-yULeCth4Ky6fJ3FxqwRPmGSSlIhFO_BOl6W_Xxk0SgXLqZAJKqiLgG1zbl3-zb4_Xl3SN8ntMwrYutBFHftn3salfbGhqrJaT-eQVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e068d317d5.mp4?token=DlTHyrWc0afRnH6uV2ZGUGVhZh5wXCy6BuI-x5HnOaZxp9igtSjDKnBdox2tp-daoMh8b3M1f2PFMtGiBj4OcKe7tIqhUKGO-fmsW5bgswR7X-dNgwWahmnZO40jXBl7HcWFxMq57vYalPl3ACeNM6gFQ1oTjOG0le5J9UoBpc-fIhTUZ7qx-ohSzAXHpsC_lzZBBgrWHjRqX88GYEPg7hveFGuR3Kb4PBMAQh7RPiojCju-yULeCth4Ky6fJ3FxqwRPmGSSlIhFO_BOl6W_Xxk0SgXLqZAJKqiLgG1zbl3-zb4_Xl3SN8ntMwrYutBFHftn3salfbGhqrJaT-eQVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
ترامپ از اروپایی‌ها در قبال موضوع ایران انتقاد می‌کند: من از ایتالیا ناامید بودم
🔹
من از بریتانیا ناامید بودم. ما از آلمان و فرانسه ناامید هستیم. ما از بیشتر آنها ناامید هستیم. اسپانیا یک نمایش وحشتناک است. اسپانیا حتی از دیدگاه شما هم وحشتناک است #Devil…</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/663037" target="_blank">📅 00:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663036">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c1037aa46.mp4?token=EINSHluP_sei-HsVzGyr43dKJ8MgUUQy1oXW4kOAqBy8yUnBalzKgfI0N0K-OmdQeL5BsGkqpF8C8wyhpQFM4QsfLc9mgW7C3HL8hLpHETPjeiXTA6KAU5eLTu37SIN2Ahpny8BcHlLF5vVABICJ82G5gpl6cFRyFPW2-eBlZAQTF6ksQzHMGLXQXAvgH22sehChb4-ea1_H3HW9jnMMoQ1ZbUOLHG0EiRl2xk6zK3hK6ERaKeqrxccPmBXnzwHW-C-C6J8vC_j8RXoeXHwwP80J5jCLfgFZiJUBjyPN9fvkb5YyHWpvWwRIFq0F-Vpu61nn39sv-KYSLtDeahTRFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c1037aa46.mp4?token=EINSHluP_sei-HsVzGyr43dKJ8MgUUQy1oXW4kOAqBy8yUnBalzKgfI0N0K-OmdQeL5BsGkqpF8C8wyhpQFM4QsfLc9mgW7C3HL8hLpHETPjeiXTA6KAU5eLTu37SIN2Ahpny8BcHlLF5vVABICJ82G5gpl6cFRyFPW2-eBlZAQTF6ksQzHMGLXQXAvgH22sehChb4-ea1_H3HW9jnMMoQ1ZbUOLHG0EiRl2xk6zK3hK6ERaKeqrxccPmBXnzwHW-C-C6J8vC_j8RXoeXHwwP80J5jCLfgFZiJUBjyPN9fvkb5YyHWpvWwRIFq0F-Vpu61nn39sv-KYSLtDeahTRFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
توانایی هسته‌ای ایران تهدیدی برای جهان بود  مارک روته، دبیرکل ناتو:
🔹
واقعا می‌خواهم روشن کنم که کاری که شما در مورد ایران انجام می‌دهید چقدر مهم است. این، اول از همه، در مورد توانایی هسته‌ای است که ایران اساسا به آن دست یافته بود و این می‌توانست تهدیدی برای…</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/663036" target="_blank">📅 00:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663035">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d33de4e4d.mp4?token=D8R4O6BZrwv9q_dwrt0ciqH_ejtZH7ZD9lFBCACX4jIBr-5SRWERZLp89KhCBdlSVJR7Q9tIimZrG27E3NZJQzCoLUst3heq9RiHfa6z_Ws2sI5c3R9s5uGvWJV74zgWSywsTjhGxa9RK_vlObrbTIUjbVSc5R_ItwUAZ6OAtdQkrO0lX84wbSMnUhXQVXMMfc3GKzdDt5sNvHxBVMVyYfZLMI381X6d6E7iul-ckYc8IFhPZ51PGHtae07iEu-wv0nPO3UymBHrhpv4jY67KuqrKhEs-oVIPwr9A0045XGytS2D0YbEHpsDpqZc0lqgAIepKMhxvt-KzSOKGAe9Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d33de4e4d.mp4?token=D8R4O6BZrwv9q_dwrt0ciqH_ejtZH7ZD9lFBCACX4jIBr-5SRWERZLp89KhCBdlSVJR7Q9tIimZrG27E3NZJQzCoLUst3heq9RiHfa6z_Ws2sI5c3R9s5uGvWJV74zgWSywsTjhGxa9RK_vlObrbTIUjbVSc5R_ItwUAZ6OAtdQkrO0lX84wbSMnUhXQVXMMfc3GKzdDt5sNvHxBVMVyYfZLMI381X6d6E7iul-ckYc8IFhPZ51PGHtae07iEu-wv0nPO3UymBHrhpv4jY67KuqrKhEs-oVIPwr9A0045XGytS2D0YbEHpsDpqZc0lqgAIepKMhxvt-KzSOKGAe9Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
ترامپ: اردوغان می‌خواست برای کمک به ایران وارد جنگ شود  رئیس جمهور آمریکا بامداد پنجشنبه در دیدار با «مارک روته» دبیرکل ناتو:
🔹
«[اردوغان] کاندیدای اصلی برای ورود به جنگ با ایران بود. شاید، از طرف ایران، زیرا طرفدار اسرائیل نیست. من از او (اردوغان) خواستم…</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/663035" target="_blank">📅 00:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663034">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔹
ترامپ: اردوغان می‌خواست برای کمک به ایران وارد جنگ شود
رئیس جمهور آمریکا بامداد پنجشنبه در دیدار با «مارک روته» دبیرکل ناتو:
🔹
«[اردوغان] کاندیدای اصلی برای ورود به جنگ با ایران بود. شاید، از طرف ایران، زیرا طرفدار اسرائیل نیست. من از او (اردوغان) خواستم که [در جنگ ایران] دخالت نکند و او دخالت نکرد».
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/663034" target="_blank">📅 00:17 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663033">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔹
سفر در زمان به قلب تاریخ... جایی که تشنگیِ یک کودک، او را به خیمه‌های کربلا و قصه‌ عمو عباس رساند
این ۹۰ ثانیه را تا آخر ببینید
A journey through time to the heart of history... where a child's thirst leads him to the tents of Karbala and the story of Uncle Abbas.
Watch these 90 seconds until the end.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/663033" target="_blank">📅 00:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663032">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gfqg74t70d1nff4yR5yVfKTklLuu_7ufZFFP7GDK_T5cacRZyXitiC1_mAezRQQO_ajTGIV5DbFTwqq5K9eWtgQ7AKjE0Oq8HN461ESLUs_pZ-18A4ljwazxoGX5bomdMwyRZzDWwpHFCZXEeAqpJRZcvK8P1uEeHmtEo5hOsXYqcDM041bpPgt6QtKGajtdJ7aot7V6CHOQGvyCM_-eWm3yPXb_hQ6TG64WLecTMnnka3U7D4PJZ5ws8lKsAf_65lcItahKWRyNSC4dJgxqi6Ta5zeFSY1n1d3by_C9IFPednyeinzWnBHTXUC-iVYCIfvmvwWfvH-vWdvxGr63rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/akhbarefori/663032" target="_blank">📅 00:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663031">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔹
عجیب اما واقعی؛ به دلیل اشتباه تیم ایران در تعویض بازیکنان؛ امتیاز این ست از ۱۸-۱۸ تساوی به ۱۹-۱۶ به نفع فرانسه تغییر کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/663031" target="_blank">📅 23:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663030">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔹
پایان ست دوم والیبال ایران و فرانسه لیگ ملت ها
🔹
فرانسه ۱ - ۱ ایران
🇫🇷
۲۵ | ۲۳
🇮🇷
۲۱ | ۲۵
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/663030" target="_blank">📅 23:54 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663029">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔹
پزشکیان: هر فردی بخواهد به هر بهانه‌ای وحدت را به هم بزند، آب در آسیاب دشمن ریخته است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/663029" target="_blank">📅 23:50 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663028">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔹
خبرهای داغ امروز را از دست ندهید
🔹
🔹
ایجادخط ارتباط مستقیم میان آمریکا و ایران
👇
khabarfoori.com/fa/tiny/news-3225360
🔹
چرا جی‌دی ونس برای مذاکره با ایران، یک استراحتگاه لوکس سوئیسی را انتخاب کرد؟
👇
khabarfoori.com/fa/tiny/news-3225366
🔹
راز جوراب‌های پاره بازیکنان جام جهانی چیست؟
👇
khabarfoori.com/fa/tiny/news-3225487
🔹
زنی که افشاگر فساد رئیس‌جمهور بود کشته شد
👇
khabarfoori.com/fa/tiny/news-3225365
🔹
وایرال شدن بیل زدن پزشکیان در اسلام آباد
👇
khabarfoori.com/fa/tiny/news-3225358
🔹
ویدئوهای جذاب ما را در وبسایت خبرفوری کلیک کنید
🔹
http://aparat.com/akhbar.fori/videos</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/663028" target="_blank">📅 23:48 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663027">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HRAH-3cN_YoqEpJyv2BlJZ8tKnlVmayqk1ZeMRiJdmdKXN_MDbPRV9MGHA6H_g69zYD1syeqwm2R0K0Tcnn60ZHpwa6LzktefBZMNqwaPDSAj5DFAezpVEUSJlW0sDyPES0h2KPa3FYvDAOgtQsYelOzvsMb1KXnsG3o6BD91roYg89lSnmY7icclMIgARPcG8DNp31u7EfaoM740Bg8EMGcShD6s_B9a_y7vqaco5Lxfa_Igt8gA6MMJZVNL09gn_JeLvKbnMwvxSMXpFR4slbDsyNXmrUE1Pg6eGSE0IvBNQmvKO2aRMJqO32TWOKuSfz0Le3s4WPfdPTrxh0ARA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
بقائی: اظهارات ضد و نقیض مقامات آمریکایی درباره تفاهم خاتمه جنگ تحمیلی، کمکی به کاهش بدگمانی متراکم ایرانیان نسبت به آمریکا نخواهد کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/663027" target="_blank">📅 23:44 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663026">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-text">کاروان کربلا در راه است...
❤️‍🩹
✍🏼
‌نوشتن از تو همیشه سخت است، به وقت دهم محرم از همیشه سخت‌تر... .
با کدام قلم باید از تو نوشت؟! با کدام کلام باید از تو گفت؟! در ساعاتی که کلمات به لکنت افتاده‌اند و جملات سرگردان شده‌اند.
اصلا چگونه از تو بگوییم وقتی که تو خون خدایی و خودش زیارت تو را به ما آموخته است... . آری گفتن و نوشتن از تو فقط کار خداست؛ ما فقط محض تسلی دل داغدارمان چند خطی می‌نویسیم امشب.
🌘
امشبی که هر سال آرزو می‌کنیم به صبح نرسد؛ که صبحِ فردا، معرکه‌ای در پیش داری عزیزِ عزیزتر از جانم... . معرکه‌ای که به قیمت شکستن چندبارهٔ تو، حق و باطل را برای همیشه از هم جدا می‌کند. فردا نه یک‌بار، که بیش از ۷۲ بار به شهادت میرسی پناهِ عالم... .
💔
گودال بهانه است؛ وگرنه کمرت پیش از رفتن به زیر سم اسبان، در کنار علقمه می‌شکند. و استخوان‌های سینه‌ات، با دست و پا زدن های اصغرت خورد می‌شود... . قلب نازنینت، پیش از تیر سه شعبهٔ مسموم، با پا بر زمین کشیدن‌های قاسم پاره می‌شود. پیکر مبارکت، پیش از گودال، کنار هر تکه از علی‌اکبرِ اربا اربا، از هم می‌پاشد. و پیش از آنکه تشنگیِ خودت تو را آزار دهد، فکر عطش کودکان حرم، تو را از پای در می‌آورد. و تصور جسم نحیف و زخمی رقیه، در اسارت این حرامیان بی‌رحم، برای تو هزاران بار از زخم‌های بی‌شمار پیکرت دردناک‌تر است.
😔
و زینب.... زینبی که فکر اسارت و جسارت به ساحت مقدسش، برای هزار بار رفتن جان از بدن کافیست.
🥀
و در نهایت تو، با تنی خسته و قلبی مالامال از درد و غم، به گودی قتلگاه می‌روی و داغی به وسعت همه تاریخ، بر دل زمینیان و آسمانیان می‌گذاری. می‌روی اما تمام نه، بلکه جاودانه می‌شوی. و خونت، آن خون پاک و مطهرت، در رگ‌های زمان جاری می‌شود و جانی به این جهان مرده می‌دهد. آری نبرد عاشورای تو در دهم محرم ۶۱ هجری شروع شد، اما تمام نه... .
🚩
خوب که بنگری عاشورا هنوز به شب نرسید‌ه‌ ست. و ما اگرچه عاشورای سال ۶۱ هجری را درک نکردیم اما در وسطِ میدانِ امتدادِ عاشورای تو ایستاده‌ایم. جایی که فرزندت با قلبی داغدار از ستم و جنایت همه شمرها و یزیدان تاریخ، هر روز ندای هل من ناصر سر می‌دهد که عاشورای تو، فقط با ظهور او به شب می‌رسد. شبی که به صبح دولت کریمه او می‌پیوندد. و به قول سید شهیدان اهل قلم «جایی برای ای کاش‌ها و اگرها باقی نمانده است. عاشورا هنوز نگذشته و کاروان کربلا هنوز در راه است. اگر تو را هوس کرب‌وبلاست، بسم‌الله ...»
@Heyate_gharar</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/663026" target="_blank">📅 23:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663025">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔹
فرودگاه بن گوریون هنوز به حالت عادی بازنگشته است
تایمز اسرائیل:
🔹
رئیس سازمان فرودگاه‌های اسرائیل هشدار داده است با وجود آغاز انتقال بخشی از سوخترسان‌هایی آمریکایی که ماه‌ها در فرودگاه بین‌المللی بن‌گوریون در تل‌آویو پارک شده‌اند
🔹
حضور این هواپیماها همچنان تهدیدی برای لغو پروازهای ۱۰۰ هزار مسافر در اوج فصل تابستان محسوب می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/663025" target="_blank">📅 23:26 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663024">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔹
پزشکیان: رهبر انقلاب در پیامش به ما وحدت و انسجام را ابلاغ کرده است
🔹
اگر می‌خواهیم به جایی برسیم باید برای رسیدن به وحدت و انسجام تلاش کنیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/663024" target="_blank">📅 23:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663023">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔹
حریدی‌ها خطاب به نتانیاهو: رژیم را دگرگون می‌کنیم
🔹
هزاران نفر از حریدی‌ها امروز در اعتراض به دستگیری دانشجویان مدارس مذهبی و یهودیان حریدی، جاده‌ها و خیابان ها را مسدود و عنوان کردند که «رژیم را دگرگون می‌کنند».
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/663023" target="_blank">📅 23:21 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663022">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔹
پزشکیان: امروز هم در سران قوا، هم در شورای امنیت و هم در مجموعه سیستم یک نگاه مشترک داریم
🔹
اگر دستاوردی داریم دستاورد این مجموعه، رهبر بزرگ و مردم عزیز است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/663022" target="_blank">📅 23:18 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663021">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔹
هفته دوم والیبال لیگ ملت ها
🇫🇷
فرانسه ۲۵
🇮🇷
ایران ۲۱
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/663021" target="_blank">📅 23:13 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663020">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔹
رئیس جمهور در حرم امام: امروز ایران را در منطقه به عنوان یک قدرت می‌بینند
🔹
فکر می‌کردند کار جمهوری اسلامی سه روزه تمام است و مثل سوریه یک شخصی از خودشان را سر کار می‌آورند.
🔹
سپاهیان و ارتشیان ما با جان فشانی کاری کارستان کردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/663020" target="_blank">📅 23:11 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663019">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔹
پزشکیان: هیچ ملتی روی سعادت نمی‌بیند، مگر اینکه به قرآن عمل کند  رئیس‌جمهور در حرم مطهر امام خمینی(ره):
🔹
من به عنوان مسئول در این کشور، وظیفه ام این است که کتاب خدا در مقابل دیدگانم باشد و به آن عمل کنم و عدالت را در جامعه پیاده کنم.
🔹
من نمی توانم مسئول مملکتی…</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/663019" target="_blank">📅 23:05 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663018">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔹
پزشکیان: هیچ ملتی روی سعادت نمی‌بیند، مگر اینکه به قرآن عمل کند
رئیس‌جمهور در حرم مطهر امام خمینی(ره):
🔹
من به عنوان مسئول در این کشور، وظیفه ام این است که کتاب خدا در مقابل دیدگانم باشد و به آن عمل کنم و عدالت را در جامعه پیاده کنم.
🔹
من نمی توانم مسئول مملکتی باشم که مملکت شیعه و علی باشد و یک عده بیکار باشند و گرسنه باشند. خدا از من نخواهد گذشت، از دولت نخواهد گذشت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/663018" target="_blank">📅 22:58 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663017">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔹
بقائی: اظهارات ضد و نقیض مقامات آمریکایی درباره تفاهم خاتمه جنگ تحمیلی، کمکی به کاهش بدگمانی متراکم ایرانیان نسبت به آمریکا نخواهد کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/663017" target="_blank">📅 22:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663016">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔹
معطلی دوباره برای طارمی و الهویی در فرودگاه و معطلی تیم ملی
🔹
در حالی که تیم ملی ایران برای سومین بار در حال سفر به آمریکاست، بار دیگر مزاحمت آمریکا برای تیم ایران باعث معطلی تیم در فرودگاه شده است.
🔹
اعضای تیم ملی فوتبال ایران ساعتی قبل برای انجام دیدار…</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/663016" target="_blank">📅 22:44 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663015">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔹
هفته دوم والیبال لیگ ملت ها
🇫🇷
فرانسه ۲۵
🇮🇷
ایران ۲۱
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/663015" target="_blank">📅 22:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663013">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromقرار مداحی</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">نماهنگ مظلوم من</div>
  <div class="tg-doc-extra">محمد حسین حدادیان قرار مداحی /  @gharar_madahi</div>
</div>
<a href="https://t.me/akhbarefori/663013" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🥀
صلی علی مظلوم من
آبت ندادن رفتی از حال
پیراهنت رو دستمه
دستم گرفته بوی گودال
🎙
#محمد_حسین_حدادیان
#عاشورای_حسینی
مرجع رسمی مداحی و نماهنگ انقلابی
👇🏻
👇🏻
@gharar_madahi</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/663013" target="_blank">📅 22:24 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663012">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942f58146c.mp4?token=bt7qljrHJFIGXXttDT5ZB55Uqrt8pGLhi-2iMekOpR1lnwkQXzhqgT_SRVeJOZaGkMpWRWsK_y7toyEKD62V-1ne5OxG-Ec5ozxYwc7HdOcFC31-kJgbVw0u3teTW90GAkHk8gfIokQawYifS9nD9w213wvc8SG3W9briCYn-jvDt2EQuCOpZNrYDsUmLBsEYBgdYF5Ecdh-bkTzI3lfMKXtTXJpH7jeZxGyyTZnUJp1xLt9ttAQorG-WWLlLS8Wq4w_zjUTpskaV3doCTxp90St5FnEjQyKuejXkXfoveOEwziubvv_BGEnF4b4wKuu9orzSW4l9VrVbuYUTOMflQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942f58146c.mp4?token=bt7qljrHJFIGXXttDT5ZB55Uqrt8pGLhi-2iMekOpR1lnwkQXzhqgT_SRVeJOZaGkMpWRWsK_y7toyEKD62V-1ne5OxG-Ec5ozxYwc7HdOcFC31-kJgbVw0u3teTW90GAkHk8gfIokQawYifS9nD9w213wvc8SG3W9briCYn-jvDt2EQuCOpZNrYDsUmLBsEYBgdYF5Ecdh-bkTzI3lfMKXtTXJpH7jeZxGyyTZnUJp1xLt9ttAQorG-WWLlLS8Wq4w_zjUTpskaV3doCTxp90St5FnEjQyKuejXkXfoveOEwziubvv_BGEnF4b4wKuu9orzSW4l9VrVbuYUTOMflQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
حضور قالیباف و مخبر در هئیت ریحانه الحسین _ شب عاشورا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/akhbarefori/663012" target="_blank">📅 22:21 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663011">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0842175d8.mp4?token=vs3AAKbRt_txOfYWBa5Yhz1T7ENjj4USL7av7Fs0hnqwowMZFGGpySMy-GmVLSNFfnJGWvfVHY5XRUYziLBc2CN64SZ9FwwpI9ZavycaJnXYSv7AKZbxbQ11SX_msW-ooLtBuXqV5zmmQdYxzuPYT62FOuB4OcslirAVyTe4n7r51ORB3Ixtwp-i-8lB2o7pq0nNoFt_1sWGstZqgCt3dvJ9u_l271Vr3-vVUpME9R-bwJEskXw8x7HOq5ln8YPoeAK4I-97iXqkDFp60bsr8-yCuLsgUGonaCasXWG0WVW-QaBAvqfutCG6gVrxDqI7y2z2SBoa3EWct3P60uN5Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0842175d8.mp4?token=vs3AAKbRt_txOfYWBa5Yhz1T7ENjj4USL7av7Fs0hnqwowMZFGGpySMy-GmVLSNFfnJGWvfVHY5XRUYziLBc2CN64SZ9FwwpI9ZavycaJnXYSv7AKZbxbQ11SX_msW-ooLtBuXqV5zmmQdYxzuPYT62FOuB4OcslirAVyTe4n7r51ORB3Ixtwp-i-8lB2o7pq0nNoFt_1sWGstZqgCt3dvJ9u_l271Vr3-vVUpME9R-bwJEskXw8x7HOq5ln8YPoeAK4I-97iXqkDFp60bsr8-yCuLsgUGonaCasXWG0WVW-QaBAvqfutCG6gVrxDqI7y2z2SBoa3EWct3P60uN5Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
ترامپ: خواهیم دید چه می‌شود  ادعای رئیس جمهور آمریکا:
🔹
تهران امتیازات بسیار بزرگی می‌دهد.
🔹
خواهیم دید چه اتفاقی می‌افتد، فعلا که اوضاع بسیار خوب پیش می رود. در حال برنده شدن هستیم. #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/akhbarefori/663011" target="_blank">📅 22:15 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663010">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/193cd69f4b.mp4?token=Io69wpcSuMaxl3JAOTm9vYidwOya1HTHQbei61KyIoyaT7NAHRHa8C9wjPTrs8lyXuHUfj8MJjzXcDbKlQZ4GvxHSRlx9D13HkAjfXVkBR1FuUOJ4GSRZpn4AQdOKPAeutvKszI5Gnz4Mila_Spd06wEdbmUPKX35pqNAqBSVtVlk4RlIsQitWOsq70_PxNan5RL1KqCu2tWzrwCg0DCjdc2ExdxwiJbBa-3PHaxxzw5azylTD5iAI-KR93TlDYEJtk0XLBpdGoX_jvItXPevdCmTue6O-NEwovLALRDyOy_w7uG_FdZ_gVuGbtwQUAtOfLAMzo1p7ZHM_SnA_HUug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/193cd69f4b.mp4?token=Io69wpcSuMaxl3JAOTm9vYidwOya1HTHQbei61KyIoyaT7NAHRHa8C9wjPTrs8lyXuHUfj8MJjzXcDbKlQZ4GvxHSRlx9D13HkAjfXVkBR1FuUOJ4GSRZpn4AQdOKPAeutvKszI5Gnz4Mila_Spd06wEdbmUPKX35pqNAqBSVtVlk4RlIsQitWOsq70_PxNan5RL1KqCu2tWzrwCg0DCjdc2ExdxwiJbBa-3PHaxxzw5azylTD5iAI-KR93TlDYEJtk0XLBpdGoX_jvItXPevdCmTue6O-NEwovLALRDyOy_w7uG_FdZ_gVuGbtwQUAtOfLAMzo1p7ZHM_SnA_HUug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
غار یخی چما، کوهرنگ چهارمحال و بختیاری
خنک‌ترین نقطه خاورمیانه در تابستان به علت موقعیت دره و زاویه تابش خورشید
#اخبار_چهارمحال_و_بختیاری
در فضای مجازی
👇
@akhbarchaharmahalvabakhtiari</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/663010" target="_blank">📅 22:10 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663009">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔹
به گزارش MS NOW، در جلسهٔ ناهار امروز ترامپ با سناتورهای جمهوری‌خواه در کنگره، سناتور بیل کسیدی، در مورد تفاهم‌نامهٔ ایران با ترامپ مقابله کرده است
🔹
به گفتهٔ یک منبع، کسیدی در جریان این برخورد «فریاد می‌زد»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/663009" target="_blank">📅 22:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663003">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">زمینه</div>
  <div class="tg-doc-extra">سیدمهدی حسینی هیئت قرار / @heyate_gharar🏴</div>
</div>
<a href="https://t.me/akhbarefori/663003" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">پک هیئت قرار  ویژه شب عاشورا
🖤
#محرم
محتوای مذهبی ویژه محرم در این کانال
👇🏻
👇🏻
@Heyate_gharar</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/663003" target="_blank">📅 22:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663002">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ebfa87979.mp4?token=gX7ASq96fGo7fDai2x86FNpPbpoJ2vLKTBiFNzdqJLsTp7erR1W62Gk67nsqPtmiq_G9w3APK0G-XS04Gn6K5_xzHSyOEjUrlJqKGddrR2sHJusXZYjLivvc4jYMwwsOQ02qchBLqi3s__AbQMT1txnFEasM08VdYVqKDAadBk5C6ftmGL6ZiO6hDCwvK1SugSTK07DdupXeK2lFy3Zm765Otkx5eLgfWSQ6hLxwFYmZZOWwrWFOWt6VrcZz0Nl4Pvhmp_xv_MogExfL_gZIcMLgBl2Q_IhFYALSNth1FntfmMoAKlHDSe0Qagk5jnb_GxJsVlAbooiGEXIB9e64Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ebfa87979.mp4?token=gX7ASq96fGo7fDai2x86FNpPbpoJ2vLKTBiFNzdqJLsTp7erR1W62Gk67nsqPtmiq_G9w3APK0G-XS04Gn6K5_xzHSyOEjUrlJqKGddrR2sHJusXZYjLivvc4jYMwwsOQ02qchBLqi3s__AbQMT1txnFEasM08VdYVqKDAadBk5C6ftmGL6ZiO6hDCwvK1SugSTK07DdupXeK2lFy3Zm765Otkx5eLgfWSQ6hLxwFYmZZOWwrWFOWt6VrcZz0Nl4Pvhmp_xv_MogExfL_gZIcMLgBl2Q_IhFYALSNth1FntfmMoAKlHDSe0Qagk5jnb_GxJsVlAbooiGEXIB9e64Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
عزاداری باشکوه در مهرشهر کرج
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/663002" target="_blank">📅 22:02 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663001">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2cfac7da8.mp4?token=jKgMiTyFgTsksYNsGC0S-7w1Vdc1sKY17NXWN8Sqpy8TcqBTdDjQkV3-kRhSySSoge71EbmkcVKpH_mqLU40HbIe1j11lc6JzLcCM7OErk-d5x9_s86Uk_XBBXyRVRikbDm-CtM-kc_S56ATMC1kVKFmRmZTv1qjkrGS-20mv_9hKv_N9JpSYJzoW2JbuH9zGbvhUI8bY-688crw9IygWgH2MKCjvIVuz6qMRW9fHsEYHdSvpSUfxutq9qje3KohsA6nLS3aSlioyV6Rb6CbDhphbGOddgDQV3dllIXo-PVc6tMKxQnN-eh7PIjDoBQ88BdKTtwwxkiXaxQMT3jy8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2cfac7da8.mp4?token=jKgMiTyFgTsksYNsGC0S-7w1Vdc1sKY17NXWN8Sqpy8TcqBTdDjQkV3-kRhSySSoge71EbmkcVKpH_mqLU40HbIe1j11lc6JzLcCM7OErk-d5x9_s86Uk_XBBXyRVRikbDm-CtM-kc_S56ATMC1kVKFmRmZTv1qjkrGS-20mv_9hKv_N9JpSYJzoW2JbuH9zGbvhUI8bY-688crw9IygWgH2MKCjvIVuz6qMRW9fHsEYHdSvpSUfxutq9qje3KohsA6nLS3aSlioyV6Rb6CbDhphbGOddgDQV3dllIXo-PVc6tMKxQnN-eh7PIjDoBQ88BdKTtwwxkiXaxQMT3jy8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
شمع‌گردانی خدام حرم رضوی در مراسم خطبه‌خوانی شب عاشورا
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/663001" target="_blank">📅 21:57 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663000">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d3fbe8bbd.mp4?token=Ad12HbiS4rTONi81LpDMWqW08Xz94VLrrc_PXqGgvi0u5lWzQLofE521xJeXHKfmpEDVwOJwidUs3UP0vX3x0p0XYlRN6swcitcgoE2M1-9uoxt4iqXl1JL6oTjfpbzDg8XeRdhV65Q9GbfXcRx-AI37ZLS1HRTPKzNCxqkV_1Y151J-kH78Lm4FOaXYwTu8L7mWxmtlK5HLzTlZC7IzsVgfvZzJfJdchfVk-qJpqvUXO46oYk6sYexLntmLKFh5PvpZW64DopeJo07H8DqJb9UjCCY4EF0B0M_uDfF3eGlxIVK7Uv016tSdKsZ58tEWZka6n_PNBMm0xJwmLchbIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d3fbe8bbd.mp4?token=Ad12HbiS4rTONi81LpDMWqW08Xz94VLrrc_PXqGgvi0u5lWzQLofE521xJeXHKfmpEDVwOJwidUs3UP0vX3x0p0XYlRN6swcitcgoE2M1-9uoxt4iqXl1JL6oTjfpbzDg8XeRdhV65Q9GbfXcRx-AI37ZLS1HRTPKzNCxqkV_1Y151J-kH78Lm4FOaXYwTu8L7mWxmtlK5HLzTlZC7IzsVgfvZzJfJdchfVk-qJpqvUXO46oYk6sYexLntmLKFh5PvpZW64DopeJo07H8DqJb9UjCCY4EF0B0M_uDfF3eGlxIVK7Uv016tSdKsZ58tEWZka6n_PNBMm0xJwmLchbIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
تصاویری از عزاداری عشایر ترک زبان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/663000" target="_blank">📅 21:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662999">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔹
نتانیاهو: موقعیتی هست که باید به رئیس جمهور آمریکا نه گفت
نتانیاهو:
🔹
آنها به من گفتند که وارد رفح نشو،  می‌دانی چرا این را گفتند؟ چون رئیس جمهور ایالات متحده گفته است که دیگر سلاح نمی‌فرستد؛ گفتم من برای او خیلی احترام قائلم، او در ابتدای جنگ در کنار ما ایستاده است، اما چاره‌ای نداریم ما وارد می‌شویم و اگر لازم باشد، با دستان خالی می‌جنگیم.
🔹
موقعیتی وجود دارد که باید حتی به رئیس جمهور ایالات متحده آمریکا نه گفت.
#Demon
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/662999" target="_blank">📅 21:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662998">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔹
نیویورک تایمز: داماد ترامپ به جمع میلیاردرها پیوست
🔹
منبع اصلی این ثروت افسانه‌ای، همانطور که در گزارش فوربس آمده، شرکت سرمایه‌گذاری "افینیتی پارتنرز" (Affinity Partners) است که کوشنر در ژانویه ۲۰۲۱، یعنی درست پس از پایان دوره اول ریاست جمهوری ترامپ، تأسیس کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/662998" target="_blank">📅 21:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662997">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔹
ادعای وزیر امور خارجه آمریکا: مذاکرات فنی ایران و آمریکا هفته آینده از سر گرفته می‌شود
🔹
مارکو روبیو در فرودگاه کویت اعلام کرد که گفتگوهای فنی بین ایالات متحده آمریکا و ایران در روزهای ۲۹ یا ۳۰ ژوئن (۸ یا ۹ تیر) در سوئیس از سر گرفته خواهد شد.
🔹
فکر می‌کنم آنها دوباره به سوئیس خواهند رفت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/662997" target="_blank">📅 21:36 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662996">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SNSeny98OvWg462jyXuIzQzJZlLu0bVlgDGvq5iPwg8W8kOF7Fm9-jW-o-BlC1HxNds46yZemON_TeQWWnjlD7ymWCITQ46xPTM3tTSFEzRe29eObBG0FJpe84f4iqLvU8pIam-ZT2mqdk-Genxxlw38Jhqk8Y1VM3TBa-Kis8nJxGUuTBHY_j8dikEAwk1IXY_gc6kvbSLxPVq38jHSMbIq0ZZUxL_iZU4QEp-aDOKCCzHiADdYzlzeat9k4UicH_jCjRM48L4EZRXwfk1XbwFEK1IB8i3oZ_T4Qs6Icoj3C_chn1W-R-3ghuKHLZvDWUKk_YH_gvmICHiYZEOixA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
راهنمای دریافت ارز اربعین
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/662996" target="_blank">📅 21:28 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662995">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔹
معطلی دوباره برای طارمی و الهویی در فرودگاه و معطلی تیم ملی
🔹
در حالی که تیم ملی ایران برای سومین بار در حال سفر به آمریکاست، بار دیگر مزاحمت آمریکا برای تیم ایران باعث معطلی تیم در فرودگاه شده است.
🔹
اعضای تیم ملی فوتبال ایران ساعتی قبل برای انجام دیدار برابر مصر راهی فرودگاه شدند اما همچون دفعات قبل، مزاحمت آمریکا به عنوان میزبان برای سعید الهویی و مهدی طارمی، باعث معطلی تیم ملی در فرودگاه شده است.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/662995" target="_blank">📅 21:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662994">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔹
ادعای وزیر انرژی آمریکا: بازگشت جریان نفت به حالت عادی به دلیل مین‌های ایران به تأخیر افتاده
وزیر انرژی آمریکا:
🔹
ایالات متحده حتی بدون توافق با ایران، جریان نفت از طریق تنگه هرمز را تضمین خواهد کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/662994" target="_blank">📅 21:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662993">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔹
تهدید مجدد نتانیاهو علیه لبنان
🔹
نخست‌وزیر اسرائیل با وجود اعلام آتش‌بس، بار دیگر لبنان را تهدید کرد.
🔹
بنیامین نتانیاهو در ادامه کارشکنی در توافق آتش‌بس گفت که هنوز کارهایی هست که باید در لبنان انجام دهیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/662993" target="_blank">📅 21:15 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662992">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67f5ea33f1.mp4?token=QpUONw8Vs_d7XNXdrEPT5pIy59GJ4L_iJ2bRBTMVAf59qscaOPPzcXn2aWl9b99SbkdDIfncWmr5gX4loRZsU3vWjwgOWNdnEijQGqiLX8mb7TOhjohka-WE7YRAbho50FU6b_BwcP08gvInMmYIQmjeVWS4M63ouP566KV26C1l6m5f7PNCs7NP81RZppilcVMG9fo0ul3_ddYhWSyY9WUMQ378IpzdcWOgLslhPhVgUCXxZx9uFNH-CydrJLz2Xipx9np8Bp9Fu4bU1lGh2GkN2FVe3IL16xUtR1oz0ov4qAZKpoiw5_ciIgtFDaKLdAEm-5iDj8jZ2f7g0Hs2dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67f5ea33f1.mp4?token=QpUONw8Vs_d7XNXdrEPT5pIy59GJ4L_iJ2bRBTMVAf59qscaOPPzcXn2aWl9b99SbkdDIfncWmr5gX4loRZsU3vWjwgOWNdnEijQGqiLX8mb7TOhjohka-WE7YRAbho50FU6b_BwcP08gvInMmYIQmjeVWS4M63ouP566KV26C1l6m5f7PNCs7NP81RZppilcVMG9fo0ul3_ddYhWSyY9WUMQ378IpzdcWOgLslhPhVgUCXxZx9uFNH-CydrJLz2Xipx9np8Bp9Fu4bU1lGh2GkN2FVe3IL16xUtR1oz0ov4qAZKpoiw5_ciIgtFDaKLdAEm-5iDj8jZ2f7g0Hs2dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
ترامپ: خواهیم دید چه می‌شود
ادعای رئیس جمهور آمریکا:
🔹
تهران امتیازات بسیار بزرگی می‌دهد.
🔹
خواهیم دید چه اتفاقی می‌افتد، فعلا که اوضاع بسیار خوب پیش می رود. در حال برنده شدن هستیم.
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/662992" target="_blank">📅 21:13 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662991">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ed368d3d0.mp4?token=kSLLRBkl_G69eDxT489VqoQ6ETOiwRyP73Zvmk0J76mZJeETh-BxG0wmMKNYZwJJSBFMwfXDna3D80tHGOS9yoqEMzgdx7O0JGcJArBjIjxKwXr8PI7DEcnBXRjIrMfCEyjs6AExuMghwlzYk4U2W7kvBCgM5ZpIehxcGiUvK0ynor9WSk9JkXv_seNypRotUcWjSixjo2E7uH9Wq8Q7ZFWf7QID2IrSUKtqyC8sIRrTUyNjgHOWFIxNbeNVD-scSFpC5J3hre102xX4X18eHc-VuDSd4UJLqbgZg-jfl2S4ql6fSaO_RJVWe4wN_Fs_qQ1TcVlxjc72N6GkdRkZdx4--h4FwDvG56VYcwULU8QvzQ_aliJkwGiU8Fk6qw2gRrIMsybRvAAEvBQlvUjc1PCeYbIbIc8vMgZI7Kahhe6kdcZFmz8MWoJ3-4Mu7qujcqbnw7C59KS1oQk8KV3l6AgfwflL_ljMEsDjInfsYuJOQluI6EWW4YctHyEo-agKO-zqRILSQEOXrWSP7_N2KeaGB_FBW3kbs0arTiN2o3ZKCqUHWCxkSu0vq4LjLyaxHWi_WWyGOPopCkrqfW7eMaRrDUQ2vHOBO5wUrtR4iwem56GN9AuLHXo9oYKrmGBL8y5ea-YvcTgXhGxB3AOZOlUNgslOINGGM9NZqnyTU2U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ed368d3d0.mp4?token=kSLLRBkl_G69eDxT489VqoQ6ETOiwRyP73Zvmk0J76mZJeETh-BxG0wmMKNYZwJJSBFMwfXDna3D80tHGOS9yoqEMzgdx7O0JGcJArBjIjxKwXr8PI7DEcnBXRjIrMfCEyjs6AExuMghwlzYk4U2W7kvBCgM5ZpIehxcGiUvK0ynor9WSk9JkXv_seNypRotUcWjSixjo2E7uH9Wq8Q7ZFWf7QID2IrSUKtqyC8sIRrTUyNjgHOWFIxNbeNVD-scSFpC5J3hre102xX4X18eHc-VuDSd4UJLqbgZg-jfl2S4ql6fSaO_RJVWe4wN_Fs_qQ1TcVlxjc72N6GkdRkZdx4--h4FwDvG56VYcwULU8QvzQ_aliJkwGiU8Fk6qw2gRrIMsybRvAAEvBQlvUjc1PCeYbIbIc8vMgZI7Kahhe6kdcZFmz8MWoJ3-4Mu7qujcqbnw7C59KS1oQk8KV3l6AgfwflL_ljMEsDjInfsYuJOQluI6EWW4YctHyEo-agKO-zqRILSQEOXrWSP7_N2KeaGB_FBW3kbs0arTiN2o3ZKCqUHWCxkSu0vq4LjLyaxHWi_WWyGOPopCkrqfW7eMaRrDUQ2vHOBO5wUrtR4iwem56GN9AuLHXo9oYKrmGBL8y5ea-YvcTgXhGxB3AOZOlUNgslOINGGM9NZqnyTU2U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
اسکات بسنت، وزیر خزانه‌داری آمریکا: توافق با ایران بخشی از راهبرد تقویت دلار است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/662991" target="_blank">📅 21:08 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662990">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d89dbbaa3c.mp4?token=ey5E0f2sAOt6MF9RBKq7DNuG3bIHE5MRig-sKn-9r2MN6Z9h_CX3-C7mBeoo_Iy4jsIhvXgDt3gozVVkFvkfJuscP5iF_0Gj1JSJfAgLzPJGbVhYtFK4byHHP1066rwWnFI0faVrKgd91jlOUy3Qdg8ctUiodNQg94sWsv5K1sHZP9Se2HSmdq674Koq_IylKSFM10GQd2aHOrLyze6tb70hdxLJrSw0dcFbULL09vnJG1OHhd_NBosxjNyuJaRk9HxJ9sL-ZfE8q8iC88gzDlf0m85FNZll-7yYcVJ0OJeQlAFlafysm_W9rZD_0VGLMoxuHWeWv6oQ7ceHXWNCow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d89dbbaa3c.mp4?token=ey5E0f2sAOt6MF9RBKq7DNuG3bIHE5MRig-sKn-9r2MN6Z9h_CX3-C7mBeoo_Iy4jsIhvXgDt3gozVVkFvkfJuscP5iF_0Gj1JSJfAgLzPJGbVhYtFK4byHHP1066rwWnFI0faVrKgd91jlOUy3Qdg8ctUiodNQg94sWsv5K1sHZP9Se2HSmdq674Koq_IylKSFM10GQd2aHOrLyze6tb70hdxLJrSw0dcFbULL09vnJG1OHhd_NBosxjNyuJaRk9HxJ9sL-ZfE8q8iC88gzDlf0m85FNZll-7yYcVJ0OJeQlAFlafysm_W9rZD_0VGLMoxuHWeWv6oQ7ceHXWNCow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
پنجره‌ای به آخرین حضور رهبر شهید انقلاب در مراسم شب عاشورای حسینیه امام خمینی(ره)
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/662990" target="_blank">📅 21:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662989">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔹
وزیر انرژی آمریکا: ۷۲ کشتی در روز گذشته تنگه هرمز را ترک کردند
وزیر انرژی آمریکا:
🔹
در مجموع حدود ۲۰ میلیون بشکه نفت حمل می‌کردند.
🔹
بازگشت جریان‌های نفت به حالت عادی به دلیل مین‌هایی که ایران در تنگه هرمز کاشته بود، به تأخیر افتاد.
🔹
ایالات متحده جریان نفت از طریق تنگه هرمز را حتی بدون توافق با ایران تضمین خواهد کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/662989" target="_blank">📅 20:56 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662988">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔹
پایان دور اول مذاکرات اسرائیل و لبنان در واشنگتن بدون نتیجه
🔹
نخستین روز از مذاکرات مستقیم میان نمایندگان اسرائیل و لبنان که با میانجی‌گری آمریکا در واشنگتن برگزار شد، بدون هیچ پیشرفتی به پایان رسید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/662988" target="_blank">📅 20:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662982">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bda6a59f3.mp4?token=aWqfzmN6O6b9a7VGRDTJMfDEpfTMEhi6HyID-s0SIctA4hUtl6hU57FZaPGoWrWNkIFBHmQBhPcnoqXdeA1sM5L9N0gxpD4BA_hJVNM5vZq4l2rdLlyAJ7Wz-OLsv-NE3O-xjveYBZ3sjl3tLRv3Q7bf9iL39K46igI5AzMFfC9u38vYgTEGUN0tKr-yS_m2XQ6TJLjMkaY-AIuxe9hLCVIiqn5D_qLe7F-SNDRdisGP7XRh_9sWqLYeWVPY91gtA0ZZi51e-TJkLWUw-UXCtSaD1XtXOyHY3jbHoGEB5H28XaU-fu1zVFWew6ESRp7od1br0t1h10TApgIiIzjVLUa1SLtNYltCxP7u8p9VsCEPenqYYFT0xuFcLJmWi-p53ebtc4krXVpm0uGYregSko9Dun5FwFq8sk1dGCHXPN3qnupLIxoEkkdwNh8FKycnU5QO4oLVsGRV045q5zUVh0fkDIE4RPQKyon7inFjYDoRMSB4OrK68uHry4dmG7QaiKb0pMa9ElwqAiHEJs1R7zPTCoxkag-AzTQRTucSEc3UWzeEGoYrTkoTWL3Rlwl8dji5YbfLyCxd-bK8SP4cii1mc-OH4812g7jQDogQYerWZTFJqkaKAnSiVNM8kfC7v1BHq2kPH_S46BGWFxmn27CNFep7f1RQTunrn6IPUHs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bda6a59f3.mp4?token=aWqfzmN6O6b9a7VGRDTJMfDEpfTMEhi6HyID-s0SIctA4hUtl6hU57FZaPGoWrWNkIFBHmQBhPcnoqXdeA1sM5L9N0gxpD4BA_hJVNM5vZq4l2rdLlyAJ7Wz-OLsv-NE3O-xjveYBZ3sjl3tLRv3Q7bf9iL39K46igI5AzMFfC9u38vYgTEGUN0tKr-yS_m2XQ6TJLjMkaY-AIuxe9hLCVIiqn5D_qLe7F-SNDRdisGP7XRh_9sWqLYeWVPY91gtA0ZZi51e-TJkLWUw-UXCtSaD1XtXOyHY3jbHoGEB5H28XaU-fu1zVFWew6ESRp7od1br0t1h10TApgIiIzjVLUa1SLtNYltCxP7u8p9VsCEPenqYYFT0xuFcLJmWi-p53ebtc4krXVpm0uGYregSko9Dun5FwFq8sk1dGCHXPN3qnupLIxoEkkdwNh8FKycnU5QO4oLVsGRV045q5zUVh0fkDIE4RPQKyon7inFjYDoRMSB4OrK68uHry4dmG7QaiKb0pMa9ElwqAiHEJs1R7zPTCoxkag-AzTQRTucSEc3UWzeEGoYrTkoTWL3Rlwl8dji5YbfLyCxd-bK8SP4cii1mc-OH4812g7jQDogQYerWZTFJqkaKAnSiVNM8kfC7v1BHq2kPH_S46BGWFxmn27CNFep7f1RQTunrn6IPUHs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖤
پک
#استوری
کلیپ های عاشورای حسینی و شهادت امام حسین (ع)
🥀
امشبی را شه دین در حرمش مهمان است
مکن ای صبح طلوع مکن ای صبح طلوع
محتوای مذهبی ویژه محرم در این کانال
👇🏻
👇🏻
@Heyate_gharar</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/662982" target="_blank">📅 20:50 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662981">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lxB9i4TZemqOKpJE9KnfA7lgdOD7y4GpAiYaI453k0pBViDnOZk-Pzv2g78-kl217JAifg6MVA5yBJ66LlDKwzY8-JS5XweAOzjmUKy_MXBZyrvsmpeDHEs8cM99wKNcWZfsDaN_6uUWLLtT_9wwWZMOBO2kef_yVC3dQr6QvsISsf8HvZswbqnOIiLiENu9XFd6o2CWsLelNvT0oWI7flE81hWZYTK1jlwJO4lhM3D8USMAGB1sj3GhiX47N0gHQpBpznItfMjaBpuVfnVxCXOy_8KZykFfOEIWKSFXFktFonjIfKyNrWSuxY1X2CgVSYbOG3ZvYCuDKlqsOAhQWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
غرب به دنبال جنگ با همه است، و با کسی جز اسرائیل کنار نمی‌آید
آلوهن میزراهی:
🔹
روسیه به دنبال جنگ با غرب نیست.
🔹
چین به دنبال جنگ با غرب نیست.
🔹
اسلام به دنبال جنگ با غرب نیست.
🔹
عرب‌ها به دنبال جنگ با غرب نیستند.
🔹
آفریقا به دنبال جنگ با غرب نیست.
آمریکای لاتین‌زبان به دنبال جنگ با غرب نیست و همه آن‌ها با یکدیگر به طور معقولی کنار می‌آیند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/akhbarefori/662981" target="_blank">📅 20:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662980">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa00589e23.mp4?token=VfkJSLK8XG4FcvKgp3F5N9ykQ9siFCZt_ZUk-hf3wexCmU8_hLanEiVpv8mx6es0H1kEtTR-KIAaIsFgnEyJ3zYkKEZZpEjbxqm2F1-o4iIWYTEOTZfICme-7VqmeUlLNDML_xzYS-lxa_V0WUfJmpqklJrItHdcMaj4hloO_c-Yp7n51Itw22Qy160CKOAKeI7AJvuT4w-47eYcDcE3sE-JLPji_5OEW9qstoRjKKyRcYHkBBhNdGVHvvG2OFb1Q3KrrWe_adrWIlUATB0lokBRlURU9rDpFFIYO3KmpoT_k3A5dWGehF8CE51T87zCQ2nUizKRCJs3dMxFm5wTl64gYobQ4JM-yiyppBYdDYMsvIZ2n5dV6huG1QeYlf3JyskLSschT8P-hRYGreBqB8wAQxY-LfN7iXMj9-E82NTWeTfYebtaPRU7nPeSA0X3Wk88DeO2dfCoTe8ZFLLGHVxTKCJVKqCsym3Vv9Rye1XdooQnk8_0--D3KkH5q28dKV43tPIbTNpOHKQXyUHzwAGsfrhFmDbxNJLkajSE7zb1P-o32Fn3cxml7gfKwEfl-q7OeNp6dtZfEfXk_lRS3BhlYsBYwOx8h7wa3FyCR0wqQ7vh_WEyJHL5P5G_2USMMXzpXf1lxp9u-AylWT6yctIIQid5zrgQVb1o0WKmgUk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa00589e23.mp4?token=VfkJSLK8XG4FcvKgp3F5N9ykQ9siFCZt_ZUk-hf3wexCmU8_hLanEiVpv8mx6es0H1kEtTR-KIAaIsFgnEyJ3zYkKEZZpEjbxqm2F1-o4iIWYTEOTZfICme-7VqmeUlLNDML_xzYS-lxa_V0WUfJmpqklJrItHdcMaj4hloO_c-Yp7n51Itw22Qy160CKOAKeI7AJvuT4w-47eYcDcE3sE-JLPji_5OEW9qstoRjKKyRcYHkBBhNdGVHvvG2OFb1Q3KrrWe_adrWIlUATB0lokBRlURU9rDpFFIYO3KmpoT_k3A5dWGehF8CE51T87zCQ2nUizKRCJs3dMxFm5wTl64gYobQ4JM-yiyppBYdDYMsvIZ2n5dV6huG1QeYlf3JyskLSschT8P-hRYGreBqB8wAQxY-LfN7iXMj9-E82NTWeTfYebtaPRU7nPeSA0X3Wk88DeO2dfCoTe8ZFLLGHVxTKCJVKqCsym3Vv9Rye1XdooQnk8_0--D3KkH5q28dKV43tPIbTNpOHKQXyUHzwAGsfrhFmDbxNJLkajSE7zb1P-o32Fn3cxml7gfKwEfl-q7OeNp6dtZfEfXk_lRS3BhlYsBYwOx8h7wa3FyCR0wqQ7vh_WEyJHL5P5G_2USMMXzpXf1lxp9u-AylWT6yctIIQid5zrgQVb1o0WKmgUk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
شگفتی رسانه‌ های دنیا از قدرت تسلیحاتی و فناوری نظامی ایران
شبکه قطری العربی:
🔹
ایران با استقاده از برترین تکنولوژی و فناوری، جنگنده F-15 آمریکایی را ساقط کرده؛ این شبیه فیلم‌ های علمی‌، تخیلی و موجودات فضایی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/662980" target="_blank">📅 20:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662979">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
رازهای برزخ از زبان یک بازگشته از مرگ؛ دیدار با اهل‌بیت و سرنوشت برخی مدعیان ایمان
🔹
00:08:40 ماجرای خمس و زکاتی که پدرم به نیت امام زمان(عج) پرداخت می‌کرد
🔹
00:17:00 اهمیت نماز اول وقت و اعمال نیک
🔹
00:23:10 زیارت حرم امام رضا و کربلا توسط روح در کسری از ثانیه
🔹
00:34:35 درخواست انسان‌های حیوان‌نما از امام زمان(عج)
🔹
00:40:20 وضعیت شیعیان گناهکار در عالم برزخ
🔹
00:59:30 نذری دادن به نیت ظهور
🔹
01:03:00 اعمالی که با نیت خدایی انجام می‌شود
🔹
01:20:10 ترسناک‌ترین لحظه در زندگی
🔹
قسمت بیستم (نذر)، فصل چهارم
🔹
#تجربه‌گر
: محمدحسن حکیمیان
#زندگی_پس_از_زندگی
#فصل_چهارم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/akhbarefori/662979" target="_blank">📅 20:33 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662978">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e95ef43275.mp4?token=Li4rNVl8xzz6z_ubfEM6-lz3qfkWoMzz6zHw9rY9Qezg2PVXMcuMwR4DWuh27_yPo_eCxycpsv5Bbe2p7hZjbnB4J-OU0S081PiPcVistV-XJPTvekuEPy0J0PllAWRQoQfF17wRX06Uux887AxlBlfh1HDL1UtOENOER0-oxCx47DYmgseFfgY0-2wQiC7MUn9smB3Pv7r4RnmdsuhOlsuP0ykM1YygIK6z4rFuB1pY7uZMaSgWYHLKJ7LH-rt02BikAz20Igu-xc98s1IsBr8X8eC2XdjXw8Tz_h56_v8XeDgeR5gZYK7OTNnolmdraJzi2HfC60z-wAAvEvQA_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e95ef43275.mp4?token=Li4rNVl8xzz6z_ubfEM6-lz3qfkWoMzz6zHw9rY9Qezg2PVXMcuMwR4DWuh27_yPo_eCxycpsv5Bbe2p7hZjbnB4J-OU0S081PiPcVistV-XJPTvekuEPy0J0PllAWRQoQfF17wRX06Uux887AxlBlfh1HDL1UtOENOER0-oxCx47DYmgseFfgY0-2wQiC7MUn9smB3Pv7r4RnmdsuhOlsuP0ykM1YygIK6z4rFuB1pY7uZMaSgWYHLKJ7LH-rt02BikAz20Igu-xc98s1IsBr8X8eC2XdjXw8Tz_h56_v8XeDgeR5gZYK7OTNnolmdraJzi2HfC60z-wAAvEvQA_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
وزیر خارجهٔ آمریکا: اسرائیلی‌ها با تفاهم ما با ایران مخالف نیستند  خبرنگار:
🔹
آیا شما هم مثل برخی از بخش‌های نهادهای اطلاعاتی آمریکا معتقدید که اسرائیل به دنبال تضعیف یادداشت تفاهم فعلی است؟
🔹
روبیو: من نمی‌دانم از کدام ارزیابی اطلاعاتی صحبت می‌کنید؟
🔹
خبرنگار:…</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/662978" target="_blank">📅 20:28 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662977">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UMoHwM1xzvfSYqSOOVA4U28cqwSRdHodQ7wY4y1Ze-mHjtEoONhiaoYMq8LFtNL6xu6odzz1VNcg0SFccV_5DyHGWhMReJY7RZfOoqslte623iKxWcmqYj_Mx_MCBJ_NtQywVrl0zvnDMga8p8CtqUg4NW2mD5e1pu4_X4nrN9eky8v8NS8_5HWRSLpwlx04PXaXSr-n6ZQ_AJn4A0zxn4y7Px4pJdqNqDfG6nUE6w-8YhxqUJCjX9N4Bs5rjIG0K1JVbI1Fz8SCiBC-iCDCzTx_wb57kOQ6wIbHJLc7eKO-LjuGdLT-OY5GhHesqRsjths5R2fCpoNGyD0etAaMxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
سخنگوی وزارت خارجه: صلح واقعی در منطقه غرب آسیا تنها با پایان مداخلات آمریکا و خاتمه اشغالگری محقق می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/662977" target="_blank">📅 20:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662970">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KCuic0uhDvrD9Ve41dW1se2YQ9SjEGEPAA_Z-Ad1CFzh42Vu6pW9Ei_25fXB1X4_DP0PhzJbZ4KYhrIEj1ENYadGT_GQf5WLgFo1pnBWLXzZ1QjFqpSxtLL9nAiE8aPFbOZBMllZwu8I7G1RSvtvEgS_VGzQjjTGTm6GDDiIHW0oJjWhmSIXcJvQc9XeoPB7w7naWFTrnS7_uoAIARIKp70LynzCF2Z9VadwQM5C_f6Fg3hRqVwU-yF_AILgOjwv4JVBIdNb3tOlJwezyXG4FmMbRtjcrgBAg6rGL9ffiMxWPdaT3iXtCRulOWQImZQRbAkfL0RG0N1O5B2SaDqVZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MoRZLqrMmOtl4DeCMuYRLUWGyM523IHKXCHw1g3zf2Kx_ic97KQ4poN_OEXjczRD5dYBU2Xk2makHfCgizA-TjHF8K4JQkvdnVqfG0vJVY8Avl5RTBOLhl3dsO6RKrYVtyq0vvFSI9D0HMxN2lCh__tfKO5HCTCcyYRAbKQ5kSIUHzPcO_grA4rNoZF4tWlGExtgWIc_VwnIpfaOIKDy-NLn_Y_eQmNWeVUdh6nFC_PCBwb3OxgvExXJhOCWmPnRqJiByeBXozDl6OemJJuFUKZHNCxa62L8oqQhlzJatEhmkR7P-Ik18E6Av7j9awjdfQOfVSvYCQuNQ-xYFY_ZcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iWKYd6UuxFTFfweEI4sLWNyjDN2T5rsky9HBULLnurKTcrgkC8PZQLLESnPPCfuamhuJKvwA6XY7mBjxsGAOlQCxxTdDr7GiSaAvhFlzdTRZpwE_JxqqmCgAU9NtU0UFNho85nNCaSjS9_r-yukMCk47pAjDJIeMrIKBsZWuLtbwS0F4pmrLRlDJYhrIdmo2A51ZAbMpYa6FGlqhp1BglJEaUg3PiDhHYC4we07F2IVIvnyTdLRKAkl0dTMZIE5kSYsodjWS9r25VwLfSt271--SwFL3TbSHQc7KmPnO8w2eiK_tfgf-IUD9NYh71rEUAHFi6UbZuP208XVQtMDvFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FdO2gptj2sNsv9m7SlY3rPqWI2lSpLvo2c-Y2mCsvMZ6WaDBWP1tmye7TsoKUo_xZ5ViAwJFAHI_jBxJvVC63QWnD1eB_e9ilwXy9hrgnoEOrigoVcIGKx7WlKmRPWlt9goYRexg-qqbQYGG9yd2mSOX0HQiaOPLp_ffJpyOy5bIOWDg93rXZoDFOnELXUIHoZD-dL1YubVgBzqb3BsG1gKZPlWvqhuOdlFdxyehxKKrzz_Ktk7kyNyLPstfWH8JBcJ4yK5m9wt8Xr2zIBpXcRxxCIwJD4_JGMwOgEdA4KP0b4EhJOc8jsCywQsTp25q-BZSIdTutdAIiHeMAnVlPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gXgLAkigTqnx01w-7s90IIXYPHHBW51Rgk3gC__RUNepD-Bfe_dsg3MGmsXQ-HOURMj6RAw8SY4VkIonx8dOp5uHosZOvcLSExNbkvR3h3IuL9B7q80oz3QUVUKgG9CIAWlK-DdASjXawN5XxAZlRNpBx5JiY-XGnYRHHPw-QuIOWA9w4VFhkT2ZODbHgMXObv3VcAVnNvzmj3KN4mUJ9eFal2PjhIyxkCtZI90dsJgYFEUhq5-MiarULHfuK5fN1KyIuybbq31qKrru0wDqNrEJ_af9jq1f_3ShWjUK-YE4CAFVOTLo_MRiE-6CVpRnCCEl0F68PDAvUh6ry1Pb0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZXsNpV-cMqkx-V42TWi_UGmyjNEuSco3AFj-jiXppmr4DtJrb73RIlMbYHGomh8sRaHJtSDhn5HTQongM9i8XaRgNIIs3izzn_XS8jaRgqYpm3mC2CP1b9zgP2PzaBPeyBuJzt_Z4-dCnSh8YU_ucnOMj8traiI7DZSb_sn-Ez3-mACva00ztf4N5kFZyk00jfwhP4glPts0CIMVx1t0N1sGQLiUSdI_QlRKuKJH6MMxkgyTo3jYp4jZ5zuLsW0Qab3ckfoxr-0mzdvCnnrupC3Fey59ZUZPnDY_PBDPePFjEnIRAIVgx6XMfrgOnlP2GLHxN5ngCHJpAWGLeVCDow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZzzMA-bXh1bzUCNLfHIA4rcU0CWIstKGHmttnOMF_A9F2oRaq7N1JMDuLCIqPDBXutWTOswzWYvkwPd4lwW4_togL_Ufr8PW7xbpspzyE6EIZKX3qORbrL7C6a7RbtIXqOnkA79osKwTzHZRL7ht9l-EGI3RgoN-v7E0OrFE4s6iCkWGyXahTSMP_nydOspz8zIuXMPR4RI0R9T4fKH9-zUtemI1bDh5DW8ro0JQXbhR0U36m6mR3FGuXVy6LFens9gZV-_JawPyvG-x9Bk9IW6DqK6W1i_mkBEaLOUzO3dmyXvT_BW3jy5GfD8lg_IadFt21xr8xcMwYJD5Ke1J2w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
نشان حسینی
🔹
قاب‌های ثبت‌شده توسط شما مخاطبان خبرفوری از کوچه‌ها و خانه‌هایی که در سوگ اباعبدالله الحسین (ع) جامه سیاه بر تن کرده‌اند.
🔸
تصاویر خود را با ما به اشتراک بگذارید
👇
#ایران_حسینی
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/662970" target="_blank">📅 20:19 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662969">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45d8ecba5a.mp4?token=NEAANLNLsa6CIfVSetXvdUYhavQWvbdhqdhmjC_EUGw3P4ZuJJy4Bi-RI-k9t468FZTqn4EuxAGANu0l5_ocX4nY7quA42bRTZzLLqAGTqfAunzZnWiEdXlm_9txPhIPq8XZNw722SY-wUncPWPkJBOZk8skj7WLIc8uvmihSSMAf3lctbL8ANkDYLcf7A7xTD8xRwy64YZ_Flm0CPGUtO6lzJyceD7dhSSv0vjZUKkDRYqkp3rHMdVrKAOYIiZCQwxdfhyQDT8M4WDeb9NeQ6pkOH5YUjDA4kx0bFuEpbakm1O7xLxSfQ9JSrRhBApvnXUeWol6VDHjehuVAW24bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45d8ecba5a.mp4?token=NEAANLNLsa6CIfVSetXvdUYhavQWvbdhqdhmjC_EUGw3P4ZuJJy4Bi-RI-k9t468FZTqn4EuxAGANu0l5_ocX4nY7quA42bRTZzLLqAGTqfAunzZnWiEdXlm_9txPhIPq8XZNw722SY-wUncPWPkJBOZk8skj7WLIc8uvmihSSMAf3lctbL8ANkDYLcf7A7xTD8xRwy64YZ_Flm0CPGUtO6lzJyceD7dhSSv0vjZUKkDRYqkp3rHMdVrKAOYIiZCQwxdfhyQDT8M4WDeb9NeQ6pkOH5YUjDA4kx0bFuEpbakm1O7xLxSfQ9JSrRhBApvnXUeWol6VDHjehuVAW24bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
وزیر خارجهٔ آمریکا: تمام دنیا با هر سازوکاری که برای استفاده از یک آبراه بین‌المللی یعنی تنگهٔ هرمز هزینه دریافت کند، مخالفت خواهد کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/662969" target="_blank">📅 20:10 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662968">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔹
آلمان پروژه ساخت ناو جنگی را لغو کرد
‌
فرانس پرس:
🔹
وزارت دفاع آلمان اعلام کرد به دلیل تاخیرهای طولانی، افزایش شدید هزینه ها و مشکلات مربوط به قرارداد، بزرگترین پروژه ساخت ناو جنگی خود از جنگ جهانی دوم تاکنون را لغو کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/662968" target="_blank">📅 20:06 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662967">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MzpTTuV1_Yn4oj23bzELp3AazevmMmcNtqVPNiUdbWk2QN7GZ1cpi9T8_d0VtkEF9sFAeK2uzRzJxUqntbGvN85NUWwZQZSy4p_qkkGD2LQ6ZuNA-2VHwc-nG9bPJ9a0Lj0QZ99wFHSpuHII8fq3aHhF6L5-wO3ZYTahG7Ze9Nfrb--nhW_8IshuUK0MthZ82G7AJ9klhGS6aoMeDjXBECExXwIifJ4p2qB1o_evCDunVaapxHCbRdGRpdErH1I0ecaDGU0HxPdiqCUw9d3GZURZJwYPNzoTcspbU_999oUyTLhOiAEN0R_I6jXwATH9lM2j1X9Ies9Ku8mIfmvq7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
تانکر ترکرز: ایران از تاریخ ۱۵ ژوئن ۲۰۲۶ تاکنون ۴۰ میلیون بشکه نفت خام صادر کرده است
🔹
دقیقاً نیمی از این مقدار در یک روز واحد صادر شده است؛ آن روز جمعه گذشته، ۱۹ ژوئن ۲۰۲۶ بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/662967" target="_blank">📅 20:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662966">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53461dc2d1.mp4?token=QgB3LWpzKMRsAzXKANr0sw-bIryKvImhXr3zXXPzo7-jcJS_AtDEbBUhLER0-RjdUYygp67_Uzqzg-F-y_dJdfDfMvyNZtKaLzla39znv6WE53kWtA67D4at6S7YYuWALTQDxhnfp4zZVmnEblcaMrkPgH8GWkGqxiWodRX9STR5oWd3KJ5NCTSmz50o_M_aJqZGtR3MvIMiKaGocmymBxUXOSAq0S64aaHqnalCCgQKbgnl0zh0LRJMT6yifhTP-IvOcvwGSAS1EG6FzOGQk5GCrH2BHJTNNfN6ICVLsHz-Rx8zOWxS1I2xyr4_uCRgd-RdpPgHBt883RsBj0wbDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53461dc2d1.mp4?token=QgB3LWpzKMRsAzXKANr0sw-bIryKvImhXr3zXXPzo7-jcJS_AtDEbBUhLER0-RjdUYygp67_Uzqzg-F-y_dJdfDfMvyNZtKaLzla39znv6WE53kWtA67D4at6S7YYuWALTQDxhnfp4zZVmnEblcaMrkPgH8GWkGqxiWodRX9STR5oWd3KJ5NCTSmz50o_M_aJqZGtR3MvIMiKaGocmymBxUXOSAq0S64aaHqnalCCgQKbgnl0zh0LRJMT6yifhTP-IvOcvwGSAS1EG6FzOGQk5GCrH2BHJTNNfN6ICVLsHz-Rx8zOWxS1I2xyr4_uCRgd-RdpPgHBt883RsBj0wbDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
ادعای نتانیاهو: تا زمانی که من نخست‌وزیر هستم، منطقه امنیتی در جنوب لبنان را حفظ خواهیم کرد
#Demon
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/662966" target="_blank">📅 20:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662965">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9928199fd8.mp4?token=j1Y3LubUTzxmpB_jjDVNhTUr3sPZSfpAujjR2PQTTJo8FqT0kW9G3zVvPrba0kWGCxCZSrFb2QaZ5QeNUS4C-91O4hH0LitvqBu29Y0Kg8WoORYeEYKbB9-j48dZqljTtMXZq6mWOqsnHDJqoHXSFIpK8EUaoUx6MaZQXJTkaaOTY8YRWuIfL-hn286MaRtcMSjwHzWoJSZt_qgaFjc56nvJKZxF4ACADOeeKUEbujuCAygCcvrrSiwHq_slKRW03iRux6m3grlp3O339YKsKHuwb4h-UYcLn_Mkgmwytxc2xQwvAUQTKZ_vcWrHCD76Va_NY0zZ5FG0ALPzNTELvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9928199fd8.mp4?token=j1Y3LubUTzxmpB_jjDVNhTUr3sPZSfpAujjR2PQTTJo8FqT0kW9G3zVvPrba0kWGCxCZSrFb2QaZ5QeNUS4C-91O4hH0LitvqBu29Y0Kg8WoORYeEYKbB9-j48dZqljTtMXZq6mWOqsnHDJqoHXSFIpK8EUaoUx6MaZQXJTkaaOTY8YRWuIfL-hn286MaRtcMSjwHzWoJSZt_qgaFjc56nvJKZxF4ACADOeeKUEbujuCAygCcvrrSiwHq_slKRW03iRux6m3grlp3O339YKsKHuwb4h-UYcLn_Mkgmwytxc2xQwvAUQTKZ_vcWrHCD76Va_NY0zZ5FG0ALPzNTELvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
ادعای روبیو: کشورهای عرب خلیج‌فارس را در جریان مذاکرات با ایران قرار می‌دهیم  مارکو روبیو، وزیر خارجه دولت تروریستی آمریکا:
🔹
روابط مستحکمی با کشورهای عرب خلیج فارس داریم و از حمایت آنها سپاسگزاریم .
🔹
آنها را در جریان همه موارد مربوط به مذاکرات با یران قرار…</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/662965" target="_blank">📅 19:58 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662964">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔹
روبیو: یادداشت تفاهم با ایران ظرف ۶۰ روز اجرا خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/662964" target="_blank">📅 19:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662963">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔹
ادعای
سربازان آمریکایی: پنتاگون شدت تلفات جنگ با ایران را پنهان کرده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/662963" target="_blank">📅 19:51 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662961">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F31mYvbTwOwEjji_cxGIL-gdsiHgZMe6xCDIPQHvdP6hRd8Tp5EJUC7LoH8YpdzhARXHmHEUVJkbbXYV3mRYo0CRRv63pPc_2psKb6pJx6P14eybqMLw2M1iGmmIxbahUP33BivU20-9E4vDxCdkvp7-7IAQXEQap6Ff-t6emVNEQbqCYkkmlUovlToh2oKhh0xWTkpiDbga7peQ9B-P_O58IwgOEAe9QDE5J6G70bvSNiAgmn8Dieh_7KHfTMS9JzGiXhu2F7h5ugsBDZq4Zbw_cWWTYgo65QPRyYcBS_ugimTeYHgZbHfzFzEtmwI6MMmy4lWHzMXY69aoIF9vzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dL7GNpMGOjfC1EqQgbrydVTHdXx0tObhhEGv8PK36io6FZXRG9s1IMB7KIrDkUR7-PBMr9HjN4F4K5ydrfMy8UWhoTUAZupH8bT3qvh1Qw3s2D--ey7aT8NYFeL3TbEdfmb8ZlJqVtEgMg8uwwZXbC3LF4wWAfHssFmB77XvYa0svrWVOkyD1f5lCA0ZxGnlNJF92xsCvbZ6tTy1ufLGW1pbRdElT9XMM4qvww3TRmtHXugy6gSz0xv9jxTSGS9gA16oS6AGau2IloMVIvxrEPqv72-lcfAx1Ae7l6ra-GW9CRxzjCXajfOFIkYocgwzI-zvMbFqvqDReh_hnARKdg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏴
اعمال شب عاشورا
#عاشورا
@Heyate_gharar</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/662961" target="_blank">📅 19:51 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662960">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48ca134d1d.mp4?token=PxkpSH1sMoXPyk5fhpxi2FNAVyvzwq8HCiVZcJjc_7ReZ6PbLmMxG8FgxJp9Z5QYv0DY7lODT-GEkgxp0_HzXbBiAYFKh4Wc7btX5Xx3V9CaDVSVqnzNysj2j_Hq1yrGrfNxHnQZnKfFVIGoV16hzTYNfsKsM2iQuum0wILIbTvNSJyIU04wUxAAKgmGhj-xMeYdnfNba5s5BoYbONP0a-QKjcpJ5ZyCrCXRgEMiRtfB21U2ySasZDzfVkXGD5KXcE-8YQZMfElbeSOkYLYyvwRxyL4AgA2hqc7t68OxZFF0rukqfrLEDVsJjcKphCXzupNpGI_0UxCJ8Fs1a5ECVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48ca134d1d.mp4?token=PxkpSH1sMoXPyk5fhpxi2FNAVyvzwq8HCiVZcJjc_7ReZ6PbLmMxG8FgxJp9Z5QYv0DY7lODT-GEkgxp0_HzXbBiAYFKh4Wc7btX5Xx3V9CaDVSVqnzNysj2j_Hq1yrGrfNxHnQZnKfFVIGoV16hzTYNfsKsM2iQuum0wILIbTvNSJyIU04wUxAAKgmGhj-xMeYdnfNba5s5BoYbONP0a-QKjcpJ5ZyCrCXRgEMiRtfB21U2ySasZDzfVkXGD5KXcE-8YQZMfElbeSOkYLYyvwRxyL4AgA2hqc7t68OxZFF0rukqfrLEDVsJjcKphCXzupNpGI_0UxCJ8Fs1a5ECVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیرمردان ناتوان حتی
با عصا میزدند بر بدنت
همه جا را سیاه میدیدی
به فدای نفس نفس زدنت...
🔹
عاشورا، یک پیام آسمانی در زمین که پژواک آن همواره به گوش وجدان‌های بیدار آزادگان در هر زمان و مکان می‌رسد و آنان را به خود فرا می‌خواند.
🔹
عاشورای حسینی تسلیت باد
🥀
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/662960" target="_blank">📅 19:45 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662959">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔹
روبیو: یادداشت تفاهم با ایران ظرف ۶۰ روز اجرا خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/662959" target="_blank">📅 19:44 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662958">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a822dd944.mp4?token=s7FQbNJXv9j4sk8-z_Bqn8OjzTQ7p-KUVEmOdXpz3U1xT2bC0Hftm6TcGMvEo4Ypkwz8T_ntJJ2zJAh7pDCq5UKzEogvYMtC2prg8tXgoAuGLZIs6HK-Zz3ZC5EhpGhJB1OTEWGEnsRmkopt0jt2lzp3iga8BAou1yjufQirT1Kz4pYBoyfX2OZ63yjTf29OEUrMwhPWbtHgTBNeKlBTXAZOAVZYLYEijQHDDZJbCll9YfSSg5o8FgzNuY2D9SR-9L_13J6SXHVED89npumSsQjo1g0q-vCdFGEGo4AcYslSl_Z_idV-hXPAgjrvuiXmgMdk-zSoJ-VJNqarzJhZ3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a822dd944.mp4?token=s7FQbNJXv9j4sk8-z_Bqn8OjzTQ7p-KUVEmOdXpz3U1xT2bC0Hftm6TcGMvEo4Ypkwz8T_ntJJ2zJAh7pDCq5UKzEogvYMtC2prg8tXgoAuGLZIs6HK-Zz3ZC5EhpGhJB1OTEWGEnsRmkopt0jt2lzp3iga8BAou1yjufQirT1Kz4pYBoyfX2OZ63yjTf29OEUrMwhPWbtHgTBNeKlBTXAZOAVZYLYEijQHDDZJbCll9YfSSg5o8FgzNuY2D9SR-9L_13J6SXHVED89npumSsQjo1g0q-vCdFGEGo4AcYslSl_Z_idV-hXPAgjrvuiXmgMdk-zSoJ-VJNqarzJhZ3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
مارک روته، دبیرکل ناتو، در گفتگو با فاکس‌نیوز: فکر می‌کنم ترامپ دقیقاً همان کاری را انجام می‌دهد که لازم است
🔹
یعنی تضعیف توانایی هسته‌ای ایران؛ می‌توانید تصور کنید اگر ایران به سلاح هسته‌ای دست پیدا کند؟
🔹
ایران صادرکننده آشوب است؛ صادرکننده تروریسم است؛ این مسئله برای منطقه فاجعه‌بار خواهد بود و برای کل جهان هم فاجعه‌بار خواهد بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/akhbarefori/662958" target="_blank">📅 19:37 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662957">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔹
تلگراف: ترامپ ممکن است پس از انتخابات خواستار توافق جدیدی با ایران شود
🔹
روزنامه انگلیسی تلگراف بر اساس اطلاعاتی جدید فاش کرده است که دونالد ترامپ ممکن است پس از انتخابات میان‌دوره‌ای کنگره توافق کنونی با ایران را کنار گذاشته و خواستار توافقی جدید شود.
🔹
یکی از اعضای نزدیک به ترامپ گفته که او برای مهار تورم فزاینده و محافظت از کرسی‌های آسیب‌پذیر حزب جمهوری‌خواه در جریان انتخابات ۳ نوامبر نیاز مبرمی به توافق فعلی با ایران داشت.
🔹
گفته می‌شود ترامپ خود را آماده کرده است تا پس از انتخابات میان‌دوره‌ای که موازنه قدرت در کنگره را تعیین خواهد کرد از این توافق با ایران خارج شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/akhbarefori/662957" target="_blank">📅 19:27 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662956">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FDoSc0XUA5GOZzdF8AO1RcXB7aMWnGxajqPhIcXFQJza5N_c2jH53TyzbmmsJsdNV2hqDK4oI7L_dfayIjMgHGZWkZf1pxenuGMS0E9PVzDIYsoswl1x2S4kupLxmCfaILTRR-Xf4a8PMrGV1ozHbRbzcgDqMaYBqhsKjqarp6V4JoZRDZAYV4ONvV3zvA3XEgzUP58kWfNxEPUNyNHvI-2X1sCfLsAYRZBGpZ79ioWi8lDicYdTqcttupBw8nRXPU59C7htNhgmUPU3tos-p2YvLY4F6z-uifrZFTGXQVuNnE3oTUMDURM7de9r3J8zhock_AYWDQ4nz9WkZr3Cow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
تداوم نقض چندین باره تفاهم‌نامه
🔹
حمله هوایی دشمن صهیونیست به نبطیه فوقا و حمله توپخانه ای به یاطر در نزدیکی بنت جبیل
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/662956" target="_blank">📅 19:24 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662955">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mvDo-EDftU2LCSBDRmEdmX0Vg66B4R-pnKeIUtsOF_cohUtIP06sJxiNw5ifAvZZceGF1ydG_mRx__5pvUNrNguFrvIpfgQhh7ePlIc2uheTxH5l-CNQsPjRke5Sw_BpDRLygSlCUKs6E__NW066IAEI0dJKPK47DBzhcGMgRqnXResiY4Sl2pV6wmvPoPU2bGmAcIHV9C3Lc4Qd2H0sFb6BLLI6Oh2OZeF8pPhsoTTlAhJWe2dPeDYnDOctzobmfY9LM8ORCaD53H3eI0vM6zVGgDo1nMjsjhsVT1Kl1z9HmIEV0ryBP1aoXEDfrQ5AmIoGLEiTOf3Yw5Ovv82s9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
تصویری از هنگام ورود و اهتزاز پرچم خونخواهی در مراسم بزرگ یوم العباس زنجان
#اخبار_زنجان
در فضای مجازی
👇
@akhbarzanjan</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/akhbarefori/662955" target="_blank">📅 19:19 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662953">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abaef1863b.mp4?token=J0mwYNqqDejj6OWU1Su6M7okCWc8ssiM325kXKALDJy9b5MC03K5nJrQ5msWJywVnEwF515LiS_sw_uURlkcUvcx5yCjvhQ0PX2DqeNpMxllWDbVWjYUpoIHKHorBQDsgumd0v4_U3jetZExjm8fmnVncxgGQOhoJFtIyrTve_gH-0yO3sLfEcxsRcAGoK2AXdkhg0KwG3e3WADjAV0z2XvvxhNGQvx8DjAuj6VUWU0wWzWvO_WOlq44Jo4wMMJm5Pt-mtrKxi19tIezyM-Fdph9gmUSoBNlGKTH4GDMKvVU5XhkO1hhRVK2Ju3V9q0KW9auwgkKRGZ99uY1XVF-rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abaef1863b.mp4?token=J0mwYNqqDejj6OWU1Su6M7okCWc8ssiM325kXKALDJy9b5MC03K5nJrQ5msWJywVnEwF515LiS_sw_uURlkcUvcx5yCjvhQ0PX2DqeNpMxllWDbVWjYUpoIHKHorBQDsgumd0v4_U3jetZExjm8fmnVncxgGQOhoJFtIyrTve_gH-0yO3sLfEcxsRcAGoK2AXdkhg0KwG3e3WADjAV0z2XvvxhNGQvx8DjAuj6VUWU0wWzWvO_WOlq44Jo4wMMJm5Pt-mtrKxi19tIezyM-Fdph9gmUSoBNlGKTH4GDMKvVU5XhkO1hhRVK2Ju3V9q0KW9auwgkKRGZ99uY1XVF-rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
جان مرشایمر، استاد علوم سیاسی: ترامپ خیلی واضح تصریح کرد اگر جنگ با ایران تمام نشود، فاجعه اقتصادی در جهان رخ می‌دهد
‌
🔹
به همین علت مجبور شد توافقی با ایران امضا کند که از هر نظر به ضرر آمریکا و به نفع ایران است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/662953" target="_blank">📅 19:17 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662951">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
فرمانده قرارگاه مشترک خاتم الانبیاء: کارکنان پدافند مردانه ایستادند تا ایران استوار بماند
🔹
جمهوری اسلامی ایران امروز با منفورترین جنایتکاران عالم روبه‌رو است؛ دشمنانی که هیچ‌گونه پایبندی به اصول انسانی، اخلاقی و حقوق بین‌الملل ندارند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/662951" target="_blank">📅 19:11 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662950">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f831a8fda.mp4?token=LPomIsJf9T5z56nqmoqoCpuGWw3Gs5-UydjKWWzAS3kIXfR81NgKCeUzxJLfhPUSAPkfSk41VPxTFplcXiYSZhjnrTgBSPWyDAJinCr38ctPQNXysfBiczTz3LcGoIVMwCWnHP00UIXHWDcqCnh2tA6mGjFdNAnBW3gdEYSzSzHV3ehmmKa6OtQYy01b-dyKjtlXGf8ejBS8epuA2UDqd-MX3h--2C-4PYnw6dapKUqjLulwYaSKZdogx1zqHGK2dPFKcc30qrRh8nov2umvJCZyiUq01VGn49GyrkFBau8eFwhThienwL1zylhTSxwAilHyFDTDuwHlD9B5LVgmsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f831a8fda.mp4?token=LPomIsJf9T5z56nqmoqoCpuGWw3Gs5-UydjKWWzAS3kIXfR81NgKCeUzxJLfhPUSAPkfSk41VPxTFplcXiYSZhjnrTgBSPWyDAJinCr38ctPQNXysfBiczTz3LcGoIVMwCWnHP00UIXHWDcqCnh2tA6mGjFdNAnBW3gdEYSzSzHV3ehmmKa6OtQYy01b-dyKjtlXGf8ejBS8epuA2UDqd-MX3h--2C-4PYnw6dapKUqjLulwYaSKZdogx1zqHGK2dPFKcc30qrRh8nov2umvJCZyiUq01VGn49GyrkFBau8eFwhThienwL1zylhTSxwAilHyFDTDuwHlD9B5LVgmsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
تصاویری از مداحی و نظم عجیب یزدی‌ها از نمایی متفاوت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/662950" target="_blank">📅 19:10 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662949">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ae119ec00.mp4?token=akQxSIYih0cIbgUKMgI8tFlU_r_WzvNryS4bSGfVWEinrfR5_FctD-2uyVmZRf0KYgVxmSFz46nbvvb4mp58uhnfKWRRTnYIT8D_zWvkmW8LP_kTtsLDRNGidzySIoZyazg9ity4TUAh_WD9p1AiWh19ByGLWORVaYN7ZYS2ZHbyrvEE0xezrjTqH2obSdu-yt9JKKnoyvJeFX0Tly4J8x1f_blPc6UVCTxrcrHGTnATkLLolb4m2b_dh3fReSyRWImaV4bLT1SGPBnKtTAoykW764N1FxhGRzCSxYo18RlF1bx5b5ml_Cj2aKLBm1T_TVdmCsblOCbeFaJjyJzWNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ae119ec00.mp4?token=akQxSIYih0cIbgUKMgI8tFlU_r_WzvNryS4bSGfVWEinrfR5_FctD-2uyVmZRf0KYgVxmSFz46nbvvb4mp58uhnfKWRRTnYIT8D_zWvkmW8LP_kTtsLDRNGidzySIoZyazg9ity4TUAh_WD9p1AiWh19ByGLWORVaYN7ZYS2ZHbyrvEE0xezrjTqH2obSdu-yt9JKKnoyvJeFX0Tly4J8x1f_blPc6UVCTxrcrHGTnATkLLolb4m2b_dh3fReSyRWImaV4bLT1SGPBnKtTAoykW764N1FxhGRzCSxYo18RlF1bx5b5ml_Cj2aKLBm1T_TVdmCsblOCbeFaJjyJzWNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
مدودف، معاون رئیس شورای امنیت ملی روسیه: اکنون زمان آن فرا رسیده است که این توهم را کنار بگذاریم که یک کشور یا یک بلوک واحد می‌تواند قوانین و حقوق بین‌الملل را دیکته کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/662949" target="_blank">📅 19:06 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662948">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T-H5E41kW2MdAXUadzNWxfXe9ctAV_fqACMXqN6XWp4V8KJtlvtq9wtwqNmk3XGXkdfzXcbZcgAgicY8fszz5oXL0UfrOxhvnN7KnoLGY7bmlXLVvbKJYdDRxOOuxhJxSRG8I0FGfcPeV5Wf96ovQ0gz6QQyyaFPINStMtg3wVk1YbdAgB16NFGY3Z-mLFxBAzcTpVkyKRqzVwD3hE3uVfgWJ_xLdxicdYbPUKfvGTFU8oFr_4FA99v9FeXRmnuCAb-otUxiyJ6p1buV-rTCO9k4xvGOizy69uAh6hQ0RQK130wgt01rgIJHH_MD-q3ROJIqnmfvoCJV4tk48lVcrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرفوری رو در سایر پیام‌رسان‌ها هم دنبال کنید
🔹
خبرفوری در ویراستی
👇
https://virasty.com/akhbarefori
🔹
خبرفوری در روبیکا
👇
rubika.ir/AkhbareFori
🔹
خبرفوری در ایتا
👇
eitaa.com/AkhbareFori
🔹
خبرفوری در بله
👇
ble.ir/akhbarefori
🔹
خبرفوری در سروش
👇
Splus.ir/AkhbareFori
🔹
خبرفوری در روبینو
👇
https://rubika.ir/akhbarefori
🔹
خبرفوری در گپ
👇
gap.im/AkhbareFori
🔹
خبرفوری در ای‌گپ
👇
iGap.net/AkhbareFori
🔹
خبرفوری در واتساپ
👇
https://whatsapp.com/channel/0029Vb1RfOdJkK71F9wpxh3F
🔹
خبرفوری در اینستاگرام
👇
http://instagram.com/_u/akhbare.fori
🔹
سایت خبرفوری
👇
http://khabarfoori.com/</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/662948" target="_blank">📅 19:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662947">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔹
ادعای ترامپ در مصاحبه با فاکس‌نیوز: ایران به عنوان بخش اولیه توافق، تاکنون ۵۰۰ میلیون دلار کالای آمریکایی خریداری کرده است
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/662947" target="_blank">📅 19:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662946">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a430f52c54.mp4?token=lFI-ahzc2BwwW3XMyysIDZgBGQuIzj-L_BqUcsGIvcyo4JiXT5UHbD1kYnRvXpaN64-gWT_TRrIFScpNhrUJmErN6ovVVhxI9pUtpFZe1wd68ZKzZUwZqLRcBB7Fd4cZMhb27M2u-LlFk9zBhZ9XrKKhckJ21tZN9n9OjPs_2traIo6pxUPQnhZS74abhueonFUqA7iLGnZFB9CaA73PZGIwyOO0gmMgK0ZjkB7Z144jXOxqgRwK38Dn5cRjGcoK32jjcphFZyigFsBZ8lstyJKgGzyh6-miMofwBYEm-OFsUcz2H9GoAZ8qtY4FsYvNoMySdMiVkbxgIKtPsK0C3H_kTms2iOLJzpD45fhS75L6WB-XkqH39FJTlmLz37NUsleQ3ENtUSIqV0RrOfR5rCvp8NxbLtK_l7ZLm6ahWuBDpUPhcAx1IWOiUHEfOIdzPAw5XrXiSfonp1Vp67dtNErejd-krGfnKlTM2-QhnTdK5IlKKB9zd_YPOAVz630HfOSWegpL3OCXb9jRurV-W4D-EWHFhSh3gi2tk7_wawK8WWRrRsw9UCr3FpztdQZAfc7Y1297WaCMmTqtcp5n8j8PNm8tvVo9mTh_K0viL-G3d7KnmiL0bletBPfiovOfBAfZpI_t-NOc-MYeluVZWdgUMPQwTaHxSf2_BhWzVIo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a430f52c54.mp4?token=lFI-ahzc2BwwW3XMyysIDZgBGQuIzj-L_BqUcsGIvcyo4JiXT5UHbD1kYnRvXpaN64-gWT_TRrIFScpNhrUJmErN6ovVVhxI9pUtpFZe1wd68ZKzZUwZqLRcBB7Fd4cZMhb27M2u-LlFk9zBhZ9XrKKhckJ21tZN9n9OjPs_2traIo6pxUPQnhZS74abhueonFUqA7iLGnZFB9CaA73PZGIwyOO0gmMgK0ZjkB7Z144jXOxqgRwK38Dn5cRjGcoK32jjcphFZyigFsBZ8lstyJKgGzyh6-miMofwBYEm-OFsUcz2H9GoAZ8qtY4FsYvNoMySdMiVkbxgIKtPsK0C3H_kTms2iOLJzpD45fhS75L6WB-XkqH39FJTlmLz37NUsleQ3ENtUSIqV0RrOfR5rCvp8NxbLtK_l7ZLm6ahWuBDpUPhcAx1IWOiUHEfOIdzPAw5XrXiSfonp1Vp67dtNErejd-krGfnKlTM2-QhnTdK5IlKKB9zd_YPOAVz630HfOSWegpL3OCXb9jRurV-W4D-EWHFhSh3gi2tk7_wawK8WWRrRsw9UCr3FpztdQZAfc7Y1297WaCMmTqtcp5n8j8PNm8tvVo9mTh_K0viL-G3d7KnmiL0bletBPfiovOfBAfZpI_t-NOc-MYeluVZWdgUMPQwTaHxSf2_BhWzVIo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
حاج قاسم کیست، دشمن هنوز حیران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/662946" target="_blank">📅 18:59 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662945">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/222f86887e.mp4?token=q2hiOdodxJCU5XtxI7feWvVF0S8_1oyFUBmfcbCAu8jgGvSrP6UWWqepm5mw0q-WJXIsu8QoELDvX9A966FIcQe-w26Y-bf5i1tthgzTmM42FF3t_9dJh7w8A25N1L4y4b-L9tIhm7idp0ZS-fl3p0HDOwayZW8gxk1IrFW7YqPwRT4hFrz8qspojrQ8SMHrD1XBiEUNEOL-B9TTsFTJKH7nvlWWwIdsTKOcY8nDeetXB63jJHZV_xWdo7InUw__H4mIiYiKJrVS1Zv0yauUcLdE_92gfW1S4BhnD0lTH-KOKAFeavGcB7gtbONFhbeKtAMszsTvS-Gkle9uhnX3mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/222f86887e.mp4?token=q2hiOdodxJCU5XtxI7feWvVF0S8_1oyFUBmfcbCAu8jgGvSrP6UWWqepm5mw0q-WJXIsu8QoELDvX9A966FIcQe-w26Y-bf5i1tthgzTmM42FF3t_9dJh7w8A25N1L4y4b-L9tIhm7idp0ZS-fl3p0HDOwayZW8gxk1IrFW7YqPwRT4hFrz8qspojrQ8SMHrD1XBiEUNEOL-B9TTsFTJKH7nvlWWwIdsTKOcY8nDeetXB63jJHZV_xWdo7InUw__H4mIiYiKJrVS1Zv0yauUcLdE_92gfW1S4BhnD0lTH-KOKAFeavGcB7gtbONFhbeKtAMszsTvS-Gkle9uhnX3mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
تاسوعای حسینی در حرم مطهر حضرت عباس(ع)
🔹
همزمان با تاسوعای حسینی، خیل زائران و عزاداران از نقاط مختلف جهان اسلام در حرم مطهر حضرت عباس(ع) گرد هم آمدند و با برپایی آیین‌های سوگواری، یاد و نام علمدار وفادار کربلا را گرامی داشتند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/662945" target="_blank">📅 18:54 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662944">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F1SjcE43eqWi_PfafuMCNQqTmdXRVYsDdVQ-FukIQVJzw1hyIGWFw73CRGFIwKC5Jfteww7C81aGVdiGGkpAH9VIWsC4BDHs6iBdjb_MSmjZUIsGqCFJ9B-8ncw5bLFDozPFt_xIdPmi3E75yTGOeOXexfVL_FN5Km2XVK08QLRDigfD_RL-FxRhT0HNaDvhNOGHSOslYR9DOAAFJA4HegorvD8WK5k7SfZLmFUZdWwzHyACZ3UN1tdzdod-6iOf66t8f5WBHa_VSJs3twjIkfeojnAUjwaBQpxzsugsoTS9qwnK9fhuQTR-ONa4NFqAiAS_G5y5CA_CXZnxvrl6ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
فیفا تبلیغات مربوط به مشروبات الکلی را از محل دریافت جایزه بهترین بازیکن مسابقه در جام جهانی ۲٠۲۶ حذف کرده است؛ تا به عقاید و باورهای دینی بازیکنان مسلمان حاضر در مسابقات احترام بگذارد
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/akhbarefori/662944" target="_blank">📅 18:44 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662943">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔹
نتانیاهو: برای حمله به ایران از ترامپ اجازه نخواستم، فقط او را مطلع کردم
#Demon
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/662943" target="_blank">📅 18:41 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662942">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔹
آمریکا فعالیت سفارت خود در کویت را از سر گرفت
🔹
ایالات متحده آمریکا همزمان با سفر مارکو روبیو وزیر خارجه دولت دونالد ترامپ به کویت اعلام کرد که فعالیت سفارت خود در این کشور از سر گرفته است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/akhbarefori/662942" target="_blank">📅 18:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662941">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oaZP6ADyYMSXbKmv1dZl1q7RoDxjXZAroYkbeSp0IoJYT4ki6xXJkhjfBMn6JXWYuuHLBZe1cch_IlTsOUAsYk2N1wKIUmMiKjeDP9WQgB2-baURvSMHVTZ48iFhPB0EJw_8YrHEHTSgQMKmC-Rdj7ldhkEwCzrS99MBQ4iipVsvZSN7zpapKD_mr10K7fns-ytUpdETKOVB3aOk2uPmPdF49jv89mMMvOR2pznS5ELYK-bllhsI3sGFeKHhhsaH85LJ5dZ3a8smuhqFUf9fGSq3f6YSXi39-mYrtkoC31VLmEQdTeP_rCsCXVzEWwcJ3NgxdAINwlh1MXCvlhbL4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
سخنگوی کمیسیون امنیت ملی: تنگه هرمز را با مذاکره فتح نکردیم که با مذاکره واگذار کنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/akhbarefori/662941" target="_blank">📅 18:30 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662940">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32e0667054.mp4?token=MSapErE-5VRABB6tCKjk50ZAh5qrnLiZjM-2ci0mFu0Fm6rkbYMapBvARb32U0sxV8YyTrOxYa1A2DZiG9QpjljGsIKW9SyLDb4skD9mHhOvPtCDBcD_yGIJ0ETiABNoWXiBeO9x2Bfr5DACBH7d1xZ3zvBIC8hB8KQoZakqgjIAN4s9B9u-RksCO8J8IG36Y6TLEXp8jCzo9MG1ZEeCzWXTV1Tk50tTlWWCDmP6h74V49eaztdjUR2j_oCm6cVc0euxEiYs1WvdnkKmlF45Gfu6ItyrqYeTdm2RDHmd_17W7sLr0yKR6wNkJhzaKoTJ6WzUEEfqnsLq4enPgLAjrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32e0667054.mp4?token=MSapErE-5VRABB6tCKjk50ZAh5qrnLiZjM-2ci0mFu0Fm6rkbYMapBvARb32U0sxV8YyTrOxYa1A2DZiG9QpjljGsIKW9SyLDb4skD9mHhOvPtCDBcD_yGIJ0ETiABNoWXiBeO9x2Bfr5DACBH7d1xZ3zvBIC8hB8KQoZakqgjIAN4s9B9u-RksCO8J8IG36Y6TLEXp8jCzo9MG1ZEeCzWXTV1Tk50tTlWWCDmP6h74V49eaztdjUR2j_oCm6cVc0euxEiYs1WvdnkKmlF45Gfu6ItyrqYeTdm2RDHmd_17W7sLr0yKR6wNkJhzaKoTJ6WzUEEfqnsLq4enPgLAjrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
وزیر امور خارجه قطر، که پیش‌تر بنا بر برخی گزارش‌ها از سوی پیت هگست با تهدید به ترور مواجه شده بود، در جریان مذاکرات ژنو برخوردی سرد با جی‌دی ونس داشت؛ به‌گونه‌ای که نه به او اعتنایی نشان داد و نه با وی دست داد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/akhbarefori/662940" target="_blank">📅 18:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662939">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0367a0040.mp4?token=r_hQiGKp_KVLmLZ0QV3RwSMHENTY0E8fru-pcpi0gypVapJe5v-hzNKlV_-6nb7fxOjpyyXoJ_eykWHNH1mXd8TzrVw3Nv3T7Q7rOrcTkbh2UJ-YBrOhfFbhPF_Il1Zu0Fk353LBdr-VyMe41xqmf8q6gdpmLJ6PavuwhSJOpPtNxVcyepgxnoydl9ESDUjumCgO7jvO87rCMP6N5yJ1I6KPY7RpJbkcZqhi-HUwLYmA38zVj1nIK1y3Wq6MKmHs-SDt4r1wt7ZYHvMoxSNGb1uukcO67U1u77PHdrvkln2BYTfpE7kXMWwr8Yu71QnZUGDq8H9zOWmSZPrWS3Mz1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0367a0040.mp4?token=r_hQiGKp_KVLmLZ0QV3RwSMHENTY0E8fru-pcpi0gypVapJe5v-hzNKlV_-6nb7fxOjpyyXoJ_eykWHNH1mXd8TzrVw3Nv3T7Q7rOrcTkbh2UJ-YBrOhfFbhPF_Il1Zu0Fk353LBdr-VyMe41xqmf8q6gdpmLJ6PavuwhSJOpPtNxVcyepgxnoydl9ESDUjumCgO7jvO87rCMP6N5yJ1I6KPY7RpJbkcZqhi-HUwLYmA38zVj1nIK1y3Wq6MKmHs-SDt4r1wt7ZYHvMoxSNGb1uukcO67U1u77PHdrvkln2BYTfpE7kXMWwr8Yu71QnZUGDq8H9zOWmSZPrWS3Mz1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
تصویر آیت الله سید مجتبی خامنه‌ای، رهبر معظم انقلاب اسلامی در دسته عزاداری شیعیان با غیرت عراق
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/akhbarefori/662939" target="_blank">📅 18:21 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662938">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf01081c61.mp4?token=bTbPQx0AFvIvD_6sf0WIV0QKqJ7IK6a7w9V2srIjYOlLxO1n4vak0MadkwpGWOl2MuQhqiOXGG202pZi32jtegGf0BV66eHCR0WLWfaaVEjP5ICzNy5sC46m7DyqwxDxjgRvtZsGrCgFTqwjoAbcHEk4QlGrKZVwN_S6PcR3fMopbTuE2LEFihFm4CwwR6DerKjjd86Equ74zQETswdbxlktAiA3Hzl_mb9HYXWnC11uOlHpBxyXhI_37_sFub8K4cnH8tRbH-4Zr80n0ZHr5rKqKuU2Ag65FEh-u5Yd-gpZJP9Uxq4_FkmrISTrGnExQUY6SIjnt0Pbjla28VTKKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf01081c61.mp4?token=bTbPQx0AFvIvD_6sf0WIV0QKqJ7IK6a7w9V2srIjYOlLxO1n4vak0MadkwpGWOl2MuQhqiOXGG202pZi32jtegGf0BV66eHCR0WLWfaaVEjP5ICzNy5sC46m7DyqwxDxjgRvtZsGrCgFTqwjoAbcHEk4QlGrKZVwN_S6PcR3fMopbTuE2LEFihFm4CwwR6DerKjjd86Equ74zQETswdbxlktAiA3Hzl_mb9HYXWnC11uOlHpBxyXhI_37_sFub8K4cnH8tRbH-4Zr80n0ZHr5rKqKuU2Ag65FEh-u5Yd-gpZJP9Uxq4_FkmrISTrGnExQUY6SIjnt0Pbjla28VTKKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
با این ترفند عالی بادمجان را سرخ کن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/akhbarefori/662938" target="_blank">📅 18:16 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662937">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔹
افشاگری رئیس ناتو: ایتالیا در جریان جنگ علیه ایران پایگاه‌های خود را در اختیار آمریکا قرار داد
مارک روته، رئیس ناتو
:
🔹
ایتالیا به ۵۰۰ فروند هواپیمای نظامی آمریکایی اجازه داد تا از پایگاه‌های این کشور در جریان حملات آمریکا و رژیم اسرائیل علیه ایران، به پرواز درآیند.
🔹
کشور به کشور، متحد به متحد پایگاه‌های خود را در اختیار آمریکا گذاشتند./ تسنیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/akhbarefori/662937" target="_blank">📅 18:09 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662936">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d2ac6eadb.mp4?token=DQYmG0WjlZhSolecfaU1ntyxXKg74NFlKIqFbyXlfpDhRti8KLx5TMA953K7Wcxb-pMmWkr7WdLHVWrIkUJOyTTRzGXWeje2JbvGkdDD6KDrkObI8ExLhzKpxu39n22PbawYXbKS2kBrAGihUiKN2SgjnNw5swxxygUtQdZjlQ7RO74bfIlrGnq_p4Ig4LH6kwC30TYZ8O50zUcQUh_6ZUVbNqvBJLSJTz0ZeRTrqs6aejE-Sarf4seD5u4rFIiveoTcfPN4t4Hb62Ajf4D0XwcirrYvMY_BX3GnRshu5woXsd8HXl7yl_xLsA4t1B2R0AXQyCBEVJ2Fm-tKJcC9Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d2ac6eadb.mp4?token=DQYmG0WjlZhSolecfaU1ntyxXKg74NFlKIqFbyXlfpDhRti8KLx5TMA953K7Wcxb-pMmWkr7WdLHVWrIkUJOyTTRzGXWeje2JbvGkdDD6KDrkObI8ExLhzKpxu39n22PbawYXbKS2kBrAGihUiKN2SgjnNw5swxxygUtQdZjlQ7RO74bfIlrGnq_p4Ig4LH6kwC30TYZ8O50zUcQUh_6ZUVbNqvBJLSJTz0ZeRTrqs6aejE-Sarf4seD5u4rFIiveoTcfPN4t4Hb62Ajf4D0XwcirrYvMY_BX3GnRshu5woXsd8HXl7yl_xLsA4t1B2R0AXQyCBEVJ2Fm-tKJcC9Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
رونالدو بعد از دبل مقابل ازبکستان:  یه جوری رفتار می‌کردن که انگار من دیگه از فوتبال خداحافظی کردم و تموم شدم! اما من تحمل کردم، مثل همیشه؛ چون من بیشتر از هر چیزی به کار و تلاش اعتقاد دارم. سخت بود، باید بهش اعتراف کنم، اما خب... ما دوباره برگشتیم!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/akhbarefori/662936" target="_blank">📅 18:05 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662935">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2996f9020a.mp4?token=tMu-FdG6KLFQF93Ae7vPt9bgmtUxDwI028-CcJ22K9XkYzSH7oonqBRohDq0mS_CcIeW04w3OE2QIm_FNPzja2U22OwVQ9_KowbrxGMm0wq-NUN2VRt3FKNB_nO9cxudc39jSdkoRpXMICVFO9bdSj65jq6o6AT7B5eDw3KIIQ63IgxrWZU_KzHs5Va6oy4XohohkNBqTsgpwURlxE0fHa0pWW1X5C36pPkaTjXfj66DrvIudqTsVsYx84sXJQMV-bcqh65tlRKn3eDu0W12hKEz3UBqtuRfyYuZkYbIvQdmR-kUKhS7KPLVlYxJPtOu0adT0Pfh-JIrKMlKg3ZZYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2996f9020a.mp4?token=tMu-FdG6KLFQF93Ae7vPt9bgmtUxDwI028-CcJ22K9XkYzSH7oonqBRohDq0mS_CcIeW04w3OE2QIm_FNPzja2U22OwVQ9_KowbrxGMm0wq-NUN2VRt3FKNB_nO9cxudc39jSdkoRpXMICVFO9bdSj65jq6o6AT7B5eDw3KIIQ63IgxrWZU_KzHs5Va6oy4XohohkNBqTsgpwURlxE0fHa0pWW1X5C36pPkaTjXfj66DrvIudqTsVsYx84sXJQMV-bcqh65tlRKn3eDu0W12hKEz3UBqtuRfyYuZkYbIvQdmR-kUKhS7KPLVlYxJPtOu0adT0Pfh-JIrKMlKg3ZZYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
ویدئویی از حجم بسیار زیاد آب رودخانه سیمره در شهرستان دره‌شهر ایلام
🔹
نیروهای امداد و نجات هم از پس سیمره برنمی‌آمدند
#اخبار_ایلام
در فضای مجازی
👇
@akhbarilam</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/akhbarefori/662935" target="_blank">📅 17:59 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662934">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/INwJvF64pSdKtFl0wigenECe5qOSOxJlojzmqWV0SyKzx3JLdHe-3T3-lqYvpDC9vXKfJ6cJMb3hcTw57-whPsyD_8N_lsorps65_9MRHe4_CzyDcMEpwLfcm06xJ_7gjUhDlkIQvw-Zt5E35FmqI9ya8Pi3wey_AJheKcwhoGYf5aWzbI1hithuezMM78QTvLX4s4-mXaVBQm2lr4ijK0kVrjbvvHOThpPXTpeMboRgQuChan1BeNaL6Efa0fQ90MQCiTTsxFCzj3CKwDMgtxaZxqb7M31QDQzTuvCpyQPB2LrqSPnKz3DIy-Ndfu5FgXgIe9E8RG2OUizciqOyTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
سقوط طلا به زیر ۴۰۰۰ دلار؛ پایین‌ترین سطح از آبان ۱۴۰۴
🔹
قیمت طلای نقدی در بازارهای جهانی رسما به زیر مرز ۴۰۰۰ دلار در هر اونس سقوط کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/662934" target="_blank">📅 17:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662933">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94068cf6ec.mp4?token=G61kiHUkABGXncySGbQtF-stCHPMe7z0sr6BV1gwwBqLbCxQhFhNI21jAVH9wTGgWOsl7C9YLvLlJIdCOpRgx0Jl_T9PY2VCIt03s1m_tlUwvZcb7C6KVw4rm_0q2lkEzuv1QWYyp1_0sHquX5jmWUzNHPzy4t4KNESToAVf2ke1yy_aW2fSWw-1bAPbouhWP9x-IJtMCTrGLNk98og6oc40AqVu0JjWYV3vybtxt5TtojPImjd05WqHPFQNgE87ubPdLxAE11zLLUYRz-JCSBcWKvcRVeFfNwF4cldP36l7mMXJ1ASzTA5-Em3FCwealP63cX-vILnHqSprGsAb3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94068cf6ec.mp4?token=G61kiHUkABGXncySGbQtF-stCHPMe7z0sr6BV1gwwBqLbCxQhFhNI21jAVH9wTGgWOsl7C9YLvLlJIdCOpRgx0Jl_T9PY2VCIt03s1m_tlUwvZcb7C6KVw4rm_0q2lkEzuv1QWYyp1_0sHquX5jmWUzNHPzy4t4KNESToAVf2ke1yy_aW2fSWw-1bAPbouhWP9x-IJtMCTrGLNk98og6oc40AqVu0JjWYV3vybtxt5TtojPImjd05WqHPFQNgE87ubPdLxAE11zLLUYRz-JCSBcWKvcRVeFfNwF4cldP36l7mMXJ1ASzTA5-Em3FCwealP63cX-vILnHqSprGsAb3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
همه‌زیر بیرق حضرت عباسیم(ع)
🏴
🔹
این بیرق نه فقط متعلق به یک‌جمع بلکه مسیرو هویت یه امت است؛ مسیری که همه ما به تأسی از رهبر شهیدمان، خودمان را زیر سایه بیرق علمدار کربلا می‌بینیم
🔹
منتخب تصاویر از حضور عزاداران و آیین «علم سلام» در حرم مطهر رضوی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/akhbarefori/662933" target="_blank">📅 17:50 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662932">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F6oaBzW3RL1S8h7NDMZ8XKOBr8qdq8dGiXs5PamCCeCeGodwVvGLuHDdmygBCC1cXaY6cahlvwvnGhyndiC0cSIeq4br28ABM-MYJ9L9oi3XFLO1rAGt9USDeIIvaxoyWMuD41I26C7suUHpXoQdbxcNSynDBLRiI-Id6t43twqwqzvtLr-5qsnExEyehZompdZgDeHiCRjpC1XwI5Z2RSxep0XpUdOWDK2VM6I0Im3xV_L_30747afWNasE0sg0AcrSdbR-RiEOe8SOaPi_wsuo0eVrxTk_o46A19fZAHWQW9Zn5gQhZgptMEZKy_eGCPwm_GAMADJvbGyFOd01Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
۵ اشتباه رایج تابستانی که می‌تواند عمر لاستیک، موتور و سیستم خنک‌کننده ماشین را کم کند و خرابی‌های پرهزینه برای خودرو به بار بیاورد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/akhbarefori/662932" target="_blank">📅 17:44 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662931">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vDcuNyitGKo42uRd0wKXctNBUyju7qSe-0VqQXmVl2W5bAioIM5URTgGZu-_HWb50oil0imVrOnXPGq8rfVSWlzaZBxiXMexeHk1JiDmskDYyVobZ9XaN1ANbSsRRyfd_eDd62VDHnqxjoYf5DsMpf3mbl-QWXuOmzkOcWdy6MJxJvOjHSNW3m4g14T433VFr77lkK5ytNlB1-vS3LMSuXEYm01DIWyoh49VoHWmv2TcYgxR8D0Qs9MjP1zJ8wb0dUG5Y0v847UED4yBrIHKw56W3qrwIj2JzD8jf5s5WYlFabjduWTtYx_gfNF6NshMyDDwfxfTaeIpTcESY2YYCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
سعید عزت‌اللهی در رتبه اول مشترک با پدری در بیشترین قطع توپ در دور دوم مرحله گروهی جام جهانی ۲۰۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/akhbarefori/662931" target="_blank">📅 17:38 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662929">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53f14fb2f9.mp4?token=Gzho-6yEXZ7pqmoavm2XFu2E4icFPQXapFs7VCIXVh692R_mRmiZnp76EHRhTnyjt4UbN-H1n6hvIoPGSVUag0NVt8As70hsFS7lhzqDw9Mxss1vuY_rYiWvYGdPyPsvY9O3Ql7TzNP1PCrfp2BSTZP-2fiREztmaD8S-MHOfP2sHPHxYZypZVpT5OdIbPtf_2IyGWYEZ1Mu2v60k4ZnjMcKaWLzMHnr1cuUd03UAYl52FgHUaISIpjv94D_tf7E6tKAaZlNViz_wvFTKk4oS8cRl-2R4vU8FHwfKcW_LuDTyIy7YH8dsPiBMTx9We0xnNc5r31aL-8iOJ0dQMlKlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53f14fb2f9.mp4?token=Gzho-6yEXZ7pqmoavm2XFu2E4icFPQXapFs7VCIXVh692R_mRmiZnp76EHRhTnyjt4UbN-H1n6hvIoPGSVUag0NVt8As70hsFS7lhzqDw9Mxss1vuY_rYiWvYGdPyPsvY9O3Ql7TzNP1PCrfp2BSTZP-2fiREztmaD8S-MHOfP2sHPHxYZypZVpT5OdIbPtf_2IyGWYEZ1Mu2v60k4ZnjMcKaWLzMHnr1cuUd03UAYl52FgHUaISIpjv94D_tf7E6tKAaZlNViz_wvFTKk4oS8cRl-2R4vU8FHwfKcW_LuDTyIy7YH8dsPiBMTx9We0xnNc5r31aL-8iOJ0dQMlKlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
عزاداری حسینی در شهر دنهاخ هلند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/akhbarefori/662929" target="_blank">📅 17:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662926">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c756e008b5.mp4?token=jDHbJUG8DXONdaLLGO5IdWNWwHHfyAnhZT_9nSaq98jh9jthAWovjEzxYO004dSJTsraKuZe24DUK_ue9utvz3dVUs0Bw6BBoLn4MUU-ekmWzTyTCQ-iB8Pd_5EcbURiuCGH6K_1UXVI0SdF-Nn4Cw7gjY3XsRakyanOHU3VslPI9c4VQnJ3SOl6Fzgeh5cfmyHkH2Y09w7vKcfQ_FFkFc986Po4cLGGvD5F3Rq5_YZNEdrZIbEdjelCmrZ8fbFTanPPzbNptVraOK2DaLPJpoRPfJw2LO2ULobukkjZt0PQtHoLI7BbvL0BXSE0km8C0qugwij0XfUBVXHsfwpKWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c756e008b5.mp4?token=jDHbJUG8DXONdaLLGO5IdWNWwHHfyAnhZT_9nSaq98jh9jthAWovjEzxYO004dSJTsraKuZe24DUK_ue9utvz3dVUs0Bw6BBoLn4MUU-ekmWzTyTCQ-iB8Pd_5EcbURiuCGH6K_1UXVI0SdF-Nn4Cw7gjY3XsRakyanOHU3VslPI9c4VQnJ3SOl6Fzgeh5cfmyHkH2Y09w7vKcfQ_FFkFc986Po4cLGGvD5F3Rq5_YZNEdrZIbEdjelCmrZ8fbFTanPPzbNptVraOK2DaLPJpoRPfJw2LO2ULobukkjZt0PQtHoLI7BbvL0BXSE0km8C0qugwij0XfUBVXHsfwpKWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
شور عزاداری محرم حسینی در شهر سماوه عراق
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/akhbarefori/662926" target="_blank">📅 17:06 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662922">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7TmOGl_74BohrtKk_3JODZ_BwOGGswSGbNKjIYf7BJybx_r8HPTys45feasnZ0EB4ZCxPjPYIR31DXk0wCpP_iseiPEX6AbckpYWxrWyiWvVyHR0FEqLGVBwf1FvsGWBE3R7bTftTPgwH291mB7Nmo3hiidbMBwsHUJ0pZ-6D8g28rM8V23rXP9dGd-SZkmg3s2B1eXz2iijCHi-AzarZ8ri-NJ7P_LfL3UqrEaiwzFPXrf1REuxMQUDwoMOGbtEsmGdY40LNtGQDSCudm9m5ULapJ-txoMw1w8_5wz4qCfVNnaq_sJPnSPEBnQLwYDw9dojZN0vEYKZ2m7-afWFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
علیرضا بیرانوند در رتبه دوم بهترین دروازه‌‌بانان دور دوم مرحله گروهی جام‌جهانی
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/akhbarefori/662922" target="_blank">📅 16:51 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662920">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N0_n5ZAespYdVduYwkhUDfwZWKpYzpNwr9mk_OpZYySSLBCV7g8t-smHZy-zFuBllFuPTOxdXwNEJB1lM43YEVyYgH0ZNtli60yFT5u-HJXkxAFS4TGzqy9IFNAVvBSdDI5O27oZoagF0WU9O6PZjtHyq__UGvBd03ToLppzdc5OsULkkfbV_uvrRh-V1BJeURdrefCJBlcHreZt5e-BmkaMjczIaB4QGoJVNvpf19EdTjqKXQJnmqkcmxa2eGVApHZVJx7GQhuzNm75Qj0uzY5vUK5-iz6cEKId41wMRhTSOW0nnpR6pLimbvzFpVV86aU9uOP0MaNpxznl_mEQ_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تمهیدات حوزه حمل‌ونقل جاده‌ای در مسیرها و میعادگاه‌های وداع با قائد شهید امت
🔹
مدیرکل دفتر حمل‌ونقل مسافر سازمان راهداری و حمل‌ونقل جاده‌ای از آمادگی و مشارکت حداکثری ظرفیت ناوگان حمل‌ونقل مسافری جاده‌ای در مراسم تشییع و تدفین قائد شهید امت در شهرهای تهران، قم و مشهد خبر داد.
🔹
مرتضی اله‌یاری با اشاره به فعالیت ۵۶۰۰ دستگاه اتوبوس بین‌شهری با توان پیمایش بیش از ۳۵۰ کیلومتر در کشور، گفت: هماهنگی‌ها در خصوص برقراری سرویس‌های ثابت روزانه و اعزام ناوگان فوق‌العاده متناسب با حجم تقاضای سفرها صورت گرفته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/akhbarefori/662920" target="_blank">📅 16:44 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662919">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔹
شوک بزرگ برای جامعه اطلاعاتی آمریکا!
🔹
خلبان جنگنده F-۱۵ ساقط شده در ایران برای اولین‌بار فاش کرد
پهپادهای ایرانی با چینشی چون «عروس دریایی» و «سفینه فضایی» حرکت می‌کردند!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/662919" target="_blank">📅 16:41 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662918">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VXme25TbP7D8ZlOfjYpwaFR9qcmTookwjZlImQIEYAfb4_tfVr06r3ecfN3RzdvQ7KcA87RcOdkpYH5ivUZNqvk6aDgxYkXKZOEbjqBWnMMKJd4CYlKlljd6ALaPG3pWkHZRxsL_zeOwMbHQ4C153FX5K8PKWUIbcIatbFH5GOS8ftX4BaUlZEqtkRJ0FffmhVxSAajkIteqvB6l8KC8UKHMy9fknqn7JrA6gmZk92DCmNejjzddeunjbBGENLiz1z_lOJKf4PniFfRuFQ6yxKySnOZ6GkStzJA1lHt04vy3EA6JPhloZJji38COOY-qrikWcIxW6E69SRqZL7Fw5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هواپیمای پزشکیان با اسکورت ۶ جنگندۀ ارتش پاکستان وارد اسلام‌آباد شد
🔹
رئیس‌جمهور در بدو ورود با نخست‌وزیر پاکستان دیدار کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/akhbarefori/662918" target="_blank">📅 16:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662917">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HmmQgRrhq56iN2YCuaOSvmSU9jalxoM1jXWCQ2786CB8gRtnGrmivvUtDwjGXPvYay0qZHs1dtMHtocQ3GYOTDuJf4b-ur_SduSXFrJwcYQoZXhgk0GoiMyzIFg1cpe48GSY4dFNbYQTU2E3x7h4aWCYCsV0nFdQaYL5OfYuzL6lQw6wHkFYmZ9YaNhn8N3-RZFOvHsUMyMGBkLKs82vzfaYiZuZXefNavTyfR8b7OPIDLq-w7uqnvizVCyK5qCRLueCL3-AiLWPDW1NLjVB5W11Pxb2Kwxg7u95QDqgNYqfKebG7R76_ILpKsqrCwey8uH0qhpsKbhnAOCf5HCrVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
غول ۸۴ متری در جنگل‌های تایوان پیدا شد/ پیدا کردن سوزن در انبار کاه
🔹
پژوهشگران پس از بیش از یک دهه جست‌وجو، بلندترین درخت شناخته‌شده شرق آسیا را در جنگل‌های تایوان یافتند.
🔹
این درخت هزارساله با نام «شمشیر آسمانی رود داآن» ۸۴.۱ متر ارتفاع دارد و از یک ساختمان ۲۰ طبقه بلندتر است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/akhbarefori/662917" target="_blank">📅 16:26 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662915">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7351a1ba79.mp4?token=ts4WntIcPnywDNEGLmzXuwB4LgtlICGJDik-gI9RzMBojikUPTYbWVgT3Qluw_YcnV4xvATlupNA8ciCgwiW5CDVDM1Wq4Pw2WjahiphSphd5h2cCZEAtKjRkfDlMpuEctsB7cEtt4BQVKLhrJ9kiahAZxJMqoicDh88ZenRO2U4FqR7K08auT-KSjP6Sod1yES17MOqHMlfIeQuvJgf4b08JlfVOW1PQlvTbPC9Xq7nGPDuyNXsRI5fj9m5VbpyhgYxkdljJH0axmA0cBrd_gIIl--wfeGAKhCTBcuY_a2_E2aw4m8SaFfup1VQHloWessV5TYXEEAtdOZAbXa6Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7351a1ba79.mp4?token=ts4WntIcPnywDNEGLmzXuwB4LgtlICGJDik-gI9RzMBojikUPTYbWVgT3Qluw_YcnV4xvATlupNA8ciCgwiW5CDVDM1Wq4Pw2WjahiphSphd5h2cCZEAtKjRkfDlMpuEctsB7cEtt4BQVKLhrJ9kiahAZxJMqoicDh88ZenRO2U4FqR7K08auT-KSjP6Sod1yES17MOqHMlfIeQuvJgf4b08JlfVOW1PQlvTbPC9Xq7nGPDuyNXsRI5fj9m5VbpyhgYxkdljJH0axmA0cBrd_gIIl--wfeGAKhCTBcuY_a2_E2aw4m8SaFfup1VQHloWessV5TYXEEAtdOZAbXa6Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
گزارشگر: جورجیا ملونی، نخست‌وزیر ایتالیا اعلام کرد که سیگار را ترک کرده است
🔹
اردوغان: بسیار عالی است. کاش می‌توانستم مردم کشورم را نیز به ترک سیگار ترغیب کنم.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/akhbarefori/662915" target="_blank">📅 16:15 · 03 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
