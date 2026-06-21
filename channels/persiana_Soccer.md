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
<img src="https://cdn4.telesco.pe/file/O1ufRcbpQuYmcEa_PWk8cWFAOxOdfa-dHNLw0QOpTEz4L00tD9Sy-ssiK_KdfWVQ5PzVQH8AUO8nM-umZ5h1Qdgrukb9a2Tb5gJnGMtZftCqRhnDQ4g8b1MeUJwI7OGuHnk4bM7dRPgcjZCxIQjo1PIQFuLj9fJxs7cYRFGzR_3iMW3Ng3oea7bPVYI24lzsKEeEJSNoUj5JZ3Lb4oHDMtJIr2ijSNp85Puu_nqL2lBQ3kUbSwHGK44UBDMH8SLiiku1oBFkXmnPNNiZq8zLeYZjF117xWQMiTmZ87YLTpG4FYjGj7ZjK3VpCfAsl0jTWtXt_-WJYeSJt2UlshduJA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 313K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-31 16:31:23</div>
<hr>

<div class="tg-post" id="msg-23989">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c577c16fe.mp4?token=u6GmKuv9O1Jx4Sy1eCA4QjiirLsFepKdgPtB-VIIg1C_WgVZjiCZgyA6inEHoMHFuZEBWmCvVYvmFrEIevpPVJ3MNJoLB1ZNnb-uQYnQxirnsKEYUYIgqJjzBlIqyQjqzyEybvki4Y6TazySDaoTcw_LpsfxFuiJeR60PhDLuSkmgdYIzLOGSCRGos2Q9oQV3hWXtKwmc6A-1yacho_gCO_EUG3AheXs13R5-f0i7a_Vl4YWa-wQJNK6_c7JGeSmIXRZLqBBvgFJWauBjJKWrgM46RWh22vNTwNlFVE_nmajIPpZQcQflogt2shR-lFnhpqOzX8hJ2_-K2YZb2l8XA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c577c16fe.mp4?token=u6GmKuv9O1Jx4Sy1eCA4QjiirLsFepKdgPtB-VIIg1C_WgVZjiCZgyA6inEHoMHFuZEBWmCvVYvmFrEIevpPVJ3MNJoLB1ZNnb-uQYnQxirnsKEYUYIgqJjzBlIqyQjqzyEybvki4Y6TazySDaoTcw_LpsfxFuiJeR60PhDLuSkmgdYIzLOGSCRGos2Q9oQV3hWXtKwmc6A-1yacho_gCO_EUG3AheXs13R5-f0i7a_Vl4YWa-wQJNK6_c7JGeSmIXRZLqBBvgFJWauBjJKWrgM46RWh22vNTwNlFVE_nmajIPpZQcQflogt2shR-lFnhpqOzX8hJ2_-K2YZb2l8XA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ساعت‌داوربازی پاراگوئه دزدیده شد!
در جریان یک مسابقه‌فوتبال درپاراگوئه یکی از بازیکنان، ساعت هوشمندداور راکه درگیرودار نیمه اول بر زمین افتاده بود، برداشت‌به‌مچ‌خود بست و  در نهایتاز زمین خارج شد.  بااین‌حال در نیمه دوم ساعت دوباره به مچ داور بازگشته بود، اما نحوه پس گرفتن آن مشخص نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/persiana_Soccer/23989" target="_blank">📅 16:23 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23988">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fpehE7gVD72gc_GC3TnrRPazBjYyavhVsQ6NaAZuXdq7yL3JY9nFwft0c6O938gnpWG65yZTF42TIFvUYFiqUFbU5Dzk8FFD_VScEvPVLsvuV8rWzaAL1YZ6fBRTA_oZz6j6-9I4D3DN5ncu0fk2KALSkj4hhhUNzYoZc3enVvR8OPOFcH_IKJ6vSF6BFKfexC5hk_0Zs5RFnfKJDwBL5au1D1lQYNHawa2EwVCR49KieElvHLF2YIFZkQPFe4w95n90qoYfoeWVdV37BdOXwndhHJOKcO7MNHgKifsbUDMxdk3muwG_Y5gMKJJb1VOMwvotOVvM99-ggEisCtVQmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
🇫🇷
خوزه فلیکس دیاز: بعداز توافق شخصی فلورنتینو پرز با انزو فرناندز؛ کاماوینگا و شوامنی دو گزینه پرز برای جدایی‌از رئال مادریده. شانس جدایی کاماوینگا بیشتراز شوامنی است. درباره فده والورده پرز گفته او فروشی نیس بهش هم فکر کنید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/persiana_Soccer/23988" target="_blank">📅 16:17 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23987">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pHfgW_7S7cAroy5oqrgpB9wK2-pyPSNYjE2b7Ddi7Ae3mxQS98qql-ouByEMdUEKrpKEPaneMYR3lxuQMKoQlDp6wrpQRyaZGE2VECQj4P30euOFuv3mdyKQ79wFzXDKYiI4QMZ0Wo8T31tNszTjQ82KkNshZY_3eV0wSByuErD5ADKeX0A34sr3EVJTU1VCc0YY9SlHUAk4nym1JQ_Q9H_kunzgCVdoXV3_EBXoodUDDQRQ4V4CJVFUMVcvM9zx46tZbMmePQ9egsG1G-2xI7Hl0TuLzvKuvbVsU_HI_1vj9IZvckpy-CWekIZXGRm2_GSCgu68dIgB45hSmlF6VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مصاحبه‌قدیمی کوکوریا در سال 2019: حاضرم موهام رو که علاقه زیادی بهشون دارم از ته بزنم ولی هیچوقت تحت هیچ شرایطی به رئال مادرید نروم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/23987" target="_blank">📅 15:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23986">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8dba54f8d.mp4?token=Uzr3IrTfID43fkLZHxFKxLuo3lE1NGwIlqFFAHee6wK48wF07XvHISPen_pPd0A_2jr6NAL2NG_goR-rt4ioMK0KW2fkzEMmKmdxR50Ix9dvv9uQF1YepQnGr62LfmOEGZE35DN9oR1dS4IrvzzyKJxAxFavwt1pIVt0gMcaqfY04I7vwT6ssMjjWmmOwqdC05KJBVcVSNqMzMzdtTTtbY2zs4wONP_QoK62u3Xain2tvqQFx_CseA4YUsuIiy3PZKqkGcIO4j04JVAl1Ywsc4zTGARx8UT6SGTPYnzF9e-bgsA-LFSNnKGehp87319-_pTRSd4E0GZGwe_fvZKyMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8dba54f8d.mp4?token=Uzr3IrTfID43fkLZHxFKxLuo3lE1NGwIlqFFAHee6wK48wF07XvHISPen_pPd0A_2jr6NAL2NG_goR-rt4ioMK0KW2fkzEMmKmdxR50Ix9dvv9uQF1YepQnGr62LfmOEGZE35DN9oR1dS4IrvzzyKJxAxFavwt1pIVt0gMcaqfY04I7vwT6ssMjjWmmOwqdC05KJBVcVSNqMzMzdtTTtbY2zs4wONP_QoK62u3Xain2tvqQFx_CseA4YUsuIiy3PZKqkGcIO4j04JVAl1Ywsc4zTGARx8UT6SGTPYnzF9e-bgsA-LFSNnKGehp87319-_pTRSd4E0GZGwe_fvZKyMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
سرهنگ علیفر: از اونجااصلا نمیشه گل‌زد؛ واکنش صادقانه آیاسه یوئدا بازیکن ژاپن به علیفر
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/persiana_Soccer/23986" target="_blank">📅 15:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23985">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bTgrSJhrsfsY2NnarsaBA9ia_2WS-3avXB0A8zlcNNux-l6bHdOosMcrE7kzFYU4u7jCCRGwqNd5KJ3Lj93togFdCw9Jm56dSQfHY_vWDcggue0L7ONk33dgMZXenN-0tQ4roKOccxMendd8CJYg-eA8WhXuYuO7qdqGxfJtjXDgZ74rDsFoyHtNaV6MirN868qaokypyaW4JHDvEx13HsyBZr637rsLyj0nYKzYjDV0knATImodGN074PSQipYB-3K3rc1KUKc5NB1GW7Tw9tTjD1cmdZqGeM_UhTEL9FlKnz1U5i2nPg_XMlyjPp39qqZuPk5utlSlBS7ChAjfbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته دوم جام جهانی 2026؛ آتش بازی سامورائی ها مقابل شاگردان هروه رنار + جدول رده بندی گروه F در پایان هفته دوم رقابت‌ها
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/persiana_Soccer/23985" target="_blank">📅 15:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23984">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4e6bc8b00.mp4?token=WKmhXB1u7QkBZQLBlmQb737RCuIVMWs4NwEhFWYOfQZ35VbHUYXnhKpkeol7NRJjARh-oXAQpu34KWCfGjIwUtjtPNI3uKmaCJ8wxeDd1W-2cnIjZtOPp0jWxCg-3DLAnYxozfhYVrU3wJ6a4iToaUcEO7Z-FOBkD9gkD2PD7p9aPDc0UnzlBcrQIrShlb4BwQh7jt4qNnP928uYkqY6HNQ7h1OluAiGmqoag20_AW3qwOj1b1OM3jja9AbbWbMpoBGh3GWkgM5cXB58qzvpEQo9otVl0KEtlltOB1naQYYSRQXGi3ITJr1A1x5m4Ks-OryWGph7gOdZmh9HAp_Y8Y5ecCaHNQB8dsGVHSppgFznjxJYeKZDeX_xnutWVrGFzuBgyiiVkfdQvi4X3Uoqyj7bcCCmOmsbYmo3sfQXaT5P6vNBKfw15XokzGv-z_tsfNr1O2-KrCZVgiWG6WUhdvsdZlZutk8N6j2b_eDfGVtQjqAD-MYvYGeUixFViEHN6wRdGuTYVgb8w5wlYz21FJ95VvwfMom0JfkxeT8MWTvAQAOPOQMgSSLyvzUhniA91Z_dDXFsWZQqHztGtqfAwBufISrEMBOg35SI_CITHpJOPwNSZddTxa1blNDPZA8Ocaylz0ZMM6GQ_KyZTXPexAePf4_CmSbLir3A2l3a4_E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4e6bc8b00.mp4?token=WKmhXB1u7QkBZQLBlmQb737RCuIVMWs4NwEhFWYOfQZ35VbHUYXnhKpkeol7NRJjARh-oXAQpu34KWCfGjIwUtjtPNI3uKmaCJ8wxeDd1W-2cnIjZtOPp0jWxCg-3DLAnYxozfhYVrU3wJ6a4iToaUcEO7Z-FOBkD9gkD2PD7p9aPDc0UnzlBcrQIrShlb4BwQh7jt4qNnP928uYkqY6HNQ7h1OluAiGmqoag20_AW3qwOj1b1OM3jja9AbbWbMpoBGh3GWkgM5cXB58qzvpEQo9otVl0KEtlltOB1naQYYSRQXGi3ITJr1A1x5m4Ks-OryWGph7gOdZmh9HAp_Y8Y5ecCaHNQB8dsGVHSppgFznjxJYeKZDeX_xnutWVrGFzuBgyiiVkfdQvi4X3Uoqyj7bcCCmOmsbYmo3sfQXaT5P6vNBKfw15XokzGv-z_tsfNr1O2-KrCZVgiWG6WUhdvsdZlZutk8N6j2b_eDfGVtQjqAD-MYvYGeUixFViEHN6wRdGuTYVgb8w5wlYz21FJ95VvwfMom0JfkxeT8MWTvAQAOPOQMgSSLyvzUhniA91Z_dDXFsWZQqHztGtqfAwBufISrEMBOg35SI_CITHpJOPwNSZddTxa1blNDPZA8Ocaylz0ZMM6GQ_KyZTXPexAePf4_CmSbLir3A2l3a4_E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرمصدوم‌شدن‌کورتوا کذب‌محضه‌اسکای اسپورت همچین‌خبری روکارنکرده ولی باتوجه به فعالیت‌های دعانویس ژنرال‌ممکنه‌یک‌ساعت دیگه خبر بیا کورتوا و دیبروینه سر صبحونه کینه های قدیمی رو دوباره کشیدن وسط و سر دختر دعواشون شد و گارسیا به دلیل‌مسائل اخلاقی‌اونارو ازبازی‌کنار گذاشت. ویدیو بازکنید متوجه منظورمون از کینه قدیمی میشید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/persiana_Soccer/23984" target="_blank">📅 15:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23983">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc33af7706.mp4?token=Vgi8G-EzbqhA43rBiPpcQmMAdzvS25Dymi5vEz7qnaLYxPIzeW242lhcRkmMmbIqfv6Xl3uqb2tB5uCwrT7II01IGa4UNrZyAsqCtNYqVsxGEbU6MN6HwJ3AfyV5Nik-darAmzqOyameVUN1_0wfvDMHKWCVIvd5OzgBu0lbYiXz_4UUyn7LMrxO2R5775Fzj_oCy3pBu9Yvdsc5X32NgWZEj0dILhd9NKO4GVCv86lJUIW5sUdq-q97KVCQ0R6SObH6jOtawiuHvVJO_e_jmUkrIALm7s2ytdaLsGFaufSzfFpU-Emu6PD8GytgmTt9QdXdzwcOiWhYYy0F_xYWgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc33af7706.mp4?token=Vgi8G-EzbqhA43rBiPpcQmMAdzvS25Dymi5vEz7qnaLYxPIzeW242lhcRkmMmbIqfv6Xl3uqb2tB5uCwrT7II01IGa4UNrZyAsqCtNYqVsxGEbU6MN6HwJ3AfyV5Nik-darAmzqOyameVUN1_0wfvDMHKWCVIvd5OzgBu0lbYiXz_4UUyn7LMrxO2R5775Fzj_oCy3pBu9Yvdsc5X32NgWZEj0dILhd9NKO4GVCv86lJUIW5sUdq-q97KVCQ0R6SObH6jOtawiuHvVJO_e_jmUkrIALm7s2ytdaLsGFaufSzfFpU-Emu6PD8GytgmTt9QdXdzwcOiWhYYy0F_xYWgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
#نقل‌انتقالات|اسماعیل‌ سایبری هافبک تهاجمی جوان مراکش‌باعقدقراردادی 5 ساله به بایرن مونیخ پیوست. هزینه انتقال 55 میلیون یورو اعلام شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/persiana_Soccer/23983" target="_blank">📅 15:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23982">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0eba240be.mp4?token=RzIk7bmcBUP_ZGbJEjrLrW1p-TOEp_zoXtMIBekqikabo_uPod4aVh9qvwZsOsVlEdVkCM3teCgnjxxIjfxJlI0NYU-5baGDb7XPXYGliWh7pS3SzmNaBuTZQp-_ydxBqXBROpJMmWvlUPmPIk75uPkUDYWEoWPWJFZ_gNlwbs3D-VqnnNmq_fDU46hTVheOGyUccQ1C4k53qa8-GBjXLrLk8wXqrQ1cQ2RNGzgJs2UEhWbQfF6z83yI8RuPg-bFfZiQZ3NPhNwAWQ3fyk6kzYrLkkszr66Decnu_oeWFjX4xAYk9Ko9T6WSssH3eNKl9-X0f0LRxuALg7nPsM0kqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0eba240be.mp4?token=RzIk7bmcBUP_ZGbJEjrLrW1p-TOEp_zoXtMIBekqikabo_uPod4aVh9qvwZsOsVlEdVkCM3teCgnjxxIjfxJlI0NYU-5baGDb7XPXYGliWh7pS3SzmNaBuTZQp-_ydxBqXBROpJMmWvlUPmPIk75uPkUDYWEoWPWJFZ_gNlwbs3D-VqnnNmq_fDU46hTVheOGyUccQ1C4k53qa8-GBjXLrLk8wXqrQ1cQ2RNGzgJs2UEhWbQfF6z83yI8RuPg-bFfZiQZ3NPhNwAWQ3fyk6kzYrLkkszr66Decnu_oeWFjX4xAYk9Ko9T6WSssH3eNKl9-X0f0LRxuALg7nPsM0kqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
50 ثانیه از دیوانه کردن خداداد عزیزی توسط جواد خیابانی در ویژه‌برنامه‌روزای‌اخیر جام جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/persiana_Soccer/23982" target="_blank">📅 14:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23981">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sFvRA2Wcb2NNkrOhMoFHR664ongzcI7kIZ-pawYut_U1PIxgvILtxbsQbNdu2JaiDoHzdLv5ej5eqOistFC50QwyDS7cwk_uBobiLAf77lKxygIXlW4FlHG5qsByW3GI5iqdFsq_hKUaeO4AQvyP0fPcqNFBvyJBv-9nqL7tDGJP5aMGnhueIc8kGjSZZx7JOZVoBpK5lIkzJlKZAUMqPfMISPql7hHuluP_UbA0sZNXvstHy8VBTHbj07pIwgKTlX39qmZsSHmVegT1rrOxvBZ6CFEOJZZyf_0Vl0-Hal-pfHYxKPnfukcujIdIlLm4aFfxW63cZtAl0MmRAlHNdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛سهراب‌ بختیاری‌زاده سرمربی جدید استقلال امروز صبح باحضور در ساختمان این باشگاه قراردادش رو با آبی پوشان پایتخت به مدت دو فصل امضاکرد. بختیاری‌زاده‌درباره تقویت کادرفنی و جذب بازیکنان مدنظر نیز گفتگویی مفصل با تاجرنیا داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/persiana_Soccer/23981" target="_blank">📅 14:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23980">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vUWVD0MIVFt0ZoLkLUEsS0K55xTg7TGBqCr4xF2LgoNAJx6prMfC0gKTXRvduJu7G4yGMk6CblZXWwbJflDX8K773ng_e3UFudivckK0J50D5VxpMSyU-YffGuXTsJYTIeqPZEvYsq_fhMi_iYJSl0NEk1wZ0yntbWWZmjizszbRwgQqfySTiyjwpzQotLmYbd9WrCKBo3Hs8O-nvh333msV9CZ49hmBnbz07OHkqw6gBU5eAZ8-3CJmDaNbw4U18T-qX5zgPmcPcoev0vonelMNNduWfGMEu_VqNm_mZzuLgmf2qpgya_pjdHwq7pZpXbRsktXYzfU68Z-uSJyqfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ تاجرنیا امروز صبح در تماس با سهراب بختیاری زاده سرمربی جدید استقلال گفته درصورت موافقت او سریعا با گابریل پین قرارداد امضا خواهد کرد. بختیاری‌زاده علاقمند به مربیان ترکیه‌ای است و احتمال داره دستیار دومش هم اهل این کشور باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/persiana_Soccer/23980" target="_blank">📅 14:13 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23979">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nESqrOxQS1v58VqVpcF9gZIDGu5jGzHSjisDBvXHFGnQV8IjSpGzEEMuTIa6xbG3ghR_M5Ol1peNq4YzJX6W9qwdnqP9rGUT9ayxc9JhCtFQDbtXwo5eylvo3WCmJsW7_M54f_CD0J2bWzZBC8XPLWbcPQrn_Dsjc0B3ry56UOL2vSdZyvWr9zqBLejvtW4NLQoIo6ecR08oEKG_vVs1o3SS8ho8njttlAGsxbnfLVLkASYRXEimOTNTzm9y-Vnwk46p3I9qOX8uxBgd0RKgWd04KQuaplxLEN7FaDSMdLoPogWNOOGVG7AO3GNEcyNYiiWOrJCKJyfr94122A-4vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
#تکمیلی؛ باتوجه‌به‌تعدادسوالات زیادی که درباره آخرین وضعیت نیمکت‌پرسپولیس پرسیدین لازمه در این باره به یه جمع بندی برسیم؛ امروز پرسپولیس با اسکوچیچ مذاکرات نهایی روانجام‌میده اگه به توافق کامل‌برسند بر سرجزئیات قرارداد امضا میشه اگه به توافق نرسند اوسمار…</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/persiana_Soccer/23979" target="_blank">📅 14:08 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23978">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9df1a6812.mp4?token=hubq86CscdPLOig7FcAjDTsiStumoBdY2TCxrUiD5HSnXnenoxGfsyuNGsksnJuqkyExeGISSSoPwXrEVGhdFqyjALY0r_jIJ_OpfMgBraWQTtIrMnhP6g2FSGGwzGd-LyWxdYL1GiuaYqT_zLVTjfyMxenRHMPHqM-1eFoxv10Tl_uOUIy8S_YRxM2uzLvI3pCZCQaH3tGDDXBIKzW7x4g71AnjJxbwcQ2G8SbCK78iy7eQQb11ibm7gKCg3gpYWWXJkdpMt5XsNNZofONv_SkLcjXNNTwK0OlC3gKBjfMVu0tv6M5wHzGNIvFqxNRAnkpNleDXTXM8cMrBvtmb8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9df1a6812.mp4?token=hubq86CscdPLOig7FcAjDTsiStumoBdY2TCxrUiD5HSnXnenoxGfsyuNGsksnJuqkyExeGISSSoPwXrEVGhdFqyjALY0r_jIJ_OpfMgBraWQTtIrMnhP6g2FSGGwzGd-LyWxdYL1GiuaYqT_zLVTjfyMxenRHMPHqM-1eFoxv10Tl_uOUIy8S_YRxM2uzLvI3pCZCQaH3tGDDXBIKzW7x4g71AnjJxbwcQ2G8SbCK78iy7eQQb11ibm7gKCg3gpYWWXJkdpMt5XsNNZofONv_SkLcjXNNTwK0OlC3gKBjfMVu0tv6M5wHzGNIvFqxNRAnkpNleDXTXM8cMrBvtmb8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇵
هاجیمه موریاسو سرمربی تیم ملی ژاپن با دیدن هری کین کاپیتان تیم ملی انگلیس فورا تبدیل به یکی از هواداراش میشه و باهاش سلفی میگیره:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/persiana_Soccer/23978" target="_blank">📅 13:49 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23977">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nv7peAJ0HMOrWAZjVfKn9m_7EasSoZf3YbttEWgZhLSSNQRyf1R6gQ-e1QnsTQ5JRanvp0O2w4RFgC_CUdlF7ixe2OZuZWOROreBPfGkjlncCHAHNh-hae4st1Gfsa8wY-m7z_8UYL4dFQPqfqRASu71jPle1JChiLoUqDjXIPvVWYhUv8KH2ZiGDzuvHqr6QqJMQdNDfETdPBFwHmzXgkP8-9JGjASU26WWPTae9vogo-zMvBgNty4n1OiSlQDcirHbXn0GYGEzOzkbb_m1AvKxIfSVWfi0Fv2k-CJOWAYeuwS2MX4CjFZis2qqQVCDvZch3loexSIHNXyk3qEWEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیانیه‌رسمی‌تیم‌ملی‌بلژیک: آقای قلعه نویی عزیز دعانویست‌رو از تیم بکش‌بیرون‌. ما اصلا با شما بازی نمیکنیم سه امتیاز بازی‌برای‌شما. تک تک بازیکنانمون رو به دلیل مصدومیت داریم از دست میدیم.
⚪️
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/persiana_Soccer/23977" target="_blank">📅 13:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23976">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CGr2AO-3puRbQ-APZ6wZ4wT29u6WZQ_E88a-c4oVkTswasnV920zWKZsrM_9us6XJLv0YZ_z6uK5vZowQRjjbgnKnEAnc2TqxT-nHf3FY1SkQk58dSm4WcTi9MIi0dnmV87BVusNV6peoWGJiVXzYBsOFxzFg42h9qfUt55kU5hplIOmLCILETmvjPlwn8ODB5s_PhVK_KZ3NeEZeRx3LNaxWO9mrEZLUCPLULf-fG9lrO3wKzMu3D0R9IeMwHo1NMMM5RYqq-KbvxWTkcRThdKgFesYN65aRXS3uzkcCTg5rHiPUtt3DKRFgER7woYZiDCME4kTXVWbt-8jzZ9RKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فوری؛ مگه‌میشه؟! رسانه‌معتبر اسپورت بلژیک گفته لئاندرو ترسارد ازناحیه‌کتف‌احساس دردمیکنه و ممکنه دربازی‌امشب‌مقابل ایران فیکس به میدان نره. پزشکان بلژیک در تلاشن او رو به این بازی برسونند. تروسارد جانشین جرمی دوکو مصدوم شده بود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/persiana_Soccer/23976" target="_blank">📅 13:26 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23975">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tizu5hK7fOUkzjLexAFvcH7vrkcDXhFm3Y-H7uC7wX1DtIZ98wgcNmbwd9khxEPWGqMBaIm4McqCbOpy0ThuG-mvy_q8MgpZ1I8YQ_RSlXiHy_2uYSv6usSoVrLh5QxPVnKJOXb9QLYaK9p-KMIhrBHqAfc_Mp37HXmgeaRa5E-5XowI8gAkFrUdT5YUqelIVr7CCoV72H_ju2Ec-cw9D7AkBxVkSn88Akk6loKi1OikTbK-ywpG0auEzAe7MfQ57JZByoll8MVvuHNXEXKrEfmJC5pieiEONe2TNG0y5x4kE5ZgGUgBQiz-tnqUAg-yePR1w8CcJzcDkNWg-meHNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌شنیده‌های‌پرشیاناازباشگاه پرسپولیس؛ امروز ساعت 14:00 جلسه نهایی مدیر عامل باشگاه پرسپولیس بادراگان‌اسکوچیچ و نماینده‌اش در ترکیه برگزار خواهد شد. باتوجه به مذاکرات مثبت روزهای اخیر انتظار میرود امروز قرارداد رسمی بین طرفین امضا شود و اسکوچیچ بزودی راهی…</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/persiana_Soccer/23975" target="_blank">📅 13:18 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23974">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ewTvkyYmzCR4IC7XnczFBIfLiuUbO4DM5zPHfHLyvgRWM9aUpdVaDdxiHcDEaBJbrbnXyh49iZuWYxIJqYGJAog15a-6eaX1ky1Akr-SdPPbjdlMhWYK0Hc9ojG42Xnhyr_uD4cOCzBbapMUfXmKhp_FPuMqmD8ugZwfNjbYFQLVH5ZyhhG8ftb4s68VOj3Md0KuXN-NOv-VCw8TqD_rfY-TPQua4MYIL8zm08vic2l5BicwPfONhcZXiyPZUXEQserBoiOjFZPoamDGFCk41Y_mSjixDRSAsIWobFVE4QvtXt8R-cNryFr1vBWnw24o9J3TopAf0dzTRZ5qMFvdqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبراختصاصی‌پرشیانا؛ با اعلام فدراسیون فوتبال رقابت‌های‌فصل‌اینده‌لیگ‌برتر 18 تیمی خواهد بود. هیچ تیمی سقوط نخواهد کرد و دو تیم از لیگ ازادگان نیز به رقابت های لیگ برتر خواهند آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/persiana_Soccer/23974" target="_blank">📅 13:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23973">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/415bb37d05.mp4?token=hFo1IwE13kN1tGzLyBe5srGKWiY0756LOBiM3tyUFnbsCJkPCvL3k769H8oAYnSistg7SQlHgSuwOFh2wDMdk-s_d15YszSCIJQ2DBbEtMAUa4kdQWacGMIWt50FbljgSMtVsryTXsmIZDW8v8sS_IpLjOcX468WfX_SXsXWAJ7aSk43YX4o9coRI_6svTf9w5qfGyrg5ijOZyj0s5iNOXeeZHnKDjG94uSG34uomOtpb0lAkkCQ8kJexq4pF3sP6WdeXThJv910hMJEPzvFkpG3GJjIfOCT4GfAwfQln15phnneD0rCllrs0urXrv2_NoEBoL6ccKUvISsZww9QJ12BQf1a_iLBXPgb5ezRw3lN2JjFvjvZ974oinihD5uIbSSYnl2z4NQE5r_f5RrRwQJaomZlc6nhEpsJmqGWk14EiZubbM2vkysCbQ4p7m-XETAhyBtni7WzzPSleQuHgVOmDnT5YgTubEeX3h1yX2lUS46b48Z4vZs_CTaY_OiMFv8Tno7XzkKryQGnGTC0Rzr5YYghQV6kyEV8UC1C-HY586xMrnT5MHWYpJVWMHcGjiDxMZ6jBVor1heXrKH6QO5BnjVxoaN9ucpk5tzLL1dKkjc9MkQaRc7EdadFXeN5all7u4yqozmGx_rCra9H88qNbsVfIm7PeRTEf_7Tn7I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/415bb37d05.mp4?token=hFo1IwE13kN1tGzLyBe5srGKWiY0756LOBiM3tyUFnbsCJkPCvL3k769H8oAYnSistg7SQlHgSuwOFh2wDMdk-s_d15YszSCIJQ2DBbEtMAUa4kdQWacGMIWt50FbljgSMtVsryTXsmIZDW8v8sS_IpLjOcX468WfX_SXsXWAJ7aSk43YX4o9coRI_6svTf9w5qfGyrg5ijOZyj0s5iNOXeeZHnKDjG94uSG34uomOtpb0lAkkCQ8kJexq4pF3sP6WdeXThJv910hMJEPzvFkpG3GJjIfOCT4GfAwfQln15phnneD0rCllrs0urXrv2_NoEBoL6ccKUvISsZww9QJ12BQf1a_iLBXPgb5ezRw3lN2JjFvjvZ974oinihD5uIbSSYnl2z4NQE5r_f5RrRwQJaomZlc6nhEpsJmqGWk14EiZubbM2vkysCbQ4p7m-XETAhyBtni7WzzPSleQuHgVOmDnT5YgTubEeX3h1yX2lUS46b48Z4vZs_CTaY_OiMFv8Tno7XzkKryQGnGTC0Rzr5YYghQV6kyEV8UC1C-HY586xMrnT5MHWYpJVWMHcGjiDxMZ6jBVor1heXrKH6QO5BnjVxoaN9ucpk5tzLL1dKkjc9MkQaRc7EdadFXeN5all7u4yqozmGx_rCra9H88qNbsVfIm7PeRTEf_7Tn7I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ماجرای جالب آشنا شدن اوسمار ویرا سرمربی فعلی سرخ‌ها باسنگربان برزیل‌ و لیورپول؛
پسربچه هفت‌ساله‌وتپلی‌که حالا یکی از بهترین‌های دنیا شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/23973" target="_blank">📅 12:49 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23972">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K7jyC_pD0_5UxMdzhboveOHCTQ6bHz88cZZKTykacK3pSvJAdOF83TW9VXs2c0HZ8sChI4myWc-bCjE0Ucc_psgz9_AOZpN4zLBm5ttvxb0lPvb1dDQlJhtarNXS9iqxrkM3IS3bXXyTHGNIUhVCU7ympYMljOvGp7ZJQqNmrdswWRjaPn07FdtYdRycC8oQsrH8ad-NIFwaxZ-wsHBGvjmYwpJJh89APqyoBX1gml7NCNjR90giXvprt7JbSPjvDXb_3R1vCffXWFC8_YTICWC8yPP05EGYEJhXss-gYS-IApzCl187N33wiQSVyW55h-hIfQiB-qCqicIcIMu8jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
رکوردداران‌کمترین‌درصد مالکیت توپ در یک بازی جام جهانی؛
پاراگوئه با مالکیت ۲۱ درصدی در بازی با ترکیه، در رده هفتم کمترین میزان مالکیت توپ در یک بازی جام جهانی قرار گرفت.
‼️
ایران با ۳ بازی، تنها تیمیه که بیش از یک بار در جدول کمترین میزان مالکیت توپ قرار گرفته است.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/persiana_Soccer/23972" target="_blank">📅 12:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23971">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FUGtzVryx4iouyPcZ3EJB3Ao9Pa9sHuHmqgoPEwJgQUl_lpFLPIC-YavFjqsc5Aj80Nw1YXQqQPVEMfd7GMsR7BWC92co16JJvZCsqVh-drR00zhBSwnnCPz7kRP4r0RIZVNjufz981PvulDgHyGwtFBaIQ396M_RUy7-DtNYa-bn90-25AVS2ubiEoC9XQTKOhQfUPsxM_g8AQqLSYMu-Zf5v5hVkkzyF8Z1hQunAGJTkvirMn_fAPGSxMDYWb33zP4vjfy0cGvcHzg_dU7xW65kAJOT5wdpc67lP_RAwSMbjS3mKkBHNCUNyJGH6qdc-NlLjK3-RvoKveX0ZmMdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
فوق‌ستاره‌های‌فوتبال‌جهان بابیشترین تعداد فالور در اینستاگرام؛ کریس رونالدو با اختلاف در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/persiana_Soccer/23971" target="_blank">📅 12:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23970">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VeT4YsER5bO8QSmv34H6xcMRREY-mHpCg_o6xAE51jt5YdQNGHuVkwXt2F9GkWciN0dm4_zNQOcSIhHCMVzpZeCfXggJPwid7v8AVd_7dYlzQWBH3moIn_rfayn35f7G92TJ5bYO9wCjFlL6jHyTSSEXl-KeKMG0MUzM7bUobE3fDArzmitU9qiXbp5JPzk5MRmEFVOIOGHhb6HE9ev5-zHeXUBSLhHjLe1gP61Ew1zY7aJ6FvjRvvYsXOwB5spn9JOfcufvySBivc0dwR-tqtdX2xTxO2Gshrtonc9dKRccIyOw32nPUgPI3jLaUKfV0642vB5joFwrXBLAzRHBtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ به احتمال زیاد دراگان اسکوچیچ کروات روز دوشنبه یا سه‌شنبه همین هفته وارد تهران خواهدشد تاکارهای‌معارفه‌اش بعنوان سرمربی جدید باشگاه پرسپولیس در هتل اسپیناس انجام شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/23970" target="_blank">📅 12:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23969">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d78439566.mp4?token=QZXQ8MT1vGI67Vu-oURG8budwg70bNTKotnevE-ww0TcKYuNJf77YI3ZYFWB2Tvi1b-gyYljUVlvr3D659Gg7orlf-RHGDbOy-M1IJf1P9u2W8Lmk8V1IBS6-qMcZ_KCGtnvqEIS9P3p5QFzAZsCAzdrh6T0G3-KgmTefT4t1KjNEFABlVXbLj6Huq8tvnobLlrWtMQK7mLcED6dp3HHC5QGdEs_RV8_jteDQsqFCq7TcTh8udDNinGt3vaBvFRCBVzogpQrr11l9JgoRramAX8NNJYe-pDY1vgcF_F8Fc68F9c8AIozw5reW8yuDn7SoD_ddQDwqi3ggfYh5biZnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d78439566.mp4?token=QZXQ8MT1vGI67Vu-oURG8budwg70bNTKotnevE-ww0TcKYuNJf77YI3ZYFWB2Tvi1b-gyYljUVlvr3D659Gg7orlf-RHGDbOy-M1IJf1P9u2W8Lmk8V1IBS6-qMcZ_KCGtnvqEIS9P3p5QFzAZsCAzdrh6T0G3-KgmTefT4t1KjNEFABlVXbLj6Huq8tvnobLlrWtMQK7mLcED6dp3HHC5QGdEs_RV8_jteDQsqFCq7TcTh8udDNinGt3vaBvFRCBVzogpQrr11l9JgoRramAX8NNJYe-pDY1vgcF_F8Fc68F9c8AIozw5reW8yuDn7SoD_ddQDwqi3ggfYh5biZnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇧🇪
بااعلام‌‌رسانه‌های‌بلژیکی‌؛روملو لوکاکو دیگر ستاره خط حمله تیم ملی بلژیک به دلیل مصدومیت جزئی در بازی‌ امشب‌مقابل تیم ایران فیکس نخواهد بود و احتمالا این مسابقه رو از دست خواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/23969" target="_blank">📅 11:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23968">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">‼️
رکوردجهان توسط یک مرد اهل جزیره کوچک کم جمعیت‌در دریای‌کارائیب‌شکسته شد
؛ الوی روم دروازه بان 37 ساله کوراسائو در بازی دیشب مقابل اکوادور موفق‌به‌ثبت 15 سیو شد و رکورد بیشترین سیو در 90 دقیقه‌یک بازی جام جهانی رو شکست!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/persiana_Soccer/23968" target="_blank">📅 11:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23967">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21c204841a.mp4?token=PE23OgfBoAsgaZMbAUGt0LGc0srK1fGxiyta8s5BNC0UGzjdw3VtRrGWosYKkNeqiQPGAjI-6k30CUyr9LhQqK_pm1vUjFIZ6yL3IUAoRlxFJGVV5CpdNLJxYqwcl8YDCwFz3JeI-wIQk0ogOfLMaJlXYNqxuZPmk0mD2m8xZUMJ9CwQSFm-2JshZT36RqMf_cvQWxmnrpfAYRno6m8-IEaQD8qhl_8F-wElCmZIqhVqlk5p9AX3hYc4ahKNJhY_orU-z2GtyPxSN6im49-E7i4mfEzYxLjwGANi9z4DISwo2_LBpaUFVXlvJVEHD0cmLQNhDRqh4rt0SG-HuUALeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21c204841a.mp4?token=PE23OgfBoAsgaZMbAUGt0LGc0srK1fGxiyta8s5BNC0UGzjdw3VtRrGWosYKkNeqiQPGAjI-6k30CUyr9LhQqK_pm1vUjFIZ6yL3IUAoRlxFJGVV5CpdNLJxYqwcl8YDCwFz3JeI-wIQk0ogOfLMaJlXYNqxuZPmk0mD2m8xZUMJ9CwQSFm-2JshZT36RqMf_cvQWxmnrpfAYRno6m8-IEaQD8qhl_8F-wElCmZIqhVqlk5p9AX3hYc4ahKNJhY_orU-z2GtyPxSN6im49-E7i4mfEzYxLjwGANi9z4DISwo2_LBpaUFVXlvJVEHD0cmLQNhDRqh4rt0SG-HuUALeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
فیروزکریمی‌کارشناس‌ویژه برنامه جام جهانی:
خانم‌های ایرانی می‌توانند داور بشوند. حامی بانوان هستم‌. داوری بانوان از رانندگیشون خیلی بهتره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/persiana_Soccer/23967" target="_blank">📅 11:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23966">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FgnJO2_AOvK9TEPExFdt1jhyHZQWDkAign3Nci_G1lCNX4hCQmY_HQiyQNqMkx13sOCv-aT3zSXHNmGAcoP8ui8kH9ZHHXgylaRQmisP5o3iPdCT874Fj7SoLmD2wwwNj6fRFKK6T2JvgCAzn-KHPCFbR02t8HK6SirqRjdfZVuP8CFm5f4Jd0ADt3tDA6uKbJLhCJzc_D2qQzUSHFB_l9fHF_hjiJPRH95Wbo8UhFkdsGxlL6a7oU6T2nHNF6njmodC78P7pmbtRp27Pp-0pUW0IZECARkUwuMGsST5ctn6a7_ziWTeAl_duk1m0s_QnzF2jPyPUCfGR6ja6aOwTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پیشنهادویژه‌فقط برای بازی ایران
🇮🇷
- بلژیک
🎁
🤩
🤩
فری اسپین رایگان کازینو در انتظار شماست!
فقط کافیست حداقل
🤩
🤩
🤩
هزار تومان روی مسابقه ایران و بلژیک شرط‌بندی کنید و
🤩
🤩
🔠
🔠
🔠
🔠
🔠
🔠
🔠
رایگان‌دریافت کنید.
⚽️
بازی ایران
🇮🇷
vs بلژیک
🇧🇪
💰
حداقل‌مبلغ.شرط:
0️⃣
0️⃣
0️⃣
0️⃣
0️⃣
5️⃣
تومان
🎰
جایزه:
0️⃣
5️⃣
فری اسپین کازینو
⏳
فرصت محدود!
همین حالا وارد شوید و شانس خود را امتحان کنید.
هوشمندانه بازی کن، برنده شو
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
کلیک کن و درآمد کسب کن
📱
کانال اخبار و هدایــا er31
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/persiana_Soccer/23966" target="_blank">📅 11:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23965">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iVgwp7TUVX7UQlTf-qOUzbcuJfgpkbDDfHc6s3-Wsw1npmhk0O8tD4D96HsQR6lJ2ePoISq1QyNKWiL4rfYHtna7xK6uZ6RTA6L3Tk9gNrnlsK_KlJVfExvLxScQYLVvFSuMdqwwXES0Jz6bhraAT-mxUZ8uZxcZUsTX2lcsxS3fS-e3uERHqITRi9ULjCabi0KBUKpbLUNwxKvYO4oVvEIIJs6ElWROCs_qf1qEYvC2qyzm8FZfvfh01Brn2LrooaXf6jkXmxsUlLd2YJUJ3uZAWsrE26GuFno7jJsKaOB-N3mgA5EicRwTUA1JWHPBzspGdiMuyjlepJbMzZ7t2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇪
طبق ادعای رسانه‌های بلژیکی؛ گویا روملو لوکاکو ستاره تیم ملی بلژیک نیز دیدار امشب مقابل ایران رو به دلیل مصدومیت جزئی از دست داده است.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/23965" target="_blank">📅 11:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23964">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YBpSNP-eB65-tiHV9BXqeb-2RKtIuQwr0oYIjrfoZoU2W8TcsVNPinq6aGxkTzfjTAiJMq3Lh6S_2YzgQxvJWC_o1RLBhK3m2TlLUBt7oVUm9KOY-U0bigJ3H8hx46jzXrKn6ZPYj4AF1k8pSane6rotxtYyo-_Y2g3xsPQ_XhVWxmTBPfrJckrGTXh8xb_ELjpaoAZmzvWZpPtgPPh3c5TSdWxsaaMio0-kmGH8PN79SCX8j8unY5YCyxvcN9z-a3vQXWxUHycEHJXmbs_WE65abhVhVPKPyXZWjCviOI0n1caINlePHKLFpcAvPpISc32X8NJ6w9RD5BmsikbHOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ طبق شنیده‌‌های پرشیانا؛ باشگاه تراکتور بامدیربرنامه‌های محمد دانشگر وارد مذاکره شده تا در صورت توافق مالی با این بازیکن قرار داد امضا کند. دانشگر در کنار مذاکرات باسایر باشگاه‌ها درتلاشه که با قراردادی خفن به استقلال برگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/23964" target="_blank">📅 11:09 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23963">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eH2evKFOr7ZBP3hw4hiPFK2qLj-1IfqUOYj_PXATFhVi7Sru8CpQ1d5uO5vPGsVgDSJqN9Onha3f9DWOTHanjFJTR222wwPVq16mY82Frt6qRDgDCuvC00mZBKREcIiOuAZDRIudDnjyfPKZf1h1cFobXBnZpa81adbfxLEMj7nswHbiRb4KYikGskQ8G1U0-x-6stU0E3iu0YA_MOm91QWU-RJ0wYlNBMrOFD0Jd9U58F4ihnWN_4ikkNkC0YDquCPABAwNYirPo1q_Kqvtj0O-YFU3DmDF4voAFcpySZ9PRxkJo5m93OZdhx1Zzb87yfeWq3Xjt7ci28rhLH15gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌شنیده‌های‌رسانه‌پرشیانا؛باشگاه استقلال امروز با وکیل‌ایتالیایی‌خود تماس گرفته که این وکیل به باشگاه اعلام‌کرده‌است که نهایتا تا پایان هفته اینده فیفا پنجره نقل و انتقالاتی آبی‌ها رو باز خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/23963" target="_blank">📅 10:44 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23962">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/caZWsBnquqJn_FUz7etX4ekibKsWeDSGxUIbE6i8IBzIYobUUfLLLBIxBKC8h3x6k65CImhafh5aJhxV86ttu2z1N70hZP48UTC0AC60SGYeN-a9-u9bg8vVlDlfEXufYrT5IWJvt1YHZIVPoHtRUm_QPdNB5YnlmkkCBS5aO39W7CCxXWJD2m6JR2hmLnKfizycMiGZfexWw1Wixwa1n64fzfwvN_7YNS2wOtX6ztOaWF44q-9xzqSvkAquzT8B370OnyxnjWi-F4S22y-mX63Lb_NMlESDNbZqNLsuFW_Cz8fve9zXMQ_nPxwAq0mE9wn6G_y9-Ug7N5ofb_rZ8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پرچم‌باشگاه استقلال تهران درحاشیه بازی امشب دو تیم آلمان
🆚
ساحل عاج در جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/23962" target="_blank">📅 10:37 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23961">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r8CEwgFv1ZFp0ZvJ2ahEFuSfLeJLX-OSBC8GpFZUevp1dCs_lSYT62YFbG0RgQDx5Dyy-kP1l1H2r-c6ztKKHG0FsSoZklv0lvpSytK2OwLwV-WskA1A7bcFXzCAS33GTvPMnsmJhVjPQdXraiTVkZL1blPyiTsYVKn--_m1UnXpT6RX1yqLm7-HYwD9Nfj6C0YvTAtdb8WcdAA1oURROjXy-D6xqvF6uBSgKrq5WDp_Grjlnu5dqG3Rq9rOM5Q5Z4Myclc-h8tGK_DVPCHrLK7Bgwh-y8Ae86YnPuIFBujpGN5sihiwwuQ9gbI2g0IKExcDK-TVDRCzh_uJwmoV5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
آمار پیروزی تیم‌های‌ملی‌آسیایی درادوار مختلف رقابت های جام جهانی؛ کره جنوبی فعلا در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/23961" target="_blank">📅 10:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23959">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/550fbf8a8f.mp4?token=lHXTQUm_1KN7jPMrm9-Jh0HhC7jBrce8hc5aB4B8YOHbnUok6QQniohiCkvIj73mZ-7lBQxKEDF2lv0JtU1aqwbNM9DPJfCAehf0Fl-lATQ0JTGfFB3FIRgfi-8BcBEMnNhvN-zZXl53JBl9jTph8mBfbK8aDu---nPA4LTzIpNqVVsDdjMB3xXEXqAOS9CJ-vKi-V6bpIfP3QeZJQ9dGYQCACUb_T60tXBGHfYh0FMV9wXY-REYwA4UOTgY_LZ9o8PbMaVhlzHeU0TJxldhF-nuC730bli-U9xRmglFT69XiAhdrg47LlRQo9F8I_ecSyZngigXGdfWiU9zRYq5Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/550fbf8a8f.mp4?token=lHXTQUm_1KN7jPMrm9-Jh0HhC7jBrce8hc5aB4B8YOHbnUok6QQniohiCkvIj73mZ-7lBQxKEDF2lv0JtU1aqwbNM9DPJfCAehf0Fl-lATQ0JTGfFB3FIRgfi-8BcBEMnNhvN-zZXl53JBl9jTph8mBfbK8aDu---nPA4LTzIpNqVVsDdjMB3xXEXqAOS9CJ-vKi-V6bpIfP3QeZJQ9dGYQCACUb_T60tXBGHfYh0FMV9wXY-REYwA4UOTgY_LZ9o8PbMaVhlzHeU0TJxldhF-nuC730bli-U9xRmglFT69XiAhdrg47LlRQo9F8I_ecSyZngigXGdfWiU9zRYq5Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
سرهنگ علیفر:
از اونجااصلا نمیشه گل‌زد؛ واکنش صادقانه آیاسه یوئدا بازیکن ژاپن به علیفر
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/23959" target="_blank">📅 10:02 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23957">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VTS0EgvTqu3GfqcBOj2tfJvO9yWBMVNM3D1pucn91f18jDzhkL2N3tvMU2jV1W1ApAzrXuvq8YzGw5xowU6QhXtRsPh0XoUX8_JyMSk-fz1sXMJyzC8wVvPtTHBsKeUJu2PpHKtZ4wJvqJ05NFm2U_XH1KDaxfeKR6axmJ1BSybLad8oaox88SVDrJsOXUsGf8H3MpIAgKIWv8Iogks3NbGvHkxbtXNKPxrXU8w3-QP7zQW4Ibe3VauBidGzzx_C-3_4Exv8lKhTcTUNC4OFuVGUQR3FryOdQEzNVmUq_ztA_4WSIBpiw4VxFXogpBO8Bgk0yrSLAcYiMX91fXCQMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ROVYeh0x63C3JcvKCbT6L8CXqP6B_YGD6ZkXa3ngZXLAH3fTavQXiAJwbpYiFcoMIlPVih0t0Gh_Cq1Z-1GrvId4xyjJ1UP9cc0Yn1C7-qI-djPnIt5NOOSwq4zp3kgbScWV6B8vwx7dWOehZ3n6peq1vA9QDDctmpXRh7q57ZKA9I5-4SRdy8q5wnMPhnccHBGMnA-T7Py3XqEK72v0d7phJQpSX_0hf2QafheiVERgE9A_M2hSgyW7OCdfMZXLt6A-fLZhnCMku1u68Jiz7-HnaZcN7S7wx5lWRe63-ElZlha-BfUNlqeE7WYpEbIqLcn9giw-jJMcWQiQtdYc8g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛ از جدال ماتادورها مقابل عربستان تا مصاف بلژیک با شاگردان امیر قلعه‌نویی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/23957" target="_blank">📅 09:52 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23956">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q1ZDqF6BZUFmtP0N0-IfpndXIpzFCOMveKf1K-UuJALqyWW6ovcJKvsIOEEY00m2-L9omwcp0XZ52-yObxm2FZ23Hy6Km4hS7O3ta35FO7fbIF4c5hG1j2_6rsT1DpZv5ifOwTBQvfpXiC-JVezi26TabXF1zLUzkvP5qbVC9xG2iM8iEHyZePAQ-f4L_sJT8tYyWqNmhye7DaCnkSemOB_6tKiZST_TBmMy0VGXoDzG-9A4xwNLThw2zRNbHJdp2EyppeqMsn2WYaWXWSE2o412OCAqzlVzho_IyhAXwmjV7Pmkb1HlEBr3N_qVQtMIWOSYCGzm6mM2VCubqZAFhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇪
رودی گارسیا سرمربی‌تیم‌بلژیک:
مهدی طارمی، سامان قدوس و رامین رضاییان بهترین بازیکنان تیم ایرانند. رضاییان اگه 25 سالش میبود الان در یکی از بهترین‌های تیم‌های اروپایی میتونست بازی کنه‌‌. چند تااز بازی‌های او رو دیدم فوق العاده بازی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/23956" target="_blank">📅 09:01 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23955">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EOljrrBvmZTpmkwhG3iczplb_cuXFmIvr18YS4dTCHD_9kh7yCAVmOwU8GzWxQQtaVwzJM0OAoC7FEUHVMP5ZQfsKwNMW-i8DyLqQvfY2p7tUZBrISP9lRnFtEZ86qJbEFDleB2G005pbZVF9XlrgHyhDF0zjbHfkqg71w5bHYxsFvnAP6aC4r69hwegyfATWjWB4lma0M577VN6DPxuzi18yZcf9b2Pi4F1V90Sy3b4oa_8UvXA27iKJNl5MX5dRBFkD0R6a0N_udMtjLkxbtIE9ChcRJhmBLMdmuy_aN3RaMiFN9UBRFcxJqwTz2EYV5FvpUKMmGjGE4L9q_vtfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته دوم جام جهانی 2026؛ یه پسر کُرد سه امتیاز ارزشمند روتقدیم ژرمن‌هاکرد؛ کامبک  دیدنی شاگردان‌ناگلزمن‌درشب‌درخشش‌دنیز اونداف ستاره کُرد زبان آلمانی‌ها در فاصله تنها 20 دقیقه.
🇮🇪
ساحل عاج
1️⃣
-
2️⃣
آلمان
🇩🇪
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/23955" target="_blank">📅 02:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23954">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TkNigWgx5bUzDNT58cOpJcFBHlDV_8c2gLTFYw6V3D6QcZff6inbLPyagNAIzwo1ZDAjo2QthxHNvLMKBgfeQVE3MxUN7X-H556XRbnQ3yAZB0VHKbAAa16qAAMOD8UIMCMhqdDI5kA4ZkCNyVcHwrs21VOHEGgGpSkmZ7wVer05lToWloo3T7rQRCkHCUyZnH2dbMeScWkfTd5w338kUlLyBjgstjCYh0rrSvQS0wfJVTm4XG1QYo6tx-wFEVr7eG1qDdC7011q2WsCNP4QUhHPYMzPq7dUi0fNgxNqoh6qznW6ov2K8FIUmhqN1pH7Zf8WjvbD55GPj3OlT8GUIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
دنیز اونداف ستاره اشتوتگارت همیشه در شادی های بعدگل خود کُردی رقصیده تا اصالت زیبای خود راهمیشه به همگان نشان بدهد. امشبم کلا 30 دیقه بازی کرد دو گل زد و نمره خارق العاده 8.7 گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/23954" target="_blank">📅 02:35 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23953">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XcsVHwqXOGw6_nmq-KVVJsO_-aOrK44jW-x5LpRh1L9zUUWw6ZRMuQNd_kekWcaiyyFGwy0t__KrpHu-kxsyM7Uvky1yrUmB9hIDVWchKNaqLogtY3bpQPoz3flHNOsvWvdsXu3YcduFAr_bsvODHqO0XXkOdftG6BNaF0Zt1yOOeT26jJRi-tXmowLxd8J2zAzbb6pNHiEEWPjoPK49jIJUG6aT1FU9bnCPUK-87fXDmGezU-bUQ5Qp5TSB0IzlRwdfSqhgpvgcngreMxgAjCmP7tlX18xZWihi2pZWyR8Irx0uoskSSRitEA5pxrAJiOHpduv-YqiYA2Cebr448Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
از جدال ماتادورها مقابل عربستان تا مصاف بلژیک با شاگردان امیر قلعه‌نویی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/23953" target="_blank">📅 02:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23952">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PG7RJhAuKckc4tkIV3Lal-gH9m4cxVl4P7lNvrSRJicgGI2rbt05uTldgGNO04aC4GBjhTZy4FI8S_Hh0eKEDYVhHlSC_q5IFv2mqD_gRTA0wF1bTCwD4EiAR9HP_4ry-UIadNNkcI1vRe1WUyjMUoVWqAHIj_cqXQk75OGpnNsIQKkSuInGrVNLrGs70U0BqqJ1axl34VCm9mKOIM5eYJybpl3vRUzDfNBIhhedR28meoTtHNUxFlPb-YLPD1eGc42np9am3s0ZkcKEYTKYibIy-D4ABp4WujBywatmbBIU45aehKmt66RRP3URzo_ke6gYbg7mdEy7dja2TG0iwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌‌‌دیروز؛
ازبرتری‌برزیل و هلند مقابل رقبا تا راهیابی مانشافت به دور حذفی جام جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/23952" target="_blank">📅 02:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23951">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bf800e040.mp4?token=Va9hu9Zxn8Z9g6bi5qfasXg5qpNqqo7r_DP45GNvnpQkER9pkVHnRjFWzLu9yX3VxKFBahDK3NYGLN6N6oYyIqfv9vMua7UFzmEseljkyXG75jSjZ1IL3JzB_K8WLZXmMLPqZmC-BzL5-jauf3ULzkCBe4Lbho7N7gwp4KISALl_SB1F4gjGL9Uu0uZ7JOFfkWbLnon_AqoLXOhz-ZZ6A4mMPoRaqUFUzxA4-XwZQcyAHQo0IYvs9V5umkr38wG67ioRM8INLRIP3UTeujOCbPK2et13QUOgPAGfPwaGB7tb3DeG5zx4q6dUsiH_Dz32VR9AXDa-CEcsbBVqfSbI1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bf800e040.mp4?token=Va9hu9Zxn8Z9g6bi5qfasXg5qpNqqo7r_DP45GNvnpQkER9pkVHnRjFWzLu9yX3VxKFBahDK3NYGLN6N6oYyIqfv9vMua7UFzmEseljkyXG75jSjZ1IL3JzB_K8WLZXmMLPqZmC-BzL5-jauf3ULzkCBe4Lbho7N7gwp4KISALl_SB1F4gjGL9Uu0uZ7JOFfkWbLnon_AqoLXOhz-ZZ6A4mMPoRaqUFUzxA4-XwZQcyAHQo0IYvs9V5umkr38wG67ioRM8INLRIP3UTeujOCbPK2et13QUOgPAGfPwaGB7tb3DeG5zx4q6dUsiH_Dz32VR9AXDa-CEcsbBVqfSbI1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
دنیز اونداف ستاره اشتوتگارت همیشه در شادی های بعدگل خود کُردی رقصیده تا اصالت زیبای خود راهمیشه به همگان نشان بدهد. امشبم کلا 30 دیقه بازی کرد دو گل زد و نمره خارق العاده 8.7 گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/23951" target="_blank">📅 01:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23950">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/exU-xW9J9CH_WkhPd51on3UT7vgt9y6cZsfOOqNhR9SniZhnnh05jcjvWqixJitCZCUDC2D6M8lIxtZBrnzHVyHqE30mTJsuw1fKKAv5gbkUaAmu97kSOBm57j4HLngvqrldrjT2q3VA4lJ59u4IbbeOcxAjmeRZL9vBMQ2frqFwAXbl1ld2s1ISVumKH7J3KYFgQQPEow9sDr3h3NiHO55sqCuJh5SFKnhmfTaW-iWcBa-5K5iK2I6oGOsC0gBStMy4YP35xpi3x5xrVMzQh9tD2uOG18BO8fmMMxleR1kQTA51RzJeJeDSbWzjzgqZnYhzgFXy9E4msR9MzDtXpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
باشگاه‌ گل‌گهر به مدیران استقلال اعلام کرده با دریافت20میلیاردتومان‌رضایت‌نامه پوریا شهر آبادی مهاجم جوان این تیم رو آبی‌ها صادر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/23950" target="_blank">📅 01:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23948">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40b51e8a93.mp4?token=hzMuZFRpTc4wUTfgBJgzCd7dr1pcI_60XljzfLbNbP_JQJUi1wtE3fkl229gZUssWeUrXpekgS5-xUADwYc42B8VH1823IT-h43zmo6-FdVqV-8RRhNAp9rgWsZmQbbj9pNAqmFzNa1566EBOX6jg_sQuSa7HaNtbrQRUujTHaGyZxN8XgbbuLsNSYU07nm01wbjmipmca_-uWxUVvKGHc18LWvcqbtsrCKDwc9icIXaeE6te-haxvZ0WeQEv5OK7KDMPhdqQf6UXwCzFu6jvJAUq0DR58ywolKATzxoqF5Yj-bYcBbgKA8LI7f1UV9cUjksLk-zr7yP0vb0OsKNrhMtrKVhFjCnfYMQj1NalOywkVi7KMaOHpH_xS8zbwcFas5vLRvu_dHJ72CqFoOTvH-L7N_3_Tg-kQXrmkS0qQOF84ppSjuo7ShFXQd1dXZY_H6izeOHMV-qfsK-jN_mHkDVlgWRfmWzQUnddr0QDJw7tKePi0rD3xvpfN4e3FOQklh-Q7-2BQhhXeBaGA4hDU7G-K5ZI5-EugBZr3S9lEsKV2jCU8Z4OMRrhxYAzyar7PwurBf-nAgdpKYTvY-hAGcZpj9cXk3Ic2-R_7sirujkadti-9oooaLxEL5woJBbjHByLqNdP0RapbqzEo4aNaBavx8y17iZsnktD3nh0vs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40b51e8a93.mp4?token=hzMuZFRpTc4wUTfgBJgzCd7dr1pcI_60XljzfLbNbP_JQJUi1wtE3fkl229gZUssWeUrXpekgS5-xUADwYc42B8VH1823IT-h43zmo6-FdVqV-8RRhNAp9rgWsZmQbbj9pNAqmFzNa1566EBOX6jg_sQuSa7HaNtbrQRUujTHaGyZxN8XgbbuLsNSYU07nm01wbjmipmca_-uWxUVvKGHc18LWvcqbtsrCKDwc9icIXaeE6te-haxvZ0WeQEv5OK7KDMPhdqQf6UXwCzFu6jvJAUq0DR58ywolKATzxoqF5Yj-bYcBbgKA8LI7f1UV9cUjksLk-zr7yP0vb0OsKNrhMtrKVhFjCnfYMQj1NalOywkVi7KMaOHpH_xS8zbwcFas5vLRvu_dHJ72CqFoOTvH-L7N_3_Tg-kQXrmkS0qQOF84ppSjuo7ShFXQd1dXZY_H6izeOHMV-qfsK-jN_mHkDVlgWRfmWzQUnddr0QDJw7tKePi0rD3xvpfN4e3FOQklh-Q7-2BQhhXeBaGA4hDU7G-K5ZI5-EugBZr3S9lEsKV2jCU8Z4OMRrhxYAzyar7PwurBf-nAgdpKYTvY-hAGcZpj9cXk3Ic2-R_7sirujkadti-9oooaLxEL5woJBbjHByLqNdP0RapbqzEo4aNaBavx8y17iZsnktD3nh0vs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته دوم جام جهانی 2026؛ یه پسر کُرد سه امتیاز ارزشمند روتقدیم ژرمن‌هاکرد؛ کامبک  دیدنی شاگردان‌ناگلزمن‌درشب‌درخشش‌دنیز اونداف ستاره کُرد زبان آلمانی‌ها در فاصله تنها 20 دقیقه.
🇮🇪
ساحل عاج
1️⃣
-
2️⃣
آلمان
🇩🇪
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/23948" target="_blank">📅 01:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23947">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lMb5YqSTvV6hUgudyAEPz4rIqjEIIYqqdRBInbaa6tLn7689w3tdQZa8CSG40QISP8ItSv_lvwU7mR21UsvDxrReMXx4AEI_NHGTKfZWE5ZS5-HkuM2JEddZMAUuCMYw5UWd57Xa-zI7V6EY1BE45nlkIHnf-DGzqNW9jpCsHxnuMPDMwI6XgDyIHOY40qu2_3gP5RgwFvDRoPIcaSZis9N_j0FbrksBZxxWFmR-49z3Cmm-Mrqdd9KoDp4NjK4wstE35Mab_Gx_ctdZRZRbU7CaRqpJF07S5Muwg-VXqZauFvDcf8_w9LhRgoMYK5X5xcnnWzOOghP4NPaMGFwQmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
گل امشب تیم آلمان به ساحل عاج: ندیم امیری بازیکن اصالتا افغان پاس‌گل داد. دنیز اونداف بازیکن اصالتا کُردگل‌زد. اونداف در دقیقه 60 به زمین اومد و8دیقه بعدش گل مساوی رو به ساحل‌عاجی‌ ها زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/23947" target="_blank">📅 01:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23946">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LsqHgy_rrd8HXxpvQQDKjR_pGzacO4rggG_9C-_RkZJecamHgqRMyp4dGW5BMAO4NCfw6scrBNO90ErKvc3-TJOx0ZBl7P-W3OR1VINGTS7p8GpGQCbtOU03o1C3ZtJ_v9oexg60tXbkefryRcR4l3TudUy_ght_xsFHt5_GOmJ4GLb-ln9xqFXpC99ASwTCcMUVzPmTdoCwxLqzlwGAhzLHTp-XSfvuqT3kOkTo-NjfTR1lS2VNlEOQ4oxOP3ZAJDDLGZoq4dG1ThKKdBi19uLK7vpa_LVdRdjG80RbTltY360O9RZVChqAIsNlPQp49jg9deICEDjQX0drnJ-elg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته دوم جام جهانی 2026؛ شماتیک ترکیب دو تیم آلمان
🆚
ساحل عاج؛ ساعت 23:30 از شبکه پرشیانا اسپورت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/23946" target="_blank">📅 01:21 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23945">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TexTjT393f7QGSjqX9xClr805tP4Gld-RNrVI7CBahwTP3Un1Wdkh3Vz_M8hehSZBmoVhDBG7jLjYtZE-Fo1mMhoP7ILGb8fQBroEX7ctSYRTHs2-QlM6aSscxOyIbLqOC4azCmCL7v2x8tdCU9s8AN6gxv_AYCvk_bg2vaJZanJIsiVhgnp0auW8KIljYSpnised6wgMez8wc3rH00m5zwHlWJFJv6-Im4Lq5vC2G00HKUNH6_gkRDJ-cJwtNzW6IGLktR8jzuLdPAHHKJfGiXexJTNNebjygrQmFs3qDSOz4419M5fZ9VjLLyKkZSYCJ3Ox8JV-vv2sl9cUm8lDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👤
امیرقلعه‌نویی سرمربی‌تیم ایران به این شکل نشون داده که ساعت رولکسش رو پیدا کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23945" target="_blank">📅 01:12 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23944">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb124e2149.mp4?token=LuDvvfMgZu2rn8eCykn71H4Kwe0MmCyy27V-lfqcvRKaU5QtV36l6s7LxBlSMB71HmYSrvzw_0WVyd0H6jaazQBB0CnrAm4LjVEc7GJzw3l9q1GP9Erp7kiKebl-G5EATfAzGwEe_LMV8VYHjjYpAjq6fcHBqBpttPW_Uwz64EK-D29QgT7K3gXKsqQvY6aDA7gYi87v-636Xz3YRsgdxt484qT7jlx9Oe_Du0-nZEWC1mQbAEOcLZM1ksM3GytQoE9xSeH86cXOIRvA9lL4ZFu9HLkdgoB0vYGM2MMLixBIQ62Qwu8W-LuDryyJUOR2KD9ot0i_a-Qy4B_bMtPBvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb124e2149.mp4?token=LuDvvfMgZu2rn8eCykn71H4Kwe0MmCyy27V-lfqcvRKaU5QtV36l6s7LxBlSMB71HmYSrvzw_0WVyd0H6jaazQBB0CnrAm4LjVEc7GJzw3l9q1GP9Erp7kiKebl-G5EATfAzGwEe_LMV8VYHjjYpAjq6fcHBqBpttPW_Uwz64EK-D29QgT7K3gXKsqQvY6aDA7gYi87v-636Xz3YRsgdxt484qT7jlx9Oe_Du0-nZEWC1mQbAEOcLZM1ksM3GytQoE9xSeH86cXOIRvA9lL4ZFu9HLkdgoB0vYGM2MMLixBIQ62Qwu8W-LuDryyJUOR2KD9ot0i_a-Qy4B_bMtPBvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روزهای اخیر شایعه شده بود ساعت ژنرال فوتبال ایران دزیده شده که عکسای رسیدن تیم به لس‌آنجلس نشون میده‌که‌خداروشکر این خبر کذبه.ساعت‌امیرخان
🟰
خط قرمز مردم ایران
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/23944" target="_blank">📅 01:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23943">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XE56T4cDhI_0ZDQMRw59vMF8y8fp-eIeNemfDPT324lJ0VBPq0YNF-Fjm_rD0jZpj3Q5lVR4NYaphUrhNgnnNwxG6SyYkSGMHp4dBh4o8zRqIhHpPdRbsUR2kY4lqd25P6eyLbYdxTfwVSqv9a9efha6PmTaVu5zuLmiL0njz3Hm1q4hgibYkL8-sr1_KQ4NTQavx1HBnJOdeyuAdtSsi3N1nCh-ZjDPYBzMLLIpVohTOWeaf5P6v4Nx8V2MzIAFiHq66WECoSHNknfYu3GfKb80zugagaO29Xv4sgy4DtmmTYQgcw-zr5rOTQ_d73NnywsFiAcEG6auDVrJQRKKww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته دوم جام جهانی 2026؛ شماتیک ترکیب دو تیم آلمان
🆚
ساحل عاج؛ ساعت 23:30 از شبکه پرشیانا اسپورت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/23943" target="_blank">📅 00:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23942">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lnu3rdG57mFzPLkX6K2fBc3rWaIA_5DqhT9s3SnfxtZakAW3C-nFMjQgl-i7gkFtoi7apWTYFjHtMabzRCWDQ9qUTjwoT9B70t2JN_WF4c573DIIaOl0p0PSLhlt9JQT0OCGlST6XcFPBB63h-jRykHtPnW42PdPTCc4Vk7sJGpLovD07EMZrsT5OBUBGUPNDEVg_Es4r8HqS9fa6_xwPdUtfSO0WOcqf1rUzD4gY4YXRUqOS-9JD88YogSizScYbQsSadpSDaZRfpHNVhXyrEX0ln6cRSRrkgCBFy748-ElYbh1348fSTf1vZqLGLBFBoau7Po-hObfMYFi3UCHrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛ مهدی‌ گودرزی ستاره‌ جوان تیم خیبر امروز از طریق نماینده اش آمادگی خود را برای پیوستن به تیم پرسپولیس در نیم فصل اعلام کرده و درصورت‌توافق دوباشگاه‌این‌انتقال انجام خواهد شد. احتمال اینکه فخریان راهی خیبر شود نیز زیاد است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/23942" target="_blank">📅 00:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23941">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a6c4ff321.mp4?token=r-5vsb1WGgxONBeoyuI3pILcJWh_C9tU0MomCal4fBYF3OdeT1m3raBHTD44igzh45fyHyF-4cPfSzZavHffGNvfNOiAe839gSGT6MeAt5WdZrDeWu7nIWaUrO3YtwpRJaclb1z0MvBb5-07Jqw-rG43xkBw5mWn691P7S8LVUKJsRwJE9ndVSDUGS_nQ9l3m_rX1BPx6DNOSH6JC1hjJ6L5GgDFDpEu4jyOYMe7zr2oQl8KmL4DN_3j-AFRqSgO4J3mxEKoPYIxf7n16-6deGPYIDr8P_61g5NPu7ETPUYotT4b6zxHrMSUni_tPpDRpkCsF0RGrE55vNPlU96u1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a6c4ff321.mp4?token=r-5vsb1WGgxONBeoyuI3pILcJWh_C9tU0MomCal4fBYF3OdeT1m3raBHTD44igzh45fyHyF-4cPfSzZavHffGNvfNOiAe839gSGT6MeAt5WdZrDeWu7nIWaUrO3YtwpRJaclb1z0MvBb5-07Jqw-rG43xkBw5mWn691P7S8LVUKJsRwJE9ndVSDUGS_nQ9l3m_rX1BPx6DNOSH6JC1hjJ6L5GgDFDpEu4jyOYMe7zr2oQl8KmL4DN_3j-AFRqSgO4J3mxEKoPYIxf7n16-6deGPYIDr8P_61g5NPu7ETPUYotT4b6zxHrMSUni_tPpDRpkCsF0RGrE55vNPlU96u1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خداداد عزیزی از دست‌کارای‌ جواد خیابانی فشار افتاده میگه حضرت عباسی این کارها چیه میکنی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/23941" target="_blank">📅 23:53 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23940">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QJOMxK165KRnNbQAfK6dHKitJBz5X52qosnCd0GFmq72RqLy6dXD3IXo-_dQplUcG_w8_1gXow-mXp-1A8FhXzjMPd7qufcM6XiAqUskyf6X8dGH4P6y8p5-5iBjJvLmMe5jg9mRMd5cOoQqNqInVDhlqLBzPQsO0-fm3BOq0mDknu_HBSH_zP-2Qt0RJoFwUE3eHN6AXtUDt-Xds3k0JoPhtaaoIQF-a1sFfbwbnlRXkle41hCNg6rKu97lOQISTeQu947hkXF36C3SbYXXmy3BI8g6_OLdZ-EVMkosy1X6g5kw242xgAEphmtvFuifxxStIMa8vJrCR1u5GdkTXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنانی‌که در جام جهانی ۲۰۲۶ امتیاز کامل ۱۰.۰ را کسب کرده‌اند: لیونل مسی مقابل الجزایر؛ جاناتان دیوید مقابل قطر؛ کودی جاکپو مقابل سوئد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/23940" target="_blank">📅 23:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23939">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cJzjvK0Ur_u0KvqV_VFH_vBKAmUghHBtZ5MrKj70pLd_pqe4iHqnPgixe72stRpey4It7tCrohsSFt90TEksMq40jJefAMKnq_z9Mq3xQxCrP6qxG6TiIIjdCe5o7CQqOdEalcULARw0MJmgk1f_tgNtW7ZeyzpsMQF3YgZmnzI3ndjNdPejib7DefqK_jgIkmJeVDbbYrOlcYVLT849VrSEZKCxzk_HbqyZ5eYeraiV8WmICYq0Fe9F7zuEH8nP7jeCSeJ0SWavMKwODtsCos8crq7001NfoiUoQTNt_ZvRwre6xwpuqulSV5pOijpmHttrJOnt58zhO5sVm60rMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم جام‌جهانی 2026؛ پیروزی ارزشمند و پرگل لاله‌های‌نارنجی مقابل یاران گیوکرش در سوئد.
🇳🇱
هلند
5️⃣
-
1️⃣
سوئد
🇸🇪
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/23939" target="_blank">📅 23:28 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23938">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k_ObyA2-aEaFBX5KMEIWtjojLVSREMTRvj-vnXNcmwfaO4_z-b3ivkDRh9Vl_w4RtMFQyBLpLtjosQPbUo_RgPowTarxhBI5tKO4rQsvwMD_HfCCohBcqJ9n1YzhmBxh-wiIXeei8raMC9Z9E59kdumFeUKyiBT4nxQkkxCF_XgkYPe4UdQjDYqfsSjoaMeJo_qZF_JXoqJ2cLYCAtNhlhuBUOa9HXxG3hQ2Y_XzrHIJgow5TXSZ9ClCC17hVYr1aKSFzsytmOlnx5H2lVWYWwaoV718ItKAM_KXg3EAvR-RTq-6ePjQs5yWO5Zjyyw8Qi4a5zf72QijnZm5gH2T3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌های بلژیکی مدعی شدند که جرمی دوکو ستاره تیم ملی این کشور دیدار فرداشب مقابل تیم ایران در هفته دوم جام جهانی رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/23938" target="_blank">📅 23:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23937">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qhh02YrScFqmUEXqLBmQOGYcIVo9KkSdNgmsydTUv1JtABxoAoz-Tt4Ca5WXfvI7b_2kxu3knI0TFm3Vhif8XbrpqzB1EAboBGqY3bT65znk6o9PBd-xzleWhJOJNy3658QBhotcbNfvw4SeuC48YH8O-pF5s9ADAaCLDK9qABCTuKMPozHhZarYYOBYvu6bewR4DSwRFL4kSWjo1c2wVmLGQ4vOOZ7p1zmDaI4hn5-82TuqZwhqyRCS1C8NDdu0XL79rQBT3iNYIj03azkG4R5Va4zEf2ZSIi6vp0vbqjHnAgDFTKJttT94rrtnpvDGnQnSPpecaCfHMrdN5Z9nng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ پیمان حدادی مدیرعامل باشگاه پرسپولیس برای انجام مذاکرات نهایی و عقد قرارداد با دراگان اسکوچیچ  راهی ترکیه شده. به احتمال 99 درصد اسکوچیچ سرمربی فصل پیش‌رو سرخ‌هاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/23937" target="_blank">📅 23:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23936">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e541eb115f.mp4?token=kNl8VyPU7FVjGngmcW-wtA40dSCAiVhLdUg9uzJyN6W7KPeDMqwyK4zX7rrep1ITz1gYFcuf22bkZLFcp2Y94-ZHwAfyRs35O2_bEQjadUNjRaSUWyMdni9_fCbfVK7-GkLkQJHvvDaR318rDyJYE_gRoFwUSdO-oMMWB7BDWrmcYUN7OhZpRDMhleHt49KLX3fN_8ghx0_q3YWseViDyorN6DTydx2pUwJWF2KIlcsleOYwoV80K5ivJrHvEtVoNdUsYrKNjN1SasFVfpt7a3GFgQnDSO0aJXGzjoZtuApsWkybCpLxHCs8rvH__ZTmvA2b8Nchoopr06m40jqd65LfOGvTs2p7QwMfTdrt3UYE0q4bK3ALtIa5BZT_nvBZF7v8wrs6CFv4gv1cDZqPeRP7XJedwKgLJdMjGDMaq6MXxi6z_bbw1QJ-V9nVy_DuLgIK3rTdJbRkRvi8GK79EGFwbSXmRPV7beYeB6BrpeVvBxW6NZS8PfS_cNoGnTz4Qswb7PPYpFhFHVhusFl2rvW_A6DVb22hNKnmIxINb2YIjdL_En38kOD_pegNqTvImobkeuN4kPn2rOUy31kba8RlGI8fuA-q2GK55aMl4wq7YNg5JJDZhQsdX-1qIGPl266-_hEbho1E4DC9sIfXwZQpdwOpYqX02ha-Ev9YVis" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e541eb115f.mp4?token=kNl8VyPU7FVjGngmcW-wtA40dSCAiVhLdUg9uzJyN6W7KPeDMqwyK4zX7rrep1ITz1gYFcuf22bkZLFcp2Y94-ZHwAfyRs35O2_bEQjadUNjRaSUWyMdni9_fCbfVK7-GkLkQJHvvDaR318rDyJYE_gRoFwUSdO-oMMWB7BDWrmcYUN7OhZpRDMhleHt49KLX3fN_8ghx0_q3YWseViDyorN6DTydx2pUwJWF2KIlcsleOYwoV80K5ivJrHvEtVoNdUsYrKNjN1SasFVfpt7a3GFgQnDSO0aJXGzjoZtuApsWkybCpLxHCs8rvH__ZTmvA2b8Nchoopr06m40jqd65LfOGvTs2p7QwMfTdrt3UYE0q4bK3ALtIa5BZT_nvBZF7v8wrs6CFv4gv1cDZqPeRP7XJedwKgLJdMjGDMaq6MXxi6z_bbw1QJ-V9nVy_DuLgIK3rTdJbRkRvi8GK79EGFwbSXmRPV7beYeB6BrpeVvBxW6NZS8PfS_cNoGnTz4Qswb7PPYpFhFHVhusFl2rvW_A6DVb22hNKnmIxINb2YIjdL_En38kOD_pegNqTvImobkeuN4kPn2rOUy31kba8RlGI8fuA-q2GK55aMl4wq7YNg5JJDZhQsdX-1qIGPl266-_hEbho1E4DC9sIfXwZQpdwOpYqX02ha-Ev9YVis" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت های فیروز کریمی سرمربی سابق پاس و آبی‌ها درباره‌ اون‌ویدیو معروفی‌که ازش بیرون اومد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/23936" target="_blank">📅 23:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23935">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hXir4Tdg84lYWO-8hVC528Q3DoVrOTNo3_tIHFgHLDCP0UkOBft6VklnuqzflM5BrTjvjNGImd9E1S5sQL7vz1aLYbxh3_ouo2NtXG2X1UZOKkH4hHhmSVMhO9HgAGkHcqfx_ik2J-uQzrcBcrddN5QSdxGBmSGdP2eDkTTcKvovDYyfRjC9Pj_viNEFO3fc7PiCRvZXsmOFM1Ym4-WicJDSr7WFKpgNF93ZTp2vMjEQzexMpZl8KIZK788elAs76vMPMrZP_8ipONI_N5OBlJJq7MW_W4801pzfHhS51n_-X44oGO0Tx00Eh9SAO4mSdkBG9Sx02M_wiBsP0lnAvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بزرگ‌ترین تورنمنت فوتبال جهان آغاز شده…
📺
پخش آنلاین و بدون سانسور مسابقات منتخب جام جهانی
در کانال تلگرام Betegram
🎁
شرط رایگان ورزشی
🚀
100% بونوس
🪪
داراي لايسنس بين المللي
🌐
فعال در بيش از ٤٩ كشور
⚽
هر گل، هر لحظه و هر شگفتی را از دست ندهید.
امشب میلیون‌ها نفر مسابقه را تماشا می‌کنند…
تو هم به جمع آن‌ها بپیوند.
🌍
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/23935" target="_blank">📅 23:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23934">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">✅
هفته‌دوم جام‌جهانی 2026؛ پیروزی ارزشمند و پرگل لاله‌های‌نارنجی مقابل یاران گیوکرش در سوئد.
🇳🇱
هلند
5️⃣
-
1️⃣
سوئد
🇸🇪
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/23934" target="_blank">📅 22:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23933">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mJAftfsek8qyM61wD4YEVG_0traQYCQ46Qo_1A3qZfV7Q6W1vNoxtjUmeMt60Cz5G1zouR5RE5vh1NDv4Y5oi5ht8aPGY4mIaQpAh-QWpS_LIY79qYztvm1xAOfi0_hvYuDqhvAsZcrbljbXLQRknfUdWKItaBehmUQIwsjjyvSrASBIlCFC0dWDseEnX5KTtP0FMkUT1iQIEKM6OxbncQXOZNuLB9CNjS1PZtkZ2Q-i56YcGt3D22TGPVshLErauHA68kURCHGyiyMVq1Ur9U98veCWK92XUEgfyaRa7TdA1dsIp1MCLzucvxGpjUCz4AG3I1iCH2ytcRJnt3tDpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
هفته‌دوم‌جام‌جهانی 2026؛ شماتیک ترکیب دو تیم سوئد
🆚
هلند؛ ساعت 20:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23933" target="_blank">📅 22:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23931">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RlbE1-uohwQD5HjfarRXukuNwrmSi_LPFcwCQPyrZn8EY_pu1TCr9HNqzFNldtWMmmnZ9AVALgB2HvN-OUqGy9OM6NjrD6Mak2qbD1hv_Milk84n8Nm62XjYJZN-sSqUSCEfkUT_fcfD4LTaQrS8W7tpVK-6-u8fhkSGMkGhSJ07LKNAO5myf6xHkp2b9wD95i4WuLXrofzmjnL9VlrcUvxtOfTgTYmnUUW0ydEE35uS1ZBbmhGYfoW6F_B5ix1pxHusSsUNmUOsw5wcXcx8apVSuJU4e0FTv28Yje5oppJIKCD8w63PL5MbT-ueXBArqa2QEdYoxS9-71xetlK57g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rWkDMWE5gOkToF0uMcWoBJI9QQB0JSPe--c6aybKhVGgjDw06xktmz7vCOsteBzICguWwZ2mDtmnBO4XACUJe_A2hTn6C7iZc1RaZsf9slXe6eYWNRmQzqVDjpzBJD-2SBHs8xVVRZX6gLfXEuwLSQ5FTWWsjoCiGbMHKNR4U2UQSQxmebq4Z4m0nqVEFGMLblqcU-ehLxzVGsVbtfUcthpGrjRifT5LBDvw0QnuMn10jWBMyPm17syegA8ReoNnHH9ScjIAN9BwEHnJzRONd7xXei9dLIVVmo3Drc60DvMnVZQXD76Kph0r7QGmGYot2b2dQtwZg0ZUGybBKQSVrQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته دوم جام جهانی 2026
؛ شماتیک ترکیب دو تیم آلمان
🆚
ساحل عاج؛ ساعت 23:30 از شبکه پرشیانا اسپورت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23931" target="_blank">📅 22:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23930">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Em2J3F9kDheM1q45J3Gr734qz0tI66N_Q_CSswk6fMNY7waZQp2CI3-aM16nfHlUGHU5DOPrSue6Q1uqBG3WneiEjtdcBtDmTf3CX-AejX8BxhQFVMvl9bptOFaX1_X-zr_oGy7BxSe7ENY78mo0Zpmoxfb7RhxJswNxSgC3aYWqgGX0afpdFPZbanHyYMe24_bzi2W1RGWULD8O0MXWSn73SLJr3tFQLAnnKlV3GNFULHxW854x8m0Qmab5JjBUANz_UP8jbMfB_8qjwWLx1F9yN8EcUp2hSIpeI-ku1MNvxSgNJQyu1bh9BYhcQQA7pTccVJc2vqCsNvOW1yU3tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جرمی دوکو ستاره بلژیک بخاطر زایمان همسرش و متولد شدن فرزندش اردوی تیم ملی بلژیک رو ترک کرده و ممکنه به بازی فرداشب با تیم ایران نرسه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/23930" target="_blank">📅 22:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23929">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3537466720.mp4?token=MJgTh4G94WTy4WZbS1rf_9gfaoozlqjBnHT9VT_x3KAWUZeFC7GfZU-1ghFjCkQoNAus8X9tE3UvYS8MjMudRBaOr3NDSdXYhHPysFy1httR9aJykJL8a4QOFHyy44q93PjUEKULHpe0y2rxvFov0tDWIW8PPTNDQz8mYyHip3joRJZ6YeoM3Iiau92Ky25alhSlum0bzN3c2fFaGGwXSGnX_VW-QyypRmqYEXEKcNeBpCyI7JUJtNzNSskaSKCQ-LtENj0I36UmcMI2y3ijIULMr-BBVuknbbNMLp0S_znrV5Vhx9cvT69GeO8YzpXuxmuU1BEx9Xavg8jQ2NeXGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3537466720.mp4?token=MJgTh4G94WTy4WZbS1rf_9gfaoozlqjBnHT9VT_x3KAWUZeFC7GfZU-1ghFjCkQoNAus8X9tE3UvYS8MjMudRBaOr3NDSdXYhHPysFy1httR9aJykJL8a4QOFHyy44q93PjUEKULHpe0y2rxvFov0tDWIW8PPTNDQz8mYyHip3joRJZ6YeoM3Iiau92Ky25alhSlum0bzN3c2fFaGGwXSGnX_VW-QyypRmqYEXEKcNeBpCyI7JUJtNzNSskaSKCQ-LtENj0I36UmcMI2y3ijIULMr-BBVuknbbNMLp0S_znrV5Vhx9cvT69GeO8YzpXuxmuU1BEx9Xavg8jQ2NeXGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
سعید دقیقی امشب‌ مهمون‌برنامه عادل بود بنده خدا داشت‌راجب‌برادراش‌میگفت‌عادل برگشته میگه خودتم سفید مفیدی؛ عالی بود ببینید
😂
😂
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/23929" target="_blank">📅 22:08 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23928">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/463a3196cd.mp4?token=KlLnSxhFuI0nXmmUCnlF2jdGcBmG99UthOkaGQ6GcK6SZA7vcEOMmHas0lUxDNMp1-C9xUa3d5196oBZthJQ26JOsKAiD3V0WVHL5j0Sw3gqAjpq0VGwK69EIXhi1MqHirPEvyXDs74fHT7aLCz9qUmEWGXGPDgqjrdwyQIP343Sa14YQfuZBLMGyDmLeZhbBRfe9ZiPQWOLxjo9Zz1eMXs9jrEGVFec-IAodUONJYlzyhJyuD22V_9wLMsbh-ZJXWrS_4O6nZPlbOI8UALhhyh1ZcO2Z93MPq4xELCu-WRdI7PMa9Vy2xhjP7WVtjbh-N2H9ekK3DJTSWLPDrLf_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/463a3196cd.mp4?token=KlLnSxhFuI0nXmmUCnlF2jdGcBmG99UthOkaGQ6GcK6SZA7vcEOMmHas0lUxDNMp1-C9xUa3d5196oBZthJQ26JOsKAiD3V0WVHL5j0Sw3gqAjpq0VGwK69EIXhi1MqHirPEvyXDs74fHT7aLCz9qUmEWGXGPDgqjrdwyQIP343Sa14YQfuZBLMGyDmLeZhbBRfe9ZiPQWOLxjo9Zz1eMXs9jrEGVFec-IAodUONJYlzyhJyuD22V_9wLMsbh-ZJXWrS_4O6nZPlbOI8UALhhyh1ZcO2Z93MPq4xELCu-WRdI7PMa9Vy2xhjP7WVtjbh-N2H9ekK3DJTSWLPDrLf_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
این بخش از گفتگو دیشب عادل و اوسمار ویرا تامل برانگیزه؛ زندگی‌سخت و تلخ اوسمار در بچگی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/23928" target="_blank">📅 21:57 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23927">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇳🇴
هوادارای‌نروژ وتشویق‌وایکینگی‌شون‌کف آمریکا؛ چه عشق و حالی‌میکنن، چه تابستونی رو میگذرونن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/23927" target="_blank">📅 21:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23926">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oTbNlf93GsEdhe1E05T-xOvqBiTZhP2zMkPgqWAlt62--uSKsQlawnzkgnavWgQNh_n99qqr-GMzKIfiF4bOVQvLIYpIf2Mr0IPiqQ4GyzXtGKd4_uote1FkqtM2Ls9ZOgc3nFwONAn02qam8bj1FL9fQx0WI3b2ZhjEGn_3FMPEcxidHd9QbD1RJ08PlCG4mLgPAVKXSzjrrlg6TT-GjRw8CXXf74KVNRrsjE6S6SDzrxWS9DOEG14hA5mJ9hV-mHoN4k8OrhnRSYwWbJk4Pe9O4ojqSf-sSID7xMA-bZlt33At6Rgbs51tBaA7HuGqQTP_cOBEqu5ZapUyE5ejhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌اخباردریافتی‌پرشیانا؛دقایقی‌قبل با یکی ازمسئولان‌باشگاه‌پرسپولیس ارتباط گرفتیم که ایشان اعلام‌ کرد بزودی قرارداد اوسمار ویرا با باشگاه فسخ خواهد شد و او فصل بعد درپرسپولیس نخواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/23926" target="_blank">📅 21:36 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23925">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ievfpD2bAvJChl-VVwoQp1VzMBX_dLggXQexyOTG7emhb116uq4wuX2jJeC7ANMkznoTGKAVMA16Z3HrMcxGKLqapWCh86rzRb9RqdmXP9rGsw-8YqWCCCHCxmn4UBTT5d6LzPZWPkzt5QVJ81qmsYyR55TIOucbbY5V8xX5meEWZz7DnNSyVj2jbIJz26S7l5HWXlwk4gZGJ8ZXwP4FT1K3HSEaf0znFaP0s9DZmk3KjN3kgfzsuPvAEQ55yjk0sG3cy7R67GmIOiJUdBsrvM93mhjehzxDP-QG8HWWHHeSzb_wx3Xgp5DQo6ELNuL96NQ9nWKquSN0JxDcAhQsjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🇹🇷
تیم‌ملی فوتبال ترکیه با ترکیب 300 میلیون یورویی و لژیونرای مطرح بادوباخت بدون گل مقابل استرالیا و پاراگوئه از جام جهانی 2026 حذف شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/23925" target="_blank">📅 21:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23924">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">✅
محمدجواد حسین‌نژاد ستاره سابق سپاهان: من خیلی میتونستم به‌تیم‌ملی کمک کنم و خیلی ناراحتم که در جام جهانی حضور ندارم.از لیگ ایران پیشنهاد دارم و احتمالا برای فصل پیش رو برگردم ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/23924" target="_blank">📅 20:28 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23923">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QIUqbbw3b8Ge7Qz1c_5SiwFoTwc1O0cXcywjQahKH3jOrD8XJSJf6_87XMrWamKPa3no9XLtPsy6OEelHNd_YI8Z5ua2aB_UrgHmwR-L1tmv_vf5aCa70k6E9mTjmSZoN-K_2ajxdV0oIddZsHwF83YROIR6H1EmmH4PPVkwUrUaBth1QrkNf3ujNEsfz7LiHcDSnJlPkWwxVBsMp8es3Li0LgNhOXioGE2M2o2Jhqxur-NWEwLPpk_Ew94wgHRuKuY8lckslR33L4udfNRvHE9uoR2FrDN5iUH9UBMl5-MX8HHYj59C1-4aAgtMdmf8y-CqUi4WVSMTDceCDwAzOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ علی نظری جویباری مسئول‌نقل‌وانتقالات استقلال با مدیربرنامه های محمد جواد حسین نژاد مذاکرات خود را شروع کرده تا بعد از باز شدن پنجره این انتقال رو بالاخره بعددوسال نهایی کنه و حسین نژاد آبی‌پوش بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/23923" target="_blank">📅 20:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23922">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c65b32d4ba.mp4?token=mRwcrJU0bYkMjU-Ty8A_Tbg680m4NzHBWU7dDdm6HYDBcW4busBHD5yJUor9-bLfJldbV4EpOt_rh95paM8g4WgvKG8JrvtpJ2KIf_DSdskkxYHYZxJeghO3W4Yb8VjgBCPMrKXcrb3OrABxw-QI2Gs3Ht9BSaNB9oz_SVURrE-E8gI5D7wl3_hFbsZfnScOiuwe3UtThyLyJieZwaq18SWSz7ZAhUYDdz23QIASNm7K2Vc6JAv0pAX9swbBcg0nbg4rh2tVMdy1HOQPjdh9-CiWf8q-kST8l_sD6XB9GRtv-7qFOhzCvry5JBkTyT393Lffpa-6S9kVGx3NN003gRLOk0LeeDAc-8F-I-sG09AfVVffRlN_dy8tSQop_AXcFdyCKlyacvnmR9fWhOnRU8IEgLry468PBt3GJV4EQfL71i4LbdCMLIGrqO7xE4G3CztkgNkPLCJJ_PCN-Hov_qzResTqTjeOq6QSp29YQ9YrZbl5AcVPQBzMowMUPALQBXw-QRkvsuO_IttiFwXBA_bAOFHIFmQ7WpodooJ-tpDzkwlfm7YkzhPnsPSlPUFUOeXxqf2tFMlXWTEBwa2n3U92gB_8ElPnxKcFCoOdYG-nSC0hsCDtFRhV7CSYVg395hlFkpBkNrZXwVFl_IXynHMe_tvOx2zgiLsixUb2xE4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c65b32d4ba.mp4?token=mRwcrJU0bYkMjU-Ty8A_Tbg680m4NzHBWU7dDdm6HYDBcW4busBHD5yJUor9-bLfJldbV4EpOt_rh95paM8g4WgvKG8JrvtpJ2KIf_DSdskkxYHYZxJeghO3W4Yb8VjgBCPMrKXcrb3OrABxw-QI2Gs3Ht9BSaNB9oz_SVURrE-E8gI5D7wl3_hFbsZfnScOiuwe3UtThyLyJieZwaq18SWSz7ZAhUYDdz23QIASNm7K2Vc6JAv0pAX9swbBcg0nbg4rh2tVMdy1HOQPjdh9-CiWf8q-kST8l_sD6XB9GRtv-7qFOhzCvry5JBkTyT393Lffpa-6S9kVGx3NN003gRLOk0LeeDAc-8F-I-sG09AfVVffRlN_dy8tSQop_AXcFdyCKlyacvnmR9fWhOnRU8IEgLry468PBt3GJV4EQfL71i4LbdCMLIGrqO7xE4G3CztkgNkPLCJJ_PCN-Hov_qzResTqTjeOq6QSp29YQ9YrZbl5AcVPQBzMowMUPALQBXw-QRkvsuO_IttiFwXBA_bAOFHIFmQ7WpodooJ-tpDzkwlfm7YkzhPnsPSlPUFUOeXxqf2tFMlXWTEBwa2n3U92gB_8ElPnxKcFCoOdYG-nSC0hsCDtFRhV7CSYVg395hlFkpBkNrZXwVFl_IXynHMe_tvOx2zgiLsixUb2xE4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
‏یسری‌از آمریکایی‌هاازهمچین‌جایی‌شاهد گل دوم تیمشون مقابل استرالیا درهفته‌دوم‌جام جهانی بودن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/23922" target="_blank">📅 19:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23921">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CHpr4mgW-PKaseIhLJh2tNhuPKqMmR-7hLqwfUTwqfGSmBIFcuSRfrMIsklqHuDVCP0XqWgCkFEngZIhj_E4eLQjxR2LVrlkpyIrRQxxgytlPLalGc_UKg4JHqu1q2nd6WqmVQssiAj05Ca6eFt_yLXVT8WirA9rHXdFvq8k5Q_noJHvKW1wqhCdmPGv9Ju3dGa_l-INlCW9-gRk3zS6SIrZ8Do52ftP5r7y6b51jXPrl2zG5sX0jJ1WAM5WbMKN9HKJw1MLv9lhiVx5QO8m2vgA83ABiFTvMCbK-u8ju_eTuljjeb-j90Fq7wPAaoUqT-riIWJJyahnAcfLCzlqRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🟢
طبق شنیده‌های رسانه پرشیانا؛
سید مهدی رحمتی در روزهای اخیر مذاکراتی با مدیران باشگاه پیکان و ذوب آهن داشته و احتمال اینکه با یکی از این‌دو باشگاه قرارداد امضا کنه بسیار زیاد است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/23921" target="_blank">📅 19:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23919">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u1UhRwNdtVQWVNKj3eTBD9TnfqVCmA8_Lw-c4sloFCtEE1UOk-mgLGAYj5GmYiyuEs6uIUffMqElPn5iUi0cCG1vwwijXmDcRU0f1RkLEqBMId6dnS95yXyWaNvDYmv5YBz2GinpquushttyjGBdgWRsBjrjbtYHtVqXLSHicdoX5Wo846ddwcdVzJgVeG0CFqxJDo5CMh3Y2QlP1L6UE_IeIQqhqPepMO-6GheutG6aIxT2wzrtjGzyLFOeH8EhOtO5INDPA-s62tLMk03HA2SwnkuYjvuipm4CZ-g-52gM9eitrmOAI6LJhJVMovp5t7vhpKVVRPlaJjm-tDfXHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DImGqpZ0Amht9nJoF7Bq-TqLErwKFiUfu6d3gmrQH6oCh-Ya0T9oEDbOM8WLm5503LA04U-hziwuHY1_aWRqK41VRGonjVEfpCur6_GyPZ-nQCZSKmrDQcJqtY1N5ezmJqfpZNkPcqaT-npdt8A8UIzMNF4Ui0IeVswjqT0JJOyVxB3S3e-IjKl-hMq_BL-gxXtCO7JMtfEGRg57xjDov9QyfIAo6gCzd5aWrv-0hd_JoFBixtQZTUQhQQbOLESfyfMkRgHkD749fVVaZR-IBaahVekVYZSAigjcnVXyrI6o6LtsGiQrM-B2Qitou9ANnQXCQg-h1OBggeTEJ3kXSA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
هفته‌دوم‌جام‌جهانی 2026
؛ شماتیک ترکیب دو تیم سوئد
🆚
هلند؛ ساعت 20:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23919" target="_blank">📅 19:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23918">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/413165ef88.mp4?token=HDXQ0dGBVa_nnRoOunwHj_iKYm3DQ9vGQhNh48U7qz7H8wpvFmg-ERXQopSx0BGLgHesy0YShr7v5u8ZS0-FjT8asPcpk01CFdH7JZxV5UKTwRZp-WXVlPNsCLqYH5pEMuAOB3iBRMwhMHTQpRIRHcriUCD9X-ailSma-XSDaPLpJYklojIwM6ffLrwivv_pZXujJ-kNGeMz25YpQ4YpVUXa0_Jx1_84uGsvGwp3wWKcbC7YFyuq60X1f3SR_y4RdN7C_p8o2l2a9twn5Lzb8qk1jyEnpNKNxOyeRlRIIAgm-D6ylnVxcdWHyezX2AYbBj1XSbCZNA8Ao9vFufKAn1R0WFCUdzzVwYd6_LPbixerBXMhKVB1WlVzrhQfF6v71k4xGyhjpn-FizuqxqR01YXg4DbvU8YIRFhuMXFMkRXkvoDxRsJ_cEKD5HoeRLjRf1ieOtPsTnlnUCZj5eoHG2WHfTzznjS6ij0hjGrV2N-LWXsW4TbIETk2F1TCe3g5hMImv_Bmqn8-7dAb7pK4nzQB_wLEXSitdkpawa7ZobRhPH0lJOIEaxMTy6y-86W7Z4CjjKIZOhHqVRYHkQjOrr5ImiVschbFpaalsI16SMfdvnxFATIa2xtSfHsVHNpy-B68X3RI2lQLHNtr0QqYfp-ATQRv28dkVgwC_khycqY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/413165ef88.mp4?token=HDXQ0dGBVa_nnRoOunwHj_iKYm3DQ9vGQhNh48U7qz7H8wpvFmg-ERXQopSx0BGLgHesy0YShr7v5u8ZS0-FjT8asPcpk01CFdH7JZxV5UKTwRZp-WXVlPNsCLqYH5pEMuAOB3iBRMwhMHTQpRIRHcriUCD9X-ailSma-XSDaPLpJYklojIwM6ffLrwivv_pZXujJ-kNGeMz25YpQ4YpVUXa0_Jx1_84uGsvGwp3wWKcbC7YFyuq60X1f3SR_y4RdN7C_p8o2l2a9twn5Lzb8qk1jyEnpNKNxOyeRlRIIAgm-D6ylnVxcdWHyezX2AYbBj1XSbCZNA8Ao9vFufKAn1R0WFCUdzzVwYd6_LPbixerBXMhKVB1WlVzrhQfF6v71k4xGyhjpn-FizuqxqR01YXg4DbvU8YIRFhuMXFMkRXkvoDxRsJ_cEKD5HoeRLjRf1ieOtPsTnlnUCZj5eoHG2WHfTzznjS6ij0hjGrV2N-LWXsW4TbIETk2F1TCe3g5hMImv_Bmqn8-7dAb7pK4nzQB_wLEXSitdkpawa7ZobRhPH0lJOIEaxMTy6y-86W7Z4CjjKIZOhHqVRYHkQjOrr5ImiVschbFpaalsI16SMfdvnxFATIa2xtSfHsVHNpy-B68X3RI2lQLHNtr0QqYfp-ATQRv28dkVgwC_khycqY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
یادی کنیم از این صحبت‌های علی دایی عزیز اسطوره مردم ایران درباره رونالدو اسطوره جهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/23918" target="_blank">📅 19:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23916">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UnlBaXeukLB61_IsG6xUEK_Jifz3NlmaFtFV9w8TQCfjhvINn0xZHmIe5P9QCm5NmSG42V2_SxJmdnwlMAKqZO5dQCKR61ondbu_aVvGjplM1mmIazy2DhTt7VTcqyelKuNE1HtKPkkbO7tPM9yYxXb-1kw-kaOljvKNLw4IQ88g4we7zp7RtkJapOLmio96ZPuQgUhs5pUlRli77j5hyCzkRvySsxpDPFcLRYrzjMOAzn4nPfbD7EetRMpV4Ij8Q8J6BRx9hwdKn_IS7hA7BPExnKd2XsgJUDCVUIDrID2M89D9GPQqkIvoCGzHBbyXNBMDN9gpPTN1TAJlUlStPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇪
👤
تیبو کورتوا دروازه‌بان تیم ملی بلژیک: تیم ایران یک مدافع راست‌خطرناک و گلزن به نام رامین رضاییان دارند که زیاد در حملات تیم شرکت می‌کند و ارسال‌های‌دقیقی‌انجام میده بایدمراقبش‌باشیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/23916" target="_blank">📅 19:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23915">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iSS2PWkrpVVVylJWXlNsj4Pn27gAoOja-anUIofeKO1ZVdkpQwkqlFQeOeiLjmV3gCDrjxlXCErltIrlS3cb_8V7iZiv5ayiW_TILSo35dfWDK-svNHANb8xM7Jdw4emTJnXetnBCEmT-h2sdWgRbhLOYQr0yhafAy2zM63YHpW2mI_xKtepwk5V62bhU5pSHCxqA9SBq_GU262U8uhM9_QKYPBdDYNylMs_fTZnFA3QlCLUi22GHmpMEo2qcawQXWVpizdbqBWe3n-Arz5WPxmN-l_woy4lZVDlFk4NagrDG3RYG1stZ_rDqVTyV3r9DLpZRq2ApSw6JrD3NAXrFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پیش‌بینی اپتا از نتیجه بازی ایران و بلژیک
‼️
سایت‌اپتابراساس۱۰۰۰۰شبیه‌سازی‌نتیجه‌بازی ایران - بلژیک را پیش‌بینی‌کرده که درآن شانس برد شاگردان قلعه نویی ۱۵.۱ درصد است.  در این پیش‌بینی شانس برد بلژیک ۶۶ درصد و تساوی ۱۸.۹ درصد است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/23915" target="_blank">📅 18:55 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23913">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/602d7756fa.mp4?token=kyxLwWbocAILsx00XAwwYKePd8MAKdem1UryOpRCMqacmpoSCtAPU2r6K-Hhex3RCleKpMMMXIdUjk5rkG0F1AyG3HPWg2ADgfCl9jfGTYzHA4GIEjlaYXdwnH-WbbSy1IyDopwHfN2pftB5zlLpWPUlBGKxo6Wg9xKkis4ow99Jmh2sxISbch9TPQnFZhCI8SnE9O0SY6dN95rCKKyD0AGndYvEpkKexPdUoVmq4ozLZJPj0SsOvR3lcJax3mbwCF4EUooYhtcw6WdX7qR-IY7TT7mz1Wldra3fR_o1haIbgtXskfLP5SSiAhF0VxHFeGsP-w2KK67jRDHRSKvcHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/602d7756fa.mp4?token=kyxLwWbocAILsx00XAwwYKePd8MAKdem1UryOpRCMqacmpoSCtAPU2r6K-Hhex3RCleKpMMMXIdUjk5rkG0F1AyG3HPWg2ADgfCl9jfGTYzHA4GIEjlaYXdwnH-WbbSy1IyDopwHfN2pftB5zlLpWPUlBGKxo6Wg9xKkis4ow99Jmh2sxISbch9TPQnFZhCI8SnE9O0SY6dN95rCKKyD0AGndYvEpkKexPdUoVmq4ozLZJPj0SsOvR3lcJax3mbwCF4EUooYhtcw6WdX7qR-IY7TT7mz1Wldra3fR_o1haIbgtXskfLP5SSiAhF0VxHFeGsP-w2KK67jRDHRSKvcHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اخراج‌المیرون‌ بخاطرتوهین به ترک‌ها:
آلمیرون بازیکن پاراگوئه به‌دلیل توهین‌قومی به بازیکن ترکیه اخراج شد! تو قانون‌ جدید اگر دست‌جلوی‌دهان بیاد و مشکل پیش‌بیاد بازیکن اخراج خواهد شد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/23913" target="_blank">📅 16:36 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23912">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94a793ad17.mp4?token=eyXzfHQlWJyb4zTv_hYnO2k9ZW_aX1yDR7bR4fQs0UDXNbCZV7JPXv2Z0qArQBzgDoUpgTzbWe2GqZ0iuKwPuuuRN0az_JRotIZLM7EeJtREKtEeuOnxZb6i3ikqju9jJmNxy0iIiIlntCK4dHw1TgpXwIM3URyPXjETZQv-piYfhYu5nRWqy20H8dqJS0DdGXxrjtwkDbPr5gSgnJUSP22c77qmbBXK6CIHNBQ53zqSE1_oBFLPtCyX4aE7wvlc-NWvSiV5wu0HuISKRd1kjlXlAZ8nkvDcMkT0yA6UEKe0pWASDsaNEhVjIoQSQ-sCetzIBUOYkDuv8A61vaEOwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94a793ad17.mp4?token=eyXzfHQlWJyb4zTv_hYnO2k9ZW_aX1yDR7bR4fQs0UDXNbCZV7JPXv2Z0qArQBzgDoUpgTzbWe2GqZ0iuKwPuuuRN0az_JRotIZLM7EeJtREKtEeuOnxZb6i3ikqju9jJmNxy0iIiIlntCK4dHw1TgpXwIM3URyPXjETZQv-piYfhYu5nRWqy20H8dqJS0DdGXxrjtwkDbPr5gSgnJUSP22c77qmbBXK6CIHNBQ53zqSE1_oBFLPtCyX4aE7wvlc-NWvSiV5wu0HuISKRd1kjlXlAZ8nkvDcMkT0yA6UEKe0pWASDsaNEhVjIoQSQ-sCetzIBUOYkDuv8A61vaEOwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
گرفتگی یهویی عضلات پای عادل در ویژه برنامه پریشب جام جهانی؛ سه تایی غش کردند از خنده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/23912" target="_blank">📅 16:17 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23911">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r-gbLOJQtgzP7SzqOYxXlYxsLGGDQm-B8tyn_oM1qpwMM14pxpco7XWZMFkhlhqQuyJmUzCsjzP6-gkUDPgG6VZd8JVhmUfU84zxV7aOPqNBcswj0xT6ZhlgsU87vMBJNedDnhbvOELJ9COrmBJNl6BgNjIPG2pMBr3R0-6C1BmexESqq2FgfPuothRPpOu_iaG94ITg71FokBXUP-ZmwcfKWFG9GPzjdRFRwCZPysvQ9p85_L_GygggIIVwXzEBklvVJxQMWtRU13Q0QEugNxZYPKbKY4DM64SOsb0YJc0Bsa7tHXZnVZChq5o2026RZsTO6ceTcOEY9TZaYDnrRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هوادارای خارجی رونالدو بخاطر مصاحبه ژائو نوس که گفته بود کریس‌رونالدو برای‌ما فرقی با بقیه بازیکنانداره‌وبهترین‌بازیکن‌فصل پیش لیگ عربستان هم فلیکس بوده ریختن تو پیج دوست دخترش:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/23911" target="_blank">📅 15:54 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23910">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NQb1ux451UeaF44oXZhfAvaqu5J_nX6FiIn1H1wnsBQujHCexHeNzV0TeSGky2a0BtKAeT3T0xjTCisRZ1BXC4oIqo_fbSVvziITlVb3w9GCqoRARYR3ZJnMYdOk8Uk62OulUGgCdpFm8e2KloFDq176ArxwOYxo6n4d9hMOJPyA77P9kx0L-K4FX5iZSeU2D2UlOYfTI1d_Zsx52FPt1VcbQVJf8o-dCoGgSquaUV9S7iuZbOr_tEcgo5GzevygpQvJhX6OyZjqcbw7NL1oS9XG7bihjemD_SVXUeg2ieoinXK-s4MvNL9opve6LweqR0ZAHPn3p4FbuGWjPBUtWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ علاوه بر امید عالیشاه و مرتضی پور علی گنجی، سروش رفیعی دیگر بازیکنی است که در پایان فصل قطعا از جمع سرخ پوشان پایتخت جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/23910" target="_blank">📅 15:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23908">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d95ab0dfbb.mp4?token=X0UWFBrUIZ4fe7zNndlybKTpnNZnUb_AYIYf_yrqPRu3g8n51yl-PaEUJ0-imfDxqCoxJc4SwD9k32kPCO_tPCxldhXxxKSC1FLtP5Gfte4ETRKhZPDgEfMndtwxuoqYSIimp4rYpc0Xj5Tm6W2kxLjPlfpTDNcFFEcMxHWr3cySCZcaxgn4OlM_AdSbQ7DMl_4rPhMYjAtyyJ4uM2Ql5N9-U_etdO4DjWqpJ7r4lTMNeNDcrpLjxahPjCAopKOEvnfkmarU3CAY0iFuxkBCOEWjMTJEPBT9si6JqFpA8AO8FGcrHOJulz44GrCeQiBcVhM6V4dunekZEs_kxWnH0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d95ab0dfbb.mp4?token=X0UWFBrUIZ4fe7zNndlybKTpnNZnUb_AYIYf_yrqPRu3g8n51yl-PaEUJ0-imfDxqCoxJc4SwD9k32kPCO_tPCxldhXxxKSC1FLtP5Gfte4ETRKhZPDgEfMndtwxuoqYSIimp4rYpc0Xj5Tm6W2kxLjPlfpTDNcFFEcMxHWr3cySCZcaxgn4OlM_AdSbQ7DMl_4rPhMYjAtyyJ4uM2Ql5N9-U_etdO4DjWqpJ7r4lTMNeNDcrpLjxahPjCAopKOEvnfkmarU3CAY0iFuxkBCOEWjMTJEPBT9si6JqFpA8AO8FGcrHOJulz44GrCeQiBcVhM6V4dunekZEs_kxWnH0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ لحظه ماچ کردن خبرنگار کره‌ای توسط یه‌خبرنگارمکزیکی؛ حالا خبرنگاره اگه ایرانی میبود تا از خانومه لب نمیگرفت ول نمیکرد! این خجالتی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/23908" target="_blank">📅 15:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23907">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rrm6ko7rKHOGOGECXwKErO2EzkTIBRwrVyyVkQaouZ4XpOuyU6kFNo6J9qoFU3B8ZZA0mr0ZPkRhpzSZAMDKHS1rFjYd0QhVI0GtZR6mXYASBI2BuB6GhOHzlBm5-n3h0-w0du1XP_CeG1c1LfuTf-tGMekS4hGluCUfOqbSWB15w8Z4l0ouLMZCx-cU9n4SKm0Kn-Uokv9UjAQiTQH06LOqW_TXWph7acs7J0Z2_Zjw88Gww4FKBOQc27r6Y12Kjen2eZPEA4OGACuFrcFY9wAfe7GBlUjbdKuCXUMdrqblJ2mJgwtGzCJ_tS5IN5bOynI5a6XmMOqzUXJ5CrgH0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جرمی دوکو ستاره بلژیک بخاطر زایمان همسرش و متولد شدن فرزندش اردوی تیم ملی بلژیک رو ترک کرده و ممکنه به بازی فرداشب با تیم ایران نرسه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/23907" target="_blank">📅 15:23 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23906">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OCnauG0pKI91InivKSLVZKcAM0cwMmGvxJoya_5E2JXZdTiL06p8aQWWcXpYzo-Zc9TwMjVQBPfUcLDA0-spI7K9BaUzxNHzsNcz9w8wfIX2ErWm0cCfyzBuEoLlxobz-J_fR1_ds7uMpDRbL3CdTrF5gPv12angb5EYlQ9vLFFbIejfNMcvoSaEoDF0wz9ORVkjIaRYA0Tc-u_2fDf42BqEL9MARIlhQVZ5zwnxtnNxjmzDARMr3FjF2b_pxE7RbjBlKCaCvrguh0-IaDIe2-c-SLnBUZOcFz8oUhsabCWybZVi-ttRAU2pehKuM328g5Npe9ysVS89JkSJ_aOwyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ طبق اخبار دریافتی پرشیانا؛ محمد دانشگر مدافع 32ساله سپاهان بعد از جدایی از این تیم از طریق یک‌مدیربرنامه که رابطه نزدیکی با علی تاجرنیا داره خودش رو به استقلال پیشنهاد داده و گفته حاضره به جمه آبی پوشان پایتخت برگرده.
‼️
محمد دانشگر تابستون سال‌قبلم…</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/23906" target="_blank">📅 15:16 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23905">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j-ThCIT2vsLXgyRENF_kFUP6c15YK9V5LGqxL9eVHrIs1CB47b1xcH_bjsxYLlgOQJ9KDjm2nuiV3I5DkUvJ_IgfCIxhZauxxl4u4SIKOgCJXfJMEcdFJFgmNhYoNTaBcjW2t1AM-a8KOh9iG2oIxUalzLA7qdsorK7bpuTtavbWt0tZz7YCbQbtxr0E_dJbxcGwCXq0wGmE4LdVzOXGrIodxPHWFlkjL9VHkejx_63L-0QXl28uSFyFU7oCxS4mNtBpTBhLFZ3qdzOuf3Dee5myl2ZUEoDSY7fylxWb4G4iqtaHrQ5rRLg8Hgel3MU-J8jsKdEujKIEhIqy9PnfKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کاسمیرو ستاره‌خط‌هافبک تیم‌ملی برزیل و سابق رئال‌مادرید و منچستریونایتد برای‌عقد قرار دادی دو ساله با باشگاه اینترمیامی به توافق نهایی رسید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/23905" target="_blank">📅 15:08 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23904">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UH0KDbV1zju4pAjHPLFB161sUpbEwofTLWuH20a2hUL5HB4cgG2CnTTyj0lAUA0-5XgNrkqDNfh00Ae8Epv1SM33ke2cmRO0CBCQMh-ojxqAUBXmBBelUPf7ukUwKXPZfa-5GdOQIyJJBw5QEyBSE2-pO21Op48UMEbSx7SBRYbPrJprDSdL8guxhYhVUuvwYaHjN7RMbccL5OoPh0GJKSbMV9YE8R4MFbPkN2n1tvemXx57a73BSchpH6NXzAaFtF2JgsFgZwwVmqop8zOyggKMv4t1SXndK4ESGC3yAtvA2EDGdr1GHJDsiuqwzMY1gHvyz5O-jkgGNYQr5Qn9Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ویژه برنامه پیمان یوسفی برای جام جهانی بدلیل این که علی فتح الله زاده به میثاقی مجری سبکه سه تیکه انداخت متوقف شد و به او اعلام شده که دیگر حق ادامه تولید این برنامه رو نداره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/23904" target="_blank">📅 14:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23903">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50f475cbb4.mp4?token=ttslkvEZl8jyz5xKiET5iXjs2-OgO4m4bli7B_6dF53Zy1zih6TVewGO4x-pBfNPVHsLPZgvdKz0rcnckJT2DVSCQo7eQf0jnUPdBUzYOegUxCOS4RKkWxCN6OakoLkxuBllggifESt2aul5BwzWV_Xopbj3a8Y9Kj-AgtPH4B_wihzcZByOCK-vq4h9hPB_kWxrFPxAtlFLqqBjRcEafnTXtWxMRNaoDXwNrybZyhsarLP6M1CD9egujrFSqtN4kmN7CSi-8L8RVY_Dnedm9CA97G2CXEhGX-SOY4nsjPIh9Nug__VinGyyPRbMG_jklMB1yXC883waS6ytlpH0lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50f475cbb4.mp4?token=ttslkvEZl8jyz5xKiET5iXjs2-OgO4m4bli7B_6dF53Zy1zih6TVewGO4x-pBfNPVHsLPZgvdKz0rcnckJT2DVSCQo7eQf0jnUPdBUzYOegUxCOS4RKkWxCN6OakoLkxuBllggifESt2aul5BwzWV_Xopbj3a8Y9Kj-AgtPH4B_wihzcZByOCK-vq4h9hPB_kWxrFPxAtlFLqqBjRcEafnTXtWxMRNaoDXwNrybZyhsarLP6M1CD9egujrFSqtN4kmN7CSi-8L8RVY_Dnedm9CA97G2CXEhGX-SOY4nsjPIh9Nug__VinGyyPRbMG_jklMB1yXC883waS6ytlpH0lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
عادل فردوسی پور:
یه زمانی من و محرم خیلی بدمون ازهم میومد ولی الان من خیلی دوسش دارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/23903" target="_blank">📅 14:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23902">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WHc38-2ccGyiUiE_Ib-bhza3V4s5wki-AqaXT2xOPw1h4qK0ZgG_75xVJXfaJ6FkY7eTB5ZeGfvsoaYZro8c5P7zj-3tzlklyv0pXDmgZcW9dMMm4Jfb_mspi7B1LE1GO882HXQDm3afBqa0uTP6DoLM8vWiMTD0wTgn2vAYYRdjnZeWfl66pQk7VGdcJn09c2_skVEgAq4mVLLGExgb-T9mg3n0DLnM8N2z1IBR0a7d8SqTCSVApBjYF8O__Vb8yyDcKdIxZRpNa0jrKzP1Vh-NZ9m1LIHHvOMKMIENYv7GAB6AZ_SfpxuO5PuIwVbW62TSQdczle0gnjBP8Lgdhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ طبق اخبار دریافتی پرشیانا؛ محمد دانشگر مدافع 32ساله سپاهان بعد از جدایی از این تیم از طریق یک‌مدیربرنامه که رابطه نزدیکی با علی تاجرنیا داره خودش رو به استقلال پیشنهاد داده و گفته حاضره به جمه آبی پوشان پایتخت برگرده.
‼️
محمد دانشگر تابستون سال‌قبلم…</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/23902" target="_blank">📅 14:27 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23901">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J4VjZ_ZUsQClpXl8WVArCHIU-kIurpdNG3lNHM84_pklUqAjSGEzTBg8uD87uhlgxanebHMkmrAOptx-5ucJyW8M-ydG7jBdlmNr7DjEkVa_oiO3sRc7-DWPUGIQgHIwz_5DoxDCWPcTLfjA0a0ycrXMXJFkF_dLo--bnon4cDdXocqaYucoHnepXKi8mKldRhnJsHiwjgFP7-zzjLt-P7BGHOLAlvXIK9Y35-BxK-SndpvDMl6S0159GBZ3jP4hFZgznrZR69OjHftC3fRZCgp2Mzf1ln2TcOd4_NEtQT0Fk567VzHuAgV05rCWnRGIzwFMDjF9eeL4WWYcQ2Ow2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
عملکردشاهکار ارلینگ‌هالند در لیگ‌ها و تورنمنت‌ هایی که تا امروز بازی کرده: 279 بازی و 260 گل!
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/23901" target="_blank">📅 14:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23900">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/utqrUjlfJwBgqBeQjPnEE_htVZ7IAQzrYiH5RXKman8H_svu7j4Bpx0qvAruLYC-FELwzcJ6ggbQsOB6juZDdNx_HPXsOYeMFz39yv-c8AEG92OxyAo1jtQoFDKvB2IVj9s2QsR3ToPVpzn8jwcS7TjCBvSLwQEbqO5ElJvzdVOpfYqtK_BlOHA8qd7F_H_C-tUfSGPZRaxC65yRSYpgqHgnmweNtwK2wFFqUcZHsUK9qoh5UMLn5W30qp-m8xhHVN9Y-kO8SpYh35_5E6M5I-L4Q2w-niZVYvDg1WOFI0oa1aNvsWPsTZuUd0kF3ZtnNCZFJCEB1Y79dPSgLf5NeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌فدراسیون‌فوتبال؛ سهمیه خارجی باشگاه‌ های لیگ برتر درفصل جدید چهار عدد خواهد بود که یکیشون حتما باید آسیایی باشه. به این شکل 3+1.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/23900" target="_blank">📅 13:56 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23899">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UPMNIufNXJpYwffBCayBBW_WR0fezyQYYQ47-54OW9ueMHCQBY-GUoz_b8cavCiPRILpZflhaUtJGkWMRYljd1ZcHZqFP9DTPTA2CjM58YfgTxkxCuBdxHzcQTI1lQSP_WAmvhxPWVXchOZYB9m0l721X3tkFaWtTpY4Kd4Yxv4X3cS9YNmifmn0eLKELq5gOhn9psZMgY28iAHaYVBa_aU8SSee1zzERyyi3NQVzamOOuvuFmt9Xj-W0rg7-4n8V0nTR99veIxIZq7Lae-0a1acy74gqGInuZeVY1xHCK9ZYliu5mgTFeLGWy53Fk56M_orR5J-kRN4jpeKuW5B1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی تاج رئیس فدراسیون در اردیبهشت قصد داشت استقلال رو بعنوان قهرمان این فصل رقابت‌ها انتخاب کنه و حتی‌به‌مدیران این باشگاه این موضوع اطلاع داد اما بعدِ تماس مدیران باشگاه پرسپولیس با مسعود پزشکیان و بادستوررئیس‌جمهور تاج از انتشار این خبر خودداری‌کرد.…</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/23899" target="_blank">📅 13:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23898">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d55cf4416c.mp4?token=C9pazTwaKSlN5UCpyIlLKhnVbJddt55ZRKLk0KizxQye8mdLr0fWsWZskv24WcOD7K4gvgju-VJibVHx5dSZs75UyCZ3xQUwXiogZ7HR4Z6opufHoIEXgwQiwYXk4jarCzEUzDCNkPf2llgMI7neT_EN1vAeFKXEEyz6jE16_fK_t3GHhxUAyQ2L21_SPWqC3dPMSB84ETyNkwDC7caVkneMChFfYYEF4v1ls6Mp8GyDQwWxkk745iq7sHTKGf-y52YUjxCvxooXmGLJcGZwhTyNGpXYzSrwc0oLv4ZsdHX-ZxCLDT_530tv7cEu4T8fu8wC2Q4U4WzZ1XvM47XCnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d55cf4416c.mp4?token=C9pazTwaKSlN5UCpyIlLKhnVbJddt55ZRKLk0KizxQye8mdLr0fWsWZskv24WcOD7K4gvgju-VJibVHx5dSZs75UyCZ3xQUwXiogZ7HR4Z6opufHoIEXgwQiwYXk4jarCzEUzDCNkPf2llgMI7neT_EN1vAeFKXEEyz6jE16_fK_t3GHhxUAyQ2L21_SPWqC3dPMSB84ETyNkwDC7caVkneMChFfYYEF4v1ls6Mp8GyDQwWxkk745iq7sHTKGf-y52YUjxCvxooXmGLJcGZwhTyNGpXYzSrwc0oLv4ZsdHX-ZxCLDT_530tv7cEu4T8fu8wC2Q4U4WzZ1XvM47XCnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لوکاس برگوال ستاره تاتنهام به سرعت داره به یکی از مطرح‌ترین ستاره‌های فوتبال تبدیل میشه. این هافبک سوئدی‌که ۲۰ سال سن داره نه تنها بخاطر ورزش حرفه‌ای تو جام جهانی ۲۰۲۶ آمریکا معروف شده بلکه به خاطر صورت زیباش هم وایرال شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/23898" target="_blank">📅 13:41 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23897">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8cf4e4f15.mp4?token=bDH2ZTYaFD2c2i9LBAS0jXZes6qk-lGm_fjKMyRDe1HwoqB8tGuIoholnBMkfeFQkNG3vMLLSyv9SQNgUozclBTmvVKZDAZYB6Pzok8Z4y03JOLk20rfAh7Q1CYy6nvwsl95riQjbFiFYzhHjWV0tC0eF8rFrkSQ54hwLrYtKgOla8RIqyfI0MxoJ7uhTcavRCDxnvPPPcoAOWVv_HBtP74t8e7OriGNUPO_jOL_dNOYexxkdI7GKA8nLYIJeUszD4qXqJaGsz5IkV7m4kKFy3jmmqQTP75yFmnzWbHRSNetiS-e6hmpqarbQT4t5VrNS7wajv5Q0p39gLRE_UlzYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8cf4e4f15.mp4?token=bDH2ZTYaFD2c2i9LBAS0jXZes6qk-lGm_fjKMyRDe1HwoqB8tGuIoholnBMkfeFQkNG3vMLLSyv9SQNgUozclBTmvVKZDAZYB6Pzok8Z4y03JOLk20rfAh7Q1CYy6nvwsl95riQjbFiFYzhHjWV0tC0eF8rFrkSQ54hwLrYtKgOla8RIqyfI0MxoJ7uhTcavRCDxnvPPPcoAOWVv_HBtP74t8e7OriGNUPO_jOL_dNOYexxkdI7GKA8nLYIJeUszD4qXqJaGsz5IkV7m4kKFy3jmmqQTP75yFmnzWbHRSNetiS-e6hmpqarbQT4t5VrNS7wajv5Q0p39gLRE_UlzYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خداداد عزیزی مهمون ویژه برنامه جام جهانی یه لحظه از دست جواد خیابانی عصبی شد پا شد زد تو سر خودش و نشست گفت من استعفا میدم.
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/23897" target="_blank">📅 13:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23896">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yilv3ALR2pY5rsJwWYrEgMD9bjs5MWbccG-8-7h_H_PbmyLWQSyIbTuaqJL14ENp4Y_dPFkoiz0eTNuZCJ-rV6lEhCEsDgKJp15U64yNwrGRKv2RXnwbaRWjem3yXngfuCdI3RsafopS1JA14g1kNFuG2H8GFt-ZyAed2_rZ3iNPZ-JDsduGKCM-mw_FogAroLfgespwKzu_Ypy0KeE2PoO1cRVBgZ0J3VmITfUfTrhLGJxY_BaMJQdX0N_KxqkQgRPMS-mDz4HY99Lhwn3dwCCS7EKDuKO3kZ_-_t0-hhTHigyflnC0oghPQGkM3FWXk33YciXMcuKo08FG_KSq4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول گروه C رقابت های جام جهانی در پایان هفته دوم؛ برزیل سه هیچ هائیتی رو برد و مراکش هم‌با یک گل از سد اسکاتلند گذشت. بازی های هفته اخر بسیار جذاب، مهیج و تماشایی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/23896" target="_blank">📅 12:59 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23895">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aIgxL17aZFzy4YvDG0FoOLpJezY1zOnYebhwr3E--gxAC8IZa1ndyvbdieaSjKLdrEF_BatnIcK12NGCTYUW7tFungRvVhM_DlcAhxn2FXgZCgUXraLdFo6hD5gNFgtvtu9pAH2wENB0kcuFR36wR6bCjBiJWwG0SwDbYJjAsbljstmlI1FQiJ0RC9CYfaxcnvIdR2l_8fsx2mXkVxypfEc_luGMTM1Cc3C6qOwwo7H11WD2j_WW3ZlB4pAQJvEvq-GvuMRnzaRjGKfpgDSS2fF82BiHW95k2zP3BmfkvvgP9DIHb0hsxjtV5CvqpI-go5NgvcRSN4SkcTslSOWVDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دقیقا 19 روزپیش؛ صبح 21 اردیبهشت؛ مهدی تاج با تاجرنیا رئیس‌هیات‌مدیره‌استقلال تماس گرفت و به او گفته بود که فدراسیون به این نتیجه رسیده که امکان برگزاری لیگ وجود نداره و بزودی استقلال رو بعنوان قهرمان لیگ معرفی میکنیم اما تماس‌های اخیر حدادی مدیرعامل باشگاه…</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/23895" target="_blank">📅 12:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23894">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b18c6a9792.mp4?token=DHlFd_PVuOwMmOkRKyk5ObGhzugtOvdp7lGXo4bamkwZdXxXXFReErR3RtTD2EXtKAyvlV48tMBy7lngMLNK8XOtv37ZXN_lF9DX-nE62TdbiWVWv6Dte3ifdLtV9BBxkBMGKrKnTinqmQtiEEqGQieFEVgFioclQ7yfEMaZ6w71n4lztN8sbUQVcePwOJmhu3-EO7RYZwtWjqwiL6MqVPNBwelI6pIlX2mGYvpXFtcBeqINQDT6nBYjEHEjMNXZ7W3Y5EbWxcXdNGrIJLiX_xCRiLFx_cWJSMrtH7gcCWBj8bGeIfWcpEmGIFlU6R5vPcIce2dWsuj8RHpjz63td1veuF7EWfy7A7A1NBX_UUNGEhpcmbdlHZf-2JL-40HIZTtR2sDRj7E14vUdL0SLVOMBCBbED6pfp3Hy3tSCPpdD7B740FeGFtYdJ24ox2riiyMGcO8yNNKkwnQvghj0Lu6_zBuQ3HsNbvnDA_9rW_bLDQS2WJjQbsHESsLHDKoWIN_co2Q_QsNqi9gCAjbAFcL9b2P1NlhNcGBV_VpW_8NWuyi1MPDtc0Z3xNoHabWQhW06B_ZyVZwcipgBp9Dj7Km3X5Z-ThPv_qm_N8w3MVFI_sqRDc29JTWuHVEaIlw8NhXbQLZsf_5z0isdErjReJmhlUkTuN_9Fx6ITmlqcLc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b18c6a9792.mp4?token=DHlFd_PVuOwMmOkRKyk5ObGhzugtOvdp7lGXo4bamkwZdXxXXFReErR3RtTD2EXtKAyvlV48tMBy7lngMLNK8XOtv37ZXN_lF9DX-nE62TdbiWVWv6Dte3ifdLtV9BBxkBMGKrKnTinqmQtiEEqGQieFEVgFioclQ7yfEMaZ6w71n4lztN8sbUQVcePwOJmhu3-EO7RYZwtWjqwiL6MqVPNBwelI6pIlX2mGYvpXFtcBeqINQDT6nBYjEHEjMNXZ7W3Y5EbWxcXdNGrIJLiX_xCRiLFx_cWJSMrtH7gcCWBj8bGeIfWcpEmGIFlU6R5vPcIce2dWsuj8RHpjz63td1veuF7EWfy7A7A1NBX_UUNGEhpcmbdlHZf-2JL-40HIZTtR2sDRj7E14vUdL0SLVOMBCBbED6pfp3Hy3tSCPpdD7B740FeGFtYdJ24ox2riiyMGcO8yNNKkwnQvghj0Lu6_zBuQ3HsNbvnDA_9rW_bLDQS2WJjQbsHESsLHDKoWIN_co2Q_QsNqi9gCAjbAFcL9b2P1NlhNcGBV_VpW_8NWuyi1MPDtc0Z3xNoHabWQhW06B_ZyVZwcipgBp9Dj7Km3X5Z-ThPv_qm_N8w3MVFI_sqRDc29JTWuHVEaIlw8NhXbQLZsf_5z0isdErjReJmhlUkTuN_9Fx6ITmlqcLc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
گلچینی از صحبت‌های جواد خیابانی در گفتگو با امیر حسین قیاسی؛ مجری برنامه هنگ کرد قشنگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/23894" target="_blank">📅 12:27 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23893">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W4lWnCLa6KfXpg11OcqlzxW-gNgbtHRCub-rE5GVz-cFI5GrtNK5cziidCZsyeNWKhkj6asBZAUZaYkap_E7WXSajcuNleFQQ8qoTSwCb1rJPwsGb1WiksrGFvfxL7orDT1kxs8drGaRsG90zsLqS26k28ujr07FBjcRQib1BbLzEvsgh3aHqYVFENgTsyoDdFa1En6oc_ZJbNhwxvzfA7U_MSe8DFgQ6WCwo5zoZu1kEYqzQxQpuXk4Y_e58c2bhai5hZheRw153KhS13bbJIRDEPbhl3T9wxzrGIW-pYEY1EN8etAQTpQVJUITZXaPg_bJdcNKQu4l8AA2huSjaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا؛ به احتمال فراوان فصل اینده رقابت‌های لیگ برتر 18 تیمی خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/23893" target="_blank">📅 12:08 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23892">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QZ64yXmx-94XSKNKPqIlqL5kvrP0QCtQ4UXBk3Dp-_Cpp-VTjYyk3aD586vvMGyZztRfk_ldaBjxPAa7WvXFnuElCVg-DnHanyImIG9byxeLmk3hGuINCUBop2vppW0VVZVToBCA0ZiSxh_KP1IG9cIa5fA-CgFvhZkTEOlnPSoPBXozaWDIKzcv6A4RsiCZG_4Z2j3BTLF3y2jHi50Q-oCEpK5jUBTb7UBCrw1M0BkGSZULya3ra94arTXajYKhUHhVPvi7x8HIOfZa9PSfbWML6ItmXyvSygLMC31-StMDEar9TokFM3YU8FL_qqN43qB-vF-MA8rdh_8dm9PMfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق آخرین اخبار دریافتی پرشیانا؛ دراگان اسکوچیچ ظرف 72 ساااعت آینده به تهران خواهد آمد تا مذاکرات نهایی رو حضوری با مدیران باشگاه پرسپولیس داشته باشد. هیچ چیزی قطعی نشده. اوسمار 50 درصدشانس داره. اسکوم 50 درصد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/23892" target="_blank">📅 11:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23891">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0ae405613.mp4?token=r7BwbHJlnKNAU5dTcjN7l54fQWtsqVOSn0L2idMnpadb0E6qBWq2rcGrTMzHSXeAGXwlOhJq5iQ9nh6vqPVkdG3SK6LgtqrwX6VCo6GDmsoNFnEL7Gqza4H4-wGzS7rJj1BPfxEZVlR8wAvyC23wAOt-uOUTfCgkDh7R8KcSilHN-TfwjTCcgpzP8V-atRavbBnRrP4kXWZMBNGA_ZsO2xaOyfWlJhcRgl7H_t6QIyWZfwxFYtEFywreLYmiTRoQVZA5xb5AZ1sacSt89ItdoTS9RClUEfmjUq79q0CwIl1A5DI_JgGXFUnGULQbPyl66GCez0WkdxBGIA3JFtnp-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0ae405613.mp4?token=r7BwbHJlnKNAU5dTcjN7l54fQWtsqVOSn0L2idMnpadb0E6qBWq2rcGrTMzHSXeAGXwlOhJq5iQ9nh6vqPVkdG3SK6LgtqrwX6VCo6GDmsoNFnEL7Gqza4H4-wGzS7rJj1BPfxEZVlR8wAvyC23wAOt-uOUTfCgkDh7R8KcSilHN-TfwjTCcgpzP8V-atRavbBnRrP4kXWZMBNGA_ZsO2xaOyfWlJhcRgl7H_t6QIyWZfwxFYtEFywreLYmiTRoQVZA5xb5AZ1sacSt89ItdoTS9RClUEfmjUq79q0CwIl1A5DI_JgGXFUnGULQbPyl66GCez0WkdxBGIA3JFtnp-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
👤
واکنش‌طرفداران تیم‌ملی فرانسه وقتی بعد چک کردن وار فکر کردن علیرضا فغانی براشون تو بازی مقابل تیم ملی سنگال پنالتی گرفته ولی...
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/23891" target="_blank">📅 11:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23890">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FC67rttLy4QUI1ezMqo-bHefRdZ9DygmmlZHP4pXBwnnr5dPaNQ1aDwlTuMHIpxQBppw_sweE7uZI_rXmhVZRxAGAIqBDFqfaBjsf5OjdcgG6i00-1JhBcHBeeL2VdeJXdBwGpkx1ysIJmYA4H-3qJg9bcoVQfAiB4ixLx9-leBncTsyHGU2Dn-h3zP2JZziiOZmtDtWM8IxRtRkfw6pt1AMRinue2Brs0tz_S3uLDpuaDWwbl5nhz77o1su2En6zPB5RyXGPjw6vL0GN_bhILWmSXOBciZp0KEunI3ZZ8FFfjNy8kFfXPaP--ptfgYf2ckZOX_psWKPn0QGYvONBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
👤
بااعلام‌فابریزیورومانو؛نیمارجونیور ستاره برزیل که به دلیل مصدومیت دیدار با مراکش رو از دست داده بود حالا در حال ریکاوریه اما ‌کادر فنی نخواسته روش ریسک کنه و او رو برای دیدار مقابل تیم ملی هائیتی خط زده که به آمادگی کامل برسه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/23890" target="_blank">📅 11:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23889">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f8eb0d50c.mp4?token=AsjWYqskQ2n9kroLHLxKRcU908TxC-ueHNF0XSlYo3ciVT_RKCaDg2NvYqScusS-Rq3UV8i4OF2FtNNhidz4aVYWl13R41OIKTJ-m6HjQRPij0IEDz178FcQrJlchIcmi_SeT-u0LqD1BSR-het8DyunyKyRCU7i9acrGB2yFemrf3YT0M7WbicTdnBQ8XN64yAYy8lv66LRj7ypKZJW2VXq14J49svPfjIBlYBNVXWfdskvaN86IjpLCInJis2PWavzjH8-frnyywZEyqr_obzZ9e0edcn9sN5BvDjav4oVHzcETGGrEnEVbb-71zTGQGAEI-fIe6Jmj7BWZvwVvjxC7ufMtG4P1N4Ew1wMiJkTt9szL8H9EFrjE-KDsZT4fDhaW9FvLcKs9B7q2FQNT9w1vYqlyjBkOajm71Ipe2XptoxNSWEJ34LRg5UiS8ZPYTxcPzOmEAxM3UitZat-NRsBvpZKvlKD83gSRQ6Yz3lPjOciQaIMxdwU6Q0cF4zkfuRU_mGeQ8eQmqdr2Wo8abDoVnCCsPaJoF7_bemzYFy1MJkRdj0cOzmpGzOmCs6MYRu6aM5Ff8bKJBmL9bsVqM_15kZdaXwxjwF5t9JT7dBMB61uvy8Fx5pcrIoMgNrmXquebHVop6u3Eyj1CB5jnA9SxePQ1CXRBMiE_Ty8Udo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f8eb0d50c.mp4?token=AsjWYqskQ2n9kroLHLxKRcU908TxC-ueHNF0XSlYo3ciVT_RKCaDg2NvYqScusS-Rq3UV8i4OF2FtNNhidz4aVYWl13R41OIKTJ-m6HjQRPij0IEDz178FcQrJlchIcmi_SeT-u0LqD1BSR-het8DyunyKyRCU7i9acrGB2yFemrf3YT0M7WbicTdnBQ8XN64yAYy8lv66LRj7ypKZJW2VXq14J49svPfjIBlYBNVXWfdskvaN86IjpLCInJis2PWavzjH8-frnyywZEyqr_obzZ9e0edcn9sN5BvDjav4oVHzcETGGrEnEVbb-71zTGQGAEI-fIe6Jmj7BWZvwVvjxC7ufMtG4P1N4Ew1wMiJkTt9szL8H9EFrjE-KDsZT4fDhaW9FvLcKs9B7q2FQNT9w1vYqlyjBkOajm71Ipe2XptoxNSWEJ34LRg5UiS8ZPYTxcPzOmEAxM3UitZat-NRsBvpZKvlKD83gSRQ6Yz3lPjOciQaIMxdwU6Q0cF4zkfuRU_mGeQ8eQmqdr2Wo8abDoVnCCsPaJoF7_bemzYFy1MJkRdj0cOzmpGzOmCs6MYRu6aM5Ff8bKJBmL9bsVqM_15kZdaXwxjwF5t9JT7dBMB61uvy8Fx5pcrIoMgNrmXquebHVop6u3Eyj1CB5jnA9SxePQ1CXRBMiE_Ty8Udo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
تماس‌تلفنی امیرحسین‌قیاسی با «سردار آزمون» وسط برنامه بفرماییدجام: من ایـرانی الاصل هستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/23889" target="_blank">📅 11:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23888">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y16PaUkQxGNJj7xT9gg5rSBt_cK0sD-3g0YA7NsktELPqBa5201FLyQoPkBEW23gZP7ZD1Mq_pOAPGUeFuMzzxn554m27mVrPPm-RUwwzLS56QlFjHvkqRArCDLyRuCSwaz2iDaVOSQJPd7vMP-lVv86BkCwp8nI4I5ErfDlaodeFCd5I0ZtuxnHitk9SJ9JO7RxQZvJw5Zo_7-UJwSjvhyPBBsIdUy-OjIO8QKEg5UPtZ2uHtxgeoDXXFc3TOp0nhqq0fH1sK_470JyxkZRtRq_n9BBYlImupAdTz9cT0B_oqT4cZT1Fgnr8UiA23pXIRFy6BCFKqLO2JFQ5VkkaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇪
👤
تیبو کورتوا دروازه‌بان تیم ملی بلژیک:
تیم ایران یک مدافع راست‌خطرناک و گلزن به نام رامین رضاییان دارند که زیاد در حملات تیم شرکت می‌کند و ارسال‌های‌دقیقی‌انجام میده بایدمراقبش‌باشیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/23888" target="_blank">📅 10:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23887">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55029334cb.mp4?token=mx9ixLsQTzcyFaLFq-6RuBUJRuoC8JgSXUMylkP8kZ6fHkO4QPxQavKdTVHMV8wnbX22P1kLai9kssc7J3NFe5pjhj6YybOXMP7_iox1SDSn7TdeJAYrbaxdoxRRc6LS5Merz-Gg4KAxwIvjDK7L01dCngLxUgLWbN0cWV631MjYYEnwInbicjGp_QDRabfKSMAvqMss4R06PNn9haeVCjf2awDemDCjsqxeDSNPFSeFPm3pKtQL2ZluN76nUW1gcX0xEMnZSWUGa6KJJ5ixu0MDDI3DVDGjzEXaSwcwR0Sl5e42zKRZC2c1v0biuurQHg2RXuJW2OHC6F3xXeWlAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55029334cb.mp4?token=mx9ixLsQTzcyFaLFq-6RuBUJRuoC8JgSXUMylkP8kZ6fHkO4QPxQavKdTVHMV8wnbX22P1kLai9kssc7J3NFe5pjhj6YybOXMP7_iox1SDSn7TdeJAYrbaxdoxRRc6LS5Merz-Gg4KAxwIvjDK7L01dCngLxUgLWbN0cWV631MjYYEnwInbicjGp_QDRabfKSMAvqMss4R06PNn9haeVCjf2awDemDCjsqxeDSNPFSeFPm3pKtQL2ZluN76nUW1gcX0xEMnZSWUGa6KJJ5ixu0MDDI3DVDGjzEXaSwcwR0Sl5e42zKRZC2c1v0biuurQHg2RXuJW2OHC6F3xXeWlAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
#فکت
؛گل‌اول‌تیم‌قهرمان‌درجام‌جهانی در 3 دوره اخیر این رقابت از روی نقطه پنالتی به ثمر رسیده.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/23887" target="_blank">📅 10:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23885">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eRCgpgfSJ4LeMyZX-5uiMCyqhgt9yKpKbjU_yvb3fmALyv0vNsN0ZGuT1Iv2DzuUOq-ukqwr0VRUmBCdRJSThmgxEOrEgBCVTV3SLQo1FThcs_NhA0JiDTjOIynMx72i9G8RKqIzNPfY1Zq4MsQlBuUG-XvOANUbnxV0I38C2MXFEApWCrm5mbEplI9kNWCNinDsQYqVvcUw27FHyWuSELcdeWDoo3BljXwRmrVHVuEMK0lCqDyJtrNEOla7ytEBRfWT-Zzft_2gFFlj_zPfIFvnoM5wGC_uh-Bh9bondX7ZvghpVyWVOUQRjdZEVNDC_0eLoAVNrX2KYDnfRJi8pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛باشگاه‌پرسپولیس بلافاصله بعد از پرداخت مبلغ  توافق شده به باشگاه روبین کازان از کسری طاهری خرید‌جدیدخود رونمایی خواهد کرد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/23885" target="_blank">📅 10:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23884">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2831c060e3.mp4?token=huTgAs5t9PYzZWIa-ZYbdo0t3effbvVrIK4wxgpapSNyhXrRFLW4ZwarLQhvxtimKnWY8NZG5a3hc7ejQGbFxHel1Mmugoba01kT-o7Eg4OAfKjYbkmeEaS4uQ-Ar7n3C0RV5Bn8Hi4YmUjkLFhMP4QkjM3mWDmFiUiTzEHekC5asf5XIeWHAsLoqd3AnjKITB8T6o6ttYyycEtlmOSnLsJ5uayJhIE6ZX0dQYC3x_-JO_TRGhVfifBiqNa1V00F8r0f-sqdwbToVX8uxtSRsWb_bcq2b6eDRq5ekqcZaSMNoKn7eJnCao3Pno-DGehO373TgEEeUnNS42uKWIk2Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2831c060e3.mp4?token=huTgAs5t9PYzZWIa-ZYbdo0t3effbvVrIK4wxgpapSNyhXrRFLW4ZwarLQhvxtimKnWY8NZG5a3hc7ejQGbFxHel1Mmugoba01kT-o7Eg4OAfKjYbkmeEaS4uQ-Ar7n3C0RV5Bn8Hi4YmUjkLFhMP4QkjM3mWDmFiUiTzEHekC5asf5XIeWHAsLoqd3AnjKITB8T6o6ttYyycEtlmOSnLsJ5uayJhIE6ZX0dQYC3x_-JO_TRGhVfifBiqNa1V00F8r0f-sqdwbToVX8uxtSRsWb_bcq2b6eDRq5ekqcZaSMNoKn7eJnCao3Pno-DGehO373TgEEeUnNS42uKWIk2Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
بعضی حرفاوجملات هستن که ارزش داره روزی چند بار بشنوی؛ جمله‌ای که این داداشمون تو برنامه دیشب ابوطالب گفت واقعا باید با آب طلا نوشتش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/23884" target="_blank">📅 09:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23883">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TVKmfw5gndEYTrFovghjNVNUkQUYgbpOD4O8WqLtQJGIZmc_PALd8_QrWhSoC_k-oxOg6XESrVm7v19zIFEyG_6Xstc5Nax-aRLa0fGwTEAPrsbRWVH5IhYhvdr1qvG3DL4dYwsc-uuFe8bTBpfMzVyVEkJlGvqnh0RWxajwFtYq_NAEW6nZzWVN1pPesnZtkZlFnxCO2xLwq2igOZA83OGjq1fQArgWaBOLCVRNfmVH0mvfb7xVBq1PueX0L-v-MvvLBEwK-kCZgdU8WhF1RemKqUPFYrVR5MWJFJrAGJPugXleQgqCEdV8uOh4ANici9oaeMr4Awz2vF262-rsmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
یادی‌کنیم‌از واکنش‌کریس‌رونالدو وقتی مسی بعد از کوپا آمریکا 2016 از فوتبال‌ملی خدا حافظی کرد: دیدن مسی درحال‌گریه کردن واقعاً ناراحتم میکنه و امیدوارم به‌تیم‌ملی برگرده چون‌اونا بهش نیاز دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/23883" target="_blank">📅 09:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23882">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OE7nnQL-oZlZ4TC-3NTepXK5542hcnkc5riseiFWv-oFnVCylEuD98vE0VHxcSZxUkNBiAODZ625Q4l5Q9RZw6hUC52VTuwYeVWRUrqLi5umopcOWAJkxM-zKSZZPnLqRhVuiZRQ5W_eAb8Mz4j399EPIVgkVO2eixcvqLuq2B3IrJleY6owT174f6--EJtBwEjoHaxGinyypzTLCAEMkEc18Ds83bytCj0DA16GXuzSWoHT_18WZlxLU3lHEJpvFvyFzTF9pKpeOJ43CIhu3Hj9C30VfMbKJ6S2TkS2o6c6Z3pPJKbQfjmzRxTePYJXPt0kXZKnJywNlnNa8GyoBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول گروه C رقابت های جام جهانی در پایان هفته دوم؛ برزیل سه هیچ هائیتی رو برد و مراکش هم‌با یک گل از سد اسکاتلند گذشت. بازی های هفته اخر بسیار جذاب، مهیج و تماشایی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/23882" target="_blank">📅 09:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23880">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CoANCDvbrmhnZjKZGIiFwk3DXTpSX_g_E7xFzLfdNtxHBmQwLRmz7xYgIZohhNZ1v5my-jZMd5VfoEOGDaLJsiiQjAYvuO2EHW_W_ZxixCn0hsEgZlzVs4h-GgXehSZE2ogjEjx9bC3X1PkSYZgKveSzx2VW_O_kY6AokjOE0gaxYPjGCpy46UIQgufUimfSok_RMIoYqB75tugFAwZOcW-Lavn7IvxUg-AwOZ6UZQZJYLXcgTVnvjm2_Y0LyhIalwLVMslZ7Rbi673z8BSa6HnV05iDIvGS2o73g125NC1L_TA-Lm9qHTLRM8sVI2SqcTjGv35sVvUuHjVqqYNKKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدارهای دوم ایران در ادوار مختلف جام جهانی؛ پبروزی دو بد صفر شاگردان کی روش مقابل ولز بهترین نتیجه در هفته های دوم جام جهانی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/23880" target="_blank">📅 08:33 · 30 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
