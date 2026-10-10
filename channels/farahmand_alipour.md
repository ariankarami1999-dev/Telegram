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
<img src="https://cdn4.telesco.pe/file/eVw7Ido8aogrHNgn8Av5g1WwFbg4MUAtsWcUsdFWfoDvvfKmm1SE20uPVp_x4Hb73CBJ3QeZ9lugl4_ryMySa2zC2Y1VXxq8yIqRS6xJbE91gE_RC366k8ChW0HdcN0MBd8MwabV4Dfl1CalJaaTJYkhDfCrnOKLv_iAgHQVQYhEwUBRRbLNT3CaqZu8FFTcWIbPCM-pyP8AlnlAzViC7FryDU2Dy9fCUcYbMBzk0JihOUCKxCb8mbazWQU3rhkY1cKpYCvXsRUU-wzGEiEyOfIgFR_ueUU-ZCNYHlCaRcZf8kWFoC4w352MbsXfzMwRjNBt5SxXoqPNAK_3VRB3YA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.4K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-19 00:25:11</div>
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
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/6804" target="_blank">📅 15:30 · 16 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/6803" target="_blank">📅 11:29 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6802">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AGOey_jBLBxLdpyqfgjQ6yjG5SXM9Y_BC1Eo5u_9ziTd6Ab5PkydFXpZzms3lAZB_iZdgrzXGZKHQRgFhZlmJS0jhYIvn2r4ycW6xwUW_0P9eoijkIqy2OZjJimxkyHSiozJ9TDjd6yLoKb2ImlGI7t0PohtRx39at9KRyV0B5HzsaOv1oY-ljON9b2-nsRWHKTBIyBol7VSalGopyUbArXtwPX__KIND5nyLA-SampYzI8g1nbGfBZQix2VlT2UheRd8wHJDbCgHSnc_M73t6eF5kLetBzD2mhkqG_bi1eUxbiqhHOewnjflG_96sPseWlvP88SFuAk4UdM9m8KLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌د‌ونستید یکی از معروفترین آیات قرآن  که آخوندها دائم به نفع خودشون و شیعه و….. استفاده می‌کنن آیه ای است که دقیقا و مستقیما در مورد یهودیانه؟  یعنی قرآن وسط تعریف یک داستانه، و آیه  قبل و بعدش داره در خصوص جدال بنی‌اسرائیل  و فرعون صحبت میکنه و  اینکه خدا…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6802" target="_blank">📅 10:52 · 15 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6801" target="_blank">📅 10:42 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6800">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">روز ۷ اکتبر ۲۰۲۳  وقتی به اسرائیل حمله کردن،  نوشتن که دنبال کنیز اسرائیلی هستن!  هر چقدر اونجا کنیز گرفتید اینجا از تنگه‌ پول در میارید!</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/6800" target="_blank">📅 10:41 · 15 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6799" target="_blank">📅 12:52 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6798">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tZyMKTdo9tWXDm3IqRKfNsXOxqzuQMJD6G6ykThT6dv-2ySnIhM4CKMENeOZIDBV-Uo03aOSUw6Hma64vVk2AQycakTqlgS5P4AjEOgEcNVF03q9FY2ZJU0p4IgWAXmSy_UFwdmS3-gM9-tMIO949M7VMmg89GAtchbctA5bchSBat6yhElC3zpF_E2OeDXKIIfMHNIm7MKz-eDch7RwC7P1bPLUrkwdw-J7XLO7A9j_4BtWfNeckGE62fg0ZdM1DQ9-7U6e-HRbYmQubQ3PPvgu1Yp0uTvKB8m4V3i6pognp0WnoV4k2bbKvsjIFrn-6ZpYsMYuyDfilgH3U4M4hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه فرانسوی لوپون از همکاری چپ افراطی فرانسه و «اخوان المسلمین»  در تخریب‌های اخیر خبر میده. دولت فرانسه نیز دیروز بر اساس اطلاعات نهادهای امنیتی از حضور چپ افراطی در گسترش دادن اعتراضات و به آشوب کشیدن اعتراضات خبر داده بود.  در حالی که اعتراضات دانش‌آموزان…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6798" target="_blank">📅 12:45 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6796" target="_blank">📅 12:43 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6795" target="_blank">📅 13:10 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6792" target="_blank">📅 12:57 · 12 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/6784" target="_blank">📅 12:08 · 12 Mehr 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kkzEXuqEeMcbGn1_3YqT3BrHN-I1aoAtbRmZpK2jazvYAT1ldQ-gShcpFeaJSkyOMAoH8nKmOCD0s7TW22e70mYUj-Ojmx9XR6bldHYgaB_pIJMGpn7Te3r1VRudM6U15O3WlTyTdQNw5_QX3BUhfUKM_-QIW0XjvdlDzcoB6b02KtdRvlaPsXuCv0BFJuLFdnyaQ4AD334pE2EpcUwN9N-1nbr84gMvPrbynxtaK3iazEWyKEOIcE4EBjXPosrLLrhapuEgtIzuziKkMhMTPbSgE-YfUXXwsRGIrkaxNk31SFCt975GRSNghbM3J0JHJqha4MqfTz0cOQVKTVqIig.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6780" target="_blank">📅 14:21 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6779">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">بلومبرگ به نقل از منابع آگاه:
جمهوری اسلامی  پیشنهاد داده در ازای لغو تحریم‌ها، اجازه دسترسی بازرسان هسته‌ای به تأسیسات بمباران شده خود را بدهد.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6779" target="_blank">📅 22:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6778">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VinBWWXBe7MpO0UU2xK78VZ70iz2vW7wtzI0yi9JSxjbRbwDmQ-D2SB7vgUWD9wqPAz-8kBkfJGj0eGRtnn3wKnc3f5r8QhQzlVcQORZ0eGRW7IZy85cLNlj9O0OlbDBPUyeKb-B4odDDa5OoDj4HxzVCm0V5piD0vgI7-yr9cr2bCk_57ZrXKXOvJBYa_VZLJ-drJHNHT_lIt0aAjBXTaetKtbnG8LxyoSwQHYoXiTczzV_I6eAi4Wa_LFPccAK2gOMw4r8tPp0xnU_B-IfzX2_eMmHxy4bC-o6_MLVSWmJpNQhZBXD8nziWymM672U8NPWp7j4LJbFZJr_gTIgvQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aKMLwBzjuxnK_iHAGRkI16exXfeB0drUPtGWUNsMY8qQln8GIUZaoMsNVXhlE3n-ZklLPOIK7JKzXvMxM3aVq5yTm6VCcCDQr4w_ftI4DyxIHh43ddS9Bhuh9FP3kLoJGH43CTupakFFO6Dwijkh0u1U0bVmP1GXxgePLSIbnzmS01TXd2LYOV7bzs_Y9jFG3asuGQND8b61q-vXm3OgfCZRFbq3Zwdw-yKojLT3Wkgn9aY7hHQmeR5dnYp-gT5g9K-yXjK7lnH1PE89lA_nrGTILyTXeT3omPGCHKMVbZ28uuT693VR6j9PMCXU6zrknSM-rzwL78CkuTni_waMBQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/c578cb6e91.mp4?token=CcDtsgQpVKwZmSIN1jPIxVTEvFM-pUsc2Cy5cPlMrvRpGrMQ7_OTkJkcGP5cT1HhwDoPSgD0elePvoUTRcB6hrgl59pX4B9pqXT8ddrLUVhJyCskBHlRsWMLu2y_Zb3BX5BBXAdAUiqygQlhUKw9hcP6k7kEYs6EgDvhgtwa8gaWoCBiDzbs_NRRpV0THhmKi-LMMLuSP_xecsMgBCFIYpzhOI9zcn-8_h4g60vbwQlm2DdF6MpjNAnZU9WwzE_vWATjcihO3zy3tb9sQdMQRQAnBQiM6c1uVdwEVcO4lKX07cwkPmJ9vUMl7ekyYlIT0Fk3zXLEi58K9i_NkaXaxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c578cb6e91.mp4?token=CcDtsgQpVKwZmSIN1jPIxVTEvFM-pUsc2Cy5cPlMrvRpGrMQ7_OTkJkcGP5cT1HhwDoPSgD0elePvoUTRcB6hrgl59pX4B9pqXT8ddrLUVhJyCskBHlRsWMLu2y_Zb3BX5BBXAdAUiqygQlhUKw9hcP6k7kEYs6EgDvhgtwa8gaWoCBiDzbs_NRRpV0THhmKi-LMMLuSP_xecsMgBCFIYpzhOI9zcn-8_h4g60vbwQlm2DdF6MpjNAnZU9WwzE_vWATjcihO3zy3tb9sQdMQRQAnBQiM6c1uVdwEVcO4lKX07cwkPmJ9vUMl7ekyYlIT0Fk3zXLEi58K9i_NkaXaxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/8a5052b840.mp4?token=Qr1gIWxwGePe2CZm-uSfsBIdQOyB-dcdZab0rMl_fXMqJnjBkR0mPsLvghE4egqC-_PPCVt7U3ze-LFdxdCy8OJe5BwQSS4hq_5sL5S1mbnVcC2YtrkcJGzuid540fFY7tPnL1LR4xfjntkgasD3NqpIGcXJRnJdPAVR1vIeSszX4OCDqUdMPBPNOYnN8bOM-wMR1Cw-ZbEl9UqtNgIxn-dujeRvI8GahosHX4AaDi1PHQScdk0Mdc5URXhkUio1eL1c9SoCFk7ypesPjT1X5w68FiAe0cAVya05XVBhmYajTq1mPD80yQ6wNt9IsUoYMLRuxxJJMfJnPIw204EjilOwXt4Q4rtIwC8ES1U6KxwxA1jJV6ZKSK96p7Av0gLotvxdZhSpC4a7ZfBB85kIhoHAQPXdTLCSKQ_d-6lawVnELiGG0R0Gtv_21MsNJIb81O41ovjhcx11HUftCaJSKThJYS8snVt_Jqt4sMNdGyibPRw8MEXG804A_Grd2QVCHSkc9lRCVt7uIvN6AOxYhCT8I5_HbamBu06mhqW_Ce8vjb3FMkMA0NxdJM2jmsraU-uqV8n5F5m_eEWY7zk1qCxNVditskwYjP6BN8hDFA9yOmfbqKKPGUV9hHHdGDfKh1b-uKt-7Aco32oeK4wlZrF0QFcu2MyqQ9Xe15hqxu4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a5052b840.mp4?token=Qr1gIWxwGePe2CZm-uSfsBIdQOyB-dcdZab0rMl_fXMqJnjBkR0mPsLvghE4egqC-_PPCVt7U3ze-LFdxdCy8OJe5BwQSS4hq_5sL5S1mbnVcC2YtrkcJGzuid540fFY7tPnL1LR4xfjntkgasD3NqpIGcXJRnJdPAVR1vIeSszX4OCDqUdMPBPNOYnN8bOM-wMR1Cw-ZbEl9UqtNgIxn-dujeRvI8GahosHX4AaDi1PHQScdk0Mdc5URXhkUio1eL1c9SoCFk7ypesPjT1X5w68FiAe0cAVya05XVBhmYajTq1mPD80yQ6wNt9IsUoYMLRuxxJJMfJnPIw204EjilOwXt4Q4rtIwC8ES1U6KxwxA1jJV6ZKSK96p7Av0gLotvxdZhSpC4a7ZfBB85kIhoHAQPXdTLCSKQ_d-6lawVnELiGG0R0Gtv_21MsNJIb81O41ovjhcx11HUftCaJSKThJYS8snVt_Jqt4sMNdGyibPRw8MEXG804A_Grd2QVCHSkc9lRCVt7uIvN6AOxYhCT8I5_HbamBu06mhqW_Ce8vjb3FMkMA0NxdJM2jmsraU-uqV8n5F5m_eEWY7zk1qCxNVditskwYjP6BN8hDFA9yOmfbqKKPGUV9hHHdGDfKh1b-uKt-7Aco32oeK4wlZrF0QFcu2MyqQ9Xe15hqxu4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو : ‏مشکل ایران انقلاب است. مشکل آن مقامات دولتی نیست که کت‌وشلوار پوشیده‌اند و در برنامه «میت د پرس» ظاهر می‌شوند و در رسانه‌های آمریکایی آزادانه حرف می‌زنند.
‏ما در مورد آن‌ها حرف نمی‌زنیم. کسانی که در ایران حرف آخر را می‌زنند، روحانیون رادیکال شیعه هستند که نگاهی آخرالزمانی به آینده دارند.
‏آن‌ها باور دارند وظیفه دینی‌شان این است که آخرین روزهای دنیا و آخرالزمان را به راه بیندازند. می‌دانم این حرف برای خیلی از بیننده‌ها شبیه فیلم به نظر می‌رسد.
‏اما واقعیت همین است. این هدف اعلام‌شده انقلاب آن‌هاست. چنین آدم‌هایی هرگز نباید سلاح هسته‌ای داشته باشند، چون از آن برای باج‌گیری از دنیا و کشتن مردم استفاده می‌کنند. این خطر غیرقابل‌قبول است.</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/6775" target="_blank">📅 08:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6774">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/luW67_k8pfKspjZVcJAdz6Yrg2k6g2o-gxPyjjaEHBUuoOERrZAXmM3XfVhdaFiQG4lu4fdhlD0SsxSPrZXObGssgHRapr3aMIx7Mgn4JgwNSutjS1CTtST9cWp7u5KEZNY7ret-8g42tn8q1y4KYogcgon5BdJNlTSBilOKUpuRfaLghGUubVDQu0yQTD6OuCcSxK2QEaNLZxwGoiyYbkFXf9QfIxbJHvmwDWYqZl0x37ZPeeM_FMmHiPXgcV6QkTuteNLlmRNl9RhtA8z0szm4OGEotx8Y77WkIRog3DnIKKWIZipX6KivWTxqhK8-AU5qC9dPPPBKXVME7ttN0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/6774" target="_blank">📅 02:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6771">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rEHhYytZ6mAZGZyml2qbsHBEjg5qFLpHPrII6_dK-9sUX1JYvALYwRG-ltit_2AAl3jp_hwYpMCBO7vSHLTBkBqHG3XRyxqO3aQfRZ7WT_ECsNDz5taHXPzY9UcuEQnP_iFh-srX5PFrwIcAviGd3Cod6ZuY8DRVyBgb-uUo5WsN8rggmO0IH8oe-bwryCgvLh2K9baMD_Bs9QHEhdGmyUKgGNTfoGjgQ1GbzOgkOkJBvhf_vhIRzdDTHxEz2NgCjZet-kBiOXUv8ytbajc-L_CK_EFnVJk1TV3JbxBNTwYh2s-nN7hiDHgMdv6-Mus0x_msQtS8cZ4oQSv0IvnVfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YcbnnV1-rUs3JPHDzM2q9SfxJuZ1VEJJB7tplFFpaeNfVFphsQv9rRKPkPHcO8qp5c7tJ5JDpHlUVHM4bSF9TDMviBslkjUNzbBtkgYrmPd_GIYNwKMgCw_z4c6VFnW8SFC7Cyc-kbm7ggH4Zeq3_Ewy-WIlgcwEx6bcOMwnQF0hTcOmrv4cIeeCN5HXNbjFaJiyj4pbM3vH78beqLccqfvvs6w0SnTpdgJMe6bfXYmpNAYqKe46MNdjBA7mUyD_-6Yc_clXLMkucMTEUIDQ2iVD6xR4OzbD4iszyOeCT9jerdeWkT2HO3qWl6p65PhTN7nC6q_2iAbLE3FEUYR-Pg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/895be358cd.mp4?token=XDKf1pC9fcf9rVHx3NQzskp1tgvgOAov1pTWtcW5VyehQ-eOfp4LLXztcUa7uF7-WJ8iZo8xfLGWw2_-0CY6GlDRZthgRPZi6MdSb5l-qJkeKRSU4Mw7MT7bTi7pAIbJ9HodB_ZD3DTuzNvHrB8J-EE_b6Z9B9S16flRAXRx3lHV42q6XpDvGco-QelDR2FDgWdDFnxkWBdwhCu5eaFUQ2JxZTuC65Yk7QxhWsq11IMAgNXSXIV_Wk1ViRGksZBY5JsPeYKL1W1JrIEREkmvnG6TOSmJeT3loLWWy_uYEclezuudyKN41-S0iQNhTNwceP_CY4zQyepd-DsqFJAkCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/895be358cd.mp4?token=XDKf1pC9fcf9rVHx3NQzskp1tgvgOAov1pTWtcW5VyehQ-eOfp4LLXztcUa7uF7-WJ8iZo8xfLGWw2_-0CY6GlDRZthgRPZi6MdSb5l-qJkeKRSU4Mw7MT7bTi7pAIbJ9HodB_ZD3DTuzNvHrB8J-EE_b6Z9B9S16flRAXRx3lHV42q6XpDvGco-QelDR2FDgWdDFnxkWBdwhCu5eaFUQ2JxZTuC65Yk7QxhWsq11IMAgNXSXIV_Wk1ViRGksZBY5JsPeYKL1W1JrIEREkmvnG6TOSmJeT3loLWWy_uYEclezuudyKN41-S0iQNhTNwceP_CY4zQyepd-DsqFJAkCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=Y2_j3Q4jjmMMoEda_MnkZ6ZD1tdrFQPBFviDIfxHSYDpj61WeWdFOK3kRDUeu5x8WvBTNEK9qmP9Tfn8vdbnXanjmo-3epqdp9VQ7bnKVb3T5chQRvorS3f0iw2NRK5lqkPoleHDlSxGrQHW0cYO-O2Mvys9PQQca_eRpEBdnzo2C8p0edGSt8BjP3L8qWTnOTg3ljCaHC1rtbxdoLU5vNArDrSBmRgAxhdk_ZZ9z4unYIS2oMT3WfFKTiZCLEtT9fdTTahelfLvkbVyhI6UY6wLsE77PbW8qwbalSLQ9Afm9GazanIGWKYVGT5Ileqbr9oLgQU_0am9qwyqJnhKlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=Y2_j3Q4jjmMMoEda_MnkZ6ZD1tdrFQPBFviDIfxHSYDpj61WeWdFOK3kRDUeu5x8WvBTNEK9qmP9Tfn8vdbnXanjmo-3epqdp9VQ7bnKVb3T5chQRvorS3f0iw2NRK5lqkPoleHDlSxGrQHW0cYO-O2Mvys9PQQca_eRpEBdnzo2C8p0edGSt8BjP3L8qWTnOTg3ljCaHC1rtbxdoLU5vNArDrSBmRgAxhdk_ZZ9z4unYIS2oMT3WfFKTiZCLEtT9fdTTahelfLvkbVyhI6UY6wLsE77PbW8qwbalSLQ9Afm9GazanIGWKYVGT5Ileqbr9oLgQU_0am9qwyqJnhKlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افتادن به التماس برای بازگشت به همون شرایط قبلی!  ترامپ ولی رد کرد!    احمدی مقدم چند روز پیش گفته بود به کشتی‌ها حمله کردیم - و تفاهم نامه نابود شد - چون میخواستیم چند میلیون بشکه نفت رو به قیمت بالاتر بفروشیم!  می‌د‌ونید که بخش عمده نفت ایران در دست گروه‌های…</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6770" target="_blank">📅 12:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6769">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BmC6xWP8Qj0-jgUJ2n7mOt2I0GdeCBVZku5wSpC-fMeaXgPCbVAVOFbR3TlHzqxSB35nFPuzP9kZxRqjgkkOxc2xZXdgGx_DDSjBYDoRjWQB3lqNeY-C8NJyE6ibaVy4JZe5LqGcrWM0VfAsWKryZscr_uwI_NYqdA2HOmT85mLvrYpTrdDE81nv9iOa0EaRq3dP-f1mLSB3fM4mR-THw3PySE72fJmFijobFTMY-avSiFi6w0P5jond_TMIFA1bxoN0stx12GDyR8bDXGoaYdxoMySCQFzLbcC0UfX1y-PJ5Q1qmA20F8VB37eiBcg08Se-HiKUSVgiosJ3cy7uJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد  تا به دنیا فشار بیاره،  اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/6769" target="_blank">📅 12:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6768">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89284f5821.mp4?token=J2npwkbKQ-gO1DG-zh_l8hwTZTI9jvmhLRLDuMC3PaakcroDhTo4hAC9ZuMHIdELVI9NNxwjh9Yyv1DSivr2T93bO-eApZ47MMteEMTp3fP6qIXdF2zshVHlPJgqTAbqoPGAxKQqpPQehzFdO00sl0MVKjCvwMd6ZIEEMi73YTFyQxTPvPKv9-22HeaAEg4gcn1g-1GiF888VcnvVC4nOxrpiyOBb7XBuz3xFIJ6AZr3Y7woDtpkxTsZTIyX2v1xwiRxr8sx1q-qhKM_QxmpKStM1bTsy7wHiZ-IPpGpTLcyYUw52FVuRW0wa0yk2EbTGpBc1F2jVeisS6UHyzI7OpMVKyKHz-iOGqqcv5yISRI-CvGJV3rr4Vgk8xsxUNyIlPN8rrmQ5lPSpvKohoP3Bdf7yuvhXKQ9Lvr3oSSDHGJ0fehUNvrMPpuIEqjahhtnqll4Ct0Vfmq2uC28jVqmQAjWgqnTbsYrCaNPTovQbIHIDQ-aeBLXuPMaccHbLe_eRNs18gvCdPSkLevVE0-VZ7CqR23h3soZVEvEYf3sLRfnvJDqPDHKV7BHnTdlYgEzczTdAW1ux_1dKxsn0FFa0JlgM_GBtB9p8_EPxKSfbogCCoXALpxaMqKJNAebgRVd7lNa8QvguCK-f9e_gOP-BGCd096I1xnDEGf2aK4phJY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89284f5821.mp4?token=J2npwkbKQ-gO1DG-zh_l8hwTZTI9jvmhLRLDuMC3PaakcroDhTo4hAC9ZuMHIdELVI9NNxwjh9Yyv1DSivr2T93bO-eApZ47MMteEMTp3fP6qIXdF2zshVHlPJgqTAbqoPGAxKQqpPQehzFdO00sl0MVKjCvwMd6ZIEEMi73YTFyQxTPvPKv9-22HeaAEg4gcn1g-1GiF888VcnvVC4nOxrpiyOBb7XBuz3xFIJ6AZr3Y7woDtpkxTsZTIyX2v1xwiRxr8sx1q-qhKM_QxmpKStM1bTsy7wHiZ-IPpGpTLcyYUw52FVuRW0wa0yk2EbTGpBc1F2jVeisS6UHyzI7OpMVKyKHz-iOGqqcv5yISRI-CvGJV3rr4Vgk8xsxUNyIlPN8rrmQ5lPSpvKohoP3Bdf7yuvhXKQ9Lvr3oSSDHGJ0fehUNvrMPpuIEqjahhtnqll4Ct0Vfmq2uC28jVqmQAjWgqnTbsYrCaNPTovQbIHIDQ-aeBLXuPMaccHbLe_eRNs18gvCdPSkLevVE0-VZ7CqR23h3soZVEvEYf3sLRfnvJDqPDHKV7BHnTdlYgEzczTdAW1ux_1dKxsn0FFa0JlgM_GBtB9p8_EPxKSfbogCCoXALpxaMqKJNAebgRVd7lNa8QvguCK-f9e_gOP-BGCd096I1xnDEGf2aK4phJY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0493705c07.mp4?token=WHZ9gL6clUADdeyz6sjNjVc6PfslHCtNOy1qqzOWX0FumvSXB8yMD6XeuXwMTBkSKFGbbZb9qxM2EU5iWHClA9bRbRolbckl4oklvgSU93BDcU-yHEpRhpVZcro6vP1KbIqJH4fXy8miLsnfIOO2DRsvdaJl-3COS4zV0D0frkFMApQ0SCB7zEge6sp1YXxF76btQNeuUlQTCPmsvDXcbaKKnPZtaExELYCrMTCBP5zyR9PIFD6DduiyZ_jX-llkGmBHuJGts49jJBwTwFj-tM2jQHLTZ8Rkoq9VGg44fuTHoj2KwCJm6bH-ER8V5d1z5nj9sut4smKcXXWAGEd_eQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0493705c07.mp4?token=WHZ9gL6clUADdeyz6sjNjVc6PfslHCtNOy1qqzOWX0FumvSXB8yMD6XeuXwMTBkSKFGbbZb9qxM2EU5iWHClA9bRbRolbckl4oklvgSU93BDcU-yHEpRhpVZcro6vP1KbIqJH4fXy8miLsnfIOO2DRsvdaJl-3COS4zV0D0frkFMApQ0SCB7zEge6sp1YXxF76btQNeuUlQTCPmsvDXcbaKKnPZtaExELYCrMTCBP5zyR9PIFD6DduiyZ_jX-llkGmBHuJGts49jJBwTwFj-tM2jQHLTZ8Rkoq9VGg44fuTHoj2KwCJm6bH-ER8V5d1z5nj9sut4smKcXXWAGEd_eQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موج جدید پناهجویان و مهاجران افغان
به سوی مرزهای ایران</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/farahmand_alipour/6767" target="_blank">📅 17:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6766">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ahPJKqBWcYFRRmTQzpY17OQ7ce0ZsmfaAvRD5u8F1aQMu-tSSxDWzaOJyuDvxnx4Cakx4k-B8nn--kKDO5xwiWt3So4icgJkwpGsn5_SiiP3Du2SMjuAP84r_b4KINngtYxt3GOy8Pc0yGXYdAsMK9dqy46BwsVOAzS_Cn-Y3qO1Xtbl01YBriAUk1KKL6GanGE7lUTtwuWfpx5LpPKJg-n6YW9IJfnm1uqVH_RFamjuYzKPelojejSpl1pmj6_YokFGBwn1EB38DBwkz290OJ2jqGz0UxM79UoYWEpRqcg6n48ZmqoDGmlEXHBxKtZ0wpxK-vZndz6J0H5HetTsGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو و این حرکت یادآور داستان‌های عهد عتیق است!  شجاعت و جسارت فرزندان داوود!  که در عین جوانی و نحیف و خرد بودن،  مصمم و بی‌هراس،   مستقیم به چهره دشمنان خود می‌نگرند!  مثل داوود، نوجوانی ظریف و آواز خوان!  خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه…</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6766" target="_blank">📅 15:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6765">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=EV4rWpnSrpZuGf1DF14EM3bZ0Y0zf6ix6SMsRSm9cs1H0JZpK0oP8fHuq0hed4jKxpnxsB4HaLzwx4I7nCv7b0hx43YntkPmGwU51_qCWc1UYQ5Q2aXHBS16wtIVDwWaPSYR6GIa2qxKgdp519Luk3kV7vY_DTGxlOr5oW7Htc_NqZWjAn5YzTQkwcCnJDunYbyj6R7JcVZS9q2D3pObhZ5HYb05yPr0CZcSm2jbahyROGGtBwi4c-0nXpOqp1bkMP3uDAV9997-zr7ILrtlwFLvqsuI2tB-iwsdZIFW6CXXOf2IKqqoSE-QI6wvB4kovP08-VnuKtyalsUG6O0EJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=EV4rWpnSrpZuGf1DF14EM3bZ0Y0zf6ix6SMsRSm9cs1H0JZpK0oP8fHuq0hed4jKxpnxsB4HaLzwx4I7nCv7b0hx43YntkPmGwU51_qCWc1UYQ5Q2aXHBS16wtIVDwWaPSYR6GIa2qxKgdp519Luk3kV7vY_DTGxlOr5oW7Htc_NqZWjAn5YzTQkwcCnJDunYbyj6R7JcVZS9q2D3pObhZ5HYb05yPr0CZcSm2jbahyROGGtBwi4c-0nXpOqp1bkMP3uDAV9997-zr7ILrtlwFLvqsuI2tB-iwsdZIFW6CXXOf2IKqqoSE-QI6wvB4kovP08-VnuKtyalsUG6O0EJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rWuIMOhMYMiQRV3Oa6stFLckxiuhuAGhpzXzF6oQuQll9g6z7Ievq1dUqdEL7d8DIXLjBCHEYsPY0437yyUuB4e_S17k2krrBPeDMA8QNAAhqimcNp1jcAMKkYCWd-MO6gHid_bz3UH8JMBAwS8InKwofX7dISmi_mpLt8sEHmxdnl7CKhSr-y2S8x8YO06eFB2r84U2NFuRhxgrXRpYCB2Np9HYKJxGpsS9WyZQqhXXiw6w1eqgrufhLG5KJEzv9-TNvOYN7n-8bpbyB71dqMbzIGO6ruoOGnMPxTXk5uKQ-lR6aTkAm-x5sbQ76wyZ3VVx63AYv7v50-V4vfBPEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.  . این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،  و نقش میانجی‌گری این کشور. (وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،…</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6764" target="_blank">📅 14:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6763">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZ7mhy54RiPHTus1pTppFC0kHjw3UtR4ZLeqUY2dTeaSKbb8Qy_EMacpepbmJaQhNOC7HQprNVrIZBFmgI04-8bytBm2EO6Yp95HAgbKwylAlIkOkDMrw6IX4JkveNZsWK2R-yh0r0EEZGFf92Ztr4hmZQ3vUesuN-8UHuep9YclwRHdnDKJKHb9uOgwgTwDYUV5BQfjK3z7YaDcZt736faMAg_Z-s0Cb7yaFRmbiae2kgU-ytQFQPN2Atf7wtfKcJPYKG_R8hCwe1ylowgkAvxkZQoOlF1E4ax5yxQwjyIi4QEcLbGktirrY1y6Ervap_KeKkP8UEI3z-i6YuGJaw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=pgQNTS1RQhwQ-6Jw_quR_tF_CH7aNUMulxOJtvN47jUv6tdVpQ-z_f6L3-Jbde1riP6KDWaPMen0RG1Eu1WDj06i37CglvFnxSEi2HcdSW2xn59PFUC7gdd1mQYGGfC6Oq4J0loHR6o7iu4BF76ERQQP3wpeUJCf834UGueCphYzcOqNhlbySx57MDbsuw1A9zQDW96ekcr3ZI_xA_oHAeTatbzKyrBidA8e_-zElgOnJcr9ji6mLe2oeJXND3wLuKC_xx10E68U61QQ8Es7TldC52nNdIwiFkwDJSw8KZ80v6T2T_TMrAWN-tQqk0GMV-NUXO_X9dE0qVQ1xH2SXU6SOLu3biv-yRK-tdl8NnGDITRCvEo2-uNP4lj-SrAdsN-hsW5UNyORa8ySXXR-NRH1qU6DkGNqOQnYij_LVIYZ6UYpJQBUvRAZknUDm86LPPGD8wG4qmOViXg258HtVoz6SMPp8l5bZ_XvThp2GPEPxoiadQ4TRTXz8vWKH_v9ZG8OguumF6IDR8N9TjnXQiKty6Ek50m5snpXzJDT4cMXUpjllGzJQ0D3LhVEMeCMxg5n9YtnZ52U1NmChVzWx3EbtJ83xs-TpIFzbdDvwPzgVnKp8311UQGTfLfJhS5sCTFy0OiXSid2Et_zEpfEwBHrxsbf3OAQoifq86pAbaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=pgQNTS1RQhwQ-6Jw_quR_tF_CH7aNUMulxOJtvN47jUv6tdVpQ-z_f6L3-Jbde1riP6KDWaPMen0RG1Eu1WDj06i37CglvFnxSEi2HcdSW2xn59PFUC7gdd1mQYGGfC6Oq4J0loHR6o7iu4BF76ERQQP3wpeUJCf834UGueCphYzcOqNhlbySx57MDbsuw1A9zQDW96ekcr3ZI_xA_oHAeTatbzKyrBidA8e_-zElgOnJcr9ji6mLe2oeJXND3wLuKC_xx10E68U61QQ8Es7TldC52nNdIwiFkwDJSw8KZ80v6T2T_TMrAWN-tQqk0GMV-NUXO_X9dE0qVQ1xH2SXU6SOLu3biv-yRK-tdl8NnGDITRCvEo2-uNP4lj-SrAdsN-hsW5UNyORa8ySXXR-NRH1qU6DkGNqOQnYij_LVIYZ6UYpJQBUvRAZknUDm86LPPGD8wG4qmOViXg258HtVoz6SMPp8l5bZ_XvThp2GPEPxoiadQ4TRTXz8vWKH_v9ZG8OguumF6IDR8N9TjnXQiKty6Ek50m5snpXzJDT4cMXUpjllGzJQ0D3LhVEMeCMxg5n9YtnZ52U1NmChVzWx3EbtJ83xs-TpIFzbdDvwPzgVnKp8311UQGTfLfJhS5sCTFy0OiXSid2Et_zEpfEwBHrxsbf3OAQoifq86pAbaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترکمنستان، آذربایجان ، گرجستان و
امارات و تا حدودی عراق،  آسمان خود را
بر روی پروازهای ایران بسته‌اند.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6761" target="_blank">📅 14:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6760">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o7Tupj-humhi_iRwTQqh3j7dNrslpgBJ-bdxzzvBxKiF4HlFrpmjJhP7lwuBTIuwOItFXulWznx6VcAhKa9Uut4YVmN4O9elS_uDU1ijzKwkaYFVAyN2ighzaWOEpzrt4SyczvoDF7tkYlqtgxJUDdzeOWvTMSG1Zse6LNy45Wc3uDIdjOdpUIJdy9E9BtYDQNuaTXAmSBHLsgYT1n2rkbWIgMYvhjKnC_Yp4MvU-iIr4twf3c_ImiYHFkA91R7VHPhk2VxiJHwpzXL_1C2X2eSDzXYdZUb9JLMuyo9_1ESHszcIhWJMlckV5d4Uif_JuBsXaN6j5-CXreoVmRTMqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6760" target="_blank">📅 00:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vLiQ4Kq0utTeE1GotqSJq5T9wCxTqBSVwsvZdNXuT-ywTvqAAKSqVYjUMXWLJH-QtzormpL6KW604RFPWPTia7S4MQFqcW540yxZ1YUXKAGj6VtSyMkfsxFZT_ClRkK5CFp6smtARZ2M-njnuMdb6s8bzOliGj6GBM4f24r9YVGUNbIAWDxQ5NO-NK4dz5Tgbvzrs_w8mtfPnzswuic8wuSBAXdjbvWGoeE-uaNnHpBu2lzuwgn7bcMVNhZuhAibHPeTOdGs6JcG5I4OMFRap07ZCjQug692dXl81t3f1qFEA5UPTZmc7KwXVBV4JByLBFednYHbGr2TvcRuvTfMtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مهدی حبیبی؛ دبیر کانون امام الرحمه:
پزشکیان باید تو نیویورک با دستای خالی به ترامپ حمله کنه و اون رو توی سازمان ملل خفه کنه تا انتقام خون رهبر شهید رو بگیره.</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/farahmand_alipour/6759" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6758">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=m_o1ZjI7YAiHUUCJgKiOprjK-MoXMiLHts4jIUlfKv0KRiTA7B-n-RroCKKVeadvtg4o7r4e6tvizzGPmcoJSY5oGxAfGqFdC5VecW9K9NZn3ShHWINSi6ur4VycnxHFdV1vxzaVqaiETDHyUG5AV23mJA9UJtHuwQ9zm8TIY37cvSgBzu7b4Hwnz1Dm8mgckxL0eWX6fYa7VG7nd2WvUypxn152pQy70rc_1x0b5EQdZrx9dW7IaLEJlP6EMVoY8_f1XuJXyuYc-buRqfAlFWOh1cRyBxNWdNJOOp2mib2K4STZ-8cPAn42OVHEQBLB4N0MNoJY1SABXvF0GUaPYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=m_o1ZjI7YAiHUUCJgKiOprjK-MoXMiLHts4jIUlfKv0KRiTA7B-n-RroCKKVeadvtg4o7r4e6tvizzGPmcoJSY5oGxAfGqFdC5VecW9K9NZn3ShHWINSi6ur4VycnxHFdV1vxzaVqaiETDHyUG5AV23mJA9UJtHuwQ9zm8TIY37cvSgBzu7b4Hwnz1Dm8mgckxL0eWX6fYa7VG7nd2WvUypxn152pQy70rc_1x0b5EQdZrx9dW7IaLEJlP6EMVoY8_f1XuJXyuYc-buRqfAlFWOh1cRyBxNWdNJOOp2mib2K4STZ-8cPAn42OVHEQBLB4N0MNoJY1SABXvF0GUaPYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=Z2Zj0kCBTn5j8KsUBQ9P8guPyLctPjFZnA4F7Sv3Glgq5610ucV1WtsiCwTtO_Y7QlzPXFNwHr8w3rSP2wcmZqB8ycKdAa1nCtrBidykxVnqqql9KhD1FR9zd0_-U1k_svBJLBvn57RQsN_mdWCD8rqbTNVdyoBT3uZ7Er44InBvt1AahCfEWmwyWY-OKNxAbO1Vipe8FQA45Qr3S6ZkAl-bYOB4nHwUJ5Ia75tdQywvj-BKxBtmCBJFGy36eDJfXlzYHl_X0YHFYwFfT2sXWlaTDrqs3n7bonf73OBdMmKNYewnvBWVtAHKiRsjjINaEqRl8ydhvGd1aaAdjNN0fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=Z2Zj0kCBTn5j8KsUBQ9P8guPyLctPjFZnA4F7Sv3Glgq5610ucV1WtsiCwTtO_Y7QlzPXFNwHr8w3rSP2wcmZqB8ycKdAa1nCtrBidykxVnqqql9KhD1FR9zd0_-U1k_svBJLBvn57RQsN_mdWCD8rqbTNVdyoBT3uZ7Er44InBvt1AahCfEWmwyWY-OKNxAbO1Vipe8FQA45Qr3S6ZkAl-bYOB4nHwUJ5Ia75tdQywvj-BKxBtmCBJFGy36eDJfXlzYHl_X0YHFYwFfT2sXWlaTDrqs3n7bonf73OBdMmKNYewnvBWVtAHKiRsjjINaEqRl8ydhvGd1aaAdjNN0fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=bmwek3j09Mx374jPomXUtiWbH3LB_ZNPQMLkAAYUrrTgMgVcW--i07MgXOrh4rDvCLsA3hiLaZGG9bBBnv5yJOWa8ig8PZqnDdoMzznabmJkCmEiw_JQyZKopxxAENFpneCUUMccf5FwVesPDMaSMdhocLJ9cqOnpq9Al2cRVeDaZTv_N_F3_q7-SrWCwLvVb7j7j0ylU3sRnLIsE4DmUQM2FXOzYALuDMhK9GBTBmieHdC89xH59LCQVB3wDZjjBbxx6WA2hP5MybzNgGuV1DPdNiJjIQ_pEDS7_Df6zVJ8rkO_Ii-JI7MQVh0hXwgEhe1fC8eZkaKqVzOCHQU7NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=bmwek3j09Mx374jPomXUtiWbH3LB_ZNPQMLkAAYUrrTgMgVcW--i07MgXOrh4rDvCLsA3hiLaZGG9bBBnv5yJOWa8ig8PZqnDdoMzznabmJkCmEiw_JQyZKopxxAENFpneCUUMccf5FwVesPDMaSMdhocLJ9cqOnpq9Al2cRVeDaZTv_N_F3_q7-SrWCwLvVb7j7j0ylU3sRnLIsE4DmUQM2FXOzYALuDMhK9GBTBmieHdC89xH59LCQVB3wDZjjBbxx6WA2hP5MybzNgGuV1DPdNiJjIQ_pEDS7_Df6zVJ8rkO_Ii-JI7MQVh0hXwgEhe1fC8eZkaKqVzOCHQU7NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uA8kKy4Jutr6lR-3Q1YI-iZbqa4dO-DKwjLuJ3T6l7dUmnx1PtM76UoXh5csergRLGA1ZiwgHPp-pKNJ-J9y765rLQ1EBYMtxzQezGkEqQbcgm4X2PbJsR7-Bn9b85lHBvMFkqD3akNtRdZGF7pVQLVnmyip54y4Y7hA0Zaj1Id2Q5BREockVmC_XTuECdwUJoYKeL4WjGyyGIBJfupCKt21aVvyvXFpYgYOmQqn0i72iZbTj4xku6s8eqmIZcxtR6Lx-Y0P4318nPdVZMs6myFw2pbIrjZozarrnXm6FFCvcoI-jeKC-ggD8u1geYJmExYjX1p0Wr7PsujsaZ9nyw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8HlNRNxKnPXO2-X_1eTpjsTruHmqctpE93mYkw9_Z5_VmGtr1UDGp-h7rnJbc8OKI9fTi9HkTMeD8hDzyle4dfi3lGC5Vk0kfrjTaXp1BZLspZxiGkgDHvJB6Smnyq3GB0sHJuEIx6rTDdhkR1c2Mz4RhBPcnPkYHRo784Os7C_AgVhjroPq-zQFzNJscy5mpGofdY_aQ75dYylVA3RsZct6wpnuAgsRlz5qlo6UnYSKzp0-0KQEWGEl-RFMJZtr-NId6tUrDwcYkqVOEdZtQ2ekgCQf3COiyllp8WRv-Bw5UZmU7SDXKicz66DILPzyiwmgPr6BI3wXkFrgHmpLmF0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8HlNRNxKnPXO2-X_1eTpjsTruHmqctpE93mYkw9_Z5_VmGtr1UDGp-h7rnJbc8OKI9fTi9HkTMeD8hDzyle4dfi3lGC5Vk0kfrjTaXp1BZLspZxiGkgDHvJB6Smnyq3GB0sHJuEIx6rTDdhkR1c2Mz4RhBPcnPkYHRo784Os7C_AgVhjroPq-zQFzNJscy5mpGofdY_aQ75dYylVA3RsZct6wpnuAgsRlz5qlo6UnYSKzp0-0KQEWGEl-RFMJZtr-NId6tUrDwcYkqVOEdZtQ2ekgCQf3COiyllp8WRv-Bw5UZmU7SDXKicz66DILPzyiwmgPr6BI3wXkFrgHmpLmF0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/67af3237af.mp4?token=wA4EVDd5YXmcMxxn6bIA3Ch11pCtjam65yIEHBmaPC_jdXVYc9JcCo-wuirf78sCFDXUwgeLbif64DPsFypqS1p03CQ_Mth0oDcBOoYdYmAiBF_1f17gO1YE1WT6YpukTHMzCcdPX-lSeMb7IIrEpT15cDRYlQ0JCzLHocyZPMMIzR_paozAQlxMq4u7mI1yuNuZDcMdw5lGVjpB_qjxgritiGLwJCZeMUZwVLPCzLa_lS6fnQbFxDmne_P_4vmOc7bnjSUDiPG7UPDyaTWHqGLkT6WYubgP1sWRnhPq1cDQ0hW6g8---a8l90ovTXOXipdfWwcUvM8nwOxmx26EPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67af3237af.mp4?token=wA4EVDd5YXmcMxxn6bIA3Ch11pCtjam65yIEHBmaPC_jdXVYc9JcCo-wuirf78sCFDXUwgeLbif64DPsFypqS1p03CQ_Mth0oDcBOoYdYmAiBF_1f17gO1YE1WT6YpukTHMzCcdPX-lSeMb7IIrEpT15cDRYlQ0JCzLHocyZPMMIzR_paozAQlxMq4u7mI1yuNuZDcMdw5lGVjpB_qjxgritiGLwJCZeMUZwVLPCzLa_lS6fnQbFxDmne_P_4vmOc7bnjSUDiPG7UPDyaTWHqGLkT6WYubgP1sWRnhPq1cDQ0hW6g8---a8l90ovTXOXipdfWwcUvM8nwOxmx26EPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم تعرض به کودک در کلانتری
نیروی انتظامی جمهوری اسلامی آینه تمام قد نظامشه، وحشی و عقب افتاده و‌ خشن.</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qnyJzJxulS0EojRz4Gm97wHLwAKU7EZIUayc_jsbEpXb9CokBf-kn-CSJ3DzFV-P47vvlsujT0UX9JALMmRrmB2CBhyZ3V3doGwGRPNGzwru8ReG6E-E1YkSpPaSBQ7ODMxoW7Hvogjz9Uhsy5F0P6r9QBhcmNY2xr-nKXODkaaqSaR3wpIrleO0e5R8IMPhwNT1VHK8CoxEnxOxuPNKr46iQcP42vlafr7QtXUsdm-0EpeGhkGKszE1NwC_9t8cLHWEkV8cPoW1t8rCvwShWlPqW_uuAgWZS5zW_lrBG-v5YfUVkKHIfaBW9YWlVqNdzRHAw4LsqEkWAdJy4rbbGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=XSyzn4Z0ku3H7O1ldyKn0SAOSCRtxHVZpsZTNYGMBjauNQ2jnQFNvQgY0KiLY50gaJC2XKKlUTP35tzqUj3X-D1JOuddr_gfOMFvBnBA73nubdOkuAf_i8oHJBJvSrfSnvyjFDFSgkJm9KQN3s6cSKDFvfJ15A9Fc1Ic_S3Rt7eG1y_JopnG3jnYbq96N2QqP4hAuDLhXOd3asRsypiBfjS-9Mec3OwbNnIBDneFIA_fOYItU0AydJf8O1qYQu9I5qHNq3FdO7pLJwZHkD-Sr3UDJIPdOY16aLcucqFZRJfJWNVpl4wxfqsCfwkeiN0Urq1EgosFOQWZMFu1HfWZuWyLgb1Po-2mwb2IAlLqM3qyIeWAyslwBqNzS8Mw_6dJsSl9c_9D8__ifaGA3eqTWBMJFWQak25AqBiDUJPnUF5yYkkKo8HbEtNKHwQhpUuORUNbsoOw5Tf7HHudy9prtjD9bgZebY1EirPzOL_A93jyhPpr2u8I_deyuXALlI4vNQjYWeWX5x8_T7trc-8WZvWgMRRoHXOhpATxk4KGcCzd1jG1SBk5cWlTURgjd-GyXzAklKOWDXM1rW178vqgeVhogNO4CEabB_WLOQ5CAxJa1eyreJbruN4KGGXp12f27fPDGdYtm5kf38kcZhGcskLvlaBC64XdWIA2c9kHSyc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=XSyzn4Z0ku3H7O1ldyKn0SAOSCRtxHVZpsZTNYGMBjauNQ2jnQFNvQgY0KiLY50gaJC2XKKlUTP35tzqUj3X-D1JOuddr_gfOMFvBnBA73nubdOkuAf_i8oHJBJvSrfSnvyjFDFSgkJm9KQN3s6cSKDFvfJ15A9Fc1Ic_S3Rt7eG1y_JopnG3jnYbq96N2QqP4hAuDLhXOd3asRsypiBfjS-9Mec3OwbNnIBDneFIA_fOYItU0AydJf8O1qYQu9I5qHNq3FdO7pLJwZHkD-Sr3UDJIPdOY16aLcucqFZRJfJWNVpl4wxfqsCfwkeiN0Urq1EgosFOQWZMFu1HfWZuWyLgb1Po-2mwb2IAlLqM3qyIeWAyslwBqNzS8Mw_6dJsSl9c_9D8__ifaGA3eqTWBMJFWQak25AqBiDUJPnUF5yYkkKo8HbEtNKHwQhpUuORUNbsoOw5Tf7HHudy9prtjD9bgZebY1EirPzOL_A93jyhPpr2u8I_deyuXALlI4vNQjYWeWX5x8_T7trc-8WZvWgMRRoHXOhpATxk4KGcCzd1jG1SBk5cWlTURgjd-GyXzAklKOWDXM1rW178vqgeVhogNO4CEabB_WLOQ5CAxJa1eyreJbruN4KGGXp12f27fPDGdYtm5kf38kcZhGcskLvlaBC64XdWIA2c9kHSyc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NcKReCeVXCp4eQ3UeY3NNaDXeGsmM5zxwh4gdindls-RCSrbTSBH6gjueIikagrdF3WhyHOYJrgJT7NDtyRhjUwc2lqiqiMQPltKWl9mF6pRJW0vqjXzFwROnH5zJik5AxWq1ArG6rX40WZOtQ35NpASGjrk6Gl-NyDyJLH6-6Q9pJSADDkU_sCSR5FVwbbOY390LI9YEj7zCc9SVIBobnHyVGjY1MoUB9NJh3zQlh9KRK86zZZ1QNbMGmS9f3lBqsw3nxPwHsk-kcvEn2K1ooP1i7kn4tbnR15h7DIxtCpEYrIO_1pRI00uw-8FmppmbbHZK5IaPtmhi2cTeYMzgg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=b9Vdt0hQau0ciMCro5tai_ftvYhGpi20PtG4cmXQBglDKmkaG3fMu4YklHBU1J6xAqYCMkVvR5OrsIjghUJaarvHiePUe636Ivz0VmDbizbWfnxc16eeFgXOZVE_aJGX7ks9ybpq1jhZVKrhGLrr2joaHfq6bTyllrESQwihk2jJhVAf87svUVgT1FBNFe2-G2a7I9GSOHEb6O7D3J6HP__W48Y-mhRJlh9yZIj1L99kA4prVg4Al0Po_4LYC9dreUty-YcueZgn-se5Ihc8Xm4q5BQGu1h9rVFiwEGiRmrCuZsZkEZafGUUm_I37LLToW2J4wtFXhoMAYnjepNeZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=b9Vdt0hQau0ciMCro5tai_ftvYhGpi20PtG4cmXQBglDKmkaG3fMu4YklHBU1J6xAqYCMkVvR5OrsIjghUJaarvHiePUe636Ivz0VmDbizbWfnxc16eeFgXOZVE_aJGX7ks9ybpq1jhZVKrhGLrr2joaHfq6bTyllrESQwihk2jJhVAf87svUVgT1FBNFe2-G2a7I9GSOHEb6O7D3J6HP__W48Y-mhRJlh9yZIj1L99kA4prVg4Al0Po_4LYC9dreUty-YcueZgn-se5Ihc8Xm4q5BQGu1h9rVFiwEGiRmrCuZsZkEZafGUUm_I37LLToW2J4wtFXhoMAYnjepNeZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bvUH1ptSuwZcg1Z0tA4-kZVHeVjAOOIX0KPB10UlCjBpw980MZu-QhuUH8rfPglV13Mxyr553mxI44pzJJgeINWPHUORDCEjkVtulIYggjqib23GUKAqNN8WPrpl72DAZM0BKf77wh2Gtzk8DAucHXy5YNZjuXG8VQqGF0t0KWAH1QhO2XDGA7UujHbKtwn4t-sWF2F5zSXQNJMMA93Gkikt2XWsjHxXmFzmIr_ylMpvtKQUIgLM8erZWZjb5dflqUdWlIyCJ-EsU-UYn3-ey0ncGd4ponD8sbpkmxFPq0QIxEkleVNIdTrXyW5WgBooQmsrLStKtQJ2CCpPXRKB4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c17bp1kRvdv6iojSwM445xMepZOnMDpd8bbXC4zdQyqJEPRD-Ak8H16TbfFUQE_bh_QYTxRLWtQU4q4DXXQoCqI7aCaDhTGdiCwVLK5uUK0lbjcdGbVFtkrpt8SI4wwK8DjGyPkWq9RPihUjsACgF-rz1EpyZSLLqpBm8nvIUv41CNbHPjdAfJ1fQ5X3XXkWYFwFHaoCk1LZuxcNRjTaHmX-VJsR4OCMIVZTG7ZY5N1uFA-8H0adB2B-vrJgys6usrEPsPSBNzoVuzlPhvpVA7q2kfhMcKC4uUhG9404W5fN-gkmwaeWeP8ApxC4rAF4Si3PlSDotyEUI9DmKIP1vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q9hrIWZSlZZt62Biwob9ot9VcxiQnu8pHzR07GskbfBvPK0yp_NINJBfS-GjxqOIo6_Dd1L6r8BeXeOkFBFaszG4aM35gGK-gb2pTe-2fzMzdKofe4HZK1KOFxanasRAyfEpFVhKJ3M-wtWZgVJpyPEbW3NBucGPJZLmzdHlNXRtXFrRttoVpqpV_38R5-7CiE4uIzsduc15ievtH0eQ6_WYi0yhBqugrjpEuMWHYsDLe_HVEkMBPyh5qsjgG0nNjWgTZDugj-6ZoAxuklIxwXfLZAwdPZsW5Bu8o6l_mA68LMbKrOznJcvbV4s5iycI3Gh3uVGI0s4wbkgeGabMMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=NuQ0UtF8fX6fD7McPMetkKpqLQ5-Nzx0QMtNBt5gDmQW_jIJa7g0IHw0Ei-9mXtibLmmJkUB7Jv75Lq5ftd5ZqKCRZOXnW_ZTk482trp_uXXLJD5AohABOlkh3jjiT53nSQmJk6MfnkiZa1FHzE7HijI9AVQI2EEAJ-eJlo1vTH5gtGaS-KHHSwXF_KFHhUuKxjOvht9LRTwRjXt_lBD5yF4n37USWMMHgNKw8FQ_Yu0JgpcU0cjO1dQkWlZmVwT9AIIDkorPp8u_YtTqr9A27dusgkThoY8IofxSMTif4TtZOnjL1sFVw3x6GB9PxbHZdVXxkLYMjED7Y1QxDpJ4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=NuQ0UtF8fX6fD7McPMetkKpqLQ5-Nzx0QMtNBt5gDmQW_jIJa7g0IHw0Ei-9mXtibLmmJkUB7Jv75Lq5ftd5ZqKCRZOXnW_ZTk482trp_uXXLJD5AohABOlkh3jjiT53nSQmJk6MfnkiZa1FHzE7HijI9AVQI2EEAJ-eJlo1vTH5gtGaS-KHHSwXF_KFHhUuKxjOvht9LRTwRjXt_lBD5yF4n37USWMMHgNKw8FQ_Yu0JgpcU0cjO1dQkWlZmVwT9AIIDkorPp8u_YtTqr9A27dusgkThoY8IofxSMTif4TtZOnjL1sFVw3x6GB9PxbHZdVXxkLYMjED7Y1QxDpJ4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه
مهم اینه دلت با خدا باشه!
علی علی!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r1VEgjGOt5NGJ9jh67wa4Hg5XI4_63C-lfV1Yssr172nAwk6103RBF3TY8SBxknrey5qI6smq7zQqYVSa1bWOy-tckqwa8mnJQ3E1eYdAH181m7d5lQqv5cS5nygm3-WSYnLiQJjFk7oPldCUOGwDgp4kPrKqw46YTVxLozq0fflO4ukuqUx0QFDUBbYylsweDCb5Yy2uYPtibwJLfYxaAon6k6OLuDRHUbPnMfxwb6ufB3Yd3weSlOHLzw2jR514vMdm3DgrAM2MQfpaTHct-YxrzVmw-Ll9Q6T3ZGsb0_fZI4dQgPOJoMCr1NcKRGNh-sZLnpDYuOqjCx9wQdz9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=lnnAWgSVv-mfQZiAmpJi6zFNLr_yJrSwEbJ2z6_cX2dbw6nplsbZwjnTSh_3CXiC_kIM_FQeDlSREYZiTnrJ3jhqMUNBoYJrunSCAfZs9P-kD21c8NSjqK95t60Qm2smKQkWi4IQPdS_TPtEtwFFI9F51yarrrh0csVC3k7_06PZ0amT1gr620rUK9qlQu9daa-d75VpiZ0sZ1VM1OapcNXnMEqgNL7h62SeCWCKiOpxq70uIeDQXFxkbf9JWOCf8NkOY3s5Ji3OHZ77Ssi2OjFVjex-G4hIFTDXAsINJXsOPDkDRvWGSOvMhdgoGbUbc8AUGCTkYdjaFXWvbTBfFGmiEbAKJjpouQ_BGbO290i4imD7XclrBO8qMJDwmuSMVopN3Imp3_FWKskPUt37BbevxhdCzbwxtQA9w8rPj1WezAECNZxZ1J6i9SbR6HQABgTGnc03IE20fJ77GcK1n19nR0RGspGGQ-9dPBsVE7aAOPV5DTWztaiFz8240Ff0pgqlgKhzJXZl9xnu3GdDZRXUWQ2rprWFRCg5Peg5k-yKemdU_Q3XamuHZ2eWJqHJTgi4SOmojfNKePXkzisg9bhz_Jepnb-ERMX7Zxlb1G-SrGpoPQFMnpfLoi0pDCVeKegmZs5IV1cY9kWQYRalT5IY_lvKz_yZH4UoaODLeyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=lnnAWgSVv-mfQZiAmpJi6zFNLr_yJrSwEbJ2z6_cX2dbw6nplsbZwjnTSh_3CXiC_kIM_FQeDlSREYZiTnrJ3jhqMUNBoYJrunSCAfZs9P-kD21c8NSjqK95t60Qm2smKQkWi4IQPdS_TPtEtwFFI9F51yarrrh0csVC3k7_06PZ0amT1gr620rUK9qlQu9daa-d75VpiZ0sZ1VM1OapcNXnMEqgNL7h62SeCWCKiOpxq70uIeDQXFxkbf9JWOCf8NkOY3s5Ji3OHZ77Ssi2OjFVjex-G4hIFTDXAsINJXsOPDkDRvWGSOvMhdgoGbUbc8AUGCTkYdjaFXWvbTBfFGmiEbAKJjpouQ_BGbO290i4imD7XclrBO8qMJDwmuSMVopN3Imp3_FWKskPUt37BbevxhdCzbwxtQA9w8rPj1WezAECNZxZ1J6i9SbR6HQABgTGnc03IE20fJ77GcK1n19nR0RGspGGQ-9dPBsVE7aAOPV5DTWztaiFz8240Ff0pgqlgKhzJXZl9xnu3GdDZRXUWQ2rprWFRCg5Peg5k-yKemdU_Q3XamuHZ2eWJqHJTgi4SOmojfNKePXkzisg9bhz_Jepnb-ERMX7Zxlb1G-SrGpoPQFMnpfLoi0pDCVeKegmZs5IV1cY9kWQYRalT5IY_lvKz_yZH4UoaODLeyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=ATi0gVZM_wJlHZIOLIOLPBK19Cof3zroan_5oy6WdnljE9PjcyMrBfTMZTUDMpD9I4i4IbZeu5BEbCtx-ozeFnt2vwUnKdPeb1hYY3mWzusCu68ipjFiJpbggTL9a6eJmM4NtVaX9FXezg6dgrUx7T0baQiBvqjEUNUbbFMr8dcRRaMIVkuQ9e4lY4nm3SkDBshm4uUTfnXysayPMaUQbmdOv84_fm9dNE3IdsTKgQvvbOcGSxBIli27qvxuAjexZjc-F4XMlgLMfxxIH2d1B8vNQ03sIz0V5UQo-GxD15zvUri-v8JIjYxwsxyBpOqnIl1VCGOFVVCnAqJeh2beeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=ATi0gVZM_wJlHZIOLIOLPBK19Cof3zroan_5oy6WdnljE9PjcyMrBfTMZTUDMpD9I4i4IbZeu5BEbCtx-ozeFnt2vwUnKdPeb1hYY3mWzusCu68ipjFiJpbggTL9a6eJmM4NtVaX9FXezg6dgrUx7T0baQiBvqjEUNUbbFMr8dcRRaMIVkuQ9e4lY4nm3SkDBshm4uUTfnXysayPMaUQbmdOv84_fm9dNE3IdsTKgQvvbOcGSxBIli27qvxuAjexZjc-F4XMlgLMfxxIH2d1B8vNQ03sIz0V5UQo-GxD15zvUri-v8JIjYxwsxyBpOqnIl1VCGOFVVCnAqJeh2beeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=VpvU_sYRmOJ_Lzje894ECMhZzRiin0mr75XmlW5eTEfVY3z13LmK_5ynqztG672vR1PFFkRxhANOB4a7IBRkWHmLCYQEi6UNvJY4Qkeow3ZBf3kcHPRepyN6Z5alW1XHq3hKX_VJrAHCjKvWPYS7qAOpyCf3suPawTSen_O5q1_ayI6tiQjuoSz8HRr5JT2cHRRpR7KR0Q-qmf2hyD_s3xmRdxSlU4OkncdkawT8U_VM8Mt3fYOJijqOHbbKwspX61w5QA0zHho7HoYddq6UvhdImiX-ga3wsLEJQf29XMnT3yAHLxK-Mou7-P4q-wMMaOY4UZfI6NHlxw2c9Mm9-nFOwbpXasyGtFnbZj_prQCQ93_NYOR-zeqgbRIKzFQRsxKV1-sWov8Mw9cfpJWohDBF7UiZLrXr4yCR_Rhe20wbiHcslFaNSDJo7yT1mYpMkblMF3QD3XJ3mnPjBxQNUD5JvRaJwh44eAtcaWr2x9StHi8IXygO-HPScAne2p32eUl7C-KV8iwvptXqp3DTwGdUoPT2Cpt-QBxXcZuzGp0uTs3fPAW608MFPLiRJpK0Hj4l1ZiBz4n3UGp1QdL68XvdYwKDm_tSvBKtye6B8AYqcXRZ-6mV1sGcX5aXb_rsGE65Tkl174oFx_KTAmmlTQ2HwzYgHra1F_LKzLKbbM8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=VpvU_sYRmOJ_Lzje894ECMhZzRiin0mr75XmlW5eTEfVY3z13LmK_5ynqztG672vR1PFFkRxhANOB4a7IBRkWHmLCYQEi6UNvJY4Qkeow3ZBf3kcHPRepyN6Z5alW1XHq3hKX_VJrAHCjKvWPYS7qAOpyCf3suPawTSen_O5q1_ayI6tiQjuoSz8HRr5JT2cHRRpR7KR0Q-qmf2hyD_s3xmRdxSlU4OkncdkawT8U_VM8Mt3fYOJijqOHbbKwspX61w5QA0zHho7HoYddq6UvhdImiX-ga3wsLEJQf29XMnT3yAHLxK-Mou7-P4q-wMMaOY4UZfI6NHlxw2c9Mm9-nFOwbpXasyGtFnbZj_prQCQ93_NYOR-zeqgbRIKzFQRsxKV1-sWov8Mw9cfpJWohDBF7UiZLrXr4yCR_Rhe20wbiHcslFaNSDJo7yT1mYpMkblMF3QD3XJ3mnPjBxQNUD5JvRaJwh44eAtcaWr2x9StHi8IXygO-HPScAne2p32eUl7C-KV8iwvptXqp3DTwGdUoPT2Cpt-QBxXcZuzGp0uTs3fPAW608MFPLiRJpK0Hj4l1ZiBz4n3UGp1QdL68XvdYwKDm_tSvBKtye6B8AYqcXRZ-6mV1sGcX5aXb_rsGE65Tkl174oFx_KTAmmlTQ2HwzYgHra1F_LKzLKbbM8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=ioEP3Cmyd2sRMVr8F3ohPZnS72SkfwdmUbPKf2hvvbqu6m7Pv7XZOhAm1KxK4t7RkgmItjiD0uEY919wXMFDuf1q_PKpp2eiOeUViMe7fEM6fa7iDjX6hfEomtQSkXXN3bkRxa2HIrHEexPQyil09w-1rtTOUOlcxvezL7icxEFmR1vqzTKXDpZ3lc2Y7DVTeW3PZRYaGUlrzASCHmkoUlaXOOHJkPLjSoH_qwv_uwDJXajVAzvRxD69clFr2_HxZoiQsBZpSW1cLQvOqLAJdONwICCvBi19v4czVmkvRtYGElBX5FYAkBMbUVJp1bc1qDFdAp3S9IIU3Bbhlxzq4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=ioEP3Cmyd2sRMVr8F3ohPZnS72SkfwdmUbPKf2hvvbqu6m7Pv7XZOhAm1KxK4t7RkgmItjiD0uEY919wXMFDuf1q_PKpp2eiOeUViMe7fEM6fa7iDjX6hfEomtQSkXXN3bkRxa2HIrHEexPQyil09w-1rtTOUOlcxvezL7icxEFmR1vqzTKXDpZ3lc2Y7DVTeW3PZRYaGUlrzASCHmkoUlaXOOHJkPLjSoH_qwv_uwDJXajVAzvRxD69clFr2_HxZoiQsBZpSW1cLQvOqLAJdONwICCvBi19v4czVmkvRtYGElBX5FYAkBMbUVJp1bc1qDFdAp3S9IIU3Bbhlxzq4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EuV9OuyCrIwnhWFZKrcvRG4W9x76KbxbAGKl4Trs3HTnyGT7rXRh3SIrut30pe_FkY0fEILPeYJa7c9KEBsBuBpR8Hr3KBLzrd55UM02GawG08mUVJf6neo9wNvGz6nSUpucOSVI2dU-ZDmb_q5KJLLo8jNssrmL1tl9QRB342pTwulOoGXT3-F15BSAQ3Q2LmWD7gBt-a9D1mLF7FeBzoKt6eQA4y13vAoca_2c5Zmjr50bmZnjcUUmhJI__EO1eSn5rbkgrLQlTzPT5v3f9iB4qmhUo60ztm4TDUlGdzvgBKiM6zQR8ZFFlyLd_biin4bZo-XuFxs2gSRFDYBaXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=oMUaAOKQKPhV0VlcQ0LUU-n0ZVfHrQuXZ4lYAbGlGoUOf_KjZnzwqymbTFCsLb2BBEB_TOuPNB0nNQR9i6ixF6UivlknEYqQYFikBZWzjVVZLVi6PjQ4MZDIgna_rX_B28XuzIl6spRg_8TFNtLwNHyuUBqHpUSVQ7_yrlanbjomGU1AMOIfxKQJ7fuP1YhHCAfZpc1ska-Fj0CK8vFhhUyycR6JkQMdS_xBczkRQLmWTkyOC6PpL3YfbhVKdiBqfc2p8oXtjieGr9Yt5_bZ7r6BM0i1qrQqX7PvGi1y_zNmRZeNj5JuqPSxOOB27lgBHAh7WKS4JjThj_qFKZoqmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=oMUaAOKQKPhV0VlcQ0LUU-n0ZVfHrQuXZ4lYAbGlGoUOf_KjZnzwqymbTFCsLb2BBEB_TOuPNB0nNQR9i6ixF6UivlknEYqQYFikBZWzjVVZLVi6PjQ4MZDIgna_rX_B28XuzIl6spRg_8TFNtLwNHyuUBqHpUSVQ7_yrlanbjomGU1AMOIfxKQJ7fuP1YhHCAfZpc1ska-Fj0CK8vFhhUyycR6JkQMdS_xBczkRQLmWTkyOC6PpL3YfbhVKdiBqfc2p8oXtjieGr9Yt5_bZ7r6BM0i1qrQqX7PvGi1y_zNmRZeNj5JuqPSxOOB27lgBHAh7WKS4JjThj_qFKZoqmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=OIs-Hb-T_oSjGa9MNmIlVdiL7g5G7CEPLAB_FYo2zp71mp_UWLYWfe0-YuIh5obxwvkq5ZoXtGYcbi-TFtYDyTA_JGiKGarn_26Y2UFzYLk2gvKTYwkW0bN6-tuIKjiFJihHxJGPyRN1EjXrTpjBaDMcXbWzCFJ8F28p8S4osHXRc9tU95bOu7sHRPFqqLAQtTh2yqAVvrZ8Iu6-p2xiggXamCjzvMzDtW417m2dhqGF3ivje3aJ-aMlEqhkhHIqLpkEHhOcrwN0t9PebozdneNanJPjqEWdfneCnMKbXiuov3yqyXvKaNHN9ujm5it85CHaDRHYn3nEzTr2qK9EnHeQTIouaGiF5TEvxPV1EY3yLyR5BwaJ4aQR9Z6Mjl-jaJrGBWK3LfMBTGKNqqo84niNmOQP27jOkKHAk6SZZ8Z5uVbC2jmSj9-c_bU3VFR3ZcRDpDgx_W9KQM1fXpxwiuyALh5Y09hPlm2OtCg_J4HJ89V-BkppfFqmmU0FOEod73WF7C2AgPq5DO0BL6Dajly1S0ZOXA6EVFapZcR30Hpq0S0UnG-VJJ5dAZvrf3IIHBP_p3qJBTPu7i4vL_73XIFq15vF6HQ_Fygb9Tk9ZUDLRVMYWsu1tcflQGXGAXbA0vT-W5R6SseX3MiK44e7hx6nX2YJYJLFzVuhCM72Emw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=OIs-Hb-T_oSjGa9MNmIlVdiL7g5G7CEPLAB_FYo2zp71mp_UWLYWfe0-YuIh5obxwvkq5ZoXtGYcbi-TFtYDyTA_JGiKGarn_26Y2UFzYLk2gvKTYwkW0bN6-tuIKjiFJihHxJGPyRN1EjXrTpjBaDMcXbWzCFJ8F28p8S4osHXRc9tU95bOu7sHRPFqqLAQtTh2yqAVvrZ8Iu6-p2xiggXamCjzvMzDtW417m2dhqGF3ivje3aJ-aMlEqhkhHIqLpkEHhOcrwN0t9PebozdneNanJPjqEWdfneCnMKbXiuov3yqyXvKaNHN9ujm5it85CHaDRHYn3nEzTr2qK9EnHeQTIouaGiF5TEvxPV1EY3yLyR5BwaJ4aQR9Z6Mjl-jaJrGBWK3LfMBTGKNqqo84niNmOQP27jOkKHAk6SZZ8Z5uVbC2jmSj9-c_bU3VFR3ZcRDpDgx_W9KQM1fXpxwiuyALh5Y09hPlm2OtCg_J4HJ89V-BkppfFqmmU0FOEod73WF7C2AgPq5DO0BL6Dajly1S0ZOXA6EVFapZcR30Hpq0S0UnG-VJJ5dAZvrf3IIHBP_p3qJBTPu7i4vL_73XIFq15vF6HQ_Fygb9Tk9ZUDLRVMYWsu1tcflQGXGAXbA0vT-W5R6SseX3MiK44e7hx6nX2YJYJLFzVuhCM72Emw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M7EUEMFTIkf74I0awT4qLcf9-_iuSfcW3omoDTI4SaqxvzOddEFgsap54_ttyNW-1tddO_RqoLwOwqjhFEliOxKW_Vp2TnD--b5Shj5HTLOh3FZpPerlWMbFynbdcoDpz5vpU4Kuk6tHHgeGG34rJRQ55AiGJjOHz7g_riLs9jLhVXqzUewqk0fGXNiN7EXCvqzzacrZGbBtV2FN9a29SU1LaH01ZJafS-tS7-51WhkMJ6T-RSQZMQFxcR2lhy6Sqa0X2d4E6BDVAC-2lxAFyFUBdjw5XQzIb_uz-FStATKaqma2yujuwzHBaQJXZJdADC4SBE6xhdNtQA6NmsdQ_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=Z_S1PskbyBfudBQTQbLn-xK1gQEvUteNCdX3lAyQM3pbizsSh9IKUdyibDOUViOOARVaASKEfcQGR3FaqSF_oWLW2x3Sq47-1nAIOqtFPksAuChBaiKw3dODcw_pcXD3khgGmWA8QzWTTNvWa1TRaZIIAVvM9D68nDpUEuAitn88WMXfSq6D6wMrTpk9pBNi1TIVUqftZoh6EDwBRzQuhfwynnN8_PeQA85ULstGwZJ3Fck5ca1GicFsA1l8FKLyx7xlxGSGmN9xjHyTOJ6PKgmguiIZv14zjN1EkoCsf7sIgw2UrN-CmYzXiDorLP1x_vhr9gRN1giC7BjZq7I64nAnMrRNcWp8kujhAcH7UC4Ne41o0ShfkEHYoPHtDO_vr5oLAueSJnNvIbIJrpi8rcA_o5Kf6L6icEXc0eVwjZvP8veiSOjvkjbcvG3udmzxD09Wan3k4v2wpICwrW55wiY1GxTvHwpg727S5rgFYINKMGVSLzzz6JRgF9oaoBajRsLM0Vq6X3U8MVWWHOr0clb4uph5oY-epnNc2MEOEaK2TRLh9nClUiji0JNlZGBstBv4QPYflELCjgXi6eDqzFrVHnPeIeR4_78qcgkr5kqh9ldPEmMuX08mHkscpMUbLVe-0jOcgDY1mbjNMFCebgUOSMfHsbakwM7XHdxJKWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=Z_S1PskbyBfudBQTQbLn-xK1gQEvUteNCdX3lAyQM3pbizsSh9IKUdyibDOUViOOARVaASKEfcQGR3FaqSF_oWLW2x3Sq47-1nAIOqtFPksAuChBaiKw3dODcw_pcXD3khgGmWA8QzWTTNvWa1TRaZIIAVvM9D68nDpUEuAitn88WMXfSq6D6wMrTpk9pBNi1TIVUqftZoh6EDwBRzQuhfwynnN8_PeQA85ULstGwZJ3Fck5ca1GicFsA1l8FKLyx7xlxGSGmN9xjHyTOJ6PKgmguiIZv14zjN1EkoCsf7sIgw2UrN-CmYzXiDorLP1x_vhr9gRN1giC7BjZq7I64nAnMrRNcWp8kujhAcH7UC4Ne41o0ShfkEHYoPHtDO_vr5oLAueSJnNvIbIJrpi8rcA_o5Kf6L6icEXc0eVwjZvP8veiSOjvkjbcvG3udmzxD09Wan3k4v2wpICwrW55wiY1GxTvHwpg727S5rgFYINKMGVSLzzz6JRgF9oaoBajRsLM0Vq6X3U8MVWWHOr0clb4uph5oY-epnNc2MEOEaK2TRLh9nClUiji0JNlZGBstBv4QPYflELCjgXi6eDqzFrVHnPeIeR4_78qcgkr5kqh9ldPEmMuX08mHkscpMUbLVe-0jOcgDY1mbjNMFCebgUOSMfHsbakwM7XHdxJKWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=T7JFOYG-foQwUt_YqWUOAhMg4iXPnAnrM28CTGKmR7gayea4A-lA5tvQtJOv344cNQ4F4kS6po8Op-XHACz7fKNvtqW3J9N_JyoJ_wK5OXSLaONR61oasJaLVqMJrS12NOBA0RyrEC1x9DqXXe_KSBjPWbnh6GrLNcvM61CDDGwjySLQE-2PZ9bzxCr--arjM4hTMSfB5QpBMWoyc8N5Cs73FZqygtFrOFAJaxrV1tgnAsmywticdcBhn-Qwr847kBxomEygwI0teycYKnXFyMK0qcjrUSNaI8XovKQjO39Bygq0JgTNdc09_XXgYwspgfFg1IoHwVwyCFW_HGz_YkmweFTWhQ2srWp-68wiuSnmfTgW9XD278h-WeEut5d91v4xwBbhc4PQDVZ5p64ls5GdTz6pBvbk1VPUA4GRcvWszriet6_3nh9EK7PVOkQUIfZWgXqGevGSCzOGCzKsLDg4ULpQsJ9OytgAbVCuOZt-Z8TTmOAnWBMVAxwgwxmFrJY3NiN2z22fAa3HgYjTidXjSnkzvvq2qm_TQ5lKWLoCCcOKnNEuKWXy6CFT8qMY6yFSX-1aCqOL9mfaJ32aUMAH3cysVVtdcsMoghlAp8fUcPpIISYiCWO85I_0ffBN2vjk_9rqWzaCz6H_ONqQDVj6zrU1MJUGcuPERQTc1Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=T7JFOYG-foQwUt_YqWUOAhMg4iXPnAnrM28CTGKmR7gayea4A-lA5tvQtJOv344cNQ4F4kS6po8Op-XHACz7fKNvtqW3J9N_JyoJ_wK5OXSLaONR61oasJaLVqMJrS12NOBA0RyrEC1x9DqXXe_KSBjPWbnh6GrLNcvM61CDDGwjySLQE-2PZ9bzxCr--arjM4hTMSfB5QpBMWoyc8N5Cs73FZqygtFrOFAJaxrV1tgnAsmywticdcBhn-Qwr847kBxomEygwI0teycYKnXFyMK0qcjrUSNaI8XovKQjO39Bygq0JgTNdc09_XXgYwspgfFg1IoHwVwyCFW_HGz_YkmweFTWhQ2srWp-68wiuSnmfTgW9XD278h-WeEut5d91v4xwBbhc4PQDVZ5p64ls5GdTz6pBvbk1VPUA4GRcvWszriet6_3nh9EK7PVOkQUIfZWgXqGevGSCzOGCzKsLDg4ULpQsJ9OytgAbVCuOZt-Z8TTmOAnWBMVAxwgwxmFrJY3NiN2z22fAa3HgYjTidXjSnkzvvq2qm_TQ5lKWLoCCcOKnNEuKWXy6CFT8qMY6yFSX-1aCqOL9mfaJ32aUMAH3cysVVtdcsMoghlAp8fUcPpIISYiCWO85I_0ffBN2vjk_9rqWzaCz6H_ONqQDVj6zrU1MJUGcuPERQTc1Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=hzdeFcbbleGY_d5R8L1zhx4BsPEcq7eoI6I7UzbfWlHtqn6KpfVxGr6x0lo7qvc7i02OMWIIkqBYCB07P0LMpWROrj8d_j8D3je0nEB42l2pFyX3uj7MUs3viQCDazAny2MlIEiAg0u3TOlUkwSeU9Tgh5goLNdtknTjloCgFX_tLStt_59UbjO6lLB3QSGtwHexp09ppw2zhd9v4TMEfzTnonveimybzkIvM720yVBp1cDMGMrDHcAY0g7aLTopygDDoxoEHIILrmDxe2sZAcEu_7l6GsXFltT0UHeXvHeO9QFzvjj4WT18uOH90ADbuUJp_4m8qEsukX8mupWzxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=hzdeFcbbleGY_d5R8L1zhx4BsPEcq7eoI6I7UzbfWlHtqn6KpfVxGr6x0lo7qvc7i02OMWIIkqBYCB07P0LMpWROrj8d_j8D3je0nEB42l2pFyX3uj7MUs3viQCDazAny2MlIEiAg0u3TOlUkwSeU9Tgh5goLNdtknTjloCgFX_tLStt_59UbjO6lLB3QSGtwHexp09ppw2zhd9v4TMEfzTnonveimybzkIvM720yVBp1cDMGMrDHcAY0g7aLTopygDDoxoEHIILrmDxe2sZAcEu_7l6GsXFltT0UHeXvHeO9QFzvjj4WT18uOH90ADbuUJp_4m8qEsukX8mupWzxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=mM_LGO5rgIMQ41l0MyHx2CqUNA3Yx_0VlTqK8XISxBKB-pd7v2JEPCzWKbZS3uLAQtBt1t1Gw5dG30hBMsqgp0VGLC8FhUcfkClesO_28_yAHUgqU47njH01Mp8Rs1M7pIRkxE1_Fo9wQgTw1j2iiCIMDLe1Mk4iGZSKJUnxxkKrZoFsOQKl3roFkJHwLnWLPdhX92BO_OHnGxFVf8jsImSea0O43nCUlk1pDj9ij1O9VZR0ByybRHjLKL9sg7s_AYIyKPi4qvUZ-VrMjZIaETL3GC9wObs5mqx1WoRpNOkPoNQpWz6LXxwV4O6P4rZfl9ypZr6DiLBAqllB6WrwZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=mM_LGO5rgIMQ41l0MyHx2CqUNA3Yx_0VlTqK8XISxBKB-pd7v2JEPCzWKbZS3uLAQtBt1t1Gw5dG30hBMsqgp0VGLC8FhUcfkClesO_28_yAHUgqU47njH01Mp8Rs1M7pIRkxE1_Fo9wQgTw1j2iiCIMDLe1Mk4iGZSKJUnxxkKrZoFsOQKl3roFkJHwLnWLPdhX92BO_OHnGxFVf8jsImSea0O43nCUlk1pDj9ij1O9VZR0ByybRHjLKL9sg7s_AYIyKPi4qvUZ-VrMjZIaETL3GC9wObs5mqx1WoRpNOkPoNQpWz6LXxwV4O6P4rZfl9ypZr6DiLBAqllB6WrwZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=ML7fMgeXcTxA3nQC2TjdkVT59HHUItKdCzlIAosr08aS8gX4-GAdJmV3i_jYWE0DbuPK6921Q5DtQ0MGeLaJTRE1_-OTIxjD78W94_JpPQnrTOLC8NWzJF3tOycP0NeUdJNqEdTIkvjcdZFKaszHoHrulot4ZhgBCNjh7_KexurmGpTTyK4gJqNNFArcquHRAQaiz2h1qbtvEOKHNXoVYLeFe9zK537CX_8AV_QhJUFziQmI4XeYwu7udErngJIPBaxnyD7txwNVFGoW1urtE0wxgLNWs793A83kmXHuU4-GSt_7almHyW-Jc5vwUv_1nhdQe2x2TZjADSw-mnkzXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=ML7fMgeXcTxA3nQC2TjdkVT59HHUItKdCzlIAosr08aS8gX4-GAdJmV3i_jYWE0DbuPK6921Q5DtQ0MGeLaJTRE1_-OTIxjD78W94_JpPQnrTOLC8NWzJF3tOycP0NeUdJNqEdTIkvjcdZFKaszHoHrulot4ZhgBCNjh7_KexurmGpTTyK4gJqNNFArcquHRAQaiz2h1qbtvEOKHNXoVYLeFe9zK537CX_8AV_QhJUFziQmI4XeYwu7udErngJIPBaxnyD7txwNVFGoW1urtE0wxgLNWs793A83kmXHuU4-GSt_7almHyW-Jc5vwUv_1nhdQe2x2TZjADSw-mnkzXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ویدیویی از نخستین توزیع قند و شکر کوپنی در دهه ۶۰، عبدالناصر همتی، خبرنگار وقت صداوسیما و در میانه گفتگو با مردم به مصاحبه شونده می‌گوید: «اگر قند و شکر کوپنی کافی نیست، باید کمتر بخوری» مصاحبه شونده هم می‌گوید: «اصلا ترک می‌کنیم، ضرر هم داره ...»
همتی در این کشور خبرنگار ساده بوده و شده وزیر و رییس بانک مرکزی و کاندید ریاست جمهوری‌ ...</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=dwvNckosWkbwXjI7aqCAmGPIXYWka94kkGNGMSX-s0XKGFU0eX_bhQ3eaJP1BTn9v0-E3WIH3WAfV4FaeqJmro_fF_QEKvEN6BzLgmgljTYm6XpSioyD0QFXTIgly-SYi5YOjdG7xLN4lMg-c706ij_u17KiE9iBCF6OlJGXnffIYn_wQ53ivMGuE1yJnW5ziPoajd5pmdmcrxcWPx4gfGNX7UAqT_1b1rniPL9syi5omxm03IkXn-6rlGSNchceFhuXnwoK--uj4cVoVGHYoPzZsctSI3zzuqigViwHD50FMk297Gzbl2bwikMb74zu5oNVZL9lClfSUJ17RuYHNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=dwvNckosWkbwXjI7aqCAmGPIXYWka94kkGNGMSX-s0XKGFU0eX_bhQ3eaJP1BTn9v0-E3WIH3WAfV4FaeqJmro_fF_QEKvEN6BzLgmgljTYm6XpSioyD0QFXTIgly-SYi5YOjdG7xLN4lMg-c706ij_u17KiE9iBCF6OlJGXnffIYn_wQ53ivMGuE1yJnW5ziPoajd5pmdmcrxcWPx4gfGNX7UAqT_1b1rniPL9syi5omxm03IkXn-6rlGSNchceFhuXnwoK--uj4cVoVGHYoPzZsctSI3zzuqigViwHD50FMk297Gzbl2bwikMb74zu5oNVZL9lClfSUJ17RuYHNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=p8EncCc8COEBObmKgOH3pgRzJhb2vbNHUfQRlIo-FLnWI6MrFVUNCoZ6Y9kf20sHE1YP2tljF-LfOvQLkjx8qD-bhylvAvLLFCO8w3hkARaLdTuvSmnJ_wVKUmr6WHbLXx_4Cy_hjJ02m8c7_QTH4uWIYNaSpocQNdv-igv-qCJweu4g0SwEvh5ZA4HMHg7jp6ohDWVajfONcgSfpsLZdj-7EfCgiK427fp1tJXmsrDbAnYOZHevjqdseHXnTS3X2gtxWzGdvlZGTS7LBTK8mkuJGB8zBufSzHtMSKJ1ORfMSBM_-TusuE6ArJfc8y7GGbifENPZiy-TNcykM2waQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=p8EncCc8COEBObmKgOH3pgRzJhb2vbNHUfQRlIo-FLnWI6MrFVUNCoZ6Y9kf20sHE1YP2tljF-LfOvQLkjx8qD-bhylvAvLLFCO8w3hkARaLdTuvSmnJ_wVKUmr6WHbLXx_4Cy_hjJ02m8c7_QTH4uWIYNaSpocQNdv-igv-qCJweu4g0SwEvh5ZA4HMHg7jp6ohDWVajfONcgSfpsLZdj-7EfCgiK427fp1tJXmsrDbAnYOZHevjqdseHXnTS3X2gtxWzGdvlZGTS7LBTK8mkuJGB8zBufSzHtMSKJ1ORfMSBM_-TusuE6ArJfc8y7GGbifENPZiy-TNcykM2waQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=qyrNbewTBdH-zue9Anj_7yIfBqz_UlAFb4Z2HJ_Ownu8QGtRjTQumeiF-X5lODCnbKcStI05yyL902FPJKfN37dg4n98M0lKme73EXfq6azs79z7LUDU_GU2b7hpvAYcRT2x8Uxiz2KoElXaAgyQ7dTLxWUClOHtbPOw4Hhxvqs8_5N1tZ1yI5iDP5RCGVu8Koiuh5XlDxXkQMa3xjiemGjHtyOxY7Uxngl3GaYJqvI84REXGC9SeOF087zqkzTvOqncZsQdZtA8x-aieH9s6Hf_oiHb4ckYSsaD_cxIB4wCtrdUVL2j4CS4UiPDRciCxpvQROqNkrb33gr6wbtlaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=qyrNbewTBdH-zue9Anj_7yIfBqz_UlAFb4Z2HJ_Ownu8QGtRjTQumeiF-X5lODCnbKcStI05yyL902FPJKfN37dg4n98M0lKme73EXfq6azs79z7LUDU_GU2b7hpvAYcRT2x8Uxiz2KoElXaAgyQ7dTLxWUClOHtbPOw4Hhxvqs8_5N1tZ1yI5iDP5RCGVu8Koiuh5XlDxXkQMa3xjiemGjHtyOxY7Uxngl3GaYJqvI84REXGC9SeOF087zqkzTvOqncZsQdZtA8x-aieH9s6Hf_oiHb4ckYSsaD_cxIB4wCtrdUVL2j4CS4UiPDRciCxpvQROqNkrb33gr6wbtlaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=X3z3gRHL2Uy1uc_vRYm1QQZXAWyzCQi4_GkAHjqxyVWbhkUVTOHiTnVLD6AN4ZTBeAJTwmn1aieqQWQQULJ8Vb4RTtNiQC4IROlf-Bej6794N0G3h1Dbugcp7-UcnjCzql7lnsIbpJBzi17gTS-k99kzfi4EmxU8owK0vDPLktMrvIyYS8s7ziMK4L0ZEYLiElfYD7DFyyb5U9eg431E7EMhxAWkynzQDksjnfgKmeTdHqxD6f3zYmV-5bXxfyd0oCKETQqPJJpCwNP_9U_H2QwF0sSJisk9H1weqfqYFQ2t8cCn0jkzwiawbS6Jg5A95XMOPS8nnvS6C5E14CUxVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=X3z3gRHL2Uy1uc_vRYm1QQZXAWyzCQi4_GkAHjqxyVWbhkUVTOHiTnVLD6AN4ZTBeAJTwmn1aieqQWQQULJ8Vb4RTtNiQC4IROlf-Bej6794N0G3h1Dbugcp7-UcnjCzql7lnsIbpJBzi17gTS-k99kzfi4EmxU8owK0vDPLktMrvIyYS8s7ziMK4L0ZEYLiElfYD7DFyyb5U9eg431E7EMhxAWkynzQDksjnfgKmeTdHqxD6f3zYmV-5bXxfyd0oCKETQqPJJpCwNP_9U_H2QwF0sSJisk9H1weqfqYFQ2t8cCn0jkzwiawbS6Jg5A95XMOPS8nnvS6C5E14CUxVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rig3DKnkQPwCfVYFRTiIXvhQNawiPOkHY3VcY4hVUWlLaatRt_N19OtOUcGzYayQ3QgbgMDfIbNcejmDr209mD2yN8yC-71olNHTVl0qapMEdeVDNYl0w6vbT5DBrHLR0uQAy6Z6rgCTMw3aVAGxi5IIeJFrjF4T3Bi-iCVOBkU0-QrekduT72bgmQ7YgGBGXvD7QMxH69tVrelQJYpUFs9uBpo3OEDVq5pkcle7jLwJwJEnzfq4yd4jZI-2l0IdnPMTm35PK4YwffJtYEWKqAQt8H8NeV1QvAJKDiuKGOQEhDcFiGfXafMoaJGZI-gVoNSqOZQIgsVJcVbo8x4pNQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=JRSZ77K6ifMquc7wDFVRuPcEaPFS_QE1n05p8FMx385tJlkvnmPrX8y-7TLJ78I4iPXw7HGsDPwR2yz8vIn1IXAChzXImSxj9cKI-K1dYOA1qnuS3ceCciojG6Xfn57F6Rgybnc9PB6cbURXjBnOibfIx4H5lQH17m-G8Nm-BTl7jPEGPBdkcWUG3IkTHW6pJwF58IGZ35wdbORNmqt-pmhYOk9YIQx9TWJVA0E7pYZKAPCe2vLvLdinhhdeuPVpnVIyoKqHBV5JPH01TO81AxE-r0m-mMlsB40iZ9Kn5yhc7Iu9Xda9f4ZaQzitqdp3ghgfH4SSUaF0EY_U3C718g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=JRSZ77K6ifMquc7wDFVRuPcEaPFS_QE1n05p8FMx385tJlkvnmPrX8y-7TLJ78I4iPXw7HGsDPwR2yz8vIn1IXAChzXImSxj9cKI-K1dYOA1qnuS3ceCciojG6Xfn57F6Rgybnc9PB6cbURXjBnOibfIx4H5lQH17m-G8Nm-BTl7jPEGPBdkcWUG3IkTHW6pJwF58IGZ35wdbORNmqt-pmhYOk9YIQx9TWJVA0E7pYZKAPCe2vLvLdinhhdeuPVpnVIyoKqHBV5JPH01TO81AxE-r0m-mMlsB40iZ9Kn5yhc7Iu9Xda9f4ZaQzitqdp3ghgfH4SSUaF0EY_U3C718g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=prSRru32L1x5HgxyuGc2ZgIS3yvSelKnECN-HFfwJnBUBdbDMSE_ByrXOgdtC250Ys29jLn2fY7ClXi3ZBSR8V1szBCx4ObXGiEtzIEp8_8HrDzOBq6NlqZ6lKPAYj6aozM77yfrx9VB2u4Dy9zRpJlDQ7hQEaEZJTbBc7QMZhxu6v1kn_1HqHpbICkgW9-pcY3W06fjT-glSuZdtH8LHJrmunM9AppgY5SDD_PgzoEU626f2lp998jtMWfSSKG4-E3Pq13uMmRretyzYRMWZyQneYru1FamjQVkB6qn8z3A5HvNYZ2rCRQN_AsRjn3Mfr18aMLiN8XukNcmISymuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=prSRru32L1x5HgxyuGc2ZgIS3yvSelKnECN-HFfwJnBUBdbDMSE_ByrXOgdtC250Ys29jLn2fY7ClXi3ZBSR8V1szBCx4ObXGiEtzIEp8_8HrDzOBq6NlqZ6lKPAYj6aozM77yfrx9VB2u4Dy9zRpJlDQ7hQEaEZJTbBc7QMZhxu6v1kn_1HqHpbICkgW9-pcY3W06fjT-glSuZdtH8LHJrmunM9AppgY5SDD_PgzoEU626f2lp998jtMWfSSKG4-E3Pq13uMmRretyzYRMWZyQneYru1FamjQVkB6qn8z3A5HvNYZ2rCRQN_AsRjn3Mfr18aMLiN8XukNcmISymuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=cKyyOYtgPAwSy9Moco_lfBCHblAomnUpIfZERZPNOQEFmi9EjjedBptT_rbk63rc4VnKpxGmlBlQXXU9vtTzD9W7JLLZoYgrzYCnNOoNnc2Nrl2td4P6woKeCqF_U5uYiVvOfCQW11rfBcrGz18ptOgV3mAaey9hdtIcfxqA8otUnV_3sPCXrluECD-BISaZDUziqOhBmZdvCRvukHkNqxF6o5snqTBu6LBzFKD9qxUJVOZcS2vREDOwnsHPc8C4mUgSOGDYZAQlUhQQHSbrNNNkLt0gMinedxcJrBVwC__7MTN9jCPHKa4lO5a5bgi-iXaogGXDWw_VOX6HunxVPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=cKyyOYtgPAwSy9Moco_lfBCHblAomnUpIfZERZPNOQEFmi9EjjedBptT_rbk63rc4VnKpxGmlBlQXXU9vtTzD9W7JLLZoYgrzYCnNOoNnc2Nrl2td4P6woKeCqF_U5uYiVvOfCQW11rfBcrGz18ptOgV3mAaey9hdtIcfxqA8otUnV_3sPCXrluECD-BISaZDUziqOhBmZdvCRvukHkNqxF6o5snqTBu6LBzFKD9qxUJVOZcS2vREDOwnsHPc8C4mUgSOGDYZAQlUhQQHSbrNNNkLt0gMinedxcJrBVwC__7MTN9jCPHKa4lO5a5bgi-iXaogGXDWw_VOX6HunxVPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=rDRxHLxIlYxTron66WxavH8wKYI8-ZqQh8KJsZ_qnDPDfNd0xpsKDAcrpLA_CY9rA6mxMEfgjPUKscM1CZUNJ8QVW9Urm23Aq8mdJutqTSPJrEKQtt5GBOsFih38oYEFuL9rUH_eZ5IkH-WPTdZSnJAMMuWyL2kFV-kAtVR4SL_UT12HFPdAcX0pIod5mhAzWSNtMac7OcBKG2s9Ul540Aw3Ud7k4lqR3ReiraSQB1VuuhR7RGM400cjyzkZkkp3u2ejllQTaVRBrZWfyYiCiR0gMUSSDF0Zg4jYTvlAVlyHkVV00Hd5EulgBTfUbUtMvGa7iRX6ajx_EDryVUmX1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=rDRxHLxIlYxTron66WxavH8wKYI8-ZqQh8KJsZ_qnDPDfNd0xpsKDAcrpLA_CY9rA6mxMEfgjPUKscM1CZUNJ8QVW9Urm23Aq8mdJutqTSPJrEKQtt5GBOsFih38oYEFuL9rUH_eZ5IkH-WPTdZSnJAMMuWyL2kFV-kAtVR4SL_UT12HFPdAcX0pIod5mhAzWSNtMac7OcBKG2s9Ul540Aw3Ud7k4lqR3ReiraSQB1VuuhR7RGM400cjyzkZkkp3u2ejllQTaVRBrZWfyYiCiR0gMUSSDF0Zg4jYTvlAVlyHkVV00Hd5EulgBTfUbUtMvGa7iRX6ajx_EDryVUmX1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QYecpY_WckPvu7xqhBHYZS6Dnnabv1jSkHGrjYTZqTWCLEGJMjksifnO2hE62YYTuOhk2wXF6F3x2dQPtNKtIEnPonTWqm1GNVbTfBvCBUfKSCVSmByUR6R1COdJSY11kz-542ruUrd5s-pHzC0Sq9iGCgy4QZNIxveK3fyfAoeMib5LCekmjE7-74N3DChXEmKf-b4o8wvqTF8K0wRaHs50Qgs6E5btb7DzC5vDL9iLpAW06u5VZg3rvU6p2hVWhPcBMK4Wj0o4hSEW2g3jP3FAWgT7DqXN67nbNNhoqr2hXTz0171APfmvHgh9P7AJlwVfWUatvxBbc8NtR1aXog.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=qxs5T1tD9_0hY1t6ngnlauMbLjJGKXetx7K4PUZs4bs3WJheCnPlN_V_jJju6oT0RlvbsPHvCdFxMGF0AuaG6QJi8JWjzhBNK5eNUjWJ4XYcQUFoK_HbKoIyeKtp1W66Ac3nMDUlJbBDbu-cH117aJL2ZJCVFCX36QFogHDBFV0fYvGwbHviltszyPeAYKzyUni3Ux200DQWleB-nfO3Ls_yCLhmmCNyDcaMoBmLi8GO_fbEvkAYWw6zrbboZWap40T_CzpreFgTw4VK19kBdWpxncSg2vCQNPvaHmCVOdXbZdeO-aJ370BugaJK07SSMRSQMt2YsA1ycXJn2aTBY4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=qxs5T1tD9_0hY1t6ngnlauMbLjJGKXetx7K4PUZs4bs3WJheCnPlN_V_jJju6oT0RlvbsPHvCdFxMGF0AuaG6QJi8JWjzhBNK5eNUjWJ4XYcQUFoK_HbKoIyeKtp1W66Ac3nMDUlJbBDbu-cH117aJL2ZJCVFCX36QFogHDBFV0fYvGwbHviltszyPeAYKzyUni3Ux200DQWleB-nfO3Ls_yCLhmmCNyDcaMoBmLi8GO_fbEvkAYWw6zrbboZWap40T_CzpreFgTw4VK19kBdWpxncSg2vCQNPvaHmCVOdXbZdeO-aJ370BugaJK07SSMRSQMt2YsA1ycXJn2aTBY4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=pRhxmvniGBz4LWv-d4i3vqWPXPsPyOT43WBUKvFZkWvduixo18ITtTBfhVVlCgNL6hQl-6EpBM3TSLikYNwpi9R5iWln0gDic-I4PQYdxLZWpg6Y0QX-G_NbuPEQhBcpqQTBti-gYE1pf_bX08FauVOhhu2vqITUQCLYcXvgJ7YdK3y_4WLEGEwQ-a7ur1-E15C-OkwZLlfDM_nKErlbMoiJkLoCvo0-uePqFYEh1kEopjM-PWHeOYB9mFhJyVWtx16MF8VJRvjIMicbJU3YkF4td1INLzCSpTMp2fh4dxsgpbOzRu276w1CjFQbpcVmbzm9vQ6QMjHX9QEvwRpynw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=pRhxmvniGBz4LWv-d4i3vqWPXPsPyOT43WBUKvFZkWvduixo18ITtTBfhVVlCgNL6hQl-6EpBM3TSLikYNwpi9R5iWln0gDic-I4PQYdxLZWpg6Y0QX-G_NbuPEQhBcpqQTBti-gYE1pf_bX08FauVOhhu2vqITUQCLYcXvgJ7YdK3y_4WLEGEwQ-a7ur1-E15C-OkwZLlfDM_nKErlbMoiJkLoCvo0-uePqFYEh1kEopjM-PWHeOYB9mFhJyVWtx16MF8VJRvjIMicbJU3YkF4td1INLzCSpTMp2fh4dxsgpbOzRu276w1CjFQbpcVmbzm9vQ6QMjHX9QEvwRpynw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dwRfMTy23kU1A1ZWE1qQjTazfC42V0tm6ELMYERHhrziZ_Wvi4mp4wcKXZbhyZok4Ipvy6U1RZgZQitao6gpxo5k3IL9x2enA3SkX17XlJCWhf4zq0uQ1sN9ziZb-_GI_KW0QAqy8XxdiPoDlgHXvnMM3cEY7RrcRgAkVcSiIeYnL7ucSvQ5gS0C1SA6vV98aFUesqUluiaX8SZWnwr0Zgi14pbOaygA8fDfkjq4O_NFNDZQTyEg_Daa-gkjS9sYV8V945OH9EkSnbllSruf_3n1AvGVsqsSNVRLCJLmtPqLALIfLIp91cqTX5OxY6ghZ9tBb2MNUYMh3KkG-wjvfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BSywMjY-HURx5IKycrEJdZd2g_ONuoBozIfftbqvZF-MYlef-d0a0h0Wsdc-gJQe4FwWCY3rDTlkuMXiiIj4nRtWNdN1KvcZubFKECPi6PGQgLjDrISuoDhIphmU0suqkXa0MenRD39xKWy0mlianqbWEx1m2P75eK4uBKKyjwFSslvpPvsKG2jlFK0OdYVGAJBjh_7w6GLaJ0xMMVY9ZgcdUNBIX4VhIeFH_6V_p7HDzCrg9t_0PTXDo_4cCugNvgI97xCDDVMP7Y08pJE1sMqfy7Xw_eBke7S56T3o1FknpLLI9sF5uPeTPCcP0GIKuG1mEhNRBSkMx_aIcKnOQw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=IdJHhyd9YBGw2TeebzflTTV0ncyKNZu_VMFg5RQIxBobVhuQWc56xqIxom_XuXrRbAlkN-K__UrPxLinI6tl8BBRzMEAkCwA2qjktY49aXvXHOuKj03og0bNpP4IPlIf-ydsZ35Ltox2hIC_GQezozy8rMr_Qv_gCW7XK2hKfyMTSctTxHip9aNQjDL-uYHtXt7ZXqbiawlR_NBbIwUF0vQ14BmHBmF_I8ZytNYcL2ybWhFrMjX5q7Ynd3xI-CGD3Ajg7XnKkSoLH0WcbUMzq3fQdhXuVHBNQQD3hk6mGGQqCUHHTe-ahbChZWMSGAIh7hGT88avxmLO1ZPyFrAypg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=IdJHhyd9YBGw2TeebzflTTV0ncyKNZu_VMFg5RQIxBobVhuQWc56xqIxom_XuXrRbAlkN-K__UrPxLinI6tl8BBRzMEAkCwA2qjktY49aXvXHOuKj03og0bNpP4IPlIf-ydsZ35Ltox2hIC_GQezozy8rMr_Qv_gCW7XK2hKfyMTSctTxHip9aNQjDL-uYHtXt7ZXqbiawlR_NBbIwUF0vQ14BmHBmF_I8ZytNYcL2ybWhFrMjX5q7Ynd3xI-CGD3Ajg7XnKkSoLH0WcbUMzq3fQdhXuVHBNQQD3hk6mGGQqCUHHTe-ahbChZWMSGAIh7hGT88avxmLO1ZPyFrAypg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VKdWbVA3ZwvNoF1yedXsWeC-emwXQ0Rej087jp_pezERUUYwM3jQzzrRFraLjAaI5tEL52LcNjV24VZMy7b4p0V8U40uSI4jHjFMIqReoWnMILyIHfyj1z0g9W3NCpdQPm3TlsqEfvLxG-q6CvQnru47TPc8XnHdJg7gnOJWLXy8X-wGOXNjHUmP3gyFOVE0B_3-INQCvhJn8_psFb_BMlfqcaKuWQfv8x_TzcZRvQKZKCK2opRxrdXpVHYd5E5-k0qSQO1rYmA1pr-8pm-zGx2RgyuZVG5G3lK09wETKImP0CneiVoL03OkiWPn2w9E56oCERHpn4gp4xV0jQWZ5g.jpg" alt="photo" loading="lazy"/></div>
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
