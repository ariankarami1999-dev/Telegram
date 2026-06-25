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
<img src="https://cdn4.telesco.pe/file/uCb7hx2Dzou_75HvZLXsTiTbXPAPkbMpgvjmqJB6ymHLL_Y-ItsdQ-cWrg02nFfm_dk8hdYody03DhNy58PtgPZyjlwVo37KhhyIzKdZIU9QfQWdhcCkJZMyLSMzXxpiAQz6EsSsmExhmZcGB7INF8yJjywHM9XkRT84H325cRJVy6Qwx12G-YUHRhO8Z79SjPcon-3rI1rgw6vbrJEGR8ugCaQjI4IBc-ngcjsZup03izTW7J276RBzponngTcOC7gOLp8g6Z85JfGmTlgabq6pWVkQ3TCC1538Os4ZTy5xCbJcGfj-yyFRTHJHpEZC0IpcmOeCRDEdpxk-BaSQ9w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-05 01:45:57</div>
<hr>

<div class="tg-post" id="msg-444790">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c0e474c49.mp4?token=v-G_Es-mD_oToIhNd7gn6FvuwKU5pnGz-hNfhP5eaL36cUL50W8rj8UDhHHrh_7p896sZ6ws_keGiQbITrTWFY33RNRMMicBODfc3UMGEHuy47BGeO8zTiV7ZWjzrPkPjHOB-dkAeCKl62guAGS29dEMCTtT6cCvsviKOBebqordUlCYSBwPTZ3z2dEs-b74ua5rMWY8UpzPjrtVYx1pa8u4cRvmvQAR7732YbjEHO10eb0yu5OVCqy4H2qWHYVCMTFiWuVUTNKf2b-pKrheoW5XLPmR8N3vKa-jKKQBuK-mLUpqUJoIgV8Ye1-bNwJS9JIDrBPbfnWScLPrE-C_ZDALwxpJktPw-PGTWvGwJFMU__F1IpIFchJ3sIxM6tSjuZXC5cuBE0gP3LLYkVF3aaVYcPd3i0TFIhxoVvWFWM1B5vIEKWei7eW22BUnp4yITEN1OdqOZGzJg7kOSecVDbMW2pZVYGSQY8Uv5jxl9RG8lQrrK21I9TQJwdnzNU4-a4m8QJt1gLU9pxF9RMNEPl1ufh1TUVfFvHQcyEtQraVZaIUEqupJILvt-NEAXUFkZQ-DBvOynoCWrtrnYfD_w3K675CAmdStiJupQe0QFNB0JS-g6HUEVqxDqvFVIhHyriUciIs6QgHVSumZPW3CcVFOsLlva6Vvq_S49NpDQvk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0e474c49.mp4?token=v-G_Es-mD_oToIhNd7gn6FvuwKU5pnGz-hNfhP5eaL36cUL50W8rj8UDhHHrh_7p896sZ6ws_keGiQbITrTWFY33RNRMMicBODfc3UMGEHuy47BGeO8zTiV7ZWjzrPkPjHOB-dkAeCKl62guAGS29dEMCTtT6cCvsviKOBebqordUlCYSBwPTZ3z2dEs-b74ua5rMWY8UpzPjrtVYx1pa8u4cRvmvQAR7732YbjEHO10eb0yu5OVCqy4H2qWHYVCMTFiWuVUTNKf2b-pKrheoW5XLPmR8N3vKa-jKKQBuK-mLUpqUJoIgV8Ye1-bNwJS9JIDrBPbfnWScLPrE-C_ZDALwxpJktPw-PGTWvGwJFMU__F1IpIFchJ3sIxM6tSjuZXC5cuBE0gP3LLYkVF3aaVYcPd3i0TFIhxoVvWFWM1B5vIEKWei7eW22BUnp4yITEN1OdqOZGzJg7kOSecVDbMW2pZVYGSQY8Uv5jxl9RG8lQrrK21I9TQJwdnzNU4-a4m8QJt1gLU9pxF9RMNEPl1ufh1TUVfFvHQcyEtQraVZaIUEqupJILvt-NEAXUFkZQ-DBvOynoCWrtrnYfD_w3K675CAmdStiJupQe0QFNB0JS-g6HUEVqxDqvFVIhHyriUciIs6QgHVSumZPW3CcVFOsLlva6Vvq_S49NpDQvk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای شام غریبان در قتلگاه میناب  @Farsna - Link</div>
<div class="tg-footer">👁️ 693 · <a href="https://t.me/farsna/444790" target="_blank">📅 01:44 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444789">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03fd973e38.mp4?token=n76tLXzsvu_R2jH3v8FTuEsTZcKdN3spklwIYKOljmg2BU_Sc6juFjqnvh-olIioXqCI-Wg7FLl6YKLvs2908ogJf0b76cv6vDMsUcZq9AEfk6VPBHhxfoG54FrVVHWDB5r0DNF7KZXyrrhhwL3yCJyPxEmkvdx8EbwE37ggL9vZapQswrQuRXCSjEGxVQh2Q6kOkmx1Sj2gPaz1-yIEa9t5BXMy_N5gS6furQxpxNMUoHh6rFjECs4a17X8URurQtBdN3qb6WUulZNK4aw0NT0KLOWjCht9xKHkyeKx-MsA9gGTzD4QsP7GbiOPR4HlNEPMLejDJ5znZ1WDWnD8R1cwhF5K-pnmItkmyTEFBN-iI2ENIwQ0oi5xq0-260JDt_JSA3Ogfh2wHRvczRolov4bKOLrBGWRmIKPQdpHxyN9BIKUPwIgLdRQJrflTROXU2LEKnK1FCEplxnaAdndFjYlXTZVV5fJIAtvLGyuOikk3dRBQftmTsOpZF5KBOfav--GXUAMfI3Q5qd6hJ1iOWs4B5ODTSmIh-TASJ9_EtjPoNTcbsDIzSeJutdsYnzDeax5BvmxezuSSSzUvlzYKh4Blwaixa0bHlR1B5E7AtnRAX6MKv0P5NX3miwtK_3Hn54zc97u2vY1GtlGM-AHXX-28_8s39_KOeob9n2w6Ns" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03fd973e38.mp4?token=n76tLXzsvu_R2jH3v8FTuEsTZcKdN3spklwIYKOljmg2BU_Sc6juFjqnvh-olIioXqCI-Wg7FLl6YKLvs2908ogJf0b76cv6vDMsUcZq9AEfk6VPBHhxfoG54FrVVHWDB5r0DNF7KZXyrrhhwL3yCJyPxEmkvdx8EbwE37ggL9vZapQswrQuRXCSjEGxVQh2Q6kOkmx1Sj2gPaz1-yIEa9t5BXMy_N5gS6furQxpxNMUoHh6rFjECs4a17X8URurQtBdN3qb6WUulZNK4aw0NT0KLOWjCht9xKHkyeKx-MsA9gGTzD4QsP7GbiOPR4HlNEPMLejDJ5znZ1WDWnD8R1cwhF5K-pnmItkmyTEFBN-iI2ENIwQ0oi5xq0-260JDt_JSA3Ogfh2wHRvczRolov4bKOLrBGWRmIKPQdpHxyN9BIKUPwIgLdRQJrflTROXU2LEKnK1FCEplxnaAdndFjYlXTZVV5fJIAtvLGyuOikk3dRBQftmTsOpZF5KBOfav--GXUAMfI3Q5qd6hJ1iOWs4B5ODTSmIh-TASJ9_EtjPoNTcbsDIzSeJutdsYnzDeax5BvmxezuSSSzUvlzYKh4Blwaixa0bHlR1B5E7AtnRAX6MKv0P5NX3miwtK_3Hn54zc97u2vY1GtlGM-AHXX-28_8s39_KOeob9n2w6Ns" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گچساران یک‌صدا با زینب(س) در شام غریبان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/farsna/444789" target="_blank">📅 01:35 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444788">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YcyaVsenTo709tzXZ73qayOwkzuwKvs98bCyygrrfJpl4XqkOxWBScZf1pwyY8nt7rasgMzdbHIbaqM3Ofah_ChCC8o05_VC8pu8hvLyZ_ovQ692tVz38JTy27qbdP4jcesQF6wCDFPMh3vKD6v5g378nBrT42Gdw-qmzbONsp3u2oizuo9R01o2Zple-yi8js90bCQq6eDVzwnSKRi2Yel1mW14kn2-WlXiEan3xVpFRP8iDWKGgrf2cnM8JdpFOzu8cNa0NImT4fqQ6lmo_kYQhaYaAJMlR1ZX-sIqgPtMuWFFL6Ie2mFDqO8ah0j5w4ynPxq5jTcSuYMQN_RxBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکوادور غول‌کشی کرد و به‌عنوان تیم سوم صعود کرد
شکست ناباورانه شاگردان ناگلزمن مقابل اکوادور
آلمان ۱ - ۲ اکوادور
@Sportfars</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/farsna/444788" target="_blank">📅 01:34 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444787">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YDONam7NfI_2Z8g7EgFioFs4Z4G10qgM2ESIQti6DjFip-tAsQLNlnD8ZV6c8XddbC2Z6VOYVaDLyouMR-aaJe1jG0T4T16AYmD8TTkrgTrXtRC0DTh7pCZqxiTOtfGzxkxYZJT6fYOBzYhNRi0rt1pIC04qTynDUA4EWqH9Ml3ZlGYW_PjsrU1nqhvDEg0g4WT8jjwGHEbSuRFoO6LckY0jxB_9EdNkMsDyM66G7SKEZfUT21znzYTnu5VSJxbA1NvU1Ppweb70Izo5JB9NGjFcYTCtfDy4Z3UK2Z-JS1u_BS5xiDTMeBKB2ZsL3ZPw9crz5tR48V2l8Z64yW2vcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساحل‌عاج مقابل تیم ضعیف گروه پیروز شد
⚽️
ساحل‌عاج ۲ - ۰ کوراسائو
@Farsna</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/farsna/444787" target="_blank">📅 01:34 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444786">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b942a47af.mp4?token=TVwwm2i8ZfhwA0-7jCjjzvrGuXMFgc66i9qU7YjF4FnykDxt9eYJ_p09L-xWxrWfmInyq6jTIhRMU068mGQoNz6ofUPNX_UG40kYeaWjoCHZh0zPjTYbJ-jkz6n4hbRSE0Y6Y0Wr0Zt6XIGDSceDrpWI98xJcPbklGPgW4I9pr-7Vf1NpAoa_G_JLDQqtpJZ_AfwXlARwPKs-gXvxtPOKNWhuZM3wULoAuTBQ_nFeCNXNnB9mf_G9DhCS12Hkom3PXNpB_iv5SrKRLdyP_LgNt7jzXjUxT4f0meL5egP1JnJJI07wgwUJ_8SNa-7Gx4e_M6dPFK7YVvYnNHPUk7H_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b942a47af.mp4?token=TVwwm2i8ZfhwA0-7jCjjzvrGuXMFgc66i9qU7YjF4FnykDxt9eYJ_p09L-xWxrWfmInyq6jTIhRMU068mGQoNz6ofUPNX_UG40kYeaWjoCHZh0zPjTYbJ-jkz6n4hbRSE0Y6Y0Wr0Zt6XIGDSceDrpWI98xJcPbklGPgW4I9pr-7Vf1NpAoa_G_JLDQqtpJZ_AfwXlARwPKs-gXvxtPOKNWhuZM3wULoAuTBQ_nFeCNXNnB9mf_G9DhCS12Hkom3PXNpB_iv5SrKRLdyP_LgNt7jzXjUxT4f0meL5egP1JnJJI07wgwUJ_8SNa-7Gx4e_M6dPFK7YVvYnNHPUk7H_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شام غریبان حسینی در صحن و سرای حرم حضرت عبدالعظیم(ع)
@Farsna</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/farsna/444786" target="_blank">📅 01:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444785">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8fde42a79.mp4?token=gbNexGx27vFppHWKglebIlR7uvuZ8p6qfB1BXJM4GAjsA0IkE_1V2noww8WS-IX3dk6Ghx2Hgqr4t-i4rk9fvUCys8DJIR_ssiyeS7AM0o-eHcA1e0Sf6zW28hVOYskNzjQvxk5MXnx-Mo8O2W-vmtYkDV2nionv8mFabGoN16f875plR6UtfZREERDtxnC8b_jRqtlyajLIIGc_IVHGlZ_wQAVaIHIOQ8FKa0Ok6uuFKAMgPndRo0qE55fN5JUZ7rWwc4QOFhgxrXMcKu5dRb27wOoY0wsY3fq1GMl8iR-Y4qVxfkF26f6b5B_SmkXZjyLo-IKLeNVjIFfRSpgiAFTFsUKDZLQOrO13MnmUtQtdO90-bLHsDRMSn4puq7w3jWn1Fd_iuFaX26CBMPL382M_iJavkEP_BxQXATNMyJqZgtQrkaphxzsNX-8kWJ2hWr7BLiZcOHe3nfKHk-xoxjMSjkuz3iiDuFUCxtMCcgYgyeHoEm03WHuoy--aZePeWMV7US8ps63BNOz2pRuWuLMXTiGt8XCGpdB3mJaPbt8cVUzaxb1qzAfTyJ6tj7TSSs64TnDdCZY7QNn4GGjcNpGNoZWbRswxCeRZ9OhKDeRiSMlOFxD9wLbADwf8e2xTIgro5Y-X-lTOGmNdResmbQRaajNaz6Iu4Uuw8CYb1gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8fde42a79.mp4?token=gbNexGx27vFppHWKglebIlR7uvuZ8p6qfB1BXJM4GAjsA0IkE_1V2noww8WS-IX3dk6Ghx2Hgqr4t-i4rk9fvUCys8DJIR_ssiyeS7AM0o-eHcA1e0Sf6zW28hVOYskNzjQvxk5MXnx-Mo8O2W-vmtYkDV2nionv8mFabGoN16f875plR6UtfZREERDtxnC8b_jRqtlyajLIIGc_IVHGlZ_wQAVaIHIOQ8FKa0Ok6uuFKAMgPndRo0qE55fN5JUZ7rWwc4QOFhgxrXMcKu5dRb27wOoY0wsY3fq1GMl8iR-Y4qVxfkF26f6b5B_SmkXZjyLo-IKLeNVjIFfRSpgiAFTFsUKDZLQOrO13MnmUtQtdO90-bLHsDRMSn4puq7w3jWn1Fd_iuFaX26CBMPL382M_iJavkEP_BxQXATNMyJqZgtQrkaphxzsNX-8kWJ2hWr7BLiZcOHe3nfKHk-xoxjMSjkuz3iiDuFUCxtMCcgYgyeHoEm03WHuoy--aZePeWMV7US8ps63BNOz2pRuWuLMXTiGt8XCGpdB3mJaPbt8cVUzaxb1qzAfTyJ6tj7TSSs64TnDdCZY7QNn4GGjcNpGNoZWbRswxCeRZ9OhKDeRiSMlOFxD9wLbADwf8e2xTIgro5Y-X-lTOGmNdResmbQRaajNaz6Iu4Uuw8CYb1gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تجمع بزرگ عاشورائیان بندر امام خمینی(ره)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/farsna/444785" target="_blank">📅 01:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444784">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c42d828f9.mp4?token=PG95Z0z-xuUGzjgwte5xfUUg1URF6V_ukb35BrByZHEoU4YctDI8QTTjG-JiHNRQ8aLVIOAJsOUXwvwhnkDgR4TFR0aKSm7eLE_xa2QhGYscXpacjPiS1qOQzQVGFtI3oTU6FTarY3AgR5shiIGFSqSL_PUtPMRXZ-k-g1g9PzcL4jsoB62BP_65aUmQyjqXNOaOKygfiWoaBWTmi95C8I-lrS6JPMDDYef5yVwOeKsXyCaVEHNgQ1uXHRx0aLpXzMTLzzBbC5oIVwiAi-AHmvEL1Da1sYAExjgldjruY5aPlQnpc_u2Bskp26w-4eh7R3RFzGQat_6a2lxMaOMScg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c42d828f9.mp4?token=PG95Z0z-xuUGzjgwte5xfUUg1URF6V_ukb35BrByZHEoU4YctDI8QTTjG-JiHNRQ8aLVIOAJsOUXwvwhnkDgR4TFR0aKSm7eLE_xa2QhGYscXpacjPiS1qOQzQVGFtI3oTU6FTarY3AgR5shiIGFSqSL_PUtPMRXZ-k-g1g9PzcL4jsoB62BP_65aUmQyjqXNOaOKygfiWoaBWTmi95C8I-lrS6JPMDDYef5yVwOeKsXyCaVEHNgQ1uXHRx0aLpXzMTLzzBbC5oIVwiAi-AHmvEL1Da1sYAExjgldjruY5aPlQnpc_u2Bskp26w-4eh7R3RFzGQat_6a2lxMaOMScg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رزمایش هوایی مشترک ترکیه، مصر و جمهوری آذربایجان
🔹
وزارت دفاع ترکیه از آغاز برگزاری رزمایش‌های هوایی مشترکی با مصر و جمهوری آذربایجان خبر داد، این نخستین بار است که چنین رزمایشی در آسمان ترکیه انجام می‌شود.
🔹
این رزمایش حلقه‌ای جدید از همکاری میان ترکیه و مصر به شمار می‌رود؛ دو کشوری که طی هفته جاری رزمایش‌های هوایی مشترکی را در مصر به پایان رساندند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/farsna/444784" target="_blank">📅 01:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444783">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fb90483b0.mp4?token=APWoI0mPdtfzfWh-idL1PJ6X2ksIdHmMSsTBTxWVXYn3Kr6Iujqdb7LlbAOZaEvxWGhilM3Px_pOyzenpR30oai-VnuL-ZHFFmLBau02eomxGupWn4Z68PP8BJ_hb5wDXySV_Z4fnlMitFBil_8SivppuF3OVzsT7jjvip7Cf8Og3U1G1Tv9HWI8ekV1GBrzU2joALDCwc2q1maPSO4qW1KaWEaMPrinuxO82aHhfwQjBJm8Rx0V2Rf-imFxnx1PCbAW1Q0tvuRwkGBSZOcXz1TuhXHE9pM4IVKCmOZ-b_e3QnMH3s5nJMZWeHKsxjEkwKK6GChTjY25aS5FOgtJ8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fb90483b0.mp4?token=APWoI0mPdtfzfWh-idL1PJ6X2ksIdHmMSsTBTxWVXYn3Kr6Iujqdb7LlbAOZaEvxWGhilM3Px_pOyzenpR30oai-VnuL-ZHFFmLBau02eomxGupWn4Z68PP8BJ_hb5wDXySV_Z4fnlMitFBil_8SivppuF3OVzsT7jjvip7Cf8Og3U1G1Tv9HWI8ekV1GBrzU2joALDCwc2q1maPSO4qW1KaWEaMPrinuxO82aHhfwQjBJm8Rx0V2Rf-imFxnx1PCbAW1Q0tvuRwkGBSZOcXz1TuhXHE9pM4IVKCmOZ-b_e3QnMH3s5nJMZWeHKsxjEkwKK6GChTjY25aS5FOgtJ8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
میان‌داری مهران غفوریان در مراسم عزاداری امام حسین(ع)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/farsna/444783" target="_blank">📅 00:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444782">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🎥
نخل‌برداری مردم تفت در قاب دوربین
🔹
هزاران عزادار در تفت یزد با به دوش‌کشیدن نخل، بار دیگر سنتی چندصدساله را زنده نگه داشتند؛ آیینی که یادآور تشییع پیکر مطهر سیدالشهدا(ع) است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/farsna/444782" target="_blank">📅 00:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444781">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e7c8a296d.mp4?token=mjLISo-vY1GPSBObRL3o3jEsnS4VQBvQ7FVKfZbkaZkqOpKlGx2-f-fMkVlVnx_ZIorJwRlwRe37QGDxjNQRoM6bUdnStfmFwfyCSzG4P_FZGs0L09jh0qITm2KTCI3-ghNkuphsY4a04CY3pJq147qEyAdNs69uFPIb_6YG4c0MrNTxFopKlGETOPhb2Frxd8erLR8JYdZFCohDoOLoFQjfC_mEL_wQt-OGOb_a0owED27L-JmM513cz6pB0l4zqYJ_ta3VJHVShBJRH6J99zhuu_n2fnEDGkGBAR-Yo1rgxdAsIXAttg8czE25j59N1-elcxxCuOs8ldpL2zWQrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e7c8a296d.mp4?token=mjLISo-vY1GPSBObRL3o3jEsnS4VQBvQ7FVKfZbkaZkqOpKlGx2-f-fMkVlVnx_ZIorJwRlwRe37QGDxjNQRoM6bUdnStfmFwfyCSzG4P_FZGs0L09jh0qITm2KTCI3-ghNkuphsY4a04CY3pJq147qEyAdNs69uFPIb_6YG4c0MrNTxFopKlGETOPhb2Frxd8erLR8JYdZFCohDoOLoFQjfC_mEL_wQt-OGOb_a0owED27L-JmM513cz6pB0l4zqYJ_ta3VJHVShBJRH6J99zhuu_n2fnEDGkGBAR-Yo1rgxdAsIXAttg8czE25j59N1-elcxxCuOs8ldpL2zWQrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور رئیس‌جمهور در مراسم شام غریبان امام حسین(ع) در ارومیه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/farsna/444781" target="_blank">📅 00:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444780">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1167de7231.mp4?token=kaKlUqaMq6D71jFQlaXUsJItlmcq9afqbU4W-45QJK6kaLB6NvCk270aXPV26bUStOgUcOeAuwD6pa6N-l2NXBxD32HWGCFobfVEsY8-RUcjWPSGVNJeu6S5AfgzdcXZJvdpxCuGRipDAsHkBMdg8BKtQ49bYwN1aiqEeCwQowx9qmgUo1yOL2ohL3RWsZ-IIqKv-hIWaYEBDuLtltA4LEdJ1EY6rxqbJEh-6W0r41RuKTUoVm4ofyMySPlEMM0HJyyennWIliFVvhiAqFDT3UnxaCaTw4jcBdPfk-FYTIrWM1lV0Es5_7m6BFOvQKgaSAcroQyd5UVKn_zC2EMfYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1167de7231.mp4?token=kaKlUqaMq6D71jFQlaXUsJItlmcq9afqbU4W-45QJK6kaLB6NvCk270aXPV26bUStOgUcOeAuwD6pa6N-l2NXBxD32HWGCFobfVEsY8-RUcjWPSGVNJeu6S5AfgzdcXZJvdpxCuGRipDAsHkBMdg8BKtQ49bYwN1aiqEeCwQowx9qmgUo1yOL2ohL3RWsZ-IIqKv-hIWaYEBDuLtltA4LEdJ1EY6rxqbJEh-6W0r41RuKTUoVm4ofyMySPlEMM0HJyyennWIliFVvhiAqFDT3UnxaCaTw4jcBdPfk-FYTIrWM1lV0Es5_7m6BFOvQKgaSAcroQyd5UVKn_zC2EMfYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای شام غریبان در قتلگاه میناب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/farsna/444780" target="_blank">📅 00:36 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444779">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">کتاب آه</div>
  <div class="tg-doc-extra">قسمت ۱۱</div>
