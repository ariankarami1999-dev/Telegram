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
<img src="https://cdn4.telesco.pe/file/CxVYziccE7QQdPMQFPvmFi2pu_OiZX6YLvLe1wg1BKT9WuHVha8UzFYOgy7ZQY2oPh2Da5H8SXxsatQu246MbzsH55hvfcyMAs26aNxmqajS0DpnxnlGWn6q0T5Rw60qXwpdIkWjo1pZeqGJ6Ra8FPN7QVEzmn4QzSGPLMFb7120Kg0jxWQXx7RsZNUvG9M4jaKmE54_ML_XUqSntXZkPG4mTOo0EcDFaSCZUo4KHp4lJxLZ4uziPNQqABNXC8Q1NXeuo6U2aqh7wLIYjRLQO0TdXMT_r1VdpZeIPmMp8H0EPSxGqfJ5tIf_y-OMhKw9zzEFWbJNBgY575UDggJAog.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.4K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-18 21:02:44</div>
<hr>

<div class="tg-post" id="msg-6804">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o3dAVzKDx7hBWM_1zhbpJNryBsq9LlpbCZJJrbk1w3e5VHwA7v5pDJeJkm_BeLbasHP48iuQKajuzWRs21f1ylJxuERVjyvb52RIiZMARQU3dfC33SxkXh5QDdl8baDL_eaQyddf6xN5coHTlHM9DJ02KTYD0NKM3LYcI57uzJps0toxvpVur5bTQWJg9SFit8PrMwHDmqny0Cmcerm4bgrMHfdj5SBEwQVMXtHXRuLG8heSTD7Bhp9Bum2D4F3rtQ0yDgcJ_MfaQY7JdCSlIR_DwxvdIuPmly70VGeh8kAo-lKUnyqJGDd5kSae_3JcVKRBJLZRwqqibdC25ZgMSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zc2bwJfKBd-cXRtYUK4lVRoyL7yz1m2jflGfjFkOJB1k2A6VuQ_oJBJBRd9sG5oEVEUJ7IrttsGWwkdofcKxpzDVYYG-VEfuWajU72_occb_ITKF5WnMwzEd9dtCRNADb5bQZtJRr9cvrXjcEsCmTDFKXzGSK2zPk5JLHHARY28q2C91IDKHjekGd8DDRlPKihJSkD6xLYLkuoiFf5IwG8uvCNVskOdi3YCY3OK3IkLIR7c14P1osWinIoXk-b7OHFxoV05fnPcssoy_LBwx5bYm9TdeIArc2cuUVlTn2b8ArlvNpDCG8ukb6qucmkWP4keaM0q1N525cOWoMdcCHw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bca5f42c66.mp4?token=NctiGj2uhYb3el30Q7Wy_IEAFgo_27izNzOHmgmlW2dx9qLryak1C7CsJPzGwvcX-MEJ7sR0Sfc9bOxwUNyCcTUb2ozva79VpcSbcbyn4DxcBpbl5nPqqJU7T31KE2HVU09xZm0YOL5Ef6ZAfBCsaKJhmi737BQ6npq31JDgO2ZPMZpsr78gqSFEZ9Ea7_X2BVbEBw8PdVFXeBd3lvb4zqOvWtNv5wrCiEOYNGhwlyPIpkRuRR1Gzw3tmRZDa0H5q-NGZI39G-RVrMsV1zehfR78Z6AaPfPmQHd1Jf3EyAKzXH8iGtTuttVsNJD65KmR7PKQk9KFZC9Iptz6k_ENIjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bca5f42c66.mp4?token=NctiGj2uhYb3el30Q7Wy_IEAFgo_27izNzOHmgmlW2dx9qLryak1C7CsJPzGwvcX-MEJ7sR0Sfc9bOxwUNyCcTUb2ozva79VpcSbcbyn4DxcBpbl5nPqqJU7T31KE2HVU09xZm0YOL5Ef6ZAfBCsaKJhmi737BQ6npq31JDgO2ZPMZpsr78gqSFEZ9Ea7_X2BVbEBw8PdVFXeBd3lvb4zqOvWtNv5wrCiEOYNGhwlyPIpkRuRR1Gzw3tmRZDa0H5q-NGZI39G-RVrMsV1zehfR78Z6AaPfPmQHd1Jf3EyAKzXH8iGtTuttVsNJD65KmR7PKQk9KFZC9Iptz6k_ENIjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چهره اصلی اعتراضات دانش‌آموزی فرانسه
با چفیه فلسطینی که در یک ویدئو
رهبر جناح چپ افراطی فرانسه را می‌بوسد.
ائتلاف ارتجاع سرخ (چپ) و سیاه (اسلامگرایی)
همان دو گروهی که عامل انقلاب ۵۷
در ایران بودند و سیاست خارجه و داخله
و جنگ و بحران و تنفر و انزوا
و عقب افتادگی  رو برای ایران آوردند.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/6804" target="_blank">📅 15:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6803">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04f7f5c283.mp4?token=M-vVWDWPMpJivFZZuZTORBlAn-bTq9TVe-Vp5DSpOHoyuS4G9pi3FIZycXMb0Raxuzhkf_bNWBdw_842bXeSP2M5ubJFsRu63lAhlXm9UKXCx3EdSAgH97KKyJ_SQ9Qb9YUdZE402RewgEmilvsRuRNFHhCKF9QhmSeJNWNtzGhvHmFhFt4YwsGpn0vdQg6yHx7niYLF0yCpKmGW1UYEaDexYQcHhw1u1YDMvzHBa1q-QfmSbthG4qH980sC_2yB80RfUP-nI0phoX4W7KKPhSO80Uouu__F4H1PyBK5iFnzdVyhRLbFOOepkzztX1nA0ioBMLfspsM4o9E51VFGQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04f7f5c283.mp4?token=M-vVWDWPMpJivFZZuZTORBlAn-bTq9TVe-Vp5DSpOHoyuS4G9pi3FIZycXMb0Raxuzhkf_bNWBdw_842bXeSP2M5ubJFsRu63lAhlXm9UKXCx3EdSAgH97KKyJ_SQ9Qb9YUdZE402RewgEmilvsRuRNFHhCKF9QhmSeJNWNtzGhvHmFhFt4YwsGpn0vdQg6yHx7niYLF0yCpKmGW1UYEaDexYQcHhw1u1YDMvzHBa1q-QfmSbthG4qH980sC_2yB80RfUP-nI0phoX4W7KKPhSO80Uouu__F4H1PyBK5iFnzdVyhRLbFOOepkzztX1nA0ioBMLfspsM4o9E51VFGQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روز ۷ اکتبر ۲۰۲۳  وقتی به اسرائیل حمله کردن،  نوشتن که دنبال کنیز اسرائیلی هستن!  هر چقدر اونجا کنیز گرفتید اینجا از تنگه‌ پول در میارید!</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6803" target="_blank">📅 11:29 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6802">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AGOey_jBLBxLdpyqfgjQ6yjG5SXM9Y_BC1Eo5u_9ziTd6Ab5PkydFXpZzms3lAZB_iZdgrzXGZKHQRgFhZlmJS0jhYIvn2r4ycW6xwUW_0P9eoijkIqy2OZjJimxkyHSiozJ9TDjd6yLoKb2ImlGI7t0PohtRx39at9KRyV0B5HzsaOv1oY-ljON9b2-nsRWHKTBIyBol7VSalGopyUbArXtwPX__KIND5nyLA-SampYzI8g1nbGfBZQix2VlT2UheRd8wHJDbCgHSnc_M73t6eF5kLetBzD2mhkqG_bi1eUxbiqhHOewnjflG_96sPseWlvP88SFuAk4UdM9m8KLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌د‌ونستید یکی از معروفترین آیات قرآن  که آخوندها دائم به نفع خودشون و شیعه و….. استفاده می‌کنن آیه ای است که دقیقا و مستقیما در مورد یهودیانه؟  یعنی قرآن وسط تعریف یک داستانه، و آیه  قبل و بعدش داره در خصوص جدال بنی‌اسرائیل  و فرعون صحبت میکنه و  اینکه خدا…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6802" target="_blank">📅 10:52 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6801">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aVSSSoBFcueDN7cZPuL9S2uU8g79KviGtO2fanbA9v9_NGYmgtKUIl5_D9Y_UlOdqHRZ-Rm0n4b_jv06gpuKXgPv7mtqWrS8lIS3uXihzEtgr5iln4J_Z970PcSDcSDhP8EoIAqHyOAeXhzIUuycP0-40FC12VbHY0W4bWl_ShOgZXi0hAKjIYCjMQakEzkWx56Jl0rdPQ7C1YEOXyHYJdGhzvT4AR3Vxe57xbyPPzu5WUQ8oyxexFTUqcpJv5dNBUdVDtkLOxHU6eD0VyC62J9R3pMiz3HL4-APYPFfpwMUJzPkjg1qOGcUSxUyR9mpC2yLo5BAdotGGWY84VGcQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌د‌ونستید یکی از معروفترین آیات قرآن
که آخوندها دائم به نفع خودشون و شیعه و…..
استفاده می‌کنن
آیه ای است که دقیقا و مستقیما در مورد یهودیانه؟
یعنی قرآن وسط تعریف یک داستانه،
و آیه  قبل و بعدش داره در خصوص جدال بنی‌اسرائیل
و فرعون صحبت میکنه و
اینکه خدا اراده کرد امت بنی‌اسرائیل
رو  پیشوا قرار بده و البته «وارث»!
این آیه مکی است و این نکته مهمیه!
چون آیات قرآن در مکه همه در مدح و ستایش یهودیان و مسیحیان بود، تا زمانی که اسلام در مدینه قدرتمند شد و شمشیر و سرباز هم به دست آورد!
اون موقع آیات متفاوتی نازل شد سراسر سرزنش یهودیان و مسیحیانی که مسلمون‌ها  رو تحویل نمی‌گرفتن!</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6801" target="_blank">📅 10:42 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6800">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">روز ۷ اکتبر ۲۰۲۳  وقتی به اسرائیل حمله کردن،  نوشتن که دنبال کنیز اسرائیلی هستن!  هر چقدر اونجا کنیز گرفتید اینجا از تنگه‌ پول در میارید!</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/6800" target="_blank">📅 10:41 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6799">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebe3608b04.mp4?token=OqiPacSLiV-543iADiGO_l_rqHorI5n9q4lsQqPIwLiJssmCknCjfqr86LbzvPbORXPicUUdKS7nylB-4oCfdMvZ19bAzNeR22-4sK5k4jPCYDNs28crux6t8ulqdhtIDv7oq5v86N8stmRgnIZJfpWqob08fxeHJ1CWbsRpJzrToFp3Ad2IodSPtHBjP4X91xXtK7lrxalJGHfKsTViiP77V8hCwj6vbcPne1CvOC0j_zd070cSGmsIpRptm4qvfmRP0uM-dxvNHgPK0ZTLi-rKdQhlf4RmV3rFwOsvmUPjaxz5duI0IjcOyb9BXSS71IyRzI5hRVIIHrnV3uhoa13JWCEvlmqPn1lMpBsSmaVRdEWrzVmT24UnmQVU7EIBsBSqcnPT0QQ4PblStEBseKMG_d-3mz8GVq9dotcqmXDw8_pJVCxnIJYCSMFIb3TXYPdWmg1MrZrjMdqb1yMV3izAmHGDeeAPDmr-6eUdPOMksL-hzmO7-lk2scH6PRP4GZCBRiAcPiyTynLBr5l5o7ocHsThmbNcqX6H0i2CmUac_MJapiMPT82Sd9Rf3M857oC0CmagDW5EKQQEscLRiVldJgX64YKFPc-76mCnTG-DBIawjAILCvusNy4ijoVe8ORpOE2Ib-3Hiz5z1ZVfinEGXcC2iaJnuFJsKSkhngc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebe3608b04.mp4?token=OqiPacSLiV-543iADiGO_l_rqHorI5n9q4lsQqPIwLiJssmCknCjfqr86LbzvPbORXPicUUdKS7nylB-4oCfdMvZ19bAzNeR22-4sK5k4jPCYDNs28crux6t8ulqdhtIDv7oq5v86N8stmRgnIZJfpWqob08fxeHJ1CWbsRpJzrToFp3Ad2IodSPtHBjP4X91xXtK7lrxalJGHfKsTViiP77V8hCwj6vbcPne1CvOC0j_zd070cSGmsIpRptm4qvfmRP0uM-dxvNHgPK0ZTLi-rKdQhlf4RmV3rFwOsvmUPjaxz5duI0IjcOyb9BXSS71IyRzI5hRVIIHrnV3uhoa13JWCEvlmqPn1lMpBsSmaVRdEWrzVmT24UnmQVU7EIBsBSqcnPT0QQ4PblStEBseKMG_d-3mz8GVq9dotcqmXDw8_pJVCxnIJYCSMFIb3TXYPdWmg1MrZrjMdqb1yMV3izAmHGDeeAPDmr-6eUdPOMksL-hzmO7-lk2scH6PRP4GZCBRiAcPiyTynLBr5l5o7ocHsThmbNcqX6H0i2CmUac_MJapiMPT82Sd9Rf3M857oC0CmagDW5EKQQEscLRiVldJgX64YKFPc-76mCnTG-DBIawjAILCvusNy4ijoVe8ORpOE2Ib-3Hiz5z1ZVfinEGXcC2iaJnuFJsKSkhngc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دو روز پیش به فراخوان یک اینفلونسر مسلمان
و هجوم جوانان عمدتا مسلمان در شهر «وینچنزا» در شمال ایتالیا، شهر  به آشوب کشیده شد.
در این ویدئو یکی از دیگر از اینفلونسر‌های مسلمان رو به دوربین به صراحت میگه :« باید اصول کشور مبدا خودمون رو به اینجا بیاریم. باید به کشور مبدا خودمون احترام بگذاریم.
دیدید دیروز در فرانسه چه کار کردیم؟
همین کار رو در این «فاکینگ» کشور [ایتالیا] ، این کشور گوه، انجام میدیم! تغییرش میدیم ، مگه نه؟ تغییرش میدیم!»</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6799" target="_blank">📅 12:52 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6798">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tZyMKTdo9tWXDm3IqRKfNsXOxqzuQMJD6G6ykThT6dv-2ySnIhM4CKMENeOZIDBV-Uo03aOSUw6Hma64vVk2AQycakTqlgS5P4AjEOgEcNVF03q9FY2ZJU0p4IgWAXmSy_UFwdmS3-gM9-tMIO949M7VMmg89GAtchbctA5bchSBat6yhElC3zpF_E2OeDXKIIfMHNIm7MKz-eDch7RwC7P1bPLUrkwdw-J7XLO7A9j_4BtWfNeckGE62fg0ZdM1DQ9-7U6e-HRbYmQubQ3PPvgu1Yp0uTvKB8m4V3i6pognp0WnoV4k2bbKvsjIFrn-6ZpYsMYuyDfilgH3U4M4hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه فرانسوی لوپون از همکاری چپ افراطی فرانسه و «اخوان المسلمین»  در تخریب‌های اخیر خبر میده. دولت فرانسه نیز دیروز بر اساس اطلاعات نهادهای امنیتی از حضور چپ افراطی در گسترش دادن اعتراضات و به آشوب کشیدن اعتراضات خبر داده بود.  در حالی که اعتراضات دانش‌آموزان…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6798" target="_blank">📅 12:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6796">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CuU_5cFBShMrvn57Ih5hrOHsJpMdyIjnbaRw4iR7zkp-5v1daKeeYqBpau1V7b2T_ugDLug8rfXajC80-h3BM2OAjCBvZMdhPUBvgJkrsHJULu4RhiGuOwSIzIC_V3507TTMga9ZGcs6DjCbIht-wYx6NTod2uRqaG_n-c8tF3rk-ooLVFgv8l2TBNl0yBJzq84EoTDeWvREsdPEBK3BeO1qzOcBy9lDypM-_BTiyoWOTW92RQxTQJjHKCfLiFMafqCmUrkHJWxaITKAEBHvMEUMWPa25Zm5BIh-XX4yI0U6XJ9V23bVja8RKflmnVxvDjJrlTpMW2AxOkJhIOR0uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NVq3mZsFqs0CVPqRmqvcuHjWpix8wwbUZrRHr6t34dwA8mYUVISm7TO9D2_HQPRY-i-5M-EbKzs7QBNfKJT_27i4Q6f-wuICk_VMszmonBtI1DVI1fMO-fn3fEEc_dFmNgstTOLUJephE3gVgoN0bBML6PCqmpO58fQOaVX3kj1-VzGi923zLeYHi6B4fsang5qP-rUoH8L1M1TzStLhiCX665u6P2euZ7pfbZVEgRqRoZpusDiDdXgIf4v8IBx4ncXdtRH8mUZPKYHvBdMbSjjxzm9r_57icCmANL2rDZP5xObk4CYUJaGeJfXYm2AaOlARqrY_FLXFU2Ees9Jrqw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روزنامه فرانسوی لوپون از همکاری چپ افراطی فرانسه و «اخوان المسلمین»
در تخریب‌های اخیر خبر میده.
دولت فرانسه نیز دیروز بر اساس اطلاعات نهادهای امنیتی از حضور چپ افراطی در گسترش دادن اعتراضات و به آشوب کشیدن اعتراضات خبر داده بود.
در حالی که اعتراضات دانش‌آموزان فرانسوی
کاملا مشروعه و دولت بهشون مجوز میده،
عده زیادی با پرچم فلسطین، الجزایر و مراکش،
در تجمعات حضور دارند و دست به تخریب میزنند. دقیقا مثل هر بار که بازی فوتبال هست
و همین جماعت شهر رو به آشوب میکشن.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6796" target="_blank">📅 12:43 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6795">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">می‌د‌ونید چرا جریان چپ اینقدر خودش رو
هم داستان و همراستا با آخوندِ جنایتکار دیده؟ می‌دونید چرا اینقدر چپ از جامعه ایران
متنفر و خشمگینه؟
چون همه هویت و هستی اینها مبارزه با آمریکاست!
ایران اگه یک پایگاه ضد آمریکایی و یک کوبا
و یک ویتنام بشه براشون ارزش داره!
ج‌ا، چپ‌ها رو قت@ل عام هم کنه براشون مهم نیست!
چون هدف و نقطه مرکزی آمریکاست.
همه هستی‌شون در این تعریف شده که جایی آمریکا
حمله کنه و اینها سریعا بیان وسط میدون
و ضد آمریکا شعار بدن،
در قضیه ایران ناراحتن که چرا آمریکا حمله کرد
و اکثر مردم ضد آمریکا نشدن؟
البته به جز اقلیت مزدور اسلامگرا و اقلیت بی‌آبروی چپ که هر دو اساس انقلاب ۵۷ رو داشتند.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6795" target="_blank">📅 13:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6794">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">مثال دوم گنده‌گویی‌ها و شعارها که کار رو به جنگ کشوند و به شکست سنگین  هم ماجرای شاه اسماعیل صفویه شیعه افراطی بود که چند باری داستانش رو مرور کردیم که دائم نامه‌های فحاشی  برای خلیفه عثمانی می‌فرستاد،  یک لباس زنانه هم همراه با نامه می‌فرستاد،  پایان نامه…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6794" target="_blank">📅 14:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6793">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">بالاخره امام علی در کوفه  تونست ۲ هزار نفر جمع کنه!  برای کمک به محمد بن‌ابی‌بکر!  در حالی که در خود مصر ۱۰ هزار نفر مصری جمع شده بودند علیه محمد بن‌ابی‌بکر و به لشکر ۶ هزار نفری عمر و عاص پیوسته بودند!  این ۲ هزار نفر از کوفه،  تا راه افتاد و …..  هنوز وسط…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6793" target="_blank">📅 13:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6792">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">امام علی هم که خلیفه بود و در کوفه بود، قبلا هم گفته بودم که کوفه (و بصره)  اساسا شهرهای پادگانی - نظامی بودند. احداث شده بودند برای حمله به شهرهای ایران و تصرف مناطق مرکزی ایران.  با این وجود به خاطر جنگ‌های پشت سر هم مثلا جنگ صفین که نزدیک دو سال طول کشید،…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6792" target="_blank">📅 12:57 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6791">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">کار به جایی رسید که جنگی بین  محمد بن‌ابی‌بکر و «عمر و عاص»  بر سر حکومت مصر شکل گرفت!  عمر و عاص، دفاع قبل توضیح داده بودم که اولین حاکم مصر بود!  و جایگاه محکمی هم در مصر داشت!  و مرور کردیم  که اوضاع مصر هم از زمان حکومت  محمد بن‌ابوبکر از لحاظ اقتصادی…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6791" target="_blank">📅 12:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6790">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">معاویه برای محمد بن‌ابو‌بکر  نوشت که تو که هر بار توی نامه‌‌ات علیه پدر من می‌نویسی، و یادآوری میکنی پدر من فلان بود و بهمان بود، پس من حقی ندارم و خلافت حق علی است،  پس چرا پدر خود تو (ابوبکر)  همراه با عمر در سقیفه بنی‌ساعده،  حق خلافت رو از علی گرفتند ؟؟…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/6790" target="_blank">📅 12:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6789">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">بعد از چندین نامه تند که معاویه نامه‌ها رو هم می‌فرستاد برای نخبگان و مردم مصر،  (البته محمد بن‌ابی‌بکر هم خوشحال میشد که نامه‌هاش خطاب به معاویه،  دوباره برمیگرده به مصر و‌ مردم مصر هم می‌بینن نامه‌ها رو!  اما قضاوت مردم به سود محمد بن‌ابی‌بکر نبود! نمی‌گفتن…</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farahmand_alipour/6789" target="_blank">📅 12:33 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6788">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">محمد بن‌ابی‌بکر نامه می‌فرستاد بدون سلام!  همون اولش به مادر معاویه فحش میداد!  (این موضوع فحش دادن کلا در بین شیعه به شدت رایجه! حتی در متن سخنرانی‌های امام حسین در کربلا!  یکبار هم مستقیما معاویه برگشت به خود امام علی گفت تو با من مشکل داری با مادر من چی…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6788" target="_blank">📅 12:27 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6787">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">مصر، ثروتمندترين استان حكومت اسلامى بود،به خاطر جلگه رود نيل وكشاورزى پررونق و...! به خاطر اينكه در دوره حكومت امام على ساختارهاى اقتصادى رو عوض كردن وساختار جديدشون رو هم نتونستند به درستى پياده كنند، اين مصر بسيار ثروتمند فقير شد!! يعنى اوضاع اقتصادى داغون!…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/6787" target="_blank">📅 12:22 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6786">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">این رو هم در نظر بگیرید که امروزه به خاطر حدود ۴۰۰ سال تبلیغات یکطرفه، اکثریت مردم ایران میگن حق با علی بود و معاویه در سمت اشتباه بود!  اما در اون سال‌های اولیه اسلام،  چنین شکاف و فاصله‌‌ای هنوز وجود نداشت!  بین نخبگان بود!  برای عموم مردم، جایگاه این افراد…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/6786" target="_blank">📅 12:16 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6784">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">محمد بن ابوبکر  یکی از نزدیکترین چهره‌ها به امام علی بود که حاکم مصر شد!  یک جوان تندخو! از این حزب‌الهی‌های افراطی و عرزشی‌های گنده‌گو!  نه سن کافی داشت! نه تجربه داشت!  اینو امام علی گذاشت حاکم مصر!  حکومت خودش که متزلزل بود!  چون وسط آشوب کشتن خلیفه سوم…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/6784" target="_blank">📅 12:08 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6783">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">پس تا اینجا همه می‌دونیم که  فقط شعار ندادند!!  همه ما این قوم رو می‌شناسیم و ۵۰ ساله که حیاتشون در تنش و بحرانه!  اما فرض بگیریم،  فقط شعار دادن و حرفهای تند زدن بود آیا در تاریخ داشتیم که حرفهای تند زدن باعث جنگ و ….. بشه؟   بله! و اتفاقا دو مثال روشن در…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6783" target="_blank">📅 11:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6782">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">لابد در این ماه‌های اخیر زیاد دیدید که حامیان حکومت،  در دفاع از خودشون میگن :  بله درسته، ما نیم قرنه علیه آمریکا و اسرائیل شعار میدیم، ولی کدوم کشور به خاطر  شعار دادن و پرچم آتش زدن و حرف،  حمله کرده به یک کشور دیگه؟   البته که همین جا هم صادق نیستند، …</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/6782" target="_blank">📅 11:44 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6781">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">لابد در این ماه‌های اخیر زیاد دیدید
که حامیان حکومت،
در دفاع از خودشون میگن :
بله درسته، ما نیم قرنه علیه آمریکا و اسرائیل
شعار میدیم، ولی کدوم کشور به خاطر
شعار دادن و پرچم آتش زدن و حرف،
حمله کرده به یک کشور دیگه؟
البته که همین جا هم صادق نیستند،
چون اونها فقط شعار ندادند!
خامنه‌ای رسما در برنامه «گام دوم»
که سیاست‌ها و اولویت‌های جمهوری اسلامی
رو برای ۴۰ سال بعدی تعیین می‌کرد،
اخراج آمریکا از منطقه خاورمیانه
و مبارزه با اسرائیل رو رسما جزو برنامه‌های نظام قرار داد، بگذریم به اینکه در عمل و با افتخار و صدای بلند می‌گفتند ما به گروه‌های تروریستی حزب‌الله لبنان، حماس، جهاد اسلامی و….. موشک، سلاح و پول میدیم برای مبارزه با اسراییل و….!
هر گروه دیگه هم بخواد مبارزه کنه،
بهش پول و سلاح میدیم! اینو خامنه‌ای هم علنا گفت.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6781" target="_blank">📅 11:37 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6780">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HllaTK_6outwrE-WsAvFdF9M-ZPemAcPUFw3434UDKYUGxa8AEkhTTId4OixCsV9JTBAch4PUvDkjKZmOg8Y7PRxSaH5AyWcK_Fv565E6AQUrafktySj8bt99fjj-9iyjk6ltLkZvxE0wyxVAI_M2v8sFFWnw46bYvED3-684P_S0B1stl1OC-rJ2nonCL9XMfQLE7ZfqZOl9x-MZMksEAbUDUtvJQrNKwIwBl4me_KxkNXSkwAOTvFF0HpscDwEyvi8e8HLJTk_MdGU6MujAO_R-FCVTD9FUeo89Dh_d8PzTkeh7Lt1tNlzFRHf4ukaUOCNaq6nolqA-Q0eJxdtyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یورو شده ۳۰۰ هزار تومن!
و دلار تقریبا به ۲۷۰ هزار تومن رسیده.
ولی یادمون باشه که بزرگ‌ترین
فروشنده و عرضه کننده ارز در بازارهای ایران
خود حکومت و عوامل حکومت هستند!
ارز دست اونهاست!
صادرات دست اونهاست!
حکومت و عواملش خودشون دارند قیمت رو بالا
می‌برن، تا ارزهاشون رو به قیمتی بالاتر بفروشند
و سود بیشتری به جیب بزنند!
اساسا برخی از دامن زدن به جو جنگ و التهاب،
کار خود حکومته و مافیای حکومتیه، برای افزایش
قیمت‌ها و افزایش قیمت ارز
و افزایش درآمدهای خودش!</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6780" target="_blank">📅 14:21 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6779">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">بلومبرگ به نقل از منابع آگاه:
جمهوری اسلامی  پیشنهاد داده در ازای لغو تحریم‌ها، اجازه دسترسی بازرسان هسته‌ای به تأسیسات بمباران شده خود را بدهد.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6779" target="_blank">📅 22:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6778">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PbGUbEdrufSqhWFTv0B729KSC-YnOCk_FmJ6kMiAJSo9h8T3pOmfpnlZFaEZs_Wi49lKOVYQUTQQut5ZFa1YCjDn_t5sJlx4SZ8N4otPrpTYRllzKfq0HPMVEdKn49x802R4dLSNw_WQoZpNm_K9KffsPrtsaUaew_EiIdelw4HmoH5bL0yAWgtzwGwB1goJXgQzW0CHgY3-DHWQnZ9x_4oxM0k2qk-fXRHNhP5l1EuBDm1gWFF43G0ihfJhWmsi_wBXYys2fMjGWZSv9EE64sx3lOQO956JIx1DvmhTbWj_TNmBZrovHyO7u7aMxndgZePtc98u1qTGcA1SEyTAlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی این ۷ شرط رو داده
به آمریکا که در قبالش  ج‌ا تنگه هرمز
رو «باز کنه»! آمریکا گفته تنگه هرمز برای شما بسته است!
برای ما که بازه! نفت که داره عبور میکنه!
و اصلا درباره تنگه هرمز مذاکره نمی‌کنیم!
اینها مثلا زرنگی کرده بودن بریم تنگه رو ببندیم در آستانه انتخابات قیمت نفت بره بالا،
آمریکا بیاد گریه و التماس کنه!
برای «زمستان سخت اروپا» هم منتظر بودن روسای جمهور اروپا برن بیت رهبری گریه کنه، لکن هیچ کس بهشون محل نگذاشت و خودشون دچار مشکل کبود گاز و برق شدن!</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/farahmand_alipour/6778" target="_blank">📅 09:57 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6777">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a-fqusdwsNCMOSgqzRtuterUzEXFSX98buGeptGiRWl-N2YWlnqQtyjFjZzduzy-TLYHeH1ni3iwxTJFKw7yjS758zO3YuxdTsXJIbMSFlXaXg_E7spu9RyBEOuwJocxHre-q9F5XzkKzcGarMF7UumgHThb03BiP64TFaYQkvuFey5KaRsipC2XMCYuVZwmLe_uF4cEC0RHlLUJ8ClranRz3_Q1Czsdf6FC_Bo-CgOdMYux5fNDBchTc3zVnPPRr4B1QfBUx91Pmq0LP8J_xaD5viMoZ2WxEm6zP3adsZ_0vDhhn5sHmb9h6I84TovcM9ZHJuPnI74VAZ3J5VrK4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزش واحد پول ایران، «ریال»، قدرتمندترین کشور جهان در محاسبات الهی، در برابر «دلار آمریکا» رسما «صفر» شده!
در زمان حکومت صفویه،
و بر اثر سیاست‌های شدید مذهبی شیعه‌گرایانه شاه سلطان حسین (مردم بهش میگفتن ملا/ آخوند حسین)  مردم اصفهان از زور گرسنگی به مرده‌خواری افتادن،
علمای شیعه از همین هم یک پیروزی
ساختند و گفتند همین خودش نشون میده که دیگه وقت ظهوره و امام زمان داره میاد و ما بر جهان مسلط میشیم و….
چند روز بعدش شاه سلطان حسین
تاج شاهی‌‌اش رو با دست خودش گذاشت روی سر یک شورشی سنی مذهب افغان و خواهرش رو هم به همسری بهش داد و امام زمان هم نیومد!</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/farahmand_alipour/6777" target="_blank">📅 08:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6776">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c578cb6e91.mp4?token=ONPTiPEOrRiEkt2Oc-rw85cL4nGjIZ1HMbTEuBeFxxue5g8lZzyDLv8OWy4_ms3qy3FXMPpmqwLSR0cirinwWVA5S5JUICLfBY7W29dcgyz0E5MqZGlgSwUqKGi3kDHRcoVM-AptvKnph9uEspyTmBNO7HVTexTdUOLTc91--SMb29fNytepjxfOP1eXxdO24YyjcD-vTn8qUqAlAELfX_ulYY3rTTmbwAvvLNUpwKrUb4Dgmnyh8NH29AB2YIoFnrS9ga092E3iuJU6HLJKtPrsY5MyoWI4JSQ0rJzAW_Im3xQ89hAZYYaBbS0rPIOsJyRTbTkS92E-sHAP5nfoxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c578cb6e91.mp4?token=ONPTiPEOrRiEkt2Oc-rw85cL4nGjIZ1HMbTEuBeFxxue5g8lZzyDLv8OWy4_ms3qy3FXMPpmqwLSR0cirinwWVA5S5JUICLfBY7W29dcgyz0E5MqZGlgSwUqKGi3kDHRcoVM-AptvKnph9uEspyTmBNO7HVTexTdUOLTc91--SMb29fNytepjxfOP1eXxdO24YyjcD-vTn8qUqAlAELfX_ulYY3rTTmbwAvvLNUpwKrUb4Dgmnyh8NH29AB2YIoFnrS9ga092E3iuJU6HLJKtPrsY5MyoWI4JSQ0rJzAW_Im3xQ89hAZYYaBbS0rPIOsJyRTbTkS92E-sHAP5nfoxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند سال پیش یکی از دوستان با آب و تاب تعریف می‌کرد از سیستم پیشرفته
بانکی ایران و کارت و انتقال پول با کارت و …
همون موقع بهش گفتم این گسترش سریع
فعالیت‌های دیجیتال بانکی به خاطر پنهان کردن بحران عظیمی است که اقتصاد کشور باهاش دست به گریبان شده!
وقتی پول نقد دستشون باشه خیلی بهتر متوجه میزان بحران اقتصادی کشور میشن تا با پرداخت آنلاین و کارت و…!</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6776" target="_blank">📅 12:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6775">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a5052b840.mp4?token=j4-sEcURCdAHn03dfU7lgkukZ0w56PZ6IA5XkIQmANJ0_bGtQDwOwmtcHot8z7l_YAJdcdwnGQ1w41xA3kButqH7IzmEOM9r7AMO_IuQrrTDcY6iwCbz1t5GOrCyT6vvHt5mk6XdT1bQew8iQfZjqUY_opiLkWY-g5WTwh0YBYGfM_u32T4MKdE-vcR9vRe0Qh0j8mR0JXBbkp2W2hcRgWVce3GaREEw-0V2Z_yTQDEtKra0IjYqRt0f7taNxWOcwYoHm0YsaEdxGd35vWERqA9wcnFx2XPXl-XtwY6uz0i0-lsqQStIDremo4ziMLbXChjPXww3Lw1Ra6bjTHfaqXQu4feo5OHrH9uc-Qppr5eYW1BdroKJxLRDCFu3ZAMyUQ2Cyo7Oueg9Mf5OfhgCj329Ss25Zur3QhJ0QEvMMYg_AA2iGjsrSd2MnVWufGBYOJumSH8xcu_RTDORF4Z3eG-W-vboVhXwpD7GfJ1-Ri_JDE8ExJLABU3Ys3AnMvj5Aj7bowFsz35M8NQ8_DDCe-w9L0aePIumJWZkV_SkTGsBeN6L16uHZZtLwxflhthUbknby5haLR8w94jC0s-2KPvfjOlam80NMO8xVq36Cx-SEBXbIHwPnsXclNGX1Go43y4fQT9qncJlw4EgHk7DyNLsIhu90XuZEijB6_yb7f0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a5052b840.mp4?token=j4-sEcURCdAHn03dfU7lgkukZ0w56PZ6IA5XkIQmANJ0_bGtQDwOwmtcHot8z7l_YAJdcdwnGQ1w41xA3kButqH7IzmEOM9r7AMO_IuQrrTDcY6iwCbz1t5GOrCyT6vvHt5mk6XdT1bQew8iQfZjqUY_opiLkWY-g5WTwh0YBYGfM_u32T4MKdE-vcR9vRe0Qh0j8mR0JXBbkp2W2hcRgWVce3GaREEw-0V2Z_yTQDEtKra0IjYqRt0f7taNxWOcwYoHm0YsaEdxGd35vWERqA9wcnFx2XPXl-XtwY6uz0i0-lsqQStIDremo4ziMLbXChjPXww3Lw1Ra6bjTHfaqXQu4feo5OHrH9uc-Qppr5eYW1BdroKJxLRDCFu3ZAMyUQ2Cyo7Oueg9Mf5OfhgCj329Ss25Zur3QhJ0QEvMMYg_AA2iGjsrSd2MnVWufGBYOJumSH8xcu_RTDORF4Z3eG-W-vboVhXwpD7GfJ1-Ri_JDE8ExJLABU3Ys3AnMvj5Aj7bowFsz35M8NQ8_DDCe-w9L0aePIumJWZkV_SkTGsBeN6L16uHZZtLwxflhthUbknby5haLR8w94jC0s-2KPvfjOlam80NMO8xVq36Cx-SEBXbIHwPnsXclNGX1Go43y4fQT9qncJlw4EgHk7DyNLsIhu90XuZEijB6_yb7f0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو : ‏مشکل ایران انقلاب است. مشکل آن مقامات دولتی نیست که کت‌وشلوار پوشیده‌اند و در برنامه «میت د پرس» ظاهر می‌شوند و در رسانه‌های آمریکایی آزادانه حرف می‌زنند.
‏ما در مورد آن‌ها حرف نمی‌زنیم. کسانی که در ایران حرف آخر را می‌زنند، روحانیون رادیکال شیعه هستند که نگاهی آخرالزمانی به آینده دارند.
‏آن‌ها باور دارند وظیفه دینی‌شان این است که آخرین روزهای دنیا و آخرالزمان را به راه بیندازند. می‌دانم این حرف برای خیلی از بیننده‌ها شبیه فیلم به نظر می‌رسد.
‏اما واقعیت همین است. این هدف اعلام‌شده انقلاب آن‌هاست. چنین آدم‌هایی هرگز نباید سلاح هسته‌ای داشته باشند، چون از آن برای باج‌گیری از دنیا و کشتن مردم استفاده می‌کنند. این خطر غیرقابل‌قبول است.</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/6775" target="_blank">📅 08:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6774">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ckOceXuwfnjhHU1_KaqlInO7LM0EkTwChF7oD_ujDZEnjTkL0lyy7nKyWN9IHMhSeg0MCCll7YFhWxLVgAVqfFsRX0z0Py_XekWYyOdEDv9V-EvRATfo74Dm9YETPlMODKnJX9RvwI3FisyK9ZpqXgz2LtleMqZbCQ2EeYY5i80nq1bMG2DnOUItsjSyW0vS7qo1tM91MWWXLTPsNiLBZvfc2hQuhAdTQHwZJrB_QjGBwToMwDLUrYJsoq8dHUEIxcxOcLghW9IBIDHlJIM6_s-sMHKx2N9sEdY8FAmIl0dk_BoTQHA_0Exepx8JRyJJJYUPNF7smbky3X9_McZPxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/6774" target="_blank">📅 02:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6771">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fGlwlYcbcFl60BibkdRlGZxMFWcNKgyGwj7VB7BIqGWSHE613U3IrRNlAPOe5CH-qZKcTMrIIYndWNol7ZDsw4E4BQRO9FVsIWHy_vkAIIac13vy5WvDA6hT3eEApGZOo8gDIHqP-SAAOTH-HPczaRF5BEb5qaCsFK5KlLHsTi4zhAqNsyzO7p5frDKHPvFfGwzLP6J66IIWodsxLMouN_9Fvfm2Xzg8idJ1-aMwAR9rJ4ZYPgQpw3ktc9CSxh9ddS6JdnodN3HlRRP6FYDMBQtmBe4CBEuwhbhMeq3GfXcIACQFlKp8pYQkCfUuLOVW4_3OEiewGEbEFb_QqK4Nbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bGcaetc_zZ-jfvmkolgg-xAUd1ImIZmcMIeeh2szEGPKp_lFA17z7JLzB6zmNbqe4j6DBXnLP6eNNSR_8kpEKqccwzuPSJX89zpVg1usdsFKdKG6cL5CbWveEuo80sZzgVBNZI9pyGq8yY7K6i84lJK6IgJLR19vembRpaIzAGnT9THK7ohoPcayOyc34lLSBEpVtPBdVTwfCeuhPvXeAwhPSOc3_Eu25bHKlE9lyJKqNSR_hb840untw5EsIHEnqN5i3RU3R6XW3sNHCP5HpqdtV4Z7PSsr95tqXyxfdPJLHSczc8fom6HdQ6SbtZWbkL4B-CorkdJYZRG-Rv36DA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/895be358cd.mp4?token=IWrrvQJ8sfrXT-DPVqwVFAv5DbODhi-FwGM4JN7FNjnr778tJq1g06-dJQ7fymPs6pyNEuLzgXFy8S8HkijWZ0PRiODmrOOOjV_B6kJT0CkFoPYdPBHazNLqxpAbzObQRoXiy_Se-pbjtRIqSWlQsv4xudma5tK5SJIrfS60Osa9XM-EeaTiCXttfywSI4aWinBAQeYY7ZUjpxc8plqZEjFOmpvCjX3wQJdzp2QywX4eQtqjoLAVQi7lnZx_yoI08syGKOqxKkJC-Yo5RugPgW_gwTfyLDngHibmKcYH7Pp1E2SNw9jwJbwPxfF6EcgnH_jwQUK37Rty8qUWniL2QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/895be358cd.mp4?token=IWrrvQJ8sfrXT-DPVqwVFAv5DbODhi-FwGM4JN7FNjnr778tJq1g06-dJQ7fymPs6pyNEuLzgXFy8S8HkijWZ0PRiODmrOOOjV_B6kJT0CkFoPYdPBHazNLqxpAbzObQRoXiy_Se-pbjtRIqSWlQsv4xudma5tK5SJIrfS60Osa9XM-EeaTiCXttfywSI4aWinBAQeYY7ZUjpxc8plqZEjFOmpvCjX3wQJdzp2QywX4eQtqjoLAVQi7lnZx_yoI08syGKOqxKkJC-Yo5RugPgW_gwTfyLDngHibmKcYH7Pp1E2SNw9jwJbwPxfF6EcgnH_jwQUK37Rty8qUWniL2QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دو سال پیش
حسن نصرالله، رهبر گروه تروریستی
حزب الله لبنان، برای چند هفته،
ویدئوهای تهدید آمیز می‌ساخت!
کج نگاه میکنه! انگشت میزنه روی میز!
رد میشه و…!
رسانه‌های جمهوری اسلامی هم جشن گرفته بودن که آقا اسرائیل «با یک ویدئو!!» بهم ریخت!
تا اینکه در روزی چون امروز
(۲۷ سپتامبر)  ارتش اسرائیل با احداث یک گودال ۳۰ متری (به اندازه یک ساختمان ۹ طبقه) در بیروت، به تهدیدها و ویدئوها  و گنده گویی‌ها پایان داد!
به همین سادگی! فقط چند ثانیه زمان برد!</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/farahmand_alipour/6771" target="_blank">📅 13:06 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6770">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=HFu8vo1fDQVCZyytZojk-PCl12qCfsiiDr7qHZW2gdRj6zOzAT2GXC2cSMDlo74idEJkbF8B80LblUQoEgSFQi3RGNX8tkvwuVh-vVLV85Se8LaQtKZL-LRZL9OMmyGz6HqWYWvGz8hQ_YtB_HGJhF_BcpAAetBxvdO7E5hyIkPJhBeCSjgCI-DJ1d7347XKxXHtNvLBGSIZtVH89ROJcVVG_7rZxeYhre5rtDmFb5Dvl_KM2wA6OEUGp6ccnVLEFl_SBmneG5IzsutEjmLPMWoQktEDh3-cNu0F887zx2Rh4m3pQlAFo0uVHD0_m_pTWx9hTWTwOVPzL2n01QBNGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=HFu8vo1fDQVCZyytZojk-PCl12qCfsiiDr7qHZW2gdRj6zOzAT2GXC2cSMDlo74idEJkbF8B80LblUQoEgSFQi3RGNX8tkvwuVh-vVLV85Se8LaQtKZL-LRZL9OMmyGz6HqWYWvGz8hQ_YtB_HGJhF_BcpAAetBxvdO7E5hyIkPJhBeCSjgCI-DJ1d7347XKxXHtNvLBGSIZtVH89ROJcVVG_7rZxeYhre5rtDmFb5Dvl_KM2wA6OEUGp6ccnVLEFl_SBmneG5IzsutEjmLPMWoQktEDh3-cNu0F887zx2Rh4m3pQlAFo0uVHD0_m_pTWx9hTWTwOVPzL2n01QBNGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افتادن به التماس برای بازگشت به همون شرایط قبلی!  ترامپ ولی رد کرد!    احمدی مقدم چند روز پیش گفته بود به کشتی‌ها حمله کردیم - و تفاهم نامه نابود شد - چون میخواستیم چند میلیون بشکه نفت رو به قیمت بالاتر بفروشیم!  می‌د‌ونید که بخش عمده نفت ایران در دست گروه‌های…</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6770" target="_blank">📅 12:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6769">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DiDkol_fBNs7J6uwsE1ucn756ibpSBcNRt6PGBxSRy79Gz3v7smrAHesrhFKU0ik8hrJDkg4dJn6CLoDVyWWEagPV2BVNQFOKU6gT86ddJXakaqtJkxbRX8tl2nexCCtyoGeOo9XsMw5CsqibpllPhkzf6zqfaVvXp2pcSZz3SR6VMXE0qi5PucHHtPqwcVM-qYT7zcxryhQbRknY6lwMfX29PjYaMOZtsjLB2Hm9FksQXXkV1A1HofGomTEpNR3TVjAyKK5vg1-yqDq8Pxt_7v7iByY9jwNtU_jzYuYMNevTBZ_FC-6JOKK22cShwlWdUq_rPqfcqlXKnma-WUD3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد  تا به دنیا فشار بیاره،  اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/6769" target="_blank">📅 12:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6768">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89284f5821.mp4?token=Hm9MfObF3ezMPkd_0nprucxa3_uCo1miOHgT_7n1TBGgsUbJHNKwaBE2LBn4JfqLzagvHFrOoEzy4iq8X6s5SZvYfl8djIKnFd8SiM3sBT-Mp-9wARvcKxpJv02h8fmz5J52O3Ty6vFGcHYe-xu0LvyrKlhzx6sxXHBDXwieVojYcP3DTJO9wo16HYzkwNIofkDEeE7LCeH9DlkA5cuq3WLrwUNjLNK0zRtN-uH8hVDyIyac8LGpy5lHTvvYXTuaP1VEIZDEPhucwI1nZY8Lq7E-EDtL_6Rw7pTWOCO9VUMWiVFpZZ1IewmYZWkQ-eU3wX52EbVemGIoBVYyHTWp_wKF-qy4iS1OS_NJFFtdgtWHezpBdzXgpsaOgrf7obJP40FaXSsyYUEtY6ETLtvFswoOx2KZBO0FFwoCLldouFzpsASXrEqvKlXavbZoRLWsHMDUSyexERa9un2pMBwZSjZCvr6Ee1KxbakoREbcjzSDIEbSnJZyCb8z5RBJ9VW5tQX7-NcCHvtrfQYCsGCZ-aUXgOde5JWeOZyrSJSED6-_t7i6hFZ0n7dyPkTFgEHgnQnQsQb2BRuSguRY1LcrdN1C6J5m-vQyF90IapOOMTCitevqIu4hoOq8Damat9PyvcJZxy_9KvQPF29Eo3AymtMSHtHwtQl_t_X79Tk6M1M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89284f5821.mp4?token=Hm9MfObF3ezMPkd_0nprucxa3_uCo1miOHgT_7n1TBGgsUbJHNKwaBE2LBn4JfqLzagvHFrOoEzy4iq8X6s5SZvYfl8djIKnFd8SiM3sBT-Mp-9wARvcKxpJv02h8fmz5J52O3Ty6vFGcHYe-xu0LvyrKlhzx6sxXHBDXwieVojYcP3DTJO9wo16HYzkwNIofkDEeE7LCeH9DlkA5cuq3WLrwUNjLNK0zRtN-uH8hVDyIyac8LGpy5lHTvvYXTuaP1VEIZDEPhucwI1nZY8Lq7E-EDtL_6Rw7pTWOCO9VUMWiVFpZZ1IewmYZWkQ-eU3wX52EbVemGIoBVYyHTWp_wKF-qy4iS1OS_NJFFtdgtWHezpBdzXgpsaOgrf7obJP40FaXSsyYUEtY6ETLtvFswoOx2KZBO0FFwoCLldouFzpsASXrEqvKlXavbZoRLWsHMDUSyexERa9un2pMBwZSjZCvr6Ee1KxbakoREbcjzSDIEbSnJZyCb8z5RBJ9VW5tQX7-NcCHvtrfQYCsGCZ-aUXgOde5JWeOZyrSJSED6-_t7i6hFZ0n7dyPkTFgEHgnQnQsQb2BRuSguRY1LcrdN1C6J5m-vQyF90IapOOMTCitevqIu4hoOq8Damat9PyvcJZxy_9KvQPF29Eo3AymtMSHtHwtQl_t_X79Tk6M1M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد
تا به دنیا فشار بیاره،
اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6768" target="_blank">📅 12:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6767">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0493705c07.mp4?token=Yssjzv_JQBggviuvkaKgT3wde-sNkOrW8TRuKdUthzWb9gGRGFvzNmTn907LoX6j2A2uHl7OgoCJXWqb0V2ug4d-ygQ4UaYQNMsrjHV6Fb2_L-souphNmbjd0JDajbv_-K1dGcvruLyirX-sjzvxluHtuhRw_ebY7QvLac1j3ksqmkV6wovEhtqN48jmcxNe2tneeFpoAefrEGt74LD_l7wNiWhL8Inj-Cckng-3LG62NhrH8Ot7yHD7S8kZoJ9DUGBovVukSmEbhKjLMSpk3hJkVjDy13dIT7vZxJK2ndu5NksK8L1cce3JFZzaI-zpQyPGxfQcFviy7AMPvYHtsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0493705c07.mp4?token=Yssjzv_JQBggviuvkaKgT3wde-sNkOrW8TRuKdUthzWb9gGRGFvzNmTn907LoX6j2A2uHl7OgoCJXWqb0V2ug4d-ygQ4UaYQNMsrjHV6Fb2_L-souphNmbjd0JDajbv_-K1dGcvruLyirX-sjzvxluHtuhRw_ebY7QvLac1j3ksqmkV6wovEhtqN48jmcxNe2tneeFpoAefrEGt74LD_l7wNiWhL8Inj-Cckng-3LG62NhrH8Ot7yHD7S8kZoJ9DUGBovVukSmEbhKjLMSpk3hJkVjDy13dIT7vZxJK2ndu5NksK8L1cce3JFZzaI-zpQyPGxfQcFviy7AMPvYHtsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موج جدید پناهجویان و مهاجران افغان
به سوی مرزهای ایران</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/farahmand_alipour/6767" target="_blank">📅 17:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6766">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LCTe_25bwZcmtIcnHY1_k4B_ZBDmdZELUcWBUGE_1wKjzAbbeFHaGbWwcad68QhkF05FTZk5r1Qminy5chm0dSa2KHdtWX8C7IUL8fgElX2KG0gjQ4Qq7JElPc3Ny2UcNsOJwfPAMzKJNkbjcBK8XyWrpMxg2Eq_iyA-CJZBtpkLxgZZG4irrzx4WPtiVopGcxGyOp8FKhiJdJ_babhZPQh0glK4791FvROA7YOjq8I_8xMM3QrijRWxVAbv3-0RbErysk2q5-MprA1r2Oxii7EtjxwGE4qHBr8mdyU2Pkif7q-kWuLeokcG7IOyN-hYhug7eqHeb3lP7mSAoNtxJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو و این حرکت یادآور داستان‌های عهد عتیق است!  شجاعت و جسارت فرزندان داوود!  که در عین جوانی و نحیف و خرد بودن،  مصمم و بی‌هراس،   مستقیم به چهره دشمنان خود می‌نگرند!  مثل داوود، نوجوانی ظریف و آواز خوان!  خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه…</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6766" target="_blank">📅 15:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6765">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=dv4sFlt2MSqqQA6b6zy_4Gn4Def-UvXP_6IEBq__M5qrMnZi-CCns-JLMFDyQma-28rXUgaj-2Csn8Zo6VSR4WSLcvsI_Hxf3ZeLlyEfwJPNR05JupJ_MgZaeOdmjt7X3H5dpIDO-I0EqSYBRjaqarHq1O2K0h_iM5qzqDXaXOtVa674uRXP191IdMWkFUTypwBOLplxUh4h2aZiy2ua6mYy2CcqN4CUOdo7SBBguOHjSwA9Ary5cFcUUzGo-FLAcAR7cdzqIBFG9uWY4TNwXtou0biu4CeDtODVJJo2CfWiwYlxMQcHhegfiQZBy8mDIjkmfzgsRkkIZ8wv4fUuFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=dv4sFlt2MSqqQA6b6zy_4Gn4Def-UvXP_6IEBq__M5qrMnZi-CCns-JLMFDyQma-28rXUgaj-2Csn8Zo6VSR4WSLcvsI_Hxf3ZeLlyEfwJPNR05JupJ_MgZaeOdmjt7X3H5dpIDO-I0EqSYBRjaqarHq1O2K0h_iM5qzqDXaXOtVa674uRXP191IdMWkFUTypwBOLplxUh4h2aZiy2ua6mYy2CcqN4CUOdo7SBBguOHjSwA9Ary5cFcUUzGo-FLAcAR7cdzqIBFG9uWY4TNwXtou0biu4CeDtODVJJo2CfWiwYlxMQcHhegfiQZBy8mDIjkmfzgsRkkIZ8wv4fUuFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدئو و این حرکت
یادآور داستان‌های عهد عتیق است!
شجاعت و جسارت فرزندان داوود!
که در عین جوانی و نحیف و خرد بودن،
مصمم و بی‌هراس،
مستقیم به چهره دشمنان خود می‌نگرند!
مثل داوود، نوجوانی ظریف و آواز خوان!
خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه زده بود، اما اسرائیلِ ۸۰ ساله، از این نهراسید!
یا از اینکه جمعیت ایران ۱۰ برابر اسرائیل است!
یا اینکه مساحت ایران ۷۵ برابر اسرائیل است!
در قطع سر حکومت جمهوری اسلامی تردید نکرد!</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6765" target="_blank">📅 15:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6764">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hvLh60rk-ccMPGRKmiesKD1vVIjt7mo3XS_oRe5DZRXc9N1jnnqgAku1pzvkf4xQB2XVRdXVfCyFSALPrAaeQWfw6Z_q-12od5yPiO2702CutPtCkK5ce_cE9jICtX46_rxMcpITJMWbt1_apVCtl7haj2CGETLOAR5R_fowfrSWe93Cy-bO0dGLxaGhTbaVVce7h3OQ8lx6Dstpyo2x5t3FNqS20CeDw3ev0uFLGiFGCuCeKwyXmnWbDkooArj2-8q8xZrxpJM49o30fbHDs3Le4NnSvzRVUJRObFWMfeWRtih9YXHvroSNhjS4we0n7td5bK63v9fCtxD-eypqLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.  . این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،  و نقش میانجی‌گری این کشور. (وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،…</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6764" target="_blank">📅 14:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6763">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B_o281YVZ71ZKsCFr8pPhgyh_Lajko4obcfiYCGQsIws-60X13xp7fgF0tETpGCoGbGH8DYYqoWBxTimFyx9QuOAn_lkl-44OCKTFFBmGBQS-MR_N_4khJcSzLNf6KFeProgY6GDDjYQwpctO81lTfa3E3ZpLfDSd9WKwHfS2JiyjoWf1QCdebfQCbiM4jA-xDHWvj4PVPX6ICfr1ShLEDlOnKghrYP4EcnMqs4qEGT_uZGL8VZWbO28v5NJyr70yIV2_-rF_qz13EmbE2UHoT8jhvVzAm-0isbw5LAJmxyighQ20stQg10G1NWiBBXlVT0JpmPMRU3eaOEoNndJRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود
که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.
.
این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،
و نقش میانجی‌گری این کشور.
(وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،
باز هم ترکیه این مسیر رو باز نگه داشت و گرچه  از انتقادها هم مصون نماند، اما کار خودش رو ادامه داد و سود بالایی هم برد)
🔴
با توجه به وضعیت افغانستان، پروازهای ایرانی به سمت شرق (چین و..) هم احتمالا ادامه داشته باشه
🔴
و از روی خزر پروازها به روسیه ادامه خواهد یافت.</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/farahmand_alipour/6763" target="_blank">📅 14:24 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6761">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=ukRlGn2b0pW3TNYNI4jo_xr6rY-meA3yCpNl28OTTFU-8i0vwNsoPSH4g_Ww5jlFEDq46nmoD2il1PiQbQsAkq5ITexwk_3swk3S6rz5QOgtEkgj7bvUnQPyXB2al-meq_Ai-A-ClBlSVY_V5yRXc8TeOAC8qJTvLAy8Dd0T5F59GHkbqYdoMe-rTUkVDYIDGDEeDBG6moxtW0uxa--56m30Mu44yexkUx335FtPC-5xI5cDIrphExOwKe5-h1HcC5wu1n-3Ax_z1_RacbvfU3c3PxxjfYPTKClYmpgDK4Q2yh7upqVEE357UUou3qu1c0M61IuXwakOwUT4ws39D4p0UhdRP3Yxtqweq3wJ9e-mxOsdylwN0p1biib6ehlLgtau_Pi_f8eDGeywY-IdxZ0OO-jNv62i4CPTrV39H4Rgg_dyPeav3oaiojDtk2PRFHZ4aY7y1JvpCb7HsE151eMm4sC1m_2A7FBEBif7BgzMdE-X3bp3aaN3-wtnD8oTr9lopMgaT67KHoRauirpox91nWwT0XifnZLqItuOOqxOD-m7ZV7s8RN7emNIK5r7uYXZYOA5C3GHqcXy8L_MgE8aLwC7DScVVhfMlInJBAgCL7bPjCBTcw19jPwYaTx9t-RjMWOzx3MX5L9W99lHWTPnYMW9jp1HAref1eLoBcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=ukRlGn2b0pW3TNYNI4jo_xr6rY-meA3yCpNl28OTTFU-8i0vwNsoPSH4g_Ww5jlFEDq46nmoD2il1PiQbQsAkq5ITexwk_3swk3S6rz5QOgtEkgj7bvUnQPyXB2al-meq_Ai-A-ClBlSVY_V5yRXc8TeOAC8qJTvLAy8Dd0T5F59GHkbqYdoMe-rTUkVDYIDGDEeDBG6moxtW0uxa--56m30Mu44yexkUx335FtPC-5xI5cDIrphExOwKe5-h1HcC5wu1n-3Ax_z1_RacbvfU3c3PxxjfYPTKClYmpgDK4Q2yh7upqVEE357UUou3qu1c0M61IuXwakOwUT4ws39D4p0UhdRP3Yxtqweq3wJ9e-mxOsdylwN0p1biib6ehlLgtau_Pi_f8eDGeywY-IdxZ0OO-jNv62i4CPTrV39H4Rgg_dyPeav3oaiojDtk2PRFHZ4aY7y1JvpCb7HsE151eMm4sC1m_2A7FBEBif7BgzMdE-X3bp3aaN3-wtnD8oTr9lopMgaT67KHoRauirpox91nWwT0XifnZLqItuOOqxOD-m7ZV7s8RN7emNIK5r7uYXZYOA5C3GHqcXy8L_MgE8aLwC7DScVVhfMlInJBAgCL7bPjCBTcw19jPwYaTx9t-RjMWOzx3MX5L9W99lHWTPnYMW9jp1HAref1eLoBcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترکمنستان، آذربایجان ، گرجستان و
امارات و تا حدودی عراق،  آسمان خود را
بر روی پروازهای ایران بسته‌اند.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6761" target="_blank">📅 14:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6760">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D0oKUGrtB2gn6CyQ5JCdLVC-tZwmb_ECT_1e5Kbfm_rzJaOCbFhzYj5VLoswSasNPxwYkUZIR2qEEGyefKoddgKYCK0twFDBzP7oevlmGFqhDiBwve9jofidrev4rheimLXzniVJ51Z0GbDVtx4Iei3J64Hpq1ogIoRePubalr75RclwEjl8SI7kd0COgTsP69Hnn9SgZvwC_eZ6R1Aypq5zu73TVXpm3YpUY8c44gL0TGRhDtffUm2MAjvRv24tNrHiGpJYi-Z9t3x2IKl9bFneCvbN5hSwDuE_O03x3M8Gxjw-fTCUD6XeeMdxRO9_pX_9bR_VEqrzi1mwXWV7Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6760" target="_blank">📅 00:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cCgwlifxXiiRaEj5cXe8EsCPt1pw7dQlUpOYT_v9fLYuSNZGESTt8p4mRSQP2XpgP0s7ELR6axOuUeHwiXteqY-OiZsCiHlbhcAVWJ16oq-K9iTMC_vgunDLVQR-vZEPeC_Ehxm3FGp5_kPQNyof0bBs3DteGyORZFfcGCc0qefDLaUu_NtqCE0wCQkvYuf-vrQT2Lb262OX1ID1RnCmVc6ioaqL28Df9NF6ERBQ-7avaUlyXbw4rNSRxOM0KwK5o_QTxTWVszkzfHWBvas76oXbaKGhD07WwqxLF74xQFzWnOmP9sN5tliKxw-OiBV0A10b-lGq0MwqwqEzkhNJmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مهدی حبیبی؛ دبیر کانون امام الرحمه:
پزشکیان باید تو نیویورک با دستای خالی به ترامپ حمله کنه و اون رو توی سازمان ملل خفه کنه تا انتقام خون رهبر شهید رو بگیره.</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/farahmand_alipour/6759" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6758">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=Vxmoh0UAxn_r5RVZP4N62yMam4nz1gxLve1PnKOu6AxYCVKnGt05RtGxBMTz5bg44t4t5D8P0Yn1329smgwOItapbzm64ciNlNN8aftstlVXl6GMNsZ4nkG14wt5_6kHhsAYm4jbOkLBQTWzDTAlhaZP8aMcYPK_r-4nMqp32-GqJjFVGTaUuFRles0grEzRx7uX9gBYXP-P3Vzzhn07cW3GQM3qFtG5M2XOmZSt2iSr8c1DdBa1_SNqPyz06M0-a4humvyc5pmfbkS2d90EAxf2MANg-SO5Pzlpy2QBeQIWZU92Mfi5GygeajDrGge_E5NJOmWQHWHxtnSoHYQF0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=Vxmoh0UAxn_r5RVZP4N62yMam4nz1gxLve1PnKOu6AxYCVKnGt05RtGxBMTz5bg44t4t5D8P0Yn1329smgwOItapbzm64ciNlNN8aftstlVXl6GMNsZ4nkG14wt5_6kHhsAYm4jbOkLBQTWzDTAlhaZP8aMcYPK_r-4nMqp32-GqJjFVGTaUuFRles0grEzRx7uX9gBYXP-P3Vzzhn07cW3GQM3qFtG5M2XOmZSt2iSr8c1DdBa1_SNqPyz06M0-a4humvyc5pmfbkS2d90EAxf2MANg-SO5Pzlpy2QBeQIWZU92Mfi5GygeajDrGge_E5NJOmWQHWHxtnSoHYQF0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در دوره «جاهلیت» سطح موفقیت خدیجه
چنان بود که کاروان‌ تجارت خدیجه، به تنهایی،
با کاروان تمامی بازرگانان مکه برابری می‌کرد!
اسلام - ظاهرا - ایشون رو به جایگاهی رسوند
که به گرسنگی افتاد و خوردن چرم کمربند.
حالا شما میگید جمهوری اسلامی
ایران با اینهمه نفت و سرمایه رو فقیر کرد.
این چیزها ظاهرا ریشه داره!</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/farahmand_alipour/6758" target="_blank">📅 16:27 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6757">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=OV2g70b11utclGVJxLy0bsiC-Bog0pru7BJanZfO4IBEZMAxmSDRYOrJfHdmGx2IKbIq_1FB-i3lqvOI66gidVKY_OXMwZIccIb2oMw9iLBPUrrAyaCv2A1bv1FwKZpR8GSSu2TolF07wE4HNFUHCxrNGo6NKdDE23MU12SzBxVHa1ifyDcpePxUtwznMXjyiITQUiZflIXEWwakz89GcqJLzlfmk4gYY51RkJ9j8stuYeg9ADgK9dSOy4DThCW6P0-3GrVdZ4vdSEYRJR-vMUdLnLs95Ag_63gz_5qBNQV5C7nzeg8BYPnZqo0ag9EBqhEOnTMKelu1_hvZPIg7iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=OV2g70b11utclGVJxLy0bsiC-Bog0pru7BJanZfO4IBEZMAxmSDRYOrJfHdmGx2IKbIq_1FB-i3lqvOI66gidVKY_OXMwZIccIb2oMw9iLBPUrrAyaCv2A1bv1FwKZpR8GSSu2TolF07wE4HNFUHCxrNGo6NKdDE23MU12SzBxVHa1ifyDcpePxUtwznMXjyiITQUiZflIXEWwakz89GcqJLzlfmk4gYY51RkJ9j8stuYeg9ADgK9dSOy4DThCW6P0-3GrVdZ4vdSEYRJR-vMUdLnLs95Ag_63gz_5qBNQV5C7nzeg8BYPnZqo0ag9EBqhEOnTMKelu1_hvZPIg7iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سر تکون دادن،  یعنی خیلی اوضاع خرابه نه؟
رئیسی هم کتاب حافظ رو برای اردوغان باز کرد و خوند :
«خوش باش که ظالم نبرد راه به منزل»
و امروز نه رئیسی هست و نه خامنه‌ای!</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/farahmand_alipour/6757" target="_blank">📅 13:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6756">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
دولت عراق تصمیم گرفته تمامی پروازهای هوایی با ایران را متوقف کند و این اقدام در چارچوب پایبندی عراق به تحریم‌های آمریکا علیه ایران انجام می‌شود.</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/farahmand_alipour/6756" target="_blank">📅 22:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6755">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ترامپ: اتفاق بسیار بزرگی در راه است
‏خبرنگار فاکس‌نیوز می‌گوید دونالد ترامپ در گفت‌وگو با او درباره ایران گفته در مرحله تصمیم‌گیری است و در آینده نه‌چندان دور «اتفاق بسیار بزرگی» رخ خواهد داد.
‏به گفته خبرنگار فاکس، ترامپ سه گزینه را مطرح کرده است: نابودی کامل ایران، رها کردن جمهوری اسلامی تا از نظر اقتصادی فروبپاشد، یا رسیدن به توافق.
‏ترامپ همچنین با لحنی تهدیدآمیز گفته پرسش این است که اگر تصمیم به چنین اقدامی بگیرد، چه زمانی کل کشور را نابود کند؛ و هشدار داده که «بهتر است آنها رفتارشان را اصلاح کنند.</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/farahmand_alipour/6755" target="_blank">📅 17:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6754">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">این حرف‌ها چه چیزهایی رو یادآور میشه؟  ۱- اکثر مردم لبنان دشمنی با اسرائیل ندارند!  مسیحیان و سنی‌ها که بیش از ۶۰٪  جمعیت کشور هستند، گروه تروریستی  حزب‌اله وابسته به جمهوری اسلامی را عامل تداوم جنگ‌ها می‌دونن!  حتی به زخمی‌هاشون و آواره‌هاشون خونه هم اجاره…</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/farahmand_alipour/6754" target="_blank">📅 16:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6753">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.  انتقام خون خامنه‌ای رو گرفتید؟  عزتتون مستدام!</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6753" target="_blank">📅 16:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6752">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=KXz7QAuIn9P2jHwL9vSk5d1OgxSWENl_tT63UWwrpSeNZqJmZEfZWUGuFBVQEBoBRNaT729I01nv0-F9sbAF1fJFkRfkc5VyBbE-sHHFL03ouPeUrTXSQPYutH6jcajavnIZC9sxFaY9lpE1XhHLJAC5tw_tGdzZy4DtX8husT2AdqtLy8CeJ0TJrlf-sfQ0ZTu3yxrQxEOK2yhq9WE2ewiMbKBxK2ASAipZmst2OVNoQ1ovGdP-mkqfrUbIluJvuX7_R5L59p_Pki43G0YUFyBF-f4I02pehQs7N4dr767OXEm7vwwulsb90KJ5X-7csbMVteiNJjMVVHzgMHaBTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=KXz7QAuIn9P2jHwL9vSk5d1OgxSWENl_tT63UWwrpSeNZqJmZEfZWUGuFBVQEBoBRNaT729I01nv0-F9sbAF1fJFkRfkc5VyBbE-sHHFL03ouPeUrTXSQPYutH6jcajavnIZC9sxFaY9lpE1XhHLJAC5tw_tGdzZy4DtX8husT2AdqtLy8CeJ0TJrlf-sfQ0ZTu3yxrQxEOK2yhq9WE2ewiMbKBxK2ASAipZmst2OVNoQ1ovGdP-mkqfrUbIluJvuX7_R5L59p_Pki43G0YUFyBF-f4I02pehQs7N4dr767OXEm7vwwulsb90KJ5X-7csbMVteiNJjMVVHzgMHaBTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو :
«نصرالله، دو سال پیش هنوز در پناهگاهش نشسته بود. الان کجاست؟ با من تکرار کنید: پررررر!
و سنوار کجاست؟
پررررر!
و ضیف کجاست؟
پرررر!
و هنیه کجاست؟
پررررر!
و با خامنه‌ای چه کردیم؟
پرررر!
«سران ترور را یکی پس از دیگری هدف قرار دادیم.»</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/farahmand_alipour/6752" target="_blank">📅 13:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6751">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fBXf-LRRpKKsH4hhOFfs95QJlMPV1BZkERjjD7ILLTKYfUGC9iD2UdM-eqzYINT34S0-lP9dm2uAQa3oDn9t9EYbmwzBBWcodaVNyFJffd5CmUUnCJ7kn1EEhGWd0ZRDNxL9TC2B1r1VqdVdH52KqC5nBBufpU7t-xzDZ07oJxflkJphtzWfMrQf41Oyracn50VhH7SYE3dhOuxmJCF08pJy_kD-dC5ah4d909Nl_8swhEea-hJR6Kc_x8SYCbsuK4ws2N50ywlWOaKTJ8vgYJEJ0GbSyFOqf3dNiR27g7nJ8zo_Y8PQD6fCmqZTpcixELb0sulukFfHSC-1OU14yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا میگن : اروپایی‌ها و غربی‌ها
حسادت کردند به اینکه ما تنگه رو داشته باشیم!
نمیگن ما رفتیم بستیم تا به دنیا فشار بیاریم دنیا هم اون تنگه رو دور زد و ارزش جغرافیایی و اهمیت استراتژیکش رو ازش گرفت!
تا گروگانگیری شما بی‌اهمیت بشه!</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6751" target="_blank">📅 13:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6750">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04900863be.mp4?token=EfWAXC3-4Yvhj3Lxg0J3N7lrRB-cK4iZ3MJNILpdLfYokVh2EZ0y2k_Z_uAnLFKa5I3TvlBhm6iIigLl-VwPojnUogzOTMuhWTCmXEQkQuGbrQrkAwxv4mggbz59kXYoa1nhg6N5k0f7WJmArpP8tDzyZaDh7Gbw4MYsvQqHmyKF40JeGADugs9W8z_nYCZHSC4mHV5OHwRBZ6y1FuLCj_5uvcv9fmdrlNy_IvztYktNgnkJK5sg4pxdGJ3EzRrgilnr7jfjBZMohAtfpyebx_NcjAXBnpDDaqEVyLiJfT1_ymO3w1id-d-WAxy5aD_lVcCTdPhHkRRnftDzRUBro24qYJbGzNpNlkzOSDzgppTzGAItNb7R4zAtA0IL0Th_BnK0eYmwfOkMl1ct6v3ILEfhn_kBf6qbG9WKjxZQOLIvZ5rUiDvBGK_RZto65gWNVpMWmeRHHd6VQj5Q2bcqSp9bJ59WKG_YcGsQi43zQGImWfEAqXBdCV81bLszmh9InmvLPOh-Xx_eiyGaYqkEbvpuPLFnUNTfH-6VvWTqbGVj36vfgPhd33GZvwchkbdtobMpGQ6QU27PF3SwRnAE0-dTFkas8wVf3OTAcRSGIvkATPPolO6hvDrtraZtZvVx-e9oUUXwV4ptaXOMiCMNa6kCfmLi2CGQFyC1xlMTe28" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04900863be.mp4?token=EfWAXC3-4Yvhj3Lxg0J3N7lrRB-cK4iZ3MJNILpdLfYokVh2EZ0y2k_Z_uAnLFKa5I3TvlBhm6iIigLl-VwPojnUogzOTMuhWTCmXEQkQuGbrQrkAwxv4mggbz59kXYoa1nhg6N5k0f7WJmArpP8tDzyZaDh7Gbw4MYsvQqHmyKF40JeGADugs9W8z_nYCZHSC4mHV5OHwRBZ6y1FuLCj_5uvcv9fmdrlNy_IvztYktNgnkJK5sg4pxdGJ3EzRrgilnr7jfjBZMohAtfpyebx_NcjAXBnpDDaqEVyLiJfT1_ymO3w1id-d-WAxy5aD_lVcCTdPhHkRRnftDzRUBro24qYJbGzNpNlkzOSDzgppTzGAItNb7R4zAtA0IL0Th_BnK0eYmwfOkMl1ct6v3ILEfhn_kBf6qbG9WKjxZQOLIvZ5rUiDvBGK_RZto65gWNVpMWmeRHHd6VQj5Q2bcqSp9bJ59WKG_YcGsQi43zQGImWfEAqXBdCV81bLszmh9InmvLPOh-Xx_eiyGaYqkEbvpuPLFnUNTfH-6VvWTqbGVj36vfgPhd33GZvwchkbdtobMpGQ6QU27PF3SwRnAE0-dTFkas8wVf3OTAcRSGIvkATPPolO6hvDrtraZtZvVx-e9oUUXwV4ptaXOMiCMNa6kCfmLi2CGQFyC1xlMTe28" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن
مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.
انتقام خون خامنه‌ای رو گرفتید؟
عزتتون مستدام!</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6750" target="_blank">📅 10:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6749">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">وزیر نفت اختیار فروش نفت نداره
صد میلیون بشکه نفت گم شده!!</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6749" target="_blank">📅 09:55 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6748">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67af3237af.mp4?token=putQrulGES9w_keqQd0k9vvstrqz_LmJ9dGqTeFU4MLKOgLr-g1vOa1v_Engp6XIHHmOjuZ2hhy0aNL4LFeptzTAjh8Y-OoowD2YObB5oUzvjMrSsaoyX1MPIgHAu6aIRKIhGFCp40qrmCSKHhILbR7fNmlQbHo4uoywnXoDd9SsOoONDpLGHHlNEYfIQNyALpwfcGvracFlP_CbcbIPG2MNcujiiBOKsBuSrR97Qb_WOKCqy4akHpLvZH_mRlVJXQg8JGPnL1eJNxjxBB2vm44IDLoTWy7RJLwl5AaJoMk0UVfPLYfVcckymLThXrVqxeJ7qx53ndraOGrTR2X3KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67af3237af.mp4?token=putQrulGES9w_keqQd0k9vvstrqz_LmJ9dGqTeFU4MLKOgLr-g1vOa1v_Engp6XIHHmOjuZ2hhy0aNL4LFeptzTAjh8Y-OoowD2YObB5oUzvjMrSsaoyX1MPIgHAu6aIRKIhGFCp40qrmCSKHhILbR7fNmlQbHo4uoywnXoDd9SsOoONDpLGHHlNEYfIQNyALpwfcGvracFlP_CbcbIPG2MNcujiiBOKsBuSrR97Qb_WOKCqy4akHpLvZH_mRlVJXQg8JGPnL1eJNxjxBB2vm44IDLoTWy7RJLwl5AaJoMk0UVfPLYfVcckymLThXrVqxeJ7qx53ndraOGrTR2X3KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم تعرض به کودک در کلانتری
نیروی انتظامی جمهوری اسلامی آینه تمام قد نظامشه، وحشی و عقب افتاده و‌ خشن.</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NtkqTTOj06728_wJ2ms0eChzbWCs4DoIA_ju2Rs5oYq16j3PAqxSxkA9bJ9TI707rwQyjdFxPfR1ozPRB_ccseOECSHYPWLAjOpmb_ysA5Z9vCjzCbpmIZLtxTJ1sr9wGiHV2n6IcTfJxxHD4uGe4gWbvmen7wV2JgT2_C18Qa6paxkdHjJqRw9XVK26yHKbXFdOB9VlglbVqPKJ85xsnxjpknov2B1qC2MnXPFizQKpryNv-o4QTEZiomTUxijakP5qDJVJGcQu-ohyqk1WmuCaD-mwx9KwMcXsLZ183cy0TK3L-2o-z4XcCdw0NzQX3gCK8yNzlcMgxB6agaEXCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=CzP40huYFQW0n5jFskJSVT6re_kjgh3QrjTBSRyPLjjIOJdq1Ht0h0nAtD-vltwQPtEEp7_MbWcIA543oSjpP22YcqP0__yliucAWG25SsTggJhaVrYOK_0cMIBVJ5QG2EFwLrU-pYM_ep5rTGK7xD44U3VZHbgejZWUTEvNaK1qx7upDnwa3QNRbaB7NF_Jpm7AgqW5QVMrjgXNm4p6v_qyJm5ciDjHNH4NkKF3fMu1pFtXKo7toY6-7wbBwQIYTCfLUcLFjaKFXKKYVgQQo0IlAFMU9ijwP-Mh12tRCNFOuLNkeZDwfS-6As7yg-9QuZ6PWV2lH_R3GQOinM8cj6PcgD5NVqfRU130K1kKJ0CPjqcz3zFSAcnSY6R7RUahQ9Q5sBjtrcV7DvIUZI6XD_fEaRc3b2F0EQuXYZlnzcWUZTKkvjPhYNW776JypSK6iDWR3SHh3mglibSr1UVS9CPTMgSS3icNqn8ob5Ga6VBPXl0_FBC8JoD6Ub8fDJF2rRoM5IJlFxAaL1PcVvK0abiOlmbv-Xu1KLYjb7xEa_mdXUTiAcDkAo6pJ-HTJeTj1t6mw2I6S5qg7_dPGJXq0VO7hc_-qllY6pQZ1z094im64jWQuke_c9oU2ZU57Cc-8SnkcE5YgiVjshIAsoDKkCPIITrIun4u6RyI-We4FPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=CzP40huYFQW0n5jFskJSVT6re_kjgh3QrjTBSRyPLjjIOJdq1Ht0h0nAtD-vltwQPtEEp7_MbWcIA543oSjpP22YcqP0__yliucAWG25SsTggJhaVrYOK_0cMIBVJ5QG2EFwLrU-pYM_ep5rTGK7xD44U3VZHbgejZWUTEvNaK1qx7upDnwa3QNRbaB7NF_Jpm7AgqW5QVMrjgXNm4p6v_qyJm5ciDjHNH4NkKF3fMu1pFtXKo7toY6-7wbBwQIYTCfLUcLFjaKFXKKYVgQQo0IlAFMU9ijwP-Mh12tRCNFOuLNkeZDwfS-6As7yg-9QuZ6PWV2lH_R3GQOinM8cj6PcgD5NVqfRU130K1kKJ0CPjqcz3zFSAcnSY6R7RUahQ9Q5sBjtrcV7DvIUZI6XD_fEaRc3b2F0EQuXYZlnzcWUZTKkvjPhYNW776JypSK6iDWR3SHh3mglibSr1UVS9CPTMgSS3icNqn8ob5Ga6VBPXl0_FBC8JoD6Ub8fDJF2rRoM5IJlFxAaL1PcVvK0abiOlmbv-Xu1KLYjb7xEa_mdXUTiAcDkAo6pJ-HTJeTj1t6mw2I6S5qg7_dPGJXq0VO7hc_-qllY6pQZ1z094im64jWQuke_c9oU2ZU57Cc-8SnkcE5YgiVjshIAsoDKkCPIITrIun4u6RyI-We4FPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pOdYVxWCDmLI9kn34Yj6y6IzpqqUr2Pl_ZaV3Ax3OxhP_qDHu64WHRY44gDXrlboDWx-1IhtTaQVblADzGeRS6cgzMhQl00OQ_3dBkFgmt_WdoE5CMGvFOp8BhE4sZVk1ODZ3NC2eNKHJN1zMA6LVSkoIlmw-2yyxF6h7vCEh6_spYimRiXjk2JG1lQzHiEsraDjG7rcFIxpukD6C4rTPPa0iK_MFVpMKHMSjenEYGrpJu-VSwjwT8_DYByNWHOKmrmw0OnZrGgBHiZmnQCQbB3bEbZWwFsXG1F3lqR0_x9oJGoFXXpo1M3SbhcMYKTpIQH_DYg7Kuoo8ruwDNNA8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان جمهوری اسلامی این روزها
برای عروسی در یمن شیرینی میدن،
۳ سال پیش برای عروسی
در غزه شیرینی میدادن،
پارسال برای جنوب لبنان!
عروسی‌هاتون و پیروزی‌هاتون پی در پی
✌🏼
۲ میلیون اهالی غزه سه ساله زیر چادر هستن
۶۰۰ هزار شیعه لبنانی ۵ ماهه
توی توالت‌ها و گاراژهای محله‌های مسیحی و سنی پناه گرفتن!  پیروزی‌هاتون پر تکرار!</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/farahmand_alipour/6745" target="_blank">📅 13:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6744">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=IPkpC3c9O7x7sU2x_fev2HM7-w7H9b4-22ipj_Mk8vNrAmM8my6JeI7kjASz956XHBlbDmmp0g9I084w1UpAlp_NqNBcAm5URw3ayfsG73OFfxloJ9sglUyxTQIsp9HAfa2rJu-hYg7bJbCwYMz7QxywnzMjW8jL32JkxxsUj218sy_JC6GxeCNHjtO47TcGKv25H_IqeZpkdaARqSEZ4ETGEMMc0w36LZ2tGeVb1L3coifJaaYp0JVTcELVwl53KQShkMv7LZ2-pvmHN1ZBwLMiYOUzI_8fUuP7LwDv3LIegQXz2MpWykIuScUWDYRu2Zek0a5LdlOan9bva17Efw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=IPkpC3c9O7x7sU2x_fev2HM7-w7H9b4-22ipj_Mk8vNrAmM8my6JeI7kjASz956XHBlbDmmp0g9I084w1UpAlp_NqNBcAm5URw3ayfsG73OFfxloJ9sglUyxTQIsp9HAfa2rJu-hYg7bJbCwYMz7QxywnzMjW8jL32JkxxsUj218sy_JC6GxeCNHjtO47TcGKv25H_IqeZpkdaARqSEZ4ETGEMMc0w36LZ2tGeVb1L3coifJaaYp0JVTcELVwl53KQShkMv7LZ2-pvmHN1ZBwLMiYOUzI_8fUuP7LwDv3LIegQXz2MpWykIuScUWDYRu2Zek0a5LdlOan9bva17Efw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bOEaMOYIJrM5BdqSBKAZTqQRBVt0U7ybtJYxRbm8YFPvbfDfWX-5wUc9Tfmo6xL4yqHWAx_0jOpcc-7Ry_Y6pkMPpIqPXU_vBV_3kGT-3tVGflvjPIxEKfQxZfrowDzcUz_QWVu6O4fUbEWai13DjMR8m4JMzTAsxMtXBOQwIuPz6WReyxp7JA9zcHazjgXi_8ZCLFQuLRkwDCBxQ7LLCNdrijcCouLLMliZxvI7S4F4ejFeOzXhrS7OFpjmalnQOSebwv9QFUwBwGRSn7PyYP2S2bXnKdBE7tMtfQmn03Q7UDvBxyS5ZqRIPhebmpWIncqKmwi3okV8YEPahjKX3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ohIKyBCQM4SdsYPdO6dxdJGotwO4_3_MRHGCh-s9OAATC9BLaXFDhV6VeSFFD6-jhnIzkFZ4iOpBbjrjlSPQRSUHhIAI254MeFD_keRY-TYUzOoli5Ioxl0IidlxI3rbC12XnLahsNmBRj5h6z955FfqSM_14V_HGNTgbXpUMgVk5TRHk8XXQlH0Ljrg6cB9_CMx6v2xZfTV4_CxA22LzAhpEGI28uUandcgRcG_XA7psXp5O-VHiaGJAKSP1Ar5X1Kq3Rzx1gY9qe7tJRUE1PwNEEcvJ0DsGVJNPDc33BYejbCsxxAm62WOd60tz6pDOdNnOl1-7nVJ8ChZU9-y6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EZq6i82R8vQmRk3us9YwoVZvRM90MjLxfeS0W7CIWml6SkIT2mxtv23oUJ3rPMHpvUrwNbpeaZBiBL8SwXq1E1mgvo4Rqb23JAcW-3B-GUOTMC_GH_3P8XKQ1k27DHBQDPZcI0pK_YK2brFYcTK2ULCI6GTvIfzgFlTsy5EB8blpuhX4oxI2ucBpT_rYVLPR-GSwU9NX6N3snAVO-_Vhcf0Z9mIQ3gxL0gzBveAd42vfR4k-A5g0ns5Wm-iQ-h2mwSZcyl4UqRXlmBByLfsGvgnXuUPXNETpc_a3GbJqbltSkNyw7-kURZOp54fzMpEDlPDaK95r9jUJsUQCnw4gHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=Mit8p84KIXoUM5S-wQMJPd9ZRpx9hdqQVg38DOd8Y44KykaNSCbGQ6-EzEayICGK339w5UPLmHSB08ezzfN_9Pz4kidbbZ_ufWlKttsXfO6f4ehOzFwRXmnx1oSmzqwkkm2CCJ_lAO3Unblf0cNZ49oaQOBsqE13tejfICNxU3xygKQzLIjkCH71RL9hl3R8tUcR-NbC-gqgJaAF1sw81DKDCGoAfEjtLWnlq416-oRtUwHJsFoaludtlDYW1yxntQXPSr8gKcb9ydL9xm-94j0aqTAGbMQMBVlkuV_zCgDIkD_JGRSZEoCve5UEAQRryF1VYTXdPqT8tQf0p2v6wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=Mit8p84KIXoUM5S-wQMJPd9ZRpx9hdqQVg38DOd8Y44KykaNSCbGQ6-EzEayICGK339w5UPLmHSB08ezzfN_9Pz4kidbbZ_ufWlKttsXfO6f4ehOzFwRXmnx1oSmzqwkkm2CCJ_lAO3Unblf0cNZ49oaQOBsqE13tejfICNxU3xygKQzLIjkCH71RL9hl3R8tUcR-NbC-gqgJaAF1sw81DKDCGoAfEjtLWnlq416-oRtUwHJsFoaludtlDYW1yxntQXPSr8gKcb9ydL9xm-94j0aqTAGbMQMBVlkuV_zCgDIkD_JGRSZEoCve5UEAQRryF1VYTXdPqT8tQf0p2v6wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه
مهم اینه دلت با خدا باشه!
علی علی!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q0T2O6zbXQ171GC-PZ3SC6vQtqXCgph0T02XUCsdNfd2BDwbOsMAcsmEq56bWrDAsLGcvLHOY9T7ne0_8q46-4OO5jDHCjoVYw6whCye-v80QRrw77aOcVhtCiNvv9tZX5MDJKgHC867xkMk06HUpnLEiZfKeR3KrtsdKVmYrf2MmnjAoGXEm6NOmCcZX776qWkZecT-y9nxE9YIt7a_LAW02sVyG8PLwHFx41Vo3Iacj1fivaAFWlvkfvlkSuU21QT1bKvICLJJ9lhahqXjyZYsj43K8Dh3svpnDGV5PScIlpMc6fL47bICr6ct4KZJQnithirMckzGvyOLTYwqeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu6Iy8xcLLJGtB0Tl0gWnunh80oohxzp0XVEE38no-urulj29tzj7bNWLGyvkEgGxlD3aah_RY5u0xifqVH0g8_UgnvioLvm7wejINDOhhb1Ozqvyut_3wse_x7k-RiHnNjjtq5PoTBx6280vHXS9qjEVY1jfOGIL05HMwqLyPs2xvl1cC1nAVHthiZWQbcw33barDphYn9Sj_Is-WkleXe0dBOXnN6-Yc4Wg0spg_LkpG7wDca8RPWiEUmMT4E_tzsCDg18yjTyNXWRtE62tZdGuXRrZKC_hmtf_UdHlOKlC9BJeoL5STTjCRyya1Zyi3TOMkeiTnaDHz46k6eMjn-0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu6Iy8xcLLJGtB0Tl0gWnunh80oohxzp0XVEE38no-urulj29tzj7bNWLGyvkEgGxlD3aah_RY5u0xifqVH0g8_UgnvioLvm7wejINDOhhb1Ozqvyut_3wse_x7k-RiHnNjjtq5PoTBx6280vHXS9qjEVY1jfOGIL05HMwqLyPs2xvl1cC1nAVHthiZWQbcw33barDphYn9Sj_Is-WkleXe0dBOXnN6-Yc4Wg0spg_LkpG7wDca8RPWiEUmMT4E_tzsCDg18yjTyNXWRtE62tZdGuXRrZKC_hmtf_UdHlOKlC9BJeoL5STTjCRyya1Zyi3TOMkeiTnaDHz46k6eMjn-0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=EP_78Xi5KiKkobXgRuNe5v9JdSnTmRcNUrY4Dq2-bCmxVTTvM-p-wB5c7WOEqM0OjtLuICqIeYdrSyYNMyND7JY5AuaAguru9EE56qhZbWPqlB4jXIMuiQpr7SkoAOzhGzYY8jFgu-O99Gh2mhdy0AeZ1gbtZ-QzTXQbQepEsMDMlWSo63HPDFfNKEPO6cY3K4yqu_FtBqnsFPxULxJcdwrw-Mn0IGfglge0CzFnBXKjolFM2thh7GC8NbiUhF3sZOWPSfBWrgjCzK5-mxv7pE0g2kVglnav-tvkeM4YetbkLPa09IyHi3rzSFNYn43myWhMKG7AoeZO281MivxGzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=EP_78Xi5KiKkobXgRuNe5v9JdSnTmRcNUrY4Dq2-bCmxVTTvM-p-wB5c7WOEqM0OjtLuICqIeYdrSyYNMyND7JY5AuaAguru9EE56qhZbWPqlB4jXIMuiQpr7SkoAOzhGzYY8jFgu-O99Gh2mhdy0AeZ1gbtZ-QzTXQbQepEsMDMlWSo63HPDFfNKEPO6cY3K4yqu_FtBqnsFPxULxJcdwrw-Mn0IGfglge0CzFnBXKjolFM2thh7GC8NbiUhF3sZOWPSfBWrgjCzK5-mxv7pE0g2kVglnav-tvkeM4YetbkLPa09IyHi3rzSFNYn43myWhMKG7AoeZO281MivxGzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=Ix1_HfYVZgx-CRjgTsvkcGruFFROwtAwMjH29-5HmtHjSTwoYo4NTiqzvL_F2AyubzWK87MtX9QSFwP2SKR1QCoh_O6ABAWTAdOe9xTRYdLXl25r89kt5WzsL9hBOIHiFsgL0mrJdEY-lHUtImr2B5abP0mBDqm6yhUtpPoY2MSrriFBMhaV9keYcn9V7Ry5RU3pjhg6huo22DEWYUmjkn854-4nVzIVeZkeSCNwXt-r26GntEd3Sz1U6iCF4q5T3tTPSS3hKOcnZhBa6nUNEbwuL6IjctBX2roI8MORdGZwfsTusPfbC82vZGRDkpUWrvAThkSoQJcEWED6foZhc136U9qNHunQOovcO_PNRsPlbh_aQ9LsKY7HEKgxh6PPoETeGF89TKaobmdm92K5AeB6BjCJtIDgCxP0qFEh47sDcqH2fU_FZyvGNkPU8iiXd5RJZhWHUKXI-mpEfffFG0ViBA8HXPjckxfRZ7rojrtavEQ9ZytxldXcSwauVGVQOGdzRAjdMOX4QSlS_uiF31WRJKNoDQ8m-yWa9iZHtZmSuBe3JZ2_e6fqdjbCSvp65U8PsEInuFl0dE5WPAQ16AHOcjKUrdZESc_6cF971JFIVYkLqQM_MzfwkmqWY2jy4Ja2S5MG0dgWk9GKOv0OlVD42y_7Nz4kAZ-3djA4A38" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=Ix1_HfYVZgx-CRjgTsvkcGruFFROwtAwMjH29-5HmtHjSTwoYo4NTiqzvL_F2AyubzWK87MtX9QSFwP2SKR1QCoh_O6ABAWTAdOe9xTRYdLXl25r89kt5WzsL9hBOIHiFsgL0mrJdEY-lHUtImr2B5abP0mBDqm6yhUtpPoY2MSrriFBMhaV9keYcn9V7Ry5RU3pjhg6huo22DEWYUmjkn854-4nVzIVeZkeSCNwXt-r26GntEd3Sz1U6iCF4q5T3tTPSS3hKOcnZhBa6nUNEbwuL6IjctBX2roI8MORdGZwfsTusPfbC82vZGRDkpUWrvAThkSoQJcEWED6foZhc136U9qNHunQOovcO_PNRsPlbh_aQ9LsKY7HEKgxh6PPoETeGF89TKaobmdm92K5AeB6BjCJtIDgCxP0qFEh47sDcqH2fU_FZyvGNkPU8iiXd5RJZhWHUKXI-mpEfffFG0ViBA8HXPjckxfRZ7rojrtavEQ9ZytxldXcSwauVGVQOGdzRAjdMOX4QSlS_uiF31WRJKNoDQ8m-yWa9iZHtZmSuBe3JZ2_e6fqdjbCSvp65U8PsEInuFl0dE5WPAQ16AHOcjKUrdZESc_6cF971JFIVYkLqQM_MzfwkmqWY2jy4Ja2S5MG0dgWk9GKOv0OlVD42y_7Nz4kAZ-3djA4A38" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=KuGIQc2d6KU4KMBQ8VWke296hSfUOQ6RqqULDrVX1w4rzcVlocEtpM7O-oEA9vsSsSPJpPIFbtdpiAX6Bufr49w6pHIzrxLAjHAzbtYO0Iznnzy5CrzqKnVDZAB9ZWWAF-PnJhh5wgLUOoDMPd1AzCfn8FJYyPsy12TXUK0lSw4FAwS7uUiH9coEnYBxlYOpESW7PhZ_uMIvqmW8NR8ZIzroC0hgiyK7Q2gbw327E8oKqW4a78R7WD-CmcwMsGblaWt5h8pKQ_fMb0oAe6xHXkrscQZhoCER-fKPZzyWtkMYW8Wao3Drf_LidQZxSfzsmod4ipGYw0AcB--Xs6Dlww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=KuGIQc2d6KU4KMBQ8VWke296hSfUOQ6RqqULDrVX1w4rzcVlocEtpM7O-oEA9vsSsSPJpPIFbtdpiAX6Bufr49w6pHIzrxLAjHAzbtYO0Iznnzy5CrzqKnVDZAB9ZWWAF-PnJhh5wgLUOoDMPd1AzCfn8FJYyPsy12TXUK0lSw4FAwS7uUiH9coEnYBxlYOpESW7PhZ_uMIvqmW8NR8ZIzroC0hgiyK7Q2gbw327E8oKqW4a78R7WD-CmcwMsGblaWt5h8pKQ_fMb0oAe6xHXkrscQZhoCER-fKPZzyWtkMYW8Wao3Drf_LidQZxSfzsmod4ipGYw0AcB--Xs6Dlww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UceyswEDkPGlxfZ-oQDQugA5SI1C8UJRWmsO4gOpfLsG2sZsTW-8HT2FikkoRllAWwYOM1j7MHAmdjdyle_xgjgnhnMItY2JT7foxxoevOqRwivmDDk9uO2AhJol3f3MOWHTgYdbslyTL5HmTHRn3gBdxNAy4u0bdjS4AJPCtV0qL6PiyNHg_BViEfumnjCR_1j7Y_aYNIuE_NGSDxGPdhpBNw-Btuqj9X_g6TktJjiGB_q65xoLwPHwY4qQBkEIZIxE2RFPr7S533x1P_xb261eebrCEdnNzCKXDIwUR5cKuw-yswpHwOk2zoWI_1JUNK8-HoXEJVCoxmm6cz_V3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=JBgv44tPcBY2h880EHm1lRt8LLHZAD0ot3CDcTqBHPDtzpesg6bzACVLPFnhl0ijTgDN33ShML7rn9ACdue-mLRy3zRY2W3pe3ZTf142XBIO5-GsdxtTcOVhJQ42boaPoQgQhyHWNZFAbxOfnthi1_bhmLDyXE36ZUOGj1N6zmF6x7Vf6NGCux_zEIyNxfPNxbpiJdA0X-fFvyBp7cfL9K3FBmiw65HtD8VYCQmpg5Xl8GmqDjmoVEgWqHQjbQvEG-43jPMrZQpOpmtRBUkWpmaoAnVOgtrxMySgTlJHo-ETc8i78GXi1qJsYna3Q7VtvDvSMjqFMlvsi7xNb1ifPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=JBgv44tPcBY2h880EHm1lRt8LLHZAD0ot3CDcTqBHPDtzpesg6bzACVLPFnhl0ijTgDN33ShML7rn9ACdue-mLRy3zRY2W3pe3ZTf142XBIO5-GsdxtTcOVhJQ42boaPoQgQhyHWNZFAbxOfnthi1_bhmLDyXE36ZUOGj1N6zmF6x7Vf6NGCux_zEIyNxfPNxbpiJdA0X-fFvyBp7cfL9K3FBmiw65HtD8VYCQmpg5Xl8GmqDjmoVEgWqHQjbQvEG-43jPMrZQpOpmtRBUkWpmaoAnVOgtrxMySgTlJHo-ETc8i78GXi1qJsYna3Q7VtvDvSMjqFMlvsi7xNb1ifPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زهران ممدانی
به مناسبت ۱۱ سپتامبر که هزاران آمریکایی به دست مسلمانان افراطی کشته شدند،
با صدایی بغض کرده
از عمه‌اش یاد کرد که بعد از ۱۱ سپتامبر
از مترو استفاده نکرد، به خاطر اینکه حجاب داشت و در مترو احساس امنیت نمی‌کرد!</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/farahmand_alipour/6731" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6730">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=MlR993sEPiHm8WFHEF0HUkZ_hS6bAQazvj1a0Yc1PzEpupybKfTgE8u45Wf5US6rxwZxjtVS83IATUXDieCSdrL3dPEmZR9E4Ec-OMYTDEw5lpTdcaYpyjDOk3OZ-69sx6edDGTiboSpi4W1a1GFqbnSTv9E6oFtpPEqaiDM5d7kbCYvTfMmCE_6YLWLJZ8yvxzzxxcZ6TpOfTjxKITf4pHk84j0MgLzwvHR2twhgg-tYWllIk6ZbFNqzEpzQyikJOqxZvSaLgUr47B-3S8SURj6qWJ53Jv2xi_TPbou1WMYc8OmzbwmkUvgWBed6Ltb_MmiMB3qJVMm2QiPKGHVMkyWdsjkUKf_m-zWm--uisMJIY2xpTIkacqCLiVHIED7uQJFTzM3Lxe84r4zcLZwRLjrxJM3r801CR2W9y8BCSQlxOjk1LSvSsE58jiswhX3iC2_7Twl-mOR2iDrDB-taTOCg3HpqSnV3WZ2X_7UMwUdPVPJnBBzOrbPgVG9Q7Soufdg5c5WulJBlc4bcvVk-8pe02bfXF7Py0CTcB0Iuelv1WQOIkMAxjpnUyPhvd-XmqhavgMiMh1BrOUNqcs3V1YTN5TA97FlJqAFIYPXOUnlxTA4GC3gRQ8_tbAN_17cLimAYe71wpLEOheyOzT3QVNkag8o87mzKchPFBImkyk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=MlR993sEPiHm8WFHEF0HUkZ_hS6bAQazvj1a0Yc1PzEpupybKfTgE8u45Wf5US6rxwZxjtVS83IATUXDieCSdrL3dPEmZR9E4Ec-OMYTDEw5lpTdcaYpyjDOk3OZ-69sx6edDGTiboSpi4W1a1GFqbnSTv9E6oFtpPEqaiDM5d7kbCYvTfMmCE_6YLWLJZ8yvxzzxxcZ6TpOfTjxKITf4pHk84j0MgLzwvHR2twhgg-tYWllIk6ZbFNqzEpzQyikJOqxZvSaLgUr47B-3S8SURj6qWJ53Jv2xi_TPbou1WMYc8OmzbwmkUvgWBed6Ltb_MmiMB3qJVMm2QiPKGHVMkyWdsjkUKf_m-zWm--uisMJIY2xpTIkacqCLiVHIED7uQJFTzM3Lxe84r4zcLZwRLjrxJM3r801CR2W9y8BCSQlxOjk1LSvSsE58jiswhX3iC2_7Twl-mOR2iDrDB-taTOCg3HpqSnV3WZ2X_7UMwUdPVPJnBBzOrbPgVG9Q7Soufdg5c5WulJBlc4bcvVk-8pe02bfXF7Py0CTcB0Iuelv1WQOIkMAxjpnUyPhvd-XmqhavgMiMh1BrOUNqcs3V1YTN5TA97FlJqAFIYPXOUnlxTA4GC3gRQ8_tbAN_17cLimAYe71wpLEOheyOzT3QVNkag8o87mzKchPFBImkyk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RuC7j2eaJQ3HcGtBb8qogwmn7TfEqHL3FWCcw40FRjvGNva_1BclbknPORpMNULPqp4lOtgu3SV5i7nygpoHgRdsHoknv11RfLzthGO05xTQzZmSjssMSYMKOXxm0BzrYQX___bfQt53ND4r3eXZoLlUBrOZ9NW1fCA_uVUhRaHNetkedQXNvZZOPvxQfBt2Cjqc3HNxzgBXta1u1vIH0U5FdKsPn-8baINxg-z2BzoWN1p1x_CvYuxTQrMPG2779et7IxtWAfVSXVT0T0jG0_xFh3EHSMJ8SFr8OFqQjLN69_BoupuahOHGMLzB-KBZM86BMWnsGc-sBE3Sl9lG-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=maThull8LEw9LYcqSCVpZv-Qt--V_qYehVrH1FVMxB5DEbs6uwBNtIzRSeYOfdpzMVvEpjhaPF8bSTNk76-7_ZvvSFdEovXUseGQKUFELC9a6nQszU8_7FjPwfGa_EcEf9GiC1NFn7EbFrGQ9rW-tAwcq3sv-JWLVIHAb7Zh6fkuDNyhcXa2fpkwrOXaV2kTjfyI-WxWNueoh8SGhnJUBIfMRh5E_W7Us7GnZR1Sm89IXaQtN9bUXnLGjjFPMxAoVpvA411bQAcGQOcFvM1qdReeLgh1tYpwktQbHUbMt9YjwUocoTpAefEmb0iLMwW17L_cGjsoE3fJyrWTLECvfm3RmzG38CgTaEou6yms_RUqdwS6rI84tS6mIrpRKWfVYHpiEP8AuFX88r4AQpIlIcmchvKd8WrXLJcBCpjCEshFLpPBR_Qe0i7g60hiJ2vYxudQKn0OG9YP7ZyXoe9I1BM3Q2Iv6Icj9GWGUIk7jigjd39lOmCYs7cuz95Na2gBdP1asB-koLrubj9iCmC0_X2Jvy8yLwJMCXmwHgzn0A2hPHdloYx1a7wSCggYsto9wBpmjyPjKQ6rzCiQGsOJSoX-gIWDuT4oPejP-atc3qGMlYQHLq4Vco8yAB95KNyP2AzKynNUSGi6MRA09vnaoMXq0QHka0lLUPJA33WKpRU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=maThull8LEw9LYcqSCVpZv-Qt--V_qYehVrH1FVMxB5DEbs6uwBNtIzRSeYOfdpzMVvEpjhaPF8bSTNk76-7_ZvvSFdEovXUseGQKUFELC9a6nQszU8_7FjPwfGa_EcEf9GiC1NFn7EbFrGQ9rW-tAwcq3sv-JWLVIHAb7Zh6fkuDNyhcXa2fpkwrOXaV2kTjfyI-WxWNueoh8SGhnJUBIfMRh5E_W7Us7GnZR1Sm89IXaQtN9bUXnLGjjFPMxAoVpvA411bQAcGQOcFvM1qdReeLgh1tYpwktQbHUbMt9YjwUocoTpAefEmb0iLMwW17L_cGjsoE3fJyrWTLECvfm3RmzG38CgTaEou6yms_RUqdwS6rI84tS6mIrpRKWfVYHpiEP8AuFX88r4AQpIlIcmchvKd8WrXLJcBCpjCEshFLpPBR_Qe0i7g60hiJ2vYxudQKn0OG9YP7ZyXoe9I1BM3Q2Iv6Icj9GWGUIk7jigjd39lOmCYs7cuz95Na2gBdP1asB-koLrubj9iCmC0_X2Jvy8yLwJMCXmwHgzn0A2hPHdloYx1a7wSCggYsto9wBpmjyPjKQ6rzCiQGsOJSoX-gIWDuT4oPejP-atc3qGMlYQHLq4Vco8yAB95KNyP2AzKynNUSGi6MRA09vnaoMXq0QHka0lLUPJA33WKpRU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :
«مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»
و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6728" target="_blank">📅 11:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6727">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=pNLrw8XCt2GmdeC00s5pZY_FxrT_uZ1Qa_yLZeCxWYVttxck--biL9KkONxmFMZU5IQfRXe1c21NHbqrdB0n4y2E0YvN8Ue3tM6uStUGISalw7Rsx6ASNTgI7zmlwASIRRgkX8Eo_LeNp9LIbxnZwYVJZX0xsqADv4L1QfKop2txOtAdeYli07QlJkGnpm7IbbsQIl1pNSRLIhWaklJKxk6Rty7OjiYA9jcffIPrwq2V0yoVBnbaH9gEdAdWINlipHyFE3xqdb-GNLRNeGmjXzQhX5OI9zOwFaZa-bgWU6JPCxUf6rp7IuB_lCzO_i5IxlCZCAaJGCRIbtfE0kjdjhCMs_xrtoeAyV0rTVsENW1_XUr5tmP2NysbrLKC2YiYA0ipZABNi_iyBtWjQoX_5IDAmCbLrJ09h4V9ZpJmASYDqQuDhUcvdFT7jQ6OguY2X0_adi00iSII4R_5ZgtmnW0ZB_lL9yl1lo-oHpJ7T0D2xh0azA3sLYuhJ3-rop0ZRksiw6UPK_oK1xtSDbckuFy8B2tc8oCDWJnD4vh0OUmHekvMhwDNXUDnC05wDmmGMXRl1qyaY9PA9y1ozyZUJ9PX89QPETpUDxGz8qevzWLgHwdJTSiPgPUdo2M5onxWjUZ0zTU1cypcMFFkQIhF16l4mlHbbCtqFD4mmiYE43o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=pNLrw8XCt2GmdeC00s5pZY_FxrT_uZ1Qa_yLZeCxWYVttxck--biL9KkONxmFMZU5IQfRXe1c21NHbqrdB0n4y2E0YvN8Ue3tM6uStUGISalw7Rsx6ASNTgI7zmlwASIRRgkX8Eo_LeNp9LIbxnZwYVJZX0xsqADv4L1QfKop2txOtAdeYli07QlJkGnpm7IbbsQIl1pNSRLIhWaklJKxk6Rty7OjiYA9jcffIPrwq2V0yoVBnbaH9gEdAdWINlipHyFE3xqdb-GNLRNeGmjXzQhX5OI9zOwFaZa-bgWU6JPCxUf6rp7IuB_lCzO_i5IxlCZCAaJGCRIbtfE0kjdjhCMs_xrtoeAyV0rTVsENW1_XUr5tmP2NysbrLKC2YiYA0ipZABNi_iyBtWjQoX_5IDAmCbLrJ09h4V9ZpJmASYDqQuDhUcvdFT7jQ6OguY2X0_adi00iSII4R_5ZgtmnW0ZB_lL9yl1lo-oHpJ7T0D2xh0azA3sLYuhJ3-rop0ZRksiw6UPK_oK1xtSDbckuFy8B2tc8oCDWJnD4vh0OUmHekvMhwDNXUDnC05wDmmGMXRl1qyaY9PA9y1ozyZUJ9PX89QPETpUDxGz8qevzWLgHwdJTSiPgPUdo2M5onxWjUZ0zTU1cypcMFFkQIhF16l4mlHbbCtqFD4mmiYE43o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=CMflSyqouDP4NPDLM8DbClnLOvsb0r6zmymss0NjIHAhwdAq0rlmu3pLVzd3sakyOe3xd3lZrdPSOjFlJOD2tVqNxYNOv3Z7qu9ny9Q7Dw1pXCVB889pOb0QEHM-59G3rwUEdcUu39_UfrTywpQHoSBGQ59mwHB1DHeMbCG_LP842U-FoIsbq6E-8KN-yd6HEParxwmlspjaOBvtrl5yYASt9qzWzs7bcx1TJNGs-e3n0bIjFOZiD_gaXpjRaYUD3BIA3DlNVw7cQYmyM8u8_t7o0IQZ2662VXRL_WZ7vv0Qatk1Paxuw7LtfzG1NFRrZlz4CPnAnTjIIEXCANqbzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=CMflSyqouDP4NPDLM8DbClnLOvsb0r6zmymss0NjIHAhwdAq0rlmu3pLVzd3sakyOe3xd3lZrdPSOjFlJOD2tVqNxYNOv3Z7qu9ny9Q7Dw1pXCVB889pOb0QEHM-59G3rwUEdcUu39_UfrTywpQHoSBGQ59mwHB1DHeMbCG_LP842U-FoIsbq6E-8KN-yd6HEParxwmlspjaOBvtrl5yYASt9qzWzs7bcx1TJNGs-e3n0bIjFOZiD_gaXpjRaYUD3BIA3DlNVw7cQYmyM8u8_t7o0IQZ2662VXRL_WZ7vv0Qatk1Paxuw7LtfzG1NFRrZlz4CPnAnTjIIEXCANqbzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شدت انفجارها رو ببینید
بخشی اش موشک‌ها و سلاح‌هایی است
که درون تونل‌های این تپه بودند.
این دژی که تصور می‌کردند شکست ناپذیره از درون نابود شد.
پول‌ها و سرمایه‌های ملت ایرانه
که دود میشن و به هوا میرن</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6726" target="_blank">📅 09:48 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6725">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=dFy20vKgUVjpuQv63UqDAvBuPH7o6Nc5gW7s04niLxnS7cotYMAzgZfceC-c2_iir6qF1qhQd1gEnSKQuEvvK3tgLtJHHpHyEjxPvw4MtLQwUBp6csNScZwWjdnQZUl_bBWs9ffdo-7ou1uFlFfe7Y59Ol4S6jsISj2akCB56oU7t9o14iNTAptr-ly-wg_UgQPhXSZ7IGzh-km-F73Vsunx1GdSeXhjXRyIGEUftlmqzXylgJYIdhWrChLKyWyHaGW6gZjrI4cTkA53EPE-fXUeKUu2cEUTr8bBvDjftxZv-tYZgHLOYqxOaTUAIVdMT8Zh-XIky7JLmoHso__O5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=dFy20vKgUVjpuQv63UqDAvBuPH7o6Nc5gW7s04niLxnS7cotYMAzgZfceC-c2_iir6qF1qhQd1gEnSKQuEvvK3tgLtJHHpHyEjxPvw4MtLQwUBp6csNScZwWjdnQZUl_bBWs9ffdo-7ou1uFlFfe7Y59Ol4S6jsISj2akCB56oU7t9o14iNTAptr-ly-wg_UgQPhXSZ7IGzh-km-F73Vsunx1GdSeXhjXRyIGEUftlmqzXylgJYIdhWrChLKyWyHaGW6gZjrI4cTkA53EPE-fXUeKUu2cEUTr8bBvDjftxZv-tYZgHLOYqxOaTUAIVdMT8Zh-XIky7JLmoHso__O5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی به «علی الطاهر» میگفت «مینی پنتاگون» پنتاگون کوچک. با هزینه میلیارد  دلاری، با صرف ۱۸ سال زمان، شبکه‌ای از تونل‌ها در درون این تپه ساخته بود،  مرکز فرماندهی، انبار تسلیحاتی، محلی برای حمله به اسرائیل و…..
اسرائیل دو سه ماه محاصره‌اش کرد و اجازه نداد آب و غذا به اونجا برسه،
سه هفته پیش جمهوری اسلامی
به آمریکا پیام داده بود که اگر دست
به علی طاهر بزنید، جنگ برپا میشه و…..
اسرائیل در یک شب، پس از شناسایی ورودی تونل‌ها، ورودی تونل‌ها رو نابود کرد و تبدیلش کرد به یک «تله» برای سازندگانش.
جمهوری اسلامی تنگه رو هم بست و خودش در داخل تله اش افتاد!</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/6725" target="_blank">📅 09:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6724">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=Vp5wIFxm5c_iNJJWtBuIDMyxm6MiSZw_kb3AUVDgiIpsFb06wYblEMw3AvgwPl8aQeAo9J1HJss8I0UErpXomT3ghVI4qrjToNoA6idPicyvUt_W2jYecGFnGqPfZJCL3TIk_I6UhbAwgax7a9kuYUI8Lig3To4BB4vF_ZYjZ2NhP1Y46cC5FzCNPPrDzifBdHViQRmlgQS2IOpcfSyYHInyQY7IolcT9iuS6NpX5kCS3WaezIGBLymd6oH0hY_SbgXA-iyfNgI_H1fuqIhy9mZShk7iQ58GNGfNZKDL1thq4WMMThWr1nmPrW2rOpPtSX09cDJJqf0gJ_AJvg-egw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=Vp5wIFxm5c_iNJJWtBuIDMyxm6MiSZw_kb3AUVDgiIpsFb06wYblEMw3AvgwPl8aQeAo9J1HJss8I0UErpXomT3ghVI4qrjToNoA6idPicyvUt_W2jYecGFnGqPfZJCL3TIk_I6UhbAwgax7a9kuYUI8Lig3To4BB4vF_ZYjZ2NhP1Y46cC5FzCNPPrDzifBdHViQRmlgQS2IOpcfSyYHInyQY7IolcT9iuS6NpX5kCS3WaezIGBLymd6oH0hY_SbgXA-iyfNgI_H1fuqIhy9mZShk7iQ58GNGfNZKDL1thq4WMMThWr1nmPrW2rOpPtSX09cDJJqf0gJ_AJvg-egw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ویدیویی از نخستین توزیع قند و شکر کوپنی در دهه ۶۰، عبدالناصر همتی، خبرنگار وقت صداوسیما و در میانه گفتگو با مردم به مصاحبه شونده می‌گوید: «اگر قند و شکر کوپنی کافی نیست، باید کمتر بخوری» مصاحبه شونده هم می‌گوید: «اصلا ترک می‌کنیم، ضرر هم داره ...»
همتی در این کشور خبرنگار ساده بوده و شده وزیر و رییس بانک مرکزی و کاندید ریاست جمهوری‌ ...</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‏آغاز جلسه شورای امنیت سازمان ملل برای بررسی موضوع ایران</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6723" target="_blank">📅 17:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6722">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=jpehaijEhOKfmA1gTYNDiyf5VryNYWldhqt2bwz4OzQJekp3H6lQP_ixnvvmtVkwmY2v9_aEZckQDE5DdPuSlV-Sg42wmpniist6bOyUfrxgZ9mA4bcPRZ5jZF4Jc_XpcYfsgByKAnd9XfVbn7if0VD5K_alQToElVBf6uECQS5af3ZLJfG1H3A-t507magiwv_sHYryW1u5lAyyA6H3h06i0qRz6o0e2S_l4NHBVc7uH_vNYOLZ56IgFVHxFjk08rSkRZ5le0t1oKemTtVVQ76TOUXhJbonf-2ugPLPHIQh59iNODK3-xD-PSYV5hjwcs1m0Bn7hBtRoCvX15gwsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=jpehaijEhOKfmA1gTYNDiyf5VryNYWldhqt2bwz4OzQJekp3H6lQP_ixnvvmtVkwmY2v9_aEZckQDE5DdPuSlV-Sg42wmpniist6bOyUfrxgZ9mA4bcPRZ5jZF4Jc_XpcYfsgByKAnd9XfVbn7if0VD5K_alQToElVBf6uECQS5af3ZLJfG1H3A-t507magiwv_sHYryW1u5lAyyA6H3h06i0qRz6o0e2S_l4NHBVc7uH_vNYOLZ56IgFVHxFjk08rSkRZ5le0t1oKemTtVVQ76TOUXhJbonf-2ugPLPHIQh59iNODK3-xD-PSYV5hjwcs1m0Bn7hBtRoCvX15gwsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=X1ZY79LzlpCkLHGHF_8D8cc488xbFdnDnDkxjMfOEc1hivAQTolE4Q7nwQsb1Pxlx2Bl4Plkdd9fHoDgYGh_BmJ27NhEIj42pNfTzObPA-fk5xXxLyED6tSquVBsEe23gkzjYV0LDOkSoLSoq0adqWfJhYnzjHL7OI0sXslh0oApWAv8l8JUCrtku9wN1FnJEGBgY7-9pGqZAcbySjy0PlJCujykKQmGhgsmpkGp7riYj-kA71wBYX7sIIn09CMH_dnhq7KQXopBEULc2IvmPE8iJxZvOnWKKPKbO98JuAaHnRAVZIGSfdc3uKdacRd2eFLACtoVzwQt59sBpCYvwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=X1ZY79LzlpCkLHGHF_8D8cc488xbFdnDnDkxjMfOEc1hivAQTolE4Q7nwQsb1Pxlx2Bl4Plkdd9fHoDgYGh_BmJ27NhEIj42pNfTzObPA-fk5xXxLyED6tSquVBsEe23gkzjYV0LDOkSoLSoq0adqWfJhYnzjHL7OI0sXslh0oApWAv8l8JUCrtku9wN1FnJEGBgY7-9pGqZAcbySjy0PlJCujykKQmGhgsmpkGp7riYj-kA71wBYX7sIIn09CMH_dnhq7KQXopBEULc2IvmPE8iJxZvOnWKKPKbO98JuAaHnRAVZIGSfdc3uKdacRd2eFLACtoVzwQt59sBpCYvwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صدا و سیما میگه :
مردم ایران در خانه‌هایشان
«۵۰۰ میلیون تن طلا دارند»
یعنی «هر ایرانی» حدود
۵ هزار و ۸۰۰ کیلو طلا داره :)
روایات اسلامی و معجزاتشون رو هم
همین مدلی ساختن!
اون مجری شوت هم میگه : الحمدالله!</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/farahmand_alipour/6721" target="_blank">📅 09:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6720">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=VKxi8-ZvoLClkRxFQnBJGKFQcy0FyQErlAvqe9E4odTGK3ObMgyFKEcI2Zmif-mclKi8-2Au7b6OLZWmhUFkz5sy5uFDh2uY59w3Kj2U3MQnf52beisk5mCp7JSR_xX8eJL5mKpO_mWqWuwVdJqEuNKIWjlS0-hkUBZm7JLUiTF5L8shDNYcAoFxliQmPgxvaeITwZ-mDI5uYqEYWZSsvfc36r-Zb-lWIjHdempCJr_d2TsizGsCPMwvGmhnrZibhdzyKE9InVsFwRoEMLMmktIjuatacvUJSjX_kFjLD1N3D5BHBTn2dqt5Uulx9YLqgoRmtL0c6YCCSH-QBjeCsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=VKxi8-ZvoLClkRxFQnBJGKFQcy0FyQErlAvqe9E4odTGK3ObMgyFKEcI2Zmif-mclKi8-2Au7b6OLZWmhUFkz5sy5uFDh2uY59w3Kj2U3MQnf52beisk5mCp7JSR_xX8eJL5mKpO_mWqWuwVdJqEuNKIWjlS0-hkUBZm7JLUiTF5L8shDNYcAoFxliQmPgxvaeITwZ-mDI5uYqEYWZSsvfc36r-Zb-lWIjHdempCJr_d2TsizGsCPMwvGmhnrZibhdzyKE9InVsFwRoEMLMmktIjuatacvUJSjX_kFjLD1N3D5BHBTn2dqt5Uulx9YLqgoRmtL0c6YCCSH-QBjeCsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قابل توجه کسانی که دنبال بهانه‌ای هستن
برای پناه گرفتن در آغوش امن و گرم آخوند و توجیه حفظ قدرت در دست این‌ها.
این مفنگی، پدر زن مجتبی خامنه‌ای،
میگه «فعلا به خاطر شرایط جنگ
با حجاب کاری نداریم»!</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/farahmand_alipour/6720" target="_blank">📅 08:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6719">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=Tiw45MxS0sbPPiUn3Emuw-RbaDdj23vuYQheT03nBj0BDdBPYVipoOqW-C2-12ujN-6j_uSu3WO1PVOvCdlKznDdeSAFfN9Mq_UHnklqru20ggNSzB1eS5M0NdJS9XH6BpoFsb2bDbWznqNp5sEl1HHmWNDTkwZp4V7Xls33WTcOM6yE5rHrHi-QG_RqL2iE8TX126ETnosc_V1Gy3-vWL2GBQY1bAtPdpOBF_dIK49LsGWC1D769BtUOzkflT5kI5f6nozYS6y3AkbJUnTLMQOhZHl_ftiZLcu3SMW2bLtM5Rv9pY2-oCcvAjMxyBJv5A3_nWSqw53lQ_oMvpiqSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=Tiw45MxS0sbPPiUn3Emuw-RbaDdj23vuYQheT03nBj0BDdBPYVipoOqW-C2-12ujN-6j_uSu3WO1PVOvCdlKznDdeSAFfN9Mq_UHnklqru20ggNSzB1eS5M0NdJS9XH6BpoFsb2bDbWznqNp5sEl1HHmWNDTkwZp4V7Xls33WTcOM6yE5rHrHi-QG_RqL2iE8TX126ETnosc_V1Gy3-vWL2GBQY1bAtPdpOBF_dIK49LsGWC1D769BtUOzkflT5kI5f6nozYS6y3AkbJUnTLMQOhZHl_ftiZLcu3SMW2bLtM5Rv9pY2-oCcvAjMxyBJv5A3_nWSqw53lQ_oMvpiqSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان حکومت دیشب این شکلی موافقت خودشون رو با قطعی برق و افزایش قیمت بنزین،
دلار، طلا و گوشت نشون دادن:
تو تاریکی می‌نشینیم، دلاری گوشت میگیریم،مهریه کم میگیریم!
موجودیتتون ذلته!
دیگه ذلت چیه!</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/farahmand_alipour/6719" target="_blank">📅 14:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6718">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">دلار ۲۳۲ تومن!
💸</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6718" target="_blank">📅 13:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6717">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xn3ExmWKJ8lFhWLGbQkqAsxq5aqc-cWHwUbRz4s5d_he3bgVP57lNksgkMgi2_aFx0qfc60DqCMW6wcSjAdd6cR0oHY1FJTVINNuXZKBQRlUBwgu5ZklgbGC1jupF0LSV-loqj9ZHBR9haIJQL4MhO8hRo-ySIr1SCOBnKYft9V1n5dDuFemGfDvewcLq41Uwms0yf85uS2CZrGgI3zogIHYtbcaXVcQRQe63vmZ7-Artgn-xPLr2M83sFPU-AlzIJMlZBgWWrof4oGQgjIXE3VrhCqOTeLbh7TYaxRr8ZNNnIIuhVIHJFkMx3KYL7LNcMYyGq_1TWOVhUcogwNMWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکر نعمت کنید،
بلکه این نعمت‌ها افزوده بشه،
اصلا گیریم یمن نیفته دست عربستان!
بگو اصلا بیفته دست کفتارهای
بیابان‌های سومالی !
همینکه این‌ قوم ظالم در ایران شکست بخورن  و به غصه‌هاشون افزوده بشه، جای شکر داره!</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6717" target="_blank">📅 13:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6716">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=OhzzoQFkwtXtbW6jbwj96EN6XWEU2ELjcOKpqx7iX_dOTVLicNp8hYzQ87isj3cyOYyflPDPUL0WxRfp8sRZgnF9F0qKXJFdh1kgKgGfrg7GcxhtjdEYW2CBJLlUPwUJMBxWI6512woUe_F9-YxiIuqEUdrohI2p6Tt0Wxep5k8W0waLn1HlmGU89aQd-ExLHy5avoG9hNuOKMmWm4_WHmY5ZaTdrdmqR4Ft2f8b0W3oam0PYnO-FooZ5rUbMsOAbAYW7etXDx5OJKowofI8doMFmE4fKtusqD8YvKFmRsfUWT7-snvQZ5lAk-vFQ_i938pQihW6XSfFT96x_a2ORA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=OhzzoQFkwtXtbW6jbwj96EN6XWEU2ELjcOKpqx7iX_dOTVLicNp8hYzQ87isj3cyOYyflPDPUL0WxRfp8sRZgnF9F0qKXJFdh1kgKgGfrg7GcxhtjdEYW2CBJLlUPwUJMBxWI6512woUe_F9-YxiIuqEUdrohI2p6Tt0Wxep5k8W0waLn1HlmGU89aQd-ExLHy5avoG9hNuOKMmWm4_WHmY5ZaTdrdmqR4Ft2f8b0W3oam0PYnO-FooZ5rUbMsOAbAYW7etXDx5OJKowofI8doMFmE4fKtusqD8YvKFmRsfUWT7-snvQZ5lAk-vFQ_i938pQihW6XSfFT96x_a2ORA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=grQxtbcuQ2sUYYSa-Ur5tB3Bvygm9IJFtS-i9DQ3jMpx2rA9oIXe50xqVwBbMtXWrSWUOEWNd2uMtjqMtGh4LltwXRA0ycn_De19WfDpyg3DssjAsCKnEwaW1uZVxAHz6TeoLWc53IOMQ0BEPCV84V26mXyXjIltq1pkHFutcYzHni2_5DktBytqH4tYkSb9c6QAfEmzK1QF9X86o2IBGb9u4I6I0exhBGEnT7LD02UwOqmwy_V-G4EMAYALRWBOP9cqEs7QEce-BK2krlWQKILduzTUqdxz8eyRHdA_m0qqxuuFfemAz2Cbb6LWjfl-13BO7iOqr7rhrbRQMoY1og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=grQxtbcuQ2sUYYSa-Ur5tB3Bvygm9IJFtS-i9DQ3jMpx2rA9oIXe50xqVwBbMtXWrSWUOEWNd2uMtjqMtGh4LltwXRA0ycn_De19WfDpyg3DssjAsCKnEwaW1uZVxAHz6TeoLWc53IOMQ0BEPCV84V26mXyXjIltq1pkHFutcYzHni2_5DktBytqH4tYkSb9c6QAfEmzK1QF9X86o2IBGb9u4I6I0exhBGEnT7LD02UwOqmwy_V-G4EMAYALRWBOP9cqEs7QEce-BK2krlWQKILduzTUqdxz8eyRHdA_m0qqxuuFfemAz2Cbb6LWjfl-13BO7iOqr7rhrbRQMoY1og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم
همون ۱۶-۱۷ فروردین، کارشناس
صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه
رو رها نکنیم تا قیمت نفت بره بالا!
و فشار رو بر آمریکا اعمال کنیم!
چون خواست مجتبی خامنه‌ای اینه!
نتایجش رو هم همین روزها داریم می‌بینیم!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6715" target="_blank">📅 11:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6714">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=mq5YhCP_gvxbQx8dMn7pGbVc5u_MqWC5tohJQNfzA5UIKfrDeLqG3ZWHrtzWhfrv4XfP514leniIW3rOe1L_BLpAebbl79uklsKo8lllgeXJX4TXZV8Avhm6yVdR1OBLKmZhLpLnqycebWt3PT8StQ1jhhgRbTzU2BS7XL5WKs1aJz48q43gF2uwZYb53CAUh8kG3gDi6EkMPw42TbCOIoQ-06pKSHMTjn_Wk-JL0rpl-PptXMeriFSQzIg6i3_ADcPdDOLwT4Wi3TTIsKR0igEDutv9Jg4aTM1kyCCO9u-ovSp_3kgQRXcflkRF3AyFgpjDSE-IaLta8TnO7NprdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=mq5YhCP_gvxbQx8dMn7pGbVc5u_MqWC5tohJQNfzA5UIKfrDeLqG3ZWHrtzWhfrv4XfP514leniIW3rOe1L_BLpAebbl79uklsKo8lllgeXJX4TXZV8Avhm6yVdR1OBLKmZhLpLnqycebWt3PT8StQ1jhhgRbTzU2BS7XL5WKs1aJz48q43gF2uwZYb53CAUh8kG3gDi6EkMPw42TbCOIoQ-06pKSHMTjn_Wk-JL0rpl-PptXMeriFSQzIg6i3_ADcPdDOLwT4Wi3TTIsKR0igEDutv9Jg4aTM1kyCCO9u-ovSp_3kgQRXcflkRF3AyFgpjDSE-IaLta8TnO7NprdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون هم که با افتخار این  تصاویر رو منتشر میکردن!  بگذریم کل سپاه و ارتش و بسیج و مردم و عشایرشون نتونستن وسط خاک ایران،  این خلبان رو پیدا کنن!  فقط هی نوشابه پشت نوشابه باز میکردن و تعریف و تمجید از خودشون! زارت!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6714" target="_blank">📅 11:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6713">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">هالیوود از این داستان فیلم خواهد ساخت خلبانی که وسط جنگ ۴۰ ساعت در عمق خاک ایران بود.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6713" target="_blank">📅 11:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6712">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">آزیتا در کالیفرنیا داشت محله نیاوران و فرمانیه  رو به دوست آمریکاییش نشون میداد،  که ایران چقدر پیشرفته است،  یهو به خاطر اینکه خلبان در یک منطقه نه چندان نامناسب اجکت کرد، سی‌ان‌‌ان و فاکس‌نیوز پر شد از این تصاویر از ایران!  تازه هالیوود فیلم سینمایی «نجات…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6712" target="_blank">📅 11:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6711">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=fIi785eb7SZAhzSQ0EgxvlGZA0a_okgeRyfxmbgdUiEteMh8I4y0fFaBG5G3GrLhBBEVJFdMlgitcJQyVw9O-hrU1_x-l3IoMp-mqEmPn4LHyDXp_tUpCLgOxU6dzU7PNBALc1VZHn1mIkXKKyxwr01Df3hM2wZw9TGP9W4_ZGcWWih05mqtxenPsN57c5u2kihfeFh7wPGRoWPCvUrIDHz1DLsHBcKMgX7kVrvIfGiYKYMWJEkGydzG1nL1XJRVK0iFG3G3DH44NcIoTbgMjj0exnOtKi_K-u0hRGToprtwBookBO_atP-5a8qoibGdqDjqKwdxz22GFKmZj9smwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=fIi785eb7SZAhzSQ0EgxvlGZA0a_okgeRyfxmbgdUiEteMh8I4y0fFaBG5G3GrLhBBEVJFdMlgitcJQyVw9O-hrU1_x-l3IoMp-mqEmPn4LHyDXp_tUpCLgOxU6dzU7PNBALc1VZHn1mIkXKKyxwr01Df3hM2wZw9TGP9W4_ZGcWWih05mqtxenPsN57c5u2kihfeFh7wPGRoWPCvUrIDHz1DLsHBcKMgX7kVrvIfGiYKYMWJEkGydzG1nL1XJRVK0iFG3G3DH44NcIoTbgMjj0exnOtKi_K-u0hRGToprtwBookBO_atP-5a8qoibGdqDjqKwdxz22GFKmZj9smwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fm5Z1YqTuEuSz-0s-5Ry2Tt_l209YcaOOchzekOvbR6WT_CTqK3pyLL8CK0NVFm8z1BrJe5BKIfqgNV_yxmW0G6jSmxZ8PqqZ7-t_0v3DVH7BsyyA8hEYr448x4rWnBLoIbY8XwGh6MUhhgULvasJbm_AGLB1VMBvascaKu-8mIvtdZ7zEdvQxNi4yqE66ubquLSR5kpoS6sL6iolsw8AxnroUrZvpO-DC2PVYFYsj-Mlfd-jZzt1skRuVKZa2bf7A9CWi4jJbgJJ2SkiJHgJn0oi0ofCMla-LUnGexE99R1IcbSK0rLCOKRhtIURWT6QISi_mzeXIPESUY21rrF7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
شب گذشته و در جریان حملات آمریکا ۵ نفتکش ایرانی منهدم شدند.
سنتکام اعلام کرده که حمله به این نفتکش‌ها در پاسخ به حملات موشکی جمهوری اسلامی به  یک ناو نیروی دریایی آمریکا صورت گرفت، گرچه ناو آمریکایی آسیبی ندیده بود و موشک‌های شلیک شده ج‌ا دفع شده بودند.
سنتکام ویدئوی انهدام این نفتکش‌ها به نام‌های « ام‌تی کاویز، ام‌تی چارمینار، ام‌تی هورایزن ۱ ، ام‌تی ریسکو و ام‌تی دریا» را منتشر کرد.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6709" target="_blank">📅 08:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6708">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
ج‌ا با ۱۳ موشک به اردن حمله کرد</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6708" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6707">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
طبق گزارشات، سپاه از اصفهان، یزد، تبریر، لرستان و... بیش از ۳۰ موشک شلیک کرد و حملات سنگینی رو آغاز کرده!</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6707" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6706">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
حملات موشکی جمهوری اسلامی از مناطق مرکزی ایران</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6706" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6705">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها، ارتش آمریکا امشب دو نفتکش ایرانی را  در نزدیکی جزیره خارک غرق کرد و به یک نفتکش دیگر در نزدیکی جاسک حمله کرد.</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/farahmand_alipour/6705" target="_blank">📅 23:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=RtPc_X4H42TK-Vh1mdPg0oZ9olNRnMbt7lUbWeSTFI5gKlKgJ2OOBCmfSB1IWT-8EeHzx-0k8kE2L0XwQktCs0SMD8PQhhlpazs4Pa-0hGJURZrPCtYx5WyIgqW_HvnbdOK5DnnKI0fhh4BTfyGkRvw24GFKYHF4bRh4X7wgsOOOaAuXYbH0EH33UB6xDKrn08ssdWtKY6q-FK7AjGDwDonJ3aqw4wT5F6nuea3leqPfjoCQD4h_IfToVhLy-HNyKWxcmvCKxcHansvgQuHOPw2UnqulAwDpEDN9Q9-DymxUhK9vdWp9UH6tlXQ4cYRaBtw4nQEctULQahyxVChSSIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=RtPc_X4H42TK-Vh1mdPg0oZ9olNRnMbt7lUbWeSTFI5gKlKgJ2OOBCmfSB1IWT-8EeHzx-0k8kE2L0XwQktCs0SMD8PQhhlpazs4Pa-0hGJURZrPCtYx5WyIgqW_HvnbdOK5DnnKI0fhh4BTfyGkRvw24GFKYHF4bRh4X7wgsOOOaAuXYbH0EH33UB6xDKrn08ssdWtKY6q-FK7AjGDwDonJ3aqw4wT5F6nuea3leqPfjoCQD4h_IfToVhLy-HNyKWxcmvCKxcHansvgQuHOPw2UnqulAwDpEDN9Q9-DymxUhK9vdWp9UH6tlXQ4cYRaBtw4nQEctULQahyxVChSSIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی موز خوران میگه
که از خامنه‌ای «وصیت نامه» نمونده
و دنبالش نباشید!
(خیلی‌ها حدس میزنن که در وصیتامه‌اش اومده
که از پسرانش کسی جانشینش نشه، برای
همین منتشر نمیکنن)
صدای کار و چنگال و بشقاب و
صحبت از وصیت نامه رهبرشون :)</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/farahmand_alipour/6704" target="_blank">📅 18:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6703">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">بنزین ۱۰ هزار تومان!</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6703" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6702">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=Nw7yOs1HRf0-RGkbWhuxCqUArB8-BOucIEime9aPK5B2MHa35KjrY2aflipO0ksPqBBhm-JXNM-4Q9qu0JqiuSNW8o3_4MfiZJSO56L-XjRdDnpH_TO208knRap9mqBa401Sxm5RQJZI9aFqbsmYRLEeH2TZ5RVch20ETGHyODLQwFt2pwQBqHm43bpWVdcnDXbYJqoIO7EyGkBA905TBFZQOBuYS1aONuQa7a8n5G1mYyw7r_zOAXFWML5YSOo73VNFwPORvQwXK4t83hj0g9cIc59jksKwL9JPBN2o6hkotnMv94MOGxswbMaMR_FTjGdIqwT7rGMI3NGxdyC_BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=Nw7yOs1HRf0-RGkbWhuxCqUArB8-BOucIEime9aPK5B2MHa35KjrY2aflipO0ksPqBBhm-JXNM-4Q9qu0JqiuSNW8o3_4MfiZJSO56L-XjRdDnpH_TO208knRap9mqBa401Sxm5RQJZI9aFqbsmYRLEeH2TZ5RVch20ETGHyODLQwFt2pwQBqHm43bpWVdcnDXbYJqoIO7EyGkBA905TBFZQOBuYS1aONuQa7a8n5G1mYyw7r_zOAXFWML5YSOo73VNFwPORvQwXK4t83hj0g9cIc59jksKwL9JPBN2o6hkotnMv94MOGxswbMaMR_FTjGdIqwT7rGMI3NGxdyC_BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صحبت های سردار محمودی :
ترامپ باید موشک رستاخیر و موشک آتش افروز ایرانو بیینه،ی موشکی داریم سوخت جامد وقتی وارد جو هر شهری میشه خودش جنگ الکترونیک راه میندازه، کلا تمام وسایل الکترونیکی و برق ی شهرو قطع میکنه، وقتی به هدف میرسه قبل از اصابت تمام اکسیژن هدفو میخوره و وقتی سر جنگی این موشک به زمین خورد، ۸۰ کیلومتر مربع رو کلا نابود میکنه، اینارو هنوز رو نکردیم.
﻿
+++ قدرتمند ترین بمب اتم جهان یعنی بمب هیدروژنی تزار متعلق به شوری ۱۵ کیلومترو کاملا نابود کرد.</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6701">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرده است که موشک‌های بالستیک ایران، ناو هواپیمابر «یواس‌اس جورج واشنگتن» و یک ناو جنگی دیگر آمریکا را هدف قرار داده‌اند و این دو شناور برای گریز از حمله ناچار به انجام مانور شده‌اند. در این حمله هیچ‌یک از نیروهای آمریکایی آسیب ندیده‌اند.</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/farahmand_alipour/6701" target="_blank">📅 00:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6699">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pBp9vqCoRWu4pUzQi_VuqnGIOE1Nblx_Q0qlWPhgpg-Q0NCs3H56uAJefQI-VO04FgipxcyMwV192FBxu8Cr84ZxJz851pz200nBOnavlqaTwgH0suEpJw94yMBw_GzwGfBBDmzrmy9UK0H-cwi0YkI7-LMjuLVKG8czA2A3c-r1M39qz40_KJYcnKNlLrMiRURBQnIMeJmHasOxWreeoI4JUh8AmbRCOwVjNHSvmG194MuvhUU1DeEfontQqbiVglA7F5vXZmVorEkdlRMi3pZ5pv7hd_YcABrSjqKAXUBfFqDQghbjOxg_LoZOiTxWeytshMyOKrlfmo2NlYBjFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZIM5aMkVitxpf6rVvbBkFVX0iFUQxAWdc33byWlFGLITta335apaN_xHwIU_pKJXE_yOegwuIAC9ZtGKe_HA5lNHZxuIT2Tq3AvyBtMKyZThskVGpkN0iiQLlM2VIjI9xwXe7KUf946PFNbNJ8QyiWraT-6l_PrRj0bDf7CrM-E9J8xSdxqxVdxuwJ5i7kxcWuw99GkYyuVFO200FBnY0NHHkSaIF6TvquAUZ5wj-Jw-RgyL1GiFyvFngDVuW9qUz6cExyBIMQDIPujaTVa5CCJaTG6n63cf4kW0yWCXPvWH2iRq3o7dtM5mh3y8_oSRsoeiNR2sOCt8gJFiDW4MYQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برده‌ها در مزارع پنبه اربابان سفید پوست
در ایالت‌های جنوبی آمریکا،
سالانه در بدترین حالت ۴۳ کیلوگرم گوشت میخوردند. در حالت معمولی حدود ۷۰ کیلو گوشت در سال.
ولی در برخی ایالت‌ها وضعشون بهتر بود و برده‌ها تا ۹۰ کیلو گوشت در سال مصرف می‌کردند.
وضعیت برده‌ها در آمریکا، بهتر از وضعیت زندگی در کشور امام زمانه.</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/farahmand_alipour/6699" target="_blank">📅 21:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6698">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=LTGnLHjKweBJWoxMvQ6MdH3M6GwXkMv6SgVJKE2yRzmHd15jzkC4am_hnC6LdKR1GlSUq_t141tf4cSyl0afEACOzKVCfPjtl22PhLrXUcXMiGnH3v_ZWRxDSQm1-DuAsG9pa-q3T4qQOrXy6RuJFczrOn_qJhZk9leSJvellarKmtaAiqwz6T8TvMWSkBa5K3MXl_2-Y7NexcxDEj2NytoOeIAgtO6bVGpI3GY4r_Peu-w7Xro_QLgcszeCZWP_2SSRXXUV03mOSKngo44BGXyaO9yE2QLJRi_BlM3OoHosG5lQwqkvO-so2XkYUtk8-EQbU4DN_vyulbvBS3B3zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=LTGnLHjKweBJWoxMvQ6MdH3M6GwXkMv6SgVJKE2yRzmHd15jzkC4am_hnC6LdKR1GlSUq_t141tf4cSyl0afEACOzKVCfPjtl22PhLrXUcXMiGnH3v_ZWRxDSQm1-DuAsG9pa-q3T4qQOrXy6RuJFczrOn_qJhZk9leSJvellarKmtaAiqwz6T8TvMWSkBa5K3MXl_2-Y7NexcxDEj2NytoOeIAgtO6bVGpI3GY4r_Peu-w7Xro_QLgcszeCZWP_2SSRXXUV03mOSKngo44BGXyaO9yE2QLJRi_BlM3OoHosG5lQwqkvO-so2XkYUtk8-EQbU4DN_vyulbvBS3B3zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W1TjkJP3XPGeh5OUp67NPj24W0FKMGzVd1k7iTOrtIaX8JAzxt7fhTzlcb1GW6vMjQDcfBllpdFDlWTTBowTzGqcSt1UuAwBqdXA7lloRQbufGHEKyykYVLi40c5jYlJwOG8mS1aqdrKB1Ul9AaZLydDCwG0KqkWyaAYCergQJQ4p5yFJ9QwwsFPFa5nnT3yAYsb2hoiKvpZj6ZoM6JfjIVD3AgvN5u_9EeL6jMAvQ_AD55BmKWjD-JOk7P_-Bab_1bfEEGdVLq93tkTn7tTjl3_omTpqncg-xagxBOyF7--Uef4cpA-RI0P9DRCptB3WqBdx_99KoNPyIwudukX_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
