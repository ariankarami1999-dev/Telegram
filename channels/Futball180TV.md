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
<img src="https://cdn5.telesco.pe/file/lKncEe7zBz7hl2UtJeuPpgnKfuCPXOwvPTzoD0p5IjFq_XCbCXF3ItbfU-zhpyNq1VYevMMacTHrKPV-IBEasGUU9c7oPmmEN5c8vlECoEuB6Xi59ViWFUrTMnXAb7RdruTqKGleeFoMlIHUSOyjv4MO_ffBvFJtxmsUq_yZXD9SoTs3kqLxi9mYM1VK15cd3GMddzAx0yG_B35h0QgFOd0zcucmXMJlfBF81guHVdob8vnnbZL-mGNV6HTpXe2LkXo0zdp-MbJpkc3SkCcCJ8mdu-hKTAob4OZGjS_OfiL4IEiVZNx3lpPJvl1azLkBEWAaSG2pefYKXa6n3EP-aQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 522K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-05 20:45:13</div>
<hr>

<div class="tg-post" id="msg-102091">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZhcB9WE-W_-6ybd_nOwmeBA4C2JqGv8tzmRoHY1UkgZPRGRwYG8PmV7v1o3ElAqEGRW9hLLTYyPv9z7dJj7Qjt2d6Qea7zBQP4pus8imlGx6EtBzH65jdS10PxerdKlMQgLvuwD7vWFxLXrQMu_Vnz2VLF-3wt_HqqZVpof_OjHGtgpKzwC_Mw_G7heWjESKv3hggi1XtMRwnKBeliFidULWPSwPqwNpI_TgHCZFu3P7OEI_yajU31KLxry1diM4UHdKOjpcwKmHrgnSFG_e_xo7Ueno0iGfQojGDyuf8xvwH2Cp7qC2cGyYPVXucJ-iU_Ru4b-eEVE0jvyW6idLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🇮🇹
فابریزیو رومانو: پائولو مالدینی و لئوناردو از سمت‌های خود به عنوان مدیر فنی و مشاور در فدراسیون فوتبال ایتالیا استعفا دادند.
❌
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/Futball180TV/102091" target="_blank">📅 20:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102087">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BEWTo3NM6WoKMVaB7-V02yR4uYUmmA83gSaZbx3nnbb5sXWskAL_QHouS61sg7krnybGkRdQrdcLLQHku7Bd1RKZGI_qx_LI1iGVZNOl46830Rf8CGZhiVwToZaPokA6NlBC7CjuaUQtsr3HuciyyX8Pkle3HlACjc2wcSsl5J1yyYKveduXLsWHvO5PMHMPt55qg2rW09I5t2EtZuV-sBFcOarBaXrBLQSgeqPI-MzXnNd2p7dvO0XxAZfC6Tw8GFrqpGfSJ7Mwh-hHhTq8bjqXD5rbje1g21AJw1kizhrPaIEU8_woTh3XVpRDuTA6rj5ODJbbMjSZ_0wPMsmGaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dnu-JOERf7PjaUTIG0kaE5tfHOOAyFEiIKI3m2egDRWSqDnm8VFTKMJVRODTmbkNHUFV7qBDLwF10c2mf90K3iUk2gQq94DnMyCaQr6SCDMN6rVwyNFKkzukTogZZyMReALRk8GcIYHbrTm9kcsVO7spW9esfp-TVh3rQnv2O9zXDg5ExdB2_g4C9XmCjdCujkIJWQ8fJYhMT6Rb-UX5MmZycJ69ACeKMcSgRTNkWufedpu1Hr2VGmDYkKEUJouj_SDPgoEnRglwTb-ECxJjlcIWdIoUyV7OVn0615faUs9HzYUvK9IDgLrPayhfoeb0nxKTRYsfgnV-E213DaODiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MbB8yRwn7hytYAYdczDSMLH4o26_b2obI01nd1CH8fSPFN7oBCDvMCezK3rVbXeApfcl_g-2Dyg43YuXkilhobHX3aPPo0Ytm8WmG4hkEhtkDNG1rJ4yQxbHgago3P7x9Bin49Yx_cnqSxQkwCB8kz99GNe5aTP4Ut1zRi51MPEmHE1JIP1jocPm5VIREYb9-un9cgTvvWusQFD9ZZhUAGuyy1flJzxJSlEjosTvCWqlckEcT7gvDlp09DhRcvpSx3y016VLR0FYXeSHPcojkUiIsPF2fMgR6_mTQYgR1pEo1HIJZv0Yb6D_vJ-ARifjkxtzudPqTOzKEgU9f2CTng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sjbNAPQeFj--i2Y5rCXYf0uihH2yGe_Qpn7ANUjDcRT0AgpVhqLFFxZFRf4aFlOSXvTvDz0_Yu7PTwWaMU0Zpa3Zml9TO9Z5rQrArhGxwsoLdwRPAPYW5UwwE3hB4YuraJehBXBbaNptGC_IrPbxwm_fHHfolIkvAr_cciw9D__KDijeZSf4gv2fES-KeIM0igK-e9YFnBdw0hjwsw-xTgfI5eC_ry1l54vnulyPtwibHFd-HYMC4S7kQg2hTSEvQNhu3AjuYhCfqGiYKF9YIrtub75_gkj-a10nl-edYk4RHsiczDSxfirQpjuTRu5-I8cp08EsJRnRlKxPt_6kTw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عشق و‌ حال وینیسیوس تو‌ جامائیکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/Futball180TV/102087" target="_blank">📅 20:31 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102086">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tVrJ8-aq1pyQFk_g7_eEVU9rQ4Nzt1kQkMz1TR8n6grFFIt068Ig02rD2UbXEUwWwdYr7OFSHe-lgDtYvVHm7PljbS4Qk5sXJfQeiJMEr1AdzjAkZuJabNLwZIOoPn-ZgL46ki4j3Dp1Z4jhPqIGrAgVPa6bbZmdeMY4C3NmkZrZm8GPdb5MigvGbQmYh01p3CyuIuEInOMRjKvhmy8gDU6ye1GVPtChM921n_wJvGcB4blBBDlpEms0OtcYHL-4y5iEc5_fraH7jGdGL802GTxyhAV6eedNppzZc-zif0tpNdT1OmTbtPIlJ8G6IYNFhSfdWgbXkcYLlWn1GZTHAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇷
گلوبو برزیل:
سانتوس قصدی برای تمدید قرارداد با نیمار نداره و این بازیکن در دسامبر جدا میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/Futball180TV/102086" target="_blank">📅 20:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102084">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oWHam_NetwC-s1mGyBF2DzN-NLqZgmBoO_yCoRUcGiwkcAq69vNj7O0q_z6KERzCc3pfwoRyneassThyjjXvJmxnPbsGn_zh6ffb3xZIniVO9ljRTUFNAL_QC4CiwzpBdc9Ead4zjwIrjl-Ten3oG17oddLMtzw9MBRv8t7u691xSaKy1doKIFP4Lpp3AEn0Tkaa2KI61hFgCfQimDrB1LsYwxyKZFkJ8P-wpvEpVXSZT38Z5dxdBnmoiueVjuooA_hrq68rzt24kKOSuxPMV3GPjawfVMnVyk21kYABVGeGVreVOTREZQ28nfp3MTSzZxLPDJSTtX9mmj1RbBup9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LBL75KG8JpU6hE0f1JJxiJjb1kdc5pvWRgnb4ViIP9k5P44oSqsZUDkIdyFm4VcELMUY4FV3VcIel_4VxHB1RR8u2wVOlYGfsIWT9cpiPXjuyJF1xCB4CHMkWCESeeu1Ks1go526cfgnqqZZSAdV-M1EUrd16aQhlms2koMt9HZSbOM6g7jI_45AKlk1guvOnxU9JMEa0V897doZRylJwXLjlk6W8noYZbQbypCiGrMWapZBSqmPn5vBotpVISZij5v4vkV_8SU7TlXPXsWQyM_NX8NJBhCzHKsF_0i_--IzuZtjTDN4AdwZq5KhPB8r_0k7QCWgwj1f0D1gdRQGJg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
اشرف حکیمی درباره شایعه معروف طلاقش گفت:
اینکه همه اموالم به اسم مادرم بود، هیچ ربطی به ازدواجم نداشت. از ۱۸ سالگی که فوتبالیست شدم، مادرم همیشه مسئول مدیریت پول‌ها و دارایی‌هایم بوده، چون کاملاً به او اعتماد داشتم. حتی الان هم قبل از هر خرید یا تصمیم مالی مهم با او مشورت می‌کنم و این روند از همان اول همین‌طور بوده، نه اینکه بعد از ازدواج یا برای فرار از تقسیم اموال اتفاق افتاده باشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/Futball180TV/102084" target="_blank">📅 20:13 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102083">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IgtSL0WLvMQSg0lxmyyuLbQifxL9SXDjROYRyBrARLeZNpz8Twte4wJBzSRU6Zm7b8IyEZrCKp4_KaUTHm4lEmtzs2WKEoAKkuE066KfNH8wzdo_OUqgbTPCEn-L5RRoFJa8OhAw8QHMIyn9wrAyA20iCeQmk1QAgcOZ9rb3cMc9fLEBKCtYq6l9ZldjXDx4f6y-woqWQdQVVzBMIkVyVt4djRGkT3tMaQjV9gAk5io6SU8jPnjVG8iNk3JlyARD_wCapfK2KWmSQry32NSd7-FRHmmjnr-UGsyIeNYJ-Z8xZW1IPfqUQwG7lAyoRsB1V0O1UF3DYNv0OFbQv3hgKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
⚽️
امار سه فصل اخیر جونیور کروپی که ظاهرا گزینه دوم بارسلونا در پست مهاجمه
جونیور کروپی ۲۰ ساله متولد فرانسه ، پا راست . پست اصلی پشت مهاجم ، مهاجم نوک هم میتونه بازی کنه.
💸
ارزش ترنسفرمارکت ۵۰ میلیون یورو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/Futball180TV/102083" target="_blank">📅 19:56 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102082">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QdHG2lJTESeRDGSnFr0Fghgst4M0yjENYMN-NwMnPY59nuBQY-mP1XXCtdwYoYLCbaluSTH0P4yspzeyeC_jEA9v0kNVMiGem-YbawMHkuLHPDB3xZTg5xdUW9hnPz8LNx6Um1nfuz1g9dw3nOxyegJSOvnMUcGjDJcsfWDsGp0fDd3xrOMvoyayqVApJSLji-O7CuzpTUaPBpgSJhPJ5UAKttHiLhv9nmXf0Rrbcv0NxTf1MvzVIiaEe1MIS3OLr0xQkacz80otnqSq28hRGXlMmHMAkfUOCVDrGI1Xa0P44KqEsBcO6IaLDlRLvgIsWB1GncogBRG4Rofca2YIgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
قدرتمندترین باشگاه های جهان از نگاه اوپتا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/Futball180TV/102082" target="_blank">📅 19:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102081">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e948c535d5.mp4?token=PQYBlOVv5FVbRxT4VK9cbvr8mL22fodY4Qs5cuic0X-yCcvJNn5RilOCFUmlqwg-USnqvnEmpG4gyUE3OD61KXtKYQO-RkrPTtO7_CyvYmaLwy-qrcGOvRX71Fo-nnZYjXK5hzlSRAnKcM-3usKx8qVfsYJBKy70Em9BHubBXQrSSFL9Z17q4CsPepBx7s3vQ7mCT-zkBAKy3zupshg-1PDxnpkaXT3xM1ykaW5TmapshEhxYLgk_8sWIHwCuOHowY5svB9SEimEpSL5qzavZDLl5jOs7mda35_8DbnE_hqtl58QX5eW-S5fN2wi2BJUjtWQZch-tkIPP-l7LCKm9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e948c535d5.mp4?token=PQYBlOVv5FVbRxT4VK9cbvr8mL22fodY4Qs5cuic0X-yCcvJNn5RilOCFUmlqwg-USnqvnEmpG4gyUE3OD61KXtKYQO-RkrPTtO7_CyvYmaLwy-qrcGOvRX71Fo-nnZYjXK5hzlSRAnKcM-3usKx8qVfsYJBKy70Em9BHubBXQrSSFL9Z17q4CsPepBx7s3vQ7mCT-zkBAKy3zupshg-1PDxnpkaXT3xM1ykaW5TmapshEhxYLgk_8sWIHwCuOHowY5svB9SEimEpSL5qzavZDLl5jOs7mda35_8DbnE_hqtl58QX5eW-S5fN2wi2BJUjtWQZch-tkIPP-l7LCKm9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داستان کریر سرمربیگری دلافوئنته
از اخراج تو تیم دسته سومی‌ تا قهرمانی جهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/Futball180TV/102081" target="_blank">📅 19:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102080">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
فوری ترامپ: به درخواست واسطه‌ها ما در حال انجام مذاکرات فشرده‌ای هستیم. اگر این مذاکرات موفقیت‌آمیز نباشند، به اقدامات نظامی قوی بازخواهیم گشت. ایران فرصت کمی برای توافق دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/102080" target="_blank">📅 18:49 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102079">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D7ooaVI_DvXbplMBM_mWIcSUaU5gp70ZrlGnwfejtpS3aK7AXhdlkoqIjZA5G6EpWHLT87iTRchVuHWurSY5KS-zAHwkynxPDzQsTT50lxCFUhzciut0Lu5135VCbMqFtNnDjX7h87VKefvmutT325_oJAeKgOUJd0UQImuNLZN_emiLSuYRVq1zc5bTt1VsiizA4ITp7lPzJB068tvnKqzmdOic4hZL1BaMvFSqfBP1_9jV0JKvzM_mfLu4uEINk6WYofq0L3lMIGvT-Z0Ust71L8k55HdCBU7MF9Hj5k1YNbKJdOSgzVyD_vgdxXdg9bPvjG6-ZH4g2SLrCsVjkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
👀
چند ماه پیش الچیرینگیتو توییت زده بود بارسا به بازیکن های بالا نیاز داره، و حالا همه این بازیکنا رفتن رئال!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/102079" target="_blank">📅 18:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102078">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ru09_HfwE2SPkORjfDJSIa6ce_MJooCx5CijpBlTU0ZHmOCjLcYmEYnOkI_kZZQHvUdI7SFWTDoJCQo3VE08ae-UU8t0ADsHcYp3K_G2aO44KECshjiJSgTFm396yIukUVv1o2KDqRUu-iSGt1paqiri-Z_sUm5-ockCsHsEABPRXh04GtsdiJV85LNcJ2JdezcTaj2T-QbvKwvVYcd1CHM3tgh8DMLaFaKjaiFLJdt6POkNPGDO15SQShh6EJAEj_SfIzwAg1KDrG8emK9N2l4_J0nCa5vRAx5DWCsNFIe-q0b1gyfPFlfx296hza_hlmlk1t1TsuqbfvxWSmO3yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
امباپه:
ازم میپرسن ممکنه یه روز سرمربی شم؟ نه فکر نکنم، من تو تجارت مهارت بالایی دارم و میخوام که تاجر بشم البته بچه‌های تیم میگن تو میتونی برای ریاست جمهوری کاندید بشی ولی باید بهش فکر کنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/102078" target="_blank">📅 18:13 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102077">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M-kaq3X8DHKyHrA40cN3pXJsY5ko5nSUGUi9gCNpWgOSY-VL6A5nKjPCm9jcO_f6hq14bgKIUAt8PdZ1nsKUranF5Hr720D-8dg8GtBogKM0mqtWhX9oqAEsTOM3hqhU3ObtaxoI69wDapLLlJcRtmE6zaw6Qdvdcbqen43ysxkw-q-XvARaLSA7jKMSYpCb2A2X0lGxXUT8uSh6yIKOeGsTanaKlC8sP7mR_H8J-MRZKi6yVLlIGsqPm_Ad-9V9PBdv4I-7tagLf1GsW_cdeaNb0IWUh_z025yLsKJQp-wVi4N5U3FHkTlTUb3S9QVMPqte-M2luEeg03DD8cN9Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بی‌بی‌سی اسپورت
:
یک قانون جدید در فوتبال انگلیس در مورد مصدومیت‌های دروازه‌بان‌ها اعمال خواهد شد.
اگر داور اجازه دهد که کادر پزشکی وارد زمین بازی شود تا به دروازه‌بان مصدوم رسیدگی کند، مربی تیم 10 ثانیه فرصت خواهد داشت تا یک بازیکن از بازیکنان حاضر در زمین را انتخاب کند تا به مدت یک دقیقه از زمین خارج شود.
در صورتی که هیچ بازیکنی در طول 10 ثانیه انتخاب نشود، به طور خودکار کاپیتان تیم به مدت یک دقیقه (خروج موقت از زمین) انتخاب خواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/102077" target="_blank">📅 18:07 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102076">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fLE5THPEjNFzyS6MBdKuXMoI0IFxLaDkEBYUnVobhk0DaUKXD_OPLlUUnYHEII95mMPEuZG7ulQP9rks7s3oQCs8QJpyEb9_jHEF72_z8-eirWjHDPJ5UGKYRqFBIwEiKDAlpSrAUPHAfQ0g0izkt6tbAGqZwHY_PdIZAN29QtZ-B1OWOFQh1dLFnRJmkJCgj_Z5VPdoTI7JdsgYXKGckvAYUtLgl0paYSg3JjU4QNJpJfq4VEmne9J1g5c2YZ_rPPxdymQs6cEceE4G-v1px-0-i_Q8LCN7804MusPbsBdlT_Nf8Ib3hgLBLwQDnbTyKOlLX0DLJ8mKN3M4Sbhnaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🗞
فابریزیو رومانو:
‼️
بارسلونا با افراد نزدیک به کروپی وارد مذاکره شده.
⚠️
بارسلونا با بورنموث تماس گرفته تا درباره امکان جذب کروپی پرس‌وجو کنه. بارسا یه سری اطلاعات درباره شرایط بازیکن جمع کرده و چند تماس هم داشته تا وضعیتش رو بهتر بررسی کنه. کروپی بازیکنیه که داخل باشگاه بارسلونا خیلی مورد توجه قرار گرفته.
❌
البته این انتقال خیلی پیچیده‌ست؛ چون بورنموث نمی‌خواد تابستون امسال بازیکن رو بفروشه و منچسترسیتی هم بهش علاقه نشون داده. بنابراین، این معامله اصلا آسون نیست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/102076" target="_blank">📅 17:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102075">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n7hT0ZAEGd1c_n6nEFg8KbNNdbX8FQOX6mEO3aMRH9PnZ0qybs1GOk15C3s5-BHW9FO_5evC8hAoyVtkamftKJkK6tXdJs-O-Uev_FVsRHo_DPZVVWZVYI7GxxMSkanf5Vw8uTQcSBcIYopvQF1nB-BJU7gv1mqLIbms3ZTC49mHKJkc3OSZ9sTHIyHtyNP943FnL3VbXzNFtg9osSclqNN_UH0WqM0tFBQA2cgjWrJo73pjc5_wLlgHyyu0noXoldD99NItxI_31XwVlvuXctpiUhJpbs-GWL_DYJk4N3lmNyuPWdacFgGBo32LlG3d7Sq88CccluDBGyAZDn1zLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
فرانس فوتبال اعلام کرده که بردن توپ طلا حتی بدون کسب یک جام بزرگ تیمی هم امکان‌پذیره.
📊
این اتفاق برای این بازیکنان افتاده:
🔺
جورج وه‌آ در سال ۱۹۹۵
🔥
🔺
لوئیس فیگو در سال ۲۰۰۰
🔥
🔺
کریستیانو رونالدو در سال ۲۰۱۳
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/102075" target="_blank">📅 17:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102074">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/czCXJ5f93YtMacoNjSm-GhMLzXLbzFewc8I0jdf4mkFTQxxgFycrXrj6KoqnqRYBE7SPsOQAECgY5-wEI39DY4iwMIhYCWPqrCK8TNqbx5QtJnvdZ1tCH6jF95p2xEwn6W17-PM8S-z7ZZd6RbUaMJepjdLqodPx8pygbz-WHhGTpttLNZaffrc-OvsMtY6VuZSLL_U53CGJ6VAYpapbkdWXDKlw9cZkL549WEjz7tOcZeOcmP0BzE6cG8khjnVTrI_T0PdOu4sCoJWN98j5zPJWWexiB5a3gBf5QR0ZDe1Ph9aN9by37kvRqZg_dgzWXCm3JeCmUXWDm9VTMK6moA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فابریزیو رومانو:
یوونتوس و پاری سن ژرمن در حال مذاکره با سوزوکی دروازه بان ژاپن هستند.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/102074" target="_blank">📅 17:07 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102072">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nm6Igoe33qI_V3q03ogwEOWM5hwbKN6mSFLe4pvbYhYf4aiCEuJ9GzB6sAHojQ3U-QHy0ZuVfiGjLY-C1izF6AUuui6DIFjkNtjODxHZO0R9RC-eyR6m2alrUJ26mON6pRYdc8ytsJ4kK_jQd5wvAP17CcExk_MaW434dsWEMxAmPG_HxkJjlVqnKr90UlyL_A_7NBZZ86v-HR9SxJuSEyfKiXxvPDNxnf-KRPvK4niviJBGM85Hg6ZqgvSHdxifUiPQqD_lOYw-oAIql0P18_dbRu0RogJKW81Hf4-o1FRa0GPhH6ODAKyVuSiL3u3DKhUM-7LwzGSH3mlCqtqR2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qdANBG0UT5YHhq_refDmi7hg_DbiNfRTqZPssIOELD5rlsSlJPFdoIw4gSvmgWsRnopNEAWNrpgJQ8T3eLkfN9ys6OsfWWNemJTd2GPUkCRbPqxZcPO3xFMtyc10xVSxv-8hxdLwa5h27j4yq417K4oVlF8tLk9wJ6IZ8LJwVUm6pJafufmA5TGevCA4-MPEg5j2wJuFRJhuCsHBjK3VjAquHQiayRiBtM7rAwIbf8BhNKDSpGq_eX13oxPUELAgo-bs8VbhaEzhO9HHWyhpdZpaPCibeWhacC-hzso3qnGQ3P6iP2RNKLsExK0XHJ07zgkVmiIpWsPtDjgdoDAExQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
اشرف حکیمی درباره بهترین خاطره دوران کودکی‌اش:
روزی که رئال مادرید با من تماس گرفت و من را برای تست دعوت کرد. آن روز بهترین خاطره دوران کودکی‌ام بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/102072" target="_blank">📅 17:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102071">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vy2JL5U7tDdGJ429KDWQN6otYVponUOQsSSt4YFQDa3WMOjQesB6O3QFKo75Pl81T2Vy4stjr6wtQLcCqmMfsibqIRNQiL2e41glUtvyL4y4VbYP58weK_Mbtp0oITBmBrnjqPcBzfNKeCmTWoP-l1xxDPuY8Gnhz11Obti-CFeznb2eBylt5RHERAeINU8C5tegaouWMCIi0uUGzPsl78DkfZefC5SVfF2WmAn1E8pqqA2a8dSz-aqUCsY_f-TIrxHLOVLqzBaEJByk8NoyEz0oShxeSkySE4vqR-L7RH__WNgnjj2D5aFF6f8DGSQAPaakwicVMoFxr3BkheWGMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حضور دیومانده در تمرینات لایپزیش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/102071" target="_blank">📅 16:26 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102070">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3120e668b.mp4?token=uJAshLxpo0CB0Lqi8t-WZjdtnrpuymJ7VkejC-ADSXTK2A-r3A-K_Ba33itwbzku1XfU42XsAljq6cCdeHt4dT2WBzqJgyvncRtHPQuTDyIaAQWEKudix1o9mCOs2pdQsSgvylb8VyO7_Yw8DZLbcVRfAt7OFdR77U5j5ZZRCMSmRlggaoTGLSz96Ld2FMccEazcJaK0Oq52A8NcWw0H8U3sGQpN8Jdpt54gAjtP7xsiYlpXhkBZolPf7zFNl_D_Lu0X-B3IjJb-XQXOPuUXNBCGNKclaEGyvXQ_Chj15DPjfLbmpHExaZ7Rtd-hNXbfA5hfNM6GBozOatCYnYBwOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3120e668b.mp4?token=uJAshLxpo0CB0Lqi8t-WZjdtnrpuymJ7VkejC-ADSXTK2A-r3A-K_Ba33itwbzku1XfU42XsAljq6cCdeHt4dT2WBzqJgyvncRtHPQuTDyIaAQWEKudix1o9mCOs2pdQsSgvylb8VyO7_Yw8DZLbcVRfAt7OFdR77U5j5ZZRCMSmRlggaoTGLSz96Ld2FMccEazcJaK0Oq52A8NcWw0H8U3sGQpN8Jdpt54gAjtP7xsiYlpXhkBZolPf7zFNl_D_Lu0X-B3IjJb-XQXOPuUXNBCGNKclaEGyvXQ_Chj15DPjfLbmpHExaZ7Rtd-hNXbfA5hfNM6GBozOatCYnYBwOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
عاشقانه‌های رونالدو و زیدش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/102070" target="_blank">📅 16:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102067">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/orUoyUrhagI10YDYWkyYeyQMy0kGQj3JrY7QTNQcyFVnEdRXezLAoe-Qlxr3KNqhjG4OBO9U5jl80Q0arc3_7CB06Eswpr0FZqeGRnjdcw_avDn1p_a1TEQoio0yq0yVeed068kW4oZYmJKj7Um4U2Oq0hBmMSmTWjkAgckyCsLpvm0RLZ8zXY5GgkmSjPkywXSnQ3QlcdZEihnYq0H_tDuwaSmnAA7-F5Ry1rprmFu0Ro6IHkQLz7lM0_p-Dxo1q0qVHPkwtYUxpLbtK1DFMspu44SSZNvL1eNS_Cm3xQBBZ124VLWsyHYWILx9qTmUB2SXrSys3X0i_pDiV2QsTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hz0DKsiVEbL-yb0JqYu3W4rWGK5xEjTRd5cyhUGbvHDXivqXiaFYxgZ3BXDKE_WKWZd_44ugE-aHwK3kpt9IlI2JuvexxCpnBFhz9NpQsFFci__hn1pSLcHtbvLqndhS_tWumEigkJM785xzz7eZni0uFB36vihBTPs8Mjq8p_NPN8M2q-_5lLy1ttjeZ2LJ1AOJRccTrQi0TrY90Uq5XhLFIi1QK00Z0vTxAyCq3aWlgLn_hLHhqbp3lg42_CHA6V3AgkQw7JD0L95qOMgiJR2QMa3bErIW_DgTBNts4vQqORYVFVBfd36deefieQkf6cUgCtVyl33fyw6XScEyhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A4D4XFOCDkFaGoVzJOqYAKtBUsi4pFNlCASqCmqlUqtZvFOngq5M33H7ZWE-Uu6wGnBtJB8aevnQYIcbYPzYKXDTghTMccZkEEuo9SZBKoaEazaVvEwE1pt-5afNaLGwIRdQnytryqka0WJFidRF21qZQrGYgp6_-JJjOR6YMyj18e-1uFBCo4sbKrbmuIetiG9s4TFpPDdv_eYJrBYb5JTesIheLMmv41cZEAgICGrxJes6OI9dDpKmPk_tfeRhKXmLSVG5qNj88kcVpKi5eUa2w8j7IOvuqyxmtU3aavJjHQRen5Kav049cV_E5n4Y7Kh5irTiPNVzJL5IIOYIRg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ایشون که تو تصویر میبینید مارتینا گونزالس دفاع 18 ساله بارسلونا هستن؛ حالا هی برید پیگیر یامال و رافینیا باشید درحالیکه اصل داستان جای دیگست..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/102067" target="_blank">📅 15:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102066">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
‼️
انتقاد شدید امیرحسین صادقی از مجری خانم شبکه دو سیما بابت انتقاد از قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/102066" target="_blank">📅 15:04 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102065">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f32263398.mp4?token=H2_Q_-EuvdZbJwsLT8pf8Ag-5pgq3jNQs3stmOK0Bb9iYsJ8x6gRzyukvbOrakh3fyYll7SDZGpUwqVYPX_S6nJDPM-CSDiEAmu6XT_8HDhLC86AOcLeLGk_ZB1evlFoYFTbFWEINsMw6fOpaoBsfm0KIRBJHl59mbidcMLjLCxx5lIgJ0JEEAj4Lceqki1NT-qdrdOeu6OojUp9vVsg1Mu4C5iKMJGGgToSl84dGBNBgmKl-hCPqHlI12SMUyGzgFqWizYzJ6e6DdeRvu1or1L6DT3Y4tgCr4Ya9Y9qHltE7ahhNf4Lx8v2xHh6NMM3qZfg6khB2NymEKkZiIbFJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f32263398.mp4?token=H2_Q_-EuvdZbJwsLT8pf8Ag-5pgq3jNQs3stmOK0Bb9iYsJ8x6gRzyukvbOrakh3fyYll7SDZGpUwqVYPX_S6nJDPM-CSDiEAmu6XT_8HDhLC86AOcLeLGk_ZB1evlFoYFTbFWEINsMw6fOpaoBsfm0KIRBJHl59mbidcMLjLCxx5lIgJ0JEEAj4Lceqki1NT-qdrdOeu6OojUp9vVsg1Mu4C5iKMJGGgToSl84dGBNBgmKl-hCPqHlI12SMUyGzgFqWizYzJ6e6DdeRvu1or1L6DT3Y4tgCr4Ya9Y9qHltE7ahhNf4Lx8v2xHh6NMM3qZfg6khB2NymEKkZiIbFJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غزاله اکرمی بازیگر: رضا عنایتی کراش دوران نوجوانی‌ام بود
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/102065" target="_blank">📅 14:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102064">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lwl5GwU2_WPSyeLM1apW0RGYIAmjIzoaG4Y9cZECh5E8YhcZu2p_QJAwTHIefPEpGo93op2Y7ttC3Hjm7PJvTlo8PTEFT6fa7XkTXkBYkROryu5e7EHHSnrHA2G0XykKfv5iqQv-5_5s9rZ56B-aU7xvHiTWfU1vUte6m3ODBacuijZlYY1raeMXkU_Xy3kUcJ5GjEimO7KwJXH0Yzfh3Xqm62odUxpbX1GAhniR385L6ngj6a_KZpqEfOzthSCSzjoh5PvtUpzxoLM2FFt4vWL1l8nUA67zsgjgST0XmoCq3liUepDph3WatTu6QqW5qYxmPEqAmhHaBXioEP0i-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فوری از رودرا (ESPN): رئال مادرید نسبت به احتمال جذب رودری خوش‌بین‌تر شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/102064" target="_blank">📅 14:47 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102063">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sQUrjA11MZubmEyqcAn4iqMlwLNQvajPRbX9M_V7uKDvWYXrwECak709F4RRs0vntqirshjMv3V2OcMjQa2cvJGxJeKipBYXEdNA6dJSkmy0RP6-iIYJXmV2uCzrNEKCB189WM7_-FcS5w0NeUeo9tQ8zQebRmlq90c4KcvkdzVCnT5CgiGp15Uryn3uhGJMhbs76AJA4tw4FvJwCicuZCzjiwyEYO3H7aF034MWpsT8vdfdNR7UAuhSLXl2qutA96yT5SgUe_lXxo9ZOW2KzgglrDMrtZ_TmMw9VtdZCe9_MQsn1VDQQR5Ougj6OrBi-S55pM4nQYcmEjruynG2jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
اسم کوکوریا تو لیست رئال  برای لالیگا ثبت شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/102063" target="_blank">📅 14:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102062">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sChJWF5oIqWhzwWNzfmoEAPh0zNCaca8H2dbM9QBESmABJVxkZlWLKFD-FtaWuTvmUeoNUG4zRx4oOlVMmUpX49nhFcTk3DqAR0SvAnJxmdZUCWb20-rhQTf-V8oft7SFWCL2_AZjGjqLp-_XZAkEQj6iGdg7A8v_-mmyCoIJsbKM2_IjZSTBRQm_yNpRMus1qnrlIjCX6FfdYatryUaWDSWwyxvMV9rIfftolJKGtke87OvNdR7CE54OlPNmizb76Pz5SnSK9G5A1SCyNqnPOSeGEhVX29zcZM5UMXXr39km8oSvZ0IPIbVjEaZfCSXoqByPKu19NKUdBV1qaxpYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
👀
مقایسه عملکرد نیمار و امباپه و هری‌کین در بازی‌های ملی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/102062" target="_blank">📅 14:03 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102061">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2084d796e5.mp4?token=Ppuw877SF89XUEkTsp5yrY81aPaMBifrt8rHcuxvTZp3r0UXwvxpiMfSZ6GMHhKGbM-95C1ekuse2FkHvBSbLe-NmQg8zV15Q1dgPtzIMvDDETN1zKhRPSBoWu9MePSRSbA8LmP2ciIe_H8BWEPql_PHNcj9jrc5tolXgHoeoDCmdY6st-TDGaOabJ8CcbSk-ubkecZhkLbBKCKMn0IRCdwmL8R8QXSFSWuyQyW2n8go1wu4IX6nV2Ux2oJZ8QMQKG0jsh5tD5ODYKvqaSInrELeEUdzKYYSCZTAuhX4PLuTyigECPVRsY5kSA0yBzR9LCuloNgDotolULFo3_RIzr1iVg1LCexEeKwlQx75jeezp0PgLPyVJDchwNJpR1sxYPmBe1_ZXTMZL9MRx9UH2D_AyLD4zYYrBDZTkNH2-b2MO6hJmngRZfMBL-9NIMHmqJ9mk08VaUoO0Opr5JkJE0fBxrnWYfgw-_NRTQqxC_gDHxV4a2-Afzlo6RAOjAyP0vKa21rdQRtZVmhk1O7ZvT7kf6DZqNGVbUQf6kta0nBlIUzlCN7luIX1ZB0I0aS-3T_dvHaTfGhxDtWLz56MpMhg65_77SOayEK8tYK7kBnRT0FWpary8MBBqjv1XdI5hIffOZXdnmSTUNRQQ0BL-_M11XHMkEttMYyqPsfMEYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2084d796e5.mp4?token=Ppuw877SF89XUEkTsp5yrY81aPaMBifrt8rHcuxvTZp3r0UXwvxpiMfSZ6GMHhKGbM-95C1ekuse2FkHvBSbLe-NmQg8zV15Q1dgPtzIMvDDETN1zKhRPSBoWu9MePSRSbA8LmP2ciIe_H8BWEPql_PHNcj9jrc5tolXgHoeoDCmdY6st-TDGaOabJ8CcbSk-ubkecZhkLbBKCKMn0IRCdwmL8R8QXSFSWuyQyW2n8go1wu4IX6nV2Ux2oJZ8QMQKG0jsh5tD5ODYKvqaSInrELeEUdzKYYSCZTAuhX4PLuTyigECPVRsY5kSA0yBzR9LCuloNgDotolULFo3_RIzr1iVg1LCexEeKwlQx75jeezp0PgLPyVJDchwNJpR1sxYPmBe1_ZXTMZL9MRx9UH2D_AyLD4zYYrBDZTkNH2-b2MO6hJmngRZfMBL-9NIMHmqJ9mk08VaUoO0Opr5JkJE0fBxrnWYfgw-_NRTQqxC_gDHxV4a2-Afzlo6RAOjAyP0vKa21rdQRtZVmhk1O7ZvT7kf6DZqNGVbUQf6kta0nBlIUzlCN7luIX1ZB0I0aS-3T_dvHaTfGhxDtWLz56MpMhg65_77SOayEK8tYK7kBnRT0FWpary8MBBqjv1XdI5hIffOZXdnmSTUNRQQ0BL-_M11XHMkEttMYyqPsfMEYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
درخشش‌های فصل‌گذشته لامین‌یامال در بارسا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/102061" target="_blank">📅 14:03 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102060">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ap50rvTiVleX_PK6zusjXmdq49VexkkU5OWO2dnuv22MO0cBJ3Ka8ylrKSOytsrgmyxFTAIp12qZmQZMB9An6q5Ul9Dh2TV6F151hmdgHOIhTZuqR-EvcJ6SxiT4LKPDv3iPFwhz5GV9LZIBpcXrmTXwXAviJN6At4KBmv0hZocs9zHZg6kr68JislmNj_j8hsk545cLGuCu8bnUwvJILihN5oDddnW57UkThFIs1BCLsdVMwlzGPAY-01i2dz8wwPWa5MMVJo08mAmWgwlbtmKAUy5zhF8Ybel3gtYFoolnRG7WFJLQzF8AGSm1KTN-f7nZth_fw5TsS5Is4SJyIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽
لیست بارسلونا برای سفر به انگلیس برای پیش فصل با حضور ترشتگن و دیونگ.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/102060" target="_blank">📅 13:38 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102058">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pLipo37XpQRJjMrnscnAYXoqEfri71pujDL5k7G6bl76kaqnvqlgACOqEYvfRbwBVHteqZirmXB053r1AaW2MPROLO9F60BSBzP677rU1X2kdbqyfqswCMFSSjDmLTjE3ONt4kQQIe_fWsBqNZ7XIoBLe9pqV2ld_i9ULo12ECr7lOGT3WgmY66ntFrxJ5glanmx3z1tebaAK4srROS9HRc060ropQRHNUQm2nPkseHBq5cWIA5T_P6kNCTrbewPlrwZ3fBrhXw30H4H9TccqgNyZnxW5DBrZRfrK04AYCnaXYy45pp01qDYwCSH-HhQ6EubzqrGhtWa3CwUgzcu3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/olfgU8RdiVcLsHfeiGMsAO7ClXoANC8-2Xranav4Wgk18KM5UfNlFBHX7Habs8zabT2ETZpab2eQIwVWKO2W1YOwl9-LJslyRgpp3PCUB5wINz0S4WirdASasMNUWnxBr-BmQ4raXwgxlerM_mrUsnFC2ZaKcJhYWBMgqBgG6RGtnxeHnwMCfIzYI_xxmkTlAkoaPLwLLLz8CksXCGEgfWEnnjTXnVyLN8tt_V8EueOCJxdbFt5xj6wMzbKs6f2at1jcUszFw1cfB9053c1LXatw3tz4kEslnAIxyPzxhptFQ9BnwPtfw9HBC_CxOWUcMGRK4ocYZ6EcTITxlavl9A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
نیمار:
وقتی در پاری‌سن‌ژرمن بودیم، از مسی خواستم پنالتی‌ها را بزند، اما او گفت: "نه، من برای این کار اینجا نیستم. یا خودت بزن یا بده به امباپه." او حتی برای هیچ‌چیز هم بحث و جدل نمی‌کند. آدمی فوق‌العاده آرام و صلح‌طلب است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/102058" target="_blank">📅 13:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102057">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/772e430691.mp4?token=oMz0AeB5Iq5BtLiMfpuZ20Lf4WlKK3QxdsYL2PNQ0tbSpT_eqwibMuq43uySvg9LZHLCfwtFmpWYSzZVrge-e39OhKdEy0Xj3eczbe6AcW1mPTZoeFiMrxeIc0NnpRH6rJ0_GBHJ8L9cJTduzNJWLXuIB-t28yR9dtHFaGfcX3RRTZ7I1eGAEm0geZrBl11MVNa1sc-wQPOxQuwN8NAfZYWitvoNDBV53BWsS1EECr0KdA7fM69kx7EVCTip1D0rU6izSI4dTw6K513qODtlKcOQ2QfzKTjzs--oE9-zkNEk_MBIjRAI2KM9dpkqR4y5ghRKWDet54sfUFmckOXu-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/772e430691.mp4?token=oMz0AeB5Iq5BtLiMfpuZ20Lf4WlKK3QxdsYL2PNQ0tbSpT_eqwibMuq43uySvg9LZHLCfwtFmpWYSzZVrge-e39OhKdEy0Xj3eczbe6AcW1mPTZoeFiMrxeIc0NnpRH6rJ0_GBHJ8L9cJTduzNJWLXuIB-t28yR9dtHFaGfcX3RRTZ7I1eGAEm0geZrBl11MVNa1sc-wQPOxQuwN8NAfZYWitvoNDBV53BWsS1EECr0KdA7fM69kx7EVCTip1D0rU6izSI4dTw6K513qODtlKcOQ2QfzKTjzs--oE9-zkNEk_MBIjRAI2KM9dpkqR4y5ghRKWDet54sfUFmckOXu-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این جامی که داری میرینی توش آرزوی خیلیاس پسر جان نکن
🌟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/102057" target="_blank">📅 12:52 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102056">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qwtbYgdT2wmo10EvZmvSzTFc5VYiGOa-4uS6QONHfn8upRb8smCIJRVWXFQJdcB1XfaF16rUOTKsF4zm994BxmKveuORph0AjRGikt2nJOI87Q63k4S3axcSX_LeOFcoAWUHpAKvbfinCA9ENUwhqXafkYTrARVGfhYu8qbfSgzOeamoXnZcZN4nuTLNyva3uhOqHNe2NvPxlsZRJZ0Me7YGInLvWqThKMsuERAEk0XUktx5tdP6SC_Du1dzmSHKKxKlyvCDXH1Ju9mgW9SnISlnCZe5jFe51Sgl2EXTLX2fottxBtRnocnIdlDeDDk5p0n7F4yIoKJkQMf1J3vI8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇦🇷
بنر هوادارای بوکاجونیورز برای تیم ملی آرژانتین:
ممنون بابت تمام این شادی‌ ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/102056" target="_blank">📅 12:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102055">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
فابریزیو رومانو:
🇮🇹
✅
پائولو مالدینی، به عنوان مدیر فنی جدید تیم ملی ایتالیا انتخاب شد.  HEREEE WEEE GO
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/102055" target="_blank">📅 12:38 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102054">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ebffP0JjbQ747RbG-W2N4qx4aM0NvdWinoQ9a73MUpQrrkYp-F26pbxoL4SDUJcm0zY69_-qjm4dlhodKuADiW5M99KatHxU_Nl6Ags-bj1_UE3YFosDU8ytZcOk_rzj2OLeGjRZMPktl-xYnvWSvk0FTfh6DZAtPYVx66D3dBDu6ZA5vbCQ4QxBd50stJB3EhNH2xVLy9QUXjPbKBL-5LpjnE1gM6kOUgK7i39hdohPdCibVCM1N2gvgnQ47rNv5Z6X3N4SlZIzcF2QsmC6C_k-JrCElmU1dF_52x6Cpzq3u03u5F7nn0gtScnkFwXSOZy5U1WC00oNCO_5b9q5EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
الهلال به کریم بنزما پیشنهاد داده بود که به هر باشگاهی در لیگ عربستان که میخواهد برود. اما بنزما این پیشنهاد را رد کرد. این مهاجم کاملا روشن کرده که هیچ قصدی برای ترک باشگاه ندارد و این خود الهلال است که می‌خواهد او را کنار بگذارد. در واکنش به این شرایط، بنزما خواستار نامه فسخ قراردادش و همچنین پرداخت کامل ۱۰۰٪ حقوق باقی‌مانده‌اش طبق قرارداد شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102054" target="_blank">📅 12:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102053">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ChWiwSNlUgBsASpCasJpnNAivaqFAflA6zuiz-x7oZGxmXGn8Hf3mzDtZH5B8qZMnN_ysCGgPWD-IMdpLYIcIrWt9YCA8VeiW6TMGR4pmN7Bki_QPeEGp1wD99WfoeUB4784yl2cvm4wTp0JPe4Y9E4RgR0OHIu4JAUkd-Q95GhoCxlNWa1-fpXFtDV_HLKKkmOHCSUa0NC_DhrNaEEAtwzg2ewNO97BCjUf99d6jrBHSfGk1IO_iHbU5ZCOwBhGbhkHwjGf2Y8YVUUW6ET9MuRS9pG6C6q_cT_7MjmhWHsZ7zvVivSg4Kd4WG_ydzLaC02lP_tANHKeu2TNr59X9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
جورجینا رودریگز درباره اولین دیدارش با کریستیانو رونالدو:
قد بلندش، بدنش و زیبایی‌اش توجه من را جلب کرد. جلوی او می‌لرزیدم، اما یک جرقه بین ما شکل گرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102053" target="_blank">📅 11:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102052">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WCE4XnxmTAfNmJ5hRr6W3ajuo-_PnjnLMuEFzwhnqAE7HlLSdxcLYYAh2kQDHRLhTwO5NglIBF6_irEhvU4zzxFmyIbWt9L6MCB9S985e2Di5VTLUhgtxQLPQHXvhnNcWRA78RVWNb-VayM0GKQt9p5eCfJwtElfLfsjFErWa512ticBcJvaVhZTzVV2eQM678eJ-O-CsxWw_TAsRWkXMJRSMW_A-ftVPKSMgoQjO1oV9ns-5ndHXKKQu1kAWEZoKJxNm0vwF7Rh5TLFsnh8ZLl3FSjU-DgLLUwy2sNi1k540PhWGGfJXaTidFWmJp3VXiyOvtq_S8ioTo9WD7Tadw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برناردو سیلوا و ژائو نوس به همراه زیدیاشون تو مراسم عروسی گونزالو راموس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/102052" target="_blank">📅 11:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102051">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/809e9f523f.mp4?token=VouvFJkG23N0HP8tXpaFKUxovjucc050dS3Ddoy7Xri8O4Og9PduEjRwzRrmRIQOQWtF2tuNXkm0km5Qfpu5gJfcayO2jOzsHjp899Sy_jYxLgUyrdLcUfjMEIInQFEKWIf6GKKy6f-IQ5YN2Lk5qknaaQBTSsFndN5HN7fMassbxDdf2X2IeBmnCyiQNnZP0tBziDaPiiltG4rSCzQBoYtVpdn-7d2C5x-WLdyBuU5gvgUWUVBNWA9hGWkT7wq-zX-HQ29toHb3xEJu-id9UaIvjkjaNss9sH21Lfh0uBw1gUWobFM8upBbbXpB_RyALX9D_44zRLgOP7MRPjwipQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/809e9f523f.mp4?token=VouvFJkG23N0HP8tXpaFKUxovjucc050dS3Ddoy7Xri8O4Og9PduEjRwzRrmRIQOQWtF2tuNXkm0km5Qfpu5gJfcayO2jOzsHjp899Sy_jYxLgUyrdLcUfjMEIInQFEKWIf6GKKy6f-IQ5YN2Lk5qknaaQBTSsFndN5HN7fMassbxDdf2X2IeBmnCyiQNnZP0tBziDaPiiltG4rSCzQBoYtVpdn-7d2C5x-WLdyBuU5gvgUWUVBNWA9hGWkT7wq-zX-HQ29toHb3xEJu-id9UaIvjkjaNss9sH21Lfh0uBw1gUWobFM8upBbbXpB_RyALX9D_44zRLgOP7MRPjwipQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📆
🇧🇷
۱۵ سال از روزی که نیمار این گلو زد و پوشکاش گرفت گذشت:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/102051" target="_blank">📅 11:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102050">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qfPw_DakiWIuYvgkhOksj-Eu4GrKo0CO1SaCccJc-PMsWUeRcnYHBKlL7vCWJRycWgTBj_HENipSrXXBVd143vflM0Lsqbfr6k1h12TJJ9jE-B2CvzEwgqbfdmvp_CkPjSYVzvMAIJBkUulkQ7OqbSE52s4TBDM8ou4TzhUGUNgatP8PdyzFLl_GD3tclTPzZJpsE1gO65O_D3qiNgq4wqzQLdvBWGq4Z0kB2nrpnkKIQ3YlGotOzYq7aC0QHFDWgc783ez7MKMxq-7CObBVeKGz28J0fr0F-ITSaGUpuRZMyMQr9SXkYSUwIlXjZ2K_RcFPd8zgEOHbXN1OjLwOlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
فابریزیو رومانو:
منچسترسیتی مذاکراتشو با باشگاه لیل برای جذب ایوب بوعدی ادامه میده. مذاکرات با باشگاه و بازیکن همچنان ادامه داره و تصمیم‌گیری در مورد انتقال او، یا در حال حاضر یا در تابستان سال 2027 انجام میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/102050" target="_blank">📅 10:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102048">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ie5Uc4jlmGlSqTlO8QPQ2aCpq9qzLSDENCQjm57D5-B1FjT8hxiNl6LRNPoOxMRDOrxMm0gjynQ1ySGYioupVhXhLFohmD8H-OkYGwphfWGUPmtIzai5Sa9XizlIrhplULpAUsn-PqFKB9luL9eMtWGOpkmbZWkbRmG8JFmyJ3lCISIeYFB8wTtqH7b7kcfd9gZ1y9dnCAUaNmobLJIc_hX1kJT0Bcip7YZhIeNM2UohRsFTol4ECRJ12kxELcP9uMblqOx2MnqB0nllEUYC9fJX0eYzi54pI5qwQP8KHMNBx7vesL1Qhc4CNKbyJhtLisZodzXXlBThReafjmNk4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U5K9UsvBOEJm_xOFDpseRXn35KjlBbJYm0xq3a9dDPyFr3xmIqjzHbIwiHnWFbVA5hEANki65U1E28ywVRVju9VytZGhKnuVpzQxLiov9niHwoOaborVfVhSadf-iwCSWXUc1FLVki5xTRWnQsb9Hthn3s9AuuQJf5vwjE6KGw4nDgWwyuDtWGRbjlwfF3_D8kDo_IcB_sfxsS0FwLn67YeU6vURPjLmQsFy-xZdqgou7ORDtrFm-Alngk70d_K8LZ_TNZHKMJLSeJiKAM5maDuIo84oTKK9dX1kcR2ydzgn_DXTcmKv_YkB2L4ThQtEoExavQpkl-bza6lIYuDLuQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جورجینا و پسرخونده‌ش که حسابی باهم گلف بازی میکنن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/102048" target="_blank">📅 10:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102047">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FZq4GPifQ83R8SDEnhmqHe7hV3WNVwnqn286fZ1rZoEUOmqEckNJWZ3zPSSDCc_RoJdM7HdoNZmYV3pluFZazIlGAWXQqcwxsg1s0RQC5PeQG66yGHqpm9NejS9hAsHO_8kHd_FwO_xhF5C1dHEq7cr3AQLNo19UVardKnqkPfOFf3XLcOQvhwOmdPwj1Mgcak9G71AT0cYEDQqHPSTs2815IQW8Qt_oYIQJr79SxPJjEB2VBWUHkBe-N-BsfDJjq-aawJPjecWl70WIOBk-_kLQ4h8fFfEIhRYxX1A7J-KK0k-ptoVE1bxsqECIzWHrh2Osex95sl6ELnMW_QgMWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
الیور کان در مورد کلوپ و تیم ملی آلمان:
شخصا فکر نمیکنم کار در تیم ملی به آن سادگی که خیلی‌ها تصور می‌کنند باشد. من معتقدم مشکلات خیلی عمیق‌تر هستند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102047" target="_blank">📅 10:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102046">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MV50iwe06tVwV_Y3wtKxEd9oSEqCh21VediSr16G8WLyXw4XERdh2f-bow2e5b7uwMD20g-pe7g4BWPXmoq2xshYGJuJG0_FMdlAO30STRz3-5cBwYTagu6muo8x6rG8qMVnWFXBwxfLFTgd9WVXxqDr7fnp0MgkA3vgHM0uApE2R4QHwXML3kUMycH48HNbbBVbKwvx3jg66_96XQQbjmoP-M8ojRLmNEF7DTxI2LXyf5DyNMgqvH457f19LNxtNGbgwCzTF9BWdKNMMZ8cKEyiN8K04oa7C-Fj1udGlpLF63YQ59-pOx5NDrJYesriyZS8shPo0hGfd6Tz5AapAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔴
وینیسیوس جونیور فصل گذشته ۱۴ گل و پاس گل بیشتر از هر مهاجم آرسنال ثبت کرد. او می‌تواند خط حمله قهرمان پریمیرلیگ را فورا یک سطح بالاتر ببرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/102046" target="_blank">📅 10:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102045">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OQ19ttLEK6pG9hIvCKqn4agJrRNORHih7x0Rvc6f8Mcg7PGSl3uO8NjBdZTzeoc_Hdddg-7JuEO23zWJj0IiEvL6e3nv9o3sfWPaWYs-lYk1crfh8Stg3xI1EmXE95eJz0ZKu_DCkZ2w09W8DI7si_I80FANAQgfkUa5vRdaM8S9Hg4IRXbNcsQo85bwAcKgIfaweQPaLr8-CrMcE6ed73sAnkxY3lazFWP_MjesO02WU4tXCdOJYyc-e0FKIvmern4QzZQy_ZUFQgjtDTQuhh2e9TMLylA19X-4a8mPRcboKjeKfmI_X68tnp3hGLth3SfShoXBID6zncUlDrx4tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فابریزیو رومانو: پاریسن ژرمن تلاش میکنه بین رودری و رئال مادرید مشکل به وجود بیاره
‼️
🔺
🔻
پاریس از هایجک شدن دیومانده بسیار عصبانیه برا همین با رودری تماس گرفته تا اوضاع رو برای رئال مادرید سخت تر کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/102045" target="_blank">📅 09:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102043">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zo71YSJ0eRLykuaF_PA7fsLFVFbcydYQYghizCJbqyYSG5JnvMoYsdceGLnCKnJZM2EXfNownDXwDa5dzx_DvHe5mZBBTmagG9kTuz9VTZeQniRP9pKgeDti0pbg9hSqHAYKN23KdfjgX_SGdKX463MdwuazC0n2J-RR6Ih5VU4kOPmixGtDtcvt9G__sMPckEDHTjjnZOJqommmCgjPVfYLhXyCeN5rC4Je-8Z9LBnwoXj8wa-8vGWz04U4JhamF7TmEO7Y2fBMATtVekdD0SqOeEUgZVfIMAY5P1AY5M95uv0PqGFm-IH7uLVTf3yraIaer14_ljDW35tQRgdQ9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d3eF6WFMF5xi0w_zhtXcUp5TZLps2j76hX_Ab8Mw-HI5llfFe3WE7qr5Nck6OSQ3ltqlcsQk2_qwsDpSsRpq7RUI3pyi_sas24BoW2zFVBEEuTOXxLJBtt0Tf2oYKhg4rBIUJnRGKcwjvis2bgmWWd-TWnAgxP1Tkxnt6HoJ4OaN5zmWK1epZNyA65GO0TMcwII2vS00aizyvEd892nOwTtHb7Qn59pq3dmxx-tRhDQJ3BfQTvl-vJRB1kHLZ_b6k3XfYXN4q308JSKa8-5OfknDoRHavrxJqRfTCeC4jhEyOeXJxNmbjGOk1rnVIC7IDoyTr90CCUYv7qGxOuzLKQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
👀
طبق گزارش رسانه‌های برزیلی؛ نیمار بدون اجازه، کمپ تمرینی سانتوس را ترک کرد و بعد از برگشت هم در تمرینات تیم شرکت نکرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/102043" target="_blank">📅 09:31 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102042">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VTt9dokoU-A02FqQrxqvVgDT9QXIggcdmC4zGnXQ9v6BvTjbG9AD4ZokiPz7MFHsKtczKYDHnb0fGv7SXXHX-9nTXtQRMw914RBbwv4yGXBKBprxY9-t1qoq10S7-G01BI5zmVmtXk0q2E3aW9vAzPF0tyeJHcKTW-3p_QJkCL8DhUU_fhr-D1vF6eyKLfOviSmp6wUgoaGeKbTLY1M1J-nfBSXRH6mrQ4-FQBNmpsz3S0Wj5Wm-rz2JQ1oihU0gPzFh4mEtumQpqcS_B9ATRFD1Y7US3VKIhY1Iyj0Cw8hBWcdKnZ7RGaRPR4r5CpirXT0nSRCgSJKQZXfo3npz1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نیکولا شیرا:
رئال مادرید آماده ارائه اولین پیشنهاد به منچسترسیتی برای جذب رودری است.  ارزش اولیه پیشنهاد بین ۵۰ تا ۶۰ میلیون یورو.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/102042" target="_blank">📅 09:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102041">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fWgI6838P4f6mKZen73HzrvaS2x2vlkXfTjc_OHuA_VL1Eo4_eK_kT4IzyOt_-r2jlzid3GBf_IesQtggV_6wNxmFSyGGej-wVihsGEaONk9VKA5c72Ig9t8Wa8XpYvW9V3Y1nAvFYTr66LQBijO-QjgFa87ep6_Yn0GYrUMj8hiFryEFbLtDLbIR939KBkoZyL1GIdj15wVtK4xJ2AJslJTir-MZigrT67HRh58ramzBwPn7B63c23H1eo4bGZ4o0A7Gk02UbUIxBlAL8L9tpyKozcBPrCcDNWtiHlP8u8LsGVuJpwD2IdqQ2cTeuibKQqUH3Sy48UcY1fKNEhYLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
⚠️
اوه‌اوه یکی جلو فلوریان پلتنبرگ رو بگیره که ریده به سر تا پای رومانو:  حالا که ما را "دروغگو" نامیدید، شما خط قرمز را رد کردید. شما فقط یک روز پس از آن، انتقال رسمی لوزانو به آینتراخت فرانکفورت را اعلام کردید، و با این فرض که هواداران شما احمق هستند،…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/102041" target="_blank">📅 04:53 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102040">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_rim_tIw7z1kYxLoiS_qn_rW94bK0XBuMMDpNcRigaatQZpHzC3vth5ojZnH_gDRzfO0fZtG2pRepMRfxjaP52h-JTc7iMb4LVz2rKpnN9UVGRAeqzuRvnS9L6bGqCyu8GKsP67sr0ipeE-hlIwJ08zO8-b3V1hVvIEJlKubbrYe_TAvtL_bNbYGPOQisSfNQSwViIekgM_WqC7WDa7iKE6nSLEkGjgctXuQcq5A8AwJaU1CeCypKR_QQxBJe-A-osOKoV4P53XF-Qbx4AfkrFSbnocSc3Wpc18O1QBDpOFmil6arkHpZb7inEnzKhTkoQVuJAZ3hf3h8mihU0S7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
❌
🇮🇹
#فوووووری؛ حضور پیرلو به عنوان سرمربی تیم‌ملی ایتالیا بدلیل فعالیت‌های شرط‌بندی وی منتفی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/102040" target="_blank">📅 02:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102039">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EyTThOG9AwDcsmyGYI8cbp3HOj7S_f2Ica6cCQWgEKoKg-klmCACPfVus6Eu8qACVZDDKoMApbU5dGGkyFyLCyzuwR3_ZAjZYkGM694hDFHKffAkQpU06LJIh2MeJJmPfiarH_XjIEkNFDTHw0gwAa62ks-aBqw8wxmwgW7JrEe0hNhYz-TFkUG4Yspbse8fMVzxli2nVHmzbXNDmZbafr8X1UzBbc_vTF8MPQ7i59OGk0FriQFZguj7mt2VlbgSafTuOUC9-JyYbctn3enrG89ztpiD-c0rVh3z9f13XUtdDKbrsjUfBbp0iLQ3MACyKYAjxohxjyXKguCG6gYpMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
❌
🇮🇹
#فوووووری
؛ حضور پیرلو به عنوان سرمربی تیم‌ملی ایتالیا بدلیل فعالیت‌های شرط‌بندی وی منتفی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/102039" target="_blank">📅 02:03 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102038">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cWrrbqIYE468t1YJSj3UJjIkHjAGt6cc4J-wcAZqLBCpI6FiTXHn0-nh2_PTRlCpvzAUNSi_B5bBYR85zXKeK-EctyWcrcevL5g_5UV5bm-Ki1F8Vx1cCuM-EKUEo4hjdvsB_MgTrpwNevQ6AQ9B1uJN-i-d1MOw_evAHPNwtPJu4JPHDQf6ypVN1h3CHCCo56syXvBXH8fkaFlBv541rTp-F_yzfFnql9z72--mS2deWDrw9VVv8FtJz2B0mFMqIJi3fo1XhSccQWqoHy3Zsv4dIpsYHVM5Cw5RkWhzcuGCeDiRU0Qa7Ukl4WWIdmq1NkbJWfI3o6xOsqbcyhjXEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
ماستانتاتو بازیکن آرژانتینی رئال‌مادرید قراره به صورت قرضی راهی بنفیکا بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/102038" target="_blank">📅 02:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102037">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gHSE_uSbXQJUmobBU3rS5zgiXprMdXlMlbGGln-i13oZls9utDWbc6i4GICoCc3nfuTwDbr14dc-61TYyWNKpQD25_XtO0Lr_VEqyYe_Q5uQqw5AUKCp5tZPwsKVWo_D28P1qlvq2QSCuTf3nPj22VVmERGuu6q8clyQ5xlxBNIT8Bdf6xTorBZBxwiLFm9G69eRc8dAd89Powz1RluWx8qTYOLgXgBHkEDvWPTonBz7qEcJB_wU-sbf7oFHFAfbGiC7WOr6HxRqqe8F59rXbjLmV6YKb89Xr7t-0mSQ0VUXgTor4OXmeYhArISuoPCagkHU-2Y_52PjfnZPbFNLBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
جنگ بین خبرنگاران مطرح فوتبال اروپا بالا گرفته به طوری که دیوید اورنشتین گفته پیشنهاد رئال‌مادرید هنوز مورد موافقت لایپزیگ قرار نگرفته و نیاز به زمان داره و به نوعی گفته رومانو فعلا زر مفت زده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/102037" target="_blank">📅 01:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102036">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BHGS0dIk0Tt3jkiGkavzl-oADm2Zua7i9p1pdLmmHfEgVdnlfcHyp20uPJoTesdyJ2-27xaaYjPtGhynG22T__9zRAsVvNFVSm0O-I_9YE1TOhtim-HLv24YKi5HVTvzuXLK_gtnfHL-nxmwA7DpzaVh3Z49plZmgQ9a68yd11s4p-GXTtBjzkhLi82Ugh5Ke3gl81uO0WJmrAAR5auNzETkdkLWGnQ1IyrrA0At2aM6Jbx21kekVnMc_6Amhl_hy4d0PyS5BRpakhusdE87iAlBhA9n0B7Ek2rhRp8mpCpAcDpP0LAyZqgp6AW0NqmbqYQg2Sy2qLsNESVZgFHtDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
سرخیو والنتین خبرنگار فوتبال اروپا: ژوزه مورینیو به کاماوینگا گفته که فرصت بازی زیادی در فصل‌آینده نداره و بهتره به فکر تیم دیگه‌ای باشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/102036" target="_blank">📅 01:16 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102035">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Huz5GJJLSV8Ax8Hzqo-0NWAEdYPo3x0A0ecxDZUVqMDLqQyhhkQ1vtOHFukXkikf1CkeHmD2eaMQKJzyoenjrduOMFePFwQW97ccrpAWtHVRjZuD9jxRHq2lhDndvPxh6YiCmaaDs3pA38Hq95kT4iMVZoVrd1f16cODH6s5IdDjUZGEqo53n4Dy_had-8Q1fKRGaa8DnpuLzJLjUrCVW4X4fbfcjoA_Uo6uw6_bc4updS9bYVw-7a8vyDcAgUMAnThIZqsHPQKAuzpXusvuHCbNosavJ37tEC1EHUADrqh7w0U20Sbfg4f94sBUQ9YphLRlwiYnQMKgVveG5SpT5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
💣
💣
#فوریییییی از رومانو:
🇨🇮
⚪️
یان دیومانده از لایپزیگ به رئال مادرید پیوست. 𝑯𝑬𝑹𝑬 𝑾𝑬 𝑮𝑶!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/102035" target="_blank">📅 01:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102034">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fa8UvnkUF_f01vHrldLAh4E4VdD3JzARKGXGz3RFKzsPpcM1eX2eUfoKVH8VljRLfWZ4tSQbj1YIJiEH4F__W9PC-gKkJz7qWc7rPP2EFV-iZyk9ihqLHvI8AsJtS5GUKpDCg8yMRHxgAwPHtyoJcn8O-WtdbzdMpLA9_TK4MTkQMX7kcne9Xma0iL8cetXtNFyiXqHbjX5y1y5oDfqSXn3J0rVcVw17afAQetE2rlK3W_Dbh1eJARXGuuV3QtS_nXCTHFuripIW-qmwDz5dKcO0b8zoELd09PlpYZnAZo23J1Hm7FH9UjvUwcySP-fBDdNf7OUlR9d5AACi6ekJ1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
تلگراف:
مدیرای آرسنال معتقدن وینیسیوس جونیور همون بازیکنیه که میتونن باهاش چمپیونزلیگ بگیرن و هرچی واسش خرج کنن ارزش داره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/102034" target="_blank">📅 00:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102033">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fda4a57b7.mp4?token=EtXiPOLft1nrldRd2vwmqejQ7dGMuSUShujyNG1y2cOH6sQFxtht0Q8OAnnruVwTAUDk9GhdmH87iSgo1aZNzAqgqIxadZ5-_9yt4b6vdqywh2LdO4k8Snhgmc7lycWYoODZGGCbSmPzM74nY6iv4VSgGtbqd3Eyj_trNh87xjZpApkiiqTEJpftT1g-djtUJKyLje2ta2RnXHkoAq7NBRvasAc3FyUaw2C23AEqP2WcPBa0y6OWZQ3PxezKiv5nlNl5vLx7x8gz-F3DQzFQuk5yvEUhUJayZmlCk2HwmjE8GJ0yhn27znOJcffl9me_-QljtJ0E88sj3JR8_XHFRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fda4a57b7.mp4?token=EtXiPOLft1nrldRd2vwmqejQ7dGMuSUShujyNG1y2cOH6sQFxtht0Q8OAnnruVwTAUDk9GhdmH87iSgo1aZNzAqgqIxadZ5-_9yt4b6vdqywh2LdO4k8Snhgmc7lycWYoODZGGCbSmPzM74nY6iv4VSgGtbqd3Eyj_trNh87xjZpApkiiqTEJpftT1g-djtUJKyLje2ta2RnXHkoAq7NBRvasAc3FyUaw2C23AEqP2WcPBa0y6OWZQ3PxezKiv5nlNl5vLx7x8gz-F3DQzFQuk5yvEUhUJayZmlCk2HwmjE8GJ0yhn27znOJcffl9me_-QljtJ0E88sj3JR8_XHFRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
وضعیت این‌روزهای لیونل‌مسی در تعطیلات:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/102033" target="_blank">📅 23:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102032">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LsxSCbDGDoskxmMlPAA0qbm6GCmsP9l9pbPe6AskIGOgNdB0ZQZzFZ2ZlcKeg9sxg95QeDZC49RKcoUDKF26FqsWfEwT8j35-4VrZuxBt5Xdg2sYvFxQcKOpMu_8V8XgR9ka9Cxiuh4PLCT0vTLhbq-MzQ3p_cDSrUJ21K-ZrCgF6zfGQRZuPmViOm48flAN7FLFfdy3v7ZuPolt8KVFa_ljlyC0bN3q-o9KKAgBl_90kzNB0mW315qI1SIT-rl01CT89qKmJddERHwUxoo3Z3TjeLI5FDXMfq3_XAI0Z-nL0gfuVpOHgrUCb90kulTSmK7Sj9dX98wBtt3cZqiWkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📮
🇮🇹
دیس فلوریان پلتنبرگ به رومانو: بعضیا همیشه میخوان اول باشن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/102032" target="_blank">📅 23:36 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102031">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pg6834j19-onTZyksz_TLGfUfB3KwP4Qe1TahPuOJcGEH2PmNQGgw4IivhCxLodImPkpzXS9US0CueVpsQpemcT9ig4iN0onPdURtxbxWz6nyKDKLGD2vA10xp4qdY23A2WtqrGE1G1Ly2wSWkAKpDeb_PnOdqrl8G9MtvHc9Kqo_09m26C1rU6H_vaMJ069Rp9L6uFbjlOtQ8zvsvu5f-AeBMeva4tLFM8715B6NEOyL7QTTaEeckNt5QST0o7jr8k2GEL7gfYjfw7FoCmar2PIqLhUAk0XjVNaXewBB-gR1vwVOMbF7xsVW72qbANiCsCCA4ZOLdA-fOhztU5CwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😐
فلوریان پلتنبرگ اصرار داره که هنوز هیچ توافقی (حتی توافقی اولیه) بین لایپزیگ و رئال مادرید حاصل نشده
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/102031" target="_blank">📅 23:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102030">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
💣
💣
#فوریییییی از رومانو:
🇨🇮
⚪️
یان دیومانده از لایپزیگ به رئال مادرید پیوست. 𝑯𝑬𝑹𝑬 𝑾𝑬 𝑮𝑶!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/102030" target="_blank">📅 23:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102029">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e020f6fb8a.mp4?token=dEMdWHUTzPVrAitDx5eMqMu_DsZFbn6YzvlwSg6PYBD2yQj7gyCFziTQOlkSYThPn51NCnIx_FxmPDUsGk1BLQ3EgALDUqGntTE6sWu14xkYhwlUqpAL8aev6NXGSjXFY7d3lylypGSROgqGTaodfvz8v3f_h6tlc6GVgAGLJvM5TIsQBIhT5rn5xuKJ9qn2dXJbXidqY1iH8YQI4eQcA-ru2gJQSG0-TBMV9R_4arOaIygGqmF3RRcbospymVavh8KdlOaUad2OjG-uH5AkPa7VsoFpMurj9r6cxTu8MZCt0iKneoEzfNPOKx-UESPeCFuNocxicIcsZJVnGPoKMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e020f6fb8a.mp4?token=dEMdWHUTzPVrAitDx5eMqMu_DsZFbn6YzvlwSg6PYBD2yQj7gyCFziTQOlkSYThPn51NCnIx_FxmPDUsGk1BLQ3EgALDUqGntTE6sWu14xkYhwlUqpAL8aev6NXGSjXFY7d3lylypGSROgqGTaodfvz8v3f_h6tlc6GVgAGLJvM5TIsQBIhT5rn5xuKJ9qn2dXJbXidqY1iH8YQI4eQcA-ru2gJQSG0-TBMV9R_4arOaIygGqmF3RRcbospymVavh8KdlOaUad2OjG-uH5AkPa7VsoFpMurj9r6cxTu8MZCt0iKneoEzfNPOKx-UESPeCFuNocxicIcsZJVnGPoKMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسطوره فوتبال مملکت علی‌آقا دایی
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/102029" target="_blank">📅 23:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102028">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V-Jf-JDFYT5hmzFjQoKs4JmLlmoPVu4ar7P8xJCR4KckGrpHNOWgX_G_SzdWzabmwMBGHLBDFvjmlTf_9rLStKBzL86wLdDH9bH3bbIAcH2O9lNMO3iZ9JGYoPTvSfxEeKMynx6rjPkOYpnhhb-K9i9hf8ykdwLEZorzGLvgbWz3yewPdGjfYlI5jLxixaKNZKRYD4X72Ru2fKNgYvtreJTAzaQTIruILOXCnhoWR39XllTCLE7FJx745MlvsbK_agBM0eQPeFCaV8NstUc4viHOirwnlVvuFQ2-d5CoAl5B6nXip13iCf7qHRL-NHjY-fSY3N3bP5eVXkTPXrM5Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
👀
رومانو:
🔺
خرید دیومانده بیش از 100 میلیون یورو برای رئال مادرید آب خورد.
🔺
مدت قراردادش هم تا سال 2031 هست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/102028" target="_blank">📅 22:48 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102027">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h7akM1nsPOQPdQq40UThZrzimtRHiV5G2c2jjLfuaMUYR68CktDIGCI7bSdYWCBydryz-PhCemq2c04aXuumGL5xY6otk_0Her-HiaE7nicGREDEHUKmgxsjcR3LqMJoSQi1wPxRA9HcgC2jvlJgJc_DFtSyoJFyg4i8BnZXggH-JZGne0VvmLtwgfflSlRS0JQ7I996kdeV9XHbz-SdA73GkxxCxNB7LdzAtH0X8_57Op5wrUnJYNaxDJtMEnmKxYdO4Nu6kMlVP_rk9FMvM8gTmnvMgXwosEaCYjyr8b1jlgiWEx72EXFNXGiQT6pajE1-ICqPzEW3uWsNhaxFPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاهکار پرز:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/102027" target="_blank">📅 22:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102026">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
💣
💣
#فوریییییی از رومانو:
🇨🇮
⚪️
یان دیومانده از لایپزیگ به رئال مادرید پیوست. 𝑯𝑬𝑹𝑬 𝑾𝑬 𝑮𝑶!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/102026" target="_blank">📅 22:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102025">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s3FoT2IcQaQfdDpg0riZpW-BtKr8o4ToHw14lClyoKbswHRD1ciyDrmfdJJoEIgeu4W_m80aQ8q8vYJMS45t6fG9NsjnvYlRvs7z30bFR4ukIt7HvZusRh0pg3lMFfvGGVX-_gTx9fDZJNBd36b068uevnBOUk3utMor-xNIpI__sTxDoiqpr4ZfQgIPnsvP1qjRQRU3m_e5NS_aWAylNeEvtH0ugmmx5tdParQa16x2fF1nG5z1JKt2NkBQ7_sa6B4XyB_uvs09PoVzKX3c8feP25iByIk1UtpoEtBcB0b3Fuq0VdNBWTnUNmNVUdEeIanYYnAZx8V18f_g1xiSwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
اسپورت: خولیان الوارز گفته میخواد یه قدم دیگه برای پیوستن به بارسا برداره و بزودی انجامش میده . نهایت تا ۱۰ روز اینده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/102025" target="_blank">📅 22:32 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102024">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lsoxNlju29xs5yhDxU3V7X_k0Ye9pVSVP2Bg0MxQ1eBmRD9TOq_cfFskYMQ7sZ6rQwqvzxd7tsng57mpYfIbytTe_6krCyIs2aPqkJCTi62PI4MLZzE5623Y7DWAN-nI0yv-85uUxdfo3TX3Dthu3TBLZheaB4ZHY49cqrcCm4h-_vq9YC_DINDLTEHjUaKScLA9ZrNUCdiQimr80Oxmq7iOlVx63oo4I-SbzW_29NYs4mwgeiM6Lzm-QSmRVi586Tu8UZ8kC2Pj-cMjNRy7sscp3qvcS9NRkY6HT7qu34VD5ik51OsA1FrubFTPMZ25D9dqpLjrIZdlamPo3367ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
💣
💣
#فوریییییی
از رومانو:
🇨🇮
⚪️
یان دیومانده از لایپزیگ به رئال مادرید پیوست.
𝑯𝑬𝑹𝑬 𝑾𝑬 𝑮𝑶!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/102024" target="_blank">📅 22:29 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102023">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9274ecf947.mp4?token=BbDyRDe2uaPqO9h_XTou3bFQrZ4JUgHDPZdBDaTVkPAxalp9waXzT0xoB3CacwpV2XNSQZ9UJqS_azxz7pVDSw7z6R7PjF8EzwuJ7nFK2dUVvsaHbw0SJ7fUA62T08kmED4XHITlmySChw9bx4dVGtWbW_rn6i_jXeq0K91NQhAf6giXZrj9OJ5v-EOqJY4MSyvuqWoWYWcYm3lnE5I3S1I8hLTMqX1Z413MZhqfmSvDpLYWcsr8TBKFMHr6A3fGsWEHppFmFUnMl0FHsjjg0yDCMPyKnr--Mt8aEVVaUBRl44kdYUmoBF-tJtOlUMlQ1wtcw__jh1vk_LgnKWoWYylSb-5XafBgReHqfHyBKfeYI5QbHWo3HW_ebK16Zg5PI6ZlPZNBtueQHRtcoEjVWluY_SM0IHmuIhJEz9lKLk_z4BpMkfV0hGQpNyFtZZ5v4oOOz6JjVoF2T2RjIyrj9crX9Q8AVCZlTdIqNah60COUJh25AhQIMeSE1pWZQHxlKGw2tUuOSc6e438LT4dSUzC6ktSGMeTc85YwBRkTBP3PvHufrlkVQsTQppEdS-X3cG-rEXYiy62eirBy3FMsJ-PWk6AoNf8MRNziO_fqzLhaaoGn8pLVctv6QZdToSxhn0pfh0j0x2xN_V42pah-Qkl-SVNVGLHMJ1RJmr08dQM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9274ecf947.mp4?token=BbDyRDe2uaPqO9h_XTou3bFQrZ4JUgHDPZdBDaTVkPAxalp9waXzT0xoB3CacwpV2XNSQZ9UJqS_azxz7pVDSw7z6R7PjF8EzwuJ7nFK2dUVvsaHbw0SJ7fUA62T08kmED4XHITlmySChw9bx4dVGtWbW_rn6i_jXeq0K91NQhAf6giXZrj9OJ5v-EOqJY4MSyvuqWoWYWcYm3lnE5I3S1I8hLTMqX1Z413MZhqfmSvDpLYWcsr8TBKFMHr6A3fGsWEHppFmFUnMl0FHsjjg0yDCMPyKnr--Mt8aEVVaUBRl44kdYUmoBF-tJtOlUMlQ1wtcw__jh1vk_LgnKWoWYylSb-5XafBgReHqfHyBKfeYI5QbHWo3HW_ebK16Zg5PI6ZlPZNBtueQHRtcoEjVWluY_SM0IHmuIhJEz9lKLk_z4BpMkfV0hGQpNyFtZZ5v4oOOz6JjVoF2T2RjIyrj9crX9Q8AVCZlTdIqNah60COUJh25AhQIMeSE1pWZQHxlKGw2tUuOSc6e438LT4dSUzC6ktSGMeTc85YwBRkTBP3PvHufrlkVQsTQppEdS-X3cG-rEXYiy62eirBy3FMsJ-PWk6AoNf8MRNziO_fqzLhaaoGn8pLVctv6QZdToSxhn0pfh0j0x2xN_V42pah-Qkl-SVNVGLHMJ1RJmr08dQM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
آنخل دی‌ماریا: مسی نشون داد که یکی از بهترین‌های تاریخه و تا وقتی که خودش بخواد میتونه همچنان ادامه بده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/102023" target="_blank">📅 22:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102022">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aNtM0RqHP3dW_GfaYJ2r_0Prw2B80aAR16G66xL-glT3ZVN6DOV1L1SoT196vFCGGkUP1-Grof_1kDSQEyOYnCZEjqV_wKEehM8zyWyr514u3FTMgvDMDPuAQOsYID7LPkWwQkVnuwaR5mqUgLvhXRO81t6UzZy8uy95pNP5epkp1iDS-BocQhxcSnwxoUoLfS79HmOZR5YZfj4fp8SpXLCb0LgoaueXBwuO6KeRJrJDkXI9bTrQh7ZMheR-sB1o28BISzKItJkt3g6JcTK7LIxe09uRtRH4rIGdGSoUb8wjQYn136OcCquwd_GAl-rXwAsqbZduuRzgo2uWMAYqeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
⚪️
عمق اسکواد رئال مادرید برای فصل آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/102022" target="_blank">📅 21:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102021">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e76692a40.mp4?token=joDSwv7XweHfsH3poL_bUo1BRbFi8ysrlWRHu8nWMf8E_Sdd0TPrt_NDW-tkqUviEKd3SEzG4a3iEhaugWQid-tYm6560WMLQpUXpAp5clRHJqvQSJTTvTgShs5K3ick14nHYzYWmKp1yBYsktJZ8lZ-Zd906pgp2SpT-J6HLniqH6uuST2bouZbd73E4SQFqO9GYINZBR3aITKOV89UBMQZMIm3bDTI9_NoLjYOAQMSa-ZuWgCfrZ7SLUnGlZpa7QxjxEHvqkl43FpzOs0jItsr4hPrTqX-BL-c62Dc-f1TAQ70m9_wsfdXNwUyvd47Jl_xvIOYGzQ-BzSH57c7KLg4H3s9BYPgXqKMXaLrR6vhkzzyHn1KBGgGkJP_PALrD6q89XyEm3LRmF4cxNAaMWnI57O3d0tHeh7IKLrt820uM5ITr6V37nlMOehwgUecRqxQBBMkYONBJ0FSpa2sIrkOKLcRgSzdCCcsK4-_BcPx-JCWDjegWBB6BW2bzen3SuOQvkq6DFZn-y4D6ZAor-KwfOKgsK2Bv-bJn4I_LyZlFGJyV6kNcaSnDY8AugDnSknTlOPMQn-qizHrHA72msqAlsFscN3JtHTnxM4ko7kkJFGC4Tejn3PkaUBX9BWeFvwmd4NFF5ejdNFRPvt4eK2E_qYRl-cNB_Sn4IzaOq8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e76692a40.mp4?token=joDSwv7XweHfsH3poL_bUo1BRbFi8ysrlWRHu8nWMf8E_Sdd0TPrt_NDW-tkqUviEKd3SEzG4a3iEhaugWQid-tYm6560WMLQpUXpAp5clRHJqvQSJTTvTgShs5K3ick14nHYzYWmKp1yBYsktJZ8lZ-Zd906pgp2SpT-J6HLniqH6uuST2bouZbd73E4SQFqO9GYINZBR3aITKOV89UBMQZMIm3bDTI9_NoLjYOAQMSa-ZuWgCfrZ7SLUnGlZpa7QxjxEHvqkl43FpzOs0jItsr4hPrTqX-BL-c62Dc-f1TAQ70m9_wsfdXNwUyvd47Jl_xvIOYGzQ-BzSH57c7KLg4H3s9BYPgXqKMXaLrR6vhkzzyHn1KBGgGkJP_PALrD6q89XyEm3LRmF4cxNAaMWnI57O3d0tHeh7IKLrt820uM5ITr6V37nlMOehwgUecRqxQBBMkYONBJ0FSpa2sIrkOKLcRgSzdCCcsK4-_BcPx-JCWDjegWBB6BW2bzen3SuOQvkq6DFZn-y4D6ZAor-KwfOKgsK2Bv-bJn4I_LyZlFGJyV6kNcaSnDY8AugDnSknTlOPMQn-qizHrHA72msqAlsFscN3JtHTnxM4ko7kkJFGC4Tejn3PkaUBX9BWeFvwmd4NFF5ejdNFRPvt4eK2E_qYRl-cNB_Sn4IzaOq8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔵
امیرحسین صادقی: وحید مرادی من و فرزاد را در هتل المپیک آشتی داد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/102021" target="_blank">📅 21:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102020">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XD2VflmfTVXPrE25w_cY4iyLzV0YuoSAKLJFvvo6pC0ZNCac6A515x4w8IJ-FF1JBr_B-BrfZ70w-oSuwao7cndjhKQaJsL2A58KSl-G1hZ42Hn21MBsSPl6NbJ37B3h9H96LQacaXzkn5GM1IUImHQRRj0y-BvG98Hf4X_WZWymll52f0sukb_WmXgsIPQJ9AKkrDUpR7wFyD3OGD-AiYqvjtRyEPpUfgjFLdsw8qhgBwnYZ0w16agVnVYliL2NkSnnDPr9Fnw8LukGu0SsvGtQHmoIkHvcaTX0sh_VPLYOiNXGQCvVUNlkBUVNOI8ctXUMXqR7jbdNt174Ww92sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🚨
پژمان جمشیدی که به تجاوز متهم شده بود، در رای نهایی دادگاه از این اتهام تبرئه شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/102020" target="_blank">📅 20:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102019">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eHDc1cYe6-e3IMvLAMWpWtBiMrK77HLffhbDrk3tXVERXFicT23B-s6vLnwEdr0qIULCu4ysZDYCnD7S2LFFeMyF3mrfzdvq1-XKh9dj6q1BPQRwzAXnoSZYEPpCPGJb4x-jOE0djsxY5D62UFMUQE94WSroVvh9W_yi2M51S0LeBrkNRC8acLceWLaFm8AY2fiAE5i_YXGWZ1x97-r4dhhe1RLx7H8dY_lNqTYkW7eqOaAu7xXODdKgaYLNcTyWAnYIbiXX9jy0xDTpAhobJNCs6BCk90Qjeh57l9NfrDKvQAbCnLz6OWo4kVgEFkzycRNPGcgXlNLgEr0EqWHyqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💣
آرانچا رودریگز: انتظار میرود که یان دیوماندی این هفته به تمرینات رئال مادرید بپیوندد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/102019" target="_blank">📅 20:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102018">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/260d53f1d3.mp4?token=O72gAn2RjfWYhG2M3dj7t2ecKmlz7nBypTsvLfzPmyB7-wZLda1x-_zjJksLc5otzl8FLbXLYV5vZ-1eslf6Xb7Egw-yI1aFOjg4YmZE5EBiyR2v1momHunw4ZsTMiVvcLcufZexvrnWM_hzo_KJIz-46F97INcUBn5QVeOLiMRblr_fGAD0M0OoArlDPNj2Ufd9pLAEOac2TOhOgNXZ054mI-MnjqFamXNz96ORCp78U09ONnCyWk3nCblpeDhtrNhuHizNn1r1hco1gm2LpOYIxg7ZK_WbFNDNSM4NkGI-CJkoEjj7Gchr5jyFn-cb9SOgizJcQ3Ab4CewacaHb6Qz0-APQEWXgCHSwzhHOzzAN7mk89m4w48Cx7_9xxK-38ymxKXqexBqlzrr_b9mppoQf7cD7CX69aP3aIZZflT5yjHBB4UfjO5eXDnJlxWkbC_eW4QYg-cVdWoi1aeRAgCbHIMfm4jfxnu_vIjqiOUcRgGTmlNeWVIdPnu2LPngliSTk1O581fhcfV4MSMOvk0_xpT1hp8SSedIeB-4giMCWL2Czc7geS0XemrF8xGAy-zk1Lp80wEGtYdc3GcyORiQMV79VwafRax7oznDZrR2GZby6wkfo-CN_5lwuDJ0ThLc_5yMZ83B8CXglQiOsuYpllMG9NMmuaFtP4vs9r8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/260d53f1d3.mp4?token=O72gAn2RjfWYhG2M3dj7t2ecKmlz7nBypTsvLfzPmyB7-wZLda1x-_zjJksLc5otzl8FLbXLYV5vZ-1eslf6Xb7Egw-yI1aFOjg4YmZE5EBiyR2v1momHunw4ZsTMiVvcLcufZexvrnWM_hzo_KJIz-46F97INcUBn5QVeOLiMRblr_fGAD0M0OoArlDPNj2Ufd9pLAEOac2TOhOgNXZ054mI-MnjqFamXNz96ORCp78U09ONnCyWk3nCblpeDhtrNhuHizNn1r1hco1gm2LpOYIxg7ZK_WbFNDNSM4NkGI-CJkoEjj7Gchr5jyFn-cb9SOgizJcQ3Ab4CewacaHb6Qz0-APQEWXgCHSwzhHOzzAN7mk89m4w48Cx7_9xxK-38ymxKXqexBqlzrr_b9mppoQf7cD7CX69aP3aIZZflT5yjHBB4UfjO5eXDnJlxWkbC_eW4QYg-cVdWoi1aeRAgCbHIMfm4jfxnu_vIjqiOUcRgGTmlNeWVIdPnu2LPngliSTk1O581fhcfV4MSMOvk0_xpT1hp8SSedIeB-4giMCWL2Czc7geS0XemrF8xGAy-zk1Lp80wEGtYdc3GcyORiQMV79VwafRax7oznDZrR2GZby6wkfo-CN_5lwuDJ0ThLc_5yMZ83B8CXglQiOsuYpllMG9NMmuaFtP4vs9r8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چنتا سوپرگل قیچی‌برگردون ببینیم تا روحمون ارضا بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/102018" target="_blank">📅 20:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102016">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LqjjjwqYJPBt89vbPwcyaWrH610vhfXzNcZUl-OafGPbkEnc8T6NlmQotxu3Wx71RJuym0UIT4eqbBsyRKM-hMXy9Q3AjMRvvB2WsGV9nyh2W1ScuCAQNxk2bXt69Q7_D8tc31EVnhUayX2oOoXgXo68XocVQ3tvHztg9C055ufcd2BkMqU8gNKMqOoBB5uTYZnOKYx5p7W7K2bgvD0HB5PTMzvNZUJ44QdWKu-goEL6Q9izNZNf4pkHaGGhvZehS3Erb9w508t8SbE4D_wXfsl9hiMzCO2LHHYxHOTOtKDOtGdqektfAZ4CnQk-UGqH8B6pbDQjSuIT08ElccNcYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m8DZbBQksaLODYljxqtlGe31rajeNkI1tn_AQeUoFAq5CaicnK46qIAZrn5KqsGOcAoIZaWObxZu0rcoQ9TDgn7KKtPMzVAHfGcO9UPLDPpoi1YZm-XMSEmJd3nhm32pm6bRGR2Vgu4PBGYBkYg4TRph8yfI2uXHjLDppKddNUTwZfsR2AUNBUmypAslkrdoOOdrP-e37aRxMPlHnXnguOdadQtm7iXmLC70hrfS5OHF79Lt_AJEPhr5s5hAe3gfADihQ22BATUXa-Eigx5La3u_h12jJ02HmcLXGkD3lKbybTeLdw19AKdB6pmJBGBh3Q-_uQ_DrXkA-IaAv7VQtw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
لواندوفسکی:
شاید مجبور باشیم ۱۰۰ یا ۲۰۰ سال دیگه صبر کنیم و منتظر بمونیم تا دوباره بازیکنی مثل مسی ببینیم.
🐐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/102016" target="_blank">📅 19:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102015">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PMq7eyrje8ioSDMyQLfM6uIJ-zJ92r0ZQf7IGsD-8DKuzQ2AmaQmwVUfBULmUoE5pnbP0DLESt7NBURwYSR8Lt4AQEo6lVjVRg2cJdtbyQEwk_6bAcPngiICMabX1HJ5o46qqtH3yX5iUeE6q4DCPo6RO7Ge1hdPCaT9hCoW8NwthzqxhILo8STB1Tu-CoasY-NxLoG86GdejBBVXNh02F8dM18EHy80tXnhLXXZvlRFYSVa_RpipPnOmCVVWauaLqbIzyJxeCn-Fd7loYKZCGdxN8r49t2icJxhQnTthWj92IxopphyX5DNDP1yEiALap2aPm80jza-tKA8XeZ6nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
گران‌ترین انتقال‌های تاریخ فوتبال با در نظر گرفتن تورم:
🥇
رونالدو: ۸۰ میلیون پوند → ۲۹۲ میلیون پوند
🥈
ادن هازارد: ۱۵۰ میلیون پوند → ۲۴۵ میلیون پوند
🥉
آلن شیرر: ۱۵ میلیون پوند → ۲۳۸ میلیون پوند
نیکولا آنلکا: ۲۳.۵ میلیون پوند → ۲۲۶ میلیون پوند
فیلیپه کوتینیو: ۱۴۲ میلیون پوند → ۲۱۷ میلیون پوند
پل گاسکوئین: ۵.۵ میلیون پوند → ۱۹۷ میلیون پوند
مارک اوورمارس: ۲۵ میلیون پوند → ۱۹۶ میلیون پوند
گرت بیل: ۸۶ میلیون پوند → ۱۹۲ میلیون پوند
استن کولیمور: ۸.۵ میلیون پوند → ۱۷۹ میلیون پوند
ریو فردیناند: ۳۰ میلیون پوند → ۱۷۵ میلیون پوند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/102015" target="_blank">📅 19:49 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102014">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb3e14eaaf.mp4?token=dGL2agXBkWLxcuK8jjBWGk0w4PtyCl0GilZNRgNrdZVJXFnOzitxXsDRqqfQrNcqpXW9h8Lgug53KG2mDwhQXMxymfDyq3FR0j0xuptYuKBtoBdgepDq5wHYpzkL-dAo9YIFFajJ7QkBShkd2l7sIQO1Yz5GOohjdsKeSxl_6g9Cr4Q3VE70qFNfIM2UpZ1O1YdmJe2L2jwIfYln9lRF7fz-vNE-QA48oOYohgMCEuZnP2D7ZCJkuybwlUZzLoKseY0ciXRt7_XyhJTGcC5DWS7zRP-LdY2V-iW51FYRtTxeDmRPiOPQPGvPZM2llddWQGuz1ogxFu0F8d5j0k6K3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb3e14eaaf.mp4?token=dGL2agXBkWLxcuK8jjBWGk0w4PtyCl0GilZNRgNrdZVJXFnOzitxXsDRqqfQrNcqpXW9h8Lgug53KG2mDwhQXMxymfDyq3FR0j0xuptYuKBtoBdgepDq5wHYpzkL-dAo9YIFFajJ7QkBShkd2l7sIQO1Yz5GOohjdsKeSxl_6g9Cr4Q3VE70qFNfIM2UpZ1O1YdmJe2L2jwIfYln9lRF7fz-vNE-QA48oOYohgMCEuZnP2D7ZCJkuybwlUZzLoKseY0ciXRt7_XyhJTGcC5DWS7zRP-LdY2V-iW51FYRtTxeDmRPiOPQPGvPZM2llddWQGuz1ogxFu0F8d5j0k6K3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الگوت کیه؟
دیومانده: رونالدو
رونالدو یا مسی؟ مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/102014" target="_blank">📅 19:39 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102013">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromچِشم به راهیم</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c1d6e560e.mp4?token=dIQoQYvgBmc_1pNhDnTcKgr_LFmX-mk72uKiz-2nGi_NrPEZ0PB11I3g3ikRwwnA2l33ww_UTuCSo4XmmTcCKBm_Y5NKCO16GDl3h3FDkW7O0iiNJUTaQr42UA9T9ZAp5pLjD8Wb_h4XKIFgF7s9Fkg55nY64o2s678d6aKDMVd5Y2oMpsrDyMAI-vqosUYbCtAQFlS9T7hzyZ68OV7TvdrFATypBXht6dVoEOmlSskvK0JYRPSX0GlB4RvMEjz59j7VeqwNEqx3gW1uPVp_vHUNQM3ydLqW0WDGCyGr_-uQ-NQT0yAOYvRn5DYotxPWOcXDooCQY_gqcEM5YWv2FEZ8StXWrcDMM21J4atqLvkFo2UEpijFydXJjg1AnhApGrLJty-5Jx9AXe5OwgZRgwqB9p9poHTM_eRZ96JppFiIXGFDK6t6UZCQZXKBI4JNJLLDSWo2DVXtDzUI6qyFoqCjrUQqF5AcS0WVvSsvQsn8BhFDrZ3Wl2rytYXYwswGBV_27yxVmfh8G1odkgkVxMbj5owxtBm38Q5QQ7Na9z9Gf3AlBEp4RLKOcr5mt4e_VZKHQQCnO0cje8Ms9WZWnCGmXRfPd-GisThHC88niabFi9N2OXgbUOWDoCEwE9RVEvIEqBVxLFxLqt9SCPdi1QVk52JjJem0v8UTKZfM4Vs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c1d6e560e.mp4?token=dIQoQYvgBmc_1pNhDnTcKgr_LFmX-mk72uKiz-2nGi_NrPEZ0PB11I3g3ikRwwnA2l33ww_UTuCSo4XmmTcCKBm_Y5NKCO16GDl3h3FDkW7O0iiNJUTaQr42UA9T9ZAp5pLjD8Wb_h4XKIFgF7s9Fkg55nY64o2s678d6aKDMVd5Y2oMpsrDyMAI-vqosUYbCtAQFlS9T7hzyZ68OV7TvdrFATypBXht6dVoEOmlSskvK0JYRPSX0GlB4RvMEjz59j7VeqwNEqx3gW1uPVp_vHUNQM3ydLqW0WDGCyGr_-uQ-NQT0yAOYvRn5DYotxPWOcXDooCQY_gqcEM5YWv2FEZ8StXWrcDMM21J4atqLvkFo2UEpijFydXJjg1AnhApGrLJty-5Jx9AXe5OwgZRgwqB9p9poHTM_eRZ96JppFiIXGFDK6t6UZCQZXKBI4JNJLLDSWo2DVXtDzUI6qyFoqCjrUQqF5AcS0WVvSsvQsn8BhFDrZ3Wl2rytYXYwswGBV_27yxVmfh8G1odkgkVxMbj5owxtBm38Q5QQ7Na9z9Gf3AlBEp4RLKOcr5mt4e_VZKHQQCnO0cje8Ms9WZWnCGmXRfPd-GisThHC88niabFi9N2OXgbUOWDoCEwE9RVEvIEqBVxLFxLqt9SCPdi1QVk52JjJem0v8UTKZfM4Vs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
اگر قصد دارید سفر اربعین را با اتوبوس راهی مرز شوید، پیدا کردن بلیت را به سپاس بسپارید
🔹
سامانه پایش آنلاین سفر (سپاس) با اتصال به همه درگاه‌های رسمی فروش اینترنتی بلیت اتوبوس امکان مشاهده و مقایسه ظرفیت‌ها را در یک سامانه فراهم کرده است تا سریع‌تر و آسان‌تر بلیت مناسب سفر خود را پیدا کنید.
🔹
از ۲۷ تیر پیش‌فروش بلیت سفرهای اربعین آغاز شده است. برای برنامه‌ریزی آسان‌تر سفر به سامانه سپاس مراجعه کنید:
🔗
sepas.rmto.ir
#چشم_به_راهیم
#اربعین_حسینی
#سازمان_راهداری_و_حمل_و_نقل_جاده_ای
🌐
rmto.ir
🌐
141.ir
@Cheshm_Be_Rahim</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/102013" target="_blank">📅 19:39 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102012">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
⚪️
فوووووری از خوزه فلیکس دیاز: انتقال دیومانده به رئال مادرید نهایی شده و بیانیه رسمی فردا منتشر میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/102012" target="_blank">📅 19:27 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102011">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L91Yb2eDpDEWwPTA6DJZvwFFhJC2fVHOzbJF422kFywPTCjLTSqlo7G_CTXbQ4_p_PluqLBMy0pW0INpOyGkhR0VXYLt9XJR0Qj0JEthZX0RebTCLw3x8z6fFQUs0Ws3cHq1_JmFdAEJJZ6e0wMsEtMkQOKKOLD_DGrJQIjkdvpa2MDzsfeCykCiPtQ5EiEY1L0YBlVIOM63izqDAcp2grDNvVeNuJy0iVzMaS48_ECKNhIBrl6z4Q2Qi4G74jGsps9JVmm4oAq3nN05_i8zqJPvzeWMtxDjq_QsXynrzrSsBFhLwtELo6lUEhb3aUKLJ8GgP1ziHBL7Chae7EX-9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فوووووری از خوزه فلیکس دیاز: انتقال دیومانده به رئال مادرید نهایی شده و بیانیه رسمی فردا منتشر میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/102011" target="_blank">📅 19:23 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102010">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/746abba13b.mp4?token=a6JVOyBIDWUJnzZzhpiPgAyfLh-wVwACPKyMPvYp3crFSPghflCujQE5jqsAwPFYRO9jcZyyAtbY2yYjpU7ytrFR3HeatekcVnButfwzVvz7kWbyB23MTvI0gP6JzOr4Yj9sBhWpA6KB0RNT2fx8ZHE6nKdhcRWh0jo3laO_vmUN_HTdAJ0LGh-icYdtxYm9VBp_Km0YXyWxj1xku1dU8D4Q-56jXMM63oAPaXXqZVQH-CeXi3rerrISfGIKtsLNkRe7Q63iUgQiwpV8Swxqq5FPUwOu2P8mwxrXjwdwBE3iROioUFeG-AyZ0RjgGU-zLeCw0XCn8Jr2T9uYewHY_qZI3RDA-tIONYmLnYZR4GU0Orwjstu5RaYi2ruS5Wplyp4U703iIXohKJCpPXamTInAhBCwo5IXD8Zxw3VkGA_1IUexEdkNLOJmlsCMjBr9zElrOd7YiqU_SCzkFFdZSiFU845X_sbqofhiJTxmJX9yWjNnMZRLbPYoWdVZmeMFcFn5iDR24f94FLz15KtQ5zbYKFn1HzNV96jiKL_k4nvw6njRW8BW_k7Z70VGlQrxBWEiTCUUv8pXUlqla7XUgMfXXujMM5EhCuUxMmA01QdspXOZW5NgRundpsCzVCXd6YUh3DHrVc7yKGgbgcwpMEx122pfXuGwm3J5nCtEyHE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/746abba13b.mp4?token=a6JVOyBIDWUJnzZzhpiPgAyfLh-wVwACPKyMPvYp3crFSPghflCujQE5jqsAwPFYRO9jcZyyAtbY2yYjpU7ytrFR3HeatekcVnButfwzVvz7kWbyB23MTvI0gP6JzOr4Yj9sBhWpA6KB0RNT2fx8ZHE6nKdhcRWh0jo3laO_vmUN_HTdAJ0LGh-icYdtxYm9VBp_Km0YXyWxj1xku1dU8D4Q-56jXMM63oAPaXXqZVQH-CeXi3rerrISfGIKtsLNkRe7Q63iUgQiwpV8Swxqq5FPUwOu2P8mwxrXjwdwBE3iROioUFeG-AyZ0RjgGU-zLeCw0XCn8Jr2T9uYewHY_qZI3RDA-tIONYmLnYZR4GU0Orwjstu5RaYi2ruS5Wplyp4U703iIXohKJCpPXamTInAhBCwo5IXD8Zxw3VkGA_1IUexEdkNLOJmlsCMjBr9zElrOd7YiqU_SCzkFFdZSiFU845X_sbqofhiJTxmJX9yWjNnMZRLbPYoWdVZmeMFcFn5iDR24f94FLz15KtQ5zbYKFn1HzNV96jiKL_k4nvw6njRW8BW_k7Z70VGlQrxBWEiTCUUv8pXUlqla7XUgMfXXujMM5EhCuUxMmA01QdspXOZW5NgRundpsCzVCXd6YUh3DHrVc7yKGgbgcwpMEx122pfXuGwm3J5nCtEyHE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی فوتبال تبدیل به یک فیلم و اثر هنری میشه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/102010" target="_blank">📅 19:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102009">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UVVHRPhb5Yk7HFZEPPE6Oq37l1EkLMfILIiAQEx-qPtM6LNmwO_TadpBeVzj286J4q1tZYbV6-u7Zha3GmBTtNyfHYcgHQiw0-QSVDb9XXI5nTcIHHluO1h3QzFsNp7QltKsFz6y5Aeg11LchoAU5SOxgXszpFSYaz7D5M0ashX0y2zrmx2xlioqkKrIU_ejvQt2ylikydR0LIOjPvGdkOMIQ3WJ5LnkDIV3KB-p1cKfM7wXqxXtBtFSHgV11mX71O6vK0GkQQaRyBqosNYPRdSEv3TUe7U-XCTLoIF_VtHb6ckkblGC9pROoALs4u0huRE82LkhOSpbPIDKZXA04A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
اشرف بن عیاد:
کار تمامه، مدیرای بارسا متوجه شدن که موضع اتلتیکو برای فروش آلوارز تغییر نمیکنه و نمیفروشنش، حالا بارسا منتظر واکنش آلوارزه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/102009" target="_blank">📅 18:52 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102007">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AGNFM5XJpTwOUhPOO7MoTQ-i8WhCB5qTtPIAaG8TK52PdEnMfKGz5lLj3u4hhk0Rb41yahSYt6O01yxs55o0HcBvR6aiLYJgIWG2td8PCss6y0L_1hhag8LN9VwkIah7TG2zczwojCXrC1HyiMoqderpCvNe2MQnFxeABzhLDYFIZpaH9RQEhaZHckPpAZ-tdmr7ujaPeslmPlMjaJVyBD9FdOfYR3GR_B8xrYXi--73XfcCixdksGwnE_UOBePoI7jM_IdChts1awau0zrumBMp2xr6ZvIuFTnvWebBJGOoelReOqPt1LsKjHdokuuNLFdLEeChtfrU3iSI0TWCqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F0Y1nWVGXMIynrw7nRqXamTxSrHmfo0-NLzdjSNbSRd1CjjRQIEu9w-e4mhxWHpGEX58FydLQNLApxdUKZ4kgXbO-ruS00CuT87PY1KC5yKRWetjfkqbjXazrsI5SKx5ZpTk6R9UqcQ6Ig_BOtGKnnfpAkExWZy39daJCuklpbO91-CQPwBmEZxgi7U4hl-K_E9iaeVbDFZGptY735glu_RfAYnkCdkoWQQjQXkh9ABV1eYnrUcZEjGn8Ys5vfRJ0uw8jt0yT0a38dfxqTG36I8GkumVgFrVdD5aJSnv2FAyQCJ6qy300QYuM_XZj-06Z9nuwbu-DcLXYpxeHukxNA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
تاریخچه رابطه‌‌های وینیسیوس جونیور:
• 2021 —
🇧🇷
ماریا جولیا مازالی
• 2022 —
🇪🇸
اِستر اکسپوزیتو
• 2023 —
🇧🇷
لورنا ماریا
• 2024 —
🇧🇷
جولیا رودریگز
• 2025 —
🇧🇷
ویرجینیا فونسکا
• 2026 —
🇧🇷
ویرجینیا فونسکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/102007" target="_blank">📅 18:28 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102006">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac77f90860.mp4?token=wAydTH0q0hyvN-I7QnmNBcHETCOJZMG1e-6XQCKOt7y7Nac0QcS2x2jhgmwVXXAJj1_Pkzn5HxssdILh1KvR1KnTeHriYX-R9iHIt2vZ9IYLCSGoEAgNxyecmik1uGL13PmQlNiDgGghjpFBnxX5InekMBkVp6Exlg-T4DgPVGsRV15X06KJSCgZED4nZEiU_AgJWKmp-0A1hL_W0_XJxk48Glc053nyr0xMnlSuZ9L01JTC_CSFUF_FTvnXYguNhhMmgzUvYTytHWRulg7y0DvWw1CFzfddWARCH_CXnbHueTz0C1rVj-JzvVZUl7a-xQZoFAU0mqbOA4YQX00oPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac77f90860.mp4?token=wAydTH0q0hyvN-I7QnmNBcHETCOJZMG1e-6XQCKOt7y7Nac0QcS2x2jhgmwVXXAJj1_Pkzn5HxssdILh1KvR1KnTeHriYX-R9iHIt2vZ9IYLCSGoEAgNxyecmik1uGL13PmQlNiDgGghjpFBnxX5InekMBkVp6Exlg-T4DgPVGsRV15X06KJSCgZED4nZEiU_AgJWKmp-0A1hL_W0_XJxk48Glc053nyr0xMnlSuZ9L01JTC_CSFUF_FTvnXYguNhhMmgzUvYTytHWRulg7y0DvWw1CFzfddWARCH_CXnbHueTz0C1rVj-JzvVZUl7a-xQZoFAU0mqbOA4YQX00oPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خشونت بی‌سابقه در لیگ‌فوتسال بانوان برزیل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/102006" target="_blank">📅 18:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102005">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dRtd0JVlxPZ2Fh9VYOtjyTP8NTtOevy9Tmx5bRmdm4zPE_qNTt5HhdGAmfmXKBvF0Ra0S5ryeS_fkaAslQY20m1safPCclF9Y3MrA6nO2HxQ0SxHmr_kouZOq76zQYZPPiQZRbChHyg8OLCqcliTwOh2QEFwUpv3vNSjNIpW5yjyM77xm3wrghc4pY_99flREmmqqMq39PAfSc5qDo6vUGu_E1AcwCv_1sSJnjFRxvqRM5-3Tm8StEWSc6rKWiJyUn2gBTJbv2eQHqcshiW2XNHiIv9JxLD59nBwguTBux0KMadOAA-xuCezTFxePgHdQ7AjfPi4RzzRgxiyGITQWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔥
🇪🇸
رقبای احتمالی رئال‌مادرید در سید یک UCL که با دو تیم از این تیم‌های در تصویر بازی میکنه
🇮🇹
اینتر
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منچسترسیتی
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیورپول
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آرسنال
🇩🇪
بایرن‌مونیخ
🇫🇷
پاری‌سن‌ژرمن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/102005" target="_blank">📅 17:50 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102004">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pje6KoMMn3w_f3fADgAvNe1ASRiprWq9vdOlGwbWlt3BUP-Q-QeVyQ35nM0TVhoFMrXmdo0w8AVsKpD-lyeIssnmba3cSgZyWSwSJtZBgmCivZV3p2li6mPiGK8Z6KfCW5CKnQrpoDSurjd06zwK2t45NguiU8vojIh7w0odnABFB9wr7hUXk4pmz9H5y0C5nRMnUgRHTzDPVH3IiIqXvuBB-T5DeAjXUeNT-jxYhZ2oOC9liikXH6uC-s9liw6isVhguyFaJUcsiwM1OWT3twnu267nBzD1cc0N4uEdV6J_oeGtq7dwPOQ3PPM6S5eGZ736_2dmJMC8C1UNP0ChOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
متئو مورتو:
فولام قصد دارد یک پیشنهاد بزرگ به رئال مادرید برای جذب گونزالو گارسیا ارائه دهد. آربلوا می‌خواهد او را به تیم خود بیاورد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/102004" target="_blank">📅 17:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102003">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K2bkerGSjP9Aecog2ftiisyMiBF7HmVj76UsfBjLx0ouvQuyf3XgCtxqGeGuzt8YH5catwr88Jx1WWpHz26anN11sro7-1p5KtTPeQFZIO143cm-4RFGSRsOmICBH-XVskdPkugdeQm0DICfpb1-JyP4yRRzQvRkxKrdOK9fPf94WgcnjF7iBriiuCRUIHfgxsS7W36jVCbbUel70gJgUP6f3yfe5V7IVSwt26GW80xQaa2skKYrQD8tuQHGQk1Q3W18zAw9qxdW3pGrAJjAqIVkbjIuWg6kgA1VNREilZ-SvL-Gwcy_4i4UQSk5gIEIAZnvlgirRIqbQ-V4aAlD9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سانتی اونا:
باشگاه الریان قطر پیشنهاد خود برای جذب جیدون سانچو ارائه کرد
باشگاه قطری در تلاش است تا وینگر انگلیسی را متقاعد کند.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/102003" target="_blank">📅 17:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102001">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🏅
فوری؛ لینک پخش زنده بازی پرسپولیس و پیرامیدز مصر گذاشته شد
💬
@squadify_ir</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/102001" target="_blank">📅 17:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102000">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9608d1c2fe.mp4?token=CfWfMLOLVQ3Z-Mi9jrLrRVBmM0-8B6E0tbPHE3rKzwWFMUjlrudxQfwfSKP40-8FabPMIYfPNYrSwJnW4ip0ah99-vphgDMdmlMtNL9bVJPTx_qZv4vPTd_-yjxwqXuFD29J33Q-N3QtEOHKcNW7MpiABAJGoZxnyXtyZ3rvla5Y2f2gvqwvGmYQLnsz-ARsrvOpfq5fh5cUP3nLFkPefoqHrowurUmvxUTo2wG8LoTq1pz3WVC7A5QxDjHEAOYTkUUXT1C5ko04C3GLEKmNORBCZfLPdzmOke3sPqNz9Z8MkSNJvKuxdUw_7Z3QnGz6OMo-omqenQk4nIm9OB7mNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9608d1c2fe.mp4?token=CfWfMLOLVQ3Z-Mi9jrLrRVBmM0-8B6E0tbPHE3rKzwWFMUjlrudxQfwfSKP40-8FabPMIYfPNYrSwJnW4ip0ah99-vphgDMdmlMtNL9bVJPTx_qZv4vPTd_-yjxwqXuFD29J33Q-N3QtEOHKcNW7MpiABAJGoZxnyXtyZ3rvla5Y2f2gvqwvGmYQLnsz-ARsrvOpfq5fh5cUP3nLFkPefoqHrowurUmvxUTo2wG8LoTq1pz3WVC7A5QxDjHEAOYTkUUXT1C5ko04C3GLEKmNORBCZfLPdzmOke3sPqNz9Z8MkSNJvKuxdUw_7Z3QnGz6OMo-omqenQk4nIm9OB7mNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
آنتونی جاشوا، قهرمان سابق بوکس سنگین وزن جهان، از آهنگ سیاوش قمیشی برای آهنگ ورود خودش استفاده کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/102000" target="_blank">📅 17:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101999">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57f6f418b4.mp4?token=FGyuKNwA4Y4S43GWV4hTSupAcDAsyhf64rGGCUgIkJAA-hfJZ3GvS-2n3iKxL9bElsTX8FGeZl43PZQdeUMSlIEHOdDqf-6E79fwhP43iQzbrUBZGP7b0C3qyj4Ry20UWzATOXFYgIvgA6USMKzVLlIQSJ3VpdcUFIbpcKbGHi0snuD3KBtYP79YxiwKvFI-EsfteZaipW__OhKe7gtqDQw6dCQ4ZXLcTlqpYpBbY7tRKgOMAvobsoxxuv8b_JH67oRkqS5VU_jAXPIga1B1tjZCAYTGgu_CuoUzLole3Woz2xEXNcdD1_jHj0pbdUgko_S7uqXojdh7J-q-BlyW_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57f6f418b4.mp4?token=FGyuKNwA4Y4S43GWV4hTSupAcDAsyhf64rGGCUgIkJAA-hfJZ3GvS-2n3iKxL9bElsTX8FGeZl43PZQdeUMSlIEHOdDqf-6E79fwhP43iQzbrUBZGP7b0C3qyj4Ry20UWzATOXFYgIvgA6USMKzVLlIQSJ3VpdcUFIbpcKbGHi0snuD3KBtYP79YxiwKvFI-EsfteZaipW__OhKe7gtqDQw6dCQ4ZXLcTlqpYpBbY7tRKgOMAvobsoxxuv8b_JH67oRkqS5VU_jAXPIga1B1tjZCAYTGgu_CuoUzLole3Woz2xEXNcdD1_jHj0pbdUgko_S7uqXojdh7J-q-BlyW_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
قلنج‌گیر معروف ایرانی که با درودافای مملکت ویدیو میگرفت توسط پلیس بازداشت شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/101999" target="_blank">📅 16:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101998">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a860d22dd.mp4?token=H2Dgjr0mS6rb0LKFUcC_JPJtEjg95MRNU0M4oAOQBLMbqmEY8BvNhew5DaN0IbgucbUJMfc10Zlp03p1lVw66a1t9YujDLhgfu9b1LNuIqaqrj1XC2ZvSWHa2iMsw2aGo-Z5W01OpOykB7ngsX3ctTkyRlrVwDpztMLnnlX1ywXTuV5SXBUlCjjD-2zkShlY5I_Iyfx7lGSna7ouWMdyQtHOenRpHALJjhawELzaYXJVq0A0569QYAOS3K_R1AVCjIIvluiMeW8m4ACOKZLhKZ725niTih6AlZiAWLIvEzPj--4h_IH9eCC2tGERl5461g3Fv5whWAFGMvpPEbAQKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a860d22dd.mp4?token=H2Dgjr0mS6rb0LKFUcC_JPJtEjg95MRNU0M4oAOQBLMbqmEY8BvNhew5DaN0IbgucbUJMfc10Zlp03p1lVw66a1t9YujDLhgfu9b1LNuIqaqrj1XC2ZvSWHa2iMsw2aGo-Z5W01OpOykB7ngsX3ctTkyRlrVwDpztMLnnlX1ywXTuV5SXBUlCjjD-2zkShlY5I_Iyfx7lGSna7ouWMdyQtHOenRpHALJjhawELzaYXJVq0A0569QYAOS3K_R1AVCjIIvluiMeW8m4ACOKZLhKZ725niTih6AlZiAWLIvEzPj--4h_IH9eCC2tGERl5461g3Fv5whWAFGMvpPEbAQKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
⚠️
اسلحه به دست منتظر آمریکایی‌ها
صداوسیما: مردم بندر جاسک به صورت خودش با اسلحه در ساحل قدم میزنند و در انتظار ورود نیروهای آمریکایی هستند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/101998" target="_blank">📅 16:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101997">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vZhVTLCRbFKUgcfc3U0M2i1kLQ_t_HKR_5iJxzwZDnJ0ehvy-20Wc5LxcigAv31rOx85kxOUYG1rZ7HSnD5BgaYR72M_fe8tYAmO-dO6-DFV7Y0En6iN1Txl31TdwA0LN9k5RD2HyO0mZcstrQQ5Iu7LKG6koGqMxuaSaLxlHyezXMtpGsGrQg-4X4K3CH-LkeY0bKOgZn0YvRskYkfpGv0nAsy8E8_xewZ_CZ8KnXXDtwttlNJVfzS9QIdEzQro_H9TuINvSmjMyPlQfml6HlrYrzUmEQfb8zDMLSRWBX17az5Y0vYl4M4rpn-MM8VbBYZHB_YjZZQPne7mYCUOQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیکنانی که با همسر یا پارتنر هم‌تیمی‌هاشون وارد رابطه شدن:
🇦🇷
مائورو ایکاردی و همسر مکسی لوپز
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جان تری و دوست‌دختر وین بریج
🇩🇪
مسوت اوزیل و دوست‌دختر کریستیان لِل
😀
تیبو کورتوا و دوست‌دختر کوین دی‌بروینه
👀
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/101997" target="_blank">📅 16:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101996">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58250e2a71.mp4?token=vCpCa60uyaeuV6YKGfgGjS7v3o9vj4gssHVgz_5JYE3C3GS44GfE04-E3JvfrA0vuodzYli0OvNHq5n7-ggU7HGcTlMVrVjNT8rvaUkRskdpBeiRc6QfvUBV8zLyCzF4uzIh0ZX3PVaTRWCzsBdAiJsDUqEB_82RHuEpuXDDQ60NU37ox5WjUkvoGtvo92LeuZf9k75b0fgoCZGft56xNsDrWKTQRqw-5GQlMeUgBq7kn9V3WaYQIjU9JW7Vq_QJgC_iDCu87FOKz-nY4wDAfMNvaFQHHJ1KEXAR6kO1wUs69CA7ihXVsgftqI6EbYXWDwsPwy-YjIkBHZ8XvoXJdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58250e2a71.mp4?token=vCpCa60uyaeuV6YKGfgGjS7v3o9vj4gssHVgz_5JYE3C3GS44GfE04-E3JvfrA0vuodzYli0OvNHq5n7-ggU7HGcTlMVrVjNT8rvaUkRskdpBeiRc6QfvUBV8zLyCzF4uzIh0ZX3PVaTRWCzsBdAiJsDUqEB_82RHuEpuXDDQ60NU37ox5WjUkvoGtvo92LeuZf9k75b0fgoCZGft56xNsDrWKTQRqw-5GQlMeUgBq7kn9V3WaYQIjU9JW7Vq_QJgC_iDCu87FOKz-nY4wDAfMNvaFQHHJ1KEXAR6kO1wUs69CA7ihXVsgftqI6EbYXWDwsPwy-YjIkBHZ8XvoXJdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
🎙
علی علیپور: حتی خود پرتغالی‌ها هم کیروش رو گردن نمی‌گرفتن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/101996" target="_blank">📅 15:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101995">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MCl0yD5-AiPBtmdx2rTAvrYVTbwFO5GjHddPo83TtRItdBFCZWosAUS15HfswCS9gfzJbUsZSs8y-GJ8Ka6E_rDyH-7MdUkC1Qlr9xwET4OWTHcPo8jXfaFkU5ouPZ1IEqI665k-KgHalAw8y_x9Wb7z85QxJY5yu34GB87VLpJ-2pT-MEoE6dCGrrT7CWDB7yTh7c4GEo7bBgU2HGOE6_iPgrZeCbvnvzPajLfLukL9LCA6TuTyCZpW_BHXAudUdiY7Z3LaeNBmVyYd-Rkk7PcJeQ5qf0piBtpqYbl0P5PeSRyZr2ZImN0tuYALV0igf4pTor6BhRu1DY9je4tH8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📉
می‌دونستید؟ فقط چند هفته قبل از جام جهانی، اینس گارسیا، دوست‌دختر لامین یامال، حدود
۲۵ هزار
فالوور در اینستاگرام داشت. از زمانی که با لامین وارد رابطه شده، تعداد دنبال‌کننده‌هایش به
۴ میلیون نفر
رسیده است. فقط در روز فینال جام جهانی هم حدود
۱.۵ میلیون
فالوور به دست آورد. همین رشد انفجاری باعث شده چندین برند بزرگ برای همکاری تبلیغاتی سراغش بروند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/101995" target="_blank">📅 15:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101994">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🔴
فوری از رومانو: لیورپول در حال تلاش برای تکمیل انتقال بارکولا است. این بازیکن تمایل به انتقال دارد و اولویت خود را به لیورپول داده است. لیورپول منتظر اعلام قیمت مورد نظر از سوی پاریس است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/101994" target="_blank">📅 15:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101993">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UV4-cUcAJKS9DtVuIulEs3E8fK2tG5enBC4TxGSdWXWuW3njexkW67CqiyipoEGKLSsRlblcyNmVcglRqAY2hvKXs3jv6n1x2NyzFNq3kSEctO9ppmwHW7wvWroqtz493GG59Ts0wesgVEZLOdlh2I8gvYCCgxuKklXhD61e4lj-8oQRA7Hvv8S9qMP3SZYQguRywgYhAZDi2K0mZPZDntRn2fKnZv4fEjrm1TkXH_RH81nEC_BPExU2uxcJ-mfWxHhONF05bVQEIdrZJ6w0BwTM1zZ4xKfmD3PodbrduiGtZ2pUqLpQ3Xrlc8c3TK9LvkbHKcsHEKrJNBcAUnlF4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
فوری از رومانو:
لیورپول در حال تلاش برای تکمیل انتقال بارکولا است. این بازیکن تمایل به انتقال دارد و اولویت خود را به لیورپول داده است. لیورپول منتظر اعلام قیمت مورد نظر از سوی پاریس است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/101993" target="_blank">📅 15:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101992">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45e9d378eb.mp4?token=iKctxhOB2aUcgJ8B29KAOSXaQYR6suJXbdgOQRZAf78mTqXcs-fBAA1fiKXzThplKm0V39vyXnhgasJGOoaC4miDiq38L6Mb2EQOTu77HqzaMzqiqLEo1mzBZKwvgl2-wz0WTd64LcJay3KdH60B5TluxjU6MFuUPcA8otiNanCyXhsso-YZGKYHwvXWsytRyBATcTcMpfaDlbtGw13QRsymBLmdyPMKHop6-fBgLs0CcOkqCvyCsreMzfKAr2x_RT6LKdv-dIWBfRwu0yN2ns64YBYsuxWvynFUNAI7Sqo1alSofcmOFdRL6zYDSnjxHip4p2tGk-kZlSkvnZvRVi4B7ZHzfouOXC3RDJ0bPqbZXbqNueBssxs1yLWXowYggfSqwoggv7xvQSqrYv5KvfDcIggvUvwhIQIL12l6nzTMmL8vKpV4xx_-3Nr8sB3gEccYBsr5xtUuJJd9IHCc10qUpuUmPinGyOp_rNi3ELkbOuFVVGsJkV-4lBrs9pHjDC7TU-mxyTXxPQ9yH-_frDDQI5XjzICt3v4ZuXKPx-WTQGJuKea5_nCNnsvzMWjL_wCZIGwM0dEHSckWAgFs1A3Fv2XBkPD5kn9hNnCnSL7Xz0Ahqa6ImYD2pufEF_kexms_KMLuAd5mw-CA59tA6V1QUz-hGedvd5c0O8z9GH8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45e9d378eb.mp4?token=iKctxhOB2aUcgJ8B29KAOSXaQYR6suJXbdgOQRZAf78mTqXcs-fBAA1fiKXzThplKm0V39vyXnhgasJGOoaC4miDiq38L6Mb2EQOTu77HqzaMzqiqLEo1mzBZKwvgl2-wz0WTd64LcJay3KdH60B5TluxjU6MFuUPcA8otiNanCyXhsso-YZGKYHwvXWsytRyBATcTcMpfaDlbtGw13QRsymBLmdyPMKHop6-fBgLs0CcOkqCvyCsreMzfKAr2x_RT6LKdv-dIWBfRwu0yN2ns64YBYsuxWvynFUNAI7Sqo1alSofcmOFdRL6zYDSnjxHip4p2tGk-kZlSkvnZvRVi4B7ZHzfouOXC3RDJ0bPqbZXbqNueBssxs1yLWXowYggfSqwoggv7xvQSqrYv5KvfDcIggvUvwhIQIL12l6nzTMmL8vKpV4xx_-3Nr8sB3gEccYBsr5xtUuJJd9IHCc10qUpuUmPinGyOp_rNi3ELkbOuFVVGsJkV-4lBrs9pHjDC7TU-mxyTXxPQ9yH-_frDDQI5XjzICt3v4ZuXKPx-WTQGJuKea5_nCNnsvzMWjL_wCZIGwM0dEHSckWAgFs1A3Fv2XBkPD5kn9hNnCnSL7Xz0Ahqa6ImYD2pufEF_kexms_KMLuAd5mw-CA59tA6V1QUz-hGedvd5c0O8z9GH8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
لحظات خنده‌دار از زنده‌یاد اکبر عبدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/101992" target="_blank">📅 15:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101991">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d63baf35c4.mp4?token=nC5nkmn1Q5z92_Jt9MIK0wItm5fFwKNVvJBK1OrG4C7zoBUhgctg5XIkAlEJUcFy9m5kgkgRxKziDpEE5FBVIka5v0LCZTTY7QRb7zq8GiKjKisDmnYoaKeTFUgH-jTG0GFckfo9U1eIeHbsIWy1jDy8cHzRY7qqCNm2vC7d-3T-CacF0FBRRRW1sR_hm2XXWTyu6x_ZKalX22rM8YujoZaJwP0aC9DdsefAMuFgO9lpRKfVRgTgi66FmDLnWuP8LIQWHKFGnbPpwFVpBii8ygRwRWpIYpAJl2_dJPwNxwmPMZLw-pOTeJ0qo56SlFz-XuJeX_E-FzfJSGHo1ins4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d63baf35c4.mp4?token=nC5nkmn1Q5z92_Jt9MIK0wItm5fFwKNVvJBK1OrG4C7zoBUhgctg5XIkAlEJUcFy9m5kgkgRxKziDpEE5FBVIka5v0LCZTTY7QRb7zq8GiKjKisDmnYoaKeTFUgH-jTG0GFckfo9U1eIeHbsIWy1jDy8cHzRY7qqCNm2vC7d-3T-CacF0FBRRRW1sR_hm2XXWTyu6x_ZKalX22rM8YujoZaJwP0aC9DdsefAMuFgO9lpRKfVRgTgi66FmDLnWuP8LIQWHKFGnbPpwFVpBii8ygRwRWpIYpAJl2_dJPwNxwmPMZLw-pOTeJ0qo56SlFz-XuJeX_E-FzfJSGHo1ins4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
دستاورد دیگه تیم‌ملی در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/101991" target="_blank">📅 14:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101989">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R1B-J5HcP0fSEE7OpTirCQDyQSLoY8RYsGSKtJtQRFrCVJIYqYE0U-969YMa1i9r1rQHgL9LrBYfwhQQ9nTnR1CZYTnHPgg4cEczwxrwm0nyOP2yBcPVDCBTjYB8h7CaMyhIE0M0q8d2nvq5CgFiuq14xgmR7ABbSNHPcRujI46f_o8EbYDzJK69BonQj1GI2tjwjSKQTIwOO2WVKIIrjJEI9x10aQxc3nCL1mesAU7soiRvg7TE3XTzl01-Ye445jjYnAgvEAzdqMKGaIIyetMFw4jKHGCaiuTEN7Tg5xzruI9Bc_OWb5qfAv8x6aty3kdeTw18uD0sMBb8JupyzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IWwsZU0IoYdGCPbrT_zknRRycv9z3gy4ZBrY7hC59D2A6eb7qIlB6ljO07nQa1VTD2pTI9JOHoOCAl3UESN_5gHJaYv0tY7bNuq-nLOrlJQpwmbY2kcd1gGyDyyFZfi1bd-flz77FjUMetx7KygNLJatYfMN2o7kP9yfqu4i61yOfbvyap1Tce2zUkmxylGqqq-XaJvt6Ufd2ORviG2d9kphG-TStvvyEDFbcK_a3S4G4LuK69kXPeXssQFlfgxtkuIejIat09Fqe9qCiips9uGy0Y7zCt75e8v7glOoBRt01VXPt5_cWQvUJdvYxl1XVIbxIj8E5jka9t-T-YGUzA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
اینس گارسیا، دوست‌دختر جدید لامین یامال به این موضوع که گفته میشد باعث جدایی او و نیکی نیکول شده، واکنش نشون داد:
من به کسی آسیب نمیزنم، چیزی رو از دست کسی نگرفته‌ام؛ فقط دارم زندگی خودمو میکنم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/101989" target="_blank">📅 14:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101988">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/310ebc00ec.mp4?token=Hnx1ERfK-HhpuFHNLCGMM6rlDc9cqSU-mhth_IqMXDz5BkkEtXglraFjFfY9REglpQGVZ_fDkZgQd_g9IAOkfGWSvYPs5z6uZOslivEfEMirpwgaPIXrdWN0E3LpgeT_kl7O4nTM74S_mQJrSe2d5rDreSYAdd622mfY7v_4wGqctH9EybMfO9Fxh0pgugYTOmlBs0_ftGqXgsjVNb_Ta9b2EHVeBN3NlNXTHOvlvco1EdlCCNqJ9QRMA0ehNretuk-E5-Rt9pfb6SAl6c2hZpugjCWOOOKzNyy6lgQCEHJ3VXn8AgRXANiQ4sM8K-DH08659roYD5JuU7QtyaGCzTDQw1W1JE4kCX-2VbYIC6ikI7rwfZUnh2THeU1kmFO2mUexk3UAcpTCFGKJ_xXejoMkXjXq6rzm9pZBIJyXa2BL9482qY0D7YlRQSxXUn58G_v2veFC-jJ9DaynhuGqhpFv4haPYdJy3SPkbj_uKfynPX9-BnT-xiQQdKo6B6Xm0ouKaneO1umJ-TYugzmybAj6YJksA2RAFl3jYKdtdKc2rg6Z3ULucM61e1jOvaIBu75qwOShn_lknYnaRSZ43dQlisaiQXNfaFz6nGeJ77VcJp0h8CW-rDvjCr5Ce9YMI0MkrK20VDMG3YgPUf81Q5zAmFaOBP9Pzt354JR2Fng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/310ebc00ec.mp4?token=Hnx1ERfK-HhpuFHNLCGMM6rlDc9cqSU-mhth_IqMXDz5BkkEtXglraFjFfY9REglpQGVZ_fDkZgQd_g9IAOkfGWSvYPs5z6uZOslivEfEMirpwgaPIXrdWN0E3LpgeT_kl7O4nTM74S_mQJrSe2d5rDreSYAdd622mfY7v_4wGqctH9EybMfO9Fxh0pgugYTOmlBs0_ftGqXgsjVNb_Ta9b2EHVeBN3NlNXTHOvlvco1EdlCCNqJ9QRMA0ehNretuk-E5-Rt9pfb6SAl6c2hZpugjCWOOOKzNyy6lgQCEHJ3VXn8AgRXANiQ4sM8K-DH08659roYD5JuU7QtyaGCzTDQw1W1JE4kCX-2VbYIC6ikI7rwfZUnh2THeU1kmFO2mUexk3UAcpTCFGKJ_xXejoMkXjXq6rzm9pZBIJyXa2BL9482qY0D7YlRQSxXUn58G_v2veFC-jJ9DaynhuGqhpFv4haPYdJy3SPkbj_uKfynPX9-BnT-xiQQdKo6B6Xm0ouKaneO1umJ-TYugzmybAj6YJksA2RAFl3jYKdtdKc2rg6Z3ULucM61e1jOvaIBu75qwOShn_lknYnaRSZ43dQlisaiQXNfaFz6nGeJ77VcJp0h8CW-rDvjCr5Ce9YMI0MkrK20VDMG3YgPUf81Q5zAmFaOBP9Pzt354JR2Fng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
👀
چنتا سوپرگل نامزد پوشکاش ببینیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/101988" target="_blank">📅 14:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101986">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dcZFtrwYxVbK8iHucfcOxnDHhJnlvgnd6CKbsLjb98CnC3GX8Lr4QVux4Spc1xfL_v1-HrLXQmyjBuVgSnusTEmAtwHB5heRnuYUncM6CEBqpB_wLo0ggyeO_ZSU2tiSfnMm-wsF-dbR3y4rLgqTFjRVvzQxiekNJRI8U6kdyzdP2qnhfQCeIG20_v7G5-5sp1UhQQ3ZrkpIYeJwUWSAZIdVKhnfYcQL9sm7KhhnmkH_4UJpJ8WHGeRoFgNd2wqFQvmAbzgsEzCmf15ZpCeWgBftKYELblzh5Q5bLFt-q5AFxAIwXP4asSmx69V5nUE3BENceOtBD52DmJFzXPb9hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ha4483M4oyBlwqpMgWOV0Km5ME3m85qhjtYVBby0HiDj74FPlz_GMLYCEgpN2epJA8vyU9RhXonIzAcUf0J4VT_T-n9cZBO3AoaXfzZM4t43q2jgKgh1O28ULLCfTcsUzAixhK1i5wsSIKUhm8eLOHTmA9ifdYdvhuVNeEEip2oSbwtGv3afbLUZU9rT1nv4Hv5TZG9TIsJwA2w9kqpAwvS0PNwZ1vfStiHaEdVCbK0M-kz-EXmoLuLUu_8AcBz_S971JQ88HJW71acTAWRxZGW1_lDu6LXgizgEdi104q14-piH0u3whfBSl6GO3oHJ6viN_zfqIaxXLDk6iF1a4A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
تاریخچه رابطه‌‌های لامین یامال:
• 2022 — سینگل
• 2023 — آلیسا
🇷🇺
• 2024 — الکس پادیلا
🇪🇸
• 2025 — فاطی واسکز
🇪🇸
• 2025 — کلاودیا باول
🇪🇸
• 2025 — نیکی نیکول
🇦🇷
• 2026 — اینس گارسیا
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/101986" target="_blank">📅 13:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101984">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qiu2jFVoMpxRrP9WO3SFA2Lfo7tGx4ZhDwkFO8kWVlH61B-_yfuRcP9kpWF11uqPxIx0rjKCXdgWV7qQHftwZULIYEac-luznMZDTDTZB2gDzphJJXdFVUkWNXbWmKhtP3d-eWNV3a0H_Trrf1_RCKKu1dKd6BYkWDwzQ0gGhB18rrDaWVSYzIM_i2IJ-0Rwa7JINTB6tbOnd58QQHt4BB-1CUOgCTrwjXt7ZhBdqqEptEOoxymwM-TRi3xlPG57Eb15t43bPF3NpekaPDig2nS3qmWNe7YYTpDRis06JdFTteuzVjeY5NE8dJ48HG1ZsjIiQrLyPsrLUO8wqOi4SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rt_AlDmAuD8E2oTLJM2DTRKcpnaf7i5-SBM4VsMz-_o-OytzQuNlhv4Mm0bt8VDL0DzqeBi-SKNEU2vHxzTJSnJdJrXtCKXf25gnn3CALzLeF2XDTvNqsRoS0Epq7xaBV049MRVzNEmpTQ0YpcnATpYpd01VOsL1vj_tCVsfG96JyODjUfgMa8iyEgNBN4ggW-0UTF9uBDkzTxLX69_zwParb3wz0aEQIpb28-U-voc2HObNSti0BOnWVsI8yqaVPjn0ItoUMb5BfdlLOlBAA9eqy8n7G7LOCO5-e75F8ws38no0fIsgvV629wGYy54_-Uti0p_ntqVJM_aX-st5rQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
جسیکا توگا دوست‌دختر سابق وینیسیوس جونیور:
این فوتبالیست‌های سیاه‌پوست فقط از نژادپرستی شکایت میکنن ولی همیشه با زنان سفیدپوست و بلوند وارد رابطه میشن. اونا هیچ‌وقت با یک زن سیاه‌پوست وارد رابطه نمیشن یا چنین رابطه‌ای رو علنی نمیکنن دلیلش چیه؟ جوابش واضح و مشخصه! خواهشا این سیاه‌پوستا فاز آدمای اخلاق‌مدار رو برندارن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/101984" target="_blank">📅 13:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101983">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
په‌په‌آلوارز: دیومانده به رئال‌مادرید تا 2031
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/101983" target="_blank">📅 13:11 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101982">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jVqzFRN3Klo1xZvFYDmJmsyM9siRhXT-Pnfr7zfzlAB7w-dKOcu-7MdxGalqJSL0b2TqXeP_3RHQ-4YLomMH42mkHyxap25k0GP5vAR4IfrykwauTXXHDxuY0R-3J2kotmujnbrFV9NEzIC7zgn7rY557_2OPXats51TdRcezkXVsFZRQyEpifH9VO65BcE8aS6AvTuGVvhxWRTstly6f3_hZq2xuKNtmOzf7XKSeJOTtkq2BN-ioztpaozjM4MLd63CbF-xrhX_39HIQ1uTcRRkzU7CNrTdJ3_20OCIbZw_5f1wcgtnLbKNmY2cru9JtSZPaqkc66e6enIZkApesg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
په‌په‌آلوارز: دیومانده به رئال‌مادرید تا 2031
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/101982" target="_blank">📅 13:10 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101980">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/INJQNgPvCZvE1vxlOstq_HizBMjcKmHiwOcYF7KwwavlQXnb8uj4jGbEaMqb6t1cWwClY0MVAf0FhjIzHC4l3CKMr-8e4FFcdhWzl9aqRDXmA-km-OQj_1ePVpqG6Ei_eW-5In98T5kAe9MbJduwU-JRZZ302LB69WqLDPgLU3LO5pBVpZnDYdR7cSrLDu9hd7bd_OcJofhkaVp-iIqXMzz7oKs5gmDaUzEjkKCaSkn-ontyQJgkWPbHkfKm3uDXy7dodUpPCboAwVlyqvxfGvsbTZC6Oozay96wlZFN9XosjXaFXkQVCOYxeAwlu1XEyXabYaoKBN9VKAwQknrTTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bwTGTzAgFFwygqGZ6TIK1-2ybs22gYMO8to4IYJvnxCiAm3kC0yobPC4WYaOxhj7eQJb39jXzlYFvJHZ_C97OYhVLvVbgHza7grNdYgXClg5dHK95ljUCYOglghRD6NA8mjWf7BFYMebWBPYzcdUZ_FDy5aeokQKZZ9cB3jG0Cr7Zs7MQSEaxGiFI1tEBC7Cm17sXMqWLDUFdXh5FSj4ATxSXNT6r-nOxWcXI9E-wp7X5RRiLKLIPvruJNrExtGQsl1wL6l3VPMEBc_ylTPyTBHsIdEofjuJBijP0D-_i54z6YclVuPn1EIRPPEfF6ZbZHR4NBY5d9jkgqSDxyHhgA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📅
🔵
17 سال پیش توی همچین روزی بارسلونا 46 میلیون یورو + اتوئو رو به اینتر داد تا زلاتان رو از اینتر جذب کنه.
🔵
🔺
فصل بعد اینتر تونست با حضور اتوئو یکی از موفق ترین فصلای فوتبالی تاریخشو رقم بزنه:
🏆
سری‌آ
🏆
لیگ قهرمانان اروپا
🏆
کوپا ایتالیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/101980" target="_blank">📅 13:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101978">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ODtARHaNxQr7DtBUzwknT6JHwOJBq2WBG3PvIMKGlaOeBem768Mk8zJBPsR1-Ja0Dke3ESpDqAUl9lMaLVkDRkYZMTKdYI5qCq8c6JRdF35wrehjBdsa1RJpgWnG7gDH0jjzQbmJ17zXUoVA3MG3BLnDTTBHiWoQs2E1oxlVwUaiyMDW8SyocxnFb7wYbrT7MmlN0CxOFdn2OjxrXOX_QP4ONMKk7NQ2xdyAfqDl1MLrT0k3vyFdw6neSzBMPgmeVxKnscCBcvFj_qavmwqjDDcqTVvlplhHFMfIISPdiM2zHXpslT1pmVGnq959HkLuj-y5W_4bAGIlRtcs7eFxaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VbFYEktkmVQLvSS1O_w5QdIIarozrW3eXUGAyNRX-W14sq1YhpzazZIsDTnvhB4Jz8xPSIoR0QhquOheX5blJVf1k2sbCxIZ_kbv0nvdJbeuwngVBm57Sq5f4zkICBR6NRiYTG9JlNaGJ-KiC0sKM7Z4hOVplUyXD2MO12gPbzzkakzV5-Uagxz1fc2bgO3lilv-7tKZJDiha_OQmXWIHRqQo94HpQd1RJrj6bblfsZvhsx1Q7chfD4SMiw9PRarLItsebumJTRcM0UzfhWrMkl9DR7aNcnOmBLUS_EyITeuS9ZdITs73OzY6yGuMpY5U4dJgXu2MyxJKjU7s0JSkg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
الساندرو نستا درباره غیبت ایتالیا در سه جام جهانی متوالی:
باورنکردنیه! پسرم تقریبا ۱۸ سالشه و هیچ‌وقت ندیده ایتالیا توی جام جهانی بازی کنه. وقتی بهش میگم ما واقعا جام جهانی رو بردیم، تقریبا باورش نمیشه. میگه: واقعا؟ برای نسل بچه‌های امروز، دیدن ایتالیا در جام جهانی انگار داستانی از یک دوران خیلی دور و گذشته است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/101978" target="_blank">📅 12:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101977">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KG4h1mMyuuZ2Lv3cTVDjuji-nTEWvcnWyREl4hp4ck6CRcJLtHFInRbdFkdEHI1qto29wPGzOAIv71DTwRmsIRjSrqNAJPcRIgDM9j36Gc3P7TJwgmTe2O0mIyjtfbG9H0FWR_rSfoXXyN7R6wqdmLMHDgnJAhCPzvF2Xn7OaPIE09D1JJzVCUW_ZlpmAEMeD8F2z-XORpwoUzz7WTsxChb3SFZ3OmWkYTLEMb5NO7dvyhTwFTzTuoFPyr0csKOJ0ShU1tC430hP8_pr8dPYdqJvPP4YaRM2tcJ6OSg57WEb_BOEaCJ9LP2d1sJEl49df9UjVHQS7g8TeiYXuE_mpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔴
ترکیب آرسنال اگه همه شایعات نقل و انتقالاتی به واقعیت تبدیل بشن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/101977" target="_blank">📅 12:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101976">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v84WRSuYkeAj-PI6O20SRJNk_p9xBvXhWQg35V5gsjBLHF3aCbkaxYNBfjIWDf14Y-nCcVsc9BJxeA1AwOq_kuJAujW4GTOPsO18A7lRubyZxjkxr-CXFULLT10yOHUeqHER9INFXNBNuX_bUJcSz70q14pjlgdEoS7IGrZ-tVJZ4jb-pE6gyzwyj4agGzMVcA8oeTJLMM11WOIQMKVquILi7XELJtlNyFWSbN_8q8Km6zeHZbXhAztS11ahSRpkRsbxv2o6gtmaiRGNIIgLhj5ZM2gmMB2aw52mlFOdHJVXlAMtbdQZA1jYDpF43RIn3khYFsn1ydNi8fhVunk1Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
طبق گزارش‌ها، بدهی‌های النصر عربستان به حدود ۱ میلیارد دلار نزدیک شده و همین موضوع توانایی این باشگاه برای جذب بازیکنان جدید را محدود کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/101976" target="_blank">📅 12:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101975">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ddfc2f853.mp4?token=enJUhpY0GIsIT0MAR_rIUpAZa8hcCi5szsmo9a1EipE1UNYtIe0YhNWKZbGg-irECFAo21bPKo43PJBR82F2uHv2_8fesSofCB1bcO6XwLzhP506TyPUr41xYvXaGKRI3ktF4bP3lQR_7yFKgl2yTH87PuSvvL6bID6e4ykoCMHudA9X5q5dtg9P2t5uDjbf-Ic3Kknfkh6mKyljB_NgRRgNU1O6Sp_TjaUxElJLoWR5lruaWG6THIZQmCbpi4fzJ9K8ATj8_z06FI4YIqlJq8VoEEgPCnhQz_Q4u1fMg6uYUdyboiJOLEiatEPd6ahvcMOapJfXn0rjgXD4Vs_HJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ddfc2f853.mp4?token=enJUhpY0GIsIT0MAR_rIUpAZa8hcCi5szsmo9a1EipE1UNYtIe0YhNWKZbGg-irECFAo21bPKo43PJBR82F2uHv2_8fesSofCB1bcO6XwLzhP506TyPUr41xYvXaGKRI3ktF4bP3lQR_7yFKgl2yTH87PuSvvL6bID6e4ykoCMHudA9X5q5dtg9P2t5uDjbf-Ic3Kknfkh6mKyljB_NgRRgNU1O6Sp_TjaUxElJLoWR5lruaWG6THIZQmCbpi4fzJ9K8ATj8_z06FI4YIqlJq8VoEEgPCnhQz_Q4u1fMg6uYUdyboiJOLEiatEPd6ahvcMOapJfXn0rjgXD4Vs_HJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
خارکسده جزیره برا ایرانه
✔️
خارک و سه‌جزیره برا ایرانه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/101975" target="_blank">📅 11:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101974">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eGDLLZ22HfzhkRKV6gh4ZmqCKuhtADOzSGQPWHmqWzZoiVkZEQ8RofIPgtUydYJsVFNILsfpG3ommRSzNHN2vEB5tzKQ3o67rJDuMXelcFSo79NLxDNnksykAKPSj5SkzaY8IRmdUit4-BXnr76vpIW8uL4yhO5_OL9nRxOVv0onVQDkWJNWM4WgH-gRYPo3FWRzivkiDRKAiSao0B-Gu0XC3Hu0V0xTD6uN-AX2p1ailArVzDhc1TrnNyaOFJzX_cpVzvXa2O6HhIOmqMGk6ZSizkQQk0rzA7V9JYfIW6_hhBJOSK9NUHQQIVvMR_EQul40eSULpSRBDyiXcr1_gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انزو و خانواده تو تعطیلات
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/101974" target="_blank">📅 11:20 · 04 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
