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
<img src="https://cdn5.telesco.pe/file/MmVNw1imC60hETuqpU757ZhlgTDiyd4iDODdNCq437amDmWYoU4nYDbrBjItlj9HWvXutnlx_HylkupMIsL0Cy3CFqsDQJK95s4VW9Qt36QbklsNp3-2x2D0JfGFjcCEI00jArdJe6sQ88QUx7YWF1hTeh7K9EmpiQSONaE-JJXVY8_n3lPubkuVXp7CbZwrfjR-aTSrClHUmldCMQmw0F80gHgbC6a934Vfv2nQyxxMtm-eclCunApE4ygWWJ04Njun1JpZMNIFYO4Y8TupHfjshe4qDO-Gf67aK3_fYrwC6Z32M8zlgQ5eZwwrzLkltHofrIzw-EnRtLnltfvD3Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 619K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-16 19:49:56</div>
<hr>

<div class="tg-post" id="msg-98814">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">پنالتیییییییییی برای ارژانتین</div>
<div class="tg-footer">👁️ 305 · <a href="https://t.me/Futball180TV/98814" target="_blank">📅 19:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98813">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">گل‌اول مصر به آرژانتین توسط یاسر ابراهیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/Futball180TV/98813" target="_blank">📅 19:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98812">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">وقتشه اوس مسی دست بکار بشه</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/Futball180TV/98812" target="_blank">📅 19:47 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98811">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">پشماممممممممم</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/Futball180TV/98811" target="_blank">📅 19:46 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98810">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">یاسررررررررررر</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/Futball180TV/98810" target="_blank">📅 19:46 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98809">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">مصرررررررذ ردددددد</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/Futball180TV/98809" target="_blank">📅 19:46 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98808">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">گاگلگلگلگلگلگلگل</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/Futball180TV/98808" target="_blank">📅 19:46 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98807">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">گل مصررر زد</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/Futball180TV/98807" target="_blank">📅 19:46 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98806">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">موقعیت خطرناک برای مسیبیی</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/Futball180TV/98806" target="_blank">📅 19:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98805">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">موقعیت خوب برای مصر که توپ دور شد</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/Futball180TV/98805" target="_blank">📅 19:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98804">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇦🇷
🇪🇬
بریم سراغ بازی حساس آرژانتین و مصر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/Futball180TV/98804" target="_blank">📅 19:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98803">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
🚨
🚨
😐
اظهارات سلیستی آماریا (نماینده پاراگوئه) که لحنی نژادپرستانه و بسیار زننده علیه کیلیان امباپه داشته است:  ‏این موجود وحشی حتی بلد نیست بنویسد. به جای شیر مادر، با آب نارگیل بزرگ شد، و باهوش‌ترین موجوداتی که شنیده، میمون‌ها بوده‌اند.  ‏باید به او انگشت…</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/Futball180TV/98803" target="_blank">📅 19:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98802">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sYYnE0dnlbPpKWUrPm5mQ3f-d9pvSBB52Tk37ycJaaRV738_xuZtrqR42yfhNWBTOeHvqbJ-qJcE4kpfju8ksmHojkULDbH4t90uFTr34oq4nmvTtUSXcMuOpZe0SmxICyKnD0Gx039TPWoOA3rNbZHNXFklKae2_nY4K5Itmk7tLX9iuA88lqrS-09Rea2YDR5d_pjgeE9_X8VEkuXBGDFwB67ne4tUnaV4_NxjOSzUDbscuiQ4vtiAS8t1wRZooZg0Yi9g2ARX7Nz1f7LYAExuLbzQXwS_iylRh1MoMfmSeD_K_-B_ZYp_kRAWYSzISiqp_kSLL5UmaXEPe2cZTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حال‌دلش امروز خیلی خوبه
🔥
🔥
🔥
🔥
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/Futball180TV/98802" target="_blank">📅 19:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98801">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CzOu-aXBU8tlLUproZGMNP7Fb_qPIMjEj-S-3t6zgDunsStDI4Zc9kX1FjGrvkZE9AFoGJ8qFbBCJ93I7Ai8-0nPtWuJmLQ7IRN2KtdeU1ENLYDR8CtPU1OYChl4diNPZi9Nj1E5aSsA1XgkGpJO076r3JXi0sL2Dv_gNvVYIT4u6cM-6YprsT2ECvDnglF4UHksIeUAI2KWeZvU-gctIdfunixLBC9c3updCkeKLC__BEvUHr6O01GdN19T9we9kMmrthrspcA1o9Ao7TOvvSZG9WaeRJZnDuFWSOW7SW0a1u0O9wtGWFGfFSw-7DXOfAeWWng_mmRPjnYETSZIgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
📊
بازیکنانی که بیشترین نقش را در گلزنی در جام جهانی از سال 2022 داشته‌اند:
19 – کیلیان امباپه.
🇫🇷
17 – اسطوره مسی.
🇦🇷
12 – هری کین.
🏴󠁧󠁢󠁥󠁮󠁧󠁿
8 – وینیسیوس جونیور.
🇧🇷
8 – عثمان دمبله.
🇫🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/Futball180TV/98801" target="_blank">📅 19:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98800">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XzAH5sZzwb-AsIZQ1xpUsq0qvzA84q7c9XwuZdiOmBn7xj-ASE0IfluJzUquLHwiiudgBwgd9lTHGndCKxULSYgS1PgRs3nhE9es2V1NYuQLpggNz71zXm6XKhmxrf3FzSAbRR1nApO6qHe4bxQjmOPlhkXqjZPI5cbfFLPYex5-ioqhR-14RqYZWFwQW0DBm2oOGsVlq5tSAoLxqCrX4B1P6xUAIWGbX4U8YLLDn1L0b6S3w4Eg6U34E5YrooZmiisQ3rh1tpMtdO-gvk61KPerGQRB0xiG5NIeJnZRA79vGWaZQQqowqTTTDE9sA06KCDh84iFis9iv58jH3Mp7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🔥
اسطوره شاداب و خندان اومده که بترکونه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/98800" target="_blank">📅 18:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98799">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d35458dc78.mp4?token=FKDGPo4x_ZyUOJYb0uiI2rP4aJv9_R5RpxoJABF_Hj3sJMb30ZFxOS16j8mscJuTqmx1LpUZ14bTdlV93lt1wchwBgq3UtmHLopnUChly8F2wyJCBDPevCrtmPpdWGD8tBeex5uaHUAOzr7iqWUpnx25N2BAJjohSBNJ0AXmTKN12K_jAG77E_-gX-VgOfWwT12KihAunWYOnEEKRR7utkz2Po_NZssgf6AJ5zBqrsE3fq1LrrejWa0PDKwKz3lcZL1M_4_US3H3vMp-VPDRI-a35MjJ6SlBPzar0rzqA4B8vLQ-VU1r1zRQs_Q3rCtG3M5UlZpLKmSJljduJ_30dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d35458dc78.mp4?token=FKDGPo4x_ZyUOJYb0uiI2rP4aJv9_R5RpxoJABF_Hj3sJMb30ZFxOS16j8mscJuTqmx1LpUZ14bTdlV93lt1wchwBgq3UtmHLopnUChly8F2wyJCBDPevCrtmPpdWGD8tBeex5uaHUAOzr7iqWUpnx25N2BAJjohSBNJ0AXmTKN12K_jAG77E_-gX-VgOfWwT12KihAunWYOnEEKRR7utkz2Po_NZssgf6AJ5zBqrsE3fq1LrrejWa0PDKwKz3lcZL1M_4_US3H3vMp-VPDRI-a35MjJ6SlBPzar0rzqA4B8vLQ-VU1r1zRQs_Q3rCtG3M5UlZpLKmSJljduJ_30dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🏆
🇳🇴
غول نروژی که رویای نیمار را به باد داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/98799" target="_blank">📅 18:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98798">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oCBe8CLUSsmLLRu2O9fPFNM1Mmd4r5FG3Wd1x6AVwaeLLGzXHWKQaDsOUnOEZe8vsiiFAMPHKF9CBwtdBrD3KAtKvftMmpfvAP4I4elHs4BtScngS_IFhhUjXeprZCVGfQkMyC4LCVxRd-LJJkZYS-YSTEtV04BpxKjTK6KwThNb4mon3be2En4cujlFGxMwQ-UvQV5xE-DdmjLXOzZvwA7RvIpFDvByIaf_r7Ak8cEasB3iLYZJHUAC5q7CjMdIFJpGq_-rb3w2Rifq-WRfVHRx0f3a0gQjF48OY-tfFVAWeLDHTBybf14_z7vS8RYTTpIJfP9_6Cs_NmjXRC6_Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#
فورییییییی
از رادیو مونته کارلو:
🔻
بسیاری از بازیکنای تیم ملی نروژ در آستانه دیدار حساس مقابل انگلیس بیمار شدن و سرفه میکنن.
🔻
یورگن استرند تب داشت و مارکوس پیدرسن بازی مقابل برزیل رو به دلیل بیماری از دست داده بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/98798" target="_blank">📅 18:13 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98797">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UkudBjj49ZjE_BHuKeK_k9et4c8LhViX3zh7AtoIAw6XN5iyaFcoRVHXcrKecdxj9r_Wu2RTdwHYB43gdN4DW57cOIiKbntqxc1uDSmB0SF2tCRjxmSbBLLJvl0om6eJ1rJvWCck6aUqaKitZnlev2v2ibCo_cL-mIW3PTgEzcL0Hxs7DwD_SzaRnAnbgsRR8RTgn__LO5eutw-kyK9iYS5goocV4JMoCqeFi8LP2pc-u7XYC4LYWs3r5zMA3PbjqNfiwqQPtSlS6S255it3eIJs0Mq37cqQB1o95L5bLB2-sUGP-NERwSeF_j11d9wPF5nTy9lxFpWRjcOeRBz17w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترکیب اصلی تیم آرژانتین برای بازی با مصر:
🇦🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/98797" target="_blank">📅 18:10 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98796">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc3745a4f5.mp4?token=KmL4e0T1B3dY5UQSD_n9Ldm2X06bPYUgw-feDIilMaMqA3IuBnjY0dPVGIl3og57LZH8IQu79DC3XQnReCP_QeoIIXLABPJEk1-XLfJ0XugoTmttQJ_K3nT3qX3Dd4PgrEGoqUJEyUu6ZtT7ziVIrkcvOKL9CihwAIZpeuVc7kFL16s_tCP4hpI4nxCURHNKzxM65tw-oyp8fsjsAM637MGGPNthYAu2A1NYApDHQfWsWKnI0Nz-MhZC5HZGP-2CxVKZpcmZMu_kuAyQvRmLF0axR29no_nOSG0Z5Cxx2lQu6EtcqRHJSV2j1vjV0ksT40DFW53W8v8h3IQrstje4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc3745a4f5.mp4?token=KmL4e0T1B3dY5UQSD_n9Ldm2X06bPYUgw-feDIilMaMqA3IuBnjY0dPVGIl3og57LZH8IQu79DC3XQnReCP_QeoIIXLABPJEk1-XLfJ0XugoTmttQJ_K3nT3qX3Dd4PgrEGoqUJEyUu6ZtT7ziVIrkcvOKL9CihwAIZpeuVc7kFL16s_tCP4hpI4nxCURHNKzxM65tw-oyp8fsjsAM637MGGPNthYAu2A1NYApDHQfWsWKnI0Nz-MhZC5HZGP-2CxVKZpcmZMu_kuAyQvRmLF0axR29no_nOSG0Z5Cxx2lQu6EtcqRHJSV2j1vjV0ksT40DFW53W8v8h3IQrstje4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
شادی‌هواداران اسپانیا بعد صعود به ¼نهایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/98796" target="_blank">📅 18:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98795">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fbasa_hTdCf0YIebvwYSgWzlpi5pI74ee2ZlFpS0oUd_-QjkrJPi5Y72KAhKc6Tc_gw9rYPNGKjItxMm2X8czVshbq6HA9lJd9KsGohfNfyRw38RQA7O5CYv_XdidRtch5tNa0aAD2yks65TJ-MP95yl7eJcmgw5vPAxgT7f0QMyhRuGjfRGSeNBbPIOpnPEuJ4IcGm_-g97swA5eVtZGE_kiw04-IgXT4mNlFlbw7-uQcAMOQlQBGP35XvsfITwy0LeLBv2-Eiv_lcmIDv7dpo0p0-hT8U4QMqVQjcR9aIivEKCCJdNPgUE_f69vgRXLH7A6dPOqDvvPxQHU3c9iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
تاتنهام تا اینجا نقل و انتقالات 267 میلیون یورو هزینه کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/98795" target="_blank">📅 17:51 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98794">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hPT82nB6tbMhAIcP1JVd5Aw3-k9N4nu3NEo-jBrHoa8FYEIQgRA5srSEu67mWtpQlt1nNANIOsWStlb4OwJkDvrstxNDERgRQUX1pZkVVW0xKr3NofvJ2vSgXtGFOEiPkMOeU3SYXKWeqBA_c0p_74TcQD3QpopT3iUzVvLNAfleKDa7ra11hk694zqP1liGJH1oLOblnVhg0gEf0xL-QzhkMaOHHl_Mf9k9zOLMIWO-p1TkPZISTgLQxnFPaHYQkDNbh7c8o1MKTTqNA2y3-FfpSqW6GdomU3Z3h7P4nLlVdWmSDWTQtW-ObuEmeBxGRpe_8-2VXavVSIp0NVokxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
🚀
🚀
پیش‌بینی خودت رو ثبت کن!
🇪🇬
مصر
🆚
🇦🇷
آرژانتین
🎁
۵۰۰ دلار جایزه
بین تمام کاربرانی که نتیجه مسابقه را به‌درستی پیش‌بینی کنند، مطابق قوانین سایت تقسیم خواهد شد.
⏳
فرصت شرکت فقط تا قبل از شروع مسابقه.
👇
انتخاب شما کدام است؟
🇪🇬
مصر یا
🇦🇷
آرژانتین؟
🎁
جایزه به‌صورت فری‌بت و مطابق قوانین سایت پرداخت می‌شود
https://t.me/betegram_bot?start=p3_r4EF37DCE</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/98794" target="_blank">📅 17:51 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98793">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LAuZJQ6K53PEQurLn1-uCXbPwxxHc7-UyzSa6nuOunbEOyY6hVRggEk6AynvXCkYu8sG9pQwUaEMGX9bNE0rE6bTnyYAqFnhuGtMbAlyoaXeNnDf7I8sxxYJukef8Cki0abmMPMEK7BPqI9_WuFbyYIJvRLKrZa-L_c8NE2LM54DFANj-84LQeE0kSJH6ixpE16ZrO8FQbNT0uFz29fAnap8egWPhc82By2rNjUjwszKlKFQUlJO0OfuNYEjKRIUIPlLUuMO1xX3zoz3XYIvwGrVbZQ_T0DpWEK1D_-aGevSXnSA7TDYIH0lAql1X4qCw0lC-p1fKAjaTUIb5ypa-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترکیب اصلی تیم آرژانتین برای بازی با مصر:
🇦🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/98793" target="_blank">📅 17:45 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98792">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cylJvlIFfcFA2Nz28WDqcwEDMhYBXg93JaOmMPGzowfttin2UJu_OKgebMJ-jotYI2cyWOLvFVcZFQkSG2NcZixOHRua3F5dJrRJ5GgNBfDILxTiyUZ0aS4RV2v9YJL7dtN7-k3f55DGh3BpT1nLSCaGis6mo35go-4T-sysNJZPSbBTVqicmsAqvxzfm8mC8xyHAr7tILKk2ir29skf8blFa7mmGqTmPu_2kNzIrRFd_l2ox_zrNt81itOEHwVtQhHdGFqJF3cl0vYTSSmM91Cv-kMzc4WjisQpZcB5UncJkijjJgnuktnxHdmq-S8z1_3A38cmt0jwpCxiYh7OeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👀
|
تاکنون، تمام تیم‌هایی که در مرحله یک‌هشتم نهایی جام جهانی 2026 پیروز شده‌اند، تیم‌هایی بوده‌اند که میانگین قد بازیکنانشان بیشتر از رقبایشان بوده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/98792" target="_blank">📅 17:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98790">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">▶️
🇦🇷
🇪🇬
تیزر جذاب بازی امشب آرژانتین و مصر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/98790" target="_blank">📅 17:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98789">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZYQ1K-tTpbS6aVbZ1D6aO_iUE_hOQf1yw3KKqZjjToFPbAveUvUtIQS3oRVz684qDAMM9Ya_i9jicxqQG1AyiKAwTCDVf7_qkzPzoPerzFYi6_hQlN8GZEPm9jOxzcbOPL_X-9hpD0b6qVMuMuMerUmdvSnLhv0vqLt7czAE182dPXCHY-TiDP7GbC1FfZeE8xDyakOPJVrosRbUtKGY9OnqqXRy9BrxK0RffSdhMMD3EkmJq7GtmnEMQjLQX6ONyCUAPyEo1SpgUP4wHzEY4FDkiD3hYkLbfHtK7DskXWQh1FWz8AVMCXyYvoF0kuJLtC5JnY901ytu8Frur59AKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👍
🏆
قضاوت‌های علیرضا فغانی در تاریخ جام‌جهانی؛ احتمالا حداقل یک‌بازی دیگه به اسطوره داوری فوتبال جهان میرسه که امیدواریم فینال باشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/98789" target="_blank">📅 17:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98788">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf4ebc2564.mp4?token=sBFgJ6WzAO_nUM9-e99ViZJ6h_eWgAmQo92Oci2G1T6rnsPvKe6RCgpkrUReo_wkfspmouHMRvcZiSLg3fo8eCiHt6n0rg5e64XMFjK2HRl3Xcw11DYroDu3dpGAd_Psa9VQjoQocSN5c3kF_OXNJT8FS5LVG_MAvFOovdThQ6V-wA1YDsW8YfbtQdBzfqoeRCvupxSb3SinlayPAUFX8_qzT-oZmBcE4v2d1sI-6GBtMHzTIzL5J35c-auSqn-e0k7v864cd_jNtv_uttJmL_WE25PqxV2sktz1bXP9ck8yA5_QOWU8zxsCNN-FAJAt4H9pAlLFczwzwmI8a0yA5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf4ebc2564.mp4?token=sBFgJ6WzAO_nUM9-e99ViZJ6h_eWgAmQo92Oci2G1T6rnsPvKe6RCgpkrUReo_wkfspmouHMRvcZiSLg3fo8eCiHt6n0rg5e64XMFjK2HRl3Xcw11DYroDu3dpGAd_Psa9VQjoQocSN5c3kF_OXNJT8FS5LVG_MAvFOovdThQ6V-wA1YDsW8YfbtQdBzfqoeRCvupxSb3SinlayPAUFX8_qzT-oZmBcE4v2d1sI-6GBtMHzTIzL5J35c-auSqn-e0k7v864cd_jNtv_uttJmL_WE25PqxV2sktz1bXP9ck8yA5_QOWU8zxsCNN-FAJAt4H9pAlLFczwzwmI8a0yA5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
تفریحات داداش لامین‌یامال در آمریکا؛ بیچاره بلد نیست گلف بازی کنه
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/98788" target="_blank">📅 16:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98787">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b1325b4b8.mp4?token=NlbFC3xyUoE18CzWewqTYFPorxbvNhw7b_-NwVtlJ6FyXs5p4HdYC9aovYgOIine6oeK_QGOyn5vnGHBkTmFMOn_EA62NBtpYIz9YhJa4U53sVgqEHMMm6Hz42vv0EjCyUzzuPXe4xx6fzuQeUYeWOGgrzXtVAGutmmdYBMq8yP3lVma1ZaDemDrgN40lvTx1Ge64honuPUKy03QvlkbIn8dHqLsWk1HL3KASIUm7hc4y_r1yMl5vcYJkZO-ZHyHSQmk2mAjAkMIfJgoLWmwn-qDDIXe-PnNjCm-diBGxpNGM7dMzwOqCJmz-qbXQGvEdF6eEAR7-EKMwIyv7fdDVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b1325b4b8.mp4?token=NlbFC3xyUoE18CzWewqTYFPorxbvNhw7b_-NwVtlJ6FyXs5p4HdYC9aovYgOIine6oeK_QGOyn5vnGHBkTmFMOn_EA62NBtpYIz9YhJa4U53sVgqEHMMm6Hz42vv0EjCyUzzuPXe4xx6fzuQeUYeWOGgrzXtVAGutmmdYBMq8yP3lVma1ZaDemDrgN40lvTx1Ge64honuPUKy03QvlkbIn8dHqLsWk1HL3KASIUm7hc4y_r1yMl5vcYJkZO-ZHyHSQmk2mAjAkMIfJgoLWmwn-qDDIXe-PnNjCm-diBGxpNGM7dMzwOqCJmz-qbXQGvEdF6eEAR7-EKMwIyv7fdDVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇵🇹
CR7
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/98787" target="_blank">📅 16:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98786">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aTblcPuw-wEpm9y5gL2SebBpAojkBVna8APnct3MT_ynFvNOm4qYEWkuw97gWg_lsA-af6G3C7lEe7Wwo8hUGxfamSeXIBGFnzJb_5REgHn5KRH9r48ZomfP6ucPRI-PuVab23wD_pzceMH_TUxxzyZ2fM6zIiXnJi9Qte36MpgPNhUcmQrv06-0hxEUhYUO4VbgOIFZfXYzTgqTJLTKKjSAIQpnMJ0pTwIXtfyd_F0hP8IB-nzhK4rQr5aCnkH5YYLEh56L0xwE6rlX3DAVzMKIAHCPrX7Kb18XRxWrS7RXHNKAwrNZZ6fseEZk15O5NBDeaHhgTTdojYdU6Dq0Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
اگر لیونل مسی به مصر گلزنی کند، دومین بازیکن آرژانتینی تاریخ خواهد شد که در یک جام جهانی 8 گل به ثمر رسانده و با رکورد 8 گل گیرمو استابیله در جام جهانی 1930 برابری می کند.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/98786" target="_blank">📅 16:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98785">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6074b72f72.mp4?token=CIhT09xAJlhZ4u_F47bXZM9dpe7o8gQ7ptXXlNS2xtZ6UI5OMRmwc7UTYvzhuMStkM2wNOo81j8TxidYMFJmcCXlzgJKhBhUT73aOqw9XsDX_8Ztc38x7JHfu60Es91tRYJRUbswgJaREvDfBAqKgXvvNMV-Np6eW3vmNYXmZilYv4xzSYOVPJR7O8Dc-c-xM_5M-MpeB39vryOecjmGgOd5MFUzc148INj5K1qXqJ1nkSqSGCb6AgAhF6wDss9r7rFqDwOdy76NW-PjZBP3ZDxQrjFbYIoVhFBhqZeXGn6hNSzb8qW2Tp1OFeKuFBklRvK84GCzzYiqAgYzyHqTvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6074b72f72.mp4?token=CIhT09xAJlhZ4u_F47bXZM9dpe7o8gQ7ptXXlNS2xtZ6UI5OMRmwc7UTYvzhuMStkM2wNOo81j8TxidYMFJmcCXlzgJKhBhUT73aOqw9XsDX_8Ztc38x7JHfu60Es91tRYJRUbswgJaREvDfBAqKgXvvNMV-Np6eW3vmNYXmZilYv4xzSYOVPJR7O8Dc-c-xM_5M-MpeB39vryOecjmGgOd5MFUzc148INj5K1qXqJ1nkSqSGCb6AgAhF6wDss9r7rFqDwOdy76NW-PjZBP3ZDxQrjFbYIoVhFBhqZeXGn6hNSzb8qW2Tp1OFeKuFBklRvK84GCzzYiqAgYzyHqTvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
تو شادی بعد بازی انگلیس، جان‌استونز خودشو به مصدومیت میزنه که توماس توخل نزدیک بود سکته کنه
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/98785" target="_blank">📅 16:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98784">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RcyAFGNh2v19pSoLFQzdrba4o-tpQCUeTteV1e8_y1k7zRhNU2_sUkvndItjjF3JG8WA5_QPW0lZYX-zdI0yKOtMWDfrhcYqKnyDWHwxX4j_XcViPZMfuzahzFUIvxh_lWAxOCF1dLVlxJJpLrtPSpowk6DtFLL7DTeIXeR9__lcrp1xSEa4od7bIKAL7SZmdc6ikmBmTMPwgG_sLt5xmzPcrDVAtv2IEj4EQvUDAbdC9mUGhjElsGArA12qQPK_qNHvQKU1TjnA64nN8O5jZjGhrkbv3lnl7DSqdTQCoBZdcb51X8zQayYBPYHO4-CjW_-1y9e0zVG4VrAJP1a6wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کورتوا :
آمریکایی هارو به خاطر بی احترامی های چند روز گذشته مجازات کردیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/98784" target="_blank">📅 15:51 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98783">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/98783" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/98783" target="_blank">📅 15:51 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98782">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/98782" target="_blank">📅 15:51 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98781">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b9aaabfe4.mp4?token=jfNAvmYMbAYIO5YBIsMW407rWIAhoFPA0vTi7HEOorGQBMKEmdo-mIt2Xo-H20XMO7tWWr2Gsn2ag7u95l4-rWLA48xXFL-Ws3ZSskjHo_YLhkBy0OkSX0tyVC-epVCPrYdTjL01KX2QhjMy2pbJsJ-9JeRqiwRDp5N3pVhyyu7vSLwOAgtUgPh8zwq-iylX5UWGtoSrF-34RCnDm1K34PLaDSw8S56eIqduD4znLW5acBaldMqRF0r-17lZbm3djOSyrUgVxGSo2cExpncO3CmoxIn74PSklbYExxc6kglJ2dK3IloUNI2oZNRp5BDHEkMQxMxSAl2kkA8vdUBMmzp_CH0L4wmYkPQ9D_Pd7e4rjcf-JTpRu2eKz8i6jSe9u4yd4zzIK23imkEkCrVNxYY4_o15SckoSyGOj8Pwo9HmNUUrlayK-WevxIQhCVZN3Wjld1Q7pG-jK4gm6fwho2hcecS9LZ8ITcfoN8liaVZKguWzw3Bopz0D7v4qdr4Wrg5pOeNfBW7ShFPebjLgr6mVwK5D9aQd1D3pvKEgXTruVWe8K2ZTpGeMzLl9GZJpgRdMVo22gMEysPYKZ8eMgEtAT4mTemPF9nk2ou-g2OyljJ84RYnDjg1C-XTPbUNBIVI07gFDLy97_y3i934RMKf0GpyrkgC8lHAIYvmXX-0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b9aaabfe4.mp4?token=jfNAvmYMbAYIO5YBIsMW407rWIAhoFPA0vTi7HEOorGQBMKEmdo-mIt2Xo-H20XMO7tWWr2Gsn2ag7u95l4-rWLA48xXFL-Ws3ZSskjHo_YLhkBy0OkSX0tyVC-epVCPrYdTjL01KX2QhjMy2pbJsJ-9JeRqiwRDp5N3pVhyyu7vSLwOAgtUgPh8zwq-iylX5UWGtoSrF-34RCnDm1K34PLaDSw8S56eIqduD4znLW5acBaldMqRF0r-17lZbm3djOSyrUgVxGSo2cExpncO3CmoxIn74PSklbYExxc6kglJ2dK3IloUNI2oZNRp5BDHEkMQxMxSAl2kkA8vdUBMmzp_CH0L4wmYkPQ9D_Pd7e4rjcf-JTpRu2eKz8i6jSe9u4yd4zzIK23imkEkCrVNxYY4_o15SckoSyGOj8Pwo9HmNUUrlayK-WevxIQhCVZN3Wjld1Q7pG-jK4gm6fwho2hcecS9LZ8ITcfoN8liaVZKguWzw3Bopz0D7v4qdr4Wrg5pOeNfBW7ShFPebjLgr6mVwK5D9aQd1D3pvKEgXTruVWe8K2ZTpGeMzLl9GZJpgRdMVo22gMEysPYKZ8eMgEtAT4mTemPF9nk2ou-g2OyljJ84RYnDjg1C-XTPbUNBIVI07gFDLy97_y3i934RMKf0GpyrkgC8lHAIYvmXX-0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇲🇽
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هایلایتی کوتاه از عملکرد درخشان و قاطع علیرضا فغانی در بازی انگلیس و مکزیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/98781" target="_blank">📅 15:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98780">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KHzrnY3hVnwWax28BJiSECSoA8ieN7qGdVGStNwTh3RdkrqsW4XI_Mzf5gOtYHjNCZCRXYB1wU71BuuG8WEN9T42CxMwnzVp_gv-KlysyOJGO2jdvg0oa3EQLxpPyXJH0tgYrIvk7jJfNKQ-9mlLCxVLCt6cKDhrzGSFwh1yoYAJxI683EqomycNN4cRzRSEwg-fkfxlNlawoeFAjsBHmUnKMmNFRo8ndiUj6Tyew4_JMc-lB0evdNgCMBNDyN9OalkkTawEtp8nqWpnguZwStELvF4-VT47QOtEddmd6lO2JBPVBK88FsPGxCqM2-7LhT7nbZ1WjcblcCjYyBL_Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پوریا پورعلی، پوریا شهر‌آبادی، مجید عیدی و علیرضا علیزاده چهار بازیکن گل‌گهر سیرجان هستند که اگر اتفاق خاصی رخ ندهد بزودی با پرسپولیس قرارداد امضا خواهند کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/98780" target="_blank">📅 15:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98779">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20451491aa.mp4?token=Ut7AwcBbAEWr9qFqiTZWbk3Xu4q-XTbnBXCnK3xS8mfv_Atzc6fJZFv3w2xo7NWWVJhGkpBiwe4qjTD94BGseOn4-7nm2Fl3e_sA0O5LF8BVwhNmZtXkQuRG2gQQVoIjtQYWE4a7uVyK7HXr1TJyJJ2BGN4E80TrU2nztuzpC-0NnLEj27wInLkFwu4n8rH14jWiS9f3yJWpfTP3vh8xmLhxBEU32pbnd1ACjVjnjH9CwjifK4PoNb1FuklkVZiYw6kgvOPwh7V-Ki9lcV_f7pxdbvmF0vPcxdGLm7DbkBgI0SxjvnOxR-1m8GqCxgsN_tjyMmpntAQEF1EN60h-uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20451491aa.mp4?token=Ut7AwcBbAEWr9qFqiTZWbk3Xu4q-XTbnBXCnK3xS8mfv_Atzc6fJZFv3w2xo7NWWVJhGkpBiwe4qjTD94BGseOn4-7nm2Fl3e_sA0O5LF8BVwhNmZtXkQuRG2gQQVoIjtQYWE4a7uVyK7HXr1TJyJJ2BGN4E80TrU2nztuzpC-0NnLEj27wInLkFwu4n8rH14jWiS9f3yJWpfTP3vh8xmLhxBEU32pbnd1ACjVjnjH9CwjifK4PoNb1FuklkVZiYw6kgvOPwh7V-Ki9lcV_f7pxdbvmF0vPcxdGLm7DbkBgI0SxjvnOxR-1m8GqCxgsN_tjyMmpntAQEF1EN60h-uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
صحبت‌های چندی‌پیش علیرضا فغانی درباره ظلم برخی از افراد فدراسیون نسبت به وی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/98779" target="_blank">📅 15:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98778">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd25c97626.mp4?token=Oy6j1fZo0VfkX4mmiIlMOf4AXHyjimNBD4-UqqiNN3fP90hxOAqNI31uAqdasTbM48LggW32kkjVmCHJy_02WMa-fl74DaGQkoXJoeEGWF9RNg_xX7wZ9PCSw7LGyF48Z6bfdgp6aNeIavJhagDDSLmtNKvboZBeu1LrtfPocJQ1Fm0MDlwKEkIT4FM7acm0oJ-YuoY4FoavHiK9kNhMSKiHFYhZT_QT8M8ATaDRfKWmdwWLoN2kcUWQw3wuEKJ14itJX-k9gcS_7q1l-GDwgfKcZ4-26SgUjCyXDujpFlBHkTmPmugHDBd0L-fQhX5YlLhyT0wSLGV7CHtc6nsHbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd25c97626.mp4?token=Oy6j1fZo0VfkX4mmiIlMOf4AXHyjimNBD4-UqqiNN3fP90hxOAqNI31uAqdasTbM48LggW32kkjVmCHJy_02WMa-fl74DaGQkoXJoeEGWF9RNg_xX7wZ9PCSw7LGyF48Z6bfdgp6aNeIavJhagDDSLmtNKvboZBeu1LrtfPocJQ1Fm0MDlwKEkIT4FM7acm0oJ-YuoY4FoavHiK9kNhMSKiHFYhZT_QT8M8ATaDRfKWmdwWLoN2kcUWQw3wuEKJ14itJX-k9gcS_7q1l-GDwgfKcZ4-26SgUjCyXDujpFlBHkTmPmugHDBd0L-fQhX5YlLhyT0wSLGV7CHtc6nsHbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚬
لب‌خوانی نیمار در صحنه پنالتی بازی نروژ؛ حتی تو لحظه‌بگایی دست از کری‌خونی برنمیداره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/98778" target="_blank">📅 15:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98777">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09d155e75a.mp4?token=TBESBV10AT_DL3RykQThCyCq5W2UVB84QMR7iFwwhdTIFqxfHOAYAbNohJ2YTk4nG5GSvhlFrAkrE2iUx_YYz4fPZVLZK4zGL1dGBQiqL6x-9hbbpuEbIVzcs0EIr3gIHDy4h3T_KKJmRisFKg99yd7-VRcbaru_dooyvpo6qkfak7dfnAlwdyylri-5MOByRuoYIkAG1XfJZ98SrDO876tN4yiMRnrAsKIu3orTKRxxLeH7G4tXVHHQVKF0Z0vah1YJ5V-p7xF46-wj84gN9uAk2nzg40B8WoV4CXi6w7-FsU5HdCBZXFBVpmI--NEbEApNvS4pT_rF6guzi-BHZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09d155e75a.mp4?token=TBESBV10AT_DL3RykQThCyCq5W2UVB84QMR7iFwwhdTIFqxfHOAYAbNohJ2YTk4nG5GSvhlFrAkrE2iUx_YYz4fPZVLZK4zGL1dGBQiqL6x-9hbbpuEbIVzcs0EIr3gIHDy4h3T_KKJmRisFKg99yd7-VRcbaru_dooyvpo6qkfak7dfnAlwdyylri-5MOByRuoYIkAG1XfJZ98SrDO876tN4yiMRnrAsKIu3orTKRxxLeH7G4tXVHHQVKF0Z0vah1YJ5V-p7xF46-wj84gN9uAk2nzg40B8WoV4CXi6w7-FsU5HdCBZXFBVpmI--NEbEApNvS4pT_rF6guzi-BHZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
رویای‌علیرضا فغانی: قضاوت فینال جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/98777" target="_blank">📅 14:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98776">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca02eb2095.mp4?token=pe8fAv_7LUXq1QQ1BLMSXbAflcG1R_QrKdDhmdsJopXosTEWVJkB8Hx1LuwfsKeDjazeCu-aQ0dTO3CDvRjernwzXuy0Zz4Mznjbq0fWyKcJBRLUBXzE04l0EYGoT42_9q_n61zWjIQVGdGcmdYj7t5hHA5Itco9qDGAA7ZCtGgfDZhUIVMUk4riXmldrxIptrm07ZFyFX1hWqT90sJNVKYDOh3jH94HDrl-qIkTUmZver6B8XhgsGjEOsA5HDMzXuKVOXNZ30vqKgzgtlVN_auKrGPNw9_DhrBMEljpJQdtwawabTHxuM8yISaxrrzYTJeKgtkG7ZJz7h3JTuBCFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca02eb2095.mp4?token=pe8fAv_7LUXq1QQ1BLMSXbAflcG1R_QrKdDhmdsJopXosTEWVJkB8Hx1LuwfsKeDjazeCu-aQ0dTO3CDvRjernwzXuy0Zz4Mznjbq0fWyKcJBRLUBXzE04l0EYGoT42_9q_n61zWjIQVGdGcmdYj7t5hHA5Itco9qDGAA7ZCtGgfDZhUIVMUk4riXmldrxIptrm07ZFyFX1hWqT90sJNVKYDOh3jH94HDrl-qIkTUmZver6B8XhgsGjEOsA5HDMzXuKVOXNZ30vqKgzgtlVN_auKrGPNw9_DhrBMEljpJQdtwawabTHxuM8yISaxrrzYTJeKgtkG7ZJz7h3JTuBCFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🇪🇬
آماده‌سازی ورزشگاه بازی مصر و آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/98776" target="_blank">📅 14:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98773">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E_kYQq4Ho84F-SnVIIL73uwwpdRTXu3bmqOciu9sveLft2cKrE-jHmZMQZRK9NRfdrNtHUDwOmuxygyZnZvKGv3py86MKz4nyCcBXWidTRrPxyLctp3iM-BRfZf71u_AE5iju18mTMpTnbRAoAVy7a0QxSqIepShDEroSD4jfCNjn_iCm4FcIKB1yplaHCmOnl0_M4uQ2pHTM1qd_98ifefax92jk41RsQSxPfAqeC8H51nenorSurg1QFROKwDyQYf-NEelrbtPI71nypgtigtevVkYt9IQihxce8J0lENwxR0BO2M9jLxBkeocC_iUjZTaSosqdSuMmUjthCi8VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MXwdO4ynZI2Qpn-JZcmD2wPSYopTKxQKFAtrHgv9h_w3Po15dM_F66n4jrhjjzng4Iv2hrBgEgGTmU9XySEJpcgJB-0iqKpzHcmISjjjbphfJMM4pxsr_pQXeA8Jbw_uRYstfg3euLSpLCGSx9Hlrve8l8uP7nO1Q4IRuejpYVahY9C6X6Lef8ziSfVdh-2qsuzFetiKBUBc41AONuk1-c4dLHif_ikgbKruaJ2Csw8n8tvO0oGX0VTHK6b7ff2coypq_YPrU10UwJmllTetYPLql3hNbw3xaZuBXYhq_-Pr4ExlrXx3d477DkKAus_OV_2hK4GM-bzSHMPmUeDuIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/utl_IU7n7F5r79p1VcouvflAzfDkelz62RbDzlq-O-IwX7vntweCt-JsRAAgVSopi_LO7FVCGv66Fn3Vs_1ucxN2rXsgApk8tPyaxDnwTPXoQElFPXyjrTrpP6Ak51eB8g4QSAe3U4qm6qjiTimB49Xcru72QMDxy2Rcv8gEQZpua439EE3Vv9S3rzuBGy8nTG7geKt1yatOIG9lBy_scplX-vHue7ge3oMPW67Ui-D2LXKyDtHO1MGyP-jumQ81L8LUb4-p4PCFsSGSBxAIyj8bDDDgEGeNlxVjy7QndXwcCEXrCaJFkw3PGpURrDQ2fg6fHCByhi5pXrKxISh-mg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
💥
دوس‌دختر ژائو نوس در بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/98773" target="_blank">📅 14:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98772">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/jtc78GXfYb_IAGwc7N8JDa9UZOa-5mEcpQOipixSr37CRNzeG3Zj1MybtKBCsw5YXpjTxUAHLptyA1q1nWR3PpgExW30u0pBlavnNLFS2nDNmBxacMAHoFIg9uRn7fw0uWVJGeXCnjMPtUoyNFpCwRIYpZB1034O-gwgf1RGOfUnVf869Dq56EdA3rGVgHHd-zV5vRmovL-biUC18uglmoKQHsb7GlLJZeohQygFO0jPV5lQmXrD4H04BHH5UZfLoTX4nyb-W1jpSbvCWViCFiOtiO9lGQuEWv1vD_Vc6TIOFGq-_Cu-S-OomHjsNFoi1uNtCdYiUjnNKpQdmubWbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حق
🫠
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/98772" target="_blank">📅 14:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98771">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc9e2f1596.mp4?token=H7C7d7bouV94cjyNuYIR_MyxRSfmvigI5LVqHZ0t_8QRcwg5eR8xy57CIjDeRVOAec5viMr3B20WDI2cshGuWZNHLraionF5qKt9KXM9T2DhCJ-LdkRndsgJIUo62rwUjHQ_aH1HnPN9XhO3Or2wm0mlaaBggVmJeszpy8L-n8f8PcB_Z7J7LVhcECgI80USD3oNxkiECE7jmPWSCENmvk7GzNl5dZcfaHpKiOBxqxlTIYdmqNm9ZxyZQaVMN_w850Za9rGvsAJFxYImzXzmU2ogk_tnSLiniAEDfT2gUEnSzqLYgr45oT4O3SrseSaBR5TN9RrERrxGY0IAwn8MyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc9e2f1596.mp4?token=H7C7d7bouV94cjyNuYIR_MyxRSfmvigI5LVqHZ0t_8QRcwg5eR8xy57CIjDeRVOAec5viMr3B20WDI2cshGuWZNHLraionF5qKt9KXM9T2DhCJ-LdkRndsgJIUo62rwUjHQ_aH1HnPN9XhO3Or2wm0mlaaBggVmJeszpy8L-n8f8PcB_Z7J7LVhcECgI80USD3oNxkiECE7jmPWSCENmvk7GzNl5dZcfaHpKiOBxqxlTIYdmqNm9ZxyZQaVMN_w850Za9rGvsAJFxYImzXzmU2ogk_tnSLiniAEDfT2gUEnSzqLYgr45oT4O3SrseSaBR5TN9RrERrxGY0IAwn8MyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
🤣
🤣
🤣
💸
💸
وضعیت دیشب اهل دلا:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/98771" target="_blank">📅 14:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98770">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r2lkJParYxFRaDzCk3yXTlm_l9GHPFv-9HWUtgIQBqdeDAiKkeAp2ynA5gM360El43mKdd_Iumaj75p1dVuNPdk5KxQgBf2EYmgGUUUszCz2QFCzwPpS5jNpAdHm3ZLFme0g2WmniPJN_vpHgAyxehrAPJHorYSKpUa4MxxJwIkiAhS5tv7zCMx3ef9bQvILLMbKwB0ZH6Qq7Z65AeAlKR_xJtCUBOxfdTt04qCcEUhlw_0v7kTbw3al-hnrnUTfeON1Qllfr-fLfx_WoC4_kBdqFzCGxXctuwkrQ3jTCzGBGRHpp7PhiaYNXGbDw7otL7mDxwu2oio1oN5TNIhs0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
📊
آمار لیونل‌مسی، در بازی‌های مرحله حذفی رقابت‌های جام جهانی:
• 13 مسابقه.
• 6 گل.
⚽️
• 6 پاس گل.
🔴
• 12 مشارکت.
🔥
• بیشترین مشارکت در گلزنی در تاریخ بازی‌های حذفی جام جهانی.
🇦🇷
🐐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/98770" target="_blank">📅 13:47 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98769">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f_8IqI8HA-dJIqmhLqpN3wv5WD4FmwVQBGi73aVqbSEoBL7GWsmjE37IR0nfcB_Pe_XhZrvuAm0-5pDCUSdbBxdZdbVfljNO9o5Gzhf4V9HN5y6DxkMvrspcRPrvCpUZeH2PwagLQKNs8EfO1b1JSWHOfvoqcE6IVokzxL7gM4JsvqjxdzShyO5weFrbkmz8sDQXuecLxuuWNlvxIubALV6uXHDXHrVMHkSchLGxmZANbOMvrMXy_88XLFM5jwi2J_GmydWJkJ3wq2jZBCspQFKYAtRr62uZIb3ygbaXcDfL-2pSxjJtWY4BvrZOfgtQoejAtVVJph-QyCBVe1rtQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری
؛ باشگاه بارسلونا در آستانه تکمیل قرارداد ژائو کانسلو با پرداخت ۱۰ میلیون یورو به تیم فوتبال الهلال عربستان قرار دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/98769" target="_blank">📅 13:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98768">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3126b51523.mp4?token=eKWOkYKU6ypgxg1ghJgQcoND9fOqWln8sIMHS9zq1F4igAhjm22R8t08KoKyalbcr6Y-rh0qT-jyz4ztj3BULIw_-9wxCnlujSvhvHxRBAY9PTlv8JVphg-kyZT2Hc9mWm4Jv9ZMN52RxI7mo90ya5yIuQdKIUovTF7EpiXnVIsomSHaglzrUXJGwKzYs1_fmA4EVr_ecU7_kLYEu_mLDDsqdqv5IJKrPQR3KpgWBP653hLHsok4e_Ih4GMoellkfGoo3VtozuCrs3-7YtbamaikS7YcyYNYIok86DPdvH3zGXo1yEEtYlnNvtX1WT-SO0Zi_nPIRdiNefVcjrp-Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3126b51523.mp4?token=eKWOkYKU6ypgxg1ghJgQcoND9fOqWln8sIMHS9zq1F4igAhjm22R8t08KoKyalbcr6Y-rh0qT-jyz4ztj3BULIw_-9wxCnlujSvhvHxRBAY9PTlv8JVphg-kyZT2Hc9mWm4Jv9ZMN52RxI7mo90ya5yIuQdKIUovTF7EpiXnVIsomSHaglzrUXJGwKzYs1_fmA4EVr_ecU7_kLYEu_mLDDsqdqv5IJKrPQR3KpgWBP653hLHsok4e_Ih4GMoellkfGoo3VtozuCrs3-7YtbamaikS7YcyYNYIok86DPdvH3zGXo1yEEtYlnNvtX1WT-SO0Zi_nPIRdiNefVcjrp-Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
😂
وقتی با رفیق بی‌اعصاب فوتبال میبینی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/98768" target="_blank">📅 13:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98767">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a26046d5a.mp4?token=v5m728CnenH-FdFteDWBdK0P1SLAzVb6G2RDBlP3k1ZMMXqtQikTetASJRD3SCUEIBdgiyRZSv0BxECxIeBZbafU30o03XuZhik3oQa7RiheLVI_wcnGCgQBowV5h1rNQSJl1OU6sTXndp0VFrJpzlVpmhBr7brR6c07nE0YucCS7p0afc6MYShD2VBsNmD1X7nJCYs6w_aSzedcKbVxiIRXVb3elcfhtGdxnxi5VLTo26OW78IYOfrixtZmULoHtcciGQdozozAKXq5lPNii0rPXo8rvI9q8TLTmbfEF3LYScP6H6FJuRzEc_ZzgncVtTgCPpVCxQiRIPFW1nBrig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a26046d5a.mp4?token=v5m728CnenH-FdFteDWBdK0P1SLAzVb6G2RDBlP3k1ZMMXqtQikTetASJRD3SCUEIBdgiyRZSv0BxECxIeBZbafU30o03XuZhik3oQa7RiheLVI_wcnGCgQBowV5h1rNQSJl1OU6sTXndp0VFrJpzlVpmhBr7brR6c07nE0YucCS7p0afc6MYShD2VBsNmD1X7nJCYs6w_aSzedcKbVxiIRXVb3elcfhtGdxnxi5VLTo26OW78IYOfrixtZmULoHtcciGQdozozAKXq5lPNii0rPXo8rvI9q8TLTmbfEF3LYScP6H6FJuRzEc_ZzgncVtTgCPpVCxQiRIPFW1nBrig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🇵🇹
مشکلات‌رونالدو و بازیکنان پرتغال در همین ویدیو کوتاه کاملا واضح و مشخصه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/98767" target="_blank">📅 13:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98766">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
#فوری
؛ پائولو دیبالا ستاره آرژانتینی قرارداد خود را با آاس‌رم تمدید کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/98766" target="_blank">📅 12:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98765">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90c01d0028.mp4?token=lnwQB29F8ruPJe6CPTvQIPVd48S3m1c9LJEYXACVVxx0ZpHFkipaP-4ItrEwSue97T9ZWrKrqUhy4TQse5Ir5oxbpU86wyQZnI9ozaql0PdPPXZyAchuDTPpa7siuxKLUJmFN1bSPYJTD5JZ9ReA3uv-IPsl058-xa0Zzj54X5yyKwDactOrAANZP6Af3kSZcK6Ht4fJ2wFLLbmgs_lngJeOjZe1UT7QPCGnzeda_L_3ifjxDe0rE53OhKVLwSh1lxRr7xa4UJ4zxzg1NKorNT-D8czRlb09YAakP0NVq9B8JPJf24qGo01n6xR9ZjgOxUbUqKO4I6OLcHy94r4_pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90c01d0028.mp4?token=lnwQB29F8ruPJe6CPTvQIPVd48S3m1c9LJEYXACVVxx0ZpHFkipaP-4ItrEwSue97T9ZWrKrqUhy4TQse5Ir5oxbpU86wyQZnI9ozaql0PdPPXZyAchuDTPpa7siuxKLUJmFN1bSPYJTD5JZ9ReA3uv-IPsl058-xa0Zzj54X5yyKwDactOrAANZP6Af3kSZcK6Ht4fJ2wFLLbmgs_lngJeOjZe1UT7QPCGnzeda_L_3ifjxDe0rE53OhKVLwSh1lxRr7xa4UJ4zxzg1NKorNT-D8czRlb09YAakP0NVq9B8JPJf24qGo01n6xR9ZjgOxUbUqKO4I6OLcHy94r4_pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گریه‌های شدید نوجوان ایرانی طرفدار CR7
😢
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/Futball180TV/98765" target="_blank">📅 12:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98764">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eac4eb6bae.mp4?token=eU_i5rmrJhAzcn90pluHUzFiInAkmAV1MjdJ3OaO7VBbt621FL4IWBBCZZSb1nZUkm7CEPc2q6SKxyearJ60R6q808rJsg91ssbcPxsDnc3tPArcpL0P8Jt7ePuXQpRnEnpUtbfrPwyo4xcClyfKtJ23Fid15UVhv8nsenb5MDwa2tF1LXV_NhnYpp6iM7CTCnXJtFxv6DEhowalvq8Sak6HHn2rN-r3FFmLMlxr3EarS0AO7MK7rJhaNGuv5VCpPqK29RyaJZwuNBty_8ICJXS1FKhxi62jeepgb6YTztsda8s7_-pjtAsy1DlSby2ekF2r9lJmmqSdlkIZm6UaVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eac4eb6bae.mp4?token=eU_i5rmrJhAzcn90pluHUzFiInAkmAV1MjdJ3OaO7VBbt621FL4IWBBCZZSb1nZUkm7CEPc2q6SKxyearJ60R6q808rJsg91ssbcPxsDnc3tPArcpL0P8Jt7ePuXQpRnEnpUtbfrPwyo4xcClyfKtJ23Fid15UVhv8nsenb5MDwa2tF1LXV_NhnYpp6iM7CTCnXJtFxv6DEhowalvq8Sak6HHn2rN-r3FFmLMlxr3EarS0AO7MK7rJhaNGuv5VCpPqK29RyaJZwuNBty_8ICJXS1FKhxi62jeepgb6YTztsda8s7_-pjtAsy1DlSby2ekF2r9lJmmqSdlkIZm6UaVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
😆
😆
پرزیدنت دونالد ترامپ در بازی دیشب:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/Futball180TV/98764" target="_blank">📅 12:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98763">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5f978d2d1.mp4?token=RgZ19zE2EKVasBtldGrC-zuC-rO7tSZ7t5P401TT_LiBE29bQh09G63Y1tH0EEfCWzYsbl3bPImX8RNb0U5Zj7wfrh-W59PvXDezZnH9xv0FU-bXXAgdvPGb3NHAdPunpZ10VG4RHRJY7UCNDiK39RPYzHZfw1KbBOaEZtHIq79PQSkrtOkOascHoP2jCs3mzP9srDPhSjlq8rTZSffVgik0ZGQynfomb2nTpHP0vRk8pw-vdWpCLuDGDAHKociL5r9TWuJq7YC5BJZP2gzYc7C9lSF6qz5LxrCNpB7fospYmVAMBBunWz2qnwZDUe7jg6_DsJKBxlTrAC1E6V9izg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5f978d2d1.mp4?token=RgZ19zE2EKVasBtldGrC-zuC-rO7tSZ7t5P401TT_LiBE29bQh09G63Y1tH0EEfCWzYsbl3bPImX8RNb0U5Zj7wfrh-W59PvXDezZnH9xv0FU-bXXAgdvPGb3NHAdPunpZ10VG4RHRJY7UCNDiK39RPYzHZfw1KbBOaEZtHIq79PQSkrtOkOascHoP2jCs3mzP9srDPhSjlq8rTZSffVgik0ZGQynfomb2nTpHP0vRk8pw-vdWpCLuDGDAHKociL5r9TWuJq7YC5BJZP2gzYc7C9lSF6qz5LxrCNpB7fospYmVAMBBunWz2qnwZDUe7jg6_DsJKBxlTrAC1E6V9izg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
ویدیو لو رفته از رونالدو در رختکن پرتغال
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/Futball180TV/98763" target="_blank">📅 12:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98762">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vpOgTlZrHhBrbHfF8wS_s8izBhKrIdYqB7P95fEaXWpR-XM8rFHpxSR4pugTRygLeYHo70DbqQo_zl61y0i-5tpRGjkVkZasjkRafkhoryPvAcwMtaKRMAjmtu-wn4a_ZIS7cb3ZFBIgTfvFII0PHCfrzKy8DkuTbu99zfB2CkkoDLStWsrXOyyjj-1--Q9pxP73zzQnfQy0QvXQCvbZpb4v_OCAxAO2YOylJ7FeTKE4sneJs9p-HWY4vCXkx4wPeIV2nh8ACqTApJzovfBjJFJrJ2WFxS7Di8iIn9K1ZqfE1J1cKxD3dsDjTZcm68p4OqYaRF5LgBNAxYuZxbJnZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇧🇪
اونانا هافبک تیم‌ملی بلژیک در بازی دیشب دچار پارگی رباط صلیبی شده و ماه‌ها قادر به حضور در میادین فوتبال نخواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/Futball180TV/98762" target="_blank">📅 11:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98761">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔥
🏆
فقط چند روز تا نبرد حساس مراکش - فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/98761" target="_blank">📅 11:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98760">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q4HSIayb7GyKDWWTAaEYmiYN_7j4W9qIeAHi_xpMaLp-l9Zfzb1-Mz5iK4mrgxUZttaTmp4uao6E43JMTFFeum0gH1ePcNw3Xe7VTL2ZqQ8nCnikajpr6icAUyAEUenhE3nzh6jJoVtEWpKrqDhvYsRUw4Gb80tfzaq9n3UFc9KXWMvFEUm6GpODTyu-_Aux8BJNYomajX52tGwdbX1ZGONpsXXOcKJOuw4bcggEGokX5pybfdaews1tKOzpIQ0z0cagHScicJy12kfrejxTpy_iKRFeViHReQrOknCQIGWIFDzDSiacuAPlvW6xsGfm0fRs-LwZicQE4YUktd9MPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رومانو:
اینیگو مارتینز با النصر عربستان برای تمدید قرارداد یک ساله به توافق رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/Futball180TV/98760" target="_blank">📅 11:10 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98759">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V3Pxc_emWVzkWgBneIfrs9DjSz7PRMk4MfENlqZ_16Zzd4REOdT1YaTOG91mzN4MdxWDnCnJMVj3IIHQhXcJedqsplPJqyrKDwF3WUJa75plxKXWJhC73zTiQ987wh8ke4bzUcN_kt86MyIwH8r-oEJ3Qje1GvpITUMM4WeQ3uXbmQSUdGlfqdfb1q3a2mquTq52ZemAFj3t9nz_eV-d-XhbDi0eI2XH3F6Nrw15ucHYVUQOf9IcYH3XvxQ-3RY5K1LpejVyCWm9fROHx6snu1dCoCssrldxszFXjzmUZooI_XmDlz-azODfagQ0Apmiys6HB1YlM9iSDqoJIt_Agw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
بازیکنان رئال مادرید تا به امروز، از بین تمام تیم‌ها، بیشترین تعداد گل را در جام جهانی به ثمر رسانده‌اند.
⚽️
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/98759" target="_blank">📅 11:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98758">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8801234d0.mp4?token=HT2CWRq3kwdfuJrhCcG6z1VbBVXmkEaTqVhubDmju0UykU6NU6YZ6Zg42lA_R7TBkdRrP3xL9jDe4kKBYAq8BgA3guRisJD04HRixAEyuJAzerbJ11xE9qxnaJns6dyDEhrwPedOAIVtkS1IF_k2LOPq7qoQ8ugPhY9Ooj_8ZKeN_cGU-GpFcq6HIzR8VnX37Fyc0TbSECQCXJf3AyS7c8C7aic9bs_mvC96h-cWkyLdiNeOQ4t1xDgP4v9wjad9O1mgfMbB-C8GapefOu8Fobfh8dV4OtOLizVF_0wolw_oolPSzDFMJUELM_sJ6h0A-eDEb1J1hAWsgThX4TTTSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8801234d0.mp4?token=HT2CWRq3kwdfuJrhCcG6z1VbBVXmkEaTqVhubDmju0UykU6NU6YZ6Zg42lA_R7TBkdRrP3xL9jDe4kKBYAq8BgA3guRisJD04HRixAEyuJAzerbJ11xE9qxnaJns6dyDEhrwPedOAIVtkS1IF_k2LOPq7qoQ8ugPhY9Ooj_8ZKeN_cGU-GpFcq6HIzR8VnX37Fyc0TbSECQCXJf3AyS7c8C7aic9bs_mvC96h-cWkyLdiNeOQ4t1xDgP4v9wjad9O1mgfMbB-C8GapefOu8Fobfh8dV4OtOLizVF_0wolw_oolPSzDFMJUELM_sJ6h0A-eDEb1J1hAWsgThX4TTTSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇺🇸
🇧🇪
خلاصه تقابل آمریکا و بلژیک:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/Futball180TV/98758" target="_blank">📅 10:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98757">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PO52lA9m_qtSoIffauJDav0Ydi4YxeDjixXOgIVLMCskG9nFCE6iAm7YJai4fk8OsZLisK9L2SLO6oIFA53AhADJN0hIM3olGsAaX4ftUkzIkbusUPBlw3qY11jDeaYWc3hF_2jWWUXdZVqL5ZavJVNItUs6iaG4AeEcw3yXDVKPyyQTCtAkaF4NbJ4WpmHaDj3FqwyMBKilxueGoiTyn61gAksRKFZRgeI_Q5_1ixmKtFw5-j5rPCIBmTqxxt65g5ZN9DcJay20jkjofNM_5sSKUywBliMNHBOeBKM4EruTEKvkuX3GS7c0lb5RYgrmh2r4S5cbguXGUITI6HCQcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
استوری پیج تیم ملی و کنایه به حذف آمریکا
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/Futball180TV/98757" target="_blank">📅 10:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98756">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d094fe0d5.mp4?token=WCOayQxfav-A-JoCratW3bGkJF0re6sx-R0U8FAfyhNtgRwFPP6ciT6mfY5K3c5ZgYbQpD94QXlGfg9oZWdh4Vob88XNQ4gccHIWRcLACk_4LcKVonjfWuKaL_JbHiqrdfxPns8OtkZlpAq9yk6XtGXTPJlYFNkaMI96kOIlKHEl7jP5DNCmFi6HWE-YBbORm7eQvtJ6qJAKUfJpNdoGCYIamfF0alXPw4gmGk7eHv6oWwUgSLqTLI193aJ1JMYMfXZJKHuqRn0vrXVClgOfMRvGNn5jnkyLGDcqpd9oTICyfxo6RtFSqWNiJLCIlN-NST33GMBInWsLoEySJ4QLc6Sq4DGKzTCiWC38_IFvT777kzh4Qz1tVqZvkQKn_4HutsmazUP8lwmmYsflPob_WoXXuk_l3xTLROKQnAL-Eo2EkBYN3PO7SZ2DcUcFyPF7gIZREcX-ULO-tpH3nprbtUpe9jMInFbJVBkp0g7tJ-9RWSr5-sk14nE55KVqcOGHtSX_zJ_MwjyVyXvfdyVqgDkO6rqHrWS1R0fK0x_5wBdlsVztKLEqL8wpWPTWybHoiVYg6eXk7PL6HLqbf10-Uo6qULZCMXhtixSzczUSwh2JJMfapOA9G_HqmEpIRT-GEc8kQrSjFXQW1RRhG3TXbDyfJ28AwReTN_7FsdjZQyc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d094fe0d5.mp4?token=WCOayQxfav-A-JoCratW3bGkJF0re6sx-R0U8FAfyhNtgRwFPP6ciT6mfY5K3c5ZgYbQpD94QXlGfg9oZWdh4Vob88XNQ4gccHIWRcLACk_4LcKVonjfWuKaL_JbHiqrdfxPns8OtkZlpAq9yk6XtGXTPJlYFNkaMI96kOIlKHEl7jP5DNCmFi6HWE-YBbORm7eQvtJ6qJAKUfJpNdoGCYIamfF0alXPw4gmGk7eHv6oWwUgSLqTLI193aJ1JMYMfXZJKHuqRn0vrXVClgOfMRvGNn5jnkyLGDcqpd9oTICyfxo6RtFSqWNiJLCIlN-NST33GMBInWsLoEySJ4QLc6Sq4DGKzTCiWC38_IFvT777kzh4Qz1tVqZvkQKn_4HutsmazUP8lwmmYsflPob_WoXXuk_l3xTLROKQnAL-Eo2EkBYN3PO7SZ2DcUcFyPF7gIZREcX-ULO-tpH3nprbtUpe9jMInFbJVBkp0g7tJ-9RWSr5-sk14nE55KVqcOGHtSX_zJ_MwjyVyXvfdyVqgDkO6rqHrWS1R0fK0x_5wBdlsVztKLEqL8wpWPTWybHoiVYg6eXk7PL6HLqbf10-Uo6qULZCMXhtixSzczUSwh2JJMfapOA9G_HqmEpIRT-GEc8kQrSjFXQW1RRhG3TXbDyfJ28AwReTN_7FsdjZQyc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
مشکلات واضح کریستیانو با برونو فرناندز و سایر بازیکنان پرتغال در بازی دیشب...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/Futball180TV/98756" target="_blank">📅 10:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98755">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92b541523a.mp4?token=c-VaCOPptkFQ1-ZxxnGwgP0Ya38D1-eAIS2JkuiuOYd-WRiWlfyhEVUtu9yOufeJEQtsr-f16ZBh0d3pg0U49Sbcdac6uhW0VhOeLRlDv3FAhhSVze6GcY0tuOohD2KSgqebPvM5XxYnU4qiZeqKtFUsOcRHfUEcgwfxF3eoeOAs-Mje5RkQ17SJ7SO6O7zy9-gb65hphn92Y6b4NfKvHZDHflKahvxidevL6B8Ydc_0zUc-7LDWPpQADp2O1wBvPT3HNklbFH4u73k5W1ohirYcQH2kYKq8RJ18HhKFhrTc9SamxelCHBt1LJGFe0kENr32T367aU4Ge01Boda1rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92b541523a.mp4?token=c-VaCOPptkFQ1-ZxxnGwgP0Ya38D1-eAIS2JkuiuOYd-WRiWlfyhEVUtu9yOufeJEQtsr-f16ZBh0d3pg0U49Sbcdac6uhW0VhOeLRlDv3FAhhSVze6GcY0tuOohD2KSgqebPvM5XxYnU4qiZeqKtFUsOcRHfUEcgwfxF3eoeOAs-Mje5RkQ17SJ7SO6O7zy9-gb65hphn92Y6b4NfKvHZDHflKahvxidevL6B8Ydc_0zUc-7LDWPpQADp2O1wBvPT3HNklbFH4u73k5W1ohirYcQH2kYKq8RJ18HhKFhrTc9SamxelCHBt1LJGFe0kENr32T367aU4Ge01Boda1rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
⚠️
خوشحالی شدید میثاقی و دیگر مجری شبکه سه سیما از باخت و حذف تیم‌ملی آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/Futball180TV/98755" target="_blank">📅 10:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98754">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2731679c05.mp4?token=YshaLJMtabCuCnq67qclYWsOley3fJI_m2TtEcGNzRsc6IsKtuQWYqJmhXIxcjv-Nvih5c3PMUkpTkZdPNZnhoXxYZtWVSf4nvfeO8FNmUdKHx0W-oqrVrbCCc0Qq35jgaLkXqUuPEbYURLSzjQNIbAn72_0BY3gRvXB32F7xWRwbSeLidyexte2IhCq6ge6tCeaX6esc8ekthNB0TZnBtr5rIQiZnhNkHSZDA0N_A7Pm8dpowRrketISnzCN5kjxY9aj7SEvJaIjXOe2fQHPRjundc5X0Phe1GmFjggJMkFWfxf0m0zI2uVyI7vZuOFW6ud64j7bk1XtbDwZq3UvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2731679c05.mp4?token=YshaLJMtabCuCnq67qclYWsOley3fJI_m2TtEcGNzRsc6IsKtuQWYqJmhXIxcjv-Nvih5c3PMUkpTkZdPNZnhoXxYZtWVSf4nvfeO8FNmUdKHx0W-oqrVrbCCc0Qq35jgaLkXqUuPEbYURLSzjQNIbAn72_0BY3gRvXB32F7xWRwbSeLidyexte2IhCq6ge6tCeaX6esc8ekthNB0TZnBtr5rIQiZnhNkHSZDA0N_A7Pm8dpowRrketISnzCN5kjxY9aj7SEvJaIjXOe2fQHPRjundc5X0Phe1GmFjggJMkFWfxf0m0zI2uVyI7vZuOFW6ud64j7bk1XtbDwZq3UvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
💔
💔
The End
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/Futball180TV/98754" target="_blank">📅 09:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98753">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6be3fa0b5.mp4?token=LMkgrbVUi9-VrMNxagGesfiyQWtX8l85kOxdqU-7ngegOqhMrlwEJaUXuXPieN5OTrIKN3jqFf4nOpLnUmcr9hH1qygPCKgzT0TlaBu14sKaWcYrNzH_PzlavL4IX-ygDdJe9_f8-TO_QhnuRpca5lNn6YxdPNr8y0IOyite07WxcWNqC8K3t_DG6zV5l5QgkGjX2Sv-DsdaxFS0iwA6ny84rcU6qo_N6nFE0CcA0YiOhHf_LvTKJAMqJNeBW4IPj6sUYAcmJpunSBHe77WX2AJ5tUoYqsscwGybXvqX1qcTB14FhYMB2aSdiiviKm6BZhwIpO25_FVxJrQgtix0vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6be3fa0b5.mp4?token=LMkgrbVUi9-VrMNxagGesfiyQWtX8l85kOxdqU-7ngegOqhMrlwEJaUXuXPieN5OTrIKN3jqFf4nOpLnUmcr9hH1qygPCKgzT0TlaBu14sKaWcYrNzH_PzlavL4IX-ygDdJe9_f8-TO_QhnuRpca5lNn6YxdPNr8y0IOyite07WxcWNqC8K3t_DG6zV5l5QgkGjX2Sv-DsdaxFS0iwA6ny84rcU6qo_N6nFE0CcA0YiOhHf_LvTKJAMqJNeBW4IPj6sUYAcmJpunSBHe77WX2AJ5tUoYqsscwGybXvqX1qcTB14FhYMB2aSdiiviKm6BZhwIpO25_FVxJrQgtix0vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب فوتبال گریست.
💔
😭
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/Futball180TV/98753" target="_blank">📅 09:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98752">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a1d0006e7.mp4?token=JKRw6UxrRU0M_MZKUQX3oCnIyyRgNMYj_jlEagt3ra07FfWMsMx4ucb4TwPUZ55iQCK0YFQfdWl6jFB6hG68b6uOBG0cwPRItaBQRSislh4OiLV5PQUUch4rSNTlzIOChlzPyxWS1pBJA_kxztn7F8IHIBoPi9xWRn-8AtQ55CfOPp51DnJdrBNLw7fpHwcMi_15cFWCfOk1FZu_tZAH_N_t2woujm-oE8y51iaORP9txQANCA058inVcRnbvfHaQHhVU3dj8LowF1CJr_9enTO9ZCzH1HhXIGSG3T-DjF_DMysLvYFjClyShIbRoAWkg1pbUze-eVRE3dqGIgAclw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a1d0006e7.mp4?token=JKRw6UxrRU0M_MZKUQX3oCnIyyRgNMYj_jlEagt3ra07FfWMsMx4ucb4TwPUZ55iQCK0YFQfdWl6jFB6hG68b6uOBG0cwPRItaBQRSislh4OiLV5PQUUch4rSNTlzIOChlzPyxWS1pBJA_kxztn7F8IHIBoPi9xWRn-8AtQ55CfOPp51DnJdrBNLw7fpHwcMi_15cFWCfOk1FZu_tZAH_N_t2woujm-oE8y51iaORP9txQANCA058inVcRnbvfHaQHhVU3dj8LowF1CJr_9enTO9ZCzH1HhXIGSG3T-DjF_DMysLvYFjClyShIbRoAWkg1pbUze-eVRE3dqGIgAclw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
خداحافظی رونالدو و پرتغال با جام جهانی 2026! اسپانیا به یک چهارم نهایی رسید.
🇪🇸
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/Futball180TV/98752" target="_blank">📅 09:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98751">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fbf2cb410.mp4?token=dWVxjQ81YU5BG-cOrRvF2dbK7F0HWzvc6FqYy0AKJmElO4yAhqt_kmUi-SeYreyW8giwZsFPKRsCJGaQ4Byz4rdCeYtMLqdeGAOLLlEVfFGXecMxF9miFb-JAd8HYfuY22tIDdoU5d7CWdtx4dfDOARYvFDzgHa_15uCsUwRcOt6rf7SIQJ0CiIbUr_dojSS9wyCzPE65JjgYe-jINEoe-9wY3szTuI8qG7gfJQcPgp_KjlAIoOtlNFZlVMQx9_Ull286YcEKS40MPdY58EjHt6e0E7vZIKZgbwmz6mmBJIYlPAGSdLV5ssPUm9p6_Lw8yqIO87UqZiR5QodQ2QD_ACEfpco1h9UnOKF2d4cJKn8McMuS6WcrDjVWl0ZCiCF3eyj9hnHAyMwUYEdKTvIBFfJpRnKPJC466gUE4ZMV8AQaEq5FlK1pSyHFxMH2Ls9JD0M9px2ux63TfbdbeVyc-2Q8vGXpQyjh_jNms29nWgCChtFyUDBJJHr2UASaDQF3pjo5LJlw7mO4COld2syw0fwDiRbFJW7N5eAjH2IOmLx1qFOq0bxErrtjIM69ViieqUCHMB3OtJfSeOwQaWZO5mFFBeNQmnI5FPnEaHC3I28lP_Vp1kMaRKEfH5iT6maRKH0RvlPNZAyOoyp9pt_yjlclfA3XyifITcUixmN2AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fbf2cb410.mp4?token=dWVxjQ81YU5BG-cOrRvF2dbK7F0HWzvc6FqYy0AKJmElO4yAhqt_kmUi-SeYreyW8giwZsFPKRsCJGaQ4Byz4rdCeYtMLqdeGAOLLlEVfFGXecMxF9miFb-JAd8HYfuY22tIDdoU5d7CWdtx4dfDOARYvFDzgHa_15uCsUwRcOt6rf7SIQJ0CiIbUr_dojSS9wyCzPE65JjgYe-jINEoe-9wY3szTuI8qG7gfJQcPgp_KjlAIoOtlNFZlVMQx9_Ull286YcEKS40MPdY58EjHt6e0E7vZIKZgbwmz6mmBJIYlPAGSdLV5ssPUm9p6_Lw8yqIO87UqZiR5QodQ2QD_ACEfpco1h9UnOKF2d4cJKn8McMuS6WcrDjVWl0ZCiCF3eyj9hnHAyMwUYEdKTvIBFfJpRnKPJC466gUE4ZMV8AQaEq5FlK1pSyHFxMH2Ls9JD0M9px2ux63TfbdbeVyc-2Q8vGXpQyjh_jNms29nWgCChtFyUDBJJHr2UASaDQF3pjo5LJlw7mO4COld2syw0fwDiRbFJW7N5eAjH2IOmLx1qFOq0bxErrtjIM69ViieqUCHMB3OtJfSeOwQaWZO5mFFBeNQmnI5FPnEaHC3I28lP_Vp1kMaRKEfH5iT6maRKH0RvlPNZAyOoyp9pt_yjlclfA3XyifITcUixmN2AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🎙
▶️
امیر مهدی‌ژوله یکی‌دوسال پیش این حرف طلایی رو به عادل فردوسی‌پور گفت. بفرستید برا هوادارای فوتبال خصوصا رونالدو فن‌ها که بدونن ناراحتی هیچ فایده‌ای نداره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/Futball180TV/98751" target="_blank">📅 08:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98750">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/898c349cd0.mp4?token=AibIqAO4Z6GcJkV97s4MXGn_a2TCh2GB2TgJQOtNWoEtlV3bkMTIeYlJoW9i5mBPmMQm5VjiqnXsxpX5nEYDdH4Ayu3RJajZ3_jAcG4VP5pR9OuDkqmk7K0tJ65nBcW8JmrT38B9dIWrHFSv2AeKf3EiA43Tdmif4mWqVCZnZyHnhpC_V3lZi58X2KgQvq_PBE-3UOYQgL5xgpiSBUrTEPT0R64Ad_H765K__WKfppdwRLTbmyAqhNxBH0yIemUf9oZg3Ta5OgaZ9R8W0uyxcGAsd0kqsu6-sX6vC3D9XiM1VaW7wwhtCBJnZ3rQmHZ5y-vBqVvgkLAaMAfUD-K9bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/898c349cd0.mp4?token=AibIqAO4Z6GcJkV97s4MXGn_a2TCh2GB2TgJQOtNWoEtlV3bkMTIeYlJoW9i5mBPmMQm5VjiqnXsxpX5nEYDdH4Ayu3RJajZ3_jAcG4VP5pR9OuDkqmk7K0tJ65nBcW8JmrT38B9dIWrHFSv2AeKf3EiA43Tdmif4mWqVCZnZyHnhpC_V3lZi58X2KgQvq_PBE-3UOYQgL5xgpiSBUrTEPT0R64Ad_H765K__WKfppdwRLTbmyAqhNxBH0yIemUf9oZg3Ta5OgaZ9R8W0uyxcGAsd0kqsu6-sX6vC3D9XiM1VaW7wwhtCBJnZ3rQmHZ5y-vBqVvgkLAaMAfUD-K9bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
وضعیت آسمون بلژیک بعد از بازی امروز:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/Futball180TV/98750" target="_blank">📅 06:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98749">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dRcVqMoZ-mW0cAhWBeJYc5z7_rY2RwkW1tfKGiU3cizlr_ZT3iIt7pDQx45-Gmvpe1tyRZTQfaTwSxK7FAElMXGGpZNABFg0yu7vGT4AdBDI24fyCT26lamp5pcWp03s4PaPEAICnLcuUD9dyU_eIo7uIMWfbw3ZigdjONK5rEjh2-mL9JYIveSXCCYOPcGvXwY7rQ_jE6WG8dzwAwPC_KSaqvscxBAr7AS4v8OrBKAA1uIKwG6FgDRUP0J3xmJqE1g6M7ZO9-fW1GSwHPS40_UjlOOM0cPL02A3SoaD39YSG_7QcEKhGyrIbEa0JiSKi2Lb7jCt3e4C2OJbeW33ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🌎
| روملو لوکاكو اولین بازیکنیه که در چهار بازی جام جهانی، به عنوان بازیکن تعویضی گلزنی کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/Futball180TV/98749" target="_blank">📅 06:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98748">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dHKWO5S7LfcgGJQpQUpOBUSkd1pbe22yu5ULsZEpK6wYtO4-5TAkhOIRo5fs8KoPD5ZenHX_VHAQIvwLXjrIIgtRZEzVuEM3U-73ryhFzZpjg5npejaYPj9U75rH8AErZtWCWeMJrDOe10wJI3eQDxDAOME8CFagdbxRggI_VN1zb5EQ8t3yacechBuhgYAoLYVI5muGBALJREBJl6gzHQfoDPbgRF4y8y4eWQkRWMu56J9ft7B1OwbzFNGFK1JTEsxgpUpkzZqg03_0asPS3hu6A1jqettuBp0XQIWHT5XzzThUsATYTg34fRY8GvtzIhthhUr1-9fs3RGLGylgBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🌎
| روملو لوکاكو اولین بازیکنیه که در چهار بازی جام جهانی، به عنوان بازیکن تعویضی گلزنی کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/Futball180TV/98748" target="_blank">📅 06:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98747">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DYZZVA_r7B1PcHyBcjYja8bGITPpGts4kegTjfAn_EtUCwW6DRfbIM7R1UWF23oS6vci3vYc6VzXqffu4lJpn7o_EsGZblLJ6fFgGQaZhZOPZ88zcaMMked03m3CUcNgtOdwFph5U0QV2pESX1G7VU5AinblsfcceC8N52PutSKD3NGH7rRF2KftngMRvTEWSytgo9LEJKtsHUzybynNn86-JS04ueQn0UnHbX7d5qKRYovtKyuCPYDAOWu-vBW3KFWA9fv33Cr0nJmeeGr2SKICNUBp9ekR6ffXsXy-h_DmXhWJh12zE38ysYyXTRpWRzWNP1nOiRnAXXpw7algyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیس پیج توییتر تیم ملی بلژیک به آمریکا: به این میگن
ساکر
فوتبال
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/Futball180TV/98747" target="_blank">📅 06:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98746">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MfDSS0wkvNJE9wtB6WtwQ2QtVRLSqE9ulQ_4mijbXDcQUte-ss-8ii4wwEIZVIhO0-KaTBD1R-sDeLtuCgTFEaTbEuF8Q1H_Rhy8m-NqdnLijKHnuHWO5BHwbZ2Y1zumerkPjDKvMMtz6pgX_OZO1I-tXDeq-MbmlltEH-VJ0jeiXCYDj1kRVUngJaAdp20NxuqwQcXt-URzeWruXOb4BRzx_gEgHuPWFFK41cyjD4q_e2IsFVSOTU_yWgdZgm6M7SPHdrTWgdO6_wqaKBh8YSUnQNTGpFGR_n7SjGeROUrPXnh3jfmNTJxp5Iqf9Q-t6Y4-4tOrlK8A4MGms_n5rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تقابل جذاب دو ستاره این‌بار در جام جهانی
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/Futball180TV/98746" target="_blank">📅 05:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98745">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U4pmhD0_hSO4HWJW1qjCSa4vksvEeQ3g2XqqjME6ZUILGE6gYhjd7Kktwzt9tq7hpmv45OCxyXbgeDD24_LnoadvxfJ5TwTWclEz_slsIVU4z-aPYT4dN6P8y7LC3EQzEusagJLszkztGEpw_SDPHaaaHs5znG_eukmTQ8QMrhTiPWflIeTQhZtOizp8d_AWhkOvKOPUnvBNLdqLuHZts7D_SkAdAXUIhSipvzoE8_JE8Mc-PtW_RjznUAY5KuQMhx__cU5OzkvIL_Hfpr7dFJeOjxYcpitFGCVWgFPOEQ9JQ_unnVXF16-GtENwBwYPOCImB3m1pbSFtWSDXmcbaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
مرحله یک چهارم نهایی جام جهانی
🇪🇸
اسپانیا - بلژیک
🇧🇪
📆
جمعه، 19
تیر ساعت 22:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/Futball180TV/98745" target="_blank">📅 05:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98744">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WRwZs2DWQI2BUGfel-zisik1HC7f841jk1xSzn3c1cQssu20pqpud3IXOlI04p8rjIl0oFTOSZnq0D_ti6kwC6qpJZDEHTbNPTppo8p3vggcfrsLXMNT4GdWYOmU18nCKU6qaA_pammjDtt8b7zIB89wcRCEJBBTzge573hKjL_ix_70JpUwPZhdsW0XtOF99iRQW-6f2VE7iLzzF4xy67PwBKEbaKk_nwQTY09NyMB1Pzvrq_P3jSO4kErFAgMbLetNTSojSP4g-MoUumh8IYRlAgoAdYVBWU1rbIC0Ua_vgDS5cD3wU74LyYlSWlW5U7oniJZ6jr90cO0lD_Milg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
آپدیت نمودار مرحله حذفی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/Futball180TV/98744" target="_blank">📅 05:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98743">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sq3qt4IPGemaQK7trl0Ag8xTW69npqRmQEmxtJOpME7QHu39syEDaWbbOCUZTzyynx85EpPQ00ON9YS1G7lF8ZxvemEKU-0fPoiOswA_bcWu_Ku-2uy9Pg2PJ7TauTLsy-0EWtm70pUtxxC6aa9B5JQs9R-78ibcn-q6-q1-4ZrkTrniT3Op4mYAhq6NdgQJtcIq-nbrNHqzxoWR5zzXWoCh1cC00DYqtMnIr5vzCu3AJZKm5_0IEnqN8FMJZPqvCkCbdDKIchLwZUYQQ9tj0BJxrCdjOVL73cLKKX8F-XcANgphZPV0e8AiMtY-Kwb6pM-PirlU3jN0R-VbR6Yj_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | برد قاطعانه بلژیک مقابل آمریکا در سیاتل؛
کارمای بالوگان!
🇧🇪
بلژیک
4️⃣
-
1️⃣
آمریکا
🇺🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/98743" target="_blank">📅 05:36 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98742">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9f32a4acd3.mp4?token=qwgTiRmaO5m4lxWbWngzGCqpFkWb3qXC7xfKIe6aF7UCiUBwWrRMxJxIw3WbgZPKTPIrDzbdNLRDPKFZj-ZQrHJQ1oy2rXleAyeGY99p6VW7bqODUlTZ9-4Vac51qRPyAwTvvC52pxmjuE3z5k-W9axvvgFzG3aEZid_61kLSk02mX3tYWQ-P2OaVViRGtQvshIMp49J3a308loEOeW89W3nMHgz6Yyb26ZDAwAmWe2lD7B0uOqjlToWU9p12SQzVlDlH9kY-nU_0XVac5dNCMYK_ePm_8OoVOWzPLUPXJ4tf6JH9XyOHqDkQs1Wco3BaVRq-8AuT86mG6zsYn0Mqw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9f32a4acd3.mp4?token=qwgTiRmaO5m4lxWbWngzGCqpFkWb3qXC7xfKIe6aF7UCiUBwWrRMxJxIw3WbgZPKTPIrDzbdNLRDPKFZj-ZQrHJQ1oy2rXleAyeGY99p6VW7bqODUlTZ9-4Vac51qRPyAwTvvC52pxmjuE3z5k-W9axvvgFzG3aEZid_61kLSk02mX3tYWQ-P2OaVViRGtQvshIMp49J3a308loEOeW89W3nMHgz6Yyb26ZDAwAmWe2lD7B0uOqjlToWU9p12SQzVlDlH9kY-nU_0XVac5dNCMYK_ePm_8OoVOWzPLUPXJ4tf6JH9XyOHqDkQs1Wco3BaVRq-8AuT86mG6zsYn0Mqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇪
🔥
تقه چهارم بلژیک به آمریکا توسط لوکاکو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/Futball180TV/98742" target="_blank">📅 05:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98741">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">بالوگان فردا املاکی کونت میذاره.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/98741" target="_blank">📅 05:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98740">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">جوری که بلژیک داره میرسه به یکچهارم نهایی ماتحت خیلی از تیمایی که حقشون بود تو اون مرحله باشن رو به آتش میکشه...</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/Futball180TV/98740" target="_blank">📅 05:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98739">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2f766a24c9.mp4?token=L-bqSrXz7k0HjQQSpzZAqiyGSVPDLnqn5RmXpoVmccLZKKPmFBttjXFe0tCn1pl2ykkxtYBCp-dRlYpbhcj97IykfJV0FxBVbdjv6vgqvvcEfX4zH5Fd2uJDkSeabrx-tsp-Vh1TVdTREhM4T7_0699s6-3vNBUwtsJLxVzYnsnIpm_fEij9DgUZcB_I-Nvt0YhDRaApxFfedHY_zD_-JRFmqA93Qs3IpJ0q2Rf8e_sNwOMbTckfn5hszk5RrXSoOo2izlB_w1mUmMCPXi1xQt_HYWdyjZ1YMY1FJRTlWYjeXCDU-GtHK3drCAoLvY6KMu85yosxyri2lkMtxe17qA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2f766a24c9.mp4?token=L-bqSrXz7k0HjQQSpzZAqiyGSVPDLnqn5RmXpoVmccLZKKPmFBttjXFe0tCn1pl2ykkxtYBCp-dRlYpbhcj97IykfJV0FxBVbdjv6vgqvvcEfX4zH5Fd2uJDkSeabrx-tsp-Vh1TVdTREhM4T7_0699s6-3vNBUwtsJLxVzYnsnIpm_fEij9DgUZcB_I-Nvt0YhDRaApxFfedHY_zD_-JRFmqA93Qs3IpJ0q2Rf8e_sNwOMbTckfn5hszk5RrXSoOo2izlB_w1mUmMCPXi1xQt_HYWdyjZ1YMY1FJRTlWYjeXCDU-GtHK3drCAoLvY6KMu85yosxyri2lkMtxe17qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇪
گل سوم بلژیک به آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/Futball180TV/98739" target="_blank">📅 04:59 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98738">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YvSYwepCwosy9sFnbArj_naR8BFcOkQQ5kz4KMzPIozdiUWrlZrDOOckXKIVw4QSDejDmlYfZ2wzF2MtT0n1WO3jJxHAI9nQ3WMppFY3oRh0AeB-n0vtlJFllkudqi1gcbUIOxYHCNwJe1R9foQkXW1_5lIjH9kIPciv_X5vH0wSXA1alzZlsQoFIahYZ_uxbeWrQETu5LA547aGQJgYEhDEHSdnHcRFRXkE7iR33gbr1wKr1bJqgpCyx5S82gpEvVPpqlwYHnR3HvqBc6EY12EsEP9qm7nMcC9jC_0qvjgEEReMvrCBNkEaBLBfCubEMhapYcjTB2r1tOmOJe9D2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی ترامپ قرار نیست برای گل‌زدن بلژیک به آمریکا با سنگر‌شکن B2 حمله کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/Futball180TV/98738" target="_blank">📅 04:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98737">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1e15b6c1dd.mp4?token=eAVkKfnE3hhrYpVrRxriXvJmk3r3F5rFxLlJypyUU7uIzqU7A9ezqtFv-JyGtG8R88u0jArW9mQHwXQ0aOszB3YBQarVr9Qj9houhjzalGrn5tbmUyh05WXiZSTy3TmDUkN_KykSOljUzj5mXnXiSHPlYDyunH80pYFvChV4uuR-SPsurWHYZUFosexcxPyKq9tGDOw2RWrfGK2jd8Ok_WSI3ziVLB0pdU5bY2BSfplqdzSzXLffEmG73fsiJXRjx_lgGaYsDBsbgqv54QTK60gEGCFlDHJUunOMbGFFGx5m8nqM6NqJEAAsuQxv7TnzS1uzCEyBnwcdlV0oDCI9kw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1e15b6c1dd.mp4?token=eAVkKfnE3hhrYpVrRxriXvJmk3r3F5rFxLlJypyUU7uIzqU7A9ezqtFv-JyGtG8R88u0jArW9mQHwXQ0aOszB3YBQarVr9Qj9houhjzalGrn5tbmUyh05WXiZSTy3TmDUkN_KykSOljUzj5mXnXiSHPlYDyunH80pYFvChV4uuR-SPsurWHYZUFosexcxPyKq9tGDOw2RWrfGK2jd8Ok_WSI3ziVLB0pdU5bY2BSfplqdzSzXLffEmG73fsiJXRjx_lgGaYsDBsbgqv54QTK60gEGCFlDHJUunOMbGFFGx5m8nqM6NqJEAAsuQxv7TnzS1uzCEyBnwcdlV0oDCI9kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇪
گل دوم بلژیک به آمریکا توسط دکتلاره
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/98737" target="_blank">📅 04:15 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98736">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/275ce58db7.mp4?token=lu77L3SB72zR5go06c-5GlqQ1bsYbhMf5akVbJ8_09gT8GUUT-iq01Q5--sm1lvPRggue0MOsbZ4OAs9wudJ6iLbWYdx9lz9ZFYnHUiN6D5zV89juReS8Ez3u4T4O07_i-247QjEdw9Oab1DwYz6DiC7rhXIxrokezn6GT6y4y1DHRrjEgM66KAmNhruFOlODyf7ec9vrDEL5gcJby_O5gQkcC-XNBV6WanzVUaOVv96Wh-LRBVDwa67qp08Dj8GUY1_4nTyaoWjLZXmsise-CZ5jNwoBV_C8TFjnrzhXYM-WPUREU3Do8ZouI1PTivp5YZz1Q90yyxk4t4I3ODOZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/275ce58db7.mp4?token=lu77L3SB72zR5go06c-5GlqQ1bsYbhMf5akVbJ8_09gT8GUUT-iq01Q5--sm1lvPRggue0MOsbZ4OAs9wudJ6iLbWYdx9lz9ZFYnHUiN6D5zV89juReS8Ez3u4T4O07_i-247QjEdw9Oab1DwYz6DiC7rhXIxrokezn6GT6y4y1DHRrjEgM66KAmNhruFOlODyf7ec9vrDEL5gcJby_O5gQkcC-XNBV6WanzVUaOVv96Wh-LRBVDwa67qp08Dj8GUY1_4nTyaoWjLZXmsise-CZ5jNwoBV_C8TFjnrzhXYM-WPUREU3Do8ZouI1PTivp5YZz1Q90yyxk4t4I3ODOZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
کاشته خوشگل و گل تیلمن به بلژیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/98736" target="_blank">📅 04:14 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98735">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccd14e6484.mp4?token=ASXuwKorWK_eNoIF3Zw7fKSLauBrXUHHshYr8nZ4ohYqRbDBJ1n3WAX79kjxoRGoZGhYrsS_goUXutYR-5l_3Iy7Rv4vnGLsh4b02a_5IGT191KqGmO4_4Mr9sFgjgrKHc0fr5LfpsfmlJsnBNpttPBsm66w1guVfiiGqiITZec9b5iQpqQw_svBdkOUHv42oQPnp-MiB-7E31fbI4_qW5_Z4ANfZoqOw-yGKgOsAuCs7xZVGbDs3AkQspqwXegUitjqgVW2yl8N76HFMquFoUUbsLyglEKmfLK91JfjU2PtVkb2e7jOAa88ypqtnWq3vDD-8dTc2gRUngUaA4fywA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccd14e6484.mp4?token=ASXuwKorWK_eNoIF3Zw7fKSLauBrXUHHshYr8nZ4ohYqRbDBJ1n3WAX79kjxoRGoZGhYrsS_goUXutYR-5l_3Iy7Rv4vnGLsh4b02a_5IGT191KqGmO4_4Mr9sFgjgrKHc0fr5LfpsfmlJsnBNpttPBsm66w1guVfiiGqiITZec9b5iQpqQw_svBdkOUHv42oQPnp-MiB-7E31fbI4_qW5_Z4ANfZoqOw-yGKgOsAuCs7xZVGbDs3AkQspqwXegUitjqgVW2yl8N76HFMquFoUUbsLyglEKmfLK91JfjU2PtVkb2e7jOAa88ypqtnWq3vDD-8dTc2gRUngUaA4fywA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇪
گل اول بلژیک به آمریکا توسط دکتلاره
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/98735" target="_blank">📅 03:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98734">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AVCGh9-YELjXHYZ6ekfXSCZbYAvseYoQc47VrKdL4rVK2goRJwN3cjZkKK4Sw58GF0kwyvBUQg1rIZ8vb9ZyGQBD-ENMe-9W_5FSb4ygVdrMAGtec66cIJCGkRerB7oQ2qkOiWtA03JmOeRUBzV8Hcv2Ag6hPPDfYyKmqE43ftdTru9ZAmRhHLa2vtZh0YtRPPk0fUIwMY_2jISldeLIiW_TiWQ4JWRdtCAi5yKwpfW5wyXCdN0uvrBsZe2zlYTdriDaqYdp3wmFqwnpCDtjepWNjZ3x9Zh_fNQXp20gQPf1T8nnROcB9YmyQihY1bxROhYdXnR9MTvX-xltRM4v_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیس اینفانتینو بعد گل خوردن آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/98734" target="_blank">📅 03:54 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98733">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r-7nme9g5TvdkDQbKuH2QcLxING3EkFxLGq6701OHolI0ZCmbRmClTWaY6SDWCp2GBVKQgYUuUVdKeORv3UiUUtJ5939q-h7BeXUnws8cO2ZBrexXLGfNaLiwsruJFEp-Ue-Gth0P05NfrzbROTtjZo1pIdRIE2pTqGGH2ux0oYvXFAud3C_zhrxIEA0TrfWJXf-u3OacjlU9-tQUwMXRpDsOX-YVuSCpGnDmMMqKsDCyLD7fgutPJC-T2ic5J4ypY3xmVWvCiGxWD5lAPtsnJhwhyRJVcwfvXGX1S7aNRqmLoJ_yE2ZQlaplNOFqY6eMiRYaAGS5PBFo3sNJQt03A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فنای رونالدو کامنتای مرینو رو بعد بازی حسابی گاییدن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/Futball180TV/98733" target="_blank">📅 03:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98732">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">گللللللللللللل بلژیک
🔥
🔥</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/98732" target="_blank">📅 03:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98731">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">بریم برا بازی آمریکا - بلژیک</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/98731" target="_blank">📅 03:36 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98730">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iCGOQWLZjNMi94ZJok17ueoFUe7M_rSRFcjHQH328I33ypfwoxxMUpJ3F_f1aDvj4x_LWMPR91Owrlyftjrw1Gh9rs8pJLpJjO3EO4YJbF-UOYVIG-5SVtLVGiNEygtkX1ECR1OQjcHGD7SXoh576ld8U9tGOd06MuIMdKduiQkcmTbFcpS0vvmZd18xv-PvKYg2LeLzsHDZkTf8Sc7xOXDxdrhU1hm19gi8O0t49_yNb1OWKeH9YlOTMh8XQWH9UBPITtqvzHvLLtPVR_tmwQxJO5rD43RzlyaDIfJSbI4XX2ZfEj3UrydQOXlCXxFMs9m-8BLSyM28OVDJ89jhdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🤯
مقایسه عملکرد هالند و امباپه در تیم‌ملی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/98730" target="_blank">📅 03:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98729">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/98729" target="_blank">📅 03:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98727">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VxFb9wRYjPPVMtJu1WIbzMeaBFMUvlsCC5GlyDxVzWKtWg47WsVCYL_g_ZJmjGo_3_BVc8YB-akwcpWT0UAvG-6c7Snxzknh3xGP_xG3FnH_X9RlOVTFYLibCx7vktDG4xICLPDH-poD4r7Ys8-UKGGMF6cwqqnNGOKXE60XmjICqa7NKejaQ0Y1BB9QVNySctldGhT4cT3pSwmyLS6E2wWUd0NfEzTGVGGuqPmX-ThNaHZhxUeZjEqsk3ziNGHyTeDDX99ypY05P7_RdniQBvVB-_j1R8EDLNhRKui7PjpGT0jMxUYutQ5LHRsz6WubB7CImt9bgDU4oTHf13yCFw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/98727" target="_blank">📅 03:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98726">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ce0afd819.mp4?token=dCEghKtfi3C_4AzYFDbQ9d8BxbrJbehv7OwHJnjKr8c29Z0bapljrn3nTD8s0mO6CrlkpRzbPOj_x5DS8UkPs_ibHFKviTq_QJBYmMozcj3kTFfKdk9s90ubjpkhtETMnozIXxV3mbMJiwQTLdqFBNJ34V3BnrX4c7YnPn3OLhV4nsErvaBOvSVs3RRPRUb2Z05C8yNBg2YL_GlPndZ3q--RJoyMD0qnVDoHSTNg0Zyk7PEidsqNwD7YHZ92OXND5_1x07-jsgHx0GO1dcyng-hcgykeopzt_LboiXTRFWPV0sWnW1Llf2gkendKk4F0XBXkZfsDxm_evkKWXAE_6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ce0afd819.mp4?token=dCEghKtfi3C_4AzYFDbQ9d8BxbrJbehv7OwHJnjKr8c29Z0bapljrn3nTD8s0mO6CrlkpRzbPOj_x5DS8UkPs_ibHFKviTq_QJBYmMozcj3kTFfKdk9s90ubjpkhtETMnozIXxV3mbMJiwQTLdqFBNJ34V3BnrX4c7YnPn3OLhV4nsErvaBOvSVs3RRPRUb2Z05C8yNBg2YL_GlPndZ3q--RJoyMD0qnVDoHSTNg0Zyk7PEidsqNwD7YHZ92OXND5_1x07-jsgHx0GO1dcyng-hcgykeopzt_LboiXTRFWPV0sWnW1Llf2gkendKk4F0XBXkZfsDxm_evkKWXAE_6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گریه های اسپید بعد حذف پرتغال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/98726" target="_blank">📅 02:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98724">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/moLljciv7E86aYgMUquHH6Fl7SlBmf5g4bqMYBhGQpk-k73Rg62DM1DM0mzpRwvT0FpzohQ0L_9JVO_q-CG6F9X-momw-N9dWYsJfJRIcERPM-SRcmYwbSSBB-orGbREDPvYCbQV32QK29ec-9et6bGsjbnJ_2b_nHody6wFvTtaqFpUbKlEl1acUks7IZLEz0InZPYB8nArbRaVtfg25BeTEHFY4aUKOx7zi-oi4xB9gk1KimYbVSn_3gI6NYb49hX4JyxfQ1nBgqXWwYJMoKaBB1NAu_Fz4tOVJ0L3m9PBdo5sa6zQUIojJGg6M4PtqgpOeDU7aDI2uZv1xSy3Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KPsqqUa324eAEj40MO4CF8Cn2tJ1J7k_l3-lkIF8V3Le-YA1Jv1jg38DLWjc5sKF_OIA0O5qvJBzOiJEwSA7kDSvID2QYUKY_1g5UVQ6hAf9pgjOAEZnSmjrdpLWYRCDcZ1brYFK3VLzEdVi_h7j6T7JmW894WwfTJj_6I8OLm1bYSe1hZrJne1XKJjcBe7EMl92PrPXqyd6sYLC2QI6BndI2Z6nsXa1NUsP_Ixa2TDjVyW4QPDw1LqrqJW30_pohTwPgKZ5N_AIoSbX532ouf6Iim3VOtH86AzvxbymFziWdCXodpdrt12H_rBOBetFnHixNXAanRPdMqdzCae7zQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">-
First dance.
🫣
- Last dance.
🤕
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/Futball180TV/98724" target="_blank">📅 02:16 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98723">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
رونالدو: از فردا در آغوش جورجینا خواهم بود و با فرزندانمان تعطیلات را با لذت و آرامش پیگیری خواهیم کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/Futball180TV/98723" target="_blank">📅 02:11 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98722">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🔥
👀
#فوووووری از جورجینا بعد از بازی:   برای امشب و تعطیلات تابستانی برنامه ویژه‌ای برای ریکاوری ذهنی و جسمی همسرم کریستیانو دارم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/Futball180TV/98722" target="_blank">📅 02:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98721">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
🚨
🚨
اسطوره، کریستیانو رونالدو:  ‏"من ناراحت هستم، اما تمام تلاشم را کردم. من با آرامش خداحافظی می‌کنم؛ این آخرین جام جهانی من بود و حالا باید فکر کنم، با خانواده‌ام باشم و به زندگی‌ام ادامه دهم."  "زندگی ادامه دارد، و فردا یک روز جدید است. بزرگترین پیروزی…</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/Futball180TV/98721" target="_blank">📅 02:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98718">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pxl29NWuVIMCIv58sf6NjbCOV94qBCbhexOD3WIJ3mD8qV5lBxafv2AAQeoqkyayQOmWPfVHZNp3SqM5fC8dZCc__LakA8t9gMb8v4P8ULPssQfNgk3bZr3rpfxTVMLoDg0UAzXnDfnYtO2RViMzE1Hym_sIdp-VUzXVC1Y4MDv7Uy83Kt5sHYPzBZ05oOBZNphlZDaYFf9NhuPhnLbjFnjZmBIy3X7f7jA5aGkBdk0PZQfhPikt9dKiNl54jFbGlRaeljIq7ZdVu1rmTtSVk9YwvZg8bM1W3Glv_GYEseYQrakW5q5TSK2rrRJGNcpbJXh3VF_ap5_6gE2_zEPEWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
🇧🇪
ترکیب تیم‌های بلژیک و آمریکا با حضور ثابت بالوگون بازیکن جنجالی آمریکایی‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/Futball180TV/98718" target="_blank">📅 02:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98717">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
🚨
🚨
اسطوره، کریستیانو رونالدو:  ‏"من ناراحت هستم، اما تمام تلاشم را کردم. من با آرامش خداحافظی می‌کنم؛ این آخرین جام جهانی من بود و حالا باید فکر کنم، با خانواده‌ام باشم و به زندگی‌ام ادامه دهم."  "زندگی ادامه دارد، و فردا یک روز جدید است. بزرگترین پیروزی…</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/Futball180TV/98717" target="_blank">📅 02:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98716">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
🚨
🚨
اسطوره، کریستیانو رونالدو:  ‏"من ناراحت هستم، اما تمام تلاشم را کردم. من با آرامش خداحافظی می‌کنم؛ این آخرین جام جهانی من بود و حالا باید فکر کنم، با خانواده‌ام باشم و به زندگی‌ام ادامه دهم."  "زندگی ادامه دارد، و فردا یک روز جدید است. بزرگترین پیروزی…</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/Futball180TV/98716" target="_blank">📅 02:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98715">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DEDlGAXiy-d-I2TW2LrwSkq6zhGBKvHIfIqTyjkJwDkbYDAicgxpIHySKg7fNbVo6d7dPDcLIojNGoVGYco9cl_JRpq7SBWu9AziyO3WeotzeMX__R_E8icLViitr1eLI5JBhAHRV1ff8MZ4ruYL_6YleZPo497329bsC-XlIQ_XIYk5WHknTn1Zaw8PPzIK-pMYk-mqn2Izd1f6WztUx81wxV-Rkgvx_787IgOSCdrXo0_e1Jf8M3UHpqO8_lMPssCD-6U-423RZYrQILrLr5-7osqaM8SgsUumQpnGDUdF7m3g97M7bLKef9-TAmpt3hf53ggKck1_WU4IaXZRcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
اسطوره، کریستیانو رونالدو:
‏"من ناراحت هستم، اما تمام تلاشم را کردم. من با آرامش خداحافظی می‌کنم؛ این آخرین جام جهانی من بود و حالا باید فکر کنم، با خانواده‌ام باشم و به زندگی‌ام ادامه دهم."
"زندگی ادامه دارد، و فردا یک روز جدید است. بزرگترین پیروزی من با تیم ملی در سال 2016، با قهرمانی در یورو بود. برای من، این مساوی جام جهانی بود."
🥶
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/Futball180TV/98715" target="_blank">📅 01:59 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98714">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XhxxmmZiPmWzgdVI-Kal-cUC78VtbGOrL26NeIdZ-CsAq1iTpXil3rDmgAPs-rAN8KlgBn9FwG2aw-Yqo-p9zhQuRcsa2qhZUynXxIU75SwqDVh7iXv7Wc6fKNe5_MvzzYu6yehdCiwniSeUr6Smv9Pp5G5iO0uWhgS33ZWXXFaeS0BggdYFpHqQGg6P3LL8-gfQt7KimETeiC660EmID7cHL5YFFjor1N_bx1-TyaquiDXGtHtYlFFcBqkSr9mz6zLOsRs83L6s-NNQANshewgA4s6x3ttSYkWMNSut9jV3Bb2blp9BX0Vlmp6wF1Z1qf3-nvyi2xAVaR4y5LEYlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
خورخه ژسوس گزینه اصلی جانشینی روبرتو مارتینز در تیم ملی پرتغال است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/98714" target="_blank">📅 01:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98713">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sUgnumq_SftQoFEN_ya8o4ETMEQVLNTzD8Mxz_5tHsXNdZynYjqLN-8r_uWvCIQ0lgMcSMAZJk83HJZbRy1DBdhYsRX-ghYbWjTyRMBOkWnO8k3cdnX-LDbVlNdc9wQ8J49CvYb34IooHT1XlmRpvs-aga5sF4eE6b8jbJOydL_6dExygLen65_L6b_FHkZRHq2d6wXtKGoEzRsEDh-R4pXUmkNKlb384ArSZpyY9thrxepWTGcIzJYG9rq8B4x5Ud9b_bsC1Ge4sipdKgRA6QMVSE7kJuo7cG-uheSq8dac4gj7r9WftahHu3DovfpfeQ6nJTHG2BOoB47QOdBC_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😀
کسشر و خیانت‌کار اگه قاب بود:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/Futball180TV/98713" target="_blank">📅 01:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98712">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/edfPgANDwuclZH1mgNNFySc3NWl7LwWt42lkpJ4Pz0oGGdHR82Gqrs6BShYC2dLhM6i9Dg7671nz_ovQ7SmnljSg5ku4jS-rKvrXGv8Xd8ZR7f6ZTYZHqYa55pH-Tgbujre3qc2OzNCO_qPs69z1VMvtlvgKQQC0dU-P7VDrZ--eQbe0-FRBFCuokJS2w9QuGm1YKNvZIRMHGgoxoFt9VSECIfTUrEp1cP0rSt4kG20Ir19jHYkOfz-CLqcs_0ldKCaXkrHtV1s-gP58YDshCjg2adI4uBdMHBfou9DV7WGuJQWYPVTz19TGenz3uy9URPAucDUNlFUwlZd8PcDX1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
👀
🙂
ژست لامین‌یامال در رختکن اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/Futball180TV/98712" target="_blank">📅 01:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98711">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CwlHdH8gO11JpqmZprLcVVm-tj0pFce120i4Xmy7QqKwgs3G6HGpVghfFz8RWv_HiRw6Q1c6-6IRanRHJImVsY7epfiINNPzZF6U2cz0ZeX9Rjsbsf-ODQyqnh79jaqPblu_T8RQUlR3DmxzJgiL1RYmyl9mG3tOQsB3GgcfZqdRHR5I-pI5tuysI7SecRQQov8OM8JNB2iamd5AG1-Z7WMn3CSynW1CJ8XFkWfB7o4pAq5kaf7-P-8EfDlH07PNXjs67Yv24wmr57OX3ZCsoYn7Y3ZL-KXbfTlBgGT2fn0MJOnPWWKP2UM3COJIkUN2N2ziQyXHTy4XMdwM2vmn8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
نمودار مراحل حذفی جام‌جهانی؛ حریف اسپانیا تا ساعاتی دیگر مشخص خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/Futball180TV/98711" target="_blank">📅 01:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98710">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XPp-J-QgTQD_hqCsPyhjO3h1I0sdFUvvn98g7-l7LKYll9BLip9CC_1hqh6hOqS3WvY6X5hUdCCBwvDSnXBFD-TBixlxzwFzj2GTd6SQXqXX4saE0e3hQiYkPD-W-BUR3AzQtvewfHI4GfxiUE0LSuhNBX6DwDSWSbHhXiWcPpEfGqYYLXvl4v0u-LwCtBQ0nAuLOMkTbl9qw5Zle_E0tr-Jf8Vw03lCiUL3_9Baz4nKzGRB54uTj5yIq-tlifgUBNcs9PApWUw0THAbBJhbM0jmGSzDn97C25m3U4XQegTARR658hvJmAx-uyzfralhePCUnBvVGoylOSB3cR1NKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
پرتغال قبل کریستیانو
🇵🇹
:
❌
در 3 دوره از 17 جام جهانی شرکت کرده است.
❌
در 3 دوره از 11 مسابقات یورو شرکت کرده است.
❌
0 قهرمانی.
📊
• پرتغال با کریستیانو
🇵🇹
:
✅
در 6 دوره از 6 جام جهانی شرکت کرده است.
✅
در 6 دوره از 6 مسابقات یورو شرکت کرده است.
✅
قهرمان یورو
🏆
.
✅
قهرمان لیگ ملت‌های اروپا
🏆
✅
قهرمان لیگ ملت‌های اروپا
🏆
— پرتغال بدون کریستیانو، هیچ چیز نیست
🐐
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/Futball180TV/98710" target="_blank">📅 01:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98709">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
❌
🏆
واقعیتی که دنیای فوتبال دیدند اما بازیکنان بی‌غیرت پرتغال تکذیب کردند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/Futball180TV/98709" target="_blank">📅 01:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98708">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kyjg2hyVBH1I11NrG6r-Zg7uZaJcEfy5pGmHuIwuZLbY5w7PQCvILxUF5hTjdGklrSBOFKyE7dVhJwipyl9-xKSuh6WovYKTRkMtWx3L1PTEYo4cO-w02pqnGG42SwEhx2mr5dYmLmEnR4H-3_QrUG79g7ytKnnUS6Iu-y4RUQSoWraHGx1EK-8DrASZgmxyhauBZhsYeplmycjndykm3oE64lTTvSD_OsemEq9Ad1JZ8DFu5OmcDbY8MAKSvv81rLPskUAmLwxR3L6CtvWUgq2o5-Ovp7qEIGU3XreSGmnt_T84atdyUzYRPS8htKLbCJGwLhtkl81kxO69IMfv2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🏆
واقعیتی که دنیای فوتبال دیدند اما بازیکنان بی‌غیرت پرتغال تکذیب کردند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/Futball180TV/98708" target="_blank">📅 01:25 · 16 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