</div>
<a href="https://t.me/farsna/444779" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">قسمت ۱۰ – کتاب آه</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/farsna/444779" target="_blank">📅 00:32 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444778">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">حزب‌الله: ارتش اسرائیل ۲ غیرنظامی لبنانی را در جنوب لبنان به شهادت رساند.
@Farsna</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/farsna/444778" target="_blank">📅 00:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444777">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62f86a659f.mp4?token=HivBmWex_UdfYRyLS9e214TBJFEq-hwNe8cFFkzLaMZNAwauBRso2Y296wvT9vyxOHlbKM08VI8iXIPhpe3l3fyFhcqlskmtx1hB3MxhjiKb1a55NEaI69kSiOwguRtW7isIDXHduTiwvd_8OZTJEAFN-CSV-00OwAO1FhZBsLHHMYXMWJPUfZLb0TG_ymUQwG2kjUNpKYqVKgTqfrOUYTWinl5ybjhBr5S-65mgQcMT4FOlJ47FJKGMK_WxmCgm7IEL1tr0p4mdFbErNskX6EBKYYoe2QavT2yUIBfKrEqK5ctGI9YGgIX90OGDBwaJaHGDQnyKYs41c4jPTkYQGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62f86a659f.mp4?token=HivBmWex_UdfYRyLS9e214TBJFEq-hwNe8cFFkzLaMZNAwauBRso2Y296wvT9vyxOHlbKM08VI8iXIPhpe3l3fyFhcqlskmtx1hB3MxhjiKb1a55NEaI69kSiOwguRtW7isIDXHduTiwvd_8OZTJEAFN-CSV-00OwAO1FhZBsLHHMYXMWJPUfZLb0TG_ymUQwG2kjUNpKYqVKgTqfrOUYTWinl5ybjhBr5S-65mgQcMT4FOlJ47FJKGMK_WxmCgm7IEL1tr0p4mdFbErNskX6EBKYYoe2QavT2yUIBfKrEqK5ctGI9YGgIX90OGDBwaJaHGDQnyKYs41c4jPTkYQGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شهیدان حاضرند
حضور و غیاب شهدای ناو دنا و جماران در شب عاشورای حسینیه معلی شبکه سه
@Farsna</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/farsna/444777" target="_blank">📅 00:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444776">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VGcFL0d-GtSa6QVDvB4yaltWMuOEkqr-UTraGNLr1jjrsvO5Ga4vaFXuy930cdANZ4jc3_hd3Scdp36x8eIEJ5B-K3YMt1e-d1MCIe8LeNra704pgSAq7bkx6a6Iw14vvUx9FS9FIPA-aDqzDo4Ympo6vaQg4URyVkI3ZSzN5I_J6hYuvJow92deGXcArFwfsdnZdYUeoorE0psTyu7gy1DZ39kHf5Npc_ItB2mmsrQolMVht3PmWQ9qsUJ81qQU9u50ktd-vuMZMjN6fWy3ANMUB0Vroo91REkeZrEiN6n5kVJaNhRB_LBk0AnH8Dgl-QpS3PUbA1oREbYdg2zr5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایمان و همسایه‌آزاری
🔹
مردی از مسلمانان انصار به حضور رسول خدا(ص) آمد و از دست همسایه‌اش شکایت کرد و گفت: «ای رسول خدا، از آزار و اذیت‌های پی‌درپی همسایه‌ام به تنگ آمده‌ام و در خانه خودم آرامش ندارم.»
🔹
پیامبر(ص)، علی(ع)، سلمان، ابوذر و مقداد را فراخواندند و مأمور کردند که پیامی را به گوش همگان برسانند و با صدای رسا در مسجد بگویند: «هرکس همسایه‌اش از شرّ، آزار و بدی او در امان نباشد، ایمان ندارد.»
🔹
سپس رسول خدا(ص) فرمودند: «از هر طرف تا ۴۰ خانه، همسایه محسوب می‌شود.»
@Farsna
-
#حکایت</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/farsna/444776" target="_blank">📅 00:04 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444775">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">نجات ۱۱ کوهنورد در اشترانکوه لرستان
🔹
مدیرعامل هلال احمر لرستان: ۱۱ کوهنورد گرفتارشده در ارتفاعات اشترانکوه ازنا با تلاش امدادگران نجات پیدا کردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/farsna/444775" target="_blank">📅 23:59 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444774">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">حمله توپخانه‌ای اسرائیل به جنوب لبنان
🔹
شبکه المنار گزارش داد که توپخانه ارتش رژیم صهیونیستی مناطقی بین دو شهرک بیت‌یاحون و برعشیت‌ را مورد حمله قرار داد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/farsna/444774" target="_blank">📅 23:42 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444773">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KRoFLlJx2gGtQaUo7QoMiST7rgyVxbLV1l9TBqgZiwG4W6rEdhzKQJaLLrvlUxutBXpvC3XpSjpxYGzKB_uMuC7nnyal0YgClDwTgHBRWgpaBcHXHXjJcTpCC9kE5Xm1lbMQ-9DWVBWjCaBtq_emDY3jIqx_lLxMZuuzu5GBIONG2a98z00gsHtAwsMsR7d-a7v668CRd2blPw9AWSw_H7at4KkDBgVpU_6mfXvgydoqes4Yk3pqH2WYi32oTklTevmmJNorFRdQCKjRg6cGXHNGUqUsw2PYUWh73T8j_Cj00TNWvcfuszRK9fqttuVJbbx0jn7HVQvJGYDxtM_Ipw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر انرژی آمریکا: تحریم‌های نفتی علیه ایران بی‌تاثیر شده بودند
🔹
کریس رایت، وزیر انرژی آمریکا امروز در پاسخ به سوال خبرنگار آمریکایی مبنی‌بر دلیل برداشتن تحریم‌های نفتی علیه ایران، گفت تحریم‌های نفتی علیه ایران عملاً بی‌اثر شده بودند.
🔹
او بر همین اساس اشاره کرده که صدور مجوزهای عمومی برای صادرات نفت ایران امتیاز چندان بزرگی محسوب نمی‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/farsna/444773" target="_blank">📅 23:35 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444772">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b_Qb85TfmEUQiLTVAhMoPG-zqT8zelE9MzVaYtc8vwT5Pvkv0jtZtuEdmpekDG5MXoWyjGyD3cCg4BeJCWNnW3XcwKz5GiomkZlaH6D_Iq1Z8YNXIkM2GJWhtCz48O5xRyV9ocwW-pxobxsb4bBQHgHjy-FZRqM0pV8oY0rDNr7YruC5sR_j2XinWdgyPzU4MqYN7Dnmih_cUvS2qLkn3MZAobDkpr9URNMHMivUx3X1F6tufP6czNwbMb3_xVr1x8S0mneb24Wp0WXIvlNFT19_JG2ABGaPx8yUMCXzT-x9KmurxxxLT6fPGZMAt2W53ylMG0sKENndn3G7_JM98A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
مهدی طارمی: وقتی مردم زیر موشک بودند فوتبال دیگر هیچ اهمیتی برایم نداشت. ترجیح می‌دادم در زمان جنگ در ایران می‌بودم.  @Sportfars</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/farsna/444772" target="_blank">📅 23:16 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444771">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CDdTuDnNxmdshGr4aP7pJGhFhgpbaZ6Z70fhU3vWLiKH7x7PXTezlY0zfmQr-qMyYu3xu99DXpLT1dl0sKrCSblzb6ftIigFBkLMMtg5CgvOhE36oTJOUR3ItUt2OgB4Eavc8gJ334qb6tGS0w6h7JKN1z5n0aJjK-MF1NP6IM4hrGyHicT8A4lAUbF4yt1yyjVuEUT54ytltl0s1oeEV6yTB-TsWaTLfVE9181PIsZVHd1OvQbFhednZcDEj71cN8JGZYiIsdlMZe4h3wBSv0Ag8BRhISiVX6tQQnXDtuqJZPfOcImzISMxSKh8bXptJBk-BjfDpZ4LaOVDbsNi3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«پادماده» رویای سفر میان‌ستاره‌ای را محقق می‌کند؟
🔹
استفاده از «پادماده» برای پیشرانش فضاپیماها بار دیگر مورد توجه قرار گرفته؛ موضوعی که از حمایت ایلان ماسک و جرد آیزاکمن، مدیر ناسا، نیز برخوردار شده است.
🔹
پادماده نسخه معکوس ماده معمولی است یعنی به‌جای پروتون، نوترون و الکترون، از پادپروتون، پادنوترون و پوزیترون تشکیل می‌شود.
🔹
هنگامی که ماده و پادماده با یکدیگر برخورد می‌کنند، هر ۲ نابود شده و مقدار عظیمی انرژی آزاد می‌کنند؛ انرژی‌ای که از نظر تئوری می‌تواند برای به حرکت درآوردن فضاپیماها مورد استفاده قرار گیرد.
🔹
بااین‌حال مانع اصلی در این مسیر عملیاتی‌کردن این فناوری است؛ کنترل انرژی عظیم تولید شده از واکنش ماده و پادماده همچنان یک چالش بزرگ علمی و مهندسی محسوب می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/farsna/444771" target="_blank">📅 23:11 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444770">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a9j2BuJPupJrvitDU2irTk0jw8TNi2IgszR3N51XkBabo9nML48qtXf_il1epVEaKwDtW5bl6CoVesJjr0e0_FTg6MfZkQuR5q_sklJv3AOppp7CruuHakh6hjcvEirbu0J6L_At6K5w39hR0TEt4JHH-DUAy2beEjV2hzXf02bofUUDCK80Bx6Sb6fjy5_igrv477RaoPoEiugL7Q-53XqmPLS6cdI6yw0H2rfC3AsJZgRdK5qPBtPPYMithW-1lYX64oniTygsR9P4fomULo0k8pxLqJZ1JPYisogh-q39OXmmfe3uE7Zi7Xr9OXZajc-QvmRNgLYkDHMGtb-hCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
روضه‌خوانی مهدی سماواتی در مراسم شام غریبان حسینی(ع) در جوار محل شهادت رهبر شهید  @Farsna</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/farsna/444770" target="_blank">📅 23:04 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444769">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O5_GI2wAtJy69Fnyaz6ENL4PLS0hIEG7_w6YM6SdwqXt-tfBMQAAd6lNagzEteo4shBWrXBtBxHKzIgXMNw6Nk42aC_VPQin5xXPG7r5hVM2UF3JyAZgYzw0EH-8XIq8WRmUZSy0TvyEHwxKihfaruhL2NvnlM_f9LtSp_bA72fM23esICueKQxPq1c9Q-lRZ3fhblzDqDT1BQXvleJ4PrqnUDypSW-AqxLrB-HS0Ocf28ZiyvSVfSJUhjJ2Dwg44GMMrj89ThpF-kod2_IfdFmOroiGBpjGs6VZMnHmOLKbV95Z6npg0gJV74Q4R3T7RLC9DSwMHfC4ftqTuKHPLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آتش‌بس در جنوب لبنان کماکان نقض می‌شود
🔹
ارتش رژیم صهیونیستی مدعی شد که ۵ نیروی حزب‌الله را در شهرک زوطر شرقی پس از نزدیک شدن آن‌ها به نظامیان اشغالگر هدف گرفته است.
🔹
ارتش اسرائیل همچنین عنوان کرد که نیروی هوایی این رژیم یک نیروی حزب‌الله در ارتفاعات علی الطاهر را مورد هدف قرار داده است.
🔹
شبکه المنار هم گزارش داده که نظامیان صهیونیست با سلاح‌های خودکار به سمت شهرک بیوت السیاد در جنوب لبنان تیراندازی کرده‌اند.
🔸
این درحالی است که طبق بند نخست تفاهمنامه آتش‌بس میان آمریکا و ایران، جنگ باید فورا در همه جبهه‌ها از جمله لبنان متوقف شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/farsna/444769" target="_blank">📅 23:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444768">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84ddbb7c13.mp4?token=o9L_JXeolcFf44vMi_gmjEDQyc6T0cAs5g0U2eE_RTQgBwA_dWo-CR5nh9uBvooA8QyVtZxTn5bEOfYfDdSlGn8A1ITbugCM9K4h7W1Afv0W_7etnAPgjvSGQdsXmXwE-yPL9WN4pvrJdWzsHExrsTiW2UlLbQ4ITrqvJEoaqSKFVXajdZ8NuxOAlAVIvbIbQs4J-dT9gC_5uyvqRV-8GMxf4bo7AuLq-1On432Cg79WJLIrVci7ql2w13gW2W0Qt0FzFq3QhIdPmDYrcB6cMBbToWrc3Dr1LZmWFtlevnvXzVCvBJyoZJuLrWGcZk4gvfmZW0LJhusTqiGZ3nvHDcAkG88JFShOYaGSDdKFKflzF4OT1Zd6TD0DUj5PIwzFpP-qexPISnegewl6AmQy8MCQs5tDrtXXlOt00nhZwory5ga-FBsham8AFg72itYkMHlZQu5iq62zIJjOCRrgqndWP6rKLKCS_dnRc70VvyB8NeO-EJHIWF7Ygcx8lpQoe7D-NQp9oJhTpc2lM6QCA8p1lm8etjZBmFh_GA4W5Md9xdQ5QdH5ko8naSBV1qNiZEZo0KWHwJTZ-N_CLWMxrvJlu3eXjSddWvksN3kHiVQYbwmkGfbojH8OgL1P_8-GXvMUW_SU8e0rUVaE2pfOffJOfsGrF7mwGxsQOWAC2Y0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84ddbb7c13.mp4?token=o9L_JXeolcFf44vMi_gmjEDQyc6T0cAs5g0U2eE_RTQgBwA_dWo-CR5nh9uBvooA8QyVtZxTn5bEOfYfDdSlGn8A1ITbugCM9K4h7W1Afv0W_7etnAPgjvSGQdsXmXwE-yPL9WN4pvrJdWzsHExrsTiW2UlLbQ4ITrqvJEoaqSKFVXajdZ8NuxOAlAVIvbIbQs4J-dT9gC_5uyvqRV-8GMxf4bo7AuLq-1On432Cg79WJLIrVci7ql2w13gW2W0Qt0FzFq3QhIdPmDYrcB6cMBbToWrc3Dr1LZmWFtlevnvXzVCvBJyoZJuLrWGcZk4gvfmZW0LJhusTqiGZ3nvHDcAkG88JFShOYaGSDdKFKflzF4OT1Zd6TD0DUj5PIwzFpP-qexPISnegewl6AmQy8MCQs5tDrtXXlOt00nhZwory5ga-FBsham8AFg72itYkMHlZQu5iq62zIJjOCRrgqndWP6rKLKCS_dnRc70VvyB8NeO-EJHIWF7Ygcx8lpQoe7D-NQp9oJhTpc2lM6QCA8p1lm8etjZBmFh_GA4W5Md9xdQ5QdH5ko8naSBV1qNiZEZo0KWHwJTZ-N_CLWMxrvJlu3eXjSddWvksN3kHiVQYbwmkGfbojH8OgL1P_8-GXvMUW_SU8e0rUVaE2pfOffJOfsGrF7mwGxsQOWAC2Y0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شام غریبان حسینی در میدان فاطمیه کرج
@Farsna</div>
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/farsna/444768" target="_blank">📅 22:45 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444767">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc4a0c646f.mp4?token=jQUIhhUP1VxTrdWGGBbkZtoLU8V0smQPYZ6X9BSsotKxo0yL7yxKpnPb2zhPpSOOKpq8_mBXLa6S4nnAuZwIAt2IxD5AZIEiutwdJ275TImeaNLlId7vALTbhPBjGjM86Pnb2c8F9f8aKJ_E0_D7Psgf9-pVNJjBl7DOafHaReNiQTgo5DNF5gHSY8pEJ95hYwjF0eyEN617ZpoKO3s0f8ThSqj2XgwWOT2ktjf7J17Zs8zYDpMGmrMl92m25nDe8ai-0U0jazDnAPNhCXtEa8xQ57BY1ZZhm8OHtoXGHdxHlGutRNc3Bfu-v_v_5s2u_23NV-0TrL6TmJP-RiGAwZLzZuAMVmq_oIn2RSko4aYkHCjut0lVOyL_TUYOixUou9tw7OVy0cRoTHJoNqDw3BtUG3Qe9Imtahq_OplJydAyaRJFQ-JF_REFnvkF6JgT-cE4kDJ5VFYrJSvNpxwUCIf0FvWoTt8jQ_--4FdXcWK5JG-pyWpGrBliwm_6ocblR1o3MT3x-7qFxR6eKpERQIWx6ZewmGcOss9Be4hnhQ4F4NBb3Nbza2hHa2qu8opKLWdNzZ8vsqXuBukzvfz11nthe1jkbg7OoYFMWZgwvC1NqB1s2fbxeAmNZCA_3_keFQiGHt8i1IyzBq8yB6UjFmksdPe7oLpmdx1CsCkUKp0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc4a0c646f.mp4?token=jQUIhhUP1VxTrdWGGBbkZtoLU8V0smQPYZ6X9BSsotKxo0yL7yxKpnPb2zhPpSOOKpq8_mBXLa6S4nnAuZwIAt2IxD5AZIEiutwdJ275TImeaNLlId7vALTbhPBjGjM86Pnb2c8F9f8aKJ_E0_D7Psgf9-pVNJjBl7DOafHaReNiQTgo5DNF5gHSY8pEJ95hYwjF0eyEN617ZpoKO3s0f8ThSqj2XgwWOT2ktjf7J17Zs8zYDpMGmrMl92m25nDe8ai-0U0jazDnAPNhCXtEa8xQ57BY1ZZhm8OHtoXGHdxHlGutRNc3Bfu-v_v_5s2u_23NV-0TrL6TmJP-RiGAwZLzZuAMVmq_oIn2RSko4aYkHCjut0lVOyL_TUYOixUou9tw7OVy0cRoTHJoNqDw3BtUG3Qe9Imtahq_OplJydAyaRJFQ-JF_REFnvkF6JgT-cE4kDJ5VFYrJSvNpxwUCIf0FvWoTt8jQ_--4FdXcWK5JG-pyWpGrBliwm_6ocblR1o3MT3x-7qFxR6eKpERQIWx6ZewmGcOss9Be4hnhQ4F4NBb3Nbza2hHa2qu8opKLWdNzZ8vsqXuBukzvfz11nthe1jkbg7OoYFMWZgwvC1NqB1s2fbxeAmNZCA_3_keFQiGHt8i1IyzBq8yB6UjFmksdPe7oLpmdx1CsCkUKp0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تاکر کارلسون: مردم دقیقاً برای جلوگیری از جنگ با ایران به ترامپ رأی دادند
🔹
تاکر کارلسون، مجری سابق فاکس‌نیوز و از چهره‌های تأثیرگذار جریان راست آمریکا، در مصاحبه با شبکه اسکای‌نیوز با انتقاد شدید از سیاست‌های دونالد ترامپ در قبال ایران گفت که مردم آمریکا دقیقاً به این دلیل به ترامپ رأی دادند که از جنگ با ایران جلوگیری کند، اما در نهایت دقیقاً همان جنگی را گرفتند که وعده داده بود هرگز رخ نخواهد داد.
🔹
کارلسون که چندی پیش از حزب جمهوری‌خواه به دلیل حمایت بی‌چون و چرای این حزب از اسرائیل خارج شده بود، در این مصاحبه تأکید کرد که وعده‌های انتخاباتی ترامپ درباره پایان دادن به جنگ‌های بی‌پایان خاورمیانه، نقض شده است.
🔹
او که پیشتر از طرفداران سرسخت ترامپ بود یادآوری کرد که ترامپ در زمان تبلیغات انتخاباتی گفته بود که رأی به بایدن یا کامالا هریس به معنای رأی به جنگ در خاورمیانه و جنگ‌های بی‌پایان است.
🔹
کارلسون در ادامه با اشاره به جنگ ۳.۵ ماهه آمریکا با ایران و هزینه‌های گزاف آن، آن را یک «
شکست تمام‌عیار
» برای سیاست خارجی ترامپ توصیف کرد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 7.51K · <a href="https://t.me/farsna/444767" target="_blank">📅 22:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444760">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l36Np8Q_dJb-zTEH5NLt5vm-CdQQflla1rmH7FoGEWul9fnE3JA80z_bgbpCqJRAJFlphmQXCKBnOT46ezKGVH-Z-iBSToX26k_VJw9iNPvnCuHuMhzayzmYL57zFtcHOOhjaoqYuIrEVvAtvk6dEX7NK2L52YWQaGfu2NNDYf7XuVXhtm5o-Bf7QgDkzkz7IW41I1x0oM1P2C3faHTMXVkEpXXs4nyhprNi9b3gS-cIAgL1VsolG8CqmJl1A4cdXnxPjQFsWSGzPyZV1cIkHLDAoDkaYSmLs5hIgTG08C5ShK8XIxnjzoMnmc0H-aqx3YSwVUBH2GrC8oI_UxFSSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s9yfw2fCjz4WU6f8wdy9oUEL83lYADeleHxtYDBXRu2dCoj4SsO_c0eCHTGYbx7Dudb7DRElSSuKnnKf1PBiDGjedTAViGqH3XNRwHrhbiU69pkF5ruGOGtOvjs3GVUI9yWI1wFS2j-dO6-z2XIWfACfZfTgYaUAlX9SIx35h8nMRmDi-nJerxPQraUt-x67fCPWnLu_xZA0NbJRILbCeWNYvBHTMS8Ru5Qhg9sMm9hQm3VfilrP2hYGielCcsWptNG45Bx7YyzOeN-MB_AORv40RvWOqDrkLYCMCaKzOmxfe4ehBjR0x2EZJNYCe7Bwb0uHdATx3pvYHOHQ119DVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KVhaKwY9X0po0aBAewyUjeeW1uu3xauGrjMeTVEjBIwclea7XrcuHhQGihUo2zfIuk2b28N1rPKXU8WnQPVEquTGahfY5xg2f8VobS4FQ7MdJ38tEVvTGx8M6mqqMuMyuFCvCUQNRz5RLR7HfbY9z5n5YuPWCH5qfHuqKN3ugUGPXWBqXy2qXHS5q0LxpcczAtxiO1ymzDLlieFQWJojLVsjAdiRr_8xBkgzNY1fzX7M5JplYYCZOVSYiWj9u4LvNNovbBQf4ivackLjS2AW2-rIOXrN0bTvyoRbbIUidFg-Gh5Uu0KY2JeAbNag2pnsjOkYeUGQG3ICT0MQb44FZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HefgriA81jVf8DdE_iD57ZJxt0jZuE27Pmm1aJ0o0qvbd1h3cYZqGIZnAz3TM5Jw6vzyyuWfTmzAq0PvuXft4ddTB1jsh-ufQ7Za-MQLVd14nwVzV1pd35Vsc1dacT98GGayT2q9vAzPU3fNQ6HdG32QIZtQ14XRsesSzKVLPfaMfrdSdWU5qsaqB9B13DhULhVPeySKAcatEVwVOO-67lbyqoFtXY11sVn41JBs5xX1BpQaul4rXSR_aO-vdcBi2ObDg5p_Owyif9tljl2XEeJhgXrxLnnE3zgRPbP_BkOgsQZpODj1qyJVifM35nOAn5MgNEmb7hJSsZwJyQJZAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rYhKazF-H6BvbUw9MuGtcybENF3okxnGo4NxKc0Po2biQvtmcDvK_pma_caL4wgCpOIH6kiaEjEiGprnJb2kXY-gMh40bmUfFUmbzxdUiXBign1mL_SiuZa5pQ8UdukgJ-Hv6yMYIjNxPmnRlvLLH_Gdf18RIEk8AhxcgzDPJGGTEMd6XANtLw6B-vg5VzDenrGuYg-Rrjp__z74ugQQg51eX1Z1bBPBNUNFrTHQMvdX2ysRCN8CpHA164XmPidsOH3DtDaa1DSIz1957rCRP2Zetr00p1VqaBwpriRk4OznMwBYKTXK1DY2aTsGYfZ4neCR-CeYTBC8tkjFbcK_Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/idRoyhdRIzdRLTA5TteY8wXU0_FBmhI8hkBukOvXYUQXpP3vhL8UskNON1T58KSmHD-UDkmVYknvy2ai2hYW8MIn-bVtCuC_NiBiC0vYg8_O6KmnkOwxinhzqNb3d8laJnfAMW8YpLip8PO-UfBwJkYiMljol8abauNdaC1LxKM_EXh6xpj3LHOVq5h8tzaGCqpV1FioZiAruQiq4LO2qG-ffMG2n0eUz6LdmX8VWt2u0hMB8KLmJ_4y7FinQnxAJW8vChDyx7bPH8u2b7DGWGuT4svrNjqxt_cNXeOg5BRkorod-YMHfYyRIx8TDZch_2HKzVi6AK5645kFJ3ZsGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vUb0OPktQyXiYWSdAq5l62tC2EFCiNgdMMEn1-pTJ89-tqztN3Lg05KZ1aN-mxUOPrc6cZgP-WTnx0s9cSA7dNBWozraWHlc4nwnDfQxIYEE7o2cmmlGWe2i4ZT-hdCfZWL1_CJ75bMvoQ_WQt_Z_RxF6_MnP5q2xfePEDPT-Jjg9kV9qP_3WXTXfFwWBRtTx5H1O6P4KvFEEtBmC6pZYVptBRB8vGyvPeyNJ1azGhF5rMHrrjh3KIiStuJCM6Gxg79ghoeY85PyksrrRcT2cY33fDf_TeRtUYUF6gKFkzDQO8sP04e02WoPE2Fp36CFKBg0GRBr8XoecjVfitpYqw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
خروش عاشورایی اصفهانی‌ها
عکس:
حمیدرضا نیکومرام
@Farsna</div>
<div class="tg-footer">👁️ 7.9K · <a href="https://t.me/farsna/444760" target="_blank">📅 22:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444759">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l1ZBIQLMsuqWwBa185CAxMCBMhSuWwudg2QRcresBYfH9UjZFsIR6nN-bSldAGxKB2a4omXLKeJqk7l-Ru2WOtzYRlaz4eInZk9Ql1bIsIlwkUL6flATl-tpyLzrrMK-aIYAUcc2sMsLtca8g89Yn1VzUMjb025jqS50lz5p8JQ72zjfLRmQjBgR2MaL1uxvc5IQl2kC7T7kfEHgSvfWhTZsiMTCSir3_N836uZoNtmY2z3E7nBP4zmQecDzyZL5gGNJgQBO4aqWCFg9Fah5U6EGe3-UaRSw3dnc1veg23QOkvANlBXlH8kIQvDvMmMk05Ffakv-k-U7lUiriUCAWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
نهاد مدیریت تنگه هرمز: تبعات عبور از مسیرهای غیرمجاز با خودتان است
🔹
نهاد مدیریت آب‌راه خلیج فارس(PGSA) در پاسخ به استعلام‌های مکرر اعلام کرد: هرگونه تردد از مسیرهای خارج از چارچوب تعیین‌شده PGSA، مشمول تضمین عبور ایمن نبوده و از پوشش بیمه و مسئولیت‌های مرتبط برخوردار نخواهد بود.
🔹
تبعات ناشی از تردد از مسیرهای غیرمجاز، برعهده مالک، بهره‌بردار و فرمانده شناور خواهد بود.
@Farsna</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/farsna/444759" target="_blank">📅 22:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444758">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc6b44073e.mp4?token=hLAdO_O6-ycKRWM0OCeitn0Lfxz8M_6Y1V0d_kSZtaSXefJRfEbCOPAWywdfWBXhyxa2GU-U3Hr_djbKdz6kV7bWeRHV6EOcLItymz63fndDzmVFsabmm2AYthWaLTE1c_Wo-R7OfD_Vgyh2vRW_w_qqBoOQLcIRj9z1AL6qzdcsf-nHYompcnNDob_McpJO6T4YIE8oFSevlhJzU-2BE9y-AIMX0aQr3PEne_OJeOKijgAg7dvbQgiuZOEVXYpfXqs19QmbnjO0NCf_uUSZ6vLtxPHsJAOD4Qu6UpKYv2SH-tUavvj5s3_dU5KBPSpejgpZyDIaK7GSn8nTkf6n6b9QyLSY9B7HjJPhsDrryQs-k1wRbNGN6fbl8A5LYMBRJauUPcISFSV09TOJ4wBhe75HS7qYT9gf9Ft6zcGaHgdSfdJi9Id8Q50dYNI58XD-H2u_-8Dbk0dvREBRCPAie7xA5goOScevg1on7eHdOZpcJo3NtGi8QUUbVdGYwvvov1r2DfGgzqmn-pfCD_3ft9uj7PhGQcvA7d2GE3VDcDzdBbmwJe9I2j3OYD6uEpIRi3gcyniP337eBqthVbz3W6T_T20_OXJ3zyZw64mE-Vx0lJOLc79dwltLVyL6N5I6SnJ7Ub34nbqScZug-vaz_IfEN3U05_RBQApc_gTGYNU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc6b44073e.mp4?token=hLAdO_O6-ycKRWM0OCeitn0Lfxz8M_6Y1V0d_kSZtaSXefJRfEbCOPAWywdfWBXhyxa2GU-U3Hr_djbKdz6kV7bWeRHV6EOcLItymz63fndDzmVFsabmm2AYthWaLTE1c_Wo-R7OfD_Vgyh2vRW_w_qqBoOQLcIRj9z1AL6qzdcsf-nHYompcnNDob_McpJO6T4YIE8oFSevlhJzU-2BE9y-AIMX0aQr3PEne_OJeOKijgAg7dvbQgiuZOEVXYpfXqs19QmbnjO0NCf_uUSZ6vLtxPHsJAOD4Qu6UpKYv2SH-tUavvj5s3_dU5KBPSpejgpZyDIaK7GSn8nTkf6n6b9QyLSY9B7HjJPhsDrryQs-k1wRbNGN6fbl8A5LYMBRJauUPcISFSV09TOJ4wBhe75HS7qYT9gf9Ft6zcGaHgdSfdJi9Id8Q50dYNI58XD-H2u_-8Dbk0dvREBRCPAie7xA5goOScevg1on7eHdOZpcJo3NtGi8QUUbVdGYwvvov1r2DfGgzqmn-pfCD_3ft9uj7PhGQcvA7d2GE3VDcDzdBbmwJe9I2j3OYD6uEpIRi3gcyniP337eBqthVbz3W6T_T20_OXJ3zyZw64mE-Vx0lJOLc79dwltLVyL6N5I6SnJ7Ub34nbqScZug-vaz_IfEN3U05_RBQApc_gTGYNU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
با تبسم گفت ای ایران بخوان...  @Farsna</div>
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/farsna/444758" target="_blank">📅 22:13 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444757">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">پیام‌هایی که شما برای فارس فرستادید
🔸
من راننده تریلی هستم ماشین‌های وارداتی که دولت دست مردم داده گازوئیل یورو می‌خواد. قبل عید به خاطر کیفیت پایین گازوئیل‌ها ۲۰۰ میلیون خرج سوزنای پمپ گازوئیل کردم الان مخصوصا استان سمنان اصلا گازوئیل یورو پیدا نمی‌شه لطفا پیگیری کنید.
🔹
الان ۲ روزه خط‌های موبایل و اینترنت روستای دهشیخ استان کهگیلویه و بویراحمد بخش پاتاوه شهرستان‌ دنا کامل قطع شده و داخل این هفته ۳ بار این اتفاق افتاده و به هر مسئولی زنگ می‌زنیم امروز و فردا می‌کنه من به شخصه از شما تقاضا دارم این موضوع را پیگیری کنید.
🔸
وزیر می‌گوید قیمت مرغ طوری شده که مرغداران ضرر می‌کنند. گناه مردم چیست؟ چرا برای جلوگیری از ضرر مرغداران، به مردم باید فشار بیاید؟ اگر می‌خواهید مرغدار ضرر نکند و مردم هم بخرند، واسطه‌ها و دلال‌ها را حذف کنید.
🔹
۲ ساله می‌خوام ماشین بخرم، ماشینی که می‌خواستم بخرم از ۱۵۰ میلیون شده الان ۸۰۰ میلیون تکلیف ما جوانان چیه؟
🔸
مسکن ملی برای جوانان بندرعباس مانند یک رویا شده، من از سال ٩٨ ثبت‌نام کرده‌ام نه‌تنها هنوز خانه خود را تحویل نگرفتم بلکه با پیشرفت ٨۰ درصدی هنوز هم پیامک واریزی برایم می‌آید.
🔹
اگر ممکنه یه گزارش کار کنید در مورد نقش مافیای پمپ آب در کاهش فشار بیش از حد معقول آب که عملا مردم رو مجبور به خرید پمپ کردن.
🔸
اختلال بانک ملی هنوز درست نشده کسی که مثل من بچه مریض داره برای خرید دارو باید چیکار کنم پول تو حسابمه ولی نمی‌تونم انتقال بدم.
🔹
خواهشمندم موضوع برگزاری حضوری امتحانات تحصیلات تکمیلی دانشگاه آزاد را پیگیری و منعکس کنید.
🔸
برای دریافت اعتبار از پلتفرم ازکی‌وام استفاده کردیم گفت اول باید ۱۰ میلیون تومن به کیف پول واریز کنین بعد مراحل طی شه. درنهایت با درخواست موافقت نکردن. حالا حدود یک ماهه از کیف پول برداشت زدیم میگن به علت شرایط زیرساخت‌ها به مشکل خورده!
شناسۀ ارتباطی ما:
@Fars_ma
@Farsna</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/farsna/444757" target="_blank">📅 22:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444750">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R5SuJMN3UPuWH_dzNq8kUSJ2vvDijdzJHrbxsxCQBFYm2SlhzEixySTz07sxsuUeEQwW6CiumkmE6JjSbxq0K7TfigfSoYGJ-Da6VcTPr3K0fSikfBCcSIkFmzM7gHx3IWPZBuUfrjVtw85q2OkCkUlaIuhLpzKhJiqnIHhPpkAJnpsDfD3TvIGHFrsTOtj8hdB2HW3k2i0iKhL910jbR09Yuco4r9fLfaYiT5CZMHA-3HC5JvRNocKSiUSdvB_-3_tcEPv5JwvDVE8UX7hAzUschqZkwMJ9AEAdyVQGCV-OeD0grReYrn_rgfq8P3jUdCjjVJZwLShZiYqQ2-ciqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DFkmEuyBcx2tpro49j7K0g6BtJOHLqkb3GsVT02fuSbbeKja2QspTLK_tl_20ZK45kpn1ICbagEeYrDz2f3CoAFkqtQUS6TxYwpGKcQnb6uyOKwlH0hkxgu2di4_U4lSMkWfj3KozpVgLu3MO7q-5uRDa2xLKakr3MSSDyGFapimVNVA1iH4v180M0qDjVVzmOB4XZ-ZagQRqiLTZkB9d5nLYi_LrC24ojQfjLt9TAxuCw7V6hX_QiIOcG4K1XHPd_q1T-7ASS00zjGjaf0co6FZEZzzt1kEMhBCPDH0wRB98mx5oX1eOqbB3tiW1rD2p4M-991dyj6ntQPQI_8ZSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VkWrzHpxHPYgfvZU01i6Bry351KgII-sVa9BJRIo9kyvSTJmuehaPq33c7sibkNFB8OaRd2VTP2ikhd9osHDAQYfti_oJ0frNtLgsrk-gkwGmlXS_jPQRgqkri_H5MVDQIk3oTn8opCqDk-vW5tzC3LeQ8ocfWXnwtgaj7EpSQ-u8oIX2qgpZZVCW_giQtefeGJDeEBII-k7zELZ2PYAereEARE9toCtiu22R1MBT1P344Vm5a_tllcnrRauTUh9FOGFNs-kV5qwmA3_TW2QaLZtNevVWs59VV4vpG3xJgrRqqx9Zi1h58bYvizrFgZ2TO801189ZEodOxu0LGNUzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GC-J98MpvQLtj-lJiJ1KoYW6usxCAouulQ_KZS6m8VsBavWAuMAyRI1SCO-Ve3p_KhHMS9M3RV9vhUfR5ELjP4hiN1dSq3ZUT91BJ_rpeoesrRZPc9u5mDDFNNIWaNWMXdNK3T1GdCge7tfXn0vNqNhPpUkkLN84pTQqMCbYjGD2829X6ZS_8ktius_ruquZagaB64X3VGV_eQa4JBqqi4BWhWWYR4DbFwRh4f7ioMWbEtHQXtUFrDtQobwN1jGCbsTWdU5m2udpxRJC7-QgXT9TC2ErPql8NhlwC4_bLBAJclJFUt_qHghsn6dsPSG6Hfgnhbfxrna5QdwswVG_hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u5PfeKozuz7HLyW2hDuHYsWnMcEAxTR3hF7MPGRKUREFCfZrqDFknwe1xzYfSFaxR6GuR1zFF0JpP_8zkousl2o60OY0CJP6CaZsXpTtV7Orleu4wYBHFkF-LiHMH67HzRatQJkjDYsEZRRsN5I0Fh5jJi7p0eIoEgzNi-15-EneRlTuLPIRNx0sYErsAgDvRH4DQgVGbCNrE59YXy8AIVyhofwgigGg2bHoku_94lGgC7VlyrVeac_NjkmuD9QFklDQEIesbr7PsKtUNIXltCJNybo9zGxnMQVS4OPrmdYD0ycre_tKHa8W6gnVeOWhyQLAyyk-n6bks2cLsP0DMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nADQbUvGm5y3OH3BbseC4vv5DerRsCXBMbsrYF4ZJuxKMbMiiGDFKMxCmbktdYB4PKCEOPFHxE6xZmbvkMpBK_6xqQYgv4EeCabeGH6B02VknqtqDgrnIWtw4mHUj06BcWZjQV00ju6zQcc1cqCiuJ3moAqhY1qxc4MU8ej9jwl567p7TruT_qfj5o5K8fhWlJ_2Ot0V6CO--sSZuUh_sGkLsQJE4Wh02qXif5qc_Hxo5QZsSvDU_EPslVUESZTBj-zkaQAlyayTomFmXkwJYcJP6Zi3-Jtg6Q6Mkqmyx4PMD1C_B6BPNQkHc_QeUfLLlUvRAXX_YRnK2QcI_mCnEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OUa2N4gLpkOW8tcVdCQS29XtFwUjRg1rVAiA99iIcrxoNzcA5WeGVVeydIyacZqmj-gH-VeOy4J3nrywI58UGeR-41IY-7wosg_kx_-NKuNAMfte41bYIIdIcuMb1zy9iHokzfnvftbDPUNzuFHlmK6-litWnqMBG5yGR1T9ctSRvlXBHMFApkfFmjclHWh8DYkgo5E_xDQ8MkJ2W7c45zZxiuCtnopsQYaLnn7fn5udmjtmHsqSojBTM2B0eS9HudURScHy5VzoaKbKuxw9SJkBfLMQEMJavh4CiVNhwoPoXUnpP7gGd_nU19rGmmwlDnrxwoRjLADbFl9VHhDxDg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
عزاداری پرشور زنجانی‌ها در روز عاشورا
عکس:
عرفان تقی‌بیگ‌لو
@Farsna</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/farsna/444750" target="_blank">📅 21:46 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444749">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2ebd68482.mp4?token=EWl2tMdD3GQxh-hDRS-P75qwFdrk5JusgsZbUlMB_-W4IF-h-mkX252hhpCK7_tCNbGerVyd9jIdd5lSlRsHgw9mftMpg_jnoAEBv9kqrdzyFj6IIAmALW439y-gRO4M8PMrILYQPK0Duqv3PG9S0MqgmpDyyg8Go8AQ56nfog2lcnR_bVvqhT6Hu3sEJEvZDHhlsLeONzKrltxpBgKLeIRGakBuoSEEwPRZaznGvxPtA2hKypUdvAcVFvvO_39My_gvF4Da3Ph25b43-aoA-AeVBkdrdoDo1HzOqtecF_Nb4THGHAkDx7mrYmJYo4ruP1ziKxQf5Q6tKqIn9N8Fcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2ebd68482.mp4?token=EWl2tMdD3GQxh-hDRS-P75qwFdrk5JusgsZbUlMB_-W4IF-h-mkX252hhpCK7_tCNbGerVyd9jIdd5lSlRsHgw9mftMpg_jnoAEBv9kqrdzyFj6IIAmALW439y-gRO4M8PMrILYQPK0Duqv3PG9S0MqgmpDyyg8Go8AQ56nfog2lcnR_bVvqhT6Hu3sEJEvZDHhlsLeONzKrltxpBgKLeIRGakBuoSEEwPRZaznGvxPtA2hKypUdvAcVFvvO_39My_gvF4Da3Ph25b43-aoA-AeVBkdrdoDo1HzOqtecF_Nb4THGHAkDx7mrYmJYo4ruP1ziKxQf5Q6tKqIn9N8Fcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تشییع نمادین سیدالشهدا در اشکذر یزد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/farsna/444749" target="_blank">📅 21:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444748">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61eb241cef.mp4?token=HMYfbp9si8egGSGNPXBl-ZINDUdp-TXdvnJjdGBWFUi5DyqQ_XNmKFieyBmisiFaPNHbJrmEkZbZ6_AcQJI2mFq0GOMd8WydDLUJD8IdSkNozlnB5ZCtO1N5WTaRFCkqC4fYgbmRwyOSTAfU3xTH5QLoohPg9AQGAeyObVMKtiHdZdVEbExEDbgLiOghvGJXnlIhevJd52OVJ83q79yjmFTP7vPkEpVDEVlunTQ45eIl8I-AYsfu21U7XUi03AhC62jy3UBjWhLn29pYh0nCIuqUNu96Er8IX2GbV7v2-vRZGfwDuzFlD6pXtsUXMqwUmarv7L7EycAxAI9zdlF05Q7OZkEBsfSJ2gOi4FFPuRGy9ZtPQkjTZAxqig-rfQZk64QuCQ47SKL5XEkWr_HSw06kOEnm_FQ7y2DNuh9JeX3vSPnyTrmqIEhOMQIVIJ3_ibzwhziNTh45elRH5x9FJHM7vnM0khrNYpanYyI9Gweri-BaoKtxMVujAXsZxJJW2sCOXUcv22KkDIGM_NmdGTZ1lheM282ajyQlSeOsh_1VXxlmyPIvrmDxzvvqWlJVgAY-dW3KrpgpuRX2ClMgxizgQopV7edpsjvtYQNffyTrDZbAm1fwlQcSN7s97gW47wqKMwyytznGEqCuH_1TpqJTJ-oj4GntEK02F00ilVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61eb241cef.mp4?token=HMYfbp9si8egGSGNPXBl-ZINDUdp-TXdvnJjdGBWFUi5DyqQ_XNmKFieyBmisiFaPNHbJrmEkZbZ6_AcQJI2mFq0GOMd8WydDLUJD8IdSkNozlnB5ZCtO1N5WTaRFCkqC4fYgbmRwyOSTAfU3xTH5QLoohPg9AQGAeyObVMKtiHdZdVEbExEDbgLiOghvGJXnlIhevJd52OVJ83q79yjmFTP7vPkEpVDEVlunTQ45eIl8I-AYsfu21U7XUi03AhC62jy3UBjWhLn29pYh0nCIuqUNu96Er8IX2GbV7v2-vRZGfwDuzFlD6pXtsUXMqwUmarv7L7EycAxAI9zdlF05Q7OZkEBsfSJ2gOi4FFPuRGy9ZtPQkjTZAxqig-rfQZk64QuCQ47SKL5XEkWr_HSw06kOEnm_FQ7y2DNuh9JeX3vSPnyTrmqIEhOMQIVIJ3_ibzwhziNTh45elRH5x9FJHM7vnM0khrNYpanYyI9Gweri-BaoKtxMVujAXsZxJJW2sCOXUcv22KkDIGM_NmdGTZ1lheM282ajyQlSeOsh_1VXxlmyPIvrmDxzvvqWlJVgAY-dW3KrpgpuRX2ClMgxizgQopV7edpsjvtYQNffyTrDZbAm1fwlQcSN7s97gW47wqKMwyytznGEqCuH_1TpqJTJ-oj4GntEK02F00ilVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نقشه آمریکا برای گرفتن اختیار تنگه هرمز
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/farsna/444748" target="_blank">📅 21:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444747">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9610b1e11f.mp4?token=XZJ4vmO0FeLj52Dt6dl6i6pKb2jQUNEnjF6I_iS4CQgk3C2Ahf8dcC32LmuqjwjBNB__sVReVmGhQ7uvsaT7yxKqMwOHYaYTtYZEPeBgrzVkjByuZ9mRjYg8JnrhdKEA1AgeK0pDkffx80tWN5AzjSd9uWpsKMkc_srrwOaXfcT0bBiXBbdWcQlrZHGQOQnuwffLV2C_K2S8Y-IR0tQGcrqyezUI-ES4_Q1GxiQU6v7JJynbFho7aUKE7CgVTxss_T3j2o1sYKyio-0z6VianWlAOBznEjsw0L9sAPuZyXpZWnTx138iIm0hx_xo8wVZ4FHycneZB2VfO2o6DX3QfKypfdeGzK-t4TVTLfvx3MOE_-LaUwBOWm4XjPhNZdOrNT8HBhM4phXxKAAkECvPlacsCPz769oUWWDIIfPFvqCs2Wq4pUjZz_vrdBGMAqXjKBVdgqEuZI9qtopJGE68zD3lK2botupYcjSXc5vqcxL4Ku1DDmV6m6JWzgObtCdbXIHU_zziq9DlX-rgxGaqaXfJFo0-ngWNDe5wcKtwDAUQIeu5eJZbPjMInhjF8iSDBPewTYrLWkD0n7foQ4-qjGUbC4rQR3M40MKrgT--kVlYAqEw3xrikrH7NvPASGN2QZGp7b_ZJ-ay-HTRmWSiLtND-6bpS7xnjZA71ZQYhCE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9610b1e11f.mp4?token=XZJ4vmO0FeLj52Dt6dl6i6pKb2jQUNEnjF6I_iS4CQgk3C2Ahf8dcC32LmuqjwjBNB__sVReVmGhQ7uvsaT7yxKqMwOHYaYTtYZEPeBgrzVkjByuZ9mRjYg8JnrhdKEA1AgeK0pDkffx80tWN5AzjSd9uWpsKMkc_srrwOaXfcT0bBiXBbdWcQlrZHGQOQnuwffLV2C_K2S8Y-IR0tQGcrqyezUI-ES4_Q1GxiQU6v7JJynbFho7aUKE7CgVTxss_T3j2o1sYKyio-0z6VianWlAOBznEjsw0L9sAPuZyXpZWnTx138iIm0hx_xo8wVZ4FHycneZB2VfO2o6DX3QfKypfdeGzK-t4TVTLfvx3MOE_-LaUwBOWm4XjPhNZdOrNT8HBhM4phXxKAAkECvPlacsCPz769oUWWDIIfPFvqCs2Wq4pUjZz_vrdBGMAqXjKBVdgqEuZI9qtopJGE68zD3lK2botupYcjSXc5vqcxL4Ku1DDmV6m6JWzgObtCdbXIHU_zziq9DlX-rgxGaqaXfJFo0-ngWNDe5wcKtwDAUQIeu5eJZbPjMInhjF8iSDBPewTYrLWkD0n7foQ4-qjGUbC4rQR3M40MKrgT--kVlYAqEw3xrikrH7NvPASGN2QZGp7b_ZJ-ay-HTRmWSiLtND-6bpS7xnjZA71ZQYhCE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آئین شام غریبان حسینی در سواحل تنگه هرمز
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/farsna/444747" target="_blank">📅 21:08 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444746">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r8Rv1vPu-Sthc_VVfafrk7MQHTSTYxO3IEYs9jmHW3t9bpAW1eNJmzhL_b1qw1nEpWCTOjeaAqVCakHw0tIzwsBSEDpqWjFweC0KuYtEyZcxfIGFAcwAIukYOBxaYOWj3CZPQTo-8uv2ZUZjZowaqWh2GjyQs85DvmNDb9D4721dpZ0DVcSpUh5rNWwq1wSUBC9WwCLlyfEsW7I_m_St8XFRASw9ixP-r-8dslb-SRx_eMP_5TGxQm1QB8eNExyKiLRt61_BbJtwZhtccM3sLS8kFtIAKJElyY1btcUTvyNeLxd1HWIUiNU9q9JeOGl9tx930M5PBEze_LRbJKkc_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشورهای عربی و آمریکا بیانیه مشترکی دربارۀ توافق با ایران صادر کردند
🔹
در این بیانیه آمده: ما از امضای یادداشت تفاهم بین واشنگتن و تهران استقبال می‌کنیم و اهمیت تلاش‌های میانجیگرانه انجام شده توسط پاکستان و قطر را مورد تاکید قرار می‌دهیم.
🔹
ما بر اهمیت حفظ روند مذاکرات برای پایان دادن به خصومت‌ها و جلوگیری از توسعه سلاح هسته‌ای توسط ایران تأکید می‌کنیم.
🔹
صلح در منطقه مستلزم مقابله با تهدیدات ایران، از جمله موشک‌ها، پهپادها و حمایت از نیروهای نیابتی آن است.
🔹
ما بر اهمیت بازگشایی تنگه هرمز تأکید می‌کنیم و اینکه آزادی نامحدود دریانوردی برای امنیت منطقه و جهان ضروری است.
🔹
هرگونه سرمایه‌گذاری یا تجارت با ایران مشروط به پایبندی این کشور به یادداشت تفاهم و توافق نهایی است.
🔹
ما تعهد خود را به حاکمیت، امنیت و تمامیت ارضی لبنان مجدداً مورد تأکید قرار داده و از مذاکرات تحت حمایت ایالات متحده بین اسرائیل و لبنان استقبال می‌کنیم.
🔹
ما بر اهمیت حفظ روند مذاکرات بین اسرائیل و لبنان و اطمینان از عدم ارتباط آن با سایر درگیری‌ها تأکید می‌کنیم.
🔹
ما تأکید می‌کنیم که حاکمیت لبنان تا زمانی که بازیگران غیردولتی قابلیت‌های نظامی خود را خارج از اختیارات دولت حفظ کنند، محقق نخواهد شد.
🔹
ما خواستار خلع سلاح همه گروه‌ها، احیای انحصار دولت لبنان در استفاده از زور و حمایت از نیروهای مسلح آن هستیم.
🔹
ما حملات گروه‌های عراقی وفادار به ایران علیه کشورهای شورای همکاری خلیج فارس را محکوم می‌کنیم.
🔹
ما با اعمال هرگونه هزینه یا اخذ مالیات در تنگه هرمز یا تلاش برای کنترل آن مخالفیم.
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/444746" target="_blank">📅 20:56 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444745">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LmCyI0EoVBA1ooQsL_yddi6VJxt1dbMOAjdV_71uOQo9uzdZmsZ9gPLucLAf2Hn28F9CY_D7A362JoCl8V-W_JVDkbyUB1zB40lZ7ugcMF1WlZieTWu2-xj7QMoto-R5ZenYbmhCEjXQA-ylN1ORv270zUR5KUOznc3VZWv78WOszh0h9qBvkT0pbnJxauTv15d0y2Jei3jP9--X_sxG6AqXuJ1pqHMEnmjWnbDkiGSHCvUYXi5OCRHl_M--Ma1BceN220EtfS34DUhu0oiKYqcRrCuQjOwMGAmHm26sceMkdOMavyFvz32cZiKaPmyEwpSH8K5etqq1hYtl8PFpwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرانسه در لیگ ملت‌های والیبال به سختی از سد ایران گذشت
🏐
فرانسه ۳ - ۲ ایران  @Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/444745" target="_blank">📅 20:35 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444744">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d6e230c1a.mp4?token=SUpWYlGytsOfBt8xmoFhkUEHVahVWajPtHVbNhCTjJttyMJ5Lvr6iKCXIe_ji2V1IU0hGWQ3rAB33Xv-1M7QRh4EsqNK8pzZike5SFSoQfE9jlxnlLzIv01fMPxgRRVeFRXNdTgU7oUG6Qv918NzZbqG3Lb1Nd7JUVepx8EgT4yTv7W3ZaCci2qDU42cMLwymfPBLncBB6lStD_3ZMnFJ0qzqJWrFze84eVXTXsH9Q-tDX9yn9tlE6xG95UMZ4xZZggwriUu02mqu70iQjCMyYO_j4Yrlh7pH1ScR3-2kFAFZF5Mt4nh91KUaoDLcLP9jgyPfIrjdZmhzJ7bqFugh0Q2RtOQNwdeOMbrvltXhucyogZYnoaAVyoFflVmCPJerRD79kueqVHDfGknypbRGZh6MuLJCbpd7XJhM3a7iZ_kwalFeVaf7MZ1Rwbz-qx_aTVuXt1MYudxU_6B6QnxkA8K54tX6eIzsUbE5q4Q82yJXwUSF33HIseCAECBCtDlXkE63kr4danbzCfpN3gYQAl8X8TLa2ehBEjlpWy-9NrWlvu7JdE7yTSGO53kA9U6VMfYNB1fInf6MC7RIUI-QI2mdP3lApw4SSJL24VT_ZBEjTBkut0SC_FkSc0StenP5ZczwyYaRzH05RgSYN_F0Tr5DtbCUMzFPN037NTDAEk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d6e230c1a.mp4?token=SUpWYlGytsOfBt8xmoFhkUEHVahVWajPtHVbNhCTjJttyMJ5Lvr6iKCXIe_ji2V1IU0hGWQ3rAB33Xv-1M7QRh4EsqNK8pzZike5SFSoQfE9jlxnlLzIv01fMPxgRRVeFRXNdTgU7oUG6Qv918NzZbqG3Lb1Nd7JUVepx8EgT4yTv7W3ZaCci2qDU42cMLwymfPBLncBB6lStD_3ZMnFJ0qzqJWrFze84eVXTXsH9Q-tDX9yn9tlE6xG95UMZ4xZZggwriUu02mqu70iQjCMyYO_j4Yrlh7pH1ScR3-2kFAFZF5Mt4nh91KUaoDLcLP9jgyPfIrjdZmhzJ7bqFugh0Q2RtOQNwdeOMbrvltXhucyogZYnoaAVyoFflVmCPJerRD79kueqVHDfGknypbRGZh6MuLJCbpd7XJhM3a7iZ_kwalFeVaf7MZ1Rwbz-qx_aTVuXt1MYudxU_6B6QnxkA8K54tX6eIzsUbE5q4Q82yJXwUSF33HIseCAECBCtDlXkE63kr4danbzCfpN3gYQAl8X8TLa2ehBEjlpWy-9NrWlvu7JdE7yTSGO53kA9U6VMfYNB1fInf6MC7RIUI-QI2mdP3lApw4SSJL24VT_ZBEjTBkut0SC_FkSc0StenP5ZczwyYaRzH05RgSYN_F0Tr5DtbCUMzFPN037NTDAEk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قیام بروجردی‌ها در عصر عاشورا
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/444744" target="_blank">📅 20:08 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444743">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aqy3izpabfRA0cjqjwElkghnE19PwgT1p8SyNzGT_4RC4q7IYwekvB5NJ6MrCwAS81tw-dyspdl0aSgff-TLn53Z6rn2GDYuN-yfdUO36IuaqoEXeoYBrRtMckgR9Gg6pdqej0A8iqFaPW9drE8RNG3Rm3XBFVbfo-7HG4xKhnFwKj43xJJODjI75F6dkDDWEa6-B5DCJeJiOvqTa_StMEWINuF194hvJdI1jKFAuqsExKF9zVaEEHSfsHEuU4RfF_wMCXG7Rnmy37Hakg4Vh-tfs_2jCwtRE2VdDhsxPJmQ-yibDbVdE1F7HU2kKQihopWvp8eFy1UfR9__f_Y3tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
رهبر شهید انقلاب: آخرین برکت عظیم حادثه کربلا، همین انقلاب شکوهمند ماست
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/444743" target="_blank">📅 19:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444742">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aI03D3YwvrxaOdyknZ6dih7RtmQlEBMzbz6h_uOHWgb7inirMIKlXLcBupvHJKOxjRSaQvWMVacnLhwZWjsTtzOvsqlDfVz5gVb93EBIOOYg2fn9YMBKlze7LmXpH5bAoB1VTQiPeoVMfvlMc3igSZljKwOCUC4xtJvpWlWio8j9xAms4O2ZW5hE7h5AUiFvoNH_HtQGbN7vFTKQKdyWEUE4udRcd9he703WtnXUGZpZXmnaFDKBaJ8a_xJ3o9AVEfWi_Ked4l_Ug78g1eZsp0kPKjWXzI2_qmrNKyH8rORAOyAMY41RnuVyalyEY_oSjNiScQpS1gsMJGW6-Ab1jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو: از جنوب لبنان عقب‌نشینی نمی‌کنیم
🔹
نخست‌وزیر صهیونیست‌ها: ما از فراز قله «بوفورت»، بر جنوب لبنان تسلط کامل داریم و تا هر زمان که لازم باشد، در منطقه امنیتی جنوب لبنان باقی خواهیم ماند.
🔹
ما قصد عقب‌نشینی از این منطقه را نداریم وزیر دفاع و من این موضوع را برای ارتش اسرائیل کاملاً روشن کرده‌ایم: شما برای نابودی هرگونه تهدیدی علیه سربازانمان یا ساکنان مناطق شمالی، آزادی عمل کامل دارید.
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/444742" target="_blank">📅 19:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444741">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4f6819169.mp4?token=uGQ_OvzahALCbJ7KRF94FXgPouZ7uw0LjYlOr7vGr91CsyboBPEHl4TVwyIzoyBYcSYRBsVogsCYi1wsvRgdK9DGkhnz9LpL47XENW9WQOiWryaRwHa-cIMSZ0o16NZLdp2LpS-taOaQH3Jmdrzll3Upio8Q84LGSBRZASHsLAgNwLqltbOzr1EPYN4RwvVDGOyVQ6NZ6azGr8puMPULdw5ZkQBc3xQ7aomeb6HZRxUk4rSspsPUajzNHwGwey65pbpSu9EfkGW-Fqom4XNqnbwWcpMosV11Kul72Kv8uHcFZNeVutE-iQpw5c0qZo5KQO0KINKwYUUR5xld6GrWiRp5gpoC0O6ThLEsJVXke-Z9kJkliyaVx8DmiB4QwQPmPOQW_tcJcC9mGF2kW8pNDKvHLezwr0GA1jpHuoMaPwT_KUA_aD1PodYO-onHwHFv9Z0kFNR5qR9iy20TNvCHnB_HtRrfGeJj-XzxfPlaS2skkG6CRXrxFTmqZyNxNVPPQpEGkkATGkNVmfRcu5lGxu3GCqtQJLI06lM_N0G7aXcUv3L9NwdPMQ7nvAFzHl3o4nYoIqe_HK76ZBcgRYaK1yUTJMpDYB2-1ZsSxJsLS2k8PIp5dqj64xjts0pmixDh26yuhkMoM6H6ST3-jiRjVAQoHQp-Ya9oproe8hhC3xE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4f6819169.mp4?token=uGQ_OvzahALCbJ7KRF94FXgPouZ7uw0LjYlOr7vGr91CsyboBPEHl4TVwyIzoyBYcSYRBsVogsCYi1wsvRgdK9DGkhnz9LpL47XENW9WQOiWryaRwHa-cIMSZ0o16NZLdp2LpS-taOaQH3Jmdrzll3Upio8Q84LGSBRZASHsLAgNwLqltbOzr1EPYN4RwvVDGOyVQ6NZ6azGr8puMPULdw5ZkQBc3xQ7aomeb6HZRxUk4rSspsPUajzNHwGwey65pbpSu9EfkGW-Fqom4XNqnbwWcpMosV11Kul72Kv8uHcFZNeVutE-iQpw5c0qZo5KQO0KINKwYUUR5xld6GrWiRp5gpoC0O6ThLEsJVXke-Z9kJkliyaVx8DmiB4QwQPmPOQW_tcJcC9mGF2kW8pNDKvHLezwr0GA1jpHuoMaPwT_KUA_aD1PodYO-onHwHFv9Z0kFNR5qR9iy20TNvCHnB_HtRrfGeJj-XzxfPlaS2skkG6CRXrxFTmqZyNxNVPPQpEGkkATGkNVmfRcu5lGxu3GCqtQJLI06lM_N0G7aXcUv3L9NwdPMQ7nvAFzHl3o4nYoIqe_HK76ZBcgRYaK1yUTJMpDYB2-1ZsSxJsLS2k8PIp5dqj64xjts0pmixDh26yuhkMoM6H6ST3-jiRjVAQoHQp-Ya9oproe8hhC3xE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عزاداری سنج و دمام در بندرعباس
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/farsna/444741" target="_blank">📅 19:35 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444735">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LUItPQbdCJCfdOE4_5aLdmd2Uik19hVGdXzIN3hyT0PhEe8RKk1AOVPplhuDSlezcMIK6h40ot8vaghrM6_GTViymOT3CL7z3bx9QZBf-cR0VByNYn_IWvjXiPguRsazUKYsd-8ge_mG1k-B8MdgCzrDcQK70bdyA5ALxUIcahql1ygkBMVE-FcW6izBujiX-xvjmp16LeTf6tTV5gO8hXlogMeOppXhooUArK-vJzskJSXSbJDndpFzYxT86Fe2BRxcUc5JGTlx4WDiIh302Ehh-TdyYSlFEHCZq_HzfN-xv2lspx3LjSns_n5yWExPLaJuaEEW34MlfLlBJxAbAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SAcQ2WMDCeYOhzA6HNBec66jaQ44xLdtr4wsAmJveA-E2eQBoprg9LWj_WUzyQqj7je3QhkaUUqWE4gH8jhc_a_UjK3HV9-_Cj7HGZet-vc85vWlGfCNK6VthM3YMQjiTINuXUMhJgrPRSg-QTYHuUsNiyw9clHWZ3dw88z9GxmSopAiVIRIrattxxCqFo6ZDlvQV7ZK792_xsdDGQ4xg7LCD7_Uy7aLQWb6CHO44MHmn3kZgXhceDK0EDYIcLfuCRanmBrdFBl1GjGw83sM0TJ3pzy4eOsqPj0izq7Qy990KTltujeUY9_hZU6idJ5qgRZu-Vd5bwqs-yp_y4R3dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/daM0yK53f3H8sd9f5DnQYvkN0VJLadrD3GX0C2kltWE8evgRUqbzUlS1p1J6c4zOm099i9Wx9KEX6mvjIDU7D7V4l9ayB03Pu3J8_w2rvu0INqatkhjzWDR30NqM4SC8GVXHaPZmWeZPBnHJZQobZoBKoLIW7BJqk1kix8r0x8bmnEQb_FfrdybcNWjeHyKFi_7aHk2TfmFFcziJXpvF-6FQtZy7qBDuwdrMZGhcKTz4vCLylGXIaQ6fAokb9kp_zhVYK5Wr-BmnCR7OppoFPbHpqzivJhqLJaM7A-bUfqPX-Wjj65-ZcJ_1CUDb7Ovz29KfEhmKFxJHA09ynVchLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p1Ns7Z0qcslDD_-NxMrp9rM398uXw8449nxMaQkwFLEzja1kLHAbvfZL57XOjwcPQKRidOEBM_CR4mn17uxz9o7X-MBfauR3SMhmr8y2-yQy66-MQpVyisoRA20cjBDVftC9yLxHlxTvFEgVAutEAOn90aCKu35tQERYNoIKwlX52IeU5stPJdubJM039BDUpmqTl1gPFDiyI2tr7012jIr5S7yF_zcYnHKbomNpVHjNZBM9par4UD7owgaahIZDmZWQ20jl8xMnVHhtEi1pC9rIFqfBvPmVP850PSfZVIpmGnKdcoRkv8K70b_qHnN3cIttXwIS4mAeyxove1RU8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m--s-j-osyyyGzR8bDJc1j_5iDKLdE19IylfsxJ9MY5EuP73032jzXo0V1Kh66F0vD3sj6fH72iSMyURNvAcusLcQK6VJfooJr-QTl_CFWzTiaegTza4V6-kEl8fNq1dhHkuR_IF_nymMn9kAWhnilun7JGwar4ujdeG9dHiV7vpAyClEiLlVmXIbY1jMRLD6x1yvjvcRlRkEmnejt8SExcOM_i2zePnGQB6gKy-N6yf1ctRlhqtkpENuq-85pQasr-Ej7salSUegfiDVICg_xgm8AP3Qak0J6YRR_FHQo7JFhCOfardxgQsmEA4P3plrKbDaB37t1XatdLD0DH1sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PwjcfoGCRm2UX3pXqIIXbMihrqjIT8wuRhoN4u7VX9oSoX5Rl5fgmXYzBGtxSRO_u9uFuJwEnduGR2_4vOSN9jJc7wfZPIyPA49dtKo3Dztt2Hj87ulfQbT-4Ob4ni5R6AR2zn9pPZfzHD7LmLL42zxcfiNNYdOYAk6afGgaVOEBFLR1DWod67BRFS05n-fPNRLUOFVOytsLgfLFT5ZSPrVHL922UoEOssvzxFl51B3VcYfMo4HACVoazbWQehuQRlM19iejw0JgbjecfrH-xL4ZZebAbcP-cbNKFvGhg77erjhKIz9u_QCxACQgln6X_VJgXjUu8eB5rY0zlABwBg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
شکوه تعزیه و گل‌گیران عاشورا در بیجار
عکس:
شهربانو مرادی
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/444735" target="_blank">📅 19:16 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444734">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OfsTpR3A0TbzBDeHH8d1ZB-VWi0NB4D-Ru-CruSF8awHmGF37kPvx_zbavNVdTHq9M0RQb_8LkCQjRS1HVsbI8uw-1Xa4ImwFTG7BUt3rtmx2V4MGb4N1WecM5-WhaI6YFySTAua8OfXXLPvwwAH6TCh03eB8LdaFZZHP7y11FJNXGDfpEF6VL3UsvTwZXaOY_hcxovSoYdFCi01TJrJs4DKb0rTLhyhCWf3dldBfs1UOX50Cgdab20afIJOMggvaiTG1Uo69STE3OIejVwanVejKA35Jn4XtFyNUlC_TCEF_iU-CIcQcTE5R7CIqL2G59y5RaF5b8gEKJF8Jvh8eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اصابت پرتابه‌ای به یک کشتی در شرق عمان
🔹
سازمان عملیات تجارت دریایی انگلیس اعلام کرد که یک کشتی باری در جنوب ‌شرق عمان با یک پرتابه ناشناس هدف قرار گرفت که باعث وارد شدن خسارتی به آن شد.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/farsna/444734" target="_blank">📅 18:55 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444732">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">رهبر انصارالله یمن: حضور اسرائیل در سومالی‌لند را تحمل نمی‌کنیم
🔹
ما با نهایت دقت و اهتمام تحولات اوضاع در خاک سومالی‌لند و اقداماتی را که دشمن اسرائیلی با هدف تسلط بر خلیج عدن، باب‌المندب و کنترل دریای سرخ انجام می‌دهد، زیر نظر داریم.
🔹
از کشورهای مشرف به دریای سرخ می‌خواهیم موضعی مشترک درقبال فعالیت‌های دشمن داشته باشند، یمن در خصوص هرگونه تمرکز و استقرار اشغالگران صهیونیست در سومالی دست‌روی‌دست نخواهد گذاشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/farsna/444732" target="_blank">📅 18:50 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444731">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27efdc29e0.mp4?token=vYV-Gq6ewWi61aBgoofFRtns48j3gSuRDv4E_n4bdBrdFahDf-o5gIFoPeYyeVDPo4I6DjDS-UtXMOROSD24orFrQAoIoWIlATxRpVsIXSl5n1U71lUMmSi2kF_ObDuJLKHsnWEU-qWW48cp_WSSoGWV0Le_A_2tb_OxWdrGv2_sgPFi1ORnZ-ymGe9nQ2fNnd7e4RxSQ6usK4R7CRTgw7-Yid7g-VHyskJUzgor9eO9UHhpkjO7CXPdcDlSUgzjdko1TWThqaSjhVR6wjjDMV8JaJCS8PYPsmoEnU_zNxfDim2Ts8xfiR02HPNMTP-bJYFJNKaD7JQ39g8lQBdw4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27efdc29e0.mp4?token=vYV-Gq6ewWi61aBgoofFRtns48j3gSuRDv4E_n4bdBrdFahDf-o5gIFoPeYyeVDPo4I6DjDS-UtXMOROSD24orFrQAoIoWIlATxRpVsIXSl5n1U71lUMmSi2kF_ObDuJLKHsnWEU-qWW48cp_WSSoGWV0Le_A_2tb_OxWdrGv2_sgPFi1ORnZ-ymGe9nQ2fNnd7e4RxSQ6usK4R7CRTgw7-Yid7g-VHyskJUzgor9eO9UHhpkjO7CXPdcDlSUgzjdko1TWThqaSjhVR6wjjDMV8JaJCS8PYPsmoEnU_zNxfDim2Ts8xfiR02HPNMTP-bJYFJNKaD7JQ39g8lQBdw4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عاشورایی‌ترین لحظه والیبال ایران
🔹
ملی‌پوشان با مچ‌بند مشکی و شعار «ای ایران» به مصاف آمریکا رفتند
@Farsna</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/farsna/444731" target="_blank">📅 18:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444730">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13793e5897.mp4?token=hHQrH4sW1zpzxghnP_Fr-TC1diXVQls2sp2jWfwMkrfb2WS4cIWYLkKYW0olqtZzfvO5a9StWN0UEJtKWsMzMr4HbaE7ZQHZc1FCIW5CPGHfarH4AfGV6yvUiDL8qv2CIB8ii8ERBhEhyj8Gb-Fzh5_xZK72SAW425qqkj9UStEq5lUPC5XqCk6CeGgLkMIQx8hBfu7kwqU4GjYB-z9CsLGIND_bg484_4PfUnazlkBK3lsIJi8NzMs2k0p2JHBFOJ4A15fX4t3rscDOzpSfboHW-B1xWqwBlNE2V9jy7cVQWa5iZBe1syjWN-Z1OTSQdvG_QD7P-NDakly8r2yZNCdL_q3xkhXXOaTmw03PwnGJbG3SqJIdGp95qXcHzz1R29SQefWUZqpLk8aL2n5kAp7zhWfHDEfQYfaE2cxJEa6_PY7q9DzpLobXyYwSfE6vjsx-QztXpEx17XpC6azK7f5OyOjQ-6NGLvyRifqaqosq394dIf5fuegVdbZjYgOffwSAHcJJcVawl5-XsofkS-nvy5RpO-uliIlp4HKs55w5361-GM6kuVmBDFwZMNG2voKYfJQlHjmcktWDfTu50H2vnAZPoXgIWOxZH-KYX6gH539CtSqVgVfX3k8so-a-Q56c88Tej5pGPff-RAiK0aJ3qtxgb14C-R4TiowtCF4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13793e5897.mp4?token=hHQrH4sW1zpzxghnP_Fr-TC1diXVQls2sp2jWfwMkrfb2WS4cIWYLkKYW0olqtZzfvO5a9StWN0UEJtKWsMzMr4HbaE7ZQHZc1FCIW5CPGHfarH4AfGV6yvUiDL8qv2CIB8ii8ERBhEhyj8Gb-Fzh5_xZK72SAW425qqkj9UStEq5lUPC5XqCk6CeGgLkMIQx8hBfu7kwqU4GjYB-z9CsLGIND_bg484_4PfUnazlkBK3lsIJi8NzMs2k0p2JHBFOJ4A15fX4t3rscDOzpSfboHW-B1xWqwBlNE2V9jy7cVQWa5iZBe1syjWN-Z1OTSQdvG_QD7P-NDakly8r2yZNCdL_q3xkhXXOaTmw03PwnGJbG3SqJIdGp95qXcHzz1R29SQefWUZqpLk8aL2n5kAp7zhWfHDEfQYfaE2cxJEa6_PY7q9DzpLobXyYwSfE6vjsx-QztXpEx17XpC6azK7f5OyOjQ-6NGLvyRifqaqosq394dIf5fuegVdbZjYgOffwSAHcJJcVawl5-XsofkS-nvy5RpO-uliIlp4HKs55w5361-GM6kuVmBDFwZMNG2voKYfJQlHjmcktWDfTu50H2vnAZPoXgIWOxZH-KYX6gH539CtSqVgVfX3k8so-a-Q56c88Tej5pGPff-RAiK0aJ3qtxgb14C-R4TiowtCF4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آیین کهن گل‌مالی در روستای امام قیس
🔹
آیین گل‌گیری به‌عنوان یکی از سنت‌های دیرینه عزاداری در روستای امام‌قیس، هر سال در روز عاشورا برگزار می‌شود و عزاداران با آغشته کردن لباس و پیکر خود به گل، اوج اندوه و همدردی با مصائب کربلا را به تصویر می‌کشند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/farsna/444730" target="_blank">📅 18:38 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444729">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48b424f52e.mp4?token=StVEDf6rrycjGn92nANEMmn8sPOgsp5HVn3I6FrE8P7wPO0MaL0JmQ_Rb7udy8dxYD_8g55thBWGUZR4yOg0Tj5GgPvejKBu21EL-5biBehr1yTh87j5S85CtT9d96hjedimuYzJiZpTa1KL2Lv2BFGzmiQf92_fDGy9llUsC8fi8NbONMqLoYVUzu6WSDMoQ-hDzp7BraSEm0eoWPh9lPsTBIO1kg0595v-QGAhKitazyJE8Bc66cMspXFvLX4Pc3HLc2cBCHSiAVFRH6XXz2rbfRCFCBTlhgC7MYhgzSEfVLhAqI9JRfdWvrdKgv5Qm745Jb_QLbshrQs-tL_8zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48b424f52e.mp4?token=StVEDf6rrycjGn92nANEMmn8sPOgsp5HVn3I6FrE8P7wPO0MaL0JmQ_Rb7udy8dxYD_8g55thBWGUZR4yOg0Tj5GgPvejKBu21EL-5biBehr1yTh87j5S85CtT9d96hjedimuYzJiZpTa1KL2Lv2BFGzmiQf92_fDGy9llUsC8fi8NbONMqLoYVUzu6WSDMoQ-hDzp7BraSEm0eoWPh9lPsTBIO1kg0595v-QGAhKitazyJE8Bc66cMspXFvLX4Pc3HLc2cBCHSiAVFRH6XXz2rbfRCFCBTlhgC7MYhgzSEfVLhAqI9JRfdWvrdKgv5Qm745Jb_QLbshrQs-tL_8zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قرائت زیارت ناحیه مقدسه در مسجد مقدس جمکران
@Farsna</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/farsna/444729" target="_blank">📅 18:36 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444728">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e700273c0.mp4?token=DfY0JBOJYf2Kc_dzUwhQ7-ZFSsybzQCPoJi7S4S_asm-6wGtXEHRYJXj5Xp_YmfcFpte0fR4bzU5-uX-7sM3sCUo58YVEfIQoSdVotRaD7LcB9scSVU_TFOLfSVpspEORlm0YpkO571B-dXqMeKQJBPi2Ltmwlc6KHx85ruS-q47peWPF_8aQQw28oICuZ9GtsUyr0lJokTfEg02gz52vgKaLDU034MyLyMXQxUMXU_j5sMA5ridWFnebRH7qJseHp4aaDTrO3kDUIFvoYN4vFN1N5F6m5J6EnDAWy8C5Y9xIuSFz-tvlNgC7SabCe6o5i9ub5a48I7xqMiZiRyIzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e700273c0.mp4?token=DfY0JBOJYf2Kc_dzUwhQ7-ZFSsybzQCPoJi7S4S_asm-6wGtXEHRYJXj5Xp_YmfcFpte0fR4bzU5-uX-7sM3sCUo58YVEfIQoSdVotRaD7LcB9scSVU_TFOLfSVpspEORlm0YpkO571B-dXqMeKQJBPi2Ltmwlc6KHx85ruS-q47peWPF_8aQQw28oICuZ9GtsUyr0lJokTfEg02gz52vgKaLDU034MyLyMXQxUMXU_j5sMA5ridWFnebRH7qJseHp4aaDTrO3kDUIFvoYN4vFN1N5F6m5J6EnDAWy8C5Y9xIuSFz-tvlNgC7SabCe6o5i9ub5a48I7xqMiZiRyIzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امام خمینی(ره): باید ما محرّم و صفر را زنده نگه‌‎‌داریم به ذکر مصائب اهل بیت علیهم‌السلام
@Farsna</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/farsna/444728" target="_blank">📅 18:25 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444727">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8856d143c4.mp4?token=O8gQGm2a5kToQja_TPDiq9SKII3TMTE7mdwbBpXC0bS4VRkF7YMByhwpE9FFti1LGAH6oNBIWIFYZmW61l_LByItDCWG6pkcmWrLL2I0XIeEty4F4PnaHIEvo6lB0d0LzZg_42gowOR6tr1EcqOn1tHElMSbgdsrE9m67sa9KDuBzMMSpGuC4Lro4QNdG37rxe71AL-DcDZk3ViltBe6DyiDs5IBDepNuz3hFMste80mUCo3ICAe-620f8ryaSqxQBoMvoGVUUlV95ko8pqEigyyuQ77Iu1dIEjuXDGcKFKVhUYghiW1D8-ETMAEllaRY1ePoubfob67F0icCqPXvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8856d143c4.mp4?token=O8gQGm2a5kToQja_TPDiq9SKII3TMTE7mdwbBpXC0bS4VRkF7YMByhwpE9FFti1LGAH6oNBIWIFYZmW61l_LByItDCWG6pkcmWrLL2I0XIeEty4F4PnaHIEvo6lB0d0LzZg_42gowOR6tr1EcqOn1tHElMSbgdsrE9m67sa9KDuBzMMSpGuC4Lro4QNdG37rxe71AL-DcDZk3ViltBe6DyiDs5IBDepNuz3hFMste80mUCo3ICAe-620f8ryaSqxQBoMvoGVUUlV95ko8pqEigyyuQ77Iu1dIEjuXDGcKFKVhUYghiW1D8-ETMAEllaRY1ePoubfob67F0icCqPXvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شور حسینی در سیرجان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/farsna/444727" target="_blank">📅 18:17 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444725">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/521e20e006.mp4?token=rSJdCxn0u_IFr23WBfSS_A9w51OR8_enj1HJLon0iztsdUq8ezD3y5jUg0mSgyGE4MDfZTkwmPlUoCoeXxT7HiFkdM1d5eklx8jMCEK0cOQrjglv8K1GZmNBd_tmHce3KHsol3UsQejUhdUHxxG7vYwCOYqV_todJLc1KZQnEB4-HgSVUhqwHfHqXBLHcl9wUTsmT4xh4st-qdSv7zwOKoPHyRtaNyXcHOe5xzC7SNBK83NX7bmJ1R-GfxlgQAMuRi5VgRMsVInCYORDysjdEr3mAq12noozJPovZUkZ7HDNQjbFNYxZmMi5dtkZeUlfvgmz4HF6MpcowRruOg_p7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/521e20e006.mp4?token=rSJdCxn0u_IFr23WBfSS_A9w51OR8_enj1HJLon0iztsdUq8ezD3y5jUg0mSgyGE4MDfZTkwmPlUoCoeXxT7HiFkdM1d5eklx8jMCEK0cOQrjglv8K1GZmNBd_tmHce3KHsol3UsQejUhdUHxxG7vYwCOYqV_todJLc1KZQnEB4-HgSVUhqwHfHqXBLHcl9wUTsmT4xh4st-qdSv7zwOKoPHyRtaNyXcHOe5xzC7SNBK83NX7bmJ1R-GfxlgQAMuRi5VgRMsVInCYORDysjdEr3mAq12noozJPovZUkZ7HDNQjbFNYxZmMi5dtkZeUlfvgmz4HF6MpcowRruOg_p7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شهید طهرانی‌مقدم: گریه بر امام حسین(ع) بدون یاری ولی‌فقیه کافی نیست
@Farsna</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/farsna/444725" target="_blank">📅 18:04 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444724">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۷۷.pdf</div>
  <div class="tg-doc-extra">3.3 MB</div>
