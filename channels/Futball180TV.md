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
<p>@Futball180TV • 👥 659K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-11 15:33:43</div>
<hr>

<div class="tg-post" id="msg-97629">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/Futball180TV/97629" target="_blank">📅 15:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97628">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c29cb7614f.mp4?token=cX_OjZNU6P-V9e06CFMSKpVinMEg2Wu7JxuXGi88ZZI-SdN432bodnToNaNfo_AdD9IHB9xxFHe7a2nSQlF4Deg6xkCK5lJKLhDP859WU9uVAdOUVjs05Hy0rVccvSoXyhTUooWIpS3FtIEPbyhI50AJzBRfDjbnpuoOW_r9apNygBcsu5mN8o0Oe8Bv55_V7-hGwTJNXR97WWJaGJSxlf8s9sT6MuGISOJJafjgQNZpkbR0POMEszIfu4v1xOnhUALj1HsM-_h-f3k6vTEa6VwYRfZcCVC4HMtj1qFDBYOTcBCPv7KFLSs7IsZYFysgs_90dcA4VZT8BNS0hB2VJSRMSb9NPvNeV9D6XfhZyaXAcfJHemJPBrN9DiNUnwEs3rLbuXmLhl4zfCgxaOeeSf1bnVaFMDahRsmHYlQ-Umi7tQu7lQYWVRsBMSVlRA9PHWFNA_LcRsl20H7AueGENZNdShMwjz3nfUT2bgLdbqLH4oAgg1h5oqI1-XIoAEEZoxzVP7GzteZMkUvtvZW7JG_tTsn-t8XOY9ivLtVVKfUmV490KRqggmOVb5kvPNgnw9TkWS6frVj2li6fx8wiag4JbM71ujxR4O2Z2mVGRpB5DOcwuuSUQiG_d7aHotkP3lyQwqblGAhGRjQg-PZnuKKbv3wpQpm1quZ6qyJO0vM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c29cb7614f.mp4?token=cX_OjZNU6P-V9e06CFMSKpVinMEg2Wu7JxuXGi88ZZI-SdN432bodnToNaNfo_AdD9IHB9xxFHe7a2nSQlF4Deg6xkCK5lJKLhDP859WU9uVAdOUVjs05Hy0rVccvSoXyhTUooWIpS3FtIEPbyhI50AJzBRfDjbnpuoOW_r9apNygBcsu5mN8o0Oe8Bv55_V7-hGwTJNXR97WWJaGJSxlf8s9sT6MuGISOJJafjgQNZpkbR0POMEszIfu4v1xOnhUALj1HsM-_h-f3k6vTEa6VwYRfZcCVC4HMtj1qFDBYOTcBCPv7KFLSs7IsZYFysgs_90dcA4VZT8BNS0hB2VJSRMSb9NPvNeV9D6XfhZyaXAcfJHemJPBrN9DiNUnwEs3rLbuXmLhl4zfCgxaOeeSf1bnVaFMDahRsmHYlQ-Umi7tQu7lQYWVRsBMSVlRA9PHWFNA_LcRsl20H7AueGENZNdShMwjz3nfUT2bgLdbqLH4oAgg1h5oqI1-XIoAEEZoxzVP7GzteZMkUvtvZW7JG_tTsn-t8XOY9ivLtVVKfUmV490KRqggmOVb5kvPNgnw9TkWS6frVj2li6fx8wiag4JbM71ujxR4O2Z2mVGRpB5DOcwuuSUQiG_d7aHotkP3lyQwqblGAhGRjQg-PZnuKKbv3wpQpm1quZ6qyJO0vM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😐
جیمی‌جامپ‌های بازی دیشب از این‌زاویه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/Futball180TV/97628" target="_blank">📅 15:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97627">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6859ad42ee.mp4?token=NI9tJynsSvfkNF3I8DcbbRNPYj3LAAogrJcWI8mZp37M1ZRHrR2E9COSv-9Xd9KNYVi91kbOn474vYpxdDJHx7lhR-OcYtHj-lfVSICRemmCDPjC0YCZJ-JM5Q6bZxQZ1LSV8Vd3KUHbgIm9FoPNTk69iMGC898_CWn2G4od6P-yM41Fv8tTreeogAItOLsmBl3UQYFVsanwoBerI9jKbFWyjArSJixZ2AtXF5bATRuWkGyIt6-brq4JchgYrGQeHtWL7jmfAU7IXInlA2kkT0Tl9kUh3xQ5d4akg2EyjflLd-YhHZq8BxiQWqIskHaFp9eXgUeO2xX_Kzm4K5Dgew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6859ad42ee.mp4?token=NI9tJynsSvfkNF3I8DcbbRNPYj3LAAogrJcWI8mZp37M1ZRHrR2E9COSv-9Xd9KNYVi91kbOn474vYpxdDJHx7lhR-OcYtHj-lfVSICRemmCDPjC0YCZJ-JM5Q6bZxQZ1LSV8Vd3KUHbgIm9FoPNTk69iMGC898_CWn2G4od6P-yM41Fv8tTreeogAItOLsmBl3UQYFVsanwoBerI9jKbFWyjArSJixZ2AtXF5bATRuWkGyIt6-brq4JchgYrGQeHtWL7jmfAU7IXInlA2kkT0Tl9kUh3xQ5d4akg2EyjflLd-YhHZq8BxiQWqIskHaFp9eXgUeO2xX_Kzm4K5Dgew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ژکو داشت مصاحبه میکرد که اونور زیادی سر و صدا میکردن یهو برگشت گفت هیس همه ساکت شدن
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/Futball180TV/97627" target="_blank">📅 14:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97626">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMoris News</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cAlTaJ_QN280UjpuRAXsezSmtHE8E1jTLa88PAu2zk1Cd4zJns_HeNjOy5dhpUHyCjDf8hH7RX_hrtg--SKM85zfevf3N_SBh-QVF1g__Liz7uW26l4RQoARI9dMMad9XhuYp_tJkJGmvnPOGqbBNLTBj6UM5UiB2mcpn-FgpR0cIqJe57T1xGVPvd4n0YMHSJgnxkQ_IxqUqkBahzk2hZZ07_Z2mBG50mDSrgJvxZdR1Rjewq3-u8qwSDqodF6tZJXLXy4RDuRBT1zvOe7TCHO6xP-qTDz8FnAOQd9bJ1Z3gVaYvFg2V5JRRCGRfJ3mF_V8NAr_X4TOhNpKiZ69_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه جدید یک دوست عزیز و هنرمند که احتیاج به حمایت داره
از دوستان خواهش میکنیم با فالو کردن و شر از این دوستمون حمایت کنید.
@egyptinpersian
در اینستگرام</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/Futball180TV/97626" target="_blank">📅 14:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97625">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/Futball180TV/97625" target="_blank">📅 14:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97624">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/97624" target="_blank">📅 14:30 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97623">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6470fe1aae.mp4?token=TzLMrOi22wASZb_a0yBa8IY_zZjqLATcYy6056VTuLtYbOq71iHgW6p9Rd9Yq0aOz6FV65x5pq0Z2Z88Eu2sRQtAN5NG355dWWL7lEabC4q9HMtn003vcFcKguLriDqaEOlXfV6vg2vNscRmo1llYPYd8s3Tm5l21Tb72wyBap_B4UduWW32VUNMAPdt2FjAghYP1cTBc3V1vVdNw0PNBeKeKhCg_6nuC5DgpFgjaU62DHUmmiFXzO1DjOLnaVgYagdoSGUqLi58aPNMC3sXdat6I1SdITpaw9Qt87leFAYsYwLvcdD7bqjWsTx_qFqmiLbdsn2LJNzVamWkX8xjdlci-0IN7rdpv_yWUD5af8NuHC0eeTCgOxJ4YEi1nOWHChfr9OeVUZ6LePfAgIxRM_iZYkAqpVwdIG27V9q9CV-LLeMFTDAkjQOTGmXmrQxr7jxinH1wascxn9ANHMKzcZNSuooLRPOlCLUqZXpGklc4MQoW0afxzuyUC2uIFe325uhertJPCRzck4MDdAn2tcohPRW0U4nW-DIiJwNZoqfGslh57YfP6SIah7JqPUDtem3hmKosrhUK0vzg4UkF0lTry6brQ3UGGACYmq6Sau4uQg8kiQwKZk5G7AlEV9ca1RSj65qfZFOPrvuWDZS95mKQgEBLhYLG5WkM1dOFwP8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6470fe1aae.mp4?token=TzLMrOi22wASZb_a0yBa8IY_zZjqLATcYy6056VTuLtYbOq71iHgW6p9Rd9Yq0aOz6FV65x5pq0Z2Z88Eu2sRQtAN5NG355dWWL7lEabC4q9HMtn003vcFcKguLriDqaEOlXfV6vg2vNscRmo1llYPYd8s3Tm5l21Tb72wyBap_B4UduWW32VUNMAPdt2FjAghYP1cTBc3V1vVdNw0PNBeKeKhCg_6nuC5DgpFgjaU62DHUmmiFXzO1DjOLnaVgYagdoSGUqLi58aPNMC3sXdat6I1SdITpaw9Qt87leFAYsYwLvcdD7bqjWsTx_qFqmiLbdsn2LJNzVamWkX8xjdlci-0IN7rdpv_yWUD5af8NuHC0eeTCgOxJ4YEi1nOWHChfr9OeVUZ6LePfAgIxRM_iZYkAqpVwdIG27V9q9CV-LLeMFTDAkjQOTGmXmrQxr7jxinH1wascxn9ANHMKzcZNSuooLRPOlCLUqZXpGklc4MQoW0afxzuyUC2uIFe325uhertJPCRzck4MDdAn2tcohPRW0U4nW-DIiJwNZoqfGslh57YfP6SIah7JqPUDtem3hmKosrhUK0vzg4UkF0lTry6brQ3UGGACYmq6Sau4uQg8kiQwKZk5G7AlEV9ca1RSj65qfZFOPrvuWDZS95mKQgEBLhYLG5WkM1dOFwP8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تمجیدهای زلاتان و مورینیو از ایران فیک بود؟
‌
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/97623" target="_blank">📅 14:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97622">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/un7ldE6mFKyG6hwiiYLLWs4twH3mnBh5zx1p3xWbl7HwHIbxaNOSDNc8r914DuRNNOFa8-PsFBTb018M043lQtYOfOC4eC546r5Nmak-stxz9Dx8TyA4dzgk5b-ThUx4AtGyr-srfeMpBss4b4kXf4TCf4KFJTD3INFi8fEAho7kt8SjyCP0ng8YN28q9_ees1rIZhfQEgwF67P158zl0I-fJvbWztWvej7yD0wAkPuOlrEG_vvWt2Ej-e020F1zo0bDmZ5l1dKj12ok0UuLUe29a7fQtoKL7S2DBabJyKRTR2vs_tDygF7THME2LFtCyApc8i1lkbQLdYj-3kkznQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇳🇱
#فوووووری
؛ ترشتگن با عقد قراردادی به تیم فوتبال آژاکس‌پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/97622" target="_blank">📅 14:18 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97621">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fl0sQXYgrPaV71T2132nZeEhIiQv_l6lzpx2k3s3JZqzg3dQ81dnQ_pbyCn_h5OM9a5X4-Peoh29HVwozEgKkua0mR-8NBlIiL7NBZiRl9cpLujX97vCaJZ3VXDleqRA560RoyHP7Ysk-d0n8BIgDI-QEGrRxa7ta2901Hon1xoI4bK7Dn5SdNX9ID0ygRX5PXbsKbT78u6pPcQtA6tKRBQdub591pV-4x_RqWEwykQLRz4pBhM97TL3KtdFOSFK5tjbEsADUisidkZ4jANRATgpcT1rmxoS00pLTLsfq2wCWtXYEYHQ3orNG-Zvfhd16MwH_ps698hEaUZQ22zFeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
#فوووووری #اختصاصی_فوتبال‌180
🔴
با تصمیم نهادهای امنیتی و توصیه به ارکان فدراسیون فوتبال، امیر قلعه‌نویی با توجه به فعالیت‌های اخیر در دو سه ماه گذشته، روی نیمکت تیم‌ملی برای جام ملت‌های آسیا خواهد بود و خبری از تغییر سرمربی نیست. این موضوع پس از حذف ایران…</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/97621" target="_blank">📅 14:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97620">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/97620" target="_blank">📅 14:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97619">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/97619" target="_blank">📅 14:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97618">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FJ6pK0I_kW21hWcCjMnywzd7vEw7RL9E3WW_PT7SLHk0Dsv2cg-s3O7frpkLls5xfbAEd0tWy1Y4AqpwYpPJEd7lxdffhGkLrEnZEncME3Ya2_cvH-7sCBLeeKR8-rtaNTi9Lrx5qO5otXsZgWQNySemJdMmAI9YqP3xkftxHNQp18Sy-atT9UuhoWEMaWB2yVJnWqq6kOfFFsR37Lco87drBRP2xOAXxEx8pqW-Y4lQ16DX5dO2haEDKLI_OLWIwPfxyTdu80KLVICIGTY1d-FKUHSasIBP9Rv9LYpEThl1fkYctW1f_eYLCh_g3XMPt7a4yeN58Iz0O-5eRPWHIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سانتی کازورلا از فوتبال خداحافظی کرد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/97618" target="_blank">📅 13:44 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97617">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/afhn1ffJ9ZPn1w2JVvP3TcoSy2ieN8s7Gs0Y_PZSnQI742BciQsb6yZguEwHX3HMwFaCUB2GYWPNaKfrdE4yKmBtQHgMWcJLG-AzPA2cr4rIhmru69LEH3uAO3OdhaTtF9K4wpARDjFENl4pJB2_rO0PqrqF5BAt8FQEmGVsccgCuQUubFeMf2Y2SQsW4AfiKjLlYbfV4gFe7dVuZ1idX-QywDvwsc5ab25on0FPS3HkVGNKqDHQV98xJK5C1HaQXCQjjnMFTCA_36wd35Thsb8s8TSD9BYlQxXpF5VzvsMfRIXDVU-GfgfqU2UI8Wrl2hguoy3um9lShyry2bxiLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇽
🔥
مکزیکی‌های جذاب در حاشیه جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/97617" target="_blank">📅 13:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97616">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5e7dc94b5.mp4?token=jCuOzxmc43Szg-dXCwuUdVltI5EzOpUeAPp1J0Nh4q9tyTp5qBZuJn1krnV98sMhqdSqd2JzWd4d7HjGGsxpyri3gPoLMTm_J84UR-wK97CaIH30OG8E3MCAfRL9oHrU9AJoZSdnlXx5BPtNkq1gL8h7HneM-BEowAtHg_xJQrZDxLzrygKp6HgEqsyi4vFAkHWHsnD-KwgeVWEWKWyXLTpgbzGmYuzsWesKj6ESXuW6vbrF-ihvwqIW0VyKNOZ9XSYMYYF8XCPhTcM5_UsYwCwUHd7LrTWBYiqkQGKfNT36il-zh8L9Yn0McYWzYpDSmDzUgBqabqtB1NASPMMKCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5e7dc94b5.mp4?token=jCuOzxmc43Szg-dXCwuUdVltI5EzOpUeAPp1J0Nh4q9tyTp5qBZuJn1krnV98sMhqdSqd2JzWd4d7HjGGsxpyri3gPoLMTm_J84UR-wK97CaIH30OG8E3MCAfRL9oHrU9AJoZSdnlXx5BPtNkq1gL8h7HneM-BEowAtHg_xJQrZDxLzrygKp6HgEqsyi4vFAkHWHsnD-KwgeVWEWKWyXLTpgbzGmYuzsWesKj6ESXuW6vbrF-ihvwqIW0VyKNOZ9XSYMYYF8XCPhTcM5_UsYwCwUHd7LrTWBYiqkQGKfNT36il-zh8L9Yn0McYWzYpDSmDzUgBqabqtB1NASPMMKCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
ما تو ایران چه کار خوبی کردیم؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/97616" target="_blank">📅 13:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97615">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KjdUZEE24Nod2R8H3pI1GDE38MadHzn31SL5uhXarwmq02ZgKPR9Reb5_NdFu5Wg1WFs_Le8v3r0BHY2lYjOLyz9eTyRDIsYEKq4Jf-_bcG1hm5ADMGU1dKQqSGP6JmuHXd8LGYxCZAoknx13OYdAM410JJFJdCx1DZQc3nDfuvbgW1XT3Hlq0hvHoSlpky3dHdWZ4UzA0XU_SSahM8lrpM_2_W0NpdNTMXKl2EHyrBdkF_yQsJA3wUT5F8e-q8xgA4adjijqT3waNFCPgUQZsqD5J1OenWBD4TPeKsOKXX_WtkSrzBoPrPy97VCTgL3DhsXMhz4OmuSEtoX4RTusg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
از حواشی بازی مکزیک و اکوادور
🤣
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/97615" target="_blank">📅 13:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97614">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A6oLOy9QlxQPwhyUOOIikkdfVlKSexav1BgRp8442eykpqq_mRxhkYiW3XkG-hF-T6sIUZ8hx7aNPyRu7PZmxa0UTUn31rAWeSTCdVm0wICDY3zv0uUEgpLOCn4_dM5SgZHZcJ9nrJ2Pr8cLJBTZoNujST6Kd7oDVL61wbOT1txCv7Oerm4OsZfZFJpepAjwlI6xirRxbWE-wOO76XOStFYtRdFkD3fzTD8T1pN27-3XABawnYULtD_TBe8Nwb9zT8TrAjbXBXBVV8eVB0xuYV0jQ6y694fKeaRHyql20gtrNi-pCvs0B85MNbvdCeHn25k6mVs6XQ7cb43-uuXK4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
فرناندز تو تاتنهام شماره 18 رو میپوشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/97614" target="_blank">📅 12:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97613">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/97613" target="_blank">📅 12:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97612">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/97612" target="_blank">📅 12:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97611">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pxhxRzSxeg_-ee65Xy3IhVuktsJFSCMe6psR7Y5Ou81dd4sf5CckOkamb5glRbn-zdYcY226Yl3NQG00EZt0Yn1J7Je8xXBm28tLQORfCSoENzbPQ8Cida929TR0ATskSia0P-2_Xie-pM3tkGYYD5gLzVFolOH2hd-YTpfOjesB-5ag6NWXq2qjohkQ2COyj8g1-Bq8rAxIrNbjt7XYvjkFRU8j2B-0Sva9KSCokXzrBvy7cXwibNwPZZB4uKtJRo2tFy_sJoLma62qz2lbL1dPMiipritDkTMlEQXRVS1MbXlRW1Odm2hZs8MN-RPiWvWwgfLJDNKiiMugs6Ct7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
#فووری فابریزیو رومانو: متئوس فرناندز به تاتنهام؛ !HERE WE GO
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/97611" target="_blank">📅 12:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97610">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EERB2GcefyKp6FlC3uZXb1fs50wdGy5MZOm8WvCWu5Rlpp_6Gwx0sLMoh2CcBZQpKdTo2FtFkHbgu_ayOx9Pyxf0_0BK0xgokuBGr6FcPHtD4z-uqFJDcPqNBwnU_GK9eeBbeDyyfC7CN8nQHsU20EqEtzdqssLJyby8mBrCtyh_x3aVgySXGbe3UJ9S7OVbRXAz2h9A88dO81ZPmNQaDpJwtMwCrzZiYuXSs_IodEnW57VQV5m0aKnQvxEBAxPx4CJEOAhdU3tgiLsrEoklHMlFRdMya4jJjb1uCee_f0evJtlLjHngjfNbJwL33jll3q9GJswJKeMCk7l8i1y0Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از باخت کنگو جلوی  انگلیس، سباستین دزابره، سرمربی تیم ملی کنگو متوجه شده که پدرش حین بازی با انگلیس فوت کرده و از دنیا رفته
😭
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/97610" target="_blank">📅 12:26 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97609">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oKfuEcfRK_sbemuYNxKsw6em3OHIfN4wTwlVY-UKXpUBDMDLjHLjMguXbOudzwe7HWjA-nprUNrY-BtgiEGAF7tKiumigduVVpBIBI4YhzvlEsu665ViO5X7R8vzJVRgJEk_izauiOtLJgQedUMvAzvi6ZUF4jHUIeqNH-7ROVT90OrRYeiIilbuqcBkuBpjPqGFBoCCNajmKYFZqzwDaGEsak0WThODaK7OQqs6R04oxK7i-CgLTJHo0mBC-R40TMbcz5RYAiK7e_YUIZB3sWM1iK_9AK-nVi9YkDNvwSXtKcDysewUDcakYFvCd_30zCRe1qZkBxs9pwB8Vh4qjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤣
🔥
کار درست مثل گاوی که بین خواهرش و زیدش رفاقت به راه انداخته تا زندگیش بگا نره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/97609" target="_blank">📅 12:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97608">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/97608" target="_blank">📅 11:58 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97607">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🔵
#اختصاصی_فوتبال‌180 #فوری
🔵
باشگاه استقلال با چندین ستاره‌جوان لیگ‌برتری به توافق نهایی رسیده اما تا باز شدن پنجره نقل‌وانتقالات آبی‌پوشان، هیچ امضای قرارداد رسمی صورت نخواهد گرفت. هرچند شانس بازشدن پنجره استقلال کم است اما پیگیری‌های وکلای خارجی این باشگاه…</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/97607" target="_blank">📅 11:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97606">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/97606" target="_blank">📅 11:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97605">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/inUskAadUWU2F63VQaod6tIYwET8KnQvxg3v0ynHYfnIWTvPPM_lfSnsWzqQa8joTXfBS7RKK_dvBTZNbgTyZriVbIfLlp6XcGl1PCupUT4rvJmAq_sYja4_pVpd-WviL317_n-nQxtZhn9RFN4gZPfrTGxGcBVXrIuexJlqEiNBsH4XESpJMfKs6ZvH92_hso2HG25bTX_x1MKmUHNcnBan8b-xX2FFBcpONlUbAH7fC46CW13L0DdSUjx5NpdFm8QtZM9A0-HEGbWmN3LzJS2U55PhPXEHNDkD4PjdV494rZ3opLkqnpJcepNiuOK4raUkYU_nf8hiYvGe-nJdWg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/97605" target="_blank">📅 11:31 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97604">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/97604" target="_blank">📅 11:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97603">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hlbi8uLGO4M-G-NRkAxtITofN1qUPZ38vIx_gDaNeKgFL80uteW4nv_nN1sh-Iryn3qtoSVpGO3AaD-dzJzGoDuvGzojWSkFDW3hQDEDbWDOPh_Ho2HnM2Jj58H0yC1KeFeXfCMO0lGiludjQ0S5NmbEv-VHZIfoYOKUukUOZjvsk1bmuOo5jUxy2utveA8K-rlssiiERpxdqG__zxPS9SKSzMcVqWCRiDCD1e82H4vRPfc5BGJY4JjFkOj3iLzqZDOxQD2hldBFH5OcSRPyCPl_JeTgYL2HE78y3Z6fN13LrxbYOKHV0XkrLf719wml5UIyFz3wlQ61MSFgn5bHZw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/97603" target="_blank">📅 11:15 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97602">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ed83a057c.mp4?token=WbktLwXf0kDZrrlPhViXIjgo1CS7WPffLwJF0C6UQGM6Cra2MNoUQ611a23i1JnUu4p0QvMqAGtywWKDRazeKH65slKRaNniSn0qu23_wckS8d0zNJX3FplK-Hayv9qTTM2_l6QTRAKEMrGh3P4Qx7CTPiM-DC20UrjrzSpR-6RtLT_t2n3xVuPA_VIGdnlMzpVKB3et2f586Aa9eTqIWCewGjp5AvURxsElVFnQ5SvnXElTFmMoSdDUSVH9GRqR6LkPLssXnpBc415ERvpt--Y3LslDb1JNcGQFOjBWA0nTP1u6_tFcL_EjLkfXdNoAvcjQjsDwHD0nL2w3cdQTbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ed83a057c.mp4?token=WbktLwXf0kDZrrlPhViXIjgo1CS7WPffLwJF0C6UQGM6Cra2MNoUQ611a23i1JnUu4p0QvMqAGtywWKDRazeKH65slKRaNniSn0qu23_wckS8d0zNJX3FplK-Hayv9qTTM2_l6QTRAKEMrGh3P4Qx7CTPiM-DC20UrjrzSpR-6RtLT_t2n3xVuPA_VIGdnlMzpVKB3et2f586Aa9eTqIWCewGjp5AvURxsElVFnQ5SvnXElTFmMoSdDUSVH9GRqR6LkPLssXnpBc415ERvpt--Y3LslDb1JNcGQFOjBWA0nTP1u6_tFcL_EjLkfXdNoAvcjQjsDwHD0nL2w3cdQTbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇧🇷
🇳🇴
اینبار تقابل دیدنی گابریل و هالند در سطح ملی و بازی حساس برزیل
🆚
نروژ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/97602" target="_blank">📅 11:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97601">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">لحظه ورود تیم ملی آرژانتین به میامی
تفتیش بدنی مسی و در ادامه خنده هاش
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/97601" target="_blank">📅 11:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97600">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🗞
رومانو: فلورنتینو پرز برای تکمیل معامله اولیسه دست به هرکاری خواهد زد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/97600" target="_blank">📅 10:53 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97599">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F-ENb7dqBRbeXgIeR9ryCKzNzMoTKFsXp7xGs7zh-oXBzzkKotH7ajI95K9MfTYIu9CXcGKlSnfK-O37c40bg8HCdQhi15BAe_ojws3VGezUqSY0fXUI2LB95088SnfdKOO8t3CRe41NrK-YuQRKNyeGNnZmAZT2mCV2CxHcxzO921QS-esb_JoXQGr-MFIc5kP0kvWMh0wFckuOlQUcvgL20vdEj_yLkMPeq9UbOc7ykPlSJeVUuwBXaSytAOVwU7TG2VEBu0wTkaVtdTQtxxQKASy2naPehAk3TG-mnG6rLb-SXsky8P3GpZb-fVDUddNt4zEqnWBTLmyGZrOaew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
⁉️
🔥
#فووووری خوزه فلیکس دیاز: رئال‌ مادرید و یک تیم دیگر با نمایندگان مایکل اولیسه درحال مذاکره هستند. کهکشانی‌ها با توافق نزدیک‌ترند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/97599" target="_blank">📅 10:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97598">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kjoUyVCSskct-WGhgiIbkeqDIlbZTDynXugRC--pkWy2U-sEZ8KFfKNPFLUulxUCeHTBFLtgg69rVDH8JreoUAVPMUUS_Fg1Bn7D8MQwmDksoBZX9krbPRnHQfC16yw5q0yuLqXfYbn-ZOyvKmgWK9N9Wwa9-DQID-JUFiik0Alv_xM-UPnGFI_Hxxlmmc4ItR382n6FX8YLxlImTIlCcSNov8THDm7ygw2KnsDAmFFldjgnz6Oz0jSqliAw7zOf70SbZ2hNkbgpxGc7d-KTfteTdRG1uj64G_GqJsyZKaMIFliRwYsftdXHRtiZzbgovg641SV3KC2wXzQVxw7jyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
⁉️
🔥
#فووووری
خوزه فلیکس دیاز: رئال‌ مادرید و یک تیم دیگر با نمایندگان مایکل اولیسه درحال مذاکره هستند. کهکشانی‌ها با توافق نزدیک‌ترند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/97598" target="_blank">📅 10:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97597">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v6s3lHRyXc18kprgLT1TwLuo7BWFWSIVpqLhG8kQ9RrTRLdil2xBbHhhkXGqmCCalfCiKI50LrMw2Te9SLBycavZeLKzchyhyV87p-X8uNGCarFM2JjCgtoCHfBqmU7ilClbUn-bGm1zZTrNiCd5Uj03sfLLwWJqxJb75R2D7vSdk1XpZpUnaAv108lcG2IXuNubH7PIx6wmdO52T2i5kqCdPpEjDZnKYCPUJa5OgSnAykuhDUWSx5Q4m7eM49fwQRjbLTrkusVp2XPBMNx1hgvaCTpyEodsLwjF0o93wZCN88ro6RpqC5csAKXBInMCPlYrd4fY6wQlP_1jLHJO7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فووووری؛ ساندرو تونالی با رد پیشنهاد هنگفت منچسترسیتی در آستانه عقد قرارداد با تاتنهام قرار دارد و بزودی رسمی خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/97597" target="_blank">📅 10:25 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97596">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aec355d42.mp4?token=dQL23vUMOY4Qru98CiGis6oSPFhMKxX4TYPPiTDIV3Wbh11hrY4MtHNTm7s5lYRX0gfKoesyT8Iom2gf1LajjJmgI_rgTJ9qAvnKA25mEoy1x0pn3HivpJDFZpPvTjt6kqudu8FslelzvkkjDGayciAt5a_StnnpYBeRiNwi3VfqD5PU2mVZfjX7QYsZiPwkTysU7JVVT_htEKLg3WSiJUZI3Uk4GyPwbR-2aQzDxBzx-2dVSe95cuDG7WQxqgb_VjtBoGTTOSUfzdyruIcoSMhC75_lD6Bw26yMFomDLfmqkqS8QQI7K6HXCttd_-1pN8bLG5GrIIZuo4DY5R__6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aec355d42.mp4?token=dQL23vUMOY4Qru98CiGis6oSPFhMKxX4TYPPiTDIV3Wbh11hrY4MtHNTm7s5lYRX0gfKoesyT8Iom2gf1LajjJmgI_rgTJ9qAvnKA25mEoy1x0pn3HivpJDFZpPvTjt6kqudu8FslelzvkkjDGayciAt5a_StnnpYBeRiNwi3VfqD5PU2mVZfjX7QYsZiPwkTysU7JVVT_htEKLg3WSiJUZI3Uk4GyPwbR-2aQzDxBzx-2dVSe95cuDG7WQxqgb_VjtBoGTTOSUfzdyruIcoSMhC75_lD6Bw26yMFomDLfmqkqS8QQI7K6HXCttd_-1pN8bLG5GrIIZuo4DY5R__6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
یه زوج روسی معروف که صخره نورد هستن، بدون داشتن تجهیزات ایمنی و در سکوت کامل دیروز به بالای برج Empire state رفتن و یه پرچم با شعار "وقتی قدرت عشق بر عشق به قدرت غلبه کند، دنیا صلح را می‌شناسد" به اهتزار در آوردن. پلیس آمریکا هم با هزارتا مشکل این زوج رو به پایین آورده و بازداشت کرده. حین انجام این کار، تو بالای برج پسر از دختر خواستگاری میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/97596" target="_blank">📅 10:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97595">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7a9e27c8f.mp4?token=inNjgZGIbm_IsOMPWlRWgy4PyCcY6cd7CVEX-7KLpg4XcbymiYI3WAEPUn0A8qbxQhoFrOthFuFILyH8y6tYstHuXICc9khdU1DC1byEeKq3mGMePzVtOo_DWoBB5-DzpGBVIGYisZxxpHaMexltswqoHx-LHlz2fbVCjWOLS5UAiRhHg3CdoNkCKZim1H54a3A54sr-T-GzpUAWO-roz6PK9yDg0kBLwtxS4Z9l8LvC920eZ9fHVWd9sSthovQtlchs_HdbESET9bxNMTTRZjqxfrp4DePkp3kKWM88PJh0j1fHwJnD6dqtWwwg3Pqq4w35OA_st6fyzOIQxYkGew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7a9e27c8f.mp4?token=inNjgZGIbm_IsOMPWlRWgy4PyCcY6cd7CVEX-7KLpg4XcbymiYI3WAEPUn0A8qbxQhoFrOthFuFILyH8y6tYstHuXICc9khdU1DC1byEeKq3mGMePzVtOo_DWoBB5-DzpGBVIGYisZxxpHaMexltswqoHx-LHlz2fbVCjWOLS5UAiRhHg3CdoNkCKZim1H54a3A54sr-T-GzpUAWO-roz6PK9yDg0kBLwtxS4Z9l8LvC920eZ9fHVWd9sSthovQtlchs_HdbESET9bxNMTTRZjqxfrp4DePkp3kKWM88PJh0j1fHwJnD6dqtWwwg3Pqq4w35OA_st6fyzOIQxYkGew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
اگه قرار بود با مربی ایرانی بریم جام‌جهانی بنظر این قاب برای عموم مردم دیدنی‌تر بود...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/97595" target="_blank">📅 10:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97594">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/97594" target="_blank">📅 10:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97592">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PpAQRu7wIHdTlcIrL0EApDDu46WnBsp3y-dfghUxUdiZfGSqbjJhjhCjZMkvFbFT9EVHhmB1tBYZKV38pnVkKXklAtNNDaakI5l6Sg4FnTL2_x_1T49CRtgAfaoAYoMUdTw_CQasIOAbuxod7CKtjcg2O_BjZlz9HQdSWCpXCRHyPI58f4azwodLk-LbTmwMAuzGiG-wnUWE_sEttsrnVhP5zNwTd32lmcZxP_BJ0SrXWbOiXmiVZAaqWvMs5jXSfstBovKj08wjXdfGjL6LN3lcxJKm7O28EvXZ55PSetGYkOT67teBK-x2lFiJKaBgxOLpL9WADG-aw6Vv4sCz8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فابریزیو رومانو:
فلورنتینو پرز حسابی عاشق بازی مایکل اولیسه است و رئال مادرید هنوز هم دست از فکر کردن به جذبش برنداشته. توی باشگاه، خیلی‌ها اولیسه رو «خرید رؤیایی» می‌دونن. با این حال، فعلا بایرن مونیخ اصرار داره که نگهش داره و قراردادش رو تمدید کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/97592" target="_blank">📅 09:46 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97589">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KQzQ8lK9rEs2lyQJmG3igN8gOuIV1hEpWu3p6ctQEv-gRnRFH3GRRDB1E_O7cxX6iELCpoyD5onLusaS7mxgPiq9eeUduA_Kg9Hd2gceQTb8n7qX1lBsNBQRj_VO1irrIBTmbzgyuoCqz15swxaQjwG7WKJoMSIH2JRmDUbYWg9o0ph03hfoUZFKqEw72DpcUJv9_BvbXGH6jlEVtzcdX9E3WInK0rP9FLJa2incD2_610e6S3OD_XwqNyj3MWdfY3nyr6nhAXjh2xl1T1moknzg-2nWK90hehaTpnC25OlOVfRvLE1h5nSqKao4VTyppP_X29nwbSEANyn5dTaXBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gRgkBVFYiBlm_tlYknGRMzJXdl8ws_OM9_HPHy0o3Hl273yVAL2S3MwSLpBGpPq5u2XvA2iKwofd6vo99wez8bOVMj8svCZgPgz0dsSo6zEFJ8_T6ljp7_UMlp07C7NzzNZ5yGhznkKf3LJ7fIJzQeR2rOkqjX7AUb6UIPJ0s-XMcUlxlwd2nulTfEAsxDeHqnNt5ieT6_Xiw_9sd3HPxhiq8vN5HEtGlXw1uIIgz5fB-WZIh6v9LviWJnRE6XCcRKv8FH-caLOA7pPBcG0X7wLusJdKa7Ec3MOZW7Rycoh3SvropVq7CuZCtKkf54ovs17LJyiXpaMtKTQced2WMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/szjbpVELhqTUHgDyl9aQ_JEmqm3h1-VNG1RocZVyEQyL82ncYEuKQPYMuTmY0NuyDBsuCq-7tyeS8YNUoMkQcam1NMfC9bAgEqWeXdgRZYR69uwD6xxnYd5LFMXB-p6tRQLB8oolnZMej4yQV74yMsmItq3-DAUo2ERL2dIMYEcwoh8icD3UYux0Y1Lsu_V8DIbrHEvYYcoqdYknWp69nM_rlCrwNTyYVUjRuOsVsQgH8XUUy_klgDIXGnmYpg3IjQc1ZxCVnxnbxoaz31HGZBzX4q6DeMm5a6xJ9eet41voHRgC4_oPg_5zNZ_68IUgVGLpgUaoTgin_IrOvJxdKA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
تفریحات تابستونی خانم آلیشا لمن ستاره تیم‌ملی بانوان فوتبال سوئیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/97589" target="_blank">📅 09:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97588">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QxuLmJhRY4HrSOEXGe6LMylK_7Vkgpy5SR-WDaoM5_P7HJ5R4wRg1TYzn9faKe2lxICq6zjN0rlhFdtb0CKRb4yNDIUtbrWlxXxhuTmURo7dMdkh78lhqCt6Iezkcubrnhptayr0dmv1tUzhnP5vTjta-wGpBBtHPI-_UhgOLQGpVQXL3BHNj3WcM_yWIkIib_0Ijv1s7PNEy1CYysc8pdenAs-CXCdkj4NB-4BbwX3rDEadHf3EbhaM1F4t5054xie0lqkXf1K8kDzGjljgQVPc6hMb7SMcETyGn1vvULMLqAn11m1ThVWqmOzpZzNsBmjjIZK7giweCRSx6dBjjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤣
چیزی که وینیسیوس از هالند میبینه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/97588" target="_blank">📅 09:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97587">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5cfa932c1.mp4?token=Z5Z0Fp8luFd4fVbrqTJCqI2THsBswNMwAzvpviGVIDWDdu76SCboieStPgVmUcXiaehag6MfkPc1QZ2n0Vf6DLgN7PyrunHdV-qGJI39WbZtDkQwJa1EpqMF1sB0-Ep1RHYjaij8-G3iT_5gP1HO6I5agj0i7BTRsZCvxVrtVY8PtlkuDF5hCfS1Yy1-oM-2Spc1XRNblx4KDfKqmrg3w_PSJA51eaV0OzlmpCnuZREPnbIP01NE76rkLtP-QyOCKnUZFsUkMAqUyjr8BYHDsLbqUmorPSa01YW4ek_xQxVXxrAGIhP56nULRKp2Ee-vmNbwNFRAIkRkAazq1by4DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5cfa932c1.mp4?token=Z5Z0Fp8luFd4fVbrqTJCqI2THsBswNMwAzvpviGVIDWDdu76SCboieStPgVmUcXiaehag6MfkPc1QZ2n0Vf6DLgN7PyrunHdV-qGJI39WbZtDkQwJa1EpqMF1sB0-Ep1RHYjaij8-G3iT_5gP1HO6I5agj0i7BTRsZCvxVrtVY8PtlkuDF5hCfS1Yy1-oM-2Spc1XRNblx4KDfKqmrg3w_PSJA51eaV0OzlmpCnuZREPnbIP01NE76rkLtP-QyOCKnUZFsUkMAqUyjr8BYHDsLbqUmorPSa01YW4ek_xQxVXxrAGIhP56nULRKp2Ee-vmNbwNFRAIkRkAazq1by4DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🙂
یادی‌کنیم از مصاحبه سمی سوشا مکانی با خبرنگار برنامه نود که فوق‌العاده وایرال شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/97587" target="_blank">📅 09:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97582">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IUoj_SadaY4JffP05KxIe_Z0j-fk3BagRTPcaAPbnX-40RarU75-taPuGVN5Jn1LEmav2jo0XzgtWJ6HC3SErPglghwwQWWF469jWTYQX8JVpx6XqHOusY4WU6hs9dKFVEL-bM2Xo3uUh5Ews16pXk5XZAg0KnHvJ0vaGWL-E6oY8lm9P9TN-SWJcJqoANlhcAUby4S4tn1YCLWZP1AirX0_GQ3Wzii6BuZSVVxCTTQ1KmxKweHbhztvBZ7_ANujhAiopC_f0GPkdVeszeiRxvjgkV2u-YrZN031wvSqMhQNcGnMjsyQ38RUGG3fQPwa_XCgRTTXYEJSQeDuBt6BKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YZgIk-cRKqYIMRLc2so5s_3I4Dg3GAZZXBkk1dW7NMNkqEJD8IZdQbnzvIBPMvz_7wcIzFUAPqaPw2L7yCGTrI4jF9MMy9QY1YzRao5pWEqqNqiKHGkuvBOxIQysnQa3XAGHdmwV4tvZARHBoUEzxrZBqsw71DXqDKyEM3mCvvP415WK_uUr3NYoDonVazY5ZCJREwoK1sv6qjYHyzdy0BS4yK4PTpNpxPQ-3wCHQajlU1PZPokF0zDrFU0BGVrGhNR0hqII7OvsoW2W7ndlSqWsPHmyHZqGUzKNhCPrBnkSzh9I49nqkujcvK9vrUMh-K4hwL0D_BmK1M6ANTdDCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/leDA68D_HeosmhNIijSTPVztnbDiYPA4cvaNTahLZpQv2HGhaZjPuFP5T9EOViK1emgxAr8jkLJmri5KSmpNWJ75wwxkBke8fgSuQn2niWyl_DYl2Yu_Rv92qecGWIYZEJ1VjPWpWx57Du0TEBwU0OebE0dc2tC0rXlPn9FknDefnPaLEAUfypuuipwkz0ebNRv6BuzafGFdHMA3CMFTogQ_6JP8E1kT9ucK_9kax_Mk2-IEP3crh7-vqlHDSajuJ88JOlSLfcFkMNfn9P6wiVwTt9iAmKjDWnwAjXRRQrNqwC9Dg821zS-p4-78xeIxh33VPQudB6kOe71kvze4yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rA_rQ8HqirnhnpgQlFebkfVjHcp8fqtUEJ_t5Ob1ngK6T3TfRWT2EvOuw1F1bgg13bS7pknXy0WltuKgtXo-hGQ4wTujZfA1Ndh71MsLdtdZjqJr054GbiWtqc3TxfjGgg_W3LWwIu-yREyHYR4TydZeVAouetzk74V36kJea3YwG_a9ZqFFejNWI8KXiiFyP6XC7t8naxn3tyksWiKbjRv5b8bUwVTV1OnBEBw3bslNXZAEIMc7LOWMtqfzLJZ6ONWbeLjMXAzCVnXrnCD6uxYaL8uyec33StAchMU_voU4aSs9OBxtqFSk3KLyPLvnJ8erQHh7iM_4gwIE3xZToA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kfeNECkkUSduoJjdQh_JbKEHqNAl0wSeHXlE_3wDIfnw158Ex7vTY7oSW0GWDHZpYTJ2K6aK27pVrvH-xTdgCp8kDaoN8amIhXPHGiTxhuv3S7IMJqqL0OlLDoTojV2ICXr8TpK0MMzTMblg4jmewCpUErB-JpKwUhfHPPjctg1lLajy5Ft8h-JykRJV1mOAratZbFSdhqlxs9GuIHCjYWPw5PzvSqzGGPiutXDkXYH65llHFMudPAeo05EwYn9o6I7WVNmV8_L056Or-fD-hTgYHVmC8kM4iAFLvMKoVpQROtECVyIhItxMj502AyENQF3KStVIf-zLNAxTgmC_rA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
دیت‌ بازیکنای انگلیس با زیدیاشون بعد از حذف دکتر کنگو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/97582" target="_blank">📅 08:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97581">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af6bf8f214.mp4?token=cNq2j4uwSVIHyDNvwTI_1wVHgHMOohZnOk0mdlSYNT7BySBKaWPKqzN03Y1Se9T0J-b_Fq79J9oynaZVJaYsfciV4sQHPdVJ3Lfrl2czXxpmTJvNLCgCt0PybgkMGqtbiMwQzei7MKbYXyRG3zHP1hd2m-pcyQf22Vzf1FW1lae1bGvWB6u0dFyai9qJ5Q0bSpIQurHe-Dgu7CqsQAZHM8pAL8zVdBEzgQUCn4axGbhX_6QaODacUEy612k4Jh9yIVOohqEmZ1fW379qafExT15mNFJQwmlIVQDusSIJtvfrr6aw6oPgII8SUkVMzvFvfhzSSVj7GGo0iMNzCYjWgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af6bf8f214.mp4?token=cNq2j4uwSVIHyDNvwTI_1wVHgHMOohZnOk0mdlSYNT7BySBKaWPKqzN03Y1Se9T0J-b_Fq79J9oynaZVJaYsfciV4sQHPdVJ3Lfrl2czXxpmTJvNLCgCt0PybgkMGqtbiMwQzei7MKbYXyRG3zHP1hd2m-pcyQf22Vzf1FW1lae1bGvWB6u0dFyai9qJ5Q0bSpIQurHe-Dgu7CqsQAZHM8pAL8zVdBEzgQUCn4axGbhX_6QaODacUEy612k4Jh9yIVOohqEmZ1fW379qafExT15mNFJQwmlIVQDusSIJtvfrr6aw6oPgII8SUkVMzvFvfhzSSVj7GGo0iMNzCYjWgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👀
نعیمه نظام‌دوست: روی عابدزاده کراش داشتم.
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/97581" target="_blank">📅 08:16 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97580">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oq3MjBeT2l4155LdVZUgEhkZGYXGOT6ROIRtpg_MoE0P1MBhacUr-TOPDXMUz2IqPblW-vaJwOFEpcR4KHMc4TISM_PlHJZBSz6XmKIsgISxFwi1w1liAnBT8dUqTBkZnUkE8LLABvCk6V9TfePZbrRFeZSOZ48726oNXACazBUGy8Y6wojrnvn6ARvYFlLGMz0_LuwQxb_bvnNDpAfeSrnQBmV1jsR4bR6laiL51T1O6l6gicPTJ7BT7Ml8B9S8eND51SLYo2SbvxjgzcZlCSlUBeCldrZTSa29q6NPwrhq7t07JRcH4cbquZMWxVrVjpgtTXouLslW-aMHZtu8kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
ادینسون کاوانی 39 ساله پس از 3 سال حضور تو بوکاجونیورز به صورت توافقی از این تیم جدا شد.
🔺
کاوانی از اون مدل مهاجم‌هایی که وقتی توی زمین بود، حتی اگه گل هم نمی‌زد، جوری برای توپ می‌جنگید که انگار آخرین بازی زندگیشه. از اونایی که دیگه نسلشون داره منقرض می‌شه؛ با تعصب، جنگنده و تموم‌کننده حرفه‌ای
🍸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/97580" target="_blank">📅 07:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97579">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eda3b086b1.mp4?token=pJsFCTXXT8_UL3psJWAa5myTrODV-Hx0G9NgbnHTqaHEkFsW5RjVipTn1InV61BM3F_EJV2uFrUACJ9OnTYu7DeTHBC1IUDB073-FXZmPbuxgMQcUQujVZziz4UmkOGw2_sQD5OsVbFMv1Xyv-ruk0-mYWmTY_SVob0kxsu3SJDD2nSTWLoiHwle3sQusJ3KesrS1rmQqVx0jC-5saZpG5TNup1_9K7sxvLMchonek29TTXW9TcszBCWqsaTvZx1P8wKZRGHcVBpsbMZ_quJ6k60t3WNHozVsrg-QwV_HfUKyXJEslw1JgTIHL4n0lp9I7I9xYSl6m092FsnkBSyfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eda3b086b1.mp4?token=pJsFCTXXT8_UL3psJWAa5myTrODV-Hx0G9NgbnHTqaHEkFsW5RjVipTn1InV61BM3F_EJV2uFrUACJ9OnTYu7DeTHBC1IUDB073-FXZmPbuxgMQcUQujVZziz4UmkOGw2_sQD5OsVbFMv1Xyv-ruk0-mYWmTY_SVob0kxsu3SJDD2nSTWLoiHwle3sQusJ3KesrS1rmQqVx0jC-5saZpG5TNup1_9K7sxvLMchonek29TTXW9TcszBCWqsaTvZx1P8wKZRGHcVBpsbMZ_quJ6k60t3WNHozVsrg-QwV_HfUKyXJEslw1JgTIHL4n0lp9I7I9xYSl6m092FsnkBSyfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این وسط فقط بدل رامین رضاییان رو کم داشتیم
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/97579" target="_blank">📅 07:11 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97578">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d15220e2e5.mp4?token=ep6_1WFL2SToevI51ZZNHEQ-ot3ZagidvDcxoq5ou5nybvp-6W7zMV3aXYlCej6uhs6jL3hHu1ahDLder_609o4-vhfNTHXJdMFUnT6XTJSmM9Z4ryxHHcAB_vixGowkTZFX7fJ50OmEk0WDRN-5q2m5pTAk539uzd7FHUkgFZLTmSlHIT4GZkRjV2HLXX4FfzkIz7bwWo7GVBRLbRerqHKhiH361FaOcyPdNUvj435aCHM2Dx1pTygOJXBarb6D1hnstFOBPxGl1AnscxKiJnPl_GF6csoNiFsSE3vk-dVipr1YvMfuUF7HSbQXqbBwGN32uKi8TqluDEf6FItLpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d15220e2e5.mp4?token=ep6_1WFL2SToevI51ZZNHEQ-ot3ZagidvDcxoq5ou5nybvp-6W7zMV3aXYlCej6uhs6jL3hHu1ahDLder_609o4-vhfNTHXJdMFUnT6XTJSmM9Z4ryxHHcAB_vixGowkTZFX7fJ50OmEk0WDRN-5q2m5pTAk539uzd7FHUkgFZLTmSlHIT4GZkRjV2HLXX4FfzkIz7bwWo7GVBRLbRerqHKhiH361FaOcyPdNUvj435aCHM2Dx1pTygOJXBarb6D1hnstFOBPxGl1AnscxKiJnPl_GF6csoNiFsSE3vk-dVipr1YvMfuUF7HSbQXqbBwGN32uKi8TqluDEf6FItLpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی میفهمی بعد این بازی باید اشک‌های رونالدو یا مودریچ رو برای خداحافظی از بازی‌های ملی ببینی
♟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/97578" target="_blank">📅 06:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97577">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uSiXS7FrIsMLrRff396lwAG-n1TalOx-Noc62o8i7EQKh6R1apUZp0A-eisPKB1JZ_pRvsXi1YHK7U3cAIOqRPpQkP17KFNh8aqQUzAUxHHeHdSYsgK2EFKythW4aCSQ1rizF8xTnTstw9AT_xuLQC2s4pVRvamJs4h6gh92N6AEHgFbOMWfuskoD_5HdbH024ukShyYzFyQVjjF1mns33GCET1cZTuTT0JrY4-DZrHUyP-XwgRktKKpUazirvureMzMszL933ZXMQOl0LZ-Ie5Enu0vMMq0H6KX3qWl9Tt6X_7ldAUch4cVH4hrqZstBvFbMYbvEGph_m6N1H80OQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/97577" target="_blank">📅 06:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97575">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NnF_pivk0efhGdmIJqUekyczyv9tBfgYKs82BHJR-zged2QZIqrGvA-dGQQ0oOXlew1Sz2RDmnmoDzsPIx2GJwTDRBlLsQh1PkF1Rsq2k0NSAzztlFPlY-_ZLwnFqVa04Himnwkr5LCj1wrnLLlw4pmafOKCatpikKmWUokEEzftgiW38H2fOxfYpBlPfhZUicNNG6HTGijm9Kzm2toFDX65Ezpx4Z6tU_UzWY-VVlF3NLiMhIA1g_3TsKWv1fQ36MThXR2mO4bJPrTp5EyIPx_ncGW6L49t4HpqKCcPf5VdqBU9e9RR4QcBLZdQt1A0Sj_3zBF1rKfRe29MYRmRbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LwbfL-XdSLx9WLbHgzXWMxEJPI0J7cLT_z8VvNPOyTv7YaGqMEI4yz6CiIQ1sptj4-VYQ_W-HdEPMPGi82Ef6O3L7VJA0hOWra07FB_bsQggkpLzZXxGOP2_wyx0t5M7IUngNfUKWUnztokouRQqGOPXC0HqyIi_UUZ3snFdV2D0SSydd65MOng2v3fbqewEtY2fB6lNJqSqSLvjHxYH-AKU1Ot6jzdBGyIhZ2z961E04ipMdbVquozT7bdnq4f85XF5CerJ9XmLZLVBlGKCwmvZHG_kzap6VPklrJ3dzJYqNiIMtUwwuf61Pe6Cbxnb1MjSKMRSDKgGf4t1krYWRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🔺
پاپه گی در اینستاگرام:
🟢
بعداً درباره دلایل حذف صحبت خواهم کرد. اما امروز اعلام می‌کنم تا زمانی که این کادر فنی در سنگال باشد دیگر در تیم ملی بازی نمیکنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/97575" target="_blank">📅 06:08 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97574">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FImpBxsn_1cTE4BaQoLoBN6xyHxfB5of0fAyuQyoqTt_zfvteyn7EXGAPQFZquftyOkbE9yCgxnjHd1gpatwpsUVFvcuAciqjreuif_9FtMMfPhPN4tbUa7vbO1qIO2GUNtf-RB9eIdXET-j3Nh_WoyQpawE6OuwkAkzOsTN-YpOj_nlOHlTOtsvzDPcEiLTbxW0ksNAH1rud4DXCMWtwmwijm_fPmLAdGRrenw1m1F8n6cErhFCEie9F7vBOk7o4KIat2An1ebLVp2xJ-dREmG618pgGPNggVlZGEsMyDeX5kCynYEOITYuj2hgL9a_JDzIEtuchm1neZOLBvvoBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
آپدیت نمودار درختی مراحل‌حذفی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/97574" target="_blank">📅 05:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97573">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AgXnFwLnZmyvFcR9Yt8jSQBTBA8nUJ9tGS5rMOW-iQveVh_UGiBFChABgV9ifCw1ZksiLRFB2arEQx-VRxvpKrIHJP47xRFb9jrVSALcSglS5VUtpngCLpUPAfTQyuM_73hXeYly08p-VDqAMLDi9-LfXZndm8PeMshULB0mIqeCUTH9E_TRDKM9WunQGxnOsS4n33Z153M2n62LH7HdgJgSIYlSkP1mKp7WdCZTzYmilWtYt4H0AV16APrgiJVqqcRqkyU4Vq9HEADTqxh7vw0wPPIexWNVH0s9OGi8KSy13NOYzbVQNykgjsDHBR2PxM4LwJbayJEOBLYjOGOzxg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/97573" target="_blank">📅 05:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97572">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NrMOBJp8Q73Xx1cj6nwCsSVhRrvfxKJT-UgTaNXWPiK68f2W8vztJEkBdwUh2w2ccxVzC4mgIcZS97rl3jNJwxm35CC7dmEch651L_F07xaxhiCY50nM8mXrrEt_v4Ghl3w-rIU-t0tilZukOu-tApshTZu0svf9YfS7mDI3mBIc69HF4x4SXCLvoSiD7SmxrtI8XJ-b7IYtGgNsxpchWOvZn_7yYLUtHzwi8MHdSg17SIpIgyfJQozC7OSG_VKINbxnQVUFtRb66XTrLQMFrMFyhI91022YT0SaDIaxshQZGaOslgjBi_ZzFpPGCnPk4PpFmeSHy19k9sIM6Zjfrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | پوچ بدون بالوگان در یک‌هشتم به بلژیک رسید؛ ژکو و یارانش به خانه برگشتند.
🇺🇸
آمریکا 2 -
🇧🇦
بوسنی 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/97572" target="_blank">📅 05:39 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97571">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pw_dxMlk-e1hWOSEpB_2Cqcc8uhQ8PjQDRKxfmLhkFDcxcS4FKXe5uq_A2nNIgIhUg6GdfudaVhC7OQ797RmVq4oQpGDUG38G-QbF3nkxlY7SzrEraK29NJF0JqUOP0-OnLLMEwEgGFza7FgbWWmoR_tMaJKkws_uLq4tMxEzPt1vu2xgvanjYpuMQ7Pns-GeOJHjINfHzVcF73F1XZOc2-zTy3D-k4hqCSzyIs1zhF5LQgwieCGK6pxg4v2Mm9Ki-hsOwBgIJatCvA58Vy04TJ8C8Acwus4Hfn_I9EFfKPnQatw6h0HY6fAdPXK-gc0UWON5HC4bGwWqY0cW4lzwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
#رسمیییییی
؛ آمریکا راهی مرحله یک‌هشتم نهایی جام‌جهانی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/97571" target="_blank">📅 05:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97570">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ده دقیقه وقت اضافه</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/97570" target="_blank">📅 05:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97569">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76ea16f99e.mp4?token=VR6YbEFWlSthYSz7eKZdgV2qqmAdZhlPpkAGpWB22J-yb1_NKeFwRHjnEucH5w9frVnXbS_m8sVvPvPfFeAoi4xS4V3AUOZ4z6bpb-wCSPNvNURrcaBoUruKsWxGOrMnr8BSwUIZLNNhW_ZJe2DKmkm3Hvfpd55jL7ejZgGQmXMx-RfNWRPR3X3pB4aos20Xv-T47EePjHEkbZEQy4W3tCC7Oi41vG0lX-dRg2XtY3Le2S6CHn4eTBx24bSEff-bMJkbd9h3Bf9avIOWVj1xSLT_iWPZuDeH9b7zLFTCjv-1HAb1RVwaIgbqAXzlTKoVJ0I9dE49xvn63UjkkbP_-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76ea16f99e.mp4?token=VR6YbEFWlSthYSz7eKZdgV2qqmAdZhlPpkAGpWB22J-yb1_NKeFwRHjnEucH5w9frVnXbS_m8sVvPvPfFeAoi4xS4V3AUOZ4z6bpb-wCSPNvNURrcaBoUruKsWxGOrMnr8BSwUIZLNNhW_ZJe2DKmkm3Hvfpd55jL7ejZgGQmXMx-RfNWRPR3X3pB4aos20Xv-T47EePjHEkbZEQy4W3tCC7Oi41vG0lX-dRg2XtY3Le2S6CHn4eTBx24bSEff-bMJkbd9h3Bf9avIOWVj1xSLT_iWPZuDeH9b7zLFTCjv-1HAb1RVwaIgbqAXzlTKoVJ0I9dE49xvn63UjkkbP_-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
گل دوم آمریکا به بوسنی توسط تیلمن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/97569" target="_blank">📅 05:23 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97568">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">عجب تیمی ساخته پوچ
🔥
🔥</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/97568" target="_blank">📅 05:18 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97567">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ده نفره زدن</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/97567" target="_blank">📅 05:18 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97566">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">دومی آمریکااااااا</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/97566" target="_blank">📅 05:18 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97565">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">گلللللللللللللللللللل</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/97565" target="_blank">📅 05:18 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97564">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cgs-WS4ibvcuWzCz6KVGNcXafM6AlvjFRng-7JoNHpm9PO_BqQ_e-kM70bzgN0O0eQTBwBe4fqFP89W0Q079dh7a9CJdqp4dkaDpLDLRJJ4guShQeRKDJr4cAXBeiRPizhVwjo3PbK0aSxmXZqXr_DCABGTccmrDHeE4mTAj20Bb9FwvZifL8XZGwCevRqAyv6QHnJyWt8FUzCLjQCvGbMxd6TE3d__Xc6b2T0GSs_7lai6ZI39QMP22P9Q-BqVBcq2Su8tI3xBb97FhNYI0Jq34uZwtaS4MzeDdFstx3vz0JurliOwl55yHGzWyGgSlTiyWNtXNX359bDk4XFsuyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/97564" target="_blank">📅 05:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97563">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">دومییی آمریکا که رد شد
❌</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/97563" target="_blank">📅 05:15 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97562">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GBKaWGYEZd0qps7eEtjlZD8MFUHJG_4vNUFekP6IOhIpPGnBzb23NIYJwHaD9YVAM2YhUeHifW8fvfFxz604hLPSxBubMrCpnnyVUAZrC4nTPBRKIuT9VZcQCEKrwB5SAelSPXhboF8oMsE4Vd_fgwKB3WeA97329GRpcdHe9p01p1uVZXPE_SWlU_-jU_A9UKABOL1eOw_y7s5oxSXpsqXE68c43jsrRXG28AL6_eh11Ws98EqPsAU4eYcz5HSs4U_uzIJl85EM1lX1HxukQdZp9LT8nEG-Icvg-DhBc1r9TlxHaQO_JsZB3gIqGGu1Hgkmt6TD-d5geKzCOph51w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بالوگان اخراججججججج شد.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/97562" target="_blank">📅 05:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97561">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">بالوگان اخراججججججج شد.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/97561" target="_blank">📅 05:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97560">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">دقیقه 62</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/97560" target="_blank">📅 04:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97559">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">اوه اوه رفت کارت قرمز برای بازیکن آمریکا چک بشه</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/97559" target="_blank">📅 04:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97556">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KcCNNVE-8dFzxFImodZxT4yTkt2bEaXH9m7ckEl9kpwSCxwAAmADuxuOFMxDUo3qeG4C1qxhpJT80QKPR8lG7knZWC8yvhcezt_r1uz_e2Kvi43p0FU-iY6n4bnjyfBmIl4zoq7lzZabrerzHgvENmEpGW4qJ9fR_NV1TNQHMuetbfBWPS_RZ8plBeH1cNcgeY9cYHEhUrSBkk8NRskgvgnQVDyVdEX1eFM6UUzc3Mhi5_WbPPoeLCxZDV9ZF_O1RHBQF4LoIBW2vAqUXanNCCqdCbF1Mmf4mUf_yYMenHlPpuLQFZjVSw0J_zIjOCq1UyjKwrZo7h226Af0CChS2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TM9ij0_V_aaieYhAbipZO6bnsGgqFualO5cfPq7L8pq4WUOYCrXmjdJDI0D1Sr2G0p1yBFUhYkdO9eHI10lmm-40ezAmHgtGXsgnYJ6HsQO6RTrGbe2k5urfg7ud4D-Meq2D_WdmbSqivSvatOGWpg5dMANgNCSjWSP2ebAC5EWvVmCRA8h7SP5Sy_t8M3IDJtx699H_tauzuiYrempAqFX-_Y-JTzIGSfmsvmtD1DE1ElD_hTtumqZeIjWg7kd_tW5MD31cpl2UqLaB_q6Bme-tBmCBcfomPTsHywHYJ77slTRBVsIuyPdNnEcOpsRYXSp814v32sPNryNYo2xRKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dAANbPZxclWCaaoihMbbqdQ8ckwGHHT3Hr_pKaSC8PnIhCXyDoVmjcozldD0L7p2tNirmZMretlp6DHbGAx_kPWxUbiTtDUaKCSreVDP1fTg0ANdhxyS6PompCbjNNzJuCg4slQWLyj3AJtRa4I5UmVxyzpDUf8NVQidzOV-SuLmpaf-Is69MPK3aZhglSUaqGABtKUXC7S16XbbLFBy9oKk9IPnr4-Ykmc232W0XZTuR0e177SPlFqpMgGXrLSbJWqrjmPDDJTYef2b49771QQgl0LuHoriEjr45d6ixsCpBfAvcoQnCxebsFmUgy3NHADoo_VIs3b3JfUKegD8_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
بانو میروسلاوا مونته‌مایور مجری شبکه TNT اسپورت جام جهانی هستن
🐸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/97556" target="_blank">📅 04:58 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97555">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t5qhE8RdvP2B6wRaPpVuAm4Wlyt6Ecm1WY2ffxeFCid-vLZS9E4f3xR4XGCLC4I5TdfLXCGxuD3mZCkQxyhA6hTBqC6b8Fq1F_xl8Qd2VzWTqdWpDEBLu0cBSBBPr2mI0MMtJazeBiQy8Baldc6xj3ccicayfYuj_awjXDGQEPpeQzOghQ70vOvwegnPa0qB8xrl_TYbJCsSul4GG7m3CysCsaAMWgYoO8Qglk3jppVf1hhcxOP1lYa4nfGnsI3Z-GD71Hed4jtHZUXRNHlWZZ4MRlLnMxb7ycnTRlKs1Btp8q4XkQp6iMvVv6iYCiXWWdiHZT0MFond8oPDEXeR2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
تاریخچه دیدارهای تیم‌های اروپایی مقابل آفریقایی در مراحل حذفی جام جهانی:
🗺
اروپا: ۱۴ پیروزی
🤝
دو تساوی (که نتیجه در ضربات پنالتی مشخص شد).
🌍
آفریقا: 4 پیروزی که دو تای آن در ضربات پنالتی بوده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/97555" target="_blank">📅 04:54 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97554">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ch5CvkGAAeDZU8tsDFFLfAsJ-SnQfBaWfLqoyWnr8so6H7aesFG4asv7HQIxKy9FQHiLHWB_-PrTS3lZ7nFavKHXSJXZkUyO2vYADpdjZXmkD-MzUkuMr9T1bIHLbQ4cWCN_yFM-B9lxaa7p19OgHUivoZGqclcYnl2thNLf5SArLTORuIO78VrdU2g8epadOOyV1N-IyRNWi4AFwg644QEN7uf3yttYfcOAWWN_oQ_47RRBJ4Nsr1zvW468YNKfIXbhLmfbVSDkaQThyNrPdK69G8nEJFE8hBBQ1GVxsnBEwSWv_BC3XqSTOH-L12rmZo8G4BWZCaBy-_HQEv4r2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخ داد پرز بخرش
😛
🎙
ویتینیا : لوکا مودریچ برای من یه الگوعه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/97554" target="_blank">📅 04:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97553">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/94e4656d07.mp4?token=SNf7hEm3XEbB_CnTkQK3qES8pGBSjvHogdUq67QdclUoI_OaBimArIG3INdiTfj23C_M-9xvCoktH4uvVW-WynY8cM_Lzt2q_lFpqY29xij6GpoVgp0ntvfxczCNZUllzeAkoLtLob2zzEuBs8cIpnNoFoIhOMF873elXPVGxUOVhmlhsZ_alVC09r_ep5WTOOvNsAzKm3r6Rc6OykOss7aie0MNgIKiwOHvPNAn6E1i_Vm4Lr51gtwfaI3i1l7zah94uNCZFuufYubwihFO5ai76wOSSEz7tbppB4tdEuyD6mvSdnAkphJn6AyCGD-d8xU595VaN_kXYh0mNhf_bA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/94e4656d07.mp4?token=SNf7hEm3XEbB_CnTkQK3qES8pGBSjvHogdUq67QdclUoI_OaBimArIG3INdiTfj23C_M-9xvCoktH4uvVW-WynY8cM_Lzt2q_lFpqY29xij6GpoVgp0ntvfxczCNZUllzeAkoLtLob2zzEuBs8cIpnNoFoIhOMF873elXPVGxUOVhmlhsZ_alVC09r_ep5WTOOvNsAzKm3r6Rc6OykOss7aie0MNgIKiwOHvPNAn6E1i_Vm4Lr51gtwfaI3i1l7zah94uNCZFuufYubwihFO5ai76wOSSEz7tbppB4tdEuyD6mvSdnAkphJn6AyCGD-d8xU595VaN_kXYh0mNhf_bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گللللللل اول آمریکا به بوسنی
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/97553" target="_blank">📅 04:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97551">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A-GAA_5FRGaPmn_hrGVeT8l39ps6JKSO3jHYdfDoVUv9O9d2Xgq-xcgIPysuW54LfIGSa1HfZUEdBNm997dsiOhldCC-wej0gCQseOkNwC3k_LFu0z-dw_7jAjdia-2JgCDFwivcXnOmSjleg1sgWx5kBzcF3akV6I8ggkeqZ9iFny2YlJGwgFG1Yvj9iAqRpB4iyV7NXd2Is2A2I5tVR7aZT0cMvr7BGiHI9ljsnRBfBsODEbxJW8r7HEwdCqcBjuf4HByOj7YZEum40-o-OUZY8emOVt1XUoSYYiQa9z4Mz_pNGyE9b_GecUfhq4JSYRl5-gqEvT5NzcwkcAZK1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇸🇳
| تیم ملی سنگال اولین تیم در تاریخ شد که پس از پیش افتادن با دو گل در دقیقه ۸۵، از مراحل حذفی جام جهانی حذف می‌شود.
❌
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/97551" target="_blank">📅 02:36 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97550">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XqPXqU681qMqBy_evz-Nqn_gYsrRLcWxuMNCIhYGZxHW3T8Z2RLn9o5n6AbwYohccPjbCc7nFLl8M8OZkTKSlM4Ki2E0yrts1od4_ccDfbvy_KTgiM67cNJZjVZhirrYzMTdIX7jdBrA8f1yhp9Yvf-ozHzeBv7Ht8g6n3MNE8T5gN4SQ-tpIB5gnjk3doEOcoCUED5qA5FoJkW2eKifx0qZe9aZlLV9TwwEerCPEce5omVVlDskRzTx--5fnNA9GbwllhmsB4chfRrrVAM1I7l81SMDzxeCFiTWQt2YjxbuOhINh2GsEOV62iXIYkEDUYNGHdtkEPuf9t9zbHvbyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🇧🇪
بلژیک در ۱۷ بازی آخر خود در تمامی رقابت‌ها شکست نخورده است:
11 پیروزی
✅
6 تساوی
🤝
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/97550" target="_blank">📅 02:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97549">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ekJRpPFwtjGBWWStmMUxHAg69dZ_G0csacy27yd9K9TzXPPgBM0uja2ZSx5CdiNS79Upb-lbN0YtycJN7786ggqt-bCYkiWD9Ri9BX9h6vTCMDYgthkChEYDoxIWwmsjy5Ef5_MrIUM9MYA5fyoB8gqQQpdahmxwYB42diXy6gr7BPUuOiQmeGA8_3IMsQmtGa7rdevg3-FNShYeHHKc2quQ6cJwzKAltI9EnBp50UUoa7HEcfWIoFiG1tP8w-a06T3LHTq73zAip4fHHsR84ABrm5AWeLgqWa3kFFHdivqJ1kbxCY4m1NrmzfjvmCnNTJiGTgsFRX84Rnrex0TqAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⁉️
🔥
🏆
بهترین بازی جام‌جهانی تاکنون
؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/97549" target="_blank">📅 02:31 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97548">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T6cLpbqqpPYjxlYsf0_Ma2sxkCsZP1tjblE_3SZW7q3k1-gLRbVxl6hPYlOEkgLNKOOGIsnfzaHfJCyNVnIauxOgo3gfCSEXwJ4w2EpJ6Ve4_j5NEXYTE77fGdvsC-ll_wyJ1gG2Nkt4-plGICWdhcae9PsdhznwqEqRV1mkaGS-Sd9BUA_psGNYJNWfcYq8mFUZjodP08CW8zy5KOPYk9C7_Ra2Y6QxD1V72L-Zb4EzhIQ6lPmhEGGUMlq0UPt6l-ciYYrgNUnZqsrjJOGpbOby_E8FhCUJONzLYjAs2osXbM8n444aQ1B9DK3wY9M_-ZS6aPx0GIXiKnw9pdPEbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏆
🇧🇪
| بلژیک برای نهمین بار در تاریخ به مرحله یک‌هشتم نهایی جام جهانی صعود کرد:
‏— دوره ۲۰۲۶
‏— دوره ۲۰۱۸
‏— دوره ۲۰۱۴
‏— دوره ۲۰۰۲
‏— دوره ۱۹۹۴
‏— دوره ۱۹۹۰
‏— دوره ۱۹۸۶
‏— دوره ۱۹۳۸
‏— دوره ۱۹۳۴
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/97548" target="_blank">📅 02:30 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97547">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ge0CTF1S2bTUmpHv8vqSQPH7RFyvlcvciTA7e2xmzd-8TaK4xN-oeEMRrtXcipdT8QWVb95KFRN-58QeyCi5f-d4PwZKJcZnxTJBqmDXI73jmNUgIsCt-YaYnT5xlP3fl19IBl4jdK79i_jCrq_q9QJyMMSpRQnvUHqfqhobA8kEtZlrVh9fU-QDNfUBko3iFswQCBXsc663FV9Fa-2seRaAClbTEyq78KbJbWW6NAjz3eiAw2DlOpx_vPiimj85_rafNsnPyCO7osD8HsQ9VAIXYGTNjZapbc5fX_RB0p4q01VJJrnlAtUXNjyxyKrKnZrdh3nanxE61KY7Zm-r7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🏆
| سنگال چهارمین تیم آفریقایی است که از مرحله یک‌شانزدهم جام جهانی ۲۰۲۶ حذف می‌شود.
‏ــــ سنگال
🇸🇳
❌
‏ــــ ساحل عاج
🇨🇮
❌
‏ــــ کنگو دموکراتیک
🇨🇩
❌
‏ــــ آفریقای جنوبی
🇿🇦
❌
‏• تنها تیمی که صعود کرده، مراکش است!
🇲🇦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/97547" target="_blank">📅 02:29 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97546">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FAJunsQbElkg2JC66zN8esu7WOmIBQTcR63pKUQjjphjVQS3t9y2nv9g5_0gQVmEjVrUv99gzuzuRp_wMDrD4fGlUGr_UB5Kp10nwWWJZAYvU-QkceAzG4_hSnyT6kqdy--l7g4or6OO3WzdWyfdar1mV9-ZIwRMNKfrJdcsRKFuK6rU0j8yXj6HiW2xMZy_guMZEWIdAXz3beN85onNAwDkj8yb8o_gBwMbBmio_ahyLO0hKS4-ziHaWbHqBlf6ptbxZrE73Ih86N4b1eQcL8Nbemi_ORVlqIlpqTD9cpgEWPPFnfHo61Ecsf3PBiNE5PaY0nDxK6A2D_OVTlKnBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک تیم از بین آمریکا و بلژیک تو یک‌چهارم بازی میکنه. بعد هلند و ژاپن باید حذف شن
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/97546" target="_blank">📅 02:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97545">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OckRyVtqsjT3OG12xFeNn0CLXKEfE7j1Zeiou3VmwfM2Jax1AX-vyTnfKkY8uqvrL80fdiT3wABBgKWHfqYNvCu7mbpwaxDMxh1vilq1wQ-D3bQVfEmJDKIhkQh-fDAKudozXhwh6t_IcTlY9xJD3YB9SeJHAyaluDisrEbwuxBspcqSmtUqXizJefVFGUsZ1FmSA0-rRu4qYNXMEy49wugHPm44eMKuxkwi3uRzdOjeFgxG9ijg2GaFAE_D75cAL_hp4K5RZCTzO65Pso8LiPpuAVBQX3dJyttnyUfB57U11dfNBGuKoF-_S0fH1xyDppKkP9r8c-9s-aUWY28bGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
آپدیت نمودار درختی مراحل‌حذفی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/97545" target="_blank">📅 02:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97544">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kDk2EVLy0u48tiuTNVt7U3f4XufxnYLz1kg4JR5jqGARjBE6Rbj9aLpnSc4pDBOnaTlkgMcO9aceNWqwOD53Vk5HPOz7LqS5dQZzj8_djUt81bFFyWBrAOMgquc6CAmhYtpCrMCzZVSu12CuZ0GdSeAbviNKRHOMH4bRuM58cqSkMReW5LdLlSfOWN_qbAvbqbzV9r-ECgAkVbo_onbp_SVI0TaqilO9pAy5OJA2S6g2fblVSIXhjXwQ8H13kJOsXUO6jUyJ7mOImCdkytepaKvJBMKNDmNPWNb-Ltju8fq_vTQy0kPrsPQ6PgVJzv_DovooMY6ccc2lMt9ucZ31Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
🏆
گل‌دقیقه 120+4 یوری تیلمانس دیر هنگام‌ترین گل تاریخ جام‌جهانی فوتبال لقب گرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/97544" target="_blank">📅 02:26 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97543">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X8R-km4keT9iCPj3VRyH1YakCVg1intbqXjcwKGWIj1D4LsS-7uQfvWZFPGug-3PBIehRecwPOggkTbnxgZBBkibinl6k_1KdgZaZs9_W4SS9V346fTdAQyQQAsTpZ2CyHcZEqMrHf5vXMOj64avKlnx3ZgA96tyFl_Tx6pGooNkX99zaqdXOIcDub56G3idlVfJOcnUepNNEt2xxopasSWfZUMYNbL6MZxSB9qhV4KHjZb3Jdmrm4qwQndNMFTeskqwbIUAIC-a1-0_2zQwccXaJuj8yP368OUXpiY97q4CGP1l6scu7A4ut3jw6kWeeioREGIuTkT1zHfnu2SP0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇪
آرشیو وار:
پنالتی بلژیک درست نبود و به اشتباه گرفته شد، بازیکن بلژیک خودش باعث برخورد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/97543" target="_blank">📅 02:26 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97539">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q2Qj5dociKOGr_ZNkkFRWl09qn3tx-B6Gf2rJO32X3PliB1_slE2LTDZmsF2SHK_VKAxs5DWsSHVqYAfh7Ezh1oAjdbwNyD5hTdAvfvmDKmgwuf5MQTFsahBdHcu1B45-A-4csbz1FuTccbkUdIifWM2FQL-toqbe49fAelakZz3GzEJdMk-9iorgJ9Am6Smxem2vuKwwvYRdf0EsMAfctunLX2kY3Ld2126oYwyak6PUxSOOmiSLy69YMCgFCFEK7eXUdVuPxDJ0oxWDR23J_RLjsyOSdVwe2G2sw4J9AHUdyF0Ki_3FISRZJAmPZ5F7-Drh7-G-aLibgn_BJQOXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TmKX9p2qPV-oSAwkf_7MZBiXf8phXUyIVa7vkqgdN8cINli1qevHrWGvs-c-gPlDRnn_r47KUtCy7u0cK1W1uI3jHnk76Xz3qPI2Kl5amqBhw5wg8bGKYUQSzq7sDlRmbUDY-mwDiD1YApkIF03SDFDJ-X3wRrGblM9KySF681TIRUr6BeUD1v5ykwpnGrQzHou6lyeVtP0d3GbQy1Xa_ZwqpumUmlSfDcfi_Xx8mUYdMAcF0qWFjm4urdQ4tRwBU3risAx0bcNRV8zEImxQF_QNvJ5qGDTdHzoTqaoyByPClsGM2nCSI7ATkfZaT4zTP1muS7soGu1Idt33TON_sg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇺🇸
🏆
🇧🇦
ترکیب آمریکا و بوسنی
⏰
ساعت 03:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/97539" target="_blank">📅 02:25 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97538">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mE-EQaIemf9Xk6KsBLKeOk69YHfOHadRJszJPpVouNKgnEt9sTC8nILeIKc4nu0s-Rn-C-TI4VnY5I6j-PGty_NfkSs1PpSLtY4s_eEMGFzOOFeGWBBxSz-O_EJIMSjL-u38uHtWFDbwrsqPTjq5A4yZ93V42jbVwixGjADSZOISigiS-oANLzi4QATXYDmcZQIecgzbEfGx9abTVANHapl46bGJ4Ls2M_rVZS6B2b0M6caEgqzRIdrPT_ZyVXVX9wFbSLHO6NUs9qJO5h6LI85n3a8eNkQwYtViY-UrV1lcLuozKinDEMG0tH23R-g5_Fup6sEF8mjn7T14rKPKIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏆
🇧🇪
برنده دیدار ساعت‌دیگه آمریکا و بوسنی حریف بلژیک در ⅛نهایی خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/97538" target="_blank">📅 02:24 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97537">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v2KFGhXPgqqgLJIAr7KDCzsPA3wGPWN5P7vj7IavJTr7fy_LrbFgv4u-M4NAHWsiLd9g_IDmIFUhJA0cDNMGDeCTPi592oFxDZ6V38msDzhCq-5i2QzSxygjTCUXUlI797_f2pb1MJuzKJsu3qNOznjKWrmCFPwjRUvn99N51iHXU2BK2_NhutqLSwFsiDWFcZDVf4qfWCrU-Q-6ReTZd34x0Qrv-zSsPMs6vouMbLoNG1g1siuTlH5mB1zhVW8GSF5tnAeWwoZNtvM1Itfr_uWjPI5Jo426R8NDrGHx1oS6LD-UP1lrjZXQUGpnFHz3FUVI1kcERR52bevpcYyu4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
تیم‌های فعلی مرحله ⅛نهایی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/97537" target="_blank">📅 02:23 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97536">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ovGnHkWkgBK8hHxG_x6iP38MimSWulQFlbMK4gS6rSLjEHwRuNaaeOj4CwFOC3sBiLss8920hSdl3_D8R4HWP4oWf4i3wiILi84EAIc6P96ndYC2EBLFGdFqmv0st_X9szk3BqJI0lXWyGYoBG_2OCDsFxWlbUkmcFnUPjiBK8E7Dt3o953PzuDiCqlcu4vUY1nwT2giUJJYLbFcWq8DEjTIGKbgRkjje7gTRVQy_WJMC0eJV5h-4ayoriAw1leZdcKdCRr4g_y6x9AxmYrcDJJfKek7qgcLDpar1cgsLQIloYwBdQV2COqQ4Jd_9D_ypeP_SZYI78vk2skb3H-hYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
و تاریخ که باز هم برای بلژیک تکرار شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/97536" target="_blank">📅 02:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97535">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sBq0Ezm_Ovq_NV0qpsO7y6OBl0vElW1TIwMvLGEKRNPQcOxFXQ_mNFt7Ki9UWqNanlIShWYUIW7cKVpICmyxRBJg1ASqGFf3lzHg07Fh4BI2jsg9Xhc0cJ4r24b8PbL-ub6zXt6Bwj0bfxMuZgxutMU8FkSEDqHpbdfsu2MKb465WCZc5h3Z0NmRIrFXp7x8hfYVXW9jtEzJoOwCWis9m4KfADRCxxGY7mX9C7zyzRHRRGs0sb2w8J9TJHDAwoKgFAp3poDPRZVrmDnHGTNsSbeDrcWuaMmRDiT_eQ4MFkhD9PW496xq6vhLVuza8Nm7omNDGnQbyWLOTY9OA790-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | کامبک بلژیکی‌ها با پنالتی دقیقه 120 تکمیل شد؛ بدون دوکو، بدون دی‌بروینه، با تیلمانس!
🇧🇪
بلژیک 3 -
🇸🇳
سنگال 2
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/97535" target="_blank">📅 02:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97534">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">بلژیککککک صعود کردددددد</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/97534" target="_blank">📅 02:19 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97533">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">تمامممممممم</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/97533" target="_blank">📅 02:19 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97532">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">تسلیت به هرکی گرفت خوابید
😐
😐</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/97532" target="_blank">📅 02:19 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97531">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">دقیقه 131
😐
😐</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/97531" target="_blank">📅 02:19 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97530">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">میگن پنالتی شدددددههههههه</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/97530" target="_blank">📅 02:19 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97529">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">چه حساس شددددده</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/97529" target="_blank">📅 02:19 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97528">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">سنگال فشار آوردههههه</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/97528" target="_blank">📅 02:18 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97526">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0db93ce7eb.mp4?token=Ml7ZY8WR-YACcT2y9GE1041McZ4Els3rBVK5sJBKfzQR-4KGgmdMSqzw5k5Rk_ywUkm2wVHXeRZ8boXoZV_Ot0lQw7U2qph3-X19gQf9PgNTDPlLR7H-eBo0URzkjbKMNpVH97_-3SWndeBJVaWRHOeT33Ae0KVsFpsgaCV594XG372o2qyOzB4OAeAutw3s6FT6dlSapni7miwmGDJ8_ATI1dlScmY4UKUexJhgQnODn9TBIYa9hes83D8FDzVjPxGkZgooPVr-3tjAnLelOM4W_9ZGmFh5tJ139-6JcmfFd-28mZ0UJfSp6U4xM9T87cIC8b-2IERczcXxrwJPOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0db93ce7eb.mp4?token=Ml7ZY8WR-YACcT2y9GE1041McZ4Els3rBVK5sJBKfzQR-4KGgmdMSqzw5k5Rk_ywUkm2wVHXeRZ8boXoZV_Ot0lQw7U2qph3-X19gQf9PgNTDPlLR7H-eBo0URzkjbKMNpVH97_-3SWndeBJVaWRHOeT33Ae0KVsFpsgaCV594XG372o2qyOzB4OAeAutw3s6FT6dlSapni7miwmGDJ8_ATI1dlScmY4UKUexJhgQnODn9TBIYa9hes83D8FDzVjPxGkZgooPVr-3tjAnLelOM4W_9ZGmFh5tJ139-6JcmfFd-28mZ0UJfSp6U4xM9T87cIC8b-2IERczcXxrwJPOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇧🇪
گل‌سوم بلژیک توسط یوری تیلمانس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/97526" target="_blank">📅 02:15 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97525">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e3uj1f5CR68EQt0gWNUCm7x8J4FBUyyIbIDBB2D0B6zXbIgGrAKoeA56hgNWCEvQFeM8cWmxKwLFIn07Es50lyzVfben4ARUb-IAdjJHDHcfqktpa3_TSTzmQQq5N5wKDBN8FBEbTNI_AQBqeIwNERSX8G8cvdBDGrDFbhkKLoNR7S1QORT3bQnX1Ix86Rrpl5wCiK-mlda5vb-L_tHue05jtSr-4Tnk8rj4zmknhaWtvksUyA66dAOgbLQHI_ZHoJfYllCbPQ7J3HYi55CI1fPEJB4vMt2dl49YSdjc31PsNuNwGuTtW2OBXVpT-NpeKS6NLRdIRy1_chJMCrwURw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب کامبکی
عجب دقیقه‌ای
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/97525" target="_blank">📅 02:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97524">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">عجب کامبک تمیزی زدن
یکی از بازیای قشنگ جام بود واقعا</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/97524" target="_blank">📅 02:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97523">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">بالاخرههههههه زدننننننننننن کامبکوووووووووو</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/97523" target="_blank">📅 02:13 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97522">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">کامبک تکمیل شد</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/97522" target="_blank">📅 02:13 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97519">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">گلللللللل</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/97519" target="_blank">📅 02:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97518">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">گلگگلگلگلگلگگلگلگلگلگلگلگگلگلگلگلگلگلگگلگلگلگلگگلگلگلگلگلگلگگلگلگلگلگلگلگگلگلگلگلگگلگلگلگلگلگلگگلگلگلگلگلگلگگلگلگلگلگگلگلگلگلگلگلگگلگلگلگلگلگلگگلگلگلگلگگلگلگلگلگلگلگگلگلگلگلگلگلگگلگلگلگلگگلگلگلگلگلگلگگلگلگلگلگل</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/97518" target="_blank">📅 02:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97517">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">لوکاکو رفته پشت توپ</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/97517" target="_blank">📅 02:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97516">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GrwsK0LxUkAQgEeCErMXFCq3MeCLe2af8bTI8o8zaxcYA5jtC1459VtfVQVaB5MvlEQe31DzuIGZwut9WVqxDlJJMTAqg1HxS11ioc57FGU52TLqOefA-i8luEkSLJFbL8ApG99GBRzvh7PGrKw9a9e2260g2drwuLvwVQNYGQW2ka9gA8fvxiHTN6GgTgqC5ZAT3hDUoHqpRFml7MWwJQzj2yv8WDUeGcKeKGYAFMjPiqFNa-EH47gjhOW1ptAMfxKtZ_deGJZcV8-PdKQva98AG53Hf2x2U1b1x6U_-WOiT8WzfluEMPnb3duWlPRRc1wRYtMYVvag1MfT7AiYig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چه کااااریههههه ناموساااا
😐
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/97516" target="_blank">📅 02:11 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97515">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">خوابیده رو نقطه پنالتی بازیکن سنگال
😂
😂
😂</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/97515" target="_blank">📅 02:11 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97514">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">دارن کرم میریزن تمرکز بازیکن بلژیک برینه</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/97514" target="_blank">📅 02:11 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97513">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">دعوا شد</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/97513" target="_blank">📅 02:10 · 11 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
