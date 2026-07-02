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
<img src="https://cdn4.telesco.pe/file/itHaiWTdT-1XahCcpvQx1PKObiRfl8PodXuHeXFzckzdv9l4L01SFYJayHqweelnjKMYb6lPbNC5rz3ZRiyOMEYXJlLBOsuVp4y7m_7u2tPtM5EBFjRD_5UdE-fxqaeIwqgVJsh1_jUfg5N48pUBPtLgp2j-XLqbF8eHncQX5Zgi72qqCld-7A7f2iWO7HGWS23J9NUMe7DvT9_ZbenGlDCXPHgV_MJUPKpmcHoEdcsTLQx5z1QEsAPdGdfKWLkMRS2buIy6PJo8UJw23Nm-ZpEoMQCWagyhidA4i9yFimjlUdulkSXKjngt-7wq_svcp37Jsdtn8TN_qawL8pDDmg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 334K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-12 03:26:36</div>
<hr>

<div class="tg-post" id="msg-16373">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2642f2a070.mp4?token=d89AWsGLfuvhXUDkcA7yJHZB1lW9uDtBeX0ViUbvwoBXxyoJt8T-q9LpW8L0rn4lIEgkxSEQzK30EhmzsygcTJuzeNBqSgcYTgcYuwWlHf7huE7af22b0xohHZUZw8W2w1DQ56rnVmji2CzeGPTCb1JLidRGpW0mLpYrOw_hZREM2mkmiU4QKbUzrQnyHfkU0awba1MFeqyoygpJfWRbdya3N92xRqOrNe8JzJiFr2EEvRB1VzzccuKpoE7j6ADQGjvdNWaHe92yrsXNujHPFVdiwYGSb5oHKUgDmVYmG3a7x__i76RLPPKqdQLBN_WwVYOMIhoOZm7mVZgnd9Dz84WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2642f2a070.mp4?token=d89AWsGLfuvhXUDkcA7yJHZB1lW9uDtBeX0ViUbvwoBXxyoJt8T-q9LpW8L0rn4lIEgkxSEQzK30EhmzsygcTJuzeNBqSgcYTgcYuwWlHf7huE7af22b0xohHZUZw8W2w1DQ56rnVmji2CzeGPTCb1JLidRGpW0mLpYrOw_hZREM2mkmiU4QKbUzrQnyHfkU0awba1MFeqyoygpJfWRbdya3N92xRqOrNe8JzJiFr2EEvRB1VzzccuKpoE7j6ADQGjvdNWaHe92yrsXNujHPFVdiwYGSb5oHKUgDmVYmG3a7x__i76RLPPKqdQLBN_WwVYOMIhoOZm7mVZgnd9Dz84WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم اکنون بمباران شدید جت های اسرائیلی در جنوب لبنان، چندین انفجار مهیب در عمق جنوب لبنان به وقوع پیوست. @withyashar</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/withyashar/16373" target="_blank">📅 02:49 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16372">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CDl0Z6DT1YwMJvv6C6y0GUNvU6mzJgYdD7uacOQ3mv0pbqb-XKmJcvBv66XSU9IVgrNfO-XjUxA7OpP8Svavfhb5N4Xp3iTFYUDS4KreWwdFMsKsJ50q0iK-VOdtpjbyxJLXTbzVPY_El218LsRvi2zVuWpfHB2Sesbm6QHnsUWFrQ4ZldVE7B1QnxcgzSFTIHveQ1wR5yWFVPVjUDc8zC8vj_lMo25-S8a9sQkPV2TpFp58WonPF3LrmeImdrDsH_ndEQunyCUsEfsubVUmWZigH3vWdHIqUVfj58ZkBVoefF8uipXwYvflZTwJ9muCCaW5yUGKQAIHm1PidhUC0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان تجمع و عزاداری شدید نیروی هوایی آمریکا برای عظما
@withyashar</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/withyashar/16372" target="_blank">📅 02:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16371">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">هم اکنون بمباران شدید جت های اسرائیلی در جنوب لبنان،
چندین انفجار مهیب در عمق جنوب لبنان به وقوع پیوست.
@withyashar</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/withyashar/16371" target="_blank">📅 02:07 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16370">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rC7vS3AgLwSQ2y0k1TeOcBgRah_kDwhbIeK780UqjvxkVxfpLpmxnEsfhzezuCRYFIcKGH0pFXmqAXYxDLykD01TnkiZTBkT1ZC3iZrTrWQnTHm5xPRdJ1K49hkreoleqD3efqmaslGrBMQjDpEc2QkI1JoismPxMWND57FtAjxk5CCh6e84ZGSAoMcyEG6-2ZQzACac6mWs5TcZ0wQX2H7vxRLD22uS-f89fo5DicN2LyObsx2t1sNlYcgjXWqIUsK-KwZy3npaG0AR6SD3A-4gwP6F_kHgRk0WiqsqpELEnnQdTWDu1clJkj1uFdVzpE1q5lN7YqfvIybgc2xbyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: ما رادار ایران را نابود کردیم. آن‌ها هیچ راداری نداشتند. و هنوز هم ندارند. ما هفته گذشته دوباره آن را نابود کردیم. آن‌ها یک رادار جدید و پیشرفته داشتند. آن‌ها آماده بهره‌برداری از آن بودند، اما ما آن را نابود کردیم. @withyashar</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/withyashar/16370" target="_blank">📅 02:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16369">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3226c235ec.mp4?token=qBNVfbQhh9YSDVb2iPy4ilPfocApyTJaio3oCEVRIvVBR8pmuHmXEflXj8Iv-0sGJmvdvgpWQHEsafwkBCk6D30C7EFF3OyOFsGzhtqhiuF9uOJBpGJCOW6oSCkYnTkNjM_XzkbsPZgj67H179eRkY40HTjefExcmcgb5GvqpLdYw1ymfDNSeq-1R5nLq4t7KWYYFQzksk2SHpyTNhOhHDumGNV8YhQhqj_sVaRf_Pg1kjL-f6q8okQEWQM5Wcek_6OivrIm9TPVBrAP9_g8szNN6DTep9w36w9q67TKKw2lSkL0DAFb-XqbOn1UvUOG8XdLCw5lyewfJYiLhdXcBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3226c235ec.mp4?token=qBNVfbQhh9YSDVb2iPy4ilPfocApyTJaio3oCEVRIvVBR8pmuHmXEflXj8Iv-0sGJmvdvgpWQHEsafwkBCk6D30C7EFF3OyOFsGzhtqhiuF9uOJBpGJCOW6oSCkYnTkNjM_XzkbsPZgj67H179eRkY40HTjefExcmcgb5GvqpLdYw1ymfDNSeq-1R5nLq4t7KWYYFQzksk2SHpyTNhOhHDumGNV8YhQhqj_sVaRf_Pg1kjL-f6q8okQEWQM5Wcek_6OivrIm9TPVBrAP9_g8szNN6DTep9w36w9q67TKKw2lSkL0DAFb-XqbOn1UvUOG8XdLCw5lyewfJYiLhdXcBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ما رادار ایران را نابود کردیم. آن‌ها هیچ راداری نداشتند. و هنوز هم ندارند.
ما هفته گذشته دوباره آن را نابود کردیم. آن‌ها یک رادار جدید و پیشرفته داشتند. آن‌ها آماده بهره‌برداری از آن بودند، اما ما آن را نابود کردیم.
@withyashar</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/withyashar/16369" target="_blank">📅 01:53 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16368">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cdd54f95b.mp4?token=G6BTB-SJqWux4PXKg98r4G9sSeIcZaP90Bhu5rlmbVJI0hfEar3hmgJMb8E4fHfsXUlPe3eOI_uk2H_rjRBlDeJbbROutsgQukGgYykDFUxLHTKAXsATulyduvvni1DJQYh0zvmpheypyP7-UuSl6W8THeAr1BU31BKcr1kpvf6z7yggYMZXfzty3Q1hdSgrF39_jo4_pksqkYs_svnio_Fnj_O8duJpYleBKFfS0xSddu7Js2TeCj_opzzvPgkVBKRFbC3DUZhc3d4Kf2moVF-oeTlvxprT7bg702sSzM2UQ_qkLpbqO8BjyP-3uRat8fTyl2oDPV3sPnJ4tai4nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cdd54f95b.mp4?token=G6BTB-SJqWux4PXKg98r4G9sSeIcZaP90Bhu5rlmbVJI0hfEar3hmgJMb8E4fHfsXUlPe3eOI_uk2H_rjRBlDeJbbROutsgQukGgYykDFUxLHTKAXsATulyduvvni1DJQYh0zvmpheypyP7-UuSl6W8THeAr1BU31BKcr1kpvf6z7yggYMZXfzty3Q1hdSgrF39_jo4_pksqkYs_svnio_Fnj_O8duJpYleBKFfS0xSddu7Js2TeCj_opzzvPgkVBKRFbC3DUZhc3d4Kf2moVF-oeTlvxprT7bg702sSzM2UQ_qkLpbqO8BjyP-3uRat8fTyl2oDPV3sPnJ4tai4nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدیو رو قبل از خواب ببینید تا پستای قبلی جمهوری اسلامی رو بشوره ببره.
@withyashar
🌟</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/withyashar/16368" target="_blank">📅 01:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16367">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">فیلم مستند "از چشمان جاسوسی درتهران" که حاوی تصاویر مستند از چشم موساد در قلب‌ تهران است و از شبکه ۱۴ اسرائیل پخش شده است.
@withyashar
نسخه اصلی با زیرنویس انگلیسی و حجم کم تا بعد با زیرفارسی شو بزارم</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/withyashar/16367" target="_blank">📅 00:58 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16366">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdc81a4ce6.mp4?token=Z7ejCZZX53ty53X2T7hk43JUCBdi9UaREusMSXTyAPQi0PibjrKPtrpSM1EfLv-qxpV3uDnUSzIqmCRogbbJFIvorihl3GauFFYEbwMYc9MUFPgUzbK03XMO2VRd6uqyp2IrGTmZmpIofAolBP1qa253zqO1a0dBRk-97_77egHbQm0PqWdsKHWCh01x35SwLN7ZH9Lop-aju8Xp8qrf2wUD0U1J0-fGSk5MskfdKYuCOlrffYyIMzQ1UKkuPlSSjBoxQf-pU5QPPXG7jABqlblYM1BUTP9wtqMFpkm5Ety6pAHI2BhzxhrUcKNeRL951clEu8v1HdfTvMf6NOVUCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdc81a4ce6.mp4?token=Z7ejCZZX53ty53X2T7hk43JUCBdi9UaREusMSXTyAPQi0PibjrKPtrpSM1EfLv-qxpV3uDnUSzIqmCRogbbJFIvorihl3GauFFYEbwMYc9MUFPgUzbK03XMO2VRd6uqyp2IrGTmZmpIofAolBP1qa253zqO1a0dBRk-97_77egHbQm0PqWdsKHWCh01x35SwLN7ZH9Lop-aju8Xp8qrf2wUD0U1J0-fGSk5MskfdKYuCOlrffYyIMzQ1UKkuPlSSjBoxQf-pU5QPPXG7jABqlblYM1BUTP9wtqMFpkm5Ety6pAHI2BhzxhrUcKNeRL951clEu8v1HdfTvMf6NOVUCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌های یک مداح حکومتی:
ترامپ رو هلیکوپترش غیرت داشت، اونوقت رهبر رو زدن هنوز خاکش نکردیم.
چرا راستش رو نمیگید هسته‌ای رو دادید رفت؟ چرا نمیگید هر روز لبنان رو میزنن ولی بازم کاری نمیکنید.
۱۰۰ میلیارد دلار طلب داریم، بعد برای ۱۲ میلیارد دلار مارو کشوندن پای میز مذاکره، تازه نصفشم گفتن ذرت و سویا میدیم.
@withyashar</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/withyashar/16366" target="_blank">📅 00:55 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16365">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd374ffde1.mp4?token=jOBvRH7c1EzpEzPQOp2fCgfzDw5jdwAPRW97Q6xWHIPcxhLOpa3q1emZRfitZFEegqO8_kNsSJ6LP0o_fIruOkj650LC3bFZDQJeXZ1QTDcvWHPzZ0jtCUhNZ7ws3WxNiOKJArwxWANc8vGlqAVae2cigmz7GEVJDEzzWlH1AtEVS79O_-tMDGCClU1FxSlnNGtK7S2tC99g72ZAOB7f4jYMIQx8Qwsp27UKVSoqBgdKRBA_NxWfiYJRKGHP0dPvTQ7hwPYhkeQ5M8R8Q3CfKheYmkNLHWfXWhqFRsbN_rRWmdmBnoDR-o9DpFVyWuEq1rEXlMTgepxoM5yyflqQBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd374ffde1.mp4?token=jOBvRH7c1EzpEzPQOp2fCgfzDw5jdwAPRW97Q6xWHIPcxhLOpa3q1emZRfitZFEegqO8_kNsSJ6LP0o_fIruOkj650LC3bFZDQJeXZ1QTDcvWHPzZ0jtCUhNZ7ws3WxNiOKJArwxWANc8vGlqAVae2cigmz7GEVJDEzzWlH1AtEVS79O_-tMDGCClU1FxSlnNGtK7S2tC99g72ZAOB7f4jYMIQx8Qwsp27UKVSoqBgdKRBA_NxWfiYJRKGHP0dPvTQ7hwPYhkeQ5M8R8Q3CfKheYmkNLHWfXWhqFRsbN_rRWmdmBnoDR-o9DpFVyWuEq1rEXlMTgepxoM5yyflqQBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاستگاری‌جنجالی نوک برج امپایر استیت
دو شهروند روس پس از بالا رفتن از نوک آسمان‌خراش «امپایر استیت» در نیویورک، در همان محل مراسم خواستگاری برگزار کردند، اما پس از پایین آمدن از ساختمان توسط پلیس دستگیر شدند
@withyashar</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/withyashar/16365" target="_blank">📅 00:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16364">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">لحظه ورود تابوت علی خامنه ای به مراسم
،
امشب در حسینیه عمام خمینی
@withyashar</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/withyashar/16364" target="_blank">📅 00:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16363">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">⁨ اتاق جنگ با یاشار : خشک خشک ، از دیدن بشقاب پرنده بگیر تا نرم باز‌ کردن تنگه هرمز
💥
کارای اداری یادتون نره ! برام بنویسین چند وقته منو دنبال میکنید ببینیم ترمیناتور شدید یا نه
😁
⁩
https://www.instagram.com/reel/DaTbNq0x1Pf/?igsh=cmx6bXhnYXB6aTN5</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/withyashar/16363" target="_blank">📅 23:50 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16362">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">بلومبرگ:  ۵۸ میلیون بشکه نفت و میعانات ایران روی آب انباشته شده و ۹۰٪ این محموله‌ها مشتری یا مقصد نهایی ندارند.
با وجود تعلیق ۶۰ روزه تحریم‌های آمریکا، خریداران بزرگ همچنان با احتیاط عمل می‌کنند و خریدها محدود مانده است
@withyashar</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/withyashar/16362" target="_blank">📅 23:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16361">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uz3MJjiQMeQelfD3KdkwT0K6pIzKEFM8MUpjIdPRWOz69t7JluQl-_i4_Yx_QOerwzbfc8Dv6wO2Ac9W-rdiNvpzg9JHyrTGJqtaA5VlD2NZsnfgekRJ_crHd2Dh-LFnMD-tkDTAbTp00f3qBZwmaGOF4k57VZ7r1gZIbdsZjF-uyXUwiZKl5UXmTNgef8u7gcnRarMptfcFuzZ0zUBs3obSfUgSsbnBaPHQX1Qp2QTv62rPIVpvKt-aN-FUPsvuwEMeTZv7ARwwxxOIfn318ag32A3iSdCogHEQdzTaVXOp9jASdtQsMXXlw8Y3PFp2JIEfeybJkVwSbwt4fe2rYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاور پست جدید اتاق جنگ
💥
@withyashar</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/withyashar/16361" target="_blank">📅 23:25 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16360">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">مهران مدیری : با مرد ۳ هزار چهره که دارم میسازم باز به اوج برمیگردم
@withyashar
😐</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/withyashar/16360" target="_blank">📅 23:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16359">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GNkntL6n5Z6NM2Xm0L_vYR0xumdsLa5Ag6hdHhV8pFIsppA4gN5sjGAXw3phnEZdeW20i3TBaGmD3nBVWNagdG4qp0xP0XaPY-5Si6hq5cY7ismvmK8e3YK2c0v720zxVzvJiEOwyAR4W8rg6Sd1CQjjLIV1TMuakdgOGZQBEb4PBjf5hSsazFQ1ICJIH2omVnh82JLP5hlns5vTScm4rO3sbv_uO5WpQX2ufMzvIabphL0wq8RP7zcfauqz01Q4YhMMt1_EFVtmKFH6n_-yWx44tgQC-_Y-bIBlotYKalywLq6Hj7y92FuYRaEhWugVmhFsF5dPmVWz0BgW20Au4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه های عبری در‌سالگرد ۱۰۰۰ روز پس از ۷ اکتبر : آنها بدون هیچ نشانه ای از حیات، در حالی که در آغوش یکدیگر در تخت خواب قرار داشتند، پیدا شدند. یک خانواده کامل که در تاریخ 7 اکتبر به قتل رسید.
ما آن را فراموش نخواهیم کرد و بخشش نخواهیم کرد.
💔
@withyashar
یاشار : اسرائیل درد مارو که ۱۸-۱۹ و کل این ۴۷ سال کشیدیم با تمام وجود درک میکنه و اینارو ول نمیکنه خواهید دید!</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/withyashar/16359" target="_blank">📅 22:53 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16358">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">نیویورک تایمز گزارش می‌دهد که هواپیمای قالیباف پس از آنکه نیروهای امنیتی ایران در مورد اطلاعات مربوط به قصد حمله اسرائیل به آن هشدار دادند، در مشهد فرود اضطراری کرد و مدعی شد که دو جت جنگنده اسرائیلی وارد حریم هوایی ایران در نزدیکی مرز عراق شده‌اند. @withyashar…</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/withyashar/16358" target="_blank">📅 22:50 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16357">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/withyashar/16357" target="_blank">📅 22:43 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16356">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">نیویورک تایمز گزارش می‌دهد که هواپیمای قالیباف پس از آنکه نیروهای امنیتی ایران در مورد اطلاعات مربوط به قصد حمله اسرائیل به آن هشدار دادند، در مشهد فرود اضطراری کرد و مدعی شد که دو جت جنگنده اسرائیلی وارد حریم هوایی ایران در نزدیکی مرز عراق شده‌اند.
@withyashar
🚨</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/withyashar/16356" target="_blank">📅 22:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16355">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mJ58fcbqIJYUH7XeZ2SMMzUGc-Y0fG13e6aPZFNqenx_1Nl6inklnQZkCOyh-uVt86QhYdBoqtn-OPRYvKNmBCENdhjApQOHc0H-OgBacyu_6x79buDgHRITTT3m18uPku8DfsTtthnc91D3KIwS3ssGwmLT9oHH6XjBk7a6ruFEsihfAcfhSxV1O9LZiG8LLyPrX_CXxeyeTHmqtH-_xrDwFMSup2MykpaQ3JCWXPvguMSaK4bvuF6337tQsYcXzmzrvkF_oG2Urswa5nczhoeAF7fYV2WZGMpRLCRcNH6Il6dD1XanrYva-0InJiApPMD6UAejUp1Hbw7S1vo58w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشت گوشتون رو دیدین، بیرون رفتن ما از جنوب لبنان رو هم میبینید.
@withyashar
بنیامین نتانیاهو: تا وقتی تهدید برطرف نشه ما از جنوب لبنان بیرون نمیریم.</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/withyashar/16355" target="_blank">📅 22:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16354">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aBYVc7_uHCW8nMrfchSQy2R8vssVJwAS6jb6QEoPKcfursiqdw1UVaEO44ITgYOTwse47eDDtwkCxAwlhbPvS3fdaHmcTxdx754tao2TbHOWWtbqjXzefL2FwcbgB2glnQZBfYI8l1iJ_9Jgb_Qj1i5MEeJu8teD4u-pb3pE3jgIJj7nnAvyz840KdtgKMhWPMdgWOCTQQ7TAKeyyLlWZHmGLvTd0Q_VDJ-AO66NqTm8Ng_wvjGm-cEOdUcc0WyM5Tdi1XnPOljyfEMI1sBRG9RIHc-pEa39f1PZTHzjnA-RlKRpBhuWcOJIVSYnAa7AYHRu227PWu0e__fYXTFuuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام صفحه مجتبی هم اکنون
من این توفیق را داشتم که پیکر ایشان را بعد از شهادت زیارت کنم؛ آنچه دیدم کوهی از صلابت بود.|  ۲۱/اسفند/۱۴۰۴
@withyashar
دروغ نمیگه تو اون دنیا بدش دیدن همو</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/withyashar/16354" target="_blank">📅 22:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16353">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">وزیر دفاع اسرائیل: ارتش اسرائیل باید برای انجام جنگ مستقل علیه ایران آماده شود
@withyashar
🚨</div>
<div class="tg-footer">👁️ 75.8K · <a href="https://t.me/withyashar/16353" target="_blank">📅 21:25 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16352">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b7b14f43a.mp4?token=DVHYE53KmryMf84xGaik11LCVHVCFnjLlMbIdxYTOOT4fhdTkI5S1cAMQa9WLjkzftGOqupCcz79bXVBZoFRz21O1NivuunHh99qsdqOnahvgoXr06lahSe8Lq-ia2pRRAhgB6-B_mv2RdcvOmHRHJnvAWqikNL9kyvNushvbU5X0XzXJqkaRhHFisVxGSm87pl1SJWcBfi4zBS1sS9tSlxebOZguuRUPSC-gzGvCG-Nw8jOmu43GdWum2dIQZFCGQ0xQAW-OggpTcUTAdJ0W494v4qQHYJUaMqbv4nczrqYbCcNqF4-Yx7LJCRgDv1WG6soTYKV5ap5f0uhkEpxrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b7b14f43a.mp4?token=DVHYE53KmryMf84xGaik11LCVHVCFnjLlMbIdxYTOOT4fhdTkI5S1cAMQa9WLjkzftGOqupCcz79bXVBZoFRz21O1NivuunHh99qsdqOnahvgoXr06lahSe8Lq-ia2pRRAhgB6-B_mv2RdcvOmHRHJnvAWqikNL9kyvNushvbU5X0XzXJqkaRhHFisVxGSm87pl1SJWcBfi4zBS1sS9tSlxebOZguuRUPSC-gzGvCG-Nw8jOmu43GdWum2dIQZFCGQ0xQAW-OggpTcUTAdJ0W494v4qQHYJUaMqbv4nczrqYbCcNqF4-Yx7LJCRgDv1WG6soTYKV5ap5f0uhkEpxrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شبکه 14 اسرائیل قراره سه‌شنبه و چهارشنبه، 16 و 17 تیر مصاحبه ای که با جاسوس های موساد و شاباک تو سپاه کرده پخش کنه
@withyashar</div>
<div class="tg-footer">👁️ 80.9K · <a href="https://t.me/withyashar/16352" target="_blank">📅 20:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16351">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">کامنت جدیدم برای ترامپ. حتماً فقط همین کامنت را لایک و ریپلای کنید. میتوانید با اد استوری ( با نگهداشتن روی  کامنت)، انتشار بیشتری دهید.  https://www.instagram.com/reel/DaSrqH3NjVK/?comment_id=18333946015271080  ترجمه : آقای رئیس‌جمهور،  بسیاری از ایرانیان…</div>
<div class="tg-footer">👁️ 79.2K · <a href="https://t.me/withyashar/16351" target="_blank">📅 20:11 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16350">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">نماینده آمریکا در شورای امنیت: اجازه نخواهیم داد هیچ عوارضی بر تنگه هرمز تحمیل شود
@withyashar</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/withyashar/16350" target="_blank">📅 20:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16349">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PgkAq4ll8vBEHhLzcUp0mJVE8NA1qZ9emGfeARh_Uvm7gPBQgg083RrQa_YpnvzfLAUzOc55QC_-oddCqOsRfrWw9mNLu4-jYZcMsefdns9cQxftdPQaXu7IyXIP3Au0vg3ZkkKTfbYyrLynSftEWUHwigbIG2DdbelbQWJ4Z43TQbuChh_c89GWbCysLzQrELh2GcFTczKNJ5HlC7_aQtYYxTyUzBayPVghJjkrlU_MByg09hUZvveO61hAxZ9FqZp_8etSYLGQwIZTX6ER0epE-qpGFaOvz4zZwOEPRP_NlWlzVNsdIvvO6on5Y-RVXDhi0JnWwQhlaDaFRKpBgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وحیدی؛ فرمانده کل سپاه پاسداران برای اولین بار بعد از جنگ رویت شد. @withyashar</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/withyashar/16349" target="_blank">📅 19:46 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16348">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o7o3l6nnnebqD54SsxGro1ZomnQgPK2wM4uq5rK_8XEQaSX4OqKuSdu5xuGFKHw-zOeObEvYZV5bnR_qamg0XCA9I7w_7S0pDGkOHCKCQC-GwCHEZH-YuFNEurcd0IsnxpleptqIfsbEkhdT1x9h_SS8B2ZW14xGvt0n1HepQNYoxR57Zh_iSC7HGU6B52x-wwd6icNV0KPf6l0LqxuxGnDDghmbcIbjv1GFvL00CeZM6U9mNdVc1Kg6zwR0smY5wUfnl_Fgkc2gAMxp9W9K-GFslV1r-SXAvIjasoXe4cWrbyV5gwe7xr1dYcRaUCnLNpInIoXuEPhA5K1r6qmQoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وحیدی؛ فرمانده کل سپاه پاسداران برای اولین بار بعد از جنگ رویت شد.
@withyashar</div>
<div class="tg-footer">👁️ 77.9K · <a href="https://t.me/withyashar/16348" target="_blank">📅 19:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16347">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">طبق گزارش ها برخی از مقامات ارشد سیاسی و نمایندگان پارلمان عراق از کشور به صورت پنهانی فرار کردند.
@withyashar</div>
<div class="tg-footer">👁️ 76.2K · <a href="https://t.me/withyashar/16347" target="_blank">📅 19:39 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16346">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">وال استریت ژورنال: ایالات متحده به جمهوری اسلامی گفته است ما بخشی از وجوه مسدود شده را آزاد خواهیم کرد، اگر شما از دریافت عوارض در تنگه هرمز صرف نظر کنید. در حال حاضر، تهران این پیشنهاد را رد کرده است
﻿
@withyashar</div>
<div class="tg-footer">👁️ 76.9K · <a href="https://t.me/withyashar/16346" target="_blank">📅 19:15 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16345">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">گزارش ها از استقرار گسترده نیروهای پیاده نظام و توپخانه ایران در مرز با اقلیم کردستان، عراق.
@withyashar</div>
<div class="tg-footer">👁️ 78.3K · <a href="https://t.me/withyashar/16345" target="_blank">📅 19:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16344">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">گزارش درگیری در مهاباد @withyashar
🚨</div>
<div class="tg-footer">👁️ 77.8K · <a href="https://t.me/withyashar/16344" target="_blank">📅 18:58 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16343">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">جان‌باختن شش عضو تشکیلات مخفی حزب دموکرات در کمین سپاه پاسداران در پیرانشهر
بر اساس بیانیه منتشرشده از سوی حدکا، این درگیری در ساعات پایانی شب چهارشنبه ۱۰ تیرماه ۱۴۰۵، در حوالی روستای قزقپان، در سه کیلومتری پیرانشهر رخ داده است. این نیروها هنگام انجام یک مأموریت تشکیلاتی و سیاسی، در کمین برنامه‌ریزی‌شده و سنگین نیروهای سپاه پاسداران قرار گرفتند.
@withyashar</div>
<div class="tg-footer">👁️ 78K · <a href="https://t.me/withyashar/16343" target="_blank">📅 18:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16342">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">پزشکیان: کشته شدن علی خامنه ای آغاز فصلی نوین در جمهوری اسلامی است
@withyashar</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/withyashar/16342" target="_blank">📅 18:44 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16341">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">گزارش درگیری در مهاباد
@withyashar
🚨</div>
<div class="tg-footer">👁️ 79.3K · <a href="https://t.me/withyashar/16341" target="_blank">📅 18:39 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16340">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">این ادعا که «سرکرده حزب دموکرات کردستان به آمریکا گفته در صورت حمله به ایران، ارومیه و آذربایجان غربی به ما داده شود» کاملاً بی‌اساس و فاقد هرگونه منبع معتبر و فیک نیوز است
@withyashar</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/withyashar/16340" target="_blank">📅 18:11 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16339">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">روزنامه بریتانیایی ایندیپندنت : لطف‌الله کاظم افراسیابی شهروند ایرانی-آمریکایی مقیم ماساچوست ، استاد سابق علوم سیاسی که در جریان تبادل زندانیان میان ایران و آمریکا مورد عفو قرار گرفته بود
به دلیل رد شدن گل ایران در جام جهانی شکایت ۱ میلیارد دلاری علیه فیفا طرح کرد
@withyashar</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/withyashar/16339" target="_blank">📅 18:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16338">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">کارشناس شبکه افق، به قالیباف:
این مسیر به جایی نمی‌رسه، حالا دیگه خود دانید
@withyashar</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/withyashar/16338" target="_blank">📅 17:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16337">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-footer">👁️ 79.2K · <a href="https://t.me/withyashar/16337" target="_blank">📅 17:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16336">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">آبدانان</div>
<div class="tg-footer">👁️ 78.8K · <a href="https://t.me/withyashar/16336" target="_blank">📅 17:13 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16335">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">کامنت جدیدم برای ترامپ. حتماً فقط همین کامنت را لایک و ریپلای کنید. میتوانید با اد استوری ( با نگهداشتن روی  کامنت)، انتشار بیشتری دهید.
https://www.instagram.com/reel/DaSrqH3NjVK/?comment_id=18333946015271080
ترجمه :
آقای رئیس‌جمهور،
بسیاری از ایرانیان بر این باورند که صلح و ثبات پایدار تنها پس از پایان حکومت کنونی امکان‌پذیر خواهد بود. از شما با احترام درخواست می‌کنیم هنگام تصمیم‌گیری، این چند نکته را در نظر داشته باشید:
مردم ایران
گرسنه نیستند
(لطفاً به ویدئوی آبادان مراجعه کنید).
بسیاری از ایرانیان از شاهزاده رضا پهلوی به‌عنوان شخصیتی وحدت‌بخش برای یک دوران گذار مسالمت‌آمیز حمایت می‌کنند.
مهم‌ترین اولویت ملی ما، ایرانی آزاد، دموکراتیک و با تمامیت ارضی کامل است. حتی یک سانتی‌متر از خاک میهن ما نباید مورد خدشه قرار گیرد.
لطفاً با آزادسازی منابع مالی یا توافق‌هایی که موجب تقویت این رژیم شود، به آن کمک نکنید.
از توجه مستمر شما به مردم ایران سپاسگزاریم. ما به آینده‌ای بهتر امیدواریم و از تلاش‌ها و حمایت‌های شما قدردانی می‌کنیم
@withyashar</div>
<div class="tg-footer">👁️ 82K · <a href="https://t.me/withyashar/16335" target="_blank">📅 17:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16334">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">وال‌استریت ژورنال: در یک تغییر راهبردی مهم، فرماندهی مرکزی ایالات متحده (CENTCOM) در حال بررسی جدی انتقال بخشی از سامانه‌ها و زیرساخت‌های عملیاتی نظامی خود از برخی کشورهای حوزه خلیج فارس به اسرائیل است.
بر اساس این گزارش، منطقه صحرای نقب  به‌عنوان گزینه اصلی برای استقرار این سامانه‌ها در نظر گرفته شده است.
@withyashar</div>
<div class="tg-footer">👁️ 76.9K · <a href="https://t.me/withyashar/16334" target="_blank">📅 16:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16333">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">استاندار تهران: تمام تلاش ما اینه که مراسم تشییع رهبر بدون تلفات به پایان برسه.
@withyashar
😐</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/withyashar/16333" target="_blank">📅 16:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16332">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ترامپ در تروث : ایالات متحده بیشتر از هر کشور دیگری برای ناتو هزینه می‌کند، و این هزینه بسیار زیاد است، بدون اینکه هیچ سودی از آن ببرد:
آمریکا - ۹۹۹ میلیارد دلار، بریتانیا - ۹۰.۵ میلیارد دلار، فرانسه - ۶۶.۵ میلیارد دلار، ایتالیا - ۴۸.۸ میلیارد دلار، لهستان - ۴۴.۳ میلیارد دلار. سایر کشورها، از جمله آلمان، بسیار کمتر هستند. (۲۰۱۴–۲۰۲۵) مضحک است!
@withyashar</div>
<div class="tg-footer">👁️ 79.8K · <a href="https://t.me/withyashar/16332" target="_blank">📅 15:43 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16331">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">دریاسالار برد کوپر(فرمانده سنتکام): امروز، با افتخار از سربازان و ملوانان آمریکایی که به یک واحد مشترک ضد پهپاد (C-UAS) در بحرین منصوب شده بودند، به خاطر عملکرد استثنایی آنها در سرنگونی ۱۴ پهپاد تهاجمی یک طرفه جمهوری اسلامی در چند هفته گذشته، قدردانی کردم.
@withyashar</div>
<div class="tg-footer">👁️ 79K · <a href="https://t.me/withyashar/16331" target="_blank">📅 15:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16330">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">‏دبیر کل حزب دموکرات کردستان ایران ، مصطفی هجری گفته: ‏حمله زمینی به ⁧ ایران⁩ مطرح است اما پیشروی تا تهران در دستور کار  نیست، اگر شرایط مهیا شود تا ارومیه پیشروی خواهیم کرد @withyashar</div>
<div class="tg-footer">👁️ 82K · <a href="https://t.me/withyashar/16330" target="_blank">📅 15:29 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16329">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">‏دبیر کل حزب دموکرات کردستان ایران ، مصطفی هجری گفته:
‏حمله زمینی به ⁧ ایران⁩ مطرح است اما پیشروی تا تهران در دستور کار  نیست، اگر شرایط مهیا شود تا ارومیه پیشروی خواهیم کرد
@withyashar</div>
<div class="tg-footer">👁️ 81.3K · <a href="https://t.me/withyashar/16329" target="_blank">📅 15:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16328">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">کانال ۱۴ : منابع مستقر در قطر گزارش می‌دهند که ایران در جریان مذاکرات غیرمستقیم و مهم این هفته با ایالات متحده در دوحه، تضمین‌های امنیتی محکمی دریافت کرده است و تضمین می‌دهد که مقامات و فرماندهان ارشد نظامی این کشور در مراسم تشییع جنازه آیت‌الله علی خامنه‌ای، رهبر فقید ایران، هدف قرار نگیرند.
@withyashar</div>
<div class="tg-footer">👁️ 80.2K · <a href="https://t.me/withyashar/16328" target="_blank">📅 15:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16327">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">الحدث : پس از ۱۲۵ روز از کشته شدنش.. ترتیبات استثنایی برای «تشییع جنازه خامنه‌ای»
@withyashat</div>
<div class="tg-footer">👁️ 80.2K · <a href="https://t.me/withyashar/16327" target="_blank">📅 14:30 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16326">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">الحدث : دور بعدی مذاکرات هفته آینده با حضور عراقچی و قالیباف در  در بورگن اشتوک سوئیس براگزار خواهد شد
@withyashar
العربیه: دور بعدی مذاکرات آمریکا و ایران در ۱۸ ژوئیه برگزار خواهد شد</div>
<div class="tg-footer">👁️ 81.1K · <a href="https://t.me/withyashar/16326" target="_blank">📅 13:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16325">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16cdb8cfe8.mp4?token=XV1kvr5EjonYN7LvISLdC14YR8h3iWCBbHZn_inzmXGuIjFE_HDT3Nc0cbyHz3FnZmJ90Njd8qorI6-esSe9_IOg106yhsdP7S9BwOaViv83XlcsHDVnNJjd3iZZCyNPeWt-afcxTBI1kyrGwczzxLVMDjp5OSsgaVznMYU6XXjzeox4trZ1DL7iKIZY7g_xDTc9giFELxHZh1AiCWW-gP9TZlfl5kIjPkfrnxuv_PrQ1pAgQswOdU5LW2YuRrOLCRmUJf-benw-3fLAf_eRCPYJoERuLbRAPzi8QfuNp9-kOvv49lXsnqzzIDjbsd1KR2EzXorZEU1elsVJPdxBrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16cdb8cfe8.mp4?token=XV1kvr5EjonYN7LvISLdC14YR8h3iWCBbHZn_inzmXGuIjFE_HDT3Nc0cbyHz3FnZmJ90Njd8qorI6-esSe9_IOg106yhsdP7S9BwOaViv83XlcsHDVnNJjd3iZZCyNPeWt-afcxTBI1kyrGwczzxLVMDjp5OSsgaVznMYU6XXjzeox4trZ1DL7iKIZY7g_xDTc9giFELxHZh1AiCWW-gP9TZlfl5kIjPkfrnxuv_PrQ1pAgQswOdU5LW2YuRrOLCRmUJf-benw-3fLAf_eRCPYJoERuLbRAPzi8QfuNp9-kOvv49lXsnqzzIDjbsd1KR2EzXorZEU1elsVJPdxBrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : با توجه به داده ها به نظر میرسد کشتیهایی که از مسیر امن آمریکا در نزدیکی عمان رفت و آمد می کنند، نسبت به مسیری که جمهوری اسلامی تعیین کرده بیشتر است.
@withyashar</div>
<div class="tg-footer">👁️ 81.9K · <a href="https://t.me/withyashar/16325" target="_blank">📅 13:13 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16324">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">بلومبرگ:جمهوری اسلامی ایران کنترل مؤثر خود بر تنگه هرمز را از دست داده است.مقام آمریکایی اعلام کرد حمایت نظامی آمریکا و کمک به احیای جریان نفت و تجارت از تنگه هرمز در هفته‌های اخیر به بیش از ۱۰ میلیون بشکه در روز افزایش یافته است.
این افزایش ایران را غافلگیر کرده، توانایی آن برای کنترل ترافیک را محدود و به حملات اخیر اطراف تنگه کمک کرده است.
@withyashar
🚨
🚨</div>
<div class="tg-footer">👁️ 78.9K · <a href="https://t.me/withyashar/16324" target="_blank">📅 13:04 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16323">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">غضنفری نماینده مجلس :
یک کودتا علیه رهبری مجتبی خامنه ای در جریان هست
@withyashar</div>
<div class="tg-footer">👁️ 80.2K · <a href="https://t.me/withyashar/16323" target="_blank">📅 13:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16322">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">امروز صبح، علی عبداللهی، فرمانده "خاتم‌الانبیای" (فرماندهی عملیات مشترک نیروهای مسلح ایران)، هشدار صریحی به اسرائیل و آمریکا داد و از "هرگونه محاسبات اشتباه" در طول مراسم عزاداری خبر داد. او گفت که این اقدام، "واکنش‌های شدید و ناخوشایندی" از سوی نیروهای امنیتی ایران به دنبال خواهد داشت.
@withyashar</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/withyashar/16322" target="_blank">📅 13:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16321">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">وقتی یک ماه پیش من گفتم در روابط عربستان و آمریکا تنش جدی ایجاد شده ، یک اینفلوئنسر تندرو سلطنت‌طلب که شبیه ته نون باگت است، حمله سختی به من کرد.</div>
<div class="tg-footer">👁️ 77.2K · <a href="https://t.me/withyashar/16321" target="_blank">📅 12:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16320">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">نیویورک پست: تنش در روابط عربستان و آمریکا بر سر ایران و نگرانی از جنگ و تهدید منافع نفتی با احتمال بسته شدن تنگه هرمز افزایش یافته است @withyashar</div>
<div class="tg-footer">👁️ 74.9K · <a href="https://t.me/withyashar/16320" target="_blank">📅 12:53 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16319">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">نیویورک پست: تنش در روابط عربستان و آمریکا بر سر ایران و نگرانی از جنگ و تهدید منافع نفتی با احتمال بسته شدن تنگه هرمز افزایش یافته است
@withyashar</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/withyashar/16319" target="_blank">📅 12:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16318">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">یک منبع عبری : سقوط هلیکوپتر روز گذشته آمریکا توسط ایران بود
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/withyashar/16318" target="_blank">📅 12:50 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16317">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">نتانیاهو: ممکن است جنگجویان کُرد ،حملات خود را به غرب و شمال غرب ایران امشب یا شب های بعد آغاز کنند.‌‌‌‌
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 78.9K · <a href="https://t.me/withyashar/16317" target="_blank">📅 12:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16316">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">بعد از حمله به بیت، اعلام کردن منصوره خجسته باقرزاده، همسر خامنه‌ای کشته شده.
اما بعد از اینکه مجتبی پیام تسلیت داد و یادش رفت اسم مادرشو بیاره، خبرگزاری‌ها تکذیب کردن و گفتن زندس!
الان دوباره گفتن کشته شده و قراره همزمان با علی خامنه‌ای، براش مراسم بگیرن.
@withyashar</div>
<div class="tg-footer">👁️ 76.9K · <a href="https://t.me/withyashar/16316" target="_blank">📅 12:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16315">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o0gM4XpF9TiGgy7yLRI_cEF5XXi3s4dfedm48nx6tpw1tifDUDIr16WQqiomYb7EPky9glHfWnuvXkwFnxWpxp6Vb8ijNjhDvrWOu39yrYp6lK2A2pHhuAj0F-uWZPdKsJeOrx_ki2hNJ_5nYmRHOEXpca9TCHmqV0-96ryyMZLhaNpurgm8XxwfFKLOtahDgMwjHOFJN7NJQ0qjWhH1RqA1nncpicIDnKCJbaorH7U4G9osll5CF3veCZzYke3nxrqr5qA4HvhUTX--Tj5wk-ZVjSpm4XK8GxKQevUMzRCR15XQeY8SvMpn1RsfXH4TKVPqlGyyVnIZH0rpnHDtgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمودار سقوط دستمزد و ارزش پول ملی ایران از سال ۲۰۱۰ تاکنون
حالا اگه درامدت دلاری بوده این نمودار برعکس میشه
@withyashar</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/withyashar/16315" target="_blank">📅 12:26 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16314">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">فرمانده  خاتم الانبیا، گفت : «تنگه هرمز زمین بازی آمریکا نیست، بلکه قلمرو حاکمیتی تهران است. همه نفتکش‌ها و کشتی‌های تجاری موظفند فقط از مسیری که تعیین کرده عبور کنند.» آنها بعداً تهدید کردند که «هرگونه عدم رعایت پروتکل‌های ناوبری ایران در تنگه هرمز با واکنش فوری و قاطع نیروهای مسلح مواجه خواهد شد. ادامه حضور جنگنده‌های آمریکایی بر فراز تنگه هرمز، امنیت کل منطقه را به خطر می‌اندازد.»
@withyashar</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/withyashar/16314" target="_blank">📅 12:24 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16313">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">1$ Tether = 178,000 Toman
@withyashar</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/withyashar/16313" target="_blank">📅 12:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16312">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/071529db45.mp4?token=OQ3fz7UXVKk_2j4HTYiqzgCbTbSky3JGL-WWkU_w37V5s7FVwMHVmFakaCRtE9Q8x50goqPiLiFG5OGijs7SFJ_SZk_92sWQE48kTYSN-wdnyKN9oNtH81_ga3s9WlGyaGc413XPmHV0nGw8Hl8tZep5GbDMdN6yJEp9J4dEhH5QmAqdyjL-vq94ofd30cjBfe58oJ3S5RfzQWm18TtMftn8UNFrps1rPcsflbQV5G6F6eVbudQ_DwBmN3fwHf20Iuapu_3A8rjbQwuqS5El263UfGd9R_UMfP40nrCNDDBtDNJS2-u61AhpxSS5Hwu0HbqQoJ8iwW1m_x0MfgRJuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/071529db45.mp4?token=OQ3fz7UXVKk_2j4HTYiqzgCbTbSky3JGL-WWkU_w37V5s7FVwMHVmFakaCRtE9Q8x50goqPiLiFG5OGijs7SFJ_SZk_92sWQE48kTYSN-wdnyKN9oNtH81_ga3s9WlGyaGc413XPmHV0nGw8Hl8tZep5GbDMdN6yJEp9J4dEhH5QmAqdyjL-vq94ofd30cjBfe58oJ3S5RfzQWm18TtMftn8UNFrps1rPcsflbQV5G6F6eVbudQ_DwBmN3fwHf20Iuapu_3A8rjbQwuqS5El263UfGd9R_UMfP40nrCNDDBtDNJS2-u61AhpxSS5Hwu0HbqQoJ8iwW1m_x0MfgRJuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از خودروی حمل خامنه ای رونمایی شد
رئیس ستاد تشییع، وداع و نماز رهبر انقلاب در تهران: شکل کلی خودرو شبیه ضریح حرم امام رضا(ع) است.
@withyashar</div>
<div class="tg-footer">👁️ 76.2K · <a href="https://t.me/withyashar/16312" target="_blank">📅 11:50 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16311">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">پاکستان: مذاکرات غیرمستقیم ایران و آمریکا در دوحه پایان یافت
وزارت امور خارجه پاکستان اعلام کرد ایران و آمریکا در جریان مذاکرات غیرمستقیم دوحه، ضمن دستیابی به پیشرفت‌هایی در موضوعات مرتبط با تفاهم‌نامه اسلام‌آباد، بر سر ادامه گفت‌وگوها توافق کردند.
طبق اعلام اسلام‌آباد، زمان برگزاری
نشست بعدی در اولین فرصت ممکن پس از برگزاری مراسم تشییع رهبر سابق ایران تعیین خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 75.2K · <a href="https://t.me/withyashar/16311" target="_blank">📅 11:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16310">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">یک منبع آگاه:حال روحی آیت الله مجتبی خامنه ای مناسب شرکت در مراسم رهبر انقلاب نیست
@withyashar</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/withyashar/16310" target="_blank">📅 11:23 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16309">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/634f71e520.mp4?token=i6vdfl2us4lrBspXZ98IMzIRw4qcdVOXMaekOPOLkjExeDtS0ZwI-kiFDM8wQScz9AOmYIivVQMyF_QqxG9D2frlWjTzb3YqegXu7V_Ib_MKH5iKGSMtDf74COl9BFR8AQomTjL-g6U6tG6y4MGPfFGwaBJgg58ONyKVusFEwo6PFdAxdLDMi44t-s8UNVMv5GIKHlOo4Eg3-4hsDIIwhTXwT004UZT8LAsyr1yQ6H_5chgQfTPI3xiUiHy1HM8W-wi-to2qjVj-G_kQeK4DIV5U2R7Yqb6WUvzS2kpF9jRYVJus7TtVpvweo1oyI9edRQ3_TU7Jtc_yWCr1WOC-cIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/634f71e520.mp4?token=i6vdfl2us4lrBspXZ98IMzIRw4qcdVOXMaekOPOLkjExeDtS0ZwI-kiFDM8wQScz9AOmYIivVQMyF_QqxG9D2frlWjTzb3YqegXu7V_Ib_MKH5iKGSMtDf74COl9BFR8AQomTjL-g6U6tG6y4MGPfFGwaBJgg58ONyKVusFEwo6PFdAxdLDMi44t-s8UNVMv5GIKHlOo4Eg3-4hsDIIwhTXwT004UZT8LAsyr1yQ6H_5chgQfTPI3xiUiHy1HM8W-wi-to2qjVj-G_kQeK4DIV5U2R7Yqb6WUvzS2kpF9jRYVJus7TtVpvweo1oyI9edRQ3_TU7Jtc_yWCr1WOC-cIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در‌ پست جدید تروث ساخته شده با هوشمصنوعی دکتر می‌شود و بیماران مبتلا به «سندرم اختلال روانی ترامپ» را درمان می‌کند از جمله بیماران وی رابرت دنیرو نشان داده میشود
@withyashar
😂</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/withyashar/16309" target="_blank">📅 11:22 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16308">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78d47807c6.mp4?token=iUK75NnkB6V-YfBuRYdhu8flALp5MlTskmdsj2oQ_vy_TlwDeE30ctYvbrxSBnWFsRf5Hm_bfqMU-6Iua1wl1eDrfW0o3NmnP6FiJbPeGLrWpIJiplnDBvFMhNZJljZ3dBekFiLZ4J56FX_4Sbuc89rh-pSp-KN-uWfUnxeVpOul2DuFTSL9kkwm2AsbpSzY4C9Vlc174L_moM16QUz5IPXj14LA2f9fu8lfErAbqA-w81GwhYzAfMyxvwUiBFy0-o2J6JsxWQq1WSciSzNSCFgTG9x3ZIaeTL8izx08BGLPaOCl1A0rjXFucreEUCmCTMfMLuyXnWhP4zvaAWBoaIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78d47807c6.mp4?token=iUK75NnkB6V-YfBuRYdhu8flALp5MlTskmdsj2oQ_vy_TlwDeE30ctYvbrxSBnWFsRf5Hm_bfqMU-6Iua1wl1eDrfW0o3NmnP6FiJbPeGLrWpIJiplnDBvFMhNZJljZ3dBekFiLZ4J56FX_4Sbuc89rh-pSp-KN-uWfUnxeVpOul2DuFTSL9kkwm2AsbpSzY4C9Vlc174L_moM16QUz5IPXj14LA2f9fu8lfErAbqA-w81GwhYzAfMyxvwUiBFy0-o2J6JsxWQq1WSciSzNSCFgTG9x3ZIaeTL8izx08BGLPaOCl1A0rjXFucreEUCmCTMfMLuyXnWhP4zvaAWBoaIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر ماهواره‌ای از سایت هسته‌ای اصفهان نشان میدهد ورودی‌ها همچنان مسدود هستند و هیچ نشانه‌ای از فعالیت جدید دیده نمی‌شود. گفته می‌شود بخشی از مواد هسته‌ای غنی‌شده ایران در این مکان نگهداری می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 82K · <a href="https://t.me/withyashar/16308" target="_blank">📅 10:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16307">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">سایت The War Zone با استناد به گزارش‌های محلی اعلام کرده است که هر شش بمب‌افکن استراتژیک B-52H Stratofortress حاضر در پایگاه RAF Fairford در بریتانیا، پایگاه را ترک کرده‌اند و احتمالاً به ایالات متحده بازگشته‌اند.
دوازده بمب‌افکن استراتژیک B-1B Lancer همچنان در پایگاه باقی مانده‌اند که این تعداد نسبت به هجده بمب‌افکن استراتژیک قبلی کاهش یافته است
@withyashar</div>
<div class="tg-footer">👁️ 83.9K · <a href="https://t.me/withyashar/16307" target="_blank">📅 10:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16306">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">سقوط قیمت نفت برنت به کانال ۷۰ دلار
بعد از افزایش عبور از تنگه هرمز، قیمت هر بشکه نفت WTI به ۶۷ و هر بشکه نفت برنت نیز به ۷۰ دلار کاهش پیدا کرد
@withyashar</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/withyashar/16306" target="_blank">📅 10:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16305">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">https://t.me/boost/withyashar</div>
<div class="tg-footer">👁️ 89.9K · <a href="https://t.me/withyashar/16305" target="_blank">📅 02:53 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16304">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">گروه
حزب آزادی کردستان ( پاک ) مستقر در منطقه کردستان عراق نیز در بیانیه‌ای اعلام کرد که دفتر مرکزی آن در استان اربیل هدف موشک بالستیک قرار گرفته است.
@withyashar</div>
<div class="tg-footer">👁️ 92K · <a href="https://t.me/withyashar/16304" target="_blank">📅 01:58 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16303">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">کانال 14 اسرائیل: مرکز فرماندهی منتسب به سپاه پاسداران در لبنان توسط ارتش اسرائیل (IDF) تصرف شد
@withyashar</div>
<div class="tg-footer">👁️ 92.8K · <a href="https://t.me/withyashar/16303" target="_blank">📅 01:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16302">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">رسانه های رژیم : در ساعات گذشته دو مقر گروهک های تجزیه طلب متعلق به گروه‌های تروریستی در اقلیم کردستان عراق هدف حمله قرار گرفته‌اند.
بر این اساس، یکی از حملات مقر گروهک تروریستی دمکرات در منطقه کویه را هدف قرار داده و حمله دیگر نیز مقر گروهک تروریستی پاک در منطقه بالکایتی را مورد اصابت قرار داده است.
‎
@withyashar</div>
<div class="tg-footer">👁️ 93K · <a href="https://t.me/withyashar/16302" target="_blank">📅 01:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16301">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">سپاه: در پاسخ به اقدامات گروهک‌های کرد که منجر به کشته‌شدن سه نیروی فراجا شد، یکی از مقرهای این گروهک در منطقه دِیکله (شمال کردستان عراق) هدف حمله قرار گرفت.
@withyashar</div>
<div class="tg-footer">👁️ 91.4K · <a href="https://t.me/withyashar/16301" target="_blank">📅 01:23 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16300">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">گزارش هایی از ارسال تجهیزات گسترده ارتش جمهوری اسلامی به خصوص نیروی زمینی به منطقه غرب کشور
این حجم تجهیزات  بعد از زمان درگیری با داعش بی سابقه هست
@withyashar</div>
<div class="tg-footer">👁️ 91.8K · <a href="https://t.me/withyashar/16300" target="_blank">📅 01:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16299">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">رویترز به نقل از منابع امنیتی عراق گزارش داد یک پهپاد حامل مواد منفجره به اردوگاه یک گروه مخالف کُرد ایرانی در شرق اربیل عراق برخورد کرد.
@withyashar</div>
<div class="tg-footer">👁️ 91K · <a href="https://t.me/withyashar/16299" target="_blank">📅 01:16 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16298">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">گزارش های زیاد از شلیک لانچر در ارومیه
🚨
@withyashar</div>
<div class="tg-footer">👁️ 91.9K · <a href="https://t.me/withyashar/16298" target="_blank">📅 00:44 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16297">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dQrOs9Z66-5hdwbPIafdrwCQpTKJTNeGl1X36ZSeYVjRCy5m3IIFwmzXEpo887GAeF8eOK9qX6EAB5MGlRjochgX7xWefFkyLJStj3bgQm7meJJ0Ot7YLNDK66VHdTfirE6hZIQn3Y8AJQk1a3OUgwaiSdEqwEPR2dElBKFR2bRPnFBFnpKiT7pBPHIBXJ_1HVdl63VLNPf82addMOM8cGDGauc6GD9kZYI5dk5q2B8O2UeGOmyh_su64B6rkplrypjzi1RGebaiJ2vUyZnJyKDZRMIQ-3u-4trGXMF-QMKyfhE6bv1MSs5hSZ8auZzOGk9XGY0opyovttMCcxw0eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق نظرسنجی شورای جهانی طلا از ۶۹ بانک مرکزی، رکورد ۹۰٪ از بانک‌های مرکزی عملکرد طلا در زمان‌های بحران را به عنوان عامل کلیدی در تصمیم خود برای نگهداری طلا ذکر کردند.
@withyashar</div>
<div class="tg-footer">👁️ 91.2K · <a href="https://t.me/withyashar/16297" target="_blank">📅 00:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16296">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc829af2ea.mp4?token=s8unCgRbBIc_04DHpNOq0ICHY1J-8o1ymOvbKF5zHnJS0clMrLqvnBegC60FoSJBiop56w97ADtm86RfXqu7ffSKm8Wp_oy9rXmE0Jl3b7c395hl-a-Pw2Vmw3-_3UfZTuQDLYJtYGqg7Y-LjBGpgB5j2OkhckzrDyCjfwM9GnPLsi6-HwuK_JrZG-Bk2OHBMaZQhEdTOe_22ThjpTMMOYqxrjiDGxko0vEPKvwl7sLBwaF-fW4QgZTITsuIUDlCBIocMSq2RptFldAyZblfHIgZbmf03c7Is8bw4M8FON1CtdHSwwhQmkpr4QDhDs88ZX8ozo_Q1wjWAXEmC6D_UkRxYe58hEKt3nIb5Rbvsta8c5SLHcdzGPgWV0VuKHZUA7ZpC3D7FKjE1K7hTT99RdMv_ff1SV1SrQMY4gyP-CXD3hkiCy9VMehZif1OyESPdST5UKxu74MDEDRTzPsWfN3VrBESeQAm2cBsTtBs8ACjsAKkap7l4y20qfrYQhoHs39BQBa26562Gb5VDLyhND3s-epO5oXudbeFZHECrVDxd_KfZn4b2CxhCDCR0l4LZQTe2DCR3pPtlNaSQZOV5C4IWmzSP3N29qf2Yeln_qOD6SsDwmvCfGaKA7Rt17SpaYOjBPqJVgjBwVUUEb7HtFvPZcFbi5L2HMHu5mLylT8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc829af2ea.mp4?token=s8unCgRbBIc_04DHpNOq0ICHY1J-8o1ymOvbKF5zHnJS0clMrLqvnBegC60FoSJBiop56w97ADtm86RfXqu7ffSKm8Wp_oy9rXmE0Jl3b7c395hl-a-Pw2Vmw3-_3UfZTuQDLYJtYGqg7Y-LjBGpgB5j2OkhckzrDyCjfwM9GnPLsi6-HwuK_JrZG-Bk2OHBMaZQhEdTOe_22ThjpTMMOYqxrjiDGxko0vEPKvwl7sLBwaF-fW4QgZTITsuIUDlCBIocMSq2RptFldAyZblfHIgZbmf03c7Is8bw4M8FON1CtdHSwwhQmkpr4QDhDs88ZX8ozo_Q1wjWAXEmC6D_UkRxYe58hEKt3nIb5Rbvsta8c5SLHcdzGPgWV0VuKHZUA7ZpC3D7FKjE1K7hTT99RdMv_ff1SV1SrQMY4gyP-CXD3hkiCy9VMehZif1OyESPdST5UKxu74MDEDRTzPsWfN3VrBESeQAm2cBsTtBs8ACjsAKkap7l4y20qfrYQhoHs39BQBa26562Gb5VDLyhND3s-epO5oXudbeFZHECrVDxd_KfZn4b2CxhCDCR0l4LZQTe2DCR3pPtlNaSQZOV5C4IWmzSP3N29qf2Yeln_qOD6SsDwmvCfGaKA7Rt17SpaYOjBPqJVgjBwVUUEb7HtFvPZcFbi5L2HMHu5mLylT8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش شبکه آی24: سیا و موساد در طرح استفاده از نیروهای کرد به عنوان بخشی از تلاش گسترده‌ علیه ایران نقش داشته‌اند
@withyashar</div>
<div class="tg-footer">👁️ 91.6K · <a href="https://t.me/withyashar/16296" target="_blank">📅 23:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16295">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ed15951ba.mp4?token=GEuJO82D4KRI_u2gYzJeAcOyaOL157aUEUSGEWFdvbo9CU0Mg5Ie3ozgdYvK3ZM-EdCuxepb9_nohMXNmIwg2ze-2rjYCJzqA1dt6ROV6Qmaiqq-PpotzhFvburT9biRU8Ol0Aud8kGW0hkteXdUROKiTlZxwfCygk4vesKYrUUgqFRU4H41lSH0ari4LkBZSm-93_DA02DqeTfzK7ilyJ9qaU2WolIdT7r2lsiLkJlXuekkErqI_tWKDEgnz4rCjqLfRa2lzsTDah_utGm3gSjZWDBB_6Prtu2d82M5-tg97Sr_fS1CATV0vN0VmO0F0652Cy2d8Sy6aGKFilZp_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ed15951ba.mp4?token=GEuJO82D4KRI_u2gYzJeAcOyaOL157aUEUSGEWFdvbo9CU0Mg5Ie3ozgdYvK3ZM-EdCuxepb9_nohMXNmIwg2ze-2rjYCJzqA1dt6ROV6Qmaiqq-PpotzhFvburT9biRU8Ol0Aud8kGW0hkteXdUROKiTlZxwfCygk4vesKYrUUgqFRU4H41lSH0ari4LkBZSm-93_DA02DqeTfzK7ilyJ9qaU2WolIdT7r2lsiLkJlXuekkErqI_tWKDEgnz4rCjqLfRa2lzsTDah_utGm3gSjZWDBB_6Prtu2d82M5-tg97Sr_fS1CATV0vN0VmO0F0652Cy2d8Sy6aGKFilZp_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: کانال پاناما گران‌ترین چیزی بود که تا به حال ساختیم و همچنین سودآورترین چیزی بود که تا به حال ساختیم. این ترکیب خوبی است.
کمی شبیه ونزوئلا. ما در واقع با جمهوری اسلامی ایران هم به همان اندازه خوب پیش می‌رویم. شاید شنیده باشید؟
@withyashar</div>
<div class="tg-footer">👁️ 91.1K · <a href="https://t.me/withyashar/16295" target="_blank">📅 23:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16294">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">گزارش های زیاد از شلیک لانچر در ارومیه
🚨
@withyashar</div>
<div class="tg-footer">👁️ 89.5K · <a href="https://t.me/withyashar/16294" target="_blank">📅 23:37 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16293">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3b695ead9.mp4?token=C0Xjy328tj0vWqp1zIKtvjzdcpXH6Pqky-DLn8OH2Lo2iIFAnrasM-bhhrLLV6qpNhppAEdC9WDwb9rLyb3_XkxexFV66Iw0DaRPrix0vWpwEIfSyxkac2zO_mly6V49owb-wLHkQlToTtQm7gQXxYtCLTGTXmtDstmeI9wg3WHa0V51pOOCOgczyuweHKaTKjAq102nEo-EsBwYcRG0dBRd5dLoKAx_3sZHRRRvU46u3n3KJSQ253daWCKwa_mGl12JJPiHIhOj2ishA2iKSfvwaD-pDKwFW0NbZYbbA3oXji5rgTzba2I7FEM_BW5gwDytae4Fc5d92HIxvGVuEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3b695ead9.mp4?token=C0Xjy328tj0vWqp1zIKtvjzdcpXH6Pqky-DLn8OH2Lo2iIFAnrasM-bhhrLLV6qpNhppAEdC9WDwb9rLyb3_XkxexFV66Iw0DaRPrix0vWpwEIfSyxkac2zO_mly6V49owb-wLHkQlToTtQm7gQXxYtCLTGTXmtDstmeI9wg3WHa0V51pOOCOgczyuweHKaTKjAq102nEo-EsBwYcRG0dBRd5dLoKAx_3sZHRRRvU46u3n3KJSQ253daWCKwa_mGl12JJPiHIhOj2ishA2iKSfvwaD-pDKwFW0NbZYbbA3oXji5rgTzba2I7FEM_BW5gwDytae4Fc5d92HIxvGVuEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تحلیلگر ژئوپلیتیک چینی: امضای تفاهم توسط ترامپ، فقط برای عبور از گرمای تابستان منطقه است!
۶۰ هزار سرباز آمریکایی آماده حمله زمینی به ایران هستند.
@withyashar</div>
<div class="tg-footer">👁️ 93.4K · <a href="https://t.me/withyashar/16293" target="_blank">📅 22:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16292">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">@withyashar</div>
<div class="tg-footer">👁️ 86.6K · <a href="https://t.me/withyashar/16292" target="_blank">📅 22:44 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16291">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">تحقیق جدید نیویورک تایمز : بیش از دو میلیون سرباز روس و اوکراینی از ابتدای جنگ بین این دو کشور کشته یا زخمی شده‌اند. روسیه بیش از ۱.۴ میلیون سرباز از دست داده است که در میان آن‌ها حدود ۴۵۰ هزار کشته وجود دارد. اوکراین بین ۵۲۵ تا ۶۲۵ هزار سرباز از دست داده است که در میان آن‌ها ۱۲۵ تا ۱۵۰ هزار کشته وجود دارد.
@withyashar</div>
<div class="tg-footer">👁️ 88.1K · <a href="https://t.me/withyashar/16291" target="_blank">📅 22:23 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16290">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z8FTYVz8cpsNrSkipSnBByNG7xto4JpdnUyphnzJ5C-loZwkU_u_HZ66yehxavdWNSfqE10YEYRJhjrBi5OrABbf_bCM16hu5E8dMKG8b0owMSKvL976euQAhENbV4CuYm3Jor7tBZ2wYyw03AI6gvH7KM_WhMp3spayVTsMJVcQUi7ox_cYqnZwBpF69AyzU4px6_S9gm8V-dunQ_Eix7-4TItmYLk-1aUBXjRilyfRJJHt9-xTiRl1aWyZPGKtFT8GYTDottiQp_BzQcnSx7tkKTToe0rVid_E9zujnjQihAeI6oyhI7tB9jmQ-6mXBkBLLtPqmZRBESkSO1BfHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو گروه از کشتی‌های نفتکش/کانتینربر تحت اسکورت هوایی و دریایی ایالات متحده از تنگه هرمز عبور می‌کنند.
@withyashar</div>
<div class="tg-footer">👁️ 87.7K · <a href="https://t.me/withyashar/16290" target="_blank">📅 22:14 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16289">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">سفیر آمریکا: «رابطه واشنگتن و تل‌آویو شبیه یک ازدواج ایده‌آل است که در آن جایی برای طلاق وجود ندارد»
@withyashar</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/withyashar/16289" target="_blank">📅 22:08 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16288">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78447e35bd.mp4?token=A2ksvxEABGR4mBuo-t6fPfq3-HRVG22tzhYLhYbxvsjCbe9zFOZunC4cH2MbEHwuBBsx9waGyRlCNuAmU73mssuwXtlf09arqfhRaBSa-132rsNwtBVr_VExfAMM55lnoGmRiCITcgxmD8wRLtJVxijZGcdLsVhvIkZxzAouFZj46mFkXMQ-JImQ9rFH3gD_oj_jXWOo0w9LaS0IEIaObwwUyRTAB-P5wUZWlypii52xTdEy0BAXtugIPloXSIkA96SgthhXtg7d-FvRm_gdM-uet86UZl1tdYxsi7VqH9p3u7ByAe4jLgqnMJlN40xxhTTnjqLXPNZd7QfLyjGNrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78447e35bd.mp4?token=A2ksvxEABGR4mBuo-t6fPfq3-HRVG22tzhYLhYbxvsjCbe9zFOZunC4cH2MbEHwuBBsx9waGyRlCNuAmU73mssuwXtlf09arqfhRaBSa-132rsNwtBVr_VExfAMM55lnoGmRiCITcgxmD8wRLtJVxijZGcdLsVhvIkZxzAouFZj46mFkXMQ-JImQ9rFH3gD_oj_jXWOo0w9LaS0IEIaObwwUyRTAB-P5wUZWlypii52xTdEy0BAXtugIPloXSIkA96SgthhXtg7d-FvRm_gdM-uet86UZl1tdYxsi7VqH9p3u7ByAe4jLgqnMJlN40xxhTTnjqLXPNZd7QfLyjGNrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاروان پرزیدنت ترامپ توسط سوارکاران خشن (Rough Riders) تا کتابخانه ریاست‌جمهوری تئودور روزولت همراهی شد.
@withyashar</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/withyashar/16288" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16287">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5fcb8e951.mp4?token=ITbpE2wt0vQ2gL6FP7Hke57GdBxedFvZzJdAT8gKvCpEtvMrF0fuaOE8hW6vTBUQsJ3IX2-xqAkKfMpgsbGmQkDURUWqliJpW8GCI2rc5vJIAoPtPlXpq_NG2gAgqMjQMKqV6wA0JwfgwXR0RPSm-ukk1sxhGBCsKyLsZaLdapY7xNl3d6IJz5qDLTtiVbtPzx_D9Z_bPboj_duDy8KEZ7XOw8wMQaZ_wogKcr74ZCbJwfuYQwJMOItlUh3ET8W5atj6Pjs327ba-7Y7YF2C-M5QIUpyVihcm6cgXYLoDLCcMNkZTXrbajwfUyJJEiizDPEt7MtdrD_jhuwxTBBYwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5fcb8e951.mp4?token=ITbpE2wt0vQ2gL6FP7Hke57GdBxedFvZzJdAT8gKvCpEtvMrF0fuaOE8hW6vTBUQsJ3IX2-xqAkKfMpgsbGmQkDURUWqliJpW8GCI2rc5vJIAoPtPlXpq_NG2gAgqMjQMKqV6wA0JwfgwXR0RPSm-ukk1sxhGBCsKyLsZaLdapY7xNl3d6IJz5qDLTtiVbtPzx_D9Z_bPboj_duDy8KEZ7XOw8wMQaZ_wogKcr74ZCbJwfuYQwJMOItlUh3ET8W5atj6Pjs327ba-7Y7YF2C-M5QIUpyVihcm6cgXYLoDLCcMNkZTXrbajwfUyJJEiizDPEt7MtdrD_jhuwxTBBYwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیروز کریمی روی آنتن زنده صداوسیما: قلعه نویی 5 سانت و 10 سانت رو تحمل کرد ولی 30 سانت رو میخواد کجاش بذاره؟!
@withyashar</div>
<div class="tg-footer">👁️ 87.8K · <a href="https://t.me/withyashar/16287" target="_blank">📅 21:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16286">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DLAwBRZNgazMKM26pDF-fO3QzFeGgnRSOz-teAfPef2B74YW5EJJ9-eV4RT1CrnAu1kfJWFzvoUS9tewghMZGyFNaATuty5F-zS8hMG2_giQyJc4oQbNCsEtiWobq0B49rfQLnDfG85AKzAUCe1PpRjLKJzFp5otZWcBkJYqWBW-SV6XtOMUNsX-SFV1xpzBPUuJs5kIdW8o2d7MZk0xJUzIzPGeKQIklZHpkMHOEGE629FwoJUYYSts9w9aVkpFtlkTGxzL0lfFgbuQa-XCu0wEtDmIL2FztA6hYdKOiPSohByVeFJjSTuKOTrh6BQaCmGqschla8PsCNf5U8HzLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدیو ۳پا از به گل نشستن کشتی متخلف «خطر شب‌ ادراری
😂
⚠️
» @withyashar</div>
<div class="tg-footer">👁️ 84.9K · <a href="https://t.me/withyashar/16286" target="_blank">📅 21:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16285">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">جی دی ونس: نمی توانم متعهد شوم که در طول ۶۰ روز به ایران حمله نکنیم.
@withyashar</div>
<div class="tg-footer">👁️ 80.8K · <a href="https://t.me/withyashar/16285" target="_blank">📅 21:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16284">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qVTlcRC3Arg1RWfH22FymFit2zMnwNY6i5fTmY2deV7ZIG9ZtHvZmcn-VJAxC9D6sS09YpqCZdUXkRH_bMU-wxi99M0R5jprnF_ChruA3VSfvRb48v4Ck33_NVNyMt5XFRBFNu6Ggyyy58RY_KdHGuwWSSmiTDI3C7ZWO3C4y7zEpRkXG5EGlmE6I4-bfUmpcJH6JboRiJCJ7VSOVtb7Dm9CkuovHpSSNPJ-pBLrSb4jd5FK70RN_e5zT7TFoWGs0QUdxsoO7GqUUVwyyzUNWJ4t23Jo8jEoWvpeA7BoV47T1n2-BmD3mQCeCGTfvOHn1YzGohXWwcU2LzLr1x7-Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با رسیدن ناو آبی خاکی باکسر به محدوده فرماندهی سنتکام استعداد نیروی‌دریایی امریکا در خاورمیانه افزایش می‌یابد.
استقرار ناو آبی خاکی باکسر احتمال حمله زمینی امریکا به جزایر ایرانی و حتی نوار جنوبی کشور را چند برابر می‌کند.
@withyashar</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/withyashar/16284" target="_blank">📅 21:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16283">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0fcb1fe97.mp4?token=FnvFMl4fmlD7VW3Op8XJhoIEbn80t0YA7_B0jAl9L3urszV8WhpG0kTXHoz39BLnXiMyGRN8cWq4cJg2lagdERwmh2jPojBh7rpv7ZcpEXoxTftVQJCg89vB-VbWmL0zMtt3_Hug2n-ZjxjLjoUY1T5m6xlNILfIg0mWLrL8EoejQPCEX7SU4HYH7tf6zE8YiTTYqLBUujBBqfwQeV5JCmTpxX1Z6dKF3TZtEygFCKcnqGbAakeJ_dqOxvr7t8Ubf17AlOM389ud4__VjEl2eekbzzP9wjyewgTR_0Ipnt9thr0PVEMQkpAuqDBK4k79J5NtIXfziFnQLItPk6BsYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0fcb1fe97.mp4?token=FnvFMl4fmlD7VW3Op8XJhoIEbn80t0YA7_B0jAl9L3urszV8WhpG0kTXHoz39BLnXiMyGRN8cWq4cJg2lagdERwmh2jPojBh7rpv7ZcpEXoxTftVQJCg89vB-VbWmL0zMtt3_Hug2n-ZjxjLjoUY1T5m6xlNILfIg0mWLrL8EoejQPCEX7SU4HYH7tf6zE8YiTTYqLBUujBBqfwQeV5JCmTpxX1Z6dKF3TZtEygFCKcnqGbAakeJ_dqOxvr7t8Ubf17AlOM389ud4__VjEl2eekbzzP9wjyewgTR_0Ipnt9thr0PVEMQkpAuqDBK4k79J5NtIXfziFnQLItPk6BsYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو ۳پا از به گل نشستن کشتی متخلف «خطر شب‌ ادراری
😂
⚠️
»
@withyashar</div>
<div class="tg-footer">👁️ 82.3K · <a href="https://t.me/withyashar/16283" target="_blank">📅 21:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16282">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">گفت‌وگوها با واسطه‌های پاکستانی و قطری در دوحه به پایان رسید، سازوکاری برای جلوگیری از تنش‌ها بین دو کشور ایجاد خواهد شد. تصمیم گرفته شد که بخشی از ۶ میلیارد دلار دارایی‌های مسدود شده برای خرید کالا بر اساس نیازهای ایران استفاده شود
@withyashar</div>
<div class="tg-footer">👁️ 81.3K · <a href="https://t.me/withyashar/16282" target="_blank">📅 20:53 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16281">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-footer">👁️ 78.1K · <a href="https://t.me/withyashar/16281" target="_blank">📅 20:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16280">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">گزارش ها از وقوع انفجار های شدید و تیراندازی گسترده میان ارتش اسرائیل و نیرو های حزب الله در جنوب لبنان.
@withyashar</div>
<div class="tg-footer">👁️ 81.4K · <a href="https://t.me/withyashar/16280" target="_blank">📅 20:37 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16279">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">وال استریت ژورنال: آمریکا در حال بررسی خروج نیروهای خود از عربستان است
@withyashar</div>
<div class="tg-footer">👁️ 81.3K · <a href="https://t.me/withyashar/16279" target="_blank">📅 20:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16278">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">رسانه‌های سعودی درباره نشست دوحه:
ایران خواستار اجرای ۵ بند از یادداشت تفاهم قبل از پرداختن به پرونده‌های دیگر شد
ایران اسرائیل را به مانع‌تراشی در اجرای یادداشت تفاهم با ماندن در جنوب لبنان متهم کرد
ایران بر حاکمیت خود و عمان بر تنگه هرمز تأکید کرد و هرگونه مسیر حمل‌ونقل دریایی در تنگه هرمز بدون اجازه خود را رد کرد
ایران بر اجرای بندهای «دارایی‌های مسدود شده» تمرکز کرد
@withyashar</div>
<div class="tg-footer">👁️ 82.4K · <a href="https://t.me/withyashar/16278" target="_blank">📅 20:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16277">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ارتش آمریکا:
امروز ، ساعت ۳:۳۰ بامداد به وقت شرق آمریکا، خدمه یک بالگرد MH-60S Sea Hawk متعلق به ناو هواپیمابر USS George H.W. Bush در دریای عرب فرود اضطراری انجام دادند.
هیچ نشانه‌ای وجود ندارد که این حادثه ناشی از اقدام خصمانه بوده باشد.
سه نفر از چهار خدمه نجات یافته‌اند و در وضعیت پایدار روی عرشه ناو USS George H.W. Bush قرار دارند.
یگان‌های نیروی دریایی آمریکا در منطقه همچنان در حال جست‌وجو برای یافتن عضو مفقود باقی‌مانده هستند و علت حادثه در حال بررسی است.
@withyashar
🚨</div>
<div class="tg-footer">👁️ 80.1K · <a href="https://t.me/withyashar/16277" target="_blank">📅 20:26 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16276">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">اتاق جنگ با یاشار : در سیزن ۹ اپیزود ۵ کارتون سیپسون ها پخش در سال ۱۹۹۷ پیشبینی شده فینال یک جام جهانی بین مکزیک و پرتقال برگزار خواهد شد ! همه نظرشون اینه که این پیشبینی برای همین جام جهانی است !
@withyashar</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/withyashar/16276" target="_blank">📅 19:30 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16275">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">یک مقام آمریکایی به i24NEWS درباره ادعای آزادسازی ۳ میلیارد دلار از دارایی‌های ایران:
هیچ دارایی منجمد شده‌ای آزاد نشده است و هیچ دارایی‌ای آزاد نخواهد شد مگر اینکه ایران شرایط مندرج در یادداشت تفاهم را برآورده کند.
هر دارایی آزاد شده باید به تأیید آمریکا برسد و برای خرید محصولات کشاورزی آمریکایی برای مردم ایران استفاده شود.
@withyashar</div>
<div class="tg-footer">👁️ 83.1K · <a href="https://t.me/withyashar/16275" target="_blank">📅 19:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16274">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">واشنگتن پست : وزارت جنگ آمریکا در حال آماده‌سازی برای اعزام نیروهای زمینی آمریکا به لبنان است.
@withyashar</div>
<div class="tg-footer">👁️ 85.5K · <a href="https://t.me/withyashar/16274" target="_blank">📅 19:04 · 10 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
