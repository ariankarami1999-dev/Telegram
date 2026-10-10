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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-18 16:17:25</div>
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
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/6804" target="_blank">📅 15:30 · 16 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/6803" target="_blank">📅 11:29 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6802">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AGOey_jBLBxLdpyqfgjQ6yjG5SXM9Y_BC1Eo5u_9ziTd6Ab5PkydFXpZzms3lAZB_iZdgrzXGZKHQRgFhZlmJS0jhYIvn2r4ycW6xwUW_0P9eoijkIqy2OZjJimxkyHSiozJ9TDjd6yLoKb2ImlGI7t0PohtRx39at9KRyV0B5HzsaOv1oY-ljON9b2-nsRWHKTBIyBol7VSalGopyUbArXtwPX__KIND5nyLA-SampYzI8g1nbGfBZQix2VlT2UheRd8wHJDbCgHSnc_M73t6eF5kLetBzD2mhkqG_bi1eUxbiqhHOewnjflG_96sPseWlvP88SFuAk4UdM9m8KLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌د‌ونستید یکی از معروفترین آیات قرآن  که آخوندها دائم به نفع خودشون و شیعه و….. استفاده می‌کنن آیه ای است که دقیقا و مستقیما در مورد یهودیانه؟  یعنی قرآن وسط تعریف یک داستانه، و آیه  قبل و بعدش داره در خصوص جدال بنی‌اسرائیل  و فرعون صحبت میکنه و  اینکه خدا…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6802" target="_blank">📅 10:52 · 15 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6801" target="_blank">📅 10:42 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6800">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">روز ۷ اکتبر ۲۰۲۳  وقتی به اسرائیل حمله کردن،  نوشتن که دنبال کنیز اسرائیلی هستن!  هر چقدر اونجا کنیز گرفتید اینجا از تنگه‌ پول در میارید!</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/6800" target="_blank">📅 10:41 · 15 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6799" target="_blank">📅 12:52 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6798">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tZyMKTdo9tWXDm3IqRKfNsXOxqzuQMJD6G6ykThT6dv-2ySnIhM4CKMENeOZIDBV-Uo03aOSUw6Hma64vVk2AQycakTqlgS5P4AjEOgEcNVF03q9FY2ZJU0p4IgWAXmSy_UFwdmS3-gM9-tMIO949M7VMmg89GAtchbctA5bchSBat6yhElC3zpF_E2OeDXKIIfMHNIm7MKz-eDch7RwC7P1bPLUrkwdw-J7XLO7A9j_4BtWfNeckGE62fg0ZdM1DQ9-7U6e-HRbYmQubQ3PPvgu1Yp0uTvKB8m4V3i6pognp0WnoV4k2bbKvsjIFrn-6ZpYsMYuyDfilgH3U4M4hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه فرانسوی لوپون از همکاری چپ افراطی فرانسه و «اخوان المسلمین»  در تخریب‌های اخیر خبر میده. دولت فرانسه نیز دیروز بر اساس اطلاعات نهادهای امنیتی از حضور چپ افراطی در گسترش دادن اعتراضات و به آشوب کشیدن اعتراضات خبر داده بود.  در حالی که اعتراضات دانش‌آموزان…</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/6798" target="_blank">📅 12:45 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6796" target="_blank">📅 12:43 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6795" target="_blank">📅 13:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6794">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">مثال دوم گنده‌گویی‌ها و شعارها که کار رو به جنگ کشوند و به شکست سنگین  هم ماجرای شاه اسماعیل صفویه شیعه افراطی بود که چند باری داستانش رو مرور کردیم که دائم نامه‌های فحاشی  برای خلیفه عثمانی می‌فرستاد،  یک لباس زنانه هم همراه با نامه می‌فرستاد،  پایان نامه…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6794" target="_blank">📅 14:41 · 12 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6791" target="_blank">📅 12:52 · 12 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6788" target="_blank">📅 12:27 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6787">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">مصر، ثروتمندترين استان حكومت اسلامى بود،به خاطر جلگه رود نيل وكشاورزى پررونق و...! به خاطر اينكه در دوره حكومت امام على ساختارهاى اقتصادى رو عوض كردن وساختار جديدشون رو هم نتونستند به درستى پياده كنند، اين مصر بسيار ثروتمند فقير شد!! يعنى اوضاع اقتصادى داغون!…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/6787" target="_blank">📅 12:22 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6786">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">این رو هم در نظر بگیرید که امروزه به خاطر حدود ۴۰۰ سال تبلیغات یکطرفه، اکثریت مردم ایران میگن حق با علی بود و معاویه در سمت اشتباه بود!  اما در اون سال‌های اولیه اسلام،  چنین شکاف و فاصله‌‌ای هنوز وجود نداشت!  بین نخبگان بود!  برای عموم مردم، جایگاه این افراد…</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farahmand_alipour/6786" target="_blank">📅 12:16 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6784">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">محمد بن ابوبکر  یکی از نزدیکترین چهره‌ها به امام علی بود که حاکم مصر شد!  یک جوان تندخو! از این حزب‌الهی‌های افراطی و عرزشی‌های گنده‌گو!  نه سن کافی داشت! نه تجربه داشت!  اینو امام علی گذاشت حاکم مصر!  حکومت خودش که متزلزل بود!  چون وسط آشوب کشتن خلیفه سوم…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/6784" target="_blank">📅 12:08 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6783">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">پس تا اینجا همه می‌دونیم که  فقط شعار ندادند!!  همه ما این قوم رو می‌شناسیم و ۵۰ ساله که حیاتشون در تنش و بحرانه!  اما فرض بگیریم،  فقط شعار دادن و حرفهای تند زدن بود آیا در تاریخ داشتیم که حرفهای تند زدن باعث جنگ و ….. بشه؟   بله! و اتفاقا دو مثال روشن در…</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/6783" target="_blank">📅 11:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6782">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">لابد در این ماه‌های اخیر زیاد دیدید که حامیان حکومت،  در دفاع از خودشون میگن :  بله درسته، ما نیم قرنه علیه آمریکا و اسرائیل شعار میدیم، ولی کدوم کشور به خاطر  شعار دادن و پرچم آتش زدن و حرف،  حمله کرده به یک کشور دیگه؟   البته که همین جا هم صادق نیستند، …</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/6782" target="_blank">📅 11:44 · 12 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6781" target="_blank">📅 11:37 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6780">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z095M9-xC0Eje0DLYK790QDJg_2G55nste7kmoB3raBf7FB03VujdrVCh2O03z276CuHXqjDCrkXjX_PKO1KPT-67HLDU2jf6L2ZW447dYNNNb-1-Uu6k7Wcmnq3fnLZJ1978waldhop6h7Ml6SS2TFbkNTGlNx3TE-Jeysi9Zek1nSYn-5-xq8cg81sSZ5FhGk_tL-Vr7RdaYvXF0p4ASlWdnskDcOjEXnktpSUrd5_lYigd5UyzVbx4IdC9a85DeRxZdALRhekq2gYfVR__nvf22KWithDxZ20_MFpqFKiRS6vnvbUNfyFHtpm9e3AapSYIMOyW8O1k8wdHPOxLw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bDlZCG2nGGXVImFoKXix_iAahsFqhGZd16WgR0KZUV579K3rCITEyRFjO43pnU3pilkDxQawye88RBcsjNmGHw2hSuBxAFHRQL5OBC91VO-F8VB5Lnw3RfLSnkEqQVPsA0rV6duXbzlPkcsULFNtPcdGMMTGOQ9CCXVyKpXAo5qpBgj-iZdocIgI2PWMEEWPsGd9dnMQ0W5k6uhFPxgpkjqh4eAOymok-fw_ri15f6E7OEPGBCspJixtHqWPMTi8SCZqbNEEfKKqB6qwhFSqr7eWN57v7EBAdztNr1gLiDTJQbX0tRrqJOC2ZnrJdncyqg0_QgsbwgwIAYlbmc4dmQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQkF9_rc3N-1TbwTkHh19Ka2ygCAj1_fPsN9zLCNCjZc5w0cPt2_IZhxz0Uqq-E_kXXahFRRAZMxBPqTvvkviec63CWsZaDSMEchfzHg8ajUPq8OHpSdflIQg3peS5anStNjsUNOjudjKpTEQ2Eq0BrJ8_SF6Loway7xXgJlzRxhZ7cwT3L3r5_LIEyEw8qlTUbOcZPmoYwOkEE-ybTUsOQ5JJK6haBjF9upoU7xVIL_IijnYpqxwQR-xStbCsP5vce0yHJMs2z_TN3ZOMOwI-yCcdYGV_N1cS-iGyxb7Xj0FLanWHKrWsQfAnv_g258HFeCHKla5PsovH0SFwc6NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزش واحد پول ایران، «ریال»، قدرتمندترین کشور جهان در محاسبات الهی، در برابر «دلار آمریکا» رسما «صفر» شده!
در زمان حکومت صفویه،
و بر اثر سیاست‌های شدید مذهبی شیعه‌گرایانه شاه سلطان حسین (مردم بهش میگفتن ملا/ آخوند حسین)  مردم اصفهان از زور گرسنگی به مرده‌خواری افتادن،
علمای شیعه از همین هم یک پیروزی
ساختند و گفتند همین خودش نشون میده که دیگه وقت ظهوره و امام زمان داره میاد و ما بر جهان مسلط میشیم و….
چند روز بعدش شاه سلطان حسین
تاج شاهی‌‌اش رو با دست خودش گذاشت روی سر یک شورشی سنی مذهب افغان و خواهرش رو هم به همسری بهش داد و امام زمان هم نیومد!</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/farahmand_alipour/6777" target="_blank">📅 08:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6776">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c578cb6e91.mp4?token=m_xYMM7mUx76sFaWlmHjkOZLF8aRvahx0k8_uLy2OGJeJBLiK1MeOqtnxQm4eoOQ90K8VJAG-fJemVNUGlDVUfxsP6RU6tRTm-Fu0IatO33_bRR4KbsHWdduY95Oe6qSXzV7YpdHhOGqSDVWmi4VhSzO1O65CL_tZ4KRtVNgkNzjoSawb2H-UR2nMb8A9xMmhquOTceo3M8nOz4I8JLMr84neup-RuNBXW7rSUoaxZ9ZADWoRYXR3PmxdXjJt1RQwQOTQp0eKUrxUYgNKRTBtLisSyj2F8-FKQab1pBhw7E8ZJx5n7_g05FUTrg-YQRZ8zxp4Vqd-cwdMhO2znYObA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c578cb6e91.mp4?token=m_xYMM7mUx76sFaWlmHjkOZLF8aRvahx0k8_uLy2OGJeJBLiK1MeOqtnxQm4eoOQ90K8VJAG-fJemVNUGlDVUfxsP6RU6tRTm-Fu0IatO33_bRR4KbsHWdduY95Oe6qSXzV7YpdHhOGqSDVWmi4VhSzO1O65CL_tZ4KRtVNgkNzjoSawb2H-UR2nMb8A9xMmhquOTceo3M8nOz4I8JLMr84neup-RuNBXW7rSUoaxZ9ZADWoRYXR3PmxdXjJt1RQwQOTQp0eKUrxUYgNKRTBtLisSyj2F8-FKQab1pBhw7E8ZJx5n7_g05FUTrg-YQRZ8zxp4Vqd-cwdMhO2znYObA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/8a5052b840.mp4?token=NdhiDQ1Lj8xWbcltmsYAPJRk8S4D1c3R48wAjNHCS--TAyBnmB7xZ5ZCp9TOJtmduF2JMHS2eZsG4oDNxLShXS8jH8ws6ipTkpn2Hgjuyl9OCztOnZCtUBdhCMQjGKzFPIo7oD5lD-3JPTMtkiG182Uzkz8iNH2CtQHJUoQ7meJ49zDW8MJY59oW6jJbKES89suxLpBVbiUehw1Dmpc57TmP4ptB0erViQhA8PFzPqMWdIU90wtFJHG44KbbptXMEN951dzeAs1mV-Hj3WUFg95qhx33-9u8MpvtJ8mipNV8IMiUDZR5qYWiRE3__gaSZYMp6rLRtUlFniGhH0XYUGXs6nEXAXEcn5Q6OPhFaZi-H-4N-qGWFiSV9Onhwih-cZeuA3jpky843_LjJwbQTnQsj-qbN-she6_GyX1IFkdH8NCMyP8ZJ1peD2LKXFYiHUpjISbu9rVV43F-XSf1tLz5hVQLWhKQuio9V6IiW5PjoD-Lr0yb51BuRbWO32PALODq6oVWs043NxV13cv_uEBpBh1-tPNNXgGoLFxjdatPVztWXvKGzF3MoHHBt-266R1tX3EvUzgIOtIoQgKRyZUuXkwoFUNQyQ7jpqTl57PWwulgmnDLvHMVdwKkcA94unpinhzzY_BZpoaegJWYjN6hbwyM8cO3SwnaBTja2NU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a5052b840.mp4?token=NdhiDQ1Lj8xWbcltmsYAPJRk8S4D1c3R48wAjNHCS--TAyBnmB7xZ5ZCp9TOJtmduF2JMHS2eZsG4oDNxLShXS8jH8ws6ipTkpn2Hgjuyl9OCztOnZCtUBdhCMQjGKzFPIo7oD5lD-3JPTMtkiG182Uzkz8iNH2CtQHJUoQ7meJ49zDW8MJY59oW6jJbKES89suxLpBVbiUehw1Dmpc57TmP4ptB0erViQhA8PFzPqMWdIU90wtFJHG44KbbptXMEN951dzeAs1mV-Hj3WUFg95qhx33-9u8MpvtJ8mipNV8IMiUDZR5qYWiRE3__gaSZYMp6rLRtUlFniGhH0XYUGXs6nEXAXEcn5Q6OPhFaZi-H-4N-qGWFiSV9Onhwih-cZeuA3jpky843_LjJwbQTnQsj-qbN-she6_GyX1IFkdH8NCMyP8ZJ1peD2LKXFYiHUpjISbu9rVV43F-XSf1tLz5hVQLWhKQuio9V6IiW5PjoD-Lr0yb51BuRbWO32PALODq6oVWs043NxV13cv_uEBpBh1-tPNNXgGoLFxjdatPVztWXvKGzF3MoHHBt-266R1tX3EvUzgIOtIoQgKRyZUuXkwoFUNQyQ7jpqTl57PWwulgmnDLvHMVdwKkcA94unpinhzzY_BZpoaegJWYjN6hbwyM8cO3SwnaBTja2NU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو : ‏مشکل ایران انقلاب است. مشکل آن مقامات دولتی نیست که کت‌وشلوار پوشیده‌اند و در برنامه «میت د پرس» ظاهر می‌شوند و در رسانه‌های آمریکایی آزادانه حرف می‌زنند.
‏ما در مورد آن‌ها حرف نمی‌زنیم. کسانی که در ایران حرف آخر را می‌زنند، روحانیون رادیکال شیعه هستند که نگاهی آخرالزمانی به آینده دارند.
‏آن‌ها باور دارند وظیفه دینی‌شان این است که آخرین روزهای دنیا و آخرالزمان را به راه بیندازند. می‌دانم این حرف برای خیلی از بیننده‌ها شبیه فیلم به نظر می‌رسد.
‏اما واقعیت همین است. این هدف اعلام‌شده انقلاب آن‌هاست. چنین آدم‌هایی هرگز نباید سلاح هسته‌ای داشته باشند، چون از آن برای باج‌گیری از دنیا و کشتن مردم استفاده می‌کنند. این خطر غیرقابل‌قبول است.</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6775" target="_blank">📅 08:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6774">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jwB1YEA5LmfRgGTvf17ztda9aW9o5-XojJFX7lSYChqtuMtC6tEBSw2dQ2JDRr8jkykp60j0DEtK_oShf_mc3RIlnyu7a1seIKUOOE-Fvnvlg0Sqq1P_F61MxgrUPxgaugvfzaQD--88iFa4uZMRDwObJ_PtB7eNmdSpGIk0LBl10JFcQljMQSVqfwgn6PIabo2hvcwhx-pp8OUiBAcG6mY020tol7wvYHXO3vV77HXsSX777GTKEcHozj0BBZlWWoUp58RFk9yDmdswoZ_RiD__po7eVK56KDCTFOfRr3foqKGstv2uhKHY3hPfcA5QNq0HxTWB-MjgCp6dM11Tkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6774" target="_blank">📅 02:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6771">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Psf7TIUfH4c7gNOsPMuf1_xiPZF3O2z0rk1MrSsIBE6GTgE66MmyPdUBjKXQeZv2y3l_vdr1LXq7G9vUgSahniWA615LWEC3gOQg3Z-g_uinUYuMPzicJ8G7DInggQVTwYD4_oSNYSkRY6JODMikxTl4LHK4UhYSlP5hvInfOWGwNJnEGNUidIKsGxe92hPS0FhZAgfWtKDGAmByXzwibHIs1q2o4ApWJ73NmN0D7nb5LgrTQsajGkopU8v6pIdZVcpXOBcTkmpQfUqASQjFWmVSFbygWLT3Wn1Alq3DoTBQfP2l_N3VA_x0UNA7DRpn0vta0HyRFTQ4rkJMwkgsow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I9URhCaLN4qrufL3GVkM1IzHlU6AHciPzTCXoTrj1N6vuKfDLp7tbq2zahs7XLWDDS1ED0os4gH6vxTbYMuM1keTqHI_PP5Tp0kKTtcQvIB7HdIy_jXksa1iCfifsMgiJ-vsVpso8gLHlvTzKTmrfISZVy02FWjbGks8TjhiQk_bYFpux_TkvXAJPeOGtkBBV0pdvepClOeidYY0DJQ7VUSvWdmxX4K--6bc9_M21ja3Ai4Pd_CuYYk0NuSBCgijHUIYUQ1lkfXPT6LdMmd_0DmTFaTFAandJQ5aWpFxsUsyviscxQIUQJvbIh-eJptkV-CvPWzqrtKAZvEHDpc3rQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/895be358cd.mp4?token=AOY6hgM1sCS983AxiIUHHHH0cdTwKYfQRMTt4KKKpRk-vLBugyJIw7IDczzFfN12CNH4PBjiQjy7nL7hsuDHsXeXEKn-Yx7Kn1dzJ-ERROUhdwxpaiK60Zk0ozQHNHdLkjjNG7xzI5aGX8gBdI_zX9K0_vGWWgZKhXyk5TLleN_m8tvhJROwozK2ZyRvzxKvF0QYGSpY0A3_FU8oyh3bimkgRO8am6fYkGLNDgQeNFtoptoAA8SGaXvvvCBXs_Avx_TY6KtXEGFrcW4iYGVFVEz1cFm0hnwoIEOsaKLXwA4odXuDmNGLCK_jsUuRdsqsxJvHWwSd4EFQmCuZMdBlqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/895be358cd.mp4?token=AOY6hgM1sCS983AxiIUHHHH0cdTwKYfQRMTt4KKKpRk-vLBugyJIw7IDczzFfN12CNH4PBjiQjy7nL7hsuDHsXeXEKn-Yx7Kn1dzJ-ERROUhdwxpaiK60Zk0ozQHNHdLkjjNG7xzI5aGX8gBdI_zX9K0_vGWWgZKhXyk5TLleN_m8tvhJROwozK2ZyRvzxKvF0QYGSpY0A3_FU8oyh3bimkgRO8am6fYkGLNDgQeNFtoptoAA8SGaXvvvCBXs_Avx_TY6KtXEGFrcW4iYGVFVEz1cFm0hnwoIEOsaKLXwA4odXuDmNGLCK_jsUuRdsqsxJvHWwSd4EFQmCuZMdBlqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=gr7QmsWFhW46UrV72KjLb5JN7sSab9L1wzzExbmIX5oFML5P17hcP8DC4TMw2johmnB8yiUCMzvWvEh77Wppc531sv8K2lnmbbArojd3e6PawTrQ9knJt-F2GEa2n7koID7LrsJhWBQrLkoT4lZLeApvKDATkhqpmnZYc1SS-MDgf93xxlyU-oAFyzYJnFQf5VMcBypd2O0zdCtZKMG5-xwJFisRLlvBBtMPy-ldoEW_YPrd6S0MO-zth-MF5E-3s6x-nhtAqGBYsi3dkddUtpAT3RSjmZNC9DfXSnrWVD16iIfmb9hx5BOVJoCgqQeBXJU9pyI0EdN0boI7WeP2rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=gr7QmsWFhW46UrV72KjLb5JN7sSab9L1wzzExbmIX5oFML5P17hcP8DC4TMw2johmnB8yiUCMzvWvEh77Wppc531sv8K2lnmbbArojd3e6PawTrQ9knJt-F2GEa2n7koID7LrsJhWBQrLkoT4lZLeApvKDATkhqpmnZYc1SS-MDgf93xxlyU-oAFyzYJnFQf5VMcBypd2O0zdCtZKMG5-xwJFisRLlvBBtMPy-ldoEW_YPrd6S0MO-zth-MF5E-3s6x-nhtAqGBYsi3dkddUtpAT3RSjmZNC9DfXSnrWVD16iIfmb9hx5BOVJoCgqQeBXJU9pyI0EdN0boI7WeP2rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افتادن به التماس برای بازگشت به همون شرایط قبلی!  ترامپ ولی رد کرد!    احمدی مقدم چند روز پیش گفته بود به کشتی‌ها حمله کردیم - و تفاهم نامه نابود شد - چون میخواستیم چند میلیون بشکه نفت رو به قیمت بالاتر بفروشیم!  می‌د‌ونید که بخش عمده نفت ایران در دست گروه‌های…</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6770" target="_blank">📅 12:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6769">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pn1MEWSzDVwot9fdXJPtLrO-RlupRNUYk26OB_wQF81lJl-4Py1EDRmTNsXLLb3RVgjc4uwnH1JmmXqc4j2_GSHs7XFbthFEgSLa9f2x1SpyxJPNuOYBepqxY0IHB8aXOkxRAmSlXpxoBU-LGtp6dMB0Fdo_jobUlPDOYovMypkiocrTYKicK6camy5-NaNpIQHUSn0rYZn3k_8Yz3TgKxsIpTxsWppLp0fUkPoYZvMf0Bu-6s9PnggJ9GKtcAmPSAAk2J5brXfOGahKxI2UF2Fh7kWBQB3Rjl7zRXwceCK7eUseqiKi9ExQPyHJ7HuB7PDMeaivq9MVzfLzqW1LIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد  تا به دنیا فشار بیاره،  اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/6769" target="_blank">📅 12:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6768">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89284f5821.mp4?token=t29yll_G13ILpZDomxH76d70x-O2nTXa_l83wRJcAOfZQvFNeztOlhtP1hZoT4q5kJF8tVThtiXLkkVgz-hUfSLhxNxYrEkMhZ7PFsWpdMmXoeiHnl19VDfDUtnaVnEq5xtW747jVKCxavRlNkjqV5iRGtqiOKNNHeeg0BuWcfUHugPt7ufdhZKj7YjKCcPscVXIllzFAxeFP6B4kXQ5kbKkAh9oOvUeety2YsNA-A_c56jD9ndQcL4CqLv2LpNzGqEobnFTGJC-9F68DEWO9hhdh3vU6stkzqdtNVq2lS8WCWCN93Mu4N66Oi6U8IFL4cPpyIOAz4HxtZ8A4I57wTnaA6VuFwstHJjqsRk7KlsZPyjQbj2im701MDQ8H-VDUUT3hH5oGpZ2qwmUH8q4MfJ7FUIz-zGdCivhJ9jmNBZeZNch1kRd1XqxTY7GwnxyhPj0J69e5zXYOwJ3rlR90zbAFpsKkwLDYioL6OwVcIS9QyYGFEFCjpsXehWh5_RGxHWiZFozkhpAVnEo92UVQAoOyTPUVqLMbE-3wrSE5m6IZX0cCFM2x5QSu_iZdnuL14qSvKC6uvpLCCShgRHLygjzJAudmvxw4VdxHzPZyfPxL_vQ61qguR2UUGB--9K1Y2Atf3kUqdWow2OE140kqeWExL95iegN2CMH6alFvsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89284f5821.mp4?token=t29yll_G13ILpZDomxH76d70x-O2nTXa_l83wRJcAOfZQvFNeztOlhtP1hZoT4q5kJF8tVThtiXLkkVgz-hUfSLhxNxYrEkMhZ7PFsWpdMmXoeiHnl19VDfDUtnaVnEq5xtW747jVKCxavRlNkjqV5iRGtqiOKNNHeeg0BuWcfUHugPt7ufdhZKj7YjKCcPscVXIllzFAxeFP6B4kXQ5kbKkAh9oOvUeety2YsNA-A_c56jD9ndQcL4CqLv2LpNzGqEobnFTGJC-9F68DEWO9hhdh3vU6stkzqdtNVq2lS8WCWCN93Mu4N66Oi6U8IFL4cPpyIOAz4HxtZ8A4I57wTnaA6VuFwstHJjqsRk7KlsZPyjQbj2im701MDQ8H-VDUUT3hH5oGpZ2qwmUH8q4MfJ7FUIz-zGdCivhJ9jmNBZeZNch1kRd1XqxTY7GwnxyhPj0J69e5zXYOwJ3rlR90zbAFpsKkwLDYioL6OwVcIS9QyYGFEFCjpsXehWh5_RGxHWiZFozkhpAVnEo92UVQAoOyTPUVqLMbE-3wrSE5m6IZX0cCFM2x5QSu_iZdnuL14qSvKC6uvpLCCShgRHLygjzJAudmvxw4VdxHzPZyfPxL_vQ61qguR2UUGB--9K1Y2Atf3kUqdWow2OE140kqeWExL95iegN2CMH6alFvsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0493705c07.mp4?token=JIx-b9HchWwjvw48lFfA4en2L-HOud50qj-lw6fUYjchr0ojwZKvpU_20LU-49LoFZcuacpeEtIv0SgwUMa6oBnf59F81Iy37HyIoPSzYU1qDrgn-etyV9zTcKkyq08_2WXWJ6xDXPwwcPOeJ7LHTRoOnZI1BeAOvf6jTQaSSgXTgBHOBaVEQPm4sxFuCTxuAI8SZxXhxbjChArB0RSB36NxzWCTW2InHvLvrBN4Ct1eUKF23ZwLU1k96zxRtoVGCG8mmthCOZfCGnXdtC3VgYiY-gPOa9HEGLMz21G-1Uz7GDdtZnXYPiSIhN8w0n4hlNly2qi0ZxWk3nl9r4qFQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0493705c07.mp4?token=JIx-b9HchWwjvw48lFfA4en2L-HOud50qj-lw6fUYjchr0ojwZKvpU_20LU-49LoFZcuacpeEtIv0SgwUMa6oBnf59F81Iy37HyIoPSzYU1qDrgn-etyV9zTcKkyq08_2WXWJ6xDXPwwcPOeJ7LHTRoOnZI1BeAOvf6jTQaSSgXTgBHOBaVEQPm4sxFuCTxuAI8SZxXhxbjChArB0RSB36NxzWCTW2InHvLvrBN4Ct1eUKF23ZwLU1k96zxRtoVGCG8mmthCOZfCGnXdtC3VgYiY-gPOa9HEGLMz21G-1Uz7GDdtZnXYPiSIhN8w0n4hlNly2qi0ZxWk3nl9r4qFQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موج جدید پناهجویان و مهاجران افغان
به سوی مرزهای ایران</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/farahmand_alipour/6767" target="_blank">📅 17:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6766">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T90_TlVdmO7oNqlc5rKLda5CQl-J5OUHAUbWzze_noSYx97O3RSMeZEEiHV2V6kV64wcv7jC4IKReejaMlelRNN291Ts_Znz5V3-q_jGodvv8BuN-0Rv03OtncbSxR33T4GBILN4p4PNMfIgb_8BvUrInmuIyGyKr0t0Eo5PiybdKuaaIDzkcrBoPjywNSPfLjpT5KI0sg2J4aqowlKGdkj8R2NtOqjPTDIoYC5BSPLlS2WKHvgMdx3ueLbXaMS18UOIUAPWo-J5Iq9BPzHbG45M09wDkX4aiAbqlYJKoOV9-anpGwzH58rXCde6xYFbx82nPJ58vArWsnNd42iZLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو و این حرکت یادآور داستان‌های عهد عتیق است!  شجاعت و جسارت فرزندان داوود!  که در عین جوانی و نحیف و خرد بودن،  مصمم و بی‌هراس،   مستقیم به چهره دشمنان خود می‌نگرند!  مثل داوود، نوجوانی ظریف و آواز خوان!  خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه…</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6766" target="_blank">📅 15:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6765">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=kn8-S1oFYADl3yBlnBU8_i0Ic1IlZBhAcc7jB5UyC-ErsiIYah6SwJ0BCOxCssuE9OSt9QdNWaHhAUObMpaX8ROHsytAU0ccmY_SeGmtD7uvjMjKc0y4hWOZy4MTVQh_xCsbIS6AL6sjYtivOsLYPoVU7iocGrLWGijBwMgczh-VyY9Ew1quZnKLM3JGguheglzKVr5PX9pnuiYvB5D00hWfwuo8mth1f0ECI22PwcLLdgy5CdHVqgx0JZ_OPb3D-LIyAGMPuruBE9K3uJJaqkrlSDoaM25oEsRX-ylVkFXWohngTwI3o1q1ZKUTfkd_yQ4_TJ0cqsgwi62HCjjXhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=kn8-S1oFYADl3yBlnBU8_i0Ic1IlZBhAcc7jB5UyC-ErsiIYah6SwJ0BCOxCssuE9OSt9QdNWaHhAUObMpaX8ROHsytAU0ccmY_SeGmtD7uvjMjKc0y4hWOZy4MTVQh_xCsbIS6AL6sjYtivOsLYPoVU7iocGrLWGijBwMgczh-VyY9Ew1quZnKLM3JGguheglzKVr5PX9pnuiYvB5D00hWfwuo8mth1f0ECI22PwcLLdgy5CdHVqgx0JZ_OPb3D-LIyAGMPuruBE9K3uJJaqkrlSDoaM25oEsRX-ylVkFXWohngTwI3o1q1ZKUTfkd_yQ4_TJ0cqsgwi62HCjjXhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q-IkbUxI0DKQuiuEgTOec8yfj5zkJgpMJPmBxPPioT4M3ViT8QG_Yl1d0rU5GA2awgheaJ7Z_azbJpSqnw-tB5SZZl31LFiXkTL5j5RRV2vfOnCyJfVmMZHY5AVbqEzXrkLA03NzIvrSf4OASFnhUgKYa_JKX6RsDj4GKHkVOo_FVo9hj-yT2Up9cPA7StCwRE2Efky4YxPuel_WEXemi24QE6aAKKQvH96ofeuvmiDEGuL4OkQ7S_9T43X8E9kbbRiCARzHi7M4UmDsmP6SCuS6UEmrTZuARbawlMJMaqFOl-iNDFScDf8RiX_TAYUvBYujKJ5CoBZFXVqGEKe2YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.  . این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،  و نقش میانجی‌گری این کشور. (وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،…</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6764" target="_blank">📅 14:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6763">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ahLXsr57AOiYkp1ewbzSFxgTv87KwIn0sUOiz_sVwBtE8f7osX3aoc8t4uSJmO08DMH9DwsJV8lg8fn82mqXNjM0v4IIzhtH1MBAzK6vsSX7pMMqGNQ4aLEr5UN_evnCvjejhBYeg3j5wgODBIQB8RivXp1DLcuf67yOyjmBPfsErtL9VpRwGLDMHCkPiPVoXr9k7p8d7fFAfsuXa32WpBVNVCugGp2RZrDMI4hqUp2n5xwNl2L2X6dfj6iqGLxO_9YqsyNhZQXuZWa4XdPx1YdWV8gVPIHF_sZraMSz1XI0Fjk92Acd-TXk1-MAezZz_V-7D1iW23Cg9DtrqKDChQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=dHXMXXvsK5XEMYI5_gg7TVs22Jn1j3zMeieP9YEUkOV0hZz2R7Tn4wHuJd91DgJUMjWdokXdRvaLCVHndggl5u6QGkfs3y-MJr4QRDkCxxHqI09GT2zkwRml0GJzpfr1u9C9Duvu_XS_YPn7BRme6N-tlu5jLRR1WKmzMmkpSPNtTXXd35aoZ2hwfc0FMnX6R4BmVimfXJgvrp4skHXn56uWFtE8cv9AyhJFZDgn6fet-YWTYKmHLq03suJKhcgjOArv95NHAF4zxfXq526_ZmOznEAMAVWSVfbHWvszGI-nXIFer5iX2pxLxDaev34PFMsyq3iAqRZ5xi6hlM9Mq6P9hyknaZO-TexpIEkmp65KXuFu6tifjj9QbXS0xw6BqxlCgHWHxbQj-tqjWsKXXx1Uux6wbZ9_Qf-8WMVzQWQvFB7hkZaApNg88F7-XE77M5dCQujqGecJb_wLE6p2nBnFJv2OsMgCqALdI7dx4J-Z4ryEvxYpu2SO4vTUUN_aZnLzBzofyPvg1yC51of_WAIFHCJNFgZf1zLP6GS2jWORlL48wszzxFEcSCYyCRDSZml2OpIrGd_AgH9KkiuujZnBVrsZNcWj4xDr_DP1nNKtAwuDIPNB_cg4oPW_ViQqqsA0Nln0QG20uzmsIsQeRZB9CGDUKDKV7c5hA9I7vPk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=dHXMXXvsK5XEMYI5_gg7TVs22Jn1j3zMeieP9YEUkOV0hZz2R7Tn4wHuJd91DgJUMjWdokXdRvaLCVHndggl5u6QGkfs3y-MJr4QRDkCxxHqI09GT2zkwRml0GJzpfr1u9C9Duvu_XS_YPn7BRme6N-tlu5jLRR1WKmzMmkpSPNtTXXd35aoZ2hwfc0FMnX6R4BmVimfXJgvrp4skHXn56uWFtE8cv9AyhJFZDgn6fet-YWTYKmHLq03suJKhcgjOArv95NHAF4zxfXq526_ZmOznEAMAVWSVfbHWvszGI-nXIFer5iX2pxLxDaev34PFMsyq3iAqRZ5xi6hlM9Mq6P9hyknaZO-TexpIEkmp65KXuFu6tifjj9QbXS0xw6BqxlCgHWHxbQj-tqjWsKXXx1Uux6wbZ9_Qf-8WMVzQWQvFB7hkZaApNg88F7-XE77M5dCQujqGecJb_wLE6p2nBnFJv2OsMgCqALdI7dx4J-Z4ryEvxYpu2SO4vTUUN_aZnLzBzofyPvg1yC51of_WAIFHCJNFgZf1zLP6GS2jWORlL48wszzxFEcSCYyCRDSZml2OpIrGd_AgH9KkiuujZnBVrsZNcWj4xDr_DP1nNKtAwuDIPNB_cg4oPW_ViQqqsA0Nln0QG20uzmsIsQeRZB9CGDUKDKV7c5hA9I7vPk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترکمنستان، آذربایجان ، گرجستان و
امارات و تا حدودی عراق،  آسمان خود را
بر روی پروازهای ایران بسته‌اند.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6761" target="_blank">📅 14:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6760">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLT289F9WmO3S_6W2H7hFM3aowTeP71Qa1wlk6BRnlgPFS2YCo_yYfVpC41EGTtr2QQqLe4823TI7GtyhThjPybnf1Z5Fb0hRVn0rNd9uWMcso_C65PmDhMRcgf8Otj-wfk-Su42VFqkcPkz1qcZbGdSspI-bP1dy1HmSbJ16NvFMvVpoS1-PQjhmOjZ8QoR7YQZ7urEf3qD4JX18FA-NChzlIpv3gEB5iVgopwQS8-Gg-wYCuOt-yn_5WvTHwCcRRHXDVmWUg5S0DyPPtvkjQExXs6SUChAdHNcJi8B29xsY3fGPoCsQ_JDIb-E7kk6ppk6970T2cA6CDi6JVzS1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6760" target="_blank">📅 00:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R5rkSmzrDvy4VXOiD6p-uoakrOtPddfmqZBBOUwJ6DuchnkwYol6gXNF0DGo5hzYcQTsp7BMwi62lkU_exgTQBD8vBHygxK7HBybUVJvgG8m_DtzATQfUXAdW15J8FUHmei0JDCd-O_BrRLZxEG-0rKKMZFcOXdLOC2xTMmVfJDhLGQ0LhvOzjdS7cT6aBr17Vtsgl3QULBz5mwGlmiFd8WA5gGixJGXC9AXhf2kyR5ElBu5Ddi6ldVBix6FWdGYxeaXSgqmbFCx8f0RsnQPdFipsd6YNh82I37h6GsOmRgwgfg7B24__YUuoV7lNnKCBc5_0Qd2nugwvE-CNx4OMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مهدی حبیبی؛ دبیر کانون امام الرحمه:
پزشکیان باید تو نیویورک با دستای خالی به ترامپ حمله کنه و اون رو توی سازمان ملل خفه کنه تا انتقام خون رهبر شهید رو بگیره.</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/farahmand_alipour/6759" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6758">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=HxIr_CnFB3lkMTCdGGtx-AvxUmCb4Dxkm1taJ1QrQhDxp-nqc1IlisKjjeLQoS-ObK4RS5OGG5O7Pk2YOsymYCqn-XQZTr6hPH51Tsz75ubpruj0b2viti6KsiaV1IPp0znikiqXpP5AZvcGXCBwDO179y5EzxTTRhQmNKSlnitmuDOe07Ghf6FlKHlV-FYZTrLG4egyj_iSc9cdVO69VBAuUX7IM_q4EOojgkt2NlREhUzDWHPS0PO11lsio8nl-OCxvZs8It0lKpiVdOgvPdHheCw8FQZUR39OK__uw7UNqLw6fg-vnBZOLy9rpKPGvQmTU5BOnd_e1LA22yrs6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=HxIr_CnFB3lkMTCdGGtx-AvxUmCb4Dxkm1taJ1QrQhDxp-nqc1IlisKjjeLQoS-ObK4RS5OGG5O7Pk2YOsymYCqn-XQZTr6hPH51Tsz75ubpruj0b2viti6KsiaV1IPp0znikiqXpP5AZvcGXCBwDO179y5EzxTTRhQmNKSlnitmuDOe07Ghf6FlKHlV-FYZTrLG4egyj_iSc9cdVO69VBAuUX7IM_q4EOojgkt2NlREhUzDWHPS0PO11lsio8nl-OCxvZs8It0lKpiVdOgvPdHheCw8FQZUR39OK__uw7UNqLw6fg-vnBZOLy9rpKPGvQmTU5BOnd_e1LA22yrs6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در دوره «جاهلیت» سطح موفقیت خدیجه
چنان بود که کاروان‌ تجارت خدیجه، به تنهایی،
با کاروان تمامی بازرگانان مکه برابری می‌کرد!
اسلام - ظاهرا - ایشون رو به جایگاهی رسوند
که به گرسنگی افتاد و خوردن چرم کمربند.
حالا شما میگید جمهوری اسلامی
ایران با اینهمه نفت و سرمایه رو فقیر کرد.
این چیزها ظاهرا ریشه داره!</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/farahmand_alipour/6758" target="_blank">📅 16:27 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6757">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=mWXr9BS7RVGI4mJPcQB6PxjmjAsF7w0-HOa0iFDZgI3YbQ6sxNGWW1qzA6Bxd3hIN2k9NFsZpWjqj7soD_GuLSfO8f7jtKYJIca9p_VEGBCSU0Fbc11DWFXU2dj9ijS7B6j2QCCwzNV9y7268dy4S_pskUQK1chEkUuPlfdKl97pkpbuix_kF5k7B_H0xge70Cn5uC-sVF0fTwxgJpPwdrmS8nm8ARHaBkPMRPkAKjsSyft7RpQKlDrCKMKXrMyQBwFIG7BKwJDUw2Rq3LUklgIj-LgWbJwhMCE6FUBlUlukncVaacw5U8panQIKVuXkaZR3Bs8z6eshtf_Q1gneZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=mWXr9BS7RVGI4mJPcQB6PxjmjAsF7w0-HOa0iFDZgI3YbQ6sxNGWW1qzA6Bxd3hIN2k9NFsZpWjqj7soD_GuLSfO8f7jtKYJIca9p_VEGBCSU0Fbc11DWFXU2dj9ijS7B6j2QCCwzNV9y7268dy4S_pskUQK1chEkUuPlfdKl97pkpbuix_kF5k7B_H0xge70Cn5uC-sVF0fTwxgJpPwdrmS8nm8ARHaBkPMRPkAKjsSyft7RpQKlDrCKMKXrMyQBwFIG7BKwJDUw2Rq3LUklgIj-LgWbJwhMCE6FUBlUlukncVaacw5U8panQIKVuXkaZR3Bs8z6eshtf_Q1gneZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=O3YfAwMOo5uaqSn9l2P-l6zU4yOAJXgLDKn2IQU8kxuqm6qaCLnhuKpGB92_tNzcyt6Nh8uuHdDB0kCcNRr5YXTG2WOr3rEUNkPbHKh-6s0J0x1zOhGU1G5pD7uYOuGA9kzMTKvwOcFPGh5S3jGBXZlHWZ92Dk9J5kefvp0U0dRmeT5A3fX-1pAPaR5QLH87q_Zak_T21xZfbC6pWKpwmvcUQiIoMXXwS9nNriKEc4zM_e-gu7FPQmx6_YXcwha4i6qBoYFGzpt5gzwLo0cuJw1s1x44jQWtqJNmCNs1Qciy7CQXxh6nGTtHutxun2sGvE_u7gjzLU5DcevCvcKAKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=O3YfAwMOo5uaqSn9l2P-l6zU4yOAJXgLDKn2IQU8kxuqm6qaCLnhuKpGB92_tNzcyt6Nh8uuHdDB0kCcNRr5YXTG2WOr3rEUNkPbHKh-6s0J0x1zOhGU1G5pD7uYOuGA9kzMTKvwOcFPGh5S3jGBXZlHWZ92Dk9J5kefvp0U0dRmeT5A3fX-1pAPaR5QLH87q_Zak_T21xZfbC6pWKpwmvcUQiIoMXXwS9nNriKEc4zM_e-gu7FPQmx6_YXcwha4i6qBoYFGzpt5gzwLo0cuJw1s1x44jQWtqJNmCNs1Qciy7CQXxh6nGTtHutxun2sGvE_u7gjzLU5DcevCvcKAKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IqT_teztgGOb6WlF0TCFUSNq3kUTxPDOfyUvP0g5VHTd8U1H9sE3t9W1fDrcAHmLb3QV0jerL7ByTIH6tc-6m8Y-PrdMhy-adals1TKeYH7ivxFC08mo7o3tre2rBpwTJ2wWvXgz9S0hMdtcwkeunXquLgdTfo1XryI7SK3aqFSdWzOlQbdH7GST_yXh0xyauSPDa7QHqa2u9YYNW1iEomlcuOwXvjWWo_LWBWd1iV6XRC-BuDfswt_PLzzlkm9q0rlTlgEYTSVbGLdMc2X-d-YgaIwm5xLboK12pFkINu-lO3DiQyaZNMbfHCVfHphc4F7iLZKjoU3lhEJ2RjinJQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8DAdDnYBR92YfS7eOwR8kYn9SXksgG3pBd6tR-uUJ3pimDkXvDrH-pdrfkmo9ODXY8nBwjX1OBhKsu5JNcPvp_9HFgHZ2OWLQQ0d6mhjvt0naHbTlPEgFO9NmIKW-o8PFsM4SoWE2fA7ZkXpDNteAoXfCIf18qv-BQrUYwl1mNlzZChIbEgMKxujQoxlDI10sAdZd-EEWjLUETXLn-Rd2aHwUQUd8Mh5Ve4WxDgyh2AunCTj37NUmrTawf4CnI04t5Z6OhlX9zw_AK08dEq8FSdfC8H8-ykuS6iI4EHtNg_FcrjaAf-oYUC-CG1ndVf1-EHzpDmc3E4rpJc1WEiFCsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8DAdDnYBR92YfS7eOwR8kYn9SXksgG3pBd6tR-uUJ3pimDkXvDrH-pdrfkmo9ODXY8nBwjX1OBhKsu5JNcPvp_9HFgHZ2OWLQQ0d6mhjvt0naHbTlPEgFO9NmIKW-o8PFsM4SoWE2fA7ZkXpDNteAoXfCIf18qv-BQrUYwl1mNlzZChIbEgMKxujQoxlDI10sAdZd-EEWjLUETXLn-Rd2aHwUQUd8Mh5Ve4WxDgyh2AunCTj37NUmrTawf4CnI04t5Z6OhlX9zw_AK08dEq8FSdfC8H8-ykuS6iI4EHtNg_FcrjaAf-oYUC-CG1ndVf1-EHzpDmc3E4rpJc1WEiFCsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/67af3237af.mp4?token=CTsZFth2LhXz51G6Md3lhVcMHdjMx2I1jOQuNuw9eR9mHcShh0OcvsmpWp5pl3RUYMv6ik6T-to2-ar_gABUxyPl5lxFvJ_F_CE0WDVXfkjCYWaXt0ESKkN8n7M-N7Y2G-6fQQPy9IyD6Zh4q1BFYWzxNycDvl-3s0QsYFYNQctZnBMz3LrfeS7YgnTpNO46ahxDfGCC84jhxVcVhi06rWX5oYzaHubVHPBRV0_ohCS1tX-TCP99eWECLCm-NR_zI9DjaTeDCVNL3VoAmmiLuziC9IrejzEf4nJOn-6qGdePkAcLYI7Ls_aeK6TQbMh1iRaxpYJNzD0PoDK25jJA1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67af3237af.mp4?token=CTsZFth2LhXz51G6Md3lhVcMHdjMx2I1jOQuNuw9eR9mHcShh0OcvsmpWp5pl3RUYMv6ik6T-to2-ar_gABUxyPl5lxFvJ_F_CE0WDVXfkjCYWaXt0ESKkN8n7M-N7Y2G-6fQQPy9IyD6Zh4q1BFYWzxNycDvl-3s0QsYFYNQctZnBMz3LrfeS7YgnTpNO46ahxDfGCC84jhxVcVhi06rWX5oYzaHubVHPBRV0_ohCS1tX-TCP99eWECLCm-NR_zI9DjaTeDCVNL3VoAmmiLuziC9IrejzEf4nJOn-6qGdePkAcLYI7Ls_aeK6TQbMh1iRaxpYJNzD0PoDK25jJA1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم تعرض به کودک در کلانتری
نیروی انتظامی جمهوری اسلامی آینه تمام قد نظامشه، وحشی و عقب افتاده و‌ خشن.</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mjnuhVfJ4TobtqGrwAag3E19GA7PXoHIyxZIqjKLgokHLQro2DR8xLEaHfMyrUzcY6kOw3UgVNCDYloOVrNn6wRuBXj7HkYxnGI6pHyF-N5cWEChtcBwjhiIaMC48hdGpHf98ke_XQFKe9drmt1m6mttKCITI0NBbnELlTCcbThuUbCW0k25TVk5N72_Yj4ptYEVD8fC9CQ-jsxPPNxuaorqfkbjaRGoMqQQ7g-eoc7YUnc_1pHYDMnM-uLaZV1Xe9MIpG_A96DyzdZ-LfpZLVcKHIb3WyKCak2YhUhVjKm1nvkYtt9Udoqd7c2JekDHWmjN5J4EwRQH2drgMHDH8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=rKuTL-WdCe4B-ELwoxdOvhGRz5N9pXCqQp5-JfvJdZzd-vHoCz62z7aohVYJ4TcKAFHRkMBe9VKkQsyNURO9TvoJQr4PoeJpqJLH9OcxtTwpeIeI8CUYa5hGaFiln_5haGta9xGsiLwcJ0900gUpMFcYLAc4hy2JoF9dG6jfYN0aLqD3AIOFP24jCtdQAGzLTZidJXFEVJysAIDAV24laBKzpgtYgLUeKRAP3scuicBMRK1YB8U-q0lGilfX13wGcW0WYln9e-uetf6D3_xg1E0imfV2Duy6WYNRbXU3-YBf1X06vW4yNXljXiDphya-wMZFRxpfbJRqbtVvp_9cXqnRKqvB_W7-82kL577Zsm0WQ4lClDyaFXOz83UaErJKKu9ZVMIQweIWogupV5mAO7euL3HiJuFI0BA5Nf4jmZhxTVvI-3HWaNk70vlWLLATGThclAV9364zn5AqyrAKPQR7T_Tb2iN4Kwj8eSEjTqLJVhyjVncvp1oUxlkfRUDK3lAU6LLizHT4T6owFuQcbMEya_KofWrb311uzteVP4bQYgL7SvJJVC96Cp5aKnkLxt2lZ7sVSurLzFgm7Gv67tmnDVEbKaW0tnsbMh_Hb9bgfDPAI-WIaJT1z6I-m_s-FT_qI6pGDczBPrMfukAPFQt6gydJWVhIw_03sduqB5E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=rKuTL-WdCe4B-ELwoxdOvhGRz5N9pXCqQp5-JfvJdZzd-vHoCz62z7aohVYJ4TcKAFHRkMBe9VKkQsyNURO9TvoJQr4PoeJpqJLH9OcxtTwpeIeI8CUYa5hGaFiln_5haGta9xGsiLwcJ0900gUpMFcYLAc4hy2JoF9dG6jfYN0aLqD3AIOFP24jCtdQAGzLTZidJXFEVJysAIDAV24laBKzpgtYgLUeKRAP3scuicBMRK1YB8U-q0lGilfX13wGcW0WYln9e-uetf6D3_xg1E0imfV2Duy6WYNRbXU3-YBf1X06vW4yNXljXiDphya-wMZFRxpfbJRqbtVvp_9cXqnRKqvB_W7-82kL577Zsm0WQ4lClDyaFXOz83UaErJKKu9ZVMIQweIWogupV5mAO7euL3HiJuFI0BA5Nf4jmZhxTVvI-3HWaNk70vlWLLATGThclAV9364zn5AqyrAKPQR7T_Tb2iN4Kwj8eSEjTqLJVhyjVncvp1oUxlkfRUDK3lAU6LLizHT4T6owFuQcbMEya_KofWrb311uzteVP4bQYgL7SvJJVC96Cp5aKnkLxt2lZ7sVSurLzFgm7Gv67tmnDVEbKaW0tnsbMh_Hb9bgfDPAI-WIaJT1z6I-m_s-FT_qI6pGDczBPrMfukAPFQt6gydJWVhIw_03sduqB5E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tCHcR9cL9mIuy5Kb1ZhYqXWUqVQyymbKTFWfHCQFF3hV8WLSBpVXBHk3qqJA53APbXVcfXtD0vtFdpBZotaGqiTUBUX3vEPW33k2FWLBT-vmGIzNXcNMg-SrCwQXB5G5R4AqIbzwM3PCT3tHs-3DW6g--FYi8q3ZquMYySixoONIcTt8vElgFXxTRFrRO93bYlSNqUbYIYvTa8F0EfciwcphofOj7ylbwSNYlf8vSBeGD3IZw7XnBI7hc9YbLIJpK32KfQgvLiZC6H6beSpMjGtd2xfzHmDWFQyEUQBLtl2AFR64t5cwW0RXjhky1xm_7ijQAhuxlUZnbBVpR8Jmfw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=pxWdGM0m7FwW9NA-8fXNCX7qYqdbbhI5JuDbgG7E1e4qn_qBQT5EMSyWy2o_bhGXOLSW1QPOiLiqPGcOp1Ztc9n3-k6J3P6PVawl09qhxNiEc-PYFPj9mZOJXLOUR0fNA27zV06TxrACYdIXa8Y0akqJ6PZYWj8U5oKGBglCotEmiMFcGQIWgLCjxzyQZ7jDdNjWUAqATQXNZhfM-mL4tybqKgq3eR-GzHyelJTWB15NiuBftiAonTcFixPnIGfHLdJHBNMB5eM1HlY9oAsmTsDbQeacOk2hIDio-aY3-cmgvc5-MP5XV6tDrJbo6jjQXZRZbfgPuPNfh2cHLwy5fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=pxWdGM0m7FwW9NA-8fXNCX7qYqdbbhI5JuDbgG7E1e4qn_qBQT5EMSyWy2o_bhGXOLSW1QPOiLiqPGcOp1Ztc9n3-k6J3P6PVawl09qhxNiEc-PYFPj9mZOJXLOUR0fNA27zV06TxrACYdIXa8Y0akqJ6PZYWj8U5oKGBglCotEmiMFcGQIWgLCjxzyQZ7jDdNjWUAqATQXNZhfM-mL4tybqKgq3eR-GzHyelJTWB15NiuBftiAonTcFixPnIGfHLdJHBNMB5eM1HlY9oAsmTsDbQeacOk2hIDio-aY3-cmgvc5-MP5XV6tDrJbo6jjQXZRZbfgPuPNfh2cHLwy5fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QFZIyDDIymazJjIWHxu2UA1GgKfPidHJndby2S3sUResQ5YZqdtPqbSjUO2eQSFSFjLXQ5IzQusWwk1fIhGY8vzXc2UY_tn9PxCc6rtqfcYumLlQzGm5G2DUHvsGF5aNGGzhabZ89ylOqDw0ImPExseEodVqpoZQ0NxO-nHWa_jQyyUe5TYmuhRuLJ-GpDaMBB5O5DdyHdxQNr7FXrWRzNZeiO0U2UiC-33bWBoubNfUy4nad5M8EFR5w0Pt3AajY5QpOyPnRorfHiFFNhgVBND73Ef9LP8tFi58BgBoxabD0hfx-DmZPhJ0WmgqeqBQD75VecT1wn_bn-3h3ZcA8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Po7eGRjAA_hPNoRQw07FngfAhP_EdKZ47DyIUSn--AQIk27YtSOkz9yGdFpytToNdrCR54TAE-3rXXKQqD3oR9qEAWZQxXvglhRLGvq342SQC3GWM2fBDTDuBfnM6UIiF-KCKTfRzz2fc3EU4582u1Erhi9WTlAifWcJdEW93gFvkmw5ASfJ6jRAS4bSzpATRKvkeXKr_XuOigAT8BIY_1xFgy_0qA_FGlJ0scPbclnIhu8jsMYTSKWRsH0p8ndfckNlAUqjCrSCVpc9CvknQ9o5b8uwyMAK-4SKG_ynckBcO9F0uIYLXPpUO9lUXtxGxP3ZEVygshiYoFR9WoBURw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bGAbFjebLAPMtOCU2651l_Nx2KjIdKGHQ9_gPpK4FG3MzbWNUAMWvLBS0je0haBTr0ip25Jq8dH-ATEGEO6wTyv2B11fGN0TFjKxMED46LYkE5RUVFoZ2FJjIIQUknFVH4ap3y74n0LmSi-wMD56ztY7ZM94pbcqra10asxVgyMoW2WskyTgFyBg_vODp7BKJgSpXPY9UnHGFsqnLEZVkuOLjrU6DxkmP_1ZlaUBOkvXxT7_rf9I62H1Q7Dy4xzTN0tEYrFSKUZgZnAtBWwXT5zg6VUKso3AnHmW4Sf63j6nHlCtzsldl73sZHZXwgzGj9O9RFfs19zmH5NOOFUAXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=dg_HEPjmwofBtImSJAIRhaTWfE9n_hTg6OpPzEC7PuJfDZC4SPMfgzmQCc-wUJvu_2fjAP-ACcSnieatyAIO5Hv8ALN3yv1s4IBjtjv8LLhpEKGqiyEakGSgccqpEuZ6MWDjHGOXn6O9AgSGi60SpAI1JQkbEiSBak8ag5nXohSYptVZUS-sr17SSGzIWgPI9nCRUX2hvyQ3NqUY4twZWaEVD4ViLUD0W2CAsB9OdrCT5srwY-hcwZD-Cs_TB03emM3WoQHx5RNOMD-dKnQBwScKRvHnxTbIdO3drArwj3Y3vLb9sLTGVVOPKqUTzeL1LVfKWy_Qk6D8a7xEZ0UxCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=dg_HEPjmwofBtImSJAIRhaTWfE9n_hTg6OpPzEC7PuJfDZC4SPMfgzmQCc-wUJvu_2fjAP-ACcSnieatyAIO5Hv8ALN3yv1s4IBjtjv8LLhpEKGqiyEakGSgccqpEuZ6MWDjHGOXn6O9AgSGi60SpAI1JQkbEiSBak8ag5nXohSYptVZUS-sr17SSGzIWgPI9nCRUX2hvyQ3NqUY4twZWaEVD4ViLUD0W2CAsB9OdrCT5srwY-hcwZD-Cs_TB03emM3WoQHx5RNOMD-dKnQBwScKRvHnxTbIdO3drArwj3Y3vLb9sLTGVVOPKqUTzeL1LVfKWy_Qk6D8a7xEZ0UxCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه
مهم اینه دلت با خدا باشه!
علی علی!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C8AEKUazuIvHTQ0EgZmCvQqSn_hLRNrBDUjHi0vU1gQf6T4SxXvtGeHIN-_2w_BH3ROJzl5a7dTesTQocfOwWlpQwp4nfuziL0pJgRhDhVqcUOszD3xCYUCFivQ5f8jaT0pniLbKbc9y9cmfbR0HJPGC0f1G2UhPM2K3HiLtLK9hiQRbbl3sRyESigmWIWr7N-AL2BGL6wTLxOtW8XfF5WowcTzHMpHTvj3u6uWTgM9b77jR5E1lw9IGI8cT2AVu6zL_1JeNnWvIeySUYAbAfvnNshfK7CDv-YzVD4UId9OhQIOIHoJ3FH3RT38EowRTjBE6sQXf93uZbXzv1_fbPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=lnnAWgSVv-mfQZiAmpJi6zFNLr_yJrSwEbJ2z6_cX2dbw6nplsbZwjnTSh_3CXiC_kIM_FQeDlSREYZiTnrJ3jhqMUNBoYJrunSCAfZs9P-kD21c8NSjqK95t60Qm2smKQkWi4IQPdS_TPtEtwFFI9F51yarrrh0csVC3k7_06PZ0amT1gr620rUK9qlQu9daa-d75VpiZ0sZ1VM1OapcNXnMEqgNL7h62SeCWCKiOpxq70uIeDQXFxkbf9JWOCf8NkOY3s5Ji3OHZ77Ssi2OjFVjex-G4hIFTDXAsINJXsOPDkDRvWGSOvMhdgoGbUbc8AUGCTkYdjaFXWvbTBfFKrbhLmBl3iNWPQat17b8MQs8Ujvf3Rnzvx6CUnbqbs62CbBCXlFbuprCAbwphWnWOS-WdGVENAvFHuCkIonltwd-9w5oH9eXWdtC3yJrWVKjFG3z1yRTV3h_2WHomrY7cLSvSf8csarQgiFjnV3Mb2RKO8lngANR4jn5BgcTVwB-eP0c8kpHopeKSLfrfx093x26NGZLO_qcPAY9TcxngEk7DyDcXVmRVz8_bsvK6SFNOKiUbThat4Zjr_uDrooP3GqVhd67fyeKumuJsUBusMxLuWsoHTugtxtCZXYG_EDlXCVy_uQD134M5SU0YTEHXfIA4Mmdc7cY95vDc9o-E4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=lnnAWgSVv-mfQZiAmpJi6zFNLr_yJrSwEbJ2z6_cX2dbw6nplsbZwjnTSh_3CXiC_kIM_FQeDlSREYZiTnrJ3jhqMUNBoYJrunSCAfZs9P-kD21c8NSjqK95t60Qm2smKQkWi4IQPdS_TPtEtwFFI9F51yarrrh0csVC3k7_06PZ0amT1gr620rUK9qlQu9daa-d75VpiZ0sZ1VM1OapcNXnMEqgNL7h62SeCWCKiOpxq70uIeDQXFxkbf9JWOCf8NkOY3s5Ji3OHZ77Ssi2OjFVjex-G4hIFTDXAsINJXsOPDkDRvWGSOvMhdgoGbUbc8AUGCTkYdjaFXWvbTBfFKrbhLmBl3iNWPQat17b8MQs8Ujvf3Rnzvx6CUnbqbs62CbBCXlFbuprCAbwphWnWOS-WdGVENAvFHuCkIonltwd-9w5oH9eXWdtC3yJrWVKjFG3z1yRTV3h_2WHomrY7cLSvSf8csarQgiFjnV3Mb2RKO8lngANR4jn5BgcTVwB-eP0c8kpHopeKSLfrfx093x26NGZLO_qcPAY9TcxngEk7DyDcXVmRVz8_bsvK6SFNOKiUbThat4Zjr_uDrooP3GqVhd67fyeKumuJsUBusMxLuWsoHTugtxtCZXYG_EDlXCVy_uQD134M5SU0YTEHXfIA4Mmdc7cY95vDc9o-E4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=Zr2dILucWP1ecS396kvH1AQ-1D38TaKDhA_OJL99E96-R8kAuIt9gCEch8CUd6WlveHK0ykuaOfi4MqnB8CLKzZLKSRbe-v98LWZfw40eQO8YCxIlYkL7o8tYyyf237f7V-_GS0KelhLfbDrNfDzlJyLN7_bqtDRhUOaywmT49Us5fb_KMIuZD2-R-aF1_QOYiqGKOwdiw9GmXgo0TSunDr_JUd_dnzhPrQLx3xltCP_JznebdkHkSryjE6vI-nToUPjtdVOQmrzOFec2QSIquVVJndv0-NVJub5lxErPCLP5NvPLtgBvqp9laOybBUhsNWEpL22yyj6AyxqYZIjMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=Zr2dILucWP1ecS396kvH1AQ-1D38TaKDhA_OJL99E96-R8kAuIt9gCEch8CUd6WlveHK0ykuaOfi4MqnB8CLKzZLKSRbe-v98LWZfw40eQO8YCxIlYkL7o8tYyyf237f7V-_GS0KelhLfbDrNfDzlJyLN7_bqtDRhUOaywmT49Us5fb_KMIuZD2-R-aF1_QOYiqGKOwdiw9GmXgo0TSunDr_JUd_dnzhPrQLx3xltCP_JznebdkHkSryjE6vI-nToUPjtdVOQmrzOFec2QSIquVVJndv0-NVJub5lxErPCLP5NvPLtgBvqp9laOybBUhsNWEpL22yyj6AyxqYZIjMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=PxTGu4L8ciBbsQiy25Pz4RJ--jSxP5ZDFDFtswPhXree3cRPEx0dDMFNBDLawKU1YTvkPf9RtTKEB5h7v5uH9h6SLn0ycNFF3OyV4Jbp4SYyn7txePvZSCv7dVhoAXoD29tHAQuLytvfLAwT-7m4XNxGPpF4BYHfs8DvnvyF4aptiLKH9vnF5ITN9pvYXjBwhsXEKwiCOfXzqNTdPwvA-DbiFTG7mOqrGTtAiMaSXgdmBIYI2NwU98Sp8su9KpTgGcmXAxts6xj-ceR2jimdO0tx5oUw2sfxc4a4E7hoJyGQ9zQeMsww0A0ONB9IqOwBpOg4nIvzP1g2VxaxGR8cRoyv4lYiS6ElAtjHPEF7a1EjaFpmBZ-VaydEjcWQCO-3t215m5qMup6Z-dzS6Ylh4hSabkW0yrhgFr627HQPAB0RlpcEsqNd2-FS14hOyn5VYoZvgpeliWVh7TsD1_LCf9x78rScAit-IwCa5ik7onWV7LfMD6TghIMpS-Ve925j83flhX_RtYAK1G2i2ehVc9PdAOjOX-wP2SSiHVLwqSbW6u3Rn2xXTkgb6OsLACBsQ2TiycFdc0iwgiMofRb3Z-s3ktkpil6JNIGVuu56noJ81E0kwabPiCOeSjVZePeCa_LfQKY3jWlb5Vj1sXqny5F7DR8quaagjGlAfRqQADo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=PxTGu4L8ciBbsQiy25Pz4RJ--jSxP5ZDFDFtswPhXree3cRPEx0dDMFNBDLawKU1YTvkPf9RtTKEB5h7v5uH9h6SLn0ycNFF3OyV4Jbp4SYyn7txePvZSCv7dVhoAXoD29tHAQuLytvfLAwT-7m4XNxGPpF4BYHfs8DvnvyF4aptiLKH9vnF5ITN9pvYXjBwhsXEKwiCOfXzqNTdPwvA-DbiFTG7mOqrGTtAiMaSXgdmBIYI2NwU98Sp8su9KpTgGcmXAxts6xj-ceR2jimdO0tx5oUw2sfxc4a4E7hoJyGQ9zQeMsww0A0ONB9IqOwBpOg4nIvzP1g2VxaxGR8cRoyv4lYiS6ElAtjHPEF7a1EjaFpmBZ-VaydEjcWQCO-3t215m5qMup6Z-dzS6Ylh4hSabkW0yrhgFr627HQPAB0RlpcEsqNd2-FS14hOyn5VYoZvgpeliWVh7TsD1_LCf9x78rScAit-IwCa5ik7onWV7LfMD6TghIMpS-Ve925j83flhX_RtYAK1G2i2ehVc9PdAOjOX-wP2SSiHVLwqSbW6u3Rn2xXTkgb6OsLACBsQ2TiycFdc0iwgiMofRb3Z-s3ktkpil6JNIGVuu56noJ81E0kwabPiCOeSjVZePeCa_LfQKY3jWlb5Vj1sXqny5F7DR8quaagjGlAfRqQADo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=F2J5LTnf90U2HD_uXEZVAB1e-xLPOoKj6epB0F6RyzoM0Zv23aVd70McEmqDyvLqdT_fgwJjHjc67ABctHfVQISyY0ewBCNBxpmXi2k4ZOdV6j88HY6KQ40W1d5a2SSUazYS303NJ5AS8SWagdSzW2-wFeGorGmNywTZaj2YlbNnzBHi6__aeWxRsTmjF07FCyn3fYaBH5YNh3qKCMs0CUAEDg8xC41zi9-_trD4lxF2pWyhOHR4rg2hT0zzc5lyaDiy_pGYhX6whTet_a9wrq-fxDn7qutA9Hlm0g0PHsb5-WJ8KlkM-ZB9VvCDLC5L8od4CqST_qEdwzg5MDATHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=F2J5LTnf90U2HD_uXEZVAB1e-xLPOoKj6epB0F6RyzoM0Zv23aVd70McEmqDyvLqdT_fgwJjHjc67ABctHfVQISyY0ewBCNBxpmXi2k4ZOdV6j88HY6KQ40W1d5a2SSUazYS303NJ5AS8SWagdSzW2-wFeGorGmNywTZaj2YlbNnzBHi6__aeWxRsTmjF07FCyn3fYaBH5YNh3qKCMs0CUAEDg8xC41zi9-_trD4lxF2pWyhOHR4rg2hT0zzc5lyaDiy_pGYhX6whTet_a9wrq-fxDn7qutA9Hlm0g0PHsb5-WJ8KlkM-ZB9VvCDLC5L8od4CqST_qEdwzg5MDATHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lR29jzfxh7Jrof9eewZuiQgpVR6no3gmEzQq6yu32yyXdKzsbDuauGySSA0hGF6cY59vSMH7pl_kG8HgnyQlHBMtyFPjGhOKeydXIoPARbN-rRo3gcwcJFQsw9I5V9unfYO0-PxLMxuKF87RqVFmuNpUAqtDMfBNzLZKAn0-sQbvcHLH2e35roZzbU91Ngn32B9dMfV-YME6O04okiyFZkiCr2XNBlUsXQe-0w9ge9QHjgU0wDoqtyTANKjJU59hGMhlVH93agHsIICGUPK0PlD_BpFj31za-n3GyVENeu6NCkBJAOTKk_BZtvhY9lYEHcKhIMiIOzuN97M7wxV_3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=VOwtecskSUnN1zlfRPIUjE-ddL9Egvu_Ip1rcK7oaJvkiwEb6TBhmj_Km3Zs6OYray7aijcHb9tyjeTY42663YhjX-EbWoIICkkHOSz-DbaiXisJgIzYOK7vts-aJh61sFRGn1d-JEkwKDSkOHbHQ-arW-t6uMtd1ef03Sv7oLHvs9ZdfWSEiGqdvwSDIcLNQl1DR94iFKCsvsxUkvqixFgq8UNNfMylRiV6HaYDdKLAV4GNadSJ2fQ1NZ8_H5diYZ8fuCeHG9G1xdqDkFcA2TDa8KxyGm57m6RuUY0bclgPbhCgmvku192N6On6vzHAVUYI1XjR6fyuyyaVR-sB4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=VOwtecskSUnN1zlfRPIUjE-ddL9Egvu_Ip1rcK7oaJvkiwEb6TBhmj_Km3Zs6OYray7aijcHb9tyjeTY42663YhjX-EbWoIICkkHOSz-DbaiXisJgIzYOK7vts-aJh61sFRGn1d-JEkwKDSkOHbHQ-arW-t6uMtd1ef03Sv7oLHvs9ZdfWSEiGqdvwSDIcLNQl1DR94iFKCsvsxUkvqixFgq8UNNfMylRiV6HaYDdKLAV4GNadSJ2fQ1NZ8_H5diYZ8fuCeHG9G1xdqDkFcA2TDa8KxyGm57m6RuUY0bclgPbhCgmvku192N6On6vzHAVUYI1XjR6fyuyyaVR-sB4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=DY6K18IsYd8F1qrwa5HBJWW6qm2Y24AgdePVNFwYK3UcBxgVFIU1u-el9mH1uL-20sqUltvMGHcngxpwKvksnMNBy1FLhFy1hdU2N5p9A_q0XYHUfSnsvMRchBaQg4-DdXU5PshXXPbZkr3-cbg9RAMAcKnk1kvwCHFKB4yAnXgtA5zbPlVLaBcXgLTAPSPNb40GsMCAybp2ySPj8fAq-ULIMQUyaztpI20tTkRvILahy4nV14xT1Kbr_MhCbpTtiNTfyJ0fUzH9ewUNskULqcZKCTqKCuFCq7Wj8Dc2-Kk1v0aXmXS5GvgUG3fSkYIwJjT_AUP3_g_dNHl40BlUwmK6GkUunKcCF_VTKK-5d0BjQLot4GkVABv6k4nRZBrjODX910gJMpAqqmuB097uvcB5Uw9dGlquCgETGtFWmexpnZ6bAbdEZnvVRig5Fd7lPXO1L8xFhgnZ5zfmjPq3ElVS4XiBF_VwaGZY1Md0ZKoEBb6xBTwljQq9ZCLSER4gFoNwRM2w49rvgr2qYHj8PUIkb-4bwuDfoz5v7epivGLcgoCiPdpu2se1idpOIistHHt7lyG1ji8y0EinIcR8OEwvFyV4BF2pTVGuwP79jH53ZCGQjOtnFIpMuKJcbMf-5nMqFTYvX3yC6rgzInsVAXm8Gx0V8g_aD24XhMR8tEs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=DY6K18IsYd8F1qrwa5HBJWW6qm2Y24AgdePVNFwYK3UcBxgVFIU1u-el9mH1uL-20sqUltvMGHcngxpwKvksnMNBy1FLhFy1hdU2N5p9A_q0XYHUfSnsvMRchBaQg4-DdXU5PshXXPbZkr3-cbg9RAMAcKnk1kvwCHFKB4yAnXgtA5zbPlVLaBcXgLTAPSPNb40GsMCAybp2ySPj8fAq-ULIMQUyaztpI20tTkRvILahy4nV14xT1Kbr_MhCbpTtiNTfyJ0fUzH9ewUNskULqcZKCTqKCuFCq7Wj8Dc2-Kk1v0aXmXS5GvgUG3fSkYIwJjT_AUP3_g_dNHl40BlUwmK6GkUunKcCF_VTKK-5d0BjQLot4GkVABv6k4nRZBrjODX910gJMpAqqmuB097uvcB5Uw9dGlquCgETGtFWmexpnZ6bAbdEZnvVRig5Fd7lPXO1L8xFhgnZ5zfmjPq3ElVS4XiBF_VwaGZY1Md0ZKoEBb6xBTwljQq9ZCLSER4gFoNwRM2w49rvgr2qYHj8PUIkb-4bwuDfoz5v7epivGLcgoCiPdpu2se1idpOIistHHt7lyG1ji8y0EinIcR8OEwvFyV4BF2pTVGuwP79jH53ZCGQjOtnFIpMuKJcbMf-5nMqFTYvX3yC6rgzInsVAXm8Gx0V8g_aD24XhMR8tEs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TAVtk5yds95nbXKJVd2rfPUdJVDgf20WpxnSmlpqzn02akufDUIrx6LLK0vt7u39la0Cnt3KtxH9WVXu2hzU6LcVhB004BP9-3Z_ShoHmDekL67Sb_yieL5ylL7SUXaFeruqCq86ZgkgYksUiptEAVdRhIXWZozUNQK0H6H-FtFFqWtpkPlGhfn9Pk3yr1XB036OuM6XumAZ2pAZEDi61ldT82ctJFTyNqn2Pq1YdNe1BLwG_9YNNNs3S_eqPxnSOQ8QXzWDMhnYcmVTFFBHQKYogymNXxdxsxoB1lu3sgdMmktYIHAcCo1xzqfcxPdWFkOO2dKHNica0cREULS8ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=Xn-xgLWdF_9JWhggM4923IGAXr3ovhvHd586gjnpURRgt88aQSnOHEmMC4YC1s0bGGLjOPz6q0VU6FMafK2_v1ldYq0p0LCwKBOL_Ee88KK-Yq1AMPYVzJQIIJFLKhDkKvfFZ3S9kx3MQMuyxk6xbplvdZqHbYrFGLr5efO22zqBHnEPPh8QvvSakJtsSa50dSj8EA9Zpsi7T_fHhUmeB_ogKuneg9CpISBOddKrbtuAjfxPlD7FzomTrdLH3VSV9Ck_25TxybYmwqfECcefCG6Eqh2qqRt1M7WU3VE21QyvrXBJ_GYtt4M9NYpU76Pw4mIggYW_w1bv5c11ZUbaOXyElPWqcVHfq43chZqKYn0cgJ22n_Qy4Ny2xo3Bt2X_g_z1z1YQpvbNJ83ZFowjSBRAsS_G8yqBOF6TBuOfCWIbu98NFILDyE3LQqOA8VnFVxSDfmUszJeVcKH_PTR48dBouaR9Ls4AaKudht6w7uut3i78NedW79didLLX164w6tIyI4ApNhRqLxdJ5AUvhwzh8b9ncKjNQbenFjAHzJUMbyzQiicFUaJpps2nTjVReWVCpt2QfbCSCUj7WO8IK_t4p9XMTc8oUomsGTcbKEcDhgGsbZ_IoHF7RgErG1HgfQDNeks5mQuJTPMCamFCY8s6tWWk0YQoe-2oRcI0110" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=Xn-xgLWdF_9JWhggM4923IGAXr3ovhvHd586gjnpURRgt88aQSnOHEmMC4YC1s0bGGLjOPz6q0VU6FMafK2_v1ldYq0p0LCwKBOL_Ee88KK-Yq1AMPYVzJQIIJFLKhDkKvfFZ3S9kx3MQMuyxk6xbplvdZqHbYrFGLr5efO22zqBHnEPPh8QvvSakJtsSa50dSj8EA9Zpsi7T_fHhUmeB_ogKuneg9CpISBOddKrbtuAjfxPlD7FzomTrdLH3VSV9Ck_25TxybYmwqfECcefCG6Eqh2qqRt1M7WU3VE21QyvrXBJ_GYtt4M9NYpU76Pw4mIggYW_w1bv5c11ZUbaOXyElPWqcVHfq43chZqKYn0cgJ22n_Qy4Ny2xo3Bt2X_g_z1z1YQpvbNJ83ZFowjSBRAsS_G8yqBOF6TBuOfCWIbu98NFILDyE3LQqOA8VnFVxSDfmUszJeVcKH_PTR48dBouaR9Ls4AaKudht6w7uut3i78NedW79didLLX164w6tIyI4ApNhRqLxdJ5AUvhwzh8b9ncKjNQbenFjAHzJUMbyzQiicFUaJpps2nTjVReWVCpt2QfbCSCUj7WO8IK_t4p9XMTc8oUomsGTcbKEcDhgGsbZ_IoHF7RgErG1HgfQDNeks5mQuJTPMCamFCY8s6tWWk0YQoe-2oRcI0110" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=UZivnhKAqFuX6cSQUpFy6lrSLqNu2GiLbByUghP8X9wSYeYyn64x0dvya3e3Fg9-pvqmV-3N7WLc0jvm7M_JB_xU3j8k-pQ9-eDqxoDcSimWwdehPsDZBCdFckhYofmfwVMfZFzKr6J0DljYV7zwDZB9WJNopbiAwnUxJr8z-SFh9v_cju5vUiOzyz1U4QeGWkqkGdGEicgMgMmRHxxg5Pbf6OFRYXXuvarogz36fOQONkKqerqexpgaLZkRJGHyeC7OkMR2TzVoTl1ykyrHquX57LYfDL6uFy5nIyB1Q8TMkYeMdhzelT0Wbi4_ANH2KqWrS_73j9ithO6jT4NKOmv1NdU9pvpIbsSWTVMeYeUm8i4VdSuopZrd_7UaYFr-itESPqS2gI98DM0RrOPsvPdLJ8rCrD5HyiekuLqTU45UN78spauAW_xYQT7Zj5maz4rUjcWFQWNFGBHAvmZ5rcQN8BRt83cCdV4PPCbKrOVQGlryShKxvq8Vdh7BIPau7MR2P1SxDI2yS-3T3iXVN-rHJS4SSkEW0R98NTOHY_ypgh-rBWhO6jLB-ytSnFff7Dj7ttFlv90fYjwz9qdYMQ4SUcv9W0ucLywMbVX-ZRowHn9TmnnafxWtJr_Eg3_pgl-cBr1mkFi1aXa9hmKDXB79b4prI4ovfFXs9UqX2vk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=UZivnhKAqFuX6cSQUpFy6lrSLqNu2GiLbByUghP8X9wSYeYyn64x0dvya3e3Fg9-pvqmV-3N7WLc0jvm7M_JB_xU3j8k-pQ9-eDqxoDcSimWwdehPsDZBCdFckhYofmfwVMfZFzKr6J0DljYV7zwDZB9WJNopbiAwnUxJr8z-SFh9v_cju5vUiOzyz1U4QeGWkqkGdGEicgMgMmRHxxg5Pbf6OFRYXXuvarogz36fOQONkKqerqexpgaLZkRJGHyeC7OkMR2TzVoTl1ykyrHquX57LYfDL6uFy5nIyB1Q8TMkYeMdhzelT0Wbi4_ANH2KqWrS_73j9ithO6jT4NKOmv1NdU9pvpIbsSWTVMeYeUm8i4VdSuopZrd_7UaYFr-itESPqS2gI98DM0RrOPsvPdLJ8rCrD5HyiekuLqTU45UN78spauAW_xYQT7Zj5maz4rUjcWFQWNFGBHAvmZ5rcQN8BRt83cCdV4PPCbKrOVQGlryShKxvq8Vdh7BIPau7MR2P1SxDI2yS-3T3iXVN-rHJS4SSkEW0R98NTOHY_ypgh-rBWhO6jLB-ytSnFff7Dj7ttFlv90fYjwz9qdYMQ4SUcv9W0ucLywMbVX-ZRowHn9TmnnafxWtJr_Eg3_pgl-cBr1mkFi1aXa9hmKDXB79b4prI4ovfFXs9UqX2vk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=vSsGm379oc-kdM7FOOaqpwb2vsn1oK4aiRcj9uONEQI8aWXad3phUtu2rUFelKzhjhDkCi-wTVpEUaF-lH1jmNkPwcjA2LZ3VeeETIF2XtnswZBKBcjKihxK-4yXTNAR9QuVzr82DgtD8qa9mKzc2bLgL8sq83YjpQPICCcik96kKZdv2XkOfzm55S4eNntqEhazZf-RWfJRQx3U4W4I6hM0YLGK14XywzmAdlXrbnYnQaw4xcwAb7qjy4AnBe8TuzyUZfiWorSEEbxoICsVrV2NzvjHSoi8JRjm5CWNNwqXHIewV1TC_2opjCeMX_Ccx5sTs6PxC8SpBhHwdRXz9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=vSsGm379oc-kdM7FOOaqpwb2vsn1oK4aiRcj9uONEQI8aWXad3phUtu2rUFelKzhjhDkCi-wTVpEUaF-lH1jmNkPwcjA2LZ3VeeETIF2XtnswZBKBcjKihxK-4yXTNAR9QuVzr82DgtD8qa9mKzc2bLgL8sq83YjpQPICCcik96kKZdv2XkOfzm55S4eNntqEhazZf-RWfJRQx3U4W4I6hM0YLGK14XywzmAdlXrbnYnQaw4xcwAb7qjy4AnBe8TuzyUZfiWorSEEbxoICsVrV2NzvjHSoi8JRjm5CWNNwqXHIewV1TC_2opjCeMX_Ccx5sTs6PxC8SpBhHwdRXz9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=W10MfZDztZwsXGFC1ZzBIFtoEZ_y2giU4CXSxPde5EC-aLKlXE0LAQHOjlxTVt48zKWK4fmcTygV4HtNk-6AQDHoofHjDhawzhUPUh9FxgUjIES0K41ie1-sCK-KapJI7AcE1VxSr_DIjcmLblbD9b4xHw4d2-mXXsdzYIupw7brZUoRuOHjKQZdHUtzUGlkqtZX73gqSqLJozZ3k7MpfrownM3Qwb7xLEuj1nVF1bAFk8DLTNzj77zZ-MGzmktjojhA8YgAFMl7bf_0i1lL7k4hPJDm4HSYjA8gEG8mPHySEVaA3alSqHGVdTRBA-KLGDLiIhp6Xu1RWsw4RcySzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=W10MfZDztZwsXGFC1ZzBIFtoEZ_y2giU4CXSxPde5EC-aLKlXE0LAQHOjlxTVt48zKWK4fmcTygV4HtNk-6AQDHoofHjDhawzhUPUh9FxgUjIES0K41ie1-sCK-KapJI7AcE1VxSr_DIjcmLblbD9b4xHw4d2-mXXsdzYIupw7brZUoRuOHjKQZdHUtzUGlkqtZX73gqSqLJozZ3k7MpfrownM3Qwb7xLEuj1nVF1bAFk8DLTNzj77zZ-MGzmktjojhA8YgAFMl7bf_0i1lL7k4hPJDm4HSYjA8gEG8mPHySEVaA3alSqHGVdTRBA-KLGDLiIhp6Xu1RWsw4RcySzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=LVCBttcy7_AoH77IvkmeEpKbxtrDSRWudyoMLRGMaImHxoWynh1P32M5CYlZZu_p7jc92s6lUZTsOTeTK5J5EyPPPD4VlBgA8c4W_LKq_zjjIPvSwVcGsTRDNJ7TG5uRdSL1wWbqjwK42YC9KxayrBxqZYnFkLnmLHrdb56_z2-CoQmtU19ndPGfrOa1EzN2eGZeIs9xaeDXGfJNHNihR2y3ga145FdUCQ4ovTRdJ-BHjr5HcMqdzafuDicRS7O-07lMWQDRrAK9qd08ZXlNW79MPBYY-jqEt4_CTdAp2F_wrY8RCXJT4LhalOpj_1_Zjp_cBBkPIwVpDVAEo1ERog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=LVCBttcy7_AoH77IvkmeEpKbxtrDSRWudyoMLRGMaImHxoWynh1P32M5CYlZZu_p7jc92s6lUZTsOTeTK5J5EyPPPD4VlBgA8c4W_LKq_zjjIPvSwVcGsTRDNJ7TG5uRdSL1wWbqjwK42YC9KxayrBxqZYnFkLnmLHrdb56_z2-CoQmtU19ndPGfrOa1EzN2eGZeIs9xaeDXGfJNHNihR2y3ga145FdUCQ4ovTRdJ-BHjr5HcMqdzafuDicRS7O-07lMWQDRrAK9qd08ZXlNW79MPBYY-jqEt4_CTdAp2F_wrY8RCXJT4LhalOpj_1_Zjp_cBBkPIwVpDVAEo1ERog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=rdO011Ibzw493Ad9p2HRr9fYYwX9DMcr4m4Zk135OC6tYwG-0KP-mHeqaKlJpJ7mORot9EBMwOkpojIu8ROdlo7O0TZwlm267JaYdeY7DK-PusSPLsXn9RZHiAas6eKfwBAn-NvzSgLw6CMBH3RDOE4_IIodb2GK3N7hfZjW26OIpT6hTCmjwUQVqrntICYeOr6_fsZOh4oynYw8DpBHh87U7hMtbJXCarTbVr1y-wvyDUUuOHTEk4XYgQ1rhgaaQh8KDi3M2rBo5JxOKpx-h0SO23oXTeDkSyOie046N4oKC-AuWxW-Pz--bCFanA9RBMHo2Muj4JhjDDxUFVM0LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=rdO011Ibzw493Ad9p2HRr9fYYwX9DMcr4m4Zk135OC6tYwG-0KP-mHeqaKlJpJ7mORot9EBMwOkpojIu8ROdlo7O0TZwlm267JaYdeY7DK-PusSPLsXn9RZHiAas6eKfwBAn-NvzSgLw6CMBH3RDOE4_IIodb2GK3N7hfZjW26OIpT6hTCmjwUQVqrntICYeOr6_fsZOh4oynYw8DpBHh87U7hMtbJXCarTbVr1y-wvyDUUuOHTEk4XYgQ1rhgaaQh8KDi3M2rBo5JxOKpx-h0SO23oXTeDkSyOie046N4oKC-AuWxW-Pz--bCFanA9RBMHo2Muj4JhjDDxUFVM0LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=cVfhBA8VtQ8pqRyWmcwliyV29Xew1Yh89tVCKVCjlsOiXoelcqWtVQ5wIicMEy93vDEfbTFglvQVpwyfT2o55wd4OTOSlUvMZ2QDr2jYZtvYPm8dKx6AjivNMC933msNzlapFHtevwZa7sZadxgHYeATlGOoNqFBpwchYhqLyaqgzAP6mPK1JmfEZklxPxYPLI3PHuRW03viDsXZFKiMLFHIZ-eA4jGta8mtFgGxgmgiaxyjh2kpX7RN8RMaZ2E2KgF2C4yjMleCyk4TxS0kSy7KCJhKHNMQYidz0-pXYYXg1rK2KyuWf_t3VmBRJgizSpGc9Fl9W3Wx8BF7dommgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=cVfhBA8VtQ8pqRyWmcwliyV29Xew1Yh89tVCKVCjlsOiXoelcqWtVQ5wIicMEy93vDEfbTFglvQVpwyfT2o55wd4OTOSlUvMZ2QDr2jYZtvYPm8dKx6AjivNMC933msNzlapFHtevwZa7sZadxgHYeATlGOoNqFBpwchYhqLyaqgzAP6mPK1JmfEZklxPxYPLI3PHuRW03viDsXZFKiMLFHIZ-eA4jGta8mtFgGxgmgiaxyjh2kpX7RN8RMaZ2E2KgF2C4yjMleCyk4TxS0kSy7KCJhKHNMQYidz0-pXYYXg1rK2KyuWf_t3VmBRJgizSpGc9Fl9W3Wx8BF7dommgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=gEeu6Fz4Rx6rMXjvNeTOtcKDE4kodRm64fsk0ueRlZ6iow259oA_gUEM4kuvGPC3_-iP0sgErS0U8mAz6KunvDm91Hmfdf5v9i-F5rsAnoUtF3WVUGbwRcOwmhMOrUdf9qxd3y5h9elFuNQwY9f5U57g6MTovIIa-zz2SwR4H2Wd_2hHGkD0oPn2NeNiVvcHedkDk3y8uMBRJHJNkx5fU4DWTGhXaYNJ_Jw7I7vHKBFpncflY01C76c1KXUa3OY1DlNc_5EohYJ7bnLg13r1oUeLUIIowVxwNfhwXMW0TyaUGSBMFrxWskqnfCDxDu1SyC-X0uclJfRv9sg0RDoxJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=gEeu6Fz4Rx6rMXjvNeTOtcKDE4kodRm64fsk0ueRlZ6iow259oA_gUEM4kuvGPC3_-iP0sgErS0U8mAz6KunvDm91Hmfdf5v9i-F5rsAnoUtF3WVUGbwRcOwmhMOrUdf9qxd3y5h9elFuNQwY9f5U57g6MTovIIa-zz2SwR4H2Wd_2hHGkD0oPn2NeNiVvcHedkDk3y8uMBRJHJNkx5fU4DWTGhXaYNJ_Jw7I7vHKBFpncflY01C76c1KXUa3OY1DlNc_5EohYJ7bnLg13r1oUeLUIIowVxwNfhwXMW0TyaUGSBMFrxWskqnfCDxDu1SyC-X0uclJfRv9sg0RDoxJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=SRXfOZQjChmiH3bT4BWpIGDI-QSVtkpslg-f4syebLo4RmpxhHM5ujfeK5GJuIZNz9gR5m0cIWblYQwrm9MW15czSWzB5dQuJQ--7ZxnvlBSfEB-CC2_5iTR4a_FrDp1my-AcEZV0dlosfun5xLV6pvZ06k35sgk80Qr8ImKLr_pxu0POJJK7c7wx78RT2yC28bjG3TS6vB8NGJYEPgli1PiXFD3RDOh6whGIe2lioOkQmZ_3G7IFZHM3D3U9iPls5ZyeRcgU1xIGvwr1CGmcvR6zqxGk14tQX30EcnaCmd85dlZxt2KJu38ZhSlGTd5u4o7F8bJ8IuQ_Dsz3zekRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=SRXfOZQjChmiH3bT4BWpIGDI-QSVtkpslg-f4syebLo4RmpxhHM5ujfeK5GJuIZNz9gR5m0cIWblYQwrm9MW15czSWzB5dQuJQ--7ZxnvlBSfEB-CC2_5iTR4a_FrDp1my-AcEZV0dlosfun5xLV6pvZ06k35sgk80Qr8ImKLr_pxu0POJJK7c7wx78RT2yC28bjG3TS6vB8NGJYEPgli1PiXFD3RDOh6whGIe2lioOkQmZ_3G7IFZHM3D3U9iPls5ZyeRcgU1xIGvwr1CGmcvR6zqxGk14tQX30EcnaCmd85dlZxt2KJu38ZhSlGTd5u4o7F8bJ8IuQ_Dsz3zekRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ecwDPy0KWhiI2z1I4J0MYUF1b2OjST4ULCiphWZvqoPUEEDB9k2CvN5n2K_sIBxD7_0gZc5j1aWZmCBILBkxsDVtOn3ipB8HwEUgxQgKEfJLGg2tPtkvrRVt1x53756LGz1tPuS_7WQm1ADH2TtOCob6kfsWOAmW736-4TJKsVekUwM6QSzgcIkVswz4uLGLplXdNZo8trVx0lca6lsT2lewAkjkC_wakVczoLgUd6scgyDVCnEGlX1hbak3iNkzoAU6LKtbSYPo2pv1PhjRbhdUOLey-ihi01J77MhsZ5dPwxy4akP3afI_p-lNpc_Ed09i_pQgAzLqxNoxfRI7Qg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=kJ8fkp41HAUrmnKJY1gpCLk756uDaKsSDW_t_pix-f5V4qK-REXAhBhrA2aLrFPWeg4kgje-vy5NWuOhYCwHWnICqeeU6ExiPGIfWYj3Ew6Eb3Lyjn91WbWEBtFIiNBXxwlnD7rxA7_sG31jBJ3seAYLF5T8SGp15Vw_-xlK_nbgzoRp8oia66V_-7SjLzGv-XpM307wMH_lm-rpuKicaOAP8ynt_R48IefzFKIz8foFkSdR2s-2QwLi2ucveYqeo2Jd5ES1OPHIT16C7mhCC0-ursjU7PKEDZtvkXYXzmjjHg2ll4qgwONtAXqgWve6bMKSNTWXaItVGnaev98Q0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=kJ8fkp41HAUrmnKJY1gpCLk756uDaKsSDW_t_pix-f5V4qK-REXAhBhrA2aLrFPWeg4kgje-vy5NWuOhYCwHWnICqeeU6ExiPGIfWYj3Ew6Eb3Lyjn91WbWEBtFIiNBXxwlnD7rxA7_sG31jBJ3seAYLF5T8SGp15Vw_-xlK_nbgzoRp8oia66V_-7SjLzGv-XpM307wMH_lm-rpuKicaOAP8ynt_R48IefzFKIz8foFkSdR2s-2QwLi2ucveYqeo2Jd5ES1OPHIT16C7mhCC0-ursjU7PKEDZtvkXYXzmjjHg2ll4qgwONtAXqgWve6bMKSNTWXaItVGnaev98Q0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=atGEUx5CKbT_LFmXKbmFlOGWkp68zBkx83WuvAiwVs24-Y-EcuSlmCbO-VY2CFCYBjnzC6GnHKGnAqM1Z7JSBqAz0NALd7c1Vffilz2Bgc6Y1tGNWGqmSQsdSU3qR9El-bbFlFX_YRNHyharytVCQwmG4AAcNfqKtao1gV92RgsFrp6gdxESyzYLowItGWeEZu_SxuRRdpQihZ1dJ0LE171daQXNerGvkSgbWHHKP5EYlVphbSEi86zWFUYAvmbKAWkVR9DROVCJP7f1nEm1MdZpH5jPGftXqllnUNedPlD4LSEcfrCMjGQHWBwM2zonhw1t0JGhyAnFO3t6TT3Jmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=atGEUx5CKbT_LFmXKbmFlOGWkp68zBkx83WuvAiwVs24-Y-EcuSlmCbO-VY2CFCYBjnzC6GnHKGnAqM1Z7JSBqAz0NALd7c1Vffilz2Bgc6Y1tGNWGqmSQsdSU3qR9El-bbFlFX_YRNHyharytVCQwmG4AAcNfqKtao1gV92RgsFrp6gdxESyzYLowItGWeEZu_SxuRRdpQihZ1dJ0LE171daQXNerGvkSgbWHHKP5EYlVphbSEi86zWFUYAvmbKAWkVR9DROVCJP7f1nEm1MdZpH5jPGftXqllnUNedPlD4LSEcfrCMjGQHWBwM2zonhw1t0JGhyAnFO3t6TT3Jmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=qtsziz5audDI7n-w-kq9g0ysdf2IFG6XsfiC0JWuDJntLCWoPuWgYjcn_FmO1CIF8PkKVKtRebcfdWDZUv2liSX3BQcYaL4JU7kR9ovWHvmJ5RXC1-_XswtI6by6ArMpe9NuvEDlXkZvVzrUvp9yg2IiibKQgu7N1tzfJlvMDpk8HrI_9bKu_L9W9puoFsC9AwwHZ5MMv7VVNjEVDPdvwAjkd11yMec6e69UkkdNtEArY_fZ8rTW721iWTkZXjObXBOEUWfLafWY_UzbrXCLoDnV0jHmrid2Zk4wYNptG6MVmkBJ7kbHF8UoNVKQBOPt04rkYK4L-20Mxk97b2Epew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=qtsziz5audDI7n-w-kq9g0ysdf2IFG6XsfiC0JWuDJntLCWoPuWgYjcn_FmO1CIF8PkKVKtRebcfdWDZUv2liSX3BQcYaL4JU7kR9ovWHvmJ5RXC1-_XswtI6by6ArMpe9NuvEDlXkZvVzrUvp9yg2IiibKQgu7N1tzfJlvMDpk8HrI_9bKu_L9W9puoFsC9AwwHZ5MMv7VVNjEVDPdvwAjkd11yMec6e69UkkdNtEArY_fZ8rTW721iWTkZXjObXBOEUWfLafWY_UzbrXCLoDnV0jHmrid2Zk4wYNptG6MVmkBJ7kbHF8UoNVKQBOPt04rkYK4L-20Mxk97b2Epew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=AHQmsxv2toLOF6uR8QSAL_4uNyGNpY5bwHe0omkOVsp0qSCLs-7NfnDcUeF6EJejN9Bz8X7YeWAu5sgmc2sdVisAjUeTIphVSyrJs-A3ZyRzeOrUiizzDel23wgRUH5NVXTdkobUw7LMDDlbfvyh7_J8m8tkyDvYub3-33NseMDTNtXc124xuKZ--VN6Zb7ELsDLybRJuM4RUo0ZhFmiUK69a2tzul34JSodazOubbmOuejq99LiQ8xYYecXmbtcqX23o-2KJ80qJV_TVvNY7Uwg_utOEH7FJpnQk0ifjgqszzq6YdF6Wu1nH5MtkOgcMB8TmghdZx1LXkHYbH5jfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=AHQmsxv2toLOF6uR8QSAL_4uNyGNpY5bwHe0omkOVsp0qSCLs-7NfnDcUeF6EJejN9Bz8X7YeWAu5sgmc2sdVisAjUeTIphVSyrJs-A3ZyRzeOrUiizzDel23wgRUH5NVXTdkobUw7LMDDlbfvyh7_J8m8tkyDvYub3-33NseMDTNtXc124xuKZ--VN6Zb7ELsDLybRJuM4RUo0ZhFmiUK69a2tzul34JSodazOubbmOuejq99LiQ8xYYecXmbtcqX23o-2KJ80qJV_TVvNY7Uwg_utOEH7FJpnQk0ifjgqszzq6YdF6Wu1nH5MtkOgcMB8TmghdZx1LXkHYbH5jfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ilbpdeiy3Soi1MkS21SLMuO_pkeDK1usVR92iaiyMbvSA0pCnYCu5DAJRC5redCeLwgDDvixejOGyOql8IIXWgz-8l3RBM79aWzjKvbgHeyMHccpsUflLbLyVkSsx0UoCmfooQOf1jY8RSMJFB2Tv4uwnGtpIv8NOFvxNmgHv2kvYr_-JWPSxs9evv3WGNp0woytfVnVKn7y38YwKIgsf6tEi5rpfG3YNd97P2tdfqRgIqXGH5E8rn5e4rmwOKujCpV_Rx-eI4EGZNean9WEKvhRfH8yWAQlzHy4EyTc_VUt61yXIlRLdu-Sfof7qu86szb-LH97Wgn_5RzFgQnNnA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6707" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=cJ_OGtHIC6olDYvZsBMIJHBQpxKYkDt7Y6LtHaNGYPvsJWbkqvKONCdQtswBfT8vz3qbNwKh3hN7RK-C6VDiLdr6NNtKdMZPkPTQ1_6eebnaL-IU0EL-_yfgaFndRHKQq-2UCPHvzxvOfyJ6fdj0ir61C9fM1i-q5Lm_tsRRpFAqczNBC9fp-tBD8kx3Fzw7EmdFVVNDsYx3LmZ0ANFFz_ed1nPTISS5-0jPqxN697ABHj0xhZzBYQZ9hPhT_0g_rPwEyGwCQyBDr4O1d2EmbyiWNJfzuUqyU-9Xtj7iCHVFjaJpH5H3hD8p3FylA-WvhaLb4-1EQUuT6ib9H0zU-zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=cJ_OGtHIC6olDYvZsBMIJHBQpxKYkDt7Y6LtHaNGYPvsJWbkqvKONCdQtswBfT8vz3qbNwKh3hN7RK-C6VDiLdr6NNtKdMZPkPTQ1_6eebnaL-IU0EL-_yfgaFndRHKQq-2UCPHvzxvOfyJ6fdj0ir61C9fM1i-q5Lm_tsRRpFAqczNBC9fp-tBD8kx3Fzw7EmdFVVNDsYx3LmZ0ANFFz_ed1nPTISS5-0jPqxN697ABHj0xhZzBYQZ9hPhT_0g_rPwEyGwCQyBDr4O1d2EmbyiWNJfzuUqyU-9Xtj7iCHVFjaJpH5H3hD8p3FylA-WvhaLb4-1EQUuT6ib9H0zU-zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=iUJPQ3THYj-sGD3exdr9qUgMiee5_ixoMQuDPPVoQ9B24wkarXPPIPDemg8Dx8fqtUSpkAErnOoOmOJwB9mOdzaFUMkO7YCD-KomhFn-5fpLvpn7DTEkMH8htF8Xqk8hpRS2_u5KQr-O3J7n-dNaieZM-9Vkihd6GkGqrU144HXwxwec7PgoVqTz_jU7nLSTapib8vocYabF4TXehdXfsn4UCGN-UZzfH5E-GaBQJoaIv04rRQXo63N3oo8MuBI0sL98bLEITl-mcK7EC3fEay0ow1YvGUyxxG7Ip2nUWLUh9AtULBjYK-HJjhwQAUvGwlMpzVCpu6VSFkxD4YSgIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=iUJPQ3THYj-sGD3exdr9qUgMiee5_ixoMQuDPPVoQ9B24wkarXPPIPDemg8Dx8fqtUSpkAErnOoOmOJwB9mOdzaFUMkO7YCD-KomhFn-5fpLvpn7DTEkMH8htF8Xqk8hpRS2_u5KQr-O3J7n-dNaieZM-9Vkihd6GkGqrU144HXwxwec7PgoVqTz_jU7nLSTapib8vocYabF4TXehdXfsn4UCGN-UZzfH5E-GaBQJoaIv04rRQXo63N3oo8MuBI0sL98bLEITl-mcK7EC3fEay0ow1YvGUyxxG7Ip2nUWLUh9AtULBjYK-HJjhwQAUvGwlMpzVCpu6VSFkxD4YSgIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IwBIkrKa6G0B8pVdBUoS-kMePrvemEO_D2UTMGYlsYVJ1ucOh4fB5Xo-h1m3Vgj0eKMLZvra7uYNDAKVPHG11Uyjqe6Y-a7DvJT_ZgTAhgbCGO4WVrhoWSEfAia5ESyJdsyVCYj9AVAIH-Y-EyAuyQWl1xSCajybMN3RVUSP7Lty0_g-RzftV_ejyJ2y8XO8F1rfYM_CoEd4f-obNggx1bea88o03Aj57YFAC0RzlWX-EvxpdyJulzE4NL8R2a8vYzpes1vZbBx_h9Fqav_CD-_ra3SvROYcu4wDVX-DDN2S8kjCftlB2cSrJyqsVdk1a-zk0M1_1MBFDjAPt2vSIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/inS2ZRf25AhoXKlI2chaf2dPpvLda7XVePPhTq8Sy91_E2j7wSt3Go7UUdhi7xVZzY3ykJcoMK0oNp8zr1CF6Uya869BMe_E7n6DxPzMV4f_15sF7l7MAlHAPXWVGdG4TkNtAFrjwwTXH1FK3P1FqyoFoCEHsWso1WiSSyTDzfnBVHTeWYv_dfAb9-V_H6qVLqPSiLDBlv-eJD4E8PQhkCttcliOZD0QYmAtcXaozMp8wz6gT_V3y_Fhk2_JYd77NRCV_ZIF9gZWja0UzaZtmYfIUZrQSZ_P28Bg5TpueGITiagxPL0AdprwO1ugOAzMcV7RPLAr9HaNLMgrYQDPPw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=SzG9Cy-HX0i9mHXNqWTypW5OGnPwRh-RioeCH7bTYPjcl5igwQr6UyW7eeHSJ8lROHMinePTyQ6ZAMSWQnuyDVlyBNQAVMnrPoLHiMatT_JEZBTy_4TS0Vr0a7UX5_ueLbLjuhyNJWmND3_icFDhZURxFZAXfes9-R01zLhhrpjTjX-Cx7mymBVZV5GWwTUp4yQCecRmQicqIhXDf8Af3vK97IkoZax_gQv8Brr5QAeVp4_uZPuXiee5X9mNzN5bz45ZOhixQcdmUmYeaqdSjLhSF7U_b1zCPMQzwh_oj0znZQzMoxCQwgb4pxzQk6cnl-EpVVIuJSeqbIbEz2YGxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=SzG9Cy-HX0i9mHXNqWTypW5OGnPwRh-RioeCH7bTYPjcl5igwQr6UyW7eeHSJ8lROHMinePTyQ6ZAMSWQnuyDVlyBNQAVMnrPoLHiMatT_JEZBTy_4TS0Vr0a7UX5_ueLbLjuhyNJWmND3_icFDhZURxFZAXfes9-R01zLhhrpjTjX-Cx7mymBVZV5GWwTUp4yQCecRmQicqIhXDf8Af3vK97IkoZax_gQv8Brr5QAeVp4_uZPuXiee5X9mNzN5bz45ZOhixQcdmUmYeaqdSjLhSF7U_b1zCPMQzwh_oj0znZQzMoxCQwgb4pxzQk6cnl-EpVVIuJSeqbIbEz2YGxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qSUm7_gUtwA1CTIiSoCgbtgzelFTuvZnTP_22Uz7LKJc2JQcMLjsD72f8SxBTjxc5_F8txvSlIV2N4OJwZHbhaQY3S7zJUmpAYWWH-CZiSg3TZQBHB0QxMCJArQNbL0GBEyJkEbPvKo0TB-BkcP4CW9LWQ8uswYq8Pyp7NEGhBo_cCOU1ZwI1bP85z4o1xKXG0mdbmtO8axAFziGsNbfsWc6vXfnL7D5c4mlBgTK2TzyoQGYtSvkz8r0WMMPruqmZMw-Di7EVxjL_yNAgWP8GvnzGlLCeUwmGVbnPkbPXzg-2U5LWmsvePAl2ur13LpkX4QR2w0ouaLWRLa-RtPCEA.jpg" alt="photo" loading="lazy"/></div>
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
