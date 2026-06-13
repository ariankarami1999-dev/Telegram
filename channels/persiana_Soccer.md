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
<img src="https://cdn4.telesco.pe/file/sF2V53ozbzXl-taL4NuNsMvbPCuqRq4e8CHmZc1gn630fchu5wAyP6kpHjmyTL03rQdEIw7gXzuohdG8fPsDjLP9ytys8hBzI5eodnmLXChIlwongGojXctFNGAHRNWiXMH2qLXlU2sGudtY6xOKRHAC9TF1-08WYwd_hJXwTVIzV3-TqM4rhs162bL3u5NKg46c52s2rj_H9d-fXQ6Qhn-MqoYz9PP80pzVyxVIQP91NnXhE3m9tTIGEk8oCSTtCWYRNbrd-toI_nzhGrzWvh5Oggorovcbr1CMuUAU6UBR_ibrHRE3TMDvAMuvbZlm48YAAsZ6eVxds-WrfMPJ0g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 247K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-23 03:43:59</div>
<hr>

<div class="tg-post" id="msg-23323">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jannjw0ZsIoHL3O4M9Oujoka8bgKhGgJI_MdRP87zOW7_FLbnu3TtEaKKOozPmJXvM5aNfRri0nyOMM5I2zlb3g_4i1LZekulUyFX-gThXwUEYbUPNUDcqR-xcminqcrZqTQ9duzM8JUMZdwwhZMC2rwIJvtlRx_5xs74BhDljG-NKg0ioVPrdhPLjnlJ04WJ7jvqaOMDkru8mVYu5873x-NXNLRrpQfZ27ukZnX7HgcOleRhEZcU5Lm5sBYLfkG0HUAcQvGQQh_HTtbUlex9kzGKVg2FXv8E-a2ZLcTf-pt-M6SKf13fIrDWVSR3BL-fmbIlulLeyzrXTO5bux3Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nH6stHv_o0F_oSMyYd4rKDDBKEUZLYOQjnSwWBrVAXYgYMOYD0YRhJeBDA1QLuWpibtN25d9StZ_029zlJD-q4-DyM6TzQj86P6PtTdvR4A_apnfRS9H4vUdpwpt8JD52WGMOizhdbv2kAZA82XgCBcjFb5LASWBBig_tActPbds-Jrc6IN61roKIj-NDGBkPqOVEO8Dza_D2OGKyG-RyVs84yv-ijbhJi3CsLuGLoxuYUjFKNUCafCU-LKCGEA4tggfgmlIVTmPhxmNG2hMxF4B4TP7LHYa8D0DgLQWh9uii9zPHm29x0pPdU25zfm9WPG_bycuJ4U4-67nLYNtPw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
امنتیت بالای شهر تیخوانا؛
در ساعات قبل رو به روی محل کمپ‌تمرینی شاگردان امیر قلعه نویی یه جسد توی صندوق عقب یه ماشین پیدا شده که در حال تجزیه بوده. این ماشین هم توی پارکینگ محل اقامت شاگردان قلعه نویی بوده که دقیقا رو به روی کمپ تیم هست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/persiana_Soccer/23323" target="_blank">📅 03:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23322">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n0LGHdFbG1iAWhew1nGr2ah7Tg0GpN_NLyd8EmdYO8m1xmg2jqfFVTdk3Y0Cj1nmbqzoa6s6jdFfBaxJi7TDnfujkcrhJtiG75a-foZchIg33bsUyU5yIo2rEXNlpLTFCURbdGjxdAJMot9hUGPY6kMts4X5l5ee2efnrO8LN6auO8ND57gX9GSX--lxW69kcqSKEbVu0tBiC_asZUU9orEh-b-76laIhNd80bN4cAgByguinWGJ_ZAX9XvX-dDGEYVa6msCrJTKgR7KT_99hFGFn2D5wrF9DLR33vOStYL6qoDmBBLJ8F6p-VX202OfsLVcRffr2w7PkG6uIhVbnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
👤
بااعلام‌کادرپزشکی‌برزیل؛ مصدومیت نیمار جونیور رو به بهبود است و این بازیکن از هفته اول جام جهانی دراختیار کادرفنی سلسائو خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/persiana_Soccer/23322" target="_blank">📅 01:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23321">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jf_zA0UakYS1XNQROrnRk-MSjyTYAieK86s6FV-VqNndXh30BIoXYowzM5aQPLrG6hm4tI-Z7v-U6vEBrFM7uajFJg3vlU-tpxrFbNB4ltZ7R6rvBhZ7gjxtc_fvqacmtkO3SsZaPbhFOq9G9BHGHGyX3jrBaEi5WO-Epu8yqhicUzMTba4DEJ8aCcrgGm0nizT7hfqvbaHat4prC9ifToDqKtZQtckW1KbBXhPKF7F1EASUUEZeeMGWoncdUoGXFuEZ8vneUVkGvFXj48Kd-_bmArfWozmeyRkiJI18P76Tjl00AUBIRTogHexy6Oi9iTMrynI1B_Gf8EjPf6hr4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#نقل‌وانتقالات|نشریه‌موندو:دکو مدیر ورزشی بارسا بزودی با ایجنت بارکولا ستاره فرانسوی PSG جلساتی برگزار میکنه و پیشنهاد 50 میلیون یورویی به PSG برای‌جذبش ارائه کنه که ممکنه قبول کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/persiana_Soccer/23321" target="_blank">📅 01:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23320">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">▶️
قسمت‌‌ دوم‌ برنامه‌فان‌جدید ابوطالب حسینی برای رقابت های جام جهانی 2026؛ عالیه حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/persiana_Soccer/23320" target="_blank">📅 01:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23318">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KzthCDx6slHgdv6Wh6hkCZqJCKvyD-Ixfwrb1S4C3ANODnr2G5j_50VhiCxek_MUSfZJaQSOiSNKF_FQmyB8esRTlluAOgp2TIEjh_rrIwGPqd4IW9q0-b6dN0cJ6PBXpRakpXVopWcXLESnUr3cqHSGKNWdL1sgYo50CqjlchH2Ti2Fu0c9-5sm9fcCRkeuyn-xxb7h8F3-8iWgWxtpz53yOtXSaReAVdfzVHPyLpZBdVVKjWOkVCRLTzwCiBSIz0j_ENl8LJXAV191UbBNkLVoc_AcDuTfh0IptkCg93gAKr6uyIZTRp-jIWJBHNveAheHJyqiX_E6QpWniM4UZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
ازمراسم‌سوم افتتاحیه در کشور آمریکا تا‌اولین‌تقابل‌جذاب تورنمنت بادوئل فوق العاده حساس برزیل و مراکش در بامداد فردا
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/persiana_Soccer/23318" target="_blank">📅 01:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23317">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FWmGbjFCv08HXly7ON7RCpRnWbockkMxkvKoV7zwGtdYUb-g6LixBbqJi4dZ9LznoqjQnqqsvoIOk2-U5uKMhW0btIqvKnD48ExJbv8jmZw3dgBz68zszlko8dLpz6tChtWS41QR1nJcIG3zHMYyZDTK9DIUzVLo09mjJHPe6YmdCDT-aeDTp-4Y22llxpgBs9FHQ0yTgf6sRZSHH4NqsCitbaP9J0m2vOyPpaqPEqxPQOuHw5O4UO6WjamIha0RrKVjSZ3sth6cUZy_95RWWmB5mKUkudFcrtKAIN3LQAq-TPOvHzCI7etjYiuoQDJ9IURqyNNEkOv2sa7eMqrovw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌‌دیروز؛
برتری بزرگ کره‌ای‌ها مقابل چک و توقف کانادایِ میزبان در مصاف برابر بوسنی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/persiana_Soccer/23317" target="_blank">📅 01:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23315">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K621DDLouvopBxfi61jgtqZxd6w6VmddHHMySdVtLW539ZR1xxW8n_TyUd-Y7AjOFOh4aJ83vC84QGJXlVcMmatmJRTk2VHUXUbYcfeWXotuc-w2_A1Hq1nZuZHP9V1NEC-FjdcToPLJsN7ujf_uzYrq8nU86Y1nimXink8rxeoH9mfLAmAfl67Ej3y1WXY4ahf32l4DoRvUvre4T7yidItM0wFjLjWav-d2YjuicosKOyguox-GQCw3uCa8lmQsnBFH8V7tszd_9rlmO_Y8OUmOyoWFzp4imjrNNIQIKZxxIqBrQJo5rXafwNZunfAWdO5-sixjNFrRjbsrtACAJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TwTyjC2R9Yl3HPxzD0e5MS2pAvU6zJKeGp0F6iQphnDLQeYAAcZdWzBHZEmjJ_OHBeyMI8HpXGGSeeywV1-kkcUZM7dd6VRx_YnP-Zqu7TGyh_-WjiHo7KfOqYwtnT2yg8jsJ7flZ5m0XAcCFeFfzbGXTZZphbfqIoj_VoFlXK7sX-8HCS08-v_W6H9e38JLCubElwKE_FK1B8qDYh-7Plvl3Z2O9lNMZ-dzogDt_l7EjQIZnoe5VaLWtXCo3wmP-VQseTFIkU20R7mYucw_V2zttPZMgrIyKRYFNQbV_ftdw9ERkUpHd2WQckn2H64_ELvOUahXOMoZeEpr0MCDkQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📹
شات‌های‌جدید نادیا خمز دختر پاکو سرمربی سابق تراکتور؛ ایشونم بعداز اینکه اینترنت مردم ایران کامل وصل شد پست هاش رو شروع کرد به انتشار. حدود 70 درصد فالوهاش ایرانین که اون سه ماه نت نبود اونم پست نداشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/persiana_Soccer/23315" target="_blank">📅 01:12 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23314">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L1VkY708ayw_NLWrsn_yCeJoVO2LzZDbHLoUFzzYuNIEcaVlbOvPZ2Sl9Ra7H9JmQ6g9Dvn89XI3cwSWHQq2OMQ9fROpKlX1WL_sWNZj_o1K1uCKxBDJ8cx2hxDJOlT9siRLWquvHaIDCJXgoZQSz3Cp50f6hmTvwE_jIiwRNGKQVP9Yb5L9dJyXI_k-4wqiPP9IpJkTc4vpeICQnD1ceU4haABJ8lJNqQ1aaFt9gcF7TnpVrJ4vV0orfVEuOHEdb0Uog2oAHnUxP-d6aUIC6QdS159mU4zdx7VwM0v7W2SdHJxVXsVJnOw8jgDRu3TXI-9ba4nBiuc_SjHvM5AgMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ رونمایی از استایل جذاب و گرانقیمت قلعه نویی دربازی اول ایران مقابل نیوزیلند در WC  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/persiana_Soccer/23314" target="_blank">📅 01:12 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23313">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IGO-m4Z-bBzSgbbIOL2wUynaBFFYDQsdrqlWqkQDrHePL6hoHh5NATqbuYy1J6yS06NaVou0SZlhLvNyxIyqbYIim0QJ0v7BdgaV0kWNHFnt6J78NB_UCVZBw-iqsDGdOCNtdn5OGRrLt-m5rK1QvUrCrHe7GGGwPyvQQ8OBPItLJ34ujFrFD8ZezGw1URKfu7yJ2GEqqDkOR1hJSEb5h39Z7dY2Lb-zU9jVn28uyPB8JtzyuuEG90LnzZBw5eb-uYf6JeMBVXsoLlqGis1rr095tH4rOuTsASAMtpxgbgcC_G0sY694ZwjqtTdXBRCXv_lKoyYnATGbFw27dajcBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
هدیه‌ی ویژه برای کابران جدید
🎁
اولین واریزتو انجام بده و
0️⃣
0️⃣
2️⃣
🔣
بونوس اضافه بگیر
💰
⚡️
فرصت تکرارنشدنی به مناسبت افتتاحیه
⚡️
🔴
تا سقف ۳ میلیون تومان
🔴
⌛
فقط برای مدت محدود
💣
بالاترین بونوس‌ها فقط در سایت وینرو
📺
تلویزیون لایو برای پوشش بازی ها
🛍
پیش‌بینی مسابقات با ضرایب رقابتی
🎇
بونوس‌های متنوع و جوایز ویژه
🔝
تجربه‌ای سریع، متفاوت و حرفه‌ای
🎰
همین الان وارد شو و با اولین شارژ تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگیر
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
📱
کانال اخبار و هدایــا ea22
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/persiana_Soccer/23313" target="_blank">📅 01:12 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23312">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nPxmdVB2bYlpiMwcG9hbOKhfGzbRAfxQGRuoDRL4xp21NzJ8OLFpQgcXOJgLDuqUbuSoYYa-knt0DwL3Jyaq71hUpz0jLhtlHGI0iBYQzYTafqc7Zn0D9wVtAeaj8iy2EQgWYfaVwBYU9r3tcJ9Vwe26XqZ3z7FVDvk7dPJ44rKhO9WmUikqb4EdFaIEsrBWZOcKACtdo5vx-foSybEl7R5pM4x_T378_eldUxB9UY_2d6FcTOU2I0Uj-Ve9JD-qUExasN-pUL_3Zk8wOFfbZc7C8lERW_cLG88jPWsmkZ1McCrpYs5d5_jSlWDI_4h0HEW91sMpp49yyZxeptC-9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
میثاقی‌به‌منتقدای‌تیم‌ملی‌روی‌آنتن زنده:آدم مفت بر از جا خالیی ......تره! همون شعر شایعه رو میگه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/persiana_Soccer/23312" target="_blank">📅 00:51 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23311">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8e109d357.mp4?token=tVlX0RfYw5kbZjEEt8E989JwrUrT_bm4_zVCDmmpoNcxmF8u2PbVYbbasdgMRAzo2N_b-0I2x-2PoQRaQ_EiZ2lyWVxnLKOVGTgtSdw-sz5n-0yoJNT1Yxl0tU0LyjNrMalUxdC3-DeTe1Zx61gZ5HnYF76Rdo0WvQP3sr6RQOI_8WEnnEYA0B2a8vr62s_uVpST_9IYDdEOn4vJZV7q50wqcdSFw3gIJaCH43p11eSwvdnB2r0CBzoR6L0sK_sSDOiSi_9NywCUNy7uR9lEPOix5-hLl6YHaXbWhbNV9wBeoLZka5LZQvlrV-cMeL_x5RRu-S78a9aSCg9Zfth8q0eNtUkzOQ_25sUzgffN0fGA2T-Slp5sOg-xnKcAfORlOF7i8Z1syyGkzxv6trTJ1E4IXOkYcwFcK5_aUMVTOQ32EDHtD-U9k7tWplucsUQijrWBPh-ydUX-aWWL7shnLvKVr7iVa0ZVVJBtah2PSL3vvQNGH8MEPXC-p65GB9OWYurgLNqqdcmz_0R2pnjAqYhZ4vP0CHYEkYPsTr4dgnULYWPnaZ2iyikqrvzNhYUFbzXEZKDJFNLVJ9GnGDX2FcDSS7Wu_kKBhzzGFzWPyMXz4hdY75XeudZOYEvdITDGdEhVgqf40k2M-8IOLMG0jV-c7Un8aEom5y8I9zPAb2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8e109d357.mp4?token=tVlX0RfYw5kbZjEEt8E989JwrUrT_bm4_zVCDmmpoNcxmF8u2PbVYbbasdgMRAzo2N_b-0I2x-2PoQRaQ_EiZ2lyWVxnLKOVGTgtSdw-sz5n-0yoJNT1Yxl0tU0LyjNrMalUxdC3-DeTe1Zx61gZ5HnYF76Rdo0WvQP3sr6RQOI_8WEnnEYA0B2a8vr62s_uVpST_9IYDdEOn4vJZV7q50wqcdSFw3gIJaCH43p11eSwvdnB2r0CBzoR6L0sK_sSDOiSi_9NywCUNy7uR9lEPOix5-hLl6YHaXbWhbNV9wBeoLZka5LZQvlrV-cMeL_x5RRu-S78a9aSCg9Zfth8q0eNtUkzOQ_25sUzgffN0fGA2T-Slp5sOg-xnKcAfORlOF7i8Z1syyGkzxv6trTJ1E4IXOkYcwFcK5_aUMVTOQ32EDHtD-U9k7tWplucsUQijrWBPh-ydUX-aWWL7shnLvKVr7iVa0ZVVJBtah2PSL3vvQNGH8MEPXC-p65GB9OWYurgLNqqdcmz_0R2pnjAqYhZ4vP0CHYEkYPsTr4dgnULYWPnaZ2iyikqrvzNhYUFbzXEZKDJFNLVJ9GnGDX2FcDSS7Wu_kKBhzzGFzWPyMXz4hdY75XeudZOYEvdITDGdEhVgqf40k2M-8IOLMG0jV-c7Un8aEom5y8I9zPAb2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
هفته اول جام جهانی 2026|توقف یاران ادین ژکو مقابل یکی از سه میزبان جام در ایستگاه اول.
🇨🇦
کانادا
1️⃣
-
1️⃣
بوسنی و هرزگوین
🇧🇦
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/persiana_Soccer/23311" target="_blank">📅 00:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23310">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aU1ab9p7dev3o5hUfXyKO2zjj7R2CxW_fYR_A1mexqQ_bx_i-LyeHj-GAHd22Huc1xfjaqqQ4S-o0hkqQqsv79AyjuB5KTSTVfZBDaCmEGuwYuT7HmfxKb9-p2WrmLDZQS8jC4ZO-hC6K8tuVk-TCsKDw6K2HMF-Pb8dHQwr-F_vcqd9qGhyDEwVr1fB8-wvHy_2uiZ4TCKASLgybIgkkU8AqjG5qxB1qbt0DBBZFKrCIwRtJ_MUelY7dWkLCYyGvSKf723l1yIdLVYhpziyHBwhTtWXaBho19o557t7QPzfsxiLz_oDQZjR9VzpZrFJxZ1BmqW5Gyhi7uvV6e2Jkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول جام‌جهانی گروه B؛ شماتیک ترکیب دو تیم ملی کانادا بوسنی
🆚
هرزگوین؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/persiana_Soccer/23310" target="_blank">📅 00:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23309">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v4ZUdA9G9S95p6pmUTuCFYPZi9mJZmw0s0L-LS6rBYrhQYveC64Ez0fhw5c2LH_uZfVCeAlDkQH1bEMVfpZjzRe2co474uKlDM7CVj7hVXs7XtfAHIFFOxx4Q9JLlqymHOMm3nj-db1dsQD31XxwyEY5whxVDrn59m0nmw3csh0oC8mFbuDK4sg-wnAuE-rJORDQ8rBUUNGKVyBQ7wnuO5Xv9df-ra_J58kh_zzXwb1WwsQoYHXSzoV-7t1lYzvtX7y8Y3UW1PWqsuzIigAgktgLXWHvtYmg9dJzKjtT78vikXRUTDkVYB9BJ5upmcBctFv1Mizj8CZvcGmvZoi6tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/persiana_Soccer/23309" target="_blank">📅 00:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23308">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D5kPEWe5Cs4SjDdxENl4TEpYoHxFv15_VPK8DSIxTDMqucvuKUitznbWwfzm88F9B7aeGmOaWWTihyBt8dOLrOx_l1nRga_IMIjt2pZimesOvnQ-17EiiScVrkzZPwt4EwDdoT6JxXewaOYn2iYF1BFwPoUMWiYYGZA-egjQsj65FLel6wEUwF5TQHM1xF4YOs5uC9t1eDQT3NhQ6O1Vdf8OfvdvTaT4lLxs-QqSqY-fDTGNMVSNQx5ssP4Biq8DsraPg2orPcRXwNLpucMz1cFV6Cj0IDXVos_jBzscOzxR8no8KqUNctqxNu6h3JbHjLdnn-r9QgGxT2OGqqVRZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق اخبار دریافتی رسانه پرشیانا؛ اوسمار ویرا امروز صبح‌درتماس‌بامدیران باشگاه پرسپولیس اعلام کرده که به قراردادش با سرخپوشان پایبنده و به‌زودی برای پیگیری تمرینات تیم وارد تهران خواهد شد اما توقع داره که در نقل‌ و انتقالات تمام بازیکنان مدنطرش توسط مدیریت…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/persiana_Soccer/23308" target="_blank">📅 00:22 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23307">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tTBNkGYUgi3nqCMLTlnhHz8hfC4bo588kcemZe2PLHYe4guWEPh1k_rZny1tsasufFd93GbS7y6ZWjXfOWYM_9QlNl1A0D4x3aIj4LpDMtUpZh-ZQT9u8hIKx9BvhonAzb0lW8CjPdgVPnCNlOWxb_IXa5Ei344xtwtZ_6TRlvfkCfv1c-TVxIgfxHFVPbKtPYNydOtSwVhtnCSOJgJrE57pRTK3d1vtw9Ce4gnA8vqmwMMxAxScC6yB89gv6C4PFeeu_fhBMOgNCOlrfOLkb-SHyecKuILa5uAnRRQsNb-Du_A3DE1BJcIlrgAfbar8XBgTs1Am9J8uuNBU5Fbh-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇮🇹
#تکمیلی؛ رومانو: نیکو پاز به مدیریت باشگاه رئال‌مادرید خواسته که اجازه‌بدهند یک فصل دیگر در کومو بازی کنه و تابستان 2027 با قراردادی پنج ساله به باشگاه رئال مادرید برگرده. نیکو پاز 21 سالشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/persiana_Soccer/23307" target="_blank">📅 23:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23306">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IoqkCNRlTmke0NEEwLaUUxDxxTgQjBoAndRMOHLbtw9gSyPHJ85Kr1OQtS7Hd3N1NEaFKW8_-bUmFarT97yC5OofapapTHrqBsrpQgjn14dOMfGH1d2MMiNz6AJGos6tl3dWEfsHAQ3BzAKh0D--cc7mjxLOkByy8NT_zPIxiZy0x2Hu7kb-0z3BuGhYhIhyfRfprHNa68z4SaeDiHaCpVBq5kqV_L6c8o1ZQt1GltdVREHp8N_OSYU1RTwOGUJKX_JYjTuRo_5Dqk21HLscEQYy16prFnSowNWizFDKh3DpVy3O6rPrvPw5ouJB20qC6tf4x2Jxt6aFgzId17IW0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
🇵🇱
#نقل‌انتقالات|باشگاه‌فنرباغچه مذاکرات‌خود را با رابرت لواندوفسکی ستاره سابق‌دورتموند، بایرن مونیخ و بارسا آغاز کرده تا او رو به خدمت بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/persiana_Soccer/23306" target="_blank">📅 23:44 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23305">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f8afd5643.mp4?token=MutqQItISm1EC9o_G5q7uNBJivh7FySd5q7nK8bfTiY-rAGZgGZqTCEJwQmIc2lgA-naqbYWUL_whFAN0hyH9wiYRVpQ8qOLkIII2CyAV8-7WJGAH-VtciZocjzlpPsvsYYJ9fAQKnqszK_7t0rm3rc_koQvn8XbOljOcpvqGCpHs8IZQ_hh8WNZsDRjilzH58qWiKvEuVhpMPPWt7aMuAUVuS87Nz1hMJVrDL5p75lJ7gP6G0Q0C7NkvRtgVHpLpp4u2p4X2e2JGefobdgezGUHg3nJ71bVC6hHYPCzr4CO4A34aUPkbToQNDggT36Eey1UdSL8U1kE3pP95xEFPSvjjA4Na5OxYTjx3cz_6XO6ywn1k9G3WTeDVQ8Y7vEKamTeGCBsBtp758rbeyWf_29DRkdiPgPU6d6xutYVf5Pn0WsFsyJgG47cpi1YH0rdnuBTnMiq3tIPl3goT4oGgWvHXf5RZ2bazbVNujpGGzQGdRpp2bjn0hcLhyZF9TUsQjMhZpFL7iou0x7_aAnRhlFNURZYMjjy79LdK8SYAQeMZAJPaKpkdc3S4Gcf2ACCXApuAZJRbFStuRaOQnjopz_Rgqm8Ng1pnl0UwV0-7fIWO30mDLj2vhJeLSGqBTrKvDFPE39G1CmbjVJggjmqIFcI69-1ZONKQbBGdcbtzX8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f8afd5643.mp4?token=MutqQItISm1EC9o_G5q7uNBJivh7FySd5q7nK8bfTiY-rAGZgGZqTCEJwQmIc2lgA-naqbYWUL_whFAN0hyH9wiYRVpQ8qOLkIII2CyAV8-7WJGAH-VtciZocjzlpPsvsYYJ9fAQKnqszK_7t0rm3rc_koQvn8XbOljOcpvqGCpHs8IZQ_hh8WNZsDRjilzH58qWiKvEuVhpMPPWt7aMuAUVuS87Nz1hMJVrDL5p75lJ7gP6G0Q0C7NkvRtgVHpLpp4u2p4X2e2JGefobdgezGUHg3nJ71bVC6hHYPCzr4CO4A34aUPkbToQNDggT36Eey1UdSL8U1kE3pP95xEFPSvjjA4Na5OxYTjx3cz_6XO6ywn1k9G3WTeDVQ8Y7vEKamTeGCBsBtp758rbeyWf_29DRkdiPgPU6d6xutYVf5Pn0WsFsyJgG47cpi1YH0rdnuBTnMiq3tIPl3goT4oGgWvHXf5RZ2bazbVNujpGGzQGdRpp2bjn0hcLhyZF9TUsQjMhZpFL7iou0x7_aAnRhlFNURZYMjjy79LdK8SYAQeMZAJPaKpkdc3S4Gcf2ACCXApuAZJRbFStuRaOQnjopz_Rgqm8Ng1pnl0UwV0-7fIWO30mDLj2vhJeLSGqBTrKvDFPE39G1CmbjVJggjmqIFcI69-1ZONKQbBGdcbtzX8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
طبق‌شنیده‌های‌رسانه پرشیانا؛ مدیران دو باشگاه مس رفسنجان و نساجی مازندران در روز های گذشته مذاکراتی‌باسهراب بختیاری زاده سرمربی فعلی آبی‌ها داشته‌اند و درصورتی که بختیاری‌زاده با تیم استقلال قطع همکاری کند با یکی‌از این دو تیم قرار داد رسمی خود را امضا خواهد…</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/persiana_Soccer/23305" target="_blank">📅 23:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23304">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">✅
طبق‌شنیده‌های‌رسانه پرشیانا؛ مدیران دو باشگاه مس رفسنجان و نساجی مازندران در روز های گذشته مذاکراتی‌باسهراب بختیاری زاده سرمربی فعلی آبی‌ها داشته‌اند و درصورتی که بختیاری‌زاده با تیم استقلال قطع همکاری کند با یکی‌از این دو تیم قرار داد رسمی خود را امضا خواهد…</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/persiana_Soccer/23304" target="_blank">📅 22:53 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23303">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zrl-uNMaiSvWeI3Kw1yYR3SMVcTg_fIyOYBhh8aEf0zNiDf7nUgaWflNQ-WFmYfj9Fmw_gn_JI7TOWbrQr8W0qsK5YFfSQ0Byx4sMV4pE8PvYKH9RQfi1mBVW_x97V_o5YjB-hV9kibYFgjisWdB8MgSn75gr-aEKvA5d9Q4s_Cics3XNzGPgx1GplTFce76Yxh3_nC886Tcq5S4byrhf6svGIj40LcqEP8R8Am5vrCHdo2bxcH3vexFzY_xKMNaJqXoAZtyZ0Z0Wr1aXGTBhXi-ytcqrIR_EZ3e68uFAQde5U0QkKAYPekN0jCXJm69yRuhszQAZNfkqZNz21vsfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛‌طبق‌پیگیری‌های‌پرشیانا از مسئولان باشگاه گل گهر؛ روز شنبه هفته گذشته 9 خرداد ماه؛ پیمان حدادی جلسه ای 3 ساعته با مهدی تاتار برگزار کرده و به اوقول‌داده‌که درصورتیکه باشگاه با اوسمار ویرا ادامه ندهد اصلی‌ترین گزینه هدایت سرخپوشان شخص او خواهد بود.…</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/persiana_Soccer/23303" target="_blank">📅 22:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23302">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cVgxPAv5tVJkOhlZE468VOR4SF-SPMgT7vt_dR4OBouYqgKGgvsdLBX_Uotmp1EY9lvyQKnKQeggGdboDIzOUe4br8rZX6wuUPN3jZ-URMSSVjQwaOn8vBEDILLm3t8mm2qbc2Ce964atVYIKjE4Ca36zZ5yblot8IJdjRr3Vkw68jK5l-vM1JB3wxnYTku8E-nTKNu11Al_hpiYLiRQdbSf7kmv83pXPYuFNQwDg4qkMaQ43p4Td-uvteMOzFbCiPqE5n7aCzkc1fyVM5aMiyu4WBcumsQ9XfaBsio7rVaNto38nxTY9PatrX3ORfjkHlVQG-mBoB-Fj8tbiYbVmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
معاون‌‌اول‌ مسعود پزشکیان شب گذشته با سردار آزمون تماس گرفته و از اوخواسته‌ضمن عذرخواهی بابت استوری که دردوران‌جنگ‌از سران‌دولت امارات گذاشته بود به‌جمع‌شاگردان امیر قلعه‌نویی بازگردد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/persiana_Soccer/23302" target="_blank">📅 22:26 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23301">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pNqgMmXRqFL7pSIkWVgVsjtJR5pOCqjvEULw0R5NHO3A3de5n3frovK5_LWii17I4AFuU8sipxvqKvpM2hQoHA6ko-QjElr_Dm4VecUvtW4gzDV-ZPbsn6grw6ZmkQvduIZwSDw00J02alvByEswfzavBQ5gXXgGjLBnZH28sTZCbScHipxcT6EedrEe5SBfFc6fYW8E8UwKhUm_o0-T_7h6RWVkYF0dkov-21ukKMZ62BDliBoh_at-ghTS6ZpNTzGSr34DiAA-djPT8WFznUpjuPyaA22M9pcgZek_fxEJGMonpGSZHzhGR37F_QTzeaNQOBQ0XNKQzFmc-o_9IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#نقل‌وانتقالات
|نشریه‌موندو:
دکو مدیر ورزشی بارسا بزودی با ایجنت بارکولا ستاره فرانسوی PSG جلساتی برگزار میکنه و پیشنهاد 50 میلیون یورویی به PSG برای‌جذبش ارائه کنه که ممکنه قبول کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/persiana_Soccer/23301" target="_blank">📅 22:20 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23300">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PmDY6d-v3lkO1D8uQAywztmSAMtRZpmQvmy8Mbvf21b_TmnJwmE3uqxKXeWPE0FP87k4SZfb7V8cOaGKxR620guTuckpFsrr-yp-QQiffYsvNrb9bOErk2z4lElAVN_XIlSTi387uqubGAFzCwKO4_kGcPgYT8sBSVWwvdv6mCVZgaQ0_CaoPbxLQq9S9eGAeMb_dZnLTgh4kvuXYQLaZThPpZ9aUtElofl31i5IypDWzeAwo-fdfrp4HVF9JLoim9kXKtLhAy9e3r6ABRxcWU9iOKgUsnGWO2Zgk4f8_54kTFm8rRyfWY6JjbzGAeLr6ExkAwmnlxtGTfL2O2qYwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا؛ مدیربرنامه کسری طاهری هم‌بامدیریت‌باشگاه پرسپولیس هم با باشگاه استقلال مذاکراتی داشته. رقم پیشنهادی باشگاه استقلال برای دستمزدخودِبازیکن‌بیشتر از رقم‌پیشنهادی پرسپولیس است و الان‌همه چی به‌خودِ بازیکن مربوط میشود که کدوم یکی از این دو باشگاه…</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/persiana_Soccer/23300" target="_blank">📅 22:05 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23299">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ed2c6f597.mp4?token=cxkWqnn43I6bZTwH4jmLhKyZfPIcG11IzYfpDeQz4Lu7YGXmvjVXCEIZbq0uUqVhj2FDstkODCUXFf-i_tPgIf3ghxx55C_t8ecsrYKyzXfIy2pC-hx1_ny-ZHdTo0-zTu5s4_pDDKHN15276QNzpYAgVZEkBg-FXvkAXteM8vfvjE8YcATG4uzrWN9h38s9nQT1zQ9fUfUOKpzIptzz6SXsPeL01iRaD_sA0-C6Y6C0hUiXto41G7nnr_CGncUExt4V7I8xlPhJA0HNmUG7PFCgeQafwMMGK4EJiOit0PPbT6GKqMOeWWVpaFu8KjglT2B4Lkvp9bAWwgezxwU7_oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ed2c6f597.mp4?token=cxkWqnn43I6bZTwH4jmLhKyZfPIcG11IzYfpDeQz4Lu7YGXmvjVXCEIZbq0uUqVhj2FDstkODCUXFf-i_tPgIf3ghxx55C_t8ecsrYKyzXfIy2pC-hx1_ny-ZHdTo0-zTu5s4_pDDKHN15276QNzpYAgVZEkBg-FXvkAXteM8vfvjE8YcATG4uzrWN9h38s9nQT1zQ9fUfUOKpzIptzz6SXsPeL01iRaD_sA0-C6Y6C0hUiXto41G7nnr_CGncUExt4V7I8xlPhJA0HNmUG7PFCgeQafwMMGK4EJiOit0PPbT6GKqMOeWWVpaFu8KjglT2B4Lkvp9bAWwgezxwU7_oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
دیدار کریستیانو رونالدو بایک اینفلوئنسر که بشدت طرفدارشه؛ دختره زده زیر گریه رونالدو بهش میگه اشکات رو پاک کن عزیزم. تو خیلی خوشگلی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/23299" target="_blank">📅 21:46 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23298">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EjA1qL0Ntk_uVzwY5W5vnE4tgNGfncDUxzG4HJNuab_cZxx_rouj0oYJRDC4DYjT5pqkeFWgkv9_H0d7azNtJ_9PJLtz7LGexHJ9Gypai0U8JcOzjVJyv8BoarrEWPrCZiZvX6cCL4ALTKzPiN1wsPzg-e664wcxSRDcKWvbYyJvbE0JJM0obX4Jc9aWKmX4UbqZrOEQShq4nUSeFHwifpA9owbxUUNYwDNmcnBPElTBAGffpORPUKIwVuaiDYjriDzhvYl3VnTsffSTqvf8_FYSsGN65eKhlpOOWZH4qs-rO5Ck2ttIMOTVW3aHzj99as98LlFdbzrPbxQHGrhg-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛‌طبق‌پیگیری‌های‌پرشیانا از مسئولان باشگاه گل گهر؛ روز شنبه هفته گذشته 9 خرداد ماه؛ پیمان حدادی جلسه ای 3 ساعته با مهدی تاتار برگزار کرده و به اوقول‌داده‌که درصورتیکه باشگاه با اوسمار ویرا ادامه ندهد اصلی‌ترین گزینه هدایت سرخپوشان شخص او خواهد بود.…</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/23298" target="_blank">📅 21:38 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23296">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kz2aNl6B7zkEuGBQ2DcLVQy09Nt7AC-oDhgXoA-ASvnhAR2GBGt6xULDjNGmoPigv3qu0EP2afxSOaU4sdnIgJz-7_wqYGmaqdVbdVwKpFpAEnEx938SalljbP0RyJlTJdVdi-Nrs6gCfdV3U9MxVRX25hQY4H947_1U0TlAq5rQ5mTsSJixgsiNO_txstMC1VmePx0VqKadt8vvFGOPoh8g4rSELDx1LrWHRgAQjnPKu12qGRbYBxeR8CdyMGXvr7LwOWBKm-eAdAgUfTXfjx2cL_QLNtzmbW3QMIs9RZUG_qff_Ffk0mUZScA5kGgMeUxK2g2xY7XVw4OpPsFNnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hf186UZeTroH159ws62VF4IzpN4yiqz1f7jgGdVgxBFC7QmsRUMw36yqfPko2keXaep3PleGExBTFYuGMvx-MAI_ESG2rVXDU6bG93EePfIyR_DszXqtmyy41garAKTJxUHx7gz7Ll1re4ZwVzshdb2f1-bcCst_STN5p27ExqNaZjgbzkA5dVnWLTnA-qJd4JaThjJgdpB7f7lvveBQ2r8iP5boaaR6wmNkk0fxJg_5juQW7XYIXxm--Bbmefh82N3413T4TCXSX-Q6YvUtMKAqPsgjDT5g8NLLRBvpHO1KA72sFUHQicURVdjd2Tm-87ATgKD7yWoTagFHWaTOwg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
این‌مدل‌پرتغالی و فن کریس‌رونالدو روی قهرمانی پرتغال در جام جهانی یک میلیون دلار شرط بسته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/23296" target="_blank">📅 21:27 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23295">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">‼️
آکسیوس: دونالد ترامپ به نتانیاهو اطلاع داده که زمان پایان دادن به جنگ با ایران، فرا رسیده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/23295" target="_blank">📅 21:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23294">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQvr_JHzJK9U_BqI-gnq7Ryxiwc0n-hJKKCp1znbROu_cNhOqITx7LpIB5RsmWVmNOljURBUlx7eqA-QXFKFMto2sEjZx8VRn4ReO7091gsWxT-mQ0N6YXKYG06VAyuAM5mQsFt_K5iPBJO7wxxRL5uzas7vw7kaRTUWgyRKfWomkJWhtd0F4qohSEI4FpbNluZXMc5Civokl2gmd5BtvKRGLEf5Xeqfjr20Tk5B8TUxjizoCme8YC178Pv9WJ2RWTjrfbWOYYn_NYEtL6jA0S_jofOjG1nZfxqUTUc1WuX-maO8gJJpLzBXx74gbAMD5J04Vi2L_kP5KqLLuXpUAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛روزدوم‌تورنمنت با برگزاری ادامه مراسم‌افتتاحیه‌جام در دوکشور کانادا و آمریکا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/23294" target="_blank">📅 21:16 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23293">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b49d10c6a.mp4?token=FcgUxz2RHFBB_UXxraz14y9SMvOfQzboM1uLVJXOkH1mQ6eDhLwW7bD8u8UkjNNYkxbFSpDJ3eqQC0Zvz7B62RL100LIs-4_xKt06SCmk5a5cyaVLZ8Vaoiq7XWu4ZVKuYJauX4xeEzdT9NqpEyyjdArqKj-SfAua421VDfhjWA1zOS99sKG5ZtVimMN-FVnhSCEliG5LwMkB0j5FNUOBuUmYsUhs1-VAqaYBsFzHwgrgf2HVla_nINdoUBih25RZOuxwjQ_9n1266shcT5EZTfJZL1XPq1GKJQs7YhXNL6mPFQoCXkOoA4T_vu6PF0RLL6k0Ijaaa9PX4oHZ0QN_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b49d10c6a.mp4?token=FcgUxz2RHFBB_UXxraz14y9SMvOfQzboM1uLVJXOkH1mQ6eDhLwW7bD8u8UkjNNYkxbFSpDJ3eqQC0Zvz7B62RL100LIs-4_xKt06SCmk5a5cyaVLZ8Vaoiq7XWu4ZVKuYJauX4xeEzdT9NqpEyyjdArqKj-SfAua421VDfhjWA1zOS99sKG5ZtVimMN-FVnhSCEliG5LwMkB0j5FNUOBuUmYsUhs1-VAqaYBsFzHwgrgf2HVla_nINdoUBih25RZOuxwjQ_9n1266shcT5EZTfJZL1XPq1GKJQs7YhXNL6mPFQoCXkOoA4T_vu6PF0RLL6k0Ijaaa9PX4oHZ0QN_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
اسپانیایی‌صحبت‌کردن‌جوادنکونام کاپیتان سابق تیم ملی با پائولو دیبالا ستاره تیم ملی آرژانتین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/23293" target="_blank">📅 21:07 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23292">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EayyDHbwUp2Ti0oyMgZahpe6zbfI5peFzWXGweiNAkbSNTDltVoYFh_21BGqPAwVdkzw6NzXqDDcwowATSFIjJ9R7h3iuk5AiPA7fCMA6upU5NrtO32_WSxyKr-t_UbdMZ5OdauyV40VIbBZ_yvehyBuzIiJK6dLl1rh-U9na2uLp3RgvErR-FkE53RasDiGeoK7FoMdX4yCZKJRf7Vu4Q6eI3tPSPCG17alYEp7-6qWFLCVxdY_yClHzWjBMbVDmO5Hn1lyDmgpKRVZamqNdACcSRkqiOqTUdgdhrL6P13Ksp-4rltdciEai_HxSB918HwhPW2EVY5vbZ3bP_j_9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گویا برنان جانسون هافبک کریستال‌پالاس؛ با لیلی فیلیپسِ پورن‌استار که‌رکوردسکس با 101 مرد در 24 ساعت رو تو گینس ثبت کرده بود، وارد رابطه شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/23292" target="_blank">📅 20:50 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23291">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W5d5FmErc0ypnl0SNWSBppAKhEETLbTwT_fbH8q5RNrG0QlXmruQt5I0Zfivtoxg_TicbuEtivJkCetSxqIaQHQ27QsLi9voO4vZuTwPtp2by4VDHx87gxmCxuafVygwItQaBoFPS4DPnB0MGzrJZb5Jp3J4K0k_fOFXeWICRs8Lgs-t6VEW54sy1tah9C9Fnx4_3e4nKtez9R1XmLlhzUsuCSjsMsH60p4yRKV6x3VWjj_J1N4I9LP2ekx8JVIBEyZ-XHbrKmJKszlML4Q9N-6apsJwGhWX87RgzioQrLy6ihcFTvlQM342HAm-TFf-bSDMsS4yBDofbqiqaO4A1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به‌‌ بهونه اتهامات جدید توماس پارتی یادی‌ کنیم از‌ زمانی‌که اگردوربین‌‌لپتاپ‌نیمار روشن‌نبود، اون الان بخاطر پاپوش مدل‌برزیلی پشت‌میله‌های زندان بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/23291" target="_blank">📅 20:47 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23290">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hLJ07fZMpjUqIa4BsUpcd8Sy7O-2vhV30kgm9Bn2x4QGBRIGNU8BcFKoGabC0Dxyp2a6y82YbUIXJ6aF7O1er5axMTZgjtsxZfpz69ZIkl5v63VJU2GS77VV_-FHnbI9dSu5L03NXrvzpaOF_n1oOeEaOKdmm1u43LEaXBYFzFam6V3f2m_NBOoME-gTcT5iUTAHEvS0I58MxpUcW9YkqMpp7ypgHJpNB0GEaCY4ZgEjG8WHpAoe2qWs7IqRC1fjlchDVIgRSj0ntmLDDMncQYLhS-1Gf86kZNLzpLvgZrXzaodnYhp7q59MRTtE9CSlqhmp1Sog_4ifd33pZJ5lAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛روزدوم‌تورنمنت با برگزاری ادامه مراسم‌افتتاحیه‌جام در دوکشور کانادا و آمریکا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/23290" target="_blank">📅 20:37 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23289">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DJky9QgM8mtY1dn-aFQCQJ9cgChY0QY4CynLacVsCD_6DlFUI1Bkumr2jV86JbvMjgrvd9gbM8cEi8_t6AuPsJ-xmeqpS3klIxQXkDrboX6yQ1jSsJJvoROfrH9aq9VlY3g7cT-QJA9lmypgmt8bJId2-wF54ThkN-l8pvzsW6MoOfKNr6qHR0hozfCPJWjCQ8Dfwf37pVqO2A-KQ3tGqwmiseh8SjwN43axBPj1YH9LEzW9OSyYC0MO20ADd6gnaNL6gJq82HmWou_jnymgYksam22YR8lKNh1EEeC-byFdBixo3ZSVhBjJhJ_96gQIXp9RkVUSKscBCWYHp4fohA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#تکمیلی؛شهریارمغانلو مهاجم‌ملی‌پوش اتحاد کلبا با اتمام قراردادش از این‌باشگاه جدا شد و بازیکن آزاد شد. شهریار فصل آینده به لیگ برتر برمیگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/23289" target="_blank">📅 20:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23288">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r06agJUP4QT64g63xhmysjV-5xe0VMYEZ6gIBT4ltVcMy-kQK-NlnlvPwkwk3ocQY9436bo2zTP4d4I9YGbJbZqGibWze5Hpwgn_qlVmk9eY820mattF1IGSx8pReZiM3DCxdSoVQ-_esCq5VKmEMUVbsZ_189bdk4PUdGSZxOfXWb33H7d50xd2LA0xo03-pRiTqTuJtooajnRy1f3crxbUGEcjghufmmLBAjRsidBxPooIv584WCp0k9k2cUHYjjSlESoMIP5Vrwnzsoae31WnYvPQdvT2H760cd0H5Yw3iQenMz7B024Zmq8_cLZGRBLfotHxFF4xj5wR4HlUyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
مدیرعامل‌تیم‌آلومینیوم‌اراک:طبق‌ صحبت‌هایی که انجام شده باشگاه استقلال ظرف یک هفته اینده مبلغ توافق‌شده رو به حساب‌ باشگاه ما واریز خواهد کرد و ما رضایت‌ نامه قطعی بهرام گودرزی و محمد خلیفه رو برای این باشگاه صادر خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/23288" target="_blank">📅 20:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23287">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u9VfSIJ6UlmXksjujY-991nZ_LBfbGTTLMTHSgRnK9Cu-a4iUyMXgaOhqien5Da9z98GeLxE7KQ5gzkbPF4se2HCLmsDXHeHZgqZzkTzIEtu3jTtNUsJi2Zts6BXFRPfE6do0pVgvFB66NxTpDsL5CS7oe1ihO8DyYpNf8sDYiMtfq8GRYcKOhy9YKDeVh6t4Z9cXKOqQawH7D4eXrj_M86eStKIi69vLlDnmg1dNinQgt2wMtlmO5sE4rZfPF-EXYNmzbUrbRYf3FhlTF1DHSczGX4nCSMluOzeOIjLPpg2zTXCR81Ul81xkaBqz-sXfIUUhMxaJue5HwrJFzA-xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛دوباشگاه استقلال و پرسپولیس با ارسال نامه‌ای رسمی به باشگاه روبین‌کازان خواستار جذب کسری طاهری مهاجم 20 ساله این باشگاه شد. حالا دیگه بستگی بخود طاهری داره که کدوم یک از این دو باشگاه رو برای فصل اینده انتخاب کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/23287" target="_blank">📅 19:57 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23286">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AbDWPtvk1nMrpfRlwrkJVn2LBP6BPLyckD5P2ubZNiVhjBYCKF_kwuAUUj8uMwFTtWznybOAMT8gcs-uaFmnoTEJsYSSR_26z5kn0mrMC-Iod1hxt7k5s2JUV2e_gCTwWFWQx52uFXdQKkBb2aM28YEz5ihFRgAJ6aO98A6b_VN9IEW4onb7MW9JH9RNWOaeHJUPysYyuSuxXnFXCPN-HDN4uyOj-MM572_tuGz3hnlnF9z-ERrjEEs80z-kgE_YzZyu1MPpaJs6BUw_1iyEy8-A5CU4mK3ufGA_qEwWjPlxxbsHOmXQmW1u1Lr6EgFbm_XtsWUg1r2NjUwuiFWxqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#تکمیلی؛ طبق اخبار دریافتی پرشیانا؛ مدیریت‌باشگاه استقلال از علیرضا کوشکی وینگر 26 ساله آبی‌هاخواسته‌که هفته‌آتی به همراه محمدحسین اسلامی برای تمدیدقراردادش‌به‌ساختمان‌باشگاه برود. همانطور هم که در روزهای اخیر گفتیم تموم توافقات لازم با مدیر برنامه این…</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/23286" target="_blank">📅 19:55 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23285">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🔵
طبق شنیده‌ های پرشیانا؛ سیاست باشگاه استقلال در این پنجره نقل و انتقالات جذب بازیکنان جوان ایرانیه تا درصورت وقوع جنگ در وسط فصل اسکواد این تیم خالی نشود. در بین بازیکنان خارجی رستم آشورماتف، جلال ماشاریپوف، مونیر الحدادی، اندونگ و یاسر آسانی در تیم ماندنی…</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23285" target="_blank">📅 19:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23284">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46ef7ef7d1.mp4?token=onYCRk3x7d9-il1LrmXLWAFPSXE0yu_6FX46iQktasG_j3T_o6G9mWt8_Hhqmmg4K48NhfV8Nf3rfiVzxuHSflezkWWNgJFDIIXT9XiZmBmAUeNZRqthvojvk6DJCdAkXjpIF2DseWyOxSaaeKZFZpRd2LLMJugKg8gCcUNQ2_Ic7nI1iqabfAN4RjvUnrzKyE4rtIoQEIXs3PTiObjdH26uXWA-DgugmIleV-3sKVOPvTJdZJ7s0vLlsSxfzvP0f0NB3p7EoEWU1BiyJgKW-XTBY2LAnyJVjlMmDJ727M-W2pnYNa06SWrdJ-wNMCken8htB3cVwSouTHJr6_5p6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46ef7ef7d1.mp4?token=onYCRk3x7d9-il1LrmXLWAFPSXE0yu_6FX46iQktasG_j3T_o6G9mWt8_Hhqmmg4K48NhfV8Nf3rfiVzxuHSflezkWWNgJFDIIXT9XiZmBmAUeNZRqthvojvk6DJCdAkXjpIF2DseWyOxSaaeKZFZpRd2LLMJugKg8gCcUNQ2_Ic7nI1iqabfAN4RjvUnrzKyE4rtIoQEIXs3PTiObjdH26uXWA-DgugmIleV-3sKVOPvTJdZJ7s0vLlsSxfzvP0f0NB3p7EoEWU1BiyJgKW-XTBY2LAnyJVjlMmDJ727M-W2pnYNa06SWrdJ-wNMCken8htB3cVwSouTHJr6_5p6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
صحبت‌های‌جالب کریستیانو رونالدو اسطوره پرتعالی تاریخ فوتبال درخصوص جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/23284" target="_blank">📅 19:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23283">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/joHgx8ZAXmUIQgkjd2EWnM_rD9AzU3dXJJk7-C-K7JuXOXh6VOtPa1_8mKYTKzTNdoRLdA0oLClKRMCk39Lx7h1e_CwNc5X3CnW_rGu-rRrkgFU8qtIwIzLOKMzdOf0tXvPBg9CT-gsLkvzi-96_dCO_RO9urO_cJcmaWsQAVZjwVIwYhwxMgI_idYVL-EzGENTfV053tuPLBg1JQhmC1vTY5LaJySrQjHkGyUV2mNPs3CeHGw4HVgPHF0hI8m0hEgwu2kTrMQDPCKUhm7tv-4LCAI0VwNqH76_zWz7AVbk3IFzf9Oajl_N6h_ekFQzj6-Asiiln5NZFbFsT6Mkt2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ارزش ساعت جدیدی که امیر قلعه نویی خریده و در تمام شات‌هاش نشونش داد 136 میلیون تومنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/23283" target="_blank">📅 19:04 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23282">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64a2fd248d.mp4?token=fI3e1AG8tYM-AU27MMqO20c7fCvOuxZmv_q6adpB7j9mTEe6FWF7zkSP_05jHOrWSyARqUeTbkrJllokLAHF-nmdYJFNaJM3RYSjELTZm2v5SyOCJDo2LfgPTl86jUV0WgNK9JZ0KZvqjLnTKLPBHDKcWEl1YIKtrbQorgDN5db6cRusJNR2D442eW2mA0ob1MuLU-ocKke9PRC4V8H4FJnxgHx8I4T0ja_7RP-OlwuU88aWZzpFJqHZAnqGQKttFMg5Xwt6RPP0vI_un83SMfxu-UIW20HE8e6S3qTi-ZfVSoWCttQvdTwoGXqVXv3HkgUL-wweEUm19nkayZLQKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64a2fd248d.mp4?token=fI3e1AG8tYM-AU27MMqO20c7fCvOuxZmv_q6adpB7j9mTEe6FWF7zkSP_05jHOrWSyARqUeTbkrJllokLAHF-nmdYJFNaJM3RYSjELTZm2v5SyOCJDo2LfgPTl86jUV0WgNK9JZ0KZvqjLnTKLPBHDKcWEl1YIKtrbQorgDN5db6cRusJNR2D442eW2mA0ob1MuLU-ocKke9PRC4V8H4FJnxgHx8I4T0ja_7RP-OlwuU88aWZzpFJqHZAnqGQKttFMg5Xwt6RPP0vI_un83SMfxu-UIW20HE8e6S3qTi-ZfVSoWCttQvdTwoGXqVXv3HkgUL-wweEUm19nkayZLQKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ
: آتش‌بسی نقض نشده داریم به یه توافق فوق‌العاده دست‌پیدامیکنیم؛همون لحظه خاورمیانه. یکی‌از دلایل‌مهمی که اخبار جنگ رو پوشش نمیدیم همون صحبت‌های لحظه‌ایه. مغزمون به اندازه کافی سرویس شده دیگه لازم نیس صحبت های لحظه‌ ای ترامپ و جنگ رو پوشش‌بدیم. همینکه بتونیم اخبار مفید فوتبالی رو در اختیارتون بزاریم برای ما کافیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/23282" target="_blank">📅 18:58 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23281">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/udslPFZC419yJYfpllK23VKvcK83O9n7vX0AM7AVoZri1MFSY-3qUtgBaObV6Sj28xS416w0dybNQFmfbI8jHiTZY0wQNZy-SGTHlUFqDe9uHLyMjzKxpQS35paUJsMB-Hmv4Gp-yI5G2US_yENM1k78gUcEeATW3TDRoTt8k-6Oa5NBsWFA-RVTOKSAstddflMpC1haqqe-KGz3vtcgJnS6JFP-mOC8QxmgEPXg3fHutBwXbKhpz9QHBXiagY2vmNt1gOCjMZt7yqqNKxLPAtgytv6wRzZ92slepwCCFRrgZTEFywZZcXHjexZkLxowStHr7wUoqmBPQt08xGvfSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
اینجابودکه‌عادل مثل خیلیای دیگه شدیدا کراش زده بود رو دیبالا دیگه شروع کرد به تعریف و تمجید ازش؛ خنده های کاوه رضایی هم داشته باشید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/23281" target="_blank">📅 18:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23279">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20d475f3d8.mp4?token=ezRc0qPVMGr_MYU119zSXT1x3J3_9m57HxzSv8mWkGp4mB1jVkKQAiylo52MP7VQtO-cpQntiScWpaB_MtRhKlruIrhPQ-36RSuGxwEtqMgdn8K_7wuLUGwV6PVNEiZdcYYjnAvZV8ZBdbIJnDN_pVzr9Xzdp_g_KlZ1sb_RWMHt9UhukPvxplEn8_fdGXEdI8tTfxlqMYxM_ehrQoQWkBIIFE_KCcw8vEOFlAK_jYJOTE00UAAu2q57--9LEfa2ql18LrmDTJS5g0Zvoow3aM2p3APa2ZABAqc44xAysvb6nVFOTY-TxFbIl19kMeCcr-Ldwe5EERZ3uT7urFoPOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20d475f3d8.mp4?token=ezRc0qPVMGr_MYU119zSXT1x3J3_9m57HxzSv8mWkGp4mB1jVkKQAiylo52MP7VQtO-cpQntiScWpaB_MtRhKlruIrhPQ-36RSuGxwEtqMgdn8K_7wuLUGwV6PVNEiZdcYYjnAvZV8ZBdbIJnDN_pVzr9Xzdp_g_KlZ1sb_RWMHt9UhukPvxplEn8_fdGXEdI8tTfxlqMYxM_ehrQoQWkBIIFE_KCcw8vEOFlAK_jYJOTE00UAAu2q57--9LEfa2ql18LrmDTJS5g0Zvoow3aM2p3APa2ZABAqc44xAysvb6nVFOTY-TxFbIl19kMeCcr-Ldwe5EERZ3uT7urFoPOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇽
هواداران‌تیم‌ملی‌مکزیک دربازی‌افتتاحیه روز گذشته رقابت‌های جام‌ جهانی با افریقای جنوبی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/23279" target="_blank">📅 18:25 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23278">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d34dfb18b5.mp4?token=kZqh_qLoSdPmMCUQoF-2DE7ycvYca0urAUmQzYwL-y0D3aNeOxgJolgBUK0bm6vBWFnrcx6h1eJta778L9oC16cWliQx1fT-fvTM4YkUwTMPvKF7y2rcqx9bGpoItz0W63kpvfTnDj9vLi4NzKLIFN-tvZiBaexw77gxWkosAIgu-dRErgRpe7NDgYkNFbqS27wQuzveGRLkxsxNppxm7bgopRpxG9HvrmQNQoEe-CnPXR9gaWHvRqmG7E50C7_RzAFhq-9Db2ZKZLV5ciDLvQbtKjkEbQ7K3A_cLivdU8WYzUIq_IAC-mqt3jdYXGgK50x3L_mACfXtrrfWDgAIJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d34dfb18b5.mp4?token=kZqh_qLoSdPmMCUQoF-2DE7ycvYca0urAUmQzYwL-y0D3aNeOxgJolgBUK0bm6vBWFnrcx6h1eJta778L9oC16cWliQx1fT-fvTM4YkUwTMPvKF7y2rcqx9bGpoItz0W63kpvfTnDj9vLi4NzKLIFN-tvZiBaexw77gxWkosAIgu-dRErgRpe7NDgYkNFbqS27wQuzveGRLkxsxNppxm7bgopRpxG9HvrmQNQoEe-CnPXR9gaWHvRqmG7E50C7_RzAFhq-9Db2ZKZLV5ciDLvQbtKjkEbQ7K3A_cLivdU8WYzUIq_IAC-mqt3jdYXGgK50x3L_mACfXtrrfWDgAIJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
اثر پروانه‌ای چیست؟
یک تغییر کوچک، جزیی و بظاهر بی‌اهمیت درشروع یک‌جریان، میتونه در طول زمان زنجیره‌ای از اتفاقات را رقم بزند که در نهایت به یک نتیجه‌ی غول‌ آسا، کاملاً متفاوت و غیر قابل‌ پیش‌ بینی ختم شود؛ درست مثل این ویدیو. ببینید حتما.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/23278" target="_blank">📅 18:25 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23277">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v2HkpyfrML1aBF5Ras5LYOb_2AW59_xHIjUo8RMvEVQ_Y9S0wq7CVBRll1yHPxv8fvroXahT1jzKV-ak9BDKxIL8gUbjhDOdhvjIdamA2Xbg1lo31LmLNgDRtvO99RAUeTeLP1Fnro7ytm0VQSbMSsNvg2iZ2e2oKaLqwxEDZ_ZpGRlxl96MplYwN3Or8Jt9favRjI9KLuosqLEar42YASmefZA8pK6gwh-2mOoQ4zYS5Nap12hNwbHvQ5jUXXlGfJSnR4WjWv233TqFlhktTmYqqk9iNjMN-FpPhZDlzCUo-ES9oBB_K1kf9Sfqpf7gk_z7d0g3CpW3ztNVPnlcVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
هدیه‌ی ویژه برای کابران جدید
🎁
اولین واریزتو انجام بده و
0️⃣
0️⃣
2️⃣
🔣
بونوس اضافه بگیر
💰
⚡️
فرصت تکرارنشدنی به مناسبت افتتاحیه
⚡️
🔴
تا سقف ۳ میلیون تومان
🔴
⌛
فقط برای مدت محدود
💣
بالاترین بونوس‌ها فقط در سایت وینرو
🗣️
امکانات ویژه‌ی وینرو
📺
تلویزیون لایو برای پوشش بازی ها
🛍
پیش‌بینی مسابقات با ضرایب رقابتی
🎇
بونوس‌های متنوع و جوایز ویژه
🔝
تجربه‌ای سریع، متفاوت و حرفه‌ای
🎰
همین الان وارد شو و با اولین شارژ تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگیر
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
📱
کانال اخبار و هدایــا eg22
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/23277" target="_blank">📅 18:25 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23276">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FjFUYGIQiOCossMPLNVJrLIYHUpkf6u31Br0np8V3U__y_akSmbyntd0rRvfWnB342zem51u4fgOd4p3lR_HNfFZwnSGP79S2CJPcf9Hwxj8W_U8s8EsPweoB22joTL4aU2XFoFaYDDfw-BoCfsi764s2N351vp7lXop3Edo7DAdRCxCZBdXiVrrvxRqZFduIZpCLJmUchZ4YgqGxJDCaqbjHT-fSP-7NeIYx4kihkFrYbeK-tgJkfa31P7JSDUoxj_ZfE9aqoPary_4qwTGStYXhoBK855KzUAniwKvFY8rNfXRbzJBhP_0Gg93iRES3Zwp5c_FkX10Fi0qG8l0Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛ طبق اطلاعات موثق به دست اومده پرشیانا؛ باشگاه استقلال افر سه‌ساله سالانه به ارزش 1.2 میلیون‌دلار به دراگان اسکوچیچ سرمربی کروات سابق‌تراکتور داده است. همانطور که در روزهای اخیر خبر دادیم تنها شرط اسکوچیچ امنیت منطقه است. گفته جنگ کامل تموم بشه دوباره…</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/23276" target="_blank">📅 17:45 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23275">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9833527b4e.mp4?token=Nch8nuybe15UbPc1LG3ff6y5J68vRo8vUyB1Hw-G-xXKb3wyG8tQaNkOdR2ZOlIF1YHVfWPCRHXTGgtcey8xhmvTPXIBnS0eoueSNuXuRLuIiLOHjzABmf3goJheIxpyqsIuWoEWGuTGH3i0D1wDFi4JEULngQYgdc5NjbZ5iUbAyyVcECbhkoS7E6exVwgKsHFKlUxJuvCYANTGBcUnYWBK_Cp4cakPxLzB9AiHDLQ1JkUnZjScKHYu8DyeKh2pjzCPxcwGOQ8FoHQBgvh0lVVVfG-5M-oM5slXXHMc6C9wM9mxQ7qyZFV4ngN4Ce-uCZguqLINauBdFBEcOhYGew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9833527b4e.mp4?token=Nch8nuybe15UbPc1LG3ff6y5J68vRo8vUyB1Hw-G-xXKb3wyG8tQaNkOdR2ZOlIF1YHVfWPCRHXTGgtcey8xhmvTPXIBnS0eoueSNuXuRLuIiLOHjzABmf3goJheIxpyqsIuWoEWGuTGH3i0D1wDFi4JEULngQYgdc5NjbZ5iUbAyyVcECbhkoS7E6exVwgKsHFKlUxJuvCYANTGBcUnYWBK_Cp4cakPxLzB9AiHDLQ1JkUnZjScKHYu8DyeKh2pjzCPxcwGOQ8FoHQBgvh0lVVVfG-5M-oM5slXXHMc6C9wM9mxQ7qyZFV4ngN4Ce-uCZguqLINauBdFBEcOhYGew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
شاگردان قلعه‌نویی شب‌بازی با تیم‌ملی نیوزیلند؛ ژنرال ایران از تاکتیک‌های خاصی استفاده میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/23275" target="_blank">📅 17:32 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23274">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CnWKFrUKkjNPnrniZfNyWGNX5-mijc9w7okSqzQnwHfLtgl77oRlMUbkXGm0_PIFGR29L74PfHRC_2PBdXztLuMEk9ODZw9zhECiLhyCR1jow5NoFA78WXzn0nEx-AVcO--vSEQzw7jPWJ6s0F1Gci1sZTrWZ9yvPH5zpGowJMjd7nhN7UdErPn1tu9r4U-Oo_Z9Fv0-IkIpSqsY9Egd5TaeVFYEoLddnwrAECgu_e1E9o08BxcB5IALhF-LFLlFBVpaxdKxsQOMU5cDi7u_3b62dLrnuLK9X2Jm3lxGSIeV2SXpBbGpPF29sj9ol2NanXlEPC4LIU8OyiwHpTyVGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
این‌مدل‌پرتغالی و فن کریس‌رونالدو روی قهرمانی پرتغال در جام جهانی یک میلیون دلار شرط بسته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/23274" target="_blank">📅 17:16 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23273">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0ea01c2e9.mp4?token=W3Bi4GUeGvZM297VojDmtqY6BSPGR9qcxM0QryvQC3HV00y8xbNLriWmnq6X_Lj34pPyKNrUiMhMIl7amlsVVm7xhW-QoKXNzssgvgl8m0mTIYQenhnE-s6bLm6VhFVLMS6wRaWLBGLdUJjjgEAzvUU3KnW4WvRqRGd55iXzfHzEppnIJBY7-06EbC2s7_eGGHnS3d1ZRyOi3e5bgPHEAhj2ZYsBP_dHFicsZXY_98l06HybyEhk_ZJJdUFA3GfAvLm-1H4KfxefcQhFeXt1MQDaEyjeiovf6l4DCxbdscYp4g9hKgM6sTCvObXcFVvNLK_-fDBdqNwo4mAJ6CZO7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0ea01c2e9.mp4?token=W3Bi4GUeGvZM297VojDmtqY6BSPGR9qcxM0QryvQC3HV00y8xbNLriWmnq6X_Lj34pPyKNrUiMhMIl7amlsVVm7xhW-QoKXNzssgvgl8m0mTIYQenhnE-s6bLm6VhFVLMS6wRaWLBGLdUJjjgEAzvUU3KnW4WvRqRGd55iXzfHzEppnIJBY7-06EbC2s7_eGGHnS3d1ZRyOi3e5bgPHEAhj2ZYsBP_dHFicsZXY_98l06HybyEhk_ZJJdUFA3GfAvLm-1H4KfxefcQhFeXt1MQDaEyjeiovf6l4DCxbdscYp4g9hKgM6sTCvObXcFVvNLK_-fDBdqNwo4mAJ6CZO7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
قسمت‌اول‌برنامه‌فان‌جدید ابوطالب حسینی برای رقابت های جام جهانی 2026؛ عالیه حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/23273" target="_blank">📅 17:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23272">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WRCWQpX8swPcRA6b0Rk_aPao99_63RIpZUOQAZmeevY9i3cm_xX1sHApj8vBb_ReCgOeMYt6R4m_e9asYI4qJSItga2m4GQBBOZHoj5AGvzRVc-4VhyttRceTPUHZG2HvqDMpcBpV0y6WC7hd5ppaKw5g9m9Xv6DPhHagD3v3Hnsrn9o6lA__A_McnHUrXivtxn5kmnLLgtemKRWq5POFs6TVj5y0ouI2sJXGSqUhf6WtMXuCdnMFYU5zuC-fPDGT-kpoUoQWciHUOgXhzlf8Cr0GeW8JYBHjhJJeOzUDTXBkgAEgRLP6P2-PU-tUq6m_9IkQ4OGa00T6DaTG21tLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همتون‌فهمیدین ژنرال ساعت جدید خریده یا بگم بیشتر عکس بگیره ازش؛ 7 تا شات ازش گرفتن تو هر 7 شات ساعتش رو انداخته بیرون که مشخص بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/23272" target="_blank">📅 16:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23270">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q1a4HIan_gDMgdX7WkaTGsNjaHSMG41x-rmRwvLZrGsWpqg8ETj1vVWsXMx4NWCcg4pIUNUk2xt7xVKYvjxY0m5iog1eO8oVmq6NbIn6GlNZgO5IgYaFoIL_r-GcG7d6GJ_LxO-pdH1gteV_QkcWeog0ZaASMwIKoDoZofdnaR32JqLVMJ4lRp3Y_TyHmNgLni19j4l4HU5aEPdodR9Qc0uEkiJlskN5uh8bhohm5M-GBMA1wDWRjcFQZujjd7UTvuYlm1RUh2tKeux-8LenCmL4IRlFWD1SWWj19uV2z3QPztjR7sUpSzZZYcyVOgMVuCr1fmg8IymG9rD87h0oxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ITofklj1lr_Bslvyho7rRNePrQoljBRwq2qUkGluIpg5vwfSeLcMAg_qfXxYVnzw4bZXiEWBDHmfIbQnUsYQf9W-W9oFXiy8b8TDL599hRBFiNFDabr1N3jEFvyZ9vAkPM6ah2x0ubDZCToeO1bspqUV5Lb8R2uj0YePq1CNlC75xfC_L9p_9AffIY8VBsqpYFOU2tztRH98cYvlAz1MeY_mh5fD9ZqQbiq0oEIUGPQhi3VdIF1fEYgAf6krZmkKJ8fuOjrsrXSFrqik2ucoOCml-BCI0AS8zYhwRwaPzTcVDyri4DJZg7hQg9CKQsy-zvt5TX_bxo9jCO47Yqzs5g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇲🇽
هواداران‌تیم‌ملی‌مکزیک دربازی‌افتتاحیه روز گذشته رقابت‌های جام‌ جهانی با افریقای جنوبی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/23270" target="_blank">📅 16:29 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23269">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf1b43a439.mp4?token=eXugSQKqTiGM2bP9o5FjzR7wfkLr30M_L0MV96mxCT7xL1wZuAfxB1CmjbqFsa8K-AQZpP5DxOc6FQ_4RWeGvz7iJeaer64cX8BsKPGk7qcag56BGFzJesYdRhmna1n8xR0P6WRFrqKBFCYpgxd0Yi53htwS_xNQwVmMpSLY2s8nyPC4NcarPTw4dL1GCcw6nMg4fZX4sg1LgkqGgHiMbkrIG--GCRDiBm8RVrU0bR7o4U7pMMI7HIHrqpU06fKsLyZbF0l8--DoS43G_B0bMRsGKQvx0ybZUQawX_FYrXUdKUM1kj3mZEftnyxG3Ra6dRua0_wQIfVIB_LWS0efHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf1b43a439.mp4?token=eXugSQKqTiGM2bP9o5FjzR7wfkLr30M_L0MV96mxCT7xL1wZuAfxB1CmjbqFsa8K-AQZpP5DxOc6FQ_4RWeGvz7iJeaer64cX8BsKPGk7qcag56BGFzJesYdRhmna1n8xR0P6WRFrqKBFCYpgxd0Yi53htwS_xNQwVmMpSLY2s8nyPC4NcarPTw4dL1GCcw6nMg4fZX4sg1LgkqGgHiMbkrIG--GCRDiBm8RVrU0bR7o4U7pMMI7HIHrqpU06fKsLyZbF0l8--DoS43G_B0bMRsGKQvx0ybZUQawX_FYrXUdKUM1kj3mZEftnyxG3Ra6dRua0_wQIfVIB_LWS0efHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بنظرم بهتره برادر بعد از این حرکتی که زد کلا از فوتبال خداحافظی کنه و پشت سرشم نگاه نکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/23269" target="_blank">📅 16:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23268">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uziv-EEEJt6JT2xHd63Z7DzhHkqZIx8GgQUdWfNwh7_xR0TfkyDpkKy-sU3SGHN48d59OTo24zqsJVeeVv77JPdhzY-laahp6hj8EwFA5DI9giGo7U06GrPk1rZOADxDQKkRvaIQ_ByrOVYzhm8H567wFbwjPaKZPvF5udiIzZXCRsoLDXWQ46sYJENzyGM0wo8nlFNVNhCfS82S74pl2jXW0sNB2WHF3Qamz71bVLGjrRKbzen8CtETwpgpMRD2RTDnqWNAhInQZd_ZZ4_dAU7gyRcoB4dc_rUHEo2MTS13JtyQMEWuW1u-Mw81ve_pzJFZLDXc1VSKJ1VuV8FAzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همتون‌فهمیدین ژنرال ساعت جدید خریده یا بگم بیشتر عکس بگیره ازش؛ 7 تا شات ازش گرفتن تو هر 7 شات ساعتش رو انداخته بیرون که مشخص بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/23268" target="_blank">📅 15:46 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23267">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bEghjjt1ULikenVQWTqcaoXd8vdelEB7cFtIRH9MG_o-RIvPBnQohhjg7Me3ajZiwYXXyzgDCxoo6hnxTmx2fyTtNlN7jRmW3CmpfnRxfl1yWJdQYNYaObQBAFk-yn4Q0c77Us_rER0iKjHp5OJ1JeOlReJEPHJo0UjyVnHZb6Ir4vVnCnS_i4PW5Cw6IORlMIBEv1AZXP7y_O5IQhzG-oS4CY9ckCxO1Jr_TqARNYqyGGvfm3FiAdacChnX66mWQghilpy80K4KLrMiNM5Ny0dkzafgw_TLOKoZrzdY_IWWkeVnHhoQA2S5AfsCmaBR8SfxxszhpC1rcWgmg9i5Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛براساس‌رسانه‌های‌نزدیک‌به‌دولت ترتیب رفع فیلترشدن پلتفرم‌های‌ فضای‌مجازی به اینصورت: واتساپ، یوتیوب، توییتر، تلگرام و اینستاگرام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/23267" target="_blank">📅 15:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23266">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/060b4ac464.mp4?token=gPU35x6bacDSh_uvKAVLUEatyIrEo02VONdOp96L0BP0YEELOxgTh9x_UddnQdSbmGLLbtlFKXVZ88leO5Izyanb1DcLkwinM7HBmr3__dhimN3vEpWcm5m1QXbZsarb5vAaJeOUPSoABO6LKm1pzGNg30zrak7-SBUoE04cPClCYAO3GgpLlPq7lW0L5Ml_NkluiPWlvlnHYPl3lK2bKIhvqx6ZYlQUgyG38SAE2OLX06k_RukKrBNMLGqV3ZtYThuL8PZmPb07MQ997wV5bgUagSxjc3wvR4A5sUlrvliSwYb0bxe__805o5B4lUfMYaZAheiYGtY_PrKzPN5xuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/060b4ac464.mp4?token=gPU35x6bacDSh_uvKAVLUEatyIrEo02VONdOp96L0BP0YEELOxgTh9x_UddnQdSbmGLLbtlFKXVZ88leO5Izyanb1DcLkwinM7HBmr3__dhimN3vEpWcm5m1QXbZsarb5vAaJeOUPSoABO6LKm1pzGNg30zrak7-SBUoE04cPClCYAO3GgpLlPq7lW0L5Ml_NkluiPWlvlnHYPl3lK2bKIhvqx6ZYlQUgyG38SAE2OLX06k_RukKrBNMLGqV3ZtYThuL8PZmPb07MQ997wV5bgUagSxjc3wvR4A5sUlrvliSwYb0bxe__805o5B4lUfMYaZAheiYGtY_PrKzPN5xuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درسال‌های‌اخیر؛
گولر، اندریک، دانز دامفریس و حالا هم برناردو سیلوا تا آستانه عقد قرارداد با بارسا پیش رفتند اما در نهایت سر از باشگاه رئال مادرید دراوردند و راهی سانتیاگو برنابئو شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/23266" target="_blank">📅 15:25 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23265">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PAsokkGht3PbJ1KEAO3xLVm5xVZuc3n7Y6f7AJAUwWWUSsrhp_cF8SI9FHTCVgKPTC5A_CxqPCN9-9MboI2po0pu9hwU3lRJlik-ujL15UF0F5jyufeADeIYGXK0IB_VCPQdoYttv-sE8h8dB5pZ7BWW8ufYkQfUkKoZYztXZwdt0ISH38NiYluucxQKFzwAA1s58Z3HGv6dkrQLp4tEIMn5gpZWq4SBTXp0qdL-e7ybEVgAgg0Tt9IF2WzjBhpk8boWiesiverOdZTO-g13Ft3PfiL3ClZ5k7iieSQE228WT_vvc81YRDokZ0KisMXjXikoiGgEepBcrfW1A6nHLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اینم‌یه‌لیست‌دیگه ازشبکه‌های رایگان ماهواره که قراره جام جهانی رو به بهترین شکل پوشش بدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/23265" target="_blank">📅 15:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23264">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/287a3c4809.mp4?token=ArSyxhSDCZeJszVgrJhgbcLwGvmpzMX5uK6WAcc_1K-kjESRjUsnz1Z9F49k2B_FQsXO00D2lvfliRZ7C6T5VYctDAJozlUy0CT39qgmwuicMMvXbOqRls_ygcuHarpaMnSGh5KyH8bf6lPdeo6kR6EI-i-dWOmtKEwhvCYsyKbaSr1OKcUd1WI8HbnijKstL4UHsYgI2iCwCZpyBWxWqHyVwje4loavxjBHcYEleq0DzM1ZSxyeeAXvmjbCYtJLfEHDmXsyi1oGzKF6nj1-JtlC_MbPQ341ax_88vtAb63k-0AkQ-CsXsv-hpxw-TOHXF34sk9Jyadxk9m6QucvEoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/287a3c4809.mp4?token=ArSyxhSDCZeJszVgrJhgbcLwGvmpzMX5uK6WAcc_1K-kjESRjUsnz1Z9F49k2B_FQsXO00D2lvfliRZ7C6T5VYctDAJozlUy0CT39qgmwuicMMvXbOqRls_ygcuHarpaMnSGh5KyH8bf6lPdeo6kR6EI-i-dWOmtKEwhvCYsyKbaSr1OKcUd1WI8HbnijKstL4UHsYgI2iCwCZpyBWxWqHyVwje4loavxjBHcYEleq0DzM1ZSxyeeAXvmjbCYtJLfEHDmXsyi1oGzKF6nj1-JtlC_MbPQ341ax_88vtAb63k-0AkQ-CsXsv-hpxw-TOHXF34sk9Jyadxk9m6QucvEoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇦🇷
ویدیویی‌باحال‌از مسی‌ودریبل خاصش؛ همه میدونن‌میخواد چیکارکنه ولی بازم دریبل میخورند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/23264" target="_blank">📅 14:53 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23262">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/otMSS85PcolDzgCwL2FiR5Cx2M9VA2s8_TC8tbV-VZroKUUFqmOyCzKO05otzWJQ5d6UZgdjKNx20eSYOV8hT78XumIe_f3L8M9vWz8E4n17PIMIV_Cb3OM7cipg8hbbT9Ay_RAGb4qAiVt29TRVYkNKDbF2vPOU3G-XF0ir6yy81AOlrVwcXmERwwFZAdJL2BAIOYgVYImffVzUHCI6w9dcvTmgF_D_efBJSXtFws64XFNvyzWu3MuH7qYO4vATuuBi5Re0tBISjhatu9xtwioquTw5aEB1v-AXmkvPNd3CrqX00LKQ8cs35nnkRdMEmwAgZ-TyLEzXWa9sXBVt5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
۳۲ باشگاه با بیشترین بازیکن دعوت‌شده به جام جهانی؛ بایرن‌مونیخ با ۱۶ بازیکن‌درصدر این فهرست قرار دارد. تیم های پاریسن‌ژرمن، آرسنال و منچستر سیتی نیز با پانزده نماینده در تعقیب صدر هستند.
‼️
نکته‌جالب‌این فهرست، حضور دو باشگاه ایرانیه:
🔵
استقلال با 8 بازیکن…</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/23262" target="_blank">📅 14:36 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23261">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5eeffe144b.mp4?token=etzC1XevbLQJ-na9E8Os7GLNTwWB_EOYEnc_HH7LHjLs87ooa60Jd0FyQQNCOWYiAlwVG1iJOIkj_-ZW1-FXsXIwqCw4JRvpibhWcg10gNJlNeye9vFVHttLt8mSQKEpEVoOPocQhwqqkK9cyX-cZgvsYqu1uiQlwxnl9blYo44Q37Sa083WSzB78KhWnAZ4iETA9JY1IQZGJn71ZuePi-wM0-PoPt2fLJKktCTIhmQWXpC-F0LGnQTcXnNk581n45hTBt1CYHcpu7ovhMRB6k4ddwZNUuZmM_4m5o3AYseGYy2ZWb_LmOzcVyKmexKQFY1cVUWCxii0sUUMNHLsUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5eeffe144b.mp4?token=etzC1XevbLQJ-na9E8Os7GLNTwWB_EOYEnc_HH7LHjLs87ooa60Jd0FyQQNCOWYiAlwVG1iJOIkj_-ZW1-FXsXIwqCw4JRvpibhWcg10gNJlNeye9vFVHttLt8mSQKEpEVoOPocQhwqqkK9cyX-cZgvsYqu1uiQlwxnl9blYo44Q37Sa083WSzB78KhWnAZ4iETA9JY1IQZGJn71ZuePi-wM0-PoPt2fLJKktCTIhmQWXpC-F0LGnQTcXnNk581n45hTBt1CYHcpu7ovhMRB6k4ddwZNUuZmM_4m5o3AYseGYy2ZWb_LmOzcVyKmexKQFY1cVUWCxii0sUUMNHLsUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
هفته اول جام جهانی 2026؛ پیروزی راحت و ارزش مند مکزیکی‌ ها در دیدار افتتاحیه جام جهانی و گرفتن انتقام مسابقه جام 2010
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/23261" target="_blank">📅 14:26 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23260">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NjnJpFt8rY3KMM8Vfr1c4-oRzHN0wxARMsPazaVAW2OVR8JOKKnZ9CyL9PrUsoOEh8H3F2tZdocuwuGN-U2aMQKctNnbqMnBsvdj-VgZgLtHkjiustJAD84DieKqRo0ejv8WClI57djRMHvuczgUWFdcVMt3fVvtAqN058DmWUdViOx0enyCdGMfKAjRWM9mC1a0kUUjcQql_Xqz5mhcitZcbkao9oVy2POFAlOrRdGQ_X3bivhxoq12i4ZBnfDZiOuBSAgx7fWaHwlwb1tA-dzsiEV0jePiRT3ZGwTeNUO-whbXsrRT2HtSgqEsplgnEAewF45KIjhIdPhJbS4Ikg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛دوستان‌عزیز لیست نقل و انتقالاتی باشگاه استقلال کاملاآماده‌کرده‌ایم و قرار شد امشب بزاریم که‌به‌احترام‌مدیربرنامه نزدیک به این باشگاه و طبق‌درخواستی‌که از ما داشتن فرداشب لیست کامل روبا جزئیات میزاریم. امشب باسه‌بازیکن مدنظر تیم جلسه داشتن که فردا…</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/23260" target="_blank">📅 14:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23259">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7927d57219.mp4?token=HpYvolE5WZyG8a8wMLnQlBP1viS1LpX80PeZFXTka-afL8JZUMKjvaBRwkYfPGvMsU8ncz4O2nfjE4EkBHT6-UDgQb8vCBRltk_hxTgQsx1LJM0gIeaE48gkiFM7F0Rf3EIuzbR8NlA1e0OyNOhJoJKj2QZb3_wI38sYWfFRHyis2WEX7Nd8e5c8uTakmdfBqojzheJDznC1zdKO1h3uOuF1G1dKz_3OKtttbGFOgt6PDVzqCUqJjnICRUDdTtCeP1Dg9f1yoeKFV2-tiKPDig2wH3D6Eb-twUQ4iCywc8BmLjvpY-7osRgcDmv2KZVx_7le9tu4Cv9rw1jSRMgZAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7927d57219.mp4?token=HpYvolE5WZyG8a8wMLnQlBP1viS1LpX80PeZFXTka-afL8JZUMKjvaBRwkYfPGvMsU8ncz4O2nfjE4EkBHT6-UDgQb8vCBRltk_hxTgQsx1LJM0gIeaE48gkiFM7F0Rf3EIuzbR8NlA1e0OyNOhJoJKj2QZb3_wI38sYWfFRHyis2WEX7Nd8e5c8uTakmdfBqojzheJDznC1zdKO1h3uOuF1G1dKz_3OKtttbGFOgt6PDVzqCUqJjnICRUDdTtCeP1Dg9f1yoeKFV2-tiKPDig2wH3D6Eb-twUQ4iCywc8BmLjvpY-7osRgcDmv2KZVx_7le9tu4Cv9rw1jSRMgZAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
خبرنگار کره ای پیش از بازی تیم ملی کشورش با چک درحال‌ضبط برنامه بود که یه خانم مکزیکی اینطوری خیلی رندوم اومد ماچش کرد و رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/23259" target="_blank">📅 13:51 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23257">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lRPkKrUt1daiT_VldpiTTaWgGld-YjkWhhKTIbsnldKAji6ExWq4Q5t0vEzrPt3EGEvJZ2ZI4i5GskAulzcfYKmMiN7wFC2PvAVA1v1JqQQK3kzLwD6-dfoczAFpx9J1k6tn5uslRIvhAK_C9ySi12PI1PmXlkwKJPfAMhZHJj4SQAt-ssgvciiarw3ANk1f9emnsrs-pSpCBO-rPhX5RnyGzWJOEhqu0W3yDVuXHJhUbdkuNMc1hCbf3D4yJY-uyoGIYMnuFlWvqzxWV7JFEo3wammlzsc_zPeF7wLWcDUsi0pv6qscleJjxiy_0x83H4b3Ea8vcIPe8369hLLMhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nUL8VAAQcsVbdu7s49zyg8ehpk3giWWMiogE2xXYnsO4e5t83AXVlIqVUIoXu4qj4c5tOYN_sgwkMBQazGashlNC3z97HqGFKZBoIWJ9NZhK4B9TaAh9onGx7s8J63Gv9hSH6qVkzt1G9WYMk28veRDhk1LUVbhALg99f51BGeturQTguvvhqsMMLxipMiTbYV-C7_aCzYDHP7mMbsZ7M4xcWaY_Mm1dCTWRIph-WXyov1bH8rXBTC0jE9G4nFSUQYSOYKaxIr1DhmCsoekdCDEHqT3ykv7aT7KVwBtOfTwSZE2_OYBqZYH6PkrC6XsQqqnQtzJZwzAVR59addBOUw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
به احتمال فراوان طی روز های آینده؛
پائولو مالدینی، لوئیز فیگو و رونالدو نازاریو نیزمهمون ویژه برنامه عادل خواهند بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23257" target="_blank">📅 13:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23256">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🎙
استعداد ناب گزارشگری روببینید فقط؛
با این سنش چه صدااای خوبی داره چه قدرت بیانی داره. رفقامون تو شبکه پرشیانا اسپورت تو کانالن باهاش تماس بگیرند که گزارش بازیارو بهش بسپارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/23256" target="_blank">📅 13:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23255">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d62cMLR3cL4zZIotCGw5ijrGFGGIxxEZtkpFvYlBgZf6EAuXl_QfbEaaDm9gFj4FyOP-8JaPx1Mqyzrasi9OjbYeYNNsQgJXlipXwcx48Sc4MA-BvsXt_87mdQ-Tm9alB6k8p6u7JADr0G02lVzFYyFh04JHwxbqzXJqkjF2e6ghie7AuZdk3P99j_PmPWLiaZJypPZfETPiQrVlEaMBIxbGzNz9EBwMaga-9T7qIxqy4VZhQ1Y_WAFCVGRk1tQHTzCkAqBcWvEumCQT_cTcI4YwiYwTkbChhXDgZTIMNUY70_lFLfHYwMV1qbkp-xjliiVbJO3s2bGHCvUqqkK3rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
خبرنگار کره ای پیش از بازی تیم ملی کشورش با چک درحال‌ضبط برنامه بود که یه خانم مکزیکی اینطوری خیلی رندوم اومد ماچش کرد و رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/23255" target="_blank">📅 13:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23254">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N87rOJcDp-EuuU3y1AR8KjTJf25R8TH7yysKbE34OqDlph9LZXLCmzqMGNgop4poIk4pB81pctBuANpEZWJaCxZeTP8lfypEyXT3YZbzXgaoEfkrGay-dv0hSrhxWmiWvmf_e41etzF1A08iO8beDTJobvclSIBUF8blcouIvbFMgyIR-nAu-pW5dlYgQLGgssPJpTUM1ndzN0ftICuxVmMXSmzrHCc_m7Q4scjx_e9tHdCgLYGNuawXBNdnZDWhpifdFE-0w8IBaPfYGPYoWzZUkqZe1rgrfCE-cQitvlc6930bZ65NZlw7WXsIrn51dtiJcwp9WFnNTauapOkPTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ در صورت تاییدیه مایکل کریک؛ مارکوس رشفورد قراردادش رو با منچستر یونایتد تا سال2032 رسماتمدید خواهد کرد و درجمع شیاطین سرخ برای فصل آینده رقابت‌ها باقی خواهد ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/23254" target="_blank">📅 13:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23253">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AdiQl-eXWKbq1EQOb3M37iK6cfoyjRlQrR8-2Sg6P6eNigTTepsd_jhivf_abff8XOsOSD5j2HLgAjf_5MF0O07tuUfkG3e87TGOy9yXeIh3vI3Hy4v93kYc67rQCde_WoBbXP-UnuQWyJec0yASHv-dwwdApBiFy36i8McFEfjVV921KWTQg9WpNuke5TQM6rKqPeHhIhMKgmy8oBhVAjNOu9tBbhATAOk0AW5GDZ6RKfKb24lPVkN7eqB7PaZUhNkJNXa85z18xeOA5wVle-6m4xpUi--ZukLLRLPz4nj8bc_-1HoCSOFpluqMRSr4AhRNdjccM4dnH8_hTqj3Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باشگاه تراکتور در روزهای گذشته علاوه بر تمدید قرار داد دانیال اسماعیلی‌ فر؛ قرارداد خلیل زاده به مدت یک‌ فصل و قرار داد محمد نادری رو به مدت دو فصل با پرشورها تمدید کرده‌است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/23253" target="_blank">📅 12:45 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23252">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d91e6763c.mp4?token=uz-BqI5VW7qrT4YbXAgy1WPhGTRdx1Cge48YY5thydDidLdT_2zEfDLQGFBNVXTMTt-fYCphr6enYza74HFQxOxSomqh2B1lJLZMH1KCYj7esvqm51rhFG9m4owXLgGKw6yGw7gexzEBlgBKzoyJxgvJA6-2kEVqH5qI-Mfll3JPQg1mnVQg9a3K75XwKt_60QoIShEpDYCBGfdyOxCeTQs9WpZI9uWQjpht0_NhvPslSUB1KmlyeWRes-_Jfq9tIVm4lWXnRFPy__WdcZKhXjlpCMWbm5rbT8WiIGdO9VokKatHxmSdq3rTDH4kjPOjHdQ9e4R-anmqQ_sU0rFZjoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d91e6763c.mp4?token=uz-BqI5VW7qrT4YbXAgy1WPhGTRdx1Cge48YY5thydDidLdT_2zEfDLQGFBNVXTMTt-fYCphr6enYza74HFQxOxSomqh2B1lJLZMH1KCYj7esvqm51rhFG9m4owXLgGKw6yGw7gexzEBlgBKzoyJxgvJA6-2kEVqH5qI-Mfll3JPQg1mnVQg9a3K75XwKt_60QoIShEpDYCBGfdyOxCeTQs9WpZI9uWQjpht0_NhvPslSUB1KmlyeWRes-_Jfq9tIVm4lWXnRFPy__WdcZKhXjlpCMWbm5rbT8WiIGdO9VokKatHxmSdq3rTDH4kjPOjHdQ9e4R-anmqQ_sU0rFZjoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات
|
هایلایتی‌کوتاه از عملکرد درخشان الیوت‌اندرسون هافبک 23 ساله انگلیسی که به زودی قراره به باشگاه منچسترسیتی بپیونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/23252" target="_blank">📅 12:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23251">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y2LhOGYB5r1Hy54Uv7rHgavWF-DjSivvdkaRKADGpbGaxx5xMhxhvA1MbCKVnXCfFG49I_p8IYlRZTvOEv3yos9e4fFdnVgaWSybp9Zz0mk-AF6PjfSgU4NbyaNxqty4noiIlsXJh-0DZyaZma4VMO7VIkWNzNoqA1yvbsIbT1a7l5-vsT8KEAndnIPUxWeaYWrqXQiIlRwqNrvGiR-tm9XgyPD1jk2sp1g0IAQS76HZSntoevpBZ24aKn-2MfBaxZ_V_jZ5yrt1odAKsyLEw2Mgv6m8z4mHJ-x5TigMbURaiE0Md025SHE5kk_rf0SS35u5ZDPDmK7Wz0K524J_AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
خوزه‌فلیکس‌دیاز: یوشکو گواردیول امروز در تماس بامدیران‌منچسترسیتی اعلام کرده که از باشگاه رئال مادرید آفر دریافت کرده و قصد داره بعد از جام جهانی به جمع شاگردان خوزه مورینیو اضافه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/23251" target="_blank">📅 12:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23250">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QYO7ZJvedalA8xSuL86ShAQjSeMczKSJ2dYaWTjB8fUlY1iG7Rl75Tmmozot_6JbJB3hDIA-viwbGenYcLwE5hb6Q5rBlYP1JpIM_GDY8Mu5mLH4FLm-fTUH6FzJzSufnBuEs32mfIXNgt93DUQQIo8G_BKciUnYQer8UUZF7rqBHMJCYMvHYzwF1b5wvTnX64qJJfPOLQDL8JLPdMTSHhFSklBmj6W5aBg2BQIIvRJlw-EEijN_cnZ0sGlChyuddA4bSmHmtV0TRXU0TiBFavk-onjVWOiaCw10yB6hQ3IpNGzUt7gqfMZZHd1ANMptEYtdmHJ74mgWqgqAkZO9IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری #اختصاصی_پرشیانا؛پیرو اخبار روزهای اخیر پرشیانا؛ فیفا روزهای‌آینده پنجره نقل و انتقالات تابستانی‌باشگاه‌استقلال بزودی باز خواهدکرد و آبی‌ها قادر خواهندبود تا بازیکنان مدنظر خود را جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23250" target="_blank">📅 11:58 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23249">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LyxHI-ajUH3sGl32xF_-P1Hs1xrOdfk0x9g0eyKmWXeZ4nvuLrxuLLXUg-6StI514vl2e2Hul7m8xVRdJEqfpKSh_lyAX691xbJubBB0zpXghw-GZTUPUtjGISQwVGzfWpVPRmI2_YRS7omOtIWjV8hrttuDR68DRwD1kJzXSXIB-dgWX6AQfAe3prPn9ndx4HNG5Nb6C2vWil-W30XA5J-DgPkPY2TeG1XM3tFyXkwJxIyIEkCbU7NTdUKtC5bIWwKhqfCmFpEfb3eF7T60gLUJ0ZnIE1AbD-9NZT-xkJb3U6vH1-HPpWGuI3ensma19SHfdApNMiUPZxin0NZYiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
کنفدراسیون فوتبال آسیا AFC نمایندگان ایران در رقابت‌ های آسیایی را اعلام کرد که استقلال و تراکتور در لیگ نخبگان آسیا و گل‌ گهر در لیگ قهرمانان آسیا 2 شرکت می‌کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23249" target="_blank">📅 11:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23248">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/733942b449.mp4?token=YcLuK6Nz_nF2rZX3urGQDkdDSRByDM-GnOInNZqY8-VMUmZUtzz3rBUm7d7O_COC3YCdWKET4qZ8XF0y1X9A9PEcYoqnsTNjpqVf8PbWy3m-lvGrYtJ63B_SdNaFbZ1Kz2FOrLi2fonLPjLIuYzdA1KBAT6KUfinqNg32xNSaUmHBHiH4cszhvqqMQ8Pllb4RthQ5v-6z-ZuejZ1G2Pts0ZTJSgZ4hdso9FnBKDjjttU-QcFwtJYqbgOBUxdCO46g3WyJmtDp-2JTeYcBkt96RZHRzrsrSc2_QIg9kHXqP7QC-rfOZ2kY-xxLG3PsXmM75-NqNUcdur7piYrt_lTXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/733942b449.mp4?token=YcLuK6Nz_nF2rZX3urGQDkdDSRByDM-GnOInNZqY8-VMUmZUtzz3rBUm7d7O_COC3YCdWKET4qZ8XF0y1X9A9PEcYoqnsTNjpqVf8PbWy3m-lvGrYtJ63B_SdNaFbZ1Kz2FOrLi2fonLPjLIuYzdA1KBAT6KUfinqNg32xNSaUmHBHiH4cszhvqqMQ8Pllb4RthQ5v-6z-ZuejZ1G2Pts0ZTJSgZ4hdso9FnBKDjjttU-QcFwtJYqbgOBUxdCO46g3WyJmtDp-2JTeYcBkt96RZHRzrsrSc2_QIg9kHXqP7QC-rfOZ2kY-xxLG3PsXmM75-NqNUcdur7piYrt_lTXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
هفته اول جام جهانی 2026؛ پیروزی راحت و ارزش مند مکزیکی‌ ها در دیدار افتتاحیه جام جهانی و گرفتن انتقام مسابقه جام 2010
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/23248" target="_blank">📅 11:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23247">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b63a3e61cf.mp4?token=bPtlSFsLLnm4WHDeUuhyvk9BY45ZiYvcU-hN_vXdJ5HnnjKT0tM26pUYVx5GLuUPABo401O_gdS_9fN8xXzswgpCT7WfdPomlz8-AvPjrdaKxWPiIIP7fkHJm1rWhkU4Mnr7GHxYIapM0f_b_tsjboMAHyJKVzsIiW50Qt27tBI0W-GN3EIWKl_-ObuZidCLmdC_-gqZE3vhdypzm5sCHi2myQ82EdfX21ZrSOdkJ3cqQUG_zzs1xKauhfx_RGlzj-q-UYzydWqJn-ka0Unm0-PcYLNt3w4SBDNaYTsFKuh0leXsO7N7qLFxUQmzKoraB7LpiHvEQFVcvsTNdp85pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b63a3e61cf.mp4?token=bPtlSFsLLnm4WHDeUuhyvk9BY45ZiYvcU-hN_vXdJ5HnnjKT0tM26pUYVx5GLuUPABo401O_gdS_9fN8xXzswgpCT7WfdPomlz8-AvPjrdaKxWPiIIP7fkHJm1rWhkU4Mnr7GHxYIapM0f_b_tsjboMAHyJKVzsIiW50Qt27tBI0W-GN3EIWKl_-ObuZidCLmdC_-gqZE3vhdypzm5sCHi2myQ82EdfX21ZrSOdkJ3cqQUG_zzs1xKauhfx_RGlzj-q-UYzydWqJn-ka0Unm0-PcYLNt3w4SBDNaYTsFKuh0leXsO7N7qLFxUQmzKoraB7LpiHvEQFVcvsTNdp85pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
گل‌های‌دیداربامداد امروز دوتیم‌ملی جمهوری چک
🆚
کره جنوبی در هفته اول رقابت های جام جهانی
‼️
هوانگ این‌بئوم با ثبت یک گل و پاس گل و آمار بیشترین تعداد لمس توپ در زمین به عنوان بهترین بازیکن دیدار کره
🆚
جمهوری چک انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/23247" target="_blank">📅 10:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23246">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7eeacd442c.mp4?token=OdNaoVarf6AFdAoosyd2gx8cefMZWEMe5xLX1g3iVrFwM4mbnqq-NLcX3qGBup836kBTZPxShygF-WbHU5-L3PLFm3wPRpx8J86U_mojLjzDEFMDs4XMJ5vAxmQat3z83bc1hdkWww4_QNsXeaiy8U0vEcInkRd2_5y3RpXSK05bIYDvStqZ9QIgghq27XHSZnig2fZDc162i-5VvMa5AGAE5TiXYLTJQ-ymhYhgp17P9rB7-cFkWU6RrP9AfSOLboyBhhbJ9vdrhn9WcVxYXOHghD1T33mkS5DVArDfCqSzQdXiMadS_UGBELLu4G30cMYYWzodrGf_wUCbKJWs7lKe9iTYX_orD2iFOAjNrZFCfR4V4MKRgtK7i2oEHeIgT4y8T0z1sozC3R-634ep7_onNE7K1M-QGhsEtIydOshJkpBVEksRxkdTH8okTWTLyG_6ULxntzXwcjWuepaia8jcQc7TtsaR_HrG82M9qKw02cblRyMEIIsF5nzeIk_zgYC4-0jqfLl3ER4SwRTeXETREuSZ_5LtCxftIloOCWT-bIGDxfwVSuwlGB5vOeB5CwAuDR6N_8vAxD_q0HuC5pmR_flNETORhiFzgAkcCQZfohp865R6G9U9v4EnzfcG0Pn-MoXfLEmlTRr9Ih8mu1fT3bAzMgMlxJgsHBNkCng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7eeacd442c.mp4?token=OdNaoVarf6AFdAoosyd2gx8cefMZWEMe5xLX1g3iVrFwM4mbnqq-NLcX3qGBup836kBTZPxShygF-WbHU5-L3PLFm3wPRpx8J86U_mojLjzDEFMDs4XMJ5vAxmQat3z83bc1hdkWww4_QNsXeaiy8U0vEcInkRd2_5y3RpXSK05bIYDvStqZ9QIgghq27XHSZnig2fZDc162i-5VvMa5AGAE5TiXYLTJQ-ymhYhgp17P9rB7-cFkWU6RrP9AfSOLboyBhhbJ9vdrhn9WcVxYXOHghD1T33mkS5DVArDfCqSzQdXiMadS_UGBELLu4G30cMYYWzodrGf_wUCbKJWs7lKe9iTYX_orD2iFOAjNrZFCfR4V4MKRgtK7i2oEHeIgT4y8T0z1sozC3R-634ep7_onNE7K1M-QGhsEtIydOshJkpBVEksRxkdTH8okTWTLyG_6ULxntzXwcjWuepaia8jcQc7TtsaR_HrG82M9qKw02cblRyMEIIsF5nzeIk_zgYC4-0jqfLl3ER4SwRTeXETREuSZ_5LtCxftIloOCWT-bIGDxfwVSuwlGB5vOeB5CwAuDR6N_8vAxD_q0HuC5pmR_flNETORhiFzgAkcCQZfohp865R6G9U9v4EnzfcG0Pn-MoXfLEmlTRr9Ih8mu1fT3bAzMgMlxJgsHBNkCng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مصاحبه‌جالب‌ابوطالب‌حسینی‌باهوادار معروف و روشن دل باشگاه پرسپولیس که اون جمله معروف و تاریخی رو خطاب به علی پروین به زبان آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23246" target="_blank">📅 10:42 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23245">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U1cmAjlDg1kofcIC_AvvsY4VRoFrjZJ9Y5jypcgf6tpBVEXsv_qwCjfu_9ZNwyzeue6lk1dF2enBq8Hdu8TAaOIvOgRfQ9F313XwTID-3HFv88fzUiEx3D1jZeTlNFvUUDMpWSzNmLCDyyyP350PERFHPX31Wjk-wNggSAf6DEnFRXYptbnyhBJ2IjtXvLDeFumdjPzbPZijfVoMo3RvBHJbVoyFDBu1gJMzZ7cNi2ut2xi6nbnqsLQJq8Y5DXGZlfcoZFdTTb6jKRK8H_cbph1sqVLRNCHWOMp_fIgvkNmwq2mZn209eaPJnJItxruwIgewrs9Yo4-ErR_ButMcBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💣
🔴
#اختصاصی_پرشیانا #فوری؛ رونمایی رسمی از لیست بازیکنان مدنظر اوسمار ویرا برای فصل‌آینده‌پرسپولیس؛ لازم به گفتن است برای هر پست نام دو بازیکن رو به مدیریت باشگاه داده تا اقدام لازگ برای جذب یکیشون انجام شود.
🔴
محمد امین حزباوی و دانیال ایری؛ دفاع وسط.
🔴
آریایوسفی…</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/23245" target="_blank">📅 10:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23244">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5655edf133.mp4?token=AXZIaKHK9qjAKyPPa5otR8Hy1VGOwGzH2Iqzj50JDS2FIQEU8FpnPVTI2tZ_3rQ9aYf9tVJld1SYfgHibhusjm9OV0kqQq60s6dYf84MG45kOYV4nzn90TLU67WysUUs_W1EnElt8c5YavzfT4XZ6BtLdNgd4K0zpmyCoJd7YRRcpkQ-k7pNduODCdD07czUfsjwvOMhgi33FCxGOUVsJndIwAHhnG5jNnr-a_hjjkQSlfqzO8L15jpRYxoKL_RibSi9eR6QsfwWIuAEflLfY-k7HoArh6RohIIgdF_v_dmBa-hZMEJdpYmq-gJ93wDoc-rE_n_R0Sll-gbGf3euHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5655edf133.mp4?token=AXZIaKHK9qjAKyPPa5otR8Hy1VGOwGzH2Iqzj50JDS2FIQEU8FpnPVTI2tZ_3rQ9aYf9tVJld1SYfgHibhusjm9OV0kqQq60s6dYf84MG45kOYV4nzn90TLU67WysUUs_W1EnElt8c5YavzfT4XZ6BtLdNgd4K0zpmyCoJd7YRRcpkQ-k7pNduODCdD07czUfsjwvOMhgi33FCxGOUVsJndIwAHhnG5jNnr-a_hjjkQSlfqzO8L15jpRYxoKL_RibSi9eR6QsfwWIuAEflLfY-k7HoArh6RohIIgdF_v_dmBa-hZMEJdpYmq-gJ93wDoc-rE_n_R0Sll-gbGf3euHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
زلاتان:
«مسی یا رونالدو؟ مسی بعد از بردن جام جهانی حجت رو تموم کرد.»مسی یا رونالدو؟ زلاتان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/23244" target="_blank">📅 10:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23243">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VDqg-VUdIl2DDluDoRrRPQgBSePSN9kLDxZtj-jWQK0Qmf3QJ1HhHPWYRMolfFH4G0zIHi5PJKilOXauahlzgVOof3-Ruq0jLBOiwWZo3ow9-mvxACcY7eLNUQuj4yzI2RqIwBfXuETKaHEbuerim6_SRnp7ta9TnX37eIt5XW02KPdIWuyl__j56h0HoDH6Lu9JFZpIczghaFYWGTmYdaT_m1L7Ll74dfRx3GIwdY75-yFEUltnikpSu7OxehcUDWOiV22369EDtMSWLJwH1sN1tswLZEQL5b-tl96R1bhM4KivfynBDdwLM_Xk5UA7UrSI8aqbVt4JndyWwOXwCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
هدیه‌ی ویژه برای کابران جدید
🎁
اولین واریزتو انجام بده و
0️⃣
0️⃣
2️⃣
🔣
بونوس اضافه بگیر
💰
⚡️
فرصت تکرارنشدنی به مناسبت افتتاحیه
⚡️
🔴
تا سقف ۳ میلیون تومان
🔴
⌛
فقط برای مدت محدود
💣
بالاترین بونوس‌ها فقط در سایت وینرو
🗣️
امکانات ویژه‌ی وینرو
📺
تلویزیون لایو برای پوشش بازی ها
🛍
پیش‌بینی مسابقات با ضرایب رقابتی
🎇
بونوس‌های متنوع و جوایز ویژه
🔝
تجربه‌ای سریع، متفاوت و حرفه‌ای
🎰
همین الان وارد شو و با اولین شارژ تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگیر
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
📱
کانال اخبار و هدایــا ea22
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/23243" target="_blank">📅 10:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23242">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0f934920a.mp4?token=GfozIIfmal5rRI3DixKBaURi9oNCQ83AQbfs2Kc6--6I_kXDLU9DMKzdROdsl08YSQFLyqsh0jdph2sN2LqvXrHyCqtxEGB9Zc4pndW31sl2q4WeiaJifZpY3DureMeu6iS8UQp7eVgtoFdoNNuBCEal51HAsFWIPVa8DvXR4FexT1kSb4KdMZ8H-YQws_bWH0FEquCCbbpDgNjenbM5cK9zt6OETVRtMjWCpHEhSYUofSUvZVYMn880jloaFZe1yWAIv4g8rY6lNb8Eko4SWe9JTpKQOGCPOBF62IzFIA8P0r5eiJya0WuN46a8NbAtX2QkRrUEEmIhhF65IJzjUamshJZCudcnIMP6hkAgvMWWT4c9mFbj6gGO39BGHkbCvtgdCpjgYc9VT11UsG6Y6bdsjd4eRJmbc-4TX5GSDN3DUlB5_6O-QAxrMQYx3ePy9Bepufh-60QbOR2zREPLfXskfWQr1RIC4XvjBfUrHRvkapjvgyMv4uXXj_4mjMPsACQNcgYNkxtWNIC28y46kFL5ohzMMnhEeEGWV7p5gpas5wFBFbBEl88kL_gOaBcBqYGjdpS6bTWzDBCIHBzEGcxgANBegHCZKWh4flbvawJssiBkewLeg8vkOxo-WXG2nJOTPv2d4iYdJxhccbp27unBuxgve4zcS2BxyJNq0aY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0f934920a.mp4?token=GfozIIfmal5rRI3DixKBaURi9oNCQ83AQbfs2Kc6--6I_kXDLU9DMKzdROdsl08YSQFLyqsh0jdph2sN2LqvXrHyCqtxEGB9Zc4pndW31sl2q4WeiaJifZpY3DureMeu6iS8UQp7eVgtoFdoNNuBCEal51HAsFWIPVa8DvXR4FexT1kSb4KdMZ8H-YQws_bWH0FEquCCbbpDgNjenbM5cK9zt6OETVRtMjWCpHEhSYUofSUvZVYMn880jloaFZe1yWAIv4g8rY6lNb8Eko4SWe9JTpKQOGCPOBF62IzFIA8P0r5eiJya0WuN46a8NbAtX2QkRrUEEmIhhF65IJzjUamshJZCudcnIMP6hkAgvMWWT4c9mFbj6gGO39BGHkbCvtgdCpjgYc9VT11UsG6Y6bdsjd4eRJmbc-4TX5GSDN3DUlB5_6O-QAxrMQYx3ePy9Bepufh-60QbOR2zREPLfXskfWQr1RIC4XvjBfUrHRvkapjvgyMv4uXXj_4mjMPsACQNcgYNkxtWNIC28y46kFL5ohzMMnhEeEGWV7p5gpas5wFBFbBEl88kL_gOaBcBqYGjdpS6bTWzDBCIHBzEGcxgANBegHCZKWh4flbvawJssiBkewLeg8vkOxo-WXG2nJOTPv2d4iYdJxhccbp27unBuxgve4zcS2BxyJNq0aY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌جالب‌از برخی‌بازی‌هایی‌که تیم‌های بزرگ تحقیر شدن و شکست سنگینی رو متحمل شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/23242" target="_blank">📅 09:55 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23241">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b35493e0c7.mp4?token=q9qzTJCk-l8wH2LUxkWs7RndzO7oDkOwJ87BPb5Yt06cFE_pD48JxOQyZOIt-ucemiAZ_bEyR1nZgvk6gy5DmPNocMkHNvDDwng1Zb0eBA6mP06ilMOLkTj-KNC8hyogXKCuoIMnC2J2giogYJHxciQglOoRToa9N_BiAAJGvjbTmAgNGWDf6KCFr_PkTh8PiDbV15-eEjy07IZMTLkeoa0fAjUXdcksIEPl8no7nIIrK8EbxZJsnrc4pYDmbfd354-MiOjJZ3PBj41g5SubQTR_lZXEWrU-kPHSyFtnsY1OH5d09XodcRJND_Ff-6vSnQXrlDkCs1OncKqwjvmG2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b35493e0c7.mp4?token=q9qzTJCk-l8wH2LUxkWs7RndzO7oDkOwJ87BPb5Yt06cFE_pD48JxOQyZOIt-ucemiAZ_bEyR1nZgvk6gy5DmPNocMkHNvDDwng1Zb0eBA6mP06ilMOLkTj-KNC8hyogXKCuoIMnC2J2giogYJHxciQglOoRToa9N_BiAAJGvjbTmAgNGWDf6KCFr_PkTh8PiDbV15-eEjy07IZMTLkeoa0fAjUXdcksIEPl8no7nIIrK8EbxZJsnrc4pYDmbfd354-MiOjJZ3PBj41g5SubQTR_lZXEWrU-kPHSyFtnsY1OH5d09XodcRJND_Ff-6vSnQXrlDkCs1OncKqwjvmG2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
مدعیان‌اصلی قهرمانی در رقابت‌های جام جهانی از نگاه کاوه رضایی و جواد نکونام؛ چقدر قدرت بیان کاوه خوبه. چقدر خوب و سنجیده حرف میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/23241" target="_blank">📅 09:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23240">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nGSxQf2IOvnNG0JXgdLssFC4hOC7eBCKMciWyUSYo6Yqh2Gmh8h006RPEwfpAo2wmN2q0kq_RCVKsJ67PuZPR3eNVAIDjaZMdm95aMEP2kC02mLbrfz0xogP6U6o4md18U1bVwVd2e8vfrRXJl2FK8V3-tzhCaDUSSku45m2IBmxe_R_sZg5y7HtcCRjTEfDxFBhWdSHanCZ2RtinYROsR_MiiFb5lDpOvxkdMzd_zCVLhJcpdiKLrkvfslW6trIBjcrltNGvjM9IpSrZLsT6veCTYYBnvgF5ogQAXKg8Tlt_A-pq5Nw805qrN5KSOLKE9TDpvNIQ6PSSNDp02BrxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
علی‌تاجرنیا رئیس‌هیات‌مدیره باشگاه استقلال: باشگاه مطالبات یاسر آسانی رو فراهم کرده و بزودی به او پرداخت خواهیم کرد. اجازه جدایی به همچین بازیکن‌‌ارزشمندی رونخواهیم‌داد. یاسر آسانی و منیر الحدادی فصل بعد نیز در تیم استقلال خواهند بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/23240" target="_blank">📅 09:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23238">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57efe2f2e6.mp4?token=BQDYjNFnD8amA2gLlm7IM5HMuXsUA5LahTqoI6gSHi-qLUpyHJJNwBwAQGEDzr6ikCi7BwlGlwT9Wlyd-RE-voy4tFhyVg-n8yAzflObTCjOtdLL5D6-Bh0OQgQwhy2hAcDAVVEakwZ7hNbAIWZUWAkkXUxAMLZsPstd4QRW-UrVYdzOUTq921Yw8jFRL05i1XB5FcMnjB0xf60dQxsV7cPZgqmP9YFViHzyTjvjgQY4UBRyQzQvXwBntL2DiNM79lkE6ounfk0wy0bSW8b8Ipf9EmYGwKXTkYWeh1N8iw_Xbve3YKNOBQJay_tQoUOO6aXXkU2dl2W_2tDaqhY7vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57efe2f2e6.mp4?token=BQDYjNFnD8amA2gLlm7IM5HMuXsUA5LahTqoI6gSHi-qLUpyHJJNwBwAQGEDzr6ikCi7BwlGlwT9Wlyd-RE-voy4tFhyVg-n8yAzflObTCjOtdLL5D6-Bh0OQgQwhy2hAcDAVVEakwZ7hNbAIWZUWAkkXUxAMLZsPstd4QRW-UrVYdzOUTq921Yw8jFRL05i1XB5FcMnjB0xf60dQxsV7cPZgqmP9YFViHzyTjvjgQY4UBRyQzQvXwBntL2DiNM79lkE6ounfk0wy0bSW8b8Ipf9EmYGwKXTkYWeh1N8iw_Xbve3YKNOBQJay_tQoUOO6aXXkU2dl2W_2tDaqhY7vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
هنگ کردن عادل از مصاحبه اخیر امیر قلعه نویی سرمربی ایران ازسخت‌تربودن جام جهانی 48 تیمی نسبت به 32 تیمی: واقعا نمیفهممش. یا من خنگم که نمیفهمم اون چی میگه یا قلعه نویی تعطیله و ندونسته که چی داره میگه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/23238" target="_blank">📅 08:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23237">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FR0GWAq-PO5hkP4gI4JWWeKdQWYGW4zCEXLPdXiu9SHQupwh7oRJHLzWwk76Z0E8H019wYHZcFNPFanB2I1FZRKaN8PnAiaqnT-kOsR34XOlNIhDBA765wv9pBGvBRlbmg8ZX-eQaBcE4d2epXC5f-VVz0RGIoMdrLOFERKcoV7tPOS2iZPaA6Gkvu9fDYmdLFIThKe0GC8LEx0xszEAnS8PD_0QrTYoGzFzzpAtBvm4pr2UvhBlKM6v4NwdFeNH5m5mcRV6xWr-3I6D8TYRjfaeBtdsvrLwLq36qL6KlsfxGcwbt5jvdxspZbwe8p4Td4mJW56vfeOh5lcePyKWdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇷
کره‌جنوبی برای سومین‌بار متوالی در ادوار جام جهانی حریفان اروپایی راشکست داد تا به این شکل کار خود در جام جهانی 2026 را آغاز کند.
🔴
جام جهانی 2018؛ دو بر صفر مقابل آلمان
🔴
جام جهانی 2022؛ دو بر یک مقابل پرتغال
🔴
جام‌جهانی 2026؛ دو بر یک‌مقابل جمهوری چک
⚪️
…</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/23237" target="_blank">📅 08:13 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23236">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇰🇷
کره‌جنوبی برای سومین‌بار متوالی در ادوار جام جهانی حریفان اروپایی راشکست داد تا به این شکل کار خود در جام جهانی 2026 را آغاز کند.
🔴
جام جهانی 2018؛ دو بر صفر مقابل آلمان
🔴
جام جهانی 2022؛ دو بر یک مقابل پرتغال
🔴
جام‌جهانی 2026؛ دو بر یک‌مقابل جمهوری چک
⚪️
…</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/23236" target="_blank">📅 08:02 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23235">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/So98jcIYE0VIxRn5K70JcJKw1gh8C7gB7a8qUzH--KLGUIKv6kENvCnqw3bkRJKpATF9zAg472XVKGCfF6OW_Dc0X7rLaaXXpu8TQ78_-yDdW_pfGBzDxC6HGJzJJL0Q_7coWU6CgkrMqB_8y4yHdSpJBy9VolijQDyakOiLbJZDkBHj-4ExBAr3niTjFe6pJ6pPqUGZikHcT_gRbTs8x8bERDsDovRu41wW4x09IU3wLxYbIb1ASREFvPQHHefkocxkvJ08kRGwumEkkEkZMI1U0Di6YJwQkY8C3-xcnUyvVoz-K-WTqRlSU8p2yw_y-As5DvsdLe_dnYKVWbHsUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇷
کره‌جنوبی برای سومین‌بار متوالی در ادوار جام جهانی حریفان اروپایی راشکست داد تا به این شکل کار خود در جام جهانی 2026 را آغاز کند.
🔴
جام جهانی 2018؛ دو بر صفر مقابل آلمان
🔴
جام جهانی 2022؛ دو بر یک مقابل پرتغال
🔴
جام‌جهانی 2026؛ دو بر یک‌مقابل جمهوری چک
⚪️
…</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/23235" target="_blank">📅 07:52 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23234">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bx1lTHUYlD8lfDWAXNtaqiyiJJXLuccnnylBCnQJtQmJnnpDfRDlFanP84THSMG2D0G0w1WtVJ0e9-Es17QvxeXK9LTVqujd3z6cnTazOXkQSMIV4M_7LQ9wz1Eylz6Twrbrjf6oYxanDDcP4__585gjP_XVYW-WCS6vMJwQapDrFpuUef0L_y7l7NErZz9Lxu7WYg14mS-D7hbcD6NXuY1EdaXOPgFBXlNgvlqQ7Pv5X-YGknDqRs_wF9RdubNBkpc0R0C6rzRQTKtS5aWJpx4-oturPCsavJ8-VDOS9gtESv8qtiMHioqNvdHNAFPg3h5fXyua82YCa3nz09Tqdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇷
کره‌جنوبی برای سومین‌بار متوالی در ادوار جام جهانی حریفان اروپایی راشکست داد تا به این شکل کار خود در جام جهانی 2026 را آغاز کند.
🔴
جام جهانی 2018؛ دو بر صفر مقابل آلمان
🔴
جام جهانی 2022؛ دو بر یک مقابل پرتغال
🔴
جام‌جهانی 2026؛ دو بر یک‌مقابل جمهوری چک
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/23234" target="_blank">📅 07:46 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23233">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d61b75a83.mp4?token=Yy61_RpfQdWBjYDAxpIG0SX609nmDHo8sloZdZoA6Gap14XOCY7ercZQhoEk1McTo5Fi8s8iXy4cVf6qxDxIxBKPUfLIJSR35t_gcFrgRNs5yaTMd2RUZNZkoSHIGL0UojEzhe7yKo97UOt4MGepYB1nDvLsy1ZMZtQbRYsPBNKMfaXNLTkmVCMB9htFYeNSVuMBT5PutH4l3IQJx5cO-tccJeZ5CA5QmLhRhKXl8onytLu5yn79L8ujYv3Ro7cnrhwlJ8ZGzzhz3r0DNtYJg_36cJwN6UX4oztUI7x7e8PUfx2fpFBvMg1p2K0Gny87sMyV9H2y_11xQn-KzG4ICA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d61b75a83.mp4?token=Yy61_RpfQdWBjYDAxpIG0SX609nmDHo8sloZdZoA6Gap14XOCY7ercZQhoEk1McTo5Fi8s8iXy4cVf6qxDxIxBKPUfLIJSR35t_gcFrgRNs5yaTMd2RUZNZkoSHIGL0UojEzhe7yKo97UOt4MGepYB1nDvLsy1ZMZtQbRYsPBNKMfaXNLTkmVCMB9htFYeNSVuMBT5PutH4l3IQJx5cO-tccJeZ5CA5QmLhRhKXl8onytLu5yn79L8ujYv3Ro7cnrhwlJ8ZGzzhz3r0DNtYJg_36cJwN6UX4oztUI7x7e8PUfx2fpFBvMg1p2K0Gny87sMyV9H2y_11xQn-KzG4ICA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته دوم لیگ ملت‌های والیبال؛ دومین شکست تلخ شاگردان روبرتو پیاتزا مقابل بلغارستانی‌ها
🏐
ایران
0️⃣
-
3️⃣
بلغارستان
🇧🇬
25|25|25
🇮🇷
23|19|21
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/23233" target="_blank">📅 01:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23232">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">⚽️
👤
ویدیوکامل قسمت‌اول ویژه برنامه عادل برای جام جهانی باحضور پائولو دیبالا، جواد نکونام و کاوه رضایی برای‌دوستانیکه‌نرسیدند کامل ببینن برنامه رو‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/23232" target="_blank">📅 01:46 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23231">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caf2ee1fc9.mp4?token=qBXx9XH93PsX4uHzdpfVNmwSjat7v_t1tfzDQ9Ke6IF4gnwYwEOZ-bm8-xExq8t0j16iTKl9WYwXfOmyK87dSjEwCERiTdZkx3BylR0gZ8apBlCnQqPuqHzCmx5VfEqkUuDaGYJfwQwTx8-MHdg7pGGodAmqQrUkzaJMnkaCOjX3tWi6miwkMIdWBoGUE3h0xWGeQvnvFHB_BErMBUTANE2qJePCxHLfsEx7gOc9uFSDm3I67GytNSTNJDVny6TAmXA3V3mLQarY27Zhr-4_maX1S-3wZBzMbiJBdeGrFFCSyYjJhJ1I8sRFgEOBaEwNldSmxPt8rSSBUyjVVjT7AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caf2ee1fc9.mp4?token=qBXx9XH93PsX4uHzdpfVNmwSjat7v_t1tfzDQ9Ke6IF4gnwYwEOZ-bm8-xExq8t0j16iTKl9WYwXfOmyK87dSjEwCERiTdZkx3BylR0gZ8apBlCnQqPuqHzCmx5VfEqkUuDaGYJfwQwTx8-MHdg7pGGodAmqQrUkzaJMnkaCOjX3tWi6miwkMIdWBoGUE3h0xWGeQvnvFHB_BErMBUTANE2qJePCxHLfsEx7gOc9uFSDm3I67GytNSTNJDVny6TAmXA3V3mLQarY27Zhr-4_maX1S-3wZBzMbiJBdeGrFFCSyYjJhJ1I8sRFgEOBaEwNldSmxPt8rSSBUyjVVjT7AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
عادل‌فردوسی‌پورخطاب به دیبالا: تو ۲۵ـ۳۰ سالی که کار رسانه می کنم تا الان با ادم خوشتیپ و خوش رویی مثل تو مصاحبه نکردم! خیلی خوشکلییی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/23231" target="_blank">📅 01:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23229">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TwkDC-Q9ExZdmonTc_lDiCFO3U7F9Z72AMF-S4wPDTHsXpMpMYr2CL3r47f3FrGuzc5Xh9KQZ7xDVVijzOzTn4g2r1ydwmgHdRHpBKwBsBAyhfFB4sruc-OBPR3ZPdSa_QLMojfOVgDZnruiTuUAsy_kVBMQZO527myR-wYXBAhcWF_16TaqBfG9uX8r2NOJ7-s4JZVwyPA82OCNzUeNdGll31pKUgMZ0xy_okfEkbq0wlQuF7In5Lr9FQDO-mQMCPaFVgsHitnpHTubL6qNYNjpJg7OFHAEAqmpNu2PQNEt_YrSYfihmll10n8V12FV4a71IZw84w0J3HDgf9N89g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی؛اسپورت: تماس‌فوری‌خولیان آلوارز باسران‌تیم اتلتیکو: بندفسخ‌ قراردادم رو برای باشگاه بارسلونا فعال کنید. فصل بعد در اتلتیکو نمیمونم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/23229" target="_blank">📅 01:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23228">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hU4lFjXmiogG--0kYGNnUhud5NypXN_-LNBGH45ILnjBE_uaDYLrJUKr3k3ZVYCw4UkFHniInndYR1Ae5HJna2w1AUbCGW048sUj2xx6WTdtVkw1Ylg98LbmCCHKhGWR64mhkgjd8LIXsn0qjngpgxgJm48ULKTq7YFtDnAjjl9qz47QceNo6xf9OGO1P8JZO-dH7xez7djeeiOv889h6zoumjpM3D1u-MG0s4emlEO69WmNfJGxenYDWrnvM6ng1JTh2lg4b591mBRsfgJfowWmH6vanq2n2BmDs9lVEfaUleByxVWFP2081lMMZfoonKZj-O704XzJmd22sgem7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
روزدوم‌تورنمنت با برگزاری ادامه مراسم‌افتتاحیه‌جام در دوکشور کانادا و آمریکا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/23228" target="_blank">📅 01:22 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23227">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aV-9AhXZpLPsFHTxBykVMrnMBN3EoyClQvR9PgZugDnV-bEUGlMP4RGQ9jr9hsJHZds2Pq9TjSqrmul_FuPGugllnXr3OP_MSeds9yo6X7pVzjC8MSOHakm4gAmDSVlYYLoA9iAhYJG1mnlLI_jyZKvb6z_iGkiRLV5BFVBSMnyK_GVbSuyUmCMldGzErNHcNrMMUlSK24NylqDNiN3E_niM5hXkQ1wF04rtDWrm1LD7P8nux2hZt4mu14ACQLReUvW0FPTuFKmGifR3E9pxija46URkNBf-Gct83AYlXeZP4wY88QxMJqKWeaFhCVa1SvBJBEORyHMSruaNnmzZdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه‌تنها دیدارمهم ‌‌دیروز؛
استارت قوی مکزیکِ میزبان با غلبه بر آفریقای جنوبی در دیدار جنجالی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/23227" target="_blank">📅 01:22 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23225">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">▶️
قسمت‌اول‌برنامه‌فان‌جدید ابوطالب حسینی برای رقابت های جام جهانی 2026؛ عالیه حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/23225" target="_blank">📅 01:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23224">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c4bztQMxgGqgnHn-PrxrjIfv1usLXxzMIOvT21cPCFRiqSL3PIDjP3LSbZlfhT84koZwjoA_9KniDpfchs8GdVRIoWMspGA8BZ1hJPzCyB3mIrnA2hBPYdM9Xhao4gRIkO0wPyzi0jxL11Lkz-Tmz-FShIK7EXV-vdGvccUjw15E3ovYW7xkbqvYBe40unl1WXfPYgPzJ6M9wChaGM_5b57OoAJxo-WULLC8aUi5DG08v_cNVzccdeedxrbMrruDmYX_PH7PT4ccNS2RC9Riu7JZhg-jZfjSjNC_CJbtV7wK3wWJ3gQG8V-ubDenv2kw3khx2KCFVpv1fcxeKO2G2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛ با وعلام رومانو؛ برناردو سیلوا ستاره سابق منچستر سیتی با عقد قراردادی تا سال 2028 رسما به رئال مادرید پیوست و شاگرد مورینیو شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/23224" target="_blank">📅 01:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23222">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O9zftHH9ug7D8oGouiAiMUyD8w03u6HHuzWj7J5T1dVGOmcXDDAExDfiyWUh7tCzGVL34COw0JYumawMTVcYXlYzZNsGgAW8Udj1HaNDKavNR6lYNcqBF9AxqxWNNYYMV-Pij5zPeiKj6_UL7Q4y-ufqmn8hV-y7KuR44NQg-Smnt05LJOxPqMLDX-zUnnu_z2KSRyQiRIW-UWRLXAgrRW1mSHOsvDu8ORIM3ZAQ0Misq9lKXcZT6GWxQ8Y-3QXsjCMiFf3vo5yLfF4EeRcT7BKMtiGjdxG2qmgFcCc352WMmokNoJAzhwGQW0qqmyasQrmTIcM8hSFu1c5HCJkMFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ML9XXq27N-l3kof_lueT6tFItXoDfqTE-95_OJkn_1SDM79fA-8YUyRFTKi2yK8J-UuA7z7LsNG28oqiS-AwAbDPte-h4FsrzvxwIi4B2QKCef-OQZgnCSNjAlgHzLEaNR5yafDkGGl9hG_c6Y4KludUWPBG1RnYI57--4XuPt--9d4PVsKglHvMuCDuUdQIWNTOsX1VtMLS0m24N-F6jj2Q7bmVOlj11hrxOuqAvv1K_ZtH49alY9q0Ox3wcAfaJLYFmshvvvP5p-7gCBBIePIpYV13hMihhDhZi3XbhDnjp8On6i4VaTrVybhwEGHgJpA4KraDMr_UH-xpYYoSNA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛ آغاز تورنمنت جام جهانی 2026 بادیدارافتتاحیه مکزیک و آفریقای جنوبی
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/23222" target="_blank">📅 00:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23221">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G2pSEOGyVOomdRifAoDuvsnkIyM-_Zvr4q2NbsLiptgP0uHD55yGrwQZNRhYTYEVrpW-jwUVb-zm5afy9kvtvuQtMVzRTRTp2Q7dR4Q1sf_6wBkECtfB3FBx75ku_d3KzFsiIhY4c5U0fmAcIM2YFWQpSSiNJuMRfrfFMJoZnbazvuUUtDSpAtBIBWNiXdLTr9qzE1iB9KIzHa6tdab8w-XlB6qwp3xnqdCKLd28EJ3UUt3BmOfZvVlq6LFuFfrgR8zye2SI8uifev9iEdacavhEiqihiHHvC_KVgjcdNMXPaun1rFZAAczQkeCdm4ZGJnL_w6fLbatXFUaAWcIWyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حیف‌از این‌رالی‌دیدنی‌بازی‌بامداد ایران
🆚
برزیل؛ شاگردان روبرتو پیاتزا در نخستین گام لیگ ملت های والیبال بازی رو سه بر یک به برزیل واگذار کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/23221" target="_blank">📅 00:29 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23220">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YDmxyJFXZdVecQv0POFfrBcP2HAtclmtxIC5U9g-v7-d6yx_VNrV4qOipmz1ExH_ajLGdP8dOzwHZQ8z_BK_7uSEziujvAzlsnvGgEQWPRRP30h9nD8nXNPwkrFfBVRaZqtqbkMjLnPVz4_ypUli-voY7vY2DfmQtAYaeuNZspaOhtJsU1brnU_2-Pu5pVch7FoyNxCQbcN05KAdLOc7Rn-_vP7PXjioiY5meqLKAkUzEQed3N2ChzuuJj5qkU0oGd8a2-OOFSae_vaekJ3rB_CNBi2nCfkZ2sEJk8tAMFovHRFDiRBZbufDFtiikBbo-X7jJ0RtKygKGZVlnCPoDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛ مربی‌بدنسازباشگاه پرسپولیس ساعتی‌قبل به تهران رسید و از فردا در تمرینات سرخ پوشان شرکت خواهدکرد. اوسمار ویرا و کادرفنی‌اش نیز احتمال زیاد پنجشنبه وارد تهران خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/23220" target="_blank">📅 23:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23219">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v2vMm7xZWTo9igpAbUYZzEUut1p-WbNIPuGX7aWkE7meuJOunjJInNBmENWmTtrHpjN2AaPoN3w1M4JQ6Z0qktOpRqYmbl77nE4QHTAuxT8g8nkAFrlQSPr6gKNtnXFQP76POGs3-cwBo9rTRmfo0ojq3lfwOfhqGLpHbF-0fj1OW5c4mnt9oiDcVX5K6JLo2w4d1JuCBmdG_dk_418vCJNhJQEXNRF7OxOIUTRpeyWQMDxa2Y4zxH7E88HMSIouM7bhFzkMpdquoNNb5Srlc0BhjGb1W2orUuKLptEvBhLSWbXWwTyXK5DTq0mjt7KY0_yLWbqLcUkzWWtqKFHIMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی؛ رسانه‌های اسپانیایی: درصورتیکه باشگاه بارسلونا آفر 150 میلیون یورویی برای جذب خولیان آلوارز ارائه کنه مدیران تیم اتلتیکو با این آفر موافقت خواهند کرد و آلوارز رو خواهند فروخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/23219" target="_blank">📅 23:13 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23218">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BSgGHR-JZ9l-pNEQXnvPBBNESV525rLR8yZklnJnbpj_mTq0javCm0kU8qGLJ8US4Bk2suAaIgHunRvP1MIOxu5KlhYn2uhByVWGQvCRiIhN_SOtmHs9T3P3GNbbTNRrYzwTwoZnpA16Q_u57quMmsn_6jrzuqTH7MpXh1r9AKOqkthtI7UkPOSWpjDEMXTpCnhTW0eZNWe7gLYJgWbX0m--xB-Xx8FRKUcT3hNGnEnVKAFqxX_GHEANHDTekDWldtP4-ds62zNNr9JeU-wlaYwmmVK18KzrDs0ZPMLfBim9-0xw9b_4LuIv-jZtgufwoD5bHnIpvCeA8RrNoGpVng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
فرداشب و پس‌فرداشب‌ازلیست دقیق ورودی و خروجی‌هردوباشگاه‌پرسپولیس و استقلال رونمایی خواهیم کرد. اینکه‌این‌مدت کامل همه چی رو نگفتیم بخاطر این‌بودکه ویو کانال برگرده بروال طبق و همه رفقا آنلاین شن. فرداشب از لیست باشگاه پرسپولیس رونمایی میکنیم. پس‌فرداشب‌هم‌بازیکنانی‌که…</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/23218" target="_blank">📅 23:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23216">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IU2N1Naj3yNSsBF19KhcDKcorPmrMbZdMhqNgacNZ75fMmAcJZlucHlfAz1vxqt2GHcbsCQ0MjHyweNDYf0agoj6YJcs7EyjnxtKc3KO7ZcNtmIjARmgZpbN-pfsHO0N4oLu15VBkRHWeBiQ9zp30Yu_hwUfVAhu-m4lzFf2Sj3b93I-gT7clIT_Xp9U_MsBhb2pM5xFtQ7dEB6ACYNMQG09QyXPPr4It4eSpTqLjjF7DLjeCy9HF7_GmTeXIhvqf-m8OVu2jxETLf5WMbFOa2fjicLOcOyp2OcQ0YuQ-SdUfCVdzl4D6Rh_iWbWvYxpO7ha3M9aGD4fkPQoBd7XwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OG0UpomrJ2k40hVpTrLbVIAeGSqsrlvTnRwR1c1bm3Gsghz-pgXTZlcLM72AGomeFlivkL7tpx00RGcHNPzysynLuXXP0ojMhb5fTjoFK_Zi1y_8TtM_xQJGmhEmwfkGEzZsAkycHhRywqahfLZFO8Gwc6AAIcMCKBE-Vdpv2Qy_gDj68XzfhFejiWGprVkNrPIlI7m7k2kvxnAkTVE9MvC9P8UzfkrPSvqe-xTcsptSofRbZZHKct__vqxOB6FiXPzxyWQn1rWfZiUmaDzHsA7Rf075UUGVfguy3f5HBdN3YUIJyC0S3aLrSA6yzgW_Lrvq43NYGnv7XGt2Gg9mrw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
ویدیوکامل‌اجرای‌امشب شکیرا خواننده کلمبیایی معروف در مراسم افتتاحیه جام جهانی 2026
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/23216" target="_blank">📅 22:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23215">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sCKH9zHLfH4F9KEFkf3GNIbgxd_tWZ_wLBQapMN4ClmdWDL6y9xK2Bxao9xEJzkjY0QQx0yXzADmmncAvoMsu_aDf9wQuTm3koZrAlaVmcokXZsglFEuN94p6HXdzvkEInQ2vkaDMQikr1fONT_mvR3_NBPO-Purf7GkgD_hcaBpLO9HC261FAsafPGP377w4ClYzxLXHsEDwwILJMaIg13PoLse0-CGHZT9voLUn_QLHyTLdmw_lYWSeMTxTkjdwfzcGwGCRmTYEO0mO3NKZDe-uJhmmwS6EDKKA0Op1JN-8akBWtTkP_TSfvvdCz36_F8qqr-QawinnRVoaeGJKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇵🇹
#فوری؛‌ خوزه‌فلیکس‌دیاز: برناردو سیلوا ستاره 31 ساله تیم ملی پرتغال برای عقد قراردادی 3 ساله با تیم رئال مادرید با پرز به توافق نهایی رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/23215" target="_blank">📅 22:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23214">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6a0329db5.mp4?token=P4FrQY330b2BH4-ro0XTvrjr0tW_AzU3PMJNQ47A31oYdRcdrWKR__vKlRqIx_1Ve4rkW4YZrw2hYUNyRGwg118R5TPsnmbqZuswZwd8EkmzgSVt3R-RdkJ3xXY2z-VwTriZ1wf8gqMERxKuepN4Ebb2ew5vlbRpJEtDh928E-fT0conmuaFoxDjohQZZwDSYWjlDJTRxTfm0kVvGcmgslLmSmDenPhJNVZncj6Bbof_JMkzYTlHDWueKB88h6DppQO7pw-k8_FpyMKtQGCKAhHGOCgtILbrz3OlJ1rU6-2fNaDUwPMr2XqXs_v_fDqO8r5lnuLo-w5-XiC6lDXbtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6a0329db5.mp4?token=P4FrQY330b2BH4-ro0XTvrjr0tW_AzU3PMJNQ47A31oYdRcdrWKR__vKlRqIx_1Ve4rkW4YZrw2hYUNyRGwg118R5TPsnmbqZuswZwd8EkmzgSVt3R-RdkJ3xXY2z-VwTriZ1wf8gqMERxKuepN4Ebb2ew5vlbRpJEtDh928E-fT0conmuaFoxDjohQZZwDSYWjlDJTRxTfm0kVvGcmgslLmSmDenPhJNVZncj6Bbof_JMkzYTlHDWueKB88h6DppQO7pw-k8_FpyMKtQGCKAhHGOCgtILbrz3OlJ1rU6-2fNaDUwPMr2XqXs_v_fDqO8r5lnuLo-w5-XiC6lDXbtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جواد نکونام در برنامه زنده خطاب به عادل: پائولو دیبالا لامصب چقدر خوشکلهه این پسر
🗿
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/23214" target="_blank">📅 22:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23213">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">⚽️
ویدیوکامل‌اجرای‌امشب شکیرا خواننده کلمبیایی معروف در مراسم افتتاحیه جام جهانی 2026
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/23213" target="_blank">📅 21:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23212">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WaL9aDD2bsZ0baElkBjf9ZwpdXa3evqkAaQhqjyykRw14hwP4eywA0EP93zSWLcNW7JH7GfM3veE6Hsds4OV-RZxVSxUHzQ2irlh8Sdm6RyVJaOQc8-AoNjzIhcCNvoyw7IN_efO_lC-rI2QaKbIkV1nX7A_FQWf5gPedjKbJ26QyQ0-zjF6DlsAoGOvSEqFBZVGI0YiYMEtH_b8w565SJx95kGUhs79mOG-Ma1DW2dfZarPGisg7PMMskMl1OgvI66md0cHLNH_crHsSBqW_F1Q7kdWomjm8hTd-_mBrrqRikhxMaE0UGN0fxudSav_OOt_FbcyuPhQugkXWKqSIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
🇦🇷
صحبت‌های جالب پائولو دیبالا ستاره تیم ملی آرژانتین در گفتگو با عادل؛ برگای جواد نکونام و کاوه رضایی از این مهمون برنامه عادل ریخت قشنگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/23212" target="_blank">📅 21:47 · 21 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