</div>
<a href="https://t.me/farsna/444724" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۷۶.pdf</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/farsna/444724" target="_blank">📅 18:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444723">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/098e04b35a.mp4?token=vj6m4jrpmZTxE4uZ0S6yswIApWKU3uZPFh_4JwtKNUwgNKT0bB4ktCC2kwDkTYypUlEGm8cZ2kgPec0kfcOJDTjrq9vK3cRXgVixscIuXcOvg2__PTnl36dNFBIHTuZAXAS_UvOaj9oq-b4EMPIgnRobvhRNDLIbpCnZhU-dYx7hqQ036kpb9ogvO-hmAFuVdG7QF0CgiqU0CZQXUa-hYKdHmqykMGBFAKxjBfZLkaIeiQLJWgX5SOaKXGMvOAeMtEPF23BuMe56AQTWSTyPHVAw9Dy1zxbnJIEiRniAyXVo6ZAox6F1ZUEyzyxcP0TInp3H_SDA5ha13rvjOOY0tbXwDOMqJjiJAE88Y0WwZJL7i9Ko_AS1KOtqe5Mk1Jc0RHFN24dGxdBY4EI1kBTq0YntVsqjQ33bs9uJ4wEoXoEB9uWJb86zte1pIVSjq57cOYqP3cN68NXcGdnO1oiJ4WTbBsaKrH7WpW-RLpL8pDhAvOPRT2cQ2Lu_fg_lfl6ke64QTv8p47IS6sDL9MwdQUQXgz2hyVEVb1YMh_cIwsZukPSbsxUvYfkVJm7czX_RXqCK5e-wfMvB1ra7onxXkQneHxgoHygjWPc2M2M8ddB4LWmaX-vakKvCKI5zeq23lMu5MFpvN44DiDnEV-QceloyX0RyxQKit1L-YFMbug8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/098e04b35a.mp4?token=vj6m4jrpmZTxE4uZ0S6yswIApWKU3uZPFh_4JwtKNUwgNKT0bB4ktCC2kwDkTYypUlEGm8cZ2kgPec0kfcOJDTjrq9vK3cRXgVixscIuXcOvg2__PTnl36dNFBIHTuZAXAS_UvOaj9oq-b4EMPIgnRobvhRNDLIbpCnZhU-dYx7hqQ036kpb9ogvO-hmAFuVdG7QF0CgiqU0CZQXUa-hYKdHmqykMGBFAKxjBfZLkaIeiQLJWgX5SOaKXGMvOAeMtEPF23BuMe56AQTWSTyPHVAw9Dy1zxbnJIEiRniAyXVo6ZAox6F1ZUEyzyxcP0TInp3H_SDA5ha13rvjOOY0tbXwDOMqJjiJAE88Y0WwZJL7i9Ko_AS1KOtqe5Mk1Jc0RHFN24dGxdBY4EI1kBTq0YntVsqjQ33bs9uJ4wEoXoEB9uWJb86zte1pIVSjq57cOYqP3cN68NXcGdnO1oiJ4WTbBsaKrH7WpW-RLpL8pDhAvOPRT2cQ2Lu_fg_lfl6ke64QTv8p47IS6sDL9MwdQUQXgz2hyVEVb1YMh_cIwsZukPSbsxUvYfkVJm7czX_RXqCK5e-wfMvB1ra7onxXkQneHxgoHygjWPc2M2M8ddB4LWmaX-vakKvCKI5zeq23lMu5MFpvN44DiDnEV-QceloyX0RyxQKit1L-YFMbug8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اهواز غرق در ماتم حسین(ع)
🔹
همزمان با عاشورای حسینی، عزاداران اهوازی با برگزاری آیین زنجیرزنی و سوگواری، عشق و ارادت خود را به حضرت اباعبدالله الحسین(ع) به نمایش گذاشتند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.42K · <a href="https://t.me/farsna/444723" target="_blank">📅 17:58 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444722">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e50f7441c.mp4?token=SFy2BWD6Q9rcaiZXM22HkRagywwlhaDUZaqm__h7QTwd0lsYeRPpwYTbh7ZjWtqe7DM2eXbikj8uT1QsGO4ojEqv6EK-DUHa1pPeEeX5M1lKFm2DBMYOhG4VoEF33AmLVS902O9KBOGUSDDjmlQlN4ktwBCLOuCcXMVSB0lcy8qRXggPJawFhpuwQcpidmASSMR4euhtdB4-YIpvT8fxno8xPg2dM6oDH8ggQ6NeCsJ1CcGscZD8ddHXk88VT0qFLeadle2vjWTaKsmUWgG8106ebWBRW6ugob38IQb-_tCvH4w8QSXBewJXKpiE028QNLDDYTnV9McKXU4C3xBrQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e50f7441c.mp4?token=SFy2BWD6Q9rcaiZXM22HkRagywwlhaDUZaqm__h7QTwd0lsYeRPpwYTbh7ZjWtqe7DM2eXbikj8uT1QsGO4ojEqv6EK-DUHa1pPeEeX5M1lKFm2DBMYOhG4VoEF33AmLVS902O9KBOGUSDDjmlQlN4ktwBCLOuCcXMVSB0lcy8qRXggPJawFhpuwQcpidmASSMR4euhtdB4-YIpvT8fxno8xPg2dM6oDH8ggQ6NeCsJ1CcGscZD8ddHXk88VT0qFLeadle2vjWTaKsmUWgG8106ebWBRW6ugob38IQb-_tCvH4w8QSXBewJXKpiE028QNLDDYTnV9McKXU4C3xBrQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عزاداری هیئت‌های میبد در حسینیه بزرگ فیروزآباد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/farsna/444722" target="_blank">📅 17:46 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444715">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WlHHQKkf4TmJq48I8oZCzBm3JQiLP9K8zeOYQZB9xvCrwpsVCAHtINV7Tx1MEQSLFk-rM0k8GbAt6odtjH-Uy4WdBF5HPQosGYk2RAXLGlmq2RY9Ef2pafJl92PEBZM359ijstmgUPldb0HD3lUaKoqgwpz3Douibrag76NnGqA2H700xbedLO80ScV5VbGY85BWVmji92XbQ84LNg1UqmDwwoqZ0gIAp77W8MWyaKSAb_ktJ2abUQiZVe6W1wnL_-6Ggirx0D_uBpFWLSQz7rAWtrFftlkM1B8_rQ7uLx2U5N-hg269TOwJly9PdhUtYQ6bj_2QenGxwO4lIbWCGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/wAQ4bzfFcdn3iSBaiEJujtqSbvwPOHN2dwd0TOS_lT0iGGj2JNrYHDyEWgz5NufZcn-xUTt5FkLNeiJmoYx9KO3lHTJPrHRxt1Mwnd42nlJR1tHrZcQVotBu2-8JGgiwKOmOnZ6gZ7h57fAXUsSK-Cw8N-NiwXeu1usInW72EzA7PbbmNdSmCJj6_Bt4lLUzKkm9TbKAsrd6vT4G74dUuO0VHA7PqgF5OBRh73A17N6-gW-so3jUwjTbrHvbXwPJG7gLHWEtJ8lqaLqWffVWuvbnIek5foxKbBuFHq8t0AdmOVk863eiuoGSWASAFa6bY2JmBLzzJTax_WZpDmIbGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dgsb-fDuEaxxI6kmJv0dhL_cwlaPY_2oEqcZq8hBuyxDL2YIenX1yJgFsYpg-fwP4a6VFZqCtzzXWe-Yw6JXlIgF8X1dDQqlMAGttM3ZvIkkuklIv1NcGo9-9GmBWwJEJ7W5-MVg9QT_I55PC_pTkepAiSnsH50nU5JE9cgTQ64tg8mflgeh5JsgoFph2vo-WKs-lh7FqUdMDej4LaqD9lRnCv4AzA2i_-rf2_G55UN7rz6BA_o5l-1DmuU7FhOSKAlAIHxpVDfuf_KP12vr07ygQt2zQI4Vv4sp11Hz4JsZ_An8W3RsiNnsZwvFMJZ1dSGeXxJbf7I1harbrjeXrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XbEY62NnvidTA_KZADB1VipYUrvagCvski-nCx9EvLI6W7PYvI_M3ruw5r07XRqQdf3PH2HJl2A6HiGI1cvOQXdlY2zaQM-WEPI9fgvv8JBFsNXcinqqBJIACJpZDP_PFESU265WLfzrlPbisYyVI_yFoamXhVi_Ml2EEOfOJSCc_GduCH6xTyLL9R7qCFjtEBsjAkO7CdRtx_L_nsS5w-iuaT9dZQTDWlF-BHKM3HdwSIcxCnw1BVxFcZGosOj6Seyp5hldDoevHMMVp79BwMEH_4k2Hmcnd-yfeC0zxF0HJd5Jr0OpFz0vYtcvPo5mBbPmP31qUxS93cFZ2flKJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EnvTXi2F_QsbFDnruNivK3CZtlOYt3HVGFGRULunLu122EScQZe3YHjtE2EmjOUctCCvDeYylvV1IzmQjbb1DdXebCIOZbs8QAAFlkxeIWi7yNnWdxJqRARFcV3AQuAc1JqlAE2PFAWHmQz72_BSSQDJJ2cr9s1CFHiMJ93_MzwkJta0i_pA-WxdIozc_K1nmlwI6ttmm0IlaU9E5RPj3DclkqGOCXZCXv1SUg2OLm44Xq_p1efPsNtkfDVuA98ApPRC_NyWUV-9NnV12PYBGjW3ZLbmSojiEovh0ty3VtMzzYeNpDon2X9tI4R2TUXuoQdUoqnxxfa6pcTF5VZwsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MOEa9YZTIli1Yw2vVkb4r0rx3oYfsu1drsNStwJPEQpCGXHfokhu_nvwM1wj8YuXbXUrbCXcNPCyw8mQ2MqylEQgONmn1NLjhncRBzhtNTmRCHK0uhKTMfD9RARADN0B38hWv83DC0Zhwm6Oj599hBtuIp70vnNiO19oP8lOvpYhciS-QfwauDNLN6fh9e1hBw3H7FjOl9_clBJ4D9lvnhV0XXOKsquNVVhMrnx-pubjytJKHFUof8CWZvKCtShMUOB17XmQB2K6Ix5FhPmh99ZggpMfTW33rGGoltWwc4i7F8B7Wx-WuxYGbQELaIoF3m_C0lRvqD75FrAgJFBsGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QexInJELG4jAHPkq0fyTzyIkQMpzeXfFIFk9nb4XwoVww5qNgtN2TGzgzKEECy-j4__xqVjp9zPSu3gtmpMZ_ot4nfEa3_44hO4h3q1bmVa1Uo4_HvH4LfhTBgs4EqHG-hIM14BRl8pDnxzqTmj_60_nryupKpvuveIQhbtXRqmxlroMVDG-gabvGndX-dLfLwiwfuKyTTULfEUjcqIRYwH7eUWfbCKZD2IVpI2XVzzP6UR9I_7KhOhKMDHMney6yJlbI_q75lpLkOQjGb7hIoKrbrAuoJPFZ05vxdYTSBqXDCZuauiQJmuCeRcjnIfdjQH1rl-XignhGFP_wtjg_g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نذر سرخ عاشورایی
🔹
همزمان با روز عاشورا، جمعی از عاشقان اهل‌بیت(ع) با حضور در مراکز انتقال خون، نذر اهدای خون خود را ادا کردند تا پیام ایثار و فداکاری نهضت حسینی را در عمل به نمایش بگذارند.
عکس:
نسترن کرمانی
@Farsna</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/farsna/444715" target="_blank">📅 17:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444714">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76c1a831b2.mp4?token=aTx-ZmW99PgCHWGYMDpA-8JuiiLIazPSYi2RV8zvwlF6_fBsbqY3QnxXBsugrni3N7wfTzrnGqu7rE7je-w_R9k9kH2qjJeLz48uhjL5lbmOqUTKKxAqfEOFPv9W0WcUrxH2Dj44i-HbhCAZjzlmkbY0GP70XIdKvC0xmkeBQ_iFLaCYjXida1ASxTIECeAbfVtbtWJL0NWIzCQeKoULUF8sAziTQ7CsqgH9JhECKS60OGEWMeK2776Y6tzFY2XEnKNadJJ6jciiY7YUkcJTvgDI6ZUClQSQySANq3iMRdJ688ie1zklPAehNRMrtaFnI2xXB1oBlQNhTFrkwdSZ_Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76c1a831b2.mp4?token=aTx-ZmW99PgCHWGYMDpA-8JuiiLIazPSYi2RV8zvwlF6_fBsbqY3QnxXBsugrni3N7wfTzrnGqu7rE7je-w_R9k9kH2qjJeLz48uhjL5lbmOqUTKKxAqfEOFPv9W0WcUrxH2Dj44i-HbhCAZjzlmkbY0GP70XIdKvC0xmkeBQ_iFLaCYjXida1ASxTIECeAbfVtbtWJL0NWIzCQeKoULUF8sAziTQ7CsqgH9JhECKS60OGEWMeK2776Y6tzFY2XEnKNadJJ6jciiY7YUkcJTvgDI6ZUClQSQySANq3iMRdJ688ie1zklPAehNRMrtaFnI2xXB1oBlQNhTFrkwdSZ_Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نوحه زیبای مصطفی راغب برای امام حسین(ع)
@Farsna
- -
Link</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/farsna/444714" target="_blank">📅 17:17 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444709">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cyJxtJTyXt1jUvredLIXiXiYAOOvlfQbu4v_HYNFBaySOdzlU028HdpjybhJUJrQaeOtePC1fnboQnsyrL9TsaT92F6DhH69QJVgeLWTOoqk9q6sSNAmNuUq8X2w1QJiE83I7Ur9xK9Iq5Gj9tZ0k4frnPhdEhEVjmN0SluxcX_o9NP2RIacjQLaCNwBDDjFnRc34u2kz9VYKaoArZ61OpaGLfk0OJDyzpB1LS67Y1w4VP0qvSkt3Btpu33B9v9EdV6CdgDoxs--El7GaP8j8lOYWPoEZL1SrgKeCEZrWMErzSWuUB8iKmSEfg3UucDw3OA3WachaO7ttSPhn5aGEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MgEgE8frpsmVy4Yz9DXRUh8vMNMA-DszK_yx9JTI_foH-WWuK2DEvyJemsGs9anzx-uYw7CqTu67zVqSfAQwlvVV1oCmR_zbAR_pBo5B7CZbvyAaj-korwTZlPFdQ_rZszU4h4s_dN_TE2XVJVIqAVjWJcboKBTG6sYZNVNhJt82PZnkixoWAt-JB219vuQF2m02g_Xoxjw_WYnF4TAr6Wn13eRI1wtD7ZmobpAl3XHkUJTBAFMoXog-MF23pGi8o1xrGZ2mZmgqaNPzd22VP4ss3MDRB06nZKG29fbQtENENUNsBHkKG2hColkeFVOp_SfQq_rDyuBQ9yvIvQIpMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VkXEo60mNVN5Y9lleiVmWzSGv8QOpRXfz_tOzKHulGI74ApA8qQOtNiaM8ReQ1jsFuDF7gF8jBGhED6sjv6i3q-DBK2HsScJTgQpGRMJZGEfl3e1ZCnaqsjJFr3Qh4aKNog85DafRSapJIiAtis1JtmzdnyJCUmKAarW0S1KlZs4FAoN9dP5YV1c1wPQcwWBudT_Dq4iGyvlxyvrb0NJqwg-m8MwdPz_Dnwd7O4afPl0x2K-Wm6-ONEjopf26I5CqYXiWRIOzP5LWQmD9gdgZ8KfrO5Qub34W1NOMqDdOj-6VhxC8XskCSwrzMmBb8RgBZxn5PIZoQyK69hDC-Rs0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kYqBsEKqP6y3vWUHb27mvCXz06gIg9ILrfSpmtjpo7oDCMj4QaD5B-CbghyD7Hr3cP97r1RfuaP0vMAzbQn7gfOQKxNksLp_5mWhlP_qzK34A0y6YrPfIIlWsV3LKUHa-w5nwcxOkYrbtV2mJu4jQRiAu8rcKvJGjujLj0gqKD63Ch_gEA6el65zKiqJt56JBiZFrz_MnzAWlKKezf12Y2HgcW6Cf5Pgdw7SxnYeiDKFPfxgzdsQgEeOuL6xdSgczCoJRuHzhXuKYdh6rv_1C1aRiUJqhYUhvTdbdltQAEa0AaEriAXg95qDBSGI1SAdHzAdha3T3sA9IYELOZfd8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vMSVoOD9HkWjqHgfFT4Gf62DxX8E_mHMsdNXOJYpyEXDXGGRMgRtNOeHslIxLwtwKbthnJuzs8tucafDmbfmiXfQB3xxbH8zModLTHCXE8cf7HgYzdaXGxIHGq_ZcnvcSS9FXZDVta2u2OzVm0kf2RHQ6og__jtiLDFU1coRpaD7XAqNG8IKYPZTN59JhgCnh7q-zSsJgjrqPAwMeIA1Bd0rj-GRq3zz-YQ06EIP3GtvfHHbZ3pRGxcf4JDF6nNj93es122NvhgWg9gKLv6j6XYLd1ZDDm7_DyyYob2xlaVBDXDCuSC_oJnCOFRiTNf62HhOFPetV5dBccuPRxTqfA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
آئین ۵۰۰ ساله خیمه‌ سوزان طاقانک در چهارمحال‌وبختیاری
عکس:
رضا کمالی دهکردی
@Farsna</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/farsna/444709" target="_blank">📅 17:08 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444708">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tfaGNgfEbWdnMJ0fnCBc1QIh4vi5QyBLYcQBR9_Lh102ibTBT2eWkF6R8-xFL9lkZF9UTzEB_5DNmYqIInzEOkTGZFQkBxtHUABj1xzsj0FJFJ7cL5gRuByPg-0tie3msj4XtCxE4Qpdg67C7sLiFLU2k1rxFlqx4pP2JcnrPjLF6xaCEyw22dQCahylLaGNEi2g66YZVBcXkBU7RNOvfceouS9Y3N7hFc4xwu4BPU7wPhNbYABCiXi5xkWvtEDm2UvqChG27Rjo9KsoJT9hV1S6VyCtE6ublknois4feUKhqvTECjerHEBCN_6LUDMhYYLwDcuf57nWN0iTNlBUtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
وِکُنتاکته (VK): فیسبوک روسیه، ساخته پاول دوروف؛ صدرنشین شبکه‌های اجتماعی روسیه.</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/farsna/444708" target="_blank">📅 16:52 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444707">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c47800c124.mp4?token=m5iSYfKDpK7Z137iORfL_Z1f6gxUMvjQCiVZ56IQWWc_3O32nqTb-EgH2eMJKVr-RhtW_ZftGRRLCTaCAN9wrcyY9cwsig2FE0vNssCHdXRHP48rm2_NbBYvwhAINIlBuJ11pBjYGNK_XOQwILpezRxpB-Gc5kH0RQ4NDYbPNbIu9kHcbclvzYK-d-BDLA_X_OOCBYfzBYIS1np7CkrXhRzNFmwNBgTi65gQv3HrR9wNYKgIPHlefLOLFvSqknkgUuZyVoTqUF2rgw_-ly4n3r0fy_750ZBVLy75Jrw4QsV8Ju77uxR2SdDBwST0hUWg0CeBQO-b8VvdcRhej6Tdv4xJDeka1dhMU1yN7KfLmdAYeuhfN_uHzvI2HgVUbQ0e61j9UeJ1CE065uGKU9WTNwwpJYLTMzHT7P4k8PgSmfbBA8yi-Vp_5eN2J3rysbDn4BQ7aq3NcSQFF15f6HlJ5dEveM-UmviF1o0AqclJ5sJLewPzBOr9NNwSW4V1GNJLQGwa_9KV_3nrMutRISLj4OWzChCLwQ14Sy0iLjNHpFU2J7ykYrr0umcu78iLOhbfdszU3SfuZRtmMEk6HvE5zzZke0elml0IChjOYCHO3gS2F931fN-GJ8nBt5DECY0cqvvL6wIDTEJ1qMveELVToHNqnq8d_97MlPDyYjmo-NM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c47800c124.mp4?token=m5iSYfKDpK7Z137iORfL_Z1f6gxUMvjQCiVZ56IQWWc_3O32nqTb-EgH2eMJKVr-RhtW_ZftGRRLCTaCAN9wrcyY9cwsig2FE0vNssCHdXRHP48rm2_NbBYvwhAINIlBuJ11pBjYGNK_XOQwILpezRxpB-Gc5kH0RQ4NDYbPNbIu9kHcbclvzYK-d-BDLA_X_OOCBYfzBYIS1np7CkrXhRzNFmwNBgTi65gQv3HrR9wNYKgIPHlefLOLFvSqknkgUuZyVoTqUF2rgw_-ly4n3r0fy_750ZBVLy75Jrw4QsV8Ju77uxR2SdDBwST0hUWg0CeBQO-b8VvdcRhej6Tdv4xJDeka1dhMU1yN7KfLmdAYeuhfN_uHzvI2HgVUbQ0e61j9UeJ1CE065uGKU9WTNwwpJYLTMzHT7P4k8PgSmfbBA8yi-Vp_5eN2J3rysbDn4BQ7aq3NcSQFF15f6HlJ5dEveM-UmviF1o0AqclJ5sJLewPzBOr9NNwSW4V1GNJLQGwa_9KV_3nrMutRISLj4OWzChCLwQ14Sy0iLjNHpFU2J7ykYrr0umcu78iLOhbfdszU3SfuZRtmMEk6HvE5zzZke0elml0IChjOYCHO3gS2F931fN-GJ8nBt5DECY0cqvvL6wIDTEJ1qMveELVToHNqnq8d_97MlPDyYjmo-NM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حسینیه حرم؛ عزاخانه‌ای به وسعت ایران
🔹
محرم امسال هیئت‌های ۲۸ استان کشور در «حسینیه حرم» گردهم آمدند تا در جوار امام رضا(ع) با همان سنت‌ها و آیین‌های محلی خود زیر یک پرچم عزاداری کنند و امانت‌دار میراث ماندگار عاشورایی باشند.
@Farsna</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/farsna/444707" target="_blank">📅 16:47 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444706">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">وزیر خارجه ایتالیا:‌ از خاک ما برای حمله به ایران استفاده نشد
🔹
آنتونیو تاجانی وزیر امور خارجه ایتالیا عصر امروز با سیدعباس عراقچی وزیر امور خارجه تلفنی گفت‌وگو کرد.
🔹
وزیر خارجه ایتالیا در این گفت‌وگوی تلفنی، اظهارات اخیر دبیرکل ناتو درباره استفاده ایالات…</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/farsna/444706" target="_blank">📅 16:46 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444705">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SqnZSDSYbzi1DCpc2PiN_CdBy7sPJptrievOOTLOgUECCrS1W0Uc__V8zHItcheYlauuP0lH12tWLKsjY1uALQABj3GtP0Y55XYFYvx5xJwiwIUfuFU6QVymwBheRmOY0d4fIlOVctLLqL_L8n3ES4HImnY68ftqPHRtKWdbiGdpumRGdbpI25uKD75o8yA6huZwIDqleWOq6BRAUibYEvh_86MCCJ7pcfhc8dP3PSv30TFD4b-8_SeIFQwnXhqI0PzOet8mmW9TySADW_TX5FjFuzzJjH0YvTHteCGu86g4zaLOpo-wksZfaCuPxXlK_QPAegFaUMKdYfpK7m8mDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه ایتالیا:‌ از خاک ما برای حمله به ایران استفاده نشد
🔹
آنتونیو تاجانی وزیر امور خارجه ایتالیا عصر امروز با سیدعباس عراقچی وزیر امور خارجه تلفنی گفت‌وگو کرد.
🔹
وزیر خارجه ایتالیا در این گفت‌وگوی تلفنی، اظهارات اخیر دبیرکل ناتو درباره استفاده ایالات متحده از پایگاه‌های نظامی ایتالیا در عملیات نظامی علیه ایران را قاطعانه رد کرد.
🔹
تاجانی همچنین با تأکید بر اینکه هیچ‌گونه استفاده‌ای از پایگاه‌های نظامی این کشور برای حمله به ایران صورت نگرفته و چنین اقدامی نیز در آینده انجام نخواهد شد، تصریح کرد که هواپیماهای آمریکایی برای بمباران ایران از خاک ایتالیا به پرواز درنیامده‌اند و دولت ایتالیا هرگز مجوزی برای انجام چنین عملیاتی صادر نکرده است.
🔹
عراقچی نیز ضمن قدردانی از تماس تلفنی و شفاف‌سازی انجام‌ شده از سوی همتای ایتالیایی خود، بر ضرورت تکذیب صریح و رسمی این اظهارات از سوی دولت ایتالیا تأکید کرد.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/farsna/444705" target="_blank">📅 16:38 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444700">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bqYSXjNFF2xgXMN79xIleCYuyyVKTsRzy2Np1WVTohjNmujS9DvLedqAzUlRbkuN2qoO7twWZIF2jp3bEMXN-HLjy6i_-Id13j09zuZpRGo9CNCT9sknSAxMfu0MgvIc3koE8ni847O4I3r_RYhwF6yVkIPjfOhqRgrUk-fKk95cnrJfAsbV2ur_MXN7nMp_HePeBJ3CTvRHfgggBJjS5MPPk3t-NyiQ1rGQGa2gD_VQ2FZalPfyvAFyBH9myXvew96QIJswJflPgkVIEHZgRtnyXmTNyddw75NaOoN-SKo3w6v6LfhkfttM2W9eogjm8rtVfIeLbUeoB9CNWj5z2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fUij40DVB5PF79xmsK5Ql7S_Cw0Pu7hc4PKuW6zQb8U14E7PqKnbXo9JlXAZg5fLPJL_ZdM7r_RxTfUoHSD9lFD0pqA4KkBmckqhhFn_hbmaSziWRKkoKtr-O7XSDIY1pe2Zvc5uOsIdeP_nx1RpyKVMbS-1wAJ4RLWyPkpAl4ZD9Y_tsbiCWaAMQ-RuurZ5z7OUJnLL6qhoYYfl3x1UcOc_O4eQA3qGRghwlA2XgltyKm4qKfSMf8YxLDx2XzGUa95ZO-K5SwazrPVMLTai8rE8iLoSZyOFGkgDYnLmkjQyb4WYYUCrvxdzgqFtbkXqK2W64u9Vc3fy7esS2Tx-UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vHTSyYYzlO9zLXs-gi2iTLGNiqNR_g8JRbqoHsUY0F16ERhqdOfYofZ5PBEbIR-ofSQCGnISWaPH9VdH0dMqMSeHspn86vQABXVcT6bpe5UXHsAoFQuY5vp_sYikH29gXxX6qwaOj4IX6OByU0WGADgxh216DWTT-7Dqcn0GwR_W9ff0b-JnekrE6cxJ2AFkQ4eJj8D16S9jDpdKdg-Ec9kgtC5gjZCx0eqNda3EtLDhfE3DE6aagz0sa-g1bhVpBRd8J49n7AhwgNJjgKrAZfKgnhGNSzigrdOlcJcSgXWvdbT2eFdnqxP6sPVsoRZVTIiSOXsQUVACQStOBSoCcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p3HffwLmlfL1v1JYQSRMGq66IMElah-tmCQiUPNUM50i_mZe1kK_-79TE38X4kIG2EJHfWnCKNTgdS6bjNrRik6MJzbCojCg0d7N57FrHbkKjPUB1--fZ61o5OzivoHxGX0snZo7FPqDOugl1HHap2hxNCidwOWvgpS8IP6tK8HM0XIAUXxdgtsiKsGulx-GBqhPHTg0Pv9aoYopM82AhtGN9NKmJM6zUsgpkM_NbihlBtDTx0wAQmx8Wb55T42F6J4d-oYC7QDQ9ET4-5Ld9Xe61qEozBmIqnQv-c26lJ6Z8x7srqkbkriYnMHD2o4JKsBTS08b02JLQgyTHk_W0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ez4emh_fSP5FF_xPlZthQXNkhRWTNHHD98ntQaj-hNLLGjjK74eHZVdKSBIYkk0SLBniQji1jxYi58q-81Cy84UydsFOPLoZf72m7AiT7cINszwTzz0Q2Si61Qehoyq1vibdrEbxeSL90a61aXEW81t8-HbIhZM9UZqQirp1VrIymhtPSJFAWYz8QhAsa-SacaIofAqyTsJEjlch8xwJ7XGGRYyn-YEOMUoxjtyQYOyAslpFDUxehruRZP89aDNmMHmSDKitOZnFIXp-uOKARs4iQQ8-bltY78ietEUdgLzVfKENPnTib3zCavu3UnxGgYrmFoojrU3hhURFKH2CLQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
عزاداری عاشورایی سمنانی‌ها در صحرا
عکس:
محمدجواد فرخاری
@Farsna</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/farsna/444700" target="_blank">📅 16:37 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444699">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبیمه معلم | MIC Insurance</strong></div>
<div class="tg-text">🩸
نذری از جنس مهربانی
جایی که هر قطره خون، امیدی دوباره برای زندگی است
🛡
همزمان با ایام محرم و در راستای مسئولیت‌های اجتماعی، بیمه معلم با دعوت از تیم سیار سازمان انتقال خون در ساختمان مرکزی این شرکت، میزبان پویش «نذر خون» بود.
✅
در این برنامه، مدیرعامل و کارکنان بیمه معلم با اهدای خون در تقویت ذخایر بانک خون کشور و کمک به بیماران نیازمند مشارکت کردند.
#بیمه_معلم_همراه_هم_وطن
#اهدای_خون</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/farsna/444699" target="_blank">📅 16:34 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444698">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/farsna/444698" target="_blank">📅 16:34 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444693">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nWn45ZmfVvFRtqyaJTp8Skdeeyqo6GBfTli6aTFdrQZ6YkHQTXZ-JJyXhgaKup7flfXQd2Y1P-7hQkMXxIYoT8UM7ugbaXxOgsbi5OisIzNjn713wvj9yh0Zkymk_o3nkcwlPtNzGe6RSnxXJni9sH8VBkTouxF7B_lFPINC1fBSX6tGFmKSrzl095QgyF1ISKrgVl2H25CF9jAcds2ogkkjN02niG8PM7LkwcoiQXQrn1EO5ogs7DndsskfdgxaHj2V6xooSoJL7YBCZDiqVT0pZXYAQVIFU0FHPmjQSfKqvzQutcpjMz_4nBZvY-_nTZQ89Mu0ZsCCSJZG7shXIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gnk8-nFOdToTFOqa7OiuoaLVj0mo-tKusMvzaEY7TFvv4bCpjEGhR8-KPfaW3Fk5BCY88ZjfCaQ1AVkNm7zDUk5mq7nCRvGxRHUQO0aBHiAL_gftzmJlI6QBxd0AK_GDysMc555uboGlEJp1iKOAGcqTyPn3HjsM9XfQldokjXS4cdKiDMizwYG_IAMpVm2AzYYhaIUxDwkmxigTH7H2qzUCRsFP-mDOp-QM0zoaTZBtkUB8DyHGAFzssO4-ofiRV-pqpJB3STSMMZ0RFz6jZOV1Xa7f7uy8KOoZQFctknSOGotPlUr2JAOldy7ilzzIbgvIPeUxJHC7bCuP4xguoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kBFpAQLlpyo8wpXI2O29McegybSfW_UnSZmkv4P1zuG5bzGLbhGj_grC-U57mecWfdbxzWRih8icHRN3WM-OZdWxSGEuXfi1PFf-nda5YJQXIR8t5hK8mg92sWlnxyPw1FnCS96zbu2X3K1ySpnhSvSa1Lg-Us_ev9gQBvICV9bONQVc4VOvMe8o-bfB2XJelxUUYZwFIHZToZxj2wKsRMMFCoTQQUd7_mVq6oclk1SaGjDqba8ZubGQKZh1CjN35aPcZ1mL4M7ZjCHPAAp8tiesEqJrpGL2TzDTkBb68tnhmMKrhnokCID5eN3UxX_U3lzmy47gAXe0khOK-CDh6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SPw_jzZ7EQ69qX88EgLD077dZM990bxBM6FCcb1wDW6izlYFyZkAyEdIuweJeqJWKW-gkEefjVpW5Y229kN_vVAeQ08Ia8cYoAWbLfj4an-jYpd6n5Ty21UVAOXLj9_9YiYpQ3inFl6XpGEdmmGPafpgpnOduw1NbgM2sADszj2Swkxnp8sA2cZPlO1HvwpFUbsw2V6V_wvEUWCJhbRUxcJMH0R6BHFH8UUpeyZ-KZOAuuR_N1Orv6hwMHYD4FZhnSotv392tvtV8_dKdXROqEHWwxk0VaWyhyO5Ylp4UAJK4a3OOwcuAxYpA7TADBuDnJcrRY1Ne5aa_VWkm8Ynag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rBtMv4iSWqjU55CmjMkSrlT-3PTT1rF6FbH_4tml2bOeotFiHrPVljvUniRdBb4zxUY30tXIUeAJEwAnttiQYyLg_sRKUGCL6S3V0LvOEymw7md1PV3Xj1geEBLL8Zbqr5gFtnliipB1Jw1JqtUSJezP2ibjrfBLfbF0w3j-UmoWgtoKNEcqYSusgvAbi2sYo-dfPgTE9Tced4J0bewstUiDMngTMLfrbR0qHAvmkwOVqPTAEG3dO0JRlEKHL9ijeFOn_pZ3W9wSRSLluBPJC1kipNVYrsmnj7SkqrtWjLx9Dhn3pNLBsGttXMgzMy1FWyTBJ4VSR8YAoFDOo4lXDw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
آیین خیمه‌سوزان ظهر عاشورا در چهارراه گلوبندک تهران
عکس:
محمدمهدی دهقانی
@Farsna</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/farsna/444693" target="_blank">📅 16:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444692">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MSbsS0P3N63E-p91BlgD7oo5BYv2zFTgx2S7g4KLFyTbCSwIG6ZNK-qU45p-O_wV5thLMwSfyJyZiIJB3BTJ9zEQqqmffj-Vec_4jUw2ZU6GEJhtWwJo7U2CLHxBMTdnOC990ATsb2dr390wwvNosR31wIMKbOjU4f2GY-xkPJQGkQp5Pm0mpj4UFv3WVSOpY-wkE-eGnIRYki56HMX8Whok9J_JnObaT8oEzSYfOnd-9qkICYYIZcE1YlsGXW44h3R42jZNZ6wdsjRfUOH_rruWbbl4F0GLM6as97tYqQUOBi6pBqttGOVSavQ6bCHlaqH2ujTSJizzGcmQ_HTz7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: پول ایران را برای کشاورزان و دامداران آمریکا آزاد می‌کنیم
🔹
ایران به ایالات متحده اطلاع داده که برخلاف گزارش‌های دروغین و فتنه‌انگیز رسانه‌های جعلی، «هیچ عوارضی، هیچ هزینه بیمه‌ای و هیچ‌گونه هزینه دیگری از سوی ایران از کشتی‌های عبوری از تنگه هرمز درخواست…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/444692" target="_blank">📅 15:55 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444691">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d20af7bcf.mp4?token=Gvtvsl23EJC0Fawm015HVbiUn1JxFtVCUwbpflBg0zL_32pkfv1oXsbsZaXA8xovU2tcWxlg4LI7yKWqVlkYV6v2-RGTaXb3prXCs8OnCUwUG05aMcp0PX4qsRcz7DCoDl7NPSfPf2tBrUGjKMQD58Df4mYPqWStyvMVcqFDtXzMrNYHZHzuRpkgMCje1-x9gHyVA8LzedtPIji4vSHZUoTuQyz_7b2yJZsNiM0IXg6Yq1ZiPvzfzm5P9mTGlMaEANDoYuFUC8hUVRP7ay32CxnHQ-LoncgY1LTvvLR4xaHcSRmEQxf9kiIq8Lk8etuAeh_zrm0xa3M0T43kZ78LJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d20af7bcf.mp4?token=Gvtvsl23EJC0Fawm015HVbiUn1JxFtVCUwbpflBg0zL_32pkfv1oXsbsZaXA8xovU2tcWxlg4LI7yKWqVlkYV6v2-RGTaXb3prXCs8OnCUwUG05aMcp0PX4qsRcz7DCoDl7NPSfPf2tBrUGjKMQD58Df4mYPqWStyvMVcqFDtXzMrNYHZHzuRpkgMCje1-x9gHyVA8LzedtPIji4vSHZUoTuQyz_7b2yJZsNiM0IXg6Yq1ZiPvzfzm5P9mTGlMaEANDoYuFUC8hUVRP7ay32CxnHQ-LoncgY1LTvvLR4xaHcSRmEQxf9kiIq8Lk8etuAeh_zrm0xa3M0T43kZ78LJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
وقوع ۲ انفجار مهیب در غزه
🔹
منابع خبری گزارش دادند این انفجارها ناشی از حملات هوایی اسرائیل به غرب غزه است.
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/444691" target="_blank">📅 15:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444690">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DkBCinJvZluoONtJ-TbGTqzWa3fOMUc-JB_s7OIEDF2MYwvta5WIIQ1oRCOnwdlhIUAq4ZkxJUnHDrF50wEgB0vQ1mPKhsJ1yI-jU1tgz9nJEzgqGH2ntXyxJJEgvVUHBvXI2sZtxoaQzu2mQpU9BIyhlBCXenRy4xaddaYMhMBlp9Jpnd8EK9Z4mtKYufjs1qmBieox9JDO9oz5Eq9z7dxtJqm5SELQMq6deoN3041oIs7gsVHG7oMf5k21FzblDARvW9BW1DkQJi2d95rczf0adY7TRB5u5EI5CV3ElEUdCzGisjh5FgplVmmvHlVBvtwFENaOGJjyLzZJkGmCTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تردد دریایی در تنگه هرمز محور تماس تلفنی عراقچی و همتای عمانی
🔹
در گفت‌وگوی تلفنی امروز وزرای خارجه ایران و عمان آخرین تحولات مربوط به تردد دریایی در تنگه هرمز و ترتیبات موقت پیش‌بینی‌شده برای دوره ۶۰ روزه بررسی و بر اهمیت تداوم هماهنگی‌ها، رایزنی‌های دوجانبه و تعاملات فنی و کارشناسی در این زمینه تأکید شد.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/444690" target="_blank">📅 15:22 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444689">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ace3b66cc.mp4?token=hfamaAc4VMNdfE7rq7R7yDWSkasF3m0Sl5fm1mH69kNjbP3M5rWK_pqn3p89OEJXOEn_wwoy7b4oQHeEPflMlu3I2sR74QJbAHXrTTp3qVJqMMOf_iof_cG9wN5Vk5-m2mu1ah1AR0ixxGXv7TBbD7QGCC-bzIdbTv8nFcGwr2UBbUmo-qnRGJ6YepJNKA4SzuxgexKeXWv1GoREaB5RPutsvskpKPKXYt9WwauPQL68gBghagLL9LMSX0V8agK__yjlCi_vUPRoc6WzVLjhOBAnk-V8BFmVhwS7jzuFsHuKr4FacdhFeCDKOzxhuU1jHba6Itr5-I3LxYxOceRgR32pgXc-lIXAgiV1bs5LutA6WATA9o25JvOojjwTz9QmSsnNe3Ou_eYXo5GfWAji7GIY-sCFuRGxdn0enlSlV210ErnBhDBik0oH3-P5_s0K1cTGr8r0V3DKH2vhjkweAE_nfON1-Xn4ASjLH6J_JP27drwWookAD7eKQzAdMs4P9LV_M6siRhcL-HJDm9Ck8p1NOQtAvReLMWWF4FOTKBAn4oNGI4TXDIpmZP0sb-YX96tXh43h1X-BYwLGQGOzriIWmvfR3J8mVjmCK_LjuHnlGPB5--yiMOlzMUAf6XCGcl-fuodIzRShViAd-4HzXgmPVTTIW72PI5xb-JMEGcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ace3b66cc.mp4?token=hfamaAc4VMNdfE7rq7R7yDWSkasF3m0Sl5fm1mH69kNjbP3M5rWK_pqn3p89OEJXOEn_wwoy7b4oQHeEPflMlu3I2sR74QJbAHXrTTp3qVJqMMOf_iof_cG9wN5Vk5-m2mu1ah1AR0ixxGXv7TBbD7QGCC-bzIdbTv8nFcGwr2UBbUmo-qnRGJ6YepJNKA4SzuxgexKeXWv1GoREaB5RPutsvskpKPKXYt9WwauPQL68gBghagLL9LMSX0V8agK__yjlCi_vUPRoc6WzVLjhOBAnk-V8BFmVhwS7jzuFsHuKr4FacdhFeCDKOzxhuU1jHba6Itr5-I3LxYxOceRgR32pgXc-lIXAgiV1bs5LutA6WATA9o25JvOojjwTz9QmSsnNe3Ou_eYXo5GfWAji7GIY-sCFuRGxdn0enlSlV210ErnBhDBik0oH3-P5_s0K1cTGr8r0V3DKH2vhjkweAE_nfON1-Xn4ASjLH6J_JP27drwWookAD7eKQzAdMs4P9LV_M6siRhcL-HJDm9Ck8p1NOQtAvReLMWWF4FOTKBAn4oNGI4TXDIpmZP0sb-YX96tXh43h1X-BYwLGQGOzriIWmvfR3J8mVjmCK_LjuHnlGPB5--yiMOlzMUAf6XCGcl-fuodIzRShViAd-4HzXgmPVTTIW72PI5xb-JMEGcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
رهبر انقلاب: بنده علی‌الاصول دربارهٔ تفاهم‌نامۀ رئیس‌جمهور ایران و آمریکا نظر دیگری داشتم
🔹
بنده علی‌الاصول [دربارهٔ تفاهم‌نامه] نظر دیگری داشتم ولی از باب تعهّدی که رئیس‌جمهور محترم به‌عنوان رئیس شورای عالی امنیّت ملّی از طرف خود و سایر اعضا در پاسداشت…</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/444689" target="_blank">📅 14:47 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444688">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f815f0f49.mp4?token=vmswh2ULdVE-9m7ppCcVRmQLrcjYXgwRyN7LCBsGc0lEgRc2pmX2oFls25FH7oUFF1ps1tbLr1yrf488yBCv9XKTci-LnEUjmZZBAMTRnko6dtMLs1iknbDBy9nx1QCJ9yIQB8QcZmQ8hJI4U854c9rxFI1qzSgNRXy8b5V4QkeJjTnStUB0ZJOv8fR6o7_f59stOYCb7DjuERX7dgb0ZCawPYd50VWraYRhaa6LYZ00hICMOnBxnuxgNR8ohiMbdyBoTK7EfQOxh-Jx-ujGDf5yHkn0BlnGVZiOoa0v_8jo3MrUFvOsuaU5_k4dUxRqlLTc4SPUvMBErvhZVa1S-3dRwHtdVY-JI6teGNtdzwIub3SLx_ZcK-YaUgfBECM0rjXnvhpXtvpWQTr06KzFbDiFB5FxPxKkHt0x4J_7g4weyJQqeNZC1eBROxp7lF1B1SkR9HFicdhye1pOdpTVTDkX1Q6jgqZlgBxFJF02LhK1gXcjkSMMyuTdjMhGDmQezyBd1WmbHc-YdZWNMU6QaxSiJagg2pXSU3o0-xiA3weYfPZD7259KWjmUpEAPNV8n_xj9mY8ZlwwkOVG0--zaDXMB7cPNvvYvEgV4JkEpXOrmBshxUE6cQM-0ZiFFAHfrHHIHtwiAQQkEaXns1scIJv3MWhc8L3LWCe415f-w08" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f815f0f49.mp4?token=vmswh2ULdVE-9m7ppCcVRmQLrcjYXgwRyN7LCBsGc0lEgRc2pmX2oFls25FH7oUFF1ps1tbLr1yrf488yBCv9XKTci-LnEUjmZZBAMTRnko6dtMLs1iknbDBy9nx1QCJ9yIQB8QcZmQ8hJI4U854c9rxFI1qzSgNRXy8b5V4QkeJjTnStUB0ZJOv8fR6o7_f59stOYCb7DjuERX7dgb0ZCawPYd50VWraYRhaa6LYZ00hICMOnBxnuxgNR8ohiMbdyBoTK7EfQOxh-Jx-ujGDf5yHkn0BlnGVZiOoa0v_8jo3MrUFvOsuaU5_k4dUxRqlLTc4SPUvMBErvhZVa1S-3dRwHtdVY-JI6teGNtdzwIub3SLx_ZcK-YaUgfBECM0rjXnvhpXtvpWQTr06KzFbDiFB5FxPxKkHt0x4J_7g4weyJQqeNZC1eBROxp7lF1B1SkR9HFicdhye1pOdpTVTDkX1Q6jgqZlgBxFJF02LhK1gXcjkSMMyuTdjMhGDmQezyBd1WmbHc-YdZWNMU6QaxSiJagg2pXSU3o0-xiA3weYfPZD7259KWjmUpEAPNV8n_xj9mY8ZlwwkOVG0--zaDXMB7cPNvvYvEgV4JkEpXOrmBshxUE6cQM-0ZiFFAHfrHHIHtwiAQQkEaXns1scIJv3MWhc8L3LWCe415f-w08" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان در مراسم عزای عاشورای مسجد حاج‌احمد تبریز شرکت کرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/444688" target="_blank">📅 14:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444687">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r2wJu2qRzw58y-Qluw6TKTTwINqHUHnhoy_3qw1up2-cR_GSw0dnjU0gP_eoBqgcwmK563ac02cNNowDBDNsf9QQj2EJSYvnH030Hp-FP1jDsvXBk0D8PB7vLvCjFi3357ttdB_VDwZCU88UdjzUCKlP3PNsrUQYy3cZa4CitZ8utE2mfx1c6R5TLttnp8Q0QcchbwbWp8ztMT23VEH6MkNHOiZl9ZOWIjXwjed-P2gX2KtxvHSQeXAV6v_2MJYCU1EYPMWNRpoYMWOo7eVBUMW7puGwmjVxUzz1NfBq22Ui48BH-Uehlx6nluQ4kjHf5D_gd1yzlhktcWbXHWKWyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار قاآنی: صهیونیست‌ها باید سراسر لبنان را ترک کنند
🔹
فرمانده نیروی قدس سپاه: صهیونیست‌ها بدانند؛ آنانی که با شما یزیدیان، با روحیهٔ عاشورایی و ایمان حسینی ایستاده‌ و‌ جنگیده‌اند، همان باور جاودانه را در جان دارند که «کلُّ یومٍ عاشورا و کلُّ أرضٍ کربلا»
🔹
شما باید سراسر لبنان را ترک کنید؛ چون این سرزمین، میدان ایستادگی و مقاومت است؛ نه جولان‌گاه اشغالگران.
🔹
اگر امروز با اختیار خود عقب‌نشینی نکنید، فردا با خواری و شکست ناگزیر به فرار خواهید شد.
🔹
سال ۲۰۰۰ میلادی و وصیت تاریخی شهید سیدحسن نصرالله در بنت‌جبیل را از یاد نبرید؛ آن وعده هنوز زنده است و تردیدی نیست که بار دیگر همان صحنه تکرار خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/444687" target="_blank">📅 14:26 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444686">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9594452e96.mp4?token=YAWA-Q9BjJrOEBUrLX8VUWmkJw79hl95KL7Dx117CSAe5iiiT7yUO0MIpNrZgon1EORC8QibqxLg4zpWeC6JDaJATHBtaiu4ObxWRZKAwzrHjSuDkJPsF-jYUGkzH1rlCHELXf_A6qBlx7mlUg2N03BF7Ut9lV1kMCRB4oFiDDaNuYY8zqwdCBwm8xVHS0xpiV1gzNNDtez85_OON_QUjcseyxbbZUdVRVBppZ3XYL6mhKmxiGS6DAjOLqHN1FtbGLoa8x7els5vILcqd1vlL_90oGvrcJ3Mw-gMUYf9SRPawffVQiNGFRli2XP5gPG6RoB3WmKbhsdcJ_6BDemOUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9594452e96.mp4?token=YAWA-Q9BjJrOEBUrLX8VUWmkJw79hl95KL7Dx117CSAe5iiiT7yUO0MIpNrZgon1EORC8QibqxLg4zpWeC6JDaJATHBtaiu4ObxWRZKAwzrHjSuDkJPsF-jYUGkzH1rlCHELXf_A6qBlx7mlUg2N03BF7Ut9lV1kMCRB4oFiDDaNuYY8zqwdCBwm8xVHS0xpiV1gzNNDtez85_OON_QUjcseyxbbZUdVRVBppZ3XYL6mhKmxiGS6DAjOLqHN1FtbGLoa8x7els5vILcqd1vlL_90oGvrcJ3Mw-gMUYf9SRPawffVQiNGFRli2XP5gPG6RoB3WmKbhsdcJ_6BDemOUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حداقل ۳۲ کشته و صدها زخمی در زلزله‌های ونزوئلا
🔹
طبق اعلام رئیس‌جمهور موقت ونزوئلا، ۲ زلزلهٔ پیاپی ۷.۱ و ۷.۵ ریشتری در این کشور، دست‌کم ۳۲ کشته و ۷۰۰ زخمی به‌جا گذاشت. @Farsna - Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/444686" target="_blank">📅 14:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444685">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🎥
طنین «یا حسین» و حرکت نخل‌های کهنسال در کوچه‌های کجور مازندران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/444685" target="_blank">📅 13:59 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444684">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🎥
برگزاری نماز ظهر عاشورا در کلاته‌رودبار سمنان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/444684" target="_blank">📅 13:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444682">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WmOvNSjgNWx6AvByrZKVrgzH_B9-1xNIVqTH3QF2EresOQU7slh8btmmcv16vOBFdkYVrXNC5rYMilUZPpah_E36KTAVO2bHdM7IVsqX4Eep5SjvXCXe9exTtqWDOoQk993CYhUsyQE9IEJA1hqiVEAEYqQTPMkw1S_bVcQdMZUHWH0gCmTG9WZeQthDqiTX9IljCDEAmN2fENx-dUv8ZQYOrz4MqR2_BtO63ymRrYpgf9QyP0RlQrYzkw5ZpwW5WSUFdnz7UahfZZUYizBu3_vTDJcsos4FnjZLM3-cEkhzg3RJLf9jkkPEMemCNfFczyV2KsF6-qXfgh9e-eI9Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hxXv0Z7FwS_SWSZozBGvkPIoEck6AioxmWklkVAaquNj46ZF9VlcG7_-bdWVeVzp4mruGqd04ZVB99iFZJK_8Sprn-0CxanbKsVj241T_-EDwqtjd7lA9YG_-LlILyNxD8w-RxrH9ymPUNDgJmuNyegkEvhrKl3pl3fdgruT62LLSTQkqjESG979x4TY_QFhfJXc4241KZ_I8VYahhCO41RUKzkN4J4BpaLf6gZpx3JZN66OCwQVSIPlTUm_vfOHvycRixNmsX8vGAWizOZEh8EMP9RGfxMpRt_ZUb9tu__v5L2zKAZmCsJJGyXrIZAqpm1zWBJRGeiQAbD_Y78vxQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
حال‌و‌هوای مزار شهید حاجی‌زاده و شهید محمود باقری  @Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/444682" target="_blank">📅 13:13 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444681">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0611e44cb0.mp4?token=X6VrtQM-dO0NiD6XBKVFUERiFmsfYLi8Y31vH5byCLthy6TmEJsXJjI2Z0LGsx-chmEkT0RNbOpJf6SYasb15w7faq8nhHEmZOlSizAmJTuY6jwiJsZCHK5K4LU51bHQM_kHwUtNij5BkRg0qgF5pApnQaELiAn9nB2ZHBBLjy6TLi2AvWNuOoPuvIjK8SRDtBH4F4egzvbe1bel0z4ZrM2XoOSMYGDf2UBjI3umAwwcxRJIG9LbbmJsWv8gIB4Mpl0sZpaw0x9SeC100MWrQNv3nX3b9KvwfxyOm1NKh-xFZPpCW1uGnJk_x6jbz4QInY3UDF0TGFqJKyRYWY6dlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0611e44cb0.mp4?token=X6VrtQM-dO0NiD6XBKVFUERiFmsfYLi8Y31vH5byCLthy6TmEJsXJjI2Z0LGsx-chmEkT0RNbOpJf6SYasb15w7faq8nhHEmZOlSizAmJTuY6jwiJsZCHK5K4LU51bHQM_kHwUtNij5BkRg0qgF5pApnQaELiAn9nB2ZHBBLjy6TLi2AvWNuOoPuvIjK8SRDtBH4F4egzvbe1bel0z4ZrM2XoOSMYGDf2UBjI3umAwwcxRJIG9LbbmJsWv8gIB4Mpl0sZpaw0x9SeC100MWrQNv3nX3b9KvwfxyOm1NKh-xFZPpCW1uGnJk_x6jbz4QInY3UDF0TGFqJKyRYWY6dlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
برپایی نماز ظهر عاشورا در جوار مقتل رهبر شهید انقلاب اسلامی
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/444681" target="_blank">📅 12:47 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444674">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال عکس فارس | FARS IMAGES</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VMyJIE17XJGejulO_npFCT_xpQozA0-fVEMbHbmMpEX8AKUyMGLlE4fSPnoS0o6JgTSj0sYjm5_oo3cwAi1Of93UuFJZMTjaXcVn4wwIoIGWhn0C4ILW3z_K8xworn9G2qOpN0qRJkuyKu4BcQppDMtq2qTphIyKu79oGjXm51Fxuw_L3SNYlCXk1mDg5PVH6vo3UHYilYk85lchYvefzoLSJ5COvmD3HEZfzTcNmo1zrYdgMux35J59NgsL4vfleB7IDroLgKbUvEPGZN1cWvWF-ehDk1LiZc587zezTlOs4pT33l-Tow_6EdAoKV6Y52cmapjxoNnE6cTpqSAwng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DRdEqQvZ2UlvEUJqWOfVE86EJ96YoPbR1cyelezTnQgHsEVHzwvCgRzVB6_wvr4AwFX_1bj4eN-LTYNZkYPzkKQUErBp9d0x8Utfz0jtpqLfHytsSXtA8RUt90v2SKVBHD8_kQadG2R1lLT_tqDREXalsT-aSUuGOlKDjT63yyV0bTX9BbLVhWdfQH-R0TdM0A5TH535C_0qlGZYT8Lu_Bn_gXBXSGbqUw3LbbxSKlr1MUc0BAUAIUirduyq5CV3Bto-AKcPz9EABCPIHuZslbblvx71wnZ80UyBtcm4HUBJ3Odp5PjUjYHfoM1t7cGGc7O3clQELdoKfikz8gtYgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oRGzxH28IcdH2NdsQqhoVbZO2kFWdyhYULCfqGRbpuLtzN5FnafVodUuyBAZzrstxAJLDOYx9lky67A7GAAEasGm8zDeMkKGv3qEgm77rqJhqklv3ka6ogUxB7aQBvegpORAT2ltCxRow9ExbHMbs16VVSF-0LbdZbovY79cPR7MRTl289yrK6kLYiEV4Jvu0s2EmfhXi4epNvNHCF8iXb_eMcLFiLMovvzrks-GfYnPnSXKN-Lsns5_dNZfFwrVbBXkO0Eb98meYSiJiNNqu_ebh1VZxx6U2kQPykS-gmXmM5n9gAm8otxItxstjxl3YPNyqhL8nskCfGflS7XC5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WcXUeFTFALSY190IWpXhr17WQRTNXI-4q7FDf21hUdG5aQx5xnFFIwQWXDAzIXZb6KEt7-lXZYANiexrDNGxFqt2NKOfKxBcQ6vIBjMidbzBi1zyn8CbgM1bBeph3JvIDYECuyoyC_LwmlBPmslXHTCcBgBP41ZmKQ1M9jZAUFEkRLDS002OD6TVLTEYD-2w_SIOX3OyvrydVwYFZaHCTxh4yi8aPhL3ahxtdE82mRBsP-_odMDf1iw7HdnIGQutSESXqeTFHp4-eEorR9v47O7eKXbR7nIRfII7IZNnCB-a9ZIxqrMIfSPdBNE7Rxjj_8ZRHgHKx_5O839oriA9QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/voM3iVEAQWKzh1PwCeFA3-sWEiutvnoNOSZ9FpYcTuXUOpDRHKMwAABXA-3TW1YIiBazZiZ7iUcq2QurzzAqYyR_T3Gist0ZI-n74dftS3I_moVJBIt3V-9UI18-LYaqBHN-JaYPTZryfh3DxOjyVDlXLAeCzwiVQuWT7tNh_4jJOaDUXzfTzIZSQhmAHw876csrCL1a3SvVkOarHqmqO6wsySvmLI5Y0i14oLVxvDMOvDZ09EERwX3v23wU5IPfVHVfPuAGcAmbsjTgONzD8D4z0tU6PkYfV0sijQw2gpkm7kRXZXaW0Xxmx22js2eCHPEYlpkaTh-XzqBGHUBznA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jVFkzSynjN4y2kKerDsqr9dQcsU8Q2DkPXspI8Qe4tsHy8xbAeTWUTJJ7qZZA5TtkxnRg7TUkVZ9Wxtjfkm96wxe2wl-18EQmLTzlkz1muSzK3WT_dGy-2UgBqxu7HFoTBtxbacNmu2x4hTOl2POsxQtXYpCKlJ1M69n6fmKF20138ixW1EbX_EOFeenRU810NyyYCIULJuHYRMzwXBJKzMrzVbMS1W_QYaVSBbJdb_5j4nh52SJ81fmYLLMBN-AMeqEKXgqhw4JPqEfTBnOHFBM9yabErF4hPstyYXKw6RPQpB9-dQ4hD0VRIqA7hZAL7YSIeSLj0F8siVOj6gTqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TNZESwhIWgjgJg_uzsw5O6Y7X_pDmZ782QDNVBSSrESI5yfw7Gy1B-wnXBjeezg5MD8RvKkhmUJ8hTE-vb97odaVII_sNeDtzm2vmZ7J3FYz5jynuzEkOR6FiGmtxEWlEa8FrAzLJlfHWCX3xNR0dasOTburldDW3-J3AsV8ZwcHzW2P45MWcriaoTcJ_toDSv3FYmJWuAZf0eblVwf_TShH5u1_QoDUKk6AWgiPjq5ucyoKQMMmPd9rf4e-v9bRNYv2xLpj2827TJxatNId1LAJXZZaFxQ8MhyfdZeY-ADEaDOr_xkax0LnOsfSKzZxU5U7HtaS41SbG1-4259smA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📸
آیین «گِل مالی» لرستانی های مقیم تهران
عکس:
زینب حمزه لویی
@farsimages</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/444674" target="_blank">📅 12:45 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444673">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e716e4e7d.mp4?token=lmUgyYfO9t-lSHtOnx56Ls1VHaiRwmTwZ-HK-Ooh6o6FyKowtqh1KolnwV8to2UIrs8eG6HA0wELmGQf0TXrnXkrW_41Oajl8R2UhrL90VsjmZZNzOXSiJzgyqJySwniQKiH8OEeo2JHb5nIl4Q0n04xJu09ZgGlbhK9dRECPrfGmTcAqMQpjxZat1hZcWww5Owp57mEAbkoolBHJ7YjXYllU89r57iafAL-Ll1fUZgHIl7BSnWwTvUqYeqmhv9EleJPziADz6Ex_X4BqalnKakXCTWkV7myFAclYqXkHlwAfqtupk8-3crt3gHE8rvp3oA0C9rwcchBK6FVGfLBRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e716e4e7d.mp4?token=lmUgyYfO9t-lSHtOnx56Ls1VHaiRwmTwZ-HK-Ooh6o6FyKowtqh1KolnwV8to2UIrs8eG6HA0wELmGQf0TXrnXkrW_41Oajl8R2UhrL90VsjmZZNzOXSiJzgyqJySwniQKiH8OEeo2JHb5nIl4Q0n04xJu09ZgGlbhK9dRECPrfGmTcAqMQpjxZat1hZcWww5Owp57mEAbkoolBHJ7YjXYllU89r57iafAL-Ll1fUZgHIl7BSnWwTvUqYeqmhv9EleJPziADz6Ex_X4BqalnKakXCTWkV7myFAclYqXkHlwAfqtupk8-3crt3gHE8rvp3oA0C9rwcchBK6FVGfLBRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شور عاشورایی در ایران اسلامی
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/444673" target="_blank">📅 12:42 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444672">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CkBB_jtW8Ve2aCLATgXkiSZ8waKFEzX7YU3qjLvFPhoryx5mQ9AXl1NGInP4qVObc2ef6RrAQxBIB9sAqIBqldNBLxAjb6KxvzCvY6z6D0J7bssno-oSCoxksiDDYHhGx7My2EcMb74dF9YELbA4Tx7EaI5fNytpPwnBHl5OkK1c7aSXaS6pz90GrTFhsEIG_2c-O_VTn-wMDQhOHhnXH7Z1XkTgSOudHZXxoR7OjOJVCe_iq0GriyOd0QnGIUFY7fedRa7waRlgOPwmYYBY7ck6zGyPwmkl53GzKWX5A5P2MyI0uUZKngKXtOr8PAyj7046_zyAVngX5Nqtiaf6Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
و جمعه بود. دهم محرّمِ سالِ شصت‌ویکم، مابینِ نمازِ ظهر و عصر. و حسین پنجاه‌وهشت سال داشت.
پس، سرش را بریدند...
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/444672" target="_blank">📅 12:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444671">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e78488a264.mp4?token=aRoB03thaWD0Vp2TJN7acFCWGEVTaTjla28ic5D9gJfM7HlMSDrzRaiVg7gaB05LmEBMCx4h2qSYb9CkJBwXY1i6zg1KTNlnMN8VZnq4OR4JvUQ0WY2LucK-5OiVNKrKUoqDvksegHztRNB1DeM_3pue4CEHoFNqwOOkSme0Cc-o-uQBJZbd5GtlmCeR8_eRR5OAjsZ5llsURuwim4_df_lGsnChsn9fJtDqy0E5FZH2VM-WXgUEdeM8X-VJPcwGGV42AEcuqU97AQ3pse-y7ZdwC19caskGkCO5bUSfe1DIvYTFIovFFhpUCw8lra9iyNWKujqGg5M-Xt_wcThHiwA6cxZ-JwPObz6Z7Ocn6iLlj0MH8hWlt6C4vEWZfohRDbt77HWeVPiESerh8QyG_bR-h_8JMYRH4NV_Gn6zkEyfWBsIbmE7J-0akZ6KnnEmeIP0puMNjYrOIYlUE8FvHkAxW2s-gjVlrwDDwbCG2X67SPZWINDtczFGW8rOkZc-3rOBSqGJiIvhwpYMDaQ11aTZ9lcz8vQ3SzAP2yhra3JzCk93hmopZSK-3abDTnRNpWyR1B191mKrG1fRAGOUEkJIYxbVe4GGopPEXbXlJBrfSOHniT4saJHabLE1MoIt1TMqfjFHw3gLxtQQ4bWYkUPkUH3QqNfh_COqidr_gl4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e78488a264.mp4?token=aRoB03thaWD0Vp2TJN7acFCWGEVTaTjla28ic5D9gJfM7HlMSDrzRaiVg7gaB05LmEBMCx4h2qSYb9CkJBwXY1i6zg1KTNlnMN8VZnq4OR4JvUQ0WY2LucK-5OiVNKrKUoqDvksegHztRNB1DeM_3pue4CEHoFNqwOOkSme0Cc-o-uQBJZbd5GtlmCeR8_eRR5OAjsZ5llsURuwim4_df_lGsnChsn9fJtDqy0E5FZH2VM-WXgUEdeM8X-VJPcwGGV42AEcuqU97AQ3pse-y7ZdwC19caskGkCO5bUSfe1DIvYTFIovFFhpUCw8lra9iyNWKujqGg5M-Xt_wcThHiwA6cxZ-JwPObz6Z7Ocn6iLlj0MH8hWlt6C4vEWZfohRDbt77HWeVPiESerh8QyG_bR-h_8JMYRH4NV_Gn6zkEyfWBsIbmE7J-0akZ6KnnEmeIP0puMNjYrOIYlUE8FvHkAxW2s-gjVlrwDDwbCG2X67SPZWINDtczFGW8rOkZc-3rOBSqGJiIvhwpYMDaQ11aTZ9lcz8vQ3SzAP2yhra3JzCk93hmopZSK-3abDTnRNpWyR1B191mKrG1fRAGOUEkJIYxbVe4GGopPEXbXlJBrfSOHniT4saJHabLE1MoIt1TMqfjFHw3gLxtQQ4bWYkUPkUH3QqNfh_COqidr_gl4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اذان ظهر عاشورا با تصاویر زنده از بین‌الحرمین
@Farsna</div>
<div class="tg-footer">👁️ 9.98K · <a href="https://t.me/farsna/444671" target="_blank">📅 12:17 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444666">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UE4i49zh_6gni5U7OQk-a3XM7uWvHmvfuD0hxN6_rGfSfYXN9GT6CsFRRe7nU0xFrKvSd0_A2wc-3XkOINfuAiXf13hJGcl23vngIVFgyQAtJXL682oF2lqBARmUlPCJkp7HlPD9tFLd5kpXWD2zaeKjr7RuW-_ucb9fP-OzQ60AuiCtxPPv_9BiQ5Fbzj4hQxwcxyzDgqAXXYUvPjeSpl5vXh1zOHKUVRIgq7UeRxzCNFBxYsiZHewFCfo8G_JYdERNaGcnRzjfS_FlxapyLSC0pPYNjxCEogDbBbvPWxs_i4vJVB05P7ECaQZtLg4j6qs7qJmojJ8ZzDxdoyVk4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VmdzUzAtlXLtQNWPBnIYIixWxj4np_Qh8O1dFB1Q03N5rOVcznjF4Pij7FykQ6tL661j6BDgVyqPgvqINDmwKKdae2UgGt3u7pQKrbAX0fyf8JVp-TxNtJe6UZbkGDEYunOnLF4_02Df4gD86MiOcvpHgaR-x3AZPLAaBXNw5dxKqYriRZnZPDroIN__GI2WXa-5jXlbeEc7AcFQvKiIWxtYZ4Se5NM6gesyZnXPKiTYB6OeGEw31MXPlf5jLqwUl89ll2GFdI0tYDLQ_-yoCScvIjotplqTeHc-00_vToS6Att-B7WuLEAhkpGzsP3IoxXCpuDAHm6RwGo4ufYm0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KCGXzuOWwFFD30-Yh3kJUkDCOUtIkqBPfNqjgZKAY-Lzw42PxzhGkAgccGpqRsgLGHz3xhFEAWMkhCGQHgk3X8R8TgnIbtbi0AlalHM_fFoqgcqrs4MDo0z4OaWTZNDMui21CQKqK86OelhaXP30_-TWGFfZkW9IoWv_P2m4XMcZwegM_OpmOD_-DXY5IByh7gDd_tobXFWee928x9LV7bgkjj_wMIS_si5Nz4xqVt1ENZtN0D6Cu4rjuPRXoNnLAtR4fYJ1A3aXMFTK97eciOGxN8iiSeRTuXF068ZlqsbiFUUxvSiKpI1hfWt1weq9xZsvT1fLBIpRUKcXk-m9VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BMxaSe2mudbCvItTn1-b-GpZjjViwY4gkbR9mOTMcnIxQ5xoPbdP9fRop0NotYLqXpruucnbX1QFbpIjughvskDu24-_9w7eMb3603bPegI6pSab3jJy6dBco_E2fR1DHPUV8TobbaIPoFbGvdLMQgSws-oxuFcwRoIrtzX_o-DR9fYRXyegdRtB65180T9wnTQ6lriK3tH6Dae8L_5cqdGXQjc-Ib-OtRgAkojd02ehnYhSXe-pAaHW0VBNuclLFV1PDIx-X51j2mA3bctegMtBUGUpEsINtg6u7Ju5fm1GfXnE0D0VcEMMT5Heg631aeJlqmfUQCaBL6mWB_sjAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/itUGJ5cSaVroaw653rlzrE_Gjlzd8zTNPXWxUVLwIY3uBiR2hGiYjimCP0SA8JQF391Rw6KU6L--akHm6XRMxELIkVBX94vyt9YH0pgOSiP8j8wtCSwdZj6w6B9xpLFecmiiXc9m4-Cbu4aSEX9gQFXQr134LxOn17HQYL1H5iB0x7Ot-JFyovRIUTk_B9pcXGq3BscBA5Rf6u68nvwOxE8NLLFAUQwKwY_lOZyXCMZpDmFcDtT6FfD-CqUSpwsHKHpdWvZ2Vol5aIu3KnVP4bQVmOsB4XHl0acZMcWcwcI_c-5dZjnadop_5LNO3SMgVlXT2iSBhWQmjq0QjF3Sng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
«گِل‌مالی» خرم‌آبادی‌ها در عزای سیدالشهدا
عکس:
نگاه ده‌دهی
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/444666" target="_blank">📅 12:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444665">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5ebe09e2b.mp4?token=B1Wp1ZrIwKmMiv2TSP315t6a8dISNx2EOxAEzHR0dx2HIdi2JTmc_f5hVxTtr-uqhdoLbD1im4KZMUSnQbUl-00LvfzPi_W8nS5RKdxOPTC80xly3P98_vZtrWDq4V9gBMPl7f2DoLJmSz0Y8Azg5K8EOLIgjnmOfH6iFzwtN_Y2ZcScLPHdA9DmFxuXZr9YPJ6zwWfq-MhjtOR4XfK0a7KpUQoOj6BnrF4WtYKys6qCxIkJBpiM9ekHmczKu5Ae6KAEaBluPERK64WgY1r8dFDCzjn55ofZrEGWs9f0T6P4t0R0fEMIE8zrAaJnnblfDHg-ByLPY1in53lx9GTD_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5ebe09e2b.mp4?token=B1Wp1ZrIwKmMiv2TSP315t6a8dISNx2EOxAEzHR0dx2HIdi2JTmc_f5hVxTtr-uqhdoLbD1im4KZMUSnQbUl-00LvfzPi_W8nS5RKdxOPTC80xly3P98_vZtrWDq4V9gBMPl7f2DoLJmSz0Y8Azg5K8EOLIgjnmOfH6iFzwtN_Y2ZcScLPHdA9DmFxuXZr9YPJ6zwWfq-MhjtOR4XfK0a7KpUQoOj6BnrF4WtYKys6qCxIkJBpiM9ekHmczKu5Ae6KAEaBluPERK64WgY1r8dFDCzjn55ofZrEGWs9f0T6P4t0R0fEMIE8zrAaJnnblfDHg-ByLPY1in53lx9GTD_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سوگ سرخ گناباد در روز عاشورا با یاد رهبر شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/444665" target="_blank">📅 11:56 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444664">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7251299b78.mp4?token=Owc56WWx4XoMvVJ98BluyHv1HxN7guGJpWWTe9cRHaqk3OrjUBEVxYAk3AV9mrIgAHMhiMOq5nr9TIMYxIshVZk5p1iTLSB5qZDjKpQL5hQEupbLAHxcmD-tdvrmGq5qxqYDkHhikDGzOHmXRtavXYW0hclV1GLL6PlGp7ijUj5LgRMMKbWemZMvynyVOhDeD_96bUL0yLvo8kMOZDMWl4mVo78qfDrGx2RUUm-moEPPauAq49R6dyo-LsEi0chPBxsiyQkUiyfUBpAZGxQkcKONUyyZNSXYgjTIob5BpvP6jr7_v4quHDb5Z5dntc4aUYDleyacpmTtDrHyvQSB0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7251299b78.mp4?token=Owc56WWx4XoMvVJ98BluyHv1HxN7guGJpWWTe9cRHaqk3OrjUBEVxYAk3AV9mrIgAHMhiMOq5nr9TIMYxIshVZk5p1iTLSB5qZDjKpQL5hQEupbLAHxcmD-tdvrmGq5qxqYDkHhikDGzOHmXRtavXYW0hclV1GLL6PlGp7ijUj5LgRMMKbWemZMvynyVOhDeD_96bUL0yLvo8kMOZDMWl4mVo78qfDrGx2RUUm-moEPPauAq49R6dyo-LsEi0chPBxsiyQkUiyfUBpAZGxQkcKONUyyZNSXYgjTIob5BpvP6jr7_v4quHDb5Z5dntc4aUYDleyacpmTtDrHyvQSB0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آ
یین عاشورایی «مافی» در زیاران قزوین برگزار شد
🔹
در آیین «مافی» مردم با حمل محملی معروف به محمل اهل‌بیت امام حسین(ع) به محل تعزیه‌خوانی حرکت می‌کنند و در این محل به سینه‌زنی، عزاداری و مداحی می‌پردازند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/444664" target="_blank">📅 11:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444663">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91c12769b5.mp4?token=F40XWHn0fERRo1IsKACguAcH6DhT5jbmevhI6dLowfMsAyswclWRIHQjWMpeBruNcu4saDVwJxmxJvpg1wYErmeNOssDw0NJ2r4M8_KDREElj7TCS2ZDiIjYF-gtturiFmquFYumVUb2Bu4iPH5FdvtdufVuHIsQUEapdqjBK67L4g_m48qh2MTfObFcAl14CwpLdN1LqXXUd5E3juOrtqkFtVOdJurcFtSRTpCPvsNQT1iq5GQIxsy6JZdpuYc52ftz2CATx_VYUuKcAYUt-aQSPYV4XvtE325YMiSq5JwMdiHrQGVrHuUD_Zj-xv0omBPgtGdNNXb6KX4Y6MdijIN1y9cnmY6w0ej-xWeDpC_V_QN4YlTmjsfgoaFthr9sFQSteUfm0NW0JQh3F9S7BVmwEkuJJHQWhV2VNRis7CmLQxLQpjN5sZcZST6krhIRHmAlJQVl1reHZUahlh9CcSnYP8PFN0gIK1CwpidiftAurimQtxFofjxtiugrFgkktEQTf8tQPQFRXiuSMXk5McqwrStzYLhhtM4oPb2TX47MCc4FPIdskbZiI3NofZ4Z35mvDjeHcLYGxBa4JJHBVZWcgzag35Xc_1cugq5JBQMZwZbRGXdaxexIVORkg2hPRuRE0orjCpuUNO7h9VJe0ZfhbBz1M0UkHf0MDLW-Bpk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91c12769b5.mp4?token=F40XWHn0fERRo1IsKACguAcH6DhT5jbmevhI6dLowfMsAyswclWRIHQjWMpeBruNcu4saDVwJxmxJvpg1wYErmeNOssDw0NJ2r4M8_KDREElj7TCS2ZDiIjYF-gtturiFmquFYumVUb2Bu4iPH5FdvtdufVuHIsQUEapdqjBK67L4g_m48qh2MTfObFcAl14CwpLdN1LqXXUd5E3juOrtqkFtVOdJurcFtSRTpCPvsNQT1iq5GQIxsy6JZdpuYc52ftz2CATx_VYUuKcAYUt-aQSPYV4XvtE325YMiSq5JwMdiHrQGVrHuUD_Zj-xv0omBPgtGdNNXb6KX4Y6MdijIN1y9cnmY6w0ej-xWeDpC_V_QN4YlTmjsfgoaFthr9sFQSteUfm0NW0JQh3F9S7BVmwEkuJJHQWhV2VNRis7CmLQxLQpjN5sZcZST6krhIRHmAlJQVl1reHZUahlh9CcSnYP8PFN0gIK1CwpidiftAurimQtxFofjxtiugrFgkktEQTf8tQPQFRXiuSMXk5McqwrStzYLhhtM4oPb2TX47MCc4FPIdskbZiI3NofZ4Z35mvDjeHcLYGxBa4JJHBVZWcgzag35Xc_1cugq5JBQMZwZbRGXdaxexIVORkg2hPRuRE0orjCpuUNO7h9VJe0ZfhbBz1M0UkHf0MDLW-Bpk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شور عاشورای حسینی در جزیرهٔ هرمز
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/444663" target="_blank">📅 11:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444662">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ViEC5L3i9gH-WnOdtpIqaQ4y5HB8X3Ui8iUkb76Ka-GJX55_jX6OBm5-KRQtiKo3Y9WBJNSodqY64562VOlc4Sf9WV8d3I1cDDVC5qrUVjOwooAFEP4u4Nrkq35N3gZF-pgm8W8k-jZtShGhTgKWjjTnyjM0ophma6oEwelAUcIV_hC4SoreYjdtvqBf4DddW5D0xUcDu-6pQn_I3D5HPTWDZ9Hx2GxR14TBFw8nlXbdwH2E4JFQ0-tOjb8Raf-bOe1LfjhXH3TxZ_xP8ZhEpxzmYjEn4gF_QScn2Bi7lDBHXoTexx-dV6-u317hbC1w0ugmJZaiDfvUCOaXOUv70g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
برافراشته‌شدن پرچم خونخواهی رهبر شهید در «کشوردوست»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/444662" target="_blank">📅 10:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444657">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bCV0pl9hNFWT-o6zGsdySIl0T_31A-j2HAd9aDNjnk2S5wMGrtBWtI9iV7htGg-6VanfLXcikzC6rkfUUBramMHNRrnJX7rVThAWDNvLR1ue_nyktXEMqLEyNMWAUoQJP6SZNrWGQQP8kW99yOaSOVAw8ZvGl8Q3fnkWhWUmLwfY3RIm0FVnxWOx8n529yz4TP6__hTFTG85KdEypazOMPn10mWFRxfZyowJBSAtXxdyeUPHCSdmcGJ4TDGldLsrw8oOkQf-_e57o92acfuPupocADcVP4j8BnluKS-Cko9WekhIn4fEMBCt1uDADczlIgnMl7FoOFv8Ml5SVfftUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v8RSQhHxeud9ZbjpKyrxNYexo9FLKXBfjaige_BRxS3vEz_kHqSApQGaQ1gSxowSiCIth-SyDLepS5VHrIrLzYadGfswlVHsWhlc7ZLyaAUeY8snCoJ2J-REPWQ6_O9dGckJY-RNGLVWNAGyNVVtlNhkQiUXNb2g9azHKMm1xMR_1tnYMGnnKAInP2qZsGh2G-t0ojCzRysFyLvLZ-BOI-wHXEk8x94wzssQoPRD5sCICe5ygyQ5xMeNiT-At_fvsCh44ZboPi6IHmDq59-xXkRdu6Yxu6ygPG25-IQxQCIX4nTSgqqYSf1leEE50TswfHvbMWR-eS8BrFu7JYWy4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XxrDGYUnTh9juNc1d6GbPOLfFTIpp_zQBzdQ9XCv5XD56NKYye3Xw-f1_ze2JH1xK5M4K1m2RizMoAFsjxuwPZYOpFQ75GbVhUB4Zxtv3t4lLFKXFRMC2hBubyPG5kDTZVcpZ3TvZhykIZEEty5E94n3ObqNoksbLpLkeZ2p2byyxrBL6-1ENCl2qVVu2wYT4bd7D9QCtWSkUHk5FRK4xTTpN8Lvgf_w_KY3THTk7x0EPOoIro0sS-O2rhPKB5Q1044Cu0GfubMpSN5s1y5DvfsXu-qsjK38nwP7iPzOkD9rZ_kXC1pqY7DtHpHOp-wN5t5HurVbeBy4ioa9iUODvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KyWrTXryEQj3M2qz-Bm6fMvDT2UPZy3YWZrZIBhcI6ZmYWFuUiK9C6wRthJpuyyl5bdt1WK8fzA466-_2fyAhr6RXks2GUqdsf6i_fvxC_h93mtA1_jeHq6JZp_7rIb_FhOUF0DnnRiv8RtGiRxj6n-qiZmiG99kRKPIXoCzQlqgkobHbfSkSiJI3QMG55XtbTopS12qI091-q9zNv5jgK-xlwuZtmxcUW5QabwjzKISL3QuMPQnrogRkoew_OcvKxN_iI4iqIpm6F702MK0zJ8sxNp-6Sps7vj9gZ_8U26rvCdNSiwVFTTaeniN4C_mr9RmXxinRUhkggcNcs1rvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cAsu7q-6kWeoc29cCJQ6xS8uxMbqZBE0ZV6kOBfbiApfYVpykiQpnWAlAbHWQGwSDNEShj6V7m0m67_op9A7Pei1rpggNcG3-9ajCntCxTfamp0LjTv_XfIeGd-zRe97XNTWoAN86DQnc5DCN4vcbfV00mmlNOuUrar6l31RNtOHToQTzFDcczyslGh53CXpNVQAtZi3WlSs5-SDht3JXRqyYpaG8nopOrsPUyiwffVluHWfjUACy65ZRfXRd56271jwhrioA1IWFgPD2coF4Ve7Vdxlr-M_-OOxAwpF2YjPqF1O_Jy1mJWkF38gDD-MPJkpjx9G_bVV46oJxoYVLA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
یزد در سوگ حسینی به یاد رهبر شهید
عکس:
علیرضا رجب‌زادگان
@Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/444657" target="_blank">📅 10:11 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444656">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
هلاکت یک نظامی صهیونیست در جنوب لبنان
🔹
ارتش صهیونیستی اذعان کرد یکی از نظامیان این رژیم در جریان «فعالیت عملیاتی» در جنوب لبنان کشته شده است.
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/444656" target="_blank">📅 09:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444653">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad9dc303a2.mp4?token=IUJW2q2aTEOz7-1yPGK-knjN4YETa20erGr99xGx9E30hjs8oVlDvwaHf6dTAlS6faJNdALxd5Zh25C_VBbzenYoAbTjxhyT2NQKqBM9eiX8LdX4LqkDRpDSYsFWOU5OX6YihtkEy6FQS_D6QYZ6aPQGnXeftnRLDbmiJyKA2eIVqs5w42ZH-PRwgQoXXLzFrVgFwAEOETro8haKh25_VyyKtiZZ9uGujZB0cVTM-0hLOrux6zjYzEKyduRfD8k52QyU0yNSzVKv4n_pt09_aq5nCTn95eGr73HlDNHGWWMoj61C47AdCxRk9v0kVqa7vDFLuOvodGJYx2Ymtss4J3o3e01NFOjycBQ0Tb5qQejjUa8egDAcPEOv6kIr1GicWFWW5QT_Stt4J-bfoLxH2Wabu9YKMu4Lhj6fds8hJwnPzVoPjZ5TcaenIuimRjgCzZrzBv8CzfMSQSwHRT3C0HRjebVRwp8uP72v-FHHUmk67AQaGq0aw5EK1cC-VCPwS3n3kUurT48xF-O4pkcTGV1J3tW2bn0ZKE9YYd0Nj0cytZMv3G3DshVDOM_R3Fbu8aPW98iIUn4pXOpmovONzB3jYNgv4ootbrP1dKEPsnkM3MFrxvuh6UJ1D09-S7zfOI8Pn1gPJsjNm9on6rFQy_lQwOBjh9ltV1vlzneD_gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad9dc303a2.mp4?token=IUJW2q2aTEOz7-1yPGK-knjN4YETa20erGr99xGx9E30hjs8oVlDvwaHf6dTAlS6faJNdALxd5Zh25C_VBbzenYoAbTjxhyT2NQKqBM9eiX8LdX4LqkDRpDSYsFWOU5OX6YihtkEy6FQS_D6QYZ6aPQGnXeftnRLDbmiJyKA2eIVqs5w42ZH-PRwgQoXXLzFrVgFwAEOETro8haKh25_VyyKtiZZ9uGujZB0cVTM-0hLOrux6zjYzEKyduRfD8k52QyU0yNSzVKv4n_pt09_aq5nCTn95eGr73HlDNHGWWMoj61C47AdCxRk9v0kVqa7vDFLuOvodGJYx2Ymtss4J3o3e01NFOjycBQ0Tb5qQejjUa8egDAcPEOv6kIr1GicWFWW5QT_Stt4J-bfoLxH2Wabu9YKMu4Lhj6fds8hJwnPzVoPjZ5TcaenIuimRjgCzZrzBv8CzfMSQSwHRT3C0HRjebVRwp8uP72v-FHHUmk67AQaGq0aw5EK1cC-VCPwS3n3kUurT48xF-O4pkcTGV1J3tW2bn0ZKE9YYd0Nj0cytZMv3G3DshVDOM_R3Fbu8aPW98iIUn4pXOpmovONzB3jYNgv4ootbrP1dKEPsnkM3MFrxvuh6UJ1D09-S7zfOI8Pn1gPJsjNm9on6rFQy_lQwOBjh9ltV1vlzneD_gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هشدار سونامی در ونزوئلا، بعد از زمین‌لرزۀ ۷ ریشتری
🔹
سازمان زمین‌شناسی آمریکا بامداد پنجشنبه در پی وقوع زلزلۀ ۷.۱ ریشتری در شمال ونزوئلا، هشدار سونامی صادر کرد.
🔹
تصاویر منتشرشده از کاراکاس، برخاستن دود و گردوغبار از مناطق مختلفی را در پی این زمین‌لرزۀ شدید…</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/444653" target="_blank">📅 09:04 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444651">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa81eb74a8.mp4?token=g5Bn124CviV5e1uO7Cv1XGigH5m_BvflxkLGuylp13MdIfHTI5d5Hpzt87-yboK30QfPgMv_wtphCPdPk5aYsaNBKvhdBVrO-prlZkSB2rAr3ciG6jmjzcRQ1WFo0U3VcSLBYUE5ZWE_pKFIaT6k9rOFKCj0LdAJON8ApifNnqv_MXI4axfN9HGnp9ctExbfbo-rMN-yeIYVPyG23Uh8LA5h9dlfIfpFLjVtNX4T5bOwBsBLR8oW2uz2SQR2z_fB-9mmuqBk7miI_-Mb27YT5ste6AHvUEg1Qk2oreF2lHbvKhyz4_Pw9S_Lnx7rFlOJ-Bou5LFLNFUJzDPJGrF1rzCStCzN1i_KrsGDCglW9XC02rVnOOaErkfHXWIEerR8tZ4xh2YWetm8yruAlMjMnM_gsEhukBczoGvM1vOBIRplJctaZp3xea78VGeZh9YFvM1h5UOVYmp2aQKrMPH9cYf4XoAovOklfcC0d3nUI41ERjeNKk7Dz3u6r6mSkgHv1ZHnBiQH0uqwYzxQYSe1qa_qrKlaLxkQ7bEmdVeDcgeQ51zQg8F-ROHnvuxoWE9sy9oE9RCBTiSCsxb3VVwZJk2NBW3mY-mj4NZxmU2lhck-yktk7wFPxLrlBQUC0hLoT0xORbvCZvedPo3sRL3iXl73p3Cu4WV_4LMCsZbGIhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa81eb74a8.mp4?token=g5Bn124CviV5e1uO7Cv1XGigH5m_BvflxkLGuylp13MdIfHTI5d5Hpzt87-yboK30QfPgMv_wtphCPdPk5aYsaNBKvhdBVrO-prlZkSB2rAr3ciG6jmjzcRQ1WFo0U3VcSLBYUE5ZWE_pKFIaT6k9rOFKCj0LdAJON8ApifNnqv_MXI4axfN9HGnp9ctExbfbo-rMN-yeIYVPyG23Uh8LA5h9dlfIfpFLjVtNX4T5bOwBsBLR8oW2uz2SQR2z_fB-9mmuqBk7miI_-Mb27YT5ste6AHvUEg1Qk2oreF2lHbvKhyz4_Pw9S_Lnx7rFlOJ-Bou5LFLNFUJzDPJGrF1rzCStCzN1i_KrsGDCglW9XC02rVnOOaErkfHXWIEerR8tZ4xh2YWetm8yruAlMjMnM_gsEhukBczoGvM1vOBIRplJctaZp3xea78VGeZh9YFvM1h5UOVYmp2aQKrMPH9cYf4XoAovOklfcC0d3nUI41ERjeNKk7Dz3u6r6mSkgHv1ZHnBiQH0uqwYzxQYSe1qa_qrKlaLxkQ7bEmdVeDcgeQ51zQg8F-ROHnvuxoWE9sy9oE9RCBTiSCsxb3VVwZJk2NBW3mY-mj4NZxmU2lhck-yktk7wFPxLrlBQUC0hLoT0xORbvCZvedPo3sRL3iXl73p3Cu4WV_4LMCsZbGIhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آتش‌سوزی مهیب در پنسیلوانیای آمریکا
🔹
آتش‌سوزی گسترده در یک کارخانۀ قدیمی، شهر آلنتاون ایالت پنسیلوانیای آمریکا را به‌طور کامل در بر گرفت و مقامات محلی از ساکنان اطراف محل حادثه خواستند فوراً منطقه را تخلیه کنند.
🔹
همچنین به شهروندان توصیه شده از انجام سفرهای غیرضروری به محدودۀ حادثه خودداری کنند. در برخی مناطق اطراف هم بهپدلیل دود غلیظ ناشی از آتش‌سوزی، دستور «پناه‌گرفتن در محل» (Shelter in Place) صادر شد.
🔹
این حادثه همچنین باعث اختلال در شبکه برق منطقه شد. براساس نقشۀ قطع برق، شمار مشترکان بدون برق در آلنتاون تا ساعت ۱۰:۱۵ شب به وقت محلی به ۳۵۰۰ رسید.
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/444651" target="_blank">📅 08:46 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444641">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WKeDpBSrtY35hRJmoW9Im_ODuTfiU_9ajLTzkfvmtW-ktPT0Kf73cZOmekK8-NAPoFHlEdJeP2QASMKFD8jhBsXd_AhpbrqZGMS6WAgx1l8cjHcTfYUzFl1eG87MaV74oXGNtsjX8m9rfk4d8D0W6OgGnJC3R7Ku5SqdRLhP_QPCnVteGUG0VetTzPlYHWrd2VDU5HoeBk4eSLyW_JLIvHNbukcdX-OEkd8m1aNPB_zsN7I18vk5hx9fR2WSNqAxYa94X0zMgbkVWbDQLzspel83NsCaUl96KEQdr2gczC3hOnqfCCpq6mn8_CxNCB8esjiYUyJQfZzd0a7g3mh9sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jysM64Q6cWcWFM0pCNh9E5f8PrbrC_AYflgWcKBGqMe2fKIXkwqMx3kO_XII_5jbB9kIVdq9onGZTybLBcRxbWNrfSCWwNkh9ivkrQ7NudWMqq3FXQ4inUae_4NIzmyMBTAdpK5JPTfvQk8blD0uOFfagMbMevYSBzSOgm0K0AmvRjlQiDFQsUFpHnjRs20U7J80nufFC0DORLnYaJrY1bUbIBRK9K4inntwM8Qc--O-a2h-YYyhNhyaLEv4syr7gK4y69i76ZT6GDNHAjlaAPH8IaHX1kjMd0_KC5TXISbzeaI40d1LWkUw9luaZgi9cmkOfIbhuVbHskLudab-Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M_yIgBs51g2545dah-cPCwBtSeNge4lH0Ac9f3OHLcJuODRBQjhpBkhfahFrGCvYxKOcPlTFN_U5uL23prZTYAPUjscOUG-qQa-ePLkmVNvoeGvYi83ByfS6RvBYMfluV8Bw9prKac2BZkOQ3zdebe_HAgyeXop8mhDJUTjkTCdQgCuDYtRczfW8Alq1Kww6xN5tOTEkY-qzV2DB00LOGxschYiOAPXu4p9eZdM7YG331h7aem8rnBZAyD2p3Uxz-hdaxySFb_j_BzJ8DQA7a9lB0pB1DkFNTOT6LYdyrIUMcU5HevU4qMIXzIxAWpMFQOQhXfKgXL3iOCsJN4pN6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jzFWZe58_HYZ6qKS9Q5OfGsDFldTWUvNj8W-rzqhwyWA3tUQV3223fOT-fYuU_WEgiQyMFw-ipatk0c4gyPLiwcTcBmA3J6gFoHNTSAxDIxp8DMYiXCsFxcjGBgAQNt-6ysmqBPvMkZEoz4AcsIkrL76JAQ8qCZwOnRJUyChv2tN8pZ0cXnvKWJ1td_SwlFVbOARnQFXGkgzADtK-OKuboz-8WmZNc0W4FZbDYsf8he7qziPVBMMF9liFpPTDCX_Plk4yP04zKrgzrEfB2IUqgi9Qs-qGiPfW-0Sb5PiQBZ_M1VbQVTrgFW_k-tgjUSqIcsVw89bPQj4eH2UlXIRdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vBFJMf1KG6_oETjWx1-MZji7MfwYlknw1LOb0VoK8DdMB-hDhZwDqhr8UEN9Tk3svxyiw488enSCznELZ0f7i_L21glZqUs26J1lwcOfpsCgKyUb9CUQAzRbZ2gg-GdpkJqy6N0UzV8IRfCTzh3fMauf7kxJWe6cVBvMpvqa3ROJabHZt14ju7HG2Gsb3In6nKJ_dfknc1bFnxwB0QfpBSpCG2OjMC7KKxespqM9MkcJhLF0Voc6rCEr4RjrtrP1PD0Wzfzi8aWljC7r_xAcSaZYIQJgE4Gb2xYVkrhI2dciZmiDLpoPxBRxhX8bMNAw-5G8LYnHWewujLO6wMP61Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MJlg-nHx7iPDbNHHey7IHEnk2HEvMxsoMomZtkGFE_nZZCZ-IeQiMtBQJIqxFpApJBckGuSWOo_gyB4Xd3nyO9mxt6Iuz1ST_TZIlasxR5wwWo0gTNJQu73Ek1_yCR2o4OBhXlkzq6Rc7nUmxLCQNAdh8RFwL8FFhqsRUesf4N-TKasgJYDKM1ShxtfMsbEi5SCrkczkJiYl55oxZCgozlZB7iTH76O16Ro4mQR2tSXZDztAcdy9bdKbIo_IZ_f_AETnu-0-2Qv7mzVMkh2a6w85MaJyZgYr0TfQJww1dUJAOL5iBu6HVvndUSp7zAa2irjIrPoynsRj0-LrTuxtwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b1vzmhOpEqILweZEABxZs9UAAP7bv4nVL0z7f-EikeTjv8Wvps0IKaksHWY2nwpUq7TMFdHAGBhjPTRPbykYu_UKl2b_4CbyzHzE-eZ1ZG4hZFLHLz53yjomsHtg7P-IkKkPErFHbrX9h-C-UdvE7bnwZqCDhrHWyrwT4It8YwYr44MneJ6vAxgFu2X9MeYiwt1c80sFOQec89CK64wRUUZ6TFY95Iedzk6HO9Pmdlwthe_6FM484KuXuMzLPO6TeZWPx1zlJSSfYwfQx-hxFRMdbsPNeuO-BqQujl8k73QVBPWKW2GQVTqUVoS7q00gqrTnw1UfG-c2PK9ID0sXSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OpP56mnTYgRTbmq9TTfFcybwjac4pjf79wz0oJ8_ECWSsgnXbz7RLEyVJqsP2DYpJ-NPJaj8DQmu4imsNOgawLm041fZiLNyDrHb7zVAcPNuBjeKglxa-Js6RFGmaO5BYMng_E3TdEZuFk44z7u7Kj3nllO0yWe-K1pEquE8RCwANLecoEx_y99x_0iNUX5LwfSvTxfPWHiWtdRcJkNCuRcGK299B6N1OFkokIWLT9CsoESLqoikV64V80QF9qxyvU_QeI9y1kvCk4XBdfOLarlHJm0cy6bYe8Byf8_nl7OGP6TF6Y29F5IHavdDFlCuh32zoJSJQwzMVBtA2vVIdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pwzzvuDyVJkBMSGnE6VIWjFJ0jn2WiJJkqU_QPichqxLq2eUyXusnbDEV6yqkwb_7wJeg__RXUIu2Tp6bXzaR1O_WmdmsGAZ8uJTDBrtk8cD_7E06pU2SKzD84ymaOAiEdIO7jr89Nr-YYAMlS8CMrT89pHPAsZWMR11NHMdKH5eM9Ew0_pwxIdyEKuHvUo2oEsFz-wzbpsN03yJ2AKvazFKdTNg1BepYxFw3Z5eLNpgmJqVMEBOCwJQ-9_oe1TTdiQxVOjTITYadccDdHGk3p3HjUEHiOVWk1yTk2o8HZHKTcfRT3-aB5aaXEPCg5iYJRnNizca-k8RfAmJmP0Hvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q7pEUextoY0IJz-0hIH6iY7EX2CP7A95NANUfow7bMSxcAx_SfwphDR9FaMLkVDBUyNhEcMoskWxa2uW48D1GVKxsvfhzqSDIAoSzdxLECvAVV75MPX2KOJuS8JJB44CphFlm6K5EHEVo-tJr2ei4QphQ3slBZGjtOwzgjP28bN58FFgvUTxzYWY_WofbTvKwEXMUfhCmi4hDvX2Q_7nCIASr0JgU_dXCo-3ju69myb3NtYbQwRxKC0ngsJYO63LgwlZ3oCdvy_dCCfZukHKHOqe8S3yZALlPg5fOyEq5WSk4i2ETYvBvl08_ApzEFKu6cefDs42Z8tW_Vq95G1qxA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
چشم بر دنیا، دل در مسیر ولایت
◾️
محرم، صحنۀ تجلی مردمی است که با تأسی از مکتب عاشورا، لبیک‌گوی ولی‌فقیه زمان خود هستند و گام‌هایشان را در مسیر ولایت تنظیم می‌کنند.
عکاس:
نسترن کرمانی
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/444641" target="_blank">📅 08:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444640">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WF23wf9rIW8HO2ISd6CYgkBPl4TmChQnm-zeUMYPeL5vKEKQQcHtHe9gUyqJLOB8JprjM4b-KFcDQKWXIv_uM4Lc-kjVQgzD21oKWiOXL5sci_5o8sH2iTJ3UJYzOgoxZUsdtGKD2evoQJ9BJkg4YcQu4-LjQ0UYZ7oWTEiKEFZVVBz7ZE1jQRnL1GmwxIfGmltAyEJ5UrFgMMJsjR11Jk3Ph9KoijiuBLelKHoRMi6ur2R9hae-rMAHZ-Wh8bVwUIEMPN4pd4DSy9Rlyon2AbBCr3eWv-dldvbl0zRff2ibcbxRIw7Ir1tmXRIXjCEq_lHc98wdy-XBnW59vkugDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر نوزاد ماهیانه چند قوطی شیرخشک سهمیه دارد؟
🔹
طبق اعلام سازمان غذا و دارو، جدیدترین سهمیه‌بندی توزیع شیرخشک به کودکان به این‌صورت است:
🔸
کودکان صفر تا ۶ ماه
⤴️
۱۰ قوطی یارانه‌ای و ۴ قوطی غیریارانه‌ای
🔸
کودکان ۶ ماه تا یک‌سال
⤴️
۸ قوطی یارانه‌ای و ۴ قوطی غیریارانه‌ای
🔸
کودکان یک‌سال تا  دوسال
⤴️
۴ قوطی یارانه‌ای و ۴ قوطی غیریارانه‌ای
🔹
همچنین به‌منظور مدیریت توزیع، در هر مراجعه حداکثر ۲ قوطی شیرخشک به متقاضیان تحویل داده می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/444640" target="_blank">📅 07:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444639">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CC08bZC8Y-qnY9gBJWDATe_gFuJsaMOZsKTPeZt99O6w6UGbjiFBcDkFGXZ-sGOWo6zsO83YnxVnnGVnGRNjk8FIF5QwF7IbgZEQpD0LaZaJZuIbyF1EKOJ1ev7vTS-czKD6kDA1qb9B3n95VSg8KkbeF8YWn8mzIZttK9uNJ0Kyx8xv5ZZ0DIy96eePE2hnMN13glf8t3HK5SfKGE_JehOV0ikr94zuS7BTPctsDOvxxdEltFiNJ3Kuiv0B0X8diyXONcKxcYIgniO86QsbNSzmK_g-7jL70w9Orsz0kr_v4oEq9-1HHNb-2ut1Ow7AIIIAl49-ZoWAAOEQxbID1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاسوعا فرا رسید
🔹
روز نهم محرم، کربلا وارد حساس‌ترین مرحله خود شد. روزی که در تاریخ با نام «تاسوعا» شناخته می‌شود؛ روزی که دیگر تقریباً هیچ امیدی به پایان مسالمت‌آمیز ماجرا باقی نمانده بود.
🔹
در این روز، فشار از سوی حکومت یزید به اوج رسید. عبیدالله بن زیاد…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/444639" target="_blank">📅 07:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444636">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZsyZ4c8x5uVBs6XdcLy0Ls85vnYyp1iAX651AamcNFgenf7wbiZAseIcN9-bOIfG8CaHQ0--9oY0e6qyWK8FJorSvhn5kv3Xj93fh4p8-TeHJWC17Ups5fWu4g-9Vz8WS8kiKjxS7N4HnXDdCIgwJsguICIRBdoGyV1NW0_Z-xVjhoMxd_CztSo3sk34XCCqPUk8_9TvjqNjU7aVYSVh6Vd9zwwm8dYtBMGRt3_sKxqCiM7PeQKhANXcRL8mJAD8lijAnvQTiYQmA_j6-iomhW6lk-p6zu5Pk4bbFPp0BZXUdJa7Fq315-_q4wSuAzG51LUyoTIbL5luC06poQA6ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RszkKjPLA8LA7r3bK1OLy0_7QPHJHjj1SrNN5otjhTf3t9_CKi6oeO9uuz_ScWNfA8XDQzHlMF-fXnONntKCsdJ88JKDcz5rj6sIUnnmyUUboUuXWyvJJs2jJnQjbovs8LZPmN45UCT7175lpxe5aBFE4OzGp2A_4kRnEGfKw_xn37lQ0MWHayK01zrWHNWHvRooO-g07I9QAcXSZkmnlBkT79xBgwpaHf7TxTsJbSz2wR-y6npaDnGoIAa5jGjGF9JZjBhZbvED8Z7GluM1TQ1f81af1FxE-iptmuamNgD5yZQLbL4dCyLYxgrhCrkG5tBRKhwbOWZ3ZH1BTj302g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HwqQzMGnhTZ85GsIpWnwwWmm_oN0STRQrsSOV8Z7DLOZzD7hwYU7AfWq136PaBtTt7WdDlnyzvilCDPqhrdOegYD0jnRMY_evh-yGewaCUBzZlCRDunzg_qpv1Bf2eSOtxiCpHsi4Vjoekdu_Xcc8OGV_R_T662iIq2kOtePcvnJR8U17BNhXMfJ6vomGUW0tQ3unuxqvZKa4A9_VECdfs5bkcw83uvma8-lJ8gXdnpyih7G26hYGME975BxuCqede4pwrffxHo6QUQ9KELvmMBzHNOJfDjbakJ3zKb-hH1dDvC3bgp36S36v8-ZRslTO4sheXRyW74ICMqHy8l5IA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖼
اعمال روز عاشورا
@Farsna</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/farsna/444636" target="_blank">📅 06:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444635">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CnGnyX-jjmLJ3D66SnRqKY_dmABkce6LtST2pmI5w2ppj8AnriSSL0PLRySVTfLc3DAvS6fBbLzxFIHzGUEgz1aIW0Itn0j-O0agEgrqoLI_OuV-Fjvg7Cgk9wv6-6glv3ph9f2sFotHrRocmA4kmCPz-NMe4zXaukEDsFbNpSCc6P8PKq7KeD1b4VMS912_XjiLkmAppC98QEdO8lfgulfoTfDmhbOaD__gk177g9YYBgn14WKIXoTkydMuqecr-ksqwuyTVFlX-wzIeBaBhR0TQiZzXVmZysYzfKWIfJf1_A-H-bS3iHX8ZKi9IWIM50AzRqy62sKGljHCzGfmsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکست کره در شب صعود مستقیم آفریقای جنوبی
@Sportfars</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/farsna/444635" target="_blank">📅 06:36 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444634">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gMewC7XokhiFojije3nS5q-6-ml2BWBWIpf-Vijj-_MYKiRC3Fd4VXAu9j25ZL2igEYQ_o4CCzM0OXuI7tm8gPJ2wLnmE11okN9zopw4IZ1RIoIHqqLNLIndAnbcJxTCz7b7WxYUcfpulg7gbycWHZLxlW5J6wjMEuh9XXvNnhKATWI5gWaEssxIe24UO32ZNuETeFk7fRr-oMjZaJNqnnp9KgleIp48dAcvwB2JrQ3pVqefnZA_q2TWPZhPeCS027-zSxCVOukaLVf-JHBIxaIvsn4GqAOnXE6bjY1exORG385v84kZRZzXP1zVReWluOHFQBPdeVaGACI8SVbQTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازگشت «آقای قاضی» با فصل سوم
🔹
فصل سوم مجموعۀ نمایشی «آقای قاضی» با رویکردی آموزشی و حقوقی و در راستای افزایش آگاهی‌های قضائی مخاطبان، به‌زودی از شبکۀ دوم سیما روی آنتن می‌رود.
🔹
مجموعۀ نمایشی آقای قاضی یکی از سریال‌های پرمخاطب رسانۀ ملی طی سال‌های اخیر بوده که در قالب یک درام دادگاهی به موضوعات حقوقی و قضایی مورد یاز و موردتوجه مردم می‌پردازد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/farsna/444634" target="_blank">📅 06:05 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444632">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a32654de0a.mp4?token=cmUG8RtuEKdt86uUOb-TlulTg8wDZU1HnGz5Y0s6ZiwcGQRpD-x6EA_YDDu6hJU53Fo34S8ei-zj6Jh71IkIBaIzK13PuN9-T_dpMZcqQ63csGhFkdorzBd0s9MxeZ2VcVEqhG_UMGID4fl_b4k3J-YxYr0Joyj8Iv3xzyFVt8KoJM_9IBQPydoIrVxWTSrXUqZBMPw92CvkB48wUheyeiQi13iO0FWMKW-iIvyutP2wENrHmE-bqDNR-Mg8hQc2JFPblM1DDj3hgbWdJOS0vQcUOoCP2J0ha7YvrXdH8M1yYeDHI2RBY4ol2AdjgUdaqeAy60ptXEoOZA0o6679Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a32654de0a.mp4?token=cmUG8RtuEKdt86uUOb-TlulTg8wDZU1HnGz5Y0s6ZiwcGQRpD-x6EA_YDDu6hJU53Fo34S8ei-zj6Jh71IkIBaIzK13PuN9-T_dpMZcqQ63csGhFkdorzBd0s9MxeZ2VcVEqhG_UMGID4fl_b4k3J-YxYr0Joyj8Iv3xzyFVt8KoJM_9IBQPydoIrVxWTSrXUqZBMPw92CvkB48wUheyeiQi13iO0FWMKW-iIvyutP2wENrHmE-bqDNR-Mg8hQc2JFPblM1DDj3hgbWdJOS0vQcUOoCP2J0ha7YvrXdH8M1yYeDHI2RBY4ol2AdjgUdaqeAy60ptXEoOZA0o6679Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادعای وقیحانۀ وزیر خزانه‌داری آمریکا دربارۀ معافیت تحریمی ایران
🔹
اسکات بسنت: معافیت تحریم‌های نفتی ایران مانند دادن هویج (امتیاز) به آن‌ها است که هر لحظه می‌توان آن را پس گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/444632" target="_blank">📅 05:10 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444631">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔴
نیروی دریایی سپاه: عبور ایمن از تنگۀ هرمز تنها از مسیرهای اعلامی جمهوری اسلامی ایران ممکن است
بسم الله الرحمن الرحیم
🔹
ساعاتی قبل بدون اطلاع و هماهنگی با جمهوری اسلامی ایران از طرف برخی مراجع مسیر جدیدی برای تردد کشتی‌ها در تنگۀ هرمز اعلام شده که این مسیر غیرقابل قبول و کاملاً خطرناک است.
🔹
به اطلاع همه می‌رساند تنها مسیر مجاز برای عبور از تنگۀ هرمز همان مسیر های اعلام شده از طرف جمهوری اسلامی ایران می‌باشد، و تردد شناورها در خارج از این مسیرها بسیار خطرناک و ممنوع بوده و اخطار می‌دهیم از هرگونه تردد در خارج از مسیر های ابلاغی جدا خودداری نمایید.
🔹
هماهنگی با نیروی دریایی سپاه برای عبور از تنگۀ هرمز از طریق کانال ۱۶ الزامی است و با شناورهای متخلف برخورد خواهد شد.
نیروی دریایی سپاه پاسداران انقلاب اسلامی
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/444631" target="_blank">📅 04:44 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444625">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/efd-6oMtKzJdAfX-Y4_KgSaF-dGpit-mXRE0y0PE8TxYKjqJdq8tSwXfHvPKjs-XZ25EzKK65WhN6suEc714-Jb-gPNCT7klscixpECJ88p0x2lbAuk9gu716LDcVy02oDFVvpg6YoJLK8YCLHRg0kF-pLY_kLZ7B5_7RgtaRqSIVsfL235A9wuG-vAxtrhxJhmSPGOXF9JRC-ByxhKtkBSLmVno0j-c7mm03j2QNxadchQePO9ipqbEJpL40ABqurEZc9HcEx5W2ywZaDWttthL-z8SvKqjF_zNld5LCjl6b5ftma5i4KJxN2ZfNKle_vrd5QPSBoFfM6l2l1W7YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lG7j89r2alOhQm7CkkN0DHXNWpXsbrMnQ6ghde7eKTljd-fh_T04VBI6IkU0UqsW4iahicxM7mmxCKgb3axkMBuLVPprgVaEBFq7q2WVqs27TcluJg4fD6bkRmT5tMuwB4NL9V4QaruHCagWI71kPxYwlaAEn2vN1wyW3NFL-8JPQYj6ujD0Y6ZedGWYbox3hB_sbwgYV56oNZ0ovhVK1NQvqgWd3BQ0qYPgJZ40XzwJ5TMuWnj9ZLzZLrwz_7HIhTucO_h1zBlFA9CdvaAcJ6wXXqm-7SG-OXFRPg5Q8KXYhfHT-6IQQsAV0MOhF5rq9m5W77DbtP3jgnwmRDM1ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Djqv1Hp3vZrbHkE4l8V07B0dMDnQjDk81DcnUq8YRBo9HAqJrtIOh4jlmQuEAEzH67VM8rUC2_xkOEA6jYfCs2mOsxeK7KD_TQGRkWZVrx1neWBLMj2B16VN7oN3pk3jwVa3l572KfLU0ipJkhHzGLz0JDWKS4tUnwLZt6yqIfroTH4ERLXqkD6rjQtNTfTD0KsoR5StdOvfXVblsK_ygpUtOiJafdKPhiBkjd4s6rA8_Kjn3Q2o3YwpM4ZgwPR0TOXKL7znppJPH6iwm9KqlFSnx3RvAY4Op3-Rmxf5zrlzwSmZcacHvWQiVF2trQFNjmJYdLB-UQCSSqvYNwN4lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TDSZ8bHMtaLhXnK4Y8UckwYJv6gOl31il1nk5uHaE9WyrQG_JMWqRQ9wzorHEZAF3fYOEmjwv0LfrSPrSZXOyrHYNHbD8BnY-E0g0-Kkx8QQZ16ROQh6OIMmArr0tQKjwzD4aC4zb4WUOjjhtTXOF2a6ufur825ij8egOXE4oEf0dUwwneD5OjPNUTnhaAn-S9YNsLt1DpwCW3WjX_5jsZraqcI54IgUQ8dal_uXXZ94w9k2UNAeP0DNpXn5pxyQn7gZLE7l66VF3X46p3dgoKs7xJ397pJDaR9eAD9-h6RDxxWtxl-6aMc7Yj_kbcX-celFWPpCVasrYYAEMwIsgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UJ77MRWgSA1I1An8xg6O0nKDU0j3UxSMQNZX_u7poObtC6v_4vLp9v4dShTTRZZXMFrgtAaoLcu-MPyic4p75KO6NYXMt3wb5uqXn5xVVhSw3a02KSrKJ8P8gAAueEQHmpT4bS25DlZvYU3Fee_-KzOY17i5nt5kxMf8quaI1HrzZR0LOl7IWoNZv6lbBhopiWkLcptQu0PZChEk816e0CSP2XNtN9zNqgZctrmoNqvYLPHWCqHFREDLkEHhP69fg3c78Q3Bk-o3F8NTv0ZOWBvrvGf40kjm8vN70FOAFZ9X_Tyjd8q4FbZ4nCNgLScPOMqUZZObzn-meLwmm5yDhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jpIKFGaLqMgTWG4-qhVdl1WG29TRdOX26ywJLGQEmZLXPgAZS43LM3DqWu-78FHpCcetIr37tJT9V65KCkBOj4481ynmUC7cT5Q59ZhGjI0e9ho25-ued6Tp7i1CbkDR__PkgLThdZ5XJMQNuPxGk5lyN3oKYaS1OtbxqtZTsTck8ueZSpUSJMKsLkFlCwY_36f3fnO_smLe7-ujKIv5siVUh53EXMycJQInQJbbFz51M37rjRK6qOcirDAv7blsfQswyAvYl4X7ibGnW28TtutT8qZh67spCweecoRLlUdT-ADyqMQWla3V07wd7RdJVzpwvHtnvrW7fET8wKdWcA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
قابی از خطبه‌خوانی شب عاشورا در حرم امام رضا(ع)  @Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/444625" target="_blank">📅 04:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444624">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">آمادگی ۱۰۰۰ مدرسه برای اسکان زائران تشییع رهبر شهید
🔹
مدیرکل پشتیبانی آموزش‌وپرورش: ۱۰۰۰ مدرسه و ۳۰ مرکز اسکان آموزش‌وپرورش در تهران برای پذیرایی از زائران تشییع پیکر رهبر شهید آماده و تمام امکانات در اختیار ستاد متولی برگزار کنندۀ مراسم قرار گرفته است.
🔹
در مشهد و قم نیز تمام امکانات در اختیار ستادهای ویژۀ برگزاری مراسم قرار گرفته تا پذیرای زائران باشند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/444624" target="_blank">📅 03:50 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444623">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k--EiXCrjXnv3nsh3bf862R_cnT-1NKfS3_QGLiqo-40JQiHbqULF153VUtHsSmHM62-AZahF_AIIFk97I9qnZuDPF1PjHZwDPntAj_cIISpAc0wivYRbGtWea8OngvibwTa9Bpb28r8X6qivVDtWIuvQvq7KpQ2rs4ic-NUnzUWeNk3yBcKi0fT2LPcNi2Uj9UUKoJSjIDiPrFVpC-oWs0TVtef9xPioXmh9Xm7DTTc4CiffhIZFp52lcHdyxI4IOS-_LJnU7SaKwi7Hi1LOKLe7aeTjEnQQ80C1Hxz9IWZjBocPYXaaMC32xML82qSXeRVrbvLverE447PlSdo0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیمار آمد، وینیسیوس دلبری کرد
⚽️
برزیل ۳ - ۰ اسکاتلند
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/444623" target="_blank">📅 03:42 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444622">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O2hAKbHss8i3GJAD1AmXtxjuBdBKzP8Y8DjOgGNWR6D8-NgtSAdS7dIv5f27vUIyQDO0aktIL3Ye81bRu5SuzLqikgtWcFBAIJFbIQI5xZnAPocdiHc-OzfWFP-Nlq8UL1fjFiPnDvj8WacqdBzu9WjtaHiVuad_Ymi8MumvgRDWoTOWEApD_vGNSyQ8OS7amic4ZZ_cdyD6s3hVUIh-Lh3brwhYp-Ehf5Vx3pi7S_0lJrr1Y6Z7LKD5Hc5DCv0ZTF_BBp1tVYzkKvi3pE5VZtgx54HBhAxGH6L2gsOPjNijDBgjRhJqLeD3GjQQGzOvbqDG0qM5-m2gopOkZnW8Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدار پرگل مراکش با هائیتی؛ کامبک مراکش و صعود به‌عنوان تیم دوم
⚽️
مراکش ۴ - ۲ هائیتی
@Farsna</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/farsna/444622" target="_blank">📅 03:36 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444615">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VWcSd18_4TD_-bj7QhKiaUJfj9BgSXf48SPa7glXb9k6xFCplURppRvhhJekMda7doLXNXxxs90RvsUn8cU9pw0PkjgCA4Ab_VZwf1KPcvky5ZNibtZi05jOMP2RQss0fV4B3zuLBf-UCzmHqsBJKKk8D1uX6VxAbBIX_yTa4Kn2fXr7GejjagAooI_zCf3dPJFqZHWiczxgbJkEglizxeTOtaIf2T5ZPg9cDVgQmWOD_3o2gcHg9OH4_ME-e1mKPSsvD5tq98q-yidhFkymZeRKm7DMAdr7Fa215CRUrwQ3pNK1cnYa-iP6z91ZNjhxKGXY5cXbMHl6gl-HEBbltw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/puxgP3D3-NNWmEmnw_uVvRI3C6LHsAb69iPOnNTRHrXB57AuL3CEeNDZH5HP6YtGwbcagYgn3FJk2WyuzA4gXdCK5k2U8FhX53JMkfy3kmt4bjFdbhZY9nOHO8qGG8oOr_1BNmRtvBstTut01BN2sdUkaiJLtk5mDm9KCpTmMgKbmTNYaaN-CBy9bICvkt7dNoLHL1z1-KYtsdAxftTXFtTNs6gqMtN6E2lOcsgzdGctNtO6Rx7HsNG9txF4KdQv95lCCb4kH8IrV5CkQMDM8m8Y6HKRkF1aMVxPZhuQHGDVmVGduTxoo9UV3sSBpThy-RiIakzv4JIdU6-8BjS5ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i0kFCwe4hzo31YDLEkG2h34OFN9ddjs9T-5WqosHv7cuB1X_GXGbx5CoIX3DjhEUpfnOhAXxd06KRyvBsMBq94a6cIBrfGNT7FNQjjsOeU8E0xWGrq3dIYziMU2lYOxUsialGq-SnMED9vPIkgBLxIzqCf9BtU1MTnYqWnohMcV_5Q3wkIjVswj-TyizhjyU-HywXWwZRQ7SLSiyjbJQNwdc6yQ_x88OjTx4dlAcGvNZTGjwHZwtvdUYsP_H2beOXkJGb4jcwi-ygecYYwCEawYfj2QB1kaYte0DYm_m47by0RztK7mQKdIXlj8gu5y9mPOABVlq9xj7-vPuT3x_EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KajbwnJ7sBtduqlkxWABvmH1RAXkLpjjIVWWL9uAaEYzmXbbAsc-tz3Urb1J5ALooAId53mev24zD2sMYMiM6v6se2RSNd5HfUkwCq5Ag7v9U4wD1sT97_eZGItwsQlH260ToqOHRoj2Kz3ae7a9u2-MkYrOzFhjdEsz94uTMQTSzPp4vO2wLJFjuzDIuDQO7_nloxkrh5NDAmOBWCH5l4LUpqDbK_6aV_MTc5mCL6dCJyolRtjweT743eKBgDttrfYgXgUulQU976MO5GjzO3y_nwRK7SO2YMMzHX7aVgSocu1wuoM-MDQhQC5b2LD8ohgdVv5hX5iEG8AoLivXfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZZ0tULMS9OvUGMUgkFwytqiMW5Npjf62h4fIN2X53fcHoPKCfgicuxxGO85j6wnAHZpX0ezUksh1z_1HwdxRUNtWzMCGjF9fl6pJPmxikKpN-s2eFbw-tpoTuJmgJ7pIhR02fC7ok-6rA3j6k8JXMiokfwkxUdNTUjEiSc_4eGdIbWn8jkPZYXQYucwbp1DFLL4Nof-mTwjTVeabjqsyxXCLgKOQEoz4BSlIvq6iwLzsUYuz9-jfgCyc1pDcJOVy5nAGud-dAviflLVGKRv4UUM0iOucnvRGjouKfeoftahc_hfm7H5Ufc5D-6viKEMs7ptqR2qbmizTS1-Wuu6XIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BcCvJ6L0IxJ1MOKaJZU1PZ8fmRqYH-sGJspaW_JpNP1iAMY8Sjd3SKkA19TjsAjgbIloI1j2niN9pcOPU2oacjruHNmQmZn9xSOMWcZqCNigWUy7ZSgX89cdk1MjA5xZBGKo-Lzai4-I5PphRGHBw0avW8VaeDkUilyyi557-3yTlTrhMK6QM_4evZopR3gq5WLeyRWliUAJhF9FRXlaBk277qPYUzHsjs0p6epWSuiWqoXrojNf_FchzDHYrxmC4QJG93fVDfLqbeJnszB-22xResz9kcRmG6SvK00QpT7FMaUvgef7edIFwnp4YUwodvjKmsRJ-aVDfSYe1YkRCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NFiL7dBfaSjw1ZYKhJXDAquKmybBEKp2fdGw6IrdGKw3J609eQxfS2hYwLg4eljselvs_ovZ8wkGqAffZ0x9_vUcfDJf3lviDDpvDxmH8manvV_plT_U9HSiuPB_-N7l7YcmICar7YRKMysJB0oP0qdtzY580KPqCxQS8bLquTkBq4Nfjo4_KprdcRInkGnkePcm6xw3ap1IRIqvVdHc3Buq1yTENro6PZjihbDFxSAVQYo2vIkJYgZ1QmMHhRTVtTcxunplp-zOleeWWQusX2b9u92-WTmbSw32cDvycSlO5T0Jo8x2_ClSZYyzkfFBbN_uyMrP3zZyb3GPI9takQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
عزاداری عاشورای حسینی در میدان نبوت
عکاس:
میثم نهاوندی
@Farsna</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/farsna/444615" target="_blank">📅 03:16 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444608">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال عکس فارس | FARS IMAGES</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D-dKehWxkOArKEqYAQaVdOjUpR6A-B3oZQSpsCg7e6fTZXDgPuN-ZNf5h87dFh71bZeLt_HFpjwZtdrq60etpckkWOZrGawjqpoeakUAq9sWvIraDdfiqoGpgktGSwFb7UdwfdUM51BFIfPVJasV6aIzA6m5hIiVfO0N0t_M808qDDJ89kGNjXPUhXbaI1xfRl07mZ7SC7eyxAfXae7kWFqZpvbrQZKUatCzyAsW_tJc5bmEi2MLHWTmuH2pnnPD8UhlsrdmnpQtXlwLe11mrPfPRLi0YM-Wenq9oFSqO9luEs77GjpwOIkcjCKcd7hu9hIVKpSz10HuwEm15rV78g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dU4oj_gMi-eMkYjvLIDKTgcRfiEJkGzfZIRlKQfOW3ZusonipoZLyPiSZX2-NTiLi-SX9IjVBJVseh-Nnco3slQvJBsAKxtaRt3kOZRvPXc04G0-uiYPBT24ktfGpMLjrNWDNXpLr4ARSiu2cKOO9Ny3EbVx_tMwQrs4G4lUj50wP-pjFWtS2DYk0pg93WLYQxlQLhmE44uEL5oZ6rN07b17zx6XtVg1DAD29-XOWN1blyCWSWYFgUyYdoftxqWVNS8BRJf-hHyaLqlYMVylN8PJNs6uO4zD689DTZG7UwgK5Nea0NR0tt04UW8vg3FRgb2ErrfaiptfwpYDmQ4fAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I1C_pNtz0ZIagqwhXUIqNnD9cxUrSOo4-D10Gf2ErGYsQ0e8wPQEMu-frYyF_i8-l0AnPRYgFIlN1F-5ZLftbhShfXkixMtaVye_LFjSNNW25unJn6EInzduzpmuJ6YcxrNqxsSL7GfF3ducKchl_e_X2-eWXvXUj8C7k-zxdB8Cd2oROEjths_lCvDzqrqBrp6jVB04Cg1c8qJB4xd93jxFbpi6GGXPkCokuaH_IujdkXHRJMAXSvRUeB5WwKu2VdxMAjRoMXXPAQ1Uq5tHOEiDFZDYGmySoCBZCAbpnzGyk0jfnY1choAupqFwPLMUlGF1DaXQ8JRPqRwl75hFFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qdE57A9SsVNTL3cR0YbV7KUQXaWA26h_8qiO3GFb35xDz8J9DiEXphwacdYGol782z-C_HIGGUFjEhzFH2hwfU1M4SNro1Wpx9Ky4FLNU6F6Se4JQoqw_rVV2vQG4HpR-sLmpK2FKpwe_mU77NHgqfuLEGFYABzBNGOq4PAiKOWYEbK6t4FT2M-tOzE9GU_phmv2B-abce-ZVO-d50xKtylJy9w5iphILe430eTl2mA7iT2TUdUs5r4riXBB8rVxioURFgbMlNJtwWL4PBLPdoXUv-lKHSYI-IncRWTlNJ9F5KJfLui7AowEh2OuvDgldm9xzihQWp_1FzPgm2cBQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cDiSgAGxJK3bnRcB33aQLUyDC5dv9ht0crNYPjLobAwt3K1TV5uUhUUMhh2P1hk2MHB8fMW07Jp28UU6FgPaJYDUCOH148oi54AXiQ6lriFk8QjOJZLEG-R2Crf1dh5UDIqCMfJyIQoqwWjhHmgvPb1LfiLJinAANylEElU7azN41F_NiQh0Gj9ZcyJR_XMfZCM4Xf6qBvOuZukDjsfG7R3jXfwyJiTzjR-Zy9-MYrAWfxl_AkVslGDX8ooxyR6DaNtYdDkHXdAy6TsU4oliX8Eym3FqM1jPfHeI2nIWAnzsAuQwAYrM3p2jETKVCs3sdL-KE4BfaW2ZWRO5wg8JPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LFBZwqDNiU-n7ucaV-u1ptMgh9BfcJ0RwsRo9Fy_wcXmgARcX4qR5w7eeba9pE4UmJXZckZKpxslst9Z0f64oYuVpc0OLVusf-iRUh1aFGdfdp5PqcC5eCgjT_3h97WONygAEdEHNBGuCcbhMvqFjAXmButVHfhHVK4g5AwSyLtkJj_lLjUYHxZFPNdYLLC3Ymjw8e7RbAOnQ6rCpzS-ZQs5K6d9yGiRELvYyitE0raENvR199r8wvF_M31147nVA1MRYSq0IAtegLT-Vmdgu570cc6FQqoG2X9zvZmsiXFxGJLYZ3fbcdkP2LO5PEt1A8jrUwZLRjn287d68fSakA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UFWvYUIuB9egQV4V3HE4tocZqHGTRmiQ3sceRcQY7O1NrclhQ-v3VAeJ1KGvG6bqvRfbmnK6ZqWHP1cSXE2-8blnMmwRcEfv-Nq08-FVZzlU9jcYdl-gV3Xuws9gEABhBfZtUvVWigpHUSddxTNKiJEjV5oUPEruyzJJ5qnIBx7dSHtvPfXommgCSJ5JTzK8LjTbKx7vidJuwaR87ETnGMWT3Votrm_FCp-E5PhwhxnGoyBtMaMbmc_ZmB4Y6GQDsnvTmrmg1_EydI-3n2okQvM9t0EcDIXC1fyTWQJh8QxMFzZOvIJWK3Aj_GaDDKbcMLqhEptbGFaehgUXGpOuPw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مراسم شب عاشورا با حضور قالیباف و مخبر
عکس:
محمد‌حسن اصلانی
@Farsimages</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/farsna/444608" target="_blank">📅 03:08 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444607">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jq2ToIHGBPXv6x6E4Pvdiyrn24hzIybYq9FtYHmSf4Bb47zCqpJFSJAE9LDtijUOYc9VH91Jvh0eUlXmGWz6WLYINb-Q0HZrO81_-WcBnGMSSQd8vWqPnL6Em64bdOr9Y7o-UwoNgjqYUu8tVIsmsmnHUYWkVt4sf4Bk551nKAyYz1MEw_w2x8dJ5jtkU80X_Po_ajAXUdtftEScMI92AUD_gKu8TE1hvxO-JEjA0eeQBYCTVuTCWVULJsk6tZyOwlpdPkM689QgywtiEEFt0il41l8_gM5iMSFy1PbYuk96dDdnVIuculR0Vx2Iilvy7W1Tdo0msGb6ey0tfjtsyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
گزافه‌گویی دبیرکل ناتو علیه ایران جلوی ترامپ
🔹
مارک روته: کاری که ترامپ درمورد ایران انجام داد بسیار مهم است زیرا این کشور تروریسم و هرج‌ومرج را صادر می‌کرد و نزدیک به دستیابی به توانایی‌های هسته‌ای بود.
🔹
حدود ۵ هزار هواپیمای آمریکایی در طول هفته‌های جنگ،…</div>
<div class="tg-footer">👁️ 9.67K · <a href="https://t.me/farsna/444607" target="_blank">📅 02:56 · 04 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
