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
<img src="https://cdn4.telesco.pe/file/Y_jSktuvsFhV0Kx2gy3l4stVQEtXuc8U1nJmK_n39L0iiCM6OkECDfhbjd8duQfzEutHONwagdvlGRaIVy6Kyb7PZcARhiQuPTUoIgc8ntH3_Sc9xA6f_zhlkZk0ginDi8HgcccLT595iRDylLUbQpuhUh9GNHF_hpNmRK6JOkpryD91GH6-OdgvxXh2iAcg5gSrPOfe-7zoG1Ku70mapjApS84Z6VmjI49rgtvVClX_AUvAYTiVL0GNPwKDI5JZ-8A9lRIgvpJWuigcuOlgZOmL4Hh1JnT9Ue9N-oM0aUq60uH5d6XLlXh8tTYxVa8x0vcnlV1jNutsYPOkaEk6vQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 971K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-16 19:18:04</div>
<hr>

<div class="tg-post" id="msg-125590">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lJJRYiSyfFTB0ROhwsQ1Hk2EJWyQU13MsErg2lTR2p2Cq8kYpQ1u-H31AIJoRdhFv-vAzKYsS_LxKYl375Z_vQpCXMLMrVL6xFqG2_1L5e9heqqWeWAVYNOFWD8wPhtmBG7oynFFcJzhaNCJP3It_3Nq6O-ShA7btis-bo51WwLplLJQUMv5Fw1NI544m3aLSJIgpgXPi_5mBgy2c6SKSrIZGn_RzhiOAzpvVilLS1-zfKIpH-nq_NpXuI8lE990Fid8JKw4LP_Tapg8t5QrBaR9h9K1RsorfJfGkVA4m3SKQ7uejz-y7pNDTOoVxS_wOWeieln67F-4WuajH-MlIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دولت: اینترنت را وصل کردیم
اینترنتی که وصل کردن:
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/alonews/125590" target="_blank">📅 19:18 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125589">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
الحدث: ایران خواستار مذاکرات سه‌ماهه درباره جزئیات پرونده هسته‌ای است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/alonews/125589" target="_blank">📅 19:13 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125588">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dbrPO74WHvEpV6hyDADRwjmrzxu4NQq5Xz6yCzQGYa8hI1D8pUT-x60jT5VtixMO_GQ1xk6bO9I-8n9Z8LDvxYb9gH_Dkio1jUbFBY3xKC9ovrKvQhWL8D2gF03mYvyPdG-qLhP8ZHTXI4aaEEZfVdCbUKMW3bfyT2XqtSbok3FOX6QwU3V0isbdS1CK9qFFdpJOJ7MRDc_U833Lx7HBkAXVC94jR_0Cin03iaHlcsScyPbs7JwcPo-A-aJn4elwCq6mtiFJKDc8Tzt-noJ76VbpmIt3NDEeKSWibV699AVeU05Eh0_bDBvuyxvNWd-hHd-H_wFWbGmIUw5TZmI_YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
انفجار قیمت مواد غذایی در یک سال:
🔴
روغن ۴۳۱ درصد گرون شد؛ مرغ و تخم مرغ ۳۴۲ درصد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/alonews/125588" target="_blank">📅 19:07 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125587">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">✅
با سابقه ۵ سال فعالیت مداوم
🛡
حتی بدون قطعی تو دوران جنگ
🔥
آتیش زدم به مالم به خاطر عیالم
😐
بقیه هنوز VPN حجمی میفروشن اونم با قیمتای نجومی
🚀
ما چی؟
💯
💥
VPN نامحدود واقعی فقط 190 تومن
🏷️
💥
بدون محدودیت حجم  @NetAazaadBot @NetAazaadBot</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/alonews/125587" target="_blank">📅 19:04 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125586">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rBFZshkGRi9wRpRFAC5NLi0BhPKlY2J4pBJp9i_oma8a5bsv19MwtRO_IekhC1TmXlOEBP9JxLE70fhjBPKT8ICost6wkomRGjoFJiP5MyB3tRIdSzgnm-WmCbcODAV6l7XjX1mSrlyQirFdX_jbG5AFhF5cDM7foP4luV4njgs_gD4XoNQ8Uk1SN_U2v65MNqIl5lsYQ0IZXnZ-XIK8cDkP9Y-DjqZpIvsejiz6qmJYiDXNm0YlCAmtud-cEiPTXzWXG9fqzmM-41iCFtwkJG_1rOn5DY15mq0nCobfmXajtPFt0gV9Mmjsus6nnAmlL-G2RRk1Nra417VJGFF-6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با سابقه ۵ سال فعالیت مداوم
🛡
حتی بدون قطعی تو دوران جنگ
🔥
آتیش زدم به مالم به خاطر عیالم
😐
بقیه هنوز VPN حجمی میفروشن
اونم با قیمتای نجومی
🚀
ما چی؟
💯
💥
VPN نامحدود واقعی فقط 190 تومن
🏷️
💥
بدون محدودیت حجم
@NetAazaadBot
@NetAazaadBot</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/alonews/125586" target="_blank">📅 19:04 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125585">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MsepzILsJEsg-2oL1gZOW3tWD7faUmxfaD9CoX_ILSWZRGqJSTgoK0wlsKz89xBDqVmfgS1DtAq4PWR7pSRsa8VsGhqvIDfcTBW80-0UsbTgfl7nI50E7jVgX1P-7Ab9SCYJWFYMI0PAO_3UngChOBNBJR9pmEEQclDR2q-VCrClPrc-33ymZMRer5YUQQFhn5RoZ0BHmwh33RKdF89b6pFwZ7EAVzkK846Yswa3mPRiS7On9Xf-b_pok5PKXDpev0LjnDO48PpCwyI1cFOGFPDWLTzC2i0fMCvEtRuriVh8pdoOk6eVhwZbZdPBswylIez8xjemb-9GrDVsg6o1_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حملات اسرائیل به لبنان ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/alonews/125585" target="_blank">📅 18:57 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125584">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
سخنگوی دولت: اعتبار ۲ میلیون تومانی کارت امید مادر به حساب مادران واریز شد
😍
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/125584" target="_blank">📅 18:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125583">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d72c112b3f.mp4?token=pQc_lxoLmKApgecIZx2c3YKtv4aZ9bgmnnQ8qYaIugDN_CSQuJukUo0DKuQFsgiX5A5bsf35MrvlksvsSM0Uzx4EUezrFtTCPg0nPKEHAld1gFO0x_1T8qMvZcDQRxnOnEYrjtOREPZtjgdaWTowSd8G_7tEq4F8hjHqU2sYJ_5PVNDCF69cTHwe6mrPZbqYObVo66Q7iso89wONgXPXunRp8W9pL8hlveV3z4t5LhwKWRhvotvC9ajVUy0jIEW80qs1e4n2suxfXgWDTsNOfo11HN0F09X8y3tTvUOxDyVZo-ikE5h0h9fwcI5Kxo1xuUfcr3A11zktZJpqrVuIfEPERuQ_Dy-zyC6r2Ll1xIop35pf7xktntImDCughng1DUhCFfpiPodILO0nI0Vv0Wac---gkMs92tOoKusuVV40FiLdTlzDjhtRX8cfG91uI0wFCt1s2HF76IQwAdn8FiZJOvyJUxdhhfBLAbkM_6-gVE1hA9MbaO8aKWVs9I6Pt1ot1eptd8oCHVGF25ErSVk5wGvU_gS4eURH_L7xVPrxXve15oyhH5YnT9Ej6ORGHufSf6PbyZqbeNZyzV40KKruvLGcr5croL4Kks6ctaROIlfRV5BsrvZawfjTBLvnIxmCcYlv4S5aGbXZzhRCIsumQOq9GSU5xP5P9mJ5UPs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d72c112b3f.mp4?token=pQc_lxoLmKApgecIZx2c3YKtv4aZ9bgmnnQ8qYaIugDN_CSQuJukUo0DKuQFsgiX5A5bsf35MrvlksvsSM0Uzx4EUezrFtTCPg0nPKEHAld1gFO0x_1T8qMvZcDQRxnOnEYrjtOREPZtjgdaWTowSd8G_7tEq4F8hjHqU2sYJ_5PVNDCF69cTHwe6mrPZbqYObVo66Q7iso89wONgXPXunRp8W9pL8hlveV3z4t5LhwKWRhvotvC9ajVUy0jIEW80qs1e4n2suxfXgWDTsNOfo11HN0F09X8y3tTvUOxDyVZo-ikE5h0h9fwcI5Kxo1xuUfcr3A11zktZJpqrVuIfEPERuQ_Dy-zyC6r2Ll1xIop35pf7xktntImDCughng1DUhCFfpiPodILO0nI0Vv0Wac---gkMs92tOoKusuVV40FiLdTlzDjhtRX8cfG91uI0wFCt1s2HF76IQwAdn8FiZJOvyJUxdhhfBLAbkM_6-gVE1hA9MbaO8aKWVs9I6Pt1ot1eptd8oCHVGF25ErSVk5wGvU_gS4eURH_L7xVPrxXve15oyhH5YnT9Ej6ORGHufSf6PbyZqbeNZyzV40KKruvLGcr5croL4Kks6ctaROIlfRV5BsrvZawfjTBLvnIxmCcYlv4S5aGbXZzhRCIsumQOq9GSU5xP5P9mJ5UPs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک روحانی:
مذاکرات
کصشره
و آمریکا قصد داره سنگین حمله کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/125583" target="_blank">📅 18:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125582">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X-4cLTon10A3-C889mijt9dXtz5PIgvdMAAbsG-TWyDqERnrZlUWsarG8NV8L0WHthL4r-5Q_8x6VwJ4zj8U62vwr1xiS3FFhUAyb1Cv1la9NPOaH25PEnzvI8wA_GfgUx0q1tJPuA-fFQBJWRcDm2z9rE-q1HPOMqdrqGo68EhX-H_jJll0pBHOWJabQhUgif9gGmojllTt9Yebv4U5hBmQ72Nz7NnmYShIO4-kIDFhLBWfi4gq3wiyvvDISAGAwYDQ5SyTczLM4MsKxhJmoosAfVzuRhqbvBZjWZ9364I-EX_hCOooeiDgUJquhZJ6p02Ln5uGjSNL8je5EgKuEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیکزاد، نایب‌رئیس مجلس: همه آرزو دارند بروند دست رهبری را ببوسند ولی چون ممکن است دشمن در این حین بخواهد اقدامی بکند، نباید این کار را بکنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/125582" target="_blank">📅 18:31 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125581">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
العربیه:
ترامپ به میانجی‌ها اطلاع داد که مذاکرات با ایران بیش از 60 روز ادامه نخواهد داشت که این مهلت در روز های آینده به پایان می‌رسد و ایران باید به‌سرعت پاسخ دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/125581" target="_blank">📅 18:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125580">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
نورالدین الدغیر خبرنگار الجزیره در تهران:
درگیری‌های ایران و آمریکا در خلیج فارس بیانگر وضعیت «نه جنگ و نه صلح» است که تهران و واشنگتن در آن قرار دارند.
🔴
طرفین آمریکایی و ایرانی در حال مذاکره برای یافتن راه‌حلی جهت پایان دادن به جنگ بین خود هستند، اما آیا می‌توان گفت که این وضعیت به همین منوال ادامه خواهد داشت؟ قطعاً خیر.
🔴
هرگونه نقص یا اختلال در مذاکرات می‌تواند این درگیری‌ها را به جنگی تمام‌عیار بین تهران و ایالات متحده تبدیل کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/alonews/125580" target="_blank">📅 18:07 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125579">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TPaSVAKEJJPVhX3GqaxakYxemrzQ7aCs8U9BilDPcummMa77Lq4s8H65FhTTuiq09Om02yrthdCS1Fb8eN_DRTiy-RtxO82-wAFA9gbQzm7B1OBqfXt9o-dJoqDb63ys2C___NYhu83KbUcLlhdR66icLR4E0qDXiffOvayIs9sZqTUZqjC2n46GrsofEwvfguPYLOR-hdPt7gFAWN72lhO3NrYvguc-mHk7EpqzV-el6BfZl588mBwyDkF_h1v8rplIz9JHCrqOFMbgfkw0kpFjN1JdqaFSw-GFcoNXNRDQ_B9CPseTBDbb8jOgeL5EInXIjPJy86wbG0d2_OsloQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نفت برنت: ۹۳ دلار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/alonews/125579" target="_blank">📅 18:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125578">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
سایت آدم و حوا که دختر و پسرا مشخصاتشون رو توش ثبت میکردن تا پارتنر پیدا کنن، اعلام کرده بزودی قراره زیر نظر وزارت فرهنگ یه قسمت راه بندازه تا داخلش به صورت ویدیویی پوزیشن های جنسی رو آموزش بدن!
🔴
مدیر سایت اعلام کرده که پوزیشن های اسلامی و مورد تایید رو…</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/125578" target="_blank">📅 17:57 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125576">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nj-xv3u6pTju7sxulnu4DklEtru_jz9bduEeCVlDrHPHSI5zjB65ZPaFKOf5v0ZY3pi9n0R9biS9WVct1UAanQ3Ufut-yfRYG2Z07jobjvBJcJGNb4oRoU5NGOBCIZEUKvJvWGAY93eyBrbvHjcwp1iL_Gc1ukRyZjjPBOKKMJkTDSgjORnL3dlo9T4UenAmAmOCockXeP7D5vEJBB68xkpmH_FJPBUgw6eczfzrK3L-gr5jOMzZvE4Fs_aJm6qNGGSQlqRaBV81ViodYHS4wVU47K-Uo06e2R-n4yf8KKX-FPSzKU9BiNATBWTXQQf6U7XAK7W9KStGS30hQUeYkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PBAugxUOBSMZ1Yede0_Fzqu-mGGVKyX0Sc60erel-56GY959nrEagV45oyKAtYdtF1MkQMvX0Tqnp1lNrS89qOYDjafKvn-c45USxvDz56dqg8FOb6oW9n_I9oZk47J_OTuVy9gtFEEPgbtnBiGG5BoAast4aT1V6SQkpU8Swr4hyeWX88iSGqAcy_sVOF4HPB24LkUfgIdb7XG3AdV6mE2fC7AlKPVfNLY1z2PikbO9iyk0hWwI9XTF7a1DZ8beArqfRjfQLnlWsXRDE-nriqqUJp1N8_4KWOVibpik9x9rrPPOjJkIHf4X_GrNazOaO059X7Jfw1uDZrcjqCxMxA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
سایت آدم و حوا که دختر و پسرا مشخصاتشون رو توش ثبت میکردن تا پارتنر پیدا کنن، اعلام کرده بزودی قراره زیر نظر وزارت فرهنگ یه قسمت راه بندازه تا داخلش به صورت ویدیویی پوزیشن های جنسی رو آموزش بدن!
🔴
مدیر سایت اعلام کرده که پوزیشن های اسلامی و مورد تایید رو آموزش میدن و چون سکس افتضاح ایرانیا باعث طلاق شده قراره اینکارو کنن.
🔴
گفته میشه این سایت زیر نظر دایی حسین یکتا است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/125576" target="_blank">📅 17:55 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125575">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78c3ae38d3.mp4?token=VbizpjOqa9Sh4YKgGiSyuZAfFaf_QH-tLUgH9lrbiAqbkCwQXRQwY911dWa0PihnF4VnFbp615n4eRknTWUbWhGUJgImRnaNYRZtOw-P_cclnq3lcMhpz0onP420RshLzWdYnJTuLtRzxbH-ss7lpK2jS-W8Nx7mNC2hEQDEuwbeBva65lk60hkQLxaIBeAkGDrww1abf69bns6yrAE31kzLznHMyoCt0dNG6GHuJM7qJmzxhxSAhb3UZr9E2b2QzwzcTYFFlRAtb_elcdPDtZP1y9nNcoymkBsyVTi4MQarxAmQ2wf7sfVp2Ud9dvqRHIhacEHOlNAf9DLJVvWFwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78c3ae38d3.mp4?token=VbizpjOqa9Sh4YKgGiSyuZAfFaf_QH-tLUgH9lrbiAqbkCwQXRQwY911dWa0PihnF4VnFbp615n4eRknTWUbWhGUJgImRnaNYRZtOw-P_cclnq3lcMhpz0onP420RshLzWdYnJTuLtRzxbH-ss7lpK2jS-W8Nx7mNC2hEQDEuwbeBva65lk60hkQLxaIBeAkGDrww1abf69bns6yrAE31kzLznHMyoCt0dNG6GHuJM7qJmzxhxSAhb3UZr9E2b2QzwzcTYFFlRAtb_elcdPDtZP1y9nNcoymkBsyVTi4MQarxAmQ2wf7sfVp2Ud9dvqRHIhacEHOlNAf9DLJVvWFwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
استفاده از جرثقیل برای تکان دادن پرچم در تجمعات شبانه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/alonews/125575" target="_blank">📅 17:52 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125574">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vj1jrNtuZG3r0p3lSLSgUwxYM9jEgZezcPuwV63FbqOclnzkC2PI87yX_tKVoy4ZwK6jm_dEHJO-On7SPpWRhg--vayYJBtuNZJfmVNW8ub1i5CxMl5us2jBQCiTTbzMbMV_AGQQWkMDLrVHX6kmjtG5vKh11hHpWkLzmhUuhD4gH-osm6Z5jtivB-Sg-UJsh5HIXHpDE4zK5cyPGPedxa2jlQynLTdJY1y795_0JfZO5FU-QUjiHIiryzcPgpzV4DgiKr_tEjEfqMz0TWR9qh5iBmMu_ZtlfYMqvBlaAqPlesxV3rF7-8jo9JIp1P193KLxWVETCtOzmlMhks4vMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیصر، خواننده انقلابی: نظام ما یک تنه جلوی امپریالیسم ایستاده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/125574" target="_blank">📅 17:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125573">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FVnsT6JxGDis2HrU0r2UcQvkFJNtAQGTkj_3FPpenFmjWt5OUcMz9dlgnmoM_xbe-UjXVF1PmCHiCBFQN8YvXcQQHISAWMuRk8TYbPrH17YzLp95LYL8h6SRwczQBu0zukCAV9hDIhkiZdaVkjb_DILI31At79A4PZWhm_Iufbt6t5mZIJeAJG3oMBiTKUNuBS7bPXFnPQB-Ge3HPenGnKx1A80fWDo9tHJGrdDJUv5exN-2zpds7dbR1rA7clUezJIwbnozaXpHEn21Qo2RwALfTTLw7OWJ5AENPhqsf5An2_cJjDoXEg4ea1aUTwVFuXKKYyMKCog1RwHxky6nGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خسروپناه، دبیر شورای عالی انقلاب فرهنگی تو شبکه خبر رسما اعلام کرد که تاثیر معدل یازدهم تو کنکور قطعی می‌مونه و قرار نیست مثبت بشه
🔴
پ.ن: دانش آموزا یه جمله به خسروپناه بگید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/125573" target="_blank">📅 17:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125572">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcc2ba7680.mp4?token=fxXZ4igpyQWRCPzxV4fbH4T7eVs4RUHEpo4pOLZcNgbz88dlA6eQmGZiYoPGfqorNuIbUkIePerAtVMa5TECTb2FKc1NsKP6RvDYj6Gm-RDUSpPxajDH2CCYx3mtKd6J4zVTYfZOweq3I7SoLEQSKKNNqzP3ciT-xRs9Joz5veZO79Xko-KfDstXUFZ7Tnji6gqNP2zNNTP5Ven6d37VQVdaP48qYCyMPHWXYi8qYcSfdOBiNxMM3mPl_378AtW6rkzdUhM7TquDtlTdu4n8CEkbWMyUes4TbKnEmQct4GU1-zTp56xJkVJ4t4znPS2ezJPJi_-5kyN9QITQdb91SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcc2ba7680.mp4?token=fxXZ4igpyQWRCPzxV4fbH4T7eVs4RUHEpo4pOLZcNgbz88dlA6eQmGZiYoPGfqorNuIbUkIePerAtVMa5TECTb2FKc1NsKP6RvDYj6Gm-RDUSpPxajDH2CCYx3mtKd6J4zVTYfZOweq3I7SoLEQSKKNNqzP3ciT-xRs9Joz5veZO79Xko-KfDstXUFZ7Tnji6gqNP2zNNTP5Ven6d37VQVdaP48qYCyMPHWXYi8qYcSfdOBiNxMM3mPl_378AtW6rkzdUhM7TquDtlTdu4n8CEkbWMyUes4TbKnEmQct4GU1-zTp56xJkVJ4t4znPS2ezJPJi_-5kyN9QITQdb91SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یادی کنیم از روزی که تو صدا و سیما گفتن ناو آبراهام لینکلن رو زدیم
🔴
فقط اونجایی که آخونده رو جو میگیره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/125572" target="_blank">📅 17:31 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125571">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d397f35c8.mp4?token=eTGI3XvnUwSF02g5kO3PlOloEnrScknEqzUwpftbvUxOIn88N76oyV6pwyh9VutgAzGYT-cCfOBY9xCgKqs1A8Ij28e0mPBkaXGv_Ikjf_pdtIcDc17NuZiqiOKvR1UGAd7X3GJRPO9CrSnemae6sSm5lb3ew6gOEgW9K2G8iLUDR_104i6aSl7wTC3F7BZTFCi_C3mZq5gx7Ud-f5cCLWZqw_JaPnM0HGE0aMX-y24xwkHYTeVkYoGmIUcGvGSM7EIFTCFmDwPYz1QXw3roqgd-8zFIdGZFRfXMpdQCKFGc8dh7AJCepsGqZSr53TaSpcfhleiu3lJSsAIS9dw7Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d397f35c8.mp4?token=eTGI3XvnUwSF02g5kO3PlOloEnrScknEqzUwpftbvUxOIn88N76oyV6pwyh9VutgAzGYT-cCfOBY9xCgKqs1A8Ij28e0mPBkaXGv_Ikjf_pdtIcDc17NuZiqiOKvR1UGAd7X3GJRPO9CrSnemae6sSm5lb3ew6gOEgW9K2G8iLUDR_104i6aSl7wTC3F7BZTFCi_C3mZq5gx7Ud-f5cCLWZqw_JaPnM0HGE0aMX-y24xwkHYTeVkYoGmIUcGvGSM7EIFTCFmDwPYz1QXw3roqgd-8zFIdGZFRfXMpdQCKFGc8dh7AJCepsGqZSr53TaSpcfhleiu3lJSsAIS9dw7Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرزیدنت ترامپ
از خواب بیدار شد و تصمیم گرفت یک "موزیک ویدئو" تولید شده توسط هوش مصنوعی منتشر کند که نشان می دهد همه عاشق ترامپ هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/alonews/125571" target="_blank">📅 17:21 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125569">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OmaXeF1KxkN0pKmmR5JW8hfo9xyxdz4HyeBG6cafrM2L8WiUNRIuZ3Q3xnBCiJmUav4DoIBMx1pTTXSN3ZvQjm7lMpcqRuDmcCGV3bFgIdVAQQ-AtqanyAIcWfpmaUHZaJ6J7QX72DaNMda3l5VUZIvb36Z3rZ7diPZCoqJEYVx8K502KJsrp7KuZ3DERwV1PEPPR2LqDS-i1nyzPB38zvjTNDdt8ub6FYUhUWotAqTUaZ3ZgId9tQ6ZvwdCSqwjOJPYpA3XunUP41o1PZr5LFkzRmF6aNebCO3ljv9Li1WKreum5xLFfAhMuVH1TpizPnHV7ZGTWxr0yNV0eSWpww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HbYX08rcNf53YpKhtJVzKPKmo8-VmHFMcG0k6o7mNSwmqq3W1fvPpKnCwz_wPOI5UXTaTyOHSTUbK-xbYve3a64lok-2X08cQsA8W8xYHPvSEG8hcmdCN5MQ_8TQ-W7Mp577FxQbQ42-GHD5UmlIgiloMGvgV-brMva4nMiLzUAielrK5IyivRUvH8axjGYoTu2QGicNAtdkcsyXdNK8K3zu8GwlCLQRTpVSBGvDA8UsERerU8fPqegZiRENe3O4pIV2O1OmHNYjJyVRPc1L3ubrGCy8-BBnL6pzKwUYAUp5gKcfLuEIHcXDRf3SxSI-IRut16MNLQRYtSFMP3cRlQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تئوفیلوس سوم از اورشلیم، رئیس برادری صلیب مقدس، در دفتر بیضی با پرزیدنت ترامپ و در کنار مشاور ارشد مسعد بولوس دیدار کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/125569" target="_blank">📅 17:18 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125568">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uuo0BoicIyOp-KWdu6Kb5vSphjXk3TDG__szZDyecu4PEVwx3aH9SIc5S-LdBWjIj_S2pnlfAOFjc_oWE7IB32XVIV0CfqYqLjX418efdxVzA4ELiWxgXupaLPdp-hLKxEGwK-ksW4KtkaQpzdXVwgtBA-M9UJJCtXPYDwibdl8PuKEYWDQ2rPqPUz-vChBhhdHsHjVxhH4OX1l1N1QItgkRViK7h-xLaCnLADZCcjKxlTsrlHQS3kQN73pW6ExJL7hL3t6h5QDkTupujLlCE-Y3QdiEjlK5iQqgju0mSRonWO8oMWXNda8VmCLse0pHXU45qpe0wiNs91iu0Y6ksA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫
🏆
به دنیای هیجان‌انگیز فوتبال خوش اومدی!
⭐️
اینجا قراره باهم لحظه‌به‌لحظه‌ی جام جهانی رو زندگی کنیم؛
از بازی‌های حساس و نتایج داغ گرفته تا حاشیه‌ها، کری‌خونی‌ها و اتفاقاتی که همه درباره‌ش حرف میزنن!
🔥
🔥
✅
پوشش کامل مسابقات
💀
ترول تیم‌ها و بازیکن‌ها
🎥
ویدیوها و لحظه‌های فان فوتبالی
📊
آمار، ترکیب‌ها و اخبار فوری
🌍
حواشی جذاب از سراسر جام جهانی
📢
اینجا فقط یک کانال خبری نیست؛
یک جمع فوتبالیه برای کسایی که فوتبال رو با هیجان، شوخی و احساس واقعی دنبال میکنن
📛
💟
🆘
🔞
آماده باش چون قراره جام جهانی رو متفاوت تجربه کنیم!
⚡
@Vaarzesh_Plus
⚡
@Vaarzesh_Plus</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/125568" target="_blank">📅 17:12 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125567">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
ترکیه در حال توسعه یک شبکه دفاع هوایی چندلایه موسوم به «گنبد فولادی» است که در آن رادار، جنگ الکترونیک و سلاح لیزری به‌صورت هماهنگ برای مقابله با پهپادها عمل می‌کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/125567" target="_blank">📅 17:04 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125566">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NfMeQ9sUrEhuIrL6i-J3VUUxdw2RVs_w2McpKU-RagOpm82MbM-pBHBUSKGEdbRkGSrs_XJc5wIJx2taMltTk0sZyAWD7L0_dkwjT4OTSvW6wfR4N8m3ZMk3D9zEMTfpIDP2yCYUQI7KXmG93FDcJpJGDcTT6jdcAgiAe8D0g0Axot7LF8aJNj5OaRWw5cBQHKvUljFdscKkGqXrjtvmszSU_oM45XXeII1TTsQukWVcHvTn9v6230KzvpBUMqhugfITHaUG4IgqqOuZ894AnYfDyCJwgYTYuem3mpU_CYvM-AHWVS5ylF1oCHjjreBoR955oQg0TY_ij-t8Bhs0MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جهانبخش: آنطور که من شنیده‌ام کارتل‌های مواد مخدر مکزیک، ایرانی‌ها رو دوست دارند و گفته اند مشکلی با آنها نداریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/125566" target="_blank">📅 16:58 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125565">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
وزارت امورخارجه برای بار هزارم، نقض آتش بس توسط آمریکا را به شدت محکوم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/125565" target="_blank">📅 16:55 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125564">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AD-zTx42vO1MhcWJKkBVYrA_EyufOWDLQ9nDgGAUV2r3mjH4OZHzXgwvEYHwsN5vf3dnMBjbGhPkcsG8-bGBsr-GG9Roxs6N2iAQCr0u1Ezj3W11CRxNjgyt41dlzr1Tm4rPiD5gzRLU_vMBSjDyOBb3PwEtNWrjdOqEFcLCz50iD3RsC-qp_8gFsR6XCviFFoH2E8SkXeo0WVG7gpj1rVRVQpGehhNd42tHu-vU88sApCLV59PK7eok2OuJYiGcT1Gc8K-Ixd4BmS35uyZRz7pSDDEybPDAqH56YCEbbEAVlWbQw6WTZypR0prLDLH24QbMmk7F5jFj6vDUfcRaqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نفع بزرگ اقتصادی چین از جنگ ایران
🔴
جنگ ایران و بستن تنگه هرمز، به صادرات تکنولوژی‌های پاک چین مانند باتری، خودروی برقی و ... منجر شده و به ماهی ۲۰ میلیارد دلار رسیده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/125564" target="_blank">📅 16:53 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125563">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nkFwQ4iCK-FQgq-AusIJrUp6p8qnfgrJGG6Qf6v2X1j6odwDDpQZuqy94644eW0tSPxHel_IaTPHf-bfVtFSMgcFKvQrOC6v345TclHw6BUjnhYE_OURQTeAPziK3UQoPm1YMRNAaMSQvIO5IhnyfibfBS3Gyt9EkZSMN8HUfdavyv-etJuIIYnAHlRWzgOAIJaA_GRIrMlC-6SZKb6bv_fSdqmfogEU3UXeOnKhTY7KU_vKO9EG1Y372grGVIAqym28NeOvhS1Y4QsLfv3vvKATtjg6bPUKFzwyKGHNzmD_z7ZKGoEpGS0F7ci2pFjvltu_udjFfETxTgbhXbhPiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیدار وزیر کشور پاکستان با شهباز شریف پیش از عزیمت به ایران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/125563" target="_blank">📅 16:49 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125562">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
پست ترامپ با عکس‌های خودش و آهنگ : ترامپ ترامپ ترامپ، هی دونالد ترامپ...
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/125562" target="_blank">📅 16:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125561">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
مسیر غرب به شرق تونل نیایش و پل صدر امشب (۱۶ خرداد) از ساعت ۲۴ تا ۵ صبح مسدود است و مسیرهای جایگزین، بزرگراه‌های حکیم و همت به سمت شرق می‌باشند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/125561" target="_blank">📅 16:41 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125560">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
خضریان در نامه به عراقچی: صدور ویزای ۱۳ کادر تیم ملی در بالاترین سطح دیپلماتیک پیگیری شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/125560" target="_blank">📅 16:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125559">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
وزارت خارجه کویت در پی حمله صبح امروز به پایگاه نظامی آمریکایی علی السالم، بیانیه ای صادر و این اقدام را محکوم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/125559" target="_blank">📅 16:39 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125558">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
وزیر کشور پاکستان، لاهور را به مقصد تهران ترک کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/125558" target="_blank">📅 16:39 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125557">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
وزارت خارجه ایران: وزارت امور خارجه موکداً کشورهای منطقه را به رعایت اصل حسن هم‌جواری و پایبندی به اصل بنیادین حقوق بین‌الملل مبنی بر خودداری از اجازه‌دادن به طرف‌های متجاوز برای استفاده از قلمرو و امکانات آنها جهت طراحی و انجام اقدامات تجاوزکارانه علیه جمهوری اسلامی ایران فرا می‌خواند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/alonews/125557" target="_blank">📅 16:38 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125556">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
وزارت خارجه ایران: نقض مکرر آتش‌بس از سوی آمریکا بار دیگر اثبات می‌کند که
این کشور نه‌تنها اراده‌ای برای کاهش تنش و بازگشت به مسیر ثبات ندارد،
بلکه با اقدامات ماجراجویانه خود امنیت منطقه را با مخاطرات جدی مواجه می‌کند و
مسئولیت کلیه آثار و تبعات ناشی از این اقدامات غیرقانونی و نیز هرگونه تشدید تنش احتمالی، بر عهده دولت آمریکا خواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/125556" target="_blank">📅 16:38 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125555">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
وزارت خارجه ایران: نیروهای مسلح مقتدر جمهوری اسلامی ایران در چارچوب حق ذاتی دفاع مشروع و با هوشیاری، قاطعیت و اقتدار کامل،
پاسخ متناسب و مؤثری به این اقدام تجاوزکارانه داده و اجازه ندادند که اهداف شرورانه طراحان این تجاوز محقق شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/125555" target="_blank">📅 16:38 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125554">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
وزارت خارجه قطر: ایران نباید مدام با حملات بی توجیه خود، امنیت و آسایش منطقه را برهم بزند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/125554" target="_blank">📅 16:37 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125553">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce4f1fac45.mp4?token=UOJ2-YsPhGyCeFiRUNguRD4vsRQD2geK9bgZPFHoLPGVJM4YjC5h-SqrZ8TTGq5DgqYQP6AWSIS_-LITdS9fpV1rkbsCKy6Yxx-8-0CMS5Xj0IAbwI1EaRRhEu-zAv7agwCvr89RflI76M63eQwjYoQHGf9W7O_VkocXeVMS2oYxLGR8XRwlBpoh-ZBE7ieHgbuP_ucuv10oQ0Eg_kWxvHRnJxBYSgyaD0sc8kJ36_Gc4oPfQ2PBZizQKUqFpeHyLcXhopAiITr4i3EyJdfPmZwbH5Bndl8I35RGSgJyvXUkevfQDsyMbx-vicldom58vutS3pItfS31jy_cwaBogw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce4f1fac45.mp4?token=UOJ2-YsPhGyCeFiRUNguRD4vsRQD2geK9bgZPFHoLPGVJM4YjC5h-SqrZ8TTGq5DgqYQP6AWSIS_-LITdS9fpV1rkbsCKy6Yxx-8-0CMS5Xj0IAbwI1EaRRhEu-zAv7agwCvr89RflI76M63eQwjYoQHGf9W7O_VkocXeVMS2oYxLGR8XRwlBpoh-ZBE7ieHgbuP_ucuv10oQ0Eg_kWxvHRnJxBYSgyaD0sc8kJ36_Gc4oPfQ2PBZizQKUqFpeHyLcXhopAiITr4i3EyJdfPmZwbH5Bndl8I35RGSgJyvXUkevfQDsyMbx-vicldom58vutS3pItfS31jy_cwaBogw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فیلمی از ۱۸دی خیابان سهرودی تهران
🔴
از سری جنایاتی که جمهوری اسلامی با قطعی اینترنت در صدد مخفی کردنش بود.
🤔
عرزشی حرام زاده این مردم تروریست بودن که بهشون شلیک میکردین؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/125553" target="_blank">📅 16:32 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125552">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
شبکه ۱۴ اسرائیل: همه امیدوار بودن که آتش‌بس دووم بیاره اما ظاهرآ قواعد بازی داره کاملا عوض می‌شه. خودتون رو برای  آخر هفته‌ای داغ تو خاورمیانه  آماده کنید، زیرا ایران و آمریکا درحال گذار از حملات پراکنده و شبانه به رویارویی‌های گسترده در روشنایی روز هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/125552" target="_blank">📅 16:25 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125551">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9995675c84.mp4?token=Z6FzkoI-K11M0776wP3bVkeJFxd-ULYstiYE94UsXlHC2iEjyxPnXS2NUrwjQKB8Fj-6y3EOAhi7WEncrYoqAsGbVf-QWauopxShzcn0IGSo97BCujk_aA3yNKyrcvwl8GRXfjYYJNG2-VwG0R3ev_CJA4D_Uvga5nwUnoWSJBWG8fpSN8CBHYYxIzEAqlgM7v9lj72AuAf7EKE3eooUUA_s7FyiPYdxzvzJtpyasT4LaU22AO2WJDe7tcqIB47QrBiIBt3MnzCT02P4MEB8csWLMLGJadYF6e725opjqnU3nEVh1oet9PdVSmqqOV0JRAWqCwEXnJsw-jj6JTHntg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9995675c84.mp4?token=Z6FzkoI-K11M0776wP3bVkeJFxd-ULYstiYE94UsXlHC2iEjyxPnXS2NUrwjQKB8Fj-6y3EOAhi7WEncrYoqAsGbVf-QWauopxShzcn0IGSo97BCujk_aA3yNKyrcvwl8GRXfjYYJNG2-VwG0R3ev_CJA4D_Uvga5nwUnoWSJBWG8fpSN8CBHYYxIzEAqlgM7v9lj72AuAf7EKE3eooUUA_s7FyiPYdxzvzJtpyasT4LaU22AO2WJDe7tcqIB47QrBiIBt3MnzCT02P4MEB8csWLMLGJadYF6e725opjqnU3nEVh1oet9PdVSmqqOV0JRAWqCwEXnJsw-jj6JTHntg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سپاه فیلمی منتشر کرده که نشان می‌دهد  آن‌ها بامداد امروز موشک‌های بالستیک به سمت کویت و بحرین پرتاب کردند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/125551" target="_blank">📅 16:22 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125550">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7e63a2b05.mp4?token=COjtLsQLZnv0zi4JSZ0u8Q-gz8o2GsCmnoaw4_zWlpZYoNQHW28eSx7GQvES72g2usEwPhgEOR7Yh2W7Ywjbh1vmSc7mpEwSAHt3UA95rWlWSkesD-6VsrtV0XKJQlYC4FvGAW_aGBE0hupLtlRxwYyvmrBGZv_7O9xy69yR56YNShxFDg32u_lei00PK_xXBO2DWx1lGxruYqoZDRi96eeBcyxgX8e1Z3Aa8hG-pHaZGuHZSpjmu1vdAh0qdRkP-dgPZ-sK6V6cOg4jFve5ntovYhvM4sjmV9X3tGdS1uET032jc2oJxUvlqGvxLmP5Mn5AP0r-dhYNH51rGflg9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7e63a2b05.mp4?token=COjtLsQLZnv0zi4JSZ0u8Q-gz8o2GsCmnoaw4_zWlpZYoNQHW28eSx7GQvES72g2usEwPhgEOR7Yh2W7Ywjbh1vmSc7mpEwSAHt3UA95rWlWSkesD-6VsrtV0XKJQlYC4FvGAW_aGBE0hupLtlRxwYyvmrBGZv_7O9xy69yR56YNShxFDg32u_lei00PK_xXBO2DWx1lGxruYqoZDRi96eeBcyxgX8e1Z3Aa8hG-pHaZGuHZSpjmu1vdAh0qdRkP-dgPZ-sK6V6cOg4jFve5ntovYhvM4sjmV9X3tGdS1uET032jc2oJxUvlqGvxLmP5Mn5AP0r-dhYNH51rGflg9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روسیه در حال استقرار سامانه‌های پدافند هوایی Pantsir-SMD بر روی پشت‌بام ساختمان‌های بلند در مسکو با استفاده از هلیکوپترهای Mi-26 است، به عنوان بخشی از تلاش‌ها برای تقویت شبکه پدافند هوایی پایتخت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/125550" target="_blank">📅 16:17 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125549">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
وزارت امور خارجه آمریکا: تحریم‌هایی علیه شبکه‌های دخیل در قاچاق سوخت ایرانی. ما سیاست فشار حداکثری بر نظام ایران را ادامه خواهیم داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/125549" target="_blank">📅 16:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125545">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aph_W4vCwxFej7kP9bcAmNFp5_AhGwcZMP_W3a7iJALTknln2KOfJTXsUuIJZAMpbrFCFKaDeQhJf6Po4mHQV3zQnpLSyN23uUxrkzWXJ0pl_vgiZtnvrh1-Ga_AXqz_3k5njel9RSg9XBL07tfpkG4VXmpDnt052nA19npY2DKiS6p8H0m4G1sQh3CKYd85pgq0pRM3FjHf0vJpeJSuCN9RjmW5_5s6FEc-7Ee6wGSstJEomVbZPebnuX_fYya6leiYnT9nqHCD0kqGTXdKdOnl4SfVkrnxJo36xEbQw7oqUhnknTX-3HB6f5EFWPh6dRu7kmDb4AtseNDbJ4dt5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ukxogvXu03mnsi86GAT3zS8S7RsQDQ_XNDKxqyXlzrcUS1Wgao42NNRgvz5CqxjvNghmvS30VVNVb4Mve7yJDq5iDdcd0HSQe0TLY_rbE57FuwzVmANVtVEenkv_2XH1ALEnSJTxr0atRluNRlsHsGZ33c0qi5f5qxgHXEYpTteqhgfZWFVl_ylv3W1kMW3pvXwgn6Sp17_QMh5DJp1qbK1WkITX3mPw1-0BtZ0zZT6oBNRXopG5UiIBT66XEKX61svB7n9PjncdvHEY5GFmBaLq_HSQXmXlCXl7BuG7xbVbaNLjBIRYyhY-O5HD14g0vIFZNHXR-0waUy37FJRCGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F3gklu0Z659sp4l_Pd-BERyBebqhdyutSdaDc81M3y4JijfMXLVHhSQyracMQOBaKtImQvCVmGlqgZubEIUuYCQVGLUmbUIMoMqNj4IYZdyhfhi3MqqjGjr-JR1u7a4nTN4AVhirVYfIR2KTDXKe8BWKWVzLMseezwwai6JqVuPF63aBj8eEtNUfld26Uqb7z8dtU7UAzDQEN4mNph3wyTn9mtoFv5NqAjXRiOriCa_4hKvDqzHWlNRnzsnRCKw-eXSlpC1DvrF2m-SxdYJRseyieO9g5MbPQJYY-PQCd9Nf5GsEM-u5EKsx1jKmek4-J1aQNMShghiO4o35LvD-Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VJLGNtkHRDF90cL1g9PhZ4Md37TT5GUTtO04ual22Q8I0vtknssytVSUPQ55hrEk_uOxUM0GyXn1-CzvQJccXQtb5sVMgSXoskkYFsJ_dfnSvxrS50e-Wb_bh7j4UcYbmtSxzvz_fiV5mnXdlJULZ1rvd9KCrMQIX71T1dRDoyfRTutFQDmZLTo4TC2dSf0FOFb6yjS3d_EVRwxdcAtVWHLAGadpaHSHL56zPFFhnUCm7BTOUDrgltlAYCfmU757RXWL8eetXeLK7Y_EXsBU-fUYYGlhAXQe3kbeSQ4i9bZ8W6bvvGVUozr5Xxi0pwRoQH51FqPdIoazSPQxiy1TPw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
جنگنده‌های اسرائیلی در چند ساعت گذشته حملات هوایی را در سراسر جنوب لبنان انجام داده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/125545" target="_blank">📅 16:09 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125540">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vNuiS5AFfW_iFH89Z7ixie9JF7Ediovlm1BLeFLh8SNEhDf5h-nyDr78STNWkculx5qGTe5stoneTJmyOrYXiFdRZhBuHt82PWlQ4NlZQhYftcJBmH1i0w8Or9fwewXB9CAjO15QBa4p_BKYqqtTI_plt7_FUmdZ7wgUEQkKzxwGTQRahk6C2r0oEnUuT-f5KcvM2yW37xcI7w7foWFxq6u269mMZPfgDd7AzgzlwUUTw78Jls2k6ifvzXCSNpmUorfLY2k3Xr5OoHmc-Pl-KjMlJ3M6V9-3inABm7cnqeiu2B3EEivTRCjlnN3n3K5JU5DiBdc9iDALip0jrYRBLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kn9dlxyUCol9eyhU0z9x5ch0kDv5n7-x0vpNwLX5-bYMWWWjAdZXurs6Ttm2xmiXajOBARV1fgq8EJ83AqFOY3YBk8pM04XxeRendMA-dxYhq3II80POQG5NTFIbAOMn94SakpPu6TeEwVBTpiszXRH7D6GdMNSAd8qG-1EhxquR3r-e2pRdeNrymNn2SZgfUnGMJogAzxiUC8GYpW3-e9zIexkwfAHuLBkjm8gYsEtJwLHfWnY7O1XShLgj0CvS-96YNKSsqhXw9nLyp7FoJS2dkDDuaOK3ZoB120MZ8N1FWo2EZRVjSANy-Q71HyAlsLUWJlGmRJComzp2SEQEKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nb3d-npASTk_34aKBEGaMycquC6Re_utibdYiiqjDt4bkeZvZn0VFvzu5toNmvtpTgNBGDARZB-wcizGmSlZnuOdBJqpxDhaeul2DTlON-oicPzQfIjtcZGCyS8NrwtwSgCY6hmFOyf5sYNXqcNCwzPtB_IRAbHZsYk0cLaLe8Af3OPQcrtdJOuzcF8z2-Kuaje6uYS4p1Z5hKazsElXltdV7ShdhmsXCJUIhziDYkfuWfVBsYfY5ZBswmHAWfqXc38zSXIX-S7EhDVPBQOnjfvkUl-f4u3yoZB4-j9H4lOWYsemqRx9PwjZlrY-ijsFxRgIKGe4y1wUpqthDGAbZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cPTcs2CLeYewkBzdarwJzHQfTSwLplTKD66YH1f2oX8d1BdCO5KUFLfXVsdk_SQpEouakSVsyhyz_PLRBpSf0Iifkd0w4z7HXgDRVJt7YCWr7q7bLvLjM5Fa_c_ekA4gGjUfsUgoeC_-tDGlE1I1QKY9Oqm7orBNcl15e7JtfQIZrDNQtDbeLgOfCcCY_C1JMH69RuFYPIUUFtq_iwONyXb-N33tnKOkXBFeodr-vtKtYdW4H-ejP14TxBtPYF7WgYM5nRtdyeGAlGPpxAjVaZAdmCkUIP_lj-mzF36IfrkAuDf2tRyqBXLAhJOHRro6KOeQh-I9E9dhnYDh6C-hQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DCXhqUMNKOxSWPRichIZMEaexHjHFBOGt4xGs-_G7Me0yDVTvMOVmxnNqe_Dpv8HmwTRGHH6JpOatG4wXFxG6Z76Far43RD7sZlWo1r4WVgdpGmqv9irrkHaYvmvh-HevUF7sRFT54mRlP1dhy8wEjIn8fGUOJSvjgY1TokiDSKOMfNsREK49BEAfnjHyZHLr8v5tuYbZ-OHwtwr1Qnt1I4sdWOMBaYstjmyQkGu9ptMS9hcJNvmPm0fpr_vHbLghZCby8SmM9G28BmnTP4EQWuG8vROwuAqk6iMkdJeMgXOXzRKvnqGWusx2vtINXJUTdEMp6gwlfTz5JNknDbIPQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
کاخ‌ها و دروازه‌های تخت جمشید
۵۰۰ سال قبل از میلاد مسیح vs امروز...
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/125540" target="_blank">📅 16:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125539">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dGDJiEEihDVnGj2DJqHp3PlhmndUYQJYlCcdP7Zy8TlKxhxvZLB0T-4H3-QAM8j7TCKCnuDiTRfIC8QQtIc-Dv3t1TV_fYo_kTZTLPsWPnSJIqwrMuxpTbyOwfVaruKuerH3avlRqsQ2mzGEKHkS--3rQRWC20-dJxBl2X6X8FMN-B_ypzhvkoMaNw1nynqJC6Kns9M6wgmRNyhWcwp2jSrNd9i5DifIaGNPJc4NUbnthR7eu6E6gnr_CFyr5BBwyOx5P4uZJXwO1kSq3QG4csfBfyDGJZrYJtWE4fI1acJU-i4daSOrE4z6k02uVfUI0BF0lPWAQStH5FiZLKDdVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بلومبرگ : پیش‌تر هشدار داده می‌شد که بسته شدن تنگه هرمز یک فاجعه تمام‌عیار برای اقتصاد جهانی خواهد بود؛ اما اکنون مجموعه‌ای از راهکارهای جایگزین توانسته اثرات این بحران را خنثی کرده و مانع از عبور قیمت نفت خام از مرز ۱۰۰ دلار در هر بشکه شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/125539" target="_blank">📅 15:57 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125538">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JSMfRatoZRerlYrCC45QPIMT5ZDw1U4SvYzS-PfAuCrYa-2GGVU7OyA8c1VggjNBmdZ_kkOer9-TfK6asQhZecVT0WQJzY6rdqvolwEOS3XuPKX_DopL1efCgYA5NAjhv0uQYFUW51DWCu8K6uC58h4vpES6zfZ8FQmllnKZDBDp9yNeyXqnN-di9AY01zyjJkurdcNSMlFPaS9W1mQxNyJqFyeZt_hDzmL5ITK_KiXcIv8p8XJ_optjjztgzVkBBKr0Z0mBkCfZrmXc-_-4wlESGhMoY_c-A5ysxERlHmRlvnD0D2iUdSPM3tKDuszio9_1cqwhgA8Lh3BwnkJyeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ستاد کل ارتش کویت در بیانیه‌ای مدعی شد سامانه‌های دفاعی این کشور امروز موفق به رهگیری و مقابله با ۷ موشک بالستیک شلیک‌شده از سوی ایران شده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/125538" target="_blank">📅 15:54 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125537">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
صدر اعظم آلمان مرز: آمار مهاجرت غیرقانونی در سال ۲۰۲۶ نسبت به سال ۲۰۲۵ به میزان ۵۰٪ کاهش یافته و نسبت به دو سال پیش بیش از ۶۰٪ کاهش داشته است.
🔴
ما این مشکلات را به روشی بسیار آرام اما بسیار مؤثر حل می‌کنیم
🔴
ما به افرادی که برای کار به آلمان می‌آیند تهمت نمی‌زنیم. ما از آن‌ها استقبال می‌کنیم.
🔴
ما می‌خواهیم آن‌ها اینجا کار کنند، اینجا زندگی کنند و در اینجا ادغام شوند.
🔴
این دیدگاه ما از یک کشور باز، لیبرال و آزاد است — نه انزوا، تبعیض و تحقیر شخصی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/125537" target="_blank">📅 15:49 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125536">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C28C5mje19vK1r630f0IdeLHxvwBHgZ23Kt-6V6-9c8GlJnrfsZxGmrasazmBCyIcm6PwZzt5dEiahW0MNQPGyyrzVWSRdBJ59jhNzbTSihoTRVpzJs7a5eMpZgj6oKkTr51M-44PjvxVowtTW4l0DkUe4e29ULgTUmEspdwmbAjxZvlUQjYr1Yd7ZB17VLIA4bx9DZfWqe1ZW5gYa6XZVVqU5bWVtyLFLf15lrBTt46OZDplzPkKrCXRJdxc4tQsRnK7r6Vq17xEUSY-jYNtOzHWSUT0oaBRELRTtqIwpCd6sQJVzlTRKNIs_MIeehJXAY7q9dE90HHT977JIGqtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزارت امور خارجه ایالات متحده فروش نظامی خارجی احتمالی به ارزش ۱.۵ میلیارد دلار به نیوزیلند را برای پنج فروند هلیکوپتر MH-60R Seahawk و تجهیزات مرتبط تأیید کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/125536" target="_blank">📅 15:45 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125535">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97ae3c51ca.mp4?token=XvRpqLJTZGB8pY7081csxqFPThwib7mZhlPNSRz6nMOcB3WHFNMCIPr05JoJG76MAuY5kgDu78gfvkxpfh0wabJuGf61fjhmgZ0bf22LW1kJ6ZIAUZxE-ZlJ-Bl2NjLzY4__LjQlsU-0fXDGFBO6DPLNDTnRPkgtiJ0IUdOWTmD9ZZK7HC4PKks2_NBE7Xd6D1Jb_9Uwz5Ft4Rozhr3kh182eAWtg8K3Sx_HFB0bkDkgRPhCF3N_NKwXI7gqgbLbHBXNS7F2SgQ9K5i7-i5IO8dhtQK9ZVXl7cF9dqlu2ngpVmkr979tWongH4NUnOOz8uMasPvhN3pKw-fTIDY6Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97ae3c51ca.mp4?token=XvRpqLJTZGB8pY7081csxqFPThwib7mZhlPNSRz6nMOcB3WHFNMCIPr05JoJG76MAuY5kgDu78gfvkxpfh0wabJuGf61fjhmgZ0bf22LW1kJ6ZIAUZxE-ZlJ-Bl2NjLzY4__LjQlsU-0fXDGFBO6DPLNDTnRPkgtiJ0IUdOWTmD9ZZK7HC4PKks2_NBE7Xd6D1Jb_9Uwz5Ft4Rozhr3kh182eAWtg8K3Sx_HFB0bkDkgRPhCF3N_NKwXI7gqgbLbHBXNS7F2SgQ9K5i7-i5IO8dhtQK9ZVXl7cF9dqlu2ngpVmkr979tWongH4NUnOOz8uMasPvhN3pKw-fTIDY6Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اطلاع‌رسانی عجیب مجری صداوسیما: مرکز ناوگان پنجم دریای آمریکا مورد اصابت موشک قرار گرفت؛
نه ببخشید اشتباه شد
؛ صدای انفجار در جزیره خارک شنیده شد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/125535" target="_blank">📅 15:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125534">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">✅
با سابقه ۵ سال فعالیت مداوم
🛡
حتی بدون قطعی تو دوران جنگ    برای ۱۰۰ نفر اول و یک ربع بعد
😍
❤️
🔥
آتیش زدم به مالم به خاطر عیالم  بقیه هنوز VPN حجمی میفروشن اونم با قیمتای نجومی
🚀
ما چی؟
💯
💥
VPN نامحدود واقعی فقط 190 تومن
🏷️
🫴
ویژه ۱۰۰ نفر اول
💥
بدون محدودیت…</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/alonews/125534" target="_blank">📅 15:39 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125533">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RHvUz67QqPXuBEOympxb_88uVEzkKMceRbqxNxhVQ0eaSj4BkO1HuvkwNkfK_1q6T7INrL8QknPJL2pI1WsL2zvh-72kOb8o72ZuQQ_z4FjawptzmFb9dBdEFPqxpTaugdGcfn1cB3QdtCqSZuJ8okMc1yWzHaEhF2I3f_fFgXVXCc8UEAMobZQqorXKRW7DhPUrAfyc7fK_rmlY3N3UBt6ij8pG1Ds2YyQYPdq-N2mrYl5REjsjrTpvOlyxWRye4lUtb8Bvp7yUD8rJF2MGRuhKjfPBPK6mk7oV_H2H_CmzDEkkMxHotKir9siB9zVHxavI7DhJURdtiDNdjC3MEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با سابقه ۵ سال فعالیت مداوم
🛡
حتی بدون قطعی تو دوران جنگ
برای ۱۰۰ نفر اول و یک ربع بعد
😍
❤️
🔥
آتیش زدم به مالم به خاطر عیالم
بقیه هنوز VPN حجمی میفروشن
اونم با قیمتای نجومی
🚀
ما چی؟
💯
💥
VPN نامحدود واقعی فقط 190 تومن
🏷️
🫴
ویژه ۱۰۰ نفر اول
💥
بدون محدودیت حجم
@NetAazaadBot
@NetAazaadBot</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/alonews/125533" target="_blank">📅 15:39 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125532">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bFUWvuM43TKnQKETj2V9JjK0y4fq4ftc6L9aSEhMDJ3nSB_YesPN0NQFk3UZSg5MvsZ_LicOPtZT7F7WyksSdZon-rj1IC1vF0c4IeBPaI--Q7CnXjuflQvwP-4cVgdVND3i29H3hidi966TFCcv6Vc67lo-XWkslvY26RQeaxDKBPrrEakvIWgdiURZxt90zkEhVEHvRUfgQUkDX_CnTDXQaIcAiosG5MCxGqjZpFtI5LtCh6BY8t2khmCCbF5XzL2_ISGi6F8n-BbAvaHV8YdHDdjwaVBS89ZtU0oSQvBU1D8z6L67yjnVwPedXhS3LKjtaJxT-sGI-y0uHsO01w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بلومبرگ : از ماه می ایران نتوانسته نفتی را از طریق تنگه هرمز صادر کند و ۸۰ میلیون بشکه نفت ایران پشت تنگه هرمز گیر افتاده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/125532" target="_blank">📅 15:37 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125531">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔴
فوری / الجزیره به نقل از یک منبع پاکستانی: وزیر کشور پاکستان در سفر به تهران حامل نامه‌ای درمورد پیشنهادهایی برای بحث منابع ارزی مسدودشده ایران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/125531" target="_blank">📅 15:29 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125530">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
سازمان اورژانس : روزی حدود ۶۰۰ تا تماس مزاحم داریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/125530" target="_blank">📅 15:26 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125529">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kQ459Y7cJP38PHx71VFI-JF7M_ZSIobV-t0IvxPk9g93ZCgbaH6IwyNfFVOxWoJSeGbwY9GIhV2upzDDl4GD58cKv3kGq_GVfEtAfPiZ9pwTyZgkjK_Cb_ysrycVkeQ5TY0LA7Yci8oEKavA4F-vKRi0HNy47vTtWz1kECg1QBFHn_dT8Pz1bJmV2HGsl5OvR06yB2dF_4w4nxd1m0ewEwExpxlUK4v5iqUQhqk-dE-3XcPfZhhmnEQgqJNLVs_Kg08_F-TQPex5CtBCzOragKpoVnU72IyNoWr9R7L1Gux-XKxpjyGIs_OA9CjSNyC0jzddE7-f_bShurr3V9Z1jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امیرحسین قیاسی: سکوتم در جنگ اشتباه بود!
🔴
حتى در صورت سكوت هم معلومه كه من مقابل كسى هستم كه بدخواه كشورمه.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/125529" target="_blank">📅 15:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125528">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BbYGtnLWdkBaBtuGfoHi2ezVyrIy5BTT5aiSWvuTT8WCv-u41MjE5TxXb9E8B76xTrMYwSRm_QrItDZeuBdS4FFJTBbvMhRo6zEQUSVCOE-ooxc_yjGIAsDP0fZgTaHhyvPIHjApuljt3KYX9myOjwIBRC5h53uccDA5P7VQ3ZemkWWniywNZOO_2WYXPYiQU-l8fsoyIVyegtgIJgLbg9dkZJLFSVA2ulUjWuyLzsxzKlE7iuG3JjGxVwEJhtHEtLlbrapHVr3NRR7HoaTN9_QplQ5El-Iz7K1X77e52Q_91Demm4vyTN4q7kcVENPZE9ZUwhN6vD7xZEBFatp9Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزرای کشور کشورهای عضو شورای همکاری خلیج فارس (GCC) جلسه اضطراری تشکیل می‌دهند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/125528" target="_blank">📅 15:12 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125527">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70f4e56d3b.mp4?token=fU50Hs6QBDgx7xorn-yLgg_imy3Nw9IVoJNMQRFMHw2IesPxAI9OlELuUEMktkYkTWdbJTVd1WRCwHE0C6meOKme1JKy_j9g7SJcgCC5ThIGCyEyGTbsVml0SZJ51LV3c8VSwK4xKgEbTvmWzcwg8l7YAjFo3yglRrzYDbtTlv2JFY1J1RoYcC1eQs87y_z2mc8x8ksfNQgNV_ThRhjpFNaTuUMCocJW_HB-hi0BcIKAWYZZrG2Np-qY_eJht0dai_wbkChqEltBr14nt910R21Y8-oQQUZs1HjjnJ763l9t-eqqC0OUUucCXy4PCPiYNr7C_azXulU1BctXf9bEag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70f4e56d3b.mp4?token=fU50Hs6QBDgx7xorn-yLgg_imy3Nw9IVoJNMQRFMHw2IesPxAI9OlELuUEMktkYkTWdbJTVd1WRCwHE0C6meOKme1JKy_j9g7SJcgCC5ThIGCyEyGTbsVml0SZJ51LV3c8VSwK4xKgEbTvmWzcwg8l7YAjFo3yglRrzYDbtTlv2JFY1J1RoYcC1eQs87y_z2mc8x8ksfNQgNV_ThRhjpFNaTuUMCocJW_HB-hi0BcIKAWYZZrG2Np-qY_eJht0dai_wbkChqEltBr14nt910R21Y8-oQQUZs1HjjnJ763l9t-eqqC0OUUucCXy4PCPiYNr7C_azXulU1BctXf9bEag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فوران آخرالزمانی یک آتشفشان در هاوایی
🔴
طبق اعلام وزارت کشور آمریکا، فعالیت این آتشفشان در ایالت هاوایی همچنان ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/125527" target="_blank">📅 15:09 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125525">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TiVSr0dJkXYYHeifbGYzOTk8u_UTMXUBmp7aKFzQUrwxW_vBFVlaF8urgRri12qmcZvEHVjvnx7Mt4ph4SRMCKu9v_dxsRGdzaM7NFFjioCM3QW_AyC2gGK6_1LeriFhQCpquVcA-L293jDcwM_GEBQB-iFNZQFM6iKf_wFecCypGimItPeg81CABHP1yU_9zfDkOjo7aRK_nG8oBoxzxlBF2JLlY7Hrrp9zDu3z6xsQ5pvhW3Egq1LKItmGoiybC99mIsA5LIsAqHZZovU6y7KHmet6yBE_lkecqb6i00g-FsYxRR29-8mqLnBxIX8Sz0BhDVPziTws0gOzANbhTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e25126b98d.mp4?token=AYSrVuWR_kxz3Y3Dub6dyHioNUianu5UNxzlv7wXAB3kvH2njtZ74bZO6lksPnKQ1BCBbep_6fDDVlNvvVd0ldCLnGh3xa4vwBAlhTDGNV45rfKB1ZlaQDYsSQ7-d0qIBNNQs5lNjq61oytowdKwlA_5wg69CgEHi9jbDZiDEk-jUJHzWYTT5HjKvzGDP7_MGO-lzxTyITwrtSUjL_LeSoklcMRA6DG4PKPZKjImlMTvr6VT4loirBirV9X48NoDYiFeQYtJtkDYGQfCLyg2BkEYnQbLm_1Uxud4Ahqx4-YG6UG7BcxLzoBdb1TIRZG7zj6H2uU3ibMz7D9Xn0Czdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e25126b98d.mp4?token=AYSrVuWR_kxz3Y3Dub6dyHioNUianu5UNxzlv7wXAB3kvH2njtZ74bZO6lksPnKQ1BCBbep_6fDDVlNvvVd0ldCLnGh3xa4vwBAlhTDGNV45rfKB1ZlaQDYsSQ7-d0qIBNNQs5lNjq61oytowdKwlA_5wg69CgEHi9jbDZiDEk-jUJHzWYTT5HjKvzGDP7_MGO-lzxTyITwrtSUjL_LeSoklcMRA6DG4PKPZKjImlMTvr6VT4loirBirV9X48NoDYiFeQYtJtkDYGQfCLyg2BkEYnQbLm_1Uxud4Ahqx4-YG6UG7BcxLzoBdb1TIRZG7zj6H2uU3ibMz7D9Xn0Czdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فیفا ایرانیان را از آوردن پرچم شیر و خورشید ایران به مسابقات جام جهانی منع کرده است.
🔴
یکی از راه‌حل‌های هوشمندانه‌ای که ایرانیان ارائه داده‌اند، ایجاد اپلیکیشنی است که به آنها امکان می‌دهد پرچم را به صورت دیجیتالی و گروهی نمایش دهند.
🔴
از ۴ نفر تا ۳۸۰ نفر
👑
https://www.iransync.com
#جام_جهانی
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/125525" target="_blank">📅 15:07 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125524">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
وزارت خارجه قطر: بر ضرورت دور نگه داشتن منطقه از پیامدهای حملات بی‌دلیل تأکید می‌کنیم و بر کاهش تنش برای بازگرداندن امنیت و ثبات تأکید داریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/125524" target="_blank">📅 15:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125523">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
الحدث به نقل از منابع ارشد پاکستانی:
وزیر کشور پاکستان پس از دیدار با نخست‌وزیر شهباز شریف و مقامات ارشد، امروز عازم تهران خواهد شد
🔴
نخست‌وزیر پاکستان دستورات ویژه‌ای به وزیر کشور خود درباره مذاکرات بین ایران و آمریکا داده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/125523" target="_blank">📅 14:55 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125522">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
سرتیپ ویسام صبرا در حمله‌ای که صبح امروز در جاده خُردلی رخ داد، همراه با تعدادی از نیروهای نظامی کشته شد.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/125522" target="_blank">📅 14:52 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125521">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
منابع رسانه‌ای و وزارت دفاع بحرین از وقوع چند انفجار درپی حملات موشکی و پهپادی به این کشور خبر دادند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/125521" target="_blank">📅 14:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125520">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
اینترنت  دیتاسنترها همچنان قطع است
کسب‌وکارهای اینترنتی کماکان با مشکل مواجه‌اند
مدیرعامل شرکت آسیاتک در گفت‌وگو با سیتنا:
🔴
برخلاف برخی اظهارنظرها مبنی بر بازگشت وضعیت  اینترنت  بین‌الملل به شرایط پیش از دی‌ماه سال گذشته، دسترسی مشتریان مراکز داده (دیتاسنترها) همچنان برقرار نشده و  کسب‌وکارهای اینترنتی کماکان با چالش مواجه‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/125520" target="_blank">📅 14:34 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125519">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
سفیر چین در تهران: همه طرف ها باید به حقوق مشروع ایران در تنگه هرمز احترام بگذارند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/125519" target="_blank">📅 14:31 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125518">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5580004caa.mp4?token=iIsPFnzsfdEaiAYM_M1BdRGhqvNfSM0htfybL3pax1kApJF-zR5pMFbP2_GSFqa_jnFdPzoQucgY7macsFdU3p9X_EVwcYAMZOLjv7FxCc3KP6ApfAtDMoaNw4QTGahsU1cRuW_7Q0WFn4r8EU0PR2lZp0ZUocAtQW1NgK9nzQ1Q8eWC88Yf8CbU-iQt66aRu-ssTJsOZQlsI3krZ3pOKFfDd_ivK_c08LndjzhiHL_YOzDQBA0aV0r36p7jVnmFmbVGaZ83Fe5wIGTRwtqhXGkaFB5FMNlWe-Ezp7KAkr0iqwfJYw1C5DHOYJvvVTo9b_sOuto_H6YLfSvVBnLzpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5580004caa.mp4?token=iIsPFnzsfdEaiAYM_M1BdRGhqvNfSM0htfybL3pax1kApJF-zR5pMFbP2_GSFqa_jnFdPzoQucgY7macsFdU3p9X_EVwcYAMZOLjv7FxCc3KP6ApfAtDMoaNw4QTGahsU1cRuW_7Q0WFn4r8EU0PR2lZp0ZUocAtQW1NgK9nzQ1Q8eWC88Yf8CbU-iQt66aRu-ssTJsOZQlsI3krZ3pOKFfDd_ivK_c08LndjzhiHL_YOzDQBA0aV0r36p7jVnmFmbVGaZ83Fe5wIGTRwtqhXGkaFB5FMNlWe-Ezp7KAkr0iqwfJYw1C5DHOYJvvVTo9b_sOuto_H6YLfSvVBnLzpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هواشناسی از احتمال بارش باران، رعدوبرق و تگرگ در نوار شمالی کشور خبر داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/125518" target="_blank">📅 14:29 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125517">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
ترامپ به میانجی‌ها گفته ایران باید زود جواب بده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/125517" target="_blank">📅 14:28 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125516">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
غریب آبادی: موضوع رفع تحریم‌ها و مباحث مرتبط با مسائل هسته‌ای در مرحله دوم مذاکرات قرار دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/125516" target="_blank">📅 14:27 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125515">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
فوری / الجزیره: وزیر کشور پاکستان در سفر به ایران حامل پیامی برای رهبر ایران خواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/125515" target="_blank">📅 14:26 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125514">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
احتمال شنیده شدن صدای انفجارهای کنترل شده در بندرعباس به مدت چهار روز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/125514" target="_blank">📅 14:25 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125513">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RZB3HHD2qRUzkJYp2g_cydkLcyLQHGiyIWfxOZUhE6GFmyqzgjZwO4Ofefy3ecSHaoGl_jW831eLSQc6YihaDLWwqAELtkNty3hDwCM0VwGNsD7nXqVb6Jdm30UCLE8L8cUkeA6lvWv-krWd76yB8-mymEv8AYwospXylUWZfAEdz4IpdFSGQOqT4cWl8KgDcFn1UcU0j0TbZXLm9E3Q-1o9lRR_fXgfu6u23ZBpGcu23mg1Sl7VVC9S4p1gnCItcwACAokLfYKOdU8AFqVoanJIYRlBvos55JdMFZTErSLsLzgVkQd3EE2_3uyTWy82egVY36bPAYQEu3x6r4cmsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
الجزیره: نواف سلام، نخست وزیر لبنان با اشاره به اینکه مشکلات مردم جنوب، مشکلات تمام لبنانی ها است، خاطرنشان کرد تا زمانی که این منطقه در معرض تهدید باشد، کشور در ثبات نخواهد بود و دولت از حق لبنان در دفاع از حاکمیت و امنیت خود کوتاه نمی‌آید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/125513" target="_blank">📅 14:25 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125512">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
دبیر انجمن صنفی شرکت‌های حمل‌ونقل ریلی مسافری: ۳۰ درصد قطعات یدکی قطار وارداتی است و دستمزد نیز حدود ۵۸ درصد بالا رفته که افزایش هزینه‌ها را به دنبال دارد. قیمت بلیت قطار در همه مسیرها ۲۱ درصد افزایش داشته و از فردا اعمال می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/125512" target="_blank">📅 14:24 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125509">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/999b104f0a.mp4?token=TYUG3K290Yq7GMWouQ3cpeb7OQ9tiiB6MkUlu4KSKQ2u7qR99F4DNVyCjrGTBh5okPJBfdh-tc1tNWckrJMuPqazMRU92-vewARFhcnzpluomz9Vl7qZ5_0cDGynjIWtoCEL9KRJ2iqAtn4BI_Q6EE3AWrO64kDplr2cLgiZgt9AF4-Tu1J_Tqvu30JkqTSgQemUpfeCwXCNvvyIFSx7AmnsypXTDzmQUuIvTZnjNzg8465iESB2ID1IweYNij4dSu57vh-4zycgnLzHDs6sSl_k7vWce0_tA69xHHfHOJ1rqmHq8VT0QzgGWxZWOOAabi5_774QoismcZ_7C8RKFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/999b104f0a.mp4?token=TYUG3K290Yq7GMWouQ3cpeb7OQ9tiiB6MkUlu4KSKQ2u7qR99F4DNVyCjrGTBh5okPJBfdh-tc1tNWckrJMuPqazMRU92-vewARFhcnzpluomz9Vl7qZ5_0cDGynjIWtoCEL9KRJ2iqAtn4BI_Q6EE3AWrO64kDplr2cLgiZgt9AF4-Tu1J_Tqvu30JkqTSgQemUpfeCwXCNvvyIFSx7AmnsypXTDzmQUuIvTZnjNzg8465iESB2ID1IweYNij4dSu57vh-4zycgnLzHDs6sSl_k7vWce0_tA69xHHfHOJ1rqmHq8VT0QzgGWxZWOOAabi5_774QoismcZ_7C8RKFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
امروز هم در سراسر کشور، دانش آموزا به تأثیر قطعی معدل یازدهم توی کنکور، دست به اعتراض زدن و حتی جمعیت از سه شنبه هم بیشتره.
«خسرو پناه حیا کن، کنکوریو رها کن»
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/125509" target="_blank">📅 14:24 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125508">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hCYNwXUPEFrsV-mKUmeunBkXLyn2BD6COGeWsSqcbE2bHBbPeWEv7IxwJQse7pSK48-NNt4tzw-HryqF0yhbpYm6oqYnRT6YFyp7e6OZTz_L0eQE14hIx4DHGf1X4T8SelDZT3Aa4rSPJBlu3YW75217xmCTM0IqLZnsSi4KBo8DUoUxB_JQOnlzQ-63aCw1We1QsUTXZTzDDUCyh8VRP8cK4z61CEB0XuNSK1rHTvXYm_U1l5qa65zji_udXqQp0el6m-5bLZJG3vRMQqgL3Eg2ICHNzhIzk1Fwysgpe8P7fzlZGAqE6d-MZU9JO87Dw4Kwjy5Aa9zHoOn4u-77uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
داخل امارات یه منطقه ای هست که جزو عمانه و داخل اون منطقه یه منطقه دیگه هست که برای اماراته!
🔴
خاورمیانه همینقدر عجیب غریبه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/125508" target="_blank">📅 14:24 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125507">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3c6f0cb3e.mp4?token=VP5_-yJu6omqOWL44dq1OcHPcex832LmNsjWF1kgWgxgaIMXZ8wOT-hQglvl_M01sLwqZFFh1AWsTwnC5bPrY5SPwv4MMWVsQE2XvPdD1hWS57Orb_DdkFZx6J70TBoT00WmKPAwnS1ID2u2koi5ERY4aWhWBxMFEyeSpf7Ms7T7dECpmHjoS1YnXvzT5Z0bmtSjuOBpoQYX6Y-Hvb9gzmJ_6ew4Hqd6h0u2TCAAimhcEF6tuB6FgWFFFvP1MmI-c0W96f5Jl6ovdOPfZeegbuyUD6xDqVlRcOO5pNRlTF4bly8ywdM5VJS1Hjn55mvJzt2vFBNH3efF420bQbyRCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3c6f0cb3e.mp4?token=VP5_-yJu6omqOWL44dq1OcHPcex832LmNsjWF1kgWgxgaIMXZ8wOT-hQglvl_M01sLwqZFFh1AWsTwnC5bPrY5SPwv4MMWVsQE2XvPdD1hWS57Orb_DdkFZx6J70TBoT00WmKPAwnS1ID2u2koi5ERY4aWhWBxMFEyeSpf7Ms7T7dECpmHjoS1YnXvzT5Z0bmtSjuOBpoQYX6Y-Hvb9gzmJ_6ew4Hqd6h0u2TCAAimhcEF6tuB6FgWFFFvP1MmI-c0W96f5Jl6ovdOPfZeegbuyUD6xDqVlRcOO5pNRlTF4bly8ywdM5VJS1Hjn55mvJzt2vFBNH3efF420bQbyRCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👑
«هویت ایرانی» ما بر روح و‌جان ما حک شده! غیر قابل نابودی است!
🔴
ایران بر همه چیز الویت داره.
🤔
قابل توجه عرزشی حرام زاده که از تخم عرب های سوسمار خور عربستانه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/125507" target="_blank">📅 14:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125506">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97ae3c51ca.mp4?token=DtdrIjabDgGUk1kh8R-CDo7KztuuUMM9dd4F7BYNRCbbuLUm17XjcGi7g8CLG9HR1XF3GK_4cxP244gZScUoeAXqOeizWB3HlFgH8T6db1iuayYLm4vNC_eiXwOXl6dv_nIxGRQ-WZ7vYzVYX-jC0cFBtjirmK_6aKBeQ58r7UghNVw0NgA7x8R3T7zj7w_iObXNZ_7rrpkZ-nXyJ4yd5hXDK4lIYHl1XxNJFAA7lsujEdvsA90pNBzLVD-ol9GwgqoP6caSbLLFXaU-Xy3wjNCREheCALfZZZ7FNNmWh5bmnjIfvS488gMuV6waMJO7YE06HohakHChlKTnlnVeVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97ae3c51ca.mp4?token=DtdrIjabDgGUk1kh8R-CDo7KztuuUMM9dd4F7BYNRCbbuLUm17XjcGi7g8CLG9HR1XF3GK_4cxP244gZScUoeAXqOeizWB3HlFgH8T6db1iuayYLm4vNC_eiXwOXl6dv_nIxGRQ-WZ7vYzVYX-jC0cFBtjirmK_6aKBeQ58r7UghNVw0NgA7x8R3T7zj7w_iObXNZ_7rrpkZ-nXyJ4yd5hXDK4lIYHl1XxNJFAA7lsujEdvsA90pNBzLVD-ol9GwgqoP6caSbLLFXaU-Xy3wjNCREheCALfZZZ7FNNmWh5bmnjIfvS488gMuV6waMJO7YE06HohakHChlKTnlnVeVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صداوسیما: مرکز ناوگان پنجم دریای آمریکا مورد اصابت موشک قرار گرفت؛ نه ببخشید اشتباه شد؛ صدای انفجار در جزیره خارک شنیده شد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/125506" target="_blank">📅 14:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125505">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EWBh0nim5OCrxQMQ5SGICeHaTze5aCp5IJjPmwoKVJXKLQSWNLlnFoIBMTXYx857v0ONeu2DdnFYam_mc7ASbCQMpaCJvqmu4E1MLCaFi6p_8BN8cHcTRwtmUCsEQt91WKZvP3l5MhRp8uyYTGxkIrjk0gW_3hOUkqiAyKub95Wzp65k_tA9y0Jm-nSK6wisP9qGpuscXEx6l-8N89O2xBb-rtktAaq5BVV6uUGp2pHpfSGI8gW0Wno-VgLcT4xoB9lH4pcNz1_nhLH16rRse91BowFHrGNh-DIr7B8fMiK9esa9pRMl_KPXPRV6cZnV6fJBxoVTw9zd3MUPFmTUfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
چند روز پیش گروهی از اتحادیه معلمان مکزیک، ساختمان آموزش پرورش در مکزیکوسیتی را تصرف کردن و خواهان افزایش حقوق شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/125505" target="_blank">📅 14:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125504">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
وزارت دفاع روسیه اعلام کرد که نیروهای ما بر منطقه «شوچنکو» در اطراف خارکیف تسلط پیدا کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/125504" target="_blank">📅 14:02 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125503">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
فارس: ۴۱۷ میلیون متر مکعب آب از افغانستان راهی شمال سیستان و بلوچستان شد؛ یعنی کمتر از نصف حقابه ایران که در سال‌های نرمال آبی پرداخت می‌شود
🔴
فارس نوشت: افغانستان یکی از پرباران‌ترین دوره‌های خود در قرن اخیر را پشت سر می‌گذارد اما تاکنون تنها نیمی از حقابه ایران از رودخانه هیرمند پرداخت شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/125503" target="_blank">📅 13:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125502">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
بحرین: ما مورد حمله ۳ موشک و چندین پهپاد قرار گرفتیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/125502" target="_blank">📅 13:54 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125501">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
وال استریت ژورنال: دادن پول به ایران برای ترامپ خیلی سخت است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/125501" target="_blank">📅 13:45 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125500">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
وزیر آموزش و پرورش: امتحانات پایه‌های یازدهم و دوازدهم نهایی و حضوری برگزار می‌شود
🔴
کاظمی: تلاش می‌کنیم امتحانات از ۱۳ تیر آغاز شود.
🔴
همه ملاحظات لازم برای کاهش نگرانی دانش آموزان و خانواده‌ها رعایت می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/125500" target="_blank">📅 13:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125498">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nY7CBQXMRfxH4OS0a1OSvszIkYs3uMYIsRANNPJRl8kFM-K_TAPW3qTPyMwoJERLDb9G6o08sdj5BynsxJsAvttIISbcAmcOJmzibr8HTw5KKuWE7ZYuRXGGu2WCD5RxHhRsjXLhMB0dESTCwzF_cTYOUQ8lVtPlTp5WTmSeVZ1X7x_WszZY-D3T08-HZcF0aKB3qDL6A6E26yfHkb77t0CSLceht3qWbe8LACxsn_L70gWn-3PyNZrRmxRc9ISqERfZ9eLsfY5iLPj3iFT0BLZ0XVpyqlRnO6tTJIuBb-WDR_WPHIYZjPO0fycqEGb3PBs7QHnGUAwmP4Xe6jXetg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/duyIUOSRefABVJRYEf2DoTzOy7JwIZz8ebz9uVVDj-hwL7CwF5pO5jIR9MIlQCRnjKG0rgHVaHKFxVM7LPTUx4TE9kdLN8ZHbjv76Mkrin2g7_n-55TE8pj-mLg1x3_lyyOhg52bQFv00qj3ot3R46G6mGl1WE2q8u2DBQ-1OqBYwD9hcgJVgm0qjorRN7FobqjVFQASFi74kNwv9_q_Py8FW76B1VqeXtfdqiWTvUhoNBe4SIRja9k0XZAwVbpvRUw8SH0JjHvUFpjqiPa2zR5uiDUyKdNBmBqGuoAeORjyvW0dfAIr7BT_I1b5K0aQl3XfXAp-h8x7ta_7KKhMcw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
آتش سوزی منتسب به اطراف پایگاه هوایی استان شیراز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/125498" target="_blank">📅 13:37 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125497">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
ایرنا: وزیر کشور پاکستان امروز به تهران سفر می کند/وی در قرقیزستان طی روزهای پنجشنبه و جمعه، دو بار با اسکندر مؤمنی همتای ایرانی خود دیدار کرد.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/125497" target="_blank">📅 13:29 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125496">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
الحدث: ایران خواستار مذاکرات سه‌ماهه درباره جزئیات پرونده هسته‌ای است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/125496" target="_blank">📅 13:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125495">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
وزارت امور خارجه کویت : ما حملات مکرر ایران، که آخرین مورد آن امروز صبح رخ داد و نادیده گرفتن خواسته‌های بین‌المللی برای توقف تجاوز بود را محکوم می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/125495" target="_blank">📅 13:15 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125494">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
العربیه : پیام‌های بین آمریکا و ایران از طریق عراقچی و ویتکوف منتقل می‌شود.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/125494" target="_blank">📅 13:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125493">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uS30uptd5TNr6DjqcGycTf_TZQ6dtnNk5czUcMGHiRZ5m8bouat_Ri6R7KX4ymE1CRZCKH05Njy05tuAVDdrMY1Iv5fzYRFo8XguNTPm58UkZ1vtcXJsqgVhp59dsx0HTygx-YNq92wvgmaxc8sKa1qWpvEDjKCjcri0-ZbMABAQbCfwdt0F2u7wK0cnV3UNEukI9mUjGlLrT5LkNejjO3mOHTBUa2dZ1Qc4befl4gSJi38kRFlveEvFUq-iqn10IIb6Yux_NLtbnutmysnTCZmP8eK_BGN9FEtf1BYNdH46mLfFjN2Fdoe6YPw0jim6s704qaFJPT-oAbTvyAfCxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
العربیه
:
پیام‌های بین آمریکا و ایران از طریق عراقچی و ویتکوف منتقل می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/125493" target="_blank">📅 13:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125492">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-text">⚽️
🇺🇸
یک مقام آمریکایی در گفتگو با رسانه اتلتیک گفت:
🔻
ویزای ساعتی بازیکنان ایران و اعضای ضروری کادر فنی این تیم صادر شده است ولی ویزای افرادی که هیچ ارتباطی با ورزش ندارند برای آمریکا صادر نخواهد شد.
🇮🇷
اسامی افراد تیم فوتبال ایران که ایالت متحده آمریکا درخواست ویزایشان را رد کرده:
مهدی تاج - رئیس فدراسیون
مهدی محمدنبی - مدیر تیم
محسن معتمدکیا - مدیررسانه
مهدی خراطی - مدیراجرایی
مسعود اردشیر - عضو اجرایی
مهدی ملک آباد - رئیس حراست
سروش سلماسی- آنالیزور
مهرپویا اسدی - آنالیزور
رضا جاودان- تدارکات
حامد افضلی - بین الملل
سیامک قلیچ‌خانی - رسانه
امید جمالی - رئیس بین‌الملل
🔻
تاج: آمریکا ویزای همه را ندهد، به جام جهانی نمیرویم!
@AloSport</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/125492" target="_blank">📅 13:07 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125491">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
سازمان میادین میوه و تره بار شهرداری تهران: قیمت مرغ تازه در میادین و بازارهای میوه و تره بار، بسته‌بندی کیسه‌ای( پوشش کیسه نایلونی) کیلویی ۳۵۰ هزار تومان است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/125491" target="_blank">📅 13:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125490">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">😍
قبل خرید، رایگان تست کن  ما کیفیتو با حرف ثابت نمیکنیم
😉
با تست رایگان ثابت میکنیم
🔥
@Netaazaadbot  @NetAazaadBOT
🚀
VPN پرسرعت و پایدار
📩
برای دریافت تست داخل کانال عضو شو
😍</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/alonews/125490" target="_blank">📅 12:58 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125489">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WZp3UClv6LnOqX1KXrgq3LafFwwA3X6iTkenqV_rnoBAAJ_oc8NKvcEZSVJSDw9QHVeGHBsmMl25YOWs4RZ53suJmENPy1oeaFWKo1Gno92S_um8JD_f2JomfPF-v2ujWqVrm3X_1Xw1L4jn2iosv5b4sl_KWngPj9hl1urUYD24a8k2yzIehRjdePTWuZyhjvo4RNV8lEGb8it5m8xp4ECaaaBoj_4sN94Cj9pAiE6B9sgav94DT6Zr9NuuqNn3TtabrHAfD_zhGcWLolBSdwch5oiDYcXtolZ_BDRyJmHiWKk1Z-J8tAwOlW4fyHeCoxHo87UQUQNTQINzGtLaHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😍
قبل خرید، رایگان تست کن
ما کیفیتو با حرف ثابت نمیکنیم
😉
با تست رایگان ثابت میکنیم
🔥
@Netaazaadbot
@NetAazaadBOT
🚀
VPN پرسرعت و پایدار
📩
برای دریافت تست داخل کانال عضو شو
😍</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/alonews/125489" target="_blank">📅 12:58 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125488">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
ژوزف عون، رئیس‌جمهور لبنان: هدف قرار دادن یک گشتی از ارتش ما توسط اسرائیل، نقض حاکمیت علیرغم تلاش‌های ما در مذاکرات واشنگتن برای توقف تجاوزات است.
🔴
از جامعه بین‌المللی می‌خواهیم مسئولیت خود را انجام دهد و به تجاوزات اسرائیل پایان داده و احترام به قوانین بین‌المللی را تضمین کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/125488" target="_blank">📅 12:58 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125485">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IvQ4LDVSgYkU7M6Z8nNbKRZgjHALTFwsgLllYI9PWKQvhPpuBAIJSwn0Uf8tSgmVnnLs42gJuIs84hnWEmWv6JQ-ZceYhkkDPRap6LbBo_mzjbPm149Mfly5VijdzHe0VS0Kmht_AD2SyuYKeF30Osk47a5XwMMLV8vKPPszm27pYugfcWLJB8Vi7JovsEWDXxW2_mN7Lx4C5cM-ul_1H5yhai-o1Z_S9qrPEeeVRlRblEyWzcp1yvFVaKDOSwlVNABYWl_Z4lAprmfCTYLAli4Db22vM-bfSdR5HwOf_YI9Vhc4K3MbW7fhBTGGRTEhyjrE1cpHXcrVErC9BhfSbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ofu82RsiyHWkjAFs0n-7qKx7VhmH1rg-IJxwtC2kHXKqDsdX8noFf_AHqhFzWbXNxJTwepTDxG027soUFvIjHoz_k1ICzx6YRh3GWSWPConzmaK13-nnOK43aHHSp-eQ6YSF9XJnBcvjPbTg83xasbUNTn1CjlkTDlJ3EchdpGJCKrEGQDRl-vgoPZjVVw2lHp95GK1izi1ZHjENglL962Hibr9DkhWnYOXEPhZLfzvCwQ15mN6NfIrSwKkFQ8yqVCl_BIeszJ_uBwPbPhG_2X7c0jHS2tYqytE25C30uJ9bgycBlt3gCbkzPesgSDDZ3smMdSWmzjS_0TCsxz_Tzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fd6Agk6KFeYOP9cyCv0VeYmfWtB6cWNccFRGBt3H3AjYAIXOJRsB4vh99e2yB7Z0lUxQSwfQpPuLPEsMbxwb0XGgjR6QO-3Pphsy7lp8UJauA-dmgusWCywmaecBm2wgfrlwrl4G70iwv-MZz-2EbZBayY6KUjbQq6HzF-juZNFEmd7IE7BrzTch8_nCM9CLrJwGmYd0df-rG05iNE2OrNo1gZdFweQfxD-oAXGw-hBUyMhWl5AnE2LcfhoKYSA6twOVX_KTQEXtLc7wha6mWH0Ug7oNkHpM62HLdhxG-IloxQDzOqvaOrEgnGikvhurqtoFFGqbLazA06_QWCcLsQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/125485" target="_blank">📅 12:49 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125484">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
نواف سلام، نخست‌وزیر لبنان: قلب‌های ما با جنوب است و دولت شما از حق لبنان در حاکمیت و امنیت خود دست نخواهد کشید.
🔴
درود بر تمام روستاهای جنوب و به آنان می‌گویم که رنج شما، رنج همه ماست.
🔴
تا زمانی که جنوب تهدید می‌شود، ثباتی در لبنان وجود نخواهد داشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/125484" target="_blank">📅 12:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125483">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
غریب آبادی: آژانس نمی‌تواند از ایران هزینه سیاسی ناامنی ایجادشده توسط متجاوزان را بخواهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/125483" target="_blank">📅 12:45 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125482">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eM6RVDqAU1Mk11_0MIbp_ZRjjkSN5kEpRl3d5lGGsQ6w7ukORdYNij2WC1sphh8q1ASBIs_q3uHsMoyjBRz21Tjuxz2CBIwgfQTO3osRD10HgVk9EvVdPoPfMTee0ERjoRv842xbOUspMnpYUMyKRC5f5qoeF0Kx6TAe3iorUBq6LFJp_aygGN-VrzUc-sbw3lDK0R1BrH0i-4kzsx5BBPyeXxNNCTIf89yDzPpZw0sjfDzttQF_BY5jvZxjHzj5WLGwAHdfkSzY9acmLBKP4_97Its9OTkNQOi1d-s6h1Hl5blBDjUdZccp6fkKBYHOOQzACfzBDGCZ1qgJs6UrDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری که به تازگی در فضای مجازی منتشر شده است/دادخواست مطالبه ۴۱۴ سکه مهریه دو روز بعد از ثبت ازدواج توسط زوجه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/125482" target="_blank">📅 12:45 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125481">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p567qoz4S3LQuyfxmUmZ1w4Pe1A2_arQ1VXRVvJgcamd0dMAKfi7-JLXfG5APnnE92gFT1fGic1NzvuT9eCEplGjnssmCH1cgPcyrSXKZcKvEmhOC1rbljZHVXpo5oB7M393EtYjU3y-_MQYSbbFoM0M_pwbzkomTvyOn3KsSmVlf-Xn8H-hLBPVT-F2_JjHW2lctgu1vZNVWd5HKTGth59Nqf6mGJ6pMi537X_orBCOym68NyGad7n5XsvfHzhyj5tqZYqi4Xgask8zvP225Jd_OtgHb5hgFXHQLPm0Itn7hqhLpmDlNcuNamxgXCfehUVt91IBgHWW3NJ5j-1rUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مشکل جایگزینی پهپادهای منهدم شده آمریکا در جنگ علیه ایران
🔴
ناوگان MQ-9 نیروی هوایی از 165 فروند در آغاز سال 2026 به حدود 135 فروند در حال حاضر کاهش یافته است. طبق اعلام فرمانده سنتکام، این پهپاد در جنگ اخیر علیه ایران شاکله اصلی حملات علیه ایران بوده و بیش از 4 هزار عملیات شناسایی و رزمی انجام داده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/125481" target="_blank">📅 12:44 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125480">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q7KxYVJ9_JAuOsdhgU_h5xfB5gQ2o3t9KLEHmAVLiHSopKQn6oJsEWErMuXBIN6cKdfRlpusRpgq3WPmKAyD3Spu2m5y0jiBoztQuXikOlZmw64W7LVAfmas_IffhZOxAYxqYIAX7IVuK_2kJgwYkuGiG23ej8Yq7O1cSjrOtMl8Pw9xawaHwzzj7GJEFREJYfk0WopLBWKakCbBXsHSijFqE01xcQV0fOrFJ5CuuZeo17cFplSCXjb4idnmFeYFNc-C4AzTiTbSCb2sQwKilMNSaG39Pb9i2B0RrKAI5dSv6mc3hgIyBtGSLErAmPxuVXJD2CumNdnDm6Gro6mrpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رشد ۳۲ هزار واحدی شاخص بورس
🔴
شاخص کل بورس با رشد ۳۲ هزار واحدی در پایان معاملات امروز به ۴ میلیون و ۳۹۱ هزار واحد رسید.
🔴
شاخص کل (هم وزن): ۱۱ هزار واحد مثبت
🔴
ارزش معاملات: ۲۰۷۵۰۰ میلیارد تومان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/125480" target="_blank">📅 12:43 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125479">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/082a0108d0.mp4?token=cBe7iTVb2qfFwxe6e89LodmUvPh6pxeS0sGThhIr8K1vlWg4JEgV55fbocbcmZ-lM9XzWYn8cYSu-rZ8bMrUrAmzpPCdZca_G259T5QOQzd3xOfpgQi0TIekc1cJRMa3wFui_laNCOgIs8FSVtyc8-ib8O02UTmv4aZcpEPtsjotBt0BR0xgTnrnP7MKW5laqtobdbfGLZNX0PuftO0eQH__FLvV_fFoYuvodq8UNi3cItAOT0atvlWdPVX9_0zgUojKsYmxYtah7ERKjubYPr7mLWRBa_KsMv7OPRPy9JIUQBX_AnFXahI0nSlguHZlXU5KFzKey_t8evlBS6JZ7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/082a0108d0.mp4?token=cBe7iTVb2qfFwxe6e89LodmUvPh6pxeS0sGThhIr8K1vlWg4JEgV55fbocbcmZ-lM9XzWYn8cYSu-rZ8bMrUrAmzpPCdZca_G259T5QOQzd3xOfpgQi0TIekc1cJRMa3wFui_laNCOgIs8FSVtyc8-ib8O02UTmv4aZcpEPtsjotBt0BR0xgTnrnP7MKW5laqtobdbfGLZNX0PuftO0eQH__FLvV_fFoYuvodq8UNi3cItAOT0atvlWdPVX9_0zgUojKsYmxYtah7ERKjubYPr7mLWRBa_KsMv7OPRPy9JIUQBX_AnFXahI0nSlguHZlXU5KFzKey_t8evlBS6JZ7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
پیش بینی های درست تاریخ
🔴
نسل 57 چون زندگیشون تامین بود و نگران آیندشون نبودن ،دنبال یکی میگشتن که بگه بعد مرگتون من بهشت براتون می‌سازم.
🤔
یه مشت حرام زاده سکان کشور رو گرفتن که به این روز افتادیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/125479" target="_blank">📅 12:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125478">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
غریب‌آبادی، معاون وزیر خارجه ایران :
آژانس اگه روی بعضی سایت‌های هسته‌ای نظارت نداره، به‌خاطر حملات نظامیه، نه اینکه ایران همکاری نکرده باشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/125478" target="_blank">📅 12:24 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125477">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/niKtpSayHrxzMvrIqqbmgMKtYVfXdXdOuYctXsoOc4g26GZY2Eho42zAvnufOjSzE6kxHLXkpMIxUQM44QexS0XaethIH77WDfJG1TvN6SicfGvXeycQjTGucY5CPNM1rXNRXwocar69IZEk6k59MI3EwbeFipQizkDLxA5N6lGxl8lJq7aNJ-DfLbbvKKAhEK9KRG8m7Ylyvlt0CTs2xuVJFmiJ1lzTIc1YZuWfECVuF6NVuSbQgJ3BrrUCjRTgLS-wvPW3tEQzjjBASkmERWdgWTLa11irYO4l6ue8LlpgD_H4mthonzTDyN80KwGxgqQ0PiLAxRurFoIkt7yVcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسرائیل یک سرتیپ ارتش لبنان و دیگر پرسنل را در حمله‌ای ترور در جاده خاردالی-نبطیه هدف قرار داده است.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/125477" target="_blank">📅 12:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125476">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
ایرنا: وزیر کشور پاکستان امروز به تهران سفر می کند/وی در قرقیزستان طی روزهای پنجشنبه و جمعه، دو بار با اسکندر مؤمنی همتای ایرانی خود دیدار کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/125476" target="_blank">📅 12:20 · 16 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
