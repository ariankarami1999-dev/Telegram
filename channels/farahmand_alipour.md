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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-19 03:30:25</div>
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
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/6804" target="_blank">📅 15:30 · 16 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6803" target="_blank">📅 11:29 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6802">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AGOey_jBLBxLdpyqfgjQ6yjG5SXM9Y_BC1Eo5u_9ziTd6Ab5PkydFXpZzms3lAZB_iZdgrzXGZKHQRgFhZlmJS0jhYIvn2r4ycW6xwUW_0P9eoijkIqy2OZjJimxkyHSiozJ9TDjd6yLoKb2ImlGI7t0PohtRx39at9KRyV0B5HzsaOv1oY-ljON9b2-nsRWHKTBIyBol7VSalGopyUbArXtwPX__KIND5nyLA-SampYzI8g1nbGfBZQix2VlT2UheRd8wHJDbCgHSnc_M73t6eF5kLetBzD2mhkqG_bi1eUxbiqhHOewnjflG_96sPseWlvP88SFuAk4UdM9m8KLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌د‌ونستید یکی از معروفترین آیات قرآن  که آخوندها دائم به نفع خودشون و شیعه و….. استفاده می‌کنن آیه ای است که دقیقا و مستقیما در مورد یهودیانه؟  یعنی قرآن وسط تعریف یک داستانه، و آیه  قبل و بعدش داره در خصوص جدال بنی‌اسرائیل  و فرعون صحبت میکنه و  اینکه خدا…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6802" target="_blank">📅 10:52 · 15 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6801" target="_blank">📅 10:42 · 15 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6796" target="_blank">📅 12:43 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6794" target="_blank">📅 14:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6793">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">بالاخره امام علی در کوفه  تونست ۲ هزار نفر جمع کنه!  برای کمک به محمد بن‌ابی‌بکر!  در حالی که در خود مصر ۱۰ هزار نفر مصری جمع شده بودند علیه محمد بن‌ابی‌بکر و به لشکر ۶ هزار نفری عمر و عاص پیوسته بودند!  این ۲ هزار نفر از کوفه،  تا راه افتاد و …..  هنوز وسط…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6793" target="_blank">📅 13:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6792">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">امام علی هم که خلیفه بود و در کوفه بود، قبلا هم گفته بودم که کوفه (و بصره)  اساسا شهرهای پادگانی - نظامی بودند. احداث شده بودند برای حمله به شهرهای ایران و تصرف مناطق مرکزی ایران.  با این وجود به خاطر جنگ‌های پشت سر هم مثلا جنگ صفین که نزدیک دو سال طول کشید،…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6792" target="_blank">📅 12:57 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6791">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">کار به جایی رسید که جنگی بین  محمد بن‌ابی‌بکر و «عمر و عاص»  بر سر حکومت مصر شکل گرفت!  عمر و عاص، دفاع قبل توضیح داده بودم که اولین حاکم مصر بود!  و جایگاه محکمی هم در مصر داشت!  و مرور کردیم  که اوضاع مصر هم از زمان حکومت  محمد بن‌ابوبکر از لحاظ اقتصادی…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6791" target="_blank">📅 12:52 · 12 Mehr 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eBey8b_5unRJSO_uelw9E0eA-bWlNywybrjiVhAO-9_8uNwfaL4A8DypklO6UVDIVZhkhL7EfLp_NzeCS7OrhhrHcv4It3dlepVLPB0z6wDvy7eS8aR2NbjYUadLyT3L-BOc7DPafvn4icq9pxJuscdzXNqV9sF2gNqNxGBoR6jNcLsoBCVqa493c_QG7PVd-xKRhQhXSRpBv6j_tdJ5IqsMloAE89jyObSJNRPkGUFyYJYjZ8q_tsWHZ14vgxEUJccLDDxW-FC6gtJo02vlYNGgZ_DTHBFsZUBre7kM2EFw7m8KUrQmwRO4iSx54FwkDgo-brmsxm4QwIKVZgqQjA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pkc_uZiG_GONzx4YeSMqi0sZv-g3SnKSf8lOmjF-UTVn0j5Of41xtHvv9Mz6_R2QmxiANwogiQtlzmu3mboWqXJdpgGZ_TYMplmIq0T0By88mHRzDpqdvS0ZDail-E0ceoFl9Bl5ew4Z8hxf-_bD-bvU5pPnDMB8ckHPqZYMuXFFJLBLGtBpMFqDEA5FlMJQNY5QgReoiIlYOBKTB8IsthEsU8_cpIlKGipUCd2OHiibV9tH5Wvg8q8W_flstb-gtwIHEL8RuIQumS7C2HITMOQ69OnNn4-bLrgsreffdOahd5lYfop_IQKOOEQfwKK9YSCl4W0x2fefAXDDzepTxw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ypo8mVKWyALyDLS2M2qNRDO4TyRuLapUjJHiVc7bOMXW85939l2oPHX8hCTGgHV1zRwG_GvlgvUHTEaIsxWIk2Qhib0ECfDUwIdnlHsNv9Z8-K5wNY_JBjcYQtwvHS8gZz7ZO7tsCU39jOtxzaBd3TJBww8BC3q6S820z8dD-83Nxh667eZt7nGZgH97MBO7S0eBflPb5KPCYMa4ECFTMinCr4_Gj-hkc5obrpbsqRNHitciAA_1Zuk8KRhFBIVdAnvMTDYLpg5-6j0Vmp-fyavR2aiVd__o3qa5OBX3LU2yXiP_xWCyjTINBxXeWcSe_qFRK9xtMHqLhqJ6c3sE5Q.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/c578cb6e91.mp4?token=CjDxupQN8wXIDaK20VJ-9_ek_ImQIKbf7fgrnBS9Tc55HTupUAf86kgjx0K2nBhLnY_HHqz7QD6RiwGjpMGbUtz3aH5t-YcTP_U4-bR5RF8Cvu2VwZzwDZq-C6BrUfa6XXFqoO-90GrWtpPIZFs6GoJYKYK6pDZ_-xqm2lmfAqgYbWIS0msI_lqJmKMPxRsL8Zg5KqWY05j8MDdCe7naZz4rrAP0KAznT2Q09PVeABWF6zR15jAoVN_ubgopSHTc77H6zol2qFGgudOCLRfS-_v4joqHN0lL93PyDxcLG_F_nbVv1oRaVGs7YaC7yhrXK6iinDO4nG8ublpTzK_6LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c578cb6e91.mp4?token=CjDxupQN8wXIDaK20VJ-9_ek_ImQIKbf7fgrnBS9Tc55HTupUAf86kgjx0K2nBhLnY_HHqz7QD6RiwGjpMGbUtz3aH5t-YcTP_U4-bR5RF8Cvu2VwZzwDZq-C6BrUfa6XXFqoO-90GrWtpPIZFs6GoJYKYK6pDZ_-xqm2lmfAqgYbWIS0msI_lqJmKMPxRsL8Zg5KqWY05j8MDdCe7naZz4rrAP0KAznT2Q09PVeABWF6zR15jAoVN_ubgopSHTc77H6zol2qFGgudOCLRfS-_v4joqHN0lL93PyDxcLG_F_nbVv1oRaVGs7YaC7yhrXK6iinDO4nG8ublpTzK_6LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K2P_841O4OAniLdr5AiuTTmawwuLZLOCuIsk3EvRakTng8arEP5zIYtWgSsZAPrEen-Z5FurLRg7uXRyImGQsSGLE5VH7piU2v2MzfbeDrUvViZ3X-AQpXRZNfTxoPeZN7Kn0SWjIBEQ0t6xJfBx3rto-79bAn5si3IjTcgumOuFV-YXQWqWiquD_78Ts3Nb9lcDC6YQDx8TMxTfZZEqWablfcMTKVaJg9cdgwBZFl8eamIPGX4Y-yyK5LhNz4BfJ2hakzRdMrJxO_Svtip32wqKpaFyQ3tKp5VHSmXcgYaGIONNaFaCE7zaMd7gkoAu5tWK_Wz5gZAZO9Ei3ffTeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/6774" target="_blank">📅 02:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6771">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jwggz39u1tCUe3mz_VzykXWPGkRNvTPTw8UzSSa7qsUIEPV2neA49maH3BMlcKdJ4RnZ4uKA8ZxWl0DhlAEW-wmZJK-MR_6hvVpFPtv8jT-BqA07ipPK-hpR85ONLoz7X1d8zNQmA6KcGEpxDcm-IOieYf2n7zkCm28EzOkvUm-rPzfWj9ikw1p-woTVnuYb09b3dSRcG6QbamSgNQ4A8csljP4FoqeVRkbd3A55N-H7afoi4OkmWk8_aN94xrpE36nptZY7i5tpsh6WSg6e8OlBK1TeoFPYdgQn-DByO3pHDRhT8tGZpVQMGpZYD9ylMpCnbtL3_h_EERfeslVWfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X7j7VbRCmGib6_lpvi6Mvroeq_eTzbqbZMUJeBR4o_Oh_ksYbvafWJzTd4fnD3CmFntMb7neYWiSIAU12xBP4E1mBDFrxQip77WL_eV1UTXriU_h2vOPjg9Y07jc2VMR5tR9fgYc3ndhkgOp9TSXzYP6RPrZETsZeT3ySeCUzSrmIWQDg3dme5R7OYrIO3BH0sN5IOqFamn1OF77iPhfQKZgpRc6jX9MOXYEjlO1JD3dkVDfEyazxYnrHvwPJnNBk0IjYjHnPb_tpicLNp7dSKcnIRdE-xO7qH3LGolbY220mWh_5F48Cb0ynuYxBe3ci7jbM9LnQZ9zSqyrw9YWvg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/895be358cd.mp4?token=URn-kuI9VJN9DrsB2c0Qy8VsP6qz7o90nITA774Thv22LOgEJp1bkqQ7CmUYeMy0IFvQpJgn20NDQ3MzN6TWt3ydTnf-3FaDd2LclgpOKRE-51CNWaJIw8Ulhp_tCEW18tzeAWsdFUp-B4Vd8RxiuWVA90OGAI1XOByjIGlWhrICnwc7RUhLVKAxl51V_0n0M61XE93OIoOHaRwDfRLRlK7y0UVmMSWSlWNWjNAhpnjkX4mvBf0ynNKBtKQSRV-UfMBzH5bZ13YvW3B80xi0m_J54SOg8BUAuVULTOJHHl28tOOyvRb1Pn2ftBgGRqQDPZcUU0ff-WK4fxB5F9fiSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/895be358cd.mp4?token=URn-kuI9VJN9DrsB2c0Qy8VsP6qz7o90nITA774Thv22LOgEJp1bkqQ7CmUYeMy0IFvQpJgn20NDQ3MzN6TWt3ydTnf-3FaDd2LclgpOKRE-51CNWaJIw8Ulhp_tCEW18tzeAWsdFUp-B4Vd8RxiuWVA90OGAI1XOByjIGlWhrICnwc7RUhLVKAxl51V_0n0M61XE93OIoOHaRwDfRLRlK7y0UVmMSWSlWNWjNAhpnjkX4mvBf0ynNKBtKQSRV-UfMBzH5bZ13YvW3B80xi0m_J54SOg8BUAuVULTOJHHl28tOOyvRb1Pn2ftBgGRqQDPZcUU0ff-WK4fxB5F9fiSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=R6EE_izSq9lp24fULI1dmIsRyt8R_Onyxeg1ohkYm9bsPJB5WmaqXQ4FY0qAwwpWar3Gh2-2JH6CwMP1QeiCjpzpUcRAKuPy6btIftVHEbrL5EeRbxK9e792L-q42dGasest-czEvrp19aRIyPnzQH4Yj2Djrket2HTf7y34_kYBgW4Lo0DcNY1jrHBEI3V-iWoLCkFz60n9xmcMhjlHww42eTwR8le_mYUehlcK-PDpcRSD33hZocolk2YfJ0B-MtP_BkD1KYt2dziEmf-OR9eZMwjqf_JgyKrp7c_DcISLOxolZ630u8S3f3hEl5YMYqRsAlnuURTtGxD9RKypJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=R6EE_izSq9lp24fULI1dmIsRyt8R_Onyxeg1ohkYm9bsPJB5WmaqXQ4FY0qAwwpWar3Gh2-2JH6CwMP1QeiCjpzpUcRAKuPy6btIftVHEbrL5EeRbxK9e792L-q42dGasest-czEvrp19aRIyPnzQH4Yj2Djrket2HTf7y34_kYBgW4Lo0DcNY1jrHBEI3V-iWoLCkFz60n9xmcMhjlHww42eTwR8le_mYUehlcK-PDpcRSD33hZocolk2YfJ0B-MtP_BkD1KYt2dziEmf-OR9eZMwjqf_JgyKrp7c_DcISLOxolZ630u8S3f3hEl5YMYqRsAlnuURTtGxD9RKypJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افتادن به التماس برای بازگشت به همون شرایط قبلی!  ترامپ ولی رد کرد!    احمدی مقدم چند روز پیش گفته بود به کشتی‌ها حمله کردیم - و تفاهم نامه نابود شد - چون میخواستیم چند میلیون بشکه نفت رو به قیمت بالاتر بفروشیم!  می‌د‌ونید که بخش عمده نفت ایران در دست گروه‌های…</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6770" target="_blank">📅 12:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6769">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TkMx36MKDAVygtl6S0VqerCWEjnbK367TuBUiyTkVsRE-SJH3jGeMov8vo0SIZ1a1kRX6WehFWd4x01O7PP2H5cFPhwzZGaIVysGxsxiYcAqXnFKzaMlLom8nFTUNhZ8iDga4SzXB4MPNWYVdHRkK1-CHcklJ3IOLl373-LzWKNqZ-AEGkw6n5TX0vbe6n9NYKW5MPvxaFsKW6rAbp3yvu3LrujnhFQ6_zpvBJp4CCag_tKw5kEju-TLZPiBojXRLwwrlTgmpt1IHBuMFv1zFjvkA0gFIZqM2lhCnQTq03axY8yOnYAMIVi8T8gUaJ8LjTdIkvplS4oIOILAj9TRKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد  تا به دنیا فشار بیاره،  اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/6769" target="_blank">📅 12:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6768">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89284f5821.mp4?token=VHIycsRP_4hP_mjHF3LYiwgtXNXcoUmFEMcnqGVJ4QoSbiGAeUWRHsJC4edqmC9q3YiFvIO3-v8g3-u5hmLbS6SL-RXn5I4Qf2JOzy2K1bNU88ycc3j7-2HX-HBFzosD_4HHB0hhVmRw5Q600art_9-JZIigOLADx7WzKTGEyjSZRioH4qDFH1ZvVmp_FWKlTf41Ouah933pBecxNFiMFeV7wbxaDr5X6on-H9T2gfLUuW612gOIhtm6gCGH45eu-Qd-qmSCi3d8aHmWA-vr_N9ph_EC8P1xzXcavuTQD9aHJDd3n-N8QWP57ihGbBfWyqTCdCGx4npWocE8W3uIM7Yg948ZEEpyKGS7g0NpjWC1cgyG__8qHqlEDHNrpIokm6xiwpGq76-o-bPWDSmo6frTbgtFuKBlHrI-YwFFC4FRx6p4DTEBrPlpO-AvRWPp72zpPA-X9LdDKSkkk3VRHMGepLT7f8X931hWVt7lpryPFKob6XAH-wywyH8H0jIeDD4rCrgM9Blc_JhnhSD7GmVZvA1Hqj9BYV2Tc8mhwFIhvLGrNsw_qV02rwXsDVCkpMKbBS0N8Q95UUydm0EDxST2fsRfDi6hARX52ugBPFJ5Z_Pm3wB_1Ag_myRKOp4Bbcdnmc6Acq2wuBWyW4fVSQrxS-p5rTGoTM79xYdqxyc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89284f5821.mp4?token=VHIycsRP_4hP_mjHF3LYiwgtXNXcoUmFEMcnqGVJ4QoSbiGAeUWRHsJC4edqmC9q3YiFvIO3-v8g3-u5hmLbS6SL-RXn5I4Qf2JOzy2K1bNU88ycc3j7-2HX-HBFzosD_4HHB0hhVmRw5Q600art_9-JZIigOLADx7WzKTGEyjSZRioH4qDFH1ZvVmp_FWKlTf41Ouah933pBecxNFiMFeV7wbxaDr5X6on-H9T2gfLUuW612gOIhtm6gCGH45eu-Qd-qmSCi3d8aHmWA-vr_N9ph_EC8P1xzXcavuTQD9aHJDd3n-N8QWP57ihGbBfWyqTCdCGx4npWocE8W3uIM7Yg948ZEEpyKGS7g0NpjWC1cgyG__8qHqlEDHNrpIokm6xiwpGq76-o-bPWDSmo6frTbgtFuKBlHrI-YwFFC4FRx6p4DTEBrPlpO-AvRWPp72zpPA-X9LdDKSkkk3VRHMGepLT7f8X931hWVt7lpryPFKob6XAH-wywyH8H0jIeDD4rCrgM9Blc_JhnhSD7GmVZvA1Hqj9BYV2Tc8mhwFIhvLGrNsw_qV02rwXsDVCkpMKbBS0N8Q95UUydm0EDxST2fsRfDi6hARX52ugBPFJ5Z_Pm3wB_1Ag_myRKOp4Bbcdnmc6Acq2wuBWyW4fVSQrxS-p5rTGoTM79xYdqxyc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0493705c07.mp4?token=nt0DiG6VZJodI1AyP4hlGxklpitEwxVxaHQDKv8tmY_9ovUzVGIZAs5AvIFxfh_-STUhBZ5tC7gJgFRDwQ1osOnQt0dcjFurudh6GFEeRFRtSvjvaWsDLCX0lPA1m2SiZWieYLr42FvFc2Xsbvp3MR_g65tfXuq-uACcdfdiRjrXNwtcxzKg7wud23ODv2WIaz3zMtIgShErVkvo5VQGvxBsQbiUY9DpyV2PTG0dKfUfqlUMWnk_fVmdJ1bk548Ez8ip9ZJQg3-40wGqhm2aMWi5tZTlCjGJhyae5sPOV7vR9xR5vmJ8yPmCXc3zbEiFhC3qkFh6pdUY7Q10z0wpBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0493705c07.mp4?token=nt0DiG6VZJodI1AyP4hlGxklpitEwxVxaHQDKv8tmY_9ovUzVGIZAs5AvIFxfh_-STUhBZ5tC7gJgFRDwQ1osOnQt0dcjFurudh6GFEeRFRtSvjvaWsDLCX0lPA1m2SiZWieYLr42FvFc2Xsbvp3MR_g65tfXuq-uACcdfdiRjrXNwtcxzKg7wud23ODv2WIaz3zMtIgShErVkvo5VQGvxBsQbiUY9DpyV2PTG0dKfUfqlUMWnk_fVmdJ1bk548Ez8ip9ZJQg3-40wGqhm2aMWi5tZTlCjGJhyae5sPOV7vR9xR5vmJ8yPmCXc3zbEiFhC3qkFh6pdUY7Q10z0wpBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موج جدید پناهجویان و مهاجران افغان
به سوی مرزهای ایران</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/farahmand_alipour/6767" target="_blank">📅 17:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6766">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c6izqMuFO8i46ejG7XQlVBd6xouJeXynlll8CZvW0b5bNdxDaf9RL_wBvnkeWZP4BGDRGC5LaXUefn7fiDq6hmh_fjNz3cVpUVfSuW-jyifhaHZHyaifrqFS7ajMlUFRfLkNzJ4WNTDFdEQE1nL_Gh0A5smbD9B1z0_okm5FhRUwvZIdhBuhsSt7P_B_9f4DyfLNCspdj8p9Fl4WBClOM54CqJWRx1Ze9pDDWrtmrj1PvmO_Q9NTLZzzH2lPMoA24HztO6uIVw-gl7-6qmzO_cnCUmyCY0mZ5J9SvlhO0PdCV80TrrVDy0l2UpAwltVFdU3FQAyA9i1jC9zKaTSusA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو و این حرکت یادآور داستان‌های عهد عتیق است!  شجاعت و جسارت فرزندان داوود!  که در عین جوانی و نحیف و خرد بودن،  مصمم و بی‌هراس،   مستقیم به چهره دشمنان خود می‌نگرند!  مثل داوود، نوجوانی ظریف و آواز خوان!  خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه…</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6766" target="_blank">📅 15:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6765">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=Absy19k6Et9avXXg2I8KMwRi6Nf0Q8PLOH3tyVS_MDdWGpNEDnty_O8VPbw6RB0HTK0WrFVwqIHqgO78QrU94V2Do3oKk2e0fEoz_-pkoVcsfNMK8uggTKe3_7_EwlELqOWlWhRLdwRo7W5VTzq4cBe3DAwidml11UIJ_XHcmM178ngMFGhaQ8kd6t34_skLruQWhc9IWs19bj4Oz-Ta-nRF_bQuU54w86SJ9VRCFRKtek9AX4-b4W0HgtnieXC9SHapxOb77_rCP16fTgHycXyQ83Pih6Ro56MBNyCWpn-6gRGUl0Z9drBRigKtCWuWZXffv1Diu3ddqI22_qS-9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=Absy19k6Et9avXXg2I8KMwRi6Nf0Q8PLOH3tyVS_MDdWGpNEDnty_O8VPbw6RB0HTK0WrFVwqIHqgO78QrU94V2Do3oKk2e0fEoz_-pkoVcsfNMK8uggTKe3_7_EwlELqOWlWhRLdwRo7W5VTzq4cBe3DAwidml11UIJ_XHcmM178ngMFGhaQ8kd6t34_skLruQWhc9IWs19bj4Oz-Ta-nRF_bQuU54w86SJ9VRCFRKtek9AX4-b4W0HgtnieXC9SHapxOb77_rCP16fTgHycXyQ83Pih6Ro56MBNyCWpn-6gRGUl0Z9drBRigKtCWuWZXffv1Diu3ddqI22_qS-9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k3UTSsQMaMrJckC0gxnnKcpZc7PS20Dhh95LBAz7z17-lygdxBbltC5J2SW0_Z-eFR_qO-9zMj6XUJGBNsvQmGTLLxdsMVKBCPbvqJMepF0RnZCczu0D10AVV7L5BWxnQojFwpU3Fh0v6o6UEIfcNhGcF5-GgZ-kqXidSSmj8CoHNJnyiTV2KSGa5_schHcJvUv0mkKK0kxddrf4WWqyIeQbem8_zlcYICIj3c-YAY9wp1lImYRNA-oTUQZ8qoI3JTSHC1FW4RAPW3VN2om-im7WcdZAdcQJJKmIQE5wdPIvJ3lUkJ2h6favIYspfyZlH2rJZOR7_qQocIn3yu8hvw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=ZNkZvGEbVZ9jxDchp1GlKy0P-k51TLem9D5dkg9madUzhYSwHi93UZeF_fwiC6QtYvGQ_4Fgvtx7ciKgn8XfRdjxgySBeLJ90_Jgvakaxz0hHxncB0ZfZj1Xy2rRKUyHGn5gWZ_8D7DSTrkfzQpGc8Iq_sOHJyi3t1uEqD8hEV0xWLfALJd5OdnndCsEE5Qfpu3TUYtOU1IS8PvqKGxLqJpD-OBbHokoLbTHQfJLXJ4SKTifWVfjeWwmF4BwZ-3sgvT288nIihyYRbpyIMz-mkP9lj6at_9753E0PXTaGMgZOXFBFrNwM8rnPV-yDExA-kBVj8Il6mqzFRDdVMIglK72-QW1QGld6iz73cluecQyHcEggwdvsW3ZV8bh7ERfwjPwFTiNfXvR_TinKeVznAxdNJHvw5FZKGy8YV7pSDlURhfIfsX09ngT496cEmFF8UmuxDoAAHGPPP_fm3Lj72UjqDH2rYX1cqSYWefEUM-hP3uE7gSgYh6YiwDoC_nxJ-RgM2qs_TBLg2xjPL1AmF5Q8jsdL8GYzaoZ5Xvps2owmx6nGwEeLiiJ4PTszSmEMixzIcstBKyk5VSLd6kQv_-2w7mnZy3BHuiQAFE-BI24tcxQvAmgOA1RGSXaF4JBixv9XG2Of0xMk9q70TjYYcDIPqm02ELgEaIM-1rNbxU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=ZNkZvGEbVZ9jxDchp1GlKy0P-k51TLem9D5dkg9madUzhYSwHi93UZeF_fwiC6QtYvGQ_4Fgvtx7ciKgn8XfRdjxgySBeLJ90_Jgvakaxz0hHxncB0ZfZj1Xy2rRKUyHGn5gWZ_8D7DSTrkfzQpGc8Iq_sOHJyi3t1uEqD8hEV0xWLfALJd5OdnndCsEE5Qfpu3TUYtOU1IS8PvqKGxLqJpD-OBbHokoLbTHQfJLXJ4SKTifWVfjeWwmF4BwZ-3sgvT288nIihyYRbpyIMz-mkP9lj6at_9753E0PXTaGMgZOXFBFrNwM8rnPV-yDExA-kBVj8Il6mqzFRDdVMIglK72-QW1QGld6iz73cluecQyHcEggwdvsW3ZV8bh7ERfwjPwFTiNfXvR_TinKeVznAxdNJHvw5FZKGy8YV7pSDlURhfIfsX09ngT496cEmFF8UmuxDoAAHGPPP_fm3Lj72UjqDH2rYX1cqSYWefEUM-hP3uE7gSgYh6YiwDoC_nxJ-RgM2qs_TBLg2xjPL1AmF5Q8jsdL8GYzaoZ5Xvps2owmx6nGwEeLiiJ4PTszSmEMixzIcstBKyk5VSLd6kQv_-2w7mnZy3BHuiQAFE-BI24tcxQvAmgOA1RGSXaF4JBixv9XG2Of0xMk9q70TjYYcDIPqm02ELgEaIM-1rNbxU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترکمنستان، آذربایجان ، گرجستان و
امارات و تا حدودی عراق،  آسمان خود را
بر روی پروازهای ایران بسته‌اند.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6761" target="_blank">📅 14:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6760">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yz8Vc8VGmPKKPswWv0tfzPrS_18p2aBvlM4CMivzUgeGW3JNHE3zQe41x1e4SZ8CScKvG5MNBzDgqrStfrVRvjPi70F5ujV4fa4YaVImSfurfSNuBQAMzK093bqE7VRQdsCOpWMhgrZb7Pn2pl3piYhv9kDXFj3DrKB4yFmgN_PyqdOiKxEGKwpLawCUNA1weS0rVR0s3Fu3eVLn9Gwq-7PuaEbqf4ZskyFLvt9q5bJ-5INR2xsasRqHD0SuDmb-1wZ6Rj2x1ch_iQBrU5060Vrs7TptOX7GcuuwoBzOadIo-0eoNDrqZ3WIE1uNCcEUvtZCItH6NvAxWDbYoTNQgg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=vNkIIL0FsfzNCjXwwuCZ9J4xiJfIWVMlIS_Qk1Rg6UuhBDVlT3ANhnFcW98u0Zh59IIjcUUTLeyNR8PhNDCb3PhpFywfe5ZsRCqHvtj_9dzuy56_ox-24m0upVEHbAFywgVHFc2_YxPCqVSC2DfV6d8kR6l6fhB_f_k5PHz3DfI7Vo_CP7g5g17JTL2-80HNMbiaIkXTWty5NSJB3Ul7AdFG9IyXdIvkSG9xf0oOMREnFKJ_2Lz7XsYNyqEVtEPXyWV5JLDrcj7IHudPrmwBaFJb5oWvEoUG8h354EnUrpabWzg4bhORnAYWHB0xwro55SWIejnqwBAVsRHegn6dNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=vNkIIL0FsfzNCjXwwuCZ9J4xiJfIWVMlIS_Qk1Rg6UuhBDVlT3ANhnFcW98u0Zh59IIjcUUTLeyNR8PhNDCb3PhpFywfe5ZsRCqHvtj_9dzuy56_ox-24m0upVEHbAFywgVHFc2_YxPCqVSC2DfV6d8kR6l6fhB_f_k5PHz3DfI7Vo_CP7g5g17JTL2-80HNMbiaIkXTWty5NSJB3Ul7AdFG9IyXdIvkSG9xf0oOMREnFKJ_2Lz7XsYNyqEVtEPXyWV5JLDrcj7IHudPrmwBaFJb5oWvEoUG8h354EnUrpabWzg4bhORnAYWHB0xwro55SWIejnqwBAVsRHegn6dNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=UruJLla7iE3VAo9UjKPHhNXJtcX8HjmdS8VIiKNRoJAVo7_Je-LfT_fJggtLN3TEBNusagMdnJHBZ0vXqEbr8fCSEzuexo7WGBpHAgiFTRFTVn6hjfp5e31C1HwBuAbz_eV-H_2uWmTaOHliTwIMsamW7LeP6NeMvKYjozlwS1SiWClUrtm2Bv-D5T88K49mumUAMMcIPMYNZgYM_ictob2RIzEHkW-lvcUc8oLqQjPgOJPw520HJxs8jtzvw405o7tQ_LqV-WfIhKkhmC8PU7S0bnpbYWN2UBOLw51RI3c0l2OM8ff_6cwwmA2dPjPj6EFYk_0ZNav1Q0PQ4fHuug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=UruJLla7iE3VAo9UjKPHhNXJtcX8HjmdS8VIiKNRoJAVo7_Je-LfT_fJggtLN3TEBNusagMdnJHBZ0vXqEbr8fCSEzuexo7WGBpHAgiFTRFTVn6hjfp5e31C1HwBuAbz_eV-H_2uWmTaOHliTwIMsamW7LeP6NeMvKYjozlwS1SiWClUrtm2Bv-D5T88K49mumUAMMcIPMYNZgYM_ictob2RIzEHkW-lvcUc8oLqQjPgOJPw520HJxs8jtzvw405o7tQ_LqV-WfIhKkhmC8PU7S0bnpbYWN2UBOLw51RI3c0l2OM8ff_6cwwmA2dPjPj6EFYk_0ZNav1Q0PQ4fHuug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=S_sySO9zl3CZDolSctdB1afx_uqALTSFcJDOELsjH4_f-vATK3CRZEzPVL3lu_91xptYuOhUaOxCHXGXk8YzPNPIywNbQcS70TjWindrVC9NikvADyrO2XJWtCX6aPuR3YwmAncolOHZU0sZaqzUhDua15Uw9TV79FuwWhjeDKr61zXqS-PvoOWdoCuN_D6jXCCqS95TJONwHLRJaaEIb83HflovgpgQqDGaqo9B1w0RbLOzK49jOI5RMCaEhFvnYxHRvSYCWX2yx3d7ZYc9fodYg-IBLcyDBO-YLSYxxzb1GqgSqcLCWdQOXx97VWQHoNUPBCr4_WduOukLz--Hqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=S_sySO9zl3CZDolSctdB1afx_uqALTSFcJDOELsjH4_f-vATK3CRZEzPVL3lu_91xptYuOhUaOxCHXGXk8YzPNPIywNbQcS70TjWindrVC9NikvADyrO2XJWtCX6aPuR3YwmAncolOHZU0sZaqzUhDua15Uw9TV79FuwWhjeDKr61zXqS-PvoOWdoCuN_D6jXCCqS95TJONwHLRJaaEIb83HflovgpgQqDGaqo9B1w0RbLOzK49jOI5RMCaEhFvnYxHRvSYCWX2yx3d7ZYc9fodYg-IBLcyDBO-YLSYxxzb1GqgSqcLCWdQOXx97VWQHoNUPBCr4_WduOukLz--Hqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/04900863be.mp4?token=iBPJTasIy0Omreh7UoLpcYCZ9hANpU3NMY9zAb955Q3237mFhmzSKwXkWlqBv0929FdaZR-Qwd2GBy8hwFo5kcPbXOlxlU-LTeG4cF_dO-ClW8wQsUd2i2v8Yyg_l_8HuKGQ5VXUpq_KoPc2g9CQL3y5hzu96cIjOnD0__6E7SfuijHnQDxpu6YnYWLHXZ5t2-Ij62XIaCYrMQEOJ-0tc2r4NOI66kQ5MER6lF4Ior1e7vIBJg8RKMvXBwXAzOY8uvJbdPLsG2lI1xttYvkfSdwJYu2DUiA6NoSz-dBAr1mROg9Z-seMC5XigkIk022bqyHR-Lfd4PXvVR-UkZeOsmBewPmJVIyk0uLxkEWHobuq7m3c3gRGin-SdFA5OzoPoPj-xz0Lo3t1Q8aDOYm0m8NllohMcBnVLH7LgimWPENVzwY8SCy66sj2cs5PqIJSc25wNFsIMtNc0j6OXyW7D5tSaeYjDG1X7Lht_AiHx-ng1k4xJXWyeG6sz8NiQ75lJrtjDRUMobmrXmskIybzNFDOOflHHNcr8K7OPtWeZVtgEkIDeUp4BVDhrVhsQ6Dwr6igM0ZGU9SzNSNy4SRCiosTBLv8VrWMhhwKsyAL1TFXjxTujj0vz68horGWbexiNzxblqN7VTsKCCsFA6Nn_j0FOgK5cozYOv9GGttk8YE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04900863be.mp4?token=iBPJTasIy0Omreh7UoLpcYCZ9hANpU3NMY9zAb955Q3237mFhmzSKwXkWlqBv0929FdaZR-Qwd2GBy8hwFo5kcPbXOlxlU-LTeG4cF_dO-ClW8wQsUd2i2v8Yyg_l_8HuKGQ5VXUpq_KoPc2g9CQL3y5hzu96cIjOnD0__6E7SfuijHnQDxpu6YnYWLHXZ5t2-Ij62XIaCYrMQEOJ-0tc2r4NOI66kQ5MER6lF4Ior1e7vIBJg8RKMvXBwXAzOY8uvJbdPLsG2lI1xttYvkfSdwJYu2DUiA6NoSz-dBAr1mROg9Z-seMC5XigkIk022bqyHR-Lfd4PXvVR-UkZeOsmBewPmJVIyk0uLxkEWHobuq7m3c3gRGin-SdFA5OzoPoPj-xz0Lo3t1Q8aDOYm0m8NllohMcBnVLH7LgimWPENVzwY8SCy66sj2cs5PqIJSc25wNFsIMtNc0j6OXyW7D5tSaeYjDG1X7Lht_AiHx-ng1k4xJXWyeG6sz8NiQ75lJrtjDRUMobmrXmskIybzNFDOOflHHNcr8K7OPtWeZVtgEkIDeUp4BVDhrVhsQ6Dwr6igM0ZGU9SzNSNy4SRCiosTBLv8VrWMhhwKsyAL1TFXjxTujj0vz68horGWbexiNzxblqN7VTsKCCsFA6Nn_j0FOgK5cozYOv9GGttk8YE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=ViBJmz3Gq5Cbji2WgRxIkLjJY8anLFmvUDKI6dhuWWQWxgoKNm2j2zTNdkAMOaNw0Zm6yAkHCMDljwzbVwa6_a6JDy5BFTqJkS0QMcI1nQntJdcKB3xBg5mdXfZVZlTIIvbKKt29CZomzaS8YKddsOG6YbhOhwbS3uAlGDjhadNkroojNv7Hq6AccaeDzWEqAJI2qDEmUvL5Xuk7K3fn9hykAGarIWfFokL1--J4godOJcvh_d2to1j6SOVmmuYwaTZbVodXEGZYsZbfDpwnLEyTVPHPCwjZeuRUQkyomQmdjE3IBZXKh-Nb_w5rypafocvsGB97A3Czixa2qRQF_GDnVhgkUJv25meISv22IAKq3oP660ed4Zd-f85KDTJ98wVQqZWHG3w-oS_spKNhdtFStLNLdznoUxfmQyOG4iOHOmi52TAYJ7FvalaWJ1DhQN8chB0v3gxwU7YEsRUnrnFnuMvttpGDI3AdEnaS6WYvxgp2JJUhVXGJmZT0Wx2Jh0tlwKbU5P9PR7vAO8NZ4mFQd5cZ7BIaoFj-K7SVu5U2_t6K-26e8dgY-8Pc98rEk60MB19XH5kLz4IvfOYh1UcHLdYn86bRBBBFXDYO_vKRF5AvXCBaUtjWGBao3U-MZY3Yf6cBmS0cFjB9y2vdcasRzl6S0ElW8WVW70p1dis" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=ViBJmz3Gq5Cbji2WgRxIkLjJY8anLFmvUDKI6dhuWWQWxgoKNm2j2zTNdkAMOaNw0Zm6yAkHCMDljwzbVwa6_a6JDy5BFTqJkS0QMcI1nQntJdcKB3xBg5mdXfZVZlTIIvbKKt29CZomzaS8YKddsOG6YbhOhwbS3uAlGDjhadNkroojNv7Hq6AccaeDzWEqAJI2qDEmUvL5Xuk7K3fn9hykAGarIWfFokL1--J4godOJcvh_d2to1j6SOVmmuYwaTZbVodXEGZYsZbfDpwnLEyTVPHPCwjZeuRUQkyomQmdjE3IBZXKh-Nb_w5rypafocvsGB97A3Czixa2qRQF_GDnVhgkUJv25meISv22IAKq3oP660ed4Zd-f85KDTJ98wVQqZWHG3w-oS_spKNhdtFStLNLdznoUxfmQyOG4iOHOmi52TAYJ7FvalaWJ1DhQN8chB0v3gxwU7YEsRUnrnFnuMvttpGDI3AdEnaS6WYvxgp2JJUhVXGJmZT0Wx2Jh0tlwKbU5P9PR7vAO8NZ4mFQd5cZ7BIaoFj-K7SVu5U2_t6K-26e8dgY-8Pc98rEk60MB19XH5kLz4IvfOYh1UcHLdYn86bRBBBFXDYO_vKRF5AvXCBaUtjWGBao3U-MZY3Yf6cBmS0cFjB9y2vdcasRzl6S0ElW8WVW70p1dis" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BP8LR1JLBxoQnlCsQPgqimtcbRi_wE9oYLWEmmbmPxVrai97xxQjzo5YJnh7hgL-s8nfFDZ-wxFjldp_YDEzBxHH6vXRCfl-rLZfdnXINUATZnh4QYuE5KjU0-rQ_W2jYHTlalwv6Tb8VF8Z89d47iw-nOFTEhp7JytZNiqonqH_AJQuPDO8LkRjjWf31J6wMofOIdSMSQjEXRF1zBrLUjqGlsA_gFmfrD8Y6ZAj5-JFhKKFRl3liqfi2O16Ds8H5irkXotKdw3f7IAMoHg5zHbHaHFaZn4l9rDgHVAH2PIslyeZh_W-V0xME4dvkCOCFIeaqrDATSWETLbD1JWQ_g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/emuB3hrAfsEipjN_KifOuKPQ_z1Z-tVDJqVcY3WCEDH0LcuLricFdUzZxFtfGgzrSK1Z3SWs-hG6RL3zKvAxPNF8QpVMdDoqm7-qPIrCU-_ByJu41FztQMar1f6c_cnyNaqKeu1tq47Nq67PRGhWwBR9jDBWgbaCMswz5c-WFhoZMxVUPairUY3sHkliW-a1EDyaZQhZkT_pLhRfUIvOkS2CK2Y1gvn90lF_z66RpHWrLYOVPklLTXYOoJz45hX3YyUu9fgmOFrrnX6U5_TkXNGdq3om6vhgu3fxtvCgTQjB6dY0TihZVAdvY2OX_mMrh7z0ijHDF19bgEXQ9WwK1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aWxzbvKZz21AAG-RRbEHAptvhcr3dQu5GVcoDYiLuAgrmxP4H_cr0KeRR9gHk3TRrFFhq-7zFIJn4CN9I6WOmBAo8WvKuFLQojj1t8iK3QrRaPJXTipVj9jMfB9liZiqNjwzrTb3d9JkD7_TjO1BtmWWi5wyh3Ew8yhdv1iiFSc_E7EFt3OX1biGXR-P_0Wp-JeoLjRdBifGq_xYpV4ODgUXnb21w_I96f5b6TlmpjVEFsDWUjsqlaHqbyDJzgFeM1y1ts0ra4oGFK-HcdDnQWHVBpd3d0TEhMWuefPfMykc4-08Ek4bLtRsnV7hveouDKM4FkLe4X67knU8ZWb2gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AI4QQF3N6SQXRwREqaIBoqRFlxQuI4lNi2_HpnvgVDogQJQlg6jd9tvnorbA33CPG8yHKDaoFoSd_hoQr809gSAoirsG4FvIjzPMvc3gaeMSY5Fq1h1h0BDhaaOmu8Kwpn_GHNHWATNqSmkz-68B4v94BdGzz6oJq5pSedWOVn4LYcN6QInP93VabGTAUIJBa6cIzVsSGDFtNo2q5BSGBcYu2mdyfmHNxUAucwP5wO0eGAlAlAh4yH5X4EJSKSKtJ6Z3wTu3IdZ0WUSMRDGf-XaAM4DtfbpXiY3HUtxCG-sd2eQ1gHnsAFmEpAhaDLtE9iNiU3eQNijyWIGOzXfgtw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cntLLR8czpvYkigdOywN4kAv6A71_HweF8o3gkF2ALjAiYKNzwppYw8tsv1Y9wOZwl9hRXG3fgGL7ARjIKZntoPNRuyn9mLCacgrH1TakxBbMgD8wnpypdatwdP1X8eLBsFA4YcayenRS59G9E7JJy6DSJWXsR4OnrzJ-ZxJablxcULIRm_B4Urv9H2OF28oHubcs5P_lFRny4M-f5WG2YmTDd6R0tO4kVkDehDCDyib60ZH7ntqBbqWnvFhIs8_Q6wPoNLjRwKxGimX8nZYyiSt5-efBQrf4GwuFgpHarj9_BVzM6p1adr7V9YEazh8RmBkKG-bk_9kcYF3NpED4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=ngcFTQTvxuoQfUrDutcjYcKZffNOkgkpsP-BdNILgwKsRjzwCQ6XSq5GaFXhXn0ElqgtYb64z3LvdxIC1Gd3COObywVDJiti89knzBQot5dl0lyqeNF7-F7Lh5BzIhaaVA4irAfuQ8-4oH5eAnCdquDWboweXGukPhtB-Jo7TigSSWj2c313k8U9vILbzMQ4Qdz3foaZQzqqCVX3wyJ2-0MTb5NDejwncmqItAe6rUe525C98yiqxRZZFYHqFHVN9MrDE_RKObPluBJ-FvSRQp3o4rrwR33DcOgtMdg18c7MnlNOdUIsC0BNEwPyQOgoXWZuLZoI4DWe4cdFXAzp6U5GQPJEVQH_3pyOTL0u6OX1tbVE6VQpmBzWNECJWO01daKPH5ysbrrCRo_lnHKkSYovXhAx1KfNETsSfzx6KRWHjBe_MliVJxw7Qmon2PpLDkbWEXGEdo0BCDx_L1km01LCBZnbfM3gROzzTs3_6U1YAOQEp_pxhy97PAcd6xEfSh8B3m9kV9uFYZGFpLZPEyHP8P_C_0qghTmhJZzHMeUe8pynGHxY3QyIyvNjhS9x94RZ-FxPFze7Xm-1ZA9NcP8TGh6mxpEq-8FaWX2v64J1xKklcuX41KZRpGKLzSgbl_c5p5LUapyV9W7wWlYhQcQ4RhWDlMGeWjGkkz1lGIo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=ngcFTQTvxuoQfUrDutcjYcKZffNOkgkpsP-BdNILgwKsRjzwCQ6XSq5GaFXhXn0ElqgtYb64z3LvdxIC1Gd3COObywVDJiti89knzBQot5dl0lyqeNF7-F7Lh5BzIhaaVA4irAfuQ8-4oH5eAnCdquDWboweXGukPhtB-Jo7TigSSWj2c313k8U9vILbzMQ4Qdz3foaZQzqqCVX3wyJ2-0MTb5NDejwncmqItAe6rUe525C98yiqxRZZFYHqFHVN9MrDE_RKObPluBJ-FvSRQp3o4rrwR33DcOgtMdg18c7MnlNOdUIsC0BNEwPyQOgoXWZuLZoI4DWe4cdFXAzp6U5GQPJEVQH_3pyOTL0u6OX1tbVE6VQpmBzWNECJWO01daKPH5ysbrrCRo_lnHKkSYovXhAx1KfNETsSfzx6KRWHjBe_MliVJxw7Qmon2PpLDkbWEXGEdo0BCDx_L1km01LCBZnbfM3gROzzTs3_6U1YAOQEp_pxhy97PAcd6xEfSh8B3m9kV9uFYZGFpLZPEyHP8P_C_0qghTmhJZzHMeUe8pynGHxY3QyIyvNjhS9x94RZ-FxPFze7Xm-1ZA9NcP8TGh6mxpEq-8FaWX2v64J1xKklcuX41KZRpGKLzSgbl_c5p5LUapyV9W7wWlYhQcQ4RhWDlMGeWjGkkz1lGIo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=Vu7WeJqy8bgI_amBo--Y3-jU0C-BORD1NrND20AREWcwVmt0o13xe9AG_rCXRtA6WKj65JQBpAnbPs59hYuOH57AqXtuG7q0bIZdDuE1_CPunbrh7ylqQOcrCQ3mfKG6nLdNAjHiM35UZx1BDWAoKv7_OxA2_EC6KHlpjEOOy4xKP-sW0xQYtqMgNfglZUjnZXIWEYF_ehnWF40KkLlhh9RCyN0BIUtium_TDVb7G3Ibc2NnhuLuChegZaxRWFwtz3itJXuC46o-hu1tTCnN8lJCEEB1thFdBGQPQpg63lMCgFFmvrW7Vxt0tDSRDt6yCjSSdM7VPlJjiaqizIErIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=Vu7WeJqy8bgI_amBo--Y3-jU0C-BORD1NrND20AREWcwVmt0o13xe9AG_rCXRtA6WKj65JQBpAnbPs59hYuOH57AqXtuG7q0bIZdDuE1_CPunbrh7ylqQOcrCQ3mfKG6nLdNAjHiM35UZx1BDWAoKv7_OxA2_EC6KHlpjEOOy4xKP-sW0xQYtqMgNfglZUjnZXIWEYF_ehnWF40KkLlhh9RCyN0BIUtium_TDVb7G3Ibc2NnhuLuChegZaxRWFwtz3itJXuC46o-hu1tTCnN8lJCEEB1thFdBGQPQpg63lMCgFFmvrW7Vxt0tDSRDt6yCjSSdM7VPlJjiaqizIErIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=rDnUIVULzyvug-GIg1lgR2W8gJrmQfgWPGtfV18iwGC8YqpTkc5-3VRrSA41HgoMVANYeIVUvrhQq9FjtJ9fdG1Xn3aIj8WhDo44357UQIGzVDTBJ8N6P2aZB5uadn_FkxRpR0URtgLgKT3UW7sn_sD2ltY59Fka6jujzt8UFmYUtatWyNZQqU7H-oQcm9iuQJS5NzIhP4vCR3YuYZYC7d_oKvDqdwQCS_6NRmg_mMNlbbOi7vcQSQpFFO1n9ZTIt5zIAq40FQVP-l69yrY9J3tpNqfErX9nQmaVYHgL5dUB3UTMpwIfNJZKkd66UeoW8SgZeNW9V4kvvoLawfu2Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=rDnUIVULzyvug-GIg1lgR2W8gJrmQfgWPGtfV18iwGC8YqpTkc5-3VRrSA41HgoMVANYeIVUvrhQq9FjtJ9fdG1Xn3aIj8WhDo44357UQIGzVDTBJ8N6P2aZB5uadn_FkxRpR0URtgLgKT3UW7sn_sD2ltY59Fka6jujzt8UFmYUtatWyNZQqU7H-oQcm9iuQJS5NzIhP4vCR3YuYZYC7d_oKvDqdwQCS_6NRmg_mMNlbbOi7vcQSQpFFO1n9ZTIt5zIAq40FQVP-l69yrY9J3tpNqfErX9nQmaVYHgL5dUB3UTMpwIfNJZKkd66UeoW8SgZeNW9V4kvvoLawfu2Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DSpEzHwDJYfCy4EIehKTE-3dH5LxUOQe8V_EVc9lZk3_k3COsAy-rui-p8wNgA6n933tctHfQWE4TiJiVYRSxL1OzUApRQiY1ixn2MFDLyHhO5i2a17OmRBWpcgZO-oiSS8T8Vuo_c2mli68X6qyw1xU7K3XKjinjUZKj9sG1fPw4b5SFOM0ozpovOgBh5n23DArWW4zUy0fsDSDuuBHAxTj1EZurgbRU611YTJH-v6Ow43VRc4Gp4B0ee_h1w77ysdRghqfgWj3QMwePrNmf4gTmdKcUTeoPlg6DQvBkoGh1Qp8i58yZ1eKspNugLzXpi3_-zspQHt1RJFca0M5mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=B2zaC0PgEwvrQxYn9D_ZKRXWB8_8bWiQOJ3AXvYynnaQWNjO_sJSNzrBhhuJ0CgSQIRdBM79JKebFeh9Dt24qllf9HNtGnlt12pl27r7hTwgTFSI_I5hpUnUZnZrgrxXNQZaII_5cJhem84haMQEv0lFmd6NzwablMdqjfgGaXl0nJohgDI1KxfdhQ4xqHCNcW859YWYFd8ykZA9haDNjqzEHSSH4EowzUpZIpex-ZnrlPsMkeEBGMaxXHIJilXlL-T-J4V211zZQLxfKd_UTJwTsAJxQgVXtLiPntIhaNyBehQye4L6_5mPhOvhq02iLZ7GItx2GcM-8jVyjyzlAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=B2zaC0PgEwvrQxYn9D_ZKRXWB8_8bWiQOJ3AXvYynnaQWNjO_sJSNzrBhhuJ0CgSQIRdBM79JKebFeh9Dt24qllf9HNtGnlt12pl27r7hTwgTFSI_I5hpUnUZnZrgrxXNQZaII_5cJhem84haMQEv0lFmd6NzwablMdqjfgGaXl0nJohgDI1KxfdhQ4xqHCNcW859YWYFd8ykZA9haDNjqzEHSSH4EowzUpZIpex-ZnrlPsMkeEBGMaxXHIJilXlL-T-J4V211zZQLxfKd_UTJwTsAJxQgVXtLiPntIhaNyBehQye4L6_5mPhOvhq02iLZ7GItx2GcM-8jVyjyzlAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=sQxP1LsiilAp8ywYWi-NxE99E9KE07-Bj7xyg6e6g9_pFoaMTg8xN_TCuNzIgBPPUEWbGQwlu_cx1wBDBkAMZZQnbAm5yuaGNmyhzHB2ntGO5pjFuY2Yhopk7FytrGZG5WF86pjbXt-UDY9eqQs1VQcN3JG7HxysYrYddKFVWLxZmd8LjXGecy22EmrwkLIev2B4cEeZCAhQS1qFWA5J1qbszaJkX41Uie9RVjJXLqroK4T7c4OeDNQt-4P4F5KLRaW91yY00nsnZhDG1Qvtp3cRJ0oOCgswxu5eLLi3luwDxNN6V2zy1806EVDtCSHldJre5y-S_bELEz1cSHEuOLRFjT2mYPazRNqmlX7Rw2Pujg5UVuefsEBXYMi0tpzuXZzxLpia_yoIQujPaTgjn2gZFP77eXQGgmH5YPpkwQyWs-53xkltNmv4oWMrHOM57l3Tv6wdgUMx7prVyMeDeu7r-cxPt1MXQmD7YGWtHcB_fUzqYL51BKGjWeT_3dDI7hyUeMyaXnpC4x7EiOw2HREbwyjJwvm39ffd0CUqMxEdSRGozjcr8sivn5rjYJ7MYNmLwbcnLNLyyCpTJLr-m6Pinr2kV4X-DGaZW9o-uvFsTRyPtkGLNE9f6_k2fWgI7DzRqs9pZ2lVY_zv2d6uTpeN_PuqbycJjaGysu1mkAM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=sQxP1LsiilAp8ywYWi-NxE99E9KE07-Bj7xyg6e6g9_pFoaMTg8xN_TCuNzIgBPPUEWbGQwlu_cx1wBDBkAMZZQnbAm5yuaGNmyhzHB2ntGO5pjFuY2Yhopk7FytrGZG5WF86pjbXt-UDY9eqQs1VQcN3JG7HxysYrYddKFVWLxZmd8LjXGecy22EmrwkLIev2B4cEeZCAhQS1qFWA5J1qbszaJkX41Uie9RVjJXLqroK4T7c4OeDNQt-4P4F5KLRaW91yY00nsnZhDG1Qvtp3cRJ0oOCgswxu5eLLi3luwDxNN6V2zy1806EVDtCSHldJre5y-S_bELEz1cSHEuOLRFjT2mYPazRNqmlX7Rw2Pujg5UVuefsEBXYMi0tpzuXZzxLpia_yoIQujPaTgjn2gZFP77eXQGgmH5YPpkwQyWs-53xkltNmv4oWMrHOM57l3Tv6wdgUMx7prVyMeDeu7r-cxPt1MXQmD7YGWtHcB_fUzqYL51BKGjWeT_3dDI7hyUeMyaXnpC4x7EiOw2HREbwyjJwvm39ffd0CUqMxEdSRGozjcr8sivn5rjYJ7MYNmLwbcnLNLyyCpTJLr-m6Pinr2kV4X-DGaZW9o-uvFsTRyPtkGLNE9f6_k2fWgI7DzRqs9pZ2lVY_zv2d6uTpeN_PuqbycJjaGysu1mkAM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=erS6x47ae-6fLH69aT4njt6Hn8qJssVeEcNQ0-x7FbOvwDWdi3eAd-Yr1vuqQYCe828FdSX4Q5eNImdTrHvazmSMvzD_nhYro165OP6qw5i45Th5Vs9COKBF6YRmSFZpNsaIhgq158CKB4KdOgeU0fqyToQfZIQpUCx3FIBcPPYXiXeFp3s3-6iRgXazwpe94odkticleS6jv2m1Z98kSC-TUCr0ysyDjMsQ7V3lzL2NboYkW6_p83AqeRRJMTyyIfDvJc5KaLtWlVe1ilPXKEpfj4yxc7I2aCQ_nZSxE9ht2jlKrqCmYtg3NYGF2u91Bt0Wyfsbg0UofThynSa6SDSAWwnfM2YVPJTap7ubI8wqYRgD4sGaAYYlebOVkn6I8UUpdd6VmTaIoxxXD2QJbtMfml9_n0hcMuj-cSGvTrR8JENCzq7TRDTo4gla-tm1A3aG5wq9iFqpAKrXH64bbsd42oMXpqjyBNYqkx1j_bJagzCLMxzue8GsePeG6ZKOZ0GRv02mtfT8z1XUjy6H16rZ0OmrAPGOUipzcvdhYwz9vadRGyYt_LiM2KMKQuh-czzd_r_4_Ww-cdX3eerO7umCVyACXpXUP-6_oSFV-MGgr8bCPzrb2QEM5fesmfiKF3BArZABBOAwrC6ewFFiZDftude9piTNcQKqwPCXn4s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=erS6x47ae-6fLH69aT4njt6Hn8qJssVeEcNQ0-x7FbOvwDWdi3eAd-Yr1vuqQYCe828FdSX4Q5eNImdTrHvazmSMvzD_nhYro165OP6qw5i45Th5Vs9COKBF6YRmSFZpNsaIhgq158CKB4KdOgeU0fqyToQfZIQpUCx3FIBcPPYXiXeFp3s3-6iRgXazwpe94odkticleS6jv2m1Z98kSC-TUCr0ysyDjMsQ7V3lzL2NboYkW6_p83AqeRRJMTyyIfDvJc5KaLtWlVe1ilPXKEpfj4yxc7I2aCQ_nZSxE9ht2jlKrqCmYtg3NYGF2u91Bt0Wyfsbg0UofThynSa6SDSAWwnfM2YVPJTap7ubI8wqYRgD4sGaAYYlebOVkn6I8UUpdd6VmTaIoxxXD2QJbtMfml9_n0hcMuj-cSGvTrR8JENCzq7TRDTo4gla-tm1A3aG5wq9iFqpAKrXH64bbsd42oMXpqjyBNYqkx1j_bJagzCLMxzue8GsePeG6ZKOZ0GRv02mtfT8z1XUjy6H16rZ0OmrAPGOUipzcvdhYwz9vadRGyYt_LiM2KMKQuh-czzd_r_4_Ww-cdX3eerO7umCVyACXpXUP-6_oSFV-MGgr8bCPzrb2QEM5fesmfiKF3BArZABBOAwrC6ewFFiZDftude9piTNcQKqwPCXn4s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=P4nwlUSogvW0aO4hd7_wyozEZK_nwLGCPQqbaYE6n6i_EUdsDKLemV10rqsw3Doau5BEVMQcbrQ53_RJXSBcGk4UTIVSLHTPMj9a07otELOwgml-yaF0bUOhgLwrJbNepBGYeFRAnUfFYnKvBJJTDQz1qSxGIEs3WOg05hbLnM8H8Kow3at0HlcNZJoZPmuIYNFihf8wir1AQyQYPRdJNP7WQ58jQ8TelK-afSx53mU2WthGNQjVnp2vfHLZInPnXiCOZMtUmivooJgrNu8tTDdmrm41-t_SYgEx0Bf9VN9Qw_BdujwXMhOd-MgfR4zxwIsS-Yvb8REIfum_XnxOBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=P4nwlUSogvW0aO4hd7_wyozEZK_nwLGCPQqbaYE6n6i_EUdsDKLemV10rqsw3Doau5BEVMQcbrQ53_RJXSBcGk4UTIVSLHTPMj9a07otELOwgml-yaF0bUOhgLwrJbNepBGYeFRAnUfFYnKvBJJTDQz1qSxGIEs3WOg05hbLnM8H8Kow3at0HlcNZJoZPmuIYNFihf8wir1AQyQYPRdJNP7WQ58jQ8TelK-afSx53mU2WthGNQjVnp2vfHLZInPnXiCOZMtUmivooJgrNu8tTDdmrm41-t_SYgEx0Bf9VN9Qw_BdujwXMhOd-MgfR4zxwIsS-Yvb8REIfum_XnxOBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=r3sIJc4KfOfyW69aebyIOiJZ9PJ4bjpMhG7oXL1zJjg0rm_Epo12pOgvcsARrJXzLY1QjfXysfwh01Rne9wyKx-V44L0E792oWkf_cXVC8o2KgOB5PPSzl1azWyOHM3NKpPkj2sBNa9zdeiZDDLlAk6tF0ftr67UqcaoRFyaLs8hle3pmsUVPKUXyb-wnkNp91qj3iS6H5or-mQUZ38iL5K0Cx4eePNKxlGsZbf2ZYPA-KoCbkmbUMVJF4NZ4HfAsdId0TFayHBg-ii4YVhn1rcIBVznwMucLs3Kuds9DRiqNsx-rq5u-yOt-0cG_uZxDVFMVYc9oN6SL5r6ZTs3fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=r3sIJc4KfOfyW69aebyIOiJZ9PJ4bjpMhG7oXL1zJjg0rm_Epo12pOgvcsARrJXzLY1QjfXysfwh01Rne9wyKx-V44L0E792oWkf_cXVC8o2KgOB5PPSzl1azWyOHM3NKpPkj2sBNa9zdeiZDDLlAk6tF0ftr67UqcaoRFyaLs8hle3pmsUVPKUXyb-wnkNp91qj3iS6H5or-mQUZ38iL5K0Cx4eePNKxlGsZbf2ZYPA-KoCbkmbUMVJF4NZ4HfAsdId0TFayHBg-ii4YVhn1rcIBVznwMucLs3Kuds9DRiqNsx-rq5u-yOt-0cG_uZxDVFMVYc9oN6SL5r6ZTs3fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=Yp9feUD-PqWcPNozn0eHQ2RngL6ZRIA_lOgXVFddQA1xntwQbG-CX5PRt9MGOrEj-jCve3fiF4cuD_92OfUEnN-yGOPCIXstBhyW-O6R5bNNdRzNrFeJGUZLZ9JkojOf_MljhUQu-d3085hyfcaC7VhClveTwVjkkyFozhugZ3Tdn8_oxxSvDpRSezlMMW2IQTChYDH2gUg7lawKjOoDsr4I908lSdzsUtv23vM0kI6WJ0ClIhUrIpGoxRrPfDhvwEIMUq_RLh03uatUliRWO7dahXdtFh484jEFVVscjH4WiNDo8KG0IQw_nyZcaQlYhQJRD3F47O_RU0r0weu9EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=Yp9feUD-PqWcPNozn0eHQ2RngL6ZRIA_lOgXVFddQA1xntwQbG-CX5PRt9MGOrEj-jCve3fiF4cuD_92OfUEnN-yGOPCIXstBhyW-O6R5bNNdRzNrFeJGUZLZ9JkojOf_MljhUQu-d3085hyfcaC7VhClveTwVjkkyFozhugZ3Tdn8_oxxSvDpRSezlMMW2IQTChYDH2gUg7lawKjOoDsr4I908lSdzsUtv23vM0kI6WJ0ClIhUrIpGoxRrPfDhvwEIMUq_RLh03uatUliRWO7dahXdtFh484jEFVVscjH4WiNDo8KG0IQw_nyZcaQlYhQJRD3F47O_RU0r0weu9EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=vQRH1I9yxAz9LE_dYu_Z-WC-2jtgmfeQEqMmfkEQ-wDxXTr-p2Y7BykE0ON1m_yh-VW9dmr0iwQ9IcXKlzAQLNgzPZoXZ5ptvvns1zFEicuSJEbe6B_Ey8uxTYypzxVXkwu7eV-2eBAs1gVYFhQE92X8OSWJpjcbvwaRZETDuyJP4M3AgxkV8ICO8Qqn6zUpui5WhowewK-mtFrV4whsLCrzpJjVIzTKouZphqcoFmgpD-kMmXgQpUJIQz9JMUtNBJp3FyEa80j3qRBjxXBx0_ov8Yke1wuohQAT4PT_bnOR-IrgM_FG6uiWya1MlbxnC7lKrE1AYsOR842OxS23qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=vQRH1I9yxAz9LE_dYu_Z-WC-2jtgmfeQEqMmfkEQ-wDxXTr-p2Y7BykE0ON1m_yh-VW9dmr0iwQ9IcXKlzAQLNgzPZoXZ5ptvvns1zFEicuSJEbe6B_Ey8uxTYypzxVXkwu7eV-2eBAs1gVYFhQE92X8OSWJpjcbvwaRZETDuyJP4M3AgxkV8ICO8Qqn6zUpui5WhowewK-mtFrV4whsLCrzpJjVIzTKouZphqcoFmgpD-kMmXgQpUJIQz9JMUtNBJp3FyEa80j3qRBjxXBx0_ov8Yke1wuohQAT4PT_bnOR-IrgM_FG6uiWya1MlbxnC7lKrE1AYsOR842OxS23qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=VGz4qhElOkzl4KZNyV4JiPrtVdlJXv67Fgm6k7g9WamtzJpmqy7O39HnLzI3D13kUW9J6CDZCyR6Ty2h5iXZgw_uI45yCU_SK8hlJ17ACjPaYCsNOw6o0if7VFi_DC1RsC86QPpGvK627RAz0KIAW_4RUSM4nJOhF_iNMdnZl5xQtTAIsz6TQ48L4ms6eAiibvKM085Ax9nntLAhCnWRbOfjZyQFhfrXGyfDIok-mqFV3HpMMS_GRa1F4K3BQFtkZkCNd5HY57sHDrz1btHEvhnJtdgP-hxmqR3nFNzfSJ2haTk0Z7IkVV2Dz3_IbLU70qXeTO3fUUl0K3Nk1KWrOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=VGz4qhElOkzl4KZNyV4JiPrtVdlJXv67Fgm6k7g9WamtzJpmqy7O39HnLzI3D13kUW9J6CDZCyR6Ty2h5iXZgw_uI45yCU_SK8hlJ17ACjPaYCsNOw6o0if7VFi_DC1RsC86QPpGvK627RAz0KIAW_4RUSM4nJOhF_iNMdnZl5xQtTAIsz6TQ48L4ms6eAiibvKM085Ax9nntLAhCnWRbOfjZyQFhfrXGyfDIok-mqFV3HpMMS_GRa1F4K3BQFtkZkCNd5HY57sHDrz1btHEvhnJtdgP-hxmqR3nFNzfSJ2haTk0Z7IkVV2Dz3_IbLU70qXeTO3fUUl0K3Nk1KWrOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=ldK3ZmA0DX_sY5RCYzwlLbSC9YzvO2xOHC3ibQPyuo0gvSdCjo4iaXZnX7aE3GO9rCK70wS4zzbB258T1nakAA78B_JeaWmrH97ieNIR9czsxSqS5iiF3CRMy1eYCpizBkmXvzNrdHPeyRNhblOiXuoCU2FMWhtfUBeiRYlG9QIhqkNGjDxty7FYCP8S59DSgaLQqkaUkVkc8RTqEACQKVxcDT_oKCgMzZI9VSW2ohtGK7zI5EbNvBZRsyLaaLIWXOh1Fxxnr2t24PdO9QuOZCFDOI-khlr75zdz6epsb5WPWHI4GwoiOgv4V3HYjFaAaz9HDjLUADrHNCU5ReKzEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=ldK3ZmA0DX_sY5RCYzwlLbSC9YzvO2xOHC3ibQPyuo0gvSdCjo4iaXZnX7aE3GO9rCK70wS4zzbB258T1nakAA78B_JeaWmrH97ieNIR9czsxSqS5iiF3CRMy1eYCpizBkmXvzNrdHPeyRNhblOiXuoCU2FMWhtfUBeiRYlG9QIhqkNGjDxty7FYCP8S59DSgaLQqkaUkVkc8RTqEACQKVxcDT_oKCgMzZI9VSW2ohtGK7zI5EbNvBZRsyLaaLIWXOh1Fxxnr2t24PdO9QuOZCFDOI-khlr75zdz6epsb5WPWHI4GwoiOgv4V3HYjFaAaz9HDjLUADrHNCU5ReKzEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=MW7RZ3bmvyANcfDV2uDRAJJjc2S0WNpZPSnfQIn_KQA6xuWwNHfxA6KQWDINAh_b_61nkuGSmbcBtUE7G8_PosQE_wjAq2z8psJFHRPIC_u4NUsvLv_ppoZJQ0y3oyFX0SDgwPeHReQBGT-H5ifP4J02mR7KMjBL_pbzoeXSrQpCrXmG4xFekHniqfFcyAwlm7Og5UN398k0LgJzvPKyTf12KqHRa3YW0yL5tG-mXdPHxjWS9gP9d4s-T53qgVrP8n_Pw2bXEa1WgFVYibNKy4WDMRlh0uYDdjhh9m8bFEecj9yOUeKOXdyqHWaUyf_1umebbCtgQZsqMMTlMRR0bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=MW7RZ3bmvyANcfDV2uDRAJJjc2S0WNpZPSnfQIn_KQA6xuWwNHfxA6KQWDINAh_b_61nkuGSmbcBtUE7G8_PosQE_wjAq2z8psJFHRPIC_u4NUsvLv_ppoZJQ0y3oyFX0SDgwPeHReQBGT-H5ifP4J02mR7KMjBL_pbzoeXSrQpCrXmG4xFekHniqfFcyAwlm7Og5UN398k0LgJzvPKyTf12KqHRa3YW0yL5tG-mXdPHxjWS9gP9d4s-T53qgVrP8n_Pw2bXEa1WgFVYibNKy4WDMRlh0uYDdjhh9m8bFEecj9yOUeKOXdyqHWaUyf_1umebbCtgQZsqMMTlMRR0bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=LTfDWBV7Pe0kV3vu7Su4t0FQadSLqZ0MS-QMsd7xBF61G8PsUhXclcuYgR8cI8tHmdXPUe70FzdqGUEFyCjFRr_befRumlAS4bUpftx-yt7J40mevcJiyzrUnZAD6N5vCA2sMM2_kHYV9PaDbLosiTMIb-Zv14vaEtoWhVbpVxYjPOmRYKFWi7OFC2FF9KEPvOTCrM58TydXMJ1s0z_mpSjT_gePFQUeFE4msSrd7S5lZzFpT5hNX_SFSjp7NeD6XGmQF2pBx2Du5k56PNUitiwUtmZl5N_y8R_56rqpRuEWvVn5gUhlFHg4ZCLGcFZrk97lBTYBAKdQ9yAm_lF_BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=LTfDWBV7Pe0kV3vu7Su4t0FQadSLqZ0MS-QMsd7xBF61G8PsUhXclcuYgR8cI8tHmdXPUe70FzdqGUEFyCjFRr_befRumlAS4bUpftx-yt7J40mevcJiyzrUnZAD6N5vCA2sMM2_kHYV9PaDbLosiTMIb-Zv14vaEtoWhVbpVxYjPOmRYKFWi7OFC2FF9KEPvOTCrM58TydXMJ1s0z_mpSjT_gePFQUeFE4msSrd7S5lZzFpT5hNX_SFSjp7NeD6XGmQF2pBx2Du5k56PNUitiwUtmZl5N_y8R_56rqpRuEWvVn5gUhlFHg4ZCLGcFZrk97lBTYBAKdQ9yAm_lF_BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HBJMosI5QlRIcIEA3EDJW4t-rM3q07OB6qmwzSU7ypbQwinQXgf_h1e-yHZVj21xPzjPqvrFbqZbSMruSjCiaDvkWHoXShCb-BLRrtIlykwsuAx4B1nxCroyNAzdA01DQcifWda-dPicTLms16EKBi6Feh5Nq78RjvHnJENTYDtV8EBq_r5vIrGf8Q7eGWNG0F89s_CAn-6Eawfg5T54InijQ52CZdSQL2-zQOo-E1ITpUGSgUaXcm7il_CAX_J6Phz-IIcL6Jdg2h2SpjaRRdhq2butQ0SKRxXbk1uoroujiQgMkuzRmzyQgRMkpeCM2i56ZNk4ZBE-q5-dPeMJ4A.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=mHI_aKSCaLfsA-zFMuDh40r977FvwBJZlzA2-O22aFiwyUkmWtffRzmw_evP8WG1tFEIqC5qk9g-oyYIP79eGdosavEi_UsKN2VpZwkogWpYT3rIPaHQXI10MT86Evv0uNAny3CB-RXhyeGN_34nqmOAKFJPEavguT_50jErWZFjhn-lBPvDbNOvZjqkk-Te7xhFvfFZk6dE7Xq4wf0DDqJtAzyrGToY_86n8fxA5C7Zt7MnU7AtblmMucbCppfc5vk8YsXLIFfqDLTdL003v7LIjd-snMnINfXDLUezieHhFYp8pOVXKJ3PRDcl5CdGHsfG83KYshU-xx4J2GWHE4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=mHI_aKSCaLfsA-zFMuDh40r977FvwBJZlzA2-O22aFiwyUkmWtffRzmw_evP8WG1tFEIqC5qk9g-oyYIP79eGdosavEi_UsKN2VpZwkogWpYT3rIPaHQXI10MT86Evv0uNAny3CB-RXhyeGN_34nqmOAKFJPEavguT_50jErWZFjhn-lBPvDbNOvZjqkk-Te7xhFvfFZk6dE7Xq4wf0DDqJtAzyrGToY_86n8fxA5C7Zt7MnU7AtblmMucbCppfc5vk8YsXLIFfqDLTdL003v7LIjd-snMnINfXDLUezieHhFYp8pOVXKJ3PRDcl5CdGHsfG83KYshU-xx4J2GWHE4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=fVlQHtGupfK75plYPzxNjxOI8fdSj5NdJUUoveE-wYeGsHzpGw6JnB9mSUvJ9t307M_NG65Jm0o0GxGtd2Nqo4enLeD6J2bL73mlBV6SibqTDZ39JIUkKeZeVOWcp79RLRY8euV-8HJu3BX__vS0_ngdD-URjE7S9OenfYl7FJWhV9eAUQd-MNX1n2JKVOwVLs_rIcCVl_qc3lbZkQjo-8PENOzhQoECn5zPWAz3M0sLvhuxwb0TQomusaJf__aX_IpWr-V01HYvbtXjjS6YAZt9EhvEI3gJjDHVhmKBgne2GAkokXOufV8LBNqIruM12qN2hidN0aWxLF4i8bHP0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=fVlQHtGupfK75plYPzxNjxOI8fdSj5NdJUUoveE-wYeGsHzpGw6JnB9mSUvJ9t307M_NG65Jm0o0GxGtd2Nqo4enLeD6J2bL73mlBV6SibqTDZ39JIUkKeZeVOWcp79RLRY8euV-8HJu3BX__vS0_ngdD-URjE7S9OenfYl7FJWhV9eAUQd-MNX1n2JKVOwVLs_rIcCVl_qc3lbZkQjo-8PENOzhQoECn5zPWAz3M0sLvhuxwb0TQomusaJf__aX_IpWr-V01HYvbtXjjS6YAZt9EhvEI3gJjDHVhmKBgne2GAkokXOufV8LBNqIruM12qN2hidN0aWxLF4i8bHP0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vIvKQLYOoiM78kvy6YkU0pF8SkQ9GEZDGVfmJsi71OCmw6J7ojRat5GQelOrqbh5myiK4CFvuwvLKqkDl56FqF4MXpWHmmclwbUe3olpUS4y2xYG_tDbXY8v01l9nCSCGIbXEAFN32c7fBZpdNlPv37OQEFJX02iGXkrVqbSMOt2sShR77yIcYyjSxrJp0Q8mkxEf2Xg-iVZLNI3KOkx2HUDEkxu4lKVtHix2lZxCPWxjEBGSGMOkG0C1kLZ8ymclQcm8u6BOuwZ7xfWUklX_P6cIcxdM7FhH8vNyv2KBY8StNRxGrjn5rPO-o1VQwaZvadWqmpy16MozjGnpMLAyA.jpg" alt="photo" loading="lazy"/></div>
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
