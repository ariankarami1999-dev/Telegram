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
<img src="https://cdn4.telesco.pe/file/VodC7mPs4FrQXNI7816SdJh8oz1GJxa1vr6Qo63Hy4sSZ0Drh5plf5xmY9lEj6aY4UCtQLNcQzbxB99TAXB2qf2Wa1ra4Ka5NdmZi5S6dAwKE6OjMOiWkJgtyi7UHglsutJ2uc3YQZRLQbM4yD6hI63HLxwO1Afrrm5VVrhxh0LqRU9O7NY4_v03619P7ozwcAzfz01Az9MuhN_dZ5Q3BLgOEgxCoPYwdBY9XP4zztZDBLTL5dLe7NaGjg4H6t5sZSKnkQ6BsSYVUgOSv0hUZoPwVKE_6JlW7nICtdbQh-Eg6NocZEycvj09DYEJl0MYoHN-p_qHIro2Rf1FQ1hAnA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 528K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-29 18:55:36</div>
<hr>

<div class="tg-post" id="msg-26161">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/021b11787b.mp4?token=azidKWydorsHFhKU-ahwZPmX8JVgF-APB173unGRUpnTJJ65fXxW8mvvi-9W2WQuGG2tsuH4x4HDb2HwachyM_Q0FRX8NvPUzVnBnln_ZdoDjB0SNtXfo5Wg-7jD4YF4lWfrm27nUoz3IM7DKtHU-M30NEaoPQvKY9FqCOSpuRdMo8y98HKnR03J4ppq1oB76K_nWxqSYhOZcNDyLZca8fE-KljasbzXB4CCwoWZ-ZbuQ9L3OFOpqsLo43nb0KSwHrp77MubMwEgxfFb80cCLC7znDLQVnWh8TgLJ2s0N1HcLtXsxEW_BHRXuR9yZQmAsjpCZ0L7dYdn0o2jyIaMiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/021b11787b.mp4?token=azidKWydorsHFhKU-ahwZPmX8JVgF-APB173unGRUpnTJJ65fXxW8mvvi-9W2WQuGG2tsuH4x4HDb2HwachyM_Q0FRX8NvPUzVnBnln_ZdoDjB0SNtXfo5Wg-7jD4YF4lWfrm27nUoz3IM7DKtHU-M30NEaoPQvKY9FqCOSpuRdMo8y98HKnR03J4ppq1oB76K_nWxqSYhOZcNDyLZca8fE-KljasbzXB4CCwoWZ-ZbuQ9L3OFOpqsLo43nb0KSwHrp77MubMwEgxfFb80cCLC7znDLQVnWh8TgLJ2s0N1HcLtXsxEW_BHRXuR9yZQmAsjpCZ0L7dYdn0o2jyIaMiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
جملات‌زیبای عادل‌فردوسی‌پور برای لیونل مسی فوق ستاره آرژانتینی‌فوتبال‌دنیا در پایان جام‌جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/persiana_Soccer/26161" target="_blank">📅 18:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26159">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/522741a6f4.mp4?token=iGsSYYrUH_Vi32QE6b8ZzvfJaTkI1NCjdlSC9bP-WWM9yuWBmiMCC1RMX0DLOpNFCBGq2tGestYSZDdia1I0TtcOH14Na04MiFhHPZPCAsrznDFNiaVZHkLHdxftHXYE5qi8qSPJrE09AYkWMnKwnmOXznvuApDpHIf1ZvxEi58yn_IGjddadjaODLoB3-A9zMpwR3IvhINp6J1uAdiStRM5ILjV7Y3ckdvtXaeVDIHURHi_ZOU4QtIdxUBq5MUFFo-ntKHQ3e1fhzUsqi5qTEyx4l78btfyRiM5V76BRtgIUnn2EVTAt6yCRt9yRi5AwPi59uDu3PFT1dBed9ygtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/522741a6f4.mp4?token=iGsSYYrUH_Vi32QE6b8ZzvfJaTkI1NCjdlSC9bP-WWM9yuWBmiMCC1RMX0DLOpNFCBGq2tGestYSZDdia1I0TtcOH14Na04MiFhHPZPCAsrznDFNiaVZHkLHdxftHXYE5qi8qSPJrE09AYkWMnKwnmOXznvuApDpHIf1ZvxEi58yn_IGjddadjaODLoB3-A9zMpwR3IvhINp6J1uAdiStRM5ILjV7Y3ckdvtXaeVDIHURHi_ZOU4QtIdxUBq5MUFFo-ntKHQ3e1fhzUsqi5qTEyx4l78btfyRiM5V76BRtgIUnn2EVTAt6yCRt9yRi5AwPi59uDu3PFT1dBed9ygtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سوتی خفن سوسن پرور دربرنامه اخیر قیاسی؛
قیاسی از سوسن خانم پرور میپرسه که کدوم ورزش رو دوست داری؟ میگه ژیمناستیک قیاسی میگه خب چرا؟ سوسن میگه: چون میخوابی پاتو میدی بالا!!!
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/persiana_Soccer/26159" target="_blank">📅 18:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26157">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/219a5ecb02.mp4?token=otSDe0w-AcpX9Ep5irZsqnRcoz8h7nafh8_70Kx2RUlM4ozKTamfLbhDAxvfm1UysXICk8s68fs6djxdimRR6IiP4mbqbhylt_COsrdtBWJHlGQoLbc46oL9mO-xYNYaoa5hiMdDlxzQaMD0gWSh5_X90uefdeBbbP-APNPxlinPRi3rmSgGZuzTWNBxd0IkqC5bcwH51L38lvxKWbKln6rvhbEBIn22gVyubWKJHtvC4WXq_12ZtEUVD8rxdmHcUOoR6epcpJOhqpLrqNGq48Xtq9U5zBV-S4eqcvVN4EMGlsKQ9QtgXtKr_IedOHr1hDLBjsnMsuksUDnesrOrpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/219a5ecb02.mp4?token=otSDe0w-AcpX9Ep5irZsqnRcoz8h7nafh8_70Kx2RUlM4ozKTamfLbhDAxvfm1UysXICk8s68fs6djxdimRR6IiP4mbqbhylt_COsrdtBWJHlGQoLbc46oL9mO-xYNYaoa5hiMdDlxzQaMD0gWSh5_X90uefdeBbbP-APNPxlinPRi3rmSgGZuzTWNBxd0IkqC5bcwH51L38lvxKWbKln6rvhbEBIn22gVyubWKJHtvC4WXq_12ZtEUVD8rxdmHcUOoR6epcpJOhqpLrqNGq48Xtq9U5zBV-S4eqcvVN4EMGlsKQ9QtgXtKr_IedOHr1hDLBjsnMsuksUDnesrOrpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دخترهاوقتی‌امتحان 19.75 میگیرند
🆚
پسرایی که امتحان 0.75 میگیرند و درباره‌اش حرف میزنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/persiana_Soccer/26157" target="_blank">📅 18:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26156">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fmfRnNJlIPjIdV5eNBGgB-XzM9NnRfUQHKxDP1r2-jUszIumufn6tS7ADKEF5J-dfcPmQpWQrdpPemOMzw_mUs2Y--K2DhtHJ4meZKSDxCXN9FAHKdxgMXrLFwHVcXUC4FhBU2mtYlDQ0u1NcM2GjhohWzn2hdec-W4cLT2fT8K2zqBwrJUltkOuNnc1vqy-oLzDdL6PqeHXLgKLpkgDN_t-J7M75iVRZnDlaC0_xBNxD_Yjy3qsEHS56kpLGR9TrdbEIHMivsBehX3MuHMHstD42uQGZskjZ8UP74Pv3zLwmsnYcFjLFyyXgZoG0DTGb8CgiPrGxJBmKtUtEafSyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بهترین گلر شش دوره‌اخیر جام جهانی؛ بوفون، کاسیاس، نویر، تیبو کورتوا، مارتینز و اونای سیمون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/persiana_Soccer/26156" target="_blank">📅 18:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26155">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TT39W1SulUzaD2SjX5TC3A0-NjJr3tfeOBhR28fc_m3oqknWIKn0lv38yfCrpAZQTiKntU5d5eTweUCPZHgkc8WzkjwYpqpwmEEzegsfpjbHWvPwL0SM80d5KVNc3AZDv11e68PTVsV3oknZUr-VthkFU5ClcKLEqglAn8NRY9LPVvrPh9nz0mXK5rjU5i5-RI1KLvt9F0M3tfHFL1ihrwW7YEO3aV4RwbZT0A2arieOs3o0PodkHapVHzpOLUWTy53oUModDmWfYuhWGDTRwP1PKt7zPFZWrjSmZVVv4iMMFwv-z-bjU7jsw6myHLpk5-22GrKtaD3L2FjZUyJrIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی پنج روز پیش پرشیانا
🔴
محمد عمری26ساله باحضور درساختمان باشگاه پرسپولیس قراردادش روبه‌مدت‌سه فصل تمدید کرد. حتی مدت‌دقیق‌قراردادش هم گفته بودیم. عمری آفر خوبی داشت ولی تارتار مخالفت کرد اینم موند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/persiana_Soccer/26155" target="_blank">📅 17:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26154">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b054f61942.mp4?token=sfjELI-Q81uLhG5oJ1GW1KRbzGK8pynJJ4kCGXxnm2syrYj6U-tbATM5a-4YcY8qz5j-1NBNhbRKIC_ffeDwpeRVgODBk9HKvbvzARwU20avh8hoxOQuOqgLsNNCJwQHer-keSZ0D6n4Jr8LQDxkpPGEK7XQmEQyWg96BmMLjmUSajBedsTVMU_u7IrUAtTYViBDO1573F2z3zjxjHx3xOHBZlcYxO2UqsDbRo0WtMaDLomKzqduDc-Zyah0NFDc2ttLDiA6EuoUEDogZwqI4j3bjdQRw-WM657RhzuJWl1XRvXZ-Jdbit4won_vqLpVlxHmBCirp2EpqCXhOpcbjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b054f61942.mp4?token=sfjELI-Q81uLhG5oJ1GW1KRbzGK8pynJJ4kCGXxnm2syrYj6U-tbATM5a-4YcY8qz5j-1NBNhbRKIC_ffeDwpeRVgODBk9HKvbvzARwU20avh8hoxOQuOqgLsNNCJwQHer-keSZ0D6n4Jr8LQDxkpPGEK7XQmEQyWg96BmMLjmUSajBedsTVMU_u7IrUAtTYViBDO1573F2z3zjxjHx3xOHBZlcYxO2UqsDbRo0WtMaDLomKzqduDc-Zyah0NFDc2ttLDiA6EuoUEDogZwqI4j3bjdQRw-WM657RhzuJWl1XRvXZ-Jdbit4won_vqLpVlxHmBCirp2EpqCXhOpcbjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
قالبی بسیار زیباوسنگین از فوق ستاره هایی که باعث‌شدند ماهاعاشق‌فوتبال بشیم. چه زود گذشت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/persiana_Soccer/26154" target="_blank">📅 17:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26153">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1819c235ea.mp4?token=ZZUK0w2J_k3bNS9lNdec3c-24_lDRicj-zI-fTD-exN2KgS8HGhYcMqakxrJAjIN-yRkJpBOGOWkTGhkUPg2-OzMNL13gfk6uw2lNLyKhEiryIw_Z2g-BN9DUCHn42wUNxB3r6L0yroipQUYyduMdVIB8j5lMYIW8ty1-g6FjjoiS49gST4eFedJrLNSTsRQcCGIJEhUO9uNUkiizdMZ0jA3IWhhz_zw3KhU2TIjEHNDqCfFcnrfzRouby5iGwIrvegrVMA0WcPB1kCIg_Z8Y2h72rnNKzSgkM2hGpuI_gNsD7kxSx0XGfCYRgOIqrd3ko3FrJJtF4oFswO8pgjemQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1819c235ea.mp4?token=ZZUK0w2J_k3bNS9lNdec3c-24_lDRicj-zI-fTD-exN2KgS8HGhYcMqakxrJAjIN-yRkJpBOGOWkTGhkUPg2-OzMNL13gfk6uw2lNLyKhEiryIw_Z2g-BN9DUCHn42wUNxB3r6L0yroipQUYyduMdVIB8j5lMYIW8ty1-g6FjjoiS49gST4eFedJrLNSTsRQcCGIJEhUO9uNUkiizdMZ0jA3IWhhz_zw3KhU2TIjEHNDqCfFcnrfzRouby5iGwIrvegrVMA0WcPB1kCIg_Z8Y2h72rnNKzSgkM2hGpuI_gNsD7kxSx0XGfCYRgOIqrd3ko3FrJJtF4oFswO8pgjemQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
نیکو ویلیامز ستاره‌تیم‌اسپانیابلافاصله بعد از اینکه مدل‌روگرفت به این‌شکل به مادرش تقدیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/persiana_Soccer/26153" target="_blank">📅 17:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26152">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AVWwYtqce66Up02mZbMO8WwkhqOZwSd_3dUYKSLFFziRNMcCfYWWYYbCa5TFKc68HO1K3rI4FJpB8O4nX_-1A6gFyqHpMqf_8OHVm1n563sKdbnQIIeOBZ_sVHxkU8GT3TVLuskOP0GW6baVTETkyPzyiKsFHfeR86QbM_vSviY0CbG3vO7t82bMH3VkyCvb4eOV53qE1aA6700LBWt7d3Ih4y1HyMruqXXn1uqW--z2zmGmpk9nTNhCkUN7OYXvfv3q4vyBRXTZf63x0ij_iTweIFKqbD4KV2RcoAcFfGjwm1uqwoz5SqzbpWus9aOfudNOYSh6yXPaLhYrXw60dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐉
میخوای به راحتی از فوتبال و باقی ورزش ها کسب درامد کنی؟!
⚠️
پس همین الان وارد کانال
Evil Bet
شو
چون بهت اموزش میده چطور دلاری پول دربیاری
❗️
💵
اینجا میتونی روزانه درامد داشته باشی و سرمایت چندبرابر کنی
👍
آدرس عضویت کانال vip:
https://t.me/+TmGWkUYH_8c0OWZk
https://t.me/+TmGWkUYH_8c0OWZk</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/persiana_Soccer/26152" target="_blank">📅 17:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26151">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jN-i0CfJ_YCFBMis3ucrnqpkx7jVRb8doAb1JgIoDebFc-X2p8HgUAdDsqShIy2zailyFQUn6Fty_upEZzczx-PT9G2clRp9cGnxxu-38Kl_3h589T8njKQ9K5HYPVfGgLzKoddaOuf8U0KzhgsO94GTTc59PyDKUHkrbAnUt7s4iLiVZud7fhpkVnXZymi8rGSTBa-z_s7ylef1bgrq7vfb5WW2Vd7zZ7k54we_YqWDh6z4TeELUyTzmGFZPO-b8CBX44yyFByXVA80qOrgGsgXEuBO9MRCI7GWwtToVFJ5Wla37gNIDJxx46fOwNg33J6R5g87TrKhZblkgj3eUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بهترین بازیکن 6 دوره اخیر جام جهانی؛ زیدان، فورلان، لئو مسی، لوکا مودریچ، لئو مسی و رودری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/persiana_Soccer/26151" target="_blank">📅 17:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26150">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l_zMz8EJkDzHF0cVYq8yYTTndy9zakXdVviRYjRXNDSkKESs9oxFjqmKFV5Mma3KkPr06z9UxRICabX3sXMBg6QhpLbIOAwOFDdiBQnQnjJEaYv6MXKKbpmA46TI_tG3ersSQwlBej25HEx_3WroBNKEunJ3gkOv27XdEfZY6hjKDcqwaiZLx6Il60rX4-kvYRFxoIVjtdKxT01f6L0UqQuBTCqbOxjbVnADL_Cn5WvbDrw4B4yvHmrAzbTVo3UmLXsDZRwfD-7lvoXgrUupnxRPh9lFPK0flBPejtJtl41thy7he2jtz0LtAUdSP_VX8PFhOYlRYamBLjatI6XN5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
درحالی که با قهرمانی اسپانیا هیچ گزینه قاطعی برای کسب توپ طلا دیده نمیشود ، فرانس فوتبال در آخرین‌آپدیت‌خود درماه آپریل "عملکرد فردی در تمام مسابقات بزرگ و مهم" را جزو ملاک‌های مهم انتخاب برنده توپ طلا در سال جاری اعلام کرده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/persiana_Soccer/26150" target="_blank">📅 17:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26149">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afc40ade6c.mp4?token=fIPsuwmWoYM6UEpL_Q0-jTAw_RvxWeAOzFQipoPxQuaJnKUE0inX4YXKBslwHtIRukn0TPzASx0iRd0PF-BuHUBQ409xnUyLHJm6WhKr--e13LEKUmd_5NssXQpaE1lXxipoPn_5_P103GqZDrYKE8f5PSH-IlGKpQ7_QsVCOSP80y9I99LrN_x6u9xy9NYcjy8YpaOLuA0fkN4Fy8SEw7K12M13mmTYlf7th3j950jhMcvv14XbpdX1re_W-pCnY1jnHOBt53IvXDKHh-D4pROEi6gJbPFKc0OSBpDlbVbaz8A4slSChP209FCAzJgn-touC9DxJy1AXqGsslJr0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afc40ade6c.mp4?token=fIPsuwmWoYM6UEpL_Q0-jTAw_RvxWeAOzFQipoPxQuaJnKUE0inX4YXKBslwHtIRukn0TPzASx0iRd0PF-BuHUBQ409xnUyLHJm6WhKr--e13LEKUmd_5NssXQpaE1lXxipoPn_5_P103GqZDrYKE8f5PSH-IlGKpQ7_QsVCOSP80y9I99LrN_x6u9xy9NYcjy8YpaOLuA0fkN4Fy8SEw7K12M13mmTYlf7th3j950jhMcvv14XbpdX1re_W-pCnY1jnHOBt53IvXDKHh-D4pROEi6gJbPFKc0OSBpDlbVbaz8A4slSChP209FCAzJgn-touC9DxJy1AXqGsslJr0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تمام امتحانات نهایی پایه‌های یازدهم و دوازدهم چهار استان هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان، تاآروم‌شدن شرایط لغو و به تعویق افتاد. وضعیت دانش آموزای  بقیه استان های ایران:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/persiana_Soccer/26149" target="_blank">📅 17:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26148">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BIoC6dgeHCxKfcGbldjQKzc1w7B8fnugWuFkXCPz8xQphTh6iHNrN3BSA5uNd8JYgFa0mJ2pIFWbhUIYmhVgAtT9CFIukecWcQnSNCbiu1GxSORUc4zwRgHdT8_BDM9ZuUcU_aB1zhcEdiyXhkBG5b2hPxDSLNfZzwzQHmhYqM1CGHPxlwwheibmKPxPGuG4pt6Jy7-no5J9d2n2GDCLhBQdKBaPiEsatFwRE59mLpdsM2OHSsiOiL6k8d8F8YSJ6QOrpBFOAMEiqNF11VdpA6IYkBhJBS-OSveMemvSKoQHdZEF923uBdQ-pyBVUCp4P78XYetlta4uX_cU95WuUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
تو نوزادی مسی با اون همه افتخار نشست کونش رو شست. تو دوره نوجوونی‌هم‌یه‌کلی جام با بارسلونا برد. تو 16 سالگی‌قهرمان‌یورو شد. تو 19 سالگی جام جهانی رو برد. این وسط هم بالای 10 تا دوست دختر داشت لاس خشکه میزد. این بشر دیگه از خدا چی میخواد؟ چی روش میشه اصلا…</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/persiana_Soccer/26148" target="_blank">📅 16:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26147">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qX7uFQo1ZBTrj0BJT8X5rvI-IgOdtoaV6Hr6P2Nyg5xiDF7oIVuuLrtclk7c2GHGHkz7lK2Uv-Qj9drKk2uymTpzX0hWW2sl6E_JeqBXYYRVoOy8HUof_9fFZBY4CtL0CnGFMXkawZ1zrawae_rvIlD9ylJ7mUvmmTDNHWv5XLyKWBbp79bDf01-FLicIs0dpFVjfUxBIo3vJa2smkpNfPJFMq2zken7lKJse_un8y-9imbKRlFZUNREWcF4zzZM1Z7vMtlunv_vykWck6yZuR7PHpRYRK9VOa7uVS0sb_SpgIzSFW7sLkWNB-soQWO1d1YlHJd7d7_kyGWDWf94Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آتزوری‌درحال‌شخصیت‌گرفتن؛بعدِانتخاب روبرتو مانچینی‌بعنوان‌سرمربی؛حالا پائولو مالدینی اسطوره میلانی‌ها بعنوان‌مدیرفنی تیم‌ملی‌ایتالیا انتخاب سد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/26147" target="_blank">📅 16:33 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26146">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X6eX1D63Yzj2NHWsx8PFDqO6diGPFkAYWzIwsm4XdYiKazjmth3sA9zW45lNOvRJmlRYWo6ZQNvOaCubxPHEQ-7tZyGRhXZ-s9a9SIuHTEVyyegTN2WkBlDLwgQGnqp61VhTkCA36uDElaPuAk8wfjnH9S0ShzVJDB9fBrI1hlmqJy722kZSNU2FCiz93zN36AuXHZSXb-lPFuPoFN4aYlXyiNYe3ok3Y1HKFHbSaj4WFPh6FTmZ-D1brM8fSruTscBJ_EBZH6RWSp1CvuUfwvX9LpyJRuZKdYb7mmY2R8lM4oVCADAL3z8C9FGygQHdkFvcw3K6OJ67T4iguK9sMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛بامخالفت‌تارتارسرمربی پرسپولیس جدایی محمد عمری وینگر سرخ ها از این‌ تیم منتفی شد. ضمن‌اینکه محمد عمری برای تمدید قراردادش با باشگاه به مدت سه فصل دیگر به توافق کامل رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/26146" target="_blank">📅 16:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26144">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ezu-ih1th5T3y83hWFqPSqrWD66PNyytjAzVDCDdLrgdRPbiHwhwF85nTbWFy-DDv_r_NROl5rWx98Gdgbi_1GUdJNZs5rWFX6fhashxL3AOA1yfQS_Pcwq2f4OSUZdFR9LIxWEMcox-94mf6egCTbo1ig7xLdTmyUf9AI7-_P2cBp85HVGMo9WsSDn-IatMOaOV77wzoc-MC8PQyCLl6VYzA9Df-pv-ozf4obJmkpJ-n_bxc6SbrojtjzcG730qsb1x95yaL8bdgEKn_qHP9aUdidAgbQpWjGFjW3YEF32aqpQmoiuWxmUVFgbA1DsZFyWag6BEy5U0I6-dwwZm7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iy3-TIyKME5fXq_N6s9V7-EgLXXJfLBv5RAJE97s0EPWMxlR8KGD6jSbTKHKFvXO1c1Fm9tLHoaHjkqoLjlFkfSv0hEsjM28B57Tfd_96dw70c6yWO3jYSp54sGX3XPpKnE-1kWhEExzAVmskOEDJA076YGjpSDtQCPMfPqh3kjijofYqHVtCfPhoOCRtBTcsHuL4qhvsaVZIBh_LHx8J7w4jT_fx5fFwIn1w5IJO0s8ZABZY_0ipz_Z4odtuXLwEUA3SyX4kf0Xx86nSL7oTYvLYpjyjzNeXibA1guR0xwvoYUg0NRwuJsBw8vLaQOKywhdSvMfMQDLDrxm3QKhXg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
اسپید، یوتیوبر معروف که بشدت فن کریس رونالدو هست‌ شب‌گذشته حین اجرا در اختتامیه جام جهانی مقابل‌چشم‌ میلیاردها بیننده رو کُتش "فروهر" نماد ایران باستان و آیین زرتشتی داشت و به شدت مورد استقبال ایرانی‌ ها قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/persiana_Soccer/26144" target="_blank">📅 16:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26143">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EfSWo4Pg6MXeq3DY-yHM1vuD8Gxu3mFAlqDm5fZl4exuv7cksv_jX1uxjY-Fs9UvVaD5RR6Bf7Ul78dY1nie6e0kHesWv4ztwuedvgZO67wz4KKP06quYQsqDL7zeoYr8zi3GLH8Ukfs2XR9kOLtY-GQRzzkkzYcL_v1spluZkQ0ex8rsM7aozpyaLkfUHKJpKbUdZV5UcFkM-9qzgKSyWjVH3Lc8WU4RhsE_181Wim3yCUxq1wp8-FyqFW1Mos2wOaARmlo7OhPnZDtw1JjJIoLi8lzKb3L5DpzV6I-C68bz15PkhQ_DzelfLozPs3XmenSokNpt0uRwxfuV8gfXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لئونور ملکه‌آینده‌اسپانیا: بی‌محلی به گاوی؟ من اصلا همچین ادمی رو تومراسم‌دیشب ندیدم. بچه‌ها فوق‌العاده‌بودند و یک‌شب‌استثتایی برای تموم مردم اسپانیا ساختند. نمیخوام راجب گذشته حرف بزنم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/26143" target="_blank">📅 16:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26142">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/afcXrHHHKPR9oRwkIbhzCQ0_KLkd3WOFsHg2sBfTyR-zz4ycSBHJec7saz25o92fgueme0oJ9bEFin7RO43OkS1y6M1u3X40EqddaICIJ9Rk9ZB2BJfYsfehWZPVdQP47i_8o_QeZ_mRbPCMu6P4KFZPrhUU6G1lMo0lfLQHEV9fa4yIZvOQJ0TSTf8sUfZ5mi5H4eT5YBuv7hLbwzELHiOEFUhdjMY5Jcl2_UVrisBfntnDLJQdG4RUF71KXZ2UhaMVZHbhcwqnXJosrVmV1D_WkI2sTrcG8BEMh2xGdVQ4Qm5C2BcT6buGGOQP2VWEOMPdWsGnLnAimNf0zNsR2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لامین یامال ستاره جوان اسپانیا و دوست دخترش همراه با کاپ قهرمانی جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/26142" target="_blank">📅 15:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26141">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I-L-9sjgKp75l_Ww8yt-4Hxy1_N4euOVcPM79irh6-DIR5afaY4icpQqb_zKj1ZC8Q1PMME16KG0do6OcKeoxxFAyC7FxEGMNlhmpYMI2azitz-i1GKY4MLqrHVw-Hl-EpKdkXiIKbR6WG-IFGIUsC0OQ4Ox0qVShzxDwxfWetZMbfN5-k0Cslzxiz4HpmPzUu4yI0JWer5nCv6za2Z0vHzK1DHBeYSG6AG1hH4_VEVd00tb5yGh-q7MfUhe3QADh6zJ79PhEdwryDnMuSO3vVAa0hS0S2giyDLgiEuafOaR-YR0iHucYWtzLY4s_wbxvdND4WaoX8P19w_GuZ_hCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
وحید امیری کاپیتان‌سابق‌تیم پرسپولیس به‌مدیریت.این‌باشگاه اعلام کرده‌که درصورت تاییدیه کادر فنی سرخ پوشان علاقمند است که یک فصل در پرسپولیس بازی کند و در پایان فصل از دنیای فوتبال خداحافظی کند و به کادر فنی سرخ ها اضافه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/26141" target="_blank">📅 15:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26140">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6473e7bf72.mp4?token=NhsRYvIW15wRsHeuunSp0QZxX4aox-X15zYxkzXe0GD6GLQg6lW4s6hJItFTzhV5Gpe2fKdv3DR_KV6zoRZ_INYo_1Isd9LpF6nGKPWRXca-EtXaZ76TPPZrT6wkC4gs4qLakfp7VSp5Wz2dKu2e3uManzarFrmf5PSPMNlLmK4au14uXJt4_QhEXnl_agHgvxQDhIKciCdlb9NqQTfx55Tovf4YialkIHCgUskxX3x3Lfmj_I73E5PPnrIcl_DRGqYEl_E62kj--kNfJq--YGUc4Wacj_HxFzPPt_qwj7MYr57XCmY3jEdjksRkkRp5ZAln958uVDr0PYr6j_E2Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6473e7bf72.mp4?token=NhsRYvIW15wRsHeuunSp0QZxX4aox-X15zYxkzXe0GD6GLQg6lW4s6hJItFTzhV5Gpe2fKdv3DR_KV6zoRZ_INYo_1Isd9LpF6nGKPWRXca-EtXaZ76TPPZrT6wkC4gs4qLakfp7VSp5Wz2dKu2e3uManzarFrmf5PSPMNlLmK4au14uXJt4_QhEXnl_agHgvxQDhIKciCdlb9NqQTfx55Tovf4YialkIHCgUskxX3x3Lfmj_I73E5PPnrIcl_DRGqYEl_E62kj--kNfJq--YGUc4Wacj_HxFzPPt_qwj7MYr57XCmY3jEdjksRkkRp5ZAln958uVDr0PYr6j_E2Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیس فوق سنگین روزبه حصاری بازیگر مطرح سینما به علیرضا بیرانوند
: اینجا ایرانه چاله میدون نیست. با کشتی گرفتن با بزرگ‌تر از خودمون بزرگ نمیشیم با احترام کردن به بزرگ تر، بزرگ میشیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/26140" target="_blank">📅 15:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26139">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hHwY2KksjQODTyZ-JknPdBvspQRM1bX9QLZaNxaE4O6_4Sut92v4kdGIHitX4xk_85qmNi_liMiz27NN_U4xpOA9Qnkw_26jInkDjeM7hsHJqYylD1amPWpdPIpPbHHXGxYOlkc38eVJoT6byAYpulFfApHCEusPRBbKLixFV4PiXAm1g_MVNiQohXwsggQ923uCSsyBuevx7KFSF0um6803x9YUL0sTplVFaTNHFUKW6XO4U4lKJwPNKAcwnBwSBlCGzmsObcEoYgo3xmdpk0GuA7wQBJv8LIB5KuXL_0Gpb-HIAwK5u20X_-eLOkFi4UY5z3x9YwI_39N3J7GUDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
استوری شدید الحن علیرضا بیرانوند علیه علی دایی اسطوره فوتبال ایران: من را با رانتی بازی به جایی نرسیدم که الان بخوام الکی جانب داری کنم. ترفند هات دیگه نرخ نما شده آقای علی دایی!!!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/26139" target="_blank">📅 15:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26138">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sftX0W9nj_Y6fQEZeT9GLtDijRZkt3w0pJcvWDYA7n4MiRJu3DAIwanVNKpgZhSGy0SZe7MD4BcCPaH_-8z2EWCFxWe-ufmRyIib_4Z2RjDgiKmbnf9LCWulFcwlutL7RbzTDO97jQoDXM1ILj-vKmuQTg2mVffB1Qu9yMP0Ort1WFVraQE6zBPsydpt_5tVtoAiVeOKPgTYORDi6Wy0iCW7_0y_drhHY_HkyVKx2mK_aQ0EpYvun6Ynzlbfzq1kuCpJIUPUNb3-x2pDdFXsbwc_ObV9zrzDRud9SgSMZ07ZALz0I5dZ8EcllQ4liD_0Y_IP86jmNnCa1tWdtIKBvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
آرمین سهرابیان مدافع میانی سابق تیم استقلال باعقدقراردادی دو ساله رسما به سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/26138" target="_blank">📅 14:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26137">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gom1r_2UpwmMSlVfe6YTTN485mJj1PQ6o3XkrksXXPyM7A91GLVinAGSBvIDGpguBOToJvewj0rzgGLIPwksuXsFgRdBh_pDaeEMF3jUEBmilUsnr7IY1ueWS6FglkvdjODS2R1_0mYN4xH5aAuCJyb2ZjyyXTZObY4SFyvff3tdredsgpLjrXAvo9QN2ft0nf9fvxmqHFSnTRPIsPln35GRAxTRgTcwejEnskUhvO0DWid4zWz8-TMFj9ci8_M4rsVrSJDs7g0Nm-jfCAkMw-LqHIlP_H_2DWpULGYAKKjD45ur7OsFglzKpfVWPEpYzpT9LpJvAmg4C5WAFfA7bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد...بااعلام مدیربرنامه‌های عارف غلامی و آرمین سهرابیان در ترانسفر مارکت؛ این دو مدافع میانی از جمع آبی پوشان پایتخت رسما جدا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/26137" target="_blank">📅 14:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26136">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">📹
ویدیو کامل ویژه برنامه فینال جام جهانی 2026 شب گذشته عادل فردوسی پور؛ برنامه جذابی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/26136" target="_blank">📅 14:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26135">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nhc-2nUObFah4qg8Cx-O5ufdDoPWby1OKdZXtBuyuTq5oYzbLjPli_AP4k71_5q47OQYhz6R6GEZlopViSxDiO1T2rjfcDrUUYpkpwLQWLhqTDAPW_e_qLee2BursRRrkw3FGNvwXU8CPftHUhZRIVJ8lEN7VxOuHksHxDynYf4tCPBPT0Lr_K8emkoGjyWGD7d0872XaaCBYbZrIAW2ZrlQcfvVYeaDy2wH_TO1reozQEP5AJOAlphkongBYY1KEgTwMlEqahmVWJOI17ZYx5aDLb4ro62wNMUz9f8EJr6Ovkt0eGht8lhUoYNdN9Usk2W3gSNnT27Iynzju_4btQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق شنیده‌های رسانه پرشیانا؛ مدیران هلدینگ خلیج فارس از عملکرد مدیریت‌فعلی باشگاه استقلال به هیچ‌عنوان رضایت ندارد و در هفته پیش تغییرات گسترده‌ای که مدیریت آبی پوشان رخ خواهد داد.
❌
علت نارضایتی هلدینگ بابت هزیته هنگفت برای جذب ستاره های خارجی استقلال در…</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/26135" target="_blank">📅 13:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26134">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N0kf-0HDe5EhSc5JHWnVIOG0YBa-xrIwJse4zIB9M1IS7cqv_Hz-5Cwm5GzdzPqyEgA2pGuoMPRCAjYnqbbzI4HIbHfQkcvnOueaOY3eWHdlXtIZhS1xhZu_ljQWcH-zW4D-Q-0TJO0cRpnDqJJiQI6oYYqKm0toyrM31vZigWoxoL1USSpCPT8I6SRb2CHJgtASxzQ8bhB9zAn2WL7xMBu9l0RTnly53ySvEg9jDKmsvh3S2fh7ekOXcKF4RqR6S5i-bXP3Pu9hzj7oW2kEs8HgR9nPKIyjB5m5HuIwKX66lIc5beCaNbfNXHv7T7va4K4TqExbEZftdmBHBWtCEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
🇪🇸
#فکت؛ مارک کوکوریا مدافع جدید تیم رئال مادرید درمرحله‌حذفی‌جام‌جهانی تا فینال حتی یک‌بار هم دریبل‌ نخورد. یکی از بهترین‌های این جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/26134" target="_blank">📅 13:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26132">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MuuRMA3yaYjHAalDRCR2GYI2auDPnEo0oBBZrXRKmNwnD2xnjDswkFM3RHLbu4S70r4wvZIN4jaKUILMbmAwPHr3xWHWQAqzubQ-X_klI0ZEn5MTgNiDT_kev_VPFwkjHkO6rdFMFYIdFMFrFooDTKy7IHhLq6ho3xJ3Y5WsE_ck8aOKqSagAUOTYmwPSN8aSW6ymI1taS-Y7vIpt9X1VdYslpWrIKEXEKPpXkbMjcOZqMuG-jJgn9ljYMdGXC7vft9RMNt5I6Tg9UscgqElbhJBYVESY8KBEgaD7iOVWzFx7-Xy1K52vItjOvlkzKhV9dvgKRWl99cGfqN9RL8_vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
◽️
🔴
#تکمیلی #اختصاصی_پرشیانا؛ باشگاه نساجی بعد از جلسه امروز با باشگاه پرسپولیس رقم رضایت‌نامه دانیال ایری مدافع تیم خود را از 190 به 150 میلیاردتومان‌کاهش داده و72ساعت به‌ مدیران پرسپولیس فرصت‌داده تااین‌رقم روپرداخت کنند در غیر این صورت توافقات طرفین بهم…</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/26132" target="_blank">📅 12:57 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26131">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vLLxjvGyMkRdnivswxyzAnqg1uyWlrZfGsYgF77ryU9voIt_GRund1VVdmXju5NNxYwHeTRZq_T5QaH9Z2-9QdsSlkFn2xtQMB7kPOsfMe351chvT3WzGBYf3-AHXXmPrAWXd1c3A44i9mixsGj26Vp1RutTzMauemj2SfEvKWKNtgeDtBie4RcfA05KC1EkxHycZmZ80d9zMvGOHH3pE_3MjbJYwq2MNNOoFynDJm2Ep7ZbiPUo_xqKRrZpobbcft1O_pUw8RXPGYqpVEvtOuxCn8DhwYZkxjMj7QrxlIVkLbT1J40Nt3ZHKo9dDZ28FTIeo4YYWbWdUaI3A9mBVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برگاتون بریزه؛ میثاقی روی آنتن زنده شبکه سه خیلی‌جدی‌گفته آه مردم غزه  ایران تیم ملی آرژانتین روگرفت و باعث شد که این تیم قهرمان جام جهانی نشه. بعد همین شخص اون شب در گفتگو با گلر تیم قلعه‌نویی‌میگفت این چه‌حرفیه‌که میگن کارما مردم باعث شد که تیم‌ملی‌ایران…</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/26131" target="_blank">📅 11:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26130">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cq-nnpX2DK73LF7ma43g1jcYmem_MUf_VV0rlyJ-z1PEtitxCUk9ls4PJheYUi-6PCnKp3UtP7svbSobbop8OXW29rBUeAF3Jn6IpPGrbxH4dBHdrnaaEm8OgYk9mPiOTzvrlTt_55de0wDDfK29K6e7yT7xcAeQmU3Mcl8IzgS-iflOjVzd8A3o5lL-fcFFc2JT2ZfBxt0Z3udB_OHjBF57CuyabnKYgLI0jVMVpvip-gjM38CmQ7PWZ8PmfNR7hKTtzGzV05324sII1L54kfCQygKnS0RWoQtaf4Rlvdyh3XGifpsFGnVOKx52_11glF28Y7io4YaTw1AkhvahMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برگاتون بریزه؛ میثاقی روی آنتن زنده شبکه سه خیلی‌جدی‌گفته آه مردم غزه  ایران تیم ملی آرژانتین روگرفت و باعث شد که این تیم قهرمان جام جهانی نشه. بعد همین شخص اون شب در گفتگو با گلر تیم قلعه‌نویی‌میگفت این چه‌حرفیه‌که میگن کارما مردم باعث شد که تیم‌ملی‌ایران…</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/26130" target="_blank">📅 11:33 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26129">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m5Jc5h-gSojuzb9ivJPzvhaDXEs2tCuJWiI4Ifv5vLzxk2YJq0kOKWtWyKeTFYQpX5aCpsCU2pLls9QMCl1FFOpm3bfUk_czLi_o7plukLbwI12Ptxs2rCkP5nwGRGBHy7Um_aOGxlfMmR6SQ-f8T0v4xeOG15uq1eRRqidQflJIyAAu9LS6VEeB-EI8zKrTGFcYjTms8JxOanubn5MedZWvKSyXwBvu_nUQssVp2FBue7iEHpMvGaZOkXLIIZ0c1uEQIezXWwXXYlainoZHERPjYpUajoA3ckNbFBiWOt0GuAlTp9dSEcWHJfLGDZZBoosO-KqunVv8mctANPznEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇪🇸
#فوری؛ باشگاه پاری‌ سن ژرمن بزودی قرار دادی چهار ساله به فران تورس اسپانیایی تا تابستان 2030امضاخواهد‌کرد. تورس به مدیران‌بارسا اعلام کرده که‌دیگر‌علاقه‌ای به موندن دراین باشگاه ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/26129" target="_blank">📅 11:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26128">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/202f77d369.mp4?token=mNivYloZQ7LMgtjUxGCSEM6GEL57o51OlpYUQfRLlagDUZ7NtK9YQkmfulLVamMSb-KOBo1-AVxbUIvaV4rlFIu4bPg31cREUstyv8OSea1WTZ1_oJ2DqLFNdmPA5gx5wjTKuvetRpragiWw-Jw4di_j6yYux5xMuVddRhMReWCzF9aoN7oJMiWpeEfonStoAhOzL5dQ0EQFphNd7-15yxlFtUqHQbWN8kBmjSqtt9IfglT_OsREW3fAf5q_cFdq8GIkShwAVG0noByKerzBZow-eLuIwZQUnpSfafkW_oYP-PG2LQeichhllyvWBZPURugKCeEDBzRNTI2GV1Ul2qle8s4IUz0YV0m010xeigYoRFoL6FSnVKJ7ArEdvcDWMByI6etvhOx0qKihIv6LlvsXB4TlL3Jh9oc4TWPP0XtMTezBHRQZH5HvX6wAKquO4z-rW2Qm-aFD_jEWlpjqVpUFWrDLGgsVjJgKHIqWMt0bWsG311eVcqP3kyx3OI6LlLNEAd70dCPbjpYn0MtfUdD7WqEMOVvAaR3hTwaxnKC5c4wPQz8N6VNZ3Od26JOSHYEkVTAc_lrtgU-sfUvIz6cDnLVy6o9DPS9OoPznOWqxP9MWAjQoEeihIXHFhHBwJhZxMAv7kausqWGfxB-7ffUNwhVeL-k-ivvQnuTVIVE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/202f77d369.mp4?token=mNivYloZQ7LMgtjUxGCSEM6GEL57o51OlpYUQfRLlagDUZ7NtK9YQkmfulLVamMSb-KOBo1-AVxbUIvaV4rlFIu4bPg31cREUstyv8OSea1WTZ1_oJ2DqLFNdmPA5gx5wjTKuvetRpragiWw-Jw4di_j6yYux5xMuVddRhMReWCzF9aoN7oJMiWpeEfonStoAhOzL5dQ0EQFphNd7-15yxlFtUqHQbWN8kBmjSqtt9IfglT_OsREW3fAf5q_cFdq8GIkShwAVG0noByKerzBZow-eLuIwZQUnpSfafkW_oYP-PG2LQeichhllyvWBZPURugKCeEDBzRNTI2GV1Ul2qle8s4IUz0YV0m010xeigYoRFoL6FSnVKJ7ArEdvcDWMByI6etvhOx0qKihIv6LlvsXB4TlL3Jh9oc4TWPP0XtMTezBHRQZH5HvX6wAKquO4z-rW2Qm-aFD_jEWlpjqVpUFWrDLGgsVjJgKHIqWMt0bWsG311eVcqP3kyx3OI6LlLNEAd70dCPbjpYn0MtfUdD7WqEMOVvAaR3hTwaxnKC5c4wPQz8N6VNZ3Od26JOSHYEkVTAc_lrtgU-sfUvIz6cDnLVy6o9DPS9OoPznOWqxP9MWAjQoEeihIXHFhHBwJhZxMAv7kausqWGfxB-7ffUNwhVeL-k-ivvQnuTVIVE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
گاوی در جشن قهرمانی خواست لئونور دختر پادشاه اسپانیا روبغل‌کنه‌که لئونور پسش زد و نذاشت بهش نزدیک بشه تا به‌نوعی انتقام گرفته باشه. لئونور در عوضش با پدری برخورد خیلی گرمی داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/26128" target="_blank">📅 11:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26127">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MjvHc9XjCJ3Z86ikbbGYcnQkeiF0kobQ8zsuk7_tNR2QXy3aI4bDfqGfsKX7xsudD2NuqZDrhAcFeJM2bWIJriHwcsefR3bKiwxWNgQ5aODCvtNBp0-3O6S_ub27rtFyDEMNPH4d0KnPfmwetYMvPqzU55dU1V8pi28d8P-zDjc7PwCLOvUIF0NUzYnY4tXkmHBjEtCz8_KOrsYvpLlHwS92GoIMqUma5MTulG_3ruTq4hPuOZV7GUZFqQkyIV7l-6FE0ijPkTZd85Wl2smWaDxTm5BDJ6EbfrENqGai-lQpJkd9JW3flmNDwX1xzot1tg8wIvkU6ls6FPJnc3hGqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
طبق اخبار دریافتی پرشیانا
؛ رضا شکاری وینگر فصل گذشته پرسپولیس دو پیشنهاد از لیگ ستارگان قطر و سوپرلیگ‌بلژیک‌دریافت کرده و به احتمال زیاد درصورت‌توافق‌راهی یکی از این دو لیگ خواهد شد.
‼️
پیش‌تر در روزهای‌اخیررسانه‌ها مدعی شده بودند که شکاری قصد داره به باشگاه استقلال بپیونده اما پیگیری‌ها نشان داد هیچ مذاکره‌ای انجام نشده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/26127" target="_blank">📅 10:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26126">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27dd0a5169.mp4?token=idW8rejfOV-O0xOY5DtLWQJsHsgcrCXKeAu5sTIVvNb2yp1Wvd21kv39GPSghEgLRY8OUZMkdrthkGkfkQFRLCG02JNz_bFAfsmBeTx85569uZZCMv31qYeActNVqVYWpblpZA0NaS2nOtNNmiLJ1WbXACrJ2PDAL6ayPQZTXezBNjnxucc8XiqQxaKlPaasi0E68bMXju74S-NviYv22r5CAZcvkcVtJMTXuiv7r6ZFCi8kUaKnwg8CSKz-2WfYtceZHrYLiE56UiYuJKdJX6GBH4uoqiktCILKuusetIyIdunndXDR_F3UwEAsI7dfwxhR20QPW3-b855BR64t3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27dd0a5169.mp4?token=idW8rejfOV-O0xOY5DtLWQJsHsgcrCXKeAu5sTIVvNb2yp1Wvd21kv39GPSghEgLRY8OUZMkdrthkGkfkQFRLCG02JNz_bFAfsmBeTx85569uZZCMv31qYeActNVqVYWpblpZA0NaS2nOtNNmiLJ1WbXACrJ2PDAL6ayPQZTXezBNjnxucc8XiqQxaKlPaasi0E68bMXju74S-NviYv22r5CAZcvkcVtJMTXuiv7r6ZFCi8kUaKnwg8CSKz-2WfYtceZHrYLiE56UiYuJKdJX6GBH4uoqiktCILKuusetIyIdunndXDR_F3UwEAsI7dfwxhR20QPW3-b855BR64t3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🩵
آپدیت جدید تلگرام دیشب اومد؛
چند تا قابلیت جدید بااستفاده‌از هوش‌مصنوعی اومده. چندتا عکس رو میتونید مثل اینستگرام پست کنید تو یک پست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/26126" target="_blank">📅 10:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26125">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6a101f8f4.mp4?token=oBNmELigDh2gurrC0hnt4URDK9gfomUCXz9sBUUNC24UuToxA1Sy5167zj0ex6I_RFaCfL66Z9ID-Wt2KOJYj-ZUPyYX7AdvRybxIcU_izFs8jYYkoK0H6IOMdx-3c5o1r34X05xLXyo0VkyxvOMC3-fDFAi7ixwUplF2MDJjECC7lg6oqInprsJFih0X5LhluuguGnK2D1sKR3jG44R8rypFFKGRvFDXqk_j7pQE1hfSp_kYoD9qBA0T9_X9yvIUxxVpslNc2u4JKNySkLQZduFAF31NksYcxOBq1CreD6s9hkh36E-DSqRVm-pZs2m9rZow3ZdOr04og5lLrWCdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6a101f8f4.mp4?token=oBNmELigDh2gurrC0hnt4URDK9gfomUCXz9sBUUNC24UuToxA1Sy5167zj0ex6I_RFaCfL66Z9ID-Wt2KOJYj-ZUPyYX7AdvRybxIcU_izFs8jYYkoK0H6IOMdx-3c5o1r34X05xLXyo0VkyxvOMC3-fDFAi7ixwUplF2MDJjECC7lg6oqInprsJFih0X5LhluuguGnK2D1sKR3jG44R8rypFFKGRvFDXqk_j7pQE1hfSp_kYoD9qBA0T9_X9yvIUxxVpslNc2u4JKNySkLQZduFAF31NksYcxOBq1CreD6s9hkh36E-DSqRVm-pZs2m9rZow3ZdOr04og5lLrWCdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
گاوی در جشن قهرمانی خواست لئونور دختر پادشاه اسپانیا روبغل‌کنه‌که لئونور پسش زد و نذاشت بهش نزدیک بشه تا به‌نوعی انتقام گرفته باشه. لئونور در عوضش با پدری برخورد خیلی گرمی داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/26125" target="_blank">📅 10:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26124">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1235d344e.mp4?token=ZDkREQzfOodkyZuuwa1n4Oag4KhDNxH1wq-uN_QIaHxYLegtxiG989EtHqWs0mimbhzVZ_gyg2zbgkPiTTMU3bekF0wn0v4nZmSFtpeBvEUUaYZFoKCgQMe9mvEyoGkCPELhxHwwkkNnD1CJeHZFYZtkdTrsMHucq-pGXlYN6MFBj4kaloIGqyCOhd7cPuvvwTrnIKNoO1wjJpNaj0rpVk4kPY6b6m2JWFPL3E3wE_97tv7LEam1y9zuJPYm8yA0L7KlMrwrOSPBrqSuC0IOMLVVChf1bbpkrHH3CedMJYjGKAVsr9MlUFeX5rbTeX8Gj0TvLBh05gckTYYuy2psnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1235d344e.mp4?token=ZDkREQzfOodkyZuuwa1n4Oag4KhDNxH1wq-uN_QIaHxYLegtxiG989EtHqWs0mimbhzVZ_gyg2zbgkPiTTMU3bekF0wn0v4nZmSFtpeBvEUUaYZFoKCgQMe9mvEyoGkCPELhxHwwkkNnD1CJeHZFYZtkdTrsMHucq-pGXlYN6MFBj4kaloIGqyCOhd7cPuvvwTrnIKNoO1wjJpNaj0rpVk4kPY6b6m2JWFPL3E3wE_97tv7LEam1y9zuJPYm8yA0L7KlMrwrOSPBrqSuC0IOMLVVChf1bbpkrHH3CedMJYjGKAVsr9MlUFeX5rbTeX8Gj0TvLBh05gckTYYuy2psnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دونالد ترامپ‌موقعی‌که‌کاپ‌رومیخواستن ببرن بالا ازپیش بازیکن‌هانمیرفت‌ بره‌ کنار؛ رئیسفیفا اینفانتینو دست ترامپ رو گرفت جدا شه از بازیکن‌ها، جدا نشد وایستاد تاکاپ ببرن بالا؛ فِش فِشه ها اتیش بازی بالای استادیوم چرا آبی بود. قرمزنبود! ازقبل بازی چرا آبی تدارک دیدن!؟ فکر میکردن تیم ملی آرژانتین میبره!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/26124" target="_blank">📅 10:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26122">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z4kM7u7gwLzmwt5Feekunbw3ug4zfpR8ZawJT1-JSgmbLRgZT8yp-wf-bonE22S45iX9Joi_lcy3A79I3Rj7ciJFj1hCg7OagLiER0fxetJyWXwm1gilGoLcRHhKeGBecmfcJl6BEYl9zDB-8xk_rM1XxdkSsLoQRQVZ6g8INkYGnpeOdtiKqhRddJjJIWKj2zSgfytj57nTy5hSPQKwUVbst8SJVZ1XL9d114wBs23a72zPLJzIe2aaUMtk0aBM-9FRwFnogxGl3QzHzt4JUTpMTwhJRGn-rgJndfFB8kcZ-m76Uz6tKJgnSpEN8TbKNF0rr3H1tF8Mm5Ves81vLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mZWBOovLgs8m5HR9PZDle0QeG2Akn8fe4VVj5kBDPPJDuE-fgzlzjgXMApkF3fTMN7jzmZ-BmOUdc8L2OZzhQT5nmkQBv6N9vF8ZeyDDLdWgSrnJhZmF0lLrtAYg8q1r9sl5SC_rTcBOwJKiFkhc_GU8Kk0fGITBxS-Nre6BldZBsPdlWoUL22rnsGFmAPE3pXQnN27XOS56NQVj9R4xy3aDK53SBTnR13sUzTWNEKIjT7A94A1Vu7_yL7IQlXUWM2l_vY5QGq8LomfWCiGot41mU_J2UukyO00zykd3GuOJqOW_iPfRCy0iAO8enYO5xk_vF0Jv7a_I5tGu3pFH8g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇪🇸
گاوی در جشن قهرمانی خواست لئونور دختر پادشاه اسپانیا روبغل‌کنه‌که لئونور پسش زد و نذاشت بهش نزدیک بشه تا به‌نوعی انتقام گرفته باشه. لئونور در عوضش با پدری برخورد خیلی گرمی داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/26122" target="_blank">📅 10:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26121">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c071bd0be.mp4?token=HFkFndpHetNCkD6sEWxeyUMTW4WI-edBxArPRFA19Az2RBpO_ouZyx6U1QJGkTWR3SMbUjXpWLN4lGGdfL0WBjyS4Lgz1gePVNECtRIY_kt2h1lLQ7VQOsFXx867wmtJ1gCmqIU-JOM7oPVqWSoPKCLaPtShVpL7BH3mxEd41irVLKxZlP7Hbp-SPb1TkPFPNShm-NyTjnosWPvi-x1OG-2eHN-lmceSt8LV7OrMRvarL2JadQHvsIz7fGfC-A231I76Fj9oGWMO9fgMbXxC01mmn5DHGzcvj7XI9MuHh3ryIqz1p-KGkSGvDfTiaMuaG8aA-gXI_c0Ycb3OmGr4lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c071bd0be.mp4?token=HFkFndpHetNCkD6sEWxeyUMTW4WI-edBxArPRFA19Az2RBpO_ouZyx6U1QJGkTWR3SMbUjXpWLN4lGGdfL0WBjyS4Lgz1gePVNECtRIY_kt2h1lLQ7VQOsFXx867wmtJ1gCmqIU-JOM7oPVqWSoPKCLaPtShVpL7BH3mxEd41irVLKxZlP7Hbp-SPb1TkPFPNShm-NyTjnosWPvi-x1OG-2eHN-lmceSt8LV7OrMRvarL2JadQHvsIz7fGfC-A231I76Fj9oGWMO9fgMbXxC01mmn5DHGzcvj7XI9MuHh3ryIqz1p-KGkSGvDfTiaMuaG8aA-gXI_c0Ycb3OmGr4lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حماسه‌جدید خیابانی دربرنامه زنده؛ خداحافظی اوس جواد با مسی و میراث مارادونا با شعر مدونا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/26121" target="_blank">📅 10:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26120">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec0657aa93.mp4?token=JTs6vRjyjHrlCaN1no4TPCsSj5lHHjmI9rSdF23YK_bSOUMeeQGuHHn5PP4HsWqrDpke1hxpx52WJlWPQdmZrRzn_Q4hmSomfsZgm85tDqjyNtaGzFgB1PfcWy3YHYzlmFl3Hv-je6es25OfSI6Pquj7ywfo9no_UbKyTNgYRwtiIfdiMt9GupwUHqsxN6E5kP0A694wsOFfx5EB2KVz7zdBTEQHSLLPv4KSlhZna4RJgobgj8IU7z3kQt_Qp9wpHm__Lfm_AYHg98yF5Mfbn0TkkHHyREfmcShso4-JrXy51Quw_R0y9LAkpDJDOMLtw3-UMWDh2BAflDdcLQMbsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec0657aa93.mp4?token=JTs6vRjyjHrlCaN1no4TPCsSj5lHHjmI9rSdF23YK_bSOUMeeQGuHHn5PP4HsWqrDpke1hxpx52WJlWPQdmZrRzn_Q4hmSomfsZgm85tDqjyNtaGzFgB1PfcWy3YHYzlmFl3Hv-je6es25OfSI6Pquj7ywfo9no_UbKyTNgYRwtiIfdiMt9GupwUHqsxN6E5kP0A694wsOFfx5EB2KVz7zdBTEQHSLLPv4KSlhZna4RJgobgj8IU7z3kQt_Qp9wpHm__Lfm_AYHg98yF5Mfbn0TkkHHyREfmcShso4-JrXy51Quw_R0y9LAkpDJDOMLtw3-UMWDh2BAflDdcLQMbsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
#تکمیلی؛ اینجا دیگه عادل آن‌فایر میشه و خطاب به قلعه نویی میگه من تو جنگ‌های این یک سال اخیر ازتهران‌تکون‌نخوردم ولی‌تویی‌که خودت هرسری فرار میکردی تو ویلات‌نیا ازاین‌حرفای‌عجیب‌وغریب بزن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26120" target="_blank">📅 03:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26119">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aa1c44954.mp4?token=OHpciiw9Sc5PEkmjwmE2qt0uQ84ino1h-o4rPBaBRRe5EjOlkf1lA0_axYnyhYtPK7Rc4cq6hSEmK0Twny3tKVsM7eQBvCr7D1ZjPWiZ-gJKFhzpe2tKNA_DN7Bb2TyuK2KKzGPNkylWvVDMNXVYaTBOBm6mnhf8Cr6CU862vZSU4Y8SGvZk1rCX-Cq-aZ41Kq9LygujXv56Ar4onUKKdMAs1gES4zNkaceUUgbC6eyl6LaoV1HDIQTmCDdd3hVbeu_VCIHUOCi1YzBG8qXLCrcRXXaFr5USNlWyusyfKrkqYcywN30IUbVnhL6zVASut9X_Eph3qk8CRypX9lEv-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aa1c44954.mp4?token=OHpciiw9Sc5PEkmjwmE2qt0uQ84ino1h-o4rPBaBRRe5EjOlkf1lA0_axYnyhYtPK7Rc4cq6hSEmK0Twny3tKVsM7eQBvCr7D1ZjPWiZ-gJKFhzpe2tKNA_DN7Bb2TyuK2KKzGPNkylWvVDMNXVYaTBOBm6mnhf8Cr6CU862vZSU4Y8SGvZk1rCX-Cq-aZ41Kq9LygujXv56Ar4onUKKdMAs1gES4zNkaceUUgbC6eyl6LaoV1HDIQTmCDdd3hVbeu_VCIHUOCi1YzBG8qXLCrcRXXaFr5USNlWyusyfKrkqYcywN30IUbVnhL6zVASut9X_Eph3qk8CRypX9lEv-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
جملات‌زیبای عادل‌فردوسی‌پور برای لیونل مسی فوق ستاره آرژانتینی‌فوتبال‌دنیا در پایان جام‌جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/26119" target="_blank">📅 03:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26118">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55d171bce1.mp4?token=c8I3kpcHEmwARHJaielbosDNSWex5KyzCQEpbmXZyq1-4o7W4jvlU2SSfr0jmkJF3RF3Hfm6PPUrNve79Z0gAuM3AKNuo38mWBE3llkgbEGvICCLqsHryIpVr9lZeZJdlcV3weTw92_ElbnFH7KVPP2To1KC4w4_qw6Z3hT4D18Zq3syPKJduItUen0eS7qF13mdzxvq9T6Db-8t8wCuokLKElfRPKzLBkXuCqlAjXNSIAxqOoXx-r-fWjM1m0eLiHqQSHUUS1vewUOaCt_-XTi2gmervniN2MmD6kAjiIIZsHZ-eqFkg_H1ICqt68l4CUeqoWE4841YqpP7R6cAsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55d171bce1.mp4?token=c8I3kpcHEmwARHJaielbosDNSWex5KyzCQEpbmXZyq1-4o7W4jvlU2SSfr0jmkJF3RF3Hfm6PPUrNve79Z0gAuM3AKNuo38mWBE3llkgbEGvICCLqsHryIpVr9lZeZJdlcV3weTw92_ElbnFH7KVPP2To1KC4w4_qw6Z3hT4D18Zq3syPKJduItUen0eS7qF13mdzxvq9T6Db-8t8wCuokLKElfRPKzLBkXuCqlAjXNSIAxqOoXx-r-fWjM1m0eLiHqQSHUUS1vewUOaCt_-XTi2gmervniN2MmD6kAjiIIZsHZ-eqFkg_H1ICqt68l4CUeqoWE4841YqpP7R6cAsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
این هم برای هواداران لیونل‌مسی؛ مسیِ ۳۹ساله اگر نبود آرژانتین‌حتی‌از گروهشم صعود نمیکرد اما او یک‌تنه تیمش رو تافینال‌جهان برد و تهش به هم‌تیمیای خودش باخت. توخودت‌رو قبلا بارها ثابت کرده بودی لئو ممنونیم ازت که حتی در آخرین نمایشت هم درخشان بودی و مثل همیشه…</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/26118" target="_blank">📅 02:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26117">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b94e4b0c7b.mp4?token=uCyJ7BmWWsX5hZH5tdFKX-PbUiQm4l7gC6swhOJLEBrbP1m4580WJya--0YV7vZEuMLq8mxQry8rslo7opmuJCq658JzjuYVEIRl4hTg-i1r4BhcRD-XfMdke-JTCD1xiCWotrjpd5S6jk-XyyplHbCycIZvTZ5ohvrH2ZZjIQUHozzDjSUFrsMfzggA6yutvXNuugd7LIt4WL3m4s08FCmnIwgbFtNj6ZZIwDTAj2-RpwZC5g6W0uTV69AW9WDJhmltdZlfgGAe8rrLBfev-BvZ4bHpR4LNn1vB8H_F_VK2F6_w9qBbJiUIHzTJ-AmgaXgYP6ZLhRwJR-02PnnOtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b94e4b0c7b.mp4?token=uCyJ7BmWWsX5hZH5tdFKX-PbUiQm4l7gC6swhOJLEBrbP1m4580WJya--0YV7vZEuMLq8mxQry8rslo7opmuJCq658JzjuYVEIRl4hTg-i1r4BhcRD-XfMdke-JTCD1xiCWotrjpd5S6jk-XyyplHbCycIZvTZ5ohvrH2ZZjIQUHozzDjSUFrsMfzggA6yutvXNuugd7LIt4WL3m4s08FCmnIwgbFtNj6ZZIwDTAj2-RpwZC5g6W0uTV69AW9WDJhmltdZlfgGAe8rrLBfev-BvZ4bHpR4LNn1vB8H_F_VK2F6_w9qBbJiUIHzTJ-AmgaXgYP6ZLhRwJR-02PnnOtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
نسل‌جدیدعلاقمندان‌به‌فوتبال:اینادقیقاکی بودن که بازی اسپانیا
🆚
آرژانتین روداشتن نگاه میکردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/26117" target="_blank">📅 02:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26116">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e72188ac69.mp4?token=AiCQpD9FZX36_J5aOv0I6uokIbo0IH8lA9VWGr57dwKuljJ4hgZv_VFZPYcX9j3WzKmj6FLuR_xqMPYQBNahY63OFxUH0LffxNqXj30TI5vIwOXnmDcGsXc8rYHQ9vMwIJxMpSDbeImskgipSUxMtQXnIOkg8z8SLIy5-4hdGe1CXYcXbSKZxWmid7fhnhQPcuhorTh9wRXlOFVTf7nDd5Li_ingGeEEqE7YsrJ2tbYkeFB4r_vh4c6fX75I-Hk7VusbGPPlNPXQjBvvcOEdFTH49uqxxPCiM_CExj2CtQIhHvXO2UO_HF9CRp04E2FYUDUNDZEE0rrubGGg8GnZow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e72188ac69.mp4?token=AiCQpD9FZX36_J5aOv0I6uokIbo0IH8lA9VWGr57dwKuljJ4hgZv_VFZPYcX9j3WzKmj6FLuR_xqMPYQBNahY63OFxUH0LffxNqXj30TI5vIwOXnmDcGsXc8rYHQ9vMwIJxMpSDbeImskgipSUxMtQXnIOkg8z8SLIy5-4hdGe1CXYcXbSKZxWmid7fhnhQPcuhorTh9wRXlOFVTf7nDd5Li_ingGeEEqE7YsrJ2tbYkeFB4r_vh4c6fX75I-Hk7VusbGPPlNPXQjBvvcOEdFTH49uqxxPCiM_CExj2CtQIhHvXO2UO_HF9CRp04E2FYUDUNDZEE0rrubGGg8GnZow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
نسل‌جدیدعلاقمندان‌به‌فوتبال:
اینادقیقاکی بودن که بازی اسپانیا
🆚
آرژانتین روداشتن نگاه میکردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/26116" target="_blank">📅 02:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26114">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CAoo9uBqNaqLx9VUqo0Nb70LmZastsJmbh9M9Z996qxhm-nkrJ_OyGXXzkZ8h3uskSUaUkH8c11u-2wRm28tPsSomTj8sYRk20k_hRs61oA5FTW8PMp4WSrJdNGJ9FVn457YeAqgTJKBKdK_BFlljZjeOl_z5fj9dfpSdjPdeVgbAgayhPptoPboTVqVOyqeCuKFASH1z6V3SouiJj-5hYSDxGXFDvqgvtGFXYupZAkX-HGC1D2ZXxi7GqRA1anYgwkNryHysNiRO3EbdxfoaGuIs120Oat5VRVEkR7hdqyyT5tpe0SEpHtSVtBCZtE3ShAhN7msJ_8unDydTNJ2PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یادی کنیم از دست دادن فرصت طلایی توسط گاوی؛ سه سال پیش شاهزاده اسپانیا لئونور ۱۷ ساله به بازیکن جوان‌تیم‌بارسلونا «گاوی» علاقه‌مند شد به طوری‌که همه عکس‌های گاوی رو داخل پیج اینستا و توییتر خودش پست‌کرد و ابراز علاقه نشون داد؛ بعد مدت‌ها به گاوی پیشنهادداد…</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/26114" target="_blank">📅 02:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26113">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ecq9xazHxMp0MSnF6diVx5G5VREt8r9PTCsX3z7dEob5qRqfNFEwOgx9gxWqjNSNlkaAj0Fhf6AVj-kGFo6y7oQ7V46UCJtZXsyEBnBgIiOti__mHre8LTOKiNVA4tubbkfkFZ4j2Hy6YXP8vKQ8nP1L_4E1OrV-vldVVsNlsi18C1lPyoFOSudrzRvDiy5jwaODON2DHqTpxvz1XeRWcurCbzrh0BTZmWAPO8BltBD2fZpIyWij0TzKN7xi_ubZodTVIoV7Mal6VrRia6ZQcyNs0Qt1GTkt-kihRFMWQOqmDRuQaYX_Xabwkn_0BP32zHFMdSwbibD_1bexQA-HkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
این هم برای هواداران لیونل‌مسی؛ مسیِ ۳۹ساله اگر نبود آرژانتین‌حتی‌از گروهشم صعود نمیکرد اما او یک‌تنه تیمش رو تافینال‌جهان برد و تهش به هم‌تیمیای خودش باخت. توخودت‌رو قبلا بارها ثابت کرده بودی لئو ممنونیم ازت که حتی در آخرین نمایشت هم درخشان بودی و مثل همیشه…</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/26113" target="_blank">📅 02:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26112">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QegqSPLfRUYWXOoZCrX-oopwUwp4nynwNcTvJd3bjOT9UtnG1GVmmE3EK_SN1rv7MVmBVUWhZFgzQhcEhkmavQ02SQUAM2Rdcg9JGZ6R38IDe6VKKvVwDqJE_c5tdLOszuAzEeKtagKd0t_CP0lMs04kPqyPALsbTI41xNQWeoFpvSoReHsAF5UnJZZ7sCawg4jDDQy4WpkB-kR217J2Ug7Db2sd1bsmmyk-Mjwh1InJUdJdtkzXxWzPyBXlc9Igo7UQ2dGkqPEtuzNqHmQ_nOtgkdbMyuZyS_TUCY4O2O_SwT3fAFo-O4Q6_PS4ZTTu8RozffMr0bw22Njjv5jfcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#فکت؛باحذف انگلیس،ایران، اسپانیا و آرژانتین تنها تیم‌های شکست‌ناپذیرجام‌جهانی هستند! اسپانیا و آرژانتین بدبخت باید تا آخرین نفس برای قهرمانی بجنگند، اما ایران؟! ایران یک مأموریت مهم‌تر دارد؛ حفظ رکورد شکست‌ ناپذیری! دو تیم برای بالا بردن جام‌جهانی میدوند…</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/26112" target="_blank">📅 02:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26111">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nsSAWW4rYDKJ91R8H5TGLCbdn1o523pYNh5EKzx-SA81XOUR3KLLof85asdd6QbG63bgZHVbIwIxB0XFGz5U7C8sKO7gPs_BgRTkmFlLfYGYtJlcSYNl28Q7y30SRagszSdzysuAfLYfgq8FE41t82SqOma3SnJRYwxBJPsSULtcMR51c950OieX_25tsLuAapmPiGZ7PN0MHc_PV_s2XIOkTTttYabr2TkbsWNjU92lqfkNfz75WdwcmQR33HwgGRx4cB_kc4mOJOhb7I5SHnCxCAJcn8KpsS23DjwOv2HTSfgFVG6_vtzzGoP3Qso4gjjWY1z2cKe9wxcQ5gYRgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
با عدم گلزنی لیونل مسی در فینال؛ کیلیان امباپه با 10 گل‌زده آقای گل‌ جام‌جهانی 2026 شد. همچنین امباپه با 22 گل‌زده‌لقب‌بهترین گلزن‌تاریخ رقابت های جام جهانی رو دوره بعدی مسابقات از آن خود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/26111" target="_blank">📅 02:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26110">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TeN7jDP6QwqmqzbNMpenDUFdm656C7ShRtXMvAUX_5MXZ57xt2T5NELVgOcf6L6QQINY1UPqFLzW6VhgaCdXqJpJl1j0HZniOyHf2lmQMwMcVuhpSoZXAo3Fh5jem7r-9q8Hbi62HcH4NAEuaLq3fjYadMKBTzrmjMEb7fzcOB-3UK-lYidMMVJiIzWP_mWJ0fihLRc1MdZArP3_ZUDFv15sbOxyRcDgFXgcQhy-1lq_KQYrMCls384MN1ZE4wy_wbr_KDL-u8_U113rhEAkQY_6PewFsvG9fz9XJo-BROdJ_zjfmZE2Ez05kTxch25k08qCxHutYrDU8h2ZYm3AOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدار های‌ دیروز؛
پایان جام‌جهانی 2026 باقهرمانی اسپانیایی‌ها و گل نجات‌بخش فران تورس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/26110" target="_blank">📅 01:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26109">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LaMFK6NwvMxhwxoep--XLZmYNv7Ta1jJSQBuVTO1wyCx41S9UuPQxBeERMms95XS__ZM6CZra0u8wDwI-gNrCKeTgP3ngbhDSID2BiDhtrnM902VB8h-5yrckGa5XyaIdW9E_WydLgx3zIIDlE3rU_JSmxkAxKrmrQEmGKH4OYbQN1Wfy5AsnuuegEcS3vHylBAXTS8AI3GBeDX1k0w9VI_iOC-hiSAXRjRYKNfrm9faVNKC2sBM_9tVFpM4q9vhKsf93PkjRW33OQwQYtxU6Ke7QIyvFjOEDi6EO6vlJckHvt3N50xaGYhJMCDYo3R1Q5Wul5i7Ga5m66X9XxB-xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آرژانتین وقتی فینال رو به‌اسپانیایی‌ها باخت که دریک رپر کانادایی روبرد آرژانتین شرط بسته بود. او در این جام جهانی روی هم 10 میلیون دلار باخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/26109" target="_blank">📅 01:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26108">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p6ejL9ypnKU37-jlqCvKqdTUSf8cUZ1ZTM0TudnzvMdktn_QcdNJMbxNrAAgtiT-uJVYwb9wiquWfanu5jEo7Stiyl0Gob-96clIbuJKybuotrjywyTQUl9ZKqyJCzmJyO_zHsexw5Qgnm5tAxnHIgh8uLimUhtNeLlbV17yCxi3nCfKoAwg9G4-GnlpKZiL9G8TJQu1oAFw48JR2bfK_kjzlkGZyx-E-NurTGw7dUqRe7OEutCNAj2xxyyJMDYKx6C-zXZlsZ3MIvEwl22xi4R7ubnZdlDtglPmP2RZwVN9ay_cWIsVLS2a5SDDiQ1x16lM-BmX3423JJKxjB835Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آقا یکم جمع و جور تر بشینید بلینگهام هم اومد:) فینال هم یه ستاره دیگه به این قاب اضافه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/26108" target="_blank">📅 01:49 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26106">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q7qU8D22U0p0vw0tqIQscbvG77wYHqxxHOsFdEpe67tf31-tN0Y00TspL0bGlvRF3fipbLux-BjEY4edVz6it5DFLDSkGLGIPEuplqwXTYG5x1RcyLJKB4k5dC_qlAdhZLlGxHqMTgKoLWgkQw2ON8ZpfaJIRX88JYprmVAj3x9UmoqgKcKcmpdMgzakYJwQlbRe3xTQYsBnLjP7v6wDJXcRe2dzpK-Yoy-IBSzM5geHQJY1qHg0ayFgUSKkgjoQvustJKC7Ef0jXYmJTaaqT1OGdnP8ywDr11DDDipNtiH50mSjhCKf2DKWyFDSs4_pbIa2NfDSinHDpWwVhuqWbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برترین‌گلزنان‌تاریخ‌جام‌جهانی‌ و برترین گلزنان این دوره از رقابت ها؛ کار لیونل مسی برای آقای گل سخت تر شد. لئو اگه آقای گلی میخواد باید امشب در فینال برابر اسپانیا دو یا سه گل بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/26106" target="_blank">📅 01:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26105">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v1WNPwI3jYRtnY8YmklUBh0z9zxNW5HHcULVmK8dMV7MJJVnPNnhNRCajVC39xgb2R-X0fm6vbvxRusp58Ieev4MdN8ZqqxtivqwWErrKcj-LRKLJtMGeRYfmvsVC1OAogznP9p7_zCtfy5QZldSTbGAe5CmGVUu5WwC7lKqG7qGypbjbT58EO_G5n_ncQcr7f5s6KJn_-JWo3It6yAKlhzkaVBLoK1pp6kg_ylKyJv01h5o8k2O2wfJ0EJ4HrHXzLZ5RXvgYSKLjfNkbYuWj9Eajra3OmPRXiZUR3ET5PxNI4lcG-0H4vw1GW85h2CF6MhlaUETiAesgaXkVjVINw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دریک رپر آمریکایی اعلام کرد که؛ این بار روی قهرمانی آرژانتین 5 میلیون دلار شرط بسته. تا حالا هرچی شرط بسته‌بود برعکس در اومده حالا ببینیم این بار درست در میاد یا 5M$ بی زبون هدر میره.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/26105" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26104">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eetfnq1-x_d5y0SDzxJXV4SKkDHandGlkDxmJuo6l3xeQgSXF5zeB0ouyj6HT-VwzNxniAFa_r3ic0E0h5wvbc0W37RGSUooTiSaNljpLyEXyOZBvYy5RvEC8EHj178B4rKxbuJ-1fzJG4rIey6cTn3RDbWwyypCaspg8upN7MDYWKBRR_F83N8CkttzEfZ047UylyoJCQOQvWaXytgYWblwlkkEL4xwakUx2Ttbt887UDQZXxqhEPw7vRwFg3BiiUWwUq2GYbIh1TCTmbDCnfwdy11znBTFUSUeZ-zIsKL5rxH-dgXqkvLj5WC3IYb0rQjmLcCelsX_7Jb9RAlf7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
بعداز 12 سیو بالاخره‌مارتینز تسلیم‌شد؛ گل اول اسپانیا به آرژانتین توسط فران تورس در دقیقه 108
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/26104" target="_blank">📅 01:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26103">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b656d9cc6.mp4?token=a4ex1nB8RXdOtOgBoz8K_hgpqc71267B-2jF4dBD0jPh242kDRPyMi2eTG8gL2Zli_jfM34hxS343FYwgUKB_4A3dv17e6wJg4IKs4bcwfvmwJBy-WTUzk6Q2s2EOEftRse7OY4EhgQFhyvJ8rktONAuIelStt3sufW5p8k-W9Z_dQoqyTED0RFSRj4DxA9Vi-gNomcz1JFoo9iu7ulBnU1KdvmO57OsrWStZssceL7jR7YT2Ah2YH1xCyERSNwiuADLZznFetAYCFdmZV0W1eibAmzS8rotxKRyDX4EVekg0lx54ZeMJPQsA_wTqwhQvW4a0d7RTGrs4SEBNpDQ1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b656d9cc6.mp4?token=a4ex1nB8RXdOtOgBoz8K_hgpqc71267B-2jF4dBD0jPh242kDRPyMi2eTG8gL2Zli_jfM34hxS343FYwgUKB_4A3dv17e6wJg4IKs4bcwfvmwJBy-WTUzk6Q2s2EOEftRse7OY4EhgQFhyvJ8rktONAuIelStt3sufW5p8k-W9Z_dQoqyTED0RFSRj4DxA9Vi-gNomcz1JFoo9iu7ulBnU1KdvmO57OsrWStZssceL7jR7YT2Ah2YH1xCyERSNwiuADLZznFetAYCFdmZV0W1eibAmzS8rotxKRyDX4EVekg0lx54ZeMJPQsA_wTqwhQvW4a0d7RTGrs4SEBNpDQ1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
فینال جام جهانی 2026؛ شماتیک ترکیب دوتیم ملی اسپانیا
🆚
آرژانتین؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/26103" target="_blank">📅 01:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26102">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HOvvpXUAR7tVlzR7-o7H1RNeAtjAJ1CQw0ZA9lsJ4i7Iq9uuiybdIozp6zaAlDrE-jF8F0AmD93xPnvdmOd9SsCl3CL5rrel2ky3Gr4bVYqVy3PVDCfU1kTZ5YSIuq77QOiUOk48honcW-O36AgQ2oR1WaXLzwhdoP5qzKMPyuhI6yf60_9RRLvzM_iNInJuESv2yeoDgqfUiXZgZf6w1lkavj0ZJlNkKo7GgBakEanIn46dNDciVpB2HdbP4ILKdUCy7oE9rZo3uvpLhYq4A6k9elYdDGqjq090h7TzNsAWrgEhpQEgsLUwzO8WYjT6hginf3sygxm5mgfsulGFwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
ارزانترین بلیط برای فینال جام جهانی ۴۴۵۱ دلار و گرانترین آن ۱۸۸,۸۰۳ دلار قیمت خورده است. به‌عبارتی ارزانترین : ۸۴۱ میلیون تومان و گرانترین: ۳۵ میلیارد تومان و ۶۸۳ میلیون تومان ناقابل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/26102" target="_blank">📅 00:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26100">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g2Sirxwx51n7GEwFgQKE3PZCCDop5G5jV24Mgk_L_AGnH8fMjK5BvAAArwyTePBlqXZliYP43fAhkl_I98Qtk0_P0KaoWdKOrxO5zVMyNaCMIPpEX9AKYvkMY-txDt0REvkoDEpS1gOQMeSQf0PCLBGTQsbzoR9kBWacHvp9uXjzv865ts4AEXmJ5hD_4sO5_tYfyNGSLgYmIZrtW142mWVA5ml5qKxyHd6HKTiZZ5l8Rv37SFSMXg0gE9lh2cy4SsI5y5rhnDmRnW_KiXZrI46LHwCkbGnqKBLoBl32jPZYo2w0JZH-K4SE-Mm2_1yq2qGNEsx3TWRQtPkEfmgZHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sIe9OjI_56s8cxMEN9JuPaOA_w8n2uoXZSL3l0ew-s_4si_saHxmFfBrseqh16pGF2mYTr6RzfRtYeCavv9R2cMDCHP7POSrCmyOt9k2Tg04gIaoQJH4oqDu5uw0n_zUnO4z67U5-T9TQxfPsMaP2i-KqCcNtgTcyFs-m26YMNUVshI0gRr37Jcja5MZhmIW17yk3zixZAr1YmXBkBM_Vmktc7HZSl1Ukx55wNAvsMlMgxOpV39ExCUbexbhcJabTin_7wSuJV138lk4PG9wZFpxRlKzXPLKpt304v2jh4wyuqzdRrQDB234qPbkQ2EIeezng_7g64dZuvnOsgz8xg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
ملکهٔ آیندهٔ کشور اسپانیا به‌تازگی به‌ طور رسمی سه‌سال‌آموزش‌نظامی خود را به پایان رسانده است؛ ازش پرسیدن هنوزهم به گاوی فکر میکنی؟ خندیده گفته دیگه نمیخوام راجب این موضوع حرف بزنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/26100" target="_blank">📅 00:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26098">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kCe8-yqdEDMPhyVeH1UCFVgRWNHtdV2r2stwD1KCmvDfCB5SysSuZGZva4_Eqpz2bU3bF0RbvVyCy9j0vqF9N73iLElij8S0C4sauMaTaJNot3mqwItqurj_R86-pZBqPyZfA5tf4MKNB1QFlFUPGYfjKc3ExPiX4JAwsyHcqirXMG7CPeSY9tk2aAv0n1dJGb-yusz4Q0BxpBkKjIeUZ6tXHc_daO-hgq6vpNL7e2EdcuUTttsxnJchCbAUqBBpLslh6PakrAP_HwotyKJGwd1_JR22zg0-ACAgNetW4C1tJ6FunvhgjL9zXbD0yZNtIuasCRUSRYISB6MogVqxnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V8zHR54JeD8sG3h5AGnUtbRYuilxmr50q8IslSoArreM1Z0VWYI6u33BM1qvgdHCZok7NkmEraPpcqgcsok7obPsWBkxy4DMUue9tA5dXMGJMJCTjWbbvtoCk9t2OMOu6_pkr-2bzHpm0bKDuF8CcaJ8dK2jNq8-tLEAI4UO0PztD2UE73hXe0szHs-aWzpuyO8us0Y_6FSXVPZIEU4IOqlodqzkEy8S82hhZXdu30czMSllqR-W2pnL12qxQJF0CaZZf0zSRbfq_ZkW6fDP3aNDDTP3qR2TtRVTZTkQu3KzdvViiFU5umdSYMqXQbYzXzjfq0rKtohtjLJur1wJYA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
ویدیو کامل اجرای بین دو نیم فینال جام جهانی با حضور شکیرا و بیژن مرتضوی؛ عالی بود ببینید.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/26098" target="_blank">📅 00:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26097">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🏆
لحظاتی کوتاه و جذاب از اجرای امشب شکیرا خواننده کلمبیایی درمراسم بین‌دونیمه بازی فینال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/26097" target="_blank">📅 23:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26096">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6a67771f7.mp4?token=bAQNUQnjuLBVy6lV2aP0luPgvMNzJxE6QP-B42bnnAOf8o5eWHENFk4TCSLneADaxdC1CYQruha1QYvE5LypPXfyAWiHqLRyV5kqzv8efclYP6_j_48D4teaMkD2EKJqKcsig5yN326skkJRq0WFd0Y1TgNF0akuen-2ELtfZnEXDxVE9mv89sKMNkKFGvcg5KHa85h2IXybuwinr8-YQaDHIh9Q43t6nGUmP8NKQDp88sO0PkalWhHvaX3Kqdohc7cAd4luc8Qx5rJXPr2P8dhETOgOf4YEeHGSOUVaN0OphNaQWy9aXn-5rZOY09ZKwTVPEYbTkdR9x8ndbIhyrbzUklUQeHXkX-dFvfSKXrb2WJAfogx6xov-jyTXswBtWmSkg-lsqqjluxw4IWxyh9aFZ0hSii5JkGxfbMHKRPXn9WCqFpX_gjdSN80vlPop1LoyIUg0ZAyNM2WUwtNcCs2y0N4QifgZLQrQtmgBqGVIpLA8B9cAQiKhdzC4joBmddcjdM2B0vF8Pyw_sw1OcboCYICn4Thq3KD1w1gX4zhrJGhNqXJNmXPb4xBX6SYDjo0EnA9VzBF4D_IXHPXyS4vTavo5gcS4mreV90oLavsUTpiKYAb6IniWjSNfzOlkFWq8A5K6Cslpv0V3hMDOlgTbTL0_bPq29FHeKGjrxk0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6a67771f7.mp4?token=bAQNUQnjuLBVy6lV2aP0luPgvMNzJxE6QP-B42bnnAOf8o5eWHENFk4TCSLneADaxdC1CYQruha1QYvE5LypPXfyAWiHqLRyV5kqzv8efclYP6_j_48D4teaMkD2EKJqKcsig5yN326skkJRq0WFd0Y1TgNF0akuen-2ELtfZnEXDxVE9mv89sKMNkKFGvcg5KHa85h2IXybuwinr8-YQaDHIh9Q43t6nGUmP8NKQDp88sO0PkalWhHvaX3Kqdohc7cAd4luc8Qx5rJXPr2P8dhETOgOf4YEeHGSOUVaN0OphNaQWy9aXn-5rZOY09ZKwTVPEYbTkdR9x8ndbIhyrbzUklUQeHXkX-dFvfSKXrb2WJAfogx6xov-jyTXswBtWmSkg-lsqqjluxw4IWxyh9aFZ0hSii5JkGxfbMHKRPXn9WCqFpX_gjdSN80vlPop1LoyIUg0ZAyNM2WUwtNcCs2y0N4QifgZLQrQtmgBqGVIpLA8B9cAQiKhdzC4joBmddcjdM2B0vF8Pyw_sw1OcboCYICn4Thq3KD1w1gX4zhrJGhNqXJNmXPb4xBX6SYDjo0EnA9VzBF4D_IXHPXyS4vTavo5gcS4mreV90oLavsUTpiKYAb6IniWjSNfzOlkFWq8A5K6Cslpv0V3hMDOlgTbTL0_bPq29FHeKGjrxk0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
این هم ویدیو زیبا اجرای بیژن مرتضوی افتخار ایرانی ها در بین دو نیمه فینال جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/26096" target="_blank">📅 23:49 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26095">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb8fe73d8b.mp4?token=FA4KUMrd5LMEEURsR0qrcdqhLsdfAMtxa5AWc9XSmcGXATkidSw0HBDGeFsqMZnlFsBriSbV5xCAK7wBFK-hkrc9DIWxGqg2U7CqwCM93hjDyK3bexLr5cIiggojsQ1CuvpU8I74HHcXVe8nyhIluy_OM-s5GXXijqRT0qrvbbNFhDkFVvKtDhioocpGCYdnGP0fHRyJmYq0tg7gkGPOxESSOOm5j7Hjwl7zEkL5AwUObVVg69ov2PjDxydBgJr44Up1YQMYAcsutB9nNUV6KiSRctfHKeZPPVeHLWqczr9GJ1oV43ISMB4L8bsr8brs4hyF0gJKzeZ-ZCoi4EWbpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb8fe73d8b.mp4?token=FA4KUMrd5LMEEURsR0qrcdqhLsdfAMtxa5AWc9XSmcGXATkidSw0HBDGeFsqMZnlFsBriSbV5xCAK7wBFK-hkrc9DIWxGqg2U7CqwCM93hjDyK3bexLr5cIiggojsQ1CuvpU8I74HHcXVe8nyhIluy_OM-s5GXXijqRT0qrvbbNFhDkFVvKtDhioocpGCYdnGP0fHRyJmYq0tg7gkGPOxESSOOm5j7Hjwl7zEkL5AwUObVVg69ov2PjDxydBgJr44Up1YQMYAcsutB9nNUV6KiSRctfHKeZPPVeHLWqczr9GJ1oV43ISMB4L8bsr8brs4hyF0gJKzeZ-ZCoi4EWbpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
اجرای شکیرا همین الان شروع شد؛ بزنید شبکه پرشیانا اسپورت نگاه کنید. ویدیو کامل مراسم براتون میزاریم که ببینید. نمیزاریم چیزی از دستتون بره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/26095" target="_blank">📅 23:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26094">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e6ePasQpovPtJktP95oC-VXNP8qTvBjbUbc0uBjKrlYlEWLd7w-ylweDJY-ZFkPppKT8MHqgh8e1sS_OHjPHXTTZGdB11djaR_LVOfXeVql4W1JDjV7fB7AdzVO7tit0QftyGjJasPfP1e1zZzArmLcKrC5_gK92bAJdcQZgiRDQotf_196xZEWzexHP6mqq8SGeZiMSK9p7GS5rby_5aKZDEr29ADMWvm6iQ3hHkJokT5cpsuga3FfQfTq7yEiK2DZZmcLKqOa2xLaN3lP8RTNyaiCWftWqkD50dvXgS3YhxT3X5RgnB_ydctVpSc1P3LWMkVeLmEd38UHhTmd3gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
خب‌تادقایقی‌دیگه؛عمو بیژن‌وشکیرا خانوم میان وسط برامون برنامه اجاره میکنند حدود نیم ساعت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/26094" target="_blank">📅 23:42 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26093">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2daebffff4.mp4?token=FIjVUy-_bKsbXpf5MUHAGSZcvR68rVRB1GKxicDO8LYaB6zlc8Gr5tSZAoPqulQ4YBrtrclV5dhmr11GDQ_wWZ-ks8Lo0C5hgUH1j-cLXL4wYX9zERVjG4XcTnlD3yIWlCS86dSBRST70JVO5Kx9rSJWHFoV3JPn58AyNo2yrRDJO3IPp0FYe-dn1ks-40FE141VG2qaNBzz0CteA66pUcBuRCQ1IVkqAlM4Q6iNk5CIs7nsltnTKndRk9fMCngVjtm0MU6yQseSOxeUM4o4fxUTgKBxvK6ORk8aNg4TB1gmmxgngqlVDZSXmrU1CAY5ORPjWZRCltdSiydNCQVNGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2daebffff4.mp4?token=FIjVUy-_bKsbXpf5MUHAGSZcvR68rVRB1GKxicDO8LYaB6zlc8Gr5tSZAoPqulQ4YBrtrclV5dhmr11GDQ_wWZ-ks8Lo0C5hgUH1j-cLXL4wYX9zERVjG4XcTnlD3yIWlCS86dSBRST70JVO5Kx9rSJWHFoV3JPn58AyNo2yrRDJO3IPp0FYe-dn1ks-40FE141VG2qaNBzz0CteA66pUcBuRCQ1IVkqAlM4Q6iNk5CIs7nsltnTKndRk9fMCngVjtm0MU6yQseSOxeUM4o4fxUTgKBxvK6ORk8aNg4TB1gmmxgngqlVDZSXmrU1CAY5ORPjWZRCltdSiydNCQVNGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
خب‌تادقایقی‌دیگه؛
عمو بیژن‌وشکیرا خانوم میان وسط برامون برنامه اجاره میکنند حدود نیم ساعت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/26093" target="_blank">📅 23:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26092">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ebtwz2KTfQA09PUwNjygJplIrERXlN2yOVpq3tmW6cFhAy1P8_BD-NJyXfY4fZMNCuwEe72ceBE9MISmP2W2-96qVjBrJ_aVBVB8Q8iwwDRE2PBMVNz162KJ0KuXymk5hRacdheF6SLerko5gAa0T0MNgQkT3EUGpnWx4-0ZdkcbKcujoqn_YkcNRpEsr_42kibxaBaP0y-H6hEf16gmsYGwRWizGWp6YdzSLZyt0N0Ywt2zmTaV5pcqwRXEdWiBYO6gF5A15Z6N8j9iqBYnibDwUa-93OR8uhpKtiwW1x-uwACFukeZNe4BSsITYtSUTBUhLHBNyC-5U2tKetnlQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تقابل لئو مسی
🆚
لامین یامال بعد از 19 سال؛ لیونل مسی: چقدر بزرگ شدی بچه جون! انگار همین پارسال بود که داشتم تو حموم باسن‌تو میشستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/26092" target="_blank">📅 23:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26091">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JtL9IVI9Oji4tHKK5dNQMwy1c63gz-SQeV6MZ3wdIm-N-6oSbcDrThUpIWfWlcI61B6CPkdsXwGCRR2b8qVcqTf2wZBc79lhxDEa4ZvDu9kIGOC44tlznGGJRGWbr3cSnOjOP6ZykdJKareEQLaWYzONIxrpi4eA6zi4-xCjlxxP28Lhbs-NTtI-xFKambf1FApFxCwgVkfvAZAXKFlISzhGd1spymXWKRLM1MX83m1foJRzOfxJ8jURkf4Kp8L4PC6QOLS_dRwN3iEHs08y0g-lEU-2LL_Zd9M6Ce8_FeZXYAX3BISFJInz9t3wneK1NdoEGDPVbZireEFQuLewHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
الان‌فهمیدم CR7 چرا انقدر بچه‌داره؛ جورجینا: من آرژانتینی هستم و تو کل زندگیم طرفدار تیم ملی کشورم بودم و امیدوارم‌امشب آرژانتین قهرمان بشه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/26091" target="_blank">📅 23:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26090">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🏆
روایت‌جالب فیروز کریمی در ویژه برنامه امشب جام‌جهانی‌از غش کردن معروفش کنار زمین مسابقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/26090" target="_blank">📅 22:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26089">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de9d2fca55.mp4?token=aGqQueU5MxORO2uD4bs4DkzKMwZfFwmj5WAQU_s3Yx_6Odcz3odzqQBwsUObkxAUcN24MVMkrkHUhD3-AbDFByLIh_ZvSnmVss0pjN0sQgjVh8wGu0lzNiGBE2DBYAbQ7JkkLAHCJIWaXi36m0wwzVWdtI91J9zj5FXvWgzKhxEw96dWw0fEL_tynV3d3ENP03qqT5alJ4bqu3wTK_6nZX2maepNME54d10YxVwor0XKxf1Pe1M2XAkL_mV1a-BxMP0L_UJCnbpZII0tTpgcTKUJbkVgnGvl51Y_FD1iMfAOdOIuHGLoXJQ3bcclw5r0KZ5JJThsenUm92oGeT_HEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de9d2fca55.mp4?token=aGqQueU5MxORO2uD4bs4DkzKMwZfFwmj5WAQU_s3Yx_6Odcz3odzqQBwsUObkxAUcN24MVMkrkHUhD3-AbDFByLIh_ZvSnmVss0pjN0sQgjVh8wGu0lzNiGBE2DBYAbQ7JkkLAHCJIWaXi36m0wwzVWdtI91J9zj5FXvWgzKhxEw96dWw0fEL_tynV3d3ENP03qqT5alJ4bqu3wTK_6nZX2maepNME54d10YxVwor0XKxf1Pe1M2XAkL_mV1a-BxMP0L_UJCnbpZII0tTpgcTKUJbkVgnGvl51Y_FD1iMfAOdOIuHGLoXJQ3bcclw5r0KZ5JJThsenUm92oGeT_HEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو ویژه برنامه جام جهانی یه هدیه به ایمان صفا میدن که میگن این هدیه کوچیک برای شما! بعد صفا میگه این اصلا ک چیک نیس چرا اعتماد به نفس ما پسرا رومیاری‌پایین. جفت مجریان‌برگاشون میریزن میفهمن منظورصفا چی‌بودمیگه‌تموم‌کنین‌برنامه رو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/26089" target="_blank">📅 22:24 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26088">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pUUbbeJLEY6urXpL4MAXB1OU4vebQw_8UMbzwdt37WmLaaog-RnFAXUrL3VlfqSZwh8IvrEOKqiDqskJyC5O88rI8Q_E96pJxL-9JmgrORmxkI7wN8b9WLnyThUHks1NbIszDMXqjaOfBYUd2cONUZ2rXYqQVKjHt4x9txd7yc0ButJGw7zbMp3eEgxm1Nt6y84iwyO6t8y76i88BuVl4mmiOe98grId_2rARGybyVP3r2DN1FI-lCWTDbHjaWPXRkTfwaHIiHeK2xQXbrCL1o6R1UUpBAMed3bgkcxfXQNQmlj1f8B-vtdVlLl4SjwnLmwsfjZxmF9Wy7YXXPl21w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابوالفضل رزاپور درصورت جدایی میلاد محمدی.</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/26088" target="_blank">📅 22:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26086">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68101d4663.mp4?token=FPTmjbS78z0a0MrMp3Zxcv1KYyFxrkc0M4oLZmZjtcGtFkQ4jo_WH_r2FwOeh6e04btncbq5pQZ39x5HtIe4oGcqWpT1YrjwvPfwBo2IVkgMaLwdIp35P030GmGL-ycSQVX2n27ie3Yu4CxI-PSrQ6WSJ9FxPaGjqGfoITFRROsCI6s1fDjntkZcTNE7efUHfLnsjbeV6HROb6TruK0ut60_WaU3VP58CVuwN4QuJyDCpSth5BCcFduRAJIkzuF0sjrS-AHDyja9Sf5xTHxnX3Rz2VA6GQ6KhhD3bflGKd-e99S4wLk-igP67cH7nMuLkfcq1PH28yUeiHMr1iWfhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68101d4663.mp4?token=FPTmjbS78z0a0MrMp3Zxcv1KYyFxrkc0M4oLZmZjtcGtFkQ4jo_WH_r2FwOeh6e04btncbq5pQZ39x5HtIe4oGcqWpT1YrjwvPfwBo2IVkgMaLwdIp35P030GmGL-ycSQVX2n27ie3Yu4CxI-PSrQ6WSJ9FxPaGjqGfoITFRROsCI6s1fDjntkZcTNE7efUHfLnsjbeV6HROb6TruK0ut60_WaU3VP58CVuwN4QuJyDCpSth5BCcFduRAJIkzuF0sjrS-AHDyja9Sf5xTHxnX3Rz2VA6GQ6KhhD3bflGKd-e99S4wLk-igP67cH7nMuLkfcq1PH28yUeiHMr1iWfhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
عادل‌فردوسی‌پور: سعی کردم تیم ملی رو خیلی منصفانه نقد کنم امااین‌حرف‌که هر کی نقد کنه وطن فروشه نمیره تو کتم هر کاری میخواین بکنید. وقتی اینترنت بین الملل نیست من چجوری میتونم برنامه بسازم. عادل از اوردن اسم قلعه نویی خوداری کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/26086" target="_blank">📅 21:32 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26085">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9df505731d.mp4?token=Mbtr9XM6LSTjW1nftsXQ9fpXsMbG4HfzDOLXViDuHKnVth3cj-OgV32qs2UhSKFfx3jtS__K60NpkyQDF8s-q3nCfDrdj6i5WKJd8b7j5gpZmyX5JJKrVjD8PQE4W2IUNrYoaPAGDfMD1stD-FfoW2f5-akjprM_KUGY9DgmAtYhndTJ13lXZ9y6zr6NP1pW7l5FORTbvTt7x2JEF3S_7FsYkc56IY-TOPIoR8NFSN85EUuAVecFkxI9AX1arHonnomg1Rnsi0k7L-YrdRqiIYUn5Wj8D5Yf0-weEhThVLo659DM87h1Nje1cyn4IJ3nkr7wahts9kYYlpvTEob59Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9df505731d.mp4?token=Mbtr9XM6LSTjW1nftsXQ9fpXsMbG4HfzDOLXViDuHKnVth3cj-OgV32qs2UhSKFfx3jtS__K60NpkyQDF8s-q3nCfDrdj6i5WKJd8b7j5gpZmyX5JJKrVjD8PQE4W2IUNrYoaPAGDfMD1stD-FfoW2f5-akjprM_KUGY9DgmAtYhndTJ13lXZ9y6zr6NP1pW7l5FORTbvTt7x2JEF3S_7FsYkc56IY-TOPIoR8NFSN85EUuAVecFkxI9AX1arHonnomg1Rnsi0k7L-YrdRqiIYUn5Wj8D5Yf0-weEhThVLo659DM87h1Nje1cyn4IJ3nkr7wahts9kYYlpvTEob59Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خداداد عزیزی تو این دو ویدیو به بد ترین شکل ممکن‌جواب‌صحبت‌های‌قلعه‌نویی رو داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/26085" target="_blank">📅 21:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26084">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iPGjsnKFHMymrIPadJhQ73N8aw0vUbpnhTsJUBB3nrHS5Xc9kLX7lbzkro7fPq0vaDuJ2ovzLO0JQFsCqb2O8LvjriBtguSXRdXB9EWfY0tFWdPKiNAQkhaa-kUOyz1v5Iy5iZpIMqei_Wd8EZjZ2Tc3zynUKE4QFlbQhj9s3fJx3kiGABsuKLeVhdIFRNX6r8hAEOJZUpTWdJz7kbP18bbb-ctiFMAoydDvA_LMg1r3H17EAC9giyag7keSsrJ0bFqZFfX9u4pDC9T6FpeQ1cMGMaPSb8s6-etaRZDzAOVpI4DUI4edxenuePXkFssWlhwnngk6W75PX_ZFqfHuXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وضعیت‌بین دو‌نیمه فینال: بیژن ویالون بزنه شکیرا شیک، کی میخواد جلو این ترکیبو بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/26084" target="_blank">📅 21:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26083">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60f87ee3ff.mp4?token=VUUZLSyRb1LcsrPjoNKT7PvWSUZJQxRWEpzSHJ_Li3vUGvm8Q37XIVxxQnCEUzD3E9rMIfxIKTXUP9OWs66d-JJpAZu3uK2PKkH9AwYLzT0nSmTsaH88_Bf7iEoXnx9yRimq9YUvelrGUYkvu9__r0PTayG9AGNWAGjxQW1a7EuUWyf728Zqobe1lGX97RGLcUHybYZOdYalvqpj7P7Fi6-4Sz980LhDh7y8CtMDsvj2ba-r4BomboxqK0-0sR_MCY02MSFSEbZbvJ-DAFW28W_UcgTQns_D4v0pfJdeO-y4rK14Dd5Dtg4_bCHPElnF366QnLy0HxyUG-iIueKoaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60f87ee3ff.mp4?token=VUUZLSyRb1LcsrPjoNKT7PvWSUZJQxRWEpzSHJ_Li3vUGvm8Q37XIVxxQnCEUzD3E9rMIfxIKTXUP9OWs66d-JJpAZu3uK2PKkH9AwYLzT0nSmTsaH88_Bf7iEoXnx9yRimq9YUvelrGUYkvu9__r0PTayG9AGNWAGjxQW1a7EuUWyf728Zqobe1lGX97RGLcUHybYZOdYalvqpj7P7Fi6-4Sz980LhDh7y8CtMDsvj2ba-r4BomboxqK0-0sR_MCY02MSFSEbZbvJ-DAFW28W_UcgTQns_D4v0pfJdeO-y4rK14Dd5Dtg4_bCHPElnF366QnLy0HxyUG-iIueKoaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو ویژه برنامه جام جهانی یه هدیه به ایمان صفا میدن که میگن این هدیه کوچیک برای شما! بعد صفا میگه این اصلا ک چیک نیس چرا اعتماد به نفس ما پسرا رومیاری‌پایین. جفت مجریان‌برگاشون میریزن میفهمن منظورصفا چی‌بودمیگه‌تموم‌کنین‌برنامه رو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/26083" target="_blank">📅 21:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26081">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">❌
کنایه‌قلعه‌نویی‌به‌علی‌دایی: ساعت‌بستن و کت و شلوار پوشیدن نشانه شخصیت منه. اگر لباس یقه باز بپوشم و زنجیر طلا بیندازم میشوم مربی خوب؟!
‼️
همچنین قلعه نویی از مسئولان جمهوری اسلامی خواسته که مانع پخش برنامه عادل شود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/26081" target="_blank">📅 20:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26079">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rUiIMx163j6SLScG_rEy4z4LEnncliFoEkrw1rgooF_fYwkQKAhAZtGvzY_OY2cCl1i9whmao9LkZE7PSs0rdp8zAeI0WCuV5Qw6ahHCdn8LfZnJYtHserDCh7S_ULfGiRx5Id-7T_xAUo14rDLUhVA5BJ27PJWEO6SLXm3Gx3wvQ8q9RNi-xgA1RKBi7XmPKEWWQTw8iJKhhREsnuQlpy4NJ7Q6cgFYQpq3SwXbBBtk5yC6zLsNYG3d4PQygxGjyQUkNs52Q-lxn2j6YOjwFavnHaBxdO6NxAns6T4_mcXmTZCpltqyXg189tk7wMAIyVxsC_PT9kf_GlQEFvmsWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S7OW_MzThLdNca9rGCx4BPQ3uUKXAOuN3BAd2LjJMam5lDNnpCKOx9bU_2MU2caVzn6-yajLun93-uEmB8XZT45bLPxQADP3ZM0RSt4wjnIsI3fTwbbqGeSNBNaHnpqD77oztHTi7IALQ73ySLjurnAIbBB0W6Z5dAZwCIEa7K_Ra-XRZsmuoE7D8_XYkkMDKVKyLBE2Uq4f9EIapikTRB7FbuY6g6KBI8uslPFp4oXUIBUlsxEk3aHviwoWOdcgLzAcecv7Ft1gsezlhx5O4HiXD5QajviKHXdp3tObLzN90NFlFElR8-AXAVXige9wsEd0dEs-dEg-xXVimO6pQg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
فینال جام جهانی 2026
؛ شماتیک ترکیب دوتیم ملی اسپانیا
🆚
آرژانتین؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/26079" target="_blank">📅 20:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26078">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SMG3Xe0NDhH7kPr319XL8vzJa4LN4W34np0ZzmRllKRmaDJw-Dabqz9EPijUhKTGc2677XmWLyGHUXhIGNiFOlltK3xDgzBYTmQrOcfVVp9PuBkZH7kBlOEb7cVFp_s-Rb0R0s02aJddzg3NvMS9WHnSoDbqhmu-5pb6cZfZiVOXtAb6BqyHicnROEcfCDTCRyy1YgNsigHCmdByP-_TIqRuDz9o447rr1Sjbm3P49ItI2URZpB9AgXOgYkUFHtbCaBjBacSni47_mGHQoDrTiSBP-3i6DyHZFtd5Tl1JUstHpEHY69KjMTbj9q7MUmZBmUkBlckDzsRO4jD9c4eHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
💣
#اختصاصی_پرشیانا #فوری؛ طبق پیگیری‌های رسانه پرشیانا؛ باشگاه تراکتور در روزهای اخیر مذاکرات‌مثبتی با مدیربرنامه‌های علی قلی زاده ستاره 29 ساله لخ پوزنان انجام داده و قرار شده که زنوزی 700 هزار دلار بعنوان رضایت نامه به باشگاه لهستانی پرداخت‌کند و قلی‌زاده…</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/26078" target="_blank">📅 20:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26077">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tMGqkmARObbz6ZNgJ0XogIQPccpdG48xqi3vChzhFgypAmavf7IedhGYRoEd6Ljes-PJ-cy2Ut5f_7hOwfRM-M4zybzkMIHFOMZPuNfwKJlnRhzkhmgaGW5W-WcqPCgrYhGmes24wQN6bPBzW7p4-pVgSKUlJEYhe569wLbgS-lZX8pVzQWCjyyeZQy0sw3jzwfTUttt_hqxSJSYe_RapIwGlKq_u9fIYG23dCBzMoVT9ETu96_XNOxxmaFZwUpA4c3_gUxfTDjc80JxtBVkCMJAGgc80peK70kJd63DOcwGD7dP0AGTjZSjeGJg9lzS3NR8DH1qK8LJWQD3UQPiwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
💣
#اختصاصی_پرشیانا #فوری؛ طبق پیگیری‌های رسانه پرشیانا؛ باشگاه تراکتور در روزهای اخیر مذاکرات‌مثبتی با مدیربرنامه‌های علی قلی زاده ستاره 29 ساله لخ پوزنان انجام داده و قرار شده که زنوزی 700 هزار دلار بعنوان رضایت نامه به باشگاه لهستانی پرداخت‌کند و قلی‌زاده…</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/26077" target="_blank">📅 20:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26076">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XwmEZdQ2o97-TNbNXwoEk-RU0KouAy8LpIEI_MOcra5XjvWndEtUfES1OfmQDxxycWnC9iskXB5ih0BGnYFyeNjWAELvoaJWq5lYRj9I8yPhzRe1MMYe-tT7DjgF85vR60YX3IgQHbPix-7vkfWDxEqtDYQt17fwrcZse7NRMFUUcWRClIiVjhhONkFSQ4JFDqJK0VaUn_C9Bl2Jj3BDIifRAGxoeb6A8eERu_AwS_EJoTGum6gvlWyuihLpi2UaX_xyQ7oECgTGXX6w1UkBy1sf2bzS59VSHa6NwvzpgsUfMR2FtJgv0BDN2WwYA2hRrG4i-B4kDws8oYPhJsIftg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
خداداد عزیزی سرپرست باشگاه تراکتور: تراکتور بزوی پنج خرید بسیار بزرگ خواهد داشت. 3 تا از این 5 بازیکن لژیونر هستند و سابق بازی در دوتیم‌ پرسپولیس و استقلال روکارنامه خود دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/26076" target="_blank">📅 20:06 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26075">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S1q7lVodFgHg4aSUFPGVwaWyFrJZ4MFQQ9WD7PweP3eR6ph0obVwnvmLvorSE5MIgh1YW4rKFS60dnjci4RJWHhZ9i8qZ6cyv8gufWIVwNqmsJbQIZaeEd3ys8xpf8acv1WB4qSuuQJycBXA1Lmi60clwQhT2p0yJ2tkEy6xNX_4sV8H_2hFvkpkgwg85GW1Zm_9kkH07ALyrHsPUB0QWbQ4RkTya3IX6rvxN3BKNVRzROM-rSP7GQP8fJWcIkcQeaoXP6luR1B1N3VIbhjrf_vmnYLYf0nKIH7_9LDeMikKsN6TKzL5xqyVmDgNLhNMbiEWBcfbCSR1fOyP5lvAfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یادی کنیم از دست دادن فرصت طلایی توسط گاوی؛ سه سال پیش شاهزاده اسپانیا لئونور ۱۷ ساله به بازیکن جوان‌تیم‌بارسلونا «گاوی» علاقه‌مند شد به طوری‌که همه عکس‌های گاوی رو داخل پیج اینستا و توییتر خودش پست‌کرد و ابراز علاقه نشون داد؛ بعد مدت‌ها به گاوی پیشنهادداد…</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/26075" target="_blank">📅 19:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26074">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qW-4QwqRJlToUmUnzQFUH7rCGolePZ373xpYhSYm_mwu4ksNpmkYhQPHc2l1uh2IqVtVRlEPWJ9Xj97cJf63x2A2URhDtyQ-7_OHDhGAj44MFWjqzi157d82sIP8BhPRfLoxOsJSVOU64Krdx94qzjMj_qXb8mfBQkBALnZAcUqWvbe5Zm7hBmhkF0rneSbvI635cUBFOH5t_CQsUfV3qz390CAyb1X7ahmJktSdR8JXlPDKhGSjVOrgEpQZoU_9IFDVZ6gmTpbx9AjdDXd8Zas1jjn7Bi6Wx-WigVSqb_R518-1dnAdwb2fdpsiEWIOBNdl8kNVbvoJ1OH3viYf4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
علی دایی بهترین میانگین گل ملی در مقایسه با کریس‌رونالدو و لیونل‌مسی دو اسطوره فوتبال دنیا؛ بعضی رکوردها شکسته میشوند، اما بعضی از نام‌ها برای همیشه در تاریخ بشر به نیکی می‌مانند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/26074" target="_blank">📅 19:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26072">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WnokxRyD33CNUWqfg7Qq_jeVUpgkazm2a2aKuQbompA9bFLWJPJzFCw2BdU68i7_9ApHVbZeef257cjQCWJf5AbuqELLcmzIShDGhgUeuazAlVfAXGNWlVPc_U5pJFsY_-fNVI5DnOqnCko76SiGAGfg-DJc6VWjq23Na747w7yllmCTK84XnVMudD9MvE3bfeH7pyPyPZC1vGd1FYl3LkNQ5mlnEyCOG2spQE1LGZPhkffVqJsx4Vywq65GkCCtUwq69Bl9aVMM2SA-pkK7edsMQbK-0Pa_L3lOmI5l3nUfOONyqjT2wyT511nAygoefOBhMarKX9Qi_UObFQzwqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
مزدک میرزایی:
عوامل‌شبکه ایران اینترننشنال در سه مقطع پیشنهادمالی‌بسیار بالایی به عادل فردوسی پور داد که‌به‌این‌شبکه ملحق بشه اما او هر سه بار این پیشنهادات رو رد کرد و اعلام‌کرد هرگز خاک ایران رو به خاطر رفاه و منافع خودش ترک نخواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/26072" target="_blank">📅 19:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26071">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qJmAPLO2sHZMrIr_YXl9mKKVyFy8JB5d9UYFMpWvvD4IVxOiwMo1MbTt1OQNiyD87peQRWayJ3VdGUEZ_akqc72U0xR9W4h4BkU4GUntsZlrZIGUE50safHhM4giMoYcihOVt85zqy0vLVVvz5DaR3IvtUU-n_tkwa0aVi1W7twtClgHatozybARr9Za8VooZB6AIeXsiQ_ETaO_Mxsbxg45QtmRVkADQJ-O5QU-Z3r7G2bdXcau4V0FkS0_L88ODehF6lArrkSGbpBR-f-xsB_kqxqN-3uBhP4C7lx_W1FCGPSoDjBGArdpNemTHcriZCRTDD2DWIv0iuMI3WXdLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جود بلینگهام دیشب نیم ساعت دنبال دوست دخترش گشت پیدا نکرد مورگان راجرز یهو اومد گف اوناهاش اونجا نشسته؛ فقط ذوقش رو ببینیند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/26071" target="_blank">📅 19:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26069">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76a250b46c.mp4?token=DnPb_JjtP1RD8MPj-UYbvQBzeYVGxYY2dP-OHXTxNtQlsDAqGp3_JjyVW3aNjUUcrPCRRNpmT9zuHWMEDCaLNUv8IHGVHTuDPNgB_x_Lrr-Pp1EAxGbpOoC_yktU4zcndBFLCHlSS08vkrPNBjX4oNBiF6UHqrd71oyWzKEK5lK5p2kjwpWtxPmdCi_A81-OjoM5KU9Q-YTbepgRPdxRrh6m_tBEUpEwD9-V40hFKS9scvYzCBXf9zoxMqjxAEYrNNxD0SVjkIK8E6gyG6x_kg-hx2_VNSVE2EoIujHrubWl2lmrHOgEHzHc9AgRg7kz7ZOQpzE5kqenckCr4IMRGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76a250b46c.mp4?token=DnPb_JjtP1RD8MPj-UYbvQBzeYVGxYY2dP-OHXTxNtQlsDAqGp3_JjyVW3aNjUUcrPCRRNpmT9zuHWMEDCaLNUv8IHGVHTuDPNgB_x_Lrr-Pp1EAxGbpOoC_yktU4zcndBFLCHlSS08vkrPNBjX4oNBiF6UHqrd71oyWzKEK5lK5p2kjwpWtxPmdCi_A81-OjoM5KU9Q-YTbepgRPdxRrh6m_tBEUpEwD9-V40hFKS9scvYzCBXf9zoxMqjxAEYrNNxD0SVjkIK8E6gyG6x_kg-hx2_VNSVE2EoIujHrubWl2lmrHOgEHzHc9AgRg7kz7ZOQpzE5kqenckCr4IMRGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جود بلینگهام دیشب نیم ساعت دنبال دوست دخترش گشت پیدا نکرد مورگان راجرز یهو اومد گف اوناهاش اونجا نشسته؛ فقط ذوقش رو ببینیند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/26069" target="_blank">📅 18:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26068">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dC6Kc2fMBgNQnWbOEC5MA9VOqFNXLcX0NQV-oY4CFTL99DGkn3UNufuBjtQLqa_XTie04kQD5gupdC-lXIulLkK4TMn4pWyuKypqy_vRMZnai_UrGwerWQ_elmRP_5APpeVpB8qIaM9m1Wb9e7sSaNAtsU7Qur05JP7YehazyFuKkeLjq6zYSpFBrWIe4PNpKw-WsQKSRA0u4OCNfYVSHbrXZVI2waHtC18gz49il7yCUgKaTeosllFNItzFwKG4OeCgR66q0b28Vr6qw4dFWWywg_guBEZiZOQjfED5E_QrHyrDzXqor0K2DuAy03dc5WB4TQYbTCe2TYexAWxASQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در دو جام جهانی گذشته؛ تیمی که در مرحله حذفی با نتیجه ۲ - ۱ انگلیسی‌ها رو شکست داده در نهایت درفینال‌باخته. این اتفاق برای کرواسی ۲۰۱۸ و فرانسه (۲۰۲۲) افتاد. در این جام جهانی، آرژانتین در نیمه‌نهایی انگلیس رو با نتیجه ۲-۱ شکست داد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/26068" target="_blank">📅 18:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26067">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GJPiGWo_4UUJiTGCZnMlrWdpYSR_89FxPRCN32XeHgWxxlXvfX2llsT4ycbpwWPZ-l6NprQJrAw55i6WwrAyNd98K3qOGlE3qOt-HCZmxHFekcmUJn5NhmA0tnKuOVDiG8UZT8xEM4xf9ohvuFFblOpPVj8PhHUmYek75f9VN1fd3Q0u2i0ldkjKHgg7jfOhO8xl_GLdC_6-KSJKheMt0Bp53Xq20iyoVbXbTx-ylGLDBA2A2QIDel3i_WELmG3Nb900WXXhAsmeEK0sQznmVN487DKmUZOxzEZjJESR_tRSgTCYpkxEbe3XMFaT0brspl7tPTRglrmheHZmgYVqfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
میلاد محمدی مدافع‌چپ‌فصل‌گذشته پرسپولیس باعدم تمدیدقراردادش با سرخ‌ها با عقد قراردادی یک و نیم ساله به مکس لاین ویتبسک بلاروس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/26067" target="_blank">📅 18:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26066">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q1msX6YCXoreeg2WVoDZyNozmMkRaM4y3N7-NWbDiqmvnlF0U7EO49H1HUmij7kRLSsIS8iX780yPeil3IkQcqLh_BZ-DUlKpuOdUQmNjXGmZZhYoPhSob3n6v4V71D-HTsVt0BFAUijWiyb7IIu6wxK8sY0_wmoryp1yt5A2eCq7NceUQ3WuK2ye-2kKp5MdpUdGZyOO55bzGZTXNJEX8bD5ZOfIy9mdOKM6YIfqiC7SqkSEElC7oYuChytUA1ZvXjawtcxCwkQHLoQi_piV145mE_LFCQHh59k6TFMVCnDKX-ucwKLBi0kBlIFQxb1AtgPaavcmJWXEplHPc33gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
طبق‌شنیده‌های‌پرشیانا؛ مهدی‌تارتار سرمربی تیم پرسپولیس از وضعیت فنی سیدابوالفضل جلالی مدافع‌چپ‌جدیدسرخ‌ها راضی نیست و به او گفته اگه عملکرد فنی‌اش بهتر نشود مجبور به فسخ قراردادش خواهند شد. تارتار نیم نگاهی به جذب مدافع چپ نیز داره. جلالی سه‌فصل قبل آقای…</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/26066" target="_blank">📅 18:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26065">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33544e2a7b.mp4?token=JKsBPQ5Q2WeXkMoTY1C7ualCOC6oPbkblTHo_8QkeUS3RebDv6d8dnzwohnQOgy-v121rnbAQSaabEVpcbbRrtTuDkve-TfK-Fujc2rr7nMXHkQGub-E55QcYarDv9PR1u_2ys8Ddrl3Gp4nK_cME5ZnEPXvbb4IxDYiU5LbV95jg7eZqXwFbJptXFtwMe8HQTgUlmgJbPAVjheB294zWDe0bc_p0_ehT-HiOce-bvZ57CryENv7BK017baQYDi6yVciU-YIq1RG44strQamEiDxqlxAkGFO8OjzISUJWOUxNS-cTvDKLijgbHzAJYT5r-eL42M0yihNA_r69nJBtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33544e2a7b.mp4?token=JKsBPQ5Q2WeXkMoTY1C7ualCOC6oPbkblTHo_8QkeUS3RebDv6d8dnzwohnQOgy-v121rnbAQSaabEVpcbbRrtTuDkve-TfK-Fujc2rr7nMXHkQGub-E55QcYarDv9PR1u_2ys8Ddrl3Gp4nK_cME5ZnEPXvbb4IxDYiU5LbV95jg7eZqXwFbJptXFtwMe8HQTgUlmgJbPAVjheB294zWDe0bc_p0_ehT-HiOce-bvZ57CryENv7BK017baQYDi6yVciU-YIq1RG44strQamEiDxqlxAkGFO8OjzISUJWOUxNS-cTvDKLijgbHzAJYT5r-eL42M0yihNA_r69nJBtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تمام امتحانات نهایی پایه‌های یازدهم و دوازدهم چهار استان هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان، تاآروم‌شدن شرایط لغو و به تعویق افتاد. وضعیت دانش آموزای  بقیه استان های ایران:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/26065" target="_blank">📅 17:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26064">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k9GSPLgMeFWrVXQIRK_txz8po4nUVXjs1IHNyXEj4bFAcDhTyPgvkWLcKKGYQo9XD_vrJwureN-aESBRE8Y2LlL2iuXxNza674tRvyqhG4Fv5mN2sDZYOGt2jmZH9myEKNYhV7kNnv5cWNTD5ragrr8CXRCb1lgd2DJpodOiNoqXaoP9jOepnmEQjfZz7MCYAj9Dq6AOpSl3u17-ov6UGtPG2F5SHu6q5cfDSx-sMH-UUKX6IRCxXQnTLzY7jh_0tK36Y0HaOLS4mnBRJfSFXQwoL2O1ZmJoiNTYelnnwMHtTTySK0OsWsvpSMgD7HhQBEaaXTQYxPeErK2cJks8Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیگ ملت‌ های والیبال مردان 2026؛ فقط یک ست خوب و دیگرهیچ؛ پایان‌تورنمنت برای شاگردان روبرتو پیاتزا ایتالیایی با یک شکست ناامیدکننده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/26064" target="_blank">📅 17:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26063">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3d2e6f73c.mp4?token=ZQDogpn6Ot2u7M_-o7g10FzbHsyGiRALJQ7AIFrVclfDtpMUoA2iCSLsSYqtSaABdmc1VdIN6aIfLBOJM63V9pfBO8Q10GqDH_IE-iCdbbqb_ajn_1ORlgZmCcXKM7K4oeH69pDeAvQpf-B7JkTqGYLp_eSsu1SLARulkRwfkzm9bAaN3e7M5JfvgLTPu1ZzOwVF9jW8vQyJllhh8crPb5sghjxYtSBCws02yyUquEjh1F7UgYNGPjbHDJn6dfdVxs3pYdcSk40ImOZQaRIiudvm9xDVvVG3Xg2Pca-PwJWxt_pz5gIYMmddns_qtwiNROTZUh6oHG5O42z1dMTwQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3d2e6f73c.mp4?token=ZQDogpn6Ot2u7M_-o7g10FzbHsyGiRALJQ7AIFrVclfDtpMUoA2iCSLsSYqtSaABdmc1VdIN6aIfLBOJM63V9pfBO8Q10GqDH_IE-iCdbbqb_ajn_1ORlgZmCcXKM7K4oeH69pDeAvQpf-B7JkTqGYLp_eSsu1SLARulkRwfkzm9bAaN3e7M5JfvgLTPu1ZzOwVF9jW8vQyJllhh8crPb5sghjxYtSBCws02yyUquEjh1F7UgYNGPjbHDJn6dfdVxs3pYdcSk40ImOZQaRIiudvm9xDVvVG3Xg2Pca-PwJWxt_pz5gIYMmddns_qtwiNROTZUh6oHG5O42z1dMTwQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
مسی و آنتونلا ازکودکی‌و‌ازسال ۱۹۹۲ در روزاریو باهم آشنا شدن. بارفتن‌مسی‌به‌بارسا ازهم دور شدند، اما سال‌ها بعد دوباره به هم رسیدند و در سال ۲۰۰۹ رابطه‌شان را رسمی کردند. آن‌ها ۲۰۱۷ ازدواج کردند و امروز همراه سه فرزندشان، یکی از ماندگارترین داستان‌های عاشقانه دنیای فوتبال را رقم زده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/26063" target="_blank">📅 16:59 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26062">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jPig2bHYIA_oVYZ8zkFUMBbd_CU8I6Uhf8HGl1vkXXgEx7PHOjge9gqOOPUTYx_HVsevQ_z47r6ttoyt2iMWXlDB-sij_m9NdHHlJP54ibNLsCKnIXdHYu9cgEJI5g7oRDfL7klyKuf-5Mpt6AVxLlnCoBF8EyXmJFgn3CEmmcCbETPWngjV9b1PYuTcrC7orSf-ZYcybnY_Lk05xgakF7Bqw5wit574KNOSQjbA1inE9PDh2gpa1dkuXnZRCT5uj9fekeu7PDYm4wVJURIYJwTx7lVVJ46QitjuwbvTCzd5vk5_FGnqGuX2sI5GXZX-fA_-B_MeXth6HLFFJHkcsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیگ ملت‌ های والیبال مردان 2026
؛ فقط یک ست خوب و دیگرهیچ؛ پایان‌تورنمنت برای شاگردان روبرتو پیاتزا ایتالیایی با یک شکست ناامیدکننده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/26062" target="_blank">📅 16:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26061">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H5AP4m1_sfXflA4kXw94EczXWyzD0vRZ8H8d_IWALMItZo1Sh-AbB5E3O567_Eg_TBUQbgnNnOaOjfQRnwi-8wnYA9bbXJMRf52OM2Nv446k23442i_oXUPGWTUEBZXAkyNncB-pj3ByuetV9qy2WJ9cTLQwuJ_YKPamHHnTAfbC2fi4hsLGYySKT7DH591C0s7NCV9A_q-5akBSZ_4Fr0NpFqXATzdFpxFEin01X9kDB6d7vbcbvup6iPTwpuIifIWnivZfrmTQLcTmu_Fb8sYybuZ_peXAlkOpLw3Wnv2E4k0VtMm-gUAsZvhk1Wnq7At7aXgzz3Q7rMaXscsjJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
طبق‌ اخبار دریافتی رسانه پرشیانا؛
به درخواست مهدی‌تارتار؛ مدیریت باشگاه پرسپولیس با 3 مربی‌ایتالیایی،اسپانیایی و ترکیه ای در حال انجام مذاکرات نهایی است تا یکی رو به عنوان دستیار اول تارتار در فصل جدید رقابت‌ها حضور داشته باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/26061" target="_blank">📅 16:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26060">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WtKvvST_iO-5oYQdVlrr-eGNy_6ylc3R8mi17pFKfHELfBem8uqSN_Gk-91v-vFT16RtPmhd509Own9VTV2qfsiW8oO26PZDwRa4AXblblSlxTeW1brTB8Il0vtr56kVxD3ruLN_Mpl7Vfj3wQP3cVZ3wjMPbyScdhq1X4m8wgaVpW401Z45IL0jGEXFLHoFL3xRwMcPTnxGZzv23vHVy7gzHtrDJVuOzNnyF4MSDX604IQwfFCGATc_X0WcPik5XVb1ApUn4cFkAoIWy_mXRBaIMDHAsatlkcqn5u4MLzr04jKbET7M2meBqf44aVizFchv2kvNDATu5QuB64Rvbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خوزه فلیکس دیاز: وینیسیوس جونیور تصمیم نهایی خود را گرفته و اعلام کرده بعد از جام جهانی قراردادش رو تا سال 2030 با رئال تمدید میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/26060" target="_blank">📅 16:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26059">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=T-G8rrxHCfC7bYvSuJsEpfO4upoqTm5JgkMV78_AVTc81IFz9PFVxCQ-HBRELVPagvz-PvPgS9UdjlGDzlneSrIi8d7AMKak9tlQwGXuWkk9pYM8zYp8cfE0qsYDs30-0xkq3OuIZU_-did5xAJBRdcfwC6gkEE9-ClG81eu67Xi9RLiLW7KC9MUBWusAZeO6m1JhMd2qx0iitOLP5IacT2Ds3T7b2O0jZPrw2TaJryKKYzuAd3mJCTV3QpzP4EjexOYs3JqN3L8Le6X5QcrgCGb7BJoIbtxOpilI57a9tTlfQ0XNmO8P4q9u8k536eR_isT_g_ye34lAlS0D-AGTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=T-G8rrxHCfC7bYvSuJsEpfO4upoqTm5JgkMV78_AVTc81IFz9PFVxCQ-HBRELVPagvz-PvPgS9UdjlGDzlneSrIi8d7AMKak9tlQwGXuWkk9pYM8zYp8cfE0qsYDs30-0xkq3OuIZU_-did5xAJBRdcfwC6gkEE9-ClG81eu67Xi9RLiLW7KC9MUBWusAZeO6m1JhMd2qx0iitOLP5IacT2Ds3T7b2O0jZPrw2TaJryKKYzuAd3mJCTV3QpzP4EjexOYs3JqN3L8Le6X5QcrgCGb7BJoIbtxOpilI57a9tTlfQ0XNmO8P4q9u8k536eR_isT_g_ye34lAlS0D-AGTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔵
باشگاه‌استقلال‌اخیرابدون‌مجوزو مدرکی 80 هزار دلار دستمزد به اوزجان بیزاتی مربی ترکیه این تیم داده‌ و بیزاتی چند روز مرخصی گرفته بود و به ترکیه برگشته بود که بابت به همراه داشتن این پول بازداشت شده و باشگاه درتلاشه‌ مشکل رو حل کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26059" target="_blank">📅 15:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26058">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rSlL7SyqnHBc_iL8R2i7V0-nb_xj7HsGBwW6rkf8ORY6kD2W43vf7-J7Wb6-D7SUZrHA8nMjUyFDlOvesxwQ5FN9ouCJdHRDNgPvcmIa4vPUWJUxlriQHvjFigYftBlpI2DLSlyIRsFoGw43TxAr_LCiS_6hVh1iu-RqIKYevZs8IXevXcddNdZ2oO3_bbZIusnnKW88aMgOQqkRjrOYZWgFKbmgiQegVnnhcPO2PAZIT1RMgfqK6KP41HmqW_T_y9ez3i4Fgd5QLM4Fc0ORnjA2v-8BjkYZwBfWuAIitwXT02S7-FEpgY6q2kl_vtZujbJ19Jt-VJLujJ5IFqXIkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
باشگاه‌استقلال‌اخیرابدون‌مجوزو مدرکی 80 هزار دلار دستمزد به اوزجان بیزاتی مربی ترکیه این تیم داده‌ و بیزاتی چند روز مرخصی گرفته بود و به ترکیه برگشته بود که بابت به همراه داشتن این پول بازداشت شده و باشگاه درتلاشه‌ مشکل رو حل کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26058" target="_blank">📅 15:08 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26057">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B91YROEHNLnfIduZRn_kme7z5OTgty5xrR-9mib-WyIpL4L1I4R-m1c44rS9h3omOuhfz4JUAGGKBQMxq9uimdil5qSTp7bH-JWBRwO9hgQWswuAtBfWG-Yr9mC3YouBIn0hohdWdU1yO-8xbqrFIOa7FOmxgwtOd63yLsWQ39m7NgxSEA5t50LF2wjjbftPijYzJOxNBZ4CgTdkmxo-peBta-ypP9ClAyDun6Wfl8MJop7b9LeYbgsh0aBXBxXWCtlmLsMNyQFkBnU_z8kwF05vSf-I1ogudEJjkYHCxgHYE719aTC6SJmS776jRHKh75nlAl981wPT1_FvkcNPHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی #اختصاصی_پرشیانا؛ اگر اتفاق خاصی رخ ندهد؛ محمدمهدی محبی با عقدقراردادی سه ساله به تراکتور خواهد پیوست‌. تمام توافقات با او و باشگاه اتحاد کلبا امارات انجام شده است و به محض پرداخت رضایت نامه از او رونمایی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26057" target="_blank">📅 15:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26056">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebd306e48a.mp4?token=TBnPraA64vBmJcOEB6l0etkBnm18dw0HfW1YJD3BNpGGqO7nLQEy76ZGP_s6RYzoG14ghfrwP2x0pUfNTicuQgPBFopCBWUpXicUG2u9Ki_DZyiVQVaxliIGn-COLB8NN0IkoQlUYBHM42PoEz_y4cGthmWKvdZJ3xvRTWbhVH6AUjtbe_djjUCNoNX82sk_WjoSmaeXmaWtthpEQcsxIBWuhw75rKDrsMffmAN1Dc_GSwB4T4GEf5OPUpz-mdOZPCo3uHxVKj0A6Xrm1QjKL0mBEfbagCL_F0df_H790na8wSfiZwUPwnGihuiRbw3RIXKgwNQPiH0op1QhXPCoug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebd306e48a.mp4?token=TBnPraA64vBmJcOEB6l0etkBnm18dw0HfW1YJD3BNpGGqO7nLQEy76ZGP_s6RYzoG14ghfrwP2x0pUfNTicuQgPBFopCBWUpXicUG2u9Ki_DZyiVQVaxliIGn-COLB8NN0IkoQlUYBHM42PoEz_y4cGthmWKvdZJ3xvRTWbhVH6AUjtbe_djjUCNoNX82sk_WjoSmaeXmaWtthpEQcsxIBWuhw75rKDrsMffmAN1Dc_GSwB4T4GEf5OPUpz-mdOZPCo3uHxVKj0A6Xrm1QjKL0mBEfbagCL_F0df_H790na8wSfiZwUPwnGihuiRbw3RIXKgwNQPiH0op1QhXPCoug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏐
از تاثیرات جام جهانی فوتبال بر والیبالیست ها در لیگ‌ملت‌ها؛ دریافت‌جالب بازیکن‌تیم‌ملی آرژانیتن با پا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26056" target="_blank">📅 14:42 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26055">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e509ae8f31.mp4?token=tyto-oDoCPGvSGsAKHq2D0oxzSEibO-yD1RTPxuvm5AllaN3tRpigLC__1uSGeMKrBwaeGB1MkMyYehbX9InXDiVUhPofH_qM4tqiFEtmSKVtXSYutoWNg1OVs1uvVsfOIIRR_LoYScUy4uG4Xbwn-eIzYudK-u4agCjYJ1UpQYYvJmZxmMXwggYlxJgPatpeIeQsTSteWMkZVjwO1-RZTDT4wDXwkCkOIzJ2B5TirJdLJlGv45_e6cl60gxV_AdaNSs8BX4Aqvb7BoyuE90pq9jloq9Su4T2keBW0m4RL_N33AmksGAETdUkwedtQ6Vb1lar5HyTEkXVM70R1q3_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e509ae8f31.mp4?token=tyto-oDoCPGvSGsAKHq2D0oxzSEibO-yD1RTPxuvm5AllaN3tRpigLC__1uSGeMKrBwaeGB1MkMyYehbX9InXDiVUhPofH_qM4tqiFEtmSKVtXSYutoWNg1OVs1uvVsfOIIRR_LoYScUy4uG4Xbwn-eIzYudK-u4agCjYJ1UpQYYvJmZxmMXwggYlxJgPatpeIeQsTSteWMkZVjwO1-RZTDT4wDXwkCkOIzJ2B5TirJdLJlGv45_e6cl60gxV_AdaNSs8BX4Aqvb7BoyuE90pq9jloq9Su4T2keBW0m4RL_N33AmksGAETdUkwedtQ6Vb1lar5HyTEkXVM70R1q3_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پله همیشه می‌گفت زیباترین گل زندگیش رو در ۲ اوت ۱۹۵۹ مقابل تیم‌یوونتوس زده! اما از اون مسابقه هیچ گونه فیلمی وجود نداشت. حالا گوگل با همکاری خانواده پله و با استفاده از Google DeepMind، فیلم این گل رو ساخته. این ویدئو، فیلم واقعی اون گل‌نیست؛ بلکه‌بازسازی‌مبتنی برAI و اسناد تاریخیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26055" target="_blank">📅 14:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26054">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fQI8l03la-NHpsjNGCpLrveutLxdPnTUE-oc_BJcs4wrQ5BncDkKWuCLUrFgwVZYgbJBDpXxYmDCwI1QbasvzjayFvCoR6S68y1ldpJ3U7LT0TK9iyFVytYgyNrlzzT6whuzTbDoiQdiOkRYmF-poRSu0gT8hHiEo-XFCszHYRDeJs6s6DLd3r69jHe_yZeh5_sGOk0AgqKe8AV2Qbym66qUdG4y4LX75ZbQNtvjJ_kgtONhpJrmz3NxTxwCl3acPc0fGBeQQvRHityiAkMzTb4R39YV9HjOkDNvHIaVVpEWcN_YaQAWhPYUehJoVEoqLhpLRecxFl42TA9Y8l9dtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دریک رپر آمریکایی اعلام کرد که؛ این بار روی قهرمانی آرژانتین 5 میلیون دلار شرط بسته. تا حالا هرچی شرط بسته‌بود برعکس در اومده حالا ببینیم این بار درست در میاد یا 5M$ بی زبون هدر میره.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26054" target="_blank">📅 14:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26053">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h8LJ-2XG-FgQDr1U8Xvtvo_R4LeehIF-wYae9fGQdMjQPv3kH1Qq8YShcs4jij8kUTeaf_w0WGFGg3G-UaCiMzpumalCH5FuP9ta5w-aAU7w5NVypXsBQupLKWpp6wT-_FgwMSCrHMORkXCOKVQg--z8-bnMxmjozcIq-QFDQpIyBh98qw6sgCD2cY9rUlLqzuMJbce7bRqJu31pDnTE8VCsElkSo8uGGM0G7GgljU2QZgPZbSOBxkJ8CoID3zSXwubKKa9Tnz1a2KeuFl65yRHd1rqjxZerFh0Tagu6ou3k6-XmRXAcoeLWttH_JyOcfhemiOmpV8xmsT3WhP-_fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#فوری #اختصاصی_پرشیانا؛ سیدابوالفضل جلالی دقایقی قبل‌ازطریق مدیربرنامه‌هایش به پیمان‌ حدادی مدیرعامل پرسپولیس خبرداده که فردا صبح برای عقد قرارداد وارد ساختمان باشگاه خواهد شد.
‼️
حالا بایستی‌صبرکرد و دید تاساعات اینده باشگاه استقلال برای تمدید قرارداد جلالی…</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26053" target="_blank">📅 14:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26052">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iGS7q50XkgBtNvhFxEsTtQwFntRnEjd_inPiPUHWnf88tHkDsLiFhvkCIopO857BcqXCHpRl2BjYzuDGkvE4OWHU-ZoeBA53ydw_nwyaFTFSDneaNph7riNNA-VOY4PCDX-NfXDLiCEprURM-Cj-6afE0x4qmmEANhf_sTJDQtwaR5BPbY2Neo96vp_lmxqxwE0hvLK-Mo5Oy57puiqwIdte0bvkrK3G7fA_TvhsJmyKD6rYDG3BYNsNykXCpxISlgcWI1jmtpgLSRdzgISmdU9A11nefJF7_x-57rQAqh1npYs_HV0oSc12r7_nvn3h2xsTx3Ahmj9LmIhb-q9m9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
شرط‌اصلی‌باشگاه پرسپولیس برای قرارداد با ستاره‌سابق‌بارسا؛مدیریت‌ پرسپولیس با آلن هلیلوویچ گفته که‌مامشکلی‌برای‌عقد قرارداد باهات نداریم منتها قبل‌قرارداد دراردوی ترکیه بیا چندجلسه با تیم تمرین کن و اگه کادر فنی تیم اوکی داد قرارداد میبندیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26052" target="_blank">📅 14:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26051">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P-1ige4AZsco701gaRb5xUnpzIV8oIVTEDbRn7HSJjRQtaSPsvDvvwK6h5lFhtgiMGOOEYCSls4PdP6WF1MeTfp-whUiO3WnoUhKOwtvJ1KH6lOSanyTrE6Tr46OmpmnTLr71Vg_XHpfIYhWIEX89rfDgRnAV30YcgyjNtHPtJZbzVmj83uby4UZYb78ev-sDZOMyNcQUw6EwryZkzz1FHlF0M7d6YXkNlfzxc75tid7Cpu6jC3N76iLG-1Q4SJqjHnhJAsfnbvF21vivSz5x9WXqt5RbhIjogx1EZcDmN2eOVTIt3y97_Tw23x3wZzqnd6pIzLKGVGfje1rEsduGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
طبق‌اخبار دریافتی‌پرشیانا؛ مدیربرنامه های رامین رضاییان شب گذشته به باشگاه استقلال اعلام کرده که این بازیکن مذاکرات مثبتی با باشگاه لگانس اسپانیا داشته‌است‌اما اگر رقم قراردادش رو افزایش بدهید ظرف 48 ساعت آینده رضاییان به ساختمان باشگاه خواهد امد و قراردادش…</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/26051" target="_blank">📅 12:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26050">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lsT3eQPvg3OpveJAU6Df6SyF4iXV4m0w1kimweoxppbLL9d7IvVFZOU8HcmqpkMuYW9ypLE_Nc1-nf4TF8sV1vw7pCMPfPa6wlVzTijX5TV0DSTtQbC6dW4SfG-HtDiaGFoAJ5boRg4fctNEZ6j2rE3Nq70Z7tps4Ij97pAq3WZTGZVk34raxz3p7WGCMLsRID6StzM3td1e4Ec81Ou6lfDx-IULO5vQYvwP7DDwcT49p5JGdhx8FeCGa5BKU5fKjkl7rrJIwuFvls-a48vEQ1ZnJ_K6nlwedpgDEtgTYI1B-tyWijq7I6q64tHQ21azr0bpkCVHX--E2jTjyy8MEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
🇦🇷
#تکمیلی؛ نشریه لکیپ: فلورنتینو پرز قصد داره به محض اتمام جام جهانی پیشنهاد فوق سنگین خود 200 میلیون یورو برای جذب مایکل اولیسه به بایرن مونیخ ارائه بدهد. بعد از کارهای اولیسه پرز میخواد انزو هم به برنابئو بیاورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/26050" target="_blank">📅 12:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26049">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kM6n1A26u4wlak86I7Aigwb_ldwUvopa7GRNx8aR27_jc2UpJ4T9cBu_lnAnLNLeAvuOEnLUjVPrCRrtIBpHEAYa2JaeNF5RgTQHRAEmBIQabOU7x9gFTEwAWazoib92w0tjs-7eldxdfVhAi2ZC8jdVsURdOPhPohDqe31wVkDJ7xXN40I2pD9v2s5ylb-ANIyj-Ta_pwiIjWQ1eT19uiDsuSi816EnmWZkZzyLO9LhN_1B1okWjGOLUt89clOL5M7XELOX1Rt3-_vO1G5llqCJq2qVsqOsfIAZnzA-AutSWCXhCy-cjtyRsQgALIGr9FvmzKKIl1j99TdWi5bFyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
کلارنس سیدورف اسطوره‌باشگاه‌آث‌میلان و رئال مادرید درکنار همسر ایرانی خود؛ سیدورف فصل قبل بعنوان مشاورمدیرعامل آبی‌ها 250 هزار دلار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/26049" target="_blank">📅 11:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26048">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gidhc8t5B79ZhXwwZ2aOJuc6Imkuoc6UPdOloymQ7qzXCY1YaVurJbtd1ppxffkoGQ_jFaF76tFb4EKHa7qTtKkqjs-Hdz4HxhQon9raNJ9cWuxd3UtGroaa70kBMiF9xBAf9PFY1TYCUVUhyxnSCk2FZiF4Dm5ML_XnjpXuC2ajzN9rkDsJ6Yzlz2wz4zl5IBa6HjFbPa6mMk_VZRIA5Qat6IYT-A22-q-K8T8YlxZhdu5xf-XtfD4sSIOHopWKIetwEwwUQCgv-T16rr8Oi8drn8yTGN5rflQ4QYYNLA-1i5SevB15iOktdkZh1nx9tG5CmDi-gtGcKA5fedPOFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال موافقت کامل خود را با افزایش 300 هزار دلاری رقم‌قرارداد یاسر آسانی اعلام کرده و به مدیر برنامه های این بازیکن گفته که یاسر آسانی به ایران برگردد قراردادش رو سه ساله تمدید خواهیم کرد و پیش پرداختی یک میلیون دلار به…</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26048" target="_blank">📅 11:28 · 28 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
