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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-05 22:22:38</div>
<hr>

<div class="tg-post" id="msg-102096">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wA0yZU_bjYgQrcImRTOsVWQ48FvZ-2SGuTpGQHiBWo5QjXX706EhhPAhjAFi8IxpcKEZ-_ajRXxA_bgnO4yfGhrpXUfR3eRXbjEn-iAFesmsqAPrilRjH09DvhD991E_NnGvOl2vYHmSWDAdaSB3gt9GdCQXJFafjv7XHlOo20A8vdzZrTL5tTrNWKiHJLZw8VQ-w9e7Fz-K_qqoefJC7BKSFT1ur9k1FmM4IwD0aB3mjDYtOHIGY-JlqwpWV7BEe8C1Me25Wcjw-Bs26HNBWy2_gMPXEPlprzef8u6onNKowK_DTGkS9qyJTxLb9WvjBczO_wVEE6VaFZVkDFvL4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
👀
تیم منتخب بازیکنان آزاد در تابستان 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/Futball180TV/102096" target="_blank">📅 22:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102095">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🔵
متئو مورتو: جان استونز در آستانه پیوستن به اینترمیلان است. دو باشگاه در حال نهایی کردن جزئیات این انتقال هستند تا آن را به طور رسمی اعلام کنند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/Futball180TV/102095" target="_blank">📅 21:58 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102094">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qW_cJnSrzYqdDbtD-fWJ-snZhQyYvQ7aYhm3IrigwJdcJg8O9pSK_x3UbXdLhxPbt9g90EMujuXWrPiWC5-BKigjPxpb9pfGePUyPCi-OJVgjxttWgsWtNID_M6l7m8NBkgkcij5bcZqdQk2gvTD8mJbuPEhvbUb47NCXBjuCvCtf4RaDq5B2vGLGUgxHY0Z5467vo_DY07Nbc2WIdLZhEOUbb_UEyZ4rpIEr4sJo7si_FafT-FELyLTKcHrs0tY1p0he9IJezkAoAamUJPJwYwtknQY1_fOO4LphkM2AHWzZcnoFyE5mOvcZSneLC1u_K_p88m8KFSmB0QsUHpgdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
فلوریان پلتنبرگ:
لیورپول گفتگوهایی را با مدیر برنامه‌های برادلی بارکولا و باشگاه پاری سن ژرمن آغاز کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/Futball180TV/102094" target="_blank">📅 21:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102093">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oQjs40IEYNXOK3vqVKyY0z3wsF8XCgxcxR2q0v0k-L-E5bVLa4J222RZJb30DyWo2fm8LaT9khDp93gAMl9IM2OWJV1OVyM95gUUeY0uqu7Z4_Tb0MR2sspmjkhDvmbrPTpIRifNKe1xahExr3eXyIwbdNGXeIcLQwhX90YMBHZfbkkB7WbjPk6pM3IjuIUAWFnk_uJM2xQOeDYFYfXNDf4TwfXIBj9CNVk7Ctd9zqFKqwu2y21RuU7X3by06BBycdE2gAbqswbKccUzKPAdQPY7-PjPwtFG7WwsW6AO43McBFm79eyio8fWNsiTBa7yTauRLAmeMiEPMWUWdmB7EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
رومانو: چلسی قصد داره جردن هندرسون 36 ساله رو به صورت آزاد جذب کنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/Futball180TV/102093" target="_blank">📅 20:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102091">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZhcB9WE-W_-6ybd_nOwmeBA4C2JqGv8tzmRoHY1UkgZPRGRwYG8PmV7v1o3ElAqEGRW9hLLTYyPv9z7dJj7Qjt2d6Qea7zBQP4pus8imlGx6EtBzH65jdS10PxerdKlMQgLvuwD7vWFxLXrQMu_Vnz2VLF-3wt_HqqZVpof_OjHGtgpKzwC_Mw_G7heWjESKv3hggi1XtMRwnKBeliFidULWPSwPqwNpI_TgHCZFu3P7OEI_yajU31KLxry1diM4UHdKOjpcwKmHrgnSFG_e_xo7Ueno0iGfQojGDyuf8xvwH2Cp7qC2cGyYPVXucJ-iU_Ru4b-eEVE0jvyW6idLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🇮🇹
فابریزیو رومانو: پائولو مالدینی و لئوناردو از سمت‌های خود به عنوان مدیر فنی و مشاور در فدراسیون فوتبال ایتالیا استعفا دادند.
❌
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/Futball180TV/102091" target="_blank">📅 20:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102087">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BEWTo3NM6WoKMVaB7-V02yR4uYUmmA83gSaZbx3nnbb5sXWskAL_QHouS61sg7krnybGkRdQrdcLLQHku7Bd1RKZGI_qx_LI1iGVZNOl46830Rf8CGZhiVwToZaPokA6NlBC7CjuaUQtsr3HuciyyX8Pkle3HlACjc2wcSsl5J1yyYKveduXLsWHvO5PMHMPt55qg2rW09I5t2EtZuV-sBFcOarBaXrBLQSgeqPI-MzXnNd2p7dvO0XxAZfC6Tw8GFrqpGfSJ7Mwh-hHhTq8bjqXD5rbje1g21AJw1kizhrPaIEU8_woTh3XVpRDuTA6rj5ODJbbMjSZ_0wPMsmGaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dnu-JOERf7PjaUTIG0kaE5tfHOOAyFEiIKI3m2egDRWSqDnm8VFTKMJVRODTmbkNHUFV7qBDLwF10c2mf90K3iUk2gQq94DnMyCaQr6SCDMN6rVwyNFKkzukTogZZyMReALRk8GcIYHbrTm9kcsVO7spW9esfp-TVh3rQnv2O9zXDg5ExdB2_g4C9XmCjdCujkIJWQ8fJYhMT6Rb-UX5MmZycJ69ACeKMcSgRTNkWufedpu1Hr2VGmDYkKEUJouj_SDPgoEnRglwTb-ECxJjlcIWdIoUyV7OVn0615faUs9HzYUvK9IDgLrPayhfoeb0nxKTRYsfgnV-E213DaODiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MbB8yRwn7hytYAYdczDSMLH4o26_b2obI01nd1CH8fSPFN7oBCDvMCezK3rVbXeApfcl_g-2Dyg43YuXkilhobHX3aPPo0Ytm8WmG4hkEhtkDNG1rJ4yQxbHgago3P7x9Bin49Yx_cnqSxQkwCB8kz99GNe5aTP4Ut1zRi51MPEmHE1JIP1jocPm5VIREYb9-un9cgTvvWusQFD9ZZhUAGuyy1flJzxJSlEjosTvCWqlckEcT7gvDlp09DhRcvpSx3y016VLR0FYXeSHPcojkUiIsPF2fMgR6_mTQYgR1pEo1HIJZv0Yb6D_vJ-ARifjkxtzudPqTOzKEgU9f2CTng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sjbNAPQeFj--i2Y5rCXYf0uihH2yGe_Qpn7ANUjDcRT0AgpVhqLFFxZFRf4aFlOSXvTvDz0_Yu7PTwWaMU0Zpa3Zml9TO9Z5rQrArhGxwsoLdwRPAPYW5UwwE3hB4YuraJehBXBbaNptGC_IrPbxwm_fHHfolIkvAr_cciw9D__KDijeZSf4gv2fES-KeIM0igK-e9YFnBdw0hjwsw-xTgfI5eC_ry1l54vnulyPtwibHFd-HYMC4S7kQg2hTSEvQNhu3AjuYhCfqGiYKF9YIrtub75_gkj-a10nl-edYk4RHsiczDSxfirQpjuTRu5-I8cp08EsJRnRlKxPt_6kTw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عشق و‌ حال وینیسیوس تو‌ جامائیکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/102087" target="_blank">📅 20:31 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102086">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tVrJ8-aq1pyQFk_g7_eEVU9rQ4Nzt1kQkMz1TR8n6grFFIt068Ig02rD2UbXEUwWwdYr7OFSHe-lgDtYvVHm7PljbS4Qk5sXJfQeiJMEr1AdzjAkZuJabNLwZIOoPn-ZgL46ki4j3Dp1Z4jhPqIGrAgVPa6bbZmdeMY4C3NmkZrZm8GPdb5MigvGbQmYh01p3CyuIuEInOMRjKvhmy8gDU6ye1GVPtChM921n_wJvGcB4blBBDlpEms0OtcYHL-4y5iEc5_fraH7jGdGL802GTxyhAV6eedNppzZc-zif0tpNdT1OmTbtPIlJ8G6IYNFhSfdWgbXkcYLlWn1GZTHAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇷
گلوبو برزیل:
سانتوس قصدی برای تمدید قرارداد با نیمار نداره و این بازیکن در دسامبر جدا میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/Futball180TV/102086" target="_blank">📅 20:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102084">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oWHam_NetwC-s1mGyBF2DzN-NLqZgmBoO_yCoRUcGiwkcAq69vNj7O0q_z6KERzCc3pfwoRyneassThyjjXvJmxnPbsGn_zh6ffb3xZIniVO9ljRTUFNAL_QC4CiwzpBdc9Ead4zjwIrjl-Ten3oG17oddLMtzw9MBRv8t7u691xSaKy1doKIFP4Lpp3AEn0Tkaa2KI61hFgCfQimDrB1LsYwxyKZFkJ8P-wpvEpVXSZT38Z5dxdBnmoiueVjuooA_hrq68rzt24kKOSuxPMV3GPjawfVMnVyk21kYABVGeGVreVOTREZQ28nfp3MTSzZxLPDJSTtX9mmj1RbBup9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LBL75KG8JpU6hE0f1JJxiJjb1kdc5pvWRgnb4ViIP9k5P44oSqsZUDkIdyFm4VcELMUY4FV3VcIel_4VxHB1RR8u2wVOlYGfsIWT9cpiPXjuyJF1xCB4CHMkWCESeeu1Ks1go526cfgnqqZZSAdV-M1EUrd16aQhlms2koMt9HZSbOM6g7jI_45AKlk1guvOnxU9JMEa0V897doZRylJwXLjlk6W8noYZbQbypCiGrMWapZBSqmPn5vBotpVISZij5v4vkV_8SU7TlXPXsWQyM_NX8NJBhCzHKsF_0i_--IzuZtjTDN4AdwZq5KhPB8r_0k7QCWgwj1f0D1gdRQGJg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
اشرف حکیمی درباره شایعه معروف طلاقش گفت:
اینکه همه اموالم به اسم مادرم بود، هیچ ربطی به ازدواجم نداشت. از ۱۸ سالگی که فوتبالیست شدم، مادرم همیشه مسئول مدیریت پول‌ها و دارایی‌هایم بوده، چون کاملاً به او اعتماد داشتم. حتی الان هم قبل از هر خرید یا تصمیم مالی مهم با او مشورت می‌کنم و این روند از همان اول همین‌طور بوده، نه اینکه بعد از ازدواج یا برای فرار از تقسیم اموال اتفاق افتاده باشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/102084" target="_blank">📅 20:13 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102083">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/102083" target="_blank">📅 19:56 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102082">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QdHG2lJTESeRDGSnFr0Fghgst4M0yjENYMN-NwMnPY59nuBQY-mP1XXCtdwYoYLCbaluSTH0P4yspzeyeC_jEA9v0kNVMiGem-YbawMHkuLHPDB3xZTg5xdUW9hnPz8LNx6Um1nfuz1g9dw3nOxyegJSOvnMUcGjDJcsfWDsGp0fDd3xrOMvoyayqVApJSLji-O7CuzpTUaPBpgSJhPJ5UAKttHiLhv9nmXf0Rrbcv0NxTf1MvzVIiaEe1MIS3OLr0xQkacz80otnqSq28hRGXlMmHMAkfUOCVDrGI1Xa0P44KqEsBcO6IaLDlRLvgIsWB1GncogBRG4Rofca2YIgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
قدرتمندترین باشگاه های جهان از نگاه اوپتا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/102082" target="_blank">📅 19:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102081">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/102081" target="_blank">📅 19:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102080">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
فوری ترامپ: به درخواست واسطه‌ها ما در حال انجام مذاکرات فشرده‌ای هستیم. اگر این مذاکرات موفقیت‌آمیز نباشند، به اقدامات نظامی قوی بازخواهیم گشت. ایران فرصت کمی برای توافق دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/102080" target="_blank">📅 18:49 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102079">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D7ooaVI_DvXbplMBM_mWIcSUaU5gp70ZrlGnwfejtpS3aK7AXhdlkoqIjZA5G6EpWHLT87iTRchVuHWurSY5KS-zAHwkynxPDzQsTT50lxCFUhzciut0Lu5135VCbMqFtNnDjX7h87VKefvmutT325_oJAeKgOUJd0UQImuNLZN_emiLSuYRVq1zc5bTt1VsiizA4ITp7lPzJB068tvnKqzmdOic4hZL1BaMvFSqfBP1_9jV0JKvzM_mfLu4uEINk6WYofq0L3lMIGvT-Z0Ust71L8k55HdCBU7MF9Hj5k1YNbKJdOSgzVyD_vgdxXdg9bPvjG6-ZH4g2SLrCsVjkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
👀
چند ماه پیش الچیرینگیتو توییت زده بود بارسا به بازیکن های بالا نیاز داره، و حالا همه این بازیکنا رفتن رئال!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/102079" target="_blank">📅 18:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102078">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ru09_HfwE2SPkORjfDJSIa6ce_MJooCx5CijpBlTU0ZHmOCjLcYmEYnOkI_kZZQHvUdI7SFWTDoJCQo3VE08ae-UU8t0ADsHcYp3K_G2aO44KECshjiJSgTFm396yIukUVv1o2KDqRUu-iSGt1paqiri-Z_sUm5-ockCsHsEABPRXh04GtsdiJV85LNcJ2JdezcTaj2T-QbvKwvVYcd1CHM3tgh8DMLaFaKjaiFLJdt6POkNPGDO15SQShh6EJAEj_SfIzwAg1KDrG8emK9N2l4_J0nCa5vRAx5DWCsNFIe-q0b1gyfPFlfx296hza_hlmlk1t1TsuqbfvxWSmO3yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
امباپه:
ازم میپرسن ممکنه یه روز سرمربی شم؟ نه فکر نکنم، من تو تجارت مهارت بالایی دارم و میخوام که تاجر بشم البته بچه‌های تیم میگن تو میتونی برای ریاست جمهوری کاندید بشی ولی باید بهش فکر کنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/102078" target="_blank">📅 18:13 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102077">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/102077" target="_blank">📅 18:07 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102076">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/102076" target="_blank">📅 17:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102075">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/102075" target="_blank">📅 17:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102074">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/czCXJ5f93YtMacoNjSm-GhMLzXLbzFewc8I0jdf4mkFTQxxgFycrXrj6KoqnqRYBE7SPsOQAECgY5-wEI39DY4iwMIhYCWPqrCK8TNqbx5QtJnvdZ1tCH6jF95p2xEwn6W17-PM8S-z7ZZd6RbUaMJepjdLqodPx8pygbz-WHhGTpttLNZaffrc-OvsMtY6VuZSLL_U53CGJ6VAYpapbkdWXDKlw9cZkL549WEjz7tOcZeOcmP0BzE6cG8khjnVTrI_T0PdOu4sCoJWN98j5zPJWWexiB5a3gBf5QR0ZDe1Ph9aN9by37kvRqZg_dgzWXCm3JeCmUXWDm9VTMK6moA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فابریزیو رومانو:
یوونتوس و پاری سن ژرمن در حال مذاکره با سوزوکی دروازه بان ژاپن هستند.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/102074" target="_blank">📅 17:07 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102072">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nm6Igoe33qI_V3q03ogwEOWM5hwbKN6mSFLe4pvbYhYf4aiCEuJ9GzB6sAHojQ3U-QHy0ZuVfiGjLY-C1izF6AUuui6DIFjkNtjODxHZO0R9RC-eyR6m2alrUJ26mON6pRYdc8ytsJ4kK_jQd5wvAP17CcExk_MaW434dsWEMxAmPG_HxkJjlVqnKr90UlyL_A_7NBZZ86v-HR9SxJuSEyfKiXxvPDNxnf-KRPvK4niviJBGM85Hg6ZqgvSHdxifUiPQqD_lOYw-oAIql0P18_dbRu0RogJKW81Hf4-o1FRa0GPhH6ODAKyVuSiL3u3DKhUM-7LwzGSH3mlCqtqR2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qdANBG0UT5YHhq_refDmi7hg_DbiNfRTqZPssIOELD5rlsSlJPFdoIw4gSvmgWsRnopNEAWNrpgJQ8T3eLkfN9ys6OsfWWNemJTd2GPUkCRbPqxZcPO3xFMtyc10xVSxv-8hxdLwa5h27j4yq417K4oVlF8tLk9wJ6IZ8LJwVUm6pJafufmA5TGevCA4-MPEg5j2wJuFRJhuCsHBjK3VjAquHQiayRiBtM7rAwIbf8BhNKDSpGq_eX13oxPUELAgo-bs8VbhaEzhO9HHWyhpdZpaPCibeWhacC-hzso3qnGQ3P6iP2RNKLsExK0XHJ07zgkVmiIpWsPtDjgdoDAExQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
اشرف حکیمی درباره بهترین خاطره دوران کودکی‌اش:
روزی که رئال مادرید با من تماس گرفت و من را برای تست دعوت کرد. آن روز بهترین خاطره دوران کودکی‌ام بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/102072" target="_blank">📅 17:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102071">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vy2JL5U7tDdGJ429KDWQN6otYVponUOQsSSt4YFQDa3WMOjQesB6O3QFKo75Pl81T2Vy4stjr6wtQLcCqmMfsibqIRNQiL2e41glUtvyL4y4VbYP58weK_Mbtp0oITBmBrnjqPcBzfNKeCmTWoP-l1xxDPuY8Gnhz11Obti-CFeznb2eBylt5RHERAeINU8C5tegaouWMCIi0uUGzPsl78DkfZefC5SVfF2WmAn1E8pqqA2a8dSz-aqUCsY_f-TIrxHLOVLqzBaEJByk8NoyEz0oShxeSkySE4vqR-L7RH__WNgnjj2D5aFF6f8DGSQAPaakwicVMoFxr3BkheWGMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حضور دیومانده در تمرینات لایپزیش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/102071" target="_blank">📅 16:26 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102070">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3120e668b.mp4?token=pn1QmsvtjTrok7mgIEovbSmLeX9yyJ_0JQTsxAtVWn9Zv-M3pZKEOHR7P4jqK7DvquMxQ3WY2JS16PtLIekMOF4fACjhapsf7XQ7YK-HX0CFf-Z7Y8HBtUQjj1iXd_bpTuh4kOYoMW0cHLgNxYOGVr-9ZjuOl4SVcTo_QqPQKs2rvo6wWTjnv7pWmR0uI8p-ZsOGvOPFfO9poXeYh_pW5R-61P1XkVdP04fssYWKAYRCgI60IF_cHNf9_gjZUShf-kdM4trwBScWSGO1XxPAVxh3lWmoCMGqvQaQJ549eR9eOKXhaMygYuTFc0FyzDvhbzOtofXXNPXzmvyWJNpRtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3120e668b.mp4?token=pn1QmsvtjTrok7mgIEovbSmLeX9yyJ_0JQTsxAtVWn9Zv-M3pZKEOHR7P4jqK7DvquMxQ3WY2JS16PtLIekMOF4fACjhapsf7XQ7YK-HX0CFf-Z7Y8HBtUQjj1iXd_bpTuh4kOYoMW0cHLgNxYOGVr-9ZjuOl4SVcTo_QqPQKs2rvo6wWTjnv7pWmR0uI8p-ZsOGvOPFfO9poXeYh_pW5R-61P1XkVdP04fssYWKAYRCgI60IF_cHNf9_gjZUShf-kdM4trwBScWSGO1XxPAVxh3lWmoCMGqvQaQJ549eR9eOKXhaMygYuTFc0FyzDvhbzOtofXXNPXzmvyWJNpRtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
عاشقانه‌های رونالدو و زیدش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/102070" target="_blank">📅 16:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102067">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/orUoyUrhagI10YDYWkyYeyQMy0kGQj3JrY7QTNQcyFVnEdRXezLAoe-Qlxr3KNqhjG4OBO9U5jl80Q0arc3_7CB06Eswpr0FZqeGRnjdcw_avDn1p_a1TEQoio0yq0yVeed068kW4oZYmJKj7Um4U2Oq0hBmMSmTWjkAgckyCsLpvm0RLZ8zXY5GgkmSjPkywXSnQ3QlcdZEihnYq0H_tDuwaSmnAA7-F5Ry1rprmFu0Ro6IHkQLz7lM0_p-Dxo1q0qVHPkwtYUxpLbtK1DFMspu44SSZNvL1eNS_Cm3xQBBZ124VLWsyHYWILx9qTmUB2SXrSys3X0i_pDiV2QsTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hz0DKsiVEbL-yb0JqYu3W4rWGK5xEjTRd5cyhUGbvHDXivqXiaFYxgZ3BXDKE_WKWZd_44ugE-aHwK3kpt9IlI2JuvexxCpnBFhz9NpQsFFci__hn1pSLcHtbvLqndhS_tWumEigkJM785xzz7eZni0uFB36vihBTPs8Mjq8p_NPN8M2q-_5lLy1ttjeZ2LJ1AOJRccTrQi0TrY90Uq5XhLFIi1QK00Z0vTxAyCq3aWlgLn_hLHhqbp3lg42_CHA6V3AgkQw7JD0L95qOMgiJR2QMa3bErIW_DgTBNts4vQqORYVFVBfd36deefieQkf6cUgCtVyl33fyw6XScEyhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A4D4XFOCDkFaGoVzJOqYAKtBUsi4pFNlCASqCmqlUqtZvFOngq5M33H7ZWE-Uu6wGnBtJB8aevnQYIcbYPzYKXDTghTMccZkEEuo9SZBKoaEazaVvEwE1pt-5afNaLGwIRdQnytryqka0WJFidRF21qZQrGYgp6_-JJjOR6YMyj18e-1uFBCo4sbKrbmuIetiG9s4TFpPDdv_eYJrBYb5JTesIheLMmv41cZEAgICGrxJes6OI9dDpKmPk_tfeRhKXmLSVG5qNj88kcVpKi5eUa2w8j7IOvuqyxmtU3aavJjHQRen5Kav049cV_E5n4Y7Kh5irTiPNVzJL5IIOYIRg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ایشون که تو تصویر میبینید مارتینا گونزالس دفاع 18 ساله بارسلونا هستن؛ حالا هی برید پیگیر یامال و رافینیا باشید درحالیکه اصل داستان جای دیگست..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/102067" target="_blank">📅 15:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102066">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
‼️
انتقاد شدید امیرحسین صادقی از مجری خانم شبکه دو سیما بابت انتقاد از قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102066" target="_blank">📅 15:04 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102065">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102065" target="_blank">📅 14:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102064">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lwl5GwU2_WPSyeLM1apW0RGYIAmjIzoaG4Y9cZECh5E8YhcZu2p_QJAwTHIefPEpGo93op2Y7ttC3Hjm7PJvTlo8PTEFT6fa7XkTXkBYkROryu5e7EHHSnrHA2G0XykKfv5iqQv-5_5s9rZ56B-aU7xvHiTWfU1vUte6m3ODBacuijZlYY1raeMXkU_Xy3kUcJ5GjEimO7KwJXH0Yzfh3Xqm62odUxpbX1GAhniR385L6ngj6a_KZpqEfOzthSCSzjoh5PvtUpzxoLM2FFt4vWL1l8nUA67zsgjgST0XmoCq3liUepDph3WatTu6QqW5qYxmPEqAmhHaBXioEP0i-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فوری از رودرا (ESPN): رئال مادرید نسبت به احتمال جذب رودری خوش‌بین‌تر شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102064" target="_blank">📅 14:47 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102063">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sQUrjA11MZubmEyqcAn4iqMlwLNQvajPRbX9M_V7uKDvWYXrwECak709F4RRs0vntqirshjMv3V2OcMjQa2cvJGxJeKipBYXEdNA6dJSkmy0RP6-iIYJXmV2uCzrNEKCB189WM7_-FcS5w0NeUeo9tQ8zQebRmlq90c4KcvkdzVCnT5CgiGp15Uryn3uhGJMhbs76AJA4tw4FvJwCicuZCzjiwyEYO3H7aF034MWpsT8vdfdNR7UAuhSLXl2qutA96yT5SgUe_lXxo9ZOW2KzgglrDMrtZ_TmMw9VtdZCe9_MQsn1VDQQR5Ougj6OrBi-S55pM4nQYcmEjruynG2jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
اسم کوکوریا تو لیست رئال  برای لالیگا ثبت شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/102063" target="_blank">📅 14:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102062">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sChJWF5oIqWhzwWNzfmoEAPh0zNCaca8H2dbM9QBESmABJVxkZlWLKFD-FtaWuTvmUeoNUG4zRx4oOlVMmUpX49nhFcTk3DqAR0SvAnJxmdZUCWb20-rhQTf-V8oft7SFWCL2_AZjGjqLp-_XZAkEQj6iGdg7A8v_-mmyCoIJsbKM2_IjZSTBRQm_yNpRMus1qnrlIjCX6FfdYatryUaWDSWwyxvMV9rIfftolJKGtke87OvNdR7CE54OlPNmizb76Pz5SnSK9G5A1SCyNqnPOSeGEhVX29zcZM5UMXXr39km8oSvZ0IPIbVjEaZfCSXoqByPKu19NKUdBV1qaxpYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
👀
مقایسه عملکرد نیمار و امباپه و هری‌کین در بازی‌های ملی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102062" target="_blank">📅 14:03 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102061">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/102061" target="_blank">📅 14:03 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102060">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ap50rvTiVleX_PK6zusjXmdq49VexkkU5OWO2dnuv22MO0cBJ3Ka8ylrKSOytsrgmyxFTAIp12qZmQZMB9An6q5Ul9Dh2TV6F151hmdgHOIhTZuqR-EvcJ6SxiT4LKPDv3iPFwhz5GV9LZIBpcXrmTXwXAviJN6At4KBmv0hZocs9zHZg6kr68JislmNj_j8hsk545cLGuCu8bnUwvJILihN5oDddnW57UkThFIs1BCLsdVMwlzGPAY-01i2dz8wwPWa5MMVJo08mAmWgwlbtmKAUy5zhF8Ybel3gtYFoolnRG7WFJLQzF8AGSm1KTN-f7nZth_fw5TsS5Is4SJyIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽
لیست بارسلونا برای سفر به انگلیس برای پیش فصل با حضور ترشتگن و دیونگ.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/102060" target="_blank">📅 13:38 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102058">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pLipo37XpQRJjMrnscnAYXoqEfri71pujDL5k7G6bl76kaqnvqlgACOqEYvfRbwBVHteqZirmXB053r1AaW2MPROLO9F60BSBzP677rU1X2kdbqyfqswCMFSSjDmLTjE3ONt4kQQIe_fWsBqNZ7XIoBLe9pqV2ld_i9ULo12ECr7lOGT3WgmY66ntFrxJ5glanmx3z1tebaAK4srROS9HRc060ropQRHNUQm2nPkseHBq5cWIA5T_P6kNCTrbewPlrwZ3fBrhXw30H4H9TccqgNyZnxW5DBrZRfrK04AYCnaXYy45pp01qDYwCSH-HhQ6EubzqrGhtWa3CwUgzcu3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/olfgU8RdiVcLsHfeiGMsAO7ClXoANC8-2Xranav4Wgk18KM5UfNlFBHX7Habs8zabT2ETZpab2eQIwVWKO2W1YOwl9-LJslyRgpp3PCUB5wINz0S4WirdASasMNUWnxBr-BmQ4raXwgxlerM_mrUsnFC2ZaKcJhYWBMgqBgG6RGtnxeHnwMCfIzYI_xxmkTlAkoaPLwLLLz8CksXCGEgfWEnnjTXnVyLN8tt_V8EueOCJxdbFt5xj6wMzbKs6f2at1jcUszFw1cfB9053c1LXatw3tz4kEslnAIxyPzxhptFQ9BnwPtfw9HBC_CxOWUcMGRK4ocYZ6EcTITxlavl9A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
نیمار:
وقتی در پاری‌سن‌ژرمن بودیم، از مسی خواستم پنالتی‌ها را بزند، اما او گفت: "نه، من برای این کار اینجا نیستم. یا خودت بزن یا بده به امباپه." او حتی برای هیچ‌چیز هم بحث و جدل نمی‌کند. آدمی فوق‌العاده آرام و صلح‌طلب است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102058" target="_blank">📅 13:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102057">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102057" target="_blank">📅 12:52 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102056">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qwtbYgdT2wmo10EvZmvSzTFc5VYiGOa-4uS6QONHfn8upRb8smCIJRVWXFQJdcB1XfaF16rUOTKsF4zm994BxmKveuORph0AjRGikt2nJOI87Q63k4S3axcSX_LeOFcoAWUHpAKvbfinCA9ENUwhqXafkYTrARVGfhYu8qbfSgzOeamoXnZcZN4nuTLNyva3uhOqHNe2NvPxlsZRJZ0Me7YGInLvWqThKMsuERAEk0XUktx5tdP6SC_Du1dzmSHKKxKlyvCDXH1Ju9mgW9SnISlnCZe5jFe51Sgl2EXTLX2fottxBtRnocnIdlDeDDk5p0n7F4yIoKJkQMf1J3vI8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇦🇷
بنر هوادارای بوکاجونیورز برای تیم ملی آرژانتین:
ممنون بابت تمام این شادی‌ ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/102056" target="_blank">📅 12:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102055">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
فابریزیو رومانو:
🇮🇹
✅
پائولو مالدینی، به عنوان مدیر فنی جدید تیم ملی ایتالیا انتخاب شد.  HEREEE WEEE GO
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102055" target="_blank">📅 12:38 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102054">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ebffP0JjbQ747RbG-W2N4qx4aM0NvdWinoQ9a73MUpQrrkYp-F26pbxoL4SDUJcm0zY69_-qjm4dlhodKuADiW5M99KatHxU_Nl6Ags-bj1_UE3YFosDU8ytZcOk_rzj2OLeGjRZMPktl-xYnvWSvk0FTfh6DZAtPYVx66D3dBDu6ZA5vbCQ4QxBd50stJB3EhNH2xVLy9QUXjPbKBL-5LpjnE1gM6kOUgK7i39hdohPdCibVCM1N2gvgnQ47rNv5Z6X3N4SlZIzcF2QsmC6C_k-JrCElmU1dF_52x6Cpzq3u03u5F7nn0gtScnkFwXSOZy5U1WC00oNCO_5b9q5EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
الهلال به کریم بنزما پیشنهاد داده بود که به هر باشگاهی در لیگ عربستان که میخواهد برود. اما بنزما این پیشنهاد را رد کرد. این مهاجم کاملا روشن کرده که هیچ قصدی برای ترک باشگاه ندارد و این خود الهلال است که می‌خواهد او را کنار بگذارد. در واکنش به این شرایط، بنزما خواستار نامه فسخ قراردادش و همچنین پرداخت کامل ۱۰۰٪ حقوق باقی‌مانده‌اش طبق قرارداد شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/102054" target="_blank">📅 12:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102053">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ChWiwSNlUgBsASpCasJpnNAivaqFAflA6zuiz-x7oZGxmXGn8Hf3mzDtZH5B8qZMnN_ysCGgPWD-IMdpLYIcIrWt9YCA8VeiW6TMGR4pmN7Bki_QPeEGp1wD99WfoeUB4784yl2cvm4wTp0JPe4Y9E4RgR0OHIu4JAUkd-Q95GhoCxlNWa1-fpXFtDV_HLKKkmOHCSUa0NC_DhrNaEEAtwzg2ewNO97BCjUf99d6jrBHSfGk1IO_iHbU5ZCOwBhGbhkHwjGf2Y8YVUUW6ET9MuRS9pG6C6q_cT_7MjmhWHsZ7zvVivSg4Kd4WG_ydzLaC02lP_tANHKeu2TNr59X9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
جورجینا رودریگز درباره اولین دیدارش با کریستیانو رونالدو:
قد بلندش، بدنش و زیبایی‌اش توجه من را جلب کرد. جلوی او می‌لرزیدم، اما یک جرقه بین ما شکل گرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/102053" target="_blank">📅 11:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102052">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WCE4XnxmTAfNmJ5hRr6W3ajuo-_PnjnLMuEFzwhnqAE7HlLSdxcLYYAh2kQDHRLhTwO5NglIBF6_irEhvU4zzxFmyIbWt9L6MCB9S985e2Di5VTLUhgtxQLPQHXvhnNcWRA78RVWNb-VayM0GKQt9p5eCfJwtElfLfsjFErWa512ticBcJvaVhZTzVV2eQM678eJ-O-CsxWw_TAsRWkXMJRSMW_A-ftVPKSMgoQjO1oV9ns-5ndHXKKQu1kAWEZoKJxNm0vwF7Rh5TLFsnh8ZLl3FSjU-DgLLUwy2sNi1k540PhWGGfJXaTidFWmJp3VXiyOvtq_S8ioTo9WD7Tadw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برناردو سیلوا و ژائو نوس به همراه زیدیاشون تو مراسم عروسی گونزالو راموس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/102052" target="_blank">📅 11:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102051">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102051" target="_blank">📅 11:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102050">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qfPw_DakiWIuYvgkhOksj-Eu4GrKo0CO1SaCccJc-PMsWUeRcnYHBKlL7vCWJRycWgTBj_HENipSrXXBVd143vflM0Lsqbfr6k1h12TJJ9jE-B2CvzEwgqbfdmvp_CkPjSYVzvMAIJBkUulkQ7OqbSE52s4TBDM8ou4TzhUGUNgatP8PdyzFLl_GD3tclTPzZJpsE1gO65O_D3qiNgq4wqzQLdvBWGq4Z0kB2nrpnkKIQ3YlGotOzYq7aC0QHFDWgc783ez7MKMxq-7CObBVeKGz28J0fr0F-ITSaGUpuRZMyMQr9SXkYSUwIlXjZ2K_RcFPd8zgEOHbXN1OjLwOlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
فابریزیو رومانو:
منچسترسیتی مذاکراتشو با باشگاه لیل برای جذب ایوب بوعدی ادامه میده. مذاکرات با باشگاه و بازیکن همچنان ادامه داره و تصمیم‌گیری در مورد انتقال او، یا در حال حاضر یا در تابستان سال 2027 انجام میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/102050" target="_blank">📅 10:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102048">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ie5Uc4jlmGlSqTlO8QPQ2aCpq9qzLSDENCQjm57D5-B1FjT8hxiNl6LRNPoOxMRDOrxMm0gjynQ1ySGYioupVhXhLFohmD8H-OkYGwphfWGUPmtIzai5Sa9XizlIrhplULpAUsn-PqFKB9luL9eMtWGOpkmbZWkbRmG8JFmyJ3lCISIeYFB8wTtqH7b7kcfd9gZ1y9dnCAUaNmobLJIc_hX1kJT0Bcip7YZhIeNM2UohRsFTol4ECRJ12kxELcP9uMblqOx2MnqB0nllEUYC9fJX0eYzi54pI5qwQP8KHMNBx7vesL1Qhc4CNKbyJhtLisZodzXXlBThReafjmNk4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U5K9UsvBOEJm_xOFDpseRXn35KjlBbJYm0xq3a9dDPyFr3xmIqjzHbIwiHnWFbVA5hEANki65U1E28ywVRVju9VytZGhKnuVpzQxLiov9niHwoOaborVfVhSadf-iwCSWXUc1FLVki5xTRWnQsb9Hthn3s9AuuQJf5vwjE6KGw4nDgWwyuDtWGRbjlwfF3_D8kDo_IcB_sfxsS0FwLn67YeU6vURPjLmQsFy-xZdqgou7ORDtrFm-Alngk70d_K8LZ_TNZHKMJLSeJiKAM5maDuIo84oTKK9dX1kcR2ydzgn_DXTcmKv_YkB2L4ThQtEoExavQpkl-bza6lIYuDLuQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جورجینا و پسرخونده‌ش که حسابی باهم گلف بازی میکنن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/102048" target="_blank">📅 10:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102047">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FZq4GPifQ83R8SDEnhmqHe7hV3WNVwnqn286fZ1rZoEUOmqEckNJWZ3zPSSDCc_RoJdM7HdoNZmYV3pluFZazIlGAWXQqcwxsg1s0RQC5PeQG66yGHqpm9NejS9hAsHO_8kHd_FwO_xhF5C1dHEq7cr3AQLNo19UVardKnqkPfOFf3XLcOQvhwOmdPwj1Mgcak9G71AT0cYEDQqHPSTs2815IQW8Qt_oYIQJr79SxPJjEB2VBWUHkBe-N-BsfDJjq-aawJPjecWl70WIOBk-_kLQ4h8fFfEIhRYxX1A7J-KK0k-ptoVE1bxsqECIzWHrh2Osex95sl6ELnMW_QgMWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
الیور کان در مورد کلوپ و تیم ملی آلمان:
شخصا فکر نمیکنم کار در تیم ملی به آن سادگی که خیلی‌ها تصور می‌کنند باشد. من معتقدم مشکلات خیلی عمیق‌تر هستند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102047" target="_blank">📅 10:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102046">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MV50iwe06tVwV_Y3wtKxEd9oSEqCh21VediSr16G8WLyXw4XERdh2f-bow2e5b7uwMD20g-pe7g4BWPXmoq2xshYGJuJG0_FMdlAO30STRz3-5cBwYTagu6muo8x6rG8qMVnWFXBwxfLFTgd9WVXxqDr7fnp0MgkA3vgHM0uApE2R4QHwXML3kUMycH48HNbbBVbKwvx3jg66_96XQQbjmoP-M8ojRLmNEF7DTxI2LXyf5DyNMgqvH457f19LNxtNGbgwCzTF9BWdKNMMZ8cKEyiN8K04oa7C-Fj1udGlpLF63YQ59-pOx5NDrJYesriyZS8shPo0hGfd6Tz5AapAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔴
وینیسیوس جونیور فصل گذشته ۱۴ گل و پاس گل بیشتر از هر مهاجم آرسنال ثبت کرد. او می‌تواند خط حمله قهرمان پریمیرلیگ را فورا یک سطح بالاتر ببرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/102046" target="_blank">📅 10:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102045">
<div class="tg-post-header">📌 پیام #59</div>
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
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/102045" target="_blank">📅 09:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102043">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zo71YSJ0eRLykuaF_PA7fsLFVFbcydYQYghizCJbqyYSG5JnvMoYsdceGLnCKnJZM2EXfNownDXwDa5dzx_DvHe5mZBBTmagG9kTuz9VTZeQniRP9pKgeDti0pbg9hSqHAYKN23KdfjgX_SGdKX463MdwuazC0n2J-RR6Ih5VU4kOPmixGtDtcvt9G__sMPckEDHTjjnZOJqommmCgjPVfYLhXyCeN5rC4Je-8Z9LBnwoXj8wa-8vGWz04U4JhamF7TmEO7Y2fBMATtVekdD0SqOeEUgZVfIMAY5P1AY5M95uv0PqGFm-IH7uLVTf3yraIaer14_ljDW35tQRgdQ9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d3eF6WFMF5xi0w_zhtXcUp5TZLps2j76hX_Ab8Mw-HI5llfFe3WE7qr5Nck6OSQ3ltqlcsQk2_qwsDpSsRpq7RUI3pyi_sas24BoW2zFVBEEuTOXxLJBtt0Tf2oYKhg4rBIUJnRGKcwjvis2bgmWWd-TWnAgxP1Tkxnt6HoJ4OaN5zmWK1epZNyA65GO0TMcwII2vS00aizyvEd892nOwTtHb7Qn59pq3dmxx-tRhDQJ3BfQTvl-vJRB1kHLZ_b6k3XfYXN4q308JSKa8-5OfknDoRHavrxJqRfTCeC4jhEyOeXJxNmbjGOk1rnVIC7IDoyTr90CCUYv7qGxOuzLKQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
👀
طبق گزارش رسانه‌های برزیلی؛ نیمار بدون اجازه، کمپ تمرینی سانتوس را ترک کرد و بعد از برگشت هم در تمرینات تیم شرکت نکرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/102043" target="_blank">📅 09:31 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102042">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VTt9dokoU-A02FqQrxqvVgDT9QXIggcdmC4zGnXQ9v6BvTjbG9AD4ZokiPz7MFHsKtczKYDHnb0fGv7SXXHX-9nTXtQRMw914RBbwv4yGXBKBprxY9-t1qoq10S7-G01BI5zmVmtXk0q2E3aW9vAzPF0tyeJHcKTW-3p_QJkCL8DhUU_fhr-D1vF6eyKLfOviSmp6wUgoaGeKbTLY1M1J-nfBSXRH6mrQ4-FQBNmpsz3S0Wj5Wm-rz2JQ1oihU0gPzFh4mEtumQpqcS_B9ATRFD1Y7US3VKIhY1Iyj0Cw8hBWcdKnZ7RGaRPR4r5CpirXT0nSRCgSJKQZXfo3npz1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نیکولا شیرا:
رئال مادرید آماده ارائه اولین پیشنهاد به منچسترسیتی برای جذب رودری است.  ارزش اولیه پیشنهاد بین ۵۰ تا ۶۰ میلیون یورو.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/102042" target="_blank">📅 09:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102041">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fWgI6838P4f6mKZen73HzrvaS2x2vlkXfTjc_OHuA_VL1Eo4_eK_kT4IzyOt_-r2jlzid3GBf_IesQtggV_6wNxmFSyGGej-wVihsGEaONk9VKA5c72Ig9t8Wa8XpYvW9V3Y1nAvFYTr66LQBijO-QjgFa87ep6_Yn0GYrUMj8hiFryEFbLtDLbIR939KBkoZyL1GIdj15wVtK4xJ2AJslJTir-MZigrT67HRh58ramzBwPn7B63c23H1eo4bGZ4o0A7Gk02UbUIxBlAL8L9tpyKozcBPrCcDNWtiHlP8u8LsGVuJpwD2IdqQ2cTeuibKQqUH3Sy48UcY1fKNEhYLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
⚠️
اوه‌اوه یکی جلو فلوریان پلتنبرگ رو بگیره که ریده به سر تا پای رومانو:  حالا که ما را "دروغگو" نامیدید، شما خط قرمز را رد کردید. شما فقط یک روز پس از آن، انتقال رسمی لوزانو به آینتراخت فرانکفورت را اعلام کردید، و با این فرض که هواداران شما احمق هستند،…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/102041" target="_blank">📅 04:53 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102040">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_rim_tIw7z1kYxLoiS_qn_rW94bK0XBuMMDpNcRigaatQZpHzC3vth5ojZnH_gDRzfO0fZtG2pRepMRfxjaP52h-JTc7iMb4LVz2rKpnN9UVGRAeqzuRvnS9L6bGqCyu8GKsP67sr0ipeE-hlIwJ08zO8-b3V1hVvIEJlKubbrYe_TAvtL_bNbYGPOQisSfNQSwViIekgM_WqC7WDa7iKE6nSLEkGjgctXuQcq5A8AwJaU1CeCypKR_QQxBJe-A-osOKoV4P53XF-Qbx4AfkrFSbnocSc3Wpc18O1QBDpOFmil6arkHpZb7inEnzKhTkoQVuJAZ3hf3h8mihU0S7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
❌
🇮🇹
#فوووووری؛ حضور پیرلو به عنوان سرمربی تیم‌ملی ایتالیا بدلیل فعالیت‌های شرط‌بندی وی منتفی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/102040" target="_blank">📅 02:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102039">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/Futball180TV/102039" target="_blank">📅 02:03 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102038">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cWrrbqIYE468t1YJSj3UJjIkHjAGt6cc4J-wcAZqLBCpI6FiTXHn0-nh2_PTRlCpvzAUNSi_B5bBYR85zXKeK-EctyWcrcevL5g_5UV5bm-Ki1F8Vx1cCuM-EKUEo4hjdvsB_MgTrpwNevQ6AQ9B1uJN-i-d1MOw_evAHPNwtPJu4JPHDQf6ypVN1h3CHCCo56syXvBXH8fkaFlBv541rTp-F_yzfFnql9z72--mS2deWDrw9VVv8FtJz2B0mFMqIJi3fo1XhSccQWqoHy3Zsv4dIpsYHVM5Cw5RkWhzcuGCeDiRU0Qa7Ukl4WWIdmq1NkbJWfI3o6xOsqbcyhjXEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
ماستانتاتو بازیکن آرژانتینی رئال‌مادرید قراره به صورت قرضی راهی بنفیکا بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/102038" target="_blank">📅 02:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102037">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gHSE_uSbXQJUmobBU3rS5zgiXprMdXlMlbGGln-i13oZls9utDWbc6i4GICoCc3nfuTwDbr14dc-61TYyWNKpQD25_XtO0Lr_VEqyYe_Q5uQqw5AUKCp5tZPwsKVWo_D28P1qlvq2QSCuTf3nPj22VVmERGuu6q8clyQ5xlxBNIT8Bdf6xTorBZBxwiLFm9G69eRc8dAd89Powz1RluWx8qTYOLgXgBHkEDvWPTonBz7qEcJB_wU-sbf7oFHFAfbGiC7WOr6HxRqqe8F59rXbjLmV6YKb89Xr7t-0mSQ0VUXgTor4OXmeYhArISuoPCagkHU-2Y_52PjfnZPbFNLBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
جنگ بین خبرنگاران مطرح فوتبال اروپا بالا گرفته به طوری که دیوید اورنشتین گفته پیشنهاد رئال‌مادرید هنوز مورد موافقت لایپزیگ قرار نگرفته و نیاز به زمان داره و به نوعی گفته رومانو فعلا زر مفت زده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/102037" target="_blank">📅 01:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102036">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BHGS0dIk0Tt3jkiGkavzl-oADm2Zua7i9p1pdLmmHfEgVdnlfcHyp20uPJoTesdyJ2-27xaaYjPtGhynG22T__9zRAsVvNFVSm0O-I_9YE1TOhtim-HLv24YKi5HVTvzuXLK_gtnfHL-nxmwA7DpzaVh3Z49plZmgQ9a68yd11s4p-GXTtBjzkhLi82Ugh5Ke3gl81uO0WJmrAAR5auNzETkdkLWGnQ1IyrrA0At2aM6Jbx21kekVnMc_6Amhl_hy4d0PyS5BRpakhusdE87iAlBhA9n0B7Ek2rhRp8mpCpAcDpP0LAyZqgp6AW0NqmbqYQg2Sy2qLsNESVZgFHtDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
سرخیو والنتین خبرنگار فوتبال اروپا: ژوزه مورینیو به کاماوینگا گفته که فرصت بازی زیادی در فصل‌آینده نداره و بهتره به فکر تیم دیگه‌ای باشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/102036" target="_blank">📅 01:16 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102035">
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/102035" target="_blank">📅 01:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102034">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fa8UvnkUF_f01vHrldLAh4E4VdD3JzARKGXGz3RFKzsPpcM1eX2eUfoKVH8VljRLfWZ4tSQbj1YIJiEH4F__W9PC-gKkJz7qWc7rPP2EFV-iZyk9ihqLHvI8AsJtS5GUKpDCg8yMRHxgAwPHtyoJcn8O-WtdbzdMpLA9_TK4MTkQMX7kcne9Xma0iL8cetXtNFyiXqHbjX5y1y5oDfqSXn3J0rVcVw17afAQetE2rlK3W_Dbh1eJARXGuuV3QtS_nXCTHFuripIW-qmwDz5dKcO0b8zoELd09PlpYZnAZo23J1Hm7FH9UjvUwcySP-fBDdNf7OUlR9d5AACi6ekJ1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
تلگراف:
مدیرای آرسنال معتقدن وینیسیوس جونیور همون بازیکنیه که میتونن باهاش چمپیونزلیگ بگیرن و هرچی واسش خرج کنن ارزش داره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/102034" target="_blank">📅 00:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102033">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fda4a57b7.mp4?token=QKt6HVPyBlqkrMxI3df2bFzOCJKLU4QHBR2Ge26L7A75A_L604xRApeCSpaqTski7A5BLew8QfaTYzCet1626NoIRuEjENQ9ejkNFn-e-MaDoXWmfk10BjVprNFZio7J54MKutHh0MFXaJCz1KaeqmYSBWHZqiKzbO9942GvdE54v7OsSoowPxTe-8w3S1ovAtxf9AwUBxRUUCkMOPaBpoPW3PfPCAJcbtTfXkVATBDDkr0v37NHMjgtqPbqlZ9kuTnuoBgGLtROIuaPRVQe8dZ69aliQP0gXiKQWnDBbNqz8SWF9luU4EtO-seOOYD8gXa8XbXvtuGn416jWJGn6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fda4a57b7.mp4?token=QKt6HVPyBlqkrMxI3df2bFzOCJKLU4QHBR2Ge26L7A75A_L604xRApeCSpaqTski7A5BLew8QfaTYzCet1626NoIRuEjENQ9ejkNFn-e-MaDoXWmfk10BjVprNFZio7J54MKutHh0MFXaJCz1KaeqmYSBWHZqiKzbO9942GvdE54v7OsSoowPxTe-8w3S1ovAtxf9AwUBxRUUCkMOPaBpoPW3PfPCAJcbtTfXkVATBDDkr0v37NHMjgtqPbqlZ9kuTnuoBgGLtROIuaPRVQe8dZ69aliQP0gXiKQWnDBbNqz8SWF9luU4EtO-seOOYD8gXa8XbXvtuGn416jWJGn6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
وضعیت این‌روزهای لیونل‌مسی در تعطیلات:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/102033" target="_blank">📅 23:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102032">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RvJsWrperTsjQkAvQd35JN6MXaeycYEpIdNhW8RXQj3CFg9A_MxY_T-11guuxfr270bnto5B013HtlFxU3wkDDWR5urTXa4YwFgpc5V5bfephaNB8A0-C1KMkQcSFjhuS5xglRiRts7tj2QvSx0XYaq_UT9xGOqW923mAlXoNeIrL4E8HvHkiMONwTIreGsS6-zwFDrde4s_tu9TC0wXGkVAI3_xbhjxaLazQbv__768mQchEhzliPPoQHzqvUuvc-AzTp__Hys48YT0ejMbiJBF4EV47VCoN-sUznZGst7JbIZiD6AlKcao5d1ZEcZp-D9xb8KcIayqfhsBazgmRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📮
🇮🇹
دیس فلوریان پلتنبرگ به رومانو: بعضیا همیشه میخوان اول باشن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/102032" target="_blank">📅 23:36 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102031">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/knLIykMorghBCVMkRKJi71_JJYEU3ELPjPH3e96la2joUFfTQJ617qr8VFWugFebXE-tbN0AtpYcixzwl73FGQzO9FuqqBh0Lzuk_KNGT6Bqn5y8jxTxDTZP9KwpMsWgBVtBh1VRlbQYiKq2yp6PCIqwX7MWQ53ChhlHbGcVd_PqWxci9yRl_WG7vyhTeLwE4BAn8bGRmmTnLvooaDh6tqvR7EoFUs-6JBs4-D4qrS8IVlLx7ESn_d08r7pxBVjXZBi8elrFm9XOHgJ-fJXBkaMK3Keb2Swqc-Mt2avckaE8ub-xWCrz7n2eIqDSo0hY8y7VRbQg73KjAwVGKzvrOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😐
فلوریان پلتنبرگ اصرار داره که هنوز هیچ توافقی (حتی توافقی اولیه) بین لایپزیگ و رئال مادرید حاصل نشده
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/102031" target="_blank">📅 23:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102030">
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
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/102030" target="_blank">📅 23:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102029">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e020f6fb8a.mp4?token=EBfoxv4vYDNz8wGJl5vxcew5PwgyDtVLe-iIuRSnnf0fps_6hLq3_Atj9Y2E8B-34e6g_f8_iQiDRXg3jsG_lqPW4sSCfVQ9Ltm9aEKT3ZofC75Hrxk4e7dO3lXNdtifMOmD_kqCRYp5lFelKmqhGQvjc99EpidzvrUHLGhmRfjFFilDOB2QIXEGxozMntOX4sjod6AtbF5ayZvhmW0e0g8jNGm_ey5Ur_zQvHmPN8MS4dnNRS_FohnuS7VHT58ynRxeNZlfVSz52QuYj2SGtzO_HwW0zczKqjadnPsFYQQ1epEEE7kdGA24PalhwLHDhOQmJjTLXE729kIZFAwO-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e020f6fb8a.mp4?token=EBfoxv4vYDNz8wGJl5vxcew5PwgyDtVLe-iIuRSnnf0fps_6hLq3_Atj9Y2E8B-34e6g_f8_iQiDRXg3jsG_lqPW4sSCfVQ9Ltm9aEKT3ZofC75Hrxk4e7dO3lXNdtifMOmD_kqCRYp5lFelKmqhGQvjc99EpidzvrUHLGhmRfjFFilDOB2QIXEGxozMntOX4sjod6AtbF5ayZvhmW0e0g8jNGm_ey5Ur_zQvHmPN8MS4dnNRS_FohnuS7VHT58ynRxeNZlfVSz52QuYj2SGtzO_HwW0zczKqjadnPsFYQQ1epEEE7kdGA24PalhwLHDhOQmJjTLXE729kIZFAwO-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسطوره فوتبال مملکت علی‌آقا دایی
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/102029" target="_blank">📅 23:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102028">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cfe5yDV6sP9eSZ0vI9MlJT1y1yjZOH01i_wA_Lw3MFQK1-U68_Ok1f4VQTiaBlkUYQh6QqgHP0vle3ZYI9EgxTELtgVWtTAyMI4Ez8VTwFHKPBRT3wuiqirtcRC5i1juwgQsyUqv1JWe5lHTo7d-zoskU7r1z2EsY1HNIMg2I5JE2gEvaOjUK1iQcDyaGRFRNtB-70KIZ5bsr8FU2BjYT7UovDZhqZ_BvdT3PtgjCs5va9FUFaY5UjsmppHT5h00Vi592V3plfw3M_dHUaAxETYa4zXsGRTkB9FWKryFOzOzyT_8i20Qnz0rMxLk0baXJtNRExKWspmFYlZm0YLTag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
👀
رومانو:
🔺
خرید دیومانده بیش از 100 میلیون یورو برای رئال مادرید آب خورد.
🔺
مدت قراردادش هم تا سال 2031 هست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/102028" target="_blank">📅 22:48 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102027">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eun4MzasQw_M7Iz30XkbYrv0cyCJX3l1T8PdA8par64c6z3pC1BB9g6qMgmQv_q2BWdD9f9ZI1aTwVF1Jwe51YUsvHdPVSPwFjcJwoZSjwxVFMyQVQWpd3wZIVgld2IaTIFw2MK-2AASxCWBhftctpr9aD3WDCJNtXhsu9hh7osmdje7G_HBghssQcy-QivtiNXAKMl5Y_6Hh0q3WvP2tyulIKuhDyn6RV3o46bEVPIrQwjqtrCL8xMzqmj-L9c4sVuzzkBsmLVcazJjuwKjsni7hQ3P04zh-9n22NKjF7FQuTxIm47TEbAomDGxeEHVf47v_V0fP8rP5pgG3GiNQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاهکار پرز:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/102027" target="_blank">📅 22:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102026">
<div class="tg-post-header">📌 پیام #41</div>
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
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/102026" target="_blank">📅 22:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102025">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vaOjrmsLWWyH0gvdH_ldtbzDikOMJjLltv3eGCj20MGuN_Gn4_FbDw51RXIv7IjvN9s3UUuD0bN41NkNq_6a9uQU3-Ks4-XuxWvodtKTxRewiiIJFqBMxBbbmKGLsUls5i2Fi3NWvJX3lryxFlMUfPgMKDIvt2dtHAaKPsLTXU65Bspis02WWjYs4vn9vB7jaYmcTc3jvccM2tB-2TuJ4_gEuJX7Jw4xluShvBctJhOMCFP65jj-2-CA_KeBcLs1mjlxX0wVYiGCf8BIUiTX2qEEAlS8jKlPbFDGz2AXAiYHtshJMIoyrlkHje_vd_jsTFrfUITng0HUUOZOAEAuJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
اسپورت: خولیان الوارز گفته میخواد یه قدم دیگه برای پیوستن به بارسا برداره و بزودی انجامش میده . نهایت تا ۱۰ روز اینده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/102025" target="_blank">📅 22:32 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102024">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NQVvAc_LmMasYSWco2Z3gSyV6SehwQFgK5MrRD2ynXovlPjlU2FpoY1atOJyRzDaG7hkExxs3zpt24J-nc0fndpNLt_rjQz-22Ibh97LPDkK9LZiZcxc4ld0tLVqkS9lg3U2x4yqlvQyVU6E8YgXR87UU93iNN4r1pyRwPHSBcOqz4E2MXE9PgjNyqpKSzURCEp_ciRwwfPAaHc_KA4vnzVUHm9scK4qE7H2XG6noo5wX90O-iWYZF2iRWba25-Ua9t3mzf8sWgZVBPl8rcwhxw71GDgPYTiK2EJaTnXLvZ98gTxNQtNOYoGH8K5FBV2tJbrTVhT7gS6rGN6qRPoKg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/102024" target="_blank">📅 22:29 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102023">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9274ecf947.mp4?token=m_Jw2BDMxcCtkHgUsT8TD5WSdsguFt97bPy8XiASGQJHd6L4Snw7nS39-Pn7X7FZQEOBNfI7RWI_LQzmIE43XgdQypc7GpwL3XgQECtlNHEJ2zL3v9cEDe6hBWw7998fQ5jVaAE-e7bmoxgkXmVOXuH9YJv3n7D2RQOLgZmqlZe4se_KQn-1kPUemlp37l48Soo3HC2exe06BXR6j17ZWNKwrwfn64cnIXc9MPZnbIDHbVTizUKLRyayKjxGhUun2ZK-Umca7EpNHPpwGNRvkH_SQ_uezjBydXplHQF7Dk-shYJmrn602MT9MVv4RA6YuEBDYQ-6SsUABJdpsvupg5P4KdMVtnUwUC0gmys1sC501wgmN_3XEl1dDZrqn_OfsFt5GrwEGEYFoMtxFCc44KNEEKT3Q1u2ZqD1awHiauliXdKdyUzu563OzJ_wOWyqL8n3gZiD8ySMW0tyGm8oQ37NZApNDjmoT9s-EBac4k2xJ2EwB6Sh1W7k2o1D34sddV2pn0Q0jROco5x17dD9b39369FqQCY6lDv8p3v3s6fZ6xS6xVTQRcmD2utEJWhj7U2BovkOTLsn6p5Fddt9Msv4ueDoBn0esCKmbli3EGOU8TSWZdsAMlXwmbjszFIuFMLaX69l6ngJrBuHJDXt_ODl-OOnuTjdf2dKlyFNurM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9274ecf947.mp4?token=m_Jw2BDMxcCtkHgUsT8TD5WSdsguFt97bPy8XiASGQJHd6L4Snw7nS39-Pn7X7FZQEOBNfI7RWI_LQzmIE43XgdQypc7GpwL3XgQECtlNHEJ2zL3v9cEDe6hBWw7998fQ5jVaAE-e7bmoxgkXmVOXuH9YJv3n7D2RQOLgZmqlZe4se_KQn-1kPUemlp37l48Soo3HC2exe06BXR6j17ZWNKwrwfn64cnIXc9MPZnbIDHbVTizUKLRyayKjxGhUun2ZK-Umca7EpNHPpwGNRvkH_SQ_uezjBydXplHQF7Dk-shYJmrn602MT9MVv4RA6YuEBDYQ-6SsUABJdpsvupg5P4KdMVtnUwUC0gmys1sC501wgmN_3XEl1dDZrqn_OfsFt5GrwEGEYFoMtxFCc44KNEEKT3Q1u2ZqD1awHiauliXdKdyUzu563OzJ_wOWyqL8n3gZiD8ySMW0tyGm8oQ37NZApNDjmoT9s-EBac4k2xJ2EwB6Sh1W7k2o1D34sddV2pn0Q0jROco5x17dD9b39369FqQCY6lDv8p3v3s6fZ6xS6xVTQRcmD2utEJWhj7U2BovkOTLsn6p5Fddt9Msv4ueDoBn0esCKmbli3EGOU8TSWZdsAMlXwmbjszFIuFMLaX69l6ngJrBuHJDXt_ODl-OOnuTjdf2dKlyFNurM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
آنخل دی‌ماریا: مسی نشون داد که یکی از بهترین‌های تاریخه و تا وقتی که خودش بخواد میتونه همچنان ادامه بده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/102023" target="_blank">📅 22:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102022">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vDZupqzJC-zdmcnoAZ084JywTHoaE_nJqvQhLvtOefn-5rKDHzYgKQv5cXEy2LR-pNl5l3BpumdQ3L7k3dRTHlp9IxyIbjylr6u70NxVMr4Sb_zU7ZGxbn7BtrZs6NaRanZtKkw5GhKqLoFeeLfzLQKb8nfaUJHej5cPWBFYAJqmVcjkifaaEo9s0ya7Dr0BkzDFFTfZNeWd6V35AW_o-TPyTLG6p0xiQNa6477F5Z-9gNXx3Iwv3AObCQvIfdArlPTc5LlkDZiQcFGs7-kWYm_NgCZtU6vm0YpC24TU6GQQ0hjCSFFPFS1zX7EcwjIgqS5OCEORJlLC7YpqSlYVBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
⚪️
عمق اسکواد رئال مادرید برای فصل آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/102022" target="_blank">📅 21:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102021">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e76692a40.mp4?token=joDSwv7XweHfsH3poL_bUo1BRbFi8ysrlWRHu8nWMf8E_Sdd0TPrt_NDW-tkqUviEKd3SEzG4a3iEhaugWQid-tYm6560WMLQpUXpAp5clRHJqvQSJTTvTgShs5K3ick14nHYzYWmKp1yBYsktJZ8lZ-Zd906pgp2SpT-J6HLniqH6uuST2bouZbd73E4SQFqO9GYINZBR3aITKOV89UBMQZMIm3bDTI9_NoLjYOAQMSa-ZuWgCfrZ7SLUnGlZpa7QxjxEHvqkl43FpzOs0jItsr4hPrTqX-BL-c62Dc-f1TAQ70m9_wsfdXNwUyvd47Jl_xvIOYGzQ-BzSH57c7KDX3OzUui2ckyP-M1_znl3OXXDD56lFA4NkjldiI8lo4WcAfNPK4Ihr3A5ZuwaL2eo4vUFzoFwJa9EN3mlnjlSLvc97Qql-RKffzjBdqXzEWF9cY0nRja0esXaMaeO5YplaNbGqwq2o-42qe71kqGuyWLM-Vp4z7S9mMOMuH8WRpf85RUiZ94HmQd_FHlStMwsUx7GM_R7iGtXq2wzamipz-KcVkt6CHWpNqZBInhGHW0twFWeOSxRX9z6BGZQWA-EZ6LEQfKqB6o_0OJ5D4s4_2QMdotE3BYhvL5v0E1UfC0h_pGI6mQpnWPJi_ZBLMBIOC2waRZnhPuhuT-5NS6Ls" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e76692a40.mp4?token=joDSwv7XweHfsH3poL_bUo1BRbFi8ysrlWRHu8nWMf8E_Sdd0TPrt_NDW-tkqUviEKd3SEzG4a3iEhaugWQid-tYm6560WMLQpUXpAp5clRHJqvQSJTTvTgShs5K3ick14nHYzYWmKp1yBYsktJZ8lZ-Zd906pgp2SpT-J6HLniqH6uuST2bouZbd73E4SQFqO9GYINZBR3aITKOV89UBMQZMIm3bDTI9_NoLjYOAQMSa-ZuWgCfrZ7SLUnGlZpa7QxjxEHvqkl43FpzOs0jItsr4hPrTqX-BL-c62Dc-f1TAQ70m9_wsfdXNwUyvd47Jl_xvIOYGzQ-BzSH57c7KDX3OzUui2ckyP-M1_znl3OXXDD56lFA4NkjldiI8lo4WcAfNPK4Ihr3A5ZuwaL2eo4vUFzoFwJa9EN3mlnjlSLvc97Qql-RKffzjBdqXzEWF9cY0nRja0esXaMaeO5YplaNbGqwq2o-42qe71kqGuyWLM-Vp4z7S9mMOMuH8WRpf85RUiZ94HmQd_FHlStMwsUx7GM_R7iGtXq2wzamipz-KcVkt6CHWpNqZBInhGHW0twFWeOSxRX9z6BGZQWA-EZ6LEQfKqB6o_0OJ5D4s4_2QMdotE3BYhvL5v0E1UfC0h_pGI6mQpnWPJi_ZBLMBIOC2waRZnhPuhuT-5NS6Ls" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔵
امیرحسین صادقی: وحید مرادی من و فرزاد را در هتل المپیک آشتی داد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/102021" target="_blank">📅 21:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102020">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vuONn_wYN0MCILUN6amZf5ZLUFq_XLdvklp1pFLrmIepyUjPyaJKzIHG4aBLzmKvaBJc68zSGra75mTf_WTaYuvNPRCHBSvmGQPb6-P_GPDBnurYbrjAe4zWQAnVvV4I3b5dTWQNYikFa50uHqJuLhm_MgxAx_4MOgRI8qY4wkI4cpiSEBr5lTdhuSmwmCZyaSjxGfC9pfql4wEvdu4duEYQbesEXvyJ7OAFyXj4wZv3KIROAo5jRQwQwfpkX8TK5jpcHR4cum3TAQtrisBvvu-jWG2-vysgz9D8iQYHobbsEvQ1GQfI4pJ2pF3qmOvqW9Oc_KmDSLXrMP1Ku-qaBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🚨
پژمان جمشیدی که به تجاوز متهم شده بود، در رای نهایی دادگاه از این اتهام تبرئه شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/102020" target="_blank">📅 20:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102019">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gukZkYW_1ff9aw8y3PB5xMS-6RQ7AJs_0ov8iQ2Sbk3VjOdWzisHmsruYeYj8cN4FEh_IrUqAWNZETjpWqj-H-cJ5yfsKY0IzBbgX-B1huIVYqDTsQ8IHAjfY9yHuGT1z-je_J55zqCTChlzy-d_DUrwL7Y_sOMDT8uMUFEGe8QU1k1O7CfJwN_erOt0dvLh3XvK2OSwMO0aXRT7GLI7QTE89XPYx4j63J15EdUNFH3kk2tZbD6JcEK8Rzj8JGg_ie4D33dyxzi9QOSWfk6VYCPRXhcGdXVEgDrCA9wf8B2TGPwYu1B5Ah0wqSlOOGk-aluuXUO5UzA5NdsJh-Q_xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💣
آرانچا رودریگز: انتظار میرود که یان دیوماندی این هفته به تمرینات رئال مادرید بپیوندد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/102019" target="_blank">📅 20:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102018">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/260d53f1d3.mp4?token=BDJnIHmZqqFp-KIiFpPLvQBnEBuITsGmS3EkbWyrDAhhQWrUYmiy5zGs-Kj7iQwSA3tq90TyIJ_f_eOsY1031n-TgIHideuHq_UE9PcWhiW0xx0-JYGqeW0gik3BmxHOqJGuzUOrU2FOz6_ciTSPOucx3OQNqzjLkvpSmtdgg5cZZPGXjz_cnw6qAVwv2OZwBWx_4SQ7dS1FTKeAsQeCs5zTkVwIt12OtCv6Ppar34XehV9HjQpFumII5nzal_dYe9YGhpKJJdpPcddFBvnkFSkZrWMe4-ILWySfQJSlXoDsdeq_SReRt4t_2ns2WX4wvvaDp7JC6EUdAUoqFnW4fAF_I9_h9XK81aKIs4ofzAGpnWoeZz1hvr9QrA_AuphRpTvEsnqkQikn1I_LyaonIjEwf5zLe9Stg82zx5DhIZEJ9w_-rNJGJssa6YkRSHN7dG8nDEw4FG5X0QvhycVjM58swgK-DDzSo6VfnI9k5daXWP2fb_iMhOIbYyWk2J9KXxwJbJ2DDt5JCR3NV3sUjdIekIkUPz6x18vP5WEKUnNXguts71rfXkTbpthktFaQiBi8PWKDLav8_SwQjraGo-6fX-mzrazAyBXWLsNuMfyd-wtp8fTC0pdLwXIZFAceDH8Kc5ZWMqR_RUTg14n6ATTdqgKY-T9jnJ8eW_sc6k8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/260d53f1d3.mp4?token=BDJnIHmZqqFp-KIiFpPLvQBnEBuITsGmS3EkbWyrDAhhQWrUYmiy5zGs-Kj7iQwSA3tq90TyIJ_f_eOsY1031n-TgIHideuHq_UE9PcWhiW0xx0-JYGqeW0gik3BmxHOqJGuzUOrU2FOz6_ciTSPOucx3OQNqzjLkvpSmtdgg5cZZPGXjz_cnw6qAVwv2OZwBWx_4SQ7dS1FTKeAsQeCs5zTkVwIt12OtCv6Ppar34XehV9HjQpFumII5nzal_dYe9YGhpKJJdpPcddFBvnkFSkZrWMe4-ILWySfQJSlXoDsdeq_SReRt4t_2ns2WX4wvvaDp7JC6EUdAUoqFnW4fAF_I9_h9XK81aKIs4ofzAGpnWoeZz1hvr9QrA_AuphRpTvEsnqkQikn1I_LyaonIjEwf5zLe9Stg82zx5DhIZEJ9w_-rNJGJssa6YkRSHN7dG8nDEw4FG5X0QvhycVjM58swgK-DDzSo6VfnI9k5daXWP2fb_iMhOIbYyWk2J9KXxwJbJ2DDt5JCR3NV3sUjdIekIkUPz6x18vP5WEKUnNXguts71rfXkTbpthktFaQiBi8PWKDLav8_SwQjraGo-6fX-mzrazAyBXWLsNuMfyd-wtp8fTC0pdLwXIZFAceDH8Kc5ZWMqR_RUTg14n6ATTdqgKY-T9jnJ8eW_sc6k8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چنتا سوپرگل قیچی‌برگردون ببینیم تا روحمون ارضا بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/102018" target="_blank">📅 20:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102016">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EFH59FUOJw62hlL2nabP7zCyXDL_0-02uextFN78otGsPql7zAYCC4-cfSOM11eZpEXty-XeR-XIKE1inEeZJVoOpSu7Vth6x9XU0l0wRBMUJLoS3RUxS6fjD5GzrYsqmWH03keKbSzf1W8Ci2BPp9WvKLrKi0jmF9oCELmvM56Xpz2pVWiwSUxC_97uuohHO2Ze8wl42r3o5tDwLinADwNyua_K5PWnQIyI2ulLDtyIt4N5zE8nBFysD3oX74Gwil835eyYWjV405EPtJQbs2ccLgEgQTX_RDgkUeNGBkQXQB817iplJQBYGwjWI9IwTCT6CKBtymIYfq0T0XbhUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iCjNvCZbm0bm2Jm5krk-T1RIZsc2imvC39hkCBlDAhkLdItn-Bc0ltho2z8I0kyzLndWP-NUFqo9OCZcIpC8sDnhX55gE_Hn6zdKyFGzbqw-WZ85PopF8tGPylCKKQXk76qsAHx8nYatDM6l4mldA0fRZRMV6hFy-Kj7w2DE7AXF-KREFoKBVWs6QdeL0krrytD-LIDIlYiVpHQatHQN_Ty2H2iCiMlK8lCG92NLemTdS5KlXEw-vRhV1kouPcdo-mVP6qknEOEqig8Y2E-Et7sH0g_B0sxmtYdQlgMyjxCqiE-pkGuIVJ-OGiVwGpRRY2gDkvsGlYU6eAxq7phNng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
لواندوفسکی:
شاید مجبور باشیم ۱۰۰ یا ۲۰۰ سال دیگه صبر کنیم و منتظر بمونیم تا دوباره بازیکنی مثل مسی ببینیم.
🐐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/102016" target="_blank">📅 19:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102015">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YLQif6I1Bo1g59Fw0SgfgkGGMD2Oei55edNTFupAql8F3cQfDmCSEE_sSaJoOc1XenoIPhbA4WJ7Ldov7iCb9Joptb0ivZ7H2dW96BCHsoDFdiUau1lNo1ysuDY9UbjjyCgqt84M3zTAOJ8u0vx9e7KZkJtY-S2K-LpQ7L82jBswgPgRcZyiunN9jAoKR0EGwye6p79PnwEy3JzCcinX6AU0Oek6uYEH2UkZSz3p_0nQ1QHJaq4OeaAVd9V7OXhMb9FiKP3Nhs_N_nmhlPtyyfE5Voebb8LDV0P5L5hWTWao2vyD5l7Ngfg06nTBJAwXmgVuVOplBAKQ29vFm5qOOw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/102015" target="_blank">📅 19:49 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102014">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb3e14eaaf.mp4?token=dF3WsmgIWRCFTYNgr1IT28H1C1L1z6stbNABhIL9sDRs8I65u2k2I2hhK4n0ZJsLX8L3def9PPj5F0-8UTQtHSQob_q0_aW9tGtFdtqGR9BPEdF5XtzvfrEttypLvIqcxnxkRTaaIOMPW5B_RFoA5Faju82WaycrOI35uY5oAddkKcXWlCgf570-cCiExfcTZIlcVglV3U7iE8NfuHf2bbKRZwrIsbPFWiFdUuHWhJ39Qv7pvqvqMhpW_Ydv1RIUIxtB7_go_82n6MTe2IfgVMow8M4VB10LIoqkU6adaHE7luKaP3snR8g3153vgDghWuod4DuMDfPzA1Q7fJE7vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb3e14eaaf.mp4?token=dF3WsmgIWRCFTYNgr1IT28H1C1L1z6stbNABhIL9sDRs8I65u2k2I2hhK4n0ZJsLX8L3def9PPj5F0-8UTQtHSQob_q0_aW9tGtFdtqGR9BPEdF5XtzvfrEttypLvIqcxnxkRTaaIOMPW5B_RFoA5Faju82WaycrOI35uY5oAddkKcXWlCgf570-cCiExfcTZIlcVglV3U7iE8NfuHf2bbKRZwrIsbPFWiFdUuHWhJ39Qv7pvqvqMhpW_Ydv1RIUIxtB7_go_82n6MTe2IfgVMow8M4VB10LIoqkU6adaHE7luKaP3snR8g3153vgDghWuod4DuMDfPzA1Q7fJE7vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الگوت کیه؟
دیومانده: رونالدو
رونالدو یا مسی؟ مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/102014" target="_blank">📅 19:39 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102013">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromچِشم به راهیم</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c1d6e560e.mp4?token=iNhcXzgIvhe32iCF-kB7hJFflEF5oGa2TzwJB6Y37ENnXJiLlYVg7tYRRYC4ZDiFeu8fo8oeJPkq71BFi1IJP1NJL6HxyW0F0Bsg31uzIm2YT0d2IqKgcK67y5RdV1enMZ6nFlsthUt0rAZRTxJfZE0hFPBPJt97nFzYUP_o5wrcueXhgUdlTD-XJsi6GAITqNLrNlLrT2Hcs25VaSL7la8pRpBlTCiLJJQm_TpFawdikhej0lKrVsqE9mUcnY-LCsDSLQyyWOlxt5dJtyfmU1fAlEG2m7v2cqHzyjLSMUil-IOeWMbMIDeTKoHAvnshpwJDxd5N8l3jnFvjC8b4O1Q0LoAZNmrUFyO_MQtjl95g1Qx-kEYgbb89nZxfkj-Jj-b83mgPvKathlTiy1cKXp58vykrWwWfvpXW5kucwHLgnZmvmDBYKo4a-LwwpCZiNwIu-YRroBDa6hGJx5_jqoFuthSJ54sLbrulC2GbmRT83CkkCGQX101LM8y_msNyyidmExOSEYxCgBbsBhCKMTs-UEKVs87RMy66EOkiI8S82cRgUvA7OEP47GYZEKn-BIqm0gaDuUBMozpSUeXejMimQsoyp7LAPwWop7Sdbe15RTWaLvLm_h1D4c-vyYDzY1b32F9YWQeHwIpvwSFA0JiA6aZX-I7CmvLMjo_IfFE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c1d6e560e.mp4?token=iNhcXzgIvhe32iCF-kB7hJFflEF5oGa2TzwJB6Y37ENnXJiLlYVg7tYRRYC4ZDiFeu8fo8oeJPkq71BFi1IJP1NJL6HxyW0F0Bsg31uzIm2YT0d2IqKgcK67y5RdV1enMZ6nFlsthUt0rAZRTxJfZE0hFPBPJt97nFzYUP_o5wrcueXhgUdlTD-XJsi6GAITqNLrNlLrT2Hcs25VaSL7la8pRpBlTCiLJJQm_TpFawdikhej0lKrVsqE9mUcnY-LCsDSLQyyWOlxt5dJtyfmU1fAlEG2m7v2cqHzyjLSMUil-IOeWMbMIDeTKoHAvnshpwJDxd5N8l3jnFvjC8b4O1Q0LoAZNmrUFyO_MQtjl95g1Qx-kEYgbb89nZxfkj-Jj-b83mgPvKathlTiy1cKXp58vykrWwWfvpXW5kucwHLgnZmvmDBYKo4a-LwwpCZiNwIu-YRroBDa6hGJx5_jqoFuthSJ54sLbrulC2GbmRT83CkkCGQX101LM8y_msNyyidmExOSEYxCgBbsBhCKMTs-UEKVs87RMy66EOkiI8S82cRgUvA7OEP47GYZEKn-BIqm0gaDuUBMozpSUeXejMimQsoyp7LAPwWop7Sdbe15RTWaLvLm_h1D4c-vyYDzY1b32F9YWQeHwIpvwSFA0JiA6aZX-I7CmvLMjo_IfFE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/102013" target="_blank">📅 19:39 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102012">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
⚪️
فوووووری از خوزه فلیکس دیاز: انتقال دیومانده به رئال مادرید نهایی شده و بیانیه رسمی فردا منتشر میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102012" target="_blank">📅 19:27 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102011">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q2d4GoP5rNDIirs6evTqwNreu3-ovg_HiOZvuQXgf5APJ4IfKqGjvRqdsa__POfSruhps3gKP4qpTzgHXr_OGhfCble9x536ILYTwVKDvBjW4vZgYpkrsSdkyKbSR7vJGX1ra6TrGWZdGRUdRb_sgRtjEqUpVvxhK6Tr9AI7-rYfL0EsZpESpng05d0do2MIDvFwuraF4F3-cilLmZMGL22bLuVAVZL6xjFzq4bu04TP2BB_BBFDtxsbBT4QsNizuRFpviD0giML3z9yiqLSOqVXgmGo5XgPCZjLrYJY85weCbfB1WLd3dparpPUCimWelV8CjDmO088Yy3d1sAPqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فوووووری از خوزه فلیکس دیاز: انتقال دیومانده به رئال مادرید نهایی شده و بیانیه رسمی فردا منتشر میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/102011" target="_blank">📅 19:23 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102010">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/746abba13b.mp4?token=Nnvf6qXPBKgiEcSUJ4cNF1f8xlaEUoIsf_YeWyLVwG29sU17y87Nm1YcYDKq9w48xRHfpk9SsvoZHmWoyd_YZY0u0nDJ_ifzcl3F3lzwWeVyzL5ORvQyl-lEp5AFTV-2jxG_iIRtpGumJE6NG8T9nrs4ueEnDY7lbMQTNrqs7jM5k53zhpxzFBzfH8gmdTSz7yMVvsT0MEa9Zn48qkpEdC5A5tZpXX-VgIg4J4vpRt0rCRsg9SRKbQtHv_i6Cwb9toeOhqi6VuBAOxrfJyO6Dvy9y1AysqmGDHgtHrKgIJe9mXznicMffLfBFuyZVQBKBy2esVkeSB0cbPHLchFgRXv-rNSPh_GFZyMv-T5AcwAbLuYEvYyhreuVkK50GCYfSQxprZLkBnTnJYxJKhXnR-3nYyY-NRvNa-2Wh3dVn_LyApG3S66oEw1sRCrN_3MFtuMp85OK2aayAHOvCzyCmtNrr814rzSCkIoMBHGT7tHbp0WNJ4iYsO1yOIT4-7fhpv9IvbCLYsTo3p98SUWCa8Kl_P23wdGefpmUvzin3OVIWR7aTPEv72Zgn7e2l6W1BlgGb-KT91tA28UYWfMg8lClCw_nOh9C72AolTKRt0fFQszO2JTcRdnM3FmL-6YJvWORECOqkOyNzxxwbDEmLLFUQuNFqe6xwCPegeMOLOE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/746abba13b.mp4?token=Nnvf6qXPBKgiEcSUJ4cNF1f8xlaEUoIsf_YeWyLVwG29sU17y87Nm1YcYDKq9w48xRHfpk9SsvoZHmWoyd_YZY0u0nDJ_ifzcl3F3lzwWeVyzL5ORvQyl-lEp5AFTV-2jxG_iIRtpGumJE6NG8T9nrs4ueEnDY7lbMQTNrqs7jM5k53zhpxzFBzfH8gmdTSz7yMVvsT0MEa9Zn48qkpEdC5A5tZpXX-VgIg4J4vpRt0rCRsg9SRKbQtHv_i6Cwb9toeOhqi6VuBAOxrfJyO6Dvy9y1AysqmGDHgtHrKgIJe9mXznicMffLfBFuyZVQBKBy2esVkeSB0cbPHLchFgRXv-rNSPh_GFZyMv-T5AcwAbLuYEvYyhreuVkK50GCYfSQxprZLkBnTnJYxJKhXnR-3nYyY-NRvNa-2Wh3dVn_LyApG3S66oEw1sRCrN_3MFtuMp85OK2aayAHOvCzyCmtNrr814rzSCkIoMBHGT7tHbp0WNJ4iYsO1yOIT4-7fhpv9IvbCLYsTo3p98SUWCa8Kl_P23wdGefpmUvzin3OVIWR7aTPEv72Zgn7e2l6W1BlgGb-KT91tA28UYWfMg8lClCw_nOh9C72AolTKRt0fFQszO2JTcRdnM3FmL-6YJvWORECOqkOyNzxxwbDEmLLFUQuNFqe6xwCPegeMOLOE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی فوتبال تبدیل به یک فیلم و اثر هنری میشه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/102010" target="_blank">📅 19:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102009">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eLxBoaPTr5EmMfZPjWv-ej0ySzKyo-tevRRhCPomjOi0F5JHCnWW2UcxWRaJTj-pi2KrQZubpHs3NjYlMBOlfFpkWNhCoOPRPnEgd4BzzINFmCdL6kbPX3yC7WWFjQMT4GcWN3PzMlCBQK-XI-nrTgwWTF7A0_kuEQmnuFjDP8qAtG0rCi_EB7ZMsBEMnLkc-paO1moo4CYOyTr-KBqFVqyQz2nqtOhTlUuJcQVOnyn7s__Ix-0QilJRTJL_MTUJ47JYyINAt3aBI1YAFpvSJ36WG3Yo1BvG8zg_a9pAeo041rLP_3fEkbAxuNXKMYpQgkS0c3_9_rXCnVo6oqQ-zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
اشرف بن عیاد:
کار تمامه، مدیرای بارسا متوجه شدن که موضع اتلتیکو برای فروش آلوارز تغییر نمیکنه و نمیفروشنش، حالا بارسا منتظر واکنش آلوارزه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/102009" target="_blank">📅 18:52 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102007">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jivBwVHFUfKdrEKCOGxXjoNOLGgPMsCoPYFzOjOY57-OYMrwF033LbngmZjs0Pmr_0310d5sbzYf1-JTGkKe6xoR072HjW_KXopbo9EZJ_ntdOJpb2OdHulxREtcoeIMZ9eAlcCpd6LEpzC8Ghiqg9tU7BCTdFTHSAXCSansJYXgdM6sjuBmo_wdVqsBNZ-Hd7DxQkOggucgPs9Ut3Bjex6Tq7DLVLPoNOUZyCt7HHNcuS-tFPffSG_mngDibI6J04bd1pmaOl3nLl0Fh8XEkfd1KCjFIAvvlTBeDzlQ6Nwn845PyMuvwZsZIPhpGhMqfD8GmqBSl88iWSkmcfjI3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/idBAEuetnQdGY1U0JvoCph4O7k3peCgf5C3gpIlhEuImbL5i54R3SF2xGU72g32u6fdwj0T5mHB_dvIjs84N7pFFl3XLSvTlm9-PWJ0JnkenIlawSTZKz00kSLvLETEWFqOD8t18z7JzUiTmvuHmga8IlYlqy4XitvgX1iJk1rnxcJ8926L2uCFq4lBzO15om9B0uZflVTlM1ggN7B86cwJ_mB3otp8lszMSSQI4chvzqrXFQJcoXivTkd4SHKKdefVIyAmOzJK_TItRXAe2XpoNaRPSbLqfxCWh46hBhkNyAiGIBNJLbFHir5vtDWMXd_yL-xL684F8g8BlvmGjqQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/102007" target="_blank">📅 18:28 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102006">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac77f90860.mp4?token=fkhbJCguXE_ARJo1oOXisjXzHwx-Qs64AxxNiGJWPLIdP5Kyr3SPUyJqSG94Fja8hRtqi4m1z7H29iXM11nULXW9ype6VljMOdpxnYBwEwtcDi6m7fNB2wjHwj3llt_x9WwsqpgAFSxftoJ7YBeRNPLx1HJdsDCmfqt5jMuj4N6tlefJJvi_pHU16qAQ91v2crfaghMjoOgR4ixwCKNNlur5LID8P4ExhagEbcEJ-y1nN0KWZ1wjpOp8XIlalgA9ZSvx3U2Q_2-IedNjjnI6UGuud8-kLP99w6_JolHtn9dpHrQwUyseYIeQBuqvuTcIDHx9F1Vk4fJbeSk2XLwO5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac77f90860.mp4?token=fkhbJCguXE_ARJo1oOXisjXzHwx-Qs64AxxNiGJWPLIdP5Kyr3SPUyJqSG94Fja8hRtqi4m1z7H29iXM11nULXW9ype6VljMOdpxnYBwEwtcDi6m7fNB2wjHwj3llt_x9WwsqpgAFSxftoJ7YBeRNPLx1HJdsDCmfqt5jMuj4N6tlefJJvi_pHU16qAQ91v2crfaghMjoOgR4ixwCKNNlur5LID8P4ExhagEbcEJ-y1nN0KWZ1wjpOp8XIlalgA9ZSvx3U2Q_2-IedNjjnI6UGuud8-kLP99w6_JolHtn9dpHrQwUyseYIeQBuqvuTcIDHx9F1Vk4fJbeSk2XLwO5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خشونت بی‌سابقه در لیگ‌فوتسال بانوان برزیل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102006" target="_blank">📅 18:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102005">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YY6X5ja66gEGrBF-G2oKT81xm8pnKKrtnVk1t9GAahzNZmsvE0VlWGFSpieXGL_UccCFdAqk4IO5_aER-AvvUECvjj4JulvaKcSnlrFDDXG2eIx4A0iU3LB1onQs015Fiy_bcIk2qaJUgmhMN2Pd13Pfv_ULMBT_o7UgLD0q5rQ34c-NUK5WHzhQqInUiGZiWDvXKw4EkUqtoh-xgOtDI1M7GV1Dj-uNTz9DqyRODE6WirVaxRWcNgQ0DGZg6ESvJC_eu2mNHfBWTB78hPJoceqy2zf8Mdp1MSrJlO-iejma01TedGvSd6V6wT2q0iLarYwvhjl1mfa4fvMfkZU6XA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/102005" target="_blank">📅 17:50 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102004">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aSjsVKVZpVKpnX8l42AYNJDarkMtgPcB1ZlTwuUK_pygatBgGvBuqHf1dc8SBAF6OwDBVFxzOU7GT4ACtG1WjA-zFu8zCXp0TVFTTcXpsgxume53nKzlQQXBSgzeGiZ9mOYIBSbco4Cls29FOfq0mYDpbqGh9gaTnCJy3f0mt0oeYlaQL_Xtk9OSQA-N5oPyP-7a69CHkgRfuZyPjWGm8B4H3WkL7XkurjepernRAI37Rv031rGS1zyxro_NZlRYm2jartRSu2xlj8aEwb8iRffeeHwVa1C_qqLNu1-Nw_SouCOe4013Bp6tpAVM_hWBto2VT-euEYq4chw3rCGIqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
متئو مورتو:
فولام قصد دارد یک پیشنهاد بزرگ به رئال مادرید برای جذب گونزالو گارسیا ارائه دهد. آربلوا می‌خواهد او را به تیم خود بیاورد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/102004" target="_blank">📅 17:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102003">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KdWCuQnhLWwfHiePodooP-K3yRRXY6BxF9yz-dxaIlnuMN8gJtAWBiXARRGFnGkUHTl3iCuXC2IJhPNelOVLahA1BA2RfScF8Tv97IbZZW-tBXicjtvDZVodDslvZRlCXDnqEyPSz1Zi9P5dP5hS2gkCNTfmR9BBpJs_ys-7S1Dzx6AWbcpvbexqg4w0QNhrJXZvh8MAFYnxa6jVgk2Bz4DczIJnWWkOj6qSinb12WiexRXkxJMuZ_wydk-asQjtADqfAeI7KrXFkFZ2MVXuhspTnreI4FgwxcUy4tdovypQHskupM5SqpiGIB_8Pg0TPtU-1AvT6AlOuOUFkc3C3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سانتی اونا:
باشگاه الریان قطر پیشنهاد خود برای جذب جیدون سانچو ارائه کرد
باشگاه قطری در تلاش است تا وینگر انگلیسی را متقاعد کند.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/102003" target="_blank">📅 17:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102001">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🏅
فوری؛ لینک پخش زنده بازی پرسپولیس و پیرامیدز مصر گذاشته شد
💬
@squadify_ir</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/102001" target="_blank">📅 17:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102000">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9608d1c2fe.mp4?token=G9RdswxCEa0O7DPWU-50fIrl4kHoLvBPnSq40alVxZEoFsZFUsJDqhWEopV20Blm06JW_Emx6cpC6UONShFHiXw-7D1CcLYVZs6mljPo_MsOS9t02aiKtJISf4CID4UExv-NcejjVkWKQnqyYI_jXmgYFlcjEEdrtK8UZK3BnUhbpDiIBaK1YSdYoPYJ4Jvyw4-7OH6YwwU7xjHlkaaWg77tzBxG7ZnEW-aFK_2xBjzqmEPrSt8uZHUBwsJoZIVVIfR2ibLaabN-t__tUEYkIrq4V2es7UN_WPc0O0EZUHAwM8Ak_HQ3wtX-vRc0lT9HYlKcARN4IJsWklowj32Ehw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9608d1c2fe.mp4?token=G9RdswxCEa0O7DPWU-50fIrl4kHoLvBPnSq40alVxZEoFsZFUsJDqhWEopV20Blm06JW_Emx6cpC6UONShFHiXw-7D1CcLYVZs6mljPo_MsOS9t02aiKtJISf4CID4UExv-NcejjVkWKQnqyYI_jXmgYFlcjEEdrtK8UZK3BnUhbpDiIBaK1YSdYoPYJ4Jvyw4-7OH6YwwU7xjHlkaaWg77tzBxG7ZnEW-aFK_2xBjzqmEPrSt8uZHUBwsJoZIVVIfR2ibLaabN-t__tUEYkIrq4V2es7UN_WPc0O0EZUHAwM8Ak_HQ3wtX-vRc0lT9HYlKcARN4IJsWklowj32Ehw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
آنتونی جاشوا، قهرمان سابق بوکس سنگین وزن جهان، از آهنگ سیاوش قمیشی برای آهنگ ورود خودش استفاده کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/102000" target="_blank">📅 17:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101999">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57f6f418b4.mp4?token=XxkA9-1ZY5L2VA4dlWsFmQaURpIivAxlWoC480xu5JSCX1vY_r61Ph-oCeTNRajltV2rnH2MK-wYh_MWoDH_Wb7emhUoaLyTiWmhntltre5K60VGP1hxk6ZsJWXyC57i5-y1ZVmiketz4sMzK50cQn05O6Lnlv2e-tIQWPzqSQY97QlF7StVlloR6N78_lmW7gBC4ZjnJ8_aC0Rx3JnM6_KuSj2qxlCpfw6cL7bysWzyTqGx9Of5HOv3DswHhaBW6ii-uxFrxoF8IHeISQVfj2ZyNtvTONFzfqRMeA3wR94IMua_E3DGhAwKOdrCcXUku6uleAixd4iUWDSeY868MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57f6f418b4.mp4?token=XxkA9-1ZY5L2VA4dlWsFmQaURpIivAxlWoC480xu5JSCX1vY_r61Ph-oCeTNRajltV2rnH2MK-wYh_MWoDH_Wb7emhUoaLyTiWmhntltre5K60VGP1hxk6ZsJWXyC57i5-y1ZVmiketz4sMzK50cQn05O6Lnlv2e-tIQWPzqSQY97QlF7StVlloR6N78_lmW7gBC4ZjnJ8_aC0Rx3JnM6_KuSj2qxlCpfw6cL7bysWzyTqGx9Of5HOv3DswHhaBW6ii-uxFrxoF8IHeISQVfj2ZyNtvTONFzfqRMeA3wR94IMua_E3DGhAwKOdrCcXUku6uleAixd4iUWDSeY868MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
قلنج‌گیر معروف ایرانی که با درودافای مملکت ویدیو میگرفت توسط پلیس بازداشت شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/101999" target="_blank">📅 16:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101998">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a860d22dd.mp4?token=H1BezFPmlpK0R3XshHcq3jJJDS76y6L48Sbkv5c3noqdOYhfnvpAUC2GELzapDGOHFfHQqrJOcn8TrEPzZ2UTeHeNJM3-zkgcJ-4PMMQFtm8vIp5rUc5mn5V6rE4IBPjojYq0vJ0UgxWGgVnZr4F8URL3VpofLCCz73o7bXl4NEswCWsbrqrJtNRsA8SyIUbCpYYN7Qp08LQK_hBEIo8CAN_ZWKkZpRwWdXieP3Jk2n92zB3dNTPvY35AuAQdxZP1ayLzHs5XaUl92XTYS9yXOJz8tBNV7s2SZ8izDawMxD_bm8__M0KkFNBIJ1Ax9unO7K1fkIi6k0CdwWwvF1YQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a860d22dd.mp4?token=H1BezFPmlpK0R3XshHcq3jJJDS76y6L48Sbkv5c3noqdOYhfnvpAUC2GELzapDGOHFfHQqrJOcn8TrEPzZ2UTeHeNJM3-zkgcJ-4PMMQFtm8vIp5rUc5mn5V6rE4IBPjojYq0vJ0UgxWGgVnZr4F8URL3VpofLCCz73o7bXl4NEswCWsbrqrJtNRsA8SyIUbCpYYN7Qp08LQK_hBEIo8CAN_ZWKkZpRwWdXieP3Jk2n92zB3dNTPvY35AuAQdxZP1ayLzHs5XaUl92XTYS9yXOJz8tBNV7s2SZ8izDawMxD_bm8__M0KkFNBIJ1Ax9unO7K1fkIi6k0CdwWwvF1YQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BDpcxeCJl039usYaoIgobDTxwPwVu6MHQZok5Ji2aaO6ufnU6p-iZ21q0c3OPBh2efu9RXgz-mGwGQ79Ng6Vo2f3FB9tKS5VwmwwR_PND644bYzMiymR3sQJMMq0iTYLkouwc62XVdQfSXVtbfrz7EaCqkn9wk1YAa_T97iYIBSkoAA6h1NXF8xCj9NYfbevSg2EXZNupnE24SJlBE_6_DldcFDG220x-JSF9LGqdKZs77wilXT-4ZTOPBD8AGQ0ebsfm5ro-mHQkapD3-ZdpAUPQCZo-HywPn2Einnq2UqWCR_2TwmnDW5gA2zZE4XZMe47PFFfmnWECqA65Vny3A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/101997" target="_blank">📅 16:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101996">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58250e2a71.mp4?token=LXzrShXccSS4mzfsZSGyaoowU1p6WPcVixcYABiY_ddPQVEl7QYtpxjkRx3ZBR0lNxlsy9o19Y6wnaG06VvX9Q6NKqx9xfsbdlrelHtof5QQxDk5ybcreQe_ymkGGHM8mlDMMhPmTEimKn9yfBPxbr4LFcQ_VGSgPP1p2cj4iQBpS8lzGot0Q-rxkQdaNocy5Z8GCnSGr6Vm2lTdYDpGnscIDrce5KwrrYM4dDr55-nBPt4i6z9OYN3O0TXseq1gMl9xLQCkwGPuz965N8kI1j-ffX5ANwAGVnPx5udCbFFafOMicGhLwLLrQUhRPv15Ul1cpBlZgr5ROtb6E5OrbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58250e2a71.mp4?token=LXzrShXccSS4mzfsZSGyaoowU1p6WPcVixcYABiY_ddPQVEl7QYtpxjkRx3ZBR0lNxlsy9o19Y6wnaG06VvX9Q6NKqx9xfsbdlrelHtof5QQxDk5ybcreQe_ymkGGHM8mlDMMhPmTEimKn9yfBPxbr4LFcQ_VGSgPP1p2cj4iQBpS8lzGot0Q-rxkQdaNocy5Z8GCnSGr6Vm2lTdYDpGnscIDrce5KwrrYM4dDr55-nBPt4i6z9OYN3O0TXseq1gMl9xLQCkwGPuz965N8kI1j-ffX5ANwAGVnPx5udCbFFafOMicGhLwLLrQUhRPv15Ul1cpBlZgr5ROtb6E5OrbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ieWugNGInf-WggO_4t4qo-dwrQrgnVQCZGCUumCPGTphUFS-hzXa3yLborbSOyeZnV-oc5StKC439Xsa74vi_mDM__bMIuX9HLeTnv3Mux3rRkfztvLukzFIGq02zU03DyMTqygO2IU_rv_tUjb6P14c-jM2W-rQqXk9l21vNUCUOrgbPTb947yY2IauBc9i_AHNmJaOItYyTVPe5V2jh3sHXRunWPfHdfdk3HDWgSpRt3-iAOoK9lsTF3OeK9jbkJjLkEnPD2dEJnAlVlz0C1UgpodRgQQu62zYTKV3alsomOCB2xzTE_N90JFrU96DSsWgh2HNxM7jQEcHpwMaew.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/101995" target="_blank">📅 15:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101994">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🔴
فوری از رومانو: لیورپول در حال تلاش برای تکمیل انتقال بارکولا است. این بازیکن تمایل به انتقال دارد و اولویت خود را به لیورپول داده است. لیورپول منتظر اعلام قیمت مورد نظر از سوی پاریس است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/101994" target="_blank">📅 15:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101993">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sswRBXGKpp760Tvrg3jFdaerL3Uq1odIjkR7riHEBNhxBGhC3M1545VmBxhehaj7qIesZhxHeZxzVc0jSawdKVM-CMNBjvU0rVbaoYyhQ9BBZUy4vYSnJdsctbmR9PmJvo6OAHJ86rVyn5vk83Rxh-YkEr6dGscf_4XVrMSGWzcba9fn5RhvKlxrZIr4EZJWRaLiiFK20INLZWUKplOS_Z2Iv2IEoBHSrnko2ExYfkpd0Gj0xrlHSxbHwPgR7BP8ES8AAkPCLX8HPur528N5JBHn2NWB5GVYGSg14NWBlkyCQqf8CJ9XVJ8fovneaXQPxa2uB47D64_qHerzB6p2cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
فوری از رومانو:
لیورپول در حال تلاش برای تکمیل انتقال بارکولا است. این بازیکن تمایل به انتقال دارد و اولویت خود را به لیورپول داده است. لیورپول منتظر اعلام قیمت مورد نظر از سوی پاریس است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/101993" target="_blank">📅 15:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101992">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45e9d378eb.mp4?token=dAqOnDxrq2-1Jd29iTHmeJfy-DUP9CYzSvmUFh_oA4edIAjg873dMhhvpKxGvUVymv5Jo9f4XvvS1cHs8OiQi5F1gFyZyO-cU9iN4JP1ObcVBCmIDHZjwYWkWGc6LSYx53QXfv8Pq-OpP8DUrny4NM93S0bNqjX6Gg44Mqkj9Bo-KO6ObcTmoBDoI7O8BQVTOlliyCQ6-FfPA-XolKE-mMjM1tsPLLqtfS6oxzOsQ7xoFAu1t7R41kWl_HQUUJ891Mg-swPiwoxqfzvKGZdWH9Ha9UzfNBi7c_bAnRRPF4Mxx9CSC-7E7oHmLoVA_nPpiDJJtOhy1JWeIpAd8zMV4YntVOvhvIeI__CZ2aw9r4-X28_uDlYsm-LpMKAPa1j_iRVywj8ppXtChiPSgtMpr73cRwvo_PR3uTlV1Fb_NN1IpHA-zNEDdN6xjwE5_fsyre7d3dItwQIWO-roQVS-s9BDYTM7Y7yU2iIQcQv-6_UllG0AdmE_6af-NfWxkFh3AEdHINfjVlgbPo_1gL4o3nrn0Eb_4PWVlsxgA9E7sxj0EgqrBj9RAqXf_Tolj62E_FzlNz2TiVNMo9ktyXag6t3CiCijZ4OripzdEeOo5k325qBW2J-LEe9oEE-B4BDTgXMTxyBGGZS9Igvs5CBDyTFXW6hYwFwDpwAsbMYHWK8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45e9d378eb.mp4?token=dAqOnDxrq2-1Jd29iTHmeJfy-DUP9CYzSvmUFh_oA4edIAjg873dMhhvpKxGvUVymv5Jo9f4XvvS1cHs8OiQi5F1gFyZyO-cU9iN4JP1ObcVBCmIDHZjwYWkWGc6LSYx53QXfv8Pq-OpP8DUrny4NM93S0bNqjX6Gg44Mqkj9Bo-KO6ObcTmoBDoI7O8BQVTOlliyCQ6-FfPA-XolKE-mMjM1tsPLLqtfS6oxzOsQ7xoFAu1t7R41kWl_HQUUJ891Mg-swPiwoxqfzvKGZdWH9Ha9UzfNBi7c_bAnRRPF4Mxx9CSC-7E7oHmLoVA_nPpiDJJtOhy1JWeIpAd8zMV4YntVOvhvIeI__CZ2aw9r4-X28_uDlYsm-LpMKAPa1j_iRVywj8ppXtChiPSgtMpr73cRwvo_PR3uTlV1Fb_NN1IpHA-zNEDdN6xjwE5_fsyre7d3dItwQIWO-roQVS-s9BDYTM7Y7yU2iIQcQv-6_UllG0AdmE_6af-NfWxkFh3AEdHINfjVlgbPo_1gL4o3nrn0Eb_4PWVlsxgA9E7sxj0EgqrBj9RAqXf_Tolj62E_FzlNz2TiVNMo9ktyXag6t3CiCijZ4OripzdEeOo5k325qBW2J-LEe9oEE-B4BDTgXMTxyBGGZS9Igvs5CBDyTFXW6hYwFwDpwAsbMYHWK8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
لحظات خنده‌دار از زنده‌یاد اکبر عبدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/101992" target="_blank">📅 15:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101991">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d63baf35c4.mp4?token=spzwec3CMh-C2G86RMRyt-oZ12uTUw8nxnFbcln9ES2FBTQd6fAtc6VI621etsL8ISlzNB3yeBIivVCEeZDIYCop3L21onKnycGMNU7YjvuZwzDP-ELsmT1yWxBItEMPY872EudeFQNgwwXe6W-jEApjZZFYLCs_bUexR_63cuat6rsBQo62Sh09dALwEac_5xRegn5RgcUN5-3gZ3Og1DCjUB4UGdt0yA3V9FSKXSrPdPnuM358H-DrIZ5pBfjYQqrIqkL4Sm0nEN5XkbO8pR5ebvI8S3MG71nhmXS_PWZlMeOGNXl5bANqy0rae3-H-W0BpLXD_IXroA3pNeZ-3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d63baf35c4.mp4?token=spzwec3CMh-C2G86RMRyt-oZ12uTUw8nxnFbcln9ES2FBTQd6fAtc6VI621etsL8ISlzNB3yeBIivVCEeZDIYCop3L21onKnycGMNU7YjvuZwzDP-ELsmT1yWxBItEMPY872EudeFQNgwwXe6W-jEApjZZFYLCs_bUexR_63cuat6rsBQo62Sh09dALwEac_5xRegn5RgcUN5-3gZ3Og1DCjUB4UGdt0yA3V9FSKXSrPdPnuM358H-DrIZ5pBfjYQqrIqkL4Sm0nEN5XkbO8pR5ebvI8S3MG71nhmXS_PWZlMeOGNXl5bANqy0rae3-H-W0BpLXD_IXroA3pNeZ-3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
دستاورد دیگه تیم‌ملی در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/101991" target="_blank">📅 14:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101989">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UPw2Fcaxy0Tjyh8wugozH622Osf3h7Wb80KNaKBDHILZvTTFH03OROA9SMewC3TfsHdbBQrH8O2aRVXOHsOMZJGKHLe-Fpk-GZ6wT_KEFTxs0zDYxAeQXiVXswxdXPeniZGX5tLhF5CxoxNd1PxbGqJEDh-76ce80ZOMwQ0M1ztKRKc7ofRDoP_7M0wYjd-h7RhLkzvnobGC-8kOxKx4zvRPdsKJHdrEMqGkk6LeIoCAdkBkXRSLadzeznvSoXv28kUsIz6kEgFskfGrOZ6PCRsvD-NDwyMhqzgABzRfTrPXkZttdgwjp9Z5YSdgsQO75CePFXfDj3fpkDnP7aXPbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CfGZNI5sRM9-ngQozwQbFKeKS9tS6DD53g8KprYk2_jMGtsZE9UMI6kQbNf3BeFyV7uI_DN7V-mVMzOG-hCZawLIuANizQgGTWfBmYMUCkLpSqKDcXiy8weWrR17_FGPMCoAFvCE2j-9onNb4VMfmoBszKXGrT5cLQOeU2KLOYKqKkwTS-KBtog0JaxdGnc04tiILlZibZUfmt1j3Zk_whF_T0kX_cerkqVfvYsb-prwt9psh3E1nurThOpiGlzSskhTxCsNG5Q7GSxLue5KQywWoBKsdpFyoJrNgcj19PHDYxFKPnnIWVHgCBtgNKo_YDmr7pPzd8ul8Ts_nY0JUg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
اینس گارسیا، دوست‌دختر جدید لامین یامال به این موضوع که گفته میشد باعث جدایی او و نیکی نیکول شده، واکنش نشون داد:
من به کسی آسیب نمیزنم، چیزی رو از دست کسی نگرفته‌ام؛ فقط دارم زندگی خودمو میکنم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/101989" target="_blank">📅 14:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101988">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/310ebc00ec.mp4?token=pZmFdHkfiFvm7LtLtVmchG00ZoX3Lfy9heoNYHwR7eWydfy3oT9TneBS0SO0b5QwO17cFlzlqv4rjW6W8p99SYqbDY10lQhKC_nozKLXub_X2Gz_rZOdB4QaUat1oQchxj4-QjnPgOqtECCoggVcahXBUYdacQf05ona_4LJ7UTwvPg48ZK7PZ9kI_6gcSylowrqf9vvQAkyKH2JwdKrupQPEUUTekbOEFVYGC5oZlOBv3PYkNrPlp2IU47C8od2rug-uvxXKPnuBPnB27i5Ai4Yiz0iduZ7R1qV_qyMLIUsqrL3mORaGsp7-ijJd6Kr2YRm-mwOxTpgEhVghF6ADWmfbkQYkDbpncPO5iy4thC4F7bwFQri20DZKpITpbQr8Wkii__TIXkYHesj7xipFf702-bSmdRsmklwxt_syMcBHDs5ZVuPF1gOqqqLUXI0MxZ2-2eD143aQy7PZmyw4IePPLL8el2W7cls0ROv_PGPgBDUaIRShgfEB5A4udTivnrMH1Wgpo1BPxKGSnaxGA1Pr9V1BlMTTiozUk-Ddc-Pg5kuko2zOF3NTmh_5PkiWmfkqNlImAV3-Ri6zktRSo_icqk65iq-gssa7xWRAXF0KYpaq2iIQCfhi4gBZjyQ5CCJCCDCsICcYb9JuiY09PuRtTgRd3MQFpy4g-ubpLk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/310ebc00ec.mp4?token=pZmFdHkfiFvm7LtLtVmchG00ZoX3Lfy9heoNYHwR7eWydfy3oT9TneBS0SO0b5QwO17cFlzlqv4rjW6W8p99SYqbDY10lQhKC_nozKLXub_X2Gz_rZOdB4QaUat1oQchxj4-QjnPgOqtECCoggVcahXBUYdacQf05ona_4LJ7UTwvPg48ZK7PZ9kI_6gcSylowrqf9vvQAkyKH2JwdKrupQPEUUTekbOEFVYGC5oZlOBv3PYkNrPlp2IU47C8od2rug-uvxXKPnuBPnB27i5Ai4Yiz0iduZ7R1qV_qyMLIUsqrL3mORaGsp7-ijJd6Kr2YRm-mwOxTpgEhVghF6ADWmfbkQYkDbpncPO5iy4thC4F7bwFQri20DZKpITpbQr8Wkii__TIXkYHesj7xipFf702-bSmdRsmklwxt_syMcBHDs5ZVuPF1gOqqqLUXI0MxZ2-2eD143aQy7PZmyw4IePPLL8el2W7cls0ROv_PGPgBDUaIRShgfEB5A4udTivnrMH1Wgpo1BPxKGSnaxGA1Pr9V1BlMTTiozUk-Ddc-Pg5kuko2zOF3NTmh_5PkiWmfkqNlImAV3-Ri6zktRSo_icqk65iq-gssa7xWRAXF0KYpaq2iIQCfhi4gBZjyQ5CCJCCDCsICcYb9JuiY09PuRtTgRd3MQFpy4g-ubpLk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
👀
چنتا سوپرگل نامزد پوشکاش ببینیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/101988" target="_blank">📅 14:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101986">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uzvjKLB0xMJaQu6XmUhVl3uAv8tpif53yk6bMu40nz1E04NSxnNRVUjHrUsFP1s2_ZI6kGq6k0HCJSG77OwyCh3kgja48qSGlvh06gn1R35-dcwrNlzULaVilqhdBp9Jnm-iz3dHCOKU6cNO9MQp2AJIlR_tJEbZbhve1_A7fSSIN3UtHjpCFIi70C6Sv8UyCKDaPVFSJloVwl7UzLeHz-GQngxuQ-h4OgvVGhnTVbPMmpL2oFDem2V3FLYf-zmdMEJjQ1NsaGW0hUjBB4kMe6nCiPRkhFXO-97owB5aYORbeamRgY99e7jnWEUMbFw6_mwHNMKTz_FJUKIAlRCAeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bgvl2FyF6PK8qp4qI_SiEP1TZtTu51MS4cckqb8cM3qZQBbk-OlllmtDlkp2tw76zu-3Vstrs9wboWa_rwYhABa0WF7JJZEhjb2kaYV1mWqFjt6f46xJvnTaLlC0gPGXyq-Qqf8bxLjyil0v69AtdVdZ7m5QtXprMpWGkK_Sal--sRawaTgNCoZbPAb4upl6PF7dB6Sr8XsUse-KlFGR6MINdF6Otifp8DwP5qIkjUS6LhTgnBurLYbH7UPCEyM8Ntv1EaibgsXTK9LOU84pVfxr-SZ0I03SdUTo9n12Naj3rjA1BJk6oov5pU1bgu9r7DPmE8RsHNd-tCQ7PUXneg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/101986" target="_blank">📅 13:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101984">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jCIy8OpJhBfulC-_xfVs65qGpxUVWb7gcPePkM1bmUqmb88zG-AimA36-XnSzaFhR_xDOqi9XdmEpot9oXLTNf_30-ojTa87kOTjZCU1q7RJiDkIA96FF3JCrt_fGUGQl3GTGi7LEHcAikyd58cPfWQWu1BvShBJT8XeeMPdnNJER-hgf3Wl6DniJeQ9zrjse5VCqkxupt5lH9HAjyba_BjJQYFLs78X6oKRazmU98j-DUxS3xibq729XJNBOblOWwVOUVjlLCr6p-W1fRAnh5uNaol5oDJcTKX9h2YNyx8LNZeKQfsAnATnsSV8uzb1NKJSOka7sVLvkdP7FoA_Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZOWcpphZKANEoGvFH8cXcTt4WiWwByhh0aFy5czBFXbyGVCauehP4UOTWqzZppFDg2w69YZ3N8mpmEBXwB1acOqji2_mySvNHRbpnXksWAeOKX6ZVSGyiQH5m5jIyqfea0srJz6DbuMgp_8zpw5FzIeivvSs1E2afw1QiK2lBi5MUMKULiO6FZNlpKielAqF-AFM-ggEJ7mTcmtdVs3jGomMdpwL5VFqFQ-_6bcKNpUzyJDRuPOzA_FIawY0kfmdoT42lXoeyksNx4LpYtAmpQftbU46h8l-YmApWBp76sbEnx3tQZw6FAztKokWNbbQaGgAl7PbA2JCFnjE-zUETQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
جسیکا توگا دوست‌دختر سابق وینیسیوس جونیور:
این فوتبالیست‌های سیاه‌پوست فقط از نژادپرستی شکایت میکنن ولی همیشه با زنان سفیدپوست و بلوند وارد رابطه میشن. اونا هیچ‌وقت با یک زن سیاه‌پوست وارد رابطه نمیشن یا چنین رابطه‌ای رو علنی نمیکنن دلیلش چیه؟ جوابش واضح و مشخصه! خواهشا این سیاه‌پوستا فاز آدمای اخلاق‌مدار رو برندارن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/101984" target="_blank">📅 13:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101983">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
په‌په‌آلوارز: دیومانده به رئال‌مادرید تا 2031
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/101983" target="_blank">📅 13:11 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101982">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iUcfNEGkxYEbcfxSfUcOv_QyA7k7wAXOpScWV4lAFKTX-lwZeeyYTsGG8gRC_LPPMCs7IfRELLRb7WujUiu69MFrG-H3gvVyhvGS68W0eUMrEDUzpulWxsZEFKJ071A4q7rWZThRTK3SffvUh-GUq0YL3Myau_lxgx9IKt3TLD__-VGepI97SGI0qUj0qAvXWECfskvGbj07-VcMa234aqvPaLk8DXiY1Bu4C2AU5zLCgaYth6DDbsUKwtQrR61rr_YDGbasXUhBkQ9g7Fi8zU6UwUCwGQb79sGbxHWb5nJJWyWi0BI-RRjmNQLJkgKQ-2WazdtbIDvgD5MWPiSZqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
په‌په‌آلوارز: دیومانده به رئال‌مادرید تا 2031
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/101982" target="_blank">📅 13:10 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101980">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fzPGnsBawigxJUonxUa8YfRdDImdPaOvfqb7SKihjfL7432LG8mx8YPEHFseKKiZ3q3e2VltA7QTZGTMccV1uEYehrPdCkRIyHa7iCJL3FD1Lq15rGDkzXqk1KNZNPUd9OMHetSluJl1azg9n7-aYD5eak3vCiqxvGqM1cD_ndAWzYn3tDlVbBA5l-or3yiPd9A_4Qu4rUQtiwvMbp5Bsf1hO6WBPkivjbmxNY98UV_i-PuotamjLGuORhDddTX4aj7i6Iibj0yu7EJFjros-fmhGOlruinNQowbNBnvalcVkhkE6k2-3n-L0Q87Wbzeu2FzZeL7RSmZQpZbSEzhIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DCOnxyJsCpo56nyvN6bbTmHqeoqTmKYpSOS_wHlgYYTShTQwEMwbSAgKWhkU8NnpEa5MoBLtyJtTaLNflORPgpWhgLYjBnTmX1SB6BYO4VwOUkQqgisMo5Di7HdGzS0ppcpFc19He_YKBqq8kzmPP4WyoiRtaDyWALs2x-qZfpu9hJkRYXlfn9G8bRMLQnbRxqwadvJuY3gqdF5Ut7B8OJHIbLqreBXKgPW23KHBMruFnQeq1qVHSdHKCtDfSTHr6aaz13Mzlu_ciZIPPjmY_CcOiNDQh2XC2kc4C_YBsMIaGlRby6DbI6LzxkFsVCL4qdk-sVUrUUAcspUxj2Yxfw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/101980" target="_blank">📅 13:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101978">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GsPqFumdPJw-scu75qJ3vR4wEDXu04BLNauvenh0fr_eqOT0wIREPtGnELtgi9asM6Iewtc9wJNznSJbODldPxMVsKhluzR-9y8erU12S3GiBuh0RIiWviVHMYf9cifI5V9o8QEvS3HYXRZRJgjXjdq0oWDSGFAo2wQOgw9kUljA2j9ih_U1yTKBA6GHB6gWI6H5O2hs_Dhb9bd6_K91e3Pazpk_MSj-ku3mCPCJamb4r037lzTNOuLUuid0ZV9nuSD43OvGQVLFfCfun6pZ95Tw0SffX1b4oivb_KQFhIcA3lLNl47_V9LQhvb4R6eZAUSj16uKbGnp7YUYiYv58Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L7RobYQWUDvBMAVssnQQZgGL2Kc7hF6CcMSF3gaenh4WzOpvRrab5OKC2_2c0-J3ao3MORbo9YIZSvwt939F-iQa_CaiN6tGRqmRIRkdYqqqpsCyI63EpgzHg1EKehv3GqgmWBuLipFUKfUMNoBOmk6tJtZiRYJ1McxuifCC0fMDCSb8JGa9zA0yjarFeuUWOlLjiUn7fonRrzEND3DF9FeT57BNOPUeEfcQm3jfkEEs1W8A-6xoL1alr3GJsvV2DzWU7o4eMzn3TOKxdNpr4jTTAP_buZIVEDIbOrnKIJNG4x9uefMJYxQp2A3pmlArEucKX61qOIhajvopzufXfg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
الساندرو نستا درباره غیبت ایتالیا در سه جام جهانی متوالی:
باورنکردنیه! پسرم تقریبا ۱۸ سالشه و هیچ‌وقت ندیده ایتالیا توی جام جهانی بازی کنه. وقتی بهش میگم ما واقعا جام جهانی رو بردیم، تقریبا باورش نمیشه. میگه: واقعا؟ برای نسل بچه‌های امروز، دیدن ایتالیا در جام جهانی انگار داستانی از یک دوران خیلی دور و گذشته است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/101978" target="_blank">📅 12:40 · 04 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
