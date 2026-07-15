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
<img src="https://cdn4.telesco.pe/file/lNsezOxA2BHXfY6tRgOFhECqXX5ssgKeCQ-EQwdmZv1AtCTmpoEASS4_0m4s7dY8Lo-txw1bSOIgvI9oTcj0j5lFWtD9fjbGmiBzwUBsxCFzqO5mCruOQr9LKjqjU4MK7J_bvEMy49XgLGxsYhlpPY5yl_0FiEN-MR0aABDFVWR2BPr3H4qicfQrCmDiepWsPiyBtPvmNBkmvmGY_7iLZbqhCalV_tXdogu7hF5ls57LG3NxaTPy1T6hJt1soh72eys9kSU-_MfCARxdiNgQFkpZSY4e3gfUz9bDSLBUy54n-dM-upj3ea1--iESkonEEi5ax-8YsHvZGSbuHFbwjQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 195K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-24 18:12:16</div>
<hr>

<div class="tg-post" id="msg-80404">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">به به به این خبر
عظیمی راد، نماینده مجلس:
به آقای کاظمی دقیقاً ۲۴ ساعت فرصت میدم تا امتحانات نهایی کل استان‌های کشور رو به تعویق بندازه وگرنه برخورد نظارتی شدیدی روش اعمال میکنم
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/funhiphop/80404" target="_blank">📅 17:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80403">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">کصکشا حداقل برق دکلای اینترنتو قطع نکنید</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/funhiphop/80403" target="_blank">📅 17:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80402">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sqg3lITGD4CF4poh0hsbN8-4Gvb2iX0BACLqFmkeYcpy_Iw6M8ZwMie0ON80JCm0ntuVg-GCGNlQvRfEL6nz-zcy9G5OJVqM-0TGtOK0C2lql6cVxuyb1EWnus55f9wOJR0_M3UylZGKi4_7c5LUyKx_K1WH0xC_GzirgBf4IA-jDikphiB4SF4ZpBF1009lo9G6rJoWfjy5Kb1dKjunTDMgO62N12F-5INI_hNg5cjtvLf2hWdmnjLUsesnhiGg4vMEoaHjMbzcHMtLci-mhAnBnngrx6y4GC9rlfoJnXhpxGlQqicF3tCYqJDFk9oolhBv8EjDlB9ZSI9EQwLzDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیک علی تجزیه رو از صدای امریکا زدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 7.09K · <a href="https://t.me/funhiphop/80402" target="_blank">📅 16:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80401">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G8TWVPknFP0idEzcD29vp3im4pSuE9leIq1lrt6b19vFh6nJWFV3K4gqi1UMDC2pxJdb9U1gX5XyePBZumI5YfK3UpfSlIZiBEReGgaY1ygszONyTDrHj1JQ9PFCXl4eN_YgQjzPzmRtupimzsER64jytNNdYIhoPgy9qgI6W01G2x72bha0QkDg6Wpjabo5h5-Ncg1AtgEylpPWe4XpGyj_PS3gr58LcNW_uDRA7i3BlTX5fIK9EN6rnLQvJP5MLmDkpms3dVI18zYVXPBEKoeCWFx7fNmhU-fhX_sU0mBkdLVshtb683zsUc8odTlglBVnQNslZDyZim_TTTXRHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این چی بود دیگه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/funhiphop/80401" target="_blank">📅 16:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80400">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ترک جدید لنا و مهیاد به نام اشک ریلیز شد  Spotify  @FunHipHop | Mmd</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/funhiphop/80400" target="_blank">📅 16:11 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80399">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QlfA_KT3Tt3cZWFBYiXKVkFBphNY2J5Vbwh6dQgDTJUopUuA5bsVaKf8gJjAtGOWsay_atkgBaSu33HPv_qXAe3SPwWDbBsr1-OpOx-rlHxdx0HboLnIQpNGYF-q87eSA13p0VTGHi3o4ds6S7bVyn-J6QOXPvEql0XMR8oAmv5OLNnGf8HwpMSheWV17nTi1iDk7w6fl4EaRWBgkPxfypWa_iFyXTLeb3KpCsRLmxDMQ5ibrs9OcWlnqe5YuzcizQS--lL3si0GlwD8ggLGQmYAFT5--Sc9CebZG9tjT3ZVVpQTFD6vFSKXYqkQT05v7zWpsVN1k6EA0dTL4_Lzow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید لنا و مهیاد به نام
اشک
ریلیز شد
Spotify
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/funhiphop/80399" target="_blank">📅 16:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80398">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">عجب ترکی دادن لنا و مهیاد</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/funhiphop/80398" target="_blank">📅 16:04 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80397">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BTrL3-0lfhkxwJoLq8uL574VzwxlI0OMy76hSRMKLz4xsImHNzWGCQaukvNj2fP1eudmO73xMldo8qIi1Evvk9wPc7S9TK-mHFfzJbY3Fjf7qFJWo9xKRLeIaqAHWsjuY2VjknSVQ-59OCfXXC1L-AQF4R4jYCHL8Zl9P3BgdvRy3zQwHTrrtyev2dAOaZoK1PC6O3NCZqURyv3fuxc-yZn_Zp4jDS3YkC4L8mXYBzasDuKb_xY-8TWZA0IAoDswjWeDrPDhjl63sVvLMMwzCsnxLD_SHj5797k1uVc1MmpCd63hLhPEndgeQf_2X6PpcPNhD6-YeWJwbjc5oMKEwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به پیر به پیغمبر من خشخاش نکاشتم، دست از سرم بردارید  @FunHipHop | Menot</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/80397" target="_blank">📅 14:57 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80395">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">جدی مملکت هیچوقت اینقد رو هوا نبوده
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/80395" target="_blank">📅 14:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80394">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">امتحانات نهایی سال دوازدهم در ۴ استان هرمزگان، خوزستان، بوشهر و سیستان و بلوچستان لغو شد  @Funhiphop | Farid</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/80394" target="_blank">📅 14:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80393">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">امتحانات نهایی سال دوازدهم در ۴ استان هرمزگان، خوزستان، بوشهر و سیستان و بلوچستان لغو شد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/80393" target="_blank">📅 14:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80392">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">که اولیسه و امباپه و دمبله قرار بود کوبارسیو جنده کنن</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/80392" target="_blank">📅 14:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80390">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">زمان جنگ میگفتن نیروگاه بزنن هم ما برق کم نمیاریم، حالا که نیروگاه هم نزدن روزی ۴ ساعت برق نداریم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/80390" target="_blank">📅 13:24 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80389">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">تا کی باید تاوان جنگ طلب بودن چارتا پلشت مثل جلیلی و رسایی و امثالهم رو مردم بی‌گناه بدن؟ دیروز بچه های میناب امروز چارتا سرباز بدبخت
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/80389" target="_blank">📅 12:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80388">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">حقیقتا تصور خوبی از این که همزمان با محاصره سیلو گندم میزنن ندارم، خدا رحم کنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/80388" target="_blank">📅 12:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80387">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">محمد امینی دهاقانی، از معترضین دی ماه، متاسفانه در بامداد امروز اعدام شد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/80387" target="_blank">📅 11:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80386">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">با اعلام دفتر رهبری، مجتبی خامنه‌ای روز سه شنبه در مصلی تهران برای مراسم پدرش حضور پیدا خواهد کرد.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/80386" target="_blank">📅 11:24 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80385">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">وزیر خزانه داری آمریکا اعلام کرد چند کیف پول دیجیتال مرتبط با بانک مرکزی ایران را تحریم و بیش از ۱۳۰ میلیون دلار فاند و بلاک کرده.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/80385" target="_blank">📅 10:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80384">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RMycaFqEqKacy73Jn3yRvwmtlYkbh1VhxclVB0hbatgXczb9s9v8ATk2St3TiTwUEmTuFTi6lAQrE-l336VnxHu2K1hw-DiA0C8Ofcl1yfX_Myw21YuG1eX7OJdFgn3mq88yV26TaJBQx0mSUz9vcgd2THng0hvvK7wngQ_QIrE3N5UqWN_EaXJx5EG1flBiO03xAOSgKHdzUqrPxvwsdElxoe5TJtD_5zyOK8nMMgn5u4d7_GRrvWTaHZyQFGUsHbNp_EI00diO_Cp4TDngnBuv9eNPQQSz6YfzrnE_Z5_EeNoz0ODQEAnUuxGlsbnq5iEroqcynFVgaPtLG48-bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوکوریا تا الان توی مرحله حذفی جام‌جهانی یدونه دریبل هم نخورده.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/80384" target="_blank">📅 10:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80383">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hMi2z4ClKSpIN3jQiGBgfb_xfqBuSGeqiDMY8UtD5lmy-ix_TWkDOffi6NqBPw-IFCA0xXuFDWmOTquaQQYRip6Jaz9_Lra3TC9y_tWs9j3C55hfYr8m6GllcZC4Z7lItNHHgZ5PQ1BxEQkHAfSNUwTv1SY0kR3OJfMwBee_mxIhOLPX7rdbR7tV_f38ud4AdmStDDUoBj9nc_ggZUDE6B6E1IOoLIBPntNWNFrG6yHluoJ-aKQAQ8WUptmHQCaiVd2P0qjoPnpNt8L3J0-8K2tNGZ8PBiRU8Md8aa7UP8VsjZegqzOyiMfqWL5OeM-c9uMC9oHFgGuZYpncUC0SFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شات جدید داداش یامال و طرفداراش :
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/80383" target="_blank">📅 10:17 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80382">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dk5b33Kmknr7ZsM5ESzohBYHfeN2rtDUg9Ya2I8qfvV_iYPSSmJrGmb6e12to_P7gW5qxZdej_5UVombXnPXzije3zLway4TCZQIWCZ0oYv8eggFx9ezyX9AtDo0IhqlKUrnfJ_BAmNCzpc-oViQSfIopI8w8oItrQsH39INvS0vZgfu-86b8YziqVISEyurNNe65BxM3hc6IF5TdKW-YQH1WPO37wKHJ1mEqAfNwkhY3A3_Qm5Nwo_vdzIuxj2uImW5EBDIkO7gBKm6aSIeQ4ew0ZM2_dqCLNCsBCoQO1Feoifch26a6n9pdsztSh64-FiRAIJAiEWfygt19R6BeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
-
🇦🇷
آرژانتین
🏆
نیمه‌نهایی جام جهانی ۲۰۲۶
🏆
🕔
چهارشنبه ساعت ۲۲:۳۰
📍
ورزشگاه آتلانتا (مرسدس-بنز)
🎲
با بیش از ۸۵۰ نوع آپشن پیش‌بینی
⚡
با بالاترین ضرایب پیش‌بینی
‌‏
⚽️
نکاتی در مورد بازی‌های رودررو:
در
۸
تقابل اخیر دو تیم، انگلیس موفق به کسب
۴
پیروزی شده، آرژانتین تنها
۱ بار
به برتری رسیده و
۳
بازی نیز با نتیجه تساوی به پایان رسیده است.
⚽️
حقایق داور:
🟨
میانگین کارت زرد:
۳.۸۴
کارت در هر بازی
🟥
میانگین کارت قرمز:
۰.۲۶
کارت در هر بازی
🧠
بودجه‌ی تفریح از بودجه ضروریات زندگی جداست.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r24
💻
@BetForward</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/80382" target="_blank">📅 10:17 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80381">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">جمهوری اسلامی ایران اعلام کرده زیر ساخت های استارلینک متعلق به شرکت اسپیس ایکس جزو اهداف مشروعش خواهد بود.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/80381" target="_blank">📅 09:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80380">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">متاسفانه طبق گزارشات، آسایشگاه سربازان در ایرانشهر با موشک هدف قرار گرفته و تعداد زیادی از سربازا جونشونو از دست دادن و آمار مجروحین هم خیلی بالاست.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/80380" target="_blank">📅 05:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80379">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">متاسفانه طبق گزارشات، آسایشگاه سربازان در ایرانشهر با موشک هدف قرار گرفته و تعداد زیادی از سربازا جونشونو از دست دادن و آمار مجروحین هم خیلی بالاست.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/80379" target="_blank">📅 04:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80377">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">روزتون چطور گذشت؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/80377" target="_blank">📅 02:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80376">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">باز که شروع کردی تاجر
ترامپ: ما امشب، فردا و پس‌فردا به ایران با قدرت ضربه خواهیم زد و در مرحله نهایی، نیروگاه‌ها و پل‌ها رو هدف قرار خواهیم داد.
اگر اونا با بازگشت به میز مذاکره موافقت نکنن، تمامی پل‌هارو هدف قرار خواهیم داد
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/80376" target="_blank">📅 01:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80375">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">بهترین فرصته ویناک هم با یکی شرط ببنده سر پول جیگرای اونشبی که شاهی با دوس دخترش خورد و فرار کرد
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/80375" target="_blank">📅 01:39 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80374">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">اینام میدونن ویناک نمیگیره هی دنده میدن به همدیگه
اگه خیلی پولدارید ویناک نگرفت 333 میلیون بدید خیریه با سندو مدرک
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/80374" target="_blank">📅 01:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80373">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">اقا رپفارسی درست شد
ادرویت و شاهی رو بازی فرداشب بستن
هرکی ببازه باید بدهی دکیو بده به ویناک
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/80373" target="_blank">📅 01:22 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80372">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/80372" target="_blank">📅 01:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80371">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">تنها دلخوشیم ویسای شبهه علی داییه
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/80371" target="_blank">📅 01:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80370">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">دیکتاتور بعد از باخت سنگین از شدت خشم به ترامپ دستور داد به جنوب ایران حمله کنه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/80370" target="_blank">📅 01:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80369">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">سرنوشت دیکتاتور سقوطه امباپه جان</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/80369" target="_blank">📅 00:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80367">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">بارها گفتم تو فوتبال تا خط هافبک درست حسابی نداشته باشی هیچ گوهی نمیشی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/80367" target="_blank">📅 00:39 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80366">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ihOrlXsHWtm3AZExh3PMXESKCvC6UdaTEfF_DwSSgdHj108Pwf_3GfJu4DkcwSqUezGcxS8B_uH2EtkNe7jVbqTEjMhRpfvaV5kgSn66eP09eItsUHirAXv-Jsqq3nL1vQNKjJoOVQTt3aa_YCGiZan7zJvP_WuKQoR-gZyel22ZLkzJc7qp3eHdUgmT0RaY5kEsQ03q4F0lEJEIUuL8hqLVnyU7c6TuCK36JzSwlY_IvKJrqrJnooM18d4Q3vZArf-S-BHBmKwQsiWD38BoypGf4MkaClFjEPfC44JvrgTASbKkUCtepFPAoeY5Ah_MLdKRnREDTxQnX7sGNQBV0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیرم تو این بازیکن اسماعیل، کیرم تو این بازیکن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/80366" target="_blank">📅 00:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80365">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KFkVjx63JQb6t242WdpXfcvho-SzzM95KWdQXKaMlf_9n57s-pfhn1Cy3T5_BdjBQgfUI96_cMjZZvxnhFN8YcP5B9OnCo__msof0j8-MDu4wgM0BT8VTv9NqemI1RtB8r-cWHOVTWo4yz3bCtP5yNuj0k9isy3KQ-RTY8i7KhrGsLrD_FQZOzEUlQ10_l01S9RXEmVMSdxVzTeYvwwRgnLItGu3OtkpwEM_snTQC2HknOphonogJVed4Lc5qGxofSce3HaSCFdyy6ffzXw7fHyBbAxR82cMWCEeeE3g8klVagbawhQVxFBy_XG2I7qDA0AewRTWRA4_gqVFfAxOeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرانسه برگشت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/80365" target="_blank">📅 00:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80364">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">سرنوشت دیکتاتور سقوطه امباپه جان</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/80364" target="_blank">📅 00:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80363">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">با اختلاف این گوه ترین جام جهانی بود که تو زندگیم دیدم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/80363" target="_blank">📅 00:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80362">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">امباپه فشاری رو
😂
😂
😂
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/80362" target="_blank">📅 00:18 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80359">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">امباپه دیکتاتوری که ایستاده سقوط کرد (رید)
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/80359" target="_blank">📅 00:09 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80358">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSajad Shahi</strong></div>
<div class="tg-text">سنگین بستم رو فرانسه</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/80358" target="_blank">📅 00:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80357">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded froma.r.m.27</strong></div>
<div class="tg-text">از وقتی شاهی گفت سوئگ دارم مایکل اولیسه یروز خوشم ندید</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/80357" target="_blank">📅 00:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80354">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">گریه امباپه ضریبش چنده ببندیم روش
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/80354" target="_blank">📅 00:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80344">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">چه بتایی که امشب لوز میشه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/80344" target="_blank">📅 23:24 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80326">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">سلام آقا فرید همین الان اهواز رو زدن
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/80326" target="_blank">📅 22:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80323">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">امشب اگه فرانسه برد نفری ی شارژ بیست تومنی ازتون میگیرم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/80323" target="_blank">📅 22:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80322">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">جنوب، همون همیشگیا
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/80322" target="_blank">📅 22:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80321">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">بارسایی بدبخت شدی
دیونگ چون جلو مراکش با مصدومیت بازی کرده رباط زانوش پاره شده و نصف فصلو از دست داد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/80321" target="_blank">📅 21:56 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80320">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">اگر دنبال یه پلتفرم کامل برای فیلم، سریال، انیمه و انیمیشن هستی، وقتشه Meowvie رو امتحان کنی.
✨
امکانات Meowvie:
🎥
آرشیو گسترده فیلم، سریال، انیمه و انیمیشن
🤖
هوش مصنوعی اختصاصی برای پاسخ به سوالات و پیشنهاد محتوا
🌐
نسخه تحت وب (قابل استفاده روی iPhone، iPad و همه مرورگرها)
📱
اندروید
💻
ویندوز
🍎
macOS (Intel و Apple Silicon)
📺
Android TV
⚡
اگر فیلم یا سریال موردنظرت داخل آرشیو نبود، کافیه فقط درخواست ثبت کنی؛ پس از بررسی توسط پشتیبانی، در سریع‌ترین زمان ممکن (معمولاً تا ۳۰ دقیقه) به آرشیو اضافه می‌شود.
🇮🇷
حتی در صورت اختلال یا قطع اینترنت بین‌الملل، Meowvie برای کاربران داخل ایران در دسترس خواهد بود.
🔥
همین حالا می‌تونی وارد Meowvie بشی و تجربه‌اش کنی.
🔗
لینک دانلود و ورود:
meowvie.ir
@meowvie_ir</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/80320" target="_blank">📅 21:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80319">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">خبر خوب برای دانش اموزا
آموزش‌وپرورش: حوزه‌های امتحانی نزدیک مراکز حساس و نظامی جابه‌جا شدن.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/80319" target="_blank">📅 21:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80318">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">طوری که بحرین رو زدن احتمالا امشب تهرانم میزنن</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/80318" target="_blank">📅 21:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80317">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">فرانسه فقط حملش سوپره مگر نه خط هافبک و دفاع جالبی نداره
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/80317" target="_blank">📅 20:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80316">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rgqGCMyNtDWyedc0umZDJT_WoCs0NzfZxaro2zchlRr8kdqPCh1ipu7-aWIJ_RAcsnu0DPd5LSNMkUIxtlRDK1zPEDce4ArgHl07ohDodb9ZMSzprOF4Jf0X5BQvt2S7vmWVyZR8wi_ebmPVT5cKPg3pLRkylNfA0MzeExcIrNmnjh6OBwYlFRKQTK5SdHnsLwxdHnE6eVkvhBUdFJVLXDMdhmDxztSjs-D_gWjIElm7vCymnG80F5dIWJgMU7jdItbKnXDipiWYnDeOyGpYQ03bmiE-dbSqgFgDGtrfEhsXJLcmo7A6vtotUIHDHLF_58ehFjoJm4KaXzIKzBbf1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب فرانسه
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/80316" target="_blank">📅 20:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80315">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gURlkB91p_WxsNEeHnnNGzn79WHJ9tKuBk3N1_EM1xskEwrMOCWJajAyt4w4bvuWPEtVszrc6WtqmoDlR8o2bJysZPqpDrgE0J2FxdOoHk7C--yqZlJQK3M8cTJIDZiwTiPpAVxhNGSxSeqJOvFpul4RUkggLvTCJgoX-aWU1GPhkRW2J2dLuPvCZnxaDUouFEz3IsvHXDS8fZFGvDNTL2iXgOTqxOGBEtPO8XgbHTTOSNryKsumFDYrXGvx_to62KElhDPpxFVYsDiYUgrVn7XmCb33Tj9dpxNwbL9WvZ_bK_Rge6-B9Z9BEmmJWDHNJE01qpOclNECtOcVAXOJwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بابا کصمادرت با این ترکیب چیدنت
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/80315" target="_blank">📅 20:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80314">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">داش میدونیم مادرت کونیه لازم نیس یادمون بندازی
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/80314" target="_blank">📅 20:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80313">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">یامال باز استوری گذاشت، هر چی دارید ببندید رو صعود فرانسه.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/80313" target="_blank">📅 19:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80312">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96d014ea48.mp4?token=gR9t8fsxM7g7QSHCmebZGdwWvfnfDvUjHF2Na0dBLgdk48wjg8E96EI2rclHXhg3gy5lUOCwnKfdO85S0_OP3T8wXI7SxbVzfxyOjmjcm8b0rszEWFGQA9Raum1P_OcyHFtBbVm4bhXZg_3J3BygYsW99qbsbccU8XsrgY8Kq9j7K8lFFzCcuScxMe3VoHzaqn4e2KtfBlhuqzAyNafVbTYwU90d5gUEq0hv58VynCp-DoVkdcXq566OnRKxHdlA1GVDKIjqhrjHGE_4NLJ94FGFaQ8wQQz0drnBg-gE1zZhk-cApnO2hOzP8MN6qAwGQ30OWSty0XUUz0oIBqhKKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96d014ea48.mp4?token=gR9t8fsxM7g7QSHCmebZGdwWvfnfDvUjHF2Na0dBLgdk48wjg8E96EI2rclHXhg3gy5lUOCwnKfdO85S0_OP3T8wXI7SxbVzfxyOjmjcm8b0rszEWFGQA9Raum1P_OcyHFtBbVm4bhXZg_3J3BygYsW99qbsbccU8XsrgY8Kq9j7K8lFFzCcuScxMe3VoHzaqn4e2KtfBlhuqzAyNafVbTYwU90d5gUEq0hv58VynCp-DoVkdcXq566OnRKxHdlA1GVDKIjqhrjHGE_4NLJ94FGFaQ8wQQz0drnBg-gE1zZhk-cApnO2hOzP8MN6qAwGQ30OWSty0XUUz0oIBqhKKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسئولین بد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/80312" target="_blank">📅 19:35 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80311">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aefqbpYfKQh5Bjm2QWNERi62abMgrZteQONazgF7pM-JZpU4T6VOivcS7Kc71CK6OIaa8G1hj9hTP4sPE3BZslqjB6MULWCaXk9BVFm8dTtHexXtcBAaTSVx2aob7r8a94-k-i2in2-RzAs70ERM5QOmC4QJuON9WZkjExTgD147K4olqy4bGAAlnvD7AN8_dRtPPBUAZlzKaFpPULoGLcpnEftP9DGePP3g_vN2RwQ4bWXh7FZeSL7cpRVoz_pGnLpuVsKDmDCyQHgs7nq4Eir5liJ3rCKLsn2ps7OVvtp8RO6hRQ2tKq1QCCwxdHnbzO5Ws9AAlQV-iXCaAUwCug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یامال باز استوری گذاشت، هر چی دارید ببندید رو صعود فرانسه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/80311" target="_blank">📅 19:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80310">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">هرچی دارید بزنید رو صعود اسپانیا به فینال جام جهانی
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/80310" target="_blank">📅 19:24 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80309">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">بر اساس تحلیل های بخش نظامی سازمان فان هیپ هاپ، در موج های بعدی تهران، سمنان، کرج، مشهد، اصفهان و تبریز به شهرهای هدف حملات آمریکایی در ایران اضافه خواهند شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/80309" target="_blank">📅 18:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80308">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">بنظرتون با پنج درصد شارژ میشه ۷۰ دقیقه دووم اورد؟</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/80308" target="_blank">📅 18:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80307">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d49901ac45.mp4?token=O4mIgv4SXklSqf1UsXTh7r_bl7csRbgeOSYrXFMFi9I1bm0wQ8p_hfn6hxhkk385pCoZNdwhwaMteTwspCCR2gKnCUWxvhcLrvoj6RTGL7OsewZV1OQyAjBGEaNjDYPgTFTN5bgfmo_VS4rlRURj5PVE-5y4cDZiqstkGv796GiHoeVwJ8-B2eMz80TLVouG7YthaaLpfoCu6P0a0VRG5DxUZOyY96iNstbzR3NWU8otEzzny2Z-7XegYmqUpIqx9Z-EME6FpdKKui8oxnyzc6BzOUnG1TH79wHKhMi99EuOmCvCVERJt7OaQUb3l7qqBY7I5kLtf2L2gZzMpn9zkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d49901ac45.mp4?token=O4mIgv4SXklSqf1UsXTh7r_bl7csRbgeOSYrXFMFi9I1bm0wQ8p_hfn6hxhkk385pCoZNdwhwaMteTwspCCR2gKnCUWxvhcLrvoj6RTGL7OsewZV1OQyAjBGEaNjDYPgTFTN5bgfmo_VS4rlRURj5PVE-5y4cDZiqstkGv796GiHoeVwJ8-B2eMz80TLVouG7YthaaLpfoCu6P0a0VRG5DxUZOyY96iNstbzR3NWU8otEzzny2Z-7XegYmqUpIqx9Z-EME6FpdKKui8oxnyzc6BzOUnG1TH79wHKhMi99EuOmCvCVERJt7OaQUb3l7qqBY7I5kLtf2L2gZzMpn9zkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داداش لطفا نخون دیگه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/80307" target="_blank">📅 18:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80306">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">میگن پرستاران و کادر درمان در شیراز و یزد دست به اعتراض زدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/80306" target="_blank">📅 18:39 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80304">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P31yVHEcANeddb2_vvHyZC6YF7f5_ptdB6ATt1umNco8CRlInsqi88R1Kbk3z3PdUZayO5jS23yRiZwfVQ3I6rWQedQOfpEgFNKNG-pHQOQVyYlJY-DXevSpk4bXU9DFuxsHoC7eTjaXwikqLfa7_uhgAJDXF1FeMQcvHPN760jeLzPhwRiLeTlZbX0TLmiPB_wJ6NBmpl9_asWx0Wvs4mSpDoBdc-VZ76bL-EZzu6AgmIhnR1bm2w9QJVakjhdp2JHUPBNr3KdsdEpukc0bfPoKn45v8aRamsSNE-9l4fhcGMx1KEtKZufrYqpXY__VEgl7ZDxhegrhQ2ohqRJJtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OiLD1S7dlpey5kFMXKoWCuTaXk-COz8RdgG8-rPhwigdF07XWwxYRS_aCCavaQS4lNghIp8Y-UkPoe1OTTIizxM3si0xB9KOeOlk5-eNRCOZkT3xsx1vG2f13JgQ46RhGIfY2-IzyxIf0oqqqDYXAG4rpF6anoJoy65g-fFTqrr9K7ap1vAtzpdqcGLVvrzQgPyxIwlEOMpeRpdd6dQV_EfVxBObyqbXj8WVsRaSYb7S_LLcL-IAZd8-XfUD7IQWojtocnUo1XMIrZ0jc6TRcR8bvj84RL4ij0-ipP7OfUsimSZMvrL5JlOaLnQhKoKofiH21Yebo4k3-dQZQL70wg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جنیفر لوپز ۵۶ ساله.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/80304" target="_blank">📅 18:23 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80303">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J2Ny140SGf-7usA-YUIGrSKS4z_nuerTPCsw1JNaAc-Sa2nQA7_k339tOUF7neOMeeGSK0H5DV9bxWTG3CUOVEaYRUbC2TsBXVo_IFHcIwAeezssyIp8TWjEJZ-V3xWjsLWUYtTq34KXEasrIGIJvh6VhxparTd8IhknNivdVJ8rc-o1MGKALsIjnKsME0UXP65Pv4xELAkGeGcgCo9RZIdMtup0aETRtzxuaYVywAjQNQcBycCX-yELqnWTTFC1ADizFPe15GcjJithFlv_dyC4edgNahVomQ3RMMr0jq4rZNlxKa-GN0pn3vosFhGO7Ki3GhfqfrRaKZy9g9ctmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
فرانسه
🇫🇷
-
🇪🇸
اسپانیا
🏆
نیمه‌نهایی جام جهانی ۲۰۲۶
🏆
🕔
سه‌شنبه ساعت ۲۲:۳۰
📍
ورزشگاه دالاس (ای تی اند تی)
🎲
با بیش از ۸۵۰ نوع آپشن پیش‌بینی
⚡
با بالاترین ضرایب پیش‌بینی
✍️
اطلاعات و شرایط بازی:
- فرانسه در دور قبل در یک دیدار جذاب، با نتیجه دو بر صفر مراکش را شکست داد.
- اسپانیا نیز در مرحله قبل موفق شد در یک دیدار نزدیک، بلژیک را با نتیجه دو بر یک شکست دهد.
- برنده این دیدار باید در فینال به مصاف برنده بازی انگلیس و آرژانتین برود.
- با توجه شکست‌ناپذیری مداوم دو تیم و نزدیک بودن بازی، تساوی یا پیروزی خفیف فرانسه گزینه‌های مناسبی هستند.
🧠
وقتی بازی با فکر انجام شود، باختی وجود ندارد.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
g23
💻
@BetForward</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/80303" target="_blank">📅 18:23 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80302">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LtzhiLl5wl_T8k_UpU5qkzpnSTvyK86xRz1VhGCc8bkXcSqrkTltdNqnHXz3TbdVm5-PiZxOUwrHXsApg2zNCUZ_TGLFIi5cEdR_8owFUdHvSUVc7o2hEMYXhfGht_1VglKmBG7ZrvgNBGFmZTRP45ZM-xdQsXo4zQwBO9tcrUVrigVQx8m9Vsfyol8hQCVphValYGHCMWtRw2IZhEJZkRSipOQaJWYJ9Ioqa0HhyzGeMVOBuzBtTGcFjHfTEU6mF-ILxIH6qQ4WIYJCCykp6Iz6wUyhHWf2AG4S6T2LY-HvnQHQu9SHkJklBjKE0p4D8QTZu9ppuUB9Ev4X_9NaNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوه اوه   @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/80302" target="_blank">📅 16:28 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80301">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I8CqDo37Dujo8VGhnxl17YWfwk9FTkNc6nDtVB0aGUTIZ_FvoQdEEFQAn8KmmdbzMro6nId-iC8gxTo8Uk7DN7dHeErY5Bf_BitErn11edZd2kXWPCccPBCuLUrcv2lesXIA5_mcDAryPvZIPsZHA1r4umTSdvT2saDyYcBrabDoaKLWDIM62acXE4mEiDtN7iwe6G2dn8djqQUdDfejGpApEMPIMm_1VBKQLXw5klTuLk43Z_Ju8X7LEp_LDdftpPSVvJnBDaDOku5yKH0SX0hOlSEQIPZ5-UGnPhNIsHk1EzM97yVzztR94AA3Y2KJvz7Z0RXCXdGoq8RhMKNeAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوه اوه
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/80301" target="_blank">📅 16:21 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80300">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lPcdSjKViZjG-y3fmJ7Z04Gf4rnuiKvR7jLFuKd3FtZiOvacSm1odAzYe2g_8ii6DpwPoivzy_8wb9z-YKQwrHK1vblouJEfbeZ6s-AX-u-UhlkvJeDGwEAmIJQ9UHT8rt8sexgpukV7CZ5qv9XkfH3Hu-dVlZMjDcAR5-fISIK8VfVIlzNPoiC3D6MZ480PHQ4tQbp2XUe-zvGNx2Gfqd83400g4Y9uU04pHf1QgvwKwh34W0Iw9AADq9aEVsBa_QZuD3LM8iHKQk5YfGwkpzKCcmITLOx5BRz7oxNZti0yEuoHnVbaFEMrD2KT8rgR2hp5lEILeH4igW9WJYha-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/80300" target="_blank">📅 15:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80298">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K2gbJRmE1lEeme2-ZHjC5StDohsk6-FJV7ywVXsYaZvUN4XMc5zp4VXKK_ri3c_6YXPW68RoWq_0te1qdRBaSq3KjI8AjwmjG0sxh6xmUqLWRZRCWs9TLdrCyP8ImkFEOJiFVAW6kiRgKSgpLl76_LM9ITJC1tw3YcCNYFZc_3rz0bGKJ9lzIK-HHC4ODOF5cfTC-iCX-nQsgobIQyHyN3yYXSr0Q9SMCijpibRozV8OBf01jMusTb6Z2ZJlauvGVbqa7oSaetGB7XP9qMR1f5pD2j-KT68dk_OL1wYVSPD_AVC5PT1aBJOk3szrmAhu4q_bYsOJhWHcN5ncvlLubw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uaN5X76mm8p89s9zrJ8__am4Stu3r7nhoK3MDX1_3TnkQ4zSekZ0xugvEFopUjmBxntjpLC7OnVvbKpeN1TN93aHV9xqs8FrHosEFxWLh4bq0w5EPGfU7m7vfBKE-hQCc6jAhsU0u_rtgQ9iaHAs8BiXkUUEWq2oXBfNSlrSA0FhlmpzjH4wVeRkC_WdgHLKUwUBqpHYJJg3gsLXhOn1ZC81Scc_AguTnttFWbWHmx4t84NgvsB2K6WQrPRqoDt2RkX7YN2UZMiTcJkvZXNOIxNb_0atWYXzAE4PSMWtFyUuE2ik3h7BODV2mFTIZx8eXiKPAp2aXnKo2axOiaVAyw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/80298" target="_blank">📅 15:21 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80297">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">امتحان ادبیات امروزتون چطور بود؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/80297" target="_blank">📅 14:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80296">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">امتحان ادبیات امروزتون چطور بود؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/80296" target="_blank">📅 14:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80294">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">الان سکته میکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/80294" target="_blank">📅 14:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80293">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">Shoti ke vinak az chateah ba kagan pakhsh karde.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/80293" target="_blank">📅 14:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80292">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">چه فشاری شد حاجی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/80292" target="_blank">📅 14:04 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80291">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cTtSgk-QJC7MqnnATdnkduFJTJRNVMPRRhJupiTztrX21vtT_WCc5x68DmwIio877bQyn7EP7u6DIatfh74iE1-8c2qQnkijK7k-8Xhch68gkL-kzHtgz3UrlMiJTEATnaRc0CKXZELtcE_pS0fd_DV0XO9vOPcBKFnQAxrXTiD4dlHp2se5FTxaLLCj3kE74po_vQ_qaEl6CRvRVtlV9qmC6vBpFxCRP9XYeW597mlmSXnV8UFjM7C8rxBxg6rZ1LA_CnS6kZJRqm46Icr9K0XqNW0iobxY-pejv1JiqJuC118OzQv1eS_QEP_B_Iq510GOAszYbA4fruzpt_vR3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Shoti ke vinak az chateah ba kagan pakhsh karde.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/80291" target="_blank">📅 14:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80290">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/80290" target="_blank">📅 13:55 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80289">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">پسر دوش آب سرد بگیر
😂
😂
😂
😂
😂
😂
😂
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/80289" target="_blank">📅 13:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80288">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">مامان عمو پورنگ درگذشت
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/80288" target="_blank">📅 13:23 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80287">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ Fun HipHop ](Young Arash)</strong></div>
<div class="tg-text">امروز روز فلانه و کیرخر‌.
@FuunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/80287" target="_blank">📅 13:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80286">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">انفجار دوباره در جنوب برای ترور مجدد چرسی در جبران ترور ناموفق قبلی.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/80286" target="_blank">📅 12:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80285">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">حرفای ترامپ بوی "من همین الان یه تماس از ایران دریافت کردم که میخوان توافق کنند پس یه فرصت دو هفته ای بهشون میدم" میده  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/80285" target="_blank">📅 12:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80284">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">عجب امتحان پیام های آسمانی سختی بود.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/80284" target="_blank">📅 12:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80283">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/80283" target="_blank">📅 12:23 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80280">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">حالا ویناک که گوز کونی نیست ولی همه این سلبریتیایی که دارید ازشون دفاع میکنید وقتی ایران بودن خایمال بودن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/80280" target="_blank">📅 12:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80275">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YgTgk2UDFh-fIzAiV-OMkMO_rQtn6o4Owf9L377VeVnHiZlAWlLe4txy5K3Imrrq7mDx6Z-I19dhsvcP77GTK3E1767-g2vtOeH9tpaepc3aYxMg1fV4lYhwyhaxWkt9P6R37vmfVH4KcveSN7L7WoPqr-h1DAw1jl-Nyg6fugOwoHVqaH46V7k-MFZpeEyw_OWgt2UQrKSUIbBbTCWrn6x2YclvfYSDbj3Jze6Z2AOb3ClNtyqCpBTCbrMjlHKMojiKnXXgm9r07uD5cAHMtr2PKXZ1UAN0fn1xaS09bM0qj3MEvGbuSv1cRsm6uOeuCdhO6u5QGePJplvPYTPktw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q9Jd-efrELrh4MWnxQQubvVJfYaDmsvxJiYFfNope85TU3T2bUMGEd1fUZVSZg0s2aSwSQpZlDBP6PN39Sn4lhLd5cEYv5eUNv5euBE9RbratnC2xUEXyZudEwS9MvEKS8jRzk1Xn4xcHyCjjppIKD2g8qJx75RYd_FyHggHdRuUW2XkFuUOXXMe8c3mc2MTXbcdGLoqLsYE2KxxukhL1-96PhJeqB1MyzFUoy0pe7Hp_l1-CrAqd_WjJiK2NTbTmqYqz7irtcz3FWuOozb_WGGboRi605aYt-4B7kOwi9QfAs71FXKIJ5zRx-i4u8OPDW0t69ISnbe2-FiTm4Qg1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tbeL3lTksyCuRwlIOTOA-14Ha9LrmBaormTbnEYbMBNSdvNk8it9DDags2hAWftMxZEDbnI8OnTWP3SMjjBYzhFKCjOEOvf8y_QPEjW4wde-31x2QMfiV9jJi-VZBDG8qeLZTOPV54eCKrhDcBut550XLYno5dYlv8vmjw1DvLs_yqe549Z71JzA02vk2T7x-jVi-XVYaYiubOO_E9CrZMx-gyGtjlYAeDCJXl_IpYrd9jVe7IlErWEOiniazb85GQzGLh0vrVuQ0BPp7Dk80MgYeybUnIgRgWWBdcl10LEFH3TyJIg1JBGe78u_S5QLGUZwVhU3uU3VOzYNEWiFrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JevY3NrnFeRiIVJwwpycZ-GdzuJxoCjmyK0g-QuYIg_5dTXv0bGFnqvcSit_bkubAjHTNbYpw92AvABBzNr7NcRAK-YRTXTfq2vrJvWTlalrjKmAYlrec0qQkeS2s3KZnsrxaKdIAnn4ai6Dbg1N65C6jVEkzJ3TErtg7XfM_8FSXHGOcpg2o7WQOjUkti-Qx7Wcb89Y4m7rEk0YknGH2zl3LworxS4eOevoAZyN0ckLRUS1GnODDk1c7Y7deSNRSNngKdprYA2YhKUtw4h-vh93GydKohpFca-H5t1YQE7VeoqGHYwe1MBjNDPfoTuyKzxQOaBMmcUbu_oMOqfglw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hw9gRfc-PzKtO9UH8pJpVvmqPXf9FEG9vAE2Gh4_ZOfRh2PaHhiXMMjnqD9gZDl8svo6kcRg_vNQ4OBBNIGdMFGETGgW0CZ_ZVViIKBlUMHV05Q7q_wMJtXwJSLZeSp7rIDETLiXUrqOEySUY7Gsr409MAsmDhBhqjWN3hYBtC2TX6RMVn16ebFBg-u48JPDth-leb2lX0rBBtyM6XWE4_gbeZPRp6Ymsrv6vyO7oX-A6jYyVobkxAZYOhWwMd6tt7qGmEBm17H2Wi4fjTQqLZlyLn6mDnpEGk-pG1RZOqb9wcJUwVRGyA4c1wtyoWNTfjJyaTl2o9DcdDk1e5RhTw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ویناک اینارم از ۴۰۱ گذاشته و میگه من اون موقع هم خایمال نبودم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/80275" target="_blank">📅 11:55 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80274">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73eef393f7.mp4?token=jUdsPuueAguDdNByj3IdRjZl2UfS5VdZ7VQMIJgdywEZwFBdRtFwqs8gen9_c69tLTSsBU-UAccgsGun8Oqi7NmqloErHnuEb9FqypJGbzaP97wL4iTKGptRKZQ_WMAyxyhqWnM07yXUe0dw5w_roY4_iCtbRXHmzHgyySGlNyoU6hWDzv7FbE0pLqICbPScBjPB7s1D0ck5B4XR-wYRVkYGFwJeIRZevkxfmyvU7Nd2lYPXBMQlZGOg2_6o5y_HTGf_ysjixb2VUC-Q_kGmyiZKnxL_wL88pxf1kzG2Mg_e8ebSUgzLyo1AEaQIWL98_X3Bf1O58aaG-oTAeCQ4Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73eef393f7.mp4?token=jUdsPuueAguDdNByj3IdRjZl2UfS5VdZ7VQMIJgdywEZwFBdRtFwqs8gen9_c69tLTSsBU-UAccgsGun8Oqi7NmqloErHnuEb9FqypJGbzaP97wL4iTKGptRKZQ_WMAyxyhqWnM07yXUe0dw5w_roY4_iCtbRXHmzHgyySGlNyoU6hWDzv7FbE0pLqICbPScBjPB7s1D0ck5B4XR-wYRVkYGFwJeIRZevkxfmyvU7Nd2lYPXBMQlZGOg2_6o5y_HTGf_ysjixb2VUC-Q_kGmyiZKnxL_wL88pxf1kzG2Mg_e8ebSUgzLyo1AEaQIWL98_X3Bf1O58aaG-oTAeCQ4Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویناک یه اجرا از دکی گذاشت چنلش.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/80274" target="_blank">📅 11:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80273">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ui1Dm77S56XsIZ5wRNB0800gJ433Yz79DYqMNLSZc9YxweV-kNJTNdZZoxJcZ2G167x3JrkfRMDqLXobpO8ItxK6S2KVCTscGRsTnyCCUAx_nplaPjCJOaLb3VaH_vTlNz0exumPvdsTGNveblRx_jxc2sV7UnAb3c1UJoCi0IaVxKlzriGQ8XVJ3fcsH5DCKQrhzQQfzs5wTimfHCRMKYO16bUI7s6gHzZFq-BZO-DRYsffclvE1vlMdR2NwvZOpBTo957Fre8ODVPPb59VZGpik5VPAJZjdlh-o7rOqdBAZu8zE5X-fJHeg9YjuWmsLR3DDP61Ky0v8RrAYjlEoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
فرانسه
🇫🇷
-
🇪🇸
اسپانیا
🏆
نیمه‌نهایی جام جهانی ۲۰۲۶
🏆
🕔
سه‌شنبه ساعت ۲۲:۳۰
📍
ورزشگاه دالاس (ای تی اند تی)
🎲
با بیش از ۸۵۰ نوع آپشن پیش‌بینی
⚡
با بالاترین ضرایب پیش‌بینی
✍️
اطلاعات و شرایط بازی:
- فرانسه در دور قبل در یک دیدار جذاب، با نتیجه دو بر صفر مراکش را شکست داد.
- اسپانیا نیز در مرحله قبل موفق شد در یک دیدار نزدیک، بلژیک را با نتیجه دو بر یک شکست دهد.
- برنده این دیدار باید در فینال به مصاف برنده بازی انگلیس و آرژانتین برود.
- با توجه شکست‌ناپذیری مداوم دو تیم و نزدیک بودن بازی، تساوی یا پیروزی خفیف فرانسه گزینه‌های مناسبی هستند.
🧠
وقتی بازی با فکر انجام شود، باختی وجود ندارد.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r23
💻
@BetForward</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/80273" target="_blank">📅 11:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80272">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/djHBX1LirY5D9gVNzBY-id3x0ol_vZbyMeeWwEFK1HXfv1LOs66GHEzpx-Z8uYujWDohZJaw1rnMuM5nYW-M9lcV1EE7BaMomfo7dortkghQVc54IXvSwA5zl098vTENBbH1rQ6i7SPwYrguqRHhjP6f4lzs_5irVuZ2Lb29S3xP2Xr8OZSkImsaFPFjG6XxQjTVgQK3-Wea-PjgBZ5VFSfW0AgDTG5IkvfX8pGBH674AU_Ax7QngfHAune4ZmLaDGjpCmXcrF6nxcCCFoVr_mGPYn7v5Jp0ry3WeTl6qd5PVqSwYtzG6xy8d-TBy_XGEyowdwbD-vTgR30KsJXHrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خواهر لیندزی گراهام جانشین او شد
فرماندار کارولینای جنوبی هنری مک مستر، خواهر لیندزی گراهام، دارلین گراهام را به عنوان جایگزین او ، سناتور این ایالت منصوب کرد.
با توجه به پیروزی لیندزی گراهام در انتخابات مقدماتی،خواهرش یک دوره شش ساله کامل در سنای آمریکا خواهد بود.
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/80272" target="_blank">📅 10:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80271">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ترامپ دلقک از تنگه هرمز هم میخواد بیست درصد تعرفه بگیره.
سازمان دریانوردی بین المللی اومده گفته این نقض فاحش حقوق بشره.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/80271" target="_blank">📅 08:24 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80270">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">اسرائیل نیست خوب لانچرا رو کشیدن بیرونا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/80270" target="_blank">📅 04:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80269">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">الان که شما خوابید آقا آرش بیداره و موج دوم حملات آمریکا به جنوب هم شروع شده.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/80269" target="_blank">📅 03:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80268">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">نفت شق کرد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/80268" target="_blank">📅 02:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80267">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">کنکوری های عزیز ایران بخوابید، کمک در راه نیست.
ترامپ: معتقدم دستیابی به توافق با ایران همچنان امکان‌پذیره.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/80267" target="_blank">📅 01:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80266">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">حالا که مجبورید امتحان بدید حداقل بخونید تا دوازده سال از عمرتون که اینطوری گذشت بگا نره و ی ثمره ای داشته باشه، با آرزوی موفقیت برای تک تک شما در امتحانات پیش رو.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/80266" target="_blank">📅 01:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80265">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">من که میدونم این سری هم جنگ نمیشه ولی نمیگم که دانش آموزا همچنان امیدوار بمونن.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/80265" target="_blank">📅 01:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80264">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ایرانم به رسم همیشه عربارو داره میکوبه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/80264" target="_blank">📅 01:21 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80263">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">آمریکا هم یاد گرفته ها
دیگه جنگنده بلند نمیکنه هزینه الکی داشته باشه
یدفه صدتا راکت شلیک میکنه</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/80263" target="_blank">📅 01:09 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80262">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XIeTYkQvis4crGCf_xMoBqmmZFrXRJ3z9D-SLIqwOZjKasOh5FUgtYrF92rBaeKwHwDaGAXMCGkSgu8WkxQEq_58-tiU8DjupxVC5uumiv8Kk7DHmbCMm0tTB_45rGoRr8bvqagfobO_mgo_k-3ewlWwPUJ7ZNaW33qn_peE7a8tb8k-w2k0LyBV1wHGrcxJ0R7eFbm6HRkFDwDrAG9qnkjQvGGYSzE9mLOR3rgv92RTwnM4ajNOCeX9cPUka7OKkDXrwC4wjB3wQIrpit_Dr9bcw8-RMkdtsBCluaidnwBZKQ86kezm4N0XLHNtI1Ln1923z1xxhxA-0FutXSAeaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا موشک کم اورده داره لانچر پرت میکنه</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/80262" target="_blank">📅 01:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80261">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17049dea80.mp4?token=CbZTbEwm_TN2SnilpGBWGbm8h078cqjufQJotv4On80KjkD9IW8TUJnUc7uu9Z9jpjkaHwEAqcVZAadAD8R8SO7k5hkbBR5XiZ_cI1sox24RqueEX75Ni17lqEFCRGudwlFScxbgHvankgYkuUS0Egk0AG4AHkElXcjCbg9oLvSu4b7JZROYYz9bT7P-cEw_MJz87CXpRMHX8bIjL4WVVQ8INNK2ecxr7vXb7DWejlF1m21zTn95q1anLgdYf-jnDTMzDAd4NANYeGvhfvI2gk8LIpa23hsPFQiEk_la3m02BcH2Qmqbvh7C6id9_lUWIWwz-vqsXzWrlaLaQ4WfMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17049dea80.mp4?token=CbZTbEwm_TN2SnilpGBWGbm8h078cqjufQJotv4On80KjkD9IW8TUJnUc7uu9Z9jpjkaHwEAqcVZAadAD8R8SO7k5hkbBR5XiZ_cI1sox24RqueEX75Ni17lqEFCRGudwlFScxbgHvankgYkuUS0Egk0AG4AHkElXcjCbg9oLvSu4b7JZROYYz9bT7P-cEw_MJz87CXpRMHX8bIjL4WVVQ8INNK2ecxr7vXb7DWejlF1m21zTn95q1anLgdYf-jnDTMzDAd4NANYeGvhfvI2gk8LIpa23hsPFQiEk_la3m02BcH2Qmqbvh7C6id9_lUWIWwz-vqsXzWrlaLaQ4WfMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شدت حملات از جنگ ۴۰ روزه بیشتر نباشه کمتر نیست
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/80261" target="_blank">📅 01:04 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80260">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">حداقل کشورو بسپارید به فلیک شاید فرجی شد</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/80260" target="_blank">📅 01:01 · 23 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
