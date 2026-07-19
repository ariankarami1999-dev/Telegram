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
<img src="https://cdn4.telesco.pe/file/KEpbMtAUAUHx6xRkQ1PyrR0B7qORyftpajmtBDAZ0omrbrEbEJN231C-04sbKzH9SjwPqvuhtyI1Q3grPBOadhweWZKgpZUUY7GhiL_zr-yUF56K5oeNOHYCmhCBwVrElfmyyNswuvjJWfrIDW8v1myjFhKwORrLgc1x7jHg6lL6PWed0iq9p4AvmnKw4Lm-Oh6XK8T4qpoN9zYF0pWm89MiY9EPgRh48oY0JwinTSm7cVE2zUTEAlieYQSJ0ro4f742eqOOtd7O4xQxIi5zpGhiaUUZ_Skx8S5fdAMFpjVaJLIwOjjqT6wXbolZybvbRWiJXu9y4C4zSV-o7fw2gA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 268K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-28 18:26:48</div>
<hr>

<div class="tg-post" id="msg-84239">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24db6b1462.mp4?token=KKmBA49Noep4FjgqzBNxai-VocVbxdk1RJlfKt_-PNXIV0vsW2lRLM3F5-HHZjUwODH82i8NTZZamHszbZUu2Xjmi702V6ISUaVoOypKyEVGLItDzSBvRZfTR87UsGT1Ft-KUwQMWljV3jx6999E_RhHLzinfWNLhqrTG8pdOzKJtrfM0YQlC7cI4t481YkMHPnCTulyvOtqxH_U2ZrLAT4YzIN2fuHZHW5uH8As9sYOApMewmy3k1mjb9qofQQvk9NAoWxjgWyyt-q85Rt1MqQ6hgsj5eD5E7vWg0KrY3z_FVFhZodvCm-Q5-_MOT4cWDYSwM4RZbWoDp-j9oTqJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24db6b1462.mp4?token=KKmBA49Noep4FjgqzBNxai-VocVbxdk1RJlfKt_-PNXIV0vsW2lRLM3F5-HHZjUwODH82i8NTZZamHszbZUu2Xjmi702V6ISUaVoOypKyEVGLItDzSBvRZfTR87UsGT1Ft-KUwQMWljV3jx6999E_RhHLzinfWNLhqrTG8pdOzKJtrfM0YQlC7cI4t481YkMHPnCTulyvOtqxH_U2ZrLAT4YzIN2fuHZHW5uH8As9sYOApMewmy3k1mjb9qofQQvk9NAoWxjgWyyt-q85Rt1MqQ6hgsj5eD5E7vWg0KrY3z_FVFhZodvCm-Q5-_MOT4cWDYSwM4RZbWoDp-j9oTqJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتفاع أعمدة الدخان من مدينة ديزفول الإيرانية يرجح انه عدوان أمريكي انطلق من الكويت ..</div>
<div class="tg-footer">👁️ 7.56K · <a href="https://t.me/naya_foriraq/84239" target="_blank">📅 17:49 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84238">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PS3dsHTq6tmGuOuanEPkJrgHfLhXMrBUb63lJrLWcn82UbvD0Yh7M9R_XpgRO_BmJMdwc7mGNcq8mAUODwx4n8A07Kt9-KTX0rHxW_3aPvhsVLZigsg5217f1logPbu6KpTA8z0fhK53r5J8Pj3SnGOuJ7cfBQ631GohNgzEvV7hmIriPH4tm0T5z3fn-VKfoO4dkvKV90TTNoyEO65Oz19OcdnSPWzG6I9RKNiwfkWtDdKJIme2hpwsUfBxscOHgoW_YcOyYBknKRTJVWEwoVIX6BICv87VaJwk2Ic6lhKtH_f1hVlIE0lBeGoh4FnBBoE62YqKxBGH6cgi45_irw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/naya_foriraq/84238" target="_blank">📅 17:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84237">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/naya_foriraq/84237" target="_blank">📅 17:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84236">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44cc310eee.mp4?token=dC05oLOklenJcze2SPinWGNGN4q9TVoYiPmSaEA1BPxeaAeXmhrlRT7iIhQO973F5Z63boeo1ZCoG8C5wysCu0STWaZmLAWGdcHlQdFYcROKjCGBB0_ZIZvRem3zsGWyyJUxUetbFHw6HIACyTg3U0v1ikW5Aq1LTu4a2o3NmeCtdgxFyljksjkDLrcugxkL2u1eUz-BzIm5rCsWSsdMRCS7FGeK9e8-5SwtXGjmucJweLlXHN9urUSltGTjUIypMwtuiYbJV_7zEddyOPfmiCe_hmK8yNSO2xe6hBtiEHQ4BiEGoX0wgRDS82tWemzzP1XhbmkqEVkhX7R-RZeCyCHWE2zL0O6VHyj9O_SWkl4cK8nRSVE_TZydHDjZDrhTwOqaFEEbaB7VaaKOA8MMnNHF-B-DC45vTLG_lI1Ib7e95wrjQDUpBY9c8YwJ2Ic3MDh02E2k2d-n49WXkWmJT1VcNgzJieFBUCqVu2WoNkXUPpS50NxnLGj39YtyhRoVfbiVlftdQQCNfveix2k1BbNwIVC_4TmMqSRkzYZiS-OttUqtqUtKj8ZP4mG4gsYljJGNQjSZsV__ifu2klkMpOb71RImkJMcyQmHWA1Z1fcZ8ohJo3MnNE906_NuPVp1nZospaAht74Ec7_qLp8hfJzeet5qfCww4_0XUPuq5ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44cc310eee.mp4?token=dC05oLOklenJcze2SPinWGNGN4q9TVoYiPmSaEA1BPxeaAeXmhrlRT7iIhQO973F5Z63boeo1ZCoG8C5wysCu0STWaZmLAWGdcHlQdFYcROKjCGBB0_ZIZvRem3zsGWyyJUxUetbFHw6HIACyTg3U0v1ikW5Aq1LTu4a2o3NmeCtdgxFyljksjkDLrcugxkL2u1eUz-BzIm5rCsWSsdMRCS7FGeK9e8-5SwtXGjmucJweLlXHN9urUSltGTjUIypMwtuiYbJV_7zEddyOPfmiCe_hmK8yNSO2xe6hBtiEHQ4BiEGoX0wgRDS82tWemzzP1XhbmkqEVkhX7R-RZeCyCHWE2zL0O6VHyj9O_SWkl4cK8nRSVE_TZydHDjZDrhTwOqaFEEbaB7VaaKOA8MMnNHF-B-DC45vTLG_lI1Ib7e95wrjQDUpBY9c8YwJ2Ic3MDh02E2k2d-n49WXkWmJT1VcNgzJieFBUCqVu2WoNkXUPpS50NxnLGj39YtyhRoVfbiVlftdQQCNfveix2k1BbNwIVC_4TmMqSRkzYZiS-OttUqtqUtKj8ZP4mG4gsYljJGNQjSZsV__ifu2klkMpOb71RImkJMcyQmHWA1Z1fcZ8ohJo3MnNE906_NuPVp1nZospaAht74Ec7_qLp8hfJzeet5qfCww4_0XUPuq5ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظة سقوط الصواريخ الايرانية بشكل مباشر على اهدافها في العقبة</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/84236" target="_blank">📅 17:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84235">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c82dfd1851.mp4?token=rwe0mkRxkNe0QDek3mSe1FgXUwrJvMSZ98DUHT4MX3qCXLNRkhclICk6jUnuf6jF6fNNVYD1fgiBMovbcM4jo8qUDd_lKjpvMyj1wmXVxNb7AzN6X57qfrlGXV0q9cePfBNf_66BgQBF7QJNA56B9zoVs2Lh6fnuVi5ow0RIqo9YvZKFGKWwAtUAUiJMUTDfF9IZVOoI1uBsEB2VPhT42-icQk2MRKn6Pb4bA9BbN1TSs9824UdEDP17guPoPK_GIV4NBErwP4FzJGMmW-lxZSuD7WdkoBKIl9XBZX53Jc1DxAhqTzJ1WYgGiizEn6TahvPsvo-vMcJPJSTSH5FxMTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c82dfd1851.mp4?token=rwe0mkRxkNe0QDek3mSe1FgXUwrJvMSZ98DUHT4MX3qCXLNRkhclICk6jUnuf6jF6fNNVYD1fgiBMovbcM4jo8qUDd_lKjpvMyj1wmXVxNb7AzN6X57qfrlGXV0q9cePfBNf_66BgQBF7QJNA56B9zoVs2Lh6fnuVi5ow0RIqo9YvZKFGKWwAtUAUiJMUTDfF9IZVOoI1uBsEB2VPhT42-icQk2MRKn6Pb4bA9BbN1TSs9824UdEDP17guPoPK_GIV4NBErwP4FzJGMmW-lxZSuD7WdkoBKIl9XBZX53Jc1DxAhqTzJ1WYgGiizEn6TahvPsvo-vMcJPJSTSH5FxMTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
اندلاع حريق كبير في مجمع مشن لتجارة الاطارات والبطاريات بمنطقة الكرادة ضمن العاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/84235" target="_blank">📅 17:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84234">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🇮🇱
وزير الحرب الصهيوني:
لقد أبلغنا أنه إذا أطلقت إيران صواريخ على إسرائيل، فسوف نرد عليها بقوة، دون أي تردد أو شروط.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/84234" target="_blank">📅 17:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84233">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">انباء عن انفجارات في بندر عباس</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/84233" target="_blank">📅 16:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84232">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/84232" target="_blank">📅 16:49 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84231">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">من سماء الجمهورية الاسلامية الايرانية</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/84231" target="_blank">📅 16:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84230">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🇮🇷
مسؤول الشؤون السياسية في حرس الثورة الاسلامية:
وجهنا ضربات قوية للقواعد الأمريكية في الأردن والكويت ودول أخرى.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/84230" target="_blank">📅 16:39 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84229">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KTVkzExreWRnAAhxK7HPJL0WLrFBvlbcesbsn2fpt5cluLFsIrbPlCNuyajxvs2WBGNnW7hgeA6TOWVo-0q-ULegg-P7OwEMBh1TWHeToBcy_58r1s7zPA80yX7nz9Vs8Y-0vONgR-6fw_cJ3a6CPasJiVcCpZwVy1YPz4QwN3Xo0m0k94DPiyZ5AbvZ-6oGJmYN6Boyv_NEBchK9mabmKFjFbs6ux0LkiLFOn4k0BVTEkGuud8zLVsUZ2z851pqauaay2BDJkEgi6HWxeevZdJ8lAlN4HaaBdBfLLvB_p9UpaaRAPht5tc-wFXbUGJtUvrs1mVgEx3ZX4P9EWhniw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انباء عن اطلاق جديد من ايران</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/84229" target="_blank">📅 16:38 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84228">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XwVxJnUp4S3lFALl90NxeLnx1kT90VZWZ7E0CAaBb9odTcb2NTaegXwH5xJ1skUtwMKhXju6fOAvDDQviqC1YST3rz9CT2RY4wBkIYTcWNIc-5sOR0RlJneaecI4ujSCZae4YAvPBWwoIqx9l0rJTP35mzKmPfq9QGD1j0zGc5Y9fq8GezMg5j7KYWQv3nlE1AJjSyi8PK9ByEfcG7hS51_U5A5133BbJL3D15r9707Pi7795TJiXuZ_7n2yTSUbcm5yxm0XYLgdDh4E_qS0jCvunq6UtHMqHEwsrwPvdfsD-RVGUTm0BggpA93qpyDhF21UN-Fu_RIYUI5-vJu3Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رصد غواصة اسرائيلية قرب ايلات</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/84228" target="_blank">📅 16:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84227">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/84227" target="_blank">📅 16:34 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84226">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/84226" target="_blank">📅 16:34 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84225">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇮🇷
🇺🇸
منظمة الطاقة الذرية الإيرانية:  حكومة الولايات المتحدة الإرهابية والمجرمة، التي لا تملك طبيعة سوى التسلط وانتهاك القوانين، قامت، في عمل عدواني ومتوحش يتعارض مع القوانين الدولية بشن هجوم على موقع بناء محطة دارخوين النووية - أحد رموز عزيمة واكتفاء إيران…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/84225" target="_blank">📅 16:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84224">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">اعلام العدو: إخلاء طائرات الوقود الأمريكية من مطار رامون بعد استهداف العقبة بالأردن</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/84224" target="_blank">📅 16:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84223">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">اعلام العدو: قد تكون الصواريخ الإيرانية الأخيرة تجاه العقبة بمثابة رسالة وتحذير إيراني لإسرائيل.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/84223" target="_blank">📅 16:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84222">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">امريكا تتوقع الهجوم
الاردن تنفي
امريكا تحاول التصدي
الاردن تنفي وجود قواعد في الاردن
اسرائيل تحاول التصدي داخل الاردن
الاردن تنفي خرق اسرائيل لسيادتها
الملك عبدالله خلال كل هذه الاحداث:</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/84222" target="_blank">📅 16:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84221">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">اعلام العدو: سقوط شظايا في منطقة "شحورات" الصناعية بالقرب من مدينة إيلات</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/84221" target="_blank">📅 16:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84220">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">الشرطة الصهيونية تلوذ بالفرار خلال الهجوم الايراني على العقبة</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/84220" target="_blank">📅 16:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84219">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebd2cd208b.mp4?token=cJJBuHwWHXUalm4pV5LP6COG0BS0AEXWt3W8JNpQul98LVJmAXk5J9tevSlWWOJj-oiWV4xnKINe8vRyfvz4nEtiAU9pU7FjOwAGI5eH1o3qWjcZj48IARu7K3bnFYlIRmKTJTduGNN-c25eiVdfLKIcb69-VznMvX44JEQUfS86QfRAPrLcyVYA0rRtjurmqyvtS5hVTj3-FdYIc6kU1etKhzo0eUGyejfKLIhWNmmOw1yJZ0tUI03wFErOLASjdUP8l1hEFNHGyEXPV9gRNFFuNmNtZGjPApea6e8zXoJ524Qsy5idjMHDFViPPnj4FDgRIZl4l6k8rmxKt_gKHYhxFyA0gFJVIHMyXNf7cUeO1vcPXKI6LXBEbe6JUDZKDYLKPcjW05Ih11KXKK5VQWewGhm4MllrZ_S5MjxZHZgE-AHooU9N3fSKbM9Djp3onWEHVAg8Y9046-kfLn6tb3Q_sJZa1Jv8dnpICt7Zn1xOnMVhLMXKvC4TQkxLVYNdWTdiOfLJTzWVBqsogY5rQ0YVsA9qBZaQhYRwrafvkUIS0f0rHYLu4Y5liJ8cuuFWDScOKabtbMPksSqobtg_8Qjodj52l1xtpZSF_x1axaLh_XWAayMti0QlzV6r52aUDkga-CauiuEZPsVWX1_bNodsPCCYSJ9jkhpqWMW39iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebd2cd208b.mp4?token=cJJBuHwWHXUalm4pV5LP6COG0BS0AEXWt3W8JNpQul98LVJmAXk5J9tevSlWWOJj-oiWV4xnKINe8vRyfvz4nEtiAU9pU7FjOwAGI5eH1o3qWjcZj48IARu7K3bnFYlIRmKTJTduGNN-c25eiVdfLKIcb69-VznMvX44JEQUfS86QfRAPrLcyVYA0rRtjurmqyvtS5hVTj3-FdYIc6kU1etKhzo0eUGyejfKLIhWNmmOw1yJZ0tUI03wFErOLASjdUP8l1hEFNHGyEXPV9gRNFFuNmNtZGjPApea6e8zXoJ524Qsy5idjMHDFViPPnj4FDgRIZl4l6k8rmxKt_gKHYhxFyA0gFJVIHMyXNf7cUeO1vcPXKI6LXBEbe6JUDZKDYLKPcjW05Ih11KXKK5VQWewGhm4MllrZ_S5MjxZHZgE-AHooU9N3fSKbM9Djp3onWEHVAg8Y9046-kfLn6tb3Q_sJZa1Jv8dnpICt7Zn1xOnMVhLMXKvC4TQkxLVYNdWTdiOfLJTzWVBqsogY5rQ0YVsA9qBZaQhYRwrafvkUIS0f0rHYLu4Y5liJ8cuuFWDScOKabtbMPksSqobtg_8Qjodj52l1xtpZSF_x1axaLh_XWAayMti0QlzV6r52aUDkga-CauiuEZPsVWX1_bNodsPCCYSJ9jkhpqWMW39iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاعد اعمدة الدخان من مطار الملك حسين في العقبة</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/84219" target="_blank">📅 15:58 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84218">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/quC2Dr0r1mWmv2PhcA84tN3G6_3Q-ixWS_oONrXvqYpBsyn4pA78nb7FDfYbYs8yKYn3PE0EYB1nbhNgs31xLVS7P2Vlahqdh-63v56fNHDB2TCL46ZLbeVWnID0oRfoAEhV-NvNxLpVYRcWkJ-LL7aAGKOLcPm21uqZ9nm4xXb4sZuu_PDIW6DNSM7c9s0xcxjT3d9Mez_QUdsfAIRi0TwGz0stFBcozyxq_yHCg6sohGVVf7KeZd99lVo8WWVOO96yLEhTmVz7t3IOaae6QJ-4NQzx9vLTu-PIc1jYNICzMjlqIfxhwWXzGI-U-CxRNxsXJPByOB76ai2GSZj9mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجيش الإسرائيلي: قوات إسرائيلية وأردنية نفذت عمليات اعتراض لصواريخ إيرانية فوق العقبة</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/84218" target="_blank">📅 15:58 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84217">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/194f305a4a.mp4?token=ctGY2AtSzNs3CSwCY5IEdCOxxOy5Mvs2wtyF2Bh2t55yUxnM1ZqM242B425u9gdXZSc2ihe5_3vGOfnGHZcchZB10jzl_R76YQe9QczTh20OUr-tQOYFDBzl-X8VvpN3eGmf7sfL4ixfY6X_X80yUiZodb3QfbC-0Z2NLcuOXaPqi94-Ba0dcxw5P_xjUwSsjdhH7loPKlHxcpDvixJt0RY2BFzY6nJ0REBInmijH_6rAvazEp35DrtepfkuqAOk0NPQZQq8a1-YaVsTgoyGNv_TeLtsz1ov16iYPYEvbWSrNjwIw8sK3YKJ9QRK3PsaU-Mi_e4b4QhpANq20v7-HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/194f305a4a.mp4?token=ctGY2AtSzNs3CSwCY5IEdCOxxOy5Mvs2wtyF2Bh2t55yUxnM1ZqM242B425u9gdXZSc2ihe5_3vGOfnGHZcchZB10jzl_R76YQe9QczTh20OUr-tQOYFDBzl-X8VvpN3eGmf7sfL4ixfY6X_X80yUiZodb3QfbC-0Z2NLcuOXaPqi94-Ba0dcxw5P_xjUwSsjdhH7loPKlHxcpDvixJt0RY2BFzY6nJ0REBInmijH_6rAvazEp35DrtepfkuqAOk0NPQZQq8a1-YaVsTgoyGNv_TeLtsz1ov16iYPYEvbWSrNjwIw8sK3YKJ9QRK3PsaU-Mi_e4b4QhpANq20v7-HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سقوط صاروخ في مطار العقبة</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/84217" target="_blank">📅 15:56 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84216">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">سقوط صاروخ في مطار العقبة</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/84216" target="_blank">📅 15:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84215">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">متداول ارتفاع أعمدة الدخان في ايلات جنوب فلسطين المحتلة</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/84215" target="_blank">📅 15:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84214">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1702163fed.mp4?token=J0I8Xb4VeqsT-tRL0SBtskYA5tjertth8XduiLupgXJtzIrDUj9MyvhydYmia94Epxhh2UOq0duglnsXmn3P4Osm6kSoAk3ldGae8O4wL9AfRhjj8CNyMjY5ugYd_RzMiWCoMTuPGVJW0V824COyszHnfwOSKlXTwliZEJlVZbSmAzxuRir3vI90aX6KIQli8PICc5vBY9MUltvv_u2hTXeEYIORmiRzsOBt8K7FzrcNAjmuBVLfNdL2A2xsrQBruJsdPaSroso0Ljrq2MPwYJB56FzteKrXDiNUTfBqJnLnXrooCJUwGiquKuv7dmRto5QRgBZii2J3lbNM3K1YDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1702163fed.mp4?token=J0I8Xb4VeqsT-tRL0SBtskYA5tjertth8XduiLupgXJtzIrDUj9MyvhydYmia94Epxhh2UOq0duglnsXmn3P4Osm6kSoAk3ldGae8O4wL9AfRhjj8CNyMjY5ugYd_RzMiWCoMTuPGVJW0V824COyszHnfwOSKlXTwliZEJlVZbSmAzxuRir3vI90aX6KIQli8PICc5vBY9MUltvv_u2hTXeEYIORmiRzsOBt8K7FzrcNAjmuBVLfNdL2A2xsrQBruJsdPaSroso0Ljrq2MPwYJB56FzteKrXDiNUTfBqJnLnXrooCJUwGiquKuv7dmRto5QRgBZii2J3lbNM3K1YDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">متداول ارتفاع أعمدة الدخان في ايلات جنوب فلسطين المحتلة</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/84214" target="_blank">📅 15:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84213">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f07aff8569.mp4?token=o-KgmCvHr1yAnJ84Y7I3txIZGuWf9VOAHmcQ7zWV-tgjeKP6TM0cuyzApANg9ZKPjTmR-3BMvokAaG1Hh5je7b7nNwAnZf9kHu392KWXVaAo5CDRmsel0Ex5j3EUKmU2E47xSS93MXym6aFtzyAxbH28oFcwRK4OOSG9xEgHj8vrTwOZ141nqAaVP1Iux9LoCy7uejjTZCv6AnuzHHXR2DlTe2TPJlFgsO1CXnNPCyMwgzfIZmQKA0PQLsinnFmYB5o9eUYtW0AKor34hanjPpPlnI4eK-ebPlobe7Fn3-yv_N1IVixrqzdmsJwXjhodks6xfQsgLyRNnzw1mPVJKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f07aff8569.mp4?token=o-KgmCvHr1yAnJ84Y7I3txIZGuWf9VOAHmcQ7zWV-tgjeKP6TM0cuyzApANg9ZKPjTmR-3BMvokAaG1Hh5je7b7nNwAnZf9kHu392KWXVaAo5CDRmsel0Ex5j3EUKmU2E47xSS93MXym6aFtzyAxbH28oFcwRK4OOSG9xEgHj8vrTwOZ141nqAaVP1Iux9LoCy7uejjTZCv6AnuzHHXR2DlTe2TPJlFgsO1CXnNPCyMwgzfIZmQKA0PQLsinnFmYB5o9eUYtW0AKor34hanjPpPlnI4eK-ebPlobe7Fn3-yv_N1IVixrqzdmsJwXjhodks6xfQsgLyRNnzw1mPVJKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعلام العدو: سقوط شضايا في ايلات</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/84213" target="_blank">📅 15:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84211">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O83ESLvLZBda5gB4I0r809RmFf-A8VU_EBtvM0hxkMmwXq6IvzXNSNAGvSTMoPQUAlXoayJtguY2FdqLwvzorzF_eBni-dOAV566k0l4IVeqE8a3mc7P_76fiU_dyvXi2PzFe7-tdlyLTJ9iZIGA9pFgG6IfijIccX3BNMbfQq5KLscjhsubPukdL1PVTJ8zlezsI6qiGefOAi3wgNmAhMI9rvCCcgUBEGIxAmUxA2Gw2Fom0hmdI3OgOFL4x7iGFGxa8WeKK7qDPHgLiw1lm9b9pyaD6RtaxdzG4wDaJHmRvuL9hGhisNf5Trc7uOAv6AzUX3QKC4bJxmBhH2OPtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nePQMxeGOBUuwO-e8wmrrr_ihnLcYZBJbhg2EPB-1bCYkSnEXcAJenQ7X8svd8IN3p88vDBVWN66sZFpdo8wAzDTPc-hzdkUgkEvg-ZcLmm6PbukZb3Nrb4OCSO5M8Gkq6qJxq38EomW2KXwdfyIMBtAL9okk8dc0FTimoGQ0TWBbVAceObJqqrxCvtcACT8t11lupJUPzA3CuHp58PQuMs-eywYFneG6n47LXAyTq0J7K4734KgsuBYC2HyW5aaY1uLG_maEVcndQdS-2jcdNi2MKXSEBdstL85lhBI9Vgw72kFLltKnaBK_4B7z8u6rluiPanl_I2mGkss74vY7A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طيران المدني يغادر ويبتعد عن الأجواء في الأردن نتيجة القصف الإيراني على العقبة …</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/84211" target="_blank">📅 15:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84210">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">اعلام العدو: اطلاق صاروخين من القبة الحديدية للتصدي للصواريخ في سماء الاردن</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/84210" target="_blank">📅 15:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84209">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">إيقاف هبوط واقلاع الطائرات من مطار رامون شمال إيلات بعد الهجوم الايراني</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/84209" target="_blank">📅 15:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84208">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">شلل يصيب السيطرات في اجواء الأردن ، الطيران المدني يغادر اجواء عمان</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/84208" target="_blank">📅 15:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84207">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">انفجارات في سماء ايلات</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/84207" target="_blank">📅 15:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84206">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">انفجارات تهز إيلات</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/84206" target="_blank">📅 15:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84205">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/scosYyV8eOZawk9Nu2tgFi4EY0HvUdcUQ02nJCHiyr7EY_X7hvY9QYarWSA5GsoCblYoSSIfWAkq_g48zIgvF3ul8aIBQyBiK8-1XN1DSdm0yMHYhrtpdr8VXlpYhcoQkXzb3IXA_nTX-x_QguB6P81mfROLlZHVHaGpHT3sqkSuBPZqHx7MvBH0VCmbdiGgBfbAkvLI_sY0VDsFd_ClERW1g41nyg5aKF_U1bS8iFEjURNetMa9_MpauqJw0mpyOj2UYn7c1n-1JoUn6pYz-aCQlSbvYT8Gc9NTPMq81vu50knge2kYdPGIFIz2ezQAE_lKwHHW1Tl7b8UNN_fSCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سماء ايلات</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/84205" target="_blank">📅 15:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84204">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rl3MYMvYvJxxd-loT50fsQ0E0UB6CrNoGkt5ylXw0OXbD19fokoyV1Fd9077_ncJKpn4RNqfk2Zqoua9_shcWwpAVEwzPnQ5pzGleXjeqkoeHkWjK90JOagKUjmv281gruvePLevozzbrBh3Cg6-HbEAADquL2rWA-7Vg8jhGFgrw3cso6kcc1NSUG7E2xYxSVD66SYNjcbG20Nlv_KW0UhAOEIu5GaXo1cHSWRy48Re1ZS5HmAMxtDmsLiQFZ3vg5q2vmCGmUTrfJ0Lwp3EFFksIyFggCovi7ZI7UH7ljqGFDqrqlkID8BTjMtdY9BhzhXA78sDWUBEEHoGrbXcMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من سماء ايلات</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/84204" target="_blank">📅 15:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84203">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/geh1FFDc_nrdJVTMHztxV0gYgEIdLVV0tDbI1lt54yZ8V7atHrjRh1_GRslcFn57WQ-01V9Sumbuv9x22r63vtGLIq-lJ-iHPqeADHqUiHxocn6bZP4GP0tBiSbngKnODTlikOX9IFMkTKH9IOE9cSzxMHYbCDSMlJ3PdrQpKp5Od2_MQ_qSZjFbmngVXRR-K80oB4OcwQP8rcDVWipqZIx9MkyG0oFKQ9nORJGOzihrXGmXH6pHss58f38GVsk6a9-kQrPA_-WGjGNYTtflv5vTEA0SX43qEnlcUkvj7BXHvhnoau7ZyC2wLHdo8jfTYvtFhT3b-Y88zcRQE9Yimw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صافرات الانذار تدوي في العاصمة الاردنية عمان</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/84203" target="_blank">📅 15:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84202">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e79776748.mp4?token=mfol-NNVukG5y1sFKot2kJ3EILsIK6b0sd8l5dArFrHzyL-bJYxuE5WABloW4D6ozQRdWPJGcpHgYDPBairXztRBSisNwcQ2s0RB21nnmjoPkpAVAz96UlOb6lp7hivsLlL35wo2TIcwH4V7IAFTHuhnffOvqV40le6OlyhCJ_WVzjVVyuHL3VOK5f0vqTHSfCVA2-vPdyo4mpYrWcQUrlh7N-CK7O9PE_j39M7Tv7zvhhezpVWYJGAFJsuZQ_9WeMfrwe0zmOJ13Xk6opc2lYh50lBO22bX1q5-6npbewJ26tfJLJROKjnY4cPo3U7I9EtQefK9CcCjUnfkyuo1fhK7BLkZvj-WLIvEJVuD-5awqWYHku0GtZOFnhHTRTO0aLfnNPovfD9ZJ3xVooM6quatsuJ1aYRxuCyCV1WpRM-ASu8goAE2VXxz2NKgmgzQFiLadFCVqnwTaSoGeuR-pZ5743zQgcWVZ2p5CqU_jo3IYujBNYDnGbnjPnrZs8FnFux7eB0KfoR2upKQTq-qbq7wUKbpb0eUegL1rE63ZByixq24vuflJoRXoQ4Wh4GHxPdUE9k-7OHKPQ11Ogq_9a5if4LAVkAAgeRG_H7E09MTLRB1B-KPHH4QVDa0qvgLWPUVByDb8_Nf1DYkkkE_2g39H5P7v9AltMB7I5oxndE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e79776748.mp4?token=mfol-NNVukG5y1sFKot2kJ3EILsIK6b0sd8l5dArFrHzyL-bJYxuE5WABloW4D6ozQRdWPJGcpHgYDPBairXztRBSisNwcQ2s0RB21nnmjoPkpAVAz96UlOb6lp7hivsLlL35wo2TIcwH4V7IAFTHuhnffOvqV40le6OlyhCJ_WVzjVVyuHL3VOK5f0vqTHSfCVA2-vPdyo4mpYrWcQUrlh7N-CK7O9PE_j39M7Tv7zvhhezpVWYJGAFJsuZQ_9WeMfrwe0zmOJ13Xk6opc2lYh50lBO22bX1q5-6npbewJ26tfJLJROKjnY4cPo3U7I9EtQefK9CcCjUnfkyuo1fhK7BLkZvj-WLIvEJVuD-5awqWYHku0GtZOFnhHTRTO0aLfnNPovfD9ZJ3xVooM6quatsuJ1aYRxuCyCV1WpRM-ASu8goAE2VXxz2NKgmgzQFiLadFCVqnwTaSoGeuR-pZ5743zQgcWVZ2p5CqU_jo3IYujBNYDnGbnjPnrZs8FnFux7eB0KfoR2upKQTq-qbq7wUKbpb0eUegL1rE63ZByixq24vuflJoRXoQ4Wh4GHxPdUE9k-7OHKPQ11Ogq_9a5if4LAVkAAgeRG_H7E09MTLRB1B-KPHH4QVDa0qvgLWPUVByDb8_Nf1DYkkkE_2g39H5P7v9AltMB7I5oxndE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دوي انفجارات في ايلات جنوبي الكيان نتيجة الهجوم الصاروخي على العقبة الاردنية</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/84202" target="_blank">📅 15:45 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84201">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">المتحدث باسم جيش العدو الإسرائيلي: قبل وقت قصير، تم رصد عمليات إطلاق من إيران باتجاه مدينة العقبة في الأردن، وقد تحدث شظايا أو سقوط بقايا مقذوفات داخل أراضي اسرائيل نتيجة هذا الإطلاق.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/84201" target="_blank">📅 15:42 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84200">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">صواريخ تتجه الى العقبة</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/84200" target="_blank">📅 15:39 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84199">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">صافرات الانذار تدوي في الاردن</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/84199" target="_blank">📅 15:39 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84198">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">صواريخ باتجاه الاردن</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/84198" target="_blank">📅 15:38 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84197">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">انباء اولية عن اطلاق صواريخ من ايران</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/84197" target="_blank">📅 15:38 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84196">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">انباء اولية عن اطلاق صواريخ من ايران</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/84196" target="_blank">📅 15:37 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84195">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uUiFwOHz-yvnhAalnqqMLNmVfMyCMoypBmNNkBI3H9P5V92pgKGuokiEKu7MDPXVWFgRa55m0kfja231lABrLYwuXq0iedYvu9tuYh_AIuBi-jSb7SzlDmrpMM5-jaeHC0Q1iJInFVDtunCcc2Ua7xYAORMsJYwQHYGTwx64FDpI3mCFGdkSHxL_m_Evl0-x3ZJrGYWb8l5EhG6JfwSYOjnw7jycILaMMko3e4TQ6tfrbdIHkSX2WJfkbJVTpVZBQCM8JPIGeIlF9RNTIUFkKwjPno3240XhUqBlAg_i3EgfERdArlSeR1X8nnWkHEZwMIkI-qjvV479d3n7Ri1eTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
‏على الجمهوريين إضافة إيران إلى مشروع قانون العقوبات على روسيا. هذا ما أراده ليندسي، وكان سيحدث لا محالة. هام!</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/84195" target="_blank">📅 15:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84194">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">مجلس النواب العراقي يصوت على إعفاء قائد القوة البحرية وآخرين بسبب تقصيرهم بشأن فاجعة قتل الصياد العراقي من قبل عصابات خفر السواحل الكويتية والاعتداء على الصيادين الآخرين.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/84194" target="_blank">📅 15:26 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84193">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🇮🇶
🇰🇼
مجلس النواب العراقي يُصوت على إضافة فقرة على جدول أعماله قراءة تقرير لجنة الامن والدفاع بخصوص استشهاد الصياد العراقي من محافظة البصرة على يد عصابات خفر السواحل الكويتية.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/84193" target="_blank">📅 15:24 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84192">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🇮🇷
🇺🇸
القضاء الايراني:
لم يتم إطلاق سراح أي سجين أمريكي بالمواصفات التي ذكرها ترامب من سجون إيران. السيدة التي يتم الحديث عنها لم تكن سجينة ولم تتهم بالتجسس. ترامب في وضع صعب للغاية ويحتاج إلى إظهار أي إنجاز. حتى خروج مواطن إيراني-أمريكي من البلاد.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/84192" target="_blank">📅 15:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84191">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇰🇼
‏الكهرباء الكويتية: محطة للكهرباء وتحلية المياه تعرضت لهجوم للمرة الثانية خلال يومين</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/84191" target="_blank">📅 14:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84190">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇰🇼
‏
الكهرباء الكويتية:
محطة للكهرباء وتحلية المياه تعرضت لهجوم للمرة الثانية خلال يومين</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/84190" target="_blank">📅 14:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84189">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">عراقجي: كل شيء بدأ بتصور إيران كدولة ضعيفة؛ حيث ساد الاعتقاد بأن هذه الدولة فقدت قدرتها على الردع في المنطقة، وأنها ستلجأ إلى الردع النووي لتعويض ذلك.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/84189" target="_blank">📅 14:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84188">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇮🇶
🇰🇼
مجلس النواب العراقي يُصوت على إضافة فقرة على جدول أعماله قراءة تقرير لجنة الامن والدفاع بخصوص استشهاد الصياد العراقي من محافظة البصرة على يد عصابات خفر السواحل الكويتية.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/84188" target="_blank">📅 14:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84187">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔻
مصدر في موانئ البصرة العراقية:
- الناقلة Surename الراسية على أحد أرصفة التصدير ستنهي عمليات تحميل شحنتها البالغة 2 مليون برميل مساء اليوم الأحد
- من المتوقع ان تكمل الناقلة Bahamas الراسية على منصة SPM1 تحميل شحنتها البالغة 2 مليون برميل يوم غد الاثنين.
- الناقلة Nissos Heraclea من المؤمل أن ترسو مساء اليوم الأحد لبدء عمليات تحميل شحنتها البالغة 2 مليون برميل.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/84187" target="_blank">📅 14:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84186">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇺🇸
🇯🇴
خلاف اردني امريكي  الاردن: لا صحة لما نشرته السفارة الأمريكية بشأن إخلاء مطار العقبة ومينائها</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/84186" target="_blank">📅 14:02 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84185">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇮🇷
🇺🇸
منظمة الطاقة الذرية الإيرانية:
حكومة الولايات المتحدة الإرهابية والمجرمة، التي لا تملك طبيعة سوى التسلط وانتهاك القوانين، قامت، في عمل عدواني ومتوحش يتعارض مع القوانين الدولية بشن هجوم على موقع بناء محطة دارخوين النووية - أحد رموز عزيمة واكتفاء إيران العلمي - باستخدام عدد من الصواريخ.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/84185" target="_blank">📅 13:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84184">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">‏السفارة الأميركية في الاردن: إخلاء المطار والميناء البحري بالعقبة جراء تهديد موثوق</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/84184" target="_blank">📅 13:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84183">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🇮🇷
وزير الخارجية الايراني عباس عراقجي:  منذ يوم الجمعة (قبل الحرب بيوم) كانت الأجواء تتجه نحو الحرب. التقيت برئيس الجمهورية يوم السبت في الساعة 8 صباحًا، وأخبرته أن "الأجواء حربية". كنا عادةً نقدم التقارير للسيد حجازي، وكان هو يرسلها إلى القيادة. التقيت بالسيد…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/84183" target="_blank">📅 13:49 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84182">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🇮🇷
وزير الخارجية الايراني عباس عراقجي:
منذ يوم الجمعة
(
قبل الحرب بيوم
)
كانت الأجواء تتجه نحو الحرب. التقيت برئيس الجمهورية يوم السبت في الساعة 8 صباحًا، وأخبرته أن "الأجواء حربية". كنا عادةً نقدم التقارير للسيد حجازي، وكان هو يرسلها إلى القيادة. التقيت بالسيد حجازي في الساعة 9، وقدمت له تقرير المفاوضات، وعندما كنت أتحدث عن الأجواء الحربية المشحونة، تعرض المكان للهجوم.
كان المجلس الاستراتيجي للعلاقات الخارجية يعقد اجتماعه الأسبوعي المعتاد في ذلك الوقت، وكان الإمام الراحل موجودًا في مكتبه، كما كان الشهيد شمخاني يعقد اجتماع مجلس الدفاع. كان عقد الاجتماعات المتزامنة في ذلك اليوم أمرًا غير غريب؛ ولكن علم العدو بهذه الاجتماعات كان نتيجة لثغرة استخباراتية، والتي ربما لا تزال موجودة.
كان اجتماع الشهيد شمخاني مع القادة في مجلس الدفاع، ومكتب الشهيد شيرازي، ومكتب السيد حجازي، ومكتب الإمام الراحل، كلها تقع ضمن نطاق مكتب الإمام.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/84182" target="_blank">📅 13:43 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84181">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">‏السفارة الأميركية في الاردن: إخلاء المطار والميناء البحري بالعقبة جراء تهديد موثوق</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/84181" target="_blank">📅 13:30 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84180">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s1J62FvCisZCdwgOgXiMXvkQLOwzqO5xjyVfUbxDjtdz_wDwkFqO5qNrTskc8vs2yT4jLsyMjzNota04ojCo8z3NiN_1DeKVaK5y5kL5fRONym1-KD7mfWVkHFtwePrYZ7Jz-JYKESByoXluw9IOYOP3oe4Lxd7KK1NWtVYIKLWNto2B-DtWpmVcLmm4iTn78NXqGvXc_MroRjUimgLHTBjQg2PMsiJJCa6Yjbr7SGP6urCCtqJg2KQ8rWHJYTdspRjcty6kviE28B_3LNYr6oncn1iUgq4y9woM_fBzLZ_5b4x3FrQszqUKw86d8Cn3IFYznH31P9rwB-hJblR-AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سفارة موسكو في العراق تهنئ المجلس الأعلى الإسلامي بمناسبة عيد التاسيس !</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/84180" target="_blank">📅 13:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84179">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🇺🇸
🇯🇴
‏السفارة الأميركية في الاردن تطلب من رعاياها عدم السفر إلى مطار ومرفأ العقبة.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/84179" target="_blank">📅 13:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84178">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇺🇸
🇯🇴
‏السفارة الأميركية في الاردن تطلب من رعاياها عدم السفر إلى مطار ومرفأ العقبة.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/84178" target="_blank">📅 13:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84176">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vVuitNMnfsxiA0sqtLWuOFnTbSy6MQfrodS_oDelW8DfubYpYBYQbVSVUwzQJsQ3psaK49NA4XF0-qhnFlQfEDmEUImual2iMlTQj9f5MeQ_YsDJqPPfqsLivojkyaEeafvsXUXxCDKr6hbvHgLIPWdY-cyNdACr4a66RaFS-m3-FWBjPY6i60-37VVWOGw2A2e2eU3Kl7VgdxT9-gNJGMmBTgnjt3RcjU38a0YT3bQOHMbUavDqhSDNhmxW97qJ0sn-xuvT-ClFLndcXNz0H1zGfShHJjq4vbhHZRLMmlMc2FndPA48ToLPLduL25KpqrMeUPR5iSC8n_rZUvhgRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c0HudP7-6tcSQVZ0k9BQKbuipCafSvCtay3RH9C_G5sQiVEwdqFYXFhvAN5n99ikbUf8zt5bTZ62ngh6eUhrKmjuR1DizMxPOmW8ZEhCz3x6duCvmruJ3ecHEgQCydcPSa6La7GfudSnoTqy7qopD9bGKsE6rYJ5bi6VE7M7nmP7YvDo4MhVD6NdCXmT-RNoPoJImHlCQfoYUahX4M5hDiDVi6BnKd8J-HpfkkqM4bB5dpNK07YbXH4TFpqLNSl_XY_mdQvYxqsdNLc83FofgLHR25cezIWtmQG4aIx5mvTc1r52NGB-BwcygjbSe7fRaD93n1MYkLMd6I6YZc3Stg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇰🇼
لاسباب غير معروفة..
طائرات كويتية تحلق بشكل دائرة بنفس النقطة.
يمكن اعراض القزو هاي
😄</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/84176" target="_blank">📅 13:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84175">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇮🇷
قوات حرس الثورة الإسلامية البحرية:
- قبل ساعات، حاولت أربع سفن مخالفة، بدعم من الإرهابيين المدعومين من الولايات المتحدة، وتعطيل أنظمة الملاحة، وتجاهلًا لتحذيرات مركز التحكم في مضيق هرمز التابع لقوات البحرية التابعة لحرس الثورة الإسلامية، تعطيل حركة المرور والخروج من مضيق هرمز عبر مسار غير آمن. وقد تعرضت سفينتان من بينها لحادث وتوقفت في مكانها، بينما تراجعت السفينتان الأخريان عن مواصلة المسار.
- تعلن قوات البحرية التابعة لحرس الثورة الإسلامية أن السيطرة على مضيق هرمز تقع بالكامل في يد هذه القوات، وأن المسار الآمن الوحيد هو المسار المحدد والمعلن. كما تؤكد أن أي كمية من النفط والغاز والأسمدة لن تعبر مضيق هرمز إلا بتنسيق وإذن مسبقين.
- السفن التي تتأثر بإنشاءات العدو الأمريكي وتدخل مسارًا غير آمن، ستتعرض بالتأكيد لحوادث.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/84175" target="_blank">📅 13:06 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84174">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g1EQ_6Hcf3rqlPS1nRGFhbBV80ZqyhjnaEYyItVVpaorRWBssjV83junmOVoidTsCIcWKnUlR4WBTqfa0OD7QoAJdydHwZN5ap9vQNzpsNZTFTLtaHNKCKD_AGhVKk7fd-6SV2GzjZ4h0RfdMaH6r1FP9jPLDJPa2KWL7KpvW_sAcys1c_8byG54-noqb72UYEqO8qKkxxA_YeqNizMUSG4guFQb2Lj-KHPYw_3CwcmWVqgxH42nm_wz25LbeuMqjeI8JeHVtBeTHVK0A34vCrT2QrTDHCQtFECKr2DAvEA06dGAt5AG1tGgJmkdHEKebxlwVxM2Ve20YcRRMn9zVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قاليباف:
ينبغي لنا أن نعتبر طاعة المرسوم الديني والوطني الصادر عن القائد الأعلى للثورة جزءًا مهمًا من دورنا التاريخي في هذه المقاومة الوطنية وفي حكم البلاد.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/84174" target="_blank">📅 12:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84173">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50ae58319d.mp4?token=PUaTuUmxboH83FB8LDh4MOn9e88S1Ynou_YjqwlKt0uvPcaKEjI2tM-5pjtIfqBjQlSzQqqIHcL1X4Lsl5W2pEZu0POvNkrdLOLeIe6UsOAqkU-YB-Qbelzvf44a1EpQc9hY1_ON5w3GkePMlpXkM_h6leDgyn1QnL1vlGfc92RWwDDHf-Y5JgKA5Am64UauJDGVRVljkYJYv7dy90LUz6fu0sM6Lpz2SJqOtgag7hbylw53WsuSKrrxnufh54m602_ChopZBjqz2Pt5SowSOnUfRrftvVfufvmN16oXWBm08YEQcsDFGXmxQMbHPbWo4DKe0gqwMWnQieKoBheOoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50ae58319d.mp4?token=PUaTuUmxboH83FB8LDh4MOn9e88S1Ynou_YjqwlKt0uvPcaKEjI2tM-5pjtIfqBjQlSzQqqIHcL1X4Lsl5W2pEZu0POvNkrdLOLeIe6UsOAqkU-YB-Qbelzvf44a1EpQc9hY1_ON5w3GkePMlpXkM_h6leDgyn1QnL1vlGfc92RWwDDHf-Y5JgKA5Am64UauJDGVRVljkYJYv7dy90LUz6fu0sM6Lpz2SJqOtgag7hbylw53WsuSKrrxnufh54m602_ChopZBjqz2Pt5SowSOnUfRrftvVfufvmN16oXWBm08YEQcsDFGXmxQMbHPbWo4DKe0gqwMWnQieKoBheOoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبر سيء للكويت
🇮🇷
🇰🇼
عضو في لجنة الأمن القومي الايراني: يجب أن تعلم الكويت أن وضعها لن يكون طبيعياً بعد انتهاء هذه الحرب. نعتبر الهجمات التي انطلقت من الكويت هجمات مباشرة، ويجب أن تعلم أننا سنتعامل معها بشكل خاص.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/84173" target="_blank">📅 12:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84172">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🇮🇶
القضاء العراقي:
إلقاء القبض على متهمين اثنين اعترفا بانتمائهما إلى ما يسمى حركة دين السلام والنور الأحمدية المعروفة بحركة اليماني.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/84172" target="_blank">📅 12:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84171">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇲🇱
مقتل 50 عسكريا بهجوم مسلح في مالي</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/84171" target="_blank">📅 12:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84170">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">سماء البحرين في هذه اللحظات بعد الهجوم الإيراني</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/84170" target="_blank">📅 12:26 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84169">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nsk3LQzycNB74N8llN25jdyA9dmce4l5xrmu9z9iGypIrmGmNXAYRKe9ZJOCVNee9RYoMC67e4JpwND_4xs3wtSgjChD5Kc5BKrtGzVCaU1VMUPs-Mf8xtHrmtZvGFIvwWV4A-FI2HGmlmFR2ry8PFYNMVkmIAH12fJo_Rsy1atOBgnouQTLuBBFs0L2Oo7esSYJAn35bfmpUtIjzgx_bMTtScTPxUkVIoniHelgu6f8HF_Fdi620STMo2EbGD7p-iBn6BsM0xE1xA-Yc5ybvL2gm62P4-UmRM4Vih6bmzFR2Xx_sTm99zlCh_1EsePB-gb62adt2NIjF63F1qPCCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">البحرين: نتعرض لهجوم جوي ضخم</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/84169" target="_blank">📅 12:24 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84168">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">البحرين: نتعرض لهجوم جوي ضخم</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/84168" target="_blank">📅 12:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84167">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">البحرين: نتعرض لهجوم جوي ضخم</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/84167" target="_blank">📅 12:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84166">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6df9cce2a3.mp4?token=pmBPgEQnhBqy2VpGw6-3s8bl1ycn9oCaLmQ5LKa1gBCXKeTOUt6Mo9qMH2KSAPR8Uc3Du1akg_PBj3FKdbKOk014UCMMyfoIoEYvTA-ICyYIhhNdNFTWmCZBndA5yPy_zIJu9Fxdc5FeaADuKmud28LAs8zepFM4F4cWG7gcTQOovOBv5CNUcE1b0Pk9bft31tD153qRdDUQZEsf1Q66ohNuJUzn7qdkWou7_hBTlaiTvgNuys7YVFBzs6HcrVPs93FWbxwJRekKBbHDSBCk4C3NRlpl8JtmJHVatlM7D7j56-zKZb4Duy2Qws-QgHxqOfpoVwpM3XrwrX6Nvr_Cuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6df9cce2a3.mp4?token=pmBPgEQnhBqy2VpGw6-3s8bl1ycn9oCaLmQ5LKa1gBCXKeTOUt6Mo9qMH2KSAPR8Uc3Du1akg_PBj3FKdbKOk014UCMMyfoIoEYvTA-ICyYIhhNdNFTWmCZBndA5yPy_zIJu9Fxdc5FeaADuKmud28LAs8zepFM4F4cWG7gcTQOovOBv5CNUcE1b0Pk9bft31tD153qRdDUQZEsf1Q66ohNuJUzn7qdkWou7_hBTlaiTvgNuys7YVFBzs6HcrVPs93FWbxwJRekKBbHDSBCk4C3NRlpl8JtmJHVatlM7D7j56-zKZb4Duy2Qws-QgHxqOfpoVwpM3XrwrX6Nvr_Cuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مشاهد لتدمير طائرة مسيرة من طراز MQ9 تابعة للجيش الأمريكي الإرهابي، وذلك على يد مقاتلي القوة البحرية التابعة لحرس الثورة الإسلامية في منطقة عسلويّة.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/84166" target="_blank">📅 12:06 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84165">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ilcfs_Zc2bXT18UcWASophHfqeJ6LS5p9gPL3yCGa5QNNamgOeE75w2gr2F7pshZUfwmd_odqPp3S6vjYxGPxRSf3Xar1Oa0MVFPGVR8ts83t_I81sovY5WBPnNgkUTVdQt_wEjyIEgAIoWWKBZ1L0AOsVp6C7gJyjpOsHhks4q6SUGq6J1PprhD--UHk6T7NU9dEkmy65rFSf_c7SAHUzSkRbOWAszIIiMZErFk6nGGwI5MMAz0-6k_tJ61XeqNdTy7eZCd5eMXeGup7J2Vw384Ulxu-bzZgVEoWh2NKWuknxFRwh16Qsq6uMj2iFamF9_WsehgevFeLsuovpKTew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طائرة تزود بالوقود أمريكية تنشط فوق مياه الخليج الفارسي قبالة سواحل الإمارات.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/84165" target="_blank">📅 12:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84164">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">تجدد الانفجارات في البحرين</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/84164" target="_blank">📅 11:59 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84163">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bux6Asw0OrUE1JSES8u6IRnIyEBpP4OYz-eCCLiQYaILntxup83PDC_ecthTTO7skiFh2VmqJDfkn9Q_XHqItCxP1VXVyCSIeCUSpGgOLRRpKtXEyOxhG6x14Iv2_rlUZ91FUtbRLijtbc9rpbzW1NDGfaCKXzkuuiSNRgxLXUC_go-_LG-a90ycQkQUKciJoXKqZ27-T9ZQ4fAeG1S8e2C4GNuRP-3VTfgJOzWKFQSiICtrTJFqj-jV8nawZPlsH54qJuRIjP0muoR3sUMmUVGNADn8DBwg5JJeNvWUDMA75LQRlhuGR3aprv-1jA5ZIeOSWK3RBPh_Scew-qvFWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجارات تهز البحرين في هذه الأثناء</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/84163" target="_blank">📅 11:56 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84162">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">انفجارات تهز البحرين في هذه الأثناء</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/84162" target="_blank">📅 11:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84161">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">انفجارات تهز البحرين في هذه الأثناء</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/84161" target="_blank">📅 11:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84160">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">انفجارات تهز البحرين في هذه الأثناء</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/84160" target="_blank">📅 11:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84159">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nwUFDO-un3IV-Qz-0NAAATKARwmiH4GouIzH2S41IVx0cmFLlZvWqX4F-4fkL8wNNGCyepyQaKDA84u6EjtdQ59MWYJ30rSghUouP5sVyeNVN4FRw_Opy3VTpZvH107GR2ER-flli9XeRbWt7iDzP7GlR3OM6z0dO4Mq0_Eftb1vky0MDoeQ-qxxqs-GKacQnQTIhgZ4hnDEMOpMr44iWoCfK0G7_hYG76DlsJF-RINKGYqEl_coTn4pYlcC2cLaHwATThzK_v0mqtwF5HNuaxuQFA3tB38aafIw-_tzER9OEOeIBcOqeVffmrpilAb0lNkCcv_NG8d7clsvw3KfYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفارات الإنذار تدوي باستمرار</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/84159" target="_blank">📅 11:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84158">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">انفجارات تهز البحرين في هذه الأثناء</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/84158" target="_blank">📅 11:45 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84157">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">انفجارات تهز البحرين في هذه الأثناء</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/84157" target="_blank">📅 11:45 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84156">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/84156" target="_blank">📅 11:45 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84155">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🇮🇶
انفجارات تهز محافظة أربيل شمال العراق</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/84155" target="_blank">📅 11:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84154">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🇮🇶
انفجارات تهز محافظة أربيل شمال العراق</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/84154" target="_blank">📅 11:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84153">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔻
مراسل نايا: لا يوجد أي حدث أمني في تشابهار وصوت الانفجار قبل قليل يعود لتفجير ذخائر حربية.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/84153" target="_blank">📅 10:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84152">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">سماء الكويت تهتز اثر الصواريخ الإيرانية</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/84152" target="_blank">📅 10:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84151">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">سماء العاصمة الكويتية الآن بعد الهجوم الصاروخي الإيراني</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/84151" target="_blank">📅 10:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84150">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XQCbmi5FVWK6QmIqtcz_vFqSIwwDZCjf8C7qtQo53j7mJi6cGXQ-boHw3L2uf50oEmY_e1MC07VZx7sYjko-t0QL_X0iBNm6MeovUwKOrv8hDAVtpwge31aHPl-Tl-r0ZfrP8MhPeV6j5hcSEQXOD03sZl3l68id7cKqxI_QSkUBLRwaS2PS_FOHYNGbmouTh1EMErKEwH3_p4C_BuqDcpTWdHpV6K1oFHGC7jVUfQbtApcGm0Q-DHm3XmO7e5HwqQKLkC22w0n1az7wp6nDU4UOf-qxolJio1CyVvSjR3hxBrrxWMEWrmikf4XNkLyYlT_WAeYUGAdKUXPminH85g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سماء منطقة الجهراء في الكويت</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/84150" target="_blank">📅 10:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84149">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nniAbCcMpSSVMtuuGCAMPwerbqLZcwcuZBpQb9O91pPA-JKOIa1lpCXAmQUtHBpwo0IyW9PvmTJ8Xw-B9K35HF1uTXQaavgLQElLwGJy5AR1pJmRkz6y1V7s47WGHfcZMzP3to1ajXJNTzIkMxBnGoQ4R1XyXH9atqkgvzoWNZzZyqs10yYI0m0_DKhTxpEwt9h0qLAnLvZA2YQBruTE8z59OoOfKCcz4S1_OFDa7IUC6GganaBqwpnbhWDny7oSzPKG9JtlCMeXE0zQJZ0XIHazKOVTamglnPAvlCGr6cTyo-KbsUPMWJliR5mSv4fjvbrFWMPfht5LfmanVe3XAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سماء العاصمة الكويتية الآن بعد الهجوم الصاروخي الإيراني</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/84149" target="_blank">📅 10:06 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84148">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/248e6a79d1.mp4?token=JezVMkIdVq-DZW71hZvRtcGBxlDfAk4drHdh5rh1yEbm-FhyU1YK7DVp8kfLeyR2xYsw6btysslr5Btf1xy952O9Ye4S47Q-IyFuYe1_PnnvAOHre2Q94we9AwkMc2psYp6aLlHGiK_KBTPYdb__Bliv_Z-mq-NdJsrSbGyQDxu3AMv0V6e7s68aOwyKswCFhJmgq92t0ApIePXtl0EMMrmkn0cn7iMOpGgRyoUlMCMP7Kvtev-97oTTQOujAUEst1Np785LjOjRDYvCcYHBxAo_ACLDQXNFEEHDsRaHZH8wPiklzHa9b4hp3KzLEfFFkbLBTv7wF5w2TIt9M5I45Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/248e6a79d1.mp4?token=JezVMkIdVq-DZW71hZvRtcGBxlDfAk4drHdh5rh1yEbm-FhyU1YK7DVp8kfLeyR2xYsw6btysslr5Btf1xy952O9Ye4S47Q-IyFuYe1_PnnvAOHre2Q94we9AwkMc2psYp6aLlHGiK_KBTPYdb__Bliv_Z-mq-NdJsrSbGyQDxu3AMv0V6e7s68aOwyKswCFhJmgq92t0ApIePXtl0EMMrmkn0cn7iMOpGgRyoUlMCMP7Kvtev-97oTTQOujAUEst1Np785LjOjRDYvCcYHBxAo_ACLDQXNFEEHDsRaHZH8wPiklzHa9b4hp3KzLEfFFkbLBTv7wF5w2TIt9M5I45Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سماء العاصمة الكويتية الآن بعد الهجوم الصاروخي الإيراني</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/84148" target="_blank">📅 10:04 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84147">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/84147" target="_blank">📅 10:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84146">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">الفرار الفرار حيدر آمد شكار _ شور مزلزل _ الفرار الفرار جاء حيدر…</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/84146" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔻
الفرار الفرار..</div>
<div class="tg-footer">👁️ 7.64K · <a href="https://t.me/naya_foriraq/84146" target="_blank">📅 10:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84145">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">إصابة مباشرة في قاعدة علي السالم بالكويت</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/84145" target="_blank">📅 10:02 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84144">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/84144" target="_blank">📅 10:02 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84143">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">صفارات الإنذار تدوي في الكويت اثر هجوم جوي ايراني</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/84143" target="_blank">📅 10:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84142">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/84142" target="_blank">📅 09:58 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84141">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/84141" target="_blank">📅 09:58 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84140">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/84140" target="_blank">📅 09:58 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84139">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇸🇾
دوي انفجارات في محافظة القنيطرة جنوب سوريا</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/84139" target="_blank">📅 09:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84138">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇸🇾
دوي انفجارات في محافظة القنيطرة جنوب سوريا</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/84138" target="_blank">📅 09:24 · 28 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
