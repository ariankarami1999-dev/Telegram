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
<img src="https://cdn4.telesco.pe/file/vJM0Blj1ZfLHKPSPvru6ho7JvClCvqDsL9rl70_CST0BTh_oGY_MYQDHaRV5zSg6Pi2EGW_soVY9I8NqyMV2PSRHe7IPmaKGoK_QX8wUbw_-5V-QVa-oIniKWX5Ka5_sNn8ABdi8lTgEQcBIYvXDx3BoMLS-6-vo8W5Wj2B4DdJCzHjUGgb09lMgsEyNqrahyZB9KyV5JHrE51G_kmlOlCYMrksorM0oDbcUVzS2mQPzuJcmLTCM5mOmTc385MsjMIvAwokZBi_NFKANFd8ob7rJGx4V_E6ZdTc8LkNG1oLbFpf2Twf3CHDwf6DrDGxxmtd4gPLQNhQsUbdsxiPG5Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 317K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-04 07:27:51</div>
<hr>

<div class="tg-post" id="msg-24265">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07d25b9dc0.mp4?token=AAnnWWarpZreS6t1xkjux2dXZDExXbHmaCwuhh8ptEKUoDd3tejiOctEeDHkUdh2daSMhnrt48ti5nM9K1WWBuLGYjvAzmHMLqqMYe4Z0WhHN_HEbVGvN7O5BiebzCwuf60hlrqryqEGIxhRJx_4jT3dTM5WxS14h5DKE3QziQW5qg65TGGM0rofsF9D6550zQC6MOrwArCQ3nlewFau26mzNg7seVibop0Y0bZhBHtdfaFTQ5u4i3kl6OH_JvFgp48jNE1FI4Bhipb4M8gpoLcyvA8ODlDO5kTvCiVN80aOZNmds1oF6O-_WWMEzXOJF59180puxX-5PAhxaTSjkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07d25b9dc0.mp4?token=AAnnWWarpZreS6t1xkjux2dXZDExXbHmaCwuhh8ptEKUoDd3tejiOctEeDHkUdh2daSMhnrt48ti5nM9K1WWBuLGYjvAzmHMLqqMYe4Z0WhHN_HEbVGvN7O5BiebzCwuf60hlrqryqEGIxhRJx_4jT3dTM5WxS14h5DKE3QziQW5qg65TGGM0rofsF9D6550zQC6MOrwArCQ3nlewFau26mzNg7seVibop0Y0bZhBHtdfaFTQ5u4i3kl6OH_JvFgp48jNE1FI4Bhipb4M8gpoLcyvA8ODlDO5kTvCiVN80aOZNmds1oF6O-_WWMEzXOJF59180puxX-5PAhxaTSjkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جدول‌گروه C جام‌جهانی 2026 در پایان مرحله گروهی؛ برزیل بادرخشش‌وینی سه بر صفر اسکاتلند روشکست‌داد؛ مراکشم چهار بر دو هائیتی رو برد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/24265" target="_blank">📅 03:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24264">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🏆
جدول‌گروه C جام‌جهانی 2026 در پایان مرحله گروهی؛ برزیل بادرخشش‌وینی سه بر صفر اسکاتلند روشکست‌داد؛ مراکشم چهار بر دو هائیتی رو برد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/24264" target="_blank">📅 03:45 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24263">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CNgubZPLOyqo8_G64h9XHsE4F-xHcJYifurOd5B_UxiCbkg9Zcr-fpepDNR19Fjhulx4I5j_aIZJHJCKvXnpVMpRATwuHz7R49BZMYbQ3O-O89OmiRKz74G9W5zOiv8z1sB190L3kukrrvRuHUK2OWjZoAlZhNt0Hc4eclmlroN4owSywJJ7T6UU1GtbggqukwHWaypkqJSPFc2u-hRmw1iGo3VbZm86Oi8Q_sPfQUjNjnLlm9joODDQPnLkAhKGcf1SwJcUpOxcVeXvMFMuq9ueQXKMGmLZ_KUvEkD9dZ4dGoT36XsCyia9D39Kxxyb1LDlDpq9jfN8TqRYLTX3nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدول‌گروهB درپایان‌مرحله‌گروهی جام جهانی؛ سوئیس، کانادا و بوسنی راهی مرحله بعدی شدند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/24263" target="_blank">📅 03:37 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24261">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nrU4CmL_oSmUS05GkjbgL4nUQpC_BBqijOuMxmOnGi_6MiJKqzWaXfobDqCmFUr_v9tTayviGPbyJXdX5ZSZJ8y70kMjn6WOLsSOLkYn6z8UugQbKRbu5SY3SpvMnuRyGRXI4a_-ENKI2EwKh4q9GHJMFu2uNNj6pg6-n80SY5Bax_wXu3oaX6CoYBHsMn1t2ddMqoECSpgd3J7yir8CTWkmvT3qGM2-vGggWC8wAY0gL4luW-O4MtyEv4l69TMB-bTbYhvzB_kdMw6-GMS21xNn6_FQ0rqQcJtQuZHv6gtegPSNb3jaImWyCbcTJxnBW6-onjgQ2XzTf7u6eNa-RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a6d46fb08.mp4?token=E03uCDKqHRJYaej2T8q-iy_OmiIBhhiSWSvfAEb8jLGI7K61AhXwHGhgptalhgF1pjJJ7CUWcgzfCbfjEl50kjBb7I5sUB5ruubBERDyhWZhIsuXHg6JDTZHMOfqlhFbggtXWxqNQUYizHV80I6Hi_TFuzEa3P-ax-rZAfTaj_iAbn31Cm_7MNmU4PCjl7HdF82dqq6WN3Uaby4i1gGGcv6DjFGwJhLNV-Pyz3PPTFSE1TcG4QvzUqB6SaiOrKYKqb6b1V8gRrg9PdagMRHthB3_TcCJVWTwTei5xiMTWAT4uXNlzcJ_8oOI6TNmWbth_F85mT4LbXLAnqj88oSjWDyFsz9fecIgRokPlUqkFdC9nOunRNg4J5RHUE-FPJxQZYd7PmCev-w_X7i4uoImC1A5wVyvQJQSL10BGcKNUaz1x43hhYBGvfvtyaFmen5oMFYyxC5a5136shEq8BjZCRie5HvcTpbgGmdur5GdNtQZILBOb93desGIZie8FIUHZ5MYtt0boO9NelzJxpdahQJYd0VB9JS3MkY49FlPB2Ex6u3JWBVNyG3KovpUyyyQ6Iqek3eWVCxyAF1XGIxKBETS4N5Fu9aLXoZ-DWlTlpwOgqGbHaqAHXWab7Hn0Kdb8e6dtSQOsAd8yGYqV0rrSzo_QJvQfOaP_fjzFjh7cMo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a6d46fb08.mp4?token=E03uCDKqHRJYaej2T8q-iy_OmiIBhhiSWSvfAEb8jLGI7K61AhXwHGhgptalhgF1pjJJ7CUWcgzfCbfjEl50kjBb7I5sUB5ruubBERDyhWZhIsuXHg6JDTZHMOfqlhFbggtXWxqNQUYizHV80I6Hi_TFuzEa3P-ax-rZAfTaj_iAbn31Cm_7MNmU4PCjl7HdF82dqq6WN3Uaby4i1gGGcv6DjFGwJhLNV-Pyz3PPTFSE1TcG4QvzUqB6SaiOrKYKqb6b1V8gRrg9PdagMRHthB3_TcCJVWTwTei5xiMTWAT4uXNlzcJ_8oOI6TNmWbth_F85mT4LbXLAnqj88oSjWDyFsz9fecIgRokPlUqkFdC9nOunRNg4J5RHUE-FPJxQZYd7PmCev-w_X7i4uoImC1A5wVyvQJQSL10BGcKNUaz1x43hhYBGvfvtyaFmen5oMFYyxC5a5136shEq8BjZCRie5HvcTpbgGmdur5GdNtQZILBOb93desGIZie8FIUHZ5MYtt0boO9NelzJxpdahQJYd0VB9JS3MkY49FlPB2Ex6u3JWBVNyG3KovpUyyyQ6Iqek3eWVCxyAF1XGIxKBETS4N5Fu9aLXoZ-DWlTlpwOgqGbHaqAHXWab7Hn0Kdb8e6dtSQOsAd8yGYqV0rrSzo_QJvQfOaP_fjzFjh7cMo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇧🇷
یک پیش‌گویی عجیب و آخرالزمانی از یک پیشگوی برزیلی بنام «وو باهیانا» در فضای مجازی جنجال به پاکرده‌است؛ او با گریه و زاری مدعی شده که در جریان بازی برزیل و اسکاتلند در ورزشگاه هارد راک میامی، دو سفینه فضایی به استادیوم حمله خواهند کرد و در دقیقه ۳۸ نیمه دوم، یکی از این یوفوها اختصاصاً
نیمار
را با خود می‌برد، در حالی که سفینه بزرگ‌تر هزاران نفر از بازیکنان و تماشاگران دیگر را می‌رباید!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/persiana_Soccer/24261" target="_blank">📅 01:37 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24260">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed8236df4e.mp4?token=nFSqvPTgWSU0880KvsNn_lXxhNFn-Io5rl4jqO8wSmEll5OQXNIs6eUJCewKTogN8ZGmlOmnV-9I5y1z2MgCAZ1o_cVYXzkP-lCW69XfWPVPJtt16nB1kfvpbnlkCH6pTsOTHwaNMI86t6qbh_TZAmqWKT6cI1PHndywXukUbratPG44NdIcfGQqUogz1fV44X7PsR4tuoqgTYz1JailZmG_5DcFh4mS45ekseSN3qv58DYoMd4Mtd03692LzEzQN5DXQehWlnzk-XgoK4Bo-l9jixRWsQxwa-zVTHmlw6EjW9ngNtI6yBIDRO0tERoWit2g83RocIMiU4N7adSNyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed8236df4e.mp4?token=nFSqvPTgWSU0880KvsNn_lXxhNFn-Io5rl4jqO8wSmEll5OQXNIs6eUJCewKTogN8ZGmlOmnV-9I5y1z2MgCAZ1o_cVYXzkP-lCW69XfWPVPJtt16nB1kfvpbnlkCH6pTsOTHwaNMI86t6qbh_TZAmqWKT6cI1PHndywXukUbratPG44NdIcfGQqUogz1fV44X7PsR4tuoqgTYz1JailZmG_5DcFh4mS45ekseSN3qv58DYoMd4Mtd03692LzEzQN5DXQehWlnzk-XgoK4Bo-l9jixRWsQxwa-zVTHmlw6EjW9ngNtI6yBIDRO0tERoWit2g83RocIMiU4N7adSNyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بااعلام رسمی فرهنگستان لغت فارسی:
آب درنگ جایگزین فارسی کلمه hydration break شد!
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/persiana_Soccer/24260" target="_blank">📅 01:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24257">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vAqxVhi-xhVLwL-_114Gj1euJBYbZnBC-mV87Xl6gGIiFRn_MLP9I_qV2JFOHgyLor0k6GnqZCvbANHceHrQJgfHnpCYsY9kcuIfFuT8SGEKLlSmdpXjasx6UXVNkOD6IkqeRpMsZd_0Z3vNiJF5z-FYHfZW3e0_9M1I_TyVvure0H1s4CED8RfN5zV4ciRmNN6c7p8wlMVhqlVPhb9XL20SNgzZ6P0vj1Lg35eoAl3evXqqysrE90Q5fMWkFRjWttk7Tad9_crrVBkQV3XVIavO_w4cM6ASPQ6K-5rEiCGH7BjiCZR9QqkuhE-c0v2bzZ7Q44c1u1TuA5f6WbqRGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارهای‌‌امروز؛
از تقابل حساس سلسائو با یاران اسکات مک‌تامینی تا جدال ژرمن‌ها با اکوادور
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/persiana_Soccer/24257" target="_blank">📅 01:17 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24256">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VxRp3WBTu1-XYmH1bzf9gbp5j_dJecfpLkrqYFtvmPBd-3S7bKJAZZ2ZjHajJwIfWWafNpS0SXLLL7YSrIMlwaYpPzY42WGu77TzPeKkcseNfnRJjK7czj3ygauXxZw_aaYrTH4azRKNiWqmPpFAlZw3zCMJOn-YcPXpLa4-y_S6qViqa1PmCmqam-ybsl3g_E-THKL6Qi2rpdDuMjsfUgdeS6spyXsU0QVjIvQmzI2tSLo5RRq5vVQ_T6ysAdVFeD5j1kT63NTHtJ6rCjoJITNGwSxDDoeMr_OOfE3xlRz25tzgVRwxYybKpIBsPAZhD01J-m82GYkiyUrvlZYxJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌‌‌دیروز؛
ازبرتری‌یاران لوکا مودریچ برابر پاناما تا صعودچهار تیم کلمبیا، سوئیس، کانادا و بوسنی به دور حذفی رقابت های جام جهانی 2026.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/persiana_Soccer/24256" target="_blank">📅 01:17 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24254">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H0y2t40eq2VhKjl5nKoRkARzdSBZ5K57xQeEpNYePcezO9q-8kinMBG92MRScKECSFDG0sQkubqKE32OUETIK6CKmuO--dN6fCWt2yCpamiWq7QZdTAECcXqAupDH1eDhsZI2oTeuGrMxxDoq-qOQua_Yv2HsSBfpJk4YsDv0Y5wApcpAUVWb36tU13aTH6ev7LyQxbGnFjcnL1coAmOgyY6qrUZPYT0W8S32WaZq4pMoP5R5OuLtthWhwfWbgPeGOG78opgF0hBGFcEkDcI2iy-kYt6XXjeg0xPMVnDrdtApOkc5jdu-c9Vw5B3sERv-T1IoMHvun6IvB1KeTUjYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qKysV4zSA35__4TCmUf1bcGT_stqBrBE67fOhX5mwxIDbronPEv5NsDkMSm5DNkaUbz0GNgeaPF4QnIapf5V4gv6iPCOglZMG7W_u4NSszimk_xNamSvLOneij2KRGPyG13cVkpcY6jUG-YETRaGiCBsTDPcQd6GFB6ce4r5NOjdy2h8irgCmaBupHT4XTFAao4ssT_6w-yEHvfODMHKMQOa9DnKkej469hGEiDULVqSMqyGbZRj44HdI2UOG8MpNNrXF1fe9N9WxWKVEsNNns92tlVQj1lEi4Arh1Je0R-ESbdKJOIGJED6dpB_YKK3xGD-T00gUGt7YdkduM0Obg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
همسر گابریل مارتینی ستاره تیم ملی برزیل که آماده دیدار امشب مقابل اسکاتلنده. جالبههه بدونید که همسر مارتینی پزشکان زنان است.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/persiana_Soccer/24254" target="_blank">📅 01:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24253">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rja2Y722oDhlRgeNdP85W-DIYHXVgnKE-QgS1IwlOMrGMNyX66FGYtZljHlqlILDEy8fHEpjaY1zK2cuUmgeDg7333ZT6wpnYK-fmu9LJGbHMNllT8B2ekguuYLcxHkIXzzkgm_3wPnpudvL6qGxVyZ2jR5KzfLY2yyWqQwF38zUppCSW5EQjyMV23Szs1MjKQipZbBIGpZ7C8kTKlzMComMkVj7CMPd8Fp4NHM06giIifOMtqK-N0pfa86K8ByinpB4R0gENhbJu1BFG1WHRXvLkun-ovvovEW2G0ptgKDHh0MeWYa5YoMcuk1kQyZV-UyddJHjMx8RlKzIhBFaGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ توافق نهایی حسینی با استقلال، رونمایی بعد از آزاد شدن!
🔵
همانطور که درروزهای‌اخیر نیز خبر داده بودیم؛ مدیریت‌ باشگاه‌ استقلال‌ شب‌ گذشته پیشنهاد مالی خودرا برای عقدقراردادی دو ساله به مجید حسینی مدافع 29 ساله تیم کایسری داده و حسینی…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/persiana_Soccer/24253" target="_blank">📅 01:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24252">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aQ9uGVvpvNkFMQX8FyHvIukg515blhCh0RkZBZsgchHoCGD1M1XaazIFn5Kv7fBowOQZC_zlWu2DYWmw1cTRn5gPYsemnxrDUnODQZv8rLOKqErD7tHQoy52Xm4q07rtYTrCGssaKtk0JTO5H-gEhf2Eemt5UU7SNOwb56scTrR3sO_eU_eeslPoNmHRKAunVFkmLfNxDZ_uaaj8QD7ZbwRf1B8wEzLphfk85VRq9xzlwPLnhsth90gbFs90pQppwQcAfgL89bP21eMp68angw4SVNvodGL6Khp1XpJkIdjxFXehrW9VBsrWowbawwtvlB2unElUd7BPRhpA7N46VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
از هرواریز
🤩
🤩
درصد شارژ اضافه خالص هدیه بگیر بدون قیدو شرط!
😮
تنها سایتی که
به ازای هر 1,000,000 تومان واریزبهتون 1,200,000تومان‌شارژ میده
اینجاس
👈
این یک هدیه کاملا نقدی است!
✔️
هرچی شارژ کنی
0️⃣
2️⃣
🔤
موجودی خالص میگیری
👇
🔴
اگر هم باخت بدی همون‌لحظه
🤩
🤩
درصد  مبلغ باخت به حسابت برمیگرده.
⌛
پشتیبانی 24 ساعته
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان
a3
@betinjabet</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/persiana_Soccer/24252" target="_blank">📅 01:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24251">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NPBTEpmooGYncWJmU86aNsmKN74R7W4NmrR3Y696cBp8k2mK8m-f7hvEziYAk2m8ugd0kTFk4JjqvEg21r_yiSVn8mshkf8nvI0O2clwLL3BTvk-gnOvZCXn-j-gE2KLyI7YEnlfMoCfOmkqYLv2Tj6pzVP34_jKU8WS3kbIvPl2cJ84U-XVy4cvxZfXZmf6womWn4WMkOg4yYuqD63p7AxkyvaMOhhm75YXbgtTBnO2ijsqVa183T9hi-dITeAkOOqaY-vbTnIInA7zFGPDPB5HdZae67f9QWbXmeDXD-Mw46x1RbBm7QlReohjdgg1DSCyPtUPuufWSvqwRmB2tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
هفته‌دوم لیگ ملت‌های والیبال؛ ترکیب تیم ملی برای دیدار با فرانسه؛ ساعت 22:00 از پرشیانا سه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/persiana_Soccer/24251" target="_blank">📅 00:53 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24250">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WSJoacyYojNFhvFQxq2Djs084GLCTDUVYQ5mbeHCaaffheZh66pCiCkU801z55tFc9L9c9e-TbiemXB98R_KRmMXib7fxMq42PxPTtYwlnThQGAwcc0rPP0-Mxv3F6Gx0eOA5O_26uht-xA4SndZiQvlWoA-4iWgksAmxzAnDfAAA8vWFHl3GmFUQx2ht1o_xVy5jQs3GYvkSDU4bSTI_FIJGHkdt87jTx5Zmx01B4qw67TbgyeCJ3jGWGbTFIVHCbF2Fg1B-5CSof0sjmtGsRC1b067gOW40t41BDafvKQ7Ir6VcVonCEQvhr2fAMfZMLlXaliBisLZ4zmMIl5msQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هفته‌سوم‌جام‌جهانی2026؛ شماتیک‌ترکیب تیم ملی برزیل برای‌دیدارمقابل اسکاتلند؛ ساعت 01:30
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/persiana_Soccer/24250" target="_blank">📅 00:42 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24249">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SNyWyV3XrR_UzJ1S-F6HbHBHR_rzsgTbQB6gGXasrrwithQs8W4zJYVMMRkzIqkGsYQKJ7JkpP0COXaW3xHDTltyqMxFa5FFQ-MGfzj7ZrTocTwXh-Y_HxTA092WLhEe-5SdSaIfROWxvdkbTvh4gaMaAry8SYWFi6V_aAKZ42yM1cpNgLKzm52Hjm5k-AocajzEuD5QKrxJRwjajW6UViW7PPnLQpOB5KQNTAgW4txgTp1zuUQ7lYFIAyO5NEAc1BSiqZw-BdwHxFkRz-VkBNzTgROfUyNvZl379oPlTp7seFL8VPAWpyT68fqQHhcKrUC5Yo3ceCER3PkA8atfTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛ آغاز تقابل‌های جذاب و حساس هفته‌پایانی‌دورگروهی جام جهانی 2026
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/persiana_Soccer/24249" target="_blank">📅 00:38 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24248">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81b3f9aaf4.mp4?token=XuvG2XL3fZ_him_tD09rmmUr1OAKh12Zv8zhSPoupgwZDY9Brf_OccGd7J9hCM62H7eg13PMrKHIqNMOffZ2k2nNfCMf1x9EoRB1C94_GXVObHlYn4PU_1xH6SG29JkTWoG3fj7PJp84qXmuhMBJla1l9HCX36GWgr79xLYKqyVYikcb0NsjHDDIw0CZo7vQOL9BjCWsYEFiO_NsriWZYlBujBguCSEiVfr46aQB-_0XaCs27dUao852BocRM0yjnxXk4w1F_DOaHNv1CNF9Ru9Zc_zCJVUd5RJ65p2ifTRhFUNAVzMkIeyCbEpInM69hpLNbj0AZHQshd6KMl4aVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81b3f9aaf4.mp4?token=XuvG2XL3fZ_him_tD09rmmUr1OAKh12Zv8zhSPoupgwZDY9Brf_OccGd7J9hCM62H7eg13PMrKHIqNMOffZ2k2nNfCMf1x9EoRB1C94_GXVObHlYn4PU_1xH6SG29JkTWoG3fj7PJp84qXmuhMBJla1l9HCX36GWgr79xLYKqyVYikcb0NsjHDDIw0CZo7vQOL9BjCWsYEFiO_NsriWZYlBujBguCSEiVfr46aQB-_0XaCs27dUao852BocRM0yjnxXk4w1F_DOaHNv1CNF9Ru9Zc_zCJVUd5RJ65p2ifTRhFUNAVzMkIeyCbEpInM69hpLNbj0AZHQshd6KMl4aVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‏میگویند کیروش باعث‌شد فوتبال‌ما تدافعی شود. مگر قبل از کیروش فوتبال ایران چه آش دهن‌ سوزی بود که نگران دفاعی‌ شدنش هستید ؟ تیمی که حتی دو دوره متوالی نمی‌توانست به جام جهانی برود و در گروهی مقدماتی‌جام‌جهانی ۲۰۱۰ پایین‌تراز کره شمالی و عربستان قرارداشت…</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/persiana_Soccer/24248" target="_blank">📅 00:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24247">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/po0N8SYrs3Zx2uuiD3B_NKmRAP9pgAP4XoQDiXE0prUrSKKCS7tWWDXwByx0oE8IW1L2Pq7Ep4EUEmpKD1fISxI3w2nNOMjZ_OS1IgRTt77vJEis3MZDZE6bldkad4eALuH6xMe989D3CpDqtAJ8oCP7IBmAkWLQGbHS3UAKAYc0gWSOar_PRbYtdQa9QFcPB0-ieewEF3wxKSvBOI9NI9J8QUdjalGmeJK_kTceIaoqR3B0tyZtjnhOh81_zL3wWYFyZHAfkn9DiQQPCFAMBQ37dzf6s3NLN9UbQifVG389tMpmVwBnwSPzXiQ-8JNcZGhH5d8xRYkm8mTxPn4btg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ با اعلام کادرپزشکی تیم ملی برزیل؛ نیمار جونیور از هفته سوم جام جهانی میتونه برای سلسائو به میدان بره و مقابل اسکاتلند بازی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/persiana_Soccer/24247" target="_blank">📅 00:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24246">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xd0prh6vQu6XzsSfY2VgMzs1VuUxVqRsN4x37-UwKoAkZ_UdOkgMuIL4vvJDG3jz4Zj5PMWtvKuZZ2ZA6strUlGHZ1xiTxTmgC3RD1_zah_6CHBr6PF-yMCFg7oGdWdpFC2GgZRoNbp3SkM6fvBFeX5dQ6NYMp7H4X2ySaFJntMgxNcsh7ONw3oyr-q2zp-Dk_opeDxEpG8plB9E1el3rd1I7f1k7f2FBdkUWnTOz_ohHOuokJHt6dqjVlw2-DMycDbKgMXs_wSz6rnndi9kHKmEe54HD5xECcZBbLvFoxWA24Fbfkc73TDemhhvcjbMLTqdVQV0OZD0dNckqghmQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇬🇭
#تکمیلی؛ عملکرد کارلوس کی‌روش در تیم‌ ملی غنا؛ پیش‌ازجام‌جهانی‌تموم بازی‌های دوستانه رو واگذارکرده‌بود امادرجام‌جهانی و درگروهی‌که دو ابر قدرت فوتبال‌اروپا توش حضور دارند دو کلین شیت کرده و باچهار امتیاز در صدرجدول گروه قرار داره.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/persiana_Soccer/24246" target="_blank">📅 23:59 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24245">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E8XVL2u1nYnGRmWjx71l9xFKRJ8G3jqNNsE1ZfOolhcwtORgA52-XJ2Ae4KkNrdhVcQsfV_nib8qMeCFQAWpbRHqfGa_cr2Mm8Uv0PUeT2a3rWe1S8gqLZsHRLQvEslnXy4ExW7uYc2_i1HUL6nqHbEfmEAgVD-SJ0XV5j7Xt94Ei5SRjxrIi3EFkSe--wB46c_FeXdpgLa6Jwrt-wsGj7Xn-MXC9G64GSTQMfL7Tbtp3ICSVZlnSBQ32WFnBRNBx5A7wc3gyfgUAEOlEUjr4BgblE3ZR-lkycU3h6LGr3XTJcY9DhcfZchGrimUDdQcHyCjTnLer302HfmqqdO2Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌پرشیانا؛
محمدرضا آزادی از سه باشگاه گل گهر سیرجان، فولاد خوزستان و نساجی پیشنهاد رسمی دریافت کرده و درصورت موافقت سهراب بختیاری زاده از جمع آبی‌ها جدا میشه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/24245" target="_blank">📅 23:22 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24244">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kzqaYIdBvR14VtCr6R1hpmTsrK80Z0s7YrIomRkXH4Y8xtWOzRRzorotLbDusgq6wVe6Do_dsd-EEo_-9Yx52HCqhmiraqo5hPKIY-ZaC-6tMRExbkywYBLPP4p8ifYv3G79UVY4Dzs15WRpMtg3OOyskg3qKDVvfLE1gB0iUbS2JKqIBR7oAXAUIhgj16ARL0yjH_3CbYlD4NVtGTY-wkVRsi2GVt4w9Z0lF3wV1FaLXsVTiEuxr1Nqio4f28IX-2bmJY8usdIeELw6YSzf5TlyUAiEvggjqMfaw9a8ytSKBfznDfaPI-0iUoqW88qr7pNpueyfMiPxlnJz25uiIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پوستررسمی‌باشگاه‌کوردستانی دهوک عراق برای یحیی گلمحمدی سرمربی ایرانی و جدید این تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/24244" target="_blank">📅 22:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24243">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e4YJEOqf3qlPEN6HVoOA1QtY3sVSAVaKP2bZ0iFdI5FJGLjeJ5PCSR2iXQwrJ9q4r1LV02jh9Wd77LULdVkNacVvCnnV-uqDNJbS1jejE8L-Ba9CTzfGb6XMYQ6Uo1qtGQ3ZefTz68KltRE3XtBo772R6QkcJp2hFlvbQ5L7_Ze5fEV404__gVHPZcr9XNlfjN62TXM22gsBTN3C1utVQBvckRFBpA1ibJ14Pt8bKiEegyJ6UdWjWvROELMUkh4lCQs5hrc4gbIw10-_uYGG9RgPOjL-JWCFfNRgajpf06L2uAk0t3Kji2IxvwUbw2s5_vehaLQnCwzej6uiFaZkaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
🇵🇹
تمام گل‌های لئو مسی و کریس رونالدو در تاریخ جام‌جهانی مقابل چه تیم‌هایی بوده؟!
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/24243" target="_blank">📅 22:51 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24242">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">📹
این چه سمی بود دیدم؛
رونالدو، یامال و هالند درمدارس هند؛ ارزش دانلود 100000 از 10
😂
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/24242" target="_blank">📅 22:51 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24241">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CiSdtn_dkT5E0ru7Sa9Gv1q_6hBxOZJIraJZnJcezMbD1VvMpIm7yFCwl2vAgZIHam5hzon2r5GvN6AwD7vWK--u4IoF3Sko4uMSaNY7EJTjF7sQCliG2CMdaEi4P-_GxF-i3q8gnF5o5F2UtTWxeFmy4hE4paSQ9S5XEk9lhMiSzyey0Ctt9OQwlWlC4oV487f_ys43X0ULIGknTW-kpNym3KWprKdZsRgVQYafPI08R86js3n-elctKTE3iH-PhR843R6gyzTvjWLhzV1nnnm9UknOeMb44CgTtDG_fQU-HntZhwwv1SDYLuiVOXfTsX2grv-38BnYeJu4ZRqvow.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/persiana_Soccer/24241" target="_blank">📅 22:51 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24239">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VXPcsVlQMUqYJRBdlxDntJELEJTzPZkvF40w_HAiVft0AYN30UicK3JFODJByibLNC2WKNoCHeqNfc_50rjlDjYTLZjysENcOM0AHlu6mChvSSGJRaSXVuf8ZLBJI0xJkYcIUtcnd8mDwru5eHfNP7jlHE-KtK3kL9URxQ7QKSTHWqHvlkoMsvnZsq_AGpAM8MEwQQ1JkbDUi4-NBp1tsWosYS6-suFTtzkF7gRPbgvuLbbz6qij8fRQh1AndSbGB3RgmP5KrEluWUs2FG5DvU30vhjlE-htWCU-0IPg2kFV3OvaTAhkqXy4WH-s_N4hvqbafXaGsLNOMzAdJrDRVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eSQlAM9Eu17ycwtFMx0dFXWfnEOJJ79kuBzwiKmm3gzaAb8F0m9-rb35WeXZCSjJ2OE5P2quxfIUsJVRCFsLot2n5HraJ16KFizq5O9FixusfJ2GGL6NFlJDQZCBWFWVhsQ22vQZlf_fsNEDcSGsL9jVGNHC8qpIcChLTVa6HHIUSvEncWIsNP_twxQkWQUgiHj63Ge_tkmT19IisqiEbcUcMUnAjoNU0W7E9ym1fvf3mM3H2t8zZl-dQM7xXxScJFpRT7t1oKe9EcI6wkLmx-0wKu_wBHMaqasdD2X6VN9eV8Ge5M_td2mbCwzvUL0rOEwLzBif4Bs9U-jkU2deGw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🤩
🇵🇹
تمام گل‌های لئو مسی و کریس رونالدو در تاریخ جام‌جهانی مقابل چه تیم‌هایی بوده؟!
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/24239" target="_blank">📅 22:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24238">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d46a7b1648.mp4?token=rRbza2iQ5sQPIs8P-Xg87QOIFlCRkIojuJVN4GCzvZGjzBtVMTf443NwFFkaJMCZlUvmxILVnrN4AIIrzGlYOD1ITwkZ--aWiwqQFvrangygjIJRBF1Y6U96hZkWOM-UzVq08vVs-Czoxo80jHkkZqsAGwFzlgXYTxN5kH_f5Fo_n6oNVlwH6-1D-kkggAXK8cUH-LecLRZCCj7r8gGRr6KXY0JWg4es0mAb-O7sZ9KAmO4OBURMCUwKoLz8qo8IuS9QfZFxu-fhQvxMrmR4TurgnghzUMtmV8L8P4Zj-AJFtFjkAOOyHp7WTTmzBCOU-wJqPWUUGLAVLGrGaZJ7JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d46a7b1648.mp4?token=rRbza2iQ5sQPIs8P-Xg87QOIFlCRkIojuJVN4GCzvZGjzBtVMTf443NwFFkaJMCZlUvmxILVnrN4AIIrzGlYOD1ITwkZ--aWiwqQFvrangygjIJRBF1Y6U96hZkWOM-UzVq08vVs-Czoxo80jHkkZqsAGwFzlgXYTxN5kH_f5Fo_n6oNVlwH6-1D-kkggAXK8cUH-LecLRZCCj7r8gGRr6KXY0JWg4es0mAb-O7sZ9KAmO4OBURMCUwKoLz8qo8IuS9QfZFxu-fhQvxMrmR4TurgnghzUMtmV8L8P4Zj-AJFtFjkAOOyHp7WTTmzBCOU-wJqPWUUGLAVLGrGaZJ7JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیویی جالب که لامین یامال ستاره اسپانیایی باشگاه‌بارسا امروز داداش کوچیک ترش منتشر کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/24238" target="_blank">📅 22:02 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24237">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nP8LbxfzNgwrOUSuxHgI-oj7ItIPDvuElQWdDMI7sU5YSaYTa9Wk1UbhA3kgQyVbYS9I0TlTFlFvDQNTZXrcRKNoWTZOHfG8qwpQ6ELCRSzGmhs-17Smpgp2ciykIbTF7ly6gCaj675f3Un52KwxwcgYojEPNCrpqVff2aDrCbXqKTNm_sgEP27yCv8otrwp5ICkqFjWqdvW4r7nLIDHOvT-4AtMFLY0fHeFAj8vl_dUc6vG_mNBta_mJxIRgGmmeYDHY4tCG9qycS4ynBFneFhC49WQDkKlD7wB3W45GSN82loTrJIol_yCC53sxSvtzfj7OED0uHbnOa6NSpprYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
مسابقه امشب والیبال تیم های ایران و فرانسه به صورت زنده‌ازشبکه‌پرشیانا 3 در یاهست پخش میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/24237" target="_blank">📅 21:45 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24236">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vsfUmVQ4cVBaCJ5KSsCi-PY0pgvLFeD2z_QByEGl-ojcCzG_K_nB3JyacyqktGK3ML6CXOyvGrFnX66afC9DT1OM1sX43oDgPX74iuZpT0HYBa__dGpXw-Rxld0tggytrJtevKu1wHs3BuZ26HfKN4aQR3A8hgtFBjCmt8CMcMoA6b0zveV4d537hxw6D4ncFndHJfo11JkmTV3QZoCQD0hwZVro_m_3EOq_y2alTm5DH5UIwYNXPckbV1n8i385VQSvdD7TKrncsv6MLgl8PZi9J08_YKutFMGVelEte4Ze8317TxOkg3DcakXvGwxHMr0VPX4PiFm9DshYqEXvxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی‌طارمی و سعیدالهویی، مربی تیم ایران به محض ورود به فرودگاه سیاتل آمریکا توسط پلیس بازداشت شده و هم‌اکنون در حال بازجویی هستند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/24236" target="_blank">📅 21:28 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24235">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fLhKfDF-hLrpHkc0DsFPoGRmTw2-r2bt2Ku55cw3zmBqZlAdYNXuK7uuTALe8m4Zlv1kzbfRZWVn1GQxeYF57Q4YUpDkidb3ChAT1RzRkMvmHTE-_6gEytDLeYkRoXaakM-mXyTfb2R7tfIcBGXMV2da7LiZtWRqdcKSiGGT907JUxm5AyuYcjAmg7AculINwafP5QWD_Ot2EKaX9l_55Jv1J2TUr0EDljrbewQqO6ty1jfcqatEvEBGJz3vBN_7GY3bDK8Kf29d4WtkFOXIpR2GDbYzwIKfrj3u00AWTeRMdegxReTge5bwR857TyzXFDyG3nfe2tVvtVqv-euWJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
طبق‌ شنیده‌های‌رسانه‌ پرشیانا؛ مدیریت باشگاه استقلال ساعتی‌قبل به مدیربرنامه سید مجید حسینی اعلام‌کرده‌که درصورتیکه‌خودِ بازیکن رضایت نامه‌اش رو از کایسری‌اسپور بگیره و بازیکن آزاد بشه بااو قراردادی به مدت سه سال امضا خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/24235" target="_blank">📅 21:11 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24233">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SuEvkyq826BJjrbpUtG_FDdx6p0-mvU_3Tg_CVwGdee6bvUbJk_Gkn_Nh95k4EPSkByrq2hGON8ev2FXQA19SZwxfK8lYJY1v-o0qlRkB-qlBDSKhnTucC2ZLZ8sg3RcfoXLc0fzhPH2wFVI5-F8KrONVkjfXoMnM1uR0h0i2Yn9d1IjtZT4IxuvOQoaSd5orp4aEY8w1h-pHLxCX6QVkZyYRKTMOn9nTwa_71nY3inNU-lolJbUemTPUaH9klA_xsMywKH4KWJhglJ1S_UUX3GjDn9eGz2f4Vr50_KxTmraUfH0CNZS1Rsj4wmxE0Gzgpfe5o_nhwdegAONLHskoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇵🇹
ژوزه مورینیو سرمربی جدید رئال مادرید:
رئال‌مادریدبهترین‌باشگاه‌دنیاست و بارسلونا هم بعد از باشگاه‌رئال‌مادرید یکی از بهترین باشگاه‌های دنیاست. درباره کریس رونالدو بارها گفته ام اگه از او متنفرید دوحالت بیشتر نداره یا او تیمتون رو به شدت تحقیر کرده یا از بازیکن مورد علاقه شما خیلی بهتره.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/24233" target="_blank">📅 20:51 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24232">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/roo-JRyO0F8lCahydBzk5JFeKXcOW6jex-I52oivVRZd3TtzUEJp3Tw23vRtKJYiAKRdPZ0dyiFqmANihFt3kBAWflOfVGA1d69uB_ewe_HUtu4zlfUCgg1kc9dn5V9WqTVodBBfVHiWhWVDmEFM5OP8Sqx_GVqS2YRtLqXELhfQEQmpUggQCWZWUatA8zdMhFQtRmjepYDek6IWICiQ5uWQlNpwQSPvjIbj5E0ayp1NwY1R8Mc8soJvzgvjsMCwZKjcCSvyeYHNOVyKugXK2EvwRvIyUOl8gIRnV5egYEmBN3Hg97bwiPHGNxMdUr-c7Vl_IISUrqQ5nNP_zTjweg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
قاب زیبا از دواسطوره تاریخ فوتبال؛ واقعا هر دو بشدت دوست‌داشتنی و محبوبن. حداقل تو کانال خودمون برای این‌دو و تموم هواداران شون به شدت احترام‌قائلیم و تموم امار و ارقام و ویدیوهاشون رو به‌یک اندازه پوشش میدیم که سوتفاهمی پیش نیاد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/24232" target="_blank">📅 20:13 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24231">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vV97mUvuBGNDuhqrHCVFx3Q9USCv78RywBJvJGTxqfEaOUaSwIQigj6euHDe_kf5h3NgnM5qXeg3MJw1QGcZjxRQGD3VTqU-cgUd5EC1CGHCl2IqKJHf56RZUa4VxylJuCV5XcVqjO9BrNTyXQ-VAQ6DntGE37Uc9l09B1VTeITsFAZHHmeU0sg_oefj70WH0rjhZU0dWV1JnC2Lb3x6prgjLj81Xb9piBNUaBZY5EzVtofgKZ8OMzuO9etof0ZVsB02MFDDZy-YGjY-muQQPXyCJc3N7OPN-lHd1BEpD-5qzILS8vtq0Snm0fqtXOoXpWfPHqFPyuSOQsi3QWMtvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه‌کامل‌دیدارهای هفته سوم رقابت های جام جهانی؛ عین برق و باد دو هفته گذشت. یه چشم بهم بزنیم میرسیم به بازی فینال و اتمام رقابت ها.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/24231" target="_blank">📅 19:57 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24230">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ab_dq4oCteske_wVVqmcV64T9zMxK485luf7aptUznfunATrz8Ig92on5lkywbiZLogtgU7wuqGOgDqafNOL3ba32sE3ExT-3iIgYGiZq1mTNuAjOrFX_d_4-Elt0gM8uDLOOWTlY99bLnTg4Wfy6oJDulFdye-qr9sxxjUWMIfCpagPVwkZXfkhi1q97fbz10hvMWUTGgqU26hnrfy88tEHKZT01v-yXXNg7EnHnJPDjHvC3wpAdy5N3IIzhFWu9m2mBcnk7bnoEG84xlqq0sU2foadWVUm4pFvwEDUrA9Ol5aQ6U7756c_kV1KbQgjSGKWvC01K5Sso4mtm8CiDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
#نقل‌وانتقالات؛ آلخاندرو گریمالدو مدافع چپ 30 بایرلورکورن با عقدقراردادی سه ساله به اتلتیکو مادرید پیوست: هزینه این انتقال 10 میلیون یورو.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/24230" target="_blank">📅 19:41 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24229">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BkZW4EIAPGtMBAJdk60RAjxDsm5Knc57yhWEhh10EvH6BgVhKNpW7CZGk2KUFP4gRjafWdf3f2E0ODcKH10VM6Gk_EQ6y0hO5cdP49FCCt9ESzLOe8WW1t_opWSSRsPxIRekG-fNQjtHct84CjDsnkTWMyvtNutV9cnxXm7taLSRcpYscjzglRI026bRPdI0IhVdSJy6eTMUQ41uFmZ36bgPj9VOfnEAmcnwbxzO54QEzFdNojSNba3Pxwq_s6sOS0cqRYv8i40mgBzBLWOkXL4NQgE2wfoSh0bFmxVIZG94_6KTG7j2JNUh8XqOSu9F1LuDysURw7ilu3VEZOLdWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇬🇭
مصاحبه جدید جادوگر تیم‌ملی غنا: در بازی باکرواسی‌تمرکزم رو اینه که گلر تیم ملی کرواسی رو طلسم کنم که تمرکزکافی‌ برای این بازی نداشته باشه. صعود تیم‌ملی غنا به مرحله بعدی نهایی شده اما اگه کرواسی رو ببریم میتونیم صدرنشین صعود کنیم.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/24229" target="_blank">📅 19:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24228">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KDws9Ln96Sj8HbuXvbEQQDKx1rHLtYVcgR_DkyoajcSiqTD7ZG4TD9jQKaTCt1zvIiM9EluBYUP20PIjWtvGlVQnwV1AmQhAtrQpuYqIyjiQ8bsnxfzwIk1L7VpjnmpyjhuQebL4W_qqodsj1WcB0kJIkhJlW3YyMnnttvnwlwUDXd_KSmY5UVN5BYC5kP8uHcnCce_G4LNkCfkK2LyU42_LSfNlDlJlY97Sn7ZkL_R5N4rk1XCMLyw6rDuK4FVUWPzYUOKzVFU0kkXoCup4fQSbBOxNnHI8IVzGnkYn6t91RXjWOkr97OueI5cWy36Otk4YHa0KcsKYogphHyiCvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇬🇭
مصاحبه جدید جادوگر تیم‌ملی غنا: در بازی باکرواسی‌تمرکزم رو اینه که گلر تیم ملی کرواسی رو طلسم کنم که تمرکزکافی‌ برای این بازی نداشته باشه. صعود تیم‌ملی غنا به مرحله بعدی نهایی شده اما اگه کرواسی رو ببریم میتونیم صدرنشین صعود کنیم.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/24228" target="_blank">📅 19:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24227">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H9yso_zKFB_RI_aUW2k2rtA1Z5Nd7dkQJ_bgk48DNbnW8IbvOemmiWNBSI-RGlr6AF6SfObEdUoiRCpims7BNhUUYT4j2V-S_O0mX5sWI-ejPDur-hNatUZI5K7thQuM6QRnPmN2eLfwt0oH4l3vmHAluOdA_RdDMkQMXQJOs1nHYQOhoGrjVJgEFtdM8gSOkZfZDMlROGfjpbxy1TKwmVEg3xDFA-Jq6NcDeGgONNSPKVNHUMrpDt-3uJDVHgjHcy_zWxEQJMTbao7XG4H7e4YIezZBheLVL77Foak5Dynd85_Ntj3FyZu5JBHDWgf7YcZ0ETrJvqsBzJ-toN0x-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علیرضابیرانوند گلرتیم‌ایران در رتبه دوم بهترین دروازه‌‌بانان دوردوم‌مرحله‌گروهی جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/24227" target="_blank">📅 19:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24226">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc38571967.mp4?token=k62wvJXr2VFACmC1Nc2KNvt7XraUxkPEYux5CLlw417ulD_WXYFvF-0eDUksntN0Hex8H3yx3v6oaPyTPIcb-fO0PUbShCEIB2V9NiF1DFfplxPTRBSrzxDc88cTM5Zqs8V5-yXlohSGzp7ipXeX3o3wh6kBSaB3VUAWMQk_MlN1gbgE-J9hj5O-826meScycP6jTvnw5AFSodueNkTm4Ary-ec-MwKgBLcLd2W26KEHZfvs8ASWp6L_qmLJVgEploBAYbqIdi2QoFs2qFVkAz_Bm4lZX88LgVM0maWsL8JG2WN0KWwaDEnf5j1Fw-UO2mLkMN-rXuMibo3Ok1Qmjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc38571967.mp4?token=k62wvJXr2VFACmC1Nc2KNvt7XraUxkPEYux5CLlw417ulD_WXYFvF-0eDUksntN0Hex8H3yx3v6oaPyTPIcb-fO0PUbShCEIB2V9NiF1DFfplxPTRBSrzxDc88cTM5Zqs8V5-yXlohSGzp7ipXeX3o3wh6kBSaB3VUAWMQk_MlN1gbgE-J9hj5O-826meScycP6jTvnw5AFSodueNkTm4Ary-ec-MwKgBLcLd2W26KEHZfvs8ASWp6L_qmLJVgEploBAYbqIdi2QoFs2qFVkAz_Bm4lZX88LgVM0maWsL8JG2WN0KWwaDEnf5j1Fw-UO2mLkMN-rXuMibo3Ok1Qmjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
۹ فکت‌شگفت‌انگیز ازکشور‌های‌جهانکه‌کمتر کسی میدونه؛
دوست داشتید تو کدوم کشور میبودید؟
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/24226" target="_blank">📅 19:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24225">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/t0XYFhYD25v1VaG5UrFRvnbcTX1LIcEXIZ4ls5n5vCVKthGTdQs0PHxKAwdZelzor3MaCH7ZnoaF3M3pS7XYgx9pdxHwrBXnSVn3UyRggzTQzzCXi5XPixrpVx0getItisToKyqM0U2r_uVOX_1nN_o4JDpT3Jizq56AIXxNFEmmiaegBpsICzzHu1KaVVb3t0yKdZOk3XyZMjFFHdbL9tTg0HQjfrbeHfhkEnV9Jo5B8X10mCA0o_i1XnD8HBQZtjIpvgRSR-5Ebd-X5HgeTxJsuLD3wlm919fY_e-p99gz6g7bOvqOekb2Aup9KI6lMMQ5nsz4fJeWODEbJUktnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😮
جذابیت‌پیشبینی‌مسابقات‌جام‌جهانی را با بونوس های لنز بت تجربه کن
🔄
☄️
بونوس خوش آمدگویی
🔤
0️⃣
0️⃣
2️⃣
💯
بونوس روزانه ورزشی
🔣
0️⃣
0️⃣
1️⃣
💯
بونوس کازینو
🔤
0️⃣
0️⃣
1️⃣
🔒
کد هدیه چرخش رایگان بعد از اولین واریز
🎁
📣
بونوسهای‌باورنکردنی‌لویالتی امتیاز وفاداری برای کاربران فعال سایت
💱
کش بک هفتگی
🔤
0️⃣
3️⃣
💳
کارت به کارت آنلاین و تمامی ارزهای دیجیتال
💬
🪙
واریز و برداشت آنی جوایز 3
👛
📱
@
lenzbet_official
🌐
https://www.lenzbet.cloud</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/24225" target="_blank">📅 19:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24224">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0eb571605b.mp4?token=i-mHdhIKqr-vZXrbRJfrhFoCTRA0cK0Pzua3LEQtH3y_6J4ofyPRgENRBG4HFrc_oRIN91bc52ccRn2SjEgckAOq-HDaCU_Qq7aFWbdVNG1Hx5EkUfTZ8gduupESj4Nh6IzcohKz26jnNTVfiWFGGVuM015XTa7zngTHqpix8tEVRME_FisnNCCm3fwHtef7JvWVHRqh5nPRXPtSmTKr5BMZWp-EDuogkOVNTLdA5BY57TdCr_JcdyLRZKWfnlTMvqwUuf600KneaNpBq_pMnC6RddymdvNpCEki66d7YRdadbpB0jg8lJFr5kDWJGJgWm5WV9vJold4g_OYo6fxnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0eb571605b.mp4?token=i-mHdhIKqr-vZXrbRJfrhFoCTRA0cK0Pzua3LEQtH3y_6J4ofyPRgENRBG4HFrc_oRIN91bc52ccRn2SjEgckAOq-HDaCU_Qq7aFWbdVNG1Hx5EkUfTZ8gduupESj4Nh6IzcohKz26jnNTVfiWFGGVuM015XTa7zngTHqpix8tEVRME_FisnNCCm3fwHtef7JvWVHRqh5nPRXPtSmTKr5BMZWp-EDuogkOVNTLdA5BY57TdCr_JcdyLRZKWfnlTMvqwUuf600KneaNpBq_pMnC6RddymdvNpCEki66d7YRdadbpB0jg8lJFr5kDWJGJgWm5WV9vJold4g_OYo6fxnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
دیگو دالوت درحمایت‌از رونالدو کاپیتان تیم ملی پرتغال: "فکر می‌کنم دیگه همه بدون کریستیانو چقدر توی کنار اومدن با انتقادها مهارت داره‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/24224" target="_blank">📅 18:47 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24222">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L8GrtOrmmygCDvXfbFSknnmOjzHcmCo3piyQoo5D4l4gr1-ZZQ6owHGtKj5uSfywAnm18D3D_P-nF1t7rqESbOm6AToq_6tTD_vKbaZBbjEXzFD5Vmv7hpUziNJpGESI5-yykAGXtg2gGh5RTkPNNmyE3klVLiY7EL0lhAuJ0ga7Ih8zK_m6lOkJSKFvt99X7yssdtZMiYc9m48i0zi8nDM6tl8tuk68TU3TtHGW_N-llVuROJHiAM09F5L1J1s-yT1Vztw8kYi19KUgJWhk4rF20a5bCXxHsaKYr11_1cFQg-1KNhnb8D5bWaxaMeBol-wze3PjivZs1UAj9FGlkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mpj57wUDhukG5myY9N-7mFR6CI9M7r0pqypDGFArMTQDZ_f3wNGOCNS8tfs1KYSI40WjLSsZvNk0rYRdyIqcBfBhxI8xkKgr4WNbqEE8mjIFzq3pqbfR9wuo_9mENU19oOWJTU69u86oCLZ_XxiJRGUknNMzDaM3L6p8CPGGnzRo4FX20fdMDXM06SWwCB1nquiTYNzHwckmy7eH5zSZerJCGeR9c9Hu_o0WbKOvgVKEXMYBOyL5P9-SEhXd3ORNlQYRhlUMb9ZH3i7JrdWpUc6eXLKVjxRjvZDzLMF15PeGFBaU9i4GDAtO74nst5vkmuTOCXKge_EmaOL4MFjEqg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇲🇦
این هوادار تیم ملی مراکش گفته که تیم ملی مراکش به فینال جام جهانی راه پیدا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/24222" target="_blank">📅 18:34 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24221">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e9UcZYkQxCMo2QBoj3dDEbgj1K2ulXsE3_w5uD8x-iS_xNTR9KO9-pwusaUhl1MUWMxG18Cxs_KFNq5lHNNz9OJQEiQ2vuEoofsLFjLy0CowuOd9am9PQ-EZ8QEHIUn3BIF7cijDzL5Aj5mFEPYq-ab_wZfiERQezVcqEXbFzGyvNhxuoSH0hE2fZ39ojjlbFS7ynZNBzlhIBNF4RyKeVnQuP5lnbLRW9UliQs2zaQNu49e3w1BcgUFh1W_fygwrDQnavpdt0jjAFwGpx_csOnPAsdSLKdOu2rsvktBMjVRTUGa2Hl8hKx1crbGv5CDIKHKJKf24z-Em2V0KsBdNag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇦🇷
باشگاه چلسی: انزو فرناندز بارها اعلام کرده که قصد داره بعد از جام جهانی به رئال مارید بره. ما مشکلی برای این انتقال نداریم. با باشگاه رئال مادرید به توافق برسیم بند فسخ انزو رو فعال میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/24221" target="_blank">📅 18:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24220">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EbZpHEBQ8Lj4YNuGvBLWQda8JoOwjnigYObl4VPA7vZ76G9viBF467gAwFsXKfezTDGA_lzDYPFG77dcjcFHWV7Y0mM29tMN2Nd2Y0Rx3wuArSV7eBmcWBMCnbkvw_LjL4qMPMLNljes8_2kLhxBv2lLVy4Hm_xMKg-h7Jw9Jx6kopRnePXOCkT-rcckiY9fITQWnoGS8i_MXpXBOnKy2swl2jNi1DwvguAL8a99IsMgy65wp8BY6OK3ZffUR5YNdGLxO6qi2g6h7juOKBGWTSyzdesn4ZHspwcvlPFZhhLX14PTLaQpaDiFuaOJFe56RnU63iCw8HPDEfBfK3JGsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌های رسانه پرشیانا؛ درصورتیکه اتفاق غیرمنتظره‌ای‌رخ‌ندهد و اوضاع‌کشور آروم باشه منیر الحدادی و یاسر آسانی هفته‌اول تیرماه به تهران خواهند آمد و به تمرینات آبی پوشان اضافه میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/24220" target="_blank">📅 17:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24219">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZoAYBz5PuS-E27DFjhlfwXXsZwN7gyeTL2eQEbtSuIkjElaNu97kbjkV93yGNukx80vzT30pSBNRc8N183a8m3INFsKU3gHJvGB6GdO1G7VUVdUw4Ths-9ZobiFKyzcEbsAXSQ6pzuGulg6bQb5r5cvG776yXtuxqPre_Tks6MRpX48SqXQgipVaOmk_HehhCuACiIlZlYx7je9OZCzevJmRvdhZCA76xOQps1_kQt91udN40C4sCXZxSC0_DraS4cB1RU7dzGH1eid-6dW59GgM_yLJctWuQ7C1o5YwyjKZvWQmlhOI4kk1EQhc1pxhrg06dVHL4Evbk3-uKC8C1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علیرضابیرانوند گلرتیم‌ایران در رتبه دوم بهترین دروازه‌‌بانان دوردوم‌مرحله‌گروهی جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/24219" target="_blank">📅 17:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24218">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ui31TouETTXkQRCkVkM7bZA96h53Gky-jqvP87CApd2UopAZMyozefAmSiN8EbnHofIYL-regDhulgDIsFOCAB_tUdqseW7iVt7I_KOD_qNMWA6YLMqOgY4Pd3Z78_nvgsHAlBkdrbmQ3_18yy_xZc9TmmTwELGPHVQlAbEH24rtKefdw5lXP4xIdOvOzh0O-DYn20BGZ75xQcCc8uM_7Qv_ye-_YzBPgxUG705fR2lp995JTffT6Of_pBcHDCKwRb8hY1h5PgMz9toCTftGXwI51krsaJMLIoM4qlYeu9MI3-BPgEQLdVKwBfz_sq_GajtQBLVGpCxAssnipZHQrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
علیرضا فغانی اسطوره‌داوری‌فوتبال ایران به عنوان داور بازی جذاب کلمبیا و پرتغال انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/24218" target="_blank">📅 17:30 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24217">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YH3kQ21eubwX-WsEpjC3gnBUWWXyWdR_wfraExZG5fpWEXSCE0p8rIxZQoZ5zdltPaH4z-vSnpw6I0KAx_UzeDbxFAI1X1vs9Rt9c1MXKJ_DTQaS6KT3A2VsD4_eCeBPk2HiUEB2ckd9dKKeNk9mgmrrQIFdAJ1bRadiJex9E2oyAyq9LWo9QGSIk1jHsBxP-n98_q_w3l98dJeyWmJiia3AbZ1m34fSLB4_urpa-awOA506yeHjLRncNGswJ16xXiZGu_TYDjC51e65uJ5q_nzZ8-GcrU7r0kRNOrrQ1WPDDkFKm1Y_DKJRZ7BrzNVye2GUQ1hArjDTYZepMBgL7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جادوگر تیم‌ملی‌غنا: گفته بودم که اجازه نمیدم امشب هری‌کین موثرمواقعگشود. همین تیم انگلیس دوره قبلی‌شش تا به‌تیم ایرانِ کی روش زده بود اما امشب حتی نتونستن به بار دروازه مارو باز کنند. به کی روش بابت صعود تیمش تبریک میگم. هدف غنا حضور در جمع هشت تیم برتر…</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/24217" target="_blank">📅 16:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24215">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q5FyqXFPftIun-oiTQXR256wvOplQtRtQUMxdCXA_V3D42CZmjSWXQGsFsx3-kPQsnDRV3yDIX3bh-avDs8mdeBHoW54kiaTWfg1Ywp9Tju0jBTpolcd-WSL01uvdbxUQsdsry5XaameVsYU5wSgI89dvgGYv6dOD8yIwGF6C5LT-xX23Nd4lrw537t6pUh8XG7ATEGpOG-cUHS6-j041UFUZQoL4vHMFOVFJo5F0Q6WZnt4iN0Wimzy3gurIDAUefHGeK3ZUscy85ApU-YpZGnOkKCRt4yiB8l-R5KvlfyaDC_z12CQEpix_IZ5hmcdWN9pMcBl3YRZ7-Fa7KBHCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DDLN_Xdf-tZ9K5HwkUCdXJKlt7FT0mkI1nQoZn5eaMRI20E-hKE_AMR8xyFGlwQEIN8yic-8wzqbL-pjM-mJ19ckvnYDhp10kZibz9m1PLGiIC9iD1W5qZYCppwb40gtCG5b4CoDV6SYTRvo4SiKJqhSbKWsaLzm6XE4KC4sKQbB1cHLb16dERTJbfQZcEGtTXOVg4BnvVXmBQQdt37gF30X_hU4LUM1KF3UUSDAv9BjJptqGki3oRppnu17MeMe_SKnquvwLcSucW093SygLlRNkK5zfuBhlajesiKpT99EMxOf1spyk4yYB8Lpao0orZFbPzR0B69HrqbpetTVbA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇲🇦
این هوادار تیم ملی مراکش گفته که تیم ملی مراکش به فینال جام جهانی راه پیدا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/24215" target="_blank">📅 16:10 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24214">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a79050b237.mp4?token=Jija6moQC-9ZzKesACm05zi4kDbucYUFTo-TUMHVfcE7ECjS2fvydwPequVR7gmHLGPlEUgS9mQfrauFBdzxtx1EBmMuEOmzA_kDvMUx1aSCYq1Sm0Qctl6g9Uaej4i4klpz69jpP-WIlh2dLXY7DHs2y3xOSwK-1pVeQhMUC0eRZnz-FIqByHnlzHsWjJWHotpP--KS6MZylfj6_xHo-WuKyPRteKcaqPq8ptpehclPtvKqVkeHgaP_xI2jDX4FX6ecm5MsBe9Hdcqh9fXPfok9CCcYAyQtXSmNFpneSiB519gH_QUBC6ZQscY1VTRKa0OTEvJC8bhpy2gQay-IIIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a79050b237.mp4?token=Jija6moQC-9ZzKesACm05zi4kDbucYUFTo-TUMHVfcE7ECjS2fvydwPequVR7gmHLGPlEUgS9mQfrauFBdzxtx1EBmMuEOmzA_kDvMUx1aSCYq1Sm0Qctl6g9Uaej4i4klpz69jpP-WIlh2dLXY7DHs2y3xOSwK-1pVeQhMUC0eRZnz-FIqByHnlzHsWjJWHotpP--KS6MZylfj6_xHo-WuKyPRteKcaqPq8ptpehclPtvKqVkeHgaP_xI2jDX4FX6ecm5MsBe9Hdcqh9fXPfok9CCcYAyQtXSmNFpneSiB519gH_QUBC6ZQscY1VTRKa0OTEvJC8bhpy2gQay-IIIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
ویدیویی از تمرینات لیونل مسی 39 ساله
؛ نکته جالب ویدیواینه که تو هر بخش آقای رودریگو دی‌پائول فقط چند قدم با لئو فاصله داره.
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/24214" target="_blank">📅 15:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24213">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ma59HwYhNApqJgd1k9xnD9HILpnQVZK_ENCDDnciJyT5QRfBPrlAFQ6vMaBVmM_TzZ5uNFBPYBGdQ0ByD5AxNQyHje63CVHYIENJeH089wOlfz9ex6a6WGOdus2Ymvgd37Y04J9oFz_Bwg50LDA8__9tERezPyCWLs7OHxI7D-0e74f-JRo7MfKC3uvImD55FnWW5e4nsg0llAagpfi_M0EN-4VRDrUVNpNpnRieAviZlVwqzfqkKIXPE0Koti85FuS-l6qP4UrpQx6_BTbMfBBmACAz7QCA42UiNHVaD3twpg8oiGADSQoPHYIqG-h3MBzTP2egjI1j2t4rcWJz7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌ های پرشیانا؛ سیاست باشگاه استقلال در این پنجره نقل و انتقالات جذب بازیکنان جوان ایرانیه تا درصورت وقوع جنگ در وسط فصل اسکواد این تیم خالی نشود. در بین بازیکنان خارجی رستم آشورماتف، جلال ماشاریپوف، مونیر الحدادی، اندونگ و یاسر آسانی در تیم ماندنی…</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/24213" target="_blank">📅 15:41 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24212">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SX3raj7ImNzmZ_PsWq90qlpW8dGhHKNveg013BjaJVKYEZzahD6-uvlcKn4n_zI51r03nZ2HBiYQPdA2rrRN_ZZuiuywUwLtXQnJz9kK-wR8Hx8jammYc_OqndxsJZSlZ5GvGevCfDrtcEieNqXVcayXtQJK6hH7_OHrR4mBvWTbVlFiwL_qF-PCPrgus24sjh2Yd2GfAgqm1kuJE2Q-L3plsGLLw0_LCdU4Macu57BtgnmeYlr0NgsdkE117v7ddqQfi-CqcoiB2l_VPqMmMT0Eiu4CvqtRZeW4OAVDQVMazSrVMLUDODWiSuvhCAsakRAyL-LvSVvpZx8AdChLnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
مسابقه امشب والیبال تیم های ایران و فرانسه به صورت زنده‌ازشبکه‌پرشیانا 3 در یاهست پخش میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/24212" target="_blank">📅 15:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24211">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fIJORollKbTrcqGIpWuY6fJld-Q6xuGn8wGdV00emnJuADfFvOYRQCcOq1HvK84GYTlch9S-LHMwbhkLyKUlxV8-vmwEGIcKPnD6fSG3D8eAq6f2QP4PGz_2lIjzqjpj9ymO1bLbGKtI0pZMM0AW2JIpyurusmswmR5Qwt7QytRm0xOpcHGRaOIBRo9LmwrlyLB5Et8gtVRhdPnFG0jhGaKmLLMUwZmPpgqXKhFKa1Djnm7doeYcplKBACh3SbsAd9B2f-CVcxgYbTV6COXOjmzNzWJmjdOYSqkzwXeN8KTgz7JhSwZEQG02-7WpcXe3NTwJUjFHbam2K2SDK6JrMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیم‌هایی‌که‌تاالان بازیکناشون دوبار بهترین بازیکن زمین انتخاب شدند؛ از ایران رضاییان و علی بیرانوند نفری یک بار جایزه بهترین بازیکن زمین رو گرفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/24211" target="_blank">📅 15:18 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24210">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n6zYuwE6rNHkbhgzT9JKHePSq4POJYFZi1DVfIJcPQyEc26UxODRN29kT5OyFWVwZS-2iNcc3ae-1wU5gVvsZFwGJXq1l39b5r2c1sm3JK3CX4ApMPBlOZFLZaGG6i8T2-4B86d6T-Aso2KZz1sfRKrqPzTQjTyzKMvs8lElzK2T2HPy5qfBKdzqOma-tkM1WoWH_AlWGiC8Tky2EzM0xFzd3ND5xAE5I5S0Jp7O3GXO2tkyk4FEk9i4AlJTevZFOLJCYfhswz5cVRKskfufNZpKCu_ZTmMQNW2wJ7KfVMHg1BTiCiadYWLDR-37afsyCX-xbIDyx9o5D2hv47UOuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ تا دقایقی دیگر جلسه بین مدیران باشگاه پرسپولیس و اوسمار ویرا برگزار خواهد شد. تابرای فسخ قرارداد دوطرفه به توافق کامل برسند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/24210" target="_blank">📅 15:06 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24209">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tar-3hgazk4MAXgVwojBvrQWwK4zwg5lihl88AnsZufcixVICfL1TS8k74uUhnbvOjiXs-CmNDmd4tu8yzL-MPHCykrf7HjcV6XAlZQKxE2zpHKVTgR64N20cA5Lf01eGvgkM86qBe46kOKA7cTi314LwScJ49D41dmPixDQxt8HLj7nYp4TUKEqxhTER0CflXq91-wg7lg863sSRFfli-Qh5Qemr0oLTU-asrY_AFW0n9d-UEJhcNtkgv1K1Efb_baw2cisd9QDlLpJOTrbL7FIAHvMjr4ztZHVR3L-BSxgYUIUmDPz7mTRo5_jX_MolNBdjyJWb6ECYmb7kTEgjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👤
مهدی طارمی کاپیتان‌تیم ایران:
بزرگ‌ ترین شادی صعود به‌ مرحله‌ حذفی جام‌جهانی این‌ست که مردم ایران به هم نزدیک‌تر می‌شوند. اتحاد و همدلی بین مردم داخل و خارج از کشور برای من از هر چیز دیگری مهم‌تر است برای رسیدن به یک هدف.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/24209" target="_blank">📅 14:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24208">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sx6UrA00w_2YnBXu4z-D6SSlAVgtkoesDE2MbCHBFYyqfkadxt0_fsYAuqZn5uV3mwJLJghBvVrj8hSRkgMqSl8sPoWrYDLxvVRumGPGuLE3EmT1w2vwwyf8Sb7jfQNLVlrU6G_5tXVgFR3hJgAeJ7HGqJE_YtTlXhWIFU4DPVKv6zRGOfq_GUPS1IdwBBXes1ebAoz44ErhsLzdTQhibPht_puMVpiUo2UbM-6x7WuhP7yW9zj5FG10lQTfryWsBSkwHl-u0oEmnkonR-8F_yhH0mdzvuhmIBP7IMYKNNo-f1ElhrNXG9ok5urgl9trvXbTvyWOxMf2mcVTkxdDBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
هلدینگ خلیج فارس و باشگاه استقلال برای پرونده بازشدن پنجره نقل و انتقالاتی آبی‌ها روی هم 850 هزار دلار هزینه کرده اند. وکیل ایتالیایی آبی‌ها هم‌امروز ظهر ایمیل جدید به باشگاه فرستاده و گفته شما تموم کارهای‌نقل‌وانتقالاتی‌خودتون روانجام بدید فیفا پنجره نقل‌وانتقالاتی…</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/24208" target="_blank">📅 14:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24206">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a203ff625.mp4?token=M0JdXjqJ8qXgZR13h4xbtXsd9eq8Zcp_Q_XXc3VKAA0Mq8xydtFdrjKhmtaZRbUxMKCdxDx1LGn7jlTz5pCkKxmJCLl-eXYsqpkVl8jyK0VS43TMolcJg-PPcqrR6g_maX54zw_YEDLdKSVa_-eYb_KzcTP0bSLzJm3eknCSE2XefopYwu2G0GKCZZ8quZl2IyuuXtqnUS3MW2QP87rbJZY3eVv5cZnRO-6ZwgACv8UhB-rvg2EI97IN0yrNQf1D0aG3nxrHDQbWD8aXtp7Y_j5HTdOatBVyq7wCsb9Vj6eFV81TEj-Rba1a7xUEZFL_LgO3V-JcaIY5UVz2z_i3tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a203ff625.mp4?token=M0JdXjqJ8qXgZR13h4xbtXsd9eq8Zcp_Q_XXc3VKAA0Mq8xydtFdrjKhmtaZRbUxMKCdxDx1LGn7jlTz5pCkKxmJCLl-eXYsqpkVl8jyK0VS43TMolcJg-PPcqrR6g_maX54zw_YEDLdKSVa_-eYb_KzcTP0bSLzJm3eknCSE2XefopYwu2G0GKCZZ8quZl2IyuuXtqnUS3MW2QP87rbJZY3eVv5cZnRO-6ZwgACv8UhB-rvg2EI97IN0yrNQf1D0aG3nxrHDQbWD8aXtp7Y_j5HTdOatBVyq7wCsb9Vj6eFV81TEj-Rba1a7xUEZFL_LgO3V-JcaIY5UVz2z_i3tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دخترای‌مکزیکی‌انگار خیلی با پسرای کره‌‌ای حال میکنند؛ هر کدومشون یه پسر کره‌ ای پیدا میکنه یه ماچش میکنه. ببینید چیکار میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24206" target="_blank">📅 14:16 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24205">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cf62dd03e.mp4?token=IpBIME00sgklUb1L0QQPOtvWnDErWpG8q-XsgW3DgZNSmg--hNlcKsiMnv-crqfHG_jiRPupIXbUGrl4OJt_5Ppfd8EwVaaoZnPaWSUuSMXy6m4LvrzhPHNKyjDJdHJ7DMoMtdp7XAk_wo22TiJxykOBSncmqZ8YcQb7EZvnGUUqDPCUyTobOLdGnaboAnVWucUvxYmm5tNH7NCpCjRLJSjd_U1w1ausscW3x-ogrrI88XjSeg3v4WVz9eqyxljGu10aNX8BslymVGlcVbRA95hMr1CytFQepwXqeokAUNt4MkdChTID3StlmmHCHX90MYWdAp2cWJ-FZtC0sm4iGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cf62dd03e.mp4?token=IpBIME00sgklUb1L0QQPOtvWnDErWpG8q-XsgW3DgZNSmg--hNlcKsiMnv-crqfHG_jiRPupIXbUGrl4OJt_5Ppfd8EwVaaoZnPaWSUuSMXy6m4LvrzhPHNKyjDJdHJ7DMoMtdp7XAk_wo22TiJxykOBSncmqZ8YcQb7EZvnGUUqDPCUyTobOLdGnaboAnVWucUvxYmm5tNH7NCpCjRLJSjd_U1w1ausscW3x-ogrrI88XjSeg3v4WVz9eqyxljGu10aNX8BslymVGlcVbRA95hMr1CytFQepwXqeokAUNt4MkdChTID3StlmmHCHX90MYWdAp2cWJ-FZtC0sm4iGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کلیپ بسیار سمی که صداسینا پخش کرد اینقدر سطح ریدمان بالا بود که از آرشیوم حذفش کردند.
🔴
از سر راه کنار برید ایرانیا رسیدن...
🔴
علی بیرو توی دروازه یا که نیازمند
🔴
کنارش شجاع و کنعانی میشن پدافند
🔴
تنگه ی هرمز ما تو دستای سعیده
🔴
شوتای قدوس و رامین مثل خیبر شکن
🔴
مستقیم به قلب دروازه ی دشمن میرن
🔴
ترابی دریبل زنه، نعمتی هم حامیشه!!!!
🔴
مثل هایپرسونیک از لای دفاع رد میشه
🔴
یه طرف میلاد و از یه طرفم جهانبخش
🔴
پهپاد شاهینو رو دروازه ها میکنن پخش
🔴
حاج صفی، حردانی و یوسفی مثل شیرن
🔴
توپای علیپور از پاتریوت هم درمیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/24205" target="_blank">📅 13:48 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24204">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/plHpezoSy-eTR28zRXS-bf7FyMz89z3uMqpD_W_kHm7CdHmaaGvqjr_3Q4MIuZWLOSkDqmyTPE3or7B-UvzGkch_D1pjJ8NDm0pApcNjSUlvQGa8Ev56yywJOSfvTF7Zocpd5RZQXsUOUK2GbEQ_9zbh47pWtKedsMoMCd1EVpxloQt1fF9WoX0HvVYpzGl2tWejG8m9wr7eBQpn3ZUYT_9fQw65RVHacMOJe4JvLYQRLGKx2RYISdqdPP9GzEZKtJdTfFeTxFHta_r3EltpVtq1Zumtibw0p30N7VkM6MHV02E9p4mMkaDbF6jJ3YORmznWkYDYa7d9dvNvYM2vfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
پس از پیروزی پرگل 5 بر صفر شب گذشته پرتغال مقابل ازبکستان در جام جهانی 2026؛ پست اینستاگرامی رونالدو بعد از گل اول او  به ازبکستان تنها در هشت دقیقه دو میلیون لایک گرفت.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/24204" target="_blank">📅 13:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24203">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rh16nR51Z5RtgBS2Xm5noZORI1dHK3djEXyPHwaUkefD-suH_ZQx8LkifCrK2WuHGnr3ylF7fxXOXpsQWaawxTPs9kfBQjFG4FEQYvxiN7ti0zDax4WGYgPNPDnNgkw2c0Zh-DjU3Zqu6BrEgyvDMnUtmVqgU91jdz0OJwAa4QL1DJDd8MVY5H9pbGgjFnSLrO5atiUSCSpYHFq09wGsXol8sOw4tK0awPjJWc5vMyO-xKQCy0zZtg3Z0ugWVVE1_L_z9J_jbc6drL2sjFGvmQsP3fVo1csYe1FTW5R-9_fxvpycRAQIgfUMIJBdvOMB11fg3eUfH4lUJdX-TR7yIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
موتورگلزنی فوق‌ستاره پرتغالی فوتبال جهان روشن شد؛ گل‌دیدنیCR7 در 40 سالگی به ازبکستان درجام‌جهانی؛ رونالدو به‌اولین بازیکن تاریخ تبدیل شد که در شش جام جهانی پیاپی موفق به گلزنی میشود. این نهمین گل CR7 در تاریخ جام جهانی فوتبال بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/24203" target="_blank">📅 13:06 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24202">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z113hzlA0zSCAbw9D0RPwBQfZl0gqx_vJfG-b7xu4osZLV-ZSA4MMPCKzanaDK5ScOJlu4sr3GozcO8JMOHpvX4ER2ZQNmbqkmSrlvRn7koPbgLXA_qy5d5RfA79GdsV2thMyB8KVs1fVusnF1KbwkjcNFTzXEovAv0LWE6xdtyJx-WAjxwKKTBuH0pcAAjbrMcOoqz9pvbGnGlbTCCqbmD4TRpKOJNg3-ZMvKV4S7SIVMVpwt0I7gb9_yc_aNLeNxaPI_CG4KIXKvsKZKCWwwUWf6ztnd3WeCApa3cL7p-CAZ1ptm9uYX6s8o2gsmfFDgW3cPRTe0yBFlx5ZvLk7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
پردرآمدترین سرمربیان حاضر در رقابت‌های جام جهانی 2026؛ سرمربی‌ایتالیایی سابق رئال در صدر.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/24202" target="_blank">📅 12:47 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24200">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DOAFvCSov1UGyYi_YxtBzF8GIsWfiy7Mjk4YLUyjg7KPiJzi43L9Jq5_15-fLqpi0HMN5JVSvsNFjBSke2aKOiInkJPr52M0YEbuB7twaoi2xIbyDeAB6llJziVPq7GUCK4xXCOQ_IYrbb3xkDK2K08G5KZHmcoBRmsMMnmqav2TygmtkIk0OSa-C3PNZ5xkRTBTt9PB_rl5336r3gtaY3O71pyNo2GiFQafPKiJMOFB8oKi45zQMDjI93_pwOcglSRxI0s2jRKLAH1X73I51tfwSuur8pQQiEgmiHAIfmW-gMC9Rg26flB4Tg6-gKPalJNaWe4gorHsxy0U8h6t9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d824e9cab0.mp4?token=EV3v5P0wat3ZgIH4z26Dj4SunRL1NhVRIC_3mVCosawOfNTIQpdE8WYaU9_ad-LC56hIzqM-mEILAlodE8G7fOKXEpMOlBAIwDSGzGJ1J05hNlPzpa20_EVrfxuwSATqPhdSkTfIagmu5_EC19QTC_lpwCNw4OccU8sFz0FuzYFz-1djSDUo_2C7c0voOzWQXlVVB3SYM7Cu-x-SW3r_BG_9jWsdIAanLsnSI2Y5rmpnNb0PbB_Rk8_Ar4eWxTsvxLNcIKDFu26h2cd_92e2aaCv_YRgzDAC2NyYh2v9wBXDJy5WXPGXsdqKlPVXdCXGjAj1sJFumextdMUdXNvrMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d824e9cab0.mp4?token=EV3v5P0wat3ZgIH4z26Dj4SunRL1NhVRIC_3mVCosawOfNTIQpdE8WYaU9_ad-LC56hIzqM-mEILAlodE8G7fOKXEpMOlBAIwDSGzGJ1J05hNlPzpa20_EVrfxuwSATqPhdSkTfIagmu5_EC19QTC_lpwCNw4OccU8sFz0FuzYFz-1djSDUo_2C7c0voOzWQXlVVB3SYM7Cu-x-SW3r_BG_9jWsdIAanLsnSI2Y5rmpnNb0PbB_Rk8_Ar4eWxTsvxLNcIKDFu26h2cd_92e2aaCv_YRgzDAC2NyYh2v9wBXDJy5WXPGXsdqKlPVXdCXGjAj1sJFumextdMUdXNvrMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
اگه جدول رقابت‌ها همینجوری بمونه؛ پرتعال
🆚
آرژانتین در یک چهارم نهایی بهم خواهند خورد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/24200" target="_blank">📅 12:24 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24199">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XVu0QQY--GsppGxGlkfSchrsujK47OjyR0_mbDNUclonCX5mNkUbUSWkVaud0vrjNxG8VfWi6OTdSLGjwsOPNKig419-FVqNCpoWsdq_96fU5tFwqHgdlR1L20xUksxpStPEcK_8hcP_1Kpvqjc9oyk_zuLcbInhxas86CYVBauozAyvl4ghBF-VqSUhe_fwJd4j_-FBERVot4PSEd5k5EHOU_qkeugCiYK6PSP5OMH6lNrlECMXTgeO3JDf1fl_UZfX55fLMAyeFhNKrSBQf1hL6K4RaQgGqmWAeHRgZrQfU09i-J5RpkC41iF4nFapNuPsDxA28fUDUGNkWbxeBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
پردرآمدترین سرمربیان حاضر در رقابت‌های جام جهانی 2026؛ سرمربی‌ایتالیایی سابق رئال در صدر.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/24199" target="_blank">📅 11:58 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24198">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2111536884.mp4?token=DvyRurfZ_BAM-g1sSNMCeGqvnja_BWgZ6S2PBeREncGYaHPaC5BMvWRbKfwUB7SbKO52nqzyw8lkA0cVWYQ4cWXgbnBeF9yBHsq60KYmvcG3P9C3FwmRpMwWC1b8ncE-gnsETdSU6jqT4p5HVnrCs2qnlCF__qxiAnoUJqhmK4bl_D6I4ZznXr7s21z_yGvrkMeCjo1au7olBwbhJYB79loijBCFLd4j4KUil-whdJi_Ginxq5uKQWlvUy1OFodgWy8d_lrQBsdM-vt-VMvIzxVRdwQ8zNZtcMwV5n7oIfhmFfsQmktlQNslLqHIN6Hhm89lDB1wnyVua9jS-UTNoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2111536884.mp4?token=DvyRurfZ_BAM-g1sSNMCeGqvnja_BWgZ6S2PBeREncGYaHPaC5BMvWRbKfwUB7SbKO52nqzyw8lkA0cVWYQ4cWXgbnBeF9yBHsq60KYmvcG3P9C3FwmRpMwWC1b8ncE-gnsETdSU6jqT4p5HVnrCs2qnlCF__qxiAnoUJqhmK4bl_D6I4ZznXr7s21z_yGvrkMeCjo1au7olBwbhJYB79loijBCFLd4j4KUil-whdJi_Ginxq5uKQWlvUy1OFodgWy8d_lrQBsdM-vt-VMvIzxVRdwQ8zNZtcMwV5n7oIfhmFfsQmktlQNslLqHIN6Hhm89lDB1wnyVua9jS-UTNoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
ابوطالب‌حسینی‌شاهکاره؛
میگه تا بازی بعدی یه 6 7 سانت کم کنیم تا قهرمانی جام‌جهانی میریم.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/24198" target="_blank">📅 11:51 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24197">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👤
👤
جواد خیابانی محمد جواد رو گیر اورده بنده خدا دهنش رو سرویس کرده؛ عالیه ببینید
😂
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/24197" target="_blank">📅 11:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24196">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/voQ0nIGKLbrSE6hs50Mb92SYbe3rDCittD-8BE4y74GIowCSPGM-QaEBD2Dp-X1Z2aG9SVcVTTw5vtArS_YoC5wzc9uoQSE0L8nImBQEK8YQr1-xjKAC8eT9Q_gZRx1T0avpaOiRopZqhnOlfqgU_9UFZeTbz3q4iJnJfMn-tIfUehL2T3Ls8D12Oobccwx9CRmks-l8Li6GdwyIZwRT3yDvgvEobJlNMVYQbpNrTIkBOrW6HS3EzW7UpaQtZOKPx843BVgG6UIa4w9cc3bsaRkpZb4rvPEkGDoWe5Qz4oiT6v7PthlxHNdWyOW1iIqAzVg2ENkpy0Gq-NGfcMj2aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لیونل مسی اسطوره‌آرژانتینی فوتبال دنیا و باشگاه بارسلونا امشب 39 ساله شد؛ 1158 مسابقه، 916 گل زده، 414 پاس‌گل، هشت توپ طلا فوتبال جهان، قهرمانی ارزشمند در جام جهانی 2022.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/24196" target="_blank">📅 11:22 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24195">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61cf639d4b.mp4?token=YtJm0OsNSdKKBhJMMwitpJi6tc-TYGCgAlL23rcViUs7iF_WU7YSmZJzgMKfHt__JHOxaEIXQAuLJXSCC91Ua7UHASqCAsvbJSDUnyrBhpI9gtdw-FG2GseJBiVRudULwITvNvsap6tBjb023PnM-BgY5neANznDfrEcV_ogw_s0_VPoyPPfmp3IsRlnS4iMTJI0ocBjN9AyOyYDVx27HseT1jM4_yTHYZFHiSc9qwz_9jZVAeSQtQa3Wkh4yiFlXHHdh9Yzdf1qiFdtVYfw-CQbZscnGksMnyu--77hwDUSVpG2iJxlNbVDFbtEIHca952PDw3uQwYJ7mSRTm9Srw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61cf639d4b.mp4?token=YtJm0OsNSdKKBhJMMwitpJi6tc-TYGCgAlL23rcViUs7iF_WU7YSmZJzgMKfHt__JHOxaEIXQAuLJXSCC91Ua7UHASqCAsvbJSDUnyrBhpI9gtdw-FG2GseJBiVRudULwITvNvsap6tBjb023PnM-BgY5neANznDfrEcV_ogw_s0_VPoyPPfmp3IsRlnS4iMTJI0ocBjN9AyOyYDVx27HseT1jM4_yTHYZFHiSc9qwz_9jZVAeSQtQa3Wkh4yiFlXHHdh9Yzdf1qiFdtVYfw-CQbZscnGksMnyu--77hwDUSVpG2iJxlNbVDFbtEIHca952PDw3uQwYJ7mSRTm9Srw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
صحبت‌های انگیزشی و زیبای کریس رونالدو اسطوره پرتغالی فوتبال درباره زندگی ورزشی‌اش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/24195" target="_blank">📅 11:12 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24194">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jYeKaGV_xgsGKyDSIe2l_JceflSVbgXESbOFxiqhxmC-8axDhK4PKTgYvf4Ddu-EFsxvVUydtZIwdC2FgOcSHvpivG4-toR7asTBP8R6O4woO4yzVhJ4GtBJUnyAQMGYkEJeCgdgse6T1nzF0SzfDncY9W_JGmJh3r54xzMIR-GkJVEccVi86yLWpkyBib6SXbYPZ7PjeBHAvLMLYjm6AsC05_9UwROn7Ug0HB1GH2x_L7BrxzFAtMVSwyf6mPThIKqbshI99JIcqY-lUNjOb2S58478VqYX4IXlvMnQRw2M-icqPNkx6c4cQsgZg0z2KgYLAp-t2NBIkeUpUBHNlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ تا دقایقی دیگر جلسه نهایی بین مدیریت‌پرسپولیس و اوسمارویرابرزیلی برای جدایی توافقی برگزار خواهد شد. باشگاه با اسکوچیچ تموم کرده و فقط باید اوسمار فسخ کنه سپس از سرمربی جدید سرخپوشان پایتخت رونمایی خواهد شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/24194" target="_blank">📅 10:47 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24193">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f67895d89f.mp4?token=STi3xMMPFqsT_cI9Bptl5TI5Y6Cmd6vSQpAcG9wUQnaBMZyjAzOjEo-tESoGO9N_LS7s_68znel4USXAG2Rar7V0YcgyowWgF9SO7WqfXMfxpZL2WUAq3Yz1O1sGyPx29cmDlJcITxqxFTGnJuGbXUBfYLFuqYXvRM9RFDk56Tf8ZEx3Q8viqM3EuKeA77GFZgisZXcPvm5muVTRIoj9VGGBg_6s0w4Lcc0tpCfM-ppE7IBWVcMpwjmZMxRjqLfteVCACrA7hOe8L0cq75ISnX31yNusErT9PmJSObSx3nLJWmFWgvhHYPh4W6185Kvd8swP-8CszDO-baqVwHb52g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f67895d89f.mp4?token=STi3xMMPFqsT_cI9Bptl5TI5Y6Cmd6vSQpAcG9wUQnaBMZyjAzOjEo-tESoGO9N_LS7s_68znel4USXAG2Rar7V0YcgyowWgF9SO7WqfXMfxpZL2WUAq3Yz1O1sGyPx29cmDlJcITxqxFTGnJuGbXUBfYLFuqYXvRM9RFDk56Tf8ZEx3Q8viqM3EuKeA77GFZgisZXcPvm5muVTRIoj9VGGBg_6s0w4Lcc0tpCfM-ppE7IBWVcMpwjmZMxRjqLfteVCACrA7hOe8L0cq75ISnX31yNusErT9PmJSObSx3nLJWmFWgvhHYPh4W6185Kvd8swP-8CszDO-baqVwHb52g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بااعلام‌ابوطالب؛
رونالدینیواسطوره‌برزیلی‌فوتبال جهان در سن 46 سالگی به دنیای فوتبال برگشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/24193" target="_blank">📅 10:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24192">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac231ff126.mp4?token=fnct_TYUb7c1xSiY4unn1gLzsl4jTVqUI8yU05bEgPc-NUeuJTzrYrY5rYntSFbKlkURuWfVMw7cn5YTrdVHjBwvfnWqAfTDGNoQQBcqwpL7hETKTI6i-26aPPDIpp8ee2f-T9wEOr4sffzl672wH_KD0jlPU0vfrzTf8hRCxf6Dx0vuV7oKSIgOH979UxbLJcpqrPTb607CC66IB6ZBlkrXnX-i8MvCIY1I9sH8oBfkWqihLdHznJjWWnZjo1-4pfd1M2Yb3b_50N37qQzP8OP0BKOJN818pEAYPyzvdyMOu4ddqvBjh3Ftg3WcN3AAaCim2xmESqnl4ATm6-SzYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac231ff126.mp4?token=fnct_TYUb7c1xSiY4unn1gLzsl4jTVqUI8yU05bEgPc-NUeuJTzrYrY5rYntSFbKlkURuWfVMw7cn5YTrdVHjBwvfnWqAfTDGNoQQBcqwpL7hETKTI6i-26aPPDIpp8ee2f-T9wEOr4sffzl672wH_KD0jlPU0vfrzTf8hRCxf6Dx0vuV7oKSIgOH979UxbLJcpqrPTb607CC66IB6ZBlkrXnX-i8MvCIY1I9sH8oBfkWqihLdHznJjWWnZjo1-4pfd1M2Yb3b_50N37qQzP8OP0BKOJN818pEAYPyzvdyMOu4ddqvBjh3Ftg3WcN3AAaCim2xmESqnl4ATm6-SzYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤩
سفر پر هیجان لامین یامال ستاره 18 ساله بارسا و اسپانیا خارج از زمین؛ 6 دوست‌دختر تا اینجا
⚪️
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/24192" target="_blank">📅 10:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24191">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gvPxuagq3enx6wC3F2WSkYNYdX5g9PU1u5tHjdznybF6YsDOmmp6XNfr9fXjsuh1gnz9lixR8-8-wbMk4oQw7eYrftaY58Ivz6f0Nz8GAS6dc1fhXkGp_eKXkKxC2L_dFPN3RuKntDJH4zTiLon5iiXYOx49c7qsBVCKS2_wVp_TfYFR7vX0GohcWUH8HcUqx627pGp29PEQASWMnPcgYCxwkoAaJobvUktP0f7E6u6ugIeg5ShCqO_32XR58swvcQgrRxJEm4IgdH_GvAB70MGVjgdfyhhAmkvjlQotHDb15dMjhnQb_8p-rotaLLGLUyRd95P1X36KuRxOrrBoZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جداول12گانه مرحله گروهی جام جهانی 2026 پس‌از پایان‌هفته‌دوم؛ تاکنون‌صعود تیم های مکزیک، آمریکا، کلمبیا، آرژانتین، فرانسه آلمان قطعی شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/24191" target="_blank">📅 10:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24190">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ROpuWXrcCe9_aTW_AvWKnGCBfTSNKUsTKKwR_sxg9QhbxeRwDwyIzFEBPZyqMltl5z7eTRg3wwxKjdjYBWS6iw0mO6iLdCI6QTGKUxhnJQ9fmfC3H3e0GMA4ANaMcK7aJnN264Kq6NM8D15TDJ_5n7Puezi8t_ASPKjt04sWt3ktBfC46l2kHwpEB_kvI6FFxrj8URMsrGcq-BVT7TVdCBZCOcAXJmL5TfXRR6rPnbu5jnEljV0kGl-h2CBZmo0MtTRS2TJA68uoNiqljxoFDCvvPrKJyxHH28uB92CcD82cXeFcZihNIBefDrdnD6EpIqIGy1x4n1s_tndL9JSPWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
دیگه بازنده مطلق نباش
🅰️
🤩
🤩
🅰️
بابت هر شارژ موجوی اضافی بگیر
🤩
🤩
🅰️
کش بک بابت هر باخت
✅
این بونوس ها بدون
#قیدو
شرط و نامحدود هست
.
💵
با بت اینجا همیشه به سمت سود حرکت کن
🔼
⌛
پشتیبانی 24 ساعته
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان
r3
@betinjabet</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/24190" target="_blank">📅 10:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24188">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tdSJoBRLbeEvqXOk8xtIdR_cqJTv-OLU-r1madpXzEXuQ_AHlRmTg3EJv1aU6eZD-wDp2ydubGCi18LBgPmqIBX4jvwA_gdVr1tVEfvU7ipV60YMUxIax5rwplIMeaL8RU2zOCRGnmtGwuh2AalWrRylENJGUxO6B3S162H52oeCF3DgS0LubmGSF1jivN2uZB1nFJWNR5MRv1A2paCD1_r65ruKURgzF1yuDFPJaqjc4OJZ4iavZRTEX-AO1mb-rbG_PyhwivuD9Ysv4Jt4MfL8Z-guW8vHyWMAZ2ougitukeweyV5WXywtyCGwqNrumrsRL_zrtCCeHoJwxKvGtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HhrvLCCa_rscVL91k7kWmrcvPg7vNNqmBKxNKVk0CRkJa0dCt9Y1onNQnpqNQwQsRkEZd8kILsQnJo1Q3sH4-rAR8HxhWa-A6K5AM5uXyMCzDr2cn-zsoYD2mL5A6GKKV9r5rJQBr3u3iMNVsvJqoqOGQZuunl7p7FH3yHPlpCAD6rfJ0XlqfT29aeyK43B5Tfc3Zn4rMguD_m_MhvLgCS1_wfokGpv6j9bC20LmQMGVSZQKfGVNPyAqimAOUWcdCymamwrS17cDeqWSnT-_ggeey4go8TWpRRyj4GiHKg8zCL-EL28GlgRsdZ9afqd0j6SpA0NmY3C1AwXJq1HUhQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
هانده‌ارچل‌بازیگرمعروف‌ترکیه‌ای:
فقط بازی های پرتغال درجام‌جهانی رو دنبال میکنم و برای این تیم و کریس رونالدو آرزوی قهرمانی دارم.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/24188" target="_blank">📅 09:59 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24187">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c00a317fa.mp4?token=tLx_azmLXW80BvdjI_la3pVWCC_NtpA5UAJEW_ZkfK9COxfVbcorggK9UzpJTtVA_7AnpdWhtBNjwMWaJmFH2eV6_c-6gV5Xq14ZJ8NxqNp-vnPxY08P4vR3TRRPRS0ayUVKNNSXecbZEPyE2PSqsQ2fR-2U1Jxwe6R5BvVlH0XnwqCkYvhodyDQhjvR4Q-T1grYZ7mayEsd44PZaQPFZxgsnQhnx86jEJGXTNKklnC6uUkoFaa_YPzST1MvQRFCH4EPIMfYM79PEPUNHIz_4IOZEr6uqlWfd2WQ3xkGOUHyQxBeJxonAnCb3-uDBkNgoclPwPYLVRS8pSnRKdENoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c00a317fa.mp4?token=tLx_azmLXW80BvdjI_la3pVWCC_NtpA5UAJEW_ZkfK9COxfVbcorggK9UzpJTtVA_7AnpdWhtBNjwMWaJmFH2eV6_c-6gV5Xq14ZJ8NxqNp-vnPxY08P4vR3TRRPRS0ayUVKNNSXecbZEPyE2PSqsQ2fR-2U1Jxwe6R5BvVlH0XnwqCkYvhodyDQhjvR4Q-T1grYZ7mayEsd44PZaQPFZxgsnQhnx86jEJGXTNKklnC6uUkoFaa_YPzST1MvQRFCH4EPIMfYM79PEPUNHIz_4IOZEr6uqlWfd2WQ3xkGOUHyQxBeJxonAnCb3-uDBkNgoclPwPYLVRS8pSnRKdENoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇴
🇳🇴
واکنش‌جالب‌ارلینگ برات هالند به دیدار بعد با تیم ملی فرانسه و امباپه: «فکر می‌کنم فرانسه ما رو شکست میده و احتمالاً قهرمان هم میشه!»
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/24187" target="_blank">📅 09:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24186">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FkMXb_7-uqJP3Rd_20DDCtA2tQXKG5hqrfNeFWuWUjU5L6BJ0sYSaa41gFJJVBKynEWd0ZsDlMhHos6dFcTO81IyX0jGf8j5PzXWdf_MIiPBimOnvbMRnSFZce-ZhDDtecZqxYQvLzeo8UeEtQu_QrkUyklpSrCMCHyx5uEueYre2cS8MJs5pWMJxY55_jEpiZsCOxUyLIyoyzpD7z2STF-qTd6tRUoGecnINVb97AK9nfTC1_RYQVLHHHkr-NOOnF0xYeSSLgE1wlvErfl1XhXqNuOFT4_WebbSL_m29yYImhuAJrZ7MjeX5LnbIUh8gAaIXdyGLEP4v5KGybdfFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برگام! کارلوس کی روش درنشست خبری بعد از بازی امشب از نانا کوآکو بونسام جادوگرغنایی تشکر کرده. جادوگره گفته که کارخیلی سختیه ولی تلاش میکنم که غنارو چند مرحله بالاتر ببریم. فعلا با این اسکواد شخمی و در گروهی انگلیس و کرواسین صعود کرد‌
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/24186" target="_blank">📅 09:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24185">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EPVAQSxeTE9odlRYgX9ukBDDE1MWnWYm0P1Zv9oxBQMAz_p2DM1AW5iknSo0fCwqp0PqVMFh72o5fYpKZBe6gOIx8JtyrgBk1kz3XRIHCl8eR4Y9qcQnOU4vJF4fbTy-N0HorrjcRHaREPsikpUQgq14b8BE25GUJHo49koxQpYT02W9jQV8h9uuEbt-lYeMu_sSPbuDClq1SsKpKbNao5LJncmI3Ykfn0OrPrnNACSsyFIwiLsefKB5Eug-Q77eD2mDHQyOvzXAy4hZXyvmu0MNd7PY7Uw2PsGjD4t6aU7mNQ1p47yBy02mcwc5GMNNTgIf5OPkVTphHAy-VAFAnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه‌دو دیدار بامداد امروز جام جهانی؛ دومین پیروزی کلمبیا و صعود به مرحله حذفی؛ اولین پیروزی کروات‌ها در جام جهانی و امید به صعود بمرحله‌حذفی درگام آخر مرحله گروهی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/24185" target="_blank">📅 09:11 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24183">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZFv-fUq5Io_uE_gbiuJ5pPULNaW4d574ms8BRix6vpk0Ejtl5nhB2HETzUSP3DSXqxq7uckFvjzsabC5mF-jhcOda6u9WiLUy0xP5SdJFIn6D-LQIuTv_UqckISt6AelQ7pGvu7JCLtaXIT0tgyg1GmSWVXEyIY6WKfmofPhh3lhMOmquwCMAVXb3nGtDjvBR9osFJ3KLUQX6U8RyCeGrbiyh3GY491Df5xVWQQ78v--FUSH91v0kAIftCmyjm57Jg9qL7ZXN0ciEx0xzIRzaBqU5YsGMmPXuV7PkR2WnK-cb0M-BTPb9doh7dOPBedHuUE52i0mrKBmPXBRnTwTZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HhunLKRe39gTR0xTwpzoB8Hs2htF7JtueALdsYJSARJt4VLvykwjfAl6l_dD1aXZyMcbWQyBC3StKvCo3MXu6KImIwSRmsiAKbf4gPTgEFKkXtxofVRdlFApmynBFrQM6hgICgTZzk5n8FJ_-kXWgWtmAn1pzL2WPW6RFPRBhqgyrT_9kbrz34PiM4Uwp4Pa1MrFhTZX1yZQiEMTkO7d1FyebqmKwsNwJQK9j42qsOyLpTFxDS6v5BvI0CL0_xYZkAWDdw1I1hMciPisuEHIb4Yiia1ZEsnGAFpq9Aq9BFOkuTn43Z9vN-_1wUFIgHOhp511Txcz__N9tH8pc0IFLw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛ آغاز تقابل‌های جذاب و حساس هفته‌پایانی‌دورگروهی جام جهانی 2026
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24183" target="_blank">📅 09:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24181">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lXs8dPRUEvo7IUkhnblO28Me9Tz5fMXvxmM_tiBK66Y2a2-NnG41FZYzcmVnc1FBqg2bXAc-agudjcTrOLRPMOkFeewf04_AklXWCxcoX2obx8pONtgkzqGTmI8metV88GxhYklwci9pNsDJIQnb9Jr6N6SBCvXXnjgxl0oDve6fyGGdsDhNFRg7Sut7cMU0tStnwfLYBUu5EL1dKq-W3srpATPWXLLARCdpGUmcSX0r03UoJYCLgGdKQKccPUbJRKnGzqtwnMlcxCi0BgqBIxleLJmiPAQ73ug0LlQ13NW_8kIGAYz8HVa3Duq7qzNISi6kfSw_KKpSbNP_U_IkUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جادوگر تیم‌ملی‌غنا: گفته بودم که اجازه نمیدم امشب هری‌کین موثرمواقعگشود. همین تیم انگلیس دوره قبلی‌شش تا به‌تیم ایرانِ کی روش زده بود اما امشب حتی نتونستن به بار دروازه مارو باز کنند. به کی روش بابت صعود تیمش تبریک میگم. هدف غنا حضور در جمع هشت تیم برتر…</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/24181" target="_blank">📅 02:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24180">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hqFo-QrL0Nmo-l9K-ohGqAcu3LE7ezd2eOOnq8q9bU3_4jpiK8nd9gI2HpysbeVnHWkP3hfJBXSll44tkS1ikJmd0x2jLiBo4hzLhN_hEtY9SgZdixWsUcwvbGmTsiLBHlA3-Sg1CaQejgisNQfo7eASRQl7beWxarX_fk6n_mwNjwSc618INK8GPUy4i3wOGQ0PkEbLbXGBW6UopHhoUWpJSGZG5LyMoPT_iQCbFrYt73wPlkDN56rjpbLxBaEmwG5BxyH6TpJ22qhHcX2cTReGh64QZnudQ3YWG_P3hB74Y7Y7qGykhImohMby2Dn8fjNxHUlWqDWBKJDD1XvoqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛
آغاز تقابل‌های جذاب و حساس هفته‌پایانی‌دورگروهی جام جهانی 2026
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/24180" target="_blank">📅 02:21 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24179">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vZOrjQO3Bu15t5Qf31qo-ukVDIq5hH022XVeUtZZIQ_0BLaCNXtl296CM0k7jL9IXOvUz28ZoiuMuyzsHFDQOZWMJcePeGd13118cv5z0ZPYa5onVUbm6WEo697xC9iTSASM0RaPGo7056MY80rh3RZSjMirL4LTBKPK27XptDTrwXlycf0TDBUTIQXJUev7Wa2feUQLSQzJniHlNXA-BO5hpOb1qQJZ-J3OFwWawz7eHrjhfuQ5V_ERUDHnyC__-R3TPjJr1xFYp4b0oCUdi5u9y6RKazjdaS0BSgCVx96zqhQqfDPrkuaDsUkpgCv32g-DmzUKCagoTk7eQQJmsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌‌‌دیروز؛
از بردبی‌دردسریاران امباپه تاآتش‌بازی پرتغالی‌ها با دبل رونالدو و توقف انگلیس.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/24179" target="_blank">📅 02:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24178">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc844d2c9c.mp4?token=Z6jpw58rxmMna7GVYlEvd5WRKphrUDCZ1nw35B4FJ0bEbNAthbBQ8mZ1biRAS4bF_MCDl9vhBb1Okx8R2ESJIcNo4YqzNccmp5daUSvd0rpOM6Ok4uvw0_A_VMHgaKnz2OXOY38ehnHcBh5Fpy4lm5CGH1OxYq3errpduABRGXzVwGE1BOVMhrj8K0p88IusXbpZso2wTPE-Rerp0v6_svlmy-4_4nNiomcnCjQ8gNGfhriD9QO4vMmZEQfP77p6pa5dLYVTjB-TOcLccxqk0r2Mv6ZRqpKedwQltx2z5DaAx6YBQJdo-mCW7R9gCJZeE1tH2-qxkzm1BkSM-V_11w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc844d2c9c.mp4?token=Z6jpw58rxmMna7GVYlEvd5WRKphrUDCZ1nw35B4FJ0bEbNAthbBQ8mZ1biRAS4bF_MCDl9vhBb1Okx8R2ESJIcNo4YqzNccmp5daUSvd0rpOM6Ok4uvw0_A_VMHgaKnz2OXOY38ehnHcBh5Fpy4lm5CGH1OxYq3errpduABRGXzVwGE1BOVMhrj8K0p88IusXbpZso2wTPE-Rerp0v6_svlmy-4_4nNiomcnCjQ8gNGfhriD9QO4vMmZEQfP77p6pa5dLYVTjB-TOcLccxqk0r2Mv6ZRqpKedwQltx2z5DaAx6YBQJdo-mCW7R9gCJZeE1tH2-qxkzm1BkSM-V_11w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عکس رو باز کنید ببینید هری کین که سه فصله داره چشم‌بسته‌برای بایرن و انگلیس پشت سر هم گل میزنه چی رو خراب کرد. تازه سه چهارتا هم زد یا گلر میگرفت یا مدافعان از روی خط برمیگردوندند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/24178" target="_blank">📅 01:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24177">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XOR_eQ-Cp-PU4n7IE5oRbtINMqpJvrPKhvQEiIMbrnLqEQykgGCyW2PbhVXHCfsGXggr7xhoE4Sme0j1e3wvA8FCHWo6nYg64q6pl_tJjgD1KdYmQHKLYlnmOfmN5Xhq7m23-mDZHPvm9XKnVle3TbUzG0DFOVTDVhIJPm7MyAczxb15eFUKAmsBdL7izLz0d83bzwYVPindj9eRDKkrk2wF7a9MuUB82R0SWypycTkrwa9A3GdoNUwto_BZ-pjXYChXk4MSMIojqF0F_V9g5-mGylyl4sD7s1Vwn1ktGdxlsNnD3GWQfuwUwxNgEqgpk_4D5YUr9p9_Kkn7a7v-hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کین واقعا طلسم شده بود؟ هری کین که امسال انواع اقسام گل برای‌انگلیس و بایرن در نقاط مختلف زمین گل‌میکرد امشب‌همچین موقعیت صدرصدی رو به آسمون کوبید. چند موقعیت دیگم گیرش اومد که بازیکن غنا توپ رو از روی‌خط‌دروازه بیرون کشیدند.
🇬🇭
غنا
0️⃣
-
0️⃣
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
…</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/24177" target="_blank">📅 01:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24176">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RnAavDi9e4rcBmLY0isG1eHW3sLJktG2h6OGuVbSqdPtoNmvrCEj70SxwCtiAF1Z-lYIp6eyqZ84-IRC5poO-F_G73GYtxaV-p_DANGwsTVtRykXNzeWiF04U8JBrspvhufB5Gi1MtKLAdAuM_FI-PBcACO3YIxYw_fKNkrak5ZKfKlErCwVcCa5iE45nw1F6Zrs9qecI5_kJAIFc_leRmWCYQFDvNGYcdjD4ngrtzc7eVGcVUfuJPVnxDg84xsVB6z3lk6KYp8moiEImGSMkwcpT8Q7zthCNg3eb_8eVBPQkbLQ4jVZ9BIqZlCY6MQH6PF-OH0vi9tJvEor2_8AiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کین واقعا طلسم شده بود؟ هری کین که امسال انواع اقسام گل برای‌انگلیس و بایرن در نقاط مختلف زمین گل‌میکرد امشب‌همچین موقعیت صدرصدی رو به آسمون کوبید. چند موقعیت دیگم گیرش اومد که بازیکن غنا توپ رو از روی‌خط‌دروازه بیرون کشیدند.
🇬🇭
غنا
0️⃣
-
0️⃣
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
…</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/24176" target="_blank">📅 01:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24175">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d277b50bd3.mp4?token=OiLExo2lFCDBx965OgKyf5f8hGaLEclh0MRS9M-hZMCDC-Yn7tIYLMMoNrbBLuTYkf_R-iZNqYG2RgK9ZoOlZ3sh5Y7PJ9OlmkWHLBb4VH4Zzmr5RBFgSeyMs7aq6FMqdR8ZzCqtyGDHK3uhmTRuKi64QQn6x8Dc7b0VgRrtKsWaR4CxxaL7XPRStV066lRuNc7tP3HQN21loapb7xm67OKqhaajd87pU6ToccNFfeCD6SNGamF6c0_nlEmSbTC0XQtYo-lJtFycS31-ywjNbix418FNswFGePwlFx-nkl1fS7frylVwEHSwTOgIeXBWmbbhqFVyRwcP2zoAkSBoCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d277b50bd3.mp4?token=OiLExo2lFCDBx965OgKyf5f8hGaLEclh0MRS9M-hZMCDC-Yn7tIYLMMoNrbBLuTYkf_R-iZNqYG2RgK9ZoOlZ3sh5Y7PJ9OlmkWHLBb4VH4Zzmr5RBFgSeyMs7aq6FMqdR8ZzCqtyGDHK3uhmTRuKi64QQn6x8Dc7b0VgRrtKsWaR4CxxaL7XPRStV066lRuNc7tP3HQN21loapb7xm67OKqhaajd87pU6ToccNFfeCD6SNGamF6c0_nlEmSbTC0XQtYo-lJtFycS31-ywjNbix418FNswFGePwlFx-nkl1fS7frylVwEHSwTOgIeXBWmbbhqFVyRwcP2zoAkSBoCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚽️
#تکمیلی؛ یه جادوگر غنایی که در بازی هفته اول جام جهانی غنا مقابل‌پاناما یه‌همچین حرکاتی در ورزشگاه‌انجام‌دادوغنا دردقیقه 90+5 گل‌برتری رو به پاناما زد گفته‌برای‌امشب هری کین رو طلسم که نتونه موثر بازی‌کنه. این جادوگر سال 2014 هم مدعی شد که با طلسم های…</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/24175" target="_blank">📅 01:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24174">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e4PYKlEdK0tuv_mP4LwREY26P0K9N69CUq_1o-efM6YDloON1eOnCsipRqyvvZeA9X2NSGw9G4pixomwzypdalHI8FRoKWBiOAL3BZgYZk60R-7M1cMPxpd_0fIsOU0VIQmSYmYoGE0H5Ty_XofQ4UBuBWjz4ddKE2HluHVMynq54IorCFyKjPfaX7Ip7KlAeczLp87fZXpHKuDz4LsGw40FE8QspmXpt3D5pBM98PpDc1_HBMy4CTV4bOZmhL5AT1b8-K9nWnsycnueHNBBpi77rzRMFNzgCIvJV3wIGPGGOG53jZfya2QRAer_4ZhWtIFDICVpFHUNxt8siflBMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو کاپیتان‌تیم‌ملی‌پرتغال بعد از دبل برابر ازبکستان: یجوری رفتار می‌کردن که انگار من دیگه ازفوتبال خداحافظی‌کردم و تموم شدم! اما من تحمل کردم، مثل همیشه؛ چون من بیش تر از هر چیزی به کار و تلاش اعتقاد دارم. سخت بود واقعا، باید بهش اعتراف کنم،…</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/24174" target="_blank">📅 01:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24171">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0d760ac60.mp4?token=IZxgZgF3zgIiQAzPnBhqAR9NO5U9xHoEsrgG3qqgQX_u3BDRtHLehSc25wOAI05xffdh3GnY26JFXaOZI_ONBC3IrOuqs2vuxELNKQb7it3Gi2qWF-UpMJj2fLRkt8Sk92Ti2JMto-nMKCA3ZYuTr8w0oFOy5iSfGg9OG2J_CzvXslsLkJwv6ulQwD67pDrlyiTYiq62UyyOw_YXoVJ98Btrn7oJD5T77EB_yx2IkH_moNY5wT7j4hQSKJlQ41xUlR88B9clwGYpt3q2gsPfk2kAKpY-aneQZRaug82jUWoAuaAtL5kC_YL1BMgPBX3VgH-mhMpvmhkrUlZaCOwHeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0d760ac60.mp4?token=IZxgZgF3zgIiQAzPnBhqAR9NO5U9xHoEsrgG3qqgQX_u3BDRtHLehSc25wOAI05xffdh3GnY26JFXaOZI_ONBC3IrOuqs2vuxELNKQb7it3Gi2qWF-UpMJj2fLRkt8Sk92Ti2JMto-nMKCA3ZYuTr8w0oFOy5iSfGg9OG2J_CzvXslsLkJwv6ulQwD67pDrlyiTYiq62UyyOw_YXoVJ98Btrn7oJD5T77EB_yx2IkH_moNY5wT7j4hQSKJlQ41xUlR88B9clwGYpt3q2gsPfk2kAKpY-aneQZRaug82jUWoAuaAtL5kC_YL1BMgPBX3VgH-mhMpvmhkrUlZaCOwHeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
عملکردخیره‌کننده‌ لئو مسی درسن 38 سالگی: 50 بازی، 50 گل‌زده، 30 پاس‌گل؛ همچین لئو مسی درکل‌دوران حرفه‌ای خود 916 گل زده و 414 پاس گل‌نیز به‌ثبت‌رسانده. یه پاس گل تو جام جهانی بده عنوان بهترین پاس گل‌تاریخ‌جام‌جهانی هم میگیره.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/24171" target="_blank">📅 00:41 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24170">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a0dGf6dLSR7rZPsitgaUw2VHzhTJb5pgIUPtgabyktELOtvkDwTLIWpDl-C2waRkNjXiZYbKaliLK1_Abrk5xPiUI7jgDDdmFQJP0tYSYZ0wmqgmN_j_4wqDVX1kMvmFsS6HghuJBAVg9GkuQGbHCI8Ou2gZJQjlDnuFI8xCNo2zf1PpiEeQDmOVoPKZWf7iufnnxwAFoPNGbW71Ge8JOyzoPo-CYaVjSB9ArvBqxkwEi9zwYrmRlAiEeeDvWdClYTqMAUNNbvw6g2lqFjHZYRnREMdeSacSqdhhdW1fJhqsII5ezZjTjpxfaSM3dMjCmAsTOo9n0ucc4yZKyreV7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو کاپیتان‌تیم‌ملی‌پرتغال بعد از دبل برابر ازبکستان: یجوری رفتار می‌کردن که انگار من دیگه ازفوتبال خداحافظی‌کردم و تموم شدم! اما من تحمل کردم، مثل همیشه؛ چون من بیش تر از هر چیزی به کار و تلاش اعتقاد دارم. سخت بود واقعا، باید بهش اعتراف کنم،…</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/24170" target="_blank">📅 00:22 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24169">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59b8e3fdc2.mp4?token=g40UQajufX2inPQpQcQuVBIsUAE5ofz7bUJ306VX9Xh8mIK-s6LKcqlSs1GM9rkSV0bs0E2lt5B98e06P4fVdMp6Kcdk0V9h0ebfp3kpKAy3mWHGMc9tZtZ9hYi89CpKui3UsahvDVrZrzC82Q8N_atN243aDa50VLYCT7oc0zeBBiI7h1xgTofXlfYH1GDaZmn0ItShFJ_vzx0f7r1c--VTQI9Xqr5YwsuBvpNRNJifdwT4bpwLOD7FmlYvVGVInT0FQLWXioLL_mD6J3bdtsMGpTXAnhblMyM1uSErHXqfwNbDf9m8Z0SQGtJyYBvn1YB6GzP3ab8EzVah_G34K4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59b8e3fdc2.mp4?token=g40UQajufX2inPQpQcQuVBIsUAE5ofz7bUJ306VX9Xh8mIK-s6LKcqlSs1GM9rkSV0bs0E2lt5B98e06P4fVdMp6Kcdk0V9h0ebfp3kpKAy3mWHGMc9tZtZ9hYi89CpKui3UsahvDVrZrzC82Q8N_atN243aDa50VLYCT7oc0zeBBiI7h1xgTofXlfYH1GDaZmn0ItShFJ_vzx0f7r1c--VTQI9Xqr5YwsuBvpNRNJifdwT4bpwLOD7FmlYvVGVInT0FQLWXioLL_mD6J3bdtsMGpTXAnhblMyM1uSErHXqfwNbDf9m8Z0SQGtJyYBvn1YB6GzP3ab8EzVah_G34K4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو کاپیتان‌تیم‌ملی‌پرتغال بعد از دبل برابر ازبکستان:
یجوری رفتار می‌کردن که انگار من دیگه ازفوتبال خداحافظی‌کردم و تموم شدم! اما من تحمل کردم، مثل همیشه؛ چون من بیش تر از هر چیزی به کار و تلاش اعتقاد دارم. سخت بود واقعا، باید بهش اعتراف کنم، اما خب. مادوباره برگشتیم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/24169" target="_blank">📅 00:12 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24168">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mukz27dbckSFkYJt6XYNHXRMaF0LXQa270gdQkKcHeEBxq0MQYoGrVjwe852hscXBodWklUBG-YQXHTiNn88X13p6RrWNFF7vJgS_JEvqUTptb-bQw8oCA4bp9CJM7_m9DU04ltA0xwguSXlwlL47tppnLuAd1cmBM80X8a_IMp3EEqEejMTf08qxEDwZWvrbHR1aWDSYz52Kje-U4PnyeZfP_6uEYkdxVv4JLLbRF74fDQkB_c4UBvXa32suPRgY5rgzMVf6jMHQEg3KqZe53bDCiEoX0up0X0xF2jU921PAoeiVY27LxFWfx3fP9I7_1LfmV5c3-Lt4eAMa_TM-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
رونالدو بادبل‌دربازی‌امشب‌وکسب‌نمره9.1 درسن 41 سالگی بعنوان بهترین بازیکن زمین انتخاب شد. رونالدو در پایان بازی گفت من برگشتم به بازی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/24168" target="_blank">📅 23:55 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24167">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QUASnEUqXz167rqf1z5G6Ra54oNG5Op95nnNrrfFB_yCZPxL5PiKX2WV4nmlu0CwSYb1FDiKbdoEo1fg6mn69EHaVYLmIZ6I7mkfB6KWOknXpqerndMOfDTUstlYI0QyPGZcrUjG8rRWdBzKf24h7Ojzfn_75c3ipjf3QgfN0_Ps_r2htiAPGhv8hf__Gz6CpMFgkIg2hwO5_GB1lqPHYj2wVGjQjetrjD7dGsJfGYF4lWzJi3TNgFABnCf1CjKtcesePHc-g0sGjuwLqlkRMe62MOcDRORQeVIlYvYkNUf2n6IpF2pWFtfzsVVd0439Zm9J_-MofF7PS3oxGvll2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
چندساعت‌پیش‌مادر دیدیه‌دشان سرمربی فرانسه فوت شده و این‌سرمربی‌برای‌مراسم خاکسپاری قراره به‌ فرانسه برگرده و در بازی روز جمعه مقابل نروژ در هفته سوم روی نیمکت خروس ها نیست.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/24167" target="_blank">📅 23:41 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24165">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e38cb7e207.mp4?token=S9_mi-2PtIE1rPELWMZazwhZNOahmCLajYBLNfjJ9wAduNXJfhoqriP_KSv0JcLHl6jxhc1DWHhBfrVeekkLfdYStb5OG-5WLbV7pJjuABvHBBCXZMBpg8K5JcJhdc67WxGZe9VXgj68qFGGgTPTrGvHKvStK5IXz0FsffykVFBP9RKZJ3YIulxiwO-YOFvNEytj6WJtN1miEp9KiPk76q7coCydO-C4VVbyb_WD-JsQ311CTRobFZzSF4BHOCm4d7tpC_0xyT4h3Gk2ZgQiFT_PmTw8uJ9yZ8AEFrAMCAu-SknKmuX7OCYAfWsze_4Kkav3dwqkJumcIE_4wELG2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e38cb7e207.mp4?token=S9_mi-2PtIE1rPELWMZazwhZNOahmCLajYBLNfjJ9wAduNXJfhoqriP_KSv0JcLHl6jxhc1DWHhBfrVeekkLfdYStb5OG-5WLbV7pJjuABvHBBCXZMBpg8K5JcJhdc67WxGZe9VXgj68qFGGgTPTrGvHKvStK5IXz0FsffykVFBP9RKZJ3YIulxiwO-YOFvNEytj6WJtN1miEp9KiPk76q7coCydO-C4VVbyb_WD-JsQ311CTRobFZzSF4BHOCm4d7tpC_0xyT4h3Gk2ZgQiFT_PmTw8uJ9yZ8AEFrAMCAu-SknKmuX7OCYAfWsze_4Kkav3dwqkJumcIE_4wELG2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هر چی تشویق تا حالا دیدی فراموش کن، دیشب نروژی‌ها به سبک وایکینگ‌ها کل استادیوم رو به وجد آوردن؛ هر کجا هم فرصت بشه تو کوچه و خیابون این تشویق‌شونو انجام میدن
😍
😂
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/24165" target="_blank">📅 23:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24164">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gbGqGyg38PNDjnfsYIfKuDmvwGkP-LHmV79ljCiyxZ7IzFtuD49bv8lvBAklzXRisqerWIoXhgnlxBC6HXkohfFYi3jSuMZI0IsrgH0W31dkciRbPHwyQBvqdTb13jep_lLv_3nkjRIZ8ZOCXWeO5cYSHjwCMbYwpyMR3OSGUHxe0y80D2cu7AgNIBBj95_ii9TOjSNMD7p9Yg0DNLhJ6x_jMiqlgvBklCdqUWtm4o3c8Auv2Ghp-HqXvxjjrebJw9lJhMeQDgUWCKnVGnSZoGXtjC_bTQHmydXfqeJGTqlo3WUSkvSiLkYuO5QMAyHvfrr2xZsbU8MVEOyFMGqaAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌نساجی‌مازندران درگفتگو با ایجنت دانیال ایری مدافع میانی ملی پوش 21 ساله این تیم رقم فروش او رو 90 میلیارد تومان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/24164" target="_blank">📅 23:16 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24163">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41c27664f5.mp4?token=FfbyHCOvqqjGPJsw5pf1h_fhyK8kjgxBqg2SpgAL_zL-n9tAzOzyi38tIVOk21ZkkvZf8usBG46iQVCDNIW16y5DTGUcuFHpGaDlgPftAFzSMiKv31oSoTXn5JFgON4U4Lpk_82La0dcM4--IQfnnTjb20398wD1anvQlfVh4i2zUa_mUS8iP2On_MWZ3jbpePEB9KKZMQdhOhUKqiEioxbWWehODjuU465N2KG8QeEpXPe7GSuNN_lxtXOierlMdMBKVuUSq3xq0L6PNjSx7AEfkcYelFJvCP0A6BMiA31xV72Oj5AVrgOxxCps1N5jfVMYtKk2n_6OPBrccYUmxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41c27664f5.mp4?token=FfbyHCOvqqjGPJsw5pf1h_fhyK8kjgxBqg2SpgAL_zL-n9tAzOzyi38tIVOk21ZkkvZf8usBG46iQVCDNIW16y5DTGUcuFHpGaDlgPftAFzSMiKv31oSoTXn5JFgON4U4Lpk_82La0dcM4--IQfnnTjb20398wD1anvQlfVh4i2zUa_mUS8iP2On_MWZ3jbpePEB9KKZMQdhOhUKqiEioxbWWehODjuU465N2KG8QeEpXPe7GSuNN_lxtXOierlMdMBKVuUSq3xq0L6PNjSx7AEfkcYelFJvCP0A6BMiA31xV72Oj5AVrgOxxCps1N5jfVMYtKk2n_6OPBrccYUmxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
هفته دوم جام جهانی 2026؛ پیروزی پرگل و قاطعانه پرتغال‌مقابل‌شاگردان‌فابیو کاناوارو در شب درخشش‌دوباره CR7 با ثبت دو گل در این مسابقه.
🇺🇿
ازبکستان
0️⃣
-
5️⃣
پرتغال
🇵🇹
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24163" target="_blank">📅 23:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24162">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ejS-COKDTeKdrxdPeAF7wBzWKqUDQpn3rW-Ym26whbVzPznFwLy09N_mz8KLxTA__7bp4zt5_8K7ah6V9G8AzFZOeUbK6ICOI08_B1VkKxgKuTF5ZpcSt5TfmGZKewh8oR-Haj2A3dj6eLekas1dARw2Kt4yGw8HGbEWOs9F4WsGsRdw9KuHIFSVlTzQAKZOjtcplZsq69hFEh9Sh1vAVR6rJFfCSCP1iOdO2wBYBPJJPNcoR3afs6noNJltjgZNHMVfkC6doF5QSEn8RE7DLUEHoW8DvCf22Rd1szGMAsHV4bTGmc9g_9nKRs1cgQgzQxuQYGLLFm40xGA00QVazw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
عملکردخیره‌کننده‌ لئو مسی درسن 38 سالگی: 50 بازی، 50 گل‌زده، 30 پاس‌گل؛ همچین لئو مسی درکل‌دوران حرفه‌ای خود 916 گل زده و 414 پاس گل‌نیز به‌ثبت‌رسانده. یه پاس گل تو جام جهانی بده عنوان بهترین پاس گل‌تاریخ‌جام‌جهانی هم میگیره.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/24162" target="_blank">📅 23:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24161">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NjAvnZJOOroBRf9K98rzTnFX0iZo7JBrWoM053pNXq8p0mI9gO0yW8rCBmDleoWEtQko8ysEKC4BkdjYCecZ0Y5M0G4kYaFTETWFw6ycOm19jK3S84F_tZUMwHVcHEMrhpW7TxkPnouiKz-TTXjCLrlb34S7byxKQlegwyqZDoHnt6JbyoBsobcjBhBKXwjPcwfDspINmzOX0yi7G7edW-yGdS6G9aaXHoyw9lR12dHrfgQJDZwhMdmlN1d3rG0aBTA872pmCUUkLn7XgbKWV-V7j8WNNYIQjZnOWsawehDhMyHF1Q_jsC7Uxzn-91-8G5jOBzpfRoTnVT7fBJvUOQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/24161" target="_blank">📅 23:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24160">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DHgJbwUxr0GttZmgaf5dmg3c-9rv7ScWRNdSSYaA9e0ybGz9TGwa0u0PQYoAQ9Yc4iSa7riAofEi_k9y-8xroKW1hRXllCgtl4Q-82K6KQQZSZgsujxp1hZuyQ0XZNwbQ7PWfbCKJzcoUk0wfVlAYnpwQtc0GCZrCkaNOb53BSs8xtC-U1d404GLAn5WcEVgTyRHjco3HaT8A5_fNBeVntjYrkoBuUGkoXD1uc5hoTa7ax_Xf5iIYrxGG8cCUXB9YCRTBZXW-CnqZsLYuoJdzYgfFU-snwoGIPFdmmCMH8OayRhPM_VX98Y_0vJS5zbmKREIPrL3IU1ZF_7u2HLyyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇷🇺
👤
#فوری
؛ ادعای رسانه‌های روسیه‌ای:
بعد از درخشش دربازی‌مقابل بلژیک؛ باشگاه زنیت روسیه به دنبال عقدقرارداد دوساله‌با علیرضا بیرانونده و قراره بزودی با مدیر برنامه هاش مذاکراتی داشته باشد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24160" target="_blank">📅 22:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24159">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eNN9-E8gSGRPZmTAQtBoVjMufI2YxTC1ZZf7cIhJTqXQ6CRIKp_5oCmeXcri08YuL7B0zvHFMm4wWyrz8DQ3IxkFus-NoagHzyiiES8HbGXH0wJYskS6sjqsI960P-9wP-0Zsp6AR-RoX6g_iXaoBsOsie1Kbd3bjQSCJkJ-6tCvYKKBvb6BppeiOhtEqnHzVTXxtXKUNl3_-5GbOc66ietSOl9Bd-Vpn2UBXS9UnrBogc7F9n6zbOlrCecqjAl69nnlF6BPf40li1lxiuyMH1XIrDbhrLb_TUerPv2vco25RyzJPQnnOXPwQ2jrrIbYH2444treyCh9nCyut9bnQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
هفته دوم جام جهانی 2026؛ پیروزی پرگل و قاطعانه پرتغال‌مقابل‌شاگردان‌فابیو کاناوارو در شب درخشش‌دوباره CR7 با ثبت دو گل در این مسابقه.
🇺🇿
ازبکستان
0️⃣
-
5️⃣
پرتغال
🇵🇹
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/24159" target="_blank">📅 22:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24158">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HTmz9dxsYehWB7X4AdYRmiFjxyNvY9tHcjAHTIqTPvoTl5vIF3mAPYvAYZMU4lcxqgNwxRj4o1ZFUJI2I0P01-_FKEt4bwg2ocXAMrgaYq41MRkCSc0hOBToCS6dG1XsH_sFALqeQJo5DB4271fGWLREpkOyymXIBJAaV44EIQt-68klrz9kK4yiD7Z3Q4rWll6NnPIdDKOiyErAwM781acwwiq0K6h_jwg3yyT2Q1AhWkskh0s3_5V7q4HVs1XnVnDSPSqRof2JHljsKzmPQ5u8SkFH56sqhpXajud0jfvJRo_dGmODwpO3NyOT03a7ShuYv_B2QB6dghP_gqNw7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
🇵🇹
بازیکنان ازبکستان به این شکل گل چهار پرتغال رو به خودشون زدند. رونالدو سمت ژائو نوس رفت با او رو در آغوش گرفت. بزرگی یعنی این.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/24158" target="_blank">📅 22:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24156">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lswJHT_2-9ML0zsLM3KNkLe5omaffZa5GBN61LP3i82mw4J3v_Nu1CDM0BtTUXQnvR7JP8qnt8vkND8kHNREa0USvQvlBFo0BsWb_yqhXR3yCmdhY6N2clLeXCzwZ9mlaxiWDsxe0_7qojTWohThRCznuYHoucYe_Bl5DYhMpvML4-6KFfGRuhBU0hCNMHgTmnndEzpwsNFTEiELqo0LvNwgScuvpJthFZYdVgD7v3DAIkNHsrB68MAKn76hVmuheHFoMeWFXTKMkMMSvHSqA-HkaQUeOHoJboOHTuRxRII8pmWBo3V7_FklkDKCfBPZcUWo7-oidMHQx7D0QZppcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/skdqpk2t52wMIs5nwcfuEsdbU15ICNB2PXZYJ-34Z_q3rgjiINBtxJEyt-sTZkl-KsvNuA83x9CLoxhoEQz-364r-2B1A86MfzB91_XV-9pOfnSY_COda-nn6wZl8YN-frb8cywfecMCED0Dm9XO_77xBWt8cNk6VJLtt5jHZZHc_hD8I2XhBtj_TtrOJpYIXtBNDE8aSCZEpjnr2t_rVxNBqrHy9mrxc2TOh06KE8G8TexUkyK_x6zNLIW7vya14FgghYR2h5ABXmhBkEwl11hgMiE-MoUyUQY-Zd85eAbR0sUUxaDMZhBDDLqLuZtaL9S5z5X0hjHn3F4ON-kTcw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
جادوگر تیم ملی غنا: کار بسیار سختیه اما تمام تلاشم رو بکار خواهم برد که با طلسم هایم غنا رو به جمع هشتم برتر جام جهانی 2026 برسونم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/24156" target="_blank">📅 22:21 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24155">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U2rLgnva4JE0EUJpU1dahmM6_teIOIgTGtnA0ahOO-H35bYCNcj1AKvDwotT_cYrLguvhubNNcDQFEEMNYh4GooPfBiCppA0DDI5RRcvrmticzXVS_7bYzV0K14F69x7o7k3IjklEZsMaCkggqLNnQK4MAZ8OMQcGDnUR453SYJ5w43tIW6gqdf5a9GaEs9CRXwMEvAi43IJkO51_u9nTm0jNgoi1mlDHqYCJaOqaeiz2xnqaBVHYohkQsKIdzPDbpHaC2u3LJvZhJ65VrUlZvGN1i6Iji0oZM3miCzG9fcq3E5Yv2Y960mDByYIZhOhqNVpenyVEcSx_pEOt-lhDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
🇵🇹
بازیکنان ازبکستان به این شکل گل چهار پرتغال رو به خودشون زدند. رونالدو سمت ژائو نوس رفت با او رو در آغوش گرفت. بزرگی یعنی این.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/24155" target="_blank">📅 22:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24154">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a29fa94bc.mp4?token=BvDQLHqqAfVX3M1EyHSK1uOrAM0_1N_4mo2HdlM5JBTW9QmNmTirNT4gdWyJXMoEjG4hDn2lEE4IPGjm7a63NQMQJYQKUesFfmrkVpU37Rt1FxSEmvR0X3psaST5mO8jUHNIYXu4wBddJn5o2tdwDgNBvcF73IrRj38skjKncbkYP3rJZhjRMfLqhkxsGhHWE9Z4xlb84l6kEm1cK-7kM_fx9Zrqv_Z4tx-yJmnI8H_3e1IxrfqxiOsugkYwzj0lZ1Xm6mq99JeWJ1ZGUGQ9WMhJrx7de84jXCMjeK_mG4iijNS57Hk3dhmO_TOXhtAX_LUGfjxZvyyBV2boPjFZqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a29fa94bc.mp4?token=BvDQLHqqAfVX3M1EyHSK1uOrAM0_1N_4mo2HdlM5JBTW9QmNmTirNT4gdWyJXMoEjG4hDn2lEE4IPGjm7a63NQMQJYQKUesFfmrkVpU37Rt1FxSEmvR0X3psaST5mO8jUHNIYXu4wBddJn5o2tdwDgNBvcF73IrRj38skjKncbkYP3rJZhjRMfLqhkxsGhHWE9Z4xlb84l6kEm1cK-7kM_fx9Zrqv_Z4tx-yJmnI8H_3e1IxrfqxiOsugkYwzj0lZ1Xm6mq99JeWJ1ZGUGQ9WMhJrx7de84jXCMjeK_mG4iijNS57Hk3dhmO_TOXhtAX_LUGfjxZvyyBV2boPjFZqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
#فکت؛ کریس رونالدو به جوان‌ترین و مسن ترین بازیکن تاریخ پرتعال تبدیل‌شد که برای این تیم دررقابت های جام جهانی موفق به گلزنی شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/24154" target="_blank">📅 22:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24152">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pxH_WPQRSFTvMORPdA5Mbs35Uc0o-gc3QDZkbe9yr0KqOTu3enOa84GiKCX7V2QggWC74Jdq9GG-Uc1RKT0QuANTX_bWVnx_wY96bK9B2BxKFhcVI98f_VRcuePxEYORP0fgdiiPhVtt0HlCYfnpzzDBO8hsZxr4enZbXHWniGPscX-1ujip2kOzPVBSTbftfLfIzhB5eNhw_OnLds3LSuUdvta4OU85Mq-Oz0yhNnNoJsVluTLQj1I0uOru7V9CrF5rDfjblx83gtBIQlxWgkeUNK1MbtIr4gEBxb8EeevOMKpss21xIk9bIqrzoXXp55myMdmrW9ayo3_glLA5Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
دبل کریس رونالدو در بازی امشب تیم ملی پرتعال مقابل ازبکستان؛ این‌دهمین‌گل کریس رونالدو درتاریخ‌جام‌جهانی‌بود. یخورده بازیکن بهش کمک کنن قشنگ‌میتونه‌برای‌آقای گلی رقابت‌کنه. این 975 امین گل‌تاریخ کریس رونالدو در کل دوران حرفه‌ایش بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/24152" target="_blank">📅 21:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24151">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df5b6d9df2.mp4?token=Ld1-4K9bMHOZ6nXAPciQnImuWVna1BPQFp8eLv9i3fBcVpFUenbNiU0BFS-PxHwjh1kVwSNkKsGPjA-2rQyGzdth3MbWCLO3-Zw0ncA-Tth--SkB6qnAM63ukyQFPYslURGlaejxHNGSn6FY_InzRHsIgwHTMlx7rugmS-wVk4k8hdOq9C4I_HTX9zn4gw02LBEKq-iv1UtjNRoabLgF72-an2VQrruKu-udvl_UXwgG-3Q1691ACT6T40SDCZbNzA1miqCTerF3XH3fTbYbUe_yqHlPnIJODIXKFwRodnCHSfp_mk9rRLU2cFOnt9oijhvhLNuIj1ncPFfU_3OJHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df5b6d9df2.mp4?token=Ld1-4K9bMHOZ6nXAPciQnImuWVna1BPQFp8eLv9i3fBcVpFUenbNiU0BFS-PxHwjh1kVwSNkKsGPjA-2rQyGzdth3MbWCLO3-Zw0ncA-Tth--SkB6qnAM63ukyQFPYslURGlaejxHNGSn6FY_InzRHsIgwHTMlx7rugmS-wVk4k8hdOq9C4I_HTX9zn4gw02LBEKq-iv1UtjNRoabLgF72-an2VQrruKu-udvl_UXwgG-3Q1691ACT6T40SDCZbNzA1miqCTerF3XH3fTbYbUe_yqHlPnIJODIXKFwRodnCHSfp_mk9rRLU2cFOnt9oijhvhLNuIj1ncPFfU_3OJHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
موتورگلزنی فوق‌ستاره پرتغالی فوتبال جهان روشن شد؛ گل‌دیدنیCR7 در 40 سالگی به ازبکستان درجام‌جهانی؛ رونالدو به‌اولین بازیکن تاریخ تبدیل شد که در شش جام جهانی پیاپی موفق به گلزنی میشود. این نهمین گل CR7 در تاریخ جام جهانی فوتبال بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/24151" target="_blank">📅 21:17 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24150">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c38410752.mp4?token=GfxoS9TEGINvoBDK0FIb60bG6M-Ql18ssiWo-coTAL8parej6hT7YfzH1ziBNyeaVLZ8c7GGavm_-nswfUIt0HJuJRfQRxmN4RPUtRvT0MyrdUI-zmyi5f0eB5BGrV0_G-5_uorA29giXZxZYAOfO14y3y9aw7UdQ4TQBoP7mMOdx8IjBeKgsf2fa8yKJniR4Lvjtkp8ZUY5mvwmectaFigx1ukt6agLDcotOuuKnj2zYseTtG86j_q4l72TCPaizxocLwOWMSo3MMj6qY1xUtETgoI1S-8r-q59bWmaO7774BKMstZLREJVTv80nvRB3DG01RZwF4SwBc6sRPTmGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c38410752.mp4?token=GfxoS9TEGINvoBDK0FIb60bG6M-Ql18ssiWo-coTAL8parej6hT7YfzH1ziBNyeaVLZ8c7GGavm_-nswfUIt0HJuJRfQRxmN4RPUtRvT0MyrdUI-zmyi5f0eB5BGrV0_G-5_uorA29giXZxZYAOfO14y3y9aw7UdQ4TQBoP7mMOdx8IjBeKgsf2fa8yKJniR4Lvjtkp8ZUY5mvwmectaFigx1ukt6agLDcotOuuKnj2zYseTtG86j_q4l72TCPaizxocLwOWMSo3MMj6qY1xUtETgoI1S-8r-q59bWmaO7774BKMstZLREJVTv80nvRB3DG01RZwF4SwBc6sRPTmGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
موتورگلزنی فوق‌ستاره پرتغالی فوتبال جهان روشن شد؛ گل‌دیدنیCR7 در 40 سالگی به ازبکستان درجام‌جهانی؛ رونالدو به‌اولین بازیکن تاریخ تبدیل شد که در شش جام جهانی پیاپی موفق به گلزنی میشود. این نهمین گل CR7 در تاریخ جام جهانی فوتبال بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/24150" target="_blank">📅 20:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24148">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ab3271383.mp4?token=sX4i0ZxJ0fVRi_Seeiov3Uq1NTMixbiXXO5DBwjaN8r-Hm01xh9Ev2h_8n4p6Pg2-xx4nAx11xnR0EK_4WX0PZIs_1yuJxVROV4NpNV4v9-Ax8c4UVbgrIL5QW968wJyF3NRACGfgR9qQN-srda_JOlRozFAZ8o24EqY27Y7djagOStlVGHOs18AM_hYcJgmt9cEtqpQlZkQv4-L8fj4VsUQxcFBPTlkf5zFePK-qPyBGjP5tbPdyNIpLFdkM8oNbUcG--FWWKjSGDFXE9Ib1rxcZUOLT_8ooMGMAdxgIlU-p2g7JyMeTdQoHNq-rs4nchjtPHZvggkJ5nsVW9tLTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ab3271383.mp4?token=sX4i0ZxJ0fVRi_Seeiov3Uq1NTMixbiXXO5DBwjaN8r-Hm01xh9Ev2h_8n4p6Pg2-xx4nAx11xnR0EK_4WX0PZIs_1yuJxVROV4NpNV4v9-Ax8c4UVbgrIL5QW968wJyF3NRACGfgR9qQN-srda_JOlRozFAZ8o24EqY27Y7djagOStlVGHOs18AM_hYcJgmt9cEtqpQlZkQv4-L8fj4VsUQxcFBPTlkf5zFePK-qPyBGjP5tbPdyNIpLFdkM8oNbUcG--FWWKjSGDFXE9Ib1rxcZUOLT_8ooMGMAdxgIlU-p2g7JyMeTdQoHNq-rs4nchjtPHZvggkJ5nsVW9tLTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
هفته‌دوم‌جام‌جهانی2026؛ شماتیک ترکیب دوتیم‌ملی ازبکستان
🆚
پرتغال؛ ساعت 20:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/24148" target="_blank">📅 20:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24147">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W22cbm2jQv8j2ctMQu_89D1zw86CQS7DrsP6kWJvbYM1b0znfCtJadGXmpXNd9yWyffFv3sK8uSGtAbn5AzRG5huC4-xOcR33K7hXF3NQFHBLPGqqT9ZToTdCkogUsp1EumGWcKvUIP6Q8xqMxkuTDkZ2G3uL75yzwbHHeEY2FHGgx96yB4mbZxVmwJhjWkjWydgbLgHQw5JLMGMw8eRAFK4ZlP_PzoN8_8alXN66lLVE91lAAdcFlST--ZXl3F0Wi8pc9jUh5j_NA_TqeMQjqC4r7gHzvJ5KJEZzLqmyGuk5phhrrkY7V-Ebvj7sEYeoAZUkYtjt_sCVwZNrhqx4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛خواستیم‌بعدِ بازی امشب ایران با بلژیک جزئیات‌مذاکرات‌روبگیم اما رسانه‌های دولتی نزدیک به پیمان حدادی جزئیاتش رو منتشر کردند.
‼️
دراگان‌اسکوچیچ درمذاکرات‌امروزخود با باشگاه پرسپولیس دوشرط‌سخت گذاشته است که یخورده مدیران باشگاه رو برای عقد قرارداد…</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/24147" target="_blank">📅 20:35 · 02 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
