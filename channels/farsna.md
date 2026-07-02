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
<img src="https://cdn4.telesco.pe/file/lLXwe67IM6q4i7_wEk8EmefCQz56-Kpj1Lf9O9W2WspQKQZWCsldUdzuc7CCDCUQuaB8J52mhtscpBf8okUALc9CiW8uTxZ8EBJMY6_QZEGurLYODtEiQ5aSUEUvTaVTBw3pXK8J2Tg5bPGPq_lMw6tT-osUyXNVwhOZxU7wM2MSx9WpMmGkIwXPF1QlgT6xlKqxpg2PdE-Aq27ogBKYRPrbxfxe4NsCSv54w-1Wns0hsUGLFBQnzAse9GoP8AdG8fiTTmCdsNKAJMj4Mzs1m8-OgYVsYzsv-5es8sF50Od6QZ1C6oDFNcv3H7ysF1eUMbSE7y1sM1zmvK_vw2UZ6g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.85M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-11 18:05:51</div>
<hr>

<div class="tg-post" id="msg-446029">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f52aaac282.mp4?token=ObwMeKAOW8tojbDHU2KIrqLDvRMTU79wck6bk51ebX52SHRaqguoxcmh80TtDhK75-lvpYxSAUeOqyqjTXvskj0d0uruAKvELbqnSUkEk9D2axmfvzhnhQrJX29xLCTHbaD1btq3zNnOvMNWe84g5PO45xI6qbHLKGODErHMCSl_ndrcc0Ni20jgDFsu_3k7iQoXXfJ5ziM9aIhfcNu4CP0Pxk3TsPrbr5RO3yXSF5_u8TwILmdWjQicLILJGHZ1AY3UjlrTiwtK1fQ4M0o-gqw7S26JmCyzpta-Rywmw8ngVrNpfTGp3C2Y_9ERUDm72qgvGkFfJ90EZu0MdSlc-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f52aaac282.mp4?token=ObwMeKAOW8tojbDHU2KIrqLDvRMTU79wck6bk51ebX52SHRaqguoxcmh80TtDhK75-lvpYxSAUeOqyqjTXvskj0d0uruAKvELbqnSUkEk9D2axmfvzhnhQrJX29xLCTHbaD1btq3zNnOvMNWe84g5PO45xI6qbHLKGODErHMCSl_ndrcc0Ni20jgDFsu_3k7iQoXXfJ5ziM9aIhfcNu4CP0Pxk3TsPrbr5RO3yXSF5_u8TwILmdWjQicLILJGHZ1AY3UjlrTiwtK1fQ4M0o-gqw7S26JmCyzpta-Rywmw8ngVrNpfTGp3C2Y_9ERUDm72qgvGkFfJ90EZu0MdSlc-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم ایران عزیزانشان را اینگونه بدرقه می‌کنند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 712 · <a href="https://t.me/farsna/446029" target="_blank">📅 18:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446028">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fL1l_B0tH-r1x-SEB5aofBNfi82r_JFa-4a_UHhE0r6ylW7uTKmNOefb4UXPGcTq1TrEGZvj_9UPJISd30nAKUk2bBZ1dGHsuqBI_rkoS1f1XMqimFN_Fb5BFk5e14pYXn6hhlrpbQOS_HTgMtwthaY5g7OcC4xdY3z1_hXnb6Iv2QrOXsYZCkwLOHbnlSvd4j-1acqw7VQBBmgJeTEnS50gbEAp7QtaKqBEPmDZiagWe1A08jN0oOK2yvvSRQ5sh-aDf2V9LZ2e6k1Auv92gA8oBVxuSfpqquubgO0Y06Ea2OVn8sx_FyQhwBx72Tg8DGIXz-iwrQ9DZ582Av4McA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعدام جاسوس و عامل شهادت فرمانده کل قسام
🔹
دستگاه‌های امنیتی نوار غزه از اجرای حکم اعدام جاسوس وابسته به رژیم صهیونیستی خبر دادند که در شهادت چندین فلسطینی از جمله فرمانده کل گردان‌های قسام دست داشته است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/farsna/446028" target="_blank">📅 17:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446027">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🎥
جزئیات حضور مقامات عالی‌رتبۀ کشورها در مراسم ادای احترام و آیین وداع با پیکر رهبر شهید انقلاب
🔹
سخنگوی وزارت خارجه: از صبح جمعه ساعت ۸ صبح مراسم ادای احترام و آیین وداع با حضور تعداد زیادی از شخصیت‌ها و گروه‌های مردمی تا حدود ساعت ۱۲ ظهر برگزار خواهد شد.…</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/farsna/446027" target="_blank">📅 17:30 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446026">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9a3266a08.mp4?token=qZp3p2_PAs7E6eAvsZcd13EwafJrxoUHpRVXDMweyLktQ-mHorvM60luNZgHqLanew3lC-YK9hVjywDpfQKxh0HZnsjEIcjjgQIkepkuHedoEG9Vt7UAcCyWa56UnpTzOI4b5Nqkl9SUIwc34J2J_01ruC5mXvpNFLfGJQzQ65vc3IWr8-WEZ4QSemMFEhtvH6JVTirb1R_ubhIZ9Tu-oysJ6HesCqoymHOMarqjguuS9GTOXdaTn3V-YDvAUsAapPgn0bSEBPbBB_q94Jb0OMlzQmst18SpUJCyc2bL3-RDRiz2JIen0M0uq4GQGmEAW9ZOmkPLy_q5DYEtS5rqmoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9a3266a08.mp4?token=qZp3p2_PAs7E6eAvsZcd13EwafJrxoUHpRVXDMweyLktQ-mHorvM60luNZgHqLanew3lC-YK9hVjywDpfQKxh0HZnsjEIcjjgQIkepkuHedoEG9Vt7UAcCyWa56UnpTzOI4b5Nqkl9SUIwc34J2J_01ruC5mXvpNFLfGJQzQ65vc3IWr8-WEZ4QSemMFEhtvH6JVTirb1R_ubhIZ9Tu-oysJ6HesCqoymHOMarqjguuS9GTOXdaTn3V-YDvAUsAapPgn0bSEBPbBB_q94Jb0OMlzQmst18SpUJCyc2bL3-RDRiz2JIen0M0uq4GQGmEAW9ZOmkPLy_q5DYEtS5rqmoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سردار جوانی: شهید اکبرزاده زبان گویای نیروی دریایی سپاه در جنگ رمضان بود
🔹
معاون سیاسی سپاه: شهید محمد اکبرزاده در طول جنگ رمضان در شهرهای مختلف حضور پیدا می‌کرد و به تشریح پیروزی‌های رزمندگان می‌پرداخت.
🔹
حضور ایشان در آن مقطع، به‌ویژه برای نیروی دریایی…</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/farsna/446026" target="_blank">📅 17:18 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446020">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار استان فارس</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C7-IbwsVEKW7axjvRhgNw8BkdZEv9omb86PGrJPUrQnGKXaP9UqFUsVGzGDhswI8G0nSRGdpXkEt1xnHLAMUb6A2Y07aIR4Lufsb6agYFd3F1lIGDM4YH4TWvXFHgOwItNBvdQCy2QGMdugPXOu34lQGMF56Va_gJIx8M0PLo3BKzWUf9ysgWmoaiAi1bllnPiZZEk_OYCokMmHJzDsBcgdbOpkYoQIAW_E7_yVgTIySipSay9YQzCoEZMj0TBDD19YjKFzyU-6ajrX5zodWSgR2tko3lD67kG4PxmQ9A1zp38gdWmDOND2G7cURjL7r8yt1FwpOJEKq3waoVIQsMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fH3sEDaO5iqgLyFDhQk6EgdA2qHuPGDw-xEe43kfzUmkw4abyLSwje3IQNNXMU7VDZm-N-Rt9RR-GQh46bWbW37znZOAAfs_i9QviWeTEwmRlq-xO3dxsntCw7Vyjvpa3ZHoP-oD5IGSpCq5uX9wv64afo6MO31QSQxumoUfdpSZin9WeGcxmN1XUgwuZCh6jHAnXI1rfIZSku2qrW7foh5M08Yi8EtexEbv4TokUNhFSLItUbNHWdpfFLiog26tjeXhD2oG-9X-jASNEGdlrCkNNeAIalv0AvwA5qtKOfKN4_C7siJq5z-rce0rpI7jmIABJ5r0x5nXEgQ14r1X2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UkueUqTqk0fqQdYqyU7vrfNW_3yc_PqYCZ3UlpHop3Xwvfk7Ngco9A-FeIn7FGhm7rqMMyFZor93vUbSu98MLbhWliOb5YsWyO8ogxW7ddvhpFGJJP3MvjF9OIvQeFvz-WbYkzdKwL-gRS8ZLTNn6161qjqYWzRsa8Q0b98y4cYeqT4guBHJFuzrRT9wkmz-7K8cUbBLrI2Khp8mj0OjK_12Uw8C_kyc_cJHkMDirpz7ur-P2z4_Ao-to44byMDIeJTojIewvnTq87vkpwuMAcptLkej3PvbIZHq675Bc59kSB-Eoi5Hr2KQth0M6hX3fmQ77Q06MMMYiXQlj8YMIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EdX7HkGEMFpjzXd_raOIbS-5HvENliRrxhr4ijjahgdeirxkqWMcDojZcRZSPh00jmm0iq5pfmZREjih_yCaxsthlGBkMI3agOnK5I1N5jdxR3SVQC0T9Pw2_NczOsdkjnfiSl2yAQHq0vYYY_xepG7WvWeGEcWOyzU6SGrB_tvWcqAeqaXYVQo63NhW64jX_2AQ-bPAqChcpjeXET9xDAuQM9xyVmkl1FolADABa3913ej3QTwTGQX7OxZg1SytjG82erWLFDIMJj-jy3KRFGZoOqYEdH0trjhqDcvJoelrmv0MSLMyhnBiCuGx18tWIB_-oslt3WRZb7Yh69cOSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aifnQ8pnha6Nk52oUUzdiV0qPriTHlKjmYh-W73IS9sKJ54znsYijhO-Cyiq4oBUBNug1SCXZWaCW_k4Qb12VsKWeOZhk4vGo9gPwZaoQtR2TuhGPrgdCEcbeaRWoRNxYCGJfF_U3qJ9zK2vsK4d-lNiPjqwRckbcmcUXWs4UCqqK8aZ2bcWAo_CMNaWYSVcNYoCt_uzRFFrE_kF0lLUoe-rIP4usMFce0glSVzL3aZLZIZSnZFCdCd6kUgdKYhP-KnF4bB8GlIHgCBsWO-BQ_mGCVVlVV04Hu5knbDUrjhAxQ_teZAPJnja2El-pZIE5tkJkTIXjyFlcBJpwkmPpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/APh4rdg1VPXC25FUWqfRy8iPi8t37KZ54lYH1hsdcYb3_CNBmA-HxQ9moHDzJurZUIX_FXCGljYL2Q7Z2uwME6yAhKgrO8O1hXr67sEWjsnufAgduLBQB5sxE7V44LsRNLmTBlQdrnlOVJ23AWAPl5ul2d_92HqTw8jYvEN9sbH0bzcvlIC3o2DwusxSyuEjfvET48Zzjnu40XSe8plHFYqfC6_bwQkgGyYjEyVgpTcUb2mNfD3EcqC4GF85Ok8JgTF7x2zt-zl7slyrHx7DIxVofJ6MtSwNKteJx-Vaqeac_iY0ABDHAQUEZ9teaHfzA7RoD8HmepVDBiD7BIRSpA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
قاب‌ها هنوز آن سفر به شیراز را روایت می‌کنند
🔹
در آستانه وداع تاریخی ایران اسلامی با قائد شهید امت، هنوز قاب‌های ماندگار سفر شهید امت در اردیبهشت ۱۳٨۷ به شیراز در تاریخ این سرزمین به نقش بسته است.
عکس:
دریافتی
@farsnews_fars</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/farsna/446020" target="_blank">📅 17:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446019">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ed06b2f9d.mp4?token=J2NVrjnykMjGX7N4ej_F6-GpbHIqShc4bZ104nq4a3dZxZdZDy8gu9eSPrlE3E1Ir90ncSR2l3KD48BuLteAsBHnotwssCr5sGaRTuW_GhnHQOvEU3xYqszgkn2SD74Nit_82WjYKRZvWlgMnrBf8940jAGw38eR8gLmQpLoC7fOjlIQ3H4BGfCXqZdESQINrvHynrpgZuFpQjmxsmJvP_WLtjaW3TVUxYYWlKrJQEDKGAkhwwJq6Mva0nFJtZXYRjWT4Bv7RSFyczr6mhxObHTMQtpI1foskKWD5m5OPxAUOZ02nPGYD-kdRGOwbjUsoB4vWBNcUHmkApSZUyA7XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ed06b2f9d.mp4?token=J2NVrjnykMjGX7N4ej_F6-GpbHIqShc4bZ104nq4a3dZxZdZDy8gu9eSPrlE3E1Ir90ncSR2l3KD48BuLteAsBHnotwssCr5sGaRTuW_GhnHQOvEU3xYqszgkn2SD74Nit_82WjYKRZvWlgMnrBf8940jAGw38eR8gLmQpLoC7fOjlIQ3H4BGfCXqZdESQINrvHynrpgZuFpQjmxsmJvP_WLtjaW3TVUxYYWlKrJQEDKGAkhwwJq6Mva0nFJtZXYRjWT4Bv7RSFyczr6mhxObHTMQtpI1foskKWD5m5OPxAUOZ02nPGYD-kdRGOwbjUsoB4vWBNcUHmkApSZUyA7XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعر افشین علاء در وصف امام شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/farsna/446019" target="_blank">📅 17:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446018">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Apzle_vVDVZm0vs1YWksS1CULuAeVuiWaSeCBbbP4WAapre0BxlYTSLFRXHeq0vpCp2x6-vFRETcwXXI55b5xSAtPLnnY7P_6Z_JLiWT-RlpL6tK9WkRlFjacyvOZ1PlyXxT9qa4fn8WNpDd1s_8QsL-TYs0xUwbndes0__eOgeMoNpZyNyGHKAp3sBtpe6cmYrtEA6PCG1dvmyS20dALv-L0ia6E3UCGEtydiQxeyPJw5B57P5Jp6fAIp4GxbtxE2lF21a7Nclnaz1Dj23Axi0M8JVynF4yiCuKuTAIRL82TuX3DYDACRA6KQfeuuK0_AxrbqS1zVipKahWm2Ncmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روایت بدرقه با شما
🔹
کشور در آستانۀ یکی از متفاوت‌ترین و پرجمعیت‌ترین مراسم‌های تشییع قرار دارد. دل‌های بی‌قرار، شهرهایی که آرام‌آرام رنگ و بوی بدرقه گرفته‌اند و تهرانی که خود را برای میزبانی از خیل عزاداران آماده می‌کند.
🔹
این روزها در شهر شما چه حال‌وهوایی حاکم است؟ اگر میزبان هستید، برای پذیرایی از مهمانان چه تمهیداتی اندیشیده‌اید؟ و اگر راهی تهران هستید، از آمادگی برای این سفر، تصاویر کاروان‌ها و حال‌وهوای شهر خود برای ما بنویسید و عکس‌های خود را با دیگر مخاطبان فارس به اشتراک بگذارید.
🔹
شما می‌توانید روایت‌ها، تصاویر و ویدئوهای خود را با هشتگ
#روایت_بدرقه
در فارس تعاملی منتشر کنید، از طریق پیام‌رسان‌ها به نشانی‌های
@Interactive_Fars
و
@fars_ma
ارسال نمایید و یا در پایگاه اینترنتی
https://revayat-badraghe.khamenei.ir
ثبت و بارگذاری کنید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/farsna/446018" target="_blank">📅 16:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446017">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">درگیری عوامل انتظامی با تیم سارق مسلح در زاهدان
🔹
فرماندهی انتظامی سیستان‌وبلوچستان: لحظاتی قبل، عوامل انتظامی با یک تیم سارق مسلح در خیابان بزرگمهر وجانبازان زاهدان درگیر شدند.
🔹
در این درگیری مسلحانه ۳ سارق مسلح به هلاکت رسیدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/farsna/446017" target="_blank">📅 16:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446016">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔴
انفجار در دمشق
🔹
رسانه‌های سوریه از زخمی شدن تعدادی در پی انفجار داخل یک کافه در پایتخت این کشور دمشق خبر داده‌اند.
🔹
خبرگزاری رسمی سانا گزارش داد که انفجار در منطقه حجاز دمشق رخ داده و ماهیت آن در دست بررسی است.
🔹
تلویزیون سوریه: این انفجار در منطقه حجاز…</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/farsna/446016" target="_blank">📅 16:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446015">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iRvEqwcNmHnCOyOC9A-t02-jSEkaieooYBZO96PCk_7jp6lHD_KcYUUHqzHeexbBVVqTFa2mXle8kX9md8alclQmvah3CufLLyhPmMyXhtD5JDFe0TKDXXfqkqbiuDv9xrTQcHjn191OsfJI7yC2V5VaiXBxasbBDWi7S-0RQ8Q2zoMmLg3mZh1_aGejH1H4ZrsnZdNjLhRDYhZ-i4TyGMNNnxdSOFYcpk-H-ktDjiM0lA2eCXheEtb7maQ8nv6fzqcLQUN_1mr842Q5teEBZGb9xQr1ncb8Jk1xJnvqptoN3JSBpvi5te-gDNSizpt6xL4S9MTITaARlWYI_bHyAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
جلسۀ ستاد برگزاری آیین تشییع رهبر شهید انقلاب به ریاست رئیس‌جمهور  @Farsna</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/farsna/446015" target="_blank">📅 16:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446014">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3e2e685bf.mp4?token=gEhs4Efj5bl-xiyZY3dL3pgmojxmKocG1rHgmolItnljxykcB_yG1vToRmUY-I-oBiGQT8cnJyXUxkh_IQ7IVDkCr1mQn15u8hNOTmAzJAzfjoXdG4gg3WwpYq3QTlxH87nLm7cqNUHRsnKkz1P-mQokuOpgY1p4qIm7ILBD1fz2ZRp7c8B5BvRI46fQJlIrFQ3XAsctqL1D0JmNLGCvdc-S6r2TrekgekSKOJtRKoBSMTBcXt1nPw36ygFFBZfS00Q8NexiZo9ecDn6vygRTmHBi0HTwbecHDg9J3ZpclC9Nhba4urDRCmgLr915Qqhz4XoO8_voc1CBnMn8d4pDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3e2e685bf.mp4?token=gEhs4Efj5bl-xiyZY3dL3pgmojxmKocG1rHgmolItnljxykcB_yG1vToRmUY-I-oBiGQT8cnJyXUxkh_IQ7IVDkCr1mQn15u8hNOTmAzJAzfjoXdG4gg3WwpYq3QTlxH87nLm7cqNUHRsnKkz1P-mQokuOpgY1p4qIm7ILBD1fz2ZRp7c8B5BvRI46fQJlIrFQ3XAsctqL1D0JmNLGCvdc-S6r2TrekgekSKOJtRKoBSMTBcXt1nPw36ygFFBZfS00Q8NexiZo9ecDn6vygRTmHBi0HTwbecHDg9J3ZpclC9Nhba4urDRCmgLr915Qqhz4XoO8_voc1CBnMn8d4pDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرمانده سپاه تهران: آماده‌سازی خودروی حامل پیکر مطهر رهبر شهید به پایان رسید.  @Farsna - Link</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/farsna/446014" target="_blank">📅 16:26 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446013">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-text">استقرار ۴ بیمارستان سیار نیروی زمینی سپاه برای خدمت به زائران رهبر شهید
🔹
معاون بهداری رزمی نیروی زمینی سپاه پاسداران در گفت‌وگو با فارس: چهار بیمارستان صحرایی تخصصی در شهرهای تهران، قم و مشهد مستقر شده است.
🔹
دو بیمارستان صحرایی ۲۸ تختخوابی در تهران و قم و دو بیمارستان صحرایی ۶۴ تختخوابی در مشهد مستقر شده‌اند. همچنین ۲۵ پست امداد سیار و ۴۰ دستگاه آمبولانس نیز در کنار این بیمارستان‌ها برای ارائه خدمات درمانی و امدادی فعالیت می‌کنند.
🔹
بیمارستان‌های صحرایی مستقر، از تمامی بخش‌های تخصصی و فوق‌تخصصی شامل بخش‌های بستری، CCU، ICU، اتاق عمل، رادیولوژی و کادر درمانی مجرب برخوردار بوده و تمامی تجهیزات مورد نیاز را به همراه دارند.
جزئیات فعالیت‌ها و خدمات را
اینجا
بخوانید.
@Farspolitics</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/farsna/446013" target="_blank">📅 16:23 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446012">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5b5a61604.mp4?token=PgdX-KEKUK4kQGzkcG9tO0EvTjKB4iJWAQECfp-dmWh9eEylnUBIUPrVnKfB8D0DOWH4ItnHB1h03L7YCSSv2tn686DCDBHUonP2nuZDYurHWB1wsN0pO0FuaCCgFR05AaxllCJ7lQNONasxkoaZ0qvB-x939_0qZ5E4cKMjSwK_qWqoavAN2958Oo77fWb1nntVP92ZX5LqEwIPZiB6jDPaA_yOfJv_hQmsyPLil85l9j-JFiPtUAID1AozmeowG7cfYSVAjGoTypxkYcoFLIG8Ufywf8-weM6-yYVIvr30VjUB5Bk_ZnEt37zi2VWmOlDvB1XdhmcbOob1FkdRcjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5b5a61604.mp4?token=PgdX-KEKUK4kQGzkcG9tO0EvTjKB4iJWAQECfp-dmWh9eEylnUBIUPrVnKfB8D0DOWH4ItnHB1h03L7YCSSv2tn686DCDBHUonP2nuZDYurHWB1wsN0pO0FuaCCgFR05AaxllCJ7lQNONasxkoaZ0qvB-x939_0qZ5E4cKMjSwK_qWqoavAN2958Oo77fWb1nntVP92ZX5LqEwIPZiB6jDPaA_yOfJv_hQmsyPLil85l9j-JFiPtUAID1AozmeowG7cfYSVAjGoTypxkYcoFLIG8Ufywf8-weM6-yYVIvr30VjUB5Bk_ZnEt37zi2VWmOlDvB1XdhmcbOob1FkdRcjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آموزش‌وپرورش: امتحانات نهایی به‌هیچ‌وجه به تعویق نمی‌افتد
🔹
رئیس مرکز ارزشیابی آموزش کشور در برنامه پرچمدار: آزمون‌های نهایی طبق برنامه برگزار می‌شود.
🔹
امکان برگزاری آزمون‌های نهایی پس از کنکور وجود ندارد.
🔹
در نیمه اول شهریور نتیجه امتحانات نهایی به سازمان…</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/farsna/446012" target="_blank">📅 16:16 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446011">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea1c88eb50.mp4?token=DjaWSo3AyL7eRQltpAOS4ZEGZOivdwUIbh3uonBX4RCRcC4ZspWNi_gRj-2A4tyQNMTQnWnT1qVPvTQu2JMWF8j8lSI7QXeTY1Wu8bpiunWdaNiopWW7B49Pej6OITRvgfnRHaBiUkjACXqX03A6Z8V4jYwUvj1vxF9tdlr_3vdeqH8AdyyPt-_UOXnlUm_w1gQPlcKCL3OO1TonFjPOkZnqhrj34gd1lniBd-96OLZiLq2BwHkOR0931M-V9DUSO4qASoz9_B2kBsCjAxGsZoPmz0Ch2PCNnsTo8ULoLBs3XDtUY5LDpVSrwmYdaU-ih5_74wvOsOfQx19FkJY17Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea1c88eb50.mp4?token=DjaWSo3AyL7eRQltpAOS4ZEGZOivdwUIbh3uonBX4RCRcC4ZspWNi_gRj-2A4tyQNMTQnWnT1qVPvTQu2JMWF8j8lSI7QXeTY1Wu8bpiunWdaNiopWW7B49Pej6OITRvgfnRHaBiUkjACXqX03A6Z8V4jYwUvj1vxF9tdlr_3vdeqH8AdyyPt-_UOXnlUm_w1gQPlcKCL3OO1TonFjPOkZnqhrj34gd1lniBd-96OLZiLq2BwHkOR0931M-V9DUSO4qASoz9_B2kBsCjAxGsZoPmz0Ch2PCNnsTo8ULoLBs3XDtUY5LDpVSrwmYdaU-ih5_74wvOsOfQx19FkJY17Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اطلاعیهٔ جدید آموزش‌وپرورش: برنامهٔ برگزاری امتحانات نهایی بدون هیچ‌گونه تغییر اجرا می‌شود.  @Farsna - Link</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/farsna/446011" target="_blank">📅 16:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446010">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">دعوت فرمانده کل ارتش از عموم ملت ایران برای حضور در مراسم بدرقۀ پیکر مطهر فرمانده شهید کل قوا
🔹
ملت شریف، پرافتخار و داغ دیده ایران؛ شهادت قائد ملت، امام امت و فرمانده مجاهد و معظم  انقلاب اسلامی، حضرت آیت‌الله العظمی سیدعلی حسینی خامنه‌ای، (رضوان الله تعالی علیه)، آن بزرگمرد صبر و مقاومت، به دست دشمنان کینه‌توز، آمریکای جنایتکار و رژیم غاصب صهیونیستی، داغی عظیم بر قلب ملت ایران، مسلمانان جهان و آزادگان عالم گذاشت. دشمنان قسم خورده ملت ایران، در اوج خباثت، گمان می‌بردند با این جنایت می‌توانند اراده ملت بزرگ ایران را در هم بشکنند و روح مقاومت را از این سرزمین جدا کنند اما نه تنها به هیچ‌یک از اهداف شوم خود دست نیافتند، بلکه ملتی مصمم‌تر و متحدتر از گذشته را در برابر خویش یافتند.
🔹
رهبر شهید وفرمانده معظم کل قوا، در تمامی سال‌های پرافتخار حیات خویش، الگویی کامل از شجاعت، بصیرت و پایمردی در برابر زیاده‌خواهی استکبار جهانی را به کلیه آزادگان عالم ارائه داد. آن مجاهد بزرگ تا واپسین لحظات عمر پربرکت خود، خط مقاومت را با شجاعت و بصیرت پاسداری کرد و هرگز در برابر تهدیدها و فشارهای دشمنان، از راه حق کوتاه نیامد تا میراثی گران‌بها از ایستادگی و مقاومت، به جای بگذارد، میراثی برای همه ملل آزاده جهان که هرگز فراموش نخواهد شد.
🔹
اینک بر ماست که با حضوری باشکوه، متحد و آگاهانه در مراسم وداع و تشییع پیکر مطهر آن رهبر شهید، پیمان دیرینه خویش را با راه ایشان و آرمان‌های انقلاب شکوهمند اسلامی، تجدید کنیم. این حضور، پیامی روشن به دشمنان دارد و به استکبار جهانی، یادآوری می کند که راه آن رهبر و فرمانده شهید، با اراده فولادین ملت ایران و در سایه رهبری خردمندانه جانشین شایسته ایشان، حضرت آیت‌الله سید مجتبی حسینی خامنه‌ای، با قدرت ادامه خواهد یافت.
🔹
اینجانب، به نمایندگی از کلیه همرزمان خویش در ارتش سرافراز و مقتدر جمهوری اسلامی ایران، از عموم مردم شریف، خانواده‌های معزز شهدا، رزمندگان و همه دلدادگان مکتب مقاومت دعوت می‌کنم، با حضوری حماسی و تاریخ‌ساز، قائد شهید ملت و همراهان شهیدش را بدرقه کنند و بار دیگر به جهانیان نشان دهند که ملت ایران، در برابر دشمنان تسلیم نخواهد شد و تا آخر ایستاده است.
@Farsna</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/farsna/446010" target="_blank">📅 16:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446009">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FzPwQUDxeW84w8hl_24U-V6rznYD98HSMgQFcrfPkr6JAdFu4sVoBpJt0XDNOq1hxK0HlV8KZb6OX4qMTgseEgHN5Enq5s1ZwCahfc3Bv71MW6xSp9uqAZZfyXCXiNV8-3tk9gVR67vo05uhX2RyDn1t557j0BQ4pj86BvHYeVWkuCRhRkumtI94C-fqhnriE1KrcXI4qtNVWnWs6LcWTUy7ylipgrUxsBnmXNz2SFjvB9d25rB4DZDxMJVL_Nhg6z4JEnnWnOafb5txINCgfOxcxexMw3fDMhTWK6sbfrzvBm-fJmi6QUcwYurvPbpByoOcJdIw5oS2LapBCKms9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرنگی‌کاران جوان ایران قهرمان آسیا شدند
🔹
تیم ملی کشتی فرنگی جوانان ایران عنوان قهرمانی زودهنگام رقابت های آسیایی تایلند را از آن خود کرد.
🔹
در جریان رقابت‌های ۵ وزن نخست کشتی فرنگی قهرمانی آسیا در تایلند، نمایندگان ایران صاحب ۳ مدال طلا و ۲ برنز شدند.
@Farsna</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/farsna/446009" target="_blank">📅 16:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446008">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89260fdff2.mp4?token=MAJx9EIPEI0BYRGMvCyCUrvOScCZVJgUO4vxNyo4u6_Ii7NiUwfwLhKBYrnKehj2gFMDlCft_BTbnWJBGGudgQdvSXn68r7sVbpNJ3VlCSmGiVKV2f1KxEZk9vLimWm2hKgbT4b25v4cU8ggNe76u1WQiST1h6mSPHCg3tQJymZTLZdXuj0MpYlUFjSqgdfrRAJScmVoKkgoUTnXYXewjh6gRTj2_sotrsMpdh6gHx8xiWf67XtmThNDsfjUlsh_P-7Ym1oIsXODWs7-hVPmKsynVy26fkjU-zuglFczHw-qx_4N75SULqi3hfgC7tnmtSF8l4RjJskvw_whnLxSaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89260fdff2.mp4?token=MAJx9EIPEI0BYRGMvCyCUrvOScCZVJgUO4vxNyo4u6_Ii7NiUwfwLhKBYrnKehj2gFMDlCft_BTbnWJBGGudgQdvSXn68r7sVbpNJ3VlCSmGiVKV2f1KxEZk9vLimWm2hKgbT4b25v4cU8ggNe76u1WQiST1h6mSPHCg3tQJymZTLZdXuj0MpYlUFjSqgdfrRAJScmVoKkgoUTnXYXewjh6gRTj2_sotrsMpdh6gHx8xiWf67XtmThNDsfjUlsh_P-7Ym1oIsXODWs7-hVPmKsynVy26fkjU-zuglFczHw-qx_4N75SULqi3hfgC7tnmtSF8l4RjJskvw_whnLxSaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
انفجار در دمشق
🔹
رسانه‌های سوریه از زخمی شدن تعدادی در پی انفجار داخل یک کافه در پایتخت این کشور دمشق خبر داده‌اند.
🔹
خبرگزاری رسمی سانا گزارش داد که انفجار در منطقه حجاز دمشق رخ داده و ماهیت آن در دست بررسی است.
🔹
تلویزیون سوریه: این انفجار در منطقه حجاز دمشق در نزدیکی کاخ دادگستری  رخ داده است.
@Farsna</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/farsna/446008" target="_blank">📅 15:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446007">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">اطلاعیۀ قرارگاه برگزاری آیین وداع و تشییع رهبر شهید انقلاب در تهران
🔹
۱. حضور وفاداران به آرمان‌های انقلاب اسلامی‌ و ولی امر شهیدمان در مراسم وداع و تشییع بی‌شک بزرگ‌ترین اجتماع تاریخ بشری را رقم خواهد زد که چشم جهانیان را خیره کرده و موجب تسلای قلب حضرت ولیعصر خواهد بود.
🔹
۲. خادمان شما در همۀ سازمان‌ها و رده‌های مختلف‌ نهایت تلاش و آمادگی خود را به‌کار بستند تا بستر مناسب برای حضور زائران گرامی ‌را در مراسم وداع، برگزاری نماز و تشییع رهبر شهید انقلاب آماده شود و چندین شبانه‌روز است که همه امکانات لازم برای این امر بسیج شده است.
🔹
۳. هموطنان عزیز تا حد امکان برنامه سفر خود به تهران را به گونه‌ای مدیریت کنند که از حداکثر ظرفیت اسکان و ارائه خدمات به زائرین در تهران استفاده شود به عنوان مثال سفر را کوتاه کنند تا تعداد بیشتری از مشتاقان شرکت در مراسم بتوانند حضور پیدا کنند.
🔹
۴. مبادی و جاده‌های ورودی به پایتخت همواره باز است و هیچ‌گونه منعی برای ورود وجود ندارد.
🔹
۵. زائران گرامی ‌اخبار و اطلاعیه‌ها را از مراجع رسمی‌پیگیری کنند و به‌ویژه مراقب شایعات و اخبار جعلی باشند.
🔹
۶. پیش‌بینی و توجه به محدودیت‌های ترافیکی در سطح شهر تهران و حفظ آرامش در هنگام حرکت همواره توصیه می‌شود تا برنامه‌ریزی حضور هم وطنان دچار اختلال نگردد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/farsna/446007" target="_blank">📅 15:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446006">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bd8fcf393.mp4?token=ao3PW5REuC8nvyL9kV-ds4t9I2SAlAbnmmwrS-p1qYM3I2crnBvA8CfxiDKW6vo2vm5JjjS4qS7J6Kpnboi7H6nXDPRpiz9TCGF6BSjoIS9QyVxrR9x6Ls5hFtl0Hm4baJ3xBPGKUSxt_gvcGdZWbUGTAX0nUTmlGUmYkoMAkIw-7OhR_sLdQVk7Vlc0tmy-6FSLH37v4kkd-CW15j23Rx-cGwHTQAiZqGGPdfC7uV1--TKxBRuzGzNUGi1gJjJkSw3RtQsmnjp6cy5njCR1bXLSOyOdCr6dl3YM58KmjHYzJLmvL0coZZhjCfqjU8wM9IE1F7SNVra4AR8v1EcSF31tajRl6WpSOt__ZDJPNM7rISHi2AFqokOZRBSilTCePQTxYXjl8wtJeYOsSdw1sQV49PWf_gfqxFdlAM-lYhgHUZOH4VtgSSU28DZTjbJR4mcxhhVrXF-rQGf3mOmyN2K8b5C8qClGhH49Vl4hJvCUEEqCz9QPxJyy_lemQS27qSi9dCFzf4yeR2rmvbNFjKGUQH6wQHhaIhkG0mazFYZflLkYg8r_Cv90ZMhlBKz_vwajCM_bk-XwAPLCiRwHqOIEui93GJa2Qiq-JuACaT571BtoI6EhPc05SKjyi7R2qjyJJGikplF54Fc_5YS9-7PSd748PSLNMzp6abVdZY0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bd8fcf393.mp4?token=ao3PW5REuC8nvyL9kV-ds4t9I2SAlAbnmmwrS-p1qYM3I2crnBvA8CfxiDKW6vo2vm5JjjS4qS7J6Kpnboi7H6nXDPRpiz9TCGF6BSjoIS9QyVxrR9x6Ls5hFtl0Hm4baJ3xBPGKUSxt_gvcGdZWbUGTAX0nUTmlGUmYkoMAkIw-7OhR_sLdQVk7Vlc0tmy-6FSLH37v4kkd-CW15j23Rx-cGwHTQAiZqGGPdfC7uV1--TKxBRuzGzNUGi1gJjJkSw3RtQsmnjp6cy5njCR1bXLSOyOdCr6dl3YM58KmjHYzJLmvL0coZZhjCfqjU8wM9IE1F7SNVra4AR8v1EcSF31tajRl6WpSOt__ZDJPNM7rISHi2AFqokOZRBSilTCePQTxYXjl8wtJeYOsSdw1sQV49PWf_gfqxFdlAM-lYhgHUZOH4VtgSSU28DZTjbJR4mcxhhVrXF-rQGf3mOmyN2K8b5C8qClGhH49Vl4hJvCUEEqCz9QPxJyy_lemQS27qSi9dCFzf4yeR2rmvbNFjKGUQH6wQHhaIhkG0mazFYZflLkYg8r_Cv90ZMhlBKz_vwajCM_bk-XwAPLCiRwHqOIEui93GJa2Qiq-JuACaT571BtoI6EhPc05SKjyi7R2qjyJJGikplF54Fc_5YS9-7PSd748PSLNMzp6abVdZY0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
«دکتر ترامپ» برای منتقدانش نسخه پیچید
🔹
رئیس‌جمهور آمریکا در شیرین‌کاری جدید خود با هوش مصنوعی، این بار در نقش پزشکی ظاهر شد که منتقدان سرشناسش را درمان می‌کند.
🔹
این ویدئوی حدود ۹۰ ثانیه‌ای که در حساب کاربری ترامپ در شبکه اجتماعی «تروث سوشال» منتشر شد، شامل اظهارات ساختگی منتسب به شماری از چهره‌های سرشناس رسانه‌ای و هالیوودی است که از منتقدان ترامپ به شمار می‌روند.
🔹
ویدئو با تصویری از ترامپ آغاز می‌شود که با لباس پزشک از مخاطبان می‌پرسد «آیا شما یا یکی از اطرافیانتان به سندرم ترامپ‌هراسی مبتلا شده‌اید؟» سپس می‌گوید «علائم این بیماری می‌تواند بی‌وقفه ادامه داشته باشد. خوشبختانه، من دکتر ترامپ هستم و برای آن یک برنامه درمانی دارم».
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/farsna/446006" target="_blank">📅 15:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446002">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nm4hM1_DYSx5sTYZjAHFZQjIHvIQPMBZ9OEwOTF4c9K_C51g1SYuBWme-w0jBLDcTGTpK9QewDxhn2n7G33W5fyh6uYme17VKJK3DkKZf_hmOcWM8cH2Se-pfYJDEqpJE62n8xh8QTH4MAGOdwkGHjBevjVFmCVX4DHU3zdts6tQ_R0mn6KGIjuTnz5-JcHvrKRwiYEqHHw7ZQpXlJLSeh1nPvvVhplTAAyfYmdhEjwNMFHIU8_jhn5nWzz-PnVrmH8tfMwWC_MN--qmLGO7ja1TzfzGEsFJbd4JLV3E_PdSqL3Bo8pvezauIXf38kX3rYTuDALf3d1g53s-o3mtpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Znpuwv-0aaSm2W5t43QcdJjhEW18weltkGeYKJr6K4mocJcZzLjWJ15yzygR2NxyGyyLfjYVuHa-C-H166hdr3uuXmywIXZjspjwdl91kv2Vc2x8DMeP0QNwiNbbHsAwGwdj606heuI4gb24l_Oa66dIqz23ZZYJEGnkddFLDccGEP3K0n5QNvBGMwVQGK80eFUIUcfbCt1mAZMO_muJV7-asb3NZ3qj38GSqpzMcJYhPi6oQh7kembJ0C-gXyVB0Wu5zyk4FcQM8HHTHh85NBmssq0VqMSrUpxoQO2w1ob6bkzHctOyKI3py0O4RLxYRGEwz8VrI9mmcGIgV2n6-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PclGfc4LlEBV51ZkqXwwXMbU01whcIzVHCe01nhRmWIoRGUbRSAmlOXRx6GcAlL1iDO0Mkrt3dMoEVFthxDS_xEEt0Ggr8sDRzyyREwyPc7VaVZoRn7o_I0UDI-wPJ7aCz4hG5gA3zxl7PGStHu9F_trXg6yGolvIboiMBSJVQxBFUy4fr70_0KILFojSkvYVlknT1sNho0fPBTComTMX1DXFPxttVeghia__McpU2lZcelEnAD-EoEl_t8XnL9RSlHayr1UHZFZ3sD1bSilUU3v8U1DK1PJp-w3R6jp-NVMeUbJpJdc9qfV8dBdooBe-YHdLn2eV51V6spGWlAPFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CRlwYWWsQ6Sq5jRYnZZFpJJh6nuUP5Ik8blW-OuNMBc9UMgkBHeKxBhAYtQUGPdUrFi4WRDL2o2t8B4GYeEhFcdz9gE21vZCkSTJxRvXS4QQHw5Bb9OXSo6Leqz6AEXAOSk_QO7oI7oM30io0uKoJ69FoHAvC3fxHLV9Ih3qAn4eQdOrwkfYe7pgzsc8wSvEjkBtRvM_VD064QnWUGZgDLAfyc4nd_R86jUTJD-Irl4m27MKWb8gvNI41LajNdRY3sJvIpCs0FECo7yQYJGiB_evF5YJWYy6GdfSGfJcZFHraWlN5S-mrWRDmeOZDfs9q1m7BYsQ2PLxJx-QK0oiDw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
جلسۀ ستاد برگزاری آیین تشییع رهبر شهید انقلاب به ریاست رئیس‌جمهور
@Farsna</div>
<div class="tg-footer">👁️ 7.8K · <a href="https://t.me/farsna/446002" target="_blank">📅 15:15 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446001">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U3zU1RDhXojuv6LYrRTy15xBrf-RnV_-Ym6eA_bhuy5OL2PmzhgqNBE_GxYcDdHfDXjBWsFf0PamhAyL4eacEhKWhMl5NiHCbrxSb-NrGq_CcQrqorCKzEaX0xJhJ1CgwJktyvAbm95KwPHIwKKgdLadcc_hnkc7jGjVGAI-8oeYeaQ6JeKnOgPlWHRv-vxVOtKfBqv18Vt0s57qLpOSQHxVOzZVb9jnUoc-rq6Zz3n7mlrxt1AEUs46OrV_NK9mbzD-26XnrBzHxIWEYSSak-Vzur97oH9FvsseoG0zJ1DwFv0GqUqEbaoz3mK4hU_Gy_hHBrawKtYraZbmpK1a3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقشه راهنمای زائرشهر چهل‌سرا در جنوب مصلا
برای مراسم وداع با رهبر شهید انقلاب
🔸️
استقرار مواکب پذیرایی، بیمارستان و آزمایشگاه سیار برکت در زائرشهر چهل‌سرا در ضلع جنوبی مصلا و خیابان بهشتی
🔸️
تماس با سامانه تلفنی ۴۰۳۰ برای راهنمای مسیر، مراکز اسکان، درمان، ستاد گمشدگان و مشاوره روانشناسی
@Farsna</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/farsna/446001" target="_blank">📅 15:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446000">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oXDzF4yxJ4bA0cPgEHkbLFumRlHfxdo6cKaJpBI5HqsA0YW0NaLUdHflbC25ZH3vDV-ewdYrKYFJGgGRitE0TS7vW7CW1Xm5eYx1DeB4PPD00mJ1ig7PfjxVf642lSlNC3JU04qAUwOIKT9GbVJUZYgZAdbpQQY4RKFfHMefRgj-B5ftZ_4buJlAM56hkR2PGSlPn6eVFMko2Rv3U9Fn0kbleZ-z76bcDUQiTSij01hvBz646-MqhIeyjcdOMC4W8md2O0aLy8TafIkvUQ7gJui6GHzF-oox7c8osLQ7VopHPl3ngjG8DBzQ8TVkogYZaLFqDy3T10qx4cJnoHFCUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
به مسابقه جام جهانی دعوت شدید!
جام دی همزمان با جام جهانی
با جوایز جذاب و متنوع
⏰
هر شب از طریق شبکه ورزش و
ویژه برنامه ۲۰۲۶، همراه بیمه دی باشید.
پیش‌بینی هر دیدار،
جایزه داره تو دی‌دار
ورود به بازی
daycup.dayins.com
#کانال
اطلاع رسانی شرکت بیمه دی
@dayins24
#دریافت
نظرات
@prday24</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/farsna/446000" target="_blank">📅 15:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445999">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/farsna/445999" target="_blank">📅 14:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445998">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">تکذیب قطعی اینترنت در روزهای مراسم تشییع رهبر شهید
🔹
استاندار تهران: شایعات اعمال محدودیت اینترنت در روزهای مراسم صحت ندارد؛ بلکه زیرساخت‌های ارتباطی با استقرار سایت‌های سیار اپراتورها به‌شدت تقویت شده است.
🔹
همچنین ظرفیت شبکه‌های آب و برق مصلای تهران به شکل قابل‌توجهی افزایش یافته و کاملاً پایدار است.
🔹
علاوه‌بر مدارس و اماکنی نظیر ورزشگاه آزادی، ۷۰۰ مسجد مجهز به برق اضطراری و مخازن آب، آماده اسکان ۵۰۰ تا ۶۰۰ هزار زائر هستند.
🔹
در صورت نیاز، بیش از ۱۵۰ نقطه در پارک‌های بزرگ تهران (مانند چیتگر) برای برپایی کمپ‌های موقت و اردوگاه در نظر گرفته شده است.
🔹
تیم‌های درمانی و بیمارستان‌های صحرایی در نقاط مختلف پایتخت مستقر شده‌اند و خدمات‌رسانی از مبدأ تا بازگشت زائران ادامه دارد.
🔹
عملیات بی‌سابقۀ حمل‌ونقل با ۱۱ هزار اتوبوس برای جابه‌جایی زائران در نظر گرفته شده است.
🔹
در حلقۀ نخست اطراف مصلی تردد هرگونه خودرو و موتورسیکلت ممنوع است و زائران باید پیاده تردد کنند. پارکینگ‌های بزرگ نیز در ۱۴ مبدأ ورودی شهر آمادۀ استقرار خودروهای شخصی هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/farsna/445998" target="_blank">📅 14:49 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445997">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95167edba5.mp4?token=FxGX_NIl_um4CFJ5OIM3Zkx0__4by10CiEGSMocHZWtXb8tO8h7QJnyOFdwjjzXf8nkV0cgEIjsrcbZdW6-9T7hU5GWjx0MvQjv_LK2dlF9hMgDRXDplE4W-ydQrHIB_9jJGR833fz3WK-_b_Y1g8ER-HhUQijMB_nWCNMv4ZdYMvMAWCxnM0pbQWGC35kSvdfaT_bmYjskesUSpO1JRUEac4TecxaA4lsiJmYyFHD23PHVlbEz2Wj6CRcEoQ8qA8UALg6zwwzq7JQS4GpK6_oDeysMVHelR9FW1gcPJHKGT1ZinA1iG6u-Y9PT6O9purWB3Pq7izMTtpXi2BhZx-oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95167edba5.mp4?token=FxGX_NIl_um4CFJ5OIM3Zkx0__4by10CiEGSMocHZWtXb8tO8h7QJnyOFdwjjzXf8nkV0cgEIjsrcbZdW6-9T7hU5GWjx0MvQjv_LK2dlF9hMgDRXDplE4W-ydQrHIB_9jJGR833fz3WK-_b_Y1g8ER-HhUQijMB_nWCNMv4ZdYMvMAWCxnM0pbQWGC35kSvdfaT_bmYjskesUSpO1JRUEac4TecxaA4lsiJmYyFHD23PHVlbEz2Wj6CRcEoQ8qA8UALg6zwwzq7JQS4GpK6_oDeysMVHelR9FW1gcPJHKGT1ZinA1iG6u-Y9PT6O9purWB3Pq7izMTtpXi2BhZx-oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مصلی آمادۀ میزبانی عاشقان آقای شهید ایران  @Farsna</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/farsna/445997" target="_blank">📅 14:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445996">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار خراسان رضوی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4806cf0329.mp4?token=vA21-g5DqregFjP_amD_D4lUUrvI0XvlLyy0fuQSvGGJbutKHzzfJHAME_Pn7fz-KxjiLar812Bv5dRg6RPsj0u7kpX0qpXtLz4zjpf95TJCpXXqjzEmtdOpnlf8T4xjmD2GSFq0JK9JYipFR7Rfiy-h8zClRTvFMFOuulBw4K3F2PceefE4OUKaF-OO56WRuEiEt74mNIWmrTAxUXmDYv9Royu_ctn60r-4sbkZ2TxchTaitCWPBo86T9JUeSjNzmm8-Mxl6MpuAKPwJiuJvhUICB2wwAebd6bwwCAFsdtF_kY74UZj7kbleEcQ5c344ZYpQgB-XQPRbTBVXWLaOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4806cf0329.mp4?token=vA21-g5DqregFjP_amD_D4lUUrvI0XvlLyy0fuQSvGGJbutKHzzfJHAME_Pn7fz-KxjiLar812Bv5dRg6RPsj0u7kpX0qpXtLz4zjpf95TJCpXXqjzEmtdOpnlf8T4xjmD2GSFq0JK9JYipFR7Rfiy-h8zClRTvFMFOuulBw4K3F2PceefE4OUKaF-OO56WRuEiEt74mNIWmrTAxUXmDYv9Royu_ctn60r-4sbkZ2TxchTaitCWPBo86T9JUeSjNzmm8-Mxl6MpuAKPwJiuJvhUICB2wwAebd6bwwCAFsdtF_kY74UZj7kbleEcQ5c344ZYpQgB-XQPRbTBVXWLaOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حرم رضوی در ایام تشییع رهبر شهید محدودیت تردد دارد
@FarsRazavi
‌-
Link</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/farsna/445996" target="_blank">📅 14:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445995">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PFfrg2OALQbaOYS0tXiv752YqQTUtoYAy8Upug4QXnKm0m2sWhbphiO8ZwGBVJ2kPTnt7Ph6zgwBu3HZ5LfU0Arp5OpMnEKPYNPHRW6tmzekRxtMLbv6bV8ngW2-zqfn4-2Rsv3b2kfTxWXI9RCsQGeEeWXsnRGtlh6o0fKBijECBvi7g7kYWcnrDH-W46IVCZTSFhp_LsT2gQOrX9NeHyW0Z9MeTk1cI7ebInJBk982EuVKcute8KnOvOrv8gYeW_ubgxJ4hqypkSGLXJSVB_zn53WW-SZAwA0TR7y-4QulgVK4B7XB4pN0BTTURl6sg2-YErCafUpvP01uAhvZNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زلنسکی از آمریکا مجوز تولید موشک پاتریوت خواست
🔹
در پی حملۀ شبانه سنگین روسیه به کی‌یف و مناطق اطراف آن، رئیس‌جمهور اوکراین از آمریکا خواست به اوکراین برای تولید موشک‌های سامانه پدافند هوایی پاتریوت مجوز دهد.
🔹
روسیه و اوکراین دیشب هم به حملات دوربرد علیه اهدافی که فاصله زیادی از خطوط مقدم جنگ دارند، ادامه دادند که تلفاتی در هر دو کشور داشت.
🔸
ستاد کل نیروهای مسلح اوکراین اعلام کرد که در حملات شبانه روسیه ۱۳ نفر کشته شدند. در مقابل، مقام‌های روسیه از کشته شدن چهار نفر در حملات پهپادی اوکراین خبر دادند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/farsna/445995" target="_blank">📅 14:31 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445994">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6eab6aa623.mp4?token=IhPtiZSWnl_-Vv-b91mpzt3-I8_PAON894zAoMO9IugZC9X8RaR0aNfLS8Opx6v_gev6I0Z6IoNCJHWp5M7uumlx6SLZ8WviBcvCU5u7m53LMGg9MPFhdVN8pCUxLssMNdb021mPJY3iyzno8qa3o74i7rjaHuclOiTZGl3tlfzr-DONG2OpzHHigtoJkdChPwjO3mUTfaufh9SDnNZ1hOzbXwo5QR8973YX64H_kdm5SggTTsUtHr_XvMmYlImP5u3aNcBM2u-jAIFIE_B0Yc5lJR6yRsf7oP71975M4Ar0SUB2o36jDrgohbMr3ka__AWzxAg1wqqaHI2c-47BRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6eab6aa623.mp4?token=IhPtiZSWnl_-Vv-b91mpzt3-I8_PAON894zAoMO9IugZC9X8RaR0aNfLS8Opx6v_gev6I0Z6IoNCJHWp5M7uumlx6SLZ8WviBcvCU5u7m53LMGg9MPFhdVN8pCUxLssMNdb021mPJY3iyzno8qa3o74i7rjaHuclOiTZGl3tlfzr-DONG2OpzHHigtoJkdChPwjO3mUTfaufh9SDnNZ1hOzbXwo5QR8973YX64H_kdm5SggTTsUtHr_XvMmYlImP5u3aNcBM2u-jAIFIE_B0Yc5lJR6yRsf7oP71975M4Ar0SUB2o36jDrgohbMr3ka__AWzxAg1wqqaHI2c-47BRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مصلی آمادۀ میزبانی عاشقان آقای شهید ایران
@Farsna</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/farsna/445994" target="_blank">📅 14:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445993">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1926cb1a1f.mp4?token=b0T8F9l668RV7_6Vjs4obeTq6wdKBakIpv9TaXxZvgusMVdWb-6A8fzvKKjcxazaYi8UfQYzQJoPP-3OMEPBKz7hyqjNcR84-jlTBjY3hw3Dn-Ltht0OSSUnrKFUK0zhhlmhSt8E4GrJ7RTln9W5uxho5jnmHGhmIoaLV3enAIIhA1NkNxVGRr3w7axziq3UucgfzKL6qdwwHm7SV00kM7odpuRGslam70W0TWc663mXZkxQH_Kqok3vBaMZv7FP665ycp7atXojTKEnXma8b4iUgggMRMNyOXaqOgI1TruordLNnhLmo1O6m7x5C8AKk-7aALSpniytAcTYUEFJEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1926cb1a1f.mp4?token=b0T8F9l668RV7_6Vjs4obeTq6wdKBakIpv9TaXxZvgusMVdWb-6A8fzvKKjcxazaYi8UfQYzQJoPP-3OMEPBKz7hyqjNcR84-jlTBjY3hw3Dn-Ltht0OSSUnrKFUK0zhhlmhSt8E4GrJ7RTln9W5uxho5jnmHGhmIoaLV3enAIIhA1NkNxVGRr3w7axziq3UucgfzKL6qdwwHm7SV00kM7odpuRGslam70W0TWc663mXZkxQH_Kqok3vBaMZv7FP665ycp7atXojTKEnXma8b4iUgggMRMNyOXaqOgI1TruordLNnhLmo1O6m7x5C8AKk-7aALSpniytAcTYUEFJEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۲ روز مانده تا بدرقۀ آقای شهید ایران
◾️
در آستانۀ مراسم وداع، تشییع و تدفین رهبر شهید انقلاب و شهدای خانوادۀ ایشان، خیل عاشقان، خود را برای این بدرقۀ ماندگار آمادۀ می‌کنند.
◾️
از ۱۳ تا ۱۸ تیرماه در تهران، قم، عراق و مشهد
@Farsna</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/farsna/445993" target="_blank">📅 13:34 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445992">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rJCm20NbpHZLmLh5BXu3QmfdMjXFyQxqkYAUqgzOM0VY6AuqGLcAr8v2SHX8S5lVHExWqG1woyQbjSJ4iy-wDlhfVcgcGuJFN3GoOLg5boduIaEKqmvtlpki7kF4JPWREjtnFWvSj2muTPF8toCvw8z0YJ7iDSRl5n2MtOPBdzoE1RUV0vtTQXBx3GTXjcIIOu4rbPHmpYAbByGqHE4qaVETS_5M3LiGEFyJFhRNUH-7AoJucsMFtHDEtyT39WuxjCnSOTwXiOdinPRYHaCyB1hJw3HkHxqNssoF3SPjm1fW95T90X47HowIfEAVfU0NovBDn3-y9h-Q8p7CCOB7UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
پورجمشیدیان: ۱۷ تیر پیکرهای مطهر به عراق منتقل خواهد شد
🔹
دبیر ستاد ملی مراسم وداع و تشییع رهبر شهید: در یکی از دو فرودگاه بغداد یا نجف مراسم استقبال رسمی با حضور سران این کشور از جمله جناب نخست‌وزیر برگزار خواهد شد. در ادامه، تشییع و طواف در کربلا و نجف…</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/farsna/445992" target="_blank">📅 13:30 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445991">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/723b049525.mp4?token=kJ-c0ErsWmHQJf7gJcoqUq771QIpaKz2uT51dJIKmjkTllaqHyXnsB1yI70xkRduqnJw786UB094i2gMb5EKaTCEXxXGzFOHfm-l15U54R0xhQp7WbtuOBypvT_zCWvm7-4CxLTKViu9-SYkjzLhbFJGBBuKv7aHcx-ywvbsUJ_8Fr30vKXSBBiUuJMZLp4Zgpw_NnkYYH5q_R0AS4xWpBYvG2ZHhNnnZK8igydmMOhl3ZRL-dCYkUd0WyNzVZhH2pfbSwtzVGuVCJPugGhAsuO7NHuRiPgJAn5r-sXb3HGzN9SuCIEUJbaAMvpzx4ApX_r3ZOddKwIuuyesez_CqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/723b049525.mp4?token=kJ-c0ErsWmHQJf7gJcoqUq771QIpaKz2uT51dJIKmjkTllaqHyXnsB1yI70xkRduqnJw786UB094i2gMb5EKaTCEXxXGzFOHfm-l15U54R0xhQp7WbtuOBypvT_zCWvm7-4CxLTKViu9-SYkjzLhbFJGBBuKv7aHcx-ywvbsUJ_8Fr30vKXSBBiUuJMZLp4Zgpw_NnkYYH5q_R0AS4xWpBYvG2ZHhNnnZK8igydmMOhl3ZRL-dCYkUd0WyNzVZhH2pfbSwtzVGuVCJPugGhAsuO7NHuRiPgJAn5r-sXb3HGzN9SuCIEUJbaAMvpzx4ApX_r3ZOddKwIuuyesez_CqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جزئیات حضور مقامات عالی‌رتبۀ کشورها در مراسم ادای احترام و آیین وداع با پیکر رهبر شهید انقلاب
🔹
سخنگوی وزارت خارجه: از صبح جمعه ساعت ۸ صبح مراسم ادای احترام و آیین وداع با حضور تعداد زیادی از شخصیت‌ها و گروه‌های مردمی تا حدود ساعت ۱۲ ظهر برگزار خواهد شد.
🔹
بعدازظهر از حدود ساعت ۱۴ مقام‌های عالی رتبه کشورها و شخصیت‌های سیاسی در این مراسم شرکت خواهند کرد.
🔹
از حدود ۱۰۰ کشور اعم از شخصیت‌های سیاسی، روسای دولت‌ها، رؤسای مجالس، وزرای امور خارجه یا نمایندگان ویژۀ دولت‌ها و تعداد زیادی از شخصیت‌ها و گروه‌های مردمی میهمان خواهیم داشت.
@Farsna</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/farsna/445991" target="_blank">📅 13:18 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445990">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/978f022180.mp4?token=Gn-AdoyJcu8p0UJQPidfAERZbPDKagDKXFdsruWygq7F2IZEw5vHJ6N00p0Y3Bh2tMHSsZ3RsONIjC2h9lDOtzIxUN9YgbfkI0RlRJJDdAlNBTIJlDAzmj_EtpDP32vlv3cuT5xvRNFL0PsjHDJQa1_HyrBfKSuJBWQ1od5X61cMv2ve9dyP5Q1ZneiRQl-q7miuRAiQGc3F2B0kYM0L9NYDJ6OpMyvScmxBmRKu5k7yXRo__Zy-KHkHN0uDfwLUuLqPZFD4GTALnbr_xWMlgfnXudOQfn4oAM4y_eAN5SsSLqhYEt_vk0s3D5_wRFjAvDf5e6LGHj0AsDT_6yQ0uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/978f022180.mp4?token=Gn-AdoyJcu8p0UJQPidfAERZbPDKagDKXFdsruWygq7F2IZEw5vHJ6N00p0Y3Bh2tMHSsZ3RsONIjC2h9lDOtzIxUN9YgbfkI0RlRJJDdAlNBTIJlDAzmj_EtpDP32vlv3cuT5xvRNFL0PsjHDJQa1_HyrBfKSuJBWQ1od5X61cMv2ve9dyP5Q1ZneiRQl-q7miuRAiQGc3F2B0kYM0L9NYDJ6OpMyvScmxBmRKu5k7yXRo__Zy-KHkHN0uDfwLUuLqPZFD4GTALnbr_xWMlgfnXudOQfn4oAM4y_eAN5SsSLqhYEt_vk0s3D5_wRFjAvDf5e6LGHj0AsDT_6yQ0uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کف پایش را هم گشتند
🔍
بازرسی بدنی مسی توسط آمریکایی‌ها روی باند فرودگاه
@Sportfars</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/farsna/445990" target="_blank">📅 13:13 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445989">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SorbvzLR35PrAcZBE-k694jDglWzn9PImX9S10ZBok_XTh9CYYsBzzjMZQ9gFVGFeALXl7D-S2DjzOji41YafuP0yLzUZ7Te0B9jT3Mze42C-mTdlJoTPSfUD61XZjNpqk3DlwTQmbaOxQTWXOiKdmQ-Y_3v4q-EeiQ9Mvv0lYZVZpq9hPLf6_NbRPR_NxQi_dcCqq919jX8nk-eWebDcNFzWJZ3W1K63fnXee25bnpE_9yUPsYIaDwEWP-DeLNI4g-rDERpfqXZnkWEyhi6kw_9KTDj9XbWjC5H3eXU3lAPm_ZWrbC9EPGQcoCp17_COsYxKRfyqyLxZH4H_LkesA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم ۵ نفرۀ گروهک منحلۀ دموکرات متلاشی شد
🔹
در پی ورود یک تیم از گروهک منحلۀ دمکرات به مرزهای شمال‌غرب کشور در روز گذشته برای اقدامات خرابکارانه و تروریستی، با رصد اطلاعاتی سربازان گمنام در آذربایجان‌غربی و پشتیبانی آتش رزمندگان قرارگاه حمزه سیدالشهدا نیروی زمینی سپاه این اشرار در کمین رزمندگان قرارگاه حمزه گرفتار و به‌صورت کامل متلاشی شدند.
🔹
در این درگیری که در ارتفاعات مرزی شهرستان پیرانشهر صورت گرفت، این تیم پنج نفره به‌طور کامل منهدم شد و اجساد آنان به‌همراه انواع سلاح و تجهیزات در اختیار رزمندگان قرار گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/farsna/445989" target="_blank">📅 13:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445988">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FGO79RooN-fOXyNccMtGw-NGnUjRdTB8OWvm9iWuatkZQVoSz3CTbYEhRGUyo7rHLUyw4JKaMgrfZ24ewrphYNGtjO6njaHfs1MSc3bLCGnlbualHY8f9mNYyR-MEiutbFpPDVuq8SteqYOCUyNCVpt-Jk_xzizVocuJFAEtEbzGN7VIh7ldz4waD9NRilNqQEeJxKb-1ISh0SAA354s9HJvOkllvUIbAAuHNdETMHgsvGIT2wTRkvCl_WYgo2C5KLpNHFr2eLBSYt_yKHO9zMlJ0Ee2FY7bSn_I-rNTVexXbz7JlGgl2W1fqTvWtj3ThjpxC7ieejvpT3ZAtFyl_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سرپرست وزارت دفاع: برای بدرقۀ مردی که تا آخرین لحظه استوار ایستاد؛ همه می‌آییم.
@Farsna</div>
<div class="tg-footer">👁️ 8.61K · <a href="https://t.me/farsna/445988" target="_blank">📅 13:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445987">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aVnUwg7TEvbdtR1CdArYmC60rLglLMM-CM84FmhooE9FWzBwy1sBRq2-PjUnG0w7X1-CTQUhTiLJ5X_coLlkMALDcEp-sKT1LV3bG7eSJObMtdtj74nsokaQbUYoypHxS1jmC9gjPOid3PbB7QNwW9PPT91KwNt4xmivYEUJLCIISXiaKK7XlBNQTnt3rqT97d4jeVNwDqgVXpJidz5XTPqY6KuzG5N3Fchl_FK9AFUh-MhXra0GbOxf7e6Qumc8TEkhkUEW1FBCLSVyGw_hnLQBzhxkcbZ0xeAmQ5b3GqDdHi7qzCC2T3CUn25T3ORl0DoykRFmDdzqyl43sNBwGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نماینده ولی‌فقیه در سپاه: شهید اکبرزاده پاسدار حریم ولایت بود
🔹
حجت‌الاسلام حاجی‌صادقی: شهید محمد اکبرزاده انسانی وارسته، متواضع، پاک‌نهاد و پاسدار حریم ولایت بود که بنا بر گزارش‌های واصله، در جریان فتنه اخیر و در پی جنایات رژیم منحوس صهیونیستی و آمریکای جنایتکار،…</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/farsna/445987" target="_blank">📅 12:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445986">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00ab685976.mp4?token=RPAKZa-cb2VPOSMFmGP85HcvBG6GonWZTRf6Nxfnn14I6a0UMVVVAyfedBiOTNX_6_QbE2CucMHKagpGbwaZ8-eZdmLKuMw-tBP0PizYnImSQDyxtvLtKHfut1KhyJQRxV1r_yUsLP3M_S64VhB9rAWQ5TpZD3pjonSNjDAkTMoVMeqFtPyOb8I4nVz3eYfNrs_Cgj3A9Ut7IJ1fOIvIQ-fjjCd-o-63nDrOJ_EJQebjEV3R3P_ezyP0LFD5ZzOch7Ye-0_2CKinqmRxRy7HORrCh185JO7ZfyYwuya9xYFP1pXPk_xeMksoRrNaHFxSZS4LtTjaPT7XP7tai9isAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00ab685976.mp4?token=RPAKZa-cb2VPOSMFmGP85HcvBG6GonWZTRf6Nxfnn14I6a0UMVVVAyfedBiOTNX_6_QbE2CucMHKagpGbwaZ8-eZdmLKuMw-tBP0PizYnImSQDyxtvLtKHfut1KhyJQRxV1r_yUsLP3M_S64VhB9rAWQ5TpZD3pjonSNjDAkTMoVMeqFtPyOb8I4nVz3eYfNrs_Cgj3A9Ut7IJ1fOIvIQ-fjjCd-o-63nDrOJ_EJQebjEV3R3P_ezyP0LFD5ZzOch7Ye-0_2CKinqmRxRy7HORrCh185JO7ZfyYwuya9xYFP1pXPk_xeMksoRrNaHFxSZS4LtTjaPT7XP7tai9isAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مجموعۀ چهارباغ در ضلع شمالی مصلی آمادۀ مراسم وداع با رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/farsna/445986" target="_blank">📅 12:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445985">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h_epNcvYHeC_Tz5mEv7kiZUbN8bZB9Crr0ceCsUqtJ_Mc_p8q_0zu-Vd3aaDPmopVtHLJns0k--n97bYnjqqev3B0t5KP0k_Wi1LpahuZufBIz32KNG-K-zsm2whgZp-O92Falm-4PZKN45x1XizBTh0V3d55taah8W4ihnCPZZ8IB-bMZ436fJ0ZeOF9c1yeR3PFi_r4nBaVN200Uj_by2zhIDPnPsdoE0vw4ZQco5KkVCIuuI1BnguBScAtl-rt0nj0HNkDYVnHsk_7YgSSmzP04W8Oikx2Y7YZ9eMRIKkQjyVIok_VYo4y2-hisZ5OC1wTobjs1p5hnCOa3185g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون سیاسی نیروی دریایی سپاه طی سانحه رانندگی درگذشت
🔹
دریادار دوم محمد اکبرزاده، معاون سیاسی دفتر نمایندگی ولی فقیه در نیروی دریایی سپاه، ساعاتی پیش در یک سانحۀ رانندگی بر اثر واژگونی خودرو در یکی از جاده‌های استان کرمان جان خود را از دست داد.
🔹
پس از وقوع…</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/445985" target="_blank">📅 12:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445984">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔴
قرارگاه مرکزی خاتم الانبیا: هرگونه دخالت آمریکا در تنگه هرمز با واکنش قاطع و سریع نیروهای مسلح مواجه می‌شود
🔹
تنگه هرمز میدان بازی آمریکای متجاوز نیست، بلکه قلمرو حاکمیت مسلم جمهوری اسلامی ایران است. امنیت و حفظ ثبات این آبراه حیاتی، خط قرمز نیروهای مسلح…</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/farsna/445984" target="_blank">📅 12:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445983">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
قرارگاه مرکزی خاتم الانبیا: هرگونه دخالت آمریکا در تنگه هرمز با واکنش قاطع و سریع نیروهای مسلح مواجه می‌شود
🔹
تنگه هرمز میدان بازی آمریکای متجاوز نیست، بلکه قلمرو حاکمیت مسلم جمهوری اسلامی ایران است. امنیت و حفظ ثبات این آبراه حیاتی، خط قرمز نیروهای مسلح قدرتمند ایران اسلامی می‌باشد.
🔹
تمام شناورهای نفتکش و تجاری موظفند برای هرگونه تردد امن از تنگه هرمز، از مسیری که ایران تعیین نموده است، اقدام نمایند.
🔹
هرگونه عدم تمکین و خروج از مسیر تعیین‌شده یا بی‌توجهی به پروتکل‌های ناوبری جمهوری اسلامی ایران در تنگه هرمز، با پاسخ بی‌درنگ و مقتدرانه نیروهای مسلح مواجه شده و امنیت شناورهای متخلف را به خطر خواهد انداخت.
🔹
همچنین، مسئولیت هرگونه تلاش برای دخالت در امور امنیتی یا هرگونه اقدام مخل در تنگه هرمز توسط آمریکا، تهدیدی علیه حاکمیت ملی ایران تلقی می‌گردد و با واکنش سریع و قاطع روبرو خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/445983" target="_blank">📅 11:54 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445977">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d5paAfnNVRuMGuSUtv4BPelI64CSkN4dZih2DqzkFyojGBEFy18VM7R4QuGOu7As17fU_QlDgmHauwBcQgO31K2c2yITjmr1nIWPcknuvjb263Rfb4XuDWNA1Yp_wwf3V7A92uNYxqBxJ7D6OhXoi4BgxTpZz6nWgcohAmiJw9vJgnMPqaaGyiXIo86e4rfTai8gYks-DjQcZoF2o8-rrY-NYbQ_pZA4JN3ln-gaOzb9DD3WpLNFMS_a28UWnmFHAb0rQlAJ2MsIY-wvCuIHYDMQR9sQOusVMJ1Q6XWGyVl5QwVdM4d9AuzSEfy-HPapeOLz3aEHY_u-HmaKO8IGbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iXHpiqM9i8_Rb8RHmkmvG7jk6fRJJMBIXeqBUng9GsOGcbpMvzoBI6YHT507LAC4_ownE9QrUS3tSUvuWjxIwOdlQ-af0yKYepcDV9pTZKn8uX9SZhI8Dg-EqP3upRnOOMBEQXiz2xV_0qftluhCH7SvPl6gQCvVuKz-NQtzZkkqA_N_xFSPGxQ5WBUqKCeRFULisiRD2Zrh7RPHMXKg3Xij0nSoYYtI3Hc2gQe-QtayBZF9wQi3XjI-m6M92ezkBJGAV_sM7aCA-5YYezbQHbYrSFSZO5-PgMCOmhRjd7eZKHXIciAtWbwQYBslny97cFzUzpCvjtthQv6vC-MAAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/efj2ax0Fxtc7bHFotJZMrWoFPuHppy-n_hWx9bYhyf2jcw3RX-xtxqQXASD9ihQ4lIQcdT_SACIIZrgSXD1dchVjYjFyxpqJwyQSwmIWpfKlZ_CskOlu-O9wh1TfbixHxcf9pUanRznkrZAA1mAoW-Qp2900EznMOngcGpDFP-0vuCZudQbQwXIAbP6KCZ_qf0gAl5Q3Dchte3kp6uKTQ7o5Kdmalq05PvNPIJVIaqah_Z4CIcMTe2kfovXfPtl16pcSctcmFZ_MOADBezW9QljIM7PdRfUk2ox76KQnc_D3bfqmbb6TiQkTUHU6dYUHthwzusqFp7DJiXPMbuSb7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WnErD7tSJlcjlZM5CjgVojSqrf840tAkXyBNjMBwOsPLosqK47vMNZZ58MuUoBpLwOtxIdgD1oed2U3iv6_x3h4QhhAUrSEOZoqFjjE1yO6ZgGe9xf5t2LZEFedVGJMbVbNx-N0tQHr61Qh_uLzMRitPo4esyflZvOIDYMh6hiLRYL4xNfuLlQkP3YSbvRZJYUdFq2TNO30biWgLC93iLo0RCo_vBNxHgH5dbesNVrx0XwPvIuUH8bG3JvEdR911G8MOb-mRcWpvJXTJT_SxxrBtcMMSCXHzFxa8-DyC0OxvfvQJdxmwQmnn82z36uhDd4GFaR36NWgBYCBg8KDaDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u0NcnwFSasbGOn3wv9TtkboKaKX3_GP-2sx7ld-1JxW6Mlgzj-yX-rWRpt-b7QJULMjzdRHt_Pr1Rxr6eTMaK63jsJtic8-ooREVdtu2SDqN5b4ukHjWP6VFwKTBF1IRknEDWFFgOdhMemvG857j4c8a-g3Wv1tyzE1BTwxQkjAg9zy4OScoVoMUKPD9gcXAAWg7Bivmu2wHPUKHGrHjoC3QfbqGGxYv7a_LURlilRWu8XJ7eVQ5dJPCoBm8GXMOX2Z7IHuKYqZ-a2gycZYjcWdOfGNLkA9AjSqKB_6ONQA6LdQ7TDEEPmC6weyEzMDSjVKE5CjXfzlQloamhOKTGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uS7r_6tPJhWce75K7MwuWf8fXoj2TfbwARGKdwwjWAZmO0v1WhrS9jMFlJksNLFdLcVQ8U3nhdZr27xyYnJ-tc0Mkybh8KRWiAcBpJImQfaB9_x1sIRfXyYk3aR_C1qrbBGVjDSVZsnP9aKW2y1HFkYFAUBbsRtBPqC7rm0mCdXDC5U_elGCUFkDR3xiloN5uO8dFCzjDIFbA9h6TykJA3rKNm5fQ6n8ZP2ioN0Nses-xZ-e6vtN0oCEc8epPqtQ34hBuCSIeDuhdxxkRw_rSeCfV-_RhIHFBCyxkUgBiSM5AxVnm3VdmJzHvAnAzf0Cd7MTCXAiuJkaEHWzis55Uw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
برگزاری مراسم وداع با همسر شهید رهبر انقلاب
🔹
مراسم وداع با معلم شهید خانم زهرا حداد عادل، عروس رهبر شهید انقلاب و همسر شهید رهبر معظم انقلاب شب گذشته با حضور غلامعلی حدادعادل، خانواده ایشان و جمعی از همکاران و دوستان وی در مدرسۀ فرهنگ تهران برگزار شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/445977" target="_blank">📅 11:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445976">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/486b20a211.mp4?token=hKvHcccT9aPrtolXYLnFhgPJNW6RwEWGjFedYixd8J2b3jUPCUV0VZo75BFxa9EdI-yH6EBXHNUiNlTpkFNvdGHtKgDUGm_cjfe0OGfFBeeSyyuJFtBTE4q0TeSIIcjD7eFVE_XL_EHLaPzIVQLTRgdfEQAPAwJYu0yCpSCEle7LIFkT0MFm4HKWwQSiDLfaUtrkn6uwAG2SpiwtSfvEpA4okJhjawFcuUZ_noudOXWi5tLEERNR57v9PUluJaBTjMKKrWU-E4qaZLzoSQC2VJV25CrDiPbMpvSZbz4MHN7LMRw8UUYLDkTXodxiR3RXyieZogyPhvFzatIFhrIca10_eOVGN4G43yLtheqVUODthhtbcHsfOHdvShh5m1NU5HXwcU9bBDCB-K71y0bIVDIVbEJCaRK3FM7C1Bb5JQTD_yBtkcSqLjKBjJ6_oKMiY3XjMWoNUtEx9gSKR3xYaWQG5Y-0yFeJHIdlcm2iuy1k_-bn0ZqW-cmqxipia4DPz5Tz_ZFBiAjT3hxMcgk2-dGLzPFBTnIB6bJ03YdHpCRgCb31-drmPvV2inZW_3t22N1y_e2dtubKE5SWWnOxdg9sKR05BM0D53K11ECUWhlSXeVXoopC8F6SlsPVaJB4zskjH5XXcJHEfzKQgogDTE7ixh8frd8f__MmDyJXXrM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/486b20a211.mp4?token=hKvHcccT9aPrtolXYLnFhgPJNW6RwEWGjFedYixd8J2b3jUPCUV0VZo75BFxa9EdI-yH6EBXHNUiNlTpkFNvdGHtKgDUGm_cjfe0OGfFBeeSyyuJFtBTE4q0TeSIIcjD7eFVE_XL_EHLaPzIVQLTRgdfEQAPAwJYu0yCpSCEle7LIFkT0MFm4HKWwQSiDLfaUtrkn6uwAG2SpiwtSfvEpA4okJhjawFcuUZ_noudOXWi5tLEERNR57v9PUluJaBTjMKKrWU-E4qaZLzoSQC2VJV25CrDiPbMpvSZbz4MHN7LMRw8UUYLDkTXodxiR3RXyieZogyPhvFzatIFhrIca10_eOVGN4G43yLtheqVUODthhtbcHsfOHdvShh5m1NU5HXwcU9bBDCB-K71y0bIVDIVbEJCaRK3FM7C1Bb5JQTD_yBtkcSqLjKBjJ6_oKMiY3XjMWoNUtEx9gSKR3xYaWQG5Y-0yFeJHIdlcm2iuy1k_-bn0ZqW-cmqxipia4DPz5Tz_ZFBiAjT3hxMcgk2-dGLzPFBTnIB6bJ03YdHpCRgCb31-drmPvV2inZW_3t22N1y_e2dtubKE5SWWnOxdg9sKR05BM0D53K11ECUWhlSXeVXoopC8F6SlsPVaJB4zskjH5XXcJHEfzKQgogDTE7ixh8frd8f__MmDyJXXrM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرمانده سپاه تهران: خودروی حمل پیکر مطهر رهبر شهید به شکل ضریح حرم امام رضا(ع) طراحی شده است.  @Farsna - Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/445976" target="_blank">📅 11:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445975">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42a87fdc50.mp4?token=PH0oN91HSy9xvqhNPIZsZfZr-DJvGelkSBfASXe0URpUymcHt1gO9ahrqhhMiMxQ5xK37kl8R8ElheHmpKY_7UD-v4uQR0hsRu5jLrItcY-zjCaFEkrHFg8v-m5d2dKF8N16CsMz0GQ0lkiaYG5onR8e9fbHBz55PFaH4UD2g6hnxYq1fG7E0K6DlI2uV1QaeKPlmupdGTffSzlsP0GM-pAxKw1SQhZkUshk75XcqTa6MdHnEboyBshhtOWslQGNVGot0N_CwXk7P8-_ZT3APAuerPhnpJbgK_gZrBXK5pm1IjkLj9URO9lYvVFL_TB0JBLlzfxFKa2nsa3_LqCpLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42a87fdc50.mp4?token=PH0oN91HSy9xvqhNPIZsZfZr-DJvGelkSBfASXe0URpUymcHt1gO9ahrqhhMiMxQ5xK37kl8R8ElheHmpKY_7UD-v4uQR0hsRu5jLrItcY-zjCaFEkrHFg8v-m5d2dKF8N16CsMz0GQ0lkiaYG5onR8e9fbHBz55PFaH4UD2g6hnxYq1fG7E0K6DlI2uV1QaeKPlmupdGTffSzlsP0GM-pAxKw1SQhZkUshk75XcqTa6MdHnEboyBshhtOWslQGNVGot0N_CwXk7P8-_ZT3APAuerPhnpJbgK_gZrBXK5pm1IjkLj9URO9lYvVFL_TB0JBLlzfxFKa2nsa3_LqCpLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زائرشهر امام خمینی(ره) در ضلع شمالی مصلی آمادۀ مراسم وداع با رهبر شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/445975" target="_blank">📅 11:23 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445973">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/124c09411b.mp4?token=kInxe-pVi3ofAWFQt9zpW3tlqK98QotqgLSG9286v5S1_vtZZZDM01GvAFx6b0cmfapxfrw3Ja3Wtpvw0Sb9v_IWy2j2Ji3Dk9w7ymAAGIIV_y7ES9LU1gjWP8Cvo2pKXCClQbPiMHu6gDam_MtRa0f6NaYAlcJmvxwVNV7UKrbY3Qj_WvZ6OiN7OncyfySw6k_djt88fokx-F1_cg_hLdjKKrjRLqsbSiX1_dpWsxC7bcpt6P7-3zKvLDCFMdoDKgXz6LfvwFDcEMawXHp2jXOfiLqBIttxFGs2fVe3TQPs_cKG1J1Zubuxzzbg6ShM9Aaj1s_ajFFJ2bq8kZo6VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/124c09411b.mp4?token=kInxe-pVi3ofAWFQt9zpW3tlqK98QotqgLSG9286v5S1_vtZZZDM01GvAFx6b0cmfapxfrw3Ja3Wtpvw0Sb9v_IWy2j2Ji3Dk9w7ymAAGIIV_y7ES9LU1gjWP8Cvo2pKXCClQbPiMHu6gDam_MtRa0f6NaYAlcJmvxwVNV7UKrbY3Qj_WvZ6OiN7OncyfySw6k_djt88fokx-F1_cg_hLdjKKrjRLqsbSiX1_dpWsxC7bcpt6P7-3zKvLDCFMdoDKgXz6LfvwFDcEMawXHp2jXOfiLqBIttxFGs2fVe3TQPs_cKG1J1Zubuxzzbg6ShM9Aaj1s_ajFFJ2bq8kZo6VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
توقیف تریلر حامل ۷۶۶ کیلو تریاک در استان فارس
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/445973" target="_blank">📅 10:50 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445972">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">قالیباف در پیام دعوت از مردم برای شرکت در آیین تشییع رهبر شهید: باید برخاست و ندای خون‌خواهی ملت را به جهان رساند
🔹
ملت بزرگ ایران امروز ایران عزیز در آستانه خلق یکی از بزرگ‌ترین صحنه‌های تاریخ خود ایستاده است، روزی که یک ملت، با دل‌هایی سرشار از عشق، وفاداری…</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/445972" target="_blank">📅 10:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445971">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">محدودیت تردد تهران-شمال و چالوس
🔹
تردد در مسیرهای شمال به جنوب آزادراه تهران-شمال و جاده چالوس از ساعت ۹ صبح امروز تا اطلاع بعدی ممنوع است.
🔹
در آزادراه تهران-شمال، چالوس، هراز و فیروزکوه مسیر جنوب به شمال ترافیک سنگین است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/farsna/445971" target="_blank">📅 10:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445970">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X1xp4vCqQK8Du4ExJNpdTwzLQd9KRWJaWRhyK1_a8Czxkx0VzBGbRQzldeOrb8HOPv9NVJWqtgthuTBnMy0qBlVGVe0DiOaA_r1Ate7bZtGxpxkTlHHwAJ6uJKuz3ENikWboQnUYB24326YW6HvyGtIQT39N36OWX_Eq-RN4eR7hUevteg1oKckZ-KH5nmxFN5HLPCEWP2Q9hDslLJacQgheT1wl88EJxHLXTF4mYzokNXkwr1tk7qB3CpeaCOLJM8oxEonUqnXh1VvgLzSVOXZAN5Pv5Rpk2BwyyOoiOkWD1S4UQpAea4hb5pX2WgdFsbk9-hR0XJ_ga1D7XVUDuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهران در آستانه میزبانی از بزرگ‌ترین رویداد ادبی تشییع امام شهید
▪️
آیین بزرگداشت بین‌المللی شهید آیت‌الله سید علی خامنه‌ای با حضور شاعر برجسته فلسطینی و چهره برتر ادبیات و هنر مقاومت، استاد تمیم البرغوثی و دیگر چهره‌های شاخص رسانه‌ای جهان عرب؛ به همت پردیس بین‌الملل سازمان هنری رسانه‌ای اوج برگزار خواهد شد.
🕓
جمعه ۱۲ تیرماه ساعت ۱۷ الی ۱۹
📍
تهران، شیان، میدان شهید تجرلو،
مرکز همایش‌های بین‌المللی کشتیرانی جمهوری اسلامی</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/farsna/445970" target="_blank">📅 10:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445969">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(N@vid)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jzlh5_sluka39awzrJise-bWxmu3JJ4-ucjFSvLNKGJFJNSeQPnMjrx4qriGHmlhAPjMSlYSQCkCUDzB-9vJ70XXm-A34McYpmmoiFxWfSJfPzxsgPP1DqJHR5IUC1l3NRgZmNJuXtgUmw-SBAP-LhA6p3Bcu14KoBiz7nCDGJzj6G5GbxtJKdSjRe56GzqEb5TJ--g_VYce8zewMS1T9PL2SdSMvQ9SMYsffhiQ-HwadQMcbbiXsozy7HI-pyjAiFFemcCTLqc4O3tT0q49BYKwUWf-3rb2E2ZfPz2RlMCwOuJrfDWsE-l3NONvdwYLsiGmfJnDFUX0iXGZTH2R6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◀️
پذیرایی موکب بانک شهر از عزاداران مراسم وداع با رهبر شهید انقلاب اسلامی
🔹
در حالی که ملت معزز ایران و جهان اسلام در فضای پر از اشک و اندوه، خود را برای وداع با رهبر بزرگوار و شهید انقلاب اسلامی آماده می‌کنند، موکب بانک شهر با هدف خدمت‌رسانی به عزاداران و تسهیل امور میزبانی در این مراسم بزرگ، در یکی از نقاط پرتردد پایتخت ، آماده پذیرایی از جمعیت عظیم مردم است.
🔹
موکب بانک شهر با استقرار در محل سازمان فرهنگ و ارتباطات اسلامی (ورودی بزرگراه شهید همت)، مسئولیت پذیرایی از عزاداران و شرکت‌کنندگان در مراسم وداع رهبر شهید انقلاب اسلامی را بر عهده گرفته است. این موکب با بهره‌گیری از کارکنان داوطلب بانک، به صورت 24 ساعته، ارائه خدمات متنوع به عزاداران رهبر شهید انقلاب را در دستور کار دارد.
مشروح خبر را
اینجا
بخوانید</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/farsna/445969" target="_blank">📅 10:31 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445968">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/farsna/445968" target="_blank">📅 10:29 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445967">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WgR5rba7H8SwgJyx20OFSHNw1akjDukN8YadKsIDYW5_jGBu0ScKY5Q5QPifL7xjwnPEwa6NdzTa-H9xhKYe6ag-sBy7bP8clliJMmUeNovTgMoDSkpur3P1ql5mG1itUtVLiaQ4AmQ1J4FSt-9YRzXqzCFP8ViYA4oBfTJ-ZLYvG2N5ptEGE_9qtFmcVixa2Flyeg-cBwuNTJzHrOqMEo82VxWL4Kr0qgrZHUd-HE7xNkv85XwSRvkQFwFfVxPwplNwo-iVmSrVzGpai-bJwWBJzxR3Quja5EhMDBPZ04xSVfvI9PYKBzoLSh-K62p0jh7oq7KR4DM_mjbTCi-hNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف در پیام دعوت از مردم برای شرکت در آیین تشییع رهبر شهید: باید برخاست و ندای خون‌خواهی ملت را به جهان رساند
🔹
ملت بزرگ ایران امروز ایران عزیز در آستانه خلق یکی از بزرگ‌ترین صحنه‌های تاریخ خود ایستاده است، روزی که یک ملت، با دل‌هایی سرشار از عشق، وفاداری و لبریز از داغ فراق، به بدرقه بزرگ‌مردی می‌آید که عمر پربرکت خویش را در راه اسلام، استقلال ایران، عزت ملت و آرمان‌های بلند انقلاب اسلامی سپری کرد، مردی که به نمایندگی از ملت شریف و سربلند کشورش هیچ‌گاه در مقابل استکبار جهانی سر خم نکرد و تا فتح قله شهادت مردانه در مقابل ظلم و ستم ایستاد.
🔹
تشییع پیکر مطهر رهبر شهید انقلاب اسلامی، حضرت آیت‌الله العظمی شهید سیدعلی حسینی خامنه‌ای، تنها یک مراسم بدرقه نیست، تجدید میثاق یک ملت با راه پرافتخار شهیدان، با ارزش‌های انقلاب اسلامی و با عهدی است که نسل‌های این سرزمین برای پاسداری از آن ایستاده‌اند. عهدی که با اشارات خمینی کبیر رحمت‌الله‌علیه با صاحب‌الزمان عجل‌الله تعالی فرجه الشریف بستند و تا آخرین نفس پای آن ایستاده‌اند.
🔹
امروز چشم تاریخ به ایران دوخته شده است. حضور میلیونی و حماسی شما مردم بزرگ، جلوه‌ای از عشق و وفاداری خواهد بود، حضوری که به خواست خداوند، این بدرقه را به عظیم‌ترین و ماندگارترین بدرقه تاریخ بشر تبدیل خواهد کرد، حماسه‌ای که عظمت روح یک ملت را به جهانیان نشان خواهد داد.
🔹
از همه مردم عزیز ایران، از جوانان پرشور، خانواده‌های معظم شهدا و ایثارگران، زنان و مردان غیور این سرزمین و همه دلدادگان راه حق دعوت می‌کنم با حضور باشکوه خود، صفحه‌ای پرافتخار در تاریخ ایران اسلامی رقم بزنند و بار دیگر نشان دهند که ملت ایران در لحظه‌های بزرگ، یکپارچه و استوار پای عهد خود می‌ایستد. باید برخاست و ندای خون‌خواهی ملت را به جهان رساند تا دنیا بداند ملت شریف و نجیب ایران در مقابل ظلم و استکبار سکوت نمی‌کند و از خون امام خود نخواهد گذشت.
🔹
همچنین از همه مردم شریف و فهیم ایران دعوت می‌کنم همچون همیشه، با روحیه ایثار، همدلی و مسئولیت‌پذیری، در برگزاری هرچه باشکوه‌تر این مراسم بزرگ یاری‌رسان خادمان خود باشند، باید یک‌پارچه با خدمت به زائران و شرکت‌کنندگان، رعایت نظم و آرامش و همراهی با دست‌اندرکاران، تلاش کنیم تا این حماسه ملی در شأن مقام والای آن رهبر شهید و عظمت ملت ایران برگزار شود و این حماسه تاریخی به عنوان سندی انکارناپذیر از استواری ملت ایران و آزادی‌خواهان جهان در تاریخ بشر به ثبت برسد.
🔹
امروز هر قدمی که به سوی این مراسم برداشته می‌شود، ادای دینی است به مجاهدی که خود را وقف مردم کرد و هر قطره اشکی که بر این مصیبت جاری می‌شود، نشانه پیوند عمیق ملت با خادمان صادق خویش است و هر ندای وفاداری، گواهی است بر تداوم راهی که با خون شهیدان آبیاری شده است.
🔹
خداوند روح بلند آن رهبر مجاهد و شهید را با انبیا و اولیای الهی و شهدای راه حق محشور فرماید و ملت بزرگ ایران را ذیل توجهات حضرت ولی‌عصر ارواحنا لتراب مقدمه الفداء و تحت اوامر رهبر شجاع، دانا، دلسوز و داغدار این ملت، حضرت آیت‌الله سیدمجتبی حسینی خامنه‌ای حفظه‌الله در ادامه مسیر عزت، پیشرفت و سربلندی یاری نماید.
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/445967" target="_blank">📅 10:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445966">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a220e92f7a.mp4?token=p0TxrEHZm1Uh_StN0SyjhWz-ZAuauKpringgW0Xm5HL-g-20q2QipiZ5IdZZ23FsuurJPq275K2k1xKNC0awyI3jNC5owM4o1vjGta0UAw-YZdSO40o9XJ45maJGvfbr9qDJtLSn6U2sXeHhJVQbwkWS9ZG3MOmI7MYpEUj94MBmNyFBRgj44EPmgzUqgtR-Z2748q6-9GO56-q6Zi7KcjrldeT-fr1LJCghFnc3cHHGvopVmsegripEZzQx1mDNDsOw2IShL0r_Aon6moBr3WRa9BSyhbVCPqUbIUj_MXWujoPpW7Subbez1XYOYFp-8iAGo-ugJyu6tBvbCnbhZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a220e92f7a.mp4?token=p0TxrEHZm1Uh_StN0SyjhWz-ZAuauKpringgW0Xm5HL-g-20q2QipiZ5IdZZ23FsuurJPq275K2k1xKNC0awyI3jNC5owM4o1vjGta0UAw-YZdSO40o9XJ45maJGvfbr9qDJtLSn6U2sXeHhJVQbwkWS9ZG3MOmI7MYpEUj94MBmNyFBRgj44EPmgzUqgtR-Z2748q6-9GO56-q6Zi7KcjrldeT-fr1LJCghFnc3cHHGvopVmsegripEZzQx1mDNDsOw2IShL0r_Aon6moBr3WRa9BSyhbVCPqUbIUj_MXWujoPpW7Subbez1XYOYFp-8iAGo-ugJyu6tBvbCnbhZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قم مهیای بدرقهٔ رهبر شهید می‌شود  @Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/445966" target="_blank">📅 09:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445965">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baadb9236f.mp4?token=DMzU1DwZHu7DecAi3AlUS4Zk0walRkSTDJz1g8heynfviQTFzpE5wQ-xJO9YbDEGtkqMrpG0o6qPbhF87iDBDKUMfVipP4N11rDZokVMyGXvy1_-96Idf2N7zJiixvq-7gToceKy-toq3Q638gAE9iqFcBgGuNbn9KA1rroB6D3xJOj38hh5ZnRELCGlyJniaKGp_fWjmw7EPzZWMyK7znh1QQq3dwm9NJuuoogWVpBECdZ2mKh9u9otFlE32gPT8GaxPVnEB_-doWtbcVVbEQtWKIaTr2Pwlv7eIRBEYYilHvjvm0YZBF8OxGyXVHfVJORts6tCpBgDuiawm6aj9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baadb9236f.mp4?token=DMzU1DwZHu7DecAi3AlUS4Zk0walRkSTDJz1g8heynfviQTFzpE5wQ-xJO9YbDEGtkqMrpG0o6qPbhF87iDBDKUMfVipP4N11rDZokVMyGXvy1_-96Idf2N7zJiixvq-7gToceKy-toq3Q638gAE9iqFcBgGuNbn9KA1rroB6D3xJOj38hh5ZnRELCGlyJniaKGp_fWjmw7EPzZWMyK7znh1QQq3dwm9NJuuoogWVpBECdZ2mKh9u9otFlE32gPT8GaxPVnEB_-doWtbcVVbEQtWKIaTr2Pwlv7eIRBEYYilHvjvm0YZBF8OxGyXVHfVJORts6tCpBgDuiawm6aj9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دل‌ها آمادۀ بدرقۀ پدر امت
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/445965" target="_blank">📅 09:15 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445964">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/364498c1b4.mp4?token=e-cG5e0WJY53V-BHblK6mX7qkPt0FpyYXnk-V83PufYjIR3LGysnHy9flcwU6yhD4p40LrvDwjDcu57OlD_pbeSEanc5Z4KzfgPVufOJ0iua13_bxQR226I2vYTGs5nJ_pKpBjzkf_EBUmkuxC-iXo08kodNoBcIdK-p5T---K9TY5O35XwciW4RF8QArIn8AFbs4I1Qjl31FfWyZWCfxiKZYBAVK4aKNzZL-m0HadnXAzQb9_jkLpoD3i2iIIxR7un4JDc_AT28gtLH2wO0uOTgX1uwGxo7lye_pD8DOzr6o45VwuyuYKuYVWfJUCoT1mhuyHEG8Fk2yqKjAo5FWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/364498c1b4.mp4?token=e-cG5e0WJY53V-BHblK6mX7qkPt0FpyYXnk-V83PufYjIR3LGysnHy9flcwU6yhD4p40LrvDwjDcu57OlD_pbeSEanc5Z4KzfgPVufOJ0iua13_bxQR226I2vYTGs5nJ_pKpBjzkf_EBUmkuxC-iXo08kodNoBcIdK-p5T---K9TY5O35XwciW4RF8QArIn8AFbs4I1Qjl31FfWyZWCfxiKZYBAVK4aKNzZL-m0HadnXAzQb9_jkLpoD3i2iIIxR7un4JDc_AT28gtLH2wO0uOTgX1uwGxo7lye_pD8DOzr6o45VwuyuYKuYVWfJUCoT1mhuyHEG8Fk2yqKjAo5FWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اولین تصاویر از آماده‌سازی خودروی حامل پیکر مطهر امام شهید
@Farsna</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/445964" target="_blank">📅 08:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445963">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">۶۰۰ خبرنگار خارجی مراسمات وداع و تشییع رهبر شهید انقلاب را مخابره می‌کنند
🔹
وزیر ارشاد: حدود ۶۰۰ خبرنگار و نمایندۀ رسانه‌های خارجی در کنار رسانه‌های داخلی این مراسم را پوشش خواهند داد تا ابعاد مختلف این رویداد برای افکار عمومی جهان روایت شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/445963" target="_blank">📅 05:58 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445962">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e71fe17f30.mp4?token=HIuhJvDL9V7JIDnsEj7dVUlMRMtzP-TvH1daxxscFsCA3g5z3rZrzjrS4hRqBfkdP01dqMB5T7rFKS0ofVXUcu1ukXdDfDgaFsU5opIpx7TnuqnSa40F-TIS0Tvo3ssoCEkRrMy8uZZ6DoDOuHh2sK097xZ9caiazqIsjZoYZJGmsGZOV8gvX7ISfBe8odluk19uoLoCls_B8BwF-ikWAaW2x7qwIE2PkLHO6YZpI4GE_5_OuBDEg2Usug2EaX6H8OrKa_23duAL8Yqn3O5T0nU4To5ttkQPKe-eoTLp_skxvqPhWkcZnqngDoURevtjhJ16zYYiaI-dbu53Wj_JMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e71fe17f30.mp4?token=HIuhJvDL9V7JIDnsEj7dVUlMRMtzP-TvH1daxxscFsCA3g5z3rZrzjrS4hRqBfkdP01dqMB5T7rFKS0ofVXUcu1ukXdDfDgaFsU5opIpx7TnuqnSa40F-TIS0Tvo3ssoCEkRrMy8uZZ6DoDOuHh2sK097xZ9caiazqIsjZoYZJGmsGZOV8gvX7ISfBe8odluk19uoLoCls_B8BwF-ikWAaW2x7qwIE2PkLHO6YZpI4GE_5_OuBDEg2Usug2EaX6H8OrKa_23duAL8Yqn3O5T0nU4To5ttkQPKe-eoTLp_skxvqPhWkcZnqngDoURevtjhJ16zYYiaI-dbu53Wj_JMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بدرود پدر ایران
🔹
تصاویری ماندگار از رهبر شهید انقلاب، به‌همراه قطعۀ موسیقی وداع
@Farsna</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farsna/445962" target="_blank">📅 05:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445961">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">بلومبرگ: عبور نفت از تنگه هرمز، ۱۰ میلیون بشکه را رد کرد
🔹
یک مقام آمریکایی شامگاه چهارشنبه مدعی شد که حمل و نقل روزانه نفت از طریق تنگه هرمز، از ۱۰ میلیون بشکه فراتر رفته و ۵ میلیون بشکه نفت دیگر هم از طریق مسیرهای جایگزین منتقل می‌شود.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/445961" target="_blank">📅 04:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445960">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/facVrfe8rt66B4zYB61kkx_HdK_COt6cwrHRy33WjAdEknx2Xw1WhLtvUcgAdCvDyvmmxvk20UACdZC4I1T-5tyaWegRBCXZea_TnfOdwszbAv2rI6S6LBrg5h83EUl1D2-Z3HQ78a6j1PyeiVoOb9cO0A3cpEuNzCtUhQDI4FC1VQ9cB0YtSt_8O1Y2KAFRdlEtT_tPtfqS0HMiSYDkt9tDAs8DbQQzmYA-EzCwORGRwsvoXh74ZU6Od_Hp_yadhbs_u5wl5CEcY1poFNqeS5y6Zh4d8LKWKYM2Wm77BQO0F669m9aDVqb8YxRDUmPQ1EPzNmh37TbBFAbtIl-mMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
رئیس دانشگاه علوم پزشکی ایران:
تمام خدمات درمانی در مراسم تشییع و وداع با رهبر شهید انقلاب رایگان است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/445960" target="_blank">📅 03:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445959">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NGxtTYEbxl9q1Ly3_kS_ozguZkkIvJaqB1YOsG5XBWOVvj6DUmnhXHY4UYSUSqchnHZuNJJ8HuJsQuYruOGSGMlaTXmTRa9DSnZAz-dK7p1a772Gs9cDysp5tVIASxt8CiDKfVgPI8AUsz0SsJwsFWQK-LZGXo8twZvDsfAANapsxy39rwKviztPxilOVpSmdV4vB5SNajbr-dcDKbfU20Wy3qOfiOabzIk_Bo2JDgaJSjxx_xWcrzMSugOkVqQqbmiW6ZdDICGb5VNTewPpQq1niO4-Dz8PiWPpyRnMe5BgMYwRgN_4mVByLC7VygIQSxBCjXI0VVBId0LWybmtgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آماده‌سازی ۵۰ میلیون نان و استقرار نانوایی‌های سیار در مسیر تشییع رهبر شهید
🔹
سازمان بسیج اصناف: با مشارکت اتحادیه‌های نانوایان سراسر کشور، ۵۰ میلیون قرص نان در حال تهیه است و ۱۶ نانوایی سیار نیز در تهران و حومه آن مستقر شده‌اند تا کمبودی در زمینۀ نان احساس نشود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/445959" target="_blank">📅 03:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445958">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe5f5092e8.mp4?token=tgRP-WnnOKTFTxDpMBaACDzAsu197eJ8THkMUd_Dtgg9Qnv-NekTFU8PiKiomh6GKmJGDKDupUW25SM1kXYb2o3Bw_l0B6oipvtlfooB5q1q79NbXtgPRPHFj1DwZC4ebmDmoqnznVsIHnqpWGcvwerGbItQbES74Wzf8VYyosWwcaz0Dt83iNqMjvVhrqwD6NG37NZeAqIk2Xk5BW1qjIZynrARm4u8MBxwTcSmMTYg53AubgkCz3O-ogzVhrvGMbf2idn-D3A3N-mondjkyPqEJBos1vJ_BFkPib-edoWpbdhkNL-VIKzszKyRnoFZ9MNIsrRohK3lcU8EYFNgnZ5YwNDwyRRGjv7i5dW6lPd784FFcRcZ9tA_T4hcK5YV_ECtEwTEtyB1v0UnRRqW8rDyHnzSEaEKGDyDuKXHSbkQwkI7mRId3UKXMRbeFnVDduzGNQb98pxHUpjJ2VOIPlrS2gDwL1ka9lV7QfuP7lRzkWNs-27HE38N6DraUaCF2Vp917NGqoHsEPi-ojWwNSG0Y5iaYmEAiPPyS5-Y_LHFT8nV_9qYCVAllCJTFVkEAvBA2J5NqgRWYDMaptcD98IS6qu5p2jXL4vL-Bk3pEyD8uChOWktLSQpH3lKpIoXMAzrYOrqYzWDQXraZshDtbrf2Vl_2hn0D4gbfBbK7D4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe5f5092e8.mp4?token=tgRP-WnnOKTFTxDpMBaACDzAsu197eJ8THkMUd_Dtgg9Qnv-NekTFU8PiKiomh6GKmJGDKDupUW25SM1kXYb2o3Bw_l0B6oipvtlfooB5q1q79NbXtgPRPHFj1DwZC4ebmDmoqnznVsIHnqpWGcvwerGbItQbES74Wzf8VYyosWwcaz0Dt83iNqMjvVhrqwD6NG37NZeAqIk2Xk5BW1qjIZynrARm4u8MBxwTcSmMTYg53AubgkCz3O-ogzVhrvGMbf2idn-D3A3N-mondjkyPqEJBos1vJ_BFkPib-edoWpbdhkNL-VIKzszKyRnoFZ9MNIsrRohK3lcU8EYFNgnZ5YwNDwyRRGjv7i5dW6lPd784FFcRcZ9tA_T4hcK5YV_ECtEwTEtyB1v0UnRRqW8rDyHnzSEaEKGDyDuKXHSbkQwkI7mRId3UKXMRbeFnVDduzGNQb98pxHUpjJ2VOIPlrS2gDwL1ka9lV7QfuP7lRzkWNs-27HE38N6DraUaCF2Vp917NGqoHsEPi-ojWwNSG0Y5iaYmEAiPPyS5-Y_LHFT8nV_9qYCVAllCJTFVkEAvBA2J5NqgRWYDMaptcD98IS6qu5p2jXL4vL-Bk3pEyD8uChOWktLSQpH3lKpIoXMAzrYOrqYzWDQXraZshDtbrf2Vl_2hn0D4gbfBbK7D4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بعضی‌ها دینشان گلبول سفید ندارد!
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/445958" target="_blank">📅 03:19 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445957">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">محل وداع با پیکر رهبر شهید در مشهد مشخص شد
🔹
شهردار مشهد: محدوده بدرقه و وداع با پیکر مطهر امام شهید و خانواده ایشان در مشهد در ضلع غربی تقاطع چهارسطحی آزادگان و در محدوده بزرگراه حضرت سیدالشهدا خواهد بود. @Farsna - Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/445957" target="_blank">📅 02:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445956">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">وقوع چندین انفجار در پایتخت اوکراین
🔹
رویترز به نقل از شاهدان عینی گزارش داد که صدای چندین انفجار در کی‌یف، پایتخت اوکراین شنیده شده است.
🔹
شهردار کی‌یف اعلام کرد که پدافند این شهر درحال دفع حملات پهپادها و موشک‌های بالستیک است.
@Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/445956" target="_blank">📅 02:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445955">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qzczy55HkU7BxHX84qMHx9UuwpCaFpiItHAUYyWxNerLgf0TaBtcXaNgJS0HJ4ZcXp3sDd1pBFNbfynY5LSCfBTQWX7CE6YyPD9767l6fdsueq3-0Hlw18BusCtNQLnVGIpSWnPNl_llfO1rhAblQWTM3BLKWjm3-tE_PWxDxNIcfRcSVOj9jGTXW4xI6BkW97jBjTZXCbXQkW3T5K0d69NlleHlRDBibt6wP0Ki0-QWfmwEZQ4LEKCrOVstRTNg-0dOmidpz5rfM2wvgDsvspvfQSRym7eEHIMZP1TXBve3LO2fZOd-N232oNZ1ZFYnr_Hv38mP1PaopAyak4L3JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
نمودار مراحل حذفی جام‌جهانی ۲۰۲۶
@Sportfars</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/445955" target="_blank">📅 02:39 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445954">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔴
حملات صهیونیست‌ها به مرکز نوار غزه
🔹
منابع فلسطینی از حملات جنایتکارانۀ اشغالگران به مناطق مسکونی در مرکز نوار غزه خبر دادند.
🔹
به گفتۀ منابع خبری، توپخانۀ اسرائیل مناطقی در شمال شرقی اردوگاه آوارگان البریج در مرکز نوار غزه و اطراف پل وادی را گلوله‌باران کرد.
🔹
همچنین پهپادهای رژیم صهیونیستی در ارتفاع پایین در شهر خان‌یونس در جنوب نوار غزه درحال پرواز هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/445954" target="_blank">📅 02:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445953">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ubSoh2CHAd5s3Ll1MMvTgwii-bcQtKIZNtnvQoX3AHhDLA9ml3mFpM8cOnzPZzOaqEskikcBI3h2PEW1RcPXlgPpMQJKa0oef4v3Uc3596xmPLQUCeA3CXAeRq-xh62S0plxNrxqjwKVVy3Blhng-P6qKcOFiH6U-RJXImSuqR3jYFj1bMykDDKcvYSr2dC8cB5rV4tnUZ49OkaMIB_2lT_7UYagwMdmQe9-tNAI_hLcpM7oAmsm5HYe6P72yGC-0WKH2HA0e-yuDJ9CNMMBdIUyHINRSWhjtul926twYodIgRxF6-LyNvlUnTWCu0u5u52dZQbkrGNRu_ZU7nBxgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلای ژاپن را سر سنگال آوردند
عقب بودند و به بازی برگشتند
بدون دوکو، بدون دی‌بروینه، با تیلمانس!
شوک بزرگ به سنگال در یک‌قدمی صعود
بلژیک ۳ - ۲ سنگال
@Sportfars</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/445953" target="_blank">📅 02:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445952">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">حملات توپخانه‌ای اسرائیل به جنوب سوریه
🔹
منابع خبری از گلوله‌باران حومۀ شهرهای قنیطره و درعا در جنوب سوریه توسط توپخانۀ رژیم صهیونیستی گزارش دادند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/445952" target="_blank">📅 02:18 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445951">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">جزئیات تعطیلی واحدهای قضایی در ایام تشییع رهبر شهید
🔹
تمامی واحد‌های قضایی در استان تهران در روز‌های ۱۳، ۱۴ و ۱۶ تیرماه تعطیل است.
🔹
تمامی واحد‌های قضایی در سراسر کشور دوشنبه ۱۵ تیرماه نیز تعطیل خواهد بود.
🔹
همچنین تمامی واحد‌های قضایی استان قم در روز سه‌شنبه ۱۶ تیر‌ماه و استان خراسان‌رضوی در روز پنجشنبه ۱۸ تیرماه تعطیل است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/445951" target="_blank">📅 01:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445950">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">‌
🔴
برگزاری مذاکرات فنی غیرمستقیم ایران و آمریکا در دوحه
🔹
رویترز: گفت‌وگوهای فنی ایران و آمریکا به‌صورت غیرمستقیم در دوحه در حال برگزاری است و در این میان، قطر و پاکستان نقش میانجی را ایفا می‌کنند.
🔹
نمایندگان اصلیِ ترامپ در مذاکرات با ایران، یعنی کوشنر و…</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/445950" target="_blank">📅 01:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445949">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🎥
دلنوشته‌های مردم در «کشوردوست» تبدیل به نماهنگ شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/445949" target="_blank">📅 01:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445948">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YrniQv1lwJXmk0fqooJjC6p4FVSMH4MHwiOSxqaIATUmQLZEKEwwI9TwJREli6NyAKCH3u5RPsOqgX-UqyQ38G89IbtX8cq_mpK4DoCfJvUJQrSMy7eR-x3dNPCBDEMk3FmVc4YZXAJKbo4mjAWqs8NByUewHBdCyEqGg_dnU2eJVxlX-VeT_q_2wNG0IMiB6U6PBabIuMniFGAUb7pSE8b2J6hAX2V2a410GnrNJpTxj1ZD94PrIS5gzO29TUEwLTRkAap1lKfKI7Tp7V-JVVXGx2l1VArj5sHmil27Mm0UNIgf4c1PA2mZyKB7Z8kxk5XaYmqYP_1lbCprdb2xnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازگشایی محور هراز پس از ریزش سنگ
🔹
مدیریت بحران مازندران: محدودۀ پنجاب در مسیر شمال به جنوب محور هراز که شامگاه چهارشنبه به‌دلیل ریزش سنگ ‌و به‌منظور حفظ ایمنی مسافران مسدود شده بود، بازگشایی و تردد در آن به حالت عادی بازگشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/445948" target="_blank">📅 01:16 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445945">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd491fc278.mp4?token=VUmSYXJVUDCPeWIsk3fbPvUQGNv45J4hGAWJxtfirNI_8HzBvBPTum_HwQny6KJXAxJB1N55nMEmzcv1FP6S5hbqV6mV7CyO7iDhOUPI3jvxhf3Hoq1R6SlX6UJZmTpyFxXXTpP1hvbnSeqOiWoBikccGOkHxVeiiKoltUBHySWq85Fezzh5k8-lfxrIaYcw6BQhLX0e1tKF5r_bfM_u2qb95C_4yMVdsP4a8lC_SNDu7-nxXajbjDVOQXLVX3mdgWpqg4-IgRWpbY9ksK3g6jwJKxV4VD-HEaqoI7z7iEvCc2rYil6N1j5M8jar4syrzbno7kcb3a0g68cw6Q-w6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd491fc278.mp4?token=VUmSYXJVUDCPeWIsk3fbPvUQGNv45J4hGAWJxtfirNI_8HzBvBPTum_HwQny6KJXAxJB1N55nMEmzcv1FP6S5hbqV6mV7CyO7iDhOUPI3jvxhf3Hoq1R6SlX6UJZmTpyFxXXTpP1hvbnSeqOiWoBikccGOkHxVeiiKoltUBHySWq85Fezzh5k8-lfxrIaYcw6BQhLX0e1tKF5r_bfM_u2qb95C_4yMVdsP4a8lC_SNDu7-nxXajbjDVOQXLVX3mdgWpqg4-IgRWpbY9ksK3g6jwJKxV4VD-HEaqoI7z7iEvCc2rYil6N1j5M8jar4syrzbno7kcb3a0g68cw6Q-w6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
منابع عراقی از وقوع چندین انفجار در یکی از مقرهای گروهک‌های ضدایرانی در اربیل عراق، پس از حملۀ موشکی و پهپادی خبر دادند. @Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/445945" target="_blank">📅 01:04 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445944">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/718ee7abd4.mp4?token=kWvOPEpk5ElF8M9V1AECTfmhk1aCXEVr-j8I7d2B0TNjiX3aH5JQ94qLW1LjfsIBrqKJX4XHMz3n94bay_ABk0A2fQhpTajctyQzkE9rkPUhfNIYiMzcTSavywWFv6oy58bZupfZP58Ypl67QJwuGdTmZH-tlf3YiruJkToyKMf4XdXKecgK_9UsRDOPrLm-NA-O3SFSVDQR3ZKmzEb433dgya2NKPJMF2NDxWOVRNoVKC7lXq3gYCKyidqVFD-EifnmMM4pig_bJJguoRksHRHFqfP_ds5TwYrfrUkJD8exiMzRBrW7SRJNfY2tFKmlnBFUFY_qymhuLs5zlTZrcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/718ee7abd4.mp4?token=kWvOPEpk5ElF8M9V1AECTfmhk1aCXEVr-j8I7d2B0TNjiX3aH5JQ94qLW1LjfsIBrqKJX4XHMz3n94bay_ABk0A2fQhpTajctyQzkE9rkPUhfNIYiMzcTSavywWFv6oy58bZupfZP58Ypl67QJwuGdTmZH-tlf3YiruJkToyKMf4XdXKecgK_9UsRDOPrLm-NA-O3SFSVDQR3ZKmzEb433dgya2NKPJMF2NDxWOVRNoVKC7lXq3gYCKyidqVFD-EifnmMM4pig_bJJguoRksHRHFqfP_ds5TwYrfrUkJD8exiMzRBrW7SRJNfY2tFKmlnBFUFY_qymhuLs5zlTZrcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
منابع عراقی از وقوع چندین انفجار در یکی از مقرهای گروهک‌های ضدایرانی در اربیل عراق، پس از حملۀ موشکی و پهپادی خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/445944" target="_blank">📅 00:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445941">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PyM5VwoYIJ-4RABAJD_xsG8YMOIfZag5LM9LePt1AaBFRQO6aucQAWPidPjMLgfs0VY2CV0wxX661PPMo15be7kvBwrUQSHIUCdFhJwLZ3l8jUFgYsFf2aNS2X0rt3JISdm9jdkA-M0lz7nTXMA-_sNHdhVgbKuiEWMAVBomaROCv3Qy5XiaImvdt7iS9Flvgu1-LljRI97AhjKgxPWkVBrWSWuMKQQtUcClcF2zMdkmUnxin0B8TqfoYtS4gzP3fycyK0U8bx35BVZFC1elMQdxMWqZgDdaRrZ4FpTym3rkfIGYQNPBNHck3cipHYJDQLywZ8aWKsKwNv5f7QeAZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QnfokLda0HtCETJrMCVhfNPUgR4mpZZDRuR4r1VDhEh-eqFVnNuMGsDPq9RQCGdvAhDdZOz5SXNDDnp_nsCNtDaeWFqRJWA3VGs2S5lqZEjA8yiUOmVPlOB7A-IxU9kr6Wh8Wn2Qg-p1B-l6q21EStw0hdZqLqkc840ZCS0mlPAYVZCYnsl09nOYpuyWTwjLQIysnMKf35P6zfqefTAzRnBlF4PTuBYB9L3ZMLsklZ2uTkZIWCW65Twk-lniyLKePrpP9UlE5X1DES5qsx87JvjmuV2-skHl0jktEX5wlbXtJjt7fSLxX0G_DLkJbEWboM-hRoOjmzOodvwtQO2ToQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LUU0SyoafYp6rBA9dyktfxuSnGGP3UQczjVj99lR8qmGlZ2QkPWPfOayLAHrCk8kFT8iPN94vatuT5VD-6HT3xK-ZVr0uxu1YZxdYQYtCIeTcGWS2VhsX1-Q24XJVXKE2dlin5kc9FBwOb2-gjuKPRN8HrOblLabiEw9EYScTtHIGNpntHZBwBDxQtFOUeuU3CryeSo4zd9SjWWq1iRP1MzEWy_xS2cS-sixHYYRzkqRF4IokI6fIUpC6J9kn3me39YH-3gRd-RaASDPilLtQtONDSgVBLlJSo5bvlQZhlaKvhAONkqVu1uxKvtliMqvXrURcMdvdF4vheUUEP57ww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | پنج‌شنبه ۱۱ تیر ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/445941" target="_blank">📅 00:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445931">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ldaXFx3l3frLFWQhgntFF2LKnPAkoaeuA_eui9rIynjG6NBGZW2hSF63-y6_i98tVhzKGRWhnfZ-Rb5H40_b9EeHz-_3wTdOdrLi4iFMYRCUF-Zo38zpjYqpUyreZBfk9DXHbxECSpAqF9y0mIgye5s0qJKx-7QCoLB6uDWPvqdkc8UXlKYjVmf7wonL7MawSrExslxcK6KrmfD0lw1Yj9MFAgNSPH-CukYhV6rGL0kYSlLW6rW7XMImZsoyTr_zaDcGKEgNUrTH5RhdMUz5ZahlEpTrpjvAHY8_qyGDXb-_bOoFT465Hatk2OxXVUa1WGtZDCP_PbLQPy4rX36lag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lKMaH2fQzGocoCBR9SVpyIOAi_bh2zZza8on8DOKCtxJHuqWLaBe4BG02Y2-93fGEhQyEZ_fNsKldX9cC5SV-N5QqVtWywip-5d09ZHX-bsIcNvhyp_riDlPehfWH445bNqw2qMMKPEby66AVryFiWouAd_2_W8iktCfBBRyPflz26kYRQwItEDny0koUhubhSUiqZr_DloPKD-vwhCCz3SmCU3xQ-32ZoI9Oo0YFNDAagAs2SwKBS5qKeGOXljZv5Sc5nKZKKvJmzb_sG9X_KP28p0shMk17VJ-mauKMdgjToNMZtI8CoPxwhB5_MIpuO3bjZjgX5F8CxR5E_Mg9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/baNMu9wI5MC5oKHuDiYfNxr8mUCm6by_AKWmVwsitxAaU4H4w9i2O9q7J78WSS4nJsHS46cYwvcEZekIzVkkep1JlUM-3EYxYCeL_lLUGWbxJ0JckjJqS1YeFsEWtNivJW1FNoyytY3tzKfRtoURKrtvNA7k4OeyxAxxBgRE6zw5exfLMq75bz4uyDPT0XY9ONE7Hpi1L0Y33W6Tj5Zh1XkApa06BNZuiQgcnn2CP5N6sw1sRz6e70HG5_F3M5dJeQMZqa8gCqI_c1-NpHghHcgPa8WG388B_3qrJ8NN9D0wAIE6PJg2meZh6meH9Y3nLggBeAJvfR46C3cDqYNqdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qEiuR4XRQ8713XBAd56l9d1FWkxeq58DQBFp4Q3ugKe3-pgWRD7fh48IlOoNnZtHvaUMwm--WcnpxDNfG2WgDSElh3eu5klURSqr5KE-FlGNa6WrMJRfUZKO2VqLEEqwSnwigPeN4NTJPO5nMsr8S8eKyr2E5NRfF4EtgHfHzXbcVAitVfPSNs2zuXSdbrx7BQYgVIp8GvVP5bE22L9UU4gpUcQKV5FxVfTmAACGgJYSj7GXpUoiC9xHJbHSTxXmPFNfdgNSGlTwxMcRcHUDELDFOF_F9aBzLTxrw3aB20WxxoiO1x5bRqXFgXEtKiN3OlCyOycjxBBuWYIUo8SLiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d4Rba6zTtg_xlTVBIgbUyfYcwAIXtFaePTqUoHGeXo-5dB5fOqlMtaDoe_OD1AmNMYAOtI5y1ejj089EWMs3eWsyjUldTqXW_KoX9hVmR9JyqCInpqwkzJyb65vL5BjlseYYZBNSXT5wc3x9U_Gmq1vnxLNU8m_JHWGpZbN7ZiJ7QdBDlWY6OXjta4I9k3u6fUEwMuMt50TDDlASJf9e_42eOv_GpSf5EiNe4v54PNITbs-UKzim-kFcbvEgh0yx7JueanFSpXywciF6d82USHfHdCQY5Nnkd-ME3mcEzR-uLa1WX9vMvAePzofSojf3993wPktxJGKctvWA-s5BUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pGETAaVtlLwdCJ9Fb2r2PKd5v8o45B79eVivmBGgZVXzK1cGvuruhWrbuujezOWi5DtkevlswoEOYj07zJeV7m0pwrIKNCn-uXebfPZHF8aOmP9aRz0IXb60v7hwEzFuO4pMm2grvc_T0E0LDtnu6KokMJaq8pZQeAIShZvoC7QYFleuD2p3OvKyvj8DZPCoXZ4uT_04efwwUPC8E6TbKa4mczPyD1OJZ0s2gR9wN_TA0II3k82V3CZmC3ouA67wJQAFtfQdC9phnMQIQ7Lsc8gNmkmSGzNwtwhQ_c-WU4e3fzYQYedso9C7IEFinISV8BNCEcrs1uG1cmVIHHRcMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ugy9CHeRMwhswj8wdorT0pyTNmpq_9ckN8N5x3Ex0k0DjlPLinvE_0-nfkT1otp8HW-hSY39VspuPSVoqDaJO7a6vjYtr7IG8QIYYrTS8iZ9jnqf1_7HFTFJg7xL4tcQv6Ik8eDQ8qPzNExjAQX-FHx6cbU1GpxZb_TLwNIzIBPKR5EAIQEnTlPi-rbIdu_ce7cFDuR6IlNTtC3syFIC8lHexuMi9YqquVetKPTe_YYwYFnNmSvxgLkNMANCGFBXXus_1JwDtaUOsFmjI2KVGkLufWASN_OqEnujbga2GNovqtyZMlwBCQ4VKR3maVNa_QqSUtHngEDQ7w2Q8MTQXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A_PCZwOc5dsS_3BKOdz5kY-vh_LJANnYVs0DxAzu8CqWpHHX_dbRlbpxuZINAf_kBl4ZuAef13t98svRshccSVMLOdOlzdjzGzuxITqJNmUxbDN7A3sibIL-M9uKbia20uL9lPW9Xcm8ZSJHZhYMLYGtsE7QL2-5aSQQyiEEMGH35B5U7KsXpo4B9t6a9EUeLBc5iznxBkSN8XWvT1E96UtTLIKWkkFVN6S0awhgf75DpATyUhj1iZhMVs9tny_W-pN73IqeeNHAMsnWFyEKxiU63ZUFngSishbYTygoFyBeS8WeK22I35F38WebfdlKdFxiJcMDr-1M9OCiXYr4RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JVR1Iq0a3eFoGGc0ZRQLmUoqu7rfNfVer4GNgM_uFwAbLxu639KdniOz29__vKhtVru19kEeq8QNZy8NZZx2selXVBesl7u0cDm6DJ2pAWE9lF4nklLlYWZ1TqMhmLwfdxqcGAjfVu_K_63m4eUK0Y7_anldWArCJeNgmG8x236htXczuwzbdZXlIGioc6H8lBIdDtC_raqkWt7CKo3aNI3zEOoLpYPS-CiHOZzlrczrJ2sckJjACxIzQW8l38CurD88wIYprcHlb9weJAtWyHlq7wUgzBzxEAOmdndeciv3EiWoiYHDkBwPG6LvAPY1lUQdZpej4cRmWS8NyM-W4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sX3PC3qKj9dVBjU7DrHpEwl8YbcvML7KI4g8aPxz4YBajMZhLiZO_r-n25ymyuTmJgDhVQMRLvrzeVnQDsXkGlnqy96TyCTsZR0xEcTi9KDjFpTLNFUoaodamh4vng8Xy0VGB7_3JcH1b2fQHm__FEtmWQINlnQnq6GLVQyrQSs7G_YKYQYwJO6n7Gt13WCzLw6jchzUEkFTAtnxT-8UJDJ_TEbKB0s2lWVQLIbLs6zWyelxchjLc8DH_DvuvarCjmvYkZXbNujLxczzSXkK7kTiueIyA42gLX7d4jNyo73gh5kTFfrjtlagWDp4LBp1tVJA2gYA3k9JtVZSnE2Xmw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/445931" target="_blank">📅 00:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445930">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VhPPMu2U4GXIW2PRox4KCIEhTRCLGMo0luxXftBaikF9SWQqbVkEMgvecxgjV-jxI7aJRhmk9gXYYDnlKcQ-crTPNWe9Q1g9U9FBZPUqu4D5MepYhB-Zvcz7qfvO0MNh8qzgabUGcT9_6wqVCFCINfiXBxVzG7wwe7umk-RJDeRgEQCugaO_C1YDZ8cvTmFMQxzTityRwBKROWrTWHQN19b8in0qyAh7zhYDUQnEpzmpvgBE33MzeUFo-aC5rN65llF3ZMZQyDlXY8Q5jd1hNwofKmx_b0jx6JqWrLlOf_Inf9g0IMqZ3JKetiWALJQaOadZZxjc2M4p2B9beB4rGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اهدای اراضی فلسطینی برای ساخت سفارت آمریکا به قیمت ۱ دلار
🔹
رژیم صهیونیستی و آمریکا توافقنامه‌ای را امضا کردند تا سفارت آمریکا در قدس اشغالی ساخته شود.
🔹
به گفتۀ سفیر آمریکا در اراضی اشغالی، قرارداد اجارهٔ این زمین برای ۹۹ سال است و ایالات متحده مبلغ ۱ دلار را به اسرائیل پرداخت خواهد کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/445930" target="_blank">📅 00:24 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445929">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lb8gATv_jxk7qB2qcqjvzTbFM_P7AKFgVE-fszocRk-hG4Z_ES_ycDHKTYW14qhegFg29hHS8yJL3ElaTEPqiCoUFGlZhSN2sY9BEovPs445v7HUHKKMTWQBnHMJmpUI2Ju8k7dkg4z9ncCQVlv_5G5sOvxDRSLYaB1lChUC8VKWIPKFu2rvscljK0Vb7A_qU99Y7DxRVK8lI9spn8CzJ8EaNwrmfArb2nVGLcDH6yyQA7gtHS8Cz6x_wySUMlcPncWzPC9kp9OBM_Qn6Xdy1TpS5MBspVj5G_3lVnop5dYIna0xW6jMUXUP1vMjmtrwIcmMI8tpi3va-gjbB2zm1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سفرهٔ شراب
🔹
«منصور دوانیقی» خلیفه عباسی سفره اطعام بزرگی پهن کرد و بزرگان، اشراف و شخصیت‌های برجسته مدینه و جهان اسلام، از جمله امام صادق(ع) را به این مهمانی دعوت کرد.
🔹
امام صادق(ع) بر سر سفره نشسته بودند که یکی از حاضران درخواست آب کرد. اما خدمتکار به‌جای آب، ظرفی از شراب را آورد و به آن مرد داد.
🔹
به‌محض اینکه ظرف شراب در سفره قرار گرفت، امام صادق(ع) بدون هیچ‌گونه درنگ یا ترس از ابهت حکومت خلیفه، بلافاصله از سر سفره بلند شدند و مجلس را ترک کردند.
🔹
هرچه منصور و دیگران اصرار کردند که ایشان بمانند، امام قبول نکردند و در پاسخ به این رفتار فرمودند: رسول خدا(ص) فرموده‌اند: ملعون است و از رحمت خدا دور، کسی که بر سر سفره‌ای بنشیند که در آن شراب نوشیده می‌شود.
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/445929" target="_blank">📅 00:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445928">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f205d4e95.mp4?token=A9sdx8W5pCf3a0c0lv6Y2sFsEHpUahqdd2HtRbrla9wGLtJOIVwG-cgCtzBM9Vzf2H5Q_SH0TrEgM0GbsIG7MGkkh6NVbQSA6GBftXS7s0lfI-NkI_BI7eG19PRz974SakNxehdreybebCAJX0_LdGSlffnVUyUCgMd3YYDCLk1nRpRJ5iICSSOIR-VSpXz4xCmBTb_s56Lu87nLOG66SOORII_yk9jYy_0e8HsIZcrwPidls193LNia7_XSrfju5ea2dYK3nk1EvRHk08hKeZHANzIv2_MKNUVFY9zVFg4laX_ZH0H6XQU9pCtRokPKpZMbjQoWqjW6X67xE3mxNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f205d4e95.mp4?token=A9sdx8W5pCf3a0c0lv6Y2sFsEHpUahqdd2HtRbrla9wGLtJOIVwG-cgCtzBM9Vzf2H5Q_SH0TrEgM0GbsIG7MGkkh6NVbQSA6GBftXS7s0lfI-NkI_BI7eG19PRz974SakNxehdreybebCAJX0_LdGSlffnVUyUCgMd3YYDCLk1nRpRJ5iICSSOIR-VSpXz4xCmBTb_s56Lu87nLOG66SOORII_yk9jYy_0e8HsIZcrwPidls193LNia7_XSrfju5ea2dYK3nk1EvRHk08hKeZHANzIv2_MKNUVFY9zVFg4laX_ZH0H6XQU9pCtRokPKpZMbjQoWqjW6X67xE3mxNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عزاداری برای رهبر شهید در اجتماع مردم نیشابور
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/445928" target="_blank">📅 00:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445926">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fc0b27d69.mp4?token=LQwIcQ40n_vC2UdGxBciA1vY38E-MDR9MWVcCeAZlMWCalo-uHjAB9yRfxJ4UkMMCgK51xYlo9pFJysBbUL25bZ206pkhmPw0XRJl_NLAFLdvbmQ_oE7LEJyzvvtAruqYgVMttHbSjMdTMPkXWDaTgfQXeUpsJN82cpGLo59_o80e-RRHnpy117_tgileNoDqpPQaBBDHQV_p3In_GfX6pQQXi8Uo_EUNkNDC2u31K1Io4Fj5rUssLsk1DGYWbr9EVIA1rrUN4mLiyiSykueJRTI4PuJZkJH0vo6UyHJl7G0e4DmGvWKAHVpn08VU-GdrxiH3NmK14cq22U7tr4vag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fc0b27d69.mp4?token=LQwIcQ40n_vC2UdGxBciA1vY38E-MDR9MWVcCeAZlMWCalo-uHjAB9yRfxJ4UkMMCgK51xYlo9pFJysBbUL25bZ206pkhmPw0XRJl_NLAFLdvbmQ_oE7LEJyzvvtAruqYgVMttHbSjMdTMPkXWDaTgfQXeUpsJN82cpGLo59_o80e-RRHnpy117_tgileNoDqpPQaBBDHQV_p3In_GfX6pQQXi8Uo_EUNkNDC2u31K1Io4Fj5rUssLsk1DGYWbr9EVIA1rrUN4mLiyiSykueJRTI4PuJZkJH0vo6UyHJl7G0e4DmGvWKAHVpn08VU-GdrxiH3NmK14cq22U7tr4vag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چادرملو برنده شد اما ممکن است گل‌گهر به آسیا برود!
🔹
ممبینی، دبیرکل فدراسیون فوتبال: از AFC درخواست تمدید مهلت معرفی نماینده را کرده‌ایم اما درصورت موافقت نکردن کنفدراسیون، نماینده ایران بر اساس جدول لیگ معرفی خواهد شد که گل‌گهر خواهد بود. @Farsna - Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/445926" target="_blank">📅 23:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445925">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🎥
امشب طوفان گردوخاک هم مانع از نمایش غیرت میبدی‌ها نشد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/445925" target="_blank">📅 23:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445924">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12e8562b1c.mp4?token=AULUbs9K4miWh55XRxWH2pZcRKTB3DjcTy8hZOW9BXONUaBbvqKmwJzpNcGmnVALWUc4MOjwxYB4xznFmVdXU6Uz7WmKcV_ytjnZ63tWz-QeD-qf9nlRai463xj0X-FlK-t9MxY6SY2e2CCsFkr_m3vRfBQ7VigmF7LeP-wUMZZdz0-vxAGOyX2O_duRLA7x1KGizmmuLa0PBJ_C3I2oxxgs0L_48Knni3rU70H4w4R-dtcFXC0zvriD1qfTHP2bztpXv-RHQpJ2CeGxRwiwBfVJkJxBde2iL_m1Q77GtN8-DfTIHnqYByQ1I9Sff8puSWQgbMyAjQ_lQ5lcQ9aq2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12e8562b1c.mp4?token=AULUbs9K4miWh55XRxWH2pZcRKTB3DjcTy8hZOW9BXONUaBbvqKmwJzpNcGmnVALWUc4MOjwxYB4xznFmVdXU6Uz7WmKcV_ytjnZ63tWz-QeD-qf9nlRai463xj0X-FlK-t9MxY6SY2e2CCsFkr_m3vRfBQ7VigmF7LeP-wUMZZdz0-vxAGOyX2O_duRLA7x1KGizmmuLa0PBJ_C3I2oxxgs0L_48Knni3rU70H4w4R-dtcFXC0zvriD1qfTHP2bztpXv-RHQpJ2CeGxRwiwBfVJkJxBde2iL_m1Q77GtN8-DfTIHnqYByQ1I9Sff8puSWQgbMyAjQ_lQ5lcQ9aq2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بغض سحر امامی هنگام سخن‌گفتن از تشییع رهبر شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/445924" target="_blank">📅 23:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445923">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08336dba01.mp4?token=BD8YBiKVWaufTETLyBeNGhuVc4BOzPHG52mwW0vGyNWGpVJr8IcpiV_cBFgCLlXgoUBhoBMF0gBWHhMScd5oGee2MIBr-2ptXLfbDofy3yqClTtqL1aXixQzpxkKB9tMsc19mdc_ERpQp_KKrGIHO5h5O_up2OfrSWwwVaHn4gksbVE145xk1flGZ7UUUr95jEvVG6W4lRtlPdUMrc_LydWqUYS4SKHlGMohzMz9eRhIvPBwhXeX8C4m63TaaLzgHCDvYCTehCO8gV8vQOnLoORAoklzNTuZc7JvVMqqM8l0HD4DCz-ig7-Hrki_5rQy3rk9dgXwq73_v3a7rUULCYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08336dba01.mp4?token=BD8YBiKVWaufTETLyBeNGhuVc4BOzPHG52mwW0vGyNWGpVJr8IcpiV_cBFgCLlXgoUBhoBMF0gBWHhMScd5oGee2MIBr-2ptXLfbDofy3yqClTtqL1aXixQzpxkKB9tMsc19mdc_ERpQp_KKrGIHO5h5O_up2OfrSWwwVaHn4gksbVE145xk1flGZ7UUUr95jEvVG6W4lRtlPdUMrc_LydWqUYS4SKHlGMohzMz9eRhIvPBwhXeX8C4m63TaaLzgHCDvYCTehCO8gV8vQOnLoORAoklzNTuZc7JvVMqqM8l0HD4DCz-ig7-Hrki_5rQy3rk9dgXwq73_v3a7rUULCYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همدانی‌ها بازهم تا پاسی از شب در خیابان‌ها برای دفاع از ایران حاضر هستند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/445923" target="_blank">📅 23:51 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445922">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tZ2LlairVBF0HG-GH4F48WAEciTFDbt_n51EUpgroT0Cv6cRpI0Y9tXLa59BZeaOkQF75ipZ3aL9Q8DtoioZ0r2XWj8-DYLvaS7DwUFlhUtf2bh9FOE07NaG-iU9pzbcz4upROo1mw0_j_j7hfZk7Kb27XMwDgi_bFYoLSrKLBoBxBi3gDd8lm3HxBdLafqR_e4sTlJLBgHLea-33SYJex7FxkKxcYuXNWB-x6HBX4jKbCX3w_NvXGkyQqeGqLBw90AnzMZgih9EWd-nTs_r4d99ow4GKMbB3bV87Lz5uro2gBiLruHIUhrOpd5MDBwK2f4v-KYFpGD7rU3CR3Q6nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحرکات مشکوک اسرائیل در شاخ آفریقا
🔹
شبکه المیادین گزارش داده که اسرائیل محموله‌ای مشکوک به وزن هزار کیلوگرم را به سومالی ارسال کرده است.
🔹
المیادین به نقل از منابع آگاه خود افزود که اطلاعات موجود حاکی از آن است که این محموله شامل سامانه ارتباطی پیشرفته و مدرن با کاربردهای اطلاعاتی ـ نظامی بوده است.
🔸
رژیم صهیونیستی و منطقه جدایی‌طلب «سومالی‌لند» حدود ۲ هفته پیش رسما افتتاح سفارت این منطقه در قدس اشغالی را اعلام کردند.
🔸
الحوثی، رهبر انصارالله یمن هم یک هفته پیش گفت
که یمن در قبال هرگونه حضور و استقرار احتمالی صهیونیست‌ها در سومالی‌لند که در فاصلۀ اندکی از خاک یمن دارد، دست روی دست نخواهد گذاشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/445922" target="_blank">📅 23:46 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445920">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jk-Iq0U6QhHkBJNunM0v2nYSIGExwXJDQVhH421Q5KTW-u4cvEnESCn4kBstu3ED43ufQcKytvKj-vtc7SfKtdN0e6uet9dpGDVOpW2tZ9qlnb_0M806p3LOKRrYr9atOzjs2ER2IWd-7piWNyGj4qe_9HMVYrNcR8cFXUzEhhV77q1SkVKidu5UMkOjGaIw8arSr7IppYacBu91ht3CtANUNiqhXGXdPv8gU4ZYvQ965Y_SHoc06NRUG1pn9X3B5eUNZ1-5UPMalZtcaYjh9XUmok6sZltyj-RDT35RT2k-rB6ajQb-t900oAALNeNPYsxaSsjCmo-w8vUtSbpw4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اصرار دولتمردان لبنانی به تداوم مذاکرات سازشکارانه با اسرائیل
🔹
نواف سلام،  نخست‌وزیر لبنان گفته لبنان همچنان به‌دنبال  یک چارچوب توجیهی و مقدماتی برای مذاکرات است که مسیر گفت‌وگوها را مشخص می‌کند و هدف آن رسیدن به یک توافق نهایی است.
🔹
نخست‌وزیر لبنان اظهار داشت که اگر «چارچوب» اجرایی شود، منجر به عقب‌نشینی اسرائیل از مناطق اشغالی و بازگشت اهالی آواره شده به روستاها و خانه‌هایشان خواهد شد.
🔸
این سخنان نخست‌وزیر لبنان درحالی است که سران رژیم صهیونیستی از جمله نتانیاهو و کاتز در روزهای گذشته چندین‌بار به صراحت اعلام کردند که از منطقه امنیتی در جنوب لبنان به هیچ عنوان عقب‌نشینی نخواهند کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/445920" target="_blank">📅 23:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445919">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22ef7922d9.mp4?token=lDvTrGoqMpKJtj6-hrALaHBB-lRHaFBB1aQnz2igw_FqPhzM6fkZ4_v56l1WOkCnnTE_TsGda3tVnzzK8QUr3-3cXI3OCsB9B6g64pqE-bYdW2TxdqlihwYfvXvnKw0VhjZ8gIgidbttg0EkJecEq_XgJvwZM-2nbijHUjPjU_U1JVnOg-tLMfzGJKGbpkDBQK4SP6xyPGRQGZeSnhS8K1Ix-7U4mNnKQleTw8SOxBHBDcjVoeZRWCrp8ZLTGMormNUKTVitE8Bf0jhIWIh6VVUMlxVCxgPGxVfObJ9x4Nol1Tok38i9mmHvc1kXLG7ERAxGET4eXeas70CXxFupgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22ef7922d9.mp4?token=lDvTrGoqMpKJtj6-hrALaHBB-lRHaFBB1aQnz2igw_FqPhzM6fkZ4_v56l1WOkCnnTE_TsGda3tVnzzK8QUr3-3cXI3OCsB9B6g64pqE-bYdW2TxdqlihwYfvXvnKw0VhjZ8gIgidbttg0EkJecEq_XgJvwZM-2nbijHUjPjU_U1JVnOg-tLMfzGJKGbpkDBQK4SP6xyPGRQGZeSnhS8K1Ix-7U4mNnKQleTw8SOxBHBDcjVoeZRWCrp8ZLTGMormNUKTVitE8Bf0jhIWIh6VVUMlxVCxgPGxVfObJ9x4Nol1Tok38i9mmHvc1kXLG7ERAxGET4eXeas70CXxFupgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: کانال پاناما و سوئز باید برای ما رایگان شود
🔹
رئیس‌جمهور آمریکا در اظهار نظر جنجالی دیگری گفت: کشتی‌های نظامی و تجاری آمریکایی باید اجازۀ عبور رایگان از کانال‌های پاناما و سوئز را داشته باشند.
🔹
ترامپ افزود: از روبیو خواستم فوراً دستور عبور رایگان کشتی‌های…</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/445919" target="_blank">📅 23:24 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445918">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jka_cwTwM5Ji6fnwae-SGWHIXDV0ByeBR1vI6cIfFzpCd5zf-al4EvHOt912u4UDfSfGgdKUSSl4AZjPZGUJyz17dapCxFsR3_I_FbM8rKELt0uEdeUxFRbRrUn5OQMamfRPUgyWdNgjemfpW-RhgJGdnPMMajGzTG-yd7NAWw9XLgMd8qNk_i6OCZcXpSY925yiMfJtTeb0vrlF_kI-rsWqEVJ9x5EonSdJ4IGT_ODDKGoR1lJ2nleautzBupNBgP7nlST4Puzbq9LoIrj5uD0Y8k8elPnKXrkcKBWzsHCUSlkf8_RF7iB1XfgY31iJupL76Cfecz5UIrUj0GNVwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایان انحصار دبی در تجارت خارجی ایران فرا رسید
🔹
جنگ اخیر و اختلال در تجارت دریایی، یک واقعیت مهم را دوباره یادآوری کرد که اقتصاد ایران نباید به یک مسیر و یک کشور وابسته بماند.
🔹
پل‌مه، دبیر انجمن کشتیرانی، دراین‌باره می‌گوید با کاهش تنش‌ها و بازگشت ترددهای دریایی، مسیرهای تجاری بین ایران و امارات دوباره به راه افتاده اما ایران نباید مانند گذشته تمام ظرفیت تجاری خود را در این کشور متمرکز کند.
🔹
او می‌گوید توقف کامل تجارت از مسیر امارات به دلیل مشکلاتی که برای فعالیت‌های اقتصادی جنوب کشور ایجاد می‌کند، امکان‌پذیر نیست اما می‌توان با توافقاتی با سایر همسایگان مثل پاکستان، عمان و عراق وابستگی تجاری ایران به امارات را کاهش داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/445918" target="_blank">📅 23:14 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445917">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4bb1c38d9.mp4?token=HsqdVe-S9JFQ_VSboYdg8xBFzPmqQpmulz0IqhSo3tc-zMi_DWuD46CFlN3Tk2muUcA8ArO5K80eWyNPde--JUxJyzz_HOKnBxOMlbu3RMqHhfAlp8100l_av_1o8i4WIqoFpySXSnoZSxQKQpHQvi-pxnD85s99A19y4tF12uSirxHDWOl-xmp6dY38hdK3eczSKZVQHLK-5yunI3qp2sfKRdhiunly1cs13ZtFVqWZzCG94VdxQiWqhOgCcb0H_3R5r-8aj-DSavJ5TPEveGWrZ3RozRH4_DJ7WzPDfpAqDwF9bO4z_PZgALn-HM3ea266wK60-YsP1vx328lOMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4bb1c38d9.mp4?token=HsqdVe-S9JFQ_VSboYdg8xBFzPmqQpmulz0IqhSo3tc-zMi_DWuD46CFlN3Tk2muUcA8ArO5K80eWyNPde--JUxJyzz_HOKnBxOMlbu3RMqHhfAlp8100l_av_1o8i4WIqoFpySXSnoZSxQKQpHQvi-pxnD85s99A19y4tF12uSirxHDWOl-xmp6dY38hdK3eczSKZVQHLK-5yunI3qp2sfKRdhiunly1cs13ZtFVqWZzCG94VdxQiWqhOgCcb0H_3R5r-8aj-DSavJ5TPEveGWrZ3RozRH4_DJ7WzPDfpAqDwF9bO4z_PZgALn-HM3ea266wK60-YsP1vx328lOMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: بحث دسترسی بازرسان آژانس به سایت‌های بمباران‌شده کذب است
🔹
ما هیچ امتیازی بیشتر از دسترسی‌هایی که شورای‌عالی امنیت ملی تعیین کرده، نمی‌دهیم.
🔹
طبق قانون، تعیین سطح دسترسی‌ها بر عهده شورای‌عالی امنیت ملی است و آن هم چارچوب آن را مشخص کرده است.
🔹
در…</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/445917" target="_blank">📅 23:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445916">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6eca2186e4.mp4?token=JNA1AX7cMKOjl2-rUhigv7-g2x5cIa_OWbkgYEWVMavG8KJ2cImyGxuAz6XQ4dkh-12U_I_hvfGPDaJXriuzCvy_DMN9mXljTkIkj9oZ3QeFRDunxdgzngYN5MgLM3fkJH3AvWstiH0-Y1ilK8lXaX4lLxYWHGdsioWViYspa5-Dk9LvBRDpdesD756UlpYD4ONuTqrqHZ_xjKSa3JAqPnthjb4axxIVJoZw-AC8Wa2mqFXGyUMv5rNGF1IKq545w-IxTVq2-jtJQKE-jhXKpG-Nz8I6M8AA4xuCkGPixZwxNNlNp8nYv5V-KdntSDGPOgQTrEdEwmKYBH9KvLLWRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6eca2186e4.mp4?token=JNA1AX7cMKOjl2-rUhigv7-g2x5cIa_OWbkgYEWVMavG8KJ2cImyGxuAz6XQ4dkh-12U_I_hvfGPDaJXriuzCvy_DMN9mXljTkIkj9oZ3QeFRDunxdgzngYN5MgLM3fkJH3AvWstiH0-Y1ilK8lXaX4lLxYWHGdsioWViYspa5-Dk9LvBRDpdesD756UlpYD4ONuTqrqHZ_xjKSa3JAqPnthjb4axxIVJoZw-AC8Wa2mqFXGyUMv5rNGF1IKq545w-IxTVq2-jtJQKE-jhXKpG-Nz8I6M8AA4xuCkGPixZwxNNlNp8nYv5V-KdntSDGPOgQTrEdEwmKYBH9KvLLWRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: هیچ خیمه‌ای جز خیمه ولایت، خیمه امیرالمؤمنین نیست
🔹
من وظیفه دارم برای همه مردم ایران که با هر سلیقه و دین در سایه جمهوری اسلامی زندگی می‌کنند، نوکری کنم. @Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/445916" target="_blank">📅 23:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445915">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c046bb7d.mp4?token=r-lrs4kp88MDTibTJQ2q8d0Daki_nCZNf6a9SpeilYSzXDztKAGkIS1Ate5c_VDawZ0Noa25jPLphIt1ofMeTM1OhaXFnz86z_z7YDDtH9B0eaM1Yfp7OZ1uwoFOzEY5ebiRKLtwxLti3yiItCbVPpCw9BgPqPly9VFEjhfY1k2Z121c5O7_XEEIVtJ5HXZMO3GLChvCB0ZJMcwyJC2On66LC2JN5_ZAr4lVakV8se10ZDv6g9M7SQ8YWEduB-cVgf_eHNvLwm-ezUuBoZ42RT2ANqu4s2halxdk2V7K-zSw0HooFhEUVlV79gYVex4gmKTmoph1LPR1GRvJF4Y5Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c046bb7d.mp4?token=r-lrs4kp88MDTibTJQ2q8d0Daki_nCZNf6a9SpeilYSzXDztKAGkIS1Ate5c_VDawZ0Noa25jPLphIt1ofMeTM1OhaXFnz86z_z7YDDtH9B0eaM1Yfp7OZ1uwoFOzEY5ebiRKLtwxLti3yiItCbVPpCw9BgPqPly9VFEjhfY1k2Z121c5O7_XEEIVtJ5HXZMO3GLChvCB0ZJMcwyJC2On66LC2JN5_ZAr4lVakV8se10ZDv6g9M7SQ8YWEduB-cVgf_eHNvLwm-ezUuBoZ42RT2ANqu4s2halxdk2V7K-zSw0HooFhEUVlV79gYVex4gmKTmoph1LPR1GRvJF4Y5Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: کسانی هستند که نه در دیپلماسی به کشور کمک می‌کنند و نه در جنگ اما من ایستاده‌ام تا هم بجنگم و هم دیپلماسی را انجام دهم
🔹
بیشتر از این آزار ندهید و حرف‌های ترامپ را هم غرغره نکنید و اجازه دهید مردم آرامش داشته باشند و به جمهوری اسلامی افتخار کنند.…</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/445915" target="_blank">📅 23:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445914">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1f29024f8.mp4?token=ROSV7UBAdufspBKTZfmo0CPEHHlI55zGZV-lxBW62yN6m952dcEo5OnItRZqT_lBb6CN1kklgiA1Wg_JsfL4zp6kFcBGu6Sb0WxVNB0R0-SLNzw6FbYcfBDLt5_9pmmdTyBrXJttbwpCcS4gbPr6rbsxwiowoa4-yAS9b93-poLmu4eNbaq0wjH_znzGmXP5R7S6eZcBHgaMp9rj_8D-LX5wKG2DdQQ_J8FXluk_RiaJPLXroJhoqUBZKBftBo0q34F8LIEz8Mgb8E6NEUfHyKP3rlStB2rCmAnTOzHQCH-4FxRUlGj_xngCZto3mOKSmuG1sU77dJFCrDk537fXDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1f29024f8.mp4?token=ROSV7UBAdufspBKTZfmo0CPEHHlI55zGZV-lxBW62yN6m952dcEo5OnItRZqT_lBb6CN1kklgiA1Wg_JsfL4zp6kFcBGu6Sb0WxVNB0R0-SLNzw6FbYcfBDLt5_9pmmdTyBrXJttbwpCcS4gbPr6rbsxwiowoa4-yAS9b93-poLmu4eNbaq0wjH_znzGmXP5R7S6eZcBHgaMp9rj_8D-LX5wKG2DdQQ_J8FXluk_RiaJPLXroJhoqUBZKBftBo0q34F8LIEz8Mgb8E6NEUfHyKP3rlStB2rCmAnTOzHQCH-4FxRUlGj_xngCZto3mOKSmuG1sU77dJFCrDk537fXDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: ۶ میلیارد دلار ما در قطر بود و ۶ میلیارد دلار بعدی را آن‌ها تقبل کردند
🔹
می‌گویند چرا سوئیس رفتید؟ خب من رفتم آن‌جا اوفک را ونس امضا کرد تا پول‌ها آزاد شود‌. @Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/445914" target="_blank">📅 22:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445913">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
آستان قدس رضوی: در خصوص موضوع محل تدفین پیکر قائد شهید، آستان تمامی تمهیدات لازم را اندیشیده و پس از تصمیم‌گیری نهایی توسط بیت شریف ایشان، جزئیات آن به استحضار ملت عزیزمان خواهد رسید.‌
@Farsna</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/farsna/445913" target="_blank">📅 22:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445912">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12cfc8a569.mp4?token=I0i02cdwZTd4iNlK8lTRI5lxBbQbquyl_ulThgps6wUytLHjVdCbfpGvVZXOLB-pkbxs4FaLj1aiu17mKn7-aNdIlJIqhFWsNx0hbYRNuBc0X6vqEq-0BlpYZMjjui5B-faqNIOubJNyLbAOxayI4NZt55kLQF__Xj-bPIhissveUN5xeF5JjQgjKXYPa2Aod6Qhtgpyg-Wz0vDPNitIVSpYubnAmjGPjir-PONaq0wvedLC-ZU8OdGTeBPwjH-vQoUTvWm4CrlJ48fEXKxuf7Wlk5ITp2vOd_LBVAkLKjEqmxIYKH_RVWbNXztHei1AYGmMkttfqmxbKpM5Jii8Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12cfc8a569.mp4?token=I0i02cdwZTd4iNlK8lTRI5lxBbQbquyl_ulThgps6wUytLHjVdCbfpGvVZXOLB-pkbxs4FaLj1aiu17mKn7-aNdIlJIqhFWsNx0hbYRNuBc0X6vqEq-0BlpYZMjjui5B-faqNIOubJNyLbAOxayI4NZt55kLQF__Xj-bPIhissveUN5xeF5JjQgjKXYPa2Aod6Qhtgpyg-Wz0vDPNitIVSpYubnAmjGPjir-PONaq0wvedLC-ZU8OdGTeBPwjH-vQoUTvWm4CrlJ48fEXKxuf7Wlk5ITp2vOd_LBVAkLKjEqmxIYKH_RVWbNXztHei1AYGmMkttfqmxbKpM5Jii8Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مجری: رئیس‌جمهور آمریکا گفته پول‌های بلوکه‌شده صرفاً برای خرید غلات آمریکایی آزاد می‌شود. این چقدر صحت دارد؟
🔸
قالیباف: واقعاً هیچ. @Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/445912" target="_blank">📅 22:55 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445911">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f47669c456.mp4?token=VpaibmwPrb5K108to4oTZaCaWZJHwO3qo4G01bbHrTBb82iJXDhCNpcW1CwG0GbS3uPXsJOUJOpbwdW3U9abpAnXHZN0TVDUF3deMiE5X7zolr-gZMuz_f4iDstzg9dowS_FAaceXKevoYAPHpah4fW50WwshWwFaZws4yczfjGwi022EA_2Yi-3fYAI12Jokb2GUjXBraz_0vWvi8is2fwxXcrhhGduo9CJxiQe5jCZyNugpOgZr7EhcAflUqyNVu3rKm346xD35KKOxB24yIaBoOfhPEWQd5qMNiMBNBOcTrsJ3Jut0vQE_3U94rI3e6mrxzdwVjfMsCYe5x-Iaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f47669c456.mp4?token=VpaibmwPrb5K108to4oTZaCaWZJHwO3qo4G01bbHrTBb82iJXDhCNpcW1CwG0GbS3uPXsJOUJOpbwdW3U9abpAnXHZN0TVDUF3deMiE5X7zolr-gZMuz_f4iDstzg9dowS_FAaceXKevoYAPHpah4fW50WwshWwFaZws4yczfjGwi022EA_2Yi-3fYAI12Jokb2GUjXBraz_0vWvi8is2fwxXcrhhGduo9CJxiQe5jCZyNugpOgZr7EhcAflUqyNVu3rKm346xD35KKOxB24yIaBoOfhPEWQd5qMNiMBNBOcTrsJ3Jut0vQE_3U94rI3e6mrxzdwVjfMsCYe5x-Iaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عزاداری بروجردی‌ها برای رهبر شهید در شب ۱۲۳ حماسه مردمی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/445911" target="_blank">📅 22:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445910">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c07d1174f.mp4?token=mgMu2I-AoYJTIhcvHQEnh18oqpNx-BdwOWbZLruuqErqLQUVwjQjF_UTYyTx8mV6Uq5NRA_7UC58GzVW-6fVfX__1TuxAC95JsqjOrEf5wstOcUdC6oIbY6y8MLJIVd1m3tSqt6Gmi8PnpV1k3x1P8uv8F9BC33xakGQ72Lv2WJbQwS4u0E7iLEy-o4VAHn0dTajAIy14O0YKUlcJZPbDY07FfXA2itFtyikn7RrLoLB_RFRe_OD-dPE3DISg2iURYjO-DTFWU7cr5MCKTXEYLCiwV7uG5dbpWeWLWnfFr2Bhu8vTqm5ULiO34WnaoqGQOYqIIBT2OU-24UOODtDRQ_3QScfC1QMUL7n8wxnXETsDZOt9hdxOcECwS9Q81I6Hy2NEunlqS6Kvnx0msHHD4cubSf8H98Q0wnFabksGUVHYRYNnff3pFq27a9Ja8UDKGW0V9SApBumFI0UDqJjwZxTLWi7vUx9MD1bUgUP8zKwaumS9QSHJgGreZCJvy73SC9KgwX3dTbdtdfdBhb6iJk4ThtABqY2WX9z_IMellog21nZdpstF5ALdcRkrrTXkyyvQ4ar3ZZtPT88D7Zw-w8LU3x0Iio-sFJnghBmhswIQ9NVrJwjX-DTfMR39yCu52eSynL5NfnVH64RfV1hWyGoYoxLzh0-7XtvadLm0Hc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c07d1174f.mp4?token=mgMu2I-AoYJTIhcvHQEnh18oqpNx-BdwOWbZLruuqErqLQUVwjQjF_UTYyTx8mV6Uq5NRA_7UC58GzVW-6fVfX__1TuxAC95JsqjOrEf5wstOcUdC6oIbY6y8MLJIVd1m3tSqt6Gmi8PnpV1k3x1P8uv8F9BC33xakGQ72Lv2WJbQwS4u0E7iLEy-o4VAHn0dTajAIy14O0YKUlcJZPbDY07FfXA2itFtyikn7RrLoLB_RFRe_OD-dPE3DISg2iURYjO-DTFWU7cr5MCKTXEYLCiwV7uG5dbpWeWLWnfFr2Bhu8vTqm5ULiO34WnaoqGQOYqIIBT2OU-24UOODtDRQ_3QScfC1QMUL7n8wxnXETsDZOt9hdxOcECwS9Q81I6Hy2NEunlqS6Kvnx0msHHD4cubSf8H98Q0wnFabksGUVHYRYNnff3pFq27a9Ja8UDKGW0V9SApBumFI0UDqJjwZxTLWi7vUx9MD1bUgUP8zKwaumS9QSHJgGreZCJvy73SC9KgwX3dTbdtdfdBhb6iJk4ThtABqY2WX9z_IMellog21nZdpstF5ALdcRkrrTXkyyvQ4ar3ZZtPT88D7Zw-w8LU3x0Iio-sFJnghBmhswIQ9NVrJwjX-DTfMR39yCu52eSynL5NfnVH64RfV1hWyGoYoxLzh0-7XtvadLm0Hc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آخرین پیام از طرف مردم به آقای شهید ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/445910" target="_blank">📅 22:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445909">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🎥
نماهنگی به زبان کردی که اهالی کردستان عراق به رهبر شهید انقلاب تقدیم کردند
@Farsna</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/farsna/445909" target="_blank">📅 22:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445908">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">📷
بازگشت بازیکنان تیم ملی به کشور  عکس: محمدمهدی دهقانی @Farsna</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/farsna/445908" target="_blank">📅 22:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445907">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62044a23ee.mp4?token=gdOV9Iaq8uAg9vNJogJm8w2Nv_Q8irRyNNFNIvGeoi8OVwvt0o4TvB4NQHbaY0YhZ6s_M3hUIils-lXl4jlxWGgbSNVT3w8XMfh7FJpcZ-o8nNiw-aJmcRrWZsLgPXHhgnAazqoTFqMfgjE-bhE5blyyoZCQw2I9sptX6Wi5ngb0BLlZ0ng9kUCxT7A_dktbXZYwigkvFd4qo_-QtRIIWs-MO32_rfUedq5cULwCWY4p7rcwmF5ZNMe_6RmQQ-riEtydAnKewgKev4OdtePyRX5J04K6tlCrxiCZbfkUabx1gMs8PZx_vKESX-scwEKhu2G0JtndwxAlgwEemG1peg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62044a23ee.mp4?token=gdOV9Iaq8uAg9vNJogJm8w2Nv_Q8irRyNNFNIvGeoi8OVwvt0o4TvB4NQHbaY0YhZ6s_M3hUIils-lXl4jlxWGgbSNVT3w8XMfh7FJpcZ-o8nNiw-aJmcRrWZsLgPXHhgnAazqoTFqMfgjE-bhE5blyyoZCQw2I9sptX6Wi5ngb0BLlZ0ng9kUCxT7A_dktbXZYwigkvFd4qo_-QtRIIWs-MO32_rfUedq5cULwCWY4p7rcwmF5ZNMe_6RmQQ-riEtydAnKewgKev4OdtePyRX5J04K6tlCrxiCZbfkUabx1gMs8PZx_vKESX-scwEKhu2G0JtndwxAlgwEemG1peg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیر ستاد اسکان شهرداری تهران در برنامه پرچمدار: در تمام بوستان‌های تهران برای اسکان زائران مراسم تشییع رهبر شهید، امکانات مهیا می‌شود
🔹
هلال‌احمر قرار است در فضاهای باز شهر تهران مثل پارک‌ها، برای ۲ میلیون نفر چادر بزند.
@Farsna</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/farsna/445907" target="_blank">📅 22:30 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445906">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41f76872e4.mp4?token=Fnwgn3nYqddkcTw_17nQ6eQIxYiXAj1aftx9njUnVRqiFO-N2rCdicORlyor6dljNF4R5lO5E54mhngJShA6x02LT6xega_lk5GzDyArmAGXuHOMcf7DZjlYBll1JFwumYbDnwK9puwkimVbW8bCHWng7L7xm6z1WTvvzHLF8wg8qAVx9cpcmMMIhOWG2KwR4MGXh0vrt2Xep9efByIoCWTQT_o_E8C4UZj84yqPtES3Bk6sKcZLCqtSp7SyeFLillbO9TswmD3sLCPxd1dSgAD7rHzC7MWlBFHg4f2Dejx09N-aLYoFZ6LC5TF9700ZUIxVLblRCNCyqc685PyL2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41f76872e4.mp4?token=Fnwgn3nYqddkcTw_17nQ6eQIxYiXAj1aftx9njUnVRqiFO-N2rCdicORlyor6dljNF4R5lO5E54mhngJShA6x02LT6xega_lk5GzDyArmAGXuHOMcf7DZjlYBll1JFwumYbDnwK9puwkimVbW8bCHWng7L7xm6z1WTvvzHLF8wg8qAVx9cpcmMMIhOWG2KwR4MGXh0vrt2Xep9efByIoCWTQT_o_E8C4UZj84yqPtES3Bk6sKcZLCqtSp7SyeFLillbO9TswmD3sLCPxd1dSgAD7rHzC7MWlBFHg4f2Dejx09N-aLYoFZ6LC5TF9700ZUIxVLblRCNCyqc685PyL2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
توصیه‌های ضروری برای حضور سالمندان، کودکان، مادران باردار و بیماران خاص در مراسم تشییع رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/445906" target="_blank">📅 22:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445905">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee0709561f.mp4?token=h6CrIu8GITkuMFAv8jqbtmgL7eE5Er0dby_qu7ndGBnV9K7ox-xnT1fhFak-a_G_vAguukrlljGdQG5VlaGVf1PqlnX7RhWKYnJPOwE2FPKUwNGhD8mrEc358T3rR8UieENsZgZiqljOerJXrR84hGsfuAV2RTpnmYpw4EMZGTh3-oc4eAm9KvEQ9yIfJISxtsSjtfQlF6Q4419bDmkHmoVHBPm4IIcsdB6fXIIlHhlyK7F5BtUSAoihwPBDCyXDn-95qSz1yFlPYVCnAF8xymTZIVgDk27zUyidS-33WJSdnsNkF3hUWQ4loktjhaDNbOFpOGAlnjdvT1tPMfVAag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee0709561f.mp4?token=h6CrIu8GITkuMFAv8jqbtmgL7eE5Er0dby_qu7ndGBnV9K7ox-xnT1fhFak-a_G_vAguukrlljGdQG5VlaGVf1PqlnX7RhWKYnJPOwE2FPKUwNGhD8mrEc358T3rR8UieENsZgZiqljOerJXrR84hGsfuAV2RTpnmYpw4EMZGTh3-oc4eAm9KvEQ9yIfJISxtsSjtfQlF6Q4419bDmkHmoVHBPm4IIcsdB6fXIIlHhlyK7F5BtUSAoihwPBDCyXDn-95qSz1yFlPYVCnAF8xymTZIVgDk27zUyidS-33WJSdnsNkF3hUWQ4loktjhaDNbOFpOGAlnjdvT1tPMfVAag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ماجرای قطع مصاحبۀ قالیباف در شبکۀ خبر
🔹
مصاحبۀ محمدباقر قالیباف، رئیس مجلس شورای اسلامی، در گفت‌وگوی ویژۀ خبری صداوسیما پیش از پایان کامل سخنان او متوقف شد.
🔹
هم‌زمان، کانال رسمی آقای قالیباف نیز با انتشار پیامی از قطع شدن این گفت‌وگو خبر داد. این موضوع واکنش‌ها…</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/445905" target="_blank">📅 22:07 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445904">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🎥
خداحافظ ای مه‍ربان رهبرم
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/445904" target="_blank">📅 22:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445903">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5fd9f0fa9.mp4?token=FzCZPUZ5y2QofnPVTxxVRxIzWQ7w5znikGWb4jIyejlr5UaYKBNrAz5yjVB-C5FCzsjBMBHZmIdVrNgm2RhkWkU5OwWM0tfUXz3Rtk5vzG-a7ugXkyKjnPMKzUZ7fPwi8r-74TI_qLay2fz0BJUxA5Iel4b5SisZYsROnQa_P6Kt0KRLtaXx50adlIZpJeAJytNDDagefgWLPxq5Usd5R82zQjFpSlpQl3b_6V74PtSfpQHvnpWqWVgvb-94qDtsXT0pAE9h3oI-Y--3lYNJ0L0GcJo1tk66cbDIUWjNL1-cLuZPEMGavciO8u2PkoqmWaREDztZIYbvbNrXNoPkEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5fd9f0fa9.mp4?token=FzCZPUZ5y2QofnPVTxxVRxIzWQ7w5znikGWb4jIyejlr5UaYKBNrAz5yjVB-C5FCzsjBMBHZmIdVrNgm2RhkWkU5OwWM0tfUXz3Rtk5vzG-a7ugXkyKjnPMKzUZ7fPwi8r-74TI_qLay2fz0BJUxA5Iel4b5SisZYsROnQa_P6Kt0KRLtaXx50adlIZpJeAJytNDDagefgWLPxq5Usd5R82zQjFpSlpQl3b_6V74PtSfpQHvnpWqWVgvb-94qDtsXT0pAE9h3oI-Y--3lYNJ0L0GcJo1tk66cbDIUWjNL1-cLuZPEMGavciO8u2PkoqmWaREDztZIYbvbNrXNoPkEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رهبر شهید انقلاب: همهٔ شما فرزندان من هستید، به معنای واقعی کلمه دعایتان می‌کنم.
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/445903" target="_blank">📅 21:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445902">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2128c0af77.mp4?token=tuNQqWmlD3HHfWtLJrnD-ep4QAiDDIY3i0f6O-5I38bKfYPCIQ7rnkGk-plb-EbROo94fFuGsJlTwqIeI69bwrl07A_js8H4MB6lGoBdq1OP6_zHMRS0PKpSBs7lbqfWTserTNRXltWX2O1lb2L_zkhbsHhZkEwCcx0VEfA2nuYoBd6XGzVeWBImRc8MKBVhJ5aWs0WZ8Pll3Ku-t-3bjgIqFWTuEGq-ziFpuLYtL1ZTkIHoBZ2WaJU0M7cSzosloLk3_Yo-V_Z0E4tL8FAEGlVzElWlrOdNr2mg0xpU8yH_w87y5eoIfK1nNMmDlQehRNESWVdXpPv0tuYh2iQ1nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2128c0af77.mp4?token=tuNQqWmlD3HHfWtLJrnD-ep4QAiDDIY3i0f6O-5I38bKfYPCIQ7rnkGk-plb-EbROo94fFuGsJlTwqIeI69bwrl07A_js8H4MB6lGoBdq1OP6_zHMRS0PKpSBs7lbqfWTserTNRXltWX2O1lb2L_zkhbsHhZkEwCcx0VEfA2nuYoBd6XGzVeWBImRc8MKBVhJ5aWs0WZ8Pll3Ku-t-3bjgIqFWTuEGq-ziFpuLYtL1ZTkIHoBZ2WaJU0M7cSzosloLk3_Yo-V_Z0E4tL8FAEGlVzElWlrOdNr2mg0xpU8yH_w87y5eoIfK1nNMmDlQehRNESWVdXpPv0tuYh2iQ1nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ما همان ملت مبعوثیم که خیابان‌ها را عرصه رزمایش اراده‌ها کرده‌ایم
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/445902" target="_blank">📅 21:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445901">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">‌  پزشکیان: باور من نسبت به جایگاه رهبری مبتنی بر عقل و اعتقاد است
🔹
باور من نسبت به جایگاه رهبری صرفاً یک باور احساسی یا تعبدی نیست، بلکه مبتنی بر درک و اعتقاد علمی و عقلانی است. در طول سال‌هایی که در مسئولیت‌های مختلف حضور داشته‌ام، همواره از هدایت‌ها، حمایت‌ها…</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/445901" target="_blank">📅 21:47 · 10 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
