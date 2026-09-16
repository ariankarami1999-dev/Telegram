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
<img src="https://cdn5.telesco.pe/file/lqfnATbmRtCiMl6RavzFZ4ffRXFUOPzN98sckN0Wh96DUrpH70Xfcieq6G0qYroBBf8IHti4GUDH0Xjj4rx27zRjkBaEwbrid7FM34JRYFrgrzllY_L8iHuu20UPux02ijM4wOw28U8rGojtZ4QidRUFHxN2HXIPSOmvi19Smi1koMM5jhIjDalsKJ212qshhP975QyuwZBFNZQ7tx4KAdlsu5x2sPLIIXaSUEfpSMWLeYw4JWFdI5C5N011vWPphvNPbEpFZFUYUZI2fkfhmQ1mpTgqE-r1KD2xrXOuQ48jVSrKVDLWaC_UN1EZAHNXg8RTSdCnO6pY8NTu5n8GUw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 411K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-25 22:28:37</div>
<hr>

<div class="tg-post" id="msg-106690">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ayR4LEAySbhDXZWryVolP13Xs41Gv6xxyigOUZi6c8ge1TMwMdy4vgg8H0RzXBLSj-t0l_pP26kg5YXL1pZZnA53VGNEuVMGyQs3fOz_DM9PiVHy-ozs4wp7ponQKkxpywbb7KoOjAYK4GwBLOz-YR6fmm3GD4BRQ3mxMdv8H58T3a9AbKUEx02vRR8GlVp8RK1_gjcxTNk3q2RmB8TyqbpntQLu6LVFhr_S8R7cCE1l4hFOpDy2Zs3w59yTJQhlf1gsDMf8t8muTmPq0aWV6ThZLDvFg1rqw80BOAjJxdsIphkFxjQgrZQSR6kt8gSnEqLd3Q41zH77rypjkvhGjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
شماتیک ترکیب بارسلونا مقابل ریسنیگ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/Futball180TV/106690" target="_blank">📅 22:19 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106689">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wCEaKuNMDWcWIQToRvBHLSdg7GICsSN0pS6Y5AJ2o1w_pq3odeWjWMQ5Ohy6goigOTaeSlYuAOp-D2TBOz_mgDOKWkR9lqsHqmDNeCh2Gl3AoJsOWWEyMZaOSFJM7qeU-Gatl3CCVLdBa9RRFG051ywuQvzefB3jnPLv-67rCqubAFYaDgZl7U708FgEE261LmHqMBqMXd4s2tyJ5zN89sKBsLqkx3xh12fhcmJPJNAOqgkdbABcgWGag1HWXOaCcH7RHNg8rEd9LJiL9g-gXVINkFVfT5pqNyuTuu3BtbhDgoGphLlDWM3zbw_OVdoPb3QuX57-FHduLC9U8G4bRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
🇮🇹
🇵🇹
لیگ‌اروپا؛ ترکیب میلان و بنفیکا
⏰
ساعت 22:30 شبکه ورزش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/Futball180TV/106689" target="_blank">📅 21:23 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106688">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e46b13203.mp4?token=gmtRbKlWLDSsZolzNVnr_cjA6SZfN4BpWKpz6awm4qnvbvw4pzSwZk_qoAHZEHA6XUD-kbAv3GPEb8N3jM6caZrGUxZ9A4BHS3Ng9Qpwf5mbhzeol6g2MLgWOXbqDMc4nlUeLW288WEC6vbzFFEdBpYI3QTRM67SJ-GEJoypn-SunaTeTzFR1ycftFOynuLMaecXYoJY7TR3x7mgNJ9oMc1VV39Z-pIIWLqydzcXYPE_atqus-MelmWSQvsufb3Uihb5T1ZL2daKFTPlJgy9lp_rOe_NPuxe00T96BMRMWpr0S6piSazVeP5IqOEgayKqboaxJ-qmGZivuXqmfeBag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e46b13203.mp4?token=gmtRbKlWLDSsZolzNVnr_cjA6SZfN4BpWKpz6awm4qnvbvw4pzSwZk_qoAHZEHA6XUD-kbAv3GPEb8N3jM6caZrGUxZ9A4BHS3Ng9Qpwf5mbhzeol6g2MLgWOXbqDMc4nlUeLW288WEC6vbzFFEdBpYI3QTRM67SJ-GEJoypn-SunaTeTzFR1ycftFOynuLMaecXYoJY7TR3x7mgNJ9oMc1VV39Z-pIIWLqydzcXYPE_atqus-MelmWSQvsufb3Uihb5T1ZL2daKFTPlJgy9lp_rOe_NPuxe00T96BMRMWpr0S6piSazVeP5IqOEgayKqboaxJ-qmGZivuXqmfeBag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😐
همین حرکت دیشب رونالدو که
کیرشو
میگیره، تو ایران خیلی وقته توسط بازیکنان انجام میشه
‼️
پ‌ن: واکنش رونالدو به شعار دیشب العینی‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/Futball180TV/106688" target="_blank">📅 21:17 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106687">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2943ca3183.mp4?token=XcYzOE5owmskFVgRKd3cVDCOwOCo7kwr4b0Mj9q7qK3aF-BChPfwjGizRT8neIxtlt6vB7Oktxl5eGdRjYgkwzFAph-pb1HvUbo8OBmRkm9WfIyVrIcBXgkIKiBSFTUOSoTsX16gqvJ_1GD8SfozYnszGdWKgJlh9TstmvsrBnowtlDbozlMYIJOftp4bTu-x7zOt9daMKLqb37TCjvJ3ZV3qpV8Xn8OlG-38sCLwCXldkwaKEtg4ZO66aF0hU6O6_lQMeQW7mRVv_xgRTxbIllqjpZm2w01PH7VKJ9MM84w2TqLhm3BXyQ8j84kLwNf9ErM9KOvkPskMSTkQABM_TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2943ca3183.mp4?token=XcYzOE5owmskFVgRKd3cVDCOwOCo7kwr4b0Mj9q7qK3aF-BChPfwjGizRT8neIxtlt6vB7Oktxl5eGdRjYgkwzFAph-pb1HvUbo8OBmRkm9WfIyVrIcBXgkIKiBSFTUOSoTsX16gqvJ_1GD8SfozYnszGdWKgJlh9TstmvsrBnowtlDbozlMYIJOftp4bTu-x7zOt9daMKLqb37TCjvJ3ZV3qpV8Xn8OlG-38sCLwCXldkwaKEtg4ZO66aF0hU6O6_lQMeQW7mRVv_xgRTxbIllqjpZm2w01PH7VKJ9MM84w2TqLhm3BXyQ8j84kLwNf9ErM9KOvkPskMSTkQABM_TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل اول اتلتیکومادرید به اوساسونا(جاناتان دیوید)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/Futball180TV/106687" target="_blank">📅 21:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106686">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13f3f55505.mp4?token=cK9XfjnXHRxz3az8rPPVm6WfxmvYRBn1JhWdeC4ocrCkPVEeMPIsXHhYlf75lZLYTqZtxiGfj7Oi4xUTZsxVca5i0xDSpDXEaSPkKrtUtRt42yzyDyY883-f8qG5grM0xWxqR6MdoZvV2ma32pWw_c4H4d3D63WqXHs2m-J3Ic28z0N4LqKOh5fwm6hV3j3lsD8nBb12FEbeUvOPE8dsuUTuPOoEIa-GLjF5zMZzxpnGZpPpSZ_zRXPHrfHAFWsTtvMeoJWyfCRypgbHv1BDQ3xlqdtpZCivvJXiHP-cY5dzPouUWYKgl3JdLhR8dJe-zGnVSomnAXWY_e7kh8SZ4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13f3f55505.mp4?token=cK9XfjnXHRxz3az8rPPVm6WfxmvYRBn1JhWdeC4ocrCkPVEeMPIsXHhYlf75lZLYTqZtxiGfj7Oi4xUTZsxVca5i0xDSpDXEaSPkKrtUtRt42yzyDyY883-f8qG5grM0xWxqR6MdoZvV2ma32pWw_c4H4d3D63WqXHs2m-J3Ic28z0N4LqKOh5fwm6hV3j3lsD8nBb12FEbeUvOPE8dsuUTuPOoEIa-GLjF5zMZzxpnGZpPpSZ_zRXPHrfHAFWsTtvMeoJWyfCRypgbHv1BDQ3xlqdtpZCivvJXiHP-cY5dzPouUWYKgl3JdLhR8dJe-zGnVSomnAXWY_e7kh8SZ4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های شنیدنی و جالب علیرضا مرزبان درباره زنده‌یاد سحر خدایاری یا همان دختر آبی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/Futball180TV/106686" target="_blank">📅 20:15 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106685">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f63c731d.mp4?token=MQToTnjHsir4meya3mlVB_GH1HU5_DOvi3sM7i8ab8ARzK8FbtVo2OCLcfOSW1kpO6tP05sxQs0P88A6BkqIGcBHw4fv1VYvuUDFd4zLXFI-_e7L1ZocGNgceXoc1ntWyMeQnLjMlbh_XxW1MmpoeO6VytdctcmLaG1zsTYu5u3YF8xpJwSgOuD-551vK0dHB0cHmyUB8lHw69HgzF2SAfWW3zEIWFgWTq45VmJlt84qO0adxWHE5zXYkFKYV4nM32_auTmv8vXuJ4KhpdMaOYt_eUBUeaIAzPo9ZPjTa5cBUOPZPhbB8gBxQxnAoWAs-_mRQ0Ip7dLrLxcefasP3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f63c731d.mp4?token=MQToTnjHsir4meya3mlVB_GH1HU5_DOvi3sM7i8ab8ARzK8FbtVo2OCLcfOSW1kpO6tP05sxQs0P88A6BkqIGcBHw4fv1VYvuUDFd4zLXFI-_e7L1ZocGNgceXoc1ntWyMeQnLjMlbh_XxW1MmpoeO6VytdctcmLaG1zsTYu5u3YF8xpJwSgOuD-551vK0dHB0cHmyUB8lHw69HgzF2SAfWW3zEIWFgWTq45VmJlt84qO0adxWHE5zXYkFKYV4nM32_auTmv8vXuJ4KhpdMaOYt_eUBUeaIAzPo9ZPjTa5cBUOPZPhbB8gBxQxnAoWAs-_mRQ0Ip7dLrLxcefasP3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
📊
ترکیب‌رویایی قلیچ پیشکسوت فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/Futball180TV/106685" target="_blank">📅 19:45 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106684">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bac1a39777.mp4?token=qKfcwgJIxj9FDEJdvUP-wZpjaQwuBETCAlUM3h_E_AVkfFTyKzlBwGDuQR6H-H7T8tvr5OZFCoWSZ2S29S1YYoXTRoBVyFSYZWzHuWBL9ey2wXav8mq1d5uWWMSH9dZmsWEzBSSco8ilLTIDAlIP0CaVhKVRWI-CZsnmjCQiFFJ-_GO5s--0Qoz6ZFrffPf0PLDVdCm_IxIlq01sa37lKhwdnGRFoP7zJ6uIl8-siLeifT00oBkV_cMgZlXXzzziR3A-Sow7iTNFSgB8a84oBrVtixUkBWnKKljjPkj-43z36mr4wEPU18kVYjFjyLXI043sHdVmhhpJuRedH7x0ol27weBj1sl0BcIbuLwOTWl8ad1mXMywOR3978sPCTAu4wXMYmDztzkLBxXOlmxyjPdumZch-5Ncg5vfVa0TpcxUPw7pYxp3WIHW0uaYA6oFlay5-solruVu6yhRuL4wWM0t6Y7tLKC0bikQA5vyd7lkFziMTaNe1UU-tpMc7QVL0t0f2J5BdH0C-PNs08885FRt-RFF62R8vHcWEgbY09-miCZxUswFhs30k4qjqy2MDfSMTDM0KRZH1Y-OJt6A_vAzDDbPjrhHFsrJjHQ0gg0qRX2yT73EqJo0iPd8u2SZAeVsiXZgxlx3I2xEWeonOkTgwNew2jH98vdI6QzUjTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bac1a39777.mp4?token=qKfcwgJIxj9FDEJdvUP-wZpjaQwuBETCAlUM3h_E_AVkfFTyKzlBwGDuQR6H-H7T8tvr5OZFCoWSZ2S29S1YYoXTRoBVyFSYZWzHuWBL9ey2wXav8mq1d5uWWMSH9dZmsWEzBSSco8ilLTIDAlIP0CaVhKVRWI-CZsnmjCQiFFJ-_GO5s--0Qoz6ZFrffPf0PLDVdCm_IxIlq01sa37lKhwdnGRFoP7zJ6uIl8-siLeifT00oBkV_cMgZlXXzzziR3A-Sow7iTNFSgB8a84oBrVtixUkBWnKKljjPkj-43z36mr4wEPU18kVYjFjyLXI043sHdVmhhpJuRedH7x0ol27weBj1sl0BcIbuLwOTWl8ad1mXMywOR3978sPCTAu4wXMYmDztzkLBxXOlmxyjPdumZch-5Ncg5vfVa0TpcxUPw7pYxp3WIHW0uaYA6oFlay5-solruVu6yhRuL4wWM0t6Y7tLKC0bikQA5vyd7lkFziMTaNe1UU-tpMc7QVL0t0f2J5BdH0C-PNs08885FRt-RFF62R8vHcWEgbY09-miCZxUswFhs30k4qjqy2MDfSMTDM0KRZH1Y-OJt6A_vAzDDbPjrhHFsrJjHQ0gg0qRX2yT73EqJo0iPd8u2SZAeVsiXZgxlx3I2xEWeonOkTgwNew2jH98vdI6QzUjTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⁉️
🇮🇷
سورپرایز تاکتیکی سهراب بختیاری‌زاده؛ استقلال چطور السد را زمین‌گیر کرد؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/106684" target="_blank">📅 19:15 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106683">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be6891deda.mp4?token=kVUIYD2Sfozh4uAf1Gg09wQVRnQFYN7gV1zzwarKvQ01RVeU17XGjhvQoXJaZsay69jZRKNrrfR1zg-3e3HwMho5w8qVYmfXb_M49LSc3mX330VGVn8rhy6Yrv_KGQfZHSRhiGAd-3EVwkjUHM6iJrGi9CRKf-kFIWlXy99jarLaqIGgdoHy9kcXaoHgCPyy7lnG1zkNC7FoyQS78DvD_FDPGpcAeio51n5yDKmubST6xQOtxA_ZuTT2Vx2BsrSH80zmunLMT8oy9ZSRBK66YiMrkZdWwpWre0yNR9DutnhocjOQ5nmtAY36mIFNL2dac-_zCAlR5UUPVUTTR98VfrezeebFio7UXa2WCqX0bjv0BrMp1Mc2uuK9gtCdhvq-GmBtzbcQiA3XIfcrulsjoWgM3jpttgWGEzcBOQv2_QS32pQEmCHj4yFiCdPgZL72O93isV8WL140kOIyqqQVrsb5TiFMKmgCR8T8LHBKa3Fz9r7qenVxpUXY2RaJOmO81x-4w6klLh45M9Y0_EUPQhLLXL4S8OPgHKMI9wYfczE8Fsapl_xUjKQo9ujqAIVN142tBWHbxbyrttcy9WZY_Za9_IhskdtPpChJhR6mmQfoexvn8EXdQ-rVxuEq-vUOpCHLjONupyq0DxOXmRLVkGY4kzQfcupeCX032RW5DkM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be6891deda.mp4?token=kVUIYD2Sfozh4uAf1Gg09wQVRnQFYN7gV1zzwarKvQ01RVeU17XGjhvQoXJaZsay69jZRKNrrfR1zg-3e3HwMho5w8qVYmfXb_M49LSc3mX330VGVn8rhy6Yrv_KGQfZHSRhiGAd-3EVwkjUHM6iJrGi9CRKf-kFIWlXy99jarLaqIGgdoHy9kcXaoHgCPyy7lnG1zkNC7FoyQS78DvD_FDPGpcAeio51n5yDKmubST6xQOtxA_ZuTT2Vx2BsrSH80zmunLMT8oy9ZSRBK66YiMrkZdWwpWre0yNR9DutnhocjOQ5nmtAY36mIFNL2dac-_zCAlR5UUPVUTTR98VfrezeebFio7UXa2WCqX0bjv0BrMp1Mc2uuK9gtCdhvq-GmBtzbcQiA3XIfcrulsjoWgM3jpttgWGEzcBOQv2_QS32pQEmCHj4yFiCdPgZL72O93isV8WL140kOIyqqQVrsb5TiFMKmgCR8T8LHBKa3Fz9r7qenVxpUXY2RaJOmO81x-4w6klLh45M9Y0_EUPQhLLXL4S8OPgHKMI9wYfczE8Fsapl_xUjKQo9ujqAIVN142tBWHbxbyrttcy9WZY_Za9_IhskdtPpChJhR6mmQfoexvn8EXdQ-rVxuEq-vUOpCHLjONupyq0DxOXmRLVkGY4kzQfcupeCX032RW5DkM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚪️
توضیحات مجتبی‌پوربخش درباره فساد ۶ عضو ارشد فدراسیون فوتبال جمهوری اسلامی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/106683" target="_blank">📅 18:45 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106682">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83fb9dbe46.mp4?token=Fr6pRAGcF1D0okJ7YQqHoK3DxV70bAv8sCGpFTtd6JoCQYxvSYl0afquZ9MPoRfDYWe7BbZBlexNB1Yi2F1924485ICFFNqE9ZIFUUO5AAuSbZ0rr1EashpexbJS4cCVVWnKuOAX7zcjX9h032xYEWD58FIrvKW6Kt04xEgqOdubV3W0TiluW5iM6rNEHXCLpm1qavqTVczcOMOmjQC50JhnW0kToF3M6Gniu8nBKXiw2c1HR16XPtXj3NKbhotXRv_ddPA7vszls-b3Ajas4DU1ajlgNE01mQz7zbj2Wt4rgrp1lmBaUuHTsI5DTVa1phuVU7UAXadDPF1Mpa2Z0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83fb9dbe46.mp4?token=Fr6pRAGcF1D0okJ7YQqHoK3DxV70bAv8sCGpFTtd6JoCQYxvSYl0afquZ9MPoRfDYWe7BbZBlexNB1Yi2F1924485ICFFNqE9ZIFUUO5AAuSbZ0rr1EashpexbJS4cCVVWnKuOAX7zcjX9h032xYEWD58FIrvKW6Kt04xEgqOdubV3W0TiluW5iM6rNEHXCLpm1qavqTVczcOMOmjQC50JhnW0kToF3M6Gniu8nBKXiw2c1HR16XPtXj3NKbhotXRv_ddPA7vszls-b3Ajas4DU1ajlgNE01mQz7zbj2Wt4rgrp1lmBaUuHTsI5DTVa1phuVU7UAXadDPF1Mpa2Z0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
قائم‌پناه، معاون پزشکیان: اگر بنزین را ۸۰ هزار تومان کنیم، می‌توانیم به هر نفر ۷ میلیون یارانه بدهیم!
❌
پ‌ن: ۳۰۰ تومن یارانه دادید، از ۳۰۰ جای ما دراومد، برای ۷ میلیون چه بلایی سر ما میاد ...!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/106682" target="_blank">📅 18:13 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106681">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106681" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/106681" target="_blank">📅 18:12 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106680">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iqCc7aX29mdBWpCFswGSJNy6SuZegjbpCG23n897y9lgvwXvndmccDANszfBZMPbjRgLdx-d9M_iSY-b6coWrMEF3llVULvSkrJb8raHiIjbNrM_W-mqnnc6xSc5t2HfTGGh-vxeupUcIWt-IVb_rJGLYZ-42y5AVQQCD33rMBHFX51uRfAGhtgKd_EB-pPJKU7hh285NeDOvH5vZt7-O8IUBN942F6nubsgtYzO9PCseYv3irkMZqAx4OSUDBY2Yo32186w6O7ZvxuWaXUZmCiIxuLZAP29l35088sW9qyO5ldKKSkVcSsjkd461cw0JfO7Ix6NHm87h-ab5T0PBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد هیجان انگیز
⚽️
راسینگ سانتاندر
🆚
بارسلونا
⚽️
را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار دو تیم در ۵ بازی اخیر:
⚽️
راسینگ سانتاندر: ۲ برد، ۲ تساوی، ۲ شکست و ۹ گل زده
⚽️
بارسلونا: ۵ برد و ۲۱ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/106680" target="_blank">📅 18:12 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106679">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rKaZlNDLcx9k17CYJvPi7i38_YEbIYgnrsoPIWKC62aSOnWNbAkdJOaIi69mH2AdJlZxgoMaPspH_3W1ordrFTtJNTbNX9lihOO6OrLDC3ZcjzRX1KUgSCxyk1F1ObUbCjbHtQnIfyPurrfbF0ISuHVtL0mI1ZiExi-4F8vFIJ2TKemQEFs2w_PmUsfs7m3JKya4zP53k-sk1fq8AMceXA0suV-jWZrZEHt_4QxqvVf-_DKr7WdnO7Oaxm0v-Wq33zFsOUpAYW91rrC8pSF3DmgHflGj7G0tQkHfKex_VTLDvw2OixdPnfj7EdPLOrCHdMx9aDroNC03uY9lZE1R0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
اعلام زمان‌برگزاری سوپرکاپ اسپانیا
نیمه‌نهایی: ۱۳ و ۱۴ بهمن(۲ و ۳ فوریه)
فینال: شنبه ۱۷ بهمن(۶ فوریه) در استانبول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/106679" target="_blank">📅 17:53 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106678">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gVlBGFpNGAZ5pEs5WSruH6lCcEFrD5Oxkw1GyWHfcHcUGalqKgcP0RV_vHx3vtQN0uzpGXMCw5XSaHsZOgZEvdGe4R_B8ShL3i6RLjdNoJmRSf4HuVVAJjXPefS9KeBGx72Ikuf5uZY7lqAwUCCrMIFlUXxEWIWwzPRhn4RxtmheviKuy_VY2pLH_Uirs66cwdXdhxrUW3cfWwhRRk-zLKLcqnRvai6V29ytjtF1RoDdyhD4lW0C7qgh6M-bXnpdVhugMUPQGMq485JtkFRWW0VOJISAe9jEoFTANH6q0roYNsoGQ0cK8f_TPAein3XvANKcMbXnT6D5vmHFPkhAHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
مقایسه افتخارات ۵ نامزد اصلی توپ‌طلا!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/106678" target="_blank">📅 17:45 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106677">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15009e843d.mp4?token=YFKZhqQnosnzmQQBXg2O5CLXgJR665R9zayYfyomvrQxQWFV8P4HAxHFOa-bGeEjDjD5XoMo3_pwIltM-1lmercv2D_DWp519UhHhGppe9BjC-lkiPdI0yKVw38l6x--jenubqriEc2FmmJqRR8KEHiIOuGpM7ylI2sdAota3b2mWtNaqbM5TXKdxFm46oXjbncicWsN_CAxdfiQzc0CUQ8v2XqP54czFMOmSkSD_0TOiEns3nDwuyX76_tNRU-FSHhG3iUcSMukX1RI_b4JdgJY0tM_7ulVF0ShowIrXBrDnoAC_aqegLeSGpGBjJ0WArkca6tAqeDD--1i0jzeMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15009e843d.mp4?token=YFKZhqQnosnzmQQBXg2O5CLXgJR665R9zayYfyomvrQxQWFV8P4HAxHFOa-bGeEjDjD5XoMo3_pwIltM-1lmercv2D_DWp519UhHhGppe9BjC-lkiPdI0yKVw38l6x--jenubqriEc2FmmJqRR8KEHiIOuGpM7ylI2sdAota3b2mWtNaqbM5TXKdxFm46oXjbncicWsN_CAxdfiQzc0CUQ8v2XqP54czFMOmSkSD_0TOiEns3nDwuyX76_tNRU-FSHhG3iUcSMukX1RI_b4JdgJY0tM_7ulVF0ShowIrXBrDnoAC_aqegLeSGpGBjJ0WArkca6tAqeDD--1i0jzeMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇵🇹
واکنش دیشب رونالدو به تشویق لیونل‌مسی در ورزشگاه العین امارات!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/106677" target="_blank">📅 17:20 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106676">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/268cfcdc63.mp4?token=nyWVofO6FROmDg6tpYLsLMF3GKhqYY6SYK6R79mC0K9h_opBPNecCj5wrHYkqHUzxFP8S5PsYoxmYEwwP43a2D2FKL2mFRMWU1-7RbM0LCPq6t_cmOZaPneOIsjEY-FUHGylrncja4qdVjJN4TwT9r9IQ44PmaIE72x0rEalI5bt0wpYRnDIuBgl6rFeDp1UEpDG_N2YW5BmOhWC2SmjGcmBemGHCZgacj8SN1pdltZ4Qy3JCDKLgI0lQGqwZloaTLdQzVH6xWkhHRsAKqiHSBSHH6LN6yZITfR28omc95BV4qnZ7e3Fe3rg-ZrrzQ2WO8r27IysowC_QAHQjr2Clw96SWPh2adfwUtre9YjVlaCwRMoqkdVAozDUB4UOAOZxN9P3ZI6ZM7Ckd81EBIeo_obH-RykQbRrt2NGGSbaDvJnjKtaZ2iuOouYL2LJfdGjVi0MNFE2rAGM5A5Qs275r8po8_shBN3khCGQwJnHJ2Nmx08tktMN-Ve7tw1aHP2GKggMnyEDWbKVEZnHU4RZJw1mNVxTE5nLdGRRWnc1EUdmO9smhicZRoxYbVCbtTTgG1n1k67z2wjXM_cxb6XHp1osMpXUeERjnvDSmLKwYyqFyWUip_j1tbzd1raYZEfNnBJaXQI0hQfFed-xACUG_39T4QDcKyH_1ceAiYEkIY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/268cfcdc63.mp4?token=nyWVofO6FROmDg6tpYLsLMF3GKhqYY6SYK6R79mC0K9h_opBPNecCj5wrHYkqHUzxFP8S5PsYoxmYEwwP43a2D2FKL2mFRMWU1-7RbM0LCPq6t_cmOZaPneOIsjEY-FUHGylrncja4qdVjJN4TwT9r9IQ44PmaIE72x0rEalI5bt0wpYRnDIuBgl6rFeDp1UEpDG_N2YW5BmOhWC2SmjGcmBemGHCZgacj8SN1pdltZ4Qy3JCDKLgI0lQGqwZloaTLdQzVH6xWkhHRsAKqiHSBSHH6LN6yZITfR28omc95BV4qnZ7e3Fe3rg-ZrrzQ2WO8r27IysowC_QAHQjr2Clw96SWPh2adfwUtre9YjVlaCwRMoqkdVAozDUB4UOAOZxN9P3ZI6ZM7Ckd81EBIeo_obH-RykQbRrt2NGGSbaDvJnjKtaZ2iuOouYL2LJfdGjVi0MNFE2rAGM5A5Qs275r8po8_shBN3khCGQwJnHJ2Nmx08tktMN-Ve7tw1aHP2GKggMnyEDWbKVEZnHU4RZJw1mNVxTE5nLdGRRWnc1EUdmO9smhicZRoxYbVCbtTTgG1n1k67z2wjXM_cxb6XHp1osMpXUeERjnvDSmLKwYyqFyWUip_j1tbzd1raYZEfNnBJaXQI0hQfFed-xACUG_39T4QDcKyH_1ceAiYEkIY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
روایت مجتبی‌پوربخش از اعطای مجوز فوق‌العاده عجیب کشف معدن توسط فدراسیون کشتی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/106676" target="_blank">📅 16:55 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106675">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17d14f705b.mp4?token=jmvLv435hyuFicjTOisctJVym63_3LWgikVk_kkPJq2j9FhegL5eUy0zdtpkbDcTSDr8FPI1RwTUglPY-Nu5cMnWrZPPPILujcqHrt-d6oR3diFnejGio-lUvlMb4_tYRJ3AP7jziObIrRswUJ4hsFF4S3rVPFRg5zAjk1M1ixqgLsBtVyfXpIG8opZB-bcXv54i0KpzR-KKjb82je6CR1JoZBnVvEDJ1JQJoo5amN8A6g3r56Sk0ecbz4cL5QBbG3dRIPOQ3IXHjFR-cUPj7_g2BCAe_MwunzGHjO1rnW89xlWq0zbt_HO39OKqlnCvm3nKp4GGTEZ1Zu_A7b--rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17d14f705b.mp4?token=jmvLv435hyuFicjTOisctJVym63_3LWgikVk_kkPJq2j9FhegL5eUy0zdtpkbDcTSDr8FPI1RwTUglPY-Nu5cMnWrZPPPILujcqHrt-d6oR3diFnejGio-lUvlMb4_tYRJ3AP7jziObIrRswUJ4hsFF4S3rVPFRg5zAjk1M1ixqgLsBtVyfXpIG8opZB-bcXv54i0KpzR-KKjb82je6CR1JoZBnVvEDJ1JQJoo5amN8A6g3r56Sk0ecbz4cL5QBbG3dRIPOQ3IXHjFR-cUPj7_g2BCAe_MwunzGHjO1rnW89xlWq0zbt_HO39OKqlnCvm3nKp4GGTEZ1Zu_A7b--rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
سوپرگل توتی در یک‌دیدار دوستانه در ایتالیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/106675" target="_blank">📅 16:35 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106674">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vE4e40ZMlzF-ae5C587XXWH_YT6Avmwfq1_1QiEuj6HvC_Tvd3IbzNj0JTG_UbWhc2VU1C_o9eO6pUtVfZ-bE016nAlQEp-xACxS5eSJtVJwY90vNw58GMbRfDAfZgeQ7SxHGVLeh2jFyllSQOTKCn-4MBCKsXRtr914-OAx76LZWaF6R1aZVME-ao0kpUWRdNvj-0hW0rgR9Iuf4buEVqUZg8PxzzreRSpu4m1MyznNtUKz_fTFpbTnN4IaMQBOXjhbSugZvV4_RO1QUgrLzSXgvAG5jBqHLVFq2qpdIkgFfvV_JIj2pC5RhaRbojGgl4EHniBSTZzGNNa_WuoOuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
✅
مصدومیت حبیب فرعباسی سنگربان استقلال جدی نیست و این بازیکن به دیدار روز ۱۶ مهر مقابل تراکتور تبریز خواهد رسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/106674" target="_blank">📅 16:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106673">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21bbacd491.mp4?token=VddpEtq94Xc70fjqQ1ubr8JMs5HFe2SWGfiOiaDtTr9pbCIRqytd57g_qJ61JJYAqPIc26X0mviTbBuwA09nPnAk6CVocriBHj28zI4Uitfm24Jbk6IxXikQZkQ2H-2fULiZqYdzs5BzT4D3chwjJskfWBCW7IrsXzWdnsyDb19bxi8Yevig5CrcMdsqn16XXL5Zz8QgTybX2-bpUNhni4JK7fM-d1LHfY7bo9MsdwGsY91OVuN7wNJkOmH_P0aKc7BVOKGf7kiBiM0SX4Az7Y6XoJv204_lf9UOwMjsSqDoUQxMsFUhtDlIw2aDWMRlXTh6OoeN_N-qSujxZCdsDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21bbacd491.mp4?token=VddpEtq94Xc70fjqQ1ubr8JMs5HFe2SWGfiOiaDtTr9pbCIRqytd57g_qJ61JJYAqPIc26X0mviTbBuwA09nPnAk6CVocriBHj28zI4Uitfm24Jbk6IxXikQZkQ2H-2fULiZqYdzs5BzT4D3chwjJskfWBCW7IrsXzWdnsyDb19bxi8Yevig5CrcMdsqn16XXL5Zz8QgTybX2-bpUNhni4JK7fM-d1LHfY7bo9MsdwGsY91OVuN7wNJkOmH_P0aKc7BVOKGf7kiBiM0SX4Az7Y6XoJv204_lf9UOwMjsSqDoUQxMsFUhtDlIw2aDWMRlXTh6OoeN_N-qSujxZCdsDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
👀
صحبت‌های عجیب و بامزه پارتنر مهران مدیری در سریال مرد سه‌هزارچهره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/106673" target="_blank">📅 16:05 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106672">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6760fc381b.mp4?token=FcqwL663wYBrYcWuY3s6cVVw3gznNolO8IViwuWCZc5so_vJkSwIUF2GK_tKZmmS70bJJDhULJXYjC216wbkPEMl6iQBxZLpFiER3xuO5U501aiMwsBeWIUqHc0hhSCoO8Co51fr3zx6y6m3HLY4fCjlqzuMb-xl-Qio36iMqIl3rEZ_z_7FekzGudoiW0HG9efNhPNifhVn1WVLpvb2ftu63dvaQWfiyLY0VMvGJzSwqzJq_N0GCl1N5JQ6ZcQ9dQcM8tzGw-RmsvH-fPz04cRrNQRjeHudUCW5CAiF1nF5LJpKyLbSy1ZiDCZERZC-Ye6AR8FapN51w1tzcKOeww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6760fc381b.mp4?token=FcqwL663wYBrYcWuY3s6cVVw3gznNolO8IViwuWCZc5so_vJkSwIUF2GK_tKZmmS70bJJDhULJXYjC216wbkPEMl6iQBxZLpFiER3xuO5U501aiMwsBeWIUqHc0hhSCoO8Co51fr3zx6y6m3HLY4fCjlqzuMb-xl-Qio36iMqIl3rEZ_z_7FekzGudoiW0HG9efNhPNifhVn1WVLpvb2ftu63dvaQWfiyLY0VMvGJzSwqzJq_N0GCl1N5JQ6ZcQ9dQcM8tzGw-RmsvH-fPz04cRrNQRjeHudUCW5CAiF1nF5LJpKyLbSy1ZiDCZERZC-Ye6AR8FapN51w1tzcKOeww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدیو از استاد آریا بام رفیع دبیر زیست کنکور تو چند ساعت میلیونی ویو خورده و خیلی وایرال شده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/106672" target="_blank">📅 15:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106671">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c4e1abcd1.mp4?token=bvlmcf5CphRrUq8SxZLjiqPOU5qck4_0PHqzlZnoZzyafCq24yZLcWnDAFMDS0SqnIdbRkE1kfTSbL6Nmj2sWP83ie1KRUss5wXiQulumWk_vqC5WkzQtC1wSRG8MMt5vfpmrO5T6K1fKt3yHJE0Q74MpgMQFg7-VvSYaaTVls3os6BDCluoCGWcvwcF0JV4i4bzcCKN1PhfBxlwISrG1Cdm3yvU2j4pfiCB6u5dLrSaOi1FdFtU3Fh01odEocS6WBx69lBQKqLvb-UXYRyi9GTG3Wgo-bKH9JujEMxNEKhNxYcBq6y7E4blBJTgIxB_UcOJIPrfGMGOw_bOupYDUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c4e1abcd1.mp4?token=bvlmcf5CphRrUq8SxZLjiqPOU5qck4_0PHqzlZnoZzyafCq24yZLcWnDAFMDS0SqnIdbRkE1kfTSbL6Nmj2sWP83ie1KRUss5wXiQulumWk_vqC5WkzQtC1wSRG8MMt5vfpmrO5T6K1fKt3yHJE0Q74MpgMQFg7-VvSYaaTVls3os6BDCluoCGWcvwcF0JV4i4bzcCKN1PhfBxlwISrG1Cdm3yvU2j4pfiCB6u5dLrSaOi1FdFtU3Fh01odEocS6WBx69lBQKqLvb-UXYRyi9GTG3Wgo-bKH9JujEMxNEKhNxYcBq6y7E4blBJTgIxB_UcOJIPrfGMGOw_bOupYDUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇺
هانسی فلیک: چه به عنوان مربی، چه به عنوان هوادار بارسا، در فینال چمپیونزلیک ۲۰۲۹ که در نیوکمپ برگزار خواهد شد، حضور خواهم داشت.⁣
❗️
خبرنگار: لطفا به عنوان مربی ...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/106671" target="_blank">📅 15:15 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106670">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a617f5cf34.mp4?token=UMRkY8e4lyLe75mbKN_ESGgPsMzXPRSIfS4HI-MLBooRXBOVGCF44KAsD0ukM6qxaJuh4vLqdhHXEc-GYoUHgwf2iVHg3qK7AuvKI5RL4Bl4hB90bSLmtgQIm-rG4dsVPA75O30Y7t_PVKRamlJ9DkRsOJwGKq0oJCbgfRuqFfK3hj-cR4vS7IXv5tFggxf1f7r9R34WiJ_-ft2ZexXS9bduv_O7BsObuxuPm9RQH-3C5l-iau8K0jIMALCfk3Sqau3fWAALZ4dH5nz3siqnL9R79iv4SvPQBVX7UZPcuy6OXQPCA6jBz6JjOUadr2tqk8z7V7Gr25bFQm2NiXN-4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a617f5cf34.mp4?token=UMRkY8e4lyLe75mbKN_ESGgPsMzXPRSIfS4HI-MLBooRXBOVGCF44KAsD0ukM6qxaJuh4vLqdhHXEc-GYoUHgwf2iVHg3qK7AuvKI5RL4Bl4hB90bSLmtgQIm-rG4dsVPA75O30Y7t_PVKRamlJ9DkRsOJwGKq0oJCbgfRuqFfK3hj-cR4vS7IXv5tFggxf1f7r9R34WiJ_-ft2ZexXS9bduv_O7BsObuxuPm9RQH-3C5l-iau8K0jIMALCfk3Sqau3fWAALZ4dH5nz3siqnL9R79iv4SvPQBVX7UZPcuy6OXQPCA6jBz6JjOUadr2tqk8z7V7Gr25bFQm2NiXN-4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
صحبت‌های هانی‌رامبد درباره ضررهای مصرف سیگار روی بدنسازی و عضله‌سازی؛ حتما تماشا کنید بسیار مفید و کاربردیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/106670" target="_blank">📅 14:50 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106669">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c4b40a7a1.mp4?token=e3Gd3WXFNFCtAGLcWA0KOJ6mI5prKxclQ_WpjNHQ2kQG6QK8B_Tru-hSeM5VzOf9wv7IgmjD9nMs7gcvWF2uM5Y_PYOQHWLWSjAI-GY8dIl93FE-LyZ74jyjUwmcJKCnIWllUT8Iua9QKDuQ8PLaZdTfvfsDZxJVZXeqAMbqIkCA6T6kAsYNjk5cN7tCQsX7VfkpYLtjAtL2o-CVWyMleSQ8777qpWwS-Fd356NKLCbNW-SHtiFUHWfzAlcKe_fpPgg5LeFdL0arJbFTQp7QUoG2ozBkkGJrifTE-2MrSZJpN_H94DPqKIVKGXfgmnXFtfrawYyAFR2EX9vn2txWujzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c4b40a7a1.mp4?token=e3Gd3WXFNFCtAGLcWA0KOJ6mI5prKxclQ_WpjNHQ2kQG6QK8B_Tru-hSeM5VzOf9wv7IgmjD9nMs7gcvWF2uM5Y_PYOQHWLWSjAI-GY8dIl93FE-LyZ74jyjUwmcJKCnIWllUT8Iua9QKDuQ8PLaZdTfvfsDZxJVZXeqAMbqIkCA6T6kAsYNjk5cN7tCQsX7VfkpYLtjAtL2o-CVWyMleSQ8777qpWwS-Fd356NKLCbNW-SHtiFUHWfzAlcKe_fpPgg5LeFdL0arJbFTQp7QUoG2ozBkkGJrifTE-2MrSZJpN_H94DPqKIVKGXfgmnXFtfrawYyAFR2EX9vn2txWujzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🇪🇺
🇪🇸
رودری: قهرمانی برای بارسا دست‌یافتنیه اما بارسلونا مدعی اصلی قهرمانی چمپیونزلیگ نیست!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/106669" target="_blank">📅 14:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106668">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce8dcfc377.mp4?token=GL-ZgV-ssGnp8nJ_g1xr3TeqUWkgkUA0qdIqMhEtYhoCNUCMmyhBsRcVDpXdnouqnT9Hpdsu_M0eHtJHJZOEsgMrFy7psY09e4BRg6MHv-xlRjfLTTAZyF3mJE9vqlsOsQWxvS_1FFEs-4pqfUfZW-Ry1MJB1DpY5SJpu9hCg_FKDe1MWKM2qYpfecWDwRVTNfoGu9dby6RUR0EOQbCiDBTIwrcCle4ZDldht-UEND2OIIM947t_Uikdy8qn2Pl7L4bIPdcbZi7hGl9LzpUMbYFEX5qsLBBD5caFI5CKEmZzyW7Nn3FxBE14f8axMEvfE4w8dOw8tGb_Bxho49lARg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce8dcfc377.mp4?token=GL-ZgV-ssGnp8nJ_g1xr3TeqUWkgkUA0qdIqMhEtYhoCNUCMmyhBsRcVDpXdnouqnT9Hpdsu_M0eHtJHJZOEsgMrFy7psY09e4BRg6MHv-xlRjfLTTAZyF3mJE9vqlsOsQWxvS_1FFEs-4pqfUfZW-Ry1MJB1DpY5SJpu9hCg_FKDe1MWKM2qYpfecWDwRVTNfoGu9dby6RUR0EOQbCiDBTIwrcCle4ZDldht-UEND2OIIM947t_Uikdy8qn2Pl7L4bIPdcbZi7hGl9LzpUMbYFEX5qsLBBD5caFI5CKEmZzyW7Nn3FxBE14f8axMEvfE4w8dOw8tGb_Bxho49lARg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
شوخی‌سمی رودیگر با تدارکات رئال‌مادرید در بازی دیشب مقابل الچه
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/106668" target="_blank">📅 14:04 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106667">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NrVGw4mWFHqLvRJ6CGXiwil_MIQkTACs3545HiNCAaX_gp1FpJS1oW9blDHfTC0w90QZ-MHZxgHhqh01atlf1ysin3qIQoz6AspP1Rvw8geWSLtvtfAd_g3YMO1hk9YL5eeAnY0fBokSknn0XhocA8QcdpBid0rqCSYm2PR3o-xjXSM1fNG8RxvNT1RhlVEouDUSsLsrF9-Afm6aGqBHJI0PGzpj6Oxx765dYTRZpCCAYy_FgYC_JMX6oGllinYRNkC41GWO-wbkNT9d9UActGMYvMs5BOCcWjqoPnJk_a4UgP0x50yLigAwAJMKcL_fgJMn07NLasZa5Jf8TIOEAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
📊
لیدز یونایتد تنها تیمی بود که در میان تیم‌های میزبان هفته‌گذشته پریمیرلیگ، به پیروزی رسید. تیم‌هایی مانند لیورپول، تاتنهام، چلسی، منچستریونایتد و استون ویلا، و دیگر تیم‌ها، نتوانستند در خانه خود به پیروزی برسند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/106667" target="_blank">📅 13:35 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106666">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d150b918d.mp4?token=Dxtj2faxxpKQBiec_LlxqvTnidrRCPFXJAIkzsH00zePRPzo_jdYAcWJuLECDWBPzAQ7SwsE1MaBKQ9acUVghHs9XwKQ81mwuNCBJ1mo1T8XOm-KaFhWlSet_4OpqKv_NSeIqYxebb9jJgx5FMwOOqNDCjpOUtlotWoYZPBnFVTC-my94_Sp07tLeSfbe3QMpSDp96nReIO7F7E4qDnZ0LR78JdctbjI-DqeKdwkemz-b2_N-6Riae5PTaPCqKzYVqvahCA62Pbm1PIxPmhHQ2nQV_lMAuSCYV1n3RBfqFawzSwExItxGT92k-a0XsnUmbquicvR7Xsnvf8Af0XO400I5NLMVSRGknaRULWProfT1PNZtefNQmikgc2hR8BX5iYRS-6-kZkTUQ4Bh4BeNEAu4AeNBbPESGFv0fZELjVDRonVqWW9w4MFzPDWsxlQjSwF_OYH6G_-jadi-p80QVub29GXYfLyFL7EnqwukE-lVm5DhPo2n1M6FY9eAvYuf0Qger9gOyoZ2KscxNMrGC8bDeoiksVyslAyBoCqyq9W_pWyd3Y5cYtthtpr-Vq2VZvExO-SbpeJ7r1yWicdL7sl5C9fUlu8Q4Zy62SqrPK28QjQcR7Z-ThwpbzssZTp4HXWc1I13vgqKijHR9lTm4Ze_TEOwIEn4NZd0Ev24dU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d150b918d.mp4?token=Dxtj2faxxpKQBiec_LlxqvTnidrRCPFXJAIkzsH00zePRPzo_jdYAcWJuLECDWBPzAQ7SwsE1MaBKQ9acUVghHs9XwKQ81mwuNCBJ1mo1T8XOm-KaFhWlSet_4OpqKv_NSeIqYxebb9jJgx5FMwOOqNDCjpOUtlotWoYZPBnFVTC-my94_Sp07tLeSfbe3QMpSDp96nReIO7F7E4qDnZ0LR78JdctbjI-DqeKdwkemz-b2_N-6Riae5PTaPCqKzYVqvahCA62Pbm1PIxPmhHQ2nQV_lMAuSCYV1n3RBfqFawzSwExItxGT92k-a0XsnUmbquicvR7Xsnvf8Af0XO400I5NLMVSRGknaRULWProfT1PNZtefNQmikgc2hR8BX5iYRS-6-kZkTUQ4Bh4BeNEAu4AeNBbPESGFv0fZELjVDRonVqWW9w4MFzPDWsxlQjSwF_OYH6G_-jadi-p80QVub29GXYfLyFL7EnqwukE-lVm5DhPo2n1M6FY9eAvYuf0Qger9gOyoZ2KscxNMrGC8bDeoiksVyslAyBoCqyq9W_pWyd3Y5cYtthtpr-Vq2VZvExO-SbpeJ7r1yWicdL7sl5C9fUlu8Q4Zy62SqrPK28QjQcR7Z-ThwpbzssZTp4HXWc1I13vgqKijHR9lTm4Ze_TEOwIEn4NZd0Ev24dU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇵🇹
عملکرد ضعیف اسطوره رونالدو جلو العین!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/106666" target="_blank">📅 13:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106665">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a01bac8019.mp4?token=rMTyxDnT9bAEmyyiDAKfJkixJhIsbUdkfZRAAoXxMX-4BIk92HzLVPDAZc7WY2aAaQcDv93rCxFRh5loQmiM0baG0qIVy2YCdgXYjU8_2iJjo0fr0K_DiwoEpPdpWWyW8fPlIyezx0m8023xa-CvNzf524ouVFey5h7jyLZVkm-oYbrjNyY6IXusmMBaqPFklOb22-WZIL77JHNcAYdRZFFdLD0GvzIhh5K49vaZ725O8r-9i0UruvaTjnqX5rWA_2ek55tiGO_y94PhghMbl6KzBlnnHyJvyTmyF8B6nVugEzgNTLVfcFSBoyxdVa2BXDW_KyMHGBPT5Y8J0ARb3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a01bac8019.mp4?token=rMTyxDnT9bAEmyyiDAKfJkixJhIsbUdkfZRAAoXxMX-4BIk92HzLVPDAZc7WY2aAaQcDv93rCxFRh5loQmiM0baG0qIVy2YCdgXYjU8_2iJjo0fr0K_DiwoEpPdpWWyW8fPlIyezx0m8023xa-CvNzf524ouVFey5h7jyLZVkm-oYbrjNyY6IXusmMBaqPFklOb22-WZIL77JHNcAYdRZFFdLD0GvzIhh5K49vaZ725O8r-9i0UruvaTjnqX5rWA_2ek55tiGO_y94PhghMbl6KzBlnnHyJvyTmyF8B6nVugEzgNTLVfcFSBoyxdVa2BXDW_KyMHGBPT5Y8J0ARb3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار از علیرضا منصوریان میپرسه چون الطلبه مشکلات مالی داره این باشگاه رو ترک میکنی؟ اونم در جواب میگه: اگه تو این روز سخت تیم رو تنها بزارم کم لطفیه و امید هوادارا به منه و نا امیدشون نمیکنم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/106665" target="_blank">📅 13:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106664">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfbc375b35.mp4?token=FU-_WbLJU8VhfrHs_1sUwTRoemcoP8kehm3pyrjsPJINATx1ukcbPAujHd9quFug3jJN8TKvqE-W7lC6tZeU7LK6Tdub5fOmHbHGp65G7qk52qLBIrO9uRNT4X8uxaZ0YB2atotXd-reLv3X6VKgO1u66OX4sFNVBiUILGoGvNEW-f5i4aZKLjXomrz3A2Dsido_WYear0F8PX1XmmZEqikEHZemOBM_ysQA50g_d8fGIKDEYJG7rOQQTdyHbErHOb9-0BYZzTc3dc3aLJ9DuMrGy-XV7my-SGPmW5zKwRwYRO6kg1bmRtZA8EscOuhMA4H65_wykVTfaTR6LRQrrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfbc375b35.mp4?token=FU-_WbLJU8VhfrHs_1sUwTRoemcoP8kehm3pyrjsPJINATx1ukcbPAujHd9quFug3jJN8TKvqE-W7lC6tZeU7LK6Tdub5fOmHbHGp65G7qk52qLBIrO9uRNT4X8uxaZ0YB2atotXd-reLv3X6VKgO1u66OX4sFNVBiUILGoGvNEW-f5i4aZKLjXomrz3A2Dsido_WYear0F8PX1XmmZEqikEHZemOBM_ysQA50g_d8fGIKDEYJG7rOQQTdyHbErHOb9-0BYZzTc3dc3aLJ9DuMrGy-XV7my-SGPmW5zKwRwYRO6kg1bmRtZA8EscOuhMA4H65_wykVTfaTR6LRQrrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇦🇪
🇸🇦
هیجان‌بالای گزارشگر خانوم استادیوم هزا‌بن‌زاید العین امارات در بازی دیشب مقابل النصر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/106664" target="_blank">📅 12:45 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106663">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e050d24ce.mp4?token=WZCHgDQh2acCHspOHYCgCyrvyHeu89nOILtZH_Tarr_x9gEUc0GLMWfhSoH4SkHdniVGNsx-MJywP6pFdzwX38U-a27HXrrqTsFR36dnDHIgWMYBPv9e6Rviqfj7xjL9rReCtOpd0ImFH-p4__YUBwCySSkcppfuppo0sGMQpnKBipTBsPH1hVxwn-LXqCNAvnWfbGOgTuGP0ppShSs3UfbEQ7hMFGhygNbDhSLXlDgHTYas1bNd4DVbrLuienmf3nbo5BOB3eEqk2_XnNwuSnryHhT7A4ZQWyj2OFIIk2EV1LIRlRjNChZ5ML_E9GFHqa1zyH5ogPztBiIwwWDNjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e050d24ce.mp4?token=WZCHgDQh2acCHspOHYCgCyrvyHeu89nOILtZH_Tarr_x9gEUc0GLMWfhSoH4SkHdniVGNsx-MJywP6pFdzwX38U-a27HXrrqTsFR36dnDHIgWMYBPv9e6Rviqfj7xjL9rReCtOpd0ImFH-p4__YUBwCySSkcppfuppo0sGMQpnKBipTBsPH1hVxwn-LXqCNAvnWfbGOgTuGP0ppShSs3UfbEQ7hMFGhygNbDhSLXlDgHTYas1bNd4DVbrLuienmf3nbo5BOB3eEqk2_XnNwuSnryHhT7A4ZQWyj2OFIIk2EV1LIRlRjNChZ5ML_E9GFHqa1zyH5ogPztBiIwwWDNjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
✅
قبل از ترک باشگاه چه‌کاری مهمه که انجام بدیم؟ برای دوستان بدنساز‌تون حتما بفرستید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/106663" target="_blank">📅 12:20 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106661">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HC4tR2rKlUBaeu7u1TBft-l_bPjD1AkuQZBgj7wL2lCw8CQ3eCuxAzBmv3U9vYw6z79eQt9C97G2gfluv9evJ2M5ude4nbJ4mgLqcfPsaJfZ-fG23SqPBMJ1wFMH_Zma0ib88DvFnImuHdRHI0x0uLgF7GiCtZesMl74e0rTKi1xSciOHRvsoWnC53EQRmPSBjSkn3GpKZoeecWGvKxCMvrAGz7QfOYlxb7VJiG6a9Xi9Ub1mEeRY9n9L4HLZ6-LQhSFl9PwQ9J9MQPpNEsOHa4T1SUIVDXyktHs55zEjM0cgFnL_LKJHJ-5MazJpCoXCp-mKr6fpaqo--czPaC-aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pz0k2q6k9mx7kf59CrM9PSNPNgn6crgTdxDU3BPPbjcqycDX3OgQiWDlaeOd9UA1gb7aVSEYCE0EmeumO4FEhChjVT_iDnS4X7kZNSMCzlhCPTQdlw4H0FSBYp3BTE1MmzKEjjNDv35L5_EOd9lgBqShofLDscndIy-6TQhfCagaIDfy4iV_8DZ187mhqgBEp03_u1ZXdMNahN__yhCEivpeZvdj0Kl3_IHFHgQOkYwp-koKghWaXky2Upph1EwvZoHBx6io6VJFoR3RkJocr1mSdprssh_5inZeC3_AqdqxljPILdMmCjVoc66IDQ7tg1n64A4r9zDIH3QZLUKHcQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
عکس‌های جدید شکیرا در ششمین دهه زندگیش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/106661" target="_blank">📅 11:57 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106660">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">‼️
🇸🇦
🇶🇦
درگیری شدید دیشب بازی الهلال و الغرافه از این زاویه؛ بن‌ناصر بخاطر کشیدن موهای سامرویل کارت قرمز گرفت و جلو استقلال غایبه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/106660" target="_blank">📅 11:50 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106659">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106659" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/106659" target="_blank">📅 11:50 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106658">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nmnbf4s2u0dHgeeRUoD5g4rgcQHwi_Jcgzpr7U-NM7VK-g3angtBKTvW5uCeNcNyrRfquk_GOOkm1cEJGgoQfnFc4Ic62YkkjCnzwFsn6xcbW0S2ty7JFu5jIo5MUtttsfpJ5y2FLMt5lzw0zte3gQdwqL6sj9ZdSX4ZuU0xFBOJjtNdl5oM035rDZplgH_8M7qmEYK1NQHOuQ_7LIaWPa4hYKxw5GFBJS9GB3JvbhBrurQ2KfAHAsySj8uycj5LWHkfIwEf7vporVJznIAtWqdft912pno-2m9ReV99e9XJ0pnuWoiRYq3AikBmak4i94JkYbVVmcMEvya9sVdo6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
جدال جذاب لیگ اروپا!
نبرد هیجان انگیز
⚽️
بنفیکا
🆚
میلان
⚽️
را در
TrexBet
پیش‌‌بینی کنید!
📉
نگاهی به ۵ تقابل اخیر دو تیم:
⚽️
بنفیکا: ۵ برد و ۱۵ گل زده
⚽️
میلان: ۳ برد، ۲ تساوی و ۱۱ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/106658" target="_blank">📅 11:50 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106657">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qp3RSa0INf1IKRlWK0xPQ4KByasm3vo_w0QKte2s8CT8a-36sSEzLNpIwzVda0Q9scTcaiNPvRnSyw1mOwGptPgFj1z1bJBYDzRrAh7QgqlQ5XWMdRK7w36qpkPF5fdVYRJyVyQxlOC9-RZ1dKGAzvtjP-1Pj1qEPZl0KLICedVOXi1UVhj0fTRwJf0KKkTATHJK4ElK7QqiVR1VLB0BTb2_8e_itn_XUNh_-eH3DXM_1la-GClolpJhck07MUt1YRy8UF5oSxs04MFBreO_xsL-iYtdcko--latbee1Kz9gXSY7TbDaPRg8Vp0pLi6XoKPd2IKKVarvt7qSTI82-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
📱
استوری اسماعیل قلی‌زاده بازیکن استقلال: من هازارد فوتبال آسیا هستم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/106657" target="_blank">📅 11:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106656">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/796caa8457.mp4?token=sPyer2Ewtz1v6gV4okaS_eaxBl5yBDHnwW2GCgJjUaUpewklViqF9E-2nysNjlscbzNgo5GSF2avij1aHe3bfq0xBJ7-gdSIklodynFrhBOvUbQ3MAuvX8a8x0jXAiO5PxMSEEy841C-ssnZyjBHl9Y0dzz3tKJNQUogo2A3cEvRu9LXATYXhb992bj9mKOMht5Zetc6QgQGvnVJigEQszNBMrpIk9YevGSOUc2KaYTzYS3CHsPD-hXRAPajnozQtSq3G3YWPDt3QYaIcnB0QcwjOv8FEhT2xNlL4bUGb3RHQ_veBUcZmtHAM_qSJqhvzRfM8_LCeM6YpK5qF9vtmrYGQZoLKOfVv8FxTArSzSQiyPBmJnjafT2p92kNJVvTxPUjKX8BVuguUcBv03u91U17Mrao_r9Ac1CWRjrmilScSCKsOf_1wmp1nk6WN8q7xL1nu0Lda88e1S5bzA3sfR_Qyb8V7Tpfrfp1teKjkl5S0hDI904fcR_IjAGZ4fvatmZZhn31VCQsT0TnA5ZdGAOYNYhMGn7QD9E0u59PV2KhJhDiZHFVrgm1bePty1bcD351KDybKKI26sq0e5djIQ06B-9EDVemGx9OXqyohKdg7wjssQiYhARKyPn5RuDkbpwUJ4m7wEgQCrtkrbQMbRGPBwq0tFNugF0NAJj2PSo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/796caa8457.mp4?token=sPyer2Ewtz1v6gV4okaS_eaxBl5yBDHnwW2GCgJjUaUpewklViqF9E-2nysNjlscbzNgo5GSF2avij1aHe3bfq0xBJ7-gdSIklodynFrhBOvUbQ3MAuvX8a8x0jXAiO5PxMSEEy841C-ssnZyjBHl9Y0dzz3tKJNQUogo2A3cEvRu9LXATYXhb992bj9mKOMht5Zetc6QgQGvnVJigEQszNBMrpIk9YevGSOUc2KaYTzYS3CHsPD-hXRAPajnozQtSq3G3YWPDt3QYaIcnB0QcwjOv8FEhT2xNlL4bUGb3RHQ_veBUcZmtHAM_qSJqhvzRfM8_LCeM6YpK5qF9vtmrYGQZoLKOfVv8FxTArSzSQiyPBmJnjafT2p92kNJVvTxPUjKX8BVuguUcBv03u91U17Mrao_r9Ac1CWRjrmilScSCKsOf_1wmp1nk6WN8q7xL1nu0Lda88e1S5bzA3sfR_Qyb8V7Tpfrfp1teKjkl5S0hDI904fcR_IjAGZ4fvatmZZhn31VCQsT0TnA5ZdGAOYNYhMGn7QD9E0u59PV2KhJhDiZHFVrgm1bePty1bcD351KDybKKI26sq0e5djIQ06B-9EDVemGx9OXqyohKdg7wjssQiYhARKyPn5RuDkbpwUJ4m7wEgQCrtkrbQMbRGPBwq0tFNugF0NAJj2PSo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
برخی از زیباترین پاس‌گل‌های اسطوره CR7
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/106656" target="_blank">📅 11:05 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106655">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc02fbddb0.mp4?token=bwRUaBxiCoVS9nPodx44PmULUBeKfZRjc3voDS8yGpoAo0IkHPSpcLL24cPcpmHXc5mswQtJq7pZ4XWfDI33eOy3lj2UysKNWL5XiWXstl-m1Az83PHrC9QkKVE_TJYR0SV2moAPEPYENxpbzJfHFJoudcVPHjtcZ1hXbykD8WyYoLHwZi3XRTiVtxz1SXWdz1jCPKuUf-ZLyL02kQ2FUohPPJ1JLJCoao_76VLkSvojB3US2wQ9928V8jqkNjoz612WApqsGnY5Mk7zYP0xlAe9q1AQgqQOwnUTA9DDuG90Fz2mvh6z_ZFxBQloEb0FmgLxOH0wff2GgaxL6VSkfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc02fbddb0.mp4?token=bwRUaBxiCoVS9nPodx44PmULUBeKfZRjc3voDS8yGpoAo0IkHPSpcLL24cPcpmHXc5mswQtJq7pZ4XWfDI33eOy3lj2UysKNWL5XiWXstl-m1Az83PHrC9QkKVE_TJYR0SV2moAPEPYENxpbzJfHFJoudcVPHjtcZ1hXbykD8WyYoLHwZi3XRTiVtxz1SXWdz1jCPKuUf-ZLyL02kQ2FUohPPJ1JLJCoao_76VLkSvojB3US2wQ9928V8jqkNjoz612WApqsGnY5Mk7zYP0xlAe9q1AQgqQOwnUTA9DDuG90Fz2mvh6z_ZFxBQloEb0FmgLxOH0wff2GgaxL6VSkfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🏆
یهو هم دیدی سر توپ‌طلا غافلگیر شدیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/106655" target="_blank">📅 10:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106654">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f24687d0a.mp4?token=oKAoiEqp2jsoUcQ-m6u7Ik48A6BEhfFl6cGTzyqT68XHis91i1Z35Jwfq_i73Yxr6E-GiMcLklIuZ441iFZpvl5qTno8iDYOtURIFXlpg2nGaVSW7vGcyX2YFQanTA10nH5NVpKOBsQ5LY5HsAglCJ4zj4zZa6lPM1dY40A9nspanbh9H44Lsk9Zqs4lxgJnaU-OZLaWrz65WKfCyItfafP9H6I3UDBgLvZFIa4uUTymjuBe-IqnxcLk3O4i7GdXCJrqtEA4aGQXZm9dPdoFaG5WBZ6zzAOYhkL2qx5LLYZRoqQUM2qbfj7NuHpfPegt7lU4oELcBtqgBO49ONpdHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f24687d0a.mp4?token=oKAoiEqp2jsoUcQ-m6u7Ik48A6BEhfFl6cGTzyqT68XHis91i1Z35Jwfq_i73Yxr6E-GiMcLklIuZ441iFZpvl5qTno8iDYOtURIFXlpg2nGaVSW7vGcyX2YFQanTA10nH5NVpKOBsQ5LY5HsAglCJ4zj4zZa6lPM1dY40A9nspanbh9H44Lsk9Zqs4lxgJnaU-OZLaWrz65WKfCyItfafP9H6I3UDBgLvZFIa4uUTymjuBe-IqnxcLk3O4i7GdXCJrqtEA4aGQXZm9dPdoFaG5WBZ6zzAOYhkL2qx5LLYZRoqQUM2qbfj7NuHpfPegt7lU4oELcBtqgBO49ONpdHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
گل سوم ایران به امارات توسط مزرعه(89)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/106654" target="_blank">📅 10:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106653">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/679dc80276.mp4?token=LOr-5fY7ihEPIWtPbQvgCHmm1lTWGY-HKQbHIK8LJzYfazAEFd_1z-0_wH7NN_7EgbCoVQ8LfujgPXSMTo_i-NzmKkiQzkn9VxEhWZGIqBLUAIgzh2ILvFQbPlQ1hP7srNntgBMoqTeDytoiAC78AgJFAE7Bp-UZeYJAhc9PmGVQdobZAa0nqiNvE2_IZ8BrvCYEU59tKj3TeJxffy3CmoT67ixa59Iy3R-zp3Ko7QaoHVTKDNf61T2wTSlhAwUOMwlvnV3nxudEqEwt9NHWocvjyFh74ostjP9YP5cri03aFVCof0PYQnPL1nk4JwXvi1GfuIKzw29k0wdIUtbZ1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/679dc80276.mp4?token=LOr-5fY7ihEPIWtPbQvgCHmm1lTWGY-HKQbHIK8LJzYfazAEFd_1z-0_wH7NN_7EgbCoVQ8LfujgPXSMTo_i-NzmKkiQzkn9VxEhWZGIqBLUAIgzh2ILvFQbPlQ1hP7srNntgBMoqTeDytoiAC78AgJFAE7Bp-UZeYJAhc9PmGVQdobZAa0nqiNvE2_IZ8BrvCYEU59tKj3TeJxffy3CmoT67ixa59Iy3R-zp3Ko7QaoHVTKDNf61T2wTSlhAwUOMwlvnV3nxudEqEwt9NHWocvjyFh74ostjP9YP5cri03aFVCof0PYQnPL1nk4JwXvi1GfuIKzw29k0wdIUtbZ1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
🎙
انتقاد طرفدار همیشگی هادی چوپان از رفتار وی: درس خیابان با ساندو فرق دارد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/106653" target="_blank">📅 10:15 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106652">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eP_bcI_FmXx-ZQxhJftO-v54ds0Ka6DmSyhWMEQCT2HgSVt2ZqMcmRwlkJ5VK7A1Pb7dsi42jk0eBDCazeVPjC1v1EGiRfrslTrVhKfNGra2OCNhU0Kgtqun4_8pYtLeoJh0fyLy7y6p-gte8PsMNjGGf2zMy-UTskjQqF5_7eYbQ9xLOoE86OU0Bhaf-U2lOAtQsquUQOkOjW0e-73dmw-lAKq8WP9TdVSVcq8F8ZfeP1KXGKMBEkW68ZgD1_i6pP2Jgw0OkmvFYIV6tXB0s3WPp-7Izb-p-crwAZXGcVZtpz-maCEMcEdesBZb9kNMg6iRlbO7f-j9jiDZFbnWfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
تفکیک گل های لامین در فصل های مختلف
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/106652" target="_blank">📅 10:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106651">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccc7f1ed9d.mp4?token=cQSkCTRmMg3qsODhz4LjxdJMoe4thSfBz66TCSz-Ds0Arr1Svy7_Sb8Ka7--4-WFTAyOG4NNCTs6y0TQ6hQfwBkuj_KXvSAN5Psy3uW6-kf4RID35qXEf8U2HdPTaHTRRy1V0MGWm6qNx9sUmCx56CQELhfLkjusBjJ0Q77cb3Nim26fXmQzLhzXd74pNDsHPJ4B8NCGiZNWK2QM006Uh2x9q1v6_wuexinpvw8faMniyPq6_huoMuMMT94RgQcmEDWUk9ewJol2jWpNjGATG7G6dKaxAjJYT0YMj9xaZerBxGTRtFvyFGx7nqM0DwPVO08ZnvkmIsYvoEKJoH7HjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccc7f1ed9d.mp4?token=cQSkCTRmMg3qsODhz4LjxdJMoe4thSfBz66TCSz-Ds0Arr1Svy7_Sb8Ka7--4-WFTAyOG4NNCTs6y0TQ6hQfwBkuj_KXvSAN5Psy3uW6-kf4RID35qXEf8U2HdPTaHTRRy1V0MGWm6qNx9sUmCx56CQELhfLkjusBjJ0Q77cb3Nim26fXmQzLhzXd74pNDsHPJ4B8NCGiZNWK2QM006Uh2x9q1v6_wuexinpvw8faMniyPq6_huoMuMMT94RgQcmEDWUk9ewJol2jWpNjGATG7G6dKaxAjJYT0YMj9xaZerBxGTRtFvyFGx7nqM0DwPVO08ZnvkmIsYvoEKJoH7HjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
گل اول تیم‌ملی امید امارات به ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/106651" target="_blank">📅 09:49 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106650">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6962fda1a.mp4?token=dzZzlYuXBFn8Imkvo6O1KamMVcg-G3qjqTcBHM5E3hmMS0jcOXvTXtdlHRchhO4c0O2KqrRHbHjoEBrPsoILW70aFmT8Sl0lkQA-UQHHhdiyNXDCXbkR0bJNqkYha1dF1iZ9d7F0Af7n-zrg7-I72NS6VkKQwE6iiP01Bj2GTruUUSQq0g8tDu8BcfxIowglnoaQI7anc3Vo37xHHgCrAoTHrlExf0Nww3ShNQ4Slxd9-zwi1Jsyqcjn31g6Tv36apNKoNxlpK-s9SPoOULhZ3seKjVLl6-kyyDNg9k-UgFyh_5aFsqeZ-eDDYRQo2wkd6c4WNiJk8kPnTgEpNieTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6962fda1a.mp4?token=dzZzlYuXBFn8Imkvo6O1KamMVcg-G3qjqTcBHM5E3hmMS0jcOXvTXtdlHRchhO4c0O2KqrRHbHjoEBrPsoILW70aFmT8Sl0lkQA-UQHHhdiyNXDCXbkR0bJNqkYha1dF1iZ9d7F0Af7n-zrg7-I72NS6VkKQwE6iiP01Bj2GTruUUSQq0g8tDu8BcfxIowglnoaQI7anc3Vo37xHHgCrAoTHrlExf0Nww3ShNQ4Slxd9-zwi1Jsyqcjn31g6Tv36apNKoNxlpK-s9SPoOULhZ3seKjVLl6-kyyDNg9k-UgFyh_5aFsqeZ-eDDYRQo2wkd6c4WNiJk8kPnTgEpNieTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
گل دوم ایران به امارات توسط شهرآبادی (51)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/106650" target="_blank">📅 09:44 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106649">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0c59ac2ee.mp4?token=cZYxeQPCds39kDpsW0-zQwWNm6NSp_-6rqddyKVKN1qf7jeK5Mzi_uFoOVyA_M5WGQkzDR4J4riOkwR1JuxAnAGdGG-mU47wHzeRmkxzUICbNYHBDr5SyxWbX2DJIbDoOzTlhli-6u1K7L4-VDW-p0CT97DNju7Imso0jzQvxXiCdwD9UTXdlZs5zE_Dty2FCPx-6Bx8_DoBC4fDF0eH5_INjH-MgBdRFrtu2iwes3owNJAteiLdOJimL_mBcM6HEiKCNRcWJo4tg8P9SvoqwQvT1Ae1fjO5V61WEcQOwZEDOsiVNPUV9BwTFm5zs9I2Rf4BLdwF6T67s7Mt2poF5m4Z13mcH6zjjpnCuG6B5j2INz-KyHayZx2SXhDxHPUDaFiIReI3iOytskHiDY2Vqqi0gkf3-ozgkhOSKchWJx6UXKGs3RtzQhRBjvKE9Qv_SGdkV5sYD7jbW3W_eVeQcQtjv7bwOLgXTn0vPQNiMIM4e7-hf6Jl1kEwJR6NqUlCJKYzhjR7uaC1-AqOMuiEulG8PWMeqcTI2Yn33WMSQMbLO_svPsCua2XjMFd1-EAA6EQMdAi3Ub25n3xoZQ-gsDF2L1L6mAEFS-xp40xrHTFUP7OKl8IY3qFMstHZawG-wZJP0vj44RMYjTS-hry-39udzJ9iZ7lqMO9JM1dGnfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0c59ac2ee.mp4?token=cZYxeQPCds39kDpsW0-zQwWNm6NSp_-6rqddyKVKN1qf7jeK5Mzi_uFoOVyA_M5WGQkzDR4J4riOkwR1JuxAnAGdGG-mU47wHzeRmkxzUICbNYHBDr5SyxWbX2DJIbDoOzTlhli-6u1K7L4-VDW-p0CT97DNju7Imso0jzQvxXiCdwD9UTXdlZs5zE_Dty2FCPx-6Bx8_DoBC4fDF0eH5_INjH-MgBdRFrtu2iwes3owNJAteiLdOJimL_mBcM6HEiKCNRcWJo4tg8P9SvoqwQvT1Ae1fjO5V61WEcQOwZEDOsiVNPUV9BwTFm5zs9I2Rf4BLdwF6T67s7Mt2poF5m4Z13mcH6zjjpnCuG6B5j2INz-KyHayZx2SXhDxHPUDaFiIReI3iOytskHiDY2Vqqi0gkf3-ozgkhOSKchWJx6UXKGs3RtzQhRBjvKE9Qv_SGdkV5sYD7jbW3W_eVeQcQtjv7bwOLgXTn0vPQNiMIM4e7-hf6Jl1kEwJR6NqUlCJKYzhjR7uaC1-AqOMuiEulG8PWMeqcTI2Yn33WMSQMbLO_svPsCua2XjMFd1-EAA6EQMdAi3Ub25n3xoZQ-gsDF2L1L6mAEFS-xp40xrHTFUP7OKl8IY3qFMstHZawG-wZJP0vj44RMYjTS-hry-39udzJ9iZ7lqMO9JM1dGnfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
گل اول ایران به امارات توسط شهرآبادی(49)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/106649" target="_blank">📅 09:41 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106648">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4029ff1503.mp4?token=KyRIgt-63ZJBLf0Q62-fs7hOzeRK18JXcN0iVIo4nIOUViBiQN_QBiQSDozfpYpX_5FcUuLpMtKJUQWLXOxmrRCCHQFix0ak_Epfiag1nygswCpdniQsyrOhXGerY-yU4g5WlH_q4KtmpqQ88m3gIcweSAGu5kJls--DCXDrJcIG6JWpcldA2tm3eMiiXhT0hTCYOPBmm5XDVUXpnkQf6UGVS2a6vKfEdbx7w2rVxjTxEhsnHN_aTsQIO9GIYswu3vApll2rsF70C8aS-_zfwgf77C59NO0OY2r6BJRqSE3eOsJg2G4TWM5Zg-PVfRg4L6gVlxtnHuveqL5VuDO64Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4029ff1503.mp4?token=KyRIgt-63ZJBLf0Q62-fs7hOzeRK18JXcN0iVIo4nIOUViBiQN_QBiQSDozfpYpX_5FcUuLpMtKJUQWLXOxmrRCCHQFix0ak_Epfiag1nygswCpdniQsyrOhXGerY-yU4g5WlH_q4KtmpqQ88m3gIcweSAGu5kJls--DCXDrJcIG6JWpcldA2tm3eMiiXhT0hTCYOPBmm5XDVUXpnkQf6UGVS2a6vKfEdbx7w2rVxjTxEhsnHN_aTsQIO9GIYswu3vApll2rsF70C8aS-_zfwgf77C59NO0OY2r6BJRqSE3eOsJg2G4TWM5Zg-PVfRg4L6gVlxtnHuveqL5VuDO64Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
رئال مادرید با شکستِ الچه به تونل وحشتِ نیم فصل اول رسید.
👀
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/106648" target="_blank">📅 09:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106647">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25ec17c4bb.mp4?token=N-VvoVw1QMPPax5M_egdI4xLSKXamEF-93PmBBAhXQq6VeUL8tURBWJxrPG1Ps26gnXd_LpF30BnTIKkbBTsMlCpal9SH-XF_U4t_Y1aukzL-FH39OIvTCF4x3N9ohgipefAH-VGGGgPsMSNU-E1qAbgBHRu2FsTaw3UBPCPcoeg9FVvngGzrOEOg6a-oB3BA5JSpsgji_U8u2h7l_rh2tGtIjKzfnnbs8K-ORw8JLZnk-lMJxcZ1aSLTtIpA0DHIUN0fuBw4sq_wmCBy9qhmxy8b6MKHizZstIPscRuCRt7dxOW2E2euHlIT7QtLteBf2QeugTz0Pa1ICORmhrvfYSgpJYr-X10V7XydOv8GZXVu0klT3t3tCrnWFAk84_Kztm9VrkFgqTK70FE_UD6cY69bqY2Cfmq2oC116W_LejmCo-2pGUoPhw1_WZdIWxQ7Xspybt89s6XzGqU3r3-MFk4A_B_olVHrs1J5WtjG9D5zghY1_Ms63Mbc9AvMF9ANNXJjtAOA3G8Kd3OwddJr02akFlBDyE1gHU07Adfj1Dazjv_iMPmMR2tXW9hJmBovy_SLTtAfEluzw4UQH6kkgaVe33yyzJ-1VnWEhaOcJybAoRjZe1L5rmaHf-OTfvhldE4o6acqunQ0v8EvEcZtHT7busoBHWMpxZDs3mtM9U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25ec17c4bb.mp4?token=N-VvoVw1QMPPax5M_egdI4xLSKXamEF-93PmBBAhXQq6VeUL8tURBWJxrPG1Ps26gnXd_LpF30BnTIKkbBTsMlCpal9SH-XF_U4t_Y1aukzL-FH39OIvTCF4x3N9ohgipefAH-VGGGgPsMSNU-E1qAbgBHRu2FsTaw3UBPCPcoeg9FVvngGzrOEOg6a-oB3BA5JSpsgji_U8u2h7l_rh2tGtIjKzfnnbs8K-ORw8JLZnk-lMJxcZ1aSLTtIpA0DHIUN0fuBw4sq_wmCBy9qhmxy8b6MKHizZstIPscRuCRt7dxOW2E2euHlIT7QtLteBf2QeugTz0Pa1ICORmhrvfYSgpJYr-X10V7XydOv8GZXVu0klT3t3tCrnWFAk84_Kztm9VrkFgqTK70FE_UD6cY69bqY2Cfmq2oC116W_LejmCo-2pGUoPhw1_WZdIWxQ7Xspybt89s6XzGqU3r3-MFk4A_B_olVHrs1J5WtjG9D5zghY1_Ms63Mbc9AvMF9ANNXJjtAOA3G8Kd3OwddJr02akFlBDyE1gHU07Adfj1Dazjv_iMPmMR2tXW9hJmBovy_SLTtAfEluzw4UQH6kkgaVe33yyzJ-1VnWEhaOcJybAoRjZe1L5rmaHf-OTfvhldE4o6acqunQ0v8EvEcZtHT7busoBHWMpxZDs3mtM9U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سوتی وحشتناک پویا پورعلی در گفتگو با عادل فردوسی‌پور که باعث منفجر شدن برنامه شد
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/106647" target="_blank">📅 08:58 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106646">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a5PlLLgR4kkpZXKMLp7fHYAXt1_nD_dICykRYUPz8J2cEyMFTDaAj3wecI_tIVn5XRVDhMVMs4P5W4iDG-OjwyY-cyjPp6gmHKRBnVKxOu8BnTPL1o14JVmHidt5_32Kc2rFre3XQqfxoV3d0XqRzhXWdpFXOzOPKnXPkoLstASKm9tk2jMaouMAfaeFW6MJhu9nMcHUUWA-TFyvKFlCXIpWwCzqJq5xLMEReGAtQEG1jYtI1ngefSw4C7ivKq1GuLM-UAyX0eNxwH_GXZSMzGgRXXN5PMcmSZMCWsEU7ljUFIQQEnlOjvPmQIwBPsGZHpZwBj8v3y3OPoBPyYW8Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚠️
اتوبوسی که رحمتی امشب پارک کرد:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/106646" target="_blank">📅 08:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106645">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106645" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/106645" target="_blank">📅 01:29 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106644">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gC4R0oi25hRY-9EVMt1pYizoaa7VSTw7jUqyD5yD2rThSFJeCzQvu_lpzajqHMNcjdxEN3iYXOTvhtyCFKGjxsSduTw8rQy49vcnc2o5BJeAuy5AIbzUCIoCQGrxCCHRMoYp0kQ74QA2jGs-VJS-yLYZpIR5dXNx7kHvPgjxuQVg7rt18X3erCym1nyRpPRdupvSufKWLgFegc_MpV77QG2w8l-SiFJ1dk-_rpZtuMU0K2KMZleAQGE248iX2u08qwPKFHRrzDdvpjpEFKYSKAEXh36TeW_jzwJrOYh8qXkgxNCCElkoxzjkreNShPMkQa3J5cNfw60GFALK2WX-Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/106644" target="_blank">📅 01:29 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106643">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/106643" target="_blank">📅 01:29 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106642">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFw7Pqm1DpdpnLTy_ABzokMMx-cqOY_dChPcYhIeQTwnhko5DPplRpUgKCv4cIxoG7tg3-eGM10WF_aAnnW4-FdMsSTDk0DO81HSVtjxNJpS3di-9zwEkDeDuX1huIP2JYcR_mrPDWWhCH2aK2h7802GmNJBnK0e2emEFn1hh5PpBk7JkpshqJpNgLXc0YCWdfAh2pRMDsqAyhBDzbwk2U1JRCq1zuM0-HJMV-UO4y_uAxuw-EnXqMojGhy7HkwMWph-2RdWa5JwaZ3meyWG6vL0RL1LwuU5ewtrEFW1HUQ932upTDpUJnG1wHd_U709Z3vK90YtqMZGwvKjf5uSVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🇪🇸
🌟
یان دیومانده در حال حاضر بالاترین درصد دریبل‌های موفق را در هر ۹۰ دقیقه بازی در لیگ اسپانیا، در این فصل، دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/106642" target="_blank">📅 01:23 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106641">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XpkGxzMWN7yUz_qG5oCGk1LomegfERlpNBLpsI35Uinld_jIOGTpbboI7qMvkTAVZEwI55tokC0PFNTD3aiiTLA5eekhT9EzFatqTjd-GJMFkoxopE47ZDdOpdoimgx9iFo3dGi8vumZ564zJtoZe0c1It6eVjv2C3WKVY0zUp9yslPUMYddAU9IIbgdrZ1aXVo7otKXNOtnlbCM5eKjLhcGeSy1c-nImJg7VbUb7koNrdAmF1grkMQQNKHO0u8Mb6Fos94R6FXJf7j7b7v11cLGFWF4PQKI9IqiK68iPEKHnilLHf0Z-exkO3XlGw2mBx5AxH6VRxt2K5D-Cdbhxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
🇪🇸
ژوزه‌مورینیو: کسب سه امتیاز اهمیت زیادی داشت و صحبتی بیشتر از این وجود ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/106641" target="_blank">📅 01:17 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106640">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pl9Leew-JKIVBmWn89Yr6v1fJ0G8BwBA1x7LnTAM4OU9q0jr857oKeXYH3SNmiA_lxoDh-uQiseoQvJTzV2cvTSFvDUnxd-N43xpXxkSDjQo2nYl8JjBiCvkOWZ2d7bVpCDmdaV-X_QFWrQncOTq6aNEeR8d0AU_rnkw8sv6nHcteCZggMxjl0VnrL_ZrvLoO_Bc75us67SctSl3RTh-bPK_h_Ptqy7u5LyDPf9oAp4YUM7ndY4TTjNHEFxFEfh75QvEQvfOFEXq50BedjGzD7WQnFhLRoOUNkBSbDcG75U2OQbnUxNPMfdDxTji--gxTIv6yYBsjiX-dhwfb2Q9fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه اسپی یکی دوتا بازی گل نزنه، شعار حیا کن رها کن تو سانتیاگو شنیده میشه
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/106640" target="_blank">📅 01:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106639">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0d40ec75d7.mp4?token=MhdQsn1OHZ4104wFWTFAWiTrXAakWToDYLUF9jQCCRDe0efQt3GGyzovadELQO_6K0J4DPG2ghWZPYXysGcqT8vG1Fd2ymZ1Brq1STFzAuyVNCFqtWE45LhSgQOAK9kSJelCNTrRMKHCtvHNGbR_10s1xnaMZPwnTcdHBiP4t7M43ecRmwFwpNLUEuotiMY0GI8yNwpwsIgPGfA954BQocV0dmORdW1vdf9Dw77eq7QRELCkBVCt6lH30HlK1F0tB9nFSn9voxzbltO3X8utxIsqy-baBmDCOgTQUNeuVKk0eNz7irU5U64WNb0d1hyXnWvwWtBCqnTw1D2Gp7SjwSRZDIM7frtN74U7yjCsrc_evLGFmh_lPNyBdRpMkspXNpIpGSNbync0GhDdEx6DWTQMb8Gplf0u1AhfWS0VBqT4aRcZ2zcLt-CrtTqFG0F8Hx1npOW8ghokGyiocFlQP3Fpy180Np4UyDkGdHM0MlRPO1ciuehy0oPv1ZJDs72EW2SlLLGbmTe_byE1szqkL21-3Thd7dS1RLBrbQiEtJDA51o9aGnGk6ikgOAmOwysJDRxdQIUJWB2Z5hF_tzuLGzkIDd1SHHrbWs_35VyqdiIS7muiZvyJTzcvBmAGwgaLp95xOgGHd_yr-oiIpWjRPC_XM-8uqtq-Uns5Bk6AN4" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0d40ec75d7.mp4?token=MhdQsn1OHZ4104wFWTFAWiTrXAakWToDYLUF9jQCCRDe0efQt3GGyzovadELQO_6K0J4DPG2ghWZPYXysGcqT8vG1Fd2ymZ1Brq1STFzAuyVNCFqtWE45LhSgQOAK9kSJelCNTrRMKHCtvHNGbR_10s1xnaMZPwnTcdHBiP4t7M43ecRmwFwpNLUEuotiMY0GI8yNwpwsIgPGfA954BQocV0dmORdW1vdf9Dw77eq7QRELCkBVCt6lH30HlK1F0tB9nFSn9voxzbltO3X8utxIsqy-baBmDCOgTQUNeuVKk0eNz7irU5U64WNb0d1hyXnWvwWtBCqnTw1D2Gp7SjwSRZDIM7frtN74U7yjCsrc_evLGFmh_lPNyBdRpMkspXNpIpGSNbync0GhDdEx6DWTQMb8Gplf0u1AhfWS0VBqT4aRcZ2zcLt-CrtTqFG0F8Hx1npOW8ghokGyiocFlQP3Fpy180Np4UyDkGdHM0MlRPO1ciuehy0oPv1ZJDs72EW2SlLLGbmTe_byE1szqkL21-3Thd7dS1RLBrbQiEtJDA51o9aGnGk6ikgOAmOwysJDRxdQIUJWB2Z5hF_tzuLGzkIDd1SHHrbWs_35VyqdiIS7muiZvyJTzcvBmAGwgaLp95xOgGHd_yr-oiIpWjRPC_XM-8uqtq-Uns5Bk6AN4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
کارلووووووووس اسپیییییییییییییی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/106639" target="_blank">📅 00:55 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106638">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">وینیسیوس بیاد برا اسپی چند دست میل کنه</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/106638" target="_blank">📅 00:53 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106637">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">عجب بازیکنیههههههه
😂
😂
😂
😳</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/106637" target="_blank">📅 00:53 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106636">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">کوووووون رئال‌ نجات دادددد
😂
😂
😂
🔥</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/106636" target="_blank">📅 00:53 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106635">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">اسپیییییییییییی</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/106635" target="_blank">📅 00:53 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106634">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">گلگگلغاگاگا</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/106634" target="_blank">📅 00:53 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106633">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/90c95a451e.mp4?token=AVpOsGZ82PMK87ZK4hWPWGoVbKQ6mLk2O5MZaWP4Ixe6A5nXbZshkPcl9GBSwTRed5DvyIuFGM2twXUb0w3VcmHUpo3Sa_czLhLPpzlBo7g3cwHXWIgt3hzl8pzeXIjcCmaMsdETfi8G0EKiRrrfMU3q8XpaUnyxSd61ZAkJufjGh9yoYt1WaQp8cxJhrvl3U08ZmP3zK9NbprjyEm_IMTySiNFcK6PBcvG26YoeJhpKUO_88F4L7fLMb4Q_IEeYhGD-y4j9cnAi36EAvihEUCh6mMdAOV24jhZvYOFJEBQDVN73HIp5aaHhtoPDQbCJhqT1MUmO70VwILyVJn6xBq17o__DPBgv6OAj3fuRk-_m0xiACn5dEkv2ut0sfbqmYXVhIncAZSjbPp9Ws5rgSL2xanFT5HE0qpRmEQP9xfpCsxLKcIB9exlt49qAFvCIpbsNITddqdEgXD7jaB_Zu2W-NHKCjGH2GsH9fFL_uZX-HcBRpbWhd6QLX0HYWEjoNz9_gtOMMvVHyTCqODPbPWuNMI2ICM_-y_ZMNiDEjjZnjrpDs_7NCoVMmYKCCEZnGOTIrB5Z85pt7paMPOkSA2WRy_rISTVrkm54HXeryhAqkpbJFRuVsjTd46P307h5uqxsX7UvdTbuE_xjPs5PHdCU1GMVQIw0HDtkFsImQhM" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/90c95a451e.mp4?token=AVpOsGZ82PMK87ZK4hWPWGoVbKQ6mLk2O5MZaWP4Ixe6A5nXbZshkPcl9GBSwTRed5DvyIuFGM2twXUb0w3VcmHUpo3Sa_czLhLPpzlBo7g3cwHXWIgt3hzl8pzeXIjcCmaMsdETfi8G0EKiRrrfMU3q8XpaUnyxSd61ZAkJufjGh9yoYt1WaQp8cxJhrvl3U08ZmP3zK9NbprjyEm_IMTySiNFcK6PBcvG26YoeJhpKUO_88F4L7fLMb4Q_IEeYhGD-y4j9cnAi36EAvihEUCh6mMdAOV24jhZvYOFJEBQDVN73HIp5aaHhtoPDQbCJhqT1MUmO70VwILyVJn6xBq17o__DPBgv6OAj3fuRk-_m0xiACn5dEkv2ut0sfbqmYXVhIncAZSjbPp9Ws5rgSL2xanFT5HE0qpRmEQP9xfpCsxLKcIB9exlt49qAFvCIpbsNITddqdEgXD7jaB_Zu2W-NHKCjGH2GsH9fFL_uZX-HcBRpbWhd6QLX0HYWEjoNz9_gtOMMvVHyTCqODPbPWuNMI2ICM_-y_ZMNiDEjjZnjrpDs_7NCoVMmYKCCEZnGOTIrB5Z85pt7paMPOkSA2WRy_rISTVrkm54HXeryhAqkpbJFRuVsjTd46P307h5uqxsX7UvdTbuE_xjPs5PHdCU1GMVQIw0HDtkFsImQhM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌تساوی الچه قعرجدولی به رئال‌مادرید
😳
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/106633" target="_blank">📅 00:49 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106632">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">اندریک بدبخت بالاخره اومد زمین</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/106632" target="_blank">📅 00:48 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106631">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">اسپی رو آوردن زمین گل بزنه
😂
😳</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/106631" target="_blank">📅 00:46 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106630">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">دفاع رئال جلو حمله بارسلونا رسما خاله میشه</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/106630" target="_blank">📅 00:46 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106629">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">مورینیو ریدههههههههههه
😳
😳
😳
😐</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/106629" target="_blank">📅 00:45 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106628">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">الچه قعر جدولی مساویو زددددددد
😳
😳
😳
😳</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/106628" target="_blank">📅 00:45 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106627">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">گللگگلگلگلگلگلگلگلگاگلگ</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/106627" target="_blank">📅 00:44 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106626">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6efefc36b3.mp4?token=fkm_7O_UR4OMHzCLMGBKsnnvUoZFwo46nxSw_D-xTBN6xc2BEpdVwrsTjbYDdQUqSIFv2ikll6f8pa7E9FmSYXDGjNnP3pXug-xGXAnvfA3busQMsHT-N0GWhcaep-a5ywRmz-YvDCXUKeRrqmHWfw8pRzvFEfCuzvRFWbOniiUyrul2nTds69vGuS4no0vMNe77Kgl8NxawWnHFJAhOyunfK_S2uw7ruqdf7kuSHqyTWwwUNCp-BOohjR7gaT9TQ-Rj79lCwo_CrrjtWJJicJpB2dIWwbWbT-zoL2ST3Sh8OqgDFiRHs4dWWIBdEYw-XZGDu-CFKr9Vva-0jPhiUIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6efefc36b3.mp4?token=fkm_7O_UR4OMHzCLMGBKsnnvUoZFwo46nxSw_D-xTBN6xc2BEpdVwrsTjbYDdQUqSIFv2ikll6f8pa7E9FmSYXDGjNnP3pXug-xGXAnvfA3busQMsHT-N0GWhcaep-a5ywRmz-YvDCXUKeRrqmHWfw8pRzvFEfCuzvRFWbOniiUyrul2nTds69vGuS4no0vMNe77Kgl8NxawWnHFJAhOyunfK_S2uw7ruqdf7kuSHqyTWwwUNCp-BOohjR7gaT9TQ-Rj79lCwo_CrrjtWJJicJpB2dIWwbWbT-zoL2ST3Sh8OqgDFiRHs4dWWIBdEYw-XZGDu-CFKr9Vva-0jPhiUIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
گل‌اول الچه به رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/106626" target="_blank">📅 00:37 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106625">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">الچه زدددددددد یکی</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/106625" target="_blank">📅 00:33 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106624">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">گلگلگلگگلگلگلگلگلگلگل</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/106624" target="_blank">📅 00:33 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106623">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01890ef1a2.mp4?token=vVMLpPsf45rjOqVcZWCLwAsTkeYHTj9hZr3DyYWl3Q2HGmPTFze00KoO0-0l8Bny1lDRtJ_zpXCobv1roXO0Tbd_NECQsSc5qmP9kEkdXq0CGWbKdHkN1gIOP0oh3sfJ56-LWnTaCeSUPclASSyhdOFcCNDHgwg4HGQbDFrwl-FufE3EixqjYgwyfaKcJt3-6FOC9I9Rj6nbaEiZmWFhCXpMfGOyAOEiHEPFOCFGc0szMf-J_hAQ5Kpl4qRUmA-Y14NnaEGz-PwGUQXVqVbiPK1-ihZgUIiPbGoPOOH-ZUdYucc8i6V-IPCDVhNgsQsvTRw-Dz1pzNONjCKWn0CzTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01890ef1a2.mp4?token=vVMLpPsf45rjOqVcZWCLwAsTkeYHTj9hZr3DyYWl3Q2HGmPTFze00KoO0-0l8Bny1lDRtJ_zpXCobv1roXO0Tbd_NECQsSc5qmP9kEkdXq0CGWbKdHkN1gIOP0oh3sfJ56-LWnTaCeSUPclASSyhdOFcCNDHgwg4HGQbDFrwl-FufE3EixqjYgwyfaKcJt3-6FOC9I9Rj6nbaEiZmWFhCXpMfGOyAOEiHEPFOCFGc0szMf-J_hAQ5Kpl4qRUmA-Y14NnaEGz-PwGUQXVqVbiPK1-ihZgUIiPbGoPOOH-ZUdYucc8i6V-IPCDVhNgsQsvTRw-Dz1pzNONjCKWn0CzTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
سوپر موشک تاماهاوک سوبوسلای جلو تاتنهام
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/106623" target="_blank">📅 00:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106622">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">سوبوسلای چه سوپرگلی زدددددددددد
🔥</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/106622" target="_blank">📅 00:20 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106621">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">پشماممممممممم</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/106621" target="_blank">📅 00:20 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106620">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gHIgDeA9TUKBfZhUb1N90Ei04imaUJ-KI8XzHxNG6tRKfPv7RKgDOHTDZnph2o8ETX0563YHwwRIlJ7LYsiP-R3CpAU1xbjv8HJ0Kj9u1FsDlUY40m9-SBSAO8pA2ncWkXIe1EHnc6MUUkyuHIo4NFnBHAa6Tzfca8TJKBlJp7qA99tNW8N3nStnxhDfscea3eYpCBE45GKHda8hPiQPpJW7CkH_HYqUpsHPjtEdcAqDZdANRVIaI2aopnK_IHmQnBqd6ZNGZVavnyabDHY3jwkTeB4GlPN6LJA7fbv2oPuyjIVWj-d-er0czJmtdglC01OdYiNgSamaO1MQb9hevQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
لیست تیم‌ملی آرژانتین برای فیفادی با حضور لیونل‌مسی؛ بازی مقابل بنین مراسم ویژه فدراسیون فوتبال این کشور برای خداحافظی اسطوره تاریخ فوتبال برگزار خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/106620" target="_blank">📅 23:58 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106619">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gq3DQudSE2Y9o-Q4f8awmOPPtnlFmSE1VREoPT8hyhba5SK_pC49RzsdtBRKaNOQ_wRyavBdXsAjCRyWpCJgvvOAOgCqCkUxMaUrYP7HU8Ba-7xdpr8pMYQ3DWDZEufg_IN2ecFzwl6G8E2V79Zx-lPcAxgZFt0-_z_-8flO9YDfLEGWPZ2v27-4xmBsWYS33JyAjdtZaDxt7vKTUyIfthzq2ddlCtSeYFmNHvBjMaWYHSEotzR2-ZCnxp26D0ftGzyxCR87ZBbcwzOGQfzB23T8tyBjLTxTcUZSG-ySA4qb73AhQ2qCdp5b1sbbP6OteMfAxZZuJO-ZDFvjt-35MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟣
جدول لیگ‌نخبگان آسیا در منطقه غرب پس از پایان هفته‌اول و حضور استقلال در رده دوم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/106619" target="_blank">📅 23:41 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106618">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/01ef226cc4.mp4?token=TkCOTd7lSFyiptFNAnoFKqjHLAuew5Z-8WUxAiNx6f9-0EnxTCF8x88trpzBos4czPCuYHESK-hzxWSqRw32jmWGf3GxgNu22lPlq7hRlXun3BDT9YeIW_PkSRyec5KOCyCgJu96OHu2h-NfMZSG_1jREwEW8uxeYs4VnC2MzSPCoIChuNQpHLk_Sw7gVQd5lyUkKlrcdW5qVLAB4dq9s4UwhxTk8PddFSeB7dmN1-eE7IkEo9QRgJU6mDZfle0TbuYwW8_gtS9K25pMERBKNZLGKcNOa77WfvHazHfORKuCIXuwKoLyjw6k_kPP5Ahdb-AO7eZ3UAin_2Uqaupq6hRFhsFq6LUGVAGennwpA5xrFtQ-he0COY6IJq92HGQsJxaxzhD4lO0C3lO58IUWp1MnQfS9RESHx-icfH_hj1SjSWmjGw20HrZHpckgxELNWlyGBv1Y5KISJwVA8wkbJ-AdrjPlrUGX2YWNeIlD5-3zULCzC0_gmsFvXT5q2_hLvWopCd2DNvmRJy5PvdSX902HLW0uherj5mzOs8Ts5soLDgubWxizSfwiGpxeM8nfbJ0otYlqC6iClUyB8f8HpzxqJdAtgefLSU5tGDBh9nhSrA8yMAAf57VQzS8lBuYQXGBmrSD-gQegsJBZ3ZRxD7pd7EPnVLvF5rL3Ol1AFNM" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/01ef226cc4.mp4?token=TkCOTd7lSFyiptFNAnoFKqjHLAuew5Z-8WUxAiNx6f9-0EnxTCF8x88trpzBos4czPCuYHESK-hzxWSqRw32jmWGf3GxgNu22lPlq7hRlXun3BDT9YeIW_PkSRyec5KOCyCgJu96OHu2h-NfMZSG_1jREwEW8uxeYs4VnC2MzSPCoIChuNQpHLk_Sw7gVQd5lyUkKlrcdW5qVLAB4dq9s4UwhxTk8PddFSeB7dmN1-eE7IkEo9QRgJU6mDZfle0TbuYwW8_gtS9K25pMERBKNZLGKcNOa77WfvHazHfORKuCIXuwKoLyjw6k_kPP5Ahdb-AO7eZ3UAin_2Uqaupq6hRFhsFq6LUGVAGennwpA5xrFtQ-he0COY6IJq92HGQsJxaxzhD4lO0C3lO58IUWp1MnQfS9RESHx-icfH_hj1SjSWmjGw20HrZHpckgxELNWlyGBv1Y5KISJwVA8wkbJ-AdrjPlrUGX2YWNeIlD5-3zULCzC0_gmsFvXT5q2_hLvWopCd2DNvmRJy5PvdSX902HLW0uherj5mzOs8Ts5soLDgubWxizSfwiGpxeM8nfbJ0otYlqC6iClUyB8f8HpzxqJdAtgefLSU5tGDBh9nhSrA8yMAAf57VQzS8lBuYQXGBmrSD-gQegsJBZ3ZRxD7pd7EPnVLvF5rL3Ol1AFNM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل‌دوم رئال‌مادرید توسط کیلیان امباپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/106618" target="_blank">📅 23:40 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106617">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">دیومانده بالاخره پاس گل داد
😂
🔥</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/106617" target="_blank">📅 23:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106616">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">امباپه زدددددددددد</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/106616" target="_blank">📅 23:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106615">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">گلگگلگلگلگلگللگلگلگ</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/106615" target="_blank">📅 23:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106614">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/96af48f644.mp4?token=fXIPEYjRC2Ocl-Qfp2ni7i8RoV3m5tVYZXWhShWQyB44Q2voevtlX_EFSsLvXCaV7fBiBYPEK8kUufYzK3Owh4r7qHCFwcBopvfrDlkY0ZqY453rAhcP-2_HEzJ2x6i2t1fzApiaBNxZ0OBJxuTVSptw4l3Y4Fsdm2P-lQG9-5zpsVWAN4xqy4g6a1AahryjDYctV_iY-bixeS8EyCaEjCyaLztVrz2hw2-zZIuGUKc8bKIf82tP5iSWRT0EVNN6opj2FyGH-FKiUMM725Oz04pB2dyG9JpXTiU-xnpdJg20AMBHy3dv5UsAQEiwhVQe43o97dPbOaDwHYaPcIr8GR9Xx1xBgfu_laf7YjelaQh-4iC671V8gvN5SWSOrnlXnYRGNdjK6RYLZ0i7AHzkmNFucQHHIJFvxQr5U7wIaWdNsdfeaPN6R0POj_sIGiwdlDZspLRM0SzJ1f3D4RAhvyQP6B38pfxPuT4NNZBWi4V-kRP8T7UFnXdZSGD5G5cH8-XdeRG82OlL8a_twsXwbfdnMBgz-iHRcEfnLf7It0FxzeuF2q47klRUR4xxqAu45sEY1Acq7bMwfvsb-GQLylF9E37HY63DWJKhP0TJOZdt9RDOTxiCE1KhokTwhNuJTyY46GR83vOdetSAH1NYueYijxChTwZQ5NZfOoP8a94" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/96af48f644.mp4?token=fXIPEYjRC2Ocl-Qfp2ni7i8RoV3m5tVYZXWhShWQyB44Q2voevtlX_EFSsLvXCaV7fBiBYPEK8kUufYzK3Owh4r7qHCFwcBopvfrDlkY0ZqY453rAhcP-2_HEzJ2x6i2t1fzApiaBNxZ0OBJxuTVSptw4l3Y4Fsdm2P-lQG9-5zpsVWAN4xqy4g6a1AahryjDYctV_iY-bixeS8EyCaEjCyaLztVrz2hw2-zZIuGUKc8bKIf82tP5iSWRT0EVNN6opj2FyGH-FKiUMM725Oz04pB2dyG9JpXTiU-xnpdJg20AMBHy3dv5UsAQEiwhVQe43o97dPbOaDwHYaPcIr8GR9Xx1xBgfu_laf7YjelaQh-4iC671V8gvN5SWSOrnlXnYRGNdjK6RYLZ0i7AHzkmNFucQHHIJFvxQr5U7wIaWdNsdfeaPN6R0POj_sIGiwdlDZspLRM0SzJ1f3D4RAhvyQP6B38pfxPuT4NNZBWi4V-kRP8T7UFnXdZSGD5G5cH8-XdeRG82OlL8a_twsXwbfdnMBgz-iHRcEfnLf7It0FxzeuF2q47klRUR4xxqAu45sEY1Acq7bMwfvsb-GQLylF9E37HY63DWJKhP0TJOZdt9RDOTxiCE1KhokTwhNuJTyY46GR83vOdetSAH1NYueYijxChTwZQ5NZfOoP8a94" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل‌اول رئال‌مادرید به الچه با گل‌بخودی گلر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/106614" target="_blank">📅 23:31 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106613">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d6sGvIW3DruIJWcuxTutKbjJdfDSBeVeo8yZB6auphgFRoTtHFlE-5-45QadNTPWg-rG8T6xhjkzojo24dtXrP3akOxHrow6CmTTF1isqbii1RsQ6ApeJ1YAUWtEvktvKJZkKFcJTVT5LdE0fOJT1BA-zNHrH7uHE0wrzgEcEMvlWe9iqXvuSLzEGCf5ssNBIhnqgqA6-_4YBY_KL1ZGNq3_sKhkKXaMDnn5xz9tdR8el79AtemXjPjY4PZcS6oHIgkuTTgaOPTE7O6aVQmk_uis5kamQCJncH5OuBR72MJ-PyXx43z5ZGjgG5mybWi_eOqp9onb7HD2yw_-zi3CGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوووووووف
🔥
🔥
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/106613" target="_blank">📅 23:30 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106612">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">عجب سوپرگلی زدددددددد
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/106612" target="_blank">📅 23:28 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106611">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">آردا گولررررررر زددددددد برای رئال
🔥
🔥</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/106611" target="_blank">📅 23:27 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106610">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">گلگلگلگگلگلگگلگلگلگغگ</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/106610" target="_blank">📅 23:27 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106609">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb9c936306.mp4?token=dzEhufwPS5JSg0CtzXc_NZJud0qMnOBdBavyHZ2r1xxL_-o-EJuE-Wx2LGSVEIjSnlkq3m3-KqGRbjpBGg8cLPgYpKj5GrwZfGKl2goojF9Qt6uy6HNs12QcfHW1x3HsjNAzGfiFzF37XiDX7c5DbsOhW2F5vYx8uoS4zyNT7K1-oPwXbSMkOmuOwoIewwkdeyftBmH_zgLkmtf8qIaJLMJzmDwI0Xqz8-GsTruaatS8ja_soqrZI7mOLYfm2DXyXMxyRwdvGchKgWwiQ819iPsdahjSJWAVWixa0qvGG5GiNdF1i94apJiFRYplJAp6my-3M5Rdu22hKspXv40GLXVoWEZXZSlImgkq3hIZ9PdqyqfjMsMJpBrhQCfylUzGPYMoKjXhC-fTAGNJqH8YvwIFeb5wm-WGLm2VJNXhPwK9tbSKUwohizpCmXO-XewkPPrNAizr2OlNfBeMchisJ7ALaVh2bDZD5SDICjgeUmghomuUqmsDNeeNBLAAw1TFvMPNGpL1BNx_Jq5hcP6I3f4r1BSybbVv20IPsCBFg-uEs8fpBYgV7tMSKXKBo-u4zNKj1bw1iJjjfAViMIFagh9_2mZNWsNuvVWS0-zTX9J51jjyTqntK0Y6n-mNyCvh_bo4GmvnrmvSRhor4mnNtaf5crPvkWJCYVrOUFMWfJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb9c936306.mp4?token=dzEhufwPS5JSg0CtzXc_NZJud0qMnOBdBavyHZ2r1xxL_-o-EJuE-Wx2LGSVEIjSnlkq3m3-KqGRbjpBGg8cLPgYpKj5GrwZfGKl2goojF9Qt6uy6HNs12QcfHW1x3HsjNAzGfiFzF37XiDX7c5DbsOhW2F5vYx8uoS4zyNT7K1-oPwXbSMkOmuOwoIewwkdeyftBmH_zgLkmtf8qIaJLMJzmDwI0Xqz8-GsTruaatS8ja_soqrZI7mOLYfm2DXyXMxyRwdvGchKgWwiQ819iPsdahjSJWAVWixa0qvGG5GiNdF1i94apJiFRYplJAp6my-3M5Rdu22hKspXv40GLXVoWEZXZSlImgkq3hIZ9PdqyqfjMsMJpBrhQCfylUzGPYMoKjXhC-fTAGNJqH8YvwIFeb5wm-WGLm2VJNXhPwK9tbSKUwohizpCmXO-XewkPPrNAizr2OlNfBeMchisJ7ALaVh2bDZD5SDICjgeUmghomuUqmsDNeeNBLAAw1TFvMPNGpL1BNx_Jq5hcP6I3f4r1BSybbVv20IPsCBFg-uEs8fpBYgV7tMSKXKBo-u4zNKj1bw1iJjjfAViMIFagh9_2mZNWsNuvVWS0-zTX9J51jjyTqntK0Y6n-mNyCvh_bo4GmvnrmvSRhor4mnNtaf5crPvkWJCYVrOUFMWfJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
صحبت‌های عادل فردوسی‌پور درباره اسامی عجیبی که بازیکنان استقلال در پشت پیراهنشان در بازی دیشب نوشته بودند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/106609" target="_blank">📅 23:25 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106608">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/001b323a9f.mp4?token=crVD-RUk_oTgOSnCBVVp_rTmVgjt9N7sl4ZwCD7HBRzHYK4iIirdAHiLWLaVfdwwTT7FtMAGOn7WB8F3e-lryv3aZb8l9K5xer3iynwwJ6BO-tGACDT-THUzh5iF9zW4EbVtjI1hnZ-vuBPgb2hr5CiJInRuSnYluf27XApyYeYw4XAEV1exszW4Vvl7C-3DCS1_jgfGNdCkXrTJXHp37hVbSFRtjK_VdZ693LqvqzTllBGoh_3NB06E4ci6DR4SWydbIx1aMSEZqiWBWAylB2Rdl2hkrJ_7VEeMajSUiljfYdNay6M-QEOdJvIo_b05d9dAcYNZK1nUsPEvIIH594WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/001b323a9f.mp4?token=crVD-RUk_oTgOSnCBVVp_rTmVgjt9N7sl4ZwCD7HBRzHYK4iIirdAHiLWLaVfdwwTT7FtMAGOn7WB8F3e-lryv3aZb8l9K5xer3iynwwJ6BO-tGACDT-THUzh5iF9zW4EbVtjI1hnZ-vuBPgb2hr5CiJInRuSnYluf27XApyYeYw4XAEV1exszW4Vvl7C-3DCS1_jgfGNdCkXrTJXHp37hVbSFRtjK_VdZ693LqvqzTllBGoh_3NB06E4ci6DR4SWydbIx1aMSEZqiWBWAylB2Rdl2hkrJ_7VEeMajSUiljfYdNay6M-QEOdJvIo_b05d9dAcYNZK1nUsPEvIIH594WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
گل‌دوم الهلال عربستان توسط ساویچ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/106608" target="_blank">📅 23:22 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106607">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">یه گروه همفکری بت زدیم مخصوص دوستان بت باز
😂
✅
https://t.me/+6XLorNFkXGgzNmE0</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/106607" target="_blank">📅 23:22 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106606">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">یه گروه همفکری بت زدیم مخصوص دوستان بت باز
😂
✅
https://t.me/+6XLorNFkXGgzNmE0</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/106606" target="_blank">📅 23:22 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106605">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e75776b642.mp4?token=NQ4TSA7scXu4XSSynizKE3HY3d33PN_7nAH2MBF-_v8S9wFyK_5T-qLZXLBjEI2dH0Mh4bxu2WeC2yjd46w6-XeKE2sXkmxqo6z4nHONBzTFClF7kPHvLZNul03oseevEWz0kOCHd1l0JJarsZ77SpbFC_gv1HjJIySsZH9AOnJZwF-W4sYz6TGT1dLrizbB1ltEWKBa1Mc_y2oKcCVZvFMxZKQqVrz0jYq7w0KpKNrz6l0X7YWKnqfFkRAZpvpgMo8I1naxoOvJQpU_nCxUDHHhl05Xh50hLsP5zTVRsJiwUALniPmLRh4i-PPyK8Jv3rpeg3EgKPk6pB5PufzyYA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e75776b642.mp4?token=NQ4TSA7scXu4XSSynizKE3HY3d33PN_7nAH2MBF-_v8S9wFyK_5T-qLZXLBjEI2dH0Mh4bxu2WeC2yjd46w6-XeKE2sXkmxqo6z4nHONBzTFClF7kPHvLZNul03oseevEWz0kOCHd1l0JJarsZ77SpbFC_gv1HjJIySsZH9AOnJZwF-W4sYz6TGT1dLrizbB1ltEWKBa1Mc_y2oKcCVZvFMxZKQqVrz0jYq7w0KpKNrz6l0X7YWKnqfFkRAZpvpgMo8I1naxoOvJQpU_nCxUDHHhl05Xh50hLsP5zTVRsJiwUALniPmLRh4i-PPyK8Jv3rpeg3EgKPk6pB5PufzyYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
گل‌اول الهلال به الغرافه توسط روبن نوس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/106605" target="_blank">📅 22:52 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106604">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🟥
🇶🇦
اسماعیل‌بن‌ناصر هافبک الغرافه بدلیل دریافت کارت قرمز دیدار با استقلال را از دست داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/106604" target="_blank">📅 22:19 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106603">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t1jzDjdjME4gxcrTw-jZnlY-4B8Q8RKRtLW1TEPIKR64SnZxrpyFpqEyLnyIrlcA8MF1MS31MDEEkcoR6QYrT9OK_ROiPIZonE5WzDf83WHem-j1QZm1J5iRD3nsJkbSjNTxWBOkuuhlzHRhqi7zhA58q4SiiP09r8mVxuxz3y3dlTZZ243QtK0gfkgXcCxU6BYR77mXQXylL_0MFyh58K_W7FRqqp69zrHBCGr8BFoiL4hZIPTCYJEaOj9vYYVX3aiMr7lP38-0bU3TuXIuUWbEtZvvCcCCX-AlxVwucpTOidK1F44OkH8XpluQHMHr22B3X4H6f4hE1i89xxuRrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🇪🇸
ترکیب رئال‌مادرید مقابل الچه؛ ساعت ۲۳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/106603" target="_blank">📅 21:47 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106602">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">‼️
🇸🇦
عصبانیت
رونالدو از مدافعان النصر!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/106602" target="_blank">📅 21:28 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106601">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d5839d9f6.mp4?token=oHDuabxwVKkDyrL8PNMh5SRpo3cu_iWYBvOku61LiTctSB6q4u4-e6f57xUXRnRZf7Shd44u6TYoX5UAbrRgmuO30y3fHVsWrmLvOPopDeNiieyJ_1BlOd3KRHhx_tebVlSjWSo1OjqXT2FFwKl5xvm6cqeCLO3bvaZ7Lcih51Nv2Sp-dhQ0J7Dmu5yMnfGTC2sXVtTdIxALUoD4vpU7wDJyeUpTt2eJCYbYWZJ5kL9B1Kdqv24pe8GCzB3Ir_NCiEEDte7GsjOx4hKD-YoKwPOFTXG9m8XpQX4fQaqp59P3QDNJQtXrG14UmgVP75lrFttBf9h6lB38mxHemewa2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d5839d9f6.mp4?token=oHDuabxwVKkDyrL8PNMh5SRpo3cu_iWYBvOku61LiTctSB6q4u4-e6f57xUXRnRZf7Shd44u6TYoX5UAbrRgmuO30y3fHVsWrmLvOPopDeNiieyJ_1BlOd3KRHhx_tebVlSjWSo1OjqXT2FFwKl5xvm6cqeCLO3bvaZ7Lcih51Nv2Sp-dhQ0J7Dmu5yMnfGTC2sXVtTdIxALUoD4vpU7wDJyeUpTt2eJCYbYWZJ5kL9B1Kdqv24pe8GCzB3Ir_NCiEEDte7GsjOx4hKD-YoKwPOFTXG9m8XpQX4fQaqp59P3QDNJQtXrG14UmgVP75lrFttBf9h6lB38mxHemewa2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇦🇪
گل‌چهارم العین به النصر عربستان!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/106601" target="_blank">📅 21:24 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106600">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DNEhPACN-tAEqW4ls7q64bYjT1xSqr75ykN8WsE4nlFT6q-2AiA588Zwn6RYMp7AT2FxhX5uzunniiryiS_CXRc8g96Q7RNUO_Rl727jfdExrQnyYmwjzVEqkBZ1NMcSrtWfhIU-vSC6YBLNTz_rEkAr8w_ub5GWlTmwpi4_9AJSFvCus__NzpJMA0hkfKOMzGO4XaC831kfsRXq4UzTxUyKKeiSfr-lGR0OmWabivB1plkpRqVx5RhPazmcU-PGvbhympb1tb_83XLLMWvKi8ZsI9HdSrT60BO8nk76r-uE9zySXEv5fTLz2yvCuwySbZvoV6Q3cUxDgQ6RY9C6wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇪
گل‌سوم العین به النصر توسط سوفیان‌رحیمی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/106600" target="_blank">📅 21:13 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106599">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2424b5a6f9.mp4?token=o6rDbbHLokcZBvfVhStljMNmcB3PVI40ZbDTbRDFyteeM_gac0xnxu_bdg76qdiSYgUBuJu3u1IftbupYmuzqJwcsvHNi_i4z-wzlWjKHJ3FTYvzuAEaSe-q27fFlZqWfUr6QXX93HqyCUWExvkNJi87cDGSKi-0UKkjv6oaOkb6C3tYEQKBdbS2yR-TtJ5gJzd3V3uR_Z9R-3PD36yIvSGHE7lh44putK2SoJOUgAPXdQT64gs6SrdaS_WDIwVmtUTDLKvAlOeZofHW4KUD1jbcQ38eQtQmnHf64gb7-WDM2QaVyXSYw0UMj9CmpSpDZPuOlsxft18FE3MSKmX4CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2424b5a6f9.mp4?token=o6rDbbHLokcZBvfVhStljMNmcB3PVI40ZbDTbRDFyteeM_gac0xnxu_bdg76qdiSYgUBuJu3u1IftbupYmuzqJwcsvHNi_i4z-wzlWjKHJ3FTYvzuAEaSe-q27fFlZqWfUr6QXX93HqyCUWExvkNJi87cDGSKi-0UKkjv6oaOkb6C3tYEQKBdbS2yR-TtJ5gJzd3V3uR_Z9R-3PD36yIvSGHE7lh44putK2SoJOUgAPXdQT64gs6SrdaS_WDIwVmtUTDLKvAlOeZofHW4KUD1jbcQ38eQtQmnHf64gb7-WDM2QaVyXSYw0UMj9CmpSpDZPuOlsxft18FE3MSKmX4CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇪
گل‌سوم العین به النصر توسط سوفیان‌رحیمی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/106599" target="_blank">📅 21:11 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106598">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">گلگلگگلگلگلگل سوم العین به النصر</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/106598" target="_blank">📅 21:08 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106597">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d9f6b6fba.mp4?token=vlV3xKszSLfKFMbb-AX3cV1G8h73O0CBTreUN9GccOJBwaoCEftEQm-HtFgEn2nypA8Yw8Gh_4FO5uCR9aR-MwvQuZqwFqzfcnSqr4Pr9r2Q695FPigg11EYU9484IdrpH_zifeXMU2SzlHP2wUHec8FYAtUPJobNJNHel5lp4lIijm9RlnyHq4UAg41LQxF9s20vzRGhsSF-tI09Evl0kBahFWtmAn4s_s6ayD9foJ7W364ehJBLYg65HP3VC0YQ3gcQjbVlhgI4wEgae6cwaakw9gnLQKFbFbGo_ByJ1WQ13SvZbCJxBclGNvKhwr05A2p-MB81xTffFo8Lhqp4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d9f6b6fba.mp4?token=vlV3xKszSLfKFMbb-AX3cV1G8h73O0CBTreUN9GccOJBwaoCEftEQm-HtFgEn2nypA8Yw8Gh_4FO5uCR9aR-MwvQuZqwFqzfcnSqr4Pr9r2Q695FPigg11EYU9484IdrpH_zifeXMU2SzlHP2wUHec8FYAtUPJobNJNHel5lp4lIijm9RlnyHq4UAg41LQxF9s20vzRGhsSF-tI09Evl0kBahFWtmAn4s_s6ayD9foJ7W364ehJBLYg65HP3VC0YQ3gcQjbVlhgI4wEgae6cwaakw9gnLQKFbFbGo_ByJ1WQ13SvZbCJxBclGNvKhwr05A2p-MB81xTffFo8Lhqp4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گل‌دوم العین به النصر توسط حسین‌رحیمی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/106597" target="_blank">📅 21:03 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106596">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">العین دومیوووووو زدددددد</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/106596" target="_blank">📅 20:58 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106595">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">گلگلگلگللگگلگلگلگ</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/106595" target="_blank">📅 20:58 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106594">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef7815d7dc.mp4?token=Rypdjlj20qSe8Y913fF18Mr0bgS1zfTgRZHzI39hOnnCJozxTzC-LBheEIraseKfi10u0JE5Dn1V0FIRNWplOktZsLk-HtmPTwgcIEoykJ12qt_uG7tqd8MnNIX35OiafHEk6kqdHHCdmiVDMgit73X7-pDUSrMHyZEjSIlGT9RQVjIIOeHJ3sf_1s_zJFUpyvTp8SBVxenXYq30cOmxjxsaWyChwtJVECw70LveeFnoYoH2hUE0yC7q7gO9ugVpNmzV6tQ3Uol1hhmQn-uwpiMgyvrt_OxA5sdYYHVxDpzmvVSK4Zu3btCxhqA725h0BEEB7aULlTDvdXinQtOyIWHRBmYSiZklm6hdbTyQHujw4HQIdsivQuCN4xDbkXBcKPkbYp4oRHORagGFp7sLpecqqfLVHUumeKjjHBkWrsubzie6cButpOPgbVuNgxPDPqzxB8_zJy-tsDw14Bnu2QF7rcGpNC3Vyqo1wt6QvHX_ZhJNMg0-XP4aG8V42GpAMhYqF4khflZY1GlaRXeDOte1fzgcQfHIIKr0JYi2fTqL1hjaCM0RPWjtDQ7r0T6FpXCDamcikRH_rvVm9RYg8FRPIuyNvLNWsX5rCqWo855psUC2NZj746XWXu2LrSVh_EWubJeU9dNTVJzKUxCDzClpGeH303Qu8w8pPgzgw2o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef7815d7dc.mp4?token=Rypdjlj20qSe8Y913fF18Mr0bgS1zfTgRZHzI39hOnnCJozxTzC-LBheEIraseKfi10u0JE5Dn1V0FIRNWplOktZsLk-HtmPTwgcIEoykJ12qt_uG7tqd8MnNIX35OiafHEk6kqdHHCdmiVDMgit73X7-pDUSrMHyZEjSIlGT9RQVjIIOeHJ3sf_1s_zJFUpyvTp8SBVxenXYq30cOmxjxsaWyChwtJVECw70LveeFnoYoH2hUE0yC7q7gO9ugVpNmzV6tQ3Uol1hhmQn-uwpiMgyvrt_OxA5sdYYHVxDpzmvVSK4Zu3btCxhqA725h0BEEB7aULlTDvdXinQtOyIWHRBmYSiZklm6hdbTyQHujw4HQIdsivQuCN4xDbkXBcKPkbYp4oRHORagGFp7sLpecqqfLVHUumeKjjHBkWrsubzie6cButpOPgbVuNgxPDPqzxB8_zJy-tsDw14Bnu2QF7rcGpNC3Vyqo1wt6QvHX_ZhJNMg0-XP4aG8V42GpAMhYqF4khflZY1GlaRXeDOte1fzgcQfHIIKr0JYi2fTqL1hjaCM0RPWjtDQ7r0T6FpXCDamcikRH_rvVm9RYg8FRPIuyNvLNWsX5rCqWo855psUC2NZj746XWXu2LrSVh_EWubJeU9dNTVJzKUxCDzClpGeH303Qu8w8pPgzgw2o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
لحظه‌مردود شدن گل السد از جایگاه تماشاگران در بازی دیشب مقابل استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/106594" target="_blank">📅 20:30 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106593">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f5e9475ab6.mp4?token=G9qU0fsMhS3OQbgCeXm7zqjgu9fsMijlucb22fbhZdF6pzU5fY7MsAPKkzta1QxEV1HNoAV-Rk4vKpmIMXN8wUKHatoZGM5eES6LpyP8iJF6BpgH_id6tJb0BRO5Og9ObQBSH8CF0h-gzDejQ-V7Vk7Mzg8ZEOLQdBt8N1QMkKtn_7ckzFLm8XuFr5UL10iSe4BbLDeqhxg3vliX-ghPL1_9sZuKJ7Seh0AM778zg1eI2P0K_piYXDRX_ffD_as1zqq-2kcM3H_QXFj52EnHUmypWv6hvdQ1FTDv1fFVmHQ5dCXwIkveRlRbxGCBj0C-D0CEUiAGbbSv4HRrCzz6zWRnC4qC1f31nPDVY7Ep9Yixd5_DCFzH246f4eHbs9dUY_n-LktLOAQgSykz6bVj1yxU_gylMQL1NNQJlFLqfesaeJlgvGUBpCJbwacCSbnRgzAsl2aQMK4ZbYH5JWLRL8sRKpVhD4x1QJF-faXRkbjDXpj4dG5EUC85OwlmmP6nZwi8gE9BPVOaozEidjwdUzQue00cwZzi4nONWiVydtMaPIRPZJyjx4MJE1TKpsUVk4f1xqa2HjaaUfi0rv0qfxb9yEi7FyjFXCNv-esCjTeX-jiIGIAvC33kHgdqX6SvoFNPAuFCbQnPbBfEL-o9h_DewsCDiCJU3f1QMS5FxNo" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f5e9475ab6.mp4?token=G9qU0fsMhS3OQbgCeXm7zqjgu9fsMijlucb22fbhZdF6pzU5fY7MsAPKkzta1QxEV1HNoAV-Rk4vKpmIMXN8wUKHatoZGM5eES6LpyP8iJF6BpgH_id6tJb0BRO5Og9ObQBSH8CF0h-gzDejQ-V7Vk7Mzg8ZEOLQdBt8N1QMkKtn_7ckzFLm8XuFr5UL10iSe4BbLDeqhxg3vliX-ghPL1_9sZuKJ7Seh0AM778zg1eI2P0K_piYXDRX_ffD_as1zqq-2kcM3H_QXFj52EnHUmypWv6hvdQ1FTDv1fFVmHQ5dCXwIkveRlRbxGCBj0C-D0CEUiAGbbSv4HRrCzz6zWRnC4qC1f31nPDVY7Ep9Yixd5_DCFzH246f4eHbs9dUY_n-LktLOAQgSykz6bVj1yxU_gylMQL1NNQJlFLqfesaeJlgvGUBpCJbwacCSbnRgzAsl2aQMK4ZbYH5JWLRL8sRKpVhD4x1QJF-faXRkbjDXpj4dG5EUC85OwlmmP6nZwi8gE9BPVOaozEidjwdUzQue00cwZzi4nONWiVydtMaPIRPZJyjx4MJE1TKpsUVk4f1xqa2HjaaUfi0rv0qfxb9yEi7FyjFXCNv-esCjTeX-jiIGIAvC33kHgdqX6SvoFNPAuFCbQnPbBfEL-o9h_DewsCDiCJU3f1QMS5FxNo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇪
گل‌اول العین به النصر توسط حسین رحیمی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/106593" target="_blank">📅 20:01 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106592">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">العین دومی رو زد ولی مردود شد
‼️</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/106592" target="_blank">📅 20:01 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106591">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">گلگلگلگلگلگلگل</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/106591" target="_blank">📅 20:01 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106590">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">العین خیلی قویه بیشرف
النصر رو کرده تو قوطی</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/106590" target="_blank">📅 19:58 · 24 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
