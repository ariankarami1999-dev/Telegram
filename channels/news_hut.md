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
<img src="https://cdn4.telesco.pe/file/vg7qumNc66eMXZ2cO3boI9fJs26fA5yoaQ9E4uW0p-HU-0vaYw0jIGAhQOMCAYYMtwfhWOtl7Hs1_kbnorsaUsBMRQXoJxJnX3_sV3xnqF0Y3x3D5nHpnxjnqfy72Q49yoMy8EXbNGkY0uKlYuZSQ9x-Lum57PCzLtJXc_4vK06KDuuQ4qNoImlVTwStVOKIWm1o-Y6hqxW_BnHCQsPZUdQgkWitkiS937NgSMgEK-aQ5yIlGboHIyBBaNO6mq6JpFgJ_A2gLVqXAYW4SfQtbHTKs-wo_v0avBrTDCQFMydKOWGYQvMfz8K6pj-q9Qjzlx5etFAUE3XI0yGlbw2HjA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 112K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-16 23:33:12</div>
<hr>

<div class="tg-post" id="msg-71256">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f56a780504.mp4?token=LmLH-rg4tglwZJY5T-kIfu1LF5eYkQbD5NjXs6sWuHWuYqh65e5boicciz8d_NXbeLusoPLV4TyXvvBvcVSfdoVLJnLbEi1w_jVzJETwu-8z3kHq7UrkiqOH8_tHhkqfzX69ROy2u8HaBewY2Lt7ONScCx30rWXjAlL9IYgEcyUwzCx-VV7xCimGKS09ZBZMzH6Mps9WeG6GVTpb14pRgzMHR2SRQM_Le5LNaIRSsbvUlhQAQWlXidkspMiX2NZQqQ-L2iynvO2rocVBy2ack9NVWKrs4zLETkancT1HgrrAu6PnK4k0KSdg7A-QCWkuf6AwshOPntkyTIj86oM4mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f56a780504.mp4?token=LmLH-rg4tglwZJY5T-kIfu1LF5eYkQbD5NjXs6sWuHWuYqh65e5boicciz8d_NXbeLusoPLV4TyXvvBvcVSfdoVLJnLbEi1w_jVzJETwu-8z3kHq7UrkiqOH8_tHhkqfzX69ROy2u8HaBewY2Lt7ONScCx30rWXjAlL9IYgEcyUwzCx-VV7xCimGKS09ZBZMzH6Mps9WeG6GVTpb14pRgzMHR2SRQM_Le5LNaIRSsbvUlhQAQWlXidkspMiX2NZQqQ-L2iynvO2rocVBy2ack9NVWKrs4zLETkancT1HgrrAu6PnK4k0KSdg7A-QCWkuf6AwshOPntkyTIj86oM4mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
🇱🇧
عادی‌سازی سقوط تپه علی‌الطاهر توسط طرفداران قالیباف
😂
@News_Hut</div>
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/news_hut/71256" target="_blank">📅 23:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71255">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23e98b62df.mp4?token=Ci3TjndQERCcSAq3WvCxvLiYu3i7AERhqMSjNRk8uuFgaoq1PlnMdNUa7JdaIKJ0k7lsyxrXo1K7tuxKCW_isjx3OIcfLtaEwtHCbBK8A4BDjljl9SNfSieG1pM_eihVLzGBZe1UJsaH-tGA6KGL3qwe38eNlk5yxnKIoyseqd_Il27PS0vOg2NAieLd9-D6N8jc5dZR6k3J1KY_bBh9M9RH3MefJKm0ECATjIgYagk1bm6HypfHHsOfsQGFLr-w627ukqnd7Fgawpe_nKPqjprgBZVXL-JvFgAnFpJGc_Nc3tJjiEmlwsO4F1GZro2Jbj5ytFBlYg_7-G1Zyjj8Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23e98b62df.mp4?token=Ci3TjndQERCcSAq3WvCxvLiYu3i7AERhqMSjNRk8uuFgaoq1PlnMdNUa7JdaIKJ0k7lsyxrXo1K7tuxKCW_isjx3OIcfLtaEwtHCbBK8A4BDjljl9SNfSieG1pM_eihVLzGBZe1UJsaH-tGA6KGL3qwe38eNlk5yxnKIoyseqd_Il27PS0vOg2NAieLd9-D6N8jc5dZR6k3J1KY_bBh9M9RH3MefJKm0ECATjIgYagk1bm6HypfHHsOfsQGFLr-w627ukqnd7Fgawpe_nKPqjprgBZVXL-JvFgAnFpJGc_Nc3tJjiEmlwsO4F1GZro2Jbj5ytFBlYg_7-G1Zyjj8Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
یادی کنیم از اوستاااااد خانعلی‌زاده که در دوره جنگ 12 روزه معتقد بود جنگنده های اسرائیلی هرگز وارد آسمان تهران نمیشن چون باید چندصد کیلومتر داخل ایران بیان و برن و این کار ممکن نیست  و اینا همه شایعات مجازی هست!
@News_Hut</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/news_hut/71255" target="_blank">📅 22:53 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71254">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚫
فوتبال مملکت هم اوضاع جالبی داره.  خداداد عزیزی امشب کلش فوق‌العاده کیری شده و اینجوری خواهر و مادر امید عالیشاه رو به فوش کشیده
😳
😳
😳
😳
😳
@News_Hut – ویس فحاشی خداداد</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/news_hut/71254" target="_blank">📅 22:14 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71253">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
⭕️
دقایقی پیش صدای چندین انفجار از سمت تنگه هرمز شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/news_hut/71253" target="_blank">📅 21:28 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71252">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ead429175.mp4?token=eOdKFzwbcWeAdCaNs3AB0iODX846pwUC1k3kcREaD9nVj3W5bxKiIAkGoJyjPFgIyPHqRAx3kFPLf68DGDibw_bzzYXLEKGH0VEHiTsrnE80wsAeIc-ROFQy3VG0S-_yP8ZZX8nF2A_fU5m_teXmQbLH_MUsYc-mLuTEWPzoqPfJ9DTViwRFK6M_ZGJIt1AHfao1LcFwlsmqbZzl_CGprQnApCh7_X5xFOpvWUR0kB3QCAWNz_6rpoPWXSBgDKh94oh6ze7GfLK4mpEIDImxIsHsGUiw98Tm87yRhfPCTM4bESTPaEI4mtM6VEcwmPOh_cdK_ZRoq23-oGp5XjX4qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ead429175.mp4?token=eOdKFzwbcWeAdCaNs3AB0iODX846pwUC1k3kcREaD9nVj3W5bxKiIAkGoJyjPFgIyPHqRAx3kFPLf68DGDibw_bzzYXLEKGH0VEHiTsrnE80wsAeIc-ROFQy3VG0S-_yP8ZZX8nF2A_fU5m_teXmQbLH_MUsYc-mLuTEWPzoqPfJ9DTViwRFK6M_ZGJIt1AHfao1LcFwlsmqbZzl_CGprQnApCh7_X5xFOpvWUR0kB3QCAWNz_6rpoPWXSBgDKh94oh6ze7GfLK4mpEIDImxIsHsGUiw98Tm87yRhfPCTM4bESTPaEI4mtM6VEcwmPOh_cdK_ZRoq23-oGp5XjX4qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
دیشب خبرنگار لبنانی داشت توی نبطیه گزارش تهیه میکرد که همون لحظه به شکل پشم‌ریزونی اسرائیل حمله کرد به اونجا و همچی قطع شد
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/71252" target="_blank">📅 21:01 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71251">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4a7bd5cfa8.mp4?token=RpO1CxxFbZ7pB_DbG7QVdtw2-arfS7ZMWEGsz7QSzVDwKcDTD_dLjF4r12A-S1uHetO97Gh16kYqYfpYkgqHRHWtQ_g1mqG9NBCpfV3I7MnYDMTxvj2GWBca76TwwVHQ6fw7dvZ4oKCylcS7z-xsQfS1eV1lgVhEbU1M4hMSRXVjDsYk0ZTv-FcBFSmTaFeaoNTo_lhIk8eqZWIfIppzTVH5HR5eJMemOMyNYqWKRkC_AjE9j7z08yu2egFbUrRc_memo3KnDIaSBCb33TAIlBaPAj2ncfuXWPzSEhkZJgVukysbu2j_-FbZt961ggtVv12aYPLZC24zoA3gEx1IAAYNoe5DoRy5p3O0rD8LZ-moaFRcl1hd7zT5xUJce9XA1H_CcR8Vx0KPqXV9_0NwZK5AkNsoatM97h_fAIb20dkpGeZKvdSDFylsnIHJN9O1vtiKmP7d1AU3LwFkoLE3NBGExI--c3wpVPQJoD75WBluH3IcaytMb1hoN2-x9u6nY8xlKpoClrKL6j2EWf_iYPlmbw4Ftadf0xuwt_-SY5CHCeIw6MJuuNq87FqI4ORAd526S-T8BJg6EG7XpFF7yX1YAItB5HQKLtvgkv8TjJusXF7kFN_EH3OaJ6AKhVaPSBKvpSC2-IpAYb_9XCMBD6RVdWtd-LLqjCm8AbDplX8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4a7bd5cfa8.mp4?token=RpO1CxxFbZ7pB_DbG7QVdtw2-arfS7ZMWEGsz7QSzVDwKcDTD_dLjF4r12A-S1uHetO97Gh16kYqYfpYkgqHRHWtQ_g1mqG9NBCpfV3I7MnYDMTxvj2GWBca76TwwVHQ6fw7dvZ4oKCylcS7z-xsQfS1eV1lgVhEbU1M4hMSRXVjDsYk0ZTv-FcBFSmTaFeaoNTo_lhIk8eqZWIfIppzTVH5HR5eJMemOMyNYqWKRkC_AjE9j7z08yu2egFbUrRc_memo3KnDIaSBCb33TAIlBaPAj2ncfuXWPzSEhkZJgVukysbu2j_-FbZt961ggtVv12aYPLZC24zoA3gEx1IAAYNoe5DoRy5p3O0rD8LZ-moaFRcl1hd7zT5xUJce9XA1H_CcR8Vx0KPqXV9_0NwZK5AkNsoatM97h_fAIb20dkpGeZKvdSDFylsnIHJN9O1vtiKmP7d1AU3LwFkoLE3NBGExI--c3wpVPQJoD75WBluH3IcaytMb1hoN2-x9u6nY8xlKpoClrKL6j2EWf_iYPlmbw4Ftadf0xuwt_-SY5CHCeIw6MJuuNq87FqI4ORAd526S-T8BJg6EG7XpFF7yX1YAItB5HQKLtvgkv8TjJusXF7kFN_EH3OaJ6AKhVaPSBKvpSC2-IpAYb_9XCMBD6RVdWtd-LLqjCm8AbDplX8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سردار محمودی بعد مصرف یک بَست:
موشک رستاخیز ایران می‌تواند در لحظه اصابت ۸۰ کیلومتر مربع را نابود کند
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/71251" target="_blank">📅 20:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71250">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bVVqDhP_ozVdC7RuN_qkpNJEkhgtzu6AYGnfs738l9UG4vxUbuZhQ51Q3n-5tuLW2ID_Voq8DhXDsbd6fKP0BF-WCqARWDpKrZ4z8uulAJkdi948ajNrZ7krcAoQx9xwHXZ6u2tbLwzFShZZPp9vyj2wkTUwzkn-Hcn-Io7RhjFDe2SsuQQkFj9j3Nbl4-zBx3K99hEGAhtISVZO1nlo8ccxfFPynZ97yIfQ5R7AVFLmWMSYjWB6rwwTnkqwUZ9WsP3yAde92gyUyu2uNC5U1ob3luwhvA45cUxLov72Jeyxha6HkNhsKTXXIYxd9IwZClQ_y7pJFLiWwXNfHHElCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">〰️
🇺🇸
ترامپ بازنشر کرد:
سیاستمداران ارشد ایران خواستار پایان دادن به جنگ هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/71250" target="_blank">📅 19:31 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71249">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/807f8a83aa.mp4?token=Eo8H6C9C7b71TDDnIVLsRsFzHTVJc-tKEF8Y4Cn4EXyVvYHZtRo47qGBSyv1eEZ-PgfWiFEmiHS0EhiJOvmAjmQSH51n6X5rQu9gt9s7u4P5y8miZ-zkC2XxJXvZLb1nWiof1LseR5H7gOIJGJ1NSR3jkZk05WuAox14WWoe1RQTYuokGTmxLBJWMhzhIfLShkK8TWzp5jrl5ZcCW0jdU3gXWhw04IAeHOWp8L1tqykgwbrusSbDcxBR8QJOt5TObp2rnzqdIkl7Aty4fJkRXBKkKGj0x3s4gHhLc7PXoIXMgk0b0u446-0l9FDfBg6DDPcwmxUMuCXhbSFrIEGDAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/807f8a83aa.mp4?token=Eo8H6C9C7b71TDDnIVLsRsFzHTVJc-tKEF8Y4Cn4EXyVvYHZtRo47qGBSyv1eEZ-PgfWiFEmiHS0EhiJOvmAjmQSH51n6X5rQu9gt9s7u4P5y8miZ-zkC2XxJXvZLb1nWiof1LseR5H7gOIJGJ1NSR3jkZk05WuAox14WWoe1RQTYuokGTmxLBJWMhzhIfLShkK8TWzp5jrl5ZcCW0jdU3gXWhw04IAeHOWp8L1tqykgwbrusSbDcxBR8QJOt5TObp2rnzqdIkl7Aty4fJkRXBKkKGj0x3s4gHhLc7PXoIXMgk0b0u446-0l9FDfBg6DDPcwmxUMuCXhbSFrIEGDAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
به تازگی یه چیزی مُد شده به اسم «جوجه پارتی» ، تو این پارتی، پسرا رفیقای دوس دخترشون رو به همراه رفیق سینگلشون به این پارتی میارن، تا برای همدیگه جوجه بکشن و از سینگلی در بیان.
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/71249" target="_blank">📅 19:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71248">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v7Fsbt5DhlEU0CQnt0liXa0TExIFRd3H4cSre3bpHnzfol1hTnGnMMbc7xgICEOUoqnSBX8O2hDt_h4HhFveJGWVCYnA2dpQbQOj8HSawF331MVUG4NyOf4LIRsuTnqFdpQeFVQC9ZKQZ2Eko9ECCnJ21xJIddOg2dOnALg2sBDIpxc-57_EMwglJQQ5YNuanBZ-2j_5QPWUzqBykLWucjolJQEcz_cF5q2jQuDNlzNR1XlBc6rIKj01Mzr959fqQGYOrJU0W6pqixFlifvRmP3ySvOgBcxUnQGe3IkSlM5dZ2Sd2hWQJLkK9vrtC0GtiGp957ge2T5PlbodFuOswg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه موضوعی هست که فکر می‌کنم تقریباً همه ما به‌نوعی باهاش درگیریم؛ هزینه و شرایط بنزین.
شاید خیلی‌هامون هر روز درباره‌ش صحبت کنیم، غر بزنیم یا فقط سعی کنیم با شرایط جدید کنار بیایم، ولی در نهایت چیزی تغییر نمی‌کنه مگر اینکه صدای تعداد زیادی از مردم شنیده بشه.
برای همین این کارزار راه افتاده تا نظر و درخواست مردم درباره این موضوع جمع‌آوری بشه.
من خودم اینو امضا کردم و فکر می‌کنم اگر شما هم با موضوعش موافقید، چند دقیقه وقت بذارید و امضاش کنید. حتی اگر فکر می‌کنید یک امضا تأثیری نداره، همین امضاها وقتی تعدادشون زیاد بشه می‌تونن نشون بدن که این موضوع برای تعداد زیادی از مردم مهمه.
اگر دوست داشتید، لینک کارزار رو برای چند نفر دیگه هم بفرستید. شاید همین کار ساده باعث بشه افراد بیشتری از وجودش باخبر بشن.
🔗
https://www.karzar.net/346254</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/71248" target="_blank">📅 19:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71247">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71247" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/news_hut/71247" target="_blank">📅 19:29 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71246">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U9O_z4L2kLBpxHvcnS4uXdONI7YaDYJYeu6cjjJCRl8pRCFPsSYfRqk-V8plpgMHnLFHUjmOWtPOpsdHGxPU1ZSFPxuckLnxNfbGQ_mJDPOVAHDyy6Pk3yr-E2q-uRaM6SCQVJ272k5F-fAdQzPek-O39uspOMuJkQylEkM4vrCaMWH8D7coGbUhrtD3As7D3TiD0g8nlVVkHi270bmdnL6eZDD0KlcjRjPcw2QkdcfpBPtWy77j3esCdynMcqTcpzfwCxZNcbiwReqOe0FgnR9MMoJ_w3yVo2S3Bne_MATQh3XhBxsWDZEl5tcA9_Ff3En5xVzqQXYUtcv0MdQI9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
آماده‌ای هیجان واقعی رو تجربه کنی؟
🦖
در
TrexBet
، دنیایی از اسلات‌های جذاب، بازی‌های کازینوی زنده و لحظه‌های هیجان‌انگیز منتظر توئه!
🦖
صدها بازی متنوع
🦖
تجربه‌ای سریع و روان
🦖
هیجان در هر اسپین
🦖
🦖
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/news_hut/71246" target="_blank">📅 19:29 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71245">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">▶️
🇱🇧
🇱🇧
این ویدیو رونمایی شهر موشکی عماد است که مو به مو طبق شهرهای موشکی و پهپادی سپاه پاسداران ساخته شده؛
دو سال پیش حزب‌الله لبنان از این شهر موشکی زیر کوه‌های علی الطاهر رونمایی کرد.
جمهوری اسلامی بیشتر از خود حزب‌الله لبنان خرکیف شده بود؛
از برنامه ثریا تا اخبار سراسری صداوسیما تماماً افتتاح شهر موشکی عماد با ۴۸ کیلومتر تونل بود که مدعی بودند ساختش چندین سال طول کشیده و اکنون تسخیرناپذیر و نفوذناپذیرترین دژ عالم است.
این شهر پس از سه ماه محاصره توسط ارتش اسرائیل سه شب پیش در سکوت خبری تمام رسانه‌های جمهوری اسلامی سقوط کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/71245" target="_blank">📅 19:01 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71244">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c892ca398.mp4?token=BkVvp0DMCbonYMbCXQEdB3JFc7lFvjEMi54HCXya7b4hFFufmiUf0HX6VEnvn8h6FH5Ox0UYbh93PEcPBhkBEYPJNrYo0VZkCHT3w7FYKTFR0yI1p9I0K-L_pNy3EGCn8w80k61R7R8QpnxzySuGO1jph6Mb1fZYay_9xY_i8pq9Jz6BQHQ6gK0bhJTLtq3kpCqXEF0l-S5BSmTpIFornnnwhHBbHGFsdIYlUCuHMz8cX5Y6whYXCrd-IjCgTQEYzjpFPLpXhx7UVSiOiigqhqy8bcqNigt4dUOJa2vPvCyOrx6UkbjzlPerthtwD3QvsA-kgd_1wS4bfpGMwUP72w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c892ca398.mp4?token=BkVvp0DMCbonYMbCXQEdB3JFc7lFvjEMi54HCXya7b4hFFufmiUf0HX6VEnvn8h6FH5Ox0UYbh93PEcPBhkBEYPJNrYo0VZkCHT3w7FYKTFR0yI1p9I0K-L_pNy3EGCn8w80k61R7R8QpnxzySuGO1jph6Mb1fZYay_9xY_i8pq9Jz6BQHQ6gK0bhJTLtq3kpCqXEF0l-S5BSmTpIFornnnwhHBbHGFsdIYlUCuHMz8cX5Y6whYXCrd-IjCgTQEYzjpFPLpXhx7UVSiOiigqhqy8bcqNigt4dUOJa2vPvCyOrx6UkbjzlPerthtwD3QvsA-kgd_1wS4bfpGMwUP72w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی از لحظه فاجعه انفجار تانکر حمل سوخت در سنندج که باعث مرگ 11 نفر شد
@News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/71244" target="_blank">📅 18:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71243">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08df0f1761.mp4?token=JYb0JcABkRLu-zFhAciCJM4qAR__wdD4ovCFkNGvfqfsDjZSk83bipKXFrv2X9qDF0bSGDyrVLPvUaGQxkZL0og1zBolfdRcBiYTag_wjNUhvGUWZKbU4gkeVT-QmgW2PGqKMdffwfxYOx81AixaFdLy9rHWotj5pD9dqmhSDX4G2XYfwSkT-NMBeLNPAPCn_IdF-QUhlRM0yUTpEWfDoJtuPAQJGqIi5lZW_lMORjs4mLU1aRnikRCe6v7c7zyC5tNJkLUoXQcEfi7sA4VaPS__9-0DtoOKB5jsh7xpQujKVDrmt9WTwkg5oLEEiw6lQ59jlBJPDMvjNWDZ2Z-VtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08df0f1761.mp4?token=JYb0JcABkRLu-zFhAciCJM4qAR__wdD4ovCFkNGvfqfsDjZSk83bipKXFrv2X9qDF0bSGDyrVLPvUaGQxkZL0og1zBolfdRcBiYTag_wjNUhvGUWZKbU4gkeVT-QmgW2PGqKMdffwfxYOx81AixaFdLy9rHWotj5pD9dqmhSDX4G2XYfwSkT-NMBeLNPAPCn_IdF-QUhlRM0yUTpEWfDoJtuPAQJGqIi5lZW_lMORjs4mLU1aRnikRCe6v7c7zyC5tNJkLUoXQcEfi7sA4VaPS__9-0DtoOKB5jsh7xpQujKVDrmt9WTwkg5oLEEiw6lQ59jlBJPDMvjNWDZ2Z-VtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗣️
طبق قانون، استیکر و گیف خنده داری که از رفیقت میسازی جرمه...
و میتونه ازتون شکایت کنه و تا 1 سال حبس و 5 تا 33 میلیون جریمه نقدی داره.
اینکه شوخی بوده هم هیچ تاثیری تو مجازاتش نداره
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/71243" target="_blank">📅 17:31 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71242">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff06303045.mp4?token=kN4d7eCpzXuKwUBqmhbmcv5gb4vjcr3IVgn75zrR8E0Bt4sEc1hDzd00ISyAnLSI7AoG-vtTENzujRrwHZFCp2ARYjg5aM7h94Zm9uXx-4ELAuTK1Lv5vmHf5IozxwEEggn9cEShJObUuWhU9-doSbaSb1eJupGno-A6_wmWd9hCf_44w0v0PX5uws8oK89yRd58xQixTonK6nqiHiqEfEC1_U3i2r4lr3lcx_cNHtxtggAmBhVJHKynRAyrpVZc7vhcBN2IqLuHI0UZSx5c2G3RMRM7SFP5hNV8qvJi1ZcQ90Q-l3WI0T79X6dnLBcQz3bM80lHaTePhEV4GngAGQ_g0-fO4BSDnQAh3ENkAJJWpy692b-CIGM46Oxdyc1aM9M71aID0ELElmaw6HPhaE4m78l-oPYZAxgLSsyEOrbe51M8_WJtFjV1YruPqdelPFfk6F_y89v3E2CrHrwdKojEdlvnziXxV4NOnvM7LA4nd8hVF8Bu1UW1YAs9_BMOzT4BsZr6GfF0ch9u2RXCtSLJ5E4StJ5dBffGeVCe3XZkMpwBBU7lYaJ0ko4mbuu02L1zuE_W7Wkt_kYOZdy6iFgc78DhWvwBtyEIvwKy4ybNCxOsZnTFaOxdPzIeUhhe0yiPNpliEwQG8LIeJSz34XeHqf5ke26xDoWalXMeQio" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff06303045.mp4?token=kN4d7eCpzXuKwUBqmhbmcv5gb4vjcr3IVgn75zrR8E0Bt4sEc1hDzd00ISyAnLSI7AoG-vtTENzujRrwHZFCp2ARYjg5aM7h94Zm9uXx-4ELAuTK1Lv5vmHf5IozxwEEggn9cEShJObUuWhU9-doSbaSb1eJupGno-A6_wmWd9hCf_44w0v0PX5uws8oK89yRd58xQixTonK6nqiHiqEfEC1_U3i2r4lr3lcx_cNHtxtggAmBhVJHKynRAyrpVZc7vhcBN2IqLuHI0UZSx5c2G3RMRM7SFP5hNV8qvJi1ZcQ90Q-l3WI0T79X6dnLBcQz3bM80lHaTePhEV4GngAGQ_g0-fO4BSDnQAh3ENkAJJWpy692b-CIGM46Oxdyc1aM9M71aID0ELElmaw6HPhaE4m78l-oPYZAxgLSsyEOrbe51M8_WJtFjV1YruPqdelPFfk6F_y89v3E2CrHrwdKojEdlvnziXxV4NOnvM7LA4nd8hVF8Bu1UW1YAs9_BMOzT4BsZr6GfF0ch9u2RXCtSLJ5E4StJ5dBffGeVCe3XZkMpwBBU7lYaJ0ko4mbuu02L1zuE_W7Wkt_kYOZdy6iFgc78DhWvwBtyEIvwKy4ybNCxOsZnTFaOxdPzIeUhhe0yiPNpliEwQG8LIeJSz34XeHqf5ke26xDoWalXMeQio" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇷🇺
🇰🇵
روسیه و کره شمالی یک پل جدید را در امتداد رودخانه تومن افتتاح کردند. این پل دو کشور را به هم متصل می‌کند و با گسترش همکاری‌های نظامی و اقتصادی این دو کشور، اهمیت این اتصال نیز افزایش یافته است.
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/71242" target="_blank">📅 17:05 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71241">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c8cf25fef.mp4?token=mKxyLRE9V4th-pN-3TZciGbjvVBwBXZYU93gYXmTDRKl6wDwuTh7XMP3js2H874bQp64fHSilxBhZFmwT8_pr8VQDjRpPiDvlvA6y8mtWJUEpJbG0dckkPBn8PzKtPzim7GAW8D0-1GQ4xfvJJFC2lNkwXKmh4F-GlP6Y_VFidsPlwKyMb1uOikrYO5vCpXeZjIJaUCY9aoMnXZNFO5_7I3iQl5xbfqR-W4EpPzHVGe3AdZy3hYM1FTKqTWm-Wl_ponN2NDCeO_DMawBOkO2dPahotMS0msNfQCMQfc7-IoBZ_HjnrzgJRCkr1R8bOLGekj6JojZ1_yvTXwmBMgJHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c8cf25fef.mp4?token=mKxyLRE9V4th-pN-3TZciGbjvVBwBXZYU93gYXmTDRKl6wDwuTh7XMP3js2H874bQp64fHSilxBhZFmwT8_pr8VQDjRpPiDvlvA6y8mtWJUEpJbG0dckkPBn8PzKtPzim7GAW8D0-1GQ4xfvJJFC2lNkwXKmh4F-GlP6Y_VFidsPlwKyMb1uOikrYO5vCpXeZjIJaUCY9aoMnXZNFO5_7I3iQl5xbfqR-W4EpPzHVGe3AdZy3hYM1FTKqTWm-Wl_ponN2NDCeO_DMawBOkO2dPahotMS0msNfQCMQfc7-IoBZ_HjnrzgJRCkr1R8bOLGekj6JojZ1_yvTXwmBMgJHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
معاون وزارت ارتباطات :
حتی تو شرایط جنگی هم اینترنت قراره برقرار بمونه و همین که الان اینترنت وصله، نشون میده حاکمیت تصمیم جدی داره دسترسی مردم به شبکه ارتباطی کشور حفظ بشه؛
اینترنت پایدار و باکیفیت جزو حقوق اولیه مردمه و خدمات ارتباطی باید ادامه داشته باشه.
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/71241" target="_blank">📅 16:31 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71240">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a6ea773c3.mp4?token=f0_VPEkIvuKgWfX-UzLOP_x1rhsOUSg8KOqJ1z1eYP8OAheNfNEMf-7HKoul764q_F2D8WDHmykubhnPEypc4Wb5-adOdjhArBVeuNk0N3ynJEuAOJTY2l96ogo_5ZPRdsakTVg7irPwjxt86mqIrcgdFYm82raLVWWK-EzSJmPdWEDblgt-ZTG9o9oaNGN9dOI_nDFmaQ6KBpF3EaOSd3uV0RPHH8jPa2mWb_iHeTpE12jr-VTk4dLxMitnHstC88q73syEoRzu3pLi97dAYtsqsL5cgfbJivJKpbWS-USC48GOW9QcrpiHZP1g27CSDUsqj-NdQ-usZyG4EZhbOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a6ea773c3.mp4?token=f0_VPEkIvuKgWfX-UzLOP_x1rhsOUSg8KOqJ1z1eYP8OAheNfNEMf-7HKoul764q_F2D8WDHmykubhnPEypc4Wb5-adOdjhArBVeuNk0N3ynJEuAOJTY2l96ogo_5ZPRdsakTVg7irPwjxt86mqIrcgdFYm82raLVWWK-EzSJmPdWEDblgt-ZTG9o9oaNGN9dOI_nDFmaQ6KBpF3EaOSd3uV0RPHH8jPa2mWb_iHeTpE12jr-VTk4dLxMitnHstC88q73syEoRzu3pLi97dAYtsqsL5cgfbJivJKpbWS-USC48GOW9QcrpiHZP1g27CSDUsqj-NdQ-usZyG4EZhbOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
آخوند قاسمیان:
برادران یوسف 11/11 وحدت کردن یوسف رو انداختن تو چاه، این که وحدت نیست، وحدت باید حول محور رهبری باشه..
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/71240" target="_blank">📅 16:03 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71239">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/98f065761f.mp4?token=jHCDmYZkfs-LxY5IonANWtGG1T0fnj9kXgOL9OD1brZIbjUbpwRioTYExs03EbJHVaaI6y-csNTnrqC24jwwhr6dxpsfgu2ID6003oNgId0hk5szXOvUawMHygQN8W5c892FNTB3frvMyxd3qQ7ixrKoCxTotYn2P5jiJu1YpERuDc1PI0TV05INIzuNLZAERjhS_DqrDZVSQ7noLrkGotac6qWVXbaaBKcC7O-IM0DIq2W8PZC4JZfW7xyhkT9NdIANZjTj4d6NSvInIy5FsPEKLbFg6nOhWlstZ4lweFChCD-dqnSeSS4JJPZ_ro_IhFRnDbbmDn04Mb7q_pXwNw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/98f065761f.mp4?token=jHCDmYZkfs-LxY5IonANWtGG1T0fnj9kXgOL9OD1brZIbjUbpwRioTYExs03EbJHVaaI6y-csNTnrqC24jwwhr6dxpsfgu2ID6003oNgId0hk5szXOvUawMHygQN8W5c892FNTB3frvMyxd3qQ7ixrKoCxTotYn2P5jiJu1YpERuDc1PI0TV05INIzuNLZAERjhS_DqrDZVSQ7noLrkGotac6qWVXbaaBKcC7O-IM0DIq2W8PZC4JZfW7xyhkT9NdIANZjTj4d6NSvInIy5FsPEKLbFg6nOhWlstZ4lweFChCD-dqnSeSS4JJPZ_ro_IhFRnDbbmDn04Mb7q_pXwNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ایشون رو آورده بودن موقع زایمان پیش زنش باشه و بهش روحیه بده، آخرش دکترا مجبور شدن خودشو درمان کنن
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/71239" target="_blank">📅 15:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71238">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f53489458.mp4?token=pJYVHrmZtduj0mc7eMHCS67-r37Yfzcx9efSO-R6Ir3apt-rhOyVBrJjlJqlhjZeaK-uj-dQGZ-hd6gwqWkBOz2Jykp5shOf9_aGnU_xGziy-Pz0skFG_-0AoQV24o6eMPbNLedgYsv5BNCB67082H8Uf88s7m6HgYjgmpciyEurUr9x3A59z2l9WrEBecMRfRylqhQf21tVd-Sy4qlO1W9wYT0ahVgQiW0d2snu4RRFL5Dqp12kM46K1vt4ratgM9tT3TMGCG0SLeqmlNteJopvUiwFh8kGBc79vLAi4t1frGsPH6_yaNmXrHek3gGyBbbnXnX4dioS01QFl_mJpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f53489458.mp4?token=pJYVHrmZtduj0mc7eMHCS67-r37Yfzcx9efSO-R6Ir3apt-rhOyVBrJjlJqlhjZeaK-uj-dQGZ-hd6gwqWkBOz2Jykp5shOf9_aGnU_xGziy-Pz0skFG_-0AoQV24o6eMPbNLedgYsv5BNCB67082H8Uf88s7m6HgYjgmpciyEurUr9x3A59z2l9WrEBecMRfRylqhQf21tVd-Sy4qlO1W9wYT0ahVgQiW0d2snu4RRFL5Dqp12kM46K1vt4ratgM9tT3TMGCG0SLeqmlNteJopvUiwFh8kGBc79vLAi4t1frGsPH6_yaNmXrHek3gGyBbbnXnX4dioS01QFl_mJpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ویدیو وایرال شده از یکی از معلم‌های مملکت :
اگه مدارس امسال مجازی بشه، از گوشیِ شخصی‌ام نمی‌تونم استفاده کنم.
چون پارسال 4 تومن گذاشتم رو حقوقِ 14 تومنیم و این گوشیِ 18 میلیونی رو خریدم.
امسال همین گوشی 70 میلیون تومن شده!
حقوق من چقدر شده بعد ده سال تدریس؟ 20 میلیون تومن...
اگه این گوشی من خراب بشه، دیگه نمی‌تونم گوشی بخرم.
آموزش و پرورش باید به فکر تهیه وسایل آموزشی (گوشی و لپ‌تاب) واسه معلم‌ها باشه.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/71238" target="_blank">📅 15:01 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71237">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">‼️
این خانم ادعا می‌کنه که در جزیره اپستین بوده؛
صداوسیما هم صحبتاش رو پخش کرده.
ادعا کرده که به کل جزیره تجاوز کردن و شرایط بدی بوده.
بعد میگه خداروشکر فقط خودم مصون موندم و بهم تجاوز نشد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/71237" target="_blank">📅 14:32 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71236">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c603211e44.mp4?token=XEX2PU3dDdyqenO9jn2AClVltmD8OjLGc9EA1vPduK__Nl1PBC7512WbVLPPWOWUflJ5GxeboOyluHbteLYPDG_4yD6dCe891-M-f_jMoNxIv2hphEs53508yYoyTRvoUIXCeu1Ag5djCWsYE8VQzMwS2WQj0J8llSy459CpENmI4xa6dIWhorB2_Z-7hz3bzaP-_-uhHeb2xBKoRxSoTFame-sHP_UTjG_nG3MMxjD_qkiPB4QOWnjVX0vaz9r6TaA1AxalCTUgECGfO6xocwkQ3q6yTZ327-x-iFEX5usBRpgshB7DyKwzqLCvq8Cua7f4PqxzLfjrLvVIo-OFvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c603211e44.mp4?token=XEX2PU3dDdyqenO9jn2AClVltmD8OjLGc9EA1vPduK__Nl1PBC7512WbVLPPWOWUflJ5GxeboOyluHbteLYPDG_4yD6dCe891-M-f_jMoNxIv2hphEs53508yYoyTRvoUIXCeu1Ag5djCWsYE8VQzMwS2WQj0J8llSy459CpENmI4xa6dIWhorB2_Z-7hz3bzaP-_-uhHeb2xBKoRxSoTFame-sHP_UTjG_nG3MMxjD_qkiPB4QOWnjVX0vaz9r6TaA1AxalCTUgECGfO6xocwkQ3q6yTZ327-x-iFEX5usBRpgshB7DyKwzqLCvq8Cua7f4PqxzLfjrLvVIo-OFvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
فیلد مارشال محسن رضایی
:
چهل‌هشت ساعت پیش اولین موشک ناوشکن خودمون رو بالای سر یه ناو آمریکا تست کردیم
واقعاً یک جهنمی به وجود اومد.
🎙
مجری:
موشک بالستیک؟
🇮🇷
محسن رضایی:
موشک خاص حالاااا. موشک خاص
😟
ناوها فرار کردن.
حادثه آنقدر بزرگی هست که سنتکام هم نتونسته نفی بکنه. اعتراف کرده به این
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/71236" target="_blank">📅 13:49 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71235">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rJyodev9TSJbtqRTnbqYvVmfkNaneD70bSld43KH2OdEdt8d3YO0UgbqZ-p4gjw-NjgTg_yceNiQwtKpXOgB5olDjuTJnaIizjxnl7IHH5UYeMES0XDDxjGp7xCLZT7xW2oaLd0EmmO6CFW5ZQRLLgoc5FHe7qGTWAxnxFETHy4gSqz_ykDgLlBSz63SlIqBMHkIRacRPP1LKX0ToQVgreatfEp8HnsmpZiCjlpoCjALoVNPM2BP9H_ntdkfujWirjMdTWUnu_ikk8wXyy3W69ryEGYNB05fpc6axwC49cDbmGaLyWFs2PRTE_5Z_i9u81PjAuIIKvFFxC2WqAdipg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
⭕️
🇺🇸
👀
افزایش شمار هواپیماهای سوخت‌رسان آمریکا در شبکه مرتبط با عملیات ایران
بر اساس نقشه OSINT منتشرشده توسط DefenceGeek در ۷ سپتامبر ۲۰۲۶، مجموعاً ۱۹۵ فروند هواپیمای سوخت‌رسان KC-135 و KC-46 در شبکه مورد بررسی این نقشه ثبت شده‌اند.
⭕️
جزئیات این آمار:
۱۶۶ فروند KC-135
۲۹ فروند KC-46
مجموع: ۱۹۵ فروند
این نقشه پایگاه‌ها و نقاط مورد استفاده برای مأموریت‌های تانکر در مناطق تحت پوشش CENTCOM و EUCOM را نشان می‌دهد و علاوه بر پایگاه‌های فعلی، برخی پایگاه‌های مورد استفاده قبلی و مسیرهای ترانزیتی را نیز دربر می‌گیرد.
در نسخه فعلی، تعداد KC-135 نسبت به آپدیت قبلی(3 اوت۲۰۲۶ منتشر شده) ۷ فروند و تعداد KC-46 ۲ فروند افزایش نشان داده شده است؛ بنابراین مجموع ثبت‌شده ۹ فروند افزایش داشته است.
منابع مستقل نیز در سال ۲۰۲۶ از به‌کارگیری گسترده تانکرهای KC-135 و KC-46 برای عملیات مرتبط با ایران گزارش داده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/71235" target="_blank">📅 13:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71234">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kjnQmBBEp_55Q2TdX4Q5aeRiaVgBMQMDakOA8C-_MaxFMFA5o76i329RT4d6eLdR0ZxshXY1gMhkWr1hdVf6D_btpgbC6EsvtnNkTytL_N-ogIte6wWe_OqBV_R-LIoS9sJPr2XljfLLaXLaAYvLpahbYtivWeJnCGpgmGv0U9_qsRHnlvXhJV0cWmmd7yjy2klMRbW3BpGRDDzn0xcNyRNcDlnIH5WvXIKBnBKmgodDHfMApJX-W0iLpYQ_Sk3FBkuvT71oxzCL8lng91BxRSQP4ROiDkV2-jGPrmRVjGMYEA8H-JShtGVd9u1ivoqE_LTMLfFcqDfX9zNwAw6QtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قالیباف:
موضوع ساده است: زنجیره تولید نفت و گاز در اینجا گسترده، در دسترس و آسیب‌پذیر است.
شرکت‌های نفت و گاز آمریکایی که در این آب‌ها و تأسیسات حضور دارند نیز در معرض همین آسیب‌پذیری قرار دارند.
به دارایی‌های ما حمله کنید، ضربه خواهید خورد. ما پیش‌تر این را ثابت کرده‌ایم؛ از پایگاه‌هایی بپرسید که دیگر کارایی ندارند.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/71234" target="_blank">📅 12:46 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71233">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9570398f5.mp4?token=C5-M5xZfIvisoXI4NAiE3-lrFjUDoiSYBk0IOzEfkv_8_e3sziRIsObaGBkSqFDFCtI9GRt26qdaDGT3GYZqlRQAhlO2U9UFBd7LLs5_7DXm_0yt2yvvaWKWDjf5IAV2m-UH1HhR6gpQRSNWmUXrvq-Zl0KqrUEfyC4yiieEVJ1NF_iCyhzVII3dmwjGEYxlje7GSMUCGCIikcLi4n-VAFo0pOliVva0j5mnhHyv4feXEJiXqlUu7wqHEGG529HDw0isXxWfDUpYWhJrTPsLVAfGCwp1Qe7SQo2GLnj8RgG-YNkLEsg2Uo2kuTXaQv1_j5QkdCOQw5ru3_5Lv72ghw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9570398f5.mp4?token=C5-M5xZfIvisoXI4NAiE3-lrFjUDoiSYBk0IOzEfkv_8_e3sziRIsObaGBkSqFDFCtI9GRt26qdaDGT3GYZqlRQAhlO2U9UFBd7LLs5_7DXm_0yt2yvvaWKWDjf5IAV2m-UH1HhR6gpQRSNWmUXrvq-Zl0KqrUEfyC4yiieEVJ1NF_iCyhzVII3dmwjGEYxlje7GSMUCGCIikcLi4n-VAFo0pOliVva0j5mnhHyv4feXEJiXqlUu7wqHEGG529HDw0isXxWfDUpYWhJrTPsLVAfGCwp1Qe7SQo2GLnj8RgG-YNkLEsg2Uo2kuTXaQv1_j5QkdCOQw5ru3_5Lv72ghw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
بمباران آخرالزمانی پادگان فتح خوش‌نام کرج توسط جنگنده های اسرائیلی در جنگ ۴۰روزه
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/71233" target="_blank">📅 12:45 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71232">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71232" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/71232" target="_blank">📅 12:44 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71231">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p94bvqQKm_pOqXURIopkPXLDV85Jx2hv7UAwEYWzr_Vzm-4iHMs4Rm8ZD8CnN_4KtRbsflVCDLnwGAsfw1rEC7z7gwRF3lGu8nIlJby3I_7e3EAoZnRNL8rX-DEVfxwXAI0ccu9mxFGoZeAtjkn3XeK3WXnp7m7C05F5MVEB2_vQyxcoiMxFrXvDg0YR4zuwPDBIEIGUSb776ZytYVvDa9Drv2ckrmC0qFWz3WF2gCOjfLWyAPcvEiPOpyXHzyutJLuoYBaOTAC_5zO8Ijq2TjzFuc3o4rLUNXGvg9VixCHKWDX7CXO--ogbzFXLk3pfPlgWhnqh8gs0Goc0eOWLSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
بازی جذاب
⚽️
ذوب‌آهن
🆚
پرسپولیس
⚽️
را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید.
📊
نگاهی
به آمار ۲ تیم در در این فصل
ذوب‌آهن: ۵ بازی ۱ برد, ۳ تساوی، ۱ شکست
پرسپولیس: ۵ بازی ۳ برد، ۱ تساوی، ۱ شکست
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/71231" target="_blank">📅 12:44 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71228">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6953e87af5.mp4?token=kUb-8VXwaBRDoD5SYvNrRyxHtR8r8vymk0Qdk-fLaMr9V8V7OGiLVEfMYYkFm0fEc8QUnHdzJ4C4-3Otxf_sPozTmz1SjqbjFYLdVepVsfSAkhuP1dwEwrsnl-sWbgaiHDh61idtfjqUqucqWQeRkepqoM2Xalyxo9-U_cm1wOr0abkgtdSksgVYrE1b9-GP8KlkefhmRTCgeY6qbm3c-YPhOGpXG8Ofs_zKKn4YGsWjCX1qFWRFD0k5fwOULoZyET03Rk3own8P11ufl272ih1Rmall6uqR0LhpHk7xRNtAZU9zHQHgVK6nDdeyf4zHXcD2LHqkKmytlAFaA8PPog" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6953e87af5.mp4?token=kUb-8VXwaBRDoD5SYvNrRyxHtR8r8vymk0Qdk-fLaMr9V8V7OGiLVEfMYYkFm0fEc8QUnHdzJ4C4-3Otxf_sPozTmz1SjqbjFYLdVepVsfSAkhuP1dwEwrsnl-sWbgaiHDh61idtfjqUqucqWQeRkepqoM2Xalyxo9-U_cm1wOr0abkgtdSksgVYrE1b9-GP8KlkefhmRTCgeY6qbm3c-YPhOGpXG8Ofs_zKKn4YGsWjCX1qFWRFD0k5fwOULoZyET03Rk3own8P11ufl272ih1Rmall6uqR0LhpHk7xRNtAZU9zHQHgVK6nDdeyf4zHXcD2LHqkKmytlAFaA8PPog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🇮🇶
#فوری
؛ بیش از ۱۵۰ ایرانی به دانشجویان عراقی در سمنان حمله کردند.
🎙
به نوشته خبرنگار بغداد الیوم در سمنان:
گروهی که این رسانه تعدادشان را بیش از ۱۵۰ نفر اعلام کرده، به محل اسکان دانشجویان عراقی در دانشگاه سمنان حمله کرده‌اند.
گزارش ادعا می‌کند پلیس پس از اطلاع از حادثه به دانشگاه رسیده، اما هیچ‌یک از مهاجمان را بازداشت نکرده و صرفاً تلاش کرده درگیری را متوقف کند.
طبق این گزارش، مهاجمان وارد محوطه محل اقامت دانشجویان شده و تعدادی از دانشجویان را به‌شدت مورد ضرب‌وشتم قرار داده‌اند و در نتیجه، شماری از آنها زخمی شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/71228" target="_blank">📅 11:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71227">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6387c174d3.mp4?token=lx-CWXgzRkNJKGXaeHqI-6s78EAbOjZQlvD0anoD54Oic4K2JMYlBbUUVv_DHh-oACJ8K9_wNQ_L9yc6XPHJocPsyeg9CrRWsBk_zzKMmVhxZx4ZlMhOV9VUj_85JCBLrDk0N3tHZugb_GWoJNW1CbrBLXafllkdjP4FxKD6gimdoUMSTsAb0zojHDL1zhstiSKChMVw72BSbVwZQELrR87_hb05d2ZAOmEajHSN8qcVsMoejUwbJFvAMu9DpQ1aGhI6vEA0Oo_trJFDE4t4dYbIp5Ujt3r_vQP2_URKuvEqzyBimykY-ql3DqbeKtxHXonElAaGPlfc2Nm93T08Kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6387c174d3.mp4?token=lx-CWXgzRkNJKGXaeHqI-6s78EAbOjZQlvD0anoD54Oic4K2JMYlBbUUVv_DHh-oACJ8K9_wNQ_L9yc6XPHJocPsyeg9CrRWsBk_zzKMmVhxZx4ZlMhOV9VUj_85JCBLrDk0N3tHZugb_GWoJNW1CbrBLXafllkdjP4FxKD6gimdoUMSTsAb0zojHDL1zhstiSKChMVw72BSbVwZQELrR87_hb05d2ZAOmEajHSN8qcVsMoejUwbJFvAMu9DpQ1aGhI6vEA0Oo_trJFDE4t4dYbIp5Ujt3r_vQP2_URKuvEqzyBimykY-ql3DqbeKtxHXonElAaGPlfc2Nm93T08Kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو وایرال شده از روز انتخابات دانش‌آموزان پایه هفتم آمریکا که این پسره ادای ترامپ درمیاره و مثل ترامپ وعده میده
😳
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/71227" target="_blank">📅 11:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71226">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbb757b4cf.mp4?token=RWmiCUuhcwuuttPcwrtygoGKeNt2LADXxuMKakSU-_CrHQoBU8YEAnSK6Htcg3XVeWbgZOCQdvdVkOtj_jRP6nTgiYZj1Qvb3OnnV5hvBGud_PAISP6Y1ASpH_NQTJK71xyf1FkDXqO8Kp4gfhJtQo5DUI_jfy-8phB41y6ALZMN7LPuKkStVJxjkW1iU4wRXNj7CwtIK5Mx7GZkJlfkPujpD7-Q8yk0HV_KSM6CNxHiOD_35FUbL52X9nBGkjX83Fl1nyMSq17wu1JPCT2VbEpzYVPejgx7VQrjeiPLM7YY_K6j09sltXOJhaZmOldHo-XuGrhXzMGjS59RUKxc7xOlfY3YqTvPdydwii0dsipJOdwcfE0nO5xdQnm53Zl0oekTCgQioAGbK4Toup70ccF3ygrIf8tuFCnEeJaMqAGic6D0nqlbBQLlzHJ08J3-bWm_sCKWcmXkokc-vNuix0Ky-35opzmIGMvD6uV7BqgReM8sbXPetcZlNQGGU9kdAbixmbInnHk-QyF1BJ97f5IAQKdGYE1UchuXBojwsDVYI_86E7z9JfWZqMuCZ70NaRqCVJlUbExBBFReqSclRIhuNFvPa7RUfrG0XZ4SgxM3kyDS4KOm81iCLuwJhqRHsXqw8p1k5qTfFGTl9gZqgQbRx9lkzDlFIdCDrVLX99E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbb757b4cf.mp4?token=RWmiCUuhcwuuttPcwrtygoGKeNt2LADXxuMKakSU-_CrHQoBU8YEAnSK6Htcg3XVeWbgZOCQdvdVkOtj_jRP6nTgiYZj1Qvb3OnnV5hvBGud_PAISP6Y1ASpH_NQTJK71xyf1FkDXqO8Kp4gfhJtQo5DUI_jfy-8phB41y6ALZMN7LPuKkStVJxjkW1iU4wRXNj7CwtIK5Mx7GZkJlfkPujpD7-Q8yk0HV_KSM6CNxHiOD_35FUbL52X9nBGkjX83Fl1nyMSq17wu1JPCT2VbEpzYVPejgx7VQrjeiPLM7YY_K6j09sltXOJhaZmOldHo-XuGrhXzMGjS59RUKxc7xOlfY3YqTvPdydwii0dsipJOdwcfE0nO5xdQnm53Zl0oekTCgQioAGbK4Toup70ccF3ygrIf8tuFCnEeJaMqAGic6D0nqlbBQLlzHJ08J3-bWm_sCKWcmXkokc-vNuix0Ky-35opzmIGMvD6uV7BqgReM8sbXPetcZlNQGGU9kdAbixmbInnHk-QyF1BJ97f5IAQKdGYE1UchuXBojwsDVYI_86E7z9JfWZqMuCZ70NaRqCVJlUbExBBFReqSclRIhuNFvPa7RUfrG0XZ4SgxM3kyDS4KOm81iCLuwJhqRHsXqw8p1k5qTfFGTl9gZqgQbRx9lkzDlFIdCDrVLX99E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طرفداران حکومت یه بازی ساختن که برگرفته از بازی مافیاست و فقط نام نقش ها فرق میکنه.
در این دور از بازیا ترامپ برنده میشه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/71226" target="_blank">📅 11:01 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71225">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecc54f259a.mp4?token=IiATQjNxL22OdKVjCDqxcoxy7bG66vheSXU7J6X5AI1CYTm6m9SmZ9jYXhTPlc_yPsNCOchMDh1flO3-hJyy_bvipUs3bAWrPZAYk0ZjLo8FpWCwXoWSNDe_PmTKbd2aoj9Zk2h5PK-BgPr1wkgBWAELBVj20hud3jg7CccQVM18BzWf3fHobbSuY2B0g5K8fjPXlwjnO1av76tBlOoNLSbnZXrI56mt03UPR-YAyeLZvXRuku8ETWI89hfHqvMs9qQYKsYOVHUQabf79G5T4GJCAWD99Vl6xz2D_plSKFbdB-FD5tRvHoyPA_DcG3txj0UVEfK7Qx2djgkDa-XYXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecc54f259a.mp4?token=IiATQjNxL22OdKVjCDqxcoxy7bG66vheSXU7J6X5AI1CYTm6m9SmZ9jYXhTPlc_yPsNCOchMDh1flO3-hJyy_bvipUs3bAWrPZAYk0ZjLo8FpWCwXoWSNDe_PmTKbd2aoj9Zk2h5PK-BgPr1wkgBWAELBVj20hud3jg7CccQVM18BzWf3fHobbSuY2B0g5K8fjPXlwjnO1av76tBlOoNLSbnZXrI56mt03UPR-YAyeLZvXRuku8ETWI89hfHqvMs9qQYKsYOVHUQabf79G5T4GJCAWD99Vl6xz2D_plSKFbdB-FD5tRvHoyPA_DcG3txj0UVEfK7Qx2djgkDa-XYXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ادعای عجیب یه آفریقاییِ سیاه‌پوستِ ساکن ایران:
خیلی از کاکولدها به پیجم دایرکت میدن و اصرار میکنن که بیا وارد رابطه‌مون بشو و با زنم بخواب!
حتی یکی‌شون می‌گفت هرچقدر پول بخوای بهت میدیم تو فقط بیا..
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/71225" target="_blank">📅 10:33 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71224">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v-D3vaiopHeDL6i71Us6X9JGOLM3xXvFFML91idN0RPTP7wj1DQdbLYAJZwTpw9YDggwx4nvaKpSD2Gisgjntrk0uQoy0J8HyAkiTzu2rNrkti6HORrRxcGqNYhHcaO_yH5yChxj4GXYHZ2wIdjfDsROPmyYPNQYre5T7VFq6c03CrryVA5FFbbDhKmrqjuytAXkfUHQQHppJQJv5r6UU1aZQusOLBwqA8zcn2uVOYW0qwBJDaGYcQwaaTPDfBxlDZx0zU7oHjPiAxJJRGzw-rDGfOIKroW9zoNfE9AivDM9XJV-dSRXxY1D2wOdC7HATRKh_jkqCLossiF59us0_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
شاهزاده رضا پهلوی:
هم‌میهنان،
جمهوری اسلامی بار دیگر با افزایش قیمت بنزین، هزینه بی‌کفایتی، فساد و جنگ‌افروزی خود را بر دوش مردم ایران گذاشت.
همان‌گونه که در پیام ۳۱ مرداد گفتم، گران کردن سوخت در شرایطی که مردم زیر فشار سنگین اقتصادی قرار دارند، اقدامی ظالمانه و خیانت به ملت ایران است.
به رژیم ضحاکی و رهبر مفقودش می‌گویم: فقر و فشار اقتصادی که بر مردم ایران تحمیل کرده‌اید، نتیجه مستقیم سیاست‌های ویرانگر شماست. منابع کشور متعلق به مردم ایران است؛ نه برای پر کردن جیب مافیاها و نه برای تأمین مالی تروریسم و جنگ‌افروزی. اموال غارت‌شده ملت را بازگردانید و حمایت از تروریست‌ها را قطع کنید.
گمان نکنید با کشتار ده‌ها هزار میهن‌پرست توانسته‌اید اراده ملت را درهم بشکنید. آتش خشم و اعتراض مردم خاموش نشده است. ملتی که برای آزادی، رفاه و آینده‌ای بهتر ایستاده است، در برابر سرکوب، فساد، بی‌کفایتی و تحمیل فقر سکوت نخواهد کرد.
پاینده ایران،
رضا پهلوی
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/71224" target="_blank">📅 09:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71223">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DSmqNrObdN7aS56l-NSEl--SurarUuVJJTYayUghUfZOEne5s_4EoiRZ8_UPnIHxLnhY1hUlCHTkwXOVePDiZiojVXuAGQRhqpi-kW56GEASWQBy4YSaLxaiRyJYS8xg2q-OZT6Vwa1OnAB22s2k6R5jYTqYOwgLqjB1i9LtVjA2Jp2E6nwjkWVpI9SxM5GLTdlmbT12LxYznsjmp5OKWJ2-cb_qUM7z4U9Tp0G_JjK6cWi4x4NI_m_CAHN2gvfhJkhURHxXf7iaH1z46clwUWkUNBfv40j67UuhBiof4amnh2zwUAJusYVJOveJtkMkZstf51PbE0jxJk2fDCffZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/71223" target="_blank">📅 09:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71222">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/924d85f6dc.mp4?token=K0Koly-oS4LP4CcErPiod32F0Q79ONxegOv2rTLAgDpPA1df3-4oRElvtcSksF2ZoTj1m7fijaqlq2JM3mAcYMP-wbVBGqh7tWCwOWxa5aJuEjOs8KgFqU7Bsla4XDjZE-On2UrmznPEhtZHsp7Vhp16gGhrJDanWvQNMExZprMa6ChYw5Tjh_MHQp-_W42xQjm0NJLHYwrpsjiB97CvJx87rg-HCWPRHlFsfkM6VayTzPx3UQ6Q31gib0hrafnTzgBORoo2A05q7dJrRyVoaajj1z2bH7z3F4pn8J_7YcVZtTjNviUQKgXqaectp13gyCoLKhCMSAeCm2oKN_zf_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/924d85f6dc.mp4?token=K0Koly-oS4LP4CcErPiod32F0Q79ONxegOv2rTLAgDpPA1df3-4oRElvtcSksF2ZoTj1m7fijaqlq2JM3mAcYMP-wbVBGqh7tWCwOWxa5aJuEjOs8KgFqU7Bsla4XDjZE-On2UrmznPEhtZHsp7Vhp16gGhrJDanWvQNMExZprMa6ChYw5Tjh_MHQp-_W42xQjm0NJLHYwrpsjiB97CvJx87rg-HCWPRHlFsfkM6VayTzPx3UQ6Q31gib0hrafnTzgBORoo2A05q7dJrRyVoaajj1z2bH7z3F4pn8J_7YcVZtTjNviUQKgXqaectp13gyCoLKhCMSAeCm2oKN_zf_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یک سرهنگ ارتش :
از فرمانده‌ی کل ارتش ایران تقاضا دارم، یه قایق پر از بمب با جلیقه انتحاری در اختیار من قرار دهد تا خودم را به ناو آمریکایی بزنم و منفجرشان کنم
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71222" target="_blank">📅 09:32 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71221">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26767c2cac.mp4?token=TZ_grNtz53sKbLuuoPT-XTHI-0Yh-9d2UvguoSzBFFbUd-0o70WHtxSuketPBLq6TNbbccCeFMtFWR_ul34XBF1L6EzmFahUin4416RA2b8cL2gKN4EtxiR0y5oUKkuh6hRvRtE1dqS5SRKW1FMisJx23RSgNpLv9D1vvdVQeB3Mk2Ozh8HWBHVkaF3C5CkB1_OLf_-Ubypc_fKa49K4E1UnrF8q28JSMVwNW4QghBV0hkZyUiTxVZL1GR69SsP8JCBwW7oImAD7QWD2E-W9retSesHUr8oPW9lAGUrbIWPljDOCL1SRoDkRKqNSsCKnrnlfHX0PM1_UDL1T3qdQ0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26767c2cac.mp4?token=TZ_grNtz53sKbLuuoPT-XTHI-0Yh-9d2UvguoSzBFFbUd-0o70WHtxSuketPBLq6TNbbccCeFMtFWR_ul34XBF1L6EzmFahUin4416RA2b8cL2gKN4EtxiR0y5oUKkuh6hRvRtE1dqS5SRKW1FMisJx23RSgNpLv9D1vvdVQeB3Mk2Ozh8HWBHVkaF3C5CkB1_OLf_-Ubypc_fKa49K4E1UnrF8q28JSMVwNW4QghBV0hkZyUiTxVZL1GR69SsP8JCBwW7oImAD7QWD2E-W9retSesHUr8oPW9lAGUrbIWPljDOCL1SRoDkRKqNSsCKnrnlfHX0PM1_UDL1T3qdQ0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پزشکیان زمان انتخابات:
خیلی‌ها میگن من اگه رئیس‌جمهور بشم میخوام بنزین رو گرون کنم، ولی من بارها گفتم بنزین رو گرون نخواهم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71221" target="_blank">📅 09:03 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71220">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71220" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71220" target="_blank">📅 00:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71219">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L_dX66uuWYUSmLfbvOrsPm-bsW1QvFAfKGCqu7_nBdLDK9aMJrYauLiiioCCD80mvD4WNG5uJ0NYSyw2WdWwgd8cTP4TWmh2q7rca66QXoptbLRgWcybuhAQi1gh6OvQzzWZrg67tGFfqZmjE6Cg2bGgSEKKoMYg28YB8xGddViDO-wM9H8jBKP8qvH5bKrwPxnJmrDemh1oeQD-Nm_GShvdSd8BuhgxvDNsgrjqEEbFi0cNLv6fuDEo1dhRd62U0q7Lt-ll97_lYk5SJuJlmMm3SdvtuyduK0kwDl2tAr_9ixw_abOJmu1WBR_vWJO4HqSxBAz-a_OU5D2eD2fw6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
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
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71219" target="_blank">📅 00:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71214">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q0E4xZPkAc6aZT3ZofH1g_ie-1A0jh5qbj4O08C9KZV0OZ6jFQgjiD6d5SmJqfEB92JrYXIez55N6xI4oeHdeFCUGTZuFQr-XKqX4mPvE1lVOIOZrXfYPzHSq4Upsoa2DnapzDHdsJhj3_oQU3j-dQNiftgxll9G4lGEaTGPfiogPX7y_BwllJIdE_N6u1Z22z6_DqUfFxIsqffF7S3M8ceIz741cwZzP4mATohotkIqiJswXn1MxcrPWiHjTO41UqRG1uKdqHIDzptFLFYxR3OYuum9wN9i6XuP6oQqOSUNU0pY5Maa7ZkPkehp01FA6SRkHpAM_wy8ikP5cf2pgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ee_2EpSZrHFA9mv67s_iON9S9GVUM89s7gGhpoCTELOa7_H7Ty9nAAmEb83nVEB-KBrVZ5TsETCBxeB1R8Y7ZVDq-vY-OdWYC9hE2EaK3Zrrkqs4lh5aOSQz0rkZ5nUAlrY_wA53xHBFteBdBLIGwdDuLx_9Dlb_nPEFUarsYSsH-PONhEdEUgUrTLr1XjU93w-vrDotB6aoUdMO4p84xw7skPwKc2RPNTbrl8ut6cetxtmXfRNJBUUCENqlbzZ5jJCtu28i-NR9Omzdaw30zqnRiqS2jIXbANcEzPPf8GGIuiFisBGtRkkEm23qkSdeJBFZD0d9TsOv-WUSGRs2qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p9zTAgICxK6ne7zMlyWPhAEwUHmUAD_uGm1fSc81e7pRVZSqwSXx4WTDCh_WHWdnVed62vn_-_keD4lHlqvQ3VCOnBnsvXDMquFS2_IhMysCKX3keR4OsAjDEIPLRMB8ram_x5GtlnipSOqU7A2tUwINlQEnbEipSK37TSlhrcW_jEznubCeJTY2r1f29S07s-EFAxWnnxcfZeMslAb5JAc49fdZ8pykdI-YrS5bfL3klG85xATT5IOCptUo0vbXNezhuWkCjRJJH0kIo9semjpvlLBpPd8jRgFLiQP56P0PN_amB8l2yXVHp7DbAcyY3e9xUWRofjrCWrhGlC7j7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HhY0N0_-hSTOIG5IeSPqwwlaTHKv4oxqzUz8o_-_VqRs4RxhytnXNQF2Wxvx2VzXf1WL9TIMMXt6nuxhxr3WuIySnpk6SCzShT8Jg7Zkkaf-9ldSuy1gDBT7Z-TSVS3bZy2WmOaNCV3ciC5bAQZSm5x1awnMAZz56Imh3mCBVJojQkxY-7xdsZn5qP10ndCOPm2GHsNGKvT0TuanHORfJkrZImwpeOMQknlsMQ3plLwayLZdqayW6BIA408rRvp9pOE_xK0SLNXaY7PjRObQMkJrnzBhf5wwpnESs_MAsI8lU93Pn5pyR5gi9PyZhrVnictqDpfJmv-SabDdz-MJnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LoYHUb-4FFm8B-cx34VISggXutLcwvZU3y0Wptq3bCU7rgJVQaHYLpKemkTqot_Uh_V9ore6mLwedWir1aoOocInRVaGxzVhO-Pgo_Lc8uESkt9O0q7D_Gyo1mU6lbC-Pzmad-47U7aggfiytTde19xa0LbDIxoLL9YjpmiOBspgEEXj4YxDJ1ozKND_KFzg4e6icSY6v9ZuvQgJ-nFAbzwC0bUmHDVeLBDaLr9jzomfK0O2hZvhB87EtOL0QDwnfDyIT1SEe9gUMJdR22Vf4UXufTL0eEUwZRj7_cdeo5N0-yMqD9NY6QfWarMuWQdBE-4Ftu4S_YT6zEb4tmKV4g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇸
ترامپ:
۱_ایران کشوری در حال فروپاشی‌ست.
۲_خداحافظ جزیره خارک.
۳_ارزش پول ایران از بین رفته است.
۴_صادرات نفت ایران به شدت در حال سقوط است.
۵_ حجم‌های نفت هرمز به سطح قبلی بازگشته‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71214" target="_blank">📅 00:28 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71210">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZUzHzQVto53Di7K_nZNNiX4Y_ageeh1jmnoElFKaWwMa5jAuVk0IeT_5jTjsnS9aGEX1PbeFXxNcvFtZeQRf52ykxt6qPETT3K_02ehDKSs--r9IGOyF5tvxWPzKo1GKuzrPBYv2OHLPGyUW2YRf8rnoJES_WxvmJfpdRFGqP2x2EkPbj1i7Yb3QF2R7nDCuASKQF_B6cAgs6L-Uj9bpLDV8h8xh3TpocMtVrsLExFMWEQZojCbzxNxRcxlV89cCiYG5FIkyghwxgeZpytWIIfh4oGEOKAckzvW4Sa_GLiyHwFpZhZu2NbejyNoAE3dsPOBag2EPqg0S-Ju4QLhQQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ukwPW8gFaTgxgG12ti1a3AkYI4umfmY9jT4MW0dP9sTJrYHJDfiv7SQYRbQWlVE_UArsd9scgFPX3a4e8Go_scdZo2Au9TiOBN_i8oSFnwvTlmDYn2AvHjGaY7cuKnxUrln7Rhk8woKjWbWHDJiCwr2NB6CgRl0nsaMdjwX-gq9msOONRQsKf2sJW4qLJMtiuA_wdpFbEyZwkCWxPpZNRgoKP61ae1YwEJxdeDQ2ZsY6FQa9aiqmjBLSABXbPDPbibwjW0UN83kqQVhaMpeT0pnUp5Qm1C-iRx5eobdVtNVcUV6HCn5I2hMEnMxSCJi1ZaxQg83TRm_KMpIJV6q1pA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویری که ترامپ در تروث سوشال منتشر کرده
😟
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/71210" target="_blank">📅 00:09 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71209">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bca8942d62.mp4?token=YOfLAV8CJKTGyxucXWcrlPl3j0rPxzJKozXEy2rJXk34aYIpUE5d-0RQbWJHqDIqcruEUe3QoqfJrBcNjTMxffeewwf2gnNELfOVjPwycsNTU8i-8beoZq49pAAz4lD3GhPMj8SyQrcCYMjfNSvDLtwHc2_jl9IGlgBmvDZU3JpPQ5-0Qo52EX5V3iqsuJj79f_CV9NZdGSM0AXjk6GqJzF5fXPBwqw6huMFSrROSliNHO7BeslT_wEYs0jfjaoacfeupI7sGKL1qnGdgvRvdVGNY7C9m3YJFFsb2cWV6cjSCts12jMxXl37Oy2UzDIrvW0hzygSRsrgArFLZYYkDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bca8942d62.mp4?token=YOfLAV8CJKTGyxucXWcrlPl3j0rPxzJKozXEy2rJXk34aYIpUE5d-0RQbWJHqDIqcruEUe3QoqfJrBcNjTMxffeewwf2gnNELfOVjPwycsNTU8i-8beoZq49pAAz4lD3GhPMj8SyQrcCYMjfNSvDLtwHc2_jl9IGlgBmvDZU3JpPQ5-0Qo52EX5V3iqsuJj79f_CV9NZdGSM0AXjk6GqJzF5fXPBwqw6huMFSrROSliNHO7BeslT_wEYs0jfjaoacfeupI7sGKL1qnGdgvRvdVGNY7C9m3YJFFsb2cWV6cjSCts12jMxXl37Oy2UzDIrvW0hzygSRsrgArFLZYYkDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
دو عدد سیب زمینی 100 هزار تومان؛ اینکه قیمت یه دونه سیب زمینی بزرگ‌ به ۵۰ هزار تومن رسیده‌؛ یعنی فاجعه اقتصادی.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/71209" target="_blank">📅 23:33 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71208">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a65cbcd011.mp4?token=XLuVx0uCjG9HusOUoxSiOPD4vOnZn27RjFVMSg4J52NX8JZIYSaHSVQaD0w-5pJ2sqajSQUZhbP7j4YyLxxPBYO0DPkz7hl7kdGWD1-DC5qvHr9u0N3pEsowUd_oDRX2_AxEVFV0joXz3o4bXiDMwVFww9oFyJ8RDX481WtDF_7piJ1mpddnneZrirG6cdS1lRLFXZxT8KMf7bsP1NsvcW13-AMcacQsBnSrm4l-RJFWGx_SZpKGXAK4yfTVFL_qdddPwncD0CSStAA8fdIKewH68Cuj1P2p50aeTyz1_Hp2ZVkOS0bQrNmMmltEGio3SZnG4Gb444IOoOl34OyT5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a65cbcd011.mp4?token=XLuVx0uCjG9HusOUoxSiOPD4vOnZn27RjFVMSg4J52NX8JZIYSaHSVQaD0w-5pJ2sqajSQUZhbP7j4YyLxxPBYO0DPkz7hl7kdGWD1-DC5qvHr9u0N3pEsowUd_oDRX2_AxEVFV0joXz3o4bXiDMwVFww9oFyJ8RDX481WtDF_7piJ1mpddnneZrirG6cdS1lRLFXZxT8KMf7bsP1NsvcW13-AMcacQsBnSrm4l-RJFWGx_SZpKGXAK4yfTVFL_qdddPwncD0CSStAA8fdIKewH68Cuj1P2p50aeTyz1_Hp2ZVkOS0bQrNmMmltEGio3SZnG4Gb444IOoOl34OyT5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سعید لیلاز، اقتصاددان و کارشناس اقتصادی:
«کشور با تذبذب و دودلی، مس‌مس کردن و فس‌فس کردن  اداره نمی‌شود و حکومت باید تصمیم‌های قاطع بگیرد.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/71208" target="_blank">📅 22:51 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71207">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQwqT-5mZKUoKGPNpvxpUtvzYUGDcRLUSGxvz_yvDA_q8tiJQ-VssuURW8cJTu6b2R2_OQ7zmBDe3kaBXZQqhW1w_bXrvRVr15YmR7pPPPXpusxFXhchDQW78m11wF9Hp2AeLSxL_X4O1OTu5Tuwb7JBfI7XTljZzaO7q2YhkDtPe3fuGiwH7hOLzOd8ORwSNWHmcorVEJNrCcbixcSquXftGRw2In98HGSoFxkUD3N07u6clljF3gTEADYXI4rc6bOQInDBXMjLhyRGY45dQsmCTIQ9Z-2Y5zHyyf-QmkYdWSdN4WfKuNM_8ovhdDcAv70sL6_tsG9-o_SFfXnGew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ در تروث که اومده کلشو جای نقشه ایران گذاشته
😟
😟
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/71207" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71206">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6400639d7.mp4?token=O1xyQHC-Np2WgRJ4ICJY5XW3HyHZEzCzKJWtVkE7lwowQk9Y_-Rej-R9aJKPCKf6-2_apZyW7R_ht9OAJklWU8oSy3yCoY20IIIOg5REjyYyVSkCJwNaeSUCx6tHuZwuDDyE-rodAV5VFv-aSxdSMaOLRPS8z5LhOg4rd-xaAhXd2ZaYn6-EiL9rzDereGE25PnTZXjChiVTv8IEssZnw_74IpgEmHLcOemhSB1sRToCe-qbJvUpnc3ng58AwjW8hdFqDb2kvmbNHq_Yn6qbpVhXiZgfXwjAQYBdTsNOxWQW86UM8l8dceNfJUwh0gG8o_SwCPAz3egn7O_WzVih3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6400639d7.mp4?token=O1xyQHC-Np2WgRJ4ICJY5XW3HyHZEzCzKJWtVkE7lwowQk9Y_-Rej-R9aJKPCKf6-2_apZyW7R_ht9OAJklWU8oSy3yCoY20IIIOg5REjyYyVSkCJwNaeSUCx6tHuZwuDDyE-rodAV5VFv-aSxdSMaOLRPS8z5LhOg4rd-xaAhXd2ZaYn6-EiL9rzDereGE25PnTZXjChiVTv8IEssZnw_74IpgEmHLcOemhSB1sRToCe-qbJvUpnc3ng58AwjW8hdFqDb2kvmbNHq_Yn6qbpVhXiZgfXwjAQYBdTsNOxWQW86UM8l8dceNfJUwh0gG8o_SwCPAz3egn7O_WzVih3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
مجری لبنانی:
مجتبی خامنه‌ای، رهبر عالی و ولی‌فقیه، اگر به بیروت بیاید باید بداند که هویت ما عربی است، نه فارسی.
بگذارید این را به روشنی دریابد: اینجا بیروت است، نه تهران؛
اینجا پایتختی عربی و آزاد است و هرگز به پایتختی فارسی بدل نخواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/71206" target="_blank">📅 21:34 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71205">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
⭕️
#فوری
؛ نرخ سوم بنزین تغییر کرد
سخنگوی دولت: نرخ کارت جایگاه سوخت از بامداد سه‌شنبه به ۱۰ هزار تومان افزایش خواهد یافت.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/71205" target="_blank">📅 21:13 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71201">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UbKW0c0sR7LzlkZAdJWmJ086FQ-a34Vj4OVj_5J9-8veRBynPqcR-UXIF1MAKXSZCQxN7SiWhXq5tRr9AYUy6ckJXcqdepj2qUjdbuAiEllT9A0VaKIel8_UmzwYN8dqfIJNdB6F6pelzMRMDBPQ2MNanpg1BV5zeeGNoVd415PlE8GFlhsOD9cK8kNNlI8TS-ITbMGWY6RZ3OtkaPfc0exaLOmQ7dRvXWKqhsXwhXQBBbegOOblhZPdW4IQMsV4EOnujbfteZhacVsFdxaaZlpCbtfC_VfKHfQuopV1GdEGP2JdgEva9hPP3JqQSRRVRP7GhE3vXuCJrO83Zk1iiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UiNe_MHGoxKNWs3jQvfe4X-IYniSrCxR3zgj7XyGy-qnqEyCkT9ZLjBSs0uxqcmH2RtyzQOlwhxCcPqncJpGsE1d5rzELI9OAoHIdzBh67bZisURVkIj__7r2_rheuoYkIZvd2TjFkzTvE700a14d6GC5n6eB0hDCdisPJHN8q002Nf1E_W8TXubfLf6P-1anORhmgDXP3EUGDBUXCzBZXr0R6FFRNz4B_CNgBdUVH5Ew363dI-uinjjtYQq8jA8AcFdYwFiGJGwJtM2_-GgoFyYocsj4a_6Ar8VT9s4Nqoi0eiQKIGXLV3UGVUQrKDsNz7UE2eBa8e1Pg6Eg-3Mvw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98460c35d8.mp4?token=bwQCQ-7mPH_grdRBBDJCsEnRuEuts-PZbr3E2SEx_Lby_bTxfgtDha7yAbw3y8asY68y_K9vE53Vkpqe8Hk_zSvSUM3zqXA1U5XdDgjoz1OoAeoVxsydAPFXEs7Nw347ocwhaN5DSV09jU__PA_WULI6PkACCC0uK1c61S054TSFu_c2rACgEwisgFbtGTdFZrYA67AwX84P7qp4tnJGzezkP-1IhhSRziZkwn4J-mrUdvcQR38Wo8umREzQ078LpXgEhA7-98FVsXG9_opV4YWS0ik_rzCRaOX9EpiPg_ThXxjR4BQ03vnoafOFXYzLGiOfK2MBDInrfTaI_1ydYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98460c35d8.mp4?token=bwQCQ-7mPH_grdRBBDJCsEnRuEuts-PZbr3E2SEx_Lby_bTxfgtDha7yAbw3y8asY68y_K9vE53Vkpqe8Hk_zSvSUM3zqXA1U5XdDgjoz1OoAeoVxsydAPFXEs7Nw347ocwhaN5DSV09jU__PA_WULI6PkACCC0uK1c61S054TSFu_c2rACgEwisgFbtGTdFZrYA67AwX84P7qp4tnJGzezkP-1IhhSRziZkwn4J-mrUdvcQR38Wo8umREzQ078LpXgEhA7-98FVsXG9_opV4YWS0ik_rzCRaOX9EpiPg_ThXxjR4BQ03vnoafOFXYzLGiOfK2MBDInrfTaI_1ydYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
🇱🇧
حملات شبانه جنگنده های اسرائیلی به ارتفاعات علی الطاهر و نبطیه الفوقا در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/71201" target="_blank">📅 20:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71200">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a237cee509.mp4?token=HlHYvW5vdNguWxxGXwEc5KxY0-Syxc3KQSR11RzJHjmAN0JMqzagb7l_0DhiH0kGewMa8LiwycJPLeM3AUahAaPFRGqyzYUrDzbiCb08UYG3ttF_6Otk8Iw6VD07RF5tN7H4s0lfEIf4u1suu8VaA7y7q0eEg_Nj2S37OevRAAV4L2rHyf4dr5krPJiaV7HsnfVadc30D1VutEJzELRRtp3M6knoDzA5KcssNEUrnSSsK4_Rlb1-BmApmjZQENQ6usN-jg8HOXWCZkGGx4Zv9eRtUk2Kv1UAHjsKc81UK1giV8CovLqIVgvq3EXEEF8umtaKNQgafWdrDBJWqigJCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a237cee509.mp4?token=HlHYvW5vdNguWxxGXwEc5KxY0-Syxc3KQSR11RzJHjmAN0JMqzagb7l_0DhiH0kGewMa8LiwycJPLeM3AUahAaPFRGqyzYUrDzbiCb08UYG3ttF_6Otk8Iw6VD07RF5tN7H4s0lfEIf4u1suu8VaA7y7q0eEg_Nj2S37OevRAAV4L2rHyf4dr5krPJiaV7HsnfVadc30D1VutEJzELRRtp3M6knoDzA5KcssNEUrnSSsK4_Rlb1-BmApmjZQENQ6usN-jg8HOXWCZkGGx4Zv9eRtUk2Kv1UAHjsKc81UK1giV8CovLqIVgvq3EXEEF8umtaKNQgafWdrDBJWqigJCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
زاکانی:از وصیت‌نامه علی خامنه‌ای خبری نیست، احتمالا در بمباران از بین رفته.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/71200" target="_blank">📅 20:15 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71199">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90305378ee.mp4?token=qj5d7UlM4CwEMDWEMji62EEGHMcUZNiYkSb8nw48gfk3pK_GEOwn6_WxgzHbBoCC6JPJXumgDIRsIsL37cEpeCUy8sOh3s69K0bO7bOJaIKqhR-8i6vgkfD5EmKZIxtDhJgSx838o0HQUOC2Se6FUqREGQydGvI5a7_A7fnYwRH8MrdBS5EjzsKb8yhS4njDZzm-zWLG8xOWVXFpoxG0GYoVi_5m6VFzpxG0YzbnmCmdilZfSMXS-Nxrjn5bsmTgNadovyOi8vDeMSPsQMx9CVdp3sC38seZKj_KmEiokIRlZJxQZl5Qf2Ceet6BE6IjpIF07HimpUchCSTMFlNhaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90305378ee.mp4?token=qj5d7UlM4CwEMDWEMji62EEGHMcUZNiYkSb8nw48gfk3pK_GEOwn6_WxgzHbBoCC6JPJXumgDIRsIsL37cEpeCUy8sOh3s69K0bO7bOJaIKqhR-8i6vgkfD5EmKZIxtDhJgSx838o0HQUOC2Se6FUqREGQydGvI5a7_A7fnYwRH8MrdBS5EjzsKb8yhS4njDZzm-zWLG8xOWVXFpoxG0GYoVi_5m6VFzpxG0YzbnmCmdilZfSMXS-Nxrjn5bsmTgNadovyOi8vDeMSPsQMx9CVdp3sC38seZKj_KmEiokIRlZJxQZl5Qf2Ceet6BE6IjpIF07HimpUchCSTMFlNhaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇵🇰
بلاتکلیفی بیش از یک‌هفته‌ای صدها راننده ترانزیت ایرانی در نقطه صفر مرزی پاکستان
این سنگین‌سواران ١۴ شهریور در ویدیویی گفتند که بی آب، غذا و امکانات بهداشتی به حال خود رها شده‌اند. با اتمام سوخت یخچال‌ها، بارهای فاسدشدنی در آستانه نابودی است و گمرک هیچ‌یک از دو کشور پاسخگو نیست
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/71199" target="_blank">📅 19:32 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71198">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">بیناموسا مگه نگفتین از امروز برق نمی‌ره؟ رفت که
#hjAly‌</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71198" target="_blank">📅 19:06 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71197">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd3aa09393.mp4?token=QJhpPjFBXPH-gOQ2abL5N2S83ipEqwC-YT5bsuuVgUDscsiY6umnxU5QYpBlm-tFaLPoJFpHi8dkrKMJjMak_v8IbJ3DZPs4LxKZlgzWj3A-E1B9JnH1CFFSljI_wtqVDxwdZD5uHPKNplSkOjV8XiDkJXy5EZWYx0Ien5RxKaUTjP-XgQYvHePKL74bzJlewaD9bnJ-j9Z1jgNHCb6zlEByok8sv_Ttn4VUFppVYS1CNmSgyVcLHyvESaMSUYS7RAEghmgU8illxJAMSXCcWdmEEyywFDUmQP4xzGZQLj4ZiR_96hvirwThsG6-cKGsD_2IBIHwDj3qJPxKfdl64w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd3aa09393.mp4?token=QJhpPjFBXPH-gOQ2abL5N2S83ipEqwC-YT5bsuuVgUDscsiY6umnxU5QYpBlm-tFaLPoJFpHi8dkrKMJjMak_v8IbJ3DZPs4LxKZlgzWj3A-E1B9JnH1CFFSljI_wtqVDxwdZD5uHPKNplSkOjV8XiDkJXy5EZWYx0Ien5RxKaUTjP-XgQYvHePKL74bzJlewaD9bnJ-j9Z1jgNHCb6zlEByok8sv_Ttn4VUFppVYS1CNmSgyVcLHyvESaMSUYS7RAEghmgU8illxJAMSXCcWdmEEyywFDUmQP4xzGZQLj4ZiR_96hvirwThsG6-cKGsD_2IBIHwDj3qJPxKfdl64w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نخست‌وزیر نتانیاهو درباره ایران:
پایان این رژیم در ایران نزدیک است.
این رژیم ضعیف است، برای بقای خود می‌جنگد، متزلزل شده است و هنوز مأموریتی ناتمام باقی مانده که ما مصمم به انجام آن هستیم.
این امر در نهایت چهره خاورمیانه و مسیر تاریخ را تغییر خواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/71197" target="_blank">📅 19:00 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71196">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FPxauPNQT7ahOsJvfUIZrUKp1EsnrsnWXqROquQIEm09ljYEEnOcI8bPEyTT4SvkXXGhYgf9ze9YDX4zGLzjObO7fdxYJSs97T0mnLN6CVV5Ld76KTs7VmB-OjlhGij1JY_J6delq8f7l8s-FiI5ESmzz0TEnxk8DLMB8fXiVLyVpwWhcq9Yi4xHDwtZ3aawAeHfKTk7toT_lRH_kdFhH0r9td0Fpcx6lmL0mNMAln3vJJa2knvsDlEro616x_ek7eWZI-BeCl664Q8F3OQlTiJG1C1VX3I4cU_IcfXO3IYf69CcYspcsg-OfsDs_wdkqUhVg4MvkK8EAswWSr5NGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
دیس قالیباف به بسنت:
چرخ‌ها آماده. گرم کردن قبل از پرتاب:
دیزل ATH: فروش فوری
بزرگترین طلبکار شما: موفق باشید با Yentervention++
80میلیارد دلار کاهش می‌دهد: نام نروژ را به Americaway تغییر دهید
استخدام کم: بدهی به خدمات با DO[Israel's]W، طبق گفته عروسک‌گردان‌های شما
اوه. طرح نقطه‌ای فدرال رزرو قرمز چشمک می‌زند
😁
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71196" target="_blank">📅 18:55 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71195">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rkqbQFbtK_zZrjzvze1Kwr-wC5VhLompSuyC_l5StwwMmYNQBPOdtlvktIy5mFCT97BbsN86kojbgrc0ig2XqEEz-1ELIec_Spf2O_X5RFrR-dxoKHytOy3_ui1XDaCCodkKiSjUOskPOFcW1nrD1Y1PJ-Jd24GCFOcRkDy24qkK6is2yHjSga_ZM_UqPLTfgRbXpdFzW1GHRjoZDL8nPtzox0NuVRZGxaRhSeujzVoh9IviDzJSv_k_gFYhVEIYndYcH-L3O2--PP6EW_ybqN7y_23bxdJ5zjDPxmX1kGwbJjuxWYHk2tysz5j2m4XE8l9FRx6_vtLb381TgWSY2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
گویا املاکی موهاشو رنگ کرده
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71195" target="_blank">📅 18:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71193">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WoR4kyuTmFdlZfDvx4JzGKCTTD4-RTOViSG5w8biKUX-XKrvzy2K7b2TRBTcAyiIC2b6BSkTDKW7lwFL5QzrTT04u3MG3MbwlHy-ujg_OvS5GNwXh4HV1aS-blnwXu-xBf0oyRMnWQzmGs7DLDOJiUWXoDizwMKjpn3AfU3QbXztIqOvHJyBKWnm54gbvtnR30rnP0mICtV4beoLXmZb5Vm_kGl_h8Cm6tVewrwvktoMBRKLRM2IUuan_0vQpHIKq4dhYeZRPTeybwjj9Uk_L0K6lvD78_TRemDi1VwPsT6t6kxFUtc6clsPX7q5qd9AKm5F5tzpap9K4PB7n3sQmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/385d0bbd1a.mp4?token=g6bsZD7K7foAMi30jGRpj5hBHUr3QviEkoTH2DDZoni-PyqLvWGxcUhP_2yQssFb88yBLVIz2BLwYFiXJy7sUA1toFfVhOdRN17IxfCY4c77JGGRn-z5XucW16lUgzjhsDKU42nftrTrWPNrj_VKY4ciU9a_4GDKIyMajFKmOFGbsSc2aRlEQ9nLF2xoqisr30ZPsPTJuNfhb4l9GvTIQC1maG1aQaTRSnga1lYpLDFV52XIcHt9_9Lez__BrtsAGYsZ5LZvHjyZ4gDvLzAh4FbcAFzWTZIN-JlI9ktGfvc7zfA39NYih_HdL5bkfXAW5sFaHxwJAbYRve6lPGjh7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/385d0bbd1a.mp4?token=g6bsZD7K7foAMi30jGRpj5hBHUr3QviEkoTH2DDZoni-PyqLvWGxcUhP_2yQssFb88yBLVIz2BLwYFiXJy7sUA1toFfVhOdRN17IxfCY4c77JGGRn-z5XucW16lUgzjhsDKU42nftrTrWPNrj_VKY4ciU9a_4GDKIyMajFKmOFGbsSc2aRlEQ9nLF2xoqisr30ZPsPTJuNfhb4l9GvTIQC1maG1aQaTRSnga1lYpLDFV52XIcHt9_9Lez__BrtsAGYsZ5LZvHjyZ4gDvLzAh4FbcAFzWTZIN-JlI9ktGfvc7zfA39NYih_HdL5bkfXAW5sFaHxwJAbYRve6lPGjh7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
تو همه جای جهان هوش مصنوعی داره جای آدما رو میگیره ولی تو ایران برعکسه
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71193" target="_blank">📅 18:13 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71192">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa47cd6f21.mp4?token=NTYczLc5F9imu_IcwfedcEJzldifUXxpmPdwijUYeD27AF57w00COdZuZzUi_GiATugLty_0YGS3KWAno3QXZyHv3-VQzE5rZg9IflPftAeyiYioMgMs2IPCoFe8hzT5BwtVZRB5w8-_emxt8t-Qnc5KqYyt-zQqjCfi3njG2jTIA7xOObej3Q3ge9-S4Z_wsanPb69v3k4sm_cTY6d8kL2xccX57WFzcT-xi3BWajbmfqIJpo831XuBttGqqSwFm4ODoOJSMH-gZi36bN-F2MTBiJ8Q541u_Dm2VEut4uYyjqUG2NfXCsGoTrX51-Q9yFCKBj0jEf9oU8UvxmxBlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa47cd6f21.mp4?token=NTYczLc5F9imu_IcwfedcEJzldifUXxpmPdwijUYeD27AF57w00COdZuZzUi_GiATugLty_0YGS3KWAno3QXZyHv3-VQzE5rZg9IflPftAeyiYioMgMs2IPCoFe8hzT5BwtVZRB5w8-_emxt8t-Qnc5KqYyt-zQqjCfi3njG2jTIA7xOObej3Q3ge9-S4Z_wsanPb69v3k4sm_cTY6d8kL2xccX57WFzcT-xi3BWajbmfqIJpo831XuBttGqqSwFm4ODoOJSMH-gZi36bN-F2MTBiJ8Q541u_Dm2VEut4uYyjqUG2NfXCsGoTrX51-Q9yFCKBj0jEf9oU8UvxmxBlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دعوای دو تا ترنس تو پارک لاله تهران!
فقط آخرش
😐
😐
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/71192" target="_blank">📅 17:34 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71191">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb7600cfd5.mp4?token=qg7xXpLsLtwoPpQI_poHGTUnGhlwZ7v3_iW444RvSm8EVAqwRUfwh-oP4X7ytkj2t9uxNr1WoGvgldohmcJFvpEbAyDsopDMHdE45bLS1DuuN0xDDwHOAdZS9IUgC9gFR-ZHYK2jQeMUphAprqNM4lJm5XV3cfuV19A_KOkOOsJFccrWjIhdhx3cOO_g9InyhXwj0Ss2labz-nZAxwer69gRiGyUYzdfjEp6IgBPxWTZDD30SkEx9tpcGQSvhaF6qb6gDCMWhYr4-9ot6cUbgKS56SpFJqj2D5XXZdXKe_RKix388vbRJaPVc2gQeAZRBHWWk2tJBcT1btAOvVPJ2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb7600cfd5.mp4?token=qg7xXpLsLtwoPpQI_poHGTUnGhlwZ7v3_iW444RvSm8EVAqwRUfwh-oP4X7ytkj2t9uxNr1WoGvgldohmcJFvpEbAyDsopDMHdE45bLS1DuuN0xDDwHOAdZS9IUgC9gFR-ZHYK2jQeMUphAprqNM4lJm5XV3cfuV19A_KOkOOsJFccrWjIhdhx3cOO_g9InyhXwj0Ss2labz-nZAxwer69gRiGyUYzdfjEp6IgBPxWTZDD30SkEx9tpcGQSvhaF6qb6gDCMWhYr4-9ot6cUbgKS56SpFJqj2D5XXZdXKe_RKix388vbRJaPVc2gQeAZRBHWWk2tJBcT1btAOvVPJ2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇭
🇺🇸
وضعیت دخترای حشری تایلندی بعد دیدن پرسنل ناو هواپیمابر آبراهام لینکلن در پاتایا برای تعطیلات!
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71191" target="_blank">📅 17:02 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71190">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/45226525f2.mp4?token=gyFa1sfXp4HD0mv2vfoPJLnKCr3PdRJbNJa8p7-jLuMV5n_KyepJWlhL9ZrbW1mJqQ-xpHlaocpxXZ2zX7A-iUM4PotRQN01tOxPetgmT2Mu3CXqXBIrVl6Pwk51UzCoGcEUdkYsTKTzjiuKITKdF4g8B-v67xOh3GKaapv5zmnDvxK8v7qIt7-Hei_vkR4UDwgE07lfzOh8CKX6QLvXOIwF_InTOF2RE9j-B11QCNfsqxb39fL6ISmI5_y1c4EeY0pKrpDKC1myqJ1Vj2Q3IVGcXbgX6UqypXMKmvfrSm81SHhHu8tqqb_h69FdAsw4B8tx6UCNX46Q4KZwunBLuA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/45226525f2.mp4?token=gyFa1sfXp4HD0mv2vfoPJLnKCr3PdRJbNJa8p7-jLuMV5n_KyepJWlhL9ZrbW1mJqQ-xpHlaocpxXZ2zX7A-iUM4PotRQN01tOxPetgmT2Mu3CXqXBIrVl6Pwk51UzCoGcEUdkYsTKTzjiuKITKdF4g8B-v67xOh3GKaapv5zmnDvxK8v7qIt7-Hei_vkR4UDwgE07lfzOh8CKX6QLvXOIwF_InTOF2RE9j-B11QCNfsqxb39fL6ISmI5_y1c4EeY0pKrpDKC1myqJ1Vj2Q3IVGcXbgX6UqypXMKmvfrSm81SHhHu8tqqb_h69FdAsw4B8tx6UCNX46Q4KZwunBLuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
راننده ای که چند شب پیش در مشهد طرفداران حکومت رو زیر گرفت:
عمدی نبود تعادل نداشتم به یکی برخورد کردم تشنج کردم جای ترمز گاز دادم و یهویی زیر گرفتم
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71190" target="_blank">📅 16:51 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71189">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71189" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71189" target="_blank">📅 16:51 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71188">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d8EACAfxADTirZpdXlogNmjfiGq32iM7-X-XiJLImOpAnxlQD4M29XJ49zz1n_zOKc7YUZ_htKyQfmgJHMedG7lPcXNPozK5fau2ZsNokTuP6EoL4ABAeg5SvG3tLpH5qA7SUebR7Vn_bvdHHR3K-wEp1B06mp7troUpoDXtG1MHY-zbw33mQwBzxLL28Z2M9Poe39i1x_hzQHAsdYyqvCgP0W9Loi7Upatiwf49hfu9zhQ6dlFoPZYm8ZdUmhFLbkqVyBU6Om6-YMjVzDVH5GFIk3N0Mh3lD1Zn7HE1ZLjNWtVCKnq8IqgvA8AjUotJTGRTZAjZD2Vx-PDiauDHvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
بازی جذاب
⚽️
چلسی
🆚
آرسنال
⚽️
را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید.
📊
نگاهی به آمار ۲ تیم:
چلسی: ۲ بازی ۲ برد و ۷ گل زده
آرسنال: ۲ بازی ۲ برد و ۴ گل زده
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71188" target="_blank">📅 16:51 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71187">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mFiIjk8U7hyLlu674xpmUHsg-n7YSNwiAzWHsWacB5Fdixu9p92Mo6bbq40hftLgxbW34T0nBWU3RvNMXe_pXoEq9qZAprm_ojgs-mQgniHwgsBdX9LrdQMFwnQ9wdNHnWNVrZ48qh063L3wPkvCY6DE3yUqYrxxgaxR7w-FV8fEYEYEuz0lLI194iCZw8endy5FVZRvIw5L1OnKuqdI244A0IRaRjrPR-eLNLM1juMQVmmqnyt3gWwd-BkwJRxSeM0Wh-df2XbyRCP_urnkeYYVGboQDVc-EUq_KoRbO8Mgwr8FkLlHHvJEBRTlWF-e-zfySyFFJp9wMXcGX6pmkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇰
🇵🇰
پارلمان پاکستان برای نخستین بار در تاریخ این کشور، فرماندهی قانونی هر سه شاخه نیروهای مسلح — شامل نیروی زمینی، نیروی دریایی و نیروی هوایی — را به «عاصم منیر»، فرمانده ارتش، واگذار کرده است.
او می‌تواند بدون نیاز به تصویب کابینه، کارکنان این نیروها را بازنشسته یا اخراج کند و یا در خدمت نگه دارد.
دوره پنج‌ساله مسئولیت او دست‌کم تا سال ۲۰۳۰ ادامه خواهد داشت.
او با دریافت درجه «فیلد مارشال»، این درجه و مصونیت قانونی را مادام‌العمر حفظ خواهد کرد و برکناری‌اش مستلزم کسب رأی دو‌سوم نمایندگان پارلمان است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71187" target="_blank">📅 16:30 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71186">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22246726de.mp4?token=P3Z7Ij5HOXNR6k5Wt1ovSnkVbJUnfoFtATiXC846oPogSDge8coxLRyIyAkjjh7jZDZ2vWZ7-furPT3WTDZDD9bxnHApo4el63Z_LG6oYryr5VthmoLU_iqwrwrX6eLeOYSPZPUSQAFyiM8Vce56fZg5J8TnjxEnReIY2Ku8RxVDcXSDGEr3K4LbcygO3RZbpNG_PQ0c4kIyGXgmTqgnOBhjoaKShbYIk1V9_jXEJ1QTzYQVxRyy6vKMig_nF0q8hwdvYCqw_A0cDQpEjhO_g0SGKCcNpzoMyv3QC_INh7kYpoXkS3RkUQgSy5nvnqoh3c4agmKoiPZDr3bbytd1FA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22246726de.mp4?token=P3Z7Ij5HOXNR6k5Wt1ovSnkVbJUnfoFtATiXC846oPogSDge8coxLRyIyAkjjh7jZDZ2vWZ7-furPT3WTDZDD9bxnHApo4el63Z_LG6oYryr5VthmoLU_iqwrwrX6eLeOYSPZPUSQAFyiM8Vce56fZg5J8TnjxEnReIY2Ku8RxVDcXSDGEr3K4LbcygO3RZbpNG_PQ0c4kIyGXgmTqgnOBhjoaKShbYIk1V9_jXEJ1QTzYQVxRyy6vKMig_nF0q8hwdvYCqw_A0cDQpEjhO_g0SGKCcNpzoMyv3QC_INh7kYpoXkS3RkUQgSy5nvnqoh3c4agmKoiPZDr3bbytd1FA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فیلم وایرال شده از ی دختر ایرانی که با یه پسر مکزیکی با هم وارد رابطه میشن و بعد از ۴ سال بالاخره به هم میرسن و باهم ازدواج میکنن.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71186" target="_blank">📅 16:01 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71185">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uMp8EK6EQ62LlIYXQkOVNLberCzxZNnr2CI5GnE-VCsbfYz3G3L6H09VPY-jbPBhxwzM0EZ8JP15GP-U7Fcru3PT5lMFXUb5UeGmOhwsqQewk8TbBKn8lABpkLIfnPS3uyjyfBwDNJLrgf0SkGfjY5ODDbL6JXaaZ4jBipTLS13eoLm_91KSn-3V9CIua-FlIteMzMRD-KN-uuFvck2_urSRKdM743UfGog7JpR5AsR3zcP-Dt8k2yM4laxkC_dfT5F_-fzVxNgwOKuZchRTNGnEGaiKsGBBD2dVGE184P7kCZ6XpqBgoN8MH9zXBeH7ZlTR8jklG5j9ayJdez50pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
دیده شده در تجمعات شبانه:
قالیباف
:
علی الاصول یادت رفت
علی الطاهر هوا رفت
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71185" target="_blank">📅 15:30 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71184">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/64baa312ad.mp4?token=LwX44Dh4eHcY3N13M3JT5nMrx1RmZ8GX3IXU474PbXUrb5EwFUngWorCdkgbfQreRW-w-iBcadQ0_5yYEbUonZrCPOkOFjwzB_nsMwAMDyIw6wzPhGTuVWDGKEtNbFoRde79-ybv_kNsNe-hcmQa4mbnSPGdv_jfxTKZElxrYn_4Qgrhjz8mll1bSCsyA__Y0HDjuHrupOcXfmCtJswh9x56AqxEZVqGQZGv-qVyCLurlCMqYACmezmDGMRc6w4p6cwZIO70RPW-MWxPUyjnf5mIW2-8hbxhU0kW20wMamRLOfhC82dBvKTTvEInonZBJXm6kWZcP0lhU3n6GF9hEw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/64baa312ad.mp4?token=LwX44Dh4eHcY3N13M3JT5nMrx1RmZ8GX3IXU474PbXUrb5EwFUngWorCdkgbfQreRW-w-iBcadQ0_5yYEbUonZrCPOkOFjwzB_nsMwAMDyIw6wzPhGTuVWDGKEtNbFoRde79-ybv_kNsNe-hcmQa4mbnSPGdv_jfxTKZElxrYn_4Qgrhjz8mll1bSCsyA__Y0HDjuHrupOcXfmCtJswh9x56AqxEZVqGQZGv-qVyCLurlCMqYACmezmDGMRc6w4p6cwZIO70RPW-MWxPUyjnf5mIW2-8hbxhU0kW20wMamRLOfhC82dBvKTTvEInonZBJXm6kWZcP0lhU3n6GF9hEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این ویدیو درباره یکی از جنبه‌های سختی مرد بودن در حال وایرال شدنه:
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71184" target="_blank">📅 15:05 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71183">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c325a7591.mp4?token=sCMSzlyn2V3imc4XPmMRoazf-uzUhCpoGnrS8ufpNXxVRTQvZsnnLmhoudcyMekCH79t2AMHbV_pgWgQAxSY_v0pRBnUiu6s2k8BeNUlNcqliW_kuvy2oCnZIiq40wzc_uVX6jVtiiWWN9HsMbtraA7uxxec7xxa3GZTIDMR4andsyvROVXv7Oogjk6att8iYHv0SxvMI4wHbkHeSmFJK3rp5cOqjrj4UrHFkAQpvgcrGfY9lk5VvAQrtUjNObXo92a2p2wkvjGRXNqwL_ZnWyjexhdOnOjz85E5DwjKD8mevNaA7Lxne4dT2r4xcZ2x3GFxhMs4H1K8i1oxZa5g5oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c325a7591.mp4?token=sCMSzlyn2V3imc4XPmMRoazf-uzUhCpoGnrS8ufpNXxVRTQvZsnnLmhoudcyMekCH79t2AMHbV_pgWgQAxSY_v0pRBnUiu6s2k8BeNUlNcqliW_kuvy2oCnZIiq40wzc_uVX6jVtiiWWN9HsMbtraA7uxxec7xxa3GZTIDMR4andsyvROVXv7Oogjk6att8iYHv0SxvMI4wHbkHeSmFJK3rp5cOqjrj4UrHFkAQpvgcrGfY9lk5VvAQrtUjNObXo92a2p2wkvjGRXNqwL_ZnWyjexhdOnOjz85E5DwjKD8mevNaA7Lxne4dT2r4xcZ2x3GFxhMs4H1K8i1oxZa5g5oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مراد ویسی درباره مسعود پزشکیان:
حساب اینو نکنید این متخصص قلبه. از نظر سواد اجتماعی یه آدم به شدت پرتیه پزشکیان.
گفته کارمند‌های دولتو داریم صحبت می‌کنیم در سراسر شهرها، نیان تو شهرها. مثلاً اگر کارمند بانک‌اند اولین بانکی که اونجا هستن برن تو بانک بشینن کار کنن. اگر کارمند تامین اجتماعی‌اند اولین شعبه تامین اجتماعی که هست برن اونجا کار کنن
😟
گفته دو میلیون خودرو میاد کارمند ما اگر یه میلیون از این کارمندها رو بگیم روزانه نیان سر کار تعطیل کنیم اداره رو یا بگیم اولین اداره‌ای که می‌بینن برن اونجا بشینن کار کنن.
گفته یه میلیون خودرو هرکدوم روزی بیست لیتر مصرف می‌کنن یه میلیون ضربدر بیست لیتر می‌شه بیست میلیون لیتر مسئله بنزین حل می‌شه
🧠
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/71183" target="_blank">📅 14:32 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71181">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c318eb355.mp4?token=qIIbhEu5Nf8Q7hK6QgmtuO7k0ku7XZg7IQRcGH4HLHYLQk3jjHpuj2VJflsED76myhM-rMHjEfbIYRaj9heQN0xsF6qE-HH3tsmqbHFtawUxIYbhVSjQoPUKO7iuPB_G9IY_87auV0JYf_PiMelm4BjfbBYY7LAAwx5RqsVxdd1n9O5biy3VhVASzvFrzk0BIZyeHQ_1H8o05GXQgUUzOl_6SJUIlneBoTS4b6i3GPg5ZpXgezrg0b3oXhpT2CD8viv1aadksIiXCENgB3JO4oDgxOf4nAEj6sT_ZYAb-BNv2RUNzLxFAMyT_ANKSPumZCOamoeMoIN-e6Abp4pfZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c318eb355.mp4?token=qIIbhEu5Nf8Q7hK6QgmtuO7k0ku7XZg7IQRcGH4HLHYLQk3jjHpuj2VJflsED76myhM-rMHjEfbIYRaj9heQN0xsF6qE-HH3tsmqbHFtawUxIYbhVSjQoPUKO7iuPB_G9IY_87auV0JYf_PiMelm4BjfbBYY7LAAwx5RqsVxdd1n9O5biy3VhVASzvFrzk0BIZyeHQ_1H8o05GXQgUUzOl_6SJUIlneBoTS4b6i3GPg5ZpXgezrg0b3oXhpT2CD8viv1aadksIiXCENgB3JO4oDgxOf4nAEj6sT_ZYAb-BNv2RUNzLxFAMyT_ANKSPumZCOamoeMoIN-e6Abp4pfZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇭
〰️
ناو هواپیمابر «یو‌اس‌اس آبراهام لینکلن» (CVN-72) اسکله C-0 در بندر «لائم چابانگ» واقع در استان چونبوری تایلند را ترک کرد و مسیر خود را در عرض اقیانوس آرام به سوی پایگاه اصلی‌اش در سن‌دیگو در پیش گرفت.
خروج این ناو در صبح روز ۶ سپتامبر، به توقفِ حدوداً چهارروزه‌ای که از ۲ سپتامبر آغاز شده بود پایان داد و مرحله بعدیِ مسیر بازگشت آن به ایالات متحده را رقم زد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71181" target="_blank">📅 13:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71180">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/003437fd92.mp4?token=GPCWB7Y4IOCxoGPtXoTXOD64sOib8HDfK4YAOfhBPHfOcv-gYMpcb5LlfVu-bAEHNhfHLXpOq5UE7bOx-zpyZNXmhHyBnPza-fe2DgA2iXa-G8io4h9-O3mgVU2rKmhyjtAa7dwgsX6TzcKiu7dchGrU9R6wnGwJB3b1OCqMsE_OZLXYqWhalIsCGezdgL1UH1tJwwRWIKjcYyM_JFc6WOBYJzD5Yxhee30Mh8UjQdk_N4-BWB4HnH5iT4z1AAjDD8L3HlQZaY6KvSN2DPb578wdPBkxsYmRoXfChRwtgFUp6HU0N7IEhfGJDElrrZbukizO-9Vdx-aHuoqtBZHxug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/003437fd92.mp4?token=GPCWB7Y4IOCxoGPtXoTXOD64sOib8HDfK4YAOfhBPHfOcv-gYMpcb5LlfVu-bAEHNhfHLXpOq5UE7bOx-zpyZNXmhHyBnPza-fe2DgA2iXa-G8io4h9-O3mgVU2rKmhyjtAa7dwgsX6TzcKiu7dchGrU9R6wnGwJB3b1OCqMsE_OZLXYqWhalIsCGezdgL1UH1tJwwRWIKjcYyM_JFc6WOBYJzD5Yxhee30Mh8UjQdk_N4-BWB4HnH5iT4z1AAjDD8L3HlQZaY6KvSN2DPb578wdPBkxsYmRoXfChRwtgFUp6HU0N7IEhfGJDElrrZbukizO-9Vdx-aHuoqtBZHxug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
توی ایتا و روبیکا، ناو جرالد فورد رو بمبارون و غرق کردن
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71180" target="_blank">📅 13:53 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71179">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71179" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71179" target="_blank">📅 13:52 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71178">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fx5NcWl8DRiRfNTpajur-iIW3s4AXiQ_GGPJ01sKp8U4oYtoshj4KKmp7qrbZooXoZsyyddTRYVtduhvrgFqka7Ldag-KwaITZtbpHS67wZqiAmUk4DMwi5CewtNt0zXEs_Z3ZU-oaigLywOxclmZVnzwqQxFpCS9mBDjP5r2IeiBUJxiSSUd4AlmpT3pJb5nZAp103O02wnZQMZXoEfCTN_0OSDHU-WpgeqwFqWOMroJB-3IljEvX3eohCASe2ab9ljqRO9Tqr3pGd-ztQH6i31qf3TEKZdfyPuYeVufpgl6A6dOW-rHFFSY8DL8a1JZP4qjtjv75KXQtv6pKSNbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
پیش‌بینی کنید
.
اورتون
🆚
منچستریونایتد
آرسنال
🆚
چلسی
آلومینیوم
🆚
استقلال
والنسیا
🆚
بارسلونا
یوونتوس
🆚
میلان
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز و برداشت آسان و امن
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71178" target="_blank">📅 13:52 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71177">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3c6743716.mp4?token=PrkExif217XxWt2UrKAcHdza4XCSEGS_2VOfcmrw1KRC4etRQjxs5zQN7iXg7kqt5H2kHcDM_0GZ6-XTLErkjIvW3grS_U4jJT9pwuNOXjGuGuLy5WR5c-uWSrBehjTnvbMzAMBir3hRZE3CQ2odr4i2RnjhFyu_eeKYDmQJWsJCh5dNF7f_l3gTTmC6ZekameCd3K8UInglw64H-DKf_6JTr8dIq7rE9nJVXXku9Nx_mMo9v-40eAl7ka0ceqUeOJVwjLTXhkUzb2S3J2Q7qBtqZ9jBykoDRitM8MV2vorsDaXuVNLd6rgWTyGJJ0NgVgIpu1j2w_fvIV1R8q65oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3c6743716.mp4?token=PrkExif217XxWt2UrKAcHdza4XCSEGS_2VOfcmrw1KRC4etRQjxs5zQN7iXg7kqt5H2kHcDM_0GZ6-XTLErkjIvW3grS_U4jJT9pwuNOXjGuGuLy5WR5c-uWSrBehjTnvbMzAMBir3hRZE3CQ2odr4i2RnjhFyu_eeKYDmQJWsJCh5dNF7f_l3gTTmC6ZekameCd3K8UInglw64H-DKf_6JTr8dIq7rE9nJVXXku9Nx_mMo9v-40eAl7ka0ceqUeOJVwjLTXhkUzb2S3J2Q7qBtqZ9jBykoDRitM8MV2vorsDaXuVNLd6rgWTyGJJ0NgVgIpu1j2w_fvIV1R8q65oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">〰️
سنتکام ویدئو غرق شدن نفتکش ایرانی در دریای عمان را منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71177" target="_blank">📅 13:12 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71176">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">⏺
🇮🇷
قالیباف:
آمریکایی‌ها باید دریافته باشند که دوران «پاسخ‌های متناسب» به سر آمده است.
حملات ما به پایگاه‌های متجاوزان تنها یک آغاز بود.
قواعد بازی تغییر کرده است.
از این پس، هرگونه تجاوز به منافع ایران، پاسخی سریع‌تر، سنگین‌تر و دردناک‌تر در پی خواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/71176" target="_blank">📅 12:44 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71175">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20d5a31326.mp4?token=tPz6mzjRydpzwq3ByFJWjrAemc2k0ZvMzBu28EMG88ELDW3s5gUvRhcYbsz0dpaS7j1leRl3mNWeiKUI7Dfdkq5QWjwTAB6GttB2iMiOGvqmS2FJrnOkGXTCP8HEu_orCS2bH0y3MD8EMaZLsjY3Wm4L3UExBs9gLzmO1jFlHTNsiRisIRlKN6JoQGqHgaCaamUGsePAEwA71TahpYwgIU7vclVIktvyIYS-WQTr3E2FsL7s5ZpXBt15aihu7j0sYP6yL86Jw5IDkL5J2mJdV-LNdFZOotl2FB5AsSiik_IAF-ec-hCkj7CawuiE2Uf7FuXMrA2tenhTGVoL5StlIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20d5a31326.mp4?token=tPz6mzjRydpzwq3ByFJWjrAemc2k0ZvMzBu28EMG88ELDW3s5gUvRhcYbsz0dpaS7j1leRl3mNWeiKUI7Dfdkq5QWjwTAB6GttB2iMiOGvqmS2FJrnOkGXTCP8HEu_orCS2bH0y3MD8EMaZLsjY3Wm4L3UExBs9gLzmO1jFlHTNsiRisIRlKN6JoQGqHgaCaamUGsePAEwA71TahpYwgIU7vclVIktvyIYS-WQTr3E2FsL7s5ZpXBt15aihu7j0sYP6yL86Jw5IDkL5J2mJdV-LNdFZOotl2FB5AsSiik_IAF-ec-hCkj7CawuiE2Uf7FuXMrA2tenhTGVoL5StlIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
قالیباف:بستن تنگه هرمز به ضرر ایران شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/71175" target="_blank">📅 12:01 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71174">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8313313bb.mp4?token=IGyOmiPODSsfi7xW7amJyDEtlq1v5HxBGaX4PCnHK5q6urgezvgPv95Tsah2HnV-qmv1X1csh4sgVU05OfY-g17au7iz92xWSXTiqGvN1dP05eCMlX0OcVTgDnuUUs7dFnla4kSZ0y32FmmF1qEtC0pfoVjbo5MHIuVbxkru9GJX56J3JdteEcJFbvH-Th66Q7QT0i1iXUAj8oDztunvwrsfEmKo-Tc37TAoHfwasCuehy2Lv28Qgn9Etl2uYY6QeE0R8JabtJkgi73n6cVHMPsRygDsnFXEUdsqUyUqs83ncJybVSV5W9O3XLDiHJNeh3eMI-g4d7ChlNvpdeXCOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8313313bb.mp4?token=IGyOmiPODSsfi7xW7amJyDEtlq1v5HxBGaX4PCnHK5q6urgezvgPv95Tsah2HnV-qmv1X1csh4sgVU05OfY-g17au7iz92xWSXTiqGvN1dP05eCMlX0OcVTgDnuUUs7dFnla4kSZ0y32FmmF1qEtC0pfoVjbo5MHIuVbxkru9GJX56J3JdteEcJFbvH-Th66Q7QT0i1iXUAj8oDztunvwrsfEmKo-Tc37TAoHfwasCuehy2Lv28Qgn9Etl2uYY6QeE0R8JabtJkgi73n6cVHMPsRygDsnFXEUdsqUyUqs83ncJybVSV5W9O3XLDiHJNeh3eMI-g4d7ChlNvpdeXCOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">〰️
ویدیویی که در توییتر فارسی به شدت در حال وایرال شدنه
😃
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/71174" target="_blank">📅 11:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71173">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f8295abc0.mp4?token=P_-zZnBzIXhNpQZp7mD2zxgDwzbgnz0FXrt0zp7rYLvAevAHjrulN0rvLKPvST1EKC6O0qbd2IdIRifGBXdBDCpxCttbnpkptYtprYRJVhn3zcv2u6lyLTg8caqxt5hsdxyJCl5z4nj9LWGiMGqLmz6y9Pl5NAO2F_4rfaj_5XSAVkq3VAaEIpNL4TCxrCESyx417S2UB2Ue8MGqOmDx3WryLZLrNGGD04czatPKdVeidJg7E_BRK7oTAEs-4PTGZNI3s7s2-_AR1k6GBAB_gMFhujufXOYez7QkVJElvTB-4xVJhNfsYRJfQ9vh2OCKA5v_dNxcOuo9P_HWE50sgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f8295abc0.mp4?token=P_-zZnBzIXhNpQZp7mD2zxgDwzbgnz0FXrt0zp7rYLvAevAHjrulN0rvLKPvST1EKC6O0qbd2IdIRifGBXdBDCpxCttbnpkptYtprYRJVhn3zcv2u6lyLTg8caqxt5hsdxyJCl5z4nj9LWGiMGqLmz6y9Pl5NAO2F_4rfaj_5XSAVkq3VAaEIpNL4TCxrCESyx417S2UB2Ue8MGqOmDx3WryLZLrNGGD04czatPKdVeidJg7E_BRK7oTAEs-4PTGZNI3s7s2-_AR1k6GBAB_gMFhujufXOYez7QkVJElvTB-4xVJhNfsYRJfQ9vh2OCKA5v_dNxcOuo9P_HWE50sgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
به گفته آقای دکتر اگه می‌خوای سرطان پروستات نگیری، باید ماهی ۲۱ بار سکس کنی...!
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/71173" target="_blank">📅 11:02 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71172">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b321711db4.mp4?token=OdLyg0HwYtC9oRbffM8fcPGu4EId9qE6DovNLNIs7tLQFfaOJ04sJm0Q8rETrYi5JHG4_97X2pSFBz3iRKj_tyssmTYTZHDUYbFWGh_QtgUrMdKME7mg0QN0PHmUjneKB8hxL03Cc1LH3F1awekeprk_b22bM9lZls-66lc2kGknA3KqHOEEj_8BquAID2UjQX-0B1BTACmt0Gc54Z5y-ls7OweZ_hRhTgFYosf-8ypkuNHWJR-yzo_Tk9WDgmPHBFGfIDA6fZmEEpczvZImZ6o6GOe9HbxyzfLzWRjRJRqcLY2OOGzMlV1ME-V-gJ-qPRBTKrURq_j_6pHcLjxSwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b321711db4.mp4?token=OdLyg0HwYtC9oRbffM8fcPGu4EId9qE6DovNLNIs7tLQFfaOJ04sJm0Q8rETrYi5JHG4_97X2pSFBz3iRKj_tyssmTYTZHDUYbFWGh_QtgUrMdKME7mg0QN0PHmUjneKB8hxL03Cc1LH3F1awekeprk_b22bM9lZls-66lc2kGknA3KqHOEEj_8BquAID2UjQX-0B1BTACmt0Gc54Z5y-ls7OweZ_hRhTgFYosf-8ypkuNHWJR-yzo_Tk9WDgmPHBFGfIDA6fZmEEpczvZImZ6o6GOe9HbxyzfLzWRjRJRqcLY2OOGzMlV1ME-V-gJ-qPRBTKrURq_j_6pHcLjxSwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇹🇷
این پسر بچه ارومیه ای که چند وقت پیش با ویدیوش که در حال آهنگ خوندن بود توی اینستاگرام به شدت وایرال شد حالا یه کمپانی بزرگ از ترکیه اومده و باهاش قرارداد همکاری بسته؛
فعلا این قرارداد واسه اجرای کنسرت های مختلف تو ترکیه‌ست
رئیس کمپانی میگه که این تازه اول راهه و قراره بزودی تو سراسر جهان کنسرت برگزار کنیم...
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/71172" target="_blank">📅 10:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71171">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99e529d142.mp4?token=RjilQo2UquTHWJvn74Sil8siBQxvEmVH_ESXgDdXprU8xvnxDbXP_zyWrKJGvweoz8fdfCmr_n1uajbFbM_HivBh15fayV-pdIFrBrR7kxqwQTZLBkaO2b0b3MNg6k3IKuJntdjXpykS2WqRwylTwZx1xXFXu2OgCo_cGNB4qQBVoHHI9edmSL8GDN35h1sP7bP1q_b6Zj2uX2dyXssiiGcpI0ngEDRjtn9Sg6Yurawi_NO-OWo8u641WgNXXhQ-MJ8O-nT8wB9tD2gMlya9P9IDIL2Mqw1grT1PdOYcm669G_sg9bnw_HZB_CEWEcARcgwuc_Oe5n-IaVosdZ_b2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99e529d142.mp4?token=RjilQo2UquTHWJvn74Sil8siBQxvEmVH_ESXgDdXprU8xvnxDbXP_zyWrKJGvweoz8fdfCmr_n1uajbFbM_HivBh15fayV-pdIFrBrR7kxqwQTZLBkaO2b0b3MNg6k3IKuJntdjXpykS2WqRwylTwZx1xXFXu2OgCo_cGNB4qQBVoHHI9edmSL8GDN35h1sP7bP1q_b6Zj2uX2dyXssiiGcpI0ngEDRjtn9Sg6Yurawi_NO-OWo8u641WgNXXhQ-MJ8O-nT8wB9tD2gMlya9P9IDIL2Mqw1grT1PdOYcm669G_sg9bnw_HZB_CEWEcARcgwuc_Oe5n-IaVosdZ_b2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
🇱🇧
خبرنگار جمهوری اسلامی در لبنان:
اعضای سپاه پاسداران در تپه‌های علی‌الطاهر، به دلیل محاصره اسرائیل، در شرایط عاشورایی قرار دارن.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/71171" target="_blank">📅 10:04 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71170">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a662811c73.mp4?token=WxqRS78o4j008rPwBBxGKlz-5Xa850nT6vPYucqdN0AzQZtnuRBsS5tM3SncAuRsk-LHu4KaXdxeNGte6whKgsEFGmgG951bk0w7v_hRFl97t-GKs3kXrcCDcyiUMYNUigeYB9GnBesVpZhvSriyXj40DcDREtT3_8RYPKALtAn3sOvfPDQeF4hlZgVi8Q5NXALosk51ptoKcLX8nu6FZOeMg7AIwAFUCpqIv4sMXLXYkIEomeUpq_hlYSXezLcMsz28iTrQOelsGZUMIO6ae-KKWDxjdbqVA9JKwdKog6bCVnzGIZ443_QxNNNXTxe0H2TnQoSv92D1JNOQvmpmSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a662811c73.mp4?token=WxqRS78o4j008rPwBBxGKlz-5Xa850nT6vPYucqdN0AzQZtnuRBsS5tM3SncAuRsk-LHu4KaXdxeNGte6whKgsEFGmgG951bk0w7v_hRFl97t-GKs3kXrcCDcyiUMYNUigeYB9GnBesVpZhvSriyXj40DcDREtT3_8RYPKALtAn3sOvfPDQeF4hlZgVi8Q5NXALosk51ptoKcLX8nu6FZOeMg7AIwAFUCpqIv4sMXLXYkIEomeUpq_hlYSXezLcMsz28iTrQOelsGZUMIO6ae-KKWDxjdbqVA9JKwdKog6bCVnzGIZ443_QxNNNXTxe0H2TnQoSv92D1JNOQvmpmSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
شاهین نجفی:
هرکسی رضا پهلوی رو مورد انتقادهای عجیب غریب قرار میده و میزنتش یه سرش وصل میشه به جمهوری اسلامی
اینا جوگیر شدن چهارتا شعار دادن و حرف زدن بعد دیدن اینجا خبری از سهم دهی به کسی نیست مسیرشون رو عوض کردن
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/71170" target="_blank">📅 09:33 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71169">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2d150aea8.mp4?token=kfn0FhbdpqnGteAGHEhvsz0t4gblCXYRuBq1xHvHfN00wSNTaVr01ps08-B-8Gx8Jt5VVvddSGqP4VkB2TKeueaMjppial8fCdlp0LC0l7U03AVPJ-PVEeAOO0nRjeQQIovHnYP77e1fHx0MMOOKM5EcFqswKd9buoHDj1bPea8fwSSkuQR-U2OETZ_1qxGYoJ1smxYz9vRyPbxOKINPIWecZb9MJ7bwr6xBCM8vYUPD6CBLQcpAsCLyPURnwzhbHbjH2tZX9YCA38zProFYEIDFZuGmrNUisuqcPZyJ0odVk3fYY7HNvO5DFQLWxqHGYSsI_PSDr9ZY6wGwcojlRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2d150aea8.mp4?token=kfn0FhbdpqnGteAGHEhvsz0t4gblCXYRuBq1xHvHfN00wSNTaVr01ps08-B-8Gx8Jt5VVvddSGqP4VkB2TKeueaMjppial8fCdlp0LC0l7U03AVPJ-PVEeAOO0nRjeQQIovHnYP77e1fHx0MMOOKM5EcFqswKd9buoHDj1bPea8fwSSkuQR-U2OETZ_1qxGYoJ1smxYz9vRyPbxOKINPIWecZb9MJ7bwr6xBCM8vYUPD6CBLQcpAsCLyPURnwzhbHbjH2tZX9YCA38zProFYEIDFZuGmrNUisuqcPZyJ0odVk3fYY7HNvO5DFQLWxqHGYSsI_PSDr9ZY6wGwcojlRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
صداوسیما آمار رسمی کشته شدگان اسرائیل تو سه روز اول جنگ رو منتشر کرد:
۶عدد ژنرال ارشد اسرائیلی
۳۲ نفر مامور موساد و ۷۸ نفر مامور شین بت
یازده دانشمند هسته‌ای
۱۹۸ نفر افسر نیروی هوایی
۴۶۲ سرباز و ۴۲۳ نیروی ذخیره ارتش اسرائیل کشته شدند
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/71169" target="_blank">📅 09:01 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71168">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🇺🇸
🇮🇷
سپاه پاسداران انقلاب اسلامی ساعاتی قبل در بیانیه ای مدعی حمله به یک ناو هواپیمابر و یک ناوشکن آمریکایی شد و اعلام کرد که پس از این حمله اونا خسارت دیدن، ترسیدن و از منطقه فرار کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/71168" target="_blank">📅 08:02 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71167">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71167" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/71167" target="_blank">📅 01:34 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71166">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cEGFGNpJx1wJqxLX3XEqjfdPrxT94KcK5ege85d5MHGInm8seHJZSAX09fz-7Q1AKZOQFlssG0F5fgW30WfYl7EirJK0zbMiXgL1VY3HCM5u6wyH11vKqncGx_zoP45Rg9uY0WaSK2kN6Z9nR55KxH8sr1IOgtuZQGs0MBx_Tp1r6ncUCpM92bOaOjWikQvu2sbAp2B4fiKu4q-Ux6TwSQq1c_M_epTsDI46FQCigUt3WwGYu05rKfvTn5h9n1C-k0FNkLUPEPCxdL6Vxho5KYu7xInRCHeaHHkgEGBU3aW2zX7_-tqBq7J2lNBN7h4JI1sdCabBVfbaagMH7L26BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
تنیس US Open داغ‌تر از همیشه دنبال میشه!
🦖
مسابقات جذاب
US Open
رو در
TrexBet
پیش‌بینی کنید، هیجان رقابت‌ها رو بیشتر کنید و برای جوایز جذاب وارد رقابت بشید!
🦖
فرصت هیجان
US Open
رو از دست ندید!
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/71166" target="_blank">📅 01:34 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71165">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ویس فحاشی خداداد</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/news_hut/71165" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🚨
🚫
فوتبال مملکت هم اوضاع جالبی داره.  خداداد عزیزی امشب کلش فوق‌العاده کیری شده و اینجوری خواهر و مادر امید عالیشاه رو به فوش کشیده
😳
😳
😳
😳
😳
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/71165" target="_blank">📅 01:04 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71163">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c0f365bbb.mp4?token=af2xkcBum99VXfVsEifSPbUKt1HoIZR_0D28waW9nq0HjF65gzhzjoMTo38TukZJR-Elh9aoCcbH5WavJQNfLZdfyGFsi_83oDJBSMKAOD1PwgiwPE8k4WbhRAzjD6Uwfh-4BrA1Lba1e1b82K6xmaPf71UuLPwFFzR3dBmhcABNW6-P1dApypQNISaucqBliY3pti0E2cd3PfVD4SyW5YNPbR3OrWzkw-TormUPj5NL56vo1zbGdd2UtbA3tF7SsJ-7I6wX3t-6aKgY9tHCLB7SFWNJDMmyyQtwxumPv3vuu2nUuSNzDznEa43q4MC_g2ojVvfNnSjxKCJ6TV8Vag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c0f365bbb.mp4?token=af2xkcBum99VXfVsEifSPbUKt1HoIZR_0D28waW9nq0HjF65gzhzjoMTo38TukZJR-Elh9aoCcbH5WavJQNfLZdfyGFsi_83oDJBSMKAOD1PwgiwPE8k4WbhRAzjD6Uwfh-4BrA1Lba1e1b82K6xmaPf71UuLPwFFzR3dBmhcABNW6-P1dApypQNISaucqBliY3pti0E2cd3PfVD4SyW5YNPbR3OrWzkw-TormUPj5NL56vo1zbGdd2UtbA3tF7SsJ-7I6wX3t-6aKgY9tHCLB7SFWNJDMmyyQtwxumPv3vuu2nUuSNzDznEa43q4MC_g2ojVvfNnSjxKCJ6TV8Vag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سپاه پاسداران تصاویری از «رصد و رهگیری شناورهای متخلف» در تنگه هرمز منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/71163" target="_blank">📅 00:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71162">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e9440ae83.mp4?token=P-wphfcgTeOR0164NlCeDEWi2VDaGFB3W-3_WV611_7bIfMda8-gBsev-bzocLQ5XgcHsXpGK4baHcDXninx8FZoxoYXGdjtZgaxEuiRSTYe5ZHPeZKF0H6QYh5i7RPZNm54SyEjBiCthUu0akNz3cLg9Vvy-bDWP_I0E4jVRV3G0zb2mhQnjgSEOMPVIr1uDgEAEmBh9GmYdwCWiM7ioW0qmB7gFnh_fju03U9laxDwUxW1IKJu1T9-C0rhnVMwxusdEz5gdkkavXYthskGq_YnhPihHTBLYXocjI2Ndkx0Km3nshrlQFeWNHBTIekRW16ZXb1WsK2UF8JhW2Ubbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e9440ae83.mp4?token=P-wphfcgTeOR0164NlCeDEWi2VDaGFB3W-3_WV611_7bIfMda8-gBsev-bzocLQ5XgcHsXpGK4baHcDXninx8FZoxoYXGdjtZgaxEuiRSTYe5ZHPeZKF0H6QYh5i7RPZNm54SyEjBiCthUu0akNz3cLg9Vvy-bDWP_I0E4jVRV3G0zb2mhQnjgSEOMPVIr1uDgEAEmBh9GmYdwCWiM7ioW0qmB7gFnh_fju03U9laxDwUxW1IKJu1T9-C0rhnVMwxusdEz5gdkkavXYthskGq_YnhPihHTBLYXocjI2Ndkx0Km3nshrlQFeWNHBTIekRW16ZXb1WsK2UF8JhW2Ubbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇬🇷
یک فروند جنگنده F-4 فانتوم نیروی هوایی یونان در جریان رویداد «هفته پرواز آتن» در پایگاه هوایی تاناگرا سقوط کرد و دو خلبان این جنگنده کشته شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/71162" target="_blank">📅 00:14 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71161">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a02f1d06a.mp4?token=bJtchC4P5tSitmSnsZBk4889ZZoXHWE6HG_RqQpLFQ1Afeu4dqo494TcI7UoWHyV54Johh5i9xVREiok-9I3PSeIna5QTMbPEtgDc22RhATGqDsBWjSNihH8gvQHuUM61JYNpmA5P67z_yENQDHFaZyAsxVur7hAzyCLWzRtT2BKaq1qU-vmeMSN94yyn9lrWPHX5BPvTATr_uj_EPoLHTicdISdwbPdlAURujxwIdnVxlnWResD1u2zAt8nyuwBqETcDkxliUPhQ1uW3LyQ9bKY0-5ZmzF-i2kfajPNN7NlBW9gqGqKJCssQL1XDiSbsidMOl_9D7sLQxqeEln0_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a02f1d06a.mp4?token=bJtchC4P5tSitmSnsZBk4889ZZoXHWE6HG_RqQpLFQ1Afeu4dqo494TcI7UoWHyV54Johh5i9xVREiok-9I3PSeIna5QTMbPEtgDc22RhATGqDsBWjSNihH8gvQHuUM61JYNpmA5P67z_yENQDHFaZyAsxVur7hAzyCLWzRtT2BKaq1qU-vmeMSN94yyn9lrWPHX5BPvTATr_uj_EPoLHTicdISdwbPdlAURujxwIdnVxlnWResD1u2zAt8nyuwBqETcDkxliUPhQ1uW3LyQ9bKY0-5ZmzF-i2kfajPNN7NlBW9gqGqKJCssQL1XDiSbsidMOl_9D7sLQxqeEln0_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
یه خانم درباره اقتصاد:
چرا مردم هر چی گرون میشه از زاویه ی آدمای متوسط بهش نگاه می‌کنن؟
خونه از ۵ میلیارد شده ۵۰ میلیارد.
گوشت از ۵۰۰ تومن شده ۴ میلیون.
سود شما چند برابر شده.
مردم از گرونیا دارن سود میکنن، مردم باید دیدگاهشون از آدمای متوسط جامعه تغییر بدن و بگن هر چی گرون میشه خب ما هم سودمونو داریم میبریم
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/71161" target="_blank">📅 23:32 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71160">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2d7d2ec60.mp4?token=GeKbZPrzpHY0hY5kssPqIK49Fix0jaBpK67UrXjCN8FaZE2giwsxJFEeJDReI8pQ5RyEhH3lDSYeEs3GhOMx06OgMstKO5LHaRIAhpACHbTYm81exhqFqyT1J7n2ehOcXRZwwx3dGpZZYF8G62DqMyBvnW8ZyLVaHqf-1Ay4jp4zpQnEo9tlP-XnN17EFjlc5HNa9q7yq9oeyvIBbY6PgEduM5fFVUHsfSjWjRyNr2eVxuJCZNWs8okeob57M6awCNpo7jwxi7Wppqxi53fPpOLf89oUh10VvXolhBiGJ1FsS4qoMZP1CDRg6n5u53Il86GEkteZhAmdkU7c2KzrIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2d7d2ec60.mp4?token=GeKbZPrzpHY0hY5kssPqIK49Fix0jaBpK67UrXjCN8FaZE2giwsxJFEeJDReI8pQ5RyEhH3lDSYeEs3GhOMx06OgMstKO5LHaRIAhpACHbTYm81exhqFqyT1J7n2ehOcXRZwwx3dGpZZYF8G62DqMyBvnW8ZyLVaHqf-1Ay4jp4zpQnEo9tlP-XnN17EFjlc5HNa9q7yq9oeyvIBbY6PgEduM5fFVUHsfSjWjRyNr2eVxuJCZNWs8okeob57M6awCNpo7jwxi7Wppqxi53fPpOLf89oUh10VvXolhBiGJ1FsS4qoMZP1CDRg6n5u53Il86GEkteZhAmdkU7c2KzrIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه جانفدای رندوم و حرکات جالبش
😃
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/71160" target="_blank">📅 22:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71159">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66b1ca1096.mp4?token=dJ8hkq6iQRJN8HuABT9TZy3X2DwyDKPmelFb2o01xBNg7AyxLzZMYsxD8RrO82pnSqQqnUS2fwN1X_nFdMX53K_4cTLJRU7Zi-B_FQLiRyqNKxLgktD0EACbfnGz5ESWBpwXmdmGvPG_6cpjklY02NwDnQzq-StB32ak5-0NHsG_2pyDkz5rrewtSVi266zarNZe6JRmLJwha5JeyS0wvNP0BqxCPKXHUVeoPKLW7LLg0rq3a0_Zux8kUaR51R0kUwMyT5uld5hp5dMfFthzbbnUxTAqfoit191lvzYIMiizaUS8ucs-GzUbwTmf5qc6VLNmJ5oGRqeLz5DafAmctA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66b1ca1096.mp4?token=dJ8hkq6iQRJN8HuABT9TZy3X2DwyDKPmelFb2o01xBNg7AyxLzZMYsxD8RrO82pnSqQqnUS2fwN1X_nFdMX53K_4cTLJRU7Zi-B_FQLiRyqNKxLgktD0EACbfnGz5ESWBpwXmdmGvPG_6cpjklY02NwDnQzq-StB32ak5-0NHsG_2pyDkz5rrewtSVi266zarNZe6JRmLJwha5JeyS0wvNP0BqxCPKXHUVeoPKLW7LLg0rq3a0_Zux8kUaR51R0kUwMyT5uld5hp5dMfFthzbbnUxTAqfoit191lvzYIMiizaUS8ucs-GzUbwTmf5qc6VLNmJ5oGRqeLz5DafAmctA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساعاتی پیش تو مسیر پلیس‌راه همدان ـ سنندج، یه ماشین سنگین گویا ترمز می‌بره و مستقیم با یه دستگاه تانکر حامل سوخت برخورد می‌کنه و یه انفجار وحشتناک رخ میده!
متاسفانه تا الان 7  جونشون رو از دست دادن...
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/71159" target="_blank">📅 22:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71158">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3aea156fe3.mp4?token=L9jVFTl7oQm7glOaTvBDFvEj2K5qDUwVGf84K7Gq1BDNvQtmpLqSfX0FBCWN8_M4_JWIQmKBMP_xei7jjrTzg5Hou-_qq8DNXXjGz5UKbHqa_RzulfxzeK6Z7P-mvunl9se-4Ck3S7ANecv7z5XCytamhTZYv8JQOl0LpFGxyFmEaDRmJhjazFBKZArz7XUk95mzbix9W82GBaplom-YDLttobHW-nzreHRKultlF093rVO5-QzABtdxy9QwOI_AWtyJTRpkuTl1hdoo82JkNHfyBo0IEM8YQlkL5yLpiAQWK83yyHw33_O_9mSVcJ-dCIRpi-9Tm05h5xQnPsPx7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3aea156fe3.mp4?token=L9jVFTl7oQm7glOaTvBDFvEj2K5qDUwVGf84K7Gq1BDNvQtmpLqSfX0FBCWN8_M4_JWIQmKBMP_xei7jjrTzg5Hou-_qq8DNXXjGz5UKbHqa_RzulfxzeK6Z7P-mvunl9se-4Ck3S7ANecv7z5XCytamhTZYv8JQOl0LpFGxyFmEaDRmJhjazFBKZArz7XUk95mzbix9W82GBaplom-YDLttobHW-nzreHRKultlF093rVO5-QzABtdxy9QwOI_AWtyJTRpkuTl1hdoo82JkNHfyBo0IEM8YQlkL5yLpiAQWK83yyHw33_O_9mSVcJ-dCIRpi-9Tm05h5xQnPsPx7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
وزیر نیرو:
دیگر قطعی برق برنامه‌ریزی‌شده نداریم
اگر مردم جایی دیدند به سامانهٔ ۱۲۱ اطلاع دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/71158" target="_blank">📅 21:42 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71157">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31160c5df1.mp4?token=bwauOkyrX8ZigVruuOpbvVcjpK7KPkWsnxlIbubU-frBwQjucaTAx30ZTT09mdGStFPbZCME9NveuIfBUGCYxIRhaGsU0ZMwYjwbtY1Aw3Oaql-9pSfOh9y2VwEa1-UvH-JOPNwFxLZQw7jdJ39pW1tdShjDzm9huTWWjajx_4sy-t7HSXsehI2lKxOLGIcEdMA0QNwENSJqYYT2NVbBuWi6yoPPVZX5yHVJb7SQshxwyqqGhWQNABNQollG36M72TdMNdmLEknvxXd1ttvAVjjqci-1S3Uq6qX4jzvHHF1XueiWSSBBy78lLB3eMFJNuQnLesQu53qbJUtEwfhY_Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31160c5df1.mp4?token=bwauOkyrX8ZigVruuOpbvVcjpK7KPkWsnxlIbubU-frBwQjucaTAx30ZTT09mdGStFPbZCME9NveuIfBUGCYxIRhaGsU0ZMwYjwbtY1Aw3Oaql-9pSfOh9y2VwEa1-UvH-JOPNwFxLZQw7jdJ39pW1tdShjDzm9huTWWjajx_4sy-t7HSXsehI2lKxOLGIcEdMA0QNwENSJqYYT2NVbBuWi6yoPPVZX5yHVJb7SQshxwyqqGhWQNABNQollG36M72TdMNdmLEknvxXd1ttvAVjjqci-1S3Uq6qX4jzvHHF1XueiWSSBBy78lLB3eMFJNuQnLesQu53qbJUtEwfhY_Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
جان بولتون دیپلمات آمریکایی درباره ایران:
من معتقدم — و دهه‌هاست که چنین نظری دارم — که تنها راه دستیابی به صلح و امنیت واقعی و پایدار در خاورمیانه، خلاص شدن از شر رژیم تهران است.
به گمانم حملات آمریکا و اسرائیل آسیب قابل‌توجهی به این رژیم وارد کرد.
بی‌شک ما اشتباهات زیادی مرتکب شدیم.
اما اگر اراده کنیم که درباره چگونگی انجام آن به‌درستی بیندیشیم، این هدف همچنان قابل‌تحقق است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/71157" target="_blank">📅 21:19 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71156">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
صداوسیما:
صدای انفجار هایی که در جزیره قشم شنیده شده مربوط به شلیک موشک ها به سمت شناور های متخلف در تنگه هرمز است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/71156" target="_blank">📅 21:04 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71155">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed43299c5.mp4?token=dS6JoJPSFaunMrx_ymZ_HFwuLEQUWxA9ylYHLnaaEMWJiuIV5p1R1FiuyCkJ6ARjXjyB0fUzK8CLfYO9QgIHKG9nJRpjpTK0rPwYCF9OLfA78wonE114yZPsJM2cKevYQx_QEH4Dt8pXhG6LF-ZF9RsiACG1Ta82OTVox0EPlP61QC8GgPpCurgTBhA8LN7j3SdJz3PqpFoqnD6Kb6u4MW2IK2Hct8s-4zhrjyq8TQoJJh8ThVfQAK5K-qWROArt-_4uDdoREGTMQ_J-RBJCacM-YZJBfVzxLM30TOai7OZ1cG0nZ_NGbkiMbWz6nC9JYVxYXSnsdqFQAEY-joSMMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed43299c5.mp4?token=dS6JoJPSFaunMrx_ymZ_HFwuLEQUWxA9ylYHLnaaEMWJiuIV5p1R1FiuyCkJ6ARjXjyB0fUzK8CLfYO9QgIHKG9nJRpjpTK0rPwYCF9OLfA78wonE114yZPsJM2cKevYQx_QEH4Dt8pXhG6LF-ZF9RsiACG1Ta82OTVox0EPlP61QC8GgPpCurgTBhA8LN7j3SdJz3PqpFoqnD6Kb6u4MW2IK2Hct8s-4zhrjyq8TQoJJh8ThVfQAK5K-qWROArt-_4uDdoREGTMQ_J-RBJCacM-YZJBfVzxLM30TOai7OZ1cG0nZ_NGbkiMbWz6nC9JYVxYXSnsdqFQAEY-joSMMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
تصاویر منتشرشده نشان می‌دهد یک کشتی کانتینربر در اسکله بوشهر تقریبا به‌طور کامل نابود شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/71155" target="_blank">📅 20:33 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71154">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
سازمان تجارت دریایی بریتانیا UKMTO:
گزارش‌ هایی مبنی بر وقوع حوادث برای چندین کشتی تجاری در شمال خلیج فارس و دریای عمان دریافت کردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/71154" target="_blank">📅 19:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71153">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5717843ac.mp4?token=VttY82I_XORKHhVPfZRcrFzNb48aOMZw8kewXBI8GBH1aPUOq4BPrVruodWE9CxTOBrSAp66Mh4bndZQePLNATXGI8QkrYa-Xje9lPJIJQiybUAfyxSjBWr8osAa6CSSFgLmj5u8377yXXRidBm_tgserDAIvimcTQatDswg_tMwH2t_TBqwl7uZTHgbAvsIc2NLty3OxueEpOzDeJuAgxGyJDrYs8M-6PfDbWBJp-yWhzYsNBaqOwzMAy5mQ9OJp8ywoV5Yyvp9y8jd-PZW1rhA1kGRQPlNevdkACvjzRe_vHhF_Vll5x9UnK5-x9sciDq9jrZlDMWBs_gI-BmEBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5717843ac.mp4?token=VttY82I_XORKHhVPfZRcrFzNb48aOMZw8kewXBI8GBH1aPUOq4BPrVruodWE9CxTOBrSAp66Mh4bndZQePLNATXGI8QkrYa-Xje9lPJIJQiybUAfyxSjBWr8osAa6CSSFgLmj5u8377yXXRidBm_tgserDAIvimcTQatDswg_tMwH2t_TBqwl7uZTHgbAvsIc2NLty3OxueEpOzDeJuAgxGyJDrYs8M-6PfDbWBJp-yWhzYsNBaqOwzMAy5mQ9OJp8ywoV5Yyvp9y8jd-PZW1rhA1kGRQPlNevdkACvjzRe_vHhF_Vll5x9UnK5-x9sciDq9jrZlDMWBs_gI-BmEBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
✈️
ویدیویی تایید نشده از پرواز تانکر سوخت‌رسان آمریکایی به همراه دو جنگنده در آسمان جزیره کیش استان هرمزگان
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/71153" target="_blank">📅 19:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71152">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71152" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/71152" target="_blank">📅 19:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71151">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V01-aM1JmhmvEZ0TTKcMJD6GEPt8O5xEbNwowibatkLwni9R3ucvtpGjGl_1_eTy2Wo45tw4n0SpEDl2qzQlHIy_qnZUR89lUfI5OsTgiAztqnqrfHKqXuxq2CbCbWNeLkwsLZYolQb0zzG_dzv3KraqBmIKhex4U_qXP6IYAtbxFlJ-zno4g62Pa612Qs85Ihz1GrY_lCtonz0tlYY2WPa7Jtxhs7ucAUc4LoKRKP3s-L7m5hjkQiQbyq-qYk6QMIEglBvEojJllN7sg_0ri55kVerP8XTOgcmD4Wbcgd_pzl7vyH06zos1zQeHDTnVIU0xR579Bzj2SVO3m5JzHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
بازی جذاب اینتر
🆚
ناپولی را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید.
📊
نگاهی به آمار دو تیم:
اینتر: ۲ بازی ۲ برد و کسب و ۵ گل زده
ناپولی: ۲ بازی ۱ برد و ۱ شکست و ۳ گل زده
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/71151" target="_blank">📅 19:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71150">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf5e996b2c.mp4?token=auL9-C1OmcjWkUTtSU03UUCDH-vVR0Vh43AuheK6z1xKn4p2CHz_saFrImmHYY7eJPafgv2ZSjoKP98gTHty5S1YsFnU9wA5Z_sM9thof-J7zKe6fW5lfyHQdxakFxMAumaJOC-Ff4bUU6W1LP-Y4gZFh6J3bTkCAQX_WiyAPSL4Yh-si6jY6CMJ0TYo0sjRi_A0L-eS8Ior18YKQRjm4hP1ckVifkzfTeg6MBbI72drVvqU3xV1c5SNiZFRLeWlhE0VXkypWUEGYUgJwyxTGZ5y4-ARHfZYcMC0BNnUR2L_oICjFruIj9Vd2hNZvLK0iHn1fLySbBl6gOZb-DPIS5yK65ElakfxdscF305YZmIcEni_0wyrsq3-Cbwtt6WSYkeaivZGjfMcjrqJ2V4jKvFUBs5K9iE3T4buqIpp7NcYgPQN6ig7Pp1MQ6gN7fjGSenaCWbsIuhhmmRzZkvkY8kxoZiB70kZlkrlf8kMnwfxOXKFttxmxeDh8Uy1KT4ZReeNY1wbx0dRV29FErAXbkKm6ZQEaSvkMmjsQWHPqyrYSnjyj4t0pQ49GrG2sDtnV8uL6D5qEDXb1dRRxk8wn-AjsWbmL_PD-uGfq-KPEB-xecA2NwFJrCGsUAtPuDxbDkAugMjVUaFHnPvbpwIe-B3OhS8GfuUypqfeChxFxiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf5e996b2c.mp4?token=auL9-C1OmcjWkUTtSU03UUCDH-vVR0Vh43AuheK6z1xKn4p2CHz_saFrImmHYY7eJPafgv2ZSjoKP98gTHty5S1YsFnU9wA5Z_sM9thof-J7zKe6fW5lfyHQdxakFxMAumaJOC-Ff4bUU6W1LP-Y4gZFh6J3bTkCAQX_WiyAPSL4Yh-si6jY6CMJ0TYo0sjRi_A0L-eS8Ior18YKQRjm4hP1ckVifkzfTeg6MBbI72drVvqU3xV1c5SNiZFRLeWlhE0VXkypWUEGYUgJwyxTGZ5y4-ARHfZYcMC0BNnUR2L_oICjFruIj9Vd2hNZvLK0iHn1fLySbBl6gOZb-DPIS5yK65ElakfxdscF305YZmIcEni_0wyrsq3-Cbwtt6WSYkeaivZGjfMcjrqJ2V4jKvFUBs5K9iE3T4buqIpp7NcYgPQN6ig7Pp1MQ6gN7fjGSenaCWbsIuhhmmRzZkvkY8kxoZiB70kZlkrlf8kMnwfxOXKFttxmxeDh8Uy1KT4ZReeNY1wbx0dRV29FErAXbkKm6ZQEaSvkMmjsQWHPqyrYSnjyj4t0pQ49GrG2sDtnV8uL6D5qEDXb1dRRxk8wn-AjsWbmL_PD-uGfq-KPEB-xecA2NwFJrCGsUAtPuDxbDkAugMjVUaFHnPvbpwIe-B3OhS8GfuUypqfeChxFxiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
🇮🇷
لحظه تهدید تخلیه خدمه نفتکش های جمهوری اسلامی توسط خلبان جنگنده ارتش آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/71150" target="_blank">📅 18:59 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71149">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
〰️
⭕️
سنتکام مسئولیت حمله به نفتکش های ایرانی را گردن گرفت؛  پس از شلیک موشک‌های بالستیک سپاه به سمت دو ناو جنگی آمریکا، نیروهای آمریکایی ۳ نفتکش حامل نفت خام ایران را هدف قرار داده و از کار انداختند. دو نفتکش نزدیک خارک و جاسک هدف قرار گرفتند و یک نفتکش دیگر…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/71149" target="_blank">📅 18:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71148">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eo8FZ1-DhoJGDNZOO_VioHzUPeijNz8vdrLsa9mBbeXITWlyy7pv8w-WsVGFq6kq5EkymyJhst6LR7V9qGJSdO7ycEmSZVTP5T61bXqh2sSXtetm-S4bSrXyrU3YDyCNhhEf3ABNtPq2Jkg7HJFC8UKLI6qBueER6x8YmSdjtQZm-GW6H8zIi13GRavkUZu1Ca4pj5a8qel2E-m_4lsZ2hwR0Lco2E595NSogESQ96TD_QGNe2Z4Xx5WeugTP2HxatJ3IMEbo52PE3rM7oDn7iuSqDjiz87yW0jJSd0pmandEdcaUcfrs2D1YolkruQQUUmGvwHcIwUcpxmxYuBhPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
🇧🇭
سفارت ایالات متحده در بحرین:
با توجه به تنش‌ها در خاورمیانه، وضعیت امنیتی همچنان پیچیده است و احتمال تشدید غیرمنتظره اوضاع وجود دارد.
سفارت ایالات متحده به شهروندان آمریکایی یادآوری می‌کند که ایران پیش‌تر زیرساخت‌های غیرنظامی در بحرین، از جمله هتل‌های منامه، را هدف قرار داده است.
آمریکایی‌هایی که در حال حاضر در خاورمیانه حضور دارند، باید هوشیاری خود را افزایش دهند و نسبت به احتمال لغو پروازها، بسته شدن حریم هوایی و اختلال در سفرها آگاه باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/71148" target="_blank">📅 18:17 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71147">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1d8dfb05eb.mp4?token=TM5AT0xAVklv7AZK6Vykj9C3x_qpwI9djjEXu8itwYkNTo9l5uQB-UZFKruNYazqylBBbTfIidjikZQl4InqqHo-nUIbZxOavhLMFKGAc9cp99yyV0FeqUtvtPd6AsxOE50sA2sjMZn5gJ7X5WV8L3VbKRUDSc40cOipkc6LEzctuGNioNNPVtGr1a_dGJjry7AJNgm-XNP8wHuWh0VqTIGobrVzK5t9wtSO2eAyZtQQhdAHUDOE7fD8I2d-GXg9n7qAakA5Snk9jM4J9dZlp_F2hvacDJyRLOGk8MxWS2MYwzt0bqlbTYVoJ0Te7Ng0KPcG7C9YDluV7mrzbJDZYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1d8dfb05eb.mp4?token=TM5AT0xAVklv7AZK6Vykj9C3x_qpwI9djjEXu8itwYkNTo9l5uQB-UZFKruNYazqylBBbTfIidjikZQl4InqqHo-nUIbZxOavhLMFKGAc9cp99yyV0FeqUtvtPd6AsxOE50sA2sjMZn5gJ7X5WV8L3VbKRUDSc40cOipkc6LEzctuGNioNNPVtGr1a_dGJjry7AJNgm-XNP8wHuWh0VqTIGobrVzK5t9wtSO2eAyZtQQhdAHUDOE7fD8I2d-GXg9n7qAakA5Snk9jM4J9dZlp_F2hvacDJyRLOGk8MxWS2MYwzt0bqlbTYVoJ0Te7Ng0KPcG7C9YDluV7mrzbJDZYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
〰️
⭕️
سنتکام مسئولیت حمله به نفتکش های ایرانی را گردن گرفت؛
پس از شلیک موشک‌های بالستیک سپاه به سمت دو ناو جنگی آمریکا، نیروهای آمریکایی ۳ نفتکش حامل نفت خام ایران را هدف قرار داده و از کار انداختند.
دو نفتکش نزدیک خارک و جاسک هدف قرار گرفتند و یک نفتکش دیگر در دریای عمان منهدم شد.
سنتکام اعلام کرد این نفتکش‌ها بخشی از شبکه تأمین مالی سپاه و نیروهای نیابتی آن بوده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/71147" target="_blank">📅 17:55 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71146">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c865776e9.mp4?token=QN7XGmi8AA-X18JZ0kW_2f_SGgm_Z4lw1nCsBVm196-3Smbwm1Q6voN_WKdASdKc6-jRNaxf17V6U4siMd29qTn_--Bou-KJzCjMhrJ9PfG-ZGwo3hv3IGkyEey8dSOhF_j7n-3dfeJZsrRUqXmIV54JMFp6E9naYiouEmSpqkQM4SB0R_XN5QGJS9Zs8LK2rKwxVG6z3jN3cC_aNd4DHbNTa_wlA2MXz6xFcBF1mO9qtSk9yeh7JX352U8vvhLjeg6EiERvwrYG971dZf5d740Dj_T0v7edms9_xCLihj1bS-Mn_cljw5kIG8ucBWRdS_1zWsyaNnd4o7wp6LfuOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c865776e9.mp4?token=QN7XGmi8AA-X18JZ0kW_2f_SGgm_Z4lw1nCsBVm196-3Smbwm1Q6voN_WKdASdKc6-jRNaxf17V6U4siMd29qTn_--Bou-KJzCjMhrJ9PfG-ZGwo3hv3IGkyEey8dSOhF_j7n-3dfeJZsrRUqXmIV54JMFp6E9naYiouEmSpqkQM4SB0R_XN5QGJS9Zs8LK2rKwxVG6z3jN3cC_aNd4DHbNTa_wlA2MXz6xFcBF1mO9qtSk9yeh7JX352U8vvhLjeg6EiERvwrYG971dZf5d740Dj_T0v7edms9_xCLihj1bS-Mn_cljw5kIG8ucBWRdS_1zWsyaNnd4o7wp6LfuOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
حسن روحانی:
به مردم بگیم قرار ما اینه که با قدرت‌های بزرگ تا بیست سال دیگه بجنگیم.
اگه مردم قبول کردن عالیه بریم ادامه بدیم.
ولی اگه مردم نپذیرفتن و راه دیگه‌ای نشون دادن حق نداریم نادیده‌شون بگیریم.
حتی پیغمبر هم با مردم خودش مشورت می‌کرد.
تو این کشور هیچکی از جانب خدا حاکم نیست‌؛ همه به لطف رای مردم اومدن.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/71146" target="_blank">📅 17:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71145">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/100451e13a.mp4?token=Mmb6FHUJMdr3eOaMLrQYxUrahKsF4UHL97CtBiEoCO_s94WnnODeEY60NEOVJGl2knMFkNvcnvJYGw_46X4YYwOcNTB9FaMIGOJh_Tsgc-FRYhBNP9FvCrgjkxHWnr_drDG7jRnx6rz9Nnj1EC6Ig63Dd3XFfUmPmq7let_rbs4zD2KlgD_PCpc47qzMX8Up8jRcsA_-sVlMTbSPBZmLZqvmETm2OyK1nzw7WHD3TDBL9mxQJyRcsVD9iZTx8M-zRztRh-IgACpi8KqnxaZ3ZpEox4C1zKpyMF-JUaKB9Wxrfs2Ya1IdjNUzwj-dyFbAEWMR6rYE86vzT4Gr4w81RYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/100451e13a.mp4?token=Mmb6FHUJMdr3eOaMLrQYxUrahKsF4UHL97CtBiEoCO_s94WnnODeEY60NEOVJGl2knMFkNvcnvJYGw_46X4YYwOcNTB9FaMIGOJh_Tsgc-FRYhBNP9FvCrgjkxHWnr_drDG7jRnx6rz9Nnj1EC6Ig63Dd3XFfUmPmq7let_rbs4zD2KlgD_PCpc47qzMX8Up8jRcsA_-sVlMTbSPBZmLZqvmETm2OyK1nzw7WHD3TDBL9mxQJyRcsVD9iZTx8M-zRztRh-IgACpi8KqnxaZ3ZpEox4C1zKpyMF-JUaKB9Wxrfs2Ya1IdjNUzwj-dyFbAEWMR6rYE86vzT4Gr4w81RYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
بابک زنجانی: سایپا را ۱ میلیارد دلار می‌فروختند، ۲ میلیارد پیشنهاد دادم، نفروختند
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/71145" target="_blank">📅 17:00 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71144">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b09e3df411.mp4?token=AQfJx2Prvx3dyaqRQQS6wqq05lUV9FqYLXBDFZhF_UvMgofVisqx7G33PAWBj6YNc6qUWb1GCKH9vh1X6c4i8kXrmVXkJV6BdgqUeKFqHuKu_Wp2KnabGOwJiz3PN-71KN8-EYn4H7oRrmTGy1DUVW4fjT2-0REGWSI5stK9c019k1kRGRwLK01Sov8AOy_5dmHVi4QcMUpikXxqKnUslUInjJNLcpWTs5cgG4OFJhjM88em1ikKru-4H0HodvSPDZ3QzPtWyFEsHMKioGg8CoEF-qs_-KxqB15K7Ez0cfEXd6P6ah2F8t1fl7-DdmyKgW3TYbWvjDI5ExCE7dcAeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b09e3df411.mp4?token=AQfJx2Prvx3dyaqRQQS6wqq05lUV9FqYLXBDFZhF_UvMgofVisqx7G33PAWBj6YNc6qUWb1GCKH9vh1X6c4i8kXrmVXkJV6BdgqUeKFqHuKu_Wp2KnabGOwJiz3PN-71KN8-EYn4H7oRrmTGy1DUVW4fjT2-0REGWSI5stK9c019k1kRGRwLK01Sov8AOy_5dmHVi4QcMUpikXxqKnUslUInjJNLcpWTs5cgG4OFJhjM88em1ikKru-4H0HodvSPDZ3QzPtWyFEsHMKioGg8CoEF-qs_-KxqB15K7Ez0cfEXd6P6ah2F8t1fl7-DdmyKgW3TYbWvjDI5ExCE7dcAeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه سری ایرانیا هم انگار توی یه ایران دیگن و رفتن توی جنگلای شمال پستونک پارتی گرفتن
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/71144" target="_blank">📅 16:31 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71143">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc463ce6f9.mp4?token=IBrQlwrQ2gOAXgPxBbRj-GhUa_SQ1YadZbpx6dDkQ3XnG93MtEyotc5TL5Fkuupa7pGTn3owSUud81cNeBOeOHtYWgGqMFrGBSgtA_E6ET8OoQRn9QIt6bCKUkLzQa-h45XHTTPC35_xap5snrMudR2uFE5D6Oyz20uf5wJ7edKA8Ex9_bbE0s7ItYE_gE4zZe-V0qNAYANj0KM1x_bfpUEU5xbSb2v4ox-EMeTmZNr1BHaG1BQaon4RvYpGep667eDSQbsma4S-XPz5otOOOIfy5xIkCZOJOZfzxGBb6RK2EWW28RZyvQl6lowzBHHbKTTkcuIhgqZ9UKuXL2prWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc463ce6f9.mp4?token=IBrQlwrQ2gOAXgPxBbRj-GhUa_SQ1YadZbpx6dDkQ3XnG93MtEyotc5TL5Fkuupa7pGTn3owSUud81cNeBOeOHtYWgGqMFrGBSgtA_E6ET8OoQRn9QIt6bCKUkLzQa-h45XHTTPC35_xap5snrMudR2uFE5D6Oyz20uf5wJ7edKA8Ex9_bbE0s7ItYE_gE4zZe-V0qNAYANj0KM1x_bfpUEU5xbSb2v4ox-EMeTmZNr1BHaG1BQaon4RvYpGep667eDSQbsma4S-XPz5otOOOIfy5xIkCZOJOZfzxGBb6RK2EWW28RZyvQl6lowzBHHbKTTkcuIhgqZ9UKuXL2prWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇳
تو چین یه نفر بعد ورود به مغازه‌ش که به علت نشتی پر از گاز بوده، کلید برق رو میزنه و کل مغازه میترکه ولی خوشبختانه زنده میمونه و بعد از اینکه به بیرون پرت میشه کون لختی فرار میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/71143" target="_blank">📅 16:03 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71142">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9c6b59588.mp4?token=Y47hVAkcfmR9WJCd0s0T7yUgRekoEvMqjlWyLsfLddRnVVygN5niXwPRpkxlfSljDJ_rtf9-ytklkDfjuVeaHXggPqr8uiz7TiPY768E_XPxNT5VT9yeDo8rJdAPRdaZnhxWb1JpSILfl4VTL-fxOSzyFvyxRrOouPeDLcS_Iv5yIeIO1J6s0WbgNSZILvmKGBG4ZAwU-Tr-lBtn6MmoteE9zj7uGNpSG3IVtSIZHO0Jm-HOyIfvmbAgRpgKmuHpzVySqusisrhbL46PAFuFGhk0NtU9sxjPYfoWlyJcz4n7ocPiNiohevDQzLxQTvzPteom7AEnMhO7w7dlxJJ19YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9c6b59588.mp4?token=Y47hVAkcfmR9WJCd0s0T7yUgRekoEvMqjlWyLsfLddRnVVygN5niXwPRpkxlfSljDJ_rtf9-ytklkDfjuVeaHXggPqr8uiz7TiPY768E_XPxNT5VT9yeDo8rJdAPRdaZnhxWb1JpSILfl4VTL-fxOSzyFvyxRrOouPeDLcS_Iv5yIeIO1J6s0WbgNSZILvmKGBG4ZAwU-Tr-lBtn6MmoteE9zj7uGNpSG3IVtSIZHO0Jm-HOyIfvmbAgRpgKmuHpzVySqusisrhbL46PAFuFGhk0NtU9sxjPYfoWlyJcz4n7ocPiNiohevDQzLxQTvzPteom7AEnMhO7w7dlxJJ19YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
🇺🇦
🇷🇺
یک مزدور برزیلی که در درگیری‌های روسیه و اوکراین می‌جنگید، لحظه حیرت‌انگیز عبور یک تانک از روی خود را — در حالی که میان علف‌ها پنهان شده بود — ضبط و در حساب اینستاگرامش منتشر کرد
😟
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71142" target="_blank">📅 15:32 · 14 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
