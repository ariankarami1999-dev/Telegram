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
<img src="https://cdn4.telesco.pe/file/QR1ePsiGx-a3pmKpiBAZi5GXhn55iS2k6AzlIscQ0VJDiQb2HnzNbIy58kmgMKbhI1yLumAOisYkIUNJGGylo6lB-4lOC1V-YJ_8k3rDr5crH4q1ZSfaYJEtEtzILLeNGBHD9794uPZBZKE3_1YBaiVeU6PecCpmEuS4gYEbv0_XWbewkNx4WpjL1S9QQn8SgjI2V2xsjfRMWqqH6HbDMKrJvt-Ld17QT5VkrI0K3V1ep7OkTLrFC4w_GWu_Z74-k62-BsJZI_f8qTXhNcYfvvCF71cWG4mMN1IHVciTjhWYmKIqb8wV_1nYgsAZS2Wqsiyi_rO6_CsD3xrTHsfsKg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 192K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-17 19:55:01</div>
<hr>

<div class="tg-post" id="msg-67538">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">‼️
ویدیو ای که سپاه از حملات دیشبش به پایگاه های آمریکا در منطقه منتشر کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/news_hut/67538" target="_blank">📅 19:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67537">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/735f956d53.mp4?token=g-FeuWGZC5HEIyVkVx_9GAcQ6Iv8vrwtl2Pi5tz5yMVCMrMrZSIGcJ4mCVdegg-1MdedIWtELi37FTs4qyEVhweW5evIc-vg5A420NfH-NHd7X_qKoT8yIbKoBeFMSmvoMaPp587EhJY1hddAjjqivK65laS3YeuG8XTlL6jyCDFWTciZIClyOhFFkmaCLr8k8GDDvhF8pYFqRoa6vD8N2lrVkgGiJzKd9Bo-V2FQvQFM_mIxYprH7o7KyKd62MwWWrIkeoijQak2LWliifs03a48t55gGqbOS6faCjPYHXHnT_sB-lmBisYxPYOJyA0v7XtgJMuqdXVa-kxdYWYfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/735f956d53.mp4?token=g-FeuWGZC5HEIyVkVx_9GAcQ6Iv8vrwtl2Pi5tz5yMVCMrMrZSIGcJ4mCVdegg-1MdedIWtELi37FTs4qyEVhweW5evIc-vg5A420NfH-NHd7X_qKoT8yIbKoBeFMSmvoMaPp587EhJY1hddAjjqivK65laS3YeuG8XTlL6jyCDFWTciZIClyOhFFkmaCLr8k8GDDvhF8pYFqRoa6vD8N2lrVkgGiJzKd9Bo-V2FQvQFM_mIxYprH7o7KyKd62MwWWrIkeoijQak2LWliifs03a48t55gGqbOS6faCjPYHXHnT_sB-lmBisYxPYOJyA0v7XtgJMuqdXVa-kxdYWYfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
صدا و سیما و رسانه خامنه ای برای اولین بار فیلمی از حسینیه امام خمینی در بیت رهبری جایی که رهبر جمهوری اسلامی مورد هدف قرار گرفت را منتشر کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 7.39K · <a href="https://t.me/news_hut/67537" target="_blank">📅 19:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67536">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
یدیوت احرونوت:
نخست‌وزیر اسرائیل، نتانیاهو، و وزیر دفاع، کاتز، حضور خود را در یک رویداد لغو کرده‌اند و در حال بحث و بررسی مسائل امنیتی مرتبط با تحولات مربوط به ایران هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/news_hut/67536" target="_blank">📅 18:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67535">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62a14b7982.mp4?token=RGl8Rmu7u2hp6gkmd68Zf3ChfIzVgOcLtx2TYO_1b0zkskze7tG-Pl6-leQ9B-yIYCmt2g08q4X1MIFMgm5Kad0r-iJ8Zn4UhHGyptyfqvT5mP1G8sE_T4vHA6s9IZnW_4eLo0jzeYVnsmYB_MSC5seLQaZH6tVw6ZN60H47kc0KQniICIXkq28Xjc9frMJwcR7EOLiKboVC_is7_AZzKyCFFxG2EsFB9Ca0bNzReliQzz4ieXeaI6JzxmL7HivS5IEkZNWNbOju7ORBUWkj8qyr3k3GTGsmGd11Br4RppQExKZJiyzrAy0ByKQC5a5cR41a-k6jDYb_k_ElpNegYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62a14b7982.mp4?token=RGl8Rmu7u2hp6gkmd68Zf3ChfIzVgOcLtx2TYO_1b0zkskze7tG-Pl6-leQ9B-yIYCmt2g08q4X1MIFMgm5Kad0r-iJ8Zn4UhHGyptyfqvT5mP1G8sE_T4vHA6s9IZnW_4eLo0jzeYVnsmYB_MSC5seLQaZH6tVw6ZN60H47kc0KQniICIXkq28Xjc9frMJwcR7EOLiKboVC_is7_AZzKyCFFxG2EsFB9Ca0bNzReliQzz4ieXeaI6JzxmL7HivS5IEkZNWNbOju7ORBUWkj8qyr3k3GTGsmGd11Br4RppQExKZJiyzrAy0ByKQC5a5cR41a-k6jDYb_k_ElpNegYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
خبرنگار: آیا برنامه‌ای برای اعزام نیروی زمینی به ایران ندارید؟
ترامپ: چرا باید الان وارد عمل شوم؟ من زمانی وارد عمل خواهم شد که آن‌ها کاملاً از بین بروند یا به یک توافق برسیم.
@News_Hut</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/news_hut/67535" target="_blank">📅 18:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67534">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2479db8c8d.mp4?token=b5NUGUFcwknfXWKcs04FgsSuep_LpSezJIU4y2xapqf4OuIfE5y9FI09cyLA0PkKIWuLmczxUS8nuQp_fsvEMM0fdbDpM6pU6RNFj2wdmRcQK-JZsxtMnDdSdNQv-U-Bmgrm8nm23zojB0BAHkfCh9FFyOvW1WvAaB4kXPr_q742RGJZKRk9K64r4jd-dNSWDkzVxMoKrNJwwWY-PZ4qr-2nHaXFtq-Y3TfSSy_Bqz6xWjoKKClZ2Z_SjIAHEGpx1ggHUDTd1nYFB4_8d6JWaMIhQ9OTHWc-lmyvIGp8Xf66632CzJRD4KKIpK6G6yL2_EfcjXYSDHa9zM10AdeTWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2479db8c8d.mp4?token=b5NUGUFcwknfXWKcs04FgsSuep_LpSezJIU4y2xapqf4OuIfE5y9FI09cyLA0PkKIWuLmczxUS8nuQp_fsvEMM0fdbDpM6pU6RNFj2wdmRcQK-JZsxtMnDdSdNQv-U-Bmgrm8nm23zojB0BAHkfCh9FFyOvW1WvAaB4kXPr_q742RGJZKRk9K64r4jd-dNSWDkzVxMoKrNJwwWY-PZ4qr-2nHaXFtq-Y3TfSSy_Bqz6xWjoKKClZ2Z_SjIAHEGpx1ggHUDTd1nYFB4_8d6JWaMIhQ9OTHWc-lmyvIGp8Xf66632CzJRD4KKIpK6G6yL2_EfcjXYSDHa9zM10AdeTWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ:
هر زمان که ما به ایران حمله کنیم، قیمت نفت کمی افزایش می‌یابد.مشکلی نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/news_hut/67534" target="_blank">📅 18:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67533">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72f85ab468.mp4?token=Hp-e8uze6Hk2BHakwRlAgXVWCtFqRoxF9PdIMo1-qBEd6JFjb7yXrSFVDZF5jce1BcJnKYS1itU8OknuihjCvts_aC1OgpVtpw4v1IR8fvvUJwLpZb5gttuMQ_6-ZbOWr2gvteQxLfGMcalVQjADHWO6kqpUNMoYRiIfgU346aAAOboh9r1MdxDVNBMQgIO4oMM1uCrmBzWAic1DwOjruQ8Or88aGZSK79tl3eRmQ8d4zwprDIlbLixuUTyRCeVOoHnMsi39f4iKYIjNwlJrkLOn8cGgigIDK3inqj22F9ZeHtLNkz-VZkK8medf2raybGjoEpHFg-jMGnQrO9nK5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72f85ab468.mp4?token=Hp-e8uze6Hk2BHakwRlAgXVWCtFqRoxF9PdIMo1-qBEd6JFjb7yXrSFVDZF5jce1BcJnKYS1itU8OknuihjCvts_aC1OgpVtpw4v1IR8fvvUJwLpZb5gttuMQ_6-ZbOWr2gvteQxLfGMcalVQjADHWO6kqpUNMoYRiIfgU346aAAOboh9r1MdxDVNBMQgIO4oMM1uCrmBzWAic1DwOjruQ8Or88aGZSK79tl3eRmQ8d4zwprDIlbLixuUTyRCeVOoHnMsi39f4iKYIjNwlJrkLOn8cGgigIDK3inqj22F9ZeHtLNkz-VZkK8medf2raybGjoEpHFg-jMGnQrO9nK5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ درباره اورانیوم های غنی شده:
این مواد تا این حد در زیر زمین قرار دارند که هیچ‌کس به جز ما نمی‌تواند به آن‌ها دسترسی پیدا کند، زیرا ما تجهیزات لازم را داریم.
این مواد در اعماق زیر یک کوه قرار دارند و اکنون مشخص شده است که برای دسترسی به آن‌ها، به ماشین‌آلات بسیار بزرگ نیاز است که ما در اختیار داریم و هیچ کشور دیگری این تجهیزات را ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/news_hut/67533" target="_blank">📅 18:28 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67532">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0911dd57d8.mp4?token=KdSBRMk7bTP-uXoR6dxGAC-fnNpVZ3mVgnLJRNuT1rF1R6SZT9d95wH7-WKJPUrfFCsH8tuxZq-qF1iPxNN_l-cpNM5qY7p7pG0pxD9OWbGWCkADjxAh12E8O6d0wMUHKOUL0YBNbUwV-AzwYwyt2si3dwRfaFukqcz_0qacl4XJaI17PTQXWTU3pA8xLRQA4IUYNj2MJJGsSJ9mSCg32Ve7TkpNn60IPcYXJ_2jAJpvpFwOLqws2gLEGdxx2VqRG7oCsK564xpf08lM-IK8OACPNbtPUi6um8RTZISU4FrfW4S5OahT3--anCvsjKq7bwr8BEgd7e2p7LlwvAnc_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0911dd57d8.mp4?token=KdSBRMk7bTP-uXoR6dxGAC-fnNpVZ3mVgnLJRNuT1rF1R6SZT9d95wH7-WKJPUrfFCsH8tuxZq-qF1iPxNN_l-cpNM5qY7p7pG0pxD9OWbGWCkADjxAh12E8O6d0wMUHKOUL0YBNbUwV-AzwYwyt2si3dwRfaFukqcz_0qacl4XJaI17PTQXWTU3pA8xLRQA4IUYNj2MJJGsSJ9mSCg32Ve7TkpNn60IPcYXJ_2jAJpvpFwOLqws2gLEGdxx2VqRG7oCsK564xpf08lM-IK8OACPNbtPUi6um8RTZISU4FrfW4S5OahT3--anCvsjKq7bwr8BEgd7e2p7LlwvAnc_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
وزیر جنگ هگست:   «امشب، اگر نیاز باشد، با دستور شما آقای رئیس‌جمهور، حتی بیشتر و عمیق‌تر حمله خواهیم کرد، زیرا این همان پیامد است.»  @News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/67532" target="_blank">📅 17:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67531">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db8877d1b1.mp4?token=TNjgr6dqDlyKYTB_om83D-IbuKTfaqY_iq0Havns7nxoXFa8Wr1tnmvNJbD0A4LzMGpVpHYVrVrw65Z8DSYDpq4p9Ek4CqsKEXbnUG1XhApp4buwzAH-7o6vI30u8ZGw870wpFjJqor3pcodabQ8OhhQ_7Bg1vwZLUbsAKGdT81u9blxp9uPNCQ3e3qVVbbuKzjBaEpA4m06rePNPB0oIbzOtmuAISKHTtWhghjPEO54YAwAH6B3tY7zXA4944DvYjDqTiLyj2FWNfMD3GTsJDlnp_Hzzb_OQTtL61CoD6HeXXCsqih8hERoAsEAQUyoeHGhMIOKlzABt6ZhN3v0fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db8877d1b1.mp4?token=TNjgr6dqDlyKYTB_om83D-IbuKTfaqY_iq0Havns7nxoXFa8Wr1tnmvNJbD0A4LzMGpVpHYVrVrw65Z8DSYDpq4p9Ek4CqsKEXbnUG1XhApp4buwzAH-7o6vI30u8ZGw870wpFjJqor3pcodabQ8OhhQ_7Bg1vwZLUbsAKGdT81u9blxp9uPNCQ3e3qVVbbuKzjBaEpA4m06rePNPB0oIbzOtmuAISKHTtWhghjPEO54YAwAH6B3tY7zXA4944DvYjDqTiLyj2FWNfMD3GTsJDlnp_Hzzb_OQTtL61CoD6HeXXCsqih8hERoAsEAQUyoeHGhMIOKlzABt6ZhN3v0fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
وزیر جنگ هگست:
«امشب، اگر نیاز باشد، با دستور شما آقای رئیس‌جمهور، حتی بیشتر و عمیق‌تر حمله خواهیم کرد، زیرا این همان پیامد است.»
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/67531" target="_blank">📅 17:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67530">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوووری
؛ ترامپ:
به ایران هشدار میدم، دیشب ضربات سختی رو بهشون زدیم، اما امشب قراره براشون سخت‌تر باشه و حسابی بهشون حمله میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/67530" target="_blank">📅 17:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67529">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f1152c373.mp4?token=lKW5l4jx1AeuKijz-6cj-VCMqmUHuAYscW6r6lqfwBtwef-os5NuY7sxX1H0V2R85mxVGAWyh5wvoK6lreu2pdkQiNPX8cTfvbsNJvIkVWcmZqW8QSAfI7pmdfZzVJxLhoMfwdxR3lXDekA6nhw-zcTnqqKeLZhzyrBr7cDCdw9y2gb2wBz1bmL2TsQEwmq1jb1ABY1b99m4vTlOpMIgURyOAPMkTFv9hW_LE6w5YmMI5wxxcdIkYHPo8NWuKSHFNAwSfHBYui0pRR9-xXHXdCu_USqby7lqaGXtaueoF3zW4chk5Pu8VR6QrewLrF6zHmjlmY6NbrKZM5Wn-g0lkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f1152c373.mp4?token=lKW5l4jx1AeuKijz-6cj-VCMqmUHuAYscW6r6lqfwBtwef-os5NuY7sxX1H0V2R85mxVGAWyh5wvoK6lreu2pdkQiNPX8cTfvbsNJvIkVWcmZqW8QSAfI7pmdfZzVJxLhoMfwdxR3lXDekA6nhw-zcTnqqKeLZhzyrBr7cDCdw9y2gb2wBz1bmL2TsQEwmq1jb1ABY1b99m4vTlOpMIgURyOAPMkTFv9hW_LE6w5YmMI5wxxcdIkYHPo8NWuKSHFNAwSfHBYui0pRR9-xXHXdCu_USqby7lqaGXtaueoF3zW4chk5Pu8VR6QrewLrF6zHmjlmY6NbrKZM5Wn-g0lkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
آنها توافق کردند که هرگز سلاح هسته‌ای نخواهند داشت.
و سپس، آنها به بیرون می‌روند و می‌گویند که ما هرگز درباره این موضوع بحث نکردیم.
چه کسی باور خواهد کرد؟
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/67529" target="_blank">📅 17:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67528">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff51c5e950.mp4?token=TcM2Ns-vPHDWzf59zyZQkg-k3RkKEOhqQgBJRw7rg6HC8O1bc4mpuzRxXfGySAQTPQCMWKppCJd59bRi0BxN3-RVlmw7pc9XAdyiycMH99_SRb2jgqcWjAgxLjREnbHoRrDnGC6EAdolizF4tHsnjUfWtkl1OtHF505MAuBX9hxulTn0H70vv_y39fuh-rnCKWeqUb_UDNSx0tgcfMv3SeVY8Lg17WIP9qJ3avR1Jb8SyGe3M3oigGaq7LlsI2IJiPY9yxdJbjfktLcmcED1ihDWfkKb0Ls9WZanTg88c26wxQsQJbiidOwITWFi_3CnVF-RQZg27VABjojVAjhbDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff51c5e950.mp4?token=TcM2Ns-vPHDWzf59zyZQkg-k3RkKEOhqQgBJRw7rg6HC8O1bc4mpuzRxXfGySAQTPQCMWKppCJd59bRi0BxN3-RVlmw7pc9XAdyiycMH99_SRb2jgqcWjAgxLjREnbHoRrDnGC6EAdolizF4tHsnjUfWtkl1OtHF505MAuBX9hxulTn0H70vv_y39fuh-rnCKWeqUb_UDNSx0tgcfMv3SeVY8Lg17WIP9qJ3avR1Jb8SyGe3M3oigGaq7LlsI2IJiPY9yxdJbjfktLcmcED1ihDWfkKb0Ls9WZanTg88c26wxQsQJbiidOwITWFi_3CnVF-RQZg27VABjojVAjhbDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ:
جمهوری اسلامی ژاپن دیشب به ناو هواپیمابر ما حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/67528" target="_blank">📅 17:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67527">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac18509fa8.mp4?token=bkb90r4fV5VdVjuo3STuAyByiawv3D7OCV7xvISAL7sIHCOAOG7bmdlb7SKEB5nYRF_jg-2lcUSkzhwCany2U0RCn7vF_Pf3TytOiTFIXquFqQ9Qmb6cut_0l-uPC3ekVqsChwZuz4qKCG_fTH7ayUW-VbnZbEXiBpy3HzUCuSRV3qgnRFJRoafZMEFyB4ilnTO1vKsLUaedxuWRKvBicyOsSCyBrFgu6UNh6CJ5MmjqME_nSdAcWst18lCndDqZo3sVAou0B6UlgKD7DAqdyeDgtPoPgZT3YklfELYTTeUa0ctCxH23PIfmblFBDW6IF2sGlXIbVmTRz_0I9JQLxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac18509fa8.mp4?token=bkb90r4fV5VdVjuo3STuAyByiawv3D7OCV7xvISAL7sIHCOAOG7bmdlb7SKEB5nYRF_jg-2lcUSkzhwCany2U0RCn7vF_Pf3TytOiTFIXquFqQ9Qmb6cut_0l-uPC3ekVqsChwZuz4qKCG_fTH7ayUW-VbnZbEXiBpy3HzUCuSRV3qgnRFJRoafZMEFyB4ilnTO1vKsLUaedxuWRKvBicyOsSCyBrFgu6UNh6CJ5MmjqME_nSdAcWst18lCndDqZo3sVAou0B6UlgKD7DAqdyeDgtPoPgZT3YklfELYTTeUa0ctCxH23PIfmblFBDW6IF2sGlXIbVmTRz_0I9JQLxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ممکن است محاصره را دوباره اعمال کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/67527" target="_blank">📅 17:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67526">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e08b208584.mp4?token=HzumfN0LveMGWXOf2o05EtURfyICDJRqID2r2ULl3RSOMMwvqCCo5JL62lglmHmKaIbCF5YhcIZjgp8g6E1btS9Y2MJni_tw0CCX8Q-x0sNCFTsLYL9w86IUeeYAk-1v5RxDukIKA_ndd3VJupk_NSRZR2kAhqdYq-62plBdiNcTIUKIA1l_ALEnodlgM4RO5WNJCEy6qgrkgib-aCe8mQgtyXKBP1X7e1SzQVhucwZCEaJL8C07tqipfV1kWE02NJ-XAShuxlO8s48RgY9qCsCPAe_6KZg8X2wcoZH7wc81jj8gbm1LI_IHycac3CBg-u8d2tEMmFvzMrE7CFxDMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e08b208584.mp4?token=HzumfN0LveMGWXOf2o05EtURfyICDJRqID2r2ULl3RSOMMwvqCCo5JL62lglmHmKaIbCF5YhcIZjgp8g6E1btS9Y2MJni_tw0CCX8Q-x0sNCFTsLYL9w86IUeeYAk-1v5RxDukIKA_ndd3VJupk_NSRZR2kAhqdYq-62plBdiNcTIUKIA1l_ALEnodlgM4RO5WNJCEy6qgrkgib-aCe8mQgtyXKBP1X7e1SzQVhucwZCEaJL8C07tqipfV1kWE02NJ-XAShuxlO8s48RgY9qCsCPAe_6KZg8X2wcoZH7wc81jj8gbm1LI_IHycac3CBg-u8d2tEMmFvzMrE7CFxDMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ درباره ایران:
آنها به ما گفتند: لطفا در مراسم خاکسپاری ما را نکشید. من گفتم که این کار را نخواهم کرد، و ما هیچ اقدامی انجام ندادیم.
و سپس آنها به سه کشتی حمله کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/67526" target="_blank">📅 17:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67525">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e9aa8bf24.mp4?token=XBa3-NsSD3_QOH5DBRrAQylCMmAEbob0vAXD4_R8TCYMxe2Sq2FYXrfekWPvwFCbYz2iNNSXeHRa16rOBNE9Mbo4kIuvXPQIRByy7OL9S-Ispgk1OtqyKdkJu5gE_UElqe7BMV4kR8oIfjY7uILrRqEM8aoTJjwbh0TsjponlfOUELgwRUX7TXl8TVyKxJBlRAfnBKoWCcYsRou-Oyvx2QKTTIRoIgFnFr4gj2XkmROI7H0r4kKQBsb2ISYYGVsV-tIM5vhqRZi2m4G7nnrgV08ummTE3KlnuooNNxjlYVOtZUJhW2_rEG29JfpGMo37jssgv2k83fyYSyEviW0-CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e9aa8bf24.mp4?token=XBa3-NsSD3_QOH5DBRrAQylCMmAEbob0vAXD4_R8TCYMxe2Sq2FYXrfekWPvwFCbYz2iNNSXeHRa16rOBNE9Mbo4kIuvXPQIRByy7OL9S-Ispgk1OtqyKdkJu5gE_UElqe7BMV4kR8oIfjY7uILrRqEM8aoTJjwbh0TsjponlfOUELgwRUX7TXl8TVyKxJBlRAfnBKoWCcYsRou-Oyvx2QKTTIRoIgFnFr4gj2XkmROI7H0r4kKQBsb2ISYYGVsV-tIM5vhqRZi2m4G7nnrgV08ummTE3KlnuooNNxjlYVOtZUJhW2_rEG29JfpGMo37jssgv2k83fyYSyEviW0-CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ما شب گذشته به جزیره خارک حمله کردیم.
ممکن است کنترل جزیره خارک را به دست بگیریم. هیچ کاری در این مورد نمی‌توانند انجام دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/67525" target="_blank">📅 17:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67524">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/204bddd9b7.mp4?token=C9YkfOZ4dRMfumAG6jORKiv_Mt97v5FHXYwU6OJXtMctbYuZoEJRjXJClmPumAajLlK--vNl0C6G_wGKRfOXm3E4yurqYbHqWcjzdBct_PZ8-slZzWbuIbZjDd0Sem1pBzkF2MpOLvuOztCwdlPqqzxW-D5LGRu2eOekLTQQXF65CU60m84WpTFQ7Jc-jbuHd_cTNW-AJJwdOBmLj6vyNE-du-eQbPAWKZhLaake2yTfZn9QozqCGEJ1KQt-u_60q_32VlqsR0b4cn35YUw00raR4PlgjEN8EHAmyNvU7E0w7qpOSZnBrUr2h_kUyT-HW2j64eYvQ0KgzPGpMIrwiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/204bddd9b7.mp4?token=C9YkfOZ4dRMfumAG6jORKiv_Mt97v5FHXYwU6OJXtMctbYuZoEJRjXJClmPumAajLlK--vNl0C6G_wGKRfOXm3E4yurqYbHqWcjzdBct_PZ8-slZzWbuIbZjDd0Sem1pBzkF2MpOLvuOztCwdlPqqzxW-D5LGRu2eOekLTQQXF65CU60m84WpTFQ7Jc-jbuHd_cTNW-AJJwdOBmLj6vyNE-du-eQbPAWKZhLaake2yTfZn9QozqCGEJ1KQt-u_60q_32VlqsR0b4cn35YUw00raR4PlgjEN8EHAmyNvU7E0w7qpOSZnBrUr2h_kUyT-HW2j64eYvQ0KgzPGpMIrwiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
گزارشگر: آیا امشب قصد دارید قایق‌های بیشتری از ایران را هدف قرار بدید؟
🔴
ترامپ: معمولاً این موضوع را با شما در میان نمی‌گذارم، اما می‌دانید؟ آن‌ها هیچ کاری نمی‌توانند در این مورد انجام دهند، بنابراین احتمالاً بله.
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/67524" target="_blank">📅 17:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67523">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f96f01d100.mp4?token=pCi2oSilWDdanGHNCqTEpZGMYsJslJCzQhi2KuvvrdsiRIpVCxF1yoKX8GoKFYXHD5tF4HmJaStGNBoY_e1_VEt_Y1U8JtAAtZmdHWCZjyor2mxsZd1iDxvoO3u_GH5MgEwAQGvMxYMnzAisG-omTb4VmRY408tQymebK2xFYn83LTZip5MG_LwsUB-jF2AKys90rNbwvNb_uwFlXhbjXHWC7G84rXvR-ClW5XVgChStVS5Muf2H8xUZ-urpih9LKlfiwl4TzbGnIZ5yskVJK6ZylArpDbsfajTIQhgd9Bt9HPjI_waBG4GiruH81ucw0spwihcZRxsqxhwECrSD-A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f96f01d100.mp4?token=pCi2oSilWDdanGHNCqTEpZGMYsJslJCzQhi2KuvvrdsiRIpVCxF1yoKX8GoKFYXHD5tF4HmJaStGNBoY_e1_VEt_Y1U8JtAAtZmdHWCZjyor2mxsZd1iDxvoO3u_GH5MgEwAQGvMxYMnzAisG-omTb4VmRY408tQymebK2xFYn83LTZip5MG_LwsUB-jF2AKys90rNbwvNb_uwFlXhbjXHWC7G84rXvR-ClW5XVgChStVS5Muf2H8xUZ-urpih9LKlfiwl4TzbGnIZ5yskVJK6ZylArpDbsfajTIQhgd9Bt9HPjI_waBG4GiruH81ucw0spwihcZRxsqxhwECrSD-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
انگار یه نسخه پرمیوم از ایران هم وجود داره که فقط مخصوص پولداراست.
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/67523" target="_blank">📅 17:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67519">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hqmCKBTfBHQxhA0cxFao1BqlMGh_ojZxgSLNjIf5fOH_RjR26wX0napGntfOZI7tJTOeTA2mbHYF2yRJmIHwuR8YjKlDduUV-lgwYhQLP208RCcYDxY3GcDRZEmL-Co2XxSRivro1PgeeDDg538R5mnyfnR3FZ4csYWeeiBdIG5qifTqo6x7EeywLV6-ZDmZQy8bJtpIBobUebIAgJif2G3qBloA6tUO_pZGFijiUCAf8DziKc2c-5nk33yFNZE-WX6EUc3n8afJR9hCiuGTJ_tm_Sxpx3t4KIRdmMXwtjodYf7iSat3d_wIVmsFgD2j31gW6U3armDq5dFHrkaoMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41735c920b.mp4?token=Ho2T5JmrNz8-HZ2VTDT7JFuiwOxeXAK1bzUWJH9Ic-c5UXRhFl9MvhRAWWYEPBysTtGm2kw2EFZHsSAFaAbzG78p71P4aqq36bnQvNa6CXUVVyG5jkWA6Hjn1FroOMK0YvhsrEW0mF-Dp0f_mm0_Bl_1cWxHmqFL6guZs8sB7QAO76UIhqivBBFTl30EMFOROOKQZyOLYWoJnJfudvMWqYfYNfkdfsqpUbwSprHzwI2TZlVYGb8AUka0DsJxcmj1dVo-q9tUnauu1DepQ1h-KA5gU78mmK1eqT9xsM7fqjpuRuecwjwiEJKq6xbFo10bhsAQo8YKKKbssD_mClTHhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41735c920b.mp4?token=Ho2T5JmrNz8-HZ2VTDT7JFuiwOxeXAK1bzUWJH9Ic-c5UXRhFl9MvhRAWWYEPBysTtGm2kw2EFZHsSAFaAbzG78p71P4aqq36bnQvNa6CXUVVyG5jkWA6Hjn1FroOMK0YvhsrEW0mF-Dp0f_mm0_Bl_1cWxHmqFL6guZs8sB7QAO76UIhqivBBFTl30EMFOROOKQZyOLYWoJnJfudvMWqYfYNfkdfsqpUbwSprHzwI2TZlVYGb8AUka0DsJxcmj1dVo-q9tUnauu1DepQ1h-KA5gU78mmK1eqT9xsM7fqjpuRuecwjwiEJKq6xbFo10bhsAQo8YKKKbssD_mClTHhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حملات موشکی شبانه روسیه به اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/67519" target="_blank">📅 16:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67518">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-D2AEHQGhfMJv5TEhcYCU84kypFrb3V-KKRuZ9OxgJh7bjeIgW8Y55-5QdPsY1Sbr2CaP3eSYUgfjNw4GXZfJlUMrnECJ2bBRBAvPagbr7mj2LyI8RbvPNdKQOcwVZQMSErVGFiN1kWnRBM26TU-eFzuIrpcBa0_9greRXMtZBvkp3cFOOxLIpk0qlgVlF5YE9XVHGFOBgTUWUosJss_ZetRpgMJ8gYnybBdwL-P42UKdhzAsZjFQFgeXheCIJzE7pt0QcYVzlqfhcsqQl5_MquXIg5JqzjlA9IJkteqg8AxU7d005VPvE6ysn45ydr55GHB5dUmVojx00YF9wBZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری هادی چوپان
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/67518" target="_blank">📅 15:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67515">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cM46MiW1Cpa4OBR27C9eq5_kHYiqoTqX8l-37VvRTY0XnbAmQSp4bWSE2V5rxgWs9oRUZu1OOkhFfd0qYczEbIXF98A4o95nOMQuoEKUmpuWVksWwzatLtDGfBnoGavm0BJs6h36whSEjTy7KzyEWssFdF9AjW5E6d5zLc3nr42i02StpqvbDvNiU4zjEz5P5NEaHMGxXKH9o5iHHD1528TzmU9kPEAU6BinLnsBimi0nTWN8JMzYe4nn28w2hWl4CFLhbjcL6Ke8I-aGVYP68lHnKifJN72lzILT7rHrS_3vUP5M2cyQCY2jEbrecp_dPihH8_OOcMMIqePUpTjcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OiXJAhHKn2_6vJ5D40PUb67u8D6mYbJWbSKMLZPZ--DTT4eNhfn_jrIa6fMrUvaw2otC70cWVhf0NruDaGURXg9lWjCVSPNtKVj1Xhk88N2RnMcIUNVYbE8UD9JZkZwQ43h0YyY_68rsWfRp4kyGuvnsXsn3XhOWUOk5Qkqnskx6CUTiBH2-yp5_7Ruu6_bxgmqhnXTg6F7eGA-BvZqfLSkDpN2jrla4MJlYZuMbtrL0zLpuWyS3oDYXOGqAs3pQlnFc3fJ8lBB6obzioMQd9RU25GIr6RHdJkoBrAhO2yP_ojLVZCk4aF_dVLthVWwyorggz_9BY3EFlnrcU4-YtA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2e58f00c0.mp4?token=XJW_qDfjJoecw6SWjcxMzXbXzV4xTdgwFVJ4mlAFbwW1gEZ5ZkuronpRbVAIh5wER0wJA3ffXGw5SvF-KKS7kGbSoS4YrJ-EoXdg8cD0O405zze5p26CRAyjImVJUzH-Z5FyNqHnwzz7VjhHuwvpbYuMZIggGTNyZrjLUp-bWtnImk8N8j_h00hQvKr3LWZucttdMUcs8Z4bBLu3k4NohxDb-T6OOpXfrxkvqVC4Vwu3cEJlA0Xo868WVId2su5pxEstNDpGYpYwRyFVVbmea69kO2NDsqKSHIU6l5M9gXJlaCn0XV3S3_X6pbSA0hNxYNSKS31Gg5RraI-sUW8QUYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2e58f00c0.mp4?token=XJW_qDfjJoecw6SWjcxMzXbXzV4xTdgwFVJ4mlAFbwW1gEZ5ZkuronpRbVAIh5wER0wJA3ffXGw5SvF-KKS7kGbSoS4YrJ-EoXdg8cD0O405zze5p26CRAyjImVJUzH-Z5FyNqHnwzz7VjhHuwvpbYuMZIggGTNyZrjLUp-bWtnImk8N8j_h00hQvKr3LWZucttdMUcs8Z4bBLu3k4NohxDb-T6OOpXfrxkvqVC4Vwu3cEJlA0Xo868WVId2su5pxEstNDpGYpYwRyFVVbmea69kO2NDsqKSHIU6l5M9gXJlaCn0XV3S3_X6pbSA0hNxYNSKS31Gg5RraI-sUW8QUYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
با اینکه تو ایران با سنگ و چماق میفتن دنبال عباس و میگن مرگ بر سازشگر ولی تو عراق اینجور نیست!
مردم عراق انقدر عراقچی رو دوست دارن که اون رو تَبرک میدونن و خودشون رو بهش می‌مالن تا حاجت بگیرن!
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67515" target="_blank">📅 15:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67512">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lYX8ZVxgRUvmqfZSN_rF9weLXn1czU6J2mTEudGq3YB48lp_AY-AHUNv9r1OQxk3yZwSi8UJI9EuJV7k6l2smmHVwae0I8fLCxZqqbv8fw6PH3NmEoHPjeG0aBIk0P2ot0huPSr7pLBB-dipGzlAaCZTlGjxmLgCl--iLQ0z-ZZvT4TkaWi5j8rl9dNuFTZk7g2XbDRua0FOoFmLciPwvMoqeQhQWUIdmHolv-xRWz1zo-FCeulo2MTPSP0TFzhESbiZW3_zNRsBl-8p6aM135yhteGJmSQ1aecOVgplJH0kKKNVDf1HfUQGGbw3A1NzFMfkkVzGRSZ9-cG2j490bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AZNi5ukdFZ8C3mPjbKDLcNCJHLviXbfKUgZvJXnwUA1jShb3qWcOPbY4IJlcwichFlWnxmiMjEAG0VJyJ1ADCHovnxr2ZX7QLOqLbQ-r0l46ZTW72GAtQVbBPwlZMeyi_XlWTAkQRBWNFBzMzFtdMX8F1egRV220qN45mLx9q_ENO0XS6Dki2oiER-MvNMA0yhiLKGLBZHceBTjcGjFarYwE5eCpsBBBVo2yzWXUKmu1ys0Sk_UeDSzpqL_-WOdMfh8fCQJd5n1B1ejuY1CYXQ4APW7qY7YWOP8rcbdr1YdVy_h0Xsjw067sZ61cP4Y2Z5CROnzoTAJZJlOyXZob0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tZ_4VIAlxMTvmS7QELmRHY7hyJzHhQccH773WtTTaTUT5MyB8DYWxoiprp_dOXg3CYOr4u-ad277JExF6OwtG0QWiOMSxdtwspNMZoDCDSDF5uB_SdGFrMKJIGp2xBe00NMsmN7U1hFImoanRNreNqDT6eX6mGGBJ1DrZnwIHZ3sfGCzTfDPMP5EFlklNU6EaZUI2gITKVQzfVFrzSxS7X5QTlo1BXA8p6O3MI-Q-0jiO3sjfYk57kA951JsNhUfFq_X-MnMx7NToI6QIY0CpOzezoH5E1e-WcCYIIEE_tk91PcyK6jBPZ5Xi4hHkCFQ-E-ZwIG6Y588QtFiqXWb0w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
خبرگزاری تسنیم اعلام کرد یک پهپاد تهاجمی MQ-9 آمریکا در آسمان بوشهر سرنگون شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67512" target="_blank">📅 14:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67511">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/763cc26dcd.mp4?token=cWFuCrC9lQ6MSyTUEbQhLOE-JvqLg3C552N7vxit_7Kwp16y0_vQnr2uolVbruco36DMIhGWsOLJREyv8-siZJNMnt5wd6Sv-oTh-ol_0rSfF27o-IvKyCNqyHHQHYm-hp0Ge4CQAbuY4sFS6ea7QkTkj7gcqfSzNKupblzi0f0xwEVNzEr-VqxB4clA6lNuMc6FKMuu045KpiWW_o-7GxBPaKk_XWtcovbbZlJif_3R9tOMt95tqXafE-95TocR1Lcyenv5kSZcPsrSySQIi9xpU_mUthnNv7CIqT6wB17I4S6DQkoBeDPvuk6NwRZwRHtvluPQvDmD2QXNZSllQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/763cc26dcd.mp4?token=cWFuCrC9lQ6MSyTUEbQhLOE-JvqLg3C552N7vxit_7Kwp16y0_vQnr2uolVbruco36DMIhGWsOLJREyv8-siZJNMnt5wd6Sv-oTh-ol_0rSfF27o-IvKyCNqyHHQHYm-hp0Ge4CQAbuY4sFS6ea7QkTkj7gcqfSzNKupblzi0f0xwEVNzEr-VqxB4clA6lNuMc6FKMuu045KpiWW_o-7GxBPaKk_XWtcovbbZlJif_3R9tOMt95tqXafE-95TocR1Lcyenv5kSZcPsrSySQIi9xpU_mUthnNv7CIqT6wB17I4S6DQkoBeDPvuk6NwRZwRHtvluPQvDmD2QXNZSllQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
احمدی نژاد : بابا داره بهتون فحش میده،یه مرد بین شما پیدا نمیشه پاشه حداقل بگه خودتی؟!
+ترامپ امروز به مسئولین جمهوری اسلامی گفت آشغال،پست فطرت،کثیف،تومور سرطانی، شرور،بی‌ کفایت،بی ارزش،بیمار،روانی و حقه باز
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67511" target="_blank">📅 13:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67510">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
رسانه های عبری:
ارتش اسرائیل جلسه‌ای با فرماندهی مرکزی آمریکا برگزار کرد، به منظور آمادگی برای از سرگیری جنگ.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67510" target="_blank">📅 13:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67509">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H3zXFJY_xAH1WH6qmgQNtmtRz0kBfo-RDdNLHzlmJPjB9KpFnkmp5Bb5AI-HgX3b_7KnFufpz94GOhwnC0_08TyJUxfJt0E1nO6h54ZqKGx2jxStIQFpds3E4ytwVmxkSm_H6h2uFMmwAd7wafCuGYsUc9EQjBRlJWYBiEkRqQm4biSLReE9qCU40gNoQ9g7a3ecNDm8LsdQaADJFqAtdDadUEAPSE_RlQlUsOxviz7K_WfBKus3sqw9IFEN1G1N7c8BAIxgqH1JBgsSQz2ZdjLnNS31c7slywlKdU6aRC0d_JmmQbYOri3rxJ34-XuFOrFWLMtBsFN4dMJp8F7rMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
پزشکیان:
رفتار دولت ایالات متحده به عنوان میزبان جام جهانی، همان سیاست خارجی همیشگی آن را نشان می‌دهد: زیر پا گذاشتن قوانین، زورگویی در برابر رقبا، ایجاد موانع و تقلب. این همان روشی است که آن‌ها دنبال می‌کنند. ایران چنین بازی‌هایی را رد می‌کند. ما به طور قاطع از حقوق خود دفاع می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67509" target="_blank">📅 12:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67508">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fupiYtxG4mx4I3Yqu9KHB5QWgpAbF9CmiGfcZ8qxpaPei7QxI9ES8MLQrSK7iRrFE9X7CRPTUFzD6D9KMITv46mBcar0C0_51Jj0UEOkdx1ooaOpqDiLfrG_vJYXOvvhqyP4II9A_4arGh-5mMkBkJMLhQ0f9vpzG7CH7E0UVK9x333E2b3fScKBNlI-wstzm-VsF2qc_0PfNEzS8Myg270O9YUj-9sny6Swd_Tf7Y94g-GDgTqVjbnyT8d8PvbzFd5MMls6Q09HbUGMQwBf8nMScgM32SamOVMLBs7ViX8L3TcEHbpXkG_jLEQPyA8RGRjZCWDskshVC-2Dt86OjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آمیت سگال:
پیت هگست، سفر برنامه ریزی شده خود به اسرائیل را لغو کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67508" target="_blank">📅 12:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67507">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ:
«ما دیشب به آن افراد بسیار خطرناکِ وابسته به ایران، با قدرتی بسیار زیاد حمله کردیم... یک مشکلی در آن‌ها هست. ما می‌گوییم: "بروید مراسم عزاداری‌تان را برگزار کنید"، اما آن‌ها به‌جای این کار، دیروز شروع کردند به شلیک موشک به سمت کشتی‌ها. بنابراین دیشب خیلی سخت به آن‌ها ضربه زدیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67507" target="_blank">📅 12:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67506">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb70977fa5.mp4?token=RWgD2fXgEwxdZQcDzyZHTyiCZxLIY909Co8WAlz7Fy8TgRqYDiFJQwDOPW8LPioS6GHSF5CAzPFD3uTq06X1FherPEE2df-yq3FVesukOBiYkXBMh5mzfx2om5c9tfW-85eEgl0VgoloRqlAomQ0OnnLX06jbqnCEIbP1ZTFC9839lfYC6WIxK28MEf8itE_Qi8FK7ibbEhlp6duhCyH8vBiE77rbhs-W_L3NTC7qo_BM6aUXldDRPn_tO5nQMfkw0YVlrUUg9S9ICXz-w-UP26jHGSglkmukQX73DjzEnUCJ0P9EeepZ4TBxHWo1sQw0V6wGlu-_hOwpk-qQEyvng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb70977fa5.mp4?token=RWgD2fXgEwxdZQcDzyZHTyiCZxLIY909Co8WAlz7Fy8TgRqYDiFJQwDOPW8LPioS6GHSF5CAzPFD3uTq06X1FherPEE2df-yq3FVesukOBiYkXBMh5mzfx2om5c9tfW-85eEgl0VgoloRqlAomQ0OnnLX06jbqnCEIbP1ZTFC9839lfYC6WIxK28MEf8itE_Qi8FK7ibbEhlp6duhCyH8vBiE77rbhs-W_L3NTC7qo_BM6aUXldDRPn_tO5nQMfkw0YVlrUUg9S9ICXz-w-UP26jHGSglkmukQX73DjzEnUCJ0P9EeepZ4TBxHWo1sQw0V6wGlu-_hOwpk-qQEyvng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره مقامات جمهوری اسلامی:
آنها دروغگو هستند. ما یک توافق می‌ کنیم. همه موافق هستند. هیچ سلاح هسته‌ای. ما یک توافق می‌ کنیم.
آنها به بیرون می‌ روند، با رسانه‌ها صحبت می‌ کنند و می‌ گویند که ما حتی درباره این موضوع صحبت نکرده‌ایم.
مشکلی در وجودشان وجود دارد. آنها دیوانه هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67506" target="_blank">📅 12:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67505">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5877eb817c.mp4?token=Lj4aZx0Yl6jm7x4srmsOhrAhbVUF_nFAb6jQOAG5CrdoF8L_kF-UPD_3cKXMsEAw4wzLNOIAR-uXIS_etbFJUZPbyeHvwfYDJI4txt1N3Ga6GKCmiTuGTkljrhApeTVo727NSIx1iCdtVk0WndS_XBND-JUnxuK6aG6tL9Qennkx3ASqLKFDkxrWHeKEjWGqPli8UbPC3TkHojJ5elQ69syiS8jwYF2FLn96cbtDaeqTTqR2Cr291SI7P_CpU76dNIvA5clZoV7gW2weI9jkOyyqUNiD_yt1-0nf6PRS8l2yJnvu0WwJmJVlm9J67spJjuVQjFn5lrryj1WTwYr1zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5877eb817c.mp4?token=Lj4aZx0Yl6jm7x4srmsOhrAhbVUF_nFAb6jQOAG5CrdoF8L_kF-UPD_3cKXMsEAw4wzLNOIAR-uXIS_etbFJUZPbyeHvwfYDJI4txt1N3Ga6GKCmiTuGTkljrhApeTVo727NSIx1iCdtVk0WndS_XBND-JUnxuK6aG6tL9Qennkx3ASqLKFDkxrWHeKEjWGqPli8UbPC3TkHojJ5elQ69syiS8jwYF2FLn96cbtDaeqTTqR2Cr291SI7P_CpU76dNIvA5clZoV7gW2weI9jkOyyqUNiD_yt1-0nf6PRS8l2yJnvu0WwJmJVlm9J67spJjuVQjFn5lrryj1WTwYr1zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ:
به نظر من، ایرانی‌ها ناکارآمد هستند.
اگر کارآمد بودند، ۴۷ سال پیش یک توافق انجام می‌دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67505" target="_blank">📅 12:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67504">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48d7e6a047.mp4?token=gVAW_okXoGDK0i_CNq2LhPckopg8i6n-UnRTvz1zK_6REARX4X7ky0TBFY8-MljC2rT24P0KYAEiHRiIpNM8eAzuEPLddAeRxgZ5YKBlkvErg6YAtMTPDFSK2DCBkal4ap6GaRgDVKCrqoYPldDXo50uMqzsoN3SUsRzYbFb0zTSBb7Of7Yjy2fjeHfvdwQOyNrZ7HGNy-W14kVCJFY_XZeONFuWCSqjlZ1MOwfi6CAjJ7tm_rSdGh_Kn-WwriVjAFnZq3H35UB_SoDr_-Tv4kxUqiWpSvq2zRHTwVKCTnNJcO_9R8vU2fvMJ-Dg5DN-DkTy-de4QjwwrQRDVxKhnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48d7e6a047.mp4?token=gVAW_okXoGDK0i_CNq2LhPckopg8i6n-UnRTvz1zK_6REARX4X7ky0TBFY8-MljC2rT24P0KYAEiHRiIpNM8eAzuEPLddAeRxgZ5YKBlkvErg6YAtMTPDFSK2DCBkal4ap6GaRgDVKCrqoYPldDXo50uMqzsoN3SUsRzYbFb0zTSBb7Of7Yjy2fjeHfvdwQOyNrZ7HGNy-W14kVCJFY_XZeONFuWCSqjlZ1MOwfi6CAjJ7tm_rSdGh_Kn-WwriVjAFnZq3H35UB_SoDr_-Tv4kxUqiWpSvq2zRHTwVKCTnNJcO_9R8vU2fvMJ-Dg5DN-DkTy-de4QjwwrQRDVxKhnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ درباره ایران:
من در تمام لیست‌های آن‌ها قرار دارم. و تا به حال، فکر می‌کنم کمی خوش‌شانس بوده‌ام، اما شاید این خوش‌شانسی برای مدت زیادی ادامه نیابد.
چون این‌گونه است که مسائل پیش می‌روند، اما ما افراد بسیار خوبی داریم.
اما این‌ها افراد شرور و بیمار هستند، و ما باید از شر این "سرطان" خلاص شویم. این "سرطان". و شما می‌دانید چه باید کرد؟ باید "سرطان" را در مراحل اولیه از بین برد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67504" target="_blank">📅 12:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67503">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ در پاسخ به سوال یک خبرنگار پیرامون این موضوع که آیا آتش‌بس و توافهم موقت تمام شده یا نه، پاسخ داد:  فکر می‌کنم تمام شده، دیگر نمی‌خواهم با آنها سر و کار داشته باشم، آن‌ها پَست و بیمار هستند، رهبری‌شان دست آدم‌های بیمار است و اگر سلاح هسته‌ای داشته…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67503" target="_blank">📅 12:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67502">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/385c5453ef.mp4?token=hUwn__6QnExfZqcoddIkF2L1-FsOi1aEvghjXSrKa_-kllSiRLKYyGKVyqRU0nRr3AuM8y-spsfaFjyNX23qJxw8SNEldQO1VOHPON4_BlRxjOEkhbkE890NyZPWqRD6G-jHY-ZCLhKWUX4af_8wLGC18QqW9kWPQ_YP2oXXIFagmO7KOI1pmJ1eFfRJDezNTaH93l04BjnJ7ZwtoK8zTUeCYnujYij-3g5EMb7vRUJ7sZ5t_AuAbAftVF8WbGVDxkWBPauDCjtPxKUlPpvTdFU2uS8g1uNHnnjCdI8Z2Jdn-F12sTgXGiulaxXwuOTYLmkrU89S1Kj79EJFsvzrYIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/385c5453ef.mp4?token=hUwn__6QnExfZqcoddIkF2L1-FsOi1aEvghjXSrKa_-kllSiRLKYyGKVyqRU0nRr3AuM8y-spsfaFjyNX23qJxw8SNEldQO1VOHPON4_BlRxjOEkhbkE890NyZPWqRD6G-jHY-ZCLhKWUX4af_8wLGC18QqW9kWPQ_YP2oXXIFagmO7KOI1pmJ1eFfRJDezNTaH93l04BjnJ7ZwtoK8zTUeCYnujYij-3g5EMb7vRUJ7sZ5t_AuAbAftVF8WbGVDxkWBPauDCjtPxKUlPpvTdFU2uS8g1uNHnnjCdI8Z2Jdn-F12sTgXGiulaxXwuOTYLmkrU89S1Kj79EJFsvzrYIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ در پاسخ به سوال یک خبرنگار پیرامون این موضوع که آیا آتش‌بس و توافهم موقت تمام شده یا نه، پاسخ داد:
فکر می‌کنم تمام شده، دیگر نمی‌خواهم با آنها سر و کار داشته باشم، آن‌ها پَست و بیمار هستند، رهبری‌شان دست آدم‌های بیمار است و اگر سلاح هسته‌ای داشته باشند از آن استفاده خواهند کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67502" target="_blank">📅 12:09 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67501">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/COF4plhqxkDMxsYoPASMIvkol6TiuHCCKZbuA35ch8_wyqXrXiTp4zz8598wCEiZuFIuy0Elw-EyqM1cimGANwmZG0HgJVrprufNFIP883XW8dTO3OM9hrvZ1XnPpNLNwzGK2o6rvjppj80mAaHioqLfTV_ROgnrQ7ickGM1QiH4wbIs3ifNpoa_Dhf-qxM4_ZV5G3YiN-V3xNB2J2GvFnYdqvlGVMxda8wbHYxR_fWnt6QGkTE5ZhE8e49RFyfi7bfu6hVvyvw2xOn8H9bCtxB8i2VqUfSQEKvAc2PDsd1HfdSRNMvQfo299bdZapaOyDTRunE-uCCQAi4Ytmyp1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بعد از حرف‌های ترامپ، قیمت نفت ۵ درصد افزایش پیدا کرد و به بشکه‌ای ۷۷.۴۰ دلار رسید.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67501" target="_blank">📅 12:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67500">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b7bb2fcec.mp4?token=mACrVDML_KuGzUnB1ue_nbfsdh2hp6DJw5zRLoVJ4U70rB9ppZK3AheeDKn81TOcF-EtoxFTDwxeq8QUCd0e0w_aUktGoxc_Lw2ZWiVSfhPa_R3hwWbPL2U5LDLc-JvEliWRV72JfITvo0OxP0HntOZAtBQ4taVfrkNLW3pKWU1k4mM4lLc0ACh7lQpJBUuk3BBK0rmpBf9CX_y3Hn42Lyt3YD7SOSGNz-aTsxR1dgy5FPP3syV4dg3hPr5KDjz098SEDwtfWvvRJQKXROjRrB0sOHPVdrFoVcx2YUr6vvrN47JWOhXJhoyW273s5TjglUF4UM6PZE_yzzJZWmZ92KG97NLvV-22Qde1KgoNk4b3JaWdQvJxH3Pm7RomdFnsrLCruay9Rn5RV2rGw5Ky45FasQU99oM3CC85_KIwXHHt_0Z83P1n1vMiK6pRx9ZB8fxVFvKugBdfxvsqw9tkoK8wN4z-3iRNw03Nxlqw7yYTl_-NevaiizIgQQY8srh53Wrgffri5IbklbNJRzx7BVfcuHGbxfXVii5VYW9jBO7OsrxNk6_5mJS9EXIRhhiDnkipM0-QRuAjfg4neuxYwGT5TWQwyyFQsf8Wo3NHtTB6U8FL0eTQUpemBzbWUoeEPuw0jThGbYCESd1d7ZL6ZwAeCg2vJuhJRtR94fHfaM8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b7bb2fcec.mp4?token=mACrVDML_KuGzUnB1ue_nbfsdh2hp6DJw5zRLoVJ4U70rB9ppZK3AheeDKn81TOcF-EtoxFTDwxeq8QUCd0e0w_aUktGoxc_Lw2ZWiVSfhPa_R3hwWbPL2U5LDLc-JvEliWRV72JfITvo0OxP0HntOZAtBQ4taVfrkNLW3pKWU1k4mM4lLc0ACh7lQpJBUuk3BBK0rmpBf9CX_y3Hn42Lyt3YD7SOSGNz-aTsxR1dgy5FPP3syV4dg3hPr5KDjz098SEDwtfWvvRJQKXROjRrB0sOHPVdrFoVcx2YUr6vvrN47JWOhXJhoyW273s5TjglUF4UM6PZE_yzzJZWmZ92KG97NLvV-22Qde1KgoNk4b3JaWdQvJxH3Pm7RomdFnsrLCruay9Rn5RV2rGw5Ky45FasQU99oM3CC85_KIwXHHt_0Z83P1n1vMiK6pRx9ZB8fxVFvKugBdfxvsqw9tkoK8wN4z-3iRNw03Nxlqw7yYTl_-NevaiizIgQQY8srh53Wrgffri5IbklbNJRzx7BVfcuHGbxfXVii5VYW9jBO7OsrxNk6_5mJS9EXIRhhiDnkipM0-QRuAjfg4neuxYwGT5TWQwyyFQsf8Wo3NHtTB6U8FL0eTQUpemBzbWUoeEPuw0jThGbYCESd1d7ZL6ZwAeCg2vJuhJRtR94fHfaM8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ درباره رهبران ایران :
«آن‌ها دروغ‌گو، متقلب و بیمار هستند. به مردم خودشان آسیب زده‌اند. تا امروز ۵۴ هزار نفر از معترضان را کشته‌اند.
می‌دانید بعضی‌ها می‌پرسند چرا مردم حکومت را سرنگون نمی‌کنند؟ چون دیگر زنده نیستند؛ آن‌ها را کشته‌اند.
مردم سلاحی ندارند، اما طرف مقابل مسلسل دارد و آن‌ها را به گلوله می‌بندد. رسانه‌ها هم این را پوشش نمی‌دهند.
اگر مذاکره‌کنندگان فوق‌العاده ما بخواهند، بگذارید به گفت‌وگو ادامه دهند؛ اما من امیدی به نتیجه نمی‌بینم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67500" target="_blank">📅 12:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67499">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ :
سران ایران یه مشت آدم کثیفن. اصلاً ازشون خوشم نمیاد. کلی وقتمون رو باهاشون هدر دادیم. بی‌عرضه و ناتوانن. بهتره فقط کار خودمون رو انجام بدیم.
اونا می‌خوان رهبر آمریکا، یعنی من رو ترور کنن. سال‌هاست که من نفر اول لیستشونم.
باید سرطان رو از همون اول ریشه‌کن کرد. من این‌طوری به قضیه نگاه می‌کنم.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67499" target="_blank">📅 11:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67498">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ :
من دیگر نمی‌خواهم با ایران سروکار داشته باشم. افرادی بیمار بر آن حکومت می‌کنند و از نظر من، این پرونده دیگر تمام شده است.
«از نظر من، تفاهم‌نامه تمام شده است. دیگر نمی‌خواهم با آنها معامله کنم. و اگر سلاح هسته‌ای دارند... دروغگو هستند... به نظر من، ادامه مذاکره با آنها اتلاف وقت است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67498" target="_blank">📅 11:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67497">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ایرانی‌ها رهبران آمریکایی، از جمله خود من را هدف قرار دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67497" target="_blank">📅 11:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67496">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
🚨
پرزیدنت ترامپ:
این‌ها گروهی از بدترین افراد هستند، من آن‌ها را دوست ندارم. ما وقت زیادی را با آن‌ها تلف کردیم. آن‌ها اصلاً نمی‌دانند چه می‌کنند.
آن‌ها مثل سرطان هستند و باید این تومور را هرچه از بین برد. این احساسی است که امروز دارم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67496" target="_blank">📅 11:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67495">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
قرارگاه خاتم الانبیا:
هر نهادی یا مکانی که برای حمایت از ارتش آمریکا علیه جمهوری اسلامی ایران مورد استفاده قرار گیرد، هدف مشروع نیروهای مسلح تلقی خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67495" target="_blank">📅 11:27 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67494">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ea62c3daa.mp4?token=GGGQDgk_AMWqvyyUysfVTojD40-f16Zac5Fpp00gcXI0p1Xpc3Dvk1mrO1_ilGu03YdI4B_O74K9sep4ojUAjs0MPjflxVuIpOQJGmZa083PuwykcPWmpM_giMBvWSE3-TH0TFfao0_uEy5naYiy6VW131eGv5Se31TfYGVcVXVH72IctiNu_nOCakUKahEC0213l2-L8B5tRZNdct8ngC-gkO6FyGc72dByKoaFiuyOOwnkLiZV0lmV6Vg4FZyvV8E-TTPqcmt3Za7yeyg0CPwzzeYI9SJ0tHwVdLbtVVk--NtMO1EZFqvW8l9m-zI2eZL-Il-_RdYRRSHEJlNG8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ea62c3daa.mp4?token=GGGQDgk_AMWqvyyUysfVTojD40-f16Zac5Fpp00gcXI0p1Xpc3Dvk1mrO1_ilGu03YdI4B_O74K9sep4ojUAjs0MPjflxVuIpOQJGmZa083PuwykcPWmpM_giMBvWSE3-TH0TFfao0_uEy5naYiy6VW131eGv5Se31TfYGVcVXVH72IctiNu_nOCakUKahEC0213l2-L8B5tRZNdct8ngC-gkO6FyGc72dByKoaFiuyOOwnkLiZV0lmV6Vg4FZyvV8E-TTPqcmt3Za7yeyg0CPwzzeYI9SJ0tHwVdLbtVVk--NtMO1EZFqvW8l9m-zI2eZL-Il-_RdYRRSHEJlNG8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
محسن رضایی:
مخالفان مذاکره صبر کنند، خود آمریکایی ها آن را از بین می‌برند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67494" target="_blank">📅 11:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67493">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌های غیررسمی از شنیده شدن صدای انفجار در بوشهر  @News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67493" target="_blank">📅 10:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67492">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6356a25b5d.mp4?token=OOXE1c6ArcWtwn9C-VHZvkgJufaNlkE6kreqmwz_voj_MtlaALplU0bi-pfXGf_9jvPmd1ANd66uYYwm3-EwatZVoO_VmrJDOFgP46BZCQdrbFv6bd7FuyM9ohKTWT95vTp_kTMBO5FBFLT5onTQOCUi9tWL4Pjj4O1441UsgMHsSWRVl6J_1lA7osJRdKzrNUvnuEQVa4biuPK_Lo85YQePUB6ECKgsqSfG6veFMRiPkkczE69M-ShRyQM0Z-o6EpJXzYPOdLltfxoapFSldrZd-Y2SHgl3gVkGPApkgf5gYY5dHL02VsTLTmPmWFRPYmBdHhwV8eoRBl3n7MsVvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6356a25b5d.mp4?token=OOXE1c6ArcWtwn9C-VHZvkgJufaNlkE6kreqmwz_voj_MtlaALplU0bi-pfXGf_9jvPmd1ANd66uYYwm3-EwatZVoO_VmrJDOFgP46BZCQdrbFv6bd7FuyM9ohKTWT95vTp_kTMBO5FBFLT5onTQOCUi9tWL4Pjj4O1441UsgMHsSWRVl6J_1lA7osJRdKzrNUvnuEQVa4biuPK_Lo85YQePUB6ECKgsqSfG6veFMRiPkkczE69M-ShRyQM0Z-o6EpJXzYPOdLltfxoapFSldrZd-Y2SHgl3gVkGPApkgf5gYY5dHL02VsTLTmPmWFRPYmBdHhwV8eoRBl3n7MsVvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
مستند حملات امریکا به جنوب ایران
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67492" target="_blank">📅 10:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67491">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
شنیده شدن صدای انفجار به سمت پایگاه هوایی عیسی در منطقه صغیر در بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67491" target="_blank">📅 10:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67490">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HQgKKQykbGT9cGQK96hIBbBwh93FDo_YVUkZAXdy1QwD9C7cEstkP25UykSwsI6ImAgnKnsNllj1VrZnc8Q_sgM2A0b46noclsfgtn1M2Kn9_YIdTVoj_3LrhoRddSSEBGZDMYUWmxc3QXABns3Xn2TupU-gpdWz0oVDSjmWNJe7bAWToy4FQhFQZNRNXaBhTGp3UWQQHvXOuw9CiM9q4v-p4lLV5plQ3yQwc6SmIUQHnVTguhJqQijnR530ZYhShRRJAJMfJ0aRoECcIgk9UKmciGLCvbhB1EpAa4-Ry3-MwXfrQ7BCiKPdk2xJQ02wt011CstuXu4DdnDd38WFOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قالیباف؛نقض‌های عمده تفاهم‌نامه توسط آمریکا:
نقض ترتیبات ایران در تنگه
تهدیدهای مداوم به حملات بیشتر
بازگرداندن تحریم‌های نفتی
حملات به جنوب ایران تداوم
تجاوزات صهیونیستی علیه لبنان
دوران زورگویی و باج‌خواهی به سر آمده است. این مسیر به جایی نمی‌رسد. ما تسلیم نمی‌شویم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67490" target="_blank">📅 10:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67489">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OlqF16OE2tUIlbUMv-q5Q7KEMN6ElOhFSpFepbUlUh8esqGRWhVWqoK6E6VFIApCwn-nQ6nve71DuvEzS81EFg7DJAbr6SamRn3_izwU9TnXL9VGI2qYmttimrQYgFODacT8wRTgs51yk1kjRx_GnMp1fYeE_ViY6vW7aKO0erOxgybqbBrpRnPHHU3qWY3015ixKU0Qn2X8K3Od-Xl8ejZjCOaTDPrS4ckZ175TxAnNbRM_LbeBEdc1qcWbjEQXM3Kt0bp4h9Se6Q-TqXQ_3GuyZi1y3lBocAol3ASovEPBtteKcOQfYhs1l9UT7pu6-qAhlRGkERcHhobxt6QHPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
یک هواپیمای آمریکایی مدل P-8A Poseidon که در حملات علیه ایران شرکت داشت، امروز صبح نتوانست در پایگاه هوایی خود (پایگاه عیسی در بحرین) فرود بیاید، زیرا این پایگاه مورد هدف قرار گرفته بود. در عوض، این هواپیما در پایگاه آمریکایی واقع در عربستان سعودی فرود آمد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67489" target="_blank">📅 10:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67488">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای انفجار در بندر عباس
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67488" target="_blank">📅 09:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67487">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌های غیررسمی از شنیده شدن صدای انفجار در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67487" target="_blank">📅 09:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67486">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9920364084.mp4?token=qOtZUtoPKrQFTOo_k_zZ5X0brR3Ioea9s8sRyqdDuclIUR-eVeb6pJ_rGHITJZ2gNzt-doud8lxAZiDOLk2Rwd4-PSD0FaRb5pRYZ5d65YlXGKqodESk9RVgvJ1DMk9ac7pGnu88FeQu5BhCzhPckyR02KGvoKAziAxSdfuxsCXWVcBSiIEcyI7NgJL5EQyUki_o5fF544i_4BhEWICbuH9OzDfMEGmovbgXfr8Dg5XuPPPrXI6_W-D7M5QOg2RM4AwFhEWC7TlWMvUKFN3pGXar4WbM8Jimw_eTA-u9A57LHWBO-UThxZNmRIcNl-uNrXZ5RZQNpqS47o8ZVUpIUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9920364084.mp4?token=qOtZUtoPKrQFTOo_k_zZ5X0brR3Ioea9s8sRyqdDuclIUR-eVeb6pJ_rGHITJZ2gNzt-doud8lxAZiDOLk2Rwd4-PSD0FaRb5pRYZ5d65YlXGKqodESk9RVgvJ1DMk9ac7pGnu88FeQu5BhCzhPckyR02KGvoKAziAxSdfuxsCXWVcBSiIEcyI7NgJL5EQyUki_o5fF544i_4BhEWICbuH9OzDfMEGmovbgXfr8Dg5XuPPPrXI6_W-D7M5QOg2RM4AwFhEWC7TlWMvUKFN3pGXar4WbM8Jimw_eTA-u9A57LHWBO-UThxZNmRIcNl-uNrXZ5RZQNpqS47o8ZVUpIUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عرزشی‌ها خطاب به سعید جلیلی:
نزاری به مجتبی خامنه‌ای جام زهر بدنا؛ ما امیدمون به شماست.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67486" target="_blank">📅 09:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67485">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FnPFksR0o7yr8DQOQiZt3bekHloD_gZOAOXTSzcF3Rni8OLINYT0DgHP2uwhxJsl5FPKXSYhFcTwJu4JC6aUzGb3L8T4Tuay36fm1i375v7lWgXCW1tymvhtxGkSZsiI1n7u0yeqnuapQcjLhpHG41iwLWdxSJePqr0KeFwN83ssbZy4xvKzLXwZ0ad-PwPihCZU9ic9wavo4rSsrYARty9OwJ6eox6LqgWU0Obk1bnVwhvqi3f62IntYdM4WsE9BtLiXjF0RFJTx5_scf-SS-uA6MNCFDo4MOXPsCT2GlpyQkskAw1_GPO8bQhuZiJvrRrmwCONq5W3MGtGVdYDng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
بیانیه وزارت امور خارجه ایران در مورد نقض آشکار ماده ۱۰ از یادداشت تفاهم اسلام‌آباد توسط ایالات متحده:
کمتر از بیست روز پس از امضای یادداشت تفاهم اسلام‌آباد، اعلام لغو مجوز عمومی صادر شده در ۲۱ ژوئن، نشانه‌ای دیگر از سوءنیت، بی‌ثباتی و عدم اعتمادپذیری ایالات متحده است. این در حالی است که ایالات متحده، در طول بیست روز گذشته، بارها و به طرق مختلف، چه به صورت مستقیم و چه از طریق اقدامات رژیم صهیونیستی علیه لبنان، به مفاد مختلف یادداشت تفاهم، نقض کرده است.
از زمان امضای یادداشت تفاهم در ۱۸ ژوئن، جمهوری اسلامی ایران با حسن نیت و تمام توان خود، برای ایفای تعهدات خود بر اساس این یادداشت تلاش کرده است. با این حال، دولت آمریکا، همانند روال معمول، همزمان با نقض تعهدات خود، سعی در توجیه این اقدامات با بهانه‌های واهی داشته است.
وزارت امور خارجه جمهوری اسلامی ایران، ضمن هشدار در مورد عواقب نقض توافق توسط آمریکا، اعلام کرد که هر اقدامی را که لازم بداند برای حفظ منافع و امنیت ملی خود، انجام خواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67485" target="_blank">📅 09:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67484">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/67484" target="_blank">📅 03:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67483">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ELQx6jWvYWCc78r-FSHHp3oSpbbi85tALasDfjTjKb6wgFc13v6ls1cbgGf06vZ8rW_0NUrLwuf0n8o_M9AAd4MDPMPeYAK8YSLNmazgIs6cBf049pWwyy-iuQI9jYOsXXl-_5IKIMGFUAKgum8t0v5EcxxnSaC1q5JtGTIkPEC0zk_Y-8BE58fxZjIX7eJ8J0jVCLwJ2Krrpo3dgxKOkwaqFmv65BPV6t3E_zgOVwmyrE1PoVhY3YNcd5DRQSZh2kEo8AOzrus5St1b2uLNDlS4a5hwwDsU0pxKOao9yb2aMWr1hmDdh9C99WleEJBEnasLFr4tL6HqiFe2Q_e7BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67483" target="_blank">📅 03:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67482">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sv995WEu0YtN0ZLUhh9b0KlNyNmLR2Hj4VR3rMbK4k-XigK6QMNlFdfr1ItFw5UrjmWOLFwDB03REojVd8gHXCk1eVTIu9d0_gTAhHF7NtiE8LdugX6-lL9AVKGJifWTPVpZF-MSXJqyI2GTCJ435yPvUyQQEAn9s-_HU-OIMMT45alVAHNKY1ggOPgXouiJqz5ItjHN9F_Z0L1N_oJgE8qeYDyAE5SbQ9g_-N9DG990rAOGq1Qy-UjiyJTRnKf0AcqPhAayMRnirhC3RuKztzbpCmmNkRH2tOmqfRayi2XglZWdYeHugrX5xnoTU_2x0q6PuuMNO0t-HVZ_hIIofg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به پسرا فحش میدی واسه دخترا کنشی و واکنشی تحلیل میکنی
😒</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67482" target="_blank">📅 02:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67481">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U4KLPmEwqOvgXNPF597PtZUuyy24tLRjWg4DdyZL6AFz78e2VczXKGx6Wd6K36wST3X_q29sxWcGWhBe_ijSsdTvs6NtJDA87mBNrRwn20h7zHX-tN3v10SjlQjVX0S0bYh7lnjLn4DaP62C1riT3Gq-wmxzsPi4ZjzupHm_aDjvJw3x7_kYMeJkB_0FAKUa-qGpPCNB748hAF9th2gQGwXBsdngHYrJStOhM2TkT0WVezoni_VpA3dj_f0Mvja2v5qy2bI4KOuVTeLGWMszYKf2DYGFyDXkN0EeWr_VTJZoeN9Hv9vgEQ2sa1YbboT5e-knGRb4J2b0YtPxu6U5rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
صداوسیما: وضعیت بندرعباس کاملا نرماله  @News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67481" target="_blank">📅 02:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67480">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">بنظر من زود تموم می‌شه</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67480" target="_blank">📅 02:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67479">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSor60</strong></div>
<div class="tg-text">به پسرا فحش میدی
واسه دخترا کنشی و واکنشی تحلیل میکنی
😒</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67479" target="_blank">📅 02:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67478">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K4zSb3iT1rYqWJvgDpxJbqXW59WEOYoKLNm6S9hz0-bSIM3eAihMUrLTHv0iGMnqg4YYXc0DZ49Q0ANIcsuxf8_7hAaLgDr-mLM05aNNJm92qo0r24hnnEfg7YaPCilyqRKDMTdYD8OuCF5SXo9sVYlWgj_Y722fQ1XCG5vYWETk6NShgDqD1DkCAnLPCNHb5Ep5soIle90uS1F-f5sGodFkEf12t9trp2JHehm_IhLfA7nz_YgVrMFBiBsLV-u36PVbLLG7IkA40sIABMzAyvEYqVSXAJ5i6Q2InHY1CfddjbaXKZ_9keszt0X7HfxYGzu8hASMrfzco4O-nRlEtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من اومدم بعد مدت‌ها، و تازه متوجه شدم این ادمینا تو دایرکت فقط جواب دخترارو می‌دادن متاسفانه
🧐
#hjAly‌</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67478" target="_blank">📅 02:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67477">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
دو انفجار جدید در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67477" target="_blank">📅 02:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67476">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">قشنگ نمی‌زنن بیناموسا، ارضا نمی‌شم دیگه
👉
#hjAly‌</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67476" target="_blank">📅 02:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67475">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهات نیوز | HotNews</strong></div>
<div class="tg-text">قشنگ نمی‌زنن بیناموسا، ارضا نمی‌شم دیگه
👉
#hjAly‌</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67475" target="_blank">📅 02:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67474">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
مجدد انفجار در سیریک هرمزگان
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67474" target="_blank">📅 02:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67472">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80cdbb5e99.mp4?token=aKRkvndNVNflYH3RNdX9se91-2uLNsPor7hHKjJlJ0u-Oy3r4XXI8AdUSHYjD1J5FXxvauSKCo7qpgM9-WrSvqdzIwONTXSMOTr-a6zEuDNSjNFvA0-T2gKswenv-cf9AS2fKhmVFMj1askAzahWa2oeK8k45Xj6P-giveCdpuiuZa8b57m0jIViFJNj-kJ-MjdP2nPQ4JHFXC0jrp1B1BJUWmYitGJ68nTnGaFN1Mb0JZjcAtY2FAjbCheYkJEAROowUcv1kub94pWaaW3zWbw9Cs3ky9qVUw9I7oxXITK7LEDQ57zfdM4q7BG_XZ61d50J3M54HqHTgVexe5FU-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80cdbb5e99.mp4?token=aKRkvndNVNflYH3RNdX9se91-2uLNsPor7hHKjJlJ0u-Oy3r4XXI8AdUSHYjD1J5FXxvauSKCo7qpgM9-WrSvqdzIwONTXSMOTr-a6zEuDNSjNFvA0-T2gKswenv-cf9AS2fKhmVFMj1askAzahWa2oeK8k45Xj6P-giveCdpuiuZa8b57m0jIViFJNj-kJ-MjdP2nPQ4JHFXC0jrp1B1BJUWmYitGJ68nTnGaFN1Mb0JZjcAtY2FAjbCheYkJEAROowUcv1kub94pWaaW3zWbw9Cs3ky9qVUw9I7oxXITK7LEDQ57zfdM4q7BG_XZ61d50J3M54HqHTgVexe5FU-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حملات ارتش اسرائیل به جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67472" target="_blank">📅 02:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67471">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
پرواز جنگنده های آمریکایی در نزدیکی بندرعباس در جنوب ایران
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67471" target="_blank">📅 02:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67470">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
انفجار مجدد در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67470" target="_blank">📅 02:08 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67469">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uIU5FsXBKdvpXNuK1dpVlH-7QDs89dFPjMv3gUwjxt2pc4AWhjBpPfOqyL6zeEgtGW9Z1RdxSEGgVvarPkBQS6UMVx-tmtsQ8C09FxsnuxYa5rQlXXN85ObG411EY7dICnMaz0Lh-TznS8IREoYuGOWqTTNLmY3HzFMXDquxGxNeow8NdXDfSWJOFirTtAnxa0te6A6CAkMTnr7-Nwu1kwg7umros9aQ9Txf-9Um1ZuEjFNrsDXBlSOTUg8m2nB_I-K8jFkV3wvOOfERPqaCppe-Apxjn7Qp44moyWQHSbi-ldm0ubAai4F2FhaNgpwjlnOks2RN2QZe99NATZ-3Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
باراک راوید:
مقام ارشد آمریکایی به من گفت که حملات ارتش آمریکا امشب در ایران چهار یا پنج برابر گسترده‌تر و قدرتمندتر از حملات اخیری بود که حدود ده روز پیش انجام شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67469" target="_blank">📅 02:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67468">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bLDZxOIRxk4mWYBIk3ciDX-p9xqe_8B9GnumxLmU89Gk4nH4DoENuhsaRILXv3hHyHIg_ZrWpM7AaB-GKCtsb3Ocn2hScZH6-2MbaKhfKUB3SB9fwFyY3nl7wN0rtSjnViuiLBFbnJgU1bWA24UghMAwmzEGIlnykOmVadbU21hgO1QAIqUrNQjRo3EZgnW9D0EhPL8lYfHZoVY5PxF_nxSkw_-FwGXWxb9HBEJzib7ZPSaf4g30abnrafaMhRt_1ZuS7SDM0lJLzG-ei354raoBPlOuoKI6l6-y0Kj7UglX-qer2-ijUY7OoI75_TEBucR4y4NThEQ51A9XxUXVEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ستون دود در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/67468" target="_blank">📅 02:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67467">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
قطعی برق در کویت و مناطقی از بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/67467" target="_blank">📅 02:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67466">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
🚨
انفجار مجدد در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/67466" target="_blank">📅 01:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67465">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cfe17753a.mp4?token=ORQNv0rXTMNmVs0TH-cFL2v_XTa4q5JVCbi4i-fndC_xcdtE13ZNXXYAmF03ef7PPr9aYVpwlVGqAinC6zVAgMguSeLnzXADBk3vSolGeIHFLVmgzE2WJgAXvDgVlrjHSKIeRyMaOHJlrhCD3HilDGOGfW5jT9B-IEAlwjNL3QzobXL3BYEetBW3Mj8YSj2k4ctShsYEiAR63vtYtz7Yh2r_YceQDvcJcY4mx4UOSwCw6LV6lh8dGD18GLYR3nXXiefhvvuFjsjJeYfFzX-oMOvjsPS-2OhZJh7BSsyJ3FJ8yWoLpqyHv2b3gM_4JtMbIx5uhQBEUg1P0sC7jz10Ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cfe17753a.mp4?token=ORQNv0rXTMNmVs0TH-cFL2v_XTa4q5JVCbi4i-fndC_xcdtE13ZNXXYAmF03ef7PPr9aYVpwlVGqAinC6zVAgMguSeLnzXADBk3vSolGeIHFLVmgzE2WJgAXvDgVlrjHSKIeRyMaOHJlrhCD3HilDGOGfW5jT9B-IEAlwjNL3QzobXL3BYEetBW3Mj8YSj2k4ctShsYEiAR63vtYtz7Yh2r_YceQDvcJcY4mx4UOSwCw6LV6lh8dGD18GLYR3nXXiefhvvuFjsjJeYfFzX-oMOvjsPS-2OhZJh7BSsyJ3FJ8yWoLpqyHv2b3gM_4JtMbIx5uhQBEUg1P0sC7jz10Ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حملات سنگین آمریکا به جنوب کشور
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67465" target="_blank">📅 01:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67464">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fIdATQR0xLodbxOA5e138x8cqhNp31uYG0mULLrGDOgWp4SGIg2yUdvgu_saKwJOdJ16dBWV3BIypp4r9MNGrke4QZ7gRvPq4nW9ainK08U-433L3Aey4SRiS_3GKyhjc1JVabHEwA59zmFvo8_OfOHO2p0bBNiCCBTmi7gNSqTaNI3TQyLbex1406WtL0ayEHJD_L4y61kXHAiQQURUQ4hNiXE-cet3g2GqKM7D72JnBoUed9efndNkCD6X_Ltyx-HvXUdyvesRDWj8mUYTV2Z9c7Dd3BPeqmp5doG8VUu3bIUJVptrJHhxcVtyUj-cLnAyOuNE_f6TwyaJIA-Pbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ابوالفضل ناصری، عضو فراکسیون مجلس:
آغاز موج های جدید و بی پایان سپاه
‏تا دقایقی دیگر…!
‏شدیدتر-ویرانگر! ‏
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/67464" target="_blank">📅 01:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67463">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
🚨
کان نیوز :
در آمریکا برای احتمال چند روز نبرد با ایران آماده میشوند؛ این موضوع با کشور های عربی خلیج‌فارس نیز درمیان گذاشته شده است!
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67463" target="_blank">📅 01:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67462">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d35d8f8a5.mp4?token=UPZY5ADPBVEd6-6K0L6Z5ncQghkp4iQ8z5RziPuARIsDueQ8ibXvgTlugP0RzxX7vu20OHkuDnxXGYi5huWV4EKU2XCcHTBhYD3nn2thKEObZA6nnpBAwK6RNxwC4xPy4twpwrxL2VbQo9-uZIDR6evwDHSB0gTsg1nzCpQYO82NgFJDtxwG-DjtFrNHx3bpljLJheZzR7cjrf9_YSpCn6fEI4VbmyJzORdlN_RuW0AcoXqjK_9PxR7YsYmmYPV32zY3GDZ0V4xXBkjeVrDg_GpuAEsWzgoULGo04_QdjP_pP3GIAoSjRbuYBXU4h7I0SXR-_1WP7uFofOApvBjVdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d35d8f8a5.mp4?token=UPZY5ADPBVEd6-6K0L6Z5ncQghkp4iQ8z5RziPuARIsDueQ8ibXvgTlugP0RzxX7vu20OHkuDnxXGYi5huWV4EKU2XCcHTBhYD3nn2thKEObZA6nnpBAwK6RNxwC4xPy4twpwrxL2VbQo9-uZIDR6evwDHSB0gTsg1nzCpQYO82NgFJDtxwG-DjtFrNHx3bpljLJheZzR7cjrf9_YSpCn6fEI4VbmyJzORdlN_RuW0AcoXqjK_9PxR7YsYmmYPV32zY3GDZ0V4xXBkjeVrDg_GpuAEsWzgoULGo04_QdjP_pP3GIAoSjRbuYBXU4h7I0SXR-_1WP7uFofOApvBjVdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حملات شدید و آخرالزمانی ارتش آمریکا به بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67462" target="_blank">📅 01:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67461">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8eaffe3050.mp4?token=n5Bc923Zk1DSuz3_9NlBv5GqIj3aA7Vqt56pb0gROjre6VRjKo1dyBaVIinVpysVRUx9HBvM4mbi1LPd8jfiQcv5dk6LU8S363SOK62CxwjFzgo_Zu8YQWauonjQJql61ITwNUjmjvNc8HxUB39dHWV2JXoHFKJT3VKviI09NPES8QmKNVx23LK3Ic3DXKJsb42tJfW_yW0DEudSd8fksc-7EPl_WJhunS4zvOmYeg24_UVgzFDR8-64xsz5iR0KftZ_jRlWYZ7v2Dn447tCjadkKGZ3XUKvrDBcTsWyBBpLf6ixv0NKxTorgzRZmokpvoYVx8uEks-tHznCvTPhYA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8eaffe3050.mp4?token=n5Bc923Zk1DSuz3_9NlBv5GqIj3aA7Vqt56pb0gROjre6VRjKo1dyBaVIinVpysVRUx9HBvM4mbi1LPd8jfiQcv5dk6LU8S363SOK62CxwjFzgo_Zu8YQWauonjQJql61ITwNUjmjvNc8HxUB39dHWV2JXoHFKJT3VKviI09NPES8QmKNVx23LK3Ic3DXKJsb42tJfW_yW0DEudSd8fksc-7EPl_WJhunS4zvOmYeg24_UVgzFDR8-64xsz5iR0KftZ_jRlWYZ7v2Dn447tCjadkKGZ3XUKvrDBcTsWyBBpLf6ixv0NKxTorgzRZmokpvoYVx8uEks-tHznCvTPhYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
جنوب کشور
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67461" target="_blank">📅 01:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67460">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
🚨
انفجار های مجدد در بندرعباس سیریک و قشم
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/67460" target="_blank">📅 01:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67459">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YI6cz0s3_NZdPkN3PWrSgKtnwGekdvzu0MrdeJoVa4wgv9YmdqQ6ZKiqmS41Z-BArNPA89tmHcTeVG4lLI4stwW2IRXlvKFd-tuqWJ44pdu68PsAmJDkDgRsuXAmD2hJjJ2USp1DRT4f-Bb-NxFc9F61otcNX0XUKNBh1h4GXUhcvOialnr25ZtOXGE6CllB6zmwAa-J7637y-RaSCrCslHNQnA8ail2ZxJcuw8TEZxG1bpY0K33XZryx6p8X_mRIP30rNWGHpXQzW4TnXFTDWUXJPISHwkOZyRHIXe3k0O2ajjUNjnUXGXRPzmx2qJXp9plVhOayKpNg-Dkbu9L6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تحرکات فشرده هواپیماهای ترابری نظامی آمریکا در منطقه رصد شد که شامل برخاستن دو فروند هواپیمای C-17A از پایگاه موفق سلتی در اردن، یک هواپیمای C-17A دیگر از پایگاه ملک فیصل در اردن، علاوه بر یک هواپیمای C-17A از پایگاه شیخ عیسی در بحرین و یک هواپیمای C-5M در پایگاه Alhairates در پایگاه الحائراتس بود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67459" target="_blank">📅 01:27 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67458">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/761109e119.mp4?token=ZZckI6ZnetQWFh0FKlt8fJjEBaPqxj27EKTfGKE238Osx7z3Cdh6bEO4CpolaPqxXVe57crh9StVbes4Zn6wk64e_BI6Ny0Zsa4HezGMd6C2KYHYiGGJQlq0hPJZ58pYZdJoOf0l7XC1UO2LmLw9HMhHOCiEgnkMuHQltCnEv8_qdJPxc9Bc0bJVKsiPYO_Qn_itH5qcFZjFYRbh-FfaWkazrjbokLz2xqeLuhk9GFZ0D2qOhSbjJylZh2IPYmQOmwCrHi_PD_-TRz8KFVhOGX1vzuzi9Dlak06syOIWZL-ZrvVE92wYhg6ifaknDPEpWOAU1qj4WOKW8NR5sEMS7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/761109e119.mp4?token=ZZckI6ZnetQWFh0FKlt8fJjEBaPqxj27EKTfGKE238Osx7z3Cdh6bEO4CpolaPqxXVe57crh9StVbes4Zn6wk64e_BI6Ny0Zsa4HezGMd6C2KYHYiGGJQlq0hPJZ58pYZdJoOf0l7XC1UO2LmLw9HMhHOCiEgnkMuHQltCnEv8_qdJPxc9Bc0bJVKsiPYO_Qn_itH5qcFZjFYRbh-FfaWkazrjbokLz2xqeLuhk9GFZ0D2qOhSbjJylZh2IPYmQOmwCrHi_PD_-TRz8KFVhOGX1vzuzi9Dlak06syOIWZL-ZrvVE92wYhg6ifaknDPEpWOAU1qj4WOKW8NR5sEMS7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
بامداد چهارشنبه؛ بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67458" target="_blank">📅 01:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67457">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bbd6f07ba.mp4?token=e8e1TsmzwdEppAH7fdx8fehApT7N1e_11r2jtAAndJE6hMOB7nBjT9nGjOLKJUlZq_134o6t70A7uqpCgV3H6ej7dxaVAfuudCyQ0EfNMioohYBDmBkv28RDAlUW1Sckbhl82lHoYJyXpULkrqTmJzr8DB9UqGnca75dJCFoEe9aFIrVdh0hQsJv_aWZd0bcmSgL4y3oaph8YSECAgR2CRRvQREOXhB1l1EnNSow7BXK-F9q1P9YQawKmDN9qUTK54gaDhGq5uQcDXJxReqk4LJ_o1Y9mNHOnlcBf0O3_KNbgrASbmKQfIhY03m8xvHbFQVPgmjsfMbHISCL4xbdRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bbd6f07ba.mp4?token=e8e1TsmzwdEppAH7fdx8fehApT7N1e_11r2jtAAndJE6hMOB7nBjT9nGjOLKJUlZq_134o6t70A7uqpCgV3H6ej7dxaVAfuudCyQ0EfNMioohYBDmBkv28RDAlUW1Sckbhl82lHoYJyXpULkrqTmJzr8DB9UqGnca75dJCFoEe9aFIrVdh0hQsJv_aWZd0bcmSgL4y3oaph8YSECAgR2CRRvQREOXhB1l1EnNSow7BXK-F9q1P9YQawKmDN9qUTK54gaDhGq5uQcDXJxReqk4LJ_o1Y9mNHOnlcBf0O3_KNbgrASbmKQfIhY03m8xvHbFQVPgmjsfMbHISCL4xbdRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ما که نقض نمیکنیم
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67457" target="_blank">📅 01:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67456">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d512a0d2d.mp4?token=cIgG9Qn_cw2-ixA4J15JZu0S_U6xqr1_NdYbLhnFWPLohcYpgT1jMERBriBpx6yvYyAJAIBaBoWjgno8HZDPLStIOoXJcr-3NG-ZBUc4I0FG6HPIp4P7KgI-V4jGuz1WBtcdQRo4wzctbVgyVEmkeqSJCWbov3HXz-Uh3S8PxtmCcqJRTv23BFCfKonOAmBHv1RXtveV2l2aYMsHBU1f6ySfnHYIuK_cqcmlB4Yp3UTtOc4rKvv7q3h8VEC6TbMihjgR094o737VKG1JVJjjlQckyrfywQ2Q2X14wdGLzkazDNcHiEdnkzVn-TxY_chzf5BSaaTBucLtz1p6cdvtLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d512a0d2d.mp4?token=cIgG9Qn_cw2-ixA4J15JZu0S_U6xqr1_NdYbLhnFWPLohcYpgT1jMERBriBpx6yvYyAJAIBaBoWjgno8HZDPLStIOoXJcr-3NG-ZBUc4I0FG6HPIp4P7KgI-V4jGuz1WBtcdQRo4wzctbVgyVEmkeqSJCWbov3HXz-Uh3S8PxtmCcqJRTv23BFCfKonOAmBHv1RXtveV2l2aYMsHBU1f6ySfnHYIuK_cqcmlB4Yp3UTtOc4rKvv7q3h8VEC6TbMihjgR094o737VKG1JVJjjlQckyrfywQ2Q2X14wdGLzkazDNcHiEdnkzVn-TxY_chzf5BSaaTBucLtz1p6cdvtLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
بندر عباس دقایقی پیش
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67456" target="_blank">📅 01:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67455">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a0245f958.mp4?token=FmyRHe9ynWlO-953_8brdNufOL7Urx3G8AouKCSsBYV7d71fJgEEmcuXNm5r7b5cIdzn0HFknuwjuIVY1GO1UnV8ejKj1eddyd1hFTYaCyKQGx5PO75ZPl4gIy641-f2QoXd-Ig6OydqBKd6cK8Zq2ZUnasYd4qP_RwtjO-3Uk5B4U7jT5MFWpC1V9TopxYqEchAQKu-4K_Yb6bDwhR_yq8OWFNtFf6EAbXNUVzsdtgOyn1-9w6UcAUSyJ34Dz6E3_wZ0otjDP_YR3reeS8ba2dC5M8v_KVtCtzqCIz10nhaIQVM_prxnD54J9wGV_k3WAqZje3S5GJ1J6ZxqApDeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a0245f958.mp4?token=FmyRHe9ynWlO-953_8brdNufOL7Urx3G8AouKCSsBYV7d71fJgEEmcuXNm5r7b5cIdzn0HFknuwjuIVY1GO1UnV8ejKj1eddyd1hFTYaCyKQGx5PO75ZPl4gIy641-f2QoXd-Ig6OydqBKd6cK8Zq2ZUnasYd4qP_RwtjO-3Uk5B4U7jT5MFWpC1V9TopxYqEchAQKu-4K_Yb6bDwhR_yq8OWFNtFf6EAbXNUVzsdtgOyn1-9w6UcAUSyJ34Dz6E3_wZ0otjDP_YR3reeS8ba2dC5M8v_KVtCtzqCIz10nhaIQVM_prxnD54J9wGV_k3WAqZje3S5GJ1J6ZxqApDeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حملات سنگین آمریکا به بندرعباس دریابانی
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67455" target="_blank">📅 01:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67454">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
🚨
وال استریت ژورنال:
کشتی های جنگی آمریکا در حالت آماده باش برای احتمال شروع احتمالی محاصره دریایی با دستور ترامپ  تا ساعات آینده هستند
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67454" target="_blank">📅 01:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67453">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb48bc0feb.mp4?token=ZlCH7O0huv38aayIKq-g5sashzInJah8uypRjcNRouh0FeZ38HKdw1gNbl_CBoExNstkArYpA04cncolcReS9VKacrG6HB0RVAy_-MvOdorKZS2Ez341YpAIhOgPOSzDzJ00i0rXoEGdhZIClDVWQTLVrEzWhn4YsGXV_jHJQmlTofJ44Wm5EmoUzj8x21b26wuwuRXZ9DLNI1Z4NwmZghCNwKwedtnoagLhNorZN9IBHlDvbhvhKZARTiL01220jsjaf70mGv6uD0L0vbf3uOPhhuVSg_GfvYWVir2q2yzsh9RGi1MuhRzHRU8d2m91XLFshqYh-zQ3EwLYOLeN2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb48bc0feb.mp4?token=ZlCH7O0huv38aayIKq-g5sashzInJah8uypRjcNRouh0FeZ38HKdw1gNbl_CBoExNstkArYpA04cncolcReS9VKacrG6HB0RVAy_-MvOdorKZS2Ez341YpAIhOgPOSzDzJ00i0rXoEGdhZIClDVWQTLVrEzWhn4YsGXV_jHJQmlTofJ44Wm5EmoUzj8x21b26wuwuRXZ9DLNI1Z4NwmZghCNwKwedtnoagLhNorZN9IBHlDvbhvhKZARTiL01220jsjaf70mGv6uD0L0vbf3uOPhhuVSg_GfvYWVir2q2yzsh9RGi1MuhRzHRU8d2m91XLFshqYh-zQ3EwLYOLeN2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
ویدیو ای منتسب به پایگاه نیروی دریایی سپاه در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67453" target="_blank">📅 01:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67452">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kWBLjKnDIJFHqcs-IonLBZ2lI3SuUx1A_AiSTtJ8xgh4BQGO7vbNUbzosF-KIwoMRzE_yPA8yYAFlbtBe3z2SprFfS5wnNtuGiO25KqXwaY3yzspb_6kUdDtr_6_1QjZEBwgK_1MukQ0pzUqxE_78VYatY_3fLhoYV-eiEafPNDJOQAxLbEOQFZ1fJxA_QuSfZwO60RCFURHLjZshf6LqukR7HIVRjhu7VkGzRP2R2Ro2eyCcyoD3E6D1dp19_E_iI-fQ5clL2ksRyBc8wrYHDB2fPhPqv-Y2InzCkJ3JEo47oRIyHwZajocVSIxU0Ew3edXet0Z4Jb2AEDXLGEuiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
بامداد چهارشنبه؛ مشاهده ستون دود از سمت پایگاه هوایی بندرعباس.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67452" target="_blank">📅 01:09 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67451">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b8-UWafCNvORZiQQMVwJWrME9azSsht_MC9eL6SjBMCsAkbKAkHuzzLIB990iXHJYp7pIKE-sBdwkhLVXTRB2ZZmMa-aMhP07Gg932gZ2PERbULTy2SEZiGzlWFBMU3MhKlC0mvvBSrJIYvZeJSzcc90liEJbQdxUYK9G1zt3G3GTO9ci6vzUc0dPyvU6Z_gf786Ier8QfG22MR24fQraw17zptZb6atD2Gn_kYtdefRV4F9Wrry8b96QlvP8snHMFx8sz0vC5YZ88R3MVFSyH4SVZHxbAou3trTT3am8Clmy9WYu3pFVPNEb3EuhapPyrydYTAYZimj97SCn9Fp7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
دکل مخابراتی سیریک که هفته ای یه بار مورد حمله آمریکا قرار میگیره :
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67451" target="_blank">📅 01:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67450">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TIDR3yCIqzMcN3s5EoSG15wEyVXPYvbIcagr6VBWBPFM7QvZOVAn7lV491QU37txhq4hPOzGgORuJ9ZKd8ydDGvj7kdWx0_EQrr1OZyNKG69G4WzFHZppE_M4ndLQ2yEuEm5Iy81mpwjlI-3OOF6oVeyuv1bYCYGE_aRMDCQAaWfW_GbuHgjaBmnVz3HEpdYHKgrEDoIPWcVc9-7OCvL976BwAxHE6bLDnsc-10aNpOz3itlhmnUG0CoRykRIUWSke0q_1U9YVXlA0uHdziXQJ4ELGA5bUV9dqc4CE7kOpuF6A038CEhMf0ymJxeUrmxqrj09ca5TmkVlG-5Onk8jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اوه اوه حمله آمریکا به یک اسکله‌.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67450" target="_blank">📅 01:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67449">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UDhTjEol1h-x2r0mADIMWONXces-iPSDJ-NERA4NvT7_0_HnQGESTaLu2sEr6kAssxa14S3nBN5meen3HLoVUbrp9jBC-PaaPQ2M6sz4YaVd2Fvk8ShDyDb2WEL4ItjtgSbGfFjmQ6iY859Wh6btwGbOXc4uF9ZguyP3EcyYAS7_RrMqsU_ftRdnFO33KaXy3Jx5uYgkdWtTYbTOHuSw9Xrq3yA9rL4cY7OH9MEvLK_hXilCpVylUGvIedpKlW-K2ROjgKlB0vI60ICMJ4gScnmc2TcyRhjuNxrVh47dVLehIkShu_Vn6864OAn2C3gjJOhVTvARVfvxC3luv0Cq7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
تصویری منتسب از سیریک هم اکنون
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67449" target="_blank">📅 01:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67448">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uqgT_7Ri--W62ReQMSnh24qvK63ilo3hYQ6Vl72RgAiP5aRdP-rz6TZqQuHhqtRlYvmpTwNDFs-C2sdGBqZPiEsUHLnIgq4b_GofPh4B7U-evl3fgB4EE3ouDsFN32z17sTIY6gfTNFW-I0zPL2UlVZMDact2NNZvkSnorBLnSSlBtkLurh-PjGKe0XIT58-I5VsHQfIYp5h9O8nEirtrU1Xskl2eAGK-vF4NhJ2IYfpz-LV3J34P41ibmORIZmj3Ww2BDBhWUx8Kw3VFl9lBgUBWVo1If1xlIgv_58XQzyyRB0mqoXW3r5q9DsGWv5RQB65wfyngrCJi2pWaNP9Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اسکله‌ی سیریک، شناورهای سپاه
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67448" target="_blank">📅 01:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67447">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CNyfZmJk9DTK53qRkYIHIKCuPKwz1N66W2lQ0rBvlVXv_totXySNdcbTpQ1f9500QxkordyrIwLFTwuEZVdgdXMGvfhsNqZeVDVtqBoPzUDOGKr1SGEvwHJnAidosYnD37uF-o3d40toQ-wnLkyqXoi-iMOh3qk7A4yu9j6k8sKPaF5M9QTRyql18RM2eKiNaj6Vyh02WGvkKKMtSb2yV_AWg8UEe0BeQAhy68ahaL4u61Kb-MlRN_SCwnvvWzx5-mxmogHZBiu512ZQWeNxoCypNCr5_1VRuHBF67-jnJ0ljUzkt0647ckiAeEsZImcw6ttDoKMJCxJpi9o-Beq1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حملات جدید آمریکا به جنوب ایران
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67447" target="_blank">📅 01:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67446">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش ها از هدف قرارگرفتن فرودگاه بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67446" target="_blank">📅 00:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67445">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d3287ab1c.mp4?token=ha94T7u26goiL2nd3Kg_encsM9C_j5Z2Cap7gnBor5p3CLG4r6Ap5prvgpUDv2bppsPfxrMTEki0-NZMfaRerZ7_MYnBMmsBmZEcBLAyGaMKcyHaiUUybrjmCrUppRWDOOh6Gv_qoFXx9AAGZke-yIm4_H6HU5vJ12Qhqku0CPYJAB5NtF6ojT-8D9kkmpcmEslzOcF9_JtIjNzEM3K-xZDcsR6QI71nKFtp1fcDo7Bqrfx0mGOPseggJKlX2vRWnElPREFWGgDL2ZHNEHSgUZQoadHkI8pAcnm95-4nklbijvntBTfiBOeHRYBFhqOnYA3Lv9P2GIr2H5ob7kz2qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d3287ab1c.mp4?token=ha94T7u26goiL2nd3Kg_encsM9C_j5Z2Cap7gnBor5p3CLG4r6Ap5prvgpUDv2bppsPfxrMTEki0-NZMfaRerZ7_MYnBMmsBmZEcBLAyGaMKcyHaiUUybrjmCrUppRWDOOh6Gv_qoFXx9AAGZke-yIm4_H6HU5vJ12Qhqku0CPYJAB5NtF6ojT-8D9kkmpcmEslzOcF9_JtIjNzEM3K-xZDcsR6QI71nKFtp1fcDo7Bqrfx0mGOPseggJKlX2vRWnElPREFWGgDL2ZHNEHSgUZQoadHkI8pAcnm95-4nklbijvntBTfiBOeHRYBFhqOnYA3Lv9P2GIr2H5ob7kz2qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
جنگنده‌های اسرائیل حملاتی را در مناطق باراچیت و بیت یاحون، در جنوب لبنان، انجام دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67445" target="_blank">📅 00:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67444">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ از ترکیه و بیخ گوش ایران، دستور حملات به ایران را صادر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67444" target="_blank">📅 00:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67443">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
🚨
حملات مجدد آمریکا به بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67443" target="_blank">📅 00:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67442">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nz94Wq3nd7f8MjWBZocO2CJwJBForiUjRqaiG0eNT4ppNq2ntmSeydBxIdYrt5FMKUJy5obNDxSaciLzSdqg0AXmJFRpLArcehYMKndsAhH_r9-8jk7XK33ssAOzk97ufs7zYMaAOFwJ1ANelm9SAWPo1CcRwIxxXUnbfI9CaM2hvCebplKAMly0SkJA0v8J6BDi6uWvlVMCpsmGzRv6c6-yVuWCMHp0qeSeDhpsbHv74G7a6tNRbkOs7v5J7gy3Q9kWCpkbuUVfsKT_LCwbxM24nKxDFBclCacTgJ9441XF3L1kRwJjnnBOWtoWr6uXtwJYzYGNl0A0I-m-WGiD2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده:
نیروهای فرماندهی مرکزی ایالات متحده، سلسله حملات قدرتمندی را علیه ایران آغاز کرده‌اند تا هزینه‌های سنگینی را برای هدف قرار دادن و حمله به کشتی‌های تجاری که توسط افراد غیرنظامی بی‌گناه در یک آبراه بین‌المللی اداره می‌شوند، تحمیل کنند.
این حملات آمریکا در پاسخ به حملات ایران به سه کشتی تجاری است که در تنگه هرمز در حال عبور بودند. این اقدامات تهاجمی ایران غیرضروری، خطرناک و نقض آشکار آتش‌بس بود.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67442" target="_blank">📅 00:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67441">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
🚨
#
فوووری
؛سنتکام هم حملات آمریکا به جنوب کشور رو تایید کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67441" target="_blank">📅 00:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67440">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
🚨
همزمان با حملات آمریکا به جنوب ایران، حملات اسراییل به جنوب لبنان از سر گرفته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67440" target="_blank">📅 00:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67439">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
🚨
انفجار ها در بندرعباس و قشم
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67439" target="_blank">📅 00:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67438">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای چندین انفجار در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67438" target="_blank">📅 00:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67437">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش ها از انفجار در سیریک هرمزگان
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67437" target="_blank">📅 00:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67436">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f7c257f2f.mp4?token=JpaRauQX-l_FD5IU9uV8V8OP-4-uPv_ASa33rTtM46148GoNHsSL68CiterECXgEJemlFuF4cG9AyQFOE8WpvsiSHHWozTW5M86VR8dBcV3IdSImZTtzfjp1zsKFen11cVeuJv5COyCVAjtxE94JmxTuUzW4rrQ-E4XdRy0Osl3CAPGnogeAhpGUyTpm9CzhcXHzvf-_M8Hsle8JVqQQWuQbQa6ITuYYRCIbiup8T_S2WYNiDwG_986YgG0T5fgP3sphAUdAu9KrerdNAW3x1EJycyau6gW0A_ls8fGzLf1JW945TAXOLMfj-wmPGMI6sz3Ke5jxSzkD1ihg-CYZkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f7c257f2f.mp4?token=JpaRauQX-l_FD5IU9uV8V8OP-4-uPv_ASa33rTtM46148GoNHsSL68CiterECXgEJemlFuF4cG9AyQFOE8WpvsiSHHWozTW5M86VR8dBcV3IdSImZTtzfjp1zsKFen11cVeuJv5COyCVAjtxE94JmxTuUzW4rrQ-E4XdRy0Osl3CAPGnogeAhpGUyTpm9CzhcXHzvf-_M8Hsle8JVqQQWuQbQa6ITuYYRCIbiup8T_S2WYNiDwG_986YgG0T5fgP3sphAUdAu9KrerdNAW3x1EJycyau6gW0A_ls8fGzLf1JW945TAXOLMfj-wmPGMI6sz3Ke5jxSzkD1ihg-CYZkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت های رنالد ریگان درباره جیمی کارتر و نقشی که در سقوط نظام شاهنشاهی ایران ایفا کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67436" target="_blank">📅 00:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67435">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">‼️
مرگ ژوزف استالین و نمایش سه‌روزه جسد او در مسکو، اسفند1331
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67435" target="_blank">📅 23:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67434">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VW1jkJgzFDIKxNNnAu3_Pi8IxbNtEfXv5VBfG7qRi3Bh3ZhCasfq0cqJ6C1ay2iwYIMISc7H467b-bca29yA0Mc0gdhy3nKbQL0ymNpQqifl628fxxQOLpkvpP-orykKqkutPW17VqSpXKBM3VXQt_RzdJk8QaX7ye7zNb3HGDnjJb54vdZS_iEAqdyNVYx0sDxxBh1YgkVNn9zazPLEdL8VgY9TdbRnoYkq8tVUcT9U_9VBhFJ9ltd67Tb14VRkcwrhFo-GFBz0ssnGT2tl4isb03o4ScJg3Lcy8qMLN7bdbhomReUQ1qPeIP2_nfM-iioQhfMv_H8WfLcVXUjwaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو ایتا چخبره؟!
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/67434" target="_blank">📅 23:09 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67433">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
ادعای مقام آمریکایی: واشنگتن مجوزی را که فروش نفت ایران را اجازه می‌داد لغو می‌کند
یک مقام آمریکایی اعلام کرد که ایالات متحده در حال لغو یک مجوز عمومی (General License) است که فروش نفت ایران را مجاز می‌کرد.
به گزارش خبرگزاری رویترز، این مقام آمریکایی هشدار داد که اقدامات ایران در تنگه هرمز «کاملاً غیرقابل قبول» است و «با پیامدهایی روبه‌رو خواهد شد».
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67433" target="_blank">📅 22:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67432">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
طبق گزارش ها یک نفتکش بزرگ دیگر متعلق به امارات نیز مورد اصابت موشک در تنگه هرمز قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67432" target="_blank">📅 22:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67431">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TE0aI-ROyYrWF4oV6sVOreUGu5u0lmVev7lqujrwFvzVG1dYxf9nSApDUMLvFMIN4XCdNMwIvV6iWIIxVYsY9L3yJJWC3lfXamrkQmnjqQbDu0cUv1sh_Q2K1aCEe5pJf4WANsR1_TxWKz6q1BmJq5ahafG1cP-KVN_drVw5o_u0LQnN1RRJMLt3valWsivnnbmRTusYGZml2SrgwIb6EENtsQH5n5wMzc9Qx9GFLGfrN-AGhrmx4rdl92Gb-kMZeYhXiqyFLbV2_JhnLPvdMs1VVir59nl51R7vADOSN306gYvA6_6jSIC9LqKR0t4bPEvTghDp9B6XGVSi9R7HDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
یک‌هشتم‌نهایی‌جام‌جهانی 2026؛ کامبک جنون آمیز و برگ ریزون یاران لئو مسی به جام در تنها 14 دقیقه؛ یاران محمد صلاح بازی دو بر صفر برده رو سه بر دو به یاران لیونل مسی واگذار کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67431" target="_blank">📅 21:40 · 16 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
