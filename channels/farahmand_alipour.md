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
<img src="https://cdn4.telesco.pe/file/DM4J-7KKmtvgmgL0Z6HKxyCJohe2UynowhQJpMw_MPnxqAe9oBbtEr_5MLCvkMvMzmC8WvID3-MKtN9EbfqsLvOUBVWgni_prH9FpX1KHLSZBINSAid4iOEuieBV_QXz5vLqRUx8ujdpxNkBI9ft-wWzfCqPvsFV8-m6h_bYxkEmXx6Kg2kNuOo_NrpyObRTq4wljlAANYfiXGLhrbesh61DHi4EXpzE-s_loASzmcQ8gKTyWd66Myjq4_u-erIimqjyVaUHlkk1S7jCSwVMyWZDs-w4evizlOtzZjJ-LhyCBdQXuaKdSk65enxbaIUaclE7lQJzKBFP0aqJZyCjrA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63.1K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-28 10:56:22</div>
<hr>

<div class="tg-post" id="msg-6750">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8LRAaqsmHThwCVIappFeoKnMd3ljpwiCLf1P2EQ4ryev6LCVaLTHOHiZvQ6PlEqKbsEYAzPMuT1iXURduUBbP5cB9yt04W3SM32J7gyE9C5NtXJHfLz2fCq8LRkvb2ejfJljMuWIqSF_Q2vXNni3-MdLUR_VgF8g6m87-XQzl4xGSLsrjfvWhJe26tWItOtw2uaSOlKmlEzaUKjKtfolP0cNQocY3VimutH8F0Vx4C_jYvwM8QjNzX-wlgPdb4Zh9t7195cixej_LFQc1MfE96LLYiVKcRIiD2bOj5S3Yzg-fT2G-OY8LWdXRgukJzh8PVSf7-stNCHhCq3Qk7lESds" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8LRAaqsmHThwCVIappFeoKnMd3ljpwiCLf1P2EQ4ryev6LCVaLTHOHiZvQ6PlEqKbsEYAzPMuT1iXURduUBbP5cB9yt04W3SM32J7gyE9C5NtXJHfLz2fCq8LRkvb2ejfJljMuWIqSF_Q2vXNni3-MdLUR_VgF8g6m87-XQzl4xGSLsrjfvWhJe26tWItOtw2uaSOlKmlEzaUKjKtfolP0cNQocY3VimutH8F0Vx4C_jYvwM8QjNzX-wlgPdb4Zh9t7195cixej_LFQc1MfE96LLYiVKcRIiD2bOj5S3Yzg-fT2G-OY8LWdXRgukJzh8PVSf7-stNCHhCq3Qk7lESds" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن
مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره هم بهشون نمیدن.
انتقام خون خامنه‌ای رو گرفتید؟
عزتتون مستدام!</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/farahmand_alipour/6750" target="_blank">📅 10:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6749">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">وزیر نفت اختیار فروش نفت نداره
صد میلیون بشکه نفت گم شده!!</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/farahmand_alipour/6749" target="_blank">📅 09:55 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6748">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67af3237af.mp4?token=GFwINfV6g5amFzus_aTWpLZn2kYItUs1TN5n8UUWO0sO-2xBeSpitN0yp8h6Wp1xQtIu1oRIDfln046ZhxpIkpIkGpTJ8IJa6u_8-1VyEhxPA_HcAGPLFbKesIwY3lVGGRfsJJpsk5eb_BBkKDGbki7Uwmq4pCLMpxAkOo1xMhHwtZZUgVzA_o8A4IZH4qVjqiPCN0pQueDPpXOS3Tk3G-GATi0TV1m5g31NeyI7G3rvLvwoLXu-RcT79lW-pvIw8RFWLNrubo_wKF7K1aiA4_cK3RZKD1dj5WA8Qgo9RTHSxolN2sgR1vFAiFJNHXkiEH3ncECLr_-j-PTErD8vUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67af3237af.mp4?token=GFwINfV6g5amFzus_aTWpLZn2kYItUs1TN5n8UUWO0sO-2xBeSpitN0yp8h6Wp1xQtIu1oRIDfln046ZhxpIkpIkGpTJ8IJa6u_8-1VyEhxPA_HcAGPLFbKesIwY3lVGGRfsJJpsk5eb_BBkKDGbki7Uwmq4pCLMpxAkOo1xMhHwtZZUgVzA_o8A4IZH4qVjqiPCN0pQueDPpXOS3Tk3G-GATi0TV1m5g31NeyI7G3rvLvwoLXu-RcT79lW-pvIw8RFWLNrubo_wKF7K1aiA4_cK3RZKD1dj5WA8Qgo9RTHSxolN2sgR1vFAiFJNHXkiEH3ncECLr_-j-PTErD8vUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم تعرض به کودک در کلانتری
نیروی انتظامی جمهوری اسلامی آینه تمام قد نظامشه، وحشی و عقب افتاده و‌ خشن.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OxCZqM90KVWnX2sBR0aPmmOl2LJFzVU8ry9RNId1sWC2ngzYKE1D4tre_Cv46WDTORTqmEp8G6UYBJtEFlxA4XyhLHhZ3h5ZI9DDqbGUj3GHtR6YeV_tD631Wp5p2dJdMBFp6FlaIkt355Qw318eDSC4dvfrUGpvTcZmcUIEamoua50ELP3nlBZ6w3qTzH8OGpFBjndCwEAV9dnorMOtUUrD0U58t0dg7jcPLmcTtdqTyQDnNkckCsd-1wq__3yvqhdcsvkOBRfb1NTEQ2TsaeBPl8mZwT-ox1wqsRS1fYjUW4Gl0GS9Iy-GSq0d_uRJfwZx-yhm944LQtz__QTZOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=rY4fepG24-lCTO8ulPpH1z0D6Njz-dEVo_WUAjzmA0VXF5HC9FxpIjg4Cbq4qlI12X6zks_4NtCLxH0k3g2oVuGqa_hX6h3EH5KzK09mK0tM9aEg7DSIJJ_R5Y5-dNfJmHWIBssBbk5RqZOqd71volqbvaVgwzOYVeJ0fMIybI73SfQKMlNlXc3WdYR5Nx7D-EYoiVkBHqc2doVwq_QFYP67HATAQu8aIj5oMb9kgDALWLw-CC1MQvQA5sPtedp7oiJp58ccM12tOChQh7ybjCwkvKNmqa9Z9MwvXzOOlCeBuXWPBMSU3HyUCawfotkRyEQdN8ZTm5AXSN9SQWdmIGiGMvrTTAGRwU5yZ6zLJEb25bgE8jAyZoqfvov7t-tzqY7VFnSpEmKQPKVEBrb9qfj_H5FuZogH-WN12DKFuODILIFV5lJAAYisPpFgVot7TKHw3H-VGyFIKAM0hXBno0kHAJ5XF1HNf72aOURyigRw3_Kj7tIk3QokAPZHOYZQAMm_Z3Z1nXPzy_HrkEFSzR3Zk6nUftxv8rnYa8jHsqAa-o-VUteKvmDWRYok3WudwSnQoqRi0RhKtfhkMG78t5awA1TT__Vw2NFSziowMwrq-ouz60SVYxJjDQisRtYvUHI-mUJOGFaPV1SairONwVQkSqLJrzPLu36JrMOcoM8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=rY4fepG24-lCTO8ulPpH1z0D6Njz-dEVo_WUAjzmA0VXF5HC9FxpIjg4Cbq4qlI12X6zks_4NtCLxH0k3g2oVuGqa_hX6h3EH5KzK09mK0tM9aEg7DSIJJ_R5Y5-dNfJmHWIBssBbk5RqZOqd71volqbvaVgwzOYVeJ0fMIybI73SfQKMlNlXc3WdYR5Nx7D-EYoiVkBHqc2doVwq_QFYP67HATAQu8aIj5oMb9kgDALWLw-CC1MQvQA5sPtedp7oiJp58ccM12tOChQh7ybjCwkvKNmqa9Z9MwvXzOOlCeBuXWPBMSU3HyUCawfotkRyEQdN8ZTm5AXSN9SQWdmIGiGMvrTTAGRwU5yZ6zLJEb25bgE8jAyZoqfvov7t-tzqY7VFnSpEmKQPKVEBrb9qfj_H5FuZogH-WN12DKFuODILIFV5lJAAYisPpFgVot7TKHw3H-VGyFIKAM0hXBno0kHAJ5XF1HNf72aOURyigRw3_Kj7tIk3QokAPZHOYZQAMm_Z3Z1nXPzy_HrkEFSzR3Zk6nUftxv8rnYa8jHsqAa-o-VUteKvmDWRYok3WudwSnQoqRi0RhKtfhkMG78t5awA1TT__Vw2NFSziowMwrq-ouz60SVYxJjDQisRtYvUHI-mUJOGFaPV1SairONwVQkSqLJrzPLu36JrMOcoM8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mBgiKWzDsyFQKbC1gEx65ogAuoWPyQrOmBgyRp5-rUaQesw3Gne6u5Efd_cLuvPeZCQ8fRJIl4G1ABpUCoSUq6mINfXJWgQvasLaPzlJJEEAd9pk_-KkYQ_7iJwjjjN9zjGZrRj7_t_S4DDhJHFS_rKIb4C1I8LuO-vvtJZRExVETPcZxeChWRLYHbH99NAuvLWlmxsXp05c8ZNpgU0AvyqbmiUBTCbx6D1Ram9RM6Cax5W3a7y6YNTbuATMay7lXaPpIH_2uxr1aJmqVABwnXmSLytIxpA2X7KxY7OXcYeHu6T9-VnbhkiFSXzRRpLs1VfOZvFlDE_PCdxAKYX0gQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6745" target="_blank">📅 13:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6744">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=UozVxjnXEDrgnV6hyx-Qb7lGQAaxEDSc9YbrPPa2Ydz0jgkUgOtuFkLqQBjvvzhWbXlPmQItLSwXXimhFQnt_psJSvlBlN3JnqWup-QNfvPUMET0jFfhlpsgAKVyiR0brpbhmVLM6xXm5Xi5FrGvjatNxe2_UK2J0QMKD4Y1izPrQFulRBVx32fJMHc2HnSlidFSQ7BUTq_jVhiBiIzri7I6PKOFcxOSN9RbCjiNQGbU-OutCs1LKiuUQ1vNGL3jYn4yB2iCL4y2572TSny6qKFdyDfIsfiZjIuPxapS9xjPz6xiQN9qmA0sf-LmRiBzW0IUfM3dtecGsdg8RgPNrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=UozVxjnXEDrgnV6hyx-Qb7lGQAaxEDSc9YbrPPa2Ydz0jgkUgOtuFkLqQBjvvzhWbXlPmQItLSwXXimhFQnt_psJSvlBlN3JnqWup-QNfvPUMET0jFfhlpsgAKVyiR0brpbhmVLM6xXm5Xi5FrGvjatNxe2_UK2J0QMKD4Y1izPrQFulRBVx32fJMHc2HnSlidFSQ7BUTq_jVhiBiIzri7I6PKOFcxOSN9RbCjiNQGbU-OutCs1LKiuUQ1vNGL3jYn4yB2iCL4y2572TSny6qKFdyDfIsfiZjIuPxapS9xjPz6xiQN9qmA0sf-LmRiBzW0IUfM3dtecGsdg8RgPNrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9cEyh-c8YVYFsOfkfDj9u1-I9RT181bb0OFdHohpS0w83bAKVCngZrgcJku4SZvzNJ5Yu_bXrjOQahC2Fj8W2-jO66TSZbmlXKAF8Ah-C3yCAtvU3nOAqJNScu614-bmn5eHl-rZwuUN2OHMC2alAdNgf6xOlFPNmMPVedFsioykcqKW9CVenfYqtydUtgOtWhfrCQIsdluJ2quagron3IIlhLAsckN9vZT0KpyKlsZ1UgCc3DVNU9gBQprEBoPQuK3kvaSM_rHyVmwfBKfZVPXuEURVb5HTk2OjpcYOPOlV8DuGYy0wdYYgvZELR8uLVcYkFV2AQH4DjwyBSOGsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/djqt7jeTchA0KXPM7lqatwKNrBdLhkqgZ_1hnp2CpInXaUlH89WnjTeQuI4AeuFqjyfOgKMbTYO4A9bsvsmHFpWJ2h7Mw18uFbHJN9E9h0s2OTWKKuWbiHH5x0_ndgmmZpwqAnDNLdjjjBK5jH6kere1u_cW5wbe12EywgaIf8VjuquPrVmZ5QoGxCcv-avOC4Hm2D_wd5hySonDHtD8BSK51WPdioq_5gTJtzp3IUfV9zvRKlMNXKpd2ufeSj0BKUFQsYItOTz5w1Ufnk8-MQWw3ZvFbw7QQYAPhpMeWPjW5iVklAldgMuDRJYNhdDtX0sYwVW1yfYjZqVfVFv4Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kmi_K5Lt3QJA26TTMCHJ-nL5DV96LSjxrZ3QUDZTl67E6p4tEb_4PpHkCuex-eS0z4-De-DvgtdYUQpscYMrwX0ovHAmrjZ5y_MyhxGpURAS3PvprxafpO-iofkrnIMANF3_kjpErN7uDO86965dkDCwiN22nZYppOF-BbdS7-xqkGlW98ioVGZfmQ9KX_Hl0WSlAZ6eDo5YJXEb--O_uZ7VgcC7bqms5_CdkEG6K6k1qSXrvX_uBpJkXI4DGcYo80pKfPuQ-6ga5nYUV170l5fEBUI41X2iVFcKePpk9opMboNrsGnMNIIfr_7DrRIP-MKStRz0k1H8eGOwQCiEhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=Uh4OIVpOrf0YtsBvNoCm1tKzbh5pW7Y7G4BCvfJuAwLXgRDChHng3dopZEVKX-mhgKXHEeOZIX1DfmbpCjjRZzkyfIMz2qLvixLdSAGq_YHmu7C58s-xvtkLBHXs2y5PDAKJQGGGMC71VBMKRPtZTx5sttG4eJ34n-LVdzR-zYG5DQ4aelXV8PjCFtHKiOOWvMsr5I2wptBqRXkUrovWztbOMIlL0JCh-tvFqvMSK_4tJFVcOmIufYiYAaUe615EtuifASj8rKm7IX4RKnPzZvFX9vv6SqpRtRcHtSTGyCFibw8koLgmIk7-Mmn3vqlKTZu0mB98Uuu92x0vIL7ITg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=Uh4OIVpOrf0YtsBvNoCm1tKzbh5pW7Y7G4BCvfJuAwLXgRDChHng3dopZEVKX-mhgKXHEeOZIX1DfmbpCjjRZzkyfIMz2qLvixLdSAGq_YHmu7C58s-xvtkLBHXs2y5PDAKJQGGGMC71VBMKRPtZTx5sttG4eJ34n-LVdzR-zYG5DQ4aelXV8PjCFtHKiOOWvMsr5I2wptBqRXkUrovWztbOMIlL0JCh-tvFqvMSK_4tJFVcOmIufYiYAaUe615EtuifASj8rKm7IX4RKnPzZvFX9vv6SqpRtRcHtSTGyCFibw8koLgmIk7-Mmn3vqlKTZu0mB98Uuu92x0vIL7ITg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه
مهم اینه دلت با خدا باشه!
علی علی!</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fdCZkXWmAK-z-SCDarSmag5q-GnQW0tlVyecvNhue25Q0HCfaDbvpJD32j8xnP1m2Vv_PBgt0kqfcRbStoPwSOLMhmXAiSIRHGIhVTAaB10IYl7YmAIWjywrAweASsEYfwJjMb7jarYyS95GCSXafLfiHY9bNAmNH18aHUqlg1xmDGOWWHmvdwfxDv1ZkmS9VgC94F5n3vPme0BXiMnJjntyc7eKmM5hPqyHOGkUrAT3G_0WQH2c4K8vq7rAF6TUuROi03iL413UgXO9PxXQTku4HVogGQNIyTeh9BaJHY3X3-Bqw8roN0Z7rFKO3VtkelViTJPfUET0v9rsg8zxXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu4HmQcSZ_AdPWPW-W9NjJmuNISye5s-u9xVtQH2BV3q20MmzuEOmGghWO6YVunGEMuMe4t9wUdr1CY54XmI2ZdaLjZTJmHMeaPYYPiHtz4CDe5esuJUmrhKJu31ldPxzxtl3NtTj3Kd1yAMJUAR69DnP7BpwQFmegqGA_NiRxl_VWoMr3KxRBBjeyv9IUafuB5pkMzFpEri31i80wkCLwUp7so8y8rnEBAVqGePg2Pw2MGdow9g9B7q5t6avRnwvkiGk-Obc6CPSFNN3tD8MIN8vloESZA5J8azJijKDaR0oRaDjqdqjZ1BkhlUePsLEHnAwyAiuVgZMuzMMcgxxvvs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu4HmQcSZ_AdPWPW-W9NjJmuNISye5s-u9xVtQH2BV3q20MmzuEOmGghWO6YVunGEMuMe4t9wUdr1CY54XmI2ZdaLjZTJmHMeaPYYPiHtz4CDe5esuJUmrhKJu31ldPxzxtl3NtTj3Kd1yAMJUAR69DnP7BpwQFmegqGA_NiRxl_VWoMr3KxRBBjeyv9IUafuB5pkMzFpEri31i80wkCLwUp7so8y8rnEBAVqGePg2Pw2MGdow9g9B7q5t6avRnwvkiGk-Obc6CPSFNN3tD8MIN8vloESZA5J8azJijKDaR0oRaDjqdqjZ1BkhlUePsLEHnAwyAiuVgZMuzMMcgxxvvs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=CSoEXXFPLg9wcUQ_nb7CV6nn6PVPpopqWSqMN0TwQ6Mq3NK59s6AkYLHbsuzDHqlznZsmIU2nHeMSMHgG__Kje5_eaOQj_4Xe7KMuQvMwCUy7bnlUChyRB8xk7IJzUUKtPGLyzp5FumpNTtKPkJQ9gStDeE8CQgdYfbniZxiObskP9bYuN_m5vadcbN-wucoOV3jjORYhemO85I42gdDqfWYeoqTd2AVvS6E1FuIiK-suM22HRSLjkl0X--RWbdP2XTS_5Lec6wnow4KXlyq1BqapF4-wdsjXwWG06nc0XSXBAj0JJhfK0-E_rBzByVUIZhvZxrf5eYUjF4jX6zLAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=CSoEXXFPLg9wcUQ_nb7CV6nn6PVPpopqWSqMN0TwQ6Mq3NK59s6AkYLHbsuzDHqlznZsmIU2nHeMSMHgG__Kje5_eaOQj_4Xe7KMuQvMwCUy7bnlUChyRB8xk7IJzUUKtPGLyzp5FumpNTtKPkJQ9gStDeE8CQgdYfbniZxiObskP9bYuN_m5vadcbN-wucoOV3jjORYhemO85I42gdDqfWYeoqTd2AVvS6E1FuIiK-suM22HRSLjkl0X--RWbdP2XTS_5Lec6wnow4KXlyq1BqapF4-wdsjXwWG06nc0XSXBAj0JJhfK0-E_rBzByVUIZhvZxrf5eYUjF4jX6zLAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=gz66sPnXjYc3iqW8vC8ob8d_H9G7YyDpw9SsxAK4v6kXWbwfdYwIHrKuT0m3sWlc787kiW4MdKeWHhUEyk-1OBn9Kzn1uDgmKU_O8zti4MWuPaUxuqVmXlTCT76OvRanz3EG0biO9LQwW8_CPO1rudH30HzhtI1KofNKE045I78co3vpJbtloKTz5ETSUwaPVTMa9ga-BjqAOoC74TTD51_9672ydRg2d1YI2GDL-ShEs80Jl3MoiK8EXtyu3nqapDL5d3LIEotvkPPgINwAPIvEtZmyB60Y-xr8EBJ5Qw0BnaIaD4okVeov-ILHAd39NlnYvAxcZ7eu-0H92m5B7krrL5-5tpH-D04-U2JKvndEywlswbnT8Kv9cZya1VXMfZiue9fZ7UAUdBDAnwNbh-6GRxMN99qcmSGzzEIyU-etTHHYjpWbyis2c-7nyCIVKgi_pSP00sAqnuY0oXNmqlj0YJwUgjh6AjZOO98pDK7aYWg71AbDH9PSEGxMkQZkDUgC3VmdIBTqvQ3argA93tjQDglw8hUeqtAUcasQjme5mF-5PF4YJn25j366oWuhXRCrH5mHrnFtxYxC_-Zmg6qMvIubWi9QmeR-SN_CfvaYf-XCO_TIQkWvNIbb6tbFvMg3QYx5CSfDNagP0blNUVuvDks8QpDreZ4KWOtgzq8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=gz66sPnXjYc3iqW8vC8ob8d_H9G7YyDpw9SsxAK4v6kXWbwfdYwIHrKuT0m3sWlc787kiW4MdKeWHhUEyk-1OBn9Kzn1uDgmKU_O8zti4MWuPaUxuqVmXlTCT76OvRanz3EG0biO9LQwW8_CPO1rudH30HzhtI1KofNKE045I78co3vpJbtloKTz5ETSUwaPVTMa9ga-BjqAOoC74TTD51_9672ydRg2d1YI2GDL-ShEs80Jl3MoiK8EXtyu3nqapDL5d3LIEotvkPPgINwAPIvEtZmyB60Y-xr8EBJ5Qw0BnaIaD4okVeov-ILHAd39NlnYvAxcZ7eu-0H92m5B7krrL5-5tpH-D04-U2JKvndEywlswbnT8Kv9cZya1VXMfZiue9fZ7UAUdBDAnwNbh-6GRxMN99qcmSGzzEIyU-etTHHYjpWbyis2c-7nyCIVKgi_pSP00sAqnuY0oXNmqlj0YJwUgjh6AjZOO98pDK7aYWg71AbDH9PSEGxMkQZkDUgC3VmdIBTqvQ3argA93tjQDglw8hUeqtAUcasQjme5mF-5PF4YJn25j366oWuhXRCrH5mHrnFtxYxC_-Zmg6qMvIubWi9QmeR-SN_CfvaYf-XCO_TIQkWvNIbb6tbFvMg3QYx5CSfDNagP0blNUVuvDks8QpDreZ4KWOtgzq8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=i-naGJWBc-fmO2-4GXfyqu8TZbnVsyGXnwZmtYeDd3zgR03pARoyPr1g2-4IgItkizZARbwv5TFDrQTdZoKPJHPS1taHY175WbFPyeaS3TmFcQpGOjKCd3RG2UOwc3FRLoYr4aYDK2C9llu_ArQ91Hm-sUo9Aub3VENjBpo8Y32G5CAd_3n-uNIZ05fYdZXYkfld0hpPJzEtI-XyYJbWiXwMN7rO_d0z9GrDXA1dpcL3JP84vbICHBkIBD8P2wK2vo0IYAlJwcx_B8AqpD5C1Bf1cFTJy9Zh9iuMStOWv0OVCn0CiKC2uG08voN8t6bYWwNlQWsWGvH4WY-35YHvnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=i-naGJWBc-fmO2-4GXfyqu8TZbnVsyGXnwZmtYeDd3zgR03pARoyPr1g2-4IgItkizZARbwv5TFDrQTdZoKPJHPS1taHY175WbFPyeaS3TmFcQpGOjKCd3RG2UOwc3FRLoYr4aYDK2C9llu_ArQ91Hm-sUo9Aub3VENjBpo8Y32G5CAd_3n-uNIZ05fYdZXYkfld0hpPJzEtI-XyYJbWiXwMN7rO_d0z9GrDXA1dpcL3JP84vbICHBkIBD8P2wK2vo0IYAlJwcx_B8AqpD5C1Bf1cFTJy9Zh9iuMStOWv0OVCn0CiKC2uG08voN8t6bYWwNlQWsWGvH4WY-35YHvnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/olm5am24RRfGfPsdyO1rE8rQ_118hU05zihiYJRbQiScj8SUIbev1wqpWMF2Xrsu2zdN21cfJ-wVtYnqgDneewcd16qJ9FTHp5hjFGncRx8FyvYOz71XSrT11uxjE8o8EpS3cb3iZ9cSUhugi8WgdZH2gbNg40OCa4kFeE7tX5kQRFpplQOQAf5NMDO8T1PpfsHEBZWPi_DAM-50-vSRoSWCnc23kcSi96R9M1E2R7YwnHDmpPrRw5a7f8QAhSzPjdZf7BsCaAVSxYFVxFLCDR3c6-hSEi54KEvLfeQReO9jrImKxFPuP8bVOT0alPyt3H_wv_MKLwhvUdMn46pMuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=IzD2-Zm3SN9pzy0PS1D9hp5FPWvIRK1JCeE7AkcyFNYWtrAxqslP7gC6WQFz0cp05Tog7EE6sERCiBt1_RxOXYOVQV5vP5oIi4tUq4rMlrIBgvco682Bo9Fhxn7sDtRCroinBQZBfpryE3u3j6mSPiaCfzqm0_lPEle_GF2vh2WWW0oPt9OsiFtEPeec1vorP8DRJuMPmmbSSspe3XJHqVyfBIr4xRaalp-dwy0GYakSywIvaJWH8bdZ3njPs2f4vo0z98e4_CzaKGztxfSEOPTt3byGjJQievNExu00LSe4xPDaD7D6YvFMSSQuM7T6RhxmbkXCVPkyb3bSMt9n9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=IzD2-Zm3SN9pzy0PS1D9hp5FPWvIRK1JCeE7AkcyFNYWtrAxqslP7gC6WQFz0cp05Tog7EE6sERCiBt1_RxOXYOVQV5vP5oIi4tUq4rMlrIBgvco682Bo9Fhxn7sDtRCroinBQZBfpryE3u3j6mSPiaCfzqm0_lPEle_GF2vh2WWW0oPt9OsiFtEPeec1vorP8DRJuMPmmbSSspe3XJHqVyfBIr4xRaalp-dwy0GYakSywIvaJWH8bdZ3njPs2f4vo0z98e4_CzaKGztxfSEOPTt3byGjJQievNExu00LSe4xPDaD7D6YvFMSSQuM7T6RhxmbkXCVPkyb3bSMt9n9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زهران ممدانی
به مناسبت ۱۱ سپتامبر که هزاران آمریکایی به دست مسلمانان افراطی کشته شدند،
با صدایی بغض کرده
از عمه‌اش یاد کرد که بعد از ۱۱ سپتامبر
از مترو استفاده نکرد، به خاطر اینکه حجاب داشت و در مترو احساس امنیت نمی‌کرد!</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6731" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6730">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=KHNEQv6-0pK1QmqLYZw9Tj5RXAlk9ohcmF-wJsv7L_GC9-0FIARBhwZe6_lJsCpjZPpQmlqKD-KKpfSWHLVCihXUqkTK6xnhvVQohC_xmSiVn7LeD0pz_grrNpmmWMf4njFfyiIi_Si7DPv3nh1teUFuaRMGsd6Z5Au59JZ_Ncde43Xqy1HlgAHhMhChVGcppYDdLBAM7i9tSLryp8RVGzCk51N2cX6EtTw2AQLglhVLFMAGsyF4A0uu0Npn_swUiGzbbXM_ICtKpSuvns9kwt6gf2SIpIImizmUPU3iqgAHsX-wwTAKchB58I-g6HQ8tKH403H2LKCvjelofqvCgmfuRiER9FQFERX97Nc1kGx27_uMB_YNM9XCyg6Sl3u2SleRKGtFvVujl3Pbmz4F0i55mwMrR1l28wPIsyjUVA2HUwnIxU0Cy_pP5y1rugShl_7gB-iAYl1nCxAnA54xP5LY2_vuNiBqiJ2kGsZEJLiz_vlka50RGMg_vC9eoti-PAjCArsX_EkoGPOIr919WjtZ7YbBHUAzvhnq9R_zip_pqNCg2s-VHoQMXaR1RvHN1A2MX5bIuDBCxR6DpdBv5aK8cYy6WW6dUOz54GU8QNwWX_d0QZeTegHGc9JWAHmqmbCzjg9O9z0AhgFxM41s6UkGtF_q3KEuEG0-9kGvI3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=KHNEQv6-0pK1QmqLYZw9Tj5RXAlk9ohcmF-wJsv7L_GC9-0FIARBhwZe6_lJsCpjZPpQmlqKD-KKpfSWHLVCihXUqkTK6xnhvVQohC_xmSiVn7LeD0pz_grrNpmmWMf4njFfyiIi_Si7DPv3nh1teUFuaRMGsd6Z5Au59JZ_Ncde43Xqy1HlgAHhMhChVGcppYDdLBAM7i9tSLryp8RVGzCk51N2cX6EtTw2AQLglhVLFMAGsyF4A0uu0Npn_swUiGzbbXM_ICtKpSuvns9kwt6gf2SIpIImizmUPU3iqgAHsX-wwTAKchB58I-g6HQ8tKH403H2LKCvjelofqvCgmfuRiER9FQFERX97Nc1kGx27_uMB_YNM9XCyg6Sl3u2SleRKGtFvVujl3Pbmz4F0i55mwMrR1l28wPIsyjUVA2HUwnIxU0Cy_pP5y1rugShl_7gB-iAYl1nCxAnA54xP5LY2_vuNiBqiJ2kGsZEJLiz_vlka50RGMg_vC9eoti-PAjCArsX_EkoGPOIr919WjtZ7YbBHUAzvhnq9R_zip_pqNCg2s-VHoQMXaR1RvHN1A2MX5bIuDBCxR6DpdBv5aK8cYy6WW6dUOz54GU8QNwWX_d0QZeTegHGc9JWAHmqmbCzjg9O9z0AhgFxM41s6UkGtF_q3KEuEG0-9kGvI3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BqnqhC2kFRz13RUjyBAMfcTz7UseSwuyfQDq_E5iF51uQLN4hZ3mgtl9Hu-0PlEgzBLrJamMWCBF6IvJzBT0xo16y17brw-62xl-2wOylo-dllrfP0Js844Kr6cvIuZRKaf859bv_fSrGezYzSxrPFhY-hYGf7Impy6hWcT5XU59SbkSatVASxOx7BSr6Qhf7qYZkjZJBcdEeNkiPMNpWtpxkztXKpTNcAJ9jeF-OOM_nEGhbOiRY-odB3K0t6zp9KhEyG-Wjm-Ihcir1lTO4G17isFDTV14YWKFrXd5yAi173usCYaIuPj8La_X4ffw7wM_5ALTOfrrRjQ5g_KYww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=BNKZToOt6NV1pQLM765kUVwytMhEhC4uCCXFhqSrg-F4EtvzOEguvW8uItE0LuD1a0RbI8V59wJoy_iMNUjn_QTQmvkqojtO2ig7RceZFl3QpfWSJnRTNyoLYgYjWHrg_Fk7w1mUiMU6Ol2mlxGGVrfZoGM_Y1gkZfJZTTYQeYdRFCOin4W4T0Z5XRoZSTiMMcjhjj2x2yqzwowWV-bCvOXIWls5zzMgcLp-PkbbayKNAPwXtCHWsOcJ4dh3T0XeHOckimI9jocNU1leXCHqtE6PbUCHeoBTHvxthjq-qhxiu-KhLRqBZMGpQDOs74mz_Ucdu5rdsQOcKhUhQqqxRUW-f8Uw_AjjX632aZjK0C_BYV6tjFVPX0TJokOVl9xhFam7NPgP3VXFhbSvJ-MtmL0cWiVO4IKOvdOkb0XWlWksFYHAol5I34TJuwmmxqQcmJk1OsSGR4nQyA6YmIbgD1WajTs-Zc50T9zD3jJTQHZvfteM181WMiqTEU9JThiiFNDWAQNv2lGl3uaomBL9Eep9b1FpUyinNBelyPMLgZgCyPB3PY_4LvK6aG-ZTbcH9R3scztKSqER2VBfkRYVAXCJR2ftPcbmwzKolzFFo7qfOWNbOte4OlQHH1lB-bPWftcSF9LZlPSGwN5xHeMCaPA9J9eRS44NNahnHtjSvPU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=BNKZToOt6NV1pQLM765kUVwytMhEhC4uCCXFhqSrg-F4EtvzOEguvW8uItE0LuD1a0RbI8V59wJoy_iMNUjn_QTQmvkqojtO2ig7RceZFl3QpfWSJnRTNyoLYgYjWHrg_Fk7w1mUiMU6Ol2mlxGGVrfZoGM_Y1gkZfJZTTYQeYdRFCOin4W4T0Z5XRoZSTiMMcjhjj2x2yqzwowWV-bCvOXIWls5zzMgcLp-PkbbayKNAPwXtCHWsOcJ4dh3T0XeHOckimI9jocNU1leXCHqtE6PbUCHeoBTHvxthjq-qhxiu-KhLRqBZMGpQDOs74mz_Ucdu5rdsQOcKhUhQqqxRUW-f8Uw_AjjX632aZjK0C_BYV6tjFVPX0TJokOVl9xhFam7NPgP3VXFhbSvJ-MtmL0cWiVO4IKOvdOkb0XWlWksFYHAol5I34TJuwmmxqQcmJk1OsSGR4nQyA6YmIbgD1WajTs-Zc50T9zD3jJTQHZvfteM181WMiqTEU9JThiiFNDWAQNv2lGl3uaomBL9Eep9b1FpUyinNBelyPMLgZgCyPB3PY_4LvK6aG-ZTbcH9R3scztKSqER2VBfkRYVAXCJR2ftPcbmwzKolzFFo7qfOWNbOte4OlQHH1lB-bPWftcSF9LZlPSGwN5xHeMCaPA9J9eRS44NNahnHtjSvPU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :
«مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»
و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6728" target="_blank">📅 11:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6727">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=kublmMQ3t6rQ-NAdPABg8BflMCl1gLR_FDwfwuk9k33hm0inwotn8pPqW4COD-sG3_e1HPAmSLB_35_gLpfYcjzSgg01Di7Ls14zCPt9YftfPJUqCPzSLwfIwLHqlB3P_Uu5Y3diNk-YJ08g-BZWzrSnbmCderG5LxHwykuQo38dGfzH3GKiMBjTEKsuW8BjQrL0pAenJQiwxy6ikiPreCn2K_1BLS0QI02yft3-C3HoVeTeHxSCGlvRGzapq7PEocJ07M65f3U0klRASlBBvomsYaT3qOw-4SarJrnSfxqNqAlPm4Jfogpi-uoP50qQFNnOKCqSrfOqEWMU03bSjjJQhUvo5o1OZMCUvcVpCh-E6FnmrzmcKYTAk-3qY0coJZoqIsqAdGL0PfSrw4BCn8TOSGIB5wjYNUz3OMOJpbamGkACtYjpJ55IEE0UX7j0wSBl9avLYvJmRFJcIoN8sAw0GLgzV3yRWjM8Z754C7kmHIwGR9f4EDqqFHdM7iydT4KGNgn5itoix2mZ5r-UFXduIop8qCrUcpTL6No-_OEDT31EP9PHgG37SrioJf0U7eLhm9pF4MO8AsSXHE6UlUnPjWOwGn-XRoXS2GvaJJPh2BMCT6JOC0-zsjqtLr1h_ytLb1orRN4v6I-VtitSk1c-EShDgBdzmbdYHG9qhLs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=kublmMQ3t6rQ-NAdPABg8BflMCl1gLR_FDwfwuk9k33hm0inwotn8pPqW4COD-sG3_e1HPAmSLB_35_gLpfYcjzSgg01Di7Ls14zCPt9YftfPJUqCPzSLwfIwLHqlB3P_Uu5Y3diNk-YJ08g-BZWzrSnbmCderG5LxHwykuQo38dGfzH3GKiMBjTEKsuW8BjQrL0pAenJQiwxy6ikiPreCn2K_1BLS0QI02yft3-C3HoVeTeHxSCGlvRGzapq7PEocJ07M65f3U0klRASlBBvomsYaT3qOw-4SarJrnSfxqNqAlPm4Jfogpi-uoP50qQFNnOKCqSrfOqEWMU03bSjjJQhUvo5o1OZMCUvcVpCh-E6FnmrzmcKYTAk-3qY0coJZoqIsqAdGL0PfSrw4BCn8TOSGIB5wjYNUz3OMOJpbamGkACtYjpJ55IEE0UX7j0wSBl9avLYvJmRFJcIoN8sAw0GLgzV3yRWjM8Z754C7kmHIwGR9f4EDqqFHdM7iydT4KGNgn5itoix2mZ5r-UFXduIop8qCrUcpTL6No-_OEDT31EP9PHgG37SrioJf0U7eLhm9pF4MO8AsSXHE6UlUnPjWOwGn-XRoXS2GvaJJPh2BMCT6JOC0-zsjqtLr1h_ytLb1orRN4v6I-VtitSk1c-EShDgBdzmbdYHG9qhLs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=J8oZG76Pin7PReJnklNUnleiLQ1zSbCmXe0c4U0pVsG8o1WLDKu9hw-ESs8x7cEfWZPtLHe3b_f3uuU5vi7Wh2UfB6ep8VC6a20Hi1WAT4sX6iIR8FbPIU7R9zG-8n7Xm2uHETZj48JSeA7UVGm0xOG97SMunblxLp7ADOE1EeFg84UgCJPVAP65ahK-9BLj2CtcMpHp9tko9PocKx1cQTWzzOoMgz8qqZ8OvYLHQq7zHPagO4fj911Nn0AW6ZkVtjOg0P_cw72lgNt9jJiaNSg2nvDfCMfmlxHHVS8jrjNJMIRfZeCBpyZcs13w-lY-px8__hGI2S_CSvPAbo9_1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=J8oZG76Pin7PReJnklNUnleiLQ1zSbCmXe0c4U0pVsG8o1WLDKu9hw-ESs8x7cEfWZPtLHe3b_f3uuU5vi7Wh2UfB6ep8VC6a20Hi1WAT4sX6iIR8FbPIU7R9zG-8n7Xm2uHETZj48JSeA7UVGm0xOG97SMunblxLp7ADOE1EeFg84UgCJPVAP65ahK-9BLj2CtcMpHp9tko9PocKx1cQTWzzOoMgz8qqZ8OvYLHQq7zHPagO4fj911Nn0AW6ZkVtjOg0P_cw72lgNt9jJiaNSg2nvDfCMfmlxHHVS8jrjNJMIRfZeCBpyZcs13w-lY-px8__hGI2S_CSvPAbo9_1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شدت انفجارها رو ببینید
بخشی اش موشک‌ها و سلاح‌هایی است
که درون تونل‌های این تپه بودند.
این دژی که تصور می‌کردند شکست ناپذیره از درون نابود شد.
پول‌ها و سرمایه‌های ملت ایرانه
که دود میشن و به هوا میرن</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6726" target="_blank">📅 09:48 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6725">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=QbqtYONuCHV2XVKsr-WgSqoa1t2WFgQagy-qFywBKMEf0-QDm4OrkAJQuhCk4X4mkgJOXHP_JooLyb1-0c5yp4vlX84sAW-tyLEP9FQ2Oe0_ld3UH7YajysUKeBoGpSO3NEAplSsFO0x8ehRYsfHQ94A_nObIHiRBcwAB01lXqmwbNP20u8Qk5gmF0vOzPWufeRfotZI7Ch7yn8nf_-7M1h48gKK6cin59OKBVqit7QMfafLCracDtn1LxdeTyq3DnQPqU_msXgHy9ej2xT942XM2KOB3tbvhP9dV_bBivRudjhq3zPwKZrYwh0Yanx7os78dPt6mc5ZOSD_C5Yejg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=QbqtYONuCHV2XVKsr-WgSqoa1t2WFgQagy-qFywBKMEf0-QDm4OrkAJQuhCk4X4mkgJOXHP_JooLyb1-0c5yp4vlX84sAW-tyLEP9FQ2Oe0_ld3UH7YajysUKeBoGpSO3NEAplSsFO0x8ehRYsfHQ94A_nObIHiRBcwAB01lXqmwbNP20u8Qk5gmF0vOzPWufeRfotZI7Ch7yn8nf_-7M1h48gKK6cin59OKBVqit7QMfafLCracDtn1LxdeTyq3DnQPqU_msXgHy9ej2xT942XM2KOB3tbvhP9dV_bBivRudjhq3zPwKZrYwh0Yanx7os78dPt6mc5ZOSD_C5Yejg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی به «علی الطاهر» میگفت «مینی پنتاگون» پنتاگون کوچک. با هزینه میلیارد  دلاری، با صرف ۱۸ سال زمان، شبکه‌ای از تونل‌ها در درون این تپه ساخته بود،  مرکز فرماندهی، انبار تسلیحاتی، محلی برای حمله به اسرائیل و…..
اسرائیل دو سه ماه محاصره‌اش کرد و اجازه نداد آب و غذا به اونجا برسه،
سه هفته پیش جمهوری اسلامی
به آمریکا پیام داده بود که اگر دست
به علی طاهر بزنید، جنگ برپا میشه و…..
اسرائیل در یک شب، پس از شناسایی ورودی تونل‌ها، ورودی تونل‌ها رو نابود کرد و تبدیلش کرد به یک «تله» برای سازندگانش.
جمهوری اسلامی تنگه رو هم بست و خودش در داخل تله اش افتاد!</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6725" target="_blank">📅 09:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6724">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=Sxs4bhmlDm0Nm3ObvOql05RPyt2dPMWL4l7O5mtIpI67L-xXMHhLoQvCKyeKkex5qEZXsbLApOmIiPnSlOVJ0Y24cKMUpEw23kxeTN2O-cfM80PP8AGcFxO5buBcI9e_2X28oPk_YbLMtoFn80HlGbNYsMcaTr6xNvg1fZlBLNJXGVoWtmjkp3TTP3Gf2rjBKXQsIzL84vwU9AkDFOl0TJ2-IsVrdtj4wZKvw5Fqf3gv0_gjfS2hwI6kKDeY5CBVxKyjzS5ND29ORFE5lBVr5Gjh2SskYJujTpymrKTsCsJ4Y9BD-0Mj6au0F92l_Eqr9-rGC0eiWB3KmObS-w0fcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=Sxs4bhmlDm0Nm3ObvOql05RPyt2dPMWL4l7O5mtIpI67L-xXMHhLoQvCKyeKkex5qEZXsbLApOmIiPnSlOVJ0Y24cKMUpEw23kxeTN2O-cfM80PP8AGcFxO5buBcI9e_2X28oPk_YbLMtoFn80HlGbNYsMcaTr6xNvg1fZlBLNJXGVoWtmjkp3TTP3Gf2rjBKXQsIzL84vwU9AkDFOl0TJ2-IsVrdtj4wZKvw5Fqf3gv0_gjfS2hwI6kKDeY5CBVxKyjzS5ND29ORFE5lBVr5Gjh2SskYJujTpymrKTsCsJ4Y9BD-0Mj6au0F92l_Eqr9-rGC0eiWB3KmObS-w0fcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ویدیویی از نخستین توزیع قند و شکر کوپنی در دهه ۶۰، عبدالناصر همتی، خبرنگار وقت صداوسیما و در میانه گفتگو با مردم به مصاحبه شونده می‌گوید: «اگر قند و شکر کوپنی کافی نیست، باید کمتر بخوری» مصاحبه شونده هم می‌گوید: «اصلا ترک می‌کنیم، ضرر هم داره ...»
همتی در این کشور خبرنگار ساده بوده و شده وزیر و رییس بانک مرکزی و کاندید ریاست جمهوری‌ ...</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">‏آغاز جلسه شورای امنیت سازمان ملل برای بررسی موضوع ایران</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6723" target="_blank">📅 17:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6722">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=N3AVBtyfGbzQNHfYYTXC4T-iQL-r-T_O7Sz0-afJGVIr-lh-toSJZCBTx_CAWKTksJo6zuCMGkS0SIV0-GpnTYNi5QpVYUJy1755GahbowPhJE_GTDNBPVLYiJXvrcMd9O3hovv2nFG71auQnUBskAsmzDuGJrhOU9mY2xf007nDQCFj3xa1ZPPi0aJhiYAoDODWJLuk4wCvmK-ht9wF_htDYdd2jkL9tm-Uv4A2zeDOML3oA7OupYGFcgknySx3j07XJpRNAjc2PK53qJNZprPEbEHtBsYncCybIrkxuy_esHp9DhgmYaiKBlxzqDfvPu2FxBZMyBpw03obdh-I-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=N3AVBtyfGbzQNHfYYTXC4T-iQL-r-T_O7Sz0-afJGVIr-lh-toSJZCBTx_CAWKTksJo6zuCMGkS0SIV0-GpnTYNi5QpVYUJy1755GahbowPhJE_GTDNBPVLYiJXvrcMd9O3hovv2nFG71auQnUBskAsmzDuGJrhOU9mY2xf007nDQCFj3xa1ZPPi0aJhiYAoDODWJLuk4wCvmK-ht9wF_htDYdd2jkL9tm-Uv4A2zeDOML3oA7OupYGFcgknySx3j07XJpRNAjc2PK53qJNZprPEbEHtBsYncCybIrkxuy_esHp9DhgmYaiKBlxzqDfvPu2FxBZMyBpw03obdh-I-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=ZaCiyJc1vQxm6NPrP6Pmzj2kWu22VsJNKvDkPNgZ5_IdxnAPFbF9kJ52Rbkh1fV2J_CSRKqUlRQWAsG9xU8tJKwMUZkB9CvkLAG3FiTOEViv1yHyrrPYEaHXaS1TXC5NKy4J26J6pnOPi7sob7VG6u79CbL4BqbYt8ryTFsvMadLErRVNMgV13ThqeTsM_ZxxOq8EMU-IS1Z42xKLzK0Ym7_3gD-SBvWFeOsHTV-y1EPtQqpnuzL3cUy2X3pA25dNrTO4YH3ClObF8DCxhH6wDELVNcIB3PywViHBp47KsbGv9K-szoIHnW5_hL8w_5Gar-ZISMLCKEif2JVebIMdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=ZaCiyJc1vQxm6NPrP6Pmzj2kWu22VsJNKvDkPNgZ5_IdxnAPFbF9kJ52Rbkh1fV2J_CSRKqUlRQWAsG9xU8tJKwMUZkB9CvkLAG3FiTOEViv1yHyrrPYEaHXaS1TXC5NKy4J26J6pnOPi7sob7VG6u79CbL4BqbYt8ryTFsvMadLErRVNMgV13ThqeTsM_ZxxOq8EMU-IS1Z42xKLzK0Ym7_3gD-SBvWFeOsHTV-y1EPtQqpnuzL3cUy2X3pA25dNrTO4YH3ClObF8DCxhH6wDELVNcIB3PywViHBp47KsbGv9K-szoIHnW5_hL8w_5Gar-ZISMLCKEif2JVebIMdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صدا و سیما میگه :
مردم ایران در خانه‌هایشان
«۵۰۰ میلیون تن طلا دارند»
یعنی «هر ایرانی» حدود
۵ هزار و ۸۰۰ کیلو طلا داره :)
روایات اسلامی و معجزاتشون رو هم
همین مدلی ساختن!
اون مجری شوت هم میگه : الحمدالله!</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/farahmand_alipour/6721" target="_blank">📅 09:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6720">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=n0fIwj-JMrTzTU93MGo9cd4-k8yoBLK6LI2bM-utck9AeTcyybWPHoTJqrCtqRElhn_pf_k4gTchJj7LiowA7498PkoEoLTKy6uTEkTVfExWCHI4qBegCdMLLk5pHGJN3qUiWWHEsC3O7Ll7Pa7N1EsFviKDSKN-6sMekOO-OI6huHPUR7TPokYL4eiiC5bicM63N6oMRh8H6HSZL-eOUxY9QgGzFnh4_vf-Pqcdu31bQlISJaRMGXYFtePcZaZrcqXvA3kf572kCcSrFwXLzBtLg6Xv-41lel4_ed9gCtIvIzrMFOGX-zOUiY2DWX64zFTzZ-tCAmNff4BY3a45XA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=n0fIwj-JMrTzTU93MGo9cd4-k8yoBLK6LI2bM-utck9AeTcyybWPHoTJqrCtqRElhn_pf_k4gTchJj7LiowA7498PkoEoLTKy6uTEkTVfExWCHI4qBegCdMLLk5pHGJN3qUiWWHEsC3O7Ll7Pa7N1EsFviKDSKN-6sMekOO-OI6huHPUR7TPokYL4eiiC5bicM63N6oMRh8H6HSZL-eOUxY9QgGzFnh4_vf-Pqcdu31bQlISJaRMGXYFtePcZaZrcqXvA3kf572kCcSrFwXLzBtLg6Xv-41lel4_ed9gCtIvIzrMFOGX-zOUiY2DWX64zFTzZ-tCAmNff4BY3a45XA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قابل توجه کسانی که دنبال بهانه‌ای هستن
برای پناه گرفتن در آغوش امن و گرم آخوند و توجیه حفظ قدرت در دست این‌ها.
این مفنگی، پدر زن مجتبی خامنه‌ای،
میگه «فعلا به خاطر شرایط جنگ
با حجاب کاری نداریم»!</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6720" target="_blank">📅 08:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6719">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=p3GGcE3VI5Cvf8-YbxOpIcT7fstMjNFLdYFavx_waTxVwNsdiNaLe-VZ3xcHR-AfIsvv7DmhTcudl8ELZShSAxPIxumAqXe0x70QNOXZ5b06LWP61kHnM4Hy6tTC6_t35dNh_UTlQARWHFkcw0HkJbr9euvuUAGUTOIwwQdcs19ag4f_MShVGTW4bSA7m44TSmwSodq6fOy-Pz3YglbyrpyYDdBhq0UNto7JPdULUjtQewrdoxPSxZ8wV6XHeQb-UETxZP7Tox3vfvcd2JV7uDUyPiQYWxmPQ6OQUHNw6lvFpfaKsisdjMhtJK-slVYxRQCI7-njgjdoCmXfhfEd7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=p3GGcE3VI5Cvf8-YbxOpIcT7fstMjNFLdYFavx_waTxVwNsdiNaLe-VZ3xcHR-AfIsvv7DmhTcudl8ELZShSAxPIxumAqXe0x70QNOXZ5b06LWP61kHnM4Hy6tTC6_t35dNh_UTlQARWHFkcw0HkJbr9euvuUAGUTOIwwQdcs19ag4f_MShVGTW4bSA7m44TSmwSodq6fOy-Pz3YglbyrpyYDdBhq0UNto7JPdULUjtQewrdoxPSxZ8wV6XHeQb-UETxZP7Tox3vfvcd2JV7uDUyPiQYWxmPQ6OQUHNw6lvFpfaKsisdjMhtJK-slVYxRQCI7-njgjdoCmXfhfEd7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان حکومت دیشب این شکلی موافقت خودشون رو با قطعی برق و افزایش قیمت بنزین،
دلار، طلا و گوشت نشون دادن:
تو تاریکی می‌نشینیم، دلاری گوشت میگیریم،مهریه کم میگیریم!
موجودیتتون ذلته!
دیگه ذلت چیه!</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/farahmand_alipour/6719" target="_blank">📅 14:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6718">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">دلار ۲۳۲ تومن!
💸</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6718" target="_blank">📅 13:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6717">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hJtSYYXBURU1tkhNWFruisNz9qeyKrtZjTBe4cb44mzeOyQXolQWJTe4As5tCKnVQyeCOiaj76kMd2sUUGM5wIyETzN5ApjPHOzbRr-UwvQ3lBXMYmFWP7RUUVDGi_w4bNwfBH6PMHgmfTWzHMTedJjWCSSEDF62-hYiJWn6MRuAUGToT7GHxpj_JIsowhaOoHBEzvZ1NbjBiauc-59Tr4rbWkeoEU6ShkcQOaFh7yiQqzhv5X4n68FP8D4uEYWalsDq6XXEz9t8JCqPfTFkVEHJRvLrug-ECs5KdZWa053l-sdFadLyitBm4vmkiRkvqUSuRQedysvDcLjR2BTMTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکر نعمت کنید،
بلکه این نعمت‌ها افزوده بشه،
اصلا گیریم یمن نیفته دست عربستان!
بگو اصلا بیفته دست کفتارهای
بیابان‌های سومالی !
همینکه این‌ قوم ظالم در ایران شکست بخورن  و به غصه‌هاشون افزوده بشه، جای شکر داره!</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6717" target="_blank">📅 13:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6716">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=F8-Qvv7yb04JGghwMyAVNbRrszCeya7JgmO1SOwFBwbDPdj1EcD3U-RqVCoasAeIY8svk9rlfAIZ0FLI8yTtJLL48HoWQNIo3OJ_kNGy9o5IHjdtnW5Dks2J6U8iF9V5ZbbqsNcNVTm3UCLZ_VTjCZ_2dRVb2oLooGkzakefl2-dSD6TwcG8BZyyj4s5GCUaWVm0x7APYeubT2Bf1tMGDtBuOI_cErtyV-fomtipurrf_uihxk8WiiW25Xt6t9HstsLC6QjQg0tl7B9IxbtazKZ4XqaT7ZZingZH2rhfRFirvT90wGEyK5uAuv0mZmHKdxV0fIdsuW-udj7MK_spHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=F8-Qvv7yb04JGghwMyAVNbRrszCeya7JgmO1SOwFBwbDPdj1EcD3U-RqVCoasAeIY8svk9rlfAIZ0FLI8yTtJLL48HoWQNIo3OJ_kNGy9o5IHjdtnW5Dks2J6U8iF9V5ZbbqsNcNVTm3UCLZ_VTjCZ_2dRVb2oLooGkzakefl2-dSD6TwcG8BZyyj4s5GCUaWVm0x7APYeubT2Bf1tMGDtBuOI_cErtyV-fomtipurrf_uihxk8WiiW25Xt6t9HstsLC6QjQg0tl7B9IxbtazKZ4XqaT7ZZingZH2rhfRFirvT90wGEyK5uAuv0mZmHKdxV0fIdsuW-udj7MK_spHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=K_lesfryabr7HRWRDrNZM7fNuNrOm7aZeYgY3NUu1Vvim63_x0w0aQ77QO3a1ifO6IOL6Gb_MRm9sOZARyogiV9g1FQ8Hv2raaob-vUyUuJEzZd2nW8qojfp_MdbOgLO8fe8Z0U9KoUDD6wCHOWsrX3dYt8ITiaPl3Gy__CMb8pHVEuJsgJ-Mcpy03KmXxR1M8a_F5P43ydS_hq_LIzEaymY4PVeJXUGXtd0fp92WVHNAS_t-Yifq2IG-E5nqvcWg012OXj7v7Sg8SmAqRTiPd-DxhLtCFL7FStt-uMt77Fhz_WrDAOdVNyGanBGfr-4o22WFlIhmQHcmg53CUl_SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=K_lesfryabr7HRWRDrNZM7fNuNrOm7aZeYgY3NUu1Vvim63_x0w0aQ77QO3a1ifO6IOL6Gb_MRm9sOZARyogiV9g1FQ8Hv2raaob-vUyUuJEzZd2nW8qojfp_MdbOgLO8fe8Z0U9KoUDD6wCHOWsrX3dYt8ITiaPl3Gy__CMb8pHVEuJsgJ-Mcpy03KmXxR1M8a_F5P43ydS_hq_LIzEaymY4PVeJXUGXtd0fp92WVHNAS_t-Yifq2IG-E5nqvcWg012OXj7v7Sg8SmAqRTiPd-DxhLtCFL7FStt-uMt77Fhz_WrDAOdVNyGanBGfr-4o22WFlIhmQHcmg53CUl_SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم
همون ۱۶-۱۷ فروردین، کارشناس
صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه
رو رها نکنیم تا قیمت نفت بره بالا!
و فشار رو بر آمریکا اعمال کنیم!
چون خواست مجتبی خامنه‌ای اینه!
نتایجش رو هم همین روزها داریم می‌بینیم!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6715" target="_blank">📅 11:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6714">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=dby_9O1DUE7XSmngA3YOh3UcT0JXKE60LY8Gdv9NeNkmdkd65YhAb2zEKqPcokiK2i8PWbOIUt8emdoyT4pietsNOw6kv-xk5XnD69AZIcoQWsP5QM3QRUzH61X6q1kbaGV-2-ntF4OskKaM3WLxsvbQ1iBA8zK8ejGaHMTvC7JLgQ2vBV9g-QJWyscCnUXCQmpjxZPVe9jI9xgJgRgL9Igwto6IxdKj_-S1K3LgwnVmhRtMYi6XxIEvQGGMM3QuWONNKJIaxSFAWfpYT-4DsGwFL99V38sCFK1TEJPjmtKp9J2GN5c-8qS_tFmMYXvs0GnUGUdfJNfuWw5iWsT_yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=dby_9O1DUE7XSmngA3YOh3UcT0JXKE60LY8Gdv9NeNkmdkd65YhAb2zEKqPcokiK2i8PWbOIUt8emdoyT4pietsNOw6kv-xk5XnD69AZIcoQWsP5QM3QRUzH61X6q1kbaGV-2-ntF4OskKaM3WLxsvbQ1iBA8zK8ejGaHMTvC7JLgQ2vBV9g-QJWyscCnUXCQmpjxZPVe9jI9xgJgRgL9Igwto6IxdKj_-S1K3LgwnVmhRtMYi6XxIEvQGGMM3QuWONNKJIaxSFAWfpYT-4DsGwFL99V38sCFK1TEJPjmtKp9J2GN5c-8qS_tFmMYXvs0GnUGUdfJNfuWw5iWsT_yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون هم که با افتخار این  تصاویر رو منتشر میکردن!  بگذریم کل سپاه و ارتش و بسیج و مردم و عشایرشون نتونستن وسط خاک ایران،  این خلبان رو پیدا کنن!  فقط هی نوشابه پشت نوشابه باز میکردن و تعریف و تمجید از خودشون! زارت!</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6714" target="_blank">📅 11:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6713">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">هالیوود از این داستان فیلم خواهد ساخت خلبانی که وسط جنگ ۴۰ ساعت در عمق خاک ایران بود.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6713" target="_blank">📅 11:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6712">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">آزیتا در کالیفرنیا داشت محله نیاوران و فرمانیه  رو به دوست آمریکاییش نشون میداد،  که ایران چقدر پیشرفته است،  یهو به خاطر اینکه خلبان در یک منطقه نه چندان نامناسب اجکت کرد، سی‌ان‌‌ان و فاکس‌نیوز پر شد از این تصاویر از ایران!  تازه هالیوود فیلم سینمایی «نجات…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6712" target="_blank">📅 11:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6711">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=ER7PWRTEyC7hn2l2FbyqFCn_5Ui8cM75jao1Uh2ECv8IlhCEJz6ZV-09X_8nI3AXwgT4Yicwe631mcNmU9g6H3zN46oaOc5kAH2Hk6w5xwkkeo_h2jmgjjvYFxTZ7V1lq5iiEpKotQsY1J3v8GzdwepY0OitzT44R6DC7kpJxUvpj0o7WA022WJyQnlbAyL5LWZVnckWXzmSwLjubcnNBgPYvX_73-Vo2zBQA_40HcXDuSJwikzuT9YY0AGo_h4VHSaf5MFIJQ_XWP6MDbtrUHNsFvsmFO8jQ9CR4hiOWI3iR0-iehf56V2J-TIUiT6KyBjS8YXC5TThGqz6AlGDCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=ER7PWRTEyC7hn2l2FbyqFCn_5Ui8cM75jao1Uh2ECv8IlhCEJz6ZV-09X_8nI3AXwgT4Yicwe631mcNmU9g6H3zN46oaOc5kAH2Hk6w5xwkkeo_h2jmgjjvYFxTZ7V1lq5iiEpKotQsY1J3v8GzdwepY0OitzT44R6DC7kpJxUvpj0o7WA022WJyQnlbAyL5LWZVnckWXzmSwLjubcnNBgPYvX_73-Vo2zBQA_40HcXDuSJwikzuT9YY0AGo_h4VHSaf5MFIJQ_XWP6MDbtrUHNsFvsmFO8jQ9CR4hiOWI3iR0-iehf56V2J-TIUiT6KyBjS8YXC5TThGqz6AlGDCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JaGEFkr3W8Q6QOHzSCd94_BvQ8Hh6VjBX2_VzantoJ_F9cVpIFv3jsLrErIPzS-NzjxRLSsioWc6MKCqJUKzlP05tCT2tQN5paLuXeL1HVjNQzgjdmlCW-8ssQ-mCX6FihzycN_HAuEd9KO6Z84K7mimoqjheik58DNf4XkDa0h3_QDZh8I8WKZxyEwGJ5y5sxlT9Q2W2DPaj-5T3kwq78Pj-OVO0Js3JWIXq8II7NFu-rdt6GoIgF-YDpP6n8BMQj4K7ve4oJfLHls1HoiWD0e_VjflJAbhlk4q4ILgielG6HGq5pll0jUkFqy6bQLEtuixCY5cxq_cTmVy2-yJcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
شب گذشته و در جریان حملات آمریکا ۵ نفتکش ایرانی منهدم شدند.
سنتکام اعلام کرده که حمله به این نفتکش‌ها در پاسخ به حملات موشکی جمهوری اسلامی به  یک ناو نیروی دریایی آمریکا صورت گرفت، گرچه ناو آمریکایی آسیبی ندیده بود و موشک‌های شلیک شده ج‌ا دفع شده بودند.
سنتکام ویدئوی انهدام این نفتکش‌ها به نام‌های « ام‌تی کاویز، ام‌تی چارمینار، ام‌تی هورایزن ۱ ، ام‌تی ریسکو و ام‌تی دریا» را منتشر کرد.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6709" target="_blank">📅 08:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6708">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
ج‌ا با ۱۳ موشک به اردن حمله کرد</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6708" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6707">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
طبق گزارشات، سپاه از اصفهان، یزد، تبریر، لرستان و... بیش از ۳۰ موشک شلیک کرد و حملات سنگینی رو آغاز کرده!</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6707" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6706">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
حملات موشکی جمهوری اسلامی از مناطق مرکزی ایران</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6706" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6705">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها، ارتش آمریکا امشب دو نفتکش ایرانی را  در نزدیکی جزیره خارک غرق کرد و به یک نفتکش دیگر در نزدیکی جاسک حمله کرد.</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6705" target="_blank">📅 23:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=caqphyLdO05fnYfgAMDypRO09oagUvUemfmCeKAsI2okMu-h9gRA6GIxXxkYU2UsLUu85jnL7KK0B5z1VhqRtBBWb_0kD_23zGTHAO9bMZMA5co-04UxWjmhk26e__rl-_rt2ARx2GujRtvMYumTbMso5piXhpY9bcwBqo2A7kic5MRDJBaSUFWnxuLwTboHY6fb5ObIWzLDVrOKQjfN3lv3GRf9ODFY3LKKdXXLwUSAcKP233-VjeQbZNoSfrGQsjqoY9gUPo4G3Gws10QxStPNEzVTVwq0zirj8yFcB46Xx69ml8LNs58AFK8xfuzq2KsKtx7DhYqkbHfMvodn4jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=caqphyLdO05fnYfgAMDypRO09oagUvUemfmCeKAsI2okMu-h9gRA6GIxXxkYU2UsLUu85jnL7KK0B5z1VhqRtBBWb_0kD_23zGTHAO9bMZMA5co-04UxWjmhk26e__rl-_rt2ARx2GujRtvMYumTbMso5piXhpY9bcwBqo2A7kic5MRDJBaSUFWnxuLwTboHY6fb5ObIWzLDVrOKQjfN3lv3GRf9ODFY3LKKdXXLwUSAcKP233-VjeQbZNoSfrGQsjqoY9gUPo4G3Gws10QxStPNEzVTVwq0zirj8yFcB46Xx69ml8LNs58AFK8xfuzq2KsKtx7DhYqkbHfMvodn4jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی موز خوران میگه
که از خامنه‌ای «وصیت نامه» نمونده
و دنبالش نباشید!
(خیلی‌ها حدس میزنن که در وصیتامه‌اش اومده
که از پسرانش کسی جانشینش نشه، برای
همین منتشر نمیکنن)
صدای کار و چنگال و بشقاب و
صحبت از وصیت نامه رهبرشون :)</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/farahmand_alipour/6704" target="_blank">📅 18:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6703">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">بنزین ۱۰ هزار تومان!</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6703" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6702">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=mpdRH1Du5r7d-Bmy45KjqXZ49cKrhhKLL0qN-C3WQqYy2xZco7DKl3yXvRESbJouBpxFf_pa3gxb1ecWEIqqaVs1bC0LtB-LVsDT7knIC6yRclxMg0PyFs7SdO_mpmRB5MxS2RzsxEEmsrvSNtGG7WZqPa2pqwPPnYw-fqlpxJb4npVmxiSXT5HKy9XUb9stO1wpbbkBGyuqhJ0rcNIVdyiNjA_hxxFqcgnxjqciBGjzZh_3fE7Evh-fNoIkcQCIy8hVvVuBes20WnjZ9KXvgBAcPZ_GRgWLwu6xhKcE6acJOvToINXZ5nKj-sDT-CEg6zvdnlDue3GeCE8D_UfyEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=mpdRH1Du5r7d-Bmy45KjqXZ49cKrhhKLL0qN-C3WQqYy2xZco7DKl3yXvRESbJouBpxFf_pa3gxb1ecWEIqqaVs1bC0LtB-LVsDT7knIC6yRclxMg0PyFs7SdO_mpmRB5MxS2RzsxEEmsrvSNtGG7WZqPa2pqwPPnYw-fqlpxJb4npVmxiSXT5HKy9XUb9stO1wpbbkBGyuqhJ0rcNIVdyiNjA_hxxFqcgnxjqciBGjzZh_3fE7Evh-fNoIkcQCIy8hVvVuBes20WnjZ9KXvgBAcPZ_GRgWLwu6xhKcE6acJOvToINXZ5nKj-sDT-CEg6zvdnlDue3GeCE8D_UfyEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صحبت های سردار محمودی :
ترامپ باید موشک رستاخیر و موشک آتش افروز ایرانو بیینه،ی موشکی داریم سوخت جامد وقتی وارد جو هر شهری میشه خودش جنگ الکترونیک راه میندازه، کلا تمام وسایل الکترونیکی و برق ی شهرو قطع میکنه، وقتی به هدف میرسه قبل از اصابت تمام اکسیژن هدفو میخوره و وقتی سر جنگی این موشک به زمین خورد، ۸۰ کیلومتر مربع رو کلا نابود میکنه، اینارو هنوز رو نکردیم.
﻿
+++ قدرتمند ترین بمب اتم جهان یعنی بمب هیدروژنی تزار متعلق به شوری ۱۵ کیلومترو کاملا نابود کرد.</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6701">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرده است که موشک‌های بالستیک ایران، ناو هواپیمابر «یواس‌اس جورج واشنگتن» و یک ناو جنگی دیگر آمریکا را هدف قرار داده‌اند و این دو شناور برای گریز از حمله ناچار به انجام مانور شده‌اند. در این حمله هیچ‌یک از نیروهای آمریکایی آسیب ندیده‌اند.</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/farahmand_alipour/6701" target="_blank">📅 00:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6699">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iF0FyBErdoJkfrTvpL92yJjvtvFUiS5D8SjLNWmvoKs4fnqg50Dw1BVODpC3DyRe7ej4MeC-30dPBNF_8PaG-I1-iPwSxbeD_5eVEvYo13Zd1PG5FMiDEno8h9WMF4jaUVyy3gK0-ijz1bXsr5-w0f5aVkm6f49DkJU2HuLPm8faDVxbE0G5xUygfzPoVQpzneR718NVzt0Zrwyv54DBTnl0mrpgfbboVnPNnGLDZMnAKSGG9lo2EGrvBneHNdwrCj3plCI32ZRU2OCE9XNL9RcoqPfxGL2IWkaYBcX1aGm-c0LZqmEWYXflaBm9Cr9nnnY73e5VYaPPtAtUH-kdYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mikAE8sdFxoR0SR9Dyw3LHx4O_jOQ6gLFgEATKbG13eFRXisFvahp9_6jDy9S2SYghJxprHFirdZ9P4R-oCwnMwhbaPYHWYuRz1p1V911edw1jCd4BDSPlvtxyRx-_HCmwqq1Vzvn6ROC27AoSOyrmLwlV2XbEvHfrZNh4b5PgA-kTrYn9PB3ONRE4gJYHgz1eTdnKVezf32Fpaw7qLuSzFZ99gi-ZvawDR0v8zO_Jp8pHZbswyemQmCtf2m-KH7inQ8AN3G9VQ6z6gNwbAvfMDEJZGaR6fKf4OMBLucftLiC-abR8xSo8mqrJezCXLmlPmm0pFMewDtbXHy9mcfmQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برده‌ها در مزارع پنبه اربابان سفید پوست
در ایالت‌های جنوبی آمریکا،
سالانه در بدترین حالت ۴۳ کیلوگرم گوشت میخوردند. در حالت معمولی حدود ۷۰ کیلو گوشت در سال.
ولی در برخی ایالت‌ها وضعشون بهتر بود و برده‌ها تا ۹۰ کیلو گوشت در سال مصرف می‌کردند.
وضعیت برده‌ها در آمریکا، بهتر از وضعیت زندگی در کشور امام زمانه.</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/farahmand_alipour/6699" target="_blank">📅 21:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6698">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=Cx7wEI3-fdwdVJouIng2nA4GcK19IBAIuh4ZmV9MJQqxUoZnncr66RWqPUhkOXj__8hcb0TERPRnD0juzdwFmLq8Q4FxHBI8poi69LgrmM9kQv8pp77l8oeVIo9gFz1BacyQPMBzDTgUOd3vdbUN1wl9YQPXwYOKctqJLTaFGenn6OrNw00M8nkQpG_gr3LUvB6khYczmqPuiHePMAudJKzHt3p0kmdTzyv7dy1twEWvRyaVv9O3jM2OlxSmNxzLdMH3bJNnaKCsNnKVgmyEfAqcASXCViGpAuK95DIdONyq0PkAEHbszBFdj9vUS2a9UVnD9ucyqXJRyfcNtAJpFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=Cx7wEI3-fdwdVJouIng2nA4GcK19IBAIuh4ZmV9MJQqxUoZnncr66RWqPUhkOXj__8hcb0TERPRnD0juzdwFmLq8Q4FxHBI8poi69LgrmM9kQv8pp77l8oeVIo9gFz1BacyQPMBzDTgUOd3vdbUN1wl9YQPXwYOKctqJLTaFGenn6OrNw00M8nkQpG_gr3LUvB6khYczmqPuiHePMAudJKzHt3p0kmdTzyv7dy1twEWvRyaVv9O3jM2OlxSmNxzLdMH3bJNnaKCsNnKVgmyEfAqcASXCViGpAuK95DIdONyq0PkAEHbszBFdj9vUS2a9UVnD9ucyqXJRyfcNtAJpFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tqiT2N98teJuy8I-0cKlpme6aKbBQF2CmA8qd8qROkpydaSoyCIU8EqwgfTXI4X54l4nlJXogfMqZsmM8gEfWcCPHldqArhuNmn_WvZfQxqq8Anc_MvKVLkhLJHWqNES53Lr9beMyXS_U3JObJrjIrXdFSi0CfjzYD4bMrCHsyjpGsMm_Ng0sLrfUq3vrsbNjAhF_S65a2YkE04MZjzWTAj2-mxdDFXAHcBB3V1kq1GUT7Sypt3aNjZkrpJIK8l1a3LM3_fBUp8sAmxEc-pAXm9xI5g57Uw_83AhURhVl6V0OhW9punv-BMluomCSqdzvYjpxKe7QxU2t2tMiMzG2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bjPrYlq3fMkUYjYFOvZxTioIFV48a9xSFaDJkaa7h0BXI29TzV_tPYz3S4BM4QjktxQ1mskq2RrFXufBMrRwpx_m6Nq0-T8HH06jTny9j0lmfBtkGrFjHrQvpqr8_nPURna3DiY2_38Ko9qSTfOLiOHArh_Mo4E2F6EasLoCgQZ9obyyjidUfXQPvlslBxjCfXa_2CLK87CdUxEWPan7ppea7ekPS3Eoxh7NLLTqBSE-AnQb_fIdkRsDk6JxWegVvW5oBUX9ph0631hOTg8FRLAR7EbZi8EG2JwlLtuufcG6OWT4qFXKcVtwZyGzgkV24gQR266_7ttqiUjEEV5xTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ih3-STuUxXTJBs6acFyAm_obdCQbo7jAnstDBLtIf1pX6t0UO0-DiAHBcikTuIklFmFUyG2Tde6Wg7OpdwccluIQH-QsKCZBxhT7z___QtE749RPZxOmtB3iSuG8AQW0ZMfd6ah_yyqJ7-tN64Oz0_39OiNl7dSNh_XgnjtoRwDZsxuaBnZ1Mr7RhgAyv4nMc-XeNrv6AndQx9Hqd8a3D6_2zbh_v1glxZP1OBTAnN93d8kQy727e6HO6Ff1g46zkWCZKhTwpAq_ZTHLx03E6huDpWeHs2NRDf5TPhgCZSuCtcbqgyJ0bw476hR0GTaFAo1zirAfBnuTstNnxp8mPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها به تکرار نوشتم،
تنگه هرمز، تنگه احد اینها میشه،
به وسوسه غنیمت گرفتن و پول‌ درآورن از تنگه و اعمال فشار بر بازار نفت،
دست به کاری زدن که جز زیان و خسران برای خودشان هیچ نداشت.</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6694" target="_blank">📅 23:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6693">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">‏یک مقام سپاه پاسداران به نیویورک‌تایمز گفته از ماه ژوئن تاکنون، بین ۷۰ تا ۱۰۰ عضو حزب‌الله، از جمله مشاوران ایرانی نیروی قدس سپاه پاسداران، در تونل‌های اطراف ارتفاعات علی‌الطاهر گیر افتاده اند و مقاومت میکنند.
‏این مقام گفت حزب‌الله بارها تلاش کرده است با استفاده از پهپاد، غذا و آب برای نیروهای گرفتار ارسال کند، اما نیروهای اسرائیلی، رزمندگانی را که برای جمع‌آوری این تجهیزات از تونل‌ها خارج می‌شدند، مجروح و تا سر حد مرگ زخمی کرده اند.
‏او اضافه کرد ایران و حزب‌الله، تخلیه تسلیحات و نجات این افراد را در اولویت قرار داده بودند، اما اکنون به نظر می‌رسد احتمال موفقیت در این کار روزبه‌روز کمتر می‌شود.</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/6693" target="_blank">📅 23:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6692">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=lg2IAZyctD9wGg_h0CN2p_wBLa1jv_R1xWo-GhRZ0XYEoIOtyArJhAbI6yq1Mrp_SuloR8CqecBx2YDtCuAM-e_QtKrN2rlO6W5AdWAB8SjFZR1dtbdj0srGdhhhdr8aIXvKoqfGHoekpjxTh6oSfLREgNw96GTwrzby93Tg7x8eXWvEqZeIQBfMEr7IDqsraTFpcxv-u5MmU7mP62e66Lduu-jWji3BVdGvWnX3RaR_8WUljb4k2jJjbqZse0ckQaL8ILmP53gVLfJo3t2DqsPutu5-AIvMjxGo-_UiflCmr3hITVTWLwX_A7V_3woJ31lTf7EYdBnrIUVTUuDm0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=lg2IAZyctD9wGg_h0CN2p_wBLa1jv_R1xWo-GhRZ0XYEoIOtyArJhAbI6yq1Mrp_SuloR8CqecBx2YDtCuAM-e_QtKrN2rlO6W5AdWAB8SjFZR1dtbdj0srGdhhhdr8aIXvKoqfGHoekpjxTh6oSfLREgNw96GTwrzby93Tg7x8eXWvEqZeIQBfMEr7IDqsraTFpcxv-u5MmU7mP62e66Lduu-jWji3BVdGvWnX3RaR_8WUljb4k2jJjbqZse0ckQaL8ILmP53gVLfJo3t2DqsPutu5-AIvMjxGo-_UiflCmr3hITVTWLwX_A7V_3woJ31lTf7EYdBnrIUVTUuDm0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون ناو آبراهام لینکلن بود که ۶ ماه پیش
با ۴ تا موشک بالستیک غرق کردن؟
خبر موثقش رو هم  صدا و سیما پخش کرده بود،
خلاصه دیروز رفت پاتایا  !
و یثبت اقدامکم فی تایلند!</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/6692" target="_blank">📅 23:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6691">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=QeiVuYCEHasmXeOll1eyJ65byoNrDzmOFP3MK3OKdSj9I-UCV7w0SZjy2WZpV1Nm8hM8FXxVBmR-BZP1Mg43aI5XmqPDK9RCRaSXeOl1RGUFisX8UZ2Ls_sORzwpy53SXVVTctqTdwPjQ46J5b3XaDqEsw7xjPwXmN8GB_kln3VxYhPQDl_N5gazXZbZgQ-Ta96ludr8FFFUxo88Q-rk8fLhQi9n_q-BExzaWi4CBIp_GUQfSPO7dN0FxkkJJCInZvVPvzWpDLPiaQmjvUp1sG0kkPsdMV7UrFwxE8GyifxzF0G5XcZ6aAUlmS6OxNF2SN2O9LXh8GJMdYSFQha_2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=QeiVuYCEHasmXeOll1eyJ65byoNrDzmOFP3MK3OKdSj9I-UCV7w0SZjy2WZpV1Nm8hM8FXxVBmR-BZP1Mg43aI5XmqPDK9RCRaSXeOl1RGUFisX8UZ2Ls_sORzwpy53SXVVTctqTdwPjQ46J5b3XaDqEsw7xjPwXmN8GB_kln3VxYhPQDl_N5gazXZbZgQ-Ta96ludr8FFFUxo88Q-rk8fLhQi9n_q-BExzaWi4CBIp_GUQfSPO7dN0FxkkJJCInZvVPvzWpDLPiaQmjvUp1sG0kkPsdMV7UrFwxE8GyifxzF0G5XcZ6aAUlmS6OxNF2SN2O9LXh8GJMdYSFQha_2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادتونه قالیباف برای لبنان
از اینها
⏳
میگذاشت؟</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6691" target="_blank">📅 21:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6690">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=J0z2iYqwStXisCbn9Wz35n1HAQ3zCSZGbRj4z-X_M-91qWivPsVeg2X6ThXOb9Ryk1NO98BS5s-SHPVATj3M5c86ZqDXLCchZALcJeZ8Verq0vcC70BLpx1MJtRqxyRgStBHaIh1jbJs_Ob7m-gb6gJfuMs1vT8VAcYE0BuzzbTjOmLvBCASr1MqpwWRrtYlQMuniGgeWK_-AW1EGOaBlybpY4TCfUjzubrpSqn4g2nZ1WNpAcHhfDcuhls9S_kbI8JQ1C9ENnRijEef7JTdpE2OhNECC7vaBcLIjT4L2m2Yrjlxwo58CNy3n0WQdeaLs9bDY2UmWB_2Ogu8cO1paLlflHsHCaupB8WTNyohCF4yfKFAsDUcTuxkP1X629BRaSYtyFFRaQpg5lnwlDB9EGdnwLAPKgdORGjx1C0tD8ce4X1NaeX45X5cExA1gk-ErtfZ5qYAGGIfQLSAFXJZgvZ1bQCUibRtMR4T-o8gZb4DnpGb5NLGZqbY0ObHNNngaUxHbKLmbwYLv61eLmkK4OAs1d6-1aREYgszyDukwo6RVFjEmCD3vLRl2g-JMZKgY_p27PVRvn5No_nF3VyE6actQuR_bQa5A0kdMNaB9VL1duGktdJR2pIkOtGku8Pzs8QB9yNkYwaBfG-hE3TEaTSLdSkcQSD1HfdJeo2wDqo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=J0z2iYqwStXisCbn9Wz35n1HAQ3zCSZGbRj4z-X_M-91qWivPsVeg2X6ThXOb9Ryk1NO98BS5s-SHPVATj3M5c86ZqDXLCchZALcJeZ8Verq0vcC70BLpx1MJtRqxyRgStBHaIh1jbJs_Ob7m-gb6gJfuMs1vT8VAcYE0BuzzbTjOmLvBCASr1MqpwWRrtYlQMuniGgeWK_-AW1EGOaBlybpY4TCfUjzubrpSqn4g2nZ1WNpAcHhfDcuhls9S_kbI8JQ1C9ENnRijEef7JTdpE2OhNECC7vaBcLIjT4L2m2Yrjlxwo58CNy3n0WQdeaLs9bDY2UmWB_2Ogu8cO1paLlflHsHCaupB8WTNyohCF4yfKFAsDUcTuxkP1X629BRaSYtyFFRaQpg5lnwlDB9EGdnwLAPKgdORGjx1C0tD8ce4X1NaeX45X5cExA1gk-ErtfZ5qYAGGIfQLSAFXJZgvZ1bQCUibRtMR4T-o8gZb4DnpGb5NLGZqbY0ObHNNngaUxHbKLmbwYLv61eLmkK4OAs1d6-1aREYgszyDukwo6RVFjEmCD3vLRl2g-JMZKgY_p27PVRvn5No_nF3VyE6actQuR_bQa5A0kdMNaB9VL1duGktdJR2pIkOtGku8Pzs8QB9yNkYwaBfG-hE3TEaTSLdSkcQSD1HfdJeo2wDqo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهم‌ترین مرکز فرماندهی در جنوب لبنان
و مهترین سایت موشکی در جنوب لبنان
که از دست دادنش یک فاجعه است.»</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6690" target="_blank">📅 21:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6689">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=HllZ8W2OI2BhkyosCpiJZRLg7iPN2KMgoYUCaJBu1CZDdW7zveQeL_e1KUk8WpjvJPn4j8pVoF4HRjZO5OHHe8lqA8iHERjEYYsv_Mx4O0IehexJXSOXm5XlZeQapPzuWRaz9OEnT8Ks46m5GXXB76bsIn2ldznKTX1gH_9FunYAcErzRr3oCzyBbF-Ni6IBdggvzLtPVEz7x1njDOJk_JMT6KqTa9U7s0N-29-8nVEF0Lg6CVSF82YPTrckb5VuXLRDrl400LH4mE-CFZagCAIBKk7fSRUR9egGw8SxAviLqQeaZ73iIp0ZjCbFyxuO_UFzjYn9e6jHWQldDE3TtbH6vCWbuA3Bk1wnCsL-1a5qN4p44LgwdDaTGHx5hltHk0KMpSV9aF_WtwIhHAFPDDxQuBssyFjxMaDmfjI4zdx5KItceOumqSf4ZQfIj0j3zgkSlfxvKLkgMYWwRS4fq5ymq1panw5Dz7mae-X4lJC537aZEXaySEdDEz5UC-NeaJorKsueh6XZUhJYz4hTAfEIL4wxSJ3xRN1Lv14RaAtPPHo2Fr9dGhbZe-egnJIVrMtlJzq04TbbiPzDSLhSGRbwZoai7x1uNUW9Jv1H47gmPblePbf7o-1JkknfVKlGlG4xHHVFs5hrHjnhhFSbDU8rkraDKyBYcnwOB5gCZnc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=HllZ8W2OI2BhkyosCpiJZRLg7iPN2KMgoYUCaJBu1CZDdW7zveQeL_e1KUk8WpjvJPn4j8pVoF4HRjZO5OHHe8lqA8iHERjEYYsv_Mx4O0IehexJXSOXm5XlZeQapPzuWRaz9OEnT8Ks46m5GXXB76bsIn2ldznKTX1gH_9FunYAcErzRr3oCzyBbF-Ni6IBdggvzLtPVEz7x1njDOJk_JMT6KqTa9U7s0N-29-8nVEF0Lg6CVSF82YPTrckb5VuXLRDrl400LH4mE-CFZagCAIBKk7fSRUR9egGw8SxAviLqQeaZ73iIp0ZjCbFyxuO_UFzjYn9e6jHWQldDE3TtbH6vCWbuA3Bk1wnCsL-1a5qN4p44LgwdDaTGHx5hltHk0KMpSV9aF_WtwIhHAFPDDxQuBssyFjxMaDmfjI4zdx5KItceOumqSf4ZQfIj0j3zgkSlfxvKLkgMYWwRS4fq5ymq1panw5Dz7mae-X4lJC537aZEXaySEdDEz5UC-NeaJorKsueh6XZUhJYz4hTAfEIL4wxSJ3xRN1Lv14RaAtPPHo2Fr9dGhbZe-egnJIVrMtlJzq04TbbiPzDSLhSGRbwZoai7x1uNUW9Jv1H47gmPblePbf7o-1JkknfVKlGlG4xHHVFs5hrHjnhhFSbDU8rkraDKyBYcnwOB5gCZnc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=lG3r9Qk642CHvdvokTEB5sIEMymF8s1Goy1kUK_FedP5vXJqAWPNQbZB6BfCJzBJ9tkVGIsSR4WanMPjfuC5INP8A1oo0hEmFSb5TuTGsRi0iykbc_GmqJf2DZUl2idhuDMNu8jpNow49AOBK_g9TsyKoHui1MUCJyaN0kgCpAX4PMcWT0iUIbJhJbSKYcVIk1H-Eygu5LBoBPHW7YZUs2Ywh-p0O8zyz_Aa9Na5TIxtMDoPpn8HkWdlbOXgjdkrI_6oyx5Rq-FXzSR-GF2U48oviFzUCB5PqT0v4j9u7_jGlywtGSmyg5q-9A7l2Cb40M5F6N3WNCvi1dEbK2KZeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=lG3r9Qk642CHvdvokTEB5sIEMymF8s1Goy1kUK_FedP5vXJqAWPNQbZB6BfCJzBJ9tkVGIsSR4WanMPjfuC5INP8A1oo0hEmFSb5TuTGsRi0iykbc_GmqJf2DZUl2idhuDMNu8jpNow49AOBK_g9TsyKoHui1MUCJyaN0kgCpAX4PMcWT0iUIbJhJbSKYcVIk1H-Eygu5LBoBPHW7YZUs2Ywh-p0O8zyz_Aa9Na5TIxtMDoPpn8HkWdlbOXgjdkrI_6oyx5Rq-FXzSR-GF2U48oviFzUCB5PqT0v4j9u7_jGlywtGSmyg5q-9A7l2Cb40M5F6N3WNCvi1dEbK2KZeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WBELjjZVzXVgqsuAhhKvKxr2oqaPJz1E2B4QkkPAQnkXYu16azWfb6crxgBRYfJcEzjuIYnakdVFXYC6xtAkOixMuiVKPO8FeCszppkBKcS9pr4GsrjMfBPSTx_uj5lvDrymnZEWnPNWbE7W1JEB25bx6nFrBzaJc70jytWbIJ-Qb7EvSmpGdQ8FZ08H9Do0AsXDC0ekEnFzfkqlYuHq89pkPaXDuq8CEkQ2M38QBmKrY8zaSc795KXhVW6x3yA2kliBRdvh5aoEI6IkiL7gSuRNOfR56W-9lYeYW0LoBa70O6IQ7V5pw7KMJfNjMqhgbbGecNAUfYEl53B5XuoHaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=eB_7g5PZsBdZBV-qB01yWVzkJ1eGFZ5IYohaEMuzRuWEoaMWUfo-gAsvSTBhZlBVZSTFlAIes1NaR1xkF6UD_JJ4NO6Ujxajj8cpnq4RUg9Q3gr63GAKdJSZtUWi7N71tAelu5l2g_xGYfPnjqIMy1XchUnpVHNgvxrbroDunkuWxX0xbTw6xV6S75ng-tBOaWbVwwuzsS8yQYWTDZl9pehYG4OcS0ZN088j0CYpQ_CPam225FQonz_H4VVVQMOBkwh4_vsHspSZtz88X5VpZS_n11Q3Rm6OdjvqSCWN4ivlOwW0TgmMVuSHHfIVVfC61bufZllnrXyOwmPKM4yomQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=eB_7g5PZsBdZBV-qB01yWVzkJ1eGFZ5IYohaEMuzRuWEoaMWUfo-gAsvSTBhZlBVZSTFlAIes1NaR1xkF6UD_JJ4NO6Ujxajj8cpnq4RUg9Q3gr63GAKdJSZtUWi7N71tAelu5l2g_xGYfPnjqIMy1XchUnpVHNgvxrbroDunkuWxX0xbTw6xV6S75ng-tBOaWbVwwuzsS8yQYWTDZl9pehYG4OcS0ZN088j0CYpQ_CPam225FQonz_H4VVVQMOBkwh4_vsHspSZtz88X5VpZS_n11Q3Rm6OdjvqSCWN4ivlOwW0TgmMVuSHHfIVVfC61bufZllnrXyOwmPKM4yomQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.
‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6686" target="_blank">📅 10:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6685">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ارتش اسرائیل تپه علی الطاهر را تصرف کرده است. گفته می‌شود در تونل‌هایی که در این تپه ایجاد شده نیروهایی از سپاه و حزب الله به سر می‌برند.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6685" target="_blank">📅 23:38 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6684">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">جی‌دی ونس در خصوص ایران:
ما با ایرانی‌ها مذاکره نمی‌کنیم و تا زمانی که آنها شلیک به کشتی‌های تجاری را متوقف نکنند، با آنها وارد گفت‌وگو نخواهیم شد.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6684" target="_blank">📅 23:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6683">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=lXZ2MqO28Bbh3wVqfzY6gHvf7i3OSYLdjdF6xCmXzBaJWnh2NYRCFz9jvKUYCuyea8A7ywAIAEgD1Z56n4JY2ew2e2BoKvRcxzSjBXTABtxK4Hk7O_Z2YvDVNeCjaL6DA9pv3GRBjLlv4S_pg_VcJUknptMvhwrrJxXAFErRs3Ws9KQ4kdwxU10sEESVz7yvsJlBfn0FcxAHIdInTBP16hluTKdNlzqKw1zkMy2J2YxVAyEsdh0qmGBxuhGM_vEb-P8b2iknSiKYNHy59Qj6hz839x3Ua1NNXleg2r_iC08urPJ5_MP8bl-Bq_5e-7qqhtfY9tQSFcLddglY1RwRSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=lXZ2MqO28Bbh3wVqfzY6gHvf7i3OSYLdjdF6xCmXzBaJWnh2NYRCFz9jvKUYCuyea8A7ywAIAEgD1Z56n4JY2ew2e2BoKvRcxzSjBXTABtxK4Hk7O_Z2YvDVNeCjaL6DA9pv3GRBjLlv4S_pg_VcJUknptMvhwrrJxXAFErRs3Ws9KQ4kdwxU10sEESVz7yvsJlBfn0FcxAHIdInTBP16hluTKdNlzqKw1zkMy2J2YxVAyEsdh0qmGBxuhGM_vEb-P8b2iknSiKYNHy59Qj6hz839x3Ua1NNXleg2r_iC08urPJ5_MP8bl-Bq_5e-7qqhtfY9tQSFcLddglY1RwRSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GMOyHWir7tVCjyxjunBMLoRsL6_8Ke_5ZQugFXgzVG_LqdyVBbFZh8LSTBffUHk5SxKLTHWpjJhL-Xi1G1PlPW0BMM0XnuRtz0pbmg0eqswIilk-hEmYTNYl2nqWn2JdI0qD9T9NYqVZPiz70uZw2BJqUdx_9vMx6ow3PqA3QO798aFGCn01qh68Wbkm1h8uqj1orZ3slS-hPPnWXxQo5PtaqGdy_hJm2rEnu6t05oyP8hVy3MtO5BsXFvckhXXk_RODSpwF7bsuzHRKNzp3it7fLLpJjSKT320beZeSRxxgO2BfxDh2ci_SJ5d-z-BNqDxXWAeqoORIDpeSwPwbiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KnSUMivbeqeyFeMTlR22TtmP1fm9cRwEHuYI3qzYx_jMdwqhekOCiq1NeeUBHReMmAQbUr-zYmSfpkzegc91gbRz7Tu65QzK1DsI0ismLYpFOTsKp3w91LSsO0ncC7zb-bZPfUIVW8d-9yrcXTPJC64-B9hZYJh-igmK5Gt6E2OiNahhq9zoBZlG7rstYgI2lsp1v3JkDxHj3x5Nz3xY5SlVMJlzk6oMV-HoaAZEnUMZe8P7CVIhk39nT3etg6-Vgsgev55pPXhu3CRZuCKiejXXAQVVvcHp_zVjoE-Z9LvyKbVjE7pN2M9J3g6OYmICZM_TDMY6WjW461MmJfyxUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KalJFTmPT3423Eo4qrquMkBnwRWqEax8SjrVw1xkMrxc74yjMV8-2XWoz23j-eaA8hy7rw0GKp479iTS-iGiL_sfr8yh8Q3ADf2gd1yIDrkl_Cu3X85Go7DGrJ1w-WY-MXNaITaGNjqfbpqAxskNP8PDNCK7Liev4_vtLESIqeFb9kmwibmBasyLsRzqPrGiEK8AmkXPRGBZcXx1rUSBxEl3u5pqRpEjDhV9D8KdSGxzcJShBxu20F2_7OUdkZcYtaPu8MZkBVaV5Ae-RHl3qxbEXiOu757mf4GE5Ka5QnBSvjzgF0ehYLvkFL6rzxBCIHngoGNGcjeCtXr9Gk9Z1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا بزرگ‌ترین تولید کننده نفت جهانه!
آمریکا چهارمین صادر کننده نفت جهانه!
آمریکا بزرگ‌ترین تولید کننده بنزین در جهانه!
آمریکا بزرگ‌ترین صادر کننده بنزین در جهانه!</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6680" target="_blank">📅 15:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6679">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
مرکز رسانه قوه قضاییه: حکم ساعدی‌نیا در دیوان عالی کشور تایید شد؛ ۱۲ سال و ۶ ماه و یک روز حبس تعزیری و مصادره کلیه اموال و دارایی‌های منقول و غیر منقول.
اعدام، مصادره اموال، کشتارهای دسته جمعی و در کنارش روضه‌خوانی و قیمه است که اسلام را زنده نگه داشته.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6679" target="_blank">📅 10:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6678">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">نتانیاهو: ما جمهوری اسلامی را سرنگون خواهیم کرد. این نظام سقوط خواهد کرد. تمام نهادهای ما در حال تلاش برای سرنگون کردن این نظام هستند.</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6678" target="_blank">📅 23:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C_sXHYLdQAXXvVranV-Kq_BvcaWjcy4T5qb64JbXqxW13oNg4ZJi0XSpka_RuuMKndaFgdFHfrrOWRk8d76o02hJqMKKq7gUD0Ax0xXpSb_XJDHmuAAhQ6H7wcW1iafAExk6ARs346UuTck6vP2UyTIkaIiBWH_BdvMyXTs1sT2nhodrqK61HtN1hHJlskqGeK5ZLJ5wo2M7Z5l6Ya7Fshv6NmmLHcXbpYQ6K1ZoWyg1G7W-rqmA-D20j_faVLcby-Akh5RlaK6_HPD-bR3zHHTVqqie2t3Pew0bNMmSfkTCv9WxQsNPPyjLzoL-Ay0F3k7CW7abIJYPel2MX_-bpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از پزشکیان
حالا قالیباف هم از آمریکا خواسته
تا به تفاهم نامه برگرده!
تفاهم نامه کی شکسته شد؟
وقتی حمله کردن به کشتی‌ها!
و گفتن امتیازهای بیشتری بگیریم و غرامت و پول از تنگه هرمز!</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6677" target="_blank">📅 19:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6676">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p6DAfa0LC5tYtj-maqU0ZkEqX6T_ZHg7FlwzTET2dvP3TefxZPjCEJO1ZGAlnXFrw2wolGfXFtILV95aWUTfqk7BXll4PhKR84bZ9M2uPtYrxA6mN-Fhzh0Iwd9O7DvnPfjcX1480xwPRAutnTFYLKnPlfTG0CMvYm7bhFvoVQgRnEZyrTA9YUOKn7HEWxJ10Nf05O1XfuSA41AG8svpaCTqLOkoDphMV9JU0a2iJyLod8zFf4ne5mxUARF549NDupyIutWfQ-5-9bTXL0egbahoHUkIyzgSIxu2JW1xgy-FT6jHp5Fu6MYEJgPSMvMYTm5mXzysLeRNzeiGFYBzXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6676" target="_blank">📅 14:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6675">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
یورو ۲۵۰ هزار تومان را رد کرد!
دلار از ۲۲۰ هزار تومان گذشت.</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6675" target="_blank">📅 12:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6674">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jYir97CgMnfWQhPY6bXMC9QMCSw6RXo2zE1nQ46wSaTmXo0LOSS93UzfJxjWD-p_aKbna1Z2L7RRfJyENijA32WERnlIJ3eazkf01vq5p43IC5_socuXakaKZEwQI5S4NjlpFOT0lwlnuZmqmN58hNgeRAY81Tc8DXx-VmZd8naNh47tA2_vl-a7JzWtIiSQea5fPy6uKUqSL82RoEzWFDj7NkMh5QoshgwU_c124t2Lo7GojLeIZMMoy2IONc938rKUdkwXKDx5G-kWMZJdCy0SOjpZVoYX3vjRfE1Y--1i7UfZADPs2yWz3golfCFYIvuDCTX-uWAxh_rirorf2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aGRsetaldASJDWgIY-vW7Bc6YCIw4chs7GR-vt4DQ1h8FrIg8CP6U025liC62jzV8YPwZ-AiJ0BWisc_asgv4Uc5r1J0ZViMO2Hq2IG08-KTsv8Sk-S6Uc0BpqARQo05Kii3sXlY-_UabDW-ZtLG_PZ3BI1f9unqAv5vnRIduyJ7JhcUCNTAOHBkU70Iv0xHWu20pDLO05GUesQ6URngC2FHEWTUcOha3kDpMlcCTswL59_0tbuOtChgB7mT_3CgekzbSysbDjejwQZ2BV-LpweVnepGIJ4KNSccDCF_l6Vv_HfL_gzC2y9N_14KpPsFgaJ7GUnMLCj-0ywZTJrqDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DLJdyFxXTXemmNlYmf3z5zr2TDghWzviUoMqagftRjlobFWatXfwtykgxCLFkX9hp7yB-UAJHkLSQvGudd6AfyWGVy4Y3R8yV0dxyuLQDCyK6l0jH-7AoGghNoNmTFzGbwTmgWravFDeo-cPr1mWLfHJszyzhru2WbvaoSGr9ldq7nshdYf4U2PoSmNB4g3Rt1b16YlUJEZKYfclzdoEOCXC4iABTG_tVgWZR3AiDzbCdygpJiLywLHy8LzpQQTp_zDZMsopWtkbE62VOwPrsPtvazS0HqmegQJoqI0KZvPMS0lN6a5ElS6yQzAOnUc29ka45WIsQLXwRcIDLJvGdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J970Dz8U8lAEbAiOBtKp5OQft6SAR0oXmWYjD5T2fHiwTJ8EhBg4G3on9ItprdUnBTi-oa3B4tT-vSNKxA2qkWPHYH-F1_mF3yVDY4ZMBZJwOirODDmCvuKWWt0_77khri91LuWjlVUVU8mBVuaLe5Pc-zhz7Aa5-HxaNvADwd2aYzW_zI-z-4nuznHDCKGaT0JgvsMT79Qfwi8fBbbnY1aUXObhgFsPqtNCvGqn6lExgn9CdFWEkdimwXU-hpscCJHpP8lFI8yD50OuGahUchzb_-kv7hJoNxQ5_NY3v0sDOXie3KK-XEGZ2JEMYrk6ATO3z81A7zkHH7FXq6ulcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sHC9YW-KDpCih9a5YszG2pV6yt_PZeXFUNsOfyEfXLLTyaI3DQS5UkH8WN_vXUy136qeXLUOR8HLuGOup96zKxNhPONw-WZMRh5UNj1nBD6fbwzCRkDm4GKkgNxbbjYA0E2ZVWUrcewceqPfAas7o5XC6hFJiEva9iFUmv8rqzzcWBrEsmEctVGJ2hwAjItTn4nSYXKhXLjRNR4QXdbbA-WV45NrRE5B4sXCiIvYHAFrjACZ7Q7PI6JE8wmPQxPFBrsTt1IXYW6S9edzGUSplzyWebFlC_7LdOqrDY-9nzG09jxvGmdaIItGyIYY4cMqI_MdRRkNcWudMkMzGp2NNQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رئیس جمهورچین  حاضر به نشست
و دیدار رسمی با پزشکیان نشد،
به طور معمول در حاشیه اجلاس‌های مهم
بین‌المللی، روسای دو کشور در یک اتاق و در حل اقامت خود با یکدیگر دیدار می‌کنند.
(مثل دیدار دیروز پزشکیان
و نخست وزیر هند و یا دیدار دیروز پزشکیان با پوتین)
اما رئیس جمهور چین، فقط سرپایی
حاضر شد با پزشکیان سلام و علیکی داشته باشه اما نشست و استقبال و…. نه!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6670" target="_blank">📅 08:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6669">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔴
حسین مرعشی دبیر حزب کارگزاران سازندگی:
«چینی ها رسما به ما گفته اند؛
۱- تنگه را باز می کنید.
۲- عوارض نمی گیرید.
۳- مسئله تان با عربستان را حل میکنید.
۴- مسئله تان با امارات را حل می کنید.
بعد از این آقای قالیباف می تواند برای دیدار به چین بیاید.»
نکته : چین در ۲۰ سال گذشته کمتر از ۵ میلیارد دلار در ایران سرمایه گذاری کرده، اما  حدود ۲۷۰ میلیارد دلار در کشورهای عربی سرمایه گذاری کرده.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6669" target="_blank">📅 08:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6668">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
۷ کشته و ۸ مجروح در پی حملات آمریکا به خوزستان
استانداری خوزستان:
در پی حملات موشکی شب گذشتۀ دشمن آمریکایی به ۳ نقطه در استان خوزستان، ۷ نفر شهید و ۸ نفر مجروح شدند.
🚨
دولت پرو روابط دیپلماتیک خود با جمهوری اسلامی را قطع کرد.
🚨
در جریان حمله آمریکا به کوهستک هرمزگان ۴ تن کشته و ۵۰ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6668" target="_blank">📅 08:18 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6667">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">نیروهای امنیتی اسراییل (موساد و شاباک)
با ورود به نوار غزه، رئیس دستگاه اطلاعاتی و امنیتی حماس را ربودند و با خود بردند.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6667" target="_blank">📅 23:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6666">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=gvq_rnOPDz2LaURnA0zA29F4VZh3tk2kzrE01BaInUGxOvvVoMFlSvBpW0HBmOEYPv40oJS2vTKRsLn68FPyH7wcoLlHHHi8N3nG0MUdOV6rRpaxLks0paJvo9yPgCXRc7v3nMhWtdCohX9REzdPG4vl0Zd6bXrMuSHamU-5u1Mp8sk-uEdNJzS6VBzlpMX6EafOBh1nVZqqy0j3yYqQ8CUuHuGKRDENiqDi7BP536ByEWCvleiaYUsbS06S9T6V9z41ctMG2ZirORqTmiNI99-SypW64_5bNhAPEFJISdRDNOsNt4um7ogmkGcC-_9_Ya7Vd9XfNXmZ7H4maXxnfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=gvq_rnOPDz2LaURnA0zA29F4VZh3tk2kzrE01BaInUGxOvvVoMFlSvBpW0HBmOEYPv40oJS2vTKRsLn68FPyH7wcoLlHHHi8N3nG0MUdOV6rRpaxLks0paJvo9yPgCXRc7v3nMhWtdCohX9REzdPG4vl0Zd6bXrMuSHamU-5u1Mp8sk-uEdNJzS6VBzlpMX6EafOBh1nVZqqy0j3yYqQ8CUuHuGKRDENiqDi7BP536ByEWCvleiaYUsbS06S9T6V9z41ctMG2ZirORqTmiNI99-SypW64_5bNhAPEFJISdRDNOsNt4um7ogmkGcC-_9_Ya7Vd9XfNXmZ7H4maXxnfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها یک خودرو وارد جمعیت حامیان حکومت در مشهد شد.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6666" target="_blank">📅 23:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6665">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در بندرعباس، کنارک، چابهار
سنتکام : «امروز ساعت 12 ظهر به وقت شرق آمریکا، [حوالی ۱۹:۳۰ به وقت ایران] نیروهای آمریکایی حمله به اهداف سپاه پاسداران در ایران را آغاز کردند.
این حملات پس از حملات اخیر سپاه پاسداران علیه کشتی‌های تجاری در تنگه هرمز و علیه نیروهای نظامی آمریکایی مستقر در منطقه انجام شد.»</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6665" target="_blank">📅 20:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6664">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O5Ts52zkSAq2WycQN7SL7q1N09eOUM8D8SaoZKiELxhSGHjSrwBd0PhmSkLUMqY23vtnNe9MGlIxYdbvPxaC4GtMJS1S2TFQscAYXgqjiglxuhG16SYjqnOwxELAzWUBoI4g0tJxUv5NrEaab2HogTsi1mSpcErXmkcjhy2Kglp6cSgQJIj9Pg5dYWP16vTLub9J42VuXm0AUo7p4zRZw4f6AotbDbne6apv-m0PpASZTvP2s-zhC9ZDp7EfZShpUqFMueO_AJ-EDIfm-MtAzBDT-nSNPAIQvS7CZ-0ywfVtXEv4jM82FyPIBx1sRr94uxaBUrPzH3u9BnPhozqgOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه شورای عالی امنیت ملی!
دستاورد تازه : حوصله آمریکایی‌ها سر رفته،  یکی از معاونان و زیر دست‌های وزیر دفاع (هگست)استعفا داده.
حالا این سمت : از رهبر گرفته تا ۵۰-۶۰ تن از فرماندهان ارشد و وزیر دفاع و وزیر اطلاعت و … کلا کشته شدن!!
تنگه رو بستن قیمت نفت بره بالا به آمریکا فشار بیاد، الان کشورهای عربی نقت صادر میکنن خودشون هم‌ نفت نمی‌تونن صادر کنن، هم مجبور شدن بنزین رو گرون کنن و وعده خاموشی‌های بیشتر  و… میدن!</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6664" target="_blank">📅 18:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6663">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">‏ پزشکیان:  اینجانب به صراحت می‌گویم چنانچه آمریکا به تعهدات خود در یادداشت تفاهم بازگردد، ایران نیز بلافاصله عمل متقابل خواهد کرد.
خودشون با حمله موشکی به کشتی‌ها از تفاهم نامه زدن بیرون، گفتن تنگه رو بگیریم و بهای نفت رو در دنیا ببریم بالا و فشار بیاریم به آمریکا و ترامپ و امتیازهای بیشتر بگیریم،
الان افتادن به التماس که برگردیم به همون وضع!</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6663" target="_blank">📅 09:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6662">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
ترامپ به فاکس نیوز : به حمله شب گذشته جمهوری اسلامی به پایگاه آمریکایی در اردن، به سختی پاسخ خواهیم داد.</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6662" target="_blank">📅 17:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6661">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sqdztqCM9veesVBr073y3OcZcUs0iu1L4nuTRxP5-bocJCrrvHc5lETt1e6iWkTsIidYViMog2YBh8fEtzMZWfS0ZoTIXNh29SpeLd0XYHd-LCq01E0OhjfNQUBxPIT-LmWt-MPNELd5LWtF8shgjmAFmltRtJuBu8ZZ9Lez9EvrFaMNkh-gJ_VuoDaAF2SyvmuJqW0VHxjZw_Z6ZHTmKtL1v2_DeV45duErqw1ds3E50-V_M5yHtF4qIJTaKlXFfm9noUfymkdopF280oUdZm_so0vmc-M8wDLP-p6Lhe-fgTXis65005Vq08IjGINzATV9OMEx8cGkjVrIBBWH6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=P1deSXHERYsCmGKn34zEwIvfa1ppivTf_GwGva2LFd2v8sKAUOMcG9VWYOUXdorO_p64L2ckqf-bdsCb9pSa2gAZ3zh6TqKOW4ISugB0X3A8M0sZiWDs78L1gue0GyLeDlPrhm_Vt5x5mAJX_qSAhCOuiUDXs91VPB-xUqq0S4cG2g7JFMeYJOXYA_J5MRUM8JXdRJwHrRAhLCP7nOAH90Rtg65c5zqWe4W9JKhKbIll9SNMLcM8L_UHNH6j9AZI92n4qC-VESai5_YAV9TV6RmqzNlrqHG0Q_0fUcSDrTx7es7zVC4OP2e0BqJqHFrWsF9TD3A5URX8iR5U7tYz3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=P1deSXHERYsCmGKn34zEwIvfa1ppivTf_GwGva2LFd2v8sKAUOMcG9VWYOUXdorO_p64L2ckqf-bdsCb9pSa2gAZ3zh6TqKOW4ISugB0X3A8M0sZiWDs78L1gue0GyLeDlPrhm_Vt5x5mAJX_qSAhCOuiUDXs91VPB-xUqq0S4cG2g7JFMeYJOXYA_J5MRUM8JXdRJwHrRAhLCP7nOAH90Rtg65c5zqWe4W9JKhKbIll9SNMLcM8L_UHNH6j9AZI92n4qC-VESai5_YAV9TV6RmqzNlrqHG0Q_0fUcSDrTx7es7zVC4OP2e0BqJqHFrWsF9TD3A5URX8iR5U7tYz3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت بازار تهران و اسکله متروکه شده بندرعباس</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6659" target="_blank">📅 14:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6658">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ظاهرا مشاور قالیباف،  «قیمت پوشک»
و «خون خامنه‌ای» رو توی یک جمله گذاشته
اینها هم ناراحت شدند.</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/farahmand_alipour/6658" target="_blank">📅 08:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6657">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=SV3V5GuIiEVvY5udd61obo50ULghSR_QlxGxBDj71Yws1R_p2kKYnDocMam2MMDUiS2EwEIeKgrvJcirFyDwLkeiH2-b9F3eeiFyeII2L6L7WsnoGNp3Sqcz-lhKMb4aYXSuU3fdxKiDOuxoYz7UmWXVXwt13Ij4O-1KQ71wmi2ufFM-ku-TmemakBMNXldLr54YYB8Cc5sDk5oxAVgXHX2mFDiXDPqCrq_2YDFvK9nkeHRUzzTfVX7l_Rw8drvrG8fqqqWmirTTJhzkYjG09P3GKP3sdt6gjkyz0llKA2o9hdc9uSAzMBOxKcRjnC8PuLBE9GzBA8bnxdcjn8MLcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=SV3V5GuIiEVvY5udd61obo50ULghSR_QlxGxBDj71Yws1R_p2kKYnDocMam2MMDUiS2EwEIeKgrvJcirFyDwLkeiH2-b9F3eeiFyeII2L6L7WsnoGNp3Sqcz-lhKMb4aYXSuU3fdxKiDOuxoYz7UmWXVXwt13Ij4O-1KQ71wmi2ufFM-ku-TmemakBMNXldLr54YYB8Cc5sDk5oxAVgXHX2mFDiXDPqCrq_2YDFvK9nkeHRUzzTfVX7l_Rw8drvrG8fqqqWmirTTJhzkYjG09P3GKP3sdt6gjkyz0llKA2o9hdc9uSAzMBOxKcRjnC8PuLBE9GzBA8bnxdcjn8MLcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZkmqpZfeFSwnu2OOL9lAYFisZ7JwFzS_i5kFkdX6bY8ulgKLotpo-0u5YDqig89_dje00f5Kzq1TxSm7_tFuChlsNUOR1hOBrMEUbWMlN5yPWSa_rTYBM6ciVHI3RSb7xPJkT9pQ0wzIgXGtnFGH_rclEo_3p1lJN7XOmDwlf0uD55oAXjEy0I0o22GfHiAJ0shO4uQU9-r5V7uHx0vACwEJRe740awh80U-1q_ibfu7ep2S1oT76K3WfTVC8D3HhRWCV09vgTBMZq41CgkCkJ47K8Irs6iIgW55GZS4PAp-VNSfVocamyLNgjkCz8EeNRE5IikKpQVptR1g8TRzwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ رو به بهانه خونخواهی خامنه‌ای راه انداختن
۴ هزار لبنانی کشته شدن
از جمله بیش از ۷۰۰ کودک لبنانی را به کشتن دادن!
قالیباف رسما و علنا گفت
«برای جمهوری اسلامی» بود.
بعد دست به دامن دنیا شدن،
با التماس و با تهدید به جنگ با اسرائیل
و با قراردادن «پیش شرط  شماره یک»
برای تفاهم با آمریکا
در پایان دادن جنگ لبنان،
اینها رو از زیر چک و لگد اسرائیل کشیدن بیرون
حالا اومده میگه ما فلان کردیم!!!</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/farahmand_alipour/6656" target="_blank">📅 14:47 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6655">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UiEr2v56QduHW99hbR4e0OWHNUkdFKCkAEmgCg4ghOa3QhRRfGzWpQ4c_lpXyeAVMaO6drbuWwHPxCEOJKrAFQypNKcP4nXxzWOyZTVN5ViMO9S4rZnWfApIy0z0lRLFDE2rjWPmUerM2bebow23hGzdepgQBrgWd5z2R8iv6CGOrwaz6HFBITin05BoOlqIHlqD4Acb4cG3Jyj4vZuKV2QPnWCaR_pKVZyz_WGgDDKZMw1vacIymRxJllmLDiM20dwTzULtTIflAPxx7wcwNMEt7JyFxhIK8DACMq1X-KmJwGhiS7vU378o5CbjeFBiticPCP4hA1_O57LdvX6bSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صادرات نفت کشورهای عربی
خلیج فارس در ظرف یک ماه، دو برابر شد.
جمهوری اسلامی تنگه رو بست و فروش
نفت خودش متوقف شد.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6655" target="_blank">📅 07:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6654">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">داریوش، در لس‌آنجلس روی سن زنجیر میزنه
محسن نامجو در ونکوور کانادا، سینه میزنه
دختر بی‌حجاب ایرانی در کانادا روی
ماشین قیمه عاشورا نذری میده.
ای آخوند فرورفته در مغز استخوان ایرانی!
روزانه چند جوون رو اعدام کنی، ایرانی‌ها بیدار میشن؟ چند تا جنگ و مصیبت و کشتار دیگه باید
سرشون آوار کنی، تا بیدار بشن؟</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/farahmand_alipour/6654" target="_blank">📅 19:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6653">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s2bCfKX8OsMWLaiHiJSx8AA3H3_sS9KGBq7osdjzJo0YSTiKZRRldwH15tWx00Vneycfj3N2QNE42TDZ1yYScf7yPgHXm3u5aciCCs4hFNoYJktcTSbqkvfjOBKndNT8ydWJZx_yKeRn1fQMX4VdmCqquZjXrKdAbahKyBxyhY0G5MA8FQ9-efxIx0pvBJCd9j-uqVhP1r38S_nM81BXKkCwQXp-QbTbsmRBn05DrMQl7iG_FCK7lAV92KY2MaM-FEd1OU8ivfa6Bluq3Tuas5XbTujqOdRKr72MAOfnS3Ls3XbcXWBLLjbh5rWmg7rlBc9daG5WI-iQ9IK2u0Flgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از آتش گرفتن یک فروشگاه فیلم گرفته،
دادگاه گفته این اقدام «مشارکت در آتش‌سوزی»ست و حکم محاربه و اعدام داده!
همون حکومتی که با جنایت سینما رکس آبادان و ترور نخست وزیران و بمب‌گذاری‌ها شروع به کار کرد و قدرت گرفت!
بعد بگید چرا مردم در صبح ۹ اسفند
و شخم زدن بیت رهبری خوشحالی می‌کنید!
هزار بار دیگه هم شادی می‌کنیم
از مرگ و نابودی و تحقیر شماها!
هر جا که تحقیر بشید و نابود بشید؛
از غزه و لبنان و یمن و عراق تا تهران!</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6653" target="_blank">📅 18:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6652">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EpdF-Lolp7WbUwQ1vSz8IsellaoxZbmDHc1AuxVTcUVs1mbMULuH-OzWCsAx8rnr2NuQDKfAchUBX0uH7cqdTqODFbUmc7Bqin0o4gW17BuNpBjlw7fHYLSQKEiwUmGEZKduc3jlqNI82IQj2GGFuDWimLbk4fIvZC5WZGJQb92zk5mK2BzHADmZTP1MREpZUcRpHlqrHy4kT5yv_HOFYbeLKwDwQ-tQ4UIMDGcN1LTzbcYxvOjK2JujMhsXMmJJXOv85-IUNLYX0WCcqcQG69EUIXKShTqZErZtoTLADuj7b2EbZN3hJpKMfuT4ihUtctdRRXzyS8wtHIOD3gIfQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BMEhIB1cKQD8_x2bYvLrDqHvBWDvYGMhV56WFYpCnemBsHmQZyXW3zLp-H6dt-m9iKeI4f-WoGaFCtriEX95MzY4vG4pmbY3y15wGefEtkgQc0kbJpkRHdXnAJSNF-ADhX_VU159LGFFV9CMOKpC4BfKnPs6rzPilW8hhcux9ki5TYZurZMSpL8-xmcOl1_c4sMhtACQhOeo0HbeorB8BW1ElnCioWHOe6WaV1-G9b_n2_aZ_MHA2LcUAjLb9QuYEwZQvcVbCfrRbZSwb80E8dYhVO7FrXYXlbUusF8caf9PqO1yavJ_sjPo9kOhaMAn4TysapAuRDNL06OF7Wzc0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bsrlXFJBXbLYGqWc48V7QWFwHrxKftbfLrvie6uEdZ8U8uTo3bsbPS3wdXrs-KtAlgi7NSdJ9RL5FWcqg-yQFyROqlPph7Urd_avQ6FyU22j2YMfGzHSeQuBW6-HQMH8vRhGUOJaroGIk1N9Wf2RXT10lFLFfe3KxtpFQimkCuWgExCFdtDJucsxWXYFlKVWJrg5dR8aH3_pLXbWhLqL96a-iWugSDt0EIIiVY5UzWG29IR67cM8Vpc-74SQ6p2I2dpw_3BhELXKHp0OoaPzK_WGBAIgidZ9RugL1oIZRQNZa1CA-WQN3h17avTKpMh9xmnd0ztX3nIPJHJDBAF6tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rVorTRByhJvL523gK2LPHhMM9GjSNjA86Di64A6Thtz8WPPAHEAaZuceFp7aPozftyajxVx2sVTLrKeuud5jjUE-N5WMXa9sgI0DJ1VZExw-g6TNBXXVt7QCy4YfkV6CI89HO2Qg9U6celiMgH2lfhiig9KlfYsUhK8uSCLq2ovtIvbLhN5UwSUkd6HoqtAznd8q9jIyBYP5THfec8a8WAFu2CcK2PrH4ibI839rvIUXehWNhUUz6QEvb2Htv4W1BR0prTvaUDErpMHdfXP2ufbB8HC3_qXp1hFgoqQ6ywTQRfKrfl28gePtvmnfpIZFlUElIdSYoTcHhEZdNaM59Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d0zSpzn2lwk0a-HeOHfPM5a9QFvA6YVCngC_25cAhfQrMoD0rs8nWz77LgD5JnnFjSTkmjC2MNzIoO71yhnULX0xbLuK6E9DZVc8vuEDddswcZZp27RCd1DjOF5SUHYxSh_SnCEoj1k9GYQTFEEvtADomHLO3ZLx2L9WWPQrcynzrDjU1zjP3okbSet72-Dvg1fZrNx-AzDosDOkazR-Kn77n2vXB8vywcvvQWYn329Py53oHBkGe9oeRNou6CuMbUF9Ciay-1faS2ZWwBDsXBdi3ja2WP1iDZMV2WTM5u_j0JJP8kJNn_n4uZYU8QxgHissRFYTUd-yj3LEMzpgOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی،
دیروز به عنوان رئیس هیئت مدیره
دیجی‌کالا منصوب شده!
نام او با واکسن کرونا گره خورده،
او سخنگوی گروهی بود که مخالف واردات واکسن بودند.
رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و برای ماه‌ها
مانع از واردات واکسن شدند.
تحت هدایت رهبرشون خامنه‌ای.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6648" target="_blank">📅 09:14 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6647">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=euw6-a_G5jhXsIFAbRltL749A0VdCftqk7soQtEXa4VNPbZUsVDTXyIxOnbT3SMD_aB5pOyWPyImhweswLiiKJJauYTJ719epti2kEJ-Wlv5Qi0RMMJ75hvdUNbKnGhv9jJzypVnWJkTpNQT7YBVbQ-jIxlyTmseqrLoWs5mpZhUfCd-OpAN8yxXO1_jpvIcKyDFRmYL2gs-3URy9QyNv6nRrzwqpvRWhAuDkO4DytEWhfoxHsU7DY9tG-jLTjQel3MCb_2st6Q0yM7I-gJC49qWHzXjJjxjcnwMtAseLL-hFDkn8kWToFkM2eY3_hq-MDXvHfh-0GwbYhp7O5AIwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=euw6-a_G5jhXsIFAbRltL749A0VdCftqk7soQtEXa4VNPbZUsVDTXyIxOnbT3SMD_aB5pOyWPyImhweswLiiKJJauYTJ719epti2kEJ-Wlv5Qi0RMMJ75hvdUNbKnGhv9jJzypVnWJkTpNQT7YBVbQ-jIxlyTmseqrLoWs5mpZhUfCd-OpAN8yxXO1_jpvIcKyDFRmYL2gs-3URy9QyNv6nRrzwqpvRWhAuDkO4DytEWhfoxHsU7DY9tG-jLTjQel3MCb_2st6Q0yM7I-gJC49qWHzXjJjxjcnwMtAseLL-hFDkn8kWToFkM2eY3_hq-MDXvHfh-0GwbYhp7O5AIwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات شاد جوانان غیور مسلمان</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SrNA9iNTgEQt2HsKhdQTJ6MFt3ThbT8-GkgUqq6-qyIWFJtSXgDlae4qi7C_JSy2PQzTahFximvdZetEWc3eewuKciF4t8ak_nMwcfrpZ3KaR7AZoxi2RRXG7fBHwqKnlsgqc5iLIPSPWT1WjfrY7iarPGiPJDZmxibIYuy5TEHrp5AdheVM65bGdlCdJyubK0jdV2G6qpYy-0coMXwgwsdaEiCJUzAmPhJIymjn8CwppEkRihH37dUH5vc6awThKdNnM-O0Cad_m5SbLnXYWsOOlX_R7hyQ5vnforvtj3ZrSKDDDW4BmnsXiyFxmAJjUtvDIJIOpqTaYaXDsWTggA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6645">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=Np4hRpI_Em9gfUtPslpx9PAmNlU2phqlf17YWANUbiYREBXpQW7MIW29KI4-y-5PqIWPB14A6moLuOTXQAxKMNTS36V1ZT3ueCqpGHQTkq5Z_uRewE6w1aS_Jrz9h46hRpQQYw0Y_EHwVjkXdo5GYqzUYNVUeB1iFtyUyXyGtHKdYAL5WTb0_UOHZv_20yRYh__wWjUUw_X4GwFUXQ9TQWytadJNtPPRT9jF_o-mfS-IMPycxJ85CiJqJYgP3qTP3jpUlfRqryeZ81kANeJL51Olt7nYkUEUV9U3HAev_zt81nECDoVVf-n_MkcneAam190plo3UPRUeH6TUZkSFaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=Np4hRpI_Em9gfUtPslpx9PAmNlU2phqlf17YWANUbiYREBXpQW7MIW29KI4-y-5PqIWPB14A6moLuOTXQAxKMNTS36V1ZT3ueCqpGHQTkq5Z_uRewE6w1aS_Jrz9h46hRpQQYw0Y_EHwVjkXdo5GYqzUYNVUeB1iFtyUyXyGtHKdYAL5WTb0_UOHZv_20yRYh__wWjUUw_X4GwFUXQ9TQWytadJNtPPRT9jF_o-mfS-IMPycxJ85CiJqJYgP3qTP3jpUlfRqryeZ81kANeJL51Olt7nYkUEUV9U3HAev_zt81nECDoVVf-n_MkcneAam190plo3UPRUeH6TUZkSFaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: محتبی خامنه ای رهبر ایران  به‌شدت مجروح شده است، سمت چپ بدنش، دست و پا و در واقع تمام آن قسمت از بدنش به‌شدت آسیب دیده است، فکر میکنم او زنده است.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6644">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374629de87.mp4?token=ksDaRNt_b1V6oJWAt6ewh4m6ZAjTH-5FGxQbtOy9aug5SRk1UInmuPkVFykQHROjqemEm_ODPUx9IxqVRDSkPjeYpb1ibtHkQbby17ob6UE0NtcweAkIzl2BFT6RnFHliu6VIjJ-55qQg1ixj4ncXSXijQIjOljcgnkKT39E9F_usPc4efjDrOQ8sPO_yzCukSCdBfDYkuqHOdhARpCwjGX7HHsPJyyTITOocwVJchh6pgQH3iMT3Nyrc4fx-9gkB9rx2EWbSX6PNKL4ik4Tt5tDreog_28w4R3VFOfyDzBenxfIIoiABKSwwmRJxHpSlrPAMsVngXPDZSVpLASFrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374629de87.mp4?token=ksDaRNt_b1V6oJWAt6ewh4m6ZAjTH-5FGxQbtOy9aug5SRk1UInmuPkVFykQHROjqemEm_ODPUx9IxqVRDSkPjeYpb1ibtHkQbby17ob6UE0NtcweAkIzl2BFT6RnFHliu6VIjJ-55qQg1ixj4ncXSXijQIjOljcgnkKT39E9F_usPc4efjDrOQ8sPO_yzCukSCdBfDYkuqHOdhARpCwjGX7HHsPJyyTITOocwVJchh6pgQH3iMT3Nyrc4fx-9gkB9rx2EWbSX6PNKL4ik4Tt5tDreog_28w4R3VFOfyDzBenxfIIoiABKSwwmRJxHpSlrPAMsVngXPDZSVpLASFrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رژیم گذشته‌ همه همت‌ها و توجهات این بود که آدم خونه و ماشین خوب داشته باشه</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
