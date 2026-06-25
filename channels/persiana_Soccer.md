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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-04 11:10:51</div>
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
<div class="tg-footer">👁️ 27K · <a href="https://t.me/persiana_Soccer/24265" target="_blank">📅 03:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24264">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🏆
جدول‌گروه C جام‌جهانی 2026 در پایان مرحله گروهی؛ برزیل بادرخشش‌وینی سه بر صفر اسکاتلند روشکست‌داد؛ مراکشم چهار بر دو هائیتی رو برد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/persiana_Soccer/24264" target="_blank">📅 03:45 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24263">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CNgubZPLOyqo8_G64h9XHsE4F-xHcJYifurOd5B_UxiCbkg9Zcr-fpepDNR19Fjhulx4I5j_aIZJHJCKvXnpVMpRATwuHz7R49BZMYbQ3O-O89OmiRKz74G9W5zOiv8z1sB190L3kukrrvRuHUK2OWjZoAlZhNt0Hc4eclmlroN4owSywJJ7T6UU1GtbggqukwHWaypkqJSPFc2u-hRmw1iGo3VbZm86Oi8Q_sPfQUjNjnLlm9joODDQPnLkAhKGcf1SwJcUpOxcVeXvMFMuq9ueQXKMGmLZ_KUvEkD9dZ4dGoT36XsCyia9D39Kxxyb1LDlDpq9jfN8TqRYLTX3nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدول‌گروهB درپایان‌مرحله‌گروهی جام جهانی؛ سوئیس، کانادا و بوسنی راهی مرحله بعدی شدند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/persiana_Soccer/24263" target="_blank">📅 03:37 · 04 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/24261" target="_blank">📅 01:37 · 04 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/24260" target="_blank">📅 01:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24257">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vAqxVhi-xhVLwL-_114Gj1euJBYbZnBC-mV87Xl6gGIiFRn_MLP9I_qV2JFOHgyLor0k6GnqZCvbANHceHrQJgfHnpCYsY9kcuIfFuT8SGEKLlSmdpXjasx6UXVNkOD6IkqeRpMsZd_0Z3vNiJF5z-FYHfZW3e0_9M1I_TyVvure0H1s4CED8RfN5zV4ciRmNN6c7p8wlMVhqlVPhb9XL20SNgzZ6P0vj1Lg35eoAl3evXqqysrE90Q5fMWkFRjWttk7Tad9_crrVBkQV3XVIavO_w4cM6ASPQ6K-5rEiCGH7BjiCZR9QqkuhE-c0v2bzZ7Q44c1u1TuA5f6WbqRGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارهای‌‌امروز؛
از تقابل حساس سلسائو با یاران اسکات مک‌تامینی تا جدال ژرمن‌ها با اکوادور
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/persiana_Soccer/24257" target="_blank">📅 01:17 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24256">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VxRp3WBTu1-XYmH1bzf9gbp5j_dJecfpLkrqYFtvmPBd-3S7bKJAZZ2ZjHajJwIfWWafNpS0SXLLL7YSrIMlwaYpPzY42WGu77TzPeKkcseNfnRJjK7czj3ygauXxZw_aaYrTH4azRKNiWqmPpFAlZw3zCMJOn-YcPXpLa4-y_S6qViqa1PmCmqam-ybsl3g_E-THKL6Qi2rpdDuMjsfUgdeS6spyXsU0QVjIvQmzI2tSLo5RRq5vVQ_T6ysAdVFeD5j1kT63NTHtJ6rCjoJITNGwSxDDoeMr_OOfE3xlRz25tzgVRwxYybKpIBsPAZhD01J-m82GYkiyUrvlZYxJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌‌‌دیروز؛
ازبرتری‌یاران لوکا مودریچ برابر پاناما تا صعودچهار تیم کلمبیا، سوئیس، کانادا و بوسنی به دور حذفی رقابت های جام جهانی 2026.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/24256" target="_blank">📅 01:17 · 04 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/persiana_Soccer/24254" target="_blank">📅 01:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24253">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rja2Y722oDhlRgeNdP85W-DIYHXVgnKE-QgS1IwlOMrGMNyX66FGYtZljHlqlILDEy8fHEpjaY1zK2cuUmgeDg7333ZT6wpnYK-fmu9LJGbHMNllT8B2ekguuYLcxHkIXzzkgm_3wPnpudvL6qGxVyZ2jR5KzfLY2yyWqQwF38zUppCSW5EQjyMV23Szs1MjKQipZbBIGpZ7C8kTKlzMComMkVj7CMPd8Fp4NHM06giIifOMtqK-N0pfa86K8ByinpB4R0gENhbJu1BFG1WHRXvLkun-ovvovEW2G0ptgKDHh0MeWYa5YoMcuk1kQyZV-UyddJHjMx8RlKzIhBFaGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ توافق نهایی حسینی با استقلال، رونمایی بعد از آزاد شدن!
🔵
همانطور که درروزهای‌اخیر نیز خبر داده بودیم؛ مدیریت‌ باشگاه‌ استقلال‌ شب‌ گذشته پیشنهاد مالی خودرا برای عقدقراردادی دو ساله به مجید حسینی مدافع 29 ساله تیم کایسری داده و حسینی…</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/persiana_Soccer/24253" target="_blank">📅 01:12 · 04 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/persiana_Soccer/24252" target="_blank">📅 01:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24251">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NPBTEpmooGYncWJmU86aNsmKN74R7W4NmrR3Y696cBp8k2mK8m-f7hvEziYAk2m8ugd0kTFk4JjqvEg21r_yiSVn8mshkf8nvI0O2clwLL3BTvk-gnOvZCXn-j-gE2KLyI7YEnlfMoCfOmkqYLv2Tj6pzVP34_jKU8WS3kbIvPl2cJ84U-XVy4cvxZfXZmf6womWn4WMkOg4yYuqD63p7AxkyvaMOhhm75YXbgtTBnO2ijsqVa183T9hi-dITeAkOOqaY-vbTnIInA7zFGPDPB5HdZae67f9QWbXmeDXD-Mw46x1RbBm7QlReohjdgg1DSCyPtUPuufWSvqwRmB2tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
هفته‌دوم لیگ ملت‌های والیبال؛ ترکیب تیم ملی برای دیدار با فرانسه؛ ساعت 22:00 از پرشیانا سه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/persiana_Soccer/24251" target="_blank">📅 00:53 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24250">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WSJoacyYojNFhvFQxq2Djs084GLCTDUVYQ5mbeHCaaffheZh66pCiCkU801z55tFc9L9c9e-TbiemXB98R_KRmMXib7fxMq42PxPTtYwlnThQGAwcc0rPP0-Mxv3F6Gx0eOA5O_26uht-xA4SndZiQvlWoA-4iWgksAmxzAnDfAAA8vWFHl3GmFUQx2ht1o_xVy5jQs3GYvkSDU4bSTI_FIJGHkdt87jTx5Zmx01B4qw67TbgyeCJ3jGWGbTFIVHCbF2Fg1B-5CSof0sjmtGsRC1b067gOW40t41BDafvKQ7Ir6VcVonCEQvhr2fAMfZMLlXaliBisLZ4zmMIl5msQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هفته‌سوم‌جام‌جهانی2026؛ شماتیک‌ترکیب تیم ملی برزیل برای‌دیدارمقابل اسکاتلند؛ ساعت 01:30
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/24250" target="_blank">📅 00:42 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24249">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SNyWyV3XrR_UzJ1S-F6HbHBHR_rzsgTbQB6gGXasrrwithQs8W4zJYVMMRkzIqkGsYQKJ7JkpP0COXaW3xHDTltyqMxFa5FFQ-MGfzj7ZrTocTwXh-Y_HxTA092WLhEe-5SdSaIfROWxvdkbTvh4gaMaAry8SYWFi6V_aAKZ42yM1cpNgLKzm52Hjm5k-AocajzEuD5QKrxJRwjajW6UViW7PPnLQpOB5KQNTAgW4txgTp1zuUQ7lYFIAyO5NEAc1BSiqZw-BdwHxFkRz-VkBNzTgROfUyNvZl379oPlTp7seFL8VPAWpyT68fqQHhcKrUC5Yo3ceCER3PkA8atfTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛ آغاز تقابل‌های جذاب و حساس هفته‌پایانی‌دورگروهی جام جهانی 2026
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/24249" target="_blank">📅 00:38 · 04 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/24248" target="_blank">📅 00:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24247">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/po0N8SYrs3Zx2uuiD3B_NKmRAP9pgAP4XoQDiXE0prUrSKKCS7tWWDXwByx0oE8IW1L2Pq7Ep4EUEmpKD1fISxI3w2nNOMjZ_OS1IgRTt77vJEis3MZDZE6bldkad4eALuH6xMe989D3CpDqtAJ8oCP7IBmAkWLQGbHS3UAKAYc0gWSOar_PRbYtdQa9QFcPB0-ieewEF3wxKSvBOI9NI9J8QUdjalGmeJK_kTceIaoqR3B0tyZtjnhOh81_zL3wWYFyZHAfkn9DiQQPCFAMBQ37dzf6s3NLN9UbQifVG389tMpmVwBnwSPzXiQ-8JNcZGhH5d8xRYkm8mTxPn4btg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ با اعلام کادرپزشکی تیم ملی برزیل؛ نیمار جونیور از هفته سوم جام جهانی میتونه برای سلسائو به میدان بره و مقابل اسکاتلند بازی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/24247" target="_blank">📅 00:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24246">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xd0prh6vQu6XzsSfY2VgMzs1VuUxVqRsN4x37-UwKoAkZ_UdOkgMuIL4vvJDG3jz4Zj5PMWtvKuZZ2ZA6strUlGHZ1xiTxTmgC3RD1_zah_6CHBr6PF-yMCFg7oGdWdpFC2GgZRoNbp3SkM6fvBFeX5dQ6NYMp7H4X2ySaFJntMgxNcsh7ONw3oyr-q2zp-Dk_opeDxEpG8plB9E1el3rd1I7f1k7f2FBdkUWnTOz_ohHOuokJHt6dqjVlw2-DMycDbKgMXs_wSz6rnndi9kHKmEe54HD5xECcZBbLvFoxWA24Fbfkc73TDemhhvcjbMLTqdVQV0OZD0dNckqghmQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇬🇭
#تکمیلی؛ عملکرد کارلوس کی‌روش در تیم‌ ملی غنا؛ پیش‌ازجام‌جهانی‌تموم بازی‌های دوستانه رو واگذارکرده‌بود امادرجام‌جهانی و درگروهی‌که دو ابر قدرت فوتبال‌اروپا توش حضور دارند دو کلین شیت کرده و باچهار امتیاز در صدرجدول گروه قرار داره.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/24246" target="_blank">📅 23:59 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24245">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E8XVL2u1nYnGRmWjx71l9xFKRJ8G3jqNNsE1ZfOolhcwtORgA52-XJ2Ae4KkNrdhVcQsfV_nib8qMeCFQAWpbRHqfGa_cr2Mm8Uv0PUeT2a3rWe1S8gqLZsHRLQvEslnXy4ExW7uYc2_i1HUL6nqHbEfmEAgVD-SJ0XV5j7Xt94Ei5SRjxrIi3EFkSe--wB46c_FeXdpgLa6Jwrt-wsGj7Xn-MXC9G64GSTQMfL7Tbtp3ICSVZlnSBQ32WFnBRNBx5A7wc3gyfgUAEOlEUjr4BgblE3ZR-lkycU3h6LGr3XTJcY9DhcfZchGrimUDdQcHyCjTnLer302HfmqqdO2Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌پرشیانا؛
محمدرضا آزادی از سه باشگاه گل گهر سیرجان، فولاد خوزستان و نساجی پیشنهاد رسمی دریافت کرده و درصورت موافقت سهراب بختیاری زاده از جمع آبی‌ها جدا میشه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/24245" target="_blank">📅 23:22 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24244">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kzqaYIdBvR14VtCr6R1hpmTsrK80Z0s7YrIomRkXH4Y8xtWOzRRzorotLbDusgq6wVe6Do_dsd-EEo_-9Yx52HCqhmiraqo5hPKIY-ZaC-6tMRExbkywYBLPP4p8ifYv3G79UVY4Dzs15WRpMtg3OOyskg3qKDVvfLE1gB0iUbS2JKqIBR7oAXAUIhgj16ARL0yjH_3CbYlD4NVtGTY-wkVRsi2GVt4w9Z0lF3wV1FaLXsVTiEuxr1Nqio4f28IX-2bmJY8usdIeELw6YSzf5TlyUAiEvggjqMfaw9a8ytSKBfznDfaPI-0iUoqW88qr7pNpueyfMiPxlnJz25uiIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پوستررسمی‌باشگاه‌کوردستانی دهوک عراق برای یحیی گلمحمدی سرمربی ایرانی و جدید این تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/24244" target="_blank">📅 22:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24243">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e4YJEOqf3qlPEN6HVoOA1QtY3sVSAVaKP2bZ0iFdI5FJGLjeJ5PCSR2iXQwrJ9q4r1LV02jh9Wd77LULdVkNacVvCnnV-uqDNJbS1jejE8L-Ba9CTzfGb6XMYQ6Uo1qtGQ3ZefTz68KltRE3XtBo772R6QkcJp2hFlvbQ5L7_Ze5fEV404__gVHPZcr9XNlfjN62TXM22gsBTN3C1utVQBvckRFBpA1ibJ14Pt8bKiEegyJ6UdWjWvROELMUkh4lCQs5hrc4gbIw10-_uYGG9RgPOjL-JWCFfNRgajpf06L2uAk0t3Kji2IxvwUbw2s5_vehaLQnCwzej6uiFaZkaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
🇵🇹
تمام گل‌های لئو مسی و کریس رونالدو در تاریخ جام‌جهانی مقابل چه تیم‌هایی بوده؟!
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/24243" target="_blank">📅 22:51 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24242">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">📹
این چه سمی بود دیدم؛
رونالدو، یامال و هالند درمدارس هند؛ ارزش دانلود 100000 از 10
😂
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/24242" target="_blank">📅 22:51 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24241">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dwy7vI11P31tqyiXHKs-LUKHIk0iYIICLD8CLjbJ8Z0mjletNeXqvL9954_RXs02-3WJWSgA5_Y4jwt14614Gcpncickuxm4U3Rop3YoHzbUgW5gGgL31OVaKHry-y6MInjLVSiP01__dLvdHYvuTj9kg5UqAq37PcDXOkLBq8JX637LcnCc0oFtBZsGcuoXNAyAEK69miseBaNKQFtuud9QIPy76CUTc6_hJSLCdKx6EneLTKauu8-EU-IzUe7uQZESLiUzoOLz3K7U_r4BV0HnRgoTtz7HIVTfdp5KhAfqahLjABnwOBUvTwfeKn3xzWc16yVyY7vWii03IWt-rA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/24241" target="_blank">📅 22:51 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24239">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MEF5adlx0z-lB35WRmpC2Ex0J7CHMx4tgPxXir-JccZEO5f8AFqmEOlfDicY52Hq82UX9iYoVdEH0BuNHoA4rmGWaUmsQsqPoDpSRADJ_9eNIKxlqFy2tkWxi5Ah9lFdtAUG_2gQUuDFZ132sjog5KayHKqhpPKIikjtc4aZDuAAZXwEUMQyO4iKIEfEbpNM_3jU2jPXhMiXqhq1fba0VFpS-1DXojSPY-FiGHgdPoI-gk4av5R_x4kN5Y2RkRKSJ5N22Fb9wqXXIbSAnuyJJ7r54vXo-D085AU1g3ncIGPalok2eWw8rlmOh54dXfEhtZsjoDr63Ef3_TTwLxoDPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/miS3OhvhxiXd5GWUBSzVKx23NgN6_ku80wzHUO22Dxqgn8BnNIcXvficij4XPGldBqwvdX4rXKEXttARw3ENch9tYs-fDBJVS9oyzZNH-O1LPWKYzifb_-rX2yTLEpu47LYqgf_fW3DqViQkSZ2pRf8gZfdlTVT-eq6XBnpUF1QmX7VZxbXhv5IpLfOftKE5ouwsfz1jsJ7POq-PwA8EYa8b0ha6jNuqG1iS6QBxmvOz8awGDeqEtTnQqcr-eZKNY55w1KwmTCM49ILa_vNhnC2-QCYdagQsXimMbAWh6ghpnmBTalX6_D3KU5rF0wcwj402M5Q35m1naCZ4jk_8bQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🤩
🇵🇹
تمام گل‌های لئو مسی و کریس رونالدو در تاریخ جام‌جهانی مقابل چه تیم‌هایی بوده؟!
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/24239" target="_blank">📅 22:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24238">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d46a7b1648.mp4?token=ODcFHq9YfUnhZ8OWAQ9E7RsFdWvfXNKiayKBonthjo5Ohc6yadx_nzUYFDAdzh91iIDaI8K9gXZDv1klBAMHL8w2A9D1sFtQ4nO3esRzHxkXo8O6_cz5X0KfrmleHPky9XhWVk53zMPaDvjcGj2de_37HCn9Z8Vr2VXplT4r1RzqYcc5q3vEveCRJzgLTKnPvLcULbViv_NY6-B8lmfhisXiqeDBk6Mz6Px3O1ydNG2pEWFp28PXyX9pk7UjvJDz0Q4vUohiWGB8JJvKWSduDoIrrkoYVkkEMH2Q85d4SpS8_-Dgd6YpreZtFvWEjstZ4ghE61izT4AE-40PCISCOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d46a7b1648.mp4?token=ODcFHq9YfUnhZ8OWAQ9E7RsFdWvfXNKiayKBonthjo5Ohc6yadx_nzUYFDAdzh91iIDaI8K9gXZDv1klBAMHL8w2A9D1sFtQ4nO3esRzHxkXo8O6_cz5X0KfrmleHPky9XhWVk53zMPaDvjcGj2de_37HCn9Z8Vr2VXplT4r1RzqYcc5q3vEveCRJzgLTKnPvLcULbViv_NY6-B8lmfhisXiqeDBk6Mz6Px3O1ydNG2pEWFp28PXyX9pk7UjvJDz0Q4vUohiWGB8JJvKWSduDoIrrkoYVkkEMH2Q85d4SpS8_-Dgd6YpreZtFvWEjstZ4ghE61izT4AE-40PCISCOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیویی جالب که لامین یامال ستاره اسپانیایی باشگاه‌بارسا امروز داداش کوچیک ترش منتشر کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/24238" target="_blank">📅 22:02 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24237">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kdPwz4Q3QbupmtN8-AzhzilltccpO2nQOv7wVNt5iX7ACTKvaMSVtSlFr-hebkFcohzf-lkq5A-dgfSrCDrti66HDF--IkNVcHsMojKIFIXQQmUsQ98osuEEBHm9X4oYv53QTE3sg1Uz45tnaCtgy7JOEnxbSD26NSb0K5p_2YxlKqkVtpf2mnYbjquexxEao8-F-ki3gpNwRdSxdBiBH09W17AbK8-WMH1ghA5wCt-VrEV19vtXy13Pz9yVEw4qdpheVoP43VBFwZLpZCqBSCN318jDfbK9Bc6pO2B3iHf5NZIQE6Vqwsk4mw93BBcCUAt2dNrChcHGe5vf8x0n5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
مسابقه امشب والیبال تیم های ایران و فرانسه به صورت زنده‌ازشبکه‌پرشیانا 3 در یاهست پخش میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/24237" target="_blank">📅 21:45 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24236">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nv6lIzXjUTLae0f7uw_mqsR2xQz9dAgfPBAnNV-ymFi1K0bLSvXrTpzv2xA5v-Im58N1-7hh4wJZFGtNX1SzfJWv26CXDxuiYuAOxSwID9jQdxo637ry9Chyu862xupSK4Sd-r8F0WYeeXKoi7Vky4dDoA8HddGxOuwBNaJ1YJW38sgRoHhc7MLJypMMGL-MOhU1CC8BLvuR06QKg1zXM13Bu73V9DYNZbKgypqFTBxiH9E5u69yhRrBgWoZh7U-PwKPuSC7fJCPViNrQvXhhvqCgsEM1fGvPX7RPbY_yrwjpiCKw0EXwxtlTn8hkRV_S-0xRlTRmIaVtcugf8DW0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی‌طارمی و سعیدالهویی، مربی تیم ایران به محض ورود به فرودگاه سیاتل آمریکا توسط پلیس بازداشت شده و هم‌اکنون در حال بازجویی هستند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/24236" target="_blank">📅 21:28 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24235">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rlhZ9ODs4zfSSwaw_MQwS0VFMm6ZtKkw_aT5C6C9h-WcJ3V3yvdmPUusQeYbyDYUTy5-zxo9Z3JL7EOzDspYRHHJA40CnsBurRx5QZHM5QAp2ZwN1DITqCqYQLzqJObl8ef065NfzsVSotsoIYx-ZdgmRJbJX88brACkNfWEBskiOOVcioYvpC0fTUza6nIC2oCkzOELbA2bF3PbL7mgVU3Z1u4BhlpNDFAnC-tGy_IprLFhKBxhFY3ted5xYJCyzyhMxso9crWzCYnroXfKeTGv6nmtPIwhCucnUoldzEM_thqZnsplSbhNvvs3x98SeOIa7mvkue4vdYxAi1wsJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
طبق‌ شنیده‌های‌رسانه‌ پرشیانا؛ مدیریت باشگاه استقلال ساعتی‌قبل به مدیربرنامه سید مجید حسینی اعلام‌کرده‌که درصورتیکه‌خودِ بازیکن رضایت نامه‌اش رو از کایسری‌اسپور بگیره و بازیکن آزاد بشه بااو قراردادی به مدت سه سال امضا خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/24235" target="_blank">📅 21:11 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24233">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JW-FaukMC3I2DYvVfuokatgYa3MSiSME2QNIYn-WtNIzf1cYYO92gCmW2zx2lwtO7CIZv6LSRh4yskqdU700LdVBeOLekujzpH4ouoOD0ayinaUAB8Y7Xk6CUozLKtPSNklTtBHWqjsPP9c6Qz4TLZBkpl8IgYi2zTXz9-l8VxQ9GPQ0xbxFBwHX-GEkjxVhgG_RXj3xf-r3EsB3pXi7xrkwyFhIadW5pmCSWitTACwFhdTJ1UVcgvS20tL8t_zdRzgKNc3YrdNhvwVidzlNq4zxY6ge2H9jHecOEbx9TgLhn_awo8i4H4CdDiD4Rh4aNUln3FBDBFCRpvyZ0CfMEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇵🇹
ژوزه مورینیو سرمربی جدید رئال مادرید:
رئال‌مادریدبهترین‌باشگاه‌دنیاست و بارسلونا هم بعد از باشگاه‌رئال‌مادرید یکی از بهترین باشگاه‌های دنیاست. درباره کریس رونالدو بارها گفته ام اگه از او متنفرید دوحالت بیشتر نداره یا او تیمتون رو به شدت تحقیر کرده یا از بازیکن مورد علاقه شما خیلی بهتره.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/24233" target="_blank">📅 20:51 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24232">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QetI8NXzBzxuFvsnDnwRULKaBsgeIqVG1bLrV9jzLudZx1PFrBhMqZ5rwLzGZleouvaKha_3F1iw-Cv2OHS-PVvaE0UYKiWCE0sos4_foiNrcJWeC3PyhnjHqXMTgMOA13PEPsFy167X_kcop6i1mchVJDgBz_xBCboOmPWUDODKvBKD-BCf88NpKOX76NmvFLXHiYWAOZjdTBWCQ9WW1hQZEKQMfF00W4GQ_S4n_gGeDip1xC5SBSaGXE7sgFgNOG-_pZAj8fkGXfn7vuFy5qNT72MZ8abw8oOZMLvxlEPVhxDmY1aJB86plf1NbyaFGQ7ng2wo7oYW1KaCEDWTQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
قاب زیبا از دواسطوره تاریخ فوتبال؛ واقعا هر دو بشدت دوست‌داشتنی و محبوبن. حداقل تو کانال خودمون برای این‌دو و تموم هواداران شون به شدت احترام‌قائلیم و تموم امار و ارقام و ویدیوهاشون رو به‌یک اندازه پوشش میدیم که سوتفاهمی پیش نیاد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/24232" target="_blank">📅 20:13 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24231">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QQHToVcTOItDDp-fDJWYKWI9-NCg_7IBND8dg4MNSv2mH6ck-YyUg-kD3oNJYpfRp82-YCSXxFIKULVj3yOcW1wWuq6vvt2gpgFsshMs3OAwuGAj6ATT7CrL_NO8yZWdwH5DHHQR3CmRgn2VN51R60iKNEDZc9zRWuooKj_jMgYQvIB5G-tgCt0LsvHdcH5mw6c4XW-f1u1IyYtu5OyNmJ1Y6Quf4Vs0fmjwluseohJ31w8BWMXyCTbBpfrOZiNI4Lh940MW-bhUrrqJEb_ekRzGl0s7Gs5KtYI2iMNA78DmPbaTKM9n7D6zmYhImPttzhp8Mzmhx0Vs_l300fkrPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه‌کامل‌دیدارهای هفته سوم رقابت های جام جهانی؛ عین برق و باد دو هفته گذشت. یه چشم بهم بزنیم میرسیم به بازی فینال و اتمام رقابت ها.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/24231" target="_blank">📅 19:57 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24230">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qzTjADCYkDh8M0yiHYQ0G7NwA9-etMxQ5_oq-m4uBVFZRVjj0LCHotxVSzt8k5DPB6pe6Ynh3NyUu99mKcvnDLfnbYj3ZBXTtFf0P1Jvgj0bI-1cPwTiMdeL0V759EbX1SftfGcEOGToHbJwnK5NDxIsXCJS0KE_rBLW78jUb7aPu5Ka0fHzGcSmxf21d0oKsujn1D6FhNYaJZ83XlhlCIQI9lalp3OD-z0lVgHznNiHJKhVu7ZiqgkeHTLaDuo9_bXv_ZG_BbxfZJ9ZlbWuLdr6gUsLf__KJgkotm7bV-e47J--Jeax27Amda7U4wtlwQmrz0IozrMWaYPXO88-CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
#نقل‌وانتقالات؛ آلخاندرو گریمالدو مدافع چپ 30 بایرلورکورن با عقدقراردادی سه ساله به اتلتیکو مادرید پیوست: هزینه این انتقال 10 میلیون یورو.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/24230" target="_blank">📅 19:41 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24229">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j1FeXTbkZfNWvYIIrtRtYuXhTFVYs-Hb4St69Kp1b-tC3RAeKdUhYTfLH7DTDci4MSWB-vBv0RdZLjOwIEtuLKA03fTX6GBe0i1_cVVha6poB6t4FYagoHed3Qr7K9lO90QsTUE7tWQ2onwne9z7Gr4lnsN3TI49GrF5vzjz4wJQ1RK1x_0Xa-wkmcq2ClEgJ7vYCjVRCcgc2HJx7iV0VJUER_dJvBk_5Jly_5-IiPIMPZ0hykY4C_XAB4g9WgiE5jEPGaetbQgH5Yt_0EW37SOVU1kHiyytwn4j5bnhJaj1QYdW_p6oYperkKs6ciW-rIz_QtjVEqwA-5PDD7XFxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇬🇭
مصاحبه جدید جادوگر تیم‌ملی غنا: در بازی باکرواسی‌تمرکزم رو اینه که گلر تیم ملی کرواسی رو طلسم کنم که تمرکزکافی‌ برای این بازی نداشته باشه. صعود تیم‌ملی غنا به مرحله بعدی نهایی شده اما اگه کرواسی رو ببریم میتونیم صدرنشین صعود کنیم.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/24229" target="_blank">📅 19:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24228">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lrfb_rMJo6dVRXgUzp0nkxtlJaecSTI0OW-NsrxEUgKm53bSXm4Xn4MFp4ODaZxNvCpTJRWAekRFh5Q8mrjk59zkrLjWWicUQpSIY81Zu24flDYoSETzcAp_4OIsOdGXR0AlBVuxxkqmd7uQ6xnYNAXYHBibp3qmcHjyTkFxD6bT4tByNB_LpbfXUWkd_46soPMkYElByCDZDjJMIn1FMYOxmRH8P4z2G2_n9-1Qp0XTecInkTHpZVVlAooXFsVAz_XhYSRjW6lkoyVNbuz7-8eDDvLQf37u796IaV7txFPxz57TL7f_iT1DgjktCq8bd7PfwAeyx2FJiYPi31am6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇬🇭
مصاحبه جدید جادوگر تیم‌ملی غنا: در بازی باکرواسی‌تمرکزم رو اینه که گلر تیم ملی کرواسی رو طلسم کنم که تمرکزکافی‌ برای این بازی نداشته باشه. صعود تیم‌ملی غنا به مرحله بعدی نهایی شده اما اگه کرواسی رو ببریم میتونیم صدرنشین صعود کنیم.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/24228" target="_blank">📅 19:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24227">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v6pcKIrpUXDGNKu1UX7OCHVlItVawIPe9ilDVwIUvBssD3Lxmn02lz3gD81LEfj3qupd3oJW2ECmG_rxdxSUaLhHRmoUOtyI6cE4fT6HUUslXhAdHlYRFHaTAceqDeL53IU1qGqiHe4H1aq5qPHbGV1ZwVALAfaIzpuUKKyQP5JsqUprYkmYEvT0Lk1bDqoh4fUJbtb6mw1anNOgqF1iglIkynT7BkNHSxogE313__Ov1MZAEjXLub__eAqhMK0tjBtQfMETZh9fJawfXUfQrNNU1LsKOQyz81a-0j_L8H2cpdYLvk6k_w1JCKBDGuQTHD3sIAnNhtmLWTYHVbOxuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علیرضابیرانوند گلرتیم‌ایران در رتبه دوم بهترین دروازه‌‌بانان دوردوم‌مرحله‌گروهی جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/24227" target="_blank">📅 19:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24226">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc38571967.mp4?token=UUJeFfyBMBYFiNQ2jGK4c8kU8BT855kbJDdkBFrAaAXgKiR0-bhiX_bZmtVTRtyk6Ms95DTGaugZZnYyIBb3Ra8esk-NB1eFcXcX6BExG5NBjKggSvod4JSZgLwdVnmEqE7zXY4Mya8HNc5IkC0PUaBfWabLH2GUhJbFHU4rqtl-8B9C94L3wOcO4KqRFnJXosvVSD5fpQzDSnO9hRpZNZCs2eB7g6Dy7FlxPp7Kh5GtfYZKJJlEm5u3QX1nnFPapCAr7WbeoeaFTcP_7R4IpztE2EOTHSFURbkps56dQfUtef9U9wQNvjL_6pPz_AgWIvze2Ox5iNIOt6Io1HXi8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc38571967.mp4?token=UUJeFfyBMBYFiNQ2jGK4c8kU8BT855kbJDdkBFrAaAXgKiR0-bhiX_bZmtVTRtyk6Ms95DTGaugZZnYyIBb3Ra8esk-NB1eFcXcX6BExG5NBjKggSvod4JSZgLwdVnmEqE7zXY4Mya8HNc5IkC0PUaBfWabLH2GUhJbFHU4rqtl-8B9C94L3wOcO4KqRFnJXosvVSD5fpQzDSnO9hRpZNZCs2eB7g6Dy7FlxPp7Kh5GtfYZKJJlEm5u3QX1nnFPapCAr7WbeoeaFTcP_7R4IpztE2EOTHSFURbkps56dQfUtef9U9wQNvjL_6pPz_AgWIvze2Ox5iNIOt6Io1HXi8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
۹ فکت‌شگفت‌انگیز ازکشور‌های‌جهانکه‌کمتر کسی میدونه؛
دوست داشتید تو کدوم کشور میبودید؟
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/24226" target="_blank">📅 19:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24225">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/ruSzolWAfpYNuqGziDVdTl_Qi4OLbOUXzNGS1TL4DUR1-KYUZ-wENE8n0YAllKB4wbJc9NC77WWg8fi9ATmwE3j1_gor54Yut8VHp2avhg0zr_FMuWHfU0duoMLoG-vMBuxp0TZG9nLRutK0lCzeAirhtocNH1QzZ0ELIJk5V5FrRjwitXNKiJRcTJRzSulKb0Z92RIYt-nmMY2m4HeuZVYIeYwtgqdCUbnECjrg5-eXdJvtCtyrSTrb9iRCMIun89lqzkCZKQsz3CTvUjrnoc5xKuYnGnIWx3sxg7_pmYqMXWr3XVrUvM_R3_IZf8RfbGFo6V_711e6U6vmoCx2uQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/24225" target="_blank">📅 19:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24224">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0eb571605b.mp4?token=Jzc0n5XVLS9Qw0E7JorPWXEoxHeHZTUYF5Uj2XGfQ7l2bw7XDHd8k9FQ78_J0wodXTWy4bjdzBQMbvir-SNi9wBRo9wYKQLz0cmbVXoXLL-oAx9KBGq4sp7FXOpnZQvnm1_l0a7zfh0nS1yAJ2Ow0VUuI8AWtQLkq5B1c_lzjEcIQzqr9d6hoS6TvU-VRUrJCXadzUKIo4Ycyuc4GBcWS4UiO1kNgYLto1KdNN_ID0S_wfOauZh4TwS5VxT2r2i2EHocKMqMwd2A3Kc6DOcM7a-iJg4VM3Ujf72P6G88U61m0AY9_79aHW85cLMTx4b60dqyoDcl-0GxMoGwXtFGQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0eb571605b.mp4?token=Jzc0n5XVLS9Qw0E7JorPWXEoxHeHZTUYF5Uj2XGfQ7l2bw7XDHd8k9FQ78_J0wodXTWy4bjdzBQMbvir-SNi9wBRo9wYKQLz0cmbVXoXLL-oAx9KBGq4sp7FXOpnZQvnm1_l0a7zfh0nS1yAJ2Ow0VUuI8AWtQLkq5B1c_lzjEcIQzqr9d6hoS6TvU-VRUrJCXadzUKIo4Ycyuc4GBcWS4UiO1kNgYLto1KdNN_ID0S_wfOauZh4TwS5VxT2r2i2EHocKMqMwd2A3Kc6DOcM7a-iJg4VM3Ujf72P6G88U61m0AY9_79aHW85cLMTx4b60dqyoDcl-0GxMoGwXtFGQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
دیگو دالوت درحمایت‌از رونالدو کاپیتان تیم ملی پرتغال: "فکر می‌کنم دیگه همه بدون کریستیانو چقدر توی کنار اومدن با انتقادها مهارت داره‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/24224" target="_blank">📅 18:47 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24222">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A5kjT7O7IFZliOVszEcuU8TF0rQoIEu_Ron0XJqWsi3Mcrh9p0Tc-j6gN1DZx2K58ISO1j1yjVXyOVWUFjeAE3GpcDZwRfBI2YQvWvcJO36PiVFQ4-ZbNA6R7briwxoc96DlSb2AfqY5ceyM_r8X5RQo8_WvIttjujsz4DvwRU9FlN5j8nx0vVUGH_XMgdc2YjYZxSibl74MdijI-TS6v94VF3RVir-HnsuGSSFh9NX8hndeLgYW9JmC6wRsuiMDSaqadyQRxV0KQXL5ciiYsE2n9RYsxPB5loKCVGiXXAmzJwC6dodRoqL-sOwEt-R65MlssCpSxmgtfqgwPCifyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BDzLA0hzuyf8IP7HbdtXfv8sDAtZgYlxQbJ4wdPuDasp_qOVyW_71He7pSvJypZVKbUre0AQDpBICj7CtabkQK0_65HmADqCKLJPA6c57449QVLGajmEWRy1z_dXIkwvj2IUQNVzNHX7_fX_ua_0HNf6iVsC6PDHzGRddWLbQ3Go6iqPJVLFDVzDHPMKsFZzdrafmQ7MzBZ4f95Ru3DJD0mTzIjswPHA0RlS8K17fFFrjuf7SxDBVAsyQGNxKC4yUVLspYLd48oj_dp719JS8yMneFmZnwmVCEwu6uTcxM9FOI4hHqhRQeG2Pj0oTPaUjOhrmJ0IU485NAad5hkbbg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇲🇦
این هوادار تیم ملی مراکش گفته که تیم ملی مراکش به فینال جام جهانی راه پیدا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/24222" target="_blank">📅 18:34 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24221">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yrv_sWY4zxnQFLHOt8xJNJ5QGnkreCO0HEXlCz76tZHTNYP_xMovwrT5f-1KyBAfdL4wTUjIAN-wQ_SwtQ3_m8tdUXIoJggvw08t91MmZk0T-jBQIVlQoPnof4kCRigzTfBqMHqn9J8VAx1p68YKRglEhot31RSUWI-GuJsXrrydsM1Mqj61BqzrN_xVCC6OqsP2LWALsN3NpR0oeUK8kiUJQ0E3st8xiH6cLLX0-vgoMNv3XmU4fE91ywlLrZc07JU4ZqDG1-oM8PX7hrBIIplU_rlTW_lcsgkwwysUegFT_J8d0JbeVgwQCPvbQL4GvfCCzpTOg1aoDRqDKQC0cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇦🇷
باشگاه چلسی: انزو فرناندز بارها اعلام کرده که قصد داره بعد از جام جهانی به رئال مارید بره. ما مشکلی برای این انتقال نداریم. با باشگاه رئال مادرید به توافق برسیم بند فسخ انزو رو فعال میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/24221" target="_blank">📅 18:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24220">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mOjyC2d_WYU7KtdQWaKc7W826sjCHusRZ_BbKgu9UXBVy5PichOUJl1vG-bVo1-TU0tBup04zXCC3D0K9VeUcdfLcgMKvmx4y3w4Db5hsf4Yrvo9U25geXr_dDtTWcuiJBPP35NP0Emv7gRv20PNGF94NUdoiX9-K0SJlvUu8BREM49NyyHK67-XuVqi7VHtCUwtOQIzF8DNQB7-8Fah8YfoaJH9VNgMcevfdeK7iafVRw8vYK128w8J4QqSur2gISJKIJnP1mUArIa6JA7Yix1vwRgKbzk7PDD1MpJhtRihHLwtBqcV8_P_Xc61dO4W9nZirGjRSUnp-gu2vDtboQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌های رسانه پرشیانا؛ درصورتیکه اتفاق غیرمنتظره‌ای‌رخ‌ندهد و اوضاع‌کشور آروم باشه منیر الحدادی و یاسر آسانی هفته‌اول تیرماه به تهران خواهند آمد و به تمرینات آبی پوشان اضافه میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/24220" target="_blank">📅 17:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24219">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/INCdAiLHVmyefAG62ULHgNiqL3j43LKPu5jYjCMqzPuSfmiE9PVch0uoev8MPuVMfocz4ZxaRGTkiRjlE-_dtIrVabPLsz37ST78X81rrVfXQJIWTVxAmA-68Nf42agPhI0NgjMWdgkYotoybeYQbqr9pWZ0mhHcp9jVxe5ln9lXqUyuaECaWF_S7POIl6oouS6L3Uml2HOMrEcXB0DNH2RxuUfe-PeyPwsAsUfer6HAf9SphN-ci1p9sGQwc81f5uZ_r1UXfIEfdEOD9pFy6EllcDS2dyOXg6segz_tlSxhPV6wFrIewl9PgJJQDjh1Qm0hf0FyVh5m_OMTRM8B4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علیرضابیرانوند گلرتیم‌ایران در رتبه دوم بهترین دروازه‌‌بانان دوردوم‌مرحله‌گروهی جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/24219" target="_blank">📅 17:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24218">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QBqsOlZPRjogjXy06epXDbd_kJ-qsEOJGsJ63MXHaq7VLvPp_0KBwFmtwEsGlDchQihKi2wFkSvhgEEQfCiuir_BUwI-GS5IlkLh0P1_FSGTHgzg8DTlei3XYIyYYiC5bl7PBEIROR6IrCVgEoL0ZRXil7mLGDjYncBAUb88dsnAkgd6xv-ip5wts2tJ2doWMm1i2ne6NfKua8od8sWquuDoGGab8eVLfw8ms0Tx_YbbPwefZdLJzNOmPjW_hnwNbA4q-IXGINLW4F0zVNOIaVh75uMkL8SEm3tDjWx3D4LywSObfcQiciEWL6rt_QFAKDOCeoZQjtQPCCcPMcrl_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
علیرضا فغانی اسطوره‌داوری‌فوتبال ایران به عنوان داور بازی جذاب کلمبیا و پرتغال انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/24218" target="_blank">📅 17:30 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24217">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hCeBh9bCkbqKCL4sbMD-xji8yZPXDXf0qvchgmIUUjgx1FOzl-J2wiU3oUScARzD4aScf9-DXaBMY0ox_cULntDQ2YIEHSk-Q-h0JuV6b1BuYPDvxnCRU5nTjR9gnfhD01KLYkOt0D5AdxxvC0dcNpXBvuEdJUliJ4d3pJnYiu3jla1deX50QLiTSWCd1os6PYTjttGX9sHuprtuwQ_ZJ6ctY5VkAlLxcybpTxiVzdZlkfpj4pinytFb7Tz4UQ2V_Fb49qcIoXyhErH_yxsp6BP2KHoXuwvHDoL2H4P72U78aY8P7KkYByzRDsx2PC6kG1_yCjdTNPygRdepEOTkZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جادوگر تیم‌ملی‌غنا: گفته بودم که اجازه نمیدم امشب هری‌کین موثرمواقعگشود. همین تیم انگلیس دوره قبلی‌شش تا به‌تیم ایرانِ کی روش زده بود اما امشب حتی نتونستن به بار دروازه مارو باز کنند. به کی روش بابت صعود تیمش تبریک میگم. هدف غنا حضور در جمع هشت تیم برتر…</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/24217" target="_blank">📅 16:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24215">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aC7Fwx7r6hhOGhvR4Sy4zizrB8mseU_CvyYAHQuzqFTWkqZjCSpVTQAvONwjek3mwLaEPfLd6BVEf2SsZJGQOUMrco2SPfiwi5PxZnvFOx-gwX1t568MEp_bBlvKiji13gNSEbc2MWw7FTSVn2t6UW6gOa3ao3i57wDNsKPt2_MoJzyuGi84ZfLY__jfPtf068YuxvL7g1lA7-mKQevbmtYFnc2GeNw5LfK6FDdqk8ksYwAKlwHaU3Qcv5grUCmOPyANYFQnscTNEqXKSv_L-nT0UbkLQv2NJsT0q9ZBi4utYsCqGzhIK205DpA3sAfgqdHWWk1fxey33gwiQOx4ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R7El7EyxCKO_WxYPcBN1I2s4EljJiJlqyg4l9PMP7Tre87uiVtI8AYeisNSg4n1XqvhHWxp0dI3J5_9tMnhwRLGe3EAaEfcPTGxgF_eB4H4lOp27AaBX6ZffXrXKR5EFo1moaG-lP4aipJ5xurEGBqBmW9YHUaU2JsiIBypoN_OzIHiQV-X1EBjE0ajijg7e4NwQcqD5sqPbXFeP9FoU9udUyN8cIRpnilaxZ7J3F-m8liIS33o-01S0JcadOvyKxEmNrdSyeFKiUiMIMo_sR9_HvBec5D3N3k3-6l7WhXp7Nvh-baVCqIvm_Gp8dqrqqcyRohHrLt88NfAuSsbwFA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇲🇦
این هوادار تیم ملی مراکش گفته که تیم ملی مراکش به فینال جام جهانی راه پیدا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/24215" target="_blank">📅 16:10 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24214">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a79050b237.mp4?token=ep_YY4dCpS-XpPkteLiDPpLjSTfRJ6CxSqArPw9NVX-wkYCBfIZ_ZTP9vZqSluaaye7QwBA88Gc25J6jO2bJfNY6eG1RpL5uKoPJoj12LxUxPhrYpAOjpXnCk1Jj5sjlpflF2ttgkH0pFdfcFu7ZdMlwWUTTrvq8ardJcqV1LhtFaL3ld1pjjuqwfuoqiddhE0rUVtfuu-9XcpQRMAdekbmon5_nsao-ZMuVVZz9pcqFc5MNBYreyWbK0CPbJg_aT6Xj2fnUI-Rn9S_LKpWHyQ9Ww_z9iETqOcek9-Cj6xh_gLwOMi12M_4c4kn1795IX8bW87OCQmmAzEoAHb2WpIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a79050b237.mp4?token=ep_YY4dCpS-XpPkteLiDPpLjSTfRJ6CxSqArPw9NVX-wkYCBfIZ_ZTP9vZqSluaaye7QwBA88Gc25J6jO2bJfNY6eG1RpL5uKoPJoj12LxUxPhrYpAOjpXnCk1Jj5sjlpflF2ttgkH0pFdfcFu7ZdMlwWUTTrvq8ardJcqV1LhtFaL3ld1pjjuqwfuoqiddhE0rUVtfuu-9XcpQRMAdekbmon5_nsao-ZMuVVZz9pcqFc5MNBYreyWbK0CPbJg_aT6Xj2fnUI-Rn9S_LKpWHyQ9Ww_z9iETqOcek9-Cj6xh_gLwOMi12M_4c4kn1795IX8bW87OCQmmAzEoAHb2WpIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
ویدیویی از تمرینات لیونل مسی 39 ساله
؛ نکته جالب ویدیواینه که تو هر بخش آقای رودریگو دی‌پائول فقط چند قدم با لئو فاصله داره.
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/24214" target="_blank">📅 15:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24213">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FwFx3QaSo6mm3eFI_ljBqer7ysmupqr1br-QmQlmedErH9xBnqMQtG5yXFZWDCIjIiFmoWdEzjUL8NmCTEGHKBonsYulTuA5uHtSf4s36cId-uJKRL68gP61eUJIxcAGzD-OD_vQ9h3gqktGZCZ-1IHoU3TKH21beP3QEpb8HTuQcx7vVKBGq2CqNzKzBY4NGu08ZL8ZvIJf95lt5U6O80_PdMcig1t0Cig3tr8fjQZDjQTkKqLGTZHjFNZsNgAEHK707FNWAFD9DIs0ebjGn01-qIRgMvoTGoqIsSOI8_t3LGguCJQwf0ATHZ08Reu6Xa8Y6I2hK7kvXYY8onszCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌ های پرشیانا؛ سیاست باشگاه استقلال در این پنجره نقل و انتقالات جذب بازیکنان جوان ایرانیه تا درصورت وقوع جنگ در وسط فصل اسکواد این تیم خالی نشود. در بین بازیکنان خارجی رستم آشورماتف، جلال ماشاریپوف، مونیر الحدادی، اندونگ و یاسر آسانی در تیم ماندنی…</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/24213" target="_blank">📅 15:41 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24212">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gIp7x_5CBKsCHCFasGX2pTWWt9__IBQRzyf-T8rdUv31LG_UWxilo1s0CjlmtgDExLVkzxVy2izksF1aUZJ7KpS4KVNcjN0zUDPfhQM1r0Di0MIBxv1JWZ9NSfCzAfXInb4LK3vsdDXroEtaoBFhwqcsJWGDKPRNFjeSWN0yrnOkCZI9P-DVupLG46lAiDXyAobwUUpiqXYS5QO38qYOxTDAPrPoUGb8wBv8DuNxLwe5uKAUShN8uFcXMXHawvxfd1tLMP2fsoMyQLjQnCesS9xi4XChpuYPcfkfHeqNcrEvYiPn3Ryfd_DGzeDEbdOjfouGdj5t9U_4U1ouSgOxDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
مسابقه امشب والیبال تیم های ایران و فرانسه به صورت زنده‌ازشبکه‌پرشیانا 3 در یاهست پخش میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/24212" target="_blank">📅 15:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24211">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PXZ1zHrdZKBMLj_7gn8pzpwvqJ0U3y4cIS2lLp7FB1NGrmivYoRUxfu8JiLFCHEyJ_G2_SpDUdq3ZhTj6avHINLn7XMGn4B4Ody-yVGusXEAtQU1-MnOHDOIk3wGOEdidbBeveuMW4cu8GTmdQ76GH0p4KoOPD-H0NwTCaUncwdoWjapQ3e-ps0DaRm6AoivqNTq96Ry4vNvXqcB0cInzpPF3NKM-XhvO9WM_lcIk6ncbwoaDwThfhJgTXhEp5IPMp78KBEn2OgsW-KUK1Aypu6vjuSKMEfkM7LFvA7QPHfenzghbdjGjdc5n7cEyE0sf86i-grs1wf5h9A6KmmHrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیم‌هایی‌که‌تاالان بازیکناشون دوبار بهترین بازیکن زمین انتخاب شدند؛ از ایران رضاییان و علی بیرانوند نفری یک بار جایزه بهترین بازیکن زمین رو گرفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/24211" target="_blank">📅 15:18 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24210">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m6968tVZHPjQ0rWTlHPKgoA-_WMauFsUvzFIRpFUFQb9zkUj0aTFmSVSzNP4-9EWsFm06xGrsmp4U4RQpIbao3Qd-rjKQElWZQ05Fc0EZWk_HtmydeC87lLtO8q1SpgvBvY6lfuft88lM59lEMnk7_pDwMHRhwxWfoOGRTHlMK1LO5ifh817vXyuBJJhhfj6otjDypsxviqzlY2lBND4ycefRUFw9Se_oO9BMEpr-vDHcGOBh6tp_IywZhPv7MxgzLHm0qB42_UPYEWQJARC3XtvZsEvNjBOJOt9CF1DIhXKxhGnOMwCuUUKYlp8fSbLgRBFgPDsCiqtlWQXeXDX-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ تا دقایقی دیگر جلسه بین مدیران باشگاه پرسپولیس و اوسمار ویرا برگزار خواهد شد. تابرای فسخ قرارداد دوطرفه به توافق کامل برسند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/24210" target="_blank">📅 15:06 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24209">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CORM-9LCLNawXgRvntY3c-eys6Kkksr_glEDqRW_vMYpI9pEm5eQJYpFCQiXlmkwe2Eq1HvBbmQFtyJp5wnn3iCKcR-lRAG2LYj2fecGbaNKjgLp58DDKAH8_w5gJTYSSnJsQ_kUr4CxmcuDBDSMA6qjynM5qrRW3xJ_krsbQbdrLeXX8S8VJLyoqQn0rUz-hRRwUlvxeU-iUQ8NWt_58s2Xs32z7PrLKzNGtnJNdR8f5XfRyxF39kSkBUboCDv-4Crh7NRQL_1s-fkPFk18ddSwDzqI0uTnlZpLPDaSYqkdhmnuCajJIYRx66v606FIgcaKcCgOLnW9ejyZ5e7E9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👤
مهدی طارمی کاپیتان‌تیم ایران:
بزرگ‌ ترین شادی صعود به‌ مرحله‌ حذفی جام‌جهانی این‌ست که مردم ایران به هم نزدیک‌تر می‌شوند. اتحاد و همدلی بین مردم داخل و خارج از کشور برای من از هر چیز دیگری مهم‌تر است برای رسیدن به یک هدف.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/24209" target="_blank">📅 14:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24208">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R__wDtcFzQYyybk5BFOY03N6qGgP6i4vvcEgOEfY_MLmaw-qVk25tTlsipyvB7kPTMfdw5hHaASmZVm9gVNyME4ywf-Ek5SVjmj-V_waJbaJp_2BjHpUDZhSnfQx-rLDCpmw6IKpLOgIywb0PE4WfCspxw44vmkNlw7DfmIWmD7rNIOeyZtHYjcAJaqhO07rBPudu73nnfyx8GjgPzSe2z11eZfwb4gjIWJOAjjWBz6zUonolJx74jotirLNFAp90fSgGvgZnNkC4kmFWOaBpwEMBUjvUmtvMujzi_mi2kgkmsYua5iyUi3trlxFC8kKrVf3Dl0GbqSLx71mHQJ37Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
هلدینگ خلیج فارس و باشگاه استقلال برای پرونده بازشدن پنجره نقل و انتقالاتی آبی‌ها روی هم 850 هزار دلار هزینه کرده اند. وکیل ایتالیایی آبی‌ها هم‌امروز ظهر ایمیل جدید به باشگاه فرستاده و گفته شما تموم کارهای‌نقل‌وانتقالاتی‌خودتون روانجام بدید فیفا پنجره نقل‌وانتقالاتی…</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/24208" target="_blank">📅 14:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24206">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a203ff625.mp4?token=CzqsNeMXEtjdT0cpyLgLkuU39raQzFb9-n74G-_h7cIqPvZZqAqW7WsdboTUEVcNSXiw6poHsdaXDZBNw-zhxBzmwkBxPlYTCXE-r23b0p3xjjDsHKn3uiz8w4DZOyupzTSD26eEa5cAHN5d_aEjpr5YvX3gZBKJNBxn8Ug1nDTdOG9TbkRWxrD52laQ--llr8ioS-Mk8p4ZLWssv9ljLzeLtWPUatskTDB6OUfCxXmePkvangyW3_eCOGSm6dGxhnO04GRcJoXSGoIbRpB5O5eoJGkOBHyN-HNa0kJ6yqi43Z4YUJ1yU-gulj0XdUAAd0yZLSf7hq9LdkQvdXpRyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a203ff625.mp4?token=CzqsNeMXEtjdT0cpyLgLkuU39raQzFb9-n74G-_h7cIqPvZZqAqW7WsdboTUEVcNSXiw6poHsdaXDZBNw-zhxBzmwkBxPlYTCXE-r23b0p3xjjDsHKn3uiz8w4DZOyupzTSD26eEa5cAHN5d_aEjpr5YvX3gZBKJNBxn8Ug1nDTdOG9TbkRWxrD52laQ--llr8ioS-Mk8p4ZLWssv9ljLzeLtWPUatskTDB6OUfCxXmePkvangyW3_eCOGSm6dGxhnO04GRcJoXSGoIbRpB5O5eoJGkOBHyN-HNa0kJ6yqi43Z4YUJ1yU-gulj0XdUAAd0yZLSf7hq9LdkQvdXpRyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دخترای‌مکزیکی‌انگار خیلی با پسرای کره‌‌ای حال میکنند؛ هر کدومشون یه پسر کره‌ ای پیدا میکنه یه ماچش میکنه. ببینید چیکار میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/24206" target="_blank">📅 14:16 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24205">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cf62dd03e.mp4?token=eAkocQLpRo9V4-Um2ArZBObHkm8G08PrLVVEd-kn3T8VxGF7LToj8o5Y5l945twuLk0MYA9V_pECWfcyd_acDmK84hF7wtOO3DPsZjvldV68I_DzRUrIRGkAmwBFJU_-Ov18UzuPeb2bs8LovKmq4sroci5eEhi-T2zzhe8PiQSxz-iP98SEeJhHLKVKLacS8CB6QOyfZKFZKMuAwmnVN3HDfql0Yd1j-htQUVN01Sb5tGU20sdXvpre4wyzaI0HKCiM-leLaugVriqmi1nJ_OrVdsoExWwObU4x7tYNyLrKhowYUfCljU_uCvof6eCux7FqZ---Y_AoKDuEljxFbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cf62dd03e.mp4?token=eAkocQLpRo9V4-Um2ArZBObHkm8G08PrLVVEd-kn3T8VxGF7LToj8o5Y5l945twuLk0MYA9V_pECWfcyd_acDmK84hF7wtOO3DPsZjvldV68I_DzRUrIRGkAmwBFJU_-Ov18UzuPeb2bs8LovKmq4sroci5eEhi-T2zzhe8PiQSxz-iP98SEeJhHLKVKLacS8CB6QOyfZKFZKMuAwmnVN3HDfql0Yd1j-htQUVN01Sb5tGU20sdXvpre4wyzaI0HKCiM-leLaugVriqmi1nJ_OrVdsoExWwObU4x7tYNyLrKhowYUfCljU_uCvof6eCux7FqZ---Y_AoKDuEljxFbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/24205" target="_blank">📅 13:48 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24204">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T3s5UpBkqE3e6AKCqtqNRsSgpGbKlc4XUtfCRNyx5Hs1SOTbH6tPk7S8Z8s47DhGrx6nlPvGqt-kvPFN47Ey4u1gpWbt2EMYk8AtH9GQvBJd9CSWeiGuWNG3vsWRkzE8b9Uk0RR0_9PHL6ArV5GYS0WfgKhe9VBgaKgSbkoyH7NbonZz8H_BAam0BsJJjptCRuFOuqI3sJJSFM2baBOXu6B4GtBQpf05_khN9hMp_lnWW1GYnWL747l0tJWC_DSbrSfmWnkUV5B4WHO93ZginiQ87LjhXbiv5PrZCZn2-1HDXOU_xdr_v7t8L0Bqf1BfPj2Kfjd7BggadDBuX3zNcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
پس از پیروزی پرگل 5 بر صفر شب گذشته پرتغال مقابل ازبکستان در جام جهانی 2026؛ پست اینستاگرامی رونالدو بعد از گل اول او  به ازبکستان تنها در هشت دقیقه دو میلیون لایک گرفت.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/24204" target="_blank">📅 13:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24203">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kdsiduu2iuxWwUURxup331IBHhCzaV7mTm_23Uqlub7xdA--WegJJAlDoOa93MmOOZq2eIjVED434yYwcP5wu_d2tfHfG9qjEyuufB6w84tEEAQg6BoIlL-1UscJ4s-SOsjTlYgQihh_pJxegcyqnjiT5dcDPKUTKZxXjDbEsfANKX1isHZY6dNG05yWxANWwZUCQEYNcn0V1EcT-Iqp_1wmonPsIZz8t_dHvSuiyqWs8f-NBTDNm0eUVpW7sxVC4oYkRmcqjUxCGwDxth75Jhb7Cx6S9742VN2FbrUnXgDEvrXJ-fn9gnae4VqffKm9JlgGF3dJowVpm4muyTBZpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
موتورگلزنی فوق‌ستاره پرتغالی فوتبال جهان روشن شد؛ گل‌دیدنیCR7 در 40 سالگی به ازبکستان درجام‌جهانی؛ رونالدو به‌اولین بازیکن تاریخ تبدیل شد که در شش جام جهانی پیاپی موفق به گلزنی میشود. این نهمین گل CR7 در تاریخ جام جهانی فوتبال بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/24203" target="_blank">📅 13:06 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24202">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d68XSwj2dEg5Qj_9LEaNQrulfwu8QGHw2YbwmwuUoA5SZ3kP3r_Msbo0WHRzO6exLvZu_UnJEah7ZBPm5_H1D-SNnt0dnBzq35xq_gxILyg1-m3t9V6BZiDK9tFdKp4_VRY-PC2znxPUYiSiR2Z1oElNYL570wtA_H7msEwin4Oyomr0dvjbcdHlXNVNwn7zmYO1y81xesWaIWWUy5huOhnzQ0gabdcpRwd14iEVuM3amvpI2sBt_pAK4ycInyZXhf1uSUgwrJNTYJeOlbkZN6gjgCKl78U6hId_TYsS5QYVDmekb2qs69MblVCDeSdbt8SZFXwbLiA6tnAow7jUPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
پردرآمدترین سرمربیان حاضر در رقابت‌های جام جهانی 2026؛ سرمربی‌ایتالیایی سابق رئال در صدر.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24202" target="_blank">📅 12:47 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24200">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TqPdWn4hpf_5LdKF-gXjujmf_85hgNocjQHThDfwJW1y4Fc9xWVS4RevzZodrR2bvvxhRiEAwu21lGt0ByRtbrvLSVg_PDSQDyG-m7_3-dRFe22Dy_1N-9kOV9vJN406haqLeIk7W6WFOuprWq7x8VGntfUYnIXHYW7KUBwDKwjIzYhKUMIyM2_RsxGIZS0yZWpuhZdRj9IcNycvnUByPAww0OhoB3H7JvXsFpY5eZceTs3jPWNoH_FB0H1Sr_dEueNKgsBN08vg3Dp4VO4iDQ0VCAn7QnoWjUwJMyrPolwUx_G1gz0XGgWyMZpoE1ctvn_yVQAb84wODmMNvdZjxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d824e9cab0.mp4?token=rUQ5SOTDwP2QHDewqJzZiPkVBcF4jsZw4X85wHyQ2DE7uF3omZwPR8sI7dblNjtKJ-g4jRAvVT4It2GdLvrWFR3xRxS7OoBo8hzhKOXR0Uw5ngzOesdnQVe1u5nooifhXHSC652Ftc-93n9a6xu68TD0zlQPlnBRzzl_ml_Bsut6gQiVOS8ABMDU8ZexWQDq-rFBdFq0f3_QOYNwWiadM_xNZEp_bfLwN0wrEmmTAQ0r5k7zFxtRFO84OvBqS27FjK1Drxcx7-MbT-jchOQNOe1q5APOZZ0dSrKpQA-3cnI9ELfYwgbHqDHU0gFXf-JgNn8McJiKgAiSvvUnLC9ADw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d824e9cab0.mp4?token=rUQ5SOTDwP2QHDewqJzZiPkVBcF4jsZw4X85wHyQ2DE7uF3omZwPR8sI7dblNjtKJ-g4jRAvVT4It2GdLvrWFR3xRxS7OoBo8hzhKOXR0Uw5ngzOesdnQVe1u5nooifhXHSC652Ftc-93n9a6xu68TD0zlQPlnBRzzl_ml_Bsut6gQiVOS8ABMDU8ZexWQDq-rFBdFq0f3_QOYNwWiadM_xNZEp_bfLwN0wrEmmTAQ0r5k7zFxtRFO84OvBqS27FjK1Drxcx7-MbT-jchOQNOe1q5APOZZ0dSrKpQA-3cnI9ELfYwgbHqDHU0gFXf-JgNn8McJiKgAiSvvUnLC9ADw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
اگه جدول رقابت‌ها همینجوری بمونه؛ پرتعال
🆚
آرژانتین در یک چهارم نهایی بهم خواهند خورد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/24200" target="_blank">📅 12:24 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24199">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PdgrXUKREem7x5tccdlpipYCXs1mliRrJcU_uq3cspCUQG8FI30QcWvefnC53Su1BO-S5dZp0l3S_n6R9Xg3KG1GfFAUmmm3LzwCugJHQmo9WQtflMDXiThK1F7F5GcLqyXbYss1kIu-8RI7Z3mgJz2RVM4XFh9jeZ1beZYg0FX-NqTNaT_Pmdil2XJyOh7l7A0pn25TKblhTQZgyEYJdRKOZcanYEjOFzyjQmB8ho4YfWxETQ9vMGYOaiCzMtOQbYsmtGWFFHuFoSvu37l64BbUeWXhILdVuA-YMx6-D4LWWTVWoHIxqHqE8EwnhADy03Kuoo-XtpPn2W2lsD7pMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
پردرآمدترین سرمربیان حاضر در رقابت‌های جام جهانی 2026؛ سرمربی‌ایتالیایی سابق رئال در صدر.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/24199" target="_blank">📅 11:58 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24198">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2111536884.mp4?token=Cf5nNVes0hU5MbgvxAjY8VVR2LROimnWmJuQhHSCJc84V27VLSftlIt8rBbbDXztIoj_pMvKM3Qx9NqvMVXHnszZSO6OCOJWYzxmt-7lCekj27RNeMrlZZvaoAaoZAA7Tw3-IuTuaO8ZhEMgwREdiXM0T5kG2C4DF3QpZuIPdRlxTwHjtHsQKdOztqtgk0m9NfuyFJG1vkx7wRwCnMtXLN4IZuJoJi9nIEJ1R1xcXDei2abzD_GYDJrlo9M47Ug6aJ-4lW8_QCmAxPAz_Skz0Aojjuzq7NnOG8Hdfk8reoOqk0bktXw-lER3W2BTvJUAq6z5VnOFIfkd3g3vpAIu_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2111536884.mp4?token=Cf5nNVes0hU5MbgvxAjY8VVR2LROimnWmJuQhHSCJc84V27VLSftlIt8rBbbDXztIoj_pMvKM3Qx9NqvMVXHnszZSO6OCOJWYzxmt-7lCekj27RNeMrlZZvaoAaoZAA7Tw3-IuTuaO8ZhEMgwREdiXM0T5kG2C4DF3QpZuIPdRlxTwHjtHsQKdOztqtgk0m9NfuyFJG1vkx7wRwCnMtXLN4IZuJoJi9nIEJ1R1xcXDei2abzD_GYDJrlo9M47Ug6aJ-4lW8_QCmAxPAz_Skz0Aojjuzq7NnOG8Hdfk8reoOqk0bktXw-lER3W2BTvJUAq6z5VnOFIfkd3g3vpAIu_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
ابوطالب‌حسینی‌شاهکاره؛
میگه تا بازی بعدی یه 6 7 سانت کم کنیم تا قهرمانی جام‌جهانی میریم.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/24198" target="_blank">📅 11:51 · 03 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/24197" target="_blank">📅 11:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24196">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JvqN9zrXu74eu2CCjbEXjmASikdtkeM14_DAfz1H2KYyS562yQX9kaVs07BQ6Gbp0-8xerntSygZ2c_6rxCdCxQe_PUZT-vNfLT4inORYfw2HawivPL-3amPazE0SyTO5YxWyn_ELSWuzGfCLD9pRDxLCdLvIDzWhiz63rpnPJFNxrejT-AklOKUaok7dNDdSAHlgKN0K9SG1ll0SuzJpGivkuqiliFyzf1ED-flpquvhcfj-8JDimITEsV6RefyZk2NjvD3lc_QBuiXc-4Fhq-kHQsKnE0zP5kAArI4sniNXBpE8j3xJrCh1wXExqN3nWtrN-IjMuJt4F3i2-dPQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لیونل مسی اسطوره‌آرژانتینی فوتبال دنیا و باشگاه بارسلونا امشب 39 ساله شد؛ 1158 مسابقه، 916 گل زده، 414 پاس‌گل، هشت توپ طلا فوتبال جهان، قهرمانی ارزشمند در جام جهانی 2022.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/24196" target="_blank">📅 11:22 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24195">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61cf639d4b.mp4?token=kkJaiGZ5Yuuk9Y-DH2pXTN-K0mgh2yejdkd64j5a47rtKrpWTCYxk9q3nfzy8rO9NR9rpWIVUjbZ-TJUnCDnJwzKBfM7ElPspk3Iy_Nd3rhwW1xM1VDXilFARHgq0u74du24ph87xFnK6rxwOAez0gxpheL1jCBMnXggykVB3Et9cVPYveZBwu-Fq8r2yMAmONmMBvaf2_AAJUGMEMPRQ3xnyPrZ1UAnLEeFZWmWLZIac8xwtmPnTKLX4M_YlbFLdRBceowkU_3WJhZp-A7uqTcG_HrymvBXV-VnrPrQslYgAp30mNPy4JSBj7n555mmhyrJb1FpmbaVuNYyw6XqRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61cf639d4b.mp4?token=kkJaiGZ5Yuuk9Y-DH2pXTN-K0mgh2yejdkd64j5a47rtKrpWTCYxk9q3nfzy8rO9NR9rpWIVUjbZ-TJUnCDnJwzKBfM7ElPspk3Iy_Nd3rhwW1xM1VDXilFARHgq0u74du24ph87xFnK6rxwOAez0gxpheL1jCBMnXggykVB3Et9cVPYveZBwu-Fq8r2yMAmONmMBvaf2_AAJUGMEMPRQ3xnyPrZ1UAnLEeFZWmWLZIac8xwtmPnTKLX4M_YlbFLdRBceowkU_3WJhZp-A7uqTcG_HrymvBXV-VnrPrQslYgAp30mNPy4JSBj7n555mmhyrJb1FpmbaVuNYyw6XqRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
صحبت‌های انگیزشی و زیبای کریس رونالدو اسطوره پرتغالی فوتبال درباره زندگی ورزشی‌اش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/24195" target="_blank">📅 11:12 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24194">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pg7imkDjLJwhNv8Ra_2o5-VUOCg_FBtW-W1MdP_kFpx2G9pDcDiUQ6YexzcAVMRxD9bB_JvU2Q9IPt9m94-WgMI7LnIdveH43nVQh5wZsy4EpKL-mn0RGyJFRQuSxiubcWhepiil0HwHckDDm-emJ7owUnBnaO02pYVja3PGt0b46DLGaomvAHGRJZoJStg6HuARFv90tZCMTKWOE-reaGe9XDHQq56agJ8SKpGGZNBAP8ufxEN2ZvI7jg_Hwu57kQzFRb7Tm9tQLWoKddUnwLGpBNfjOjMk9tFXR0yLu9PF5ZVz4cpWiZ8lDJVvI9B44gY59nbQA8bx2JCCvf2ztg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ تا دقایقی دیگر جلسه نهایی بین مدیریت‌پرسپولیس و اوسمارویرابرزیلی برای جدایی توافقی برگزار خواهد شد. باشگاه با اسکوچیچ تموم کرده و فقط باید اوسمار فسخ کنه سپس از سرمربی جدید سرخپوشان پایتخت رونمایی خواهد شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/24194" target="_blank">📅 10:47 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24193">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f67895d89f.mp4?token=dsTDYNlBMOQO7lVytA_uvBEtn0cheziG-htlrX2jJB4WnZ1H05PniFVxI-Kv_8an6iy15PbxlyrTHIQZvCpLQWyei8xrOTeDgAZnY-JMchLUh1y24QjIER8lRFlsf20aj2Ju59XbLcyxbVbY-Fk2yNjvcvSlFS0e5grDLKXgUzrjWK2QlWfXfa9vM4qp5Bb9nMy8re7YIjTl2f9KBKYQvrzOEnnaN_1kIU8KN2Bp8uyRO4-xZEdRVVfcfHbxz6ZAMpk_7TISzBrDPC1MosV_GHMmg3X3Iy8KnMRgHZy0Lm4-lZTtoY3IkL110E8jv1VNgigXqkn_vqM2nrMhBO59Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f67895d89f.mp4?token=dsTDYNlBMOQO7lVytA_uvBEtn0cheziG-htlrX2jJB4WnZ1H05PniFVxI-Kv_8an6iy15PbxlyrTHIQZvCpLQWyei8xrOTeDgAZnY-JMchLUh1y24QjIER8lRFlsf20aj2Ju59XbLcyxbVbY-Fk2yNjvcvSlFS0e5grDLKXgUzrjWK2QlWfXfa9vM4qp5Bb9nMy8re7YIjTl2f9KBKYQvrzOEnnaN_1kIU8KN2Bp8uyRO4-xZEdRVVfcfHbxz6ZAMpk_7TISzBrDPC1MosV_GHMmg3X3Iy8KnMRgHZy0Lm4-lZTtoY3IkL110E8jv1VNgigXqkn_vqM2nrMhBO59Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بااعلام‌ابوطالب؛
رونالدینیواسطوره‌برزیلی‌فوتبال جهان در سن 46 سالگی به دنیای فوتبال برگشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/24193" target="_blank">📅 10:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24192">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac231ff126.mp4?token=Lvb0Nn1fBEnsx6dDBMYMwtR9hgHiHJkWwGXyanuFYjU8MsLGMrYF-DQ-OZqatOT5lLE5Sw1lnJt7l3gHrnvC9jbqVI_2aixsjFEZXusghgyJ-XTkP-_RXjnFMncP2ndCpkrfgt3Re5ASyiXXrMDZKM2eS9lck01QOIdrT3XkXZlqFcGPU8XVO05mGAz834NnvmuztIiCmfYofBa0PfmVjOvZwJnDrF8Hlr-Vg3UaAtBRU0aI3DD5crXkxyBkTwxH15BxMYXvDPxpW2kXoQVJavLb6LHUDWToRCKVTp9eFpIbUNBmCsFnDPMI8tkAklwfy34043EIf1H0_vbPF1L_qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac231ff126.mp4?token=Lvb0Nn1fBEnsx6dDBMYMwtR9hgHiHJkWwGXyanuFYjU8MsLGMrYF-DQ-OZqatOT5lLE5Sw1lnJt7l3gHrnvC9jbqVI_2aixsjFEZXusghgyJ-XTkP-_RXjnFMncP2ndCpkrfgt3Re5ASyiXXrMDZKM2eS9lck01QOIdrT3XkXZlqFcGPU8XVO05mGAz834NnvmuztIiCmfYofBa0PfmVjOvZwJnDrF8Hlr-Vg3UaAtBRU0aI3DD5crXkxyBkTwxH15BxMYXvDPxpW2kXoQVJavLb6LHUDWToRCKVTp9eFpIbUNBmCsFnDPMI8tkAklwfy34043EIf1H0_vbPF1L_qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤩
سفر پر هیجان لامین یامال ستاره 18 ساله بارسا و اسپانیا خارج از زمین؛ 6 دوست‌دختر تا اینجا
⚪️
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/24192" target="_blank">📅 10:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24191">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W9ayx-KiD7pf-10YC1dt0rICg5lKY1N1jVXhABdKHVkHX3I3JWEb0oud9n2KPmBIDgxW1U-GYIiJ_GV2WPDVyzy49QmrJmV3sIGksazAKFBnfC5mMh_uwTOISK5vdh9pqxVggeqvlvMjCWqQ7jmDTb4-EMtnPNc95sCXAC7OGqkc5fNQXvV3QfkNj9UmD_FC_4It9przVXroOoYWmD0IUx70cbOawiqPP1Vf_djiVTdGGos1-JMMKWIdpJQm2q1yNgs2aZRaiXCJa245gVvkq9r-8Ncg6wh6ph6Qrq-WUKCEC6maBp0z42EOjucmtW4ZTMdJuGfZM9sqDQZS5MYtsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جداول12گانه مرحله گروهی جام جهانی 2026 پس‌از پایان‌هفته‌دوم؛ تاکنون‌صعود تیم های مکزیک، آمریکا، کلمبیا، آرژانتین، فرانسه آلمان قطعی شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/24191" target="_blank">📅 10:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24190">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aD_vsBLOc04AGcjVtguboidzyRI7jHBVirewk-RdDaGAx_2PbhYMCJ8iqdSlEOBVrTnnFCi3bd0NJkq7SjX0xzVrDR9U2vyvYuoOzY1BxKrrMhrkYAn0Xs2F9ZEofZn2eBYSDTFbiYvVrI-TREu9B29XhOxCS2yFVPLpkD-VIAWwW37TF4FefYU4AvEk0Vi3uJkAmEWD7dWDYlax-txAqsQrBDh9uF-fU0vVuEzV6Ie6uAO7GkoOvL6vdlUx8xeAYDrpOI62Dp_AePR-WPIey4waSLFOcsHj3E9h8O4MIKGtch-sM7i8gLTMRqGWiv4w3xwZHvV0oTuuLrr8CcW5Yw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/24190" target="_blank">📅 10:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24188">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XrVXHVFssrXlgCBevU6a3BLSkipIjpZM0wnxGIhzXzpgIBT-ilq468Lffxje6gQkvYRAPQefXC-cISUMxKebpjhSSySyx1-PJoIic187pzq_WW347m2Tb4ThCUvExpu5WTjyO6IQyRfK9qT1fllVKVE2bv7E_uS-dfG1sdnKzKVP3cOnLvw26VX2G-zKwOCSza0jiI2OfOeJIZQtUGOGJnGrb01ZzrtONXRP9FrgrpbxDX8JfHZ2RYOczUDn5qDpg1pd--jI9jyU8MNAH63TS-szfKig28A7rEBDxgPWFx8eTaoHjR_sZ4SiZI2IZawihx0fBL9p2O-NHAYgzf99tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N80TO-G6EHDqCHjs3NHR5kifhs0pPqpWJ-7hO2trW4WiwYzPlBuDOnSeSoblqulRxxTLDSWZAauaJIlJ7JJ7oy3QzOXf7KI0Y92jw_jM87z4ZFv30DcgXr7oRpwYQNiqvyT3_JjHsz4R-a4WZ9sJolcHADRUnKIhvWhZaVasF_d-YX--A0uHDXXKGJjdz5pVeurUhUbfLwzuErheYushu8to539LYbqsTp_-7ks84o3ZZpVZH61veCrMc4FcNzqlSlq1oO2IGh2p7JVed9HHFCN2fDkOBdD9riOwSEWsVpF_THg7tDlrwsaGxRzClG0TMMBUCZy6Xz0q0ma8r6RIeQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
هانده‌ارچل‌بازیگرمعروف‌ترکیه‌ای:
فقط بازی های پرتغال درجام‌جهانی رو دنبال میکنم و برای این تیم و کریس رونالدو آرزوی قهرمانی دارم.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/24188" target="_blank">📅 09:59 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24187">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c00a317fa.mp4?token=W8vyzah4WwrF1G4W_uS3-4oJJjLbjNVed9P789fXHvUorbug60fuoWpmFaWTDsqOWnQK4nbYx6vntUJ8zrld_Er7UurMlNWE1BkHrnvKJmXEVaLd9Uq8O6VVzdEt1r3PeOuSWCoVYN2qZTu_hCrVd7cw7KCmhN_0bOz6_zl8zYDX2amYGqTTWTFrKJy743adcUkCkqXjdIofw8C6RyYM6RCi6nJ9tbfipFWPQd0U3G0JIe1LpUibyjGauNIChy_dgKAi3Sl213q37hirIdBYDXSV--q8pNmqgVgnHWqjx7nUu8DYXo2FpbFWj1advUITowr-ZldnHAX52Hnyv5GDDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c00a317fa.mp4?token=W8vyzah4WwrF1G4W_uS3-4oJJjLbjNVed9P789fXHvUorbug60fuoWpmFaWTDsqOWnQK4nbYx6vntUJ8zrld_Er7UurMlNWE1BkHrnvKJmXEVaLd9Uq8O6VVzdEt1r3PeOuSWCoVYN2qZTu_hCrVd7cw7KCmhN_0bOz6_zl8zYDX2amYGqTTWTFrKJy743adcUkCkqXjdIofw8C6RyYM6RCi6nJ9tbfipFWPQd0U3G0JIe1LpUibyjGauNIChy_dgKAi3Sl213q37hirIdBYDXSV--q8pNmqgVgnHWqjx7nUu8DYXo2FpbFWj1advUITowr-ZldnHAX52Hnyv5GDDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇴
🇳🇴
واکنش‌جالب‌ارلینگ برات هالند به دیدار بعد با تیم ملی فرانسه و امباپه: «فکر می‌کنم فرانسه ما رو شکست میده و احتمالاً قهرمان هم میشه!»
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/24187" target="_blank">📅 09:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24186">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ELhJjyt15GDGXGQsEPJq187O3eYdk9iMQJUCLvC4xNwEsWmvXWnEmMlesyg7bWGcjkv0FNx04zf27P2q-WNWjqPUtyQQshpq7W8hqFLbd8F5haY6YsbHDkKcik_UBBKKTzSqDf3mFl08qtOEpce4eHB5vUUdqNpGnmYe34CXIQ-BwhO3GlxBmqD0XYjPTFyB7LCNbrCBZW-PmnfZgodOhljJlKeczxbBTukJYd2n8fwxjoJLM-2joP4Q69ZggiKa_oLgJsZBW7jOvaUgRe_v4UaxUZgvR8c1lsQCAgRKcWG9eu1i4HqxO-8j_aJXKl1906zTQW07rbvkuOErkqZVZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برگام! کارلوس کی روش درنشست خبری بعد از بازی امشب از نانا کوآکو بونسام جادوگرغنایی تشکر کرده. جادوگره گفته که کارخیلی سختیه ولی تلاش میکنم که غنارو چند مرحله بالاتر ببریم. فعلا با این اسکواد شخمی و در گروهی انگلیس و کرواسین صعود کرد‌
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/24186" target="_blank">📅 09:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24185">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gHE-hjvJkHQ77BwpR6yHRMAhuL3HpeFk2oACmLN7AQZjEXMqbN9dLQPUerUUBA5LGkfFKOYvEWXw8jho2X9QsM-E2v02V9c83wRpEs97zj9Gc4AOdnXC9hX5vhd8nupx9EcrO1kE6GuZW4Ii45cqHVZx_14hAbwDp2s1w2txvPmU27L9ZLePRHpDKzK4I6aGNOA-2HQjhY6QyhhWHH9UH-UKm--zS5Sm7kQdk7jNkGEq3ITn_MEhIurg0Yc41uxAEk_H767zTLvRYEZ_gTBWTL1gPDUwpkyaYyozfK310owQRg2VJN2Lxk0wgdCmLPFoTxt-1Qkvv_lWe7Nh-odR5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه‌دو دیدار بامداد امروز جام جهانی؛ دومین پیروزی کلمبیا و صعود به مرحله حذفی؛ اولین پیروزی کروات‌ها در جام جهانی و امید به صعود بمرحله‌حذفی درگام آخر مرحله گروهی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/24185" target="_blank">📅 09:11 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24183">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oGBv0MxyZdclk6hVtVElMAQVsjOIHGwcY4CZm612V0fa9gA_XdRG2zzy3otxAHXuCd88WcSbdv4zEoSw56kqpwPfefoz-OfPC_nYFZE_XUS1iCfvxxGKtythQd3c1uLFYwMeTu1-REml94wlz7p-76CPDTMuh1ierecUqPf0a97w3-SkLV9u4Ij-tlaFGB5zRF_jTGDfQJBWiN6AByNSzqQ_ck83oZP_H2DWmKYx3eK3AX9lQuYnlmf6cqL_VE8A1GaZ5sFUebECLgzywuQrTzXkAq6pryXZf5bh2JbNX5fmbEAwXRIFFaCppCWYU9YjB93kfJsl5ZhsK94RHQVE_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sGJZiZNS1iSjbGCNRU8Vr3ME_4kgqcsvmuSps2IdTat6_9AuYT97jeYw5Zw8Hhxe_1NI45q5EQ8Z94SxaFiliTBQqler8LT2Ve-OxBN0xTGhZ86BG3jnQcUcR-qvO4aGI-FXpdA223CV9Yvw_juPaFPkkXUiPiQBfBuH8BDgvuIRdOxg3nB4VBDn8F1-Re2BtzKMK8WcFlK6Yo7bAUk28kAdjpzK2whQnxvVeLpBUxXupgXa63IDZnGJfPOvSO388BfPeCR5imd2EbZme4pcPFRu_7PmUzDaCy_YgYk7piimnPEOrvBw_GwdWsb8P8IfYc1g19rvVa9ps6cS0i3WWg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛ آغاز تقابل‌های جذاب و حساس هفته‌پایانی‌دورگروهی جام جهانی 2026
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/24183" target="_blank">📅 09:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24181">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kMwRRxEdvT7u0wbEbWqIPTKXdj3sN-GZixu4oTUgpbw5qIrXPUJ0S08L0hyqIzTY7xx87xt-hhz1eJa1tbWjvGytvAr3eA5yv2KyK3Hlcg_FuOHTcMRz-fFMG57xpbNYrNfKbAQTD3xCT6ynJ9knZeNy7cqJM2tZeJuKOjGt2BtAxSMr7FP15uruFRoe1jhhywWFxwrMwEF-A8emWHSSgznHzlq3PVJntIJNpfMcOXFlXiCKxRBeY3uCiCKfd9LRL2gJa7jMx35U4UrADvr5INdK7-6yCDlJvmWM3OLT41YAmIr8srut2gutArBjOqdLcrEVlcQagMToL9SNJn0UDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جادوگر تیم‌ملی‌غنا: گفته بودم که اجازه نمیدم امشب هری‌کین موثرمواقعگشود. همین تیم انگلیس دوره قبلی‌شش تا به‌تیم ایرانِ کی روش زده بود اما امشب حتی نتونستن به بار دروازه مارو باز کنند. به کی روش بابت صعود تیمش تبریک میگم. هدف غنا حضور در جمع هشت تیم برتر…</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/24181" target="_blank">📅 02:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24180">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IWqhQ2GrQJ7pZ4EZXZP4FdRNkQ1iV6ssjGk7yux6QyGjY20TFDCol2kYFrxJXuMzOpHybSNO_11BIsZ2n5B28oemUzSZ2KalFUDvLD0HwsgsM7Gg89fTn6XsXTe4u376CkWY9vkfoctYUpGx1eaodKLOHAOpvSREbsx9bOKHXe8R1ndkXYIZugFPxVTXGYU023u4gnV0jHZUQUhcGeun_vGHw83BOI2DhoxuIMx7Lgqgpmo2qk6IL1tG32B7Trig05EXUKvvl68aunZlUrg5YG3Bs7n20wqcXGsGzDrK1OQ7OW1kqjFfWX31ySGn6WqBxuBF6K5RlUJMUcxPRCyceQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛
آغاز تقابل‌های جذاب و حساس هفته‌پایانی‌دورگروهی جام جهانی 2026
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/24180" target="_blank">📅 02:21 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24179">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lVlbsVogeaUvAomcNeBWGv_jvoI2syXL_bcDXSy6IWXEHU25rE7TJjKzZ1oEhiOQMjFYIxmQxWv41SB9ZSIw1BeMLy-Oxe0m8vKqKYlPKdcRQXcqfxUJiCz71sjTJZKdJRa8QBPc8UtgWR4vYlYJrpC7-0zyNlTw0AAINWRYGLzJ2YUoBkgm3zA6JLNEvIulpqOYM3ktZ988Jang06hLuctnhiW99ozvzgCxXw2LRHDfzhP-ESQ-QL-4LbQGTUOWB9M-XxwUSrprFAmhg2JZRE9phdiwRqO30mMnMMglBIHfz42fyfDvL9XOexEDliTnz7VHiSCDflbHqosy0BzHlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌‌‌دیروز؛
از بردبی‌دردسریاران امباپه تاآتش‌بازی پرتغالی‌ها با دبل رونالدو و توقف انگلیس.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/24179" target="_blank">📅 02:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24178">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc844d2c9c.mp4?token=Md1Cjim9qd_Cvtwaauh619nrEgvXzmJPYId4qCFNtBOkjpHdDgdlV1aTNpeeBd7P76Y7lZfvdwknjqwYUDfOnIFaXw9wR7VtI_xz9K2va4UyINjM0LUu73itkH5fr-gOR5zVlYTcVQ9VSkEyXy_0eHoAiZpCetPAOiil9_QSL2mRp1KfWXgDsSlwHCq9-EVs-cUrk4lJ9KjzAiwIc09XbJ-Tju84_uaqa-Ag0UyHSmFiQKJenBGbZxjtwjnG2WEGjQZDEaqlgu1TEFKRsoEn3OV4e1jzHXf_Aph877lgj1l-h4hnuOlzcji9NEYchR70CpGeIJGMkcGJngaP3Hc65g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc844d2c9c.mp4?token=Md1Cjim9qd_Cvtwaauh619nrEgvXzmJPYId4qCFNtBOkjpHdDgdlV1aTNpeeBd7P76Y7lZfvdwknjqwYUDfOnIFaXw9wR7VtI_xz9K2va4UyINjM0LUu73itkH5fr-gOR5zVlYTcVQ9VSkEyXy_0eHoAiZpCetPAOiil9_QSL2mRp1KfWXgDsSlwHCq9-EVs-cUrk4lJ9KjzAiwIc09XbJ-Tju84_uaqa-Ag0UyHSmFiQKJenBGbZxjtwjnG2WEGjQZDEaqlgu1TEFKRsoEn3OV4e1jzHXf_Aph877lgj1l-h4hnuOlzcji9NEYchR70CpGeIJGMkcGJngaP3Hc65g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عکس رو باز کنید ببینید هری کین که سه فصله داره چشم‌بسته‌برای بایرن و انگلیس پشت سر هم گل میزنه چی رو خراب کرد. تازه سه چهارتا هم زد یا گلر میگرفت یا مدافعان از روی خط برمیگردوندند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24178" target="_blank">📅 01:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24177">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aSZjSlhXhMwmT0j5LxvJCtS2PcCTI1A4qooSsc1N54kHDzHOF6YNEhsMwFZ0nlPyOoVPnqJwAM8oh579t-7XaTX2858V0rC1anVZoGX7ZcKTs_RwuHNROb1E_sNYmGy7e7BOc7XRRN7SSvrdJWkXytAAjATuj8m540rJu1gCryrYRWtzKHYmmu1LP3GbyAvzQ39VFYxho0frkZoZFJhe8rJut88_vPFGzgNs4OF2_B4I80znRHLuQgweaSIq-9sgpNqpxuSNFnOOeis97OIQJSfln9nVhlZOCF5UqYySfcGO9zR1nfzHabr2POfuB0Uy7tG5fZOSwpY8ChcH1b0onw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/24177" target="_blank">📅 01:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24176">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hf0aK-7jsPpVp8gsQdiE5ZcJkt4lMbqtyH1ZQ3TtIq8Ex7QDppwdSH6M0g-vb-h61xP5KjSGX4TzXTcOOWeoIsXIK6LM2zVgeO4KIjYvhCV71PAMyDIXGczz7xcynwLZvP2QVE3ayuYC55agJL8-aZxo_Ql2v93jLz2eumXaeabKhj9pv4S4Fa3woWc9If1Uh6xMzLxJgIwl3IMT3GRCBdcQ4CnDb6xNN8fbK3KkxR_qrAwRdshj76dwRMby-baWUaJ8NLSXrebC_QXjU2LC0mGNrKiBAHIIJ3OiFPxkyqf7qQFBtE0dUi_LFvO8AtRnor07Cux-1POk8ZH01c60BQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/24176" target="_blank">📅 01:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24175">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d277b50bd3.mp4?token=RG9pbyoECWmSUhhVq29knguPhSoK6Qr6TRR9Xx2Vt9IXX18LD1E0zu4I5cYmdw5H7dY5NH_X7h6UYiICpw3XrXqoFxC6Eg5-oQYiRS7HeTLATsISjxcRsgFrPDNSsLjNFgEf9j7ISBo9DMB8JrlUwiFW_EUCxMuP9DMzNIfcg8i6CrT_mtmbcclS59Aced-R8sUlGE0P_OUSW8G-d8qzZR_mSxXrsB1Z6q_k0MIo9zxioOvXrUJblw_kFgVS7vbg4XkzcPpFOm7SfbvslPP3v6y-O0RPGKsXf9i6Kde2HLV9JsTiNUPj0lWnYyg0p-Kn5Q679MiDweG13uqtAjjVgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d277b50bd3.mp4?token=RG9pbyoECWmSUhhVq29knguPhSoK6Qr6TRR9Xx2Vt9IXX18LD1E0zu4I5cYmdw5H7dY5NH_X7h6UYiICpw3XrXqoFxC6Eg5-oQYiRS7HeTLATsISjxcRsgFrPDNSsLjNFgEf9j7ISBo9DMB8JrlUwiFW_EUCxMuP9DMzNIfcg8i6CrT_mtmbcclS59Aced-R8sUlGE0P_OUSW8G-d8qzZR_mSxXrsB1Z6q_k0MIo9zxioOvXrUJblw_kFgVS7vbg4XkzcPpFOm7SfbvslPP3v6y-O0RPGKsXf9i6Kde2HLV9JsTiNUPj0lWnYyg0p-Kn5Q679MiDweG13uqtAjjVgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚽️
#تکمیلی؛ یه جادوگر غنایی که در بازی هفته اول جام جهانی غنا مقابل‌پاناما یه‌همچین حرکاتی در ورزشگاه‌انجام‌دادوغنا دردقیقه 90+5 گل‌برتری رو به پاناما زد گفته‌برای‌امشب هری کین رو طلسم که نتونه موثر بازی‌کنه. این جادوگر سال 2014 هم مدعی شد که با طلسم های…</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/24175" target="_blank">📅 01:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24174">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UHjSXgdJwWtioq1gqArgXFrM6v_kstGs-jywgOQlx-3PStXNxPrRO2SfoP5pDnK7CGjSQbyBSWSWu3pHekX0dF3ySXkvrE0XfIkWuagbp8lVRIznVDeGvSM2eLOqscMkvCPbgCO37TwVdD8cgyj2hTyttJPH9KWbtpTFXBfcccr0MTKBgj673XM9gxshH_dFKIcJgleJ7WqDawTkpfsWYBowkPB_1Vp6uPb7BKAjVEM_7rtJQ3rgKBNcPD4Fqmla-4FPigJnAhRmlDAqXCfInnz7WNfGtGyQr4DrL89y6i5eE3BSAcYNNH62zVDsYQRjHth3CTVTUx2Qf3OpXHAx8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو کاپیتان‌تیم‌ملی‌پرتغال بعد از دبل برابر ازبکستان: یجوری رفتار می‌کردن که انگار من دیگه ازفوتبال خداحافظی‌کردم و تموم شدم! اما من تحمل کردم، مثل همیشه؛ چون من بیش تر از هر چیزی به کار و تلاش اعتقاد دارم. سخت بود واقعا، باید بهش اعتراف کنم،…</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/24174" target="_blank">📅 01:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24171">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0d760ac60.mp4?token=bzUuL2yelJPPP6_T4gqKnERxY1w2tgk2Yz3XJKlRawWbSXYGY9t1IMD0zrKCahzOCP1g5UpKyHdn1Zt-zilFDMHghNUEyRu0xq9hAO57VppYOspppnv0CJbH750jQoZq37z5xQjkI8ZEU5yxRzmgmqHX8dohirNda2HU7SntEF50fD2YBQya1mDYYjkgJ2XGrNBMiozL0fuo4zs4TUuFzURS92anRnH1jC2YOkuQPPrMFzvEO62a3Ym1Tv2rxg6wwHuP9ukkssIui05CpUsJy8wMTGSacgMDDSaIZVK1Zln47bug2sVrGmjrv_vOTtItcMd6W3R8_qlh0VpCEmc2Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0d760ac60.mp4?token=bzUuL2yelJPPP6_T4gqKnERxY1w2tgk2Yz3XJKlRawWbSXYGY9t1IMD0zrKCahzOCP1g5UpKyHdn1Zt-zilFDMHghNUEyRu0xq9hAO57VppYOspppnv0CJbH750jQoZq37z5xQjkI8ZEU5yxRzmgmqHX8dohirNda2HU7SntEF50fD2YBQya1mDYYjkgJ2XGrNBMiozL0fuo4zs4TUuFzURS92anRnH1jC2YOkuQPPrMFzvEO62a3Ym1Tv2rxg6wwHuP9ukkssIui05CpUsJy8wMTGSacgMDDSaIZVK1Zln47bug2sVrGmjrv_vOTtItcMd6W3R8_qlh0VpCEmc2Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
عملکردخیره‌کننده‌ لئو مسی درسن 38 سالگی: 50 بازی، 50 گل‌زده، 30 پاس‌گل؛ همچین لئو مسی درکل‌دوران حرفه‌ای خود 916 گل زده و 414 پاس گل‌نیز به‌ثبت‌رسانده. یه پاس گل تو جام جهانی بده عنوان بهترین پاس گل‌تاریخ‌جام‌جهانی هم میگیره.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/24171" target="_blank">📅 00:41 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24170">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hi9oNjV2LeMNVJnQV4OhADdd-HMGAYjud6AB14uu3fp2DASmMQdW-10V2Ocg1zNWToDVIfeklUemN4ECGhYiNEDT2lDfu_N__ca7mFtruyJTNiYdhpmaZLnCQYs47iUqCUEhoVp1m5107MTBFH577oIPrY2j-b_7Qaws_2zI0Sv4RyKHsuvKOAE8Jwchp73U_NcBnzwFPH-qnnuUF1piqCf60hbpFe2d-CSlrasxpwHzw8BBuvyJ1poCrASUmNvJxAaWt_ToESZeRMO4nFlfn4InO5KTZXb2-2dMGx9c-z3-MnoYwyo8va9aF2VR4EJAC1wAABVJxSQovMGfg-T1Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو کاپیتان‌تیم‌ملی‌پرتغال بعد از دبل برابر ازبکستان: یجوری رفتار می‌کردن که انگار من دیگه ازفوتبال خداحافظی‌کردم و تموم شدم! اما من تحمل کردم، مثل همیشه؛ چون من بیش تر از هر چیزی به کار و تلاش اعتقاد دارم. سخت بود واقعا، باید بهش اعتراف کنم،…</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/24170" target="_blank">📅 00:22 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24169">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59b8e3fdc2.mp4?token=dPNFPZUeSyqrjuute-2Xj16dGP-ZQo2KSLEiC9kGqz82QJqJD0q_eTGpo2be39g3EAVwtwTZuBJGaeT17banzWNS0SHOR_nyzX8mN8Bo6yNhxUO8FvhtEoIjNkg00nUMPNApojzhyuMAld4Tjq4vIiOcCUlYup83pwa6QNPU4FPadrypYpZSqA7UkNGyGVutNHAQo3ahsC7-e38gUOlKxkGlLwuuU4ZnXd77tul8-jqDOUtYRE3qTNpPEa60CIUPUX1B-afBq2cCEwOZO9IQYZn7D-YKg7wajup_6SUmYkrukiSeTGeONO5MHXwPdv75QyucV09CcwY_7Bnu266SvzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59b8e3fdc2.mp4?token=dPNFPZUeSyqrjuute-2Xj16dGP-ZQo2KSLEiC9kGqz82QJqJD0q_eTGpo2be39g3EAVwtwTZuBJGaeT17banzWNS0SHOR_nyzX8mN8Bo6yNhxUO8FvhtEoIjNkg00nUMPNApojzhyuMAld4Tjq4vIiOcCUlYup83pwa6QNPU4FPadrypYpZSqA7UkNGyGVutNHAQo3ahsC7-e38gUOlKxkGlLwuuU4ZnXd77tul8-jqDOUtYRE3qTNpPEa60CIUPUX1B-afBq2cCEwOZO9IQYZn7D-YKg7wajup_6SUmYkrukiSeTGeONO5MHXwPdv75QyucV09CcwY_7Bnu266SvzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو کاپیتان‌تیم‌ملی‌پرتغال بعد از دبل برابر ازبکستان:
یجوری رفتار می‌کردن که انگار من دیگه ازفوتبال خداحافظی‌کردم و تموم شدم! اما من تحمل کردم، مثل همیشه؛ چون من بیش تر از هر چیزی به کار و تلاش اعتقاد دارم. سخت بود واقعا، باید بهش اعتراف کنم، اما خب. مادوباره برگشتیم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/24169" target="_blank">📅 00:12 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24168">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VARioHwQa4EcXkWMRycfTPTIrgF4Q7kkxzufQfuRRYAiW01duuGJb6HpEoCAH3zPWP-Fbsp9GhGjx8z0SlWNRFVqQZTKHXQXhXQAYUQYtUkAgaBAuyMMWlCRW6NDo_FSYvVRkH1eK_E-ykwDP5PCqLCbDerLLJhrRB0WnGMGP1G30QDmHC7P-M7Y7ZX9vJ-iVYC4MYM631-nmYiRjGoz91v-2EBefokvLjNMFFMJNsuLiNTgsUl0Y6GJmwu7pLMPDnRG2Wu3blpUyrJHhYquKsKktf4mkvSv-3PHbuujpJZ-T4GaNDSW4svGaiFGlCNQxX6Bnr62R2FcOBaaqWUgbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
رونالدو بادبل‌دربازی‌امشب‌وکسب‌نمره9.1 درسن 41 سالگی بعنوان بهترین بازیکن زمین انتخاب شد. رونالدو در پایان بازی گفت من برگشتم به بازی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/24168" target="_blank">📅 23:55 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24167">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/APKU_DvloeyLlaFnGcDtE3-YppqQG7VFKpIsCTP6hKVPfxKqBYBk3yZNdsEhcg2jKThslhx5b20NNXm3iLE0Phv4jxUCewo9cBFCtzzBb0Y2lwmF7bTXox9_onk2PCOrGKG-xrRCBt4GDtt2RSKup8hkfd9t2asv2MeZgeweDnuEYtlybzNj6WYZSUdBkR9UtL8P4s28FsF6Xh9GBUzl-xniisH0pqoXXHCIwhep9Cpa4BC9T6mEM_I5i2DiHgG1y1goM7FoLEuYfPihN6PpQEpd52rC-Dr9PdVML8uPHFRbYbjAw9mIRH0bIgKGlaUg3-PyVY4vKfjfnFf4N8rW9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
چندساعت‌پیش‌مادر دیدیه‌دشان سرمربی فرانسه فوت شده و این‌سرمربی‌برای‌مراسم خاکسپاری قراره به‌ فرانسه برگرده و در بازی روز جمعه مقابل نروژ در هفته سوم روی نیمکت خروس ها نیست.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/24167" target="_blank">📅 23:41 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24165">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e38cb7e207.mp4?token=pDmjOZIU5MR6gDaq24xmOA1tX1znTo4Pi2-cQOWI997iqswYeCupSqlC-ylZnif56SSqo6WqkFDzsr9G-arasCVgTxHuEiMXYnsyP-PAWCyQTD10iTwHPcVhlqSspl-P9Wl2v3AcSUZUvQY8Qw9epEw3lU82tnfQ9eR70gUGEl1AsuGdkc_mUaQEZ3wrbwP24wOYur2Cfxp1l02BqFbn2H3-HNw5ar0APDTKt3Wle4PnB80rhfJ9xxdAOYplkBl0drHEB28BDBNzIehS8bQk6X6PdIdMpAeeMS_lpqThId91-mfH_suMu5GPQqqQcZlQOWjKs8enKaY6U4JaftCZFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e38cb7e207.mp4?token=pDmjOZIU5MR6gDaq24xmOA1tX1znTo4Pi2-cQOWI997iqswYeCupSqlC-ylZnif56SSqo6WqkFDzsr9G-arasCVgTxHuEiMXYnsyP-PAWCyQTD10iTwHPcVhlqSspl-P9Wl2v3AcSUZUvQY8Qw9epEw3lU82tnfQ9eR70gUGEl1AsuGdkc_mUaQEZ3wrbwP24wOYur2Cfxp1l02BqFbn2H3-HNw5ar0APDTKt3Wle4PnB80rhfJ9xxdAOYplkBl0drHEB28BDBNzIehS8bQk6X6PdIdMpAeeMS_lpqThId91-mfH_suMu5GPQqqQcZlQOWjKs8enKaY6U4JaftCZFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هر چی تشویق تا حالا دیدی فراموش کن، دیشب نروژی‌ها به سبک وایکینگ‌ها کل استادیوم رو به وجد آوردن؛ هر کجا هم فرصت بشه تو کوچه و خیابون این تشویق‌شونو انجام میدن
😍
😂
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/24165" target="_blank">📅 23:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24164">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IfAsxDabSS1CK0AkfyL9KE-Ox6JpcL3keyFlejaMhXglQeDxugsAPBJXRi0s4U3MYgryXXabNKHZzaluXXkOKqQYfEZq0W145MS0f7z9lDcKhy0xn9JDXl5lyBha8vFz09uEEIaGC9VYeWZQWOIIS6N5-wTf0xSPvJp9jyszrkYrvFdDqgoqkBXddw3skGCXRsVzqVLdDsuAfTFh3mn4lQ_FKnnd41E3eD9q_VCU0EUaKgeBhYE03U4rrIA2dklWV33kROCaYY43A9CsP3KBh-31Rz6Z_JAXxa6u1a-7M5j7ozixeXp69GBIODxNGbfl2iLwSdGdH2KegYA-eecJMw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/41c27664f5.mp4?token=IXTos8wBvVVzkAi7G10npy7okiRUrjNRYC7_j_7TljOyz8CVy0FLfDWaj14zp_yjWiW6Ig_cDbpUpfIzLj4mGfjG7pEyn5MSv4qZ-p-SqBrI3gWzMNxZOivgLfGw0DAWaJw48H80QI0Bhs0Mw1m8q1FXHBZ7ivID9yPl2T3K5NGMd2XkEIOat_sX9rPimYGTL-1wA4Z0D1MhTT4a-191HnemS7VrfxJsdj6TfhMH8_yqQOmaoKFCEie10mzTYJ7GyzDLJZJ4clSCXSFS-izy-pgoIxV5q7LIZEjZUnFueGGxZFpHPGORBMIxku6I4AloEaBzte_sK__He8lgMuViIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41c27664f5.mp4?token=IXTos8wBvVVzkAi7G10npy7okiRUrjNRYC7_j_7TljOyz8CVy0FLfDWaj14zp_yjWiW6Ig_cDbpUpfIzLj4mGfjG7pEyn5MSv4qZ-p-SqBrI3gWzMNxZOivgLfGw0DAWaJw48H80QI0Bhs0Mw1m8q1FXHBZ7ivID9yPl2T3K5NGMd2XkEIOat_sX9rPimYGTL-1wA4Z0D1MhTT4a-191HnemS7VrfxJsdj6TfhMH8_yqQOmaoKFCEie10mzTYJ7GyzDLJZJ4clSCXSFS-izy-pgoIxV5q7LIZEjZUnFueGGxZFpHPGORBMIxku6I4AloEaBzte_sK__He8lgMuViIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24163" target="_blank">📅 23:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24162">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N3x260ZqA_PHNX8QqLItr39DQ2dNu_82hT9PrsU1nuHph-mBMSdFO2coFYwAEHomUUBkrubZh7ow9bBFeFA7423ITFAFJ7IDTkWLSZLbaRvJvqPR1eJr7fUf4FnTBcQuAoaWEISkbNSvlYwSu8GW_bLeLxiKk6tMbURY3P0NMwYh9MoD_dvXH4e_eMlj7LTM9_zJCyk61vYZUHz9e3Pg3ed30JgSPKyExSelSlm2_5QrRQIxP9C0IVZzg-XvmrprFMdNMlL8sm8fiuz__qOQJs-3Um3ubBHs_dFvyAinGumndpKJxyOYmkZmD2RE6LozmNSg-V0gXA8jwVwLFoj8dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
عملکردخیره‌کننده‌ لئو مسی درسن 38 سالگی: 50 بازی، 50 گل‌زده، 30 پاس‌گل؛ همچین لئو مسی درکل‌دوران حرفه‌ای خود 916 گل زده و 414 پاس گل‌نیز به‌ثبت‌رسانده. یه پاس گل تو جام جهانی بده عنوان بهترین پاس گل‌تاریخ‌جام‌جهانی هم میگیره.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/24162" target="_blank">📅 23:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24161">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VGaWDvAYB3BXAZm0-aA-kSG4QypG8BHEwPLXP9U5fCB-DcukZuze2iC6d6LpMYSPx5_giEXaeVy8V16-R2RRi3T5mftNY9a4YAxNK-gvY3DXNNJyOlmyF7U6g1lFiLmrcAYTL9I-syiliqu00iWr-D5ViBXiTCOymEi0Dahpq2OYtp8y6Gi8k-8GSyTZc_MffXekDN_iP8kmUXniq0Skpzq5_WIO3sdIOM8ChUKLGQbWui5hkOgQethdMsa-agg3Z3BCfzfYpSLWg9up0SzrBLVGLEi-olK_txPAxxB6Ov1r9xikFveB4MgUj8LlqdeZZgoDbtijR2KXB_ofvPO9Kg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24161" target="_blank">📅 23:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24160">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IYxI7GyYXopuqDCVV6Bl6YO3bpy6G7yOyFNf8FphDI-nqMEAgX9t1xn6WypNn8rC592q8_Oxe8ZN_0Pcj7UuWlFuuqkNeF4Fvk9wisidqgnvQtD4LOMaCGInJRGXt99jiuZEegt0o0tQdi0FRKNFdT9A3wjhOk60rhKOOSKhCCxCA6F3LaqExpPuCYp1vnka0E-DjEQm537gzO7OlXsC5JxmC_UCJ98RLXOThJCGzY5KwiNThzNRbB7AQQMpLDf8CjDfOkz0OX6WmuY_rI12MXBjAIlDV0p2F_UFnNRxJxkg2vPBHRacjZ975EFyIjvbdFyI8DhhJJ8Y2oVVCPQnRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇷🇺
👤
#فوری
؛ ادعای رسانه‌های روسیه‌ای:
بعد از درخشش دربازی‌مقابل بلژیک؛ باشگاه زنیت روسیه به دنبال عقدقرارداد دوساله‌با علیرضا بیرانونده و قراره بزودی با مدیر برنامه هاش مذاکراتی داشته باشد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/24160" target="_blank">📅 22:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24159">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nJqjNz-tle-iGBA9aAb1J8Y1GsF7EZxStMdq6bWDhyPK3dQdMc6FEcg-WyY1iSwKa2dfytU3fkrUCX7yrWPyqsBM-yzw1z2-Rc_qpVqhpDrt11Fvc0epLfpJoIkEZVYhMWmHmlLOjpNglHeM0ezEp159ad7xLb0_d_Ha9WGHbhc-o-Sxd6JrfGuRnyd6PGsKwr2KL2P620miUDTF3LY7keip3pDfbeIM_VmlY5WIt5MvofmIYs-FKSfjIsz9amS1jXnLfkAXs4R58q2h2tcU-2Op9PV5qVALSIdSUU7TcLBDsxvDQqsBfitkItN1AYK4s2da-Oj4YhiCOfpUMg-fSw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24159" target="_blank">📅 22:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24158">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iGngEEOxHd26ONeIhobyw-1XreQNJsBroPYnPyI5bjL9R9oSPYdhup7IxDoaq_g9pqxQq0XzJu3UGkbvmZDpAhniJkWP9WE23yC7KQbdR5oA57AxF2w6ThAT0rY9jweKuWUi_TztsQevsHsBn7Pvi0So_6wMqonCp6qoxz1KhjmKzRXkgxypvt1WUuZIx5gs0seauplHcw81f3jNC9_D9ikqTbB5ZZIYgHV0d8fXVJnaZNZbPlj07-K2o0t8rAPAeB7X3AEu8WP1-_muVSs_ZbGJFhW10uX0g3jX8bFd1xu18MpP0mXDB72-TPhPa9w5cvGMZf6hlYa9-3LITKpNWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
🇵🇹
بازیکنان ازبکستان به این شکل گل چهار پرتغال رو به خودشون زدند. رونالدو سمت ژائو نوس رفت با او رو در آغوش گرفت. بزرگی یعنی این.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/24158" target="_blank">📅 22:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24156">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AsIOwzCZOVo5ViywKnD8FGDgD2RO5U1ILUM-ziiZquldZ9d-Sw5qtEH8Ikdu8YcteT-b9v6ho9mbb1nENLXI7KFYoRk9_etaWledVzyeq_c3Zo7YRY6mauhIgym4icHcV3s-f91bGSEMu71Zl6DuVY_NOpoWHKrCl-5X-2jpugoEmvigFOgqa1NiGkr4yvnT5AWcU8ufQ-CX_DHWrBR5SA3cEXlRPYpYz2LlLlvdBi9Z563w6pH693t3sfRZ2GKIMXZlLMu0jhxqCm7M7DxE581xSxxSFgbG9Fgmf_V6RQZDA7nBrGc2fGiw1zH0t_ZQy0TEpx7VUf4IQll1BLpLNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pdXjlP2DsntrYHgnLh25xPnS9fiUUDTTQ4PMbK5mkaufxNV_gn9IFrKWjxvZan0oe5CWMQDLSCFzjA3n_2PBhTSqPX6bcxRGUd4ZbKpPN4uN45ZXDeG8EPOJVbN3VnLWHueGDZb3MbW7Zd7d6vR7fc42HzGCiTIhcbBqjKmkJZ1f-ZC3Fnc2RD-ihnmhbsS5raUxlwLWUUiFOkLj5tzkD3sH682wIYSmRfTq3NTQpXU83JmHp9XL57ZOPUmU5-A-FCSFD99KRlM0bX1X5PMehRGD4EkEqMirX9C98a035g6GRLRnHIYsHNkq6ugiztdB42kSqzzLuomPK8bn3dVhtg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
جادوگر تیم ملی غنا: کار بسیار سختیه اما تمام تلاشم رو بکار خواهم برد که با طلسم هایم غنا رو به جمع هشتم برتر جام جهانی 2026 برسونم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/24156" target="_blank">📅 22:21 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24155">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r5A1AnNn4diTmBZTiHLorA6gtRXKTIJn_DUGf98aM0HS1Cr0_UKMixIiaq-gAzo9MQG3Es_7Qau-ypHZwr3PrO8sbFXMQ6geaF1nTx3Mj2bISMQ-37E9d3MuAdfHB53RaLQLQc7ql7gxa7SQcNkBKbQpP8VktIJ7GaEWWjfZ6bEnrINhFpoGRqEXyLccqVRdlvn0reNRWCPrBuE1BoMH1WNwRxm_YaDhqCkNLwZCvRBfiPFuOXfVWb5Ync5i10sitRosiXuOXIcl_XIL33UFt_D_0c8oY8p5JE-8sZgxCbwkr2Nb-NjHW2J9CzQM-jIbTMwEs2x2Cu-OK-DmacTGug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
🇵🇹
بازیکنان ازبکستان به این شکل گل چهار پرتغال رو به خودشون زدند. رونالدو سمت ژائو نوس رفت با او رو در آغوش گرفت. بزرگی یعنی این.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/24155" target="_blank">📅 22:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24154">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a29fa94bc.mp4?token=s5PFYbg_nXR8P7nBFiN15oDHg178FmxqIuHiL1jLw3MULpaNrY6DwW6ZsiWVYmMxUvT4Zzo6YQxGhsAZaMhHDaLmktqK2xwG2nKjhwSOWNUNLvcmxvYx7HeSUwtQnDSsH9azj1xryre-zcvJK7ROyFqk5H7XNGmLSK2yIjsNLAretyhIr6LFn8nmNQ1ZkIwK_TSReDlduyzPNquyWWWuMlGwPjoFdAjOwxEo98qoRaTKHLSW3g_GIm1XpjFLpzRIvfZkgTickeUO8faYfMe8cDS0fK-wbrsdxX9-E6cGpElH03Wfq03euJaFaOv3EP0p21XrQIy-8NakHzNMiuI51A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a29fa94bc.mp4?token=s5PFYbg_nXR8P7nBFiN15oDHg178FmxqIuHiL1jLw3MULpaNrY6DwW6ZsiWVYmMxUvT4Zzo6YQxGhsAZaMhHDaLmktqK2xwG2nKjhwSOWNUNLvcmxvYx7HeSUwtQnDSsH9azj1xryre-zcvJK7ROyFqk5H7XNGmLSK2yIjsNLAretyhIr6LFn8nmNQ1ZkIwK_TSReDlduyzPNquyWWWuMlGwPjoFdAjOwxEo98qoRaTKHLSW3g_GIm1XpjFLpzRIvfZkgTickeUO8faYfMe8cDS0fK-wbrsdxX9-E6cGpElH03Wfq03euJaFaOv3EP0p21XrQIy-8NakHzNMiuI51A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
#فکت؛ کریس رونالدو به جوان‌ترین و مسن ترین بازیکن تاریخ پرتعال تبدیل‌شد که برای این تیم دررقابت های جام جهانی موفق به گلزنی شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/24154" target="_blank">📅 22:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24152">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rRrbveTFpv2_hQ-3DZUTg5FxHEWU3Q53vg0m7GENHcI3J50-JNc72cN4c7ZXYTNoerAatvEsmL0WDPQQDkzp30ng3sh8pK20mehGoAH6zMRFC4XNMKagGnUaenvp5_qAu1azqbpEZhj9VLfmQ5_kdyplbaKCVkDs8AMxZSrRG3ytOUfJ7Fz3nerTsnL9am28xFN0D6XxPbzhGA2BYK3biQfkudY_d7YqfUG2yfkp2Vvm9sfTYlp4bl9wNIjt6rv28RpV_0rx17oDaOA5nJbjJxx4K5igMF7pjvvmoNs_Oc40ECI_lzHEBlxIIMkVBQ108CAcehpOfTQAtpmuv7K3JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
دبل کریس رونالدو در بازی امشب تیم ملی پرتعال مقابل ازبکستان؛ این‌دهمین‌گل کریس رونالدو درتاریخ‌جام‌جهانی‌بود. یخورده بازیکن بهش کمک کنن قشنگ‌میتونه‌برای‌آقای گلی رقابت‌کنه. این 975 امین گل‌تاریخ کریس رونالدو در کل دوران حرفه‌ایش بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/24152" target="_blank">📅 21:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24151">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df5b6d9df2.mp4?token=eMhECwhL4ElHWXxRwBZfiaSP1_JGrHuv6RtI1-tznC-_-ueemJGl2rgk7aHN7imwwMMqZvkt-zl5fITDj2MvzW_6GEIDK5UeaGUYdb2KC1p9YoRIFGzAvDLO4ewUjwIxtGfvKxD7U1qBRXLDTZv_Pu1Kc9vuTiMGSvXzWQbRKhinwbsn82-rpUBjta_1RmDXovlW-yJDEauKRyPjlvK1085d2XNJY84RtMdWallY26IkJmIeiG7kTaY5Pd7S1JbJ08AJMdPSPA902OqdMfCYmBSTuXH-VvFdPuZ77VfyNtGd3F0fNMUfj0O32byrWONzgbSNMQKpryHc58Ix1E9gyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df5b6d9df2.mp4?token=eMhECwhL4ElHWXxRwBZfiaSP1_JGrHuv6RtI1-tznC-_-ueemJGl2rgk7aHN7imwwMMqZvkt-zl5fITDj2MvzW_6GEIDK5UeaGUYdb2KC1p9YoRIFGzAvDLO4ewUjwIxtGfvKxD7U1qBRXLDTZv_Pu1Kc9vuTiMGSvXzWQbRKhinwbsn82-rpUBjta_1RmDXovlW-yJDEauKRyPjlvK1085d2XNJY84RtMdWallY26IkJmIeiG7kTaY5Pd7S1JbJ08AJMdPSPA902OqdMfCYmBSTuXH-VvFdPuZ77VfyNtGd3F0fNMUfj0O32byrWONzgbSNMQKpryHc58Ix1E9gyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
موتورگلزنی فوق‌ستاره پرتغالی فوتبال جهان روشن شد؛ گل‌دیدنیCR7 در 40 سالگی به ازبکستان درجام‌جهانی؛ رونالدو به‌اولین بازیکن تاریخ تبدیل شد که در شش جام جهانی پیاپی موفق به گلزنی میشود. این نهمین گل CR7 در تاریخ جام جهانی فوتبال بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/24151" target="_blank">📅 21:17 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24150">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c38410752.mp4?token=TTLeghkZ1jEpZp5iVo0kbDYa_VdKKdfkHguDAgPQWHSQhDT0-WOiKmN2DP7zDZZl0j3voK_tXACpl7NKYRezWeYSizY8HCswotgnYpj9h-B7tfhjiLPYzzPv9ZZRIc1FmBJWQzXXIzUWc6si1TJ_m0AfLKw4olLINmqFEjoq4zy3zE3xzUyuj85IvXCgH-2SzZyp-LbkJtp2M83Jp2KtrTmZMImBW0KkwWQ1WNn82rjqmXLMSo0yaWWH4uon5Hxef5ULT2V2E7dzsXZ3geWQqOiIdIeub6Gudoc4wnDAVTClkFsW2JvjVFhMYQ5SwUqkEG25kFaW_7ts16qjSiYEDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c38410752.mp4?token=TTLeghkZ1jEpZp5iVo0kbDYa_VdKKdfkHguDAgPQWHSQhDT0-WOiKmN2DP7zDZZl0j3voK_tXACpl7NKYRezWeYSizY8HCswotgnYpj9h-B7tfhjiLPYzzPv9ZZRIc1FmBJWQzXXIzUWc6si1TJ_m0AfLKw4olLINmqFEjoq4zy3zE3xzUyuj85IvXCgH-2SzZyp-LbkJtp2M83Jp2KtrTmZMImBW0KkwWQ1WNn82rjqmXLMSo0yaWWH4uon5Hxef5ULT2V2E7dzsXZ3geWQqOiIdIeub6Gudoc4wnDAVTClkFsW2JvjVFhMYQ5SwUqkEG25kFaW_7ts16qjSiYEDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
موتورگلزنی فوق‌ستاره پرتغالی فوتبال جهان روشن شد؛ گل‌دیدنیCR7 در 40 سالگی به ازبکستان درجام‌جهانی؛ رونالدو به‌اولین بازیکن تاریخ تبدیل شد که در شش جام جهانی پیاپی موفق به گلزنی میشود. این نهمین گل CR7 در تاریخ جام جهانی فوتبال بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/24150" target="_blank">📅 20:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24148">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ab3271383.mp4?token=SQhOzdqlu2HPQo4g_YleX_iqClkpDtB9k6sw1EUF8wLWDdqY044zFjj2e4Q-e7RVzYQoz94GrN8ecUVEw8juDkdWygAm5mmLQesKf4JaBDZdDKb7UJ9xE6JB7JsCZima7sFoXjPARDhhor_fuPv6uXEL6cL7XhqYrp3iUDBmvDEAzPHTk1QRbFXKjjgj6dH70MLUkBSSaYW-vl7Y17YKM8-JRLnNTIpp8n5qRgove1sMK3NdZmtAi5sO5e-nhFUc5fmZizvo0mmGGNAOLisiTNjHNT8gPqvx2ghgvNx0RJ7YatedKUtBIdB_i1uymt8bo1b7-QnkXViw_MlM2S5fSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ab3271383.mp4?token=SQhOzdqlu2HPQo4g_YleX_iqClkpDtB9k6sw1EUF8wLWDdqY044zFjj2e4Q-e7RVzYQoz94GrN8ecUVEw8juDkdWygAm5mmLQesKf4JaBDZdDKb7UJ9xE6JB7JsCZima7sFoXjPARDhhor_fuPv6uXEL6cL7XhqYrp3iUDBmvDEAzPHTk1QRbFXKjjgj6dH70MLUkBSSaYW-vl7Y17YKM8-JRLnNTIpp8n5qRgove1sMK3NdZmtAi5sO5e-nhFUc5fmZizvo0mmGGNAOLisiTNjHNT8gPqvx2ghgvNx0RJ7YatedKUtBIdB_i1uymt8bo1b7-QnkXViw_MlM2S5fSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FoPdWPLOz6N1GStmuK84rXVP-_ywnvrQiM6Rz7YpRfuioZAlJNUuRfeXNBPsQMekYcpuBbxt4rfZ-6mp9lyTmMEv8HH7Vk9TsZZluJ98wFqtPEivoR4k06ArlTFMVMfNxKw4OVveyS66BfZ-dKp8nfV3Y0SQUFkcWurLrZ4GH-CuM5DdIFlhLgcm0Ki_1JG1_j3fMlwd7Rj0SpRqMWT7VirxhplKTVus4f7TDsBTLr5rP8YZbzmq5v6hs6sqWl96MP4HUjVK-k4OUcltQhU0Svdz6pTX0AGIMniFRQMNAaYFFBjhmKOfflJh1n6PxTHtE5ileEk_tkJZKgN7YPqVjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛خواستیم‌بعدِ بازی امشب ایران با بلژیک جزئیات‌مذاکرات‌روبگیم اما رسانه‌های دولتی نزدیک به پیمان حدادی جزئیاتش رو منتشر کردند.
‼️
دراگان‌اسکوچیچ درمذاکرات‌امروزخود با باشگاه پرسپولیس دوشرط‌سخت گذاشته است که یخورده مدیران باشگاه رو برای عقد قرارداد…</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/24147" target="_blank">📅 20:35 · 02 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
