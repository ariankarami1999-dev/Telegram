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
<img src="https://cdn5.telesco.pe/file/Yg0vjgrv1Ox2Ty-ArkAxqB_5TKLeR3ZWGpdFSEFx6-OIZDkKfrwy_0R5jnVa_gzUpsOWUK1dVV-5JgBxsIHP_VTVbk73YU1FDTmCTbYpuWa3Wu83z46eCsORyolQ4irgm_pQlnFoPnG_4YpcFoSmzEtYJGq93aRc-nqxYFZMyVMCMtXFUBv3Ow1G8E9U-Q-3x09DqIX3WWNdcRdFZKnCvy76Yq0Xy92x3MeCVKzYrr6A3HpWAKHUkwk1cu2HM3Tf5YuRcUnAbQbbxhs-eXPx-Xo4j6IPSq7fHMJ_tZN5FOtJEs5HlSsliEI3Xexc0fEB_n-BMTxjqCNHAEIoXn_fhQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 656K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-11 23:28:44</div>
<hr>

<div class="tg-post" id="msg-97682">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iFwD8FRrv7UtQuMlNIzrrqlKv41D-fGgqji54eP9DCctP5AL0hi6HBA99NFurLxDapPkOJ0rsn9KtY_of84tHH5d_ao3JkNyNidfbFEeroyUKcx-CLQEtB_keoXYqdZayssDVMPRSS9qeFCoOEKE9jhpWwSpc3IqFxY8VpyM1ZVTASDftTqbOcF_TuKKN2qBynXiMDkKSVUzuBpT0mDyhEiUQCjrIglbDBTzkSD-Sj24u6a_eiMEzjJ7Fki0bs0uAuCkDoymtz1nepBg0nnKeYGVA53xqEBqwf5g7peQc26p0Um1MyRMCJFvlygDnzgnRYAxAX3cYiNCRZI9ta2qaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اویارزابال در 10 بازی اخیر اسپانیا 11 گل به ثمر رسانده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/Futball180TV/97682" target="_blank">📅 23:23 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97681">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">پایان نیمه اول؛ اسپانیا 1 اتریش 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/Futball180TV/97681" target="_blank">📅 23:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97680">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f0033c4efc.mp4?token=j38GQm3WyinpyBoReXRniUH8aREHb3uaKvuIc0XNtiexz74ECqPl27ay60cT-jpGgia1o3iQan1HliPKkvsXgFmnUtCnucU_Owf8-CnZ5V32l4WWF2y8buge-DYJBoW_J6ryQe8Z_OCo2gN6O0JCllgogwYttOc-IeYYTjQOCtg0iHBaglUZ9ubcvKlbzKHrxL0a-7RLQdzCQTCmxjh53Qk924xCFKuRK_Uz9H8wIXoYez89Szgkf13hWxojmICUk0X7q93JSkml0Y8HG4Q2bE65BRV7PiSbcGeCE1kitwyUqYblegamEQJlacZP_Gdzmc9GTccWXKnh-Nf1qGUezTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f0033c4efc.mp4?token=j38GQm3WyinpyBoReXRniUH8aREHb3uaKvuIc0XNtiexz74ECqPl27ay60cT-jpGgia1o3iQan1HliPKkvsXgFmnUtCnucU_Owf8-CnZ5V32l4WWF2y8buge-DYJBoW_J6ryQe8Z_OCo2gN6O0JCllgogwYttOc-IeYYTjQOCtg0iHBaglUZ9ubcvKlbzKHrxL0a-7RLQdzCQTCmxjh53Qk924xCFKuRK_Uz9H8wIXoYez89Szgkf13hWxojmICUk0X7q93JSkml0Y8HG4Q2bE65BRV7PiSbcGeCE1kitwyUqYblegamEQJlacZP_Gdzmc9GTccWXKnh-Nf1qGUezTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل اول اسپانیا به اتریش توسط اویارزابال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/Futball180TV/97680" target="_blank">📅 23:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97679">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">پاس گل کوکوریا</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/Futball180TV/97679" target="_blank">📅 23:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97678">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">اویارزابالللللل</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/Futball180TV/97678" target="_blank">📅 23:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97677">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">گلللللللللللل اول اسپانیا زد</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/Futball180TV/97677" target="_blank">📅 23:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97676">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">گلللللللللللل اول اسپانیا کوکوریا</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/Futball180TV/97676" target="_blank">📅 22:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97675">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">گلللللللللللل اول اسپانیا کوکوریا</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/Futball180TV/97675" target="_blank">📅 22:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97674">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kqCC4K4PEYC-YzXp2eRsxQ18GeESNEeqhTlPYVGxliGN1B8Z0zDd4Zv8OacQCp5QXPnD72Iaw-9wIJlVdx9lbBMbvn50vxBQE2lrGDvBGBW8UKCo5FFjix5zECMkVycsx0_Mqq_XG0LnkfvJdJ5EXAnq-8sjfEzf6uFKH05QjNfz8gRHhU3FifVZ1twKHTDPxJrZcSgHbgZq_nrtamGMlZtU1LQOOc5wwnqh3hV4Q_aiVYcYjrQgpmOIFXnu4F4SDD4iieAw7ZBgsboIK4ikNdyLMaVeNIHr2K_XpECf9GlgbGwLmEyI21XNcm3CQMoe0jGE-mFgCfS-X_FXL8Wstg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قابو ببین
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/Futball180TV/97674" target="_blank">📅 22:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97673">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">شروع بازی اتریش و اسپانیا</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/Futball180TV/97673" target="_blank">📅 22:30 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97671">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tyqIXDe6WHXKTyixLym-oGrG-7ewmI8oFSVedrRxFYuIie0TEewjVLBWKICtiHHCYVbDzM9xjFegXblqGEjpftJBpoBblJ6A-tMkMClZF5N8iZNCvuZiwIC-jG2vMTOU0AyT6B-gwNgFpdfvZxxVimtLMpu9Y6KUXla0JunSbS9uHechc2Dg1a2cETQBOnxWm2t-ylJzgM3P4qjH641JNTzchmfufRYIFF0sETUEBvWa_UKDkRhpr_vE6_Q6JBEew44CNrG_H_0JDGjAJ_U5UM3nnilR1KixYg0NzdKem4SnaIwoa9zn0mfr7z7BPIMmYSwzMKb8RurU7HaGINrQng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aomp9aOkvMKcn0IInxroDzdU5-aYYa0nJ5n06hgxYfyNQBiKPBK2cLKaLhn7OligIwqR8eSnyypnzQQbncxzxHPh65Ao5Pw-mBkRRvtyPNsnZ6hTNos1S3Qrl9H59AsHYIUV3tXxP8d_XR5fSXjDNikUZLy8WeS5kSqZQZVehkcFlPzkLUXbln2Wymhdyd8ZlalMeqmwtuhptjBzXdmLofW2jn0LCJaE5aaV1KToi1XzuTnNPKiBu0OOFcux19rq9DYfvwnUCIRn43KdJ0M6vtXwQ_DAXsgv17_Q_0G30BFKHZI0sUmSkmNstJVgB3VeaH7j9D9M3xIXnJcRYBtKYQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یامال با گردنبند بتمن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/97671" target="_blank">📅 22:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97670">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
🚨
🚨
😆
تراکتور باعث شد مردم از استقلال و پرسپولیس بِکَنند؛
‼️
زنوزی: در رسانه سخت است قبول کنند تراکتور پرهوادار است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/97670" target="_blank">📅 21:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97669">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🔴
زنوزی: طرفداران تراکتور از گالاتاسرای و فنرباغچه بیشتر هستند
😆
😆
😆
در ترکیه ابتدا طرفدار تراکتور هستند سپس تیم شهرشان. خیابان‌های تبریز شلوغ‌تر از خیابان‌های استانبول بود. امکان نداره طرفدار گالاتاسرای، فنرباغچه و بشیکتاش بیشتر از تراکتور باشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/97669" target="_blank">📅 21:49 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97668">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/InbN56RKUknnSa9MgsCfQYAfKvBhTERwvTEqVRTB2QKWe3adm93q-bPgMvWZjBGYGzBYiQ1HSJAsA_PHehPQWj0mbFakzPIAT5lBPIlKA8k5eo7Hwl5wiyc85Ez3AwxEMeutGIXlI0_mPA5Oev8f8iZsuObrPw9Mp13g_gMZoTnJrO74XA4axMs7MXNHPuNyfueOMuYyPWaqjWIqNMXCEq-ZBAU7xYIVrB7NqXqFBE1hTyWYHPCFgJu5jV-T3l-4svOgkSnu_GD-HwQx0rLH6ndw58fLEOlJ3I4uSRZrQqynq6WxUcvz5C1KOwpk7jDiXQK-mETeuNFwAqWyQH7p0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فابریزیو رومانو |
❤️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آلوارو رودریگز از باشگاه الچه به بورنموث پیوست. رئال‌مادرید ۱۲.۵ میلیون یورو از این انتقال را تصاحب خواهد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/97668" target="_blank">📅 21:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97667">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mxc-l-9rTb9jsmAGxBEaPOEYNfaDq6aLIPzA2hLQzl5gjcvTsSZYx1Fu3f6L9OvWQYziIa4FalqyXd6Q41AFRE6VKPSDS3_z9Bo63LRZm7JeKvcbb6SMcZVj8GP5ZiqZYzsdsklslH10dVGq_wLYXZyyXIrCfmxtGuIMkBgqO9wrtWhiGotbbKAMI55t8n6NZnrVRZBS4BqQhjnY6cKZ2GGG5kZYt_egqro_9O0JL41CmEqv_hxZBpHjEVU2iPI7Rvn4EmGAz_Gj99ju0IR_8Frftb-MvnzRlk_7Vfr3h58okI3Eg0GGLJazwgeMEAh3yFE-gBdbZBkLhBY_bniGVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق اعلام خبرگزاری ها ایجنت اوسیمن در مادریده و در حال مذاکره با اتلتیکو مادرید است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/97667" target="_blank">📅 21:36 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97666">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SFq32o165lC1SRi2rGmgXfq70u6jpPJyCbJxjKHCP99OqreQarfT1zBQs0piB-hJTbqxe8G7NUX78i8Z0EL8d3A1ZJSryQpEVuDjkeTm-YSsxyPEHLMWNbpdyvjL6feAMS16l664i8bHDDaI2ldQUxOHKo21dYNIxdj3mTH4k0PXEYrLZxz0H-zZ54cliUVvQA6FoUrVIEmjmpnWozzokYZ91iFF2EtthD3boGQgjeT-hDLaSAgIzipgtYNIn7nJ0H_r-NwpNmk-8p6dGKWkN9ySGxEEdr-GsSRMCrfsHmmsPs6Y-OTDaLbtESqJeDSiMeLurVw8BykDh2jqippixA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇹
شماتیک ترکیب اتریش مقابل اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/97666" target="_blank">📅 21:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97665">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iqtiDSTytkPTNC9e-9qFJEl0FVrQnQNohgZF7YqOHEtSuPnDbhvRIChC8nCNxuQbWtWNmbspDHHZljd0VUIIEqmVoD2jVbhnDWPojp_5v3zIIQwRBlXIs1oF1FNquwKBvLY5pEKygH48TSs7st8dCc4JnAm3MRZAq1p9SyMh1sLtjY9MZ2jxnOnGVGKeOiKZy3JXp9bi0P7JcbBOW06w-wHxcgD0E_lRbo3qlVtsmZziIyv1Z3nIHtaLbv9nlu6W0iaYFR_xAQyub0-lc8Ofblu3Hvi8L424buMJJX8rVIMiMXY3QdepiTgGhp02SU04sCdHmsO6f75cJ6VBamNtUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیگه لازم نیست بین انتخاب‌های تصادفی یا تحلیل‌های زیاد سردرگم بشی…
🎖️
همه‌چیز برات به‌صورت پکیج‌های آماده با ریسک و سود متفاوت آماده شده.
🔝
فقط
پکیج مخصوص خودت
رو انتخاب کن و وارد همون بخش شو.
🏆
ویژه مسابقات جام جهانی فوتبال ۲۰۲۶ | ۱۱ تیر
⸻
🟢
CORE
📊
انتخاب‌های کم‌ریسک و مطمئن
🔗
ورود به پکیج:
https://betegram.com/share/betslip/NPKLR49657
⸻
🟡
PRO
📊
پیش‌بینی‌های متعادل با سود بهتر
🔗
ورود به پکیج:
https://betegram.com/share/betslip/TCUMQ94076
⸻
🔴
ELITE
📊
پیش‌بینی‌های ویژه با بیشترین پتانسیل سود
🔗
ورود به پکیج:
https://betegram.com/share/betslip/AUZNP38876</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/97665" target="_blank">📅 21:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97663">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b19RaGmaGnkk2CY3eq2ENUJOOkDtPFUZEY0xbIyErgiDc-3nGD9MME3ydRG_-CPKUbQ4EkMkmQP_07fI5xlM9KJ-3qL96178hI5wML7BvEHgUlRlP1N2l9BihagV_r2dBKYYgh-JlVhMiscxXVaYfGTRNoFJwWVLYRK8NmJvU7z9WaWFbjVXcu0KwBNMkxLBYcwHWreHnjuirpge7ZOPaG4EjlcwVo5PAw9l_ffjtJh9EWJm7a6v42JiWJO3yNwnmt5thHNLNncpdk_LOaIaTSftLHvJaQ_TGUP-5CSrMBUVTbFHRSVrOgMfv4LCJokqzB4nTAqt2dO0XSLssi3SVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری
⚽️
اتحادیه فوتبال اروپا اعلام کرد که هر بازیکنی که در حین صحبت در داخل زمین، دهان خود را بپوشاند، در لیگ قهرمانان اروپا فصل آینده، اخراج یا جریمه نخواهد شد.
❌
🔴
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/97663" target="_blank">📅 21:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97662">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/usLX2o6UIqu0oR6vAcCquw3bgxTo30UGkipf5563yQcCdaArnLmzKE7qjXENRP1YO54jUBONTAQoykTpAYnL9vCmhbEe9fzVq3uyef7GF6PXhV92iS--gFfPjVxEND4QnPx_OEHHhNu-74dddsArgWRMBF7zMQ40UY0KgZdNqGlhvw_XkRhi8tHwEqWWseC2VJZPIGXvXLVp7KBieHLBWYIABnSCdQ2XbtOdxBnzbK33YzRRg-jJvqTb_2hMqFkNxY0grkh0hSOnCWlqnBzD4_N9L2SNwFksArxLD4RBh6NSbdB6C6SUiCim5AX9DuFWE-A1WkbMYydHnAvqfQ5E-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇷
رافینیا امروز بخشی از تمریناتش را روی چمن انجام داد و روند ریکاوری‌اش را ادامه داد. او همچنان شانس حضور در فهرست برزیل برای دیدار یکشنبه مقابل نروژ را دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/97662" target="_blank">📅 21:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97661">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fdeH2liNcA-CPwX5UlJMGbLYozbOoPFpgyJhoCXFqNUFSs9274dfQm8fmk1dFrf_AJHthU8dYFqRIbEPxWJ4LNvF3l4AYhdVJGC8F0RB0knCGbqVt-rB1bn0nNhOs1fBeYknX0Md-3Vvoe57SpoSCBxVP13z5sG6WxxYiOS3PhtvIpA0dE1zEYM_Jyh5dLC_lGaoj0EXjL2SIYmD6o0BRlwrueGSbSUEbAE9v1ljF4Q0eDWQKisxM-sHLrfae3oqUOusLpMfA4qdab1hgc7WTDnFNo7cVGTIHFG4TieoQ_jUznRldH6laWiMM3LPsxBC6Y6CGB4in1EjwduBpBcHQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترکیب اسپانیا مقابل اتریش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/97661" target="_blank">📅 20:39 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97660">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fcacf03f8a.mp4?token=jDef8R_ZzqSQksyJLfeY5QMGUZVG36QGX7Jw4OKW6By8w_l8sFB8XrUuLZS0JPnnTv8njh1JC2u0ZN51RR73RJyBNkaHPnWN3gsbYv7Wwg29auZhLVa8fBhocH1hEiBZPSXwn9TUTpNPwCslx0dSsJt19PeBeB0u8N0-0KuuTAVKLrSvhdh4KOYCZi1N2qoOcVkZpLwLY4XJ8gSMMCSDnBGpfm3Ea905p3ZyyyLQ0WYWY1svbC5inx1Ztu4tEXg43Z5NQW0Cy6zDdtIeFbLYCg-ovgDwSnGgb0u8tNOVCaAb1MIeBnSPO-d5_7hLPROnRVK4bHeXS-mWFHCiAyMHzYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fcacf03f8a.mp4?token=jDef8R_ZzqSQksyJLfeY5QMGUZVG36QGX7Jw4OKW6By8w_l8sFB8XrUuLZS0JPnnTv8njh1JC2u0ZN51RR73RJyBNkaHPnWN3gsbYv7Wwg29auZhLVa8fBhocH1hEiBZPSXwn9TUTpNPwCslx0dSsJt19PeBeB0u8N0-0KuuTAVKLrSvhdh4KOYCZi1N2qoOcVkZpLwLY4XJ8gSMMCSDnBGpfm3Ea905p3ZyyyLQ0WYWY1svbC5inx1Ztu4tEXg43Z5NQW0Cy6zDdtIeFbLYCg-ovgDwSnGgb0u8tNOVCaAb1MIeBnSPO-d5_7hLPROnRVK4bHeXS-mWFHCiAyMHzYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🏆
جیمی‌جامپ دیشب جام‌جهانی فیلم دوربین نصب شده روی بدنش رو هنگام ورود به زمین منتشر کرده که خیلی باحاله ببینید
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/97660" target="_blank">📅 20:30 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97659">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a57b10cb97.mp4?token=ATfOgovPvivIfg7i2uSwo-En7tcLgNbbKCsNbZA1WhgmD-JFtxU1sTMd7JpwVVnCkLxi2ghJCBiv0Fg1xSUK3qDs-H-yUgb-xFQ-5QwQ-4oWDnExB2uWHk7HFKL1OZ-onVMAotFuKtLB8d6XNqKwzb99cfUsWKGUCvOhXw7JFXorLT8E2-gClRlR4C1aanLi5XSxauktrHSXryL6WXglQchjZutQ8ThzEucyZ-sKk-XwUPw4CbEBY5v_6eDCVp78OoMi-m8hDy5HXnFdJAHPZAEhOBFv-E_VlsyBcbg_H4iqaqivAvyMiRaRvv8iPeUAL7skItJQKIUgdQL4aAszSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a57b10cb97.mp4?token=ATfOgovPvivIfg7i2uSwo-En7tcLgNbbKCsNbZA1WhgmD-JFtxU1sTMd7JpwVVnCkLxi2ghJCBiv0Fg1xSUK3qDs-H-yUgb-xFQ-5QwQ-4oWDnExB2uWHk7HFKL1OZ-onVMAotFuKtLB8d6XNqKwzb99cfUsWKGUCvOhXw7JFXorLT8E2-gClRlR4C1aanLi5XSxauktrHSXryL6WXglQchjZutQ8ThzEucyZ-sKk-XwUPw4CbEBY5v_6eDCVp78OoMi-m8hDy5HXnFdJAHPZAEhOBFv-E_VlsyBcbg_H4iqaqivAvyMiRaRvv8iPeUAL7skItJQKIUgdQL4aAszSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🏆
ذوق‌زدگی مردم کانادا از دیدن کریستیانو رونالدو اطراف هتل محل اقامت پرتغال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/97659" target="_blank">📅 20:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97658">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TCPxK-8P0vssjx7pTv960FBKwg11sqv_l2f8OE1pUSAWgXWEZSzH9Cor53_x4AS-f4VbXW3tOxmduzzmFiIEyegSdObk_NU1WeWpRzDXYx7IP-wCThEkIUK5wHrS0cyoycSWKddw6RLo9gNEpek-HhFC44tA_SeN8ACMzR4PGRtea2QFbQTBQR_hA1gketG0ZvwnlN777e8xh_SiwsahzKl8Clo83lKUmuP8wsPyqGPNjKXuo-BuJ9ovhWv2R8QTGcceMuLNdaslo-3TKPKtHuWWXGhBOVccnwz64cejVTcEaYKxhDMW8qFEYX0rF2kyrP6If50O2lfBv0afs58lfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فووووووری
— نیکولا شیرا:
🇪🇸
رئال‌مادرید به توافق نهایی با انزو فرناندز برای انعقاد قرارداد تا سال 2032 دست یافت و مذاکرات با چلسی برای تکمیل معامله آغاز شده
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/97658" target="_blank">📅 20:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97657">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tYdtOeNFeeGo-5KMDVvA0T-8na749d4f9Opkp3J_B5a2aRePXFad9FjJ9VpuOt4pRr1hD-RmKh0b5alefwbnVa1E3Qp_msXA3yCtPZ4jusjisSkn3o3Og7e8NLCTf-Wbik6_Qp_75ki2tvBsKURmZn-LC6_FDVEXZKZzV6C7P_fsPQhrlihUzfFL7YSleKgn_1-qNkMeHlL7e4CV1P0qqYN3lnGrLuoJs7KxaNn3LFx7cjtCBvy1aXjlQlYgE80INEzQx_iptktfTf1u1jDUDnHg7_OoP0x8eUIkvAl8egH0Z3dyIakO8SvYergMF4c6G2jKKUwySIGQg4OjrhDOcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇦🇹
🎙️
رالف رانکینک سرمربی اتریش:
"لامین‌یامال امشب هیچ کاری انجام نخواهد داد، ما تمام فضاها را در مقابل او مسدود خواهیم کرد و خبری از گلزنی این بازیکن نیست."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/97657" target="_blank">📅 19:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97656">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TnsdS0y41F9BlpVZZJel4OgacvxiNKsfoxh40W5CUaiCMcMkKmEF-Fuvj-vWM69-l4-HquUAd-H9SzILb1YRwOKeR5Cz9lGwv17ihhGI-HwFL9Eb46vptkoW7rowfPkQjMxw2FoJHyv-vDNoGe_hViKJhtwm07lOGOdf68YU83DMjFu7048MKJKd7-R0oZPsjDafKfgFtdgzYFwDQuX3V0-cKmFKfEomndn3V9UkZDYqMu61klJaD3M2cj27SSZgmtcDbGxgyAOPTUyS36gEJ-3KyOWUA5vB9LjRcrVRPPDb4zsQcmc4M7GRuMKmNxMHyAQTbqUonJYJyzG_kuHr4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💸
🔴
#فوری
دی‌ماریزیو
:
باشگاه میلان، ارزش رافائل لیائو برای فروش را بین 60 تا 70 میلیون یورو تخمین زده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/97656" target="_blank">📅 19:53 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97655">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M0b8DArmR3pJN8gdwz6jGdyaMYMMwpPUTKnr2fj-w6dsoHdJDY3Jl1gYx9_xXwkbtUgCfmOdrw3zjeUH4RQt1mkilbJHhu35Z9gYHTqB6VcbDAHNE0mOlF_CaykkWTZDbiMV2-l-PBb8Qi1xYmWafKZ7J-7cn4JnELY_Cogr1FEo4fnsXk_r5DDco3GKd3glNivvGQPS0lUezwTbo_8-cCWwEqXhGAo490WUZ09vM-qEQ9dVumzDqpf5jOnhisO0S-IwTxyljcE0UW2WEzl9i5iL98D3nNOY-h18zrec7VqqIcy6bb5mL24B7-gy8dUUlpOVxmCOeBwDHwVrBraG0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🤯
📊
یامال بهترین رکورد گلزنی و پاس گل در مرحله حذفی مسابقات بزرگ تاریخ تیم ملی اسپانیا را دارد:
🔴
— یک پاس گل در مقابل گرجستان
🔴
— یک پاس گل در مقابل آلمان
⚽️
— یک گل در مقابل فرانسه
🔴
— یک پاس گل در مقابل انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/97655" target="_blank">📅 19:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97654">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/97654" target="_blank">📅 19:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97653">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pzbX6kCcanh9ocPeP8W45t2rwI0qv63gQRm50DLpJ9rJ2gKLoMFTEtShVyAb-7f8AN1a0zsmbBBDJGZYlOEEBBQ29W-RXEW1vQclMm6xTjOWlukbbQr9g15ADmR1TgNbnPhE7F55AEiJN3zRtmCdCZ067dJjZeNYvqHBfvlkLmG9S4XIuoduZNho-QJJ5rbzO0G1A2zTa0ZW8mkvmvUzj4aqaURE3oD7QN_9-YjHzvfj5WYT0k_WyVxamCcSpl9BM1ME8XIgefvutCoKu3DdbLlvSs7VlrDQp031WcWNEf7iMKpRfQghxVDTSqFr6tvriC02UkXehHv4Q-0Y7BoxhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/97653" target="_blank">📅 19:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97652">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🔵
موندودپورتیو: بارسا به قانون 1:1 برگشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/97652" target="_blank">📅 19:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97651">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4659792849.mp4?token=bZDHp8wQt3UDTOrTM_pMyEcemeFa3b-r_zv8_Lplsh2WSDSkbka5Io4TA26BfJUZeDI1ux_Rqt5a2DEMPLzesLm4SJojwWzf4Da9I3beYp8XyfL0rX0YN2LqX8UsKUiwB4jz8wrB9E-oCbCEXFMFI2Rx1JlY5FDJSZdfomw2v2dUi7OS49JoJHD7SGuwpF3domzg7tTi8JTyfXEIyr9QbsE4oUEug0Rky6FQeQSBkoyq0sGNOAvMO_9-O020mBGCD3DAldPeqhVryD4MB3ICfSWx4hyOFz3ywDms4U-ZqwPMw-RQpxVozgq_XvVktnKLuGvwzdhS9gPiZ-Ncn8on8oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4659792849.mp4?token=bZDHp8wQt3UDTOrTM_pMyEcemeFa3b-r_zv8_Lplsh2WSDSkbka5Io4TA26BfJUZeDI1ux_Rqt5a2DEMPLzesLm4SJojwWzf4Da9I3beYp8XyfL0rX0YN2LqX8UsKUiwB4jz8wrB9E-oCbCEXFMFI2Rx1JlY5FDJSZdfomw2v2dUi7OS49JoJHD7SGuwpF3domzg7tTi8JTyfXEIyr9QbsE4oUEug0Rky6FQeQSBkoyq0sGNOAvMO_9-O020mBGCD3DAldPeqhVryD4MB3ICfSWx4hyOFz3ywDms4U-ZqwPMw-RQpxVozgq_XvVktnKLuGvwzdhS9gPiZ-Ncn8on8oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
متن خبر: خداداد عزیزی دقایقی‌پیش مدعی منتفی شدن حضور اسکوچیچ در پرسپولیس شد
✔️
❗️
🤩
واقعیت در پرسپولیس: جنگ قدرت شدیدا در باشگاه شدت گرفته و چند نفر اصلی بدنبال فرو کردن گزینه‌های خودشون به نیمکت سرخپوشان هستند. صحبت‌های خداداد عزیزی هم با دستور زنوزی رخ داده تا جو اطراف پرسپولیس متشنج بشه و به نوعی زنوزی از اسکوچیچ بابت نحوه جدایی‌ش قبل بازی حساس آسیایی فصل قبل، انتقام بگیره. اسکوچیچ همچنان نزدیک‌ترین به نیمکت پرسپولیس هست مگر اینکه زور برخی نفرات از پیمان حدادی بیشتر باشه...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/97651" target="_blank">📅 19:29 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97650">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gmz4V4dQmCsLtgBG8d8ZxW5esvwQs5inF7jdDTvpz7Kj5HytHGknpmh2iqlMIs5Q6DoZYZYZRmOAhNrLBaVOiS4gy0ogJWv-PNx80dAV9WsVClCUR0Fv19khXQNIvC8bZPlIV6uFLfoLMVAuDgD8JO5cUim1J24ByO712OPcUemBH3WFv1umvQ1WfAixlA7TamJXoWn7SRvblrnr8Z2N4h8YJE2CvzpAbGU3T5YXBqkn7990MGFit9RbCVlHRLkB8fhJX-PfNKQBHP92OUFrdsPluSwINxIN-ZEL6ZKkX0jYVQ3snjOJ5seBVXPAFA3xTacvEmuN3U063PQOkpKflw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
⁉️
کدام حریف، سخت‌ترین حریفی بود که با او روبرو شده‌اید؟
🚨
🎙️
لامین یامال
🇪🇸
:
"نونو مندز، او خیلی خوب است، واقعاً عالی است، من از بازی کردن در برابرش لذت می‌برم."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/97650" target="_blank">📅 19:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97649">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🔵
موندودپورتیو:
بارسا به قانون 1:1 برگشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/97649" target="_blank">📅 19:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97648">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YUygjnNANjNssIPJ4XcmmIM_fWGjWwthBE-vIQuPnLUC7QQ9p08A8HGrK6xX-jv5JzhQgEctlvryfk1yCR2idZYqG-4YGVSwg1G0jBkMAVX4tYd172PAZly9RSCGqBhA2nft-78EzLSreP7bUWbpok1SfJPoj23J0UZMoFeVAw0RYkYRTl19Jrtiv_cC-p1aRjdXisluhXHD9C75ecRHcoug_DurM2yfm-8kPEuF_E3CU0oUqdVF5BzitzZwm2cHHaRRO5byHqVYC8TkcZI1XYyOOX0Iq7XP4rboiyXnLISxh3eRmyhQhcQhBDkhyA-BUoyO4H2Z8_UXtbg5uXNB8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
🇧🇷
فوری از رامون آلوارز:
احتمال خروج وینیسیوس در این تابستان از رئال مادرید وجود داره! باشگاه رئال مادرید از قبل با نمایندگان وینیسیوس در مورد احتمال جدایی او صحبت کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/97648" target="_blank">📅 19:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97647">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CUviXAexIHm4n3z2U8CWj3s3jKLwooufYtZkVo86vldGXjxyoUWX0rbGZzLueDJPc4D07Kr6Y7SnzFLhOYNrl54t2C8bFT9_3E-DpssN1iiVU7LIRvu1z4BGfzdGzaxN8R7es4b7f6OhqZuqB6avmwnnnYwVGJUSRqu4Sl3BoNK3v_EqB9dCx9FgJQq7qQ6ylLef6jOM22dHi7TJzneGY4mv1tXypNfDdZS6Vrwuqkthk9mgUXeUsb-YNn_RnHTl6SU-35Rf46esBEik5HD-8Pm6NAYrZBixKdTPjVvRl-ipKX6ppPA2dxG1RnvDzSqsNWjF3UfJB79osMKCH1q-fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
فوری از فلوریان پلتنبرگ:
فدراسیون فوتبال آلمان به ناگلزمن توصیه کرده امروز خودش استعفا بده؛ وگرنه خودشون مجبور میشن اخراجش کنن.
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/97647" target="_blank">📅 18:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97646">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/irUqvSOudRgPfcv18IbzzJ3gT4wtmNB74-fzC3bgTSyAVIBSptmnjBsBP9hFL1RU1aXGFHTiUGCB17jJlosNhbiC52fW7eI7L3oTLEeFwRLQCtvuqo3fHKDeujk0AFFfsNMHzPi_EOslL4p24IxwOheG5b3J2B_Oyj0A4KSoOuM5wtKgusmUHYzTI5u6umwY9pMb7MceHeuFFYXghpUaA0UoJ1NqTtV3BEJVjftx7tdL3_WJwhDF-H-AttIuSCu4cZdSepnyDCAuyqdm85BJgbKZuD8DMe41eesTEtwOWl5BoojLYsrdihCl5gIYPG3RGT5RfP5phbidE0tMwll48A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🚨
اسکای آلمان:
یولیان ناگلزمن در طول جام جهانی هیچ گفت‌وگوی خصوصی و رو‌در‌رویی با بازیکنان آلمان نداشته و ترجیح می‌داده پیام‌هایش را از طریق ویس در واتساپ برای آن‌ها ارسال کند.
📱
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/97646" target="_blank">📅 18:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97645">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f55154a43.mp4?token=dGf0hS0SzslDND8waSRDpVwUDBi8xsC0Rx7pk8Hg4DAPPyFriM1T-eL8_xDCBnxin4CW69g_thjFlf7MUseS7v-GDuBMFSf1IsE6FxZMmvcTMN6pqIRjAssM9lPIKkoRFOgIC-IduMtGkcU_8iSiaHcauKVF0BIV8ua49I1vq-hGPZ3OtJsXI9znTUpNZYf6kW3eIbmjJaH2FKMqEwLgCt8pztkFiac3sCSqSyRDGv1uufq0-npedR1fOXDVQlE8_nBqC3Zm5hHsr5oe_fKLntaHm1p4L-jQkrzn60fijVIhQBgaVDRi_TVPmRwmdjsF_7UqyCe-zpl1jK1t7lPUew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f55154a43.mp4?token=dGf0hS0SzslDND8waSRDpVwUDBi8xsC0Rx7pk8Hg4DAPPyFriM1T-eL8_xDCBnxin4CW69g_thjFlf7MUseS7v-GDuBMFSf1IsE6FxZMmvcTMN6pqIRjAssM9lPIKkoRFOgIC-IduMtGkcU_8iSiaHcauKVF0BIV8ua49I1vq-hGPZ3OtJsXI9znTUpNZYf6kW3eIbmjJaH2FKMqEwLgCt8pztkFiac3sCSqSyRDGv1uufq0-npedR1fOXDVQlE8_nBqC3Zm5hHsr5oe_fKLntaHm1p4L-jQkrzn60fijVIhQBgaVDRi_TVPmRwmdjsF_7UqyCe-zpl1jK1t7lPUew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇾
عاشق پاراگوئه و کوهستان هاش هستم.
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/97645" target="_blank">📅 18:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97644">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XUDpE5Z0gqi9CiItg_g0CtGt4JnyQ1pte6HLsChSX_UbgTpA-_eRQ3mG_kjPDTpUwGAuAqspySyBaHmtj9JdwveJd10ksa3C9wF-2oNi8R8T4vjtNoeLXdI-pajAL7plDqla84it9KR8LQBsilJXM5U9WvCiFbL31sV5fKNYWHGOrUfb-lzhERKk7P55t3hd9idEf8PIjxF78hmT6m5b9P36p84Y0mMNm6-q7GnigT2N_7UoGstElR2vn_pOFiMXzoU_du3kgHR1lNfbebo4P1u7kiQLIxHTqH8qFS8zynW4KzTT3-EcXTx_F3EjiaQQabhXehQqQwsDN-W64GCvpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
بازی فردای پرتغال مقابل کرواسی، دقیقا با سالروز درگذشت دیوگو ژوتا مصادف شده.
🤍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/97644" target="_blank">📅 18:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97643">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bQaDtMrdCKZXwHsHbgYDBDBMg-Y62G7x4ngOMAtoOqorfa-gvcWWpf1KM4W-pLU5x7wyfm9dogTjdUTTC3dlK6DPDWPUBTjVc1lbgnOxT4KhS59gByQaipO5WrIBND-zvm05Ub_8ttI0-01O5T-ZCkXBkrKyz-mRxyvVt6x7ll9ofttS31xbtYulGBZR9sMGc1Bdt5esjbCYxE-ABAK1LCSH_TNmpH_PsQ96gHYApdN9Tuo3NnTVuNETN6KvXxACLjGG-GeZfLiDgynTmUCtg8Ynf8S4GYSZl5gXe7VzTdfawVWspvI4aiIiAlYlW1m5Gn7PyHPQn4fWns9uw2pnXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇩
سرمربی تیم ملی کنگو سباستین دیسابر قبل از شروع بازی مقابل انگلستان خبر فوت پدرش را دریافت کرد و با این حال تصمیم گرفت تیم را هدایت کند.
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/97643" target="_blank">📅 18:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97642">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحاشیه نیوز</strong></div>
<div class="tg-poll">
<h4>📊 با توجه به مذاکرات دولت پزشکیان، قالیباف و عراقچی با کسانی که آنها را قاتلان رهبر و متجاوزان به میهن می‌دانید، آیا به نظر شما این آقایان حق شرکت در مراسم تشییع پیکر مطهر رهبر شهید را دارند؟</h4>
<ul>
<li>✓ بله، باید شرکت کنند</li>
<li>✓ خیر، نباید شرکت کنند</li>
<li>✓ نظری ندارم</li>
</ul>
</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/97642" target="_blank">📅 18:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97641">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a4c734a62.mp4?token=aTik8msWZThrqUerGUpTRqfpLhol2-9UguiMHh9MSxepjrxQuXIWyl1vyQkifgXGDHUgAaHeEZkrds1sy6-HgiMFVEDCApXY8PPllnJSOVazBisQiqkkcf5i2VPVaCdG5MKGylrahnfJDPgd_iSg_KFr3GhqVqwRpxAvVhkCrk3x3_qO10qKnI-sgIH71ulJEKguClFlgWQni9e3R056LkuxsYsbg0ocnEznomvY1QGZbR4jcdwb8Htn3NM4KbYA-PrCFcvppvrm1puMOT59zhab9DjjY7SxWEdHv5G6cX5R9SdCX9J7j-tcK_z370UFRSfOo0z2hKB8GyCKRZeSlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a4c734a62.mp4?token=aTik8msWZThrqUerGUpTRqfpLhol2-9UguiMHh9MSxepjrxQuXIWyl1vyQkifgXGDHUgAaHeEZkrds1sy6-HgiMFVEDCApXY8PPllnJSOVazBisQiqkkcf5i2VPVaCdG5MKGylrahnfJDPgd_iSg_KFr3GhqVqwRpxAvVhkCrk3x3_qO10qKnI-sgIH71ulJEKguClFlgWQni9e3R056LkuxsYsbg0ocnEznomvY1QGZbR4jcdwb8Htn3NM4KbYA-PrCFcvppvrm1puMOT59zhab9DjjY7SxWEdHv5G6cX5R9SdCX9J7j-tcK_z370UFRSfOo0z2hKB8GyCKRZeSlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇲🇽
پلیس مکزیک: در جریان شادی مردم این کشور پس از صعود به ⅛نهایی، حدود ۱۰ نفر بدلیل ازدحام جمعیت کشته شدند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/97641" target="_blank">📅 17:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97640">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2308c1db6.mp4?token=YT1GAEnsu-SJwiyUvgoD_jUL7cc7HBIWtZD2Mkf57DOsnB1z5qnA1U-5pqWs8hACF2uRlBALolm_a7tyc9pD9Naykr2uHm4Y-K5EhESk9n9GzkHU30WTxOktjHcF-uAMrCRItKieOfB7dNn_V931oI3I59J9vTuJsY2Tp9urBhTpYfxWbq_sE9fS3rByX2Cnu181WnLYDu3EGKV2D6ZN8xSSGfIOGpdKpFFSRhrj9pZ5r8HvhLi77Q6i75v4N2iLLCXHcEsy_F_BDNQhX35wVAbPzt9m2ZztCRUew6AcLMta8uCT6lgOL84X58hszg60lCREDHvPVNwhTlE6KmOAAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2308c1db6.mp4?token=YT1GAEnsu-SJwiyUvgoD_jUL7cc7HBIWtZD2Mkf57DOsnB1z5qnA1U-5pqWs8hACF2uRlBALolm_a7tyc9pD9Naykr2uHm4Y-K5EhESk9n9GzkHU30WTxOktjHcF-uAMrCRItKieOfB7dNn_V931oI3I59J9vTuJsY2Tp9urBhTpYfxWbq_sE9fS3rByX2Cnu181WnLYDu3EGKV2D6ZN8xSSGfIOGpdKpFFSRhrj9pZ5r8HvhLi77Q6i75v4N2iLLCXHcEsy_F_BDNQhX35wVAbPzt9m2ZztCRUew6AcLMta8uCT6lgOL84X58hszg60lCREDHvPVNwhTlE6KmOAAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طوری که باز کیپ‌ورد و‌ آرژانتین داره پیش میره:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/97640" target="_blank">📅 17:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97639">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f7799c99f.mp4?token=kViICLD7LUAeKPrtjwK7TxSFLsx5wVuCSgufXHCw20DYqz2CJupSgpdZuzuTbYlEt0VTl4mGON9CFeb8L6FhjfAkoaWKSfYfPs7a22rehcqc5-83GiLUnqbrxCH1doWa1eYNxMK9lBfPDa_pNumJHDcwyR1RrluhK-LvpUXy0-aSigXMxQWqomJPVX4u7R52bG7_fW6vN4dy-mDXyVX7-U1HL_8lnH6B3u2r52tm25sGNwIU98cgQn4Q-v7NtfmDYhGNvML_2RKpHJtM_8wpB_ftlydD50ZJnVBmc6CDHW6oxjPe6QE4W2yEexf09t7eNtU8ih-Jl1vry7TF88cZ0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f7799c99f.mp4?token=kViICLD7LUAeKPrtjwK7TxSFLsx5wVuCSgufXHCw20DYqz2CJupSgpdZuzuTbYlEt0VTl4mGON9CFeb8L6FhjfAkoaWKSfYfPs7a22rehcqc5-83GiLUnqbrxCH1doWa1eYNxMK9lBfPDa_pNumJHDcwyR1RrluhK-LvpUXy0-aSigXMxQWqomJPVX4u7R52bG7_fW6vN4dy-mDXyVX7-U1HL_8lnH6B3u2r52tm25sGNwIU98cgQn4Q-v7NtfmDYhGNvML_2RKpHJtM_8wpB_ftlydD50ZJnVBmc6CDHW6oxjPe6QE4W2yEexf09t7eNtU8ih-Jl1vry7TF88cZ0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🏆
وضعیت آقای‌گل‌های جام‌جهانی ۲۰۲۶:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/97639" target="_blank">📅 17:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97638">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad14f6b1ec.mp4?token=XHrKulCgeKmwkddhvUopn-I_GAFkP82kv22FcUL4PDnzgLm-1QjcwbMfvGE11PbAS9eR9bAQ3CQz-ojDjbWVIdHxg1vGW57_dO-Nlls3w1FRY6K8i6UxFxM49AUTdMOm1h29Rwd0oCNX51WAEHRmqSupBc3lLVm7F0jY0FeC3ZdNNdkQDXTxbimtLuLVp2AOT_-5Xn0OCjH4V-3YFR7lMurJ1xJpQYLiHHQX_hCYr5CV-FixZK3rPYdRmE_lneWyrb81rV0S-OkD8bHI3Z6KAdfxU5D4KuA5uOWk0l_dLTCAqm9mELwpSY93tliiW7UZgmmpv9qZ9H9XfyxHHVo3gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad14f6b1ec.mp4?token=XHrKulCgeKmwkddhvUopn-I_GAFkP82kv22FcUL4PDnzgLm-1QjcwbMfvGE11PbAS9eR9bAQ3CQz-ojDjbWVIdHxg1vGW57_dO-Nlls3w1FRY6K8i6UxFxM49AUTdMOm1h29Rwd0oCNX51WAEHRmqSupBc3lLVm7F0jY0FeC3ZdNNdkQDXTxbimtLuLVp2AOT_-5Xn0OCjH4V-3YFR7lMurJ1xJpQYLiHHQX_hCYr5CV-FixZK3rPYdRmE_lneWyrb81rV0S-OkD8bHI3Z6KAdfxU5D4KuA5uOWk0l_dLTCAqm9mELwpSY93tliiW7UZgmmpv9qZ9H9XfyxHHVo3gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
صحبت‌های ستاره تیم‌ملی فوتسال بانوان درباره رقم قرارداد‌های بازیکنان در لیگ‌برتر فوتسال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/97638" target="_blank">📅 16:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97637">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M16ByK_Zs-UwK2eEf3fQOxw6hvyLDD_9m6hWGUsMR8rJduFCg4_REs7zrfNS9Y5yeUGGW-DqbPd-QOCxfIhwj0RONN4vmTRRxfdQMvWmMpwDqz8rjK30MFAlNjGL5W004Gv4ffKAsFFzsFGujQUkwiwat0esQHu3HM2oIAEsMU_nQGib9GJuvWNdeFIv5IhzL2TLHeSD-5hkm_7KbcYPBl_-LMSngKHLM-NaqKAfz0jdxOuy6EfHG9lFB-lw8FacXIYTZcdUNXlSe2eaxX9MOw7gyufIHKH2EewFgNmrSKYGuoZ53dlIhA7MavJN2FrKf6Ccq8xHrF7aq_jWpfi3TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
منچسترسیتی اعلام کرد الیوت اندرسون را به مبلغ 130 میلیون یورو با قراردادی 5 ساله با امکان تمدید یک سال دیگر به خدمت گرفته است.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/97637" target="_blank">📅 16:39 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97634">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vir8URksoUgP8yUj_XGsDvmIIrPdlsGHPlcj2n-S0m2N4381NK2yzGNUqMjKSSP531bJTT7TOZtSX0R5_bWCpmiPV54qkwhh2IhsaNLbSaMnQUbbIkR36P1-ReStpck_a3eGkLkMe4HuXn0Hr82i1geZW7uAP4KkFVXsI8RgCiWzqudxLQ1X1cPexaNg2S9vNaCR25T0QTtoJFSDQedEnK4zuMGr7bcj_zd14uwD6y6JzNfQXp6Pgn842Sct6HGyKyrY8_nAlEScFR7woSep8_QbfKkJ9ahLQi_OgLS-siKQt7MluGS4H5D9CSxUKOSNlhuqhZPHCzeXBtNjnQKbhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dCD__zBBbgpfc9AHRz2x4_abtsFUSll9a0rYjVNzFJ3nZLB-DLsMm9yR3He-DNPsXLDWxSDO3qLs1a83sldl3sQLSHSwHxOVC9IygWnEGie6nCxSvCIttX43THqgB63m73CqKuryrHfwNy8mjo_vTU2PKvHY9xTKlYRRubdvdigT5Ehtqzsns0rwg90MbD1FuOAngFYynx3HpMvN65eENsWJtjeqy9QVcKOZhVWZZ_oncxs3BEXidtVk1zs_JYnaYAGjC3ULaisNaeC_vmr5QuIU4d3YFsKN6VzicPgQFq-nY1D6EC6xVVJpjzRt6pbKuNx5bCnYxa6oRwKrauP-Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BnbK568B-fymvHhmuRUll9cHaLamvnqnwBWVhwMOq5WvgIL735lyW3G7jF_PPus51XPdZjRakKYLylONzr1N0BZES4FQPiBu2-7c3bGYjPzogYfKB5CYjtaghqrMTjVcasetzEC3IujDysqcq6mc-Jm_BwN6loQP65sag5mQNDE_f6EVl4CwsyOdmOlGc6Q168Eh6zkJZoIWu-QQSSGnzTDgB69lDq3NGrx2hnAP2kWSyZBf-9SexDpFdHC0gjcOYvTRRR8bTg8eUkFIg7mefRwnfIudBe6lbYI0WDehuL5kQvGDi8gV5uc043Y1lfjaepzXtUJgnkNc-1JYdWeHdA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💥
🏆
فیل‌وفنجون سکوهای جام‌جهانی :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/97634" target="_blank">📅 16:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97633">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JuPEp7WngtHZPf0Cya1bnpxSrbRa1bj-nHjT13DlSlFNLA4tBQ2d8HFoVtBrDnQkdbkYH5tNhJgXnVPYHhvtF8ht1RXGVsdcJidwe_TeJS_1YsBfknvawn4eDfNTmK_-5Lcn9Br8ex8QGd7_mxwtpfOlL292AUos5N1zvjyKWradMwrtPKZEbf05bBdIXVn7XJnmKufUMaH7UtnD8jiyKdgNXWkNVs5rx4fc86S304Ca4C1hVUkqTxMcNHXlc-maKkCT68Ehih66wBWmfxCmwPJBtspdTP49cx8TBh8mx_mZ982-xUrYxAr6PyUYM6zhTOAGgUTJtWdRoEyKR86RCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇽
عملکرد مکزیک تو بازی های اخیرش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/97633" target="_blank">📅 16:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97632">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nUs0hFHaLUd1ddpWhMSB5o8huxwqSt04L_02pqdG7OGsW8zB5UawMjjrwUfWseNp5cnqiQ4uFI7cCD1m7d2VzQunAjxuTIY11VPE-Sj-tuuzryWBadBtjb0UsKAJb4hgVEI0gpttnd3rx2WvyfiiE-CCDVfCpb7XDq4YKEdC10Sp-ggqYwk8-e-dx-81dGCZZqZjS9nfrqCfzIPAZJKNqWGENju7sdpqesaAmizMZivEiv3MZWYSNAaRKtCFP8u74HUBjgUzR-7fi-ipwQR6jfYOtT_B30O38ofrp_Irz3UEyriajmREWt1OKtvRi15CxF_pjyZJP6Jdd_NErr8t4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نماینده تام‌الاختیار مدیرعامل هلدینگ چادرملو در باشگاه با انتشار تصویر خبر «آسیایی شدن چادرملو» در سایت‌های رسمی فدراسیون فوتبال و سازمان لیگ ایران نوشت:
طبق اعلام این دو سایت، چادرملوی اردکان آسیایی شده. آیا کسی منبع معتبرتری سراغ دارد؟
با استناد به همین منابع، تیمی که در زمین حریفانش را شکست داده، به آسیا خواهد رفت.
ما به زودی تیم‌مان را مهیای این مسابقات خواهیم کرد.
مطمئن باشید از حقوق مردم اردکان و استان یزد، به هیچ وجه نخواهیم گذشت و به هر تصمیمی غیر از این هم واکنش محکم و قانونی نشان می‌دهیم.
مسئول جمع کردن این افتضاح هم فدراسیون فوتبال و شخص آقای تاج است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/97632" target="_blank">📅 16:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97631">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de1f0184f6.mp4?token=KH11pu8NrrvVAlExUWsurYJUfp-Jr_D0i_b7LBSEXRQjII9zFaty3V1VamYzC-1o_cMq5-lQ8Q3WkkBV53HtIHbxiGDlcDnCRpuXofKO2e-45wf7-vD3UEv1eYx5KfWpGvpk_xmTvtHHHJmGoiB83wcDk-5eQlFSI4QWb2VrWdoSzW8GhA55avpQastybXrLEnDqqn1Ie_a2HaUAv_Q2KR-h5RwiDLSBpRWZUwFLly5ZCpNKa5ePXwp5vjWhw-5rz51bu7ONhrFQ4UiuRGND5ZMsYG4BCHj5yLC5QwPSTNyCkUui2VgOv8lyo2IbHLVzbz2qLAs66HM3W6IYNVUJPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de1f0184f6.mp4?token=KH11pu8NrrvVAlExUWsurYJUfp-Jr_D0i_b7LBSEXRQjII9zFaty3V1VamYzC-1o_cMq5-lQ8Q3WkkBV53HtIHbxiGDlcDnCRpuXofKO2e-45wf7-vD3UEv1eYx5KfWpGvpk_xmTvtHHHJmGoiB83wcDk-5eQlFSI4QWb2VrWdoSzW8GhA55avpQastybXrLEnDqqn1Ie_a2HaUAv_Q2KR-h5RwiDLSBpRWZUwFLly5ZCpNKa5ePXwp5vjWhw-5rz51bu7ONhrFQ4UiuRGND5ZMsYG4BCHj5yLC5QwPSTNyCkUui2VgOv8lyo2IbHLVzbz2qLAs66HM3W6IYNVUJPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇵🇹
تصوری که پرتغال از بازی کرواسی داره:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/97631" target="_blank">📅 16:04 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97630">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7f836625f.mp4?token=mF37VE734kQTE5gfbVg3Gy3WpQ0Y-AW1NfZOIKc5VNMoJ9FBD9A8htnorp2yjiCZ2WGCMbnCjKf_I4gzfcbRox515bdo7XAJ_ZofVZwVe5w9dl2_qHJ23noV81vPJDOHn8n_qgyYBSZY4zCNAW6bJuPFjtwxWtw8dnNCsZLoi5XnuIBrdxfCceOWA63if2dQeMGAtvAHAfRh8UrkZApVpu0-_BGmm0z1qmSits3H4eEjwk6Obj-v_v6QWO4sgQrgSywErrgH1QLviqOmPBcrY1MGIpXDRim_iT_NpTgA50yNtTZ7EyDvlFglDf1V4CRBXP-RMBAfVwiTzS62WFkSYYcRkqgU8tHxXruhFtKdx5VB8TZgjGlIvAGk5Y_h-3cqlxFGik4aa7KpPsHTUnTa5vr9StRfXZZsX7suRm_GGSesm-8gcFmk951lbBk6j-fMiAfwET_mYOVYPcO99ir5JuSQpOaOdky1x2iDeFF3AKbaacHwwFQRUm9pig7h2aL0SQEMCBVLqiY9ceSdIFg43PUyp2tMJRTe3-29ii8Ui_Ej7k2uIPCM52DX8qt5HA_8mWWlRXcZ7iYiVt-gnmqtOe7JHeU71jRpawx8GVaATTNJHBlGvRhsOBku4RIaJWQAnmu6iJ7pLvK-9ubfjwTT83XJcbTb2dEUDO5SPfgWeyo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7f836625f.mp4?token=mF37VE734kQTE5gfbVg3Gy3WpQ0Y-AW1NfZOIKc5VNMoJ9FBD9A8htnorp2yjiCZ2WGCMbnCjKf_I4gzfcbRox515bdo7XAJ_ZofVZwVe5w9dl2_qHJ23noV81vPJDOHn8n_qgyYBSZY4zCNAW6bJuPFjtwxWtw8dnNCsZLoi5XnuIBrdxfCceOWA63if2dQeMGAtvAHAfRh8UrkZApVpu0-_BGmm0z1qmSits3H4eEjwk6Obj-v_v6QWO4sgQrgSywErrgH1QLviqOmPBcrY1MGIpXDRim_iT_NpTgA50yNtTZ7EyDvlFglDf1V4CRBXP-RMBAfVwiTzS62WFkSYYcRkqgU8tHxXruhFtKdx5VB8TZgjGlIvAGk5Y_h-3cqlxFGik4aa7KpPsHTUnTa5vr9StRfXZZsX7suRm_GGSesm-8gcFmk951lbBk6j-fMiAfwET_mYOVYPcO99ir5JuSQpOaOdky1x2iDeFF3AKbaacHwwFQRUm9pig7h2aL0SQEMCBVLqiY9ceSdIFg43PUyp2tMJRTe3-29ii8Ui_Ej7k2uIPCM52DX8qt5HA_8mWWlRXcZ7iYiVt-gnmqtOe7JHeU71jRpawx8GVaATTNJHBlGvRhsOBku4RIaJWQAnmu6iJ7pLvK-9ubfjwTT83XJcbTb2dEUDO5SPfgWeyo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های بامزه نعیمه‌نظام‌دوست درباره خیانت پیکه به شکیرا
🤣
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/97630" target="_blank">📅 15:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97629">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MsDCMOyoxPQOv90uXppXtcoySJApt-LjpAyEVNMv30CSfUvtEqyY_8x6SlguVV6C83TVjURnm_laHG-uofAt0pMPCzd0fPfvaXPdm2T9dnzk0t9B_NXrLyENUPCFOY_ASVwnojNjAfeg8HFwqWkz792MiLxXq8hDdkMFO5SoRjJsT0W4j9kbTWtT84ATp4yFiYgzGpiTohwNDEGoGEt6X5_R-8lZddaF80t_5DIerPrfKor71GVhs25kppU7ofxIRpXL0UL8Np1I2xxoLI-3i9qymc_m6h5c1ioYVUQJr7-Ydmjmir3r70Tm0UPLmvf8egMNJ0naq87-O8f75oYKoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇦🇷
تیم ملی آرژانتین برای کل مدت حضورش در جام جهانی، ۵۰۰ کیلوگرم گوشت با خودش به محل مسابقات برده
🥩
گوشت‌های انتخاب‌شده شامل این موارد بودن:
💥
فلنک استیک؛ فیله گوساله؛ اسکرت استیک؛ فلنک استیک شکم‌پر؛ پیکانیا؛ ران گوساله؛ دنده گوساله؛ ریب‌آی استیک؛ استریپ استیک؛  تری‌تیپ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/97629" target="_blank">📅 15:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97628">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c29cb7614f.mp4?token=cX_OjZNU6P-V9e06CFMSKpVinMEg2Wu7JxuXGi88ZZI-SdN432bodnToNaNfo_AdD9IHB9xxFHe7a2nSQlF4Deg6xkCK5lJKLhDP859WU9uVAdOUVjs05Hy0rVccvSoXyhTUooWIpS3FtIEPbyhI50AJzBRfDjbnpuoOW_r9apNygBcsu5mN8o0Oe8Bv55_V7-hGwTJNXR97WWJaGJSxlf8s9sT6MuGISOJJafjgQNZpkbR0POMEszIfu4v1xOnhUALj1HsM-_h-f3k6vTEa6VwYRfZcCVC4HMtj1qFDBYOTcBCPv7KFLSs7IsZYFysgs_90dcA4VZT8BNS0hB2VJTR9Iwxk3SyB-3Kwn-C5_0zMLifvDiM8eY0TnV9gT0-yaUZM4AMjLiE3NH5YyUNIMaBX7j_Z6TCdFeh__hmAgMnL9vxx2ropbo91T36ZFGcc4v9Z85ZTGW1EOKwRYi1ikhenqf1A2hf_t1EJBz7bYRmcU41bdh6qO3hNsVVQ-6oj57Ch1nsFRTisVjfaKuXpoATfo_4I2X4oYgqPCoeCchKVQE9TsC_myoihBqTGySMc2ym1TtgrBdGDO9cFyZT1-CRMu8Q0DlNubLe2gheriFjG2WofVACnwxYzxj66ct8s0C95PUw922qxnomYFVPeJyk8DkzZyvvuGrIgYcTA68E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c29cb7614f.mp4?token=cX_OjZNU6P-V9e06CFMSKpVinMEg2Wu7JxuXGi88ZZI-SdN432bodnToNaNfo_AdD9IHB9xxFHe7a2nSQlF4Deg6xkCK5lJKLhDP859WU9uVAdOUVjs05Hy0rVccvSoXyhTUooWIpS3FtIEPbyhI50AJzBRfDjbnpuoOW_r9apNygBcsu5mN8o0Oe8Bv55_V7-hGwTJNXR97WWJaGJSxlf8s9sT6MuGISOJJafjgQNZpkbR0POMEszIfu4v1xOnhUALj1HsM-_h-f3k6vTEa6VwYRfZcCVC4HMtj1qFDBYOTcBCPv7KFLSs7IsZYFysgs_90dcA4VZT8BNS0hB2VJTR9Iwxk3SyB-3Kwn-C5_0zMLifvDiM8eY0TnV9gT0-yaUZM4AMjLiE3NH5YyUNIMaBX7j_Z6TCdFeh__hmAgMnL9vxx2ropbo91T36ZFGcc4v9Z85ZTGW1EOKwRYi1ikhenqf1A2hf_t1EJBz7bYRmcU41bdh6qO3hNsVVQ-6oj57Ch1nsFRTisVjfaKuXpoATfo_4I2X4oYgqPCoeCchKVQE9TsC_myoihBqTGySMc2ym1TtgrBdGDO9cFyZT1-CRMu8Q0DlNubLe2gheriFjG2WofVACnwxYzxj66ct8s0C95PUw922qxnomYFVPeJyk8DkzZyvvuGrIgYcTA68E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😐
جیمی‌جامپ‌های بازی دیشب از این‌زاویه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/97628" target="_blank">📅 15:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97627">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6859ad42ee.mp4?token=BGtgEQkpu-WHVlfr0vPDkaO27ZD491WqdG3bvEjNrormlNnnZC70eO_-JWaqjwDyfh9TNDUGp0e9GNgV9d9mzhY1cB89Bms-rqHeyE218V1CE4q0MvAxsRmPsDjds-iA8GVXvJfzRckL3tMd7fc-leRLj9b4X2_siRum3CP6lFNahlTM6nNVP17Y3_rRgZmfUIVEo4X_3uJGjkq9VKIRj1Kqbgj2JGoJ5AzabeWqei1cn1LbeyKsaaUG3Bd37vtvQDJOVMhkKwzuFoNrHgtHZyVESvTO5ylm9WnHmHq9NlI8OYnPxYpLsNRGwtZfeRJLpmwLQRCTsbJO7NXsf7daUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6859ad42ee.mp4?token=BGtgEQkpu-WHVlfr0vPDkaO27ZD491WqdG3bvEjNrormlNnnZC70eO_-JWaqjwDyfh9TNDUGp0e9GNgV9d9mzhY1cB89Bms-rqHeyE218V1CE4q0MvAxsRmPsDjds-iA8GVXvJfzRckL3tMd7fc-leRLj9b4X2_siRum3CP6lFNahlTM6nNVP17Y3_rRgZmfUIVEo4X_3uJGjkq9VKIRj1Kqbgj2JGoJ5AzabeWqei1cn1LbeyKsaaUG3Bd37vtvQDJOVMhkKwzuFoNrHgtHZyVESvTO5ylm9WnHmHq9NlI8OYnPxYpLsNRGwtZfeRJLpmwLQRCTsbJO7NXsf7daUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ژکو داشت مصاحبه میکرد که اونور زیادی سر و صدا میکردن یهو برگشت گفت هیس همه ساکت شدن
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/97627" target="_blank">📅 14:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97626">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMoris News</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cAlTaJ_QN280UjpuRAXsezSmtHE8E1jTLa88PAu2zk1Cd4zJns_HeNjOy5dhpUHyCjDf8hH7RX_hrtg--SKM85zfevf3N_SBh-QVF1g__Liz7uW26l4RQoARI9dMMad9XhuYp_tJkJGmvnPOGqbBNLTBj6UM5UiB2mcpn-FgpR0cIqJe57T1xGVPvd4n0YMHSJgnxkQ_IxqUqkBahzk2hZZ07_Z2mBG50mDSrgJvxZdR1Rjewq3-u8qwSDqodF6tZJXLXy4RDuRBT1zvOe7TCHO6xP-qTDz8FnAOQd9bJ1Z3gVaYvFg2V5JRRCGRfJ3mF_V8NAr_X4TOhNpKiZ69_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه جدید یک دوست عزیز و هنرمند که احتیاج به حمایت داره
از دوستان خواهش میکنیم با فالو کردن و شر از این دوستمون حمایت کنید.
@egyptinpersian
در اینستگرام</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/97626" target="_blank">📅 14:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97625">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c41d7e1df1.mp4?token=ebe_YJUEnHkatq6DQ7XQojUVhA9X-RuGlzWftiYwdyzINQygqb2Df12G2KvXELuQe8hyJ35_dQmkTFDUF27VMc0MpMMtG7Ac1ViWuWrpSLf9QKfXVCWlhdGYYYfGCZiE9oFBC92O6J8-tQUUBKn4GS_3qfTj1jbFPNluzF3unr9pQTKcupNPToXdl8DS01AMxHeapgNnYWFDcP1CfwLGfpd9d4L4AxURIVegvFgZoBq_ns5l3-lMsqNT8Aeh1BLEMATkwZ4Rbu3BIS7Qws4N1URjbKHRv0YDbhwTDfG6vriFN9R1OR7wMTeWYs6_EE9-tR6rPMDv0PmWpLa_0fo5cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c41d7e1df1.mp4?token=ebe_YJUEnHkatq6DQ7XQojUVhA9X-RuGlzWftiYwdyzINQygqb2Df12G2KvXELuQe8hyJ35_dQmkTFDUF27VMc0MpMMtG7Ac1ViWuWrpSLf9QKfXVCWlhdGYYYfGCZiE9oFBC92O6J8-tQUUBKn4GS_3qfTj1jbFPNluzF3unr9pQTKcupNPToXdl8DS01AMxHeapgNnYWFDcP1CfwLGfpd9d4L4AxURIVegvFgZoBq_ns5l3-lMsqNT8Aeh1BLEMATkwZ4Rbu3BIS7Qws4N1URjbKHRv0YDbhwTDfG6vriFN9R1OR7wMTeWYs6_EE9-tR6rPMDv0PmWpLa_0fo5cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت مردم ایران که نصف شب فوتبال میبینن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/97625" target="_blank">📅 14:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97624">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/koQOvvvSqC6dSymvRgWPHvf4gOblUWOCVRzSvjsMZhacs80hWpV4s7emeZ48q4CUjp68XH_HNVaN6kAfRo2sXTfbLvtXA-uLfckpatbQr9pzxO8GzU0RPAp__2-aW0dZ1mhuG-KULblsAH-NMhELeeBo-9y3b30ATiietZXO2rkoF1PbknWaqntGdPYKt-bHSRdPfrWNLcVHBnzVic56SA1jmj6cN5kWwzx5vSpvWjlcAY195e2uzFilDeeCphSUphGBf5JLGGMj2DlwDN8gyHfkp9QpnMq4GVb5fTUA8QYZX269McnVegxkwKH_O3mIGZihaBaBd-P9gd-j2BreyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
علاقه رئال مادرید با انزو فرناندز:
👀
🎙
خاویر پاستوری (وکیل انزو فرناندز):
چه کسی رئال مادرید را دوست ندارد.. من حتی آنجا بازی نکردم اما الان در مادرید زندگی می‌کنم. انزو همچنین دوستش (جولیان آلوارز) را آنجا دارد و بیشتر اوقات فراغتشان را با هم می‌گذرانند. و جولیان هم برای انجام برخی امور کاری به دیدنم می‌آید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/97624" target="_blank">📅 14:30 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97623">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6470fe1aae.mp4?token=dPJ8PxGqmAXQTXxQZkWxYBKyixyR5HzOU2m93hAcZ_iZc5xvgTEtGZ0fUVUjGl_qTVr2bfNj3H4MZArlyVx4WY48CIUo4jE4miqZKD_qy3jFpNWzNO9BJWf18WNpDxFiC0GlyZjxaLaYHrWPKfQml3wc8lnMxNOn31sZcucxF1nieFClwE60BAge_rHf1RhYNaYOTTfsWHLtpOZeAFl2syXWS0jCC_PNnqzsKXP_wbs2AxyHnQf7fwEgMDFHv6oND2pCd91XNyg8wxl_UgfQIRYgDiaXgCbdgVIg8eDuSXPzIB4y4bXTEqtfNl5PDuWYIh-Q1EHYZWdHAykdFUhYW6kKekTG0SLKQWqE1fi4HDjucVc3rje9r3pn3-GgHvGwYHP03ip1VcAycs8Pf1x_27sozUDBD9Gd0vN1Icr2BmEj2kCYLO0Ky8Jyd-3pZ-5eP8EVOrcFOSoFHdVvXYlXxyHd-NRBEp6tqN45VNOyXknUZ-eZ58t4NXZCuLHgpfieu19RSGEG4louJGc_Kllp7duadWN9SodkoxGas-9EdsHMUFwS95rLvE9EBVR1Q-NfD5aB4FGbjzOoKKcoHhKc0XhN9Hd4tq4ILu_mD3yVFu5xfzaxzAiRLYuvq9NaiR6s81O5xVtrxxt0xiLUunS0xedYNrGVA6F9JTxZ6aEeyMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6470fe1aae.mp4?token=dPJ8PxGqmAXQTXxQZkWxYBKyixyR5HzOU2m93hAcZ_iZc5xvgTEtGZ0fUVUjGl_qTVr2bfNj3H4MZArlyVx4WY48CIUo4jE4miqZKD_qy3jFpNWzNO9BJWf18WNpDxFiC0GlyZjxaLaYHrWPKfQml3wc8lnMxNOn31sZcucxF1nieFClwE60BAge_rHf1RhYNaYOTTfsWHLtpOZeAFl2syXWS0jCC_PNnqzsKXP_wbs2AxyHnQf7fwEgMDFHv6oND2pCd91XNyg8wxl_UgfQIRYgDiaXgCbdgVIg8eDuSXPzIB4y4bXTEqtfNl5PDuWYIh-Q1EHYZWdHAykdFUhYW6kKekTG0SLKQWqE1fi4HDjucVc3rje9r3pn3-GgHvGwYHP03ip1VcAycs8Pf1x_27sozUDBD9Gd0vN1Icr2BmEj2kCYLO0Ky8Jyd-3pZ-5eP8EVOrcFOSoFHdVvXYlXxyHd-NRBEp6tqN45VNOyXknUZ-eZ58t4NXZCuLHgpfieu19RSGEG4louJGc_Kllp7duadWN9SodkoxGas-9EdsHMUFwS95rLvE9EBVR1Q-NfD5aB4FGbjzOoKKcoHhKc0XhN9Hd4tq4ILu_mD3yVFu5xfzaxzAiRLYuvq9NaiR6s81O5xVtrxxt0xiLUunS0xedYNrGVA6F9JTxZ6aEeyMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تمجیدهای زلاتان و مورینیو از ایران فیک بود؟
‌
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/97623" target="_blank">📅 14:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97622">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/un7ldE6mFKyG6hwiiYLLWs4twH3mnBh5zx1p3xWbl7HwHIbxaNOSDNc8r914DuRNNOFa8-PsFBTb018M043lQtYOfOC4eC546r5Nmak-stxz9Dx8TyA4dzgk5b-ThUx4AtGyr-srfeMpBss4b4kXf4TCf4KFJTD3INFi8fEAho7kt8SjyCP0ng8YN28q9_ees1rIZhfQEgwF67P158zl0I-fJvbWztWvej7yD0wAkPuOlrEG_vvWt2Ej-e020F1zo0bDmZ5l1dKj12ok0UuLUe29a7fQtoKL7S2DBabJyKRTR2vs_tDygF7THME2LFtCyApc8i1lkbQLdYj-3kkznQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇳🇱
#فوووووری
؛ ترشتگن با عقد قراردادی به تیم فوتبال آژاکس‌پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/97622" target="_blank">📅 14:18 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97621">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fl0sQXYgrPaV71T2132nZeEhIiQv_l6lzpx2k3s3JZqzg3dQ81dnQ_pbyCn_h5OM9a5X4-Peoh29HVwozEgKkua0mR-8NBlIiL7NBZiRl9cpLujX97vCaJZ3VXDleqRA560RoyHP7Ysk-d0n8BIgDI-QEGrRxa7ta2901Hon1xoI4bK7Dn5SdNX9ID0ygRX5PXbsKbT78u6pPcQtA6tKRBQdub591pV-4x_RqWEwykQLRz4pBhM97TL3KtdFOSFK5tjbEsADUisidkZ4jANRATgpcT1rmxoS00pLTLsfq2wCWtXYEYHQ3orNG-Zvfhd16MwH_ps698hEaUZQ22zFeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
#فوووووری #اختصاصی_فوتبال‌180
🔴
با تصمیم نهادهای امنیتی و توصیه به ارکان فدراسیون فوتبال، امیر قلعه‌نویی با توجه به فعالیت‌های اخیر در دو سه ماه گذشته، روی نیمکت تیم‌ملی برای جام ملت‌های آسیا خواهد بود و خبری از تغییر سرمربی نیست. این موضوع پس از حذف ایران…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/97621" target="_blank">📅 14:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97620">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/97620" target="_blank">📅 14:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97619">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2f0deb63b.mp4?token=ThGgp30V5E64CIPfsizivfocgjRZiz1lUBeZ1HZuovVmSm3WpTrKsqRHls1P8kwIyBVqgGboVSUECuZCs6bfYpIXrH5rbiQJNoQsXEv2ABAyMEVMpnLjcXLaMEGuTXEiuc-41pVWACd3BOuboP9-KBYAVZqpjt-wA_4bqGG-2JqQQ3E6AIALM1U32ZhEw-_fosKrOKGJ_Ukmlf7g-zNw49ucUNVAXgo0pywYBV-m79svVkbc5SM3hT0prxm6txAXfqZ048ei_kZ55BtpXQAqUDmSpAMkLuyOAB1vkuLRDhwYH3ytiUKnELkeNLgJh36Dux4zNy-TbI-jzkcDBCqYvrX6GmM7jeU5wx1-eGCz4rVIZ3S3ChLLUvIYVeAKreldOv9QrrKUt46qXnE7SDohr_nH3zkjHWgBgq2I8k4AuvVEU2x0JrhxJjdPvuFblRj7vMGzI5hSchXFRXPTPrjAuYRErifMBWQCe_KdwQz3U2kOcfAjFTxjbk6Y7Tr_Gz1_PWYGGkvcHRJIEvnrbs2IfTnlnsz5fyASH65axAKetpkiKtSrya5B64ZqpP1b5FkdC_4rCCBA91GBP7DcV31sfhYUwtA7SWWzpEzt5AmeqOyYWrjO_cD00WrI6_FiOc6upgPtF2hQ7etZaH8JPYdPojFR0MfHJt3iLdTbqq8ADxE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2f0deb63b.mp4?token=ThGgp30V5E64CIPfsizivfocgjRZiz1lUBeZ1HZuovVmSm3WpTrKsqRHls1P8kwIyBVqgGboVSUECuZCs6bfYpIXrH5rbiQJNoQsXEv2ABAyMEVMpnLjcXLaMEGuTXEiuc-41pVWACd3BOuboP9-KBYAVZqpjt-wA_4bqGG-2JqQQ3E6AIALM1U32ZhEw-_fosKrOKGJ_Ukmlf7g-zNw49ucUNVAXgo0pywYBV-m79svVkbc5SM3hT0prxm6txAXfqZ048ei_kZ55BtpXQAqUDmSpAMkLuyOAB1vkuLRDhwYH3ytiUKnELkeNLgJh36Dux4zNy-TbI-jzkcDBCqYvrX6GmM7jeU5wx1-eGCz4rVIZ3S3ChLLUvIYVeAKreldOv9QrrKUt46qXnE7SDohr_nH3zkjHWgBgq2I8k4AuvVEU2x0JrhxJjdPvuFblRj7vMGzI5hSchXFRXPTPrjAuYRErifMBWQCe_KdwQz3U2kOcfAjFTxjbk6Y7Tr_Gz1_PWYGGkvcHRJIEvnrbs2IfTnlnsz5fyASH65axAKetpkiKtSrya5B64ZqpP1b5FkdC_4rCCBA91GBP7DcV31sfhYUwtA7SWWzpEzt5AmeqOyYWrjO_cD00WrI6_FiOc6upgPtF2hQ7etZaH8JPYdPojFR0MfHJt3iLdTbqq8ADxE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هوادارای مکزیک از فوتبال یهو سوئیچ میشن رو بوکس؛ لامصب چجوری همو میزنن
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/97619" target="_blank">📅 14:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97618">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FJ6pK0I_kW21hWcCjMnywzd7vEw7RL9E3WW_PT7SLHk0Dsv2cg-s3O7frpkLls5xfbAEd0tWy1Y4AqpwYpPJEd7lxdffhGkLrEnZEncME3Ya2_cvH-7sCBLeeKR8-rtaNTi9Lrx5qO5otXsZgWQNySemJdMmAI9YqP3xkftxHNQp18Sy-atT9UuhoWEMaWB2yVJnWqq6kOfFFsR37Lco87drBRP2xOAXxEx8pqW-Y4lQ16DX5dO2haEDKLI_OLWIwPfxyTdu80KLVICIGTY1d-FKUHSasIBP9Rv9LYpEThl1fkYctW1f_eYLCh_g3XMPt7a4yeN58Iz0O-5eRPWHIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سانتی کازورلا از فوتبال خداحافظی کرد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/97618" target="_blank">📅 13:44 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97617">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jAp_-NQlJya52TjTrAqfmlD8Jy0ZTiaC5n3RO4Z-Ev_4NPhrnlG7sFJXoRBP3_0NnvBonsargucghoymRnhi7iAvJqF-AZ6ohPN1CDgtm4PQK2VnzpgiO81Q3GOQcjp7VX7tdZBkh0QOyT-uORTBO0iuuydg9tNtsJC8DjXRj2CTsqQDrktHKtyENSNnumZJGqcJ1KZaO2jVk0BNs1IrBk4sOdAIrBtJOXVkuSDXWIl0amQ_QqCAXG06xJlCxR_O6SCAgmpouSWpXw3lCszy8hl0sFvPFU1s0hm2n4z_3S-apUG06azs-_EZFrOG8yKJu3V7JgovKc2OIAq809tOeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇽
🔥
مکزیکی‌های جذاب در حاشیه جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/97617" target="_blank">📅 13:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97616">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5e7dc94b5.mp4?token=OEl-MUQ3VwKSdyBBe2SjHN3T3KMD4AvKxy-L_DuzZgI33hMfsJWZjGx-7AiSsb5iq0BB-Ern108di3zbaGHAYdocjgEHkyTgu05gQT3v2gJqX3FbOFzZyH_P-QbZlSmrDXt2jCMiJT7STRLv_LcN3ubJF7avuGytMLVSmmbv_2oArnNfgZxXgJsDx-brMH3ysDmO528eu2Mw5QOZ1DSOh5XEIYe8Y532IwwONXQSwENDRyogSaL3RkXuxn3g9gTnMOsxfGLn5bsHTGFcAg3rHEWBnOF37kx2bhn0VK4kBEsEkgp6vvj4clJTNNVA4c-0wZOhgB_TcIJHHvET3e-Zcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5e7dc94b5.mp4?token=OEl-MUQ3VwKSdyBBe2SjHN3T3KMD4AvKxy-L_DuzZgI33hMfsJWZjGx-7AiSsb5iq0BB-Ern108di3zbaGHAYdocjgEHkyTgu05gQT3v2gJqX3FbOFzZyH_P-QbZlSmrDXt2jCMiJT7STRLv_LcN3ubJF7avuGytMLVSmmbv_2oArnNfgZxXgJsDx-brMH3ysDmO528eu2Mw5QOZ1DSOh5XEIYe8Y532IwwONXQSwENDRyogSaL3RkXuxn3g9gTnMOsxfGLn5bsHTGFcAg3rHEWBnOF37kx2bhn0VK4kBEsEkgp6vvj4clJTNNVA4c-0wZOhgB_TcIJHHvET3e-Zcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
ما تو ایران چه کار خوبی کردیم؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/97616" target="_blank">📅 13:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97615">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KjdUZEE24Nod2R8H3pI1GDE38MadHzn31SL5uhXarwmq02ZgKPR9Reb5_NdFu5Wg1WFs_Le8v3r0BHY2lYjOLyz9eTyRDIsYEKq4Jf-_bcG1hm5ADMGU1dKQqSGP6JmuHXd8LGYxCZAoknx13OYdAM410JJFJdCx1DZQc3nDfuvbgW1XT3Hlq0hvHoSlpky3dHdWZ4UzA0XU_SSahM8lrpM_2_W0NpdNTMXKl2EHyrBdkF_yQsJA3wUT5F8e-q8xgA4adjijqT3waNFCPgUQZsqD5J1OenWBD4TPeKsOKXX_WtkSrzBoPrPy97VCTgL3DhsXMhz4OmuSEtoX4RTusg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
از حواشی بازی مکزیک و اکوادور
🤣
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/97615" target="_blank">📅 13:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97614">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A6oLOy9QlxQPwhyUOOIikkdfVlKSexav1BgRp8442eykpqq_mRxhkYiW3XkG-hF-T6sIUZ8hx7aNPyRu7PZmxa0UTUn31rAWeSTCdVm0wICDY3zv0uUEgpLOCn4_dM5SgZHZcJ9nrJ2Pr8cLJBTZoNujST6Kd7oDVL61wbOT1txCv7Oerm4OsZfZFJpepAjwlI6xirRxbWE-wOO76XOStFYtRdFkD3fzTD8T1pN27-3XABawnYULtD_TBe8Nwb9zT8TrAjbXBXBVV8eVB0xuYV0jQ6y694fKeaRHyql20gtrNi-pCvs0B85MNbvdCeHn25k6mVs6XQ7cb43-uuXK4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
فرناندز تو تاتنهام شماره 18 رو میپوشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/97614" target="_blank">📅 12:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97613">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/204ff9d4a4.mp4?token=Ap31tCk2btudSWKfC7Z9JsW0lZpE49nRDX8ApGPnDd4JihdR4JH-iG43Jt6UfN3NFhKKYDrhZWzgavqQ3Sbw7IhrjgLM_jX4ZAHgUFuLJP2PThs9Mhudo0TmkppaeiDbVSsL3LNOmCFCB6UTtK-EsIlKiadyCTvDd4uymodeWHv7x8Ezbw1w_WBGByLZ-3fILhCRmugA9AHSCMX9v6NHegkigGffg5yj0NIVHeRw54mVURWxd7nuVPNOsJJ8SPbJwxJeS70cCsgUyXuv1DmfKQ9JSkLrCAoSzLKzBsGPMLTVGyAw1AN1saXQBGN3I-kyKS256Q1GQjYG_nNICXy9Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/204ff9d4a4.mp4?token=Ap31tCk2btudSWKfC7Z9JsW0lZpE49nRDX8ApGPnDd4JihdR4JH-iG43Jt6UfN3NFhKKYDrhZWzgavqQ3Sbw7IhrjgLM_jX4ZAHgUFuLJP2PThs9Mhudo0TmkppaeiDbVSsL3LNOmCFCB6UTtK-EsIlKiadyCTvDd4uymodeWHv7x8Ezbw1w_WBGByLZ-3fILhCRmugA9AHSCMX9v6NHegkigGffg5yj0NIVHeRw54mVURWxd7nuVPNOsJJ8SPbJwxJeS70cCsgUyXuv1DmfKQ9JSkLrCAoSzLKzBsGPMLTVGyAw1AN1saXQBGN3I-kyKS256Q1GQjYG_nNICXy9Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏆
خوبه کشور بنگلادش تو جام‌جهانی نیست وگرنه با این هواداراش سوژه رسانه‌ها میشدن
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/97613" target="_blank">📅 12:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97612">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gAM_RKzIGYyaP4zTCthA06LCZ6QykEeulplMXykw_x-7lAI0Wd3HnItprs6KYuidwwfPAZ00v0PyTdPoidj7JYa3BtMsC1UwBrnUzsNGvDYIRPUq_V717akN6WlGWHBxkM6mLvwj8Z33crhALrbHfhxh3snt_K2lX_uBh_u-1uE_unukMmIya9DIMMaO2xPyg4MD39lNE-dld8Lh1PkAMwFteck_ldbPhlPXVASKS72V6wQ7stB0nRzBMXk_EM8f77TC-mV9JANoPGJlNR7Zn5HAAFEQYQXn0oI0kBl-16veDns8ZTDiu8luIpxeqN4vup7iGPBLBYxisygDLE5Y6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
🔥
انقلابی در صنعت هوش مصنوعی
🔥
🔥
🔥
🔴
میدونی هوش مصنوعی ترند دنیاست و اینده ی اقتصاده ولی بلد نیستی ازش استفاده کنی؟
🔴
تریدری ولی همش استرس اینو داری ضرر کنی؟
🔴
یا کلا ترید بلد نیستی ولی میخوای سود دلاری داشته باشی؟
هوش مصنوعی TimeTrade این مشکلاتو حل کرده
✅
هرکسی با هرمقدار علمو دانشی میتونه ازین هوش مصنوعی استفاده کنه و به صورت live و روزانه درامد دلاری داشته باشه
🔥
👇
https://t.me/+hcwmoHXpF6k5Y2Q0</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/97612" target="_blank">📅 12:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97611">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BhcKeL0qfmqE2FeKD5WM2OAEZSrcewZJLKbt_b4i45eN0eSIg03oGYslH0M3CtSueDTPvnuCRCoeGm4OoeaQv963mZ8WHPNVayY1nlawFxBAAri4XVnE-w0bazlQavpL3RUmd365OdRMxH1QqMHwAiUgzGE6QXEVVd4g9oYn3Dv3kNmoaBjBI3qXaY6_CpM6grYgHAp6pEuNIXTMzKG4KXZq07kcU_GbWF9D34OY5h3rg_zrMuGqlaDXab6hWbmpImEu52lBaD-BhZq-P7wooRxwDAlJp8Q0paEZIkNZcRGULuHmlmVErdjSR8mWnEiP8MhF_rsVMFp0kufNZtmD4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
#فووری فابریزیو رومانو: متئوس فرناندز به تاتنهام؛ !HERE WE GO
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/97611" target="_blank">📅 12:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97610">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p16fdVwwlPzphNhu-JaPYD3NaT13wQAgHRlzMXxShPndzqtMbRhTZivHz_iVjjRrU5VvWlbwcy1leLjVqaZEOFL4FP9iEClbJPH2t8jvjQCt9RoDcH_FX3yBArA9x0M4yhQG8M6Jli4GfCyy4CqGZZxosqZSC0g5VWR5V8VW2Ex7YrbN6WV6aKXRgVgCsHAEyPAKAB3NMSZCrubhwxF9YctWfvzGb0qt0VF8xGairys-8g842wZYUhemtCM3VgexThhu0MmWjQCHLabIepx4hYrq01QmF2XYDC8UbfniiCZxiXOrt3Z0yY8XppjXDSXdLav-4bCzH2Sv75MpbeNx1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از باخت کنگو جلوی  انگلیس، سباستین دزابره، سرمربی تیم ملی کنگو متوجه شده که پدرش حین بازی با انگلیس فوت کرده و از دنیا رفته
😭
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/97610" target="_blank">📅 12:26 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97609">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BqiJbfadWSpUYf2xDHLzrx6qZs2S30eJtNBiuh4goq1pbf7DLjPG9wk3RiKshNQ6lZt36BX7lNof2Tjjw_lwsq72qi-71mF0SuwrL9AHtJmZ8VeoWUxTCXn8eB-bfTXtowTuixxprhNfxlcP5QwImEqdFLp5h68apC61InvJv955H55kTMAVCgUuw8zFlXOILHLSQa3_vYb4H020uv4x6b44TTV-o32GTyxPlAZ4nXrsoODrb6916xL9hRZvECBsAHvr-Qw3qM6Cl1FlHTB0rpAa8KbUKpCxCcedzGQ_uGxmKvsNpDNFdzdQ_3ECALcATEmThd1BD7dzBRcLIbO3lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤣
🔥
کار درست مثل گاوی که بین خواهرش و زیدش رفاقت به راه انداخته تا زندگیش بگا نره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/97609" target="_blank">📅 12:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97608">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbba94933c.mp4?token=B4_PDEcp5fyBuE4dTDIBiSB3aDllJxPoYRjIyYNtELNUAptrnq7clsc8gdnk60v8gKNlVGiHC0rVEJjKb-zJaHH_oHEc910LBBs8tJcjZv3SXA-rap4QOjhgGapd-USWHCjmlSEwgbcoj-3iOb-_ceQ3Nsmp63d2jY-4KbN5TfngxHClXp3dgpn4YgM_SbeXg_9LOcOrjcd4jNai4STENYW4o3d81dk3n0cgE9QixHf_fnprJOfQcaF4QDCNZBCMXNPlCaUcQnC57PTzMalBoHRUVMh0cG2GwHuZzL7MEkdGnu0fwDF2BkS3knvA3JZ6yNoxhEbLnP2MsMjQcAaQPoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbba94933c.mp4?token=B4_PDEcp5fyBuE4dTDIBiSB3aDllJxPoYRjIyYNtELNUAptrnq7clsc8gdnk60v8gKNlVGiHC0rVEJjKb-zJaHH_oHEc910LBBs8tJcjZv3SXA-rap4QOjhgGapd-USWHCjmlSEwgbcoj-3iOb-_ceQ3Nsmp63d2jY-4KbN5TfngxHClXp3dgpn4YgM_SbeXg_9LOcOrjcd4jNai4STENYW4o3d81dk3n0cgE9QixHf_fnprJOfQcaF4QDCNZBCMXNPlCaUcQnC57PTzMalBoHRUVMh0cG2GwHuZzL7MEkdGnu0fwDF2BkS3knvA3JZ6yNoxhEbLnP2MsMjQcAaQPoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✈️
🇺🇸
پرواز جنگنده‌های آمریکایی بر فراز استادیوم دیدار دیشب این‌کشور با بوسنی و هرزگوین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/97608" target="_blank">📅 11:58 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97607">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🔵
#اختصاصی_فوتبال‌180 #فوری
🔵
باشگاه استقلال با چندین ستاره‌جوان لیگ‌برتری به توافق نهایی رسیده اما تا باز شدن پنجره نقل‌وانتقالات آبی‌پوشان، هیچ امضای قرارداد رسمی صورت نخواهد گرفت. هرچند شانس بازشدن پنجره استقلال کم است اما پیگیری‌های وکلای خارجی این باشگاه…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/97607" target="_blank">📅 11:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97606">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38ac3b752e.mp4?token=vgW5PF5V-ch9YaVAl8ZsV7YgGV5cGbgULlcMeOJdAPkPTUDiXIE1m-6TZuG7KEjJ-x2ciVAIKfY5eujHE4CtZ_jCuUc8jveK34jl6wkYQWrIS5MPwsDjBnbuHvn8Ypu9rTwnvQCOX6L-BESfMRAJvs2aX3QX3L0NSyCP6X0pHf9dYZp6E3NUHW4wU9NubKOPDuOBGPjpiztOuOERsKy2YXWJaJPbweTEeBYvfPo7J1fYSAok8oJmOkuMAqmJh280sbRrOB7W_zKhOMvoP_62ZUCE8Er8l5WHWB7o1GZRVI9nJ8f_3IzvRss-lzeno4GALyMZ-cME3ptVM6ZCdPwtFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38ac3b752e.mp4?token=vgW5PF5V-ch9YaVAl8ZsV7YgGV5cGbgULlcMeOJdAPkPTUDiXIE1m-6TZuG7KEjJ-x2ciVAIKfY5eujHE4CtZ_jCuUc8jveK34jl6wkYQWrIS5MPwsDjBnbuHvn8Ypu9rTwnvQCOX6L-BESfMRAJvs2aX3QX3L0NSyCP6X0pHf9dYZp6E3NUHW4wU9NubKOPDuOBGPjpiztOuOERsKy2YXWJaJPbweTEeBYvfPo7J1fYSAok8oJmOkuMAqmJh280sbRrOB7W_zKhOMvoP_62ZUCE8Er8l5WHWB7o1GZRVI9nJ8f_3IzvRss-lzeno4GALyMZ-cME3ptVM6ZCdPwtFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇯🇵
ژاپن، غیرآسیایی‌ترین تیم آسیا...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/97606" target="_blank">📅 11:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97605">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SDqJofLqEeUXS72OlGTk8PoDSmEQFXXTjnn9hrOZJ6WkIeGmmWEGj-JF706CxOk2f9Huu0nnrhPeFoXDV9la41I_uq7DeiEnp5g3iN6J4_fBcSIUQw_9cOBSLMHGHFCAYOeqhcRXT38SyTBW90X3gQ2V1e7a5AlM7470X0tCA1RRQRqTtzqU8DOBiDsQRAh-PE7KD57HZ3A2Hg5w-YWSuAcMy6r2MhephzOsa8m1HdLc6O6YCEoJfEchrR6ifDBu2g084KjSuutmvmOxnRNeIekpaOzUpB039hgJ6wxlP--_wKM2kvCTZ2zlTtzazQjvn1DmwHZ68L2fkdAhDPWlrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فوری - فابریتزیو رومانو
📰
|
🇮🇹
— هیچ تماس، مذاکره یا پیشنهاد رسمی بین رئال مادرید و اینتر میلان درباره انتقال باستونی وجود ندارد.
❌
🤩
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/97605" target="_blank">📅 11:31 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97604">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea402ec7ef.mp4?token=mGgE_vFifFYhMUif7WRV5i5_z2aJhDZW_qb8b6RZVnGKWF5mphRSBIq47IhBWAafrMud-FcGLq7_xNj8bNS8QT-sdDNq8FmGoKmJF4o2RGPAw2MfBAqImt9HI_meVoc7CV3KbXYfXsUi26VautPsdKrhoTTIrEG1Cvif6w3pzaxxRVBgU29LRW2sp2TVXEoxX-LjUEkPf1m-PDjzQcg-sugtdR9sBkGstcz4Ti4zd2eDFr9HLgWJFHBy6TWgwWJhoJAw-MiazmihTNgQYHk6EdkR3KZTNYNeF4tbkiJGB3MWvQ5uC29GsVZKEoHect5BMX-RNldZNkScO4cUvPrFEkYLkVKDKsQ4_aYDTkOoKeh37hieVdBAAoDZEjcwygqZLBszife9CUp3KRnhr6G6NKn_Ras5bdkz3nW1Cs6aOuCDqU3QHFDF47VK8DVqh6PdLP5plXb3hX7f8a2gpLA7g_ouz3MI8ik8pecborjoWNtOhBQ1S-rFOd05B4en7Bt5bMhp4UycTNYjc4nSyxZmokidukAl1n8M4M6pi15GDStwNg9iOC3rH1ygtxHafvvZHY0HGhZgVkL295dxWcgW8FgoiAPJqGD6pjJ3FzBpFx4LwAoSRdALRQyrTHbygqDxwsNg-HcXJW5czEDqIytOjV1vuG87ZIOy-Ry4luPzv74" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea402ec7ef.mp4?token=mGgE_vFifFYhMUif7WRV5i5_z2aJhDZW_qb8b6RZVnGKWF5mphRSBIq47IhBWAafrMud-FcGLq7_xNj8bNS8QT-sdDNq8FmGoKmJF4o2RGPAw2MfBAqImt9HI_meVoc7CV3KbXYfXsUi26VautPsdKrhoTTIrEG1Cvif6w3pzaxxRVBgU29LRW2sp2TVXEoxX-LjUEkPf1m-PDjzQcg-sugtdR9sBkGstcz4Ti4zd2eDFr9HLgWJFHBy6TWgwWJhoJAw-MiazmihTNgQYHk6EdkR3KZTNYNeF4tbkiJGB3MWvQ5uC29GsVZKEoHect5BMX-RNldZNkScO4cUvPrFEkYLkVKDKsQ4_aYDTkOoKeh37hieVdBAAoDZEjcwygqZLBszife9CUp3KRnhr6G6NKn_Ras5bdkz3nW1Cs6aOuCDqU3QHFDF47VK8DVqh6PdLP5plXb3hX7f8a2gpLA7g_ouz3MI8ik8pecborjoWNtOhBQ1S-rFOd05B4en7Bt5bMhp4UycTNYjc4nSyxZmokidukAl1n8M4M6pi15GDStwNg9iOC3rH1ygtxHafvvZHY0HGhZgVkL295dxWcgW8FgoiAPJqGD6pjJ3FzBpFx4LwAoSRdALRQyrTHbygqDxwsNg-HcXJW5czEDqIytOjV1vuG87ZIOy-Ry4luPzv74" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
آموزش رقص‌ توسط ایرانی‌ها به هواداران مصری قبل از بازی این‌تیم با استرالیا در آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/97604" target="_blank">📅 11:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97603">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RN629o6ujDKY0YjOz63MRx6LmdwHO2wBfP1T3P5P9aFs5fs9QgP37HLigndc7ydLcjATYmKa36QjNN_akh2pO8_r9VZl0RuOyohu3EgKdFR2XitPDJlonw9OsoX5X4eYyMuNnKeRMisw3nl5tCUg8q2d2J_U1y2S_NPTv9pREDZyej37JmRarQEvvPTdEIEcQL_IPri_QbioXdZm53qhNCkN7gtbGt242Uaf204BPv2VG9Q4VrSsb-f5tTrMd8CxqcXnhBEqEtG6eNmUMM4NcwUL8Swly8yr5YD4S4N2jV1I8EweWTOLlWgFC7BSUuIh26ex--HLf8W9O56rWH0hDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🗞
#فووووری
از آاس:
🇪🇸
سران رئال‌مادرید پس از نمایش درخشان اولیسه مقابل سوئد تصمیم گرفته‌اند که برای این بازیکن تا سقف ۲۵۰ میلیون یورو نیز هزینه کنند و رکورد تاریخ نقل‌وانتقالات فوتبال را عوض کنند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/97603" target="_blank">📅 11:15 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97602">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ed83a057c.mp4?token=iH9JJbvd7-Gv8ktbR2aabdSE0y-_BWhvt86n2ixYxKyyTYvOY3nnPG31xAppjaayI1uRwT6C808kXrOYzHS0JZ4fbJa9SKEvmqajE1fR4V08iRr-g6ToN6Qq7-JExQbBuXnE9zFQJCiFvg5gxGAZJ2IfCMZKTyE6tBvmNwg8aJqDBt3IH7nlRGD5bqXy_noq-Gp-mZ9nlF8-l8ZFTFYUKm0mLiwuHzx8VIgDvz_toTX0ISH_hQ8F42WXxn7ft7WV8q4KSRQdh6HhI8W_NSf3C465UuzGwWNaVUzSSFGb4VVjFSwQdivxP-MesIM1213sOBKHAMZcs2rb9tHOAigr3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ed83a057c.mp4?token=iH9JJbvd7-Gv8ktbR2aabdSE0y-_BWhvt86n2ixYxKyyTYvOY3nnPG31xAppjaayI1uRwT6C808kXrOYzHS0JZ4fbJa9SKEvmqajE1fR4V08iRr-g6ToN6Qq7-JExQbBuXnE9zFQJCiFvg5gxGAZJ2IfCMZKTyE6tBvmNwg8aJqDBt3IH7nlRGD5bqXy_noq-Gp-mZ9nlF8-l8ZFTFYUKm0mLiwuHzx8VIgDvz_toTX0ISH_hQ8F42WXxn7ft7WV8q4KSRQdh6HhI8W_NSf3C465UuzGwWNaVUzSSFGb4VVjFSwQdivxP-MesIM1213sOBKHAMZcs2rb9tHOAigr3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇧🇷
🇳🇴
اینبار تقابل دیدنی گابریل و هالند در سطح ملی و بازی حساس برزیل
🆚
نروژ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/97602" target="_blank">📅 11:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97601">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">لحظه ورود تیم ملی آرژانتین به میامی
تفتیش بدنی مسی و در ادامه خنده هاش
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/97601" target="_blank">📅 11:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97600">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🗞
رومانو: فلورنتینو پرز برای تکمیل معامله اولیسه دست به هرکاری خواهد زد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/97600" target="_blank">📅 10:53 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97599">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FtxsuiB5UY8PaugBGKA0QWjLIy-dzwiqN4SY0tofQvZdhmyA7likALSyDPPSKIY51lW3Vq0vfNlMwdnE84_1Fa_Oxz0lkHJacPdEBQbvrndFI9SDOcTbWcfoqcaL3f97yHLTRCTWoIMzvQeLXHggUqp3xY7ugSk4OHhhc7ingtDqxTd01Go6x_feQO0V_Jj4WhWXaxQ4QTTEyKpymZGRZb4mKtb0lV4XRjC0-ffBA-0qbtyaFcTSdrbtuxaEvW_wRJkYlZssyFnCacseH8It2rI26Fzsw2QT-4c5igFFRlHCar8ROxm0vgG9zwxvtBc4xb4Z6VCxPMgbFF38qW_rLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
⁉️
🔥
#فووووری خوزه فلیکس دیاز: رئال‌ مادرید و یک تیم دیگر با نمایندگان مایکل اولیسه درحال مذاکره هستند. کهکشانی‌ها با توافق نزدیک‌ترند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/97599" target="_blank">📅 10:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97598">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DWWLvg3Q0cGPg5KbAwFBm_m1Y6fBQJ2vVlejmumcVMYRWFWGAZ9goFXDgliOZ6R5yJFEFc2RjYV6OPghd66V7ggJvD4QPZchfXH_4PQS16eYYyND_NWV7iDg5FEWLLVborbniixI7kT6-6ww27HWct9wpi-izUjFNYI_CxUgMmwb_75QzCnRAxPRzFcuYQ12LE5yn25VOu9c-A9oq94gxisBuyWXZaUQ3m6Bm8TMuOiT32P5xoJzArNzwL6ugn23McM9CvTwTE7vr6lLzvia2fUQ29X9heCQ6SNHXbxukhJ3jje5RsAwCcN_ncAbrTFBUFbaCSz8R9oIqo6ul20dmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
⁉️
🔥
#فووووری
خوزه فلیکس دیاز: رئال‌ مادرید و یک تیم دیگر با نمایندگان مایکل اولیسه درحال مذاکره هستند. کهکشانی‌ها با توافق نزدیک‌ترند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/97598" target="_blank">📅 10:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97597">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fMCg4t8Hh_qWueL5LqnsSYEbxAS3-3jmyX9CiXRX5hwCAWWOd7KJZ5ryPhyerlLi164-MPl7Bu9Po5DpQkWR5oGOmrbjkBIBf-Vg0om4_Kuuw0bsE26EbZyhl4LpyPctiGYXU5_R4JEzA5Cm7CuY7NJWs7z11RfM0GXxdy6AVffG1wdgPOTEIXuaa5-dm41ekAfoeKihut5sUbWGTULjJ-eKgL1xw5-_bcu9mEgadB6v5ml9d6aGZlwoHJbFlJku9iCiX8xFn-IOmu7R4cXaI3d2rmzJR_3QKzFavhbUYz3pL_58vsD5QISIVjIc5Aqttl8yX5Cekh37asgAT6YF6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فووووری؛ ساندرو تونالی با رد پیشنهاد هنگفت منچسترسیتی در آستانه عقد قرارداد با تاتنهام قرار دارد و بزودی رسمی خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/97597" target="_blank">📅 10:25 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97596">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aec355d42.mp4?token=uqX3Jutg-TYvAQvNNjoxzXL3aCQCdNTRP95wiU3IEn-WXsMcH6aWLIod5vNzVrsMRANcBoKwxBqNx259vOnSFC3wNcpxnKvFlUKiUZ3EGwXFJ3H57sKyircQxhdo-EYowO7X47fQNp1OK4O84dt4lFMECC-B9VJprHxGaigGkuY1vl5ffY9o8vKynTpR9wovNt6TWR6UtwUtndBGRZWOMy931O3mo76uPEBPZeekVWUVP_74K0dJDaKdboM5PY3Zuwbv-YvSMx3Db3OdQCDy1FDbJhb0_My0aE0b5l4yZk6OSi8uEP4nrT0yNLG4HQNlOVSrwLcR3EOesq1iaFJt4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aec355d42.mp4?token=uqX3Jutg-TYvAQvNNjoxzXL3aCQCdNTRP95wiU3IEn-WXsMcH6aWLIod5vNzVrsMRANcBoKwxBqNx259vOnSFC3wNcpxnKvFlUKiUZ3EGwXFJ3H57sKyircQxhdo-EYowO7X47fQNp1OK4O84dt4lFMECC-B9VJprHxGaigGkuY1vl5ffY9o8vKynTpR9wovNt6TWR6UtwUtndBGRZWOMy931O3mo76uPEBPZeekVWUVP_74K0dJDaKdboM5PY3Zuwbv-YvSMx3Db3OdQCDy1FDbJhb0_My0aE0b5l4yZk6OSi8uEP4nrT0yNLG4HQNlOVSrwLcR3EOesq1iaFJt4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
یه زوج روسی معروف که صخره نورد هستن، بدون داشتن تجهیزات ایمنی و در سکوت کامل دیروز به بالای برج Empire state رفتن و یه پرچم با شعار "وقتی قدرت عشق بر عشق به قدرت غلبه کند، دنیا صلح را می‌شناسد" به اهتزار در آوردن. پلیس آمریکا هم با هزارتا مشکل این زوج رو به پایین آورده و بازداشت کرده. حین انجام این کار، تو بالای برج پسر از دختر خواستگاری میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/97596" target="_blank">📅 10:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97595">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7a9e27c8f.mp4?token=cNxhQLPZY8MAYQNe4bUa4FI8AXGjU48KguLxol6hYJnry046f3GV90mBzkYTNn-Bz0UwE1o8SkoMxTlDNCwY5pX5QFtiIMe99S5bsTmsy7ZlYSLLvc0fYo9LZNgKmifegW6kAyDM-iLsRI-j2OhN5PeEtcK4s3jFHs-U06PvJvgehSgGJ_tH85lEEcCXDfZNyJXjGBrql9QhyVIvU--qq9Gx_rawOgL2BtMq-1WdCq3y4y5DexmjOm5-0zTsFI1Ka5ci8sjjUan98dCt2lPDVDY2P_TAei2hQPrTqzdNrbxPUxR6_kU0GVwgk6VFiV02gTWDaXWhZURq9AS2JcXOng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7a9e27c8f.mp4?token=cNxhQLPZY8MAYQNe4bUa4FI8AXGjU48KguLxol6hYJnry046f3GV90mBzkYTNn-Bz0UwE1o8SkoMxTlDNCwY5pX5QFtiIMe99S5bsTmsy7ZlYSLLvc0fYo9LZNgKmifegW6kAyDM-iLsRI-j2OhN5PeEtcK4s3jFHs-U06PvJvgehSgGJ_tH85lEEcCXDfZNyJXjGBrql9QhyVIvU--qq9Gx_rawOgL2BtMq-1WdCq3y4y5DexmjOm5-0zTsFI1Ka5ci8sjjUan98dCt2lPDVDY2P_TAei2hQPrTqzdNrbxPUxR6_kU0GVwgk6VFiV02gTWDaXWhZURq9AS2JcXOng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
اگه قرار بود با مربی ایرانی بریم جام‌جهانی بنظر این قاب برای عموم مردم دیدنی‌تر بود...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/97595" target="_blank">📅 10:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97594">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIRAN ANKER</strong></div>
<div class="tg-text">.
☀️
هوا گرمه ؟
🔥
ما قیمت‌هارو
💲
خنک
🧊
کردیم...
🥳
جشنواره‌ی تابستانه‌ی ایران انکر شروع شد
🤩
برای دریافت لینک جشنواره به لینک زیر مراجعه کنید
.
.
🛍️
تمامی محصولات انکر در این جشنواره انقدر تخفیف خوردن که این گرمای تابستون رو خنک کنن برای شما
❄️
.
.
📍
فرصت جشنواره محدودِ ،
دیر نکنید که این قیمت‌ها حالا حالاها تکرار نمیشه...
👇
لینک ورود به جشنواره
🌐
اینستاگرام
🌐
@iran_anker
#anker
#soundcore
#جشنواره‌ی‌تابستانی
#ایران‌انکر</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/97594" target="_blank">📅 10:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97592">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P0jVkHCfNd7r56RQak8So5RlPMsnou4x2BkN59X1YY6w8225OezHpvMutYZvudD3Itfj7FOKEhK90-5vk_Jn5rqlngE6WH-sPBZPszL0e7lXphrE2i7xitqebuf2pgI9PZRkVVFNg6wrniHKIl-zOP5ztDGlQFcmgP1BhZ6Cd0Bwwh4J-dkLWc-QL7xv0VtgWYQNFXjNOFwCMjbiNHyWL1UNai2cim-IkcEr5hiRlC4RXlHIn26fY7672ql_DMvUQdsca0x-YbEvvs9zxZ0zAX2rFbGvOXtG8IwLQupXZ3dqRu4ABaxQP974J-N1Sg0DwqZcRi0YudLmxLecUbaHhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فابریزیو رومانو:
فلورنتینو پرز حسابی عاشق بازی مایکل اولیسه است و رئال مادرید هنوز هم دست از فکر کردن به جذبش برنداشته. توی باشگاه، خیلی‌ها اولیسه رو «خرید رؤیایی» می‌دونن. با این حال، فعلا بایرن مونیخ اصرار داره که نگهش داره و قراردادش رو تمدید کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/97592" target="_blank">📅 09:46 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97589">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YWfoKkOWuZrjVV722u43fC1PauvrzLsnNXG9JJ_9imXxWvKR3TG-1SNylGsuJs7WIFzdR4PC0wK3FCk4gNOk43CIHN_fkc1SkHv9Ogg080TYKebsqc66mHcX6meDlrw45SA04LeQO9IxGhiT95eymOfrWk0bvKqaFppjkaw41UvV0HnFOfqlaURgJXszxpq2pgFFqkV7e-s0DdkqdI66jZJKZMnAwvM3fIShhZ8w77a02wD5LcieiFreFnlWPcPnxugV6R_3XsfFHCpmOcpxZwZyZlagF3iVC-A4tfmsnM5k9ig6FIlGKvL75U8LtsdvtnQlsfGdRoBSnv-snEifdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E-Qqh91uVyJeFSKePbKL2rEy2RE1rSLowBnuL-2aAqAOyHacSfJlJ7m11AptbZ3CGKaLFbx8R_DEsH8yLNwv__FHuLDSedn_QTcD4pkYD5Xwc7k3_Np4Mn-Og2zS3IXuOilpONXLVTXWdbXy5OLJ5v5ZLZfXdSDkoBipH36w7IG9Alyq27pvicDjOMk5KtOEgBAYttpaPyn-mwK8UtHHIkxWYnuvViijuyWeQJ7CcQO2F_JRlLF9x_otPBVYLnVtdqfy4mTenobZMDkYp5tVSPMNAnGU5wbonUZU-7bzLxIdxRYy6cupEOqFPjg7WgtV3GI-kvmK9nkpr-lpHYGPHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eiidJeAKo45rHkHLaoucJlp88OKP7gE4Ax9fL01ydWqgwx5RLPGUqnR2ecYc-XmF2Z4tjVQl6RIIBVbMPPD32xptJSYkq2IuIP4JQzJ7fTUuRFM4-bMkiJ9pj559RRJcJTCm09HwJP4S6KqNKSqeJC2wSUHTfZhwwURwC1-LVl2Hki2U4iqO-CA4w7A8nP30wYgTvabhw8IsTlPL4IjweHYNn8_PPrXRffzRkkEIHu3vV8DkAPgNojqRVIO40Z_-1pNFbnlDh8epT8lKsxrd1kpEcqkIXsTBm3cAWl7cufx0k2P-x_n2lT5unIaGcGh2CPWKNZUPSpRiXZ8b7BXp_g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
تفریحات تابستونی خانم آلیشا لمن ستاره تیم‌ملی بانوان فوتبال سوئیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/97589" target="_blank">📅 09:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97588">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EyV3G6HOg_pafhSsl9-ss7QRM7A_nrvpR7njl93g20aW4ShmknfdSoYzOr6jo9HsvxEw0NQrt10tRvhPOceEK76ZA4AWOBPFapsqwJpFuRgd9FN20uHCfeCayibUXsxwzyYYK2pDRe4WEYhL7RpXsLDJZ6UqTm3i-eHE59MjfNVfvvHBCdtmmpypkN-sGNSa4CUu6bnl1O_pa0K6ElNzNeBMPVnFrIkdNMmAUTswSoPsr1G_5NpJoZBeWwJGcap_mLqmnGpVDzTKJd8aHv4B_JW9r_jcWTKNtfmT-hBPmO02rbMUMVG3bp7aElWBIFkOI2fegw-yT1moKr1PfM6UrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤣
چیزی که وینیسیوس از هالند میبینه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/97588" target="_blank">📅 09:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97587">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5cfa932c1.mp4?token=mKEe9MpyYOZ7oVPtmHGHIV6EtYxcRQMlZvyz1UQOGKvGC5W8puHV0g5M7sTlCoV42TAB0gYQEr-WzFZHM-tyCvWwcuuRn5MUHGuL_RTB2hDFxHmRLnbXYPVHy2apJrcEiuyaLi4pSL3BfK1Dm6xV4_5RAQlA79ivaSHuhwOcYXxAy8DROGjMLtLYOQz4AisXi70b3sNtuLZ0MbG2BHPFTytx1WgrXncFwTXz01fKP9IQf-YLNAe2_-pwy7LlnOoNWWnR1Q06nIZJdOToxnLyWeJRU89gUJcQRJnWOlI8FMGazl7Q5zw3DULx0GZymhLRqF_QadVxRJkdJtd19c5eIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5cfa932c1.mp4?token=mKEe9MpyYOZ7oVPtmHGHIV6EtYxcRQMlZvyz1UQOGKvGC5W8puHV0g5M7sTlCoV42TAB0gYQEr-WzFZHM-tyCvWwcuuRn5MUHGuL_RTB2hDFxHmRLnbXYPVHy2apJrcEiuyaLi4pSL3BfK1Dm6xV4_5RAQlA79ivaSHuhwOcYXxAy8DROGjMLtLYOQz4AisXi70b3sNtuLZ0MbG2BHPFTytx1WgrXncFwTXz01fKP9IQf-YLNAe2_-pwy7LlnOoNWWnR1Q06nIZJdOToxnLyWeJRU89gUJcQRJnWOlI8FMGazl7Q5zw3DULx0GZymhLRqF_QadVxRJkdJtd19c5eIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🙂
یادی‌کنیم از مصاحبه سمی سوشا مکانی با خبرنگار برنامه نود که فوق‌العاده وایرال شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/97587" target="_blank">📅 09:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97582">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rtRCotVu7N7MI4Vwv4auHzBfrmvuWgVvr4ZII444ZbGe0FkqZob8sXmYqV-pCcHZQQ1eUb7HnIsjF3-6gCqrwtuoiUqOjeFgeRNagSvzeSOYKlC21oNA42BGF0lEEg4IZkB00YXKYoYQK4D_Y9DHwZ_4vk9tYHZZAkek8Y-OIYH4K64d_ON126ZyaQnJKwT2HUeX8DSSVFJm7sqvQAXVgxvBm-j27Dwh9mStc2GB7e8wOz-ibHBtsSk9tGZY8hWkYEbQr_mYBhnFPXJcnAkP3Wnz4ZRRdAbT-E7RlB_Exz-BmGG8PvaWDCPjG4IkZGCuk3OverMDL0_MIdp8WSQOnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g563-JcpqZGF7LZDxNtRXnq3powAmHC4DFIWLZ6NYjFwfpAntzJuBO-LcCDKePwSnE27kr-WfYWh-wL25-RyH5wlmkeYMlxA6OXd6wozrh3zNsuJETZx00zp0f-eXhdaK284IggcrNBLIbzxLzfdWz3l2BMuy7tcLFZY8V7DBTU5Jg6lmo7ITyJZVRnMOb9sIT5dSHOsQeOV9uKEFYtk0Q6wPLu72cFeW0th7jjale70lMkMVC8vG5PYN-_onmp213QTMgt6z5csnkS7SgOyKgqljBxASV7ncnPgb6_x33DjBpcauGmDBi6z7iZLLonxvNmlcWPdyBMwxRQQ5Xj6rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uRKZ9dAioMTG6NVDZrAx-ISe7U00PYWtJzjFqetcVyPaaCyLOML8UYC5iOYJfiHybCazkp2EPA5hKI2FYzC5mb9UkZYiLxF4mLaM8ghLyzsNu9BqwE-ZLQhROriZ01NqI714nD85m5tGB6gpewwKB8LVx7GHRYmcFucSCGLZdxOtqSScPXOXsL_BA0iXb6cXP3Zw81IDlGB9tI6Q_jtQxm8AEZ1aZ7YHcbJzWqRAv3Kmqcb6P1f0w9Gew1CXqIm0tz_I8uah2kYKCDhn1zsZYem15H02vezPK_3Y95UaioU3FNfN3h86p25C70gkKFwETjw-I2Dil7AKlMUOYzxn-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rA_rQ8HqirnhnpgQlFebkfVjHcp8fqtUEJ_t5Ob1ngK6T3TfRWT2EvOuw1F1bgg13bS7pknXy0WltuKgtXo-hGQ4wTujZfA1Ndh71MsLdtdZjqJr054GbiWtqc3TxfjGgg_W3LWwIu-yREyHYR4TydZeVAouetzk74V36kJea3YwG_a9ZqFFejNWI8KXiiFyP6XC7t8naxn3tyksWiKbjRv5b8bUwVTV1OnBEBw3bslNXZAEIMc7LOWMtqfzLJZ6ONWbeLjMXAzCVnXrnCD6uxYaL8uyec33StAchMU_voU4aSs9OBxtqFSk3KLyPLvnJ8erQHh7iM_4gwIE3xZToA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j6qAhfYi_h5Qio8udArcL8cpXsitF8Tz6SI2cFTrAmRNQSkkGXTLeuKARhp1q1VHxV3jLLOy6KGSH1SbNBb0HkBgUfNWe0Jk5TwsAEhTt_Us1Skp-yUAfYSTaADGIEIXpvS01-KWNXhuFtlp07yxaAoDMnoE_pN4NB72h0YvvzXwIDS4wPnyDv-cttn647M_aNj-6BrRKzaW6OH7ImTeZlsF-O6srfB_hX8h-KcMOPufmtH1CzBr7m7xn2C0HUJp8fAyu9862Dlzcxo_76SYNOLpx56hP3I2SysjvBH4857NxAOkKg7vvl3X9Gy1Ze9x9bjkckL6fs1cbitRjnQYoQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
دیت‌ بازیکنای انگلیس با زیدیاشون بعد از حذف دکتر کنگو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/97582" target="_blank">📅 08:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97581">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af6bf8f214.mp4?token=T_eGVCAIPAeOi_VlF3s8qFXGX28TBwLMULP7V51sLH4fnvDuINMJLYzttgiyJWW_n4niSm0gYn8wv1iRIdhFJAu-2MGgUumbHABB7em1-F0jnD76Z80ef9hEbq5pEK0EyLaBLhnhi_Wn0Et3_MUg6nj_JT0l4iL1kX75eM0T5j_kb7kNmEkxHzaSLThLzaoFyc0iCi_YltYzb5vIR9AYzj4P_F3RgrzFSJnehiF-1KCvh6toR5PNJXLNKITvE98JwHs9GOmXJT7Min3frIQvr0x-zxKN-5aFaXRKDBAhh2C9ewSf9TErURab13ZiwYneI4DWT-1-5jVfp_-zT6xepQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af6bf8f214.mp4?token=T_eGVCAIPAeOi_VlF3s8qFXGX28TBwLMULP7V51sLH4fnvDuINMJLYzttgiyJWW_n4niSm0gYn8wv1iRIdhFJAu-2MGgUumbHABB7em1-F0jnD76Z80ef9hEbq5pEK0EyLaBLhnhi_Wn0Et3_MUg6nj_JT0l4iL1kX75eM0T5j_kb7kNmEkxHzaSLThLzaoFyc0iCi_YltYzb5vIR9AYzj4P_F3RgrzFSJnehiF-1KCvh6toR5PNJXLNKITvE98JwHs9GOmXJT7Min3frIQvr0x-zxKN-5aFaXRKDBAhh2C9ewSf9TErURab13ZiwYneI4DWT-1-5jVfp_-zT6xepQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👀
نعیمه نظام‌دوست: روی عابدزاده کراش داشتم.
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/97581" target="_blank">📅 08:16 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97580">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QwTvykv2jhjMmIS8fibkooLV3A5usQdlp_TZJSlBzVrJSC98NghVlKOxcKfRNt0x2-9WgRqrZOj4KBM4yX7sM5Z_x40A17FqVNBENBs_xa_zqTKPiyoacbNA_MV8TPUhe5gUtiQvd-bg9esRKVi4kmaI0Zj7nFAE8jD8ALb34QvcYlaRTsHeRsviSts_2m_HgdXX1AJ5XPq2FujL5Ct_-oh8u4YrrnKifPUumXZEJ9kgBEDVAHoEhzRK_4d-qHpCX-PtRrRTPngrlJKlQaBuM3C2DpGdQVkR9nIc1twjlkpN7pVj83IrYZTkB-0Oey3Lcb9fAEwEHT1lXklcpJCEug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
ادینسون کاوانی 39 ساله پس از 3 سال حضور تو بوکاجونیورز به صورت توافقی از این تیم جدا شد.
🔺
کاوانی از اون مدل مهاجم‌هایی که وقتی توی زمین بود، حتی اگه گل هم نمی‌زد، جوری برای توپ می‌جنگید که انگار آخرین بازی زندگیشه. از اونایی که دیگه نسلشون داره منقرض می‌شه؛ با تعصب، جنگنده و تموم‌کننده حرفه‌ای
🍸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/97580" target="_blank">📅 07:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97579">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eda3b086b1.mp4?token=Zvkos3rDyb86thJiffXXgoBdubfw_QLd5eiLYGfTvLhNNMIAxOXsHyZcDjBJh89xRONzvEX2u2-L-6bY9VbIZgtw0vRoyUBAqND58tcSy561iK_JedoSEgA5930fM41z-XhBv35wCh8A_porReS2T0qgMsIm-fbDlwm7cAkdyN7wjeV1wYw73uERPHx2znv61wkkTziow_eWX73KDseIVRDnLWfkNFQHpPL9zMQ3Jp4nWerKO1UPIvY8LPFbjEeuEqd_rhmoUmdKrvOAE1YYIbTlGzqhjql_jP21H7nUflDEiiWcoVcjNSPJpHXVkCGJJnydTDHZyhZF-kMFLN_Kqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eda3b086b1.mp4?token=Zvkos3rDyb86thJiffXXgoBdubfw_QLd5eiLYGfTvLhNNMIAxOXsHyZcDjBJh89xRONzvEX2u2-L-6bY9VbIZgtw0vRoyUBAqND58tcSy561iK_JedoSEgA5930fM41z-XhBv35wCh8A_porReS2T0qgMsIm-fbDlwm7cAkdyN7wjeV1wYw73uERPHx2znv61wkkTziow_eWX73KDseIVRDnLWfkNFQHpPL9zMQ3Jp4nWerKO1UPIvY8LPFbjEeuEqd_rhmoUmdKrvOAE1YYIbTlGzqhjql_jP21H7nUflDEiiWcoVcjNSPJpHXVkCGJJnydTDHZyhZF-kMFLN_Kqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این وسط فقط بدل رامین رضاییان رو کم داشتیم
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/97579" target="_blank">📅 07:11 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97578">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d15220e2e5.mp4?token=n0OhENZjGFZqYEWkXbNoE5_h-zDvsmusfPZTYRpSTZ6x1mNYQ0jXbcoe8Ng6XQcSJSPkbNZBEYjLjordLgXAkFD0U9Oj7auI14pSfM-QLzfF6RgfTVBV4KFFKMdpxG-Fjuq5E17-tQLgB1WcL2pYB74hXzbteSUbLxVmSgIxlCEvOgZ1J4L2cmEY1rHDIj1RUsYDs3rJsZS09OzO23JfQkN4254ngOkbc_AK2M-70GnakGnbSsLOTCPdj3n7XGO2YFUwvmq7xnM0nIINeTjH_fkx0S8-MO0TKxbqHvNwsdX51zeIYKNxyPXZofuVhu3hfFVAwEQUznDCc8WRW7p8zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d15220e2e5.mp4?token=n0OhENZjGFZqYEWkXbNoE5_h-zDvsmusfPZTYRpSTZ6x1mNYQ0jXbcoe8Ng6XQcSJSPkbNZBEYjLjordLgXAkFD0U9Oj7auI14pSfM-QLzfF6RgfTVBV4KFFKMdpxG-Fjuq5E17-tQLgB1WcL2pYB74hXzbteSUbLxVmSgIxlCEvOgZ1J4L2cmEY1rHDIj1RUsYDs3rJsZS09OzO23JfQkN4254ngOkbc_AK2M-70GnakGnbSsLOTCPdj3n7XGO2YFUwvmq7xnM0nIINeTjH_fkx0S8-MO0TKxbqHvNwsdX51zeIYKNxyPXZofuVhu3hfFVAwEQUznDCc8WRW7p8zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی میفهمی بعد این بازی باید اشک‌های رونالدو یا مودریچ رو برای خداحافظی از بازی‌های ملی ببینی
♟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/97578" target="_blank">📅 06:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97577">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZFPNKEDFJVuaZ6e8XiLCfFv4WMqfb8okuIe-zw2xCXX2Ix8gbxgak41IwsNUQUWu7bul2dQIURt7Tb4awW8f4w52Gnx771jYHDADfhEq-LzyfkNv7qYqSXKdyVzEOppukoApZFDIZlJkpNfP3T0tfXZWLH1OzHwYIoTcDX6Ezzj5Qk5zLyWkh3u7yFtt5bhsMCMyCBUiqAaJrxwcnXvDArL-HuB_PIgtmSpebHjUMIqUXNDhEo-et_FaCUx3Ft1MiSkmjQqbJSwL5LqoC4ZNBfopK3aLCSxyGI9xZqkT05NoPe6B2xQ_8hyDYxkgJEA8-1AjSTaVXDgAhKgomcGqww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🌎
تنها ۴ بازیکن در تاریخ جام جهانی در مراحل حذفی هم گل زده‌اند و هم در همان بازی اخراج شده‌اند:
🇺🇸
بالوگان (۲۰۲۶)
🇫🇷
زین‌الدین زیدان (۲۰۰۶)
🇧🇷
رونالدینیو (۲۰۰۲)
🇧🇷
گارینشا (۱۹۶۲)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/97577" target="_blank">📅 06:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97575">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GvyegtoQdJMXUZIhRQtf9NTIPMZfCTgJ5a50NY-r0SZbja5BhwqZ21_zxesD_zqzWO7rW87KTHLniFDbhdB3mtVEF-g_Rth_CsYxtSeg8qJGuVXRs2Icrvd7Q2jOaTQFbMbnBEfpzabjE7-kIa7QMI-Ckc8gtA8ZdQ5UOUCkoMJMxzeUCMD8wz_q5cj2EZclCAWTKFW0Bztn47RMjiTUYX5uXGOtJhsR92drJidHd2k46KvwPa_kFNs3J3f1GBEMP4Pv0irXf9wmDpMRR4xucXwQqtAD2I3gTY6q1Lc4GvI0_9zCKNM6_pfKdCDpbDGCD8fUq7TAU-zB4TcNqcb04w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DBg41GcR24PhUfMjYj2rEPWn1G_IAGl2tbZo3KzUKbMGmhUznMtYEWBTDZz1PLO96_wH6dE9gisgHfpvhIYowsggZ7rP1U1Q4gfuUmdDKeXOEe2T-hFxLlVj-6w0WlG9PLDHMGqp9ieRSOARfaQjfU1GQGOMwvmbSALkhEJOJTCdvRoi-xISffJ5htsPRmRM1QccL53qPQmQgQxMOiPuCsU-r0pvpV68KlDB8zPEVVOWxF6NqxO66sEbo1tSiICQYlAwK1fAfaWysPBnGljrQrH4PeUKSE77I9sL-DHXCo209BSxJ-aj7kHpauScdl-8ZDdkGxVhCzBbjlZWCDmoCA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🔺
پاپه گی در اینستاگرام:
🟢
بعداً درباره دلایل حذف صحبت خواهم کرد. اما امروز اعلام می‌کنم تا زمانی که این کادر فنی در سنگال باشد دیگر در تیم ملی بازی نمیکنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/97575" target="_blank">📅 06:08 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97574">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jviyEJEc1VEJjvhEW8JUn76isupUY5Tmf4o7K-a5MISKNGdIBlrOv4uDvMU_cUqt3pdo0axCtsyACJe5M6jAgv-7R1QNCWHYWize-sa2ohHnpMxshY6p165yx_Oor3Fp4--Rtf7idQUCsnQubrhWRBUPFIWshWrMxtQbeR_zzzKqP7-FltwX1VaTD7eXTT4aimmnX70J6fsPYWfNuxfSDFqjhLLSfOvwRhsLiQITq4C44BP35dofE5Qyra5lS7cMJtuv6sYHN3tSDKRzOpDTy6bDhWWgXCUlyDFtARSB_poqM5rccOp3VzO4u3BVhXSWWtokh2ONhTKI_Z_ixzQQPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
آپدیت نمودار درختی مراحل‌حذفی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/97574" target="_blank">📅 05:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97573">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dLc7XIGIbWRBk1HnkO_26lJrOCAG2aggGC98c0eHswPr8ZMdyAZYLgm7FlnmIJxOmgl4QjhzeZzr3LGCx8KWa0yo6F7RuEj7Q_sHq1Fcm5rGjq0x2tLUGKskr15llsGg2lePT8uV_ZE1DwaC4dbMRG0JSm8AWOBohJakN7Tfn7cqCCPXYAugdCNsYn9HmSFtCuUWc8v8wbROIZU-zWe8p5PAboC-EhJ__h__udzJvYaFm49dIkmYgDnLr5TeYinbo2pfg2Jr6FaUPBy8pNMG8uMm53IzNdCcwK5Ec0rERAtijXZyxVqVy1QHI36cnNLzWpiU4Z7DQbcMYG-eYxMjgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
مرحله‌ ⅛نهایی جام‌جهانی فوتبال:
🇧🇪
بلژیک
🆚
آمریکا
🇺🇸
🗓
سه‌شنبه 16 تیر ساعت 03:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/97573" target="_blank">📅 05:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97572">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RdjA3nzmQDgd9UMWr78To0WaYZnl377jR3SdXcQ7463NeOHOzT39WqQFQPmWmf_nDb_rVDO9Ff0zmpAbasxFK9SAgNhujT7ZtkM70t0A_7zgBsYaCBbPZixD0eRBXg6jate-dQlhbJpglZbOXxOaxzebDzkVDPdT6HZlIXmP3n10Me3waEwXRyBeNVnUKVkpAvDrxflCDY4t7CsRECGbLJCFX4b9QmDH8RkeLiiVAFr5yvIyg9R3LUFc5xVYTq46_MGd-hd8oBm8rWKznKKkGBCGFIhjJhK6sbX1Fwfg_rRv5bokxIttoJGdl59Cbc6kAhfovfESkazmGG2rV2Oyvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | پوچ بدون بالوگان در یک‌هشتم به بلژیک رسید؛ ژکو و یارانش به خانه برگشتند.
🇺🇸
آمریکا 2 -
🇧🇦
بوسنی 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/97572" target="_blank">📅 05:39 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97571">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vxfqarRmFVh-Ue1O6-7GjValk-bYDNdqiouV4PVhUgAU0PHfw_hJstSlI7Y1mm5NAXvOcauP0zKjo-9dRNBAX8pybF_Gbfkx9WVN6DgD0EgacKe-BQuvwZhqWNSPrLnl92V7hXjBukLadzv3_GTKsaeW3btscEzKLptM3JeG71pDl938RapUwmEBbmyIwXKnxmXjSK3HSJAoxZuTOYSNJc0SGfbdtx_es_PuxwFVOtO-GeeDPSLADd5brE_AKfN69g3pVH9kEby22FaePa4RROJnJYOh2CbYDy8ojzIfgBgYTENSVWe7SEiPByuosw6ln_I-k48XexE2D1kPTCjdDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
#رسمیییییی
؛ آمریکا راهی مرحله یک‌هشتم نهایی جام‌جهانی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/97571" target="_blank">📅 05:37 · 11 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
