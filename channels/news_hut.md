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
<img src="https://cdn4.telesco.pe/file/eGFEi3ORE3IVwqZ1fwZJWmaoi4ShnvAX42LasSw0K2gRsGpszqN1w4FMKLdOnNqhyTCABI_-2av5u46eCNddOpwz2y3hyHeKhGNRGXqufOwLUg8PtuE0jTVQQdEfL0AwDnCP468DmG6TRkSeWs2-EGwCw_5YnetNMqLMNhogOG5GTjHjd49eGu85fVwljVuupWiOYoYG7yq3cR4rrm-HTayYb4R0SYgm_M6ZtpGJSP30yHTW73r6c6LKE7hpsCEQH3AGm1m1SJsaZnzT9QlUtL2ye-dg0ZxtITU6TX72EArnK59Tjlh7T85z7VCtPobfF81i71ZmulAQ80Ro01MbtQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 105K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-14 22:44:37</div>
<hr>

<div class="tg-post" id="msg-72844">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c58dc98573.mp4?token=fevPm3vt3dyg90ri-v_Ugm75qyqwA7Iwe4i7LXce11Kf-ZK5BiuCFBiYivI1u8Jfdd1irZoV7ibq4Y-sZtx_gV6bg0QQIiT2SKq95mT2QFztfPhGAsCKY-qwcaQBMHeKI6ytuxN2YuM_jbOffOHhR2Z3q7SoGjSOUkVgvARgQZmEkFMCIGODU5JF9ft0pVAphHt-rjvmwyEHb3qx7TSE50JC91ZPydw18hK1IuWbU6F0EcMvNnHwkXFQ9JuTx_pne349ilhXaMYwR6loh7Wr38Ur-zWpRpUFsu4h0YFp6-B5FAUHpx6tDHopPzi5B0MR2eo_CoYaCOV0Kc9_uR3Ncg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c58dc98573.mp4?token=fevPm3vt3dyg90ri-v_Ugm75qyqwA7Iwe4i7LXce11Kf-ZK5BiuCFBiYivI1u8Jfdd1irZoV7ibq4Y-sZtx_gV6bg0QQIiT2SKq95mT2QFztfPhGAsCKY-qwcaQBMHeKI6ytuxN2YuM_jbOffOHhR2Z3q7SoGjSOUkVgvARgQZmEkFMCIGODU5JF9ft0pVAphHt-rjvmwyEHb3qx7TSE50JC91ZPydw18hK1IuWbU6F0EcMvNnHwkXFQ9JuTx_pne349ilhXaMYwR6loh7Wr38Ur-zWpRpUFsu4h0YFp6-B5FAUHpx6tDHopPzi5B0MR2eo_CoYaCOV0Kc9_uR3Ncg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش‌سوزی بزرگ توی آب‌های نزدیک سوچی
امشب یه آتش‌سوزی گسترده توی آب‌های نزدیک سوچی روسیه راه افتاده؛
توی ویدئوها یه خط طولانی از آتیش و یه ستون خیلی بزرگ دود سیاه دیده می‌شه که از نقاط مختلف شهر هم قابل مشاهده‌ست.
حساب‌های نزدیک به اوکراین مدعی شدن این نفتکش هدف قرار گرفته، اما منابع روسی فقط گفتن یه شناور نزدیک بندر آتیش گرفته و فعلاً علت حادثه مشخص نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/news_hut/72844" target="_blank">📅 22:08 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72843">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">شلیک چندین موشک ضد کشتی به سمت تنگه هرمز
@News_Hut</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/news_hut/72843" target="_blank">📅 21:11 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72842">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ایران در اعتراض به برخورد دولت فرانسه با اعتراضات دانشجویی و چیزی که «نقض آشکار حقوق بشر» عنوان کرده، سفیر فرانسه در تهران رو احضار کرد!
وزارت خارجه ایران هم از فرانسه خواسته به تعهداتش در زمینه حقوق بشر پایبند باشه و آزادی‌های اساسی، به‌خصوص حق تجمع مسالمت‌آمیز، رو رعایت کنه.
جالبه رژیم جمهوری اسلامی که بویی از حقوق بشر و برخورد مسالمت‌آمیز نبرده میاد به بقیه کشورا برخورد مسالمت آمیز و رعایت حقوق بشر توصیه میکنه!
یه نکته دیگه هم که هست اینه که تا امروز هیچ گزارشی مبنی بر اینکه معترضی در فرانسه کشته شده وجود نداره و گزارش های رسمی که وجود داره نشون میده فقط بیش‌ از ۲۱۵نفر دانش‌آموز و ۸۵کادر آموزشی زخمی شدن.
از نیروهای دولتی هم حدود ۷۱۵ نفر نیروی پلیس و ژاندارم در جریان اعتراضات زخمی شدن.
@News_Hut</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/news_hut/72842" target="_blank">📅 20:26 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72841">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ktiZNNkKxXMe4EtE7ikEhmK5UhkFceBH3cNH4do3hg8y8DbjByYZhwUD2RwcKLPBX61L4bn3u9ylUSZDnyPjDa1FTIsVxQpdS_xjAremgHceKgtiPuXbNJIWL2t9F9Zb0y90hLWo8HC2f2DDPB5tYU1Z9uVL4lpKSJ9kRQjhZpPslCiNjC1kCgwbbRUY-ethaS5Sna0-DeixSsK5pO_tMeVEGYBtc69YM5KqeLsxTrLirJzAKVKAx0KH1I7zZxxIVm-prwRk_yOS9G8d-Bn1YLNd8OEz9uClYBMM_xkG4wq5K73womnvGw5-ml1diuRimhuf0L8PRoANuHtSL5mtLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت خیابان های فرانسه پس از اعتراضات گسترده دانش‌آموزان و دانشجویان به دلیل کمبود معلم و وضعیت بد مدارس</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/72841" target="_blank">📅 19:09 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72840">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">#فوری
؛رایتل رسماً به مزایده گذاشته شد؛ شستا ۱۰۰ درصد سهام این اپراتور را با قیمت پایه ۱۳۰ هزار میلیارد تومان (۱۳۰ همت) برای فروش عرضه کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/72840" target="_blank">📅 18:30 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72839">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">یه مرد ۲۲ ساله بریتانیایی به اتهام مشکوک بودن به آماده‌سازی اقدامات تروریستی، در ارتباط با پرونده مشکوک پایگاه هوایی RAF Fairford بازداشت شده.
پلیس ضدتروریسم انگلیس گفته این فرد امروز توی وست‌مینستر لندن دستگیر شده و هفتمین نفریه که توی ارتباط با این پرونده بازداشت می‌شه؛ البته تا الان برای هیچ‌کدومشون اتهامی ثبت نشده.
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/72839" target="_blank">📅 18:26 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72838">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d2245088c.mp4?token=oR1RCz5I2jYI2QWfj88TmdSwsAbqzcp87r9ltt6QbjHLlXcwMsJ7bfqlUVN-49z7QhYq6cdU4QO0id3ohZPSEGYA66kKl0FWcCXVqha1b8TU2W9WnI2ri0lY9LVyJIBDYhwXJGdywyOgjxxdJiFrzu7J_YqXYoUrYTQyGrY-aGu4-X38p7iAG_eJa1BBubAlrLUR7GwstsJ_xGgUFWHFhRecjbf3jh22EDu1wCmogAuwWoTvZZehipZLUVEyklrH9Goi3w1tmgp2SwcCpzqHmAdutQQZyWq0C4P8-4x8DXyNHBwmcQ2v61Dmd9mbZYhcJywHll6rwbYnJKxWPfpdHIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d2245088c.mp4?token=oR1RCz5I2jYI2QWfj88TmdSwsAbqzcp87r9ltt6QbjHLlXcwMsJ7bfqlUVN-49z7QhYq6cdU4QO0id3ohZPSEGYA66kKl0FWcCXVqha1b8TU2W9WnI2ri0lY9LVyJIBDYhwXJGdywyOgjxxdJiFrzu7J_YqXYoUrYTQyGrY-aGu4-X38p7iAG_eJa1BBubAlrLUR7GwstsJ_xGgUFWHFhRecjbf3jh22EDu1wCmogAuwWoTvZZehipZLUVEyklrH9Goi3w1tmgp2SwcCpzqHmAdutQQZyWq0C4P8-4x8DXyNHBwmcQ2v61Dmd9mbZYhcJywHll6rwbYnJKxWPfpdHIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مکرون شاهد نخستین شلیک آزمایشی موشک بالستیک جدید M51.3 فرانسه از زیردریایی هسته‌ای «لو ویژیلا» بود.
مکرون:
این آزمایش، اعتبار و قدرت بازدارندگی هسته‌ای فرانسه رو نشون می‌ده:
«برای اینکه آزاد باشی، باید ازت بترسن؛ و برای اینکه ازت بترسن، باید قدرتمند باشی.»
@News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/72838" target="_blank">📅 18:15 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72837">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b292f769f.mp4?token=QdOl0JzC7IA9NQCUXUK5WVGEARi5oRjegI0OYfRzX7PmuD95cWE5kVAnvXcQ7L2CAyOWA4xOb5mB5VRRPpcZ_iH3D3ognqJEaC89qmU5G2K2ahc8IhztKpuJ6APDAlF0HJG5YL0pJAz9pkwykEetnKK8gU_2eibU6JGYcfgp1-p6sMjcIq08ZQdUUo-a0qn_flJFcYq3FxRdcTebD5HLHNuT7IEZIxv4Gg13_nXx7H2hYtD3U514I3_F2gRzaR-WCR_mq4sHmn7fqTo_ILR6NxLPmdm5lKxEnovNSCTtn-kPSMW4VOkb6iNE-O_2y-u7eREji1els5sKa7T7sMScwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b292f769f.mp4?token=QdOl0JzC7IA9NQCUXUK5WVGEARi5oRjegI0OYfRzX7PmuD95cWE5kVAnvXcQ7L2CAyOWA4xOb5mB5VRRPpcZ_iH3D3ognqJEaC89qmU5G2K2ahc8IhztKpuJ6APDAlF0HJG5YL0pJAz9pkwykEetnKK8gU_2eibU6JGYcfgp1-p6sMjcIq08ZQdUUo-a0qn_flJFcYq3FxRdcTebD5HLHNuT7IEZIxv4Gg13_nXx7H2hYtD3U514I3_F2gRzaR-WCR_mq4sHmn7fqTo_ILR6NxLPmdm5lKxEnovNSCTtn-kPSMW4VOkb6iNE-O_2y-u7eREji1els5sKa7T7sMScwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حداد عادل: هر موقع میرفتم خونه و می‌دیدم کفشای لِه و درب و داغون پشت دره، می‌فهمیدم مجتبی خامنه‌ای اومده :))
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/72837" target="_blank">📅 18:14 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72836">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72836" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/news_hut/72836" target="_blank">📅 18:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72835">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/shbHXp5Cxw4ei2HASAxENyv_JWqQX9X23xU8nEjGLqLxxtTP3PJ3XMN1cRXOdeLqZR_TX9y7elGihZEm7OM8lUtyq94ewTxI-H-aUDXRh-4g_MjbBxZsFYfqpSu-crkH7ZnWa3JHAdT5E1l_egUfIjh8YV9kOz3zcDjtkxPrejw3BELus8u8-pw4Ah2UZfAA49HJacelgBRY5POyYZ31fa3oizmiLclWpPzoluliQqonUFJfBSc8hRsMzc77tJ8F8g9iPzrzDwExLhInyx4n_72RBHc7Cj_IXHb4SvgyBhhSiB4jtXCI4bND7erxqEKiIyRZzQZmVyWY6bYLv67dtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول: ۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم: ۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم: ۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم: ۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/news_hut/72835" target="_blank">📅 18:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72834">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">مارکو روبیو درباره مورد مشکوک طاعون در روسیه:
«فکر می‌کنم روسیه باید اطلاعات بیشتری رو در اختیار دنیا بذاره. کاری که باید انجام بدن همینه و امیدواریم همین کار رو بکنن.
ما هم داریم موضوع رو خیلی دقیق زیر نظر می‌گیریم.»
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/72834" target="_blank">📅 17:28 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72833">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab24bbc88d.mp4?token=aamscDhwd7r166cAwdI_A0bsel1gqbH018rmLibAdyLoOVjfQKuSUEzQQU9JAqYu83grZBW3FGaYv1cZKwSJFYU4LqNwfLgOvCdAV542_goLb1RnnKMusK6Vg4VtpqzHetpcl7Qb_z19fD_EN0YuGXmKlem2zYEL4tkNicC3K-_io_IHL-32HotK3Ocl0Zj9Z0je0tGuHo2GtujU7FurdwZh7jmRBExZsqr7iq--1IZRWAXLCVJEANGfvYUUojI_scwK2-HRwjhf1bcd4sdvAc6DVZfFeyCSpYWMvr1fCkw4PVl_Ib6eaxnD6HpOarNb8jwXkYKcqLtoWeiEdNBVZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab24bbc88d.mp4?token=aamscDhwd7r166cAwdI_A0bsel1gqbH018rmLibAdyLoOVjfQKuSUEzQQU9JAqYu83grZBW3FGaYv1cZKwSJFYU4LqNwfLgOvCdAV542_goLb1RnnKMusK6Vg4VtpqzHetpcl7Qb_z19fD_EN0YuGXmKlem2zYEL4tkNicC3K-_io_IHL-32HotK3Ocl0Zj9Z0je0tGuHo2GtujU7FurdwZh7jmRBExZsqr7iq--1IZRWAXLCVJEANGfvYUUojI_scwK2-HRwjhf1bcd4sdvAc6DVZfFeyCSpYWMvr1fCkw4PVl_Ib6eaxnD6HpOarNb8jwXkYKcqLtoWeiEdNBVZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زن بیژن مرتضوی : مردم ایران در دنیای واقعی خیلی خوشحال و شاد هستن ، واکنش ها تو فضای مجازی دروغ هس و حقیقت نداره
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/72833" target="_blank">📅 17:01 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72832">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4be4d4d973.mp4?token=fAE1aXUiLMJ7lb7_7E5BBmct_cRisGst1sHBrA-ImHcj1IUGkdPCkqqx-h4noBaiR00dxghg39BfXLEYSrLnBzWH7HGZoBGFfSgXfaph40NPyx-Cud8_zP8Kf66ygAbyHbQ9SIIw2YzdaUgKBTMRzIMdIoGBfsAUAeQy5tModqLBuwAEO3Hz9wXPfMkXGwltFDzUiF76ArILZ62uqZAURsZTrLx1zxVUSMDHT9zPOGYPyF5fSMYRD33yasnJEf-37CgApXxYQm2w1mbzpjhF9BiIuyxPYxrlC2G6fOETEBd9L4fSVdHDAnJXCzNmI-mwT3CuI9vbR9x1YaKwnqAbnoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4be4d4d973.mp4?token=fAE1aXUiLMJ7lb7_7E5BBmct_cRisGst1sHBrA-ImHcj1IUGkdPCkqqx-h4noBaiR00dxghg39BfXLEYSrLnBzWH7HGZoBGFfSgXfaph40NPyx-Cud8_zP8Kf66ygAbyHbQ9SIIw2YzdaUgKBTMRzIMdIoGBfsAUAeQy5tModqLBuwAEO3Hz9wXPfMkXGwltFDzUiF76ArILZ62uqZAURsZTrLx1zxVUSMDHT9zPOGYPyF5fSMYRD33yasnJEf-37CgApXxYQm2w1mbzpjhF9BiIuyxPYxrlC2G6fOETEBd9L4fSVdHDAnJXCzNmI-mwT3CuI9vbR9x1YaKwnqAbnoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خوش چشم بازم تحلیل کرد و گفت جنگ در پیشه!
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/72832" target="_blank">📅 16:34 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72831">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cd2b481530.mp4?token=gZEphx0wKm5eUfxPRoTRATcgRTbLZZBUDxX5Py6rzbFp83jR3MZSt-1uGgg3AtepOLOnsF4XL5U1NVN-mb1FAO6WVD_UFlEWAhimzXRqDjJadYUwoza3Qef274qvU2imkqFS3Q5jT_cuYEo3yX9bAmQJQ5F-aQMK94-ky7cWoTtsZc-V1hkLyW1DhaA0hO5ln_YFzr-3TZ_v4jQ3SrVrzaAI-HglcWoxRBurjuaiFuRRSSGnH3k-nybMe7tBQHfkQQ7S9nMBzR6lmauIy72Og2aFD32Eka03xpyUbW3Zogv_4xyh9uQtVL3mQcohL5gzUKc4mxRWVNd_-Q0DXGqnEg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cd2b481530.mp4?token=gZEphx0wKm5eUfxPRoTRATcgRTbLZZBUDxX5Py6rzbFp83jR3MZSt-1uGgg3AtepOLOnsF4XL5U1NVN-mb1FAO6WVD_UFlEWAhimzXRqDjJadYUwoza3Qef274qvU2imkqFS3Q5jT_cuYEo3yX9bAmQJQ5F-aQMK94-ky7cWoTtsZc-V1hkLyW1DhaA0hO5ln_YFzr-3TZ_v4jQ3SrVrzaAI-HglcWoxRBurjuaiFuRRSSGnH3k-nybMe7tBQHfkQQ7S9nMBzR6lmauIy72Og2aFD32Eka03xpyUbW3Zogv_4xyh9uQtVL3mQcohL5gzUKc4mxRWVNd_-Q0DXGqnEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدنی وزیر دلقک اقتصاد: درمورد قیمت ارز از همتی سوال بپرسید.
خبرنگار: همتی هم گفت از شما سوال بپرسیم.
مدنی دلقک: نه دروغ میگه از خودش بپرسید.
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/72831" target="_blank">📅 16:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72830">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cac062b9b9.mp4?token=t0lhJ3DdJMv08yPBD8qNiDqxi_23Gze6IYq1lu7g4IqqM9nLNqfiQRMuGjY-kxL8bmE91TuuQeB021fucSBJzX-YXZGhnDaRWPROLQiKVwxX_affWE1bxv4OFjutVXTQS9hqei2kh5j-QhocaXLbER3xukyFAldeNcesKwwvW2MmHGSuN4PKKIldn-ez_kOv1-wABPqiyKgNTndY7aqJIPLly-oskxMVgDCkTMbsywW_OcqpsYEgwtFttzsLDfE6u5vHJW_zYqyDM8L97zCltL1sEaZdYMd2AuQ3hpOGVusp9iD4nX8MVp61xSAoIJX6SKJDW1B9e7cadzJQxs0gQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cac062b9b9.mp4?token=t0lhJ3DdJMv08yPBD8qNiDqxi_23Gze6IYq1lu7g4IqqM9nLNqfiQRMuGjY-kxL8bmE91TuuQeB021fucSBJzX-YXZGhnDaRWPROLQiKVwxX_affWE1bxv4OFjutVXTQS9hqei2kh5j-QhocaXLbER3xukyFAldeNcesKwwvW2MmHGSuN4PKKIldn-ez_kOv1-wABPqiyKgNTndY7aqJIPLly-oskxMVgDCkTMbsywW_OcqpsYEgwtFttzsLDfE6u5vHJW_zYqyDM8L97zCltL1sEaZdYMd2AuQ3hpOGVusp9iD4nX8MVp61xSAoIJX6SKJDW1B9e7cadzJQxs0gQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مراد ویسی:
اسرائیل توی ۱۴ ماه گذشته اسم ۱۴ تا خیابون و بزرگراه توی تهران رو عوض کرده! اونی که عملاً داره اسم خیابون‌های تهران رو تغییر می‌ده، اسرائیله؛ اسرائیل همین‌جوری مقام‌ها و فرمانده‌های سپاه رو می‌زنه، بعد شورای شهر میاد اسم همون‌ها رو می‌ذاره روی خیابون‌ها!
دفعه قبل هم بعد از جنگ ۱۲روزه، اسم چند تا خیابون و بزرگراه رو گذاشتن به اسم حاجی‌زاده، سلامی، باقری، رشید و شادمانی؛ یعنی اسرائیل اینا رو می‌کشه، شورای شهر هم جلسه می‌ذاره که خب حالا اسم کدوم خیابون رو بذاریم به اسمشون!
در واقع اونی که داره اسم خیابونای تهران رو عوض می‌کنه، نتانیاهو و موساد و نیروی هوایی اسرائیله؛ شورای شهر فقط می‌مونه و تابلو رو عوض می‌کنه!
با این حساب، اگه همین روند ادامه پیدا کنه، باید منتظر باشیم هر بار اسرائیل یه مقام دیگه رو هدف قرار می‌ده، تهران هم یه خیابون دیگه به اسمش دربیاره!
یعنی خلاصه تقسیم کار اینه: یکی می‌زنه، یکی تابلو می‌زنه:)
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/72830" target="_blank">📅 15:23 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72829">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KL393hn6QS1HbnfjKMUhA0G_VPaZe7nHSvBiJDhgbthiMTHyaAWmorqalJX6wqwBvjflRPcQdp5QENuOtGH7wOQucVq8W32Q7eIAcYQQqShgDlhDjyoBfUo_ou4T_Bnz7IZ9ahUognHuykYYLpnPTTBIzqnJRdmru2cDJlqtqJ1CCSAu-5WWU78mVMAxwDzNSSsFf4dic4AXehzbYQ1nRB7fevrn7gaIPUMqwF6aVM0ROX1TXfCAzbJ5ATrlkaU4fraTuJvljEBW7VI6Hhl41VhZHZ6wJsKoxSS4-hMFmUKUIKsOYqa8ysgPI5scDnGpX4MUrj3LacgNI5ccZm2aWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشماتون بریزه از تاثیر سهمیه! توی کنکور امسال یه نفر رتبه‌اش ۸۱ هزار شده بوده،
که با سهمیه ۲۵ درصد، رتبه‌اش ۲۸۳ شده!
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/72829" target="_blank">📅 15:01 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72828">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2512f994a.mp4?token=ekjSgKDrDLyn03Gr9ZQXefnP2BvAPRQCdDdREMUoHJPEhk4Erh89Eol3OMTAF3JzkuiHtue1glN-ztzMXJYRPh7vf23njDMdrjlmckCsdJYsjCfozETdcyjOQZdUjyDP2SeSN7WrHB0lg6nVQwEW4J8mhRdAjJzWCjWbzYigBFHiGiPuLstVCt2cfKrX7uYkRlOWsVQUZNmCdbNW2EovsQR0_he5OWk7zPO_p8itkz69EBJtzWSphRSFSkRzQYQ61O6qlPPk049QQwrFbA-POVbXTp85Gu5hWJcM-j1Q_fD5DPlVum0jMVBnrcxLK2B8c3HOalp9GQ3ku3iQ0fv0AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2512f994a.mp4?token=ekjSgKDrDLyn03Gr9ZQXefnP2BvAPRQCdDdREMUoHJPEhk4Erh89Eol3OMTAF3JzkuiHtue1glN-ztzMXJYRPh7vf23njDMdrjlmckCsdJYsjCfozETdcyjOQZdUjyDP2SeSN7WrHB0lg6nVQwEW4J8mhRdAjJzWCjWbzYigBFHiGiPuLstVCt2cfKrX7uYkRlOWsVQUZNmCdbNW2EovsQR0_he5OWk7zPO_p8itkz69EBJtzWSphRSFSkRzQYQ61O6qlPPk049QQwrFbA-POVbXTp85Gu5hWJcM-j1Q_fD5DPlVum0jMVBnrcxLK2B8c3HOalp9GQ3ku3iQ0fv0AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کشور چین واقعا عجیبه، روی یه شهرک یه شهرک دیگه هم ساخته شده. شبیه فیلم inception شده.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/72828" target="_blank">📅 14:28 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72825">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pkx5WzJKSJz0vjYc-qarBhxdKLHhlyolOzYzO6z_3y2P2zT-VyUWRikOKRYkhulrvq_IBHALEjb_HVSbwis3IRYw1FX-imXkWJCT9f6-00E_Twa0Ye0vThszfFKYc9RPjIKqfvV9Eygm1DJpE6OpybQCeaCoUivDDdOXwYVX1CE3cTz6Bj8hnL-i5GNvv-Cmoc6Br8cgWzEtPmIPQJZVyiealJTREAKeJcZc60wTN9l8ktk2-MJ753-v8L2dlDdwW1x32irXyZtkTADbpTGwV0EryFTM2lhI8JfLpb_prPqc4QkLaQQtgZdNF7BySt-0TPWtPtlLOaW35oDvFcE6Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pOAcZdAzUciwkpoe2N5YAjo7XQTZErn_5QS0WtvxXn0fTSrhkcjpSfQHrzYx6hgFEj5t-RPMu5rtuqoQIhmEG7dXttXjB5spQ0lviTK0SWB0oGoCpt1VaSKPbUS4H9qB4H28BXuDThSj8nsx-bW-WNDeqBLafQGLu5dmN0fd_7Sj5Ohpx_-Mlxv-f6wfiFrH4LVKDAh8sHU6gbsZvyt1CHzPP5pc8HJKoXZisuaRoSaQCODDm_Z1fgUfgxzc0GgGW-1xQFtfXbzIagimSSq1khGavrluKRTqy1d7qYFiSviFNsE8Zcuwb38pjsb8SSerzMC4exo2AtSkob3i3JjPOQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e31c23155.mp4?token=UPYhWaCzx5NZMUkUEpKcnPDbfxTHdU7nRvG_nzZ5pU7fQJlWwu29MpWjLDdHZjxhZFzJKyeNUj9S1Xllw7CyLljpB-2aFnLUqfigok_2m5xtXB6qlangWPTFbpEIGCJhnJrt17LlSNVWeTT-fYX-5_k-fRBtjZBg7hMZQkQyKJzJczo3IaRaJd7k4nJuPiOcMyutzUoXLGFC5eb1PVtYBdBtsMUwPGaa9V6qWVqBUlBiQRC4nXizrPuUfZeQp43_XXtWSDdnLcz7GfQrEBWxIbUCleyc9-p5KHP_Bj6t05VCZDhXpZZEbe4pNfQlZsaNxB-F8fYnyjCbt2JwrGj8wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e31c23155.mp4?token=UPYhWaCzx5NZMUkUEpKcnPDbfxTHdU7nRvG_nzZ5pU7fQJlWwu29MpWjLDdHZjxhZFzJKyeNUj9S1Xllw7CyLljpB-2aFnLUqfigok_2m5xtXB6qlangWPTFbpEIGCJhnJrt17LlSNVWeTT-fYX-5_k-fRBtjZBg7hMZQkQyKJzJczo3IaRaJd7k4nJuPiOcMyutzUoXLGFC5eb1PVtYBdBtsMUwPGaa9V6qWVqBUlBiQRC4nXizrPuUfZeQp43_XXtWSDdnLcz7GfQrEBWxIbUCleyc9-p5KHP_Bj6t05VCZDhXpZZEbe4pNfQlZsaNxB-F8fYnyjCbt2JwrGj8wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم یکی از همون ناوهای آمریکاییه(USS Delbert D. Black (DDG 119)) که سپاه تو بیانیه‌ها گفته بود موشک بالستیک خورده و «خسارت قابل‌توجهی» بهش وارد شده. ولی خب، به نظر من برای ناویی که موشک بالستیک خورده و خسارت قابل‌توجه دیده، زیادی سرحال و سالمه!
الانم برای استراحت چند روزه خدمه، وارد پوکت تایلند شده و بعد از تمیزکاری جلبک ها مثل روز اولش می‌شه!
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/72825" target="_blank">📅 13:36 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72824">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdf3b5b159.mp4?token=OvAhr7R5Y8fIY9dVDOTyyQ5Eq54JaN3bKHC0Nnc-DgNQ5xh1D0mJNQvh7WFQ5DCdWk7riR8_BEb60uVwms40c_qmVnjkg8HfwVdbwqRCywEy7-bJcWjmCRd-CsdeVtD5mR11mHnDqJ6wZbiHW3Jb0iMoS87EK5p6m1l0MEuVzh2TBaoDyjC7EdYk9ndGgfABn72FRy5T3bbYebeOez1ZfQMqr22JlLixkG6k2-NONCEAxX2e4tLzEOjBIw_xT17wFdXLG4vMoMoRnSNMdTr4IO5f36M3drX6YqMifHDzl5sTGPLIjJQzF7uUE3FmbBqMPjrc5pdrUfRHnl8spCEhXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdf3b5b159.mp4?token=OvAhr7R5Y8fIY9dVDOTyyQ5Eq54JaN3bKHC0Nnc-DgNQ5xh1D0mJNQvh7WFQ5DCdWk7riR8_BEb60uVwms40c_qmVnjkg8HfwVdbwqRCywEy7-bJcWjmCRd-CsdeVtD5mR11mHnDqJ6wZbiHW3Jb0iMoS87EK5p6m1l0MEuVzh2TBaoDyjC7EdYk9ndGgfABn72FRy5T3bbYebeOez1ZfQMqr22JlLixkG6k2-NONCEAxX2e4tLzEOjBIw_xT17wFdXLG4vMoMoRnSNMdTr4IO5f36M3drX6YqMifHDzl5sTGPLIjJQzF7uUE3FmbBqMPjrc5pdrUfRHnl8spCEhXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه خانم طرفدار حکومت:به پسر نوجوانم گفتم اصلاً نگران نباش!
خواستی سیگار بکشی، بگو خودم برات می‌خرم؛
خواستی قلیون امتحان کنی، با بابات می‌بریمت سفره‌خونه؛
فیلم مثبت۱۸(پورن) هم خواستی ببینی، بیا با هم ببینیم! این‌طوری دیگه خیالم راحته که همه‌چی کاملاً تحت کنترله!»
@News_Hut
😐</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/72824" target="_blank">📅 12:46 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72823">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e258d805f.mp4?token=fc1ev3fgcI-e8CQwAF6XswIK9bD_UQ-Qz8timcjXDdkwPzD50Doiu8-dCeubxmWuvP301Lr2q2m2vPj9d8_pK6kY230m1RDvyQ8GsajvyyAW8QnhXxSWlK15UlF4tTEAQNNAsN-cKohjbDZhk7ipfi6x_Cu3LqF4BpyVIFRu1Df0vZBtM468CbN4mvtI3_154m72KghXCIuePEiLIDOgqEYtLAHCz83CfmAPrxzSyB7IUBaq7RKs1SeYd4rQBxINjOI4QKKp2-F8fXjAdyAz9wrbzg8KX80ZIR81B5F2AC1fL-no1Ogm_Rcp6CXw-y7DpDErqXY4s6lEHirj8S04QA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e258d805f.mp4?token=fc1ev3fgcI-e8CQwAF6XswIK9bD_UQ-Qz8timcjXDdkwPzD50Doiu8-dCeubxmWuvP301Lr2q2m2vPj9d8_pK6kY230m1RDvyQ8GsajvyyAW8QnhXxSWlK15UlF4tTEAQNNAsN-cKohjbDZhk7ipfi6x_Cu3LqF4BpyVIFRu1Df0vZBtM468CbN4mvtI3_154m72KghXCIuePEiLIDOgqEYtLAHCz83CfmAPrxzSyB7IUBaq7RKs1SeYd4rQBxINjOI4QKKp2-F8fXjAdyAz9wrbzg8KX80ZIR81B5F2AC1fL-no1Ogm_Rcp6CXw-y7DpDErqXY4s6lEHirj8S04QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سال 2023 یه میم به نام Opium Bird خیلی وایرال شد که یه موجود بزرگ و پرنده‌مانند تو کوه‌های برفی رو نشون می‌داد و سازنده‌اش گفته بود که سال 2027 (۲ ماه و ۲۶ روز دیگه) می‌فهمید یعنی چی؛
حالا شباهت Opium Bird و طاعون
👺
و همچنین لوکیشن برفی اون میم و آب و هوای روسیه، دوباره همه رو داره به این فکر فرو می‌بره که نکنه داریم وارد یه سیزن جدید می‌شیم...
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/72823" target="_blank">📅 11:59 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72822">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9dc05a4717.mp4?token=lH0WYLhnvzWk-gRy4Ii-HuX9ZenrnjDou6REaa8qXEoCr_e0A2NcC-rkeVS9Y2cyjpCqosu_b_CcE1lsesG5kfJpZGV4H63Gi4rDlawoUtSbv877Bb7dDwOp1aQdt3aKiTjGKgZmbMzytIvXf4LwfwavaSYBtf87atl9Skt-WblS3CHpKNHHTd9v0KcQI19q5gmN0OXhjKVEJwfw774xNnH1p_VuWMsCKA6RcaKs6w2lh_4NRfluXG1L17CWwtkqxsYzmRN94BRYRb7bZPSqPgSGj9EL8-NzJuIzugR_U0snuLq_dqOnfuvih6K3rRoCLovRwqBDOLJ-ctfhgwKmnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9dc05a4717.mp4?token=lH0WYLhnvzWk-gRy4Ii-HuX9ZenrnjDou6REaa8qXEoCr_e0A2NcC-rkeVS9Y2cyjpCqosu_b_CcE1lsesG5kfJpZGV4H63Gi4rDlawoUtSbv877Bb7dDwOp1aQdt3aKiTjGKgZmbMzytIvXf4LwfwavaSYBtf87atl9Skt-WblS3CHpKNHHTd9v0KcQI19q5gmN0OXhjKVEJwfw774xNnH1p_VuWMsCKA6RcaKs6w2lh_4NRfluXG1L17CWwtkqxsYzmRN94BRYRb7bZPSqPgSGj9EL8-NzJuIzugR_U0snuLq_dqOnfuvih6K3rRoCLovRwqBDOLJ-ctfhgwKmnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
«همه دارن می‌گن من GOAT ـم، یعنی بهترینِ تاریخ.
من می‌گم: «پس واشنگتن و لینکلن چی؟» اونا هم می‌گن: «شما از اونا هم بهتری، آقا!»»
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/72822" target="_blank">📅 11:28 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72821">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/affe4d122e.mp4?token=cqIEOR2Y48ecJOCEBL79_MqGCTdilsTHAyNwaFj_J51UdQRuxWU4GYCgLoU1pCYddAIcNtyBEXjAgYI6VTpB24r3FScIsEo-qb9sEBzkKgQUmT4MipF9qkZhb3BLWCA50jwWR4vMDNWuQLS5P457SIuzatDIZeQ1qRlw9KdBhuIvqPtlvComHAC3StFqpxJWSwLH2P7JcdWd1VcnVB1vhiQkWSZlyePOzU2nNs3xLkNuHw7sRT-YkB1NcOvuNRW7LSH2ntXosbz8ht3ljpE0n5tV0gp95D75uyJQKlWcmgMEvZyGn6qHTs0_12lP2CVBatwZRFBIxoX8CvSpsd-rzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/affe4d122e.mp4?token=cqIEOR2Y48ecJOCEBL79_MqGCTdilsTHAyNwaFj_J51UdQRuxWU4GYCgLoU1pCYddAIcNtyBEXjAgYI6VTpB24r3FScIsEo-qb9sEBzkKgQUmT4MipF9qkZhb3BLWCA50jwWR4vMDNWuQLS5P457SIuzatDIZeQ1qRlw9KdBhuIvqPtlvComHAC3StFqpxJWSwLH2P7JcdWd1VcnVB1vhiQkWSZlyePOzU2nNs3xLkNuHw7sRT-YkB1NcOvuNRW7LSH2ntXosbz8ht3ljpE0n5tV0gp95D75uyJQKlWcmgMEvZyGn6qHTs0_12lP2CVBatwZRFBIxoX8CvSpsd-rzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«این جنگ خیلی زود تموم می‌شه و قیمت‌ها هم قراره حسابی بیاد پایین. شاید حتی خودتون بگید: «خواهش می‌کنم آقا، این‌قدر سریع ارزون نشه!»
😂
خودتون ببینید تو یه مدت کوتاه قراره چه اتفاقی بیفته.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/72821" target="_blank">📅 11:26 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72820">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67e9f8cbdc.mp4?token=ro-30RsLBNDOsoxnAfvwT1naYQV041Io4VQ3sBu3FgVGT0pvNUbXkbSNcaOEE9aWsY9oxGB8PIlRihru2KW7A0lN35nnKGFuyPBeC0b4XOBxK97NHhW7a9dliprW78x4YPWtHfYWLITHmHo1nrIk6t-lfsy7303aBwz5IUPxcU8zF9juX8GrCdgczDvV_3_kbNBXa2vW9pwV7FemvL1-_pLEBcFxXcXXPKOwMRTtWpEIlz-zfV87Om590x7gKgm4veEtJKNkEzHL0IhYKF9l7ncIS58xiDawTKcYAIu3Z8-W_VH9sEtborrZIjgr3YCqC73lDPEzWno2fVSRxcJvDgQ-uekcnV2s-X_nc1J1ktEloz95ABwbjaTJJb6waPzGk7cC_otIHM594E-kgXUK8aw2RqUlIMo-3txPrR3IpysmfgC4QqGgvCwcLogsldpcmLfeTOD1Aoaz-XeR6LU1_F39oa8urSDvHxxhIMOn4sf4uy_sk4S54BXn65QVKK5A4QJICebYWQAf0H4A01ZqLdoHvu2PhSKGgX5D7q9y7H6xkbao0aKqxKZEU1G68ODFA0rinKBdqy8UqmsTtBPtdHlkWj_YZ32tlkf9eHQBfNAmwh2mXb0R58wBVuHwU3ErDMEUr-XtS07JPZAsRBvxqRiFxtU0iVMHzR28PPsRBsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67e9f8cbdc.mp4?token=ro-30RsLBNDOsoxnAfvwT1naYQV041Io4VQ3sBu3FgVGT0pvNUbXkbSNcaOEE9aWsY9oxGB8PIlRihru2KW7A0lN35nnKGFuyPBeC0b4XOBxK97NHhW7a9dliprW78x4YPWtHfYWLITHmHo1nrIk6t-lfsy7303aBwz5IUPxcU8zF9juX8GrCdgczDvV_3_kbNBXa2vW9pwV7FemvL1-_pLEBcFxXcXXPKOwMRTtWpEIlz-zfV87Om590x7gKgm4veEtJKNkEzHL0IhYKF9l7ncIS58xiDawTKcYAIu3Z8-W_VH9sEtborrZIjgr3YCqC73lDPEzWno2fVSRxcJvDgQ-uekcnV2s-X_nc1J1ktEloz95ABwbjaTJJb6waPzGk7cC_otIHM594E-kgXUK8aw2RqUlIMo-3txPrR3IpysmfgC4QqGgvCwcLogsldpcmLfeTOD1Aoaz-XeR6LU1_F39oa8urSDvHxxhIMOn4sf4uy_sk4S54BXn65QVKK5A4QJICebYWQAf0H4A01ZqLdoHvu2PhSKGgX5D7q9y7H6xkbao0aKqxKZEU1G68ODFA0rinKBdqy8UqmsTtBPtdHlkWj_YZ32tlkf9eHQBfNAmwh2mXb0R58wBVuHwU3ErDMEUr-XtS07JPZAsRBvxqRiFxtU0iVMHzR28PPsRBsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«یادتون باشه، این جنگ یه چیز مصنوعیه؛ یه مقدار هزینه‌ها بالا رفته، ولی خب برای اینکه دنیا امن بمونه، قیمت زیادی نیست.
اگه اونا بتونن یه شهر رو بزنن، بذار لس‌آنجلس یا سن‌دیگو رو بزنن؛ این در برابر حفظ امنیت دنیا، قیمت خیلی کوچیکیه.
در واقع، این ماجرا تقریباً دیگه تموم شده.»
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/72820" target="_blank">📅 11:25 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72819">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb2e238707.mp4?token=SjJdEueXSTbXAodxlguJuK8fXAOYpVJntHXsOT-KLn0pDQcIK2mStp6iVj3jOn0gfKpdPn_08fUKCB3zOrjj82L_x-xp9YEt4DzTH1kFOodqiPT5yVCuRk9Zc_VBTCwDpw-iMo1ulruErggfJTotJx3YxMl2UY9kwRE5RPbLgtp5JXurvhADrff2Cji2PLfxs5EHp_Nhl0OA737sFUQ_4GAfkdrxsEsMsEU3QqllVMmxvpDNIpsgiJIsI4PJwYJ9ivcN7wnXPlKLjGTB-t76dy1uIHekZvcG7ElhtQxWInZ45-eheBE0gCCcJhtde26gHc9B-rCFVsKo1ADOUWWcTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb2e238707.mp4?token=SjJdEueXSTbXAodxlguJuK8fXAOYpVJntHXsOT-KLn0pDQcIK2mStp6iVj3jOn0gfKpdPn_08fUKCB3zOrjj82L_x-xp9YEt4DzTH1kFOodqiPT5yVCuRk9Zc_VBTCwDpw-iMo1ulruErggfJTotJx3YxMl2UY9kwRE5RPbLgtp5JXurvhADrff2Cji2PLfxs5EHp_Nhl0OA737sFUQ_4GAfkdrxsEsMsEU3QqllVMmxvpDNIpsgiJIsI4PJwYJ9ivcN7wnXPlKLjGTB-t76dy1uIHekZvcG7ElhtQxWInZ45-eheBE0gCCcJhtde26gHc9B-rCFVsKo1ADOUWWcTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: جنگی که علیه ایران راه انداختیم برای «
نجات دنیا
»ست!
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/72819" target="_blank">📅 11:23 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72818">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/225b755540.mp4?token=MjC6E44AMfyGYPS0TKzw4fQqO-qCfXQbnjqHrC-f-IViszR9veirmnTzMP8xzLMx7daV8l43rjOjyQ0r60NvAM4M52EvegQisTfcH3J8Gr_RSG9ntYP6kYllCsszISgMNVd2QpKkrsJFmwx3y5aNBIAeZPpYrfghr9gzaDwxbmOeg8DbuQ3Wfz64581Vq4CNm0yxdKF6OtPfyuQvwb0OSdKgetyF8fAVrfBlJF8pkl_R6z1eEyBMEj-aqaIw1tzjbIeIepGPTckWCKVtdT9H2S1odZqvKjdJOzpQcdEzuzXTKXUBE-1MCLaQVEhM9IyQMGXzwOJRIs3v3JruOtca44WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/225b755540.mp4?token=MjC6E44AMfyGYPS0TKzw4fQqO-qCfXQbnjqHrC-f-IViszR9veirmnTzMP8xzLMx7daV8l43rjOjyQ0r60NvAM4M52EvegQisTfcH3J8Gr_RSG9ntYP6kYllCsszISgMNVd2QpKkrsJFmwx3y5aNBIAeZPpYrfghr9gzaDwxbmOeg8DbuQ3Wfz64581Vq4CNm0yxdKF6OtPfyuQvwb0OSdKgetyF8fAVrfBlJF8pkl_R6z1eEyBMEj-aqaIw1tzjbIeIepGPTckWCKVtdT9H2S1odZqvKjdJOzpQcdEzuzXTKXUBE-1MCLaQVEhM9IyQMGXzwOJRIs3v3JruOtca44WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«راستی، داریم حسابی ایران رو می‌کوبیم، اینو که می‌دونید دیگه؟!
در هر صورت، این داستان خیلی زود جمع می‌شه.»
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/72818" target="_blank">📅 11:21 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72817">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72817" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/72817" target="_blank">📅 11:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72816">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GI-W-26YJJiU6pLXKGar5HW1nwNkueUjTcYS9o4u0C_lUEFxLg5VlZDjOAIr5g80ZJ9f0pV00zxldmC6BWBow8X-0WA2m22BNDLtq7zd6I2cEzLGQNkM_5tDuqd6Q3JtHFOO8OHlhAwzwhaJobxWzr1Z_F1IxMFtMW9NS0_idry4FZLMRJtTpMIqv4BeusQeaA_a8iHU9xe6y1HopLSljl2uqh6gy41JFrEdOgvYBQbme_Z88vv4amkhR6Ktyvyw2VzPTNuGeAkSciWMGd3EPmw37J3hgYisjL6Hu1lcRQ4sWlKecu9EnTpcEs7USgzbZEbEH4XB6-ih800jxLvuYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
اسپانیا
🆚
کرواسی
چک
🆚
انگلیس
اسلوونی
🆚
اسکاتلند
مقدونیه شمالی
🆚
سوئیس
ازبکستان
🆚
کره‌ جنوبی
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
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/72816" target="_blank">📅 11:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72815">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c201257b1.mp4?token=JXIc_eXXOjFkAiRteWjtYjlq0EmCg1SKphEdi83qJo2a2L3UOPJI4syj7AcRARo-sHrJB3i6TJGdLb1J1WDiN5Pyx0iOwbW1o7ijVXErpJ94dNSdgpFOPOFsUVWMY_X_qKovuN0ldK_7K2cFiIxh403qLeK_onRD4SccC08ncyV0Qn1mjPo0UFfhKAX4QLrk1uOxSQSji4qjJLmEiCGBwFOul2Tl9HaX2AHslnszFwnJJZQRwXcmxyWStZbmQ4AGh80HoA7McIQae_YrSHNDPfKq7YEveJBwN7UmbsCLzc9bQcs9wzyQX74jFHDhN33e_yDbbT3-FMIWhrDkzde7ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c201257b1.mp4?token=JXIc_eXXOjFkAiRteWjtYjlq0EmCg1SKphEdi83qJo2a2L3UOPJI4syj7AcRARo-sHrJB3i6TJGdLb1J1WDiN5Pyx0iOwbW1o7ijVXErpJ94dNSdgpFOPOFsUVWMY_X_qKovuN0ldK_7K2cFiIxh403qLeK_onRD4SccC08ncyV0Qn1mjPo0UFfhKAX4QLrk1uOxSQSji4qjJLmEiCGBwFOul2Tl9HaX2AHslnszFwnJJZQRwXcmxyWStZbmQ4AGh80HoA7McIQae_YrSHNDPfKq7YEveJBwN7UmbsCLzc9bQcs9wzyQX74jFHDhN33e_yDbbT3-FMIWhrDkzde7ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوستاد خوش چشم: اگر آمریکا بمب اتم بزند، ما هم پدر بمب‌ها را به آمریکا می‌زنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/72815" target="_blank">📅 11:04 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72814">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/796b47b54e.mp4?token=GpBBB6lKkFscfN2fS9_IRBI3akq2qbypPSR04mypONxdJQcI1pj2m-bdzZlfKs5eWv1SBHKfvGelLLjwj73ufwys5cp_2KVnW56BfWfViPP8x4sqilIIvrpZMUYhD2vOUfsetXG0AUhsEyjlwmvpyYzLK6rZuLZ3tsJk9eMlGZ8yMjgm-FNRxPwEpPMfjM3U6L1rcCzzXwWrJO02QjOzguUKnPbs8r02RR6VDEcl-uGo_UwMDnyu_rXOpuD4NVwXEQvZr1jCLLKgnAp_vWkJpT3e8F3rdMNvd1I8PKESaPjvM92nWhvUJMyT69AU_Y5HDlpkUdBYAOhRfKRAA-wEOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/796b47b54e.mp4?token=GpBBB6lKkFscfN2fS9_IRBI3akq2qbypPSR04mypONxdJQcI1pj2m-bdzZlfKs5eWv1SBHKfvGelLLjwj73ufwys5cp_2KVnW56BfWfViPP8x4sqilIIvrpZMUYhD2vOUfsetXG0AUhsEyjlwmvpyYzLK6rZuLZ3tsJk9eMlGZ8yMjgm-FNRxPwEpPMfjM3U6L1rcCzzXwWrJO02QjOzguUKnPbs8r02RR6VDEcl-uGo_UwMDnyu_rXOpuD4NVwXEQvZr1jCLLKgnAp_vWkJpT3e8F3rdMNvd1I8PKESaPjvM92nWhvUJMyT69AU_Y5HDlpkUdBYAOhRfKRAA-wEOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایران هر روز ترسناک‌تر میشه، یه پدر برای اینکه پسر 3 ساله‌اش رو تنبیه کنه، یه بسته مداد رنگی 24 تایی رو فرو کرده توی باسنش!
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/72814" target="_blank">📅 10:33 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72813">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0246c863e9.mp4?token=DoANQgeZl-KB-sBE0bM-tass19dc8odO5EIFXqguU4pMSN7Y7K93MJzXCOHjIFKGirwxk8DuaI4deFUMJDA_SkpPhlUk2MUznL61sE1PSODOzNnZALLpyivgO4YItT_h-K2YtoChNxQ6HtGvRxsaYa3Ll8WzNeckVLcUGBnJ5WUPJw7RjOtcF73Se8gb0OtZZeaM6zzP-bc8ER1UVFxNdg_3kfTDC_ulaeZd5PFkDWRx3sM62U_hezVJLXV4McvoL55PpITQJHlm_N5pRS6bGZ2hqWa42yf5DJ3brcg7MNj96_XzweNxoS1e66XMdEVx7KZzpKnFo7SAbbpt5VTP2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0246c863e9.mp4?token=DoANQgeZl-KB-sBE0bM-tass19dc8odO5EIFXqguU4pMSN7Y7K93MJzXCOHjIFKGirwxk8DuaI4deFUMJDA_SkpPhlUk2MUznL61sE1PSODOzNnZALLpyivgO4YItT_h-K2YtoChNxQ6HtGvRxsaYa3Ll8WzNeckVLcUGBnJ5WUPJw7RjOtcF73Se8gb0OtZZeaM6zzP-bc8ER1UVFxNdg_3kfTDC_ulaeZd5PFkDWRx3sM62U_hezVJLXV4McvoL55PpITQJHlm_N5pRS6bGZ2hqWa42yf5DJ3brcg7MNj96_XzweNxoS1e66XMdEVx7KZzpKnFo7SAbbpt5VTP2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دو تا از لوکس ترین مدارس بالا شهر تهران که شهریه شون یک میلیارد تومنه!
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/72813" target="_blank">📅 10:04 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72812">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84c2a17b7a.mp4?token=chbMkY507FWQsZUGCorupsIfv8KYDQusyQxPdsP57XtBHp2i7u4nKmkg9ldyhWyV3UN1uLZuOBAbJZfcoXAF0mnG2fcw4LzTbAeeQD9WUIGLq2kRfXeqfOWcfYA7Wpz3Z0x-6YrHXQ4UgDGU7ptwrZNGhnxtTEwlffOjQZboM-oqblRIBYi0paPJYqZhGPEQVMrJyuV2rqZsnwU72y3MutzwwuAh1qwY1jJSJ2yiL-zZwXfMjCYWfqgO1etuH5PrThb9fN1sbHsaBiTs5e0qirfBAOrDvg0j9egEUkxXUvZtFCv0GXoW1pWQkcuX5aHzTzRx7c37B9ODbIsqZzXJOHgV9kw1dVJbNDBK7royF93saZABBLnnL9ddvKedYZVJnq77saJ0F6-C3mlvLfMdgaU5aleyLQsiBz-0aGAb5LXFMEpWs_QeQWvF-upzO4_xHby6vdHJhG-e8oK5uJIrot2TpRU7yawbxWjqARg4QGGR3V3Qc28tg7116HW5Qwgmmg6EtKu7GcGIPlWWWA1EXObl2F5oQuHUaHTIlx5KcwZkSHZIY_GdmXPlYR1QU0xccpnT7ObFsGDaiPzQQ8w18ciJVEBp-IhykuW7hHUv-kXxTVu8gHyaSxtUOcsWoUIX_QsPm579-p7dSYWCTAHd5zxIYrnZt56M7-WvT0rFmwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84c2a17b7a.mp4?token=chbMkY507FWQsZUGCorupsIfv8KYDQusyQxPdsP57XtBHp2i7u4nKmkg9ldyhWyV3UN1uLZuOBAbJZfcoXAF0mnG2fcw4LzTbAeeQD9WUIGLq2kRfXeqfOWcfYA7Wpz3Z0x-6YrHXQ4UgDGU7ptwrZNGhnxtTEwlffOjQZboM-oqblRIBYi0paPJYqZhGPEQVMrJyuV2rqZsnwU72y3MutzwwuAh1qwY1jJSJ2yiL-zZwXfMjCYWfqgO1etuH5PrThb9fN1sbHsaBiTs5e0qirfBAOrDvg0j9egEUkxXUvZtFCv0GXoW1pWQkcuX5aHzTzRx7c37B9ODbIsqZzXJOHgV9kw1dVJbNDBK7royF93saZABBLnnL9ddvKedYZVJnq77saJ0F6-C3mlvLfMdgaU5aleyLQsiBz-0aGAb5LXFMEpWs_QeQWvF-upzO4_xHby6vdHJhG-e8oK5uJIrot2TpRU7yawbxWjqARg4QGGR3V3Qc28tg7116HW5Qwgmmg6EtKu7GcGIPlWWWA1EXObl2F5oQuHUaHTIlx5KcwZkSHZIY_GdmXPlYR1QU0xccpnT7ObFsGDaiPzQQ8w18ciJVEBp-IhykuW7hHUv-kXxTVu8gHyaSxtUOcsWoUIX_QsPm579-p7dSYWCTAHd5zxIYrnZt56M7-WvT0rFmwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: خبر داری دلار شده ۲۷٠ تومن؟
یه خانم تو تجمعات: اره ولی ما بخاطر وطنمون اومدیم، اگه ما نبودیم دلار حتی گرون ترم میشد
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/72812" target="_blank">📅 09:34 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72811">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea4d885120.mp4?token=quN5aUXujbDc4mA80EqVBq8VlWSCKLfeeaireqcWtv4bW7oI_YQQzICd0vpyiveLQnvCBnE7zp0SzEapwQrIOBCrRebxBJ3-Yn2RCMqHA2RvjddcCq_oGm-lIrRq3yE715BSL85sdzcaOSKlYVJJsoh0tu9IZmZn9ShPhNpohye9X5l2LDeb3V9Bir4aRFr0JBjJedPCKVCogXs7Am6wuwFJjcjDuvCu9AH_NYi8b-yPk_FEPgOQ2gIFAAWh_cb7Hx9Lb9KgbL54G7m5ey-V2bgSi09rQ2W92_YC3KWiW63G7N9kJvQWRQwgvXGdoh1jh-jKBT_cdgx9K9u48P35DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea4d885120.mp4?token=quN5aUXujbDc4mA80EqVBq8VlWSCKLfeeaireqcWtv4bW7oI_YQQzICd0vpyiveLQnvCBnE7zp0SzEapwQrIOBCrRebxBJ3-Yn2RCMqHA2RvjddcCq_oGm-lIrRq3yE715BSL85sdzcaOSKlYVJJsoh0tu9IZmZn9ShPhNpohye9X5l2LDeb3V9Bir4aRFr0JBjJedPCKVCogXs7Am6wuwFJjcjDuvCu9AH_NYi8b-yPk_FEPgOQ2gIFAAWh_cb7Hx9Lb9KgbL54G7m5ey-V2bgSi09rQ2W92_YC3KWiW63G7N9kJvQWRQwgvXGdoh1jh-jKBT_cdgx9K9u48P35DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آجرلو عضو تیم مذاکره‌کننده:
بابا بالاخره یه جایی باید قبول کنیم یه‌سری از این تحلیل‌ها اشتباه از آب دراومده!
هرکی نظر متفاوتی داشت رو «خائن» و «وا داده» خطاب نکنید؛ وقتی می‌گفتید ادامه جنگ این‌طور میشه، اسنپ‌بک هیچ اثر اقتصادی نداره، نفت میره روی ۱۵۰ دلار یا با شکست ترامپ در انتخابات کنگره همه‌چیز تغییر می‌کنه، باید امروز جواب همون تحلیل‌ها رو بدید.
اینکه بگیم «ترامپ انتخابات کنگره رو ببازه، دموکرات‌ها جلوشو می‌گیرن» هم خیلی ساده‌انگارانه‌ست.
بین انتخابات تا شروع کنگره جدید چند ماه فاصله هست و رئیس‌جمهور آمریکا هم قدرت زیادی داره و می‌تونه سیاست‌هاشو دنبال کنه.
خلاصه اینکه تحلیل غلط، تحلیل غلطه؛ فرقی هم نمی‌کنه از طرف چه کسی گفته شده باشه. به‌جای توجیه و فحش دادن به بقیه، بهتره بعضی‌ها یک‌بار هم بابت پیش‌بینی‌های اشتباهشون پاسخگو باشن.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/72811" target="_blank">📅 09:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72810">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72810" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72810" target="_blank">📅 01:57 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72809">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rt_bCDILDXj3Wz7heNESDaWPlHrJxoHXtFJLtDLjRl2eGs-z0ZWOXKCF7Aa_0tGxJopmTaJxs9NlQzpaWCPY475DyeeMxTouSbsELxOZ3Cz5TqMBMpYulsuq1ESHqYVORmsgDoAOzP_mWcfLn0evpyMtNvA4d0LrY47JvuYdVV5BOQXTacvGWAD9EoJrt1_jtrIf7x22kE63UQhciKm7fqVC8xIwuACsWWS5Jt1enCejwmsHOqVxh9kPPzgXqCKFfPZjuuhSnZewhh9mZJxFLLP8iRi8ySmWL9k5ZWadLLIl_2pKwZQMCBH7n7yU22PaE4kMAsUsggk_Pcp_J6rD8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
🦖
قوانین رو در سایت مطالعه کنید
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
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72809" target="_blank">📅 01:57 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72808">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9d28d251d.mp4?token=GurlpGQ2NSvIHh40Wo28NySr-qAcVavKgE7LdJw9MjcdhPWdDqV8Bcf1DB4mCzH_stiO3v1kmhTF1Eo46cW1CTuAsmUKGaPk-BRjq1j2kmz-cUfRL1Wo8_L9VC7aEif7FDju4PSKf1tJ4Spj_Hw54o2nAqp4bVuUPVn8HvL1rqrKNomva6ITDosWWURv4GFy5zbjyiyfA4UvpT9AHq3jml3O84us492Fx756KuyVbi5GQ4HerC8MlGBnTQo95PMsXhdCPAspXiJjdMnt3tMrAjGwsjNW8ZLKMdG_KX3bTcRK8fdEUKbP113EmvzSg1tyY_LTlfj85dqANf2RnajJ_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9d28d251d.mp4?token=GurlpGQ2NSvIHh40Wo28NySr-qAcVavKgE7LdJw9MjcdhPWdDqV8Bcf1DB4mCzH_stiO3v1kmhTF1Eo46cW1CTuAsmUKGaPk-BRjq1j2kmz-cUfRL1Wo8_L9VC7aEif7FDju4PSKf1tJ4Spj_Hw54o2nAqp4bVuUPVn8HvL1rqrKNomva6ITDosWWURv4GFy5zbjyiyfA4UvpT9AHq3jml3O84us492Fx756KuyVbi5GQ4HerC8MlGBnTQo95PMsXhdCPAspXiJjdMnt3tMrAjGwsjNW8ZLKMdG_KX3bTcRK8fdEUKbP113EmvzSg1tyY_LTlfj85dqANf2RnajJ_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اولین ویدئوها از شهر طاعون زده شلخوف در روسیه:
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72808" target="_blank">📅 01:29 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72807">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a90e5ff82.mp4?token=Zgi7t3N3X6F7GgJ0ZSiPDhDINskPkFzcfPoAzF73V7aKbw_K2BSjbXneky5ubDDLKlcbSOdwjbLk5BB1sZXBqjIzbMNbO57lMsDfODO9lWbXoJGQnzovS7h5WIumkM2F-RUienGQr-bSs_74UqESpz-290E7jgmLSA7Jj7gAimgKUTEczrWmpSinraEmB_dOIDg1T-QuZcwAMv7q901O9d_EsDFRKGlNuQLoJhE1k-2FHKotbA1P0XxngfW_udytp_ZHrB7sluAgb5mLe7Z9XN_JlF7UO-0lH-S8gY5-IzxF2qCdKqBOa-scQ35qfEJj52MSPzJjT52YgLyOKsJEgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a90e5ff82.mp4?token=Zgi7t3N3X6F7GgJ0ZSiPDhDINskPkFzcfPoAzF73V7aKbw_K2BSjbXneky5ubDDLKlcbSOdwjbLk5BB1sZXBqjIzbMNbO57lMsDfODO9lWbXoJGQnzovS7h5WIumkM2F-RUienGQr-bSs_74UqESpz-290E7jgmLSA7Jj7gAimgKUTEczrWmpSinraEmB_dOIDg1T-QuZcwAMv7q901O9d_EsDFRKGlNuQLoJhE1k-2FHKotbA1P0XxngfW_udytp_ZHrB7sluAgb5mLe7Z9XN_JlF7UO-0lH-S8gY5-IzxF2qCdKqBOa-scQ35qfEJj52MSPzJjT52YgLyOKsJEgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو پشم ریزونی که ارتش یمن منتشر کرده که دارن با ماشین، حوثی‌هایی رو که در کنار ساحل گرفتار شدن و در حال مقاومتن رو زیر میگیرن و له میکنن:
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/72807" target="_blank">📅 01:18 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72806">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46e493def7.mp4?token=k3eKcf_Ek8yfprHLU6l0eG3vkxHp9vVzzq8A55RWr2lOmnak5lOa3d5vmLpUb3tjp7KlXYTqLvAqb4ZEjNu1xEvvLo9ejE4Dd23UEpKodyotPOfDTFZRueCtxt-VImPttvapE00d5f0ZPsPip_Def55xYEMnmUSpsGvyMX3_T8mAuniq6w7MQbQjLb7JuP3EC6G-Y-PFbgMoOwKOw3O-MxH10_541YZm4yQAZ8en43tpmt7cob2QxtbnTiR5QDRsDUjMJYsTXNCwRbtUGc68nUBjsnlbGuG3FJ7GKVOvS2n-pA0OGz6Sr2BjlLVA5WTnNXT6QdKiEadnYFZdGZKb3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46e493def7.mp4?token=k3eKcf_Ek8yfprHLU6l0eG3vkxHp9vVzzq8A55RWr2lOmnak5lOa3d5vmLpUb3tjp7KlXYTqLvAqb4ZEjNu1xEvvLo9ejE4Dd23UEpKodyotPOfDTFZRueCtxt-VImPttvapE00d5f0ZPsPip_Def55xYEMnmUSpsGvyMX3_T8mAuniq6w7MQbQjLb7JuP3EC6G-Y-PFbgMoOwKOw3O-MxH10_541YZm4yQAZ8en43tpmt7cob2QxtbnTiR5QDRsDUjMJYsTXNCwRbtUGc68nUBjsnlbGuG3FJ7GKVOvS2n-pA0OGz6Sr2BjlLVA5WTnNXT6QdKiEadnYFZdGZKb3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در جریان سخنرانی حسین رحیمی، رییس پلیس امنیت اقتصادی، درباره افزایش قیمت دلار، برق محل برگزاری سخنرانی قطع شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72806" target="_blank">📅 01:10 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72805">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tqbnIFevzSy9Sh-K0KHMiPQ-jEwrYKrahU4f9NFZm9R7gvyoQ7zVx0rnWxsw7LT6Y5_ySlENDVFrPYwDkC-UMgyNQodOTwpesPz6TGvahuTI7PvEtEd9L2BEOmd2W7OjHZpkK6etDucD-EsXmL7u8dbAXtsenWjUhWHBnVVD9VQgyjtJdomhk1o2jGgVoXRiQEXqOnMeeg7nymdu4lLupvsWKxHhvi78QvU2BblKEnYSs17edHurGn0eC1LhuzXMK54cLp1LpSF2zQgdeVyN1_sUGDEEQBMpQ1dMYzmY9sC7Vpwa-rriLU5Rl3sbl-5j0zIwlX_770Uv7CMeN0_gEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت درباره ایران:
«عملیات طرد اقتصادی» نتیجه داده؛ ارزش ریال به پایین‌ترین سطح تاریخی رسیده، ایران ماه گذشته هیچ نفت خامی برای بارگیری روی نفتکش‌ها نداشته و حتی یکی از مقام‌های ارشد امنیتی ایران هم گفته کشور در یکی از سخت‌ترین دوره‌های تاریخش قرار گرفته.
حکومت ایران در حالی مردم خودش را تحت فشار و رنج قرار می‌دهد که منابعش را صرف حمایت از تروریسم می‌کند و عملیات طرد اقتصادی تا زمانی که جمهوری اسلامی از تأمین مالی تروریسم و ساخت سلاح هسته‌ای دست نکشد، متوقف نخواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/72805" target="_blank">📅 00:29 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72804">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75b15ea218.mp4?token=Gt3_Xv9j1OBCdNFuHmhk_fLC5h1Q8-fbyeHiURn1imUQHh9iGAa7mCLMKbwNvEnawsA1dPYUCT-rlcVJ0tWSkdY6NOnzyTys8BsblbvgaG-Jrcnp-E5xPSE1UUxmnwqU2y27352ZTMSkHXG65v8m6QQVtaGLB68xQ1hLrsgQjpSrBCZ6reeaz-DNPLFk-hMfbXmBFWa6fVv6xWTKT93YlWSRMy9heTVgjXqZ561dm9AbGK15_ixL18eiiM0PrOHTmEVjT7s_8faBEGqFzeUsekJzMyL3CNCVSVE6-rFD-7r8L9yzdeMkG0ucTZTsnGoDH-D2mwFNvjGT2pm0hR0skg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75b15ea218.mp4?token=Gt3_Xv9j1OBCdNFuHmhk_fLC5h1Q8-fbyeHiURn1imUQHh9iGAa7mCLMKbwNvEnawsA1dPYUCT-rlcVJ0tWSkdY6NOnzyTys8BsblbvgaG-Jrcnp-E5xPSE1UUxmnwqU2y27352ZTMSkHXG65v8m6QQVtaGLB68xQ1hLrsgQjpSrBCZ6reeaz-DNPLFk-hMfbXmBFWa6fVv6xWTKT93YlWSRMy9heTVgjXqZ561dm9AbGK15_ixL18eiiM0PrOHTmEVjT7s_8faBEGqFzeUsekJzMyL3CNCVSVE6-rFD-7r8L9yzdeMkG0ucTZTsnGoDH-D2mwFNvjGT2pm0hR0skg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛ترامپ:من فکر میکنم ایران مسئول حمله به هواپیمای «فلای دبی»است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/72804" target="_blank">📅 23:39 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72803">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ترامپ:
ما مقادیر بی‌سابقه‌ای نفت از تنگه هرمز خارج می‌کنیم. یکی از مشکلاتی که داریم این است که پالایشگاه‌های روسیه به‌شدت هدف حمله قرار می‌گیرند.
این یک مشکل است، اما اوضاع به‌خوبی پیش می‌رود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/72803" target="_blank">📅 23:38 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72802">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">سؤال: آیا نگران شیوع طاعون در روسیه هستید؟
ترامپ: این بیماری‌ای است که قبلاً قادر به مهار آن بودیم؛ اما به نحوی، آن میکروب‌ها قوی‌تر و هوشمندتر شده‌اند. آن‌ها مثل یک ارتش هستند. ما به روسیه کمک خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72802" target="_blank">📅 23:37 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72801">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72c9bba814.mp4?token=kWRNXjk5Ph2wJvOgtrI9X43AJtRu0HobAH-OekdL4hrs8av13rsoTTyRBw2I9G_bSWJjIIwj0oDFUlNUKRBPBqYNz2iCxvjA8TWR0gRoyOUyyp59u4BHH1ZzY9LtpdUZ8NVgzGmfVyxIZZBpbFslE86xuHFbJNqG5vnPkF1U025BSArloaiUSeui-0ZCynMXx_Q-1p_3BGi62cKFMejcVMHk_IVYy2qdEBe92AAJGTM7LmVogyV-KxMsDKZ6GS6maY0NMSTjZiz8qQLBJnRxKEKGqtYArnS9xAbTuwET1CiY49D7aTsvRJd8N3w-eCvLkvuFioJ5qiH-TLJvDEj6fV_0ZgH8yEPZsvoxaS5U-qNEgQoZLgU8MsQdf96syiFoUi_St1MPbcq-xGHc-ZH9nn69iHs2ysP3KJQhGwPueeFtQcb5wa49Iy9zDcFBz9_T4of4fldIE6RGsU6l365uMLB-ins7SjWeP1jNTQtB7bnHjEmmPJlc3Vt_AIlvDC3tNacM8t57Wg489TvUmgJrb0JorZj6Ddg1GofExddaPGYfNDP2YBK3u0vfT8cu-DPuqgEXlwGSrlggt7AjOUbT9TeJjnqe88SDxIUYv-wSYWLOiR4bTD_3DA3m92rVQKsJ7_ApumGeG--ULqibY0JakJ7oKnVHFqyW9JaepvrY5Ck" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72c9bba814.mp4?token=kWRNXjk5Ph2wJvOgtrI9X43AJtRu0HobAH-OekdL4hrs8av13rsoTTyRBw2I9G_bSWJjIIwj0oDFUlNUKRBPBqYNz2iCxvjA8TWR0gRoyOUyyp59u4BHH1ZzY9LtpdUZ8NVgzGmfVyxIZZBpbFslE86xuHFbJNqG5vnPkF1U025BSArloaiUSeui-0ZCynMXx_Q-1p_3BGi62cKFMejcVMHk_IVYy2qdEBe92AAJGTM7LmVogyV-KxMsDKZ6GS6maY0NMSTjZiz8qQLBJnRxKEKGqtYArnS9xAbTuwET1CiY49D7aTsvRJd8N3w-eCvLkvuFioJ5qiH-TLJvDEj6fV_0ZgH8yEPZsvoxaS5U-qNEgQoZLgU8MsQdf96syiFoUi_St1MPbcq-xGHc-ZH9nn69iHs2ysP3KJQhGwPueeFtQcb5wa49Iy9zDcFBz9_T4of4fldIE6RGsU6l365uMLB-ins7SjWeP1jNTQtB7bnHjEmmPJlc3Vt_AIlvDC3tNacM8t57Wg489TvUmgJrb0JorZj6Ddg1GofExddaPGYfNDP2YBK3u0vfT8cu-DPuqgEXlwGSrlggt7AjOUbT9TeJjnqe88SDxIUYv-wSYWLOiR4bTD_3DA3m92rVQKsJ7_ApumGeG--ULqibY0JakJ7oKnVHFqyW9JaepvrY5Ck" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سؤال: آن چه تهدیدی بود که باعث شد آن هواپیماها را از بریتانیا خارج کنید؟
ترامپ: احتمال وجود تهدیدی را می‌دادیم؛ خب چرا باید آن‌ها را آنجا نگه می‌داشتم؟ با تهدیدی مواجه بودیم. ما کسانی را که آن تهدید را مطرح کردند، می‌شناسیم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/72801" target="_blank">📅 23:36 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72800">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8f6705b0f.mp4?token=QDY3bV47xfbyDk96kBQ-KlHXkd-ZVeiliGCEjZiAGhkZUc99_VtnSGmhNCCElYuz6p3UP8iC3pOJH7YiwfjJ78HJWbafzvJR7D1dHvPxb-_fMCDNU1MIsIoCBGOg8BmUbrJqpQlsN-eIPDIEUWP0jAy7rzlUvGlgaML2PIxXSLmbA7wGgYT2oF4UyqK1tq3tEMHNu5AekYS6KiBhZRGfvEHaxxr_8T4D55sL0CYaSLmY3cy8t7pYdkOKPtqg9xL0zPH6esppZtY5-A93OibP5rN7QjZD4f7tBpaIolgxfC9EWEv5Ul6AWKAEUhGv9Orx6Ywstp2wck8INSesJlAiXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8f6705b0f.mp4?token=QDY3bV47xfbyDk96kBQ-KlHXkd-ZVeiliGCEjZiAGhkZUc99_VtnSGmhNCCElYuz6p3UP8iC3pOJH7YiwfjJ78HJWbafzvJR7D1dHvPxb-_fMCDNU1MIsIoCBGOg8BmUbrJqpQlsN-eIPDIEUWP0jAy7rzlUvGlgaML2PIxXSLmbA7wGgYT2oF4UyqK1tq3tEMHNu5AekYS6KiBhZRGfvEHaxxr_8T4D55sL0CYaSLmY3cy8t7pYdkOKPtqg9xL0zPH6esppZtY5-A93OibP5rN7QjZD4f7tBpaIolgxfC9EWEv5Ul6AWKAEUhGv9Orx6Ywstp2wck8INSesJlAiXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سؤال: آیا فکر می‌کنید این خطر وجود دارد که ایران پهپادهای رزمی وارد بریتانیا کرده باشد؟
ترامپ: نمی‌توانم چنین چیزی به شما بگویم. اگر دست به چنین کاری زده باشند، بهای سنگینی خواهند پرداخت.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/72800" target="_blank">📅 23:34 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72799">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a5b0254b5.mp4?token=V7reubp2apfz3hVzeQ2bzY4gGEOuVDd4kFoM6on73krrUB2EdnM-l_zGmKqMKAbNg_4hLWA60VUPfwYJOsd60Pxrp24-Um4MfIS0e5dDrgsYgYEySvuTtk3PphpvjDc68s0-Y9rHa7JjA58i3Q0AYCKECiUHgG7KYPFWA0VjWqnYdtGICaV-_wmS2eQ0DxhzTaY-Rc0rEQcsVI8OrDgd-OLiVVnOPhjEQPzEu99JRxIJfYOyy4871NkKJ2_39FpymJPdbxf4cz4jHurBDeV3St_5WMDnq6Nw5ZLyrNwl47S4X3gDG-os5S2t7dX-Vll8Ekh_iaml3YyjB5fYltjZsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a5b0254b5.mp4?token=V7reubp2apfz3hVzeQ2bzY4gGEOuVDd4kFoM6on73krrUB2EdnM-l_zGmKqMKAbNg_4hLWA60VUPfwYJOsd60Pxrp24-Um4MfIS0e5dDrgsYgYEySvuTtk3PphpvjDc68s0-Y9rHa7JjA58i3Q0AYCKECiUHgG7KYPFWA0VjWqnYdtGICaV-_wmS2eQ0DxhzTaY-Rc0rEQcsVI8OrDgd-OLiVVnOPhjEQPzEu99JRxIJfYOyy4871NkKJ2_39FpymJPdbxf4cz4jHurBDeV3St_5WMDnq6Nw5ZLyrNwl47S4X3gDG-os5S2t7dX-Vll8Ekh_iaml3YyjB5fYltjZsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سوال:نظر شما درباره ضدحمله عربستان و یمن علیه حوثی‌ها چیست؟
ترامپ: همه چیز به خوبی پیش خواهد رفت.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/72799" target="_blank">📅 23:33 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72798">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d8db85c22.mp4?token=FxJKnMCAYUYKzBb60dOXiHfF19onFKUNMaXNu3PXnfb3Wsv3pBMtiCowhtHksyWC_bKN-xnjeV3u0mr6_gtmKW3dflvuAI6DshyG6RjLQOSf6KRLHfIZja1z3RSb9JVvWVYPcEhbIjD_k_J9GKf-aIhjuoqzL4nDr8etaPejoO8Uo8Tw5CL3eLPwk8WcJJwNOfzi-3fYVyDgmlu4WqgLZN_m-Q7MND7mK6ObplM3TO7DbQhsOpojIfb-SRX0vjFTreSYHcL54ZtETq0eduoEcnJKlJCvzoAvyxZZntjQjmklEiHB-JCl826l6CcPSMgUVDx0NcCL5W5MNvAjwVvqmIjYFkPdI_3RZszw2UpCXxKz-Zzn37LwyPXzsr3BOcHUBfa2blt9pFGsS_hnVaKflblgfmqvnU9vhof3LR04sZA1J6rpyYX3joEWEGctq3-oOWFe-byguDVcB5r-NbUnRdL_Au_nabg0_H8UUw1JbDlni1fwPvoABbOPKI0G7V5v83Fl13Vb2lWIuI2j41I2_bze6T36JAwzRVqdhVrju7zIOWOO3x40Q9JFUb6-UYGAcjb0iTp1EUFPV6FMw_oP9CMLekuVJI9SCYn8plebAGY3grIbSJhRdGpAfEe0CJWtmeWAMw6EcVMv9iA7gwMtaOjPsnst4o08StfWQu9OpvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d8db85c22.mp4?token=FxJKnMCAYUYKzBb60dOXiHfF19onFKUNMaXNu3PXnfb3Wsv3pBMtiCowhtHksyWC_bKN-xnjeV3u0mr6_gtmKW3dflvuAI6DshyG6RjLQOSf6KRLHfIZja1z3RSb9JVvWVYPcEhbIjD_k_J9GKf-aIhjuoqzL4nDr8etaPejoO8Uo8Tw5CL3eLPwk8WcJJwNOfzi-3fYVyDgmlu4WqgLZN_m-Q7MND7mK6ObplM3TO7DbQhsOpojIfb-SRX0vjFTreSYHcL54ZtETq0eduoEcnJKlJCvzoAvyxZZntjQjmklEiHB-JCl826l6CcPSMgUVDx0NcCL5W5MNvAjwVvqmIjYFkPdI_3RZszw2UpCXxKz-Zzn37LwyPXzsr3BOcHUBfa2blt9pFGsS_hnVaKflblgfmqvnU9vhof3LR04sZA1J6rpyYX3joEWEGctq3-oOWFe-byguDVcB5r-NbUnRdL_Au_nabg0_H8UUw1JbDlni1fwPvoABbOPKI0G7V5v83Fl13Vb2lWIuI2j41I2_bze6T36JAwzRVqdhVrju7zIOWOO3x40Q9JFUb6-UYGAcjb0iTp1EUFPV6FMw_oP9CMLekuVJI9SCYn8plebAGY3grIbSJhRdGpAfEe0CJWtmeWAMw6EcVMv9iA7gwMtaOjPsnst4o08StfWQu9OpvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سوال: آیا تهدید خاصی وجود داشت که باعث شد آن بمب‌افکن‌ها را از بریتانیا فراخوانید؟
ترامپ: بله، فکر می‌کنم بتوان چنین گفت. پرواز آن‌ها تصادفی نبود؛ تهدیدهایی در کار بود.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/72798" target="_blank">📅 23:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72797">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/449cc78904.mp4?token=tJhBhq0UF9XZ0lNW_o94Ber5BjWleux7hMcASWKy4QZKWtGyxu3NOvxYhQNIdFarmayCstDLoiDHZrb9ERk6TlgJnZD89v5nKzTwXUkwC1MAHZR8PUxNg2-OinzudYSF_FKYA9q8whx9nEYq_7F-dC_QB2XWJ43J90D17YMhYtoEAxgrFXoVa7Vc-m1FfKedDBFJ2HPmVfzE9N3VtQaNRGEg2oNO2DCVQke6cTlwmkD1qCVlpsfddfF9O_tkKUsz6XMmhU_0s5ZeLJgPMdzZmFXV1XXKxCC-V-3vtjgxFXVNvfcr26uB1BsKXeDlVVYNZ-CyYwzPtGAn_ObNwdkfgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/449cc78904.mp4?token=tJhBhq0UF9XZ0lNW_o94Ber5BjWleux7hMcASWKy4QZKWtGyxu3NOvxYhQNIdFarmayCstDLoiDHZrb9ERk6TlgJnZD89v5nKzTwXUkwC1MAHZR8PUxNg2-OinzudYSF_FKYA9q8whx9nEYq_7F-dC_QB2XWJ43J90D17YMhYtoEAxgrFXoVa7Vc-m1FfKedDBFJ2HPmVfzE9N3VtQaNRGEg2oNO2DCVQke6cTlwmkD1qCVlpsfddfF9O_tkKUsz6XMmhU_0s5ZeLJgPMdzZmFXV1XXKxCC-V-3vtjgxFXVNvfcr26uB1BsKXeDlVVYNZ-CyYwzPtGAn_ObNwdkfgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیروز در میدان آزادی (میان اقبال) سنندج از این کوماندو‌ها رونمایی کردن برای مردم! امیدوارم این فیلم رو هیچ وقت ترامپ نبینه چون بعدش قراره دیگه شبا آرامش نداشته باشه
😂
یه ساختمون چند طبقه رو ۱ دقیقه طول کشید تا برسن پایینش! از پله‌ها میومدن زودتر می‌رسیدن
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72797" target="_blank">📅 23:02 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72796">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a1edaa900.mp4?token=td3XqTUl0Gp8cdz8nfJzRLhJGD87VHqCwSN-lo3ayBpv6z5EXxjux_9qFw3emfyZ-diWgyGhxV0U1OT2U_mi2nFmAf0uy6KF9ws9XddswMblJk7ju76dqaNZ1EHyyo4SMXSTGPXisuSfRfGYmXop8B_TZQqgC2E7fhfDGrQ1WlJrxbFQjr-OV7Y32U5NcLdoY_yGBanTDymftEmVDGALVoaBaGrSOEVpHNxhbdOy5JteNZ-uJON38p_vhTR-4wa2Qwqq60ZI9A26lDYf24VzFNECc-zOe4BLdvOfySFsP5nsxMwOP-S2x0lhL_axPmTSxXYMzdeHX2JnHgDsMh6lUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a1edaa900.mp4?token=td3XqTUl0Gp8cdz8nfJzRLhJGD87VHqCwSN-lo3ayBpv6z5EXxjux_9qFw3emfyZ-diWgyGhxV0U1OT2U_mi2nFmAf0uy6KF9ws9XddswMblJk7ju76dqaNZ1EHyyo4SMXSTGPXisuSfRfGYmXop8B_TZQqgC2E7fhfDGrQ1WlJrxbFQjr-OV7Y32U5NcLdoY_yGBanTDymftEmVDGALVoaBaGrSOEVpHNxhbdOy5JteNZ-uJON38p_vhTR-4wa2Qwqq60ZI9A26lDYf24VzFNECc-zOe4BLdvOfySFsP5nsxMwOP-S2x0lhL_axPmTSxXYMzdeHX2JnHgDsMh6lUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شامگاه شنبه ۱۱مهر۱۴۰۵؛لحظه برخورد صاعقه با برج میلاد:
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/72796" target="_blank">📅 22:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72795">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60d10955ac.mp4?token=uflKWoWuFzUfs1S89HqXML_MA5_WD_Q8fuRgVPwg1bcssifBWci0FZ-Vue5RaEVpaqoqYmFGVmSRF6ewahZ6D90OukQAs9JbWbFfXe0-sz-gYyqMfRdLm78yD8tISsd2Iikc-XaMyrFuOm7r7UMTImLyLHW4ABFyGnpHaqoAipdvw-dVR4AOXPkktFSwDZ4_PcxyLQlfsbyP7Lx9UBGN8hLmi-Ibgvzdo5sRRR_xbPXOZ_JmtfkGjpl3QnYB09YX0ErKdFTXV4G9deMDtjSWDW4Ha-t9LBg-pPxGBKeD7BST6_eW8Dnun0V7BLGnYJzTc8QbLdv6Kl3Jj6laMwibHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60d10955ac.mp4?token=uflKWoWuFzUfs1S89HqXML_MA5_WD_Q8fuRgVPwg1bcssifBWci0FZ-Vue5RaEVpaqoqYmFGVmSRF6ewahZ6D90OukQAs9JbWbFfXe0-sz-gYyqMfRdLm78yD8tISsd2Iikc-XaMyrFuOm7r7UMTImLyLHW4ABFyGnpHaqoAipdvw-dVR4AOXPkktFSwDZ4_PcxyLQlfsbyP7Lx9UBGN8hLmi-Ibgvzdo5sRRR_xbPXOZ_JmtfkGjpl3QnYB09YX0ErKdFTXV4G9deMDtjSWDW4Ha-t9LBg-pPxGBKeD7BST6_eW8Dnun0V7BLGnYJzTc8QbLdv6Kl3Jj6laMwibHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی: اخراج ما از آمریکا مثل اخراج تیم برنده از المپیکه!
پس خبر درست بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/72795" target="_blank">📅 21:35 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72794">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d035f07a6e.mp4?token=euHh1-VX6S0_QV2-kHbiwOh1tDeNr3qYuGuvvnXnGyT4_Ge0U3DoKZurm3v9qu0NXyAY3Rt8d7_LynYCy0kb0vXYHP9sNaHyN70dkgrR2eZwiRZIqZbvO8on-fFPgeHy27MHHrywpX-JQabjoSX-bUkZobABBHJtNX0C01iYcf_hPK7G6tNdm-LYNmdqc580dqlnOq0TsPeip8RIldvfEHHgZ4cLsg8po3pZLdGxxG-6iDNDLSTTrNnlyzfhAEev1FMtXvYO2GHCxuaXckkyoQmdo-lSqxRO0yTLpO_fNd8Nbf3RuikZXVAUktflvbLujOVuAnjIg2Id5PS-ab1Z2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d035f07a6e.mp4?token=euHh1-VX6S0_QV2-kHbiwOh1tDeNr3qYuGuvvnXnGyT4_Ge0U3DoKZurm3v9qu0NXyAY3Rt8d7_LynYCy0kb0vXYHP9sNaHyN70dkgrR2eZwiRZIqZbvO8on-fFPgeHy27MHHrywpX-JQabjoSX-bUkZobABBHJtNX0C01iYcf_hPK7G6tNdm-LYNmdqc580dqlnOq0TsPeip8RIldvfEHHgZ4cLsg8po3pZLdGxxG-6iDNDLSTTrNnlyzfhAEev1FMtXvYO2GHCxuaXckkyoQmdo-lSqxRO0yTLpO_fNd8Nbf3RuikZXVAUktflvbLujOVuAnjIg2Id5PS-ab1Z2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه آقای آتش‌نشان در مورد ساخت پلاک مشخصات برای دانش آموزان:
امروز رفتم یه دبیرستان دخترانه برای کنترل مسائل امنیتی بین حرفامون با مسئولین مدرسه متوجه شدم که دارن برای دانش آموزان پلاک مشخصات فردی درست میکنن مثل همونایی که زمان جنگ استفاده میشد؛
از این پلاک‌ها که زمان جنگ سربازها مینداختن دور گردنشون که اگه بر اثر بمب و موشک چهره‌شون دیگه قابل شناسایی نبود، از رو پلاک شخص رو تشخیص بدن..
وقتی پرسیدم برای چیه؟ گفتن نمیدونیم فقط از بالا دستور گرفتیم و مشخصات فردی دانش آموز رو دادیم تا براشون درست کنن!!
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/72794" target="_blank">📅 20:40 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72793">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DgPqpxvomLacOILrFGJ6anL-gmQ5i1nYLRyGXIDJPaEheXZBJrCoj1blYtiBe02gj6jBTkHrUy4rQYAfn17I0PLd6lCw_-DfuB7-1PPLLBlOm4GFshI33jjnUxAYplAt-TGx2dNtn2p9Ym3QPkyaUACml5ksZ6iM59htL-O-B3XEL5ec_IBMyc3gdXaKJo8_fhP2zkUtqubRdN6ZGcrPsnZ2_2WNxUxVS7LkCByBB151bdkyqfch5PTqHjJsURCY4z-8kM9jYFRgnYVeDGKCXafDCKnTxX3C6PsT59ypnAVPtrrDLh0CDqPbN7s6VzIwQk_rgSac9aq3bvYoQmXB8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
آنچه باعث افزایش قیمت بنزین می‌شود دیگر تنگه هرمز نیست — چرا که اکنون حجم بی‌سابقه‌ای از نفت (بشکه) تقریباً به‌صورت روزانه(از تنگه هرمز)عرضه می‌شود
.
بلکه مسئله «پالایشگاه‌ها»ست؛ جایی که پالایشگاه‌های روسیه توسط اوکراین منفجر می‌شوند و پالایشگاه‌های ما در ایالت‌های آبی (دموکرات‌نشین) مانند کالیفرنیا، توسط «دموکرات‌های احمق» تعطیل می‌شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/72793" target="_blank">📅 20:17 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72792">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/902f67b684.mp4?token=TvWG7ERS82v_gncBb9zV6S3uveolgltOJb6F1f8ekWvqYIP28w_DWFll8m8YPJKL-NX-77X1shaGTUUAbqDcYjIMV0f5KONPhM-4578bDkZZaf9I9wlECyUhugW5frJ91RyZS2EmSTlQaA8FEuUfxdC3x3O1p7pXnHzIqxPv7jIcRiA5c8UezjbzgVlCwVsvouaB8na8suNwS2B5zN8yqyf86bQd7aBKMIkw3XQ_lpaeKT74C9GMvryW1nrfEZPoL9ieXv-1DMPffas7tKRy4Ul71ByZczR4POatZlLFPq2Pv_RtALBTXYjg52CpqGJkcbUaj0LYyAr53jEr4fU31Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/902f67b684.mp4?token=TvWG7ERS82v_gncBb9zV6S3uveolgltOJb6F1f8ekWvqYIP28w_DWFll8m8YPJKL-NX-77X1shaGTUUAbqDcYjIMV0f5KONPhM-4578bDkZZaf9I9wlECyUhugW5frJ91RyZS2EmSTlQaA8FEuUfxdC3x3O1p7pXnHzIqxPv7jIcRiA5c8UezjbzgVlCwVsvouaB8na8suNwS2B5zN8yqyf86bQd7aBKMIkw3XQ_lpaeKT74C9GMvryW1nrfEZPoL9ieXv-1DMPffas7tKRy4Ul71ByZczR4POatZlLFPq2Pv_RtALBTXYjg52CpqGJkcbUaj0LYyAr53jEr4fU31Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیت هگست وزیر جنگ آمریکا توانایی خودشو توی بسکتبال هم نشون داد و تقریبا همه توپاشو سه امتیازی وارد سبد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/72792" target="_blank">📅 20:14 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72791">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0b5a00bb1.mp4?token=DLdWEpJzFCvGf29TfrvSOQCYia688RXPdhGL90rRz8hyfz5v3wC1VPK2KDVedjP35GkixJ3LA-9L9kHQy4sKaFxyZ3XBEwpCSBkRmPaovkpV72lPtd6rUOqw3EB9NDaDvDMsEpVFWZ7ip1t75ELo7YTsxVgVroqcUAbJL-arzO1nOi_chOTmyTag0vUUVagF64KGT62fPL7MT_R4huxmT8oGmxeGgvsznu_1zSlG4yfodjtO9YHeyySLasjQw18v_AVVV6DJzcY9Nx-6CjuwBZH0gCgiHaAEvzK5SBuZAOKQIMZfsLX7a2oj5iPADf5q4a3Fuw9EVChbU5ZZ6dpo74HNHpYV1ZgbRx1xQ75OdBUnuZGXnOee-o08vgFStDDixjVW1WVWb5SavJAShviLCRE_EbqZseOOIvu6v6dFc4OqYYQENlC2CsOqDbA25iWBW6JaVupujB6tX6gAU69Tz7fBe9i4anahjBkieluKmhZlhAJQHEWqjVV0Zxt_W8N9rT5YBNw-FeAuBhYSsZRR3YtOpl7NHFrjwVSxipTQ1rIyW06dGBfbVEbbjtm4SG_PGvb42eIKTSzqFvkfFIVsLjLSm2ChjZkjfFpBOjpPoM0tvkxyLMkxX_vIIpCdpQge06x4Zjtprng_vtZssGC9hXncoHaVAGSvoy2Gcaiw_us" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0b5a00bb1.mp4?token=DLdWEpJzFCvGf29TfrvSOQCYia688RXPdhGL90rRz8hyfz5v3wC1VPK2KDVedjP35GkixJ3LA-9L9kHQy4sKaFxyZ3XBEwpCSBkRmPaovkpV72lPtd6rUOqw3EB9NDaDvDMsEpVFWZ7ip1t75ELo7YTsxVgVroqcUAbJL-arzO1nOi_chOTmyTag0vUUVagF64KGT62fPL7MT_R4huxmT8oGmxeGgvsznu_1zSlG4yfodjtO9YHeyySLasjQw18v_AVVV6DJzcY9Nx-6CjuwBZH0gCgiHaAEvzK5SBuZAOKQIMZfsLX7a2oj5iPADf5q4a3Fuw9EVChbU5ZZ6dpo74HNHpYV1ZgbRx1xQ75OdBUnuZGXnOee-o08vgFStDDixjVW1WVWb5SavJAShviLCRE_EbqZseOOIvu6v6dFc4OqYYQENlC2CsOqDbA25iWBW6JaVupujB6tX6gAU69Tz7fBe9i4anahjBkieluKmhZlhAJQHEWqjVV0Zxt_W8N9rT5YBNw-FeAuBhYSsZRR3YtOpl7NHFrjwVSxipTQ1rIyW06dGBfbVEbbjtm4SG_PGvb42eIKTSzqFvkfFIVsLjLSm2ChjZkjfFpBOjpPoM0tvkxyLMkxX_vIIpCdpQge06x4Zjtprng_vtZssGC9hXncoHaVAGSvoy2Gcaiw_us" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس، معاون رئیس‌جمهور، درباره خروج هر ۱۲ فروند بمب‌افکن «بی-۱» (B-1) از پایگاه نیروی هوایی سلطنتی «فیرفورد» (RAF Fairford):
آنچه در آنجا شاهد بودید، اقدام وزیر دفاع برای محافظت از نیروهای ما بر مبنای احتیاطی مضاعف بود.
ما با اطمینان نسبی معتقدیم که ایرانی‌ها در پی انجام همان کاری هستند که حکومت ایران طی ۴۹ سال گذشته انجام داده است؛ یعنی ارتکاب اقدامات تروریستی علیه ایالات متحده و همچنین علیه بسیاری از افراد دیگر.
ما نهایت احتیاط را به خرج می‌دهیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/72791" target="_blank">📅 19:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72790">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ENAxc7HF3phGNNmmrgLewDTp543vTQwwVeUGZNSxbjxjvUO75Z1vGfDi81qQjEd1GHKMApTQD7-4CXuH2NmUDZWebSSWZ37qmoBPTowNfkSk65FgGzcaiVbVZm7BC6hLO7efLiD0iHzKq6uZRVis2SReOqY62rTw-klo8nCSKY00eESAwNQWGoBDjGf-fez5qoGdTUuy72Mjo6-0hnL0I0Ls4xVolkFFeLE27t5_xQqN0Ls5f2V-fJISNBD5AedS34Ii2FTNPRtPS64nVvpmQXq6VOYw9xnq0FLNDHNthLqwLikFNRBE8Q7MPwt4FHM4DuHVZ2K6ecvmep_rBYQfLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز:
ناو هواپیمابر آمریکایی «جورج اچ. دابلیو. بوش» به همراه حدود ۴۸۰۰ نفر از کارکنان خود، پس از شش ماه پشتیبانی از عملیات‌های ایالات متحده در خاورمیانه، برای یک دوره استراحت وارد پوکتِ تایلند شد.
پوکت نخستین بندری است که این ناو از زمان ترک ایالات متحده در ماه مارس در آن پهلو می‌گیرد؛ قرار است کارکنان آن از ۴ تا ۹ اکتبر برای گشت‌وگذار، فعالیت‌های فرهنگی و برگزاری یک مسابقه فوتبال میان آمریکا و تایلند، در خشکی حضور یابند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/72790" target="_blank">📅 19:07 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72789">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d3aadbf79.mp4?token=QEtW16264LabUOeVwoR9t83X-yTHsXlgCCMYxJR4gW409G1QnXvHC3X_8PFJS9p_A3jJL6aeXCH4orDEozBEDveTpL1OLfpgv9IziaawU00RZoRQfayA8A8BWbRSPHYUrGE1Hj3F1zml7su9NeHWzaotzhQQ-NU9oNPpUf1Ch13WbYI8R2kxDr7WWAC8N5csj6DfWhRxLzTVh9INcT4MhywO7-mc7Uy3diisiV5uEKekjSpV2Z3ozjI0TVTYChg424syk-9bIqh0nvvIu77MCC3a4uhy90mdyvKWs3sKBK3HjCS2gX92AAKwETSJv5R5RFjC5nduSxk63Ltzr_ZEeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d3aadbf79.mp4?token=QEtW16264LabUOeVwoR9t83X-yTHsXlgCCMYxJR4gW409G1QnXvHC3X_8PFJS9p_A3jJL6aeXCH4orDEozBEDveTpL1OLfpgv9IziaawU00RZoRQfayA8A8BWbRSPHYUrGE1Hj3F1zml7su9NeHWzaotzhQQ-NU9oNPpUf1Ch13WbYI8R2kxDr7WWAC8N5csj6DfWhRxLzTVh9INcT4MhywO7-mc7Uy3diisiV5uEKekjSpV2Z3ozjI0TVTYChg424syk-9bIqh0nvvIu77MCC3a4uhy90mdyvKWs3sKBK3HjCS2gX92AAKwETSJv5R5RFjC5nduSxk63Ltzr_ZEeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حوثی‌ها به معنای واقعی کلمه به سعودیا دارن تجاوز می‌کنند، یعنی شما کاکولدزاده تر از ترکیه‌ای‌ها، پاکستانی‌ها و عربا نمی‌بینید، بعد حالا فکر کنید این سه تا پیمان دفاعی هم دارن =)  تازه از خواب بیدار شدن گفتن عه بهمون حمله کردن بزار یه گوهی بخوریم وگرنه شرفمون…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/72789" target="_blank">📅 18:58 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72788">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">حوثی‌ها به معنای واقعی کلمه به سعودیا دارن تجاوز می‌کنند، یعنی شما کاکولدزاده تر از ترکیه‌ای‌ها، پاکستانی‌ها و عربا نمی‌بینید، بعد حالا فکر کنید این سه تا پیمان دفاعی هم دارن =)
تازه از خواب بیدار شدن گفتن عه بهمون حمله کردن بزار یه گوهی بخوریم وگرنه شرفمون از دست می‌ره (کنترل شهر مهم تعز همچنان به دست حوثی‌هاست)
#hjAly‌</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/72788" target="_blank">📅 18:52 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72787">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">حوثی ها دو موشک را به سمت منطقه ای که تحت کنترل نیروهای دولتی یمن بود شلیک کردند.
در همین حال خبرنگار شبکه العربیه در حال آماده‌سازی برای پخش زنده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/72787" target="_blank">📅 18:28 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72786">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VbIOvzPLxr0MSvi4JsE6gmPos729PfOANLST2e-Dj-K9nnqThUNoDYEsQcsx-Y9ATmUEpK5riHR1rqdbW0PVD4xa9oh8CuVDS6dTnoYnkHO7AodJcwtYXDsEpdM-m6RvBKjlw19nhQwpkzALLeanDJPcTzHi0J53nxu2ZsFPcXx5hnMvLKs8exGl6tCfnJ3TPei1lh_LfsbUnxky2gXomyNaBMPzZkAtW5W6quXkxVAbhB0pZSxF_ekYY_VQuFcX7JF51hGaA17PrCpWpN7IY_KVgJRSIVRTD8yL-KvN1g2HWoJ62e4RIERB1fLpSp5oZ4aStJ-xjBz-MfccI2oWag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#مهم
؛
مشاوران ارشد امنیت ملی ترامپ نشستی محرمانه و چندساعته را در «کمپ دیوید» برگزار کردند تا درباره احتمال جنگ با ایران و درگیری میان عربستان سعودی و حوثی‌ها در یمن گفتگو کنند.
ریاست این نشست بر عهده معاون رئیس‌جمهور، ونس، بود و مارکو روبیو، پیت هگسث، استیو ویتکاف، جان رتکلیف (رئیس سیا)، ژنرال دن کین و اسکات بسنت (وزیر خزانه‌داری) نیز در آن حضور داشتند.
یک مقام آمریکایی اظهار داشت که در این جلسه درباره مسائل عمده خاورمیانه «تصمیم‌گیری شد یا دست‌کم بحث‌های عمیقی صورت گرفت.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/72786" target="_blank">📅 18:12 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72785">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72785" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/72785" target="_blank">📅 18:12 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72784">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CaEbu5jmafnzUC_MZChUZySU8rbMfkU9yVKR3uen7WJwf3GKJsNqJDlGkw6xYPl98lzEJ_jeY1jhPDuP9Efcq-eSY5cuc5S4yCnOFSn8TFp8GSt9TarLA8wqeNkrKTQ9R6BawIZlvqP-IzSJdRVjenNYm1E01MTnWgTOLt9ljHCdE1B_0LUSQFtXGLzSAfvVGFteWNEzY_-DkTukxtfkY1m-YshEjLEUlAOW9vFb7gY-g92XN5CgaijrRlX8F4_LXklbhVRIFDprZO0syzRkt3qTFW8tVyS5vOWGGKZCnNULcra_fpF3g2XIhwqOhRVYmDLzZSE3jUw6VxaGD6xjoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز بلژیک
🆚
فرانسه را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
بلژیک: ۳ برد، ۲ شکست و ۱۰ گل زده
فرانسه: ۲ برد، ۱ تساوی، ۲ شکست و ۷ گل زده
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
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72784" target="_blank">📅 18:12 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72782">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e7b8e8d5c.mp4?token=RpzSrKvt0qovABS48ThM04baScYQERwU-ZEGEdJe3z936UTZ7b5P_yCss56IR9n3jz-70aZ6kmW8ncDioDa1ksw3BMN0EKfeoxcs06pvzXWtuVfzBCC5HzdkLyrMm2tFzufFg9Dy1vwCw8sJGhZVeDgxZTN2TmNh-3uRRSAHgXs7cWCqCv23nWgDKGMfsBDtm0kmWdv_CWd00tDKR8WJkNMpcWZr82MNSYecUgcaUdu4PbRIWZES9DHynjUvl4795JT5XGB3DzW_rQvpabK0JCL9iNErhSlSpUrgMqQ-OuO2L4F0LHmdfsSnJ7VXorw-2dbrKe4VS0X3f7LO_hd54Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e7b8e8d5c.mp4?token=RpzSrKvt0qovABS48ThM04baScYQERwU-ZEGEdJe3z936UTZ7b5P_yCss56IR9n3jz-70aZ6kmW8ncDioDa1ksw3BMN0EKfeoxcs06pvzXWtuVfzBCC5HzdkLyrMm2tFzufFg9Dy1vwCw8sJGhZVeDgxZTN2TmNh-3uRRSAHgXs7cWCqCv23nWgDKGMfsBDtm0kmWdv_CWd00tDKR8WJkNMpcWZr82MNSYecUgcaUdu4PbRIWZES9DHynjUvl4795JT5XGB3DzW_rQvpabK0JCL9iNErhSlSpUrgMqQ-OuO2L4F0LHmdfsSnJ7VXorw-2dbrKe4VS0X3f7LO_hd54Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت های جنجالی کوچک‌زاده مجلس :
کدام کارمند و مردم عادی پول دارد ۲/۵ میلیارد تومان بدهد ده هزار دلار بخرد، این پول زیر متکای امثال همتی و دزد‌ها و اطرافیانش میرود.
آقای قالیباف، چرا مملکت اینطوری شده که راننده رفسنجانی هر کاری می‌خواهد در این کشور می‌کند؟
طرح جدید بانک مرکزی؛
هر ایرانیِ بالای 18 سال می‌تونه تا 10 هزاردلار (۲ میلیارد و ۷۰۰ میلیون تومن) از بانک بخره!
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72782" target="_blank">📅 17:33 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72781">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f1c650a97.mp4?token=VL_WkK8jjAGqWinQml6_1lvZC9mpug9YCH0-2Sm349Zj-6HZTHLroFTg3wrguGMzKL9cd_QZ5ubpKttOJDQiyB0-EP4UNerjcSaIOWKeFNxib1yK_oDjNoPayIvLP85V5wKw6uaxv7BkvsGSzW_OZMOMhnkQHLGbI4yB54KUcUpMh6SO9eD92Ig3bpXLdKWPoqEvwm-1dS8BKOFsFemEMx-X4jX3x6RZWz3z6JUIjNEm9wI5r29w3_5m3qEw2ZxG460WTLDm5b58Eay-a16ATyizeyRgnVbc74fSIO0Oe2v8ju3_6rddLuktWhl5kkM9WJt9f2fX9bTwZfAYu0iX10uMTpMIrrhdpn5yoqu-6FMtEkDtyJs2tBICVtHv8vkjIxLtVa6bT2EBAHcx6vDSxeRXAqCOguekpDMPUqwL2RCv2cT4jMIdqaGBJOxldu21t8oFi84ggL_kfdHxKluuRp9eOOfUPm1PTVdBf2r3wTj1daRRloTgVfs7k1Btkd_z3BpjZNleM_iJ0WW1Ub314dhlxxfydUc0kRBuoEA5TtYBmi2RB1JM_Bbr6fFVv5XpIcOuhBxkwuyU0q62hAjEwCZN1Wrpe9N81H6ydCx25y2B0uXygbhgTHNJNQP9y7eshLcO09ErvLF25jFo_FdFQV0oMDa_f-FitaPDAlbfU-4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f1c650a97.mp4?token=VL_WkK8jjAGqWinQml6_1lvZC9mpug9YCH0-2Sm349Zj-6HZTHLroFTg3wrguGMzKL9cd_QZ5ubpKttOJDQiyB0-EP4UNerjcSaIOWKeFNxib1yK_oDjNoPayIvLP85V5wKw6uaxv7BkvsGSzW_OZMOMhnkQHLGbI4yB54KUcUpMh6SO9eD92Ig3bpXLdKWPoqEvwm-1dS8BKOFsFemEMx-X4jX3x6RZWz3z6JUIjNEm9wI5r29w3_5m3qEw2ZxG460WTLDm5b58Eay-a16ATyizeyRgnVbc74fSIO0Oe2v8ju3_6rddLuktWhl5kkM9WJt9f2fX9bTwZfAYu0iX10uMTpMIrrhdpn5yoqu-6FMtEkDtyJs2tBICVtHv8vkjIxLtVa6bT2EBAHcx6vDSxeRXAqCOguekpDMPUqwL2RCv2cT4jMIdqaGBJOxldu21t8oFi84ggL_kfdHxKluuRp9eOOfUPm1PTVdBf2r3wTj1daRRloTgVfs7k1Btkd_z3BpjZNleM_iJ0WW1Ub314dhlxxfydUc0kRBuoEA5TtYBmi2RB1JM_Bbr6fFVv5XpIcOuhBxkwuyU0q62hAjEwCZN1Wrpe9N81H6ydCx25y2B0uXygbhgTHNJNQP9y7eshLcO09ErvLF25jFo_FdFQV0oMDa_f-FitaPDAlbfU-4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سؤال: چرا بمب‌افکن‌های آمریکایی پایگاه «آر.ای.اف. فیرفورد» (RAF Fairford) را ترک کردند؟
روبیو:
مشاهده چرخش نیروها و جابه‌جایی تجهیزات، امر غیرمعمولی نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/72781" target="_blank">📅 17:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72780">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cde1d0199.mp4?token=TofEknsJ72WjsuMRDH2reL-EHi3G7YnFiQveqz6XqQ8WhbHC7uOi9aj-s2Te_-RpE_3jYxrNsqAjqT0aHmiKLIcD-OhRnLubPR8JM4S5Mq55LMxL_Aw4LqfgJ_guO7WDf4SNR0uzd2ZUwrZ5eHasb6r-3BmysHCrHsg3DE3f7idbouz7cLgRzYt4nP9bxzCAdrITEyDis3IR_eI2UlZM75we1JEE9-_AwckwfQiY7qTbTuXX2JTsgenm_RFbBu4BQCx2mRr2fp4TPnY3Bry0pSDU0BABvPASDSmYGdnp9Mnmdb0kt3ryKH1CCzTk6QVztNUn78hMTRSQawep1M-mFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cde1d0199.mp4?token=TofEknsJ72WjsuMRDH2reL-EHi3G7YnFiQveqz6XqQ8WhbHC7uOi9aj-s2Te_-RpE_3jYxrNsqAjqT0aHmiKLIcD-OhRnLubPR8JM4S5Mq55LMxL_Aw4LqfgJ_guO7WDf4SNR0uzd2ZUwrZ5eHasb6r-3BmysHCrHsg3DE3f7idbouz7cLgRzYt4nP9bxzCAdrITEyDis3IR_eI2UlZM75we1JEE9-_AwckwfQiY7qTbTuXX2JTsgenm_RFbBu4BQCx2mRr2fp4TPnY3Bry0pSDU0BABvPASDSmYGdnp9Mnmdb0kt3ryKH1CCzTk6QVztNUn78hMTRSQawep1M-mFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آترینا فرحمند رتبه یک کنکور تجربی ۴۰۴، پارسال همین موقع:
دخترا خیلی خفن‌تر از پسران، من مطمئنم رتبه یک کنکور تجربی سال بعدم دختره.
نتیجه:
توی کنکور تجربی امسال از ۱۰ نفر برتر، ۹ تاشون پسرن و رتبه یک هم پسر شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/72780" target="_blank">📅 17:04 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72779">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35a05bc751.mp4?token=E3ohNZ5FlUypQpJGyjTo7DhUWLo6kyz7inF8wg748OelE1H3uNhqmW81k5t2cQ_6LBJi_GdtVGXUSeJl9-x9_LKQU8NWYBtjGuyk1lSaFOhffegap6UB-yv3Yk_jLp-H7IY_k8FQw2NZ_bZuN1zc_XWaCLVrhQR3qCQ5XFzFJZ_xjQ3kki2GunMV2FmUaRVev3XgfJMwpEAMdwCF3MO4MeqswySbXXfDI9OvwODjORTw2Kne7Muxug568rRQoG6fXNEfFBeRTTTfxqK21tayBl0svJ_jErGaIO5YqL8WUmxLQl3ZdUZwXDQxKj08cyYPT5TxOt-R0P4Q9Mmqy6ZKL3npWr9mUFS8RZ6pSLgF4tONjszHWrZ9nM7cdLfrM5myB2AttjSd1pjNbdMptaayGpfYsV3hWoQI7ULOcY6fb2lLYu-qPdB0N0vrtOGPqQrAAh1sl1_X-UoIDylr6983b8wQDZIJ4jt1lvfgmroZ7KF0aQtPW8INGgoyIg_rulWAMkZtlr_eFIiliIeh1LzRnf78kWcOBAh5CGHjvrqcvDiU74BNu3EYfFY8D8BRWZVZmzxixck84LpOe9n6iknVD6WPnsdxlT2zgI0vcZUSGmfRskeiF5NYfReGGBibdKSaNb15UeAbSOwDBPtN-ce8ovV1QTlA2F8FCdsMLUg2xoU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35a05bc751.mp4?token=E3ohNZ5FlUypQpJGyjTo7DhUWLo6kyz7inF8wg748OelE1H3uNhqmW81k5t2cQ_6LBJi_GdtVGXUSeJl9-x9_LKQU8NWYBtjGuyk1lSaFOhffegap6UB-yv3Yk_jLp-H7IY_k8FQw2NZ_bZuN1zc_XWaCLVrhQR3qCQ5XFzFJZ_xjQ3kki2GunMV2FmUaRVev3XgfJMwpEAMdwCF3MO4MeqswySbXXfDI9OvwODjORTw2Kne7Muxug568rRQoG6fXNEfFBeRTTTfxqK21tayBl0svJ_jErGaIO5YqL8WUmxLQl3ZdUZwXDQxKj08cyYPT5TxOt-R0P4Q9Mmqy6ZKL3npWr9mUFS8RZ6pSLgF4tONjszHWrZ9nM7cdLfrM5myB2AttjSd1pjNbdMptaayGpfYsV3hWoQI7ULOcY6fb2lLYu-qPdB0N0vrtOGPqQrAAh1sl1_X-UoIDylr6983b8wQDZIJ4jt1lvfgmroZ7KF0aQtPW8INGgoyIg_rulWAMkZtlr_eFIiliIeh1LzRnf78kWcOBAh5CGHjvrqcvDiU74BNu3EYfFY8D8BRWZVZmzxixck84LpOe9n6iknVD6WPnsdxlT2zgI0vcZUSGmfRskeiF5NYfReGGBibdKSaNb15UeAbSOwDBPtN-ce8ovV1QTlA2F8FCdsMLUg2xoU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آیا می‌توانید آخرین وضعیت مورد مشکوک به طاعون در روسیه را به ما بگویید؟
مارکو روبیو: ما به‌دقت وضعیت را زیر نظر داریم. فکر نمی‌کنم این مسئله جای نگرانی داشته باشد، اما نیازمند توجه و تمرکز است و ما نیز همین کار را انجام می‌دهیم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/72779" target="_blank">📅 16:43 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72778">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a15378585.mp4?token=sB7szce_iG6tOhq68nni0iKyiwWlS1zpuVXX2GaUe1JW4Ht7xxUT1byxiSm8GuhzgYjtGvSnmx5KEAw6Mek-yq3iJ9dcDWt_xCNbcDEYEHCb7eJqSZrqj8Z4In_cu-0fswCDF5dGi9NmskPnCxvBE8Z6Hvu00zfw449evMneS7SgWBL7zPcbgYgRcwxaLUYWjj5u9TLxFmBeFBzcsv7xMRJg_3m-U4n4ztaZ0_cLFgJCJ7a9butS-1Am5aymYdpeq4uaDHprYI2rWOXqcbgH_FjkdwhZhrVXylnZrysOAuuxBKNaaTNLpfFMpcsnqYQxTEPrNi0S6sZN0ra5VDxYR4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a15378585.mp4?token=sB7szce_iG6tOhq68nni0iKyiwWlS1zpuVXX2GaUe1JW4Ht7xxUT1byxiSm8GuhzgYjtGvSnmx5KEAw6Mek-yq3iJ9dcDWt_xCNbcDEYEHCb7eJqSZrqj8Z4In_cu-0fswCDF5dGi9NmskPnCxvBE8Z6Hvu00zfw449evMneS7SgWBL7zPcbgYgRcwxaLUYWjj5u9TLxFmBeFBzcsv7xMRJg_3m-U4n4ztaZ0_cLFgJCJ7a9butS-1Am5aymYdpeq4uaDHprYI2rWOXqcbgH_FjkdwhZhrVXylnZrysOAuuxBKNaaTNLpfFMpcsnqYQxTEPrNi0S6sZN0ra5VDxYR4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو درباره یمن:
به‌نظر من، سعودی‌ها و نیروهای یمنی به‌وضوح مخالف آن هستند که حوثی‌ها کنترل آن منطقه نزدیک به تنگه را در دست داشته باشند.
این منطقه در پی تهاجم حوثی‌ها به تصرف آن‌ها درآمده بود و اقدام کنونی، واکنشی متقابل به آن است. ما انتظار چنین اتفاقی را داشتیم و همین هم رخ داد.
سعودی‌ها هدف حملات حوثی‌ها قرار گرفته و متوجه تهدید ناشی از آن هستند؛ از این رو، حق دارند که از خود دفاع کنند.
نیروهای یمنی تلاش خواهند کرد تا مناطقی را که از آنجا بیرون رانده شده بودند، بازپس گیرند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/72778" target="_blank">📅 16:40 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72774">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdd09dcabf.mp4?token=m31rursu0OCcEvek6Tc0RBDSfuOy1AuFGKbOzsqcUAZOaQao0fb8nl8p-RC7yHsvWYntiAtIbHPSDWNM1-RAQwBTn3wFsIBZZSrcI338f-iskwQ1XP7q2zB54Icmf4baz5_aizx1EcNCD8RrxRy0qG-GqscVRHvwlYvYrnFTBEHp5FZ4gM2tDNw9-VZZzHxW-bZkg8rf49sWsSgrormhbkVeRJ3XQ-t9TLLWy5IEUNbiFWDST5aDF8Ig8fBopl3MALvwt_dAhmZAdo1PD8aXvq_0DnM-ENip8WNa2Bltdf8A3dYhgv6hT7I64Yeus54wv7ZdabqhNmadsjOi-zfdPk71jXDolKN4EfPGKFM4yiGHvvSWOu_KYQu768CcFF5QQyaL_4-9WP5IZSWNAvu5LpyUzBS44dC-yb0QFA-X-cXk6qBPZK2mfoHm0iOEjnPUqhHQcVduOPU-28pTljI65KBu6pvehW_t8QerOKhwSxuyYiypLFZdyVUJyzFWKyS55wUzJQlkGaF5qKgmzuWn73fasVfqw-l4_LHqKa_azFqbK9dbNiTSOKo-_ia-4UU8Wnuqa0yC1oxmPlMKMJbeq8SH7weXPitomc2prVLqfvHPwrqZfCCtQRIBVnH106c4iRzEMaz9tLk-Ol6nKQXDpeYXI-rzuJrji7VXvhXjWnc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdd09dcabf.mp4?token=m31rursu0OCcEvek6Tc0RBDSfuOy1AuFGKbOzsqcUAZOaQao0fb8nl8p-RC7yHsvWYntiAtIbHPSDWNM1-RAQwBTn3wFsIBZZSrcI338f-iskwQ1XP7q2zB54Icmf4baz5_aizx1EcNCD8RrxRy0qG-GqscVRHvwlYvYrnFTBEHp5FZ4gM2tDNw9-VZZzHxW-bZkg8rf49sWsSgrormhbkVeRJ3XQ-t9TLLWy5IEUNbiFWDST5aDF8Ig8fBopl3MALvwt_dAhmZAdo1PD8aXvq_0DnM-ENip8WNa2Bltdf8A3dYhgv6hT7I64Yeus54wv7ZdabqhNmadsjOi-zfdPk71jXDolKN4EfPGKFM4yiGHvvSWOu_KYQu768CcFF5QQyaL_4-9WP5IZSWNAvu5LpyUzBS44dC-yb0QFA-X-cXk6qBPZK2mfoHm0iOEjnPUqhHQcVduOPU-28pTljI65KBu6pvehW_t8QerOKhwSxuyYiypLFZdyVUJyzFWKyS55wUzJQlkGaF5qKgmzuWn73fasVfqw-l4_LHqKa_azFqbK9dbNiTSOKo-_ia-4UU8Wnuqa0yC1oxmPlMKMJbeq8SH7weXPitomc2prVLqfvHPwrqZfCCtQRIBVnH106c4iRzEMaz9tLk-Ol6nKQXDpeYXI-rzuJrji7VXvhXjWnc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دولت ائتلاف مردمی یمن می‌گوید نیروهایش باب المندب و فرودگاه ذباب را طی یک ضدحمله با پشتیبانی هوایی سنگین عربستان سعودی از حوثی‌ها (انصارالله) بازپس گرفته‌اند.
سرهنگ ماجد النزیلی، سخنگوی ارتش، گفت که تیپ‌های غول‌های جنوبی و نیروهای سپر ملی، این مناطق را به عنوان بخشی از عملیات «فجر یمن» ایمن کرده‌اند.
نیروهای تحت حمایت عربستان سعودی در حال پیشروی به سمت مخا هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/72774" target="_blank">📅 16:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72773">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69ab7e166d.mp4?token=WCvjV5lw7AL8Wm8tgjJWbALZnPpVKE0sqHkrQ4GYHAssAxgjJfItqofWF0X748iGGiEbvwz_r1He0_kYs2wClqmoDvUJs6EdpUh2dJz_r3OlV8IwCqy9N1WgGZ1WkcsMviapDdNiy_QlzLX8DQr4nhtMEOcBxhBKy057d1XO3QmFoMT3PKeqUHum8gqpDbUuWS0ima9Im1mcZw2gMLu605KYLPh-kM9GktpyVYLmwlA9Y-GgLofsepJ-Oovtt09cuVyYQOaAPUP8mVmM9d6X7xqL7LJELVyzIHbG7V8zndVUy3rOsL3eBL_FeboplI3Dchdk3LMj2RxZa8P_KdjBdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69ab7e166d.mp4?token=WCvjV5lw7AL8Wm8tgjJWbALZnPpVKE0sqHkrQ4GYHAssAxgjJfItqofWF0X748iGGiEbvwz_r1He0_kYs2wClqmoDvUJs6EdpUh2dJz_r3OlV8IwCqy9N1WgGZ1WkcsMviapDdNiy_QlzLX8DQr4nhtMEOcBxhBKy057d1XO3QmFoMT3PKeqUHum8gqpDbUuWS0ima9Im1mcZw2gMLu605KYLPh-kM9GktpyVYLmwlA9Y-GgLofsepJ-Oovtt09cuVyYQOaAPUP8mVmM9d6X7xqL7LJELVyzIHbG7V8zndVUy3rOsL3eBL_FeboplI3Dchdk3LMj2RxZa8P_KdjBdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توضیحات خلبان هواپیمایی زاگرس در خصوص نبود رادار و تاخیر پرواز
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/72773" target="_blank">📅 16:03 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72772">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ea9911386.mp4?token=Dt1cDfTLwW_iFovz8R3sA2l_L-JrZCrvjUM3GOuQzNpsrej8xQcZ8wwFRuCO5bLUZcC7FSoYgiBckQYMx7kv0gAMXysyonOTLsWB3y27FRvu23OXbVP4PYZEpVL9rQ4TVPpmFLpwF_IVb_Dn10jHLUI8idjcv_rASjeD3SUQ7yh0MVImPMOKTFIyZ1uVFV8haIkk3rGaz9ekxMMsp0T5FE5ZLdGA7jo6EjWopn2hs1TpWJt5eqJueFrmD3XCTq6i__JWeWbTiiT8BT2eyRHIJCCuvfA4Pfp_dGLEEV8_R9nUT3GWKPAuCZDgJTj0D3MwNcjUP9UMYkDFUDNKXoDqYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ea9911386.mp4?token=Dt1cDfTLwW_iFovz8R3sA2l_L-JrZCrvjUM3GOuQzNpsrej8xQcZ8wwFRuCO5bLUZcC7FSoYgiBckQYMx7kv0gAMXysyonOTLsWB3y27FRvu23OXbVP4PYZEpVL9rQ4TVPpmFLpwF_IVb_Dn10jHLUI8idjcv_rASjeD3SUQ7yh0MVImPMOKTFIyZ1uVFV8haIkk3rGaz9ekxMMsp0T5FE5ZLdGA7jo6EjWopn2hs1TpWJt5eqJueFrmD3XCTq6i__JWeWbTiiT8BT2eyRHIJCCuvfA4Pfp_dGLEEV8_R9nUT3GWKPAuCZDgJTj0D3MwNcjUP9UMYkDFUDNKXoDqYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی پویش جانفدا: در میان ثبت‌نام‌کنندگان افرادی هستن که اقامت آمریکا دارن!
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/72772" target="_blank">📅 15:32 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72771">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6bbcade1f.mp4?token=oQhTwaMkYiq3fCKdbwrBPcw4TD5K9iAgB-NIRw5NrRpU70NFZU_A7B8m-EGyNzGnjr8UuXcY22MR8ecupCymzq10EjLmiNnVB5JvV3IusKmynEgZkr7LdiM7KMlMOwjmICkCv1c1u3_qotWX6JY1KlYQTcqy5ikCK33K8KkZVfoidytUqMHA8TliAT4NKixkwfXfxKhQwKQF80gH_C9iaiX9lHAGGuSjrqK1m6k4rirw4BcV0sLWTC75vAZHXX5maImKejpdE5icmDJuQ1g0wOmT8ZRUjRSMLF8R982eFP901vATUYMtihMr4KkdfIvo3IK3eXXvyDtly2_iJRpy0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6bbcade1f.mp4?token=oQhTwaMkYiq3fCKdbwrBPcw4TD5K9iAgB-NIRw5NrRpU70NFZU_A7B8m-EGyNzGnjr8UuXcY22MR8ecupCymzq10EjLmiNnVB5JvV3IusKmynEgZkr7LdiM7KMlMOwjmICkCv1c1u3_qotWX6JY1KlYQTcqy5ikCK33K8KkZVfoidytUqMHA8TliAT4NKixkwfXfxKhQwKQF80gH_C9iaiX9lHAGGuSjrqK1m6k4rirw4BcV0sLWTC75vAZHXX5maImKejpdE5icmDJuQ1g0wOmT8ZRUjRSMLF8R982eFP901vATUYMtihMr4KkdfIvo3IK3eXXvyDtly2_iJRpy0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاظمی وزیر آموزش و پرورش:
ما در آموزش و پرورش تمام هم و غم خودمون رو به کار خواهیم گرفت تا اقامه نماز کنیم در تمام مدارس کشور بدون استثنا.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/72771" target="_blank">📅 15:04 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72770">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RPzOUhS1G8GfT73Yxn5KlKDnS2r32A76LsxzvILAidck7Mw2Pqi3FYnVnsYcSAOe6eqJib7c-bcxziGgv--eOJh-bjaaEHo2lFTNH6S3-IpfINOLeKBr-SqHxaaWBlDZ-mvYNVjBf2n6d_s9b3N5GVBWeBPbufqJG6HzhGqXRZJpSn4yoVN0AnSfDqRftKjF0KvFXwVeF7WaKdJPRQGWl-Jqj1swYumSSYn34IXvNNBNKTmcxffiMUHWU1NEDWFR3bpPeTtHDESv-RXP9yDOzdx1oH6KgLApIyXknY2SdF2LDEzoolWW51g6kgCJifZzC49gXP_pHdGC9JY3-WuI8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO):
یک نفتکش در فاصله ۱۱ مایل دریایی شمال «خصب» در عمان، از سوی سپاه پاسداران مورد خطاب قرار گرفت و به آن هشدار داده شد که در صورت عدم تغییر مسیر و بازگشت، هدف قرار خواهد گرفت.
نفتکش مذکور از این دستور پیروی کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/72770" target="_blank">📅 14:14 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72769">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sLNlCuA6qd3ymZ1_LRtZ4ke15DwfruV4zp2uNwFbDlS__9-Yoi6EPUWtQw70HRzfWnI6BAK2eM3OTIC5AjkssMVjaFRlgLlu33RQr7ExOzLTrVuf2-xWG-DDrZZZhaeXrB-K6uX6QqAaGkQr3xbfcIoyTvT7BJspOAt-T0bU4bQuIe3iVKqIYjJvkv9fFMHQAnypKv-C9AbP5_AZ0yDPqx78poroty-1QAg2UFUqQ-9XXqhBPHrR7SBOVlEnLq418qAvHy6x2vLrblAL80CzXoDxRwTuP8crUKJyLzvlG3pWWn_P0RO-1iaMiYOZxcdcAO6V6qUsLV_MWfTVdRGOpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
؛
هشدار در روسیه؛ قرنطینه نزدیک به ۲۰۰ نفر پس از مرگ کارمند مؤسسه ضدطاعون؛
در پی مرگ یک کارمند ۲۸ ساله مؤسسه تحقیقات ضدطاعون در منطقه ایرکوتسک، حدود ۱۹۷ نفر از افراد در تماس با او تحت مراقبت قرار گرفته‌اند و برخی مراکز درمانی نیز محدودیت‌های قرنطینه‌ای اعمال کرده‌اند.
با وجود انتشار گزارش هایی درباره نشت طاعون از آزمایشگاه، مقام‌های روسیه تاکنون ابتلا به طاعون یا وقوع حادثه آزمایشگاهی را تأیید نکرده‌اند و علت مرگ را ذات‌الریه با علت نامشخص اعلام کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72769" target="_blank">📅 13:58 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72768">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">یکی از طرفداران پروپاقرص رونالدو:)))
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72768" target="_blank">📅 13:48 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72767">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">مسلمانان در انگلیس با برگزاری تجمعی خواستار حکومت اسلامی در این کشور شدند.
جمهوری اسلامی بریتانیا!
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/72767" target="_blank">📅 13:19 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72766">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abcebd0dcd.mp4?token=WdccBgJuWVkvfwRV9wyx7YHu5e9KRqj3kSEYiRAUb0ztfygn02tmviIUqyDiwYaV5pQe_4vJkvmwjRYEgMqWIqqPlZ69I_o7PMRbG7RUtsHpTT3AXVhS9hVMybeO3LAi9Rd6uFO5Ff2SaSQek9FpG_J4T6-tBk6uaC1rKFpNV_EWoH9triElyK0omNr_jklEaZkHnaTS9L8nLqZfR2V7UtXBZk4VOn_T5VTxFowROSSURGjSvc4Jef8FYGhZjcK6CijdTxXxHB1qNFAY073XgmXgVvX2AqBv2tDckyZMrvwX93FEpnQJ36qGegr611Nft4LVS4C8LXwXq_rcJkt8_qn9_fV6Zd9xk18ocz5cMzKTfcMUI_Af0AtOtFT4JgTgo7olxm4GR3qob7dVNtGoPwWU1Cgd5hPuh4toUyQwq-tCOER2aHu4am8uLK2UrpqpUn8iGAYAxRRrZz02EK-CRhtH_tE9xDGgqvUmfmmUbhnZEd5OJSGPOxzOywmnDfGyJY6rUu0RntKAX1svGxd3YeqNfpC7i2VB9oa4SVAa4cB0KyzMkEYsUQIc2jOGwdK_v65sgJyAIoNK-6BBcWJBl3NMbMFEXS4Kme3XyJUrBDxmO7EWguhnXjECkypeHNHkmnKtcjaKjiuvEbXTCTshoNtAPI0Yd2-uh7UyVuxhWfI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abcebd0dcd.mp4?token=WdccBgJuWVkvfwRV9wyx7YHu5e9KRqj3kSEYiRAUb0ztfygn02tmviIUqyDiwYaV5pQe_4vJkvmwjRYEgMqWIqqPlZ69I_o7PMRbG7RUtsHpTT3AXVhS9hVMybeO3LAi9Rd6uFO5Ff2SaSQek9FpG_J4T6-tBk6uaC1rKFpNV_EWoH9triElyK0omNr_jklEaZkHnaTS9L8nLqZfR2V7UtXBZk4VOn_T5VTxFowROSSURGjSvc4Jef8FYGhZjcK6CijdTxXxHB1qNFAY073XgmXgVvX2AqBv2tDckyZMrvwX93FEpnQJ36qGegr611Nft4LVS4C8LXwXq_rcJkt8_qn9_fV6Zd9xk18ocz5cMzKTfcMUI_Af0AtOtFT4JgTgo7olxm4GR3qob7dVNtGoPwWU1Cgd5hPuh4toUyQwq-tCOER2aHu4am8uLK2UrpqpUn8iGAYAxRRrZz02EK-CRhtH_tE9xDGgqvUmfmmUbhnZEd5OJSGPOxzOywmnDfGyJY6rUu0RntKAX1svGxd3YeqNfpC7i2VB9oa4SVAa4cB0KyzMkEYsUQIc2jOGwdK_v65sgJyAIoNK-6BBcWJBl3NMbMFEXS4Kme3XyJUrBDxmO7EWguhnXjECkypeHNHkmnKtcjaKjiuvEbXTCTshoNtAPI0Yd2-uh7UyVuxhWfI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروهای دولتی یمن مورد حمایت عربستان سعودی اعلام کردند که کنترل تنگه باب‌المندب را به دست گرفته‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72766" target="_blank">📅 12:42 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72765">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q3CtKRqavBSy2rYhQxz2Umc0r_vCR9mRVzX2vcKev60_01rQJb6GgzOFCXsSQf9LfxLoGdbrE15Rc4x3XYLASOMlEKCLhFw7xnpoicGI2eXXZDxnW0MYNCOfo17Mg-HE_z__e2umL1p5muX0PmOyGqxK9l-izFg1fWkESxCbg9ltLtbGQgqDjoPATiZT8Enw_lJt8dFoLKnKeAA2N7WmkB9FLZsnzCYmGRHZGfYfuNonNZO94sf_ybHZ7ceCq68ffWV69ARm2G_mFFUXoZof6_bYjMwdJ9YB2TyWULzZrNxpFNUrOyCPSSF283LCDnLQ9nHx1Z7Ogc7ucJjwUvCQjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علیرضا سپاهی به انفرادی منتقل شد؛ نگرانی از اجرای قریب‌الوقوع حکم اعدام</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/72765" target="_blank">📅 11:53 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72761">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e88e1de928.mp4?token=Nj80fo5wof9bbRoqn_eLwL33fHg_KIwWBxfw1wo-86A_IHQdxuGIidLtl9Fcz8mBCEwbh7KU59I27MB1lemfunEfzRuME9LKb1cs0o9qkBiJsl_c92_ijQz4DeS5DXdDr0AMozcL1im8HLf25A4ZwgRWuEiP7f4gfLUV9GIymg50p3reO9R2aCjFTHATJvBmbM3zOaqDKEnRQaH3hIlK0_suQay5xDYpY4j3uOFM1pW7k8xDGV76-8PPYm_k3PVL41S4cXGUIbkRzl3M-IjVMTdh2Le1RB0UzAouOg_6MIWglVpgUswWB_H2IiqzSVbebYMYPD0-1bcPK2YoG6ZGKg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e88e1de928.mp4?token=Nj80fo5wof9bbRoqn_eLwL33fHg_KIwWBxfw1wo-86A_IHQdxuGIidLtl9Fcz8mBCEwbh7KU59I27MB1lemfunEfzRuME9LKb1cs0o9qkBiJsl_c92_ijQz4DeS5DXdDr0AMozcL1im8HLf25A4ZwgRWuEiP7f4gfLUV9GIymg50p3reO9R2aCjFTHATJvBmbM3zOaqDKEnRQaH3hIlK0_suQay5xDYpY4j3uOFM1pW7k8xDGV76-8PPYm_k3PVL41S4cXGUIbkRzl3M-IjVMTdh2Le1RB0UzAouOg_6MIWglVpgUswWB_H2IiqzSVbebYMYPD0-1bcPK2YoG6ZGKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت خیابان های فرانسه پس از اعتراضات گسترده دانش‌آموزان و دانشجویان به دلیل کمبود معلم و وضعیت بد مدارس
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72761" target="_blank">📅 11:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72760">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72760" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/72760" target="_blank">📅 11:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72759">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/baUVCDcEqtdE-xeIRRTPQIOmhvvPnMM1_6qnM_OwMoJ7MNFgJ1_GXeogJobb3E7cV-Q2aqIOrR9K9xR1BpO1Rc7PvLL2566NBlM30iikANlESKp5Gus8p840gPZSIlFbIJFl3mfGDSNTBw3kquL3RGIpjc1NBcBvYM3gVJ019hszmTlZFtqJCfSwxz-auPeEule-8tNXL5fohGXcrEjyLl5Ad1-bP9S0myFdhB-1Bd0qFdeT_a3E_nHs-Wsmm7mGrcsgIsYmp5gee0aQ1r-x3GKJv-WW5IZ9icGhf7DvKdL3CBiFQDJuyOrbYZHxbhuGhk9ZPcAAy3lBVftObe7Odw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
بلژیک
🆚
فرانسه
ترکیه
🆚
ایتالیا
لهستان
🆚
بوسنی
سوئد
🆚
رومانی
نیوزیلند
🆚
ژاپن
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
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
http://T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72759" target="_blank">📅 11:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72758">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e436b8c05.mp4?token=V124lhfhdxXEqWUoUqR5cNlra_m5se-mf9sSLTpwEwUDM4JDHtz01KRCQkDlHkSdPKqSi--nTz7ZrJsyDNPZujSpNbdk2XwrYjmHFhwqRtfzR-I0S3MJ42nx-MNJXWVpR3giWT-x1kEYXKw-mFNODVXtIjQkUm-9uVQs6m_s5ruA60q3n0dAsCvlKNWodrhw7AIAKtTlTgqZMKRr9Rus947tkxrcECnXWBnyJ0NEYIpnIMALe1JOIJDhLehccLXGVQ-c4wdtEHMEtfaRjC4YW0tlBXdmL94Orni2zJsIUFHpq94THEi9d7RfQU4FzkWCGl__cRLRHhVrbHN5Zzt-Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e436b8c05.mp4?token=V124lhfhdxXEqWUoUqR5cNlra_m5se-mf9sSLTpwEwUDM4JDHtz01KRCQkDlHkSdPKqSi--nTz7ZrJsyDNPZujSpNbdk2XwrYjmHFhwqRtfzR-I0S3MJ42nx-MNJXWVpR3giWT-x1kEYXKw-mFNODVXtIjQkUm-9uVQs6m_s5ruA60q3n0dAsCvlKNWodrhw7AIAKtTlTgqZMKRr9Rus947tkxrcECnXWBnyJ0NEYIpnIMALe1JOIJDhLehccLXGVQ-c4wdtEHMEtfaRjC4YW0tlBXdmL94Orni2zJsIUFHpq94THEi9d7RfQU4FzkWCGl__cRLRHhVrbHN5Zzt-Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مراد ویسی:
جنگی که توی راهه، آخرین جنگ ترامپ با جمهوری اسلامی خواهد بود!
اما به قدری این جنگ شدید و گسترده‌اس، که جنگ ۱۲ و ۴۰ روزه، پیشش یه شوخیه!
شدت بمبارون‌ها خیلی شدیدتر خواهد بود، کشورای بیشتری درگیر میشن و این نبرد آخره!
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/72758" target="_blank">📅 11:06 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72757">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cf7a6e5830.mp4?token=ZVG0xAL-JCy4UKK-Ejir3XZPWmL4JnCkgVz9CpAI8GH3eqA7g6Jop0y4pGLDv_LpayMe0mmIegfuxjEMz6BRt1qqlAA3i2S3JVgMR0sMXxi-XlQ9ZdwYpGIX5xxHiSy8On8YV3ZGY-mqQW6w6GiXOS2tr6z1BMwWGEZxF6UNSM1yVLnURwdfjV-9F5jTmVg4tJKahQmwjyG6ky-SIAFESqNblZ77_Ex-75QwemyUQg_rLWU9O5gLlFyykE18ZyZjI6wW5JreFomJk9DZdKlBNkOhPcgVjvxzw79sqiKRqpdFeVnTpaJtVfQe-f8IBjEfj4tYBsfRjxhRmP7TWGkQQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cf7a6e5830.mp4?token=ZVG0xAL-JCy4UKK-Ejir3XZPWmL4JnCkgVz9CpAI8GH3eqA7g6Jop0y4pGLDv_LpayMe0mmIegfuxjEMz6BRt1qqlAA3i2S3JVgMR0sMXxi-XlQ9ZdwYpGIX5xxHiSy8On8YV3ZGY-mqQW6w6GiXOS2tr6z1BMwWGEZxF6UNSM1yVLnURwdfjV-9F5jTmVg4tJKahQmwjyG6ky-SIAFESqNblZ77_Ex-75QwemyUQg_rLWU9O5gLlFyykE18ZyZjI6wW5JreFomJk9DZdKlBNkOhPcgVjvxzw79sqiKRqpdFeVnTpaJtVfQe-f8IBjEfj4tYBsfRjxhRmP7TWGkQQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاطره یه دختر تن فروش: یه دفعه یه سید بهم گفت بیا رابطه داشته باشیم، فقط تو زود بیا چون ممکنه خانمم بیاد خونه.
رفتیم تو اتاق و شروع کرد صیغه خوندن، هر چی قرآن، آیت الکرسی، تابلو و کتاب دعا بود برعکس کرد و گفت زشته، گناه داره.
یه دفعه وسط عملیات زنش اومد، گفت سید زودباش درو باز کن خیس شدم زیر بارون، سیدم بهم گفت تو فقط چادر بنداز سرت شروع کن نماز خوندن.
خانمش اومد به سید گفت این کیه؟ برگشت گفت این خانم مسافر بود، اومد گفت نمازم داره قضا میشه، میتونم خونه شما بخونم؟ منم آوردمش نماز بخونه.
آخرشم خانمش بهم چایی داد و کلی پذیرایی کرد و رفتم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/72757" target="_blank">📅 10:30 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72756">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de6e0dfa99.mp4?token=hbWbVi5Cm1SBydtcCFsxs9ymn80Hwkio6CmhG8q5vciTBrNksMUssftafR89ZD-8kHKIa2-AJLFjP4cggzZacEWXGXKoDRl36cjw_1mAacpX8e8xi3GzkT_PfsvnbIERdP_G4u70ZbU9B6F7YBTxH5MlfMy3i2nLiU8SkbxpgQWTYdHaQ5ExlFZZVx7Ya8xXDqUQXlvwbmWYP6RUl5enh2OCiAw7vCKCSzU2iINKWirZDnuj9TtW0G9mGFaWUN9LwUwTgF7awO42d5jqhNLtHwHxL1yQpUBWSaapRI_yKpp5QwIeIXFVzsh9vb7Lm468Za1rs41Ktv-Tl9y1QOLU3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de6e0dfa99.mp4?token=hbWbVi5Cm1SBydtcCFsxs9ymn80Hwkio6CmhG8q5vciTBrNksMUssftafR89ZD-8kHKIa2-AJLFjP4cggzZacEWXGXKoDRl36cjw_1mAacpX8e8xi3GzkT_PfsvnbIERdP_G4u70ZbU9B6F7YBTxH5MlfMy3i2nLiU8SkbxpgQWTYdHaQ5ExlFZZVx7Ya8xXDqUQXlvwbmWYP6RUl5enh2OCiAw7vCKCSzU2iINKWirZDnuj9TtW0G9mGFaWUN9LwUwTgF7awO42d5jqhNLtHwHxL1yQpUBWSaapRI_yKpp5QwIeIXFVzsh9vb7Lm468Za1rs41Ktv-Tl9y1QOLU3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو وایرال شده از یه عراقی :
به حضرت عباس اگه بگن بین پسرات و جمهوری اسلامی یکیو حذف کن میگم بچه هامو حذف کنید تا فدای جمهوری اسلامی بشن
ایران از بچه هامم ارزش بیشتری داره
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/72756" target="_blank">📅 10:01 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72755">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aaee08d663.mp4?token=OADSgiVuahdGRovBmsungJZcRmLZtLtFPJj9hGd1wrV0AeSNRC4uB8JtWhUPzsSM3I1lbW0Quc0ir36wcNhFrzP4fBJE388pC_PYEpdNj4jJSwcsv3lrH0QiJIBUidQkze9vuxF-8LHEEfkXkMu0o2eRBqO9eoiysNZ0oCGBO4LuhUqznfVLyGRFZ79MjQA55HaMaYHxUSRa4fdOmudIGJH512zXFkxOxg741C9yyD7z7tJohB31UiY3RIDbJrwVoCNp2WqKoc-SrJWPlqBN5sfWOaWJvJq0p4GnVkeu7CLLh6DlUKgxzo5rz13FBoAYwAFQ4d8k4ZULhJXBgG75mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aaee08d663.mp4?token=OADSgiVuahdGRovBmsungJZcRmLZtLtFPJj9hGd1wrV0AeSNRC4uB8JtWhUPzsSM3I1lbW0Quc0ir36wcNhFrzP4fBJE388pC_PYEpdNj4jJSwcsv3lrH0QiJIBUidQkze9vuxF-8LHEEfkXkMu0o2eRBqO9eoiysNZ0oCGBO4LuhUqznfVLyGRFZ79MjQA55HaMaYHxUSRa4fdOmudIGJH512zXFkxOxg741C9yyD7z7tJohB31UiY3RIDbJrwVoCNp2WqKoc-SrJWPlqBN5sfWOaWJvJq0p4GnVkeu7CLLh6DlUKgxzo5rz13FBoAYwAFQ4d8k4ZULhJXBgG75mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار :
از آقا مجتبی (خامنه‌ای) چخبر؟
حداد عادل پدر زنِ مجتبی خامنه‌ای :
سلام میرسونن...انشاالله خوبن...همیشه...خوبن الحمدالله
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/72755" target="_blank">📅 09:32 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72754">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32e173a359.mp4?token=tFSTov2rq5vtyI_8w-_0umTmGPxhGYETzneZkfK4EKIuRTBbg59UwHy5tCDa8L_toXEI2jkKTPJ3rMp9ftCfBb16hM9hVpbC__BKcbFd6MekZmVI0RkUxIY-HUjJnl9lgGWc3OhWmC-4Kgqa5qQmmwbobKiu5wPtdL2TsE-WgTEgqC6Y8JC5JdsIAbyYBduPgu3fNqr6zyI7lNpkoAjQ6F6F-L4iS4kLfUk6Gihw_lyFRcNMXaaQ5VIdfdUzhUemD4BK5XHHp7vgPrkeSbnhW2LXuAgQgSDLLe7UFIq90WslRGKc8QNDcXNswhzm8nVWYmAWWG-gg_iLs7nLyiBq8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32e173a359.mp4?token=tFSTov2rq5vtyI_8w-_0umTmGPxhGYETzneZkfK4EKIuRTBbg59UwHy5tCDa8L_toXEI2jkKTPJ3rMp9ftCfBb16hM9hVpbC__BKcbFd6MekZmVI0RkUxIY-HUjJnl9lgGWc3OhWmC-4Kgqa5qQmmwbobKiu5wPtdL2TsE-WgTEgqC6Y8JC5JdsIAbyYBduPgu3fNqr6zyI7lNpkoAjQ6F6F-L4iS4kLfUk6Gihw_lyFRcNMXaaQ5VIdfdUzhUemD4BK5XHHp7vgPrkeSbnhW2LXuAgQgSDLLe7UFIq90WslRGKc8QNDcXNswhzm8nVWYmAWWG-gg_iLs7nLyiBq8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در حاشیه ختم خواهر عباس عراقچی، وزیر اقتصاد از پاسخگویی درباره وضعیت فروپاشی اقتصادی و کاهش ارزش ریال فرار کرد و خبرنگاران را به همتی، رئیس بانک مرکزی، حواله داد و همتی هم بدون پاسخگویی فرار کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/72754" target="_blank">📅 09:02 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72753">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72753" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/72753" target="_blank">📅 01:41 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72752">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H-jyfOHpK63wYe-6vJFBMTshrfhS_v9E5ulerhH5FKK6VjTID9-uHEy2nWURurR2WTPiAylQFoHxsqw1RYYJ7EqHAOipto8K6lIkHiMjAgNarNKDLlzo5Ihhx1rBpMRR25ZMX8gZ3SmEyHqLZfB_33beqgir4a3gXuLFT777rvTcV7VnfMMvpiJigJdsj9o3qXpByYSggOupBy3ndpuuq9aNyynMyTpozOpjD3rWsbGtaqbS-pNYEs48PG2QWYCVC9N-P09Np_6zcOhQlf5TjIxSd_D4BVZyx1qTI7yxmep8XqSelJu4amgdLT6We2F0q-seScXQaZD-VjwVypWdIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول: ۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم: ۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم: ۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم: ۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/72752" target="_blank">📅 01:41 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72751">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WQZvAUHazGjMqrOL73TlmJAYZ0nzeA6aocondRGWyEp0ipSzu9XJLHxTiDewh5pa-UusGetAUfkKQfJFs_KCMtpMUWJyGMR_tiW-Wrek3UL6Or_16j6CQs_Klxje8gNsrL817X4hnxfbJ8pDdneNmortq0iIDOBYsOYkGPOZEcgP3VFN6RvPAb5VVV4vgWjn2dREe2OnsPWkViG7m7219RkBKlJkpqf8K9hvC-7FZineITjex6xA0SGBB1BkqcsCCZV2J9afFGABW948_55xA1rnfUYcbJkmqjzRJmuwJDxpAU52aw2TtUreoHdz9G2rU9yID15l3x0mx3CKqw_w4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وال‌استریت ژورنال به نقل از مقامات آمریکایی گزارش داد که بمب‌افکن‌های راهبردی «بی-۱بی لنسر» (B-1B Lancer) در حال خروج از پایگاه نیروی هوایی سلطنتی بریتانیا در «فِیرفورد» (RAF Fairford) هستند؛ این اقدام به دلیل نگرانی‌های امنیتی و در پی دریافت اطلاعاتی مبنی بر وجود طرحی از سوی ایران برای حمله به این بمب‌افکن‌ها در پایگاه مذکور و کشتن کارکنان آن صورت می‌گیرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/72751" target="_blank">📅 01:32 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72749">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s8jDVGyUOvYbIV8cU4ljzyY_QYxDHeVrCliTrqrIRK9ej1L2zqLP5tIOtEsfgz3FmbkbrVd5lgHi0OqvWwip6Us0vlvW5px4XDAKVQnEuHl5JnkNGr05Xs4XVS8Ct6el9Z7NCMD_YJlnu87t5g35B4mr2ItmgkMEgqe5k2BV0cpSdv-4JCoxD-XuyzH7Y9fJNTlrbqWxmtUEBtsv6lZGVER2FvEGIquKCR68VdjTfYm3nTq1EA22lh1UyXShsJMyywPDN3xSG-UyEM1MMfbviHVEsoQAaNYOw5nkmtKC8DlZTvtT61wX353t9ieFMvJ1kZ1xCdn5qFHHV7k3o7WocQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5cef955dd4.mp4?token=IiPeTo4xAQZ3b9lZwXSvioWzNPYpw-ayFNAsP0cGfX_OagKp3U41Tcbxwz2TZVNcYH2hbv8tbqojRSjZvZ-9IfTPLmE5CJN1_1Y_aoGKV94bgoc1KwRa0HrrfnNvTdITZxYAqgJkZwfJ3aJYErN-eJsW22-L-7rrlIKJJ8bS097etG-fv0mscuzWowenucWggV-v6R7blvrfa4N7gfCmRWbe2W6cFDmgwf8je3ncVdkFgQ7zfpAhym1U09TEWvLCkL6mXPbsb4Bj9eT5Hv1OUfAWVhdLC4rmymtGCwhgLYZAXfvTqaMojqM7Xajniaq62_d6c-wVe8P-ILXtNFzyVA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5cef955dd4.mp4?token=IiPeTo4xAQZ3b9lZwXSvioWzNPYpw-ayFNAsP0cGfX_OagKp3U41Tcbxwz2TZVNcYH2hbv8tbqojRSjZvZ-9IfTPLmE5CJN1_1Y_aoGKV94bgoc1KwRa0HrrfnNvTdITZxYAqgJkZwfJ3aJYErN-eJsW22-L-7rrlIKJJ8bS097etG-fv0mscuzWowenucWggV-v6R7blvrfa4N7gfCmRWbe2W6cFDmgwf8je3ncVdkFgQ7zfpAhym1U09TEWvLCkL6mXPbsb4Bj9eT5Hv1OUfAWVhdLC4rmymtGCwhgLYZAXfvTqaMojqM7Xajniaq62_d6c-wVe8P-ILXtNFzyVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علیرضا سپاهی به انفرادی منتقل شد؛ نگرانی از اجرای قریب‌الوقوع حکم اعدام
علیرضا سپاهی، از معترضان بازداشت‌شده در جریان اعتراضات دی‌ماه ۱۴۰۴(پرونده میدان علیخانی اصفهان)، به سلول انفرادی زندان دستگرد اصفهان منتقل شده و خانواده او برای آخرین ملاقات فراخوانده شده‌اند.
وکیل علیرضا سپاهی نیز انتقال موکلش به انفرادی و اطلاع خانواده برای آخرین ملاقات را تأیید کرده است.
بر اساس گزارش ها دختری که عاشق علیرضا بوده گفته آرزو دارم باهاش ازدواج کنم و امشب در زندان خطبه عقدشون تلفنی خونده شده
💔
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/72749" target="_blank">📅 01:04 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72748">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nW_9oVFemg1KJLSpTbgsOTz62z8ntXwrbn6V9EIEyBzCGV2x9BmLVRpG6VIoSFJv3nnjVf375oqDvrtynZJtEirI9hPpmuka3Sx4ecZNx1q2X5x4JPVB8fEaqr9SAMZ04G2ff1yww1Fba0RmIa_6S0XUq8mGMqypXJUtOOS7X3fToF-Ts3QvgeCJvxMzLlmeedZFRMsB2uKNfdvYfvQtGzcJEjE1fRcqQwvIATgMoxK_8JDLAkIQ7o2yqHmuQdG-hMhBR1uA4cWhBlXNA9NkLoXeRRIKokDDuwlEIa-0sICnwPppBeS2s3xIp2QXOtAYOowmg4n6mSvamzrd57yHHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید صفحه یوتیوب امیر تتلو:
امروز دادستان و رئیس کل دادگستری صحبت‌های خوبی با تتلو داشتن و اگه گزارش خوبی هم رد کنن، امیرتتلو فردا آزاد میشه و به استقبالش میریم!
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/72748" target="_blank">📅 00:46 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72747">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">۱۰فروند از ۱۲ بمب‌افکن راهبردی B-1B Lancer نیروی هوایی ایالات متحده که در پایگاه «آر.ای.اف فیرفورد» (RAF Fairford) انگلستان مستقر بودند، در حال ترک این پایگاه و بازگشت به خاک اصلی آمریکا هستند. انتظار می‌رود دو فروند باقی‌مانده نیز امروز این پایگاه را ترک…</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/72747" target="_blank">📅 00:37 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72746">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec28377bbb.mp4?token=rmabcly5ly9cvDWazFVKhBdX0ZgfG21JoJuwM7ygk2B_ohR52FPbwO6tWhw2H2ExijVl3H79hrG2owabeh1vEP5xbyt9_nJ9FKbgGt1XWGfFVfzjrJpyHe5FPV8JdroMTAXnePUV5H1SSar9TmKchJTru9PUBKe9DRVfOTcMcOYmOVvFgsWxOze61V39QVZh9zvGY2_Z3VHyjWz4nWpX2rzBK8IIHEzfQ2-e-7mNzE-DdygWAA3_0OHk7qzKuSmVMkytRgXS52QR3NMdYdgXBJtu-DltoHoPl9JX6Rgbf01e7hlRNt-5VhJefabCPvpoGSbrhy4BwFYEi4UN3pKV2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec28377bbb.mp4?token=rmabcly5ly9cvDWazFVKhBdX0ZgfG21JoJuwM7ygk2B_ohR52FPbwO6tWhw2H2ExijVl3H79hrG2owabeh1vEP5xbyt9_nJ9FKbgGt1XWGfFVfzjrJpyHe5FPV8JdroMTAXnePUV5H1SSar9TmKchJTru9PUBKe9DRVfOTcMcOYmOVvFgsWxOze61V39QVZh9zvGY2_Z3VHyjWz4nWpX2rzBK8IIHEzfQ2-e-7mNzE-DdygWAA3_0OHk7qzKuSmVMkytRgXS52QR3NMdYdgXBJtu-DltoHoPl9JX6Rgbf01e7hlRNt-5VhJefabCPvpoGSbrhy4BwFYEi4UN3pKV2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ادعای عجیب در تجمعات شبانه: حسن روحانی در یک سفر استانی دستور داد برای دستشویی‌اش کولر نصب کنند!
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/72746" target="_blank">📅 23:33 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72745">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7673e09822.mp4?token=FWXeeGICZEw7s4DyvsbTN-1tHX0gxL0zD_cf9cE8IwZCnCOP8TtGLuAm2Gn2iDV6-Be9jwX1EWxjwov2xYNf4IuW4yxgoy6Lu1cD9ltbwNVRcC4z55ABN1ajR9jpc4LCilTZPCrBGdhE6UMmpIKfOrfjl1jfCTuRNdsXOSbYo6wCDfnobSx-iZMuu3TY39lkRKuaPmyJd8PWYR8O6l6VBG6cgUjdMlcSvUlGrnaK9c71eWNSTwi8IlKWiKTn6LGJxI0bYlTx3MJ-XYaJOjoi8egm4uN3GpiQ_qTWVWH6LTzoN6iTvqk_2L3C70ylRhBpSSSwEF0cbB5LYc7aqFSE-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7673e09822.mp4?token=FWXeeGICZEw7s4DyvsbTN-1tHX0gxL0zD_cf9cE8IwZCnCOP8TtGLuAm2Gn2iDV6-Be9jwX1EWxjwov2xYNf4IuW4yxgoy6Lu1cD9ltbwNVRcC4z55ABN1ajR9jpc4LCilTZPCrBGdhE6UMmpIKfOrfjl1jfCTuRNdsXOSbYo6wCDfnobSx-iZMuu3TY39lkRKuaPmyJd8PWYR8O6l6VBG6cgUjdMlcSvUlGrnaK9c71eWNSTwi8IlKWiKTn6LGJxI0bYlTx3MJ-XYaJOjoi8egm4uN3GpiQ_qTWVWH6LTzoN6iTvqk_2L3C70ylRhBpSSSwEF0cbB5LYc7aqFSE-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سیل اخیرِ گرگان، یه
موش
برای اینکه جونشو نجات بده، این شکلی داشت تلاش می‌کرد...!
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/72745" target="_blank">📅 23:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72744">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bffb33370b.mp4?token=iVr7ziua67v4q4cX-hx6Mv3bMvv3ASV2U7pESLHK1SB_Dwls9oPAXj57EeYF1yy0iNoQGcwk56ur3Dsm-rR6_oEoRcZFZmcWfhW3xer6OEi1stQj07Y-tSwYT3fxA5HPMSsrD_dL9M2y77mk5i7Oe2UWd6AD6ijV4gXKuOuHph8ZViE-iEC4hodE80tdM6l06ktRX7dHYxURZIeeVBzOllWmdEcsWuM-aL2UIgFKXumYyaUyFTxzl3oN3UCrSVGNDcGn54y4uJAvPxOHkDwKGzN31kdVgvQCX0qQmnGqmxOHsJP7HVvW9OQmJl8A19OQBIV1eGTxWmxJ_HcrvDb0IZJztX-X4Kw4Snyr_uqW63rWOAS-NCis_VQSCrpwqODIeUWJQZEMx2EwSKDxGICqw3EalncGcosAaaKSeLsZFnqU0GmLEDJC_x8cTIY_RHfHZmRdcqDxXzJtHRjowhQAAwrI3d5cj78U1cOD4VMNVynrK2oKr3N-bae0AojFgUmNdaNGJywd5meTf6TeOp96MzbqBUx7-mOck__eKWsrS_LXF92qGQS4Jvpx3SKRj69p-fATbYusG6q_4cGaywHef-SkjL78R_jrJ1RpRzgGoZ2jjsGw6-ogShxXE7BkYrGa6T0uSyGEHx8V28uwkJvwB3cA-bXtYaaD4Q2kTPyuU1I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bffb33370b.mp4?token=iVr7ziua67v4q4cX-hx6Mv3bMvv3ASV2U7pESLHK1SB_Dwls9oPAXj57EeYF1yy0iNoQGcwk56ur3Dsm-rR6_oEoRcZFZmcWfhW3xer6OEi1stQj07Y-tSwYT3fxA5HPMSsrD_dL9M2y77mk5i7Oe2UWd6AD6ijV4gXKuOuHph8ZViE-iEC4hodE80tdM6l06ktRX7dHYxURZIeeVBzOllWmdEcsWuM-aL2UIgFKXumYyaUyFTxzl3oN3UCrSVGNDcGn54y4uJAvPxOHkDwKGzN31kdVgvQCX0qQmnGqmxOHsJP7HVvW9OQmJl8A19OQBIV1eGTxWmxJ_HcrvDb0IZJztX-X4Kw4Snyr_uqW63rWOAS-NCis_VQSCrpwqODIeUWJQZEMx2EwSKDxGICqw3EalncGcosAaaKSeLsZFnqU0GmLEDJC_x8cTIY_RHfHZmRdcqDxXzJtHRjowhQAAwrI3d5cj78U1cOD4VMNVynrK2oKr3N-bae0AojFgUmNdaNGJywd5meTf6TeOp96MzbqBUx7-mOck__eKWsrS_LXF92qGQS4Jvpx3SKRj69p-fATbYusG6q_4cGaywHef-SkjL78R_jrJ1RpRzgGoZ2jjsGw6-ogShxXE7BkYrGa6T0uSyGEHx8V28uwkJvwB3cA-bXtYaaD4Q2kTPyuU1I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیرک جانفدایان در اصفهان، سازماندهی اراذل و اوباش با قمه و شمشیر و چاقو!!
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/72744" target="_blank">📅 22:15 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72743">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BlXGyndw6XuYYCirjTNMHMtv5b2-wXirulAYp-TyGxPRwlTRzYFubLoJDBzxarBy7ePKy40NeMVzskOv-Fzu3exyHtf6ftpn06wLadGpUu3Rca_vIWTKTgWinnoNFnAw8Grc5sazrA_Yn-f7robyAOhODSKx6UURC2AYY2W4ABO6-oZd698Su0eJrFo3T0UCtYmc2qb2R37XRIfKz60rBUt4cKcHSZbObU8hARNgDoRktTaABTv8cVigBN6iSJVFyRZC7iyTmbjHVvtZo3Ztisg6CBWDP5Hyv5Hc3t2oEUjCqKaUh3Ai0KnSDpbBUp7zUveC6wkM8SPQvaI_pb6Xjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ تصویری از خود به همراه پنگوئن‌ها در گرینلند منتشر کرد.
پنگوئن‌ها در گرینلند زندگی نمی‌کنند
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/72743" target="_blank">📅 21:36 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72742">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">شنیده شدن صدای انفجار در جزیره قشم   @News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/72742" target="_blank">📅 21:03 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72741">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">شنیده شدن صدای انفجار در جزیره قشم
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/72741" target="_blank">📅 21:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72740">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d25df363a1.mp4?token=Q1glQnGhYD9J7AnRaY4tFqJMx-5iJZkdxL5unhD3Pme8wRQLxRHmWWw0LmNoTRNKv58K983sd0E0OGQLXVTfJgqqtkqNQTOZvZpBx2ROwh0w21lJfkgreTWfypKhenpnRtzuOY07WTL0vWqsPeDl8IeBsv7Z-YsNFD_o6RgEul0IZNbUi9h0pXefcJoAuXXyi6by6oAghRf3vrn4XDBmSG3vFIG26rAPGotuPrQK6Oqubuy1WCSfbjZv-Ev9E1C-FRnk-5wTsNlTGN-5CDIXZoeFgJR0uaDEHyckYNSxqDvofBO5qrKMhzLLlTmi9iLRE06Slu2UNt75Q5up4aOAlA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d25df363a1.mp4?token=Q1glQnGhYD9J7AnRaY4tFqJMx-5iJZkdxL5unhD3Pme8wRQLxRHmWWw0LmNoTRNKv58K983sd0E0OGQLXVTfJgqqtkqNQTOZvZpBx2ROwh0w21lJfkgreTWfypKhenpnRtzuOY07WTL0vWqsPeDl8IeBsv7Z-YsNFD_o6RgEul0IZNbUi9h0pXefcJoAuXXyi6by6oAghRf3vrn4XDBmSG3vFIG26rAPGotuPrQK6Oqubuy1WCSfbjZv-Ev9E1C-FRnk-5wTsNlTGN-5CDIXZoeFgJR0uaDEHyckYNSxqDvofBO5qrKMhzLLlTmi9iLRE06Slu2UNt75Q5up4aOAlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۱۰فروند از ۱۲ بمب‌افکن راهبردی B-1B Lancer نیروی هوایی ایالات متحده که در پایگاه «آر.ای.اف فیرفورد» (RAF Fairford) انگلستان مستقر بودند، در حال ترک این پایگاه و بازگشت به خاک اصلی آمریکا هستند. انتظار می‌رود دو فروند باقی‌مانده نیز امروز این پایگاه را ترک کنند؛ بدین ترتیب، دیگر هیچ بمب‌افکن راهبردی‌ای در «آر.ای.اف فیرفورد» حضور نخواهد داشت.
پنیک نکنید!
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/72740" target="_blank">📅 20:59 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72739">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eh7_gRNWoWYySaorDmf7APiGBqd-8Ii_uWi4A9lFBXekXXlVhAin8e4e_q6q-QxVKS2UlchPl3SuS8ById9x1TZDkDYJJfqpvTqy-qwFyIVxW3rbTCi9PrXmBzvNWJMQqYbBnzVjZ_PgPwhh0uqaK9Kj9wt3RSx-6MsVCOV6tsV3uzq5KtZ3gpTLn34IDmM9x1nQmYhjTvfXwx-EuCZZPW2akLBtTB8niVIIodhLXWEqNbPhspQvryx_hHBhLJ-QndGz5NUV62l2q6-E4xEHrDZawSO5Kg5bBBptL-NVdAId89qYZaw-8Vfi4hYsK4G_sYP2-jaqVRqdHzhc98vOgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
؛محسن پاک‌نژاد، وزیر نفت جمهوری اسلامی، استعفا داد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/72739" target="_blank">📅 20:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72736">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1dad032a8.mp4?token=GzByGRZITDDU3nHY3AeWPui_wJ8AQmxCMreEMxlriYWy_Bla_tf190jk1nuRxLbe6gApK3YoRFAWcXqFnJrdxDQnXP6oYn0PJn1zmhoym6My4bzZj_cNH5Bk-biSNeHGfaS6KG3RBjxVJ61AUgGd7GCl-d0sM0zWSJSm2QvSa67mbF0Ph9dKO4iWS8sWVs2GlQk59Ojhr5uiqr5a3KaahdW47WU3LuA2pfFotm9G8ow4sAGY4E_JJ_Ar1BdETbruePhtatZdcFFnKQacoAGGaAvkuOvk-bkXMSAqQC30P93t_0mmL74fMVKAwvmOJt9bFGbai_TVPQMJUvq1ALxkTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1dad032a8.mp4?token=GzByGRZITDDU3nHY3AeWPui_wJ8AQmxCMreEMxlriYWy_Bla_tf190jk1nuRxLbe6gApK3YoRFAWcXqFnJrdxDQnXP6oYn0PJn1zmhoym6My4bzZj_cNH5Bk-biSNeHGfaS6KG3RBjxVJ61AUgGd7GCl-d0sM0zWSJSm2QvSa67mbF0Ph9dKO4iWS8sWVs2GlQk59Ojhr5uiqr5a3KaahdW47WU3LuA2pfFotm9G8ow4sAGY4E_JJ_Ar1BdETbruePhtatZdcFFnKQacoAGGaAvkuOvk-bkXMSAqQC30P93t_0mmL74fMVKAwvmOJt9bFGbai_TVPQMJUvq1ALxkTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رتبه یک کنکور تجربی همین‌جوری داره بین موسسه‌های کنکوری دست به دست میشه و تو همشون میگه که من از بچگی اینجا بودم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/72736" target="_blank">📅 20:15 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72735">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/112f06092b.mp4?token=RXdXo0rnAZy91i0e3hqqNjAdg-OM8OFitvvg8khLX1y74z8l-WZcb8oj09_iovG8aD9Ze6MFoLI32V8xLfFVvDUVslLITZzxVjdZSe2xW9oqBhjug3X7CFALvlwN3kNmOAFkgC5AMQKBgLbVKfHddKDw6y-jvQOt2A59N-XGaeujVjCcEUgwXhm4l84w8xuWzXruwwuI9jVgw08rhRXACSXW7Mp1mthhRnSg7h6AkIQ5vB9_QrJyiuBfDv82XuK3roabnz9KXlHMEHhx5XmDx5OFfCDffKYRsq2o1Qtc-fDgzaKO5O4G_XMc4Vn9m5qOMh6kdy-1JoqP9DHkaXQu-KB9sqclHEbj5ApwXCaQOycoWfngUTQtrbDpCv6MQBwZfbHFnm24DjfQXbt5Bu7ZDqHSr1Y25loV4Tff5tA7e5IUQzkAMOuYRpti96JSEBDgIXiVh4-mlW7k5CUHC749qhLG7fKCTE5Ppd1jmN6bK544Fr2aeO-E1b6aCDmtVdT77XAfLPpUK1MEFmtp5PebNLQ4jeqH5FNeLtMZnRWR8-emrSJcz9gwDDtMgdh-VXFpCTnynhmKpdNC73n6PvT_chlUfc7zxXGTI6OavdzAkAyaLf59k0kaJEiakkAPd1RluKelRlYfkOXQxihUnA7EVjPOLqElt_mFm4v4Tm6koXo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/112f06092b.mp4?token=RXdXo0rnAZy91i0e3hqqNjAdg-OM8OFitvvg8khLX1y74z8l-WZcb8oj09_iovG8aD9Ze6MFoLI32V8xLfFVvDUVslLITZzxVjdZSe2xW9oqBhjug3X7CFALvlwN3kNmOAFkgC5AMQKBgLbVKfHddKDw6y-jvQOt2A59N-XGaeujVjCcEUgwXhm4l84w8xuWzXruwwuI9jVgw08rhRXACSXW7Mp1mthhRnSg7h6AkIQ5vB9_QrJyiuBfDv82XuK3roabnz9KXlHMEHhx5XmDx5OFfCDffKYRsq2o1Qtc-fDgzaKO5O4G_XMc4Vn9m5qOMh6kdy-1JoqP9DHkaXQu-KB9sqclHEbj5ApwXCaQOycoWfngUTQtrbDpCv6MQBwZfbHFnm24DjfQXbt5Bu7ZDqHSr1Y25loV4Tff5tA7e5IUQzkAMOuYRpti96JSEBDgIXiVh4-mlW7k5CUHC749qhLG7fKCTE5Ppd1jmN6bK544Fr2aeO-E1b6aCDmtVdT77XAfLPpUK1MEFmtp5PebNLQ4jeqH5FNeLtMZnRWR8-emrSJcz9gwDDtMgdh-VXFpCTnynhmKpdNC73n6PvT_chlUfc7zxXGTI6OavdzAkAyaLf59k0kaJEiakkAPd1RluKelRlYfkOXQxihUnA7EVjPOLqElt_mFm4v4Tm6koXo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهنشاه محمدرضا پهلوی:
"همیشه تلاش میشود ایرانِ دوران من با بهترین دموکراسی‌های جهان مقایسه شود، ایرادی هم به آن ندارم.
اما درباره اینها (ج.ا) که چنین قتل‌عام میکنند همه می‌گویند بگذارید درک‌شان کنیم، بالاخره اسلام وضع ویژه‌ای دارد، در حالیکه آنچه اینها (ج.ا) می‌کنند، در تناقض با اسلام است.
حتی در لیبرال‌ترین محافل، دوران من با بی‌نقص‌ترین دموکراسی‌ها قیاس می‌شود اما به اینها که می‌رسد می‌گویند بگذارید درک‌شان کنیم، اجازه دهید با آنها دیالوگ برقرار کنیم.
این چیزی است که برای من قابل درک نیست."
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/72735" target="_blank">📅 19:32 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72734">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fe642fca6.mp4?token=anBk_JdpKyxepwIbpeokoMCYNG2eOuCZJOMz9L2RznwCxjSssA2aQFUOBWd1nI_XcOXnqNnf2Y7WjvLEU5ds30zOzGeraKKlt7HV1kqBP93D2zbmkcKuEma8PT3iPXNUkIZJVqzrjLpHqUI9spZTbYtTGYZXv6omXfAMwmTtrLVCmjA66QHbCBeSbEGLXpceLzdBmDWJD4z5x7PbKGB4PdrHNKwDuHIeBarWxTRXdCO07vf4_UEdGld4GnM34-pBYY0MY08pXFOSKrz8wPoInlKQeA2VyM1T8F7BF1WkABMqdVdfryryrIAes-VX1bQ2zXKATNXcG5OS3xnIL3z6fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fe642fca6.mp4?token=anBk_JdpKyxepwIbpeokoMCYNG2eOuCZJOMz9L2RznwCxjSssA2aQFUOBWd1nI_XcOXnqNnf2Y7WjvLEU5ds30zOzGeraKKlt7HV1kqBP93D2zbmkcKuEma8PT3iPXNUkIZJVqzrjLpHqUI9spZTbYtTGYZXv6omXfAMwmTtrLVCmjA66QHbCBeSbEGLXpceLzdBmDWJD4z5x7PbKGB4PdrHNKwDuHIeBarWxTRXdCO07vf4_UEdGld4GnM34-pBYY0MY08pXFOSKrz8wPoInlKQeA2VyM1T8F7BF1WkABMqdVdfryryrIAes-VX1bQ2zXKATNXcG5OS3xnIL3z6fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنگنده های عربستان سعودی مقر نیروهای خودی را بعد از اینکه به تصرف حوثی ها درآمد، در تعز یمن بمباران کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/72734" target="_blank">📅 18:47 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72733">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XXqT_Ypu5Hz4arHQ_EyC5g1gU2bZqEuesbqSg-Y8CVPyTSivhZyn50sQEKNN40eBwxu2L9Zna-MDrw3baA9kheLuoJL6kjDdbp7z_7bUh7Rlp_iugUHY6S2HO9uEsLVGj5hcwoMzLss3DWYsHZBV6auB6th1ambAOeXM46guAll4hNvgZhYnZ61VJQsjJKauVdBr1FWs-pAhLfLTZqOEucI8Dbwx3zCQl8lUCUrYlOsWc1K7F9kePYbhg_-RalFgX8VTA-7TMDSFz6-m_C2TM_uYTNvEYNs92ilcP6eP_8Fxqm7uGU8x5IVteM81f6vbOJ0ZYSsk_6DVdPmLtb4DVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایالات متحده با ارائه کمک‌های اطلاعاتی و پشتیبانی در تعیین اهداف، از عملیات تهاجمی تحت حمایت عربستان علیه حوثی‌ها پشتیبانی می‌کند، اما به‌طور مستقیم در نبرد مشارکت ندارد.
شاهزاده خالد بن سلمان، وزیر دفاع عربستان، از پیت هگسث، وزیر دفاع آمریکا، درخواست انجام حملات هوایی کرد؛ اما مقامات آمریکایی اعلام کردند که واشنگتن فعلاً قصد انجام «اقدام نظامی مستقیم» (عملیات کینتیک) را ندارد.
گزارش‌ها حاکی از آن است که فرماندهی مرکزی ایالات متحده (سنتکام) با انجام این حملات مخالف بوده و یمن را عاملی می‌داند که تمرکز آمریکا بر ایران را منحرف می‌کند.
@News_Hut
| Axios</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/72733" target="_blank">📅 18:29 · 12 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
